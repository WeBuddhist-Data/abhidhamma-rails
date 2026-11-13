"""Lookup helper for the pi-7 Pāli→Hindi plain termbase (brief: ../hi-termbase-brief.md).

usage (python -I -X utf8 tb_tool_pi6.py ...):
  list <from> <to> [--multi]   senses-file lines from..to (1-based, inclusive): each sense as key, tag, candidates with
                               their map counts, the decision so far (if any), and the same headword's terms in the
                               approved pi-1/pi-2/pi-3/pi-4/pi-5/pi-6 Hindi termbases. --multi: only senses with 2+ candidates.
  fam <regex>                  every senses-file headword matching <regex> (case-insensitive, Python re.search),
                               same display, all senses: use it to keep a lemma family on one Hindi word.
  prior <regex>                headwords matching <regex> in the pi-1/2/3/4/5/6 Hindi termbases, with their terms.
  check <from> <to>            every multi-candidate sense in lines from..to has a decision; no unknown keys; no ", ",
                               " / ", "; " in terms; lists outside-candidate choices.
  hcount <hindi> [...]         occurrences of each Hindi string in the merged pi-7 Hindi zero-shot translation.
"""
import collections, pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
SENSES = ROOT / "AI_translation/hindi/pi-7-pali-word-hindi-senses-plain.md"
AGG = ROOT / "0-INBOX/temp/pipeline/pi-7-hi/senses/agg-all.tsv"
TB = ROOT / "0-INBOX/temp/pipeline/pi-7-hi/termbase"
HI = ROOT / "AI_translation/hindi/pi-7-hindi-plain-zeroshot.md"
PRIOR = {b: ROOT / f"AI_translation/hindi/pi-{b}-pali-hindi-termbase-plain.md" for b in (1, 2, 3, 4, 5, 6)}
VAL = re.compile(r"^(.*)=(\d+)\[[^\]]*\]$")


def parse(line):
    hw, body = line.split(": {", 1)
    out = []
    for s in body[:-1].split("; "):
        tag, c = s.split(": ", 1)
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
            d[m.group(1).replace(" / ", " और ")] = int(m.group(2))
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
                        _prior[hw.lower()].append(f"pi-{b} {tag} = {c[0]}")
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
    for p in pr[:6]:
        print(f"    prior {p}")


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
                print(hw, "|", " ; ".join(v))
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
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
