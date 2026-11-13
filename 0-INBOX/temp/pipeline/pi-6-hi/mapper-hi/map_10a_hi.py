"""pi-6 Indriyayamaka, first half (10-01 .. 10-06): Pāli->Hindi keyword maps.
Table: PI6 (sample) + IND (map_10_common_hi, shared with 10-07 .. 10-13) + T (this half only), per-segment OVR.
usage: python -I -X utf8 map_10a_hi.py [file ...]"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI6, NDE, make_resolver, build_part, verify  # noqa: E402  (read-only import)
from map_10_common_hi import IND  # noqa: E402

FILES = [f"10-0{i}-indriyayamaka" for i in range(1, 7)]

T = {}                                  # nothing beyond IND needed («(no direct equivalent)» artefact: in IND)
assert IND["(no direct equivalent)"] == NDE

OVR = {f: {} for f in FILES}
ALLOWED = {f: {} for f in FILES}

if __name__ == "__main__":
    table = {**PI6, **IND, **T}
    for f in (sys.argv[1:] or FILES):
        build_part(f, make_resolver(f, table, OVR[f]))
        verify(f, allowed=ALLOWED[f])
