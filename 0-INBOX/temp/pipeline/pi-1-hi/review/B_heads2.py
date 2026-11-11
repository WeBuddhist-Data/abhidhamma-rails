import re,sys,collections
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
pm=[l for l in lines(os.path.join(P,'1-matika.md')) if l.strip()]
hm=[l for l in lines(os.path.join(H,'1-matika.md')) if l.strip()]
M={}
order=[]
def pre(s):
    return re.sub(r'^\([^)]*\)\s*','',s)
for a,b in zip(pm,hm):
    a=strip(a);b=strip(b)
    if a.startswith('#'): continue
    a=pre(re.sub(r'\[[^\]]*\]','',a)).strip(); b=pre(re.sub(r'\[[^\]]*\]','',b)).strip()
    if a.lower().endswith('dhammā.') or a.lower().endswith('dhammā') :
        k=a.lower().rstrip('.').replace(' dhammā','').strip()
        M[k]=b.rstrip('।').strip()
        order.append(k)
print('matrix items',len(M))
def nh(h):
    h=re.sub(r'कौन-सी हैं$','',h).strip()
    return h
def norm(s):
    s=s.replace('परिघटनाएँ','').replace('  ',' ').strip(' ,।')
    return s
miss=0;seen=collections.Counter();diff=[]
for x in d:
    if not x['f'].startswith(('4-','5-')): continue
    p=strip(x['p'])
    m=re.match(r'Katame dhammā\s+(.*?)\?',p)
    if not m: continue
    k=m.group(1).strip().lower()
    h=norm(nh(strip(x['h']).split('?')[0]))
    if k in M:
        seen[k]+=1
        mm=norm(M[k])
        if mm!=h: diff.append((x['id'],k,h,mm))
    else:
        miss+=1
        print('NOTM',x['id'],k,'|',h[:80])
print('miss',miss,'matched',sum(seen.values()),'distinct',len(seen))
print('matrix items not seen as heads:',[k for k in order if k not in seen][:80])
for t in diff: print('DIFF',t[0],t[1],'|H:',t[2][:90],'|M:',t[3][:90])
