"""Per line, compare the number of sentence ends (".", "?" before a space or at the end of the line, block id
stripped, bracketed text and ellipses removed) in the Pāli and the Russian (pi-6). A mismatch can mean a
sentence was split or joined against the Pāli punctuation.

usage: python -I -X utf8 -B stop_scan.py [max]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / "AI_translation/pali/pi-6_split_chapters"
RDIR = ROOT / "AI_translation/russian/pi-6-russian-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def ends(s):
    s = ID.sub("", s)
    s = re.sub(r"\[[^\]]*\]|\([^)]*\)", "", s)
    s = re.sub(r"…\s*pe\s*…\.?|…\.?", "", s, flags=re.I)
    return len(re.findall(r"[.?](?=\s|$)", s.strip()))


def main():
    mx = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    n = 0
    for pf in sorted(PDIR.glob("*.md")):
        if pf.stem == "preamble":
            continue
        pl, rl = lines(pf), lines(RDIR / pf.name)
        for i, (p, r) in enumerate(zip(pl, rl)):
            if p.lstrip().startswith("#"):
                continue
            a, b = ends(p), ends(r)
            if a != b:
                n += 1
                if n <= mx:
                    print(f"{pf.stem}:{i + 1} pali {a} ru {b}")
                    print("   PI:", p[:300])
                    print("   RU:", r[:300])
    print("mismatched lines:", n)


if __name__ == "__main__":
    main()
