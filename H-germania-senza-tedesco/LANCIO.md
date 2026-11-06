# Test H: "Germania senza tedesco": cosa è pronto e come lanciarlo

## Pronto
- `kit/germania-senza-tedesco-kit.pdf`: **il prodotto**. 33 pagine: 31 lettere bilingue, checklist dei primi 30 giorni, glossario. Si rigenera con `python3 kit/build.py` dopo ogni modifica a `kit/lettere.py`.
- `sito/index.html`: landing con la descrizione del kit e il pulsante di acquisto (al posto di `GUMROAD_URL` va il link vero).
- `sito/disdetta/`: generatore gratuito di disdette (la calamita del traffico).
- `sito/guide/anmeldung-monaco.html`: prima guida.
- `sito/lettere/`: 10 lettere gratuite, una pagina ciascuna, scelte tra le ricerche più comuni (affitto, cauzione, palestra, dimissioni, Steuer-ID...). Portano traffico da Google verso il kit, che ne ha 31 più checklist e glossario.

## Impegno per Manu: circa 1 ora in tutto. Ritorno: 0-100 € in settimana, poi cresce con Google
1. **Rileggi il PDF (30 min).** Sei tu che lo vendi: se trovi una frase che non ti convince, me la segnali e la sistemo. Le lettere in tedesco le ho controllate sulle leggi citate.
2. **Apri Gumroad (10 min)** su gumroad.com con la tua email. Crea un prodotto digitale, carica il PDF, prezzo 14 €, e incolla i testi qui sotto. Mandami il link del prodotto.
3. **Pubblicazione del sito**: quando la Claude GitHub App ha accesso al repo, lo pubblico io su GitHub Pages e metto il link Gumroad nel pulsante.
4. **Post nelle community (20 min)**, solo dopo che il sito è online. Vedi le regole sotto.

Commissione Gumroad: 10% + 0,50 $ a vendita più i costi della carta (in tutto circa il 13% + 0,80 $), nessun costo fisso. Dal 2025 Gumroad fa da venditore ufficiale (merchant of record) e incassa e versa l'IVA per te.
Rimborso entro 14 giorni: l'ho scritto nella landing, perché aumenta la fiducia. Lo gestisci da Gumroad con un clic. Se non lo vuoi offrire, dimmelo e lo tolgo.

## Testi per Gumroad

**Nome:** Germania senza tedesco: 31 lettere in tedesco pronte, con traduzione

**Descrizione:**
> Vivi in Germania e non parli (ancora) bene il tedesco? Questo kit ti dà 31 lettere ed email in tedesco pronte da copiare, con la traduzione in italiano accanto, per le situazioni che capitano a tutti:
>
> 🏠 **Casa:** disdetta dell'affitto, conferma per l'Anmeldung, muffa e guasti, restituzione della cauzione, conguaglio spese, subaffitto, rumori, candidatura per un appartamento.
> 📄 **Contratti:** palestra, cellulare, internet, luce e gas, abbonamenti, recesso da acquisti online, assicurazioni, conto in banca, fatture contestate, pacchi mai arrivati.
> 💼 **Lavoro:** dimissioni, Arbeitszeugnis, malattia, ferie, Lohnsteuerbescheinigung.
> 🏛️ **Uffici:** Steuer-ID, ricorso al Finanzamt, proroga, Krankenkasse, canone TV, Kita, medico.
>
> Per ogni lettera: quando usarla, se basta un'email o serve la raccomandata, le scadenze e le trappole da evitare.
> In più: checklist dei primi 30 giorni in Germania e glossario della burocrazia.
>
> PDF di 33 pagine, download immediato. Curato da un italiano che vive a Monaco dal 2023.
> Modelli informativi, non consulenza legale.

**Riepilogo (una riga):** 31 lettere in tedesco con traduzione italiana, per casa, contratti, lavoro e uffici.

## Dove promuoverlo, e come farlo senza spam
Regola d'oro: **prima aiuti, poi linki**, e solo dove le regole del gruppo lo permettono. Leggi le regole di ogni gruppo prima di scrivere. Un post per gruppo, mai lo stesso messaggio copiato in 20 gruppi nello stesso giorno.

**Dove:** gruppi Facebook di italiani in Germania e nelle città grandi (Berlino, Monaco, Amburgo, Francoforte, Colonia, Stoccarda), r/italy e r/germany su Reddit (nelle discussioni su chi si trasferisce), forum di expat.

**Post (per i gruppi dove l'autopromozione è permessa, o nel giorno dedicato):**
> Ciao a tutti! Vivo a Monaco da 3 anni e all'inizio le lettere in tedesco erano il mio incubo: disdetta della palestra, la cauzione che non tornava, la Steuer-ID che non arrivava.
>
> Ho fatto un generatore gratuito di lettere di disdetta: compili in italiano ed esce la lettera in tedesco con la traduzione, pronta da stampare. Niente registrazione: [LINK GENERATORE]
>
> Spero vi sia utile. Se avete casi che non copre, scrivetemelo e lo aggiungo.

(Nel post non si nomina il kit a pagamento: è nel sito. Il gruppo vede uno strumento gratuito, non una pubblicità.)

**Risposta tipo, quando qualcuno chiede "come disdico X?":**
> Ti serve una lettera di Kündigung: per [X] di solito basta un'email, con preavviso di [N]. Se vuoi, qui la generi già in tedesco con la traduzione: [LINK]. Ricordati di chiedere la conferma scritta della data di fine.

## Metrica per decidere (dopo 72 ore dal primo post)
- Visite al generatore > 200 e almeno 1 vendita: si continua e si fa la versione inglese.
- Visite > 200 e 0 vendite: il problema è il kit o il prezzo. Si prova a 9 € e si aggiunge un'anteprima gratuita di 3 lettere.
- Visite < 50: il problema è la distribuzione. Si cambiano canale e messaggio.
