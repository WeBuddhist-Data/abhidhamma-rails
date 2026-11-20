"""Print (writes nothing) pi-2 Vietnamese termbase entries for chapter 18.
usage: python -I -X utf8 tb_18_vi.py find <regex> [<regex> ...]   (entries whose headword matches, whole termbase)
"""
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / "AI_translation" / "vietnamese" / "pi-2-pali-vietnamese-termbase-plain.md"


def norm(s):
    return unicodedata.normalize("NFC", s).lower()


def main():
    tb = [ln for ln in TB.read_text(encoding="utf-8").splitlines() if ":" in ln]
    for pat in sys.argv[2:]:
        rx = re.compile(norm(pat))
        print(f"## {pat}")
        for line in tb:
            if rx.search(norm(line.split(":", 1)[0].strip())):
                print(line)


if __name__ == "__main__":
    main()
