"""Termbase adherence before (backup-pre-fixes) and after (current folder): totals and per-keyword differences."""
import subprocess, sys, re, os, collections
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
SCR = os.path.join(ROOT, r"0-INBOX\temp\pipeline\hindi_termbase_adherence.py")
KW = os.path.join(ROOT, r"AI_translation\pali\pi-7-keywords-by-reference-pali-plain.md")
TB = os.path.join(ROOT, r"AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md")
DIRS = [os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-7-hi\review\backup-pre-fixes"),
        os.path.join(ROOT, r"AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters")]
res = []
for d, name in zip(DIRS, ("adherence-before-fixes.txt", "adherence-after-fixes.txt")):
    rep = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-7-hi\review", name)
    r = subprocess.run([sys.executable, "-I", "-X", "utf8", SCR, KW, TB, d, rep], capture_output=True, text=True,
                       encoding="utf-8")
    lines = r.stdout.splitlines()[:1] + open(rep, encoding="utf-8").read().splitlines()
    c = collections.Counter()
    for l in lines[1:]:
        m = re.match(r"^\s*(\d+)\s+(.+?)\s+->\s+(.*?)\s+e\.g\.", l)
        if m:
            c[(m.group(2), m.group(3))] = int(m.group(1))
    res.append((lines[0], c))
print("before:", res[0][0])
print("after: ", res[1][0])
for k in sorted(set(res[0][1]) | set(res[1][1])):
    d = res[1][1][k] - res[0][1][k]
    if d:
        print(f"{d:+d}\t{k[0]} -> {k[1]}")
