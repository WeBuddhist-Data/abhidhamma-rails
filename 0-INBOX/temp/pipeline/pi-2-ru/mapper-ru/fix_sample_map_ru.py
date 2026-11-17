"""User decision 2026-11-16 on the pi-2 Russian map sample: N-vidhena keywords map to the part of the Russian that
renders them, without the word «классификация» (which the translation added for readability):
  Duvidhena = «на два вида», Ekavidhena = «по одному», dasavidhena = «на десять видов»;
  dasavidhena X-kkhandho = «совокупность X на десять видов».
Applies to all *.mapped.md in this folder; idempotent. Later chapters follow the same rule (ru-map-conventions-pi2.md).
"""
import pathlib, re

D = pathlib.Path(__file__).resolve().parent
n = 0
for p in sorted(D.glob("*.mapped.md")):
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if "] " in line:
            head, body = line.split("] ", 1)
            items = []
            for it in body.split(", "):
                k, v = it.split("=", 1)
                if "idhena" in k.lower() and v.startswith("классификация "):   # -vidhena and -bbidhena (Catubbidhena, Chabbidhena)
                    nv = v[len("классификация "):]
                    if nv.startswith("… "):
                        nv = nv[2:]
                    elif nv.startswith("совокупности "):          # dasavidhena X-kkhandho
                        nv = "совокупность " + nv[len("совокупности "):]
                    if nv != v:
                        n += 1
                    v = nv
                items.append(f"{k}={v}")
            line = head + "] " + ", ".join(items)
        out.append(line)
    p.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("values changed:", n)
