# -*- coding: utf-8 -*-
"""Scratch: print strings from the earlier builders (import only; writes nothing)."""
import importlib, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai")
Y = importlib.import_module("build_13-15_vi")
X = Y.X
S, B, T, F, G, H = Y.S, Y.B, Y.T, Y.F, Y.G, Y.H
for name in sys.argv[1:]:
    try:
        v = eval(name)
    except Exception as e:
        v = f"ERR {e!r}"
    print(f"## {name}:\n{v!r}"[:3000])
