import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
print(len(p), len(h))
pairs = collections.OrderedDict()
for i, (a, b) in enumerate(zip(p, h)):
    ia = re.search(r'\^(\S+)\s*$', a); ib = re.search(r'\^(\S+)\s*$', b)
    if (ia and ia.group(1)) != (ib and ib.group(1)):
        print('IDMISMATCH', i + 1, a[-30:], '|', b[-30:])
    if a.startswith('#'):
        if not b.startswith('#') or a.split(' ')[0] != b.split(' ')[0]:
            print('HLEVEL', i + 1, a, '|', b)
        ka = re.sub(r'\s*\^\S+$', '', a).lstrip('# ')
        kb = re.sub(r'\s*\^\S+$', '', b).lstrip('# ')
        pairs.setdefault(ka, collections.Counter())[kb] += 1
for k, v in pairs.items():
    flag = '  <<MULTI' if len(v) > 1 else ''
    print(k, '=>', dict(v), flag)
