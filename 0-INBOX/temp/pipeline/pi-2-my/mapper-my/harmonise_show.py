"""Show the Pāli, the Burmese and the mapped value(s) of a keyword in segments.
usage: python3 -I -X utf8 harmonise_show.py KW SID [SID ...]   (SID without ^; KW '-' = all keywords)"""
import sys, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent
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


def main():
    kw, sids = sys.argv[1], sys.argv[2:]
    for f in sorted(HERE.glob("*.mapped.md")):
        ch = f.name[:-len(".mapped.md")]
        rows = dict(l.split("] ", 1) for l in f.read_text(encoding="utf-8").splitlines())
        rows = {k[1:]: v for k, v in rows.items()}
        hit = [s for s in sids if s in rows]
        if not hit:
            continue
        my = segments(MY / f"{ch}.md"); pa = segments(PI / f"{ch}.md")
        for s in hit:
            print(f"== {s} ({ch})\nPA {pa.get(s)}\nMY {my[s]}")
            vals = [kv for kv in rows[s].split(", ") if kw == "-" or kv.split("=", 1)[0].lower() == kw.lower()]
            print("MAP " + " | ".join(vals))


if __name__ == "__main__":
    main()
