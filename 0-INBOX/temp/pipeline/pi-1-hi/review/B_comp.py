import re,sys,collections,pickle
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
def compress(lines,prefix,minn=5,minc=3,maxn=120):
    toks=[l.split() for l in lines]
    codes={}
    k=0
    for n in range(maxn,minn-1,-1):
        while True:
            c=collections.Counter()
            for t in toks:
                for i in range(len(t)-n+1):
                    g=tuple(t[i:i+n])
                    if any(w.startswith('⟦') for w in g): continue
                    c[g]+=1
            c={g:v for g,v in c.items() if v>=minc}
            if not c: break
            g=max(c,key=lambda g:(c[g]*sum(len(w) for w in g)))
            k+=1
            code='⟦%s%d⟧'%(prefix,k)
            codes[code]=' '.join(g)
            found=0
            for t in toks:
                i=0
                while i<=len(t)-n:
                    if tuple(t[i:i+n])==g:
                        t[i:i+n]=[code]; found+=1
                    i+=1
    return [' '.join(t) for t in toks],codes
P=[strip(x['p']) for x in d]; H=[strip(x['h']) for x in d]
cp,pc=compress(P,'P'); ch,hc=compress(H,'H')
print(len(pc),len(hc))
print(sum(map(len,cp)),sum(map(len,ch)),sum(map(len,pc.values())),sum(map(len,hc.values())))
pickle.dump(dict(d=d,cp=cp,ch=ch,pc=pc,hc=hc),open(r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review\B_comp.pkl','wb'))
