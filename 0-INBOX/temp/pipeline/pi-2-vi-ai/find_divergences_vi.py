"""Find Vietnamese divergences for identical Pāli in the pi-2 Vietnamese plain zero-shot (and against pi-1).

(a) inside pi-2, across all chapters: whole segments / whole lines / clauses / comma-dash items grouped by the
    normalised Pāli (block ID and variant brackets stripped, spaces collapsed, no space before punctuation);
    groups whose Vietnamese differs are listed.
(b) pi-2 against pi-1 (final, reviewed): pi-2 segments / lines / clauses whose normalised Pāli is identical to a
    pi-1 segment / line / clause, but whose Vietnamese differs from pi-1's (pi-1 wins).
(c) recurring terms and phrases: for each Pāli pattern in PHRASES, count per chapter which candidate Vietnamese
    forms occur on the aligned Vietnamese lines (and how many matching lines carry none of them).

usage: python -I -X utf8 find_divergences_vi.py [out.md] [--bak]
       (default out: divergences.md; --bak scans backup-pre-harmonise/, i.e. the state before the pass)
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, P1_PARTS, HERE, pairs, pairs1, segments, segments1, norm, short

SPLIT = re.compile(r"(?<=[?.;:!])\s+")
SPLIT_ITEM_P = re.compile(r"(?<=[?.;:,])\s+|\s+[–—]\s+|…pe…\s*")
SPLIT_ITEM_V = re.compile(r"(?<=[?.;:,])\s+|\s+[–—]\s+|…\s*")


def vnorm(s):
    return norm(s).rstrip(".?;:,! ")


def short1(part):
    return "p1:" + (part[:4] if part[0].isdigit() and part[1] == "-" else part[:3])


def collect(segs_of, parts, tag):
    seg = collections.defaultdict(lambda: collections.defaultdict(list))
    line = collections.defaultdict(lambda: collections.defaultdict(list))
    clause = collections.defaultdict(lambda: collections.defaultdict(list))
    item = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in parts:
        for sid, ps, vs in segs_of(part):
            loc = f"{tag(part)}:{sid}"
            seg[" / ".join(norm(x) for x in ps)][" / ".join(norm(x) for x in vs)].append(loc)
            for p, v in zip(ps, vs):
                np_, nv = norm(p), norm(v)
                line[np_][nv].append(loc)
                if p.startswith("#"):
                    continue
                cp = [c for c in SPLIT.split(np_) if c]
                cv = [c for c in SPLIT.split(nv) if c]
                if len(cp) == len(cv) and len(cp) > 1:
                    for a, b in zip(cp, cv):
                        clause[a][vnorm(b)].append(loc)
                ip = [c for c in SPLIT_ITEM_P.split(np_) if c]
                iv = [c for c in SPLIT_ITEM_V.split(nv) if c]
                if len(ip) == len(iv) and len(ip) > 1:
                    for a, b in zip(ip, iv):
                        item[a.rstrip(",.;:?")][vnorm(b)].append(loc)
    return seg, line, clause, item


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
        if len({vnorm(x) for x in v}) < 2:
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
            files = sorted({l.split(':')[0] for l in locs}, key=lambda x: (len(x), x))
            d = "" if r == top else f"  ⟨diff vs first: {diff(top, r)[:400]}⟩"
            out.append(f"- [{len(locs)}] {','.join(files)} ({', '.join(locs[:4])}) :: {r[:400]}{d}")
        out.append("")
    out.insert(1, f"groups with differing Vietnamese: {n}")
    return out, n


def report_b(g2, g1, title, minlen=0):
    """pi-2 Pāli identical to pi-1 Pāli; pi-2 Vietnamese differs from pi-1 (most frequent pi-1 form)"""
    out = [f"## {title}", ""]
    n = 0
    for k, v in sorted(g2.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        if k not in g1 or len(k) < minlen:
            continue
        p1 = sorted(g1[k].items(), key=lambda kv: -len(kv[1]))
        p1forms = {vnorm(x) for x in g1[k]}
        bad = [(r, locs) for r, locs in v.items() if vnorm(r) not in p1forms]
        if not bad:
            continue
        n += 1
        out.append(f"### {k[:300]}")
        top = p1[0][0]
        for r, locs in p1:
            out.append(f"- pi-1 [{len(locs)}] ({', '.join(locs[:3])}) :: {r[:400]}")
        for r, locs in sorted(bad, key=lambda kv: -len(kv[1])):
            out.append(f"- pi-2 [{len(locs)}] ({', '.join(locs[:4])}) :: {r[:400]}  ⟨vs pi-1: {diff(top, r)[:400]}⟩")
        out.append("")
    out.insert(1, f"groups with pi-2 Vietnamese differing from pi-1: {n}")
    return out, n


# ------------------------------------------------------------------ (c) recurring terms
PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), cands))


# realm and god names (pi-1 4-02 / 4-03 / 5)
ph("Akaniṭṭha", r"[Aa]kaniṭṭh", "Sắc Cứu Cánh")
ph("brahmaloka / brahmakāyika", r"brahmalok|[Bb]rahmakāyik|[Bb]rahmapārisajj|[Bb]rahmapurohit|[Mm]ahābrahm",
   "cõi Phạm Thiên", "Phạm Thiên", "Phạm Chúng", "Phạm Phụ", "Đại Phạm")
ph("Paranimmitavasavattī", r"[Pp]aranimmitavasavatt", "Tha Hóa Tự Tại")
ph("Nimmānarati", r"[Nn]immānarat", "Hóa Lạc")
ph("Tusita", r"[Tt]usit", "Đâu Suất")
ph("Yāma", r"\b[Yy]ām[āa]", "Dạ Ma")
ph("Tāvatiṃsa", r"[Tt]āvatiṃs", "Ba Mươi Ba")
ph("Cātumahārājika", r"[Cc]ātu(m)?mahārājik", "Tứ Đại Thiên Vương")
ph("Asaññasatta", r"[Aa]saññasatt", "Vô Tưởng")
ph("Vehapphala", r"[Vv]ehapphal", "Quảng Quả")
ph("Aviha / Atappa / Sudassa / Sudassī", r"\b[Aa]vihā|\b[Aa]tappā|[Ss]udass", "Vô Phiền", "Vô Nhiệt", "Thiện Hiện", "Thiện Kiến")
ph("ābhā / subha gods", r"[Pp]arittābh|[Aa]ppamāṇābh|[Aa]bhassar|[Pp]arittasubh|[Aa]ppamāṇasubh|[Ss]ubhakiṇh",
   "Thiểu Quang", "Vô Lượng Quang", "Quang Âm", "Thiểu Tịnh", "Vô Lượng Tịnh", "Biến Tịnh")
ph("avīci", r"avīci", "Vô Gián")
ph("niraya", r"[Nn]iray|[Nn]erayik", "địa ngục")
ph("tiracchāna", r"tiracchān", "loài súc sinh", "súc sinh")
ph("peta / pettivisaya", r"\b[Pp]et[āa]\w*\b(?<!petaṃ)|pettivisay", "ngạ quỷ")
ph("asura", r"\b[Aa]sur(?!op|ulop)", "a-tu-la")
# precepts / abstention
ph("kāmesumicchācāra", r"kāmesumicchācār", "hành vi sai trái trong các dục lạc", "tà dâm")
ph("pāṇātipāta", r"pāṇātipāt", "việc sát hại sinh mạng", "sát sinh")
ph("adinnādāna", r"adinnādān", "việc lấy của không được cho")
ph("musāvāda", r"musāvād", "việc nói dối", "nói dối")
ph("veramaṇī", r"veramaṇ", "sự kiềm chế", "kiềm chế")
# faculties strings
ph("vīriya string (vīriyārambho)", r"vīriyārambho|viriyārambho", "sự khởi động tinh tấn", "nỗ lực đúng đắn")
ph("sammāvāyāmo (in a string)", r"sammāvāyāmo", "nỗ lực đúng đắn")
ph("sati string (sati anussati)", r"sati anussati", "sự tỉnh thức, sự nhớ lại", "tỉnh thức đúng đắn")
ph("samādhi string (cittassa ṭhiti)", r"cittassa ṭhiti", "sự an trụ của tâm", "định tâm đúng đắn")
ph("paññā string (paññā pajānanā)", r"paññā pajānanā", "trí tuệ, sự hiểu rõ", "quan điểm đúng đắn")
# jhāna formula
ph("vivicceva kāmehi", r"vivicceva kāmehi", "hoàn toàn tách khỏi các dục lạc", "tách khỏi các dục lạc")
ph("vivicca akusalehi", r"vivicca akusalehi", "tách khỏi các hiện tượng bất thiện")
ph("savitakkaṃ savicāraṃ vivekajaṃ", r"savitakkaṃ savicāraṃ vivekajaṃ", "có sự hướng tâm và sự duy trì tâm",
   "sinh từ sự tách biệt")
ph("vitakkavicārānaṃ vūpasamā", r"vitakkavicārānaṃ vūpasamā", "khi sự hướng tâm và sự duy trì tâm đã lắng xuống",
   "lắng dịu", "lắng xuống")
ph("ajjhattaṃ sampasādanaṃ", r"ajjhattaṃ sampasādanaṃ", "có sự trong sáng ở nơi bản thân, có sự hợp nhất của tâm")
ph("pītiyā ca virāgā", r"pītiyā ca virāgā", "nhờ sự hân hoan phai nhạt")
ph("upekkhako ca viharati", r"upekkhako ca viharati", "an trú bình thản, tỉnh thức và hiểu biết rõ ràng")
ph("sukhassa ca pahānā", r"sukhassa ca pahānā", "khi đã dứt bỏ sự dễ chịu", "nhờ dứt bỏ sự dễ chịu")
ph("upasampajja viharati", r"upasampajja viharati", "chứng nhập và an trú")
# lokuttara openings
ph("lokuttaraṃ jhānaṃ bhāveti", r"lokuttaraṃ jhānaṃ bhāveti", "tu tập tầng thiền vượt thế gian")
ph("niyyānikaṃ apacayagāmiṃ", r"niyyānikaṃ apacayagāmiṃ", "dẫn đến giải thoát và dẫn đến sự giảm trừ")
ph("diṭṭhigatānaṃ pahānāya", r"diṭṭhigatānaṃ pahānāya", "để dứt bỏ sự mắc kẹt trong các quan điểm")
ph("paṭhamāya bhūmiyā pattiyā", r"paṭhamāya bhūmiyā pattiyā", "để đạt đến giai đoạn thứ nhất")
ph("counted plural question (Tattha katame <number> …?)",
   r"[Tt]attha katam(?:e|ā|āni) (?:\S+ )?(?:tayo|tisso|tīṇi|dve|cattāro|catasso|cattāri|pañca|cha|satta|aṭṭha|nava|dasa)\b",
   "là những gì?", "là gì?")
ph("nāma / rūpa members (ch6)", r"Atthi nāmaṃ, atthi rūpaṃ", "Có phần tinh thần, có phần vật chất",
   "Có phần tinh thần, có vật chất")
ph("Tasseva lokuttarassa", r"Tasseva lokuttarassa", "Còn khi một người")
# question-section predicates / frames
ph("«đó được gọi là …» (vuccati)", r"(?<![Tt]ena )vuccat", "đó được gọi là", "được gọi là")
ph("na vattabba", r"(?i)na vattabb", "không nên nói")
ph("Tattha katam-", r"Tattha katam|tattha katam", "ở đây,")
ph("siyā", r"\bsiyā\b|\bSiyā\b", "đôi khi")
ph("kati kusalā (question)", r"kati kusalā", "bao nhiêu")
ph("sappaccayā saṅkhatā", r"(?i)sappaccay", "có điều kiện")
ph("araṇa / saraṇa", r"\b(?:a|sa)?raṇ[aā]", "có xung đột", "không có xung đột")
# counted names
ph("counted khandhā", r"\b(?:Pañcakkhandhā|pañcakkhandhā|Cattāro khandhā|Tayo khandhā|Dve khandhā|Pañca khandhā)\b", "khối")
ph("counted dhātuyo", r"\bdhātuyo\b", "yếu tố")
ph("counted āyatanā(ni)", r"\b(?:Dvādas|Das|Dv|Ek)āyatan|\bāyatanāni\b", "lĩnh vực")
ph("counted indriyā(ni)", r"indriyā\b|indriyāni\b", "năng lực")
# misc terms
ph("sajjha / rajata", r"sajjh|rajat", "bạc", "đồng tiền", "vàng bạc")
ph("dhamme ñāṇaṃ", r"[Dd]hamme ñāṇaṃ", "sự hiểu biết về Giáo Pháp", "sự hiểu biết về các hiện tượng")
ph("dhammaṃ jānāti", r"dhammaṃ jānāti", "biết Giáo Pháp", "biết các hiện tượng")
ph("vatthu (compounds)", r"vatth[uū]", "chỗ dựa", "căn cứ", "chủ đề")
ph("āghātavatthu", r"āghātavatth", "căn cứ của sự oán giận", "chỗ dựa của sự oán giận")
ph("virodhavatthu", r"virodhavatth", "căn cứ của sự chống đối", "chỗ dựa của sự chống đối")
ph("kusītavatthu", r"kusītavatth", "chỗ dựa của sự lười biếng", "căn cứ của sự lười biếng")
ph("kilesavatthu", r"kilesavatth", "chỗ dựa của phiền não", "căn cứ của phiền não")
ph("kāmadhātu", r"[Kk]āmadhāt", "yếu tố dục lạc", "cõi dục lạc")
ph("rūpadhātu / arūpadhātu", r"\b[Aa]?rūpadhāt", "yếu tố hình sắc", "cõi hình sắc", "cõi không hình sắc")
ph("Catukkaṃ / Pañcakaṃ (closing line)", r"^(?:Catukkaṃ|Pañcakaṃ)\.", "Phân loại theo nhóm", "Phương pháp chia")
ph("Ekakaṃ … Dasakaṃ (closing line)", r"^(?:Ekakaṃ|Dukaṃ|Tikaṃ|Catukkaṃ|Pañcakaṃ|Chakkaṃ|Sattakaṃ|Aṭṭhakaṃ|Navakaṃ|Dasakaṃ)\.",
   "Phân loại theo nhóm", "Phương pháp chia", "Bộ")
ph("abhiññeyya", r"abhiññeyy", "cần được hiểu biết trực tiếp")
ph("abhiññā", r"abhiññ", "hiểu biết trực tiếp")
ph("sambojjhaṅga (quoted topic / subject)", r"sambojjhaṅg", "“chi phần giác ngộ là", "chi phần giác ngộ là",
   "” là gì?", "” thì")
ph("vossagga", r"vossagg", "sự buông xả", "sự buông lơi")
ph("viharati", r"\bviharati\b", "an trú", "sống")
ph("sukhasahagata", r"sukhasahagat", "có sự dễ chịu đi kèm", "có hạnh phúc đi kèm")
ph("four dots (…pe…. at line end)", r"…pe…\s*\.", "….", "…")
ph("seyyathidaṃ", r"seyyathidaṃ", "cụ thể là")
ph("ṭhapetvā", r"ṭhapetvā|Ṭhapetvā", "ngoại trừ", "Ngoại trừ")
ph("Tena vuccati", r"Tena vuccati", "Vì thế nên mới nói rằng")
ph("thambhitattaṃ / chambhitattaṃ", r"[ct]hambhitatt", "trạng thái cứng đờ", "trạng thái khởi cứng đầu", "trạng thái căng cứng")


def scan_c():
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
                    k = v.lower().count(c.lower())
                    if k:
                        cnt[part][c] += k; hit = True
                if not hit:
                    cnt[part]["_none"] += 1
        p1 = collections.Counter()
        for part in P1_PARTS:
            for p, v in pairs1(part):
                if rx.search(p):
                    p1["_lines"] += 1
                    for c in cands:
                        p1[c] += v.lower().count(c.lower())
        tab.append((name, rx.pattern, cnt, p1))
    out = ["## (c) recurring terms and phrases: candidate Vietnamese forms per chapter", "",
           "Counts are occurrences of each candidate string on Vietnamese lines whose aligned Pāli matches; "
           "lines = matching lines, none = matching lines with no candidate (overlapping candidates are counted separately). "
           "The pi-1 row counts the same in the final pi-1 Vietnamese.", ""]
    for name, pat, cnt, p1 in tab:
        out.append(f"### {name}  (`{pat}`)")
        for part in PARTS:
            if part in cnt:
                c = cnt[part]
                items = ", ".join(f"{k}={v}" for k, v in c.items() if not k.startswith("_"))
                out.append(f"- {short(part)}: lines={c['_lines']} none={c['_none']} | {items}")
        if p1["_lines"]:
            out.append(f"- pi-1: lines={p1['_lines']} | " + ", ".join(f"{k}={v}" for k, v in p1.items() if not k.startswith("_") and v))
        out.append("")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    vi_common.ensure_backup()
    if "--bak" in sys.argv:
        vi_common.CUR["vdir"] = vi_common.BAK
    dest = args[0] if args else os.path.join(HERE, "divergences.md")
    s2, l2, c2, i2 = collect(segments, PARTS, short)
    s1, l1, c1, i1 = collect(segments1, P1_PARTS, short1)
    o1, n1 = report(s2, "(a1) whole segments: identical Pāli, differing Vietnamese")
    o2, n2 = report(l2, "(a2) whole lines: identical Pāli, differing Vietnamese", minlen=12)
    o3, n3 = report(c2, "(a3) clauses (sentence parts of lines whose clause counts match)", minlen=12)
    o4, n4 = report(i2, "(a4) comma/dash/ellipsis items of lines whose item counts match (cross-chapter only)",
                    minlen=8, cross_only=True)
    b1, m1 = report_b(s2, s1, "(b1) segments identical to a pi-1 segment, Vietnamese differs from pi-1")
    b2, m2 = report_b(l2, l1, "(b2) lines identical to a pi-1 line, Vietnamese differs from pi-1", minlen=12)
    b3, m3 = report_b(c2, c1, "(b3) clauses identical to a pi-1 clause, Vietnamese differs from pi-1", minlen=12)
    b4, m4 = report_b(i2, i1, "(b4) comma/dash/ellipsis items identical to a pi-1 item, Vietnamese differs from pi-1",
                      minlen=8)
    b3 += b4
    oc = scan_c()
    src = "backup-pre-harmonise (before the pass)" if "--bak" in sys.argv else "current outputs"
    head = ["# pi-2 Vietnamese zero-shot: divergences (find_divergences_vi.py)", "", f"Scanned: {src}.", "",
            f"(a1) segment groups: {n1}; (a2) line groups: {n2}; (a3) clause groups: {n3}; (a4) item groups: {n4}",
            f"(b1) pi-1 segment groups: {m1}; (b2) pi-1 line groups: {m2}; (b3) pi-1 clause groups: {m3}; "
            f"(b4) pi-1 item groups: {m4}", ""]
    open(dest, "w", encoding="utf-8", newline="\n").write(
        "\n".join(head + o1 + o2 + o3 + o4 + b1 + b2 + b3 + oc) + "\n")
    print("a: segments", n1, "lines", n2, "clauses", n3, "items", n4, "| b: segments", m1, "lines", m2,
          "clauses", m3, "items", m4, "->", dest)


if __name__ == "__main__":
    main()
