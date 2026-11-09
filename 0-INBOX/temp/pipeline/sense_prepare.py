"""Aggregate a Pāli→<language> keyword map by Pāli headword and split it into parts for word-sense-grouper agents.
Generic version of hindi_sense_prepare.py.

usage: python -I -X utf8 sense_prepare.py <book number> <language> <lang tag> <audience slug> <n parts>
  e.g. python -I -X utf8 sense_prepare.py 3 hindi hi plain 1
in:  AI_translation/<language>/pi-N-keywords-by-reference-pali-<language>-<audience>.md
     AI_translation/english/pi-N-pali-word-english-senses-<audience>.md (optional; gives headword order + English tags)
out: 0-INBOX/temp/pipeline/pi-N-<tag>/senses/agg-partK.tsv
     headword <TAB> english_tags <TAB> value=count[ids] | … <TAB> NDE=<no-equivalent count>
"""
import collections, pathlib, sys

BOOK, LANG, TAG, AUD, N_PARTS = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5])
B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
MAP = B / f"AI_translation/{LANG}/pi-{BOOK}-keywords-by-reference-pali-{LANG}-{AUD}.md"
EN = B / f"AI_translation/english/pi-{BOOK}-pali-word-english-senses-{AUD}.md"
OUT = B / f"0-INBOX/temp/pipeline/pi-{BOOK}-{TAG}/senses"; OUT.mkdir(parents=True, exist_ok=True)
NDE = "(no direct equivalent)"

en_order, en_tags = [], {}
if EN.exists():
    for line in EN.read_text(encoding="utf-8-sig").splitlines():
        if ": {" in line:
            hw, body = line.split(": {", 1)
            if hw.lower() not in en_tags:
                en_order.append(hw); en_tags[hw.lower()] = body[:-1]

vals = collections.defaultdict(lambda: collections.defaultdict(list))
nde = collections.Counter()
first_seen = []
for line in MAP.read_text(encoding="utf-8-sig").splitlines():
    i, body = line.split("] ", 1); i = i[1:]
    for pair in body.split(", "):
        k, v = pair.split("=", 1)
        key = k.lower()
        if key not in vals and key not in nde:
            first_seen.append(k)
        if v == NDE:
            nde[key] += 1
        else:
            vals[key][v].append(i)

keys_all = {k.lower() for k in first_seen}
order = [h for h in en_order if h.lower() in keys_all]
seen = {h.lower() for h in order}
for k in first_seen:
    if k.lower() not in seen:
        order.append(k); seen.add(k.lower())
rows = []
for hw in order:
    v = vals.get(hw.lower(), {})
    if not v:
        continue  # only no-equivalent occurrences: omitted (skill step 4)
    cells = " | ".join(f"{r}={len(ids)}[{','.join(ids[:4])}{'…' if len(ids) > 4 else ''}]"
                       for r, ids in sorted(v.items(), key=lambda x: -len(x[1])))
    rows.append(f"{hw}\t{en_tags.get(hw.lower(), '')}\t{cells}\tNDE={nde.get(hw.lower(), 0)}")

size = -(-len(rows) // N_PARTS)
for n in range(N_PARTS):
    part = rows[n * size:(n + 1) * size]
    (OUT / f"agg-part{n + 1}.tsv").write_text("\n".join(part) + "\n", encoding="utf-8", newline="\n")
    print(f"part{n + 1}: {len(part)} headwords ({part[0].split(chr(9))[0]} … {part[-1].split(chr(9))[0]})")
omitted = sorted(k for k in nde if k not in vals)
print("headwords with values:", len(rows), "| only-no-equivalent (omitted):", len(omitted))
(OUT / "omitted-nde-only.txt").write_text("\n".join(omitted) + "\n", encoding="utf-8")
