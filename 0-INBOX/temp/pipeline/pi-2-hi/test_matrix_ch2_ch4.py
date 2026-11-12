# -*- coding: utf-8 -*-
"""Helper: run the Pañhāpucchaka parser over chapters 2 and 4 and print problems / output."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matrix_ch2_ch4_hi as M
import subjects_ch2_ch4_hi as SJ

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-2_split_chapters"
show = "-v" in sys.argv
for fn, subj, ov, lo, hi in (("2-ayatanavibhango.md", SJ.SUBJ_AYATANA, SJ.OVR_AYATANA, 64, 83),
                             ("4-saccavibhango.md", SJ.SUBJ_SACCA, SJ.OVR_SACCA, 155, 173)):
    L = open(os.path.join(ROOT, fn), encoding="utf-8").read().splitlines()
    for n in range(lo, hi + 1):
        line = L[n - 1]
        if not line.strip() or line.startswith("#"):
            continue
        line = SJ.ID.sub("", line)
        for s in M.split_sentences(line):
            try:
                h = M.paragraph(s + ".", subj, ov)
                if show:
                    print(f"{fn[:2]}{n}: {s}\n   => {h}")
            except Exception as e:
                print(f"ERR {fn[:2]}{n}: {s}\n   !! {e}")
