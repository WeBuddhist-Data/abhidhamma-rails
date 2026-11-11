"""Check the block IDs in AI_translation/pali/pi-N-keywords-by-reference-pali-plain.md against 1-SOURCES/Text/pi-N.md.

usage: python -I -X utf8 compare_keyword_ids.py [N ...]   (read-only)
A keyword file has one line per block that has keywords: "[<id>] kw, kw, ...". Blocks without keywords
have no line, so the check is: every keyword ID exists in the root, IDs appear in root order, no ID twice.
Root blocks with no keyword line are listed for information (they may simply have no keywords).
"""
import pathlib, re, sys

BASE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
ID = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")
KW = re.compile(r"^\[([^\]]+)\]")


def check(n):
    kf = BASE / f"AI_translation/pali/pi-{n}-keywords-by-reference-pali-plain.md"
    if not kf.exists():
        print(f"pi-{n}: no keyword file")
        return True
    root = (BASE / f"1-SOURCES/Text/pi-{n}.md").read_text(encoding="utf-8")
    rid = [m.group(1) for l in root.splitlines() if (m := ID.search(l))]
    rpos = {i: k for k, i in enumerate(rid)}
    kid = [m.group(1) for l in kf.read_text(encoding="utf-8-sig").splitlines() if (m := KW.match(l))]
    unknown = [i for i in kid if i not in rpos]
    dup = sorted({i for i in kid if kid.count(i) > 1}) if len(kid) < 20000 else []
    known = [rpos[i] for i in kid if i in rpos]
    order = sum(1 for a, b in zip(known, known[1:]) if b <= a)
    nokw = [i for i in rid if i not in set(kid)]
    ok = not unknown and not dup and not order
    print(f"pi-{n}: keyword IDs {len(kid)}, root IDs {len(rid)} -> {'OK' if ok else 'STALE'}; "
          f"not in root {len(unknown)}, duplicated {len(dup)}, out of order {order}; root blocks without a keyword line {len(nokw)}")
    if unknown:
        print("    not in root:", unknown[:15])
    if dup:
        print("    duplicated:", dup[:15])
    if nokw:
        content = [i for i in nokw if not i.endswith("-0") and i != "0"]
        print(f"    root blocks without a line: {len(nokw)} ({len(content)} non-heading), e.g. {nokw[:12]}")
    return ok


books = [int(a) for a in sys.argv[1:]] or range(1, 8)
ok = [check(n) for n in books]
sys.exit(0 if all(ok) else 1)
