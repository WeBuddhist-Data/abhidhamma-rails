"""Pāli->Vietnamese keyword map of pi-6 7-07-anusayayamaka (Pariññāvāra: anuloma «hiểu biết trọn vẹn» and paṭiloma
«không hiểu biết trọn vẹn», na separate).

usage: python -I -X utf8 -B map_7-07_vi.py                  (writes 7-07-anusayayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_7-07_vi.py dump [miss]      (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_7-07_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setters: map_7-06_vi.py (chains 7-01 … 7-05: value701, TENDENCY, PERSONS,
PLANES, FEELINGS, vare_value, 7-05 tendency_ca, T706 with the maggasamaṅgī persons), map_2-02_vi.py (parinna_value,
PARIJANATI: parijānāti / parijānanti «hiểu biết trọn vẹn» from the polarity of the verb's FIRST occurrence in the Pāli:
a separate na keeps «không» for itself, the 2-01 VERB_FORMS), loaded with importlib; resolution OVERRIDES[bid][kw] ->
value707() = 7-05 tendency_ca (the -ñca tendency forms) -> 2-02 parinna_value(kw, pali) -> A.value701(kw, kws, T707,
text) = T707 (T706 + own) -> 7-01 T701 -> tendency_value -> vare_value -> verb_value -> map_sample_vi.value6.
Conventions: vi-map-conventions-pi6.md, map-coordinator-rules.md, notes-map-7-01.md … notes-map-7-07.md,
notes-map-2-02.md.
"""
import importlib
import importlib.util
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from map_common_vi import (NDE, build_part, en, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, HERE / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


F = _load("map_7_06_vi", "map_7-06_vi.py")          # chains 7-01 … 7-05
A, E = F.A, F.E                                      # 7-01 (value701), 7-05 (tendency_ca)
P = importlib.import_module("map_2-02_vi")          # pariññāvāra verbs (parinna_value)

PART = "7-07-anusayayamaka"

# Own table (lower-case keys) on top of 7-06 T706 (7-02 paṭiloma headings, 7-03 puggalo «hạng người», ṭhapetvā,
# aṭṭhamakañca, Anāgāmi- / Agga- / maggasamaṅgī «người có được con đường …»).
T707 = {
    **F.T706,
    "(no direct equivalent)": NDE,                   # keyword-file placeholder (coordinator rule)
}

# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value707(kw, kws, text, pali):
    v = E.tendency_ca(kw)
    if v is not None:
        return v
    v = P.parinna_value(kw, pali)
    if v is not None:
        return v
    return A.value701(kw, kws, T707, text)


def resolver():
    vi, pi = read_vietnamese(PART), read_pali(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value707(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
