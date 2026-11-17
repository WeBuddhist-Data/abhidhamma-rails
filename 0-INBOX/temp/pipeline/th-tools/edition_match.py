"""Whole-volume check: what share of the paragraphs in our Thai draft occur verbatim (spaces
ignored) in each online edition's text? Prints percentages only."""
import os
import random
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
from parse_common import parse_draft  # noqa: E402


def norm(s):
    s = re.sub(r"\[[๐-๙]+\]", "", s)
    return re.sub(r"[\s​]+", "", s)


paras = [norm(it["text"]) for it in parse_draft(os.path.join(here, "th-1-draft.md")) if it["kind"] == "p"]
paras = [p for p in paras if len(p) >= 40]
random.seed(1)
sample = random.sample(paras, min(400, len(paras)))
for name in ("etipitaka-royal-34-1", "etipitaka-mcu-34-1", "etipitaka-mm-75-1"):
    raw = open(os.path.join(here, "edition_probe", name + ".html"), encoding="utf-8").read()
    t = norm(re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), raw).replace("\\n", "").replace("\\t", ""))
    exact = sum(1 for p in sample if p in t)
    head = sum(1 for p in sample if p[:30] in t)
    # for paragraphs not found whole: how far does the match run before the first difference?
    fr = []
    for p in sample:
        if p in t:
            continue
        lo, hi = 30, len(p)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if p[:mid] in t:
                lo = mid
            else:
                hi = mid - 1
        fr.append(lo / len(p))
    fr.sort()
    med = fr[len(fr) // 2] if fr else 1.0
    print(f"   {name}: non-exact paragraphs match for a median {100*med:.0f}% of their length before the first difference")
    print(f"{name}: whole paragraph found {exact}/{len(sample)} ({100*exact/len(sample):.0f}%), first 30 chars found {head}/{len(sample)} ({100*head/len(sample):.0f}%)")
