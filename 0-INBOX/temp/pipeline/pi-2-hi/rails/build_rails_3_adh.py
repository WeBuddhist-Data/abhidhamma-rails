"""Termbase adherence restricted to chapters 3, 14, 15 (same logic as hindi_termbase_adherence.py,
whose functions are loaded from that file without running its report).

usage: python -I -X utf8 build_rails_3_adh.py
"""
import collections
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
src = (ROOT / "0-INBOX/temp/pipeline/hindi_termbase_adherence.py").read_text(encoding="utf-8")
ns = {}
head = src.split("seg = {}")[0].replace("kw_path, tb_path, rails_dir = sys.argv[1:4]", "").replace(
    "report = sys.argv[4] if len(sys.argv) > 4 else None", "")
exec(head, ns)
stem, WORD = ns["stem"], ns["WORD"]
found_src = src[src.index("def found"):src.index("total = miss = 0")]
exec(found_src, ns)
found = ns["found"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
OUT = ROOT / "AI_translation/hindi/pi-2-hindi-plain-rails_split_chapters"
seg = {}
for ch in ("3-dhatuvibhango.md", "14-sikkhapadavibhango.md", "15-patisambhidavibhango.md"):
    buf = []
    for line in (OUT / ch).read_text(encoding="utf-8").splitlines():
        buf.append(line)
        m = ID.search(line)
        if m:
            seg[m.group(1)] = " ".join(buf)
            buf = []
tb = {}
for line in (ROOT / "AI_translation/hindi/pi-2-pali-hindi-termbase-plain.md").read_text(encoding="utf-8").splitlines():
    w, body = line.split(": {", 1)
    tb[w] = [s.rsplit(": ", 1)[1] for s in body[:-1].split("; ")]
tb_ci = {k.lower(): v for k, v in tb.items()}
total = miss = 0
misses = collections.defaultdict(list)
for line in (ROOT / "AI_translation/pali/pi-2-keywords-by-reference-pali-plain.md").read_text(encoding="utf-8").splitlines():
    i, body = line.split("] ", 1)
    i = i[1:]
    if i not in seg:
        continue
    words = WORD.findall(seg[i])
    for k in body.split(", "):
        for kk in k.split(" / "):
            terms = tb.get(kk) or tb_ci.get(kk.lower())
            if not terms:
                continue
            total += 1
            if not any(found(t, words) for t in terms):
                miss += 1
                misses[(kk, " | ".join(terms))].append(i)
print(f"checked {total}; misses {miss} ({100 * miss / max(total, 1):.1f}%)")
for (k, t), ids in sorted(misses.items(), key=lambda x: -len(x[1])):
    print(f"{len(ids):3} {k} -> {t}  {ids[:6]}")
