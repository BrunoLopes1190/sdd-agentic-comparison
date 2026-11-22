"""Title/abstract screening tool for passes 2 and 3 (protocol §4.2 steps 4 and 4b).

Run:  python slr/screen.py [2|3]   -> opens http://127.0.0.1:8765  (default: pass 2)
Queue:       slr/passN-queue.csv           (records to screen; pass 3 from build_pass3_queue.py)
Suggestions: slr/passN-ai-suggestions.csv  (AI suggestion, shown only AFTER the author decides)
Decisions:   slr/passN-decisions.csv       (append-only; the last row per key wins)
"""
import csv, datetime, json, os, sys, webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.abspath(__file__))
PASS = sys.argv[1] if len(sys.argv) > 1 else "2"
assert PASS in ("2", "3"), "usage: python slr/screen.py [2|3]"
QUEUE = os.path.join(HERE, f"pass{PASS}-queue.csv")
AI = os.path.join(HERE, f"pass{PASS}-ai-suggestions.csv")
DEC = os.path.join(HERE, f"pass{PASS}-decisions.csv")
FIELDS = ["time", "key", "first", "final", "ai", "agree", "note"]
ALLOWED = {"Include", "Maybe", "IC1", "EC1", "EC5", "Other"} | ({"EC6"} if PASS == "3" else set())


def read(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


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
            self.send(json.dumps({"queue": read(QUEUE), "done": decisions()}))
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


PAGE = r"""<!doctype html><html lang="pt"><head><meta charset="utf-8"><title>Triagem passagem __PASS__</title>
<style>
body{font:17px/1.55 system-ui,sans-serif;max-width:960px;margin:0 auto;padding:16px;background:#fafafa;color:#222}
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
</style></head><body>
<div id="bar"><span id="pos"></span><span id="counts"></span><span id="saved"></span></div>
<h1 id="title"></h1><div class="meta" id="meta"></div>
<div id="abs"></div>
<div id="keys"></div>
<div id="ai"></div>
<div id="hint"></div>
<div id="card">__CARD__</div>
<script>
const PASS=__PASS__;
const OPTS=PASS===3?[["I","Include"],["6","EC6"],["1","IC1"],["2","EC1"],["3","EC5"],["M","Maybe"],["O","Other"]]
  :[["I","Include"],["M","Maybe"],["1","IC1"],["2","EC1"],["3","EC5"],["O","Other"]];
const LABEL={Include:"Include",Maybe:"Maybe",IC1:"Excluir IC1 (sem agente a programar)",EC1:"Excluir EC1 (só funções)",EC5:"Excluir EC5 (só o agente deles)",EC6:"Excluir EC6 (passo 3)",Other:"Outro (nota)"};
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
  $("ai").className="";$("ai").innerHTML="";counts();render();if(prev)reveal();}
function render(){$("keys").innerHTML=OPTS.map(([k,v])=>`<button data-v="${v}" class="${v===first?"first":""} ${v===final?"final":""}">[${k}] ${LABEL[v]}</button>`).join("");
  document.querySelectorAll("#keys button").forEach(b=>b.onclick=()=>pick(b.dataset.v));
  $("hint").innerHTML=first===null?`<b>Passo 1:</b> decide TU primeiro (${OPTS.map(o=>o[0]).join(", ")}). A sugestão da IA só aparece depois.`
   :`<b>Passo 2:</b> a tua decisão: <b>${LABEL[final]}</b>${note?" · nota: "+esc(note):""}. <b>Enter</b> grava e avança · outra tecla muda · <b>N</b> nota · <b>←</b> anterior`;}
async function reveal(){const x=Q[i];const k=x.key;const r=await (await fetch("/ai?key="+encodeURIComponent(k))).json();if(Q[i].key!==k)return;ai=r;
  const el=$("ai");if(!r){el.className="none";el.innerHTML="Sem sugestão da IA para este registo (ainda). Decide só por ti.";return;}
  const same=r.s===first;el.className=same?"agree":"disagree";
  el.innerHTML=(same?"✔ <b>Concordamos.</b> ":"⚠ <b>A IA sugere outra coisa — relê e decide tu.</b> ")+`IA: <b>${LABEL[r.s]||r.s}</b>${r.g?" (grupo "+esc(r.g)+")":""} · ${esc(r.r)}<br><q>${esc(r.q)}</q>`;}
function pick(v){if(first===null){first=v;final=v;if(v==="Other"&&!note)askNote();render();reveal();}else{final=v;if(v==="Other"&&!note)askNote();render();}}
function askNote(){const t=prompt("Nota (ex.: poster EC3, não está em inglês, anterior a 2023, duplicado):",note||"");if(t!==null)note=t.trim();}
async function commit(){if(first===null)return;if(final==="Other"&&!note){askNote();if(!note)return;}
  const x=Q[i];const d={key:x.key,first,final,ai:ai?ai.s:"",agree:ai?String(ai.s===first):"",note};
  const r=await fetch("/decide",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d)});
  if(!r.ok){alert("ERRO ao gravar. Não avances; verifica se o screen.py está a correr.");return;}
  done[x.key]=d;$("saved").textContent="gravado ✓";setTimeout(()=>$("saved").textContent="",800);
  const nx=Q.findIndex((y,j)=>j>i&&!done[y.key]);if(nx<0){alert("Fim da fila! Avisa o Claude.");counts();return;}i=nx;show();}
document.onkeydown=e=>{if(e.ctrlKey||e.metaKey||e.altKey)return;const k=e.key.toUpperCase();
  const o=OPTS.find(([a])=>a===k);if(o){pick(o[1]);e.preventDefault();return;}
  if(k==="ENTER"){commit();e.preventDefault();}else if(k==="N"&&first!==null){askNote();render();}
  else if(e.key==="ArrowLeft"&&i>0){i--;show();}else if(e.key==="ArrowRight"&&i<Q.length-1){i++;show();}};
load();
</script></body></html>"""
CARD = {"2": r"""<b>Pergunta por ordem; a primeira que decide manda.</b><ol>
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
