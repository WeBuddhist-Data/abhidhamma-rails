"""Write the Pāli keyword lines whose segment IDs occur in the given rails folder (for a sample adherence run).
usage: python -I -X utf8 kw_subset.py <keywords-pali.md> <rails_dir> <out.md>
"""
import pathlib
import re
import sys

kw, rails, out = sys.argv[1:4]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
ids = set()
for p in pathlib.Path(rails).glob("*.md"):
    for ln in p.read_text(encoding="utf-8").splitlines():
        m = ID.search(ln)
        if m:
            ids.add(m.group(1))
keep = [ln for ln in open(kw, encoding="utf-8").read().splitlines() if ln[1:].split("] ", 1)[0] in ids]
pathlib.Path(out).write_text("\n".join(keep) + "\n", encoding="utf-8")
print(len(keep), "keyword lines for", len(ids), "segments")
