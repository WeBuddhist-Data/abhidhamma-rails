"""Find Vietnamese divergences for identical Pāli in the pi-4 Vietnamese plain zero-shot (Puggalapaññatti, 12 files).

Adapted from pi-3-vi-ai/find_divergences_vi.py (pi-3 files untouched).
(a1) whole segments, (a2) whole lines, (a3) sentences (lines split on «. ? ; !» + space, only where the Pāli and the
     Vietnamese line give the same number of sentences), (a4) members: sentences further split on «…» / «…pe…»
     (only where both sides give the same number of pieces). Groups keyed by the normalised Pāli (block ID and
     variant brackets stripped, spaces collapsed, no space before punctuation or «…», first letter lowercased);
     groups whose normalised Vietnamese differs are listed with locations and a word diff.
(b)  variant brackets: every Pāli bracket with its Vietnamese bracket (label used per kind).
(c)  recurring terms and phrases: per Pāli pattern, which candidate Vietnamese forms occur per chapter.

usage: python -I -X utf8 find_divergences_vi.py [out.md] [--bak]
       (default out: divergences.md; --bak scans backup-pre-harmonise/, i.e. the state before the pass)
"""
import os, re, sys, collections, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, HERE, pairs, segments, norm, short

SPLIT = re.compile(r"(?<=[?.;!])\s+")
SPLIT_P = re.compile(r"…pe…|…")
SPLIT_V = re.compile(r"…")


def low1(s):
    """lowercase the first letter (after any opening quote): sentence-initial capitals are not divergences"""
    m = re.match(r"[“‘\"(]*", s)
    i = m.end()
    return s[:i] + s[i:i + 1].lower() + s[i + 1:]


def key(s):
    return low1(norm(s)).rstrip(".?;:,! …")


def vkey(s):
    return low1(norm(s)).rstrip(".?;:,! …")


def collect():
    seg = collections.defaultdict(lambda: collections.defaultdict(list))
    line = collections.defaultdict(lambda: collections.defaultdict(list))
    sent = collections.defaultdict(lambda: collections.defaultdict(list))
    item = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for sid, ps, vs in segments(part):
            loc = f"{short(part)}:{sid}"
            seg[" / ".join(key(x) for x in ps)][" / ".join(vkey(x) for x in vs)].append(loc)
            for p, v in zip(ps, vs):
                line[key(p)][vkey(v)].append(loc)
                if p.startswith("#"):
                    continue
                cp = [c for c in SPLIT.split(norm(p)) if c.strip()]
                cv = [c for c in SPLIT.split(norm(v)) if c.strip()]
                if len(cp) != len(cv):
                    continue
                for a, b in zip(cp, cv):
                    if len(cp) > 1:
                        sent[key(a)][vkey(b)].append(loc)
                    ip = [x for x in SPLIT_P.split(a) if x.strip(" .,;?")]
                    iv = [x for x in SPLIT_V.split(b) if x.strip(" .,;?")]
                    if len(ip) == len(iv) and len(ip) > 1:
                        for x, y in zip(ip, iv):
                            item[key(x).strip(" ,")][vkey(y).strip(" ,")].append(loc)
    return seg, line, sent, item


def diff(a, b):
    ta, tb = a.split(), b.split()
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            out.append(f"«{' '.join(ta[i1:i2])}» → «{' '.join(tb[j1:j2])}»")
    return "; ".join(out)


def report(groups, title, minlen=0):
    out = [f"## {title}", ""]
    n = 0
    for k, v in sorted(groups.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        if len(k) < minlen or len(v) < 2:
            continue
        n += 1
        out.append(f"### {k[:300]}")
        ranked = sorted(v.items(), key=lambda kv: -len(kv[1]))
        top = ranked[0][0]
        for r, locs in ranked:
            files = sorted({l.split(':')[0] for l in locs}, key=lambda x: (len(x), x))
            d = "" if r == top else f"  ⟨diff vs first: {diff(top, r)[:500]}⟩"
            out.append(f"- [{len(locs)}] ch{','.join(files)} ({', '.join(locs[:6])}) :: {r[:400]}{d}")
        out.append("")
    out.insert(1, f"groups with differing Vietnamese: {n}")
    return out, n


# ------------------------------------------------------------------ (b) variant brackets
def brackets():
    out = ["## (b) variant brackets (Pāli → Vietnamese)", ""]
    for part in PARTS:
        for p, v in pairs(part):
            bp = re.findall(r"\[[^\]]*\]", p)
            bv = re.findall(r"\[[^\]]*\]", v)
            if not bp and not bv:
                continue
            for i in range(max(len(bp), len(bv))):
                a = bp[i] if i < len(bp) else "—missing—"
                b = bv[i] if i < len(bv) else "—missing—"
                out.append(f"- {short(part)}: {a} → {b}")
    out.append("")
    return out


# ------------------------------------------------------------------ (c) recurring terms
PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), cands))


ph("Kathañca puggalo … hoti?", r"Kathañca puggalo", "Người như thế nào là", "Và như thế nào là", "Như thế nào là",
   "Thế nào là")
ph("Evaṃ puggalo … hoti.", r"Evaṃ (?:kho )?puggalo", "Như vậy là", "Như vậy, người", "Như thế là")
ph("Katamo ca puggalo", r"[Kk]atamo ca puggalo", "Thế nào là")
ph("Katame … puggalā (person plural question)", r"[Kk]atame[^?]*puggalā\?", "là những ai?", "là gì?")
ph("samannāgat-", r"samannāgat", "được trang bị", "sở hữu", "có đủ")
ph("So (sentence-initial)", r"(?:^|[.?;] )So ", "Người ấy", "Vị ấy", "Người đó", "Vị đó")
ph("ayaṃ vuccati puggalo", r"ayaṃ vuccati puggalo", "người này được gọi là", "Người này được gọi là")
ph("ime vuccanti puggalā", r"ime vuccanti puggalā", "những người này được gọi là", "Những người này được gọi là")
ph("(aṭṭhakathā)", r"\(aṭṭhakathā\)", "(Chú giải)", "(chú giải)")
ph("Idha / Idhekacco", r"[Ii]dhekacc|Idha ", "Ở đời này", "Ở đây")
ph("puratthimena narassa / nagarassa", r"puratthimena", "thành phố", "người")
ph("Seyyathāpi", r"[Ss]eyyathāpi", "Như ", "như ", "Giống như ", "giống như ", "Ví như ", "Cũng như ")
ph("tathūpamo ayaṃ puggalo", r"tathūpamo ayaṃ puggalo", "người này cũng giống như thế")
ph("santo saṃvijjamān-", r"santo saṃvijjamān", "đang có mặt, được tìm thấy")
ph("Evamevaṃ", r"Evamevaṃ", "Cũng như thế")
ph("Katame N? (count question)", r"Katame (?:dve|tayo|cattāro|pañca|cha|satta|aṭṭha|nava|dasa)\?", "hạng nào?")
ph("Idha panekacco", r"[Ii]dha panekacc", "Ở đời này, lại có", "ở đời này, lại có")
ph("Evarūpopi idhekacco", r"Evarūpopi idhekacco", "Ở đời này, cũng có", "cũng có")
ph("Puna caparaṃ", r"Puna caparaṃ", "Lại nữa")
ph("dukkhassantaṃ karoti / -kara", r"dukkhassanta", "đi đến tận cùng của khổ đau", "người đi đến tận cùng của khổ đau")
ph("diṭṭheva dhamme", r"diṭṭheva dhamme|diṭṭhe ceva dhamme", "ngay trong đời này", "trong đời này")
ph("kāyassa bhedā paraṃ maraṇā", r"kāyassa bhedā paraṃ maraṇā", "khi thân tan rã, sau khi chết")
ph("abhininnāmeti", r"abhininnāmeti", "hướng tâm", "dẫn tâm")
ph("vaṇṇapokkharatāya", r"vaṇṇapokkharatāya", "vẻ đẹp dung mạo", "nước da", "dung sắc")
ph("pāsādik-", r"pāsādik", "đáng mến", "dễ mến")
ph("bhikkhūsu (santo saṃvijjamānā)", r"saṃvijjamān\w* bhikkhūsu", "giữa các tỳ-khưu")
ph("lokasmiṃ (santo saṃvijjamānā)", r"saṃvijjamān\w* lokasmiṃ", "trong thế gian")
ph("vimuccati (-pi)", r"āsavāpi cittaṃ vimuccati", "khỏi cả ô nhiễm", "khỏi ô nhiễm")
ph("…pe… / …", r"…", "…")


def scan_c():
    out = ["## (c) recurring terms and phrases: candidate Vietnamese forms per chapter", "",
           "Counts: occurrences of each candidate on Vietnamese lines whose aligned Pāli matches; lines = matching "
           "lines; none = matching lines with no candidate.", ""]
    for name, rx, cands in PHRASES:
        out.append(f"### {name}  (`{rx.pattern}`)")
        for part in PARTS:
            c = collections.Counter()
            for p, v in pairs(part):
                n = len(rx.findall(p))
                if not n:
                    continue
                c["_lines"] += 1
                c["_pali"] += n
                hit = False
                for cand in cands:
                    k = v.count(cand)
                    if k:
                        c[cand] += k; hit = True
                if not hit:
                    c["_none"] += 1
            if c["_lines"]:
                items = ", ".join(f"«{k}»={v}" for k, v in c.items() if not k.startswith("_"))
                out.append(f"- ch{short(part)}: lines={c['_lines']} pāli={c['_pali']} none={c['_none']} | {items}")
        out.append("")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    vi_common.ensure_backup()
    if "--bak" in sys.argv:
        vi_common.CUR["vdir"] = vi_common.BAK
    dest = args[0] if args else os.path.join(HERE, "divergences.md")
    s, l, c, i = collect()
    o1, n1 = report(s, "(a1) whole segments: identical Pāli, differing Vietnamese")
    o2, n2 = report(l, "(a2) whole lines: identical Pāli, differing Vietnamese", minlen=8)
    o3, n3 = report(c, "(a3) sentences: identical Pāli, differing Vietnamese", minlen=8)
    o4, n4 = report(i, "(a4) members (sentences split on «…» / «…pe…»): identical Pāli, differing Vietnamese",
                    minlen=4)
    src = "backup-pre-harmonise (before the pass)" if "--bak" in sys.argv else "current outputs"
    head = ["# pi-4 Vietnamese zero-shot: divergences (find_divergences_vi.py)", "", f"Scanned: {src}.", "",
            f"(a1) segment groups: {n1}; (a2) line groups: {n2}; (a3) sentence groups: {n3}; (a4) member groups: {n4}",
            ""]
    open(dest, "w", encoding="utf-8", newline="\n").write(
        "\n".join(head + o1 + o2 + o3 + o4 + brackets() + scan_c()) + "\n")
    print("segments", n1, "lines", n2, "sentences", n3, "members", n4, "->", dest)


if __name__ == "__main__":
    main()
