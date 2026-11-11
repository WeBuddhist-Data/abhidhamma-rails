import re,sys,collections,pickle
sys.path.insert(0,r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review')
import B_load
from B_load import *
B_load.IDRE=re.compile(r'\^([0-9a-zA-Z\-]+)\s*$')
d=load()
strip=lambda s: re.sub(r'\s*\^[0-9a-zA-Z\-]+\s*$','',s).strip()
P=[strip(x['p']).split() for x in d]; H=[strip(x['h']).split() for x in d]
OUT=r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review'
def iscode(w): return w.startswith('⟦')
def lcs_multi(lines,minfrac):
    # longest token sequence (without codes) present in >=minfrac of lines
    lines=sorted(lines,key=len)
    need=max(2,int(round(minfrac*len(lines))))
    # candidates from the (len-need+1) shortest lines
    best=None
    sets={}
    for n in range(min(len(lines[-1]),260),3,-1):
        c=collections.Counter()
        for t in lines:
            seen=set()
            for i in range(len(t)-n+1):
                g=tuple(t[i:i+n])
                if any(iscode(w) for w in g): continue
                seen.add(g)
            for g in seen: c[g]+=1
        ok=[g for g,v in c.items() if v>=need]
        if ok:
            return max(ok,key=lambda g:c[g]),c
    return None,None
codes=[];dev=[]
k=0
for n in range(140,5,-1):
    while True:
        c=collections.defaultdict(set)
        for li,t in enumerate(P):
            for i in range(len(t)-n+1):
                g=tuple(t[i:i+n])
                if any(iscode(w) for w in g): continue
                c[g].add(li)
        c={g:v for g,v in c.items() if len(v)>=2}
        done=False
        items=sorted(c.items(),key=lambda kv:-len(kv[1]))
        progressed=False
        for g,ls in items:
            ls=sorted(ls)
            hl=[H[i] for i in ls]
            hg,cc=lcs_multi(hl,1.0)
            frac=1.0
            if hg is None or len(hg)<0.8*n:
                hg2,cc2=lcs_multi(hl,0.75) if len(ls)>=4 else (None,None)
                if hg2 is not None and len(hg2)>=0.8*n:
                    hg=hg2; frac=0.75
                else:
                    hg=None
            if hg is None: continue
            k+=1; code='⟦%d⟧'%k
            codes.append((code,' '.join(g),' '.join(hg),len(ls)))
            for li in ls:
                t=P[li]; i=0
                while i<=len(t)-n:
                    if tuple(t[i:i+n])==g: t[i:i+n]=[code]
                    i+=1
                t=H[li]; i=0; found=False; m=len(hg)
                while i<=len(t)-m:
                    if tuple(t[i:i+m])==hg: t[i:i+m]=[code]; found=True
                    i+=1
                if not found: dev.append((code,li))
            progressed=True
            break
        if not progressed: break
print(len(codes),len(dev),sum(len(x[1])+len(x[2]) for x in codes),sum(len(' '.join(t)) for t in P),sum(len(' '.join(t)) for t in H))
pickle.dump(dict(d=d,P=P,H=H,codes=codes,dev=dev),open(OUT+r'\B_pair.pkl','wb'))
