# Stage-1 review fixes, part r3 (7-02 ... 7-08, Anusayayamaka).
# Applies the stage-1 rules of vi-review-fixes-brief.md that occur in this part.
# Builds from rails\backup-pre-review\ (backup made once, never overwritten), so it can be re-run.
# Result for r3: no rule applies (no uppajjati / nirujjhati / nirodhasamapanna in these chapters);
# the script asserts that, rewrites the log (header only) and leaves the chapters byte-identical.
import os, re, shutil, sys, unicodedata

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
VI = os.path.join(ROOT, r"AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters")
PI = os.path.join(ROOT, r"AI_translation\pali\pi-6_split_chapters")
RAILS = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
BACKUP = os.path.join(RAILS, "backup-pre-review")
LOG = os.path.join(RAILS, "review-fixes-log-r3.tsv")

CHAPTERS = ["7-0%d-anusayayamaka.md" % i for i in range(2, 9)]

# Pali triggers of the stage-1 rules (F1 cittayamaka atikkantakala, F2 ekasadisam note,
# F3 nirodhasamapanna, F4 uppajjati / nirujjhati, F9 hettha). F5-F8 are tied to other parts' files.
PI_TRIGGERS = {
    "F3": re.compile(r"nirodhasamāpann"),
    "F4": re.compile(r"uppajj|nirujjh"),
    "F1": re.compile(r"atikkantakāl|vītikkant"),
    "F2": re.compile(r"ekasadis"),
    "F9": re.compile(r"heṭṭhā"),
}
# Vietnamese strings the rules replace
VI_TRIGGERS = {
    "F3": re.compile(r"(?<!đang )nhập thành tựu thiền chấm dứt"),
    "F4": re.compile(r"không có [^,.?]*?(đã |sẽ |đang )?(sinh khởi|chấm dứt)"),
    "F1": re.compile(r"thời đã qua|đã từng vượt khỏi"),
    "F2": re.compile(r"giống hệt nhau"),
    "F5": re.compile(r"tâm cuối cùng"),
    "F6": re.compile(r"Thức qua mũi không\?"),
    "F9": re.compile(r"xuống phía dưới"),
}

def read(p):
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()

def main():
    os.makedirs(BACKUP, exist_ok=True)
    rows = []
    hits = []
    for ch in CHAPTERS:
        dst = os.path.join(VI, ch)
        bak = os.path.join(BACKUP, ch)
        if not os.path.exists(bak):
            shutil.copy2(dst, bak)
        src = read(bak)
        pali = read(os.path.join(PI, ch))
        for rule, rx in PI_TRIGGERS.items():
            n = len(rx.findall(pali))
            if n:
                hits.append((ch, "pali", rule, n))
        for rule, rx in VI_TRIGGERS.items():
            n = len(rx.findall(src))
            if n:
                hits.append((ch, "vi", rule, n))
        out = src  # no rule applies in this part
        assert "\r" not in out and unicodedata.normalize("NFC", out) == out
        if read(dst) != out:
            with open(dst, "w", encoding="utf-8", newline="\n") as f:
                f.write(out)
        print(ch, "changed lines: 0")
    with open(LOG, "w", encoding="utf-8", newline="\n") as f:
        f.write("file\tblock_id\told\tnew\trule\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    if hits:
        for h in hits:
            print("TRIGGER", *h)
        sys.exit("triggers found: review before treating this part as no-op")
    print("r3: 0 triggers, 0 changes (F1-F9 none apply)")

main()
