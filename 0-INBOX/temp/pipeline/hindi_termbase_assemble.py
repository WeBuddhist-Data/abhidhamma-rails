"""Assemble a Pāli→Hindi plain termbase (termbase-builder) from the senses file plus decision files.

usage: python -I -X utf8 hindi_termbase_assemble.py <book number>

Senses:    AI_translation/hindi/pi-N-pali-word-hindi-senses-plain.md   (hw: {tag: a / b; tag2: c})
Decisions: 0-INBOX/temp/pipeline/pi-N-hi/termbase/decisions*.tsv, lines  hw|sense_index <TAB> term <TAB> reason
           (sense_index is 0-based, in the senses file's order; blank lines and lines starting with # ignored)
Rules:
  - single-candidate sense, no decision      -> keep the candidate
  - multi-candidate sense                     -> MUST have exactly one decision
  - a decision on a single-candidate sense    -> allowed (family alignment); listed as ALIGNED
  - a decision term not among the candidates  -> allowed; listed as OUTSIDE for the user's approval
Output: AI_translation/hindi/pi-N-pali-hindi-termbase-plain.md (hw: {tag: term; tag2: term})
Report: 0-INBOX/temp/pipeline/pi-N-hi/termbase/termbase-decisions.md
Checks: same headwords and sense tags as the senses file; one term per sense; no ", " / " / " / "; " inside a term;
        every decision used exactly once; no duplicate decisions.
"""
import pathlib, sys

BOOK = sys.argv[1]
BASE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
SENSES = BASE / f"AI_translation/hindi/pi-{BOOK}-pali-word-hindi-senses-plain.md"
TB = BASE / f"0-INBOX/temp/pipeline/pi-{BOOK}-hi/termbase"
OUT = BASE / f"AI_translation/hindi/pi-{BOOK}-pali-hindi-termbase-plain.md"
REPORT = TB / "termbase-decisions.md"

dec, errs = {}, []
for f in sorted(TB.glob("decisions*.tsv")):
    for n, line in enumerate(f.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            errs.append(f"{f.name}:{n} malformed"); continue
        key, term = parts[0].strip(), parts[1].strip()
        why = parts[2].strip() if len(parts) > 2 else ""
        if key in dec:
            errs.append(f"duplicate decision {key} ({f.name}:{n})")
        dec[key] = (term, why, f.name)

out, multi_rows, aligned_rows, outside_rows, used = [], [], [], [], set()
n_hw = n_sense = n_single = 0
for line in SENSES.read_text(encoding="utf-8-sig").splitlines():
    if not line.strip():
        continue
    hw, body = line.split(": {", 1)
    assert body.endswith("}"), line[:80]
    senses = body[:-1].split("; ")
    n_hw += 1
    chosen = []
    for i, s in enumerate(senses):
        n_sense += 1
        tag, cands = s.split(": ", 1)
        cl = [c.strip() for c in cands.split(" / ")]
        key = f"{hw}|{i}"
        if key in dec:
            term, why, src = dec[key]; used.add(key)
            if len(cl) == 1:
                aligned_rows.append(f"{hw} | {tag} | {cl[0]} → {term} | {why}")
            else:
                multi_rows.append(f"{hw} | {tag} | {' / '.join(cl)} → {term} | {why}")
            if len(cl) > 1 and term not in cl:
                outside_rows.append(f"{hw} | {tag} | candidates: {' / '.join(cl)} | chosen: {term} | {why}")
        elif len(cl) == 1:
            term = cl[0]; n_single += 1
        else:
            errs.append(f"undecided multi-candidate sense {key}: {cands}"); term = cl[0]
        for bad in (", ", " / ", "; "):
            if bad in term:
                errs.append(f"forbidden '{bad}' in term {key}: {term}")
        if not term:
            errs.append(f"empty term {key}")
        chosen.append(f"{tag}: {term}")
    out.append(f"{hw}: {{{'; '.join(chosen)}}}")

unused = sorted(set(dec) - used)
errs += [f"decision for unknown sense {k}" for k in unused]
if errs:
    print("\n".join(errs[:40])); print(f"{len(errs)} errors"); sys.exit(1)

OUT.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
REPORT.write_text(
    f"# pi-{BOOK} Pāli→Hindi plain termbase: decision report\n\n"
    f"Headwords {n_hw}, senses {n_sense}; single-candidate kept {n_single}; multi-candidate decided {len(multi_rows)}; "
    f"single-candidate re-aligned {len(aligned_rows)}; chosen outside the candidates {len(outside_rows)}.\n\n"
    "## Chosen outside the attested candidates (needs approval)\n\npali | sense | candidates | chosen | reason\n---|---|---|---|---\n"
    + "\n".join(outside_rows) + "\n\n## Multi-candidate decisions\n\npali | sense | candidates → chosen | reason\n---|---|---|---\n"
    + "\n".join(multi_rows) + "\n\n## Single-candidate senses re-aligned for consistency\n\npali | sense | before → after | reason\n---|---|---|---\n"
    + "\n".join(aligned_rows) + "\n", encoding="utf-8", newline="\n")
print(f"pi-{BOOK}: headwords {n_hw} senses {n_sense} | single {n_single} | multi {len(multi_rows)} | aligned {len(aligned_rows)} "
      f"| outside {len(outside_rows)} | no errors -> {OUT.name}")
