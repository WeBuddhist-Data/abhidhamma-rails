import re,sys,difflib
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
fset=sys.argv[1]; start=int(sys.argv[2]); out=open(sys.argv[3],'w',encoding='utf-8')
THR=float(sys.argv[4]) if len(sys.argv)>4 else 0.5
hist=[]
def fmt(a,b):
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    parts=[]
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=='equal':
            n=i2-i1
            parts.append(' '.join(a[i1:i2]) if n<=2 else '·%d·'%n)
        else:
            parts.append('{'+' '.join(a[i1:i2])+'=>'+' '.join(b[j1:j2])+'}')
    return ' '.join(parts)
tot=0;nn=0
for x in d:
    if not x['f'].startswith(fset): continue
    if x['i']<start: 
        hist.append((strip(x['p']).split(),strip(x['h']).split(),x['id'] or 'x'))
        continue
    p=strip(x['p']).split(); h=strip(x['h']).split()
    best=None;br=0
    if len(p)>6:
      for hp,hh,lab in hist[-200:]:
        if abs(len(hp)-len(p))>0.5*max(len(p),len(hp)): continue
        m=difflib.SequenceMatcher(None,hp,p,autojunk=False)
        if m.quick_ratio()<THR: continue
        r=m.ratio()
        if r>br: br=r;best=(hp,hh,lab)
    lab=x['id'] or x['f'][:4]+':'+str(x['i'])
    if best and br>=THR:
        s='[%s~%s]\nP %s\nH %s\n'%(lab,best[2],fmt(best[0],p),fmt(best[1],h))
    else:
        s='[%s]\nP %s\nH %s\n'%(lab,' '.join(p),' '.join(h))
    out.write(s); tot+=len(s); nn+=1
    hist.append((p,h,lab))
print(tot,nn)
