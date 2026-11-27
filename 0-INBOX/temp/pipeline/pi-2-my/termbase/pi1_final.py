"""Count how many pi-2 termbase senses carry pi-1's locked term (same headword, same sense: exact tag, a tag that
extends pi-1's, or the only sense of both) and list those that differ. usage: pi1_final.py"""
import pathlib, collections
B = pathlib.Path(__file__).resolve().parents[5]
def parse(p):
    d = {}
    for l in p.read_text(encoding='utf-8').splitlines():
        h, b = l.split(': {', 1); d[h] = [tuple(s.rsplit(': ', 1)) for s in b[:-1].split('; ')]
    return d
t1 = parse(B / 'AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md')
t2 = parse(B / 'AI_translation/burmese/pi-2-pali-burmese-termbase-plain.md')
low = collections.defaultdict(list)
for h in t1: low[h.lower()].append(h)
same, diff, total = 0, [], 0
for h, ss in t2.items():
    for i, (tag, tm) in enumerate(ss):
        total += 1; m = None
        for h1 in [h] + [x for x in low.get(h.lower(), []) if x != h]:
            for j, (tg, t) in enumerate(t1.get(h1, [])):
                if tg == tag or tg[:35] == tag[:35]: m = (h1, j, t); break
            if m: break
        if not m and h in t1 and len(t1[h]) == 1 and len(ss) == 1: m = (h, 0, t1[h][0][1])
        if not m: continue
        if m[2] == tm: same += 1
        else: diff.append(f"{h}|{i}: pi-2 {tm}  | pi-1 {m[2]}  [{tag[:60]}]")
print(f"senses {total}; with a pi-1 entry for the same headword and sense {same + len(diff)}; pi-1 term taken {same}; differ {len(diff)}")
print("\n".join(diff))
