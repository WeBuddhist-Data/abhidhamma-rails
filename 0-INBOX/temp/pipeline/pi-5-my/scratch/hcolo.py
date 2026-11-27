"""scratch: kathā heading name (no number) vs its colophon «X niṭṭhitā.» : same Pāli name -> same Burmese?"""
import pathlib, re, collections
ROOT = pathlib.Path(__file__).resolve().parents[5]
PD = ROOT / "AI_translation/pali/pi-5_split_chapters"; MD = ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r" \^[0-9A-Za-z-]+\s*$")
D = collections.defaultdict(set)
for p in PD.glob("*.md"):
    if p.suffix != ".md": continue
    for x, y in zip(p.read_text(encoding="utf-8-sig").split("\n"), (MD / p.name).read_text(encoding="utf-8").split("\n")):
        x, y = ID.sub("", x).strip(), ID.sub("", y).strip()
        m = re.match(r"#+ (?:\([\d-]+\) )?(?:[\d-]+\. )?(.+)$", x)
        if m:
            n = re.match(r"#+ (?:\([\d-]+\) )?(?:[\d-]+\. )?(.+)$", y)
            D[m[1].replace(" ", "").lower()].add(("H", n[1], p.name.split("-")[0]))
            continue
        m = re.match(r"(.+?) (?:\[[^\]]*\] )?niṭṭhit[āo]\.$", x)
        if m:
            n = re.match(r"“(.+?)”", y)
            D[m[1].replace(" ", "").lower()].add(("C", n[1] if n else y, p.name.split("-")[0]))
for k, v in sorted(D.items()):
    forms = {b for a, b, c in v}
    if len(forms) > 1:
        print(k, "\n   " + "\n   ".join(f"{a} {c}: {b}" for a, b, c in sorted(v, key=lambda t: t[2])))
