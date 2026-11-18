"""r1 helper: scripted checks for chapters 2-01 / 2-02 (and matika).
Compares ordered sequences of key items Pali vs Vietnamese per segment,
checks factor lists via an item map, and checks formula consistency.
Usage: python -I -X utf8 r1_check.py
"""
import re, os, unicodedata
from collections import defaultdict

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
VI = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
IDRE = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")


def segments(path):
    segs, cur = [], []
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.strip():
            cur.append(line)
            m = IDRE.search(line)
            if m:
                segs.append((m.group(1), "\n".join(cur)))
                cur = []
    return segs


def seq(text, rules):
    """rules: list of (regex, label); returns labels in order of appearance."""
    hits = []
    for rx, lab in rules:
        for m in re.finditer(rx, text):
            hits.append((m.start(), lab))
    return [l for _, l in sorted(hits)]


P_JH = [(r"paṭhamaṃ jhānaṃ", 1), (r"dutiyaṃ jhānaṃ", 2), (r"tatiyaṃ jhānaṃ", 3), (r"catutthaṃ jhānaṃ", 4), (r"pañcamaṃ jhānaṃ", 5)]
V_JH = [(r"tầng thiền thứ nhất", 1), (r"tầng thiền thứ hai", 2), (r"tầng thiền thứ ba", 3), (r"tầng thiền thứ tư", 4), (r"tầng thiền thứ năm", 5)]
P_PT = [(r"dukkhapaṭipadaṃ", "D"), (r"sukhapaṭipadaṃ", "S"), (r"dandhābhiññaṃ", "d"), (r"khippābhiññaṃ", "k")]
V_PT = [(r"thực hành khó khăn", "D"), (r"thực hành dễ dàng", "S"), (r"trực tiếp chậm chạp", "d"), (r"trực tiếp nhanh chóng", "k")]
P_AR = [(r"parittaṃ (?=paritt|appam)", "p"), (r"appamāṇaṃ (?=paritt|appam)", "a"), (r"parittārammaṇaṃ", "P"), (r"appamāṇārammaṇaṃ", "A")]
V_AR = [(r"hạn hẹp và có đối tượng", "p"), (r"không thể đo lường và có đối tượng", "a"), (r"đối tượng hạn hẹp", "P"), (r"đối tượng không thể đo lường", "A")]
P_KS = [(r"pathavīkasiṇaṃ", "earth"), (r"āpokasiṇaṃ", "water"), (r"tejokasiṇaṃ", "fire"), (r"vāyokasiṇaṃ", "wind"), (r"nīlakasiṇaṃ", "blue"), (r"pītakasiṇaṃ", "yellow"), (r"lohitakasiṇaṃ", "red"), (r"odātakasiṇaṃ", "white")]
V_KS = [(r"bao trùm là đất", "earth"), (r"bao trùm là nước", "water"), (r"bao trùm là lửa", "fire"), (r"bao trùm là gió", "wind"), (r"bao trùm màu xanh", "blue"), (r"bao trùm màu vàng", "yellow"), (r"bao trùm màu đỏ", "red"), (r"bao trùm màu trắng", "white")]
P_AD = [(r"\bhīnaṃ", "h"), (r"majjhimaṃ", "m"), (r"paṇītaṃ", "p"), (r"chandādhipateyyaṃ", "C"), (r"vīriyādhipateyyaṃ", "V"), (r"cittādhipateyyaṃ", "T"), (r"vīmaṃsādhipateyyaṃ", "M")]
V_AD = [(r"thấp kém", "h"), (r"trung bình", "m"), (r"ưu việt", "p"), (r"lấy ý muốn làm", "C"), (r"lấy tinh tấn làm", "V"), (r"lấy tâm làm", "T"), (r"lấy sự thẩm xét làm", "M")]
P_CT = [(r"somanassasahagataṃ", "S"), (r"upekkhāsahagataṃ", "U"), (r"ñāṇasampayuttaṃ", "+"), (r"ñāṇavippayuttaṃ", "-"), (r"sasaṅkhārena", "s"),
        (r"mettāsahagataṃ", "me"), (r"karuṇāsahagataṃ", "ka"), (r"muditāsahagataṃ", "mu")]
V_CT = [(r"có niềm vui đi kèm", "S"), (r"có sự bình thản đi kèm", "U"), (r"(?<!không )gắn liền với hiểu biết", "+"), (r"không gắn liền với hiểu biết", "-"), (r"có sự thúc đẩy", "s"),
        (r"có lòng từ ái đi kèm", "me"), (r"có lòng trắc ẩn đi kèm", "ka"), (r"có niềm vui đồng cảm đi kèm", "mu")]
P_NUM = [(r"\b(cattāro) khandhā", "4kh"), (r"(dvāyatanāni)", "2ay"), (r"(dve dhātuyo)", "2dh"), (r"(tayo āhārā)", "3ah"),
         (r"aṭṭhindriyāni", "8in"), (r"sattindriyāni", "7in"), (r"pañcaṅgikaṃ jhānaṃ", "5jh"), (r"caturaṅgikaṃ jhānaṃ", "4jh"), (r"tivaṅgikaṃ jhānaṃ", "3jh"), (r"duvaṅgikaṃ jhānaṃ", "2jh"),
         (r"pañcaṅgiko maggo", "5mg"), (r"caturaṅgiko maggo", "4mg"), (r"satta balāni", "7bl"), (r"cha balāni", "6bl"), (r"tayo hetū", "3ht"), (r"dve hetū", "2ht")]
V_NUM = [(r"bốn khối", "4kh"), (r"hai lĩnh vực nhận biết", "2ay"), (r"hai yếu tố", "2dh"), (r"ba loại dưỡng chất", "3ah"),
         (r"tám năng lực", "8in"), (r"bảy năng lực", "7in"), (r"tầng thiền gồm năm chi phần", "5jh"), (r"tầng thiền gồm bốn chi phần", "4jh"), (r"tầng thiền gồm ba chi phần", "3jh"), (r"tầng thiền gồm hai chi phần", "2jh"),
         (r"con đường gồm năm chi phần", "5mg"), (r"con đường gồm bốn chi phần", "4mg"), (r"bảy sức mạnh", "7bl"), (r"sáu sức mạnh", "6bl"), (r"ba gốc rễ", "3ht"), (r"hai gốc rễ", "2ht")]

RULESETS = [("jhana", P_JH, V_JH), ("patipada", P_PT, V_PT), ("arammana", P_AR, V_AR), ("kasina", P_KS, V_KS),
            ("adhipati", P_AD, V_AD), ("citta-type", P_CT, V_CT), ("numbers", P_NUM, V_NUM)]

# factor map (Pali item -> Vietnamese item) for "X hoti" lists and sankhara lists
FMAP = {
    "phasso": "sự tiếp xúc", "vedanā": "cảm giác", "saññā": "tri giác", "cetanā": "chủ ý", "cittaṃ": "tâm",
    "vitakko": "sự hướng tâm", "vicāro": "sự duy trì tâm", "pīti": "sự hân hoan", "sukhaṃ": "hạnh phúc", "upekkhā": "sự bình thản",
    "cittassekaggatā": "sự nhất tâm", "saddhindriyaṃ": "năng lực niềm tin", "vīriyindriyaṃ": "năng lực tinh tấn", "satindriyaṃ": "năng lực tỉnh thức",
    "samādhindriyaṃ": "năng lực định tâm", "paññindriyaṃ": "năng lực trí tuệ", "manindriyaṃ": "năng lực ý", "somanassindriyaṃ": "năng lực niềm vui",
    "upekkhindriyaṃ": "năng lực bình thản", "jīvitindriyaṃ": "năng lực sống", "sammādiṭṭhi": "quan điểm đúng đắn", "sammāsaṅkappo": "tư duy đúng đắn",
    "sammāvāyāmo": "nỗ lực đúng đắn", "sammāsati": "tỉnh thức đúng đắn", "sammāsamādhi": "định tâm đúng đắn", "saddhābalaṃ": "sức mạnh niềm tin",
    "vīriyabalaṃ": "sức mạnh tinh tấn", "satibalaṃ": "sức mạnh tỉnh thức", "samādhibalaṃ": "sức mạnh định tâm", "paññābalaṃ": "sức mạnh trí tuệ",
    "hiribalaṃ": "sức mạnh biết hổ thẹn", "ottappabalaṃ": "sức mạnh biết ghê sợ tội lỗi", "alobho": "sự không tham lam", "adoso": "sự không sân hận",
    "amoho": "sự không si mê", "anabhijjhā": "sự không thèm muốn", "abyāpādo": "sự không ác ý", "hirī": "sự biết hổ thẹn", "ottappaṃ": "sự biết ghê sợ tội lỗi",
    "kāyapassaddhi": "sự an tịnh của thân tinh thần", "cittapassaddhi": "sự an tịnh của tâm", "kāyalahutā": "sự nhẹ nhàng của thân tinh thần",
    "cittalahutā": "sự nhẹ nhàng của tâm", "kāyamudutā": "sự mềm mại của thân tinh thần", "cittamudutā": "sự mềm mại của tâm",
    "kāyakammaññatā": "sự dễ vận dụng của thân tinh thần", "cittakammaññatā": "sự dễ vận dụng của tâm", "kāyapāguññatā": "sự thuần thục của thân tinh thần",
    "cittapāguññatā": "sự thuần thục của tâm", "kāyujukatā": "sự ngay thẳng của thân tinh thần", "cittujukatā": "sự ngay thẳng của tâm",
    "sati": "sự tỉnh thức", "sampajaññaṃ": "sự hiểu biết rõ ràng", "samatho": "sự tĩnh lặng", "vipassanā": "sự thấu suốt", "paggāho": "sự dốc sức",
    "avikkhepo": "sự không tán loạn",
}


def norm(s):
    s = re.sub(r"\[[^\]]*\]", "", s)
    return unicodedata.normalize("NFC", s)


def hoti_list(p):
    m = re.search(r"tasmiṃ samaye (phasso hoti, .*?)(?:;|…pe…\s*$)", p, re.S)
    if not m:
        return None
    items = [x.strip() for x in re.split(r",\s*|\s+(?=\S+ hoti)", m.group(1)) if x.strip()]
    out = []
    for it in items:
        it = it.replace(" hoti", "").strip()
        if it.startswith("…pe…") or not it:
            out.append("…")
            continue
        for sub in re.split(r"…pe…", it):
            sub = sub.strip()
            if sub:
                out.append(sub)
            else:
                out.append("…")
    # collapse
    res = []
    for x in out:
        if x == "…" and res and res[-1] == "…":
            continue
        res.append(x)
    return res


def vi_hoti_list(v):
    m = re.search(r"thì vào lúc ấy (có sự tiếp xúc, .*?)(?:;|…\s*$)", v, re.S)
    if not m:
        return None
    body = m.group(1)
    toks = re.split(r",\s*|…\s*", body)
    out = []
    parts = re.split(r"(…)", body)
    for part in parts:
        if part == "…":
            out.append("…")
            continue
        for t in part.split(","):
            t = t.strip()
            if t.startswith("có "):
                t = t[3:]
            if t:
                out.append(t)
    res = []
    for x in out:
        if x == "…" and res and res[-1] == "…":
            continue
        res.append(x)
    return res


def sankhara_list(p):
    m = re.search(r"saṅkhārakkhandho hoti\? (.*?)(?:;|\.\n|\.\s*$)", p, re.S)
    if not m:
        return None
    body = m.group(1)
    out = []
    for part in re.split(r"(…pe…)", body):
        if part == "…pe…":
            out.append("…")
            continue
        out += [x for x in part.split() if x]
    return out


def vi_sankhara_list(v):
    m = re.search(r"khối tạo tác là gì\? (.*?)(?:;|\.\n|\.\s*$)", v, re.S)
    if not m:
        return None
    body = m.group(1)
    out = []
    for part in re.split(r"(…)", body):
        if part == "…":
            out.append("…")
            continue
        out += [x.strip() for x in part.split(",") if x.strip()]
    return out


def main():
    report = []
    for ch in ["1-matika.md", "2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md"]:
        p = segments(os.path.join(PALI, ch))
        v = dict(segments(os.path.join(VI, ch)))
        for sid, ptxt in p:
            vtxt = v.get(sid, "")
            pn, vn = norm(ptxt), norm(vtxt)
            for name, pr, vr in RULESETS:
                a, b = seq(pn, pr), seq(vn, vr)
                if a != b:
                    report.append(f"{ch} ^{sid} {name}: PI {a} VI {b}")
            # line count
            if len(ptxt.split("\n")) != len(vtxt.split("\n")):
                report.append(f"{ch} ^{sid} line count {len(ptxt.split(chr(10)))} vs {len(vtxt.split(chr(10)))}")
            # factor lists
            hl, vl = hoti_list(pn), vi_hoti_list(vn)
            if hl is not None:
                exp = [FMAP.get(x, "?" + x) if x != "…" else "…" for x in hl]
                if exp != vl:
                    report.append(f"{ch} ^{sid} HOTI LIST mismatch:\n   exp {exp}\n   got {vl}")
            sl, vsl = sankhara_list(pn), vi_sankhara_list(vn)
            if sl is not None:
                exp = [FMAP.get(x, "?" + x) if x != "…" else "…" for x in sl]
                exp = [e[0].upper() + e[1:] if i == 0 else e for i, e in enumerate(exp)]
                if exp != vsl:
                    report.append(f"{ch} ^{sid} SANKHARA LIST mismatch:\n   exp {exp}\n   got {vsl}")
            # question/statement punctuation per line
            for pl, vl2 in zip(ptxt.split("\n"), vtxt.split("\n")):
                pl2, vl3 = IDRE.sub("", pl).rstrip(), IDRE.sub("", vl2).rstrip()
                if pl2[-1:] != vl3[-1:] and not (pl2.endswith("…pe….") and vl3.endswith("…")):
                    report.append(f"{ch} ^{sid} end punct PI '{pl2[-6:]}' VI '{vl3[-6:]}'")
                if pl2.count("?") != vl3.count("?"):
                    report.append(f"{ch} ^{sid} '?' count PI {pl2.count('?')} VI {vl3.count('?')}")
                if pl2.count("…pe…") != vl3.count("…"):
                    report.append(f"{ch} ^{sid} pe count PI {pl2.count('…pe…')} VI … {vl3.count('…')}")
            if "…." in vtxt:
                report.append(f"{ch} ^{sid} has '….'")
            if re.search(r"\bchánh niệm\b", vtxt):
                report.append(f"{ch} ^{sid} has 'chánh niệm'")
            if unicodedata.normalize("NFC", vtxt) != vtxt:
                report.append(f"{ch} ^{sid} not NFC")
    # formula consistency: definitional bodies
    bodies = defaultdict(set)
    for ch in ["2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md"]:
        p = segments(os.path.join(PALI, ch))
        v = dict(segments(os.path.join(VI, ch)))
        for sid, ptxt in p:
            pm = re.search(r"\? (Y[oāa]ṃ? (?:tasmiṃ samaye|tesaṃ).*?) – ", norm(ptxt))
            vm = re.search(r"\? (Điều mà .*?) – ", norm(v.get(sid, "")))
            if pm and vm:
                bodies[pm.group(1)].add((vm.group(1), sid))
    for pb, vs in bodies.items():
        texts = {t for t, _ in vs}
        if len(texts) > 1:
            report.append("INCONSISTENT body for PI '" + pb[:60] + "': " + " || ".join(f"{s}: {t[:80]}" for t, s in sorted(vs, key=lambda x: x[1])))
    print("\n".join(report) if report else "no findings")


if __name__ == "__main__":
    main()
