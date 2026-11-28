"""Ellipsis spacing scan: per line, the count of "…" preceded by a space and of "…" not preceded by a space
should match between the Pāli ("…pe…" counts as one "…" at the position of its first character) and the Russian.

usage: python -I -X utf8 -B ellipsis_scan.py [max]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / "AI_translation/pali/pi-6_split_chapters"
RDIR = ROOT / "AI_translation/russian/pi-6-russian-plain-zeroshot_split_chapters"


def lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def counts(s, pali):
    if pali:
        s = re.sub(r"…\s*pe\s*…\.?", "…", s, flags=re.I)
        s = s.replace("….", "…")
    # after a word "…" is always tight (pi-1 … pi-5 convention): compare only ellipses after «?» / «.»
    return len(re.findall(r"(?<=[?.]\s)…", s)), len(re.findall(r"(?<=[?.])…", s))


def main():
    mx = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    n = 0
    for pf in sorted(PDIR.glob("*.md")):
        pl, rl = lines(pf), lines(RDIR / pf.name)
        for i, (p, r) in enumerate(zip(pl, rl)):
            a, b = counts(p, True), counts(r, False)
            if a != b:
                n += 1
                if n <= mx:
                    print(f"{pf.stem}:{i + 1} pali(spaced,tight)={a} ru={b}")
                    print("   PI:", p[:220])
                    print("   RU:", r[:220])
    print("mismatched lines:", n)


if __name__ == "__main__":
    main()
