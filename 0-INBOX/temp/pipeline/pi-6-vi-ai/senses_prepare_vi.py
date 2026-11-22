# adapted 2026-11-22 from pi-5-vi-ai/senses_prepare_vi.py (pi-6 paths; prior books pi-1 … pi-5)
"""Aggregate the pi-6 Pāli→Vietnamese keyword map by Pāli headword and split it into parts for the word-sense agents.

Column 2 carries English HINTS: the English equivalents the pi-6 English map gives that headword (top 5, with counts),
written `en≈ a ×n | b ×m`. They are hints for glossing only, not sense tags.
Headwords: keys that differ only in letter case are merged; order = first appearance in the map.
The literal placeholder keyword "(no direct equivalent)" is not a headword (it is skipped).
Sample: the first 90 rows of part 1 plus the next 30 multi-value rows of part 1.

usage: python -I -X utf8 -B senses_prepare_vi.py <n parts>
out:   0-INBOX/temp/pipeline/pi-6-vi-ai/senses/agg-partK.tsv, agg-all.tsv, agg-sample.tsv
  headword <TAB> en hints <TAB> vietnamese_value=count[ids] | … <TAB> NDE=<no-equivalent count>
"""
import collections, pathlib, sys

N_PARTS = int(sys.argv[1])
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
MAP = ROOT / "AI_translation/vietnamese/pi-6-keywords-by-reference-pali-vietnamese-plain.md"
EN = ROOT / "AI_translation/english/pi-6-keywords-by-reference-pali-english-plain.md"
OUT = ROOT / "0-INBOX/temp/pipeline/pi-6-vi-ai/senses"
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
placeholder = 0
for line in MAP.read_text(encoding="utf-8").splitlines():
    if "] " not in line:
        continue
    i, body = line.split("] ", 1)
    i = i[1:]
    for pair in body.split(", "):
        k, v = pair.split("=", 1)
        if k == NDE:
            placeholder += 1
            continue
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
parts = []
for n in range(N_PARTS):
    part = rows[n * size:(n + 1) * size]
    parts.append(part)
    (OUT / f"agg-part{n + 1}.tsv").write_text("\n".join(part) + "\n", encoding="utf-8", newline="\n")
    print(f"agg-part{n + 1}.tsv", len(part))
p1 = parts[0]
sample = p1[:90] + [r for r in p1[90:] if " | " in r.split("\t")[2]][:30]
(OUT / "agg-sample.tsv").write_text("\n".join(sample) + "\n", encoding="utf-8", newline="\n")
print("headwords", len(rows), "omitted (NDE only)", len(omitted), omitted[:10], "placeholder keywords skipped", placeholder,
      "multi-value", sum(1 for r in rows if " | " in r.split("\t")[2]))


def heads(n):
    p = ROOT / f"AI_translation/vietnamese/pi-{n}-pali-word-vietnamese-senses-plain.md"
    return {l.split(": {", 1)[0].lower() for l in p.read_text(encoding="utf-8").splitlines() if ": {" in l}


prior = set().union(*(heads(n) for n in (1, 2, 3, 4, 5)))
print("sample rows", len(sample), "multi-value", sum(1 for r in sample if " | " in r.split("\t")[2]),
      "last sample headword", sample[-1].split("\t")[0])
print("pi-6 headwords also in pi-1 … pi-5 vi senses", sum(1 for r in rows if r.split("\t")[0].lower() in prior),
      "sample in pi-1 … pi-5", sum(1 for r in sample if r.split("\t")[0].lower() in prior))
