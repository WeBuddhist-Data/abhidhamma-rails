"""User decisions 2026-11-14 after the pi-7 rails review, carried into the termbase:
U1 triad/dyad names (review/names-change.tsv: old → new, substring replacement inside any term),
U3 sahajāto = «साथ उत्पन्न होकर» (and «साथ जन्म लेना» → «साथ उत्पन्न होना»),
niṭṭhitesu = «समाप्त हो जाना» (the review fix «महाभूतों का अंश समाप्त हो जाने पर»).
Updates or appends decisions in decisions.tsv; then re-run hindi_termbase_assemble.py 7.
"""
import pathlib

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TBF = ROOT / "AI_translation/hindi/pi-7-pali-hindi-termbase-plain.md"
DEC = ROOT / "0-INBOX/temp/pipeline/pi-7-hi/termbase/decisions.tsv"
NAMES = ROOT / "0-INBOX/temp/pipeline/pi-7-hi/review/names-change.tsv"
WHY = "user 2026-11-14 after the rails review"

pairs = []
for line in NAMES.read_text(encoding="utf-8").splitlines()[1:]:
    p = line.split("\t")
    if len(p) >= 3 and p[1] and p[1] != p[2]:
        pairs.append((p[1], p[2]))
pairs += [("साथ जन्म लेकर", "साथ उत्पन्न होकर"), ("साथ जन्म लेना", "साथ उत्पन्न होना")]
pairs.sort(key=lambda x: -len(x[0]))
special = {"niṭṭhitesu": "समाप्त हो जाना"}

targets = {}
for line in TBF.read_text(encoding="utf-8").splitlines():
    if ": " not in line:
        continue
    hw, body = line.split(": ", 1)
    senses = body.strip()[1:-1].split("; ")
    for i, s in enumerate(senses):
        term = s.split(": ", 1)[1]
        new = special.get(hw, term) if i == 0 and hw in special else term
        for old, rep in pairs:
            if old in new:
                new = new.replace(old, rep)
        if new != term:
            targets[f"{hw}|{i}"] = new

out, done = [], set()
for line in DEC.read_text(encoding="utf-8").splitlines():
    parts = line.split("\t")
    if not line.startswith("#") and len(parts) >= 2 and parts[0] in targets:
        parts[1] = targets[parts[0]]
        parts = parts[:2] + [(parts[2] + "; " if len(parts) > 2 and parts[2] else "") + WHY]
        done.add(parts[0])
        line = "\t".join(parts)
    out.append(line)
out += [f"{k}\t{v}\t{WHY}" for k, v in targets.items() if k not in done]
DEC.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("senses changed", len(targets), "updated", len(done), "appended", len(targets) - len(done))
