"""Coordinator audit: every pavatti verb keyword in the pi-6 mapped files against the CURRENT map_2-01_vi.verb_value
(first-rendering rule). Read-only: prints the differences per file.
usage: python -I -X utf8 -B verb_audit_vi.py [part ...]   (default: every *.mapped.md)"""
import importlib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
M = importlib.import_module("map_2-01_vi")
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation/pali/pi-6_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def pali_segments(part):
    segs, buf = {}, []
    for line in (PALI / f"{part}.md").read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            segs[m.group(1)] = "\n".join(buf)
            buf = []
    return segs


parts = sys.argv[1:] or sorted(p.name[:-len(".mapped.md")] for p in HERE.glob("*.mapped.md"))
total = 0
for part in parts:
    segs = pali_segments(part)
    diffs = []
    for line in (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        sid = line[1:line.index("]")]
        body = line[line.index("]") + 2:]
        for pair in body.split(", "):
            if "=" not in pair:
                continue
            kw, val = pair.split("=", 1)
            want = M.verb_value(kw, segs.get(sid, ""))
            if want is not None and want != val:
                diffs.append((sid, kw, val, want))
    total += len(diffs)
    print(f"{part}: {len(diffs)} differences")
    for d in diffs[:8]:
        print("   ", d)
print("total", total)
