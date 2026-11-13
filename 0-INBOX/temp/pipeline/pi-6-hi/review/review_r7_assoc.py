"""Check the sequence of (factor, associated/dissociated/with/without) per line."""
import re, os, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r7_pairs import load
from review_r7_abstract import FILES

F = {'somanassa': 'som', 'upekkhā': 'upe', 'saddhā': 'sad', 'ñāṇa': 'ñāṇ'}
HF = {'प्रसन्नता': 'som', 'समभाव': 'upe', 'श्रद्धा': 'sad', 'ज्ञान': 'ñāṇ'}
pre = re.compile(r'(somanassa|upekkhā|saddhā|ñāṇa)(sampayutt|vippayutt)|(vinā )?(somanassena|upekkhāya)')
hre = re.compile(r'(प्रसन्नता|समभाव|श्रद्धा|ज्ञान) (से जुड़|से अलग|के साथ|के बिना)')
for fn in FILES:
    pl, hl = load(fn)
    for i, (p, h) in enumerate(zip(pl, hl), 1):
        p = unicodedata.normalize('NFC', p).lower()
        ps = []
        for m in pre.finditer(p):
            if m.group(1):
                ps.append((F[m.group(1)], 'S' if m.group(2) == 'sampayutt' else 'V'))
            else:
                ps.append(('som' if m.group(4) == 'somanassena' else 'upe', 'W-' if m.group(3) else 'W+'))
        hs = []
        for m in hre.finditer(h):
            r = {'से जुड़': 'S', 'से अलग': 'V', 'के साथ': 'W+', 'के बिना': 'W-'}[m.group(2)]
            hs.append((HF[m.group(1)], r))
        if ps != hs:
            print(fn[:5], i, ps, hs)
