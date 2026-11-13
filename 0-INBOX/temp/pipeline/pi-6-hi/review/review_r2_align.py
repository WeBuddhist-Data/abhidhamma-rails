import re, sys, os
BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
FILES = [f"3-0{i}-ayatanayamaka.md" for i in range(1, 7)]
IDRE = re.compile(r"\^([0-9a-z-]+)\s*$")

def load(path):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    return raw, [l.rstrip("\n") for l in raw.split("\n")]

def nonempty(lines):
    return [(i + 1, l) for i, l in enumerate(lines) if l.strip()]

def pairs(f):
    _, pl = load(os.path.join(BASE, "pali", "pi-6_split_chapters", f))
    _, hl = load(os.path.join(BASE, "hindi", "pi-6-hindi-plain-rails_split_chapters", f))
    return nonempty(pl), nonempty(hl)

if __name__ == "__main__":
    for f in FILES:
        praw, pl = load(os.path.join(BASE, "pali", "pi-6_split_chapters", f))
        hraw, hl = load(os.path.join(BASE, "hindi", "pi-6-hindi-plain-rails_split_chapters", f))
        P, H = nonempty(pl), nonempty(hl)
        print(f"== {f}: pali {len(P)} hindi {len(H)} nonempty lines")
        if "\n\n\n" in hraw:
            print("  DOUBLE BLANK in hindi")
        # blank line structure
        pb = [i for i, l in enumerate(pl) if not l.strip()]
        hb = [i for i, l in enumerate(hl) if not l.strip()]
        if len(pl) != len(hl) or pb != hb:
            print("  blank-line structure differs", len(pl), len(hl))
        for k, ((pn, p), (hn, h)) in enumerate(zip(P, H)):
            pid = IDRE.search(p); hid = IDRE.search(h)
            pid = pid.group(1) if pid else None
            hid = hid.group(1) if hid else None
            if pid != hid:
                print(f"  ID mismatch nonempty#{k+1}: {pid} vs {hid}")
            pt = IDRE.sub("", p).rstrip(); ht = IDRE.sub("", h).rstrip()
            if pt.startswith("#") != ht.startswith("#") or (pt.startswith("#") and len(pt) - len(pt.lstrip("#")) != len(ht) - len(ht.lstrip("#"))):
                print(f"  heading level mismatch #{k+1}")
            if not pt.startswith("#"):
                pe = pt[-1:] ; he = ht[-1:]
                if pe == "?" and he != "?":
                    print(f"  end ? mismatch #{k+1} L{hn}: {ht[-30:]}")
                if pe == "." and he != "।":
                    print(f"  end . mismatch #{k+1} L{hn}: {pe!r} {ht[-30:]}")
                if pe not in "?." :
                    print(f"  pali end {pe!r} hindi end {he!r} #{k+1} L{hn}")
            pd = len(re.findall(r"[–—]", pt)); hd = len(re.findall(r"[–—]", ht))
            if pd != hd:
                print(f"  dash count {pd} vs {hd} #{k+1} L{hn}")
            if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", re.sub(r"\((?:[^()]*)\)", "", ht)):
                print(f"  latin in hindi #{k+1} L{hn}: {ht[:80]}")
            if re.search(r"[\"']", ht):
                print(f"  straight quote #{k+1} L{hn}")
            if "pe" in pt and "…" not in ht:
                print(f"  pe missing #{k+1} L{hn}")
            if pt.count("…pe…") != ht.count("…"):
                print(f"  pe count {pt.count('…pe…')} vs {ht.count('…')} #{k+1} L{hn}")
            if "  " in ht:
                print(f"  double space #{k+1} L{hn}")
