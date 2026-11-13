"""Subject-comma contexts: (prev word, SUBJ, next 2 words) counts."""
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import ar7_common as C

DEV = "ऀ-ॣ०-ॿ"
SUBJ = r"अनुरूपता|गोत्र-परिवर्तन|शुद्धि|मार्ग|आर्य|मूल|इरादा|अंग|आहार|क्षमताएँ|क्षमता|प्रधानता"
NOTNEXT = r"(?!के |की |का |को |से |में |पर |रूपी |वाल|और |या |भी |ही |न |नहीं |तथा |द्वारा |रूप |-)"
RX = re.compile(r"(?<![" + DEV + r"-])(" + SUBJ + r") " + NOTNEXT + r"(?=[^,।;–…()\[\]]*? के लिए)")
cnt = collections.Counter()
loc = {}
for part in C.PARTS:
    if part in ("preamble", "1-00-paccaya"):
        continue
    for i, (p, h) in enumerate(C.pairs(part)):
        if "paccay" not in p:
            continue
        for m in RX.finditer(h):
            pre = h[:m.start()].split()[-1:] or ["^"]
            nx = h[m.end():].split()[:2]
            k = (pre[0], m.group(1), " ".join(nx))
            cnt[k] += 1
            loc.setdefault(k, f"{part[:4]}:{i+1}")
for k, v in sorted(cnt.items(), key=lambda kv: (kv[0][1], -kv[1])):
    print(v, "|", *k, "|", loc[k])
