# -*- coding: utf-8 -*-
"""pi-6 Vietnamese rails: user-approved review fixes, stage 1, part r5 (10-03 ... 10-13).

Rules applied in this part (review\\review-findings.md A3 / A4, vi-review-fixes-brief.md F3 / F4):
  F3  nirodhasamāpannānaṃ «những người nhập thành tựu thiền chấm dứt» -> «những người đang nhập thành tựu thiền chấm dứt»
  F4  "no ca" + uppajjati / uppajjittha / uppajjissati (pavatti frames): the negation goes on the verb
      «nhưng ở <pron>[, ở nơi ấy] không có X sinh khởi»    -> «… X không sinh khởi»
      «nhưng ở <pron>[, ở nơi ấy] không có X đã sinh khởi» -> «… X chưa từng sinh khởi»
      «nhưng ở <pron>[, ở nơi ấy] không có X sẽ sinh khởi» -> «… X sẽ không sinh khởi»
  (no «chấm dứt», no participle and no "neither" form occurs after "no ca" in this part; F1, F2, F5 … F9 have no
  occurrence here.)

Builds every chapter from rails\\backup-pre-review\\<ch> (copied once, never overwritten), so it can be re-run.
Each rule's count per chapter is asserted against the Pāli (number of "no ca" clauses with a positive uppajj- verb
per tense; number of "nirodhasamāpann"). Rewrites rails\\review-fixes-log-r5.tsv on every run.
"""
import os, re, shutil, sys, unicodedata, collections

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
VI = os.path.join(ROOT, r"AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters")
PI = os.path.join(ROOT, r"AI_translation\pali\pi-6_split_chapters")
RAILS = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
BACKUP = os.path.join(RAILS, "backup-pre-review")
LOG = os.path.join(RAILS, "review-fixes-log-r5.tsv")
CHS = ["10-%02d-indriyayamaka.md" % i for i in range(3, 14)]

# expected counts (asserted; also cross-checked against the Pāli below)
EXP_F3 = {"10-03-indriyayamaka.md": 15, "10-08-indriyayamaka.md": 7,
          "10-09-indriyayamaka.md": 5, "10-10-indriyayamaka.md": 5}
EXP_F4 = {  # chapter: (present, past, future)
    "10-03-indriyayamaka.md": (69, 0, 0),
    "10-05-indriyayamaka.md": (0, 34, 36),
    "10-06-indriyayamaka.md": (0, 0, 52),
    "10-08-indriyayamaka.md": (54, 16, 0),
    "10-09-indriyayamaka.md": (61, 0, 61),
    "10-12-indriyayamaka.md": (0, 23, 62),
}

F3_OLD = "những người nhập thành tựu thiền chấm dứt"
F3_NEW = "những người đang nhập thành tựu thiền chấm dứt"
# the clause after "no ca": resumptive pronoun / place, then «không có <member> [đã |sẽ ]sinh khởi»
F4_PAT = re.compile(r"(nhưng ở (?:những người ấy, ở nơi ấy|những người ấy|nơi ấy) )không có "
                    r"(năng lực [^,.?;…]+?) (đã |sẽ )?sinh khởi")
F4_NEW = {None: "{m} không sinh khởi", "đã ": "{m} chưa từng sinh khởi", "sẽ ": "{m} sẽ không sinh khởi"}
TENSE = {None: 0, "đã ": 1, "sẽ ": 2}

# residue checks over the whole part after the fix
RESIDUE = [
    ("F3", re.compile(r"(?<!đang )nhập thành tựu thiền chấm dứt")),
    ("F4", re.compile(r"không có [^,.?;…]*? (?:đã |sẽ |đang )?(?:sinh khởi|chấm dứt)")),
]
BAD = ["—", ":-", "….", "được được", "là là", "chánh niệm", "vẫn đã", "se" + "ed", "  ", "\r"]


def rd(p):
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()


def wr(p, t):
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def pali_counts(ch):
    p = rd(os.path.join(PI, ch))
    f4 = [0, 0, 0]
    for m in re.finditer(r"no ca ([^.,?]*)", p):
        cl = " " + m.group(1) + " "
        if " na " in cl:
            continue
        w = m.group(1).split()[-1]
        if w.startswith("uppajjitth"):
            f4[1] += 1
        elif w.startswith("uppajjiss"):
            f4[2] += 1
        elif w.startswith("uppajj"):
            f4[0] += 1
    return len(re.findall(r"nirodhasamāpann", p)), tuple(f4)


def block_ids(lines):
    """block id of the segment each line belongs to (id at the end of the segment's last line)."""
    ids = [None] * len(lines)
    cur = None
    for i in range(len(lines) - 1, -1, -1):
        if not lines[i].strip():
            cur = None
            continue
        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", lines[i])
        if m and cur is None:
            cur = m.group(1)
        ids[i] = cur
    return ids


def main():
    os.makedirs(BACKUP, exist_ok=True)
    for ch in CHS:
        b = os.path.join(BACKUP, ch)
        if not os.path.exists(b):
            shutil.copyfile(os.path.join(VI, ch), b)

    log = [("file", "block_id", "old", "new", "rule")]
    lines_changed = collections.defaultdict(lambda: collections.Counter())
    repl = collections.defaultdict(lambda: collections.Counter())
    for ch in CHS:
        src = rd(os.path.join(BACKUP, ch))
        assert "\r" not in src
        lines = src.split("\n")
        ids = block_ids(lines)
        p_f3, p_f4 = pali_counts(ch)
        assert p_f3 == EXP_F3.get(ch, 0), (ch, "pali F3", p_f3)
        assert p_f4 == EXP_F4.get(ch, (0, 0, 0)), (ch, "pali F4", p_f4)
        f3 = 0
        f4 = [0, 0, 0]
        out = []
        for i, ln in enumerate(lines):
            new = ln
            n = new.count(F3_OLD)
            if n:
                new = new.replace(F3_OLD, F3_NEW)
                f3 += n
                lines_changed[ch]["F3"] += 1
                for _ in range(n):
                    log.append((ch, ids[i] or "", F3_OLD, F3_NEW, "F3"))
            hits = []

            def sub(m):
                t = m.group(3)
                f4[TENSE[t]] += 1
                rep = m.group(1) + F4_NEW[t].format(m=m.group(2))
                hits.append((m.group(0), rep))
                return rep
            new2 = F4_PAT.sub(sub, new)
            if hits:
                lines_changed[ch]["F4"] += 1
                for o, r in hits:
                    log.append((ch, ids[i] or "", o, r, "F4"))
            new = new2
            out.append(new)
        assert f3 == EXP_F3.get(ch, 0), (ch, "F3", f3)
        assert tuple(f4) == EXP_F4.get(ch, (0, 0, 0)), (ch, "F4", f4)
        repl[ch]["F3"] = f3
        repl[ch]["F4"] = sum(f4)
        txt = "\n".join(out)
        txt = unicodedata.normalize("NFC", txt)
        assert len(out) == len(lines)
        for name, rx in RESIDUE:
            left = rx.findall(txt)
            assert not left, (ch, name, left[:3])
        for b in BAD:
            assert b not in txt, (ch, "bad string", repr(b))
        assert unicodedata.is_normalized("NFC", txt)
        if txt != rd(os.path.join(VI, ch)):
            wr(os.path.join(VI, ch), txt)

    with open(LOG, "w", encoding="utf-8", newline="\n") as f:
        for row in log:
            f.write("\t".join(row) + "\n")

    tot = collections.Counter()
    for ch in CHS:
        lc = lines_changed[ch]
        print("%s  F3 %d repl / %d lines   F4 %d repl / %d lines" % (
            ch, repl[ch]["F3"], lc["F3"], repl[ch]["F4"], lc["F4"]))
        tot["F3r"] += repl[ch]["F3"]; tot["F3l"] += lc["F3"]
        tot["F4r"] += repl[ch]["F4"]; tot["F4l"] += lc["F4"]
    print("total F3 %(F3r)d repl / %(F3l)d lines, F4 %(F4r)d repl / %(F4l)d lines" % tot)
    print("log rows", len(log) - 1)

    # identical Pāli line -> identical Vietnamese line, inside the part: no new split
    def split_keys(get):
        d = collections.defaultdict(set)
        for ch in CHS:
            pl = rd(os.path.join(PI, ch)).split("\n")
            vl = get(ch).split("\n")
            assert len(pl) == len(vl)
            for a, b in zip(pl, vl):
                if a.strip():
                    d[re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", a)].add(re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", b))
        return {k for k, v in d.items() if len(v) > 1}
    before = split_keys(lambda ch: rd(os.path.join(BACKUP, ch)))
    after = split_keys(lambda ch: rd(os.path.join(VI, ch)))
    assert after <= before, sorted(after - before)[:3]
    print("identical-Pāli line keys with >1 Vietnamese: before %d, after %d" % (len(before), len(after)))

    # builder constants that still hold the old wording (report only; builders are not edited)
    for i in range(1, 14):
        b = os.path.join(RAILS, "build_rails_10-%02d_vi.py" % i)
        for n, ln in enumerate(rd(b).split("\n"), 1):
            if (re.search(r"(?<!đang )nhập thành tựu thiền chấm dứt", ln)
                    or re.search(r"không có \{[^}]*\} ?(?:\{[^}]*\})?(?:đã |sẽ )?sinh khởi", ln)
                    or re.search(r"không có \{", ln) and "sinh khởi" in ln):
                print("BUILDER", os.path.basename(b), n, ln.strip()[:150])


if __name__ == "__main__":
    main()
