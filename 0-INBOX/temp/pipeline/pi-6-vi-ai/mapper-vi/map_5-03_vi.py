"""Pāli->Vietnamese keyword map, pi-6 chapter 5-03-saccayamaka (Saccayamaka: the rest of the uppādanirodhavāra
(paccuppannānāgata, atītānāgata), the closer of the pavattivāra, and the pariññāvāra with its closers).

usage: python -I -X utf8 -B map_5-03_vi.py                  (writes 5-03-saccayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_5-03_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_5-03_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setters (loaded with importlib): map_5-01_vi (value501: SACCA, moments,
citta kinds, persons, PATH …; through it map_2-01_vi.verb_value for every uppajjati / nirujjhati keyword), map_5-02_vi
(T502: the editorial-note words of the pavattivāra), map_2-02_vi (parinna_value, PARINNA_FORMS, PARINNA_PERSONS: the
pariññāvāra). pajahati and its tenses: map_7-01_vi VERBS has the present only («dứt bỏ», «không dứt bỏ», after no ca
«vẫn dứt bỏ»); the past and future here are built with the same templates as parijānāti (PARINNA_FORMS =
map_2-01_vi.VERB_FORMS, fused n- = the «neg» row), polarity of the verb's first occurrence in the Pāli segment.
Resolution: OVERRIDES[bid][kw] -> T503 -> (pariññāvāra segments) pajahati_value -> map_2-02_vi.parinna_value ->
PARINNA_PERSONS -> map_5-01_vi.value501(kw, kws, vi, pi, T503).
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md, notes-map-2-01.md, notes-map-2-02.md, notes-map-5-01.md,
notes-map-5-02.md, notes-map-5-03.md.
"""
import importlib
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

T = importlib.import_module("map_5-01_vi")          # Saccayamaka frame-setter
T2 = importlib.import_module("map_5-02_vi")         # pavattivāra editorial words (T502)
P = importlib.import_module("map_2-02_vi")          # pariññāvāra frame-setter

PART = "5-03-saccayamaka"

# ---------------------------------------------------------------------------- pajahati and its tenses
# «thì có phải người ấy dứt bỏ / đã dứt bỏ / sẽ dứt bỏ sự thật về sự phát sinh không?»; nappajah- (fused n-):
# «không dứt bỏ» / «chưa từng dứt bỏ» / «sẽ không dứt bỏ»; after «no ca» the denied negative is said plainly
# («nhưng đã từng dứt bỏ», «nhưng vẫn sẽ dứt bỏ»). Present = map_7-01_vi VERBS (dứt bỏ / không dứt bỏ / vẫn dứt bỏ).
PAJAH_STEM = ("pajah", "dứt bỏ")
PAJAH_ENDINGS = {"ati": "pres", "anti": "pres", "ittha": "past", "iṃsu": "past", "issati": "fut", "issanti": "fut"}


def _pajah_parse(kw):
    """(base form, tense, fused_negative) of a pajahati keyword (-ti of the question dropped), else None."""
    k = lc(kw).lower()
    if len(k) > 4 and k.endswith("ti") and k[-3] in "āī":
        k = k[:-3] + {"ā": "a", "ī": "i"}[k[-3]]
    st = PAJAH_STEM[0]
    if k.startswith("nap" + st):
        neg, rest = True, k[len(st) + 3:]
    elif k.startswith(st):
        neg, rest = False, k[len(st):]
    else:
        return None
    if rest not in PAJAH_ENDINGS:
        return None
    return k, PAJAH_ENDINGS[rest], neg


def pajahati_value(kw, pali):
    """pajahati … / nappajahati …: the verb with its tense word by the polarity of its first occurrence in the Pāli
    (bare and question -ti form = one verb; the 2-01 / 2-02 rule). None if not a pajahati keyword."""
    p = _pajah_parse(kw)
    if not p:
        return None
    base, tense, neg = p
    forms = [base] + ([base[:-1] + {"i": "īti", "a": "āti"}[base[-1]]] if base[-1] in "ia" else [])
    pol = P._polarity(forms, pali) if pali else "pos"
    if neg:
        pol = "noca_neg" if pol.startswith("noca") else "neg"
    return P.PARINNA_FORMS[(pol, tense)].format(v=PAJAH_STEM[1])


# ---------------------------------------------------------------------------- own table (lower-case keys)
T503 = {
    **T2.T502,
    # «(… đã được phân tích trong mục về sự chấm dứt, …)»: «trong» = the locative frame (7-01 vare_value)
    "nirodhavāre": "mục về sự chấm dứt",
    # closer «Phần các cặp câu hỏi về các sự thật đã hoàn tất.» (lower case as written, = 2-02 Khandhayamakapāḷi)
    "saccayamakaṃ": "các cặp câu hỏi về các sự thật",
}

# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value503(kw, kws, vi, pi):
    k = lc(kw).lower()
    for x in (kw, lc(kw), k):
        if x in T503:
            return T503[x]
    if re.search(r"parijān", pi):                     # the pariññāvāra (2-02 frame)
        v = pajahati_value(kw, pi)
        if v is not None:
            return v
        v = P.parinna_value(kw, pi)
        if v is not None:
            return v
        if k in P.PARINNA_PERSONS:
            return P.PARINNA_PERSONS[k]
    return T.value501(kw, kws, vi, pi, T503)


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value503(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
