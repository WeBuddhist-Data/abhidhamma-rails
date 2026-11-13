"""Helper for 1-02..1-05: list distinct tokens / clause patterns of the Pāli files.
usage: python -I -B -X utf8 analyze_1-02_1-05.py tokens|clauses <file stem> [min]"""
import collections
import re
import sys

PALI = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters"
FILES = ["1-02-vedanattika", "1-03-vipakattika", "1-04-upadinnattika", "1-05-sankilitthattika"]
TOK = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+")
ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")

ITEMS = [
    (r"(?:a?dukkham?a?sukhāya|sukhāya|dukkhāya) vedanāya sampayutt\w*", "<V>"),
    (r"(?:neva)?(?:vipāka|Vipāka)(?:dhamma)?(?:navipākadhamma)?dhamm\w+", "<VP>"),
    (r"(?:A|a)?(?:nupādinn|upādinn|Upādinn)\w*", "<U>"),
    (r"(?:A|a)?(?:saṃkiliṭṭh|Saṃkiliṭṭh)\w*", "<S>"),
]


def lines(stem):
    for ln in open(f"{PALI}\\{stem}.md", encoding="utf-8").read().split("\n"):
        if ln.strip():
            m = ID_RE.search(ln)
            yield ln[: m.start()] if m else ln


if __name__ == "__main__":
    mode, stem = sys.argv[1], sys.argv[2]
    mn = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    stems = FILES if stem == "all" else [stem]
    c = collections.Counter()
    for s in stems:
        for ln in lines(s):
            if ln.startswith("#"):
                c["H| " + ln.lstrip("# ")] += 1
                continue
            if mode == "tokens":
                for t in TOK.findall(ln):
                    c[t] += 1
            else:
                t = ln
                for rx, ph in ITEMS:
                    t = re.sub(rx, ph, t)
                for piece in re.split(r" – |; |\. |\.$|…pe…|…|, | \(\d+\)", t):
                    piece = piece.strip()
                    if piece:
                        c[piece] += 1
    for k, v in sorted(c.items(), key=lambda kv: (-kv[1], kv[0])):
        if v >= mn:
            print(v, k)
