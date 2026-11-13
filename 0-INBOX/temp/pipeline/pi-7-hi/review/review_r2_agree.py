import re
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['1-02-vedanattika.md', '1-03-vipakattika.md', '1-04-upadinnattika.md', '1-05-sankilitthattika.md']
ID_RE = re.compile(r'\s\^([\w-]+)\s*$')
# sentence-level agreement heuristics on the Hindi, compared with the Pāli clause predicate number
SG_SUBJ = ['भोजन', 'इरादा', 'एक समूह', 'आधार', 'इंद्रिय-क्षेत्र', 'जीवन-क्षमता', 'प्रधानता', 'मन को विषय की ओर मोड़ना',
           'जीवन-धारा', 'निर्वाण', 'मार्ग', 'फल', 'अनुरूपता']
for f in FILES:
    p = [l for l in open(ROOT + '\\pali\\pi-7_split_chapters\\' + f, encoding='utf8').read().split('\n') if l.strip()]
    h = [l for l in open(ROOT + '\\hindi\\pi-7-hindi-plain-rails_split_chapters\\' + f, encoding='utf8').read().split('\n') if l.strip()]
    for k, (ps, hs) in enumerate(zip(p, h), 1):
        mm = ID_RE.search(ps)
        tag = '%s L%d(%s)' % (f[:4], k, mm.group(1) if mm else '')
        for sent in re.split(r'[।;]|…', ID_RE.sub('', hs)):
            s = sent.strip()
            if not s:
                continue
            if 'कारण होते हैं' in s or 'कारण होती हैं' in s:
                head = s.split(' के लिए')[0]
                plural_markers = (' और ' in head or 'समूह ' in head or s.startswith('दो ') or s.startswith('तीन ')
                                  or 'मूल ' in head or 'आहार ' in head or 'क्षमताएँ' in head or 'अंग ' in head
                                  or 'परिघटनाएँ' in head or 'महाभूत ' in head)
                if 'भोजन' in head and ' और ' not in head.split('भोजन')[0][-60:]:
                    print(tag, 'SG भोजन + PL verb:', s[:160])
                elif not plural_markers:
                    print(tag, 'PL verb, no plural subject seen:', s[:160])
