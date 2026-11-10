"""Coordinator fixes after the harmonise pass (2026-11-10): two awkward tie-break phrasings.

Changes a line only when its aligned Pāli line has the item. Logs to harmonise-notes.md.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[4]
EN = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
FIXES = [
    ("natthi ayaṃ loko", "there is no this world, there is no other world",
     "this world does not exist, the other world does not exist"),
    ("kāmajjhosān", "sensual holding on", "holding on to sensual pleasures"),
]
total = {}
for en_path in sorted(EN.glob("*.md")):
    en = en_path.read_text(encoding="utf-8").split("\n")
    pi = [l for l in (PI / en_path.name).read_text(encoding="utf-8-sig").split("\n") if l.strip()]
    k, changed = 0, False
    for i, line in enumerate(en):
        if not line.strip():
            continue
        p = pi[k]
        k += 1
        for cond, old, new in FIXES:
            if old in line:
                assert cond in p, (en_path.name, k, old)
                n = line.count(old)
                line = line.replace(old, new)
                total[(en_path.name, old)] = total.get((en_path.name, old), 0) + n
                changed = True
        en[i] = line
    if changed:
        en_path.write_text("\n".join(en), encoding="utf-8", newline="\n")
for (f, old), n in sorted(total.items()):
    print(f"{f}: {n} x {old!r}")
log = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-1-en" / "harmonise-notes.md"
with log.open("a", encoding="utf-8", newline="\n") as fh:
    fh.write("\n## Coordinator fixes after the pass (fix_awkward.py)\n\n")
    for cond, old, new in FIXES:
        n = sum(v for (f, o), v in total.items() if o == old)
        fh.write(f"- {cond}…: \"{old}\" → \"{new}\" ({n} occurrences; the tie-break wording was not natural English)\n")
