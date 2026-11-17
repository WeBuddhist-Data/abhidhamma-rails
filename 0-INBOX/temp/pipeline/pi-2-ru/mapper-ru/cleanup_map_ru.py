"""Coordinator cleanup of the pi-2 Russian keyword map (2026-11-16). Idempotent; logs to cleanup-log.tsv.
User rule (pi-1 sample review): non-word fragments, bare prepositions/particles and keywords with no word of their own
in the Russian = (no direct equivalent).
- Handāhaṃ «-ка я» (a particle suffix, not a word) -> NDE
- ādhigaccha «благодаря» (a preposition, from «благодаря даянию») -> NDE
- nigghosaṃ «шумный» (cut from «бесшумное»; the parallel saddaṃ in «тихое» is already NDE) -> NDE
Checks after this run: crosscheck_map_ru.py (structure, identical-segment conflicts), strict_presence_ru.py (no exception
lists: 474 occurrences of 134 kw=value pairs, all inflection the checker cannot match; reviewed by the coordinator).
"""
import pathlib

D = pathlib.Path(__file__).resolve().parent
NDE = "(no direct equivalent)"
RULES = {"Handāhaṃ": {"-ка я": NDE}, "ādhigaccha": {"благодаря": NDE}, "nigghosaṃ": {"шумный": NDE}}
log = []
for p in sorted(D.glob("*.mapped.md")):
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if "] " in line:
            head, body = line.split("] ", 1)
            items = []
            for it in body.split(", "):
                k, v = it.split("=", 1)
                nv = RULES.get(k, {}).get(v, v)
                if nv != v:
                    log.append(f"{p.stem}\t{head[1:]}\t{k}\t{v}\t{nv}")
                items.append(f"{k}={nv}")
            line = head + "] " + ", ".join(items)
        out.append(line)
    p.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
(D / "cleanup-log.tsv").write_text("part\tid\tkeyword\told\tnew\n" + "\n".join(log) + "\n", encoding="utf-8", newline="\n")
print("changes", len(log))
