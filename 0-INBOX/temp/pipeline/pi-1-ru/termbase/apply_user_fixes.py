"""User approval of the pi-1 Russian termbase, 2026-11-14, with four fixes.
Replaces three lines in decisions.tsv and writes decisions-user.tsv (outside-candidate choices). Idempotent.
Then run: python -I -X utf8 0-INBOX\\temp\\pipeline\\termbase_assemble.py 1 russian ru plain
"""
import pathlib

TB = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\termbase")
WHY = "user 2026-11-14 (termbase approval)"
REPLACE = {
    "Suññataṃ|0": ("пустой", "the adjective the text uses (40x, «пустое» погружение)"),
    "ajjhattaṃ|0": ("внутри себя", "the adverb the text uses (45x)"),
    "bahiddhā|0": ("вовне", "the adverb the text uses (45x)"),
}
NEW = {
    "ujutā|0": ("прямизна", "keeps ujutā apart from ujukatā «прямота» in the string «прямота, прямизна»"),
    "asārāgo|0": ("отсутствие пристрастия", "family with sārāgo «пристрастие»"),
}

p = TB / "decisions.tsv"
out, done = [], set()
for line in p.read_text(encoding="utf-8").splitlines():
    k = line.split("\t", 1)[0]
    if k in REPLACE:
        term, why = REPLACE[k]
        line = f"{k}\t{term}\t{WHY}: {why}"
        done.add(k)
    out.append(line)
missing = set(REPLACE) - done
assert not missing, missing
p.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
(TB / "decisions-user.tsv").write_text(
    "# user decisions 2026-11-14 at termbase approval (outside the attested candidates)\n"
    + "\n".join(f"{k}\t{t}\t{WHY}: {w}" for k, (t, w) in NEW.items()) + "\n",
    encoding="utf-8", newline="\n")
print("replaced", len(done), "added", len(NEW))
