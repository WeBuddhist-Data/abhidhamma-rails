"""Print non-empty lines a..b of 1-01 Pāli (or of the Hindi output with 'hi') with their index.
usage: python -I -B -X utf8 show_1-01.py a b [hi|prose|heads]
  prose: skip headings and pure counting lines (notes removed); heads: headings only"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.join(HERE, "..", "..", "..", "..", "..")
a, b = int(sys.argv[1]), int(sys.argv[2])
mode = sys.argv[3] if len(sys.argv) > 3 else ""
if mode == "hi":
    p = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-hindi-plain-rails_split_chapters", "1-01-kusalattika.md")
else:
    p = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters", "1-01-kusalattika.md")
lines = [l for l in open(p, encoding="utf-8").read().split("\n") if l.strip()]
if mode in ("prose", "heads"):
    import build_rails_sample as S
for i in range(a, min(b, len(lines)) + 1):
    ln = lines[i - 1]
    if mode == "prose":
        if ln.startswith("#"):
            continue
        body = re.sub(r" \^[0-9A-Za-z-]+\s*$", "", ln)
        body = re.sub(r"\([^()]*\)", " ", body)
        body = re.sub(r"\bna ", "na", body)
        body = body.replace("Nadhipati", "Naadhipati")
        core = S.lower_initials(re.sub(r"\s+", " ", body).strip())
        core = re.sub(r"(…pe…|…|\.)+$", "", core).strip()
        core = core.replace("naaññamañña-paccayā", "naaññamaññapaccayā")
        try:
            if core and S.is_count(core):
                continue
        except Exception:
            pass
    if mode == "heads" and not ln.startswith("#"):
        continue
    print(f"{i}: {ln}")
