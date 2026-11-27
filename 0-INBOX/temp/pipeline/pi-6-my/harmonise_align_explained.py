"""Consistency pass: every difference left in align-after.txt (pi-1-my/align_check_my.py) and align-hidden-after.txt
(pi-1-my/align_hidden_my.py) must be listed here with the reason (the Pāli context differs). Prints the counts and
every unexplained difference; exit 1 if any. Model: pi-5-my/harmonise_align_explained.py (read only).
usage: python3 -I -X utf8 harmonise_align_explained.py"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent

# Pāli sentence (as align_check_my prints it after «PĀLI: ») -> reason. Empty: after the pass nothing differs.
EXPLAINED = {}
HIDDEN_EXPLAINED = {}


def main():
    a = (HERE / "align-after.txt").read_text(encoding="utf-8")
    h = (HERE / "align-hidden-after.txt").read_text(encoding="utf-8")
    n = int(re.search(r"with differing Burmese: (\d+)", a)[1])
    found = re.findall(r"^PĀLI: (.+)$", a, flags=re.M)
    bad = [s for s in found if s not in EXPLAINED]
    hn = int(re.search(r"unmatched repeated sentences: (\d+)", h)[1])
    hfound = re.findall(r"^\S+\s+PĀLI: (.+)$", h, flags=re.M)
    hbad = [s for s in hfound if s not in HIDDEN_EXPLAINED]
    print(f"align_check: {n} differing, {n - len(bad)} explained, {len(bad)} unexplained; "
          f"align_hidden: {hn} unmatched, {hn - len(hbad)} explained, {len(hbad)} unexplained")
    for s in bad + hbad:
        print(f"   UNEXPLAINED: {s[:150]}")
    return 1 if bad or hbad else 0


if __name__ == "__main__":
    sys.exit(main())
