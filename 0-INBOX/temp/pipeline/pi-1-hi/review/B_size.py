import re,collections
t=open(r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\review\B_delta.txt',encoding='utf-8').read()
blocks=re.findall(r'\[(\S+)( ~\S+ [\d.]+)?\]\nP (.*)\nH (.*)\n',t)
tot=collections.Counter();n=collections.Counter()
def num(l):
    m=re.match(r'1-(\d+)$',l)
    return int(m.group(1)) if m else 0
for lab,sim,p,h in blocks:
    v=num(lab)
    b='3-02' if v<=730 else '3-03' if v<=1000 else '4' if v<=1380 else '5'
    tot[(b,bool(sim))]+=len(p)+len(h); n[(b,bool(sim))]+=1
for k in sorted(tot): print(k,n[k],tot[k])
