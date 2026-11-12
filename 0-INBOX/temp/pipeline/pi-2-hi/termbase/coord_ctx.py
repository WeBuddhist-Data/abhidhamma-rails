"""Coordinator: for each senses-file key given (hw|i), print its tag, candidates, refs from the pi-2 map, and the Hindi
segment(s) of the first refs (trimmed around the candidate). usage: coord_ctx.py <hw> [<hw> ...] [--n=2] [--w=160]"""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import tb_tool_pi2 as T

opts = {a.split("=")[0]: a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--")}
N, W = int(opts.get("--n", "2")), int(opts.get("--w", "160"))
HI = T.HI.read_text(encoding="utf-8").splitlines()
seg = {}
for l in HI:
    m = re.search(r"\^(\S+)\s*$", l)
    if m:
        seg[m.group(1)] = l
agg = {}
for l in T.AGG.read_text(encoding="utf-8").splitlines():
    hw, _, vals, _ = l.split("\t")
    agg[hw] = vals
ss = dict(T.senses())
for hw in [a for a in sys.argv[1:] if not a.startswith("--")]:
    print(f"## {hw}: {[(t[:50], c) for t, c in ss.get(hw, [])]}")
    vals = agg.get(hw, "")
    print("   map:", vals[:300])
    for item in vals.split(" | "):
        m = T.VAL.match(item)
        if not m:
            continue
        term = m.group(1).split(" … ")[0]
        refs = re.findall(r"[\w-]+", item[item.rfind("[") + 1:])
        for r in refs[:N]:
            s = seg.get(r, "")
            i = s.find(term)
            if i >= 0:
                print(f"   [{r}] …{s[max(0, i - W // 2): i + W // 2]}…")
