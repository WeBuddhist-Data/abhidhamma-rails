"""Post-fix checks: nested/unbalanced “ ”, sample lines identical, double blank lines, Latin outside brackets.
python -I -X utf8 rv_checks.py"""
import pathlib, re

HERE = pathlib.Path(__file__).parent
HDIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters")
BAK = HERE / "backup-pre-fixes"


def quote_issues(text):
    bad = []
    for n, l in enumerate([x for x in text.split("\n") if x.strip()]):
        d = 0
        for ch in l:
            if ch == "“":
                d += 1
                if d > 1:
                    bad.append(n + 1)
                    break
            elif ch == "”":
                d -= 1
        else:
            if d != 0:
                bad.append(n + 1)
    return bad


def latin(text):
    out = []
    for n, l in enumerate([x for x in text.split("\n") if x.strip()]):
        s = re.sub(r"\[[^\]]*\]", "", l)
        s = re.sub(r"\^[\w-]+\s*$", "", s)
        if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", s):
            out.append(n + 1)
    return out


for p in sorted(HDIR.glob("*.md")):
    new, old = p.read_text(encoding="utf-8"), (BAK / p.name).read_text(encoding="utf-8")
    qn, qo = quote_issues(new), quote_issues(old)
    ln, lo = latin(new), latin(old)
    msg = []
    if set(qn) - set(qo):
        msg.append(f"new quote issues {sorted(set(qn) - set(qo))}")
    if set(ln) - set(lo):
        msg.append(f"new latin {sorted(set(ln) - set(lo))}")
    if "\n\n\n" in new:
        msg.append("double blank")
    if p.name == "1-khandhavibhango.md":
        a = [x for x in new.split("\n") if x.strip()][:77]
        b = [x for x in old.split("\n") if x.strip()][:77]
        diff = [i + 1 for i in range(77) if a[i] != b[i]]
        msg.append(f"sample lines differing: {diff}")
    if p.name == "preamble.md":
        msg.append("preamble identical" if new.encode() == old.encode() else "PREAMBLE CHANGED")
    print(p.name, f"quote issues {len(qo)}->{len(qn)}", "; ".join(msg))
