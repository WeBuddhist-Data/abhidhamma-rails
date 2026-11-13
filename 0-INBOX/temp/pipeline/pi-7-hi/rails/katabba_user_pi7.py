r"""User decision 2026-11-14: kātabba takes the verb that fits its object.

  बनाना चाहिए        a basic sentence (मूल वाक्य), a cycle (चक्र), a list (मूल सूची)
  शामिल करना चाहिए   items to include (rebirth, the great elements, food, adverting)
  करना चाहिए          everywhere else (विस्तार, प्रश्न, विश्लेषण …)

1. Senses file: splits the kātabba headwords into these senses (every attested value placed once).
2. Termbase decisions: one decision per new sense (decisions.tsv), then re-run hindi_termbase_assemble.py 7.
3. Hindi rails: applies the object-specific replacements; backups in backup-pre-katabba\, log katabba-log.tsv.
usage: python -I -B -X utf8 katabba_user_pi7.py [--dry]
"""
import pathlib, re, shutil, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
SENSES = ROOT / "AI_translation/hindi/pi-7-pali-word-hindi-senses-plain.md"
DEC = ROOT / "0-INBOX/temp/pipeline/pi-7-hi/termbase/decisions.tsv"
H = ROOT / "AI_translation/hindi/pi-7-hindi-plain-rails_split_chapters"
D = pathlib.Path(__file__).parent
DRY = "--dry" in sys.argv
WHY = "user 2026-11-14: kātabba verb fits its object"

MAKE, INCL, DO = "बनाना चाहिए", "शामिल करना चाहिए", "करना चाहिए"
TAG = {MAKE: "to be made, of a basic sentence, a cycle or a list (gerundive)",
       INCL: "to be included, of items such as rebirth, the great elements or food (gerundive)",
       DO: "should be done, in general (gerundive)"}

# 1 + 2: senses and decisions
lines = SENSES.read_text(encoding="utf-8").splitlines()
new_dec = {}
for n, line in enumerate(lines):
    m = re.match(r"^([Kk]ātabb\w*): \{(.*)\}$", line)
    if not m:
        continue
    hw, body = m.groups()
    vals = body.split(": ", 1)[1].split(" / ")
    groups = []
    for key in (MAKE, INCL):
        if key in vals:
            groups.append((TAG[key], [key]))
    rest = [v for v in vals if v not in (MAKE, INCL)]
    rest.sort(key=lambda v: v != DO)
    groups.append((TAG[DO], rest))
    lines[n] = f"{hw}: {{" + "; ".join(f"{t}: {' / '.join(vs)}" for t, vs in groups) + "}"
    for i, (t, vs) in enumerate(groups):
        new_dec[f"{hw}|{i}"] = vs[0] if t != TAG[DO] else DO
    print(lines[n])

if not DRY:
    shutil.copy2(SENSES, D / "senses-before-katabba.md.bak")
    SENSES.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    out = [l for l in DEC.read_text(encoding="utf-8").splitlines() if not re.match(r"^[Kk]ātabb\w*\|", l)]
    out += [f"{k}\t{v}\t{WHY}" for k, v in new_dec.items()]
    DEC.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

# 3: Hindi rails
RULES = [
    ("मूल वाक्य करना चाहिए", "मूल वाक्य बनाना चाहिए"),
    ("मूल वाक्य करने चाहिए", "मूल वाक्य बनाने चाहिए"),
    ("चक्र करना चाहिए", "चक्र बनाना चाहिए"),
    ("मूल सूची करनी चाहिए", "मूल सूची बनानी चाहिए"),
    ("पुनर्जन्म करना चाहिए", "पुनर्जन्म शामिल करना चाहिए"),
    ("पुनर्जन्म भी करना चाहिए", "पुनर्जन्म भी शामिल करना चाहिए"),
    ("महाभूत करने चाहिए", "महाभूत शामिल करने चाहिए"),
    ("भोजन को करना चाहिए", "भोजन को शामिल करना चाहिए"),
    ("मोड़ना नहीं करना चाहिए", "मोड़ना शामिल नहीं करना चाहिए"),
]
log = []
for f in sorted(H.glob("*.md")):
    if f.name in ("preamble.md", "1-00-paccaya.md"):
        continue
    t = f.read_text(encoding="utf-8")
    new = t
    for old, rep in RULES:
        c = new.count(old)
        if c:
            new = new.replace(old, rep)
            log.append((f.name, old, rep, c))
    if new != t and not DRY:
        bak = D / "backup-pre-katabba"
        bak.mkdir(exist_ok=True)
        if not (bak / f.name).exists():
            shutil.copy2(f, bak / f.name)
        f.write_text(new, encoding="utf-8", newline="\n")
if not DRY:
    (D / "katabba-log.tsv").write_text("file\told\tnew\tcount\n" + "\n".join("\t".join(map(str, r)) for r in log) + "\n",
                                       encoding="utf-8", newline="\n")
from collections import Counter
c = Counter()
for r in log:
    c[r[1]] += r[3]
for k, v in c.items():
    print(v, k)
print("files", len({r[0] for r in log}), "(dry)" if DRY else "")
