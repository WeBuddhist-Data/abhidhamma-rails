# -*- coding: utf-8 -*-
"""pi-6 Vietnamese rails: user-approved review fixes, stage 2, book-wide answer heads (H1-H4).

Brief: 0-INBOX\\temp\\pipeline\\vi-review-fixes-stage2-brief.md; findings review\\review-findings.md A5, A6.
  H1  separate cases in one head: «và» before each NEW case (see case_join()).
  H2  faculty-attribute groups: participle first, then «mà» + the attributes in the Pāli order.
  H3  asaññasattānaṃ in a run of plane-beings = «chúng sinh Vô Tưởng».
  H4  the ye-group tail (… parinibbāyissanti tesaṃ cavantānaṃ / upapajjantānaṃ / tāsaṃ …) moved into the ye group.

Builds every chapter from rails\\backup-pre-heads\\<ch> (copied once, never overwritten), so it can be re-run.
Rewrites rails\\review-fixes-log-heads.tsv (file, block id, old head, new head, rule) on every run.
Asserts: identical Pāli heads give identical Vietnamese heads across all chapters (no new split); line counts;
NFC; no CR; no forbidden strings.

Usage: python -I -X utf8 -B review_fixes_heads_vi.py [apply|dry|trans]
"""
import os, re, sys, shutil, collections, unicodedata

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
VI = os.path.join(ROOT, r"AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters")
PI = os.path.join(ROOT, r"AI_translation\pali\pi-6_split_chapters")
RAILS = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
BACKUP = os.path.join(RAILS, "backup-pre-heads")
LOG = os.path.join(RAILS, "review-fixes-log-heads.tsv")
CHS = sorted(f for f in os.listdir(PI) if f.endswith(".md") and f not in ("preamble.md",))
BAD = ["—", ":-", "….", "được được", "là là", "chánh niệm", "vẫn đã", "se" + "ed", "  ", "\r"]


def rd(p):
    with open(p, encoding="utf-8", newline="") as f:
        return f.read()


def wr(p, t):
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


IDRX = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def block_ids(lines):
    ids = [None] * len(lines)
    cur = None
    for i in range(len(lines) - 1, -1, -1):
        if not lines[i].strip():
            cur = None
            continue
        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", lines[i])
        if m and cur is None:
            cur = m.group(1)
        ids[i] = cur
    return ids


# ---------------------------------------------------------------------------------------------- H3
H3 = [  # (old, new, Pāli that must be present the same number of times)
    ("chúng sinh trong cõi Tịnh Cư, cõi Vô Tưởng và cõi không hình sắc",
     "chúng sinh trong cõi Tịnh Cư, chúng sinh Vô Tưởng và chúng sinh trong cõi không hình sắc",
     "suddhāvāsānaṃ asaññasattānaṃ arūpānaṃ"),
    ("chúng sinh trong cõi Tịnh Cư và cõi Vô Tưởng",
     "chúng sinh trong cõi Tịnh Cư và chúng sinh Vô Tưởng", "suddhāvāsānaṃ asaññasattānaṃ"),
    ("chúng sinh trong cõi gồm năm khối và cõi Vô Tưởng",
     "chúng sinh trong cõi gồm năm khối và chúng sinh Vô Tưởng", "pañcavokārānaṃ asaññasattānaṃ"),
]


def h3(v, p):
    pl = p.lower()
    for old, new, pk in H3:
        n = v.count(old)
        if n:
            assert pl.count(pk) >= n, ("H3 pali", old, p)
            v = v.replace(old, new)
    return v


# ---------------------------------------------------------------------------------------------- H2
PA = {  # Pāli attribute -> Vietnamese attribute (the chapters' own strings)
    "sacakkhukānaṃ": "có mắt", "acakkhukānaṃ": "không có mắt",
    "sasotakānaṃ": "có tai", "asotakānaṃ": "không có tai",
    "saghānakānaṃ": "có mũi", "aghānakānaṃ": "không có mũi",
    "sacittakānaṃ": "có tâm", "acittakānaṃ": "không có tâm",
    "sarūpakānaṃ": "có vật chất", "arūpakānaṃ": "không có vật chất",
    "sahetukānaṃ": "có gốc rễ", "ahetukānaṃ": "không có gốc rễ",
    "ñāṇasampayuttānaṃ": "gắn liền với hiểu biết", "ñāṇavippayuttānaṃ": "không gắn liền với hiểu biết",
    "somanassena": "có niềm vui đi kèm", "vinā somanassena": "không có niềm vui đi kèm",
    "upekkhāya": "có sự bình thản đi kèm", "vinā upekkhāya": "không có sự bình thản đi kèm",
}
PSEX = {"itthīnaṃ", "purisānaṃ", "na itthīnaṃ", "na purisānaṃ"}
PPRE = {"itaresaṃ", "pacchimabhavikānaṃ"}
PPART = re.compile(r"^(upapajjantānaṃ|upapajjantīnaṃ|uppajjantānaṃ|uppajjantīnaṃ|cavantānaṃ|cavantīnaṃ)$")
PPLANE = re.compile(r"^(kāmāvacar|rūpāvacar|arūpāvacar|arūp|catuvokār|pañcavokār|ekavokār|asaññasatt|suddhāvās|"
                    r"kāmadhāt|rūpadhāt|arūpadhāt|apāy)\w*$")

# (abhisametāvīnaṃ / anabhisametāvīnaṃ are termbase person nouns «người đã / chưa thấu hiểu», not attributes: kept)
VATTR = r"(?:không có |có )(?:mắt|tai|mũi|tâm|vật chất|gốc rễ)|(?:không )?gắn liền với hiểu biết"
VFEEL = r"(?:không )?có (?:niềm vui|sự bình thản) đi kèm"
VPLANE = (r"(?:vào|khỏi) cõi (?:dục lạc|hình sắc|không hình sắc|gồm năm khối|gồm bốn khối|gồm một khối|Vô Tưởng|"
          r"Tịnh Cư|khổ)(?: và cõi (?:dục lạc|hình sắc|không hình sắc|gồm năm khối|gồm bốn khối))?")
VSEX = r"(?:không )?làm người (?:nữ|nam)(?:, cũng không làm người (?:nữ|nam))?"
VG = re.compile(r"những người(?P<pre> khác| thuộc kiếp sống cuối cùng)?(?P<attrs>(?: (?:%s),?)*)"
                r" đang (?P<part>tái sinh|chết đi)(?P<plane> %s)?(?P<sex> %s)?(?P<feel>,? %s)?"
                r"(?![\wÀ-ỹ])" % (VATTR, VPLANE, VSEX, VFEEL))


def pali_groups(p):
    """participle groups of a Pāli line in order: [(kind, [attr keys in Pāli order])]."""
    t = re.findall(r"[^\s.,?;\[\]()]+", p)
    out = []
    for k, w in enumerate(t):
        if not PPART.match(w):
            continue
        kind = "chết đi" if w.startswith("cavant") else "tái sinh"
        j, attrs = k - 1, []
        while j >= 0:
            x = t[j].lower()
            if j > 0 and t[j - 1].lower() in ("vinā", "na") and (t[j - 1].lower() + " " + x) in PA.keys() | PSEX:
                key = t[j - 1].lower() + " " + x
                j -= 2
            elif x in PA or x in PSEX or x in PPRE or PPLANE.match(x):
                key = x
                j -= 1
            else:
                break
            if key in PA:
                attrs.append(key)
        out.append((kind, attrs[::-1]))
    return out


ERRS = []
RUNJOIN = []
OUTSIDE = []


def h2(v, p, ctx):
    pg = pali_groups(p)
    vparts = [m.group(1) for m in re.finditer(r"đang (tái sinh|chết đi)(?![\wÀ-ỹ])", v)]
    matches = list(VG.finditer(v))
    todo = [m for m in matches if m.group("attrs").strip() or m.group("feel")]
    if not todo:
        return v
    # pair each Vietnamese participle with the Pāli participle of the same kind, in order
    if [k for k, _ in pg] != vparts:
        ERRS.append(("H2 pairing", ctx, vparts, [k for k, _ in pg], p[:400]))
        return v
    # index of each Vietnamese participle occurrence
    pos = [m.start() for m in re.finditer(r"đang (?:tái sinh|chết đi)(?![\wÀ-ỹ])", v)]
    res, last = [], 0
    for m in todo:
        part_at = m.start() + m.group(0).index(" đang ") + 1
        idx = pos.index(part_at)
        pattrs = [PA[a] for a in pg[idx][1]]
        vattrs = [a.strip().rstrip(",") for a in re.findall(r" (?:%s),?" % VATTR, m.group("attrs"))]
        if m.group("feel"):
            vattrs.append(m.group("feel").lstrip(", ").strip())
        if sorted(pattrs) != sorted(vattrs):
            raise AssertionError(("H2 attrs", ctx, pattrs, vattrs, m.group(0)))
        new = ("những người" + (m.group("pre") or "") + " đang " + m.group("part") + (m.group("plane") or "")
               + (m.group("sex") or "") + " mà " + ", ".join(pattrs))
        res.append(v[last:m.start()] + new)
        last = m.end()
        # a following run item after the «mà …» attributes: «, và» (as the consistency pass's «, và …» joins),
        # so the next group is not read as one more thing the persons have / lack
        if re.match(r" và (?:những người|chúng sinh|các bậc|tất cả)", v[last:]):
            res.append(",")
            RUNJOIN.append(ctx)
    res.append(v[last:])
    return "".join(res)


# ---------------------------------------------------------------------------------------------- H4
YE1 = (r"những người(?: nam| nữ)?(?: (?:%s))? nào (?:(?!nào |, thì )[^.?;])*? sẽ nhập Niết-bàn trọn vẹn" % VATTR)
H4RX = re.compile(r"(?P<cap>[Nn])(?P<body>%s(?: và %s)*), khi những người ấy đang (?P<part>chết đi|tái sinh)"
                  r"(?![\wÀ-ỹ])" % (YE1[1:], YE1))
YE1C = re.compile(r"(?P<cap>[Nn])hững người(?P<sx> nam| nữ)?(?P<attr> (?:%s))? nào (?P<rest>(?:(?!nào |, thì )[^.?;])*?)"
                  r" sẽ nhập Niết-bàn trọn vẹn" % VATTR)


def h4(v, p, ctx):
    def one(m):
        part = m.group("part")
        body = m.group("cap") + m.group("body")
        def cl(c):
            attr = c.group("attr")
            mid = (attr.strip() + ", ") if attr else ""
            return (c.group("cap") + "hững người" + (c.group("sx") or "") + " đang " + part + " mà " + mid
                    + c.group("rest") + " sẽ nhập Niết-bàn trọn vẹn")
        new = YE1C.sub(cl, body)
        assert "nào" not in new, (ctx, new)
        return new
    n_v = len(H4RX.findall(v))
    if not n_v:
        return v
    n_p = len(re.findall(r"parinibbāyissanti (?:tesaṃ|tāsaṃ) (?:cavant|upapajjant|uppajjant)", p))
    assert n_v == n_p, ("H4 count", ctx, n_v, n_p, v[:200])
    return H4RX.sub(one, v)


# ---------------------------------------------------------------------------------------------- H1
BR = re.compile(r"\[[^\]]*\]")


def seg_type(s):
    s0 = s[3:] if s.startswith("và ") else s
    if re.match(r"(?:[Vv]ào khoảnh khắc|[Kk]hi tâm )", s0):
        if "mà ngay sau đó" in s0:
            return "MA"          # the anantarā moment: brings its own persons
        return "M"
    if s0 in ("trong đời sống", "Trong đời sống"):
        return "L"
    if re.match(r"khi những người ấy đang (?:chết đi|tái sinh)$", s0):
        return "T"
    if re.match(r"[Ởở] ", s0):
        return "G"
    return "C"


def group_kind(text):
    """G subtype: D = persons dying / being reborn (participle in the last group), P = place, N = other persons."""
    t = text[3:] if text.startswith("và ") else text
    if re.match(r"[Ởở] (?:cõi|tầng thiền|cấp độ)", t) and "những người" not in t and "chúng sinh" not in t:
        return "P"
    last = re.split(r"(?: và |, )(?=những người|chúng sinh|các bậc|tất cả)", t)[-1]
    if re.search(r"đang (?:chết đi|tái sinh)(?![\wÀ-ỹ])", last):
        return "D"
    return "N"


def pieces_of(head):
    """split a head into pieces [(type, text)]; brackets protected."""
    prot = {}
    def keep(m):
        k = "\x00%d\x00" % len(prot)
        prot[k] = m.group(0)
        return k
    h = BR.sub(keep, head)
    segs = h.split(", ")
    pcs = []
    for s in segs:
        t = seg_type(s)
        if not pcs:
            pcs.append([("G" if t == "C" else t), [s]])
        elif t == "C":
            pcs[-1][1].append(s)
        else:
            pcs.append([t, [s]])
    out = []
    for t, ss in pcs:
        txt = ", ".join(ss)
        for k, val in prot.items():
            txt = txt.replace(k, val)
        if t == "G":
            t = "G" + group_kind(txt)
        out.append((t, txt))
    return out


def new_case(prev, cur, nxt=None):
    """True when piece cur starts a new case after piece prev (H1); nxt = type of the piece after cur."""
    if cur == "MA":                      # the anantarā moment brings its own persons
        return True
    if prev in ("M", "MA"):              # after a moment: persons, place, «trong đời sống», another moment
        return cur in ("GD", "GN", "GP", "L", "M", "T")
    if prev in ("GD", "T"):              # pavatte after persons dying / being reborn
        return cur == "L" or (cur == "GP" and nxt in ("M", "L"))
    if prev == "GN":                     # a place with its own moment after other persons
        return cur == "GP" and nxt in ("M", "L")
    return False


TRANS = collections.Counter()
TRANS_EX = {}
TRANS_ALL = collections.defaultdict(set)


def case_join(head, ctx=None):
    pcs = pieces_of(head)
    out = [pcs[0][1]]
    for k in range(1, len(pcs)):
        pt, ct, ctext = pcs[k - 1][0], pcs[k][0], pcs[k][1]
        nxt = pcs[k + 1][0] if k + 1 < len(pcs) else None
        key = (pt, ct + ("+" + nxt if ct == "GP" and nxt else ""), ctext.startswith("và "))
        TRANS[key] += 1
        TRANS_EX.setdefault(key, (head, ctx))
        TRANS_ALL[key[:2]].add((head, ctx))
        if new_case(pt, ct, nxt) and not ctext.startswith("và "):
            ctext = "và " + ctext
        out.append(ctext)
    return ", ".join(out)


SPLIT = re.compile(r"(?<=[.?!])\s+(?=\S)")


def head_spans(v):
    """(start, end) of every answer head in a Vietnamese line: a non-question sentence's text before «, thì »,
    or, when it has no «thì», before its first «…» (cut answers)."""
    body = IDRX.sub("", v)
    spans = []
    pos = 0
    for s in SPLIT.split(body):
        st = body.index(s, pos)
        pos = st + len(s)
        if s.endswith("?") or s.startswith(("(a)", "(b)", "Còn ", "(")) or "có phải" in s:
            continue
        if not re.match(r"(?:Ở|Vào|Khi|Những người|Trong đời sống)", s):
            continue
        # every chunk between «…» cuts that opens a head («Ở A, thì …… ở B, thì …», «Ở A… ở B…»)
        off = 0
        for n, chunk in enumerate(s.split("…")):
            c0 = len(chunk) - len(chunk.lstrip())
            c = chunk.lstrip()
            if (n == 0 or re.match(r"(?:[Ởở]|Vào|vào|Khi) ", c)) and not re.match(
                    r"ở (?:những người ấy|người ấy|nơi ấy|đó)\b", c):
                e = c.find(", thì ")
                if e < 0:
                    e = len(c.rstrip())
                if e > 0:
                    spans.append((st + off + c0, st + off + c0 + e))
            off += len(chunk) + 1
    return spans


def h1(v, ctx):
    spans = head_spans(v)
    if not spans:
        return v
    out, last = [], 0
    for a, b in spans:
        out.append(v[last:a])
        out.append(case_join(v[a:b], ctx))
        last = b
    out.append(v[last:])
    return "".join(out)


RESIDUE = [
    ("H2", re.compile(r"những người(?: khác| thuộc kiếp sống cuối cùng)?(?: (?:%s),?)+ đang (?:tái sinh|chết đi)" % VATTR)),
    ("H2", re.compile(r"đang (?:tái sinh|chết đi)(?: %s)?(?: %s)?,? %s" % (VPLANE, VSEX, VFEEL))),
    ("H3", re.compile(r"chúng sinh trong cõi [^,.?…]*?(?:, | và )cõi Vô Tưởng")),
    ("H4", re.compile(r"sẽ nhập Niết-bàn trọn vẹn, khi những người ấy đang")),
]


# ---------------------------------------------------------------------------------------------- driver
def pali_heads(p):
    """Pāli head of each sentence (text before the resumptive pronoun)."""
    return [re.split(r" (?:tesaṃ|tassa|tattha|tāsaṃ|te|so)\b", s)[0]
            for s in SPLIT.split(IDRX.sub("", p).strip())]


def fix_line(v, p, ctx):
    rules = []
    v0 = v
    v1 = h3(v0, p)
    if v1 != v0:
        rules.append("H3")
    v2 = h2(v1, p, ctx)
    if v2 != v1:
        rules.append("H2")
    v3 = h4(v2, p, ctx)
    if v3 != v2:
        rules.append("H4")
    v4 = h1(v3, ctx)
    if v4 != v3:
        rules.append("H1")
    STEPS[:] = [("H3", v0, v1), ("H2", v1, v2), ("H4", v2, v3), ("H1", v3, v4)]
    return v4, rules


STEPS = []


def head_rules(k):
    """rules that changed the k-th head of the line just fixed."""
    out = []
    for r, a, b in STEPS:
        ha = [a[x:y] for x, y in head_spans(a)]
        hb = [b[x:y] for x, y in head_spans(b)]
        if len(ha) == len(hb) and k < len(ha) and ha[k] != hb[k]:
            out.append(r)
    return out


def head_map(lines_p, lines_v, acc, ch):
    for a, b in zip(lines_p, lines_v):
        if not b.strip():
            continue
        ph = pali_heads(a)
        vs = [b[x:y] for x, y in head_spans(b)]
        bs = IDRX.sub("", b)
        vsent = SPLIT.split(bs.strip())
        if len(ph) != len(vsent):
            continue
        for s_p, s_v in zip(ph, vsent):
            hs = [h for h in vs if s_v.startswith(h)]
            if hs:
                acc[s_p].add(hs[0])


def main(mode):
    os.makedirs(BACKUP, exist_ok=True)
    for ch in CHS:
        b = os.path.join(BACKUP, ch)
        if not os.path.exists(b):
            shutil.copyfile(os.path.join(VI, ch), b)
    log = [("file", "block_id", "old_head", "new_head", "rule")]
    per = collections.defaultdict(collections.Counter)
    before, after = collections.defaultdict(set), collections.defaultdict(set)
    lb, la = collections.defaultdict(set), collections.defaultdict(set)
    for ch in CHS:
        src = rd(os.path.join(BACKUP, ch))
        assert "\r" not in src
        vl = src.split("\n")
        pl = rd(os.path.join(PI, ch)).replace("\r", "").split("\n")
        assert len(vl) == len(pl), ch
        ids = block_ids(vl)
        out = []
        for i, (v, p) in enumerate(zip(vl, pl)):
            ctx = "%s %s" % (ch, ids[i])
            nv, rules = fix_line(v, p, ctx) if v.strip() else (v, [])
            if nv != v:
                oh = [v[a:b] for a, b in head_spans(v)]
                nh = [nv[a:b] for a, b in head_spans(nv)]
                assert len(oh) == len(nh), ctx
                pairs = [(k, x, y) for k, (x, y) in enumerate(zip(oh, nh)) if x != y]
                assert pairs, ("change outside a head", ctx, v, nv)
                for k, x, y in pairs:
                    rr = head_rules(k)
                    assert rr, ctx
                    log.append((ch, ids[i] or "", x, y, "+".join(sorted(rr))))
                    for r in rr:
                        per[ch][r] += 1
                    per[ch]["heads"] += 1
                # nothing outside the heads may change
                rest_o = "".join(v[a:b] for a, b in zip([0] + [e for _, e in head_spans(v)],
                                                        [s for s, _ in head_spans(v)] + [len(v)]))
                rest_n = "".join(nv[a:b] for a, b in zip([0] + [e for _, e in head_spans(nv)],
                                                         [s for s, _ in head_spans(nv)] + [len(nv)]))
                if rest_o != rest_n:
                    OUTSIDE.append((ctx, rest_o[:300], rest_n[:300]))
                per[ch]["lines"] += 1
            out.append(nv)
        txt = unicodedata.normalize("NFC", "\n".join(out))
        assert len(txt.split("\n")) == len(vl)
        for b in BAD:
            assert b not in txt, (ch, repr(b))
        for name, rx in RESIDUE:
            left = rx.findall(txt)
            assert not left, (ch, name, left[:3])
        head_map(pl, vl, before, ch)
        head_map(pl, txt.split("\n"), after, ch)
        for a, b0, b1 in zip(pl, vl, txt.split("\n")):
            if a.strip():
                lb[IDRX.sub("", a)].add(IDRX.sub("", b0))
                la[IDRX.sub("", a)].add(IDRX.sub("", b1))
        if mode == "apply" and txt != rd(os.path.join(VI, ch)):
            wr(os.path.join(VI, ch), txt)
    for e in ERRS:
        print("ERR", e)
    for e in OUTSIDE:
        print("OUTSIDE", e)
    assert not ERRS and not OUTSIDE
    split_b = {k for k, s in before.items() if len(s) > 1}
    split_a = {k for k, s in after.items() if len(s) > 1}
    new_split = split_a - split_b
    for k in sorted(new_split)[:10]:
        print("NEW SPLIT", k, after[k])
    assert not new_split, len(new_split)
    lsb = {k for k, s in lb.items() if len(s) > 1}
    lsa = {k for k, s in la.items() if len(s) > 1}
    assert lsa <= lsb, sorted(lsa - lsb)[:3]
    print("identical Pāli lines with >1 Vietnamese line: before %d, after %d" % (len(lsb), len(lsa)))
    print("«, và» after a «mà …» group:", len(RUNJOIN), sorted(set(RUNJOIN))[:12])
    if mode == "apply":
        with open(LOG, "w", encoding="utf-8", newline="\n") as f:
            for row in log:
                f.write("\t".join(row) + "\n")
    tot = collections.Counter()
    for ch in CHS:
        if per[ch]:
            print("%-28s lines %4d heads %4d | H1 %4d  H2 %4d  H3 %3d  H4 %3d" % (
                ch, per[ch]["lines"], per[ch]["heads"], per[ch]["H1"], per[ch]["H2"], per[ch]["H3"], per[ch]["H4"]))
            tot.update(per[ch])
    print("TOTAL lines %(lines)d heads %(heads)d | H1 %(H1)d  H2 %(H2)d  H3 %(H3)d  H4 %(H4)d"
          % collections.defaultdict(int, tot))
    print("log rows", len(log) - 1, "| Pāli heads with >1 Vietnamese: before %d, after %d" % (len(split_b), len(split_a)))
    print("Pāli head keys", len(after))
    if mode == "diff":
        rule, lo, hi = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
        seen = collections.OrderedDict()
        for row in log[1:]:
            if re.fullmatch(rule, row[4]):
                seen.setdefault((row[2], row[3]), "%s %s" % (row[0][:5], row[1]))
        items = list(seen.items())
        print("unique", len(items))
        for (o, n), w in items[lo:hi]:
            print("[%s]\n  - %s\n  + %s" % (w, o, n))
    if mode == "show":
        want = tuple(sys.argv[2].split(","))
        seen = set()
        for (pt, ct), s in TRANS_ALL.items():
            if (pt, ct) == want:
                for h, c in sorted(s):
                    if h not in seen:
                        seen.add(h)
                        print(c, "|", h)
    if mode == "trans":
        for k, n in sorted(TRANS.items(), key=lambda x: -x[1]):
            h, c = TRANS_EX[k]
            print(n, k, "|", c, "|", h[:230])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "dry")
