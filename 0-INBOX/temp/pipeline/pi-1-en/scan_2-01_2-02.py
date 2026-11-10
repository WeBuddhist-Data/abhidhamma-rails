"""Scan all ch.2 parts for the Koṭṭhāsavāra summary items (counts) so the builder covers every variant."""
import re, sys, pathlib, collections
D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-1_split_chapters")
items = collections.Counter()
for p in sorted(D.glob("2-0*.md")):
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.startswith("Tasmiṃ kho pana samaye"):
            body = line[len("Tasmiṃ kho pana samaye "):]
            body = body.split(";")[0]
            for it in re.split(r",\s*|…pe…", body):
                it = it.strip()
                if it:
                    items[it] += 1
for k, v in sorted(items.items()):
    print(v, k)
# also questions "Katam... tasmiṃ samaye ... honti?" headwords
qs = collections.Counter()
for p in sorted(D.glob("2-0*.md")):
    for m in re.finditer(r"Katam\w* tasmiṃ samaye ([^?…]+?) (?:hoti|honti)[?…]", p.read_text(encoding="utf-8")):
        qs[m.group(1)] += 1
print("----")
for k, v in sorted(qs.items()):
    print(v, k)
