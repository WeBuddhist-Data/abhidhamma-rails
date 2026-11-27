"""scratch: forms.py PALI_RX FORM1 FORM2 ... -> per chapter: lines with the Pāli term, and how many contain each form."""
import pathlib, re, sys, collections
ROOT = pathlib.Path(__file__).resolve().parents[5]
PD = ROOT / "AI_translation/pali/pi-5_split_chapters"; MD = ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"
rx = re.compile(sys.argv[1]); forms = sys.argv[2:]
res = collections.defaultdict(lambda: collections.Counter())
key = lambda p: (int(p.name.split("-")[0]) if p.name[0].isdigit() else 0)
for p in sorted(PD.glob("*.md"), key=key):
    if p.suffix != ".md": continue
    ch = p.name.split("-")[0].split(".")[0]
    for x, y in zip(p.read_text(encoding="utf-8-sig").split("\n"), (MD / p.name).read_text(encoding="utf-8").split("\n")):
        if rx.search(x):
            res[ch]["lines"] += 1
            for f in forms:
                if re.search(f, y): res[ch][f] += 1
for ch, c in res.items(): print(ch, dict(c))
