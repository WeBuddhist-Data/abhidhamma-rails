"""Parenthetical notes (read-only): for Pāli lines containing REGEX inside «( … )», print each Pāli parenthesis and
the Burmese parentheses of the same line with the same index (when the counts agree), grouped by Burmese form.
usage: par7.py REGEX"""
import re, sys, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent; R = HERE.parents[3]
pd = R / "AI_translation/pali/pi-7_split_chapters"; md = R / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
rx = re.compile(sys.argv[1]); c = collections.defaultdict(list)
PAR = re.compile(r"\((?:[^()]|\([^()]*\))*\)")
for p in sorted(pd.glob("*.md")):
    for i, (x, y) in enumerate(zip(p.read_text(encoding="utf-8-sig").split("\n"), (md / p.name).read_text(encoding="utf-8").split("\n")), 1):
        xs = [m[0] for m in PAR.finditer(re.sub(r"\{[^}]*\}", "", x))]; ys = [m[0] for m in PAR.finditer(re.sub(r"\{[^}]*\}", "", y))]
        for k, s in enumerate(xs):
            if rx.search(s):
                t = ys[k] if len(xs) == len(ys) else "(counts differ) " + " ".join(ys)[:200]
                c[(s, t)].append(f"{p.name[:4]}:{i}")
for (s, t), v in sorted(c.items()):
    print(f"[{len(v)}] {sorted(set(e[:4] for e in v))} {v[:3]}\n   {s}\n   {t}")
