import re, sys, os
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(ROOT, 'pali', 'pi-6_split_chapters')
V = os.path.join(ROOT, 'vietnamese', 'pi-6-vietnamese-plain-rails_split_chapters')
FILES = ['3-06-ayatanayamaka.md', '4-dhatuyamaka.md', '5-01-saccayamaka.md', '5-02-saccayamaka.md',
         '5-03-saccayamaka.md', '6-01-sankharayamaka.md', '6-02-sankharayamaka.md', '7-01-anusayayamaka.md']

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]

def ids(path):
    out = []
    cur = []
    for l in lines(path):
        cur.append(l)
        m = re.search(r'\^([\d-]+)\s*$', l)
        if m:
            out.append((m.group(1), cur)); cur = []
    return out

def pali_stats(s):
    t = s.lower()
    t = re.sub(r'\[[^\]]*\]', '', t)
    toks = re.findall(r"[\wāīūṃṅñṭḍṇḷ]+", t)
    neg = sum(1 for w in toks if w in ('na', 'no', 'natthi', 'nāpi', 'neva', 'nevā', 'nanu', 'nāssa', 'nāssā'))
    neg += sum(1 for w in toks if re.match(r'^(nupp|nirujjh_|nānu|nappa|nābhi|nāsa|nupa|nuppa|nādhi)', w))
    past = sum(1 for w in toks if re.search(r'(ittha|ṃsu)', w))
    fut = sum(1 for w in toks if re.search(r'issa(ti|nti|tī|ntī)', w))
    pres_part = sum(1 for w in toks if w != 'āmantā' and re.search(r'(māna|ant(ānaṃ|assa|aṃ|o|ā)$|samāpann)', w))
    q = s.count('?')
    am = len(re.findall(r'āmantā', t))
    no_ans = len(re.findall(r'(^|[?.]\s*)no\.', t))
    nat = len(re.findall(r'(^|[?.]\s*)natthi\.', t))
    pe = len(re.findall(r'…\s*pe\s*…', t))
    dash = s.count('–')
    return dict(neg=neg, past=past, fut=fut, part=pres_part, q=q, am=am, no=no_ans, nat=nat, pe=pe, dash=dash)

def viet_stats(s):
    t = s.lower()
    t2 = re.sub(r'\[[^\]]*\]', '', t)
    q = s.count('?')
    am = len(re.findall(r'đúng vậy', t2))
    no_ans = len(re.findall(r'(^|[?.]\s*|\)\s*)không\.', t2))
    nat = len(re.findall(r'(^|[?.]\s*|\)\s*)không có\.', t2))
    pe = t2.count('…')
    dash = s.count('–')
    neg = len(re.findall(r'\bkhông\b', t2)) - len(re.findall(r'không\?', t2)) + len(re.findall(r'\bchưa\b', t2))
    past = len(re.findall(r'\bđã\b', t2)) + len(re.findall(r'\bchưa từng\b', t2)) - len(re.findall(r'đã được dứt bỏ|đã chết', t2))
    fut = len(re.findall(r'\bsẽ\b', t2))
    part = len(re.findall(r'\bđang\b', t2))
    return dict(neg=neg, past=past, fut=fut, part=part, q=q, am=am, no=no_ans, nat=nat, pe=pe, dash=dash)

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    sel = sys.argv[2:] if len(sys.argv) > 2 else FILES
    tot = 0
    for fn in sel:
        pl = lines(os.path.join(P, fn)); vl = lines(os.path.join(V, fn))
        if len(pl) != len(vl):
            print('LINECOUNT', fn, len(pl), len(vl))
        for i, (a, b) in enumerate(zip(pl, vl)):
            tot += 1
            ia = re.search(r'\^([\d-]+)\s*$', a); ib = re.search(r'\^([\d-]+)\s*$', b)
            if (ia and ia.group(1)) != (ib and ib.group(1)):
                print('IDMISMATCH', fn, i, a[-20:], '|', b[-20:])
            if a.startswith('#'):
                if mode == 'head':
                    print(fn, '|', a, '|', b)
                continue
            ps, vs = pali_stats(a), viet_stats(b)
            flags = []
            for k in ('q', 'am', 'no', 'nat', 'pe', 'dash'):
                if ps[k] != vs[k]:
                    flags.append('%s:%d/%d' % (k, ps[k], vs[k]))
            if mode in ('all', 'tense'):
                if (ps['fut'] > 0) != (vs['fut'] > 0) or ps['fut'] != vs['fut']:
                    flags.append('fut:%d/%d' % (ps['fut'], vs['fut']))
                if ps['past'] != vs['past']:
                    flags.append('past:%d/%d' % (ps['past'], vs['past']))
                if ps['part'] != vs['part']:
                    flags.append('part:%d/%d' % (ps['part'], vs['part']))
            if mode in ('all', 'neg'):
                if ps['neg'] != vs['neg']:
                    flags.append('neg:%d/%d' % (ps['neg'], vs['neg']))
            if mode == 'struct':
                flags = [f for f in flags if not f.startswith(('neg', 'fut', 'past', 'part'))]
            only = os.environ.get('R2ONLY')
            if only:
                flags = [f for f in flags if f.split(':')[0] in only.split(',')]
            if flags and mode != 'head':
                print('==', fn, 'L%d' % i, ' '.join(flags))
                print('  P:', a)
                print('  V:', b)
    print('lines', tot)

main()
