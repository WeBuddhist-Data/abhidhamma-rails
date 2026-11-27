import re,glob,os,collections
# an object «Xကို» directly followed by a recipient «…အား» or a subject «…သည်», with no verb in between
pat=re.compile(r"(\S+ကို)(…)? (\S+?(?:မှု|ခြင်း|တရား|စိတ်|မောဟ|ရာဂ|ဒေါသ|ဉာဏ်|ပညာ|အစုအဝေး|ဝတ္ထု|နေရာ|အစာ|ဥတု|ယုံကြည်မှု|သီလ|တို့)?)(အား|သည်)(?=[ …၊])")
c=collections.Counter(); ex={}
for f in sorted(glob.glob('burmese/pi-7-burmese-plain-rails_split_chapters/*.md')):
    for i,l in enumerate(open(f,encoding='utf8').read().split('\n'),1):
        for m in pat.finditer(l):
            k=m.group(1)+(m.group(2) or '')+' '+m.group(3)+m.group(4)
            c[k]+=1; ex.setdefault(k,(os.path.basename(f)[:18],i))
for k,v in c.most_common(40): print(v,k,ex[k])
