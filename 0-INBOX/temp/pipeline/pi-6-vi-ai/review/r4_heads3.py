"""List IDs of multi-case answer heads joined by commas only (our text)."""
import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs
pat = {
    "reborn/dying+pavatte": r"(đang tái sinh|đang chết đi)[^,]*, trong đời sống",
    "moment+persons": r"(khoảnh khắc [^,]*|đang diễn ra), ở (những người|chúng sinh)",
    "persons+moment": r"(chúng sinh|những người)[^,]*, (vào khoảnh khắc|khi tâm)",
}
ids = collections.defaultdict(lambda: collections.defaultdict(set))
cnt = collections.Counter()
for f, n, sid, p, v in pairs():
    for k, r in pat.items():
        for sent in re.split(r"(?<=[.])\s+", v):
            m = re.match(r"((?:Ở|Vào|Trong|Khi)\b.*?), thì ", sent)
            if m and re.search(r, m.group(1)):
                cnt[k] += 1
                ids[k][f].add(sid)
for k in pat:
    print(k, cnt[k])
    for f, s in ids[k].items():
        ss = sorted(s, key=lambda x: [int(y) for y in x.split("-")])
        print("  ", f, len(ss), ss[0], "..", ss[-1])
