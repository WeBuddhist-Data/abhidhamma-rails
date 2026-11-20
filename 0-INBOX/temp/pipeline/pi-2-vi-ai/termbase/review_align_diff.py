"""New termbase-adherence misses created by the pi-2 vi review fixes (backup-pre-review vs current rails),
with every segment ID, the termbase senses (index, tag, term) and the segment text around the keyword's old term.
Optional: --sim <decisions tsv> simulates overrides (hw|i -> term) and reports misses per keyword after them.

usage: python -I -X utf8 review_align_diff.py [--sim file] [--kw regex] [--show]
Logic copied from ../../termbase_adherence_vi.py (read-only use)."""
import collections, pathlib, re, sys, unicodedata

sys.dont_write_bytecode = True
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation/pali/pi-2-keywords-by-reference-pali-plain.md"
TBF = ROOT / "AI_translation/vietnamese/pi-2-pali-vietnamese-termbase-plain.md"
POST = ROOT / "AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters"
PRE = ROOT / "0-INBOX/temp/pipeline/pi-2-vi-ai/rails/backup-pre-review"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
GAP = " … "
LEAD = ("sự ", "niềm ", "lòng ", "trạng thái ", "tính chất ", "loại ", "đã ", "đang ", "sẽ ", "có ")


def norm(t):
    t = unicodedata.normalize("NFC", t)
    t = re.sub(r"\s*\[[^\]]*\]", " ", t)
    t = t.lower()
    t = re.sub(r"[,;:.?!“”‘’\"()–—…#*]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def present(term, text):
    pos = 0
    for part in term.split(GAP):
        p = norm(part)
        if not p:
            continue
        m = re.compile(r"(?<!\w)" + re.escape(p) + r"(?!\w)").search(text, pos)
        if not m:
            return False
        pos = m.end()
    return True


def variants(term):
    out, t = [term], term
    changed = True
    while changed:
        changed = False
        low = t.lower()
        for lead in LEAD:
            if low.startswith(lead) and len(t) > len(lead):
                t = t[len(lead):]
                out.append(t)
                changed = True
                break
    return out


def segs(d):
    seg = {}
    for p in pathlib.Path(d).glob("*.md"):
        buf = []
        for line in p.read_text(encoding="utf-8").splitlines():
            buf.append(line)
            m = ID.search(line)
            if m:
                seg[m.group(1)] = norm(" ".join(buf))
                buf = []
    return seg


def load_tb():
    tb = {}
    for line in TBF.read_text(encoding="utf-8").splitlines():
        if ": {" not in line:
            continue
        w, body = line.split(": {", 1)
        tb[w] = [tuple(s.rsplit(": ", 1)) for s in body[:-1].split("; ")]
    return tb


def occurrences():
    for line in KW.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        i, body = line.split("] ", 1)
        i = i[1:]
        for k in body.split(", "):
            for kk in k.split(" / "):
                yield i, kk


def misses(seg, tb, tb_ci):
    out = set()
    for i, kk in occurrences():
        if i not in seg:
            continue
        hw = kk if kk in tb else tb_ci.get(kk.lower())
        if hw is None:
            continue
        terms = [t for _, t in tb[hw]]
        if not any(present(v, seg[i]) for t in terms for v in variants(t)):
            out.add((i, kk))
    return out


def main(a):
    tb = load_tb()
    tb_ci = {k.lower(): k for k in tb}
    if "--sim" in a:
        f = pathlib.Path(a[a.index("--sim") + 1])
        for l in f.read_text(encoding="utf-8-sig").splitlines():
            if l.strip() and not l.startswith("#"):
                key, term = l.split("\t")[:2]
                hw, idx = key.rsplit("|", 1)
                ss = tb[hw]
                ss[int(idx)] = (ss[int(idx)][0], term.strip())
    kwrx = re.compile(a[a.index("--kw") + 1], re.I) if "--kw" in a else None
    pre, post = segs(PRE), segs(POST)
    m_pre, m_post = misses(pre, tb, tb_ci), misses(post, tb, tb_ci)
    print(f"misses pre-review text {len(m_pre)}, current text {len(m_post)}; "
          f"new {len(m_post - m_pre)}, gone {len(m_pre - m_post)}")
    new = collections.defaultdict(list)
    for i, kk in sorted(m_post - m_pre):
        new[kk].append(i)
    occ = collections.Counter(kk for i, kk in occurrences() if i in post)
    for kk, ids in sorted(new.items(), key=lambda x: (-len(x[1]), x[0])):
        if kwrx and not kwrx.search(kk):
            continue
        hw = kk if kk in tb else tb_ci[kk.lower()]
        print(f"\n== {kk} (hw {hw}) new misses {len(ids)} of {occ[kk]} occ: {' '.join(ids)}")
        for n, (tag, t) in enumerate(tb[hw]):
            print(f"   {hw}|{n}  [{tag[:110]}]  = {t}")
        if "--show" in a:
            for i in ids[:3]:
                print(f"   {i}: {post[i][:300]}")
    gone = sorted(m_pre - m_post)
    if gone and not kwrx:
        print("\ngone:", ", ".join(f"{k}@{i}" for i, k in gone))


if __name__ == "__main__":
    main(sys.argv[1:])
