"""Per line: Pāli «X ceva na/no/nana/nano ca Y» count vs Hindi «, पर स्वयं» count."""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ar7_common as C

if "--bak" in sys.argv:
    C.CUR["hdir"] = C.BAK
P = re.compile(r"(?:ceva|ñceva) (?:na|no|nana|nano) ca\b")
H = re.compile(r", पर स्वयं ")
tot = collections.Counter()
for part in C.PARTS:
    for i, (p, h) in enumerate(C.pairs(part)):
        a, b = len(P.findall(p)), len(H.findall(h))
        if a != b:
            tot[part[:4]] += 1
            if "-v" in sys.argv:
                print(f"{part[:4]}:{i+1} pali={a} hindi={b}")
print(dict(tot))
