import pathlib, collections
H = pathlib.Path(__file__).resolve().parents[1]
def rd(n):
    out = set()
    for l in open(H / n, encoding="utf-8"):
        f = l.strip().split("\t")
        if len(f) == 3 and f[0][:1].isdigit():
            out.add((f[0], f[1]))
    return out
z, r = rd("adherence-zeroshot.txt"), rd("adherence-rails.txt")
print(f"zero-shot {len(z)}; rails {len(r)}; fixed {len(z - r)}; new {len(r - z)}")
for x in sorted(r - z):
    print("  NEW", *x)
