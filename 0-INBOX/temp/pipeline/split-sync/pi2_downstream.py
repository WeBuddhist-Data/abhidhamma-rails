import pathlib, re, difflib
B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
ID = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")
ids = lambda t: [m.group(1) for l in t.splitlines() if (m := ID.search(l))]
root = ids((B / "1-SOURCES/Text/pi-2.md").read_text(encoding="utf-8"))
def rep(name, got):
    if got == root:
        print(f"{name}: IDs match the root ({len(got)})"); return
    sm = difflib.SequenceMatcher(None, got, root, autojunk=False)
    miss = [i for t, a1, a2, b1, b2 in sm.get_opcodes() if t != "equal" for i in root[b1:b2]]
    extra = [i for t, a1, a2, b1, b2 in sm.get_opcodes() if t != "equal" for i in got[a1:a2]]
    print(f"{name}: {len(got)} IDs vs root {len(root)}; missing {len(miss)} {miss[:6]}; extra {len(extra)} {extra[:6]}")
for f in ["AI_translation/english/pi-2-english-plain.md", "3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/pi-2-english-plain.md"]:
    p = B / f
    if p.exists(): rep(f, ids(p.read_text(encoding="utf-8")))
for d in ["AI_translation/english/pi-2-english-plain-rails_split_chapters", "AI_translation/english/pi-2-english-plain-zeroshot_split_chapters"]:
    allids = [i for p in (B / d).glob("*.md") for i in ids(p.read_text(encoding="utf-8"))]
    print(f"{d}: {len(allids)} IDs; same set as root: {set(allids) == set(root)}; missing {sorted(set(root) - set(allids))[:6]} extra {sorted(set(allids) - set(root))[:6]}")
