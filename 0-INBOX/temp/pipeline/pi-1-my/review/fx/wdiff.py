"""wdiff.py <dirA> <dirB>: per chapter changed lines and the changed spans (counts of (old,new) span pairs)."""
import difflib,pathlib,sys,collections
A,B=map(pathlib.Path,sys.argv[1:3]); c=collections.Counter(); tot=0
for p in sorted(A.glob("*.md")):
    a=p.read_text(encoding="utf-8").split("\n"); b=(B/p.name).read_text(encoding="utf-8").split("\n")
    assert len(a)==len(b),p
    n=0
    for x,y in zip(a,b):
        if x==y: continue
        n+=1
        sm=difflib.SequenceMatcher(None,x,y,autojunk=False)
        for op,i1,i2,j1,j2 in sm.get_opcodes():
            if op!="equal": c[(x[i1:i2],y[j1:j2])]+=1
    tot+=n; print(p.name[:-3],n)
print("total",tot)
for (o,n),k in c.most_common(): print(k,f"«{o}» → «{n}»")
