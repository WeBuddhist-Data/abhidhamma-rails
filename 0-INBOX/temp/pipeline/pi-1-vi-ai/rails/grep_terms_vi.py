"""Helper: print locked termbase entries whose headword contains any of the given substrings (case-insensitive).

usage: python -I -X utf8 grep_terms_vi.py sub1 sub2 ...   (prefix a substring with = for an exact headword)
"""
import pathlib
import sys

TB = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-1-pali-vietnamese-termbase-plain.md")
subs = sys.argv[1:]
out = []
for line in TB.read_text(encoding="utf-8").splitlines():
    if ": {" not in line:
        continue
    w = line.split(": {", 1)[0]
    lw = w.lower()
    for s in subs:
        if (s.startswith("=") and lw == s[1:].lower()) or (not s.startswith("=") and s.lower() in lw):
            out.append(line)
            break
print("\n".join(out))
print(f"# {len(out)}", file=sys.stderr)
