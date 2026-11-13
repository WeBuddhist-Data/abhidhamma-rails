"""Check faculty-name sequences and short answers line by line."""
import re, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r7_abstract import rows, p_tokens, h_tokens

ANS = [
    (r'Āmantā\.$', 'हाँ।'),
    (r'\bNo\.$', 'नहीं।'),
    (r'Natthi\.$', 'ऐसा कोई नहीं है।'),
]
for fn, i, pid, pb, hb, ap, ah, extra in rows():
    if pb.startswith('#'):
        continue
    pf = [k for a, b, kind, k in p_tokens(pb) if kind == 'F']
    hf = [k for a, b, kind, k in h_tokens(hb) if kind == 'F']
    if pf != hf:
        print(fn, i, 'FSEQ', pf, hf)
    for pre, hans in ANS:
        if re.search(pre, pb.strip()) and not hb.strip().endswith(hans):
            print(fn, i, 'ANSWER', pb[-20:], '|', hb[-30:])
    if hb.strip().endswith('हाँ।') and not pb.strip().endswith('Āmantā.'):
        print(fn, i, 'ANSWER2', pb[-20:], '|', hb[-30:])
    if hb.strip().endswith('? नहीं।') and not pb.strip().endswith('No.'):
        print(fn, i, 'ANSWER3', pb[-20:], '|', hb[-30:])
