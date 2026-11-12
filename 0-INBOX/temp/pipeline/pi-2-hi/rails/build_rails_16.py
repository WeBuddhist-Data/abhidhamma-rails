"""Builder: Hindi rails (plain) of pi-2 chapter 16, Ñāṇavibhaṅga.

Uses build_rails_16_a.py / build_rails_16_b.py (strings) and build_rails_sample (read-only: paths + emit).
Writes only AI_translation/hindi/pi-2-hindi-plain-rails_split_chapters/16-nanavibhango.md

usage: python -I -X utf8 build_rails_16.py
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails")
import build_rails_sample as S  # noqa: E402
import build_rails_16_a as A  # noqa: E402
import build_rails_16_b as B  # noqa: E402

FILE = "16-nanavibhango.md"


def build(src):
    segs = dict(S.segs_of_lines(src))
    h = {"2-16-0": ["### ज्ञान का विश्लेषण"]}
    for n in range(1, 11):
        h[f"2-16-{n}-0"] = [A.matika_heading(n)]
    h["2-16-11-0"] = ["#### मूल सूची"]
    for n in range(1, 11):
        h[f"2-16-11-{n}-0"] = [A.niddesa_heading(n)]
    h["2-751"] = A.ekaka_matika()
    h["2-752"] = A.duka_matika()
    h["2-753"] = A.tika_matika(segs["2-753"])
    h["2-754"] = A.catukka_matika()
    h.update(A.small_matikas())
    h["2-761"] = A.ekaka_niddesa_761()
    h["2-762"] = A.ekaka_niddesa_762()
    h["2-763"] = A.cross_segment("gocara")
    h["2-764"] = A.ekaka_niddesa_764()
    h["2-765"] = A.cross_segment("after")
    h["2-766"] = A.ekaka_niddesa_766()
    h["2-767"] = A.duka_niddesa()
    h.update(A.tika_niddesa_a())
    h.update(B.catukka_a())
    h.update(B.small_niddesa())
    h.update(B.powers())
    return h


def main():
    src = (S.PALI / FILE).read_text(encoding="utf-8").splitlines()
    S.emit(src, build(src), S.OUT / FILE)


if __name__ == "__main__":
    main()
