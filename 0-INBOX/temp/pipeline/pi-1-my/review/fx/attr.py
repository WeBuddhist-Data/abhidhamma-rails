import pathlib,collections
A=pathlib.Path("before"); B=pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters")
SIG=[("L28 bahiddhā","မိမိ၏ ပြင်ပ၌"),("A1/A2","အကျိုး ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား "),
("A3","ကံ၏ ကြီးကျယ်သော အကျိုး"),("A4","ဆိတ်သုဉ်းသော ဈာန် သက်သက်"),("A5","ကောင်းသည်လည်း မဟုတ် နှစ်"),("B4","ကိလေသာ အခြေခံ ဆယ်ပါး"),
("B9","သဘောတရားနှင့် ကုသိုလ်လည်း"),("B11","ရှိသမျှ ဖြစ်သည့်"),("B8","ဆိုင်သော စိတ်"),("B1","သိမ်မွေ့သော ရုပ်ဘဝကို"),("B2","ဖြစ်သော စိတ်အနက်လည်းကောင်း ငါးပါး၊")]
tab=collections.defaultdict(collections.Counter); inst=collections.Counter(); un=0
for p in sorted(A.glob("*.md")):
    a=p.read_text(encoding="utf-8").split("\n"); b=(B/p.name).read_text(encoding="utf-8").split("\n")
    for x,y in zip(a,b):
        if x==y: continue
        hit=False
        for k,s in SIG:
            d=y.count(s)-x.count(s)
            if d>0: tab[k][p.name[:4]]+=1; inst[k]+=d; hit=True
        if not hit: un+=1; print("UNATTR",p.name,y[:80])
for k,_ in SIG: print(f"{k}\tinstances {inst[k]}\tlines {sum(tab[k].values())}\t"+", ".join(f"{c} {n}" for c,n in sorted(tab[k].items())))
print("unattributed",un)
