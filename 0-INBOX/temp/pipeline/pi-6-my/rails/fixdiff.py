"""Inspection helper (read only): lines changed in the pi-6 rails against the pre-fix rails (review/fix-backup/rails-text)
or, with --zs, against the zero-shot; per chapter, and with --show N up to N changed lines per chapter (Pāli, old, new).
usage: fixdiff.py [--zs] [--show N] [--grep REGEX (only lines whose new Burmese matches)]"""
import difflib, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
PALI = ROOT / "AI_translation/pali/pi-6_split_chapters"
NEW = ROOT / "AI_translation/burmese/pi-6-burmese-plain-rails_split_chapters"
OLD = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters" if "--zs" in sys.argv \
    else HERE.parent / "review/fix-backup/rails-text"
show = int(sys.argv[sys.argv.index("--show") + 1]) if "--show" in sys.argv else 0
gr = re.compile(sys.argv[sys.argv.index("--grep") + 1]) if "--grep" in sys.argv else None
tot = 0
for p in sorted(PALI.glob("*.md")):
    pl = N(p.read_text(encoding="utf-8-sig")).split("\n")
    a = N((OLD / p.name).read_text(encoding="utf-8")).split("\n")
    b = N((NEW / p.name).read_text(encoding="utf-8")).split("\n")
    ch = [k for k in range(max(len(a), len(b))) if (a[k] if k < len(a) else None) != (b[k] if k < len(b) else None)]
    if gr:
        ch = [k for k in ch if gr.search(b[k])]
    tot += len(ch)
    if ch:
        print(f"{p.name[:-3]}\t{len(ch)}")
    for k in ch[:show]:
        x, y = a[k], b[k]
        print(f"  {k + 1} P: {pl[k]}")
        sm = difflib.SequenceMatcher(None, x, y, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != "equal":
                print(f"     - «{x[max(0, i1 - 25):i2 + 8]}»\n     + «{y[max(0, j1 - 25):j2 + 8]}»")
print(f"total\t{tot}")
