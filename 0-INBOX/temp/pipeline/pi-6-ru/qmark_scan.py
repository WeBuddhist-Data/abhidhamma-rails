"""Per line, compare the count of "?" in the Pāli and the Russian (pi-6). A mismatch means a question mark
was added or dropped (the user rule: a wrong mark stays as written).

usage: python -I -X utf8 -B qmark_scan.py [max]
"""
import pathlib
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / "AI_translation/pali/pi-6_split_chapters"
RDIR = ROOT / "AI_translation/russian/pi-6-russian-plain-zeroshot_split_chapters"


def lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def main():
    mx = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    n = 0
    for pf in sorted(PDIR.glob("*.md")):
        pl, rl = lines(pf), lines(RDIR / pf.name)
        for i, (p, r) in enumerate(zip(pl, rl)):
            if p.count("?") != r.count("?"):
                n += 1
                if n <= mx:
                    print(f"{pf.stem}:{i + 1} pali ? {p.count('?')} ru ? {r.count('?')}")
                    print("   PI:", p[:260])
                    print("   RU:", r[:260])
    print("mismatched lines:", n)


if __name__ == "__main__":
    main()
