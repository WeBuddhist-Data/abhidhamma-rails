"""Inspection helper: Pāli «yathā [W] X-sadis…» clauses and the Burmese line's «…နှင့် တူ…» shapes."""
import pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"
BD = ROOT / ("AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters" if "--rails" in sys.argv else "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters")
for p in sorted(PD.glob("*.md")):
    pl = N(p.read_text(encoding="utf-8-sig")).splitlines(); bl = N((BD / p.name).read_text(encoding="utf-8")).splitlines()
    for k, (a, b) in enumerate(zip(pl, bl), 1):
        for m in re.finditer(r"(?i)yathā ((?:[\wāīūṃṅñṭḍṇḷ]+ )?)([\wāīūṃṅñṭḍṇḷ]*sadis[\wāīūṃṅñṭḍṇḷ]*)", a):
            sh = re.findall(r"\S*(?:ကဲ့သို့|၌|၏) [^()]{0,80}?နှင့် တူ\S*|\S*နှင့် တူ\S*", b)
            print(p.name[:5], k, "|", m.group(0), "|", " ;; ".join(x[-70:] for x in sh)[:300])
