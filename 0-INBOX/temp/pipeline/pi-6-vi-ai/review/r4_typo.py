"""Typography / structure checks on our Vietnamese (our text only)."""
import os, re, sys, unicodedata, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import VDIR, PDIR, FILES
for f in FILES:
    raw = open(os.path.join(VDIR, f), "rb").read()
    t = raw.decode("utf-8")
    praw = open(os.path.join(PDIR, f), "rb").read()
    issues = []
    if b"\r" in raw:
        issues.append("CR")
    if unicodedata.normalize("NFC", t) != t:
        issues.append("notNFC")
    if "\n\n\n" in t:
        issues.append("doubleblank")
    if "—" in t:
        issues.append("emdash")
    if "…." in t:
        issues.append("ellipsis+dot")
    if re.search(r" [.,;:?!]", t):
        issues.append("space-before-punct x%d" % len(re.findall(r" [.,;:?!]", t)))
    if re.search(r"\?\s*\?", t):
        issues.append("??")
    # Latin (Pali-looking) words outside brackets
    tt = re.sub(r"\[[^\]]*\]", "", t)
    tt = re.sub(r"\^[0-9a-z-]+", "", tt)
    lat = collections.Counter(w for w in re.findall(r"\b[\wāīūṃṅñṭḍṇḷ]+\b", tt) if re.search(r"[āīūṃṅñṭḍṇḷ]", w))
    if lat:
        issues.append("pali-words:" + ",".join(f"{w}({k})" for w, k in lat.most_common(8)))
    # question lines without question word
    qn = 0
    for line in t.split("\n"):
        for q in re.findall(r"[^.?!]*\?", line):
            if not re.search(r"\b(không|nào|gì|bao nhiêu|phải không|chăng)\b", q):
                qn += 1
    if qn:
        issues.append(f"q-without-qword x{qn}")
    print(f, "CRLF-in-pali" if b"\r" in praw else "", issues)
