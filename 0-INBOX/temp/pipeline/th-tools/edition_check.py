"""Confirm the edition of a Thai draft: share of sampled paragraphs found word for word (spaces
ignored) in the Royal, MCU and Mahamakut editions on etipitaka.com, plus [n] continuity.
Usage: edition_check.py <draft.md> <royal_vol> <mcu_vol> <workdir>"""
import os
import random
import re
import sys
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_common import parse_draft  # noqa: E402

draft, royal_vol, mcu_vol, work = sys.argv[1:5]
D = parse_draft(draft)
TD = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")
nums = [int(m.translate(TD)) for it in D for m in re.findall(r"^\[([๐-๙]+)\]", it["text"])]
top = max(nums)
missing = sorted(set(range(1, top + 1)) - set(nums))
dups = sorted({n for n in nums if nums.count(n) > 1})
print(f"[n] numbers: 1..{top}, distinct {len(set(nums))}, missing {len(missing)} {missing[:30]}, duplicated {len(dups)} {dups[:20]}")


def norm(s):
    return re.sub(r"[\s​]+", "", re.sub(r"\[[๐-๙]+\]", "", s))


paras = [norm(it["text"]) for it in D if it["kind"] == "p"]
paras = [p for p in paras if len(p) >= 40]
random.seed(1)
sample = random.sample(paras, min(400, len(paras)))
for name, url in (("royal", f"https://etipitaka.com/read/thai/{royal_vol}/1/"),
                  ("mcu", f"https://etipitaka.com/read/thaimc/{mcu_vol}/1/")):
    path = os.path.join(work, f"etipitaka-{name}-{royal_vol if name == 'royal' else mcu_vol}.html")
    if not os.path.exists(path):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        open(path, "wb").write(urllib.request.urlopen(req, timeout=120).read())
    raw = open(path, encoding="utf-8").read()
    t = norm(re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), raw).replace("\\n", "").replace("\\t", ""))
    exact = sum(1 for p in sample if p in t)
    print(f"{name} vol {royal_vol if name == 'royal' else mcu_vol}: {exact}/{len(sample)} sampled paragraphs found word for word")
