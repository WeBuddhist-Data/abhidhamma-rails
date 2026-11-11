"""Coordinator's read-only lookups before the rails alignment edits."""
import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi")
import hz_common as H

H.CUR["hdir"] = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters"
PATS = [("Teva/Tāneva", r"^.*\? (Tāneva|Teva|Teyeva|Tāni|Te) ?\w* .*ceva"),
        ("kusalākusala vipākā", r"[Kk]usalākusalānaṃ dhammānaṃ vipāk"),
        ("Ekakaṃ", r"^#+ Ekaka"),
        ("Tasmiṃ kho 2-03", r"Tasmiṃ kho pana samaye"),
        ("heṭṭhim", r"heṭṭhimāni ca")]
for name, pat in PATS:
    rx = re.compile(pat)
    print("=====", name)
    n = 0
    for part in H.PARTS:
        if name.startswith("Tasmiṃ") and not part.startswith("2-03"):
            continue
        for p, h in H.pairs(part):
            if rx.search(p):
                n += 1
                if n <= 26:
                    if name == "kusalākusala vipākā":
                        m = re.search(r"[Kk]usalākusalānaṃ dhammānaṃ vipāk\S*( \S+){0,3}", p)
                        print(part[:4], "P:", m.group(0))
                        i = H.BID.sub("", h)
                        k = i.find("फल")
                        print("     H:", i[max(0, k - 60):k + 40])
                    else:
                        print(part[:4], "P:", H.norm(p)[-90:])
                        print("     H:", H.norm(h)[-110:])
    print("count", n)
for i in ("1-1039",):
    for part in H.PARTS:
        for sid, ps, hs in H.segments(part):
            if sid == i:
                print(sid, " ".join(ps)[:600]); print(" ".join(hs)[:600])
