# -*- coding: utf-8 -*-
"""pi-6 Vietnamese rails: user-approved review fixes, stage 1, part r1.

Part r1: preamble.md, 1-mulayamaka.md, 2-01, 2-02, 3-01 ... 3-05.
Rules applied here: F2, F3, F4, F7, F8 (vi-review-fixes-brief.md).
Builds from rails/backup-pre-review/ (copied once), so it can be re-run.
Writes the chapters (LF, NFC) and rails/review-fixes-log-r1.tsv.

Usage: python -I -X utf8 -B review_fixes_r1_vi.py [--explore]
"""
import os
import re
import shutil
import sys
import unicodedata
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
VI_DIR = os.path.join(REPO, "AI_translation", "vietnamese",
                      "pi-6-vietnamese-plain-rails_split_chapters")
PI_DIR = os.path.join(REPO, "AI_translation", "pali", "pi-6_split_chapters")
BACKUP = os.path.join(HERE, "backup-pre-review")
LOG = os.path.join(HERE, "review-fixes-log-r1.tsv")

PART = [
    "preamble.md",
    "1-mulayamaka.md",
    "2-01-khandhayamaka.md",
    "2-02-khandhayamaka.md",
    "3-01-ayatanayamaka.md",
    "3-02-ayatanayamaka.md",
    "3-03-ayatanayamaka.md",
    "3-04-ayatanayamaka.md",
    "3-05-ayatanayamaka.md",
]

BID = re.compile(r"\s(\^[0-9A-Za-z-]+)$")


def read(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def backup_once():
    os.makedirs(BACKUP, exist_ok=True)
    for name in PART:
        dst = os.path.join(BACKUP, name)
        if not os.path.exists(dst):
            shutil.copyfile(os.path.join(VI_DIR, name), dst)


def block_ids(lines):
    """Block id of the segment each line belongs to (id on its last line)."""
    out = [""] * len(lines)
    start = 0
    for i, ln in enumerate(lines + [""]):
        if ln.strip() == "":
            bid = ""
            for j in range(i - 1, start - 1, -1):
                m = BID.search(lines[j])
                if m:
                    bid = m.group(1)
                    break
            for j in range(start, i):
                out[j] = bid
            start = i + 1
    return out


# ---------------------------------------------------------------- rules

# F2 (A2): ^6-3-23 note, ekasadisaṃ = the questions are treated alike.
F2_OLD = ("(Ở nơi nào mà lĩnh vực mũi sinh khởi, thì ở nơi ấy lĩnh vực ý và lĩnh vực "
          "đối tượng của ý giống hệt nhau, không có khác biệt, ")
F2_NEW = ("(Ở nơi nào mà lĩnh vực mũi sinh khởi, thì các câu hỏi về lĩnh vực ý và về "
          "lĩnh vực đối tượng của ý được trình bày giống hệt nhau, không có gì khác, ")

# F3 (A3): nirodhasamāpannānaṃ.  0 expected in part r1 (asserted, Pāli too).
F3_OLD = re.compile(r"(?<!đang )nhập thành tựu thiền chấm dứt")

# F4 (A4): "no ca" + uppajjati / nirujjhati: negation on the verb.
NEG = {"": "không ", "đã ": "chưa từng ", "sẽ ": "sẽ không "}
PRON = r"nhưng ở (?:người ấy|những người ấy|nơi ấy)(?:, ở nơi ấy)?"
MEM = r"[^,.;?…]+?"
VERB = r"(đã |sẽ )?(sinh khởi|chấm dứt)"
# neither: «nhưng ở <pron> không có X, cũng không có Y <V>» (any number of items)
F4_NEITHER = re.compile(
    r"(" + PRON + r") không có (" + MEM + r"(?:, cũng không có " + MEM + r")+) "
    + VERB + r"(?=[,.;…]|$)")
F4_ONE = re.compile(
    r"(" + PRON + r") không có (" + MEM + r") " + VERB + r"(?=[,.;…]|$)")
PALI_NOCA = re.compile(
    r"no ca [^.,;?…]*?(?<!na )(?<![a-zāīūṃṅñṭḍṇḷ])(?:uppajj|nirujjh)[a-zāīūṃ]*")
F4_LEFT = re.compile(r"không có " + MEM + r" (?:đã |sẽ |đang )?(?:sinh khởi|chấm dứt)")


def f4_neither(m):
    tense = m.group(3) or ""
    verb = NEG[tense] + m.group(4)
    items = m.group(2).split(", cũng không có ")
    parts = [items[0] + " " + verb] + [it + " cũng " + verb for it in items[1:]]
    return m.group(1) + " " + ", ".join(parts)


def f4_one(m):
    tense = m.group(3) or ""
    return m.group(1) + " " + m.group(2) + " " + NEG[tense] + m.group(4)


# F7 (A6): 1-mulayamaka ^6-1-49 / ^6-1-99, first line: cut «có phải» question
# closed «… không.» (Pāli "…pe…." / "…." : no "?").
F7 = [
    ("^6-1-49",
     "đối tượng thiện… điều kiện thiện… sự phát sinh thiện…",
     "đối tượng thiện… điều kiện thiện… sự phát sinh thiện… không."),
    ("^6-1-99",
     "điều kiện thuộc phần tinh thần… sự phát sinh thuộc phần tinh thần…",
     "điều kiện thuộc phần tinh thần… sự phát sinh thuộc phần tinh thần… không."),
]

# F8 (A6): ^6-3-148: the Pāli comma that ends a sentence = full stop.
F8_OLD = "lĩnh vực ý vẫn sẽ chấm dứt, ở những người đang nhập Niết-bàn trọn vẹn"
F8_NEW = "lĩnh vực ý vẫn sẽ chấm dứt. Ở những người đang nhập Niết-bàn trọn vẹn"


# ---------------------------------------------------------------- driver

def pali_lines(name):
    p = os.path.join(PI_DIR, name)
    return read(p).split("\n") if os.path.exists(p) else None


def explore():
    pat = re.compile(r"không có [^.;?]*?(sinh khởi|chấm dứt)")
    shapes = Counter()
    ex = {}
    for name in PART:
        lines = read(os.path.join(BACKUP if os.path.exists(os.path.join(BACKUP, name))
                                  else VI_DIR, name)).split("\n")
        for ln in lines:
            for m in pat.finditer(ln):
                pre = ln[max(0, m.start() - 45):m.start()]
                pre = pre[pre.find("nhưng"):] if "nhưng" in pre else "<other>" + pre[-20:]
                body = re.sub(r"(lĩnh vực|khối) [^,]*?(?= (đã |sẽ |đang )?(sinh khởi|chấm dứt))",
                              "M", m.group(0))
                body = re.sub(r"(lĩnh vực|khối) [^,]*?(?=,)", "M", body)
                key = pre + "|" + body + "|" + ln[m.end():m.end() + 1]
                shapes[key] += 1
                ex.setdefault(key, (name, ln[max(0, m.start() - 60):m.end() + 20]))
        for kw in ("nirodhasamāpann", "nhập thành tựu thiền"):
            pl = pali_lines(name) or []
            n = sum(l.count(kw) for l in pl + lines)
            if n:
                print("KW", name, kw, n)
    for key, n in sorted(shapes.items(), key=lambda kv: -kv[1]):
        print(n, key)
        if not key.startswith("nhưng"):
            print("    EX", ex[key])


def main():
    if "--explore" in sys.argv:
        explore()
        return
    backup_once()
    log = []
    counts = defaultdict(Counter)        # rule -> chapter -> lines changed
    hits = Counter()                     # rule -> replacements
    pv_before = defaultdict(set)
    pv_after = defaultdict(set)
    for name in PART:
        src = read(os.path.join(BACKUP, name))
        assert "\r" not in src, name
        lines = src.split("\n")
        bids = block_ids(lines)
        pl = pali_lines(name)
        # F3: nothing in this part (Pāli and Vietnamese both asserted)
        assert not any(F3_OLD.search(l) for l in lines), name
        assert pl is None or not any("nirodhasamāpann" in l for l in pl), name
        new_lines = []
        for i, ln in enumerate(lines):
            new = ln
            rules = []
            if name == "3-01-ayatanayamaka.md" and F2_OLD in new:
                assert bids[i] == "^6-3-23", bids[i]
                new = new.replace(F2_OLD, F2_NEW)
                hits["F2"] += 1
                rules.append("F2")
            if name == "3-04-ayatanayamaka.md" and F8_OLD in new:
                assert bids[i] == "^6-3-148", bids[i]
                new = new.replace(F8_OLD, F8_NEW)
                hits["F8"] += 1
                rules.append("F8")
            if name == "1-mulayamaka.md":
                for bid, old, rep in F7:
                    if bids[i] == bid and new.endswith(old):
                        new = new[: -len(old)] + rep
                        hits["F7"] += 1
                        rules.append("F7")
            n1 = len(F4_NEITHER.findall(new))
            for m in list(F4_NEITHER.finditer(new)) + list(F4_ONE.finditer(new)):
                if " và " in m.group(2):
                    print("CHECK-VA", name, bids[i], m.group(0))
            # Pāli cross-check: positive uppajj- / nirujjh- after "no ca"
            if pl is not None and len(pl) == len(lines):
                np_ = len(PALI_NOCA.findall(pl[i]))
                nv_ = len(F4_NEITHER.findall(new)) + len(F4_ONE.findall(F4_NEITHER.sub("", new)))
                if np_ != nv_:
                    print("PALI-MISMATCH", name, bids[i], np_, nv_)
                    print("   PI", pl[i][:300])
                    print("   VI", new[:300])
                hits["pali-noca"] += np_
            if n1:
                new = F4_NEITHER.sub(f4_neither, new)
                hits["F4-neither"] += n1
            n2 = len(F4_ONE.findall(new))
            if n2:
                new = F4_ONE.sub(f4_one, new)
                hits["F4"] += n2
            if n1 or n2:
                rules.append("F4")
            # nothing left after "no ca"
            assert not re.search(PRON + r" " + F4_LEFT.pattern, new), (name, i + 1, new)
            for r in rules:
                counts[r][name] += 1
            if new != ln:
                log.append((name, bids[i], ln, new, "+".join(rules)))
            new_lines.append(new)
        # identical Pāli -> identical Vietnamese (line level)
        if pl is not None and len(pl) == len(lines):
            for p, a, b in zip(pl, lines, new_lines):
                if p.strip():
                    pv_before[p].add(a)
                    pv_after[p].add(b)
        out = "\n".join(new_lines)
        out = unicodedata.normalize("NFC", out)
        write(os.path.join(VI_DIR, name), out)
    for p in pv_after:
        assert len(pv_after[p]) <= len(pv_before[p]), ("identical Pāli split", p)
    # expected counts
    assert hits["F2"] == 1, hits
    assert hits["F7"] == 2, hits
    assert hits["F8"] == 1, hits
    with open(LOG, "w", encoding="utf-8", newline="\n") as f:
        f.write("file\tblock_id\told\tnew\trule\n")
        for row in log:
            f.write("\t".join(row) + "\n")
    print("replacements:", dict(hits))
    for r in sorted(counts):
        print(r, dict(counts[r]), "lines:", sum(counts[r].values()))
    print("changed lines:", len(log))


if __name__ == "__main__":
    main()
