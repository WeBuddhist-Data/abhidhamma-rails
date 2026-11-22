"""r3: map Tinh Su segments (by block ID) for 6-7-36..6-7-263 and print, per ID, a short
fingerprint (line count, '?' count, negation counts, first words) beside ours. Console only;
nothing is written to disk.
usage: r3_ts.py            -> table of all IDs
       r3_ts.py show ID    -> print TS segment + our segment for one ID"""
import re, sys, unicodedata
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
import r3_check as C

TS = r"D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Translations\Vietnamese\vi-6-tinh_su.md"
IDR = re.compile(r"\^(6-7-[0-9-]+)\s*$")

def segs_from(lines):
    out, cur = {}, []
    order = []
    for l in lines:
        if not l.strip():
            continue
        cur.append(l)
        m = IDR.search(l)
        if m:
            out[m.group(1)] = cur
            order.append(m.group(1))
            cur = []
    return out, order

def ts_lines():
    with open(TS, encoding="utf-8") as f:
        return [unicodedata.normalize("NFC", l.rstrip("\n")) for l in f]

def ours():
    allv, allp = [], []
    for fn in C.FILES:
        allv += C.lines(C.VI + fn)
        allp += C.lines(C.PI + fn)
    return segs_from(allv), segs_from(allp)

def fp_vi(seg):
    t = " ".join(seg)
    return "q%d" % t.count("?")

def main():
    T, torder = segs_from(ts_lines())
    (V, vorder), (P, _) = ours()
    if len(sys.argv) > 2 and sys.argv[1] == "show":
        for i in sys.argv[2:]:
            print("=== TS", i)
            for l in T.get(i, ["<missing>"]):
                print("  ", l)
            print("=== OURS", i)
            for l in V.get(i, ["<missing>"]):
                print("  ", l)
        return
    for i in vorder:
        t = T.get(i)
        v = V[i]
        if t is None:
            print(i, "| TS MISSING | ours", fp_vi(v))
            continue
        tt = " ".join(t)
        print(i, "| TS lines %d q%d | ours lines %d %s | TS head: %s" % (
            len(t), tt.count("?"), len(v), fp_vi(v), re.sub(r"\s+", " ", [x for x in t if not x.startswith("![[")][0])[:70]))

main()
