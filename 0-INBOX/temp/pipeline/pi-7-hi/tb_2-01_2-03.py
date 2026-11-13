import sys, pathlib, re
D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi")
books = sys.argv[2].split(",") if len(sys.argv) > 2 else ["1", "2", "5", "6"]
words = sys.argv[1].split(",")
for b in books:
    lines = (D / f"pi-{b}-pali-hindi-termbase-plain.md").read_text(encoding="utf-8").splitlines()
    for w in words:
        rx = re.compile(r"^" + w + r"\S*:", re.I)
        hits = [l for l in lines if rx.match(l)]
        for h in hits[:4]:
            print(f"pi-{b}", h[:260])
