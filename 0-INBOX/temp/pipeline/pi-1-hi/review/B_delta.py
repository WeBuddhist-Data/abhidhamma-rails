import re,sys,difflib
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
out=open(r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review\B_delta.txt','w',encoding='utf-8')
THR=0.55
hist=[]  # (ptoks,htoks,label)
def fmt(a,b):
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    parts=[]
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=='equal':
            n=i2-i1
            if n<=4: parts.append(' '.join(a[i1:i2]))
            else: parts.append(' '.join(a[i1:i1+2])+' ~'+str(n-4)+'~ '+' '.join(a[i2-2:i2]))
        else:
            parts.append('{-'+' '.join(a[i1:i2])+' => '+' '.join(b[j1:j2])+'-}')
    return ' '.join(parts)
tot=0
for x in d:
    if x['f'].startswith('3-01'): continue
    p=strip(x['p']).split(); h=strip(x['h']).split()
    best=None;br=0
    for hp,hh,lab in hist[-120:] if len(p)>6 else []:
        if abs(len(hp)-len(p))>0.6*max(len(p),len(hp)): continue
        r=difflib.SequenceMatcher(None,hp,p,autojunk=False).quick_ratio()
        if r<THR: continue
        r=difflib.SequenceMatcher(None,hp,p,autojunk=False).ratio()
        if r>br: br=r;best=(hp,hh,lab)
    lab=x['id'] or x['f'][:4]+':'+str(x['i'])
    if best and br>=THR:
        s='[%s ~%s %.2f]\nP %s\nH %s\n'%(lab,best[2],br,fmt(best[0],p),fmt(best[1],h))
    else:
        s='[%s]\nP %s\nH %s\n'%(lab,' '.join(p),' '.join(h))
    out.write(s); tot+=len(s)
    hist.append((p,h,lab))
print(tot)
