# -*- coding: utf-8 -*-
"""Scratch lookups for chapters 13-15 (prints only; writes nothing)."""
import importlib
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai")
X = importlib.import_module("build_10-12_vi")
S, B, T, F, G, H = X.S, X.B, X.T, X.F, X.G, X.H

what = sys.argv[1] if len(sys.argv) > 1 else ""
if what == "body":
    for k, v in G.BODY.items():
        if sys.argv[2] in k:
            print(repr(k), "=>", v)
elif what == "open":
    for k, v in G.PI1_OPEN.items():
        if sys.argv[2] in k:
            print(repr(k), "=>", v)
elif what == "tas":
    for k, v in G.PI1_TASSEVA.items():
        if sys.argv[2] in k:
            print(repr(k), "=>", v)
elif what == "item":
    for s, k in T.SURF.items():
        if sys.argv[2] in s:
            print(repr(s), k, "=>", T.ITEMS[k])
elif what == "attr":
    mod = {"S": S, "B": B, "T": T, "F": F, "G": G, "H": H, "X": X}[sys.argv[2]]
    for n in sys.argv[3:]:
        print(n, "=", repr(getattr(mod, n)))
elif what == "grep":
    mod = {"S": S, "B": B, "T": T, "F": F, "G": G, "H": H, "X": X}[sys.argv[2]]
    for n in dir(mod):
        v = getattr(mod, n)
        if isinstance(v, str) and sys.argv[3] in v:
            print(n, "=", repr(v)[:300])
        elif isinstance(v, dict):
            for k, vv in v.items():
                if isinstance(vv, str) and (sys.argv[3] in vv or sys.argv[3] in str(k)):
                    print(f"{n}[{k!r}] =", repr(vv)[:300])
elif what == "compose":
    print(G.opening(sys.argv[2]))
