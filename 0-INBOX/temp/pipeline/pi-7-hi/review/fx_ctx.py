"""Context counts: for a Hindi regex (argv[1]) print counts of the matched text with N chars of context
(argv[2], default 25) and the Pāli fragment matched by argv[3] (optional). Output -> fx_out.txt"""
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import ar7_common as C
out = open(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review\fx_out.txt", "w", encoding="utf-8")
hr = re.compile(sys.argv[1])
n = int(sys.argv[2]) if len(sys.argv) > 2 else 25
pr = re.compile(sys.argv[3]) if len(sys.argv) > 3 else None
cnt = collections.Counter()
loc = {}
for part in C.PARTS:
    for i, (p, h) in enumerate(C.pairs(part)):
        for m in hr.finditer(h):
            k = h[max(0, m.start() - n):m.start()] + "[" + m.group(0) + "]" + h[m.end():m.end() + n]
            if pr:
                k += "  ||  " + " / ".join(pr.findall(p))[:150]
            cnt[k] += 1
            loc.setdefault(k, []).append(f"{part[:4]}:{i + 1}")
for k, v in cnt.most_common():
    out.write(f"{v}\t{k}\t{' '.join(loc[k][:6])}\n")
out.write(f"TOTAL {sum(cnt.values())} in {len(cnt)} contexts\n")
