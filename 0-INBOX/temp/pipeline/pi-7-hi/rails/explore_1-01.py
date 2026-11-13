"""Exploration helper for 1-01: which non-empty Pāli lines does a translator fail on?
usage: python -I -B -X utf8 explore_1-01.py [module] [max]   (module: S = sample builder, B = build_rails_1-01)"""
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
mod = sys.argv[1] if len(sys.argv) > 1 else "S"
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 60
if mod == "S":
    import build_rails_sample as T
else:
    import importlib
    T = importlib.import_module("build_rails_1-01".replace("-", "_")) if False else __import__("build_rails_1-01")

SRC = os.path.join(HERE, "..", "..", "..", "..", "..", "AI_translation", "pali", "pi-7_split_chapters", "1-01-kusalattika.md")
lines = [l for l in open(SRC, encoding="utf-8").read().split("\n") if l.strip()]
fails = collections.OrderedDict()
for i, ln in enumerate(lines, 1):
    m = re.search(r" \^([0-9A-Za-z-]+)\s*$", ln)
    body = ln[: m.start()] if m else ln.rstrip()
    try:
        T.translate_line(body)
    except Exception as e:  # noqa
        key = f"{type(e).__name__}: {e}"[:300]
        fails.setdefault(key, []).append(i)
print("failing kinds:", len(fails), "lines:", sum(len(v) for v in fails.values()))
for k, v in list(fails.items())[:mx]:
    print(len(v), v[:6], k)
