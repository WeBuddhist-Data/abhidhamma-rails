# 2026-11-21 helper for vi-termbase-align-brief.md: which adherence misses the review fixes created, and every use
# of the affected headwords (segment, sense terms present before / after, Vietnamese text of the segment).
# usage: python -I -X utf8 review_align_vi.py diff
#        python -I -X utf8 review_align_vi.py occ <exact headword> [<headword> ...]
#        python -I -X utf8 review_align_vi.py seg <block id> [...]
import pathlib, re, sys, unicodedata, collections

sys.dont_write_bytecode = True
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation/pali/pi-4-keywords-by-reference-pali-plain.md"
TBF = ROOT / "AI_translation/vietnamese/pi-4-pali-vietnamese-termbase-plain.md"
AFTER = ROOT / "AI_translation/vietnamese/pi-4-vietnamese-plain-rails_split_chapters"
BEFORE = ROOT / "0-INBOX/temp/pipeline/pi-4-vi-ai/rails/backup-pre-review"
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
        for lead in LEAD:
            if t.lower().startswith(lead) and len(t) > len(lead):
                t = t[len(lead):]
                out.append(t)
                changed = True
                break
    return out


def segs(d, raw=False):
    seg = {}
    for p in d.glob("*.md"):
        buf = []
        for line in p.read_text(encoding="utf-8").splitlines():
            buf.append(line)
            m = ID.search(line)
            if m:
                seg[m.group(1)] = " ".join(buf) if raw else norm(" ".join(buf))
                buf = []
    return seg


def tb():
    out = {}
    for line in TBF.read_text(encoding="utf-8").splitlines():
        if ": {" not in line:
            continue
        w, body = line.split(": {", 1)
        out[w] = [tuple(s.rsplit(": ", 1)) for s in body[:-1].split("; ")]
    return out


def kws():
    out = []
    for line in KW.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        i, body = line.split("] ", 1)
        for k in body.split(", "):
            for kk in k.split(" / "):
                out.append((i[1:], kk))
    return out


def misses(seg, T):
    tl = {k.lower(): v for k, v in T.items()}
    s = set()
    for i, kk in kws():
        if i not in seg:
            continue
        senses = T.get(kk) or tl.get(kk.lower())
        if not senses:
            continue
        if not any(present(v, seg[i]) for _, t in senses for v in variants(t)):
            s.add((i, kk))
    return s


def main(a):
    T = tb()
    if a[0] == "diff":
        b, f = misses(segs(BEFORE), T), misses(segs(AFTER), T)
        print(f"before {len(b)} after {len(f)}")
        print("NEW misses:")
        for i, k in sorted(f - b, key=lambda x: (x[1], x[0])):
            print(f"  {k}\t{i}")
        print("RESOLVED:")
        for i, k in sorted(b - f, key=lambda x: (x[1], x[0])):
            print(f"  {k}\t{i}")
    elif a[0] == "occ":
        sb, sa = segs(BEFORE), segs(AFTER)
        tl = {k.lower(): (k, v) for k, v in T.items()}
        for hw in a[1:]:
            key, senses = tl.get(hw.lower(), (hw, None))
            print(f"== {key}")
            if not senses:
                print("   not in termbase")
                continue
            for n, (tag, t) in enumerate(senses):
                print(f"   |{n} {t}   [{tag}]")
            for i, kk in kws():
                if kk.lower() != hw.lower() or i not in sa:
                    continue
                pb = [n for n, (_, t) in enumerate(senses) if any(present(v, sb.get(i, "")) for v in variants(t))]
                pa = [n for n, (_, t) in enumerate(senses) if any(present(v, sa[i]) for v in variants(t))]
                ch = "" if sb.get(i) == sa[i] else "  CHANGED"
                print(f"   {i}: senses present before {pb} after {pa}{ch}")
    elif a[0] == "seg":
        sa = segs(AFTER, raw=True)
        for i in a[1:]:
            print(f"== {i}\n{sa.get(i)}\n")


if __name__ == "__main__":
    main(sys.argv[1:])
