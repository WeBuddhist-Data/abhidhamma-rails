"""units.py REGEX [-n]: aligned (Pāli unit, Burmese unit) pairs where the Pāli unit fully matches REGEX
(units: split on ' – ' and on sentence ends before a capital / quote; Burmese on ' – ' and '။ ')."""
import pathlib, re, sys
R = pathlib.Path(__file__).resolve().parents[5]
P = R / "AI_translation/pali/pi-4_split_chapters"
M = R / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
SP = re.compile(r"( – |(?<=[.?!;])\s+(?=[A-ZĀĪŪṬḌṆÑṄṚ\"“]))")
SM = re.compile(r"( – |(?<=[။])\s+)")
def pairs():
    for p in sorted(P.glob("*.md")):
        for i, (x, y) in enumerate(zip(p.read_text(encoding="utf-8-sig").split("\n"), (M / p.name).read_text(encoding="utf-8").split("\n")), 1):
            if not x.strip() or x.startswith("#"):
                continue
            x, y = ID.sub("", x).strip(), ID.sub("", y).strip()
            x = re.sub(r"^\(\d+\) ", "", x); y = re.sub(r"^\(\d+\) ", "", y)
            xs = [s for s in SP.split(x) if s.strip() and s != " – "]
            ys = [s for s in SM.split(y) if s.strip() and s != " – "]
            if len(xs) != len(ys):
                yield p.name.split("-")[0], i, x, y, False
                continue
            for s, t in zip(xs, ys):
                yield p.name.split("-")[0], i, s, t, True
if __name__ == "__main__":
    rx = re.compile(sys.argv[1])
    for ch, i, s, t, ok in pairs():
        if ok and rx.fullmatch(s):
            print(f"{ch}:{i}\t{s}\t{t}")
        elif not ok and "-u" in sys.argv and rx.search(s):
            print(f"{ch}:{i} UNEVEN\t{s[:200]}\t{t[:200]}")

def search(rx, uneven=True):
    for ch, i, s, t, ok in pairs():
        if rx.search(s):
            yield ch, i, s, t, ok
