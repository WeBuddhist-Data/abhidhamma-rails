"""Burmese zero-shot of pi-4 (Puggalapaññatti, «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»): 3-dukapuggalapannatti,
4-tikapuggalapannatti.

usage: python3 -I -X utf8 make_ch3-4.py [chapter ...] [--misses]
Model: make_sample.py (approved sample). Every line is generated from the Pāli by my4_formulas.translate_line()
through the frames and tables of my4_formulas.py and make_sample.py (imported: their tables are installed, nothing
is written at import, neither file is changed) and the tables of this script, which are added IN MEMORY only:
  * FIN: the FINAL pi-1 / pi-2 / pi-3 rails texts split into units (sentence / dash) aligned with their Pāli; fin()
    reads the final Burmese of an identical Pāli unit (variant brackets left out on both sides) and records it in
    REUSED (for check_ch3-4.py); fin_adj() changes it where the pi-4 Pāli differs (logged in notes-ch3-4.md);
  * QUAL: the quality nouns of the duka definitions («Tattha katamo kodho?» …), all read from FINAL;
  * EXTRA_RULES (frames of this chapter pair): «Tattha katamo X?», «ayaṃ vuccati X.», «Yassa puggalassa ayaṃ X
    (ap)pahīno», «Iminā X-ena samannāgato puggalo "Y".», the group questions «Katame dve puggalā …?» / «Tattha
    katame tayo … puggalā?», a sentence followed by an item number «… . (1)»;
  * UNIQUE3 / UNIQUE4: the sentences of the definitions (Pāli unit -> Burmese; «⟦n⟧» = n-th variant bracket);
  * BR_MY: variant brackets that my4_formulas.var_my() does not build (several readings, references, notes).
A unit no frame or table entry matches stops the run (my4_formulas.Miss); --misses lists every unmatched unit
and writes nothing. A chapter is written only when every line passed.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_sample as M  # noqa: E402  (installs the sample tables into my4_formulas; writes nothing at import)

F = M.F
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-4_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["3-dukapuggalapannatti.md", "4-tikapuggalapannatti.md"]
C, END, N, W = F.C, F.END, F.NAME, F.W
IDHA, COP, PUG, PUG_PL, CLP = F.IDHA, F.COP, F.PUGGALA, F.PUG_PL, F.CL_P

# ===================================================================================== FIN: final units of pi-1/2/3
_SPL_P = re.compile(r"( – |(?<=[.?!;])\s+(?=[A-ZĀĪŪṬḌṆÑṄṚ\"“]))")
_SPL_M = re.compile(r"( – |(?<=[။])\s+)")
_LEAD_P = re.compile(r"^\((?:Ka|Kha|Ga|Gha|Ṅa|Ca|Cha|Ja|Jha|Ña)\) ")
_LEAD_M = re.compile(r"^\([က-အ]\) ")
FIN = {}         # Pāli unit (no brackets, first letter lower) -> {Burmese unit (no brackets): [block ids]}
for _b, _k, _f, _p, _m in F.FINAL.lines():
    _pu = [x for x in _SPL_P.split(F.strip_id(_p).strip()) if x and not x.isspace()]
    _mu = [x for x in _SPL_M.split(F.strip_id(_m).strip()) if x and not x.isspace()]
    if len(_pu) != len(_mu):
        continue
    for _x, _y in zip(_pu, _mu):
        if _x == " – ":
            continue
        _x = _LEAD_P.sub("", F.novar(_x).strip())
        _y = _LEAD_M.sub("", F.novar(_y).strip())
        _x = _x[0].lower() + _x[1:]
        FIN.setdefault(_x, {}).setdefault(_y, []).append((_b, _k))
REUSED = []      # (pi-4 Pāli as used, FINAL Pāli, book, block id, Burmese as read)


def fin(p, pick=None):
    """The FINAL Burmese of the Pāli unit p (identical apart from variant brackets and the first letter's case)."""
    k = F.novar(p).strip()
    k = k[0].lower() + k[1:]
    if k not in FIN:
        raise SystemExit(f"fin: no final unit «{p[:80]}»")
    alts = FIN[k]
    if len(alts) != 1 and pick is None:
        raise SystemExit(f"fin: {len(alts)} final renderings of «{p[:60]}»: {list(alts)[:2]}")
    if pick is not None and pick.startswith("ends:"):
        ok = [a for a in alts if a.endswith(pick[5:])]
        if len(ok) != 1:
            raise SystemExit(f"fin: pick {pick} {len(ok)}x for «{p[:40]}»")
        pick = ok[0]
    my = pick if pick is not None else next(iter(alts))
    if my not in alts:
        raise SystemExit(f"fin: «{my[:40]}» not a final rendering of «{p[:40]}»")
    b, bid = alts[my][0]
    REUSED.append((p, k, b, bid, my))
    return my


def wit(pali, my):
    """Witness a reused term: the first FINAL segment (pi-1, pi-2, pi-3) whose Pāli has «pali» and Burmese «my»."""
    for b in "123":
        for k, (f, pl, ml) in F.FINAL.SEG[b].items():
            if pali.lower() in " ".join(pl).lower() and my in " ".join(ml):
                return F.witness(b, k, pali, my)
    raise SystemExit(f"wit: «{pali}» / «{my}» in no final segment")


def put(my, *anchors):
    """Insert the placeholders ⟦0⟧, ⟦1⟧ … right after the given Burmese anchors (in order of the brackets)."""
    for i, a in enumerate(anchors):
        j = my.find(a)
        if j < 0 or my.count(a) != 1:
            raise SystemExit(f"put: anchor «{a}» {my.count(a)}x")
        j += len(a)
        my = my[:j] + f" ⟦{i}⟧" + my[j:]
    return my


def nofs(s):
    return s[:-1] if s.endswith(END) else s


# ===================================================================================== variant brackets
for _t, _kd in (("dūsanā dūsitattaṃ", F.LEKHANA), ("ussuyā ussuyanā", F.LEKHANA), ("sukaṭadukkaṭānaṃ", F.LEKHANA),
                ("samaggatā", F.PATHA), ("evameva", F.LEKHANA), ("dhammassavanāya", F.LEKHANA),
                ("paṭhaviyā", F.LEKHANA), ("patiṭṭhīyati", F.LEKHANA), ("assavanoti", F.PATHA),
                ("nikujjo", F.LEKHANA), ("tilataṇḍulā", F.LEKHANA), ("… ceva", F.PATHA), ("pavattanī", F.LEKHANA),
                ("paññāpeti", F.LEKHANA), ("ehi bho", F.LEKHANA)):
    F.VAR_KIND.setdefault(_t, _kd)
F.REF.setdefault("vibha.", f"“{F.TITLE2}”")                         # Vibhaṅga = «ခွဲခြမ်းစိတ်ဖြာခြင်း» (pi-2 title)
F.REF.setdefault("ma. ni.", "“မဇ္ဈိမနိကာယ်”")                       # pi-2 ^2-760
KHUDDAKA = F.heads("Khuddakavatthuvibhaṅgo")                         # pi-2 chapter title
DUKANID = F.COLO["Dukaniddeso"]
BR_MY = {        # whole Pāli bracket -> Burmese (several readings, sutta references, editorial notes)
    "[āṭhapanā (ka.) vibha. 891]": f"[{F.LEKHANA} (Ka.): āṭhapanā{C} “{F.TITLE2}” 891]",
    "[makkhīyanā makkhīyitattaṃ (sī.), makkhiyanā makkhiyitattaṃ (ka.)]":
        f"[{F.LEKHANA} (Sī.): makkhīyanā makkhīyitattaṃ{C} (Ka.): makkhiyanā makkhiyitattaṃ]",
    "[ussuyā ussuyanā (ka.) vibha. 893]": f"[{F.LEKHANA} (Ka.): ussuyā ussuyanā{C} “{F.TITLE2}” 893]",
    "[kakkhaḷatā kakkhaḷiyaṃ (syā.) evaṃ khuddakavibhaṅgadukaniddesepi]":
        f"[{F.PATHA} (Syā.): kakkhaḷatā kakkhaḷiyaṃ{C} “{KHUDDAKA}”၏ {DUKANID}၌လည်း ဤနည်းတူ]",
    "[asaṃgāhanā apariyogāhanā (sī. syā. ka.)]": f"[{F.LEKHANA} (Sī., Syā., Ka.): asaṃgāhanā apariyogāhanā]",
    "[vipariyesaggāho (sabbattha) padasiddhi cintetabbā]":
        f"[{F.PATHA} (Sabbattha): vipariyesaggāho{C} ပုဒ်၏ ဖြစ်ပုံကို စဉ်းစားရမည်]",
    "[tappetā ca, ayaṃ vuccati puggalo titto (sī.)]": f"[{F.PATHA} (Sī.): tappetā ca, ayaṃ vuccati puggalo titto]",
    "[gato (sī.), gantvā (syā.)]": f"[{F.PATHA} (Sī.): gato{C} (Syā.): gantvā]",
    "[ehi bho (syā. ka.) ma. ni. 1.440; a. ni. 3.28]":
        f"[{F.LEKHANA} (Syā., Ka.): ehi bho{C} “မဇ္ဈိမနိကာယ်” 1.440{C} {F.REF['a. ni.']} 3.28]",
    "[kathalāya (ka.), kathalena (aṭṭhakathā) a. ni. 3.25]":
        f"[{F.LEKHANA} (Ka.): kathalāya{C} (အဋ္ဌကထာ): kathalena{C} {F.REF['a. ni.']} 3.25]",
    "[yesaṃ kho pana (sabbattha) a. ni. 3.100]": f"[{F.PATHA} (Sabbattha): yesaṃ kho pana{C} {F.REF['a. ni.']} 3.100]",
    "[patigaṇhāti (sī.) rūpasiddhiṭīkāya pana sameti]":
        f"[{F.LEKHANA} (Sī.): patigaṇhāti{C} ရူပသိဒ္ဓိ ဋီကာနှင့်ကား ညီ၏]",
}
F.witness("2", "^2-760", "ma. ni. 1.148", "“မဇ္ဈိမနိကာယ်” 1.148")
F.witness("2", "^2-754", "(sabbattha)", "(Sabbattha)")
F.witness("2", "^2-811", "aṭṭhakathā oloketabbā", "အဋ္ဌကထာကို ကြည့်ရမည်")
F.witness("2", "^2-832", "jigiṃsanatā (syā.)", "၊ (Syā.): jigiṃsanatā")
_VAR_RE2 = re.compile(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\) (?P<r>vibha\.|ma\. ni\.|a\. ni\.) (?P<n>[\d.]+)\]")
_var_orig = F.var_my


def var_my(br):
    if br in BR_MY:
        return BR_MY[br]
    m = _VAR_RE2.fullmatch(br)
    if m and m["r"] != "a. ni." and m["t"] in F.VAR_KIND:
        sig = ", ".join(F.SIGLA[s] for s in re.findall(r"[a-zāīū]+\.", m["s"]))
        return f"[{F.VAR_KIND[m['t']]} ({sig}): {m['t']}{C} {F.REF[m['r']]} {m['n']}]"
    return _var_orig(br)


F.var_my = var_my       # fill() looks it up in the module: the extended version (same output for the sample)

# ===================================================================================== duka: quality nouns (FINAL)
QUAL = {}        # Pāli quality noun (as in «Tattha katamo X?») -> Burmese, read from a final «Tattha katamo X?»
for _q in ("kodho", "upanāho", "makkho", "paḷāso", "issā", "macchariyaṃ", "sāṭheyyaṃ", "māyā", "ahirikaṃ",
           "anottappaṃ", "pāpamittatā", "indriyesu aguttadvāratā", "bhojane amattaññutā", "muṭṭhassaccaṃ",
           "asampajaññaṃ", "sīlavipatti", "diṭṭhivipatti", "hirī", "ottappaṃ", "sovacassatā", "kalyāṇamittatā",
           "indriyesu guttadvāratā", "bhojane mattaññutā", "sati", "sampajaññaṃ", "sīlasampadā", "diṭṭhisampadā"):
    _hits = [k for k in FIN if re.fullmatch(rf"tattha katam(?:o|ā|aṃ) {re.escape(_q)}\?", k)]
    if len(_hits) != 1:
        raise SystemExit(f"QUAL {_q}: {_hits}")
    _my = fin(_hits[0])
    QUAL[_q] = re.fullmatch(r"ထိုတို့အနက် (.+) ဟူသည် အဘယ်နည်း။", _my)[1]
QUAL["dovacassatā"] = re.fullmatch(r"ဤသည်ကို (.+)ဟု ခေါ်သည်။", fin("ayaṃ vuccati dovacassatā."))[1]
INSTR = {"ahirikena": "ahirikaṃ", "anottappena": "anottappaṃ", "dovacassatāya": "dovacassatā",
         "pāpamittatāya": "pāpamittatā", "indriyesu aguttadvāratāya": "indriyesu aguttadvāratā",
         "bhojane amattaññutāya": "bhojane amattaññutā", "muṭṭhassaccena": "muṭṭhassaccaṃ",
         "asampajaññena": "asampajaññaṃ", "sīlavipattiyā": "sīlavipatti", "diṭṭhivipattiyā": "diṭṭhivipatti",
         "hiriyā": "hirī", "ottappena": "ottappaṃ", "sovacassatāya": "sovacassatā",
         "kalyāṇamittatāya": "kalyāṇamittatā", "indriyesu guttadvāratāya": "indriyesu guttadvāratā",
         "bhojane mattaññutāya": "bhojane mattaññutā", "satiyā": "sati", "sampajaññena": "sampajaññaṃ",
         "sīlasampadāya": "sīlasampadā", "diṭṭhisampadāya": "diṭṭhisampadā"}
SAMANN = "နှင့် အပြည့်အဝ ပြည့်စုံသော"          # samannāgato (sample ^4-20)
NOT_YET, DONE = "ကို မပယ်ရသေး", "ကို ပယ်ပြီး ဖြစ်၏"   # appahīno / pahīno (sample ^4-9, ^4-41)
UDDHAM = F.witness("2", "^2-17-6-2-0", "Pañcuddhambhāgiyāni saṃyojanāni", "အထက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး ငါးပါး")
GROUP_Q = f" ဟူသည် အဘယ် {PUG_PL}နည်း{END}"   # Katame … puggalā? (plural of the sample's «ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း။»)


def _tattha(m):
    q = m["n"]
    if q in QUAL:
        return f"ထိုတို့အနက် {QUAL[q]} ဟူသည် အဘယ်နည်း{END}"
    g = re.fullmatch(r"(?P<a>aparepi )?(?P<n>tayo) (?P<g>\S+) puggalā", q)
    if g and g["g"] in F.GROUP:
        return f"ထိုတို့အနက် {F.GROUP[g['g']]} {PUG} {F.persons(3)}{GROUP_Q}"
    g = re.fullmatch(r"(?P<a>aparepi )?tayo satthāro", q)
    if g:
        return f"ထိုတို့အနက် {'နောက်ထပ် ' if g['a'] else ''}ဆရာ {F.persons(3)} ဟူသည် အဘယ် ဆရာတို့နည်း{END}"
    return None


def _vucc_q(m):
    q = m["n"]
    return f"ဤသည်ကို {QUAL[q]}ဟု ခေါ်သည်{END}" if q in QUAL else None


def _yassa(m):
    q = m["n"]
    if q not in QUAL:
        return None
    return f"အကြင် {PUG}၏ ဤ{QUAL[q]}" + (NOT_YET if m["a"] else DONE)


def _imina(m):
    q = INSTR.get(m["n"])
    if not q:
        return None
    return f"ဤ{QUAL[q]}{SAMANN} {PUG}သည် “{F.name(m['p'])}” ဖြစ်သည်{END}"


def _group_q(m):          # «Katame dve puggalā dullabhā lokasmiṃ?» (the mātikā group names, sample GROUP_POST)
    g = m["g"]
    if g not in F.GROUP_POST:
        return None
    return f"{F.GROUP_POST[g]} {PUG} {F.persons(2)}{GROUP_Q}"


def _excl(m):             # «…"ti! Tasmā …»: an exclamation ends a sentence as «.» does (one «။»)
    return f"{F.unit_my(m['a'])} {F.unit_my(m['b'])}"


def _num_tail(m):         # «… ābādhā. (1)»: the item number stays after the sentence
    return f"{F.unit_my(m['s'])} ({m['n']})"


F.EXTRA_RULES += [
    (re.compile(r"[Tt]attha katam(?:o|ā|aṃ|e) (?P<n>.+)\?"), _tattha),
    (re.compile(r"(?:ayaṃ|idaṃ) vuccati (?P<n>[^\"]+)\."), _vucc_q),
    (re.compile(r"Yassa puggalassa (?:ayaṃ|idaṃ) (?P<n>\S+) (?P<a>ap)?pahīn(?:o|ā|aṃ)"), _yassa),
    (re.compile(r"(?:Iminā|Imāya) (?P<n>.+?) samannāgato puggalo \"(?P<p>[^\"]+)\"\."), _imina),
    (re.compile(r"Katame dve puggalā (?P<g>.+)\?"), _group_q),
    (re.compile(r"(?P<s>.+[.?]) \((?P<n>\d+)\)"), _num_tail),
    (re.compile(r"(?P<a>[^!]+!) (?P<b>[A-ZĀĪŪṬḌṆÑṄṚ].+)"), _excl),
]

# ===================================================================================== ch3: sentences
KODHA_LIST = fin("Yo kodho kujjhanā kujjhitattaṃ doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ "
                 "virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa")
_KODHA_P = ("Yo kodho kujjhanā kujjhitattaṃ doso dussanā dussitattaṃ{} byāpatti byāpajjanā byāpajjitattaṃ "
            "virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa")
PUBBA = nofs(fin("Pubbakālaṃ kodho, aparakālaṃ upanāho."))       # pi-2 ^2-891 (pi-4 without the comma)
UPANAHA_P = ("Yo evarūpo upanāho upanayhanā upanayhitattaṃ aṭṭhapanā{} ṭhapanā saṇṭhapanā anusaṃsandanā "
             "anuppabandhanā daḷhīkammaṃ kodhassa")
UPANAHA_LIST = fin(UPANAHA_P.format(""))
MAKKHA_P = "Yo makkho makkhāyanā makkhāyitattaṃ{} niṭṭhuriyaṃ niṭṭhuriyakammaṃ"
MAKKHA_LIST = fin(MAKKHA_P.format(""))
_PALASA_FIN = fin("Yo paḷāso paḷāsāyanā paḷāsāhāro vivādaṭṭhānaṃ yugaggāho appaṭinissaggo")
PALASA_LIST = _PALASA_FIN.replace("တုပြိုင်ခြင်း၊ ", "တုပြိုင်ခြင်း၊ တုပြိုင်ထားသော အဖြစ်၊ ", 1)  # + paḷāsāyitattaṃ
ISSA_P = ("Yā paralābhasakkāragarukāramānanavandanapūjanāsu issā issāyanā issāyitattaṃ usūyā usūyanā{} "
          "usūyitattaṃ")
ISSA_LIST = fin(ISSA_P.format(""), "ends:ရှိသမျှ")
MACCH_LIST = fin("Yaṃ evarūpaṃ maccheraṃ maccharāyanā maccharāyitattaṃ vevicchaṃ kadariyaṃ kaṭukañcukatā "
                 "aggahitattaṃ cittassa")
SATHA_LIST = fin("Yaṃ tattha saṭhaṃ saṭhatā sāṭheyyaṃ kakkaratā kakkariyaṃ parikkhattatā pārikkhattiyaṃ")
MAYA_LIST = fin("Yā evarūpā māyā māyāvitā accāsarā vañcanā nikati vikiraṇā pariharaṇā gūhanā parigūhanā chādanā "
                "paṭicchādanā anuttānīkammaṃ anāvikammaṃ vocchādanā pāpakiriyā")
_MAYA1 = nofs(fin("Idhekacco kāyena duccaritaṃ caritvā, vācāya duccaritaṃ caritvā, manasā duccaritaṃ caritvā tassa "
                  "paṭicchādanahetuṃ pāpikaṃ icchaṃ paṇidahati."))
_IDHA_SU = "ဤလောက၌ အချို့သော သူသည်"                  # «Idhekacco» without «puggalo» (pi-1 / pi-2)
assert _MAYA1.startswith(_IDHA_SU)
_MJ = [nofs(fin(f'"Mā maṃ jaññā"ti {v}.')) for v in ("icchati", "saṅkappeti", "vācaṃ bhāsati", "kāyena parakkamati")]
MAYA_Q = f"{C} ".join(_MJ) + END                     # the four «"mā maṃ jaññā"ti …» (pi-2 ^2-894), joined
HIRI_NEG = fin("Yaṃ na hirīyati hiriyitabbena, na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā")
HIRI_POS = fin("Yaṃ hirīyati hiriyitabbena, hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā")
OTT_POS = fin("Yaṃ ottappati ottappitabbena, ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā")
_DOVA = fin("Sahadhammike vuccamāne dovacassāyaṃ dovacassiyaṃ dovacassatā vippaṭikūlaggāhitā vipaccanīkasātatā "
            "anādariyaṃ anādaratā agāravatā appaṭissavatā")
_SOVA = fin("Sahadhammike vuccamāne sovacassāyaṃ sovacassiyaṃ sovacassatā appaṭikūlaggāhitā avipaccanīkasātatā "
            "sagāravatā sādariyaṃ sādaratā sappaṭissavatā")
_sv = _SOVA.split(f"{C} ")             # pi-4 order: … avipaccanīkasātatā sādariyaṃ sādariyatā sagāravatā sappatissavatā
assert len(_sv) == 9 and _sv[5] == "ရိုသေမှု ရှိခြင်း"
SOVA = f"{C} ".join(_sv[:5] + [_sv[6], _sv[7], _sv[5], _sv[8]])
KALYANAM = fin("Ye te puggalā saddhā sīlavanto bahussutā cāgavanto paññavanto, yā tesaṃ sevanā nisevanā saṃsevanā "
               "bhajanā sambhajanā bhatti sambhatti taṃsampavaṅkatā").replace("ထိုသူတို့ဘက်သို့ ညွတ်ကိုင်းခြင်း",
                                                                             "ညွတ်ကိုင်းခြင်း")
assert fin("Ye te puggalā assaddhā dussīlā appassutā maccharino duppaññā, yā tesaṃ sevanā nisevanā saṃsevanā "
           "bhajanā sambhajanā bhatti sambhatti sampavaṅkatā").endswith(f"{C} ညွတ်ကိုင်းခြင်း ရှိသမျှ")


def _idha(my):
    """A final sentence of «Idhekacco …» (pi-1 / pi-2 «ဤလောက၌ အချို့သော သူသည်») -> «Idhekacco puggalo …»."""
    assert my.startswith(_IDHA_SU), my[:30]
    return IDHA + my[len(_IDHA_SU):]


_CAK_NEG = nofs(fin("Idhekacco cakkhunā rūpaṃ disvā nimittaggāhī hoti anubyañjanaggāhī."))
_CAK_POS = nofs(fin("Idhekacco cakkhunā rūpaṃ disvā na nimittaggāhī hoti na anubyañjanaggāhī."))
_YAT = {}
for _s in ("cakkhund", "manind"):
    for _n in ("na ", ""):
        _YAT[(_s, _n)] = nofs(fin(f"Yatvādhikaraṇamenaṃ {_s}riyaṃ asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā "
                                  f"akusalā dhammā anvāssaveyyuṃ, tassa saṃvarāya {_n}paṭipajjati, {_n}rakkhati "
                                  f"{_s}riyaṃ, {_s}riye {_n}saṃvaraṃ āpajjati."))
_SOT_NEG = nofs(fin("Sotena saddaṃ sutvā…pe… ghānena gandhaṃ ghāyitvā…pe… jivhāya rasaṃ sāyitvā…pe… kāyena "
                    "phoṭṭhabbaṃ phusitvā…pe… manasā dhammaṃ viññāya nimittaggāhī hoti anubyañjanaggāhī."))
_SOT_POS = nofs(fin("Sotena saddaṃ sutvā…pe… ghānena gandhaṃ ghāyitvā…pe… jivhāya rasaṃ sāyitvā…pe… kāyena "
                    "phoṭṭhabbaṃ phusitvā…pe… manasā dhammaṃ viññāya na nimittaggāhī hoti nānubyañjanaggāhī."))
_BHOJ_NEG = nofs(fin("Idhekacco appaṭisaṅkhā ayoniso āhāraṃ āhāreti davāya madāya maṇḍanāya vibhūsanāya."))
_BHOJ_NEG2 = fin("Yā tattha asantuṭṭhitā amattaññutā appaṭisaṅkhā bhojane")
_f1355 = F.FINAL.seg("1", "^1-1355")[2][0]
_BH_ALL = re.search(r"ဤလောက၌ အချို့သော သူသည် (.+?) – (.+?)ဟူ၍။", _f1355)
assert _BH_ALL
_BH_EAT = _BH_ALL[1]                                   # «ပြန်လည် ဆင်ခြင်၍ သင့်လျော်စွာ အစာကို စားသုံး၏»
_BH_Q = _BH_ALL[2]
_BH_Q1, _BH_Q2 = _BH_Q.split("ဖြစ်၏၊ ဤသို့ ")       # pi-1 one sentence; pi-4 two («… brahmacariyānuggahāya. Iti …»)
REUSED.append(("Idhekacco puggalo paṭisaṅkhā yoniso āhāraṃ āhāreti – neva davāya … phāsuvihāro cā\"ti",
               "idhekacco paṭisaṅkhā yoniso āhāraṃ āhāreti – neva davāya …", "1", "^1-1355", _BH_ALL[0]))
_BHOJ_POS2 = fin("Yā tattha santuṭṭhitā mattaññutā paṭisaṅkhā bhojane")
SATI_LIST = fin("Yā sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammusanatā sati satindriyaṃ "
                "satibalaṃ sammāsati")
MUTTHA_LIST = fin("Yā assati ananussati appaṭissati assati assaraṇatā adhāraṇatā pilāpanatā sammusanatā")
MOHA_P = ("Yaṃ aññāṇaṃ adassanaṃ anabhisamayo ananubodho asambodho appaṭivedho asaṅgāhaṇā apariyogāhaṇā{} "
          "asamapekkhaṇā apaccavekkhaṇā apaccakkhakammaṃ dummejjhaṃ bālyaṃ asampajaññaṃ moho pamoho sammoho avijjā "
          "avijjogho avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ avijjālaṅgī moho akusalamūlaṃ")
MOHA_LIST = fin(MOHA_P.format("").replace("asamapekkhaṇā", "asamapekkhanā"))      # pi-2 ^2-180 (spelling)
_PANNA = fin("Yā tasmiṃ samaye paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā "
             "paccupalakkhaṇā paṇḍiccaṃ kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā "
             "sampajaññaṃ patodo paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso "
             "paññāpajjoto paññāratanaṃ amoho dhammavicayo sammādiṭṭhi")
assert _PANNA.startswith("ထိုအချိန်၌ ")
PANNA_LIST = _PANNA[len("ထိုအချိန်၌ "):]                # pi-1 ^1-16 without «yā tasmiṃ samaye»
VITI_NEG = fin("Kāyiko vītikkamo vācasiko vītikkamo kāyikavācasiko vītikkamo")
VITI_POS = fin("Kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo")
_f1369 = F.FINAL.seg("1", "^1-1369")[2][0]
_f1371 = F.FINAL.seg("1", "^1-1371")[2][0]
_NATTHI = re.search(r"အဘယ်နည်း။ (.+?)ဟူ၍၊ ဤသို့ သဘောရှိသော အယူ", _f1369)[1]
_ATTHI = re.search(r"အဘယ်နည်း။ (.+?)ဟူ၍၊ ဤသို့ သဘောရှိသော ပညာ", _f1371)[1]
REUSED.append(('"Natthi dinnaṃ, … pavedentī"ti', "natthi dinnaṃ … pavedentīti", "1", "^1-1369", _NATTHI))
REUSED.append(('"Atthi dinnaṃ, … pavedentī"ti', "atthi dinnaṃ … pavedentīti", "1", "^1-1371", _ATTHI))
_NATTHI_B = put(_NATTHI, "ဆိုးစွာ ပြုသော ကံတို့၏", "မှန်ကန်စွာ ရောက်ရှိသော")
DITTHI_LIST = fin("yā evarūpā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ "
                  "diṭṭhisaṃyojanaṃ gāho patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ "
                  "titthāyatanaṃ vipariyāsaggāho")
_PATIGG = "လက်ခံ စွဲကိုင်ခြင်း"            # paṭiggāho (pi-4; pi-1 has patiṭṭhāho «ခိုင်မြဲစွာ စွဲကိုင်ခြင်း» here)
DITTHI_LIST4 = DITTHI_LIST.replace("ခိုင်မြဲစွာ စွဲကိုင်ခြင်း", _PATIGG, 1)
PANNA_PE = re.search(r"ဟူ၍၊ (ဤသို့ သဘောရှိသော ပညာ၊ .+? ရှိသမျှ) – ", _f1371)[1]
REUSED.append(("Yā evarūpā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi",
               "yā evarūpā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi", "1", "^1-1371", PANNA_PE))

# the duka groups (^4-83 … ^4-87), dullabha / titto (new)
KUKK = "နောင်တ ပူပန်"                                     # kukkucca (pi-1 «နောင်တ ပူပန်မှု»)
KUKK_NO = "နောင်တ မပူပန်"                                  # na kukkuccāyati (negation before a verb = «မ»)
F.witness("1", "^1-1166", "kukkuccaṃ kukkuccāyanā", "နောင်တ ပူပန်ခြင်း")
LADDHA = "ရတိုင်း ရတိုင်းကို"                               # laddhaṃ laddhaṃ
HOARD, GIVE = "သိုမှီးထား", "စွန့်ကြဲ"                       # nikkhipati / vissajjeti
SEVATI3 = f"ပေါင်းသင်း၏{C} ဆည်းကပ်၏{C} ချဉ်းကပ် ခစား၏"      # sevati bhajati payirupāsati (sevitabbo = «ပေါင်းသင်းအပ်»)
DUSS, PAPAD = "သီလ ပျက်သူ", N["pāpadhammo"]                 # dussīlo (pi-2 ^2-851), pāpadhammo (catukka name)
SILAVA, KALD = "သီလ ရှိသူ", N["kalyāṇadhammo"]              # sīlavā (pi-2 ^2-851), kalyāṇadhammo
F.witness("2", "^2-851", "dussīlo samāno", "သီလ ပျက်သူ ဖြစ်လျက်")
F.witness("2", "^2-851", "sīlavāti", "သီလ ရှိသူဟု")
DUSS_HOTI = f"{DUSS} {COP}{C} {PAPAD} {COP}"                   # dussīlo hoti pāpadhammo
SIL_HOTI = f"{SILAVA} {COP}{C} {KALD} {COP}"                   # sīlavā hoti kalyāṇadhammo
SAVAKA = "တပည့်"                                              # sāvaka (pi-2, sample)

UNIQUE3 = {
    # ^4-45 … ^4-52 the vices (lists of pi-2 Khuddakavatthu / pi-1)
    _KODHA_P.format(" [dūsanā dūsitattaṃ (syā.)]"): put(KODHA_LIST, "စိတ်ဆိုးထားသော အဖြစ်"),
    _KODHA_P.format(""): KODHA_LIST,
    "Pubbakālaṃ kodho aparakālaṃ upanāho.": PUBBA + END,
    UPANAHA_P.format(" [āṭhapanā (ka.) vibha. 891]"): put(UPANAHA_LIST, "ခိုင်ခိုင်မြဲမြဲ တည်ထားခြင်း"),
    "Pubbakālaṃ kodho aparakālaṃ upanāho " + UPANAHA_P.format("")[0].lower() + UPANAHA_P.format("")[1:]:
        f"{PUBBA}{C} {UPANAHA_LIST}",                    # ^4-66 (no full stop after «upanāho»: source slip)
    MAKKHA_P.format(" [makkhīyanā makkhīyitattaṃ (sī.), makkhiyanā makkhiyitattaṃ (ka.)]"):
        put(MAKKHA_LIST, "ကျေးဇူး ချေဖျက်ထားသော အဖြစ်"),
    MAKKHA_P.format(""): MAKKHA_LIST,
    "Yo paḷāso paḷāsāyanā paḷāsāyitattaṃ paḷāsāhāro vivādaṭṭhānaṃ yugaggāho appaṭinissaggo": PALASA_LIST,
    ISSA_P.format(" [ussuyā ussuyanā (ka.) vibha. 893]"): put(ISSA_LIST, "သဝန်တိုခြင်း"),
    ISSA_P.format(""): ISSA_LIST,
    "Yaṃ tattha saṭhaṃ saṭhatā sāṭheyyaṃ kakkaratā kakkariyaṃ [kakkhaḷatā kakkhaḷiyaṃ (syā.) evaṃ "
    "khuddakavibhaṅgadukaniddesepi] parikkhattattā pārikkhattiyaṃ": put(SATHA_LIST, "ကောက်ကွေးသော အဖြစ်"),
    "Idhekacco kāyena duccaritaṃ caritvā vācāya duccaritaṃ caritvā manasā duccaritaṃ caritvā tassa "
    "paṭicchādanahetu pāpikaṃ icchaṃ paṇidahati": _MAYA1,
    "Idhekacco puggalo kāyena duccaritaṃ caritvā vācāya duccaritaṃ caritvā manasā duccaritaṃ caritvā tassa "
    "paṭicchādanahetu pāpikaṃ icchaṃ paṇidahati": _idha(_MAYA1),
    '"mā maṃ jaññā"ti icchati, "mā maṃ jaññā"ti saṅkappati "mā maṃ jaññā"ti vācaṃ bhāsati, "mā maṃ jaññā"ti '
    'kāyena parakkamati.': MAYA_Q,
    '"mā maṃ jaññā"ti icchati, "mā maṃ jaññā"ti saṅkappati, "mā maṃ jaññā"ti vācaṃ bhāsati, "mā maṃ jaññā"ti '
    'kāyena parakkamati.': MAYA_Q,
    # ^4-53 … ^4-62 (pi-1 Suttantika dukas)
    "Yaṃ na hirīyati hiriyitabbena na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": HIRI_NEG,
    "Yaṃ hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": HIRI_POS,
    "Yaṃ ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": OTT_POS,
    "Tattha katamo dovacassatā?": f"ထိုတို့အနက် {QUAL['dovacassatā']} ဟူသည် အဘယ်နည်း{END}",   # katamo: slip
    "Sahadhammike vuccamāne dovacassāyaṃ dovacassiyaṃ dovacassatā vippaṭikulaggāhitā vipaccanīkasātatā anādariyaṃ "
    "anādariyatā agāravatā appatissavatā": _DOVA,
    "Sahadhammike vuccamāne sovacassāyaṃ sovacassiyaṃ sovacassatā avippaṭikulaggāhitā avipaccanīkasātatā sādariyaṃ "
    "sādariyatā sagāravatā sappatissavatā": SOVA,
    "Ye te puggalā saddhā sīlavanto bahussutā cāgavanto paññavanto, yā tesaṃ sevanā nisevanā saṃsevanā bhajanā "
    "sambhajanā bhatti sambhatti sampavaṅkatā": KALYANAM,
    "Idhekacco puggalo cakkhunā rūpaṃ disvā nimittaggāhī hoti anubyañjanaggāhī; yatvādhikaraṇamenaṃ cakkhundriyaṃ "
    "asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā anvāssaveyyuṃ, tassa saṃvarāya na paṭipajjati, "
    "na rakkhati cakkhundriyaṃ, cakkhundriye na saṃvaraṃ āpajjati.":
        f"{_idha(_CAK_NEG)}{C} {_YAT[('cakkhund', 'na ')]}{END}",
    "Sotena saddaṃ sutvā…pe… ghānena gandhaṃ ghāyitvā…pe… jivhāya rasaṃ sāyitvā…pe… kāyena phoṭṭhabbaṃ "
    "phusitvā…pe… manasā dhammaṃ viññāya nimittaggāhī hoti anubyañjanaggāhī; yatvādhikaraṇamenaṃ manindriyaṃ "
    "asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā anvāssaveyyuṃ, tassa saṃvarāya na paṭipajjati, "
    "na rakkhati manindriyaṃ, manindriye na saṃvaraṃ āpajjati.":
        f"{_SOT_NEG}{C} {_YAT[('manind', 'na ')]}{END}",
    "Idhekacco puggalo cakkhunā rūpaṃ disvā na nimittaggāhī hoti nānubyañjanaggāhī; yatvādhikaraṇamenaṃ "
    "cakkhundriyaṃ asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā anvāssaveyyuṃ, tassa saṃvarāya "
    "paṭipajjati, rakkhati cakkhundriyaṃ cakkhundriye saṃvaraṃ āpajjati.":
        f"{_idha(_CAK_POS)}{C} {_YAT[('cakkhund', '')]}{END}",
    "Sotena saddaṃ sutvā…pe… ghānena gandhaṃ ghāyitvā…pe… jivhāya rasaṃ sāyitvā…pe… kāyena phoṭṭhabbaṃ "
    "phusitvā…pe… manasā dhammaṃ viññāya na nimittaggāhī hoti nānubyañjanaggāhī; yatvādhikaraṇamenaṃ manindriyaṃ "
    "asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā anvāssaveyyuṃ, tassa saṃvarāya paṭipajjati, "
    "rakkhati manindriyaṃ, manindriye saṃvaraṃ āpajjati.":
        f"{_SOT_POS}{C} {_YAT[('manind', '')]}{END}",
    "Idhekacco puggalo appaṭisaṅkhā ayoniso āhāraṃ āhāreti davāya madāya maṇḍanāya vibhūsanāya, yā tattha "
    "asantuṭṭhitā amattaññutā appaṭisaṅkhā bhojane": f"{_idha(_BHOJ_NEG)}{C} {_BHOJ_NEG2}",
    "Idhekacco puggalo paṭisaṅkhā yoniso āhāraṃ āhāreti": f"{IDHA} {_BH_EAT}",
    '"neva davāya, na madāya, na maṇḍanāya, na vibhūsanāya; yāvadeva imassa kāyassa ṭhitiyā yāpanāya '
    'vihiṃsūparatiyā brahmacariyānuggahāya.': f"“{_BH_Q1}ဖြစ်၏{END}",
    'Iti purāṇañca vedanaṃ paṭihaṅkhāmi, navañca vedanaṃ na uppādessāmi, yātrā ca me bhavissati anavajjatā ca '
    'phāsuvihāro cā"ti.': f"ဤသို့ {_BH_Q2}”ဟူ၍{END}",
    "Yā tattha santuṭṭhitā mattaññutā paṭisaṅkhā bhojane": _BHOJ_POS2,
    "Yā assati ananussati appaṭissati assati assaraṇatā adhāraṇatā pilāpanatā sammusanatā": MUTTHA_LIST,
    "Yā sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammusanatā sati satindriyaṃ satibalaṃ "
    "sammāsati": SATI_LIST,
    MOHA_P.format(" [asaṃgāhanā apariyogāhanā (sī. syā. ka.)]"): put(MOHA_LIST, "နက်နက်နဲနဲ မသက်ဝင်နိုင်ခြင်း"),
    "Yā paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
    "nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā paññindriyaṃ "
    "paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ amoho dhammavicayo "
    "sammādiṭṭhi": PANNA_LIST,
    "Kāyiko vītikkamo vācasiko vītikkamo kāyikavācasiko vītikkamo": VITI_NEG,
    "Kāyiko avītikkamo vācasiko avītikkamo kāyikavācasiko avītikkamo": VITI_POS,
    '"Natthi dinnaṃ, natthi yiṭṭhaṃ, natthi hutaṃ, natthi sukatadukkaṭānaṃ [sukaṭadukkaṭānaṃ (sī.)] kammānaṃ '
    'phalaṃ vipāko, natthi ayaṃ loko, natthi paro loko, natthi mātā, natthi pitā, natthi sattā opapātikā, natthi '
    'loke samaṇabrāhmaṇā sammaggatā [samaggatā (ka.)] sammāpaṭipannā ye imañca lokaṃ parañca lokaṃ sayaṃ abhiññā '
    'sacchikatvā pavedentī"ti.': f"“{_NATTHI_B}”ဟူ၍{END}",
    '"Atthi dinnaṃ, atthi yiṭṭhaṃ, atthi hutaṃ, atthi sukatadukkaṭānaṃ kammānaṃ phalaṃ vipāko, atthi ayaṃ loko, '
    'atthi paro loko, atthi mātā, atthi pitā, atthi sattā opapātikā, atthi loke samaṇabrāhmaṇā sammaggatā '
    'sammāpaṭipannā ye imañca lokaṃ parañca lokaṃ sayaṃ abhiññā sacchikatvā pavedentī"ti.': f"“{_ATTHI}”ဟူ၍{END}",
    "Yā evarūpā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ "
    "diṭṭhisaṃyojanaṃ gāho paṭiggāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ "
    "vipariyāsaggāho [vipariyesaggāho (sabbattha) padasiddhi cintetabbā], ayaṃ vuccati diṭṭhivipatti.":
        put(DITTHI_LIST4, "ပြောင်းပြန် စွဲကိုင်ခြင်း") + f"{C} ဤသည်ကို {QUAL['diṭṭhivipatti']}ဟု ခေါ်သည်{END}",
    "Yā evarūpā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": PANNA_PE,
    # ^4-63, ^4-64
    "Yassa puggalassa pañcorambhāgiyāni saṃyojanāni appahīnāni": f"အကြင် {PUG}၏ {W['orambhagiya']}{NOT_YET}",
    "Yassa puggalassa pañcuddhambhāgiyāni saṃyojanāni appahīnāni": f"အကြင် {PUG}၏ {UDDHAM}{NOT_YET}",
    "Katamo ca pugalo amaccharī?": N["amaccharī"] + F.Q_TAIL,       # «pugalo»: source slip
    # ^4-83 … ^4-87
    "Yo ca pubbakārī, yo ca kataññū katavedī": "ရှေးဦးစွာ ကျေးဇူးပြုသူနှင့် ကျေးဇူးကို သိ၍ ကျေးဇူးကို ဆပ်သူ",
    "ime dve puggalā dullabhā lokasmiṃ.": f"ဤ{PUG} {F.persons(2)}တို့သည် လောက၌ ရခဲကုန်၏{END}",
    f"Yo ca {LADDHA}": None,
    "Yo ca laddhaṃ laddhaṃ nikkhipati, yo ca laddhaṃ laddhaṃ vissajjeti":
        f"{LADDHA} {HOARD}သူနှင့် {LADDHA} {GIVE}သူ",
    'ime dve puggalā "duttappayā".': f"ဤ{PUG} {F.persons(2)}တို့ကို “{F.GROUP_POST['duttappayā']} {PUG}”ဟု ခေါ်သည်{END}",
    "Yo ca laddhaṃ laddhaṃ na nikkhipati, yo ca laddhaṃ laddhaṃ na vissajjeti":
        f"{LADDHA} မ{HOARD}သူနှင့် {LADDHA} မ{GIVE}သူ",
    'ime dve puggalā "sutappayā".': f"ဤ{PUG} {F.persons(2)}တို့ကို “{F.GROUP_POST['sutappayā']} {PUG}”ဟု ခေါ်သည်{END}",
    "Katamesaṃ dvinnaṃ puggalānaṃ āsavā vaḍḍhanti?":
        f"အဘယ် {PUG} {F.persons(2)}တို့၏ {W['asava']}တို့သည် တိုးပွားကုန်သနည်း{END}",
    "Yo ca na kukkuccāyitabbaṃ kukkuccāyati, yo ca kukkuccāyitabbaṃ na kukkuccāyati":
        f"{KUKK}ရန် မထိုက်သည်ကို {KUKK}သူနှင့် {KUKK}ရန် ထိုက်သည်ကို {KUKK_NO}သူ",
    "imesaṃ dvinnaṃ puggalānaṃ āsavā vaḍḍhanti.": f"ဤ{PUG} {F.persons(2)}တို့၏ {W['asava']}တို့သည် တိုးပွားကုန်၏{END}",
    "Katamesaṃ dvinnaṃ puggalānaṃ āsavā na vaḍḍhanti?":
        f"အဘယ် {PUG} {F.persons(2)}တို့၏ {W['asava']}တို့သည် မတိုးပွားကုန်သနည်း{END}",
    "Yo ca na kukkuccāyitabbaṃ na kukkuccāyati, yo ca kukkuccāyitabbaṃ kukkuccāyati":
        f"{KUKK}ရန် မထိုက်သည်ကို {KUKK_NO}သူနှင့် {KUKK}ရန် ထိုက်သည်ကို {KUKK}သူ",
    "imesaṃ dvinnaṃ puggalānaṃ āsavā na vaḍḍhanti.":
        f"ဤ{PUG} {F.persons(2)}တို့၏ {W['asava']}တို့သည် မတိုးပွားကုန်{END}",
    # ^4-88 … ^4-90
    "Idhekacco puggalo dussīlo hoti pāpadhammo, so aññaṃ dussīlaṃ pāpadhammaṃ sevati bhajati payirupāsati":
        f"{IDHA} {DUSS_HOTI}{C} ထိုသူသည် သီလ ပျက်သော၊ ယုတ်မာသော သဘော ရှိသော အခြားသူကို {SEVATI3}",
    "Idhekacco puggalo sīlavā hoti kalyāṇadhammo, so aññaṃ sīlavantaṃ kalyāṇadhammaṃ sevati bhajati payirupāsati":
        f"{IDHA} {SIL_HOTI}{C} ထိုသူသည် သီလ ရှိသော၊ ကောင်းမွန်သော သဘော ရှိသော အခြားသူကို {SEVATI3}",
    "Paccekasambuddhā [paccekabuddho (sī.)] ye ca tathāgatassa sāvakā arahanto tittā.":
        f"{N['paccekasambuddho']}တို့ ⟦0⟧နှင့် {W['tathagata']}၏ {W['araha']} {SAVAKA}တို့သည် "
        f"{N['titto']} ဖြစ်ကြ၏{END}",
    "Sammāsambuddho titto ca tappetā ca [tappetā ca, ayaṃ vuccati puggalo titto (sī.)].":
        f"{W['sammasambuddha']}သည် {N['titto']}လည်း {COP}{C} {N['tappetā']}လည်း {COP} ⟦0⟧{END}",
}
del UNIQUE3[f"Yo ca {LADDHA}"]
FIN_UNITS = [    # pi-4 units identical with a FINAL unit (pi-1 / pi-2): the final Burmese verbatim
    "Pañca macchariyāni",
    "āvāsamacchariyaṃ, kulamacchariyaṃ, lābhamacchariyaṃ, vaṇṇamacchariyaṃ, dhammamacchariyaṃ.",
    "Idhekacco saṭho hoti parisaṭho.",
    "Yaṃ na ottappati ottappitabbena na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā",
    "Ye te puggalā assaddhā dussīlā appassutā maccharino duppaññā, yā tesaṃ sevanā nisevanā saṃsevanā bhajanā "
    "sambhajanā bhatti sambhatti sampavaṅkatā",
    "Yā imesaṃ channaṃ indriyānaṃ agutti agopanā anārakkho asaṃvaro",
    "Yā imesaṃ channaṃ indriyānaṃ gutti gopanā ārakkho saṃvaro",
    "Sabbampi dussilyaṃ sīlavipatti.", "Sabbāpi micchādiṭṭhi diṭṭhivipatti.",
    "Sabbopi sīlasaṃvaro sīlasampadā.", "Sabbāpi sammādiṭṭhi diṭṭhisampadā.",
]
for _u in FIN_UNITS:
    UNIQUE3[_u] = fin(_u)
UNIQUE3["Yaṃ evarūpaṃ maccheraṃ maccharāyanā maccharāyitattaṃ vevicchaṃ kadariyaṃ kaṭukañcukatā aggahitattaṃ "
        "cittassa"] = MACCH_LIST
UNIQUE3["Yaṃ tattha saṭhaṃ saṭhatā sāṭheyyaṃ kakkaratā kakkariyaṃ parikkhattatā pārikkhattiyaṃ"] = SATHA_LIST
UNIQUE3["Yā evarūpā māyā māyāvitā accāsarā vañcanā nikati vikiraṇā pariharaṇā gūhanā parigūhanā chādanā "
        "paṭicchādanā anuttānīkammaṃ anāvikammaṃ vocchādanā pāpakiriyā"] = MAYA_LIST
assert "⟦0⟧" in UNIQUE3[ISSA_P.format(" [ussuyā ussuyanā (ka.) vibha. 893]")]

# ===================================================================================== ch4: sentences
# ---- shared phrases of ch4 (new unless marked)
_f831 = F.FINAL.seg("2", "^2-831")[2][0]
AK = re.search(r"မြတ်စွာဘုရားသည် (.+?) နေတော်မူ၏။", _f831)[1]       # āsavānaṃ khayā … upasampajja (pi-2 ^2-831)
REUSED.append(("āsavānaṃ khayā anāsavaṃ cetovimuttiṃ paññāvimuttiṃ diṭṭheva dhamme sayaṃ abhiññā sacchikatvā "
               "upasampajja", "āsavānaṃ khayā … upasampajja viharatīti", "2", "^2-831", AK))
AK_P = ("āsavānaṃ khayā anāsavaṃ cetovimuttiṃ paññāvimuttiṃ diṭṭheva dhamme sayaṃ abhiññā sacchikatvā "
        "upasampajja")
VIHARATI = "နေ၏"
SUNATI = f"ထိုသူသည် ကြားရ၏"                                          # So suṇāti
HEARD = f"“ဤမည်သော ရဟန်းသည် {AK} နေသတတ်”ဟု{END}"                 # "itthannāmo kira bhikkhu … viharatī"ti.
HOPE = f"“ငါသည်လည်း အဘယ်အခါမှ {AK} နေရပါမည်နည်း”ဟု{END}"        # "kudāssu nāmāhampi … viharissāmī"ti.
TASSA_EVAM, TASSA_NA_EVAM = "ထိုသူအား ဤသို့ အကြံ ဖြစ်၏", "ထိုသူအား ဤသို့ အကြံ မဖြစ်"
DUSS_LONG = (f"{DUSS_HOTI}{C} စင်ကြယ်မှု မရှိသူ{C} သံသယဖြင့် အောက်မေ့ရသော အကျင့် ရှိသူ{C} ဖုံးကွယ်ထားသော အမှု ရှိသူ{C} "
             f"ရဟန်း မဟုတ်ဘဲ ရဟန်းဟု ဝန်ခံသူ{C} မြင့်မြတ်သော အကျင့်ကို မကျင့်ဘဲ မြင့်မြတ်သော အကျင့်ကို ကျင့်သူဟု "
             f"ဝန်ခံသူ{C} အတွင်း၌ ပုပ်သိုးသူ{C} ကိလေသာ စိုစွတ်သူ{C} အမှိုက်သရိုက်ကဲ့သို့ ဖြစ်နေသူ {COP}")
_DUSS_LONG_P = ("Idhekacco puggalo dussīlo hoti pāpadhammo asuci saṅkassarasamācāro paṭicchannakammanto assamaṇo "
                "samaṇapaṭiñño abrahmacārī brahmacāripaṭiñño antopūti avassuto kasambujāto.")
TAKISSA = fin("Taṃ kissa hetu?")                                     # pi-2 ^2-943
KATAME3 = f"အဘယ် {PUG} {F.persons(3)}နည်း{END}"                       # Katame tayo?
SANTO = f"ရှိကြ၏{C} ထင်ရှား တွေ့ရကြ၏"                                 # santo saṃvijjamānā
SEYY, EVAM = "ဥပမာအားဖြင့်", "ဤအတူပင်"                               # seyyathāpi (nāma) / evamevaṃ
IDHA_PANA = f"တစ်ဖန် {IDHA}"                                           # idha panekacco puggalo
TATHA_DASS = f"{W['tathagata']}ကို ဖူးမြင်ရန်"                           # tathāgataṃ dassanāya
DHAMMAVINAYA = wit("imasmiṃ dhammavinaye", "တရားနှင့် ဝိနည်း")
DHV = f"{W['tathagata']} ဟောကြားထားသော {DHAMMAVINAYA}ကို နာကြားရန်"     # tathāgatappaveditaṃ dhammavinayaṃ savaṇāya
_NIYAMA = "ကုသိုလ် သဘောတရားတို့၌ မှန်ကန်မှု ဖြစ်သော သေချာသော လမ်းကြောင်းသို့"   # niyāmaṃ kusalesu … (sample ^4-12)
GET, NOGET = "ရသည်ဖြစ်စေ", "မရသည်ဖြစ်စေ"                               # labhanto vā / alabhanto vā
ONLY = f"ရသည်သာ ဖြစ်၍ မရသည် မဟုတ်"                                    # labhanto … no alabhanto
FOOD, MED, NURSE = "သင့်လျော်သော အစားအစာတို့ကို", "သင့်လျော်သော ဆေးဝါးတို့ကို", "လျောက်ပတ်သော လုပ်ကျွေးပြုစုသူကို"
ABADHA = wit("ābādho",
                   "အနာရောဂါ")
RECOVER, NORECOVER = f"ထို{ABADHA}မှ ပျောက်ကင်း၏", f"ထို{ABADHA}မှ မပျောက်ကင်း"   # vuṭṭhāti tamhā ābādhā
GIL3 = (f"{FOOD} {GET}{C} {NOGET}{C} {MED} {GET}{C} {NOGET}{C} {NURSE} {GET}{C} {NOGET}")
GIL_ONLY = f"{FOOD} {ONLY}{C} {MED} {ONLY}{C} {NURSE} {ONLY}"
PUG3 = f"{TATHA_DASS} {GET}{C} {NOGET}{C} {DHV} {GET}{C} {NOGET}"
PUG_ONLY = f"{TATHA_DASS} {ONLY}{C} {DHV} {ONLY}"
GIL_P = ("labhanto vā sappāyāni bhojanāni alabhanto vā sappāyāni bhojanāni, labhanto vā sappāyāni bhesajjāni "
         "alabhanto vā sappāyāni bhesajjāni, labhanto vā patirūpaṃ upaṭṭhākaṃ alabhanto vā patirūpaṃ upaṭṭhākaṃ")
GIL_ONLY_P = ("labhanto sappāyāni bhojanāni no alabhanto, labhanto sappāyāni bhesajjāni no alabhanto, labhanto "
              "patirūpaṃ upaṭṭhākaṃ no alabhanto")
PUG3_P = ("labhanto vā tathāgataṃ dassanāya alabhanto vā tathāgataṃ dassanāya, labhanto vā tathāgatappaveditaṃ "
          "dhammavinayaṃ savaṇāya alabhanto vā tathāgatappaveditaṃ dhammavinayaṃ savaṇāya")
PUG_ONLY_P = ("labhanto tathāgataṃ dassanāya no alabhanto, labhanto tathāgatappaveditaṃ dhammavinayaṃ savaṇāya no "
              "alabhanto")
OKK, NO_OKK = f"{_NIYAMA} သက်ဆင်း၏", f"{_NIYAMA} မသက်ဆင်း"            # okkamati niyāmaṃ … (sample «သက်ဆင်းရန်»)
BHAGAVA = W["tathagata"]                                              # bhagavā = «မြတ်စွာဘုရား» (as tathāgata)
GILANA = "လူနာ"
# kodhano … pātukaroti (^4-101, ^4-125)
KODH = (f"{N['kodhano']} {COP}{C} ပြင်းစွာ ပူပန်ခြင်း များသူ {COP}{C} အနည်းငယ်မျှ ပြောဆိုခံရရုံဖြင့်ပင် ငြိုငြင်၏{C} "
        f"အမျက်ထွက်၏{C} ဖောက်ပြန်၏{C} ခိုင်ခိုင်မာမာ ဆန့်ကျင်၏{{}}{C} အမျက်ထွက်ခြင်းကိုလည်း{C} ဒေါသကိုလည်း{C} "
        f"မနှစ်သက်မှုကိုလည်း ထင်ရှား ပြ၏")
F.witness("2", "^2-198", "upāyāso", "ပြင်းစွာ ပူပန်ခြင်း")
F.witness("1", "^1-1066", "kopo pakopo", "အမျက်ထွက်ခြင်း")
KODH_P = ("kodhano hoti upāyāsabahulo, appampi vutto samāno abhisajjati kuppati byāpajjati patitthīyati{}, "
          "kopañca dosañca appaccayañca pātukaroti")
STICK = f"သစ်သားချောင်းဖြင့်ဖြစ်စေ{C} အိုးခြမ်းကွဲဖြင့်ဖြစ်စေ{{}} ထိခိုက်မိလျှင် ပို၍ ပို၍"   # kaṭṭhena vā kaṭhalāya vā ghaṭṭito bhiyyoso mattāya
AROO = f"{SEYY} ပြည်တည်နေသော အနာသည် {STICK} ပြည်ယို{{}}သကဲ့သို့"
TRUTHS = nofs(F.SENT['Idhekacco puggalo "idaṃ dukkha"nti yathābhūtaṃ pajānāti, "ayaṃ dukkhasamudayo"ti yathābhūtaṃ '
                     'pajānāti, "ayaṃ dukkhanirodho"ti yathābhūtaṃ pajānāti, "ayaṃ dukkhanirodhagāminī paṭipadā"ti '
                     'yathābhūtaṃ pajānāti.'])
TRUTHS_P = ('"idaṃ dukkha"nti yathābhūtaṃ pajānāti, "ayaṃ dukkhasamudayo"ti yathābhūtaṃ pajānāti, "ayaṃ '
            'dukkhanirodho"ti yathābhūtaṃ pajānāti, "ayaṃ dukkhanirodhagāminī paṭipadā"ti yathābhūtaṃ pajānāti')
assert TRUTHS.startswith(IDHA + " ")
TRUTHS_B = TRUTHS[len(IDHA) + 1:]
TATHA_DH = nofs(F.SENT["Tathāgatappaveditā cassa dhammā paññāya vodiṭṭhā honti vocaritā."])
TRUTH1 = TRUTHS_B.split(f"{C} ")[0]                                    # «“ဤသည်ကား ဒုက္ခ”ဟု … သိ၏»
# the monastery (^4-107 … ^4-109)
GOES = f"ရဟန်းတို့၏ အထံ၌ တရား နာကြားရန်{{1}} ကျောင်းသို့ ခဏခဏ သွားသူ{{0}} {COP}"   # ārāmaṃ gantā hoti abhikkhaṇaṃ …
GOES_PLAIN = GOES.format("", "")
GOES_P = "ārāmaṃ gantā hoti abhikkhaṇaṃ bhikkhūnaṃ santike dhammassavaṇāya."
DESENTI = (f"ထိုသူအား ရဟန်းတို့သည် အစ၌ ကောင်းသော{C} အလယ်၌ ကောင်းသော{C} အဆုံး၌ ကောင်းသော တရားကို ဟောကြားကြ၏{C} "
           f"အနက်အဓိပ္ပာယ်နှင့် ပြည့်စုံသော{C} စကားလုံးနှင့် ပြည့်စုံသော{C} အလုံးစုံ ပြည့်စုံသော{C} စင်ကြယ်သော "
           f"မြင့်မြတ်သော အကျင့်ကို ထုတ်ဖော် ပြကြ၏{END}")
F.witness("1", "^1-1355", "brahmacariyānuggahāya", "မြင့်မြတ်သော အကျင့်")
wit("manasikārakusalatā", "နှလုံးသွင်း")
_MN = "နှလုံးသွင်း"
NO_MANASI = f"ထိုတရားစကား၏ အစကိုလည်း နှလုံး မသွင်း{C} အလယ်ကိုလည်း နှလုံး မသွင်း{C} အဆုံးကိုလည်း နှလုံး မသွင်း"
YES_MANASI = f"ထိုတရားစကား၏ အစကိုလည်း {_MN}၏{C} အလယ်ကိုလည်း {_MN}၏{C} အဆုံးကိုလည်း {_MN}၏"
SEATED = "ထိုသူသည် ထိုနေရာ၌ ထိုင်နေစဉ်"                               # So tasmiṃ āsane nisinno
ROSE_PI = "ထိုနေရာမှ ထပြီးသော်လည်း"                                   # Vuṭṭhitopi tamhā āsanā
ROSE_CA = "ထိုနေရာမှ ထပြီးသောအခါ၌ကား"                                 # Vuṭṭhito ca kho tamhā āsanā
_NEVA_ADI = "tassā kathāya neva ādiṃ manasi karoti, na majjhaṃ manasi karoti, na pariyosānaṃ manasi karoti"
_NEVA_ADIPI = "tassā kathāya neva ādimpi manasi karoti, na majjhampi manasi karoti, na pariyosānampi manasi karoti"
_ADIPI = "tassā kathāya ādimpi manasi karoti, majjhampi manasi karoti, pariyosānampi manasi karoti"
# the lines (^4-113 … ^4-115)
OFTEN_ANGRY = f"ခဏခဏ {N['kodhano'][:-5]}၏"                             # abhiṇhaṃ kujjhati («အမျက်ဒေါသ ထွက်၏»)
assert OFTEN_ANGRY == "ခဏခဏ အမျက်ဒေါသ ထွက်၏"
LONG = "ကြာမြင့်စွာ ရှည်လျားသော ကာလပတ်လုံး"                              # ciraṃ dīgharattaṃ
KODHO_OF = f"ထိုသူ၏ ထို{QUAL['kodho']}သည်လည်း"                           # so ca khvassa kodho
SPOKEN = (f"ပြင်းထန်စွာ ပြောဆိုခံရသော်လည်း{C} ကြမ်းတမ်းစွာ ပြောဆိုခံရသော်လည်း{C} မနှစ်မြို့ဖွယ် ပြောဆိုခံရသော်လည်း "
          f"ညီညွတ်စွာ ပေါင်းစည်းသည်သာ{{0}}{C} ပြန်လည် ဆက်စပ်သည်သာ{{1}}{C} ဝမ်းမြောက်စွာ ဆက်ဆံသည်သာ{{2}} {COP}")
wit("pharusā vācā", "ကြမ်းတမ်းသော စကား")
SPOKEN_P = ("āgāḷhenapi vuccamāno pharusenapi vuccamāno amanāpenapi vuccamāno saṃsandatimeva{} sandhiyatimeva{} "
            "sammodatimeva{}")
_CEVA = " [… ceva (syā.) a. ni. 3.133]"
# the cloths (^4-116, ^4-117)
POT, KAS = "လျှော်ပိတ်စ", "ကာသိ ပိတ်စ"
wit("dukkhasamphassaṃ", "ထိတွေ့ရ နာကျင်")
wit("sukhasamphassaṃ", "ထိတွေ့ရ သာယာ")
UGLY, PAINF, CHEAP = "အဆင်း ညှိုး", "ထိတွေ့ရ နာကျင်", "တန်ဖိုး နည်း"     # dubbaṇṇa / dukkhasamphassa / appaggha
FAIR, PLEAS, DEAR = "အဆင်း လှ", "ထိတွေ့ရ သာယာ", "တန်ဖိုး ကြီး"          # vaṇṇavant / sukhasamphassa / mahaggha
NEW, MID, OLD = "အသစ် ဖြစ်သော", "အလယ်အလတ် ဖြစ်သော", "ဟောင်းနွမ်းသော"   # nava / majjhima / jiṇṇa
POT_Q = f"{UGLY}၏{C} {PAINF}၏{C} {CHEAP}၏"
KAS_Q = f"{FAIR}၏{C} {PLEAS}၏{C} {DEAR}၏"
BH_NEW, BH_MID, BH_OLD = "ရဟန်း ဝါငယ် ဖြစ်စေကာမူ", "ရဟန်း ဝါလတ် ဖြစ်စေကာမူ", "ရဟန်း ထေရ် ဖြစ်စေကာမူ"   # navo / majjhimo / thero cepi bhikkhu
IDAMASSA = "ဤသည်မှာ ထိုရဟန်း၏ {}ခြင်း ဖြစ်၏" + END                     # idamassa …tāya
TATHUPAMA = "ဤပုဂ္ဂိုလ်သည် ထိုနှင့် တူ၏" + END                           # tathūpamo ayaṃ puggalo
FOLLOW = (f"ထိုရဟန်းကို ပေါင်းသင်းကြ၊ ဆည်းကပ်ကြ၊ ချဉ်းကပ် ခစားကြ၍ ထိုရဟန်း၏ အမြင်ကို အတုယူ လိုက်နာကြသော "
          f"အကြင်သူတို့ ရှိကုန်၏{C} ထိုသူတို့အား ထိုအမှုသည် ကြာမြင့်စွာ {{}} ဖြစ်၏{END}")
HARM, GOOD = "အစီးအပွား မရှိခြင်းငှာ၊ ဆင်းရဲခြင်းငှာ", "အစီးအပွားငှာ၊ ချမ်းသာခြင်းငှာ"   # ahitāya dukkhāya / hitāya sukhāya
_REQ = F.witness("2", "^2-929", "Itarītaracīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhārehi",
                 "သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ၊ သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်")
ACCEPT = (f"ထိုရဟန်းသည် အကြင်သူတို့၏{{}} {_REQ}ကို လက်ခံ{{}}၏{C} ထိုသူတို့အား ထိုအလှူသည် {{}}{END}")
NOFRUIT = f"အကျိုး ကြီးမားသည် မဟုတ်{C} အာနိသင် ကြီးမားသည် မဟုတ်"
FRUIT = f"အကျိုး ကြီးမား၏{C} အာနိသင် ကြီးမား၏"
SAVAKA_BH = "ရဟန်းတို့အတွင်း၌"                                          # bhikkhūsu
BALASSA = F.witness("2", "^2-957", "kiṃ nu kho tuyhaṃ bālassa abyattassa bhaṇitena",
                    "“မိုက်မဲ၍ မလိမ္မာသော သင်၏ ပြောဆိုမှုဖြင့် အဘယ် အကျိုး ရှိမည်နည်း")
F.witness("2", "^2-957", "Tvampi nāma maṃ bhaṇitabbaṃ maññasī", "သင်ပင်လျှင် ငါ့ကို ပြောဆိုထိုက်သည်ဟု ထင်သလော")
# the three to be followed or not (^4-121 … ^4-126)
SEV_YES = f"ပေါင်းသင်းအပ်၏{C} ဆည်းကပ်အပ်၏{C} ချဉ်းကပ် ခစားအပ်၏"
SEV_NO = F.SEV3_NO
EVARUPO = f"ဤသို့ သဘောရှိသော {PUG}ကို"
SSP = f"သီလ{C} သမာဓိ{C} ပညာတို့ဖြင့်"                                     # sīlena samādhinā paññāya
FAME = "ထိုသူ၏ {} သတင်းစကား ပျံ့နှံ့၏"                                  # atha kho naṃ … kittisaddo abbhuggacchati
NOFOLLOW = f"ဤသို့ သဘောရှိသော {PUG}၏ အမြင်ကို အတုယူ မလိုက်နာသော်လည်း"   # kiñcāpi … na diṭṭhānugatiṃ āpajjati
PAPAM_Q = (f"“ဤလူ {PUG}သည် {N['pāpamitto']}၊ အပေါင်းအဖော် ဆိုး ရှိသူ၊ ဆိုးသူတို့ဘက်သို့ ညွတ်ကိုင်းသူ "
           f"ဖြစ်၏”ဟူ၍{END}")
KALYM_Q = (f"“ဤလူ {PUG}သည် {N['kalyāṇamitto']}၊ အပေါင်းအဖော် ကောင်း ရှိသူ၊ ကောင်းသူတို့ဘက်သို့ ညွတ်ကိုင်းသူ "
           f"ဖြစ်၏”ဟူ၍{END}")
TASMA = "ထို့ကြောင့်"
# the teachers (^4-130, ^4-131)
TEACHER = "ဆရာ"
PARINNA = wit("pariññāya", "ပိုင်းခြား သိ")
PANNAP, NO_PANNAP = "ပညတ်၏", "မပညတ်"                                    # paññapeti (pi-2 «ပညတ်ကြ၏»)
wit("paññapenti", "ပညတ်ကြ၏")
KAMA_P, RUPA_P, VED_P = "ကာမတို့ကို", "ရုပ်တို့ကို", "ခံစားမှုတို့ကို"
PKN = f"{PARINNA}ခြင်းကို"
ATTA = F.witness("2", "^2-948", "attā", "အတ္တ")
SACCATO = F.witness("2", "^2-948", "saccato thetato", "အမှန်အားဖြင့် ခိုင်မြဲစွာ")
NEXT = "တမလွန်ဘဝ၌"                                                    # abhisamparāyaṃ
SASSATA = F.witness("2", "^2-977", "sassatavādā", "ထာဝရ တည်မြဲသည်ဟု ဆိုသော ဝါဒ")
UCCHEDA = F.witness("2", "^2-977", "ucchedavādā", "ပြတ်စဲသွားသည်ဟု ဆိုသော ဝါဒ")
RUPAV_SAMAP = f"သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော {F.SAMAPATTI}"           # rūpāvacarasamāpatti
ARUPAV_SAMAP = f"ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော {F.SAMAPATTI}"
wit("Arūpāvacaravipākā", "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော")
SEEN = "ဟု ထိုအကြောင်းဖြင့် သိမြင်ရမည်" + END                            # tena daṭṭhabbo
TATRA_T = "ထိုဆရာတို့အနက်"                                              # tatra yvāyaṃ satthā …

UNIQUE4 = {
    # ^4-91 … ^4-93 hope
    _DUSS_LONG_P: f"{IDHA} {DUSS_LONG}{END}",
    "So suṇāti": SUNATI,
    f'"itthannāmo kira bhikkhu {AK_P} viharatī"ti.': HEARD,
    "Tassa na evaṃ hoti": TASSA_NA_EVAM,
    "Tassa evaṃ hoti": TASSA_EVAM,
    f'"kudāssu nāmāhampi {AK_P} viharissāmī"ti.': HOPE,
    "Idhekacco puggalo sīlavā hoti kalyāṇadhammo.": f"{IDHA} {SIL_HOTI}{END}",
    f"Idhekacco puggalo {AK_P} viharati.": f"{IDHA} {AK} {VIHARATI}{END}",
    f"Idhekacco puggalo {AK_P} viharati": f"{IDHA} {AK} {VIHARATI}",
    "Taṃ kissa hetu?": TAKISSA,
    "Yā hissa pubbe avimuttassa vimuttāsā, sā paṭippassaddhā.":
        f"အကြောင်းမူကား ထိုသူ၏ ယခင်က မလွတ်မြောက်သေးစဉ် ဖြစ်ခဲ့သော လွတ်မြောက်လိုသော မျှော်လင့်ချက် ရှိသမျှသည် "
        f"ငြိမ်းသွားပြီ ဖြစ်၏{END}",
    # ^4-94 the sick
    "Tayo gilānā": f"{GILANA} {F.persons(3)}",
    f"idhekacco gilāno {GIL_P}, neva vuṭṭhāti tamhā ābādhā.":
        f"ဤလောက၌ အချို့သော {GILANA}သည် {GIL3} {NORECOVER}{END}",
    f"Idha panekacco gilāno {GIL_P}, vuṭṭhāti tamhā ābādhā.":
        f"တစ်ဖန် ဤလောက၌ အချို့သော {GILANA}သည် {GIL3} {RECOVER}{END}",
    f"Idha panekacco gilāno {GIL_ONLY_P}, vuṭṭhāti tamhā ābādhā.":
        f"တစ်ဖန် ဤလောက၌ အချို့သော {GILANA}သည် {GIL_ONLY}{C} {RECOVER}{END}",
    f"Tatra yvāyaṃ gilāno {GIL_ONLY_P}, vuṭṭhāti tamhā ābādhā, imaṃ gilānaṃ paṭicca bhagavatā gilānabhattaṃ "
    "anuññātaṃ gilānabhesajjaṃ anuññātaṃ gilānupaṭṭhāko anuññāto.":
        f"ထို{GILANA}တို့အနက် {GIL_ONLY}{C} {RECOVER[:-1]}သော အကြင် {GILANA} ရှိ၏{C} ဤ{GILANA}ကို အကြောင်းပြု၍ "
        f"{BHAGAVA}သည် {GILANA}၏ အစားအစာကို ခွင့်ပြုတော်မူ၏{C} {GILANA}၏ ဆေးဝါးကို ခွင့်ပြုတော်မူ၏{C} {GILANA}ကို "
        f"လုပ်ကျွေးပြုစုသူကို ခွင့်ပြုတော်မူ၏{END}",
    "Imañca pana gilānaṃ paṭicca aññepi gilānā upaṭṭhātabbā.":
        f"ဤ{GILANA}ကို အကြောင်းပြု၍ပင် အခြား {GILANA}တို့ကိုလည်း လုပ်ကျွေးပြုစုရမည်{END}",
    "Evamevaṃ [evameva (sī.)] tayo gilānūpamā puggalā santo saṃvijjamānā lokasmiṃ.":
        f"{EVAM} ⟦0⟧ {F.GROUP['gilānūpamā']} {PUG} {F.persons(3)}တို့သည် လောက၌ {SANTO}{END}",
    "Katame tayo?": KATAME3,
    f"Idhekacco puggalo {PUG3_P}, neva okkamati niyāmaṃ kusalesu dhammesu sammattaṃ.":
        f"{IDHA} {PUG3} {NO_OKK}{END}",
    f"Idha panekacco puggalo {PUG3_P}, okkamati niyāmaṃ kusalesu dhammesu sammattaṃ.":
        f"{IDHA_PANA} {PUG3} {OKK}{END}",
    f"Idha panekacco puggalo {PUG_ONLY_P}, okkamati niyāmaṃ kusalesu dhammesu sammattaṃ.":
        f"{IDHA_PANA} {PUG_ONLY}{C} {OKK}{END}",
    f"Tatra yvāyaṃ puggalo {PUG_ONLY_P}, okkamati niyāmaṃ kusalesu dhammesu sammattaṃ, imaṃ puggalaṃ paṭicca "
    "bhagavatā dhammadesanā anuññātā, imañca puggalaṃ paṭicca aññesampi dhammo desetabbo.":
        f"ထို{PUG_PL}အနက် {PUG_ONLY}{C} {OKK[:-1]}သော အကြင် {PUG} ရှိ၏{C} ဤ{PUG}ကို အကြောင်းပြု၍ {BHAGAVA}သည် "
        f"တရား ဟောကြားခြင်းကို ခွင့်ပြုတော်မူ၏{C} ဤ{PUG}ကို အကြောင်းပြု၍ပင် အခြားသူတို့အားလည်း တရား "
        f"ဟောကြားရမည်{END}",
    "Ime tayo gilānūpamā puggalā santo saṃvijjamānā lokasmiṃ.":
        f"ဤ {F.GROUP['gilānūpamā']} {PUG} {F.persons(3)}တို့သည် လောက၌ {SANTO}{END}",
    # ^4-95 … ^4-97
    "Idhekacco puggalo aṭṭha vimokkhe kāyena phusitvā viharati, paññāya cassa disvā ekacce āsavā parikkhīṇā honti":
        f"{IDHA} {F.VIMOK}{C} {F.ASAVA_SOME}",
    f"Idhekacco puggalo {TRUTHS_P}, tathāgatappaveditā cassa dhammā paññāya vodiṭṭhā honti vocaritā, paññāya cassa "
    "disvā ekacce āsavā parikkhīṇā honti": f"{TRUTHS}{C} {TATHA_DH}{C} {F.ASAVA_SOME}",
    'Idhekacco puggalo "idaṃ dukkha"nti yathābhūtaṃ pajānāti…pe… tathāgatappaveditā cassa dhammā paññāya vodiṭṭhā '
    'honti vocaritā, paññāya cassa disvā ekacce āsavā parikkhīṇā honti, no ca kho yathādiṭṭhippattassa':
        f"{IDHA} {TRUTH1}… {TATHA_DH}{C} "
        + F.SENT["Paññāya cassa disvā ekacce āsavā parikkhīṇā honti, no ca kho yathā diṭṭhippattassa"],
    # ^4-98, ^4-99 speech
    "Idhekacco puggalo musāvādī hoti sabhaggato vā parisaggato vā ñātimajjhagato vā pūgamajjhagato vā "
    "rājakulamajjhagato vā abhinīto sakkhipuṭṭho": None,
    "Idhekacco puggalo musāvādaṃ pahāya musāvādā paṭivirato hoti sabhaggato vā parisaggato vā ñātimajjhagato vā "
    "pūgamajjhagato vā rājakulamajjhagato vā abhinīto sakkhipuṭṭho": None,
}
_MUSA = F.witness("2", "^2-942", "musāvādo", "မုသား ပြောခြင်း")
_AMONG = (f"လူစုအဝေးသို့ ရောက်နေသည်ဖြစ်စေ{C} ပရိသတ်သို့ ရောက်နေသည်ဖြစ်စေ{C} ဆွေမျိုးတို့ အလယ်သို့ ရောက်နေသည်ဖြစ်စေ{C} "
          f"အသင်းအပင်း အလယ်သို့ ရောက်နေသည်ဖြစ်စေ{C} မင်းမျိုးမင်းနွယ် အလယ်သို့ ရောက်နေသည်ဖြစ်စေ သက်သေအဖြစ် "
          f"ခေါ်ဆောင်ခံရ၍ မေးမြန်းခံရသောအခါ")
UNIQUE4["Idhekacco puggalo musāvādī hoti sabhaggato vā parisaggato vā ñātimajjhagato vā pūgamajjhagato vā "
        "rājakulamajjhagato vā abhinīto sakkhipuṭṭho"] = f"{IDHA} မုသား ပြောသူ {COP}{C} {_AMONG}"
UNIQUE4["Idhekacco puggalo musāvādaṃ pahāya musāvādā paṭivirato hoti sabhaggato vā parisaggato vā ñātimajjhagato "
        "vā pūgamajjhagato vā rājakulamajjhagato vā abhinīto sakkhipuṭṭho"] = (
    f"{IDHA} {_MUSA}ကို ပယ်၍ {_MUSA}မှ ရှောင်ကြဉ်သူ {COP}{C} {_AMONG}")
_EHI = f"“လာလော့ အချင်း{{}}{C} ယောက်ျား{C} သင် သိသည်ကို ပြောလော့”ဟု ဆိုသောအခါ ထိုသူသည် မသိလျက်လည်း ပြော၏"
_KNOW, _NOKNOW, _SEE, _NOSEE = "“ငါ သိ၏”ဟု", "“ငါ မသိ”ဟု", "“ငါ မြင်၏”ဟု", "“ငါ မမြင်”ဟု"
_SAYS_K, _SAYS_NS, _SAYS_S = "သိလျက်လည်း ပြော၏", "မမြင်လျက်လည်း ပြော၏", "မြင်လျက်လည်း ပြော၏"
_ITI = (f"ဤသို့ မိမိ၏ အကြောင်းကြောင့်ဖြစ်စေ{C} သူတစ်ပါး၏ အကြောင်းကြောင့်ဖြစ်စေ{C} အနည်းငယ်သော ပစ္စည်း လာဘ်ကြောင့်ဖြစ်စေ "
        f"သိလျက် မုသား ပြောသူ")
UNIQUE4.update({
    '"ehambho [ehi bho (syā. ka.) ma. ni. 1.440; a. ni. 3.28], purisa, yaṃ jānāsi taṃ vadehī"ti, so ajānaṃ vā āha':
        _EHI.format(" ⟦0⟧"),
    '"ehambho, purisa, yaṃ jānāsi taṃ vadehī"ti, so ajānaṃ vā āha': _EHI.format(""),
    '"jānāmī"ti, jānaṃ vā āha': f"{_KNOW}{C} {_SAYS_K}",
    '"na jānāmī"ti, apassaṃ vā āha': f"{_NOKNOW}{C} {_SAYS_NS}",
    '"passāmī"ti, passaṃ vā āha': f"{_SEE}{C} {_SAYS_S}",
    '"na passāmī"ti.': f"{_NOSEE}{END}",
    '"na jānāmī"ti, jānaṃ vā āha': f"{_NOKNOW}{C} {_SAYS_K}",
    '"jānāmī"ti, apassaṃ vā āha': f"{_KNOW}{C} {_SAYS_NS}",
    '"na passāmī"ti, passaṃ vā āha': f"{_NOSEE}{C} {_SAYS_S}",
    '"passāmī"ti.': f"{_SEE}{END}",
    "Iti attahetu vā parahetu vā āmisakiñcikkhahetu vā sampajānamusā bhāsitā hoti": f"{_ITI} {COP}",
    "Iti attahetu vā parahetu vā āmisakiñcikkhahetu vā na sampajānamusā bhāsitā hoti": f"{_ITI} မဟုတ်",
    "Idhekacco puggalo yā sā vācā nelā kaṇṇasukhā pemaniyā hadayaṅgamā porī bahujanakantā bahujanamanāpā, "
    "tathārūpiṃ vācaṃ bhāsitā hoti":
        f"{IDHA} အပြစ် ကင်းသော{C} နားဝင် ချိုသော{C} ချစ်ခင်ဖွယ် ကောင်းသော{C} နှလုံးသို့ ရောက်သော{C} ယဉ်ကျေးသော{C} "
        f"လူအများ နှစ်သက်သော{C} လူအများ စိတ်တိုင်းကျသော စကား ရှိ၏{C} ထိုသို့ သဘောရှိသော စကားကို ပြောသူ {COP}",
    # ^4-101 … ^4-103 the similes of the mind
    f"Idhekacco puggalo {KODH_P.format(' [patiṭṭhīyati (syā. ka.) a. ni. 3.25]')}.":
        f"{IDHA} {KODH.format(' ⟦0⟧')}{END}",
    f"Idhekacco puggalo {KODH_P.format('')}.": f"{IDHA} {KODH.format('')}{END}",
    "Seyyathāpi nāma duṭṭhāruko kaṭṭhena vā kaṭhalāya [kathalāya (ka.), kathalena (aṭṭhakathā) a. ni. 3.25] vā "
    f"ghaṭṭito bhiyyoso mattāya āsavaṃ deti [assavanoti (sī.)], evamevaṃ idhekacco puggalo {KODH_P.format('')}":
        f"{AROO.format(' ⟦0⟧', ' ⟦1⟧')}{C} {EVAM} {IDHA} {KODH.format('')}",
    "Seyyathāpi nāma duṭṭhāruko kaṭṭhena vā kaṭhalāya vā ghaṭṭito bhiyyoso mattāya āsavaṃ deti, evamevaṃ idhekacco "
    f"puggalo {KODH_P.format('')}.": f"{AROO.format('', '')}{C} {EVAM} {IDHA} {KODH.format('')}{END}",
    "Seyyathāpi nāma tindukālātaṃ kaṭṭhena vā kaṭhalāya vā ghaṭṭitaṃ bhiyyoso mattāya cicciṭāyati ciṭiciṭāyati, "
    f"evamevaṃ idhekacco puggalo {KODH_P.format('')}.":
        f"{SEYY} တည်သားဖြင့် လုပ်သော မီးစသည် {STICK.format('')} တဖျစ်ဖျစ် မြည်၍ တဖွားဖွား မီးပွင့်သကဲ့သို့{C} "
        f"{EVAM} {IDHA} {KODH.format('')}{END}",
    "Seyyathāpi nāma gūthakūpo kaṭṭhena vā kaṭhalāya vā ghaṭṭito bhiyyoso mattāya duggandho hoti, evamevaṃ "
    f"idhekacco puggalo {KODH_P.format('')}; evarūpo puggalo ajjhupekkhitabbo na sevitabbo na bhajitabbo na "
    "payirupāsitabbo.":
        f"{SEYY} မစင်တွင်းသည် {STICK.format('')} အနံ့ ဆိုးသကဲ့သို့{C} {EVAM} {IDHA} {KODH.format('')}{C} "
        f"{EVARUPO} လျစ်လျူရှုအပ်၏{C} {SEV_NO}{END}",
    f'Seyyathāpi nāma cakkhumā puriso rattandhakāratimisāya vijjantarikāya rūpāni passeyya, evamevaṃ idhekacco '
    f'puggalo {TRUTHS_P}':
        f"{SEYY} မျက်စိ ကောင်းသော ယောက်ျားသည် ညဉ့်အခါ မှောင်မိုက် ထူထပ်စဉ် လျှပ်စီး လက်သည့် ခဏ၌ "
        f"အဆင်းအရောင်တို့ကို မြင်ရာသကဲ့သို့{C} {EVAM} {TRUTHS}",
    f"Seyyathāpi nāma vajirassa natthi kiñci abhejjaṃ maṇi vā pāsāṇo vā, evamevaṃ idhekacco puggalo {AK_P} viharati":
        f"{SEYY} စိန်အတွက် ပတ္တမြားဖြစ်စေ{C} ကျောက်ဖြစ်စေ မဖောက်ထွင်းနိုင်သည့် အရာ တစ်စုံတစ်ရာမျှ မရှိသကဲ့သို့{C} "
        f"{EVAM} {IDHA} {AK} {VIHARATI}",
})
# ^4-104 … ^4-106 the eyes
_EYE_WEALTH = (f"ဤလောက၌ အချို့သော {PUG}၏ အကြင် မျက်စိဖြင့် မရသေးသော စည်းစိမ်ဥစ္စာကို ရရာ၏{C} ရပြီးသော "
               f"စည်းစိမ်ဥစ္စာကို တိုးပွားအောင် ပြုရာ၏{C} ထိုသို့ သဘောရှိသော မျက်စိ {{}}")
_EYE_DHAMMA = (f"အကြင် မျက်စိဖြင့် ကုသိုလ် အကုသိုလ် သဘောတရားတို့ကို သိရာ၏{C} အပြစ် ရှိသော အပြစ် မရှိသော "
               f"သဘောတရားတို့ကို သိရာ၏{C} ယုတ်ညံ့သော မွန်မြတ်သော သဘောတရားတို့ကို သိရာ၏{C} မည်းနက်သော ဖြူစင်သော "
               f"ဆန့်ကျင်ဘက် ရှိသော သဘောတရားတို့ကို သိရာ၏{C} ထိုသို့ သဘောရှိသော မျက်စိလည်း ထိုသူ၏ {{}}")
F.witness("1", "^1-M2-104", "sukkā dhammā", "ဖြူစင်သော")
F.witness("1", "^1-M1-14", "paṇītā dhammā", "မွန်မြတ်သော")
_EYE_P = ("Idhekaccassa puggalassa tathārūpaṃ cakkhu {} yathārūpena cakkhunā anadhigataṃ vā bhogaṃ adhigaccheyya, "
          "adhigataṃ vā bhogaṃ phātiṃ kareyya; tathārūpampissa cakkhu {} yathārūpena cakkhunā kusalākusale dhamme "
          "jāneyya, sāvajjānavajje dhamme jāneyya, hīnappaṇīte dhamme jāneyya, kaṇhasukkasappaṭibhāge dhamme jāneyya")
for _a, _b, _c in (("na hoti", "na hoti", ""), ("hoti,", "na hoti", ""), ("hoti", "hoti", "")):
    UNIQUE4[_EYE_P.format(_a, _b)] = (_EYE_WEALTH.format("ရှိ၏" if _a.startswith("hoti") else "မရှိ") + f"{C} " +
                                      _EYE_DHAMMA.format("ရှိ၏" if _b == "hoti" else "မရှိ"))
# ^4-107 … ^4-109 the pots and the lap
UNIQUE4.update({
    "Idhekacco puggalo ārāmaṃ gantā [gato (sī.), gantvā (syā.)] hoti abhikkhaṇaṃ bhikkhūnaṃ santike dhammassavaṇāya "
    "[dhammassavanāya (syā.)].": f"{IDHA} {GOES.format(' ⟦0⟧', ' ⟦1⟧')}{END}",
    f"Idhekacco puggalo {GOES_P}": f"{IDHA} {GOES_PLAIN}{END}",
    "Tassa bhikkhū dhammaṃ desenti ādikalyāṇaṃ majjhekalyāṇaṃ pariyosānakalyāṇaṃ sātthaṃ sabyañjanaṃ "
    "kevalaparipuṇṇaṃ parisuddhaṃ brahmacariyaṃ pakāsenti.": DESENTI,
    f"So tasmiṃ āsane nisinno {_NEVA_ADI}.": f"{SEATED} {NO_MANASI}{END}",
    f"Vuṭṭhitopi tamhā āsanā {_NEVA_ADI}.": f"{ROSE_PI} {NO_MANASI}{END}",
    f"Vuṭṭhitopi tamhā āsanā {_NEVA_ADI}": f"{ROSE_PI} {NO_MANASI}",
    "Seyyathāpi nāma kumbho nikkujjo [nikujjo (syā.) a. ni. 3.30] tatra udakaṃ āsittaṃ vivaṭṭati, no saṇṭhāti; "
    f"evamevaṃ idhekacco puggalo {GOES_P}":
        f"{SEYY} မှောက်ထားသော အိုး ⟦0⟧၌ လောင်းထည့်သော ရေသည် စီးကျသွား၏{C} မတည်နေသကဲ့သို့{C} {EVAM} {IDHA} "
        f"{GOES_PLAIN}{END}",
    f"So tasmiṃ āsane nisinno {_ADIPI}.": f"{SEATED} {YES_MANASI}{END}",
    f"Vuṭṭhito ca kho tamhā āsanā {_NEVA_ADI}.": f"{ROSE_CA} {NO_MANASI}{END}",
    "Seyyathāpi nāma purisassa ucchaṅge nānākhajjakāni ākiṇṇāni":
        f"{SEYY} ယောက်ျား၏ ပေါင်ခွင်၌ အမျိုးမျိုးသော စားဖွယ်တို့ ပြန့်ကျဲ ထည့်ထား၏",
    "tilā taṇḍulā [tilataṇḍulā (ka.) a. ni. 3.30] modakā badarā.": f"နှမ်း{C} ဆန် ⟦0⟧{C} မုန့်လုံး{C} ဆီးသီးတို့ ဖြစ်၏{END}",
    "So tamhā āsanā vuṭṭhahanto satisammosā pakireyya.":
        f"ထိုယောက်ျားသည် ထိုနေရာမှ ထသောအခါ သတိလစ်၍ ထိုစားဖွယ်တို့ကို ဖိတ်ကျစေရာ၏{END}",
    f"Evamevaṃ idhekacco puggalo {GOES_P}": f"{EVAM} {IDHA} {GOES_PLAIN}{END}",
    f"Vuṭṭhito ca kho tamhā āsanā {_NEVA_ADIPI}": f"{ROSE_CA} {NO_MANASI}",
    f"Vuṭṭhitopi tamhā āsanā {_ADIPI}.": f"{ROSE_PI} {YES_MANASI}{END}",
    f"Vuṭṭhitopi tamhā āsanā {_ADIPI}": f"{ROSE_PI} {YES_MANASI}",
    "Seyyathāpi nāma kumbho ukkujjo tatra udakaṃ āsittaṃ saṇṭhāti, no vivaṭṭati; evamevaṃ idhekacco puggalo ārāmaṃ "
    "gantā honti abhikkhaṇaṃ bhikkhūnaṃ santike dhammassavaṇāya.":          # «honti»: source slip
        f"{SEYY} လှန်ထားသော အိုး၌ လောင်းထည့်သော ရေသည် တည်နေ၏{C} မစီးကျသွားသကဲ့သို့{C} {EVAM} {IDHA} "
        f"{GOES_PLAIN}{END}",
    # ^4-110 … ^4-112
    "Sotāpannasakadāgāmino": f"{N['sotāpanno']}နှင့် {N['sakadāgāmī']}တို့",
    "Anāgāmī": N["anāgāmī"],
    "Arahā": N["arahā"],
    # ^4-113 … ^4-115 the lines
    "Idhekacco puggalo abhiṇhaṃ kujjhati.": f"{IDHA} {OFTEN_ANGRY}{END}",
    "So ca khvassa kodho ciraṃ dīgharattaṃ anuseti.": f"{KODHO_OF} {LONG} ကိန်းအောင်း၏{END}",
    "So ca khvassa kodho ciraṃ dīgharattaṃ anuseti": f"{KODHO_OF} {LONG} ကိန်းအောင်း၏",
    "So ca khvassa kodho na ciraṃ dīgharattaṃ anuseti.": f"{KODHO_OF} {LONG} မကိန်းအောင်း{END}",
    "So ca khvassa kodho na ciraṃ dīgharattaṃ anuseti": f"{KODHO_OF} {LONG} မကိန်းအောင်း",
    "Seyyathāpi nāma pāsāṇe lekhā na khippaṃ lujjati vātena vā udakena vā, ciraṭṭhitikā hoti; evamevaṃ idhekacco "
    "puggalo abhiṇhaṃ kujjhati.":
        f"{SEYY} ကျောက်ပေါ်ရှိ အရေးအကြောင်းသည် လေကြောင့်ဖြစ်စေ{C} ရေကြောင့်ဖြစ်စေ လျင်မြန်စွာ မပျက်{C} ကြာမြင့်စွာ "
        f"တည်သကဲ့သို့{C} {EVAM} {IDHA} {OFTEN_ANGRY}{END}",
    "Seyyathāpi nāma pathaviyā [paṭhaviyā (sī. syā.)] lekhā khippaṃ lujjati vātena vā udakena vā, na ciraṭṭhitikā "
    "hoti; evamevaṃ idhekacco puggalo abhiṇhaṃ kujjhati.":
        f"{SEYY} မြေပေါ်ရှိ ⟦0⟧ အရေးအကြောင်းသည် လေကြောင့်ဖြစ်စေ{C} ရေကြောင့်ဖြစ်စေ လျင်မြန်စွာ ပျက်၏{C} ကြာမြင့်စွာ "
        f"မတည်သကဲ့သို့{C} {EVAM} {IDHA} {OFTEN_ANGRY}{END}",
    f"Idhekacco puggalo {SPOKEN_P.format(_CEVA, _CEVA, _CEVA)}.":
        f"{IDHA} {SPOKEN.format(' ⟦0⟧', ' ⟦1⟧', ' ⟦2⟧')}{END}",
    "Seyyathāpi nāma udake lekhā khippaṃ lujjati, na ciraṭṭhitikā hoti; evamevaṃ idhekacco puggalo "
    f"{SPOKEN_P.format('', '', '')}":
        f"{SEYY} ရေပေါ်ရှိ အရေးအကြောင်းသည် လျင်မြန်စွာ ပျက်၏{C} ကြာမြင့်စွာ မတည်သကဲ့သို့{C} {EVAM} {IDHA} "
        f"{SPOKEN.format('', '', '')}",
})
# ^4-116, ^4-117 the cloths
UNIQUE4.update({
    "Tayo potthakā": f"{POT} သုံးမျိုး",
    "navopi potthako dubbaṇṇo ceva hoti dukkhasamphasso ca appaggho ca, majjhimopi potthako dubbaṇṇo ceva hoti "
    "dukkhasamphasso ca appaggho ca, jiṇṇopi potthako dubbaṇṇo ceva hoti dukkhasamphasso ca appaggho ca.":
        f"{f'{C} '.join(f'{a} {POT}သည်လည်း {POT_Q}' for a in (NEW, MID, OLD))}{END}",
    "Jiṇṇampi potthakaṃ ukkhaliparimajjanaṃ vā karonti saṅkārakūṭe vā naṃ chaḍḍenti.":
        f"{OLD} {POT}ကိုလည်း အိုးသုတ်ဝတ် ပြုကြ၏{C} သို့မဟုတ် အမှိုက်ပုံ၌ စွန့်ပစ်ကြ၏{END}",
    "Evamevaṃ tayome potthakūpamā puggalā santo saṃvijjamānā bhikkhūsu.":
        f"{EVAM} ဤ {F.GROUP['potthakūpamā']} {PUG} {F.persons(3)}တို့သည် {SAVAKA_BH} {SANTO}{END}",
    "Navo cepi bhikkhu hoti dussīlo pāpadhammo, idamassa dubbaṇṇatāya.":
        f"{BH_NEW} {DUSS}{C} {PAPAD} ဖြစ်အံ့{C} {IDAMASSA.format(UGLY)}",
    "Majjhimo cepi bhikkhu hoti…pe… thero cepi bhikkhu hoti dussīlo pāpadhammo, idamassa dubbaṇṇatāya.":
        f"{BH_MID}… {BH_OLD} {DUSS}{C} {PAPAD} ဖြစ်အံ့{C} {IDAMASSA.format(UGLY)}",
    "Seyyathāpi so potthako dubbaṇṇo, tathūpamo ayaṃ puggalo.": f"ထို{POT}သည် {UGLY}သကဲ့သို့{C} {TATHUPAMA}",
    "Ye kho panassa sevanti bhajanti payirupāsanti diṭṭhānugatiṃ āpajjanti, tesaṃ taṃ hoti dīgharattaṃ ahitāya "
    "dukkhāya.": FOLLOW.format(HARM),
    "Idamassa dukkhasamphassatāya.": IDAMASSA.format(PAINF),
    "Seyyathāpi so potthako dukkhasamphasso, tathūpamo ayaṃ puggalo.": f"ထို{POT}သည် {PAINF}သကဲ့သို့{C} {TATHUPAMA}",
    "Yesaṃ kho pana so paṭiggaṇhāti cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāraṃ, tesaṃ taṃ na "
    "mahapphalaṃ hoti na mahānisaṃsaṃ.": ACCEPT.format("", "", NOFRUIT),
    "Idamassa appagghatāya.": IDAMASSA.format(CHEAP),
    "Seyyathāpi so potthako appaggho, tathūpamo ayaṃ puggalo.": f"ထို{POT}သည် {CHEAP}သကဲ့သို့{C} {TATHUPAMA}",
    "Evarūpo ce thero bhikkhu saṅghamajjhe bhaṇati.": f"ဤသို့ သဘောရှိသော ထေရ် ရဟန်းသည် သံဃာ့အလယ်၌ ပြောဆိုအံ့{END}",
    "Tamenaṃ bhikkhū evamāhaṃsu": "ထိုရဟန်းကို ရဟန်းတို့က ဤသို့ ဆိုကြ၏",
    '"kiṃ nu kho tuyhaṃ bālassa abyattassa bhaṇitena, tvampi nāma bhaṇitabbaṃ maññasī"ti!':
        f"{BALASSA}{C} သင်ပင်လျှင် ပြောဆိုထိုက်သည်ဟု ထင်သလော”ဟု{END}",
    "So kupito anattamano tathārūpiṃ vācaṃ nicchāreti yathārūpāya vācāya saṅgho taṃ ukkhipati, saṅkārakūṭeva naṃ "
    "potthakaṃ.":
        f"ထိုရဟန်းသည် အမျက်ထွက်၍ စိတ်မနှစ်သိမ့်ဘဲ အကြင် စကားကြောင့် သံဃာက ထိုရဟန်းကို နှင်ထုတ်ရာ၏{C} ထိုသို့ "
        f"သဘောရှိသော စကားကို ထုတ်ဖော် ပြောဆို၏{C} အမှိုက်ပုံ၌ {POT}ကို စွန့်ပစ်သကဲ့သို့ပင်{END}",
    "Ime tayo potthakūpamā puggalā santo saṃvijjamānā bhikkhūsu.":
        f"ဤ {F.GROUP['potthakūpamā']} {PUG} {F.persons(3)}တို့သည် {SAVAKA_BH} {SANTO}{END}",
    "Tīṇi kāsikavatthāni": f"{KAS} သုံးမျိုး",
    "navampi kāsikavatthaṃ vaṇṇavantañceva hoti sukhasamphassañca mahagghañca, majjhimampi kāsikavatthaṃ "
    "vaṇṇavantañceva hoti sukhasamphassañca mahagghañca, jiṇṇampi kāsikavatthaṃ vaṇṇavantañceva hoti "
    "sukhasamphassañca mahagghañca.": f"{f'{C} '.join(f'{a} {KAS}သည်လည်း {KAS_Q}' for a in (NEW, MID, OLD))}{END}",
    "Jiṇṇampi kāsikavatthaṃ ratanapaliveṭhanaṃ vā karonti gandhakaraṇḍake vā naṃ nikkhipanti.":
        f"{OLD} {KAS}ကိုလည်း ရတနာ ထုပ်ရာ အဝတ် ပြုကြ၏{C} သို့မဟုတ် နံ့သာ ဘူး၌ ထည့်ထားကြ၏{END}",
    "Evamevaṃ tayome kāsikavatthūpamā puggalā santo saṃvijjamānā bhikkhūsu.":
        f"{EVAM} ဤ {F.GROUP['kāsikavatthūpamā']} {PUG} {F.persons(3)}တို့သည် {SAVAKA_BH} {SANTO}{END}",
    "Navo cepi bhikkhu hoti sīlavā kalyāṇadhammo, idamassa suvaṇṇatāya.":
        f"{BH_NEW} {SILAVA}{C} {KALD} ဖြစ်အံ့{C} {IDAMASSA.format(FAIR)}",
    "Majjhimo cepi bhikkhu…pe… thero cepi bhikkhu hoti sīlavā kalyāṇadhammo, idamassa suvaṇṇatāya.":
        f"{BH_MID}… {BH_OLD} {SILAVA}{C} {KALD} ဖြစ်အံ့{C} {IDAMASSA.format(FAIR)}",
    "Seyyathāpi taṃ kāsikavatthaṃ vaṇṇavantaṃ, tathūpamo ayaṃ puggalo.": f"ထို{KAS}သည် {FAIR}သကဲ့သို့{C} {TATHUPAMA}",
    "Ye kho panassa sevanti bhajanti payirupāsanti diṭṭhānugatiṃ āpajjanti, tesaṃ taṃ hoti dīgharattaṃ hitāya "
    "sukhāya.": FOLLOW.format(GOOD),
    "Idamassa sukhasamphassatāya.": IDAMASSA.format(PLEAS),
    "Seyyathāpi taṃ kāsikavatthaṃ sukhasamphassaṃ, tathūpamo ayaṃ puggalo.":
        f"ထို{KAS}သည် {PLEAS}သကဲ့သို့{C} {TATHUPAMA}",
    "Yesaṃ kho pana so [yesaṃ kho pana (sabbattha) a. ni. 3.100] paṭiggaṇhāti [patigaṇhāti (sī.) rūpasiddhiṭīkāya "
    "pana sameti] cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāraṃ, tesaṃ taṃ mahapphalaṃ hoti "
    "mahānisaṃsaṃ.": ACCEPT.format(" ⟦0⟧", " ⟦1⟧", FRUIT),
    "Yesaṃ kho pana so paṭiggaṇhāti cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāraṃ, tesaṃ taṃ mahapphalaṃ "
    "hoti mahānisaṃsaṃ.": ACCEPT.format("", "", FRUIT),
    "Idamassa mahagghatāya.": IDAMASSA.format(DEAR),
    "Seyyathāpi taṃ kāsikavatthaṃ mahagghaṃ, tathūpamo ayaṃ puggalo.": f"ထို{KAS}သည် {DEAR}သကဲ့သို့{C} {TATHUPAMA}",
    "Evarūpo ce thero bhikkhu saṅghamajjhe bhaṇati, tamenaṃ bhikkhū evamāhaṃsu":
        f"ဤသို့ သဘောရှိသော ထေရ် ရဟန်းသည် သံဃာ့အလယ်၌ ပြောဆိုအံ့{C} ထိုရဟန်းကို ရဟန်းတို့က ဤသို့ ဆိုကြ၏",
    '"appasaddā āyasmanto hotha, thero bhikkhu dhammañca vinayañca bhaṇatī"ti.':
        f"“အသျှင်တို့ အသံ ငြိမ်ကြလော့{C} ထေရ် ရဟန်းသည် တရားကိုလည်း ဝိနည်းကိုလည်း ဟောပြောနေ၏”ဟု{END}",
    "Tassa taṃ vacanaṃ ādheyyaṃ gacchati, gandhakaraṇḍakeva naṃ kāsikavatthaṃ.":
        f"ထိုရဟန်း၏ ထိုစကားသည် လက်ခံ မှတ်သားထိုက်သော စကား ဖြစ်လာ၏{C} နံ့သာ ဘူး၌ {KAS}ကို ထည့်ထားသကဲ့သို့ပင်{END}",
    "Ime tayo kāsikavatthūpamā puggalā santo saṃvijjamānā bhikkhūsu.":
        f"ဤ {F.GROUP['kāsikavatthūpamā']} {PUG} {F.persons(3)}တို့သည် {SAVAKA_BH} {SANTO}{END}",
})
wit("saṅghamajjhe", "သံဃာ့အလယ်၌")
wit("āyasmanto", "အသျှင်တို့")
# ^4-118 … ^4-120 measurable
UNIQUE4.update({
    "Idhekacco puggalo uddhato hoti unnaḷo capalo mukharo vikiṇṇavāco muṭṭhassati asampajāno asamāhito "
    "vibbhantacitto pākaṭindriyo":
        f"{IDHA} ယောက်ယက်ခတ်သူ {COP}{C} ဘဝင်မြင့်သူ{C} ပေါ့ပျက်သူ{C} စကားများသူ{C} ရှုပ်ပွေစွာ ပြောတတ်သူ{C} "
        f"{N['muṭṭhassati']}{C} {N['asampajāno']}{C} စိတ် မတည်ကြည်သူ{C} စိတ် ပျံ့လွင့်သူ{C} အာရုံခံ အင်္ဂါတို့ "
        f"ပွင့်ဟနေသူ {COP}",
    "Idhekacco puggalo anuddhato hoti anunnaḷo acapalo amukharo avikiṇṇavāco upaṭṭhitassati sampajāno samāhito "
    "ekaggacitto saṃvutindriyo":
        f"{IDHA} မယောက်ယက်ခတ်သူ {COP}{C} ဘဝင် မမြင့်သူ{C} မပေါ့ပျက်သူ{C} စကား မများသူ{C} ရှုပ်ပွေစွာ မပြောတတ်သူ{C} "
        f"{N['upaṭṭhitassati']}{C} {N['sampajāno']}{C} စိတ် တည်ကြည်သူ{C} စိတ် တစ်ခုတည်း၌ စူးစိုက်သူ{C} "
        f"အာရုံခံ အင်္ဂါတို့ကို စောင့်စည်းသူ {COP}",
    # ^4-121 … ^4-126 to be followed or not
    "Idhekacco puggalo hīno hoti sīlena samādhinā paññāya.": f"{IDHA} {SSP} ယုတ်ညံ့သူ {COP}{END}",
    "Evarūpo puggalo na sevitabbo na bhajitabbo na payirupāsitabbo, aññatra anuddayā aññatra anukampā.":
        f"{EVARUPO} {SEV_NO}{C} သနားကြင်နာခြင်းကြောင့်မှလွဲ၍{C} စာနာ ထောက်ထားခြင်းကြောင့်မှလွဲ၍{END}",
    "Idhekacco puggalo sadiso hoti sīlena samādhinā paññāya.": f"{IDHA} {SSP} တူညီသူ {COP}{END}",
    "Evarūpo puggalo sevitabbo bhajitabbo payirupāsitabbo.": f"{EVARUPO} {SEV_YES}{END}",
    "evarūpo puggalo sevitabbo bhajitabbo payirupāsitabbo.": f"{EVARUPO} {SEV_YES}{END}",
    '"Sīlasāmaññagatānaṃ sataṃ sīlakathā ca no bhavissati, sā ca no phāsu bhavissati, sā ca no pavattinī bhavissati; '
    'samādhisāmaññagatānaṃ sataṃ samādhikathā ca no bhavissati, sā ca no phāsu bhavissati, sā ca no pavattinī '
    '[pavattanī (sī.) a. ni. 3.26] bhavissati; paññāsāmaññagatānaṃ sataṃ paññākathā ca no bhavissati, sā ca no phāsu '
    'bhavissati, sā ca no pavattinī bhavissatī"ti.':
        "“" + f"{C} ".join(
            f"{x} တူညီမှုသို့ ရောက်ကြသော ငါတို့အား {x}နှင့် စပ်သော စကားသည်လည်း ဖြစ်လိမ့်မည်{C} ထိုစကားသည်လည်း "
            f"ငါတို့အား ချမ်းသာ ဖြစ်လိမ့်မည်{C} ထိုစကားသည်လည်း ငါတို့အား ဆက်လက် ဖြစ်ပွားနေလိမ့်မည်{t}"
            for x, t in (("သီလ", ""), ("သမာဓိ", " ⟦0⟧"), ("ပညာ", ""))) + f"”ဟူ၍{END}",
    "Tasmā evarūpo puggalo sevitabbo bhajitabbo payirupāsitabbo.": f"{TASMA} {EVARUPO} {SEV_YES}{END}",
    "Idhekacco puggalo adhiko hoti sīlena samādhinā paññāya.": f"{IDHA} {SSP} သာလွန်သူ {COP}{END}",
    "Evarūpo puggalo sakkatvā garuṃ katvā sevitabbo bhajitabbo payirupāsitabbo.":
        f"{EVARUPO} ရိုသေ၍ လေးစားကာ {SEV_YES}{END}",
    '"Aparipūraṃ vā sīlakkhandhaṃ paripūressāmi, paripūraṃ vā sīlakkhandhaṃ tattha tattha paññāya anuggahessāmi; '
    'aparipūraṃ vā samādhikkhandhaṃ paripūressāmi, paripūraṃ vā samādhikkhandhaṃ tattha tattha paññāya '
    'anuggahessāmi; aparipūraṃ vā paññākkhandhaṃ paripūressāmi, paripūraṃ vā paññākkhandhaṃ tattha tattha paññāya '
    'anuggahessāmī"ti.':
        "“" + f"{C} ".join(
            f"မပြည့်စုံသေးသော {x} {F.KH}ကိုဖြစ်စေ ပြည့်စုံအောင် ပြုမည်{C} ပြည့်စုံပြီးသော {x} {F.KH}ကိုဖြစ်စေ ထိုထို "
            f"အရာ၌ ပညာဖြင့် ချီးမြှင့် ထောက်ပံ့မည်" for x in ("သီလ", "သမာဓိ", "ပညာ")) + f"”ဟူ၍{END}",
    "Tasmā evarūpo puggalo sakkatvā garuṃ katvā sevitabbo bhajitabbo payirupāsitabbo.":
        f"{TASMA} {EVARUPO} ရိုသေ၍ လေးစားကာ {SEV_YES}{END}",
    "Evarūpo puggalo jigucchitabbo na sevitabbo na bhajitabbo na payirupāsitabbo.":
        f"{EVARUPO} စက်ဆုပ်အပ်၏{C} {SEV_NO}{END}",
    "Kiñcāpi evarūpassa puggalassa na diṭṭhānugatiṃ āpajjati, atha kho naṃ pāpako kittisaddo abbhuggacchati":
        f"{NOFOLLOW} {FAME.format('ယုတ်မာသော')}",
    '"pāpamitto purisapuggalo pāpasahāyo pāpasampavaṅko"ti.': PAPAM_Q,
    '"pāpamitto purisapuggalo pāpasahāyo pāpasampavaṅko"ti!': PAPAM_Q,
    "Seyyathāpi nāma ahi gūthagato kiñcāpi na ḍaṃsati, atha kho naṃ makkheti; evamevaṃ kiñcāpi evarūpassa puggalassa "
    "na diṭṭhānugatiṃ āpajjati, atha kho naṃ pāpako kittisaddo abbhuggacchati":
        f"{SEYY} မစင်ထဲ၌ ရှိသော မြွေသည် မကိုက်သော်လည်း လူကို ပေကျံစေသကဲ့သို့{C} {EVAM} {NOFOLLOW} "
        f"{FAME.format('ယုတ်မာသော')}",
    "Tasmā evarūpo puggalo jigucchitabbo na sevitabbo na bhajitabbo na payirupāsitabbo.":
        f"{TASMA} {EVARUPO} စက်ဆုပ်အပ်၏{C} {SEV_NO}{END}",
    '"Akkoseyyapi maṃ paribhāseyyapi maṃ anatthampi me kareyyā"ti!':
        f"“ငါ့ကို ဆဲရေးလည်း ဆဲရေးရာ၏{C} ငါ့ကို ကဲ့ရဲ့ ပြောဆိုလည်း ပြောဆိုရာ၏{C} ငါ့အား မကောင်းမှုကိုလည်း ပြုရာ၏”ဟူ၍{END}",
    "Tasmā evarūpo puggalo ajjhupekkhitabbo na sevitabbo na bhajitabbo na payirupāsitabbo.":
        f"{TASMA} {EVARUPO} လျစ်လျူရှုအပ်၏{C} {SEV_NO}{END}",
    "Idhekacco puggalo sīlavā hoti kalyāṇadhammo": f"{IDHA} {SIL_HOTI}",
    "Kiñcāpi evarūpassa puggalassa na diṭṭhānugatiṃ āpajjati, atha kho naṃ kalyāṇo kittisaddo abbhuggacchati":
        f"{NOFOLLOW} {FAME.format('ကောင်းမွန်သော')}",
    '"kalyāṇamitto purisapuggalo kalyāṇasahāyo kalyāṇasampavaṅko"ti!': KALYM_Q,
    # ^4-127 … ^4-129
    "ime vuccanti puggalā sīlesu paripūrakārino, samādhismiṃ mattaso kārino, paññāya mattaso kārino.":
        f"ဤ{PUG_PL}ကို {N['sīlesu paripūrakārī, samādhismiṃ mattaso kārī, paññāya mattaso kārī']}ဟု ခေါ်သည်{END}",
    "ayaṃ vuccati puggalo sīlesu ca paripūrakārī, samādhismiñca paripūrakārī, paññāya mattaso kārī.":
        f"ဤ{PUG}ကို {N['sīlesu ca paripūrakārī, samādhismiñca paripūrakārī, paññāya mattaso kārī']}ဟု ခေါ်သည်{END}",
    "ayaṃ vuccati puggalo sīlesu ca paripūrakārī, samādhismiñca paripūrakārī, paññāya ca paripūrakārī.":
        f"ဤ{PUG}ကို {N['sīlesu ca paripūrakārī, samādhismiñca paripūrakārī, paññāya ca paripūrakārī']}ဟု ခေါ်သည်{END}",
})
# ^4-130, ^4-131 the teachers
_T = f"{TEACHER}သည်"


def _pk(obj, ca, yes):
    return f"{obj}{'လည်း' if ca else ''} {PKN} {PANNAP if yes else NO_PANNAP}"


_T1 = f"{_pk(KAMA_P, 0, 1)}{C} {_pk(RUPA_P, 0, 0)}{C} {_pk(VED_P, 0, 0)}"
_T2 = f"{_pk(KAMA_P, 1, 1)}{C} {_pk(RUPA_P, 1, 1)}{C} {_pk(VED_P, 0, 0)}"
_T3 = f"{_pk(KAMA_P, 1, 1)}{C} {_pk(RUPA_P, 1, 1)}{C} {_pk(VED_P, 1, 1)}"
_ATT = f"{ATTA}ကို {SACCATO}"
_A1 = f"{W['ditthe_dhamme']} {_ATT} {PANNAP}{C} {NEXT}လည်း {_ATT} {PANNAP}"
_A2 = f"{W['ditthe_dhamme']} {_ATT} {PANNAP}{C} သို့သော် {NEXT}ကား {_ATT} {NO_PANNAP}"
_A3 = f"{W['ditthe_dhamme']} {_ATT} {NO_PANNAP}{C} {NEXT}လည်း {_ATT} {NO_PANNAP}"
_TP1 = ("kāmānaṃ pariññaṃ paññapeti{}, na rūpānaṃ pariññaṃ paññapeti, na vedanānaṃ pariññaṃ paññapeti")
_TP2 = "kāmānañca pariññaṃ paññapeti, rūpānañca pariññaṃ paññapeti, na vedanānaṃ pariññaṃ paññapeti"
_TP3 = "kāmānañca pariññaṃ paññapeti, rūpānañca pariññaṃ paññapeti, vedanānañca pariññaṃ paññapeti"
_AP1 = ("diṭṭhe ceva dhamme attānaṃ saccato thetato paññapeti, abhisamparāyañca attānaṃ saccato thetato paññapeti")
_AP2 = ("diṭṭhe ceva dhamme attānaṃ saccato thetato paññapeti, no ca kho abhisamparāyaṃ attānaṃ saccato thetato "
        "paññapeti")
_AP3 = ("diṭṭhe ceva dhamme attānaṃ saccato thetato na paññapeti, abhisamparāyañca attānaṃ saccato thetato na "
        "paññapeti")
_SAMMA_T = f"{W['sammasambuddha']} ဖြစ်သော {TEACHER}"


def _tatra(cl, what):
    return (f"{TATRA_T} {cl}သော အကြင် {TEACHER} ရှိ၏{C} ထို{TEACHER}ကို {what}{SEEN}")


UNIQUE4.update({
    f"Idhekacco satthā {_TP1.format(' [paññāpeti (sī. syā.)]')}.":
        f"ဤလောက၌ အချို့သော {_T} {_T1.replace(PANNAP, PANNAP + ' ⟦0⟧', 1)}{END}",
    f"Idha panekacco satthā {_TP2}.": f"တစ်ဖန် ဤလောက၌ အချို့သော {_T} {_T2}{END}",
    f"Idha panekacco satthā {_TP3}.": f"တစ်ဖန် ဤလောက၌ အချို့သော {_T} {_T3}{END}",
    f"Tatra yvāyaṃ satthā {_TP1.format('')}, rūpāvacarasamāpattiyā lābhī satthā tena daṭṭhabbo.":
        _tatra(_T1[:-1] if _T1.endswith("၏") else _T1, f"{RUPAV_SAMAP}ကို ရရှိသော {TEACHER}"),
    f"Tatra yvāyaṃ satthā {_TP2}, arūpāvacarasamāpattiyā lābhī satthā tena daṭṭhabbo.":
        _tatra(_T2, f"{ARUPAV_SAMAP}ကို ရရှိသော {TEACHER}"),
    f"Tatra yvāyaṃ satthā {_TP3}, sammāsambuddho satthā tena daṭṭhabbo.": _tatra(_T3[:-1], _SAMMA_T),
    "Ime tayo satthāro.": f"ဤသူတို့ကား {TEACHER} {F.persons(3)} ဖြစ်ကြ၏{END}",
    f"Idhekacco satthā {_AP1}.": f"ဤလောက၌ အချို့သော {_T} {_A1}{END}",
    f"Idha panekacco satthā {_AP2}.": f"တစ်ဖန် ဤလောက၌ အချို့သော {_T} {_A2}{END}",
    f"Idha panekacco satthā {_AP3}.": f"တစ်ဖန် ဤလောက၌ အချို့သော {_T} {_A3}{END}",
    f"Tatra yvāyaṃ satthā {_AP1}, sassatavādo satthā tena daṭṭhabbo.":
        _tatra(_A1[:-1], f"{SASSATA} ရှိသော {TEACHER}"),
    f"Tatra yvāyaṃ satthā {_AP2}, ucchedavādo satthā tena daṭṭhabbo.": _tatra(_A2, f"{UCCHEDA} ရှိသော {TEACHER}"),
    f"Tatra yvāyaṃ satthā {_AP3}, sammāsambuddho satthā tena daṭṭhabbo.": _tatra(_A3, _SAMMA_T),
    "Ime aparepi tayo satthāro.": f"ဤသူတို့ကား နောက်ထပ် {TEACHER} {F.persons(3)} ဖြစ်ကြ၏{END}",
})
F.PLURAL["kāmesu ca bhavesu ca avītarāgā"] = "kāmesu ca bhavesu ca avītarāgo"

# ===================================================================================== install the tables
for _t, _d in ((F.SENT, UNIQUE3), (F.SENT, UNIQUE4)):
    for _k, _v in _d.items():
        _v = unicodedata.normalize("NFC", _v)
        if _k in _t and _t[_k] != _v:
            raise SystemExit("table conflict: " + _k[:80])
        _t[_k] = _v


# ===================================================================================== generator
def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def chapter(name, misses=None):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    done = []
    for i, line in enumerate(lines):
        try:
            done.append(F.translate_line(line))
        except F.Miss as e:
            if misses is not None:
                misses.append(f"{name}:{i + 1}: {e}")
                done.append("")
                continue
            print(f"STOP {name} line {i + 1}: {e}\n  {line[:200]}")
            return False
    if misses is not None:
        return not misses
    write(name, "\n".join(done).rstrip("\n") + "\n")
    return True


def units_missing(name):
    """Every unit of the chapter no frame / table matches (one Miss per unit, not only the first of a line)."""
    out = []
    for line in (PALI / name).read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        m = F.ID_RE.search(line)
        body = (line[:m.start()] if m else line).strip()
        try:
            F.line_my(body)
            continue
        except F.Miss:
            pass
        for part in F.SPLIT_RE.split(body):
            if not part or part.isspace() or part == " – ":
                continue
            try:
                F.unit_my(part)
            except F.Miss as e:
                out.append(f"{name}: {e}")
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    names = args or NAMES_OUT
    if "--misses" in sys.argv:
        ms = []
        for n in names:
            ms += units_missing(n)
        print("\n".join(ms) or "no misses")
        print(f"{len(ms)} misses")
        sys.exit(0)
    ok = True
    for n in names:
        ok = chapter(n) and ok
    sys.exit(0 if ok else 1)
