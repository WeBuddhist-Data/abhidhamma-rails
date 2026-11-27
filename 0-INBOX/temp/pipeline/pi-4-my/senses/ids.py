"""List every Burmese value of a Pāli headword with all its segment ids. usage: ids.py hw [hw ...]"""
import sys, re, collections, pathlib
M = pathlib.Path(__file__).resolve().parents[5] / "AI_translation/burmese/pi-4-keywords-by-reference-pali-burmese-plain.md"
for hw in sys.argv[1:]:
    d = collections.defaultdict(list)
    for l in M.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\[([^\]]+)\] (.*)", l)
        if not m: continue
        for p in m.group(2).split(", "):
            k, _, v = p.partition("=")
            if k.lower() == hw.lower(): d[v].append(m.group(1))
    print(hw, {v: ids for v, ids in d.items()})
