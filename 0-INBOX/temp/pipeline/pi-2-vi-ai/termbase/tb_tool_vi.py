# adapted 2026-11-19 from pi-1-vi-ai/termbase/tb_tool_vi.py (pi-2 paths; prior = the approved pi-1 Vietnamese termbase)
"""Lookup helper for the pi-2 Pāli→Vietnamese plain termbase (brief: ../vi-termbase-brief.md).

usage (python -I -X utf8 tb_tool_vi.py ...):
  list <from> <to> [--multi]   senses-file lines from..to (1-based, inclusive): each sense as key, tag, candidates with
                               their map counts, the decision so far (if any), and the same headword's terms in the
                               approved pi-1 Vietnamese termbase ("prior"). --multi: only senses with 2+ candidates.
  fam <regex>                  every senses-file headword matching <regex> (case-insensitive, Python re.search),
                               same display, all senses: use it to keep a lemma family on one Vietnamese word.
  prior <regex>                headwords matching <regex> in the approved pi-1 Vietnamese termbase, with their terms.
  check <from> <to>            every multi-candidate sense in lines from..to has a decision; no unknown keys; no ", ",
                               " / ", "; " in terms; lists outside-candidate choices.
  hcount <vietnamese> [...]    occurrences of each Vietnamese string in the merged pi-2 Vietnamese zero-shot translation.
  crossbook                    headwords whose pi-2 term (decision, or the single candidate) differs from every pi-1
                               term of the same headword (case-insensitive): candidates for the cross-book table.
"""
import collections, pathlib, re, sys

sys.dont_write_bytecode = True
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
SENSES = ROOT / "AI_translation/vietnamese/pi-2-pali-word-vietnamese-senses-plain.md"
AGG = ROOT / "0-INBOX/temp/pipeline/pi-2-vi-ai/senses/agg-all.tsv"
TB = ROOT / "0-INBOX/temp/pipeline/pi-2-vi-ai/termbase"
HI = ROOT / "AI_translation/vietnamese/pi-2-vietnamese-plain-zeroshot.md"
PRIOR = {1: ROOT / "AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md"}
VAL = re.compile(r"^(.*)=(\d+)\[[^\]]*\]$")


def parse(line):
    hw, body = line.split(": {", 1)
    out = []
    for s in body[:-1].split("; "):
        tag, c = s.rsplit(": ", 1)
        out.append((tag, c.split(" / ")))
    return hw, out


def senses():
    return [parse(l) for l in SENSES.read_text(encoding="utf-8").splitlines() if l.strip()]


def counts():
    c = {}
    for l in AGG.read_text(encoding="utf-8").splitlines():
        hw, _, vals, _ = l.split("\t")
        d = {}
        for item in vals.split(" | "):
            m = VAL.match(item)
            d[m.group(1).replace(" / ", " và ")] = int(m.group(2))
        c[hw] = d
    return c


def decisions():
    d = {}
    for f in sorted(TB.glob("decisions*.tsv")):
        for l in f.read_text(encoding="utf-8-sig").splitlines():
            if l.strip() and not l.startswith("#"):
                p = l.split("\t")
                d[p[0].strip()] = (p[1].strip() if len(p) > 1 else "", f.name)
    return d


_prior = None


def prior():
    global _prior
    if _prior is None:
        _prior = collections.defaultdict(list)
        for b, p in PRIOR.items():
            for l in p.read_text(encoding="utf-8").splitlines():
                if ": {" in l:
                    hw, ss = parse(l)
                    for tag, c in ss:
                        _prior[hw.lower()].append((b, tag, c[0]))
    return _prior


def show(hw, ss, cnt, dec, only_multi=False):
    pr = prior().get(hw.lower(), [])
    if only_multi and all(len(c) < 2 for _, c in ss):
        return
    for i, (tag, cands) in enumerate(ss):
        if only_multi and len(cands) < 2:
            continue
        key = f"{hw}|{i}"
        cs = " / ".join(f"{c}×{cnt.get(hw, {}).get(c, '?')}" for c in cands)
        d = f"  DECIDED: {dec[key][0]} ({dec[key][1]})" if key in dec else ""
        print(f"{key}\t{tag}\t{cs}{d}")
    for b, tag, t in pr[:6]:
        print(f"    prior pi-{b} {tag} = {t}")


def main(a):
    if len(a) >= 3 and a[0] == "list":
        ss, cnt, dec = senses(), counts(), decisions()
        for hw, s in ss[int(a[1]) - 1:int(a[2])]:
            show(hw, s, cnt, dec, "--multi" in a)
    elif len(a) == 2 and a[0] == "fam":
        rx = re.compile(a[1], re.I)
        ss, cnt, dec = senses(), counts(), decisions()
        for hw, s in ss:
            if rx.search(hw):
                show(hw, s, cnt, dec)
    elif len(a) == 2 and a[0] == "prior":
        rx = re.compile(a[1], re.I)
        for hw, v in prior().items():
            if rx.search(hw):
                print(hw, "|", " ; ".join(f"pi-{b} {tag} = {t}" for b, tag, t in v))
    elif len(a) == 3 and a[0] == "check":
        lo, hi = int(a[1]), int(a[2])
        ss, dec = senses(), decisions()
        keys = {f"{hw}|{i}": c for hw, s in ss for i, (_, c) in enumerate(s)}
        inrange = {f"{hw}|{i}": c for hw, s in ss[lo - 1:hi] for i, (_, c) in enumerate(s)}
        errs = [f"unknown key {k}" for k in dec if k not in keys]
        errs += [f"undecided multi-candidate {k}: {' / '.join(c)}" for k, c in inrange.items()
                 if len(c) > 1 and k not in dec]
        for k, (t, f) in dec.items():
            for bad in (", ", " / ", "; "):
                if bad in t:
                    errs.append(f"forbidden {bad!r} in {k}: {t}")
            if not t:
                errs.append(f"empty term {k}")
            if "—" in t or "–" in t:
                errs.append(f"dash in {k}: {t}")
        out = [(k, keys[k], t) for k, (t, f) in dec.items() if k in keys and len(keys[k]) > 1 and t not in keys[k]]
        print(f"lines {lo}-{hi}: senses {len(inrange)}, multi {sum(len(c) > 1 for c in inrange.values())}, "
              f"decisions (all files) {len(dec)}, outside-candidate {len(out)}")
        for k, c, t in out:
            print(f"  OUTSIDE {k}: {' / '.join(c)} -> {t}")
        print("\n".join(errs) if errs else "no errors")
    elif len(a) >= 2 and a[0] == "hcount":
        t = HI.read_text(encoding="utf-8")
        for h in a[1:]:
            print(f"{h}\t{t.count(h)}")
    elif len(a) == 1 and a[0] == "crossbook":
        ss, dec = senses(), decisions()
        n = 0
        for hw, s in ss:
            pr = prior().get(hw.lower())
            if not pr:
                continue
            pterms = {t for _, _, t in pr}
            for i, (tag, cands) in enumerate(s):
                key = f"{hw}|{i}"
                term = dec[key][0] if key in dec else cands[0]
                if term not in pterms:
                    n += 1
                    print(f"{key}\t{tag[:70]}\tpi-2: {term}\tpi-1: {' | '.join(sorted(pterms))}")
        print(f"{n} senses differ from every pi-1 term of the same headword")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
