"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 4: 4-jahatikatha.

usage: python -I -X utf8 -B map_4_vi.py                  (writes 4-jahatikatha.mapped.md and verifies it)
       python -I -X utf8 -B map_4_vi.py show lo hi [pi]   (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> value5(kw, kws, T4, text) of map_sample_vi (T4 -> context5 ->
FORMULAS -> KV -> two-word composition -> the pi-4 chain).
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import NDE, GAP, build_part, en_ru, lc, present, read_keywords, read_vietnamese, verify  # noqa
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "4-jahatikatha"

_KRB = "sự tham đắm dục lạc và ác ý"               # kāmarāgabyāpādaṃ
_AP = "tự mình chứng nghiệm thành quả không trở lại"   # anāgāmiphalasacchikiriyāya
_PJ = "người phàm phu"

T4 = {
    # ---- headings: Jahatikathā «Bàn về sự dứt bỏ», (Na)suttāharaṇakathā «Phần (không) dẫn kinh»
    "āharaṇa": "dẫn",                              # sample āharaṇena «việc dẫn» (here no «việc»)
    # ---- «người phàm phu dứt bỏ / đè nén sự tham đắm dục lạc và ác ý»
    "jahati": "dứt bỏ", "vikkhambheti": "đè nén",
    "puthu": "phàm phu",                           # pi-4 (puthujjano «người phàm phu»)
    "kāmarāgabyāpādaṃ": _KRB, "kāmarāgabyāpādānaṃ": _KRB,
    "kāmarāgaṃ": "sự tham đắm dục lạc",
    "rāgaṃ": "sự tham đắm",                        # of kāmarāgaṃ (the text writes «sự», pi-4)
    "jahati kāmarāgabyāpādaṃ": "dứt bỏ " + _KRB,
    "vikkhambheti kāmarāgabyāpādaṃ": "đè nén " + _KRB,
    "jahati puthujjano": _PJ + " dứt bỏ", "vikkhambheti puthujjano": _PJ + " đè nén",
    "jahati puthujjano kāmarāgabyāpādaṃ": _PJ + " dứt bỏ " + _KRB,
    "vikkhambheti puthujjano kāmarāgabyāpādaṃ": _PJ + " đè nén " + _KRB,
    # «người đang thực hành để tự mình chứng nghiệm thành quả không trở lại, dứt bỏ …» (comma: « … »)
    "jahati anāgāmiphalasacchikiriyāya": _AP + GAP + "dứt bỏ",
    "jahati anāgāmiphalasacchikiriyāya kāmarāgabyāpādaṃ": _AP + GAP + "dứt bỏ " + _KRB,
    "vikkhambheti anāgāmiphalasacchikiriyāya": _AP + GAP + "đè nén",
    "vikkhambheti anāgāmiphalasacchikiriyāya kāmarāgabyāpādaṃ": _AP + GAP + "đè nén " + _KRB,
    # «dứt bỏ một cách hoàn toàn, dứt bỏ không còn sót lại, dứt bỏ không còn tái khởi, dứt bỏ cùng với gốc rễ,
    # dứt bỏ cùng với khao khát, … cùng với khuynh hướng tiềm ẩn, … bằng hiểu biết cao quý, … bằng con đường cao
    # quý, … trong khi thấu triệt điều không thể bị lay chuyển, … trong khi tự mình chứng nghiệm thành quả …»
    "accantaṃ": "một cách hoàn toàn",
    "accantaṃ jahati": "dứt bỏ một cách hoàn toàn", "accantaṃ vikkhambheti": "đè nén một cách hoàn toàn",
    "avasesaṃ": "còn sót lại",                     # of anavasesaṃ «không còn sót lại» (pi-4 avasesa)
    "appaṭisandhiyaṃ": "không còn tái khởi",
    "paṭisandhiyaṃ": "còn tái khởi",               # of appaṭisandhiyaṃ (positive part, as avasesa)
    "samūlaṃ": "cùng với gốc rễ", "mūlaṃ": "gốc rễ",
    "taṇhaṃ": "khao khát",
    "ñāṇena": "hiểu biết",                         # «bằng hiểu biết cao quý» (instrumental «bằng» = frame)
    "akuppaṃ": "điều không thể bị lay chuyển",     # the text's «điều» kept (pi-3 «điều được gộp vào»)
    "paṭivijjhanto": "trong khi thấu triệt",       # participles keep «khi» (sample vediyamāno)
    "sacchikaronto": "trong khi tự mình chứng nghiệm",
    "anāgāmiphalaṃ sacchikaronto": "trong khi tự mình chứng nghiệm thành quả không trở lại",
    "anāgāmiphalaṃ": "thành quả không trở lại", "phalaṃ": "thành quả",
    # ---- «Bằng con đường nào? Bằng con đường thuộc cõi hình sắc. … dẫn đến giải thoát, dẫn đến sự diệt tận, dẫn
    # đến sự giác ngộ, dẫn đến sự giảm trừ, không phải là đối tượng của ô nhiễm …»
    "avacarena": "thuộc cõi", "rūpāvacarena": "thuộc cõi hình sắc",
    "rūpāvacarena maggena": "con đường thuộc cõi hình sắc",
    "anāgāmimaggena": "con đường không trở lại", "sakadāgāmimaggena": "con đường trở lại một lần",
    "sotāpattimaggena": "con đường vào dòng",
    "khaya": "sự diệt tận", "bodha": "sự giác ngộ",   # khayagāmī / bodhagāmī (the text writes «sự», as apacaya)
    "saṃkilesiyo": "đối tượng của phiền não",
    # ---- 5-280 «người phàm phu đã lìa tham đắm đối với các dục lạc, cùng lúc với sự thấu hiểu Giáo Pháp, đứng vững
    # trong thành quả không trở lại … trạng thái A-la-hán … tu tập ba con đường … ba thành quả của đời sống sa-môn
    # … sự tụ hợp của ba sự tiếp xúc, ba cảm giác, …»
    "vīta": "đã lìa", "abhisamayā": "sự thấu hiểu", "abhisamenti": "thấu hiểu",
    "saṇṭhāti": "đứng vững", "anāgāmiphale": "thành quả không trở lại",
    "arahatte": "trạng thái A-la-hán",             # arahatta «trạng thái A-la-hán» (style rule)
    "sacchikaroti": "tự mình chứng nghiệm",        # here with «tự mình» (sample: none in its text)
    "phassānaṃ": "sự tiếp xúc", "cetanānaṃ": "chủ ý", "cittānaṃ": "tâm", "saddhānaṃ": "niềm tin",
    "satīnaṃ": "sự tỉnh thức", "samādhīnaṃ": "sự định tâm", "paññānaṃ": "trí tuệ",
    "sakkāyadiṭṭhiṃ": "quan điểm về tự ngã", "sakkāyadiṭṭhiṃ jahati": "dứt bỏ quan điểm về tự ngã",
    # ---- 5-281 «thành quả vào dòng là nhờ dứt bỏ ba xiềng xích … thành quả trở lại một lần là nhờ sự tham đắm
    # dục lạc và ác ý suy yếu … dứt bỏ sự tham đắm dục lạc ở dạng thô, ác ý ở dạng thô»
    "sotāpattiphalaṃ": "thành quả vào dòng", "sakadāgāmiphalaṃ": "thành quả trở lại một lần",
    "tanubhāvā": "suy yếu",
    "oḷārikaṃ jahati": "dứt bỏ" + GAP + "ở dạng thô",
    "oḷārikaṃ kāmarāgaṃ jahati": "dứt bỏ sự tham đắm dục lạc ở dạng thô",
    # verses (Tăng Chi Bộ Kinh 6.54) «Đã có các vị ấy … trong thời quá khứ, sáu bậc đạo sư lừng danh; Không còn
    # mùi tanh hôi ô uế, hết lòng hướng về lòng trắc ẩn, đã vượt qua xiềng xích dục lạc. Sau khi làm phai nhạt sự
    # tham đắm dục lạc, các vị ấy đã đi đến cõi Phạm Thiên; Các vị ấy có những đệ tử, đến nhiều trăm người.»
    "atītaṃse": "thời quá khứ",                    # locative frame «trong» dropped
    "yasassino": "lừng danh", "yasassinā": "lừng danh",
    "āma": "tanh hôi ô uế", "gandhā": "mùi",       # nirāmagandhā «không còn mùi tanh hôi ô uế»
    "adhimuttā": "hết lòng hướng về", "karuṇā": "lòng trắc ẩn",
    "atigā": "đã vượt qua", "virājetvā": "sau khi làm phai nhạt", "upagā": "đã đi đến",
    # sutta (Tăng Chi Bộ Kinh 7.66) «bậc đạo sư Su-nét-ta ấy, dù sống lâu như vậy, dù tồn tại lâu dài như vậy, vẫn
    # không thoát khỏi sự sinh, sự lão hóa, sự chết, sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt
    # vọng; … không thoát khỏi khổ đau. Vì sao vậy? Do không hiểu ra, không thấu triệt bốn hiện tượng …»
    "sunetto": "Su-nét-ta", "dīghāyuko": "sống lâu", "ciraṭṭhitiko": "tồn tại lâu dài",
    "parimutto": "thoát khỏi",                     # of aparimutto «không thoát khỏi» (positive part)
    "jātiyā": "sự sinh", "jarāya": "sự lão hóa", "maraṇena": "sự chết",
    "jarāya maraṇena": "sự lão hóa sự chết",       # comma dropped (pi-1; sample kattā kāretā)
    "sokehi": "sự sầu muộn", "paridevehi": "sự than khóc", "dukkhehi": "sự khó chịu",
    "domanassehi": "nỗi buồn", "upāyāsehi": "sự tuyệt vọng", "dukkhasmā": "khổ đau",
    "anubodhā": "hiểu ra", "paṭivedhā": "thấu triệt",   # of ananubodhā / appaṭivedhā (positive part)
    "ariyassa": "cao quý", "sīlassa": "giới hạnh", "samādhissa": "định tâm", "paññāya": "trí tuệ",
    "vimuttiyā": "sự giải thoát",
    "anubuddhaṃ": "đã được hiểu ra", "paṭividdhaṃ": "đã được thấu triệt",
    "bhavataṇhā": "khao khát được hiện hữu", "khīṇā": "đã bị diệt tận",
    "netti": "sợi dây dẫn đến", "bhava": "hiện hữu",
    "puna": "mới",                                 # punabbhavo «sự hiện hữu mới»
    # verses «… Những hiện tượng này đã được bậc Cồ-đàm lừng danh hiểu ra. Như vậy, Đức Phật, sau khi hiểu biết
    # trực tiếp, đã giảng Giáo Pháp cho các tỳ-khưu; Bậc đạo sư, người đi đến tận cùng của khổ đau, bậc có mắt, đã
    # nhập Niết-bàn trọn vẹn»
    "gotamena": "bậc Cồ-đàm",                      # honorific with its noun (pi-1)
    "buddho": "Đức Phật", "abhiññāya": "sau khi hiểu biết trực tiếp",
    "akkhāsi": "đã giảng",
    "karo": "người đi đến",                        # dukkhassantakaro «người đi đến tận cùng của khổ đau» (agent noun
                                                   # with its head noun as the text writes it)
    "satāni": "trăm",
}

OVERRIDES = {
    "5-4-0": {"jahati": "sự dứt bỏ"},              # Jahatikathā «Bàn về sự dứt bỏ»
    "5-4-1-0": {"kathā": "Phần"},                  # Nasuttāharaṇakathā «Phần không dẫn kinh»
    "5-4-2-0": {"kathā": "Phần"},                  # Suttāharaṇakathā «Phần dẫn kinh»
    "5-280": {"vata": "nghi thức"},                # only sīlabbata «giới hạnh và nghi thức» (no «vata re» here)
    "5-281": {"rāgo": "tham đắm"},                 # vītarāgo «đã lìa tham đắm» (kāmarāgaṃ is rāgaṃ)
}

ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value5(kw, kws, T4, vi.get(bid, ""))
    return resolve


def show(lo, hi):
    res = resolver()
    vi = read_vietnamese(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            er = en_ru(bid)
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                e = er.get(kw, ["", ""])
                print(f"   {kw}={v}  [en:{e[0]} | ru:{e[1]}]{flag}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]))
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
