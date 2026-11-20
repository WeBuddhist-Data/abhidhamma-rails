"""Write every pi-2 Vietnamese termbase entry whose headword occurs (as whole words) in chapter 16 of the pi-2
Pāli to rails/tb-16-vi.txt, entries in termbase order.

usage: python -I -X utf8 tb_16_vi.py
"""
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / "AI_translation" / "vietnamese" / "pi-2-pali-vietnamese-termbase-plain.md"
PALI = ROOT / "AI_translation" / "pali" / "pi-2_split_chapters"
OUT = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-2-vi-ai" / "rails" / "tb-16-vi.txt"
PARTS = ["16-nanavibhango.md"]


def norm(s):
    return unicodedata.normalize("NFC", s).lower()


def words(path):
    text = norm(path.read_text(encoding="utf-8"))
    text = re.sub(r"\^[0-9a-z-]+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    return " " + re.sub(r"\s+", " ", text) + " "


def main():
    tb = [ln for ln in TB.read_text(encoding="utf-8").splitlines() if ":" in ln]
    seen = set()
    out = []
    for part in PARTS:
        text = words(PALI / part)
        out.append(f"## {part}")
        for line in tb:
            head = norm(line.split(":", 1)[0].strip())
            if head and f" {head} " in text and line not in seen:
                seen.add(line)
                out.append(line)
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"wrote {OUT.name}: {len(out)} lines")


if __name__ == "__main__":
    main()
