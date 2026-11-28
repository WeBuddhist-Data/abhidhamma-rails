"""Coordinator fix for the pi-6 Russian rails (2026-11-28): a full stop at a closing bracket goes where the Pāli has
it. The rails groups wrote «(Круг следует замкнуть.)» where the Pāli has «(Cakkaṃ bandhitabbaṃ).» (user rule:
punctuation as written; the zero-shot and pi-5 «(Сокращено).» keep the Pāli placement).

Per line: the sentence-level closing brackets «).» / «.)» followed by a space or the line end (sigla such as
«(sī.)]» or «(Sī.):» are not followed by a space, so they are skipped) are listed in order for the Pāli and the
Russian; when both lists have the same length, a Russian «.)» whose Pāli partner is «).» becomes «).» and the
reverse. Lines whose lists differ in length are only reported. Idempotent. Re-run after any rails builder.
usage: python -I -X utf8 -B rails_paren_stop_fix.py [--dry]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / "AI_translation/pali/pi-6_split_chapters"
RDIR = ROOT / "AI_translation/russian/pi-6-russian-plain-rails_split_chapters"
END = re.compile(r"(\)\.|\.\))(?=\s|$)")


def kinds(s):
    return [(m.start(), "out" if m.group(1) == ")." else "in") for m in END.finditer(s)]


def main():
    dry = "--dry" in sys.argv
    fixed, skipped, files = 0, [], 0
    for pf in sorted(PDIR.glob("*.md")):
        rf = RDIR / pf.name
        praw = pf.read_text(encoding="utf-8").split("\n")
        rraw = rf.read_text(encoding="utf-8").split("\n")
        pidx = [i for i, l in enumerate(praw) if l.strip()]
        ridx = [i for i, l in enumerate(rraw) if l.strip()]
        assert len(pidx) == len(ridx), pf.name
        changed = False
        for pi, ri in zip(pidx, ridx):
            pk, rk = kinds(praw[pi]), kinds(rraw[ri])
            if not pk and not rk:
                continue
            bare = re.findall(r"[^.\s]\)(?=\s|$)", praw[pi])
            if not pk and rk and len(bare) == len(rk) and all(k == "in" for _, k in rk):
                # the Pāli note has no full stop at all («(Cakkaṃ bandhitabbaṃ) ^id»): none in the Russian either
                rraw[ri] = END.sub(lambda m: ")", rraw[ri])
                fixed += len(rk)
                changed = True
                continue
            if len(pk) != len(rk):
                skipped.append(f"{pf.stem}:{ri + 1} pali {[k for _, k in pk]} ru {[k for _, k in rk]}")
                continue
            line = list(rraw[ri])
            for (_, want), (pos, have) in zip(pk, rk):
                if want != have:
                    line[pos:pos + 2] = list(").") if want == "out" else list(".)")
                    fixed += 1
                    changed = True
            rraw[ri] = "".join(line)
        if changed:
            files += 1
            if not dry:
                rf.write_text("\n".join(rraw), encoding="utf-8", newline="\n")
    print(f"fixed {fixed} in {files} files; lines with a different count (reported only): {len(skipped)}")
    for s in skipped[:40]:
        print("  ", s)


if __name__ == "__main__":
    main()
