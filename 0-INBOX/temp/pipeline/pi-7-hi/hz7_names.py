"""Inventory of triad / dyad / cluster names in headings and closing lines (Pāli stem -> Hindi X forms).
usage: python -I -B -X utf8 hz7_names.py [--bak]   -> writes names-inventory.txt
"""
import sys, re, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz7_common as C
from hz7_common import PARTS, pairs, pnorm, hnorm, short, HERE

PNUM = re.compile(r"^[\d\s\-–]+\.\s*")
HNUM = re.compile(r"^[\d\s\-–]+\.\s*")
END = re.compile(r"\s*(niṭṭhit(aṃ|o|ā)\.?)\s*$")


def ppart(s):
    s = pnorm(s).lstrip("#").strip().strip("*").strip()
    s = PNUM.sub("", s)
    closing = bool(END.search(s))
    s = END.sub("", s).strip().rstrip(".")
    return s, closing


SPLIT = re.compile(r"(?:ajjhattikaduka|.+?(?:ttikadvaya|ttika|duka|gocchaka))")


def split_p(s):
    if " " in s or "paṭṭhān" in s or re.search(r"ādi(?=duk|ttik|chag|gocch|pad)|ādi$|ādīni", s) \
            or not re.search(r"(ttik|duk|gocchak|dvay)(aṃ|a|āni)$", s):
        return None
    s = s.replace("-", "")
    s = s[0].lower() + s[1:]
    s = re.sub(r"(aṃ|āni)$", "a", s)
    s = re.sub(r"(duk|gocchak)āni", r"\1a", s)
    parts = SPLIT.findall(s)
    if "".join(parts) != s:
        return None
    return parts


def split_h(s):
    s = hnorm(s).lstrip("#").strip().strip("*").strip()
    s = HNUM.sub("", s)
    s = re.sub(r"\s*(समाप्त|पूरा हुआ|पूरे हुए)।?\s*$", "", s).strip().rstrip("।")
    return re.split(r"(?<=वर्गीकरण) और |(?<=वर्गीकरणों) और |(?<=वर्ग) और |(?<=वर्गों) और ", s)


def collect():
    inv = collections.defaultdict(lambda: collections.defaultdict(list))
    bad = []
    for part in PARTS:
        for i, (p, h) in enumerate(pairs(part)):
            ps, closing = ppart(p)
            if not (p.startswith("#") or closing):
                continue
            pp = split_p(ps)
            if not pp:
                continue
            hh = split_h(h)
            if len(pp) != len(hh):
                bad.append(f"{short(part)}:{i+1} {pp} | {hh}")
                continue
            for a, b in zip(pp, hh):
                inv[a][b].append(f"{short(part)}:{i+1}")
    return inv, bad


def main():
    if "--bak" in sys.argv:
        C.CUR["hdir"] = C.BAK
    inv, bad = collect()
    out = []
    for k in sorted(inv):
        v = inv[k]
        out.append(f"## {k}" + ("" if len(v) > 1 else "  (one form)"))
        for h, locs in sorted(v.items(), key=lambda kv: -len(kv[1])):
            files = sorted({l.split(":")[0] for l in locs})
            out.append(f"   [{len(locs)}] {h}   {' '.join(files)}")
    out.append("## UNSPLIT")
    out += bad
    open(os.path.join(HERE, "names-inventory.txt"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(len(inv), "stems;", len(bad), "unsplit")


if __name__ == "__main__":
    main()
