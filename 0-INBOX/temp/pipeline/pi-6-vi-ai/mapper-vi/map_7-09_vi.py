"""Pāli->Vietnamese keyword map of pi-6 7-09-anusayayamaka (Pahīnavāra: anuloma «đã được dứt bỏ», the answers «Không
nên nói là “đã được dứt bỏ” hay “chưa được dứt bỏ”», paṭiloma «chưa được dứt bỏ»).

usage: python -I -X utf8 -B map_7-09_vi.py                  (writes 7-09-anusayayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_7-09_vi.py dump [miss]      (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_7-09_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setters: map_7-08_vi.py (chains 7-06 … 7-01 and 2-02: value701, TENDENCY,
PERSONS, PLANES, FEELINGS, vare_value, 7-05 tendency_ca, T706 / T708), loaded with importlib.
Resolution: OVERRIDES[bid][kw] -> value709() = 7-05 tendency_ca (the -ñca tendency forms) -> pahina_value (pahīno /
appahīno and their -ti / plural forms, first-rendering rule on the Pāli) -> 2-02 parinna_value -> A.value701(kw, kws,
T709, text) = T709 (T708 + own) -> 7-01 T701 -> tendency_value -> vare_value -> verb_value -> map_sample_vi.value6.

pahina_value: the 7-01 VERBS probe search («đã được dứt bỏ» / «chưa được dứt bỏ» whichever stands first in the
Vietnamese) would give appahīno the «đã được dứt bỏ» of pahīno in every anuloma segment (where appahīno occurs only in
«na vattabbo "pahīno"ti vā "appahīno"ti vā» «không nên nói là “đã được dứt bỏ” hay “chưa được dứt bỏ”»). So the
polarity is read from the FIRST occurrence of the keyword's own stem in the Pāli (map_2-01 verb_value style): pahīn- /
appahīn- outside a «no ca …» clause = its own value (pahīno «đã được dứt bỏ», appahīno «chưa được dứt bỏ»); inside
«no ca …» first = the plain double negative of the text (pahīno «chưa được dứt bỏ», appahīno «đã được dứt bỏ»).
Conventions: vi-map-conventions-pi6.md, map-coordinator-rules.md, notes-map-7-01.md … notes-map-7-09.md.
"""
import importlib.util
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from map_common_vi import (NDE, build_part, en, lc, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, HERE / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


H = _load("map_7_08_vi", "map_7-08_vi.py")          # chains 7-06 … 7-01 and 2-02
A, E, P = H.A, H.E, H.P                              # 7-01 (value701), 7-05 (tendency_ca), 2-02 (parinna_value)

PART = "7-09-anusayayamaka"

# Own table (lower-case keys) on top of 7-08 T708 (7-02 paṭiloma headings, puggalo, ṭhapetvā, the maggasamaṅgī persons).
T709 = {
    **H.T708,
    "pahīnavāra": "mục về những gì đã được dứt bỏ",   # paṭiloma heading «Mục về những gì đã được dứt bỏ» (FORMULAS)
}

# ---------------------------------------------------------------------------- pahīno / appahīno
PAHINA = {  # stem -> (plain value, value when the first occurrence stands inside «no ca …»)
    "pahīn": ("đã được dứt bỏ", "chưa được dứt bỏ"),
    "appahīn": ("chưa được dứt bỏ", "đã được dứt bỏ"),
}
_FORMS = {"pahīno", "pahīnā", "pahīnoti", "pahīnāti", "appahīno", "appahīnā", "appahīnoti", "appahīnāti"}


def _first_in_noca(stem, pali):
    """True if the first word of this stem in the Pāli (pahīn- not preceded by «ap») stands inside a «no ca …»
    clause (from «no ca» to the next . ; ? or the end); None if the stem is not there."""
    t = pali.lower()
    m = re.search(r"(?<![\w])" + re.escape(stem) + r"(?:o|ā)(?:ti)?(?![\w])", t)
    if not m:
        return None
    start = m.start()
    clause_start = max(t.rfind(c, 0, start) for c in ".;?\n")
    return "no ca" in t[clause_start + 1:start]


def pahina_value(kw, pali):
    k = lc(kw).lower()
    if k not in _FORMS:
        return None
    stem = "appahīn" if k.startswith("appahīn") else "pahīn"
    inside = _first_in_noca(stem, pali or "")
    plain, noca = PAHINA[stem]
    return noca if inside else plain


def value709(kw, kws, text, pali):
    v = E.tendency_ca(kw)
    if v is not None:
        return v
    v = pahina_value(kw, pali)
    if v is not None:
        return v
    v = P.parinna_value(kw, pali)
    if v is not None:
        return v
    return A.value701(kw, kws, T709, text)


# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver():
    vi, pi = read_vietnamese(PART), read_pali(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value709(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
        if only_miss and not miss.get((kw, v)):
            continue
        e = en(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  en:{e}" if e else "")
              + (f"  MISS {miss[(kw, v)]}" if miss.get((kw, v)) else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi, with_pali=False):
    res, vi, pi = resolver(), read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
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
