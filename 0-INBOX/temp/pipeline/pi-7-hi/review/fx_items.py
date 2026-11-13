"""For each dyad/triad heading in its home file, print the Hindi heading and the first item wording found in the
section body («<item> परिघटना पर निर्भर होकर»)."""
import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import ar7_common as C
out = open(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review\fx_out.txt", "w", encoding="utf-8")
HOME = ("1-0", "2-", "3-", "4-01")
for part in C.PARTS:
    if not part.startswith(HOME) or part.startswith("1-00"):
        continue
    pr = C.pairs(part)
    for i, (p, h) in enumerate(pr):
        m = re.match(r"^#+ (\w+(?:duk|ttik)aṃ) \^", p)
        if not m:
            continue
        item = ""
        for p2, h2 in pr[i + 1:i + 40]:
            mm = re.match(r"^(.*?) परिघटना पर निर्भर होकर", h2)
            if mm and not h2.startswith("#"):
                item = mm.group(1)
                break
        hh = re.sub(r"^#+ | \^.*$", "", h)
        out.write(f"{part[:4]}\t{m.group(1)}\t{hh}\t{item}\n")
