# -*- coding: utf-8 -*-
"""Stage-1 review fixes, part r4 (7-09, 7-10, 7-11, 8, 9-01, 9-02, 9-03, 10-01, 10-02).

Rules applied (vi-review-fixes-brief.md): F1 (8-cittayamaka Atikkantakala section), F3 (nirodhasamapannanam
«đang nhập»), F4 ("no ca" + uppajjati / nirujjhati: negation on the verb), F9 (hettha «xuống cõi thấp hơn").
Builds from rails/backup-pre-review/<ch> (made once from the current chapter, never overwritten), so it can be
re-run. Rewrites rails/review-fixes-log-r4.tsv each run.

Run: python -I -X utf8 -B review_fixes_r4_vi.py [--dry]
"""
import os
import re
import shutil
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
VI_DIR = os.path.join(ROOT, "AI_translation", "vietnamese", "pi-6-vietnamese-plain-rails_split_chapters")
PI_DIR = os.path.join(ROOT, "AI_translation", "pali", "pi-6_split_chapters")
BACKUP = os.path.join(HERE, "backup-pre-review")
LOG = os.path.join(HERE, "review-fixes-log-r4.tsv")

CHAPTERS = [
    "7-09-anusayayamaka.md", "7-10-anusayayamaka.md", "7-11-anusayayamaka.md", "8-cittayamaka.md",
    "9-01-dhammayamaka.md", "9-02-dhammayamaka.md", "9-03-dhammayamaka.md",
    "10-01-indriyayamaka.md", "10-02-indriyayamaka.md",
]
DRY = "--dry" in sys.argv


def read(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


# ---------------------------------------------------------------- F1 frames
MOMENT = {"u": "sinh khởi", "n": "chấm dứt"}


def f1_old(lead, tail, neg, m1, m2):
    pol = "chưa vượt khỏi" if neg else "đã vượt khỏi"
    th = "không thuộc thời đã qua" if neg else "thuộc thời đã qua"
    return (f"{lead}{pol} khoảnh khắc đang {MOMENT[m1]}, khoảnh khắc ấy {th}, "
            f"{pol} khoảnh khắc đang {MOMENT[m2]}, khoảnh khắc ấy {th}, thì có phải đó là {tail} không?")


def f1_new(lead, resum, subj, neg, m1, m2):
    pol = "chưa vượt qua" if neg else "đã vượt qua"
    th = "chưa thuộc thời đã qua" if neg else "đã thuộc thời đã qua"
    return (f"{lead}{pol} khoảnh khắc {MOMENT[m1]} và {th}, "
            f"thì {resum}có phải {subj} cũng {pol} khoảnh khắc {MOMENT[m2]} và {th} không?")


# frame: (label, [(lead_a, lead_b)], old tail, resumptive, subject)
F1_FRAMES = [
    ("person (yassa cittam … tassa cittam)", ("(a) Ở người nào mà tâm ", "(b) Còn ở người nào mà tâm "),
     "tâm của người ấy", "ở người ấy ", "tâm"),
    ("dhamma (yam cittam … tam cittam)", ("(a) Tâm nào ", "(b) Còn tâm nào "),
     "tâm ấy", "", "tâm ấy"),
    ("person + dhamma (yassa yam cittam … tassa tam cittam)",
     ("(a) Ở người nào mà tâm nào ", "(b) Còn ở người nào mà tâm nào "),
     "tâm ấy của người ấy", "ở người ấy ", "tâm ấy"),
]
# occurrences in 8: person ^6-8-20 + ^6-8-83 (2), dhamma ^6-8-40 + ^6-8-104 (2), person+dhamma ^6-8-60 (1)
F1_COUNT = {0: 2, 1: 2, 2: 1}

F1_RULES = []  # (old, new, count, label)
F1_WORDINGS = []
for i, (label, (la, lb), tail, resum, subj) in enumerate(F1_FRAMES):
    for neg in (False, True):
        for lead, m1, m2 in ((la, "u", "n"), (lb, "n", "u")):
            old = f1_old(lead, tail, neg, m1, m2)
            new = f1_new(lead, resum, subj, neg, m1, m2)
            F1_RULES.append((old, new, F1_COUNT[i], label))
            F1_WORDINGS.append((label, new))

F1_ANSWERS = [
    ("Tâm vào khoảnh khắc tan rã đã vượt khỏi khoảnh khắc sinh khởi mà chưa vượt khỏi khoảnh khắc tan rã, "
     "tâm thuộc quá khứ đã vượt khỏi khoảnh khắc sinh khởi và đã vượt khỏi khoảnh khắc tan rã.",
     "Tâm vào khoảnh khắc tan rã đã vượt qua khoảnh khắc sinh khởi mà chưa vượt qua khoảnh khắc tan rã, "
     "tâm thuộc quá khứ đã vượt qua khoảnh khắc sinh khởi và đã vượt qua khoảnh khắc tan rã.", 2, "answer"),
    ("Tâm vào khoảnh khắc sinh khởi, tâm thuộc tương lai.",
     "Tâm vào khoảnh khắc sinh khởi và tâm thuộc tương lai.", 2, "answer"),
    ("Tâm vào khoảnh khắc tan rã chưa vượt khỏi khoảnh khắc tan rã nhưng đã từng vượt khỏi khoảnh khắc sinh khởi, "
     "tâm vào khoảnh khắc sinh khởi và tâm thuộc tương lai chưa vượt khỏi khoảnh khắc tan rã và chưa vượt khỏi "
     "khoảnh khắc sinh khởi.",
     "Tâm vào khoảnh khắc tan rã chưa vượt qua khoảnh khắc tan rã nhưng đã vượt qua khoảnh khắc sinh khởi, "
     "tâm vào khoảnh khắc sinh khởi và tâm thuộc tương lai chưa vượt qua khoảnh khắc tan rã và chưa vượt qua "
     "khoảnh khắc sinh khởi.", 2, "answer"),
]
F1_LEFT = ["vượt khỏi", "khoảnh khắc đang sinh khởi", "khoảnh khắc đang chấm dứt", "khoảnh khắc ấy thuộc",
           "khoảnh khắc ấy không thuộc", "thì có phải đó là tâm", "đã từng vượt"]

# ---------------------------------------------------------------- F3
F3_OLD = "người nhập thành tựu thiền chấm dứt"
F3_NEW = "người đang nhập thành tựu thiền chấm dứt"
F3_COUNT = {"8-cittayamaka.md": 16, "9-01-dhammayamaka.md": 11, "9-02-dhammayamaka.md": 13,
            "9-03-dhammayamaka.md": 9}

# ---------------------------------------------------------------- F9
F9_OLD = "xuống phía dưới"
F9_NEW = "xuống cõi thấp hơn"
F9_COUNT = {"7-11-anusayayamaka.md": 4}

# ---------------------------------------------------------------- F4
PRON = r"nhưng ở (?:những người ấy|người ấy|nơi ấy)(?:, ở nơi ấy)?"
VERB = r"(?P<t>đã |sẽ |đang |ở trạng thái đã )?(?P<v>sinh khởi|chấm dứt)(?=[,.;:?!) ]|$)"
F4_SINGLE = re.compile(r"(?P<p>" + PRON + r") không có (?P<x>[^.,;]+?) " + VERB)
F4_NEITHER = re.compile(r"(?P<p>" + PRON + r") không có (?P<x>[^.,;]+?), cũng không có (?P<y>[^.,;]+?) " + VERB)
# participle: the chapter's own na-uppajjamāna / no-ca form «không phải đang …» (family D; 8 dhamma-frame answers
# «nhưng tâm ấy không phải đang sinh khởi»), not the brief's example «không đang …»: reported
NEG = {None: "không ", "đã ": "chưa từng ", "sẽ ": "sẽ không ", "đang ": "không phải đang ",
       "ở trạng thái đã ": "không ở trạng thái đã "}
F4_BROAD = re.compile(r"nhưng [^.,;]*?không có [^.,;]*?(?:sinh khởi|chấm dứt)")
F4_NAME = {None: "F4 present", "đã ": "F4 past", "sẽ ": "F4 future", "đang ": "F4 participle đang",
           "ở trạng thái đã ": "F4 participle uppanna"}
F4_LEFT = re.compile(r"không có [^.,;]+? (?:đã |sẽ |đang |ở trạng thái đã )?(?:sinh khởi|chấm dứt)(?=[,.;:?!) ]|$)")
# Pali "no ca" clause with a positive uppajjati / nirujjhati / uppanna / niruddha / -mana
PI_NOCA = re.compile(r"no ca ([^.,;?]*)")
PI_VERB = re.compile(r"(?<![a-zāīūṃṅñṭḍṇḷ])(uppajj|nirujjh|uppann|niruddh)")
PI_NEG = re.compile(r"(?<![a-zāīūṃṅñṭḍṇḷ])(na |nuppajj|nupp)")


def f4_expected(pali_line):
    n = 0
    for m in PI_NOCA.finditer(pali_line):
        cl = m.group(1)
        if PI_VERB.search(cl) and not PI_NEG.search(cl):
            n += 1
    return n


def block_ids(lines):
    """block id of the segment for every line index"""
    ids = [""] * len(lines)
    start = 0
    for i in range(len(lines) + 1):
        if i == len(lines) or lines[i].strip() == "":
            seg = range(start, i)
            if len(seg):
                last = lines[i - 1].rstrip()
                m = re.search(r"\^[0-9A-Za-z-]+$", last)
                bid = m.group(0) if m else ""
                for j in seg:
                    ids[j] = bid
            start = i + 1
    return ids


def main():
    os.makedirs(BACKUP, exist_ok=True)
    log = []
    per = {}  # (chapter, rule) -> changed lines
    problems = []
    already = []
    same_new, same_old = {}, {}
    for ch in CHAPTERS:
        bpath = os.path.join(BACKUP, ch)
        vpath = os.path.join(VI_DIR, ch)
        if not os.path.exists(bpath):
            shutil.copyfile(vpath, bpath)
        src = read(bpath)
        assert "\r" not in src, ch
        pali = read(os.path.join(PI_DIR, ch)).split("\n")
        lines = src.split("\n")
        assert len(lines) == len(pali), (ch, len(lines), len(pali))
        ids = block_ids(lines)

        def note(i, rule, old, new):
            log.append((ch, ids[i], old, new, rule))
            per.setdefault((ch, rule), set()).add(i)

        # --- F1
        if ch == "8-cittayamaka.md":
            for old, new, cnt, label in F1_RULES + F1_ANSWERS:
                hits = [i for i, ln in enumerate(lines) if old in ln]
                n = sum(lines[i].count(old) for i in hits)
                assert n == cnt, ("F1", old, n, cnt)
                for i in hits:
                    lines[i] = lines[i].replace(old, new)
                    note(i, "F1", old, new)
        # --- F3
        cnt3 = 0
        for i, ln in enumerate(lines):
            if F3_OLD in ln:
                cnt3 += ln.count(F3_OLD)
                lines[i] = ln.replace(F3_OLD, F3_NEW)
                note(i, "F3", F3_OLD, F3_NEW)
        assert cnt3 == F3_COUNT.get(ch, 0), ("F3", ch, cnt3)
        # --- F9
        cnt9 = 0
        for i, ln in enumerate(lines):
            if F9_OLD in ln:
                cnt9 += ln.count(F9_OLD)
                lines[i] = ln.replace(F9_OLD, F9_NEW)
                note(i, "F9", F9_OLD, F9_NEW)
        assert cnt9 == F9_COUNT.get(ch, 0), ("F9", ch, cnt9)
        # --- F4 (only on lines whose Pali has a positive "no ca" uppajjati / nirujjhati clause)
        for i, ln in enumerate(lines):
            exp = f4_expected(pali[i])
            got = 0

            def r_neither(m):
                nonlocal got
                got += 1
                neg = NEG[m.group("t")] + m.group("v")
                new = f"{m.group('p')} {m.group('x')} {neg}, {m.group('y')} cũng {neg}"
                note(i, F4_NAME[m.group("t")] + " neither", m.group(0), new)
                return new

            def r_single(m):
                nonlocal got
                got += 1
                new = f"{m.group('p')} {m.group('x')} {NEG[m.group('t')]}{m.group('v')}"
                note(i, F4_NAME[m.group("t")], m.group(0), new)
                return new

            if exp:
                ln2 = F4_NEITHER.sub(r_neither, ln)
                ln2 = F4_SINGLE.sub(r_single, ln2)
                if got > exp:
                    problems.append((ch, i + 1, ids[i], f"F4 expected {exp} got {got}", ln))
                elif got < exp:
                    # the other "no ca" clauses of the line already negate the verb (dhamma frames:
                    # «nhưng tâm ấy không …», «nhưng không phải đang …»): listed, not changed
                    already.append((ch, i + 1, ids[i], exp - got))
                lines[i] = ln2
            else:
                if F4_SINGLE.search(ln):
                    problems.append((ch, i + 1, ids[i], "F4 shape without Pali no ca", ln))
            # assert nothing left after "no ca"
            if exp and (F4_SINGLE.search(lines[i]) or F4_NEITHER.search(lines[i])
                        or F4_BROAD.search(lines[i])):
                problems.append((ch, i + 1, ids[i], "F4 left", lines[i]))

        strip_id = lambda s: re.sub(r"\s*\^[0-9A-Za-z-]+$", "", s).strip()
        for i, (ln, old_ln) in enumerate(zip(lines, src.split("\n"))):
            key = strip_id(pali[i])
            if key:
                same_new.setdefault(key, set()).add(strip_id(ln))
                same_old.setdefault(key, set()).add(strip_id(old_ln))
        out = "\n".join(lines)
        # --- checks
        assert unicodedata.normalize("NFC", out) == out, ch
        for bad in ("—", ":-", "….", "được được", "là là", "chánh niệm", "vẫn đã", "seed", "  ", "\r"):
            if bad in out and bad not in src:
                problems.append((ch, 0, "", f"new forbidden string {bad!r}", ""))
            if bad in out:
                print(f"NOTE {ch}: contains {bad!r} ({out.count(bad)})")
        assert not re.search(r"(?<!đang )nhập thành tựu thiền chấm dứt", out), ch
        assert F9_OLD not in out, ch
        if ch == "8-cittayamaka.md":
            for s in F1_LEFT:
                assert s not in out, ("F1 left", s)
        if not DRY and out != read(vpath):
            write(vpath, out)

    # identical Pali line = identical Vietnamese line inside the part (no new splits)
    n_old = sum(1 for k, s in same_old.items() if len(s) > 1)
    n_new = sum(1 for k, s in same_new.items() if len(s) > 1)
    print(f"identical-Pali lines with more than one Vietnamese form: before {n_old}, after {n_new}")
    if n_new > n_old:
        problems.append(("part", 0, "", "identical Pali split", ""))
    with open(LOG, "w", encoding="utf-8", newline="\n") as f:
        f.write("file\tblock_id\told\tnew\trule\n")
        for row in log:
            f.write("\t".join(row) + "\n")

    print("lines changed per chapter / rule:")
    tot = {}
    for (ch, rule), s in sorted(per.items()):
        print(f"  {ch}\t{rule}\t{len(s)} lines\t{sum(1 for r in log if r[0] == ch and r[4] == rule)} replacements")
    for ch in CHAPTERS:
        alll = set()
        for (c, rule), s in per.items():
            if c == ch:
                alll |= s
        tot[ch] = len(alll)
    print("distinct lines changed per chapter:", tot, "total", sum(tot.values()))
    print("replacements per rule:")
    rules = {}
    for r in log:
        rules[r[4]] = rules.get(r[4], 0) + 1
    for k, v in sorted(rules.items()):
        print(f"  {k}: {v}")
    print("F1 wordings:")
    for label, w in F1_WORDINGS:
        print(f"  [{label}] {w}")
    print(f"'no ca' + verb clauses already negated on the verb (unchanged): {sum(a[3] for a in already)} "
          f"in {len(already)} lines:", ", ".join(f"{a[0]} {a[2]}" for a in already))
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  ", p)
        sys.exit(1)
    print("OK" + (" (dry run, nothing written)" if DRY else ""))


if __name__ == "__main__":
    main()
