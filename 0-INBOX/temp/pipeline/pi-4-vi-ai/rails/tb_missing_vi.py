"""Helper: list the words of a pi-4 source chapter that have no exact termbase headword,
and print the termbase entries whose headword is a substring of each such word (members).

usage: python -I -X utf8 tb_missing_vi.py <ch> [line-regex]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / "AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md"
SRC = ROOT / "AI_translation/pali/pi-4_split_chapters"


def main():
    ch = sys.argv[1]
    lre = re.compile(sys.argv[2]) if len(sys.argv) > 2 else None
    heads = {}
    for ln in TB.read_text(encoding="utf-8").splitlines():
        h, _, _ = ln.partition(": {")
        heads.setdefault(h.strip().lower(), ln)
    text = (SRC / f"{ch}.md").read_text(encoding="utf-8")
    seen = set()
    for line in text.splitlines():
        if lre and not lre.search(line):
            continue
        line = re.sub(r"\[[^\]]*\]", " ", line)
        for w in re.findall(r"[^\W\d_]+", line.lower()):
            if w in seen or w in heads:
                continue
            seen.add(w)
            members = [h for h in heads if len(h) >= 3 and " " not in h and h in w and h != w]
            members.sort(key=len, reverse=True)
            print(f"{w}: " + " | ".join(heads[m].split(': {', 1)[0] + ' = ' + heads[m].split(': {', 1)[1].rstrip('}') for m in members[:4]))


if __name__ == "__main__":
    main()
