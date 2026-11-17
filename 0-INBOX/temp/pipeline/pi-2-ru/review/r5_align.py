import re, sys
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-2_split_chapters\17-khuddakavatthuvibhango.md'
R = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-2-russian-plain-rails_split_chapters\17-khuddakavatthuvibhango.md'
OUT = r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\review\r5_pairs.txt'

def segs(path):
    txt = open(path, encoding='utf-8').read()
    if '\r' in txt:
        print('CR in', path)
    if '\n\n\n' in txt:
        print('double blank in', path)
    lines = txt.split('\n')
    out, cur = [], []
    for ln in lines:
        if ln.strip() == '':
            continue
        cur.append(ln)
        m = re.search(r'\^([0-9a-z-]+)\s*$', ln)
        if m:
            out.append((m.group(1), cur))
            cur = []
    if cur:
        out.append(('TAIL', cur))
    return out

p, r = segs(P), segs(R)
print('segments', len(p), len(r))
with open(OUT, 'w', encoding='utf-8') as f:
    for i, ((pid, pl), (rid, rl)) in enumerate(zip(p, r)):
        flag = ''
        if pid != rid: flag += ' IDMISMATCH'
        if len(pl) != len(rl): flag += ' LINECOUNT'
        f.write(f'=== {pid}{flag}\n')
        for a, b in zip(pl, rl):
            f.write('P: ' + a + '\n')
            f.write('R: ' + b + '\n')
        if flag: print(pid, rid, flag)
