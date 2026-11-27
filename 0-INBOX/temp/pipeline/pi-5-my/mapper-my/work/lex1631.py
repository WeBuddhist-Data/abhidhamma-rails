"""a Pāli -> Burmese lexicon from the NEW tables listed in the zero-shot notes (notes-ch*.md, this track's own words):
single forms only; prints how many unmapped keywords of the group it would resolve (by presence)."""
import sys, pathlib, re, collections
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map5_rules as R

def lexicon():
    lex = collections.defaultdict(list)
    for f in sorted(HERE.parent.glob("notes-ch*.md")):
        for l in f.read_text(encoding="utf-8").splitlines():
            if not l.startswith("- ") or " = " not in l:
                continue
            p, b = l[2:].split(" = ", 1)
            p = re.sub(r"\s*\([^)]*\)", "", p).strip().rstrip(".?!").strip()
            p = re.sub(r"^\(\d+\)\s*\d+\.\s*", "", p)
            b = re.sub(r"^\(\d+\)\s*\d+\.\s*", "", b.strip())
            b = re.sub(r"\s*\((?=[^)]*[A-Za-z])[^()]*\)\s*$", "", b).rstrip("။").strip()
            if not p or not b or "…" in p or re.search(r"\b[PQXY]\b|X-|-X", p) or len(p.split()) > 4:
                continue
            for bb in b.split(" / "):
                if "၊" in bb or "⟦" in bb or re.search(r"[A-Za-z]", bb):
                    continue
                lex[R.low(p)].append(bb.strip())
    return lex

if __name__ == "__main__":
    lex = lexicon()
    print("entries", len(lex))
    for l in sys.argv[1:]:
        print(l, lex.get(R.low(l)))
