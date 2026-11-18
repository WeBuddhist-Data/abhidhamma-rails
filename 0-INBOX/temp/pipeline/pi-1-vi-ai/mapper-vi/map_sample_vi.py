"""Build the SAMPLE Pāli->Vietnamese keyword maps for pi-1: preamble, 1-matika, 2-01-cittuppadakandam.

usage: python -I -X utf8 map_sample_vi.py          (writes the three <part>.mapped.md and verifies them)

Resolution order per keyword: OVERRIDES[bid][kw]  ->  the part's table  ->  (2-01) ch2_value.
The tables live in map_common_vi.py (CORE, MATRIX, CH2); the overrides below are the per-segment
readings found when comparing each segment's Vietnamese (see vi-map-conventions.md).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import CH2, CORE, MATRIX, SATI_BARE, build_part, ch2_value, lc, verify  # noqa: E402

PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam"]

OVERRIDES = {
    # ---- 1-matika: the same Pāli item read differently by its Vietnamese
    "1-M1-16": {"ārammaṇā": "lấy … làm đối tượng",       # «lấy con đường làm đối tượng»
                "hetukā": "lấy … làm gốc rễ"},           # «lấy con đường làm gốc rễ»
    "1-M2-110": {"bhava": "được hiện hữu"},             # «khao khát được hiện hữu»
    "1-M2-120": {"vuṭṭhāna": "việc xuất khỏi",           # «việc xuất khỏi các thành tựu thiền»
                 "vuṭṭhānakusalatā": "sự thành thạo về việc xuất khỏi"},
    "1-M2-129": {"sampajaññañca": "hiểu biết rõ ràng"},  # of asampajañña «sự thiếu hiểu biết rõ ràng»
    # ---- 2-01: the sukha headings (the factor «hạnh phúc», not «dễ chịu» of the feeling string)
    "1-10": {"sukhaṃ": "hạnh phúc"},
    "1-87": {"sukhaṃ": "hạnh phúc"},
    # ---- 2-01: summary lists where sati occurs only inside năng lực / sức mạnh / … đúng đắn
    "1-74": {"sati": SATI_BARE},
    "1-89": {"sati": SATI_BARE},
    "1-95": {"sati": SATI_BARE},
    "1-127": {"sati": SATI_BARE},
    "1-129": {"sati": SATI_BARE},
    "1-130": {"sati": SATI_BARE},
    # ---- 2-01: upekkhā occurs only inside «năng lực bình thản» (the heading of 1-154)
    "1-154": {"upekkhā": "bình thản"},
}


def resolver_for(part):
    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if part == "preamble":
            return CORE[lc(kw)]
        if part == "1-matika":
            return MATRIX[lc(kw)]
        return ch2_value(kw, kws, CH2)
    return resolve


if __name__ == "__main__":
    for p in PARTS:
        build_part(p, resolver_for(p))
        verify(p)
