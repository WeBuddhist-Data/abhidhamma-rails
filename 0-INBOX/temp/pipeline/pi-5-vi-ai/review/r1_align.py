import sys, re, unicodedata
# usage: r1_align.py <chapter.md> [full|qs] [start_id] [end_id]
BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
ch = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "qs"
start = sys.argv[3] if len(sys.argv) > 3 else None
end = sys.argv[4] if len(sys.argv) > 4 else None
P = open(BASE + r"\pali\pi-5_split_chapters\\" + ch, encoding="utf8").read()
V = open(BASE + r"\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\\" + ch, encoding="utf8").read()

def segs(t):
    out = []
    for s in re.split(r"\n\s*\n", t.strip()):
        lines = [l for l in s.split("\n") if l.strip()]
        m = re.search(r"\^([\w-]+)\s*$", lines[-1])
        out.append((m.group(1) if m else "?", lines))
    return out

ps, vs = segs(P), segs(V)
assert len(ps) == len(vs), (len(ps), len(vs))
PENT = re.compile(r"^(Ājānāhi|No ce pana|Hañci|Tvaṃ ce pana|Ese ce|Na hevaṃ niggahetabbe|Tena hi yaṃ)")
seen = {}
on = start is None
for (pid, pl), (vid, vl) in zip(ps, vs):
    if pid != vid:
        print("ID MISMATCH", pid, vid)
    if start and pid == start:
        on = True
    if not on:
        continue
    print("=== ^" + pid, "" if len(pl) == len(vl) else "LINECOUNT %d/%d" % (len(pl), len(vl)))
    for a, b in zip(pl, vl):
        key = a
        if key in seen:
            if seen[key][1] == b:
                print("  [dup of ^%s]" % seen[key][0])
                continue
            else:
                print("  !! SAME PALI, DIFFERENT VI (first ^%s)" % seen[key][0])
        else:
            seen[key] = (pid, b)
        if mode == "qs" and PENT.match(a):
            print("  [pentad] " + a[:70])
            continue
        print("P: " + a)
        print("V: " + b)
    if end and pid == end:
        break
