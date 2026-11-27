"""pg.py <pali regex> [burmese regex] [--full] : aligned Pāli/Burmese lines (rails) where the Pāli matches (and Burmese, if given)."""
import pathlib,re,sys
ROOT=pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails")
P=ROOT/"AI_translation/pali/pi-1_split_chapters"; M=ROOT/"AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters"
ID=re.compile(r"\^([0-9A-Za-z-]+)\s*$")
a=[x for x in sys.argv[1:] if not x.startswith("--")]; full="--full" in sys.argv; cnt="--count" in sys.argv
pr=re.compile(a[0]); br=re.compile(a[1]) if len(a)>1 else None
def segs(lines):
    out,buf=[],[]
    for k,l in enumerate(lines):
        if not l.strip(): continue
        buf.append(k); m=ID.search(l)
        if m: out.append((m.group(1),buf)); buf=[]
    return out
n=0
for f in sorted(p.name for p in P.glob("*.md")):
    pl=(P/f).read_text(encoding="utf-8").split("\n"); ml=(M/f).read_text(encoding="utf-8").split("\n")
    ms=dict(segs(ml))
    for i,idx in segs(pl):
        for pk,mk in zip(idx,ms[i]):
            if pr.search(pl[pk]) and (br is None or br.search(ml[mk])):
                n+=1
                if cnt: continue
                if full: print(f"{f[:5]} {i} L{mk+1}\n P: {pl[pk]}\n M: {ml[mk]}")
                else:
                    pm=pr.search(pl[pk]); s=max(0,pm.start()-80)
                    bm=br.search(ml[mk]) if br else None
                    print(f"{f[:5]} {i} L{mk+1} P: …{pl[pk][s:pm.end()+80]}")
                    if bm: print(f"    M: …{ml[mk][max(0,bm.start()-100):bm.end()+100]}")
                    else: print(f"    M: {ml[mk][:300]}")
print("lines:",n)
