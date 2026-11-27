"""Check rūpa / Rūpa / rūpaṃ values against the compound of their FIRST occurrence in each Pāli segment."""
import re, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PI = ROOT / "AI_translation/pali/pi-1_split_chapters"
MY = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segments(path):
    out, buf = {}, []
    for l in path.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip(): continue
        buf.append(l)
        m = ID.search(l)
        if m: out[m.group(1)] = " ".join(buf); buf = []
    return out
W = r"[^\s,.;:?!–\-\[\]()‘’“”]*"
res = collections.Counter()
for f in sorted(HERE.glob("*.mapped.md")):
    ch = f.name[:-len(".mapped.md")]
    pa = segments(PI / f"{ch}.md"); my = segments(MY / f"{ch}.md")
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1); sid = sid[1:]
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if k in ("rūpa", "Rūpa"):
                p = pa.get(sid, "")
                words = [re.sub(r"[,.?;:–…]+.*$", "", w) for w in re.findall(r"\S*[rR]ūp\S*", p)]
                if k == "Rūpa":
                    words = [w for w in words if w.startswith("R")]
                else:
                    words = [w for w in words if not re.fullmatch(r"[rR]ūp(aṃ|añca|assa|e|ena|āni|ā|ameva|amhi|aṃ)", w)]
                words = [w for w in words if not re.match(r"\[?[aA]rūp", w)]
                first = words[0] if words else ""
                senses = []
                for w in words:
                    sn = ("FINE" if re.search(r"(?<![aA])[rR]ūpāvacar|[rR]ūpūpapatt|[rR]ūparāg|[rR]ūpabhav|[rR]ūpadhātuy", w) else
                          "VIS" if re.search(r"[rR]ūpāyatan|[rR]ūpadhātu|[rR]ūpārammaṇ|[rR]ūpasañcetan|[rR]ūpasaññā(?!naṃ)|[rR]ūpataṇh|[rR]ūpavitakk|[rR]ūpavicār|viññeyy", w) else
                          "MAT" if re.search(r"[rR]ūpasaṅgah|[rR]ūpakaṇḍ|[rR]ūpavibhatt|[rR]ūpakkhandh|[rR]ūpaj", w) else "?")
                    senses.append((sn, w))
                exp = senses[0] if senses else ("?", "")
                res[(ch[:4], sid if len({x[0] for x in senses}) > 1 else "", k, v, exp[0], exp[1], " ".join(sorted({x[0] for x in senses})))] += 1
for x, c in sorted(res.items()):
    print(*x, c, sep="\t")
