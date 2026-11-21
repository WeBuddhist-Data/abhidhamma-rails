import re, sys
R = 'D:/Work/OpenPecha/abhidhamma-rails/'
PI = R + 'AI_translation/pali/pi-5_split_chapters/'
VI = R + 'AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/'
TS = R + '1-SOURCES/Translations/Vietnamese/vi-5-tinh_su.md'
IDRE = re.compile(r'\s\^(5-[0-9a-z-]+)\s*$')


def segs(path):
    out = {}
    order = []
    cur = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line.strip():
                continue
            m = IDRE.search(line)
            if m:
                cur.append(line[:m.start()])
                out[m.group(1)] = cur
                order.append(m.group(1))
                cur = []
            else:
                cur.append(line)
    return out, order


def main():
    ch = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'ts'
    p, order = segs(PI + ch)
    v, _ = segs(VI + ch)
    t, _ = segs(TS) if mode == 'ts' else ({}, None)
    only = sys.argv[3:] if len(sys.argv) > 3 else None
    for i in order:
        if only and i not in only:
            continue
        print('=' * 20, i)
        if mode == 'ts':
            for l in t.get(i, ['<none>']):
                print('TS:', l)
        elif mode == 'pv':
            for a, b in zip(p[i], v.get(i, [])):
                print('PI:', a)
                print('VI:', b)


main()
