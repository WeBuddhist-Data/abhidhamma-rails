import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r5_lib import *

ps = pairs()
print("lines", len(ps))
bad = 0
for fn, ln, sid, P, V in ps:
    mp = IDRE.search(P); mv = IDRE.search(V)
    if (mp and mp.group(1)) != (mv and mv.group(1)):
        print("ID", fn, ln, mp and mp.group(1), mv and mv.group(1))
    ch = []
    if P.count("?") != V.count("?"): ch.append("?%d/%d" % (P.count("?"), V.count("?")))
    a1 = len(re.findall(r"Āmantā", P)); a2 = len(re.findall(r"Đúng vậy", V))
    if a1 != a2: ch.append("amanta%d/%d" % (a1, a2))
    n1 = len(re.findall(r"(?:^|[?] )No\.", P)); n2 = len(re.findall(r"(?:^|[?] )Không\.", V))
    if n1 != n2: ch.append("No%d/%d" % (n1, n2))
    t1 = len(re.findall(r"\bNatthi\b", P)); t2 = len(re.findall(r"(?:^|[?] )Không có\.", V))
    if t1 != t2: ch.append("natthi%d/%d" % (t1, t2))
    e1 = P.count("pe…") + P.count("…pe"); e1 = len(re.findall(r"…pe…|\.\.\.pe\.\.\.", P)); e2 = V.count("…")
    if e1 != e2: ch.append("pe%d/%d" % (e1, e2))
    d1 = P.count("–") + P.count("—"); d2 = V.count("–") + V.count("—")
    if d1 != d2: ch.append("dash%d/%d" % (d1, d2))
    if "…." in V: ch.append("ellipsis-dot")
    b1 = P.count("["); b2 = V.count("[")
    if b1 != b2: ch.append("br%d/%d" % (b1, b2))
    sp = sentences(P); sv = sentences(V)
    if len(sp) != len(sv): ch.append("sent%d/%d" % (len(sp), len(sv)))
    if V != unicodedata.normalize("NFC", V): ch.append("NFC")
    if "\r" in V: ch.append("CR")
    if re.search(r" [.,;:?]", V): ch.append("space-punct")
    if not P.startswith("#"):
        if not re.search(r"[.?]\s*(\^\S+)?\s*$|\)\s*(\^\S+)?\s*$", V): ch.append("noend")
    if ch:
        bad += 1
        print(fn, ln, sid, " ".join(ch))
print("flagged", bad)
