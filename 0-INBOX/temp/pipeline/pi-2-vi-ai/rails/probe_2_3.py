"""Print pi-1 Pāli and approved pi-1 Vietnamese rails lines side by side (helper for chapters 2-3).

usage: python -I -X utf8 probe_2_3.py <file-stem>:<line> ...      e.g. 3-02-rupakandam:112
       python -I -X utf8 probe_2_3.py id:<block id> ...            e.g. id:1-647
Reads only; writes nothing.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PA = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
VI = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"


def by_id(bid):
    for f in sorted(PA.glob("*.md")):
        lines = f.read_text(encoding="utf-8").splitlines()
        for i, ln in enumerate(lines):
            if re.search(r"\^" + re.escape(bid) + r"\s*$", ln):
                return f.stem, i + 1
    raise KeyError(bid)


def main():
    for a in sys.argv[1:]:
        if a.startswith("id:"):
            stem, n = by_id(a[3:])
        else:
            stem, n = a.rsplit(":", 1)
            n = int(n)
        p = (PA / f"{stem}.md").read_text(encoding="utf-8").splitlines()[n - 1]
        v = (VI / f"{stem}.md").read_text(encoding="utf-8").splitlines()[n - 1]
        print(f"== {stem}:{n}\nPA: {p}\nVI: {v}\n")


if __name__ == "__main__":
    main()
