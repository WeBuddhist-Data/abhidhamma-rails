"""User decision 2026-11-10: keep compounds whole instead of cutting them into non-word fragments (ññutā, bhuno, saha)."""
import pathlib

P = pathlib.Path(__file__).parent / "1-matika.mapped.md"
FIX = {
    "1-M2-61": {"bhuno": "cittasahabhuno", "saha": "cittasahabhuno", "bhuno dhammā": "cittasahabhuno dhammā"},
    "1-M2-64": {"bhuno": "sahabhuno", "saha": "sahabhuno"},
    "1-M2-127": {"ññutā": "mattaññutā", "matta": "mattaññutā"},
    "1-M2-128": {"ññutā": "mattaññutā", "matta": "mattaññutā"},
}
out, n = [], 0
for line in P.read_text(encoding="utf-8").splitlines():
    i, body = line.split("] ", 1)
    key = i[1:]
    if key in FIX:
        pairs = []
        for p in body.split(", "):
            pali, en = p.rsplit("=", 1)
            if pali in FIX[key]:
                pali, n = FIX[key][pali], n + 1
            pairs.append(f"{pali}={en}")
        line = f"{i}] " + ", ".join(pairs)
    out.append(line)
P.write_text("\n".join(out) + "\n", encoding="utf-8")
print("changed", n)
