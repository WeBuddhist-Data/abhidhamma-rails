import re,sys
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
for x in d:
    if not x['f'].startswith('4-'): continue
    p=re.sub(r'\[[^\]]*\]','',strip(x['p']));h=re.sub(r'\[[^\]]*\]','',strip(x['h']))
    if not re.search(r'vuccati|dhammā',p): continue
    # take the synonym run: text between the last '?' and ' – '
    pa=p.split('?')[-1] if '?' in p else p; ha=h.split('?')[-1] if '?' in h else h
    pa=re.split(r' – ',pa)[0]; ha=re.split(r' – ',ha)[0]
    # focus on long lists
    pt=[t for t in re.split(r'[\s,]+',pa) if t and t not in('vā','ca','yo','yā','yaṃ','evarūpo','evarūpā','evarūpaṃ','cittassa','kāyassa','mano','pe')]
    hi=[t for t in re.split(r',',ha) if t.strip()]
    if len(pt)>=12:
        diff=len(pt)-len(hi)
        if abs(diff)>=3: print(x['id'] or x['i'],len(pt),len(hi),diff)
