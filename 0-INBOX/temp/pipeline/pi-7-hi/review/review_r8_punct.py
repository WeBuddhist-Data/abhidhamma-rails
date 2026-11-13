import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
def tail(s):
    s = re.sub(r'\s*\^\S+\s*$', '', s).rstrip()
    s = re.sub(r'(\s*\(\d+\))+$', '', s).rstrip()
    return s
c = collections.Counter(); ex = collections.defaultdict(list)
for i, (a, b) in enumerate(zip(p, h)):
    if a.startswith('#'):
        continue
    ta, tb = tail(a), tail(b)
    k = (ta[-2:], tb[-2:])
    c[k] += 1
    ex[k].append(i + 1)
    # sentence-internal: count of '. ' in Pali vs '। ' in Hindi
    na = len(re.findall(r'[a-zāīūṃṅñṭḍṇḷ…)]\.(\s|$|\))', a)); nb = len(re.findall(r'[।?]', b))
    if na != nb:
        c[('SENT', '')] += 1; ex[('SENT', '')].append(f'{i+1}:{na}/{nb}')
for k, v in c.most_common():
    print(k, v, ex[k][:25])
