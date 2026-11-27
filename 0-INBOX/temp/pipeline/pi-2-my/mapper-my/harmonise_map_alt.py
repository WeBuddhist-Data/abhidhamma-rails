"""For every keyword with more than one value book-wide: each use, and which OTHER values of that keyword would
also pass the shared presence check in that segment (= candidates for alignment). A use where no other value
passes is the text's own wording (REPORT/text) or a sense difference.
usage: python3 -I -X utf8 harmonise_map_alt.py [kw ...]   (prints; no file written)"""
import sys, re, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from presence_check import presence  # noqa: E402
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-2_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segments(path):
    out, buf = {}, []
    for l in path.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip():
            continue
        buf.append(l)
        m = ID.search(l)
        if m:
            out[m.group(1)] = " ".join(buf)
            buf = []
    return out


uses = collections.defaultdict(list)   # kw -> [(ch, sid, v)]
TXT, PAL = {}, {}
for f in sorted(HERE.glob("*.mapped.md")):
    ch = f.name[:-len(".mapped.md")]
    my = segments(MY / f"{ch}.md"); pa = segments(PI / f"{ch}.md")
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1); sid = sid[1:]
        TXT[sid] = my[sid]; PAL[sid] = pa.get(sid, "")
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            uses[k[:1].lower() + k[1:]].append((ch.split("-")[0], sid, v))
want = set(sys.argv[1:])
for k in sorted(uses, key=lambda x: (x.lower(), x)):
    vals = collections.Counter(v for _, _, v in uses[k])
    if len(vals) < 2 or (want and k not in want):
        continue
    out = []
    for v, n in vals.most_common():
        alts = collections.Counter()
        where = []
        for ch, sid, w in uses[k]:
            if w != v:
                continue
            ok = [o for o in vals if o != v and presence(o, TXT[sid])[0]]
            where.append(f"{sid}" + ("{" + "|".join(ok) + "}" if ok else ""))
        out.append(f"   [{n}] {v}: " + " ".join(where[:12]) + (" …" if len(where) > 12 else ""))
    print(f"== {k}")
    print("\n".join(out))
