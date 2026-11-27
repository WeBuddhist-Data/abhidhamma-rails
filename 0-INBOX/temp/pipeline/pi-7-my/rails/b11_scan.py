"""Inspection helper: the stacking form «A၊ B N» of two EXCLUSIVE qualifiers (B11) in a chapter folder.
A Burmese pair «X၊ Y» counts when Y is X negated (… ဖြစ်သော / … မဟုတ်သော, … ဖြစ်သော / … မဖြစ်သော, … ရှိသော /
… မရှိသော, …လာသော / …လာသည် မဟုတ်သော …) or one of the fixed pairs (အတွင်းပိုင်း / ပြင်ပ).
usage: b11_scan.py [folder] [--list]"""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"
BD = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else HERE.parent / "review/fix-backup/rails-text"
NEG = [("ဖြစ်သော", "မဟုတ်သော"), ("ဖြစ်သော", "မဖြစ်သော"), ("ရှိသော", "မရှိသော"), ("သော", "သည် မဟုတ်သော"),
       ("နိုင်သော", "နိုင်သော")]
PAIRS = [("အတွင်းပိုင်း", "ပြင်ပ"), ("မိမိ၌ ဖြစ်သော", "မိမိ၏ ပြင်ပ၌ ဖြစ်သော")]
RX = re.compile(r"(?:(?<=[ (“])|^)((?:\S+ ){0,4}?\S+)၊ ((?:\S+ ){0,5}\S+) ")


def negates(x, y):
    if (x, y) in PAIRS or (y, x) in PAIRS:
        return True
    for a, b in NEG:
        if x.endswith(a) and y.endswith(b):
            sx, sy = x[:-len(a)].strip(), y[:-len(b)].strip()
            if sx and sy and (sx == sy or sy == "မ" + sx or sy.replace(" မ", " ") == sx or
                              ("မ" + sx.split()[-1]) == sy.split()[-1] and sx.split()[:-1] == sy.split()[:-1]):
                return True
    return False


def scan(folder):
    hits = []
    for p in sorted(PD.glob("*.md")):
        bl = N((folder / p.name).read_text(encoding="utf-8")).split("\n")
        for k, b in enumerate(bl, 1):
            for m in RX.finditer(b):
                xs, ys = m.group(1).split(), m.group(2).split()
                found = False
                for i in range(len(xs)):
                    for j in range(1, len(ys) + 1):
                        x, y = " ".join(xs[i:]), " ".join(ys[:j])
                        if negates(x, y):
                            hits.append((p.name[:-3], k, x, y, b[m.end(2) + 1:m.end(2) + 40]))
                            found = True
                            break
                    if found:
                        break
    return hits


if __name__ == "__main__":
    h = scan(BD)
    c = collections.Counter((x, y) for _, _, x, y, _ in h)
    if "--list" in sys.argv:
        for r in h:
            print("\t".join(map(str, r)))
    for k, v in c.most_common():
        print(v, k)
    print("B11 stacks:", len(h))
