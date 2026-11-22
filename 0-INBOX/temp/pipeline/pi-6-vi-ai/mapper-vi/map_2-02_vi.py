"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 2-02-khandhayamaka (Khandhayamaka, second half: the rest of
the pavatti section and the pariññāvāra); frame-setter of the pariññāvāra values (parijānāti and its tenses, the
person subjects of that section) for the later yamakas' pariññā sections.

usage: python -I -X utf8 -B map_2-02_vi.py                     (writes 2-02-khandhayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_2-02_vi.py dump [miss]          (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_2-02_vi.py show lo hi [pi]      (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Later chapters load it with importlib:
    import importlib, sys; sys.path.insert(0, <this folder>)
    P = importlib.import_module("map_2-02_vi")
and use the named tables / helpers of the pariññāvāra:
    PARINNA_STEMS     {stem: Vietnamese verb}: parijān «hiểu biết trọn vẹn», paṭilabh «đạt được»
    PARINNA_ENDINGS   {stem: {ending: tense}} (parijān-āti / -anti pres, -ittha / -iṃsu past, -issati / -issanti fut)
    PARINNA_FORMS     (polarity, tense) -> template (= map_2-01_vi.VERB_FORMS: pos / na / noca_pos / noca_neg)
    PARIJANATI        every fixed form: parijānāti / parijānanti = hiểu biết trọn vẹn, parijānittha = đã hiểu biết
                      trọn vẹn, parijānissati / parijānissanti = sẽ hiểu biết trọn vẹn (+ the -ti question forms)
    PARINNA_NA        the same verb under a separate na / inside «no ca» (for reference: «không» / «chưa từng» /
                      «sẽ … » / «vẫn …» / «đã từng …» / «vẫn sẽ …»)
    parinna_value(kw, pali)     the verb keyword's value from its FIRST occurrence in the Pāli segment (the 2-01 rule),
                      also «maggaṃ paṭilabhissanti» = «sẽ đạt được con đường» (Vietnamese order)
    PARINNA_PERSONS   the person subjects: Arahā / arahantañca «bậc A-la-hán», Aggamaggasamaṅgī / -iñca «người có được
                      con đường tối thượng», puthujjanā «người phàm phu», avasesā puggalā «hạng người còn lại» …
    PARINNA_FRAME     yo / so / yo vā pana «người nào» / «người ấy» / «còn người nào» (no «ở»: the verb takes a
                      direct subject), ye / te «người nào» / «người ấy» (Ye … te … «Những người nào …, thì những
                      người ấy»)
    HEAD202           headings / closers of this chapter (Khandhayamakapāḷi, the vadanākkhandho slip …)
    T202              all fixed values merged; value202(kw, kws, vi, pi, table=None)
Resolution: OVERRIDES[bid][kw] -> value202(): your table -> T202 -> parinna_value -> map_2-01_vi.frames201 (members,
pavatti verbs, planes, beings, persons, relatives) -> map_7-01_vi.vare_value (uppādavāre) -> map_8_vi.aspect_value
-> map_sample_vi.value6.
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md, notes-map-2-01.md, notes-map-8.md, notes-map-2-02.md.
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
from map_common_vi import (GAP, NDE, build_part, en, lc, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, HERE / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


K = importlib.import_module("map_2-01_vi")         # frame-setter: members, pavatti verbs, planes, beings, relatives
C = _load("map_8_vi", "map_8_vi.py")                # frame-setter: aspect forms, moments
A = _load("map_7_01_vi", "map_7-01_vi.py")          # vare_value (<X>vāre = the <X>vāro heading)

PART = "2-02-khandhayamaka"

# ---------------------------------------------------------------------------- the pariññāvāra verbs
# «Người nào hiểu biết trọn vẹn khối vật chất, thì có phải người ấy …?»: the value is the verb with its tense word
# (pi-6 conventions, 2-01 VERB_FORMS): a separate na keeps «không» for itself (na parijānāti «không hiểu biết trọn
# vẹn» -> parijānāti = hiểu biết trọn vẹn), the past under na is «chưa từng hiểu biết trọn vẹn», the future
# «sẽ không hiểu biết trọn vẹn» -> «sẽ … hiểu biết trọn vẹn»; the denied negative after «no ca» is said plainly
# («nhưng vẫn hiểu biết trọn vẹn», «nhưng đã từng hiểu biết trọn vẹn», «nhưng vẫn sẽ hiểu biết trọn vẹn»).
PARINNA_STEMS = {"parijān": "hiểu biết trọn vẹn", "paṭilabh": "đạt được"}
PARINNA_ENDINGS = {
    "parijān": {"āti": "pres", "anti": "pres", "ittha": "past", "iṃsu": "past", "issati": "fut", "issanti": "fut"},
    "paṭilabh": {"ati": "pres", "anti": "pres", "ittha": "past", "iṃsu": "past", "issati": "fut", "issanti": "fut"},
}
PARINNA_FORMS = dict(K.VERB_FORMS)                  # same templates as the pavatti verbs (one rule for all tenses)


def parinna_vi(stem, tense, polarity="pos"):
    return PARINNA_FORMS[(polarity, tense)].format(v=PARINNA_STEMS[stem])


PARIJANATI, PARINNA_NA = {}, {}
for _st, _ends in PARINNA_ENDINGS.items():
    for _e, _t in _ends.items():
        PARIJANATI[_st + _e] = parinna_vi(_st, _t)
        PARINNA_NA[_st + _e] = {p: parinna_vi(_st, _t, p) for p in ("na", "noca_pos", "noca_neg")}
for _k in list(PARIJANATI):                         # the question forms: parijānātīti, parijānitthāti, parijānissatīti
    if _k[-1] in "ia":
        PARIJANATI[_k[:-1] + {"i": "īti", "a": "āti"}[_k[-1]]] = PARIJANATI[_k]


def _parinna_parse(kw):
    """(stem, tense) of a pariññā verb keyword (-ti of the question dropped), else None."""
    k = lc(kw).lower()
    cands = [k]                                    # parijānāti itself ends in -āti: the bare form is tried first
    if len(k) > 5 and k[-3:] in ("īti", "āti"):
        cands.append(k[:-3] + {"ī": "i", "ā": "a"}[k[-3]])
    for c in cands:
        for st, ends in PARINNA_ENDINGS.items():
            if c.startswith(st) and c[len(st):] in ends:
                return st, ends[c[len(st):]]
    return None


def _polarity(forms, pali):
    """pos / na / noca_pos / noca_neg of the earliest occurrence of any of `forms` in the Pāli segment (the 2-01
    first-rendering rule: the bare verb and its question -ti form are one verb)."""
    hits = [x for x in (re.search(r"(?<!\w)" + re.escape(f) + r"(?!\w)", pali, re.I) for f in forms) if x]
    if not hits:
        return "pos"
    m = min(hits, key=lambda x: x.start())
    before = pali[: m.start()]
    clause = re.split(r"[.?!,;\n]", before)[-1]
    noca = re.search(r"(?<!\w)no ca(?!\w)", clause) is not None
    sep_na = re.search(r"(?<!\w)na\s+$", before) is not None
    if noca:
        return "noca_neg" if sep_na else "noca_pos"
    return "na" if sep_na else "pos"


def parinna_value(kw, pali=None):
    """parijānāti … / paṭilabhissanti (and «maggaṃ paṭilabhissanti» «sẽ đạt được con đường»): the verb with its tense
    word by the polarity of the first occurrence in the Pāli. None if not a pariññā verb."""
    words = kw.split()
    if len(words) == 2 and lc(words[0]).lower() == "maggaṃ":
        v = parinna_value(words[1], None)
        if v is None:
            return None
        pol = _polarity([kw], pali) if pali else "pos"
        p = _parinna_parse(words[1])
        return parinna_vi(p[0], p[1], pol) + " con đường"      # «sẽ đạt được con đường» (Vietnamese order)
    p = _parinna_parse(kw)
    if not p:
        return None
    st, t = p
    if not pali:
        return parinna_vi(st, t)
    k = lc(kw).lower()
    base = None
    for b in PARINNA_ENDINGS[st]:
        if k == st + b:
            base = k
    if base is None:                               # question form
        base = k[:-3] + {"ī": "i", "ā": "a"}[k[-3]]
    forms = [base] + ([base[:-1] + {"i": "īti", "a": "āti"}[base[-1]]] if base[-1] in "ia" else [])
    return parinna_vi(st, t, _polarity(forms, pali))


# ---------------------------------------------------------------------------- the person subjects of the pariññāvāra
# «Bậc A-la-hán không hiểu biết trọn vẹn …», «Ngoại trừ người có được con đường tối thượng và bậc A-la-hán, những
# hạng người còn lại …», «Bậc A-la-hán và những người phàm phu nào sẽ không đạt được con đường, thì những người ấy …»:
# the leading «những» is frame (pi-4), the head noun «người» / «bậc» / «hạng người» is the keyword's own word.
PARINNA_PERSONS = {
    "arahā": "bậc A-la-hán", "arahato": "bậc A-la-hán", "arahantaṃ": "bậc A-la-hán", "arahantañca": "bậc A-la-hán",
    "aggamaggasamaṅgī": "người có được con đường tối thượng",
    "aggamaggasamaṅgiṃ": "người có được con đường tối thượng",
    "aggamaggasamaṅgiñca": "người có được con đường tối thượng",
    "puthujjanā": "người phàm phu", "puthujjano": "người phàm phu", "puthujjanassa": "người phàm phu",
    "puggalā": "hạng người",                       # «những hạng người còn lại» (pi-4, coordinator)
    "avasesā": "còn lại", "avasesā puggalā": "hạng người còn lại",
    "ṭhapetvā": "ngoại trừ",                       # pi-2 / pi-3
    "maggaṃ": "con đường",
}
# «(a) Người nào hiểu biết trọn vẹn …, thì có phải người ấy …?»: the subject pronouns take no «ở» (proposal; not
# keywords in 2-02); «Những người nào sẽ đạt được con đường, thì những người ấy …» (Ye … te …; «Những» dropped)
PARINNA_FRAME = {
    "yo": "người nào", "so": "người ấy", "yo vā pana": "còn người nào",
    "ye": "người nào", "te": "người ấy",
}

# ---------------------------------------------------------------------------- headings and slips of this chapter
HEAD202 = {
    # closer «Phần các cặp câu hỏi về các khối đã hoàn tất.» (lower case as written, sample rule; «Phần» frame)
    "khandhayamakapāḷi": "các cặp câu hỏi về các khối",
    # ^6-2-130 «(yatthakaṃ paripuṇṇaṃ kātabbaṃ)» «(phần về nơi chốn nên được trình bày đầy đủ)»
    "yatthakaṃ": "phần về nơi chốn",
    # ^6-2-185 source slip vadanākkhandho (= vedanākkhandho; the text renders it as meant: «khối cảm giác»)
    "vadanākkhandho": "khối cảm giác",
    "(no direct equivalent)": NDE,                 # keyword-file placeholder (coordinator rule)
}

T202 = {**PARIJANATI, **PARINNA_PERSONS, **HEAD202}


def value202(kw, kws, vi, pi, table=None):
    """your table -> T202 -> parinna_value -> 2-01 frames -> 7-01 vare_value -> 8 aspect_value -> value6."""
    k = lc(kw).lower()
    if table:
        if kw in table:
            return table[kw]
        if k in table:
            return table[k]
    v = parinna_value(kw, pi)
    if v is not None:
        return v
    if k in T202:
        return T202[k]
    v = K.frames201(kw, kws, vi, pi)
    if v is not None:
        return v
    v = A.vare_value(kw)
    if v is not None:
        return v
    v = C.aspect_value(kw, vi, False, pi)
    if v is not None:
        return v
    return S.value6(kw, kws, table, vi)


# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver_for(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value202(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(part=PART, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
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
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  en:{e}" if e else "") + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi, with_pali=False, part=PART):
    res = resolver_for(part)
    vi, pi = read_vietnamese(part), read_pali(part)
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
        dump(PART, sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    else:
        build_part(PART, resolver_for(PART))
        verify(PART, ALLOWED)
