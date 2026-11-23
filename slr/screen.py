"""Screening tool: title/abstract passes 2 and 3 (protocol §4.2 steps 4 and 4b) and full text (step 7).

Run:  python slr/screen.py [2|3|ft]   -> opens http://127.0.0.1:8765  (default: pass 2)
Queue:       slr/passN-queue.csv           (records to screen; pass 3 from build_pass3_queue.py)
             ft: the pass-3 includes, AI group (a), (b), (c) order, with a view extracted from slr/fulltext/<key>.txt
Suggestions: slr/passN-ai-suggestions.csv  (AI suggestion, shown only AFTER the author decides; ft: ft-ai-suggestions.csv)
Decisions:   slr/passN-decisions.csv       (append-only; the last row per key wins; ft: ft-decisions.csv)
"""
import csv, datetime, json, os, re, sys, webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.abspath(__file__))
PASS = sys.argv[1] if len(sys.argv) > 1 else "2"
assert PASS in ("2", "3", "ft"), "usage: python slr/screen.py [2|3|ft]"
NAME = "ft" if PASS == "ft" else f"pass{PASS}"
QUEUE = os.path.join(HERE, f"{NAME}-queue.csv")
AI = os.path.join(HERE, f"{NAME}-ai-suggestions.csv")
DEC = os.path.join(HERE, f"{NAME}-decisions.csv")
FT = os.path.join(HERE, "fulltext")
FIELDS = ["time", "key", "first", "final", "ai", "agree", "note"]
ALLOWED = ({"Include", "IC1", "IC4", "EC1", "EC2", "EC3", "EC4", "EC5", "EC6", "Other"} if PASS == "ft" else
           {"Include", "Maybe", "IC1", "EC1", "EC5", "Other"} | ({"EC6"} if PASS == "3" else set()))


def read(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def ft_queue():
    """Pass-3 includes, ordered by the pass-3 AI group (a, b, c), then queue order."""
    last = {d["key"]: d for d in read(os.path.join(HERE, "pass3-decisions.csv"))}
    group = {a["key"]: a["g"] for a in read(os.path.join(HERE, "pass3-ai-suggestions.csv"))}
    rows = [dict(r, g=group.get(r["key"], "?"), ft=os.path.exists(os.path.join(FT, r["key"] + ".txt")))
            for r in read(os.path.join(HERE, "pass3-queue.csv")) if last.get(r["key"], {}).get("final") == "Include"]
    return sorted(rows, key=lambda r: ("abc".find(r["g"]) % 4, int(r["n"])))


HEAD = re.compile(r"^((\d+(\.\d+){0,2}\.?)|([IVX]+\.)|([A-H]\.))\s+[A-Z][\w\- ,:&/()?'’]{2,80}$"
                  r"|^(Abstract|Introduction|Background|Related Work|Methods?|Methodology|Study Design|Approach|Evaluation"
                  r"|Experiments?|Results|Discussion|Limitations|Threats to Validity|Conclusions?|Future Work)$", re.I)
TERMS = {"SDD / spec-driven": r"spec[- ]driven|\bSDD\b", "specification": r"\bspec(ification)?s?\b",
         "AGENTS.md / CLAUDE.md / rules": r"AGENTS\.md|CLAUDE\.md|cursorrules|copilot-instructions|context files?",
         "SWE-bench / issue": r"SWE-bench|\bissues?\b", "benchmark": r"benchmark",
         "repetitions / runs": r"repetitions?|\bruns\b|non-?determinis", "cost / tokens": r"\bcosts?\b|\btokens?\b",
         "human developers": r"human developers?|participants"}


def view(key):
    """Parts of the full text for the decision, cut mechanically (no AI): headings, contributions, method, evaluation, conclusion."""
    path = os.path.join(FT, key + ".txt")
    if not os.path.exists(path):
        return None
    text = re.sub(r"-\n(?=[a-z])", "", open(path, encoding="utf-8", errors="replace").read())
    refs = [m.start() for m in re.finditer(r"\n\s*(References|REFERENCES|Bibliography)\s*\n", text)]
    body = text[:refs[-1]] if refs else text
    lines = body.split("\n")
    heads = [(i, l.strip()) for i, l in enumerate(lines) if 3 < len(l.strip()) < 90 and HEAD.match(l.strip())]

    def section(pattern, last=False):
        hits = [j for j, (_, h) in enumerate(heads) if re.search(pattern, h, re.I)]
        if not hits:
            return ""
        j = hits[-1] if last else hits[0]
        end = heads[j + 1][0] if j + 1 < len(heads) else len(lines)
        return " ".join(" ".join(lines[heads[j][0] + 1:end]).split())[:2200]

    m = re.search(r"[Cc]ontributions?\b|(In this|This) (paper|work|study)", body[:max(4000, len(body) // 3)])
    contrib = " ".join(body[max(0, m.start() - 300):m.start() + 1500].split()) if m else ""
    method = section(r"method|study design|approach|research questions|experimental setup|setup")
    if not method:  # own section names (e.g. "3 SpecBench"): first section after the introduction and related work
        rest = [h for _, h in heads[1:] if not re.search(r"intro|related|background|motivation|prelim|abstract", h, re.I)]
        method = section(re.escape(rest[0])) if rest else ""
    return {"heads": [h for _, h in heads][:45], "contrib": contrib, "method": method,
            "eval": section(r"evaluation|experiments?|results|findings"), "concl": section(r"conclusion", last=True),
            "terms": {k: len(re.findall(v, body, re.I)) for k, v in TERMS.items()}, "chars": len(body)}


def decisions():
    return {d["key"]: d for d in read(DEC)}  # last row per key wins


def save(d):
    new = not os.path.exists(DEC)
    with open(DEC, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow({k: d.get(k, "") for k in FIELDS})
        f.flush()
        os.fsync(f.fileno())


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, body, ctype="application/json", code=200):
        b = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/":
            self.send(PAGE.replace("__PASS__", PASS).replace("__CARD__", CARD[PASS]), "text/html")
        elif u.path == "/data":
            self.send(json.dumps({"queue": ft_queue() if PASS == "ft" else read(QUEUE), "done": decisions()}))
        elif u.path == "/view":
            self.send(json.dumps(view(os.path.basename(parse_qs(u.query).get("key", [""])[0]))))
        elif u.path == "/pdf":
            f = os.path.join(FT, os.path.basename(parse_qs(u.query).get("key", [""])[0]) + ".pdf")
            if not os.path.exists(f):
                return self.send("PDF not in slr/fulltext/", "text/plain", 404)
            b = open(f, "rb").read()
            self.send_response(200)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)
        elif u.path == "/ai":
            key = parse_qs(u.query).get("key", [""])[0]
            s = next((a for a in read(AI) if a["key"] == key), None)  # read fresh: suggestions may still be arriving
            self.send(json.dumps(s))
        else:
            self.send("{}", code=404)

    def do_POST(self):
        d = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if d.get("first") not in ALLOWED or d.get("final") not in ALLOWED:
            return self.send('{"ok": false}', code=400)
        d["time"] = datetime.datetime.now().isoformat(timespec="seconds")
        save(d)
        self.send('{"ok": true}')


PAGE = r"""<!doctype html><html lang="pt"><head><meta charset="utf-8"><title>Triagem __PASS__</title>
<style>
body{font:17px/1.55 system-ui,sans-serif;max-width:1100px;margin:0 auto;padding:16px;background:#fafafa;color:#222}
#bar{display:flex;justify-content:space-between;font-size:14px;color:#555}
h1{font-size:22px;line-height:1.3;margin:12px 0 4px}
.meta{font-size:13px;color:#666}
#abs{background:#fff;border:1px solid #ddd;border-radius:8px;padding:14px 18px;margin:12px 0}
.noabs{color:#b00;font-weight:600}
#keys{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}
#keys button{font-size:15px;padding:8px 12px;border:1px solid #999;border-radius:6px;background:#fff;cursor:pointer}
#keys button.first{outline:3px solid #36c}
#keys button.final{background:#36c;color:#fff}
#ai{border-radius:8px;padding:12px 16px;margin:10px 0;display:none}
#ai.agree{display:block;background:#e6f6e6;border:1px solid #6b6}
#ai.disagree{display:block;background:#fff1dc;border:2px solid #e90}
#ai.none{display:block;background:#eee;border:1px solid #bbb}
#hint{font-size:14px;color:#333;background:#eef3ff;padding:8px 12px;border-radius:6px}
#saved{font-size:13px;color:#080}
#card{font-size:14px;margin-top:14px;padding:10px 14px;border:1px dashed #999;border-radius:8px;background:#fff}
#card ol{margin:6px 0;padding-left:20px}
q{font-style:italic}
#ftv details{margin:6px 0}#ftv summary{cursor:pointer;font-weight:600;font-size:15px}
#ftv .txt{font-size:15px;background:#fff;border-left:3px solid #ccc;padding:6px 10px;margin:4px 0}
#ftv .heads{font-size:13px;color:#444;columns:2}
#ftv .terms span{display:inline-block;margin:2px 8px 2px 0;font-size:13px;background:#eee;padding:1px 6px;border-radius:4px}
#ftv .terms b{color:#c00}
</style></head><body>
<div id="bar"><span id="pos"></span><span id="counts"></span><span id="saved"></span></div>
<h1 id="title"></h1><div class="meta" id="meta"></div>
<div id="abs"></div>
<div id="ftv"></div>
<div id="keys"></div>
<div id="ai"></div>
<div id="hint"></div>
<div id="card">__CARD__</div>
<script>
const PASS="__PASS__";
const OPTS=PASS==="ft"?[["I","Include"],["1","IC1"],["2","EC1"],["3","EC5"],["6","EC6"],["4","EC4"],["7","EC3"],["8","EC2"],["X","IC4"],["O","Other"]]
  :PASS==="3"?[["I","Include"],["6","EC6"],["1","IC1"],["2","EC1"],["3","EC5"],["M","Maybe"],["O","Other"]]
  :[["I","Include"],["M","Maybe"],["1","IC1"],["2","EC1"],["3","EC5"],["O","Other"]];
const LABEL={Include:"Include",Maybe:"Maybe",IC1:"Excluir IC1 (sem agente a programar)",EC1:"Excluir EC1 (só funções)",EC5:"Excluir EC5 (só o agente deles)",EC6:"Excluir EC6 (passo 3)",Other:"Outro (nota)",
  EC2:"Excluir EC2 (especificação formal/RE, sem agente)",EC3:"Excluir EC3 (editorial, poster, só resumo)",EC4:"Excluir EC4 (versão anterior/duplicado)",IC4:"Excluir IC4 (sem acesso ao texto)"};
let Q=[],done={},i=0,first=null,final=null,note="",ai=null;
const $=id=>document.getElementById(id);
const esc=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
async function load(){const r=await (await fetch("/data")).json();Q=r.queue;done=r.done;
  i=Q.findIndex(x=>!done[x.key]);if(i<0)i=Q.length-1;show();}
function counts(){const c={};Object.values(done).forEach(d=>c[d.final]=(c[d.final]||0)+1);
  const n=Q.filter(x=>done[x.key]).length;
  $("counts").textContent=`feitos ${n}/${Q.length} · `+Object.entries(c).map(([k,v])=>k+" "+v).join(" · ");}
function show(){const x=Q[i];const prev=done[x.key];first=prev?prev.first:null;final=prev?prev.final:null;note=prev?prev.note:"";ai=null;
  $("pos").textContent=`#${i+1} de ${Q.length}`+(prev?" (já decidido, podes mudar)":"");
  $("title").textContent=x.title;
  const link=x.url||("https://scholar.google.com/scholar?q="+encodeURIComponent(x.title));
  $("meta").innerHTML=`${x.flag?'<b style="color:#c00">⚠ DISCORDÂNCIA no passo 2: aplica primeiro o fluxo do passo 2, depois o EC6.</b><br>':""}${x.p2?"Passo 2: "+esc(x.p2)+" · ":""}${esc(x.year)} · ${esc(x.sources)} · <a href="${esc(link)}" target="_blank">abrir</a>`+(x.keywords?`<br>Palavras-chave: ${esc(x.keywords)}`:"");
  $("abs").innerHTML=x.abstract?esc(x.abstract):'<span class="noabs">SEM RESUMO.</span> Decide pelo título; se não chegar, carrega em "abrir" ou escolhe Maybe.';
  $("ai").className="";$("ai").innerHTML="";counts();render();if(prev)reveal();if(PASS==="ft")ftview(x);}
async function ftview(x){const el=$("ftv");el.innerHTML="";const k=x.key;
  const head=`<div class="meta">Grupo (IA, passo 3): <b>${esc(x.g)}</b> · <a href="/pdf?key=${encodeURIComponent(k)}" target="_blank">abrir PDF</a> (tecla P)</div>`;
  if(!x.ft){el.innerHTML=head+'<p class="noabs">SEM TEXTO INTEGRAL em slr/fulltext/. Descarrega o PDF (ver fulltext-access.csv) ou, se não houver acesso, [X] IC4.</p>';return;}
  const v=await (await fetch("/view?key="+encodeURIComponent(k))).json();if(Q[i].key!==k||!v)return;
  const sec=(t,s,open)=>s?`<details ${open?"open":""}><summary>${t}</summary><div class="txt">${esc(s)}</div></details>`:`<details><summary style="color:#999">${t}: não encontrado (abre o PDF)</summary></details>`;
  el.innerHTML=head+`<div class="terms">${Object.entries(v.terms).map(([a,n])=>`<span>${esc(a)}: ${n?"<b>"+n+"</b>":0}</span>`).join("")} <span>${Math.round(v.chars/1000)}k car.</span></div>`
   +sec("Contribuições",v.contrib,true)+sec("Método",v.method,true)+sec("Avaliação / resultados",v.eval,false)+sec("Conclusão",v.concl,true)
   +`<details><summary>Secções (${v.heads.length})</summary><div class="heads">${v.heads.map(esc).join("<br>")}</div></details>`;}
function render(){$("keys").innerHTML=OPTS.map(([k,v])=>`<button data-v="${v}" class="${v===first?"first":""} ${v===final?"final":""}">[${k}] ${LABEL[v]}</button>`).join("");
  document.querySelectorAll("#keys button").forEach(b=>b.onclick=()=>pick(b.dataset.v));
  $("hint").innerHTML=first===null?`<b>Passo 1:</b> decide TU primeiro (${OPTS.map(o=>o[0]).join(", ")}). A sugestão da IA só aparece depois.`
   :`<b>Passo 2:</b> a tua decisão: <b>${LABEL[final]}</b>${note?" · nota: "+esc(note):""}. <b>Enter</b> grava e avança · outra tecla muda · <b>N</b> nota · <b>←</b> anterior`;}
async function reveal(){const x=Q[i];const k=x.key;const r=await (await fetch("/ai?key="+encodeURIComponent(k))).json();if(Q[i].key!==k)return;ai=r;
  const el=$("ai");if(!r){el.className="none";el.innerHTML="Sem sugestão da IA para este registo (ainda). Decide só por ti.";return;}
  const same=r.s===first;el.className=same?"agree":"disagree";
  el.innerHTML=(same?"✔ <b>Concordamos.</b> ":"⚠ <b>A IA sugere outra coisa — relê e decide tu.</b> ")+`IA: <b>${LABEL[r.s]||r.s}</b>${r.g?" (grupo "+esc(r.g)+")":""} · ${esc(r.r)}<br><q>${esc(r.q)}</q>${r.sec?" ("+esc(r.sec)+")":""}${r.q_ok==="False"?' <b style="color:#c00">citação não verificada</b>':""}`;}
function pick(v){if(first===null){first=v;final=v;if(v==="Other"&&!note)askNote();render();reveal();}else{final=v;if(v==="Other"&&!note)askNote();render();}}
function askNote(){const t=prompt(PASS==="ft"?"Nota (o que decidiu; ex.: grupo a, SDD com Kiro; EC6 é issue repair; EC4 duplicado de …):":"Nota (ex.: poster EC3, não está em inglês, anterior a 2023, duplicado):",note||"");if(t!==null)note=t.trim();}
async function commit(){if(first===null)return;if(final==="Other"&&!note){askNote();if(!note)return;}
  const x=Q[i];const d={key:x.key,first,final,ai:ai?ai.s:"",agree:ai?String(ai.s===first):"",note};
  const r=await fetch("/decide",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d)});
  if(!r.ok){alert("ERRO ao gravar. Não avances; verifica se o screen.py está a correr.");return;}
  done[x.key]=d;$("saved").textContent="gravado ✓";setTimeout(()=>$("saved").textContent="",800);
  const nx=Q.findIndex((y,j)=>j>i&&!done[y.key]);if(nx<0){alert("Fim da fila! Avisa o Claude.");counts();return;}i=nx;show();}
document.onkeydown=e=>{if(e.ctrlKey||e.metaKey||e.altKey)return;const k=e.key.toUpperCase();
  const o=OPTS.find(([a])=>a===k);if(o){pick(o[1]);e.preventDefault();return;}
  if(k==="ENTER"){commit();e.preventDefault();}else if(k==="N"&&first!==null){askNote();render();}
  else if(k==="P"&&PASS==="ft"){window.open("/pdf?key="+encodeURIComponent(Q[i].key),"_blank");}
  else if(e.key==="ArrowLeft"&&i>0){i--;show();}else if(e.key==="ArrowRight"&&i<Q.length-1){i++;show();}};
load();
</script></body></html>"""
CARD = {"ft": r"""<b>Texto integral. Lê o resumo e as partes extraídas; abre o PDF (P) quando não chegar. Por ordem:</b><ol>
<li>Sem texto e sem acesso (ISEP, editora, arXiv, Google Scholar) → <b>[X] IC4</b></li>
<li>Versão anterior ou duplicado de outro registo incluído → <b>[4] EC4</b> (nota: qual fica). Editorial, poster, só resumo, tutorial → <b>[7] EC3</b></li>
<li>Não há agente de IA a desenvolver software → <b>[1] IC1</b>. Só funções soltas → <b>[2] EC1</b>. "Especificação" formal/RE sem agente → <b>[8] EC2</b></li>
<li>Grupos (a) SDD e (b) ficheiros de contexto: confirma que o texto é mesmo isso → <b>[I]</b></li>
<li>Grupo (c): agente novo num benchmark existente sem contributo de método → <b>[3] EC5</b>; fluxo EC6 do passo 3 (não é código, issue repair, nem funcionalidade/projeto nem método) → <b>[6] EC6</b>; senão <b>[I]</b></li>
</ol>Sem Maybe: decide sempre. <b>N</b> nota (escreve sempre uma linha curta: fica guardada). IC2/IC3 → <b>[O]</b> + nota.<br>
Depois: <span style="color:#080">verde</span> → Enter. <span style="color:#c70">laranja</span> → relê a frase citada, decide tu, Enter.""", "2": r"""<b>Pergunta por ordem; a primeira que decide manda.</b><ol>
<li><b>Há um agente de IA a desenvolver software</b> (escreve, altera, testa código)? Não → <b>[1] IC1</b>. Também IC1: agente que joga o jogo, agente como peça do produto, multi-agentes em geral.</li>
<li><b>Só gera funções soltas</b> (HumanEval, concursos)? Sim → <b>[2] EC1</b></li>
<li><b>Fala de especificações, SDD, AGENTS.md, regras, contexto ou memória do agente?</b> Sim → <b>[I] Include</b></li>
<li><b>Vende um agente ou mede agentes?</b> Mede (benchmark novo, compara agentes/modelos/configurações, estudo empírico, revisão) → <b>[I]</b>. Vende (agente novo + benchmark existente) → <b>[3] EC5</b></li>
</ol>Decide sempre <b>Include</b> ou exclusão; na fronteira fica <b>Include</b> (a passagem 3 aperta os benchmarks). <b>[M] Maybe</b> só se não perceberes o que o artigo faz. Raro (poster, outra língua, antes de 2023, duplicado) → <b>[O]</b> + nota.<br>
Depois: <span style="color:#080">verde</span> → Enter. <span style="color:#c70">laranja</span> → relê a frase citada, decide tu, Enter.""", "3": r"""<b>Passo 3 (EC6). Grupos (a) SDD e (b) ficheiros de contexto: [I] fica, sem perguntas. Grupo (c), por ordem:</b><ol>
<li>A tarefa <b>não</b> é escrever ou alterar código de uma aplicação (só testes, revisão, segurança, documentação, compreensão de código)? → <b>[6] EC6</b></li>
<li>É <b>reparação de issues</b> (tipo SWE-bench)? → <b>[6] EC6</b>, sempre</li>
<li>O contributo principal é o <b>método de avaliação</b> (métricas de custo, qualidade ou esforço; repetições; comparação controlada de agentes, modelos ou workflows nas mesmas tarefas)? → <b>[I]</b></li>
<li>O agente <b>constrói ou estende uma aplicação</b> a partir de requisitos (funcionalidade ou projeto), sem ser um domínio especializado? → <b>[I]</b></li>
<li>Senão → <b>[6] EC6</b> (mineração de PRs, tarefas pequenas, só hardware, data science, smart contracts…)</li>
</ol>Registo com <b style="color:#c00">⚠ discordância</b>: primeiro o fluxo do passo 2 ([1] IC1, [2] EC1, [3] EC5), depois este. <b>[M]</b> só se o resumo não chegar.<br>
Depois: <span style="color:#080">verde</span> → Enter. <span style="color:#c70">laranja</span> → relê a frase citada, decide tu, Enter. Se a IA sugerir EC2, EC3, EC4, IC2 ou IC3 e concordares: <b>[O]</b> + nota com o código."""}

if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", 8765), H)
    print(f"Pass {PASS} screening at http://127.0.0.1:8765  (Ctrl+C to stop; decisions in {DEC})")
    webbrowser.open("http://127.0.0.1:8765")
    srv.serve_forever()
