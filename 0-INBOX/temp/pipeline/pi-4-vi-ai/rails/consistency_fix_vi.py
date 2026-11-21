"""Coordinator rails consistency fix, pi-4 (2026-11-21): in ch4 the matrix names that begin with «có người»
(matrix atthi / ekacco) were used verbatim in definitions whose Pāli has no such word (^4-110-112, ^4-121-129):
drop «có» in the question and the quoted name, as the coordinator rule applied in ch5-11. Asserted counts; log
appended to rails/consistency-log.tsv; pre-fix copy in rails/consistency/.
"""
import pathlib, re, shutil

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
F = ROOT / "AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters/4-tikapuggalapannatti.md"
D = ROOT / "0-INBOX/temp/pipeline/pi-4-vi-ai/rails"
(D / "consistency").mkdir(exist_ok=True)
bak = D / "consistency" / "4-tikapuggalapannatti.pre-fix.md"
if not bak.exists():
    shutil.copyfile(F, bak)
text = bak.read_text(encoding="utf-8")
RULES = [("Thế nào là có người ", "Thế nào là người "), ("“có người ", "“người ")]
log = []
lines = text.split("\n")
for i, l in enumerate(lines):
    new = l
    for old, rep in RULES:
        new = new.replace(old, rep)
    if new != l:
        sid = re.search(r"\^([0-9A-Za-z-]+)\s*$", l)
        log.append(f"4-tikapuggalapannatti.md\t{sid.group(1) if sid else '?'}\tcó người -> người\tcoordinator rule (no atthi in the definition Pāli)")
        lines[i] = new
out = "\n".join(lines)
assert out.count("Thế nào là có người") == 0 and out.count("“có người") == 0
assert len(log) == 12, len(log)
F.write_text(out, encoding="utf-8", newline="\n")
(D / "consistency-log.tsv").write_text("\n".join(log) + "\n", encoding="utf-8", newline="\n")
print("changed", len(log), "lines")
