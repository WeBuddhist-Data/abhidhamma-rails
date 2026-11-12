# -*- coding: utf-8 -*-
"""Dry run of the Pañhāpucchaka engine on chapters 5, 7, 10, 11 (prints Pāli/Hindi per sentence)."""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
import pp_5_7_10_11_hi as P

RANGES = {"5-indriyavibhango.md": (42, 82, P.SUBJECTS["dasindriyā"]),
          "7-satipatthanavibhango.md": (102, 108, None),
          "10-bojjhangavibhango.md": (70, 75, None),
          "11-maggangavibhango.md": (73, 81, None)}
ALL5 = P.Subj("सभी क्षमताएँ", "सभी क्षमताओं", "f", True)
YE = P.Subj("ये", None, "m", True, pron=True)
only = sys.argv[1] if len(sys.argv) > 1 else None
print("matrix-check misses:", P.check_pi1())
for ch, (a, b, _) in RANGES.items():
    if only and not ch.startswith(only):
        continue
    lines = P.pali_lines(ch)
    for i in range(a - 1, b):
        l = lines[i]
        if not l.strip() or l.startswith("#"):
            continue
        print(f"=== {ch}:{i+1}")
        P.render_line(P.strip_id(l), ALL5 if ch.startswith("5") else YE, debug=True)
