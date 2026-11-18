"""Review helper for the pi-1 part 5-atthakathakandam Vietnamese keyword map (writes nothing).

usage: python -I -X utf8 probe_5_vi.py pali REGEX     (per segment: every Pāli match with 40 chars of context)
       python -I -X utf8 probe_5_vi.py vi REGEX       (the same on the Vietnamese)
       python -I -X utf8 probe_5_vi.py seg ID [ID ..]  (Pāli, Vietnamese and keywords of the segments)
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import read_keywords, read_pali, read_vietnamese  # noqa: E402

PART = "5-atthakathakandam"

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode in ("pali", "vi"):
        segs = read_pali(PART) if mode == "pali" else read_vietnamese(PART)
        rx = re.compile(sys.argv[2])
        for bid, t in segs.items():
            hits = [t[max(0, m.start() - 40): m.end() + 10].replace("\n", " ") for m in rx.finditer(t)]
            if hits:
                print(bid, " | ".join(hits))
    elif mode == "seg":
        pa, vi, kw = read_pali(PART), read_vietnamese(PART), dict(read_keywords(PART))
        for bid in sys.argv[2:]:
            print(bid, "PALI:", pa.get(bid))
            print(bid, "VI:", vi.get(bid))
            print(bid, "KW:", ", ".join(kw.get(bid, [])))
            print()
