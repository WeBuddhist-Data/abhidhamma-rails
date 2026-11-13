"""Explore the subject-comma pattern: SUBJ + NP running into «के लिए» (pañhāvāra lines)."""
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import ar7_common as C

DEV = "ऀ-ॣ०-ॿ"
SUBJ = sys.argv[1] if len(sys.argv) > 1 else r"अनुरूपता|गोत्र-परिवर्तन|शुद्धि|मार्ग|आर्य|मूल|इरादा|अंग|आहार|क्षमताएँ|क्षमता|प्रधानता"
NOTNEXT = r"(?!के |की |का |को |से |में |पर |रूपी |वाल|और |या |भी |ही |न |नहीं |तथा |द्वारा |रूप |-)"
RX = re.compile(r"(?<![" + DEV + r"-])(" + SUBJ + r") " + NOTNEXT + r"(?=[^,।;–…()\[\]]*? के लिए)")
cnt = collections.Counter()
ex = collections.defaultdict(list)
for part in C.PARTS:
    for i, (p, h) in enumerate(C.pairs(part)):
        if "paccayena paccayo" not in p and "paccayo" not in p:
            continue
        for m in RX.finditer(h):
            nxt = h[m.end():m.end() + 40]
            key = m.group(1)
            cnt[key] += 1
            if len(ex[key]) < int(sys.argv[2] if len(sys.argv) > 2 else 6):
                ex[key].append(f"{part[:4]}:{i+1}: …{h[max(0, m.start()-40):m.start()]}[{key}] {nxt}…")
for k, v in cnt.most_common():
    print(k, v)
    for e in ex[k]:
        print("   ", e)
