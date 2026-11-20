"""Scratch: classify every awakening-factor name «chi phần giác ngộ là X» by context (quoted / unquoted, role).

usage: python -I -X utf8 probe_bojjh_vi.py [--bak] [--show]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, pairs, short

if "--bak" in sys.argv:
    vi_common.CUR["vdir"] = vi_common.BAK
NAMES = ["sự tỉnh thức", "sự tìm hiểu các hiện tượng", "sự tinh tấn", "sự hân hoan", "sự an tịnh", "định tâm",
         "sự bình thản"]
RX = re.compile(r"(“?)([Cc]hi phần giác ngộ là (?:%s))(”?)" % "|".join(map(re.escape, NAMES)))
cnt = collections.Counter()
for part in PARTS:
    for k, (p, v) in enumerate(pairs(part)):
        for m in RX.finditer(v):
            before = v[max(0, m.start() - 12):m.start()]
            after = v[m.end():m.end() + 10]
            q = "Q" if m.group(1) else "-"
            if after.startswith(" là gì") :
                role = "topic"
            elif after.startswith(" thì") or re.match(r"^ (?:đôi khi|không|có|là|vừa|gắn|thuộc|lấy|dẫn|chỉ)", after):
                role = "subject?"
            elif re.search(r"(?:^|[.?] |Ở đây, )$", before):
                role = "subject?"
            else:
                role = "other"
            cnt[(short(part), role, q)] += 1
            if "--show" in sys.argv and role != "other":
                print(f"{short(part)} l{k + 1} {role} {q} …{before}[{m.group(0)}]{after}…")
for k in sorted(cnt, key=lambda x: (int(x[0]) if x[0].isdigit() else 0, x[1], x[2])):
    print(k, cnt[k])
