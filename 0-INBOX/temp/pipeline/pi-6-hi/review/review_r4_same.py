import re,collections
PB=r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
HB=r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters"
c=collections.Counter(); where=collections.defaultdict(list)
for i in range(1,7):
    f=f"7-0{i}-anusayayamaka.md"
    P=[l for l in open(f"{PB}\\{f}",encoding="utf-8").read().split("\n") if l.strip()]
    H=[l for l in open(f"{HB}\\{f}",encoding="utf-8").read().split("\n") if l.strip()]
    for n,(a,b) in enumerate(zip(P,H),1):
        sa=re.split(r"(?<=[.?])\s+",a); sb=re.split(r"(?<=[।?])\s+",b)
        if len(sa)!=len(sb): continue
        for x,y in zip(sa,sb):
            m=re.match(r"(Tesaññeva puggalānaṃ|Tasseva puggalassa|Teva puggalā|Sveva puggalo)",x)
            if m:
                k=(m.group(1)," ".join(y.split()[:3]))
                c[k]+=1; where[k].append(f"{f[:4]}:{n}")
for k,v in c.items(): print(v,k,where[k][:4])