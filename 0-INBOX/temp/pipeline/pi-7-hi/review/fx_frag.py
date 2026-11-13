"""Print fragments: fx_frag.py <part:line> <hindi-regex> [<part:line> <regex> ...]; prints each regex match with 60 chars
context, and the Pāli line (trimmed to 300 chars around the first Pāli word given after '@' in the regex arg, if any).
Arg form: 1-04:428=REGEX  or 1-04:428=REGEX@paliword"""
import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import ar7_common as C
out = open(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review\fx_out.txt", "w", encoding="utf-8")
cache = {}
for arg in sys.argv[1:]:
    loc, rx = arg.split("=", 1)
    pw = None
    if "@" in rx:
        rx, pw = rx.split("@", 1)
    part, ln = loc.split(":")
    part = [x for x in C.PARTS if x.startswith(part)][0]
    if part not in cache:
        cache[part] = C.pairs(part)
    p, h = cache[part][int(ln) - 1]
    out.write(f"== {loc}\n")
    if pw:
        j = p.find(pw)
        out.write(f"P: …{p[max(0, j - 100):j + 200]}…\n")
    for m in re.finditer(rx, h):
        out.write(f"H: …{h[max(0, m.start() - 60):m.end() + 60]}…\n")
