r"""Helper for 3-0x-ayatanayamaka: vocabulary and line templates of the Pali source.
usage: python -I -X utf8 analyze_3_hi.py words|templates [file-numbers]
"""
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
ID_RE = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")

AY = r"(?:cakkh|sot|ghān|jivh|kāy|rūp|sadd|gandh|ras|phoṭṭhabb|man|dhamm)āyatana(?:ṃ|ñca|nti|ñceva)?"


def lines(nums):
    for n in nums:
        f = PALI_DIR / f"3-0{n}-ayatanayamaka.md"
        for i, l in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if l.strip():
                yield n, i, ID_RE.sub("", l)


def main():
    mode = sys.argv[1]
    nums = [int(x) for x in sys.argv[2:]] or [1, 2, 3, 4, 5, 6]
    if mode == "words":
        c = collections.Counter()
        for _, _, l in lines(nums):
            if l.startswith("#"):
                continue
            for w in re.findall(r"[^\s,.?;()\[\]…]+", l):
                c[w] += 1
        for w, k in sorted(c.items()):
            print(k, w)
    elif mode == "templates":
        c = collections.Counter()
        ex = {}
        for n, i, l in lines(nums):
            if l.startswith("#"):
                continue
            t = re.sub(AY, "A", l)
            t = re.sub(r"\b(?:n?uppajj|nirujjh|na nirujjh|na uppajj)\S*", "V", t)
            t = re.sub(r"\b[A-Za-zāīūṃñṭḍṅṇḷ]+ānaṃ\b", "G", t)
            t = re.sub(r"(G )+", "G ", t)
            c[t] += 1
            ex.setdefault(t, (n, i))
        for t, k in sorted(c.items(), key=lambda x: -x[1]):
            print(k, ex[t], t)


if __name__ == "__main__":
    main()
