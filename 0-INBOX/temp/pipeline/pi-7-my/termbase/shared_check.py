"""Identity with pi-1 … pi-6 (brief rule 7): a pi-7 sentence (or heading) that also occurs in pi-1 … pi-6 keeps their FINAL
rails Burmese, so a term chosen here must not break it. Units and splitting as pi-7-my/harmonise_pi123456.py (its psplit /
bsplit / head / book_dict, copied, read only): headings; the sentences of evenly split lines; on unevenly split lines every
Pāli sentence of > 25 characters (the final Burmese then has to be a substring of the pi-7 line).
For every decision of raw-multi / raw-align / raw-family / raw-textinc (hw|i, term) whose headword is a word of a shared
Pāli unit: the term («…» = a gap of up to 80 characters) must occur in that unit's final Burmese in the earlier book.
With --all, every sense of the assembled termbase is checked the same way (a multi-sense headword is reported when no
sense's term fits).
Prints the units checked per decision and every conflict (a conflict is reported, never chosen against). usage: shared_check.py [--all]"""
import pathlib, re, collections, sys
H = pathlib.Path(__file__).resolve().parent
ROOT = H.parents[4]
A = ROOT / "AI_translation"
BOOKS = {b: (A / f"pali/pi-{b}_split_chapters", A / f"burmese/pi-{b}-burmese-plain-rails_split_chapters") for b in "123456"}
P7 = A / "pali/pi-7_split_chapters"
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
WORD = re.compile(r"[^\W\d_]+")


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
        for x, y in zip(p.read_text(encoding="utf-8-sig").split("\n"), (md / p.name).read_text(encoding="utf-8").split("\n")):
            if not x.strip():
                continue
            if x.startswith("#"):
                D.setdefault(head(x), set()).add(head(y)); continue
            ps, bs = psplit(x), bsplit(y)
            if len(ps) == len(bs):
                for s, t in zip(ps, bs):
                    D.setdefault(s, set()).add(t)
    return D


def units7():
    for p in sorted(P7.glob("*.md")):
        for x in p.read_text(encoding="utf-8-sig").splitlines():
            if not x.strip(): continue
            if x.startswith("#"): yield head(x); continue
            for s in psplit(x): yield s


def rx(term):
    return re.compile(r"\s*.{0,80}?\s*".join(re.escape(x.strip()) for x in term.split("…")))


def main():
    dec = []
    for f in ("raw-multi.tsv", "raw-align.tsv", "raw-family.tsv", "raw-textinc.tsv"):
        for l in (H / f).read_text(encoding="utf-8").splitlines():
            if l.strip() and not l.startswith("#"):
                k, t = l.split("\t")[:2]; dec.append((f, k, t))
    if "--all" in sys.argv:
        dec = []
        for line in (ROOT / "AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md").read_text(encoding="utf-8").splitlines():
            hw, body = line.split(": {", 1)
            dec.append(("termbase", f"{hw}|*", " | ".join(x.rsplit(": ", 1)[1] for x in body[:-1].split("; "))))
    U = set(units7())
    by_word = collections.defaultdict(set)
    for u in U:
        for w in WORD.findall(u): by_word[w.lower()].add(u)
    n_units = n_conf = 0
    lines = []
    for b, (pd, md) in BOOKS.items():
        D = book_dict(pd, md)
        for f, k, t in dec:
            hw = k.rsplit("|", 1)[0].lower()
            shared = sorted(u for u in by_word.get(hw, ()) if u in D)
            if not shared: continue
            rs = [rx(x) for x in t.split(" | ")]
            bad = [u for u in shared if not any(r.search(v) for r in rs for v in D[u])]
            n_units += len(shared); n_conf += len(bad)
            lines.append(f"pi-{b} {k} «{t}»: {len(shared) - len(bad)} / {len(shared)} shared units keep the term")
            for u in bad[:5]:
                lines.append(f"   CONFLICT  PĀLI: {u[:160]}\n             pi-{b}: {sorted(D[u])[0][:260]}")
    print("\n".join(lines))
    print(f"shared units checked {n_units}, conflicts {n_conf}")


if __name__ == "__main__":
    main()
