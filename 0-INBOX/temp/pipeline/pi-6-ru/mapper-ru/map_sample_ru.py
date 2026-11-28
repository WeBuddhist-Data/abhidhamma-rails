"""Build the SAMPLE Pāli->Russian keyword maps for pi-6 (Yamaka): preamble, 1-mulayamaka.

usage: python -I -X utf8 -B map_sample_ru.py        (writes the two <part>.mapped.md and verifies them)

Resolution order per keyword: OVERRIDES[bid][kw] -> (preamble: pi-1 CORE) -> TABLE (= YM of map_common_pi6_ru.py
plus this sample's additions) -> pi-2 KH -> pi-1 CH2 / MATRIX.  Endings -ti / -ñca / -ñceva fold to the base keyword.
Every segment of both parts was compared with its Russian; the Mūlayamaka is fully formulaic (the builder used fixed
phrase tables), so identical Pāli gets identical Russian and the table covers it. OVERRIDES holds the segment-specific
readings; the sample needed none beyond the table (kept as the pattern for the later parts).
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi6_ru import (CORE, NDE, YM, allowed_for, build_part, lc, value,  # noqa: E402,F401
                               verify)

PARTS = ["preamble", "1-mulayamaka"]

# this sample's own additions on top of YM (none needed: every Mūlayamaka keyword is in YM)
TABLE = {**YM}

# per-segment readings: {block id: {keyword exactly as listed: Russian}}
OVERRIDES = {}


def resolver_for(part):
    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if lc(kw) in CORE and lc(kw) not in TABLE:
            return CORE[lc(kw)]
        return value(kw, kws, TABLE)
    return resolve


if __name__ == "__main__":
    for p in PARTS:
        build_part(p, resolver_for(p))
        verify(p, show=200, allowed=allowed_for(p))
