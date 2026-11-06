# Contenuto del kit "Germania senza tedesco": lettere bilingue.
# Ogni lettera: categoria, titolo, quando usarla, note pratiche, testo tedesco, traduzione italiana.
# I segnaposto tra [parentesi quadre] si sostituiscono con i propri dati.

MITTENTE = """[Vorname Nachname]
[Straße Hausnummer]
[PLZ Ort]"""

LETTERE = [
# ---------------- CASA ----------------
dict(cat="Casa e affitto", titolo="Disdetta del contratto d'affitto (inquilino)",
quando="Vuoi lasciare l'appartamento in affitto.",
note=["Per legge l'inquilino ha 3 mesi di preavviso (§ 573c BGB). La disdetta deve arrivare entro il terzo giorno lavorativo del mese per contare da quel mese.",
      "Serve la forma scritta con firma a mano (§ 568 BGB): email, fax o WhatsApp non bastano. Spedisci con raccomandata (Einschreiben mit Rückschein) o consegna a mano davanti a un testimone.",
      "Se nel contratto c'è un periodo minimo (Kündigungsverzicht), controllalo prima."],
de="""[Vermieter Name]
[Straße Hausnummer]
[PLZ Ort]

[Ort], [Datum]

Kündigung des Mietverhältnisses über die Wohnung [Straße Hausnummer, Etage/Lage, PLZ Ort]

Sehr geehrte/r [Frau/Herr Nachname],

hiermit kündige ich das oben genannte Mietverhältnis fristgerecht zum [Datum], hilfsweise zum nächstmöglichen Zeitpunkt.

Bitte bestätigen Sie mir den Eingang dieser Kündigung und das Ende des Mietverhältnisses schriftlich. Für die Wohnungsübergabe schlage ich einen Termin in der letzten Woche des Mietverhältnisses vor und bitte Sie um Rückmeldung.

Die Mietkaution überweisen Sie bitte nach ordnungsgemäßer Abrechnung auf folgendes Konto:
IBAN: [IBAN], Kontoinhaber: [Name]

Mit freundlichen Grüßen

[Unterschrift]
[Vorname Nachname]""",
it="""Disdetta del contratto di locazione per l'appartamento [indirizzo]

Gentile [Signora/Signor Cognome],
con la presente disdico il contratto di locazione sopra indicato nel rispetto dei termini, al [data], o in subordine alla prima data possibile.
La prego di confermarmi per iscritto la ricezione della disdetta e la data di fine locazione. Per la riconsegna dell'appartamento propongo un appuntamento nell'ultima settimana di locazione e attendo un Suo riscontro.
La prego di versare il deposito cauzionale, dopo il regolare conteggio, sul seguente conto: [IBAN].
Cordiali saluti"""),

dict(cat="Casa e affitto", titolo="Richiesta della Wohnungsgeberbestätigung",
quando="Ti serve la conferma del padrone di casa per registrare la residenza (Anmeldung).",
note=["Il padrone di casa è obbligato a dartela (§ 19 Bundesmeldegesetz).",
      "La registrazione va fatta entro 14 giorni dal trasloco: chiedila subito, anche prima di entrare."],
de="""Betreff: Wohnungsgeberbestätigung für [Straße Hausnummer]

Sehr geehrte/r [Frau/Herr Nachname],

ich bin am [Datum] in die Wohnung [Straße Hausnummer, PLZ Ort] eingezogen. Für meine Anmeldung beim Bürgeramt benötige ich eine Wohnungsgeberbestätigung nach § 19 Bundesmeldegesetz.

Könnten Sie mir diese bitte bis zum [Datum] ausgefüllt und unterschrieben zusenden? Ein Scan per E-Mail genügt.

Vielen Dank und freundliche Grüße
[Vorname Nachname]""",
it="""Oggetto: conferma del locatore per [indirizzo]
Gentile [Signora/Signor Cognome],
sono entrato nell'appartamento [indirizzo] il [data]. Per la registrazione all'ufficio anagrafe mi serve la conferma del locatore ai sensi del § 19 della legge federale sulla registrazione.
Potrebbe inviarmela compilata e firmata entro il [data]? Basta una scansione per email.
Grazie e cordiali saluti"""),

dict(cat="Casa e affitto", titolo="Segnalazione di un guasto o difetto (Mängelanzeige)",
quando="In casa c'è un problema: muffa, riscaldamento rotto, infiltrazioni, finestra che non chiude.",
note=["L'inquilino deve segnalare i difetti subito (§ 536c BGB). Se non lo fai, rischi di pagare tu i danni che peggiorano.",
      "Con un difetto serio puoi avere diritto a una riduzione dell'affitto (Mietminderung, § 536 BGB). Prima di ridurre, chiedi consiglio a un Mieterverein: un errore può costarti caro.",
      "Allega foto con data. Conserva una copia."],
de="""[Vermieter / Hausverwaltung]
[Straße Hausnummer]
[PLZ Ort]

[Ort], [Datum]

Mängelanzeige für die Wohnung [Straße Hausnummer, Etage/Lage]

Sehr geehrte Damen und Herren,

hiermit zeige ich Ihnen folgenden Mangel in meiner Wohnung an:
[Beschreibung, z. B. "Seit dem [Datum] funktioniert die Heizung im Wohnzimmer nicht mehr." / "Im Badezimmer hat sich an der Außenwand Schimmel gebildet."]

Fotos füge ich bei. Ich bitte Sie, den Mangel bis zum [Datum, ca. 14 Tage] zu beseitigen. Für einen Handwerkertermin erreichen Sie mich unter [Telefon / E-Mail].

Ich behalte mir vor, die Miete ab dem Zeitpunkt dieser Anzeige angemessen zu mindern, und zahle die Miete bis zur Beseitigung des Mangels nur unter Vorbehalt.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Segnalazione di difetto per l'appartamento [indirizzo]
Gentili signore e signori,
con la presente vi segnalo il seguente difetto nel mio appartamento: [descrizione].
Allego delle foto. Vi chiedo di eliminare il difetto entro il [data]. Per un appuntamento con un tecnico potete contattarmi a [telefono/email].
Mi riservo di ridurre l'affitto in misura adeguata a partire da questa segnalazione e pago l'affitto con riserva fino all'eliminazione del difetto.
Cordiali saluti"""),

dict(cat="Casa e affitto", titolo="Richiesta di restituzione della cauzione",
quando="Hai lasciato l'appartamento e il deposito cauzionale non è ancora tornato.",
note=["La legge non fissa un termine preciso. Il padrone di casa può trattenere una parte per i conguagli delle spese ancora aperti, ma di solito deve restituire il resto entro 3-6 mesi.",
      "Se non risponde, un Mieterverein o un avvocato può mandare una diffida formale."],
de="""Betreff: Rückzahlung der Mietkaution – Wohnung [Straße Hausnummer]

Sehr geehrte/r [Frau/Herr Nachname],

das Mietverhältnis über die oben genannte Wohnung endete am [Datum]; die Wohnung wurde am [Datum] übergeben.

Ich bitte Sie, mir die Mietkaution in Höhe von [Betrag] Euro zuzüglich Zinsen bis zum [Datum] auf folgendes Konto zu überweisen:
IBAN: [IBAN], Kontoinhaber: [Name]

Sollten Sie einen Teil der Kaution für eine noch ausstehende Nebenkostenabrechnung einbehalten wollen, teilen Sie mir bitte die Höhe und die Begründung schriftlich mit.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Oggetto: restituzione del deposito cauzionale – appartamento [indirizzo]
Gentile [Signora/Signor Cognome],
il contratto di locazione è terminato il [data]; l'appartamento è stato riconsegnato il [data].
La prego di versarmi il deposito cauzionale di [importo] euro, più interessi, entro il [data] sul seguente conto: [IBAN].
Se intende trattenere una parte del deposito per un conguaglio delle spese ancora da fare, La prego di comunicarmi per iscritto l'importo e la motivazione.
Cordiali saluti"""),

dict(cat="Casa e affitto", titolo="Richiesta di vedere le ricevute del conguaglio spese (Nebenkostenabrechnung)",
quando="Ti è arrivato un conguaglio delle spese condominiali che ti sembra troppo alto.",
note=["Hai diritto di vedere i documenti su cui si basa il conteggio (Belegeinsicht).",
      "Le obiezioni vanno fatte entro 12 mesi da quando ricevi il conteggio (§ 556 BGB)."],
de="""Betreff: Nebenkostenabrechnung [Jahr] – Bitte um Belegeinsicht

Sehr geehrte Damen und Herren,

ich habe die Nebenkostenabrechnung für das Jahr [Jahr] vom [Datum] erhalten. Bevor ich die Nachzahlung leiste, bitte ich um Einsicht in die zugrunde liegenden Belege, insbesondere zu folgenden Positionen: [z. B. Heizkosten, Hausmeister, Müllabfuhr].

Bitte teilen Sie mir mit, wann und wo ich die Belege einsehen kann, oder senden Sie mir Kopien per E-Mail.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Oggetto: conguaglio spese [anno] – richiesta di visione dei documenti
Gentili signore e signori,
ho ricevuto il conguaglio delle spese per l'anno [anno] del [data]. Prima di pagare la differenza chiedo di poter vedere i documenti su cui si basa, in particolare per queste voci: [voci].
Vi prego di indicarmi quando e dove posso vederli, oppure di inviarmene una copia per email.
Cordiali saluti"""),

dict(cat="Casa e affitto", titolo="Richiesta di permesso per subaffittare (Untervermietung)",
quando="Vuoi far entrare un coinquilino o subaffittare una stanza.",
note=["Serve il permesso del padrone di casa. Se hai un interesse legittimo nato dopo la firma del contratto (es. motivi economici o un partner che si trasferisce), di solito non può rifiutare senza un motivo serio (§ 553 BGB)."],
de="""Betreff: Bitte um Erlaubnis zur Untervermietung – Wohnung [Straße Hausnummer]

Sehr geehrte/r [Frau/Herr Nachname],

ich bitte Sie um Ihre Erlaubnis, ein Zimmer meiner Wohnung ab dem [Datum] an folgende Person unterzuvermieten:
[Vorname Nachname, Geburtsdatum, Beruf]

Grund dafür ist: [z. B. "Meine Arbeitszeit wurde reduziert, und ich möchte die Mietkosten teilen."]

Ich bleibe selbstverständlich Ihr Mieter und für die Miete verantwortlich. Über eine schriftliche Zustimmung bis zum [Datum] würde ich mich freuen.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Oggetto: richiesta di permesso di subaffitto – appartamento [indirizzo]
Gentile [Signora/Signor Cognome],
Le chiedo il permesso di subaffittare una stanza del mio appartamento dal [data] a questa persona: [dati].
Il motivo è: [motivo].
Resto naturalmente io il Suo inquilino e responsabile dell'affitto. Le sarei grato per un consenso scritto entro il [data].
Cordiali saluti"""),

dict(cat="Casa e affitto", titolo="Lamentela per rumori (alla Hausverwaltung)",
quando="Un vicino fa rumore di continuo, soprattutto di notte.",
note=["Prima prova a parlarci. Se non cambia nulla, scrivi all'amministrazione.",
      "Tieni un diario dei rumori (data, ora, tipo di rumore): è la prova più utile.",
      "In Germania la quiete notturna va di solito dalle 22 alle 6."],
de="""Betreff: Wiederholte Ruhestörung im Haus [Straße Hausnummer]

Sehr geehrte Damen und Herren,

ich wohne im Haus [Straße Hausnummer], [Etage/Lage]. Seit [Zeitraum] kommt es wiederholt zu erheblichem Lärm aus der Wohnung [Lage der Wohnung], besonders während der Nachtruhe, zum Beispiel am [Datum, Uhrzeit] und am [Datum, Uhrzeit].

Ein persönliches Gespräch hat leider keine Besserung gebracht. Ein Lärmprotokoll füge ich bei. Ich bitte Sie, die betreffenden Mieter auf die Hausordnung hinzuweisen.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Oggetto: disturbo ripetuto della quiete nel palazzo [indirizzo]
Gentili signore e signori,
abito nel palazzo [indirizzo], [piano]. Da [periodo] c'è spesso molto rumore dall'appartamento [posizione], soprattutto nelle ore notturne, per esempio il [data/ora] e il [data/ora].
Un colloquio di persona purtroppo non ha migliorato le cose. Allego un diario dei rumori. Vi chiedo di richiamare gli inquilini interessati al regolamento condominiale.
Cordiali saluti"""),

# ---------------- CONTRATTI ----------------
dict(cat="Contratti e abbonamenti", titolo="Disdetta della palestra",
quando="Vuoi chiudere l'iscrizione in palestra.",
note=["Per i contratti fatti dal 1° marzo 2022, dopo la durata minima si può di solito disdire con un mese di preavviso.",
      "Se ti sei iscritto online, il sito deve avere un pulsante \"Verträge hier kündigen\" (§ 312k BGB). È il metodo più veloce.",
      "Se il contratto non chiede di più, basta un'email (forma testuale)."],
de="""Kündigung meiner Mitgliedschaft
Mitgliedsnummer: [Nummer]

Sehr geehrte Damen und Herren,

hiermit kündige ich meine Mitgliedschaft fristgerecht zum nächstmöglichen Zeitpunkt.

Bitte bestätigen Sie mir den Eingang dieser Kündigung sowie das genaue Vertragsende schriftlich. Einer Verlängerung oder einem Rückgewinnungsanruf widerspreche ich.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Disdetta della mia iscrizione – numero di iscrizione [numero]
Gentili signore e signori,
con la presente disdico la mia iscrizione nel rispetto dei termini alla prima data possibile.
Vi prego di confermarmi per iscritto la ricezione della disdetta e la data esatta di fine contratto. Non acconsento a rinnovi né a telefonate per convincermi a restare.
Cordiali saluti"""),

dict(cat="Contratti e abbonamenti", titolo="Disdetta del contratto del cellulare",
quando="Vuoi chiudere un contratto telefonico mobile.",
note=["Se vuoi tenere il numero cambiando operatore, non disdire tu: chiedi la portabilità del numero al nuovo operatore.",
      "Dopo la durata minima (di solito 24 mesi), il contratto si disdice con un mese di preavviso."],
de="""Kündigung meines Mobilfunkvertrags
Kundennummer: [Nummer]
Rufnummer: [Nummer]

Sehr geehrte Damen und Herren,

hiermit kündige ich meinen Mobilfunkvertrag fristgerecht zum nächstmöglichen Zeitpunkt.

Bitte bestätigen Sie mir den Eingang der Kündigung sowie das genaue Vertragsende schriftlich. Einer telefonischen Kontaktaufnahme zu Werbezwecken widerspreche ich.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Disdetta del mio contratto di telefonia mobile – numero cliente [numero], numero di telefono [numero]
Gentili signore e signori,
con la presente disdico il mio contratto di telefonia mobile nel rispetto dei termini alla prima data possibile.
Vi prego di confermarmi per iscritto la ricezione della disdetta e la data esatta di fine contratto. Non acconsento a essere contattato per telefono a scopo pubblicitario.
Cordiali saluti"""),

dict(cat="Contratti e abbonamenti", titolo="Disdetta di internet per trasloco",
quando="Traslochi e all'indirizzo nuovo il tuo operatore non può darti la linea.",
note=["Se all'indirizzo nuovo l'operatore non offre lo stesso servizio, puoi disdire con un mese di preavviso anche durante la durata minima (§ 60 TKG). Allega la conferma di residenza nuova (Meldebestätigung)."],
de="""Sonderkündigung wegen Umzugs
Kundennummer: [Nummer]

Sehr geehrte Damen und Herren,

ich ziehe am [Datum] von [alte Adresse] nach [neue Adresse] um. Bitte teilen Sie mir mit, ob Sie die vertraglich vereinbarte Leistung an der neuen Adresse erbringen können.

Für den Fall, dass dies nicht möglich ist, kündige ich meinen Internetvertrag gemäß § 60 Abs. 2 TKG mit einer Frist von einem Monat zum [Datum], hilfsweise zum nächstmöglichen Zeitpunkt. Eine Meldebestätigung füge ich bei.

Bitte bestätigen Sie mir den Eingang und das Vertragsende schriftlich.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Disdetta straordinaria per trasloco – numero cliente [numero]
Gentili signore e signori,
il [data] mi trasferisco da [vecchio indirizzo] a [nuovo indirizzo]. Vi prego di comunicarmi se potete fornire il servizio previsto dal contratto al nuovo indirizzo.
Se non fosse possibile, disdico il mio contratto internet ai sensi del § 60 comma 2 della legge sulle telecomunicazioni con un mese di preavviso al [data], o in subordine alla prima data possibile. Allego la conferma di residenza.
Vi prego di confermarmi per iscritto la ricezione e la data di fine contratto.
Cordiali saluti"""),

dict(cat="Contratti e abbonamenti", titolo="Disdetta di luce o gas",
quando="Traslochi o vuoi chiudere la fornitura.",
note=["Se cambi solo fornitore, di solito la disdetta la fa il nuovo fornitore per te.",
      "Se traslochi, comunica la data e la lettura del contatore del giorno del trasloco (fai una foto)."],
de="""Kündigung meines Energieliefervertrags
Kundennummer: [Nummer]
Zählernummer: [Nummer]
Lieferadresse: [Straße Hausnummer, PLZ Ort]

Sehr geehrte Damen und Herren,

hiermit kündige ich meinen Liefervertrag für [Strom/Gas] wegen Auszugs zum [Datum].

Der Zählerstand am [Datum] beträgt: [Zählerstand]. Bitte senden Sie die Schlussrechnung an meine neue Adresse: [neue Adresse].
Ein eventuelles Guthaben überweisen Sie bitte auf folgendes Konto: IBAN [IBAN].

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Disdetta del mio contratto di fornitura di energia – numero cliente [numero], contatore [numero], indirizzo di fornitura [indirizzo]
Gentili signore e signori,
con la presente disdico il mio contratto di fornitura di [luce/gas] per trasloco al [data].
La lettura del contatore al [data] è: [lettura]. Vi prego di inviare la fattura finale al mio nuovo indirizzo: [indirizzo]. Un eventuale credito va versato sul conto [IBAN].
Cordiali saluti"""),

dict(cat="Contratti e abbonamenti", titolo="Disdetta di un abbonamento (streaming, giornale, club)",
quando="Qualsiasi abbonamento a rinnovo automatico.",
note=["Per i contratti online, cerca prima il pulsante \"Verträge hier kündigen\": per legge deve esserci.",
      "Basta un'email, salvo che il contratto chieda una forma diversa."],
de="""Kündigung meines Abonnements
Kunden-/Abonummer: [Nummer]

Sehr geehrte Damen und Herren,

hiermit kündige ich mein Abonnement [Name des Abonnements] fristgerecht zum nächstmöglichen Zeitpunkt.

Bitte bestätigen Sie mir den Eingang der Kündigung sowie das genaue Vertragsende schriftlich. Eine Einzugsermächtigung widerrufe ich zum Vertragsende.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Disdetta del mio abbonamento – numero cliente/abbonamento [numero]
Gentili signore e signori,
con la presente disdico il mio abbonamento [nome] nel rispetto dei termini alla prima data possibile.
Vi prego di confermarmi per iscritto la ricezione e la data esatta di fine contratto. Revoco l'autorizzazione all'addebito a partire dalla fine del contratto.
Cordiali saluti"""),

dict(cat="Contratti e abbonamenti", titolo="Recesso da un acquisto online (Widerruf)",
quando="Hai comprato online e vuoi restituire il prodotto entro 14 giorni.",
note=["Hai 14 giorni dal ricevimento della merce per recedere senza motivo (§ 355 BGB).",
      "Rimandare il pacco senza dire niente non basta: serve una dichiarazione chiara, anche per email."],
de="""Widerruf meines Vertrags
Bestellnummer: [Nummer], bestellt am [Datum], erhalten am [Datum]

Sehr geehrte Damen und Herren,

hiermit widerrufe ich den von mir abgeschlossenen Vertrag über den Kauf folgender Ware: [Artikel].

Bitte erstatten Sie mir den Kaufpreis innerhalb von 14 Tagen auf dem ursprünglichen Zahlungsweg und teilen Sie mir mit, wie ich die Ware zurücksenden soll.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Recesso dal mio contratto – ordine [numero], ordinato il [data], ricevuto il [data]
Gentili signore e signori,
con la presente recedo dal contratto di acquisto del seguente articolo: [articolo].
Vi prego di rimborsarmi il prezzo entro 14 giorni con lo stesso metodo di pagamento e di indicarmi come restituire la merce.
Cordiali saluti"""),

dict(cat="Contratti e abbonamenti", titolo="Disdetta di un'assicurazione",
quando="Vuoi chiudere un'assicurazione (responsabilità civile, casa, legale...).",
note=["Di solito si disdice con 3 mesi di preavviso sulla scadenza annuale. Guarda la data nella polizza.",
      "Se il premio aumenta, hai di solito un diritto di disdetta straordinaria entro un mese dalla comunicazione dell'aumento."],
de="""Kündigung meiner Versicherung
Versicherungsnummer: [Nummer]

Sehr geehrte Damen und Herren,

hiermit kündige ich meine [Art der Versicherung, z. B. Haftpflichtversicherung] fristgerecht zum Ablauf des Versicherungsjahres, hilfsweise zum nächstmöglichen Zeitpunkt.

Bitte bestätigen Sie mir den Eingang der Kündigung und das Vertragsende schriftlich.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Disdetta della mia assicurazione – numero di polizza [numero]
Gentili signore e signori,
con la presente disdico la mia [tipo di assicurazione] nel rispetto dei termini alla scadenza dell'anno assicurativo, o in subordine alla prima data possibile.
Vi prego di confermarmi per iscritto la ricezione e la data di fine contratto.
Cordiali saluti"""),

dict(cat="Contratti e abbonamenti", titolo="Chiusura del conto in banca",
quando="Vuoi chiudere un conto corrente.",
note=["Il cliente può chiudere il conto corrente in qualsiasi momento, senza preavviso (§ 675h BGB).",
      "Prima sposta stipendio, addebiti e abbonamenti sul conto nuovo."],
de="""Kündigung meines Girokontos
IBAN: [IBAN]

Sehr geehrte Damen und Herren,

hiermit kündige ich mein oben genanntes Girokonto zum [Datum / nächstmöglichen Zeitpunkt].

Bitte überweisen Sie das verbleibende Guthaben auf folgendes Konto: IBAN [neue IBAN], Kontoinhaber: [Name]. Bitte bestätigen Sie mir die Auflösung des Kontos schriftlich.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Chiusura del mio conto corrente – IBAN [IBAN]
Gentili signore e signori,
con la presente chiudo il mio conto corrente al [data / prima data possibile].
Vi prego di trasferire il saldo restante sul conto [nuovo IBAN] e di confermarmi per iscritto la chiusura del conto.
Cordiali saluti"""),

dict(cat="Contratti e abbonamenti", titolo="Contestazione di una fattura o di un sollecito",
quando="Ti arriva una fattura o un sollecito di pagamento che ritieni sbagliato.",
note=["Non ignorarlo: rispondi per iscritto e spiega perché non paghi. Se poi arriva un'agenzia di recupero crediti (Inkasso), manda la stessa lettera anche a loro.",
      "Se ricevi un decreto ingiuntivo giudiziario (gelber Brief, Mahnbescheid) hai solo 2 settimane per opporti: non aspettare."],
de="""Widerspruch gegen Ihre Rechnung / Mahnung vom [Datum]
Rechnungs-/Kundennummer: [Nummer]

Sehr geehrte Damen und Herren,

hiermit widerspreche ich Ihrer Forderung in Höhe von [Betrag] Euro.

Begründung: [z. B. "Der Vertrag wurde bereits zum [Datum] gekündigt; die Bestätigung liegt bei." / "Den Betrag habe ich am [Datum] bezahlt; der Zahlungsbeleg liegt bei."]

Ich fordere Sie auf, die Forderung zu stornieren und mir dies schriftlich zu bestätigen. Bis zur Klärung werde ich keine Zahlung leisten.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Contestazione della vostra fattura/sollecito del [data] – numero [numero]
Gentili signore e signori,
con la presente contesto la vostra richiesta di [importo] euro.
Motivo: [motivo].
Vi chiedo di annullare la richiesta e di confermarmelo per iscritto. Fino al chiarimento non effettuerò alcun pagamento.
Cordiali saluti"""),

dict(cat="Contratti e abbonamenti", titolo="Reclamo per un pacco mai arrivato",
quando="Hai pagato un ordine ma il pacco non è mai arrivato.",
note=["Quando compri da un negozio come privato, il rischio della spedizione è del venditore finché il pacco non ti viene consegnato. Scrivi al venditore, non al corriere."],
de="""Reklamation: Bestellung [Nummer] nicht erhalten

Sehr geehrte Damen und Herren,

am [Datum] habe ich bei Ihnen folgende Ware bestellt und bezahlt: [Artikel]. Bis heute habe ich die Lieferung nicht erhalten. Laut Sendungsverfolgung [Status, falls vorhanden].

Ich bitte Sie, mir die Ware bis zum [Datum] zu liefern oder den Kaufpreis zu erstatten.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Reclamo: ordine [numero] non ricevuto
Gentili signore e signori,
il [data] ho ordinato e pagato da voi il seguente articolo: [articolo]. Fino a oggi non l'ho ricevuto. Secondo il tracciamento [stato].
Vi chiedo di consegnarmi la merce entro il [data] o di rimborsarmi il prezzo.
Cordiali saluti"""),

# ---------------- LAVORO ----------------
dict(cat="Lavoro", titolo="Dimissioni (disdetta del contratto di lavoro)",
quando="Vuoi lasciare il lavoro.",
note=["Serve la forma scritta con firma a mano (§ 623 BGB): un'email non vale. Consegnala a mano e fatti firmare una ricevuta, o spediscila con raccomandata.",
      "Il preavviso di legge per il dipendente è di 4 settimane al 15 o alla fine del mese (§ 622 BGB), ma il tuo contratto può prevederne uno più lungo: controlla."],
de="""[Arbeitgeber, Personalabteilung]
[Straße Hausnummer]
[PLZ Ort]

[Ort], [Datum]

Kündigung meines Arbeitsverhältnisses

Sehr geehrte Damen und Herren,

hiermit kündige ich mein Arbeitsverhältnis ordentlich und fristgerecht zum [Datum], hilfsweise zum nächstmöglichen Zeitpunkt.

Bitte bestätigen Sie mir den Erhalt dieser Kündigung und das Beendigungsdatum schriftlich. Ich bitte außerdem um die Ausstellung eines qualifizierten Arbeitszeugnisses.

Für die gute Zusammenarbeit bedanke ich mich.

Mit freundlichen Grüßen

[Unterschrift]
[Vorname Nachname]""",
it="""Disdetta del mio rapporto di lavoro
Gentili signore e signori,
con la presente rassegno le dimissioni dal mio rapporto di lavoro, nel rispetto dei termini, al [data], o in subordine alla prima data possibile.
Vi prego di confermarmi per iscritto la ricezione e la data di fine rapporto. Vi chiedo inoltre di rilasciarmi un attestato di servizio qualificato.
Vi ringrazio per la buona collaborazione.
Cordiali saluti"""),

dict(cat="Lavoro", titolo="Richiesta dell'attestato di servizio (Arbeitszeugnis)",
quando="Lasci un lavoro o ti serve una valutazione intermedia per candidarti altrove.",
note=["Alla fine del rapporto hai diritto a un attestato scritto (§ 109 GewO). Quello \"qualificato\" descrive anche come hai lavorato: è quello che ti serve per candidarti."],
de="""Betreff: Bitte um ein qualifiziertes Arbeitszeugnis

Sehr geehrte/r [Frau/Herr Nachname],

mein Arbeitsverhältnis endet am [Datum]. Ich bitte Sie, mir ein qualifiziertes Arbeitszeugnis auszustellen, das neben meinen Aufgaben auch meine Leistung und mein Verhalten beurteilt.

Über eine Zusendung bis zum [Datum] würde ich mich freuen.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Oggetto: richiesta di attestato di servizio qualificato
Gentile [Signora/Signor Cognome],
il mio rapporto di lavoro termina il [data]. Le chiedo di rilasciarmi un attestato di servizio qualificato, che oltre alle mie mansioni valuti anche il mio rendimento e il mio comportamento.
Le sarei grato se potesse inviarmelo entro il [data].
Cordiali saluti"""),

dict(cat="Lavoro", titolo="Comunicazione di malattia al datore di lavoro",
quando="Stai male e non puoi andare a lavorare.",
note=["Devi avvisare il datore di lavoro subito, il primo giorno, prima dell'inizio del turno.",
      "Se hai l'assicurazione pubblica, il medico trasmette il certificato in modo elettronico (eAU): tu devi solo avvisare e andare dal medico. Molti contratti chiedono il certificato dal primo giorno, altri dal quarto: controlla."],
de="""Betreff: Krankmeldung [Vorname Nachname]

Guten Morgen [Name],

leider bin ich heute erkrankt und kann nicht zur Arbeit kommen. Voraussichtlich falle ich bis einschließlich [Datum] aus. Ich gehe heute zum Arzt; die Arbeitsunfähigkeitsbescheinigung wird elektronisch an die Krankenkasse übermittelt.

Dringende Themen: [z. B. "Das Meeting am Donnerstag kann [Kollege] übernehmen."]

Viele Grüße
[Vorname Nachname]""",
it="""Oggetto: comunicazione di malattia
Buongiorno [nome],
purtroppo oggi sono malato e non posso venire al lavoro. Prevedo di restare assente fino al [data] compreso. Oggi vado dal medico; il certificato di malattia verrà trasmesso in modo elettronico alla cassa malattia.
Questioni urgenti: [note].
Cordiali saluti"""),

dict(cat="Lavoro", titolo="Richiesta di ferie",
quando="Vuoi chiedere ferie per iscritto.",
note=["In Germania con 5 giorni lavorativi a settimana hai diritto per legge ad almeno 20 giorni di ferie l'anno; molti contratti ne danno 25-30."],
de="""Betreff: Urlaubsantrag [Vorname Nachname]

Hallo [Name],

hiermit beantrage ich Urlaub vom [Datum] bis einschließlich [Datum] ([Anzahl] Arbeitstage). Meine Vertretung übernimmt [Name], die Übergabe bereite ich vorher vor.

Ich freue mich über eine kurze Bestätigung.

Viele Grüße
[Vorname Nachname]""",
it="""Oggetto: richiesta di ferie
Ciao [nome],
chiedo le ferie dal [data] al [data] compreso ([numero] giorni lavorativi). Mi sostituisce [nome], preparo prima il passaggio di consegne.
Grazie per una breve conferma.
Saluti"""),

# ---------------- UFFICI ----------------
dict(cat="Uffici e burocrazia", titolo="Richiesta della Steuer-ID non arrivata",
quando="Ti sei registrato, ma dopo 4 settimane il codice fiscale tedesco non è arrivato.",
note=["La Steuer-ID arriva per posta 2-4 settimane dopo la prima registrazione. Il Bundeszentralamt für Steuern (BZSt) ha anche un modulo online per richiederla di nuovo: è la via più veloce.",
      "Controlla che il tuo nome sia sulla cassetta delle lettere."],
de="""Bundeszentralamt für Steuern
53221 Bonn

[Ort], [Datum]

Bitte um erneute Mitteilung meiner Steuerlichen Identifikationsnummer

Sehr geehrte Damen und Herren,

ich bin seit dem [Datum] unter der folgenden Adresse gemeldet: [Straße Hausnummer, PLZ Ort]. Meine Steuer-ID habe ich bisher nicht erhalten.

Bitte senden Sie mir meine Steuerliche Identifikationsnummer an die oben genannte Adresse.
Meine Daten: [Vorname Nachname], geboren am [Geburtsdatum] in [Geburtsort].

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Richiesta di nuovo invio del mio codice fiscale tedesco
Gentili signore e signori,
sono registrato dal [data] a questo indirizzo: [indirizzo]. Non ho ancora ricevuto il mio codice fiscale (Steuer-ID).
Vi prego di inviarmelo all'indirizzo indicato. I miei dati: [nome], nato il [data] a [luogo].
Cordiali saluti"""),

dict(cat="Uffici e burocrazia", titolo="Ricorso contro un avviso fiscale (Einspruch)",
quando="Il Finanzamt ti ha mandato un avviso (Steuerbescheid) che secondo te è sbagliato.",
note=["Hai 1 mese dalla notifica dell'avviso (§ 355 AO). Se lo mandi solo per non perdere la scadenza, puoi aggiungere i motivi dopo.",
      "Si può inviare anche tramite ELSTER, il portale online del fisco."],
de="""Finanzamt [Ort]
[Adresse]

[Ort], [Datum]

Einspruch gegen den Einkommensteuerbescheid [Jahr] vom [Datum]
Steuernummer: [Nummer]
Steuer-ID: [Nummer]

Sehr geehrte Damen und Herren,

gegen den oben genannten Bescheid lege ich hiermit Einspruch ein.

Begründung: [z. B. "Die Werbungskosten für mein Arbeitszimmer wurden nicht berücksichtigt."] / Die Begründung reiche ich bis zum [Datum] nach.

Ich beantrage außerdem die Aussetzung der Vollziehung des streitigen Betrags.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Ricorso contro l'avviso di imposta sul reddito [anno] del [data] – numero fiscale [numero], Steuer-ID [numero]
Gentili signore e signori,
con la presente presento ricorso contro l'avviso indicato.
Motivo: [motivo] / I motivi li invierò entro il [data].
Chiedo inoltre la sospensione del pagamento dell'importo contestato.
Cordiali saluti"""),

dict(cat="Uffici e burocrazia", titolo="Richiesta di proroga per la dichiarazione dei redditi",
quando="Non riesci a consegnare la dichiarazione in tempo.",
note=["Se la fai da solo e sei obbligato a farla, la scadenza di solito è il 31 luglio dell'anno dopo. Una proroga va chiesta prima della scadenza, con un motivo."],
de="""Antrag auf Fristverlängerung für die Einkommensteuererklärung [Jahr]
Steuernummer: [Nummer]

Sehr geehrte Damen und Herren,

hiermit beantrage ich eine Verlängerung der Frist zur Abgabe meiner Einkommensteuererklärung für [Jahr] bis zum [Datum].

Begründung: [z. B. "Mir fehlen noch Unterlagen meines früheren Arbeitgebers aus Italien."]

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Richiesta di proroga per la dichiarazione dei redditi [anno] – numero fiscale [numero]
Gentili signore e signori,
chiedo una proroga del termine per la consegna della mia dichiarazione dei redditi [anno] fino al [data].
Motivo: [motivo].
Cordiali saluti"""),

dict(cat="Uffici e burocrazia", titolo="Richiesta del certificato di iscrizione alla cassa malattia",
quando="Il datore di lavoro, l'università o un ufficio ti chiede la prova che sei assicurato.",
note=["Molte casse malattia la mandano anche dall'app o dall'area clienti online in pochi minuti."],
de="""Betreff: Bitte um Mitgliedsbescheinigung
Versichertennummer: [Nummer]

Sehr geehrte Damen und Herren,

für [meinen Arbeitgeber / die Hochschule / das Amt] benötige ich eine Mitgliedsbescheinigung. Bitte senden Sie mir diese per E-Mail an [E-Mail] oder per Post an meine Adresse.

Vielen Dank und freundliche Grüße
[Vorname Nachname], geboren am [Geburtsdatum]""",
it="""Oggetto: richiesta di certificato di iscrizione – numero assicurato [numero]
Gentili signore e signori,
per [il mio datore di lavoro / l'università / l'ufficio] mi serve un certificato di iscrizione. Vi prego di inviarmelo per email a [email] o per posta al mio indirizzo.
Grazie e cordiali saluti"""),

dict(cat="Uffici e burocrazia", titolo="Cancellazione dal canone radiotelevisivo (Rundfunkbeitrag)",
quando="Lasci la Germania, o vai a vivere con qualcuno che paga già il canone per l'appartamento.",
note=["Il canone si paga per appartamento, non per persona: se un coinquilino paga già, tu non devi pagare.",
      "Il modo più semplice è il modulo online su rundfunkbeitrag.de. La lettera serve se preferisci la posta."],
de="""ARD ZDF Deutschlandradio Beitragsservice
50656 Köln

[Ort], [Datum]

Abmeldung vom Rundfunkbeitrag
Beitragsnummer: [Nummer]

Sehr geehrte Damen und Herren,

hiermit melde ich meine Wohnung [Adresse] zum [Datum] vom Rundfunkbeitrag ab.

Grund: [Auszug ins Ausland – neue Adresse: ... / Zusammenzug mit einer Person, die bereits zahlt – deren Beitragsnummer: ...]

Bitte bestätigen Sie mir die Abmeldung schriftlich und erstatten Sie zu viel gezahlte Beiträge auf folgendes Konto: IBAN [IBAN].

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Cancellazione dal canone radiotelevisivo – numero contribuente [numero]
Gentili signore e signori,
con la presente cancello il mio appartamento [indirizzo] dal canone a partire dal [data].
Motivo: [trasferimento all'estero / convivenza con una persona che paga già].
Vi prego di confermarmi la cancellazione per iscritto e di rimborsare quanto pagato in più sul conto [IBAN].
Cordiali saluti"""),

dict(cat="Uffici e burocrazia", titolo="Richiesta di un posto all'asilo nido (Kita)",
quando="Cerchi un posto in una Kita per tuo figlio.",
note=["I posti sono pochi: scrivi a molte Kita insieme e iscriviti anche alla piattaforma online del tuo comune (a Monaco: kita finder+).",
      "Dal primo anno di età c'è il diritto legale a un posto (§ 24 SGB VIII)."],
de="""Betreff: Anfrage Betreuungsplatz ab [Monat/Jahr] – [Name des Kindes]

Sehr geehrte Damen und Herren,

wir suchen ab [Monat/Jahr] einen Betreuungsplatz für unser Kind [Vorname], geboren am [Datum]. Wir wohnen in [Stadtteil] und interessieren uns sehr für Ihre Einrichtung.

Benötigt wird eine Betreuung von [Uhrzeit] bis [Uhrzeit] an [Anzahl] Tagen pro Woche. Unsere Familie spricht Italienisch; [Vorname] lernt gerade Deutsch.

Gibt es die Möglichkeit, Ihre Kita kennenzulernen oder uns auf die Warteliste setzen zu lassen?

Mit freundlichen Grüßen
[Vorname Nachname], [Telefon]""",
it="""Oggetto: richiesta di posto dal [mese/anno] – [nome del bambino]
Gentili signore e signori,
cerchiamo dal [mese/anno] un posto per nostro figlio/a [nome], nato/a il [data]. Abitiamo a [quartiere] e siamo molto interessati alla vostra struttura.
Ci serve un orario dalle [ora] alle [ora] per [numero] giorni a settimana. In famiglia parliamo italiano; [nome] sta imparando il tedesco.
È possibile visitare la vostra Kita o essere inseriti in lista d'attesa?
Cordiali saluti"""),

dict(cat="Uffici e burocrazia", titolo="Richiesta di appuntamento dal medico",
quando="Vuoi prenotare una visita per email.",
note=["Molti studi usano anche portali di prenotazione online. Se hai urgenza fuori orario chiama il 116 117 (guardia medica)."],
de="""Betreff: Terminanfrage – [Vorname Nachname]

Sehr geehrte Damen und Herren,

ich möchte gerne einen Termin vereinbaren. Grund: [z. B. Vorsorgeuntersuchung / seit [Zeitraum] Rückenschmerzen].

Ich bin [gesetzlich/privat] versichert bei [Krankenkasse]. Am besten passen mir [Wochentage/Uhrzeiten].

Vielen Dank und freundliche Grüße
[Vorname Nachname], geboren am [Geburtsdatum], [Telefon]""",
it="""Oggetto: richiesta di appuntamento
Gentili signore e signori,
vorrei fissare un appuntamento. Motivo: [motivo].
Sono assicurato [pubblicamente/privatamente] con [cassa malattia]. I giorni/orari migliori per me sono [giorni/orari].
Grazie e cordiali saluti"""),

# ---------------- RICERCA CASA (aggiunte) ----------------
dict(cat="Casa e affitto", titolo="Candidatura per un appartamento",
quando="Rispondi a un annuncio di appartamento (ImmoScout24, Kleinanzeigen, WG-Gesucht).",
note=["A Monaco e nelle grandi città un annuncio riceve centinaia di messaggi: scrivi subito, in modo breve e completo.",
      "Tieni pronti in un unico PDF: documento, ultime 3 buste paga, contratto di lavoro, Schufa-Auskunft e Mietschuldenfreiheitsbescheinigung.",
      "Attenzione alle truffe: non pagare mai cauzione o affitto prima di aver visto l'appartamento e firmato il contratto."],
de="""Betreff: Anfrage zur Wohnung [Straße/Stadtteil], [Zimmer] Zimmer, ab [Datum]

Sehr geehrte/r [Frau/Herr Nachname],

mit großem Interesse habe ich Ihre Anzeige für die Wohnung in [Stadtteil] gelesen.

Kurz zu mir: Ich heiße [Vorname Nachname], bin [Alter] Jahre alt und arbeite unbefristet als [Beruf] bei [Arbeitgeber] mit einem monatlichen Nettoeinkommen von [Betrag] Euro. Ich bin Nichtraucher, habe keine Haustiere und suche eine Wohnung für [mich allein / mich und meine Partnerin].

Alle Unterlagen (Ausweis, Gehaltsnachweise, Arbeitsvertrag, SCHUFA-Auskunft, Mietschuldenfreiheitsbescheinigung) kann ich Ihnen sofort zusenden.

Über eine Einladung zur Besichtigung würde ich mich sehr freuen. Sie erreichen mich unter [Telefon] oder per E-Mail.

Mit freundlichen Grüßen
[Vorname Nachname]""",
it="""Oggetto: richiesta per l'appartamento in [via/quartiere], [numero] locali, dal [data]
Gentile [Signora/Signor Cognome],
ho letto con grande interesse il Suo annuncio per l'appartamento a [quartiere].
Brevemente su di me: mi chiamo [nome], ho [età] anni e lavoro a tempo indeterminato come [professione] presso [datore di lavoro], con un reddito netto mensile di [importo] euro. Non fumo, non ho animali e cerco un appartamento per [me solo / me e la mia compagna].
Posso inviarLe subito tutti i documenti (documento d'identità, buste paga, contratto di lavoro, rapporto SCHUFA, attestato di assenza di arretrati d'affitto).
Sarei molto felice di essere invitato a una visita. Può contattarmi al [telefono] o per email.
Cordiali saluti"""),

dict(cat="Casa e affitto", titolo="Richiesta dell'attestato di nessun arretrato d'affitto (Mietschuldenfreiheitsbescheinigung)",
quando="Cerchi casa e il nuovo padrone di casa chiede la prova che hai sempre pagato l'affitto.",
note=["Il padrone di casa attuale non è sempre obbligato a dartela, ma quasi tutti la rilasciano. In alternativa, estratti conto con i pagamenti dell'affitto."],
de="""Betreff: Bitte um eine Mietschuldenfreiheitsbescheinigung

Sehr geehrte/r [Frau/Herr Nachname],

ich wohne seit dem [Datum] in Ihrer Wohnung [Straße Hausnummer]. Für die Suche nach einer neuen Wohnung benötige ich eine Bescheinigung, dass keine Mietrückstände bestehen.

Könnten Sie mir diese bitte bis zum [Datum] ausstellen? Ein unterschriebener Scan per E-Mail genügt.

Vielen Dank und freundliche Grüße
[Vorname Nachname]""",
it="""Oggetto: richiesta di attestato di assenza di arretrati d'affitto
Gentile [Signora/Signor Cognome],
abito dal [data] nel Suo appartamento [indirizzo]. Per la ricerca di un nuovo appartamento mi serve un attestato che non ci sono affitti arretrati.
Potrebbe rilasciarmelo entro il [data]? Basta una scansione firmata per email.
Grazie e cordiali saluti"""),

dict(cat="Lavoro", titolo="Richiesta della certificazione dei redditi (Lohnsteuerbescheinigung)",
quando="Ti serve per la dichiarazione dei redditi o per l'Italia e non la trovi.",
note=["Il datore di lavoro la trasmette al fisco entro fine febbraio dell'anno dopo e di solito te ne dà una copia con l'ultima busta paga dell'anno o con quella di gennaio."],
de="""Betreff: Bitte um Kopie meiner Lohnsteuerbescheinigung [Jahr]

Hallo [Name],

für meine Steuererklärung benötige ich eine Kopie meiner Lohnsteuerbescheinigung für das Jahr [Jahr]. Könntest du / Könnten Sie mir diese bitte per E-Mail oder über das Mitarbeiterportal zukommen lassen?

Vielen Dank und viele Grüße
[Vorname Nachname], Personalnummer [Nummer]""",
it="""Oggetto: richiesta di copia della certificazione dei redditi [anno]
Ciao [nome],
per la dichiarazione dei redditi mi serve una copia della mia certificazione fiscale per l'anno [anno]. Potresti/Potrebbe inviarmela per email o tramite il portale dei dipendenti?
Grazie e saluti"""),
]
