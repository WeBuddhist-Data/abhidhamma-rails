import sys, re
from collections import OrderedDict
sys.path.insert(0, 'D:/Work/OpenPecha/abhidhamma-rails/0-INBOX/temp/pipeline/pi-6-vi-ai/review')
from r1_check import load, PDIR, VDIR

TS = 'D:/Work/OpenPecha/abhidhamma-rails/1-SOURCES/Translations/Vietnamese/vi-6-tinh_su.md'
IDRE = re.compile(r'\s\^([0-9A-Za-z-]+)\s*$')


def load_ts():
    segs = OrderedDict()
    cur = []
    for ln in open(TS, encoding='utf-8').read().split('\n'):
        s = ln.strip()
        if not s or s.startswith('![[') or s.startswith('---'):
            continue
        cur.append(s)
        m = IDRE.search(s)
        if m:
            segs[m.group(1)] = cur
            cur = []
    return segs


if __name__ == '__main__':
    # console only: r1_ts.py file id id ...
    f = sys.argv[1]
    P, _ = load(PDIR + f)
    V, _ = load(VDIR + f)
    T = load_ts()
    for sid in sys.argv[2:]:
        print('##', sid)
        for x in P.get(sid, []):
            print('P  ' + x)
        for x in V.get(sid, []):
            print('V  ' + x)
        for x in T.get(sid, ['<missing>']):
            print('TS ' + x)
