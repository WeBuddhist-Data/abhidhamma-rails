"""Probe for parts 4-02 / 4-03: print Pāli of chosen 4-01 segments and the Vietnamese 4-01 builder gives them,
and list 4-02 / 4-03 Pāli sentences that also occur in 4-01 (to reuse the Vietnamese byte for byte).

usage: python -I -X utf8 probe_4-02_4-03_vi.py [ids...]
"""
import importlib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
G = importlib.import_module("build_4-01_vi")

P401 = dict(G.pali_segments())
V401 = dict(G.SEGMENTS)
PDIR = G.PALI.parent


def segs(name):
    out, buf = [], []
    for line in (PDIR / name).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = G.ID.search(line)
        if m:
            buf.append(line[:m.start()])
            out.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    return out


if __name__ == "__main__":
    ids = sys.argv[1:]
    if ids:
        for i in ids:
            print("==", i)
            for l in P401[i]:
                print("P:", l)
            for l in V401[i] or []:
                print("V:", l)
        sys.exit()
    sent401 = {}
    for bid, lines in P401.items():
        for l in lines:
            for s in re.split(r"(?<=[.?]) ", l):
                sent401.setdefault(s, bid)
    for part in ("4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"):
        for bid, lines in segs(part):
            for l in lines:
                for s in re.split(r"(?<=[.?]) ", l):
                    if s in sent401 and len(s) > 40:
                        print(bid, "=", sent401[s], ":", s[:90])
