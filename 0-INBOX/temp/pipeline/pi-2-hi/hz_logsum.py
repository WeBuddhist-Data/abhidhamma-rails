"""Summarise harmonise-log.tsv: replacements per rule and chapter."""
import csv, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.reader(open(os.path.join(HERE, "harmonise-log.tsv"), encoding="utf-8"), delimiter="\t"))[1:]
d = collections.OrderedDict()
for r, chp, n, l in rows:
    d.setdefault(r, []).append(f"ch{chp.split('-')[0]} {n}")
for r, v in d.items():
    print(r, "|", ", ".join(v))
print(len(rows), "rows; total replacements", sum(int(x[2]) for x in rows), "; lines", sum(int(x[3]) for x in rows))
