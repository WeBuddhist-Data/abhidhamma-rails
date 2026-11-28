"""Coordinator cleanup of the pi-6 Russian keyword map (2026-11-27). Idempotent; logs every change to cleanup-log.tsv.

1. parijānāti family: one value per tense whatever the word order of the segment. The negated sentences say
   «не понимает полностью» (pi-5 rule: never «не полностью понимает»), the positive ones «полностью понимает»;
   the keyword is the same verb, so the value is «полностью понимать» / «полностью понять» everywhere
   (G2 / G7 / G10b had «понимать полностью» / «понять полностью» on the negated segments).
Everything else in crosscheck-values.tsv follows the text by design (rūpaṃ форма / материальная форма, dukkhaṃ боль /
страдание, Pacchimabhavikānaṃ, the «… ума» moments, the (14) past-time «момент возникновения»).
usage: python -I -X utf8 -B cleanup_map_ru.py [--dry]
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
RULES = [
    (re.compile(r"^parijān|^Parijān"), re.compile(r"^(не )?понимать полностью$"), lambda m: (m.group(1) or "") + "полностью понимать"),
    (re.compile(r"^parijān|^Parijān"), re.compile(r"^(не )?понять полностью$"), lambda m: (m.group(1) or "") + "полностью понять"),
]


def main():
    dry = "--dry" in sys.argv
    log = []
    for mf in sorted(HERE.glob("*.mapped.md")):
        out, changed = [], False
        for line in mf.read_text(encoding="utf-8").splitlines():
            if "] " not in line:
                out.append(line); continue
            head, body = line.split("] ", 1)
            items = []
            for it in body.split(", "):
                k, v = it.split("=", 1)
                for kre, vre, fix in RULES:
                    m = vre.match(v)
                    if kre.search(k) and m:
                        nv = fix(m)
                        log.append((mf.stem.replace(".mapped", ""), head[1:], k, v, nv))
                        v, changed = nv, True
                        break
                items.append(f"{k}={v}")
            out.append(f"{head}] " + ", ".join(items))
        if changed and not dry:
            mf.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    if not dry and log:
        with open(HERE / "cleanup-log.tsv", "a", encoding="utf-8", newline="\n") as f:
            for row in log:
                f.write("\t".join(row) + "\n")
    print("changes:", len(log))
    for row in log[:12]:
        print("  ", *row)


if __name__ == "__main__":
    main()
