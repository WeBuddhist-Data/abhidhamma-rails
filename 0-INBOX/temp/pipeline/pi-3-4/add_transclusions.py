"""Insert root-text transclusions into a 1:1 block-aligned translation.

Usage: python add_transclusions.py <translation.md> <root-text-vault-path> <repo-root>

Before every content block (not headings) that ends with a block ID, inserts
    ![[<root-text-vault-path>#^<id>]]
followed by a blank line, matching the pi-2 track file's format. Then checks
that every link targets a block ID present in the root text and that every
content block ID of the root text is linked exactly once. Idempotent: refuses
to run on a file that already contains transclusions.
"""
import re, sys
from pathlib import Path

path, root_rel, repo = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
text = path.read_text(encoding="utf-8")
if "![[" in text:
    raise SystemExit("file already contains transclusions — not touching it")

m = re.match(r"(---\n.*?\n---\n)\n?(.*)", text, re.S)
frontmatter, body = m.group(1), m.group(2)

ID_RE = re.compile(r"\^([\w]+(?:-[\w]+)*)\s*$")
out, linked = [], []
for block in re.split(r"\n\s*\n", body.strip()):
    mid = ID_RE.search(block.split("\n")[-1])
    if mid and not block.startswith("#"):
        out.append(f"![[{root_rel}#^{mid.group(1)}]]")
        linked.append(mid.group(1))
    out.append(block)

root_text = (repo / root_rel).read_text(encoding="utf-8")
root_text = root_text[root_text.find("\n---", 3) + 4:] if root_text.startswith("---") else root_text
root_content_ids, root_all_ids = [], set()
for block in re.split(r"\n\s*\n", root_text.strip()):
    mid = ID_RE.search(block.split("\n")[-1])
    if mid:
        root_all_ids.add(mid.group(1))
        if not block.startswith("#"):
            root_content_ids.append(mid.group(1))

missing_target = [i for i in linked if i not in root_all_ids]
if missing_target:
    raise SystemExit(f"links to IDs not in root text: {missing_target[:10]}")
if linked != root_content_ids:
    raise SystemExit(f"linked IDs differ from root content IDs "
                     f"({len(linked)} vs {len(root_content_ids)})")

path.write_text(frontmatter + "\n" + "\n\n".join(out) + "\n", encoding="utf-8")
print(f"inserted {len(linked)} transclusions; all resolve, all {len(root_content_ids)} "
      f"root content blocks linked once, in order")
