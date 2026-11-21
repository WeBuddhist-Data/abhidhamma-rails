"""Helper: print every pi-4 termbase entry whose headword occurs in the sample source chapters
(as a whole word / word sequence, case-insensitive), or is a compound member of a word there.

usage: python -I -X utf8 tb_sample_lookup_vi.py [ch ...]   (default: preamble 1-matika 2-ekakapuggalapannatti)
       python -I -X utf8 tb_sample_lookup_vi.py --word <regex>   (grep the headwords)
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / "AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md"
SRC = ROOT / "AI_translation/pali/pi-4_split_chapters"


def entries():
    for ln in TB.read_text(encoding="utf-8").splitlines():
        if ":" not in ln:
            continue
        head, _, rest = ln.partition(": {")
        yield head.strip(), ln


def main():
    args = sys.argv[1:]
    if args and args[0] == "--word":
        pat = re.compile(args[1], re.I)
        for head, ln in entries():
            if pat.search(head):
                print(ln)
        return
    chs = args or ["preamble", "1-matika", "2-ekakapuggalapannatti"]
    text = "\n".join((SRC / f"{c}.md").read_text(encoding="utf-8") for c in chs).lower()
    words = set(re.findall(r"[^\W\d_]+", text))
    for head, ln in entries():
        h = head.lower()
        hw = re.findall(r"[^\W\d_]+", h)
        if not hw:
            continue
        if len(hw) > 1:
            ok = re.search(r"(?<!\w)" + r"\W+".join(map(re.escape, hw)) + r"(?!\w)", text)
        else:
            ok = hw[0] in words or (len(hw[0]) >= 4 and any(hw[0] in w for w in words))
        if ok:
            print(ln)


if __name__ == "__main__":
    main()
