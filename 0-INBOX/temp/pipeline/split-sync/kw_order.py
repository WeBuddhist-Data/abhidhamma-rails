import pathlib, re
B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
ID = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$"); KW = re.compile(r"^\[([^\]]+)\]")
for n in (1, 3, 4, 5, 6, 7):
    rid = [m.group(1) for l in (B / f"1-SOURCES/Text/pi-{n}.md").read_text(encoding="utf-8").splitlines() if (m := ID.search(l))]
    rpos = {i: k for k, i in enumerate(rid)}
    kid = [m.group(1) for l in (B / f"AI_translation/pali/pi-{n}-keywords-by-reference-pali-plain.md").read_text(encoding="utf-8-sig").splitlines() if (m := KW.match(l))]
    bad = [(kid[k], kid[k + 1]) for k in range(len(kid) - 1) if rpos[kid[k + 1]] <= rpos[kid[k]]]
    print(f"pi-{n}", bad[:6])
    if n == 7:
        nok = [i for i in rid if i not in set(kid) and not i.endswith("-0")]
        print("  pi-7 non-heading without line:", nok)
