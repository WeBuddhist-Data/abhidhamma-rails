import re
P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-2_split_chapters\18-dhammahadayavibhango.md"
V = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\18-dhammahadayavibhango.md"
p = open(P, encoding="utf-8").read().split("\n")
v = open(V, encoding="utf-8").read().split("\n")
# Pāli number prefixes -> value
pn = [("bāvīsat",22),("aṭṭhārasa",18),("soḷasa",16),("pannarasa",15),("cuddas",14),("teras",13),("dvādas",12),("ekādas",11),("dasa",10),("das",10),
      ("nava",9),("nav",9),("aṭṭha",8),("aṭṭh",8),("satta",7),("satt",7),("cha",6),("pañca",5),("pañc",5),("cattār",4),("catasso",4),("cattāro",4),
      ("tīṇi",3),("tīṇ",3),("tayo",3),("tisso",3),("dve",2),("dv",2),("eka",1),("eko",1),("ekā",1),("ekaṃ",1)]
vn = {"hai mươi hai":22,"mười tám":18,"mười sáu":16,"mười lăm":15,"mười bốn":14,"mười ba":13,"mười hai":12,"mười một":11,"mười":10,"chín":9,"tám":8,"bảy":7,"sáu":6,"năm":5,"bốn":4,"ba":3,"hai":2,"một":1}
def pnums(s):
    out=[]
    for w in re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]+", s):
        lw=w.lower()
        if lw in ("indriyāni","dhātuyo"): continue
        for pre,val in pn:
            if lw.startswith(pre) and (lw in ("dasa","nava","aṭṭha","satta","cha","pañca","tīṇi","tayo","tisso","dve","eko","ekā","ekaṃ","cattāro","catasso","cattāri","soḷasa","aṭṭhārasa","pannarasa") or re.match(pre+r"(indriy|āyatan|dhātu|indriyā|āyatanā|ā$|indriyāni|āyatanāni|sindriy)", lw) or lw.startswith(("dvāyatan","dvindriy","cattārindriy","pañcāyatan","pañcindriy","sattindriy","sattāyatan","navindriy","navāyatan","aṭṭhindriy","dasindriy","dasāyatan","tīṇindriy","ekādasindriy","ekādasāyatan","dvādasindriy","dvādasāyatan","terasindriy","cuddasindriy","bāvīsatindriy","pañcakkhandh","ekindriy"))):
                out.append(val); break
    return out
def vnums(s):
    s=s.lower()
    out=[]
    for m in re.finditer(r"(?<![\wà-ỹ])(hai mươi hai|mười tám|mười sáu|mười lăm|mười bốn|mười ba|mười hai|mười một|mười|chín|tám|bảy|sáu|năm|bốn|ba|hai|một)(?=\s+(khối|lĩnh vực|yếu tố|sự thật|năng lực|gốc rễ|loại))", s):
        out.append(vn[m.group(1)])
    return out
for i,(a,b) in enumerate(zip(p,v),1):
    if i<5 or i>420: continue
    x=sorted(pnums(a)); y=sorted(vnums(b))
    if x!=y:
        print(i, "PI", x, "VI", y)
