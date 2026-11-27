"""Book-wide typography check of the Burmese chapter files: no «?», no «।», no «:-», NFC, Myanmar letters only from
U+1000-U+104F (no Zawgyi-range / extended code points), no double blank lines.
usage: harmonise_typo.py <my_dir>"""
import pathlib, re, sys, unicodedata
bad = 0
for p in sorted(pathlib.Path(sys.argv[1]).glob("*.md")):
    t = p.read_text(encoding="utf-8")
    for i, l in enumerate(t.splitlines(), 1):
        why = []
        if "?" in l: why.append("?")
        if "।" in l: why.append("।")
        if ":-" in l: why.append(":-")
        if re.search(r"[ၐ-႟ꩠ-ꩿꧠ-꧿]", l): why.append("non-standard Myanmar code point")
        if unicodedata.normalize("NFC", l) != l: why.append("not NFC")
        if why:
            bad += 1; print(f"{p.name}:{i}: {', '.join(why)}")
    if "\n\n\n" in t:
        bad += 1; print(f"{p.name}: double blank line")
print("typography OK" if not bad else f"typography: {bad} problems")
sys.exit(1 if bad else 0)
