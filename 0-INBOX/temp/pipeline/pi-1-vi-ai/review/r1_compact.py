"""r1 helper: compact side-by-side dump (strips the fixed frame of the 'Katame dhammā kusalā?' formula).
Usage: python -I -X utf8 r1_compact.py <dump.txt> <out.txt> <first_id_number>
"""
import re, sys

PI_STRIP = [
    "Katame dhammā kusalā? Yasmiṃ samaye ",
    "tasmiṃ samaye phasso hoti…pe… avikkhepo hoti…pe… ime dhammā kusalā",
    "maggaṃ bhāveti ",
]
VI_STRIP = [
    "Những hiện tượng nào là thiện? Vào lúc ",
    "thì vào lúc ấy có sự tiếp xúc… có sự không tán loạn… những hiện tượng này là thiện",
    "một người tu tập con đường dẫn đến tái sinh vào ",
]
TS_STRIP = [
    "Chư pháp thiện trong khi có ra sao? ",
    "trong khi nào, thì xúc… vô phóng dật có trong khi ấy. Những chơn tướng này gọi là pháp thiện.",
    "trong khi nào, thì xúc... vô phóng dật có trong khi ấy. Những chơn tướng này gọi là pháp thiện.",
]

def strip(s, pats):
    for p in pats:
        s = s.replace(p, "§")
    return s

txt = open(sys.argv[1], encoding="utf-8").read()
first = int(sys.argv[3])
blocks = re.split(r"(?m)^=+ ", txt)
out = []
for b in blocks:
    if not b.strip():
        continue
    bid = b.split("\n", 1)[0].strip()
    m = re.match(r"1-(\d+)$", bid)
    if m and int(m.group(1)) < first:
        continue
    if not m and not bid.startswith("1-1-"):
        continue
    body = b.split("\n", 1)[1]
    body = re.sub(r"(?m)^PI: (.*)", lambda x: "PI: " + strip(x.group(1), PI_STRIP), body)
    body = re.sub(r"(?m)^VI: (.*)", lambda x: "VI: " + strip(x.group(1), VI_STRIP), body)
    body = re.sub(r"(?m)^(TS: |    )(.*)", lambda x: x.group(1) + strip(x.group(2), TS_STRIP + PI_STRIP + VI_STRIP), body)
    body = re.sub(r" ?\^1-[0-9-]+\s*$", "", body, flags=re.M)
    out.append("== " + bid + "\n" + body)
open(sys.argv[2], "w", encoding="utf-8").write("".join(out))
print(len(out))
