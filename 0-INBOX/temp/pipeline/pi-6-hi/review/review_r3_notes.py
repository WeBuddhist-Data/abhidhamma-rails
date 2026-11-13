import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r3_pairs import load
from review_r3_struct import FILES

seen = set()
for fn in FILES:
    p, h = load(fn)
    for i, (a, b) in enumerate(zip(p, h), 1):
        if a.startswith("#"):
            k = re.sub(r"\s*\^[0-9-]+$", "", a)
            if k in seen: continue
            seen.add(k)
            print(fn[:4], i, "|", k, "|", re.sub(r"\s*\^[0-9-]+$", "", b))
            continue
        m = re.search(r"\((?!Ka\)|Kha\))[^)]*[a-z][^)]*\)", a)
        if m and not re.search(r"(uppajj|nirujjh)", m.group(0)):
            print(fn[:4], i, "| P:", a)
            print(fn[:4], i, "| H:", b)
        elif not re.search(r"(uppajj|nirujjh|saccanti|sacca\w*\?|saṅkhār\w*\?|\?)", a) and len(a) < 200 and not re.search(r"saccañceva|ṭhapetvā|na ceva|ceva", a):
            print(fn[:4], i, "| P:", a)
            print(fn[:4], i, "| H:", b)
