import sys, pathlib
p = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters") / sys.argv[1]
w = int(sys.argv[2]) if len(sys.argv) > 2 else 110
n = 0
for i, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
    if l.strip():
        n += 1
        print(f"{i}/{n} [{len(l)}] {l[:w]}")
