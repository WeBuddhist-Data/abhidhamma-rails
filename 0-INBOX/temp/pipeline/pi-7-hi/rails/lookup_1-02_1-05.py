"""Helper for 1-02..1-05: termbase entries for words (args) or for the leftover words in a file.
usage: python -I -B -X utf8 lookup_1-02_1-05.py w1 w2 ...   |   python ... lookup_1-02_1-05.py --file <path>"""
import re
import sys

TB = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md"
TOK = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+")


def load():
    tb = {}
    for line in open(TB, encoding="utf-8").read().splitlines():
        if ": {" in line:
            w, body = line.split(": {", 1)
            tb.setdefault(w.lower(), []).append(body[:-1])
    return tb


if __name__ == "__main__":
    tb = load()
    args = sys.argv[1:]
    if args and args[0] == "--file":
        words = []
        for t in TOK.findall(open(args[1], encoding="utf-8").read()):
            if t not in words:
                words.append(t)
    else:
        words = args
    for w in words:
        e = tb.get(w.lower())
        print(f"{w}: {' | '.join(e) if e else '-'}")
