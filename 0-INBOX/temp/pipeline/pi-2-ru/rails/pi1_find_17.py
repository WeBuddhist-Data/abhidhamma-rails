"""Chapter 17 helper: for each line of 17-khuddakavatthuvibhango.md, find the lines of the approved Russian rails
(pi-1, pi-2 ch. 1-16, pi-3, pi-4, pi-5) that share the most 5-word Pāli shingles, and print the aligned Russian.
Writes pi1-find-17.txt (reference only).
usage: python -I -X utf8 pi1_find_17.py
"""
import pathlib
import re
from collections import defaultdict

AI = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
OUT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails\pi1-find-17.txt")
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
K = 5


def segs_text(text):
    out, cur = {}, []
    for ln in text.splitlines():
        if not ln.strip() or ln.startswith("---") and not cur and ":" not in ln:
            continue
        cur.append(ln)
        m = ID.search(ln)
        if m:
            out[m.group(1)] = cur
            cur = []
    return out


def segs(path):
    return segs_text(path.read_text(encoding="utf-8"))


def words(s):
    s = re.sub(r"\[[^\]]*\]", " ", s)
    s = ID.sub("", s)
    return re.findall(r"[^\s,.;:?!\"'–—()…]+", s.lower().replace("…pe…", " "))


corpus = []   # (label, sid, i, pali, ru)
for book in ("pi-1", "pi-2"):
    pdir = AI / "pali" / f"{book}_split_chapters"
    rdir = AI / "russian" / f"{book}-russian-plain-rails_split_chapters"
    for pf in sorted(pdir.glob("*.md")):
        if pf.name.startswith("17-") or pf.name.startswith("18-"):
            continue
        rf = rdir / pf.name
        if not rf.exists():
            continue
        P, R = segs(pf), segs(rf)
        for sid, pl in P.items():
            rl = R.get(sid, [])
            for i, ln in enumerate(pl):
                corpus.append((f"{book}/{pf.stem}", sid, i, ln, rl[i] if i < len(rl) else "-"))
for book in ("pi-3", "pi-4", "pi-5"):
    R = segs(AI / "russian" / f"{book}-russian-plain.md")
    for pf in sorted((AI / "pali" / f"{book}_split_chapters").glob("*.md")):
        for sid, pl in segs(pf).items():
            rl = R.get(sid, [])
            for i, ln in enumerate(pl):
                corpus.append((f"{book}/{pf.stem}", sid, i, ln, rl[i] if i < len(rl) else "-"))

idx = defaultdict(set)
for n, (_, _, _, pali, _) in enumerate(corpus):
    w = words(pali)
    for j in range(len(w) - K + 1):
        idx[tuple(w[j:j + K])].add(n)

src = segs(AI / "pali" / "pi-2_split_chapters" / "17-khuddakavatthuvibhango.md")
seen = {}
res = []
for sid, pl in src.items():
    for i, ln in enumerate(pl):
        w = words(ln)
        if len(w) < K:
            continue
        score = defaultdict(int)
        for j in range(len(w) - K + 1):
            for n in idx.get(tuple(w[j:j + K]), ()):
                score[n] += 1
        best = sorted(score.items(), key=lambda x: (-x[1], x[0]))[:3]
        best = [b for b in best if b[1] >= 2]
        if not best:
            continue
        res.append(f"######## ^{sid} L{i}: {ln[:160]}")
        for n, sc in best:
            lab, csid, ci, pali, ru = corpus[n]
            key = (lab, csid, ci)
            if key in seen:
                res.append(f"  [{sc}] {lab} ^{csid} L{ci} (see {seen[key]})")
                continue
            seen[key] = f"^{sid} L{i}"
            res += [f"  [{sc}] {lab} ^{csid} L{ci}", "  PI: " + pali, "  RU: " + ru]
        res.append("")
OUT.write_text("\n".join(res) + "\n", encoding="utf-8", newline="\n")
print("done", len(corpus), "corpus lines")
