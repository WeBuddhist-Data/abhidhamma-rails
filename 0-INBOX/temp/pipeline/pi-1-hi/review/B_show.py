import re,sys
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
ids=set(sys.argv[1].split(','))
w=int(sys.argv[2]) if len(sys.argv)>2 else 10**6
for x in d:
    if x['id'] in ids:
        print('[%s]'%x['id']); print('P',strip(x['p'])[:w]); print('H',strip(x['h'])[:w])
