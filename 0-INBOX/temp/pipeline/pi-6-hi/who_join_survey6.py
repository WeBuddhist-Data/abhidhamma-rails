"""Survey how multi-chunk WHO phrases are joined in each file (answer sentences of the pavatti sections).
WHO_hi = prefix of a Hindi answer sentence up to the last 'में' before the first process verb.
usage: python -I -X utf8 who_join_survey6.py [--bak] [--show=<file prefix>] [--n=5]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C

SH = re.compile(r"(?<=[।?])\s+")
VERB = re.compile(r" (उत्पन्न|समाप्त|सोई|छोड़ी) ")


def who_hi(s):
    m = VERB.search(s)
    if not m:
        return None
    pre = s[:m.start()]
    k = pre.rfind(" में")
    if k < 0:
        return None
    e = k + len(" में")
    if e < len(pre) and pre[e] not in " ,":
        return None
    return pre[:e]


def pieces(w):
    """split on ', ' and merge pieces that do not end in में/समय into the following piece"""
    raw = w.split(", ")
    out, buf = [], ""
    for r in raw:
        buf = (buf + ", " + r) if buf else r
        if buf.endswith(("में", "समय")):
            out.append(buf); buf = ""
    if buf:
        out.append(buf)
    return out


if __name__ == "__main__":
    opt = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
    if "--bak" in sys.argv:
        C.CUR["hdir"] = C.BAK
    show = opt.get("show")
    n = int(opt.get("n", 5))
    for part in C.PARTS:
        if part.startswith(("preamble", "1-", "7-")):
            continue
        cnt = collections.Counter()
        ex = collections.defaultdict(list)
        for p, h in C.pairs(part):
            if p.startswith("#"):
                continue
            for s in SH.split(C.norm(h)):
                if s.endswith("?"):
                    continue
                w = who_hi(s)
                if not w:
                    continue
                ps = pieces(w)
                if len(ps) < 2 and " और " not in w:
                    cnt["single"] += 1
                    continue
                has_and = re.search(r"(में|समय|वालों|प्राणियों|लोगों) और ", w) or any(x.startswith("और ") for x in ps)
                if len(ps) >= 2 and not has_and:
                    k = "comma-only"
                elif len(ps) >= 2:
                    k = "comma+और"
                else:
                    k = "और-only"
                if re.search(r"(वालों|प्राणियों|लोगों)(?= और |, )", w):
                    k += "+dropped-में"
                cnt[k] += 1
                ex[k].append(w)
        print(C.short(part), dict(cnt))
        if show and part.startswith(show):
            for k, v in ex.items():
                print("  ==", k)
                for w in v[:n]:
                    print("    ", w)
