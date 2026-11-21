"""r3 review helper: align list items Pāli -> Vietnamese across chapters 8-15 and report
one-to-many mappings (inconsistent or swapped items). Console output only; writes nothing.
Usage: python -I -X utf8 r3_items.py [-all]
"""
import re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / r"AI_translation\pali\pi-3_split_chapters"
VDIR = ROOT / r"AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters"
CH = ["8-sattamanayo.md", "9-atthamanayo.md", "10-navamanayo.md", "11-dasamanayo.md",
      "12-ekadasamanayo.md", "13-dvadasamanayo.md", "14-terasamanayo.md", "15-cuddasamanayo.md"]
IDRE = re.compile(r"\^(3-[0-9-]+)\s*$")


def segs(p):
    out = []
    for b in re.split(r"\n\s*\n", p.read_text(encoding="utf-8").strip()):
        ls = [l for l in b.split("\n") if l.strip()]
        m = IDRE.search(ls[-1])
        out.append((m.group(1) if m else None, ls))
    return out


def p_items(s):
    m = re.search(r"ye dhammā (sampayuttā|vippayuttā|khandhasaṅgahena)|ye vippayuttā", s)
    head = s[:m.start()] if m else s
    parts = re.split(r"…pe…|…|\.\.(?!\.)", head)
    out = []
    for x in parts:
        x = re.sub(r"\[[^\]]*\]", "", x)
        x = re.sub(r"\bye dhammā\b|\bdhammehi\b|\bye\b", "", x)
        out.append(" ".join(x.split()).lower())
    return out


def v_items(s):
    m = re.search(r"[Nn]hững hiện tượng nào (không được gộp vào cùng với|được gộp vào cùng với|không gắn liền với|gắn liền với) ", s)
    head = s[:m.start()] if m else s
    tail = s[m.end():] if m else ""
    last = re.split(r"; | theo cách| thì |…,|\?| \[|, thì", tail)[0]
    parts = head.split("…")[:-1] + [last] if m else head.split("…")
    out = []
    for x in parts:
        x = re.sub(r"\[[^\]]*\]", "", x)
        x = re.sub(r"^\s*([Nn]hững hiện tượng nào )?([Cc]ùng với )?", "", x)
        out.append(" ".join(x.split()))
    return out


def main():
    p2v = defaultdict(lambda: defaultdict(list))
    v2p = defaultdict(lambda: defaultdict(list))
    for ch in CH:
        for (pid, pl), (vid, vl) in zip(segs(PDIR / ch), segs(VDIR / ch)):
            if pl[0].startswith("#"):
                continue
            a, b = p_items(pl[0]), v_items(vl[0])
            if len(a) != len(b):
                print("COUNT", pid, len(a), len(b)); continue
            for x, y in zip(a, b):
                p2v[x][y].append(pid)
                v2p[y][x].append(pid)
    for x, d in sorted(p2v.items()):
        if len(d) > 1 or "-all" in sys.argv:
            print(f"P {x!r}:")
            for y, ids in d.items():
                print(f"    -> {y!r}  {ids[:6]}{'…' if len(ids) > 6 else ''}")
    for y, d in sorted(v2p.items()):
        if len(d) > 1:
            print(f"V {y!r} <- {dict((k, v[:4]) for k, v in d.items())}")


if __name__ == "__main__":
    main()
