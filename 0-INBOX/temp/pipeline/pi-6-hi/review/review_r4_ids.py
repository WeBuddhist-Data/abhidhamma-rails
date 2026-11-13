import re
PB=r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
def ids(f):
    P=[l for l in open(f"{PB}\\{f}",encoding="utf-8").read().split("\n") if l.strip()]
    out=[None]*len(P); nxt=None
    for k in range(len(P)-1,-1,-1):
        m=re.search(r"\^([\d-]+)\s*$",P[k])
        if m: nxt=m.group(1)
        out[k]=nxt
    return P,out
teva={}
for i in range(1,7):
    f=f"7-0{i}-anusayayamaka.md"; P,I=ids(f)
    for n,l in enumerate(P,1):
        if "Teva puggalā" in l: teva.setdefault(f,[]).append((n,I[n-1]))
        for pat in ["ariyāpanne so","anusanti","kāmārāga","Pajahanāvāre","Arahā sabbattha bhavarāgānusayena niranusayo kāmarāgānusayena ca paṭighānusayena ca niranusayo","niranusayo no ca","pajahati no ca"]:
            if pat in l and not (pat=="ariyāpanne so" and "apariyāpanne so" in l and "  " in l): 
                if pat=="ariyāpanne so" and " ariyāpanne" not in l: continue
                print(f,n,I[n-1],pat)
for f,v in teva.items(): print(f, sorted(set(x[1] for x in v)), len(v))