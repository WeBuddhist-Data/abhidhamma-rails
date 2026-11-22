"""Pāli->Vietnamese keyword map, pi-6 chapter 5-01-saccayamaka (Saccayamaka: paṇṇattivāra, pavattivāra / uppādavāra),
and the FRAME TABLES of the Saccayamaka for the later chapters 5-02 and 5-03.

usage: python -I -X utf8 -B map_5-01_vi.py                  (writes 5-01-saccayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_5-01_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_5-01_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. 5-02 / 5-03 load it with importlib:

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\mapper-vi")
    T = importlib.import_module("map_5-01_vi")
    T.SACCA_STEM      dukkha «khổ đau» (the truth), samudaya «sự phát sinh», nirodha «sự chấm dứt», magga «con đường»
    T.SACCA           every member form (dukkhasaccaṃ «sự thật về khổ đau», saccaṃ / saccā / saccāni «sự thật», dukkhaṃ
                      «khổ đau», samudayo / samudayaṃ, nirodho / nirodhaṃ, maggo / maggaṃ …); -ti / -nti / -ñca / -ñceva
                      dropped by sacca_value(kw, text)
    T.SUBJECT         Kāyikaṃ dukkhaṃ «khổ đau nơi thân», cetasikaṃ dukkhaṃ «khổ đau trong tâm»
    T.CITTA_KIND5     the citta kinds of this yamaka («tâm không gắn liền với khao khát», «tâm tái sinh» …); citta5(word)
    T.NOUN_OF         the non-citta owners of a moment (taṇhāya «khao khát», maggassa «con đường», aggamaggassa «con đường
                      tối thượng», phalassa «thành quả» …); moment5(kw, text) = «khoảnh khắc sinh khởi / tan rã của …»
                      (8-cittayamaka rule: the «Vào» of the locative is frame)
    T.PERSONS5        Aggamaggasamaṅgīnaṃ, (an)abhisametāvīnaṃ, puthujjanā, āpāyikānaṃ, caññe, nirodhasamāpannānaṃ …
    T.PLANES5         Apāye «cõi khổ» (and the slip asaññattā); the other planes / beings come from map_2-01_vi
    T.PATH            aggamaggaṃ / maggaṃ paṭilabhissanti «sẽ đạt được con đường (tối thượng)», paṭilabhissanti
    T.NOTES5          the editorial notes (yassaka «phần về người», yatthaka «phần về nơi chốn», … sadisaṃ «giống như …»)
    T.HEAD5           Suddhasaccavāro, Suddhasaccamūlacakkavāro, Paṇṇattivāra
    T.T501            all fixed values merged (lower-case keys)
    T.value501(kw, kws, vi, pi, table=None)
                      your table -> T501 -> sacca_value -> moment5 / citta5 -> path verbs -> map_2-01_vi.value201 (members =
                      SACCA; verbs by the 2-01 first-occurrence rule, planes / beings, itaresaṃ, relatives) -> value6
Values are the words of the zero-shot translation (build_5-01_vi.py MEMBER, CITTA_KIND, NOUN_OF, HEAD_RULES); the
translation file is the truth, so every later chapter checks them against its segments (the presence check does).
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md, notes-map-2-01.md, notes-map-8.md, notes-map-3-01.md,
notes-map-5-01.md.
"""
import importlib
import importlib.util
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import map_sample_vi as S  # noqa: E402
from map_common_vi import (GAP, NDE, build_part, en, lc, pick, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)

K = importlib.import_module("map_2-01_vi")         # shared pavatti frames (verbs, planes, beings, relatives)
_spec8 = importlib.util.spec_from_file_location("map_8_vi", HERE / "map_8_vi.py")
C = importlib.util.module_from_spec(_spec8)
_spec8.loader.exec_module(C)                         # moments (MOMENT), citta kinds (citta_value)

PART = "5-01-saccayamaka"

# ---------------------------------------------------------------------------- the four truths (members)
# pi-2 Saccavibhaṅga / ^2-982 «Sự thật về khổ đau, sự thật về sự phát sinh, sự thật về sự chấm dứt, sự thật về con
# đường»; dukkha here is the truth «khổ đau» (10-01 bare dukkhaṃ «sự khó chịu» is the bodily-pain faculty).
SACCA_STEM = {"dukkha": "khổ đau", "samudaya": "sự phát sinh", "nirodha": "sự chấm dứt", "magga": "con đường"}
SACCA_OF = "sự thật về {x}"
SACCA = {
    # sacca (member): «Các sự thật» / «Bốn sự thật»: leading «các», the numeral of a keyword without it, frame
    "saccaṃ": "sự thật", "saccā": "sự thật", "saccāni": "sự thật", "sacca": "sự thật", "saccesu": "sự thật",
    "saccassa": "sự thật", "saccānaṃ": "sự thật",
    "dukkhaṃ": SACCA_STEM["dukkha"], "dukkha": SACCA_STEM["dukkha"],
    "samudayo": SACCA_STEM["samudaya"], "samudayaṃ": SACCA_STEM["samudaya"], "samudaya": SACCA_STEM["samudaya"],
    "nirodho": SACCA_STEM["nirodha"], "nirodhaṃ": SACCA_STEM["nirodha"],
    "maggo": SACCA_STEM["magga"], "maggaṃ": SACCA_STEM["magga"],
}
for _s, _v in SACCA_STEM.items():
    for _e in ("aṃ", "a", "ā", "assa", "e", "ena"):
        SACCA[_s + "sacc" + _e] = SACCA_OF.format(x=_v)

# «Ngoại trừ khổ đau nơi thân, khổ đau trong tâm, …»: the member word «khổ đau» is kept (build_5-01 KAYIKA_CETASIKA)
SUBJECT = {
    "kāyikaṃ dukkhaṃ": SACCA_STEM["dukkha"] + " nơi thân", "cetasikaṃ dukkhaṃ": SACCA_STEM["dukkha"] + " trong tâm",
    "kāyikaṃ": "nơi thân", "cetasikaṃ": "trong tâm",     # proposals (pi-1 kāyika / cetasika), not keywords in 5-01
}


def sacca_value(kw, text):
    """A Saccayamaka member keyword in any form (-ti, -nti, -ñca, -ñceva dropped: map_2-01_vi.member_value), where the
    segment has it; None otherwise."""
    v = K.member_value(kw, SACCA)
    if v is not None and present(v, text):
        return v
    return None


# ---------------------------------------------------------------------------- citta kinds and moments
# «tâm <kind>» as build_5-01_vi.CITTA_KIND writes it (taṇhā «khao khát» core, vippayutta «không gắn liền với» pi-1,
# upapatti «tái sinh» pi-2); dutiye citte vattamāne «khi tâm thứ hai đang diễn ra» (citte / vattamāne are keywords)
CITTA_KIND5 = {
    "taṇhāvippayutta": "không gắn liền với khao khát",
    "maggavippayutta": "không gắn liền với con đường",
    "taṇhāvippayuttamaggavippayutta": "không gắn liền với khao khát và không gắn liền với con đường",
    "maggavippayuttataṇhāvippayutta": "không gắn liền với con đường và không gắn liền với khao khát",
    "upapatti": "tái sinh",
    "dutiya": "thứ hai",
}
_CITTA_ENDS = ("cittassa", "citte", "cittaṃ", "cittā", "citta")
# owners of a moment that are not a citta (<X>ssa / <X>ya uppādakkhaṇe / bhaṅgakkhaṇe)
NOUN_OF = {
    "taṇhāya": "khao khát", "maggassa": "con đường", "aggamaggassa": "con đường tối thượng",
    "phalassa": "thành quả",                       # phala «thành quả» (core; pi-4)
    "aggaphalassa": "thành quả tối thượng",        # proposal (5-02 / 5-03; check against the segment)
}


def citta5(word):
    """<kind>cittassa / -citte / -cittaṃ (kinds of this yamaka) -> «tâm <kind>»; cittassa / citte alone -> «tâm»;
    other kinds via map_8_vi.citta_value (pacchima «tâm cuối cùng», kusala «tâm thiện» …). None if not a citta."""
    k = C.norm(lc(word))
    if "samaṅg" in k:                                  # Pacchimacittasamaṅgīnaṃ «người có được tâm cuối cùng» (8)
        return C.citta_value(word)
    for e in _CITTA_ENDS:
        if k.endswith(e):
            pre = k[: -len(e)]
            if pre == "":
                return "tâm"
            if pre in CITTA_KIND5:
                return "tâm " + CITTA_KIND5[pre]
            return C.citta_value(word)
    return None


def moment5(kw, text):
    """«<owner> uppādakkhaṇe / bhaṅgakkhaṇe» = «khoảnh khắc sinh khởi / tan rã của <owner>» (8: «Vào» is frame);
    a bare moment word = map_8_vi.MOMENT. None if not a moment keyword."""
    words = kw.split()
    if len(words) == 2:
        m = C.moment_value(words[1], text)
        if not m:
            return None
        owner = NOUN_OF.get(lc(words[0]).lower()) or citta5(words[0])
        return (m + " của " + owner) if owner else None
    if len(words) == 1:
        return C.moment_value(kw, text)
    return None


# ---------------------------------------------------------------------------- persons, beings, planes
# «Ở những người …»: the case word «Ở» and the leading «những» / «các» are frame (pi-4, 2-01, 8); the head noun
# «người» / «chúng sinh» is the keyword's own word.
PERSONS5 = {
    "aggamaggasamaṅgīnaṃ": "người có được con đường tối thượng",     # FORMULAS aggamaggasamaṅgī
    "aggamaggasamaṅgī": "người có được con đường tối thượng",
    "aggamaggasamaṅgino": "người có được con đường tối thượng",
    "abhisametāvīnaṃ": "người đã thấu hiểu",                        # abhisameti «thấu hiểu» (pi-5)
    "anabhisametāvīnaṃ": "người chưa thấu hiểu",
    "puthujjanā": "người phàm phu",                                 # «những người phàm phu nào» (FORMULAS puthujjano)
    "arahantānaṃ": "bậc A-la-hán",                                  # «các bậc A-la-hán» (pi-5)
    "āpāyikānaṃ": "chúng sinh trong cõi khổ",                       # = 2-01 BEINGS shape «chúng sinh trong cõi …»
    "nirodhasamāpannānaṃ": "người nhập thành tựu thiền chấm dứt",   # = 8 PERSONS8
    "caññe": "khác",            # ye caññe «và những người khác nào»: ca «và» frame (sample -ñca), aññe = khác (pi-5)
    "cittassa": "tâm",          # yassa cittassa anantarā «ngay sau tâm nào đó»
    "anantarā": "ngay sau",     # pi-5
}
PLANES5 = {
    "apāye": "cõi khổ", "apāyaṃ": "cõi khổ", "apāyā": "cõi khổ",      # pi-2 apāya «cõi khổ» («Trong» frame)
    "asaññattā": "cõi Vô Tưởng",       # ^6-5-76 slip «asaññattā cavantānaṃ» = asaññasattā (build_5-01 SLIP_FIX)
    "avasese": "còn lại",              # Avasese catuvokāre pañcavokāre «… cõi gồm năm khối còn lại»
    # pavatte «trong đời sống» (the zero-shot coordinator's shared term, = 9-01): the locative «trong» is the case
    # frame, as «Trong cõi …» (2-01 PLANES) and the «Vào» of the moments (8)
    "pavatte": "đời sống",
}
# paṭilabhati «đạt được» (2-02); the future «sẽ» kept, the separate na's «không» is not part of the value
PATH = {
    "aggamaggaṃ paṭilabhissanti": "sẽ đạt được con đường tối thượng",
    "aggamaggaṃ paṭilabhissānti": "sẽ đạt được con đường tối thượng",   # ^6-5-74 spelling slip
    "maggaṃ paṭilabhissanti": "sẽ đạt được con đường",
}
_PATIL = ("paṭilabhissanti", "paṭilabhissānti")

# ---------------------------------------------------------------------------- notes, headings, other words
NOTES5 = {
    # (Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ) «(Phần về người và phần về người và nơi chốn cũng nên …)»;
    # -pi «cũng» has no word of its own here (3-01 paccuppannepi); 3-01 yassaka / yatthakaṃ / sadisaṃ
    "yassakampi": "phần về người", "yassayatthakampi": "phần về người và nơi chốn",
    "yatthakampi": "phần về nơi chốn", "yatthakaṃ": "phần về nơi chốn",
    "yatthakā": "phần về nơi chốn",                    # «(tất cả các phần về nơi chốn …)»: leading «các» dropped
    "yassayatthakepi": "phần về người và nơi chốn",    # proposal (5-02)
    "yatthakasadisaṃ": "giống như phần về nơi chốn",   # = 3-01 yassakasadisaṃ «giống như phần về người»
    "yassayatthakasadisaṃ": "giống như phần về người và nơi chốn",
    "(no direct equivalent)": NDE,                     # the keyword-file placeholder (2-01 / 3-01 / 7-01 / 8)
}
HEAD5 = {
    "suddhasaccavāro": "mục về các sự thật thuần túy",            # inner «các» kept (3-01 Suddhāyatanavāro)
    "suddhasaccamūlacakkavāro": "mục về vòng luân chuyển dựa trên các sự thật thuần túy",
    "paṇṇattivāra": "mục về sự định danh",                       # ^6-5-6-0 stem form of Paṇṇattivāro
}
OTHER5 = {
    "avaseso": "còn lại", "avasesaṃ": "còn lại", "avasesā": "còn lại",   # «những gì còn lại» (2-01 / 3-01 / 10-01)
    "ṭhapetvā": "ngoại trừ",
}

T501 = {**SUBJECT, **PERSONS5, **PLANES5, **PATH, **NOTES5, **HEAD5, **OTHER5}


def value501(kw, kws, vi, pi, table=None):
    """your table -> T501 -> sacca_value -> moment5 / citta5 -> paṭilabhissanti -> map_2-01_vi.value201 (members =
    SACCA, the 2-01 verb / plane / person / relative rules) -> map_sample_vi.value6."""
    k = lc(kw).lower()
    if table:
        for x in (kw, lc(kw), k):
            if x in table:
                return table[x]
    if k in T501:
        return T501[k]
    if k in NOUN_OF:                                     # Aggamaggassa / maggassa / phalassa (owner of a moment)
        return NOUN_OF[k]
    v = sacca_value(kw, vi)
    if v is not None:
        return v
    v = moment5(kw, vi)
    if v:
        return v
    if " " not in kw:
        v = citta5(kw)
        if v:
            return v
    if k in _PATIL:                                      # «sẽ đạt được» / «sẽ không đạt được» (na separate)
        return pick(vi, "sẽ đạt được", "sẽ" + GAP + "đạt được") or "sẽ đạt được"
    return K.value201(kw, kws, vi, pi, None, SACCA)


# per-segment choices (none needed)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value501(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(only_miss=False, part=PART):
    res, vi = resolver(part), read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v != NDE and not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        e = en(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  en:{e}" if e else "") + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi, with_pali=False, part=PART):
    res, vi, pi = resolver(part), read_vietnamese(part), read_pali(part)
    for i, (bid, kws) in enumerate(read_keywords(part)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            if with_pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"-- VI {vi.get(bid, '')}")
            out = []
            for kw in kws:
                v = res(bid, kw, kws)
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                out.append(f"{kw}={v}{flag}")
            print("   " + " | ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
