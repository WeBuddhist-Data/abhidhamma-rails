"""Consistency pass, pi-1 … pi-4 identity: every Pāli sentence (and heading) of pi-5 that also occurs in pi-1,
pi-2, pi-3 or pi-4 must have exactly their FINAL Burmese (the rails texts AI_translation/burmese/pi-{1,2,3,4}-burmese-
plain-rails_split_chapters, read only). Model: pi-4-my/harmonise_pi123.py (read only).
usage: python3 -I -X utf8 harmonise_pi1234.py [-q]
Units (all 32 pi-5 chapter files, any length):
  * headings: the heading text after the «#» marks;
  * sentences of lines whose Pāli and Burmese split into the same number of sentences (Pāli on «.» / «?» outside
    variant brackets, Burmese on «။»);
  * on lines that split unevenly: every Pāli sentence of > 25 characters that occurs in pi-1 … pi-4 must have
    one of their Burmese renderings (without its final «။») as a substring of the Burmese line (as align_hidden_my.py).
A sentence found in several books is counted for each book. A difference listed in EXPLAINED (the pi-5 Pāli context
differs on purpose, e.g. the arahant sentence said of a person, not of the Tathāgata: no honorific «တော်မူ») is
counted as «explained» when the pi-5 Burmese is exactly the final Burmese with the listed replacements applied.
Prints «pi-N identity: same / n identical (+ explained)» per book and every difference; exit 1 if any is unexplained."""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
A = ROOT / "AI_translation"
BOOKS = {b: (A / f"pali/pi-{b}_split_chapters", A / f"burmese/pi-{b}-burmese-plain-rails_split_chapters") for b in "1234"}
P4P, P4M = A / "pali/pi-5_split_chapters", A / "burmese/pi-5-burmese-plain-zeroshot_split_chapters"
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")

# Pāli sentence (start) -> (reason, [(final Burmese, pi-5 Burmese) replacements])
EXPLAINED = {
    "Natthi.": ("the answer of a speaker in the debate: the sample's answer register «…ပါ» (Āmantā «ဟုတ်ပါသည်», Na hevaṃ "
                "vattabbe «ဤသို့ မဆိုသင့်ပါ»); pi-3 «Natthi.» answers a catechism question", [("မရှိ။", "မရှိပါ။")]),
    "Katame pañca?": ("pi-4 counts persons («ယောက်»); pi-5 ch2:135 counts things (pañca dhammā): classifier «ပါး»",
                      [("ယောက်", "ပါး")]),
    "Katame tayo?": ("pi-4 counts persons («ယောက်»); pi-5 ch5:102 counts things (tayo niruttipathā): classifier «ပါး»",
                     [("ယောက်", "ပါး")]),
}


def psplit(l):
    l = ID_RE.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]


def bsplit(l):
    return [s for s in re.split(r"(?<=။) ", ID_RE.sub("", l)) if s]


def head(l):
    return ID_RE.sub("", l).split(" ", 1)[1]


def book_dict(pd, md):
    D = {}
    for p in sorted(pd.glob("*.md")):
        for x, y in zip(p.read_text(encoding="utf-8-sig").split("\n"),
                        (md / p.name).read_text(encoding="utf-8").split("\n")):
            if not x.strip():
                continue
            if x.startswith("#"):
                D.setdefault(head(x), set()).add(head(y))
                continue
            ps, bs = psplit(x), bsplit(y)
            if len(ps) == len(bs):
                for s, t in zip(ps, bs):
                    D.setdefault(s, set()).add(t)
    return D


def explained(s, finals, t, hidden):
    for k, (why, reps) in EXPLAINED.items():
        if not s.startswith(k):
            continue
        for u in finals:
            v = u
            for a, b in reps:
                v = v.replace(a, b)
            if (v.rstrip("။") in t) if hidden else (v == t):
                return why
    return None


def main(argv):
    total = 0
    for book, (pd, md) in BOOKS.items():
        D = book_dict(pd, md)
        n = same = expl = 0
        diffs, exps = [], []
        for p in sorted(P4P.glob("*.md")):
            a = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
            b = [l for l in (P4M / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
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
                    if s not in D:
                        continue
                    n += 1
                    ok = any(u.rstrip("။") in t for u in D[s]) if hidden else t in D[s]
                    if ok:
                        same += 1
                        continue
                    why = explained(s, D[s], t, hidden)
                    if why:
                        expl += 1
                        exps.append(f"{ch}:{i} {s[:90]} — {why}")
                    else:
                        diffs.append(f"{ch}:{i}{' (uneven line)' if hidden else ''}\n   PĀLI: {s[:150]}\n   pi-{book}: "
                                     f"{sorted(D[s])[0][:300]}\n   pi-5: {t[:300]}")
        print(f"pi-{book} identity: {same} / {n} identical, {expl} explained; differing: {n - same - expl}")
        if "-q" not in argv:
            for e in exps:
                print("   explained", e)
            for d in diffs:
                print(d)
        total += n - same - expl
    return total


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
