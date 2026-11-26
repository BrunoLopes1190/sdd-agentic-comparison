"""Final verification of the author's checked extractions (protocol §4.2 step 7; prompt slr/ai-prompts/final-verify.md).

  python slr/review.py prep     -> slr/extraction/final-verify/input/<key>.json (author's f, v, p only: no AI draft value)
  python slr/review.py status   -> how many records each check has done, and the keys still missing
  python slr/review.py          -> review tool at http://127.0.0.1:8766: only the fields a check flagged

Checks:     slr/extraction/final-verify/c1/<key>.json, c2/<key>.json (independent; only flagged fields are listed)
Decisions:  slr/extraction/final-verify/decisions.csv (append-only; last row per key+field wins)
            keep = author's value stays; accept1/accept2 = a check's proposal; edit = author's own text.
            accept/edit also rewrite the field in slr/extraction/<key>.json (previous value kept in "fv").
"""
import csv, datetime, glob, json, os, re, sys, webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.abspath(__file__))
XDIR = os.path.join(HERE, "extraction")
FV = os.path.join(XDIR, "final-verify")
FT = os.path.join(HERE, "fulltext")
DEC = os.path.join(FV, "decisions.csv")
COLS = ["time", "key", "field", "action", "value", "prev"]


def read(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def includes():
    last = {d["key"]: d for d in read(os.path.join(HERE, "ft-decisions.csv"))}
    return sorted(k for k, d in last.items() if d["final"] == "Include")


def load(path):
    return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else None


def norm(s):
    return " ".join(re.sub(r"\W+", " ", re.sub(r"-\n(?=[a-z])", "", s)).lower().split())


TEXT = {}


def quote_ok(key, q):
    if not q:
        return False
    if key not in TEXT:
        p = os.path.join(FT, key + ".txt")
        TEXT[key] = norm(open(p, encoding="utf-8", errors="replace").read()) if os.path.exists(p) else ""
    return norm(q) in TEXT[key]


def flags(key):
    """Flagged fields of one record, most serious first: both checks say corrected, both flag, one high, one low."""
    by = {}
    for n in (1, 2):
        c = load(os.path.join(FV, f"c{n}", key + ".json"))
        for f in (c or {}).get("fields", []):
            by.setdefault(f["f"], {})[n] = dict(f, q_ok=quote_ok(key, f.get("quote", "")))
    out = []
    for name, ch in by.items():
        v = [c["verdict"] for c in ch.values()]
        high = any(c.get("sev") == "high" for c in ch.values())
        rank = 0 if v == ["corrected", "corrected"] else 1 if len(ch) == 2 else 2 if high else 3
        out.append({"f": name, "rank": rank, "checks": ch})
    return sorted(out, key=lambda x: x["rank"])


def decisions():
    return {(d["key"], d["field"]): d for d in read(DEC)}


def prep():
    os.makedirs(os.path.join(FV, "input"), exist_ok=True)
    for k in includes():
        r = load(os.path.join(XDIR, k + ".json"))
        assert r, f"no extraction for {k}"
        json.dump({"key": k, "fields": [{"f": f["f"], "v": f["v"], "p": f["p"]} for f in r["fields"]]},
                  open(os.path.join(FV, "input", k + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(includes()), "inputs written")


def status():
    inc = includes()
    for n in (1, 2):
        done = {os.path.basename(p)[:-5] for p in glob.glob(os.path.join(FV, f"c{n}", "*.json"))}
        miss = [k for k in inc if k not in done]
        print(f"check {n}: {len(inc) - len(miss)}/{len(inc)} done; missing: {' '.join(miss[:300])}")


def decide(d):
    key, field, action = os.path.basename(d["key"]), d["field"], d["action"]
    assert action in ("keep", "accept1", "accept2", "edit")
    path = os.path.join(XDIR, key + ".json")
    rec = load(path)
    f = next(x for x in rec["fields"] if x["f"] == field)
    prev = f.get("fv", {}).get("prev", f["v"])  # the author's value before this review
    if action == "keep":
        value = prev
    elif action == "edit":
        value = d["value"]
    else:
        value = flags(key) and next(x for x in flags(key) if x["f"] == field)["checks"][int(action[-1])]["v"]
    f["v"] = value
    if action != "keep" and d.get("p"):
        f["p"] = d["p"]
    f["fv"] = {"action": action, "prev": prev}
    tmp = path + ".tmp"
    json.dump(rec, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    os.replace(tmp, path)
    new = not os.path.exists(DEC)
    with open(DEC, "a", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        if new:
            w.writeheader()
        w.writerow({"time": datetime.datetime.now().isoformat(timespec="seconds"), "key": key, "field": field,
                    "action": action, "value": value, "prev": prev})


def queue():
    titles = {r["key"]: r["title"] for r in read(os.path.join(HERE, "pass3-queue.csv"))}
    dec = decisions()
    out = []
    for k in includes():
        fl = flags(k)
        if fl:
            out.append({"key": k, "title": titles.get(k, k), "n": len(fl), "rank": fl[0]["rank"],
                        "open": sum((k, x["f"]) not in dec for x in fl)})
    return sorted(out, key=lambda r: (r["rank"], -r["n"]))


QH = re.search(r"const QH=\{.*?\};\n", open(os.path.join(HERE, "screen.py"), encoding="utf-8").read(), re.S).group(0)


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, body, ctype="application/json", code=200):
        b = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype + ("" if isinstance(body, bytes) else "; charset=utf-8"))
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        u = urlparse(self.path)
        key = os.path.basename(parse_qs(u.query).get("key", [""])[0])
        if u.path == "/":
            self.send(PAGE.replace("__QH__", QH), "text/html")
        elif u.path == "/queue":
            self.send(json.dumps(queue()))
        elif u.path == "/record":
            rec = load(os.path.join(XDIR, key + ".json"))
            dec = {f: d for (k, f), d in decisions().items() if k == key}
            self.send(json.dumps({"fields": {f["f"]: f for f in rec["fields"]}, "flags": flags(key), "dec": dec}))
        elif u.path == "/pdf":
            f = os.path.join(FT, key + ".pdf")
            if not os.path.exists(f):
                return self.send("PDF not in slr/fulltext/", "text/plain", 404)
            self.send(open(f, "rb").read(), "application/pdf")
        else:
            self.send("{}", code=404)

    def do_POST(self):
        try:
            decide(json.loads(self.rfile.read(int(self.headers["Content-Length"]))))
            self.send('{"ok": true}')
        except Exception as e:  # never half-save silently: the page shows the error
            self.send(json.dumps({"ok": False, "error": str(e)}), code=400)


PAGE = r"""<!doctype html><html lang="pt"><head><meta charset="utf-8"><title>Revisão final das extrações</title>
<style>
body{font:16px/1.5 system-ui,sans-serif;max-width:1100px;margin:0 auto;padding:16px;background:#fafafa;color:#222}
#bar{display:flex;justify-content:space-between;font-size:14px;color:#555;gap:8px;flex-wrap:wrap}
h1{font-size:20px;margin:10px 0 2px}.meta{font-size:13px;color:#666}
.card{background:#fff;border:1px solid #ddd;border-radius:8px;padding:10px 14px;margin:12px 0}
.card.done{border-color:#6b6;background:#f3fbf3}.card h2{font-size:16px;margin:0 0 6px}
.r0{border-left:6px solid #c00}.r1{border-left:6px solid #e60}.r2{border-left:6px solid #e90}.r3{border-left:6px solid #bbb}
.mine{background:#f4f4f4;padding:6px 8px;border-radius:4px;white-space:pre-wrap;font-size:14px}
.chk{border-top:1px dashed #ccc;margin-top:8px;padding-top:6px;font-size:14px}
.doubt{font-weight:600;color:#7a3e00}.prop{background:#eef6ff;padding:6px 8px;border-radius:4px;white-space:pre-wrap}
q{font-style:italic;background:#fffbe6;display:block;padding:4px 8px;border-left:3px solid #e6d9a0;margin:4px 0}
.bad{color:#c00;font-weight:600}.tag{font-size:12px;padding:1px 6px;border-radius:4px;background:#eee;margin-right:4px}
button{font-size:14px;padding:5px 10px;margin:6px 6px 0 0;cursor:pointer}textarea{width:100%;font:14px/1.4 system-ui;box-sizing:border-box}
details.hp{font-size:12px;color:#555}details.hp div{background:#fffbe6;border:1px solid #e6d9a0;padding:6px;border-radius:4px}
</style></head><body>
<div id="bar"><span id="pos"></span><span id="counts"></span><span><button id="prev">← anterior</button><button id="next">seguinte →</button><button id="nextopen">próximo por decidir</button></span></div>
<h1 id="title"></h1><div class="meta" id="meta"></div><div id="cards"></div>
<p class="meta">Cor à esquerda: <b style="color:#c00">vermelho</b> as 2 verificações dizem que está errado · <b style="color:#e60">laranja</b> as 2 assinalam · <b style="color:#e90">amarelo</b> só 1, problema importante · cinzento só 1, menor.
Para cada campo: lê a dúvida, abre o PDF na página e lê a citação; depois <b>Mantenho</b> (o teu valor fica), <b>Aceito</b> a proposta, ou <b>Edito</b>. A IA não muda nada sem ti.</p>
<script>
__QH__
const $=id=>document.getElementById(id);
const esc=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const RK=["as 2 verificações: errado","as 2 verificações assinalam","1 verificação, importante","1 verificação, menor"];
const ACT={keep:"mantive o meu",accept1:"aceitei a proposta 1",accept2:"aceitei a proposta 2",edit:"editei"};
let Q=[],i=0,R=null;
const pdf=(k,p)=>"/pdf?key="+encodeURIComponent(k)+((String(p||"").match(/\d+/)||[])[0]?"#page="+String(p).match(/\d+/)[0]:"");
async function load(){Q=await (await fetch("/queue")).json();i=Math.max(0,Q.findIndex(x=>x.open));show();}
function counts(){const f=Q.reduce((a,x)=>a+x.n,0),o=Q.reduce((a,x)=>a+x.open,0);
  $("counts").textContent=`${Q.length} registos com dúvidas · ${f-o}/${f} campos decididos`;}
async function show(){counts();if(!Q.length){$("title").textContent="Sem campos assinalados (ainda).";return;}
  const x=Q[i],k=x.key;R=await (await fetch("/record?key="+encodeURIComponent(k))).json();if(Q[i].key!==k)return;
  $("pos").textContent=`#${i+1} de ${Q.length}`;$("title").textContent=x.title;
  $("meta").innerHTML=`${esc(k)} · ${x.n} campo(s) · <a href="${pdf(k)}" target="_blank">abrir PDF</a>`;
  $("cards").innerHTML=R.flags.map((fl,j)=>{const mine=R.fields[fl.f]||{},d=R.dec[fl.f];
    const qh=QH[fl.f]?`<details class="hp"><summary>${esc(QH[fl.f][0])} ?</summary><div><b>Sim (1):</b> ${QH[fl.f][1]}<br><b>Parcial (0.5):</b> ${QH[fl.f][2]}<br><b>Não (0):</b> ${QH[fl.f][3]}<br><b>Onde ver:</b> ${QH[fl.f][4]}</div></details>`:"";
    return `<div class="card r${fl.rank} ${d?"done":""}"><h2>${esc(fl.f)} <span class="tag">${RK[fl.rank]}</span>${d?`<span class="tag">✓ ${ACT[d.action]}</span>`:""}</h2>${qh}
     <div class="meta">O teu valor (pág. ${esc(mine.p)}):</div><div class="mine">${esc(d?d.prev:mine.v)}</div>
     ${[1,2].filter(n=>fl.checks[n]).map(n=>{const c=fl.checks[n];return `<div class="chk"><span class="tag">verificação ${n}: ${c.verdict==="corrected"?"errado":"incerto"}${c.sev==="high"?", importante":""}</span>
       <div class="doubt">${esc(c.doubt)}</div>
       <q>${esc(c.quote)}</q>${c.q_ok?"":'<span class="bad">⚠ citação não encontrada no texto: confirma no PDF</span> '}<span class="meta">${esc(c.where)} · <a href="${pdf(x.key,c.p)}" target="_blank">abrir pág. ${esc(c.p)}</a></span>
       <div class="meta">Proposta ${n}:</div><div class="prop">${esc(c.v)}</div>
       <button data-a="accept${n}" data-j="${j}">Aceito a proposta ${n}</button></div>`;}).join("")}
     <button data-a="keep" data-j="${j}">Mantenho o meu</button><button data-a="editopen" data-j="${j}">Edito…</button>
     <div id="ed${j}" style="display:none"><textarea rows="4">${esc(mine.v)}</textarea>página(s) <input value="${esc(mine.p)}" size="8"> <button data-a="edit" data-j="${j}">Gravar edição</button></div></div>`;}).join("");
  document.querySelectorAll("#cards button").forEach(b=>b.onclick=()=>act(b.dataset.a,+b.dataset.j));}
async function act(a,j){const fl=R.flags[j];
  if(a==="editopen"){$("ed"+j).style.display="block";return;}
  const body={key:Q[i].key,field:fl.f,action:a};
  if(a==="edit"){body.value=$("ed"+j).querySelector("textarea").value;body.p=$("ed"+j).querySelector("input").value;}
  if(a.startsWith("accept"))body.p=fl.checks[+a.slice(-1)].p;
  const r=await fetch("/decide",{method:"POST",body:JSON.stringify(body)});
  if(!r.ok){alert("ERRO ao gravar: "+((await r.json()).error||"")+". Não avances.");return;}
  Q=await (await fetch("/queue")).json();show();}
$("prev").onclick=()=>{if(i>0){i--;show();scrollTo(0,0);}};
$("next").onclick=()=>{if(i<Q.length-1){i++;show();scrollTo(0,0);}};
$("nextopen").onclick=()=>{const n=Q.findIndex((x,j)=>j>i&&x.open);if(n<0){alert("Não há mais campos por decidir a seguir a este.");return;}i=n;show();scrollTo(0,0);};
load();
</script></body></html>"""

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "serve"
    if cmd == "prep":
        prep()
    elif cmd == "status":
        status()
    else:
        srv = ThreadingHTTPServer(("127.0.0.1", 8766), H)
        print("Final review at http://127.0.0.1:8766  (Ctrl+C to stop; decisions in", DEC + ")")
        webbrowser.open("http://127.0.0.1:8766")
        srv.serve_forever()
