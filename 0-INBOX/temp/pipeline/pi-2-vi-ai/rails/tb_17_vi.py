"""Print (writes nothing) every pi-2 Vietnamese termbase entry whose headword occurs (as whole words) in chapter 17
of the pi-2 Pāli, entries in termbase order, also the pi-2 / pi-1 APPROVED decisions are separate files.
usage: python -I -X utf8 tb_17_vi.py <start> <count>      (page through the matches)
       python -I -X utf8 tb_17_vi.py find <regex>          (entries whose headword matches, whole termbase)
"""
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / "AI_translation" / "vietnamese" / "pi-2-pali-vietnamese-termbase-plain.md"
PALI = ROOT / "AI_translation" / "pali" / "pi-2_split_chapters" / "17-khuddakavatthuvibhango.md"


def norm(s):
    return unicodedata.normalize("NFC", s).lower()


def main():
    tb = [ln for ln in TB.read_text(encoding="utf-8").splitlines() if ":" in ln]
    if sys.argv[1] == "find":
        rx = re.compile(sys.argv[2])
        for line in tb:
            if rx.search(norm(line.split(":", 1)[0].strip())):
                print(line)
        return
    text = norm(PALI.read_text(encoding="utf-8"))
    text = re.sub(r"\^[0-9a-z-]+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = " " + re.sub(r"\s+", " ", text) + " "
    out = []
    for line in tb:
        head = norm(line.split(":", 1)[0].strip())
        if head and f" {head} " in text and line not in out:
            out.append(line)
    a, n = int(sys.argv[1]), int(sys.argv[2])
    print(f"# {len(out)} entries; showing {a}..{a + n}")
    for line in out[a:a + n]:
        print(line)


if __name__ == "__main__":
    main()
