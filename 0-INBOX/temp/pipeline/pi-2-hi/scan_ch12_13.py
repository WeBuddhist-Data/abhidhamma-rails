# -*- coding: utf-8 -*-
"""Final scan of the ch12/13 Hindi outputs: Latin outside brackets, CR, double blank lines, dash/line counts."""
import os, re

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
for ch in ("12-jhanavibhango.md", "13-appamannavibhango.md"):
    h = open(os.path.join(ROOT, r"AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters", ch), encoding="utf-8", newline="").read()
    p = open(os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters", ch), encoding="utf-8").read()
    f = lambda t: [l for l in t.splitlines() if l.strip()]
    a, b = f(p), f(h)
    c = lambda t: t.count("—") + t.count("–")
    bad = [i for i, (x, y) in enumerate(zip(a, b)) if c(x) != c(y)]
    latin = [i + 1 for i, l in enumerate(b) if re.search(r"[A-Za-zĀ-ɏḀ-ỿ]", re.sub(r"\[[^\]]*\]|\^[0-9A-Za-z-]+\s*$", "", l))]
    print(ch, "lines", len(a), len(b), "dash mismatches", len(bad), "latin lines", latin[:5],
          "CR", "\r" in h, "double blank", "\n\n\n" in h, "seed", "seed" in h.lower())
