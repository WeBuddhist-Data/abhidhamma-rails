"""show_3-03_3-08.py <file> <regex> [max]  -> aligned Pāli / English non-empty lines whose Pāli matches."""
import re, sys, pathlib
R = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
f, rx = sys.argv[1], re.compile(sys.argv[2])
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 40
nl = lambda p: [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
P = nl(R / "pali" / "pi-7_split_chapters" / f)
E = nl(R / "english" / "pi-7-english-plain-zeroshot_split_chapters" / f)
seen, n = set(), 0
for p, e in zip(P, E):
    k = re.sub(r"\s*\^\S+$", "", p)
    if rx.search(p) and k not in seen:
        seen.add(k)
        print("P:", k)
        print("E:", re.sub(r"\s*\^\S+$", "", e))
        n += 1
        if n >= mx:
            break
