import re,sys
L=open(sys.argv[1] if len(sys.argv)>1 else "dev.txt",encoding="utf-8").read().split("\n")
out=[]
for i in range(0,len(L)-1,2):
    m=re.match(r"\[(\d+)\] SK: (.*)",L[i])
    if not m: continue
    sk=m[2]; f=re.search(r"lex: (.*?) in «",sk)
    out.append((m[1], f[1] if f else sk[:60], L[i+1].strip()[:230]))
for c,f,p in out: print(c,"|",f,"|",p)
