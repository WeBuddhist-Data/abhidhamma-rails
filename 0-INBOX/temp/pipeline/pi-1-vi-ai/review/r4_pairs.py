import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r4_lib import *

# check "A B-ena X ceva Xsampayutto ca" pair sequences vs Vietnamese "A', đối với B', vừa là"
MAP = {
    'lobho': 'sự tham lam', 'doso': 'sự sân hận', 'moho': 'sự si mê', 'māno': 'sự kiêu mạn', 'diṭṭhi': 'quan điểm',
    'vicikicchā': 'sự hoài nghi', 'thinaṃ': 'sự uể oải', 'uddhaccaṃ': 'sự xao động', 'ahirikaṃ': 'sự không biết hổ thẹn',
    'anottappaṃ': 'sự không biết ghê sợ tội lỗi',
}
INSTR = {'mohena': 'moho', 'lobhena': 'lobho', 'dosena': 'doso', 'mānena': 'māno', 'diṭṭhiyā': 'diṭṭhi', 'vicikicchāya': 'vicikicchā',
         'thinena': 'thinaṃ', 'uddhaccena': 'uddhaccaṃ', 'ahirikena': 'ahirikaṃ', 'anottappena': 'anottappaṃ'}
allP, allV = {}, {}
for f in FILES:
    allP.update(seg_dict(os.path.join(PI, f))); allV.update(seg_dict(os.path.join(VI, f)))
for sid in sys.argv[1:]:
    p = strip_id(allP[sid][0]).split('?', 1)[1]
    v = strip_id(allV[sid][0]).split('?', 1)[1]
    pp = re.findall(r'(\w+) (\w+) kileso ceva', p)
    pseq = [(MAP[a.lower()], MAP[INSTR[b]]) for a, b in pp]
    vseq = re.findall(r'(?:^|; )\s*([^;,]+), đối với ([^,]+), vừa là', v)
    vseq = [(a.strip().lower(), b.strip()) for a, b in vseq]
    vseq = [(a[0].lower() + a[1:], b) for a, b in vseq]
    print(sid, len(pseq), len(vseq), pseq == vseq)
    if pseq != vseq:
        for i, (x, y) in enumerate(zip(pseq, vseq)):
            if x != y: print('  ', i, x, y)
