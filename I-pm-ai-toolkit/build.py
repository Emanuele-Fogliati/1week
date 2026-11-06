"""Builds toolkit.html and pm-ai-toolkit.pdf from contenuto.py."""
import html, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from contenuto import TEMPLATES, PROMPTS
E = html.escape

def inline(t):
    t = E(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    return t

def md(src):
    out, lines, i = [], src.split("\n"), 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-| ]+\|$", lines[i]):
                    rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            head, body = rows[0], rows[1:]
            out.append("<table><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr>" +
                       "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</table>")
            continue
        if l.startswith("- ") or l.startswith("> "):
            items = []
            while i < len(lines) and (lines[i].startswith("- ") or lines[i].startswith("> ")):
                items.append(lines[i][2:]); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        m = re.match(r"^(#{1,3}) (.*)", l)
        if m:
            lvl = len(m.group(1)) + 2
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
        elif l.strip():
            out.append(f"<p>{inline(l)}</p>")
        i += 1
    return "\n".join(out)

def build():
    tpl = "".join(f"""<section class="tpl"><div class="k">Template {n}</div><h2>{E(t)}</h2><p class="why">{E(w)}</p><div class="sheet">{md(body)}</div></section>"""
                  for n, (t, w, body) in enumerate(TEMPLATES, 1))
    pr, n = "", 0
    for cat, items in PROMPTS.items():
        pr += f"<h2 class='pcat'>{E(cat)}</h2>"
        for title, text in items:
            n += 1
            pr += f"<div class='prompt'><div class='k'>Prompt {n}</div><h3>{E(title)}</h3><pre>{E(text)}</pre></div>"
    toc = "".join(f"<li>Template {i}: {E(t)}</li>" for i, (t, _, _) in enumerate(TEMPLATES, 1))
    toc += "".join(f"<li>Prompts: {E(c)} ({len(v)})</li>" for c, v in PROMPTS.items())
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>PM AI Toolkit</title><style>
body{{font-family:"DejaVu Sans",Arial,sans-serif;color:#141821;font-size:10.5pt;line-height:1.5}}
.cover{{height:255mm;display:flex;flex-direction:column;justify-content:center;page-break-after:always}}
.cover .k{{color:#4338ca;letter-spacing:3px;text-transform:uppercase;font-size:10pt}}.cover h1{{font-size:44pt;line-height:1;margin:12px 0}}
.cover .sub{{font-size:14pt;color:#5b6170;max-width:140mm}}
.k{{color:#4338ca;letter-spacing:1.5px;text-transform:uppercase;font-size:8.5pt}}
.pg{{page-break-after:always}}
.tpl{{page-break-before:always}}.tpl h2{{font-size:20pt;margin:2px 0 4px}}.why{{color:#5b6170;margin:0 0 12px}}
.sheet{{border:1px solid #e3e4ea;border-radius:8px;padding:14px 16px;background:#fafafc}}
.sheet h3{{font-size:14pt;margin:6px 0}}.sheet h4{{font-size:11.5pt;margin:12px 0 4px;color:#312e81}}.sheet h5{{font-size:10.5pt;margin:10px 0 4px}}
.sheet p{{margin:4px 0}}
table{{border-collapse:collapse;width:100%;font-size:9pt;margin:6px 0}}th,td{{border:1px solid #d9dbe3;padding:5px;text-align:left;vertical-align:top}}th{{background:#eef0fb}}
h2.pcat{{page-break-before:always;font-size:20pt;color:#312e81;border-bottom:2px solid #4338ca;padding-bottom:6px}}
.prompt{{page-break-inside:avoid;margin:0 0 12px;border:1px solid #e3e4ea;border-radius:8px;padding:10px 12px}}.prompt h3{{margin:2px 0 6px;font-size:12pt}}
pre{{white-space:pre-wrap;font-family:"DejaVu Sans Mono",monospace;font-size:8.8pt;background:#f3f4f8;border-radius:6px;padding:8px;margin:0}}
</style></head><body>
<div class="cover"><div class="k">For product managers and product owners</div><h1>PM AI Toolkit</h1>
<div class="sub">{len(TEMPLATES)} battle-tested templates and {n} AI prompts to go from raw customer notes to a sprint-ready backlog in hours, not weeks.</div></div>
<div class="pg"><h2>How to use this toolkit</h2>
<p>The templates give structure; the prompts do the first draft. Your job is judgment: check every assumption, cut what doesn't matter, and decide.</p>
<p><b>Rules that make AI output good:</b></p><ul>
<li>Always paste real context: notes, data, quotes. No context, generic output.</li>
<li>Ask the model to mark assumptions as [ASSUMPTION] and never to invent data.</li>
<li>Iterate: "make it shorter", "what's missing", "argue against this".</li>
<li>Never paste confidential company or customer data into tools your company hasn't approved.</li></ul>
<h3>Contents</h3><ul>{toc}</ul></div>
{tpl}{pr}</body></html>"""
    open(os.path.join(HERE, "toolkit.html"), "w").write(doc)
    js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{HERE}/toolkit.html');await p.pdf({{path:'{HERE}/pm-ai-toolkit.pdf',format:'A4',printBackground:true,displayHeaderFooter:true,headerTemplate:'<span></span>',
footerTemplate:'<div style="font-size:8px;width:100%;text-align:center;color:#888">PM AI Toolkit · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
margin:{{top:'16mm',bottom:'18mm',left:'15mm',right:'15mm'}}}});await b.close();}})()"""
    subprocess.run(["node", "-e", js], check=True)
    print("ok", len(TEMPLATES), "templates", n, "prompts")

if __name__ == "__main__":
    build()
