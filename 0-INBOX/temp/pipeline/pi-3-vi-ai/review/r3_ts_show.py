"""r3 review helper: print (console only) the Pāli, our Vietnamese and the Tịnh Sự segment for given IDs.
Writes nothing. Usage: python -I -X utf8 r3_ts_show.py 3-306 3-309 ... [--nots] [--en] [--ru]
"""
import re, sys
from pathlib import Path

ROOT = Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / r"AI_translation\pali\pi-3_split_chapters"
VDIR = ROOT / r"AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters"
RDIR = ROOT / r"AI_translation\russian\pi-3-russian-plain-rails_split_chapters"
EN = ROOT / r"AI_translation\english\pi-3-english-plain.md"
TS = ROOT / r"1-SOURCES\Translations\Vietnamese\vi-3-tinh_su.md"
CH = ["8-sattamanayo.md", "9-atthamanayo.md", "10-navamanayo.md", "11-dasamanayo.md",
      "12-ekadasamanayo.md", "13-dvadasamanayo.md", "14-terasamanayo.md", "15-cuddasamanayo.md"]


def seg_map(paths):
    out = {}
    for p in paths:
        if not p.exists():
            continue
        for b in re.split(r"\n\s*\n", p.read_text(encoding="utf-8").strip()):
            m = re.search(r"\^(3-[0-9-]+)\s*$", b)
            if m:
                out[m.group(1)] = b
    return out


def main():
    ids = [a for a in sys.argv[1:] if not a.startswith("--")]
    P = seg_map([PDIR / c for c in CH]); V = seg_map([VDIR / c for c in CH])
    R = seg_map([RDIR / c for c in CH]) if "--ru" in sys.argv else {}
    E = seg_map([EN]) if "--en" in sys.argv else {}
    tst = TS.read_text(encoding="utf-8")
    parts = re.split(r"!\[\[[^\]]*#\^(3-[0-9-]+)\]\]", tst)
    T = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
    for i in ids:
        print(f"######## {i}")
        print("PI:", P.get(i, "-"))
        print("VI:", V.get(i, "-"))
        if "--nots" not in sys.argv:
            print("TS:", T.get(i, "-"))
        if E: print("EN:", E.get(i, "-"))
        if R: print("RU:", R.get(i, "-"))


if __name__ == "__main__":
    main()
