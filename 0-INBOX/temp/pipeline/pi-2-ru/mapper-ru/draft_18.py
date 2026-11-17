"""Drafting / review helper for chapter 18 (not the map builder).
For each keyword: the map_18_ru resolver value; where it is missing or not present in the segment's Russian, the
values of the approved pi-1 / pi-4 / pi-2 ch1-17 / pi-5 / pi-3 maps (by frequency) that ARE present are suggested.
usage: python -I -X utf8 draft_18.py [--miss] [--ru] [id ...]     (--ru also prints the Russian segment)
       python -I -X utf8 draft_18.py --cands kw [kw ...]
       python -I -X utf8 draft_18.py --diff [pi1|pi4|pi2]          (ch18 values that differ from a prior value
                                                                    also present in the segment)"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map_18_ru as M  # noqa: E402
from map_common_pi2_ru import NDE, lc, present, read_keywords, read_russian  # noqa: E402

ROOT = HERE.parents[4]
RU = ROOT / "AI_translation" / "russian"


def _load(path, tag, store):
    for line in path.read_text(encoding="utf-8").splitlines():
        if "] " not in line:
            continue
        for pair in line.split("] ", 1)[1].split(", "):
            if "=" in pair:
                k, v = pair.split("=", 1)
                store[lc(k)][(tag, v)] += 1


PRIOR = collections.defaultdict(collections.Counter)
for n in (1, 4, 5, 3):
    _load(RU / f"pi-{n}-keywords-by-reference-pali-russian-plain.md", f"pi{n}", PRIOR)
for p in sorted(HERE.glob("*.mapped.md")):
    if not p.name.startswith("18-"):
        _load(p, "pi2", PRIOR)
ORDER = {"pi1": 0, "pi4": 1, "pi2": 2, "pi5": 3, "pi3": 4}


def prior(kw):
    out = []
    for (tag, v), n in sorted(PRIOR[lc(kw)].items(), key=lambda x: (ORDER[x[0][0]], -x[1])):
        if v not in out:
            out.append(v)
    return out


def diff(tags):
    ru, res = read_russian(M.PART), M.resolver()
    seen = set()
    for bid, kws in read_keywords(M.PART):
        for kw in kws:
            v = res(bid, kw, kws)
            alts = [(t, pv, n) for (t, pv), n in PRIOR[lc(kw)].items()
                    if t in tags and pv != v and pv != NDE and present(pv, ru.get(bid, ""))]
            if alts and (kw, v) not in seen:
                seen.add((kw, v))
                print(f"{bid}\t{kw}={v}\t<- " + " | ".join(f"{t}:{pv}({n})" for t, pv, n in
                                                         sorted(alts, key=lambda x: -x[2])))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["--cands"]:
        for k in args[1:]:
            print(k, "->", " | ".join(f"{t}:{v}({n})" for (t, v), n in
                                      sorted(PRIOR[lc(k)].items(), key=lambda x: (ORDER[x[0][0]], -x[1]))[:10]))
        sys.exit()
    if args[:1] == ["--diff"]:
        diff(set(args[1:]) or {"pi1", "pi4", "pi2"})
        sys.exit()
    only_miss, show_ru = "--miss" in args, "--ru" in args
    ids = [a for a in args if not a.startswith("--")]
    ru, res = read_russian(M.PART), M.resolver()
    allowed = M.allowed()
    for bid, kws in read_keywords(M.PART):
        if ids and bid not in ids:
            continue
        text = ru.get(bid, "")
        outs = []
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            ok = v != "???" and (v == NDE or present(v, text) or (bid, kw) in allowed)
            if ok and only_miss:
                continue
            sug = "" if ok else "  !! " + " | ".join(p for p in prior(kw) if p != NDE and present(p, text))
            outs.append(f"{kw}={v}{sug}")
        if outs:
            print(f"[{bid}]" + (f"\n  RU: {text}" if show_ru else ""))
            for o in outs:
                print("   ", o)
