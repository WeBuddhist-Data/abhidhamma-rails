"""Exploration helper: print the Pāli and Russian lines of segments.

usage: python -I -X utf8 show_seg_ru.py <part-prefix>:<id> [...] [--bak] [--nop]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ru_common as C

if "--bak" in sys.argv:
    C.CUR["rdir"] = C.BAK
nop = "--nop" in sys.argv
for arg in [a for a in sys.argv[1:] if not a.startswith("--")]:
    pre, sid = arg.split(":", 1)
    for part in C.PARTS:
        if not part.startswith(pre):
            continue
        for s, ps, rs in C.segments(part):
            if s == sid:
                print(f"== {part}:{s}")
                for p, r in zip(ps, rs):
                    if not nop:
                        print("P:", p)
                    print("R:", r)
