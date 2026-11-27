"""Inspection helper (read only): counts of the Burmese windows (regex) in the segments of one missed keyword, and the
Pāli windows. usage: ctxc.py <adherence report> <keyword> <burmese regex> [pali regex] [--rails]"""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402
N = lambda s: unicodedata.normalize("NFC", s)
a = [x for x in sys.argv[1:] if not x.startswith("--")]
P = A.segments(ROOT / "AI_translation/pali/pi-6_split_chapters")
B = A.segments(ROOT / ("AI_translation/burmese/pi-6-burmese-plain-rails_split_chapters" if "--rails" in sys.argv else
                       "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"))
ids = [N(l).split("\t")[0].strip() for l in open(a[0], encoding="utf-8") if "\t" in l and N(l).split("\t")[1] == N(a[1])]
cb, cp, none = collections.Counter(), collections.Counter(), []
for i in ids:
    ms = [m.group(0) for m in re.finditer(N(a[2]), B[i])]
    if not ms: none.append(i)
    cb.update(set(ms))
    if len(a) > 3: cp.update(set(m.group(0) for m in re.finditer(N(a[3]), P[i])))
print(len(ids), "segments; no match:", none)
for k, v in cb.most_common(): print("  B", v, k)
for k, v in cp.most_common(): print("  P", v, k)
