import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from review_r1_common import *

out = []
def P(*a):
    out.append(" ".join(str(x) for x in a))

for f in FILES:
    praw, pl, pn = load(PDIR, f)
    hraw, hl, hn = load(HDIR, f)
    P("=====", f, "lines", len(pl), len(hl), "nonempty", len(pn), len(hn))
    if "\n\n\n" in hraw:
        P("DOUBLE BLANK in Hindi")
    for k, ((pln, p), (hln, h)) in enumerate(zip(pn, hn)):
        n = k + 1
        if pln != hln:
            P(n, "physical line mismatch", pln, hln)
        pid = re.search(r"\^([\w-]+)\s*$", p)
        hid = re.search(r"\^([\w-]+)\s*$", h)
        if (pid and pid.group(1)) != (hid and hid.group(1)):
            P(n, "ID mismatch", pid and pid.group(1), hid and hid.group(1))
        ph = re.match(r"^(#+)", p); hh = re.match(r"^(#+)", h)
        if (ph and ph.group(1)) != (hh and hh.group(1)):
            P(n, "heading level mismatch")
        if p.count("*") != h.count("*"):
            P(n, "asterisk mismatch")
        # dashes
        pd = len(re.findall(r"[–—]", p)); hd = len(re.findall(r"[–—]", h))
        if pd != hd:
            P(n, "DASH count", pd, hd, "|", p[:80], "|", h[:80])
        if "—" in h:
            P(n, "em dash in Hindi")
        # markers
        pm = re.findall(r"\((\d+)\)", p); hm = re.findall(r"\((\d+)\)", h)
        if pm != hm:
            P(n, "MARKER", pm, hm)
        # parentheses balance
        if p.count("(") != h.count("("):
            P(n, "paren count", p.count("("), h.count("("))
        if p.count("{") != h.count("[") - len(re.findall(r"\[\[", h)):
            P(n, "variant count", p.count("{"), h.count("["))
        # Latin letters outside brackets in Hindi
        body = re.sub(r"\^[\w-]+\s*$", "", h)
        body2 = re.sub(r"\[[^\]]*\]", "", body)
        lat = re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]+", body2)
        if lat:
            P(n, "LATIN", lat[:6])
        # straight quotes
        if '"' in body or "'" in body or "‘" in body:
            P(n, "QUOTE chars", h[:100])
        if "  " in body.rstrip():
            P(n, "double space")
        if not h.startswith("#"):
            b = body.rstrip()
            # end punctuation
            if b and b[-1] not in "।?)":
                if not b.endswith(","):
                    P(n, "END", repr(b[-12:]), "| P:", repr(re.sub(r"\^[\w-]+\s*$", "", p).rstrip()[-12:]))
            if b.endswith("."):
                P(n, "ends with period")
        if "." in body2.replace("…", "") and not h.startswith("#"):
            P(n, "PERIOD in Hindi", h[:120])
        # ellipsis counts
        pe = p.count("…"); he = h.count("…")
        pe_pe = p.count("…pe…")
        if pe - pe_pe != he:
            P(n, "ELLIPSIS", pe, pe_pe, he)
        # question
        pq = p.count("?"); hq = h.count("?")
        if pq > hq:
            P(n, "QMARK lost", pq, hq)
        if hq > pq and "Siyā" not in p and "siyā" not in p:
            P(n, "QMARK added", pq, hq, p[:80])

with open(os.path.join(OUT, "review_r1_struct_out.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(out))
print(len(out))
