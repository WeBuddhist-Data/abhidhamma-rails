"""Independent check of root-text transclusions in a translation file.

Usage: python verify_transclusions.py <translation.md> <repo-root> [sample_n]

Checks, reading the files line by line (not reusing the insertion logic):
 1. every transclusion line has the exact form ![[<path>#^<id>]] and <path> exists
 2. each target ^id occurs exactly once in the root text, at the end of a line
    preceded by a space (how Obsidian recognises a block ID)
 3. the block right after each transclusion carries the same ^id
 4. no heading is transcluded; every non-heading root block is transcluded
    exactly once, in root order; no transclusion is left dangling
Prints a few random Pāli/English pairs for a by-eye check.
"""
import random, re, sys
from pathlib import Path

tr_path, repo = Path(sys.argv[1]), Path(sys.argv[2])
sample_n = int(sys.argv[3]) if len(sys.argv) > 3 else 5
lines = tr_path.read_text(encoding="utf-8").split("\n")
TRANS = re.compile(r"^!\[\[(?P<path>[^#\]]+)#\^(?P<id>[\w-]+)\]\]$")
errors = []

# --- root text: block id -> (is_heading, text); count occurrences
roots = {}
def load_root(rel):
    if rel not in roots:
        p = repo / rel
        if not p.exists():
            roots[rel] = None
        else:
            t = p.read_text(encoding="utf-8")
            blocks, occ = {}, {}
            for ln in t.split("\n"):
                for m in re.finditer(r" \^([\w-]+)\s*$", ln):
                    occ[m.group(1)] = occ.get(m.group(1), 0) + 1
            body = t[t.find("\n---", 3) + 4:] if t.startswith("---") else t
            order = []
            for para in re.split(r"\n\s*\n", body.strip()):
                m = re.search(r" \^([\w-]+)\s*$", para.split("\n")[-1])
                if m:
                    blocks[m.group(1)] = (para.startswith("#"), para)
                    order.append(m.group(1))
            roots[rel] = (blocks, occ, order)
    return roots[rel]

linked, pairs = [], []
for i, ln in enumerate(lines):
    if "![[" not in ln:
        continue
    m = TRANS.match(ln)
    if not m:
        errors.append(f"line {i+1}: malformed transclusion: {ln}")
        continue
    rel, bid = m.group("path"), m.group("id")
    root = load_root(rel)
    if root is None:
        errors.append(f"line {i+1}: target file missing: {rel}")
        continue
    blocks, occ, _ = root
    if occ.get(bid, 0) != 1:
        errors.append(f"line {i+1}: ^{bid} occurs {occ.get(bid, 0)} times in {rel}")
    if bid in blocks and blocks[bid][0]:
        errors.append(f"line {i+1}: ^{bid} is a heading")
    # next non-blank lines up to the following blank line = the English block
    j = i + 1
    if j >= len(lines) or lines[j].strip():
        errors.append(f"line {i+1}: not followed by a blank line")
    while j < len(lines) and not lines[j].strip():
        j += 1
    k = j
    while k < len(lines) and lines[k].strip():
        k += 1
    eng = "\n".join(lines[j:k])
    m2 = re.search(r"\^([\w-]+)\s*$", lines[k - 1]) if k > j else None
    if not m2 or m2.group(1) != bid:
        errors.append(f"line {i+1}: link ^{bid} but next block ends with "
                      f"{('^' + m2.group(1)) if m2 else 'no ID'}")
    linked.append(bid)
    pairs.append((bid, blocks.get(bid, (False, "?"))[1], eng))

targets = {TRANS.match(ln).group("path") for ln in lines if TRANS.match(ln)}
if len(targets) != 1:
    raise SystemExit(f"expected links into exactly one root text, found {sorted(targets)}")
rel = targets.pop()
blocks, _, order = load_root(rel)
expected = [b for b in order if not blocks[b][0]]
if linked != expected:
    missing = [b for b in expected if b not in linked]
    extra = [b for b in linked if b not in expected]
    errors.append(f"coverage: {len(linked)} linked vs {len(expected)} expected; "
                  f"missing {missing[:5]}, extra {extra[:5]}")

# English content blocks without a transclusion above them
text = "\n".join(lines)
body = text[text.find("\n---", 3) + 4:]
for para in re.split(r"\n\s*\n", body.strip()):
    if para.startswith("![[") or para.startswith("#"):
        continue
    m = re.search(r"\^([\w-]+)\s*$", para.split("\n")[-1])
    if m and m.group(1) not in linked:
        errors.append(f"English block ^{m.group(1)} has no transclusion")

print("\n".join(errors[:30]))
print(f"{len(linked)} transclusions checked; {len(expected)} root content blocks — "
      + ("ALL OK" if not errors else f"{len(errors)} problem(s)"))
random.seed(7)
for bid, pali, eng in random.sample(pairs, min(sample_n, len(pairs))):
    print(f"\n[^{bid}]\n  PĀLI: {pali[:220]}\n  EN:   {eng[:220]}")
