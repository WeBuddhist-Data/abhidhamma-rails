import pathlib,re,sys,collections
ROOT=pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails")
P=ROOT/"AI_translation/pali/pi-1_split_chapters"; M=ROOT/"AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters"
rx=re.compile(sys.argv[1]); c=collections.Counter(); 
for f in sorted(P.glob("*.md")):
    t=(P if sys.argv[2]=="p" else M)/f.name
    for m in rx.finditer(t.read_text(encoding="utf-8")): c[(f.name[:4],m.group(0))]+=1
for k,v in sorted(c.items()): print(v,k)
print(sum(c.values()))
