"""Probe: answer heads (the text before «, thì ở những người ấy» / «, thì ở người ấy») split into comma-chunks;
print heads that contain more than one chunk starting with «ở» / «Ở», with the Pāli head, to check runs of persons.

usage: python -I -X utf8 -B probe_heads2_vi.py [--parts a,b] [--bak] [--max N]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common as V

HEADEND = re.compile(r", thì ở (?:những người ấy|người ấy|chính những)")


def main():
    if "--bak" in sys.argv:
        V.CUR["vdir"] = V.BAK
    parts = sys.argv[sys.argv.index("--parts") + 1].split(",") if "--parts" in sys.argv else None
    mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 50
    seen = collections.Counter()
    n = 0
    for part in V.PARTS:
        if parts and V.short(part) not in parts:
            continue
        for sid, ps, vs in V.segments(part):
            for i, v in enumerate(vs):
                for sent in re.split(r"(?<=[.?])\s+", v):
                    m = HEADEND.search(sent)
                    if not m:
                        continue
                    head = sent[:m.start()]
                    chunks = [c.strip() for c in re.split(r",\s*", head)]
                    o = [c for c in chunks if re.match(r"^(?:Ở|ở) ", c)]
                    if len(o) < 2:
                        continue
                    # skip when every «ở» chunk after the first follows a time chunk
                    bad = []
                    for k, c in enumerate(chunks):
                        if k and re.match(r"^ở ", c):
                            prev = chunks[k - 1]
                            if not re.match(r"^(?:[Vv]ào |khi |[Tt]rong đời sống|[Nn]gay sau|[Tt]rong cõi|Ở cấp độ|[Ss]au khi)", prev) \
                                    and "khoảnh khắc" not in prev and "đang diễn ra" not in prev and "sẽ sinh khởi" not in prev:
                                bad.append(prev + " | " + c)
                    if not bad:
                        continue
                    key = " ‖ ".join(bad)
                    seen[(V.short(part), key)] += 1
    for (p, k), c in sorted(seen.items()):
        n += 1
        if n <= mx:
            print(f"{p} ×{c}: {k[:260]}")
    print("groups", n)


if __name__ == "__main__":
    main()
