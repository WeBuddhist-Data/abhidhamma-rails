import re, os, sys
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PI = os.path.join(ROOT, "pali", "pi-1_split_chapters")
HI = os.path.join(ROOT, "hindi", "pi-1-hindi-plain-rails_split_chapters")
FILES = ["3-03-rupakandam.md", "4-01-nikkhepakandam.md", "4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"]
ID_RE = re.compile(r"\^([0-9a-z\-]+)\s*$")

def lines(path):
    with open(path, encoding="utf-8") as f:
        return [l.rstrip("\n") for l in f]

def pairs(fn):
    p = [l for l in lines(os.path.join(PI, fn)) if l.strip()]
    h = [l for l in lines(os.path.join(HI, fn)) if l.strip()]
    if len(p) != len(h):
        print("LINECOUNT", fn, len(p), len(h))
    out = []
    for a, b in zip(p, h):
        ma = ID_RE.search(a); mb = ID_RE.search(b)
        ia = ma.group(1) if ma else None
        ib = mb.group(1) if mb else None
        if ia != ib:
            print("IDMISMATCH", fn, ia, ib)
        out.append((ia, a, b))
    return out

def vnum(i):
    if i is None:
        return None
    m = re.match(r"1-(\d+)$", i)
    return int(m.group(1)) if m else None

def blanks(fn):
    # double blank lines
    res = []
    for root in (HI,):
        ls = lines(os.path.join(root, fn))
        for n in range(1, len(ls)):
            if not ls[n].strip() and not ls[n-1].strip():
                res.append(n+1)
    return res

if __name__ == "__main__":
    # dump: C_load.py file start end outfile (start/end on verse number; include None-id lines inside the range)
    outdir = os.path.dirname(os.path.abspath(__file__))
    for fn, s, e, tag in [("3-03-rupakandam.md", 870, 965, "C_d303"),
                          ("4-01-nikkhepakandam.md", 1030, 99999, "C_d401"),
                          ("4-02-nikkhepakandam.md", 0, 99999, "C_d402"),
                          ("4-03-nikkhepakandam.md", 0, 99999, "C_d403")]:
        ps = pairs(fn)
        with open(os.path.join(outdir, tag + ".txt"), "w", encoding="utf-8") as o:
            active = s == 0
            n = 0
            for i, a, b in ps:
                v = vnum(i)
                if v is not None:
                    active = s <= v <= e
                elif not active and s == 0:
                    active = True
                if active:
                    n += 1
                    o.write("P " + a + "\nH " + b + "\n\n")
        print(fn, "pairs", len(ps), "dumped", n, "blanks", blanks(fn), "ids", [p[0] for p in ps if p[0]][:3], [p[0] for p in ps if p[0]][-3:])
