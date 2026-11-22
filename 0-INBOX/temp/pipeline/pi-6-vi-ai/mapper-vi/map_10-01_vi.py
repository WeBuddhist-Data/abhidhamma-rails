"""Pāli->Vietnamese keyword map, pi-6 chapter 10-01-indriyayamaka (Indriyayamaka, paṇṇattivāra: uddesa and niddesa),
and the FRAME TABLES of the Indriyayamaka members for the later chapters 10-02 … 10-13.

usage: python -I -X utf8 -B map_10-01_vi.py                  (writes 10-01-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-01_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-01_vi.py show lo hi       (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Later Indriya chapters load it with importlib:

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\mapper-vi")
    I = importlib.import_module("map_10-01_vi")
    I.FACULTIES      # [(Pāli stem, Vietnamese faculty name, bare Pāli forms, Vietnamese bare word)], text order
    I.FACULTY_NAME   # "cakkhundriya" -> "năng lực mắt" …          (the twenty-two names, pi-2 ^2-221)
    I.FACULTY_BARE   # "cakkhu" / "cakkhuṃ" / "cakkhū" -> "mắt" …  (the bare words: itthī «người nữ», puriso «người
                     #                                               nam», jīvitaṃ «sự sống», sukhaṃ «sự dễ chịu» …)
    I.INDRIYA        # indriyaṃ / indriyā / indriye = «năng lực» (leading «các» dropped, pi-2 khandhā = khối)
    I.SENSE          # Dibbacakkhu thiên nhãn, paññācakkhu mắt trí tuệ, Dibbasotaṃ thiên nhĩ, taṇhāsotaṃ dòng chảy của khao khát
    I.T10_01         # this chapter's table (headings, avasesa, the sense words)
    I.faculty_value(kw)                # any form of a member (-ṃ, -nti / -ti, -ñca / -ñceva, -assa, -ena, -e, -āni …)
                                       # -> the Vietnamese value, or None
    I.value10(kw, kws, table, text)    # your table -> T10_01 -> faculty_value -> map_sample_vi.value6

Values are the words of the zero-shot translation as build_10-01_vi.py writes them (FACULTY there); the translation
file is the truth, so every later chapter checks them against its segments (the presence check does).
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
_HERE = pathlib.Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
import map_sample_vi as S  # noqa: E402
from map_common_vi import NDE, build_part, en, lc, present, read_keywords, read_vietnamese, verify  # noqa: E402

PART = "10-01-indriyayamaka"

# ---------------------------------------------------------------------------- the Indriyayamaka members
INDRIYA = "năng lực"                       # indriyaṃ (pi-1 core); indriyā / indriye «các năng lực»: «các» dropped
# (Pāli stem, Vietnamese faculty name [pi-2 ^2-221 / build_10-01_vi FACULTY], bare Pāli forms, Vietnamese bare word)
FACULTIES = [
    ("cakkhundriya", "năng lực mắt", ("cakkhu", "cakkhuṃ", "cakkhū"), "mắt"),
    ("sotindriya", "năng lực tai", ("sotaṃ",), "tai"),
    ("ghānindriya", "năng lực mũi", ("ghānaṃ",), "mũi"),
    ("jivhindriya", "năng lực lưỡi", ("jivhā", "jivhaṃ"), "lưỡi"),
    ("kāyindriya", "năng lực thân", ("kāyo", "kāyaṃ"), "thân"),
    ("manindriya", "năng lực ý", ("mano", "manaṃ"), "ý"),
    ("itthindriya", "năng lực nữ tính", ("itthī", "itthiṃ"), "người nữ"),
    ("purisindriya", "năng lực nam tính", ("puriso", "purisaṃ"), "người nam"),
    ("jīvitindriya", "năng lực sống", ("jīvitaṃ",), "sự sống"),
    ("sukhindriya", "năng lực dễ chịu", ("sukhaṃ",), "sự dễ chịu"),
    ("dukkhindriya", "năng lực khó chịu", ("dukkhaṃ",), "sự khó chịu"),
    ("somanassindriya", "năng lực niềm vui", ("somanassaṃ",), "niềm vui"),
    ("domanassindriya", "năng lực nỗi buồn", ("domanassaṃ",), "nỗi buồn"),
    ("upekkhindriya", "năng lực bình thản", ("upekkhā", "upekkhaṃ"), "sự bình thản"),
    ("saddhindriya", "năng lực niềm tin", ("saddhā", "saddhaṃ"), "niềm tin"),
    ("vīriyindriya", "năng lực tinh tấn", ("vīriyaṃ",), "sự tinh tấn"),
    ("satindriya", "năng lực tỉnh thức", ("sati", "satiṃ", "satī"), "sự tỉnh thức"),
    ("samādhindriya", "năng lực định tâm", ("samādhi", "samādhiṃ", "samādhī"), "định tâm"),
    ("paññindriya", "năng lực trí tuệ", ("paññā", "paññaṃ"), "trí tuệ"),
    ("anaññātaññassāmītindriya", "năng lực biết được điều chưa từng biết",
     ("anaññātaññassāmīti", "anaññātaññassāmī", "anaññātaññassāmītiṃ"), "sự biết được điều chưa từng biết"),
    ("aññindriya", "năng lực hiểu biết trọn vẹn", ("aññaṃ",), "sự hiểu biết trọn vẹn"),
    ("aññātāvindriya", "năng lực của người đã hiểu biết trọn vẹn", ("aññātāvī", "aññātāviṃ"),
     "người đã hiểu biết trọn vẹn"),
]
FACULTY_NAME = {st: vi for st, vi, _, _ in FACULTIES}
FACULTY_BARE = {w: b for _, _, forms, b in FACULTIES for w in forms}
FACULTY_BARE.update({"indriyaṃ": INDRIYA, "indriyā": INDRIYA, "indriye": INDRIYA, "indriyāni": INDRIYA,
                     "indriyānaṃ": INDRIYA, "indriyassa": INDRIYA, "indriyena": INDRIYA})
# source spelling slips read as meant (^6-10-3 «anaññātaññāssāmīti»)
SLIP_ALIAS = {"anaññātaññāssāmīti": "anaññātaññassāmīti"}
# case endings of a faculty name after its stem vowel (cakkhundriy- + aṃ / assa / ena / e / āni / ānaṃ / a / ā)
_NAME_ENDINGS = ("aṃ", "assa", "ena", "e", "āni", "ānaṃ", "a", "ā")

# word-sense subjects «Mắt hiểu theo nghĩa thiên nhãn, mắt trí tuệ …» / «Tai hiểu theo nghĩa thiên nhĩ, dòng chảy của
# khao khát …» (2-01 A_SENSE frame «X hiểu theo nghĩa …» = frame; pi-5 dibbena cakkhunā = thiên nhãn)
SENSE = {"dibbacakkhu": "thiên nhãn", "paññācakkhu": "mắt trí tuệ",
         "dibbasotaṃ": "thiên nhĩ", "taṇhāsotaṃ": "dòng chảy của khao khát"}

# ---------------------------------------------------------------------------- this chapter's table
T10_01 = {
    **SENSE,
    "suddhindriyavāro": "mục về các năng lực thuần túy",          # inner «các» kept (as suddhakhandhavāro)
    "suddhindriyamūlacakkavāro": "mục về vòng luân chuyển dựa trên các năng lực thuần túy",
    "paṇṇattiuddesavāro": "mục nêu đề mục về sự định danh",       # «Mục nêu đề mục về sự định danh.» (2-01 frame)
    "avasesā": "còn lại", "avaseso": "còn lại", "avasesaṃ": "còn lại",   # «Các năng lực còn lại», «Tai còn lại»,
                                                                   # «những gì còn lại» (pi-1 … pi-4)
    "ṭhapetvā": "ngoại trừ",                                       # pi-2
}


def _norm(k):
    """lower-cased keyword -> candidate base forms: the -ñca / -ñceva particle dropped (Cakkhuñca -> cakkhuṃ), the
    quotative -nti / -ti dropped (cakkhundriyanti -> cakkhundriyaṃ, kāyoti -> kāyo); a listed member (sati,
    anaññātaññassāmīti) is never stripped."""
    out = [k]
    for p in ("ñceva", "ñca"):
        if k.endswith(p):
            out.append(k[: -len(p)] + "ṃ")
    if k.endswith("nti"):
        out.append(k[:-3] + "ṃ")
    elif k.endswith("ti") and len(k) > 3:
        out.append(k[:-2])
    return out


def faculty_value(kw):
    """Any form of an Indriyayamaka member -> its Vietnamese value; None if the keyword is not one."""
    k = lc(kw).lower()
    k = SLIP_ALIAS.get(k, k)
    for c in _norm(k):
        c = SLIP_ALIAS.get(c, c)
        if c in FACULTY_BARE:
            return FACULTY_BARE[c]
        for st, vi in FACULTY_NAME.items():
            if c.startswith(st[:-1]) and c[len(st) - 1:] in _NAME_ENDINGS:
                return vi
    return None


def value10(kw, kws, table=None, text=None):
    """your table -> T10_01 -> faculty_value -> map_sample_vi.value6 (context6 -> FORMULAS -> YM -> pi-5 chain)."""
    k = lc(kw).lower()
    if table and (lc(kw) in table or k in table):
        return table.get(lc(kw), table.get(k))
    if k in T10_01:
        return T10_01[k]
    v = faculty_value(kw)
    if v is not None:
        return v
    return S.value6(kw, kws, table, text)


# per-segment choices (none needed)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value10(kw, kws, None, vi.get(bid, ""))
    return resolve


def dump(only_miss=False):
    res, vi = resolver(), read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
        for kw in kws:
            v = res(bid, kw, kws)
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v != NDE and not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        e = en(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:3]}" + (f"  en:{e}" if e else "") + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi):
    res, vi = resolver(), read_vietnamese(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]\n-- VI {vi.get(bid, '')}")
            print("   " + " | ".join(f"{kw}={res(bid, kw, kws)}" for kw in kws))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]))
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
