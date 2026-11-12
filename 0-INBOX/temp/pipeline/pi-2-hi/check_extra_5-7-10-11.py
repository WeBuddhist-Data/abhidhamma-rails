# -*- coding: utf-8 -*-
"""Extra checks for chapters 5, 7, 10, 11: Latin words outside brackets, CR, double blank lines,
dash/":-" use, identical-Pāli -> identical-Hindi across the four chapters (per line)."""
import os, re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
import pp_5_7_10_11_hi as P

CHS = ["5-indriyavibhango.md", "7-satipatthanavibhango.md", "10-bojjhangavibhango.md", "11-maggangavibhango.md"]
bad = 0
pairs = {}
for ch in CHS:
    raw = open(os.path.join(P.HI_DIR, ch), encoding="utf-8", newline="").read()
    if "\r" in raw:
        print(ch, "CR found"); bad += 1
    if "\n\n\n" in raw:
        print(ch, "double blank line"); bad += 1
    if "—" in raw or ":-" in raw:
        print(ch, "em dash or :-"); bad += 1
    for i, line in enumerate(raw.splitlines(), 1):
        body = P.ID.sub("", line)
        body = re.sub(r"\[[^\]]*\]", "", body)
        lat = re.findall(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}", body)
        if lat:
            print(f"{ch}:{i} Latin: {lat[:5]}"); bad += 1
    pl = [P.strip_id(l) for l in P.pali_lines(ch) if l.strip()]
    hl = [P.strip_id(l) for l in raw.splitlines() if l.strip()]
    for a, b in zip(pl, hl):
        pairs.setdefault(a, set()).add(b)
diff = {k: v for k, v in pairs.items() if len(v) > 1}
for k, v in diff.items():
    print("same Pāli, different Hindi:", k[:80]); bad += 1
print("extra checks:", "OK" if not bad else f"{bad} problems")
