"""Probe (writes nothing): split every chapter-18 Pāli line into sentences and look each one up in a sentence map
built from the approved pi-1 rails and the finished pi-2 rails chapters 1-17 (only lines whose Pāli and Vietnamese
have the same number of sentences). Prints HIT / MISS per sentence.

usage: python -I -X utf8 probe_18.py [from_line to_line]      (non-empty line numbers of chapter 18, 1-based)
"""
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import find_18_vi as F  # noqa: E402

SPL = re.compile(r"(?<=[.?!])\s+")
IDRX = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def key(s):
    s = IDRX.sub("", s).strip()
    s = s.replace('"', "").replace("“", "").replace("”", "").replace(" – ", " ").replace("ti pi", "tipi")
    s = re.sub(r"\s+", " ", s)
    return s[:1].lower() + s[1:]


def build_map():
    m = {}
    for tag, pa_dir, vi_dir, names in F.PAIRS:
        for n in names:
            pa, vi = F.nonempty(pa_dir / n), F.nonempty(vi_dir / n)
            for p, v in zip(pa, vi):
                ps, vs = SPL.split(IDRX.sub("", p).strip()), SPL.split(IDRX.sub("", v).strip())
                if len(ps) != len(vs):
                    continue
                for a, b in zip(ps, vs):
                    m.setdefault(key(a), (tag + "/" + n, b))
    return m


def main():
    m = build_map()
    lines = F.nonempty(F.ROOT / "AI_translation" / "pali" / "pi-2_split_chapters" / "18-dhammahadayavibhango.md")
    a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (1, len(lines))
    hits = miss = 0
    for i in range(a - 1, min(b, len(lines))):
        print(f"--- L{i + 1}")
        for s in SPL.split(IDRX.sub("", lines[i]).strip()):
            r = m.get(key(s))
            if r:
                hits += 1
                print(f"  HIT [{r[0]}] {s[:70]} => {r[1]}")
            else:
                miss += 1
                print(f"  MISS {s}")
    print(f"# hits {hits}, misses {miss}")


if __name__ == "__main__":
    main()
