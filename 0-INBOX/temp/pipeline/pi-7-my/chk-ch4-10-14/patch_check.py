"""Development helper: adapt the copied model checker (check_ch4-10-14.py, a copy of check_ch4-02-09.py) to 4-10 … 4-14.
Every replacement must apply exactly once."""
import pathlib

HERE = pathlib.Path(__file__).resolve().parents[1]
P = HERE / "check_ch4-10-14.py"
t = P.read_text(encoding="utf-8")
frozen = (HERE / "chk-ch4-10-14" / "freeze.txt").read_text(encoding="utf-8")
frozen = frozen[:frozen.index("\nMicchattattikaṃ")] + "\n"


def rep(old, new, n=1):
    global t
    assert t.count(old) == n, (old[:80], t.count(old))
    t = t.replace(old, new)


rep('"""Per-line check of the Burmese pi-7 chapters 4-02 … 4-09 (the first DUKATIKA chapters: a dyad term combined with a\n'
    'triad term on one noun) against the Pāli (adapted from check_ch3-01-02.py;',
    '"""Per-line check of the Burmese pi-7 chapters 4-10 … 4-14 (the remaining DUKATIKA chapters: a dyad term combined\n'
    'with a triad term on one noun) against the Pāli (adapted from check_ch4-02-09.py;')
rep("usage: python3 -I -X utf8 check_ch4-02-09.py [chapter ...] [--out DIR] [--mutate] [--sample] [--pe] [--groups]",
    "usage: python3 -I -X utf8 check_ch4-10-14.py [chapter ...] [--out DIR] [--mutate] [--sample] [--regress] [--pe]\n"
    "       [--groups]")
rep("--mutate  plants errors in copies (pi-7-my/chk-mut-ch4-02-09/, deleted afterwards); each must be caught.",
    "--regress regenerates the model's chapters 4-02 … 4-09 in memory through make_ch4-02-09 WITH this group's\n"
    "          extensions (make_ch4-10-14 imports and extends it) and requires them identical to the files on disk.\n"
    "--mutate  plants errors in copies (pi-7-my/chk-mut-ch4-10-14/, deleted afterwards); each must be caught.")
rep("in pi-7-my/chk-pe/ch4-02-09/ (deleted).", "in pi-7-my/chk-pe/ch4-10-14/ (deleted).")
rep('''MINE = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
        "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md",
        "4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md"]''',
    '''MINE = ["4-10-dukatika-sarammanaduka.md", "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md",
        "4-13-dukatika-dassanenapahatabbaduka.md", "4-14-dukatika-saranaduka.md"]
MODEL = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
         "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md",
         "4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md"]''')
rep('''# the finished groups (identity, informational): every pi-7 chapter on disk except these and 4-01 (in progress)''',
    '''# the finished groups (identity, informational): every pi-7 chapter on disk except these and 5-01 … 5-04 (in progress)''')
rep('''if p.name[:4] not in ("4-01", "4-02", "4-03", "4-04", "4-05", "4-06", "4-07", "4-08", "4-09")''',
    '''if p.name[:4] not in ("4-10", "4-11", "4-12", "4-13", "4-14", "5-01", "5-02", "5-03", "5-04")''')
rep('''FLAGS = {a for a in _args if a in ("--mutate", "--sample", "--pe", "--groups")}''',
    '''FLAGS = {a for a in _args if a in ("--mutate", "--sample", "--pe", "--groups", "--regress")}''')
rep('''            "ekavīsa": 21, "sattārasa": 17, "dvepi": 2, "cattāripi": 4,''',
    '''            "ekavīsa": 21, "sattārasa": 17, "dvepi": 2, "cattāripi": 4, "chasu": 6, "tīsu": 3,''')
rep('''    "avigata nava": ("မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း၌ ကိုးခု", [("avigata", False)]),
}''', '''    "avigata nava": ("မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း၌ ကိုးခု", [("avigata", False)]),
    # 4-10: the heading without hyphen; «nahetuyāpi kattabbaṃ» (a locative without a count)
    "*Hetuārammaṇapaccayādi*": ("*အမြစ်ဟူသော အကြောင်းနှင့် အာရုံဟူသော အကြောင်း စသည်*",
                                [("hetu", False), ("ārammaṇa", False)]),
    "nahetuyāpi kattabbaṃ": ("အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၌လည်း ပြုရမည်", [("hetu", True)]),
}''')
rep('''           (r"(?i)nevadassanenanabhāvanāya", 2), (r"(?<=[Nn]ahetu)naārammaṇ", 1)]''',
    '''           (r"(?i)nevadassanenanabhāvanāya", 2), (r"(?<=[Nn]ahetu)naārammaṇ", 1),
           # 4-10 … 4-14 dyads: «no-X» / «na-X» terms (one «မဟုတ်» each), acetasika, «… ceva no ca X»
           (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Nn]o(?=citt|upād|kiles)", 1), (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]cetasik", 1),
           (r"(?<![\\wāīūṃṅñṭḍṇḷ])no ca (?:kiles|upādān)", 1),
           (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Nn]a(?=dassan|bhāvanāya|pītisahagat|sukhasahagat|upekkhāsahagat|kāmāvacar|rūpāvacar"
            r"|arūp)", 1)]''')
rep('''          (r"(?i)(?<![\\wāīūṃṅñṭḍṇḷ])avijjā", 1)]                # avijjā «အမှန်ကို မသိမှု» (3-03 … 3-08)''',
    '''          (r"(?i)(?<![\\wāīūṃṅñṭḍṇḷ])avijjā", 1),                # avijjā «အမှန်ကို မသိမှု» (3-03 … 3-08)
          # 4-10 … 4-14 dyads: a-terms «… မရှိ / မဖြစ် / မရောနှော / မပို့ဆောင် / အကျုံးမဝင် …»
          (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]nārammaṇ", 1), (r"(?<![\\wāīūṃṅñṭḍṇḷ])cittavisaṃsaṭṭh", 1),
          (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]nupādinn(?!upādāniy|aanupādāniy)", 1),
          (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]nupādāniy", 1), (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]saṃkilesik", 1),
          (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]saṃkiliṭṭh(?!a?a?saṃkilesik)", 1),
          (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]vitakk(?!avicār|vicāramatt)", 1), (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]vicār", 1),
          (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]ppītik", 1), (r"(?i)arūpāvacar", 1), (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]pariyāpann", 1),
          (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]niyyānik", 1), (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]nuttar", 1),
          (r"(?<![\\wāīūṃṅñṭḍṇḷ])[Aa]raṇ", 1)]''')
rep('''MA_MY = re.compile(r"မ(?:နာကျင်|သာယာ|ရှိ|ပျောက်ကွယ်|မြဲ|ရောထွေး|တွေ့ရ|ထည့်ရ|ဖြစ်|ညစ်နွမ်း|ပါဝင်|ရေးထား|ညီ|မြင်|သိ|ကျိန်းသေ)")''',
    '''MA_MY = re.compile(r"မ(?:နာကျင်|သာယာ|ရှိ|ပျောက်ကွယ်|မြဲ|ရောထွေး|တွေ့ရ|ထည့်ရ|ဖြစ်|ညစ်နွမ်း|ပါဝင်|ရေးထား|ညီ|မြင်|သိ|ကျိန်းသေ|"
                   r"ရောနှော|ပို့ဆောင်|ဝင်)")''')
# frozen tables of this group (the generator's values, compared in T)
rep('''# ----------------------------------------------------------------------------- Pāli term regexes (typed here)''',
    "# this group's dyads (frozen copy of make_ch4-10-14's values; chk-ch4-10-14/freeze.py printed them)\n"
    + frozen +
    '''DYAD_MY.update(DYAD_MY_ADD)
DUKA_MY.update(DUKA_MY_ADD)
GOC_MY.update(GOC_MY_ADD)
# triad headings in a short form (4-14)
TRIAD_MY["Micchattattikaṃ"] = TRIAD_MY["Micchattaniyatattikaṃ"]
TRIAD_MY["Sanidassanattikaṃ"] = TRIAD_MY["Sanidassanasappaṭighattikaṃ"]
TIKA_MY["Micchattattikaṃ"] = "မှားယွင်းမှု၌ ကျိန်းသေခြင်း သုံးမျိုးတွဲ"
TIKA_MY["Sanidassanattikaṃ"] = "မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ"


# ----------------------------------------------------------------------------- Pāli term regexes (typed here)''')
rep('''for _x, _s, _as, _samp in (("āsav", "sāsav", "anāsav", "āsavasampayutt"),''',
    '''for _x, _s, _as, _samp in (("āsav", "sāsav", "anāsav", "āsavasampayutt"),
                           ("upādān", "upādāniy", "anupādāniy", "upādānasampayutt"),''')
rep('''# Pāli spots the term regexes cannot see: (regex, [(dyad term index, triad stem)]) (slips and readings, logged)''',
    '''# 4-10 (3-09 dyads), 4-12 (kilesa), 4-13 / 4-14 (piṭṭhi)
for _h, _a, _b in (("Sārammaṇadukaṃ", "sārammaṇ", "anārammaṇ"), ("Cittadukaṃ", "citt", "nocitt"),
                   ("Cetasikadukaṃ", "cetasik", "acetasik"), ("Cittasampayuttadukaṃ", "cittasampayutt", "cittavippayutt"),
                   ("Cittasamuṭṭhānadukaṃ", "cittasamuṭṭhān", "nocittasamuṭṭhān"),
                   ("Cittasahabhūdukaṃ", "cittasahabh", "nocittasahabh"),
                   ("Cittānuparivattidukaṃ", "cittānuparivatt", "nocittānuparivatt"),
                   ("Cittasaṃsaṭṭhasamuṭṭhānadukaṃ", "cittasaṃsaṭṭhasamuṭṭhān", "nocittasaṃsaṭṭhasamuṭṭhān"),
                   ("Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ", "cittasaṃsaṭṭhasamuṭṭhānasahabh",
                    "nocittasaṃsaṭṭhasamuṭṭhānasahabh"),
                   ("Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ", "cittasaṃsaṭṭhasamuṭṭhānānuparivatt",
                    "nocittasaṃsaṭṭhasamuṭṭhānānuparivatt"),
                   ("Ajjhattikadukaṃ", "ajjhattik", "bāhir"), ("Upādādukaṃ", "upād", "noupād"),
                   ("Upādinnadukaṃ", "upādinn", "anupādinn"),
                   ("Kilesadukaṃ", "kiles", "nokiles"), ("Saṃkilesikadukaṃ", "saṃkilesik", "asaṃkilesik"),
                   ("Saṃkiliṭṭhadukaṃ", "saṃkiliṭṭh", "asaṃkiliṭṭh"),
                   ("Kilesasampayuttadukaṃ", "kilesasampayutt", "kilesavippayutt"),
                   ("Dassanenapahātabbadukaṃ", "dassanena pahātabb", "nadassanena pahātabb"),
                   ("Bhāvanāyapahātabbadukaṃ", "bhāvanāya pahātabb", "nabhāvanāya pahātabb"),
                   ("Dassanenapahātabbahetukadukaṃ", "dassanena pahātabbahetuk", "nadassanena pahātabbahetuk"),
                   ("Bhāvanāyapahātabbahetukadukaṃ", "bhāvanāya pahātabbahetuk", "nabhāvanāya pahātabbahetuk"),
                   ("Savitakkadukaṃ", "savitakk", "avitakk"), ("Savicāradukaṃ", "savicār", "avicār"),
                   ("Sappītikadukaṃ", "sappītik", "appītik"), ("Pītisahagatadukaṃ", "pītisahagat", "napītisahagat"),
                   ("Sukhasahagatadukaṃ", "sukhasahagat", "nasukhasahagat"),
                   ("Upekkhāsahagatadukaṃ", "upekkhāsahagat", "naupekkhāsahagat"),
                   ("Kāmāvacaradukaṃ", "kāmāvacar", "nakāmāvacar"), ("Rūpāvacaradukaṃ", "rūpāvacar", "narūpāvacar"),
                   ("Arūpāvacaradukaṃ", "arūpāvacar", "naarūpāvacar"),
                   ("Pariyāpannadukaṃ", "pariyāpann", "apariyāpann"), ("Niyyānikadukaṃ", "niyyānik", "aniyyānik"),
                   ("Niyatadukaṃ", "niyat", "aniyat"), ("Sauttaradukaṃ", "sauttar", "anuttar"),
                   ("Saraṇadukaṃ", "saraṇ", "araṇ")):
    DYAD_PI[_h] = [_ci(_a) + _W, _ci(_b) + _W]
DYAD_PI["Cittasaṃsaṭṭhadukaṃ"] = [_ci("cittasaṃsaṭṭh") + _W, _ci("cittavisaṃsaṭṭh") + _W, _ci("nocittasaṃsaṭṭh") + _W]
DYAD_PI["Kilesasaṃkilesikadukaṃ"] = [_two("kiles", "saṃkilesik"), _noca("saṃkilesik", "kiles")]
DYAD_PI["Saṃkilesasaṃkilesikadukaṃ"] = DYAD_PI["Kilesasaṃkilesikadukaṃ"]
DYAD_PI["Kilesasaṃkiliṭṭhadukaṃ"] = [_two("kiles", "saṃkiliṭṭh"), _noca("saṃkiliṭṭh", "kiles")]
DYAD_PI["Kilesakilesasampayuttadukaṃ"] = [_two("kiles", "kilesasampayutt"), _noca("kilesasampayutt", "kiles")]
DYAD_PI["Kilesavippayuttasaṃkilesikadukaṃ"] = [_ci("kilesavippayutt") + _W + " saṃkilesik" + _W,
                                               _ci("kilesavippayutt") + _W + " asaṃkilesik" + _W]
DYAD_PI["Pītisahagatādidukaṃ"] = DYAD_PI["Pītisahagatadukaṃ"] + DYAD_PI["Sukhasahagatadukaṃ"]
# Pāli spots the term regexes cannot see: (regex, [(dyad term index, triad stem)]) (slips and readings, logged)''')
rep('''PART_RE = re.compile(r"^(#{5,6}) (\\d+-\\d+\\.?) (\\S+?)duka-(\\S+?)ttikaṃ \\^")''',
    '''PART_RE = re.compile(r"^(#{5,6}) (\\d+(?:-\\d+)+\\.?) (\\S+?)duka-(\\S+?)ttikaṃ \\^")''')
rep('''    if "imesaṃ tiṇṇannaṃ" in s:                           # «imesaṃ tiṇṇannaṃ» «ဤ သုံးခုတို့၌»
        cnt.append((s.find("imesaṃ tiṇṇannaṃ"), 3))''',
    '''    if "imesaṃ tiṇṇannaṃ" in s:                           # «imesaṃ tiṇṇannaṃ» «ဤ သုံးခုတို့၌»
        cnt.append((s.find("imesaṃ tiṇṇannaṃ"), 3))
    for m in re.finditer(r"tiṇṇannaṃ (?=kabaḷīkāro|rūpajīvitindriyaṃ)", s):     # «tiṇṇannaṃ X» «သုံးခုတို့၌ X»
        cnt.append((m.start(), 3))
    for m in re.finditer(r"ekārammaṇādhipati", s):                             # «ekārammaṇādhipati» «… တစ်ခု»
        cnt.append((m.start() + 3, 1))''')
rep('''(?<!ghā)(?<!ajjha)(?<!ajjhat)(?<!mā)(?<!ka)t?tik''', '''(?<!ghā)(?<!ajjha)(?<!ajjhat)(?<!mā)(?<!ka)(?<!pī)t?tik''')
rep('''    spec = importlib.util.spec_from_file_location("make_ch4_02_09", HERE / "make_ch4-02-09.py")''',
    '''    spec = importlib.util.spec_from_file_location("make_ch4_10_14", HERE / "make_ch4-10-14.py")''')
rep('''    for w in (mk.WA, mk.WB):
        for st, my in CONDS_MY.items():''', '''    X = mk.X
    for w in (mk.WC, mk.WB, mk.WE):
        for st, my in CONDS_MY.items():''')
rep('''        if [(t, mk.dyad_value(h, t)) for _, t, _ in mk.DYAD_SURF[h]] != v:''',
    '''        if [(t, X.dyad_value(h, t)) for _, t, _ in X.DYAD_SURF[h]] != v:''')
rep('''        if mk.DUKA_NAME[h] != DUKA_MY[h]:''', '''        if X.DUKA_NAME[h] != DUKA_MY[h]:''')
rep('''        if list(mk.TRIADS[h].items()) != v or mk.TIKA_NAME[h] != TIKA_MY[h]:''',
    '''        if list(X.TRIADS[h].items()) != v or X.TIKA_NAME[h] != TIKA_MY[h]:''')
rep('''        if mk.GOC_NAME.get(g) != v:''', '''        if X.GOC_NAME.get(g) != v:''')
rep('''    for k, tab in mk.COMBO.items():''', '''    for k, tab in X.COMBO.items():''')
rep('''            dh, dt, th, tt = mk.COMBO_PALI[key]
            if val != f"{dict(DYAD_MY[dh])[dt]}၊ {dict(TRIAD_MY[th])[tt]}":''',
    '''            dh, dt, th, tt = X.COMBO_PALI[key]
            if th is None:                                    # a dyad term alone (4-13 ^7-47-59, as written)
                if val != dict(DYAD_MY[dh])[dt]:
                    bad.append(("T", "-", 0, f"dyad term alone {key}"))
                continue
            if val != f"{dict(DYAD_MY[dh])[dt]}၊ {dict(TRIAD_MY[th])[tt]}":''')
rep('''    for w in (mk.WA, mk.WB):
        wit.update(w.F.WITNESS)
    F0 = mk.WA.F''', '''    for w in (mk.WC, mk.WB, mk.WE):
        wit.update(w.F.WITNESS)
    F0 = mk.WE.F''')
rep('''    w = mk.WA
    mk.set_terms(w, {})''', '''    w = mk.X.WA
    mk.X.set_terms(w, {})''')
P.write_text(t, encoding="utf-8")
print("patched")
