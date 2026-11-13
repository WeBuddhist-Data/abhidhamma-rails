import re
PB=r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
HB=r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters"
for i in range(1,7):
    f=f"7-0{i}-anusayayamaka.md"
    P=[l for l in open(f"{PB}\\{f}",encoding="utf-8").read().split("\n") if l.strip()]
    H=[l for l in open(f"{HB}\\{f}",encoding="utf-8").read().split("\n") if l.strip()]
    for n,(a,b) in enumerate(zip(P,H),1):
        if a.startswith("#") or ("ānusay" not in a) or "[" in a:
            print(f,n,"|",a,"||",b)