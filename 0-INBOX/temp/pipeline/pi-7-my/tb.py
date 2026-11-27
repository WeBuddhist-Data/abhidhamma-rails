"""Look up Pāli words in the locked Burmese termbases of pi-1 … pi-6 (read-only).

usage: python3 -I -X utf8 tb.py word [word ...]      exact key (case-insensitive)
       python3 -I -X utf8 tb.py --file <pali.md>      every distinct word of a Pāli chapter
       python3 -I -X utf8 tb.py --re <regex>          keys matching a regex
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
TB = [ROOT / f"AI_translation/burmese/pi-{b}-pali-burmese-termbase-plain.md" for b in range(1, 7)]
ENTRY = re.compile(r"^(?P<k>[^:{}]+): \{(?P<v>.*)\}\s*$")


def load():
    d = {}
    for i, f in enumerate(TB, 1):
        for line in f.read_text(encoding="utf-8").splitlines():
            m = ENTRY.match(line)
            if m:
                d.setdefault(m["k"].strip().lower(), []).append((i, m["v"]))
    return d


def show(d, k):
    for b, v in d.get(k.lower(), []):
        print(f"  pi-{b} {k}: {v[:400]}")


if __name__ == "__main__":
    d = load()
    a = sys.argv[1:]
    if a and a[0] == "--file":
        txt = pathlib.Path(a[1]).read_text(encoding="utf-8-sig")
        txt = re.sub(r"\^[0-9A-Za-z-]+", " ", txt)
        words = sorted(set(w.lower() for w in re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+", txt)))
        miss = []
        for w in words:
            if w in d:
                print(w)
                show(d, w)
            else:
                miss.append(w)
        print("NOT IN TERMBASES:", " ".join(miss))
    elif a and a[0] == "--re":
        rx = re.compile(a[1])
        for k in sorted(d):
            if rx.search(k):
                show(d, k)
    else:
        for w in a:
            print(w)
            show(d, w)
