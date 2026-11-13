"""pi-6 Anusayayamaka 7-06 .. 7-11: Pāli->Hindi keyword maps (driver).

usage: python -I -X utf8 map_7b_hi.py [7-06-anusayayamaka ...]     (no argument: all six files)

Tables: TABLE7 of the shared Anusaya module map_7_common_hi (= PI6 + T7, imported read-only) plus T7B below,
which holds only what 7-06 .. 7-11 alone need (the dhātu section of 7-10 / 7-11). T7B never overrides a key
of T7 (checked at run time). Presence check: verify7 (map_sample_hi.present + सोया ~ सोई / सोए).
Wording = the Hindi of build_7b_hi.py (notes-7b.md) as the translation files have it.
"""
import pathlib
import sys

sys.dont_write_bytecode = True                      # no __pycache__ in the shared folder
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_7_common_hi import T7, TABLE7, verify7, build_part, make_resolver  # noqa: E402  (read-only)

FILES = [f"7-{i:02d}-anusayayamaka" for i in range(6, 12)]

# ---------------------------------------------------------------------------- T7B (7-10 end, 7-11)
T7B = {
    # «… इंद्रिय-सुखों के लोक में ही जन्म लेता है»: -yeva = ही, the keyword maps to the place (pi-1 X-meva rule)
    "kāmadhātuṃyeva": "इंद्रिय-सुखों का लोक",
    # «कितनी सुप्त प्रवृत्तियाँ भंग हो चुकी हैं», «भंग हो चुकी सुप्त प्रवृत्तियाँ नहीं हैं»: participle, masc. sg.
    "bhaṅgā": "भंग हो चुका",
    # «X में जन्म लेने वाले में» (PI6 upapajjantānaṃ = जन्म लेने वाला); «नीचे जन्म लेता हुआ वह»
    "upapajjantassa": "जन्म लेने वाला", "upapajjamāno": "जन्म लेता हुआ",
    # «X में जन्म नाम की कोई चीज़ नहीं है»: upapatti = जन्म; the fused upapattināma (6-7-348 slip for
    # «upapatti nāma») = जन्म नाम की … चीज़ («कोई» belongs to natthi)
    "upapatti": "जन्म", "upapattināma": "जन्म नाम की … चीज़",
}
# the mūlaka labels «(X पर आधारित)», «(X से भिन्न लोक पर आधारित)», «(X और Y से भिन्न लोक पर आधारित)»
_R = {"kāma": "इंद्रिय-सुखों के लोक", "rūpa": "सूक्ष्म भौतिक लोक", "arūpa": "अभौतिक लोक"}
for _a, _ha in _R.items():
    T7B[f"{_a}dhātumūlakaṃ"] = f"{_ha} पर आधारित"
    T7B[f"na{_a}dhātumūlakaṃ"] = f"{_ha} से भिन्न लोक पर आधारित"
    for _b, _hb in _R.items():
        if _a != _b:
            T7B[f"na{_a}na{_b}dhātumūlakaṃ"] = f"{_ha} और {_hb} से भिन्न लोक पर आधारित"

assert not set(T7B) & set(T7), sorted(set(T7B) & set(T7))         # follow the shared table, never override it
TABLE = {**TABLE7, **T7B}

# per-segment overrides {file: {bid: {kw: value}}} and presence exceptions {file: {(bid, kw): reason}}: none needed
OVR = {f: {} for f in FILES}
ALLOWED = {f: {} for f in FILES}

if __name__ == "__main__":
    for f in sys.argv[1:] or FILES:
        build_part(f, make_resolver(f, TABLE, OVR[f]))
        verify7(f, allowed=ALLOWED[f])
