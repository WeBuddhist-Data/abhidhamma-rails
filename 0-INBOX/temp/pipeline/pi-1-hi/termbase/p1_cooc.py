"""Part-1 helper: segments of the pi-1 Pāli→Hindi keyword map where keys matching ALL given regexes co-occur.

usage: python -I -X utf8 p1_cooc.py <regexA> <regexB> [...] [--max N]
Prints ref and the matching key=hindi pairs (keys matched case-insensitively with re.fullmatch).
"""
import pathlib, re, sys

KW = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-keywords-by-reference-pali-hindi-plain.md")


def main(a):
    mx = 15
    if "--max" in a:
        i = a.index("--max")
        mx = int(a[i + 1])
        a = a[:i] + a[i + 2:]
    rxs = [re.compile(r, re.I) for r in a]
    n = 0
    for line in KW.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\[([^\]]*)\]\s*(.*)$", line)
        if not m:
            continue
        ref, body = m.groups()
        pairs = [p.split("=", 1) for p in body.split(", ") if "=" in p]
        hits = [[(k, v) for k, v in pairs if rx.fullmatch(k)] for rx in rxs]
        if all(hits):
            n += 1
            if n <= mx:
                print(ref, " | ".join(f"{k}={v}" for h in hits for k, v in h))
    print(f"segments: {n}")


if __name__ == "__main__":
    main(sys.argv[1:])
