import re,collections
HB=r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters"
PB=r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
PL=r"(इंद्रिय-सुखों के लोक की (?:दो|तीन) अनुभूतियों|दुःखद अनुभूति|सूक्ष्म भौतिक लोक|अभौतिक लोक|अस्तित्व के लोकों में न समाई हुई परिघटनाओं|व्यक्तित्व में समाई हुई सभी परिघटनाओं|सब जगह)( \S+)?"
for i in range(1,7):
    f=f"7-0{i}-anusayayamaka.md"
    t=open(f"{HB}\\{f}",encoding="utf-8").read()
    c=collections.Counter(m.group(2) for m in re.finditer(PL,t))
    print(f,dict(c))
    tl=[l for l in t.split("\n") if l.strip()]
    pl=[l for l in open(f"{PB}\\{f}",encoding="utf-8").read().split("\n") if l.strip()]
    v=collections.Counter()
    for a,b in zip(pl,tl):
        if "adekaṭṭh" in a:
            v[(re.sub(r"\^[\d-]+","",a).strip()[-70:], re.sub(r"\^[\d-]+","",b).strip()[-90:])]+=1
    for k,n in v.items(): print("  TADEK",n,k)