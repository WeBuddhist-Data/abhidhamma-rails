import re, sys, os

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PD = os.path.join(ROOT, "pali", "pi-1_split_chapters")
RD = os.path.join(ROOT, "russian", "pi-1-russian-plain-rails_split_chapters")
FILES = ["preamble.md", "1-matika.md", "2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md"]
IDRE = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def load(path):
    txt = open(path, encoding="utf-8").read()
    segs = []
    for block in re.split(r"\n\s*\n", txt.strip("\n")):
        lines = [l for l in block.split("\n") if l.strip()]
        if not lines:
            continue
        m = IDRE.search(lines[-1])
        sid = m.group(1) if m else None
        segs.append((sid, lines, block))
    return txt, segs


def strip_id(l):
    return IDRE.sub("", l).strip()


def split_pieces(l, lang):
    l = strip_id(l)
    if lang == "pi":
        parts = re.split(r"(?<=\?)\s+|\s+–\s+|;\s+", l)
    else:
        parts = re.split(r"(?<=\?)\s+|,?\s+–\s+|;\s+", l)
    return [p.strip() for p in parts if p.strip()]


def norm_pi(p):
    return re.sub(r"^(Yo|Yā|Yaṃ|Yassa|Yā vā|Yo vā) ", "", p)


def structural():
    for f in FILES:
        pt, ps = load(os.path.join(PD, f))
        rt, rs = load(os.path.join(RD, f))
        print("==", f, "segs", len(ps), len(rs))
        if "\r" in rt:
            print("  CR present")
        if re.search(r"\n\s*\n\s*\n", rt):
            print("  double blank line")
        for i, ((pid, pl, _), (rid, rl, _)) in enumerate(zip(ps, rs)):
            if pid != rid:
                print("  ID mismatch", pid, rid)
            if len(pl) != len(rl):
                print("  linecount", pid, len(pl), len(rl))
            for a, b in zip(pl, rl):
                da = a.count("–") + a.count("—")
                db = b.count("–") + b.count("—")
                if da != db:
                    print("  dash", pid, da, db, "|", b[:80])
                pa = a.count("…pe…")
                ea = a.count("…") - 2 * pa
                eb = b.count("…")
                if pa + ea != eb:
                    print("  ellipsis", pid, pa, ea, eb, "|", b[:100])
                if a.count("?") != b.count("?"):
                    print("  qmark", pid, a.count("?"), b.count("?"), "|", b[:100])
                if re.search(r"(?<![А-Яа-яёЁ])ли(?![А-Яа-яёЁ])", b):
                    print("  LI", pid, b[:100])
                bb = re.sub(r"\[[^\]]*\]", "", strip_id(b))
                lat = re.findall(r"[A-Za-zĀāĪīŪūṃṄṅÑñṬṭḌḍṆṇḶḷ]{2,}", bb)
                if lat:
                    print("  latin", pid, lat)
                sb = strip_id(b)
                if sb and sb[-1] not in ".?…" and not sb.startswith("#"):
                    print("  end", pid, sb[-20:])
                if "  " in sb:
                    print("  dblspace", pid)
                # brackets count
                if a.count("[") != b.count("["):
                    print("  bracket", pid, a.count("["), b.count("["))
                if re.search(r"«[^»]*$", sb):
                    print("  unclosed quote", pid)
        if len(ps) != len(rs):
            print("  SEG COUNT DIFF")


def pairs(fsel, start=0, maxchars=28000):
    seen_line = {}
    seen_piece = {}
    out = []
    for f in FILES:
        pt, ps = load(os.path.join(PD, f))
        rt, rs = load(os.path.join(RD, f))
        for (pid, pl, _), (rid, rl, _) in zip(ps, rs):
            for a, b in zip(pl, rl):
                ka = strip_id(a)
                kb = strip_id(b)
                if ka in seen_line:
                    if seen_line[ka][0] != kb:
                        out.append((f, pid, "LINE-INCONS", ka, kb + "\n    PREV(" + seen_line[ka][1] + "): " + seen_line[ka][0]))
                    continue
                seen_line[ka] = (kb, pid)
                pa = split_pieces(a, "pi")
                pb = split_pieces(b, "ru")
                if len(pa) != len(pb):
                    out.append((f, pid, "NEWLINE(pieces %d/%d)" % (len(pa), len(pb)), ka, kb))
                    continue
                for x, y in zip(pa, pb):
                    nx = norm_pi(x)
                    if nx in seen_piece:
                        if seen_piece[nx][0] != y:
                            out.append((f, pid, "PIECE-INCONS", x, y + "\n    PREV(" + seen_piece[nx][1] + "): " + seen_piece[nx][0]))
                        continue
                    seen_piece[nx] = (y, pid)
                    out.append((f, pid, "new", x, y))
    sel = [o for o in out if fsel in o[0] or fsel == "all"]
    buf = ""
    i = start
    while i < len(sel):
        o = sel[i]
        s = "[%d] %s ^%s %s\n  P: %s\n  R: %s\n" % (i, o[0][:6], o[1], o[2], o[3], o[4])
        if len(buf) + len(s) > maxchars:
            break
        buf += s
        i += 1
    print(buf)
    print("NEXT", i, "OF", len(sel))


if __name__ == "__main__":
    if sys.argv[1] == "struct":
        structural()
    else:
        pairs(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 0)
