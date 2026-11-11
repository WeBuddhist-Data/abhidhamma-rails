"""Cross-chapter alignment of the pi-1 Hindi rails chapters (identical Pāli, one Hindi wording).

usage: python -I -X utf8 align_rails.py [--write]
Backup of every changed file goes to backup-pre-align/ (only on --write, only if not already there).
Log: align-log.tsv (file, line no, before, after).
"""
import collections, pathlib, re, shutil, sys

HDIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters")
PDIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-1_split_chapters")
HERE = pathlib.Path(__file__).parent
WRITE = "--write" in sys.argv

# (file prefix, exact old, exact new, expected count)
EXACT = [
    ("5-", "श्रमण-जीवन के नीचे के तीन फल", "श्रमण-जीवन के निचले तीन फल", 1),
    ("2-03", "उस समय चार समूह होते हैं", "और उस समय चार समूह होते हैं", 1),
    ("4-01", "वही मन के मैल मन के मैल भी हैं और मन के मैलों का विषय बनने वाले भी।",
     "मन के मैल रूपी भी और मन के मैलों का विषय बनने वाली भी परिघटनाएँ वे ही मन के मैल हैं।", 1),
    ("4-01", "वही बंधन बंधन भी हैं और बंधनों का विषय बनने वाले भी।",
     "बंधन रूपी भी और बंधनों का विषय बनने वाली भी परिघटनाएँ वे ही बंधन हैं।", 1),
    ("4-01", "वही गाँठें गाँठ भी हैं और गाँठों का विषय बनने वाली भी।",
     "गाँठ रूपी भी और गाँठों का विषय बनने वाली भी परिघटनाएँ वे ही गाँठें हैं।", 1),
    ("4-01", "लालच, लोभ, लोभ रूपी हानिकर मूल", "लालच, लोभ रूपी हानिकर मूल", 2),
    ("3-01", "##### एक-एक के वर्गीकरणों की व्याख्या", "##### एकल वर्गीकरण की व्याख्या", None),
    ("3-01", "एक-एक के वर्गीकरण", "एकल वर्गीकरण", None),
    ("2-03", "पहचान के समूह को छोड़कर, चेतना के समूह को छोड़कर – यह उस समय मानसिक रचनाओं का समूह",
     "पहचान के समूह को छोड़कर और चेतना के समूह को छोड़कर – यह उस समय मानसिक रचनाओं का समूह", 1),
]
# 3-01 ^1-583: same sentence as ^1-987 (4-01), whole line
L583_OLD = re.compile(r"^नैतिक रूप से अनिर्धारित परिघटनाएँ कौन-सी हैं\? हितकर और हानिकर परिघटनाओं के .* \^1-583$")
L987 = re.compile(r"^(नैतिक रूप से अनिर्धारित परिघटनाएँ कौन-सी हैं\? हितकर और हानिकर कर्म के फल रूपी परिघटनाएँ, जो .*?) \^1-987$")
# eka + genitive + noun: «एक X का Y होता है» -> «X का एक Y होता है»
EKA = re.compile(r"(?:(?<=^)|(?<=[\s,;]))एक ((?:[^\s,;।…]+ ){0,5}?(?:का|की|के)) (समूह|तत्व|इंद्रिय-क्षेत्र|क्षमता)(?= हो)")

texts = {p: p.read_text(encoding="utf-8") for p in sorted(HDIR.glob("*.md"))}
line987 = next(m.group(1) for t in texts.values() for l in t.split("\n") for m in [L987.match(l)] if m)
log, changed, ekas = [], set(), collections.Counter()
for p, t in texts.items():
    ls = t.split("\n")
    for prefix, old, new, want in EXACT:
        if not p.name.startswith(prefix):
            continue
        n = 0
        for i, l in enumerate(ls):
            if old in l:
                n += l.count(old)
                nl = l.replace(old, new)
                log.append((p.name, i + 1, old, new))
                ls[i] = nl
        if want is not None and n != want:
            sys.exit(f"{p.name}: expected {want} of {old!r}, found {n}")
        if n:
            changed.add(p)
    if p.name.startswith("3-01"):
        for i, l in enumerate(ls):
            if L583_OLD.match(l):
                ls[i] = line987 + " ^1-583"
                log.append((p.name, i + 1, l, ls[i]))
                changed.add(p)
    if p.name.startswith("2-0"):
        for i, l in enumerate(ls):
            def rep(m):
                ekas[m.group(0) + " -> " + m.group(1) + " एक " + m.group(2)] += 1
                return m.group(1) + " एक " + m.group(2)
            nl = EKA.sub(rep, l)
            if nl != l:
                log.append((p.name, i + 1, "(eka order)", "(eka order)"))
                ls[i] = nl
                changed.add(p)
    texts[p] = "\n".join(ls)

print("edits", len(log), "files", sorted(x.name for x in changed))
print("eka reorderings:")
for k, v in ekas.most_common():
    print(f"  {v}  {k}")
if WRITE:
    bak = HERE / "backup-pre-align"
    bak.mkdir(exist_ok=True)
    for p in changed:
        if not (bak / p.name).exists():
            shutil.copy2(p, bak / p.name)
        p.write_text(texts[p], encoding="utf-8", newline="\n")
    (HERE / "align-log.tsv").write_text("\n".join("\t".join(map(str, r)) for r in log) + "\n", encoding="utf-8", newline="\n")
    print("written")
else:
    print("(dry run; add --write)")
