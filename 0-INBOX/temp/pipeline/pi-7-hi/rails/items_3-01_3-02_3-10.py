"""Helper for 3-01, 3-02, 3-10: list the item strings used in the frames (stdout only)."""
import re, collections, os, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
FILES = sys.argv[1:] or ["3-01-hetugocchaka.md", "3-02-culantaraduka.md", "3-10-upadanagocchaka.md"]
acc, nom, dat, pnom = (collections.Counter() for _ in range(4))
for f in FILES:
    t = open(os.path.join(PALI, f), encoding="utf-8").read()
    for m in re.finditer(r"(?:^|[.–] |… )([A-ZĀa-zāīūṃñṭḍṇḷ ]+?) dhammaṃ (paṭicca|paccayā|nissāya|sahajāto|saṃsaṭṭho|sampayutto|sahajātā|saṃsaṭṭhā|sampayuttā) ([a-zāīūṃñṭḍṇḷ ]+?) (dhammo|dhammā)", t, re.M):
        acc[m.group(1)] += 1; nom[m.group(3) + " " + m.group(4)] += 1
    for m in re.finditer(r"(?:^|[.–] )([A-ZĀa-zāīūṃñṭḍṇḷ ]+?) (dhammo|dhammā) ([a-zāīūṃñṭḍṇḷ ]+?) dhammassa ", t, re.M):
        pnom[m.group(1) + " " + m.group(2)] += 1; dat[m.group(3)] += 1
for name, c in (("ACC", acc), ("NOM", nom), ("PNOM", pnom), ("DAT", dat)):
    print("==", name)
    for k, n in sorted(c.items(), key=lambda x: -x[1]):
        print(f"{n}\t{k}")
