"""Show word-level changes in fixes-preview.txt: python -I -X utf8 rv_diff.py [FILTER_REGEX]"""
import difflib, pathlib, re, sys

txt = (pathlib.Path(__file__).parent / "fixes-preview.txt").read_text(encoding="utf-8").split("\n")
flt = re.compile(sys.argv[1]) if len(sys.argv) > 1 else None
for i in range(0, len(txt) - 2, 3):
    head, a, b = txt[i], txt[i + 1][2:], txt[i + 2][2:]
    wa, wb = a.split(" "), b.split(" ")
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, wa, wb, autojunk=False).get_opcodes():
        if op != "equal":
            ctx = " ".join(wa[max(0, i1 - 4):i1])
            out.append(f"   …{ctx} [{' '.join(wa[i1:i2])}] -> [{' '.join(wb[j1:j2])}]")
    block = head + "\n" + "\n".join(out)
    if not flt or flt.search(block):
        print(block)
