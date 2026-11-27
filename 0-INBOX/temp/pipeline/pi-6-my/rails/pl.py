"""Inspection helper (read only): aligned Pāli / Burmese lines of the pi-6 rails (or --zs zero-shot, --pre the pre-fix
rails backup) matching a Pāli regex and / or a Burmese regex.
usage: pl.py <pāli regex|-> [burmese regex|-] [--zs|--pre] [--max N] [--count] [--uniq] [--nb REGEX (Burmese must not match)]"""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
PALI = ROOT / "AI_translation/pali/pi-6_split_chapters"
if "--zs" in sys.argv:
    B = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
elif "--pre" in sys.argv:
    B = HERE.parent / "review/fix-backup/rails-text"
else:
    B = ROOT / "AI_translation/burmese/pi-6-burmese-plain-rails_split_chapters"
opt = lambda k, d=None: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d  # noqa: E731
args = [a for i, a in enumerate(sys.argv[1:], 1) if not a.startswith("--") and sys.argv[i - 1] not in ("--max", "--nb")]
rp = None if args[0] == "-" else re.compile(N(args[0]))
rb = None if len(args) < 2 or args[1] == "-" else re.compile(N(args[1]))
nb = re.compile(N(opt("--nb"))) if opt("--nb") else None
mx = int(opt("--max", 30))
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
n = 0
c = collections.Counter()
for p in sorted(PALI.glob("*.md")):
    pl = N(p.read_text(encoding="utf-8-sig")).split("\n")
    bl = N((B / p.name).read_text(encoding="utf-8")).split("\n")
    cur = None
    ids = {}
    for k in range(len(pl) - 1, -1, -1):
        m = ID.search(pl[k])
        if m:
            cur = m.group(1)
        if not pl[k].strip():
            cur = None if False else cur
        ids[k] = cur
    for k, x in enumerate(pl):
        if not x.strip():
            continue
        y = bl[k] if k < len(bl) else ""
        if rp and not rp.search(x):
            continue
        if rb and not rb.search(y):
            continue
        if nb and nb.search(y):
            continue
        n += 1
        if "--uniq" in sys.argv:
            c[(x, y)] += 1
            continue
        if n <= mx:
            print(f"{p.name[:-3]}:{k + 1} ^{ids.get(k)}\n  P: {x}\n  B: {y}")
if "--uniq" in sys.argv:
    for (x, y), v in c.most_common(mx):
        print(f"{v}×\n  P: {x}\n  B: {y}")
    print(f"{len(c)} distinct pairs")
print(f"{n} lines")
