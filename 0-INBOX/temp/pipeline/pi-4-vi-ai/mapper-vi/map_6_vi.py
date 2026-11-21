"""Build the pi-4 (Puggalapaññatti) Pāli->Vietnamese keyword map for part 6-pancakapuggalapannatti.

usage: python -I -X utf8 map_6_vi.py                     (writes 6-pancakapuggalapannatti.mapped.md and verifies it)
       python -I -X utf8 map_6_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_6_vi.py show lo hi          (segments lo..hi with pairs; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order: OVERRIDES[bid][kw] -> context() -> T6 (this script's table) -> map_common_vi.value():
context4 -> PG -> pi-3 chain.
Conventions: pi-1 / pi-2 / pi-3 / pi-4 vi-map-conventions*.md (map_sample_vi.py is the model; map_3_vi.py followed).
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, NDE, build_part, lc, present, value, verify)  # noqa: E402
import map_sample_vi as S  # noqa: E402  (read-only: dump / show helpers)

# map_3_vi.T3 shares four keywords with this part (brahma, vaṇṇa, bhajati, gataṃ); brahma = trong sạch is taken
# over, the other three have a different sense here and are set in T6.
PART = "6-pancakapuggalapannatti"

# part-specific values (the pañcaka definitions ^4-191 … ^4-201, read from the segments)
T6 = {
    # ---- ^4-191 ārabhati / vippaṭisārī
    "jā": "sinh từ",                                          # ārambhajā / vippaṭisārajā «sinh từ …»
    "ārambha": "việc phạm lỗi", "ārambhajā": "sinh từ việc phạm lỗi",
    "vippaṭisārajā": "sinh từ sự ăn năn",
    "ārambhajā āsavā": "ô nhiễm sinh từ việc phạm lỗi",
    "āyasmato": "tôn giả", "assa": "người ấy",               # yatthassa «nơi người ấy»
    "saṃvijjanti": "có",                                      # «Nơi tôn giả, có các ô nhiễm …» (the verb's only word)
    "pavaḍḍhanti": "tăng trưởng", "paṭivinodetvā": "xua tan", "bhāvetu": "tu tập",
    "cittaṃ paññaṃ": "tâm và trí tuệ",                        # cittaṃ paññañca «tâm và trí tuệ»
    "pañcamena": "thứ năm", "samasamo": "hoàn toàn ngang bằng",
    "ovadiyamānā": "được" + GAP + "khuyên bảo",              # «khi được người thứ năm kia khuyên bảo …, chỉ dạy …»
    "anusāsiyamānā": "chỉ dạy", "anupubbena": "dần dần", "pāpuṇanti": "đạt đến",
    # ---- ^4-192 the single persons
    "puggalo datvā": "người cho", "deti": "cho", "puggalo deti": "người cho",
    "puggalo deti cīvara": "người cho" + GAP + "y phục",    # «có người cho ai đó y phục …»
    "cīvara": "y phục", "gilāna": "chữa bệnh", "parikkhāraṃ": "vật dụng",   # «thuốc men và vật dụng chữa bệnh» (pi-2)
    "evaṃ hoti": "nghĩ như vầy", "paṭiggaṇhāti": "nhận",
    "saṃvasati": "sống chung", "puggalo saṃvasati": "người sống chung", "saddhiṃ": "với",
    "parassa": "người khác", "vaṇṇe": "lời khen", "avaṇṇe": "lời chê", "adhimuccitā": "tin ngay",
    "ittara": "chóng qua", "saddho": "có niềm tin", "bhattī": "lòng sùng kính", "pemo": "lòng quý mến",
    "puggalo lolo": "người không kiên định", "puggalo mando": "người chậm hiểu",
    "akusale dhamme": "hiện tượng" + GAP + "bất thiện",     # «các hiện tượng thiện và bất thiện»
    "sāvajja": "có lỗi", "anavajje": "không có lỗi", "anavajje dhamme": "hiện tượng" + GAP + "không có lỗi",
    "hīna": "thấp kém", "kaṇha": "đen tối", "sukka": "trong sáng",
    "paṭibhāge": "đối lập với chúng",                         # sappaṭibhāge «cùng với những gì đối lập với chúng»
    "pana": NDE,                                              # only inside the bracket [ayaṃ pana (syā. ka.)]
    # ---- ^4-193 … ^4-198 the warrior simile
    "puna": "lại nữa",                                        # Puna caparaṃ «Lại nữa»
    "yodhājīvo": "chiến binh", "yodhājīvo sahati": "chiến binh chịu được",
    "sahati": "chịu được", "bhikkhu sahati": "vị tỳ-khưu chịu được",
    "rajaggaṃ": "đám bụi mù", "raja": "bụi mù", "dhaja": "ngọn cờ",
    "sahati rajaggaṃ": "chịu được đám bụi mù", "sahati dhajaggaṃ": "chịu được ngọn cờ",
    "ussāraṇaṃ": "tiếng hò hét", "sahati ussāraṇaṃ": "chịu được tiếng hò hét",
    "sampahāraṃ": "cuộc giáp chiến", "sampahāre": "cuộc giáp chiến", "sahati sampahāraṃ": "chịu được cuộc giáp chiến",
    "saṃsīdati": "chùn bước", "visīdati": "nản lòng", "santhambhati": "đứng vững",
    "satthambhati": NDE, "uhasati": NDE,                      # only inside a variant bracket kept in Pāli
    "saṅgāmaṃ": "trận chiến", "haññati": "bị đánh trúng", "byāpajjati": "bị thương",
    "abhivijinitvā": "chiến thắng", "vijitasaṅgāmo": "người đã thắng trận",
    "sīsaṃ": "chiến địa", "ajjhāvasati": "làm chủ",           # tameva saṅgāmasīsaṃ ajjhāvasati «làm chủ chính chiến địa ấy»
    "saṃvijjamāno": "được tìm thấy", "saṃvijjamānā": "được tìm thấy",   # santo saṃvijjamāno «đang có mặt, được tìm thấy»
    "upamo": "giống như", "bhikkhūsu": "tỳ-khưu",            # «giữa các tỳ-khưu» (locative frame dropped)
    "catuttho puggalo": "người thứ tư",
    "brahma": "trong sạch",                                   # ch3 T3 brahma (not PG «cao thượng» of brahmabhūta)
    "brahmacariyaṃ": "đời sống tu hành trong sạch", "cariyaṃ": "đời sống tu hành",   # ch3 cariya
    "sandhāretuṃ": "duy trì",
    "sikkhā": "sự tu học", "sikkhaṃ": "sự tu học", "dubbalyaṃ": "sự yếu kém",
    "āvikatvā": "bày tỏ", "dubbalyaṃ āvikatvā": "bày tỏ sự yếu kém",
    "paccakkhāya": "từ bỏ", "hīnāya": "đời sống thấp kém", "āvattati": "quay về",
    "sikkhaṃ āvattati": "sự tu học và quay về",              # sikkhaṃ paccakkhāya hīnāyāvattati «từ bỏ sự tu học và quay về»
    "suṇāti": "nghe", "asukasmiṃ": "như thế kia", "gāme": "làng", "nigame": "thị trấn",
    "itthī": "người nữ", "kumārī": "thiếu nữ", "abhirūpā": "đẹp đẽ", "dassanīyā": "dễ nhìn", "pāsādikā": "đáng mến",
    "paramāya": "tuyệt vời", "vaṇṇa": "dung mạo",            # vaṇṇapokkharatāya «vẻ đẹp dung mạo»
    "samannāgatā": "được trang bị", "sāmaṃ": "chính mình",
    "mātugāmo": "phụ nữ", "upasaṅkamitvā": "đến gần", "gataṃ": "đi đến",   # araññagataṃ «đi đến rừng»
    "suñña": "trống",                                         # suññāgāra «ngôi nhà trống»
    "ūhasati": "cười cợt", "ūhasiyamāno": "bị" + GAP + "cười cợt",   # «khi bị phụ nữ cười cợt, tán tỉnh, …»
    "ullapati": "tán tỉnh", "ullapiyamāno": "tán tỉnh",
    "ujjagghati": "cười đùa ầm ĩ", "ujjagghiyamāno": "cười đùa ầm ĩ",
    "uppaṇḍeti": "trêu ghẹo", "uppaṇḍiyamāno": "trêu ghẹo",
    "aṭṭhakathā": "Chú giải",                                 # bracket label «[khác chính tả (Chú giải): uhasati …]»
    "abhinisīdati": "ngồi sát bên", "abhinipajjati": "nằm sát bên", "ajjhottharati": "đè lên",
    "methunaṃ": "dâm", "paṭisevati": "hành",                  # methunaṃ dhammaṃ paṭisevati «hành dâm»
    # ---- ^4-198 the victory: seclusion, hindrances, jhāna, the destruction of the āsavas
    "vijayasmiṃ": "sự chiến thắng", "viniveṭhetvā": "gỡ mình ra", "vinimocetvā": "thoát ra",
    "yena": "nơi", "kāmaṃ": "mình muốn",                     # yena kāmaṃ «đến nơi mình muốn»
    "bhajati": "lui tới",                                     # vivittaṃ senāsanaṃ bhajati «lui tới chỗ ở thanh vắng»
    "giri": "núi", "vana": "rừng",                            # giriguhaṃ «hang núi», vanapatthaṃ «rừng sâu»
    "viharati": "sống",                                       # «vị ấy sống với tâm …» (5×); jhāna «an trú» (2×)
    "vigatathinamiddho viharati": "sống đã lìa sự uể oải và đờ đẫn",
    "satiṃ": "sự tỉnh thức", "sato": "tỉnh thức", "sampajāno": "hiểu biết rõ ràng",
    "anukampī": "thương xót", "hita": "điều lợi ích",        # pi-1 hita
    "uddhato": "xao động",                                    # anuddhato «không xao động» (positive part)
    "kathaṃkathī": "băn khoăn",                               # akathaṃkathī «không còn băn khoăn»
    "jaṃ": "sinh từ",                                         # vivekajaṃ «sinh từ sự tách biệt»
    "sukhaṃ": "hạnh phúc",                                    # pītisukhaṃ «sự hân hoan và hạnh phúc» (pi-1 factor)
    "samāhite": "đã an định", "samāhite citte": "tâm đã an định",
    "parisuddhe": "trong sạch", "pariyodāte": "trong sáng", "anaṅgaṇe": "không còn vết nhơ",
    "mudubhūte": "trở nên mềm dẻo", "kammaniye": "dễ vận dụng", "ṭhite": "vững vàng",
    "āneñja": "sự bất động",                                  # āneñjappatte «đạt đến sự bất động»
    "ñāṇāya": "sự hiểu biết", "abhininnāmeti": "dẫn" + GAP + "đến",   # «dẫn tâm đến sự hiểu biết …»
    "dukkhaṃ": "khổ đau",                                     # «Đây là khổ đau»
    "bhava": "hiện hữu",                                      # bhavāsava «ô nhiễm hiện hữu» (pi-1)
    "jānato": "biết", "vimuccati": "được giải thoát",
    "vusitaṃ": "đã được sống trọn", "kataṃ": "đã được làm xong", "nāparaṃ": "không còn gì khác",
    # ---- ^4-199 … ^4-201 the five piṇḍapātikā / sosānikā
    "mandattā": "chậm hiểu", "momūhattā": "mê muội",        # «vì chậm hiểu, vì mê muội» (causal «vì» = case frame)
    "pāpa": "xấu xa", "iccho": "ước muốn", "icchā": "ước muốn",   # pāpiccho icchāpakato «có ước muốn xấu xa, bị ước
    "ummādā": "điên loạn", "vikkhepā": "tán loạn",          # muốn chi phối»; ummādā cittavikkhepā «vì điên loạn,
    "vaṇṇitaṃ": "được" + GAP + "khen ngợi",                  # vì tâm tán loạn»
    "buddhehi": "chư Phật",                                   # «Được chư Phật và các đệ tử của chư Phật khen ngợi»
    "appa": "ít", "santuṭṭhiṃ": "sự biết đủ", "sallekhaṃ": "sự giảm trừ phiền não",
    "santuṭṭhiṃ nissāya": "dựa vào sự biết đủ", "sallekhaṃ nissāya": "dựa vào sự giảm trừ phiền não",
    "eva piṇḍapātiko": "chỉ" + GAP + "chỉ ăn thức ăn khất thực",   # «chỉ dựa vào … mà chỉ ăn thức ăn khất thực»
    "eva sosāniko": "chỉ" + GAP + "sống ở bãi tha ma",            # «chỉ dựa vào … mà sống ở bãi tha ma»
    "aggo": "đứng đầu", "seṭṭho": "cao quý nhất", "uttamo": "tối thượng", "pavaro": "ưu tú nhất",
    "mokkho": NDE,                                            # only inside the bracket [mokkho (sī.)] (sample paccekabuddho)
    "gavā": "bò", "maṇḍo": "phần tinh túy",                  # sappimaṇḍo «phần tinh túy của bơ lỏng»
    "yathā": "bất cứ" + GAP + "nào",                          # yathāsanthatikā «ở bất cứ chỗ nào được chỉ định»
}

# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
_BR = "the word is in the translated label of a variant bracket, which present() strips (pi-3 ^3-112 precedent)"
ALLOWED = {("4-196", "aṭṭhakathā"): _BR}


def context(bid, kw, kws, text):
    """segment rules of this part (None = no rule)."""
    k = lc(kw)
    s = set(lc(x) for x in kws)
    if k == "aggaṃ":                                          # dhajaggaṃ «ngọn cờ» / rajaggaṃ «đám bụi mù»
        return "ngọn" if "dhaja" in s and present("ngọn cờ", text) else "đám"
    if k == "yodhājīvo sahati":                               # «có chiến binh chịu được» / simile «Như chiến binh ấy
        v = "chiến binh chịu được"                            # chịu được»
        return v if present(v, text) else "chiến binh" + GAP + "chịu được"
    if k == "eva":                                          # rajaggaññeva «chỉ vừa thấy», …ṃyeva nissāya «chỉ dựa
        for v in ("chỉ vừa", "chỉ dựa vào"):                  # vào», vivicceva «hoàn toàn tách khỏi» (pi-1)
            if present(v, text):
                return v.replace(" dựa vào", "")
        return "hoàn toàn"
    return None


def resolver_for(part=PART):
    vi = S.read_vietnamese(part)
    table = T6

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        t = vi.get(bid, "")
        v = context(bid, kw, kws, t)
        if v is not None:
            return v
        return value(kw, kws, table, t)
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
