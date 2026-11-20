# -*- coding: utf-8 -*-
"""Scratch lookup for chapter 6: pi-1 openings (Pāli up to ", tasmiṃ samaye", Vietnamese up to «thì vào lúc ấy»).
usage: python -I -X utf8 probe_6_vi.py open <regex on the Pāli opening> [maxhits]
       python -I -X utf8 probe_6_vi.py vi <regex on the Vietnamese> [maxhits]"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
P = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
V = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def pairs():
    for fn in sorted(os.listdir(P)):
        if not fn.endswith(".md"):
            continue
        pl = [l for l in open(os.path.join(P, fn), encoding="utf-8").read().split("\n") if l.strip()]
        vl = [l for l in open(os.path.join(V, fn), encoding="utf-8").read().split("\n") if l.strip()]
        for a, b in zip(pl, vl):
            yield fn, a, b


def main():
    mode, rx = sys.argv[1], re.compile(sys.argv[2])
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    n = 0
    for fn, a, b in pairs():
        if mode == "open":
            if "Yasmiṃ samaye" not in a or not rx.search(a):
                continue
            pa = a[a.index("Yasmiṃ samaye"):]
            pa = pa[:pa.index(", tasmiṃ samaye")] if ", tasmiṃ samaye" in pa else pa[:300]
            vb = b[b.index("Vào lúc"):] if "Vào lúc" in b else b
            vb = vb[:vb.index("thì vào lúc ấy")] if "thì vào lúc ấy" in vb else vb[:300]
            m = ID.search(a)
            print("==", fn, m.group(1) if m else "")
            print("P:", pa)
            print("V:", vb)
        else:
            if not rx.search(b):
                continue
            m = ID.search(a)
            print("==", fn, m.group(1) if m else "")
            print("P:", a[:900])
            print("V:", b[:900])
        n += 1
        if n >= mx:
            return


if __name__ == "__main__":
    main()
