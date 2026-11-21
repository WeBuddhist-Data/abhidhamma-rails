"""r3 review helper: rough item-count comparison Pāli vs Tịnh Sự for segments whose items are all
'...dhammehi' matrix items. Console only; writes nothing. Usage: python -I -X utf8 r3_ts_items.py
"""
import re
from pathlib import Path

ROOT = Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / r"AI_translation\pali\pi-3_split_chapters"
TS = ROOT / r"1-SOURCES\Translations\Vietnamese\vi-3-tinh_su.md"
CH = ["8-sattamanayo.md", "9-atthamanayo.md", "10-navamanayo.md", "11-dasamanayo.md",
      "12-ekadasamanayo.md", "13-dvadasamanayo.md", "14-terasamanayo.md", "15-cuddasamanayo.md"]


def main():
    txt = TS.read_text(encoding="utf-8")
    parts = re.split(r"!\[\[[^\]]*#\^(3-[0-9-]+)\]\]", txt)
    T = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
    n = 0
    for ch in CH:
        for b in re.split(r"\n\s*\n", (PDIR / ch).read_text(encoding="utf-8").strip()):
            m = re.search(r"\^(3-[0-9-]+)\s*$", b)
            if not m or b.startswith("#"):
                continue
            sid = m.group(1); first = b.split("\n")[0]
            mm = re.search(r"ye dhammā (sampayuttā|vippayuttā|khandhasaṅgahena)|ye vippayuttā", first)
            head = first[:mm.end()] if mm else first
            items = len(re.findall(r"…pe…|…|\.\.(?!\.)", first[:mm.start()] if mm else first)) + 1
            dh = len(re.findall(r"dhammehi ye (?:dhammā|vippayuttā)", head))
            if dh != items or "…pe…" in head:
                continue
            t = T.get(sid, "")
            tm = re.search(r"mà (những )?pháp nào|bằng cách|,? (thì )?những pháp đó|, thì|những pháp ấy|thì pháp", t)
            th = t[:tm.start()] if tm else t
            tc = len(re.findall(r"(?:với|,|và) pháp ", th))
            n += 1
            if tc != items:
                print(f"{sid}: Pāli items {items}, TS 'pháp' items {tc}")
    print("compared", n)


if __name__ == "__main__":
    main()
