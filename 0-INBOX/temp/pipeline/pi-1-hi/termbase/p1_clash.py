"""Part-1 helper: segments where two different Pāli keys (at least one a headword of senses-file lines lo..hi)
receive the identical Hindi value. Keys sharing their first 4 letters (likely one lemma) are skipped.

usage: python -I -X utf8 p1_clash.py <lo> <hi>
"""
import collections, pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation/hindi/pi-1-keywords-by-reference-pali-hindi-plain.md"
SENSES = ROOT / "AI_translation/hindi/pi-1-pali-word-hindi-senses-plain.md"


def main(a):
    lo, hi = int(a[0]), int(a[1])
    hws = {l.split(": {", 1)[0] for l in SENSES.read_text(encoding="utf-8").splitlines()[lo - 1:hi]}
    seen = collections.defaultdict(list)
    for line in KW.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\[([^\]]*)\]\s*(.*)$", line)
        if not m:
            continue
        ref, body = m.groups()
        byval = collections.defaultdict(set)
        for p in body.split(", "):
            if "=" in p:
                k, v = p.split("=", 1)
                byval[v].add(k)
        for v, ks in byval.items():
            ks = sorted(ks)
            for i in range(len(ks)):
                for j in range(i + 1, len(ks)):
                    x, y = ks[i], ks[j]
                    if x.lower()[:4] == y.lower()[:4] or x.lower() in y.lower() or y.lower() in x.lower():
                        continue
                    if x in hws or y in hws:
                        seen[(v, x, y)].append(ref)
    for (v, x, y), refs in sorted(seen.items(), key=lambda t: -len(t[1])):
        print(f"{v}\t{x}\t{y}\t{len(refs)}\t{' '.join(refs[:4])}")


if __name__ == "__main__":
    main(sys.argv[1:])
