"""r3 review helper: compressed aligned reading view (console only, writes nothing).
Splits each Pali/Vietnamese line pair at '?' into question units; a Pali unit already seen with the
same Vietnamese is shown as '=', a seen Pali unit with different Vietnamese is flagged DIFF.
Tinh Su (with --ts) lines are printed, collapsing lines already printed.
usage: python -I -X utf8 -B r3_dedupe.py <ch> [<ch> ...] [--ts] [--from ID] [--to ID]
"""
import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\review")
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
            cur.append(ln)
            m = IDRE.search(ln)
            if m:
                out.append((m.group(1), cur))
                cur = []
    return out


def norm(s):
    s = IDRE.sub("", s).strip()
    return s.lower()


def main():
    a = sys.argv[1:]
    show_ts = "--ts" in a
    fr = a[a.index("--from") + 1] if "--from" in a else None
    to = a[a.index("--to") + 1] if "--to" in a else None
    chs = [x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or a[i - 1] not in ("--from", "--to"))]
    tm = dict(segs(TS)) if show_ts else {}
    seen = {}
    tseen = set()
    on = fr is None
    for ch in chs:
        for (pid, pl), (vid, vl) in zip(segs(PI % ch), segs(VI % ch)):
            if pid == fr:
                on = True
            if not on:
                continue
            print("==== " + pid)
            for k in range(max(len(pl), len(vl))):
                p = pl[k] if k < len(pl) else ""
                v = vl[k] if k < len(vl) else ""
                pu = re.split(r"(?<=\?)\s+", IDRE.sub("", p).strip())
                vu = re.split(r"(?<=\?)\s+", IDRE.sub("", v).strip())
                if len(pu) != len(vu):
                    pu, vu = [p], [v]
                buf = []
                for x, y in zip(pu, vu):
                    kx = norm(x)
                    if kx in seen:
                        if seen[kx][0] == norm(y):
                            buf.append("=")
                            continue
                        buf.append("\n  P: %s\n  V: %s\n  DIFF(first %s): %s" % (x, y, seen[kx][1], seen[kx][2]))
                        continue
                    seen[kx] = (norm(y), pid, y)
                    buf.append("\n  P: %s\n  V: %s" % (x, y))
                print(" L%d:%s" % (k, "".join(buf)))
            if show_ts:
                for l in tm.get(pid, ["<no TS>"]):
                    kl = IDRE.sub("", l).strip()
                    if kl in tseen:
                        continue
                    tseen.add(kl)
                    print("  T: " + kl)
            if pid == to:
                return


main()
