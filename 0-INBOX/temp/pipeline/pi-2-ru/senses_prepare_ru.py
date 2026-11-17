# adapted 2026-11-17 from pi-1-ru/senses_prepare_ru.py (pi-1 -> pi-2 paths only)
"""Aggregate the pi-2 Pāli→Russian keyword map by Pāli headword and split it into parts for the word-sense agents.

Column 2 carries English HINTS: the English equivalents the pi-2 English map gives that headword (top 5, with counts),
written `en≈ a ×n | b ×m`. They are hints for glossing only, not sense tags (pi-2 also has an English senses file,
AI_translation/english/pi-2-english-senses-plain.md, which the agents may read for tag wording).
Headwords: keys that differ only in letter case are merged; order = first appearance in the map.

usage: python -I -X utf8 senses_prepare_ru.py <n parts>
out:   0-INBOX/temp/pipeline/pi-2-ru/senses/agg-partK.tsv  (+ agg-all.tsv)
  headword <TAB> en hints <TAB> russian_value=count[ids] | … <TAB> NDE=<no-equivalent count>
"""
import collections, pathlib, sys

N_PARTS = int(sys.argv[1])
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
MAP = ROOT / "AI_translation/russian/pi-2-keywords-by-reference-pali-russian-plain.md"
EN = ROOT / "AI_translation/english/pi-2-keywords-by-reference-pali-english-plain.md"
OUT = ROOT / "0-INBOX/temp/pipeline/pi-2-ru/senses"
OUT.mkdir(parents=True, exist_ok=True)
NDE = "(no direct equivalent)"

en = collections.defaultdict(collections.Counter)
for line in EN.read_text(encoding="utf-8-sig").splitlines():
    if "] " not in line:
        continue
    for pair in line.split("] ", 1)[1].split(", "):
        if "=" not in pair:
            continue
        p, e = pair.rsplit("=", 1)
        for w in p.split(" / "):
            if w != NDE:
                en[w.strip().lower()][e] += 1

vals = collections.defaultdict(lambda: collections.defaultdict(list))
nde = collections.Counter()
order, seen = [], set()
for line in MAP.read_text(encoding="utf-8").splitlines():
    if "] " not in line:
        continue
    i, body = line.split("] ", 1)
    i = i[1:]
    for pair in body.split(", "):
        k, v = pair.split("=", 1)
        key = k.lower()
        if key not in seen:
            seen.add(key)
            order.append(k)
        if v == NDE:
            nde[key] += 1
        else:
            vals[key][v].append(i)

rows, omitted = [], []
for hw in order:
    key = hw.lower()
    v = vals.get(key, {})
    if not v:
        omitted.append(hw)
        continue
    cells = " | ".join(f"{r}={len(ids)}[{','.join(ids[:4])}{'…' if len(ids) > 4 else ''}]"
                       for r, ids in sorted(v.items(), key=lambda x: -len(x[1])))
    hint = " | ".join(f"{e} ×{n}" for e, n in en[key].most_common(5))
    rows.append(f"{hw}\t{'en≈ ' + hint if hint else ''}\t{cells}\tNDE={nde.get(key, 0)}")

(OUT / "agg-all.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
(OUT / "omitted-nde-only.txt").write_text("\n".join(omitted) + "\n", encoding="utf-8", newline="\n")
size = -(-len(rows) // N_PARTS)
for n in range(N_PARTS):
    part = rows[n * size:(n + 1) * size]
    (OUT / f"agg-part{n + 1}.tsv").write_text("\n".join(part) + "\n", encoding="utf-8", newline="\n")
    print(f"agg-part{n + 1}.tsv", len(part))
print("headwords", len(rows), "omitted (NDE only)", len(omitted), omitted[:10],
      "multi-value", sum(1 for r in rows if " | " in r.split("\t")[2]))
