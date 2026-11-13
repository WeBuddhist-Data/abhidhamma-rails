"""Print the termbase entries of every distinct Pāli word in the given files (first-seen order).
usage: python -I -B -X utf8 lookup_sample.py <termbase> <pali files...> [--missing]"""
import re
import sys

TOK = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+")


def load(tb_path):
    tb = {}
    for line in open(tb_path, encoding="utf-8").read().splitlines():
        if ": {" in line:
            w, body = line.split(": {", 1)
            tb[w] = body[:-1]
    return tb


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    missing_only = "--missing" in sys.argv
    tb = load(args[0])
    ci = {k.lower(): v for k, v in tb.items()}
    seen = []
    for p in args[1:]:
        text = open(p, encoding="utf-8").read()
        text = re.sub(r"\^[0-9A-Za-z-]+", " ", text)
        for t in TOK.findall(text):
            if t not in seen:
                seen.append(t)
    for t in seen:
        e = tb.get(t) or ci.get(t.lower())
        if missing_only:
            if not e:
                print(t)
        elif e:
            print(f"{t}: {e}")
        else:
            print(f"{t}: -")
