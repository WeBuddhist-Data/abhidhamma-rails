import re, sys
# r5 helper: console only. usage:
#  pi1 <pali_regex> [maxhits]     -> aligned pi-1 Pali/Vietnamese lines (snippet around match)
#  ts <id> [<id> ...]             -> print Tinh Su block(s) by root ID (console only)
#  tsgrep <regex>                 -> print Tinh Su lines matching (console only)
#  vi2 <regex>                    -> grep pi-2 Vietnamese split chapters
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
def segs(path):
    txt = open(path, encoding='utf-8').read()
    out = {}
    order = []
    for blk in re.split(r'\n\s*\n', txt):
        lines = [l for l in blk.split('\n') if l.strip()]
        if not lines: continue
        m = re.search(r'\^([0-9][0-9A-Za-z\-]*)\s*$', lines[-1])
        if m:
            out[m.group(1)] = lines; order.append(m.group(1))
    return out, order

mode = sys.argv[1]
if mode == 'pi1':
    pat = re.compile(sys.argv[2]); mx = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    P, order = segs(ROOT + r'\1-SOURCES\Text\pi-1.md')
    V, _ = segs(ROOT + r'\AI_translation\vietnamese\pi-1-vietnamese-plain.md')
    n = 0
    for i in order:
        if i not in V: continue
        for k, l in enumerate(P[i]):
            m = pat.search(l)
            if m:
                vl = V[i][k] if k < len(V[i]) else '(no line)'
                print('==', i, 'line', k, '| P:', l[max(0, m.start()-150):m.end()+250])
                print('   V:', vl[:1200])
                n += 1
                break
        if n >= mx: break
elif mode == 'ts':
    T, _ = segs(ROOT + r'\1-SOURCES\Translations\Vietnamese\vi-2-tinh_su.md')
    for i in sys.argv[2:]:
        print('==', i); print('\n'.join(T.get(i, ['(missing)'])))
elif mode == 'tsl':
    a, b = int(sys.argv[2]), int(sys.argv[3])
    L = open(ROOT + r'\1-SOURCES\Translations\Vietnamese\vi-2-tinh_su.md', encoding='utf-8').read().split('\n')
    for n in range(a - 1, min(b, len(L))):
        if L[n].strip(): print(n + 1, L[n])
elif mode == 'tsgrep':
    pat = re.compile(sys.argv[2])
    for n, l in enumerate(open(ROOT + r'\1-SOURCES\Translations\Vietnamese\vi-2-tinh_su.md', encoding='utf-8')):
        if pat.search(l):
            m = pat.search(l); print(n+1, l[max(0, m.start()-300):m.end()+300].rstrip())
elif mode == 'vi2':
    import glob
    pat = re.compile(sys.argv[2])
    for f in sorted(glob.glob(ROOT + r'\AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\*.md')):
        for n, l in enumerate(open(f, encoding='utf-8')):
            for m in pat.finditer(l):
                print(f.split('\\')[-1], n+1, l[max(0, m.start()-120):m.end()+120].rstrip())
elif mode == 'p2':
    import glob
    pat = re.compile(sys.argv[2])
    for f in sorted(glob.glob(ROOT + r'\AI_translation\pali\pi-2_split_chapters\*.md')):
        for n, l in enumerate(open(f, encoding='utf-8')):
            for m in pat.finditer(l):
                print(f.split('\\')[-1], n+1, l[max(0, m.start()-120):m.end()+120].rstrip())
