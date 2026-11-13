import re,sys,collections
base=r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
c=collections.Counter()
for i in range(1,7):
    t=open(f"{base}\\7-0{i}-anusayayamaka.md",encoding="utf-8").read()
    t=re.sub(r"\^[\d-]+","",t)
    for w in re.findall(r"[^\s.,?;:()\[\]…–—]+",t):
        if "ānusay" in w: continue
        c[w.lower()]+=1
for w,n in sorted(c.items()):
    print(n,w)
