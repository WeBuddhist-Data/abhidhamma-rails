"""r3: print Pali and our Vietnamese for given file + non-empty-line indices (console only).
usage: r3_show.py 7-03 36 42 ...   (index = 0-based non-empty line index, as in r3_check)"""
import sys, unicodedata

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PI = ROOT + r"\AI_translation\pali\pi-6_split_chapters\\"
VI = ROOT + r"\AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters\\"

def lines(path):
    with open(path, encoding="utf-8") as f:
        return [unicodedata.normalize("NFC", l.rstrip("\n")) for l in f if l.strip()]

fn = sys.argv[1] + "-anusayayamaka.md"
P, V = lines(PI + fn), lines(VI + fn)
for a in sys.argv[2:]:
    i = int(a)
    print("=== %s [%d]" % (fn, i))
    print("PI:", P[i])
    print("VI:", V[i])
