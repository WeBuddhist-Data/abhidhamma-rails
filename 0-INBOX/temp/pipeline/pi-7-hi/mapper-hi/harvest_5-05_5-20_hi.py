"""Harvest single Pāli item word -> Hindi item piece from the Paṭicca frames of 5-05..5-20.
«X Y dhammaṃ paṭicca» | «X', Y' परिघटना पर निर्भर होकर»: split the Hindi on ", " (a piece starting with
«पर » or «और » joins the previous one) and pair word by word when the counts agree.
usage: python -I -B -X utf8 harvest_5-05_5-20_hi.py [filter-substring]
"""
import collections, pathlib, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_hindi, read_pali, lc

FILES = [f"5-{n:02d}" for n in range(5, 21)]
HERE = pathlib.Path(__file__).resolve().parent
flt = sys.argv[1] if len(sys.argv) > 1 else ""
pairs = collections.defaultdict(collections.Counter)
for kf in sorted(HERE.glob("5-*.keywords.md")):
    f = kf.name[: -len(".keywords.md")]
    if f[:4] not in FILES:
        continue
    a, b = read_pali(f), read_hindi(f)
    for bid, t in a.items():
        if bid not in b or t.startswith("#"):
            continue
        ps = re.findall(r"(?:^|[.–;?] |\n)(?:Siyā )?([A-ZĀa-zāīūṃṇñṭḍḷṅ ]+?) dhammaṃ paṭicca ", t)
        hs = re.findall(r"(?:^|[।–;?] |\n)(?:क्या )?([^।–;?\n]+?) परिघटना पर निर्भर होकर", b[bid])
        if len(ps) != len(hs):
            continue
        for x, y in zip(ps, hs):
            if "ñca" in x or " ca " in x:
                continue
            xs = x.split()
            ys = []
            for piece in y.split(", "):
                if ys and (piece.startswith("पर ") or piece.startswith("और ")):
                    ys[-1] += " " + piece
                else:
                    ys.append(piece)
            if len(xs) != len(ys):
                continue
            for p, h in zip(xs, ys):
                pairs[lc(p)][h.strip()] += 1
for p in sorted(pairs):
    if flt and flt not in p:
        continue
    print(p, "|", "; ".join(f"{h} ({c})" for h, c in pairs[p].most_common()))
