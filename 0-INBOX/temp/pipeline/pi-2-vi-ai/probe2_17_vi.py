# -*- coding: utf-8 -*-
"""Scratch: print a few strings imported from build_16_vi (writes nothing)."""
import importlib
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai")
Z = importlib.import_module("build_16_vi")
print("KILESA10:", Z.KILESA10)
print("VIEWS10:", Z.VIEWS10)
print("ATTHI_DINNA:", Z.ATTHI_DINNA)
print("TITLE17:", Z.S.CHAPTER_TITLES[17])
print("IDHA:", repr(Z.IDHA), "TATTHA:", repr(Z.TATTHA))
