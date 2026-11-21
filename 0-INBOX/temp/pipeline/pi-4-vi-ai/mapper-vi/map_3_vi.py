"""Build the pi-4 (Puggalapaññatti) Pāli->Vietnamese keyword map for part 3-dukapuggalapannatti.

usage: python -I -X utf8 map_3_vi.py                     (writes 3-dukapuggalapannatti.mapped.md and verifies it)
       python -I -X utf8 map_3_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_3_vi.py show lo hi          (segments lo..hi with pairs; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order: OVERRIDES[bid][kw] -> T3 (this script's table) -> map_common_vi.value(): context4 -> PG -> pi-3 chain.
Conventions: pi-1 / pi-2 / pi-3 / pi-4 vi-map-conventions*.md (map_sample_vi.py is the model).
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, NDE, build_part, lc, present, value, verify)  # noqa: E402
import map_sample_vi as S  # noqa: E402  (read-only: dump / show helpers)

PART = "3-dukapuggalapannatti"

# part-specific values (the duka definitions ^4-45 … ^4-90, read from the segments)
T3 = {
    # ---- kodha / upanāha / makkha / issā / macchariya strings
    "byāpajjitattaṃ": "trạng thái khởi thù hằn",
    "doso": "sự sân hận", "moho": "sự si mê",                 # items of the strings «sự sân hận», «sự si mê» (pi-1)
    "ṭhapanā": "sự giữ lại", "saṇṭhapanā": "sự giữ chặt",
    "daḷhīkammaṃ": "sự làm cho" + GAP + "thêm vững chắc",   # «sự làm cho sự giận dữ thêm vững chắc»
    "niṭṭhuriya": "khắc nghiệt",                              # niṭṭhuriyakammaṃ «hành động khắc nghiệt»
    "issāyitattaṃ": "trạng thái khởi ganh tị", "usūyitattaṃ": "trạng thái khởi đố kỵ",
    "maccharāyitattaṃ": "trạng thái khởi keo kiệt",
    "vaṇṇa": "lời khen",                                      # vaṇṇamacchariyaṃ «keo kiệt về lời khen» (pi-1 / pi-2)
    "ṭhānaṃ": "nguyên cớ",                                   # vivādaṭṭhānaṃ «nguyên cớ tranh cãi»
    "āhāro": "sự ôm giữ",                                     # paḷāsāhāro «sự ôm giữ sự ganh đua»
    # ---- sāṭheyya / māyā
    "pari": "rất",                                            # parisaṭho «rất gian trá»
    "parikkhattattā": "sự quanh co",
    "paṭicchādana": "che giấu", "hetu": "vì muốn",            # paṭicchādanahetu «vì muốn che giấu điều đó»
    "uttānī": "bày tỏ", "āvi": "bộc lộ",                      # anuttānīkammaṃ / anāvikammaṃ «sự không bày tỏ / bộc lộ»
    "pāpakiriyā": "việc làm xấu ác",
    # ---- ahirika / anottappa / dovacassatā / pāpamittatā
    "samāpattiyā": "để" + GAP + "xảy ra nơi mình",          # pi-1 «nếu để các hiện tượng … xảy ra nơi mình»
    "saha": "đúng theo", "dhammike": "Giáo Pháp",             # Sahadhammike «đúng theo Giáo Pháp»
    "ādariyaṃ": "sự tôn trọng", "ādariyatā": "thái độ tôn trọng", "gāravatā": "sự kính trọng",
    "patissavatā": "sự vâng lời",
    "sambhatti": "sự gắn bó mật thiết",
    "sutā": "học hỏi",                                        # appassutā «ít học hỏi» / bahussutā «học hỏi nhiều»
    "sīlā": "giới",                                           # dussīlā «phạm giới»
    # ---- indriyesu (a)guttadvāratā / bhojane (a)mattaññutā
    "cakkhunā": "mắt", "rūpaṃ": "hình sắc", "saddaṃ": "âm thanh", "phusitvā": "chạm",
    "dhammaṃ": "đối tượng của ý",                             # «nhận biết đối tượng của ý bằng ý»
    "nimitta": "dấu hiệu tổng quát",                          # nimittaggāhī «nắm giữ dấu hiệu tổng quát»
    "āpajjati": "thực hiện",                                  # pi-1
    "aguttadvāratāya": "sự không phòng hộ cửa",
    "ññutā": "biết", "ayoniso": "không đúng cách",           # pi-1
    # datives without «để» (pi-4 sacchikiriyāya / pi-1 pahānāya; pi-2 map «vui đùa», «thu thúc»)
    "davāya": "vui đùa", "madāya": "say sưa", "maṇḍanāya": "trang điểm", "vibhūsanāya": "làm đẹp",
    "saṃvarāya": "thu thúc",
    "vihiṃsā": "sự bức bách",                                 # pi-1 vihiṃsūparatiyā «để chấm dứt sự bức bách»
    "brahma": "trong sạch", "cariya": "đời sống tu hành",    # brahmacariya «đời sống tu hành trong sạch»
    "purāṇaṃ": "cũ",                                          # purāṇañca vedanaṃ «cảm giác cũ»
    # ---- asampajañña (a-fragments = the positive Vietnamese)
    "ñāṇaṃ": "biết", "abhisamayo": "thấu hiểu", "paṭivedho": "thấu triệt",
    "saṅgāhaṇā": "nắm bắt", "pariyogāhaṇā": "đi sâu", "pekkhaṇā": "xem xét",
    "sama": NDE,                                              # asamapekkhaṇā «sự không xem xét»: no word for sama
    "paccavekkhaṇā": "xem xét lại", "paccakkha": "tự mình thấy rõ",
    # ---- diṭṭhivipatti / diṭṭhisampadā
    "gataṃ": "sự mắc kẹt trong",                              # diṭṭhigataṃ «sự mắc kẹt trong các quan điểm» (pi-2)
    "gāho": "sự nắm giữ", "ku": "lệch lạc",                   # kummaggo «con đường lệch lạc»
    "āyatanaṃ": "lĩnh vực",                                   # titthāyatanaṃ «lĩnh vực của các học thuyết ngoại đạo»
    "gatā": "đã đi", "sammāpaṭipannā": "thực hành đúng đắn",  # sammaggatā «đã đi đúng đắn»
    "abhiññā": "hiểu biết trực tiếp", "pavedenti": "tuyên bố",
    "hutaṃ": "sự cúng dường",                                 # «không có / có sự cúng dường»
    "sabbattha": "mọi bản", "pada": "từ", "siddhi": "cách cấu tạo", "cintetabbā": "cần xem xét",   # bracket label
    "vibha": "Phân tích các hiện tượng",                     # bracket «“Phân tích các hiện tượng” 891 / 893»
    "niddese": "phần giải thích", "evaṃ": "cũng vậy",        # bracket «cũng vậy trong phần giải thích …»
    # ---- saṃyojana, sīla / diṭṭhi sampadā
    "orambhāgiyāni saṃyojanāni": "xiềng xích thuộc phần thấp",
    "uddhambhāgiyāni saṃyojanāni": "xiềng xích thuộc phần cao",
    "sīlasampadā": "sự thành tựu về giới hạnh", "vuccati sīlasampadā": "được gọi là sự thành tựu về giới hạnh",
    "diṭṭhisampadā": "sự thành tựu về quan điểm",
    "vuccati diṭṭhisampadā": "được gọi là sự thành tựu về quan điểm",
    # ---- ^4-70 Pāli spelling «pugalo»
    "katamo pugalo": "thế nào là người", "pugalo": "người",
    # ---- ^4-83 … ^4-87
    "kata": "ơn", "kataññū": "biết ơn", "vedī": "đền",        # kataññū katavedī «biết ơn, đền ơn»
    "puggalā dullabhā": "hạng người" + GAP + "khó tìm gặp",  # «Hai hạng người nào khó tìm gặp»
    "laddhaṃ": "nhận được", "laddhaṃ laddhaṃ": "nhận được thứ gì",
    "nikkhipati": "cất giữ lại", "vissajjeti": "đem cho đi",
    "duttappayā": "khó làm cho thỏa mãn", "sutappayā": "dễ làm cho thỏa mãn",
    "kukkuccāyitabbaṃ": "đáng hối tiếc", "kukkuccāyati": "hối tiếc",
    # ---- ^4-88 … ^4-90
    "bhajati": "kết giao", "payirupāsati": "thân cận",       # «gần gũi, kết giao, thân cận»
    "puggalo dussīlo": "người phạm giới", "sīlavā": "giữ giới",
    "pāpadhammo": "có phẩm chất xấu", "kalyāṇadhammo": "có phẩm chất tốt",   # attribute, no head noun
    "arahanto": "A-la-hán",                                   # «những đệ tử A-la-hán của Như Lai»
    "sambuddhā": "bậc" + GAP + "Giác",                        # Paccekasambuddhā «Các bậc Độc Giác» (sample ^4-23)
}

# per-segment choices (read from the segments)
OVERRIDES = {
    # a- segments: the fragment of the a-name = the positive Vietnamese, no head noun (pi-1 / sample ^4-6)
    "4-54": {"ottappī": "biết ghê sợ tội lỗi"},              # anottappī «người không biết ghê sợ tội lỗi»
    "4-55": {"ādariyatā": "tôn trọng", "gāravatā": "kính trọng", "patissavatā": "vâng lời"},
    "4-57": {"gopanā": "bảo vệ", "ārakkho": "che chở"},      # agopanā / anārakkho «sự không …»
    "4-58": {"santuṭṭhitā": "biết đủ", "mattaññutā": "biết tiết độ"},
    "4-59": {"dhāraṇatā": "gìn giữ trong trí nhớ", "paṭissati": "hồi tưởng", "anussati": "nhớ lại",
             "saraṇatā": "ghi nhớ"},
    "4-60": {"sampajāno": "hiểu biết rõ ràng"},              # asampajāno «người thiếu hiểu biết rõ ràng»
    "4-65": {"kodhano": "giận dữ"},                           # akkodhano «người không giận dữ»
    "4-66": {"upanāhī": "ôm hận"},
    "4-67": {"makkhī": "gièm pha"},
    "4-68": {"paḷāsī": "ganh đua"},
    "4-69": {"issukī": "ganh tị"},
    "4-70": {"maccharī": "keo kiệt"},
    "4-71": {"saṭho": "gian trá"},                            # free word «có người gian trá» (no «người gian xảo»)
    "4-72": {"māyāvī": "xảo trá"},
    "4-75": {"sātatā": "thích thú", "gāhitā": "tiếp nhận"},  # avipaccanīkasātatā / avippaṭikulaggāhitā
    "4-79": {"sammusanatā": "quên lãng", "pilāpanatā": "hời hợt"},
    "4-81": {"vītikkamo": "vi phạm"},                         # avītikkamo «sự không vi phạm»
}

# presence-check exceptions: (id, keyword) -> reason
_BR = "the word is in the translated label of a variant bracket, which present() strips (pi-3 ^3-112 precedent)"
ALLOWED = {(b, k): _BR for b, k in (
    ("4-46", "vibha"), ("4-49", "vibha"),
    ("4-51", "niddese"), ("4-51", "duka"), ("4-51", "evaṃ"),
    ("4-62", "sabbattha"), ("4-62", "pada"), ("4-62", "siddhi"), ("4-62", "cintetabbā"))}


def context(bid, kw, kws, text):
    """segment rules of this part (None = no rule)."""
    k = lc(kw)
    s = set(lc(x) for x in kws)
    if k in ("pahīno", "pahīnā", "pahīnaṃ", "pahīnāni"):   # «chưa được dứt bỏ» (appahīn-) / «đã được dứt bỏ»
        return "đã được dứt bỏ" if present("đã được dứt bỏ", text) else "được dứt bỏ"
    if k == "sammā" and "sammāsambuddho" not in s:          # sammāsati / sammādiṭṭhi / sammaggatā «đúng đắn»
        return "đúng đắn"
    if k == "kammaṃ":                                         # niṭṭhuriyakammaṃ «hành động khắc nghiệt»; anuttānī- /
        return "hành động" if "niṭṭhuriya" in s else NDE      # anāvi- / apaccakkhakammaṃ «sự không …»: no word
    if k == "pāpa" and "pāpadhammo" in s:                     # «có phẩm chất xấu» (pāpamitto «người xấu»)
        return "xấu"
    if k == "duka" and bid == "4-51":                         # bracket «phần giải thích phân loại theo nhóm hai»
        return "phân loại theo nhóm hai"
    if k == "vuccati" and bid == "4-90":                      # only inside the bracket kept in Pāli
        return NDE
    return None


def resolver_for(part=PART):
    vi = S.read_vietnamese(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        t = vi.get(bid, "")
        v = context(bid, kw, kws, t)
        if v is not None:
            return v
        return value(kw, kws, T3, t)
    return resolve


if __name__ == "__main__":
    S.resolver_for = lambda part: resolver_for(part)
    if sys.argv[1:2] == ["dump"]:
        S.dump(PART, sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        S.show(PART, int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1:2] == ["look"]:
        S.look(sys.argv[2:])
    else:
        build_part(PART, resolver_for(PART))
        verify(PART, ALLOWED)
