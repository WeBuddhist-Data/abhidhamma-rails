"""Build the Pāli->Vietnamese keyword map for pi-4 part 4-tikapuggalapannatti (chapter 4).

usage: python -I -X utf8 map_4_vi.py                     (writes 4-tikapuggalapannatti.mapped.md and verifies it)
       python -I -X utf8 map_4_vi.py show lo hi          (segments lo..hi: Pāli, Vietnamese, pairs; writes nothing)
       python -I -X utf8 map_4_vi.py dump [miss]         (every distinct keyword=value; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T4 (this script's table) -> map_common_vi.value():
context4 -> PG -> the pi-3 chain.
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, NDE, build_part, en_ru, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           pi3_map_values, present, read_keywords, read_pali, read_vietnamese, value, verify)

PART = "4-tikapuggalapannatti"

# part-specific values (the tika definitions ^4-91 … ^4-131, read from the segments)
T4 = {
    # ---- the dussīla string (^4-91, ^4-124) and the sīlavā pair (^4-92, ^4-126)
    "pāpa": "xấu",                                            # pāpadhammo / pāpamitto / pāpasahāyo … (map_3: «xấu»)
    "pāpadhammo": "có phẩm chất xấu", "kalyāṇadhammo": "có phẩm chất tốt",   # attribute, no head noun (map_3)
    "sīlavā": "giữ giới", "puggalo dussīlo": "người phạm giới",              # (map_3)
    "asuci": "không trong sạch", "saṅkassara": "đáng ngờ", "samācāro": "hành vi",
    "paṭicchanna": "che giấu", "kammanto": "việc làm",        # «che giấu việc làm của mình»
    "paṭiñño": "tự xưng là",                                  # samaṇa- / brahmacāripaṭiñño «tự xưng là …»
    "brahma": "trong sạch", "cariyaṃ": "đời sống tu hành",   # brahmacariya «đời sống tu hành trong sạch» (map_3)
    "cārī": "sống", "brahmacārī": "sống đời sống tu hành trong sạch",
    "brahmacariyaṃ": "đời sống tu hành trong sạch",
    "pūti": "mục nát", "avassuto": "rỉ chảy dục vọng", "kasambu": "rác rưởi",
    # ---- the arahatta formula
    "kira": "người ta nói", "itthaṃ": "như thế này", "nāmo": "tên", "suṇāti": "nghe",
    "khayā": "sự diệt tận", "anāsavaṃ": "không còn ô nhiễm", "abhiññā": "hiểu biết trực tiếp",   # (map_3 abhiññā)
    "cetovimuttiṃ paññāvimuttiṃ": "sự giải thoát của tâm sự giải thoát nhờ trí tuệ",   # comma dropped
    "viharissāmi": "an trú", "paṭippassaddhā": "đã lắng xuống",
    "vimuttassa": "được giải thoát",                          # avimuttassa «khi chưa được giải thoát» (fragment)
    # ---- the sick-man simile (^4-94)
    "anuññātaṃ": "đã cho phép", "vinayaṃ": "Giới Luật", "paveditaṃ": "tuyên bố",
    "paveditaṃ vinayaṃ": "Giới Luật" + GAP + "tuyên bố",     # as the sample's paveditā dhammā
    "dhammavinayaṃ": "Giáo Pháp và Giới Luật", "okkamati": "bước vào", "puggalo okkamati": "người" + GAP + "bước vào",
    "evameva": NDE,                                           # only the bracket [evameva (sī.)] kept in Pāli (as nikujjo)
    "bhojanāni": "thức ăn", "bhesajjāni": "thuốc men", "sappāyāni": "thích hợp",
    "sappāyāni bhojanāni": "thức ăn thích hợp", "sappāyāni bhesajjāni": "thuốc men thích hợp",
    "saṃvijjamānā": "được tìm thấy", "savaṇāya": "nghe", "dhamma savaṇāya": "nghe Giáo Pháp",
    "dhammassavaṇāya": "nghe Giáo Pháp", "ābādhā": "bệnh",
    "upaṭṭhākaṃ": "người chăm sóc", "upaṭṭhāko": "người chăm sóc", "upaṭṭhātabbā": "cần được chăm sóc",
    "patirūpaṃ": "phù hợp", "patirūpaṃ upaṭṭhākaṃ": "người chăm sóc phù hợp",
    "aññesaṃ": "người khác", "gilāno": "người bệnh", "vuṭṭhāti": "khỏi", "gilāno vuṭṭhāti": "người bệnh" + GAP + "khỏi",
    "desetabbo": "cần được thuyết giảng",
    # ---- gūtha- / puppha- / madhubhāṇī (^4-98 … ^4-100)
    "musāvādī": "nói dối", "musāvādaṃ": "việc nói dối", "paṭivirato": "kiêng tránh",
    "parisa": "hội chúng", "ñāti": "họ hàng", "pūga": "phường hội",
    "rāja": "hoàng tộc", "kula": "tộc",                       # rājakula «hoàng tộc» (one Vietnamese word)
    "abhinīto": "được đưa ra", "sakkhi": "làm chứng", "puṭṭho": "được hỏi",
    "bho": "này", "purisa": "ông", "ehi": "hãy đến đây", "vadehi": "hãy nói",   # «Này ông, hãy đến đây, hãy nói …»
    "jānaṃ": "biết", "passaṃ": "thấy", "sampajāna": "cố ý",   # sampajānamusā «cố ý nói dối»
    "hetu": "vì lợi ích",                                     # attahetu «vì lợi ích của bản thân»
    "āmisa": "lợi lộc vật chất",
    "nelā": "không có lỗi", "kaṇṇa": "tai", "pemaniyā": "dễ mến", "hadaya": "lòng", "gamā": "thấm vào",
    "porī": "lịch sự", "kantā": "yêu mến", "manāpā": "ưa thích",
    "puggalo bhāsitā": "người" + GAP + "nói",
    # ---- arukūpama / the angry man (^4-101, ^4-125)
    "kodhano": "giận dữ", "puggalo kodhano": "người giận dữ",   # attribute «có người giận dữ» (map_3 ^4-65)
    "upāyāsa": "bực tức", "bahulo": "dễ",                    # upāyāsabahulo «dễ bực tức»
    "abhisajjati": "nổi cáu", "kuppati": "nổi giận", "byāpajjati": "khởi thù hằn",
    "patitthīyati": "trở nên cố chấp", "kopaṃ": "sự nổi nóng", "dosaṃ": "sự sân hận",
    "appaccayaṃ": "sự bất mãn", "upama": "giống như", "duṭṭha": "lở loét",
    "kaṭṭhena": "que gỗ", "kaṭhalāya": "mảnh sành", "ghaṭṭito": "chạm vào", "āsavaṃ deti": "chảy mủ",
    "assavanoti": NDE, "kathalena": NDE,                      # only inside variant brackets kept in Pāli
    "aṭṭhakathā": "Chú giải",                                 # bracket label «dị bản (Chú giải)» (ALLOWED)
    "puggalo citto": "người có tâm", "bhiyyoso": "nhiều hơn nữa",
    "akkoseyya": "mắng nhiếc", "paribhāseyya": "lăng mạ", "anatthaṃ": "điều bất lợi",
    "tinduka": "cây thị", "alātaṃ": "khúc củi" + GAP + "đang cháy",   # tindukālātaṃ «khúc củi cây thị đang cháy»
    "cicciṭāyati": "kêu xèo xèo", "ciṭiciṭāyati": "nổ lách tách",
    "gūthakūpo": "hố phân", "duggandho": "mùi hôi thối", "aruko": "vết thương lở loét",
    # ---- vijjūpama / vajirūpama (^4-102, ^4-103)
    "cakkhumā": "có mắt", "ratta": "đêm đen", "andhakāra": "bóng tối", "timisāya": "dày đặc",
    "antarikāya": "lóe lên",                                  # vijjantarikāya «nhờ một tia chớp lóe lên»
    "natthi kiñci": "không có gì", "abhejjaṃ": "không thể cắt đứt", "maṇi": "ngọc", "pāsāṇo": "đá",
    # ---- andha / ekacakkhu / dvicakkhu (^4-104 … ^4-106)
    "cakkhu": "con mắt", "tathārūpaṃ cakkhu": "loại con mắt", "bhogaṃ": "tài sản", "adhigataṃ": "đã đạt được",
    "jāneyya": "biết", "akusale dhamme": "hiện tượng" + GAP + "bất thiện",   # «các hiện tượng thiện và bất thiện»
    "sāvajja": "có lỗi", "anavajje": "không có lỗi", "anavajje dhamme": "hiện tượng" + GAP + "không có lỗi",
    "paṇīte dhamme": "hiện tượng" + GAP + "ưu việt", "kaṇha": "đen tối", "sukka": "trong sáng",
    "sukka dhamme": "hiện tượng" + GAP + "trong sáng", "paṭibhāge": "đối lập",
    # ---- avakujja / ucchaṅga / puthupañña (^4-107 … ^4-109)
    "ārāmaṃ": "tu viện", "ārāmaṃ savaṇāya": "tu viện" + GAP + "nghe", "gantā": "đến", "abhikkhaṇaṃ": "thường xuyên",
    "gato": "đã rơi vào",                                     # ^4-124 gūthagato; ^4-107 bracket only (override)
    "bhikkhū desenti": "tỳ-khưu thuyết giảng", "ādi": "phần đầu", "majjhe": "phần giữa",
    "majjhekalyāṇaṃ": "tốt đẹp ở phần giữa", "atthaṃ": "ý nghĩa", "byañjanaṃ": "văn từ",
    "kevala": "hoàn toàn", "paripuṇṇaṃ": "đầy đủ", "parisuddhaṃ": "thanh tịnh",
    "paripuṇṇaṃ parisuddhaṃ": "đầy đủ" + GAP + "thanh tịnh",  # «hoàn toàn đầy đủ, hoàn toàn thanh tịnh»
    "pakāsenti": "làm sáng tỏ", "brahmacariyaṃ pakāsenti": "làm sáng tỏ đời sống tu hành trong sạch",
    "āsane": "chỗ ngồi", "nisinno": "ngồi", "kathāya": "bài giảng",
    "manasi": "chú tâm",                                      # manasi karoti «chú tâm» (one Vietnamese word)
    "neva manasi karoti": "không chú tâm", "puggalo pañño": "người có trí tuệ",
    "kumbho": "cái chum", "nikkujjo": "bị úp ngược", "ukkujjo": "được đặt ngửa", "nikujjo": NDE,
    "udakaṃ": "nước", "āsittaṃ": "đổ", "tatra": "vào đó", "vivaṭṭati": "chảy tràn đi", "saṇṭhāti": "đọng lại",
    "purisassa": "người", "khajjakāni": "đồ ăn", "ākiṇṇāni": "đựng",
    "tilā": "mè", "taṇḍulā": "gạo", "modakā": "bánh ngọt", "badarā": "táo ta",
    "vuṭṭhahanto": "đứng dậy", "satisammosā": "mất tỉnh thức", "pakireyya": "làm" + GAP + "rơi vãi",
    "puthu": "rộng lớn",                                      # puthupañño (as 4-M-9)
    # ---- kāmesu … vītarāgo, the paripūrakārī trio (^4-110 … ^4-112, ^4-127 … ^4-129)
    "sotāpanna": "bậc vào dòng", "sakadāgāmino": "bậc trở lại một lần",
    "paripūrakārino": "thực hành trọn vẹn", "kārino": "thực hành",
    "puggalo sīlesu paripūrakārī": "người thực hành trọn vẹn các giới hạnh",
    # ---- the line similes (^4-113 … ^4-115)
    "kujjhati": "nổi giận", "abhiṇhaṃ": "thường hay", "kodho": "sự giận dữ", "assa": "người ấy",
    "ciraṃ dīgharattaṃ": "lâu dài suốt một thời gian dài",   # comma dropped
    "khippaṃ": "mau", "lujjati": "bị xóa mờ", "vātena": "gió", "udakena": "nước", "ṭhitikā": "tồn tại",
    "upamo": "giống như", "vuccamāno": "bị nói", "pharusena": "thô ác", "amanāpena": "không dễ ưa",
    "saṃsandati": "hòa hợp", "sandhiyati": "gắn bó", "sammodati": "thân thiện", "ceva": NDE,   # «… ceva» bracket
    # ---- potthaka / kāsikavattha (^4-116, ^4-117)
    "potthakā": "vải gai thô", "vattha": "vải", "navo": "mới tu", "jiṇṇo": "đã cũ", "jiṇṇaṃ": "đã cũ",
    "dubbaṇṇo": "xấu xí", "dubbaṇṇatāya": "sự xấu xí", "vaṇṇavantaṃ": "đẹp", "suvaṇṇatāya": "sự đẹp đẽ",
    "samphasso": "tiếp xúc", "dukkhasamphassatāya": "sự khó chịu khi tiếp xúc",
    "sukhasamphassatāya": "sự dễ chịu khi tiếp xúc",
    "ukkhali": "nồi", "parimajjanaṃ": "giẻ lau", "saṅkāra": "rác", "kūṭe": "đống", "chaḍḍenti": "vứt",
    "ratana": "châu báu", "paliveṭhanaṃ": "gói", "gandha": "hương thơm", "karaṇḍake": "hộp", "nikkhipanti": "cất",
    "bhikkhūsu": "tỳ-khưu", "sevanti": "gần gũi", "bhajanti": "kết giao", "payirupāsanti": "thân cận",
    "diṭṭha": "gương", "anugatiṃ": "noi theo",                # diṭṭhānugatiṃ «noi theo gương»
    "dīgharattaṃ": "một thời gian dài", "ahitāya": "sự bất lợi", "hitāya": "sự lợi ích",
    "paṭiggaṇhāti": "nhận", "cīvara": "y phục", "parikkhāraṃ": "vật dụng", "ānisaṃsaṃ": "lợi ích",
    "thero": "trưởng lão", "saṅgha": "Tăng đoàn", "bhaṇati": "lên tiếng", "bālassa": "kẻ ngu dốt",
    "tathārūpiṃ": "loại",                                     # tathārūpiṃ vācaṃ «loại lời nói»
    "nicchāreti": "thốt ra", "ukkhipati": "trục xuất",
    "appasaddā": "giữ im lặng", "vacanaṃ": "lời nói", "ādheyyaṃ": "được ghi nhớ", "dhammaṃ": "Giáo Pháp",
    "kho": NDE, "pana": NDE,                                  # Ye kho panassa / Yesaṃ kho pana «Những ai …»: no word
    "sabbattha": "mọi bản", "sameti": "phù hợp", "ṭīkāya": "Phụ chú giải",   # bracket labels (ALLOWED)
    # ---- suppameyya / duppameyya (^4-118, ^4-119)
    "uddhato": "xao động", "unnaḷo": "kiêu căng", "capalo": "nhẹ dạ", "mukharo": "lắm lời",
    "vikiṇṇa": "tản mạn", "vāco": "ăn nói", "muṭṭhassati": "mất tỉnh thức", "vibbhanta": "rối loạn",
    "indriyo": "giác quan", "pākaṭa": "buông lỏng", "saṃvuta": "được thu thúc", "ekagga": "hợp nhất",
    "samāhito": "được định tâm",
    # ---- sevitabba … (^4-121 … ^4-126)
    "samādhinā paññāya": "định tâm và trí tuệ",              # «về giới hạnh, định tâm và trí tuệ»
    "hīno": "kém hơn", "sadiso": "ngang bằng", "adhiko": "hơn", "anuddayā": "lòng thương mến",
    "kathā": "cuộc trò chuyện", "pavattinī": "được tiếp diễn",
    "aparipūraṃ": "chưa đầy đủ", "paripūressāmi": "làm cho đầy đủ",
    "pāpamitto": "kết bạn với người xấu", "kalyāṇamitto": "kết bạn với người tốt",   # «Con người này kết bạn …»
    "sahāyo": "bạn đồng hành", "sampavaṅko": "nghiêng về phía", "kittisaddo": "tiếng", "abbhuggacchati": "lan truyền",
    "ahi": "con rắn", "ḍaṃsati": "cắn", "makkheti": "làm vấy bẩn",
    # ---- the teachers (^4-130, ^4-131)
    "satthā": "bậc đạo sư", "paññapeti": "đề ra", "satthā paññapeti": "bậc đạo sư đề ra",
    "pariññaṃ": "sự hiểu biết trọn vẹn", "pariññaṃ paññapeti": "đề ra sự hiểu biết trọn vẹn",
    "kāmānaṃ": "dục lạc", "rūpānaṃ": "hình sắc", "vedanānaṃ": "cảm giác",
    "kāmānaṃ pariññaṃ": "sự hiểu biết trọn vẹn về các dục lạc",   # inner «các» kept
    "rūpānaṃ pariññaṃ": "sự hiểu biết trọn vẹn về các hình sắc",
    "vedanānaṃ pariññaṃ": "sự hiểu biết trọn vẹn về các cảm giác",
    "samāpattiyā": "thành tựu thiền",                         # rūpāvacarasamāpattiyā lābhī «có được thành tựu thiền …»
    "sambuddho": "Tự Giác Ngộ", "sammāsambuddho": "Tự Giác Ngộ Hoàn Toàn",   # «bậc đạo sư Tự Giác Ngộ Hoàn Toàn»
    "attānaṃ": "tự ngã", "dhamme": "đời",                     # diṭṭhe dhamme «trong đời này»
    "sassatavādo": "theo học thuyết về sự trường tồn", "ucchedavādo": "theo học thuyết về sự đoạn diệt",
}

# per-segment choices (read from the segments)
OVERRIDES = {
    "4-91": {"hoti": "nghĩ"},                                 # Tassa (na) evaṃ hoti «Người ấy (không) nghĩ như vầy»
    "4-92": {"hoti": "nghĩ"},
    "4-93": {"hoti": "nghĩ"},
    "4-107": {"gato": NDE},                                   # only in the bracket [dị bản (Sī.): gato …] kept in Pāli
    "4-110": {"vītarāgo": "lìa tham đắm"},                    # avītarāgo «chưa lìa tham đắm» (fragment, positive part)
    "4-116": {"hoti": "đem lại",                              # tesaṃ taṃ hoti … «điều đó đem lại cho họ …»
              "bhikkhu": "tỳ-khưu",                           # «một tỳ-khưu dù mới tu»
              "majjhimo": "đã dùng một thời gian",            # majjhimopi potthako «vải … dù đã dùng một thời gian»
              "Majjhimo": "bậc trung",                        # Majjhimo cepi bhikkhu «một tỳ-khưu dù ở bậc trung»
              "majjhe": "giữa",                               # saṅghamajjhe «giữa Tăng đoàn»
              "gilāna": "bệnh",                               # gilānapaccayabhesajja «vật dụng chữa bệnh»
              "dukkha": "khó chịu",                           # dukkhasamphasso «khi tiếp xúc thì khó chịu»
              "dukkhāya": "khổ đau",                          # ahitāya dukkhāya «sự bất lợi và khổ đau»
              "nāma": "mà" + GAP + "sao"},                    # tvampi nāma … maññasī «ông mà cũng nghĩ … sao»
    "4-117": {"hoti": "đem lại", "bhikkhu": "tỳ-khưu",
              "majjhimaṃ": "đã dùng một thời gian", "Majjhimo": "bậc trung", "majjhe": "giữa",
              "gilāna": "bệnh",
              "sukha": "dễ chịu",                             # sukhasamphassaṃ «khi tiếp xúc thì dễ chịu»
              "sukhāya": "hạnh phúc"},                        # hitāya sukhāya «sự lợi ích và hạnh phúc»
    "4-118": {"sampajāno": "hiểu biết rõ ràng"},              # asampajāno «thiếu hiểu biết rõ ràng» (fragment)
    "4-119": {"sampajāno": "có hiểu biết rõ ràng"},           # «có hiểu biết rõ ràng»
}

# presence-check exceptions: (id, keyword) -> reason
_BR = "the word is in the translated label of a variant bracket, which present() strips (pi-3 ^3-112 precedent)"
ALLOWED = {("4-101", "aṭṭhakathā"): _BR, ("4-117", "sabbattha"): _BR,
           ("4-117", "sameti"): _BR, ("4-117", "ṭīkāya"): _BR}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value(kw, kws, T4, vi.get(bid, ""))
    return resolve


def show(lo, hi):
    res = resolver()
    vi, pi = read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            er = en_ru(bid)
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else "   <<MISS"
                e = er.get(kw, ["", ""])
                print(f"   {kw}={v}   [{e[0]} | {e[1]}]{flag}")


def dump(only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v == "???" or (v != NDE and not present(v, vi.get(bid, ""))):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        ps = []
        for i, f in ((1, pi1_map_values), (2, pi2_map_values), (3, pi3_map_values)):
            p = [x for x, _ in f(kw).most_common(2) if x != v]
            if p:
                ps.append(f"pi{i}:{p}")
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + ("  " + " ".join(ps) if ps else "")
              + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
