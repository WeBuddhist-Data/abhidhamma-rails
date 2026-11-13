"""Segments whose Hindi has a given frame string; prints the keywords mapped to a chosen value set.
Checks: Sampayuttavāra frame «जुड़कर», Sahajātavāra «जन्म लेकर», Saṃsaṭṭhavāra «घुल-मिलकर», Nissayavāra «आश्रय से».
usage: python -I -B -X utf8 frames_3-02_3-06_hi.py
"""
import sys, pathlib; sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import read_hindi  # noqa
FILES = ["3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka", "3-05-ganthagocchaka",
         "3-06-oghayogagocchaka"]
CHECK = {"जुड़कर": ("sampayutt",), "जन्म लेकर": ("sahajāt",), "घुल-मिलकर": ("saṃsaṭṭh",), "आश्रय से": ("nissāya",)}
for f in FILES:
    hi = read_hindi(f)
    for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        if "] " not in line:
            continue
        bid = line.split("] ")[0][1:]
        h = hi.get(bid, "")
        for frame, stems in CHECK.items():
            if frame in h:
                pairs = [p for p in line.split("] ", 1)[1].split(", ") if any(s in p.split("=")[0].lower() for s in stems)]
                print(f[:4], bid, frame, "|", ", ".join(pairs) or "-")
