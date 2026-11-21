"""r4: list Vietnamese questions lacking a question word, and unbalanced quotes (console only)."""
import re
import sys

VDIR = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters"
QW = re.compile(r"(không|sao|nào|gì|đâu|hay|bao nhiêu|\bai\b|chăng)\s*[”’]?\s*(\[[^\]]*\])?\s*[”’]?\s*\?$", re.I)

for ch in sys.argv[1:]:
    with open(VDIR + "\\" + ch, encoding="utf-8") as f:
        lines = [l for l in f.read().split("\n") if l.strip()]
    for i, l in enumerate(lines):
        body = re.sub(r"\^\S+\s*$", "", l)
        for m in re.finditer(r"[^?.!…]*\?", body):
            s = m.group(0).strip()
            if not QW.search(s):
                print(ch, "L%d" % (i + 1), "Q-no-word:", s[-80:])
        if body.count("“") != body.count("”"):
            print(ch, "L%d" % (i + 1), "quotes “%d ”%d" % (body.count("“"), body.count("”")), body[:60])
