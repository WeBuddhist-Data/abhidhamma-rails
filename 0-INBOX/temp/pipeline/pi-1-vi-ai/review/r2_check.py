"""r2 review helper: mechanical checks Pali vs Vietnamese for chapters 2-03..2-05.
Read-only. Prints findings to stdout. Usage:
  python -I -X utf8 r2_check.py            -> mechanical checks
  python -I -X utf8 r2_check.py ts A B     -> print reference segments for IDs A..B (stdout only)
"""
import re, sys, unicodedata
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PI = ROOT + r"\AI_translation\pali\pi-1_split_chapters"
VI = ROOT + r"\AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters"
TS = ROOT + r"\1-SOURCES\Translations\Vietnamese\vi-1-tinh_su.md"
CHS = ["2-03-cittuppadakandam.md", "2-04-cittuppadakandam.md", "2-05-cittuppadakandam.md"]
IDRE = re.compile(r"\^([0-9a-z-]+)\s*$")


def segs(path):
    txt = open(path, encoding="utf-8").read()
    out = []
    for blk in re.split(r"\n\s*\n", txt.strip("\n")):
        lines = [l for l in blk.split("\n") if l.strip()]
        m = IDRE.search(lines[-1])
        out.append((m.group(1) if m else None, lines))
    return txt, out


def num(sid):
    m = re.match(r"1-(\d+)$", sid or "")
    return int(m.group(1)) if m else None


# ---- permutation token extraction ----
PI_TOK = [
    (r"dukkhapaṭipadaṃ dandhābhiññ", "DD"), (r"dukkhapaṭipadaṃ khippābhiññ", "DK"),
    (r"sukhapaṭipadaṃ dandhābhiññ", "SD"), (r"sukhapaṭipadaṃ khippābhiññ", "SK"),
    (r"suññat", "SUN"), (r"animitt", "ANI"), (r"appaṇihit", "APP"),
    (r"chandādhipateyy", "CH"), (r"vīriyādhipateyy", "VI"), (r"cittādhipateyy", "CI"), (r"vīmaṃsādhipateyy", "VM"),
    (r"paṭhamaṃ jhān", "J1"), (r"dutiyaṃ jhān", "J2"), (r"tatiyaṃ jhān", "J3"), (r"catutthaṃ jhān", "J4"), (r"pañcamaṃ jhān", "J5"),
    (r"paṭhamāya bhūmiyā", "B1"), (r"dutiyāya bhūmiyā", "B2"), (r"tatiyāya bhūmiyā", "B3"), (r"catutthāya bhūmiyā", "B4"),
    (r"nti kusalaṃ", "KUS"), (r"nti vipāko", "VIP"), (r"ime dhammā kusalā", "=K"), (r"ime dhammā abyākatā", "=A"), (r"ime dhammā akusalā", "=U"),
    (r"aññindriy", "ANN"), (r"anaññātaññassāmītindriy", "ANA"), (r"aññātāvindriy", "AAV"),
    (r"kāmāvacar", "KAMA"), (r"rūpāvacar", "RUPA"), (r"arūpāvacar", "ARUPA"), (r"lokuttar", "LOK"),
    (r"pathavīkasiṇ", "PATH"),
]
VI_TOK = [
    (r"thực hành khó khăn và sự hiểu biết trực tiếp chậm chạp", "DD"), (r"thực hành khó khăn và sự hiểu biết trực tiếp nhanh chóng", "DK"),
    (r"thực hành dễ dàng và sự hiểu biết trực tiếp chậm chạp", "SD"), (r"thực hành dễ dàng và sự hiểu biết trực tiếp nhanh chóng", "SK"),
    (r"trống rỗng", "SUN"), (r"không có dấu hiệu", "ANI"), (r"không mong cầu", "APP"),
    (r"lấy ý muốn làm", "CH"), (r"lấy tinh tấn làm", "VI"), (r"lấy tâm làm", "CI"), (r"lấy sự thẩm xét làm", "VM"),
    (r"tầng thiền thứ nhất", "J1"), (r"tầng thiền thứ hai", "J2"), (r"tầng thiền thứ ba", "J3"), (r"tầng thiền thứ tư", "J4"), (r"tầng thiền thứ năm", "J5"),
    (r"giai đoạn thứ nhất", "B1"), (r"giai đoạn thứ hai", "B2"), (r"giai đoạn thứ ba", "B3"), (r"giai đoạn thứ tư", "B4"),
    (r"\(tâm thiện\)", "KUS"), (r"\(quả của nghiệp\)", "VIP"), (r"những hiện tượng này là thiện", "=K"), (r"những hiện tượng này không xác định về mặt đạo đức", "=A"), (r"những hiện tượng này là bất thiện", "=U"),
    (r"năng lực hiểu biết trọn vẹn", "ANN"), (r"năng lực biết được điều chưa từng biết", "ANA"), (r"năng lực của người đã hiểu biết trọn vẹn", "AAV"),
    (r"cõi dục lạc", "KAMA"), (r"cõi hình sắc", "RUPA"), (r"cõi không hình sắc", "ARUPA"), (r"vượt thế gian", "LOK"),
    (r"bao trùm là đất", "PATH"),
]


def toks(s, table):
    hits = []
    for pat, t in table:
        for m in re.finditer(pat, s):
            hits.append((m.start(), t))
    hits.sort()
    # drop RUPA inside ARUPA (vi: 'cõi hình sắc' inside 'cõi không hình sắc' does not overlap; pali: rūpāvacar inside arūpāvacar does)
    res = []
    for i, (p, t) in enumerate(hits):
        if t == "RUPA" and any(t2 == "ARUPA" and p2 < p <= p2 + 2 for p2, t2 in hits):
            continue
        res.append(t)
    return res


NUMW_PI = {"eko": 1, "ekā": 1, "ekaṃ": 1, "dve": 2, "dvāyatanāni": 2, "duvaṅgiko": 2, "tayo": 3, "tīṇi": 3, "tīṇindriyāni": 3, "tivaṅgiko": 3,
           "cattāro": 4, "cattāri": 4, "caturaṅgikaṃ": 4, "caturaṅgiko": 4, "pañcindriyāni": 5, "pañcaṅgikaṃ": 5,
           "navindriyāni": 9, "aṭṭhaṅgiko": 8, "satta": 7, "aṭṭhindriyāni": 8, "chaḷindriyāni": 6}
NUMW_VI = {"một": 1, "hai": 2, "ba": 3, "bốn": 4, "năm": 5, "sáu": 6, "bảy": 7, "tám": 8, "chín": 9, "mười": 10}


def summary_nums(line, lang):
    if lang == "pi":
        return [NUMW_PI[w] for w in re.findall(r"[^\s,;…]+", line) if w in NUMW_PI]
    return [NUMW_VI[w] for w in re.findall(r"có (một|hai|ba|bốn|năm|sáu|bảy|tám|chín|mười)\b", line)] + \
        [NUMW_VI[w] for w in re.findall(r"gồm (một|hai|ba|bốn|năm|sáu|bảy|tám|chín) chi phần", line)]


def main():
    total = 0
    for ch in CHS:
        ptxt, ps = segs(PI + "\\" + ch)
        vtxt, vs = segs(VI + "\\" + ch)
        print("=" * 20, ch, "pali segs", len(ps), "vi segs", len(vs))
        if "\r" in vtxt: print("  CR present")
        if "\n\n\n" in vtxt: print("  double blank line")
        if unicodedata.normalize("NFC", vtxt) != vtxt: print("  not NFC")
        if "—" in vtxt: print("  em dash present")
        if "….“" in vtxt or "…." in vtxt: print("  '….' present", vtxt.count("…."))
        for (pid, pl), (vid, vl) in zip(ps, vs):
            total += 1
            if pid != vid: print("  ID mismatch", pid, vid); continue
            if len(pl) != len(vl): print("  line count", pid, len(pl), len(vl))
            for i, (a, b) in enumerate(zip(pl, vl)):
                da = a.count("–") + a.count("—"); db = b.count("–") + b.count("—")
                if da != db: print("  dash", pid, "line", i, da, db)
                pe = a.count("…pe…"); el = b.count("…")
                if pe != el: print("  pe/ellipsis", pid, "line", i, pe, el)
                qa = a.count("?"); qb = b.count("?")
                if qa != qb: print("  ?count", pid, "line", i, qa, qb)
                # enumeration: count 'hoti' items before ';' in a 'tasmiṃ samaye phasso hoti, vedanā' list
                if "phasso hoti, vedanā hoti" in a:
                    na = a.split(";")[0].split("tasmiṃ samaye", 1)[1].count(" hoti")
                    nb = b.split(";")[0].split("thì vào lúc ấy", 1)[1].count("có ")
                    if na != nb: print("  enum count", pid, na, nb)
                if a.startswith("Tasmiṃ kho pana samaye"):
                    sa, sb = summary_nums(a, "pi"), summary_nums(b, "vi")
                    if sa != sb: print("  summary nums", pid, sa, sb)
                if a.startswith("Phasso cetanā") or "hoti? Phasso" in a:
                    lst = a.split("? ", 1)[1].split(";")[0] if "? " in a else a.split(";")[0]
                    na = len(lst.split())
                    lb = b.split("? ", 1)[1].split(";")[0] if "? " in b else b.split(";")[0]
                    nb = len(lb.split(", "))
                    if na != nb: print("  sankhara list", pid, na, nb)
                ta, tb = toks(a, PI_TOK), toks(b, VI_TOK)
                if ta != tb: print("  tokens", pid, "line", i, "\n    PI", ta, "\n    VI", tb)
        print("  segments", len(ps))
    print("TOTAL segments", total)


def ts(a, b):
    lines = open(TS, encoding="utf-8").read().split("\n")
    cur = None; buf = {}
    for l in lines:
        m = re.match(r"!\[\[1-SOURCES/Text/pi-1\.md#\^(1-\d+)\]\]", l.strip())
        if m:
            cur = num(m.group(1)); buf.setdefault(cur, []); continue
        if cur is not None and l.strip():
            buf[cur].append(l.strip())
    for k in range(a, b + 1):
        print("#", k, " | ".join(buf.get(k, ["<none>"])))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "ts":
        ts(int(sys.argv[2]), int(sys.argv[3]))
    else:
        main()
