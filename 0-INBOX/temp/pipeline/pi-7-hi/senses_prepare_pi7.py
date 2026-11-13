"""Aggregate the pi-7 Pāli→Hindi keyword map by Pāli headword and split it into parts for the word-sense agents.

Like 0-INBOX/temp/pipeline/hindi_sense_prepare.py, but pi-7 has no English senses file, so column 2 carries
English HINTS instead: the English equivalents the pi-7 English map gives that headword (top 5, with counts),
written `en≈ a ×n | b ×m`. They are hints for glossing only, not sense tags.
Headwords: keys that differ only in letter case are merged; order = first appearance in the map.

usage: python -I -X utf8 senses_prepare_pi2.py <n parts>
out:   0-INBOX/temp/pipeline/pi-7-hi/senses/agg-partK.tsv  (+ agg-all.tsv)
  headword <TAB> en hints <TAB> hindi_value=count[ids] | … <TAB> NDE=<no-equivalent count>
"""
import collections, pathlib, sys

N_PARTS = int(sys.argv[1])
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
MAP = ROOT / "AI_translation/hindi/pi-7-keywords-by-reference-pali-hindi-plain.md"
EN = ROOT / "AI_translation/english/pi-7-keywords-by-reference-pali-english-plain.md"
OUT = ROOT / "0-INBOX/temp/pipeline/pi-7-hi/senses"
OUT.mkdir(parents=True, exist_ok=True)
NDE = "(no direct equivalent)"

en = collections.defaultdict(collections.Counter)
for line in EN.read_text(encoding="utf-8-sig").splitlines():
    if not line.strip():
        continue
    for pair in line.split("] ", 1)[1].split(", "):
        p, e = pair.rsplit("=", 1)
        for w in p.split(" / "):
            if w != NDE:
                en[w.strip().lower()][e] += 1

vals = collections.defaultdict(lambda: collections.defaultdict(list))
nde = collections.Counter()
order, seen = [], set()
for line in MAP.read_text(encoding="utf-8").splitlines():
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
