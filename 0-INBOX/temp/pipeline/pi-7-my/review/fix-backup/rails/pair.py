"""Inspection helper (read only): for Burmese lines matching a regex, count the Pāli-regex hits of the same line (and
the reverse with --rev).  usage: pair.py <burmese regex> <pāli regex> [--rails] [--show N] [--rev]"""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"
BD = ROOT / ("AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters" if "--rails" in sys.argv else
             "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters")
brx, prx = re.compile(N(sys.argv[1])), re.compile(N(sys.argv[2]))
show = int(sys.argv[sys.argv.index("--show") + 1]) if "--show" in sys.argv else 0
c = collections.Counter(); ex = []
for p in sorted(PD.glob("*.md")):
    pl = N(p.read_text(encoding="utf-8-sig")).splitlines(); bl = N((BD / p.name).read_text(encoding="utf-8")).splitlines()
    for k, (a, b) in enumerate(zip(pl, bl), 1):
        if "--rev" in sys.argv:
            if prx.search(a):
                key = (len(prx.findall(a)), tuple(sorted(collections.Counter(brx.findall(b)).items())))
                c[key] += 1
                if len(ex) < show: ex.append((p.name[:5], k, a, b))
        elif brx.search(b):
            key = (len(brx.findall(b)), tuple(sorted(collections.Counter(prx.findall(a)).items())))
            c[key] += 1
            if len(ex) < show: ex.append((p.name[:5], k, a, b))
for k, n in c.most_common(): print(n, k)
for e in ex: print(e[0], e[1], "\n   P:", e[2][:400], "\n   B:", e[3][:500])
