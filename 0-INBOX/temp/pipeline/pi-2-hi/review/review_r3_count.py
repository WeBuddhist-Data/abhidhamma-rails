import re, sys
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
f = sys.argv[1]
lines = [int(x) for x in sys.argv[2:]]
P = [l for l in open(base + r'\pali\pi-2_split_chapters\\' + f, encoding='utf8').read().split('\n') if l.strip()]
H = [l for l in open(base + r'\hindi\pi-2-hindi-plain-rails_split_chapters\\' + f, encoding='utf8').read().split('\n') if l.strip()]
for n in lines:
    p = re.sub(r'\[[^\]]*\]', '', P[n - 1]); h = re.sub(r'\[[^\]]*\]', '', H[n - 1])
    # take the segment between first 'Yo|Yā|Yaṃ ' and ' – '
    m = re.search(r'\b(?:Yo|Yā|Yaṃ|yo|yā|yaṃ) (.*?) –', p)
    pw = m.group(1).replace('cittassa ', '').replace(' cittassa', '').split() if m else []
    mh = re.search(r'जो (.*?) (?:है|हैं)? ?–', h)
    hw = [x.strip() for x in mh.group(1).split(',')] if mh else []
    print(n, len(pw), len(hw))
    if len(pw) != len(hw):
        for i in range(max(len(pw), len(hw))):
            print('  ', i + 1, pw[i] if i < len(pw) else '-', '|', hw[i] if i < len(hw) else '-')
