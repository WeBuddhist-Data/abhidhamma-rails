import re
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['1-02-vedanattika.md', '1-03-vipakattika.md', '1-04-upadinnattika.md', '1-05-sankilitthattika.md']
ID_RE = re.compile(r'\s\^([\w-]+)\s*$')
for f in FILES:
    p = [l for l in open(ROOT + '\\pali\\pi-7_split_chapters\\' + f, encoding='utf8').read().split('\n') if l.strip()]
    h = [l for l in open(ROOT + '\\hindi\\pi-7-hindi-plain-rails_split_chapters\\' + f, encoding='utf8').read().split('\n') if l.strip()]
    for k, (ps, hs) in enumerate(zip(p, h), 1):
        out = []
        for m in re.finditer(r'(\S+) अनित्य,', hs):
            if m.group(1) not in ('को', '…'):
                out.append('NO-KO before अनित्य: "%s"' % hs[max(0, m.start() - 30):m.end()])
        # head formula agreement (pañhāvāra)
        m = re.match(r'^(.*?) – ', hs)
        head = m.group(1) if m else hs
        if ' के लिए ' in head and 'कारण के रूप में कारण' in head:
            subj = head.split(',')[0]
            pl_subj = 'परिघटनाएँ' in subj
            if pl_subj and re.search(r'कारण होती है(?!ं)|कारण होता है', head):
                out.append('HEAD AGREEMENT pl-subj sg-verb')
            if not pl_subj and 'परिघटना' in subj and re.search(r'कारण होते हैं|कारण होती हैं|कारण होता है', head):
                out.append('HEAD AGREEMENT sg परिघटना with %s' % re.search(r'कारण हो\S+ है\S*', head).group(0))
            if (' dhammā ' in ps.split('–')[0]) != pl_subj and re.match(r'^\S', ps):
                pass
        # uppajjati head
        if ' उत्पन्न हो' in head and ('uppajjati' in ps.split('–')[0] or 'uppajjanti' in ps.split('–')[0]):
            pu = 'uppajjanti' in ps.split('–')[0]
            hu = bool(re.search(r'उत्पन्न होती हैं|उत्पन्न होते हैं', head))
            if pu != hu:
                out.append('UPPAJJ number P-pl=%s H-pl=%s' % (pu, hu))
        # paccayo vs paccayā number in pañhāvāra head
        ph = ps.split(' – ')[0]
        if re.search(r'paccayena paccay[oā]\b', ph):
            pl = bool(re.search(r'paccayena paccayā\b', ph))
            hpl = bool(re.search(r'कारण होत[ेी] हैं', head))
            if pl != hpl:
                out.append('PACCAYO number P-pl=%s H-pl=%s' % (pl, hpl))
        for o in out:
            mm = ID_RE.search(ps)
            print('%s L%d(%s) %s' % (f[:4], k, mm.group(1) if mm else '', o))
