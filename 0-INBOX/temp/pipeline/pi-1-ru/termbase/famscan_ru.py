# family scan for the pi-1 Russian termbase: groups senses by their tag text without the trailing
# grammar parenthesis and lists groups whose chosen terms (decision, else single candidate) differ.
# usage: python -I -X utf8 famscan_ru.py [regex-on-tag]
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\termbase")
import tb_tool_ru as T

rx = re.compile(sys.argv[1], re.I) if len(sys.argv) > 1 else None
dec = T.decisions()
groups = collections.defaultdict(list)
for hw, ss in T.senses():
    for i, (tag, c) in enumerate(ss):
        key = f"{hw}|{i}"
        term = dec[key][0] if key in dec else (c[0] if len(c) == 1 else "?" + "/".join(c))
        core = re.sub(r"\s*\([^()]*\)\s*$", "", tag).strip().lower()
        groups[core].append((key, term))
for core, items in sorted(groups.items()):
    if rx and not rx.search(core):
        continue
    terms = {t for _, t in items}
    if len(items) > 1 and len(terms) > 1:
        print(f"## {core}")
        for k, t in items:
            print(f"   {k}\t{t}")
