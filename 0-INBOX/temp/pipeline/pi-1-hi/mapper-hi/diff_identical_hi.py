"""For segments with identical Pāli, show which keyword values differ between parts (and whether the Hindi differs)."""
import collections, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import crosscheck_map_hi as X  # noqa: runs its report too; harmless

ROOT = X.ROOT
HI = ROOT / "AI_translation/hindi/pi-1-hindi-plain-zeroshot_split_chapters"
hseg = {}
for p in X.PARTS:
    buf = []
    for line in (HI / f"{p}.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = X.ID.search(line)
        if m:
            hseg[m.group(1)] = re.sub(r"\[[^\]]*\]", "", X.ID.sub("", " ".join(buf))).strip()
            buf = []
print("\n==== detail")
for t, v in X.diff:
    (p0, s0, b0) = v[0]
    d0 = [q.split("=", 1) for q in b0.split(", ")]
    for p, s, b in v[1:]:
        d = [q.split("=", 1) for q in b.split(", ")]
        m0, m1 = dict(d0), dict(d); dif = [(k, m0[k], m1[k]) for k in m0 if k in m1 and m0[k] != m1[k]]
        if dif:
            same_hi = hseg[s0] == hseg[s]
            print(f"{s0}({p0[:4]}) vs {s}({p[:4]}) hindi-identical={same_hi}: {dif}")
