"""Show aligned Pāli/Hindi non-empty lines.
usage: fx_show.py <part> <from> <to>            (1-based non-empty line numbers)
       fx_show.py --grep <hindi-regex> [pali-regex] [max]   (all files)
       fx_show.py --pgrep <pali-regex> [max]"""
import os, re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import ar7_common as C

a = sys.argv[1:]
sys.stdout = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fx_out.txt"), "w", encoding="utf-8")
if a[0] == "--id":
    want = set(a[1:])
    for part in C.PARTS:
        pr = C.pairs(part)
        start = 0
        for i, (p, h) in enumerate(pr):
            m = re.search(r"\^([\w-]+)\s*$", p)
            if m:
                if m.group(1) in want:
                    for j in range(start, i + 1):
                        print(f"== {part[:4]}:{j + 1}\nP: {pr[j][0]}\nH: {pr[j][1]}")
                start = i + 1
    sys.exit()
if a[0] == "--grep" or a[0] == "--pgrep":
    if a[0] == "--grep":
        hr = re.compile(a[1]); pr = re.compile(a[2]) if len(a) > 2 and a[2] else None
        mx = int(a[3]) if len(a) > 3 else 40
    else:
        hr = None; pr = re.compile(a[1]); mx = int(a[2]) if len(a) > 2 else 40
    n = 0
    for part in C.PARTS:
        for i, (p, h) in enumerate(C.pairs(part)):
            if (hr is None or hr.search(h)) and (pr is None or pr.search(p)):
                n += 1
                if n <= mx:
                    print(f"== {part[:4]}:{i + 1}\nP: {p}\nH: {h}")
    print("TOTAL", n)
else:
    part = [x for x in C.PARTS if x.startswith(a[0])][0]
    pr = C.pairs(part)
    for i in range(int(a[1]) - 1, min(int(a[2]), len(pr))):
        print(f"== {part[:4]}:{i + 1}\nP: {pr[i][0]}\nH: {pr[i][1]}")
