# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Vietnamese plain zero-shot: chapter 17 (Khuddakavatthuvibhaṅga).

usage: python -I -X utf8 build_17_vi.py [--dry]
Writes AI_translation\\vietnamese\\pi-2-vietnamese-plain-zeroshot_split_chapters\\17-khuddakavatthuvibhango.md (only when
run as a script without --dry; importing writes nothing).

Imports build_16_vi (Z) and through it S, B, T, F, G, H, X, Y; nothing of theirs is changed. pi-1 strings (lobha, dosa,
moha, the āsava / saṃyojana / upādāna / nīvaraṇa definitions, sakkāyadiṭṭhi, vicikicchā, sīlabbataparāmāsa, māna, issā,
macchariya, thina, uddhacca, ahirika, anottappa, the 4-03 dukas, the ten views, the ten kilesavatthu, the vedanā
strings, the jhāna and formless openings) are copied from the pi-1 Vietnamese rails at build time and asserted; ch3 /
ch4 / ch12 / ch14 / ch16 strings are asserted in their outputs. Every non-empty Pāli line is matched in order against a
key (heading: exact text; other lines: start of the line), so a missing or extra line stops the build.
"""
import importlib
import os
import re
import sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai"
sys.path.insert(0, HERE)
Z = importlib.import_module("build_16_vi")
S, G = Z.S, Z.G

DASH = S.DASH
cap, low = S.cap, S.low
between, in_out, pi1_pair = Z.between, Z.in_out, Z.pi1_pair
FN = "17-khuddakavatthuvibhango.md"
SLIPS = []


def nest(s):
    """“…” inside a quotation -> ‘…’"""
    return s.replace("“", "‘").replace("”", "’")


def called(x, cap_=False):
    v = f"đó được gọi là “{nest(x)}”"
    return cap(v) if cap_ else v


def q(x, lower=False):
    v = f"Ở đây, {x} là gì?"
    return low(v) if lower else v


def pv(fn, start):
    """pi-1 Vietnamese line (block ID removed) whose Pāli starts with start"""
    return pi1_pair(fn, start)[1]


F401, F402, F403 = "4-01-nikkhepakandam.md", "4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"
F201, F204 = "2-01-cittuppadakandam.md", "2-04-cittuppadakandam.md"


def body(fn, start, a="là gì? ", b=" – đó được gọi là"):
    return between(pv(fn, start), a, b)


# ================================================================ 1. pi-1 strings (asserted)
LOBHA_PI1 = body(F401, "Tattha katamo lobho?")                                   # ^1-1065
DOSA_PI1 = body(F401, "Tattha katamo doso?")                                     # ^1-1066
MOHA_PI1 = body(F402, "Tattha katamo moho?")                                     # ^1-1238
KAMASAVA = body(F401, "Tattha katamo kāmāsavo?")                                 # ^1-1103
BHAVASAVA = body(F401, "Tattha katamo bhavāsavo?").replace(" [khác chính tả (Sī., Syā.): bhavacchando]", "")
DITTHASAVA = pv(F401, "Tattha katamo diṭṭhāsavo?")                               # ^1-1105
SAKKAYA = body(F402, "Tattha katamā sakkāyadiṭṭhi? Idha assutavā puthujjano ariyānaṃ adassāvī ariyadhammassa "
               "akovido ariyadhamme avinīto sappurisānaṃ adassāvī sappurisadhammassa akovido sappurisadhamme "
               "avinīto rūpaṃ attato samanupassati, rūpavantaṃ vā attānaṃ, attani vā rūpaṃ, rūpasmiṃ vā attānaṃ. "
               "Vedanaṃ…pe…")                                                   # ^1-1262
VICI = body(F401, "Tattha katamā vicikicchā?")                                   # ^1-1008
SILABBATA = body(F402, "Tattha katamo sīlabbataparāmāso? Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi vatena")
MANA = body(F402, "Tattha katamo māno?")                                         # ^1-1239
ISSA = body(F401, "Tattha katamaṃ issāsaṃyojanaṃ?")                              # ^1-1126
MACCH = body(F401, "Tattha katamaṃ macchariyasaṃyojanaṃ?")                       # ^1-1127
THINA = body(F402, "Tattha katamaṃ thinaṃ?")                                     # ^1-1162
UDDH = body(F402, "Tattha katamaṃ uddhaccaṃ?")                                   # ^1-1165
AHIRI = body(F403, "Tattha katamaṃ ahirikaṃ?")                                   # ^1-1328
ANOTT = body(F403, "Tattha katamaṃ anottappaṃ?")                                 # ^1-1329
DOVAC = body(F403, "Tattha katamā dovacassatā?")                                 # ^1-1332
PAPAM = body(F403, "Tattha katamā pāpamittatā?")                                 # ^1-1333
INDRI = body(F403, "Tattha katamā indriyesu aguttadvāratā?")                     # ^1-1352
BHOJ = body(F403, "Tattha katamā bhojane amattaññutā?")                          # ^1-1353
MUTTH = body(F403, "Tattha katamaṃ muṭṭhasaccaṃ?")                               # ^1-1356
ASAMP = body(F403, "Tattha katamaṃ asampajaññaṃ?")                               # ^1-1357
SILAVIP = body(F403, "Tattha katamā sīlavipatti?", b=" – đó được gọi là")        # ^1-1368
NATTHI = between(pv(F403, "Tattha katamā diṭṭhivipatti?"), "là gì? ", "; điều mà")   # “Không có sự bố thí …” ^1-1369
NATTHI_V = between(pv(F402, "Tattha katamaṃ diṭṭhupādānaṃ?"), "là gì? ", " – điều mà")  # with [dị bản (Ka.): samaggatā]
DITTHUP_TAIL = pv(F402, "Tattha katamaṃ diṭṭhupādānaṃ?").split("sự bám víu vào quan điểm. ")[-1]
KAMUP = body(F402, "Tattha katamaṃ kāmupādānaṃ?")                                # ^1-1220
SILUP = between(pv(F402, "Tattha katamaṃ sīlabbatupādānaṃ?"), "là gì? ", " – điều mà")   # ^1-1222
SAMYO10 = between(pv(F401, "Katame dhammā saṃyojanā? Dasa saṃyojanāni"), "Mười xiềng xích " + DASH + " ", ".")
NIVA6 = between(pv(F402, "Katame dhammā nīvaraṇā? Cha nīvaraṇā [nīvaraṇāni"), "[dị bản (Syā.): nīvaraṇāni] " + DASH + " ",
                ".")
SOMA = between(pv(F201, "Katamaṃ tasmiṃ samaye sukhaṃ hoti?"), "vào lúc ấy là ", " – đó là")      # ^1-10
DOMA = between(pv(F204, "Katamaṃ tasmiṃ samaye dukkhaṃ hoti?"), "vào lúc ấy là ", " – đó là")      # ^1-416
UPEK = between(pv(F201, "Katamā tasmiṃ samaye upekkhā hoti? Yaṃ tasmiṃ samaye cetasikaṃ neva"), "vào lúc ấy là ",
               " – đó là")                                                      # ^1-153
SANNA = between(pv(F201, "Katamo tasmiṃ samaye saññākkhandho hoti?"), "vào lúc ấy là ", " – đó là")  # ^1-61
DIT = {k: pv(F403, f"Tattha katamā {k}?") for k in ("bhavadiṭṭhi", "vibhavadiṭṭhi", "sassatadiṭṭhi", "ucchedadiṭṭhi",
                                                     "antavā diṭṭhi", "anantavā diṭṭhi", "pubbantānudiṭṭhi",
                                                     "aparantānudiṭṭhi")}       # ^1-1320 … ^1-1327
VIEWS10, KILESA10 = Z.VIEWS10, Z.KILESA10
DITTHI_PE = "điều mà thuộc loại như vậy là quan điểm, sự mắc kẹt trong các quan điểm… sự nắm giữ điều đảo ngược"
AVIJJA_PE = "Điều mà là sự không biết, sự không thấy… then cài vô minh, sự si mê, tức gốc rễ bất thiện"

for _s in (LOBHA_PI1, DOSA_PI1, MOHA_PI1, KAMASAVA, BHAVASAVA, DITTHASAVA, SAKKAYA, VICI, SILABBATA, MANA, ISSA, MACCH,
           THINA, UDDH, AHIRI, ANOTT, DOVAC, PAPAM, INDRI, BHOJ, MUTTH, ASAMP, SILAVIP, NATTHI, NATTHI_V, KAMUP, SILUP,
           SAMYO10, NIVA6, SOMA, DOMA, UPEK, SANNA):
    assert _s and "  " not in _s, _s[:80]
assert ASAMP == AVIJJA_PE, ASAMP
assert DITTHI_PE in pv(F403, "Tattha katamā bhavadiṭṭhi?")
assert SAMYO10.startswith("xiềng xích tham đắm dục lạc") and SAMYO10.endswith("xiềng xích vô minh"), SAMYO10
assert NIVA6.endswith(", chướng ngại vô minh"), NIVA6
NIVA5 = NIVA6[:-len(", chướng ngại vô minh")]
assert MANA.startswith("Sự kiêu mạn “Tôi hơn người”, sự kiêu mạn “Tôi bằng người”, sự kiêu mạn “Tôi kém người”; "
                       "điều mà thuộc loại như vậy là "), MANA
MANA_SYN = MANA.split("điều mà thuộc loại như vậy là ")[1]                       # sự kiêu mạn, sự tự đánh giá mình, …
assert MANA_SYN.endswith("sự mong muốn được giương cờ của tâm"), MANA_SYN
MANA_SYN_PE = "sự kiêu mạn, sự tự đánh giá mình, trạng thái tự đánh giá mình… sự mong muốn được giương cờ của tâm"
assert MANA_SYN.startswith("sự kiêu mạn, sự tự đánh giá mình, trạng thái tự đánh giá mình, ")
VAR_UNNATI = " [khác chính tả (Syā., Ka.): uṇṇati uṇṇāmo; dha. sa. 1121]"
assert "sự vênh vang, ngọn cờ" in MANA_SYN
MANA_SYN_V = MANA_SYN.replace("sự vênh vang, ", "sự vênh vang" + VAR_UNNATI + ", ")
MANA3 = ["sự kiêu mạn “Tôi hơn người”", "sự kiêu mạn “Tôi bằng người”", "sự kiêu mạn “Tôi kém người”"]   # [pi-1 ^1-1239]
THINA_BODY = THINA                                                              # Điều mà là sự không khỏe khoắn của tâm …
assert THINA_BODY.startswith("Điều mà là sự không khỏe khoắn của tâm") and THINA_BODY.endswith("của tâm"), THINA_BODY
# the dosa definition: the āghāta sentences and the synonym list [pi-1 ^1-1066]
DOSA_HEAD, DOSA_SYN = DOSA_PI1.split(" Điều mà thuộc loại như vậy là ")
assert DOSA_HEAD.endswith("hoặc sự oán giận khởi lên một cách vô cớ."), DOSA_HEAD
KODHA_SYN = DOSA_SYN[DOSA_SYN.index("sự giận dữ, sự khởi giận"):]                # kodho … anattamanatā cittassa
assert KODHA_SYN.endswith("sự hung dữ, sự nói năng cộc cằn, sự không hài lòng của tâm"), KODHA_SYN
AGHATA9 = DOSA_HEAD[:-len(", hoặc sự oán giận khởi lên một cách vô cớ.")].replace("”, sự oán giận", "”; sự oán giận")
AGHATA10 = DOSA_HEAD[:-1]
# lobha: the pi-2 list differs from pi-1 in a few words (variants, sotaṃ, jappā …, order saddataṃhā rūpataṇhā)
_L = LOBHA_PI1
for _a, _b in ((" [khác chính tả (Sī.): nandirāgo]", ""), (" [khác chính tả (Sī.): sibbanī]", ""),
               (" [khác chính tả (Sī., Syā.): āyūhanī]", ""),
               (" [khác chính tả (Syā.): puñcikatā; (Sī.): pucchikatā]", ""),
               ("sợi chỉ, sự lan tràn", "dòng nước, sự lan tràn [khác chính tả (Sī., Ka.): visadā; dha. sa. 1141]"),
               ("kẻ thúc đẩy", "kẻ thúc đẩy [khác chính tả (Ka.): āyūhinī]"),
               ("sự thân thiết, sự luyến ái", "sự thân thiết [khác chính tả (Ka.): sandhavo], sự luyến ái"),
               ("sự thèm thuồng, sự thèm thuồng mãnh liệt, sự thèm thuồng tột độ, sự thèm thuồng, sự khởi thèm thuồng, "
                "trạng thái khởi thèm thuồng", "sự thèm thuồng, sự thèm thuồng tột độ, sự khởi thèm thuồng, "
                "trạng thái khởi thèm thuồng"),
               ("khao khát hình sắc, khao khát âm thanh, khao khát mùi", "khao khát âm thanh, khao khát hình sắc, "
                "khao khát mùi")):
    assert _L.count(_a) == 1, _a
    _L = _L.replace(_a, _b)
LOBHA = _L
assert "[khác chính tả (Sī., Syā.): āsiṃsanā āsiṃsitattaṃ]" in LOBHA and LOBHA.count("[") == 4, LOBHA
# moha: opening sentence of pi-1 ^1-1238 + the abbreviated list
MOHA_OPEN = MOHA_PI1.split(". Điều mà thuộc loại như vậy là ")[0]
assert MOHA_OPEN.startswith("Sự không biết về khổ đau") and MOHA_OPEN.endswith("tùy thuộc vào điều kiện"), MOHA_OPEN
MOHA_PE = "sự không biết, sự không thấy… then cài vô minh, sự si mê, tức gốc rễ bất thiện"
# the four-truth / dependent-origination list ends: avijjāsava full (pi-1 4-01) equals moha (4-02) in Vietnamese
AVIJJASAVA_FULL = MOHA_PI1
# sakkāyadiṭṭhi with the pi-2 dash before "rūpaṃ attato samanupassati"
assert SAKKAYA.count("chân chính, xem vật chất") == 1
SAKKAYA_D = SAKKAYA.replace("chân chính, xem vật chất", "chân chính " + DASH + " xem vật chất")
assert SAKKAYA_D.endswith(cap(DITTHI_PE)), SAKKAYA_D[-120:]
VICI_OPEN = VICI.split(". Điều mà thuộc loại như vậy là ")[0] + "."
VICI_SHORT = ("Điều mà thuộc loại như vậy là sự nghi ngờ, sự khởi nghi ngờ, trạng thái khởi nghi ngờ, trạng thái cứng đờ "
              "của tâm, sự giằng xé của ý")                                     # ch12 ^2-560 words
in_out("12-jhanavibhango.md", "là sự nghi ngờ, sự khởi nghi ngờ, trạng thái khởi nghi ngờ, trạng thái cứng đờ của tâm, "
                              "sự giằng xé của ý")
SILABBATA_Q = SILABBATA.split(" " + DASH + " điều mà")[0]                       # Các sa-môn … nghi thức”
assert SILABBATA_Q.endswith("trong sạch nhờ giới hạnh và nghi thức”"), SILABBATA_Q
assert SILUP.split(" " + DASH)[0] == SILABBATA_Q or SILUP == SILABBATA_Q, SILUP
MACCH_V = MACCH.replace("trạng thái khép chặt của tâm",
                        "trạng thái khép chặt [dị bản (Sī., Ka.): paggahitattaṃ; dha. sa. 1127] của tâm")
assert MACCH_V != MACCH
MACCH5 = between(MACCH, "Năm loại keo kiệt " + DASH + " ", ".")
INDRI_ASAMVARA = INDRI.split(" Điều mà là sự không canh giữ")[0]
assert INDRI_ASAMVARA.endswith("không thực hiện sự thu thúc nơi năng lực ý."), INDRI_ASAMVARA
VITIKKAMA = SILAVIP.replace("Điều mà là sự vi phạm", "Sự vi phạm")
assert VITIKKAMA == "Sự vi phạm bằng thân, sự vi phạm bằng lời nói, sự vi phạm bằng thân và lời nói", VITIKKAMA
in_out("12-jhanavibhango.md", VITIKKAMA)
DITTHUP_TAIL = DITTHUP_TAIL.split(" ^")[0]
assert DITTHUP_TAIL.startswith("Ngoại trừ sự bám víu vào giới hạnh"), DITTHUP_TAIL
SANNA_SYN = SANNA.replace("Điều mà vào lúc ấy là ", "")
assert SANNA == "tri giác, sự nhận ra, trạng thái đã nhận ra", SANNA
DIT_Q = {}
for _k, _v in DIT.items():
    _v = _v.split(" ^")[0]
    DIT_Q[_k] = (between(_v, "Ở đây, ", " là gì?"),
                 between(_v, "là gì? ", "; điều mà" if "; điều mà" in _v else " – đó được gọi là"))
# “Tự ngã và thế gian sẽ tồn tại” …

# ---------------------------------------------------------------- earlier pi-2 chapters (asserted in their outputs)
VIHESA_BODY = ("Ở đời này, có người quấy hại chúng sinh bằng tay, bằng cục đất, bằng gậy, bằng vũ khí, bằng dây thừng "
               "hoặc bằng thứ này hay thứ khác, điều mà thuộc loại như vậy là sự quấy hại, sự quấy hại nặng nề, sự làm "
               "hại, sự hãm hại, sự làm khổ, sự làm khổ nặng nề, sự gây hại cho người khác")      # [ch3]
in_out("3-dhatuvibhango.md", VIHESA_BODY)
TAKKA = "sự hướng tâm, tư duy sai lầm"          # takko vitakko micchāsaṅkappo: «Suy nghĩ …, sự hướng tâm, … tư duy sai lầm»
in_out("3-dhatuvibhango.md", "Suy nghĩ liên quan đến dục lạc, sự hướng tâm, tư duy, sự gắn tâm")
SURA = "việc dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả"      # [ch14]
in_out("14-sikkhapadavibhango.md", SURA)
LAPA3 = "lời nịnh bợ, lời nửa thật nửa giả, việc chăm bẵm con trẻ"            # cāṭukamyatā … [ch12 ^2-512]
in_out("12-jhanavibhango.md", "hoặc bằng lời nịnh bợ, hoặc bằng lời nửa thật nửa giả")
APAYA = "sau khi thân tan rã, sau khi chết, tái sinh vào cõi khổ, cõi xấu, nơi đọa lạc, địa ngục"   # [ch16]
in_out("16-nanavibhango.md", APAYA)
SOKA = "sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng"       # [pi-1 ^1-1343, ch4]
in_out("4-saccavibhango.md", SOKA)
ANICCA3 = "là vô thường, là khổ đau, có bản chất biến đổi"                       # [ch2 words]
in_out("2-ayatanavibhango.md", "là vô thường, là khổ đau, không phải là tự ngã, có bản chất biến đổi")
ARIYA_Q = "Ở đây, các bậc thánh là ai?"                                           # [ch12 ^2-588]
in_out("12-jhanavibhango.md", low(ARIYA_Q), "Các Đức Phật và các đệ tử của Đức Phật được gọi là các bậc thánh")
VED = {"rūpa": "các hình sắc", "sadda": "các âm thanh", "gandha": "các mùi", "rasa": "các vị",
       "phoṭṭhabba": "các vật xúc chạm", "dhamma": "các đối tượng của ý"}       # [ch4 words]
# jhāna openings, abbreviated [pi-1 2-02]
JH = {1: "hoàn toàn tách khỏi các dục lạc… chứng nhập và an trú tầng thiền thứ nhất",
      2: "nhờ sự hướng tâm và sự duy trì tâm lắng xuống… chứng nhập và an trú tầng thiền thứ hai",
      3: "nhờ sự hân hoan phai nhạt… chứng nhập và an trú tầng thiền thứ ba",
      4: "nhờ dứt bỏ sự dễ chịu… chứng nhập và an trú tầng thiền thứ tư"}
_J = pv("2-02-cittuppadakandam.md", "Katame dhammā kusalā? Yasmiṃ samaye rūpūpapattiyā maggaṃ bhāveti vivicceva "
        "kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ –")
assert JH[1] in _J, _J
assert "nhờ sự hướng tâm và sự duy trì tâm lắng xuống… " in pv("2-02-cittuppadakandam.md",
                                                                "Katame dhammā kusalā? Yasmiṃ samaye rūpūpapattiyā "
                                                                "maggaṃ bhāveti vitakkavicārānaṃ vūpasamā…pe… tatiyaṃ")
assert "nhờ sự hân hoan phai nhạt… chứng nhập và an trú tầng thiền thứ ba" in pv(
    "2-02-cittuppadakandam.md", "Katame dhammā kusalā? Yasmiṃ samaye rūpūpapattiyā maggaṃ bhāveti pītiyā ca virāgā…pe… "
                                "tatiyaṃ jhānaṃ upasampajja viharati mettāsahagataṃ")
assert "nhờ dứt bỏ sự dễ chịu… chứng nhập và an trú tầng thiền thứ tư" in pv(
    "2-02-cittuppadakandam.md", "Katame dhammā kusalā? Yasmiṃ samaye rūpūpapattiyā maggaṃ bhāveti sukhassa ca pahānā…pe… "
                                "catutthaṃ jhānaṃ upasampajja viharati upekkhāsahagataṃ")
ARUPA1 = ("nhờ hoàn toàn vượt qua các tri giác về hình sắc, nhờ các tri giác về sự va chạm biến mất, nhờ không chú tâm "
          "đến các tri giác về sự đa dạng")                                      # [pi-1 ^1-265]
assert ARUPA1 in pv("2-02-cittuppadakandam.md", "Katame dhammā kusalā? Yasmiṃ samaye arūpūpapattiyā maggaṃ bhāveti "
                                                "sabbaso rūpasaññānaṃ")
assert "hoàn toàn vượt qua lĩnh vực không có gì cả" in pv("2-02-cittuppadakandam.md", "Katame dhammā kusalā? Yasmiṃ "
                                                          "samaye arūpūpapattiyā maggaṃ bhāveti sabbaso ākiñcaññāyatanaṃ")
NANATTA = "tri giác về sự đa dạng"                                                # nānattasaññā [pi-1 ^1-265]

# ================================================================ 2. names [new unless marked]
MADA = [  # (Pāli accusative before "paṭicca", Vietnamese noun) for jātimado … pāripūrimado
    ("Jātiṃ", "xuất thân"), ("Gottaṃ", "dòng họ"), ("ārogyaṃ", "sức khỏe"), ("yobbanaṃ", "tuổi trẻ"),
    ("jīvitaṃ", "sự sống"), ("lābhaṃ", "lợi lộc"), ("sakkāraṃ", "sự tôn vinh"), ("garukāraṃ", "sự kính trọng"),
    ("purekkhāraṃ", "sự được ưu tiên"), ("parivāraṃ", "đoàn tùy tùng"), ("bhogaṃ", "của cải"), ("vaṇṇaṃ", "sắc đẹp"),
    ("sutaṃ", "sự học hỏi"), ("paṭibhānaṃ", "tài ứng đáp"), ("rattaññutaṃ", "thâm niên"),
    ("piṇḍapātikattaṃ", "hạnh khất thực"), ("anavaññātaṃ", "việc không bị xem nhẹ"), ("iriyāpathaṃ", "tư thế"),
    ("iddhiṃ", "thần thông"), ("yasaṃ", "danh tiếng"), ("sīlaṃ", "giới hạnh"), ("jhānaṃ", "tầng thiền"),
    ("sippaṃ", "nghề thủ công"), ("ārohaṃ", "chiều cao"), ("pariṇāhaṃ", "vóc người to lớn"),
    ("saṇṭhānaṃ", "hình dáng"), ("pāripūriṃ", "sự hoàn hảo")]
MADA_P = ["jāti", "gotta", "ārogya", "yobbana", "jīvita", "lābha", "sakkāra", "garukāra", "purekkhāra", "parivāra",
          "bhoga", "vaṇṇa", "suta", "paṭibhāna", "rattaññu", "piṇḍapātika", "anavaññāta", "iriyāpatha", "iddhi", "yasa",
          "sīla", "jhāna", "sippa", "āroha", "pariṇāha", "saṇṭhāna", "pāripūri"]
MADO = "sự say sưa"
MADA_SYN = "sự say sưa, sự khởi say sưa, trạng thái khởi say sưa"                 # mado majjanā majjitattaṃ
SILOKA = "lợi lộc, sự tôn vinh và tiếng tăm"                                      # lābhasakkārasiloka [pi-1 words]
N = {}   # Pāli name (as in the matrix) -> Vietnamese
for _p, (_acc, _v) in zip(MADA_P, MADA):
    N[_p + "mado"] = f"{MADO} vì {_v}"
MANA_NAMES = {"seyyohamasmīti māno": MANA3[0], "sadisohamasmīti māno": MANA3[1], "hīnohamasmīti māno": MANA3[2]}
WHO = {"seyyassa": "của người vốn hơn người", "sadisassa": "của người vốn bằng người",
       "hīnassa": "của người vốn kém người"}
for _w, _wv in WHO.items():
    for _k, _v in list(MANA_NAMES.items())[:3]:
        MANA_NAMES[f"{_w} {_k}"] = f"{_v} {_wv}"
N.update(MANA_NAMES)
N.update({
    "mado": MADO, "pamādo": "sự buông thả", "thambho": "sự cứng đầu", "sārambho": "sự tranh hơn",
    "atricchatā": "sự tham muốn quá độ", "mahicchatā": "sự có nhiều tham muốn", "pāpicchatā": "sự có ước muốn xấu xa",
    "siṅgaṃ": "sự kiểu cách", "tintiṇaṃ": "sự khó tính", "cāpalyaṃ": "sự phù phiếm",
    "asabhāgavutti": "lối cư xử không thích đáng", "arati": "sự không hoan hỷ", "tandī": "sự lười nhác",
    "vijambhitā": "sự vươn vai", "bhattasammado": "sự ngầy ngật sau bữa ăn", "cetaso ca līnattaṃ": "sự co rút của tâm",
    "kuhanā": "sự lừa gạt", "lapanā": "sự nói ngọt", "nemittikatā": "sự ra dấu gợi ý", "nippesikatā": "sự chèn ép",
    "lābhena lābhaṃ nijigīsanatā": "sự dùng lợi lộc để tìm kiếm lợi lộc",
    "māno": "sự kiêu mạn", "atimāno": "sự ngạo mạn", "mānātimāno": "sự kiêu mạn chồng chất", "omāno": "sự tự ti",
    "adhimāno": "sự tự đánh giá quá cao", "asmimāno": "sự kiêu mạn “Tôi là”", "micchāmāno": "sự kiêu mạn sai lầm",
    "ñātivitakko": "sự hướng tâm đến người thân", "janapadavitakko": "sự hướng tâm đến xứ sở",
    "amaravitakko": "sự hướng tâm đến sự bất tử",
    "parānuddayatāpaṭisaṃyutto vitakko": "sự hướng tâm liên quan đến sự quan tâm đến người khác",
    "lābhasakkārasilokapaṭisaṃyutto vitakko": f"sự hướng tâm liên quan đến {SILOKA}",
    "anavaññattipaṭisaṃyutto vitakko": "sự hướng tâm liên quan đến việc không bị xem nhẹ",
    # duka
    "kodho": "sự giận dữ", "upanāho": "sự ôm hận", "makkho": "sự gièm pha", "paḷāso": "sự ganh đua",
    "issā": "sự ganh tị", "macchariyaṃ": "sự keo kiệt", "māyā": "sự xảo trá", "sāṭheyyaṃ": "sự gian xảo",
    "avijjā": "vô minh", "bhavataṇhā": "khao khát được hiện hữu",
    "ahirikaṃ": "sự không biết hổ thẹn", "anottappaṃ": "sự không biết ghê sợ tội lỗi",
    "dovacassatā": "sự khó dạy bảo", "pāpamittatā": "sự kết bạn với người xấu",
    "anajjavo": "sự không ngay thật", "amaddavo": "sự không mềm mỏng", "akkhanti": "sự không nhẫn nại",
    "asoraccaṃ": "sự không hiền hòa", "asākhalyaṃ": "sự không hòa nhã",
    "appaṭisanthāro": "sự không niềm nở tiếp đón",
    "indriyesu aguttadvāratā": "sự không phòng hộ cửa các giác quan",
    "bhojane amattaññutā": "sự không biết tiết độ trong ăn uống", "muṭṭhassaccaṃ": "sự mất tỉnh thức",
    "asampajaññaṃ": "sự thiếu hiểu biết rõ ràng", "sīlavipatti": "sự suy đồi về giới hạnh",
    "diṭṭhivipatti": "sự suy đồi về quan điểm", "ajjhattasaṃyojanaṃ": "xiềng xích ở nơi bản thân",
    "bahiddhāsaṃyojanaṃ": "xiềng xích ở bên ngoài bản thân",
    # tika singles
    "assādadiṭṭhi": "quan điểm về sự thỏa thích", "attānudiṭṭhi": "quan điểm xem có tự ngã",
    "micchādiṭṭhi": "quan điểm sai lầm", "vihesā": "sự gây phiền nhiễu", "adhammacariyā": "hành vi phi pháp",
    "nānattasaññā": NANATTA, "uddhaccaṃ": "sự xao động", "kosajjaṃ": "sự lười biếng",
    "asantuṭṭhitā": "sự không biết đủ", "asampajaññatā": "sự thiếu hiểu biết rõ ràng",
    "anādariyaṃ": "sự thiếu tôn trọng", "assaddhiyaṃ": "sự thiếu niềm tin", "avadaññutā": "sự không rộng lượng",
    "asaṃvaro": "sự không thu thúc", "dussīlyaṃ": "sự phạm giới",
    "ariyānaṃ adassanakamyatā": "sự không muốn thấy các bậc thánh",
    "saddhammaṃ asotukamyatā": "sự không muốn nghe Giáo Pháp chân chính", "upārambhacittatā": "sự có tâm hay bắt lỗi",
    "cetaso vikkhepo": "sự tán loạn của tâm", "ayoniso manasikāro": "sự chú tâm không khôn ngoan",
    "kummaggasevanā": "sự đi theo con đường lệch lạc",
})
for _k, (_qv, _) in DIT_Q.items():
    N[_k.replace(" ", "")] = _qv                                                 # bhavadiṭṭhi … [pi-1 ^1-1320 …]
assert N["sassatadiṭṭhi"] == "quan điểm về sự trường tồn" and N["antavādiṭṭhi"] == "quan điểm về sự hữu hạn"

# group names (tika … dasaka) [new unless marked]
GN = {
    "akusalamūla": "gốc rễ bất thiện", "akusalavitakka": "sự hướng tâm bất thiện", "akusalasaññā": "tri giác bất thiện",
    "akusaladhātu": "yếu tố bất thiện", "duccarita": "hành vi xấu", "āsava": "ô nhiễm", "saṃyojana": "xiềng xích",
    "taṇhā": "loại khao khát", "esanā": "sự tìm cầu", "vidhā": "sự so sánh", "bhaya": "nỗi sợ hãi",
    "tama": "sự tăm tối", "titthāyatana": "lĩnh vực của các học thuyết ngoại đạo", "kiñcana": "sự vướng bận",
    "aṅgaṇa": "vết nhơ", "mala": "sự dơ bẩn", "visama": "sự lệch lạc", "aggi": "ngọn lửa", "kasāva": "chất cặn bẩn",
    "gantha": "nút thắt", "ogha": "dòng lũ", "yoga": "ách", "upādāna": "sự bám víu",
    "taṇhuppāda": "nguyên nhân khởi lên khao khát", "agatigamana": "sự đi theo con đường sai trái",
    "vipariyāsa": "sự đảo ngược", "anariyavohāra": "cách nói không cao quý", "diṭṭhi": "quan điểm",
    "orambhāgiya": "xiềng xích thuộc phần thấp", "uddhambhāgiya": "xiềng xích thuộc phần cao",
    "macchariya": "loại keo kiệt", "saṅga": "sự dính mắc", "salla": "mũi tên", "cetokhila": "sự chai cứng của tâm",
    "vinibandha": "sự trói buộc của tâm", "nīvaraṇa": "chướng ngại",
    "ānantarika": "nghiệp trổ quả ngay kiếp kế tiếp", "vera": "điều gây thù địch", "byasana": "tổn hại",
    "ādīnava": "điều nguy hại của sự không nhẫn nại",
    "dnv": "học thuyết về Niết-bàn ngay trong đời này", "vivādamūla": "gốc rễ của tranh cãi",
    "chandarāga": "sự tham đắm do ý muốn", "virodhavatthu": "căn cứ của sự chống đối", "taṇhākāya": "nhóm khao khát",
    "agārava": "sự thiếu kính trọng", "parihāniya": "hiện tượng dẫn đến suy thoái",
    "su": "sự lưu tâm gắn với niềm vui", "du": "sự lưu tâm gắn với nỗi buồn", "uu": "sự lưu tâm gắn với sự bình thản",
    "gs": "niềm vui gắn với đời sống thế tục", "gd": "nỗi buồn gắn với đời sống thế tục",
    "gu": "sự bình thản gắn với đời sống thế tục", "anusaya": "khuynh hướng tiềm ẩn",
    "pariyuṭṭhāna": "sự ám ảnh", "asaddhamma": "điều không chân chính", "māna": "loại kiêu mạn",
    "kilesavatthu": "chỗ dựa của phiền não", "kusītavatthu": "chỗ dựa của sự lười biếng",
    "lokadhamma": "sự va chạm của tâm trong tám hiện tượng thế gian", "micchatta": "sự sai lầm",
    "purisadosa": "lỗi của con người", "asaññī": "học thuyết cho rằng tự ngã không có tri giác",
    "nevasaññī": "học thuyết cho rằng tự ngã không phải có tri giác cũng không phải không có tri giác",
    "āghātavatthu": "căn cứ của sự oán giận", "purisamala": "sự dơ bẩn của con người",
    "taṇhāmūlaka": "hiện tượng bắt nguồn từ khao khát", "iñjita": "sự dao động", "maññita": "sự tưởng tượng",
    "phandita": "sự rung động", "papañcita": "sự suy diễn lan man", "saṅkhata": "điều được tạo tác",
    "kammapatha": "con đường nghiệp bất thiện",
    "dv_micchā": "quan điểm sai lầm có mười chủ đề",
    "dv_anta": "quan điểm chấp giữ cực đoan có mười chủ đề",
}
NUMW = {2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười"}
KHAC = "khác nữa"                                                                 # apara-pi


def g(n, k, other=False):
    return f"{NUMW[n]} {GN[k]}" + (f" {KHAC}" if other else "")


# ================================================================ 3. variant brackets
V = {
    "[cetaso līnattaṃ (syā.)]": "[dị bản (Syā.): cetaso līnattaṃ]",
    "[nijigiṃsanatā (sī.), jigiṃsanatā (syā.)]": "[khác chính tả (Sī.): nijigiṃsanatā; (Syā.): jigiṃsanatā]",
    "[palāso (sī. syā.)]": "[khác chính tả (Sī., Syā.): palāso]",
    "[vipariyesā (sī. syā. ka.)]": "[khác chính tả (Sī., Syā., Ka.): vipariyesā]",
    "[cetasovinibaddhā (ka.)]": "[dị bản (Ka.): cetasovinibaddhā]",
}
VAR_VIJJA = " [khác chính tả (Syā.): vijjaṭṭhānena]"
VAR_PACCAYA = " [dị bản (Sī.): paccayapaṭisedhanasaṅkhātena]"
VAR_ATHAPANA = " [khác chính tả (Ka.): āṭhapanā]"
VAR_MAKKHA = " [khác chính tả (Sī., Ka.): makkhiyanā makkhiyitattaṃ]"
VAR_PALASA = " [dị bản (Syā.): palāsāyanā palāsāyitattaṃ]"
VAR_KAKKARA = " [dị bản (Syā.): kakkhaḷatā kakkhaḷiyaṃ]"
VAR_KATHINA = " [khác chính tả (Syā., Ka.): kathinatā]"
VAR_SANDHARA = " [khác chính tả (Ka.): appaṭisandhāro]"
VAR_KINCANA = " [dị bản (?): katamāni tīṇi kiñcanāni; dī. ni. 3.305]"
VAR_ANADDA = " [khác chính tả (Syā.): anādā anādāyanā anādāyitattaṃ]"
VAR_KUMBHILA = " [khác chính tả (?): kumbhīrabhayaṃ, kumbhīḷabhayaṃ (kumbha + īra + a = bhaya)]"
VAR_EVAMDITTHI = " [khác chính tả (Syā.): evaṃdiṭṭhi]"
VAR_CATUMAHA = " [khác chính tả (Sī., Syā.): cātummahābhūtiko]"
VAR_GILANA = (" [khác chính tả (saddanībhi): gilānavuṭṭhito; a. ni. 6.16; nên tham khảo sách phụ chú giải về đoạn kinh "
              "văn này]")
VAR_CODIYA = " [khác chính tả (Sī., Syā.): codiyamāno; a. ni. 8.14]"
VAR_CODAKA = " [dị bản (Syā.): codakasseva; a. ni. 8.14]"
VAR_SAPATTI = " [dị bản (Ka.): āpattikova; a. ni. 8.14]"
VAR_ANAVAKARI = " [khác chính tả (Sī., Ka.): anavakārī]"
VAR_PARAPUGGALA = " [khác chính tả (Syā.): paraṃ puggalaṃ]"
VAR_AVAKARI = " [khác chính tả (Sī.): avakārī]"
assert "[dị bản (Ka.): samaggatā]" in NATTHI_V

# ================================================================ 4. matrix lines
M1 = ["jātimado", "gottamado", "ārogyamado", "yobbanamado", "jīvitamado", "lābhamado", "sakkāramado", "garukāramado",
      "purekkhāramado", "parivāramado", "bhogamado", "vaṇṇamado", "sutamado", "paṭibhānamado", "rattaññumado",
      "piṇḍapātikamado", "anavaññātamado", "iriyāpathamado", "iddhimado", "yasamado", "sīlamado", "jhānamado",
      "sippamado", "ārohamado", "pariṇāhamado", "saṇṭhānamado", "pāripūrimado", "mado", "pamādo", "thambho",
      "sārambho", "atricchatā", "mahicchatā", "pāpicchatā", "siṅgaṃ", "tintiṇaṃ", "cāpalyaṃ", "asabhāgavutti",
      "arati", "tandī", "vijambhitā", "bhattasammado", "cetaso ca līnattaṃ [cetaso līnattaṃ (syā.)]", "kuhanā",
      "lapanā", "nemittikatā", "nippesikatā",
      "lābhena lābhaṃ nijigīsanatā [nijigiṃsanatā (sī.), jigiṃsanatā (syā.)]",
      "seyyohamasmīti māno", "sadisohamasmīti māno", "hīno hamasmīti māno", "seyyassa seyyohamasmīti māno",
      "seyyassa sadisohamasmīti māno", "seyyassa hīnohamasmīti māno", "sadisassa seyyohamasmīti māno",
      "sadisassa sadisohamasmīti māno", "sadisassa hīnohamasmīti māno", "hīnassa seyyohamasmīti māno",
      "hīnassa sadisohamasmīti māno", "hīnassa hīnohamasmīti māno", "māno", "atimāno", "mānātimāno", "omāno",
      "adhimāno", "asmimāno", "micchāmāno", "ñātivitakko", "janapadavitakko", "amaravitakko",
      "parānuddayatāpaṭisaṃyutto vitakko", "lābhasakkārasilokapaṭisaṃyutto vitakko",
      "anavaññattipaṭisaṃyutto vitakko"]


def item_vi(p):
    m = re.match(r"^(.*?)\s*(\[[^\]]*\])?$", p)
    base, var = m.group(1), m.group(2)
    base = {"hīno hamasmīti māno": "hīnohamasmīti māno"}.get(base, base)
    if base == "hīnohamasmīti māno" and p.startswith("hīno ham"):
        SLIPS.append("^2-832 matrix (51) 'hīno hamasmīti' (space): no effect")
    return N[base] + (" " + V[var] if var else "")


def numbered(items_vi):
    return " ".join(f"({i}) {cap(v) if i == 1 else v}" for i, v in enumerate(items_vi, 1))


def check_numbered(pali, items_p):
    norm = re.sub(r"\((\d+)\)\s*", r"(\1) ", pali).strip()
    want = " ".join(f"({i}) {cap(p) if i == 1 else p}" for i, p in enumerate(items_p, 1))
    assert norm == want, (norm[:200], want[:200])


MATRIX = {}   # first words of the Pāli line -> (items_p, items_vi)
MATRIX["(1)Jātimado"] = (M1, [item_vi(p) for p in M1])
M2 = [("kodho", "upanāho"), ("makkho", "paḷāso [palāso (sī. syā.)]"), ("issā", "macchariyañca"),
      ("māyā", "sāṭheyyañca"), ("avijjā", "bhavataṇhā"), ("bhavadiṭṭhi", "vibhavadiṭṭhi"),
      ("sassatadiṭṭhi", "ucchedadiṭṭhi"), ("antavādiṭṭhi", "anantavādiṭṭhi"),
      ("pubbantānudiṭṭhi", "aparantānudiṭṭhi"), ("ahirikañca", "anottappañca"), ("dovacassatā", "pāpamittatā"),
      ("anajjavo", "amaddavo"), ("akkhanti", "asoraccañca"), ("asākhalyañca", "appaṭisanthāro"),
      ("indriyesu aguttadvāratā", "bhojane amattaññutā"), ("muṭṭhassaccañca", "asampajaññañca"),
      ("sīlavipatti", "diṭṭhivipatti"), ("ajjhattasaṃyojanañca", "bahiddhāsaṃyojanañca")]


def duka_p(a, b):
    def ca(x):
        if x.endswith("ñca"):
            return x
        if "[" in x:
            return x + " ca"
        return x + " ca"
    return f"{ca(a)} {ca(b)}"


def strip_ca(x):
    x = re.sub(r"\s*\[[^\]]*\]", "", x)
    return x[:-3] + "ṃ" if x.endswith("ñca") else x


def duka_v(a, b):
    va = N[strip_ca(a)]
    vb = N[strip_ca(b)] + (" " + V[re.search(r"\[[^\]]*\]", b).group(0)] if "[" in b else "")
    return f"{va} và {vb}"


MATRIX["(1) Kodho"] = ([duka_p(a, b) for a, b in M2], [duka_v(a, b) for a, b in M2])
M3 = [("Tīṇi akusalamūlāni", g(3, "akusalamūla")), ("tayo akusalavitakkā", g(3, "akusalavitakka")),
      ("tisso akusalasaññā", g(3, "akusalasaññā")), ("tisso akusaladhātuyo", g(3, "akusaladhātu")),
      ("tīṇi duccaritāni", g(3, "duccarita")), ("tayo āsavā", g(3, "āsava")), ("tīṇi saṃyojanāni", g(3, "saṃyojana")),
      ("tisso taṇhā", g(3, "taṇhā")), ("aparāpi tisso taṇhā", g(3, "taṇhā", True)),
      ("aparāpi tisso taṇhā", g(3, "taṇhā", True)), ("tisso esanā", g(3, "esanā")), ("tisso vidhā", g(3, "vidhā")),
      ("tīṇi bhayāni", g(3, "bhaya")), ("tīṇi tamāni", g(3, "tama")), ("tīṇi titthāyatanāni", g(3, "titthāyatana")),
      ("tayo kiñcanā", g(3, "kiñcana")), ("tīṇi aṅgaṇāni", g(3, "aṅgaṇa")), ("tīṇi malāni", g(3, "mala")),
      ("tīṇi visamāni", g(3, "visama")), ("aparānipi tīṇi visamāni", g(3, "visama", True)),
      ("tayo aggī", g(3, "aggi")), ("tayo kasāvā", g(3, "kasāva")), ("aparepi tayo kasāvā", g(3, "kasāva", True))]
T3 = [("assādadiṭṭhi", "attānudiṭṭhi", "micchādiṭṭhi"), ("arati", "vihesā", "adhammacariyā"),
      ("dovacassatā", "pāpamittatā", "nānattasaññā"), ("uddhaccaṃ", "kosajjaṃ", "pamādo"),
      ("asantuṭṭhitā", "asampajaññatā", "mahicchatā"), ("ahirikaṃ", "anottappaṃ", "pamādo"),
      ("anādariyaṃ", "dovacassatā", "pāpamittatā"), ("assaddhiyaṃ", "avadaññutā", "kosajjaṃ"),
      ("uddhaccaṃ", "asaṃvaro", "dussīlyaṃ"),
      ("ariyānaṃ adassanakamyatā", "saddhammaṃ asotukamyatā", "upārambhacittatā"),
      ("muṭṭhassaccaṃ", "asampajaññaṃ", "cetaso vikkhepo"),
      ("ayoniso manasikāro", "kummaggasevanā", "cetaso ca līnattaṃ")]
for _t in T3:
    _p = ", ".join(_t)
    _v = ", ".join(N[x] for x in _t)
    if _t[-1] == "cetaso ca līnattaṃ":
        _v = f"{N[_t[0]]}, {N[_t[1]]} và {N[_t[2]]}"                            # "ca" before the last item
    M3.append((_p, _v))
MATRIX["(1) Tīṇi"] = ([p for p, _ in M3], [v for _, v in M3])
M4 = [("Cattāro āsavā", g(4, "āsava")), ("cattāro ganthā", g(4, "gantha")), ("cattāro oghā", g(4, "ogha")),
      ("cattāro yogā", g(4, "yoga")), ("cattāri upādānāni", g(4, "upādāna")),
      ("cattāro taṇhuppādā", g(4, "taṇhuppāda")), ("cattāri agatigamanāni", g(4, "agatigamana")),
      ("cattāro vipariyāsā [vipariyesā (sī. syā. ka.)]", g(4, "vipariyāsa") + " " + V["[vipariyesā (sī. syā. ka.)]"]),
      ("cattāro anariyavohārā", g(4, "anariyavohāra")), ("aparepi cattāro anariyavohārā", g(4, "anariyavohāra", True)),
      ("cattāri duccaritāni", g(4, "duccarita")), ("aparānipi cattāri duccaritāni", g(4, "duccarita", True)),
      ("cattāri bhayāni", g(4, "bhaya")), ("aparānipi cattāri bhayāni", g(4, "bhaya", True)),
      ("catasso diṭṭhiyo", g(4, "diṭṭhi"))]
MATRIX["(1) Cattāro"] = ([p for p, _ in M4], [v for _, v in M4])
M5 = [("Pañcorambhāgiyāni saṃyojanāni", g(5, "orambhāgiya")),
      ("pañcuddhambhāgiyāni saṃyojanāni", g(5, "uddhambhāgiya")), ("pañca macchariyāni", g(5, "macchariya")),
      ("pañca saṅgā", g(5, "saṅga")), ("pañca sallā", g(5, "salla")), ("pañca cetokhilā", g(5, "cetokhila")),
      ("pañca cetasovinibandhā [cetasovinibaddhā (ka.)]", g(5, "vinibandha") + " " + V["[cetasovinibaddhā (ka.)]"]),
      ("pañca nīvaraṇāni", g(5, "nīvaraṇa")), ("pañca kammāni ānantarikāni", g(5, "ānantarika")),
      ("pañca diṭṭhiyo", g(5, "diṭṭhi")), ("pañca verā", g(5, "vera")), ("pañca byasanā", g(5, "byasana")),
      ("pañca akkhantiyā ādīnavā", g(5, "ādīnava")), ("pañca bhayāni", g(5, "bhaya")),
      ("pañca diṭṭhadhammanibbānavādā", g(5, "dnv"))]
MATRIX["(1) Pañcorambhāgiyāni"] = ([p for p, _ in M5], [v for _, v in M5])
M6 = [("Cha vivādamūlāni", g(6, "vivādamūla")), ("cha chandarāgā", g(6, "chandarāga")),
      ("cha virodhavatthūni", g(6, "virodhavatthu")), ("cha taṇhākāyā", g(6, "taṇhākāya")),
      ("cha agāravā", g(6, "agārava")), ("cha parihāniyā dhammā", g(6, "parihāniya")),
      ("aparepi cha parihāniyā dhammā", g(6, "parihāniya", True)), ("cha somanassupavicārā", g(6, "su")),
      ("cha domanassupavicārā", g(6, "du")), ("cha upekkhupavicārā", g(6, "uu")),
      ("cha gehasitāni somanassāni", g(6, "gs")), ("cha gehasitāni domanassāni", g(6, "gd")),
      ("cha gehasitā upekkhā", g(6, "gu")), ("cha diṭṭhiyo", g(6, "diṭṭhi"))]
MATRIX["(1) Cha"] = ([p for p, _ in M6], [v for _, v in M6])
M7 = [("Satta anusayā", g(7, "anusaya")), ("satta saṃyojanāni", g(7, "saṃyojana")),
      ("satta pariyuṭṭhānāni", g(7, "pariyuṭṭhāna")), ("satta asaddhammā", g(7, "asaddhamma")),
      ("satta duccaritāni", g(7, "duccarita")), ("satta mānā", g(7, "māna")), ("satta diṭṭhiyo", g(7, "diṭṭhi"))]
MATRIX["(1) Satta"] = ([p for p, _ in M7], [v for _, v in M7])
M8 = [("Aṭṭha kilesavatthūni", g(8, "kilesavatthu")), ("aṭṭha kusītavatthūni", g(8, "kusītavatthu")),
      ("aṭṭhasu lokadhammesu cittassa paṭighāto", GN["lokadhamma"]),
      ("aṭṭha anariyavohārā", g(8, "anariyavohāra")), ("aṭṭha micchattā", g(8, "micchatta")),
      ("aṭṭha purisadosā", g(8, "purisadosa")), ("aṭṭha asaññivādā", g(8, "asaññī")),
      ("aṭṭha nevasaññināsaññivādā", g(8, "nevasaññī"))]
MATRIX["(1) Aṭṭha"] = ([p for p, _ in M8], [v for _, v in M8])
M9 = [("Nava āghātavatthūni", g(9, "āghātavatthu")), ("nava purisamalāni", g(9, "purisamala")),
      ("navavidhā mānā", g(9, "māna")), ("nava taṇhāmūlakā dhammā", g(9, "taṇhāmūlaka")),
      ("nava iñjitāni", g(9, "iñjita")), ("nava maññitāni", g(9, "maññita")), ("nava phanditāni", g(9, "phandita")),
      ("nava papañcitāni", g(9, "papañcita")), ("nava saṅkhatāni", g(9, "saṅkhata"))]
MATRIX["(1) Nava"] = ([p for p, _ in M9], [v for _, v in M9])
M10 = [("Dasa kilesavatthūni", g(10, "kilesavatthu")), ("dasa āghātavatthūni", g(10, "āghātavatthu")),
       ("dasa akusalakammapathā", g(10, "kammapatha")), ("dasa saṃyojanāni", g(10, "saṃyojana")),
       ("dasa micchattā", g(10, "micchatta")), ("dasavatthukā micchādiṭṭhi", GN["dv_micchā"]),
       ("dasavatthukā antaggāhikā diṭṭhi", GN["dv_anta"])]
MATRIX["(1) Dasa"] = ([p for p, _ in M10], [v for _, v in M10])
assert KILESA10.startswith("Mười " + GN["kilesavatthu"])

# ================================================================ 5. recurring formulas [new unless marked]
IDHEK = "Ở đời này, có người"                                                     # Idhekacco [pi-1 ^1-1352]
SB = "Ở đời này, có sa-môn hay bà-la-môn có học thuyết như vầy, có quan điểm như vầy"   # samaṇo vā brāhmaṇo vā evaṃvādī …
MLIST = ["xuất thân", "dòng họ", "gia thế", "vẻ đẹp dung mạo", "tài sản", "việc học tập kinh sách", "ngành nghề",
         "ngành thủ công", "lĩnh vực học thuật", "sự học hỏi", "tài ứng đáp"]     # kammāyatana … [ch16]
OTHERV = "điều này hay điều khác"                                                 # aññataraññatarena vatthunā


def mlist(var="", pe=False):
    items = [f"{x}{var if x == 'lĩnh vực học thuật' else ''}" for x in MLIST]
    if pe:
        return f"{items[0]}, hoặc {items[1]}, hoặc {items[2]}… hoặc {OTHERV}"
    return ", hoặc ".join(items) + f", hoặc {OTHERV}"


OMANA_SYN = ("sự tự ti, sự tự đánh giá thấp mình, trạng thái tự đánh giá thấp mình, sự tự chê bai, sự tự chê bai thậm "
             "tệ, trạng thái tự chê bai thậm tệ, sự tự coi thường, sự tự xem nhẹ, sự tự khinh miệt")
EVA = "điều mà thuộc loại như vậy là"                                             # yo / yā / yaṃ evarūpo [pi-1 ^1-1066]
ATRI = ("Sự mong muốn nhiều hơn nữa của người không biết đủ với y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng "
        "chữa bệnh thế này hay thế khác, hoặc với năm đối tượng của dục lạc")    # [pi-1 ^1-1378 / ^1-1353 words]
RAGA3 = "sự tham đắm, sự say đắm, sự say đắm của tâm"                            # rāgo sārāgo cittassa sārāgo [pi-1]
assert LOBHA.startswith("Điều mà là sự tham đắm, sự say đắm, ") and "sự say đắm của tâm" in LOBHA


def atri(name):
    return f"{ATRI}, {EVA} sự mong muốn, trạng thái bị mong muốn chi phối, {name}, {RAGA3}"


KUHA = f"Ở người bám vào {SILOKA}, có ước muốn xấu xa, bị ước muốn chi phối"
PAMADA_A = ("trong hành vi xấu bằng thân, hoặc trong hành vi xấu bằng lời nói, hoặc trong hành vi xấu bằng ý, hoặc trong "
            "năm đối tượng của dục lạc, sự buông lơi của tâm, sự tiếp tục để mặc cho buông lơi")
PAMADA_B = ("trong việc tu tập các hiện tượng thiện, sự làm không chu đáo, sự làm không liên tục, sự làm có ngừng nghỉ, "
            "sự hành xử chùng xuống, sự buông bỏ ý muốn, sự buông bỏ gánh, sự không thực hành, sự không tu tập, sự "
            "không làm đi làm lại, sự không quyết tâm, sự không chuyên cần, sự buông thả")   # [pi-1 ^1-1379 negated]
assert "sự làm chu đáo, sự làm liên tục, sự làm không ngừng nghỉ, sự hành xử không chùng xuống, sự không buông bỏ ý " \
       "muốn, sự không buông bỏ gánh, sự thực hành, sự tu tập, sự làm đi làm lại" in pv(F403, "Appaṭivānitā ca")
PAMADA_FULL = f"{cap(PAMADA_A)}; hoặc {PAMADA_B}, {EVA} sự buông thả, sự khởi buông thả, trạng thái khởi buông thả"
PAMADA_U = f"{cap(PAMADA_A)}; hoặc {PAMADA_B}, {EVA} sự buông thả, sự khởi buông thả, trạng thái khởi buông thả"
KOSAJJA = f"{cap(PAMADA_A)}; {PAMADA_B}"
GEH = "gắn với đời sống thế tục"                                                  # gehasita [new]
SUY = "Suy nghĩ"                                                                  # takko [ch3]


def takka(pre):
    return f"{SUY} {pre}, {TAKKA}"


BODY_TAKKA = f"{GEH}"


def q_ka(letter, name):
    return f"({letter}) {q(name, lower=True)}"


# ================================================================ 6. taṇhāvicarita (18 + 18)
PRED = [("khattiyo", "là người thuộc giai cấp quý tộc"), ("brāhmaṇo", "là bà-la-môn"),
        ("vesso", "là người thuộc giai cấp thương nhân"), ("suddo", "là người thuộc giai cấp lao động"),
        ("gahaṭṭho", "là người tại gia"), ("pabbajito", "là người xuất gia"), ("devo", "là vị trời"),
        ("manusso", "là con người"), ("rūpī", "có hình sắc"), ("arūpī", "không có hình sắc"), ("saññī", "có tri giác"),
        ("asaññī", "không có tri giác"),
        ("nevasaññīnāsaññī", "không phải có tri giác cũng không phải không có tri giác")]
MOOD = {"pres": ("tôi", "tôi cũng", "tôi"), "fut": ("tôi sẽ", "tôi cũng sẽ", "tôi sẽ"),
        "pot": ("tôi có thể", "tôi cũng có thể", "tôi có thể"), "wish": ("ước gì tôi", "ước gì tôi cũng", "ước gì tôi")}
LAB = {"asmi": "Tôi là", "itthasmi": "Tôi là như thế này", "evasmi": "Tôi cũng giống như thế",
       "aññathāsmi": "Tôi khác đi", "bhavissaṃ": "Tôi sẽ là", "itthaṃ bhavissaṃ": "Tôi sẽ là như thế này",
       "evaṃ bhavissaṃ": "Tôi cũng sẽ giống như thế", "aññathā bhavissaṃ": "Tôi sẽ khác đi",
       "asasmi": "Tôi thường còn", "sātasmi": "Tôi đoạn diệt", "siyaṃ": "Tôi có thể là",
       "itthaṃ siyaṃ": "Tôi có thể là như thế này", "evaṃ siyaṃ": "Tôi cũng có thể giống như thế",
       "aññathā siyaṃ": "Tôi có thể khác đi", "apāhaṃ siyaṃ": "Ước gì tôi là",
       "apāhaṃ itthaṃ siyaṃ": "Ước gì tôi là như thế này", "apāhaṃ evaṃ siyaṃ": "Ước gì tôi cũng giống như thế",
       "apāhaṃ aññathā siyaṃ": "Ước gì tôi khác đi"}
ORDER18 = list(LAB)
IMINA = "Nhờ cái này, "                                                           # iminā [new]


def lab(k, im):
    return (IMINA + low(LAB[k])) if im else LAB[k]


def thought(k, im):
    return f"có ý nghĩ “{lab(k, im)}”"                                             # X-ti hoti [new]


def b_item(i, mood, im):
    p = PRED[i][1]
    s = MOOD[mood][0]
    return f"“{cap((IMINA + s) if im else s)} {p}”"


def c_item(i, mood, im, neg):
    p = PRED[i][1]
    s = MOOD[mood][2] if neg else MOOD[mood][1]
    tail = "không giống như thế" if neg else "giống như thế"
    return f"“Người ấy {p} thế nào thì {IMINA.lower() if im else ''}{s} {p} {tail}”"


def join_items(items, shape):
    """shape: 'full' (all 13), 'abbr' (1st, 2nd … last), 'b6' (1st … 10th-13th)"""
    hv = ["hoặc " + x if j else x for j, x in enumerate(items)]
    if shape == "full":
        return ", ".join(hv)
    if shape == "abbr":
        return f"{hv[0]}, {hv[1]}… {hv[12]}"
    if shape == "b6":
        return f"{hv[0]}… {hv[9]}, {hv[10]}, {hv[11]}, {hv[12]}"
    raise KeyError(shape)


PAPANCA = {"asmi": ("itthasmi", "evasmi", "aññathāsmi"), "bhavissaṃ": ("itthaṃ bhavissaṃ", "evaṃ bhavissaṃ",
                                                                        "aññathā bhavissaṃ"),
           "siyaṃ": ("itthaṃ siyaṃ", "evaṃ siyaṃ", "aññathā siyaṃ"),
           "apāhaṃ siyaṃ": ("apāhaṃ itthaṃ siyaṃ", "apāhaṃ evaṃ siyaṃ", "apāhaṃ aññathā siyaṃ")}
KIND = {"asmi": ("A", "pres"), "itthasmi": ("B", "pres"), "evasmi": ("C", "pres"), "aññathāsmi": ("D", "pres"),
        "bhavissaṃ": ("A", "fut"), "itthaṃ bhavissaṃ": ("B", "fut"), "evaṃ bhavissaṃ": ("C", "fut"),
        "aññathā bhavissaṃ": ("D", "fut"), "asasmi": ("E", None), "sātasmi": ("F", None), "siyaṃ": ("A", "pot"),
        "itthaṃ siyaṃ": ("B", "pot"), "evaṃ siyaṃ": ("C", "pot"), "aññathā siyaṃ": ("D", "pot"),
        "apāhaṃ siyaṃ": ("A", "wish"), "apāhaṃ itthaṃ siyaṃ": ("B", "wish"), "apāhaṃ evaṃ siyaṃ": ("C", "wish"),
        "apāhaṃ aññathā siyaṃ": ("D", "wish")}
FIVE_AGG = "đối với vật chất… cảm giác… tri giác… các sự tạo tác… thức"           # rūpaṃ…pe… vedanaṃ… … viññāṇaṃ
UNSPLIT = {False: "Không tách riêng bất cứ hiện tượng nào", True: "Sau khi tách riêng bất cứ hiện tượng nào"}


def tv_def(k, im, shape=None, var="", closing=None):
    """definition after «(n) Và có ý nghĩ “…” như thế nào?»"""
    kind, mood = KIND[k]
    close = closing if closing is not None else f"như vậy là {thought(k, im)}"
    if kind == "A":
        L = lab(k, im)
        p1, p2, p3 = (f"“{lab(x, im)}”" for x in PAPANCA[k])
        return (f"{UNSPLIT[im]}{var}, {FIVE_AGG}, người ta có được ý muốn “{L}”, có được sự kiêu mạn “{L}”, có được "
                f"quan điểm “{L}”. Khi có điều ấy, có những sự suy diễn lan man này {DASH} {p1}, hoặc {p2}, hoặc {p3}.")
    if kind == "E":
        t = "tôi thường còn, tôi bền vững, tôi trường tồn, tôi có bản chất không biến đổi"
        return f"{UNSPLIT[im]}{var}, {FIVE_AGG}, với ý nghĩ “{cap(IMINA + t) if im else cap(t)}” {DASH} {close}."
    if kind == "F":
        t = "tôi sẽ bị đoạn diệt, tôi sẽ bị hủy diệt, tôi sẽ không còn hiện hữu"
        return f"{UNSPLIT[im]}{var}, {FIVE_AGG}, với ý nghĩ “{cap(IMINA + t) if im else cap(t)}” {DASH} {close}."
    if kind == "B":
        items = [b_item(i, mood, im) for i in range(13)]
        return f"{join_items(items, shape)} {DASH} {close}."
    items = [c_item(i, mood, im, kind == "D") for i in range(13)]
    return f"So với người khác{var}: {join_items(items, shape)} {DASH} {close}."


def tv_line(n, k, im, **kw):
    pre = f"({n}) " if n else ""
    return f"{pre}Và {thought(k, im)} như thế nào? {tv_def(k, im, **kw)}"


TV = "dòng khao khát"                                                              # taṇhāvicarita [new]
IN_UP, OUT_UP = "dựa vào phần bên trong", "dựa vào phần bên ngoài"                 # ajjhattikassa / bāhirassa upādāya
GOM = "khi gom tất cả lại làm một và thu tóm lại"                                  # [sample KHANDHA_TOGETHER]
assert GOM in S.KHANDHA_TOGETHER
BRAHMAJALA = "đã được Đức Thế Tôn nói đến trong bài giảng “Lưới Phạm Thiên”"      # brahmajāle veyyākaraṇe … bhagavatā

# ================================================================ 7. the hand lines, in order
H = []   # (key, vi): key = exact heading text ("#…") or the start of the Pāli line


def h(key, vi):
    H.append((key, vi))


def hd(level, pali, vi):
    h("#" * level + " " + pali, "#" * level + " " + vi)


hd(3, "Khuddakavatthuvibhaṅgo", S.CHAPTER_TITLES[17])
hd(4, "Ekakamātikā", "Ma trận bộ một")                                            # [ch16]
h("(1)Jātimado", "MATRIX")
LBL = {1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười"}
CLOSE = {k: f"Phân loại theo nhóm {v}." for k, v in LBL.items()}                 # Ekakaṃ. … [ch16 / pi-1]
h("Ekakaṃ.", CLOSE[1])
for _n, (_g, _b, _k) in enumerate([("Duka", "bộ đôi", "(1) Kodho"), ("Tika", "bộ ba", "(1) Tīṇi"),
                                   ("Catukka", "bộ bốn", "(1) Cattāro"), ("Pañcaka", "bộ năm", "(1) Pañcorambhāgiyāni"),
                                   ("Chakka", "bộ sáu", "(1) Cha"), ("Sattaka", "bộ bảy", "(1) Satta"),
                                   ("Aṭṭhaka", "bộ tám", "(1) Aṭṭha"), ("Navaka", "bộ chín", "(1) Nava"),
                                   ("Dasaka", "bộ mười", "(1) Dasa")], 2):
    hd(5, f"{_g}mātikā", f"Ma trận {_b}")
    h(_k, "MATRIX")
    h(f"{_g}ṃ.", CLOSE[_n])
h("Aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya, aṭṭhārasa",
  f"Mười tám {TV} {IN_UP}, mười tám {TV} {OUT_UP}, {GOM}, thành ba mươi sáu {TV}. Như vậy, ba mươi sáu {TV} thuộc "
  f"quá khứ, ba mươi sáu {TV} thuộc tương lai, ba mươi sáu {TV} thuộc hiện tại, {GOM}, thành một trăm lẻ tám {TV}. "
  f"Và sáu mươi hai quan điểm {BRAHMAJALA}.")
h("Mātikā.", "Ma trận.")

# ---------------------------------------------------------------- Ekakaniddeso
hd(4, "Ekakaniddeso", "Giải thích phân loại theo nhóm một")
hd(5, "(1) Jātimado", "(1) " + cap(N["jātimado"]))
h("Tattha katamo jātimado?", f"{q(N['jātimado'])} Dựa vào {MADA[0][1]} mà có {MADA_SYN}, {MANA_SYN_V} {DASH} "
                             f"{called(N['jātimado'])}.")
hd(5, "(2-27) Gottamadādī", f"(2-27) {cap(N['gottamado'])} và những điều tương tự")
_chain = "… ".join(("Dựa vào " if i == 1 else "dựa vào ") + v for i, (_, v) in enumerate(MADA[1:], 1))
h("Tattha katamo gottamado?", f"{q(N['gottamado'])} {_chain} mà có {MADA_SYN}, {MANA_SYN} {DASH} "
                              f"{called(N['pāripūrimado'])}.")
hd(5, "(28) Mado", "(28) " + cap(MADO))
h("Tattha katamo mado?", f"{q(MADO)} Điều mà là {MADA_SYN}, {MANA_SYN} {DASH} {called(MADO)}.")
hd(5, "(29) Pamādo", "(29) " + cap(N["pamādo"]))
h("Tattha katamo pamādo?", f"{q(N['pamādo'])} {PAMADA_FULL} {DASH} {called(N['pamādo'])}.")
hd(5, "(30) Thambho", "(30) " + cap(N["thambho"]))
THAMBHA_TAIL = "tính thô cứng, tính thô lỗ, sự cao ngạo của tâm, sự không mềm mại"   # kakkhaḷiyaṃ … amudutā [new]
h("Tattha katamo thambho?", f"{q(N['thambho'])} Điều mà là sự cứng đầu, sự khởi cứng đầu, trạng thái khởi cứng đầu, "
                            f"{THAMBHA_TAIL} {DASH} {called(N['thambho'])}.")
hd(5, "(31) Sārambho", "(31) " + cap(N["sārambho"]))
h("Tattha katamo sārambho?", f"{q(N['sārambho'])} Điều mà là sự tranh hơn, sự tranh hơn đáp trả, hành động tranh hơn, "
                             f"hành động tranh hơn đáp trả, trạng thái tranh hơn đáp trả {DASH} "
                             f"{called(N['sārambho'])}.")
for _num, _k in (("32", "atricchatā"), ("33", "mahicchatā")):
    hd(5, f"({_num}) {cap(_k)}", f"({_num}) {cap(N[_k])}")
    h(f"Tattha katamā {_k}?", f"{q(N[_k])} {atri(N[_k])} {DASH} {called(N[_k])}.")
hd(5, "(34) Pāpicchatā", "(34) " + cap(N["pāpicchatā"]))
_PP = [("không có niềm tin", "người có niềm tin"), ("phạm giới", "người giữ giới"), ("ít học hỏi", "người học rộng"),
       ("ưa thích tụ tập", "người sống tách biệt"), ("lười biếng", "người tinh tấn"),
       ("mất tỉnh thức", "người có sự tỉnh thức được thiết lập"), ("không được định tâm", "người được định tâm"),
       ("kém trí tuệ", "người có trí tuệ"), ("chưa diệt tận các ô nhiễm", "người đã diệt tận các ô nhiễm")]
_ppl = ", ".join(f"{a} mà mong muốn “Mong người ta biết tôi là {b}”" for a, b in _PP)
h("Tattha katamā pāpicchatā?", f"{q(N['pāpicchatā'])} {IDHEK} {_ppl} {DASH} {EVA} sự mong muốn, trạng thái bị mong "
                               f"muốn chi phối, {N['pāpicchatā']}, {RAGA3} {DASH} {called(N['pāpicchatā'])}.")
hd(5, "(35) Siṅgaṃ", "(35) " + cap(N["siṅgaṃ"]))
QUANH = "sự quanh co, tính quanh co"                                               # parikkhattatā pārikkhattiyaṃ
h("Tattha katamaṃ siṅgaṃ?", f"{q(N['siṅgaṃ'])} Điều mà là sự kiểu cách, sự điệu đà, sự khôn lỏi, tính khôn lỏi, "
                            f"{QUANH} {DASH} {called(N['siṅgaṃ'])}.")
hd(5, "(36) Tintiṇaṃ", "(36) " + cap(N["tintiṇaṃ"]))
LOLUPPA = "sự ham hố, sự khởi ham hố, trạng thái khởi ham hố, sự xu nịnh, sự mong muốn điều tốt đẹp"   # [pi-1 lobha]
assert LOLUPPA in LOBHA
h("Tattha katamaṃ tintiṇaṃ?", f"{q(N['tintiṇaṃ'])} Điều mà là sự khó tính, sự khởi khó tính, trạng thái khởi khó tính, "
                              f"{LOLUPPA} {DASH} {called(N['tintiṇaṃ'])}.")
hd(5, "(37) Cāpalyaṃ", "(37) " + cap(N["cāpalyaṃ"]))
h("Tattha katamaṃ cāpalyaṃ?", f"{q(N['cāpalyaṃ'])} Sự trang trí y phục, sự trang trí bát, sự trang trí chỗ ở, hoặc sự "
                              f"trang trí, sự tô điểm, sự nâng niu, sự nâng niu khắp nơi cho thân thể hôi thối này hay "
                              f"cho các vật dụng bên ngoài, sự ham thích, tính ham thích, sự nhẹ dạ, sự phù phiếm {DASH} "
                              f"{called(N['cāpalyaṃ'])}.")
hd(5, "(38) Asabhāgavutti", "(38) " + cap(N["asabhāgavutti"]))
DOVAC_TAIL = DOVAC.split(" mà có ")[1]                                             # sự khó bảo, … sự không vâng lời
REVERSE = DOVAC_TAIL[DOVAC_TAIL.index("sự tiếp nhận ngang trái"):]
assert REVERSE == ("sự tiếp nhận ngang trái, sự thích thú việc làm trái, sự thiếu tôn trọng, thái độ thiếu tôn trọng, "
                   "sự thiếu kính trọng, sự không vâng lời"), REVERSE
h("Tattha katamaṃ asabhāgavutti?", f"{q(N['asabhāgavutti'])} Đối với mẹ, hoặc cha, hoặc người lớn tuổi hơn, hoặc anh "
                                   f"em, hoặc các vị thầy, hoặc thầy tế độ, hoặc Đức Phật, hoặc các đệ tử, hoặc bất kỳ "
                                   f"người nào đáng kính trọng, {REVERSE} {DASH} {called(N['asabhāgavutti'])}.")
hd(5, "(39) Arati", "(39) " + cap(N["arati"]))
ARATI = (f"{q(N['arati'])} Đối với những chỗ ở xa vắng, hoặc đối với các hiện tượng thiện cao hơn này hay khác, sự không "
         f"hoan hỷ, trạng thái không hoan hỷ, sự không thích thú, sự không ưa thích, sự chán chường, sự bồn chồn {DASH} "
         f"{called(N['arati'])}.")
h("Tattha katamā arati?", ARATI)
hd(5, "(40) Tandī", "(40) " + cap(N["tandī"]))
h("Tattha katamā tandī?", f"{q(N['tandī'])} Điều mà là sự lười nhác, sự khởi lười nhác, tâm trạng lười nhác, sự biếng "
                          f"trễ, sự khởi biếng trễ, trạng thái khởi biếng trễ {DASH} {called(N['tandī'])}.")
hd(5, "(41) Vijambhitā", "(41) " + cap(N["vijambhitā"]))
h("Tattha katamā vijambhitā?", f"{q(N['vijambhitā'])} Điều mà là sự vươn mình, sự vươn mình mạnh, sự cúi xuống, sự ngả "
                               f"ra, sự co lại, sự nghiêng người, sự uể oải như bệnh của thân {DASH} "
                               f"{called(N['vijambhitā'])}.")
hd(5, "(42) Bhattasammado", "(42) " + cap(N["bhattasammado"]))
h("Tattha katamo bhattasammado?", f"{q(N['bhattasammado'])} Điều mà là sự lịm người vì bữa ăn, sự mệt mỏi vì bữa ăn, sự "
                                  f"nóng nực vì bữa ăn, sự nặng nề của thân ở người đã ăn xong {DASH} "
                                  f"{called(N['bhattasammado'])}.")
hd(5, "(43) Cetaso ca līnattaṃ", "(43) " + cap(N["cetaso ca līnattaṃ"]))
LINATTA = f"{q(N['cetaso ca līnattaṃ'])} {THINA_BODY} {DASH} {called(N['cetaso ca līnattaṃ'])}."
h("Tattha katamaṃ cetaso ca līnattaṃ?", LINATTA)
hd(5, "(44) Kuhanā", "(44) " + cap(N["kuhanā"]))
h("Tattha katamā kuhanā?", f"{q(N['kuhanā'])} {KUHA}, bằng điều gọi là việc thọ dụng các vật dụng{VAR_PACCAYA}, hoặc "
                           f"bằng lời nói bóng gió, hoặc là sự sắp đặt tư thế{VAR_ATHAPANA}, sự bày đặt, sự dàn dựng, "
                           f"sự nhăn mặt, vẻ nhăn mặt, sự lừa gạt, sự khởi lừa gạt, trạng thái khởi lừa gạt {DASH} "
                           f"{called(N['kuhanā'])}.")
hd(5, "(45) Lapanā", "(45) " + cap(N["lapanā"]))
h("Tattha katamā lapanā?", f"{q(N['lapanā'])} {KUHA}, điều mà là sự bắt chuyện với người khác, sự nói ngọt, sự trò "
                           f"chuyện thân mật, sự tâng bốc, sự tâng bốc hết mức, sự bợ đỡ, sự bợ đỡ hết mức, sự gợi "
                           f"lòng, sự gợi lòng hết mức, sự nói lời chiều lòng, {LAPA3} {DASH} {called(N['lapanā'])}.")
hd(5, "(46) Nemittikatā", "(46) " + cap(N["nemittikatā"]))
h("Tattha katamā nemittikatā?", f"{q(N['nemittikatā'])} {KUHA}, điều mà là sự ra dấu với người khác, việc ra dấu, sự "
                                f"gợi ý, việc gợi ý, lời nói bóng gió, lời nói vòng vo {DASH} "
                                f"{called(N['nemittikatā'])}.")
hd(5, "(47) Nippesikatā", "(47) " + cap(N["nippesikatā"]))
h("Tattha katamā nippesikatā?", f"{q(N['nippesikatā'])} {KUHA}, điều mà là sự mắng nhiếc người khác, sự khinh miệt, sự "
                                f"chê trách, sự chế giễu, sự chế giễu hết mức, sự nhạo báng, sự nhạo báng hết mức, sự "
                                f"bêu xấu, sự bêu xấu hết mức, sự loan truyền tiếng xấu, sự nói xấu sau lưng {DASH} "
                                f"{called(N['nippesikatā'])}.")
hd(5, "(48) Lābhena lābhaṃ nijigīsanatā", "(48) " + cap(N["lābhena lābhaṃ nijigīsanatā"]))
h("Tattha katamā lābhena lābhaṃ nijigīsanatā?",
  f"{q(N['lābhena lābhaṃ nijigīsanatā'])} Người bám vào {SILOKA}, có ước muốn xấu xa, bị ước muốn chi phối, mang vật "
  f"phẩm nhận được ở chỗ này đến chỗ kia, hoặc mang vật phẩm nhận được ở chỗ kia về chỗ này, {EVA} sự kiếm tìm, sự lùng "
  f"tìm, sự kiếm tìm khắp nơi, sự tìm cầu, sự lùng kiếm, sự tìm cầu khắp nơi vật phẩm {DASH} "
  f"{called(N['lābhena lābhaṃ nijigīsanatā'])}.")
# conceit 49 … 60
_MH = [("49", "seyyohamasmīti māno", "plain", "māna", None), ("50", "sadisohamasmīti māno", "plain", "māna", None),
       ("51", "hīnohamasmīti māno", "plain", "omāna", None)]
for _w, _wp in (("seyyassa", "vốn hơn người"), ("sadisassa", "vốn bằng người"), ("hīnassa", "vốn kém người")):
    for _o, _ov in (("seyyo", "hơn"), ("sadiso", "bằng"), ("hīno", "kém")):
        _MH.append((None, f"{_w} {_o}hamasmīti māno", _wp, "omāna" if _o == "hīno" else "māna", _ov))
for _i, (_num, _k, _who, _kind, _ov) in enumerate(_MH):
    _num = _num or str(49 + _i)
    hd(5, f"({_num}) {cap(_k)}", f"({_num}) {cap(N[_k])}")
    if _who == "plain":
        _syn = (MANA_SYN if _kind == "māna" else OMANA_SYN)
        _gen = "sự kiêu mạn" if _kind == "māna" else "sự tự ti"
        _l = mlist(VAR_VIJJA if _num == "49" else "")
        _body = f"{IDHEK}, dựa vào {_l}, nuôi dưỡng {_gen}, {EVA} {_syn}"
    else:
        _pe = int(_num) >= 55
        _pal = _k.split()[1][:-len("hamasmīti")]                                 # seyyo / sadiso / hīno (attānaṃ)
        _dahati = {"seyyo": "hơn", "sadiso": "bằng", "hīno": "kém"}[_pal]
        if _num == "60":
            _dahati = "bằng"                                                       # as written: "parehi sadisaṃ"
            SLIPS.append("^2-877 'hīnassa hīnohamasmīti māno' defined with 'parehi sadisaṃ attānaṃ dahati' (the "
                         "parallels have hīnaṃ): as written «tự cho mình bằng người khác»")
        _gen = "sự kiêu mạn" if _kind == "māna" else "sự tự ti"
        _syn = (MANA_SYN if _kind == "māna" else OMANA_SYN)
        if _num == "55":
            _syn = MANA_SYN_PE
        _body = (f"{IDHEK} {_who} về {mlist(pe=_pe)}, tự cho mình {_dahati} người khác; dựa vào điều ấy, người ấy nuôi "
                 f"dưỡng {_gen}. {cap(EVA)} {_syn}")
    h(f"Tattha katamo {_k}?", f"{q(N[_k])} {_body} {DASH} {called(N[_k])}.")
hd(5, "(61) Māno", "(61) " + cap(N["māno"]))
h("Tattha katamo māno?", f"{q(N['māno'])} Điều mà là {MANA_SYN} {DASH} {called(N['māno'])}.")
hd(5, "(62) Atimāno", "(62) " + cap(N["atimāno"]))
h("Tattha katamo atimāno?", f"{q(N['atimāno'])} {IDHEK}, dựa vào {mlist(pe=True)}, tự cho mình vượt trên người khác. "
                            f"{cap(EVA)} {MANA_SYN} {DASH} {called(N['atimāno'])}.")
hd(5, "(63) Mānātimāno", "(63) " + cap(N["mānātimāno"]))
h("Tattha katamo mānātimāno?", f"{q(N['mānātimāno'])} {IDHEK}, dựa vào {mlist(pe=True)}, lúc trước tự cho mình bằng "
                               f"người khác, lúc sau tự cho mình là hơn. {cap(EVA)} {MANA_SYN} {DASH} "
                               f"{called(N['mānātimāno'])}.")
hd(5, "(64) Omāno", "(64) " + cap(N["omāno"]))
h("Tattha katamo omāno?", f"{q(N['omāno'])} {IDHEK}, dựa vào {mlist()}, nuôi dưỡng sự tự ti. {cap(EVA)} {OMANA_SYN} "
                          f"{DASH} {called(N['omāno'])}.")
hd(5, "(65) Adhimāno", "(65) " + cap(N["adhimāno"]))
h("Tattha katamo adhimāno?", f"{q(N['adhimāno'])} Tri giác điều chưa đạt được là đã đạt được, tri giác điều chưa làm là "
                             f"đã làm, tri giác điều chưa chứng đắc là đã chứng đắc, tri giác điều chưa chứng nghiệm là "
                             f"đã chứng nghiệm, {EVA} {MANA_SYN} {DASH} {called(N['adhimāno'])}.")
hd(5, "(66) Asmimāno", "(66) " + cap(N["asmimāno"]))
_TA = "sự kiêu mạn “Tôi là”, ý muốn “Tôi là”, khuynh hướng tiềm ẩn “Tôi là”"
h("Tattha katamo asmimāno?", f"{q(N['asmimāno'])} Đối với vật chất, {_TA}, đối với cảm giác… tri giác… các sự tạo tác… "
                             f"đối với thức, {_TA}, {EVA} {MANA_SYN} {DASH} {called(N['asmimāno'])}.")
hd(5, "(67) Micchāmāno", "(67) " + cap(N["micchāmāno"]))
_BAD = ["ngành nghề", "ngành thủ công", "lĩnh vực học thuật", "sự học hỏi", "tài ứng đáp", "giới hạnh", "nghi thức",
        "giới hạnh và nghi thức", "quan điểm"]
_badl = ", hoặc ".join(f"{x} xấu ác" for x in _BAD)
h("Tattha katamo micchāmāno?", f"{q(N['micchāmāno'])} {IDHEK}, dựa vào {_badl}, hoặc {OTHERV}, nuôi dưỡng sự kiêu mạn, "
                               f"{EVA} {MANA_SYN} {DASH} {called(N['micchāmāno'])}.")
for _num, _k, _obj in (("68", "ñātivitakko", "người thân"), ("69", "janapadavitakko", "xứ sở")):
    hd(5, f"({_num}) {cap(_k)}", f"({_num}) {cap(N[_k])}")
    h(f"Tattha katamo {_k}?", f"{q(N[_k])} {SUY} {GEH} liên quan đến {_obj}, {TAKKA} {DASH} {called(N[_k])}.")
hd(5, "(70) Amaravitakko", "(70) " + cap(N["amaravitakko"]))
h("Tattha katamo amaravitakko?", f"{q(N['amaravitakko'])} {SUY} {GEH}, liên quan đến việc thực hành khổ hạnh hoặc liên "
                                 f"quan đến các quan điểm, {TAKKA} {DASH} {called(N['amaravitakko'])}.")
hd(5, "(71) Parānuddayatāpaṭisaṃyutto vitakko", "(71) " + cap(N["parānuddayatāpaṭisaṃyutto vitakko"]))
h("Tattha katamo parānuddayatāpaṭisaṃyutto vitakko?",
  f"{q(N['parānuddayatāpaṭisaṃyutto vitakko'])} {IDHEK} sống giao du với người tại gia, vui cùng họ, buồn cùng họ, hạnh "
  f"phúc khi họ hạnh phúc, khổ khi họ khổ, khi có những việc cần làm thì tự mình dấn thân vào. Điều mà, ở đó, là suy "
  f"nghĩ {GEH}, {TAKKA} {DASH} {called(N['parānuddayatāpaṭisaṃyutto vitakko'])}.")
hd(5, "(72) Lābhādipaṭisaṃyutto vitakko", f"(72) Sự hướng tâm liên quan đến lợi lộc và những điều tương tự")
h("Tattha katamo lābhasakkārasilokapaṭisaṃyutto vitakko?",
  f"{q(N['lābhasakkārasilokapaṭisaṃyutto vitakko'])} {SUY} {GEH} liên quan đến {SILOKA}, {TAKKA} {DASH} "
  f"{called(N['lābhasakkārasilokapaṭisaṃyutto vitakko'])}.")
hd(5, "(73) Anavaññattipaṭisaṃyutto vitakko", "(73) " + cap(N["anavaññattipaṭisaṃyutto vitakko"]))
h("Tattha katamo anavaññattipaṭisaṃyutto vitakko?",
  f"{q(N['anavaññattipaṭisaṃyutto vitakko'])} {IDHEK}, dựa vào {mlist()}, mong rằng “Người khác đừng xem nhẹ tôi”. "
  f"Điều mà, ở đó, là suy nghĩ {GEH}, {TAKKA} {DASH} {called(N['anavaññattipaṭisaṃyutto vitakko'])}.")
h("Ekakaṃ.", CLOSE[1])

# ---------------------------------------------------------------- Dukaniddeso
hd(4, "Dukaniddeso", "Giải thích phân loại theo nhóm hai")


def duka_head(n, a, b):
    pali = cap(duka_p(a, b))
    hd(5, f"({n}) {pali}", f"({n}) {cap(N[strip_ca(a)])} và {N[strip_ca(b)]}")


def ka(letter, pali_name, vi_body, name=None, quoted=True, idam=False):
    nm = N[pali_name] if name is None else name
    end = called(nm) if quoted else f"đó được gọi là {nm}"
    return f"({letter}) {q(nm, lower=True)} {vi_body} {DASH} {end}."


duka_head(1, "kodho", "upanāho")
h("(Ka) tattha katamo kodho?", ka("a", "kodho", f"Điều mà là {KODHA_SYN}"))
h("(Kha) tattha katamo upanāho?", ka("b", "upanāho", f"Lúc trước là sự giận dữ, lúc sau là sự ôm hận. {cap(EVA)} sự ôm "
                                                     f"hận, sự khởi ôm hận, trạng thái khởi ôm hận, sự lưu giữ, sự giữ "
                                                     f"lại, sự giữ chặt, sự nối kết, sự kéo dài liên tục, sự làm cho bền "
                                                     f"chặt của sự giận dữ"))
duka_head(2, "makkho", "paḷāso")
h("(Ka) tattha katamo makkho?", ka("a", "makkho", f"Điều mà là sự gièm pha, sự khởi gièm pha, trạng thái khởi gièm "
                                                  f"pha{VAR_MAKKHA}, sự khắc nghiệt, hành động khắc nghiệt"))
h("(Kha) tattha katamo paḷāso?", ka("b", "paḷāso", f"Điều mà là sự ganh đua, sự khởi ganh đua{VAR_PALASA}, sự ôm giữ "
                                                   f"sự ganh đua, chỗ phát sinh tranh cãi, sự đòi ngang hàng, sự không "
                                                   f"chịu buông bỏ"))
duka_head(3, "issā", "macchariyañca")
_ISSA_B = ISSA                                                                     # Điều mà, trước lợi lộc, … đố kỵ
_ISSA_B = _ISSA_B.replace(" [khác chính tả (Ka.): ussuyā ussuyanā ussuyitattaṃ]", "")
h("(Ka) tattha katamā issā?", ka("a", "issā", _ISSA_B))
h("(Kha) tattha katamaṃ macchariyaṃ?", ka("b", "macchariyaṃ", MACCH_V))
duka_head(4, "māyā", "sāṭheyyañca")
_MJ = "“Mong đừng ai biết về tôi”"
h("(Ka) tattha katamā māyā?",
  ka("a", "māyā", f"{IDHEK}, sau khi làm hành vi xấu bằng thân, sau khi làm hành vi xấu bằng lời nói, sau khi làm hành vi "
                  f"xấu bằng ý, vì muốn che giấu điều ấy mà đặt ra ước muốn xấu xa. Người ấy mong muốn: {_MJ}. Người ấy "
                  f"suy tính: {_MJ}. Người ấy nói lời: {_MJ}. Người ấy hành động bằng thân: {_MJ}. {cap(EVA)} sự xảo "
                  f"trá, tính xảo trá, sự lấn lướt, sự lừa dối, sự gian lận, sự đánh lạc hướng, sự lảng tránh, sự giấu "
                  f"giếm, sự giấu giếm kỹ, sự che đậy, sự che đậy kỹ, sự không bày tỏ, sự không bộc lộ, sự che đậy hoàn "
                  f"toàn, việc làm điều xấu ác"))
h("(Kha) tattha katamaṃ sāṭheyyaṃ?",
  ka("b", "sāṭheyyaṃ", f"{IDHEK} gian trá, rất gian trá. Điều mà, ở đó, là sự gian trá, tính gian trá, sự gian xảo, sự xảo "
                       f"quyệt, tính xảo quyệt{VAR_KAKKARA}, {QUANH}"))
duka_head(5, "avijjā", "bhavataṇhā")
h("(Ka) tattha katamā avijjā?", ka("a", "avijjā", AVIJJA_PE))
h("(Kha) tattha katamā bhavataṇhā?", ka("b", "bhavataṇhā", BHAVASAVA))
duka_head(6, "bhavadiṭṭhi", "vibhavadiṭṭhi")
for _l, _k, _p in (("Ka", "bhavadiṭṭhi", "Bhavissati"), ("Kha", "vibhavadiṭṭhi", "Na bhavissati")):
    _qv, _view = DIT_Q[_k]
    h(f"({_l}) tattha katamā {_k}?", ka({"Ka": "a", "Kha": "b"}[_l], _k, f"{_view} {DASH} {DITTHI_PE}",
                                         quoted=_k != "vibhavadiṭṭhi"))
SLIPS.append("^2-896 (Kha) 'ayaṃ vuccati vibhavadiṭṭhi' without quotes (the parallels quote): kept unquoted")
duka_head(7, "sassatadiṭṭhi", "ucchedadiṭṭhi")
duka_head(8, "antavādiṭṭhi", "anantavādiṭṭhi")
duka_head(9, "pubbantānudiṭṭhi", "aparantānudiṭṭhi")
for _l, _k, _pk in (("Ka", "sassatadiṭṭhi", "sassatadiṭṭhi"), ("Kha", "ucchedadiṭṭhi", "ucchedadiṭṭhi"),
                    ("Ka", "antavādiṭṭhi", "antavā diṭṭhi"), ("Kha", "anantavādiṭṭhi", "anantavā diṭṭhi")):
    _qv, _view = DIT_Q[_pk]
    h(f"({_l}) tattha katamā {_k}?", ka({"Ka": "a", "Kha": "b"}[_l], _k, f"{_view} {DASH} {DITTHI_PE}"))
for _l, _k, _t in (("Ka", "pubbantānudiṭṭhi", "quá khứ"), ("Kha", "aparantānudiṭṭhi", "tương lai")):
    h(f"({_l}) tattha katamā {_k}?", ka({"Ka": "a", "Kha": "b"}[_l], _k, f"Điều mà sinh khởi liên quan đến {_t} là quan "
                                                                         f"điểm, sự mắc kẹt trong các quan điểm… sự nắm "
                                                                         f"giữ điều đảo ngược"))
    assert DIT_Q[_k][1] == "Điều mà sinh khởi liên quan đến " + _t + " là quan điểm, sự mắc kẹt trong các quan điểm… " \
                                                                     "sự nắm giữ điều đảo ngược", DIT_Q[_k]
# the three lines above for (7)-(9) are interleaved with their headings: rebuild the order
_tail = H[-6:]
del H[-9:]
duka_head(7, "sassatadiṭṭhi", "ucchedadiṭṭhi")
H.extend(_tail[0:2])
duka_head(8, "antavādiṭṭhi", "anantavādiṭṭhi")
H.extend(_tail[2:4])
duka_head(9, "pubbantānudiṭṭhi", "aparantānudiṭṭhi")
H.extend(_tail[4:6])
duka_head(10, "ahirikañca", "anottappañca")
h("(Ka) tattha katamaṃ ahirikaṃ?", ka("a", "ahirikaṃ", AHIRI))
h("(Kha) tattha katamaṃ anottappaṃ?", ka("b", "anottappaṃ", ANOTT))
duka_head(11, "dovacassatā", "pāpamittatā")
h("(Ka) tattha katamā dovacassatā?", ka("a", "dovacassatā", DOVAC))
assert PAPAM.endswith(", sự nghiêng về phía họ"), PAPAM
PAPAM_901 = PAPAM[:-len(", sự nghiêng về phía họ")] + ", sự nghiêng theo"       # sampavaṅkatā (no taṃ-), as written
h("(Kha) tattha katamā pāpamittatā?", ka("b", "pāpamittatā", PAPAM_901))
SLIPS.append("^2-901 'bhatti sambhatti sampavaṅkatā' (pi-1 and ^2-U12: taṃsampavaṅkatā): as written «sự nghiêng theo»")
duka_head(12, "anajjavo", "amaddavo")
h("(Ka) tattha katamo anajjavo?", ka("a", "anajjavo", "Điều mà là sự không ngay thật, tính không ngay thật, sự quanh co, "
                                                      "sự cong queo, sự vặn vẹo"))
h("(Kha) tattha katamo amaddavo?", ka("b", "amaddavo", f"Điều mà là sự không mềm mại, sự không mềm mỏng, tính thô cứng, "
                                                       f"tính thô lỗ, sự thô cứng, sự cứng nhắc{VAR_KATHINA}, sự cao ngạo "
                                                       f"của tâm, sự không mềm mại"))
duka_head(13, "akkhanti", "asoraccañca")
h("(Ka) tattha katamā akkhanti?", ka("a", "akkhanti", "Điều mà là sự không nhẫn nại, sự không bao dung, sự không chịu "
                                                      "đựng, sự hung dữ, sự nói năng cộc cằn, sự không hài lòng của tâm"))
h("(Kha) tattha katamaṃ asoraccaṃ?", ka("b", "asoraccaṃ", VITIKKAMA) + " Mọi sự phạm giới đều là sự không hiền hòa.")
duka_head(14, "asākhalyañca", "appaṭisanthāro")
h("(Ka) tattha katamaṃ asākhalyaṃ?",
  ka("a", "asākhalyaṃ", "Một người nói lời như thế, tức lời gai góc, cay nghiệt, làm người khác đau lòng, xúc phạm người "
                        "khác, gần với sự giận dữ, không đưa đến định tâm. Điều mà, ở đây, là sự không dịu dàng trong "
                        "lời nói, sự không hòa nhã trong lời nói, sự thô ác trong lời nói"))
h("(Kha) tattha katamo appaṭisanthāro",
  f"(b) ở đây, {N['appaṭisanthāro']}{VAR_SANDHARA} là gì? Có hai loại niềm nở tiếp đón {DASH} niềm nở tiếp đón bằng vật "
  f"phẩm và niềm nở tiếp đón bằng Giáo Pháp. {IDHEK} không niềm nở tiếp đón bằng vật phẩm hoặc bằng Giáo Pháp {DASH} "
  f"{called(N['appaṭisanthāro'])}.")
assert "Có hai loại niềm nở tiếp đón " + DASH + " niềm nở tiếp đón bằng vật phẩm và niềm nở tiếp đón bằng Giáo Pháp." \
       in pv(F403, "Tattha katamo paṭisanthāro?")
duka_head(15, "indriyesu aguttadvāratā", "bhojane amattaññutā")
h("(Ka) tattha katamā indriyesu aguttadvāratā?", ka("a", "indriyesu aguttadvāratā", INDRI))
h("(Kha) tattha katamā bhojane amattaññutā?", ka("b", "bhojane amattaññutā", BHOJ))
SLIPS.append("^2-905 '\"bhojane amattaññutā.\"' (full stop inside the quote): punctuation only")
duka_head(16, "muṭṭhassaccañca", "asampajaññañca")
h("(Ka) tattha katamaṃ muṭṭhassaccaṃ?", ka("a", "muṭṭhassaccaṃ", MUTTH))
h("(Kha) tattha katamaṃ asampajaññaṃ?", ka("b", "asampajaññaṃ", ASAMP))
duka_head(17, "sīlavipatti", "diṭṭhivipatti")
h("(Ka) tattha katamā sīlavipatti?", ka("a", "sīlavipatti", SILAVIP) +
  " Mọi sự phạm giới đều là sự suy đồi về giới hạnh.")
_NAT_PE = ("“Không có sự bố thí, không có sự cúng tế… những người đã tự mình hiểu biết trực tiếp, chứng nghiệm thế "
           "gian này và thế gian khác rồi tuyên bố”")
assert NATTHI.startswith("“Không có sự bố thí, không có sự cúng tế,") and NATTHI.endswith(_NAT_PE.split("… ")[1])
h("(Kha) tattha katamā diṭṭhivipatti?", ka("b", "diṭṭhivipatti", f"{_NAT_PE} {DASH} {DITTHI_PE}") +
  " Mọi quan điểm sai lầm đều là sự suy đồi về quan điểm.")
duka_head(18, "ajjhattasaṃyojanañca", "bahiddhāsaṃyojanañca")
h("(Ka) tattha katamaṃ ajjhattasaṃyojanaṃ?",
  f"(a) {q(N['ajjhattasaṃyojanaṃ'], lower=True)} {cap(g(5, 'orambhāgiya'))} {DASH} là {N['ajjhattasaṃyojanaṃ']}. "
  f"(b) {g(5, 'uddhambhāgiya')} {DASH} là {N['bahiddhāsaṃyojanaṃ']}.")
h("Dukaṃ.", CLOSE[2])

# ---------------------------------------------------------------- Tikaniddeso
hd(4, "Tikaniddeso", "Giải thích phân loại theo nhóm ba")


def tq(pali_q, vi_name, answer):
    h(f"Tattha katam{pali_q}", f"{q(vi_name)} {answer}")


hd(5, "(1) Tīṇi akusalamūlāni", "(1) " + cap(g(3, "akusalamūla")))
tq("āni tīṇi akusalamūlāni?", g(3, "akusalamūla"), "Sự tham lam, sự sân hận, sự si mê.")
h("(Ka) tattha katamo lobho?", ka("a", None, LOBHA, name="sự tham lam"))
h("(Kha) tattha katamo doso?", ka("b", None, DOSA_PI1, name="sự sân hận"))
h("(Ga) tattha katamo moho?", ka("c", None, f"{MOHA_OPEN}; {EVA} {MOHA_PE}", name="sự si mê") +
  f" Đây là {g(3, 'akusalamūla')}.")
VIT = {"kāma": "dục lạc", "byāpāda": "ác ý", "vihiṃsā": "sự hãm hại"}               # [ch3 paṭisaṃyutta objects]
VITN = {k: f"sự hướng tâm đến {v}" for k, v in VIT.items()}
SANN = {k: f"tri giác về {v}" for k, v in VIT.items()}
DHAT = {"kāma": "yếu tố dục lạc", "byāpāda": "yếu tố ác ý", "vihiṃsā": "yếu tố hãm hại"}   # [ch3]
in_out("3-dhatuvibhango.md", "yếu tố dục lạc", "yếu tố ác ý", "yếu tố hãm hại")
_ABC = ("a", "b", "c")
_KKG = ("Ka", "Kha", "Ga")
hd(5, "(2) Tayo akusalavitakkā", "(2) " + cap(g(3, "akusalavitakka")))
tq("e tayo akusalavitakkā?", g(3, "akusalavitakka"), ", ".join(cap(VITN[k]) if i == 0 else VITN[k]
                                                                for i, k in enumerate(VIT)) + ".")


def vitakka_lines(close):
    for i, k in enumerate(VIT):
        line = ka(_ABC[i], None, f"{SUY} liên quan đến {VIT[k]}, {TAKKA}", name=VITN[k])
        if i == 2:
            line += f" {close}"
        h(f"({_KKG[i]}) tattha katamo {k}vitakko?", line)


vitakka_lines(f"Đây là {g(3, 'akusalavitakka')}.")
hd(5, "(3) Tisso akusalasaññā", "(3) " + cap(g(3, "akusalasaññā")))
tq("ā tisso akusalasaññā?", g(3, "akusalasaññā"), ", ".join(cap(SANN[k]) if i == 0 else SANN[k]
                                                             for i, k in enumerate(VIT)) + ".")
for _i, _k in enumerate(VIT):
    _line = ka(_ABC[_i], None, f"{cap(SANNA_SYN.replace('tri giác', 'tri giác liên quan đến ' + VIT[_k], 1))}",
               name=SANN[_k])
    if _i == 2:
        _line += f" Đây là {g(3, 'akusalasaññā')}."
    h(f"({_KKG[_i]}) tattha katamā {_k}saññā?", _line)
hd(5, "(4) Tisso akusaladhātuyo", "(4) " + cap(g(3, "akusaladhātu")))
tq("ā tisso akusaladhātuyo?", g(3, "akusaladhātu"), ", ".join(cap(DHAT[k]) if i == 0 else DHAT[k]
                                                               for i, k in enumerate(VIT)) + ".")
h("Tattha katamā kāmadhātu?", f"{q(DHAT['kāma'])} " + " ".join(f"{cap(VITN[k])} là {DHAT[k]}." for k in VIT))
vitakka_lines(f"Đây là {g(3, 'akusaladhātu')}.")
hd(5, "(5) Tīṇi duccaritāni", "(5) " + cap(g(3, "duccarita")))
DUC = {"kāya": "hành vi xấu bằng thân", "vacī": "hành vi xấu bằng lời nói", "mano": "hành vi xấu bằng ý"}   # [ch16]
in_out("16-nanavibhango.md", *DUC.values())
KAMMA = {"kāya": "nghiệp bất thiện bằng thân", "vacī": "nghiệp bất thiện bằng lời nói", "mano": "nghiệp bất thiện bằng ý"}
CET = {"kāya": "sự cố ý bất thiện bằng thân", "vacī": "sự cố ý bất thiện bằng lời nói",
       "mano": "sự cố ý bất thiện bằng ý"}                                         # [ch6 sañcetanā words]
in_out("6-paticcasamuppadavibhango.md", "Sự cố ý bằng thân", "sự cố ý bằng lời nói")
PANA3 = ["việc sát hại sinh mạng", "việc lấy của không được cho", "hành vi sai trái trong các dục lạc"]   # [ch4 / ch14]
VACI4 = ["việc nói dối", "lời nói chia rẽ", "lời nói thô ác", "việc nói lời phù phiếm"]
MANO3 = ["sự thèm muốn", "ác ý", "quan điểm sai lầm"]
in_out("4-saccavibhango.md", "việc nói lời phù phiếm", "việc sát hại sinh mạng")
tq("āni tīṇi duccaritāni?", g(3, "duccarita"), ", ".join(cap(DUC[k]) if i == 0 else DUC[k]
                                                          for i, k in enumerate(DUC)) + ".")
h("(Ka) tattha katamaṃ kāyaduccaritaṃ?", ka("a", None, cap(", ".join(PANA3)), name=DUC["kāya"]))
h("(Kha) tattha katamaṃ vacīduccaritaṃ?", ka("b", None, cap(", ".join(VACI4)), name=DUC["vacī"]))
h("(Ga) tattha katamaṃ manoduccaritaṃ?", ka("c", None, cap(", ".join(MANO3)), name=DUC["mano"]))
h("(Ka-ga) tattha katamaṃ kāyaduccaritaṃ?", f"(a-c) {q(DUC['kāya'], lower=True)} " +
  ", ".join((cap(KAMMA[k]) if i == 0 else KAMMA[k]) + f" là {DUC[k]}" for i, k in enumerate(DUC)) + ".")
h("Tattha katamaṃ akusalaṃ kāyakammaṃ?", f"{q(KAMMA['kāya'])} " +
  ", ".join((cap(CET[k]) if i == 0 else CET[k]) + f" là {KAMMA[k]}" for i, k in enumerate(DUC)) +
  f". Đây là {g(3, 'duccarita')}.")
hd(5, "(6) Tayo āsavā", "(6) " + cap(g(3, "āsava")))
ASAV = {"kāma": "ô nhiễm dục lạc", "bhava": "ô nhiễm hiện hữu", "diṭṭhi": "ô nhiễm quan điểm", "avijjā": "ô nhiễm vô minh"}
tq("e tayo āsavā?", g(3, "āsava"), f"{cap(ASAV['kāma'])}, {ASAV['bhava']}, {ASAV['avijjā']}.")
BHAVASAVA_PE = "Điều mà, đối với sự hiện hữu, là ý muốn hiện hữu… sự đắm chìm trong hiện hữu"
KAMA_PE = "Điều mà, đối với các dục lạc, là ý muốn dục lạc… sự đắm chìm trong dục lạc"
assert BHAVASAVA.startswith(BHAVASAVA_PE.split("…")[0]) and BHAVASAVA.endswith(BHAVASAVA_PE.split("… ")[1])
assert KAMASAVA.startswith(KAMA_PE.split("…")[0]) and KAMASAVA.endswith(KAMA_PE.split("… ")[1])
h("(Ka) tattha katamo kāmāsavo?", ka("a", None, KAMASAVA, name=ASAV["kāma"]))
h("(Kha) tattha katamo bhavāsavo?", ka("b", None, BHAVASAVA_PE, name=ASAV["bhava"]))
MOHA_PE2 = "Sự không biết về khổ đau… then cài vô minh, sự si mê, tức gốc rễ bất thiện"
h("(Ga) tattha katamo avijjāsavo?", ka("c", None, MOHA_PE2, name=ASAV["avijjā"]) + f" Đây là {g(3, 'āsava')}.")
hd(5, "(7) Tīṇi saṃyojanāni", "(7) " + cap(g(3, "saṃyojana")))
S3 = ["quan điểm về tự ngã", "sự hoài nghi", "sự hiểu sai lệch về giới hạnh và nghi thức"]   # [pi-1 ^1-1007 …]
tq("āni tīṇi saṃyojanāni?", g(3, "saṃyojana"), cap(", ".join(S3)) + ".")
h("(Ka) tattha katamā sakkāyadiṭṭhi?", ka("a", None, SAKKAYA_D, name=S3[0]))
h("(Kha) tattha katamā vicikicchā?", ka("b", None, f"{VICI_OPEN} {VICI_SHORT}", name=S3[1]))
h("(Ga) tattha katamo sīlabbataparāmāso?", ka("c", None, f"{SILABBATA_Q} {DASH} {DITTHI_PE}", name=S3[2]) +
  f" Đây là {g(3, 'saṃyojana')}.")
hd(5, "(8) Tisso taṇhā", "(8) " + cap(g(3, "taṇhā")))
TAN = {"kāma": "khao khát dục lạc", "bhava": "khao khát được hiện hữu", "vibhava": "khao khát không còn hiện hữu",
       "rūpa": "khao khát cõi hình sắc", "arūpa": "khao khát cõi không hình sắc", "nirodha": "khao khát sự chấm dứt"}
for _v in TAN.values():
    assert _v in LOBHA, _v                                                         # [pi-1 lobha list]
tq("ā tisso taṇhā?", g(3, "taṇhā"), f"{cap(TAN['kāma'])}, {TAN['bhava']}, {TAN['vibhava']}.")


def raga(with_):
    return f"{cap(RAGA3)} {with_}"


BHAVA_D = "có quan điểm về sự hiện hữu đi kèm"
UCCH_D = "có quan điểm về sự đoạn diệt đi kèm"
DHL = {"kāma": "liên quan đến cõi dục lạc", "rūpa": "liên quan đến cõi hình sắc",
       "arūpa": "liên quan đến cõi không hình sắc", "rūpārūpa": "liên quan đến cõi hình sắc và cõi không hình sắc"}
h("Tattha katamā bhavataṇhā?", f"{q(TAN['bhava'])} {raga(BHAVA_D)} {DASH} {called(TAN['bhava'])}.")
h("Tattha katamā vibhavataṇhā?", f"{q(TAN['vibhava'])} {raga(UCCH_D)} {DASH} {called(TAN['vibhava'])}. Khao khát còn "
                                 f"lại là khao khát dục lạc.")
h("Tattha katamā kāmataṇhā?", f"{q(TAN['kāma'])} {raga(DHL['kāma'])} {DASH} {called(TAN['kāma'])}.")
h("( ) [(tattha katamā bhavataṇhā)]", f"( ) [(ở đây, khao khát được hiện hữu là gì)] {raga(DHL['rūpārūpa'])} {DASH} "
                                      f"{called(TAN['bhava'])}.")
h("( ) [(tattha katamā vibhavataṇhā) (?)]", f"( ) [(ở đây, khao khát không còn hiện hữu là gì) (?)] {raga(UCCH_D)} "
                                            f"{DASH} {called(TAN['vibhava'])}. Đây là {g(3, 'taṇhā')}.")
SLIPS.append("^2-916 the last two definitions carry editorial brackets '( ) [(tattha katamā bhavataṇhā)]' / "
             "'[(tattha katamā vibhavataṇhā) (?)]' and repeat bhava- / vibhavataṇhā: translated as written")
for _num, _ks in ((9, ("kāma", "rūpa", "arūpa")), (10, ("rūpa", "arūpa", "nirodha"))):
    hd(5, f"({_num}) Aparāpi tisso taṇhā", f"({_num}) {cap(g(3, 'taṇhā', True))}")
    tq("ā aparāpi tisso taṇhā?", g(3, "taṇhā", True), ", ".join(cap(TAN[k]) if i == 0 else TAN[k]
                                                                 for i, k in enumerate(_ks)) + ".")
    for _i, _k in enumerate(_ks):
        _w = UCCH_D if _k == "nirodha" else DHL[_k]
        _line = ka(_ABC[_i], None, raga(_w), name=TAN[_k])
        if _i == 2:
            _line += f" Đây là {g(3, 'taṇhā')}."
        h(f"({_KKG[_i]}) tattha katamā {_k}taṇhā?", _line)
hd(5, "(11) Tisso esanā", "(11) " + cap(g(3, "esanā")))
ES = {"kāma": "sự tìm cầu dục lạc", "bhava": "sự tìm cầu sự hiện hữu",
      "brahmacariya": "sự tìm cầu đời sống tu hành trong sạch"}                    # brahmacariya [pi-1 ^1-1355]
tq("ā tisso esanā?", g(3, "esanā"), f"{cap(ES['kāma'])}, {ES['bhava']}, {ES['brahmacariya']}.")
h("(Ka) tattha katamā kāmesanā? Yo", ka("a", None, KAMA_PE, name=ES["kāma"]))
h("(Kha) tattha katamā bhavesanā? Yo", ka("b", None, BHAVASAVA_PE, name=ES["bhava"]))
_V2 = VIEWS10.split(", hoặc ")
h("(Ga) tattha katamā brahmacariyesanā? \"Sassato",
  ka("c", None, f"{_V2[0]}, hoặc {_V2[1]} {DASH} hoặc… hoặc {_V2[-1]}, {DITTHI_PE}", name=ES["brahmacariya"]))
SLIPS.append("^2-919 (Ga) '\"asassato loko\"ti – vā…pe…' (a dash inside the list): kept («– hoặc…»)")
TADEK = "cùng hiện diện với nó"                                                     # tadekaṭṭhaṃ [pi-1 ^1-986 words]
KVM = "nghiệp bất thiện bằng thân, bằng lời nói, bằng ý"
for _l, _k, _x in (("Ka", "kāma", "sự tham đắm dục lạc"), ("Kha", "bhava", "sự tham đắm hiện hữu"),
                   ("Ga", "brahmacariya", "quan điểm chấp giữ cực đoan")):
    _line = ka(_ABC[_KKG.index(_l)], None, f"{cap(_x)}, {KVM} {TADEK}", name=ES[_k])
    if _l == "Ga":
        _line += f" Đây là {g(3, 'esanā')}."
    h(f"({_l}) tattha katamā {_k[:-1] if _k.endswith('a') else _k}esanā,", _line)
SLIPS.append("^2-919 second (Ka)-(Ga) set 'tattha katamā kāmesanā, kāmarāgo …' (question mark missing): "
             "rendered as a question (punctuation)")
hd(5, "(12) Tisso vidhā", "(12) " + cap(g(3, "vidhā")))
tq("ā tisso vidhā?", g(3, "vidhā"), f"Sự so sánh “Tôi hơn người”, sự so sánh “Tôi bằng người”, sự so sánh “Tôi kém "
                                    f"người” {DASH} đây là {g(3, 'vidhā')}.")
hd(5, "(13) Tīṇi bhayāni", "(13) " + cap(g(3, "bhaya")))
BH = {"jāti": "sự sinh", "jarā": "sự lão hóa", "byādhi": "bệnh tật", "maraṇa": "sự chết", "rāja": "vua chúa",
      "cora": "trộm cướp", "aggi": "lửa", "udaka": "nước", "ūmi": "sóng", "kumbhīla": "cá sấu", "āvaṭṭa": "xoáy nước",
      "susukā": "cá dữ", "attānuvāda": "sự tự trách", "parānuvāda": "sự bị người khác chỉ trích",
      "daṇḍa": "hình phạt", "duggati": "cõi xấu", "ājīvika": "sinh kế", "asiloka": "tiếng xấu"}


def bh(k):
    return f"nỗi sợ hãi về {BH[k]}"


tq("āni tīṇi bhayāni?", g(3, "bhaya"), f"{cap(bh('jāti'))}, {bh('jarā')}, {bh('maraṇa')}.")
FEAR = "nỗi sợ hãi, sự kinh hãi, trạng thái cứng đờ, sự dựng tóc gáy, sự hoảng hốt của tâm"   # bhayaṃ … utrāso [new]
for _i, _k in enumerate(("jāti", "jarā", "maraṇa")):
    _line = ka(_ABC[_i], None, f"Dựa vào {BH[_k]} mà có {FEAR}", name=bh(_k))
    if _i == 2:
        _line += f" Đây là {g(3, 'bhaya')}."
    h(f"({_KKG[_i]}) tattha katamaṃ {_k}bhayaṃ?", _line)
hd(5, "(14) Tīṇi tamāni", "(14) " + cap(g(3, "tama")))
DOUBT = "người ta nghi ngờ và hoài nghi, không quyết định, không có lòng tin trong sáng"   # [pi-1 ^1-1008, ch6]
tq("āni tīṇi tamāni?", g(3, "tama"), f"Liên quan đến thời quá khứ, {DOUBT}; liên quan đến thời tương lai, {DOUBT}; "
                                     f"liên quan đến thời hiện tại ngay bây giờ, {DOUBT} {DASH} đây là {g(3, 'tama')}.")
hd(5, "(15) Tīṇi titthāyatanāni", "(15) " + cap(g(3, "titthāyatana")))
_TT = ("Bất cứ điều gì con người này cảm nhận, dù dễ chịu, khó chịu hay không khó chịu cũng không dễ chịu, tất cả đều "
       "{x}")
_TTX = ["do những gì đã làm trước đây làm nguyên nhân", "do sự sáng tạo của đấng Tự Tại làm nguyên nhân",
        "không có nguyên nhân, không có điều kiện"]
SB_AGAIN = "lại nữa, ở đời này, có sa-môn hay bà-la-môn có học thuyết như vầy, có quan điểm như vầy"
tq("āni tīṇi titthāyatanāni?", g(3, "titthāyatana"),
   f"{SB} {DASH} “{_TT.format(x=_TTX[0])}”; {SB_AGAIN} {DASH} “{_TT.format(x=_TTX[1])}”; {SB_AGAIN} {DASH} "
   f"“{_TT.format(x=_TTX[2])}” {DASH} đây là {g(3, 'titthāyatana')}.")
hd(5, "(16) Tayo kiñcanā", "(16) " + cap(g(3, "kiñcana")))
RDM = ("sự tham đắm", "sự sân hận", "sự si mê")                                     # rāga / dosa / moha [pi-1]
h("Tattha katame tayo kiñcanā", f"Ở đây, {g(3, 'kiñcana')}{VAR_KINCANA} là gì? " +
  ", ".join(f"{cap(x) if i == 0 else x} là {GN['kiñcana']}" for i, x in enumerate(RDM)) +
  f" {DASH} đây là {g(3, 'kiñcana')}.")
for _num, _k, _q in ((17, "aṅgaṇa", "āni tīṇi aṅgaṇāni?"), (18, "mala", "āni tīṇi malāni?"),
                     (19, "visama", "āni tīṇi visamāni?")):
    hd(5, f"({_num}) Tīṇi {_k[:-1]}āni", f"({_num}) {cap(g(3, _k))}")
    tq(_q, g(3, _k), ", ".join(f"{cap(x) if i == 0 else x} là {GN[_k]}" for i, x in enumerate(RDM)) +
       f" {DASH} đây là {g(3, _k)}.")
KVM3 = ("thân", "lời nói", "ý")
hd(5, "(20) Aparānipi tīṇi visamāni", "(20) " + cap(g(3, "visama", True)))
tq("āni aparānipi tīṇi visamāni?", g(3, "visama", True),
   ", ".join(f"{cap(GN['visama']) if i == 0 else GN['visama']} của {x}" for i, x in enumerate(KVM3)) +
   f" {DASH} đây là {g(3, 'visama')}.")
hd(5, "(21) Tayo aggī", "(21) " + cap(g(3, "aggi")))
tq("e tayo aggī?", g(3, "aggi"), ", ".join(f"{cap(GN['aggi']) if i == 0 else GN['aggi']} {x[3:]}"
                                            for i, x in enumerate(RDM)) + f" {DASH} đây là {g(3, 'aggi')}.")
hd(5, "(22) Tayo kasāvā", "(22) " + cap(g(3, "kasāva")))
tq("e tayo kasāvā?", g(3, "kasāva"), ", ".join(f"{cap(GN['kasāva']) if i == 0 else GN['kasāva']} {x[3:]}"
                                                for i, x in enumerate(RDM)) + f" {DASH} đây là {g(3, 'kasāva')}.")
hd(5, "(23) Aparepi tayo kasāvā", "(23) " + cap(g(3, "kasāva", True)))
tq("e aparepi tayo kasāvā?", g(3, "kasāva", True),
   ", ".join(f"{cap(GN['kasāva']) if i == 0 else GN['kasāva']} của {x}" for i, x in enumerate(KVM3)) +
   f" {DASH} đây là {g(3, 'kasāva')}.")
# (24) … (35) single items
_TRIPLE_L = [("24. Ka", "24. a"), ("Kha", "b"), ("Ga", "c")]


def th(i, k):
    lp, lv = _TRIPLE_L[i % 3] if i % 3 else (f"{24 + i // 3}. Ka", f"{24 + i // 3}. a")
    hd(5, f"({lp}) {k}", f"({lv}) {N[k]}")


_SG = {"assādadiṭṭhi": "ā", "attānudiṭṭhi": "ā", "micchādiṭṭhi": "ā", "arati": "ā", "vihesā": "ā",
       "adhammacariyā": "ā", "dovacassatā": "ā", "pāpamittatā": "ā", "nānattasaññā": "ā", "uddhaccaṃ": "aṃ",
       "kosajjaṃ": "aṃ", "pamādo": "o"}
_seq = [x for t in T3 for x in t]
_i = 0


def nxt(k, vi):
    global _i
    assert _seq[_i] == k, (_seq[_i], k)
    th(_i, k)
    _i += 1
    gender = {"o": "o", "ā": "ā", "aṃ": "aṃ"}
    h(f"Tattha katam", vi)


nxt("assādadiṭṭhi", f"{q(N['assādadiṭṭhi'])} {SB} {DASH} “Không có lỗi gì trong các dục lạc”. Người ấy lao vào sự đắm "
                    f"say trong các dục lạc. {called(N['assādadiṭṭhi'], True)}.")
nxt("attānudiṭṭhi", f"{q(N['attānudiṭṭhi'])} {SAKKAYA_D} {DASH} {called(N['attānudiṭṭhi'])}.")
nxt("micchādiṭṭhi", f"{q(N['micchādiṭṭhi'])} {_NAT_PE} {DASH} {DITTHI_PE} {DASH} {called(N['micchādiṭṭhi'])}. "
                    f"Quan điểm về sự trường tồn là {N['assādadiṭṭhi']}, quan điểm về tự ngã là {N['attānudiṭṭhi']}, "
                    f"quan điểm về sự đoạn diệt là {N['micchādiṭṭhi']}.")
nxt("arati", ARATI)
nxt("vihesā", f"{q(N['vihesā'])} {VIHESA_BODY} {DASH} {called(N['vihesā'])}.")
nxt("adhammacariyā", f"{q(N['adhammacariyā'])} " + ", ".join(
    f"{'H' if i == 0 else 'h'}ành vi phi pháp và lệch lạc bằng {x}" for i, x in enumerate(KVM3)) +
    f" {DASH} {called(N['adhammacariyā'])}.")
DOVAC_Q = f"{q(N['dovacassatā'])} {DOVAC} {DASH} {called(N['dovacassatā'])}."
nxt("dovacassatā", DOVAC_Q)
nxt("pāpamittatā", f"{q(N['pāpamittatā'])} {PAPAM} {DASH} {called(N['pāpamittatā'])}.")
nxt("nānattasaññā", f"{q(NANATTA)} {cap(SANN['kāma'])}, {SANN['byāpāda']}, {SANN['vihiṃsā']} {DASH} {called(NANATTA)}. "
                    f"Mọi tri giác bất thiện đều là {NANATTA}.")
UDDH_Q = f"{q(N['uddhaccaṃ'])} {UDDH} {DASH} {called(N['uddhaccaṃ'])}."
nxt("uddhaccaṃ", UDDH_Q)
KOSAJJA_Q = f"{q(N['kosajjaṃ'])} {KOSAJJA} {DASH} {called(N['kosajjaṃ'])}."
nxt("kosajjaṃ", KOSAJJA_Q)
PAMADA_Q = f"{q(N['pamādo'])} {PAMADA_U.replace('; hoặc trong việc tu tập', '; trong việc tu tập')} {DASH} " \
           f"{called(N['pamādo'])}."
nxt("pamādo", PAMADA_Q)
nxt("asantuṭṭhitā", f"{q(N['asantuṭṭhitā'])} {atri(N['asantuṭṭhitā'])} {DASH} {called(N['asantuṭṭhitā'])}.")
nxt("asampajaññatā", f"{q(N['asampajaññatā'])} {AVIJJA_PE} {DASH} {called(N['asampajaññatā'])}.")
nxt("mahicchatā", f"{q(N['mahicchatā'])} {atri(N['mahicchatā'])} {DASH} {called(N['mahicchatā'])}.")
nxt("ahirikaṃ", f"{q(N['ahirikaṃ'])} {AHIRI} {DASH} {called(N['ahirikaṃ'])}.")
nxt("anottappaṃ", f"{q(N['anottappaṃ'])} {ANOTT} {DASH} {called(N['anottappaṃ'])}.")
nxt("pamādo", PAMADA_Q)
nxt("anādariyaṃ", f"{q(N['anādariyaṃ'])} Điều mà là sự thiếu tôn trọng, thái độ thiếu tôn trọng, sự thiếu kính trọng, "
                  f"sự không vâng lời, sự coi thường, sự khởi coi thường, trạng thái khởi coi thường{VAR_ANADDA}, sự "
                  f"thiếu lễ độ, sự không quý trọng {DASH} {called(N['anādariyaṃ'])}.")
nxt("dovacassatā", DOVAC_Q)
_PAPAM_U21 = PAPAM.replace("sự giao du mật thiết, sự gần gũi", "sự giao du mật thiết, sự lui tới, sự gần gũi")
assert _PAPAM_U21 != PAPAM
nxt("pāpamittatā", f"{q(N['pāpamittatā'])} {_PAPAM_U21} {DASH} {called(N['pāpamittatā'])}.")
nxt("assaddhiyaṃ", f"{q(N['assaddhiyaṃ'])} {IDHEK} không có niềm tin, không tin Đức Phật, hoặc Giáo Pháp, hoặc Tăng "
                   f"đoàn, {EVA} sự thiếu niềm tin, sự không tin tưởng, sự không tin chắc, sự không có lòng tin sâu sắc "
                   f"{DASH} {called(N['assaddhiyaṃ'])}.")
nxt("avadaññutā", f"{q(N['avadaññutā'])} {MACCH} {DASH} {called(N['avadaññutā'])}.")
nxt("kosajjaṃ", KOSAJJA_Q)
SLIPS.append("^2-U23 kosajja 'vossaggo, vossaggānuppadānaṃ kusalānaṃ dhammānaṃ, bhāvanāya …' (commas misplaced): "
             "rendered as ^2-U14 (punctuation)")
nxt("uddhaccaṃ", UDDH_Q)
SLIPS.append("^2-933 'bhavantattaṃ' (= bhantattaṃ, as ^2-928 / ^2-U29): spelling, rendered as meant")
nxt("asaṃvaro", f"{q(N['asaṃvaro'])} {INDRI_ASAMVARA[:-1]} {DASH} {called(N['asaṃvaro'])}.")
nxt("dussīlyaṃ", f"{q(N['dussīlyaṃ'])} {VITIKKAMA} {DASH} {called(N['dussīlyaṃ'])}.")
nxt("ariyānaṃ adassanakamyatā",
    f"{q(N['ariyānaṃ adassanakamyatā'])} {ARIYA_Q} Các Đức Phật và các đệ tử của Đức Phật được gọi là các bậc thánh. "
    f"Điều mà là sự không muốn thấy, sự không muốn nhìn, sự không muốn đến gặp, sự không muốn cùng hội họp với các bậc "
    f"thánh này {DASH} {called(N['ariyānaṃ adassanakamyatā'])}.")
SADDH = "Giáo Pháp chân chính"
BOD37 = ("Bốn sự thiết lập tỉnh thức, bốn nỗ lực đúng đắn, bốn nền tảng thần thông, năm năng lực, năm sức mạnh, bảy chi "
         "phần giác ngộ, con đường cao quý gồm tám chi phần")                     # [pi-1 / ch7 … ch11 names]
nxt("saddhammaṃ asotukamyatā",
    f"{q(N['saddhammaṃ asotukamyatā'])} {q(SADDH)} {BOD37} {DASH} {called(SADDH)}. Điều mà là sự không muốn nghe, sự "
    f"không muốn lắng nghe, sự không muốn học hỏi, sự không muốn ghi nhớ {SADDH} này {DASH} "
    f"{called(N['saddhammaṃ asotukamyatā'])}.")
nxt("upārambhacittatā",
    f"{q(N['upārambhacittatā'])} {q('sự bắt lỗi')} Điều mà là sự bắt lỗi, sự bắt lỗi liên tục, hành động bắt lỗi, hành "
    f"động bắt lỗi liên tục, trạng thái bắt lỗi liên tục, sự coi thường, sự xem nhẹ, sự khinh miệt, sự tìm kẽ hở {DASH} "
    f"{called(N['upārambhacittatā'])}.")
SLIPS.append("^2-U27 the question asks 'katamo upārambho?' and the answer names 'upārambhacittatā': as written")
nxt("muṭṭhassaccaṃ", f"{q(N['muṭṭhassaccaṃ'])} {MUTTH} {DASH} {called(N['muṭṭhassaccaṃ'])}.")
nxt("asampajaññaṃ", f"{q(N['asampajaññaṃ'])} {ASAMP} {DASH} {called(N['asampajaññaṃ'])}.")
nxt("cetaso vikkhepo", f"{q(N['cetaso vikkhepo'])} {UDDH} {DASH} {called(N['cetaso vikkhepo'])}.")
VIP = {"anicca": ("điều vô thường", "thường còn"), "dukkha": ("điều khổ đau", "hạnh phúc"),
       "anatta": ("điều không phải là tự ngã", "tự ngã"), "asubha": ("điều không đẹp", "đẹp")}
_AYO = "; ".join(f"{'S' if i == 0 else 's'}ự chú tâm không khôn ngoan khi xem {a} là “{b}”"
                 for i, (a, b) in enumerate(VIP.values()))
nxt("ayoniso manasikāro", f"{q(N['ayoniso manasikāro'])} {_AYO}; hoặc, theo cách trái ngược với sự thật, sự hướng "
                          f"đến, sự hướng đến liên tục, sự chú hướng, sự lưu ý, sự chú tâm của tâm {DASH} "
                          f"{called(N['ayoniso manasikāro'])}.")
MICCHA8 = ["quan điểm sai lầm", "tư duy sai lầm", "lời nói sai lầm", "hành động sai lầm", "sinh kế sai lầm",
           "nỗ lực sai lầm", "tỉnh thức sai lầm", "định tâm sai lầm"]                # [pi-1 / ch4 path words]
KUM = "con đường lệch lạc"                                                          # kummagga [pi-1]
nxt("kummaggasevanā", f"{q(N['kummaggasevanā'])} {q(KUM)} {cap(', '.join(MICCHA8))} {DASH} {called(KUM)}. Điều mà là "
                      f"sự đi theo, sự thường xuyên đi theo, sự đi theo mật thiết, sự gần gũi, sự gần gũi mật thiết, "
                      f"sự gắn bó, sự gắn bó mật thiết, sự nghiêng về phía {KUM} này {DASH} "
                      f"{called(N['kummaggasevanā'])}.")
nxt("cetaso ca līnattaṃ", LINATTA)
h("Tikaṃ.", CLOSE[3])
assert _i == len(_seq)

# ---------------------------------------------------------------- Catukkaniddeso
hd(4, "Catukkaniddeso", "Giải thích phân loại theo nhóm bốn")
hd(5, "(1) Cattāro āsavā", "(1) " + cap(g(4, "āsava")))
tq("e cattāro āsavā?", g(4, "āsava"), f"{cap(ASAV['kāma'])}, {ASAV['bhava']}, {ASAV['diṭṭhi']}, {ASAV['avijjā']}.")
_ABCD = ("a", "b", "c", "d")
for _l, _lv, _k in (("Ka", "a", "kāma"), ("Kha", "b", "bhava"), ("Ga", "c", "diṭṭhi"), ("Gha", "d", "avijjā")):
    hd(5, f"({_l}) " + {"kāma": "kāmāsavo", "bhava": "bhavāsavo", "diṭṭhi": "diṭṭhāsavo", "avijjā": "avijjāsavo"}[_k],
       f"({_lv}) {ASAV[_k]}")
    if _k == "kāma":
        h("Tattha katamo kāmāsavo?", f"{q(ASAV['kāma'])} {KAMASAVA} {DASH} {called(ASAV['kāma'])}.")
    elif _k == "bhava":
        h("Tattha katamo bhavāsavo?", f"{q(ASAV['bhava'])} {BHAVASAVA_PE} {DASH} {called(ASAV['bhava'])}.")
    elif _k == "diṭṭhi":
        h("Tattha katamo diṭṭhāsavo?", f"{q(ASAV['diṭṭhi'])} {VIEWS10}. {cap(DITTHI_PE)} {DASH} "
                                       f"{called(ASAV['diṭṭhi'])}. Mọi quan điểm sai lầm đều là {ASAV['diṭṭhi']}.")
        assert "Mọi quan điểm sai lầm đều là ô nhiễm quan điểm." in DITTHASAVA
    else:
        h("Tattha katamo avijjāsavo?", f"{q(ASAV['avijjā'])} {AVIJJASAVA_FULL.split(' Điều mà thuộc loại như vậy là ')[0]}"
                                       f" {cap(EVA)} {MOHA_PE} {DASH} {called(ASAV['avijjā'])}. Đây là "
                                       f"{g(4, 'āsava')}.")
UP = {"kāma": "sự bám víu vào dục lạc", "diṭṭhi": "sự bám víu vào quan điểm",
      "sīlabbata": "sự bám víu vào giới hạnh và nghi thức", "attavāda": "sự bám víu vào học thuyết về tự ngã"}
hd(5, "(2-5) Cattāro ganthādī", f"(2-5) {cap(g(4, 'gantha'))} và những điều tương tự")
h("Tattha katame cattāro ganthā", f"Ở đây, {g(4, 'gantha')}… {g(4, 'ogha')}… {g(4, 'yoga')}… {g(4, 'upādāna')} là gì? "
                                  f"{cap(', '.join(UP.values()))}.")
for _l, _lv, _k in (("Ka", "a", "kāma"), ("Kha", "b", "diṭṭhi"), ("Ga", "c", "sīlabbata"), ("Gha", "d", "attavāda")):
    _hp = {"kāma": "kāmupādānaṃ", "diṭṭhi": "diṭṭhupādānaṃ", "sīlabbata": "sīlabbatupādānaṃ",
           "attavāda": "attavādupādānaṃ"}[_k]
    hd(5, f"({_l}) {_hp}", f"({_lv}) {UP[_k]}")
    if _k == "kāma":
        h("Tattha katamaṃ kāmupādānaṃ?", f"{q(UP['kāma'])} {KAMA_PE} {DASH} {called(UP['kāma'])}.")
    elif _k == "diṭṭhi":
        h("Tattha katamaṃ diṭṭhupādānaṃ?", f"{q(UP['diṭṭhi'])} {_NAT_PE}. {cap(DITTHI_PE)} {DASH} "
                                           f"{called(UP['diṭṭhi'])}. {DITTHUP_TAIL}")
    elif _k == "sīlabbata":
        h("Tattha katamaṃ sīlabbatupādānaṃ?", f"{q(UP['sīlabbata'])} {SILABBATA_Q}. {cap(DITTHI_PE)} {DASH} "
                                              f"{called(UP['sīlabbata'])}.")
    else:
        h("Tattha katamaṃ attavādupādānaṃ?", f"{q(UP['attavāda'])} {SAKKAYA_D} {DASH} {called(UP['attavāda'])}. Đây là "
                                             f"{g(4, 'upādāna')}.")
hd(5, "(6) Cattāro taṇhuppādā", "(6) " + cap(g(4, "taṇhuppāda")))
_REQ = ["y phục", "đồ ăn khất thực", "chỗ ở", "sự hiện hữu này hay sự hiện hữu khác"]
tq("e cattāro taṇhuppādā?", g(4, "taṇhuppāda"), "; ".join(
    f"{'K' if i == 0 else 'k'}hao khát của vị tỳ-khưu, khi sinh khởi, thì sinh khởi vì {x}" for i, x in enumerate(_REQ))
   + f" {DASH} đây là {g(4, 'taṇhuppāda')}.")
hd(5, "(7) Cattāri agatigamanāni", "(7) " + cap(g(4, "agatigamana")))
_AG = ["ưa thích", "sân hận", "si mê", "sợ hãi"]
tq("āni cattāri agatigamanāni?", g(4, "agatigamana"), ", ".join(
    f"{'Người ta đi' if i == 0 else 'đi'} theo con đường sai trái vì {x}" for i, x in enumerate(_AG)) +
   f". {cap(EVA)} con đường sai trái, sự đi theo con đường sai trái, sự đi theo ưa thích, sự đi theo phe phái, sự trôi "
   f"theo như nước {DASH} đây là {g(4, 'agatigamana')}.")
hd(5, "(8) Cattāro vipariyāsā", "(8) " + cap(g(4, "vipariyāsa")))
_VP = "; ".join(f"{'S' if i == 0 else 's'}ự đảo ngược của tri giác, sự đảo ngược của tâm, sự đảo ngược của quan điểm "
                f"khi xem {a} là “{b}”" for i, (a, b) in enumerate(VIP.values()))
tq("e cattāro vipariyāsā?", g(4, "vipariyāsa"), f"{_VP} {DASH} đây là {g(4, 'vipariyāsa')}.")
SEEN = [("thấy", "đã thấy"), ("nghe", "đã nghe"), ("cảm nhận", "đã cảm nhận"), ("nhận biết", "đã nhận biết")]
AV1 = [f"việc nói là {b} đối với điều chưa {a}" for a, b in SEEN]                   # adiṭṭhe diṭṭhavāditā …
AV2 = [f"việc nói là chưa {a} đối với điều {b}" for a, b in SEEN]                   # diṭṭhe adiṭṭhavāditā …
hd(5, "(9) Cattāro anariyavohārā", "(9) " + cap(g(4, "anariyavohāra")))
tq("e cattāro anariyavohārā?", g(4, "anariyavohāra"), f"{cap(', '.join(AV1))} {DASH} đây là {g(4, 'anariyavohāra')}.")
hd(5, "(10) Aparepi cattāro anariyavohārā", "(10) " + cap(g(4, "anariyavohāra", True)))
tq("e aparepi cattāro anariyavohārā?", g(4, "anariyavohāra", True),
   f"{cap(', '.join(AV2))} {DASH} đây là {g(4, 'anariyavohāra')}.")
hd(5, "(11) Cattāri duccaritāni", "(11) " + cap(g(4, "duccarita")))
tq("āni cattāri duccaritāni?", g(4, "duccarita"), f"{cap(', '.join(PANA3 + VACI4[:1]))} {DASH} đây là "
                                                  f"{g(4, 'duccarita')}.")
hd(5, "(12) Aparānipi cattāri duccaritāni", "(12) " + cap(g(4, "duccarita", True)))
tq("āni aparānipi cattāri duccaritāni?", g(4, "duccarita", True), f"{cap(', '.join(VACI4))} {DASH} đây là "
                                                                  f"{g(4, 'duccarita')}.")
hd(5, "(13) Cattāri bhayāni", "(13) " + cap(g(4, "bhaya")))
tq("āni cattāri bhayāni?", g(4, "bhaya"), f"{cap(', '.join(bh(k) for k in ('jāti', 'jarā', 'byādhi', 'maraṇa')))} "
                                          f"{DASH} đây là {g(4, 'bhaya')}.")
hd(5, "(14) Aparānipi cattāri bhayāni", "(14) " + cap(g(4, "bhaya", True)))
tq("āni aparānipi cattāri bhayāni? Rāja", g(4, "bhaya", True),
   f"{cap(', '.join(bh(k) for k in ('rāja', 'cora', 'aggi', 'udaka')))} {DASH} đây là {g(4, 'bhaya')}.")
tq("āni aparānipi cattāri bhayāni? Ūmi", g(4, "bhaya", True),
   f"{cap(bh('ūmi'))}, {bh('kumbhīla')}{VAR_KUMBHILA}, {bh('āvaṭṭa')}, {bh('susukā')} {DASH} đây là {g(4, 'bhaya')}.")
tq("āni aparānipi cattāri bhayāni? Attā", g(4, "bhaya", True),
   f"{cap(', '.join(bh(k) for k in ('attānuvāda', 'parānuvāda', 'daṇḍa', 'duggati')))} {DASH} đây là "
   f"{g(4, 'bhaya')}.")
hd(5, "(15) Catasso diṭṭhiyo", "(15) " + cap(g(4, "diṭṭhi")))
SDK = "Sự dễ chịu và sự khó chịu"                                                    # sukhadukkha [pi-1 words]
_CV = ["do chính mình tạo ra", "do người khác tạo ra", "vừa do chính mình tạo ra vừa do người khác tạo ra",
       "không do chính mình tạo ra, không do người khác tạo ra, mà sinh khởi một cách ngẫu nhiên"]
TRUE = "như là sự thật, như là điều chắc chắn"                                       # saccato thetato [new]
tq("ā catasso diṭṭhiyo?", g(4, "diṭṭhi"), "; ".join(
    f"{'Q' if i == 0 else 'q'}uan điểm “{SDK} {x}” khởi lên {TRUE}" for i, x in enumerate(_CV)) +
   f" {DASH} đây là {g(4, 'diṭṭhi')}.")
h("Catukkaṃ.", CLOSE[4])

# ---------------------------------------------------------------- Pañcakaniddeso
hd(4, "Pañcakaniddeso", "Giải thích phân loại theo nhóm năm")
hd(5, "(1) Pañcorambhāgiyāni saṃyojanāni", "(1) " + cap(g(5, "orambhāgiya")))
tq("āni pañcorambhāgiyāni saṃyojanāni?", g(5, "orambhāgiya"),
   f"{cap(', '.join(S3))}, ý muốn dục lạc, ác ý {DASH} đây là {g(5, 'orambhāgiya')}.")
hd(5, "(2) Pañcuddhambhāgiyāni saṃyojanāni", "(2) " + cap(g(5, "uddhambhāgiya")))
tq("āni pañcuddhambhāgiyāni saṃyojanāni?", g(5, "uddhambhāgiya"),
   f"Sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc, sự kiêu mạn, sự xao động, vô minh {DASH} đây là "
   f"{g(5, 'uddhambhāgiya')}.")
hd(5, "(3) Pañca macchariyāni", "(3) " + cap(g(5, "macchariya")))
tq("āni pañca macchariyāni?", g(5, "macchariya"), f"{cap(MACCH5)} {DASH} đây là {g(5, 'macchariya')}.")
RDMMD = ("tham đắm", "sân hận", "si mê", "kiêu mạn", "quan điểm")
hd(5, "(4) Pañca saṅgā", "(4) " + cap(g(5, "saṅga")))
tq("e pañca saṅgā?", g(5, "saṅga"), ", ".join(f"{'S' if i == 0 else 's'}ự dính mắc do {x}" for i, x in enumerate(RDMMD))
   + f" {DASH} đây là {g(5, 'saṅga')}.")
hd(5, "(5) Pañca sallā", "(5) " + cap(g(5, "salla")))
tq("e pañca sallā?", g(5, "salla"), ", ".join(f"{'M' if i == 0 else 'm'}ũi tên {x}" for i, x in enumerate(RDMMD)) +
   f" {DASH} đây là {g(5, 'salla')}.")
hd(5, "(6) Pañca cetokhilā", "(6) " + cap(g(5, "cetokhila")))
_KH = ["Bậc Đạo Sư", "Giáo Pháp", "Tăng đoàn", "sự tu học"]                          # [pi-1 ^1-1008]
_khl = "; ".join(f"{'N' if i == 0 else 'n'}ghi ngờ và hoài nghi, không quyết định, không có lòng tin trong sáng về {x}"
                 for i, x in enumerate(_KH))
tq("e pañca cetokhilā?", g(5, "cetokhila"), f"{_khl}; nổi giận, không hài lòng, có tâm bị tổn thương, trở nên chai cứng "
                                            f"đối với các bạn đồng tu {DASH} đây là {g(5, 'cetokhila')}.")
hd(5, "(7) Pañca cetaso vinibandhā", "(7) " + cap(g(5, "vinibandha")))
tq("e pañca cetaso vinibandhā?", g(5, "vinibandha"),
   f"Đối với các dục lạc, người ta chưa lìa tham đắm, chưa lìa ý muốn, chưa lìa sự yêu thích, chưa lìa sự khát khao, "
   f"chưa lìa sự nóng bỏng, chưa lìa khao khát; đối với thân, chưa lìa tham đắm… đối với hình sắc, chưa lìa tham đắm… "
   f"sau khi ăn no căng bụng tùy thích, người ta sống chuyên chú vào thú vui nằm, thú vui trở mình, thú vui ngủ; người "
   f"ta sống đời tu hành trong sạch với ước nguyện về một cõi chư thiên nào đó {DASH} “Nhờ giới hạnh này, hoặc nghi "
   f"thức này, hoặc khổ hạnh này, hoặc đời sống tu hành trong sạch này, tôi sẽ trở thành một vị trời hoặc một vị trời "
   f"nào đó” {DASH} đây là {g(5, 'vinibandha')}.")
hd(5, "(8) Pañca nīvaraṇāni", "(8) " + cap(g(5, "nīvaraṇa")))
tq("āni pañca nīvaraṇāni?", g(5, "nīvaraṇa"), f"{cap(NIVA5)} {DASH} đây là {g(5, 'nīvaraṇa')}.")
hd(5, "(9) Pañca kammāni ānantarikāni", "(9) " + cap(g(5, "ānantarika")))
tq("āni pañca kammāni ānantarikāni?", g(5, "ānantarika"),
   f"Mẹ bị tước đoạt mạng sống, cha bị tước đoạt mạng sống, bậc A-la-hán bị tước đoạt mạng sống, Như Lai bị làm cho "
   f"chảy máu với tâm độc ác, Tăng đoàn bị chia rẽ {DASH} đây là {g(5, 'ānantarika')}.")
SLIPS.append("^2-U55 'arahanto jīvitā voropito' (plural form with a singular verb): no effect in Vietnamese")
hd(5, "(10) Pañca diṭṭhiyo", "(10) " + cap(g(5, "diṭṭhi")))
ATTA = "Tự ngã"
_P5 = ["có tri giác", "không có tri giác", "không phải có tri giác cũng không phải không có tri giác"]
CUT = "sự đoạn diệt, sự hủy diệt, sự không còn hiện hữu của chúng sinh đang hiện hữu"   # ucchedaṃ vināsaṃ vibhavaṃ
DNIB = "Niết-bàn ngay trong đời này"                                                  # diṭṭhadhammanibbāna [new]
tq("ā pañca diṭṭhiyo?", g(5, "diṭṭhi"), "; ".join(
    f"{'M' if i == 0 else 'm'}ột số người tuyên bố rằng “{ATTA} {x}, không bệnh tật sau khi chết”"
    for i, x in enumerate(_P5)) + f"; hoặc họ trình bày {CUT}; hoặc một số người tuyên bố {DNIB} {DASH} đây là "
                                  f"{g(5, 'diṭṭhi')}.")
hd(5, "(11) Pañca verā", "(11) " + cap(g(5, "vera")))
tq("e pañca verā?", g(5, "vera"), f"{cap(', '.join(PANA3 + VACI4[:1] + [SURA]))} {DASH} đây là {g(5, 'vera')}.")
hd(5, "(12) Pañca byasanā", "(12) " + cap(g(5, "byasana")))
BYA = ["tổn hại về người thân", "tổn hại về tài sản", "tổn hại do bệnh tật", "tổn hại về giới hạnh",
       "tổn hại về quan điểm"]                                                        # [ch4]
in_out("4-saccavibhango.md", *BYA)
tq("e pañca byasanā?", g(5, "byasana"), f"{cap(', '.join(BYA))} {DASH} đây là {g(5, 'byasana')}.")
hd(5, "(13) Pañca akkhantiyā ādīnavā", "(13) " + cap(g(5, "ādīnava")))
tq("e pañca akkhantiyā ādīnavā?", g(5, "ādīnava"),
   f"Người ấy không được nhiều người yêu quý, không được ưa thích, có nhiều thù địch, có nhiều lỗi lầm, chết trong mê "
   f"muội, {APAYA} {DASH} đây là {g(5, 'ādīnava')}.")
hd(5, "(14) Pañca bhayāni", "(14) " + cap(g(5, "bhaya")))
tq("āni pañca bhayāni?", g(5, "bhaya"), f"{cap(bh('ājīvika'))}, {bh('asiloka')}, nỗi sợ hãi rụt rè trước hội chúng, "
                                        f"{bh('maraṇa')}, {bh('duggati')} {DASH} đây là {g(5, 'bhaya')}.")
hd(5, "(15) Pañca diṭṭhadhammanibbānavādā", "(15) " + cap(g(5, "dnv")))
h("Tattha katame pañca diṭṭhadhammanibbānavādā?", q(g(5, "dnv")))
BHO = "thưa ngài"                                                                     # bho [new]
PDN = "Niết-bàn tối thượng ngay trong đời này"
REACH = f"chỉ đến chừng ấy là tự ngã này đạt đến {PDN}"
ITTHEKE_N = f"Như vậy, một số người trình bày {PDN} của chúng sinh đang hiện hữu."
TAMANNO = "người khác nói với người ấy như vầy"
EXISTS = f"{cap(BHO)}, tự ngã mà ngài nói ấy có tồn tại"
DENY = "tôi không nói rằng nó không tồn tại"
NOCA_N = f"Nhưng {BHO}, tự ngã này không phải chỉ đến chừng ấy là đạt đến {PDN}."
WHY = "Vì sao vậy?"
GROSS = "nên trạng thái ấy được xem là thô"


def yato_n(x):
    return f"{cap(BHO)}, khi tự ngã này {x}, {BHO}, {REACH}”."


h("(Ka) idhekacco samaṇo vā brāhmaṇo vā",
  f"(a) {low(SB)}{VAR_EVAMDITTHI} {DASH} “{yato_n('được thỏa mãn, được đầy đủ năm đối tượng của dục lạc và tận hưởng chúng')} {ITTHEKE_N}")
h("(Kha) tamañño evamāha",
  f"(b) {TAMANNO} {DASH} “{EXISTS}, {DENY}. {NOCA_N} {WHY} {cap(BHO)}, các dục lạc {ANICCA3}. Do sự biến đổi và trở "
  f"nên khác đi của chúng mà sinh khởi {SOKA}. {yato_n(JH[1])} {ITTHEKE_N}")
for _l, _lv, _why, _jh, _last in (("Ga", "c", "có sự hướng tâm, có sự duy trì tâm", 2, False),
                                  ("Gha", "d", "có sự hân hoan, có sự phấn khích của tâm", 3, False),
                                  ("Ṅa", "đ", "có hạnh phúc và sự hân hoan, có sự chú hướng của tâm", 4, True)):
    _line = (f"({_lv}) {TAMANNO} {DASH} “{EXISTS}. {cap(DENY)}. {NOCA_N} {WHY} Bởi vì ở đó {_why}, {GROSS}. "
             f"{yato_n(JH[_jh])} {ITTHEKE_N}")
    if _last:
        _line += f" Đây là {g(5, 'dnv')}."
    h(f"({_l}) tamañño evamāha", _line)
SLIPS.append("^2-943 (Ṅa) 'sukhapīti cetaso ābhogo' (the sutta has 'sukhamiti'): as written «hạnh phúc và sự hân "
             "hoan, có sự chú hướng của tâm»")
SLIPS.append("^2-943 (Kha) 'yaṃ tvaṃ vadesi neso natthīti vadāmi' (no full stop, as in (Ga)-(Ṅa)): one sentence, "
             "as written")
SLIPS.append("^2-943 (Ka) '[evaṃdiṭṭhi (syā.)]' identical to the text word: kept as written")
h("Pañcakaṃ.", CLOSE[5])

# ---------------------------------------------------------------- Chakkaniddeso
hd(4, "Chakkaniddeso", "Giải thích phân loại theo nhóm sáu")
hd(5, "(1) Cha vivādamūlāni", "(1) " + cap(g(6, "vivādamūla")))
tq("āni cha vivādamūlāni?", g(6, "vivādamūla"),
   f"{cap(N['kodho'])}, {N['makkho']}, {N['issā']}, {N['sāṭheyyaṃ']}, {N['pāpicchatā']}, sự bám chặt quan điểm của mình "
   f"{DASH} đây là {g(6, 'vivādamūla')}.")
MANAP, AMANAP = "đáng ưa thích", "không đáng ưa thích"                              # manāpiya [sample manāpa]
UPEKT = "làm khởi lên sự bình thản"                                                  # upekkhāṭṭhāniya [new]
OBJ = list(VED)


def six(fmt_first, fmt_last, adj):
    """'X-esu rūpesu …, X-esu saddesu…pe… … X-esu dhammesu …' -> «đối với các hình sắc …, … đối với các đối tượng …»"""
    mids = "… ".join(f"đối với {VED[o]} {adj}" for o in OBJ[1:5])
    return f"{fmt_first.format(o=f'Đối với {VED[OBJ[0]]} {adj}')}, {mids}… {fmt_last.format(o=f'đối với {VED[OBJ[5]]} {adj}')}"


hd(5, "(2) Cha chandarāgā", "(2) " + cap(g(6, "chandarāga")))
_cr = f"{RAGA3} {GEH}"
tq("e cha chandarāgā?", g(6, "chandarāga"),
   f"Các {GN['chandarāga']} là những hiện tượng {GEH}. " + six("{o}, " + _cr, "{o}, " + _cr, MANAP) +
   f" {DASH} đây là {g(6, 'chandarāga')}.")
hd(5, "(3) Cha virodhavatthūni", "(3) " + cap(g(6, "virodhavatthu")))
_VR = "sự oán giận của tâm, sự phẫn uất, sự hung dữ, sự nói năng cộc cằn, sự không hài lòng của tâm"   # [pi-1 ^1-1066 words]
assert all(x in DOSA_SYN for x in ("sự oán giận của tâm, sự phẫn uất", "sự hung dữ, sự nói năng cộc cằn, sự không hài lòng của tâm"))
tq("āni cha virodhavatthūni?", g(6, "virodhavatthu"), six("{o}, " + _VR, "{o}, " + _VR, AMANAP) +
   f" {DASH} đây là {g(6, 'virodhavatthu')}.")
hd(5, "(4) Cha taṇhākāyā", "(4) " + cap(g(6, "taṇhākāya")))
TK6 = ["khao khát hình sắc", "khao khát âm thanh", "khao khát mùi", "khao khát vị", "khao khát vật xúc chạm",
       "khao khát đối tượng của ý"]                                                  # [pi-1 ^1-1065]
for _v in TK6:
    assert _v in LOBHA, _v
tq("e cha taṇhākāyā?", g(6, "taṇhākāya"), f"{cap(', '.join(TK6))} {DASH} đây là {g(6, 'taṇhākāya')}.")
hd(5, "(5) Cha agāravā", "(5) " + cap(g(6, "agārava")))
_AGR = ["Bậc Đạo Sư", "Giáo Pháp", "Tăng đoàn", "sự tu học", "sự không buông thả", "sự niềm nở tiếp đón"]
tq("e cha agāravā?", g(6, "agārava"), "; ".join(
    f"{'Người ta sống' if i == 0 else 'sống'} thiếu kính trọng, không vâng lời đối với {x}" for i, x in enumerate(_AGR))
   + f" {DASH} đây là {g(6, 'agārava')}.")
ARAMA = {"kamma": "công việc", "bhassa": "nói chuyện", "niddā": "ngủ nghỉ", "saṅgaṇika": "tụ tập",
         "saṃsagga": "giao du", "papañca": "suy diễn lan man"}
_ar = [f"sự ưa thích {v}" for v in ARAMA.values()]
hd(5, "(6) Cha parihāniyā dhammā", "(6) " + cap(g(6, "parihāniya")))
tq("e cha parihāniyā dhammā?", g(6, "parihāniya"), f"{cap(', '.join(_ar))} {DASH} đây là {g(6, 'parihāniya')}.")
hd(5, "(7) Aparepi cha parihāniyā dhammā", "(7) " + cap(g(6, "parihāniya", True)))
tq("e aparepi cha parihāniyā dhammā?", g(6, "parihāniya", True),
   f"{cap(', '.join(_ar[:4] + [N['dovacassatā'], N['pāpamittatā']]))} {DASH} đây là {g(6, 'parihāniya')}.")
SENSE = ["khi thấy hình sắc bằng mắt", "khi nghe âm thanh bằng tai", "khi ngửi mùi bằng mũi", "khi nếm vị bằng lưỡi",
         "khi chạm vật xúc chạm bằng thân", "khi nhận biết đối tượng của ý bằng ý"]  # [pi-1 ^1-1352]
assert all(x in INDRI for x in ("khi thấy hình sắc bằng mắt", "Khi nghe âm thanh bằng tai… khi ngửi mùi bằng mũi… "
                                "khi nếm vị bằng lưỡi… khi chạm vật xúc chạm bằng thân… khi nhận biết đối tượng của ý "
                                "bằng ý"))
for _num, _k, _key, _w in ((8, "su", "somanass", "làm khởi lên niềm vui"), (9, "du", "domanass", "làm khởi lên nỗi buồn"),
                           (10, "uu", "upekkh", UPEKT)):
    hd(5, f"({_num}) Cha {_key}upavicārā", f"({_num}) {cap(g(6, _k))}")
    _s = (f"{cap(SENSE[0])}, người ta lưu tâm đến hình sắc {_w}, " + "… ".join(SENSE[1:]) +
          f", người ta lưu tâm đến đối tượng của ý {_w}")
    tq(f"e cha {_key}upavicārā?", g(6, _k), f"{_s} {DASH} đây là {g(6, _k)}.")
for _num, _k, _q, _adj, _body in ((11, "gs", "āni cha gehasitāni somanassāni?", MANAP, SOMA),
                                  (12, "gd", "āni cha gehasitāni domanassāni?", AMANAP, DOMA),
                                  (13, "gu", "ā cha gehasitā upekkhā?", UPEKT, UPEK)):
    hd(5, f"({_num}) Cha gehasit" + {"gs": "āni somanassāni", "gd": "āni domanassāni", "gu": "ā upekkhā"}[_k],
       f"({_num}) {cap(g(6, _k))}")
    _f = "{o}, điều " + GEH + " là " + _body
    tq(_q, g(6, _k), six(_f, _f, _adj) + f" {DASH} đây là {g(6, _k)}.")
hd(5, "(14) Cha diṭṭhiyo", "(14) " + cap(g(6, "diṭṭhi")))
_C6 = ["Tôi có tự ngã", "Tôi không có tự ngã", "Tôi nhận biết tự ngã bằng tự ngã",
       "Tôi nhận biết cái không phải tự ngã bằng tự ngã", "Tôi nhận biết tự ngã bằng cái không phải tự ngã"]
_c6 = "; ".join(f"{'H' if i == 0 else 'h'}oặc quan điểm “{x}” khởi lên nơi người ấy {TRUE}" for i, x in enumerate(_C6))
tq("ā cha diṭṭhiyo?", g(6, "diṭṭhi"),
   f"{_c6}; hoặc nữa, người ấy có quan điểm như vầy {DASH} “Chính tự ngã này của tôi là cái nói, cái cảm nhận, cái trải "
   f"nghiệm quả của các nghiệp tốt và xấu ở chỗ này chỗ kia trong thời gian dài. Nó không sinh ra, không phải trước đây "
   f"không có; nó không sinh ra, không phải về sau sẽ không có; nó thường còn, bền vững, trường tồn, có bản chất không "
   f"biến đổi”, hoặc quan điểm ấy khởi lên nơi người ấy {TRUE}. Đây là {g(6, 'diṭṭhi')}.")
h("Chakkaṃ.", CLOSE[6])

# ---------------------------------------------------------------- Sattakaniddeso
hd(4, "Sattakaniddeso", "Giải thích phân loại theo nhóm bảy")
ANU7 = ["khuynh hướng tiềm ẩn tham đắm dục lạc", "khuynh hướng tiềm ẩn ác cảm", "khuynh hướng tiềm ẩn kiêu mạn",
        "khuynh hướng tiềm ẩn quan điểm", "khuynh hướng tiềm ẩn hoài nghi", "khuynh hướng tiềm ẩn tham đắm hiện hữu",
        "khuynh hướng tiềm ẩn vô minh"]                                              # [ch16 ^2-816]
in_out("16-nanavibhango.md", ", ".join(ANU7[:6]) + " và " + ANU7[6])
hd(5, "(1) Sattānusayā", "(1) " + cap(g(7, "anusaya")))
tq("e sattānusayā?", g(7, "anusaya"), f"{cap(', '.join(ANU7))} {DASH} đây là {g(7, 'anusaya')}.")
_S10 = SAMYO10.split(", ")
_S7 = [_S10[i] for i in (0, 1, 2, 3, 4, 6, 9)]
hd(5, "(2) Satta saṃyojanāni", "(2) " + cap(g(7, "saṃyojana")))
tq("āni satta saṃyojanāni?", g(7, "saṃyojana"), f"{cap(', '.join(_S7))} {DASH} đây là {g(7, 'saṃyojana')}.")
_PY = ["tham đắm dục lạc", "ác cảm", "kiêu mạn", "quan điểm", "hoài nghi", "tham đắm hiện hữu", "vô minh"]
hd(5, "(3) Satta pariyuṭṭhānāni", "(3) " + cap(g(7, "pariyuṭṭhāna")))
tq("āni satta pariyuṭṭhānāni?", g(7, "pariyuṭṭhāna"), ", ".join(f"{'S' if i == 0 else 's'}ự ám ảnh của {x}"
                                                                for i, x in enumerate(_PY)) +
   f" {DASH} đây là {g(7, 'pariyuṭṭhāna')}.")
assert "sự ám ảnh của vô minh" in MOHA_PI1
hd(5, "(4) Satta asaddhammā", "(4) " + cap(g(7, "asaddhamma")))
tq("e satta asaddhammā?", g(7, "asaddhamma"),
   f"Là người không có niềm tin, là người không biết hổ thẹn, là người không biết ghê sợ tội lỗi, là người ít học hỏi, "
   f"là người lười biếng, là người mất tỉnh thức, là người kém trí tuệ {DASH} đây là {g(7, 'asaddhamma')}.")
hd(5, "(5) Satta duccaritāni", "(5) " + cap(g(7, "duccarita")))
tq("āni satta duccaritāni?", g(7, "duccarita"), f"{cap(', '.join(PANA3 + VACI4))} {DASH} đây là {g(7, 'duccarita')}.")
hd(5, "(6) Satta mānā", "(6) " + cap(g(7, "māna")))
tq("e satta mānā?", g(7, "māna"), cap(", ".join(N[k] for k in ("māno", "atimāno", "mānātimāno", "omāno", "adhimāno",
                                                               "asmimāno", "micchāmāno"))) + f" {DASH} đây là "
                                                                                            f"{g(7, 'māna')}.")
hd(5, "(7) Satta diṭṭhiyo", "(7) " + cap(g(7, "diṭṭhi")))
CUT_ATTA = "hoàn toàn bị đoạn diệt"                                                  # sammā samucchinno [new]
DIES = "sau khi thân tan rã thì bị đoạn diệt, bị hủy diệt, không còn tồn tại sau khi chết"
ITTHEKE_U = f"Như vậy, một số người trình bày {CUT}."
NOCA_U = f"Nhưng {BHO}, tự ngã này không phải chỉ đến chừng ấy là {CUT_ATTA}."
OTHER = f"{cap(BHO)}, có một tự ngã khác"
NOTKNOW = "Ngài không biết, không thấy tự ngã ấy. Tôi biết, tôi thấy tự ngã ấy."
SOKHO = (f"{cap(BHO)}, khi tự ngã ấy, sau khi thân tan rã, bị đoạn diệt, bị hủy diệt, không còn tồn tại sau khi chết, "
         f"{BHO}, chỉ đến chừng ấy là tự ngã này {CUT_ATTA}”.")
h("(Ka) tattha katamā satta diṭṭhiyo?",
  f"(a) {q(g(7, 'diṭṭhi'), lower=True)} {SB} {DASH} “{cap(BHO)}, khi tự ngã này có hình sắc, gồm bốn yếu tố cơ "
  f"bản{VAR_CATUMAHA}, do cha mẹ sinh ra, {DIES}, {BHO}, chỉ đến chừng ấy là tự ngã này {CUT_ATTA}”. {ITTHEKE_U}")
_DENY_Q = "Tôi không nói rằng ‘Nó không tồn tại’."
_SEVEN = [("Kha", "b", "thuộc cõi trời, có hình sắc, thuộc cõi dục lạc, dùng thức ăn trong vai trò dưỡng chất"),
          ("Ga", "c", "thuộc cõi trời, có hình sắc, do ý tạo thành, đầy đủ mọi bộ phận lớn nhỏ, có các năng lực không "
                      "khiếm khuyết"),
          ("Gha", "d", f"{ARUPA1}, với ý nghĩ ‘Không gian là vô tận’, đạt đến lĩnh vực không gian vô tận"),
          ("Ṅa", "đ", "hoàn toàn vượt qua lĩnh vực không gian vô tận, với ý nghĩ ‘Thức là vô tận’, đạt đến lĩnh vực "
                      "thức vô tận"),
          ("Ca", "e", "hoàn toàn vượt qua lĩnh vực thức vô tận, với ý nghĩ ‘Không có gì cả’, đạt đến lĩnh vực không có "
                      "gì cả"),
          ("Cha", "g", "hoàn toàn vượt qua lĩnh vực không có gì cả, đạt đến lĩnh vực không phải tri giác cũng không "
                       "phải không tri giác")]
in_out("12-jhanavibhango.md", "lĩnh vực không gian vô tận", "lĩnh vực thức vô tận", "lĩnh vực không có gì cả")
for _l, _lv, _x in _SEVEN:
    _ex = EXISTS if _l != "Cha" else "Quả thật, tự ngã mà ngài nói ấy có tồn tại"
    _line = f"({_lv}) {TAMANNO} {DASH} “{_ex}. {_DENY_Q} {NOCA_U} {OTHER}, {_x}. {NOTKNOW} {SOKHO} {ITTHEKE_U}"
    if _l == "Cha":
        _line += f" Đây là {g(7, 'diṭṭhi')}."
    h(f"({_l}) tamañño evamāha", _line)
SLIPS.append("^2-951 (Cha) 'atthi kho pana eso attā' (no 'bho', the parallels have 'kho, bho'): as written «Quả thật, "
             "…»")
h("Sattakaṃ.", CLOSE[7])

# ---------------------------------------------------------------- Aṭṭhakaniddeso
hd(4, "Aṭṭhakaniddeso", "Giải thích phân loại theo nhóm tám")
_K10 = KILESA10.split(f" {DASH} ")[1].split(", ")
hd(5, "(1) Aṭṭha kilesavatthūni", "(1) " + cap(g(8, "kilesavatthu")))
tq("āni aṭṭha kilesavatthūni?", g(8, "kilesavatthu"), f"{cap(', '.join(_K10[:8]))} {DASH} đây là "
                                                      f"{g(8, 'kilesavatthu')}.")
hd(5, "(2) Aṭṭha kusītavatthūni", "(2) " + cap(g(8, "kusītavatthu")))
h("Tattha katamāni aṭṭha kusītavatthūni?", q(g(8, "kusītavatthu")))
NOEFF = ("Vị ấy nằm nghỉ; không khởi động tinh tấn để đạt được điều chưa đạt được, để chứng đắc điều chưa chứng đắc, để "
         "chứng nghiệm điều chưa chứng nghiệm.")
LIE = "Vậy ta hãy nằm nghỉ"
ORD = ["thứ nhất", "thứ hai", "thứ ba", "thứ tư", "thứ năm", "thứ sáu", "thứ bảy", "thứ tám"]
THINKS = "Vị ấy nghĩ như vầy"
PUNA = "lại nữa, vị tỳ-khưu"
_KU = [
    ("Ka", "a", f"ở đời này, vị tỳ-khưu có việc phải làm. {THINKS} {DASH} “Ta sẽ phải làm việc. Nhưng khi ta làm việc "
                f"thì thân sẽ mệt mỏi. {LIE}”."),
    ("Kha", "b", f"{PUNA} đã làm xong việc. {THINKS} {DASH} “Ta đã làm việc. Nhưng khi ta làm việc thì thân đã mệt mỏi. "
                 f"{LIE}”."),
    ("Ga", "c", f"{PUNA} có đường phải đi. {THINKS} {DASH} “Ta sẽ phải đi đường. Nhưng khi ta đi đường thì thân sẽ mệt "
                f"mỏi. {LIE}”."),
    ("Gha", "d", f"{PUNA} đã đi đường xong. {THINKS} {DASH} “Ta đã đi đường. Nhưng khi ta đi đường thì thân đã mệt mỏi. "
                 f"{LIE}”."),
    ("Ṅa", "đ", f"{PUNA} đi khất thực trong làng hay thị trấn mà không nhận được đầy đủ thức ăn, thô hay ngon, như mình "
                f"cần. {THINKS} {DASH} “Ta đi khất thực trong làng hay thị trấn mà không nhận được đầy đủ thức ăn, thô hay "
                f"ngon, như mình cần. Thân ta mệt mỏi, không dễ vận dụng. {LIE}”."),
    ("Ca", "e", f"{PUNA} đi khất thực trong làng hay thị trấn và nhận được đầy đủ thức ăn, thô hay ngon, như mình cần. "
                f"{THINKS} {DASH} “Ta đi khất thực trong làng hay thị trấn và đã nhận được đầy đủ thức ăn, thô hay ngon, "
                f"như mình cần. Thân ta mệt mỏi, không dễ vận dụng, nặng nề như hạt đậu ngâm nước. {LIE}”."),
    ("Cha", "g", f"{PUNA} phát sinh một chứng bệnh nhẹ. {THINKS} {DASH} “Ta đã phát sinh chứng bệnh nhẹ này. Có lý do "
                 f"chính đáng để nằm nghỉ. {LIE}”."),
    ("Ja", "h", f"{PUNA} mới khỏi bệnh{VAR_GILANA}, vừa khỏi bệnh chưa lâu. {THINKS} {DASH} “Ta mới khỏi bệnh, vừa khỏi "
                f"bệnh chưa lâu. Thân ta yếu ớt, không dễ vận dụng. {LIE}”."),
]
for _j, (_l, _lv, _t) in enumerate(_KU):
    _line = f"({_lv}) {_t} {NOEFF} Đây là chỗ dựa {ORD[_j]} của sự lười biếng."
    if _l == "Ja":
        _line += f" Đây là {g(8, 'kusītavatthu')}."
    h(f"({_l}) " + ("idha bhikkhunā" if _l == "Ka" else "puna caparaṃ"), _line)
hd(5, "(3) Aṭṭhasu lokadhammesu cittassa paṭighāto", "(3) " + cap(GN["lokadhamma"]))
_LD = [("được lợi lộc", "mất lợi lộc"), ("được danh tiếng", "mất danh tiếng"), ("được khen ngợi", "bị chê trách"),
       ("được hạnh phúc", "gặp khổ đau")]
_ld = ", ".join(f"{'S' if i == 0 else 's'}ự say đắm khi {a}, sự đối nghịch khi {b}" for i, (a, b) in enumerate(_LD))
h("Tattha katamesu aṭṭhasu lokadhammesu cittassa paṭighāto?",
  f"Ở đây, {GN['lokadhamma']} là gì? {_ld} {DASH} đây là {GN['lokadhamma']}.")
hd(5, "(4) Aṭṭhaanariyavohārā", "(4) " + cap(g(8, "anariyavohāra")))
tq("e aṭṭha anariyavohārā?", g(8, "anariyavohāra"), f"{cap(', '.join(AV1 + AV2))} {DASH} đây là "
                                                    f"{g(8, 'anariyavohāra')}.")
hd(5, "(5) Aṭṭha micchattā", "(5) " + cap(g(8, "micchatta")))
tq("e aṭṭha micchattā?", g(8, "micchatta"), f"{cap(', '.join(MICCHA8))} {DASH} đây là {g(8, 'micchatta')}.")
hd(5, "(6) Aṭṭha purisadosā", "(6) " + cap(g(8, "purisadosa")))
ACC = "các tỳ-khưu buộc tội một tỳ-khưu về một lỗi vi phạm"                          # bhikkhū bhikkhuṃ āpattiyā codenti
ACCD = "Tỳ-khưu ấy, khi bị các tỳ-khưu buộc tội về lỗi vi phạm"


def pd(j):
    return f"Đây là lỗi {ORD[j]} của con người."


_PD = [
    f"{ACCD}{VAR_CODIYA}, chối bỏ với lý do không nhớ: “Tôi không nhớ, tôi không nhớ”.",
    f"{ACCD}, chống lại chính người buộc tội {DASH} “Lời nói của một kẻ ngu dốt, thiếu hiểu biết như ông thì có ích gì! "
    f"Ông mà cũng nghĩ rằng ông có thể nói tôi sao”!",
    f"{ACCD}, buộc tội ngược lại chính người buộc tội{VAR_CODAKA} {DASH} “Chính ông cũng đã phạm lỗi có tên như thế "
    f"này. Ông hãy sửa lỗi trước đi”.",
    f"{ACCD}, lảng tránh bằng cách nói chuyện này sang chuyện khác, đưa câu chuyện ra ngoài đề tài, để lộ sự nổi nóng, "
    f"sự sân hận và sự bất mãn.",
    f"{ACCD}, vung tay mà nói giữa Tăng đoàn.",
    f"{ACCD}, không đếm xỉa đến Tăng đoàn, không đếm xỉa đến người buộc tội, vẫn mang lỗi{VAR_SAPATTI} mà bỏ đi đâu "
    f"tùy ý.",
    f"{ACCD}, nói rằng “Tôi không phạm lỗi, mà tôi cũng không phải không phạm lỗi” rồi im lặng làm phiền Tăng đoàn.",
    f"{ACCD}, nói như vầy {DASH} “Sao các tôn giả lại quá bận tâm về tôi như vậy? Bây giờ tôi sẽ từ bỏ sự tu học, quay "
    f"về đời sống thấp kém”. Vị ấy từ bỏ sự tu học, quay về đời sống thấp kém rồi nói như vầy {DASH} “Bây giờ các tôn "
    f"giả hãy hài lòng đi”.",
]
SLIPS.append("^2-957 (Ja) '… mayi byāvaṭā.' (a 'kiṃ nu kho' question closed with a full stop): rendered with «?»")
SLIPS.append("^2-957 (Ka) '[codiyamāno (sī. syā.) a. ni. 8.14]' identical to the text word: kept as written")
for _j, _l in enumerate(("Ka", "Kha", "Ga", "Gha", "Ṅa", "Ca", "Cha", "Ja")):
    _lv = ("a", "b", "c", "d", "đ", "e", "g", "h")[_j]                          # Vietnamese order (no f)
    if _l == "Ka":
        _line = f"Ở đây, {g(8, 'purisadosa')} là gì? ({_lv}) ở đời này, {ACC}. {_PD[0]} {pd(0)}"
        h("Tattha katame aṭṭha purisadosā?", _line)
    else:
        _line = f"({_lv}) lại nữa, {ACC}. {_PD[_j]} {pd(_j)}"
        if _l == "Ja":
            _line += f" Đây là {g(8, 'purisadosa')}."
        h(f"({_l}) puna caparaṃ bhikkhū", _line)
SDF = "không bệnh tật sau khi chết"
ATTA8 = [("có hình sắc", True), ("không có hình sắc", False), ("vừa có hình sắc vừa không có hình sắc", False),
         ("không phải có hình sắc cũng không phải không có hình sắc", False), ("hữu hạn", True), ("vô hạn", True),
         ("vừa hữu hạn vừa vô hạn", True), ("không phải hữu hạn cũng không phải vô hạn", True)]


def asanni(kind, pe):
    tag = "không có tri giác" if kind == "a" else "không phải có tri giác cũng không phải không có tri giác"
    claim = f"họ trình bày rằng nó {tag}"
    parts = []
    for j, (x, _) in enumerate(ATTA8):
        if pe and j in (1, 2, 3):
            parts.append(f"tự ngã {x}…")
            continue
        parts.append(f"“{ATTA} {x}, {SDF}” {DASH} {claim}")
    if pe:
        return f"{parts[0]}; {parts[1]} {parts[2]} {parts[3]} " + "; ".join(parts[4:])
    return "; ".join(parts)


hd(5, "(7) Aṭṭha asaññīvādā", "(7) " + cap(g(8, "asaññī")))
tq("e aṭṭha asaññīvādā?", g(8, "asaññī"), f"{asanni('a', True)}. Đây là {g(8, 'asaññī')}.")
hd(5, "(8) Aṭṭha nevasaññīnāsaññīvādā", "(8) " + cap(g(8, "nevasaññī")))
tq("e aṭṭha nevasaññīnāsaññīvādā?", g(8, "nevasaññī"), f"{asanni('n', False)}. Đây là {g(8, 'nevasaññī')}.")
h("Aṭṭhakaṃ.", CLOSE[8])

# ---------------------------------------------------------------- Navakaniddeso
hd(4, "Navakaniddeso", "Giải thích phân loại theo nhóm chín")
hd(5, "(1) Nava āghātavatthūni", "(1) " + cap(g(9, "āghātavatthu")))
tq("āni nava āghātavatthūni?", g(9, "āghātavatthu"), f"{AGHATA9}. Đây là {g(9, 'āghātavatthu')}.")
hd(5, "(2) Nava purisamalāni", "(2) " + cap(g(9, "purisamala")))
tq("āni nava purisamalāni?", g(9, "purisamala"),
   cap(", ".join([N["kodho"], N["makkho"], N["issā"], N["macchariyaṃ"], N["māyā"], N["sāṭheyyaṃ"], VACI4[0],
                  N["pāpicchatā"], N["micchādiṭṭhi"]])) + f" {DASH} đây là {g(9, 'purisamala')}.")
hd(5, "(3) Navavidhā mānā", "(3) " + cap(g(9, "māna")))
_M9 = [N[f"{w} {o}hamasmīti māno"] for w in ("seyyassa", "sadisassa", "hīnassa") for o in ("seyyo", "sadiso", "hīno")]
tq("e navavidhā mānā?", g(9, "māna"), f"{cap(', '.join(_M9))} {DASH} đây là {g(9, 'māna')}.")
hd(5, "(4) Nava taṇhāmūlakā dhammā", "(4) " + cap(g(9, "taṇhāmūlaka")))
_TM = ["khao khát", "sự tìm cầu khắp nơi", "lợi lộc", "sự phán định", "sự tham đắm do ý muốn", "sự đắm chìm",
       "sự chiếm hữu", "sự keo kiệt", "sự canh giữ"]
_tm = ", ".join(f"{'D' if i == 0 else 'd'}ựa vào {a} mà có {b}" for i, (a, b) in enumerate(zip(_TM, _TM[1:])))
tq("e nava taṇhāmūlakā dhammā?", g(9, "taṇhāmūlaka"),
   f"{_tm}, vì sự canh giữ mà sinh khởi nhiều hiện tượng xấu ác bất thiện: cầm gậy, cầm dao, cãi cọ, xung đột, tranh "
   f"chấp, gọi nhau mày tao, nói lời đâm thọc, nói dối {DASH} đây là {g(9, 'taṇhāmūlaka')}.")
I9 = ["Tôi là", "Chính tôi là", "Tôi là cái này", "Tôi sẽ là", "Tôi sẽ có hình sắc", "Tôi sẽ không có hình sắc",
      "Tôi sẽ có tri giác", "Tôi sẽ không có tri giác", "Tôi sẽ không phải có tri giác cũng không phải không có tri giác"]
hd(5, "(5) Nava iñjitāni", "(5) " + cap(g(9, "iñjita")))
tq("āni nava iñjitāni?", g(9, "iñjita"), ", ".join(f"“{x}” là một {GN['iñjita']}" for x in I9) +
   f" {DASH} đây là {g(9, 'iñjita')}.")
SLIPS.append("^2-964 comma missing before '\"bhavissa\"nti iñjitametaṃ': punctuation only")
hd(5, "(6-9) Nava maññitādīni", f"(6-9) {cap(g(9, 'maññita'))} và những điều tương tự")
h("Tattha katamāni nava maññitāni…",
  f"Ở đây, {g(9, 'maññita')}… {g(9, 'phandita')}… {g(9, 'papañcita')}… {g(9, 'saṅkhata')} là gì? " +
  ", ".join(f"“{x}” là một {GN['saṅkhata']}" for x in I9) + f" {DASH} đây là {g(9, 'saṅkhata')}.")
h("Navakaṃ.", CLOSE[9])

# ---------------------------------------------------------------- Dasakaniddeso
hd(4, "Dasakaniddeso", "Giải thích phân loại theo nhóm mười")
hd(5, "(1) Dasa kilesavatthūni", "(1) " + cap(g(10, "kilesavatthu")))
tq("āni dasa kilesavatthūni?", g(10, "kilesavatthu"), f"{cap(', '.join(_K10))} {DASH} đây là {g(10, 'kilesavatthu')}.")
hd(5, "(2) Dasa āghātavatthūni", "(2) " + cap(g(10, "āghātavatthu")))
tq("āni dasa āghātavatthūni?", g(10, "āghātavatthu"), f"{AGHATA10} {DASH} đây là {g(10, 'āghātavatthu')}.")
hd(5, "(3) Dasa akusalakammapathā", "(3) " + cap(g(10, "kammapatha")))
tq("e dasa akusalakammapathā?", g(10, "kammapatha"), f"{cap(', '.join(PANA3 + VACI4 + MANO3))} {DASH} đây là "
                                                     f"{g(10, 'kammapatha')}.")
hd(5, "(4) Dasa saṃyojanāni", "(4) " + cap(g(10, "saṃyojana")))
tq("āni dasa saṃyojanāni?", g(10, "saṃyojana"), f"{cap(SAMYO10)} {DASH} đây là {g(10, 'saṃyojana')}.")
hd(5, "(5) Dasa micchattā", "(5) " + cap(g(10, "micchatta")))
tq("e dasa micchattā?", g(10, "micchatta"), f"{cap(', '.join(MICCHA8 + ['hiểu biết sai lầm', 'sự giải thoát sai lầm']))}"
                                            f" {DASH} đây là {g(10, 'micchatta')}.")
hd(5, "(6) Dasavatthukā micchādiṭṭhi", "(6) " + cap(GN["dv_micchā"]))
tq("ā dasavatthukā micchādiṭṭhi?", GN["dv_micchā"], f"{NATTHI_V} {DASH} đây là {GN['dv_micchā']}.")
hd(5, "(7) Dasavatthukā antaggāhikā diṭṭhi", "(7) " + cap(GN["dv_anta"]))
tq("ā dasavatthukā antaggāhikā diṭṭhi?", GN["dv_anta"], f"{VIEWS10} {DASH} đây là {GN['dv_anta']}.")
h("Dasakaṃ.", CLOSE[10])

# ---------------------------------------------------------------- Taṇhāvicaritaniddeso
hd(4, "Taṇhāvicaritaniddeso", f"Giải thích các {TV}")
hd(5, "(1) Ajjhattikassa upādāya", "(1) " + cap(IN_UP))
_list18 = ", ".join(cap(thought(k, False)) if i == 0 else thought(k, False) for i, k in enumerate(ORDER18))
h("Tattha katamāni aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya?",
  f"Ở đây, mười tám {TV} {IN_UP} là gì? {_list18}.")
SLIPS.append("^2-974 internal (7) closes with 'evaṃ bhavissanti hoti' (the parallels: 'evaṃ evaṃ …'): as written "
             "«có ý nghĩ “Tôi cũng sẽ giống như thế”» without «như vậy là»")
_IN = [
    (None, "asmi", dict(var=VAR_ANAVAKARI)), (2, "itthasmi", dict(shape="full")),
    (3, "evasmi", dict(shape="full", var=VAR_PARAPUGGALA)), (4, "aññathāsmi", dict(shape="full")),
    (5, "bhavissaṃ", {}), (6, "itthaṃ bhavissaṃ", dict(shape="full")),
    (7, "evaṃ bhavissaṃ", dict(shape="abbr", closing=thought("evaṃ bhavissaṃ", False))),
    (8, "aññathā bhavissaṃ", dict(shape="abbr")), (9, "asasmi", {}), (10, "sātasmi", {}), (11, "siyaṃ", {}),
    (12, "itthaṃ siyaṃ", dict(shape="full")), (13, "evaṃ siyaṃ", dict(shape="abbr")),
    (14, "aññathā siyaṃ", dict(shape="abbr")), (15, "apāhaṃ siyaṃ", {}),
    (16, "apāhaṃ itthaṃ siyaṃ", dict(shape="full")), (17, "apāhaṃ evaṃ siyaṃ", dict(shape="abbr")),
    (18, "aññathā siyaṃ", None)]
_IN[-1] = (18, "apāhaṃ aññathā siyaṃ", dict(shape="abbr"))
_lines_in = [tv_line(n, k, False, **kw) for n, k, kw in _IN]
_lines_in[15] = _lines_in[15] + " " + _lines_in.pop(16)                            # (16) and (17) share a line
_PK_IN = ["Kathañca asmīti hoti?", "(2) Kathañca itthasmīti", "(3) Kathañca evasmīti", "(4) Kathañca aññathāsmīti",
          "(5) Kathañca bhavissanti", "(6) Kathañca itthaṃ bhavissanti", "(7) Kathañca evaṃ bhavissanti",
          "(8) Kathañca aññathā bhavissanti", "(9) Kathañca asasmīti", "(10) Kathañca sātasmīti",
          "(11) Kathañca siyanti", "(12) Kathañca itthaṃ siyanti", "(13) Kathañca evaṃ siyanti",
          "(14) Kathañca aññathā siyanti", "(15) Kathañca apāhaṃ siyanti", "(16) Kathañca apāhaṃ itthaṃ siyanti",
          "(18) Kathañca apāhaṃ aññathā siyanti"]
for _pk, _vl in zip(_PK_IN, _lines_in):
    h(_pk, _vl)
h("Imāni aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya.", f"Đây là mười tám {TV} {IN_UP}.")
hd(5, "(2) Bāhirassa upādāya", "(2) " + cap(OUT_UP))
_list18b = ", ".join(cap(thought(k, True)) if i == 0 else thought(k, True) for i, k in enumerate(ORDER18))
h("Tattha katamāni aṭṭhārasa taṇhāvicaritāni bāhirassa upādāya?",
  f"Ở đây, mười tám {TV} {OUT_UP} là gì? {_list18b}.")
_OUT = [(1, "asmi", {}), (2, "itthasmi", dict(shape="full")), (3, "evasmi", dict(shape="abbr")),
        (4, "aññathāsmi", dict(shape="abbr")), (5, "bhavissaṃ", {}), (6, "itthaṃ bhavissaṃ", dict(shape="b6")),
        (7, "evaṃ bhavissaṃ", dict(shape="abbr")), (8, "aññathā bhavissaṃ", dict(shape="abbr")),
        (9, "asasmi", dict(var=VAR_AVAKARI)), (10, "sātasmi", {}), (11, "siyaṃ", {}),
        (12, "itthaṃ siyaṃ", dict(shape="full")), (13, "evaṃ siyaṃ", dict(shape="abbr")),
        (14, "aññathā siyaṃ", dict(shape="abbr")), (15, "apāhaṃ siyaṃ", {}),
        (16, "apāhaṃ itthaṃ siyaṃ", dict(shape="full")), (17, "apāhaṃ evaṃ siyaṃ", dict(shape="abbr")),
        (18, "apāhaṃ aññathā siyaṃ", dict(shape="abbr"))]
for _n, _k, _kw in _OUT:
    _pk = {"asmi": "asmīti", "itthasmi": "itthasmīti", "evasmi": "evasmīti", "aññathāsmi": "aññathāsmīti",
           "asasmi": "asasmīti", "sātasmi": "sātasmīti"}.get(_k, _k.replace("bhavissaṃ", "bhavissanti")
                                                              .replace("siyaṃ", "siyanti"))
    h(f"({_n}) Kathañca iminā {_pk} hoti?", tv_line(_n, _k, True, **_kw))
h("Imāni aṭṭhārasa taṇhāvicaritāni bāhirassa upādāya.", f"Đây là mười tám {TV} {OUT_UP}.")
h("Iti imāni aṭṭhārasa taṇhāvicaritāni ajjhattikassa upādāya",
  f"Như vậy, mười tám {TV} này {IN_UP}, mười tám {TV} này {OUT_UP}, {GOM}, thành ba mươi sáu {TV}. Như vậy, ba mươi sáu "
  f"{TV} thuộc loại như thế thuộc quá khứ, ba mươi sáu {TV} thuộc tương lai, ba mươi sáu {TV} thuộc hiện tại, {GOM}, "
  f"thành một trăm lẻ tám {TV}.")
VADA = ["bốn học thuyết trường tồn", "bốn học thuyết trường tồn một phần", "bốn học thuyết về hữu hạn và vô hạn",
        "bốn học thuyết lẩn tránh như lươn", "hai học thuyết sinh khởi ngẫu nhiên",
        "mười sáu học thuyết cho rằng tự ngã có tri giác", f"tám {GN['asaññī']}", f"tám {GN['nevasaññī']}",
        "bảy học thuyết đoạn diệt", f"năm {GN['dnv']}"]
_62 = f"sáu mươi hai quan điểm {BRAHMAJALA}"
h("Tattha katamāni dvāsaṭṭhi diṭṭhigatāni", f"Ở đây, {_62} là gì? {cap(', '.join(VADA))} {DASH} đây là {_62}.")
h("Khuddakavatthuvibhaṅgo niṭṭhito.", S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[17]))


# ================================================================ 8. translate
def matrix_vi(t):
    for k, (items_p, items_v) in MATRIX.items():
        if t.startswith(k):
            check_numbered(t, items_p)
            return numbered(items_v)
    raise KeyError(t[:60])


BAD = ("là là", "  ", "….", '"', " ,", " .", ":-", "thì thì", "\x01", " ;", ";;", ",,", "chánh niệm", "..", ", ,",
       "None", "—", "pe…", "“ ", " ”", "{", "}", "…,", "… ,")
PALI_LETTERS = re.compile(r"[āīūṃṅñṭḍṇḷ]")


def translate(pali_lines):
    hq = list(H)
    out = []
    for pl in pali_lines:
        if not pl.strip():
            out.append("")
            continue
        m = S.ID.search(pl)
        t = S.ID.sub("", pl).rstrip()
        assert hq, ("no hand line left for", t[:80])
        key, vi = hq.pop(0)
        if key.startswith("#"):
            assert t == key, ("heading", t, key)
        else:
            assert t.startswith(key), ("line", t[:90], key)
        if vi == "MATRIX":
            vi = matrix_vi(t)
        n_pe = t.count("…pe…") + len(re.findall(r"\w…(?!pe)", t.replace("…pe…", "")))
        assert pl.count(DASH) == vi.count(DASH), ("dash count", t[:70], pl.count(DASH), vi.count(DASH), vi[:200])
        for bad in BAD:
            assert bad not in vi, (bad, vi[:200], t[:60])
        assert not PALI_LETTERS.search(re.sub(r"\[[^\]]*\]", "", vi)), ("Pāli letters", vi[:200])
        assert vi.count("“") == vi.count("”") and vi.count("‘") == vi.count("’"), ("quotes", vi[:200])
        out.append(vi + (" " + m.group(1) if m else ""))
    assert not hq, [x[0][:50] for x in hq]
    return out


def build():
    pali = open(os.path.join(S.PALI_DIR, FN), encoding="utf-8").read().rstrip("\n").split("\n")
    return translate(pali)


HAND_SLIPS = [
    "^2-832 the matrix numbers lack a space in places ('(1)Jātimado', '(28)mado' …): no effect",
    "^2-900 (Kha) 'ottappitabbena na ottappati' (comma missing, ^2-U18 has it): same Vietnamese as pi-1",
    "^2-U21 pāpamittatā adds 'paṭisevanā' to the list: rendered «sự lui tới»",
    "^2-904 asākhalya 'kaṇḍakā' (pi-1 aṇḍakā): as written «gai góc»",
    "^2-909 lobha 'sotaṃ' (pi-1 suttaṃ «sợi chỉ»): as written «dòng nước»; 'saddataṇhā rūpataṇhā' order kept",
    "^2-892 the paḷāsa string has no 'paḷāsāyitattaṃ' (only in the Syā. variant): as written",
    "^2-860 / ^2-U31 thīyanā / thiyanā spellings: same Vietnamese",
]


def main():
    lines = build()
    dry = "--dry" in sys.argv
    path = os.path.join(S.VI_DIR, FN)
    if not dry:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines).rstrip("\n") + "\n")
    print("OK:" if not dry else "DRY:", path, "|", len([x for x in lines if x.strip()]), "non-empty lines")
    for s in sorted(set(SLIPS + HAND_SLIPS)):
        print("slip:", s)


if __name__ == "__main__":
    main()
