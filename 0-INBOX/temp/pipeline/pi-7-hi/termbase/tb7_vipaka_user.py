"""User decision 2026-11-13: vipāka = «कर्म-फल रूपी» everywhere in pi-7 (not «कर्म के फल रूपी»).

Rewrites every termbase sense whose term contains «कर्म के फल रूपी»: updates its line in decisions.tsv,
or appends a decision when the sense had none. Then re-run hindi_termbase_assemble.py 7.
"""
import pathlib, re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TBF = ROOT / "AI_translation/hindi/pi-7-pali-hindi-termbase-plain.md"
DEC = ROOT / "0-INBOX/temp/pipeline/pi-7-hi/termbase/decisions.tsv"
OLD, NEW = "कर्म के फल रूपी", "कर्म-फल रूपी"
WHY = "user 2026-11-13: vipāka = कर्म-फल रूपी everywhere"

targets = {}
for line in TBF.read_text(encoding="utf-8").splitlines():
    if OLD not in line:
        continue
    hw, body = line.split(": ", 1)
    senses = body.strip()[1:-1].split("; ")
    for i, s in enumerate(senses):
        term = s.split(": ", 1)[1] if ": " in s else s
        if OLD in term:
            targets[f"{hw}|{i}"] = term.replace(OLD, NEW)

out, done = [], set()
for line in DEC.read_text(encoding="utf-8").splitlines():
    parts = line.split("\t")
    if not line.startswith("#") and len(parts) >= 2 and parts[0] in targets:
        parts[1] = targets[parts[0]]
        parts[2] = (parts[2] + "; " if len(parts) > 2 and parts[2] else "") + WHY
        done.add(parts[0])
        line = "\t".join(parts)
    out.append(line)
for k, v in targets.items():
    if k not in done:
        out.append(f"{k}\t{v}\t{WHY}")
DEC.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("senses changed", len(targets), "updated", len(done), "appended", len(targets) - len(done))
