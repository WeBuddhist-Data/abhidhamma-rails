"""Helper: termbase adherence restricted to the segments of one chapter file, listing every miss with its segment.
Same matching logic as 0-INBOX/temp/pipeline/termbase_adherence_vi.py (its functions are reused by exec of its
definitions, nothing is written).

usage: python -I -X utf8 adh_2-03_vi.py <chapter.md>
"""
import pathlib
import sys

PIPE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline")
ROOT = PIPE.parents[2]
KW = ROOT / "AI_translation" / "pali" / "pi-1-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation" / "vietnamese" / "pi-1-pali-vietnamese-termbase-plain.md"

src = (PIPE / "termbase_adherence_vi.py").read_text(encoding="utf-8")
defs = src.split("seg = {}", 1)[0].replace("kw_path, tb_path, rails_dir = sys.argv[1:4]", "").replace(
    "report = sys.argv[4] if len(sys.argv) > 4 else None", "")
ns = {}
exec(defs, ns)
norm, present, variants, ID = ns["norm"], ns["present"], ns["variants"], ns["ID"]

seg, buf = {}, []
for line in pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    buf.append(line)
    m = ID.search(line)
    if m:
        seg[m.group(1)] = norm(" ".join(buf))
        buf = []
tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    if ": {" in line:
        w, body = line.split(": {", 1)
        tb[w] = [s.rsplit(": ", 1)[1] for s in body[:-1].split("; ")]
tb_ci = {k.lower(): v for k, v in tb.items()}
total = miss = 0
for line in KW.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    i, body = line.split("] ", 1)
    i = i[1:]
    if i not in seg:
        continue
    for k in body.split(", "):
        for kk in k.split(" / "):
            terms = tb.get(kk) or tb_ci.get(kk.lower())
            if not terms:
                continue
            total += 1
            if not any(present(v, seg[i]) for t in terms for v in variants(t)):
                miss += 1
                print(f"^{i}: {kk} -> {' | '.join(terms)}")
print(f"checked {total} keyword occurrences in {len(seg)} segments; {miss} misses")
