"""Map 1-01-kusalattika and 1-02-vedanattika (pi-7 Pāli -> Hindi keywords).
usage: python -I -B -X utf8 map_1-01_1-02_hi.py [--audit]
Tables: map_1_01_1_02_tables_hi.py (T, OVR, ALLOWED); shared tooling: map_sample_hi.py (read-only).
"""
import sys, pathlib; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa: F401,F403
from map_1_01_1_02_tables_hi import T, OVR, ALLOWED

FILES = ("1-01-kusalattika", "1-02-vedanattika")
if __name__ == "__main__":
    for F in FILES:
        build_part(F, make_resolver(F, {**PI7, **T}, OVR[F]))
        verify(F, allowed=ALLOWED[F])
        if "--audit" in sys.argv:
            audit(F, {**PI7, **T}, OVR[F], only_fallback=True)
