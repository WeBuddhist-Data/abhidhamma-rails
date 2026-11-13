import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review")
from review_r6_common import *

LAT = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]")
nseg = 0
for f in FILES:
    rp = raw(os.path.join(PDIR, f)); rh = raw(os.path.join(HDIR, f))
    if "\n\n\n" in rh.replace("\r", ""):
        print(f, "DOUBLE BLANK in Hindi")
    # blank-line structure identical?
    pb = [bool(l.strip()) for l in rp.split("\n")]
    hb = [bool(l.strip()) for l in rh.split("\n")]
    if pb != hb:
        print(f, "blank-line layout differs", len(pb), len(hb))
    for r in pairs(f):
        p, h = r["p"], r["h"]
        tag = f"{f}|{r['id']}|k{r['k']}"
        mp = IDRE.search(p); mh = IDRE.search(h)
        if (mp.group(1) if mp else None) != (mh.group(1) if mh else None):
            print(tag, "ID MISMATCH", mp and mp.group(1), mh and mh.group(1))
        if mp and not p.startswith("#"):
            nseg += 1
        # heading levels
        hp = re.match(r"#*", p).group(0); hh = re.match(r"#*", h).group(0)
        if hp != hh:
            print(tag, "HEADING LEVEL", hp, hh)
        if p.lstrip("#").strip().startswith("*") != h.lstrip("#").strip().startswith("*"):
            print(tag, "ITALIC mismatch")
        # count markers
        cp = re.findall(r"\((\d+)\)", p); ch = re.findall(r"\((\d+)\)", h)
        if cp != ch:
            print(tag, "COUNTMARK", cp, ch)
        # dashes
        dp = len(re.findall(r"[–—]", p)); dh = len(re.findall(r"[–—]", h))
        if dp != dh or "—" in h:
            print(tag, "DASH", dp, dh, "| emdash in H" if "—" in h else "")
        # hyphen-minus spaced
        if " - " in h:
            print(tag, "spaced hyphen in H")
        # ellipsis count vs pe
        pe = p.count("…pe…") + p.count("...pe...")
        # end punctuation
        body = IDRE.sub("", h).rstrip()
        if not h.startswith("#"):
            body2 = re.sub(r"\s*\(\d+\)$", "", body).rstrip()
            if not re.search(r"[।?…:]$|[।?]\)$|।”$|\?”$", body2):
                print(tag, "END PUNCT:", body2[-40:])
            pbody = re.sub(r"\s*\(\d+\)$", "", IDRE.sub("", p).rstrip()).rstrip()
            if pbody.endswith("?") != body2.endswith("?") and not ("siyā" in p.lower() or "Siyā" in p):
                print(tag, "Q mismatch", pbody[-30:], "||", body2[-30:])
        # Latin letters outside brackets / ids
        hh2 = IDRE.sub("", h)
        hh2 = re.sub(r"\[पाठभेद[^\]]*\]|\[वर्तनी-भेद[^\]]*\]", "", hh2)
        if LAT.search(hh2):
            print(tag, "LATIN:", re.findall(r"\S*" + LAT.pattern + r"\S*", hh2)[:6])
        # quotes
        if re.search(r"[\"'«»]", hh2):
            print(tag, "QUOTE char", re.findall(r"[\"'«»]", hh2))
        if "“" in p or "‘" in p or "“" in h:
            if p.count("“") + p.count("‘") != h.count("“"):
                print(tag, "QUOTES count", p.count("“"), p.count("‘"), h.count("“"))
        # braces
        if p.count("{") != len(re.findall(r"\[(पाठभेद|वर्तनी-भेद)", h)):
            print(tag, "VARIANT count", p.count("{"), len(re.findall(r"\[(पाठभेद|वर्तनी-भेद)", h)))
        # parentheses notes count
        pp = len(re.findall(r"\((?!\d+\))", p)); hp_ = len(re.findall(r"\((?!\d+\))", h))
        if pp != hp_:
            print(tag, "PAREN count", pp, hp_)
print("segments(non-heading id lines):", nseg)
