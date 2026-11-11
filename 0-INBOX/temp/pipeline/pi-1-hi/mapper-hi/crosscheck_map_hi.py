"""Cross-part check of the pi-1 Pāli→Hindi keyword maps.

(a) segments with identical Pāli (variant brackets and ^id stripped) whose mapped lines differ;
(b) per Pāli keyword, the Hindi values used and in how many lines, for keywords with 2+ values.
usage: python -I -X utf8 crosscheck_map_hi.py [--all]
"""
import collections, pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
D = ROOT / "0-INBOX/temp/pipeline/pi-1-hi/mapper-hi"
PALI = ROOT / "AI_translation/pali/pi-1_split_chapters"
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

seg = {}
for p in PARTS:
    buf = []
    for line in (PALI / f"{p}.md").read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            t = " ".join(buf)
            t = re.sub(r"\[[^\]]*\]", "", ID.sub("", t))
            seg[m.group(1)] = re.sub(r"\s+", " ", t).strip()
            buf = []

rows = []
for p in PARTS:
    for line in (D / f"{p}.mapped.md").read_text(encoding="utf-8").splitlines():
        i, body = line.split("] ", 1)
        rows.append((p, i[1:], body))

by_text = collections.defaultdict(list)
for p, sid, body in rows:
    by_text[seg[sid]].append((p, sid, body))
diff = [(t, v) for t, v in by_text.items() if len({b for _, _, b in v}) > 1]
print("(a) identical-Pāli segments with different maps:", len(diff))
for t, v in diff[:15]:
    print("  ", [(p[:4], s) for p, s, _ in v])

vals = collections.defaultdict(collections.Counter)
where = collections.defaultdict(lambda: collections.defaultdict(set))
for p, sid, body in rows:
    for pair in body.split(", "):
        k, h = pair.split("=", 1)
        vals[k][h] += 1
        where[k][h].add(p[:4])
multi = sorted(((k, c) for k, c in vals.items() if len(c) > 1), key=lambda x: -sum(x[1].values()))
print("(b) keywords with 2+ Hindi values:", len(multi), "of", len(vals))
lim = None if "--all" in sys.argv else 60
for k, c in multi[:lim]:
    print(f"  {k}: " + " | ".join(f"{h} ×{n} [{','.join(sorted(where[k][h]))}]" for h, n in c.most_common()))
