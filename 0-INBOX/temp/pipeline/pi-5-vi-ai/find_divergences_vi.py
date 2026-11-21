"""Find Vietnamese divergences for identical Pāli in the pi-5 Vietnamese plain zero-shot (Kathāvatthu, 32 files).

Adapted from pi-4-vi-ai/find_divergences_vi.py (pi-4 files untouched).
(a1) whole segments, (a2) whole lines, (a3) sentences (lines split on «. ? ; !» + space, only where the Pāli and the
     Vietnamese line give the same number of sentences), (a4) members: sentences further split on «…» / «…pe…»
     (only where both sides give the same number of pieces). Groups keyed by the normalised Pāli (block ID and
     variant brackets stripped, spaces collapsed, no space before punctuation or «…», first letter lowercased);
     groups whose normalised Vietnamese differs are listed with locations and a word diff.
(b)  variant brackets: identical Pāli bracket, differing Vietnamese bracket.
(c)  recurring terms and phrases: per Pāli pattern, which candidate Vietnamese forms occur per chapter.
(d)  kathā names: heading (where one exists) vs closing line ("X niṭṭhitā."), per kathā.
(e)  sentence-final punctuation: aligned sentences where the Pāli ends in «?» and the Vietnamese not, or the reverse.

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


QFRAME = re.compile(r"^(?:có phải là |có phải |chẳng phải )")


def vkey(s):
    """the Vietnamese key: the question frame of a member (có phải … không / chẳng phải … sao) is positional
    (sentence-initial or after …pe…), so it is stripped before comparing"""
    k = low1(norm(s)).rstrip(".?;:,! …")
    k = QFRAME.sub("", k)
    k = re.sub(r"(?: không| sao)$", "", k)
    return k


def collect():
    seg = collections.defaultdict(lambda: collections.defaultdict(list))
    line = collections.defaultdict(lambda: collections.defaultdict(list))
    sent = collections.defaultdict(lambda: collections.defaultdict(list))
    item = collections.defaultdict(lambda: collections.defaultdict(list))
    punct = []
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
                    qa = a.rstrip("”’\"' ").endswith("?")
                    qb = b.rstrip("”’\"' ").endswith("?")
                    if qa != qb:
                        punct.append((loc, a, b))
                    if len(cp) > 1:
                        sent[key(a)][vkey(b)].append(loc)
                    ip = [x for x in SPLIT_P.split(a) if x.strip(" .,;?")]
                    iv = [x for x in SPLIT_V.split(b) if x.strip(" .,;?")]
                    if len(ip) == len(iv) and len(ip) > 1:
                        for x, y in zip(ip, iv):
                            item[key(x).strip(" ,")][vkey(y).strip(" ,")].append(loc)
    return seg, line, sent, item, punct


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
    g = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for p, v in pairs(part):
            bp = re.findall(r"\[[^\]]*\]", p)
            bv = re.findall(r"\[[^\]]*\]", v)
            if len(bp) != len(bv):
                g["COUNT MISMATCH " + short(part)][f"{bp} → {bv}"].append(short(part))
                continue
            for a, b in zip(bp, bv):
                g[a][b].append(short(part))
    out = ["## (b) variant brackets: identical Pāli bracket, differing Vietnamese", ""]
    n = 0
    for a, d in sorted(g.items()):
        if len(d) < 2 and not a.startswith("COUNT"):
            continue
        n += 1
        out.append(f"- {a}")
        for b, locs in sorted(d.items(), key=lambda kv: -len(kv[1])):
            out.append(f"  - [{len(locs)}] ch{','.join(sorted(set(locs), key=lambda x: (len(x), x)))} :: {b}")
    out.insert(1, f"groups: {n}")
    out.append("")
    # label use: which labels occur with which sigla-pattern
    lab = collections.Counter()
    for part in PARTS:
        for p, v in pairs(part):
            for b in re.findall(r"\[[^\]]*\]", v):
                for m in re.finditer(r"(dị bản|khác chính tả|[a-zà-ỹ ]+?) \(", b):
                    pass
                lab[re.sub(r"\(.*", "", b)[:30]] += 1
    out.append("label openings: " + ", ".join(f"«{k}»={v}" for k, v in lab.most_common(30)))
    out.append("")
    return out, n


# ------------------------------------------------------------------ (c) recurring terms
PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), cands))


ph("Āmantā? (question mark)", r"Āmantā\?", "Đúng vậy?", "Đúng vậy.")
ph("punabbhav-", r"punabbhav", "sự hiện hữu mới", "hiện hữu mới", "sự tái sinh", "tái sinh")
ph("gotrabhū / gotrabhu-", r"gotrabh", "người chuyển đổi dòng dõi", "người chuyển dòng dõi")
ph("X-pariyāpanna", r"pariyāpann", "nằm trong", "thuộc về")
ph("samāpattesiya / upapattesiya", r"esiy", "tìm cầu", "tìm kiếm")
ph("atīta- / anāgata- (attribute)", r"(?i)\batīt|\banāgat", "thuộc quá khứ", "thuộc tương lai", "vật chất quá khứ",
   "thức quá khứ", "vật chất tương lai", "thức tương lai")
ph("nekkhamm-", r"nekkhamm", "sự từ bỏ", "sự xuất ly", "xuất ly")
ph("kanta (kant-)", r"\bkant[aāoe]", "đáng yêu mến", "đáng yêu thích")
ph("patthanā", r"patthan", "sự mong ước", "mong ước", "sự ước nguyện", "ước nguyện", "sự mong muốn", "mong muốn")
ph("apubbaṃ acarimaṃ", r"(?i)apubbaṃ acarimaṃ", "cùng một lúc, không trước không sau", "không trước không sau")
ph("cakkhunā rūpaṃ passati", r"cakkhunā rūpaṃ", "bằng mắt", "dùng mắt")
ph("paṭivijānāti", r"paṭivijānā", "nhận biết rõ", "nhận biết")
ph("ariyo aṭṭhaṅgiko maggo", r"ariy\w* aṭṭhaṅgik\w* magg|aṭṭhaṅgik\w* magg", "con đường tám chi phần cao quý",
   "con đường cao quý tám chi phần", "con đường cao quý có tám chi phần", "con đường tám chi phần")
ph("anāsav-", r"anāsav", "không phải là đối tượng của ô nhiễm", "không còn ô nhiễm", "không có ô nhiễm",
   "không liên quan đến ô nhiễm")
ph("yoni", r"\byoni", "cách thức sinh ra", "cách sinh")
ph("sammukhībhāv-", r"sammukhībhāv", "sự hiện diện", "sự có mặt", "hiện diện", "đối diện")
ph("sukhavedaniy-", r"sukhavedaniy", "được cảm nhận là dễ chịu", "đưa đến cảm giác dễ chịu")
ph("dukkhavedaniy-", r"dukkhavedaniy", "được cảm nhận là khó chịu", "đưa đến cảm giác khó chịu")
ph("vipākābyākat-", r"vipākābyākat", "quả của nghiệp", "thuộc loại quả")
ph("kiriyābyākat-", r"kiriyābyākat", "thuộc loại chức năng", "chức năng", "hành động")
ph("…ti vattabbo", r"ti vattabb", "nên gọi là", "nên được gọi là")
ph("dhammappaṭisaraṇ-", r"dhammappaṭisaraṇ|dhammapaṭisaraṇ", "chỗ nương tựa", "nơi nương tựa")
ph("dadāti / deti", r"\bdadāti|\bdeti\b|\bdadeyya|\bdinn", "cho", "dâng", "bố thí")
ph("buddho / buddhā", r"\bbuddh[oāa]\b", "Đức Phật", "bậc giác ngộ", "chư Phật", "các Đức Phật")
ph("samādhi", r"samādh", "sự định tâm", "định tâm")
ph("vīriy-", r"vīriy", "sự tinh tấn", "tinh tấn")
ph("āneñj-", r"āneñj", "trạng thái bất động", "sự bất động", "bất động")
ph("saṇṭhāti / saṇṭhahati", r"saṇṭhā|saṇṭhah", "đứng vững", "hình thành")
ph("yoniso / ayoniso manasikāra", r"yoniso", "chú tâm đúng cách", "chú tâm không đúng cách", "chú tâm một cách khôn ngoan",
   "không khôn ngoan", "khôn ngoan", "đúng cách")
ph("sukhavipāk-", r"sukhavipāk", "có quả là hạnh phúc", "có kết quả hạnh phúc", "có quả trổ dễ chịu", "dễ chịu")
ph("dukkhavipāk-", r"dukkhavipāk", "có quả là khổ đau", "có kết quả khổ đau", "có quả trổ khó chịu", "khó chịu")
ph("sukhudray-", r"sukhudray", "dễ chịu", "hạnh phúc")
ph("dukkhudray-", r"dukkhudray", "khó chịu", "khổ đau")
ph("iṭṭhaphal-", r"iṭṭhaphal", "có kết quả đáng mong muốn", "có quả đáng mong muốn")
ph("aniṭṭhaphal-", r"aniṭṭhaphal", "có kết quả không đáng mong muốn", "có quả không đáng mong muốn")
ph("saphal-", r"saphal", "có kết quả", "có quả")
ph("savipāk-", r"savipāk", "có quả", "có kết quả", "có quả trổ")
ph("avipāk-", r"(?<![a-zā])avipāk","không có quả", "không có kết quả", "không có quả trổ")
ph("parakataṃ sukhadukkhaṃ", r"parakataṃ sukhadukkh|sayaṃkataṃ sukhadukkh", "hạnh phúc và khổ đau", "dễ chịu và khó chịu",
   "sự dễ chịu và sự khó chịu", "khổ và vui", "lạc và khổ")
ph("Nanu vuttaṃ bhagavatā", r"Nanu vuttaṃ bhagavatā", "Chẳng phải Đức Thế Tôn đã nói thế này sao –",
   "Chẳng phải Đức Thế Tôn đã nói –")
ph("ruhiruppād-", r"ruhiruppād|lohituppād", "kẻ làm chảy máu Như Lai", "kẻ làm chảy máu", "làm chảy máu")
ph("uḷār-", r"uḷār", "bậc vĩ đại", "vĩ đại")
ph("cakkavatti", r"cakkavatt", "người sẽ làm vua chuyển luân", "vua chuyển luân")
ph("kāyikaṃ / cetasikaṃ dukkhaṃ", r"kāyikaṃ dukkh|cetasikaṃ dukkh|kāyika|cetasika", "khổ đau", "khó chịu")
ph("paññatti", r"paññatt", "sự định danh", "khái niệm", "định danh")
ph("Tassuddānaṃ", r"Tassuddānaṃ", "Tóm tắt của chương này –")
ph("paṇṇāsak-", r"paṇṇāsak", "Nhóm năm mươi", "nhóm năm mươi", "Nhóm nửa năm mươi")
ph("…pe… / …", r"…", "…")


def scan_c():
    out = ["## (c) recurring terms and phrases: candidate Vietnamese forms per chapter", "",
           "Counts: occurrences of each candidate on Vietnamese lines whose aligned Pāli matches; lines = matching "
           "lines; none = matching lines with no candidate. Candidates may overlap (a longer form also counts its "
           "substrings).", ""]
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


# ------------------------------------------------------------------ (d) kathā names
HEAD = re.compile(r"^#+\s*(?:\(\d+(?:-\d+)?\)\s*)?(?:\d+(?:-\d+)?\.\s*)?(.*?)\s*\^[\w-]+\s*$")
VHEAD = re.compile(r"^#+\s*(?:\(\d+(?:-\d+)?\)\s*)?(?:\d+(?:-\d+)?\.?\s*)?(?:Bàn )?(.*?)\s*\^[\w-]+\s*$")
CLOSE = re.compile(r"^(.*?kathā)\s*(?:\[[^\]]*\]\s*)?niṭṭhitā\.?")
VCLOSE = re.compile(r"^Phần bàn (.*)\s+đã hoàn tất\.?(?:\s*\^[\w-]+)?\s*$")


def scan_d():
    out = ["## (d) kathā names: heading vs closing line", "",
           "Listed only where the Vietnamese name in the heading and in the closing line differ.", ""]
    n = 0
    for part in PARTS:
        last = None
        for p, v in pairs(part):
            if p.startswith("#") and "kathā" in p:
                mp, mv = HEAD.match(p), VHEAD.match(v)
                last = (mp.group(1) if mp else p, mv.group(1) if mv else v)
                continue
            mp, mv = CLOSE.match(p), VCLOSE.match(v)
            if mp and last:
                vname = re.sub(r"\s*\[[^\]]*\]", "", mv.group(1)) if mv else v
                pn = re.sub(r"\s*\[[^\]]*\]", "", mp.group(1))
                if vname.lower() != last[1].lower():
                    n += 1
                    same = "same Pāli" if pn.lower().replace(" ", "") == last[0].lower().replace(" ", "") else "Pāli differs"
                    out.append(f"- ch{short(part)}: heading «{last[0]}» = «{last[1]}» | closing «{pn}» = «{vname}» ({same})")
                last = None
    out.insert(1, f"differences: {n}")
    out.append("")
    return out


def scan_e(punct):
    out = ["## (e) sentence-final punctuation: Pāli «?» vs Vietnamese not «?» (or the reverse)", "", f"cases: {len(punct)}", ""]
    for loc, a, b in punct:
        out.append(f"- {loc}: PI …{a[-90:]} || VI …{b[-110:]}")
    out.append("")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    vi_common.ensure_backup()
    if "--bak" in sys.argv:
        vi_common.CUR["vdir"] = vi_common.BAK
    dest = args[0] if args else os.path.join(HERE, "divergences.md")
    s, l, c, i, punct = collect()
    o1, n1 = report(s, "(a1) whole segments: identical Pāli, differing Vietnamese")
    o2, n2 = report(l, "(a2) whole lines: identical Pāli, differing Vietnamese", minlen=8)
    o3, n3 = report(c, "(a3) sentences: identical Pāli, differing Vietnamese", minlen=8)
    o4, n4 = report(i, "(a4) members (sentences split on «…» / «…pe…»): identical Pāli, differing Vietnamese",
                    minlen=4)
    ob, nb = brackets()
    src = "backup-pre-harmonise (before the pass)" if "--bak" in sys.argv else "current outputs"
    head = ["# pi-5 Vietnamese zero-shot: divergences (find_divergences_vi.py)", "", f"Scanned: {src}.", "",
            f"(a1) segment groups: {n1}; (a2) line groups: {n2}; (a3) sentence groups: {n3}; (a4) member groups: {n4}; "
            f"(b) bracket groups: {nb}; (e) punctuation cases: {len(punct)}",
            ""]
    open(dest, "w", encoding="utf-8", newline="\n").write(
        "\n".join(head + o1 + o2 + o3 + o4 + ob + scan_d() + scan_e(punct) + scan_c()) + "\n")
    print("segments", n1, "lines", n2, "sentences", n3, "members", n4, "brackets", nb, "punct", len(punct), "->", dest)


if __name__ == "__main__":
    main()
