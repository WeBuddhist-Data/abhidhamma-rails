"""pi-2 Russian word-senses sample (2026-11-17): agg-sample.tsv = the first 90 rows of agg-part1.tsv plus the next 30
multi-value rows of part 1 (as in pi-1). Also reports how many pi-2 headwords already have a line in the approved
pi-1 Russian senses file (case-insensitive).
usage: python -I -X utf8 senses_sample_ru.py
"""
import pathlib

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
S = ROOT / "0-INBOX/temp/pipeline/pi-2-ru/senses"
rows = (S / "agg-part1.tsv").read_text(encoding="utf-8").splitlines()
sample = rows[:90] + [r for r in rows[90:] if " | " in r.split("\t")[2]][:30]
(S / "agg-sample.tsv").write_text("\n".join(sample) + "\n", encoding="utf-8", newline="\n")
multi = sum(1 for r in sample if " | " in r.split("\t")[2])
pi1 = {l.split(": {", 1)[0].lower() for l in
       (ROOT / "AI_translation/russian/pi-1-pali-word-russian-senses-plain.md").read_text(encoding="utf-8").splitlines()
       if ": {" in l}
allrows = (S / "agg-all.tsv").read_text(encoding="utf-8").splitlines()
inpi1 = sum(1 for r in allrows if r.split("\t")[0].lower() in pi1)
print("sample rows", len(sample), "multi-value", multi, "last sample headword", sample[-1].split("\t")[0])
print("pi-2 headwords", len(allrows), "also in pi-1 senses", inpi1,
      "sample in pi-1", sum(1 for r in sample if r.split("\t")[0].lower() in pi1))
