# 2026-11-22 adapted from pi-4-vi-ai/termbase/review_align_vi.py (pi-5 paths): which adherence misses the review
# fixes created, every use of the affected headwords, and a test of decisions-review.tsv against the reviewed text.
# usage: python -I -X utf8 -B review_align_vi.py diff
#        python -I -X utf8 -B review_align_vi.py misses [min]          every current miss, by headword, with block ids
#        python -I -X utf8 -B review_align_vi.py occ <exact headword> [<headword> ...]
#        python -I -X utf8 -B review_align_vi.py seg <block id> [...]
#        python -I -X utf8 -B review_align_vi.py find <regex>          termbase senses whose term matches <regex>
#        python -I -X utf8 -B review_align_vi.py test                  each decisions-review.tsv line: uses of the
#                                                                      headword, new term present / other senses present
import pathlib, re, sys, unicodedata, collections

sys.dont_write_bytecode = True
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md"
TBF = ROOT / "AI_translation/vietnamese/pi-5-pali-vietnamese-termbase-plain.md"
AFTER = ROOT / "AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters"
BEFORE = ROOT / "0-INBOX/temp/pipeline/pi-5-vi-ai/rails/backup-pre-review"
DECR = ROOT / "0-INBOX/temp/pipeline/pi-5-vi-ai/termbase/decisions-review.tsv"
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


def has(term, text):
    return any(present(v, text) for v in variants(term))


def segs(d, raw=False):
    seg = {}
    for p in d.glob("*.md"):
        if p.name.endswith(".pre-fix.md"):
            continue
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


def lookup(T, kk):
    tl = {k.lower(): (k, v) for k, v in T.items()}
    if kk in T:
        return kk, T[kk]
    return tl.get(kk.lower(), (kk, None))


def misses(seg, T):
    tl = {k.lower(): v for k, v in T.items()}
    s = set()
    for i, kk in kws():
        if i not in seg:
            continue
        senses = T.get(kk) or tl.get(kk.lower())
        if not senses:
            continue
        if not any(has(t, seg[i]) for _, t in senses):
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
    elif a[0] == "misses":
        lo = int(a[1]) if len(a) > 1 else 1
        g = collections.defaultdict(list)
        for i, k in misses(segs(AFTER), T):
            g[k].append(i)
        for k, ids in sorted(g.items(), key=lambda x: (-len(x[1]), x[0])):
            if len(ids) >= lo:
                _, ss = lookup(T, k)
                print(f"{len(ids):4d} {k} -> {' | '.join(t for _, t in ss)}\t{' '.join(sorted(ids)[:12])}")
    elif a[0] == "occ":
        sb, sa = segs(BEFORE), segs(AFTER)
        for hw in a[1:]:
            key, senses = lookup(T, hw)
            print(f"== {key}")
            if not senses:
                print("   not in termbase")
                continue
            for n, (tag, t) in enumerate(senses):
                print(f"   |{n} {t}   [{tag}]")
            for i, kk in kws():
                if kk.lower() != hw.lower() or i not in sa:
                    continue
                pb = [n for n, (_, t) in enumerate(senses) if has(t, sb.get(i, ""))]
                pa = [n for n, (_, t) in enumerate(senses) if has(t, sa[i])]
                ch = "" if sb.get(i) == sa[i] else "  CHANGED"
                print(f"   {i}: senses present before {pb} after {pa}{ch}")
    elif a[0] == "seg":
        sa = segs(AFTER, raw=True)
        for i in a[1:]:
            print(f"== {i}\n{sa.get(i)}\n")
    elif a[0] == "ctx":
        # ctx <regex> <block id> [...]: each match of <regex> in the raw segment, with 40 characters around it
        sa = segs(AFTER, raw=True)
        rx = re.compile(a[1], re.I)
        for i in a[2:]:
            t = sa.get(i, "")
            hits = [t[max(0, m.start() - 40):m.end() + 40] for m in rx.finditer(t)]
            print(f"== {i} ({len(hits)})")
            for h in hits[:6]:
                print(f"   …{h}…")
    elif a[0] == "find":
        rx = re.compile(a[1], re.I)
        for hw, ss in T.items():
            for n, (tag, t) in enumerate(ss):
                if rx.search(t):
                    print(f"{hw}|{n}\t{t}\t[{tag[:60]}]")
    elif a[0] == "test":
        sa = segs(AFTER)
        uses = collections.defaultdict(list)
        for i, kk in kws():
            if i in sa:
                uses[kk.lower()].append(i)
        for line in DECR.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            key, new = line.split("\t")[:2]
            hw, n = key.rsplit("|", 1)
            n = int(n)
            k2, ss = lookup(T, hw)
            if not ss:
                print(f"!! {key}: not in termbase")
                continue
            ids = uses[hw.lower()]
            yes = [i for i in ids if has(new, sa[i])]
            other = [i for i in ids if i not in yes and any(has(t, sa[i]) for m, (_, t) in enumerate(ss) if m != n)]
            old = [i for i in ids if i not in yes and has(ss[n][1], sa[i])]
            bad = [i for i in ids if i not in yes and i not in other and i not in old]
            flag = "OK" if not bad and not old else "MISS"
            print(f"{flag} {key} «{ss[n][1]}» -> «{new}»: uses {len(ids)}, new {len(yes)}, other-sense {len(other)} "
                  f"{' '.join(other[:8])}, old kept {len(old)} {' '.join(old[:8])}, neither {len(bad)} {' '.join(bad[:8])}")


if __name__ == "__main__":
    main(sys.argv[1:])
