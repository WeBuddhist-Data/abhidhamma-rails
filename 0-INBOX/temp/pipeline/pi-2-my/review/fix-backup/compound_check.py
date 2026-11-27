"""Inspection helper: for each adherence miss, the Pāli word(s) of the segment that contain the keyword as a part
(compound / inflected form) and have their own termbase entry; prints the entry's term and whether it occurs.
usage: compound_check.py adherence.txt [--rails]"""
import pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
import adherence_my as A
N = lambda s: unicodedata.normalize("NFC", s)
TB = A.parse_termbase(ROOT / "AI_translation/burmese/pi-2-pali-burmese-termbase-plain.md")
P = A.segments(ROOT / "AI_translation/pali/pi-2_split_chapters")
M = A.segments(ROOT / ("AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters" if "--rails" in sys.argv
                       else "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"))
W = r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+"
for l in open(sys.argv[1], encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) != 3 or not f[0][:1].isdigit(): continue
    i, kw = f[0], f[1]
    words = set(w for w in re.findall(W, P[i]) if kw.lower() in w.lower() and w.lower() != kw.lower())
    hits = []
    for w in sorted(words):
        t = TB.get(w.lower())
        if t:
            hits.append(f"{w}={'|'.join(t)}:{'Y' if any(A.occurs(x, M[i]) for x in t) else 'n'}")
    if hits:
        print(f"{i}\t{kw}\t{' ; '.join(hits)}")
