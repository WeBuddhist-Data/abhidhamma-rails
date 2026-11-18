"""Consistency (harmonise) pass for the pi-1 Vietnamese plain zero-shot.

Applies fixed old -> new strings (a few regex patterns, marked rx=True) to the Vietnamese part files. A rule touches a
Vietnamese line ONLY when the aligned Pāli line (non-empty line i <-> non-empty line i) matches the rule's Pāli
pattern, and only in the parts listed for it. Line counts, block IDs, heading levels, dashes and variant brackets are
never touched (asserted per changed line).
Protected (user-approved, never changed): preamble, 1-matika, the first 122 non-empty lines of 2-01.
Backup of the pre-pass files: backup-pre-harmonise/ (made once by vi_common.ensure_backup, never overwritten).
Log: harmonise-log.tsv (rule, part, segment, line, old, new).
The pass always reads from the backup, so it is idempotent: rerunning it rebuilds the same output.

Divergence scan before the pass (find_divergences_vi.py --bak -> divergences-pre.md): 0 segment and 0 line groups
with identical Pāli and differing Vietnamese (the builders imported each other), and the recurring-term table is
uniform. The pass therefore applies the coordinator's decisions 1 and 2 only (see harmonise-notes.md).

usage: python -I -X utf8 harmonise_vi.py [--dry]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PDIR, VDIR, HERE, BAK, PARTS, PROTECTED_PARTS, PROTECTED_2_01, ID

R = []  # (id, pali_regex, old, new, is_regex, parts_prefixes or None)


def rule(rid, pali, old, new, rx=False, parts=None):
    R.append((rid, pali, old, new, rx, parts))


# =============================================================== decision 1: the rūpa answer frame (3-02 / 3-03)
# "idaṃ taṃ rūpaṃ P" = "this is that matter which is P". Old: «– đây là loại vật chất <pred>.» doubled «là» when the
# 3-01 predicate starts with «là» («… loại vật chất là lĩnh vực mắt»). New: «– vật chất này <pred>.» with the 3-01
# predicate byte-identical: «vật chất này là lĩnh vực mắt», «vật chất này thuộc phần bên trong và là phái sinh»,
# «vật chất này không do nghiệp tạo ra»; it also answers the question «Vật chất nào <pred>?» word for word.
FRAME_P = r"[Ii]daṃ taṃ rūpaṃ"
rule("D1-frame", FRAME_P, "đây là loại vật chất ", "vật chất này ", parts=["3-02", "3-03"])
rule("D1-frame", FRAME_P, "Đây là loại vật chất ", "Vật chất này ", parts=["3-02", "3-03"])

# =============================================================== decision 2: four dots
# Pāli «…pe….» (abridgement + full stop) at a line end: «….» -> «…» (as the Russian review). All 64 cases are at a
# line end (before the block ID); none lies in the protected lines.
rule("D2-four-dots", r"…pe…\s*\.", r"…\.(?=\s*(?:\^[\w-]+)?\s*$)", "…", rx=True)


# ------------------------------------------------------------------------------------------------- engine
def dashes(t):
    return t.count("—") + t.count("–")


def main(dry=False):
    made = vi_common.ensure_backup()
    if made:
        print("backup written:", BAK)
    log = []
    tot = collections.Counter()
    changed = collections.Counter()
    hit = set()
    blocked = []
    comp = [(rid, re.compile(p), old, new, rx, parts) for rid, p, old, new, rx, parts in R]
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        text = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        assert "\r" not in text and not text.startswith("﻿"), part
        el = text.split("\n")
        idx = [i for i, l in enumerate(el) if l.strip()]
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        sid_of = {}
        cur = []
        for k, li in enumerate(idx):
            cur.append(k)
            m = ID.search(pl[k])
            if m:
                for kk in cur:
                    sid_of[kk] = m.group(1)
                cur = []
        for k, li in enumerate(idx):
            p, e0 = pl[k], el[li]
            e = e0
            for ri, (rid, pr, old, new, rx, parts) in enumerate(comp):
                if parts and not any(part.startswith(x) for x in parts):
                    continue
                if not pr.search(p):
                    continue
                if rx:
                    e2, n = re.subn(old, new, e)
                    if e2 == e:
                        n = 0
                else:
                    n = e.count(old)
                    e2 = e.replace(old, new)
                if n:
                    hit.add(ri)
                    if part in PROTECTED_PARTS or (part.startswith("2-01") and k < PROTECTED_2_01):
                        blocked.append((rid, part, k + 1))
                        continue
                    log.append((rid, part, sid_of.get(k, "?"), k + 1, e, e2))
                    tot[(rid, part)] += n
                    e = e2
            if e != e0:
                assert dashes(e) == dashes(e0), (part, k, "dash count changed", e)
                assert ID.findall(e) == ID.findall(e0), (part, k, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k, "heading")
                assert re.findall(r"\[[^\]]*\]", e) == re.findall(r"\[[^\]]*\]", e0), (part, k, "brackets")
                assert e.count("…") == e0.count("…"), (part, k, "ellipsis count")
                assert "—" not in e and ":-" not in e, (part, k)
                el[li] = e
                changed[part] += 1
        out = "\n".join(el)
        assert out.count("\n") == text.count("\n"), part
        if not dry:
            open(os.path.join(VDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(out)
    if not dry:
        with open(os.path.join(HERE, "harmonise-log.tsv"), "w", encoding="utf-8", newline="\n") as f:
            f.write("rule\tpart\tsegment\tline\told\tnew\n")
            for rid, part, sid, ln, old, new in log:
                f.write(f"{rid}\t{part}\t^{sid}\t{ln}\t{old}\t{new}\n")
    per = collections.defaultdict(dict)
    for (rid, part), n in tot.items():
        per[rid][part[:4]] = n
    for rid in sorted(per):
        print(f"{rid:16s} total={sum(per[rid].values()):4d} | " + ", ".join(f"{p}={n}" for p, n in sorted(per[rid].items())))
    print("lines changed per part:", dict(changed), "total", sum(changed.values()), "(dry run)" if dry else "")
    if blocked:
        print("BLOCKED (protected lines a rule would have changed):", blocked)
    for ri, r in enumerate(R):
        if ri not in hit:
            print("NO HIT:", r[0], "|", str(r[2])[:90])


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
