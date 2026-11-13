"""pi-6 Anusayayamaka 7-01 … 7-05: build <f>.mapped.md from the shared Anusaya table (map_7_common_hi) + overrides.
usage: python -I -X utf8 map_7a_hi.py [file ...]   (default: all five)"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_7_common_hi import TABLE7, build_part, make_resolver, verify7  # noqa: E402

FILES = ("7-01-anusayayamaka", "7-02-anusayayamaka", "7-03-anusayayamaka", "7-04-anusayayamaka",
         "7-05-anusayayamaka")
T = {}                                   # chapter entries beyond T7 (none needed so far)
OVR = {f: {} for f in FILES}             # {file: {bid: {kw: value}}}
ALLOWED = {f: {} for f in FILES}         # {file: {(bid, kw): reason}}

if __name__ == "__main__":
    for f in (sys.argv[1:] or FILES):
        build_part(f, make_resolver(f, {**TABLE7, **T}, OVR[f]))
        verify7(f, allowed=ALLOWED[f])
