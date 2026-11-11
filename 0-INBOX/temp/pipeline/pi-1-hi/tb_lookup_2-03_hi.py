"""Look up Pāli keys in the Hindi pi-3/4/5 termbases (read-only helper for part 2-03).

usage: python -I -X utf8 tb_lookup_2-03_hi.py key1 key2 ...
Prints every termbase line whose head word contains the key (case-insensitive), max 6 per book.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
HI = ROOT / "AI_translation" / "hindi"
for key in sys.argv[1:]:
    print("=====", key)
    for b in ("pi-3", "pi-4", "pi-5"):
        n = 0
        for line in (HI / f"{b}-pali-hindi-termbase-plain.md").read_text(encoding="utf-8").splitlines():
            head = line.split(":", 1)[0]
            if key.lower() in head.lower():
                print(f"  [{b}] {line[:300]}")
                n += 1
                if n >= 6:
                    break
