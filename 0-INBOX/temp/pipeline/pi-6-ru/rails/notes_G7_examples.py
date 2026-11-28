"""Print Pāli = Russian example lines from build_rails_G7_ru (for notes-rails-G7.md). Writes nothing."""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
import build_rails_G7_ru as G  # noqa: E402

EX = [
    (False, "Kattha kāmarāgānusayo anuseti? Kāmadhātuyā dvīsu vedanāsu ettha kāmarāgānusayo anuseti."),
    (False, "Sabbasakkāyapariyāpannesu dhammesu ettha diṭṭhānusayo anuseti."),
    (False, "(Ka) yassa kāmarāgānusayo anuseti tassa paṭighānusayo anusetīti? Āmantā."),
    (False, "(Kha) yassa vā pana paṭighānusayo anuseti tassa kāmarāgānusayo anusetīti? No."),
    (False, "(Ka) yattha kāmarāgānusayo ca paṭighānusayo ca anusenti tattha mānānusayo anusetīti? Natthi."),
    (False, "(Kha) yassa vā pana yattha mānānusayo anuseti tassa tattha kāmarāgānusayo anusetīti?"),
    (False, "Yassa paṭighānusayo anuseti tassa diṭṭhānusayo…pe… vicikicchānusayo anusetīti?"),
    (False, "Anāgāmissa mānānusayo anuseti, no ca tassa kāmarāgānusayo anuseti. Tiṇṇaṃ puggalānaṃ mānānusayo ca anuseti kāmarāgānusayo ca anuseti."),
    (False, "Anāgāmissa avijjānusayo ca mānānusayo ca anusenti, no ca tassa kāmarāgānusayo ca paṭighānusayo ca anusenti."),
    (False, "Anāgāmissa kāmarāgānusayo nānuseti, no ca tassa mānānusayo nānuseti. Arahato kāmarāgānusayo ca nānuseti mānānusayo ca nānuseti."),
    (False, "Dvinnaṃ puggalānaṃ vicikicchānusayo nānuseti, no ca tesaṃ kāmarāgānusayo ca paṭighānusayo ca nānusenti."),
    (False, "Rūpadhātuyā arūpadhātuyā ettha mānānusayo anuseti, no ca tattha kāmarāgānusayo anuseti. Kāmadhātuyā dvīsu vedanāsu ettha mānānusayo ca anuseti kāmarāgānusayo ca anuseti."),
    (False, "Anāgāmissa kāmadhātuyā dvīsu vedanāsu rūpadhātuyā arūpadhātuyā tassa tattha mānānusayo anuseti, no ca tassa tattha kāmarāgānusayo anuseti. Tesaññeva puggalānaṃ kāmadhātuyā dvīsu vedanāsu tesaṃ tattha mānānusayo ca anuseti kāmarāgānusayo ca anuseti."),
    (False, "Arahato sabbattha kāmarāgānusayo ca nānuseti paṭighānusayo ca nānuseti."),
    (False, "Tesaññeva puggalānaṃ rūpadhātuyā arūpadhātuyā apariyāpanne tesaṃ tattha vicikicchānusayo ca nānuseti kāmarāgānusayo ca paṭighānusayo ca nānusenti."),
    (False, "(Ka) yo kāmarāgānusayena sānusayo so paṭighānusayena sānusayoti? Āmantā."),
    (False, "Anāgāmī mānānusayena sānusayo, no ca kāmarāgānusayena sānusayo. Tayo puggalā mānānusayena ca sānusayā kāmarāgānusayena ca sānusayā."),
    (True, "(Ka) yato kāmarāgānusayena sānusayo tato paṭighānusayena sānusayoti? No."),
    (True, "Rūpadhātuyā arūpadhātuyā tato mānānusayena sānusayo, no ca tato kāmarāgānusayena sānusayo."),
    (False, "(Ka) yo yato kāmarāgānusayena sānusayo so tato mānānusayena sānusayoti? Āmantā."),
    (False, "Anāgāmī kāmadhātuyā dvīsu vedanāsu rūpadhātuyā arūpadhātuyā so tato mānānusayena sānusayo, no ca so tato kāmarāgānusayena sānusayo."),
    (False, "Arahā sabbattha kāmarāgānusayena ca niranusayo paṭighānusayena ca niranusayo."),
    (False, "(Ka) yo kāmarāgānusayaṃ pajahati so mānānusayaṃ pajahatīti? Tadekaṭṭhaṃ pajahati."),
    (False, "Aṭṭhamako dukkhāya vedanāya rūpadhātuyā arūpadhātuyā so tato vicikicchānusayaṃ pajahati, no ca so tato kāmarāgānusayaṃ pajahati. Sveva puggalo kāmadhātuyā dvīsu vedanāsu so tato vicikicchānusayaṃ pajahati kāmarāgānusayaṃ tadekaṭṭhaṃ pajahati."),
    (True, "Kāmadhātuyā dvīsu vedanāsu tato mānānusayañca pajahati kāmarāgānusayañca pajahati."),
    (False, "Aggamaggasamaṅgī kāmarāgānusayaṃ nappajahati, no ca so mānānusayaṃ nappajahati. Dvinnaṃ maggasamaṅgīnaṃ ṭhapetvā avasesā puggalā kāmarāgānusayañca nappajahanti mānānusayañca nappajahanti."),
    (False, "Aggamaggasamaṅgiñca aṭṭhamakañca ṭhapetvā avasesā puggalā sabbattha kāmarāgānusayañca nappajahanti vicikicchānusayañca nappajahanti."),
    (False, "(Ka) yo kāmarāgānusayaṃ parijānāti so paṭighānusayaṃ parijānātīti? Āmantā."),
    (False, "Anāgāmimaggasamaṅgī kāmarāgānusayaṃ na parijānāti, no ca so mānānusayaṃ na parijānāti."),
    (False, "(Ka) yassa kāmarāgānusayo pahīno tassa paṭighānusayo pahīnoti? Āmantā."),
    (False, "Anāgāmissa kāmarāgānusayo pahīno, no ca tassa mānānusayo pahīno. Arahato kāmarāgānusayo ca pahīno mānānusayo ca pahīno."),
    (False, 'Rūpadhātuyā arūpadhātuyā ettha mānānusayo pahīno; kāmarāgānusayo na vattabbo "pahīno"ti vā "appahīno"ti vā.'),
    (False, 'Na vattabbo "pahīno"ti vā "appahīno"ti vā.'),
    (False, "Anāgāmissa mānānusayo uppajjati, no ca tassa kāmarāgānusayo uppajjati. Tiṇṇaṃ puggalānaṃ mānānusayo ca uppajjati kāmarāgānusayo ca uppajjati (vitthāretabbaṃ)."),
    (False, "Kāmadhātuyā cutassa kāmadhātuṃ upapajjantassa kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā?"),
    (False, "Na kāmadhātuyā na rūpadhātuyā cutassa na kāmadhātuṃ na arūpadhātuṃ upapajjantassa kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā?"),
    (False, "Kāmadhātuyā cutassa rūpadhātuṃ upapajjantassa kassaci satta anusayā anusenti, kassaci pañca anusayā anusenti, kassaci tayo anusayā anusenti; anusayā bhaṅgā natthi."),
    (False, "Rūpadhātuyā cutassa kāmadhātuṃ upapajjantassa satteva anusayā anusenti; anusayā bhaṅgā natthi."),
    (False, "Arūpadhātuyā cutassa rūpadhātuyā upapatti nāma natthi, heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati, satteva anusayā anusenti; anusayā bhaṅgā natthi."),
]
for okasa, p in EX:
    G._CUR["okasa"] = okasa
    G._CUR["ref_pl"] = False
    G._CUR["obj_pl"] = False
    print(f"{p} = {G.translate_line(p)}")
for h in ["### Anusayayamakaṃ", "#### Uppattiṭṭhānavāro", "#### Mahāvāro 1. anusayavāro", "##### (Ka) anulomapuggalo",
          "##### (Ṅa) paṭilomaokāso", "#### Sānusayavāro", "#### Pajahanavāro", "#### Pariññāvāro", "#### Pahīnavāro",
          "##### Uppajjanavāro", "##### (Ka) dhātupucchāvāro", "##### (Kha) dhātuvisajjanāvāro"]:
    print(f"{h} = {G.heading(h)}")
for f in ["Uppattiṭṭhānavāro.", "Anusayavāre anulomaṃ.", "Pahīnavāre paṭilomaṃ.", "Dhātupucchāvāro.",
          "Dhātuvisajjavāro.", "Anusayayamakaṃ niṭṭhitaṃ.", "(Ekamūlakaṃ)", "(Chakkamūlakaṃ)", "(Kāmadhātumūlakaṃ)",
          "(Nakāmanarūpadhātumūlakaṃ)", "(Vitthāretabbaṃ)."]:
    print(f"{f} = {G.fixed(f)}")
