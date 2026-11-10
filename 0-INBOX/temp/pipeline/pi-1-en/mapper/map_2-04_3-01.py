"""English->Pali keyword map for pi-1 chapters `2-04-cittuppadakandam` and `3-01-rupakandam`.

usage: python -I -X utf8 map_2-04_3-01.py [--show]
Writes <ch>.mapped.md next to <ch>.keywords.md. Conventions: map-conventions.md (incl. section 8).

Method. Each English keyword (looked up lowercased, so case variants share a value) has a list of
Pali candidates (lemma, regex, value). The regexes are written from the builder phrase tables
(build_2-04.py, const_2_03_2_04.py, build_ch2_01_sample.py, build_3-01.py, harmonise.py), so a
regex only fires on Pali that the builders render with that English word. In a segment, every
candidate is searched in that segment's Pali (variant brackets removed, as in the check script);
per lemma the FIRST occurrence wins (conv. 4); several lemmas are joined with " / " in order of
first occurrence. Identical Pali segments therefore always get identical values.
--show prints, per keyword, every distinct value it received (for review).
"""
import collections, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
NDE = "(no direct equivalent)"
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def segments(ch):
    """Same normalisation as check_preamble_1-matika.py (brackets, labels, heading marks removed)."""
    segs, buf = {}, []
    for line in (PALI / f"{ch}.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        mm = ID.search(line)
        buf.append(line[:mm.start()] if mm else line)
        if mm:
            t = " ".join(buf)
            t = re.sub(r"\[[^\]]*\]", " ", t)
            t = re.sub(r"\((Ka|Kha|Ga)\)", " ", t)
            t = re.sub(r"^#+\s*|\s#+\s", " ", t)
            segs[mm.group(1)] = re.sub(r"\s+", " ", t).strip()
            buf = []
    return segs


def E(rx, val=None, lem=None):
    """One Pali candidate. val: None -> group(1) if the regex has a group, else group(0);
    str -> fixed value; callable -> val(match). lem: lemma tag (default: one shared tag)."""
    return (lem, re.compile(rx), val)


def plus(s):
    return lambda m: m.group(0) + s


def lead_a(m):
    """'āvacarassa' -> 'avacarassa' (member written in its own form, conv. 1.4)."""
    return "a" + m.group(0)[1:]


# =====================================================================================
# shared candidates (both chapters)
# =====================================================================================
COMMON = {
    "variant": NDE,
    "having": NDE,       # English auxiliary of the perfect/absolutive (pi-4 precedent)
    "using": NDE,        # "using earth as the meditation device": accusative relation only
    "spheres": NDE, "existence": NDE, "spheres of existence": NDE,   # (a)pariyāpanna, conv. 5
    "aggregate": [E(r"(?<=k)khandh(?:o|aṃ)\b")],
    "aggregate of consciousness": [E(r"viññāṇakkhandh(?:o|aṃ)\b")],
    "aggregate of feeling": [E(r"vedanākkhandh(?:o|aṃ)\b")],
    "aggregate of mental": [E(r"saṅkhārakkhandh(?:o|aṃ)\b")],
    "aggregate of perception": [E(r"saññākkhandh(?:o|aṃ)\b")],
    "mental formations": [E(r"saṅkhāra(?=kkhandh)")],
    "formations": [E(r"saṅkhāra(?=kkhandh)")],
    "indeterminate": [E(r"\b[Aa]byākat(?:ā|aṃ|ameva)\b"), E(r"\b[Aa]byākata(?=vipāk|mūl)")],
    "indeterminate states": [E(r"dhammā abyākatā")],
    "unwholesome states": [E(r"dhammā akusalā|akusalānaṃ dhammānaṃ"),
                           E(r"(?<=Kusal)ākusalānaṃ dhammānaṃ", "akusalānaṃ dhammānaṃ")],
    "wholesome states": [E(r"dhammā kusalā")],
    "immaterial sphere": [E(r"arūpāvacar(?:assa|aṃ|ameva|ā|a)\b|Arūpāvacara")],
    "fine-material sphere": [E(r"(?<![Aa])\b[Rr]ūpāvacar(?:assa|aṃ|ameva|ā|a)\b|\bRūpāvacara")],
    "sense sphere": [E(r"kāmāvacar(?:assa|aṃ|ameva|ā)\b")],
    "sphere": [E(r"(?<=[Kk]ām|[Rr]ūp)āvacar(?:assa|aṃ|ameva|ā|a)(?=\b|vipāk)", lead_a)],
    "sense": [E(r"\bkām(?=āvacar)", "kāma", "kāma"), E(r"(?<=dv)āyatanāni", lem="āyatana")],
    "fine-material": [E(r"(?<![Aa])\b[Rr]ūp(?=āvacar|ūpapatt)", plus("a"))],
    "immaterial": [E(r"\barūpino\b|\barūpīnaṃ\b"), E(r"\b[Aa]rūp(?=āvacar|ūpapatt)", plus("a"))],
    "immaterial states": [E(r"arūpino dhammā|arūpīnaṃ dhammānaṃ")],
    "feeling": [E(r"vedanā(?:ya\b)?")],
    "perception": [E(r"saññā(?:ya\b)?(?!naṃ)")],
    "intention": [E(r"\bcetanā(?:ya\b)?")],
    "consciousness": [E(r"\bviññāṇaṃ\b|\bviññāṇa(?=kkhandh|ñcāyatana)|(?<=pañca)viññāṇāni|\bviññāṇehi\b")],
    "kinds": [E(r"(?<=pañca)viññāṇāni|\bviññāṇehi\b")],
    "element": [E(r"dhātu(?=\b|samphass|viññeyy|somanass|upekkh)", lem="dhātu"),
                E(r"(?<=mahā)bhūt(?:aṃ|ā)\b", lem="bhūta")],
    "mind-consciousness": [E(r"manoviññāṇa(?=dhātu)")],
    "mind-consciousness element": [E(r"manoviññāṇadhātu")],
    "mind element": [E(r"manodhātu")],
    "eye-consciousness": [E(r"cakkhuviññāṇ(?:aṃ\b|a(?=dhātu)|assa\b)")],
    "eye-consciousness element": [E(r"cakkhuviññāṇadhātu")],
    "body-consciousness": [E(r"kāyaviññāṇ(?:aṃ\b|a(?=dhātu)|assa\b)")],
    "body-consciousness element": [E(r"kāyaviññāṇadhātu")],
    "body-contact": [E(r"kāyasamphass(?:aj(?:aṃ|ā|āya)|assa)\b")],
    "born of body-contact": [E(r"kāyasamphassaj(?:aṃ|ā|āya)\b")],
    "accompanied": [E(r"sahagat(?:aṃ|ā|ameva)\b")],
    "accompanied by equanimity": [E(r"upekkhāsahagat(?:aṃ|ā|ameva)\b")],
    "accompanied by happiness": [E(r"sukhasahagat(?:aṃ|ā|ameva)\b")],
    "equanimity": [E(r"upekkh(?:ā(?=\b|sahagat)|(?=indriy))", "upekkhā")],
    "faculty": [E(r"indriyaṃ\b", "indriyaṃ")],
    "faculty of life": [E(r"jīvitindriyaṃ")],
    "life": [E(r"\bjīvitaṃ\b|\bjīvit(?=indriy)", lambda m: m.group(0) if m.group(0).endswith("ṃ") else "jīvita")],
    "mental": [
        E(r"\bdhamm(?=ārammaṇ)", "dhamma", "dhamma"),
        E(r"\bcetasik(?:aṃ|o)\b|(?<=a)cetasik(?:aṃ|ameva)\b", lem="cetasika"),
        E(r"\bmānasaṃ\b|\bmano(?=vilekho)", lem="manas"),
        E(r"saṅkhāra(?=kkhandh)", lem="saṅkhāra"),
    ],
    "except": [E(r"ṭhapetvā")],
    "dependently": [E(r"paṭicca(?=samuppann)")],
    "dependently arisen": [E(r"paṭiccasamuppannā")],
    "dependently arisen immaterial": [E(r"paṭiccasamuppannā arūpino")],
    "arisen immaterial": [E(r"samuppannā arūpino")],
    "arisen immaterial states": [E(r"samuppannā arūpino dhammā")],
    "arisen": [E(r"\buppann(?:aṃ|ā)\b", lem="uppanna"), E(r"(?<=paṭicca)samuppannā", lem="samuppanna")],
    "contact": [E(r"\b[Pp]hass(?:o|ā)\b|\bsaṃphus\w+|(?<=dhātu)samphassaj(?:aṃ|ā)\b")],
    "unconditioned": [E(r"asaṅkhatā")],
}

# =====================================================================================
# 2-04-cittuppadakandam
# =====================================================================================
L204 = dict(COMMON)
L204.update({
    # ---- headings / closings
    "twelve": [E(r"\bDvādasa\b")],
    "minds": [E(r"(?<=akusala)cittāni|\bakusalāni\b")],
    "unwholesome minds": [E(r"akusalacittāni|\bakusalāni\b")],
    "indeterminate results": [E(r"Abyākatavipāko")],
    "great results": [E(r"(?<=Aṭṭha)mahāvipākā")],
    "resulting": [E(r"(?<=usala)vipāk(?:āni\b|ā\b|a(?=\w))")],
    "resulting from wholesome": [E(r"[Kk]usalavipāk(?:āni\b|ā\b|a(?=\w))")],
    "consciousness resulting": [E(r"vipāk(?:a|āni )pañcaviññāṇāni")],
    "element resulting": [E(r"vipāk(?:a|ā )(?:upekkhāsahagatā )?mano(?:viññāṇa)?dhātu")],
    "mind element resulting": [E(r"vipāk(?:a|ā )manodhātu")],
    "mind-consciousness element resulting": [E(r"vipāk(?:a|ā )(?:upekkhāsahagatā )?manoviññāṇadhātu")],
    # ---- opening sentences
    "wholesome": [E(r"\b[Kk]usala(?=vipāk)|\bkusalassa\b|\bkusalā\b")],
    "wholesome action": [E(r"kusalassa kammassa|\b[Kk]usala(?=vipāk)")],
    "unwholesome": [E(r"\bakusal(?:aṃ|ā|ānaṃ|āni)\b|\bakusala(?=mūlaṃ|cittāni)")],
    "unwholesome mind": [E(r"akusalaṃ cittaṃ")],
    "mind has arisen": [E(r"cittaṃ uppannaṃ")],
    "element has arisen": [E(r"(?:(?<=mano)|(?<=ṇa))dhātu uppannā", "dhātu uppannā")],
    "done": [E(r"katattā")],
    "accumulated": [E(r"upacitattā")],
    "accompanied by joy": [E(r"somanassasahagat(?:aṃ|ā)\b")],
    "accompanied by sadness": [E(r"domanassasahagataṃ")],
    "joy": [E(r"somanass(?=a?sahagat|indriy)", "somanassa")],
    "sadness": [E(r"domanass(?=a?sahagat|indriy)", "domanassa")],
    "associated": [E(r"sampayutt(?:aṃ|ā)\b")],
    "dissociated": [E(r"vippayutt(?:aṃ|ā)\b")],
    "dissociated from wrong": [E(r"diṭṭhigatavippayuttaṃ")],
    "dissociated from knowledge": [E(r"ñāṇavippayuttā")],
    "knowledge": [E(r"ñāṇa(?=sampayutt|vippayutt)|(?<=añ)ñāṇaṃ")],
    "aversion": [E(r"paṭigha(?=sampayutt)")],
    "doubt": [E(r"vicikicchā")],
    "restlessness": [E(r"uddhacc(?:aṃ\b|a(?=sampayutt))")],
    "prompting": [E(r"(?<=sa)saṅkhārena")],
    "visible": [E(r"\brūp(?=ārammaṇ)", "rūpa")],
    "visible form": [E(r"\brūp(?=ārammaṇ)", "rūpa")],
    "form": [E(r"\brūp(?=ārammaṇ|asaññ)", "rūpa")],
    "material": [E(r"\brūpa(?=saññ)", "rūpa")],
    "material form": [E(r"\brūpa(?=saññ)", "rūpa")],
    "sound": [E(r"\bsadd(?=ārammaṇ)", "sadda")],
    "smell": [E(r"\bgandh(?=ārammaṇ)", "gandha")],
    "taste": [E(r"\bras(?=ārammaṇ)", "rasa")],
    "touch": [E(r"\bphoṭṭhabb(?=ārammaṇ)", "phoṭṭhabba")],
    "mental object": [E(r"dhammārammaṇ(?:aṃ|ā)\b")],
    "object": [E(r"ārammaṇ(?:aṃ|ā)\b")],
    "takes": [E(r"(?<=pan)ārabbha", "ārabbha")],
    "whatever": [E(r"\b(?:Yo|Yā|Yaṃ)\b(?= tasmiṃ| tesaṃ)|\bye(?= vā pana)|\byaṃ yaṃ(?= vā)")],
    "ear-consciousness": [E(r"sotaviññāṇaṃ")],
    "nose-consciousness": [E(r"ghānaviññāṇaṃ")],
    "tongue-consciousness": [E(r"jivhāviññāṇaṃ")],
    # ---- factor list / names
    "applied": [E(r"\bvitakk(?:o\b|a(?=vicār))")],
    "applied thought": [E(r"\bvitakk(?:o\b|a(?=vicār))")],
    "sustained": [E(r"\bvicāro\b|(?<=vitakka)vicārānaṃ")],
    "sustained thought": [E(r"\bvicāro\b|(?<=vitakka)vicārānaṃ")],
    "thought": [E(r"\bvitakk(?:o\b|a(?=vicār))", lem="vitakka"),
                E(r"\bvicāro\b|(?<=vitakka)vicārānaṃ", lem="vicāra"),
                E(r"saṅkappo", lem="saṅkappa")],
    "rapture": [E(r"\bpīti\b")],
    "happiness": [E(r"\bsukha(?=sahagat)|\bsukhaṃ(?= hoti)|(?<=cetasikaṃ )sukhaṃ")],
    "pleasure": [E(r"(?<=kāyikaṃ )sukhaṃ|\bsukh(?=indriy)|\bsukhassa\b",
                   lambda m: "sukha" if m.group(0) == "sukh" else m.group(0))],
    "one-pointedness": [E(r"(?<=cittass)ekaggatā")],
    "one-pointedness of mind": [E(r"cittassekaggatā")],
    "faculty of energy": [E(r"vīriyindriyaṃ")],
    "faculty of concentration": [E(r"samādhindriyaṃ")],
    "faculty of mind": [E(r"manindriyaṃ")],
    "faculty of joy": [E(r"somanassindriyaṃ")],
    "faculty of equanimity": [E(r"upekkhindriyaṃ")],
    "faculties": [E(r"indriyāni\b")],
    "concentration": [E(r"samādh(?:i\b|i(?=balaṃ)|(?=indriy))", "samādhi")],
    "power": [E(r"balaṃ\b")],
    "powers": [E(r"balāni\b")],
    "power of energy": [E(r"vīriyabalaṃ")],
    "power of concentration": [E(r"samādhibalaṃ")],
    "power of shamelessness": [E(r"ahirikabalaṃ")],
    "power of fearlessness": [E(r"anottappabalaṃ")],
    "shamelessness": [E(r"\bahirik(?:aṃ\b|a(?=balaṃ))")],
    "fearlessness": [E(r"\banottapp(?:aṃ\b|a(?=balaṃ))")],
    "fearlessness of wrongdoing": [E(r"\banottapp(?:aṃ\b|a(?=balaṃ))")],
    "wrongdoing": [E(r"\banottapp(?:aṃ\b|a(?=balaṃ))")],
    "wrong view": [E(r"diṭṭhigata(?=sampayutt|vippayutt)|micchādiṭṭhi")],
    "wrong thought": [E(r"micchāsaṅkappo")],
    "wrong effort": [E(r"micchāvāyāmo")],
    "wrong concentration": [E(r"micchāsamādhi")],
    "wrong path": [E(r"micchāpatho")],
    "wrong": [E(r"diṭṭhigata(?=sampayutt|vippayutt)", lem="diṭṭhigata"),
              E(r"micchā(?=diṭṭhi|saṅkapp|vāyām|samādhi|path)", lem="micchā"),
              E(r"kummaggo", lem="ku")],
    "view": [E(r"\bdiṭṭhi(?=gatasampayutt|gatavippayutt|\b)|(?<=micchā)diṭṭhi", "diṭṭhi")],
    "greed": [E(r"\blobho\b")],
    "delusion": [E(r"\bmoho\b")],
    "covetousness": [E(r"abhijjhā")],
    "calm": [E(r"\bsamatho\b")],
    "exertion": [E(r"\bpaggāho\b")],
    "non-distraction": [E(r"\bavikkhepo\b")],
    "hate": [E(r"\bdoso\b")],
    "ill": [E(r"\bbyāpādo\b")],
    "pain": [E(r"\bdukkhaṃ(?= hoti)|(?<=cetasikaṃ )dukkhaṃ")],
    "non-greed": [E(r"\balobho\b")],
    "non-hate": [E(r"\badoso\b")],
    "indeterminate root": [E(r"abyākatamūlaṃ")],
    "root": [E(r"(?:(?<=kusala)|(?<=byākata))mūlaṃ", lem="mūla"), E(r"\bhetu\b", lem="hetu")],
    "unwholesome root": [E(r"akusalamūlaṃ")],
    "time is contact": [E(r"samaye phasso")],
    "time is mind": [E(r"samaye cittaṃ")],
    "time is thinking": [E(r"samaye takko")],
    "time is exploring": [E(r"samaye cāro")],
    "time is mental": [E(r"samaye cetasikaṃ")],
    "time is view": [E(r"samaye diṭṭhi\b")],
    "time is greed": [E(r"samaye lobho")],
    "time is bodily": [E(r"samaye kāyikaṃ")],
    "mind": [
        E(r"\bcittaṃ\b|\bcittassa\b|\bcittass(?=ekaggatā)", lambda m: "cittassa" if m.group(0) == "cittass" else m.group(0), "citta"),
        E(r"\bcetaso\b", lem="cetas"),
        E(r"\bman(?=indriyaṃ|āyatanaṃ)|mano(?=dhātu)|(?<=avisāhaṭa)mānasatā",
          lambda m: "mana" if m.group(0) == "man" else m.group(0), "manas"),
    ],
    # ---- contact
    "touching": [E(r"\bphusanā")],
    "coming": [E(r"saṃphusanā")],
    "coming into contact": [E(r"saṃphusanā")],
    # ---- feeling strings
    "corresponding": [E(r"\btajjā")],
    "born": [E(r"samphassaj(?:aṃ|ā)\b")],
    "mind-contact": [E(r"cetosamphassaj(?:aṃ|ā)\b")],
    "born of mind-contact": [E(r"cetosamphassaj(?:aṃ|ā)\b")],
    "experience": [E(r"vedayitaṃ")],
    "experience born": [E(r"\w*samphassajaṃ (?:\S+ ){0,2}vedayitaṃ")],
    "feeling born": [E(r"\w*samphassajā (?:\S+ ){0,2}vedanā")],
    "pleasant experience": [E(r"sukhaṃ vedayitaṃ")],
    "pleasant experience born": [E(r"\w*samphassajaṃ sātaṃ sukhaṃ vedayitaṃ")],
    "pleasant feeling": [E(r"sukhā vedanā")],
    "pleasant feeling born": [E(r"\w*samphassajā sātā sukhā vedanā")],
    "pleasant": [E(r"\bsukh(?:aṃ|ā)(?= vedayitaṃ| vedanā)", lem="sukha"),
                 E(r"\badukkhamasukh(?:aṃ|ā)\b", lem="adukkhamasukha")],
    "painful nor pleasant": [E(r"\badukkhamasukh(?:aṃ|ā)\b")],
    "painful": [E(r"\bdukkh(?:aṃ|ā)(?= vedayitaṃ| vedanā)", lem="dukkha"),
                E(r"\badukkhamasukh(?:aṃ|ā)\b", lem="adukkhamasukha")],
    "painful feeling": [E(r"dukkhā vedanā")],
    "comfort": [E(r"\bsātaṃ\b")],
    "comfortable": [E(r"\bsāt(?:aṃ|ā)\b")],
    "uncomfortable": [E(r"\basāt(?:aṃ|ā)\b"), E(r"(?<=n)āsātaṃ", "asātaṃ")],
    "discomfort": [E(r"\basātaṃ\b")],
    "mental comfort": [E(r"cetasikaṃ sātaṃ")],
    "mental happiness": [E(r"cetasikaṃ sukhaṃ")],
    "mental pain": [E(r"cetasikaṃ dukkhaṃ")],
    "mental state": [E(r"cetasikaṃ(?= neva)")],
    "bodily": [E(r"kāyikaṃ")],
    # ---- perception / intention
    "perceiving": [E(r"sañjānanā")],
    "perceived": [E(r"sañjānitattaṃ")],
    "intending": [E(r"sañcetanā")],
    "intended": [E(r"cetayitattaṃ")],
    # ---- mind string
    "intellect": [E(r"\bmano\b")],
    "activity": [E(r"\bmānasaṃ\b")],
    "mental activity": [E(r"\bmānasaṃ\b")],
    "heart": [E(r"hadayaṃ")],
    "radiance": [E(r"paṇḍaraṃ")],
    "mind base": [E(r"manāyatanaṃ")],
    # ---- vitakka / vicāra strings
    "thinking": [E(r"\btakko\b")],
    "fixing": [E(r"\bappanā\b")],
    "directing": [E(r"abhiniropanā")],
    "exploring": [E(r"\bcāro\b")],
    "staying": [E(r"anusandhānatā")],
    "connected": [E(r"anusandhānatā")],
    "observing": [E(r"anupekkhanatā")],
    # ---- pīti string
    "gladness": [E(r"pāmojjaṃ")],
    "delight": [E(r"āmodanā")],
    "rejoicing": [E(r"\bpamodanā")],
    "mirth": [E(r"\bhāso\b")],
    "merriment": [E(r"\bpahāso\b")],
    "satisfaction": [E(r"\bvitti\b")],
    "elation": [E(r"odagyaṃ")],
    "contentment": [E(r"\battamanatā")],
    # ---- samādhi string
    "stability": [E(r"(?<=cittassa )ṭhiti")],
    "stability of mind": [E(r"cittassa ṭhiti")],
    "steadiness": [E(r"saṇṭhiti")],
    "firmness": [E(r"avaṭṭhiti")],
    "non-scattering": [E(r"avisāhāro")],
    "unscattered": [E(r"avisāhaṭa(?=mānasatā)")],
    "unscattered mind": [E(r"avisāhaṭamānasatā")],
    # ---- vīriya string
    "mental arousing": [E(r"cetasiko vīriyārambho")],
    "arousing": [E(r"(?<=vīriy)ārambho")],
    "setting": [E(r"\bnikkamo\b")],
    "pressing": [E(r"\bparakkamo\b")],
    "forward": [E(r"\bparakkamo\b")],
    "pressing forward": [E(r"\bparakkamo\b")],
    "striving": [E(r"uyyāmo")],
    "effort": [E(r"vāyāmo")],
    "zeal": [E(r"ussāho")],
    "ardour": [E(r"ussoḷhī")],
    "strength": [E(r"\bthāmo\b")],
    "steadfastness": [E(r"\bdhiti\b")],
    "unslackening": [E(r"asithila(?=parakkamatā)")],
    "putting": [E(r"(?<=a)nikkhitta(?=chanda|dhura)")],
    "desire": [E(r"(?<=nikkhitta)chandatā")],
    "burden": [E(r"(?<=nikkhitta)dhuratā|\bdhura(?=sampaggāho)")],
    "grasping": [E(r"(?<=dhura)sampaggāho|\bgāho\b")],
    # ---- jīvita string
    "lifespan": [E(r"\bāyu\b")],
    "persistence": [E(r"(?<=āyu )ṭhiti")],
    "carrying": [E(r"\byapanā")],
    "keeping": [E(r"\byāpanā")],
    "going": [E(r"\byāpanā")],
    "moving": [E(r"iriyanā")],
    "continuing": [E(r"vattanā")],
    "protection": [E(r"pālanā")],
    # ---- diṭṭhi string
    "views": [E(r"\bdiṭṭhi(?=gataṃ|gahanaṃ|kantāro|visūkāyikaṃ|vipphanditaṃ|saṃyojanaṃ)", "diṭṭhi")],
    "holding views": [E(r"\bdiṭṭhigataṃ")],
    "thicket": [E(r"(?<=diṭṭhi)gahanaṃ")],
    "wilderness": [E(r"(?<=diṭṭhi)kantāro")],
    "contortion": [E(r"(?<=diṭṭhi)visūkāyikaṃ")],
    "vacillation": [E(r"(?<=diṭṭhi)vipphanditaṃ")],
    "fetter": [E(r"(?<=diṭṭhi)saṃyojanaṃ")],
    "fetter of views": [E(r"diṭṭhisaṃyojanaṃ")],
    "fixation": [E(r"patiṭṭhāho")],
    "adherence": [E(r"abhiniveso")],
    "misapprehension": [E(r"\bparāmāso\b")],
    "road": [E(r"kummaggo")],
    "path": [E(r"(?<=micchā|dvedhā)patho", lem="patha"), E(r"\bmagg(?:o|aṃ)\b", lem="magga")],
    "wrongness": [E(r"micchattaṃ")],
    "sectarian": [E(r"titth(?=āyatanaṃ)", "tittha")],
    "doctrines": [E(r"titth(?=āyatanaṃ)", "tittha")],
    "distorted": [E(r"vipariyāsa(?=ggāho)")],
    "distorted grasp": [E(r"vipariyāsaggāho")],
    "grasp": [E(r"\bgāho\b|(?<=g)gāho\b", "gāho")],
    # ---- shame strings
    "ashamed": [E(r"\bhirīyati\b")],
    "fear": [E(r"ottappitabbena")],
    "fearing": [E(r"\bottappati\b")],
    "bad": [E(r"pāpakānaṃ")],
    "engaging": [E(r"samāpattiyā")],
    # ---- lobha / moha strings
    "greedy": [E(r"lubbhanā")],
    "lust": [E(r"sārāgo")],
    "lusting": [E(r"sārajjanā")],
    "lack": [E(r"\baññāṇaṃ\b")],
    "lack of knowledge": [E(r"\baññāṇaṃ\b")],
    "vision": [E(r"(?<=\ba)dassanaṃ")],
    "non-realisation": [E(r"anabhisamayo")],
    "understanding": [E(r"(?<=an)anubodho")],
    "awakening": [E(r"(?<=a)sambodho")],
    "non-penetration": [E(r"appaṭivedho")],
    "failure": [E(r"\basaṃgāhanā\b|\banekaṃsaggāho\b")],
    "fathom": [E(r"(?<=a)pariyogāhanā")],
    "consider": [E(r"(?<=a)samapekkhanā")],
    "review": [E(r"(?<=a)paccavekkhanā")],
    "oneself": [E(r"(?<=a)paccakkhakammaṃ")],
    "stupidity": [E(r"dummejjhaṃ")],
    "foolishness": [E(r"bālyaṃ")],
    "clear": [E(r"(?<=a)sampajaññaṃ")],
    "awareness": [E(r"(?<=a)sampajaññaṃ")],
    "clear awareness": [E(r"(?<=a)sampajaññaṃ")],
    "deep": [E(r"\bpamoho\b")],
    "utter": [E(r"\bsammoho\b")],
    "ignorance": [E(r"\bavijjā")],
    "flood": [E(r"(?<=avijj)ogho")],
    "yoke": [E(r"(?<=avijjā)yogo")],
    "underlying": [E(r"(?<=avijj)ānusayo", "anusayo")],
    "tendency": [E(r"(?<=avijj)ānusayo", "anusayo")],
    "obsession": [E(r"(?<=avijjā)pariyuṭṭhānaṃ")],
    "bar": [E(r"(?<=avijjā)laṅgī")],
    # ---- dosa string
    "hating": [E(r"\bdussanā")],
    "state of hating": [E(r"dussitattaṃ")],
    "malice": [E(r"byāpatti")],
    "malicious": [E(r"byāpajjanā")],
    "hostility": [E(r"\bvirodho")],
    "antagonism": [E(r"paṭivirodho")],
    "fierceness": [E(r"caṇḍikkaṃ")],
    "abusiveness": [E(r"asuropo")],
    "discontent": [E(r"anattamanatā")],
    # ---- vicikicchā string
    "uncertainty": [E(r"\bkaṅkhā\b")],
    "uncertain": [E(r"kaṅkhāyanā")],
    "perplexity": [E(r"\bvimati\b")],
    "indecision": [E(r"dveḷhakaṃ")],
    "forked": [E(r"dvedhā(?=patho)")],
    "wavering": [E(r"saṃsayo")],
    "definite": [E(r"(?<=an)ekaṃsa(?=ggāho)")],
    "stand": [E(r"(?<=an)ekaṃsa(?=ggāho)")],
    "hesitation": [E(r"\bāsappanā")],
    "faltering": [E(r"parisappanā")],
    "stiffness": [E(r"thambhitattaṃ")],
    "scratching": [E(r"(?<=mano)vilekho")],
    # ---- uddhacca string
    "disquiet": [E(r"avūpasamo")],
    "distraction": [E(r"\bvikkhepo\b")],
    "agitation": [E(r"bhantattaṃ")],
    # ---- 'Tasmiṃ kho pana samaye ...' list
    "aggregates": [E(r"\bkhandhā\b")],
    "bases": [E(r"(?<=dv)āyatanāni", "āyatanāni")],
    "sense bases": [E(r"(?<=dv)āyatanāni", "āyatanāni")],
    "elements": [E(r"dhātuyo")],
    "nutriments": [E(r"āhārā")],
    "five-factored": [E(r"pañcaṅgikaṃ")],
    "four-factored": [E(r"caturaṅgik(?:aṃ|o)\b")],
    "four-factored path": [E(r"caturaṅgiko maggo")],
    "three-factored": [E(r"tivaṅgiko")],
    "two-factored": [E(r"duvaṅgiko")],
    "absorption": [E(r"\bjhānaṃ\b")],
    "roots": [E(r"\bhetū\b")],
    "mental-object": [E(r"dhamm(?=āyatanaṃ|adhātu)", "dhamma")],
    "mental-object base": [E(r"dhammāyatanaṃ")],
    "mental-object element": [E(r"dhammadhātu")],
    # ---- results of the fine-material / immaterial spheres
    "develops": [E(r"bhāveti")],
    "develops the path": [E(r"maggaṃ bhāveti")],
    "path to rebirth": [E(r"ūpapattiyā maggaṃ", "upapattiyā maggaṃ")],
    "rebirth": [E(r"ūpapattiyā", "upapattiyā")],
    "quite": [E(r"(?<=vivicc)eva\b", "eva")],
    "secluded": [E(r"vivicc(?=eva)", "vivicca")],
    "secluded from sensual": [E(r"vivicceva kāmehi")],
    "sensual": [E(r"kāmehi")],
    "pleasures": [E(r"kāmehi")],
    "sensual pleasures": [E(r"kāmehi")],
    "enters": [E(r"upasampajja")],
    "dwells": [E(r"viharati")],
    "enters and dwells": [E(r"upasampajja viharati")],
    "earth": [E(r"pathavī(?=kasiṇ)")],
    "meditation": [E(r"(?<=pathavī)kasiṇaṃ")],
    "device": [E(r"(?<=pathavī)kasiṇaṃ")],
    "meditation device": [E(r"(?<=pathavī)kasiṇaṃ")],
    "stilling": [E(r"vūpasamā")],
    "fifth": [E(r"pañcamaṃ")],
    "fourth absorption": [E(r"catutthaṃ jhānaṃ")],
    "abandoning": [E(r"pahānā")],
    "abandoning of pleasure": [E(r"sukhassa ca pahānā")],
    "completely": [E(r"sabbaso")],
    "passing": [E(r"samatikkamā")],
    "passed": [E(r"samatikkamma")],
    "beyond": [E(r"samatikkam(?:ā|ma)\b")],
    "perceptions": [E(r"saññānaṃ")],
    "disappearance": [E(r"atthaṅgamā")],
    "attending": [E(r"(?<=a)manasikārā")],
    "diversity": [E(r"nānatta(?=saññ)")],
    "base of infinite": [E(r"(?<=ākās)ānañcāyatana(?:ṃ\b)?|viññāṇañcāyatanaṃ\b")],
    "infinite": [E(r"(?<=ākās)ānañc(?=āyatana)|viññāṇañc(?=āyatana)", plus("a"))],
    "space": [E(r"ākās(?=ānañc)", "ākāsa")],
    "nothingness": [E(r"ākiñcaññ(?=āyatana)", "ākiñcañña")],
    "non-perception": [E(r"(?<=nevasaññān)āsaññ(?=āyatana)", "asaññā")],
})
L204["minds"] = L204["minds"]

# =====================================================================================
# 3-01-rupakandam
# =====================================================================================
RF_RX = r"\brūpaṃ\b|\b[Rr]ūpa(?=saṅgaho|kaṇḍaṃ|vibhatti)|\brūpassa\b"
L301 = dict(COMMON)
L301.update({
    # ---- headings / closings
    "chapter": [E(r"(?<=Rūpa)kaṇḍaṃ")],
    "opening": [E(r"Uddeso")],
    "matrix": [E(r"Mātikā")],
    "pairs": [E(r"\bDukaṃ")],
    "set of ten": [E(r"Dasakaṃ")],
    "ten": [E(r"\b[Dd]asa(?=vidhena)|\bDasakaṃ")],
    "set of eleven": [E(r"Ekādasakaṃ")],
    "eleven": [E(r"\b[Ee]kādasa(?=vidhena)|\bEkādasakaṃ")],
    "classification": [E(r"(?<=Rūpa)vibhatti")],
    "exposition": [E(r"(?<=Ekaka)niddeso")],
    "therein": [E(r"Tattha")],
    "ways": [E(r"\b[Cc]atubbidhena\b|\b[Cc]habbidhena\b|(?<=\w)vidhena\b")],
    "classified": [E(r"(?<=rūpa)saṅgaho")],
    "form classified": [E(r"[Rr]ūpasaṅgaho")],
    "material form classified": [E(r"[Rr]ūpasaṅgaho")],
    "form is classified": [E(r"[Rr]ūpasaṅgaho")],
    # ---- material form
    "form": [E(RF_RX, lambda m: "rūpa" if m.group(0) == "rūpa" else m.group(0))],
    "material": [E(RF_RX, lambda m: "rūpa" if m.group(0) == "rūpa" else m.group(0))],
    "material form": [E(RF_RX, lambda m: "rūpa" if m.group(0) == "rūpa" else m.group(0))],
    "form derived": [E(r"upādāya rūpaṃ")],
    "material form derived": [E(r"upādāya rūpaṃ")],
    "form that makes": [E(r"rūpaṃ sappaṭighaṃ")],
    "material form accompanying": [E(r"rūpaṃ cittānuparivatti")],
    "material form arising": [E(r"rūpaṃ cittasamuṭṭhānaṃ")],
    "material form existing": [E(r"rūpaṃ cittasahabhu")],
    "form knowable": [E(r"viññeyyaṃ rūpaṃ")],
    "material form knowable": [E(r"viññeyyaṃ rūpaṃ")],
    # ---- opening statement
    "wholesome": [E(r"\bKusal(?=ākusal)", "Kusala"), E(r"\bkusalā\b")],
    "unwholesome": [E(r"(?<=Kusal)ākusalānaṃ", "akusalānaṃ"), E(r"(?<=n)ākusalā\b", "akusalā")],
    "wholesome nor unwholesome": [E(r"kusalā nākusalā")],
    "functional": [E(r"kiriyā")],
    "unconditioned element": [E(r"asaṅkhatā ca dhātu")],
    # ---- sets of one (^1-584 and, with -meva, ^1-594)
    "indeed": [E(r"(?<=m)eva\b", "eva")],
    "root": [E(r"\bhetu(?=\b|meva)")],
    "roots": [E(r"(?<=\ba)hetuk(?:aṃ|ameva)\b|\bhetu(?=vippayutt)|(?<=pahātabba)hetuk(?:aṃ|ameva)\b",
                lambda m: m.group(0))],
    "dissociated": [E(r"vippayutt(?:aṃ|ameva)\b")],
    "dissociated from mind": [E(r"cittavippayutt(?:aṃ|ameva)\b")],
    "conditioned": [E(r"\bsaṅkhat(?:aṃ|ameva)\b")],
    "worldly": [E(r"\blokiy(?:aṃ|ameva)\b")],
    "taints": [E(r"(?<=\bs)āsav(?:aṃ|ameva)\b")],
    "subject to taints": [E(r"\bsāsav(?:aṃ|ameva)\b")],
    "fetters": [E(r"\bsaṃyojaniy(?:aṃ|ameva)\b")],
    "subject to fetters": [E(r"\bsaṃyojaniy(?:aṃ|ameva)\b")],
    "ties": [E(r"\bganthaniy(?:aṃ|ameva)\b")],
    "subject to ties": [E(r"\bganthaniy(?:aṃ|ameva)\b")],
    "floods": [E(r"\boghaniy(?:aṃ|ameva)\b")],
    "subject to floods": [E(r"\boghaniy(?:aṃ|ameva)\b")],
    "yokes": [E(r"\byoganiy(?:aṃ|ameva)\b")],
    "subject to yokes": [E(r"\byoganiy(?:aṃ|ameva)\b")],
    "hindrances": [E(r"\bnīvaraṇiy(?:aṃ|ameva)\b")],
    "subject to hindrances": [E(r"\bnīvaraṇiy(?:aṃ|ameva)\b")],
    "misapprehended": [E(r"\bparāmaṭṭh(?:aṃ|ameva)\b")],
    "clinging": [E(r"\bupādāniy(?:aṃ|ameva)\b|(?<=upādiṇṇ)upādāniyaṃ")],
    "subject to clinging": [E(r"\bupādāniy(?:aṃ|ameva)\b|(?<=upādiṇṇ)upādāniyaṃ")],
    "defilement": [E(r"\bsaṃkilesik(?:aṃ|ameva)\b")],
    "subject to defilement": [E(r"\bsaṃkilesik(?:aṃ|ameva)\b")],
    "undefiled": [E(r"asaṃkiliṭṭha(?=saṃkilesik)")],
    "object": [E(r"ārammaṇ(?:aṃ|ameva)\b")],
    "factor": [E(r"(?<=\ba)cetasik(?:aṃ|ameva)\b")],
    "mind": [E(r"\bcitta(?=samuṭṭhān|sahabhu|vippayutt)|\bcitt(?=ānuparivatti)",
               lambda m: "citta", "citta"),
             E(r"\bmano(?=dhātu|viññeyy)", lem="manas")],
    "produces": [E(r"vipākadhamma(?=dhamm)")],
    "applied": [E(r"(?<=sa)vitakka(?=sa)")],
    "applied thought": [E(r"(?<=sa)vitakka(?=sa)")],
    "sustained": [E(r"(?<=sa)vicār(?=aṃ|ameva)", "vicāra")],
    "sustained thought": [E(r"(?<=sa)vicār(?=aṃ|ameva)", "vicāra")],
    "thought": [E(r"(?<=sa)vitakka(?=sa)", lem="vitakka"), E(r"(?<=sa)vicār(?=aṃ|ameva)", "vicāra", "vicāra")],
    "accompanied by rapture": [E(r"pītisahagat(?:aṃ|ameva)\b")],
    "rapture": [E(r"pīti(?=sahagat)")],
    "happiness": [E(r"sukha(?=sahagat)")],
    "abandoned": [E(r"\bpahātabb(?:aṃ|ameva)\b")],
    "seeing": [E(r"dassanena")],
    "states whose roots": [E(r"(?<=pahātabba)hetuk(?:aṃ|ameva)\b")],
    "accumulation": [E(r"\bācaya(?=gāmi)")],
    "away": [E(r"apacaya(?=gāmi)")],
    "leads": [E(r"(?<=ācaya)gāmi")],
    "training": [E(r"(?<=neva)sekkha")],
    "beyond": [E(r"(?<=nā)sekkh(?:aṃ|ameva)\b", lambda m: "a" + m.group(0))],
    "limited": [E(r"\bparitt(?:aṃ|ameva)\b")],
    "states not included": [E(r"\bapariyāpann(?:aṃ|ameva)\b")],
    "fixed": [E(r"(?<=\ba)niyat(?:aṃ|ameva)\b")],
    "lead to liberation": [E(r"(?<=\ba)niyyānik(?:aṃ|ameva)\b")],
    "liberation": [E(r"(?<=\ba)niyyānik(?:aṃ|ameva)\b")],
    "arisen": [E(r"\buppannaṃ\b")],
    "once": [E(r"\buppannaṃ(?= chahi)")],
    "knowable": [E(r"viññeyy(?:aṃ|ameva)\b")],
    "impermanent": [E(r"\banicc(?:aṃ|ameva)\b")],
    "ageing": [E(r"\bjaratā\b|\bjarā(?=bhibhūt)")],
    "overcome": [E(r"(?<=jar)ābhibhūt(?:aṃ|ameva)\b", lead_a)],
    "derived": [E(r"\bupādā(?:ya)?\b")],
    "great elements": [E(r"mahābhūtā\b")],
    "elements": [E(r"(?<=mahā)bhūtā\b")],
    "great element": [E(r"mahābhūtaṃ")],
    # ---- pairs / sets of three, four
    "produced": [E(r"\bupādiṇṇaṃ\b|\bupādiṇṇ(?=upādāniyaṃ)", lambda m: m.group(0) if m.group(0).endswith("ṃ") else "upādiṇṇa")],
    "past action": [E(r"\bupādiṇṇaṃ\b|\bupādiṇṇ(?=upādāniyaṃ)", lambda m: m.group(0) if m.group(0).endswith("ṃ") else "upādiṇṇa")],
    "produced by past": [E(r"\bupādiṇṇaṃ\b|\bupādiṇṇ(?=upādāniyaṃ)", lambda m: m.group(0) if m.group(0).endswith("ṃ") else "upādiṇṇa")],
    "action and subject": [E(r"\bupādiṇṇupādāniyaṃ")],
    "action but subject": [E(r"\banupādiṇṇupādāniyaṃ")],
    "visible": [E(r"\bsanidassanaṃ")],
    "invisible": [E(r"\banidassana(?:ṃ\b)?")],
    "invisible and makes": [E(r"anidassanaappaṭighaṃ")],
    "makes": [E(r"\bsappaṭighaṃ|(?<!s)appaṭighaṃ")],
    "makes impact": [E(r"\bsappaṭighaṃ")],
    "makes no impact": [E(r"(?<!s)appaṭighaṃ")],
    "faculty": [E(r"indriyaṃ\b", "indriyaṃ")],
    "intimation": [E(r"viññatti")],
    "arise": [E(r"(?<=citta)samuṭṭhānaṃ")],
    "arises": [E(r"(?<=citta)samuṭṭhānaṃ")],
    "arising": [E(r"(?<=citta)samuṭṭhānaṃ")],
    "arising from mind": [E(r"cittasamuṭṭhānaṃ")],
    "exist": [E(r"cittasahabhu")],
    "exists": [E(r"cittasahabhu")],
    "existing": [E(r"cittasahabhu")],
    "together": [E(r"cittasahabhu")],
    "accompanies": [E(r"(?<=citt)ānuparivatti", "anuparivatti")],
    "accompany": [E(r"(?<=citt)ānuparivatti", "anuparivatti")],
    "accompanying": [E(r"(?<=citt)ānuparivatti", "anuparivatti")],
    "accompanying mind": [E(r"cittānuparivatti")],
    "internal": [E(r"ajjhattikaṃ")],
    "external": [E(r"bāhiraṃ")],
    "gross": [E(r"oḷārikaṃ")],
    "subtle": [E(r"sukhumaṃ")],
    "eye-contact": [E(r"cakkhusamphass(?:assa|ajāya)\b")],
    "ear-contact": [E(r"sotasamphassassa")],
    "nose-contact": [E(r"ghānasamphassassa")],
    "tongue-contact": [E(r"jivhāsamphassassa")],
    "born": [E(r"(?:(?<=cakkhu)|(?<=kāya))samphassajāya")],
    "feeling born": [E(r"(?:(?<=cakkhu)|(?<=kāya))samphassajāya vedanāya")],
    "eye": [E(r"\b[Cc]akkh(?=āyatana|udhātu|undriy|uviññeyy)", plus("u"))],
    "ear": [E(r"\b[Ss]ot(?=āyatana|adhātu|indriy|aviññeyy)", plus("a"))],
    "nose": [E(r"\b[Gg]hān(?=āyatana|adhātu|indriy|aviññeyy)", plus("a"))],
    "tongue": [E(r"\b[Jj]ivh(?=āyatana|ādhātu|indriy|āviññeyy)", plus("ā"))],
    "body": [E(r"\b[Kk]āy(?=āyatana|adhātu|indriy|aviññeyy)", plus("a"))],
    "visible-form": [E(r"\brūp(?=āyatana|adhātu)", "rūpa")],
    "sound": [E(r"\bsadd(?=āyatana|adhātu)", "sadda")],
    "smell": [E(r"\bgandh(?=āyatana|adhātu)", "gandha")],
    "taste": [E(r"\bras(?=āyatana|adhātu)", "rasa")],
    "touch": [E(r"\bphoṭṭhabb(?=āyatana|adhātu)", "phoṭṭhabba", "phoṭṭhabba"),
              E(r"(?<=sukha|ukkha)samphassaṃ", lem="samphassa")],
    "eye base": [E(r"[Cc]akkhāyatanaṃ")],
    "ear base": [E(r"sotāyatanaṃ")],
    "nose base": [E(r"ghānāyatanaṃ")],
    "tongue base": [E(r"jivhāyatanaṃ")],
    "body base": [E(r"kāyāyatanaṃ")],
    "visible-form base": [E(r"\brūpāyatanaṃ")],
    "sound base": [E(r"saddāyatanaṃ")],
    "smell base": [E(r"gandhāyatanaṃ")],
    "taste base": [E(r"rasāyatanaṃ")],
    "touch base": [E(r"phoṭṭhabbāyatanaṃ")],
    "mental-object": [E(r"dhamm(?=āyatana)", "dhamma")],
    "mental-object base": [E(r"dhammāyatana(?=pariyāpann)")],
    "eye element": [E(r"cakkhudhātu")],
    "ear element": [E(r"sotadhātu")],
    "nose element": [E(r"ghānadhātu")],
    "tongue element": [E(r"jivhādhātu")],
    "body element": [E(r"kāyadhātu")],
    "visible-form element": [E(r"\brūpadhātu")],
    "sound element": [E(r"saddadhātu")],
    "smell element": [E(r"gandhadhātu")],
    "taste element": [E(r"rasadhātu")],
    "touch element": [E(r"phoṭṭhabbadhātu")],
    "space": [E(r"ākāsa(?=dhātu)")],
    "space element": [E(r"ākāsadhātu")],
    "water": [E(r"āpo(?=dhātu)")],
    "water element": [E(r"āpodhātu")],
    "earth": [E(r"Pathavī(?=dhātu)")],
    "earth element": [E(r"Pathavīdhātu")],
    "fire": [E(r"tejo(?=dhātu)")],
    "fire element": [E(r"tejodhātu")],
    "air": [E(r"vāyo(?=dhātu)")],
    "air element": [E(r"vāyodhātu")],
    "femininity": [E(r"itth(?=indriy)", "itthi")],
    "faculty of femininity": [E(r"itthindriyaṃ")],
    "masculinity": [E(r"puris(?=indriy)", "purisa")],
    "faculty of masculinity": [E(r"purisindriyaṃ")],
    "bodily": [E(r"kāya(?=viññatti)")],
    "bodily intimation": [E(r"kāyaviññatti")],
    "verbal": [E(r"vacī(?=viññatti)")],
    "verbal intimation": [E(r"vacīviññatti")],
    "lightness": [E(r"lahutā")],
    "lightness of material": [E(r"rūpassa lahutā")],
    "pliancy": [E(r"mudutā")],
    "pliancy of material": [E(r"rūpassa mudutā")],
    "workability": [E(r"kammaññatā")],
    "workability of material": [E(r"rūpassa kammaññatā")],
    "growth of material": [E(r"rūpassa upacayo")],
    "continuity": [E(r"santati")],
    "continuity of material": [E(r"rūpassa santati")],
    "ageing of material": [E(r"rūpassa jaratā")],
    "impermanence": [E(r"aniccatā")],
    "impermanence of material": [E(r"rūpassa aniccatā")],
    "edible": [E(r"kabaḷīkāro")],
    "edible food": [E(r"kabaḷīkāro āhāro")],
    "food": [E(r"\bāhāro\b")],
    "heard": [E(r"\bsutaṃ\b")],
    "sensed": [E(r"\bmutaṃ\b")],
    "cognized": [E(r"\bviññātaṃ\b")],
    "pleasant": [E(r"sukha(?=samphass)")],
    "painful": [E(r"dukkha(?=samphass)")],
    "mental": [E(r"saṅkhāra(?=kkhandh)", lem="saṅkhāra"),
               E(r"(?<=\ba)cetasik(?:aṃ|ameva)\b", lem="cetasika")],
})


def value_for(kw, cands, text):
    if isinstance(cands, str):
        return cands
    best = {}
    for lem, rx, val in cands:
        m = rx.search(text)
        if not m:
            continue
        if val is None:
            v = m.group(1) if rx.groups else m.group(0)
        elif callable(val):
            v = val(m)
        else:
            v = val
        tag = lem or "_"
        if tag not in best or m.start() < best[tag][0]:
            best[tag] = (m.start(), v)
    if not best:
        return None
    vals = []
    for _, v in sorted(best.values()):
        if v not in vals:
            vals.append(v)
    return " / ".join(vals)


def build(ch, lex, show=False):
    segs = segments(ch)
    out, missing, seen = [], [], collections.defaultdict(collections.Counter)
    for line in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        text = segs[bid]
        pairs = []
        for k in [x.strip() for x in rest.split(", ")]:
            cands = lex.get(k.lower())
            v = None if cands is None else value_for(k, cands, text)
            if v is None:
                missing.append((bid, k, "no entry" if cands is None else "no match"))
                v = "???"
            assert ", " not in v, (bid, k, v)
            seen[k.lower()][v] += 1
            pairs.append(f"{v}={k}")
        out.append(f"[{bid}] " + ", ".join(pairs))
    if missing:
        for x in missing:
            print("MISSING", *x)
        raise SystemExit(f"{ch}: {len(missing)} unmapped keywords")
    (HERE / f"{ch}.mapped.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(ch, "lines", len(out))
    if show:
        for k in sorted(seen):
            print(f"  {k}: " + " | ".join(f"{v} ({n})" for v, n in seen[k].most_common()))


if __name__ == "__main__":
    show = "--show" in sys.argv
    build("2-04-cittuppadakandam", L204, show)
    build("3-01-rupakandam", L301, show)
