"""Build + verify the Hindi keyword maps of 10-bojjhangavibhango, 12-jhanavibhango, 13-appamannavibhango,
14-sikkhapadavibhango (tables: common_10_12_13_14_hi.py + table_12-jhanavibhango_hi.py; tooling:
map_sample_hi.py, read-only).

Presence exceptions = the listed ones (C.ALLOWED) + the values whose only difference from the text is the
-िया ~ -िए / सा ~ से inflection the checker does not model (C.inflect_variant), each printed with its reason.

usage: python -I -X utf8 map_10_12_13_14_hi.py <chapter> [<chapter> ...]
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import build_part, verify, read_hindi, present, NDE, HERE  # noqa: E402
import common_10_12_13_14_hi as C  # noqa: E402

for ch in sys.argv[1:]:
    hi = read_hindi(ch)
    build_part(ch, lambda bid, kw, kws: C.resolve(ch, bid, kw, kws, hi.get(bid)))
    allowed = dict(C.ALLOWED.get(ch, {}))
    for line in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v != NDE and not present(v, hi.get(bid, "")) and (bid, kw) not in allowed:
                why = C.inflect_variant(v, hi.get(bid, ""))
                if why:
                    allowed[(bid, kw)] = why
    verify(ch, show=200, allowed=allowed)
