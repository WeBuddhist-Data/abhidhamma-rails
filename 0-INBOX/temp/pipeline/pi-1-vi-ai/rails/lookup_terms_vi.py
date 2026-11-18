"""Helper: print the locked termbase entries for the Pāli keywords / tokens of given segments.

usage: python -I -X utf8 lookup_terms_vi.py <pali_file> [<pali_file> ...] [--part N/M]
Prints each keyword (from the keyword-by-reference file) and each token of the Pāli that has a termbase entry,
once, in first-seen order.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / "AI_translation" / "vietnamese" / "pi-1-pali-vietnamese-termbase-plain.md"
KW = ROOT / "AI_translation" / "pali" / "pi-1-keywords-by-reference-pali-plain.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

args = [a for a in sys.argv[1:] if not a.startswith("--")]
part = None
if "--part" in sys.argv:
    part = sys.argv[sys.argv.index("--part") + 1]
    args = [a for a in args if a != part]

tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    if ": {" in line:
        w, body = line.split(": {", 1)
        tb[w] = body[:-1]
tb_ci = {k.lower(): k for k in tb}

kw = {}
for line in KW.read_text(encoding="utf-8").splitlines():
    if line.startswith("["):
        i, body = line.split("] ", 1)
        kw[i[1:]] = [k for x in body.split(", ") for k in x.split(" / ")]

order, seen = [], set()
for f in args:
    text = pathlib.Path(f).read_text(encoding="utf-8")
    for line in text.splitlines():
        m = ID.search(line)
        toks = re.findall(r"[^\W\d_]+", re.sub(r"\[[^\]]*\]", "", line))
        for t in toks:
            k = tb_ci.get(t.lower())
            if k and k not in seen:
                seen.add(k)
                order.append(k)
        if m:
            for k in kw.get(m.group(1), []):
                kk = tb_ci.get(k.lower())
                if kk and kk not in seen:
                    seen.add(kk)
                    order.append(kk)
if part:
    n, mm = map(int, part.split("/"))
    size = -(-len(order) // mm)
    order = order[(n - 1) * size: n * size]
for k in order:
    print(f"{k}: {tb[k]}")
print(f"# {len(order)} entries", file=sys.stderr)
