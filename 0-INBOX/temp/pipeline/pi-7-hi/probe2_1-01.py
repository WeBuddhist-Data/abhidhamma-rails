"""Probe helper 2 for 1-01: distinct heading texts and distinct ghaṭanā components."""
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S

P = [l for l in (S.PALI_DIR / "1-01-kusalattika.md").read_text(encoding="utf-8").splitlines() if l.strip()]
mode = sys.argv[1]
if mode == "heads":
    c = collections.Counter()
    for i, l in enumerate(P, 1):
        if l.startswith("#") and not (i <= 190 or 1235 <= i <= 1262):
            t = S.ID_RX.sub("", l).lstrip("#").strip().strip("*")
            c[t] += 1
    for t, n in sorted(c.items()):
        print(n, t)
elif mode == "nti":
    c = collections.Counter()
    for l in P:
        for m in re.finditer(r"([A-ZĀa-zāīūṃṅñṭḍṇḷ\- ]+?)(?:nti|ti)\b", S.ID_RX.sub("", l)):
            pass
    rx = re.compile(r"(?:^|\. |\.\) )([A-ZĀ][^.()]*?)(?:anti|īti|ti) ")
    for l in P:
        for m in rx.finditer(S.ID_RX.sub("", l)):
            for comp in re.split(r"-", m.group(1)):
                c[comp.strip()] += 1
    for t, n in sorted(c.items()):
        print(n, t)
elif mode == "notes":
    c = collections.Counter()
    for i, l in enumerate(P, 1):
        if l.startswith("#") or i <= 190 or 1235 <= i <= 1262:
            continue
        for m in re.finditer(r"\([^()]*\)", l):
            c[m.group(0)] += 1
    for t, n in sorted(c.items()):
        print(n, t)
