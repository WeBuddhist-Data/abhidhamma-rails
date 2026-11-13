"""List termbase entries whose Hindi contains «वर्गीकरण» / «वर्ग» (name candidates for U1)."""
import re, sys
TB = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md"
pat = sys.argv[1] if len(sys.argv) > 1 else r"वर्गीकरण|वर्ग"
for i, line in enumerate(open(TB, encoding="utf-8").read().splitlines(), 1):
    if ": {" not in line:
        continue
    w, body = line.split(": {", 1)
    senses = body[:-1].split("; ")
    hs = []
    for s in senses:
        if ": " in s:
            d, h = s.rsplit(": ", 1)
            if re.search(pat, h):
                hs.append(h)
    if hs:
        print(f"{i}\t{w}\t" + " | ".join(hs))
