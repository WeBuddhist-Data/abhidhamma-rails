"""Harmonise scan for the pi-6 Russian zero-shot: identical Pāli lines (block id stripped) must have
identical Russian across all chapter files. Prints each Pāli line that has more than one Russian rendering.

usage: python -I -X utf8 -B harmonise_scan.py [max_groups] [min_len]
"""
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / "AI_translation/pali/pi-6_split_chapters"
RDIR = ROOT / "AI_translation/russian/pi-6-russian-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
SENT = re.compile(r"(?<=[.?])\s+")
SENTENCES = "--sent" in sys.argv
if SENTENCES:
    sys.argv.remove("--sent")
if "--rails" in sys.argv:  # scan the rails translation instead of the zero-shot
    sys.argv.remove("--rails")
    RDIR = ROOT / "AI_translation/russian/pi-6-russian-plain-rails_split_chapters"


def lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def main():
    maxg = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    minlen = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    groups = collections.defaultdict(lambda: collections.defaultdict(list))
    for pf in sorted(PDIR.glob("*.md")):
        rf = RDIR / pf.name
        pl, rl = lines(pf), lines(rf)
        assert len(pl) == len(rl), pf.name
        for i, (p, r) in enumerate(zip(pl, rl)):
            pk, rk = ID.sub("", p).strip(), ID.sub("", r).strip()
            pairs = [(pk, rk)]
            if SENTENCES:
                ps, rs = SENT.split(pk), SENT.split(rk)
                pairs = list(zip(ps, rs)) if len(ps) == len(rs) else []
            for a, b in pairs:
                if len(a) >= minlen:
                    groups[a][b].append(f"{pf.stem}:{i + 1}")
    bad = [(k, v) for k, v in groups.items() if len(v) > 1]
    print(f"distinct Pāli lines: {len(groups)}; with >1 Russian rendering: {len(bad)}")
    for k, v in bad[:maxg]:
        print("PI:", k[:300])
        for r, locs in sorted(v.items(), key=lambda x: -len(x[1])):
            print(f"  [{len(locs)}] {', '.join(locs[:4])}: {r[:300]}")


if __name__ == "__main__":
    main()
