"""Find Pāli phrases of pi-2 chapters 10-12 in the pi-1 Pāli split chapters and show the approved pi-1 Vietnamese
line of the same position (same file, same line number). Reads only AI_translation/pali/pi-1_split_chapters/*.md and
AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/*.md. Writes rails/pi1-find-10-12-vi.txt.

usage: python -I -X utf8 pi1_find_10_12_vi.py "phrase one" "phrase two" ...
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PA = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
VI = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
OUT = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-2-vi-ai" / "rails" / "pi1-find-10-12-vi.txt"
MAXHITS = 2


def main():
    files = sorted(PA.glob("*.md"))
    data = []
    for f in files:
        pa = f.read_text(encoding="utf-8").splitlines()
        vi = (VI / f.name).read_text(encoding="utf-8").splitlines()
        data.append((f.name, pa, vi))
    out = []
    for phrase in sys.argv[1:]:
        out.append(f"### {phrase}")
        n = 0
        for name, pa, vi in data:
            for i, ln in enumerate(pa):
                if phrase in ln:
                    bid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
                    out.append(f"[{name}:{i + 1}{' ^' + bid.group(1) if bid else ''}] PA: {ln}")
                    out.append(f"VI: {vi[i]}")
                    n += 1
                    if n >= MAXHITS:
                        break
            if n >= MAXHITS:
                break
        if not n:
            out.append("(no hit)")
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"wrote {OUT.name}: {len(sys.argv) - 1} phrases")


if __name__ == "__main__":
    main()
