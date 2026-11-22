"""Answer-head joining styles in our Vietnamese (our text only)."""
import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs
show = int(sys.argv[1]) if len(sys.argv) > 1 else 3
c = collections.Counter()
ex = collections.defaultdict(list)
for f, n, sid, p, v in pairs():
    if "?" in v and not re.search(r"\?\s*\S", v):
        continue
    for sent in re.split(r"(?<=[.])\s+", v):
        m = re.match(r"((?:Ở|Vào|Trong|Khi)\b.*?), thì ", sent)
        if not m:
            continue
        head = m.group(1)
        segs = re.split(r", (?=ở |vào |trong đời sống|khi |Ở |Vào )", head)
        if len(segs) < 2:
            c["single"] += 1
            continue
        if re.search(r", và (ở |vào |trong|khi )", head):
            kind = "comma+và"
        else:
            kind = "comma-only"
        key = f"{kind}:{len(segs)}"
        c[key] += 1
        ex[key].append(f"{f}:{n} {sid} :: {head}")
for k, x in sorted(c.items()):
    print(x, k)
for k in ex:
    for e in ex[k][:show]:
        print(k, e)
