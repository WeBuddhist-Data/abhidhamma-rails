import sys, re
BASE = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
PDIR = BASE + r'\pali\pi-2_split_chapters'
RDIR = BASE + r'\russian\pi-2-russian-plain-rails_split_chapters'
IDRE = re.compile(r'\^([\w-]+)\s*$')


def segs(path):
    txt = open(path, encoding='utf-8').read()
    out = []
    cur = []
    for ln in txt.split('\n'):
        if ln.strip() == '':
            if cur:
                out.append(cur); cur = []
            continue
        cur.append(ln)
    if cur:
        out.append(cur)
    res = []
    for s in out:
        m = IDRE.search(s[-1])
        res.append((m.group(1) if m else None, s))
    return res, txt


def load(ch):
    p, pt = segs(PDIR + '\\' + ch)
    r, rt = segs(RDIR + '\\' + ch)
    return p, r, pt, rt


if __name__ == '__main__':
    ch = sys.argv[1]
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    end = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
    p, r, pt, rt = load(ch)
    print('segs', len(p), len(r))
    for i, ((pid, pl), (rid, rl)) in enumerate(zip(p, r)):
        if i < start or i >= end:
            continue
        print(f'=== [{i}] {pid} | {rid}')
        for j in range(max(len(pl), len(rl))):
            a = pl[j] if j < len(pl) else '<NONE>'
            b = rl[j] if j < len(rl) else '<NONE>'
            print('P:', a)
            print('R:', b)
