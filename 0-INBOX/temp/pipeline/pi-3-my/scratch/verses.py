import pathlib, re
R = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails")
P = R / "AI_translation/pali/pi-3_split_chapters"; M = R / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
for p in sorted(P.glob("*.md"), key=lambda p: int(p.name.split("-")[0]) if p.name[0].isdigit() else 0):
    a = p.read_text(encoding="utf-8-sig").splitlines(); b = (M / p.name).read_text(encoding="utf-8").splitlines()
    for i, (x, y) in enumerate(zip(a, b)):
        prev = a[i-1] if i else ""
        if x.rstrip().endswith((";", ",")) or prev.rstrip().endswith((";", ",")):
            print(f"{p.name.split('-')[0]}| {x}\n   | {y}")
