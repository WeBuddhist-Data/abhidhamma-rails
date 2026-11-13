import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load
p, h, ids = load()
L = r'a-zāīūṃṅñṭḍṇḷ'
PU = re.compile(r'([A-ZĀ][' + L + r' ]*?) dhammaṃ (?:paṭicca|paccayā|saṃsaṭṭho|sampayutto) ([' + L + r' ]+?) dhamm(o|ā) uppajja(?:ti|nti)')
PP = re.compile(r'([A-ZĀ][' + L + r' ]*?) dhamm(o|ā) ([' + L + r' ]+?) dhammassa ')
HUv = re.compile(r'उत्पन्न होती (हैं|है)')
HPv = re.compile(r'परिघटना(?:ओं)? के लिए [^।;–?]*?कारण (?:होती|नहीं होती) (हैं|है)')
bad = []
for i, (a, b) in enumerate(zip(p, h)):
    if a.startswith('#'):
        continue
    pu = [m.group(3) == 'ā' for m in PU.finditer(a)]
    hu = [m.group(1) == 'हैं' for m in HUv.finditer(b)]
    pp = [m.group(2) == 'ā' for m in PP.finditer(a)]
    hp = [m.group(1) == 'हैं' for m in HPv.finditer(b)]
    if pu and pu != hu[:len(pu)]:
        bad.append(('U', i + 1, pu, hu))
    if pp and pp != hp[:len(pp)]:
        bad.append(('P', i + 1, pp, hp))
    # follow-on abbreviated verbs: '… X-कारण के रूप में कारण होती है/हैं' must match head number in a pañhā line
    if pp and len(pp) == 1:
        vs = re.findall(r'के रूप में कारण (?:नहीं )?होती (हैं|है)', b)
        heads_pl = pp[0]
        # only check verbs belonging to abbreviated chains (after '…')
        chain = re.findall(r'…\s*[^।;–…()]*?-कारण के रूप में कारण (?:नहीं )?होती (हैं|है)', b)
        for v in chain:
            if (v == 'हैं') != heads_pl:
                bad.append(('chain', i + 1, pp, chain)); break
    # plural noun with singular verb inside Hindi U-head
    for m in re.finditer(r'परिघटनाएँ [^।;–]*?उत्पन्न होती (हैं|है)', b):
        if m.group(1) == 'है':
            bad.append(('HUpl', i + 1, m.group(0)[-60:]))
for x in bad:
    print(x)
print(len(bad))

