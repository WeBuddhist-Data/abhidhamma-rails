"""Assemble the pi-6 Vietnamese keyword map from mapper-vi/<part>.mapped.md in the order of the Pāli
keyword file, then check ids / keywords / empty values. (copy of pi-5-vi-ai/mapper-vi/assemble_map_vi.py)
usage: python -I -X utf8 -B assemble_map_vi.py"""
import pathlib, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
D = ROOT / "0-INBOX/temp/pipeline/pi-6-vi-ai/mapper-vi"
P = ROOT / "AI_translation/pali/pi-6-keywords-by-reference-pali-plain.md"
OUT = ROOT / "AI_translation/vietnamese/pi-6-keywords-by-reference-pali-vietnamese-plain.md"

mapped = {}
for f in D.glob("*.mapped.md"):
    for line in f.read_text(encoding="utf-8").splitlines():
        if line.strip():
            sid = line[1:line.index("]")]
            if sid in mapped:
                sys.exit(f"duplicate id {sid}")
            mapped[sid] = line
src = [l for l in P.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
out, bad, empty = [], [], []
for l in src:
    sid, kws = l[1:].split("] ", 1)
    m = mapped.pop(sid, None)
    if m is None:
        sys.exit(f"missing id {sid}")
    pairs = [x.split("=", 1) for x in m.split("] ", 1)[1].split(", ")]
    if [k.strip() for k in kws.split(", ")] != [p[0] for p in pairs]:
        bad.append(sid)
    empty += [sid for p in pairs if len(p) < 2 or not p[1].strip()]
    out.append(m)
if mapped:
    sys.exit(f"extra ids {list(mapped)[:5]}")
OUT.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
nde = sum(l.count("(no direct equivalent)") for l in out)
print("lines", len(out), "bad", bad, "empty", empty, "NDE", nde)
