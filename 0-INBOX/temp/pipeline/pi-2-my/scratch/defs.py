import re,sys,pathlib,collections
R=pathlib.Path("../../../../AI_translation")
pat=re.compile(sys.argv[1])
seen=collections.defaultdict(lambda: collections.defaultdict(list))
for p in sorted((R/"pali/pi-2_split_chapters").glob("*.md")):
    P=p.read_text().split("\n"); M=(R/"burmese/pi-2-burmese-plain-zeroshot_split_chapters"/p.name).read_text().split("\n")
    for i,(x,y) in enumerate(zip(P,M),1):
        xs=re.split(r"(?<=[.?])(?:\"|”)? (?=\S)",re.sub(r" \^\S+$","",x)); ys=re.split(r"(?<=။) ",re.sub(r" \^\S+$","",y))
        if len(xs)!=len(ys):
            if pat.search(x): print("UNEVEN",p.name[:3],i)
            continue
        for s,t in zip(xs,ys):
            if pat.search(s): seen[s][t].append(f"{p.name.split('-')[0]}:{i}")
for s,v in seen.items():
    print("PI:",s[:300])
    for t,l in v.items(): print("  ",l[:5],t[:400])
