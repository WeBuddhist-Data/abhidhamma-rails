import re,sys
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
f=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
for x in d:
    if x['f'].startswith(f) and a<=x['i']<=b:
        print('[%s %s]'%(x['i'],x['id'] or ''))
        print('P',strip(x['p']))
        print('H',strip(x['h']))
