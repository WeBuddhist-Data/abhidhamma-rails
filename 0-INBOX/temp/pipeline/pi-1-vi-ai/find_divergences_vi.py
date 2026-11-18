"""Find Vietnamese divergences for identical Pāli across the pi-1 Vietnamese plain zero-shot parts.

(a) whole segments / whole lines / clauses / items: group by normalised Pāli (block ID and variant brackets
    stripped, spaces collapsed); list groups where the Vietnamese differs.
(b) recurring phrases: for each Pāli pattern in PHRASES, count per part which candidate Vietnamese forms occur on
    the aligned Vietnamese lines (and how many matching lines carry none of the candidates).

usage: python -I -X utf8 find_divergences_vi.py [out.md] [--bak] [--no-b]
       (default out: divergences.md; --bak scans backup-pre-harmonise/, i.e. the state before the pass)
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, HERE, pairs, segments, norm, short

SPLIT_P = re.compile(r"(?<=[?.;:])\s+")
SPLIT_V = re.compile(r"(?<=[?.;:])\s+")


def vnorm(s):
    return norm(s).rstrip(".?;: ")


def scan_a():
    seg = collections.defaultdict(lambda: collections.defaultdict(list))
    line = collections.defaultdict(lambda: collections.defaultdict(list))
    clause = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for sid, ps, vs in segments(part):
            kp = " / ".join(norm(x) for x in ps)
            kv = " / ".join(norm(x) for x in vs)
            seg[kp][kv].append(f"{short(part)}:{sid}")
            for p, v in zip(ps, vs):
                np_, nv = norm(p), norm(v)
                line[np_][nv].append(f"{short(part)}:{sid}")
                if p.startswith("#"):
                    continue
                cp = [c for c in SPLIT_P.split(np_) if c]
                cv = [c for c in SPLIT_V.split(nv) if c]
                if len(cp) == len(cv) and len(cp) > 1:
                    for a, b in zip(cp, cv):
                        clause[a][vnorm(b)].append(f"{short(part)}:{sid}")
    return seg, line, clause


SPLIT_ITEM_P = re.compile(r"(?<=[?.;:,])\s+|\s+[–—]\s+|…pe…\s*")
SPLIT_ITEM_V = re.compile(r"(?<=[?.;:,])\s+|\s+[–—]\s+|…\s*")


def scan_items():
    """comma / dash / ellipsis items of lines whose item counts match"""
    item = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for sid, ps, vs in segments(part):
            for p, v in zip(ps, vs):
                if p.startswith("#"):
                    continue
                cp = [c for c in SPLIT_ITEM_P.split(norm(p)) if c]
                cv = [c for c in SPLIT_ITEM_V.split(norm(v)) if c]
                if len(cp) == len(cv) and len(cp) > 1:
                    for a, b in zip(cp, cv):
                        item[a.rstrip(",.;:?")][vnorm(b).rstrip(",")].append(f"{short(part)}:{sid}")
    return item


P_STR = re.compile(r"\b(?:Yo|Yā|Yaṃ|yo|yā|yaṃ) (?:tasmiṃ samaye )?(?:evarūpo |evarūpā |evarūpaṃ )?(.+?)\s+[–—]\s")
V_STR = re.compile(r"(?:, tức là|[Bb]ất cứ điều gì là) (.+?)\s+[–—]\s")


def scan_words():
    """synonym strings: Pāli words (space-separated) vs Vietnamese items (comma-separated) when the counts match"""
    word = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for sid, ps, vs in segments(part):
            for p, v in zip(ps, vs):
                p, v = norm(p), norm(v)
                mp, mv = P_STR.findall(p), V_STR.findall(v)
                if len(mp) != len(mv):
                    continue
                for a, b in zip(mp, mv):
                    pw = [w for w in a.replace("…pe…", " ").split() if w]
                    vw = [w.strip() for w in re.split(r",\s+|…\s*", b) if w.strip()]
                    if len(pw) == len(vw) and len(pw) > 2:
                        for x, y in zip(pw, vw):
                            word[x.strip(",.;")][y].append(f"{short(part)}:{sid}")
    return word


def diff(a, b):
    import difflib
    ta, tb = a.split(), b.split()
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            out.append(f"«{' '.join(ta[i1:i2])}» → «{' '.join(tb[j1:j2])}»")
    return "; ".join(out)


def report(groups, title, minlen=0, cross_only=False):
    out = [f"## {title}", ""]
    n = 0
    for k, v in sorted(groups.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        if len(v) < 2 or len(k) < minlen:
            continue
        keys = {vnorm(x) for x in v}
        if len(keys) < 2:
            continue
        if cross_only:
            fsets = [{l.split(':')[0] for l in locs} for locs in v.values()]
            if len(set().union(*fsets)) < 2:
                continue
        n += 1
        out.append(f"### {k[:300]}")
        ranked = sorted(v.items(), key=lambda kv: -len(kv[1]))
        top = ranked[0][0]
        for r, locs in ranked:
            files = sorted({l.split(':')[0] for l in locs})
            d = "" if r == top else f"  ⟨diff vs first: {diff(top, r)[:400]}⟩"
            out.append(f"- [{len(locs)}] {','.join(files)} ({', '.join(locs[:4])}) :: {r[:400]}{d}")
        out.append("")
    out.insert(1, f"groups with differing Vietnamese: {n}")
    return out, n


# (b) phrase table: pali regex -> candidate Vietnamese forms
PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), cands))


# jhāna formula
ph("vivicceva kāmehi", r"vivicceva kāmehi", "hoàn toàn tách khỏi các dục lạc", "tách khỏi các dục lạc", "lìa")
ph("vivicca akusalehi dhammehi", r"vivicca akusalehi", "tách khỏi các hiện tượng bất thiện")
ph("savitakkaṃ savicāraṃ vivekajaṃ", r"savitakkaṃ savicāraṃ vivekajaṃ", "có sự hướng tâm và sự duy trì tâm",
   "sinh từ sự tách biệt")
ph("vitakkavicārānaṃ vūpasamā", r"vitakkavicārānaṃ vūpasamā",
   "khi sự hướng tâm và sự duy trì tâm đã lắng xuống", "lắng dịu", "lắng xuống")
ph("ajjhattaṃ sampasādanaṃ", r"ajjhattaṃ sampasādanaṃ", "có sự trong sáng bên trong và sự hợp nhất của tâm")
ph("pītiyā ca virāgā", r"pītiyā ca virāgā", "khi sự hân hoan phai nhạt")
ph("upekkhako ca viharati", r"upekkhako ca viharati", "an trú bình thản, tỉnh thức và hiểu biết rõ ràng")
ph("sukhassa ca pahānā", r"sukhassa ca pahānā", "khi đã dứt bỏ sự dễ chịu", "dứt bỏ hạnh phúc")
ph("upasampajja viharati", r"upasampajja viharati", "chứng nhập và an trú", "chứng đạt")
ph("bhāveti (subject)", r"bhāveti", "một người tu tập", "người ta tu tập", "tu tập")
ph("jhāna", r"jhān", "tầng thiền", "thiền")
# practice modes
ph("paṭipadā", r"paṭipad", "với cách thực hành khó khăn", "với cách thực hành dễ dàng", "cách thực hành")
ph("abhiññā", r"abhiññ", "sự hiểu biết trực tiếp chậm chạp", "sự hiểu biết trực tiếp nhanh chóng",
   "hiểu biết trực tiếp")
ph("adhipateyya", r"dhipateyy", "làm yếu tố chủ đạo", "với ý muốn", "với sự tinh tấn", "với tâm",
   "với sự thẩm xét", "chủ đạo")
ph("vīmaṃsā", r"vīmaṃs", "sự thẩm xét", "sự tìm hiểu", "sự khảo sát")
ph("kasiṇa", r"kasiṇ", "đề mục bao trùm", "đề mục")
ph("formless spheres", r"ākāsānañc|viññāṇañc|ākiñcañ|nevasaññānāsañ",
   "lĩnh vực không gian vô tận", "lĩnh vực thức vô tận", "lĩnh vực không có gì cả",
   "lĩnh vực không phải tri giác cũng không phải không tri giác", "không vô biên", "thức vô biên", "vô sở hữu")
ph("āruppa / arūpāvacara", r"āruppa|arūpāvacar|arūpūpapatt|arūpajjhān|arūpajhān", "cõi không hình sắc",
   "không hình sắc", "vô sắc")
ph("rūpāvacara", r"(?<!a)rūpāvacar|(?<!a)rūpūpapatt", "cõi hình sắc", "hình sắc", "sắc giới")
ph("kāmāvacara", r"kāmāvacar", "cõi dục lạc", "dục lạc", "dục giới")
ph("sasaṅkhāra", r"(?<!a)sasaṅkhār", "có sự thúc đẩy", "thúc đẩy", "trợ")
ph("asaṅkhāra", r"(?<![a-zāīūṃṅñṭḍṇḷ])asaṅkhārena|(?<![a-zāīūṃṅñṭḍṇḷ])asaṅkhārik", "không có sự thúc đẩy")
ph("bhūmi", r"bhūmīsu|bhūmiy|bhūmik|bhūmak|bhūmi\b", "giai đoạn", "cõi", "cấp độ", "tầng", "địa")
ph("cittuppāda", r"cittuppād", "loại tâm", "sự sinh khởi của tâm", "tâm sinh khởi")
ph("counting line", r"Tasmiṃ kho pana samaye", "Và vào lúc ấy có", "Vào lúc ấy có", "vào lúc ấy")
ph("ṭhapetvā", r"ṭhapetvā|Ṭhapetvā", "ngoại trừ", "Ngoại trừ", "trừ ra", "loại trừ")
ph("tadekaṭṭha", r"[Tt]adekaṭṭh", "cùng hiện diện với", "cùng tồn tại", "cùng một chỗ", "cùng chỗ")
ph("kammassa katattā", r"kammassa katattā", "sinh ra do nghiệp đã được tạo", "đã được tạo và tích lũy",
   "đã được tạo", "do nghiệp")
ph("sāta", r"\bsāt", "khoan khoái", "dễ chịu")
ph("asāta", r"\basāt|nāsāt", "bứt rứt", "không khoan khoái", "khó chịu")
ph("viññatti", r"viññatt", "sự biểu lộ", "biểu lộ", "biểu thị", "truyền đạt")
ph("upacaya", r"upacay", "sự tăng trưởng", "tăng trưởng", "sự tích lũy", "tích tụ")
ph("santati", r"santati", "sự liên tục", "liên tục", "dòng", "tiếp nối")
ph("kakkhaḷa", r"kakkhaḷ", "cứng", "thô cứng", "rắn")
ph("diṭṭhigata", r"diṭṭhigat", "sự mắc kẹt trong các quan điểm", "mắc kẹt", "quan điểm sai lầm", "tà kiến")
ph("micchādiṭṭhi", r"micchādiṭṭh", "quan điểm sai lầm", "tà kiến")
ph("sakkāyadiṭṭhi", r"(?i)sakkāyadiṭṭh", "quan điểm về tự ngã", "thân kiến", "tự ngã")
ph("sīlabbataparāmāsa", r"(?i)sīlabbataparāmās", "sự hiểu sai lệch về giới hạnh và nghi thức",
   "hiểu sai lệch về giới hạnh và nghi thức", "giới cấm thủ")
ph("sīlabbatupādāna", r"(?i)sīlabbatupādān", "sự bám víu vào giới hạnh và nghi thức", "giới hạnh và nghi thức")
ph("lobha", r"\b[Ll]obh", "sự tham lam", "tham lam", "lòng tham")
ph("dosa", r"\b[Dd]os[oaā]", "sự sân hận", "sân hận", "sân")
ph("moha", r"\b[Mm]oh[oaā]", "sự si mê", "si mê")
ph("diṭṭhi", r"[Dd]iṭṭhi", "quan điểm")
ph("vicikicchā", r"[Vv]icikicch", "sự hoài nghi", "hoài nghi", "nghi ngờ")
ph("kaṅkhā", r"[Kk]aṅkh", "sự nghi ngờ", "nghi ngờ")
ph("uddhacca", r"[Uu]ddhacc", "sự xao động", "xao động", "phóng dật")
ph("thina", r"\b[Tt]hin", "sự uể oải", "uể oải", "hôn trầm")
ph("middha", r"[Mm]iddh", "sự đờ đẫn", "đờ đẫn", "thụy miên")
ph("kukkucca", r"[Kk]ukkucc", "sự hối tiếc", "hối tiếc", "hối hận")
ph("māna", r"\b[Mm]ān[oaā]\b|\bmānaṃ|mānasaṃyojan", "sự kiêu mạn", "kiêu mạn", "ngã mạn")
ph("issā", r"\b[Ii]ssā", "sự ganh tị", "ganh tị", "đố kỵ")
ph("macchariya", r"[Mm]acchari", "sự keo kiệt", "keo kiệt", "bủn xỉn")
ph("āsava", r"[Āā]sav", "ô nhiễm", "lậu hoặc")
ph("saṃyojana", r"[Ss]aṃyojan", "xiềng xích", "kiết sử")
ph("gantha", r"[Gg]anth", "nút thắt", "trói buộc")
ph("ogha", r"\b[Oo]gh", "dòng lũ", "bộc lưu")
ph("yoga", r"\b[Yy]og[aāo]", "ách", "trói buộc")
ph("nīvaraṇa", r"[Nn]īvaraṇ", "chướng ngại", "triền cái")
ph("upādāna", r"[Uu]pādān", "sự bám víu", "bám víu", "chấp thủ")
ph("kilesa", r"[Kk]iles", "phiền não")
ph("parāmāsa", r"[Pp]arāmās|parāmaṭṭh", "sự hiểu sai lệch", "hiểu sai lệch", "nắm giữ")
ph("sārāga", r"sārāg", "sự say đắm", "say đắm")
ph("rāga", r"\brāg|kāmarāg|bhavarāg", "sự tham đắm", "tham đắm")
ph("bahūsu", r"bahūsu", "(nhiều ấn bản)", "nhiều ấn bản")
ph("patiṭṭhāho", r"patiṭṭhāh", "sự bám chặt", "bám chặt")
ph("paṭiggāho", r"paṭiggāh", "sự bám chặt", "bám chặt")
ph("sammappadhāna", r"sammappadhān", "nỗ lực đúng đắn")
ph("kabaḷīkāra", r"kabaḷīkār", "thức ăn trong vai trò dưỡng chất", "thức ăn")
ph("Tattha", r"\bTattha\b", "Ở đây", "Trong đó", "Trong số đó")
ph("na vattabba", r"(?i)na vattabb", "không nên nói")
ph("Teva / Tāneva frame", r"(Tāneva|Teyeva|Teva|Sveva|So eva) ", "Chính những", "Chính sự")
ph("cittasamuṭṭhāna", r"cittasamuṭṭhān", "do tâm sinh ra", "sinh từ tâm")
ph("upādārūpa", r"upādārūp|upādā rūp|upādāya rūp", "phái sinh")
ph("mahābhūta", r"mahābhūt", "yếu tố cơ bản")
ph("avasesa", r"[Aa]vases", "còn lại")
ph("count words (Tikaṃ / Dukaṃ / Ekakaṃ …)", r"^(?:Ekakaṃ|Dukaṃ|Tikaṃ|Catukkaṃ|Pañcakaṃ)\.",
   "Các bộ ba", "Các bộ đôi", "Phân loại theo nhóm")
ph("four dots (…pe…. at line end)", r"…pe…\s*\.", "….", "…")
ph("rūpa answer frame (idaṃ taṃ rūpaṃ)", r"[Ii]daṃ taṃ rūpaṃ", "đây là loại vật chất", "Đây là loại vật chất",
   "vật chất này", "Vật chất này")


def scan_b():
    tab = []
    for name, rx, cands in PHRASES:
        cnt = collections.defaultdict(collections.Counter)
        for part in PARTS:
            for p, v in pairs(part):
                if not rx.search(p):
                    continue
                cnt[part]["_lines"] += 1
                hit = False
                for c in cands:
                    k = v.count(c)
                    if k:
                        cnt[part][c] += k; hit = True
                if not hit:
                    cnt[part]["_none"] += 1
        tab.append((name, rx.pattern, cnt))
    out = ["## (b) recurring phrases: candidate Vietnamese forms per part", "",
           "Counts are occurrences of each candidate string on Vietnamese lines whose aligned Pāli matches; "
           "_lines = matching lines, _none = matching lines with no candidate (overlapping candidates are counted separately).", ""]
    for name, pat, cnt in tab:
        out.append(f"### {name}  (`{pat}`)")
        for part in PARTS:
            if part in cnt:
                c = cnt[part]
                items = ", ".join(f"{k}={v}" for k, v in c.items() if not k.startswith("_"))
                out.append(f"- {short(part)}: lines={c['_lines']} none={c['_none']} | {items}")
        out.append("")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    vi_common.ensure_backup()
    if "--bak" in sys.argv:  # scan the pre-pass files
        vi_common.CUR["vdir"] = vi_common.BAK
    dest = args[0] if args else os.path.join(HERE, "divergences.md")
    seg, line, clause = scan_a()
    o1, n1 = report(seg, "(a1) whole segments: identical Pāli, differing Vietnamese")
    o2, n2 = report(line, "(a2) whole lines: identical Pāli, differing Vietnamese", minlen=12)
    o3, n3 = report(clause, "(a3) clauses (sentence parts of lines whose clause counts match)", minlen=12)
    o4, n4 = report(scan_items(), "(a4) comma/dash/ellipsis items of lines whose item counts match (cross-part only)",
                    minlen=6, cross_only=True)
    o5, n5 = report(scan_words(), "(a5) words of synonym strings (Pāli word ↔ Vietnamese comma item, cross-part only)",
                    minlen=3, cross_only=True)
    o4 += o5
    ob = scan_b() if "--no-b" not in sys.argv else []
    src = "backup-pre-harmonise (before the pass)" if "--bak" in sys.argv else "current outputs"
    head = ["# pi-1 Vietnamese zero-shot: divergences (find_divergences_vi.py)", "", f"Scanned: {src}.", "",
            f"(a1) segment groups: {n1}; (a2) line groups: {n2}; (a3) clause groups: {n3}; (a4) item groups: {n4}; (a5) string-word groups: {n5}", ""]
    open(dest, "w", encoding="utf-8", newline="\n").write("\n".join(head + o1 + o2 + o3 + o4 + ob) + "\n")
    print("segments", n1, "lines", n2, "clauses", n3, "items", n4, "words", n5, "->", dest)


if __name__ == "__main__":
    main()
