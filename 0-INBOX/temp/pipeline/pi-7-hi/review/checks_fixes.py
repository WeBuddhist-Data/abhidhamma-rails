"""Post-fix checks for the pi-7 Hindi RAILS folder: check_chapter_ids, verify_hi, dashcheck per file; protected lines
changed vs backup-pre-fixes (listed); greps («—», «:-», «धर्म», "seed", Latin outside [..], CR, double blank lines);
leftover old triad/dyad names. usage: python -I -B -X utf8 checks_fixes.py"""
import os, re, sys, subprocess, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "rails"))
sys.path.insert(0, HERE)
import ar7_common as C
import apply_review_fixes_pi7 as F

PIPE = os.path.join(C.ROOT, r"0-INBOX\temp\pipeline")
BAK = os.path.join(HERE, "backup-pre-fixes")
py = sys.executable
ids_bad, ver, dash_bad = [], [], []
for part in C.PARTS:
    f = part + ".md"
    p, h = os.path.join(C.PDIR, f), os.path.join(C.HDIR, f)
    r = subprocess.run([py, "-I", os.path.join(PIPE, "check_chapter_ids.py"), C.PDIR, C.HDIR, f],
                       capture_output=True, text=True, encoding="utf-8")
    if "OK" not in r.stdout or r.returncode:
        ids_bad.append((f, r.stdout.strip()[:200]))
    r = subprocess.run([py, "-I", "-X", "utf8", os.path.join(PIPE, r"pi-1-hi\verify_hi.py"), p, h],
                       capture_output=True, text=True, encoding="utf-8")
    errs = [l.strip() for l in r.stdout.splitlines()[1:]]
    other = [e for e in errs if "final '?' differs" not in e and "brackets" not in e]
    ver.append((f, len(errs), sum("final '?'" in e for e in errs), sum("brackets" in e for e in errs), other))
    r = subprocess.run([py, "-I", "-X", "utf8", os.path.join(PIPE, r"pi-1-en\dashcheck.py"), p, h],
                       capture_output=True, text=True, encoding="utf-8")
    m = re.search(r"dash-line mismatches (\d+)", r.stdout)
    if not m or m.group(1) != "0":
        dash_bad.append((f, r.stdout.strip()[:200]))
print("files:", len(C.PARTS))
print("check_chapter_ids not OK:", ids_bad or "none")
print("dashcheck mismatches:", dash_bad or "none")
tq = sum(v[2] for v in ver)
tb = sum(v[3] for v in ver)
print(f"verify_hi: {sum(v[1] for v in ver)} flags ({tq} Siyā '?', {tb} bracket); other:",
      [(v[0], v[4][:3]) for v in ver if v[4]] or "none")
# protected lines changed
for part, rng in F.PROTECTED.items():
    a = [l for l in open(os.path.join(BAK, part + ".md"), encoding="utf-8").read().splitlines() if l.strip()]
    b = [l for l in open(os.path.join(C.HDIR, part + ".md"), encoding="utf-8").read().splitlines() if l.strip()]
    ch = [k + 1 for k in range(len(a)) if a[k] != b[k] and (rng is None or any(x <= k + 1 <= y for x, y in rng))]
    print(f"protected {part}: changed lines {ch}")
# greps
g = collections.Counter()
lat = collections.Counter()
old_names = collections.Counter()
for part in C.PARTS:
    t = open(os.path.join(C.HDIR, part + ".md"), encoding="utf-8", newline="").read()
    g["—"] += t.count("—")
    g[":-"] += t.count(":-")
    g["धर्म"] += t.count("धर्म")
    g["seed"] += t.lower().count("seed")
    g["CR"] += t.count("\r")
    g["double blank"] += t.count("\n\n\n")
    g["double space"] += len(re.findall(r"\S  +\S", t))
    nob = re.sub(r"\[[^\]]*\]", "", t)
    nob = re.sub(r"\^[0-9A-Za-z-]+", "", nob)
    for w in re.findall(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]+", nob):
        lat[part[:4] + ":" + w] += 1
    for rx, new, old, k in F.U1_RX:
        if old != new:
            for m in rx.finditer(t):
                old_names[(old, k, part[:4])] += 1
print("greps:", dict(g))
print("Latin outside [..]:", sum(lat.values()), lat.most_common(10))
print("old names left:", sum(old_names.values()), old_names.most_common(20))
