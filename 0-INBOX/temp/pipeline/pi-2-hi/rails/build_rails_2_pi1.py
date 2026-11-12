"""Helper (read-only): print pi-1 Pāli and rails Hindi side by side for given block ids, or for segments whose
Pāli matches a regex.

usage: python -I -X utf8 build_rails_2_pi1.py id <id> [<id> ...]
       python -I -X utf8 build_rails_2_pi1.py re <regex> [max]
       python -I -X utf8 build_rails_2_pi1.py book <n> re <regex> [max]   (n = 3/4/5: pi-N rails Hindi merged file not aligned; prints Hindi lines matching)
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
PALI = ROOT / "pali" / "pi-1_split_chapters"
HI = ROOT / "hindi" / "pi-1-hindi-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(path):
    out, buf = {}, []
    order = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            out[m.group(1)] = buf
            order.append(m.group(1))
            buf = []
    return out, order


P, H, ORDER = {}, {}, []
for f in sorted(PALI.glob("*.md")):
    if f.name == "preamble.md" or not (HI / f.name).exists():
        continue
    p, o = segs(f)
    h, _ = segs(HI / f.name)
    P.update(p)
    H.update(h)
    ORDER += o


def show(i):
    for a, b in zip(P[i], H.get(i, [])):
        print("P:", a)
        print("H:", b)
    print()


if sys.argv[1] == "id":
    for i in sys.argv[2:]:
        show(i)
elif sys.argv[1] == "re":
    rx = re.compile(sys.argv[2])
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    n = 0
    for i in ORDER:
        for a, b in zip(P[i], H.get(i, [])):
            if rx.search(a):
                print(f"[{i}]")
                print("P:", a)
                print("H:", b)
                print()
                n += 1
                break
        if n >= mx:
            break
