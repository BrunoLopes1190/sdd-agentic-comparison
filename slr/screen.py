"""Screening tool: title/abstract passes 2 and 3 (protocol §4.2 steps 4 and 4b) and full text (step 7).

Run:  python slr/screen.py [2|3|ft]   -> opens http://127.0.0.1:8765  (default: pass 2)
Queue:       slr/passN-queue.csv           (records to screen; pass 3 from build_pass3_queue.py)
             ft: the pass-3 includes, AI group (a), (b), (c) order, with a view extracted from slr/fulltext/<key>.txt
Suggestions: slr/passN-ai-suggestions.csv  (AI suggestion, shown only AFTER the author decides; ft: ft-ai-suggestions.csv)
Decisions:   slr/passN-decisions.csv       (append-only; the last row per key wins; ft: ft-decisions.csv)
Extraction:  ft only. After an Include, the AI draft slr/extraction/ai-drafts/<key>.json (protocol §5-6) is shown for
             the author to check; the checked record is saved to slr/extraction/<key>.json
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
XDIR = os.path.join(HERE, "extraction")
# Extraction form (protocol §6) and quality checklist (§5; DARE-4 for reviews, Kitchenham & Charters 2007)
XFIELDS = ["Reference", "Year", "Publication type", "Author affiliation", "Nature of the study",
           "Approach(es): name and version", "Artefacts prescribed", "Phases of the flow", "Human review points",
           "Parts exercised", "SDD level", "Task type", "Size", "Domain", "Team profile",
           "Cost metrics", "Functional quality metrics", "Internal quality metrics", "Human effort metrics",
           "Other outcome metrics", "How metrics are collected", "Evaluation (each configuration)",
           "Comparison: design", "Comparison: result", "Comparison: did the method work",
           "Conclusions: limitations and gaps", "Notes"] + [f"Q{n}" for n in range(1, 14)] + [f"DARE{n}" for n in range(1, 5)]
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
    s = max(0, m.start() - 300) if m else 0
    s = max(body.rfind(" ", 0, s), body.rfind("\n", 0, s)) + 1 if s else 0  # start on a word boundary
    contrib = " ".join(body[s:m.start() + 1500].split()) if m else ""
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
        elif u.path == "/draft":
            key = os.path.basename(parse_qs(u.query).get("key", [""])[0])
            load = lambda f: json.load(open(f, encoding="utf-8")) if os.path.exists(f) else None  # noqa: E731
            self.send(json.dumps({"fields": XFIELDS, "draft": load(os.path.join(XDIR, "ai-drafts", key + ".json")),
                                  "saved": load(os.path.join(XDIR, key + ".json"))}))
        elif u.path == "/ai":
            key = parse_qs(u.query).get("key", [""])[0]
            s = next((a for a in read(AI) if a["key"] == key), None)  # read fresh: suggestions may still be arriving
            self.send(json.dumps(s))
        else:
            self.send("{}", code=404)

    def do_POST(self):
        d = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if self.path == "/extract" and PASS == "ft":
            key = os.path.basename(d.get("key", ""))
            if not key or decisions().get(key, {}).get("final") != "Include":
                return self.send('{"ok": false}', code=400)
            d["time"] = datetime.datetime.now().isoformat(timespec="seconds")
            os.makedirs(XDIR, exist_ok=True)
            with open(os.path.join(XDIR, key + ".json"), "w", encoding="utf-8") as f:
                json.dump(d, f, ensure_ascii=False, indent=1)
            return self.send('{"ok": true}')
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
#xp{margin:14px 0;padding:10px 14px;border:2px solid #36c;border-radius:8px;background:#fff;display:none}
#xp table{width:100%;border-collapse:collapse;font-size:14px}#xp td{border-top:1px solid #eee;padding:3px 4px;vertical-align:top}
#xp td.f{width:190px;font-weight:600}#xp textarea{width:100%;font:14px/1.4 system-ui;box-sizing:border-box}
#xp input.p{width:60px}#xp tr.ok td.f{color:#080}#xp tr.sec td{background:#eef3ff;font-weight:700}
#xp tr.warn td{background:#fff3e0}#xp tr.warn td.f{border-left:4px solid #e80}#xp details.hp{font-weight:400;font-size:12px;color:#555;margin-top:2px}#xp details.hp summary{cursor:pointer}#xp details.hp .q{display:inline-block;border:1px solid #999;border-radius:50%;width:14px;text-align:center;font-size:11px;line-height:14px}#xp details.hp div{background:#fffbe6;border:1px solid #e6d9a0;padding:6px;margin-top:3px;border-radius:4px}#xp.onlyw tr:not(.warn):not(.sec){display:none}#xp .w{font-weight:400;font-size:12px;color:#a50}
#xp button{font-size:15px;padding:6px 12px;margin:6px 6px 0 0}
</style></head><body>
<div id="bar"><span id="pos"></span><span id="counts"></span><span id="saved"></span></div>
<h1 id="title"></h1><div class="meta" id="meta"></div>
<div id="abs"></div>
<div id="ftv"></div>
<div id="keys"></div>
<div id="ai"></div>
<div id="hint"></div>
<div id="xp"></div>
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
  $("meta").innerHTML=`${x.flag&&PASS!=="ft"?'<b style="color:#c00">⚠ DISCORDÂNCIA no passo 2: aplica primeiro o fluxo do passo 2, depois o EC6.</b><br>':""}${x.p2?"Passo 2: "+esc(x.p2)+" · ":""}${esc(x.year)} · ${esc(x.sources)} · <a href="${esc(link)}" target="_blank">abrir</a>`+(x.keywords?`<br>Palavras-chave: ${esc(x.keywords)}`:"");
  $("abs").innerHTML=x.abstract?esc(x.abstract):'<span class="noabs">SEM RESUMO.</span> Decide pelo título; se não chegar, carrega em "abrir" ou escolhe Maybe.';
  $("ai").className="";$("ai").innerHTML="";counts();render();if(prev)reveal();$("xp").style.display="none";
  if(PASS==="ft"){ftview(x);if(prev&&prev.final==="Include")xpanel(x);}}
const XSEC={"Reference":"Identificação","Approach(es): name and version":"Abordagem (RQ1)","Task type":"Contexto (O5)","Cost metrics":"Medição (RQ2)",
  "Evaluation (each configuration)":"Avaliação e comparação (RQ3, RQ4)","Conclusions: limitations and gaps":"Conclusões e notas","Q1":"Qualidade (§5): Sim 1 / Parcial 0.5 / Não 0 / N/A","DARE1":"DARE (só revisões)"};
// Quality questions (protocol §5; DARE as in Kitchenham & Charters 2007): [question, Yes, Partly, No, where to look]
const QH={Q1:["Os objetivos ou as RQ estão claros? (todos)","há objetivo ou RQ explícitos","só implícitos","não se percebe o objetivo","Abstract, fim da Introdução"],
 Q2:["O método está descrito ao ponto de ser replicável? (todos)","passos, configuração e dados para repetir","falta algum elemento","só descrição vaga","Method / Setup"],
 Q3:["Versões do agente, do modelo e da ferramenta identificadas? (empíricos)","todas, com versão ou data","algumas","nenhuma","Setup, Implementation"],
 Q4:["Tarefas, projeto ou benchmark descritos e disponíveis? (empíricos)","descritos e públicos (link)","descritos mas não públicos","não descritos","Setup, Data, Artifact"],
 Q5:["Eficácia medida contra critério independente (testes de aceitação, ground truth, peritos)? (empíricos)","critério externo","misto","só o juízo dos autores","Evaluation, Metrics"],
 Q6:["Métricas definidas e cobrem custo E qualidade? (empíricos)","ambos, definidos","só um, ou mal definidos","sem métricas","Metrics"],
 Q7:["Baseline ou alternativa avaliada nas mesmas condições? (empíricos)","sim, nas mesmas condições","condições diferentes","não há","Experiments"],
 Q8:["Variabilidade tratada (repetições, estatística)? (empíricos)","repetições e teste estatístico","só uma das duas","corrida única","Setup, Results"],
 Q9:["As conclusões seguem dos resultados, incluindo negativos ou mistos? (todos)","sim","exageram em parte","não seguem","Conclusão comparada com as tabelas"],
 Q10:["Discute ameaças à validade e limitações? (todos)","secção própria","só de passagem","não discute","Threats / Limitations"],
 Q11:["Teve revisão por pares? (todos)","conferência, journal ou workshop com revisão","venue de revisão duvidosa","preprint ou submetido","cabeçalho, rodapé da 1.ª página, DOI"],
 Q12:["Autores independentes do fornecedor da ferramenta avaliada? (todos)","independentes","só parte das abordagens avaliadas é dos autores","avaliam a sua própria ferramenta ou abordagem (N/A se não avaliam nenhuma)","afiliações, Contributions"],
 Q13:["Abordagem proposta viável: requisitos (ferramentas, computação, custo) declarados e ao alcance de uma equipa típica? (conceptuais ou que propõem abordagem)","declarados e acessíveis","só parcialmente declarados","não declarados, ou fora do alcance (N/A se não é conceptual nem propõe abordagem)","Implementation, Discussion"],
 DARE1:["Critérios de inclusão e exclusão descritos e adequados? (revisões com pesquisa descrita)","descritos e adequados","descritos de forma vaga","não descritos","Method da revisão"],
 DARE2:["A pesquisa terá coberto os estudos relevantes?","várias bases + snowballing ou pesquisa manual","uma ou duas bases","fontes não indicadas","Search strategy"],
 DARE3:["A qualidade dos estudos incluídos foi avaliada?","critérios explícitos","avaliação implícita","não avaliada","Quality assessment"],
 DARE4:["Os dados dos estudos incluídos estão descritos?","cada estudo descrito","só resumo agregado","não descritos","tabelas e resultados da revisão"]};
// How to resolve a flagged (⚠) field: what to read and what to decide
const TUT={"Nature of the study":"<b>Ler:</b> Abstract, a lista de contribuições (\"we propose…\", \"we evaluate…\", \"we compare…\") e os títulos das secções.<br><b>Decidir:</b> a principal é o que o artigo mais entrega. Ferramenta ou método novo → Proposes an approach; benchmark ou métrica → Proposes an evaluation method; configurações comparadas nas mesmas tarefas → Compares; mede uma só abordagem → Evaluates; sem dados → Conceptual; revisão com pesquisa descrita → Review. Mineração de repositórios → Evaluates, com \"repository mining\" na nota. Secundária só se houver um segundo contributo claro.",
 "Evaluation (each configuration)":"<b>Ler:</b> as tabelas de resultados e, no Setup ou Metrics, o critério de sucesso que os autores definem.<br><b>Decidir:</b> uma entrada por configuração (abordagem ou baseline + agente + modelo), cada uma julgada por si. Veredicto de qualidade e de custo só quando os autores dão um critério; sem critério escreve \"no criterion stated by the authors\". Apaga qualquer limiar escolhido pela IA.",
 "Comparison: result":"<b>Ler:</b> as tabelas de comparação e a Discussion.<br><b>Decidir:</b> quem ganha, em que dimensão, por quanto e se a diferença é significativa, só com números do texto. Sem limiares inventados.",
 "SDD level":"<b>Ler:</b> a descrição do fluxo com especificações.<br><b>Decidir</b> (Böckeler, 2025): spec-first = escreve-se a spec, gera-se o código, a spec pode ser abandonada; spec-anchored = a spec é mantida com o código ao longo do tempo; spec-as-source = só se edita a spec e o código é regenerado; sem fluxo com spec (comum em b e c) → Not classifiable. Guarda as palavras dos autores.",
 "Publication type":"<b>Ler:</b> cabeçalho e rodapé da 1.ª página (nome da conferência, \"Accepted at…\"), o DOI, ou o link \"abrir\" no topo.<br><b>Decidir:</b> Preprint só se não houver venue aceite; publicado mas lido no arXiv → o tipo do venue. A Q11 segue esta decisão.",
 "Notes":"<b>Ler:</b> cada inconsistência listada pela IA e a tabela ou frase de onde vem.<br><b>Decidir:</b> confirma cada uma no PDF; apaga as que não se confirmam. Valores reconstruídos de tabelas desorganizadas: confirma-os no PDF.",
 "Task type":"<b>Ler:</b> Setup: as tarefas partem de um repositório vazio ou de código existente?<br><b>Decidir:</b> new project, existing code base, ou ambos; se o artigo não diz, \"Not stated\".",
 _:"<b>Ler:</b> abre o PDF na página indicada (link \"pág.\") e lê o parágrafo ou a tabela de onde vem o valor.<br><b>Decidir:</b> se o texto confirma o valor, marca ✓; se não, corrige com as palavras do artigo; se o artigo não diz, \"Not stated\"."};
const qtut=f=>QH[f]?`<b>Ler:</b> ${QH[f][4]}.<br><b>Decidir:</b> Sim (1) se ${QH[f][1]}; Parcial (0.5) se ${QH[f][2]}; Não (0) se ${QH[f][3]}. Informação em falta = Não.`:"";
const qhelp=f=>QH[f]?`<details class="hp"><summary>${esc(QH[f][0])} <span class="q">?</span></summary><div><b>Sim (1):</b> ${QH[f][1]}<br><b>Parcial (0.5):</b> ${QH[f][2]}<br><b>Não (0):</b> ${QH[f][3]}<br><b>Onde ver:</b> ${QH[f][4]}<br>Informação em falta = Não.</div></details>`:"";
const wtip=(f,w)=>`<div class="w">⚠ ${esc(w)}</div><details class="hp"><summary class="w"><b>Como resolver</b> <span class="q">?</span></summary><div>${TUT[f]||qtut(f)||TUT._}</div></details>`;
function openPage(f){const m=($("xp").querySelector(`[data-p="${CSS.escape(f)}"]`).value.match(/\d+/)||[])[0];window.open("/pdf?key="+encodeURIComponent(Q[i].key)+(m?"#page="+m:""),"_blank");}
// Fields with fixed values (protocol §6): dropdown + note, saved as one string "Value; secondary: Value — note"
const CH={"Publication type":["Journal","Conference","Workshop","Preprint"],
  "Nature of the study":["Evaluates","Compares","Proposes an approach","Proposes an evaluation method","Conceptual","Review"]};
function parseCh(f,v){const o=CH[f],lo=x=>x.toLowerCase();let s=String(v||"").trim().replace(/^main:\s*/i,"");
  const m=o.find(x=>lo(s).startsWith(lo(x)))||"";s=s.slice(m.length);let sec="";
  if(f==="Nature of the study"){const k=s.match(new RegExp("secondary:\\s*("+o.join("|")+")","i"));if(k){sec=o.find(x=>lo(x)===lo(k[1]));s=s.replace(k[0],"");}}
  s=s.replace(/^[\s;,:—-]+|[\s;,—-]+$/g,"");
  if(s[0]==="("){let d=0,j=0;for(;j<s.length;j++){d+=s[j]==="("?1:s[j]===")"?-1:0;if(!d)break;}if(j===s.length-1)s=s.slice(1,-1).trim();}
  return {m,sec,note:s};}
function composeCh(p){const h=p.m+(p.sec?"; secondary: "+p.sec:"");return h&&p.note?h+" — "+p.note:h||p.note;}
function chCell(f,v){const p=parseCh(f,v),opt=(sel,none)=>`<option value="">${none}</option>`+CH[f].map(x=>`<option ${x===sel?"selected":""}>${x}</option>`).join("");
  return `<select data-sel="${esc(f)}">${opt(p.m,"— escolhe —")}</select>`+(f==="Nature of the study"?` secundária <select data-sec="${esc(f)}">${opt(p.sec,"(nenhuma)")}</select>`:"")
   +`<br><input data-note="${esc(f)}" value="${esc(p.note)}" placeholder="nota" style="width:100%;box-sizing:border-box">`;}
function chValue(el,f){const q=a=>el.querySelector(`[${a}="${CSS.escape(f)}"]`);return composeCh({m:q("data-sel").value,sec:q("data-sec")?q("data-sec").value:"",note:q("data-note").value.trim()});}
async function xpanel(x){const k=x.key;const r=await (await fetch("/draft?key="+encodeURIComponent(k))).json();if(Q[i].key!==k)return;
  const src=r.saved||r.draft;const by={};((src&&src.fields)||[]).forEach(f=>by[f.f]=f);
  const dw={};((r.draft&&r.draft.fields)||[]).forEach(f=>dw[f.f]=f);const nw=Object.values(dw).filter(f=>f.warn).length;
  const revt=f=>(dw[f]&&dw[f].rev||[]).map(x=>`volta ${x.round} ${x.verdict}: ${x.why}`).join("\n");
  const el=$("xp");el.style.display="block";
  el.innerHTML=`<b>Extração e qualidade</b> · ${r.saved?"gravada a "+esc(r.saved.time)+" (podes corrigir)":r.draft?"rascunho da IA: confirma (✓) ou corrige cada campo; página do PDF ao lado":"<span class=noabs>ainda sem rascunho da IA</span>: preenche à mão ou grava mais tarde"}
   ${r.draft&&r.draft.rounds?` · verificado ${r.draft.rounds} vezes${nw?` · <b style="color:#c60">⚠ ${nw} campo(s) com atenção redobrada</b>`:" · sem campos inseguros"}`:r.draft?" · <i>ainda não verificado (voltas em curso)</i>":""}
   ${nw?`<button id="xonly">só ⚠ (${nw})</button>`:""}<table>${r.fields.map(f=>(XSEC[f]?`<tr class="sec"><td colspan="3">${XSEC[f]}</td></tr>`:"")+`<tr class="${by[f]&&by[f].ok?"ok":""} ${dw[f]&&dw[f].warn?"warn":""}"><td class="f" title="${esc(revt(f))}">${esc(f)}${qhelp(f)}${dw[f]&&dw[f].warn?wtip(f,dw[f].warn):""}</td>
   <td>${CH[f]?chCell(f,by[f]&&by[f].v):`<textarea rows="${Math.min(6,Math.max(1,Math.ceil(((by[f]&&by[f].v)||"").length/110)))}" data-f="${esc(f)}">${esc(by[f]?by[f].v:"")}</textarea>`}</td>
   <td><input class="p" data-p="${esc(f)}" value="${esc(by[f]?by[f].p:"")}" title="página(s)"> <a href="#" data-pg="${esc(f)}" title="abrir o PDF nesta página">pág.</a><br><label><input type="checkbox" data-ok="${esc(f)}" ${by[f]&&by[f].ok?"checked":""}>✓</label></td></tr>`).join("")}</table>
   <button id="xall">✓ em todos</button><button id="xsave"><b>Gravar extração e avançar</b></button><button id="xlater">Gravar mais tarde (avançar)</button>`;
  el.querySelectorAll("[data-pg]").forEach(a=>a.onclick=e=>{e.preventDefault();openPage(a.dataset.pg);});
  if($("xonly"))$("xonly").onclick=()=>{el.classList.toggle("onlyw");$("xonly").textContent=el.classList.contains("onlyw")?"mostrar todos":`só ⚠ (${nw})`;};
  $("xall").onclick=()=>el.querySelectorAll("[data-ok]").forEach(c=>c.checked=true);
  $("xlater").onclick=()=>next();
  $("xsave").onclick=async()=>{const dv={};((r.draft&&r.draft.fields)||[]).forEach(f=>dv[f.f]=f.v);
    const fields=r.fields.map(f=>{const v=CH[f]?chValue(el,f):el.querySelector(`[data-f="${CSS.escape(f)}"]`).value;
      const base=f in dv?(CH[f]?composeCh(parseCh(f,dv[f])):dv[f]):null;  // dropdown fields: compare in the same format
      return {f,v,p:el.querySelector(`[data-p="${CSS.escape(f)}"]`).value,
      ok:el.querySelector(`[data-ok="${CSS.escape(f)}"]`).checked,ai:f in dv?dv[f]:null,changed:f in dv?v!==base:null};});
    const s=await fetch("/extract",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({key:k,fields})});
    if(!s.ok){alert("ERRO ao gravar a extração.");return;}$("saved").textContent="extração gravada ✓";setTimeout(()=>$("saved").textContent="",1200);next();};}
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
  el.innerHTML=(same?"✔ <b>Concordamos.</b> ":"⚠ <b>A IA sugere outra coisa — relê e decide tu.</b> ")+`IA: <b>${LABEL[r.s]||r.s}</b>${r.g?" (grupo "+esc(r.g)+")":""} · ${esc(r.r)}<br><q>${esc(r.q)}</q>${r.sec?" ("+esc(r.sec)+")":""}${r.q_ok==="False"?' <b style="color:#c00">citação não verificada</b>':""}`
   +(r.agree?(r.agree==="3/3"?`<br>3 leituras independentes concordam (3/3).`
     :`<br><b style="color:#c60">⚠ IA insegura: ${r.agree==="2/3"?"só 2 das 3 leituras concordam":"sem maioria nas 3 leituras (fica a sugestão anterior)"} (${esc(r.votes)}). Atenção redobrada.</b>`):"");}
function pick(v){if(first===null){first=v;final=v;if(v==="Other"&&!note)askNote();render();reveal();}else{final=v;if(v==="Other"&&!note)askNote();render();}}
function askNote(){const t=prompt(PASS==="ft"?"Nota (o que decidiu; ex.: grupo a, SDD com Kiro; EC6 é issue repair; EC4 duplicado de …):":"Nota (ex.: poster EC3, não está em inglês, anterior a 2023, duplicado):",note||"");if(t!==null)note=t.trim();}
async function commit(){if(first===null)return;if(final==="Other"&&!note){askNote();if(!note)return;}
  const x=Q[i];const d={key:x.key,first,final,ai:ai?ai.s:"",agree:ai?String(ai.s===first):"",note};
  const r=await fetch("/decide",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d)});
  if(!r.ok){alert("ERRO ao gravar. Não avances; verifica se o screen.py está a correr.");return;}
  done[x.key]=d;$("saved").textContent="gravado ✓";setTimeout(()=>$("saved").textContent="",800);
  if(PASS==="ft"&&final==="Include"){counts();xpanel(x);$("xp").scrollIntoView();return;}next();}
function next(){const nx=Q.findIndex((y,j)=>j>i&&!done[y.key]);if(nx<0){alert("Fim da fila! Avisa o Claude.");counts();return;}i=nx;show();window.scrollTo(0,0);}
document.onkeydown=e=>{if(e.ctrlKey||e.metaKey||e.altKey||e.target.closest("textarea,input"))return;const k=e.key.toUpperCase();
  const o=OPTS.find(([a])=>a===k);if(o){pick(o[1]);e.preventDefault();return;}
  if(k==="ENTER"&&$("xp").style.display==="block"&&final==="Include"){e.preventDefault();return;}  // extraction open: save it with its button
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
Depois: <span style="color:#080">verde</span> → Enter. <span style="color:#c70">laranja</span> → relê a frase citada, decide tu, Enter.
<details><summary><b>Guia completo: porque lês, o que estás a ver, o que fazer com o que lês</b></summary>
<p><b>Porque lês.</b> Uma leitura serve para duas coisas: (1) a decisão final de elegibilidade, com os critérios aplicados ao texto inteiro (cada exclusão tem código, vai para o PRISMA); (2) nos incluídos, a extração (§6) e a qualidade (§5) na mesma leitura. O que recolhes responde às RQ:
RQ1 abordagem SDD (artefactos, fases, revisão humana) → quadro comparativo;
RQ2 métricas de custo, qualidade e esforço e como são recolhidas → as tuas métricas;
RQ3 como tornam a comparação justa (tarefas, baseline, agente/modelo fixos, repetições) → o teu protocolo;
RQ4 resultados, limitações, lacunas → a lacuna. Grupos (a)/(b): todas as RQ. Grupo (c): sobretudo RQ2 e RQ3 (como avaliam, não o agente).</p>
<p><b>O que estás a ver.</b> Resumo (dos autores). Grupo da IA no passo 3: (a) SDD, (b) ficheiros/mecanismos de contexto, (c) avaliação de agentes; só ordena a fila, confirma tu.
Contadores de termos: pista rápida (SWE-bench alto e spec a 0 → provável EC6).
<i>Contribuições</i>: excerto à volta da primeira frase "contributions" / "In this paper"; dá a natureza do estudo.
<i>Método</i>: agente, modelo, tarefas, baseline, repetições. <i>Avaliação / resultados</i> (fechada): métricas e números, abre só nos incluídos.
<i>Conclusão</i>: conclusões e limitações. <i>Secções</i>: estrutura do artigo. Os cortes são mecânicos (sem IA) e podem falhar: "não encontrado" ou algo estranho → <b>P</b> (PDF).</p>
<p><b>Em cada artigo.</b> A. Decide sem ver a IA (1–3 min): resumo + Contribuições + Método, fluxo acima, nota curta (N). B. Vê a IA: verde Enter, laranja relê a citação e decide. C. Só nos incluídos, no painel de extração: confirma cada campo no texto (página ao lado), corrige, ✓; "✓ em todos" só depois de percorrer. Pesam mais:
Nature of the study (decide que Q se aplicam); Approach / Artefacts / Phases / Human review points (RQ1, grupos a/b); métricas e How collected (RQ2); Comparison: design (RQ3); Comparison: result e Limitations (RQ4).
Sem tempo: "Gravar mais tarde" (a decisão fica, a extração fica por fazer).</p>
<p><b>Valores possíveis.</b> <i>Publication type</i>: journal · conference · workshop · preprint. Preprint só quando não há venue publicado (arXiv sem aceitação; "submitted to…" continua preprint e Q11 = Não). Se o artigo foi publicado mas leste a versão arXiv, fica o tipo do venue (ex. "Conference (UIST '26; read from arXiv v3)") e Q11 conforme o venue.
<i>Nature of the study</i> (principal + secundária opcional, ex. "compares; proposes an evaluation method"): evaluates · compares · proposes an approach · proposes an evaluation method (incl. benchmark) · conceptual · review (só se descreve a pesquisa: fontes e critérios; senão conceptual).</p>
<p><b>Qualidade.</b> Sim 1 / Parcial 0.5 / Não 0 / N/A. Informação em falta = Não. Q3–Q8 só empíricos. Q12: autor que criou a abordagem avaliada = vendedor (Parcial se só algumas). Q13 só em estudos conceptuais ou que propõem uma abordagem (§5). DARE só para revisões com pesquisa descrita.</p>
<p><b>Onde procurar.</b> Contribuições → natureza, abordagem, grupo. Método → agente/modelo/versões (Q3), tarefas e disponibilidade (Q4), baseline (Q7), repetições (Q8), intervenção humana. Avaliação → métricas, valores, quem ganha e por quanto, significância. Conclusão → Q9, limitações (Q10, RQ4). PDF → afiliação (Q12), venue (Q11), pacote de replicação (Notes).</p>
<p><b>Ritmo.</b> (a) → (b) → (c); capacidade ~250 antes do M3, o (c) é o que cede. No (c), avisa o Claude dos incluídos para os rascunhos.</p>
</details>""", "2": r"""<b>Pergunta por ordem; a primeira que decide manda.</b><ol>
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
