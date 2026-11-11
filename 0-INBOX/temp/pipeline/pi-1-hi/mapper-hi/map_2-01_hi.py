"""Map 2-01-cittuppadakandam keywords to the Hindi translation (CH2 table + per-segment overrides).

usage: python -I -X utf8 map_2-01_hi.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import ch2_value, build_part, verify  # noqa: E402

PART = "2-01-cittuppadakandam"

# per-segment overrides: {bid: {kw: value}}
OVERRIDES = {
}


def resolver(bid, kw, kws):
    o = OVERRIDES.get(bid, {})
    if kw in o:
        return o[kw]
    return ch2_value(kw, kws)


if __name__ == "__main__":
    build_part(PART, resolver)
    verify(PART)
