r"""Helper: count changed lines per 10-xx file vs the before-who-fix backup, and list distinct changed phrases."""
import pathlib, collections, difflib, re
D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters")
B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\before-who-fix")
pairs = collections.Counter()
for f in sorted(B.glob("10-*.md")):
    a = f.read_text(encoding="utf-8").split("\n")
    b = (D / f.name).read_text(encoding="utf-8").split("\n")
    n = sum(1 for x, y in zip(a, b) if x != y)
    print(f.name, "changed lines:", n, "(line count", len(a), len(b), ")")
    for x, y in zip(a, b):
        if x != y:
            for sx, sy in zip(re.split(r"(?<=।) ", x), re.split(r"(?<=।) ", y)):
                if sx != sy:
                    sm = difflib.SequenceMatcher(None, sx, sy)
                    for op, i1, i2, j1, j2 in sm.get_opcodes():
                        if op != "equal":
                            pairs[(sx[max(0, i1 - 25):i2 + 25], sy[max(0, j1 - 25):j2 + 25])] += 1
for (x, y), c in pairs.most_common(40):
    print(c, "\n  -", x, "\n  +", y)
