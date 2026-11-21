"""r4: kathā heading vs closing-line name check (console only)."""
import re
import sys

VDIR = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters"

for ch in sys.argv[1:]:
    with open(VDIR + "\\" + ch, encoding="utf-8") as f:
        lines = [l for l in f.read().split("\n") if l.strip()]
    pending = None
    for l in lines:
        m = re.match(r"#+ \([\d-]+\) [\d-]+\. (.*?) \^", l)
        if m:
            pending = m.group(1)
            continue
        m2 = re.match(r"Phần bàn về (.*) đã hoàn tất\.", l)
        if m2:
            name = m2.group(1)
            head = pending or ""
            h = re.sub(r"^(Cả ba phần bàn|Bàn) về ", "", head)
            if h != name:
                print(ch, "HEAD:", head, "| CLOSE:", name)
            pending = None
