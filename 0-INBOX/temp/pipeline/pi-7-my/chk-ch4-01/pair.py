import sys,re
P=open("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/AI_translation/pali/pi-7_split_chapters/4-01-kilesagocchaka.md",encoding="utf-8").read().split("\n")
Bm=open(sys.argv[1],encoding="utf-8").read().split("\n")
pat=re.compile(sys.argv[2]); n=int(sys.argv[3]) if len(sys.argv)>3 else 3; w=int(sys.argv[4]) if len(sys.argv)>4 else 900
k=0
for i,(p,b) in enumerate(zip(P,Bm),1):
    if pat.search(p):
        print(i,"P:",p[:w]); print(i,"B:",b[:w]); print(); k+=1
        if k>=n: break
