"""For the keys harmonise_tables.py reports: how often each Pāli key occurs (whole word, case-insensitive first
letter) in the Pāli chapters each generator writes, next to that generator's Burmese form: the «majority» of the
precedence rule. Reads harmonise_tables.py's output on stdin.
usage: python3 -I -X utf8 harmonise_tables.py | python3 -I -X utf8 harmonise_count.py"""
import collections, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
PD = HERE.parents[3] / "AI_translation/pali/pi-1_split_chapters"
OWN = {"sample": ["prea", "1-ma"], "ch2-01": ["2-01"], "ch2-02-03": ["2-02", "2-03"],
       "ch2-04-05": ["2-04", "2-05"], "ch3": ["3-01", "3-02", "3-03"], "ch4": ["4-01", "4-02", "4-03"], "ch5": ["5-at"]}
TXT = {p.name[:4]: p.read_text(encoding="utf-8-sig") for p in PD.glob("*.md")}
key, rows = None, collections.defaultdict(list)
for line in sys.stdin:
    line = line.rstrip("\n")
    if not line or line.startswith("Pāli keys"):
        continue
    if not line.startswith("   "):
        key = line
        continue
    my, _, where = line.strip().partition("   <- ")
    gens = sorted({w.split(":")[0] for w in where.split(", ")})
    rows[key].append((my, gens))
for k, forms in rows.items():
    rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])[" + k[0].upper() + k[0] + "]" + re.escape(k[1:]) + r"(?![\wāīūṃṅñṭḍṇḷ])")
    out = []
    for my, gens in forms:
        n = sum(len(rx.findall(TXT[c])) for g in gens for c in OWN.get(g, []))
        out.append(f"{n:4d}  {my[:90]}  <- {','.join(gens)}")
    print(k)
    print("\n".join(out))
