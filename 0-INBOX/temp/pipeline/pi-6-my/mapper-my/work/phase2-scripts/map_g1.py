"""pi-6 Burmese keyword mapping, PHASE 2, group G1 (2-02 … 5-03).

Imports the shared module map6_rules.py (NOT edited) and holds only the G1 chapter tables and the new context
functions of the group. Maps the G1 chapters in chapter order, writes <ch>.mapped.md, runs the three checks of the
phase-1 brief per chapter (keyword preservation `bad []`, presence, no «, » / «၊» / « / » in a value) and the S1
review (every use whose module-only value comes from the stem fallback: kept or corrected).
Run: /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 map_g1.py [ch …] [--pairs]
Notes: notes-g1.md.
"""
import re
import sys
import pathlib
import collections

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map6_rules as R          # noqa: E402

NONE = R.NONE
G1 = ["2-02-khandhayamaka", "3-01-ayatanayamaka", "3-02-ayatanayamaka", "3-03-ayatanayamaka",
      "3-04-ayatanayamaka", "3-05-ayatanayamaka", "3-06-ayatanayamaka", "4-dhatuyamaka",
      "5-01-saccayamaka", "5-02-saccayamaka", "5-03-saccayamaka"]


# =====================================================================================================================
# context functions of the group (FUNCS_G1; a table value «@name» calls one)
# =====================================================================================================================
_FREE_RUPA = re.compile("ရုပ်(?!မရှိ|ဘုံ| မရှိ| ရှိလျက်| အစုအဝေး)")


def f_rupam_g1(kw, pali, my):
    """MODULE OVERRIDE of f_rupam (rule 11, one sense per segment): in the āyatana / dhātu padasodhana «rūpaṃ
    rūpāyatanaṃ?» the text has «ရုပ်သည် အဆင်းအရောင် အာရုံခံ နယ်ပယ် …»: the bare rūpaṃ is «ရုပ်»; «အဆင်းအရောင်» is the
    word of the keyword rūpāyatanaṃ / rūpadhātu, not of rūpaṃ. Where the text has a free «ရုပ်» (not inside
    «ရုပ်မရှိသော ဘုံ / ရုပ်ဘုံ / ရုပ် အစုအဝေး / ရုပ် ရှိလျက်»), «ရုပ်»; else the module's value."""
    if _FREE_RUPA.search(my):
        return "ရုပ်"
    return R.f_rupam(kw, pali, my)


# editorial notes: the sections «yassaka / yatthaka / yassayatthaka» (harmonise-notes ch3 / ch2-02-4-5: «“အကြင်သူအား” /
# “အကြင်နေရာ၌” / “အကြင်သူအား အကြင်နေရာ၌” အပိုင်း»)
AKA_Q = {"yassa": "အကြင်သူအား", "yattha": "အကြင်နေရာ၌", "yassayattha": "အကြင်သူအား အကြင်နေရာ၌"}
_AKA = re.compile(r"^(yassa ?yattha|yassa|yattha)k(aṃ|am|ā|ānaṃ|e|a|o)(pi)?(sadis(aṃ|o|ā))?$")


def f_aka(kw, pali, my):
    """yassakaṃ / yatthakampi / yassayatthake(pi) / yatthakānaṃ … = «Q အပိုင်း» (the cited question word inside the
    quotation keeps its «အား / ၌», rule 1: inner particles stay; the final «၌ / တွင် / ကို / များ» go; the «လည်း» of -pi
    is not part of the keyword, Q4); X-sadisaṃ = «Q အပိုင်းနှင့် တူညီသည်» (rule 4; the text's adverbial «တူညီအောင်»
    where it has that, «sadisaṃ kātabbaṃ»). A keyword that stands only inside a Roman-script variant = (no direct
    equivalent) (pi-3 M2)."""
    m = _AKA.match(R.low(kw))
    if not m:
        return "@prior"
    if not R.pali_has(kw, pali):
        return NONE
    q = AKA_Q[m.group(1).replace(" ", "")]
    v = q + " အပိုင်း"
    if m.group(4):
        for end in ("နှင့် တူညီသည်", "နှင့် တူညီအောင်"):
            if R.presence(v + end, my)[0] and R.phrase_ok(v + end, re.sub("[“”]", "", my)):
                return v + end
        return v + "နှင့် တူညီသည်"
    return v


VIPP = {"taṇhā": "တပ်မက်မှု", "magga": "မဂ်"}
_VIPP = re.compile(r"^((?:taṇhā|magga)vippayutta){1,2}citt(e|assa|aṃ|ānaṃ)$")
MOMENT = {"uppādakkhaṇe": "ဖြစ်ခြင်း ခဏ", "bhaṅgakkhaṇe": "ပြိုပျက်ခြင်း ခဏ"}


def citta_value(w):
    """X-vippayuttacitta «Xနှင့် ကင်းကွာသော စိတ်» (pi-1 rule 3 «…နှင့် ကင်းကွာသော»; notes-ch2-02-4-5); two members
    «Aနှင့် ကင်းကွာ၍ Bနှင့် ကင်းကွာသော စိတ်» (the text's absolutive, pi-1 «…၍»); upapatticitta «ပြန်လည် ဖြစ်ပေါ်ခြင်း
    စိတ်» (notes-ch2-02-4-5)."""
    w = R.low(w)
    if re.match(r"^upapatticitt(assa|e|aṃ)$", w):
        return "ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်"
    if not _VIPP.match(w):
        return None
    mem = re.findall(r"(taṇhā|magga)vippayutta", w)
    parts = [VIPP[x] + "နှင့် ကင်းကွာ" for x in mem]
    return " ".join(p + "၍" for p in parts[:-1]) + (" " if len(parts) > 1 else "") + parts[-1] + "သော စိတ်"


def f_citta(kw, pali, my):
    """«X-vippayuttacittassa uppādakkhaṇe / bhaṅgakkhaṇe» = «Xနှင့် ကင်းကွာသော စိတ်၏ ဖြစ်ခြင်း ခဏ» (harmonise B1:
    «… ခဏ» without the final «၌»; the inner «၏» stays, rule 1); X-vippayuttacitte (vattamāne) = the citta value
    (rule 1: the final «…» of the locative absolute goes; vattamāne is its own keyword)."""
    ws = kw.split()
    c = citta_value(ws[0])
    if c is None:
        return "@prior"
    if len(ws) == 2 and R.low(ws[1]) in MOMENT:
        return c + "၏ " + MOMENT[R.low(ws[1])]
    return c


SAKA = {"cakkhuk": "မျက်စိ", "sotak": "နား", "ghānak": "နှာခေါင်း", "jivhak": "လျှာ", "kāyak": "ကိုယ်",
        "rūpak": "ရုပ်", "cittak": "စိတ်"}
_SAKA = re.compile(r"^(sa|a)(cakkhuk|sotak|ghānak|jivhak|kāyak|rūpak|cittak)(ānaṃ|ā|assa|o|aṃ|e)$")


def f_saka(kw, pali, my):
    """sa-X-ka / a-X-ka persons (frame-coverage «Whole-book dry run»; notes-ch3: the text «X ရှိလျက် / X မရှိဘဲ» before
    the participle) = the adjective «X ရှိသော / X မရှိသော» (pi-1 rule 3; Sahetukaṃ «အမြစ် ရှိသော» / Ahetukaṃ «အမြစ်
    မရှိသော»; the text's «ရှိလျက် / မရှိဘဲ» by the ending rule, pi-2 N11 «လျက် / ဘဲ»). arūpaka = «ရုပ် မရှိသော» (the
    person without matter, not the plane «ရုပ်မရှိသော ဘုံ»)."""
    m = _SAKA.match(R.low(kw))
    if not m:
        return "@prior"
    x = SAKA[m.group(2)]
    return x + (" ရှိသော" if m.group(1) == "sa" else " မရှိသော")


def f_nayatana(kw, pali, my):
    """nāyatanā / nāyatanaṃ / nāyatananti (na + āyatana, one Pāli word; pi-1 / pi-2 fused negatives nariya «အရိယာ
    မဟုတ်သော», nattā «အတ္တ မဟုတ်သော»): the subject «အာရုံခံ နယ်ပယ်တို့ မဟုတ်သော အရာ» = «အာရုံခံ နယ်ပယ် … မဟုတ်သော» (rule
    3; the inner plural «တို့» outside the value, rule 10 « … »); the predicate «… အာရုံခံ နယ်ပယ် မဟုတ်သလော / မဟုတ်»
    = «အာရုံခံ နယ်ပယ် မဟုတ်» (pi-1 rule 5 «X မဟုတ်»; Q5: without «သည်»)."""
    w = R.low(kw)
    subj = "အာရုံခံ နယ်ပယ် … မဟုတ်သော"
    pred = "အာရုံခံ နယ်ပယ် မဟုတ်"
    if w == "nāyatanā":
        if "အာရုံခံ နယ်ပယ်တို့ မဟုတ်သော" in my:
            return subj
        return "အာရုံခံ နယ်ပယ် မဟုတ်သော" if "အာရုံခံ နယ်ပယ် မဟုတ်သော" in my else pred
    return pred if pred in my else subj


FUNCS_G1 = {
    "rupam_g1": f_rupam_g1, "aka": f_aka, "citta": f_citta, "saka": f_saka, "nayatana": f_nayatana,
}


# =====================================================================================================================
# group table (every G1 chapter): only what the module does not settle or settles wrongly (notes-g1.md)
# =====================================================================================================================
UPNI = {"uppād": "ဖြစ်ပေါ်ခြင်း", "nirodh": "ချုပ်ငြိမ်းခြင်း", "uppādanirodh": "ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်း",
        "pariññā": "ပိုင်းခြား သိခြင်း"}
VARA = "အလိုက် ဖော်ပြချက်"

T_ALL = {
    # rūpaṃ and its R1 forms (module override, f_rupam_g1)
    "rūpaṃ": "@rupam_g1", "Rūpaṃ": "@rupam_g1", "rūpanti": "@rupam_g1", "Rūpañca": "@rupam_g1",
    "rūpañceva": "@rupam_g1",
    # yattha «where» = «အကြင်နေရာ» (the text's «အကြင်နေရာ၌», rule 1: the «၌» goes; the place noun is yattha's own word)
    "yattha": "အကြင်နေရာ", "Yattha": "အကြင်နေရာ",
    # the vāras named inside a sentence or a note (R6 reads only heading lines): «Xအလိုက် ဖော်ပြချက်» (rule 7, the
    # text's whole name; rule 1: the «၌ / ၌လည်း» of the locative go); the bare uppāde / nirodhe «X» (Q4: the «လည်း» of pi)
    "Uppādavāro": UPNI["uppād"] + VARA, "uppādavāre": UPNI["uppād"] + VARA, "Uppādavārepi": UPNI["uppād"] + VARA,
    "uppādavārepi": UPNI["uppād"] + VARA,
    "Nirodhavāro": UPNI["nirodh"] + VARA, "nirodhavāre": UPNI["nirodh"] + VARA, "nirodhavārepi": UPNI["nirodh"] + VARA,
    "Uppādanirodhavāro": UPNI["uppādanirodh"] + VARA, "uppādanirodhavārepi": UPNI["uppādanirodh"] + VARA,
    "Pariññāvāro": UPNI["pariññā"] + VARA,
    "uppādanirodhepi": UPNI["uppādanirodh"],
    "vāresu": "ဖော်ပြချက်",                                     # «ဖော်ပြချက် သုံးပါးလုံး၌» (tīsupi vāresu)
    "vārasaṅkhepo": "ဖော်ပြချက်တို့၌ အကျဉ်း ဖော်ပြထားသည်",      # «(upari) vārasaṅkhepo» (notes-ch3; rule 1 inner «တို့၌»)
    # the editorial sections (f_aka)
    **{k: "@aka" for k in ("yassakaṃ", "Yassakampi", "yassakampi", "yassakasadisaṃ", "yatthakaṃ", "Yatthakaṃ",
                            "yatthakampi", "Yatthakampi", "yatthakā", "yatthakānaṃ", "yatthakasadisaṃ",
                            "yassayatthakampi", "Yassayatthakampi", "yassayatthakepi", "yassayatthakasadisaṃ",
                            "Yassa yatthakampi", "yassa yatthakampi", "yassa yatthake")},
    # sa-X-ka / a-X-ka persons (f_saka)
    **{k: "@saka" for k in ("sacakkhukānaṃ", "Sacakkhukānaṃ", "acakkhukānaṃ", "Acakkhukānaṃ", "sasotakānaṃ",
                            "Sasotakānaṃ", "asotakānaṃ", "arūpakānaṃ")},
    # cakka (bandhitabbaṃ) = the round «လှည့်ပတ်ခြင်း» (the text «လှည့်ပတ်ခြင်းကို … ဖွဲ့ရမည်»; as the phase-1 headings
    # «…cakkavāro = … လှည့်ပတ်ခြင်း ဖော်ပြချက်»; S1 gave «မျက်စိ», pi-2 / pi-5 «တရားစက် / စကြာ» is another sense)
    "Cakkaṃ": "လှည့်ပတ်ခြင်း", "cakkaṃ": "လှည့်ပတ်ခြင်း",
    # the kinds of «sota / gandha / rasa» that are not āyatanas (notes-ch3: «X၏ အနံ့ / X၏ အရသာ»; rule 1 inner «၏»)
    "taṇhāsotaṃ": "တပ်မက်မှု ရေစီး",
    "Sīlagandho": "သီလ၏ အနံ့", "samādhigandho": "သမာဓိ၏ အနံ့", "paññāgandho": "ပညာ၏ အနံ့",
    "Attharaso": "အနက်၏ အရသာ", "dhammaraso": "တရား၏ အရသာ", "vimuttiraso": "လွတ်မြောက်မှု၏ အရသာ",
    # na + āyatana (f_nayatana)
    "nāyatanā": "@nayatana", "nāyatanaṃ": "@nayatana", "nāyatananti": "@nayatana",
    # the past / present pairs of the note «paccuppannātītepi …» (Q4: the «လည်း» of pi goes; rule 1 the «၌»)
    "paccuppannātītepi": "ပစ္စုပ္ပန်နှင့် အတိတ်", "paccuppannānāgatepi": "ပစ္စုပ္ပန်နှင့် အနာဂတ်",
    # the chapter titles cited in a note, any case (rule 7: the title whole; the text quotes it «“…”»)
    "āyatanayamake": "အာရုံခံ နယ်ပယ်များကို အတွဲလိုက် မေးဖြေခြင်း",
    "āyatanayamakassa": "အာရုံခံ နယ်ပယ်များကို အတွဲလိုက် မေးဖြေခြင်း",
    "dhātuyamakampi": "ဓာတ်များကို အတွဲလိုက် မေးဖြေခြင်း", "dhātuyamakassa": "ဓာတ်များကို အတွဲလိုက် မေးဖြေခြင်း",
    "dhātuyamakepi": "ဓာတ်များကို အတွဲလိုက် မေးဖြေခြင်း",
    # X-sadiso «Xနှင့် တူညီသည်» (the notes' «(Saddo ghānasadiso)» «(အသံသည် နှာခေါင်းနှင့် တူညီသည်)»; rule 4)
    "ghānasadiso": "နှာခေါင်းနှင့် တူညီသည်", "ghānadhātusadisā": "နှာခေါင်း ဓာတ်နှင့် တူညီသည်",
    # ch. 5 persons and moments (notes-ch2-02-4-5; harmonise A1)
    "caññe": ("အခြားသူ", "အခြား"),                               # «မဂ်ကို ရရှိမည့် အခြားသူတို့» (P6; Itaresaṃ)
    "Abhisametāvīnaṃ": ("ထင်ထင်ရှားရှား သိမြင်ပြီးသူ", "ထင်ထင်ရှားရှား သိမြင်ပြီးသော"),
    "abhisametāvīnaṃ": ("ထင်ထင်ရှားရှား သိမြင်ပြီးသူ", "ထင်ထင်ရှားရှား သိမြင်ပြီးသော"),
    "Anabhisametāvīnaṃ": ("ထင်ထင်ရှားရှား မသိမြင်ရသေးသူ", "ထင်ထင်ရှားရှား မသိမြင်ရသေးသော"),
    "anabhisametāvīnaṃ": ("ထင်ထင်ရှားရှား မသိမြင်ရသေးသူ", "ထင်ထင်ရှားရှား မသိမြင်ရသေးသော"),
    "āpāyikānaṃ": ("အပါယ်၌ ရှိသူ", "အပါယ်၌ ရှိသော"), "Āpāyikānaṃ": ("အပါယ်၌ ရှိသူ", "အပါယ်၌ ရှိသော"),   # R5
    "aggaphalassa": "အမြတ်ဆုံး ဖိုလ်",                          # «အမြတ်ဆုံး ဖိုလ်၏» (agga- pi-2 ^2-1029; rule 1 the «၏»)
    **{k: "@citta" for k in ("taṇhāvippayuttacitte", "taṇhāvippayuttacittassa uppādakkhaṇe",
                            "Taṇhāvippayuttacittassa uppādakkhaṇe", "taṇhāvippayuttacittassa bhaṅgakkhaṇe",
                            "maggavippayuttacittassa uppādakkhaṇe", "maggavippayuttacittassa bhaṅgakkhaṇe",
                            "taṇhāvippayuttamaggavippayuttacittassa uppādakkhaṇe",
                            "taṇhāvippayuttamaggavippayuttacittassa bhaṅgakkhaṇe",
                            "maggavippayuttataṇhāvippayuttacittassa",
                            "maggavippayuttataṇhāvippayuttacittassa uppādakkhaṇe",
                            "maggavippayuttataṇhāvippayuttacittassa bhaṅgakkhaṇe",
                            "upapatticittassa uppādakkhaṇe", "upapatticittassa bhaṅgakkhaṇe")},
    # Pāli slips of the source (text inconsistencies, notes-g1): the intended word's value
    "vadanākkhandho": "ခံစားမှု အစုအဝေး",                     # vedanākkhandho (2-02 ^6-2-185)
    "sotāyananti": "နား အာရုံခံ နယ်ပယ်",                       # sotāyatananti (3-01 ^6-3-13)
    "parinibbāntānaṃ": "ပရိနိဗ္ဗာန် ပြုဆဲသူ",                    # parinibbantānaṃ (3-05 ^6-3-172, notes-ch3)
    "asaññattā": "အသညသတ် ဘုံ",                               # asaññasattā (5-02 ^6-5-76) «… ဘုံမှ စုတေဆဲသူ» (R5 plane)
    # uppajjittha rūpāyatanañca run together (3-01 ^6-3-43): both members' words, the finite verb last (Q3), « … »
    # for the «လည်း» of ca between them (Q4: «အဆင်းအရောင် အာရုံခံ နယ်ပယ်လည်း ဖြစ်ပေါ်ခဲ့သည်»)
    "uppajjittharūpāyatanañca": "အဆင်းအရောင် အာရုံခံ နယ်ပယ် … ဖြစ်ပေါ်ခဲ့သည်",
}
# per-chapter tables (none needed beyond the group table so far)
TABLES = {ch: dict(T_ALL) for ch in G1}
# per-segment overrides (sid -> {kw: value})
CTX = {
    # Pāli slip upapajjissati for uppajjissati (notes-ch3; the text «… ဖြစ်ပေါ်လိမ့်မည်»): the text's word; the module
    # assembled «ပြန်လည် ဖြစ်ပေါ်လိမ့်မည်» from chunks scattered over the segment
    "6-3-212": {"upapajjissati": "ဖြစ်ပေါ်လိမ့်မည်"},
}


def mapper():
    return R.Mapper(chapter_tables=TABLES, ctx=CTX, funcs=FUNCS_G1,
                    stem=R.make_stem([R.FRAME, R.STOCK, T_ALL]))


def module_only():
    return R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK]))


# =====================================================================================================================
# run, verify, S1 review
# =====================================================================================================================
def s1_review(ch, base, lines):
    """the uses whose MODULE-ONLY value comes from the stem fallback (S1): kept (the final value is the stem value) or
    corrected (a G1 table / context value replaces it)."""
    kept, corr = collections.Counter(), collections.Counter()
    b_lines = base.map_chapter(ch)[0]
    for lb, lf in zip(b_lines, lines):
        sid, rb = lb[1:].split("] ", 1)
        rf = lf.split("] ", 1)[1]
        for kvb, kvf in zip(rb.split(", "), rf.split(", ")):
            k, vb = kvb.split("=", 1)
            vf = kvf.split("=", 1)[1]
            if base.SRC.get((sid, k)) == "stem":
                (kept if vb == vf else corr)[(k, vb, vf)] += 1
    return kept, corr


def diff_report(chs):
    """the values that differ from a pi-1 … pi-5 value of the same keyword (or of its base form, R1), and from the
    phase-1 sample (1-mulayamaka, 2-01-khandhayamaka) for the same keyword: keyword, value, the other value (uses)."""
    sample = collections.defaultdict(collections.Counter)
    for ch in R.SAMPLE:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            for kv in l.split("] ", 1)[1].split(", "):
                k, v = kv.split("=", 1)
                sample[k][v] += 1
    same = new = 0
    prior_diff, sample_diff = collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)
    for ch in chs:
        for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
            for kv in l.split("] ", 1)[1].split(", "):
                k, v = kv.split("=", 1)
                pv = R.prev_vals(k)
                if not pv:
                    for b in R.base_forms(k):
                        pv = R.prev_vals(b)
                        if pv:
                            break
                if not pv:
                    new += 1
                elif v in pv:
                    same += 1
                else:
                    prior_diff[(k, v)][pv.most_common(1)[0][0]] += 1
                if sample.get(k) and v not in sample[k]:
                    sample_diff[(k, v)][sample[k].most_common(1)[0][0]] += 1
    print(f"PRIOR same {same} new {new} diff {sum(sum(c.values()) for c in prior_diff.values())} "
          f"({len(prior_diff)} pairs)")
    for (k, v), c in sorted(prior_diff.items(), key=lambda x: -sum(x[1].values())):
        print(f"   PRIORDIFF {k} = {v} | " + "; ".join(f"{p} ({n})" for p, n in c.items()))
    for (k, v), c in sorted(sample_diff.items(), key=lambda x: -sum(x[1].values())):
        print(f"   SAMPLEDIFF {k} = {v} | " + "; ".join(f"{p} ({n})" for p, n in c.items()))


def run(chs):
    M, B = mapper(), module_only()
    tot = collections.Counter()
    allkept, allcorr = collections.Counter(), collections.Counter()
    for ch in chs:
        lines, problems, unmapped, nne = M.map_chapter(ch)
        (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        n, bad, fails, punct, ruled = R.verify_file(ch)
        kept, corr = s1_review(ch, B, lines)
        allkept.update(kept)
        allcorr.update(corr)
        print(f"{ch}: lines {n} bad {bad} presence-fails {len(fails)} punct {len(punct)} unmapped {len(unmapped)} "
              f"NDE {nne} ruled {len(ruled)} S1 kept {sum(kept.values())} corrected {sum(corr.values())}")
        for x in unmapped:
            print("   UNMAPPED", x)
        for x in fails:
            print("   FAIL", x)
        for x in punct:
            print("   PUNCT", x)
        tot.update(lines=n, nne=nne, fails=len(fails), punct=len(punct), bad=len(bad), unmapped=len(unmapped),
                   kept=sum(kept.values()), corr=sum(corr.values()))
    print("TOTAL", dict(tot))
    if "--s1" in sys.argv:
        for (k, vb, vf), c in sorted(allkept.items()):
            print(f"   S1 KEPT {k} = {vb} ({c})")
        for (k, vb, vf), c in sorted(allcorr.items()):
            print(f"   S1 CORRECTED {k}: {vb} -> {vf} ({c})")
    if "--diff" in sys.argv:
        diff_report(chs)
    if "--pairs" in sys.argv:
        pairs = collections.Counter()
        src = {}
        for ch in chs:
            for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
                sid, rest = l[1:].split("] ", 1)
                for kv in rest.split(", "):
                    k, v = kv.split("=", 1)
                    pairs[(k, v)] += 1
                    src.setdefault((k, v), M.SRC.get((sid, k), "?"))
        for (k, v), c in sorted(pairs.items(), key=lambda x: (R.low(x[0][0]), x[0][1])):
            print(f"   PAIR {k} = {v} | {c} | {src[(k, v)]}")
    return M


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    run(args or G1)
