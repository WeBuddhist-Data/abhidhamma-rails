"""H8 survey (read-only): a Pāli word W not followed by a head noun (given as -n regex), and whether the Burmese of the
line has the qualifier Q followed by the noun N (supplied) or bare.
usage: ell7.py PALI_RX QUAL_MY NOUN_MY"""
import re, sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent; R = HERE.parents[3]
pd = R / "AI_translation/pali/pi-7_split_chapters"; md = R / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
prx, q, n = re.compile(sys.argv[1]), sys.argv[2], sys.argv[3]
c = collections.Counter(); ex = collections.defaultdict(list)
for p in sorted(pd.glob("*.md")):
    for i, (x, y) in enumerate(zip(p.read_text(encoding="utf-8-sig").split("\n"), (md / p.name).read_text(encoding="utf-8").split("\n")), 1):
        k = len(prx.findall(x))
        if not k: continue
        sup = len(re.findall(re.escape(q) + " " + re.escape(n), y)); bare = len(re.findall(re.escape(q) + r"(?! " + re.escape(n) + ")", y))
        key = f"pali-bare {k}: my +noun {sup}, my bare {bare}"
        c[key] += 1; ex[key].append(f"{p.name[:4]}:{i}")
for k, v in sorted(c.items()):
    print(v, k, sorted(set(e[:4] for e in ex[k]))[:12], ex[k][:3])
