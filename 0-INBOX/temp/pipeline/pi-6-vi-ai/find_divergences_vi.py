"""Find Vietnamese divergences for identical Pāli in the pi-6 Vietnamese plain zero-shot (Yamaka, 44 files).

Adapted from pi-5-vi-ai/find_divergences_vi.py (pi-5 files untouched).
(a1) whole segments, (a2) whole lines (headings included), (a3) sentences (lines split on «. ? ; !» + space, only
     where the Pāli and the Vietnamese line give the same number of sentences). Groups keyed by the normalised Pāli
     (block ID and variant brackets stripped, spaces collapsed, no space before punctuation or «…», first letter
     lowercased); groups whose normalised Vietnamese differs are listed with locations and a word diff.
(s2) / (s3) frame skeletons: the same at line / sentence level after masking the member names (khandha, āyatana,
     dhātu, sacca, saṅkhāra, indriya, anusaya, the kusala / akusala / abyākata dhammā of the Dhammayamaka and the
     sa- / a-cakkhuka … attributes) as «X» on both sides (Vietnamese names from the builders' tables). Only pairs
     with the same number of «X» on both sides and at least one «X» are compared, so every reported group is the same
     sentence frame with only the members changed.
(b)  variant brackets: identical Pāli bracket, differing Vietnamese bracket.
(c)  named points: per Pāli pattern, which candidate Vietnamese forms occur per chapter.
(e)  sentence-final punctuation: aligned sentences where the Pāli ends in «?» and the Vietnamese not, or the reverse.

usage: python -I -X utf8 -B find_divergences_vi.py [out.md] [--bak]
       (default out: divergences.md; --bak scans backup-pre-harmonise/, i.e. the state before the pass)
"""
import os, re, sys, collections, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, HERE, pairs, segments, norm, short

SPLIT = re.compile(r"(?<=[?.;!])\s+")

# ------------------------------------------------------------------ member masks
KHANDHA = {"rūpa": "vật chất", "vedanā": "cảm giác", "saññā": "tri giác", "saṅkhāra": "tạo tác", "viññāṇa": "thức"}
AYATANA = {"cakkh": "mắt", "sot": "tai", "ghān": "mũi", "jivh": "lưỡi", "kāy": "thân", "rūp": "hình sắc",
           "sadd": "âm thanh", "gandh": "mùi", "ras": "vị", "phoṭṭhabb": "vật xúc chạm", "man": "ý",
           "dhamm": "đối tượng của ý"}
DHATU = {"cakkhu": "yếu tố mắt", "sota": "yếu tố tai", "ghāna": "yếu tố mũi", "jivhā": "yếu tố lưỡi",
         "kāya": "yếu tố thân", "rūpa": "yếu tố hình sắc", "sadda": "yếu tố âm thanh", "gandha": "yếu tố mùi",
         "rasa": "yếu tố vị", "phoṭṭhabba": "yếu tố vật xúc chạm", "cakkhuviññāṇa": "yếu tố thức qua mắt",
         "sotaviññāṇa": "yếu tố thức qua tai", "ghānaviññāṇa": "yếu tố thức qua mũi",
         "jivhāviññāṇa": "yếu tố thức qua lưỡi", "kāyaviññāṇa": "yếu tố thức qua thân", "mano": "yếu tố ý",
         "manoviññāṇa": "yếu tố ý thức", "dhamma": "yếu tố đối tượng của ý"}
SACCA = {"dukkha": "khổ đau", "samudaya": "sự phát sinh", "nirodha": "sự chấm dứt", "magga": "con đường"}
SANKHARA = {"kāya": "sự tạo tác bằng thân", "vacī": "sự tạo tác bằng lời nói", "citta": "sự tạo tác bằng tâm"}
INDRIYA = {"cakkhund": "mắt", "sotind": "tai", "ghānind": "mũi", "jivhind": "lưỡi", "kāyind": "thân", "manind": "ý",
           "itthind": "nữ tính", "purisind": "nam tính", "jīvitind": "sống", "sukhind": "dễ chịu",
           "dukkhind": "khó chịu", "somanassind": "niềm vui", "domanassind": "nỗi buồn", "upekkhind": "bình thản",
           "saddhind": "niềm tin", "vīriyind": "tinh tấn", "satind": "tỉnh thức", "samādhind": "định tâm",
           "paññind": "trí tuệ", "anaññātaññassāmītind": "biết được điều chưa từng biết",
           "aññind": "hiểu biết trọn vẹn", "aññātāvind": "của người đã hiểu biết trọn vẹn"}
ANUSAYA = {"kāmarāg": "tham đắm dục lạc", "kāmārāg": "tham đắm dục lạc", "paṭigh": "ác cảm", "mān": "kiêu mạn",
           "diṭṭh": "quan điểm", "vicikicch": "hoài nghi", "bhavarāg": "tham đắm hiện hữu", "avijj": "vô minh"}
ORGAN = {"cakkhuk": "mắt", "sotak": "tai", "ghānak": "mũi", "jivhak": "lưỡi", "kāyak": "thân"}


def alt(keys):
    return "|".join(sorted((re.escape(k) for k in keys), key=len, reverse=True))


I = re.IGNORECASE
P_MASK = [
    re.compile(rf"\b(?:{alt(KHANDHA)})kkhandh\w*", I),
    re.compile(rf"\b(?:{alt(AYATANA)})āyatan\w*", I),
    re.compile(rf"\b(?:{alt(SACCA)})sacc\w*", I),
    re.compile(rf"\b(?:{alt(SANKHARA)})saṅkhār\w*", I),
    re.compile(rf"\b(?:{alt(INDRIYA)})riy\w*", I),
    re.compile(rf"\b(?:{alt(ANUSAYA)})ānusay\w*", I),
    re.compile(r"\b(?:a?kusal|abyākat)(?:ā|e|aṃ|ānaṃ)(?=(?: ca)? dhamm| uppādakkhaṇe| bhaṅgakkhaṇe)", I),
    re.compile(r"(?<![a-zā])(?:a?kusal|abyākat)(?=a?vippayutt|a?sampayutt)", I),
]
# dhātu names are members only in the Dhātuyamaka (4); elsewhere kāma- / rūpa- / arūpadhātu are planes («cõi …»)
P_DHATU = re.compile(rf"\b(?:{alt(DHATU)})dhātu(?:ṃ|ū)?(?![\wā])", I)
P_ORGAN = re.compile(rf"\b(s?a)(?:{alt(ORGAN)})(?=ānaṃ|ā\b|o\b|aṃ\b)", I)
V_NAMES = sorted(set(
    [f"khối {v}" for v in KHANDHA.values()] + [f"lĩnh vực {v}" for v in AYATANA.values()] + list(DHATU.values())
    + [f"sự thật về {v}" for v in SACCA.values()] + list(SANKHARA.values())
    + [f"năng lực {v}" for v in INDRIYA.values()] + [f"khuynh hướng tiềm ẩn {v}" for v in ANUSAYA.values()]
    + [f"các hiện tượng {v}" for v in ("thiện", "bất thiện", "không xác định về mặt đạo đức")]), key=len, reverse=True)
V_MASK = re.compile("(?:" + "|".join(re.escape(v) for v in V_NAMES) + r")(?![\wà-ỹ])", I)
V_ORGAN = re.compile(r"(?<=có )(?:mắt|tai|mũi|lưỡi|thân)(?![\wà-ỹ])")


def mask_p(s, part=""):
    for rx in P_MASK:
        s = rx.sub("X", s)
    if part.startswith("4-"):
        s = P_DHATU.sub("X", s)
    s = P_ORGAN.sub(lambda m: m.group(1) + "X", s)
    return s


def mask_v(s):
    s = V_MASK.sub("X", s)
    s = V_ORGAN.sub("X", s)
    return s


# ------------------------------------------------------------------ grouping
def low1(s):
    """lowercase the first letter (after any opening quote / label): sentence-initial capitals are not divergences"""
    m = re.match(r"[“‘\"(]*", s)
    i = m.end()
    return s[:i] + s[i:i + 1].lower() + s[i + 1:]


def key(s):
    """final «.;:,!» and spaces stripped; a final «?» is kept (a cut «…pe…?» question differs from a cut «…pe….»)"""
    return low1(norm(s)).rstrip(".;:,! ")


def vkey(s):
    return low1(norm(s)).rstrip(".;:,! ")


# answer heads: the Pāli persons / places / times before the resumptive tesaṃ / tassa / tāsaṃ (tattha), and the
# Vietnamese before «, thì ở …» (statement sentences only; question sentences have no such resumptive)
P_HEAD = re.compile(r"^(?!\((?:Ka|Kha)\)|Yassa|Yattha|yassa|yattha)(.+?) (?:tesaṃ|tassa|tāsaṃ|tesañca|tassā)(?: tattha)?(?: |$)")
V_HEAD = re.compile(r"^(?!\([ab]\))(.+?), thì ở ")
P_RES = re.compile(r"(?<!\bca) (?:tesaṃ|tassa|tāsaṃ|tesañca|tassā)(?= )")   # compared only when there is one resumptive
HEADS = []


def collect():
    seg = collections.defaultdict(lambda: collections.defaultdict(list))
    line = collections.defaultdict(lambda: collections.defaultdict(list))
    sent = collections.defaultdict(lambda: collections.defaultdict(list))
    sk_line = collections.defaultdict(lambda: collections.defaultdict(list))
    sk_sent = collections.defaultdict(lambda: collections.defaultdict(list))
    heads = collections.defaultdict(lambda: collections.defaultdict(list))
    HEADS.append(heads)
    punct = []
    for part in PARTS:
        for sid, ps, vs in segments(part):
            loc = f"{short(part)}:{sid}"
            seg[" / ".join(key(x) for x in ps)][" / ".join(vkey(x) for x in vs)].append(loc)
            for p, v in zip(ps, vs):
                line[key(p)][vkey(v)].append(loc)
                mp, mv = mask_p(norm(p), part), mask_v(norm(v))
                if mp.count("X") and mp.count("X") == mv.count("X"):
                    sk_line[key(mp)][vkey(mv)].append(loc)
                if p.startswith("#"):
                    continue
                cp = [c for c in SPLIT.split(norm(p)) if c.strip()]
                cv = [c for c in SPLIT.split(norm(v)) if c.strip()]
                if len(cp) != len(cv):
                    continue
                for a, b in zip(cp, cv):
                    qa = a.rstrip("”’\"' )").endswith("?")
                    qb = b.rstrip("”’\"' )").endswith("?")
                    if qa != qb:
                        punct.append((loc, a, b))
                    if len(cp) > 1:
                        sent[key(a)][vkey(b)].append(loc)
                    ma, mb = mask_p(a, part), mask_v(b)
                    if len(cp) > 1 and ma.count("X") and ma.count("X") == mb.count("X"):
                        sk_sent[key(ma)][vkey(mb)].append(loc)
                    hp, hv = P_HEAD.match(a), V_HEAD.match(b)
                    if hp and hv and len(hp.group(1)) > 6 and len(P_RES.findall(a)) == 1 \
                            and b.count(", thì ở ") == 1:
                        heads[key(mask_p(hp.group(1), part))][vkey(mask_v(hv.group(1)))].append(loc)
    return seg, line, sent, sk_line, sk_sent, punct


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
            files = sorted({l.split(':')[0] for l in locs}, key=lambda x: [int(y) for y in x.split("-")] if x[0].isdigit() else [0])
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
            out.append(f"  - [{len(locs)}] ch{','.join(sorted(set(locs)))} :: {b}")
    out.insert(1, f"groups: {n}")
    out.append("")
    return out, n


# ------------------------------------------------------------------ (c) named points
PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), cands))


ph("asammohantena", r"asammohantena", "mà không mê lầm", "một cách không nhầm lẫn", "không để nhầm lẫn",
   "không nhầm lẫn", "không mê lầm")
ph("two-part citta kinds (…vippayutta…vippayuttacitta)", r"vippayutta\w*vippayuttacitt",
   "tâm vừa không gắn liền", " và không gắn liền với")
ph("cut question …pe…? / …?", r"…(?:pe…)?\?", "… không?", "…?")
ph("sabbattha", r"sabbattha", "ở mọi nơi", "ở mọi chỗ")
ph("pavatte", r"\bpavatte\b", "trong đời sống", "trong quá trình diễn tiến")
ph("yassa cittassa anantarā", r"cittassa anantarā", "ngay sau", "liền sau")
ph("Aggamaggasamaṅgī", r"(?i)aggamaggasamaṅg", "con đường tối thượng", "con đường cao nhất")
ph("avasesā puggalā", r"avasesā puggalā", "những hạng người còn lại", "những người còn lại")
ph("bare Sabbesaṃ (not + participle)", r"Sabbesaṃ (?!\w+antānaṃ)", "tất cả chúng sinh", "tất cả mọi người",
   "tất cả những người")
ph("uppanna (aspect)", r"\buppann", "ở trạng thái đã sinh khởi", "đã sinh khởi")
ph("bhaṅgā (dhātu sections)", r"bhaṅgā", "phải phân chia", "phải phân tích")
ph("kassaci", r"\bkassaci\b", "ở một số người", "ở một số chúng sinh")
ph("na vattabbo", r"vattabb", "không nên nói", "nên nói")
ph("pacchimabhavika", r"acchimabhavik", "những người thuộc kiếp sống cuối cùng", "kiếp sống cuối cùng")
ph("somanassena (beings)", r"\bsomanassena\b", "có niềm vui đi kèm", "với niềm vui", "cùng với niềm vui")
ph("upekkhāya (beings)", r"\bupekkhāya\b", "có sự bình thản đi kèm", "với sự bình thản")


def scan_c():
    out = ["## (c) named points: candidate Vietnamese forms per chapter", "",
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
    if not os.path.isabs(dest):
        dest = os.path.join(HERE, dest)
    s, l, c, kl, ks, punct = collect()
    o1, n1 = report(s, "(a1) whole segments: identical Pāli, differing Vietnamese")
    o2, n2 = report(l, "(a2) whole lines (headings included): identical Pāli, differing Vietnamese", minlen=8)
    o3, n3 = report(c, "(a3) sentences: identical Pāli, differing Vietnamese", minlen=8)
    o5, n5 = report(kl, "(s2) line skeletons (members masked as X): identical Pāli frame, differing Vietnamese frame",
                    minlen=8)
    o6, n6 = report(ks, "(s3) sentence skeletons (members masked as X): identical Pāli frame, differing Vietnamese "
                        "frame", minlen=8)
    o7, n7 = report(HEADS[0], "(h) answer heads (members masked as X): identical Pāli head (before tesaṃ / tassa …), "
                              "differing Vietnamese head (before «, thì ở …»)", minlen=6)
    o6 = o6 + o7
    ob, nb = brackets()
    src = "backup-pre-harmonise (before the pass)" if "--bak" in sys.argv else "current outputs"
    head = ["# pi-6 Vietnamese zero-shot: divergences (find_divergences_vi.py)", "", f"Scanned: {src}.", "",
            f"(a1) segment groups: {n1}; (a2) line groups: {n2}; (a3) sentence groups: {n3}; "
            f"(s2) line-skeleton groups: {n5}; (s3) sentence-skeleton groups: {n6}; (h) answer-head groups: {n7}; "
            f"(b) bracket groups: {nb}; "
            f"(e) punctuation cases: {len(punct)}", ""]
    open(dest, "w", encoding="utf-8", newline="\n").write(
        "\n".join(head + o1 + o2 + o3 + o5 + o6 + ob + scan_e(punct) + scan_c()) + "\n")
    print("segments", n1, "lines", n2, "sentences", n3, "line-skeletons", n5, "sentence-skeletons", n6, "heads", n7,
          "brackets", nb, "punct", len(punct), "->", dest)


if __name__ == "__main__":
    main()
