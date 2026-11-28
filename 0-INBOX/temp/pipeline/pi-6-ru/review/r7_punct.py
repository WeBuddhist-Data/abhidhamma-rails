import sys, re
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters\\'
R = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-6-russian-plain-rails_split_chapters\\'
for ch in sys.argv[1:]:
    pl = open(P + ch, encoding='utf-8').read().split('\n')
    rl = open(R + ch, encoding='utf-8').read().split('\n')
    for n, (a, b) in enumerate(zip(pl, rl), 1):
        if not a.strip() or a.startswith('#'):
            continue
        a = re.sub(r'\s*\^[\d-]+$', '', a); b = re.sub(r'\s*\^[\d-]+$', '', b)
        ca, cb = a.count('?'), b.count('?')
        pa, pb = a[-1], b[-1]
        ok = pa == pb or (pa == '.' and pb == '…')
        if ca != cb or not ok or a.lower().count('…pe…') != b.count('…') - b.count('……'):
            print(ch, n, repr(a[-50:]), '|', repr(b[-50:]), ca, cb)
