"""Genera kit.html e kit.pdf dal contenuto in lettere.py."""
import html, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lettere import LETTERE, MITTENTE

E = html.escape
ORDINE = ["Casa e affitto", "Contratti e abbonamenti", "Lavoro", "Uffici e burocrazia"]

CHECKLIST = [
 ("Settimana 1", ["Chiedi al padrone di casa la Wohnungsgeberbestätigung (lettera 2).",
   "Prenota l'appuntamento per l'Anmeldung al Bürgeramt: va fatta entro 14 giorni dal trasloco.",
   "Metti il tuo nome sulla cassetta delle lettere e sul campanello: senza, la posta ufficiale non arriva.",
   "Fai il verbale di consegna dell'appartamento (Übergabeprotokoll) con foto di ogni stanza e dei contatori."]),
 ("Settimana 2", ["Fai l'Anmeldung e conserva la Meldebestätigung: te la chiederanno banca, datore di lavoro e altri uffici.",
   "Iscriviti a una cassa malattia (Krankenkasse): se sei dipendente è obbligatoria e va comunicata al datore di lavoro.",
   "Apri un conto corrente tedesco (Girokonto) con IBAN DE, utile per affitto e addebiti."]),
 ("Settimane 3-4", ["Aspetta la Steuer-ID per posta (2-4 settimane): dalla al datore di lavoro. Se non arriva, lettera 25.",
   "Ti arriverà una lettera del Beitragsservice per il canone radiotelevisivo: si paga per appartamento, rispondi entro i termini.",
   "Valuta un'assicurazione di responsabilità civile privata (Privathaftpflicht): costa poco ed è considerata quasi indispensabile.",
   "Se resti più di 12 mesi, iscriviti all'AIRE tramite il Consolato italiano."]),
]

GLOSSARIO = [
 ("Anmeldung", "registrazione della residenza al Comune"), ("Bürgeramt / Bürgerbüro", "ufficio anagrafe"),
 ("Meldebestätigung", "certificato di residenza"), ("Wohnungsgeberbestätigung", "conferma del locatore per la residenza"),
 ("Steuer-ID", "codice fiscale tedesco personale"), ("Steuernummer", "numero fiscale assegnato dal Finanzamt per le dichiarazioni"),
 ("Finanzamt", "ufficio delle imposte"), ("Steuerbescheid", "avviso di imposta"), ("Einspruch", "ricorso"),
 ("Krankenkasse", "cassa malattia"), ("gesetzlich / privat versichert", "assicurato pubblico / privato"),
 ("Kündigung", "disdetta (o licenziamento)"), ("fristgerecht", "nel rispetto del preavviso"),
 ("zum nächstmöglichen Zeitpunkt", "alla prima data possibile"), ("Kündigungsfrist", "termine di preavviso"),
 ("Mindestvertragslaufzeit", "durata minima del contratto"), ("Widerruf", "recesso (entro 14 giorni)"),
 ("Widerspruch", "contestazione, opposizione"), ("Mahnung", "sollecito di pagamento"), ("Inkasso", "recupero crediti"),
 ("Mahnbescheid", "decreto ingiuntivo (2 settimane per opporsi)"), ("Kaltmiete / Warmmiete", "affitto senza / con spese"),
 ("Nebenkosten", "spese accessorie (condominio, acqua, rifiuti)"), ("Kaution", "deposito cauzionale"),
 ("Hausverwaltung", "amministrazione dello stabile"), ("Mangel", "difetto dell'appartamento"),
 ("Schriftform", "forma scritta con firma a mano"), ("Textform", "forma testuale: basta un'email"),
 ("Einschreiben mit Rückschein", "raccomandata con ricevuta di ritorno"), ("SCHUFA", "centrale rischi, il \"punteggio\" di affidabilità"),
 ("Arbeitszeugnis", "attestato di servizio"), ("Lohnsteuerbescheinigung", "certificazione annuale dei redditi da lavoro"),
]

def p(x): return f"<p>{E(x)}</p>"

def lettera_html(i, l):
    note = "".join(f"<li>{E(n)}</li>" for n in l["note"])
    return f"""
<section class="lettera">
  <div class="num">Lettera {i}</div>
  <h3>{E(l['titolo'])}</h3>
  <p class="quando"><b>Quando usarla:</b> {E(l['quando'])}</p>
  <ul class="note">{note}</ul>
  <div class="cols">
    <div class="de"><div class="lbl">Testo in tedesco</div><pre>{E(MITTENTE)}

{E(l['de'])}</pre></div>
    <div class="it"><div class="lbl">Cosa stai scrivendo (traduzione)</div><pre>{E(l['it'])}</pre></div>
  </div>
</section>"""

def build():
    parts, n, indice = [], 0, []
    for cat in ORDINE:
        ls = [l for l in LETTERE if l["cat"] == cat]
        parts.append(f'<h2 class="cat">{E(cat)}</h2>')
        for l in ls:
            n += 1
            indice.append((n, cat, l["titolo"]))
            parts.append(lettera_html(n, l))
    idx_html, last = "", None
    for k, cat, t in indice:
        if cat != last:
            idx_html += f'<li class="icat">{E(cat)}</li>'; last = cat
        idx_html += f"<li>{k}. {E(t)}</li>"
    check = "".join(f"<h3>{E(w)}</h3><ul class='check'>" + "".join(f"<li>{E(x)}</li>" for x in xs) + "</ul>" for w, xs in CHECKLIST)
    glos = "".join(f"<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>" for a, b in GLOSSARIO)
    doc = f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Germania senza tedesco: il kit</title>
<style>
@page {{ size: A4; margin: 16mm 15mm 18mm; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; color:#17202a; font-size:10.5pt; line-height:1.5; }}
.cover {{ height: 255mm; display:flex; flex-direction:column; justify-content:center; page-break-after:always; }}
.cover .k {{ color:#0b6e4f; letter-spacing:3px; font-size:10pt; text-transform:uppercase; }}
.cover h1 {{ font-size:40pt; line-height:1.05; margin:10px 0 16px; }}
.cover .sub {{ font-size:14pt; color:#5b6470; max-width:140mm; }}
.cover .box {{ margin-top:30px; border-left:4px solid #0b6e4f; padding-left:14px; color:#5b6470; }}
h2 {{ font-size:20pt; margin:0 0 10px; }}
h2.cat {{ page-break-before:always; color:#0b6e4f; border-bottom:2px solid #0b6e4f; padding-bottom:6px; }}
.pg {{ page-break-after:always; }}
.lettera {{ page-break-inside:avoid; margin:0 0 18px; padding:12px 14px; border:1px solid #e2e2da; border-radius:8px; }}
.num {{ font-size:8.5pt; letter-spacing:1.5px; text-transform:uppercase; color:#0b6e4f; }}
.lettera h3 {{ font-size:13pt; margin:2px 0 6px; }}
.quando {{ margin:0 0 4px; }}
.note {{ margin:0 0 8px; padding-left:16px; color:#3d4650; font-size:9.5pt; }}
.cols {{ display:grid; grid-template-columns: 1.1fr .9fr; gap:10px; }}
.lbl {{ font-size:8pt; text-transform:uppercase; letter-spacing:1px; color:#5b6470; margin-bottom:3px; }}
pre {{ white-space:pre-wrap; font-family:inherit; margin:0; font-size:9pt; line-height:1.42; }}
.de pre {{ background:#fafaf7; border:1px solid #e2e2da; border-radius:6px; padding:8px; }}
.it pre {{ background:#e6f2ec; border-radius:6px; padding:8px; color:#2c3a33; }}
ul.idx {{ list-style:none; padding:0; columns:2; font-size:8.6pt; line-height:1.3; }} ul.idx li.icat {{ font-weight:bold; color:#0b6e4f; margin-top:6px; }}
ul.check li {{ margin-bottom:4px; }}
table {{ border-collapse:collapse; width:100%; font-size:9.5pt; }} td {{ border-bottom:1px solid #e2e2da; padding:4px 6px; vertical-align:top; }}
.warn {{ background:#fff6e0; border:1px solid #f0d58a; border-radius:8px; padding:10px 12px; font-size:9.5pt; }}
</style></head><body>
<div class="cover">
  <div class="k">Il kit pratico per italiani in Germania</div>
  <h1>Germania senza tedesco</h1>
  <div class="sub">{len(LETTERE)} lettere ed email in tedesco pronte da copiare, con la traduzione accanto. Più la checklist dei primi 30 giorni e il glossario della burocrazia.</div>
  <div class="box">Edizione novembre 2026<br>Curato da un italiano che vive a Monaco di Baviera dal 2023.</div>
</div>

<div class="pg">
<h2>Come usare questo kit</h2>
<p>Ogni lettera ha tre parti: <b>quando usarla</b>, le <b>note pratiche</b> (scadenze, forma, trappole) e il <b>testo in tedesco</b> con la traduzione accanto, così sai sempre cosa stai firmando.</p>
<p>Sostituisci tutto ciò che è tra [parentesi quadre]. Le parti separate da una barra (/) sono alternative: tieni quella giusta e cancella l'altra.</p>
<h3>Email o lettera firmata?</h3>
<p><b>Textform</b> (forma testuale): basta un'email. Vale per la maggior parte delle disdette di abbonamenti, palestre e contratti con i consumatori, salvo che il contratto chieda altro.</p>
<p><b>Schriftform</b> (forma scritta): serve la carta firmata a mano. È obbligatoria per la <b>disdetta dell'affitto</b> e per le <b>dimissioni dal lavoro</b>. Un'email in questi casi non vale.</p>
<h3>Come spedire le lettere importanti</h3>
<p>Usa la raccomandata con ricevuta di ritorno (<i>Einschreiben mit Rückschein</i>) in un ufficio postale, oppure consegna a mano davanti a un testimone. Tieni sempre una copia e la ricevuta.</p>
<div class="warn"><b>Importante.</b> Queste lettere sono modelli standard, scritti con cura e controllati sulle leggi citate, ma non sono consulenza legale. Le regole possono cambiare e il tuo contratto può prevedere condizioni diverse. Per casi complicati (cause, licenziamenti, grossi importi) rivolgiti a un Mieterverein, a un sindacato, a un avvocato o a uno Steuerberater.</div>
<h3>Indice delle lettere</h3>
<ul class="idx">{idx_html}</ul>
</div>

<div class="pg">
<h2>Checklist dei primi 30 giorni</h2>
{check}
<h2 style="margin-top:22px">Glossario della burocrazia</h2>
<table>{glos}</table>
</div>

{''.join(parts)}
</body></html>"""
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "kit.html"), "w").write(doc)
    js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{here}/kit.html');await p.pdf({{path:'{here}/germania-senza-tedesco-kit.pdf',format:'A4',printBackground:true,
displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:'<div style="font-size:8px;width:100%;text-align:center;color:#888">Germania senza tedesco · pagina <span class="pageNumber"></span> di <span class="totalPages"></span></div>',
margin:{{top:'16mm',bottom:'18mm',left:'15mm',right:'15mm'}}}});await b.close();}})()"""
    subprocess.run(["node", "-e", js], check=True)
    print("ok", n, "lettere")

if __name__ == "__main__":
    build()
