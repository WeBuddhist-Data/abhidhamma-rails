# -*- coding: utf-8 -*-
"""Review fixes, stage 1, part r2 (pi-6 Vietnamese rails).

Chapters: 3-06, 4, 5-01, 5-02, 5-03, 6-01, 6-02, 7-01.
Usage:  python -I -X utf8 -B review_fixes_r2_vi.py scan   (read-only survey)
        python -I -X utf8 -B review_fixes_r2_vi.py        (apply, from the backup)
"""
import os
import re
import shutil
import sys
import unicodedata
from collections import Counter

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
VI = os.path.join(ROOT, r"AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters")
PI = os.path.join(ROOT, r"AI_translation\pali\pi-6_split_chapters")
RAILS = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
BACKUP = os.path.join(RAILS, "backup-pre-review")
LOG = os.path.join(RAILS, "review-fixes-log-r2.tsv")

CHAPTERS = [
    "3-06-ayatanayamaka.md",
    "4-dhatuyamaka.md",
    "5-01-saccayamaka.md",
    "5-02-saccayamaka.md",
    "5-03-saccayamaka.md",
    "6-01-sankharayamaka.md",
    "6-02-sankharayamaka.md",
    "7-01-anusayayamaka.md",
]


def read(path):
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def backup():
    os.makedirs(BACKUP, exist_ok=True)
    for ch in CHAPTERS:
        dst = os.path.join(BACKUP, ch)
        if not os.path.exists(dst):
            shutil.copy2(os.path.join(VI, ch), dst)


def segments(text):
    """Yield (block_id, [line indexes]) for each segment."""
    lines = text.split("\n")
    seg = []
    for i, ln in enumerate(lines):
        if ln.strip() == "":
            if seg:
                yield seg, lines
                seg = []
        else:
            seg.append(i)
    if seg:
        yield seg, lines


def block_ids(lines):
    """Map line index -> block id of its segment."""
    out = {}
    seg = []
    for i, ln in enumerate(lines + [""]):
        if ln.strip() == "":
            if seg:
                m = re.search(r"\^(\S+)\s*$", lines[seg[-1]])
                bid = m.group(1) if m else "?"
                for j in seg:
                    out[j] = bid
                seg = []
        else:
            seg.append(i)
    return out


# --------------------------------------------------------------------------
# Rules
# --------------------------------------------------------------------------
PRON = r"(?:những người ấy|người ấy|nơi ấy)"
HEAD = r"(nhưng ở " + PRON + r"(?:, ở nơi ấy)?) "
# X: a member noun phrase; no comma / full stop / question mark; lazy up to the verb.
X = r"([^,.?…]+?)"
VERB = r"(sinh khởi|chấm dứt)"

# F4 single: «nhưng ở P không có X [đã |sẽ |đang ]V»
F4_RE = re.compile(HEAD + r"không có " + X + r" (đã |sẽ |đang )?" + VERB + r"(?=[,.…]| \^|$)")
# F4 neither: «nhưng ở P không có X, cũng không có Y [tense ]V»
F4N_RE = re.compile(HEAD + r"không có " + X + r", cũng không có " + X + r" (đã |sẽ |đang )?" + VERB
                    + r"(?=[,.…]| \^|$)")


def neg(tense, verb):
    if tense is None or tense == "":
        return "không " + verb
    if tense == "đã ":
        return "chưa từng " + verb
    if tense == "sẽ ":
        return "sẽ không " + verb
    if tense == "đang ":
        return "không đang " + verb
    raise ValueError(tense)


def f4n_sub(m):
    head, x, y, tense, verb = m.groups()
    nv = neg(tense, verb)
    return f"{head} {x} {nv}, {y} cũng {nv}"


def f4_sub(m):
    head, x, tense, verb = m.groups()
    return f"{head} {x} {neg(tense, verb)}"


# F3
F3_OLD = "nhập thành tựu thiền chấm dứt"
F3_NEW = "đang nhập thành tựu thiền chấm dứt"
F3_RE = re.compile(r"(?<!đang )nhập thành tựu thiền chấm dứt")

# F5: «tâm cuối cùng <modifier with không có> sẽ sinh khởi»
# The modifier may not run across another «tâm cuối cùng» or a new «những người» group
# («những người có được tâm cuối cùng không có … và những người mà tâm cuối cùng không có … sẽ sinh khởi»).
F5_RE = re.compile(r"tâm cuối cùng (không có (?:(?!tâm cuối cùng|những người| và )[^,.?…])+?) (sẽ sinh khởi)")


def f5_sub(m):
    return f"tâm cuối cùng, vốn {m.group(1)}, {m.group(2)}"


# F6: 4-dhatuyamaka cut stubs: «<stub> không?» where the Pāli line is a bare stub "…?…"
F6_RE = re.compile(r"^(.+?), có phải không\?(…?)( \^\S+)?$|^(.+?) không\?(…?)( \^\S+)?$")


# Expected occurrence counts per chapter (from the read-only survey of the backup).
EXPECTED = {
    "3-06-ayatanayamaka.md": {"F4": 38},
    "4-dhatuyamaka.md": {"F4": 7, "F6": 14},
    "5-01-saccayamaka.md": {"F4": 51, "F3": 6},
    "5-02-saccayamaka.md": {"F4": 45, "F3": 10},
    "5-03-saccayamaka.md": {"F4": 11, "F3": 2},
    "6-01-sankharayamaka.md": {"F4": 48, "F3": 19, "F5": None},
    "6-02-sankharayamaka.md": {"F4": 49, "F3": 23, "F5": None},
    "7-01-anusayayamaka.md": {},
}
F5_TOTAL = 37  # review-findings A6


def apply_chapter(ch, text, log):
    lines = text.split("\n")
    bids = block_ids(lines)
    counts = Counter()
    for i, ln in enumerate(lines):
        new = ln
        rules = []
        # F4 neither first, then single
        new, n1 = F4N_RE.subn(f4n_sub, new)
        new, n2 = F4_RE.subn(f4_sub, new)
        counts["F4"] += n1 + n2
        counts["F4-neither"] += n1
        if n1 + n2:
            rules.append(f"F4x{n1 + n2}")
        new, n = F3_RE.subn(F3_NEW, new)
        counts["F3"] += n
        if n:
            rules.append(f"F3x{n}")
        if ch.startswith("6-"):
            new, n = F5_RE.subn(f5_sub, new)
            counts["F5"] += n
            if n:
                rules.append(f"F5x{n}")
        if ch.startswith("4-"):
            new, n = f6_line(new)
            counts["F6"] += n
            if n:
                rules.append(f"F6x{n}")
        if new != ln:
            counts["lines"] += 1
            log.append((ch, bids.get(i, "?"), str(i + 1), ln, new, "+".join(rules)))
            lines[i] = new
    return "\n".join(lines), counts


LEFT_F4 = re.compile(r"nhưng ở [^.?]*? không có [^,.?…]+? (?:đã |sẽ |đang )?(?:sinh khởi|chấm dứt)(?=[,.…]| \^|$)")
BAD = ["—", ":-", "….", "được được", "là là", "chánh niệm", "vẫn đã", "seed", "  ", "\r"]


def post_checks(ch, old, new):
    errs = []
    if LEFT_F4.search(new):
        errs.append(f"F4 left: {len(LEFT_F4.findall(new))}")
    if F3_RE.search(new):
        errs.append("F3 left")
    if F5_RE.search(new):
        errs.append("F5 left")
    if new.startswith(F6_PREFIXES) or any(("\n" + p) in new for p in F6_PREFIXES):
        errs.append("F6 left")
    for b in BAD:
        if new.count(b) > old.count(b):
            errs.append(f"new {b!r}")
        elif b in new:
            print(f"  note: {ch} has pre-existing {b!r} x{new.count(b)}")
    if unicodedata.normalize("NFC", new) != new:
        errs.append("not NFC")
    if old.count("\n") != new.count("\n"):
        errs.append("line count changed")
    if re.findall(r"\^\S+", old) != re.findall(r"\^\S+", new):
        errs.append("block ids changed")
    return errs


# Pāli ^6-4-6 "… Ghānaviññāṇaṃ?…Pe… jivhāviññāṇaṃ?… Kāyaviññāṇaṃ?",
# ^6-4-7 "… Na ghānaṃ?… Na jivhā?…" and "… Na sotaviññāṇaṃ?…Pe… na ghānaviññāṇaṃ?…":
# bare stubs, no «có phải … không».
F6_PREFIXES = (
    "… Thức qua mũi không?",
    "… Những gì không phải là mũi, có phải không?",
    "… Những gì không phải là thức qua tai, có phải không?",
)


def f6_line(ln):
    if not ln.startswith(F6_PREFIXES):
        return ln, 0
    n1 = ln.count(", có phải không?")
    new = ln.replace(", có phải không?", "?")
    n2 = new.count(" không?")
    new = new.replace(" không?", "?")
    return new, n1 + n2


# --------------------------------------------------------------------------
def scan():
    shapes = Counter()
    for ch in CHAPTERS:
        t = read(os.path.join(VI, ch))
        lines = t.split("\n")
        bids = block_ids(lines)
        print("=" * 20, ch)
        for i, ln in enumerate(lines):
            for m in re.finditer(r"nhưng ở [^,.]*?(?:, ở nơi ấy)? không có .{0,120}", ln):
                s = m.group(0)
                s2 = re.sub(r"không có [^,.?…]+?( (?:đã |sẽ |đang )?(?:sinh khởi|chấm dứt))", r"không có X\1", s)
                s2 = re.split(r"(?<=[.?…])", s2)[0]
                s2 = re.sub(r"^nhưng ở [^,]*?(, ở nơi ấy)? không", r"nhưng ở P\1 không", s2)
                shapes[(ch[:4], s2[:110])] += 1
            if "nhập thành tựu thiền chấm dứt" in ln:
                for m in re.finditer(r".{0,40}nhập thành tựu thiền chấm dứt.{0,10}", ln):
                    shapes[(ch[:4], "F3: " + m.group(0))] += 1
            if ch.startswith("6-") and "tâm cuối cùng" in ln:
                for m in re.finditer(r"tâm cuối cùng[^,.]{0,120}", ln):
                    shapes[(ch[:4], "TCC: " + m.group(0))] += 1
            if ch.startswith("4-") and ln.endswith(("không?", "không?…")) or (ch.startswith("4-") and re.search(r"không\?( \^\S+)?$", ln) and len(ln) < 80):
                shapes[(ch[:4], f"STUB {bids[i]}: " + ln)] += 1
    for (c, s), n in sorted(shapes.items()):
        print(c, n, s)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "scan":
        scan()
        return
    backup()
    log = []
    out = {}
    total = Counter()
    for ch in CHAPTERS:
        src = read(os.path.join(BACKUP, ch))
        assert "\r" not in src
        new, counts = apply_chapter(ch, src, log)
        new = unicodedata.normalize("NFC", new)
        for rule, exp in EXPECTED[ch].items():
            if exp is not None:
                assert counts[rule] == exp, (ch, rule, counts[rule], exp)
        for rule in ("F3", "F4", "F5", "F6"):
            if rule not in EXPECTED[ch]:
                assert counts[rule] == 0, (ch, rule, counts[rule])
        errs = post_checks(ch, src, new)
        assert not errs, (ch, errs)
        out[ch] = new
        print(ch, dict(counts))
        total.update(counts)
    assert total["F5"] == F5_TOTAL, ("F5", total["F5"])
    for ch, new in out.items():
        write(os.path.join(VI, ch), new)
    with open(LOG, "w", encoding="utf-8", newline="\n") as f:
        f.write("file\tblock_id\tline\told\tnew\trule\n")
        for row in log:
            f.write("\t".join(row) + "\n")
    print("TOTAL", dict(total), "lines changed", len(log))


if __name__ == "__main__":
    main()
