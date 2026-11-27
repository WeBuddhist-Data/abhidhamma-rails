"""For each keyword given: every value, its segments, and one Pāli + Burmese context per (chapter, value).
usage: harmonise_kw.py KW [KW ...]"""
import re, sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-1_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segments(path):
    out, buf = {}, []
    for l in path.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip(): continue
        buf.append(l)
        m = ID.search(l)
        if m: out[m.group(1)] = " ".join(buf); buf = []
    return out
cache = {}
def segs(ch):
    if ch not in cache: cache[ch] = (segments(PI / f"{ch}.md"), segments(MY / f"{ch}.md"))
    return cache[ch]
for kw in sys.argv[1:]:
    low = kw[:1].lower() + kw[1:]
    found = collections.defaultdict(list)
    for f in sorted(HERE.glob("*.mapped.md")):
        ch = f.name[:-len(".mapped.md")]
        for l in f.read_text(encoding="utf-8").splitlines():
            sid, rest = l.split("] ", 1); sid = sid[1:]
            for kv in rest.split(", "):
                k, v = kv.split("=", 1)
                if k[:1].lower() + k[1:] == low:
                    found[(v, ch)].append((sid, k))
    print(f"######## {kw}")
    for (v, ch), sids in sorted(found.items(), key=lambda x: (x[0][0], x[0][1])):
        pa, my = segs(ch)
        sid, k = sids[0]
        p = pa.get(sid, ""); t = my[sid]
        i = p.find(k); pc = p[max(0, i - 50): i + len(k) + 50] if i >= 0 else p[:100]
        st = re.sub(r"(သည်|သော)$", "", v.split(" … ")[0].split(" / ")[0])
        j = t.find(st); mc = t[max(0, j - 40): j + len(st) + 40] if j >= 0 else "(not found)"
        print(f"  [{v}] {ch[:4]} n={len(sids)} {[s for s, _ in sids[:6]]}\n     PI «{pc}»\n     MY «{mc}»")
