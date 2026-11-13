"""Probe helper for 1-01-kusalattika.md: classify the non-empty lines outside the sample ranges.

usage: python -I -B -X utf8 probe_1-01.py [mode] [from] [to] [maxlen]
  mode = other (default): list lines that are neither headings nor count lines S.count_hi converts
  mode = show: print full Pāli lines from..to (non-empty numbering)
  mode = en: print Pāli and English lines from..to
  mode = hi: print the built Hindi lines from..to (from the output file)
"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S

ROOT = S.ROOT
P = [l for l in (S.PALI_DIR / "1-01-kusalattika.md").read_text(encoding="utf-8").splitlines() if l.strip()]
mode = sys.argv[1] if len(sys.argv) > 1 else "other"
a = int(sys.argv[2]) if len(sys.argv) > 2 else 1
b = int(sys.argv[3]) if len(sys.argv) > 3 else len(P)
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 100000
if mode == "en":
    E = [l for l in (ROOT / "AI_translation" / "english" / "pi-7-english-plain-zeroshot_split_chapters" /
                     "1-01-kusalattika.md").read_text(encoding="utf-8").splitlines() if l.strip()]
if mode == "hi":
    H = [l for l in (S.HI_DIR / "1-01-kusalattika.md").read_text(encoding="utf-8").splitlines() if l.strip()]
SAMPLE = set(range(1, 191)) | set(range(1235, 1263))
cnt = {"head": 0, "count": 0, "other": 0, "sample": 0}
for i in range(a, b + 1):
    line = P[i - 1]
    if mode == "show":
        print(i, line[:mx])
        continue
    if mode == "en":
        print(i, "P:", line[:mx])
        print(i, "E:", E[i - 1][:mx])
        continue
    if mode == "hi":
        print(i, "P:", line[:mx])
        print(i, "H:", H[i - 1][:mx])
        continue
    if i in SAMPLE:
        cnt["sample"] += 1
        continue
    if line.startswith("#"):
        cnt["head"] += 1
        continue
    body = S.ID_RX.sub("", line)
    try:
        S.count_hi(body)
        cnt["count"] += 1
        continue
    except ValueError:
        pass
    cnt["other"] += 1
    print(i, len(line), line[:mx])
if mode == "other":
    print(cnt)
