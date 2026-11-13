"""Probe helper for 3-01, 3-02, 3-10: list the distinct item phrases in the frames."""
import collections
import pathlib
import re

D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
FILES = ["3-01-hetugocchaka.md", "3-02-culantaraduka.md", "3-10-upadanagocchaka.md"]
DEP = r"(paṭicca|paccayā|nissāya|saṃsaṭṭho|saṃsaṭṭhā|sampayutto|sampayuttā|sahajāto|sahajātā)"
rx_dep = re.compile(r"([A-ZĀĪŪṬḌa-zāīūṭḍṇṅñṃḷ ]+?) dhammaṃ " + DEP + r" ([a-zāīūṭḍṇṅñṃḷ ]+?) (dhammo|dhammā)\b")
rx_pan = re.compile(r"([A-ZĀĪŪa-zāīūṭḍṇṅñṃḷ ]+?) (dhammo|dhammā) ([a-zāīūṭḍṇṅñṃḷ ]+?) dhammassa")
objs, ress, srcs, dsts = (collections.Counter() for _ in range(4))
for f in FILES:
    for line in (D / f).read_text(encoding="utf-8").splitlines():
        for m in rx_dep.finditer(line):
            objs[m.group(1).strip()] += 1
            ress[m.group(3)] += 1
        for m in rx_pan.finditer(line):
            srcs[m.group(1).strip()] += 1
            dsts[m.group(3)] += 1
for name, c in (("OBJ", objs), ("RES", ress), ("SRC", srcs), ("DST", dsts)):
    print("==", name)
    for k, v in sorted(c.items()):
        print(f"  {k!r}: {v}")
