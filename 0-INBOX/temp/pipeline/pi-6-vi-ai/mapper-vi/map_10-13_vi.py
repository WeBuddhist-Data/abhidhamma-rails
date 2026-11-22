"""Pāli->Vietnamese keyword map, pi-6 chapter 10-13-indriyayamaka (Indriyayamaka, pariññāvāra: paccuppanna … atītānāgata,
^6-10-19-1-0 … ^6-10-482, with the yamaka closer «Indriyayamakaṃ niṭṭhitaṃ» and the book closer «Yamakapakaraṇaṃ
niṭṭhitaṃ»).

usage: python -I -X utf8 -B map_10-13_vi.py                  (writes 10-13-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-13_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-13_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. The four verbs of the Indriya pariññāvāra, each by the polarity of its FIRST
occurrence in the Pāli segment (bare and question -ti form = one verb; the 2-01 / 2-02 rule, coordinator):
    parijānāti …      map_2-02_vi.parinna_value «hiểu biết trọn vẹn» (also paṭilabhissanti, maggaṃ paṭilabhissanti)
    pajahati …        map_5-03_vi.pajahati_value «dứt bỏ» (fused nappajah- = «không / chưa từng / sẽ không dứt bỏ»)
    bhāveti …         bhaveti_value: map_9-01_vi.BHAVANA_STEMS «tu tập» with the 2-02 PARINNA_FORMS templates; 9-01
                      parses bhāve-ti / -nti / -ssati only, so the forms of this chapter are parsed here (bhāveti,
                      bhāventi, bhāvittha, bhāvessati, bhāvessanti and the -ti question forms)
    sacchikaroti …    sacchikaroti_value «tự mình chứng nghiệm» (as the text), same templates: sacchikaroti /
                      sacchikaronti, sacchikarittha / sacchākāsi (aorist) «đã …», sacchikarissati / -issanti «sẽ …»
Persons: map_2-02_vi.PARINNA_PERSONS, map_7-06_vi.T706 (Aṭṭhamako / -kañca «người thứ tám», Anāgāmimaggasamaṅgī /
-giñca «người có được con đường không trở lại» …), map_7-01_vi PERSONS (Anāgāmī «bậc không trở lại»).
Chain: T10_13 -> pajahati_value -> bhaveti_value -> sacchikaroti_value -> parinna_value -> PARINNA_PERSONS -> T706 ->
map_10-02_vi.value1002 (members, mūlaka headings, FORMULAS headings).
Conventions: as map_10-02_vi.py, notes-map-10-01.md, notes-map-10-02.md, notes-map-2-02.md, notes-map-5-03.md,
notes-map-9-01.md, notes-map-9-03.md, notes-map-7-06.md.
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
from map_common_vi import (NDE, build_part, en, lc, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, HERE / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


J = importlib.import_module("map_10-02_vi")         # value1002 (members, mūlaka headings, value303 …)
P = importlib.import_module("map_2-02_vi")          # parinna_value, PARINNA_FORMS, PARINNA_PERSONS, _polarity
Q = importlib.import_module("map_5-03_vi")          # pajahati_value
D = importlib.import_module("map_9-01_vi")          # BHAVANA_STEMS (bhāve «tu tập»)
E6 = _load("map_7_06_vi_for_10_13", "map_7-06_vi.py")   # T706: Aṭṭhamako / -ñca, Anāgāmimaggasamaṅgī …
A = E6.A                                            # map_7-01_vi (PERSONS: Anāgāmī «bậc không trở lại»)

PART = "10-13-indriyayamaka"

# ---------------------------------------------------------------------------- bhāveti and sacchikaroti
# «thì có phải người ấy tu tập / đã tu tập / sẽ tu tập năng lực hiểu biết trọn vẹn không?», «… tự mình chứng nghiệm
# năng lực của người đã hiểu biết trọn vẹn …»: the verb with its tense word; a separate na keeps «không» for itself
# (na bhāveti -> «tu tập»), na + past «chưa từng …», na + future «sẽ … …», the denied negative after «no ca» plainly
# («nhưng đã từng …», «nhưng vẫn sẽ …») = the parijānāti / pajahati templates (coordinator rule, 9-03 / 10-13).
VERB13 = {
    "bhāv": (D.BHAVANA_STEMS["bhāve"],
             {"eti": "pres", "enti": "pres", "ittha": "past", "esuṃ": "past", "essati": "fut", "essanti": "fut"}),
    "sacchikar": ("tự mình chứng nghiệm",
                  {"oti": "pres", "onti": "pres", "ittha": "past", "iṃsu": "past", "issati": "fut", "issanti": "fut"}),
}
AORIST13 = {"sacchākāsi": ("sacchikar", "past")}    # «Yo aggaphalaṃ sacchākāsi» «Người nào đã tự mình chứng nghiệm …»


def _verb13_parse(kw):
    """(stem, tense, base form) of a bhāveti / sacchikaroti keyword (-ti of the question dropped), else None."""
    k = lc(kw).lower()
    if k in AORIST13:
        st, t = AORIST13[k]
        return st, t, k
    cands = [k]
    if len(k) > 5 and k[-3:] in ("īti", "āti"):
        cands.append(k[:-3] + {"ī": "i", "ā": "a"}[k[-3]])
    for c in cands:
        for st, (_v, ends) in VERB13.items():
            if c.startswith(st) and c[len(st):] in ends:
                return st, ends[c[len(st):]], c
    return None


def verb13_value(kw, pali=None):
    """bhāveti … / sacchikaroti …: the verb with its tense word by the polarity of its first occurrence in the Pāli
    (map_2-02_vi._polarity; bare and question form = one verb). None if not such a keyword."""
    p = _verb13_parse(kw)
    if not p:
        return None
    st, t, base = p
    forms = [base] + ([base[:-1] + {"i": "īti", "a": "āti"}[base[-1]]] if base[-1] in "ia" else [])
    pol = P._polarity(forms, pali) if pali else "pos"
    return P.PARINNA_FORMS[(pol, t)].format(v=VERB13[st][0])


# ---------------------------------------------------------------------------- this chapter's fixed values
T10_13 = {
    # «Người nào tự mình chứng nghiệm thành quả tối thượng» (= 5-01 aggaphalassa)
    "aggaphalaṃ": "thành quả tối thượng",
    # ^6-10-468 source slip anāgāmimaggasamaṅgi (short i, lower case) = Anāgāmimaggasamaṅgī (the text: «Người có được
    # con đường không trở lại sẽ tu tập …»)
    "anāgāmimaggasamaṅgi": E6.T706["anāgāmimaggasamaṅgī"],
    # «Ngoại trừ hai / ba / bốn người có được con đường» (Dve / Tayo / Cattāro: no keyword; = 7-06 maggasamaṅgīnaṃ)
    "maggasamaṅgino": E6.T706["maggasamaṅgīnaṃ"],
    # yamaka closer «Phần các cặp câu hỏi về các năng lực đã hoàn tất.» (lower case as written, = 6-02 / 9-03 / 3-06;
    # «Phần» and «đã hoàn tất» frame; heading form «Các cặp câu hỏi về các năng lực» in 10-01)
    "indriyayamakaṃ": "các cặp câu hỏi về các năng lực",
    # book closer «Bộ “Các cặp câu hỏi” đã hoàn tất.»: pakaraṇaṃ «Bộ» (pi-2 Vibhaṅgapakaraṇaṃ «Bộ Phân tích các hiện
    # tượng», pi-4 pakaraṇaṃ «Bộ») + Yamaka «Các cặp câu hỏi» as the text has it (quotes and capital kept)
    "yamakapakaraṇaṃ": "Bộ “Các cặp câu hỏi”",
    "(no direct equivalent)": NDE,                  # keyword-file placeholder (coordinator rule)
}


def value1013(kw, kws, vi, pi):
    k = lc(kw).lower()
    for x in (kw, lc(kw), k):
        if x in T10_13:
            return T10_13[x]
    for f in (Q.pajahati_value, verb13_value, P.parinna_value):
        v = f(kw, pi)
        if v is not None:
            return v
    if k in P.PARINNA_PERSONS:
        return P.PARINNA_PERSONS[k]
    if k in E6.T706:
        return E6.T706[k]
    if k in A.PERSONS:
        return A.PERSONS[k]
    return J.value1002(kw, kws, vi, pi)


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
        return value1013(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
