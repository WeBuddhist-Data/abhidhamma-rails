"""Show Pāli + Russian segments by block ID (read-only).
usage: python -I -X utf8 fx_show.py <id>[@pali_sub@ru_sub] ...   (id without caret)
With @subs, only a window of ±W chars around each substring is printed (W from env FXW, default 250)."""
import os, pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation/pali/pi-2_split_chapters"
RU = ROOT / "AI_translation/russian/pi-2-russian-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
W = int(os.environ.get("FXW", "250"))


def segs(p):
    out, cur = {}, []
    for line in p.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        cur.append(line)
        m = ID.search(line)
        if m:
            out[m.group(1)] = (p.name, cur)
            cur = []
    return out


def show(tag, lines, sub):
    for k, line in enumerate(lines, 1):
        if not sub:
            print(f"  {tag}{k}:", line)
            continue
        for m in re.finditer(re.escape(sub), line):
            a, b = max(0, m.start() - W), min(len(line), m.end() + W)
            print(f"  {tag}{k}: …{line[a:b]}…")


P, R = {}, {}
for p in sorted(PALI.glob("*.md")):
    P.update(segs(p))
    R.update(segs(RU / p.name))
for arg in sys.argv[1:]:
    parts = arg.split("@")
    i = parts[0]
    ps = parts[1] if len(parts) > 1 else ""
    rs = parts[2] if len(parts) > 2 else ""
    if i not in P:
        print("??", i)
        continue
    print(f"=== {i} ({P[i][0]}) P-lines {len(P[i][1])} R-lines {len(R[i][1])}")
    show("P", P[i][1], ps)
    show("R", R[i][1], rs)
