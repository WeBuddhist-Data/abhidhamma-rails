"""Scratch probe for chapters 10-12: run the ch. 7-9 Pañhāpucchaka machinery on single chunks / lines.
Usage: python -I -X utf8 probe_10_12.py <ch file> <line substring>
"""
import sys, os, re, traceback
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru")
import build_ch1_sample_ru as S
import build_7_9_ru as Z

fn, sub = sys.argv[1], sys.argv[2]
pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().split("\n")
for l in pali:
    l = S.ID.sub("", l).rstrip()
    if sub in l:
        # chunk-by-chunk, so that every failing chunk shows
        t = l
        for a, b in Z.FIXES + Z.QFIX:
            t = t.replace(a, b)
        for sent in re.split(r"(?<=\.) (?=[A-ZĀ])", t):
            body = sent[:-1].replace("…pe…", Z.PE)
            parts = re.split(r"(, |; |\x01 ?)", body)
            st = {"num": "pl", "g": None}
            for i, x in enumerate(parts):
                if i % 2:
                    continue
                try:
                    r = Z.q_chunk(x, st)
                    print("OK  ", x, "=>", r)
                except Exception as e:
                    print("FAIL", x, "=>", repr(e)[:150])
