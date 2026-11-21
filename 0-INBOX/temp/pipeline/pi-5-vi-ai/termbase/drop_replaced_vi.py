"""Remove from decisions.tsv the builder lines that the user's decisions-user.tsv replaces (2026-11-21).
usage: python -I -X utf8 -B drop_replaced_vi.py"""
import pathlib

TB = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\termbase")
user = {l.split("\t")[0] for l in (TB / "decisions-user.tsv").read_text(encoding="utf-8").splitlines()
        if l.strip() and not l.startswith("#")}
src = (TB / "decisions.tsv").read_text(encoding="utf-8").splitlines()
keep, dropped = [], []
for l in src:
    if l.strip() and not l.startswith("#") and l.split("\t")[0] in user:
        dropped.append(l.split("\t")[0])
    else:
        keep.append(l)
(TB / "decisions.tsv").write_text("\n".join(keep) + "\n", encoding="utf-8", newline="\n")
print("dropped", len(dropped), dropped)
