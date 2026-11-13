import sys, re, pathlib
p = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters") / sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "head"
lines = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
print("nonempty", len(lines))
if mode == "head":
    for i, l in enumerate(lines, 1):
        if l.startswith("#"):
            print(i, l[:150])
elif mode == "range":
    a, b = int(sys.argv[3]), int(sys.argv[4])
    w = int(sys.argv[5]) if len(sys.argv) > 5 else 100000
    for i in range(a, min(b, len(lines)) + 1):
        print(i, lines[i - 1][:w])
