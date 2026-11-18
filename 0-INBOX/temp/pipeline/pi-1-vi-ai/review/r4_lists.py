import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r4_lib import *

# Compare synonym-string item counts: Pali "Yo/Yā/Yaṃ [evarūpo..] w w w – ayaṃ/idaṃ vuccati"
# vs Vietnamese "Điều mà [thuộc loại như vậy] là a, b, c – đó được gọi"
PSTR = re.compile(r'(?:^|[.?;:’”]\s*|\s)(?:[Yy]o|[Yy]ā|[Yy]aṃ)\s+(?:evarūpo|evarūpā|evarūpaṃ)?\s*(.*?)\s*–\s*(?:ayaṃ|idaṃ|ime|imāni|ayañ)\b')
VSTR = re.compile(r'[Đđ]iều mà(?: thuộc loại như vậy)?(?:, [^,]*,)? là (.*?)\s*–\s*(?:đó|những|các|chúng)')

def pcount(s):
    s = re.sub(r'\[.*?\]', ' ', s)
    s = s.replace('…pe…', ' PE ')
    toks = s.split()
    # attach 'cittassa' and 'kusalamūlaṃ/akusalamūlaṃ' handled as separate items in VI ("tức ...")
    toks = [t for t in toks if t not in ('cittassa',)]
    return len(toks), toks

def vcount(s):
    s = re.sub(r'\s*\[.*?\]', '', s)
    s = s.replace('…', ', PE,')
    items = [x.strip() for x in s.split(',') if x.strip()]
    # "tức gốc rễ ..." appended
    n = len(items) + sum(1 for x in items if ', tức ' in x or x.endswith('tức') or ' tức gốc rễ' in x)
    return n, items

for f in FILES:
    P = segs(os.path.join(PI, f)); V = segs(os.path.join(VI, f))
    for (pid, pl), (vid, vl) in zip(P, V):
        for p, v in zip(pl, vl):
            ps = PSTR.findall(strip_id(p))
            vs = VSTR.findall(strip_id(v))
            if len(ps) != len(vs):
                print(pid, 'NSTR', len(ps), len(vs))
                continue
            for a, b in zip(ps, vs):
                na, ta = pcount(a)
                nb, tb = vcount(b)
                if na != nb:
                    print(pid, 'COUNT', na, nb)
                    print('   P:', ' | '.join(ta))
                    print('   V:', ' | '.join(tb))
