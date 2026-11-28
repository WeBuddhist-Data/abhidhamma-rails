"""pi-6 Russian word-senses sample (2026-11-27): agg-sample.tsv = the first 110 rows of agg-part1.tsv plus every
multi-value row of the book not already in them (pi-6 has few multi-value headwords; the map is very regular).
Also reports how many pi-6 headwords already have a line in the approved Russian senses files of pi-1 … pi-5
(case-insensitive).
usage: python -I -X utf8 -B senses_sample_ru.py
"""
import pathlib

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
S = ROOT / "0-INBOX/temp/pipeline/pi-6-ru/senses"
rows = (S / "agg-part1.tsv").read_text(encoding="utf-8").splitlines()
allrows = (S / "agg-all.tsv").read_text(encoding="utf-8").splitlines()
head = rows[:110]
names = {r.split("\t")[0] for r in head}
sample = head + [r for r in allrows if " | " in r.split("\t")[2] and r.split("\t")[0] not in names]
(S / "agg-sample.tsv").write_text("\n".join(sample) + "\n", encoding="utf-8", newline="\n")
multi = sum(1 for r in sample if " | " in r.split("\t")[2])
prior = {}
for b in "12345":
    f = ROOT / f"AI_translation/russian/pi-{b}-pali-word-russian-senses-plain.md"
    for l in f.read_text(encoding="utf-8").splitlines():
        if ": {" in l:
            prior.setdefault(l.split(": {", 1)[0].lower(), b)
inprior = sum(1 for r in allrows if r.split("\t")[0].lower() in prior)
print("sample rows", len(sample), "multi-value", multi, "last sample headword", sample[-1].split("\t")[0])
print("pi-6 headwords", len(allrows), "also in pi-1 … pi-5 senses", inprior,
      "sample in prior", sum(1 for r in sample if r.split("\t")[0].lower() in prior))
