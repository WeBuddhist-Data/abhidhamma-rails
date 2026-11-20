import sys
# Print Tịnh Sự lines (console only) for a line range, skipping transclusion lines.
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
TS = ROOT + r"\1-SOURCES\Translations\Vietnamese\vi-2-tinh_su.md"
a, b = int(sys.argv[1]), int(sys.argv[2])
with open(TS, encoding="utf-8") as f:
    for i, l in enumerate(f, 1):
        if i < a:
            continue
        if i > b:
            break
        l = l.rstrip("\n")
        if not l.strip() or l.startswith("![["):
            continue
        print(f"{i}: {l}")
