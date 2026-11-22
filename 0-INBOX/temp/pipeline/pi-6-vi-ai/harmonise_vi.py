"""Consistency (harmonise) pass for the pi-6 Vietnamese plain zero-shot (Yamaka, 43 chapter files after the sample).

Adapted from pi-5-vi-ai/harmonise_vi.py (pi-5 files untouched).
Exact old -> new string replacements, each scoped to one file and one segment (block ID; "*" = every segment of the
file) and each with an asserted count of occurrences in that scope. Rules run in the order listed. Line counts, block
IDs, heading levels, dashes, ellipses and variant brackets are asserted unchanged on every changed line.
The builders are NOT rerun (harmonise-notes.md lists the builder constants that would need the same change).
Protected (user-approved sample): preamble.md, 1-mulayamaka.md: never written; asserted byte-identical with the backup.
Backup of the pre-pass files: backup-pre-harmonise/ (made once by vi_common.ensure_backup, never overwritten).
The pass always reads from the backup, so it is re-runnable: rerunning it rebuilds the same output.
Log: harmonise-log.tsv (rule, file, block id, line, old, new, reason). Decisions: harmonise-notes.md.

usage: python -I -X utf8 -B harmonise_vi.py [--dry]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PDIR, VDIR, HERE, BAK, PARTS, PROTECTED_PARTS, ID

R = []  # (rid, part, sid, old, new, count, reason)
P = {vi_common.short(p): p for p in PARTS if p[0].isdigit()}


def rule(rid, ch, sid, old, new, n, reason):
    part = P[str(ch)]
    assert old != new, (rid, old)
    R.append((rid, part, sid, old, new, n, reason))


# =============================================================== H1 asammohantena (editorial notes)
WA = ("asammohantena = «mà không mê lầm» (pi-1 sammoha «sự mê lầm», ^1-390; as 5-02 ^6-5-153 and 5-03 ^6-5-164); "
      "neither sentence needs «một cách»: the phrase follows the verb directly")
rule("H1-asammoha", "3-01", "6-3-12", "từng thuật ngữ một, không để nhầm lẫn)", "từng thuật ngữ một mà không mê lầm)", 1, WA)
rule("H1-asammoha", "6-02", "6-6-158", "phân tích một cách không nhầm lẫn,", "phân tích mà không mê lầm,", 1, WA)

# =============================================================== H2 two-part citta kinds
WC = ("AvippayuttaBvippayuttacitta = «tâm <A part> và <B part>» in the Pāli order (coordinator rule; 5-01, 5-02, "
      "10-03, 10-04); not «tâm vừa … vừa …»")
T, A = "các hiện tượng thiện", "các hiện tượng bất thiện"
for ch, sids in (("9-01", ("6-9-39", "6-9-43")), ("9-02", ("6-9-105", "6-9-109"))):
    for sid in sids:
        for x, y in ((T, A), (A, T)):
            rule("H2-citta2", ch, sid, f"tâm vừa không gắn liền với {x} vừa không gắn liền với {y}",
                 f"tâm không gắn liền với {x} và không gắn liền với {y}", 1, WC)

# =============================================================== H3 cut questions «…?» -> «… không?»
WQ = ("a question cut by …pe… / … and ending in «?» = «… không?» (sample ^6-1-98 «…nguyên nhân thiện… không?», "
      "vi-zeroshot-terms.md; 7-02 ^6-7-54); 3-01's «?…pe…» = «? …» (question complete before the cut) untouched")
CUTQ = {"3-04": 11, "3-05": 7, "3-06": 22, "5-01": 5, "5-02": 7, "5-03": 5, "6-01": 23, "6-02": 14, "8": 3}
for ch, n in CUTQ.items():
    rule("H3-cutq", ch, "*", "…?", "… không?", n, WQ)


# ------------------------------------------------------------------------------------------------- engine
def dashes(t):
    return t.count("—") + t.count("–")


def main(dry=False):
    if vi_common.ensure_backup():
        print("backup written:", BAK)
    by_part = collections.defaultdict(list)
    for r in R:
        assert r[1] not in PROTECTED_PARTS, r
        by_part[r[1]].append(r)
    log, changed, hits = [], collections.Counter(), collections.Counter()
    for part in PARTS:
        text = open(os.path.join(BAK, part + ".md"), encoding="utf-8", newline="").read()
        assert "\r" not in text and not text.startswith("﻿"), part
        if part in PROTECTED_PARTS:
            cur = open(os.path.join(VDIR, part + ".md"), encoding="utf-8", newline="").read()
            assert cur == text, (part, "sample differs from its backup")
            continue
        if part not in by_part:
            if not dry:
                open(os.path.join(VDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(text)
            continue
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        el = text.split("\n")
        idx = [i for i, l in enumerate(el) if l.strip()]
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        sid_of, cur = {}, []
        for k in range(len(idx)):
            cur.append(k)
            m = ID.search(pl[k])
            if m:
                for kk in cur:
                    sid_of[kk] = m.group(1)
                cur = []
        orig = {k: el[idx[k]] for k in range(len(idx))}
        for rid, _, sid, old, new, n, why in by_part[part]:
            ks = [k for k in range(len(idx)) if sid == "*" or sid_of.get(k) == sid]
            assert ks, (part, sid)
            got = sum(el[idx[k]].count(old) for k in ks)
            assert got == n, (rid, part, sid, f"expected {n}, found {got}", old)
            for k in ks:
                e = el[idx[k]]
                if old in e:
                    log.append((rid, part, sid_of.get(k, "?"), idx[k] + 1, old, new, why))
                    el[idx[k]] = e.replace(old, new)
            hits[rid] += got
        for k in range(len(idx)):
            e0, e = orig[k], el[idx[k]]
            if e != e0:
                assert dashes(e) == dashes(e0), (part, k, "dash count changed")
                assert ID.findall(e) == ID.findall(e0), (part, k, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k, "heading")
                assert re.findall(r"\[[^\]]*\]", e0) == re.findall(r"\[[^\]]*\]", e), (part, k, "brackets")
                assert e.count("…") == e0.count("…"), (part, k, "ellipsis")
                assert "—" not in e and ":-" not in e and "…." not in e, (part, k)
                assert "là là" not in e and "được được" not in e and "chánh niệm" not in e, (part, k)
                changed[part] += 1
        out = "\n".join(el)
        assert out.count("\n") == text.count("\n"), part
        if not dry:
            open(os.path.join(VDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(out)
    if not dry:
        with open(os.path.join(HERE, "harmonise-log.tsv"), "w", encoding="utf-8", newline="\n") as f:
            f.write("rule\tfile\tblock\tline\told\tnew\treason\n")
            for rid, part, sid, ln, old, new, why in log:
                f.write(f"{rid}\t{part}.md\t^{sid}\t{ln}\t{old}\t{new}\t{why}\n")
    for rid, n in sorted(hits.items()):
        print(f"{rid:14s} replacements={n}")
    print("lines changed per chapter:", {vi_common.short(p): n for p, n in changed.items()},
          "total", sum(changed.values()), "log entries", len(log), "(dry run)" if dry else "")


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
