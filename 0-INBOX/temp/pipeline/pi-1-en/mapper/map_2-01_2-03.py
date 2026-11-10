"""English->Pali keyword map for pi-1 chapters 2-01-cittuppadakandam and 2-03-cittuppadakandam.

usage: python -I -X utf8 map_2-01_2-03.py
Writes <ch>.mapped.md next to <ch>.keywords.md. Conventions: map-conventions.md (incl. section 8).

Method: the Pali of each segment is tokenised and scanned with a fixed phrase table (longest match);
each table entry lists, in order, the English keywords its words produce (from the builder phrase tables
build_ch2_01_sample.py, build_2-01_2-02.py, const_2_03_2_04.py, build_2-03.py and the harmonise pass) and
the Pali value for each. Per segment and keyword: multiword keywords take the first occurrence; single
words take the first value per lemma, and different lemmas are joined with " / " (map-conventions 4).
Identical formulaic segments therefore get identical mappings by construction.
Spec syntax in E(): "kw=value@lemma; kw=value; ..." (lemma defaults to the value); NDE = no direct equivalent.
"""
import pathlib, re, sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
NDE = "(no direct equivalent)"
CHAPTERS = ["2-01-cittuppadakandam", "2-03-cittuppadakandam"]

T = {}


def E(pali, spec, lead=None):
    toks = tuple(pali.split())
    contribs = []
    for part in spec.split(";"):
        part = part.strip()
        if not part:
            continue
        kw, val = part.split("=", 1)
        lemma = None
        if "@" in val:
            val, lemma = val.split("@", 1)
        val = NDE if val.strip() == "NDE" else val.strip()
        lem = (lemma or val).strip()
        contribs.append((kw.strip().lower(), val, lem[0].lower() + lem[1:]))
    assert toks not in T, toks
    T[toks] = (contribs, lead)


# ============================================================ frames
E("katame dhammā kusalā", "wholesome=kusalā@kusala; states=dhammā@dhamma; wholesome states=dhammā kusalā")
E("ime dhammā kusalā", "wholesome=kusalā@kusala; states=dhammā@dhamma; wholesome states=dhammā kusalā")
for y in ("yo", "yā", "yaṃ"):
    E(f"{y} tasmiṃ samaye", f"whatever={y}@ya", lead="FRAME")
E("ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā",
  "whatever=ye@ya; dependently=paṭicca; dependently arisen=paṭiccasamuppannā; arisen=samuppannā@uppanna; "
  "immaterial=arūpino@arūpa; immaterial states=arūpino dhammā; arisen immaterial=samuppannā arūpino; "
  "arisen immaterial states=samuppannā arūpino dhammā; dependently arisen immaterial=paṭiccasamuppannā arūpino; "
  "states=dhammā@dhamma")
E("yo tesaṃ arūpīnaṃ dhammānaṃ", "whatever=yo@ya; immaterial=arūpīnaṃ@arūpa; immaterial states=arūpīnaṃ dhammānaṃ; "
  "states=dhammānaṃ@dhamma")
E("yā tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya",
  "whatever=yā@ya; states=dhammānaṃ@dhamma; known=aññātānaṃ@aññāta; seen=diṭṭhānaṃ; reached=pattānaṃ; "
  "discovered=viditānaṃ; realized=sacchikatānaṃ; realization=sacchikiriyāya")
E("yā tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya",
  "whatever=yā@ya; states=dhammānaṃ@dhamma; known=ñātānaṃ@aññāta; seen=diṭṭhānaṃ; reached=pattānaṃ; "
  "discovered=viditānaṃ; realized=sacchikatānaṃ; realization=sacchikiriyāya")
E("ṭhapetvā", "except=ṭhapetvā")
E("dhammā", "states=dhammā@dhamma")

# ============================================================ opening sentence, 2-01
E("kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti",
  "sense=kāma@kāma; sphere=avacaraṃ@avacara; sense sphere=kāmāvacaraṃ; wholesome=kusalaṃ@kusala; "
  "wholesome mind=kusalaṃ cittaṃ; mind=cittaṃ@citta; sphere has arisen=avacaraṃ kusalaṃ cittaṃ uppannaṃ hoti; "
  "arisen=uppannaṃ@uppanna")
E("somanassasahagataṃ", "accompanied=sahagataṃ; accompanied by joy=somanassasahagataṃ; joy=somanassa@somanassa")
E("upekkhāsahagataṃ", "accompanied=sahagataṃ; accompanied by equanimity=upekkhāsahagataṃ; equanimity=upekkhā@upekkhā")
E("ñāṇasampayuttaṃ", "associated=sampayuttaṃ; knowledge=ñāṇa@ñāṇa; associated with knowledge=ñāṇasampayuttaṃ")
E("ñāṇavippayuttaṃ", "dissociated=vippayuttaṃ; knowledge=ñāṇa@ñāṇa; dissociated from knowledge=ñāṇavippayuttaṃ")
E("sasaṅkhārena", "prompting=saṅkhārena")
for tok, kws in (("rūpa", "visible form=rūpa; visible=rūpa; form=rūpa"), ("sadda", "sound=sadda"),
                 ("gandha", "smell=gandha"), ("rasa", "taste=rasa"), ("phoṭṭhabba", "touch=phoṭṭhabba"),
                 ("dhamma", "mental object=dhamma; mental=dhamma@dhamma")):
    E(f"{tok[:-1]}ārammaṇaṃ vā", kws + "; object=ārammaṇaṃ@ārabh")
E("yaṃ yaṃ vā panārabbha", "whatever=yaṃ yaṃ@ya; takes=ārabbha; object=ārabbha@ārabh")

# ============================================================ names of the factors
E("phasso", "contact=phasso@phassa", lead=("contact", 1))
E("phassaṃ", "contact=phassaṃ@phassa")
E("vedanā", "feeling=vedanā@vedanā")
E("saññā", "perception=saññā@saññā", lead=("perception", 1))
E("cetanā", "intention=cetanā@cetanā", lead=("intention", 1))
E("cittaṃ", "mind=cittaṃ@citta", lead=("mind", 1))
E("vitakko", "applied=vitakko@vitakka; applied thought=vitakko; thought=vitakko@vitakka")
E("vicāro", "sustained=vicāro@vicāra; sustained thought=vicāro; thought=vicāro@vicāra")
E("pīti", "rapture=pīti@pīti", lead=("rapture", 1))
E("sukhaṃ", "happiness=sukhaṃ@sukha")
E("upekkhā", "equanimity=upekkhā@upekkhā")
E("cittassekaggatā", "one-pointedness=ekaggatā; one-pointedness of mind=cittassekaggatā; mind=cittassa@citta")
for tok, kw, stem, lem in (("saddhindriyaṃ", "faith", "saddhā", "saddhā"), ("vīriyindriyaṃ", "energy", "vīriya", "vīriya"),
                           ("satindriyaṃ", "mindfulness", "sati", "sati"),
                           ("samādhindriyaṃ", "concentration", "samādhi", "samādhi"),
                           ("paññindriyaṃ", "wisdom", "paññā", "paññā"), ("manindriyaṃ", "mind", "mana", "manas"),
                           ("somanassindriyaṃ", "joy", "somanassa", "somanassa"),
                           ("upekkhindriyaṃ", "equanimity", "upekkhā", "upekkhā"),
                           ("jīvitindriyaṃ", "life", "jīvita", "jīvita")):
    E(tok, f"faculty=indriyaṃ@indriya; faculty of {kw}={tok}; {kw}={stem}@{lem}")
E("anaññātaññassāmītindriyaṃ", "faculty=indriyaṃ@indriya; faculty of coming=anaññātaññassāmītindriyaṃ; "
  "coming=ñassāmi@ñassāmi; coming to know=ñassāmi; know=ñassāmi@ñassāmi; known=aññāta@aññāta")
E("aññindriyaṃ", "faculty=indriyaṃ@indriya; faculty of final=aññindriyaṃ; final=aññā@aññā; "
  "final knowledge=aññā; knowledge=aññā@aññā")
for tok, kw, stem, lem in (("sammādiṭṭhi", "view", "diṭṭhi", "diṭṭhi"), ("sammāsaṅkappo", "thought", "saṅkappo", "saṅkappa"),
                           ("sammāvācā", "speech", "vācā", "vācā"), ("sammākammanto", "action", "kammanto", "kammanta"),
                           ("sammāājīvo", "livelihood", "ājīvo", "ājīva"),
                           ("sammāvāyāmo", "effort", "vāyāmo", "vāyāma"), ("sammāsati", "mindfulness", "sati", "sati"),
                           ("sammāsamādhi", "concentration", "samādhi", "samādhi")):
    E(tok, f"right=sammā@sammā; right {kw}={tok}; {kw}={stem}@{lem}")
for tok, kw, stem, lem in (("saddhābalaṃ", "faith", "saddhā", "saddhā"), ("vīriyabalaṃ", "energy", "vīriya", "vīriya"),
                           ("satibalaṃ", "mindfulness", "sati", "sati"), ("samādhibalaṃ", "concentration", "samādhi", "samādhi"),
                           ("paññābalaṃ", "wisdom", "paññā", "paññā")):
    E(tok, f"power=balaṃ@bala; power of {kw}={tok}; {kw}={stem}@{lem}")
E("hiribalaṃ", "power=balaṃ@bala; power of moral=hiribalaṃ; power of moral shame=hiribalaṃ; moral=hiri@hirī; "
  "shame=hiri@hirī; moral shame=hiri")
E("ottappabalaṃ", "power=balaṃ@bala; power of fear=ottappabalaṃ; power of fear of wrongdoing=ottappabalaṃ; "
  "fear=ottappa@ottappa; wrongdoing=ottappa@ottappa; fear of wrongdoing=ottappa")
E("alobho", "non-greed=alobho", lead=("non-greed", 1))
E("adoso", "non-hate=adoso", lead=("non-hate", 1))
E("amoho", "non-delusion=amoho")
E("anabhijjhā", "non-covetousness=anabhijjhā")
E("abyāpādo", "non-ill-will=abyāpādo")
E("hirī", "moral=hirī@hirī; shame=hirī@hirī; moral shame=hirī")
E("ottappaṃ", "fear=ottappaṃ@ottappa; wrongdoing=ottappaṃ@ottappa; fear of wrongdoing=ottappaṃ")
for noun, kw, lem, kaya, citta in (("passaddhi", "tranquillity", "passaddhi", "kāya", "citta"),
                                   ("lahutā", "lightness", "lahutā", "kāya", "citta"),
                                   ("mudutā", "pliancy", "mudutā", "kāya", "citta"),
                                   ("kammaññatā", "workability", "kammañña", "kāya", "citta"),
                                   ("pāguññatā", "proficiency", "pāguñña", "kāya", "citta")):
    E(f"kāya{noun}", f"{kw}={noun}@{lem}; {kw} of the mental body=kāya{noun}; mental body=kāya; mental=kāya@kāya; "
      f"body=kāya@kāya")
    E(f"citta{noun}", f"{kw}={noun}@{lem}; {kw} of mind=citta{noun}; mind=citta@citta")
E("kāyujukatā", "uprightness=ujukatā@ujukatā; uprightness of the mental body=kāyujukatā; mental body=kāya; "
  "mental=kāya@kāya; body=kāya@kāya")
E("cittujukatā", "uprightness=ujukatā@ujukatā; uprightness of mind=cittujukatā; mind=citta@citta")
E("sati", "mindfulness=sati@sati", lead=("mindfulness", 1))
E("sampajaññaṃ", "clear=sampajaññaṃ; awareness=sampajaññaṃ; clear awareness=sampajaññaṃ")
E("samatho", "calm=samatho@samatha")
E("vipassanā", "insight=vipassanā")
E("paggāho", "exertion=paggāho")
E("avikkhepo", "non-distraction=avikkhepo")
# aggregates, bases, elements, nutriments
for pre, kws in (("vedanā", "aggregate of feeling={t}; feeling=vedanā@vedanā"),
                 ("saññā", "aggregate of perception={t}; perception=saññā@saññā"),
                 ("saṅkhāra", "aggregate of mental formations={t}; aggregate of mental={t}; mental formations=saṅkhāra; "
                              "mental=saṅkhāra@saṅkhāra; formations=saṅkhāra"),
                 ("viññāṇa", "aggregate of consciousness={t}; consciousness=viññāṇa@viññāṇa")):
    for end in ("o", "assa", "aṃ"):
        t = f"{pre}kkhandh{end}"
        E(t, f"aggregate=khandh{end}@khandha; " + kws.format(t=t))
E("manāyatanaṃ", "mind base=manāyatanaṃ; mind=mana@manas; base=āyatanaṃ@āyatana")
E("dhammāyatanaṃ", "mental-object base=dhammāyatanaṃ; mental-object=dhamma; base=āyatanaṃ@āyatana")
E("manoviññāṇadhātu", "mind-consciousness element=manoviññāṇadhātu; mind-consciousness=manoviññāṇa; element=dhātu@dhātu")
E("dhammadhātu", "mental-object element=dhammadhātu; mental-object=dhamma; element=dhātu@dhātu")
E("phassāhāro", "nutriment=āhāro@āhāra; nutriment of contact=phassāhāro; contact=phassa@phassa")
E("manosañcetanāhāro", "nutriment=āhāro@āhāra; nutriment of mental intention=manosañcetanāhāro; "
  "mental intention=manosañcetanā; mental=mano@manas; intention=sañcetanā@cetanā")
E("viññāṇāhāro", "nutriment=āhāro@āhāra; nutriment of consciousness=viññāṇāhāro; consciousness=viññāṇa@viññāṇa")
# counted / bare groups (Koṭṭhāsavāra, Suññatavāra)
E("khandhā", "aggregates=khandhā")
for t in ("dvāyatanāni", "āyatanāni"):
    E(t, "sense=āyatanāni@āyatana; bases=āyatanāni; sense bases=āyatanāni")
E("dhātuyo", "elements=dhātuyo")
E("āhārā", "nutriments=āhārā")
for t in ("aṭṭhindriyāni", "sattindriyāni", "navindriyāni", "indriyāni"):
    E(t, "faculties=indriyāni")
E("pañcaṅgikaṃ", "five-factored=pañcaṅgikaṃ@pañcaṅgika")
E("caturaṅgikaṃ", "four-factored=caturaṅgikaṃ@caturaṅgika")
E("jhānaṃ", "absorption=jhānaṃ@jhāna")
E("pañcaṅgiko maggo", "five-factored=pañcaṅgiko@pañcaṅgika; five-factored path=pañcaṅgiko maggo; path=maggo@magga")
E("caturaṅgiko maggo", "four-factored=caturaṅgiko@caturaṅgika; four-factored path=caturaṅgiko maggo; path=maggo@magga")
E("aṭṭhaṅgiko maggo", "eight-factored=aṭṭhaṅgiko; eight-factored path=aṭṭhaṅgiko maggo; path=maggo@magga")
E("maggo", "path=maggo@magga")
E("balāni", "powers=balāni")
E("hetū", "roots=hetū")

# ============================================================ synonym strings
# contact
E("phusanā", "touching=phusanā")
E("saṃphusanā", "coming=saṃphusanā; coming into contact=saṃphusanā; contact=saṃphusanā@phassa")
E("saṃphusitattaṃ", "having=NDE; contact=saṃphusitattaṃ@phassa")
# pleasant feeling
E("cetasikaṃ sātaṃ", "mental comfort=cetasikaṃ sātaṃ; mental=cetasikaṃ@cetasika; comfort=sātaṃ", lead=("mental", 1))
E("cetasikaṃ sukhaṃ", "mental happiness=cetasikaṃ sukhaṃ; mental=cetasikaṃ@cetasika; happiness=sukhaṃ@sukha")
E("cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ",
  "born=cetosamphassajaṃ@ja; born of mind-contact=cetosamphassajaṃ; mind-contact=cetosamphassajaṃ@cetosamphassaja; "
  "comfortable=sātaṃ@sāta; pleasant=sukhaṃ@sukha; pleasant experience=sukhaṃ vedayitaṃ; experience=vedayitaṃ; "
  "experience born=cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ; "
  "pleasant experience born=cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ")
E("cetosamphassajā sātā sukhā vedanā",
  "born=cetosamphassajā@ja; born of mind-contact=cetosamphassajā; mind-contact=cetosamphassajā@cetosamphassaja; "
  "comfortable=sātā@sāta; pleasant=sukhā@sukha; pleasant feeling=sukhā vedanā; feeling=vedanā@vedanā; "
  "feeling born=cetosamphassajā sātā sukhā vedanā; pleasant feeling born=cetosamphassajā sātā sukhā vedanā")
# neutral feeling
E("cetasikaṃ neva sātaṃ nāsātaṃ", "mental state=cetasikaṃ; mental=cetasikaṃ@cetasika; comfortable=sātaṃ@sāta; "
  "uncomfortable=asātaṃ")
E("cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ",
  "born=cetosamphassajaṃ@ja; born of mind-contact=cetosamphassajaṃ; mind-contact=cetosamphassajaṃ@cetosamphassaja; "
  "painful=adukkhamasukhaṃ@adukkhamasukha; pleasant=adukkhamasukhaṃ@adukkhamasukha; "
  "painful nor pleasant=adukkhamasukhaṃ; experience=vedayitaṃ; "
  "experience born=cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ")
E("cetosamphassajā adukkhamasukhā vedanā",
  "born=cetosamphassajā@ja; born of mind-contact=cetosamphassajā; mind-contact=cetosamphassajā@cetosamphassaja; "
  "painful=adukkhamasukhā@adukkhamasukha; pleasant=adukkhamasukhā@adukkhamasukha; "
  "painful nor pleasant=adukkhamasukhā; feeling=vedanā@vedanā; feeling born=cetosamphassajā adukkhamasukhā vedanā")
TAJ = ("corresponding=tajjā@tajja; mind-consciousness=manoviññāṇa; element=dhātu@dhātu; "
       "mind-consciousness element=manoviññāṇadhātu")
for e in ("aṃ", "ā"):
    E(f"tajjāmanoviññāṇadhātusamphassaj{e}", TAJ + f"; contact=samphassaj{e}@phassa; born=samphassaj{e}@ja")
E("tajjāmanoviññāṇadhātu", TAJ)
# perception, intention
E("sañjānanā", "perceiving=sañjānanā")
E("sañjānitattaṃ", "having=NDE; perceived=sañjānitattaṃ")
E("sañcetanā", "intending=sañcetanā")
E("cetayitattaṃ", "having=NDE; intended=cetayitattaṃ")
# mind
E("mano", "intellect=mano@manas")
E("mānasaṃ", "mental activity=mānasaṃ; mental=mānasaṃ@mānasa; activity=mānasaṃ")
E("hadayaṃ", "heart=hadayaṃ")
E("paṇḍaraṃ", "radiance=paṇḍaraṃ")
E("viññāṇaṃ", "consciousness=viññāṇaṃ@viññāṇa")
# applied / sustained thought
E("takko", "thinking=takko", lead=("thinking", 1))
E("saṅkappo", "thought=saṅkappo@saṅkappa")
E("appanā", "fixing=appanā@appanā")
E("byappanā", "fixing=byappanā@appanā; firm fixing=byappanā")
E("cetaso abhiniropanā", "directing=abhiniropanā; mind=cetaso@ceto; directing of the mind=cetaso abhiniropanā")
E("cāro", "exploring=cāro@cāra", lead=("exploring", 1))
E("anuvicāro", "continued=anuvicāro; exploring=anuvicāro@cāra; continued exploring=anuvicāro")
E("upavicāro", "close=upavicāro; exploring=upavicāro@cāra; close exploring=upavicāro")
E("cittassa", "mind=cittassa@citta")
E("anusandhānatā", "staying=anusandhānatā; connected=anusandhānatā; staying connected=anusandhānatā")
E("anupekkhanatā", "continued=anupekkhanatā; observing=anupekkhanatā; continued observing=anupekkhanatā")
# rapture
for t, kw in (("pāmojjaṃ", "gladness"), ("āmodanā", "delight"), ("pamodanā", "rejoicing"), ("hāso", "mirth"),
              ("pahāso", "merriment"), ("vitti", "satisfaction"), ("odagyaṃ", "elation")):
    E(t, f"{kw}={t}")
E("attamanatā cittassa", "contentment=attamanatā; contentment of mind=attamanatā cittassa; mind=cittassa@citta")
# concentration
E("cittassa ṭhiti", "stability=ṭhiti; stability of mind=cittassa ṭhiti; mind=cittassa@citta")
E("saṇṭhiti", "steadiness=saṇṭhiti")
E("avaṭṭhiti", "firmness=avaṭṭhiti")
E("avisāhāro", "non-scattering=avisāhāro")
E("avisāhaṭamānasatā", "unscattered=avisāhaṭa; unscattered mind=avisāhaṭamānasatā; mind=mānasatā@mānasa")
# faith
E("saddhā", "faith=saddhā@saddhā", lead=("faith", 1))
E("saddahanā", "trusting=saddahanā")
E("okappanā", "confiding=okappanā")
E("abhippasādo", "confidence=abhippasādo; full confidence=abhippasādo")
# energy
E("cetasiko vīriyārambho", "mental=cetasiko@cetasika; arousing=ārambho; mental arousing=cetasiko vīriyārambho; "
  "energy=vīriya@vīriya")
E("nikkamo", "setting=nikkamo; setting out=nikkamo")
E("parakkamo", "pressing=parakkamo@parakkama; forward=parakkamo@parakkama; pressing forward=parakkamo")
E("uyyāmo", "striving=uyyāmo")
E("vāyāmo", "effort=vāyāmo@vāyāma")
E("ussāho", "zeal=ussāho")
E("ussoḷhī", "ardour=ussoḷhī")
E("thāmo", "strength=thāmo")
E("dhiti", "steadfastness=dhiti")
E("asithilaparakkamatā", "unslackening=asithila; pressing=parakkamatā@parakkama; forward=parakkamatā@parakkama; "
  "pressing forward=parakkamatā; unslackening pressing forward=asithilaparakkamatā")
E("anikkhittachandatā", "putting=nikkhitta@nikkhitta; desire=chandatā@chanda")
E("anikkhittadhuratā", "putting=nikkhitta@nikkhitta; burden=dhuratā@dhura")
E("dhurasampaggāho", "burden=dhura@dhura; grasping=sampaggāho; firm grasping=sampaggāho")
E("vīriyaṃ", "energy=vīriyaṃ@vīriya")
# mindfulness
E("anussati", "recollection=anussati")
E("paṭissati", "recall=paṭissati")
E("saraṇatā", "remembering=saraṇatā")
E("dhāraṇatā", "keeping=dhāraṇatā; keeping in mind=dhāraṇatā; mind=dhāraṇatā@dhāraṇa")
E("apilāpanatā", "floating=pilāpanatā; away=pilāpanatā; floating away=pilāpanatā")
E("asammussanatā", "forgetting=sammussanatā")
# wisdom
E("paññā", "wisdom=paññā@paññā", lead=("wisdom", 1))
for t, kw in (("pajānanā", "understanding"), ("sallakkhaṇā", "discerning"), ("upalakkhaṇā", "distinguishing"),
              ("paccupalakkhaṇā", "differentiating"), ("paṇḍiccaṃ", "learning"), ("kosallaṃ", "skill"),
              ("nepuññaṃ", "subtlety"), ("vebhabyā", "clarity"), ("cintā", "consideration"),
              ("upaparikkhā", "examination"), ("bhūrī", "breadth"), ("medhā", "intelligence"),
              ("pariṇāyikā", "guidance"), ("patodo", "goad")):
    E(t, f"{kw}={t}")
E("vicayo", "investigation=vicayo@vicaya")
E("pavicayo", "investigation=pavicayo@vicaya; close investigation=pavicayo")
E("dhammavicayo", "investigation=vicayo@vicaya; investigation of states=dhammavicayo; states=dhamma@dhamma")
for t, kw in (("satthaṃ", "sword"), ("pāsādo", "tower"), ("āloko", "light"), ("obhāso", "radiance"),
              ("pajjoto", "lamp"), ("ratanaṃ", "jewel")):
    E(f"paññā{t}", f"{kw}={t}; {kw} of wisdom=paññā{t}; wisdom=paññā@paññā")
# life
E("āyu", "lifespan=āyu")
E("ṭhiti", "persistence=ṭhiti")
E("yapanā", "carrying=yapanā; carrying on=yapanā")
E("yāpanā", "keeping=yāpanā; going=yāpanā; keeping going=yāpanā")
E("iriyanā", "moving=iriyanā")
E("vattanā", "continuing=vattanā")
E("pālanā", "protection=pālanā")
E("jīvitaṃ", "life=jīvitaṃ@jīvita")
# shame, fear
_BAD = ("bad=pāpakānaṃ; unwholesome=akusalānaṃ; unwholesome states=akusalānaṃ dhammānaṃ; states=dhammānaṃ@dhamma; "
        "engaging=samāpattiyā")
E("hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā", "ashamed=hirīyati@hirī; " + _BAD)
E("ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā",
  "fearing=ottappati; fear=ottappitabbena@ottappa; " + _BAD)
# non-greed, non-hate
E("alubbhanā", "greedy=lubbhanā@lubbh; being greedy=lubbhanā")
E("alubbhitattaṃ", "greedy=lubbhitattaṃ@lubbh")
E("asārāgo", "non-lust=asārāgo")
E("asārajjanā", "lusting=sārajjanā@sārajj")
E("asārajjitattaṃ", "lusting=sārajjitattaṃ@sārajj")
E("kusalamūlaṃ", "wholesome=kusala@kusala; root=mūlaṃ; wholesome root=kusalamūlaṃ")
E("adussanā", "hating=dussanā@duss")
E("adussitattaṃ", "hating=dussitattaṃ@duss")
E("abyāpajjo", "absence=abyāpajjo; malice=byāpajjo; absence of malice=abyāpajjo")
# tranquillity, lightness, pliancy, workability, proficiency, uprightness
E("passaddhi", "tranquillity=passaddhi@passaddhi")
E("paṭipassaddhi", "tranquillity=paṭipassaddhi@passaddhi; full=paṭipassaddhi; full tranquillity=paṭipassaddhi")
E("passambhanā", "calming=passambhanā@passambh")
E("paṭipassambhanā", "calming=paṭipassambhanā@passambh; full calming=paṭipassambhanā")
E("paṭipassambhitattaṃ", "fully=paṭipassambhitattaṃ; calmed=passambhitattaṃ; fully calmed=paṭipassambhitattaṃ")
E("lahutā", "lightness=lahutā@lahutā")
E("lahupariṇāmatā", "quickness=lahu; change=pariṇāmatā; quickness to change=lahupariṇāmatā")
E("adandhanatā", "freedom=adandhanatā@a-; slowness=dandhanatā")
E("avitthanatā", "freedom=avitthanatā@a-; sluggishness=vitthanatā")
E("mudutā", "pliancy=mudutā@mudutā")
E("maddavatā", "softness=maddavatā")
E("akakkhaḷatā", "freedom=akakkhaḷatā@a-; hardness=kakkhaḷatā")
E("akathinatā", "freedom=akathinatā@a-; rigidity=kathinatā")
E("kammaññatā", "workability=kammaññatā@kammañña")
E("kammaññattaṃ", "workable=kammaññattaṃ@kammaññ")
E("kammaññabhāvo", "condition=bhāvo; workable=kammañña@kammaññ")
E("paguṇatā", "proficiency=paguṇatā@pāguñña")
E("paguṇattaṃ", "proficient=paguṇattaṃ@paguṇ")
E("paguṇabhāvo", "condition=bhāvo; proficient=paguṇa@paguṇ")
E("ujutā", "straightness=ujutā")
E("ujukatā", "uprightness=ujukatā@ujukatā")
E("ajimhatā", "freedom=ajimhatā@a-; deviousness=jimhatā")
E("avaṅkatā", "freedom=avaṅkatā@a-; crookedness=vaṅkatā")
E("akuṭilatā", "freedom=akuṭilatā@a-; twistedness=kuṭilatā")

# ============================================================ 2-03 additions to the strings
_BOJ = "awakening=sambojjhaṅgo@bojjhaṅga; factor=sambojjhaṅgo@aṅga; awakening factor=sambojjhaṅgo"
E("pītisambojjhaṅgo", _BOJ + "; rapture=pīti@pīti; factor of rapture=pītisambojjhaṅgo")
E("samādhisambojjhaṅgo", _BOJ + "; concentration=samādhi@samādhi; factor of concentration=samādhisambojjhaṅgo")
E("vīriyasambojjhaṅgo", _BOJ + "; energy=vīriya@vīriya; factor of energy=vīriyasambojjhaṅgo")
E("satisambojjhaṅgo", _BOJ + "; mindfulness=sati@sati; factor of mindfulness=satisambojjhaṅgo")
E("dhammavicayasambojjhaṅgo", _BOJ + "; investigation=vicaya@vicaya; investigation of states=dhammavicaya; "
  "factor of investigation=vicayasambojjhaṅgo")
E("passaddhisambojjhaṅgo", _BOJ + "; tranquillity=passaddhi@passaddhi; factor of tranquillity=passaddhisambojjhaṅgo")
E("maggaṅgaṃ maggapariyāpannaṃ", "path factor=maggaṅgaṃ; path=magga@magga; factor=aṅgaṃ@aṅga; "
  "included=pariyāpannaṃ; included in the path=maggapariyāpannaṃ")
E("catūhi vacīduccaritehi ārati", "kinds=duccaritehi; verbal=vacī; misconduct=duccaritehi; "
  "verbal misconduct=vacīduccaritehi; avoidance=ārati", lead=("avoidance", 3))
E("tīhi kāyaduccaritehi ārati", "kinds=duccaritehi; bodily=kāya; misconduct=duccaritehi; "
  "bodily misconduct=kāyaduccaritehi; avoidance=ārati", lead=("avoidance", 3))
E("micchāājīvā ārati", "wrong=micchā@micchā; livelihood=ājīvā@ājīva; wrong livelihood=micchāājīvā; avoidance=ārati",
  lead=("avoidance", 2))
E("virati", "abstaining=virati")
E("paṭivirati", "refraining=paṭivirati")
E("veramaṇī", "abstinence=veramaṇī")
E("akiriyā", "doing=kiriyā")
E("akaraṇaṃ", "performing=karaṇaṃ")
E("anajjhāpatti", "committing=ajjhāpatti")
E("velāanatikkamo", "overstepping=atikkamo; boundary=velā; overstepping the boundary=velāanatikkamo")
E("setughāto", "destroying=ghāto; causeway=setu; destroying the causeway=setughāto")

# ============================================================ opening sentences, 2-03
_LT = "world-transcending=lokuttaraṃ@lokuttara; develops=bhāveti"
E("lokuttaraṃ jhānaṃ bhāveti", _LT + "; absorption=jhānaṃ@jhāna; world-transcending absorption=lokuttaraṃ jhānaṃ; "
  "develops world-transcending=lokuttaraṃ jhānaṃ bhāveti; develops world-transcending absorption=lokuttaraṃ jhānaṃ bhāveti")
TWENTY = [  # Pali object, English object after "world-transcending", article, extra keyword spec
    ("maggaṃ", "path", True, "path=maggaṃ@magga"),
    ("satipaṭṭhānaṃ", "foundation of mindfulness", True,
     "foundation=paṭṭhānaṃ; mindfulness=sati@sati; foundation of mindfulness=satipaṭṭhānaṃ"),
    ("sammappadhānaṃ", "right striving", True, "right=sammā@sammā; striving=padhānaṃ; right striving=sammappadhānaṃ"),
    ("iddhipādaṃ", "basis of spiritual power", True,
     "basis=pādaṃ; spiritual=iddhi; power=iddhi@iddhi; spiritual power=iddhi; basis of spiritual power=iddhipādaṃ"),
    ("indriyaṃ", "faculty", True, "faculty=indriyaṃ@indriya"),
    ("balaṃ", "power", True, "power=balaṃ@bala"),
    ("bojjhaṅgaṃ", "awakening factor", True,
     "awakening=bojjhaṅgaṃ@bojjhaṅga; factor=bojjhaṅgaṃ@aṅga; awakening factor=bojjhaṅgaṃ"),
    ("saccaṃ", "truth", True, "truth=saccaṃ"),
    ("samathaṃ", "calm", False, "calm=samathaṃ@samatha"),
    ("dhammaṃ", "state", True, "state=dhammaṃ"),
    ("khandhaṃ", "aggregate", True, "aggregate=khandhaṃ@khandha"),
    ("āyatanaṃ", "sense base", True, "sense=āyatanaṃ@āyatana; sense base=āyatanaṃ; base=āyatanaṃ@āyatana"),
    ("dhātuṃ", "element", True, "element=dhātuṃ@dhātu"),
    ("āhāraṃ", "nutriment", True, "nutriment=āhāraṃ@āhāra"),
    ("phassaṃ", "contact", False, "contact=phassaṃ@phassa"),
    ("vedanaṃ", "feeling", False, "feeling=vedanaṃ@vedanā"),
    ("saññaṃ", "perception", False, "perception=saññaṃ@saññā"),
    ("cetanaṃ", "intention", False, "intention=cetanaṃ@cetanā"),
    ("cittaṃ", "mind", True, "mind=cittaṃ@citta"),
]
for pi, en, art, extra in TWENTY:
    whole = f"lokuttaraṃ {pi} bhāveti"
    words = en.split()
    spec = [_LT, extra, f"develops {'a ' if art else ''}world-transcending={whole}"]
    for k in range(1, len(words) + 1):
        pre = " ".join(words[:k])
        spec.append(f"world-transcending {pre}=lokuttaraṃ {pi}")
        spec.append(f"develops {'a ' if art else ''}world-transcending {pre}={whole}")
    E(whole, "; ".join(spec))
E("niyyānikaṃ apacayagāmiṃ", "leads=niyyānikaṃ@niyyānika; leads to liberation=niyyānikaṃ; liberation=niyyānikaṃ; "
  "leads=gāmiṃ@gāmin; liberation and leads=niyyānikaṃ apacayagāmiṃ; away=apacaya; accumulation=caya; "
  "leads away=apacayagāmiṃ")
E("diṭṭhigatānaṃ pahānāya", "wrong=diṭṭhigatānaṃ@diṭṭhigata; views=diṭṭhigatānaṃ; wrong views=diṭṭhigatānaṃ; "
  "abandoning=pahānāya@pahāna; abandoning of wrong=diṭṭhigatānaṃ pahānāya; abandoning of wrong views=diṭṭhigatānaṃ pahānāya")
E("kāmarāgabyāpādānaṃ tanubhāvāya", "sensual=kāma@kāma; lust=rāga@rāga; sensual lust=kāmarāga; ill=byāpādānaṃ; "
  "ill will=byāpādānaṃ; will=byāpādānaṃ; weakening=tanubhāvāya")
E("kāmarāgabyāpādānaṃ anavasesappahānāya", "sensual=kāma@kāma; lust=rāga@rāga; sensual lust=kāmarāga; "
  "ill=byāpādānaṃ; ill will=byāpādānaṃ; will=byāpādānaṃ; abandoning=pahānāya@pahāna; remainder=avasesa")
E("rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya",
  "lust=rāga@rāga; fine-material=rūpa; existence=rūpa@rūpa; immaterial=arūpa@arūpa; existence=arūpa@rūpa; "
  "conceit=māna; restlessness=uddhacca; ignorance=avijjāya; abandoning=pahānāya@pahāna; remainder=avasesa")
for o in ("paṭhamāya", "dutiyāya", "tatiyāya", "catutthāya"):
    E(f"{o} bhūmiyā pattiyā", "stage=bhūmiyā; reaching=pattiyā")
E("vivicceva kāmehi", "quite=eva; secluded=vivicca; sensual=kāmehi@kāma; pleasures=kāmehi; sensual pleasures=kāmehi; "
  "secluded from sensual=vivicceva kāmehi")
E("vitakkavicārānaṃ vūpasamā", "stilling=vūpasamā; applied=vitakka@vitakka; applied thought=vitakka; "
  "sustained=vicārānaṃ@vicāra; sustained thought=vicārānaṃ; thought=vitakka@vitakka; thought=vicārānaṃ@vicāra")
for o, en in (("paṭhamaṃ", "first"), ("dutiyaṃ", "second"), ("tatiyaṃ", "third"), ("catutthaṃ", "fourth"),
              ("pañcamaṃ", "fifth")):
    E(f"{o} jhānaṃ", f"{en}={o}; absorption=jhānaṃ@jhāna; {en} absorption={o} jhānaṃ")
    E(f"{o} jhānaṃ upasampajja viharati", f"{en}={o}; absorption=jhānaṃ@jhāna; {en} absorption={o} jhānaṃ; "
      "enters=upasampajja; dwells=viharati; enters and dwells=upasampajja viharati")
for d, den in (("dukkha", "painful"), ("sukha", "pleasant")):
    for a, aen in (("dandha", "slow"), ("khippa", "quick")):
        E(f"{d}paṭipadaṃ {a[:-1]}ābhiññaṃ",
          f"{den}={d}; progress=paṭipadaṃ@paṭipadā; {den} progress={d}paṭipadaṃ; {aen}={a}; "
          f"direct=abhiññaṃ; knowledge=abhiññaṃ@abhiññā; direct knowledge=abhiññaṃ; {aen} direct={a[:-1]}ābhiññaṃ; "
          f"{aen} direct knowledge={a[:-1]}ābhiññaṃ; progress and {aen}=paṭipadaṃ {a}")
E("suññataṃ", "empty=suññataṃ")
E("appaṇihitaṃ", "desireless=appaṇihitaṃ@appaṇihita")
for o, en in (("chanda", "desire"), ("vīriya", "energy"), ("citta", "mind"), ("vīmaṃsā", "inquiry")):
    E(f"{o[:-1]}ādhipateyyaṃ",
      f"{en}={o}@{o}; dominant=ādhipateyyaṃ@adhipati; factor=ādhipateyyaṃ@adhipati; dominant factor=ādhipateyyaṃ")

# ============================================================ headings and closing lines
E("Cittuppādakaṇḍaṃ", "chapter=kaṇḍaṃ; arising=uppāda; mind=Citta@citta; arising of mind=Cittuppāda")
E("Kāmāvacarakusalaṃ", "sense=Kāma@kāma; sphere=avacara@avacara; sense sphere=Kāmāvacara; wholesome=kusalaṃ@kusala; "
  "wholesome mind=kusalaṃ; mind=kusalaṃ@citta")
E("Padabhājanī", "analysis=bhājanī; terms=Pada")
E("Padabhājanīyaṃ", "analysis=bhājanīyaṃ; terms=Pada")
E("Koṭṭhāsavāro", "categories=Koṭṭhāsa; section=vāro@vāra")
E("Suññatavāro", "emptiness=Suññata; section=vāro@vāra")
E("Paṭhamabhāṇavāro", "first=Paṭhama; recitation=bhāṇa; section=vāro@vāra; recitation section=bhāṇavāro")
E("Dutiyabhāṇavāro", "second=Dutiya; recitation=bhāṇa; section=vāro@vāra; recitation section=bhāṇavāro")
for o, en in (("Paṭhamaṃ", "first"), ("Dutiyaṃ", "second"), ("Tatiyaṃ", "third"), ("Catutthaṃ", "fourth"),
              ("Pañcamaṃ", "fifth"), ("Chaṭṭhaṃ", "sixth"), ("Sattamaṃ", "seventh"), ("Aṭṭhamaṃ", "eighth")):
    E(f"{o} cittaṃ", f"{en}={o}; type=cittaṃ@citta; type of mind=cittaṃ; mind=cittaṃ@citta")
E("Aṭṭha kāmāvacaramahākusalacittāni", "eight=Aṭṭha; sense=kāma@kāma; sphere=avacara@avacara; "
  "sense sphere=kāmāvacara; great=mahā; wholesome=kusala@kusala; types=cittāni; types of mind=cittāni; "
  "mind=cittāni@citta")
E("Lokuttarakusalaṃ", "world-transcending=Lokuttara@lokuttara; wholesome=kusalaṃ@kusala; wholesome mind=kusalaṃ; "
  "mind=kusalaṃ@citta; world-transcending wholesome=Lokuttarakusalaṃ; "
  "world-transcending wholesome mind=Lokuttarakusalaṃ")
E("Suddhikapaṭipadā", "plain=Suddhika; progress=paṭipadā@paṭipadā; plain progress=Suddhikapaṭipadā")
E("Suññataṃ", "emptiness=Suññataṃ@suññata")
E("Suññatamūlakapaṭipadā", "emptiness=Suññata@suññata; rooted=mūlaka; progress=paṭipadā@paṭipadā; "
  "progress rooted=mūlakapaṭipadā; progress rooted in emptiness=Suññatamūlakapaṭipadā")
E("Appaṇihitaṃ", "desireless=Appaṇihitaṃ@appaṇihita")
E("Appaṇihitamūlakapaṭipadā", "desireless=Appaṇihita@appaṇihita; rooted=mūlaka; progress=paṭipadā@paṭipadā; "
  "progress rooted=mūlakapaṭipadā")
E("Vīsati mahānayā", "twenty=Vīsati; great=mahā; methods=nayā; great methods=mahānayā")
E("Adhipati", "dominant=Adhipati@adhipati; factors=Adhipati; dominant factors=Adhipati")
for o, en in (("Paṭhamo", "first"), ("Dutiyo", "second"), ("Tatiyo", "third"), ("Catuttho", "fourth")):
    E(f"{o} maggo", f"{en}={o}; path=maggo@magga")
E("Lokuttaraṃ cittaṃ", "world-transcending=Lokuttaraṃ@lokuttara; mind=cittaṃ@citta; "
  "world-transcending mind=Lokuttaraṃ cittaṃ")

# words with no keyword of their own (frame words, counters, copulas): listed only so the scan can report
# any Pali word that is neither in the table nor here
SILENT = set("""katamo katamā katamaṃ katame katamāni tasmiṃ samaye hoti honti ayaṃ idaṃ ime imāni imā kho pana
…pe… yasmiṃ eko ekā ekaṃ cattāro dve tayo satta cha tīṇi vā tesaṃ""".split())

MAXL = max(len(k) for k in T)


def lc(tok):
    return tok[0].lower() + tok[1:]


def tokens(text):
    t = re.sub(r"\[[^\]]*\]", " ", text)
    t = t.replace("…pe…", " …pe… ")
    t = re.sub(r"^#+\s*", "", t)
    t = re.sub(r"[,?.;–\"“”]", " ", t)
    return t.split()


def segments(ch):
    segs, buf = {}, []
    for line in (PALI / f"{ch}.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        mm = re.search(r"\s*\^([0-9A-Za-z-]+)\s*$", line)
        buf.append(line[:mm.start()] if mm else line)
        if mm:
            segs[mm.group(1)] = buf
            buf = []
    return segs


def scan(lines, unknown):
    toks = []
    for line in lines:
        toks += tokens(line)
    out, i, pend = [], 0, False
    while i < len(toks):
        hit = None
        for L in range(min(MAXL, len(toks) - i), 0, -1):
            seg = tuple(toks[i:i + L])
            if seg in T:
                hit = (L, T[seg], False, seg)
                break
            low = (lc(seg[0]),) + seg[1:]
            if low != seg and low in T:
                hit = (L, T[low], True, low)
                break
        if hit is None:
            if lc(toks[i]) not in SILENT:
                unknown[toks[i]] += 1
            pend = False
            i += 1
            continue
        L, (contribs, lead), capd, key = hit
        if pend and isinstance(lead, tuple):
            out.append(("time is " + lead[0], "samaye " + " ".join(toks[i:i + lead[1]]), "MW"))
        phrase = " ".join(key)
        for kw, val, lem in contribs:
            if capd and val != NDE and (phrase.startswith(val) or (len(val) > 3 and phrase.startswith(val[:-1]))):
                val = val[0].upper() + val[1:]
            out.append((kw, val, lem))
        pend = lead == "FRAME"
        i += L
    return out


def resolve(contribs):
    d = {}
    for kw, val, lem in contribs:
        d.setdefault(kw, []).append((val, lem))
    res = {}
    for kw, lst in d.items():
        if " " in kw:
            res[kw] = lst[0][0]
            continue
        seen = {}
        for val, lem in lst:
            if val != NDE and lem not in seen:
                seen[lem] = val
        res[kw] = " / ".join(seen.values()) if seen else NDE
    return res


def build(ch):
    segs = segments(ch)
    src = (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()
    out, missing, joins, unknown = [], [], Counter(), Counter()
    for line in src:
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        lines = segs[bid]
        res = resolve(scan(lines, unknown))
        brackets = " ".join(re.findall(r"\[[^\]]*\]", " ".join(lines)))
        pairs = []
        for k in [k.strip() for k in rest.split(", ")]:
            v = res.get(k.lower())
            if v is None and (k.lower() == "variant" or (brackets and k in brackets)):
                v = NDE
            if v is None:
                missing.append((bid, k))
                v = "???"
            if " / " in v:
                joins[(k, v)] += 1
            assert ", " not in v, (bid, k, v)
            pairs.append(f"{v}={k}")
        out.append(f"[{bid}] " + ", ".join(pairs))
    (HERE / f"{ch}.mapped.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(ch, "lines", len(out), "missing", len(missing))
    for x in missing:
        print("   MISSING", *x)
    print("   joins:", dict(joins))
    print("   unknown Pali words (not in table):", dict(unknown))


if __name__ == "__main__":
    for ch in sys.argv[1:] or CHAPTERS:
        build(ch)
