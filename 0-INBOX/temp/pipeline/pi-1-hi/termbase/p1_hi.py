"""Part-1 helper: which Pāli keys map to a given Hindi value in the pi-1 keyword map, and where two such keys share a segment.

usage: python -I -X utf8 p1_hi.py <hindi-regex>
Lists key -> value counts (value matched with re.fullmatch), then segments where 2+ distinct keys with such values co-occur.
"""
import collections, pathlib, re, sys

KW = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-keywords-by-reference-pali-hindi-plain.md")


def main(a):
    rx = re.compile(a[0])
    cnt = collections.Counter()
    co = []
    for line in KW.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\[([^\]]*)\]\s*(.*)$", line)
        if not m:
            continue
        ref, body = m.groups()
        pairs = [p.split("=", 1) for p in body.split(", ") if "=" in p]
        hits = [(k, v) for k, v in pairs if rx.fullmatch(v)]
        for k, v in hits:
            cnt[(k, v)] += 1
        if len({k.lower() for k, _ in hits}) > 1:
            co.append((ref, hits))
    for (k, v), n in cnt.most_common():
        print(f"{k}\t{v}\t{n}")
    print(f"--- co-occurring segments: {len(co)}")
    for ref, h in co[:20]:
        print(ref, " | ".join(f"{k}={v}" for k, v in h))


if __name__ == "__main__":
    main(sys.argv[1:])
