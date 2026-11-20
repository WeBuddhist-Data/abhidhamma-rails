"""Print every pi-2 Vietnamese termbase entry whose headword occurs (as whole words) in a Pāli file.

usage: python -I -X utf8 tb_lookup.py <pali_file> [extra words ...]
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
    text = norm(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    text = re.sub(r"\^[0-9a-z-]+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = " " + re.sub(r"\s+", " ", text) + " "
    extra = [norm(w) for w in sys.argv[2:]]
    for line in TB.read_text(encoding="utf-8").splitlines():
        if ":" not in line:
            continue
        head = norm(line.split(":", 1)[0].strip())
        if not head:
            continue
        if f" {head} " in text or head in extra:
            print(line)


if __name__ == "__main__":
    main()
