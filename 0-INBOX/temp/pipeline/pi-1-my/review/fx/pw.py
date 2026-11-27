"""pw.py <burmese regex> <pali regex>: for each aligned line with a Burmese match, list Pāli matches and Burmese matches (with context)."""
import pathlib,re,sys
ROOT=pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails")
P=ROOT/"AI_translation/pali/pi-1_split_chapters"; M=ROOT/"AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters"
ID=re.compile(r"\^([0-9A-Za-z-]+)\s*$")
br=re.compile(sys.argv[1]); pr=re.compile(sys.argv[2])
def segs(lines):
    out,buf=[],[]
    for k,l in enumerate(lines):
        if not l.strip(): continue
        buf.append(k); m=ID.search(l)
        if m: out.append((m.group(1),buf)); buf=[]
    return out
for f in sorted(p.name for p in P.glob("*.md")):
    pl=(P/f).read_text(encoding="utf-8").split("\n"); ml=(M/f).read_text(encoding="utf-8").split("\n"); ms=dict(segs(ml))
    for i,idx in segs(pl):
        for pk,mk in zip(idx,ms[i]):
            b=[ml[mk][max(0,x.start()-25):x.end()+30] for x in br.finditer(ml[mk])]
            p=[x.group(0) for x in pr.finditer(pl[pk])]
            if b or (p and len(sys.argv)>3):
                print(f"{f[:4]} {i} L{mk+1} P{len(p)}:{p} B{len(b)}"); [print("   ",y) for y in b]
