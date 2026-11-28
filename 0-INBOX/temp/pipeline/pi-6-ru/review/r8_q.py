"""r8: question-frame check (yassa / yattha / yassa yattha / yo ... tassa / tattha / so) and labels (Ka)/(Kha), vā pana."""
import re, sys
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\review')
from r8_check import FILES, load

def pframe(q):
    global vp_flag
    vp_flag = 'vā pana' in q
    q = q.lower().replace('vā pana ', '')
    vp0 = True
    lab = re.match(r'\((ka|kha)\)', q)
    lab = lab.group(1) if lab else '-'
    vp = vp_flag
    m = re.search(r'\b(yassa yattha|yassa|yattha|yo)\b', q)
    rel = m.group(1) if m else '?'
    m2 = re.search(r'\b(tassa tattha|tassa|tattha|so)\b', q)
    cor = m2.group(1) if m2 else '?'
    return lab, vp, rel, cor

def rframe(q):
    lab = re.match(r'\((а|б)\)', q)
    lab = {'а': 'ka', 'б': 'kha'}[lab.group(1)] if lab else '-'
    vp = bool(re.match(r'(\(б\) )?А ', q))
    ql = q.lower()
    if re.search(r'у кого где', ql): rel = 'yassa yattha'
    elif re.search(r'у кого', ql): rel = 'yassa'
    elif re.search(r'(^|\) |а )где', ql): rel = 'yattha'
    elif re.search(r'(^|\) |а )кто', ql): rel = 'yo'
    else: rel = '?'
    if re.search(r'у того там', ql): cor = 'tassa tattha'
    elif 'у того' in ql: cor = 'tassa'
    elif re.search(r', там ', ql): cor = 'tattha'
    elif ', тот ' in ql: cor = 'so'
    else: cor = '?'
    return lab, vp, rel, cor

bad = 0; n = 0
for f in FILES:
    p, r = load(f)
    for i, (a, b) in enumerate(zip(p, r)):
        ps = re.findall(r'(?:^|(?<=[.?] ))((?:\(\w+\) )?(?:[Yy]assa|[Yy]attha|[Yy]o) [^?]*\?)', a)
        rs = re.findall(r'(?:^|(?<=[.?] ))((?:\([аб]\) )?(?:А )?(?:У кого|Где|Кто|у кого|где|кто) [^?]*\?)', b)
        if not ps and not rs: continue
        if len(ps) != len(rs):
            print('QCOUNT', f, i + 1, len(ps), len(rs)); bad += 1; continue
        for x, y in zip(ps, rs):
            n += 1
            fx, fy = pframe(x), rframe(y)
            if fx != fy:
                bad += 1; print('FRAME', f, i + 1, fx, fy, '|', x[:70], '|', y[:70])
print('questions', n, 'flags', bad)
