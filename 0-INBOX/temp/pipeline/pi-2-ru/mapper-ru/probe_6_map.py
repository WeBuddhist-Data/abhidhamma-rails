"""Chapter 6 mapper helper. usage:
  python -I -X utf8 probe_6_map.py heads [N]          first N chars of each segment's Russian (default 300)
  python -I -X utf8 probe_6_map.py seg ID [ID ...]     Pāli + Russian + keywords of segments
  python -I -X utf8 probe_6_map.py grep REGEX          Russian lines (any segment) matching REGEX, with segment id
  python -I -X utf8 probe_6_map.py kw KW [KW ...]      segments containing keyword(s)
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi2_ru import read_keywords, read_pali, read_russian  # noqa: E402

PART = "6-paticcasamuppadavibhango"
ru, pi = read_russian(PART), read_pali(PART)
kws = dict(read_keywords(PART))
cmd, args = sys.argv[1], sys.argv[2:]
if cmd == "heads":
    n = int(args[0]) if args else 300
    for bid in kws:
        print(f"[{bid}] {ru.get(bid, '')[:n]!r}")
elif cmd == "seg":
    for bid in args:
        print(f"=== {bid} PALI\n{pi.get(bid)}\n=== {bid} RU\n{ru.get(bid)}\n=== {bid} KW\n{', '.join(kws.get(bid, []))}\n")
elif cmd == "grep":
    rx = re.compile(args[0])
    for bid, t in ru.items():
        for line in re.split(r"(?<=[.?])\s+", t):
            if rx.search(line):
                print(f"[{bid}] {line}")
elif cmd == "kw":
    for bid, ks in kws.items():
        if any(a in ks for a in args):
            print(bid, [a for a in args if a in ks])
