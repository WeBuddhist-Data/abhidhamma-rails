# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, chapter 17 (Khuddakavatthuvibhaṅga): Hindi plain zero-shot builder.

usage: python -I -X utf8 build_17-khuddakavatthuvibhango_hi.py
Writes AI_translation\\hindi\\pi-2-hindi-plain-zeroshot_split_chapters\\17-khuddakavatthuvibhango.md
The Hindi lines live in khuddaka17_a/b/c/d.py (shared formulas in khuddaka17_f.py); each is paired with the
start of its Pāli line, which is checked here. Block IDs are copied from the Pāli by S.assemble.
"""
import os, re, sys
HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi"
sys.path.insert(0, HERE)
import build_ch1_sample_hi as S
import khuddaka17_a, khuddaka17_b, khuddaka17_c, khuddaka17_d

NAME = "17-khuddakavatthuvibhango.md"


def main():
    pali = open(os.path.join(S.PALI_DIR, NAME), encoding="utf-8-sig").read().splitlines()
    pairs = khuddaka17_a.LINES + khuddaka17_b.LINES + khuddaka17_c.LINES + khuddaka17_d.LINES
    pn = [l for l in pali if l.strip()]
    bad = []
    for k, (p, (pre, h)) in enumerate(zip(pn, pairs)):
        if not p.startswith(pre):
            bad.append((k, pre, p[:70]))
    if bad or len(pn) != len(pairs):
        for b in bad[:10]:
            print("MISMATCH", b)
        print("pali lines", len(pn), "hindi lines", len(pairs))
        sys.exit(1)
    hindi = [h for _, h in pairs]
    for k, h in enumerate(hindi):
        assert "\n" not in h and h == h.strip(), k
    out = S.assemble(pali, hindi)
    with open(os.path.join(S.HI_DIR, NAME), "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print("written", NAME, len(hindi), "lines")


if __name__ == "__main__":
    main()
