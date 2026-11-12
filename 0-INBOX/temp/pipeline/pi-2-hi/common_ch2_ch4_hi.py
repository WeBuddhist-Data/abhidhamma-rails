# -*- coding: utf-8 -*-
"""Shared helpers for the chapter-2 and chapter-4 builders (Hindi, pi-2)."""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_ch1_sample_hi as S   # approved sample: constants and frame functions (import only)

ROOT = S.ROOT
PALI_DIR, HI_DIR, PI1_HI_DIR = S.PALI_DIR, S.HI_DIR, S.PI1_HI_DIR
PI5_HI_DIR = os.path.join(ROOT, r"AI_translation\hindi\pi-5-hindi-plain-rails_split_chapters")
DASH = S.DASH
_ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def _read(p):
    return open(p, encoding="utf-8-sig").read()


_PI1 = None


def pi1(block_id):
    """the reviewed pi-1 Hindi line that ends with ^block_id (id stripped)."""
    global _PI1
    if _PI1 is None:
        _PI1 = {}
        for f in os.listdir(PI1_HI_DIR):
            if f.endswith(".md"):
                for l in _read(os.path.join(PI1_HI_DIR, f)).splitlines():
                    m = _ID.search(l)
                    if m:
                        _PI1[m.group(1)] = l[:m.start()]
    return _PI1[block_id]


def sub1(text, old, new):
    """replace exactly one occurrence (asserted)."""
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new)


def check_in_pi(strings, dirs=(PI1_HI_DIR,)):
    corpus = "\n".join(_read(os.path.join(d, f)) for d in dirs for f in os.listdir(d) if f.endswith(".md"))
    corpus = re.sub(r"\s*\[[^\]]*\]", "", corpus)
    missing = [s for s in strings if s not in corpus]
    assert not missing, "not found in reviewed Hindi: " + " | ".join(missing)


def join_and(items):
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " और " + items[-1]


def write_chapter(name, hindi_lines):
    pali = _read(os.path.join(PALI_DIR, name)).splitlines()
    n = sum(1 for l in pali if l.strip())
    assert len(hindi_lines) == n, f"{name}: {len(hindi_lines)} Hindi lines for {n} Pāli lines"
    text = S.assemble(pali, hindi_lines)
    assert "—" not in text and ":-" not in text
    with open(os.path.join(HI_DIR, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("written:", name, n, "lines")


def pali_lines(name):
    return [l for l in _read(os.path.join(PALI_DIR, name)).splitlines() if l.strip()]


def strip_id(l):
    return _ID.sub("", l)
