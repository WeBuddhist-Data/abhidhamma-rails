"""Check every vīriya / sati / samādhi / paññā synonym string of pi-2 against its own Pāli line (decision 2).

For each Pāli occurrence of a string (from its first word to the next « – », ".", ";", "?" or the line end) the
expected Vietnamese is built word by word from the pi-1 item renderings (pi-1 ^1-13 … ^1-16, ^1-287 … ^1-291) and
looked up on the aligned Vietnamese line (variant brackets stripped on both sides). Lines whose Vietnamese lacks
the expected string are printed with the Pāli string, the expected Vietnamese and the Vietnamese around it.

usage: python -I -X utf8 check_strings_vi.py [--bak]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, pairs, ID, VAR

W = {
    # vīriya (pi-1 ^1-13 / ^1-289)
    "cetasiko vīriyārambho": "sự khởi động tinh tấn trong tâm", "vīriyārambho": "sự khởi động tinh tấn",
    "nikkamo": "sự dấn bước", "parakkamo": "sự xông pha", "uyyāmo": "sự gắng sức", "vāyāmo": "sự nỗ lực",
    "ussāho": "sự hăng hái", "ussoḷhī": "sự bền chí", "thāmo": "sức bền", "dhiti": "sự kiên trì",
    "ṭhiti": "sự ổn định", "asithilaparakkamatā": "sự xông pha không lơi lỏng",
    "anikkhittachandatā": "sự không buông bỏ ý muốn", "anikkhittadhuratā": "sự không buông bỏ gánh",
    "dhurasampaggāho": "sự dốc sức gánh vác", "vīriyaṃ": "sự tinh tấn", "vīriyindriyaṃ": "năng lực tinh tấn",
    "vīriyabalaṃ": "sức mạnh tinh tấn", "sammāvāyāmo": "nỗ lực đúng đắn",
    "vīriyasambojjhaṅgo": "chi phần giác ngộ là sự tinh tấn",
    # sati (^1-14 / ^1-290)
    "sati": "sự tỉnh thức", "anussati": "sự nhớ lại", "paṭissati": "sự hồi tưởng", "saraṇatā": "sự ghi nhớ",
    "dhāraṇatā": "sự gìn giữ trong trí nhớ", "apilāpanatā": "sự không hời hợt", "asammussanatā": "sự không quên lãng",
    "satindriyaṃ": "năng lực tỉnh thức", "satibalaṃ": "sức mạnh tỉnh thức", "sammāsati": "tỉnh thức đúng đắn",
    "satisambojjhaṅgo": "chi phần giác ngộ là sự tỉnh thức",
    # samādhi (^1-15 / ^1-287)
    "cittassa ṭhiti": "sự ổn định của tâm", "saṇṭhiti": "sự vững vàng", "avaṭṭhiti": "sự vững chãi",
    "avisāhāro": "sự không phân tán", "avikkhepo": "sự không tán loạn",
    "avisāhaṭamānasatā": "trạng thái tâm trí không phân tán", "samatho": "sự tĩnh lặng",
    "samādhindriyaṃ": "năng lực định tâm", "samādhibalaṃ": "sức mạnh định tâm", "sammāsamādhi": "định tâm đúng đắn",
    "samādhisambojjhaṅgo": "chi phần giác ngộ là định tâm",
    # paññā (^1-16)
    "paññā": "trí tuệ", "pajānanā": "sự hiểu rõ", "vicayo": "sự tìm hiểu", "pavicayo": "sự tìm hiểu kỹ",
    "dhammavicayo": "sự tìm hiểu các hiện tượng", "sallakkhaṇā": "sự nhận xét", "upalakkhaṇā": "sự nhận diện",
    "paccupalakkhaṇā": "sự nhận diện chính xác", "paṇḍiccaṃ": "sự thông thái", "kosallaṃ": "sự khéo léo",
    "nepuññaṃ": "sự tinh tường", "vebhabyā": "sự phân biệt sáng suốt", "cintā": "sự suy tư",
    "upaparikkhā": "sự khảo sát", "bhūrī": "sự sâu rộng", "medhā": "sự thông minh", "pariṇāyikā": "sự dẫn dắt",
    "vipassanā": "sự thấu suốt", "sampajaññaṃ": "sự hiểu biết rõ ràng", "patodo": "cây roi thúc",
    "paññindriyaṃ": "năng lực trí tuệ", "paññābalaṃ": "sức mạnh trí tuệ", "paññāsatthaṃ": "thanh gươm trí tuệ",
    "paññāpāsādo": "lâu đài trí tuệ", "paññāāloko": "ánh sáng trí tuệ", "paññāobhāso": "hào quang trí tuệ",
    "paññāpajjoto": "ngọn đuốc trí tuệ", "paññāratanaṃ": "viên ngọc trí tuệ", "amoho": "sự không si mê",
    "sammādiṭṭhi": "quan điểm đúng đắn", "dhammavicayasambojjhaṅgo": "chi phần giác ngộ là sự tìm hiểu các hiện tượng",
    # path suffix
    "maggaṅgaṃ": "chi phần của con đường", "maggapariyāpannaṃ": "nằm trong con đường",
}
START = re.compile(r"(?:cetasiko )?vīriyārambho|\bsati anussati|cittassa ṭhiti saṇṭhiti|\bpaññā pajānanā")
STOP = re.compile(r"\s+[–—]\s|[.;?]|$")


def tokens(s):
    s = s.replace("…pe…", " … ")
    out, ws, i = [], s.split(), 0
    while i < len(ws):
        two = " ".join(ws[i:i + 2]).rstrip(",")
        if two in W:
            out.append(two); i += 2; continue
        out.append(ws[i].rstrip(",")); i += 1
    return out


def main():
    if "--bak" in sys.argv:
        vi_common.CUR["vdir"] = vi_common.BAK
    nocc = nbad = 0
    for part in PARTS:
        for k, (p, v) in enumerate(pairs(part)):
            pc = VAR.sub("", p).replace("viriy", "vīriy")
            vc = re.sub(r"\s+", " ", VAR.sub("", v))
            for m in START.finditer(pc):
                rest = pc[m.start():]
                s = rest[:STOP.search(rest).start()]
                toks = tokens(s)
                unknown = [t for t in toks if t not in W and t != "…"]
                exp = ""
                for t in toks:
                    if t == "…":
                        exp += "…"
                    else:
                        exp += ("" if not exp else (" " if exp.endswith("…") else ", ")) + W.get(t, f"<{t}>")
                nocc += 1
                ok = any(not vc[i + len(exp):].startswith(",") for i in [mm.start() for mm in re.finditer(re.escape(exp), vc)])
                if unknown or not ok:
                    nbad += 1
                    first = W.get(toks[0], "")
                    j = vc.find(first)
                    print(f"== {part} line {k + 1} {ID.search(p).group(0) if ID.search(p) else ''}")
                    print("  P:", s)
                    if unknown:
                        print("  UNKNOWN:", unknown)
                    print("  E:", exp)
                    print("  V:", vc[j:j + len(exp) + 80] if j >= 0 else vc[:300])
    print("strings checked:", nocc, "| not found as expected:", nbad)
    # reverse check: Vietnamese string openings without the Pāli opening on the aligned line (count per line)
    pairs_ = [("vīriyārambho", "sự khởi động tinh tấn"), ("sati anussati", "sự tỉnh thức, sự nhớ lại"),
              ("cittassa ṭhiti saṇṭhiti", "sự ổn định của tâm, sự vững vàng"), ("paññā pajānanā", "trí tuệ, sự hiểu rõ"),
              ("sammāvāyāmo vīriyasambojjhaṅgo", "nỗ lực đúng đắn, chi phần giác ngộ là sự tinh tấn"),
              ("vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo", "sự tinh tấn, năng lực tinh tấn, sức mạnh tinh tấn, nỗ lực đúng đắn"),
              ("vīriyaṃ vīriyindriyaṃ vīriyabalaṃ", "sự tinh tấn, năng lực tinh tấn, sức mạnh tinh tấn")]
    nrev = 0
    for part in PARTS:
        for k, (p, v) in enumerate(pairs(part)):
            pc = VAR.sub("", p).replace("viriy", "vīriy")
            vc = re.sub(r"\s+", " ", VAR.sub("", v))
            for a, b in pairs_:
                if pc.count(a) != vc.count(b):
                    nrev += 1
                    print(f"REV {part} line {k + 1}: «{a}» x{pc.count(a)} vs «{b}» x{vc.count(b)}")
    print("reverse mismatches:", nrev)


if __name__ == "__main__":
    main()
