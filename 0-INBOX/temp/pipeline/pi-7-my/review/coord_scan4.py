import re,glob,os,collections
c=collections.Counter(); ex={}
NOUN=r'(?:မှု|ခြင်း|တရား|စိတ်|မောဟ|ရာဂ|ဒေါသ|ဉာဏ်|ပညာ|အစုအဝေး|ဝတ္ထု|နေရာ|အစာ|ဥတု|သီလ|ဒိဋ္ဌိ|မာန|ကံ|ရုပ်|တို့)'
pats=[re.compile(r'(\S+ကို)… (?!\S*ကို)(\S+)'), re.compile(r'(\S+ကို) (\S+'+NOUN+r'(?:သည်|အား))(?=[ …၊])')]
for f in sorted(glob.glob('burmese/pi-7-burmese-plain-rails_split_chapters/*.md')):
    for i,l in enumerate(open(f,encoding='utf8').read().split('\n'),1):
        for p in pats:
            for m in p.finditer(l):
                k=m.group(1)+' | '+m.group(2); c[k]+=1; ex.setdefault(k,(os.path.basename(f)[:18],i))
for k,v in c.most_common(45): print(v,k,ex[k])
