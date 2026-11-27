"""pi-2 Burmese rails, pi-1 identity (copy of pi-2-my/harmonise_pi1.py with the Burmese folder as argument): every Pāli sentence (and heading) of pi-2 that also occurs in pi-1 must have exactly
pi-1's FINAL Burmese (the rails text, AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters, read-only).
usage: python3 -I -X utf8 pi1_identity.py <pi-2 burmese split dir> [-q]
Units (as check_sample.reuse, all 19 chapters, any length):
  * headings: the heading text after the «#» marks;
  * sentences of lines whose Pāli and Burmese split into the same number of sentences (Pāli on «.» / «?» outside
    variant brackets, Burmese on «။»);
  * on lines that split unevenly: every Pāli sentence of > 25 characters that occurs in pi-1 must have one of pi-1's
    Burmese renderings (without its final «။») as a substring of the Burmese line (as align_hidden_my.py).
Prints «pi-1 identity: same / n identical» and every difference; exit 1 if any differs."""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
A = ROOT / "AI_translation"
P1P, P1M = A / "pali/pi-1_split_chapters", A / "burmese/pi-1-burmese-plain-rails_split_chapters"
P2P = A / "pali/pi-2_split_chapters"
P2M = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else A / "burmese/pi-2-burmese-plain-rails_split_chapters"
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")


def psplit(l):
    l = ID_RE.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]


def bsplit(l):
    return [s for s in re.split(r"(?<=။) ", ID_RE.sub("", l)) if s]


def key(s):
    return s.replace("upādinn", "upādiṇṇ")


def head(l):
    return ID_RE.sub("", l).split(" ", 1)[1]


def pi1_dict():
    D = {}
    for p in sorted(P1P.glob("*.md")):
        for x, y in zip(p.read_text(encoding="utf-8-sig").split("\n"),
                        (P1M / p.name).read_text(encoding="utf-8").split("\n")):
            if not x.strip():
                continue
            if x.startswith("#"):
                D.setdefault(key(head(x)), set()).add(head(y))
                continue
            ps, bs = psplit(x), bsplit(y)
            if len(ps) == len(bs):
                for s, t in zip(ps, bs):
                    D.setdefault(key(s), set()).add(t)
    return D


def main(argv):
    D = pi1_dict()
    n = same = 0
    diffs = []
    for p in sorted(P2P.glob("*.md")):
        a = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        b = [l for l in (P2M / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
        ch = p.name.split("-")[0].split(".")[0]
        for i, (x, y) in enumerate(zip(a, b), 1):
            if x.startswith("#"):
                pairs, hidden = [(head(x), head(y))], False
            else:
                ps, bs = psplit(x), bsplit(y)
                if len(ps) == len(bs):
                    pairs, hidden = list(zip(ps, bs)), False
                else:
                    pairs, hidden = [(s, ID_RE.sub("", y)) for s in ps if len(s) > 25], True
            for s, t in pairs:
                k = key(s)
                if k not in D:
                    continue
                n += 1
                ok = any(u.rstrip("။") in t for u in D[k]) if hidden else t in D[k]
                if ok:
                    same += 1
                else:
                    diffs.append(f"{ch}:{i}{' (uneven line)' if hidden else ''}\n   PĀLI: {s[:150]}\n   pi-1: "
                                 f"{sorted(D[k])[0][:200]}\n   pi-2: {t[:200]}")
    print(f"pi-1 identity: {same} / {n} identical; differing: {n - same}")
    if "-q" not in argv:
        for d in diffs:
            print(d)
    return n - same


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
