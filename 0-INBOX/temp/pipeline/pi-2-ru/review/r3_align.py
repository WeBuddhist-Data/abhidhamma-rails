import re, sys
BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PI = BASE + r"\pali\pi-2_split_chapters\\"
RU = BASE + r"\russian\pi-2-russian-plain-rails_split_chapters\\"
IDRE = re.compile(r"\^([0-9a-z-]+)\s*$")

def segs(path):
    txt = open(path, encoding="utf-8").read()
    out = []
    cur = []
    for line in txt.split("\n"):
        if not line.strip():
            continue
        cur.append(line)
        m = IDRE.search(line)
        if m:
            out.append((m.group(1), cur))
            cur = []
    if cur:
        out.append(("TAIL", cur))
    return out, txt

def load(ch):
    p, pt = segs(PI + ch)
    r, rt = segs(RU + ch)
    return p, r, pt, rt

if __name__ == "__main__":
    ch = sys.argv[1]
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    end = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
    p, r, pt, rt = load(ch)
    print("segs", len(p), len(r))
    if "\r" in rt: print("CR in ru")
    if "\n\n\n" in rt: print("double blank in ru")
    for i, ((pid, pl), (rid, rl)) in enumerate(zip(p, r)):
        if pid != rid or len(pl) != len(rl):
            print("MISMATCH", i, pid, rid, len(pl), len(rl))
    for i in range(start, min(end, len(p))):
        pid, pl = p[i]; rid, rl = r[i]
        print(f"=== [{i}] {pid}")
        for a, b in zip(pl, rl):
            print("P:", a)
            print("R:", b)
