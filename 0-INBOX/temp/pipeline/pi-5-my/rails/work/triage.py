"""work helper: split the AUTO proposals into SAFE / REVIEW (see the criteria in the code)."""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parents[1]
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
import adherence_my as A
N = lambda s: unicodedata.normalize("NFC", s)
tb = A.parse_termbase(ROOT / "AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md")
P = A.segments(ROOT / "AI_translation/pali/pi-5_split_chapters")
dec = collections.defaultdict(str)
for l in open(HERE.parent / "termbase/decisions-A.tsv", encoding="utf-8"):
    if "\t" in l and not l.startswith("#"):
        f = N(l).rstrip("\n").split("\t")
        dec[f[0].split("|")[0].lower()] += " " + (f[2] if len(f) > 2 else "")
FLAG = re.compile(r"own entry|kept|name|fragment|only in|context|speaker|rails to|not this|another sense|departs|never occurs")
W = "a-zA-Zāīūṃṅñṭḍṇḷ"
safe, rev = [], []
for l in open(HERE / "work/auto.tsv", encoding="utf-8"):
    f = l.rstrip("\n").split("\t")
    if f[0] != "AUTO":
        continue
    i, kw, old, new, n = f[1], f[2], f[3], f[4], int(f[5])
    pc = len(re.findall(rf"(?<![{W}]){re.escape(kw.lower())}(?![{W}])", P[i].lower()))
    why = []
    if len(tb.get(kw.lower(), [])) > 1: why.append("multi-sense")
    if FLAG.search(dec[kw.lower()]): why.append("flag:" + FLAG.search(dec[kw.lower()]).group(0))
    if n != 1 and n != pc: why.append(f"count {n} vs Pāli {pc}")
    if len(old) < 3: why.append("short")
    (rev if why else safe).append("\t".join([i, kw, old, new, str(n)] + ([";".join(why)] if why else [])))
pathlib.Path(HERE / "work/safe.tsv").write_text("\n".join(safe) + "\n", encoding="utf-8")
pathlib.Path(HERE / "work/review.tsv").write_text("\n".join(rev) + "\n", encoding="utf-8")
print(len(safe), "safe;", len(rev), "review")
