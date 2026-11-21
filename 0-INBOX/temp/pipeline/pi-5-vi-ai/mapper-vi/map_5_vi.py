"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 5: 5-sabbamatthitikatha.

usage: python -I -X utf8 -B map_5_vi.py                  (writes 5-sabbamatthitikatha.mapped.md and verifies it)
       python -I -X utf8 -B map_5_vi.py show lo hi [pi]   (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> value5(kw, kws, T5, text) of map_sample_vi (T5 -> context5 ->
FORMULAS -> KV -> two-word composition -> the pi-4 chain).
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, GAP, build_part, en_ru, join, lc, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "5-sabbamatthitikatha"

_KN = "không biết ghê sợ tội lỗi"

T5 = {
    # ---- headings: «Bàn về việc cho rằng tất cả đều tồn tại», «Lập luận về học thuyết», «Sự đối chiếu theo thời
    # gian», «Sự làm sáng tỏ từ ngữ», «Bàn về mắt, hình sắc quá khứ …», «Bàn về sự gộp chung các khối quá khứ …»,
    # «Bàn về sự làm sáng tỏ thuật ngữ», «Chứng cứ từ kinh»
    "sabbaṃ": "tất cả",
    "yutti": "Lập luận", "vāda": "học thuyết", "kāla": "thời gian",
    "sodhanā": "Sự làm sáng tỏ",                   # as FORMULAS sodhanaṃ
    "sodhana": "sự làm sáng tỏ",                   # «Bàn về sự làm sáng tỏ thuật ngữ» (lower case as written)
    "pada": "thuật ngữ",
    "atītacakkhu": "mắt" + GAP + "quá khứ",        # «mắt, hình sắc quá khứ»
    "ñāṇa": "hiểu biết", "atītañāṇa": "hiểu biết quá khứ",
    "arahanta": "bậc A-la-hán",
    "hattha": "bàn tay", "atītahattha": "bàn tay quá khứ",   # the text writes «bàn tay» (KV hattha «tay»: «bị chặt tay»)
    "samodhāna": "sự gộp chung", "atītakkhandha": "khối quá khứ",
    "sādhanaṃ": "Chứng cứ",
    # ---- 5-282 «… theo mọi cách … khi coi là không có sự kết hợp …»
    "sabbena": "theo mọi cách",                    # Sabbena sabbaṃ (adverb keeps its preposition, as Sabbattha)
    "yogaṃ": "sự kết hợp",                         # of ayogaṃ «không có sự kết hợp» (positive part)
    "katvā": "khi coi",                            # Ayoganti katvā «khi coi là …» (sample karitvā «khi xem»; «là» = the
                                                   # quote frame -ti)
    # ---- 5-283 / 5-284 «chưa sinh ra, chưa trở thành, chưa sinh thành …» / «đã chấm dứt … đã biến mất …»
    "sañjātaṃ": "đã sinh thành", "ajātaṃ": "chưa sinh ra", "atthaṅgataṃ": "đã biến mất",
    "anāgataṃ viññāṇaṃ ajātaṃ": "thức thuộc tương lai chưa sinh ra",
    # ---- 5-285 «… như nhau, ngang nhau, cùng một loại … tấm vải trắng, khi đang được nhuộm …»
    "samabhāge": "ngang nhau", "tajjāte": "cùng một loại",
    "vatthaṃ": "vải", "odātaṃ": "trắng",
    "rajjamānaṃ": "khi đang được nhuộm",           # participles keep «khi» (sample vediyamāno «khi đang cảm nhận»)
    "nirujjhamānaṃ": "khi đang chấm dứt",
    # ---- 5-286 / 5-287 «thường còn, bền vững, trường tồn … vô thường, không bền vững …»; variant notes
    "niccaṃ": "thường còn", "dhuvaṃ": "bền vững", "sassataṃ": "trường tồn", "adhuvaṃ": "không bền vững",
    "jahati": "dứt bỏ",                            # ch4
    "aṭṭhakathā": "Chú giải",                      # [… ; cần tham khảo Chú giải] (after the colon: ALLOWED)
    "pañho": "câu hỏi", "pañhehi": "câu hỏi",      # [… ; đây chỉ là câu hỏi theo chiều thuận], [… các câu hỏi trước]
    # ---- 5-288 «… quá khứ không tồn tại … cái không phải là quá khứ là quá khứ»
    "vā pana": "hoặc",
    "nvātītaṃ atītaṃ": "cái không phải là quá khứ là quá khứ",
    "nvānāgataṃ anāgataṃ": "cái không phải là tương lai là tương lai",
    "no paccuppannaṃ paccuppannaṃ": "cái không phải là hiện tại là hiện tại",
    # ---- 5-289 «… ánh sáng tồn tại … ý thức tồn tại, chỗ dựa tồn tại … nhận biết đối tượng của ý thuộc quá khứ»
    "vatthuṃ": "chỗ dựa", "dhammaṃ": "đối tượng của ý",
    # ---- 5-290 «nhờ hiểu biết ấy mà làm được việc của hiểu biết … hiểu biết trọn vẹn khổ đau, dứt bỏ sự phát sinh,
    # tự mình chứng nghiệm sự chấm dứt, tu tập con đường»
    "ñāṇaṃ": "hiểu biết",                          # the text has no «sự» here (sample 5-232 «sự hiểu biết»)
    "ñāṇena ñāṇakaraṇīyaṃ": "hiểu biết" + GAP + "việc của hiểu biết",
    "pajahati": "dứt bỏ", "parijānāti": "hiểu biết trọn vẹn", "dukkhaṃ parijānāti": "hiểu biết trọn vẹn khổ đau",
    "sacchikaroti": "tự mình chứng nghiệm",        # ch4 (the text has «tự mình»)
    # ---- 5-291 / 5-292 «sự tham đắm thuộc quá khứ của bậc A-la-hán … sự kiêu mạn … ác ý ở dạng nhỏ nhiệm … sự si
    # mê dẫn đến cõi khổ … có tâm ác ý … mà có quan điểm»
    "arahato": "bậc A-la-hán", "anāgāmissa": "bậc không trở lại", "sotāpannassa": "bậc vào dòng",
    "puthujjanassa": "người phàm phu", "puthu": "phàm phu", "jana": "người",   # ch4
    "māno": "sự kiêu mạn",                         # the text writes «sự» (pi-1 / pi-2)
    "ottappaṃ": "biết ghê sợ tội lỗi",             # of anottappaṃ «sự không biết …» (positive part, pi-1 sampajañña)
    "anottappī": _KN,                              # «mà không biết ghê sợ tội lỗi» (5-292; 5-291 by override)
    "oḷāriko": "ở dạng thô", "oḷāriko byāpādo": "ác ý ở dạng thô",
    "atīto oḷāriko": "ở dạng thô thuộc quá khứ", "atīto oḷāriko byāpādo": "ác ý ở dạng thô thuộc quá khứ",
    "aṇu": "nhỏ nhiệm",
    "atīto aṇusahagato": "ở dạng nhỏ nhiệm thuộc quá khứ",
    "atīto aṇusahagato byāpādo": "ác ý ở dạng nhỏ nhiệm thuộc quá khứ",
    "apāya": "cõi khổ", "gamanīyo": "dẫn đến", "apāyagamanīyo": "dẫn đến cõi khổ",
    "diṭṭhiko": "có quan điểm",                    # sadiṭṭhiko «có quan điểm» (-ika keeps «có», pi-1)
    # ---- 5-293 «các bàn tay … việc cầm lên và đặt xuống … các bàn chân … việc đi tới và đi lui … các khớp … việc
    # co và duỗi … bụng … sự đói và sự khát … có thể bị nắm giữ và kìm kẹp, có thể bị cắt và bị đập vỡ, là thứ chung
    # cho quạ, kền kền, diều hâu … chất độc … dao kiếm … lửa … trói … bằng cùm, … dây thừng, … xích sắt, … sự giam
    # giữ trong làng / thị trấn / thành phố …, năm dây trói mà dây thứ năm ở cổ … việc của nước»
    "hatthā": "bàn tay", "pādā": "bàn chân", "pabbā": "khớp",
    "atītā hatthā": "bàn tay thuộc quá khứ", "atītā hatthā atthi": "bàn tay thuộc quá khứ tồn tại",
    "atītā pādā atthi": "bàn chân thuộc quá khứ tồn tại", "atītā pabbā atthi": "khớp thuộc quá khứ tồn tại",
    "ādāna": "cầm lên", "nikkhepanaṃ": "đặt xuống", "abhikkama": "đi tới",
    "samiñjana": "co", "pasāraṇaṃ": "duỗi",        # «việc co và duỗi» («việc» = the compound's nominaliser)
    "jighacchā": "sự đói", "pipāsā": "sự khát",
    "chedana": "bị cắt", "bhedana": "bị đập vỡ",   # «có thể bị cắt và bị đập vỡ»
    "sādhāraṇo": "thứ chung", "kākehi": "quạ", "gijjhehi": "kền kền", "kulalehi": "diều hâu",
    "visaṃ": "chất độc", "satthaṃ": "dao kiếm", "aggi": "lửa",
    "bandhituṃ": "trói", "bandhanena": "sự giam giữ",   # «trói bằng sự giam giữ trong làng» (only word for bandhana)
    "addu": "cùm", "rajju": "dây thừng", "saṅkhalika": "xích sắt",
    "gāma": "làng", "nigama": "thị trấn", "nagara": "thành phố",
    "kaṇṭha": "cổ", "pañcamehi": "thứ năm", "bandhanehi": "dây trói",
    # ---- 5-294 «… có năm mươi bốn yếu tố … sáu mươi sáu năng lực … ba vị vua chuyển luân cùng hiện diện đối mặt
    # nhau … bậc Tự Giác Ngộ Hoàn Toàn thuộc quá khứ» (Pāli sammāsammuddho, rendered as meant: sammāsambuddho)
    "catupaññāsa": "năm mươi bốn", "chasaṭṭhi": "sáu mươi sáu",
    "atītāni bāvīsatindriyāni atthi": "hai mươi hai năng lực thuộc quá khứ tồn tại",
    "rājūnaṃ": "vua", "sammukhībhāvo": "cùng hiện diện đối mặt nhau",
    "sammuddho": "bậc Tự Giác Ngộ", "sambuddhānaṃ": "bậc Tự Giác Ngộ",
    "sammāsammuddho": "bậc Tự Giác Ngộ Hoàn Toàn", "sammāsambuddhānaṃ": "bậc Tự Giác Ngộ Hoàn Toàn",
    "atīto sammāsammuddho": "bậc Tự Giác Ngộ Hoàn Toàn thuộc quá khứ",
    # ---- 5-296 sutta quotes
    # [Tương Ưng Bộ Kinh 3.48] «… ở nơi bản thân hay ở bên ngoài bản thân …»
    "bahiddhā": "ở bên ngoài bản thân",            # pi-1 / pi-2 (KV «bên ngoài»: 5-228 «ra bên ngoài»)
    # «ba phạm vi của cách diễn đạt, phạm vi của tên gọi, phạm vi của sự định danh …, không lẫn lộn, trước đây chưa
    # từng lẫn lộn …, không bị các sa-môn, bà-la-môn có trí phản đối … cách gọi của nó …»
    "pathā": "phạm vi",                            # pi-1 MATRIX
    "adhivacana": "tên gọi", "saṅkhā": "cách gọi",
    "saṅkiṇṇa": "lẫn lộn", "asaṅkiṇṇā": "không lẫn lộn", "asaṅkiṇṇapubbā": "trước đây chưa từng lẫn lộn",
    "paṭikuṭṭhā": "bị" + GAP + "phản đối",         # of appaṭikuṭṭhā «không bị … phản đối» (positive part)
    "samaṇehi": "sa-môn", "brāhmaṇehi": "bà-la-môn", "viññūhi": "có trí",
    # «những người ở xứ Úc-ca-la là Vát-sa và Bhan-nha, những người theo học thuyết không có nguyên nhân, … hư vô,
    # … là không nên chê trách … Vì sợ bị chê bai, bị công kích, bị chỉ trích»
    "vassa": "Vát-sa", "vādā": "người theo học thuyết",   # as vādī (FORMULAS)
    "hetuka": "có nguyên nhân",                    # of ahetukavādā «không có nguyên nhân» (positive part)
    "natthika": "hư vô", "garahitabbaṃ": "nên chê trách",
    "nindā": "bị chê bai", "byārosa": "bị công kích", "upārambha": "bị chỉ trích", "bhayā": "sợ",
    # [Tương Ưng Bộ Kinh 4.83] «tôn giả Phả-cầu-na … có con mắt nào mà nhờ con mắt ấy, khi mô tả các vị Phật thuộc
    # quá khứ đã nhập Niết-bàn trọn vẹn, đã cắt đứt sự suy diễn lan man, đã cắt đứt lối mòn, đã chấm dứt vòng xoay,
    # đã vượt qua mọi khổ đau, người ta có thể mô tả được … có cái lưỡi nào»
    "phagguno": "Phả-cầu-na",                      # cakkhuṃ «con mắt», jivhā «cái lưỡi»: override ^5-296
    "puna": "mới",                                 # punabbhavābhinibbatti «sự hiện hữu mới» (ch4)
    "atīte": "thuộc quá khứ", "buddhe": "vị Phật", "atīte buddhe": "vị Phật thuộc quá khứ",
    "papañce": "sự suy diễn lan man", "vaṭume": "lối mòn", "vaṭṭe": "vòng xoay", "vītivatte": "đã vượt qua",
    "paññāpayamāno": "khi mô tả", "atīte paññāpayamāno": "khi mô tả" + GAP + "thuộc quá khứ",
    "paññāpeyya": "có thể mô tả được",
    # [Tăng Chi Bộ Kinh] «tôn giả Nan-đa-ka … Trước đây đã có sự tham lam»
    "nandako": "Nan-đa-ka", "pubbe": "trước đây",
    # [Tương Ưng Bộ Kinh 2.64] «nếu nơi thức ăn trong vai trò dưỡng chất tồn tại sự tham đắm, tồn tại sự thích thú,
    # tồn tại khao khát, thì thức được thiết lập ở đó và phát triển … sự hình thành của phần tinh thần và vật chất …
    # sự phát sinh của sự hiện hữu mới … sự sinh, sự lão hóa và sự chết … có sầu muộn, có bụi bặm [dị bản (…):
    # sadaraṃ; cách đọc ấy hợp lý hơn], có tuyệt vọng … chủ ý của ý … không sầu muộn, không bụi bặm»
    "kabaḷīkāre": "thức ăn", "āhāre": "dưỡng chất", "rāgo": "sự tham đắm", "nandī": "sự thích thú",
    "patiṭṭhitaṃ": "được thiết lập", "virūḷhaṃ": "phát triển",
    "avakkanti": "sự hình thành", "nāmarūpassa": "phần tinh thần và vật chất",
    "jarāmaraṇaṃ": "sự lão hóa và sự chết",
    "sasokaṃ": "có sầu muộn", "sokaṃ": "sầu muộn",   # sokaṃ of asokaṃ «không sầu muộn» (positive part)
    "rajaṃ": "bụi bặm", "upāyāsaṃ": "tuyệt vọng",  # of sarajaṃ / arajaṃ, saupāyāsaṃ / anupāyāsaṃ (no sa- in the kw)
    "yuttataraṃ": "hợp lý hơn",                    # [dị bản (…): sadaraṃ; cách đọc ấy hợp lý hơn] (ALLOWED)
    "sañcetanāya": "chủ ý",                        # manosañcetanāya «chủ ý của ý» (pi-1)
}

# «<subject> <predicate>» keywords: the subject first, as the Vietnamese clause stands («thức thuộc quá khứ tồn tại»,
# «sự tham đắm thuộc quá khứ của bậc A-la-hán tồn tại»): contiguous, else « … » in that order. The two-word
# composition would otherwise pair the predicate with the NEXT clause's subject («tồn tại, thức …»).
_PRED = {"atthi": "tồn tại", "nvatthi": "không tồn tại", "jahati": "dứt bỏ", "niccaṃ": "thường còn",
         "aniccaṃ": "vô thường", "niruddhaṃ": "đã chấm dứt", "ajātaṃ": "chưa sinh ra", "jātaṃ": "đã sinh ra",
         "nirujjhamānaṃ": "khi đang chấm dứt"}
_SUBJ_BARE = {"atītaṃ": "quá khứ", "anāgataṃ": "tương lai", "paccuppannaṃ": "hiện tại"}   # the nouns «quá khứ» …


def subject_predicate(kw, kws, text):
    words = kw.split()
    k = [lc(w) for w in words]
    if len(words) >= 3 and k[-2:] == ["na", "jahati"]:
        pred, subj = "không dứt bỏ", words[:-2]
    elif len(words) >= 2 and k[-1] in _PRED:
        pred, subj = _PRED[k[-1]], words[:-1]
    else:
        return None
    s = " ".join(subj)
    sv = _SUBJ_BARE.get(lc(s))
    if sv is None:
        try:
            sv = value5(s, kws, T5, text)
        except KeyError:
            return None
    if not sv or sv == NDE:
        return None
    return join(text, [sv, pred])


OVERRIDES = {
    "5-5-4-0": {"rūpa": "hình sắc"},               # «mắt, hình sắc quá khứ»
    "5-291": {"vata": "nghi thức",                 # only sīlabbata «giới hạnh và nghi thức» (ch4 ^5-280)
              "anottappī": "sự " + _KN},           # saanottappī «mà có sự không biết ghê sợ tội lỗi» («có» = sa-)
    "5-296": {"cakkhuṃ": "con mắt", "jivhā": "cái lưỡi"},   # «có con mắt nào …», «có cái lưỡi nào» (the text's
                                                             # classifiers kept; 5-289 «mắt», «lưỡi»)
}

ALLOWED = {
    ("5-286", "aṭṭhakathā"): "«cần tham khảo Chú giải» is the translated note after the colon of the variant "
                             "bracket [dị bản (nhiều bản): na jahatīti; …], which present() strips",
    ("5-286", "oloketabbā"): "same bracket as aṭṭhakathā",
    ("5-287", "anuloma"): "«đây chỉ là câu hỏi theo chiều thuận» (anulomapañhoyeva) is the translated note after "
                          "the colon of the variant bracket [dị bản (nhiều bản): na jahatīti; …]",
    ("5-287", "pañho"): "same bracket as anuloma",
    ("5-287", "pañhehi"): "«cần đối chiếu với các câu hỏi trước» (purimapañhehi saṃsandetabbaṃ) is the translated "
                          "note after the colon of [dị bản (?): na jahatīti; …]",
    ("5-296", "yuttataraṃ"): "«cách đọc ấy hợp lý hơn» (tadeva yuttataraṃ) is the translated note after the colon of "
                             "[dị bản (Tương Ưng Bộ Kinh 2.64): sadaraṃ; …]",
}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = vi.get(bid, "")
        if lc(kw) not in T5:
            v = subject_predicate(kw, kws, text)
            if v:
                return v
        return value5(kw, kws, T5, text)
    return resolve


def show(lo, hi, with_pali=False):
    res = resolver()
    vi = read_vietnamese(PART)
    pi = read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            if with_pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"-- VI {vi.get(bid, '')}")
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
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
