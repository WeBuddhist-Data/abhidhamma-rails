"""Build the pi-5 (Kathāvatthu) Pāli->Vietnamese keyword map for ONE chapter: 3-brahmacariyakatha.

usage: python -I -X utf8 -B map_3_vi.py               (writes 3-brahmacariyakatha.mapped.md and verifies it)
       python -I -X utf8 -B map_3_vi.py dump [miss]   (every keyword=value per segment with English | Russian; no write)

Importing this module builds nothing. Resolution: OVERRIDES[bid][kw] -> value5(kw, kws, T3, text) of map_sample_vi
(T3 -> context5 -> FORMULAS -> KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md, notes-map-3.md.
"""
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
from map_common_vi import GAP, NDE, build_part, en_ru, lc, present, read_keywords, read_vietnamese, verify  # noqa: E402
from map_sample_vi import value5  # noqa: E402

PART = "3-brahmacariyakatha"

T3 = {
    # ---- headings: «Bàn về đời sống tu hành trong sạch», «… qua đối chiếu», «Bàn về sự dứt bỏ từng phần»
    "saṃsandana": "đối chiếu",                     # Saṃsandanabrahmacariyakathā «… qua đối chiếu» (no «Sự» here)
    "odhiso": "từng phần",                         # Odhisokathā «Bàn về sự dứt bỏ từng phần»
    "brahmacariyavāso": "đời sống tu hành trong sạch",
    "vāso": NDE,                                   # brahmacariyavāso: no word of its own («có đời sống tu hành …»)
    # ---- 5-269 «tất cả chư thiên đều đần độn, câm điếc, không hiểu biết, giao tiếp bằng cử chỉ tay, không đủ khả
    # năng hiểu ý nghĩa của lời nói hay và lời nói dở …»
    "jaḷā": "đần độn", "elamūgā": "câm điếc", "viññū": "có hiểu biết", "aviññū": "không hiểu biết",
    "hattha": "cử chỉ tay", "saṃvācikā": "giao tiếp",
    "paṭibalā": "đủ khả năng", "nappaṭibalā": "không đủ khả năng",
    "bhāsita": "lời nói", "dubbhāsitānaṃ": "lời nói dở", "aññātuṃ": "hiểu",
    "pasannā": "có lòng tin trong sáng", "dhamme": "Giáo Pháp",
    "pucchanti": "đặt",                            # pañhaṃ pucchanti «đặt câu hỏi» (pañhaṃ = câu hỏi)
    "pañhe": "câu hỏi", "vissajjite": "trả lời",
    "samannāgatā": "mang",                         # kammāvaraṇena samannāgatā «mang sự ngăn che do nghiệp» (pi-2)
    "mātu": "mẹ", "pitu": "cha", "arahanta": "bậc A-la-hán", "ghātakā": "kẻ giết",
    "ruhira": "máu", "uppādakā": "kẻ làm chảy", "bhedakā": "kẻ chia rẽ",
    "atipātino": "sát hại", "pāṇātipātino": "sát hại sinh mạng",
    "micchācārino": "có hành vi sai trái", "cārino": "có hành vi",
    "vādino": "nói",                               # musāvādino «nói dối»
    "palāpino": "nói lời",                         # samphappalāpino «nói lời phù phiếm» (sampha = phù phiếm)
    "abhijjhāluno": "có sự thèm muốn",
    # ---- 5-270 «sự xuất gia, sự cạo đầu, sự mặc y cà-sa, sự mang bình bát … các bậc Tự Giác Ngộ Hoàn Toàn xuất
    # hiện, các bậc Độc Giác xuất hiện, cặp đệ tử chính xuất hiện»
    "pabbajjā": "sự xuất gia", "pabbajati": "xuất gia",
    "muṇḍiyaṃ": "sự cạo đầu", "muṇḍo": "cạo đầu",
    "dhāraṇā": "sự mặc",                           # kāsāvadhāraṇā «sự mặc» (first; pattadhāraṇā «sự mang»)
    "dhāreti": "mặc",                              # kāsāvaṃ dhāreti «mặc» (first; pattaṃ dhāreti «mang»)
    "patta": "bình bát",
    "sambuddhā": "bậc Tự Giác Ngộ", "sammāsambuddhā": "bậc Tự Giác Ngộ Hoàn Toàn",
    "paccekasambuddhā": "bậc Độc Giác",
    "uppajjanti": "xuất hiện", "uppajjati": "xuất hiện", "uppannaṃ": "đã xuất hiện",
    "sāvaka": "đệ tử", "yugaṃ": "cặp", "sāvakayugaṃ": "cặp đệ tử chính",
    "devesu": "chư thiên", "manussesu": "loài người",   # locative frame «giữa» dropped
    "aññatra": "ở nơi khác",                       # natthaññatra «ở nơi khác không có» (adverb keeps «ở»)
    "bodhiyā": "cây Bồ-đề", "mūle": "gốc",         # bodhiyā mūle «dưới gốc cây Bồ-đề»
    "abhisambuddho": "đã giác ngộ hoàn toàn", "pavattitaṃ": "đã chuyển",
    "janapadesu": "xứ", "magadhesu": "xứ Ma-kiệt-đà",
    # ---- 5-271 «ở các xứ biên địa, giữa những người man di, những người không thông hiểu, nơi mà các tỳ-khưu …
    # không lui tới»; sutta «nhờ ba phương diện, loài người ở Diêm-phù-đề vượt trội hơn loài người ở Bắc Câu-lô
    # châu và chư thiên Ba Mươi Ba … Họ can đảm, có sự tỉnh thức»
    "paccantimesu": "biên địa", "milakkhesu": "người man di",
    "viññātāresu": "thông hiểu",                   # of aviññātāresu «không thông hiểu» (positive part)
    "yattha": "nơi mà", "gati": "lui tới",
    "sañña": "có tri giác",                        # saññasattesu devesu «chư thiên có tri giác»
    "ṭhānehi": "phương diện", "adhiggaṇhanti": "vượt trội hơn",
    "uttarakuruke": "Bắc Câu-lô châu", "tāvatiṃse": "Ba Mươi Ba",
    "sūrā": "can đảm", "satimanto": "có sự tỉnh thức",
    # ---- 5-272 «Đối với bậc không trở lại … khi người ấy chết từ đây và tái sinh ở đó, thành quả sinh khởi ở đâu
    # … gánh nặng được gỡ bỏ ở đâu, khổ đau được hiểu biết trọn vẹn ở đâu, phiền não được dứt bỏ ở đâu, sự chấm dứt
    # được tự mình chứng nghiệm ở đâu, điều không thể bị lay chuyển được thấu triệt ở đâu?»
    "anāgāmissa": "bậc không trở lại",
    "anāgāmī puggalo": "bậc không trở lại",        # the name with its head noun «bậc» renders both words
    "cutassa": "khi" + GAP + "chết",               # ito cutassa «khi người ấy chết từ đây» (participle keeps «khi»)
    "upapannassa": "tái sinh", "uppatti": "sinh khởi",
    "bhāro": "gánh nặng", "oharaṇaṃ": "được gỡ bỏ", "pariññātaṃ": "được hiểu biết trọn vẹn",
    "pahānaṃ": "được dứt bỏ", "sacchikiriyā": "được tự mình chứng nghiệm", "paṭivedho": "được thấu triệt",
    "nirodha": "sự chấm dứt",                      # nirodhasacchikiriyā / Nirodhadassanena «… sự chấm dứt»
    "akuppa": "điều không thể bị lay chuyển",      # the text's «điều» kept (pi-3 asaṅkhataṃ)
    "akuppo": "điều không thể bị lay chuyển",
    "aṭṭhena": "nghĩa",                            # kenaṭṭhena «theo nghĩa nào»
    "bhāvitena": "đã tu tập",                      # idha bhāvitena maggena «nhờ con đường đã tu tập ở đây»
    "sacchikaroti": "tự mình chứng nghiệm",        # here always «tự mình chứng nghiệm» (pi-4)
    # ---- 5-273
    "sotāpanno puggalo": "bậc vào dòng", "sakadāgāmī puggalo": "bậc trở lại một lần",
    "anāgāmī puggalo sacchikaroti": "bậc không trở lại" + GAP + "tự mình chứng nghiệm",
    "puggalo sacchikaroti": "bậc" + GAP + "tự mình chứng nghiệm",
    "parinibbāyipuggalo": "người nhập Niết-bàn trọn vẹn", "parinibbāyi": "nhập Niết-bàn trọn vẹn",
    "parinibbāyati": "nhập Niết-bàn trọn vẹn",
    "niṭṭhassa": "người đạt đến đích", "vihāya": "sau khi rời bỏ",   # Idha vihāya niṭṭhassa «người đạt đến đích sau
                                                                    # khi rời bỏ cõi này»
    "sakadāgāmiphala": "thành quả trở lại một lần", "anāgāmiphala": "thành quả không trở lại",
    "arahatta": "trạng thái A-la-hán", "arahattasacchikiriyāya": "tự mình chứng nghiệm trạng thái A-la-hán",
    "phalaṃ": "thành quả",
    "kata": "đã làm xong",                         # katakaraṇīyo «đã làm xong việc cần làm»
    "bhāvita": "đã hoàn tất",                      # bhāvitabhāvano «đã hoàn tất sự tu tập»
    "ohaṭa": "gỡ bỏ",                              # of anohaṭabhāro «chưa gỡ bỏ gánh nặng» (positive part)
    "oharaṇāya": "gỡ bỏ",                          # bhāroharaṇāya «để gỡ bỏ gánh nặng» (dative «để» frame)
    "pariññāta": "hiểu biết trọn vẹn",             # of apariññātadukkho «chưa hiểu biết trọn vẹn khổ đau»
    "sacchikata": "tự mình chứng nghiệm",          # of asacchikatanirodho
    "paṭividdha": "thấu triệt",                    # of appaṭividdhākuppo
    "paṭivedhāya": "thấu triệt",                   # akuppapaṭivedhāya «để thấu triệt …»
    "puna": "mới",                                 # punabbhavo «sự hiện hữu mới» (first; notes-map-4), also
                                                   # puna maggaṃ bhāveti «… lần nữa»
    "gatiyā": "cõi tái sinh", "saṃsārena": "vòng luân hồi",
    "migo": "con nai", "sallena": "mũi tên", "viddho": "bị trúng", "gantvā": "chạy đi", "kālaṃ karoti": "chết",
    # ---- 5-274 … 5-277 «Người ấy dứt bỏ một phần quan điểm về tự ngã … và các phiền não cùng hiện diện với chúng.
    # Có phải một phần là bậc vào dòng … đã có được, đã chứng đắc, đã tự mình chứng nghiệm, chứng nhập và an trú,
    # chạm đến bằng thân rồi an trú …»
    "jahati": "dứt bỏ", "kilese": "phiền não",
    "odhisodhiso": "từng phần một", "odhisodhiso kilese": "phiền não từng phần một",
    "ekadese": "một phần", "ekadesaṃ": "một phần",
    "ekaṭṭhe": "cùng hiện diện",                   # tadekaṭṭhe «cùng hiện diện với chúng»
    "dassanena": "việc thấy",                      # dukkhadassanena «bằng việc thấy khổ đau»
    "sakkāyadiṭṭhiṃ": "quan điểm về tự ngã",
    "paṭiladdho": "đã có được", "adhigato sacchikato": "đã chứng đắc đã tự mình chứng nghiệm",   # comma dropped
    "sacchikato": "đã tự mình chứng nghiệm",
    "sotāpattiphalappatto": "đã đạt đến thành quả vào dòng",
    "sakadāgāmiphalappatto": "đã đạt đến thành quả trở lại một lần",
    "anāgāmiphalappatto": "đã đạt đến thành quả không trở lại",
    "arahattappatto": "đã đạt đến trạng thái A-la-hán",
    "viharati": "an trú", "phusitvā": "chạm đến",
    "upasampajja viharati": "chứng nhập và an trú",   # pi-1 / pi-2 value
    "phusitvā viharati": "chạm đến" + GAP + "an trú",  # kāyena phusitvā viharati «chạm đến bằng thân rồi an trú»
    "oḷārikaṃ jahati": "dứt bỏ" + GAP + "ở dạng thô",  # notes-map-4
    "oḷārikaṃ ekadese jahati": "dứt bỏ một phần" + GAP + "ở dạng thô",
    "aṇusahagataṃ jahati": "dứt bỏ" + GAP + "ở dạng nhỏ nhiệm",
    "ekabījī": "người có một hạt giống",
    "samannāgato": "có",                           # aveccappasādena / ariyakantehi sīlehi samannāgato «có …»
    "avecca": "không lay chuyển", "pasādena": "niềm tin trong sáng",
    "kantehi": "được" + GAP + "yêu quý", "sīlehi": "giới hạnh",
    "ariyakantehi sīlehi": "giới hạnh được các bậc thánh yêu quý",   # inner «các» kept
    "rāgaṃ": "sự tham đắm", "kāmarāgaṃ": "sự tham đắm dục lạc",
    "aṇu": "nhỏ nhiệm", "aṇusahagataṃ": "ở dạng nhỏ nhiệm",
    "saṅkhāra": "sự thúc đẩy",                     # a- / sasaṅkhāraparinibbāyī (pi-4)
    "uddhaṃsoto": "người theo dòng đi lên", "gāmī": "đến",   # «người theo dòng đi lên đến cõi Sắc Cứu Cánh»
    "anāgāmiphalasacchikiriyāya": "tự mình chứng nghiệm thành quả không trở lại",
    # 5-277 the arahant string
    "rūparāgaṃ": "sự tham đắm cõi hình sắc", "rūpa": "cõi hình sắc", "arūpa": "cõi không hình sắc",
    "avijjaṃ": "vô minh", "pahīno": "đã được dứt bỏ",
    "vīta": "đã lìa", "vītadoso": "đã lìa sân hận", "vītamoho": "đã lìa si mê", "doso": "sân hận", "moho": "si mê",
    "ohita": "đã đặt" + GAP + "xuống",            # ohitabhāro «đã đặt gánh nặng xuống»
    "attho": "mục đích",                           # anuppattasadattho «đã đạt đến mục đích của chính mình»
    "pari": "hoàn toàn", "khīṇa": "đã diệt tận", "bhava": "sự hiện hữu",   # parikkhīṇabhavasaṃyojano
    "aññā": "hiểu biết trọn vẹn",                  # sammadaññāvimutto «… nhờ hiểu biết trọn vẹn …» (pi-3)
    "ukkhitta": "đã nhấc bỏ", "paligho": "thanh chắn", "saṅkiṇṇa": "đã lấp", "parikho": "hào",
    "abbūḷha": "đã nhổ", "esiko": "cột trụ", "aggaḷo": "then cửa",
    "panna": "đã hạ",                              # pannaddhajo «đã hạ ngọn cờ» (first; pannabhāro «đã buông bỏ»)
    "visaññutto": "đã thoát khỏi trói buộc",
    "su": "trọn vẹn", "vijita": "đã chiến thắng", "vijayo": "chiến thắng",   # suvijitavijayo «đã chiến thắng trọn
                                                                              # vẹn» (Vietnamese fuses vijita-vijaya)
    "nirodho sacchikato": "sự chấm dứt đã được tự mình chứng nghiệm",
    "bhāvito": "đã được tu tập", "abhiññeyyaṃ": "điều cần được hiểu biết trực tiếp",
    # ---- 5-278 sutta quotes
    "medhāvī": "người trí", "kammāro": "người thợ luyện", "niddhame": "gột sạch", "malaṃ": "cấu uế",
    "sampadāya": "sự thành tựu", "dassana": "thấy chân lý",   # dassanasampadāya «sự thành tựu thấy chân lý»
    "jahitā": "được dứt bỏ", "sakkāyadiṭṭhī": "quan điểm về tự ngã", "vicikicchitaṃ": "sự hoài nghi",
    "sīlabbataṃ": "giới hạnh và nghi thức", "kiñci": "bất cứ" + GAP + "nào",
    "apāyehi": "cõi khổ", "vippamutto": "được giải thoát", "abhiṭhānāni": "trọng tội",
    "abhabba": "không thể", "abhabbo": NDE,        # abhabbo only in the bracket [khác chính tả (Sī., Syā.): abhabbo]
    "kātuṃ": "làm", "khu": "Tiểu Tụng",            # [khu. pā. 6.10 …] «[Tiểu Tụng 6.10 …]»
    "sāvakassa": "vị đệ tử",                       # ariyasāvakassa «vị đệ tử cao quý» (classifier kept)
    "virajaṃ": "không bụi bặm", "vītamalaṃ": "không cấu uế", "cakkhuṃ": "con mắt", "udapādi": "sinh khởi",
}

OVERRIDES = {
    "5-3-1-0": {"kathā": "Bàn" + GAP + "về"},       # «Bàn thuần túy về đời sống tu hành trong sạch»
    "5-274": {"vata": "nghi thức"},                # sīlabbata «giới hạnh và nghi thức» (no «re vata» here)
    "5-277": {"pariññātaṃ": "đã được hiểu biết trọn vẹn"},   # pariññeyyaṃ pariññātaṃ (notes-map-2 arahant formula)
    "5-278": {"vata": "nghi thức", "nirodha": "chấm dứt",   # nirodhadhammaṃ «có bản chất chấm dứt»
              "samudaya": "phát sinh"},            # samudayadhammaṃ «có bản chất phát sinh»
}

ALLOWED = {}


def context_3(kw, kws, text):
    """Segment rules of this chapter (None = no rule)."""
    if kw == "kilese jahati":      # «dứt bỏ các phiền não» (inner «các» kept) / «dứt bỏ …, và các phiền não»
        return "dứt bỏ các phiền não" if present("dứt bỏ các phiền não", text) else "dứt bỏ" + GAP + "phiền não"
    return None


def resolve(bid, kw, kws, vi):
    ov = OVERRIDES.get(bid, {})
    if kw in ov:
        return ov[kw]
    text = vi.get(bid, "")
    v = context_3(kw, kws, text)
    if v is not None:
        return v
    return value5(kw, kws, T3, text)


def dump(only_miss=False):
    vi = read_vietnamese(PART)
    for bid, kws in read_keywords(PART):
        er = en_ru(bid)
        out = []
        for kw in kws:
            try:
                v = resolve(bid, kw, kws, vi)
            except KeyError:
                v = "???"
            flag = "" if v == NDE or (v != "???" and present(v, vi.get(bid, ""))) else " <<MISS"
            if only_miss and not flag:
                continue
            e = er.get(kw, ["", ""])
            out.append(f"{kw}={v} [{e[0]} | {e[1]}]{flag}")
        print(f"== [{bid}]")
        for o in out:
            print("   " + o)


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    else:
        _vi = read_vietnamese(PART)
        build_part(PART, lambda bid, kw, kws: resolve(bid, kw, kws, _vi))
        verify(PART, ALLOWED)
