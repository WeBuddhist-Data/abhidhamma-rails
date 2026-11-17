"""User approval of the pi-2 Russian termbase, 2026-11-17, "Approve with the fix".
Replaces two lines in decisions.tsv (both terms are among the attested candidates). Idempotent.
Then run: python -I -X utf8 0-INBOX\\temp\\pipeline\\termbase_assemble.py 2 russian ru plain
"""
import pathlib

TB = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\termbase")
WHY = "user 2026-11-17 (termbase approval)"
REPLACE = {
    "ajjhattaṃ|0": ("внутренний", "the form the pi-2 text uses (12 of 24) and pi-3/4/5 agree on; the pi-1 decision's own reason"),
    "bahiddhā|0": ("внешний", "the form the pi-2 text uses (27 of 28) and pi-3/4/5 agree on; pairs with ajjhattaṃ «внутренний»"),
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
print("replaced", len(done))
