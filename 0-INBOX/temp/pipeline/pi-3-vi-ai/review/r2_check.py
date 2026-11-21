# r2 helper: per-segment count / polarity / list-length / typography check, Pali vs our Vietnamese (console only).
import re, sys, os
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-3_split_chapters'
V = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters'
CH = ['3-dutiyanayo', '4-tatiyanayo', '5-catutthanayo', '6-pancamanayo', '7-chatthanayo']

PN = {'ekena': 1, 'ekāya': 1, 'eken': 1, 'ekāy': 1, 'dvīh': 2, 'tīh': 3, 'catūh': 4, 'pañcah': 5, 'chah': 6, 'sattah': 7, 'aṭṭhah': 8,
      'navah': 9, 'dasah': 10, 'ekādasah': 11, 'dvādasah': 12, 'pannarasah': 15, 'soḷasah': 16, 'sattarasah': 17}
VNN = {'một': 1, 'hai': 2, 'ba': 3, 'bốn': 4, 'năm': 5, 'sáu': 6, 'bảy': 7, 'tám': 8, 'chín': 9, 'mười': 10,
       'mười một': 11, 'mười hai': 12, 'mười lăm': 15, 'mười sáu': 16, 'mười bảy': 17}

def segs(path):
    t = open(path, encoding='utf-8').read()
    out = []
    buf = []
    for line in t.split('\n'):
        if line.strip():
            buf.append(line)
        m = re.search(r'\^(3-[0-9-]+)\s*$', line)
        if m:
            out.append((m.group(1), buf))
            buf = []
    return out

def pali_counts(s):
    res = []
    for m in re.finditer(r'(\w+?)(?:i khandhehi| khandhena|āyatanehi|āyatanena|i dhātūhi| dhātuyā)', s):
        w = m.group(1)
        kind = 'K' if 'khandh' in m.group(0) else ('A' if 'āyatan' in m.group(0) else 'D')
        if w in ('kat', 'katih', 'katihi', 'kehic', 'ekenāyatanena'):
            continue
        key = None
        for k in sorted(PN, key=len, reverse=True):
            if w.endswith(k) or w == k:
                key = k; break
        # handle '...hāyatanehi' forms: e.g. dvīhāyatanehi -> w='dvīh'
        if key is None:
            continue
        res.append((kind, PN[key]))
    return res

def viet_counts(s):
    res = []
    s2 = s.replace('một số hiện tượng thuộc ', '')
    for m in re.finditer(r'(mười một|mười hai|mười lăm|mười sáu|mười bảy|mười|một|hai|ba|bốn|năm|sáu|bảy|tám|chín) (khối|lĩnh vực nhận biết|yếu tố)(?! (?:thức|ý|mắt|tai|mũi|lưỡi|thân|vật|đối))', s2):
        kind = {'khối': 'K', 'lĩnh vực nhận biết': 'A', 'yếu tố': 'D'}[m.group(2)]
        res.append((kind, VNN[m.group(1)]))
    return res

LATIN = re.compile(r'[A-Za-zāīūṃṅñṭḍṇḷ]*[āīūṃṅñṭḍṇḷ][A-Za-zāīūṃṅñṭḍṇḷ]*')
tot = 0
for ch in CH:
    ps = segs(os.path.join(P, ch + '.md'))
    vs = segs(os.path.join(V, ch + '.md'))
    if [i for i, _ in ps] != [i for i, _ in vs]:
        print(ch, 'ID MISMATCH')
    for (pid, pl), (vid, vl) in zip(ps, vs):
        tot += 1
        if len(pl) != len(vl):
            print(ch, pid, 'LINES', len(pl), len(vl))
        p = ' '.join(pl); v = ' '.join(vl)
        # strip variant brackets for count/latin
        pb = re.sub(r'\[[^\]]*\]', '', p); vb = re.sub(r'\[[^\]]*\]', '', v)
        # prose only: drop verse lines (after the last '?'-answer line) for count checks
        if len(pl) > 1:
            pb = re.sub(r'\[[^\]]*\]', '', pl[0]); vb = re.sub(r'\[[^\]]*\]', '', vl[0])
        pb = pb.replace('Na kehici', 'na kehici').replace('Catūhi', 'catūhi').replace('Ekena', 'ekena').replace('Dvīhi', 'dvīhi').replace('Tīhi', 'tīhi')
        vb = re.sub(r'gồm (một|bốn|năm) khối', 'gồm X', vb).replace('sáu lĩnh vực nhận biết làm', 'X làm').replace('cho sáu lĩnh vực nhận biết', 'cho X')
        pc = pali_counts(pb); vc = viet_counts(vb)
        # drop question words
        if pc != vc:
            print(ch, pid, 'COUNTS P', pc, 'V', vc)
        # kehici
        nk_p = len(re.findall(r'\bkehici\b', pb)) - len(re.findall(r'na kehici', pb))
        nk_v = len(re.findall(r'một số hiện tượng thuộc', vb))
        if nk_p != nk_v:
            print(ch, pid, 'KEHICI', nk_p, nk_v)
        nn_p = len(re.findall(r'na kehici', pb)) - (1 if 'na kehici khandhehi ekenāyatanena' in pb else 0); nn_v = len(re.findall(r'[Kk]hông có (khối|lĩnh vực nhận biết) nào', vb)) + len(re.findall(r'không được gộp vào khối nào', vb))
        if nn_p != nn_v:
            print(ch, pid, 'NA-KEHICI', nn_p, nn_v)
        # natthi
        if pb.count('Natthi') != vb.count('Không có.'):
            print(ch, pid, 'NATTHI', pb.count('Natthi'), vb.count('Không có.'))
        # sampayutta / vippayutta counts
        sp = len(re.findall(r'\bsampayutt', pb)) - len(re.findall(r'(vedanāya|hetu|āsava|citta|kilesa|parāmāsa)sampayutt|vedanāya sampayutt', pb))
        # ellipsis counts
        pe_p = len(re.findall(r'…', pb)) - len(re.findall(r'…pe…', pb))
        pe_v = len(re.findall(r'…', vb))
        if pe_p != pe_v:
            print(ch, pid, 'ELLIPSIS', pe_p, pe_v)
        # typography
        for bad in ['….', '..', ' ,', ' .', ' ?', ' ;', ' :', '"', "'", '—', '–', '  ']:
            if bad in v.replace('^', ''):
                print(ch, pid, 'TYPO', repr(bad))
        lat = [w for w in LATIN.findall(vb) if w]
        if lat:
            print(ch, pid, 'LATIN', lat[:6])
        q_p = p.count('?'); q_v = v.count('?')
        if q_p != q_v:
            print(ch, pid, 'QMARKS', q_p, q_v)
print('segments', tot)
