"""Chapters 10-12 helper (prints only, writes nothing): run termbase_adherence_vi.py in memory, then list every keyword
miss in the segments of 10-bojjhangavibhango.md, 11-maggangavibhango.md and 12-jhanavibhango.md.
usage: python -I -X utf8 adherence_10_12.py
"""
import collections
import io
import pathlib
import re
import sys
from contextlib import redirect_stdout

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
SCRIPT = ROOT / "0-INBOX" / "temp" / "pipeline" / "termbase_adherence_vi.py"
KW = ROOT / "AI_translation" / "pali" / "pi-2-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation" / "vietnamese" / "pi-2-pali-vietnamese-termbase-plain.md"
DIR = ROOT / "AI_translation" / "vietnamese" / "pi-2-vietnamese-plain-rails_split_chapters"
CHS = ["10-bojjhangavibhango.md", "11-maggangavibhango.md", "12-jhanavibhango.md"]

sys.argv = [str(SCRIPT), str(KW), str(TB), str(DIR)]
ns = {"__name__": "adherence"}
buf = io.StringIO()
with redirect_stdout(buf):
    exec(compile(SCRIPT.read_text(encoding="utf-8"), str(SCRIPT), "exec"), ns)
seg, tb, present, variants = ns["seg"], ns["tb"], ns["present"], ns["variants"]
tb_ci = {k.lower(): v for k, v in tb.items()}
for ch in CHS:
    ids = set(re.findall(r"\^([0-9A-Za-z-]+)\s*$", (DIR / ch).read_text(encoding="utf-8"), re.M))
    total = 0
    misses = collections.defaultdict(list)
    for line in KW.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        i, body = line.split("] ", 1)
        i = i[1:]
        if i not in ids or i not in seg:
            continue
        for k in body.split(", "):
            for kk in k.split(" / "):
                terms = tb.get(kk) or tb_ci.get(kk.lower())
                if not terms:
                    continue
                total += 1
                if not any(present(v, seg[i]) for t in terms for v in variants(t)):
                    misses[(kk, " | ".join(terms))].append(i)
    n = sum(len(v) for v in misses.values())
    print(f"{ch}: {total} keyword occurrences, {n} misses ({100 * n / max(total, 1):.1f}%)")
    for (k, t), v in sorted(misses.items(), key=lambda x: -len(x[1])):
        print(f"{len(v):4d}  {k} -> {t}   {', '.join(v)}")
