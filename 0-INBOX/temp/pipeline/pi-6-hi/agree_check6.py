"""Item 5 check: same subject noun must get the same verb agreement everywhere (count subject+verb forms)."""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C

if "--bak" in sys.argv:
    C.CUR["hdir"] = C.BAK
E = r"(?![ऀ-ॿ])"
FEM = r"(क्षमता|रचना|प्रवृत्ति|अनुभूति|पहचान|चेतना|परिघटना)"
MAS = r"(समूह|इंद्रिय-क्षेत्र|तत्व|सत्य|मन)"
PATS = {
    "fem sg + masc verb": FEM + r" (भी )?(उत्पन्न|समाप्त) (नहीं )?(होता|हुआ|होगा|हो चुका)" + E,
    "masc sg + fem verb": MAS + r" (भी )?(उत्पन्न|समाप्त) (नहीं )?(होती|हुई|होगी|हो चुकी)" + E,
    "fem pl + masc pl verb": r"(परिघटनाएँ|क्षमताएँ|रचनाएँ|प्रवृत्तियाँ) (भी )?(उत्पन्न|समाप्त) (नहीं )?(होते|हुए|होंगे)" + E,
    "fem sg + anuseti masc": r"प्रवृत्ति (भी )?(सोया|सोए)" + E,
}
for name, p in PATS.items():
    rx = re.compile(p)
    hits = collections.Counter()
    ex = []
    for part in C.PARTS:
        for i, (pl, hl) in enumerate(C.pairs(part)):
            for m in rx.finditer(hl):
                hits[C.short(part)] += 1
                if len(ex) < 6:
                    ex.append(f"{C.short(part)} #{i}: …{hl[max(0, m.start()-60):m.end()+20]}…")
    print(name, dict(hits))
    for e in ex:
        print("   ", e)
