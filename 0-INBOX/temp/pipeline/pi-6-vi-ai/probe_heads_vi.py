"""Probe: answer heads where a second «ở <person>» follows a comma-chunk; classify the chunk before it
(time phrase / person / other) to find runs of persons that repeat «ở».

usage: python -I -X utf8 -B probe_heads_vi.py [--bak] [--show CLASS] [--parts a,b]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common as V

PERS = re.compile(r", ở ((?:những|chúng sinh|các bậc|bậc|người|tất cả)[^,.;?]*)")
TIME = re.compile(r"^(?:vào |khi |trong đời sống|ngay sau|sau khi|trong khi)")
PERSON = re.compile(r"^(?:ở )?(?:những |chúng sinh|các bậc|bậc |người |tất cả|và những)")


def classify(chunk):
    c = chunk.strip()
    c = re.sub(r"^(?:\. |thì )", "", c)
    lc = c[:1].lower() + c[1:]
    if TIME.match(lc):
        return "time"
    if PERSON.match(lc):
        return "person"
    if re.match(r"^(?:ở |trong cõi|ở cấp độ)", lc):
        return "place"
    return "other"


def main():
    if "--bak" in sys.argv:
        V.CUR["vdir"] = V.BAK
    show = sys.argv[sys.argv.index("--show") + 1] if "--show" in sys.argv else None
    parts = sys.argv[sys.argv.index("--parts") + 1].split(",") if "--parts" in sys.argv else None
    cnt = collections.Counter()
    for part in V.PARTS:
        if parts and V.short(part) not in parts:
            continue
        for sid, ps, vs in V.segments(part):
            for i, v in enumerate(vs):
                for m in PERS.finditer(v):
                    if m.group(1).startswith("những người ấy"):
                        continue
                    before = v[:m.start()]
                    prev = re.split(r"[,.;?]\s*", before)[-1]
                    cls = classify(prev)
                    cnt[(V.short(part), cls)] += 1
                    if show and cls == show:
                        print(f"{V.short(part)}:{sid}.{i} «{prev[-70:]}» , ở «{m.group(1)[:60]}»")
    per = collections.defaultdict(dict)
    for (p, c), n in cnt.items():
        per[p][c] = n
    for p in per:
        print(p, per[p])


if __name__ == "__main__":
    main()
