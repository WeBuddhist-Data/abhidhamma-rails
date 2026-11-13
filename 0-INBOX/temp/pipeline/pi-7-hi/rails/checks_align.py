"""Post-alignment checks for the pi-7 Hindi RAILS folder: check_chapter_ids, verify_hi, dashcheck per file; protected
text unchanged vs backup-pre-align; greps («—», «:-», «धर्म», "seed", Latin outside [..], CR, double blank lines).
usage: python -I -B -X utf8 checks_align.py"""
import os, re, sys, subprocess, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ar7_common as C

PIPE = os.path.join(C.ROOT, r"0-INBOX\temp\pipeline")
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
print("check_chapter_ids not OK:", ids_bad or "none")
print("dashcheck mismatches:", dash_bad or "none")
print("verify_hi: files with flags:")
for f, n, q, b, other in ver:
    if n:
        print(f"   {f}: {n} flags ({q} Siyā '?', {b} bracket) other: {other[:5]}")
# protected text
prot_bad = []
for part in ("preamble", "1-00-paccaya"):
    a = open(os.path.join(C.BAK, part + ".md"), encoding="utf-8").read()
    b = open(os.path.join(C.HDIR, part + ".md"), encoding="utf-8").read()
    if a != b:
        prot_bad.append(part)
a = [l for l in open(os.path.join(C.BAK, "1-01-kusalattika.md"), encoding="utf-8").read().splitlines() if l.strip()]
b = [l for l in open(os.path.join(C.HDIR, "1-01-kusalattika.md"), encoding="utf-8").read().splitlines() if l.strip()]
for lo, hi in ((1, 190), (1235, 1262)):
    if a[lo - 1:hi] != b[lo - 1:hi]:
        prot_bad.append(f"1-01 {lo}-{hi}")
print("protected text changed:", prot_bad or "none")
# greps
g = collections.Counter()
lat = collections.Counter()
for part in C.PARTS:
    t = open(os.path.join(C.HDIR, part + ".md"), encoding="utf-8", newline="").read()
    g["—"] += t.count("—")
    g[":-"] += t.count(":-")
    g["धर्म"] += t.count("धर्म")
    g["seed"] += t.lower().count("seed")
    g["CR"] += t.count("\r")
    g["double blank"] += t.count("\n\n\n")
    nob = re.sub(r"\[[^\]]*\]", "", t)
    nob = re.sub(r"\^[0-9A-Za-z-]+", "", nob)
    for w in re.findall(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]+", nob):
        lat[part[:4] + ":" + w] += 1
print("greps:", dict(g))
print("Latin outside [..]:", sum(lat.values()), lat.most_common(10))
