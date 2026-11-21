"""r3 review helper: print aligned Pali / Vietnamese / (optional) Tinh Su segments to console
and run mechanical checks. Writes nothing.
usage: python -I -X utf8 -B r3_align.py <chapter-stem> [--ts] [--checks-only] [--from ID] [--to ID]
"""
import re, sys
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PI = ROOT + r"\AI_translation\pali\pi-5_split_chapters\%s.md"
VI = ROOT + r"\AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\%s.md"
TS = ROOT + r"\1-SOURCES\Translations\Vietnamese\vi-5-tinh_su.md"
IDRE = re.compile(r"\s\^(5-[0-9-]+)\s*$")


def segs(path):
    out, cur = [], []
    with open(path, encoding="utf-8") as f:
        for ln in f:
            ln = ln.rstrip("\n")
            if not ln.strip():
                continue
            if ln.startswith("---") and not out and not cur:
                continue
            cur.append(ln)
            m = IDRE.search(ln)
            if m:
                out.append((m.group(1), cur))
                cur = []
    return out


def ts_map():
    d = {}
    for i, l in segs(TS):
        d[i] = l
    return d


def cnt(pat, s, fl=0):
    return len(re.findall(pat, s, fl))


def checks(pid, pl, vl):
    p = "\n".join(pl)
    v = "\n".join(vl)
    probs = []
    if len(pl) != len(vl):
        probs.append("LINES %d/%d" % (len(pl), len(vl)))
    a = cnt(r"Āmantā", p)
    b = cnt(r"Đúng vậy", v)
    if a != b:
        probs.append("AMANTA %d/%d" % (a, b))
    a = cnt(r"[Nn]a hevaṃ vattabb", p)
    b = cnt(r"[Kk]hông nên nói như (vậy|thế)", v)
    if a != b:
        probs.append("NAHEVAM %d/%d" % (a, b))
    if cnt(r"như thế\b", v):
        probs.append("NHUTHE %d" % cnt(r"như thế\b", v))
    a = cnt(r"\?", p)
    b = cnt(r"\?", v)
    if a != b:
        probs.append("Q %d/%d" % (a, b))
    a = cnt(r"[–—]", p)
    b = cnt(r"[–—]", v)
    if a != b:
        probs.append("DASH %d/%d" % (a, b))
    a = cnt(r"…pe…|\.\.\.pe\.\.\.", p)
    b = cnt(r"…", v) - cnt(r"…", re.sub(r"…pe…", "", p))
    # number of ellipses in vi vs pali pe + bare ellipses
    a2 = a + cnt(r"…", re.sub(r"…pe…", "", p))
    b2 = cnt(r"…", v)
    if a2 != b2:
        probs.append("ELL %d/%d" % (a2, b2))
    if "….".replace("", "") in v and re.search(r"…\.(?!\.)", v):
        probs.append("ELLDOT")
    a = cnt(r"\bnanu\b", p, re.I)
    b = cnt(r"[Cc]hẳng phải", v)
    if a != b:
        probs.append("NANU %d/%d" % (a, b))
    a = cnt(r"\bhañci\b", p, re.I)
    b = cnt(r"\bNếu\b|\bnếu\b", v)
    if a > b:
        probs.append("HANCI %d/%d" % (a, b))
    # negation estimate
    pn = cnt(r"\b(na|no|natthi|nāhosi|nāssa|neva|nāpi|nevā|nattha|nāyaṃ|nāsi|nāhaṃ|nayidaṃ)\b", p, re.I) - cnt(r"[Nn]a hevaṃ", p)
    vn = cnt(r"\b(không|chưa|chẳng|chớ|đừng)\b", v, re.I) - cnt(r"không\?", v) - cnt(r"[Kk]hông nên nói như", v) - cnt(r"[Cc]hẳng phải", v)
    pn -= cnt(r"\bnanu\b", p, re.I)
    if pn != vn:
        probs.append("NEG~ %d/%d" % (pn, vn))
    if re.search(r"[āīūṃṅñṭḍṇḷ]", re.sub(r"\[[^\]]*\]", "", v)):
        probs.append("PALI-OUTSIDE-BRACKETS")
    if re.search(r'"', v):
        probs.append("STRAIGHTQUOTE")
    if re.search(r"\s[.,;:?!]", v):
        probs.append("SPACEPUNCT")
    for i, l in enumerate(vl):
        if l.startswith("#"):
            continue
        t = IDRE.sub("", l).rstrip()
        if t and t[-1] not in ".?…”’–:" :
            probs.append("END(%d)'%s'" % (i, t[-1]))
    return probs


def main():
    args = sys.argv[1:]
    ch = args[0]
    show_ts = "--ts" in args
    only = "--checks-only" in args
    fr = args[args.index("--from") + 1] if "--from" in args else None
    to = args[args.index("--to") + 1] if "--to" in args else None
    ps = segs(PI % ch)
    vs = segs(VI % ch)
    tm = ts_map() if show_ts else {}
    if [i for i, _ in ps] != [i for i, _ in vs]:
        print("ID MISMATCH")
    on = fr is None
    for (pid, pl), (vid, vl) in zip(ps, vs):
        if pid == fr:
            on = True
        if not on:
            continue
        pr = checks(pid, pl, vl)
        if only:
            if pr:
                print(pid, " | ".join(pr))
        else:
            print("=" * 20, pid, " ".join(pr))
            for k in range(max(len(pl), len(vl))):
                print("P%d: %s" % (k, pl[k] if k < len(pl) else "<none>"))
                print("V%d: %s" % (k, vl[k] if k < len(vl) else "<none>"))
            if show_ts:
                for l in tm.get(pid, ["<no TS>"]):
                    print("T : " + l)
        if pid == to:
            break


main()
