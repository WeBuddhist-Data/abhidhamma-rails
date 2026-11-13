"""Word list of the untranslated units (helper for 3-01, 3-02, 3-10)."""
import collections
import pathlib
import re

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
c = collections.Counter()
for line in (HERE / "unknown_3-01_3-02_3-10.txt").read_text(encoding="utf-8").splitlines():
    n, w, k = line.split("\t", 2)
    if k.startswith("#") or k.startswith("("):
        continue
    for t in re.findall(r"[^\s\"]+", k):
        c[t] += int(n)
print(len(c))
print(" ".join(f"{k}:{v}" for k, v in sorted(c.items(), key=lambda kv: -kv[1])))
