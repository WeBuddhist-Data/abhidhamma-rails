"""Check every vīriya synonym string (Yo cetasiko vīriyārambho …) against its own Pāli line, item by item.
usage: python -I -X utf8 check_viriya_ru.py [--bak]
Prints lines whose Russian items differ from the Pāli items mapped through VW.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ru_common
from ru_common import PARTS, pairs, VAR, BID

VW = {"vīriyārambho": "душевное приложение усердия", "nikkamo": "порыв", "parakkamo": "напор", "uyyāmo": "старание",
      "vāyāmo": "усилие", "ussāho": "рвение", "ussoḷhī": "упорство", "thāmo": "стойкость", "ṭhiti": "устойчивость",
      "asithilaparakkamatā": "неослабевающий напор", "anikkhittachandatā": "неотступное желание",
      "anikkhittadhuratā": "неотступное несение бремени", "dhurasampaggāho": "крепкое удержание бремени",
      "vīriyaṃ": "усердие", "vīriyindriyaṃ": "способность усердия", "vīriyabalaṃ": "сила усердия",
      "sammāvāyāmo": "правильное усилие", "vīriyasambojjhaṅgo": "фактор пробуждения усердия", "maggaṅgaṃ": "фактор пути",
      "maggapariyāpannaṃ": "входящий в путь", "…pe…": "…",
      "maggariyāpannaṃ": "входящий в путь"}  # ch9 ^2-433 spelling slip, rendered as meant (notes-7-9)

if "--bak" in sys.argv:
    ru_common.CUR["rdir"] = ru_common.BAK
bad = n = 0
for part in PARTS:
    for i, (p, r) in enumerate(pairs(part)):
        p0 = BID.sub("", VAR.sub("", p)).rstrip(".")
        r = BID.sub("", r).rstrip(".")
        for m in re.finditer(r"cetasiko vīriyārambho(.*?)(?= [–—] |$)", p0):
            n += 1
            toks = ["vīriyārambho"] + m.group(1).replace("…pe…", " …pe… ").split()
            exp = []
            for t in toks:
                t = t.strip(",.")
                exp.append(VW.get(t, "?" + t))
            # Russian: from «приложение усердия» to the dash
            rr = VAR.sub("", r)
            k = rr.find("душевное приложение усердия")
            seg = rr[k:]
            seg = re.split(r",? [–—] ", seg)[0]
            got = [x.strip() for x in re.split(r",\s*|(…)", seg) if x and x.strip()]
            e2 = [x for x in exp]
            if [g.strip(",") for g in got] != e2:
                bad += 1
                print(f"[{part} L{i+1}]\n  exp: {e2}\n  got: {got}")
print("vīriya strings:", n, "mismatching:", bad)
