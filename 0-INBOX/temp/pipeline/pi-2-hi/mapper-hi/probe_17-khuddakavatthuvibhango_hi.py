"""Probe chapter 17: unique keywords, counts, PI2/CH2 default, pi-1/3/4/5 priors, English map values.

usage: python -I -X utf8 probe_17-khuddakavatthuvibhango_hi.py [all]
"""
import collections
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import PI2, CH2, prior, lc, read_keywords, ROOT  # noqa: E402

CH = "17-khuddakavatthuvibhango"
EN = ROOT / "AI_translation" / "english" / "pi-2-keywords-by-reference-pali-english-plain.md"


def en_map():
    ids = {b for b, _ in read_keywords(CH)}
    out = collections.defaultdict(collections.Counter)
    for line in EN.read_text(encoding="utf-8").splitlines():
        if "] " not in line:
            continue
        b, rest = line.split("] ", 1)
        if b[1:] not in ids:
            continue
        for pair in rest.split(", "):
            if "=" in pair:
                k, v = pair.split("=", 1)
                out[lc(k.strip())][v] += 1
    return out


if __name__ == "__main__":
    show_all = len(sys.argv) > 1
    cnt = collections.Counter()
    first = {}
    for bid, kws in read_keywords(CH):
        for k in kws:
            cnt[lc(k)] += 1
            first.setdefault(lc(k), bid)
    en = en_map()
    print("unique", len(cnt), "total", sum(cnt.values()))
    for k, c in cnt.items():   # order of first appearance
        d = PI2.get(k) or CH2.get(k)
        if d and not show_all:
            continue
        pr = prior(k)
        ps = " ;; ".join(f"pi{n}:" + "|".join(f"{v}({x})" for v, x in cn.most_common(2)) for n, cn in pr.items())
        e = "|".join(v for v, _ in en[k].most_common(2))
        print(f"{c:3d} {first[k]} {k} = {d or '-'} :: EN {e} :: {ps}")
