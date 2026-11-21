"""Coordinator rails consistency scan, pi-5 (2026-11-21): run find_divergences_vi.py (written for the zero-shot)
on the RAILS chapters instead, by pointing vi_common.CUR["vdir"] at the rails folder. Writes rails/divergences-rails.md.

usage: python -I -X utf8 -B consistency_find_vi.py
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)
sys.path.insert(0, PARENT)
import vi_common  # noqa: E402
import find_divergences_vi as F  # noqa: E402

RAILS = os.path.join(vi_common.ROOT, r"AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters")
vi_common.CUR["vdir"] = RAILS
sys.argv = [sys.argv[0], os.path.join(HERE, "divergences-rails.md")]
F.main()
