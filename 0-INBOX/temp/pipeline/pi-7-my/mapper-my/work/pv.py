"""query the pi-1 … pi-6 FINAL Burmese mappings: pv.py kw [kw …] -> per book the value counts (read-only helper)."""
import sys, re, collections, pathlib, pickle
ROOT = pathlib.Path(__file__).resolve().parents[6]
CACHE = pathlib.Path(__file__).resolve().parent / "prior.pickle"
LINE = re.compile(r"^\[([^\]]+)\] (.*)$")
def low(w): return w[:1].lower() + w[1:]
def load():
    if CACHE.exists():
        return pickle.loads(CACHE.read_bytes())
    out = {}
    for t in ("pi-1", "pi-2", "pi-3", "pi-4", "pi-5", "pi-6"):
        d = collections.defaultdict(collections.Counter)
        p = ROOT / f"AI_translation/burmese/{t}-keywords-by-reference-pali-burmese-plain.md"
        for l in p.read_text(encoding="utf-8").splitlines():
            m = LINE.match(l)
            if not m: continue
            for kv in m.group(2).split(", "):
                if "=" in kv:
                    k, v = kv.split("=", 1); d[low(k)][v] += 1
        out[t] = dict(d)
    CACHE.write_bytes(pickle.dumps(out))
    return out
P = load()
for kw in sys.argv[1:]:
    rx = kw.startswith("~")
    for t, d in P.items():
        keys = [k for k in d if re.search(kw[1:], k)] if rx else [low(kw)]
        for k in keys[:30]:
            if k in d:
                print(t, k, d[k].most_common(4))
