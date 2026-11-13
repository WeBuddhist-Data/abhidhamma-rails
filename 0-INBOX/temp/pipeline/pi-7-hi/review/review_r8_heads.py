import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
L = r'a-zāīūṃṅñṭḍṇḷ'
PU = re.compile(r'([A-ZĀ][' + L + r' ]*?) dhammaṃ (paṭicca|paccayā|saṃsaṭṭho|sampayutto) ([' + L + r' ]+?) dhamm(?:o|ā) uppajja(?:ti|nti)')
PP = re.compile(r'([A-ZĀ][' + L + r' ]*?) dhamm(?:o|ā) ([' + L + r' ]+?) dhammassa ')
A = r'(?:^|(?<=। )|(?<=\) )|(?<=– )|(?<=\? ))'
HU = re.compile(A + r'([^।;–…()?]+?) परिघटना(?:एँ)? (पर निर्भर होकर|के कारण|से घुल-मिलकर|से जुड़कर|से जुड़ी होकर|[^ ]+ [^ ]+कर) ([^।;–…()?]+?) परिघटना(?:एँ)? [^।;–…()?]*?उत्पन्न होती')
HP = re.compile(A + r'([^।;–…()?]+?) परिघटना(?:एँ)?, ([^।;–…()?]+?) परिघटना(?:ओं)? के लिए')

dyad = None
tabs = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
cnt = collections.Counter()
where = collections.defaultdict(list)
for i, (a, b) in enumerate(zip(p, h)):
    if a.startswith('#') and 'dukaṃ' in a and not a.startswith('#######'):
        dyad = a.split(' ')[1]
        continue
    if a.startswith('#'):
        continue
    pu = PU.findall(a); pp = PP.findall(a)
    hu = HU.findall(b); hp = HP.findall(b)
    if len(pu) != len(hu) or len(pp) != len(hp):
        cnt['countmismatch'] += 1
        print('COUNT', i + 1, len(pu), len(hu), len(pp), len(hp))
        continue
    for (s, v, o), (hs, hv, ho) in zip(pu, hu):
        tabs[dyad]['U-subj'][(s.lower(), hs)] += 1
        tabs[dyad]['U-verb'][(v, hv)] += 1
        tabs[dyad]['U-obj'][(o, ho)] += 1
        where[(dyad, 'U-subj', s.lower(), hs)].append(i + 1)
        where[(dyad, 'U-obj', o, ho)].append(i + 1)
    for (s, o), (hs, ho) in zip(pp, hp):
        tabs[dyad]['P-subj'][(s.lower(), hs)] += 1
        tabs[dyad]['P-obj'][(o, ho)] += 1
        where[(dyad, 'P-subj', s.lower(), hs)].append(i + 1)
        where[(dyad, 'P-obj', o, ho)].append(i + 1)
for d, t in tabs.items():
    print('#####', d)
    for k, c in t.items():
        byp = collections.defaultdict(list)
        for (x, y), n in c.items():
            byp[x].append((y, n))
        for x, ys in byp.items():
            mark = ' <<<MULTI' if len(ys) > 1 else ''
            for y, n in ys:
                extra = ''
                if mark:
                    extra = ' lines=' + ','.join(map(str, where[(d, k, x, y)][:8]))
                print(f'  {k}: {x} => {y} [{n}]{mark}{extra}')
