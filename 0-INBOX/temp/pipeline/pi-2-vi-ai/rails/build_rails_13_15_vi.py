"""Builder for the Vietnamese rails translation of pi-2 (Vibhaṅga, «Phân tích các hiện tượng», plain audience),
chapters 13 (Appamaññāvibhaṅgo ^2-13-0 … ^2-702), 14 (Sikkhāpadavibhaṅgo ^2-14-0 … ^2-717) and 15
(Paṭisambhidāvibhaṅgo ^2-15-0 … ^2-750).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/13-appamannavibhango.md
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/14-sikkhapadavibhango.md
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/15-patisambhidavibhango.md
  0-INBOX/temp/pipeline/pi-2-vi-ai/rails/notes-13-15.md   (new recurring formulas, Pāli = tiếng Việt)

Translated fresh from the Pāli with the locked pi-2 termbase (appamaññā «trạng thái không thể đo lường»; mettā «lòng từ
ái», karuṇā «lòng trắc ẩn», muditā «niềm vui đồng cảm», upekkhā «sự bình thản»; pharitvā viharati «an trú sau khi lan
tỏa khắp»; X veramaṇī sikkhāpadaṃ «điều tu học về sự kiềm chế X»; the paṭisambhidā names «hiểu biết thông suốt về ý
nghĩa / về các hiện tượng / về cách diễn đạt / về tài ứng đáp»). Shared strings are imported read-only from the
approved sample builder (S) and the chapter 1, 2-3, 4-5, 6, 7-9 and 10-12 builders (K1, K23, K45, K6, K79, K10); their
tables are extended only in memory, here. Passages that repeat the Dhammasaṅgaṇī reuse the approved pi-1 Vietnamese
rails (marked pi1() and asserted by check_pi1()); strings taken from the earlier pi-2 chapters are marked pi2() and
checked by check_pi2(). Importing this module writes nothing.

usage: python -I -X utf8 build_rails_13_15_vi.py
"""
import pathlib
import re
import sys
import unicodedata

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)
import build_rails_1_vi as K1      # noqa: E402  (importing writes nothing)
import build_rails_2_3_vi as K23   # noqa: E402  (importing writes nothing)
import build_rails_4_5_vi as K45   # noqa: E402  (importing writes nothing)
import build_rails_6_vi as K6      # noqa: E402  (importing writes nothing)
import build_rails_7_9_vi as K79   # noqa: E402  (importing writes nothing)
import build_rails_10_12_vi as K10  # noqa: E402  (importing writes nothing)

PARTS = {13: "13-appamannavibhango.md", 14: "14-sikkhapadavibhango.md", 15: "15-patisambhidavibhango.md"}
PI1_VI = S.ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
NOTES_PATH = RAILS / "notes-13-15.md"
cap, low, q = S.cap, K1.low, K23.q
CALLED, CALLED_PL = S.CALLED_SG, S.CALLED_PL          # «đó được gọi là» / «những điều này được gọi là»
WHICH = K23.WHICH                                     # Yo / Yā / Yaṃ … (definition) «Điều mà là»
TENA = K6.TENA                                        # Tena vuccati "…"ti «Vì thế, điều này được gọi là “…”»
SLIPS = []          # source slips met while building (reported)
MISFITS = []        # termbase gaps / misfits / sense choices (reported)
PI1_USED = []       # strings taken from the approved pi-1 Vietnamese rails (checked by check_pi1)
PI2_USED = []       # strings taken from the approved earlier pi-2 chapters (checked by check_pi2)
K10_SLIPS0 = list(K10.SLIPS)      # slips K10 records at import (its own chapters; not reported here)


def note(lst, s):
    if s not in lst:
        lst.append(s)


def slip(s):
    note(SLIPS, s)


def misfit(s):
    note(MISFITS, s)


def pi1(s):
    """mark a string as taken unchanged from the approved pi-1 Vietnamese rails (checked by check_pi1)"""
    note(PI1_USED, s)
    return s


def pi2(s):
    """mark a string as taken unchanged from the approved earlier pi-2 Vietnamese chapters (checked by check_pi2)"""
    note(PI2_USED, s)
    return s


# =========================================================================== shared strings (imported)
MONK_WHEN = K10.MONK_WHEN                      # «Ở đây, vào lúc một vị tỳ-khưu» (Idha bhikkhu yasmiṃ samaye)
THEN = K10.THEN                                # «thì vào lúc ấy»
WHAT_AT_TIME = K10.WHAT_AT_TIME                # «thì điều mà vào lúc ấy là»
CONTACT_PE = pi1(K10.CONTACT_PE)               # «có sự tiếp xúc… có sự không tán loạn»
ARE = {"kusalā": pi1("những hiện tượng này là thiện"), "akusalā": "những hiện tượng này là bất thiện",
       "abyākatā": pi1("những hiện tượng này không xác định về mặt đạo đức")}     # Ime dhammā X. (pi-1)
KIND_Q = K6.KIND_Q                             # Katame dhammā X? (pi-1)
ENTER = K10.ENTER                              # upasampajja viharati «chứng nhập và an trú»
ORDN = K10.ORDN                                # paṭhamaṃ … «thứ nhất» …
TOPIC_W, TOPIC_C = K79.TOPIC_W, K79.TOPIC_C    # «Về từ “x”:» / «Về câu “x”:»
VIHARATI_J = pi2(K10.VIHARATI_J)               # Iriyati … viharati. «Vị ấy vận động, …, an trú.» (ch. 12)
CITTA_FULL = pi2(K6.CITTA_FULL)                # Yaṃ cittaṃ mano … tajjāmanoviññāṇadhātu «Điều mà là tâm, ý, …»
CITTA_PE = f"{WHICH} {K79.CITTA_PE}"           # Yaṃ cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu
pi2(K79.CITTA_PE)
REST = "Các hiện tượng còn lại gắn liền với"     # Avasesā dhammā X sampayuttā (ch. 10-12)
pi2(REST)

# =========================================================================== chapter 13: the measureless states
AP = ["mettā", "karuṇā", "muditā", "upekkhā"]
NAME = {"mettā": "lòng từ ái", "karuṇā": "lòng trắc ẩn", "muditā": "niềm vui đồng cảm", "upekkhā": "sự bình thản"}
# termbase Mettā / Karuṇā / Muditā / Upekkhā; metti «lòng từ ái»
SAHA = {k: f"có {NAME[k]} đi kèm" for k in AP}          # Xsahagataṃ (termbase; pi-1 ^1-251 … «có lòng từ ái đi kèm»)
WITH = {k: f"với tâm {SAHA[k]}" for k in AP}            # Xsahagatena cetasā (termbase «tâm có lòng từ ái đi kèm»)
ARISING = {"mettā": "sự khởi lòng từ ái", "karuṇā": "sự khởi lòng trắc ẩn", "muditā": "sự khởi niềm vui đồng cảm",
           "upekkhā": "sự khởi bình thản"}                # Xyanā (termbase mettāyanā … upekkhāyanā)
STATE = {"mettā": "trạng thái khởi lòng từ ái", "karuṇā": "trạng thái khởi lòng trắc ẩn",
         "muditā": "trạng thái khởi niềm vui đồng cảm", "upekkhā": "trạng thái khởi bình thản"}   # Xyitattaṃ
LIBERATION = {k: f"sự giải thoát của tâm nhờ {NAME[k]}" for k in AP}     # Xcetovimutti (termbase)
misfit("upekkhāyitattaṃ (^2-673 … ^2-698): no entry; «trạng thái khởi bình thản» from the siblings upekkhāyanā «sự "
       "khởi bình thản» and mettāyitattaṃ «trạng thái khởi lòng từ ái»")
AP_LIST = {k: f"{NAME[k]}, {ARISING[k]}, {STATE[k]}, {LIBERATION[k]}" for k in AP}
AP_LIST_BEINGS = {k: f"{NAME[k]} đối với chúng sinh, {ARISING[k]}, {STATE[k]}, {LIBERATION[k]}" for k in AP}
assert f"{WHICH} {AP_LIST_BEINGS['mettā']}" == pi2(K23.METTA)          # ch. 3 (abyāpādadhātu)
assert f"{WHICH} {AP_LIST_BEINGS['karuṇā']}" == pi2(K23.KARUNA)        # ch. 3 (avihiṃsādhātu)
AP_LIST_P = {k: f"{'metti' if k == 'mettā' else k} {k}yanā {k}yitattaṃ {k}cetovimutti" for k in AP}

FOUR_AP = "Bốn trạng thái không thể đo lường"          # Catasso appamaññāyo (termbase appamaññāyo)
FOUR_AP_LIST = f"{FOUR_AP} – " + ", ".join(NAME[k] for k in AP) + "."
UP, DOWN, ACROSS = "phía trên", "phía dưới", "theo chiều ngang"
# uddhaṃ / adho: no entry (siblings uddhaṅgamā «đi lên», adhogamā «đi xuống»); tiriyaṃ «chiều ngang» (termbase)
misfit("uddhaṃ, adho, uddhamadho (^2-642, ^2-644, ^2-647, ^2-699): no entry; «phía trên», «phía dưới» from the "
       "siblings uddhaṅgamā «đi lên», adhogamā «đi xuống»; tiriyaṃ «chiều ngang» written «theo chiều ngang»")
ONE_DIR = "một phương"                                   # ekaṃ disaṃ (termbase ekaṃ disaṃ pharitvā)
LIKE = "cũng vậy"                                        # tathā (termbase)
ORD_DIR = {"dutiyaṃ": "phương thứ hai", "tatiyaṃ": "phương thứ ba", "catutthaṃ": "phương thứ tư"}
#  (termbase tathā catutthaṃ «cũng vậy phương thứ tư», catutthaṃ disaṃ «phương thứ tư»)
WHOLE = "khắp mọi nơi, đối với tất cả như đối với chính mình"      # sabbadhi sabbattatāya (termbase)
WORLD = "toàn thể thế gian"                              # sabbāvantaṃ lokaṃ (termbase)
VAST = "rộng rãi, rộng lớn, không thể đo lường, không thù địch, không thù hằn"
# vipulena mahaggatena appamāṇena averena abyāpajjena (termbase)
V_CATUTTHI = S.spell("Sī.", "catutthiṃ")
V_ABYAPAJJHENA = S.spell("Sī., Syā.", "abyāpajjhena")
V_ABYAPAJJHO = S.spell("Sī., Syā.", "abyāpajjho")


def ap_one(k, var=""):
    """Xsahagatena cetasā ekaṃ disaṃ pharitvā viharati, tathā dutiyaṃ, tathā tatiyaṃ, tathā catutthaṃ"""
    return (f"an trú sau khi lan tỏa khắp {ONE_DIR} {WITH[k]}, "
            + ", ".join(f"{LIKE} {ORD_DIR[o]}" for o in ORD_DIR) + (f" {var}" if var else ""))


def ap_all(k, var=""):
    """(iti) uddhamadho tiriyaṃ sabbadhi sabbattatāya sabbāvantaṃ lokaṃ Xsahagatena cetasā vipulena … abyāpajjena
    pharitvā viharati"""
    return (f"{UP}, {DOWN}, {ACROSS}, {WHOLE}, vị ấy an trú sau khi lan tỏa khắp {WORLD} {WITH[k]}, {VAST}"
            + (f" {var}" if var else ""))


def ap_642():
    out = [f"{FOUR_AP} – ở đây, vị tỳ-khưu {ap_one('mettā', V_CATUTTHI)}.",
           f"Như vậy, {ap_all('mettā', V_ABYAPAJJHENA)}."]
    for k in AP[1:]:
        out += [f"Vị ấy {ap_one(k)}.", f"Như vậy, {ap_all(k)}."]
    return " ".join(out)


def ap_699():
    parts = [f"ở đây, vị tỳ-khưu {ap_one('mettā')}, như vậy, {ap_all('mettā')}"]
    parts += [f"vị ấy {ap_one(k)}, như vậy, {ap_all(k)}" for k in AP[1:]]
    return f"{FOUR_AP} – " + "; ".join(parts) + "."


def ap_642_p():
    """the Pāli of ^2-642 rebuilt (asserted against the source)"""
    one = "{k}sahagatena cetasā ekaṃ disaṃ pharitvā viharati, tathā dutiyaṃ, tathā tatiyaṃ, tathā catutthaṃ"
    allp = ("Iti uddhamadho tiriyaṃ sabbadhi sabbattatāya sabbāvantaṃ lokaṃ {k}sahagatena cetasā vipulena mahaggatena "
            "appamāṇena averena abyāpajjena")
    out = [f"Catasso appamaññāyo – idha bhikkhu {one.format(k='mettā')} [catutthiṃ (sī.)].",
           f"{allp.format(k='mettā')} [abyāpajjhena (sī. syā.)] pharitvā viharati."]
    for k in AP[1:]:
        out += [f"{cap(one.format(k=k))}.", f"{allp.format(k=k)} pharitvā viharati."]
    return " ".join(out)


SIMILE_P = {
    "mettā": "Seyyathāpi nāma ekaṃ puggalaṃ piyaṃ manāpaṃ disvā mettāyeyya",
    "karuṇā": "Seyyathāpi nāma ekaṃ puggalaṃ duggataṃ durūpetaṃ disvā karuṇāyeyya",
    "muditā": "Seyyathāpi nāma ekaṃ puggalaṃ piyaṃ manāpaṃ disvā mudito assa",
    "upekkhā": "Seyyathāpi nāma ekaṃ puggalaṃ neva manāpaṃ na amanāpaṃ disvā upekkhako assa",
}
SIMILE = {   # piyaṃ «đáng yêu quý», manāpaṃ «đáng ưa thích», duggataṃ «khốn khổ», durūpetaṃ «bất hạnh»,
    #          mettāyeyya «khởi lòng từ ái», karuṇāyeyya «khởi lòng trắc ẩn», mudito «vui mừng», upekkhako «bình thản»
    "mettā": "Giống như khi thấy một người đáng yêu quý, đáng ưa thích, người ta sẽ khởi lòng từ ái đối với người ấy",
    "karuṇā": "Giống như khi thấy một người khốn khổ, bất hạnh, người ta sẽ khởi lòng trắc ẩn đối với người ấy",
    "muditā": "Giống như khi thấy một người đáng yêu quý, đáng ưa thích, người ta sẽ vui mừng",
    "upekkhā": ("Giống như khi thấy một người không phải đáng ưa thích cũng không phải không đáng ưa thích, người ta "
                "sẽ bình thản"),
}
EVAMEVA = "cũng như thế, vị ấy lan tỏa khắp tất cả chúng sinh bằng {x}"   # evameva sabbe satte Xya pharati
misfit("evameva, seyyathāpi nāma, kathañca (^2-643, ^2-653, ^2-663, ^2-673): no entries; «cũng như thế», «Giống như "
       "khi …», «… như thế nào?»")
DIRS = ("hoặc phương đông, hoặc phương tây, hoặc phương bắc, hoặc phương nam, "
        f"hoặc {UP}, hoặc {DOWN}, hoặc {ACROSS}, hoặc phương trung gian")
# puratthimaṃ / pacchimaṃ / uttaraṃ / dakkhiṇaṃ vā disaṃ «hoặc phương đông / tây / bắc / nam», vidisaṃ «phương trung gian»
LIKEWISE = (f"cũng như {ONE_DIR}, " + ", ".join(f"{LIKE} {ORD_DIR[o]}" for o in ORD_DIR)
            + f", {LIKE} {UP}, {LIKE} {DOWN}, {LIKE} {ACROSS}, {LIKE} phương trung gian")
# yatheva ekaṃ disaṃ tathā dutiyaṃ disaṃ … tathā vidisaṃ (yatheva: no entry, «cũng như»)
ALL_WAYS = "một cách toàn bộ, tất cả về mọi mặt, không thiếu sót, không sót lại gì"
# sabbena sabbaṃ «một cách toàn bộ», sabbathā sabbaṃ «tất cả về mọi mặt», asesaṃ, nissesaṃ (termbase)
WHOLE_WORLD = f"{WHOLE}, {WORLD}"                        # "sabbadhi sabbattatāya sabbāvantaṃ loka"nti
PARIYADAYA = f"Đây là cách nói bao hàm tất cả – “{WHOLE_WORLD}”."   # Pariyādāyavacanametaṃ – "…"nti.
VIPULA = ("điều gì rộng rãi thì điều đó rộng lớn, điều gì rộng lớn thì điều đó không thể đo lường, điều gì không thể "
          "đo lường thì điều đó không thù địch, điều gì không thù địch thì điều đó không thù hằn")
# yaṃ vipulaṃ taṃ mahaggataṃ, … yo avero so abyāpajjo (termbase vipulaṃ, mahaggataṃ, appamāṇaṃ, avero, abyāpajjo)
SUBHEAD13 = {cap(k): cap(NAME[k]) for k in AP}           # ##### Mettā … Upekkhā


def topic(kind, vi):
    return (TOPIC_W if kind == "w" else TOPIC_C).format(x=vi)


VIHARATI_TOPIC = f"{topic('w', 'an trú')} {low(VIHARATI_J)}"   # "Viharatī"ti iriyati … viharati. (ch. 12 jhāna)
VIHARATI_FULL = f"{VIHARATI_TOPIC} {TENA} “an trú”."
VIHARATI_PE = f"{topic('w', 'an trú')[:-1]}… {low(TENA)} “an trú”."   # "Viharatī"ti…pe… tena vuccati "viharatī"ti.
pi2(VIHARATI_FULL)
pi2(VIHARATI_PE)

SENT13 = {
    ('"Ekaṃ disa"nti puratthimaṃ vā disaṃ pacchimaṃ vā disaṃ uttaraṃ vā disaṃ dakkhiṇaṃ vā disaṃ uddhaṃ vā adho vā '
     'tiriyaṃ vā vidisaṃ vā.'): f"{topic('c', ONE_DIR)} {DIRS}.",
    '"Pharitvā"ti pharitvā adhimuccitvā.': f"{topic('w', 'sau khi lan tỏa khắp')} sau khi lan tỏa khắp, sau khi quyết "
                                           "định.",      # termbase pharitvā adhimuccitvā
    '"Viharatī"ti iriyati vattati pāleti yapeti yāpeti carati viharati.': VIHARATI_TOPIC,
    'Tena vuccati "viharatī"ti.': f"{TENA} “an trú”.",
    '"Viharatī"ti…pe… tena vuccati "viharatī"ti.': VIHARATI_PE,
    ('"Tathā dutiya"nti yatheva ekaṃ disaṃ tathā dutiyaṃ disaṃ tathā tatiyaṃ disaṃ tathā catutthaṃ disaṃ tathā uddhaṃ '
     'tathā adho tathā tiriyaṃ tathā vidisaṃ.'): f"{topic('c', LIKE + ' ' + ORD_DIR['dutiyaṃ'])} {LIKEWISE}.",
    '"Sabbadhi sabbattatāya sabbāvantaṃ loka"nti sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ.':
        f"{topic('c', WHOLE_WORLD)} {ALL_WAYS}.",
    'Pariyādāyavacanametaṃ – "sabbadhi sabbattatāya sabbāvantaṃ loka"nti.': PARIYADAYA,
    ('"Vipulenā"ti yaṃ vipulaṃ taṃ mahaggataṃ, yaṃ mahaggataṃ taṃ appamāṇaṃ, yaṃ appamāṇaṃ so avero, yo avero so '
     'abyāpajjo.'): f"{topic('w', 'rộng rãi')} {VIPULA}.",
    ('"Vipulenā"ti yaṃ vipulaṃ taṃ mahaggataṃ, yaṃ mahaggataṃ taṃ appamāṇaṃ, yaṃ appamāṇaṃ so avero, yo avero so '
     'abyāpajjo [abyāpajjho (sī. syā.)].'): f"{topic('w', 'rộng rãi')} {VIPULA} {V_ABYAPAJJHO}.",
    "Tattha katamaṃ cittaṃ?": q("tâm"),
    ('Yaṃ cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho '
     'tajjāmanoviññāṇadhātu – idaṃ vuccati "cittaṃ".'): f"{CITTA_FULL} – {CALLED} “tâm”.",
    'Yaṃ cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu – idaṃ vuccati "cittaṃ".': f"{CITTA_PE} – {CALLED} “tâm”.",
    "Suttantabhājanīyaṃ.": K1.FIXED["Suttantabhājanīyaṃ."],
    "Abhidhammabhājanīyaṃ.": K1.FIXED["Abhidhammabhājanīyaṃ."],
    "Ime dhammā kusalā.": f"{cap(ARE['kusalā'])}.",
    "Tattha katamā karuṇā…pe… tattha katamā muditā…pe… tattha katamā upekkhā?":
        f"{S.TATTHA} {NAME['karuṇā']} là gì… ở đây, {NAME['muditā']} là gì… ở đây, {NAME['upekkhā']} là gì?",
}
for _k in AP:
    SENT13[f"Kathañca bhikkhu {_k}sahagatena cetasā ekaṃ disaṃ pharitvā viharati?"] = \
        f"Vị tỳ-khưu an trú sau khi lan tỏa khắp {ONE_DIR} {WITH[_k]} như thế nào?"
    SENT13[f"{SIMILE_P[_k]}, evameva sabbe satte {_k}ya pharati."] = \
        f"{SIMILE[_k]}, {EVAMEVA.format(x=NAME[_k])}."
    SENT13[f"Tattha katamā {_k}?"] = q(NAME[_k])
    SENT13[f'Yā sattesu {AP_LIST_P[_k]} – ayaṃ vuccati "{_k}".'] = \
        f"{WHICH} {AP_LIST_BEINGS[_k]} – {CALLED} “{NAME[_k]}”."
    SENT13[f"Idaṃ cittaṃ imāya {_k}ya sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ."] = \
        f"Tâm này có {NAME[_k]} này đi kèm, cùng sinh với nó, hòa lẫn với nó, gắn liền với nó."
    # sahagataṃ «đi kèm», sahajātaṃ «cùng sinh», saṃsaṭṭhaṃ «hòa lẫn», sampayuttaṃ «gắn liền» (termbase)
    SENT13[f'Tena vuccati "{_k}sahagatena cetasā"ti.'] = f"{TENA} “{WITH[_k]}”."
    for _sep in (" ", ", "):
        SENT13[f'"{cap(_k)}sahagatena cetasā"ti{_sep}tattha katamā {_k}?'] = \
            f"{topic('c', WITH[_k])} {low(q(NAME[_k]))}"
    SENT13[f"Avasesā dhammā {_k}ya sampayuttā."] = f"{REST} {NAME[_k]}."

# ---- ch. 13 Abhidhamma: Idha bhikkhu yasmiṃ samaye <opener> <jhāna> Xsahagataṃ, <tail>
OPENERS13 = dict(K10.OPENERS)          # Pāli after «Idha bhikkhu yasmiṃ samaye» -> Vietnamese after MONK_WHEN
LEADS13 = dict(K10.LEAD)               # vivicceva kāmehi / vitakkavicārānaṃ vūpasamā / pītiyā ca virāgā / sukhassa …
LEADS13["sukhassa ca pahānā dukkhassa ca pahānā"] = pi1(K10.TOPICS["sukhassa ca pahānā dukkhassa ca pahānā"][1])


def clause13(c):
    """«<lead>…pe… [N jhānaṃ…pe… ]* N jhānaṃ upasampajja viharati» -> Vietnamese (pi-1 ^1-251 … ^1-261 shape)"""
    if c in K10.CLAUSE:
        return K10.CLAUSE[c]
    assert c.endswith(" jhānaṃ upasampajja viharati"), c
    parts = c[:-len(" upasampajja viharati")].split("…pe… ")
    out = [LEADS13[parts[0]]]
    for n, j in enumerate(parts[1:]):
        o, jh = j.split(" ")
        assert jh == "jhānaṃ", c
        last = n == len(parts) - 2
        out.append(f"{ENTER + ' ' if last else ''}tầng thiền {ORDN[o]}")
    return "… ".join(out)


TASSEVA13 = {"Tasseva rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ": K6.OF_RUPA}
J_RX = re.compile(r"^(.*?upasampajja viharati) (\S+)sahagataṃ, (.*)$")


def ap_tail(t, k, sid):
    """the part after «Xsahagataṃ, » -> Vietnamese (from «thì …»)"""
    t = t.replace("muditāyatanā", "muditāyanā") if "muditāyatanā" in t else t
    if t == "tasmiṃ samaye phasso hoti…pe… avikkhepo hoti":
        return f"{THEN} {CONTACT_PE}"
    m = re.match(r'^yā tasmiṃ samaye (.*) – ayaṃ vuccati "(\S+)"$', t)
    assert m and m.group(1) == AP_LIST_P[k] and m.group(2) == k, (sid, t)
    return f"{WHAT_AT_TIME} {AP_LIST[k]} – {CALLED} “{NAME[k]}”"


def ap_sentence(s, sid):
    """one sentence of a ch. 13 Abhidhamma line"""
    if s in SENT13:
        return SENT13[s]
    if "muditāyatanā" in s:
        slip(f"^{sid} «muditāyatanā» (for muditāyanā, as in every parallel): spelling slip, rendered as meant «sự "
             "khởi niềm vui đồng cảm»")
    m = re.match(r"^Idha bhikkhu yasmiṃ samaye (.*)\.$", s)
    if m:
        body = m.group(1)
        op = next(k for k in sorted(OPENERS13, key=len, reverse=True) if body.startswith(k + " "))
        jm = J_RX.match(body[len(op) + 1:])
        assert jm, (sid, body)
        c, k, t = jm.groups()
        if c.startswith("pītiyā ca virāgā…pe… dutiyaṃ jhānaṃ"):
            slip(f"^{sid} «pītiyā ca virāgā…pe… dutiyaṃ jhānaṃ» (the parallels ^2-684, ^2-688 have «vitakkavicārānaṃ "
                 "vūpasamā…pe… dutiyaṃ jhānaṃ»): translated as written «nhờ sự hân hoan phai nhạt… chứng nhập và an "
                 "trú tầng thiền thứ hai»")
        return f"{MONK_WHEN} {OPENERS13[op]}, {clause13(c)}, {SAHA[k]}, {ap_tail(t, k, sid)}."
    m = re.match(r"^(Tasseva .*? vipākaṃ) (.*)\.$", s)
    if m:
        ts, body = m.groups()
        jm = J_RX.match(body)
        assert jm, (sid, body)
        c, k, t = jm.groups()
        return f"{K6.ALSO_WHEN} {clause13(c)}, {SAHA[k]}, {TASSEVA13[ts]}, {ap_tail(t, k, sid)}."
    raise KeyError((sid, s))


def ap_line(ln, sid):
    if ln.startswith("Catasso appamaññāyo – idha bhikkhu"):
        assert ln == ap_642_p(), ln
        return ap_642()
    if ln == "Catasso appamaññāyo – mettā, karuṇā, muditā, upekkhā.":
        return FOUR_AP_LIST
    if ln in SENT13:
        return SENT13[ln]
    if " …pe…" in ln:
        slip(f"^{sid}: a space before «…pe…» (ignored)")
        ln = ln.replace(" …pe…", "…pe…")
    if ln in SENT13:
        return SENT13[ln]
    out = []
    lower_next = False
    for s in K79.SPLIT_RX.split(ln):
        v = ap_sentence(s, sid)
        out.append(low(v) if lower_next else v)
        lower_next = False
    return " ".join(out)


# =========================================================================== chapter 14: the training rules
PRECEPT = {   # X-ā (ablative) -> Vietnamese (termbase X veramaṇī «sự kiềm chế X»; ch. 4 ^2-205 wording)
    "pāṇātipātā": "việc sát hại sinh mạng",
    "adinnādānā": "việc lấy của không được cho",
    "kāmesumicchācārā": "hành vi sai trái trong các dục lạc",
    "musāvādā": "việc nói dối",
    "surāmerayamajjapamādaṭṭhānā": "việc dùng rượu nấu rượu men và chất gây say dẫn đến sự buông thả",
}
for _k in ("pāṇātipātā", "adinnādānā", "kāmesumicchācārā"):
    assert f"{K45.ABST} {PRECEPT[_k]}" in pi2(K45.L205_5).lower(), _k        # ch. 4 ^2-205 (sammākammanto)
assert f"{K45.ABST} {PRECEPT['musāvādā']}" in pi2(K45.L205_4).lower()      # ch. 4 ^2-205 (sammāvācā)
PRECEPT_ORDER = list(PRECEPT)
RULE = "điều tu học về sự kiềm chế {x}"                   # X veramaṇī sikkhāpadaṃ (termbase veramaṇī sikkhāpadaṃ)
FIVE_RULES = "Năm điều tu học"                            # Pañca sikkhāpadāni (termbase sikkhāpadāni)
FIVE_RULES_LIST = f"{FIVE_RULES} – " + ", ".join(RULE.format(x=PRECEPT[k]) for k in PRECEPT_ORDER) + "."
ABSTAINER = "nơi một người đang kiêng tránh {x}"          # X viramantassa (virati «sự kiêng tránh»; no entry)
misfit("viramantassa (^2-704 … ^2-711, «X viramantassa»): no entry; «nơi một người đang kiêng tránh X» from the "
       "sibling virati «sự kiêng tránh»")
ABSTAIN = K45.ABSTAIN                                     # ārati virati … setughāto (ch. 4 / ch. 11)
pi2(ABSTAIN.format(x="sinh kế sai lầm", v=""))            # as in ch. 4 / ch. 11 (micchā ājīvā ārati …)
CETANA3 = pi1(K6.CETANA3)                                 # cetanā sañcetanā sañcetayitattaṃ «chủ ý, sự cố ý, …»
PHASSA_PAGGAHA = "sự tiếp xúc… sự dốc sức, sự không tán loạn"   # phasso…pe… paggāho avikkhepo (ch. 9)
assert PHASSA_PAGGAHA in cap(pi2(K79.SENT["Tathābhūtassa phasso…pe… paggāho avikkhepo."])).lower()
HINA = {"hīnaṃ": "thấp kém", "majjhimaṃ": "trung bình", "paṇītaṃ": "ưu việt",
        "chandādhipateyyaṃ": "lấy ý muốn làm yếu tố chủ đạo", "vīriyādhipateyyaṃ": "lấy tinh tấn làm yếu tố chủ đạo",
        "cittādhipateyyaṃ": "lấy tâm làm yếu tố chủ đạo",
        "vīmaṃsādhipateyyaṃ": "lấy sự thẩm xét làm yếu tố chủ đạo"}      # pi-1 ^1-269
SIKKHA_Q = "Những hiện tượng nào là sự tu học?"           # Katame dhammā sikkhā? (termbase dhammā sikkhā)
SIKKHA_END = "Những hiện tượng này là sự tu học."          # Ime dhammā sikkhā.
SAMP14 = {"veramaṇiyā": "sự kiềm chế", "cetanāya": "chủ ý"}   # Avasesā dhammā X sampayuttā
WHEN = "Vào lúc"                                          # Yasmiṃ samaye (pi-1)


def hina_chain(t):
    """hīnaṃ… majjhimaṃ… paṇītaṃ… chandādhipateyyaṃ hīnaṃ… … (pi-1 ^1-269 shape)"""
    return "… ".join(", ".join(HINA[w] for w in tok.strip().split(" ")) for tok in t.split("…"))


def quals14(body, sid):
    """«kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti …[ hīnaṃ… …]» -> «tâm thiện thuộc cõi dục lạc sinh khởi, …»"""
    if "kāmāvacare kusalaṃ" in body:
        slip(f"^{sid} «kāmāvacare kusalaṃ cittaṃ» (locative for kāmāvacaraṃ): spelling slip, rendered as meant «tâm "
             "thiện thuộc cõi dục lạc»")
        body = body.replace("kāmāvacare kusalaṃ", "kāmāvacaraṃ kusalaṃ")
    for a in ("majjhimaṃ …", "vīriyādhipateyyaṃ …"):
        if a in body:
            slip(f"^{sid} «{a}»: a space before «…» (ignored)")
            body = body.replace(a, a.replace(" …", "…"))
    i = body.find(" hīnaṃ…")
    if i < 0:
        return K6.quals(body)
    head, chain = body[:i], body[i + 1:]
    if "majjhimaṃ paṇītaṃ" in chain:
        slip(f"^{sid} «cittādhipateyyaṃ hīnaṃ… majjhimaṃ paṇītaṃ»: «…» missing between majjhimaṃ and paṇītaṃ "
             "(translated as written «trung bình, ưu việt»)")
    return f"{K6.quals(head)}, {hina_chain(chain)}"


def called_rule(raw):
    m = re.match(r'^"(\S+) veramaṇī sikkhāpadaṃ"$', raw)
    return f"{CALLED} “{RULE.format(x=PRECEPT[m.group(1)])}”"


def tail14(t, x, sid):
    """the part after «… viramantassa[,] » -> Vietnamese"""
    if " …pe…" in t:
        slip(f"^{sid}: a space before «…pe…» (ignored)")
        t = t.replace(" …pe…", "…pe…")
    out = []
    for s in K79.SPLIT_RX.split(t):
        m = re.match(r'^yā tasmiṃ samaye (\S+) ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti '
                     r'velāanatikkamo setughāto – idaṃ vuccati (".+")\.$', s)
        if m:
            assert m.group(1) == x, s
            out.append(f"{WHAT_AT_TIME} {ABSTAIN.format(x=PRECEPT[x], v='')} – {called_rule(m.group(2))}.")
            continue
        m = re.match(r'^yā tasmiṃ samaye cetanā sañcetanā sañcetayitattaṃ – idaṃ vuccati (".+")\.$', s)
        if m:
            out.append(f"{WHAT_AT_TIME} {CETANA3} – {called_rule(m.group(1))}.")
            continue
        m = re.match(r'^yo tasmiṃ samaye phasso…pe… paggāho avikkhepo – idaṃ vuccati (".+")\.$', s)
        if m:
            out.append(f"{WHAT_AT_TIME} {PHASSA_PAGGAHA} – {called_rule(m.group(1))}.")
            continue
        m = re.match(r'^phasso…pe… paggāho avikkhepo – idaṃ vuccati (".+")\.$', s)
        if m:
            slip(f"^{sid} «… viramantassa phasso…pe… paggāho avikkhepo – idaṃ vuccati …»: «yo tasmiṃ samaye» and "
                 "the comma missing (as against ^2-704 and ^2-707); translated as written «…, sự tiếp xúc… – đó được "
                 "gọi là …» (comma rendered as meant)")
            out.append(f"{PHASSA_PAGGAHA} – {called_rule(m.group(1))}.")
            continue
        m = re.match(r'^Avasesā dhammā (\S+) sampayuttā(?:…pe… avasesā dhammā (\S+) sampayuttā…pe… phasso…pe… '
                     r'paggāho avikkhepo – idaṃ vuccati (".+"))?\.$', s)
        if m:
            r = f"{REST} {SAMP14[m.group(1)]}"
            if m.group(2):
                r += (f"… {low(REST)} {SAMP14[m.group(2)]}… {PHASSA_PAGGAHA} – {called_rule(m.group(3))}")
            out.append(r + ".")
            continue
        raise KeyError((sid, s))
    return " ".join(out)


def line14(ln, sid):
    if ln.startswith("Pañca sikkhāpadāni – "):
        assert ln == ("Pañca sikkhāpadāni – " + ", ".join(f"{k} veramaṇī sikkhāpadaṃ" for k in PRECEPT_ORDER) + "."), ln
        return FIVE_RULES_LIST
    m = re.match(r"^Tattha katamaṃ (.+?)([?,]) [Yy]asmiṃ samaye (.+?) (\S+) viramantassa(,?) (.*)$", ln)
    if m:
        names, mark, body, x, comma, tail = m.groups()
        keys = re.findall(r"(\S+) veramaṇī sikkhāpadaṃ", names)
        assert names == "…pe… ".join(f"{k} veramaṇī sikkhāpadaṃ" for k in keys), names
        qs = f"{S.TATTHA} " + "… ".join(RULE.format(x=PRECEPT[k]) for k in keys) + " là gì"
        when = f"{WHEN} {quals14(body, sid)}, {ABSTAINER.format(x=PRECEPT[x])}, {tail14(tail, x, sid)}"
        if mark == ",":
            slip(f"^{sid} «Tattha katamaṃ surāmerayamajjapamādaṭṭhānā veramaṇī sikkhāpadaṃ, yasmiṃ samaye …»: comma "
                 "for the question mark; kept as written («… là gì, vào lúc …»)")
            return f"{qs}, {low(when)}"
        return f"{qs}? {when}"
    m = re.match(r"^Katame dhammā sikkhā\? Yasmiṃ samaye (.*), tasmiṃ samaye phasso hoti…pe… avikkhepo hoti\. "
                 r"Ime dhammā sikkhā\.$", ln)
    if m:
        body = m.group(1)
        p_paths = "rūpūpapattiyā maggaṃ bhāveti…pe… arūpūpapattiyā maggaṃ bhāveti…pe… "
        if body.startswith(p_paths):
            assert body == f"{p_paths}{K6.P_SUPRA} {K6.P_J1} dukkhapaṭipadaṃ dandhābhiññaṃ", body
            n = len("Vào lúc một người ")
            vi = f"{K6.RUPA_PATH}… {K6.ARUPA_PATH[n:]}… {K6.SUPRA[n:]}, {K6.J1}, {K6.MODE}"
        else:
            vi = f"{WHEN} {quals14(body, sid)}"
        return f"{SIKKHA_Q} {vi}, {THEN} {CONTACT_PE}. {SIKKHA_END}"
    raise KeyError((sid, ln))


# =========================================================================== chapter 15: the analytical knowledges
PS = {"attha": "hiểu biết thông suốt về ý nghĩa", "dhamma": "hiểu biết thông suốt về các hiện tượng",
      "nirutti": "hiểu biết thông suốt về cách diễn đạt", "paṭibhāna": "hiểu biết thông suốt về tài ứng đáp"}
# termbase atthapaṭisambhidā / dhammapaṭisambhidā / niruttipaṭisambhidā / paṭibhānapaṭisambhidā
PS_ORDER = ["attha", "dhamma", "nirutti", "paṭibhāna"]
KINDS = "loại hiểu biết thông suốt"                      # paṭisambhidā (termbase Paṭisambhidā, paṭisambhidānaṃ)
FOUR_PS, THREE_PS, TWO_PS = f"Bốn {KINDS}", f"Ba {KINDS}", f"hai {KINDS}"
FOUR_PS_LIST = f"{FOUR_PS} – " + ", ".join(PS[k] for k in PS_ORDER) + "."
THREE_PS_LIST = f"{THREE_PS} – " + ", ".join(PS[k] for k in ("attha", "nirutti", "paṭibhāna")) + "."
V_PATIBHANA = S.spell("Syā.", "paṭibhāṇapaṭisambhidā")[:-1] + ", cũng vậy ở các chỗ sau]"   # (syā.) evamuparipi
assert V_PATIBHANA.endswith(K10.GANANA_V.split(", ", 1)[1])


def is_ps(k):
    return f"là {PS[k]}"


KNOW = {   # the locative before «ñāṇaṃ» (lower case) -> «hiểu biết về X» (termbase; ch. 4 / ch. 6 wording)
    "atthe": "ý nghĩa", "dhamme": "các hiện tượng",                     # brief: dhamme ñāṇaṃ «về các hiện tượng»
    "dukkhe": "khổ đau", "dukkhasamudaye": "sự phát sinh của khổ đau", "dukkhanirodhe": "sự chấm dứt khổ đau",
    "dukkhanirodhagāminiyā paṭipadāya": "cách thực hành dẫn đến sự chấm dứt khổ đau",
    "hetumhi": "nguyên nhân", "hetuphale": "quả của nguyên nhân",
    "jarāmaraṇe": "sự lão hóa và sự chết", "jarāmaraṇasamudaye": "sự phát sinh của sự lão hóa và sự chết",
    "jarāmaraṇanirodhe": "sự chấm dứt sự lão hóa và sự chết",
    "jarāmaraṇanirodhagāminiyā paṭipadāya": "cách thực hành dẫn đến sự chấm dứt sự lão hóa và sự chết",
    "jātiyā": "sự sinh", "bhave": "sự hiện hữu", "upādāne": "sự bám víu", "taṇhāya": "khao khát",
    "vedanāya": "cảm giác", "phasse": "sự tiếp xúc", "saḷāyatane": "sáu lĩnh vực nhận biết",
    "nāmarūpe": "phần tinh thần và vật chất", "viññāṇe": "thức", "saṅkhāresu": "các sự tạo tác",
    "saṅkhārasamudaye": "sự phát sinh của các sự tạo tác", "saṅkhāranirodhe": "sự chấm dứt các sự tạo tác",
    "saṅkhāranirodhagāminiyā paṭipadāya": "cách thực hành dẫn đến sự chấm dứt các sự tạo tác",
}
assert pi2(K6.NOT_KNOW4) == cap(", ".join(f"sự không biết về {KNOW[k]}" for k in (
    "dukkhe", "dukkhasamudaye", "dukkhanirodhe", "dukkhanirodhagāminiyā paṭipadāya")))
NIRUTTI_CL = f"hiểu biết về lời diễn tả cách diễn đạt các hiện tượng ở đó {is_ps('nirutti')}"
# tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā (ābhilāpe «lời diễn tả», nirutti «cách diễn đạt», dhamma)
misfit("dhammaniruttābhilāpe (^2-718 … ^2-745, «tatra dhammaniruttābhilāpe ñāṇaṃ»): no entry for the whole compound; "
       "built from ābhilāpe «lời diễn tả», nirutti «cách diễn đạt», dhamma «hiện tượng», tatra «ở đó»: «hiểu biết về "
       "lời diễn tả cách diễn đạt các hiện tượng ở đó»")
NANESU = "hiểu biết về các sự hiểu biết"                 # ñāṇesu ñāṇaṃ (termbase ñāṇesu «sự hiểu biết», ñāṇaṃ)
NANESU_CL = f"{NANESU} {is_ps('paṭibhāna')}"
YAYA = "khái niệm về những hiện tượng ấy có được nhờ cách diễn đạt nào"
# yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti (termbase niruttiyā «cách diễn đạt», dhammānaṃ paññatti «khái niệm về
# những hiện tượng»)
YENA = ("Hiểu biết mà nhờ đó một người biết các sự hiểu biết ấy – “Những sự hiểu biết này làm sáng tỏ ý nghĩa này”, "
        f"tức {NANESU}, {is_ps('paṭibhāna')}.")
# Yena ñāṇena tāni ñāṇāni jānāti – "imāni ñāṇāni idamatthajotakānī"ti, ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā.
# (termbase ñāṇāni idamatthajotakānī «sự hiểu biết này làm sáng tỏ ý nghĩa này»; jānāti «biết»)
BORN = pi2("đã sinh ra, đã trở thành, đã sinh thành, đã phát sinh, đã phát sinh rõ rệt, đã hiện ra")
# jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā (sample ^2-3 PRES_S; user: the pi-1 jātā string)
assert S.PRES_S.startswith(BORN)
VARA = {"saṅgahavāro": "mục tổng hợp", "saccavāro": "mục về các sự thật", "hetuvāro": "mục về nguyên nhân",
        "dhammavāro": "mục về các hiện tượng",
        "paṭiccasamuppādavāro": "mục về sự sinh khởi tùy thuộc vào điều kiện",
        "pariyattivāro": "mục về việc học hỏi Giáo Pháp",
        "kusalavāro": "mục về điều thiện", "akusalavāro": "mục về điều bất thiện",
        "vipākavāro": "mục về quả của nghiệp", "kiriyavāro": "mục về điều mang tính chức năng"}
# termbase Saṅgahavāro, Saccavāro, Dhammavāro, Pariyattivāro; vāro «mục»; Hetu (Hetuvāra) «nguyên nhân»;
# samuppādavāro «mục về sự sinh khởi» + paṭicca (ch. 6 title); Kusala / Akusala / Vipāka / Kiriya as ch. 6 / ch. 12
misfit("Paṭiccasamuppādavāro, Kusalavāro, Akusalavāro, Vipākavāro, Kiriyavāro (^2-15-1-5-0, ^2-15-2-1-0 … "
       "^2-15-2-4-0): no headword entries; «Mục về sự sinh khởi tùy thuộc vào điều kiện» (samuppādavāro «mục về sự "
       "sinh khởi» + the ch. 6 title), «Mục về điều thiện / điều bất thiện / quả của nghiệp / điều mang tính chức "
       "năng» (vāro «mục», ch. 6 niddesa headings)")
SUBHEAD15 = {cap(k): cap(v) for k, v in VARA.items()}
SCRIPTURE = ("kinh, văn xuôi xen kệ, lời giải thích, kệ, lời cảm hứng, lời đã được nói như vậy, chuyện tiền thân, "
             "chuyện kỳ diệu chưa từng có, lời vấn đáp")
# suttaṃ geyyaṃ veyyākaraṇaṃ gāthaṃ udānaṃ itivuttakaṃ jātakaṃ abbhutadhammaṃ vedallaṃ (termbase)
FACT = {"phasso": "sự tiếp xúc", "vedanā": "cảm giác", "saññā": "tri giác", "cetanā": "chủ ý", "cittaṃ": "tâm",
        "upekkhā": "sự bình thản", "dukkhaṃ": "sự khó chịu", "vitakko": "sự hướng tâm", "vicāro": "sự duy trì tâm",
        "pīti": "sự hân hoan", "cittassekaggatā": "sự nhất tâm", "manindriyaṃ": "năng lực ý",
        "upekkhindriyaṃ": "năng lực bình thản", "sukhindriyaṃ": "năng lực dễ chịu",
        "dukkhindriyaṃ": "năng lực khó chịu", "somanassindriyaṃ": "năng lực niềm vui",
        "jīvitindriyaṃ": "năng lực sống", "vīriyindriyaṃ": "năng lực tinh tấn",
        "samādhindriyaṃ": "năng lực định tâm"}          # pi-1 ^1-431 / ^1-443 / ^1-455 / ^1-469 / ^1-556 / ^1-568
OTHER_ARUPA = pi1("hoặc vào lúc ấy còn có bất cứ hiện tượng phi vật chất nào khác sinh khởi tùy thuộc vào điều kiện")
OTHER_P = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"
OF_LOK_KAMMA = K6.OF_LOK.replace("tầng thiền thiện", "nghiệp thiện")   # … lokuttarassa kusalassa kammassa … (^2-740)
assert OF_LOK_KAMMA != K6.OF_LOK
TASSEVA15 = dict(K6.TASSEVA)
TASSEVA15[f"Tasseva lokuttarassa kusalassa kammassa katattā bhāvitattā vipākaṃ {K6.P_J1} dukkhapaṭipadaṃ "
          "dandhābhiññaṃ suññataṃ"] = f"{K6.ALSO_WHEN} {K6.J1}, {K6.MODE}, {K6.EMPTY}, {OF_LOK_KAMMA}"
P_745 = ("manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā somanassasahagatā "
         "ñāṇasampayuttā…pe… somanassasahagatā ñāṇasampayuttā sasaṅkhārena…pe… somanassasahagatā ñāṇavippayuttā…pe… "
         "somanassasahagatā ñāṇavippayuttā sasaṅkhārena…pe… upekkhāsahagatā ñāṇasampayuttā…pe… upekkhāsahagatā "
         "ñāṇasampayuttā sasaṅkhārena…pe… upekkhāsahagatā ñāṇavippayuttā…pe… upekkhāsahagatā ñāṇavippayuttā "
         "sasaṅkhārena")
P_745_REST = ("…pe… rūpāvacaraṃ jhānaṃ bhāveti…pe… arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca "
              f"kammavipākaṃ diṭṭhadhammasukhavihāraṃ…pe… {K6.P_J4}")
_N = len("Vào lúc một người ")
VI_745_REST = (f"… một người tu tập tầng thiền thuộc cõi hình sắc… {K6.KIRIYA_A[_N:]}… {K6.J4}")
SENT15 = {
    "Imesu dhammesu ñāṇaṃ dhammapaṭisambhidā.": f"Hiểu biết về những hiện tượng này {is_ps('dhamma')}.",
    "Imesu dhammesu ñāṇaṃ atthapaṭisambhidā.": f"Hiểu biết về những hiện tượng này {is_ps('attha')}.",
    "Tesaṃ vipāke ñāṇaṃ atthapaṭisambhidā.": f"Hiểu biết về quả của chúng {is_ps('attha')}.",
    ("Tesaṃ vipāke ñāṇaṃ atthapaṭisambhidā, yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti, tatra dhammaniruttābhilāpe "
     "ñāṇaṃ niruttipaṭisambhidā."): f"Hiểu biết về quả của chúng {is_ps('attha')}; {YAYA}, thì {NIRUTTI_CL}.",
    "Yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā.":
        f"{cap(YAYA)}, thì {NIRUTTI_CL}.",
    ('Yena ñāṇena tāni ñāṇāni jānāti – "imāni ñāṇāni idamatthajotakānī"ti, ñāṇesu ñāṇaṃ '
     "paṭibhānapaṭisambhidā."): YENA,
    "Ime dhammā kusalā.": f"{cap(ARE['kusalā'])}.", "Ime dhammā akusalā.": f"{cap(ARE['akusalā'])}.",
    "Ime dhammā abyākatā.": f"{cap(ARE['abyākatā'])}.",
    "Tisso paṭisambhidā – atthapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā.": THREE_PS_LIST,
    "Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā.":
        FOUR_PS_LIST,
    ("Tisso paṭisambhidā kāmāvacarakusalato catūsu ñāṇasampayuttesu cittuppādesu, kiriyato catūsu "
     "ñāṇasampayuttesu cittuppādesu uppajjanti."):
        (f"{THREE_PS} sinh khởi trong bốn loại tâm thiện thuộc cõi dục lạc gắn liền với hiểu biết, và trong bốn loại "
         "tâm mang tính chức năng gắn liền với hiểu biết."),
    # kāmāvacarakusalato (kāmāvacara «thuộc cõi dục lạc», kusala «thiện»), kiriyato «mang tính chức năng»,
    # ñāṇasampayuttesu «gắn liền với hiểu biết», cittuppādesu «loại tâm», uppajjanti «sinh khởi» (termbase)
    "Atthapaṭisambhidā etesu ceva uppajjati, catūsu maggesu catūsu phalesu ca uppajjati.":
        (f"{cap(PS['attha'])} sinh khởi trong chính những loại tâm này, và cũng sinh khởi trong bốn con đường và "
         "bốn thành quả."),                                 # maggesu «con đường», phalesu «thành quả» (termbase)
    "Tattha katamā dhammapaṭisambhidā?": q(PS["dhamma"]),
    ("Idha bhikkhu dhammaṃ jānāti – suttaṃ geyyaṃ veyyākaraṇaṃ gāthaṃ udānaṃ itivuttakaṃ jātakaṃ abbhutadhammaṃ "
     "vedallaṃ."): f"Ở đây, vị tỳ-khưu biết Giáo Pháp – {SCRIPTURE}.",   # brief / termbase: ^2-724 dhammaṃ «Giáo Pháp»
    'Ayaṃ vuccati "dhammapaṭisambhidā".': f"{cap(CALLED)} “{PS['dhamma']}”.",
    'Ayaṃ vuccati "atthapaṭisambhidā".': f"{cap(CALLED)} “{PS['attha']}”.",
    ('So tassa tasseva bhāsitassa atthaṃ jānāti – "ayaṃ imassa bhāsitassa attho, ayaṃ imassa bhāsitassa '
     'attho"ti.'): ("Vị ấy biết ý nghĩa của từng lời đã được nói ấy – “Đây là ý nghĩa của lời đã được nói này, đây là ý "
                    "nghĩa của lời đã được nói này”."),     # bhāsitassa «lời đã được nói», atthaṃ / attho «ý nghĩa»
    "Tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā.": f"{cap(NIRUTTI_CL)}.",
    "Ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā.": f"{cap(NANESU_CL)}.",
    "Suttantabhājanīyaṃ.": K1.FIXED["Suttantabhājanīyaṃ."],
    "Abhidhammabhājanīyaṃ.": K1.FIXED["Abhidhammabhājanīyaṃ."],
}
for _k, _v in VARA.items():
    SENT15[f"Ayaṃ {_k}."] = f"Đây là {_v}."


def ps_item(it, sid):
    """one «X ñāṇaṃ Ypaṭisambhidā» item of the Suttanta lists (lower case) -> Vietnamese (lower case)"""
    it = it.strip()
    if it == "tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā":
        return NIRUTTI_CL
    if it == "ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā":
        return NANESU_CL
    m = re.match(r"^(.+?) ñāṇaṃ(?: (\S+)paṭisambhidā)?$", it)
    assert m, (sid, it)
    x, k = m.groups()
    v = f"hiểu biết về {KNOW[low(x)]}"
    return f"{v} {is_ps(k)}" if k else v


def ps_list(t, sid):
    """«Dukkhe ñāṇaṃ atthapaṭisambhidā, … ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā» (separators «, » / «…pe… »)"""
    toks = re.split(r"(, |…pe… )", t)
    out = ""
    for i, x in enumerate(toks):
        if i % 2:
            out += ", " if x == ", " else "… "
        else:
            out += ps_item(x, sid)
    return cap(out)


def suttanta15(ln, sid):
    """the Suttantabhājanīya lines of ch. 15"""
    if ln in SENT15:
        return SENT15[ln]
    if ln.startswith("Tattha katamā dhammapaṭisambhidā?"):                      # ^2-724 (pariyattivāra)
        return " ".join(SENT15[s] for s in K79.SPLIT_RX.split(ln))
    four = ("Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, "
            "paṭibhānapaṭisambhidā")
    if sid == "2-718":
        ln = ln.replace(f"{four} [paṭibhāṇapaṭisambhidā (syā.) evamuparipi]. ", "", 1)
        head = f"{FOUR_PS_LIST[:-1]} {V_PATIBHANA}."
    elif sid == "2-720":
        bad = four.replace("dhammapaṭisambhidā, niruttipaṭisambhidā", "dhammapaṭisambhidā niruttipaṭisambhidā")
        assert ln.startswith(bad + ". "), ln
        slip("^2-720 «atthapaṭisambhidā, dhammapaṭisambhidā niruttipaṭisambhidā»: comma missing in the list (missing "
             "punctuation, rendered as meant)")
        ln, head = ln[len(bad) + 2:], FOUR_PS_LIST
    else:
        assert ln.startswith(four + ". "), ln
        ln, head = ln[len(four) + 2:], FOUR_PS_LIST
    out = [head]
    for s in K79.SPLIT_RX.split(ln):
        if s in SENT15:
            out.append(SENT15[s])
            continue
        if sid == "2-721":
            jp = "jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā"
            assert s == (f"Ye dhammā {jp}, imesu dhammesu ñāṇaṃ atthapaṭisambhidā; yamhā dhammā te dhammā {jp}, tesu "
                         "dhammesu ñāṇaṃ dhammapaṭisambhidā; tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā; "
                         "ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā."), s
            out.append(f"Những hiện tượng nào {BORN}, thì hiểu biết về những hiện tượng này {is_ps('attha')}; các "
                       f"hiện tượng ấy {BORN} từ những hiện tượng nào, thì hiểu biết về những hiện tượng đó "
                       f"{is_ps('dhamma')}; {NIRUTTI_CL}; {NANESU_CL}.")
            # Ye «nào», yamhā (no entry) «từ … nào», imesu / tesu «này / đó»
            continue
        assert s.endswith("."), (sid, s)
        out.append(ps_list(s[:-1], sid) + ".")
    return " ".join(out)


def factor_tail(t):
    """«phasso hoti, vedanā hoti, …, jīvitindriyaṃ hoti, ye vā pana …» -> «có sự tiếp xúc, …; hoặc vào lúc ấy …»"""
    assert t.endswith(", " + OTHER_P), t
    items = t[:-len(", " + OTHER_P)].split(", ")
    happy = "sự dễ chịu" if "sukhindriyaṃ hoti" in items else "hạnh phúc"     # pi-1 ^1-443 vs ^1-469
    out = []
    for it in items:
        assert it.endswith(" hoti"), it
        w = it[:-len(" hoti")]
        out.append("có " + (happy if w == "sukhaṃ" else FACT[w]))
    return pi1(", ".join(out) + f"; {OTHER_ARUPA}")


def tasmim15(t):
    """«tasmiṃ samaye …» (no final full stop) -> Vietnamese after «thì vào lúc ấy»"""
    if t == "phasso hoti…pe… avikkhepo hoti":
        return CONTACT_PE
    if t == "phasso hoti…pe… avikkhepo hoti, ime dhammā kusalā":
        return f"{CONTACT_PE}, {ARE['kusalā']}"
    return factor_tail(t)


def abhi15_sentence(s, sid):
    if s in SENT15:
        return SENT15[s]
    m = re.match(r"^Katame dhammā (kusalā|akusalā|abyākatā)\?$", s)
    if m:
        return KIND_Q[m.group(1)]
    m = re.match(r"^Yasmiṃ samaye (.*?), tasmiṃ samaye (.*)\.$", s)
    if m:
        body, t = m.groups()
        if body == P_745 + P_745_REST:
            vi = f"{WHEN} {K6.quals(P_745)}{VI_745_REST}"
        elif body in K6.JHANA:
            vi = K6.JHANA[body]
        else:
            vi = f"{WHEN} {K6.quals(body)}"
        return f"{vi}, {THEN} {tasmim15(t)}."
    m = re.match(r"^(Tasseva .*?), tasmiṃ samaye (.*)\.$", s)
    if m:
        ts, t = m.groups()
        if "lokuttarassa kusalassa kammassa katattā bhāvitattā" in ts:
            slip(f"^{sid} «Tasseva lokuttarassa kusalassa kammassa katattā bhāvitattā vipākaṃ» (kammassa, where ch. 6 "
                 "and ch. 12 have jhānassa): translated as written «là quả của chính nghiệp thiện vượt thế gian ấy …»")
        return f"{TASSEVA15[ts]}, {THEN} {tasmim15(t)}."
    raise KeyError((sid, s))


def abhi15_line(ln, sid):
    if ln in SENT15:
        return SENT15[ln]
    return " ".join(abhi15_sentence(s, sid) for s in K79.SPLIT_RX.split(ln))


# =========================================================================== Pañhāpucchaka (K10 engine, in memory)
GROUPS13_15 = {"Catunnaṃ appamaññānaṃ": ("Trong bốn trạng thái không thể đo lường", "bao nhiêu trạng thái"),
               "Pañcannaṃ sikkhāpadānaṃ": ("Trong năm điều tu học", "bao nhiêu điều"),
               "Catunnaṃ paṭisambhidānaṃ": (f"Trong bốn {KINDS}", "bao nhiêu loại")}
KENACI13_15 = {13: "trạng thái không thể đo lường", 14: "điều tu học", 15: KINDS}
SUBJ13_15 = {  # Pāli subject (lower case) -> (Vietnamese, number, «thì» after it)
    # «thì» marks where the predicate begins: the names end in a noun or in «không …», and a bare predicate would
    # read as part of the name («ba loại hiểu biết thông suốt trung bình»)
    "tisso appamaññāyo": ("ba trạng thái không thể đo lường", "p", True),
    "mettā": (NAME["mettā"], "s", True), "upekkhā": (NAME["upekkhā"], "s", True),
    "tisso paṭisambhidā": (f"ba {KINDS}", "p", True), "dve paṭisambhidā": (TWO_PS, "p", True),
    "atthapaṭisambhidā": (PS["attha"], "s", True), "niruttipaṭisambhidā": (PS["nirutti"], "s", True),
}
PANHA_FIX13_15 = [  # (bad, good, slip note)
    ('"', "", None),                                   # «na vattabbā "X"ti» quoted (the words are the same)
    (" …pe…", "…pe…", None),
    ("Na hetū sahetukā, hetusampayuttā. Na vattabbā", "Na hetū, sahetukā, hetusampayuttā. Na vattabbā",
     "^2-717 «Na hetū sahetukā, hetusampayuttā.»: the first three dyad answers with a comma missing after «na hetū» "
     "(the sixth dyad «na hetu sahetūkā» follows later in the line; ch. 13 ^2-702 «na hetū, sahetukā, "
     "hetusampayuttā»); missing punctuation rendered as meant «Đều không phải là gốc rễ, có gốc rễ, …»"),
    ("na hetu sahetūkā", "na hetū sahetukā",
     "^2-717 «na hetu sahetūkā» (for na hetū sahetukā, plural subject): spelling slip, rendered as meant «không phải "
     "là gốc rễ nhưng có gốc rễ»"),
    ("āsavavippayuttā sāsavā", "āsavavippayuttasāsavā",
     "^2-702, ^2-750 «āsavavippayuttā sāsavā / anāsavā» written as two words (matrix: āsavavippayuttasāsavā; same "
     "Vietnamese, as ch. 12 ^2-641)"),
    ("āsavavippayuttā anāsavā", "āsavavippayuttaanāsavā", None),
    ("Āsavavippayuttā sāsavā", "Āsavavippayuttasāsavā", None),
    ("na bhāvanāyapahātabbā", "na bhāvanāya pahātabbā",
     "^2-717 «na bhāvanāyapahātabbā» written as one word (= na bhāvanāya pahātabbā)"),
    ("nahetūahetukātipi", "na hetū ahetukātipi",
     "^2-750 «nahetūahetukātipi» written as one word (= na hetū ahetukātipi)"),
    ("Anidassanaapaṭighā.", "Anidassanaappaṭighā.",
     "^2-749 «Anidassanaapaṭighā» (apaṭighā for appaṭighā; termbase lists both with the same Vietnamese): rendered as "
     "meant «không thấy được và không có tính va chạm»"),
    ("tisso appamaññāyo na upekkhāsahagatā, na kāmāvacarā", "tisso appamaññāyo na upekkhāsahagatā; na kāmāvacarā",
     "^2-702 «Upekkhā upekkhāsahagatā, tisso appamaññāyo na upekkhāsahagatā, na kāmāvacarā, rūpāvacarā …»: the "
     "predicates of all four run on after the subject «tisso appamaññāyo»; a «;» is set before them («; đều không "
     "thuộc cõi dục lạc …»), as ch. 12 ^2-641"),
    ("siyā lokuttarā, kenaci viññeyyā, kenaci na viññeyyā", "siyā lokuttarā; Kenaci viññeyyā, kenaci na viññeyyā",
     "^2-750 «… atthapaṭisambhidā siyā lokiyā, siyā lokuttarā, kenaci viññeyyā, kenaci na viññeyyā»: «kenaci …» is "
     "said of all four; a «;» is set before it («; đều là những loại hiểu biết thông suốt mà …»), as ch. 12 ^2-641"),
    ("arūpā, tisso paṭisambhidā lokiyā, atthapaṭisambhidā", "arūpā; tisso paṭisambhidā lokiyā, atthapaṭisambhidā",
     None),                                            # ^2-750: «; » before the first named subject (Vietnamese only)
    ("Niruttipaṭisambhidā na vattabbā – maggārammaṇātipi", "Niruttipaṭisambhidā na vattabbā maggārammaṇātipi",
     None),                                            # the dash is put back after the engine (DASHED_NV)
]
DASHED_NV = (f"Về {PS['nirutti']} thì không nên nói rằng", f"Về {PS['nirutti']} thì không nên nói – rằng")
P_ASAVA = " [āsavā (sī.) dhātuvibhaṅge pana pāṭhanānattaṃ natthi]"
V_ASAVA = S.reading("Sī.", "āsavā")[:-1] + "; nhưng trong “Phân tích các yếu tố” không có khác biệt về văn bản]"
# dhātuvibhaṅge «trong “Phân tích các yếu tố”» (ch. 3 title), pāṭhanānattaṃ natthi «không có khác biệt về văn bản»


def install():
    """extend the K10 question-section tables in memory (nothing is written)"""
    K10.GROUPS.update(GROUPS13_15)
    K10.KENACI_NOUN.update(KENACI13_15)
    K10.SUBJ.update(SUBJ13_15)
    K10.SUBJ_RX = re.compile(r"^(" + "|".join(sorted(K10.SUBJ, key=len, reverse=True)) + r") (.*)$", re.I)
    K10.PANHA_FIX = PANHA_FIX13_15
    K23.LOCAL["maggādhipatinī"] = K1.pred("maggādhipati")     # feminine singular (atthapaṭisambhidā), ^2-749
    neg = K79.LOCAL79["na maggādhipati"].replace("yếu tố chủ đạo", "gốc rễ")
    assert neg == "không " + K1.pred("maggahetuko"), neg
    K79.LOCAL79["na maggahetuko"] = neg                         # ^2-749 «dve paṭisambhidā … na maggahetukā»
    K79.PLK79["na maggahetukā"] = "na maggahetuko"


def panha_line(p, sid, ch):
    var = P_ASAVA in p
    if var:
        assert p.count(P_ASAVA) == 2, p
        p = p.replace(P_ASAVA, "")
    nv_dash = "na vattabbā – maggārammaṇātipi" in p
    v = K10.panha_line(p, sid, ch)
    v = v.replace("; Đều ", "; đều ")
    if nv_dash:
        assert v.count(DASHED_NV[0]) == 1, v
        v = v.replace(*DASHED_NV)
    if var:
        anchor = f"về {PS['attha']} thì không nên nói rằng “vừa là ô nhiễm"
        assert v.count(anchor) == 1, v
        i = v.index(anchor)
        a, b = "vừa là ô nhiễm vừa là đối tượng của ô nhiễm", "là đối tượng của ô nhiễm nhưng không phải là ô nhiễm"
        head, tail = v[:i], v[i:]
        assert a in tail and b in tail, tail
        tail = tail.replace(a, a.replace("vừa là ô nhiễm", f"vừa là ô nhiễm {V_ASAVA}", 1), 1)
        tail = tail.replace(b, f"{b} {V_ASAVA}", 1)
        v = head + tail
    return v


# =========================================================================== chapters
FIXED = {f"{n} niṭṭhito.": f"{S.CH_HEADINGS[n]} {K1.DONE}."
         for n in ("Appamaññāvibhaṅgo", "Sikkhāpadavibhaṅgo", "Paṭisambhidāvibhaṅgo")}
FIXED.update({"Suttantabhājanīyaṃ.": K1.FIXED["Suttantabhājanīyaṃ."],
              "Abhidhammabhājanīyaṃ.": K1.FIXED["Abhidhammabhājanīyaṃ."],
              "Pañhāpucchakaṃ.": K1.FIXED["Pañhāpucchakaṃ."],
              "Catasso appamaññāyo – mettā, karuṇā, muditā, upekkhā.": FOUR_AP_LIST,
              "Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, "
              "paṭibhānapaṭisambhidā.": FOUR_PS_LIST})


def heading(ln):
    lvl, text = ln.split(" ", 1)
    t = dict(S.CH_HEADINGS)
    t.update(S.SEC_HEADINGS)
    t.update({"Tikaṃ": K1.TIKA_H, "Dukaṃ": K1.DUKA_H})
    t.update(SUBHEAD13)
    t.update(SUBHEAD15)
    return f"{lvl} {t[text]}"


def line(ln, sid, ch, section):
    if ln in FIXED:
        return FIXED[ln]
    if section == "Pañhāpucchakaṃ":
        if ln.endswith("?"):
            return K10.panha_question(ln)
        if ln.startswith("Catasso appamaññāyo – idha bhikkhu"):
            return ap_699()
        if ln.startswith("Pañca sikkhāpadāni – "):
            return line14(ln, sid)
        return panha_line(ln, sid, ch)
    if ch == 13:
        return ap_line(ln, sid)
    if ch == 14:
        return line14(ln, sid)
    if section == "Suttantabhājanīyaṃ":
        return suttanta15(ln, sid)
    return abhi15_line(ln, sid)


def build(ch):
    pali = (S.PALI / PARTS[ch]).read_text(encoding="utf-8")
    h, section = {}, None
    for sid, lines in K1.segs(pali):
        lines = [K1.ID.sub("", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            text = lines[0].split(" ", 1)[1]
            if text in S.SEC_HEADINGS:
                section = text
            h[sid] = [heading(lines[0])]
            continue
        h[sid] = [line(ln, sid, ch, section) for ln in lines]
    for sid, lines in K1.segs(pali):
        for p, v in zip([K1.ID.sub("", ln) for ln in lines], h[sid]):
            K10.check_line(sid, p, v)
    return pali, h


def check_pi1():
    text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI1_VI.glob("*.md")))
    missing = [s for s in PI1_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    return len(PI1_USED)


def check_pi2():
    files = ["1-khandhavibhango.md", "2-ayatanavibhango.md", "3-dhatuvibhango.md", "4-saccavibhango.md",
             "5-indriyavibhango.md", "6-paticcasamuppadavibhango.md", "7-satipatthanavibhango.md",
             "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md", "10-bojjhangavibhango.md",
             "11-maggangavibhango.md", "12-jhanavibhango.md"]
    text = "\n".join((S.OUT / f).read_text(encoding="utf-8") for f in files)
    missing = [s for s in PI2_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    return len(PI2_USED)


# =========================================================================== notes
def notes_md():
    L = ["# pi-2 Vietnamese rails: new formulas of chapters 13-15 (^2-13-0 … ^2-750)", "",
         "Generated by build_rails_13_15_vi.py; import it instead of retyping. Strings already in vi-rails-formulas.md "
         "(sample) or notes-1 … notes-10-12 are not repeated (the mind-type openers, the jhāna openers and the Tasseva "
         "… vipākaṃ frames come from ch. 6 / ch. 12, the abstinence string from ch. 4 / ch. 11, the «Viharatī» gloss "
         "and the topic frames from ch. 7-12). Format: Pāli = tiếng Việt.", "",
         "## Headings and closing labels", ""]
    L += [f"### {n} = ### {S.CH_HEADINGS[n]}; closing «{n} niṭṭhito.» = «{S.CH_HEADINGS[n]} {K1.DONE}.»"
          for n in ("Appamaññāvibhaṅgo", "Sikkhāpadavibhaṅgo", "Paṭisambhidāvibhaṅgo")]
    L += [f"##### {p} = ##### {v}" for p, v in list(SUBHEAD13.items()) + list(SUBHEAD15.items())]
    L += [f"Ayaṃ {p}. = Đây là {v}." for p, v in VARA.items() if not p.endswith(("kusalavāro", "vipākavāro",
                                                                                 "kiriyavāro"))]
    L += ["", "## Measureless states (ch. 13)", "",
          f"Catasso appamaññāyo – mettā, karuṇā, muditā, upekkhā. = {FOUR_AP_LIST}",
          "X: " + "; ".join(f"{k} = {NAME[k]}" for k in AP),
          "Xsahagataṃ (jhāna field) = " + " / ".join(SAHA[k] for k in AP) + " (pi-1 ^1-251 …)",
          "Xsahagatena cetasā = " + " / ".join(WITH[k] for k in AP),
          f"Xsahagatena cetasā ekaṃ disaṃ pharitvā viharati, tathā dutiyaṃ, tathā tatiyaṃ, tathā catutthaṃ = "
          f"{ap_one('mettā').replace(NAME['mettā'], 'X')}",
          f"Iti uddhamadho tiriyaṃ sabbadhi sabbattatāya sabbāvantaṃ lokaṃ Xsahagatena cetasā vipulena mahaggatena "
          f"appamāṇena averena abyāpajjena pharitvā viharati. = Như vậy, {ap_all('mettā').replace(NAME['mettā'], 'X')}.",
          f"(^2-642) Catasso appamaññāyo – idha bhikkhu … = {ap_642()}",
          f"(^2-699, one sentence joined by «;») = {ap_699()}",
          "Kathañca bhikkhu Xsahagatena cetasā ekaṃ disaṃ pharitvā viharati? = Vị tỳ-khưu an trú sau khi lan tỏa khắp "
          "một phương với tâm có X đi kèm như thế nào?",
          ]
    L += [f"{SIMILE_P[k]}, evameva sabbe satte {k}ya pharati. = {SIMILE[k]}, {EVAMEVA.format(x=NAME[k])}." for k in AP]
    L += ["Yā sattesu X Xyanā Xyitattaṃ Xcetovimutti = " + " / ".join(f"{WHICH} {AP_LIST_BEINGS[k]}" for k in AP),
          "yā tasmiṃ samaye X Xyanā Xyitattaṃ Xcetovimutti = thì điều mà vào lúc ấy là " + " / ".join(
              AP_LIST[k] for k in AP),
          "Idaṃ cittaṃ imāya Xya sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ. = Tâm này có X này đi kèm, cùng sinh "
          "với nó, hòa lẫn với nó, gắn liền với nó.",
          "Tena vuccati \"Xsahagatena cetasā\"ti. = Vì thế, điều này được gọi là “với tâm có X đi kèm”.",
          "\"Xsahagatena cetasā\"ti tattha katamā X? = Về câu “với tâm có X đi kèm”: ở đây, X là gì?",
          f"Avasesā dhammā Xya sampayuttā. = {REST} X.",
          ]
    L += [f"{k} = {v}" for k, v in SENT13.items()
          if not re.match(r'^(Kathañca|Seyyathāpi|Tattha katamā (mettā|karuṇā|muditā|upekkhā)\?|Yā sattesu|Idaṃ cittaṃ|'
                          r'Tena vuccati "\S+sahagatena|"\S+sahagatena|Avasesā|Suttanta|Abhidhamma|Ime dhammā)', k)]
    L += ["jhāna clause «<lead>…pe… N jhānaṃ…pe… … M jhānaṃ upasampajja viharati» = <lead>… tầng thiền N… … chứng "
          "nhập và an trú tầng thiền M (pi-1 ^1-259); sukhassa ca pahānā dukkhassa ca pahānā = "
          f"{LEADS13['sukhassa ca pahānā dukkhassa ca pahānā']}",
          "", "## Training rules (ch. 14)", "",
          f"Pañca sikkhāpadāni – … = {FIVE_RULES_LIST}",
          f"X veramaṇī sikkhāpadaṃ = {RULE.format(x='X')}; X: " + "; ".join(f"{k} = {v}" for k, v in PRECEPT.items()),
          "Tattha katamaṃ X veramaṇī sikkhāpadaṃ? = Ở đây, điều tu học về sự kiềm chế X là gì?",
          f"Yasmiṃ samaye … X viramantassa, = {WHEN} …, {ABSTAINER.format(x='X')},",
          f"yā tasmiṃ samaye X ārati virati … setughāto – idaṃ vuccati \"…\". = {WHAT_AT_TIME} "
          f"{ABSTAIN.format(x='X', v='')} – {CALLED} “…”.",
          f"yā tasmiṃ samaye cetanā sañcetanā sañcetayitattaṃ = {WHAT_AT_TIME} {CETANA3}",
          f"yo tasmiṃ samaye phasso…pe… paggāho avikkhepo = {WHAT_AT_TIME} {PHASSA_PAGGAHA}",
          f"Avasesā dhammā veramaṇiyā / cetanāya sampayuttā. = {REST} {SAMP14['veramaṇiyā']} / {SAMP14['cetanāya']}.",
          "hīnaṃ… majjhimaṃ… paṇītaṃ… chandādhipateyyaṃ… … = " + "; ".join(f"{k} = {v}" for k, v in HINA.items())
          + " (pi-1 ^1-269)",
          f"Katame dhammā sikkhā? = {SIKKHA_Q}  Ime dhammā sikkhā. = {SIKKHA_END}",
          "", "## Analytical knowledges (ch. 15)", "",
          f"Catasso paṭisambhidā – … = {FOUR_PS_LIST}", f"Tisso paṭisambhidā – … = {THREE_PS_LIST}",
          "Xpaṭisambhidā = " + "; ".join(f"{k} = {v}" for k, v in PS.items()),
          f"[paṭibhāṇapaṭisambhidā (syā.) evamuparipi] = {V_PATIBHANA}",
          "<X> ñāṇaṃ <Y>paṭisambhidā = hiểu biết về x là y; X: " + "; ".join(f"{k} = {v}" for k, v in KNOW.items()),
          f"tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā = {NIRUTTI_CL}",
          f"ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā = {NANESU_CL}",
          f"Ye dhammā jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā, imesu dhammesu ñāṇaṃ atthapaṭisambhidā; yamhā "
          f"dhammā te dhammā jātā …, tesu dhammesu ñāṇaṃ dhammapaṭisambhidā = Những hiện tượng nào {BORN}, thì hiểu "
          f"biết về những hiện tượng này {is_ps('attha')}; các hiện tượng ấy {BORN} từ những hiện tượng nào, thì hiểu "
          f"biết về những hiện tượng đó {is_ps('dhamma')}",
          "Idha bhikkhu dhammaṃ jānāti – suttaṃ … vedallaṃ. = " + SENT15[
              "Idha bhikkhu dhammaṃ jānāti – suttaṃ geyyaṃ veyyākaraṇaṃ gāthaṃ udānaṃ itivuttakaṃ jātakaṃ "
              "abbhutadhammaṃ vedallaṃ."],
          ]
    L += [f"{k} = {v}" for k, v in SENT15.items()
          if not k.startswith(("Ayaṃ ", "Suttanta", "Abhidhamma", "Ime dhammā", "Idha bhikkhu dhammaṃ"))]
    L += ["tasmiṃ samaye phasso hoti, vedanā hoti, … , ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino "
          f"dhammā = thì vào lúc ấy có sự tiếp xúc, có cảm giác, …; {OTHER_ARUPA} (pi-1 ^1-431; factors: "
          + "; ".join(f"{k} = {v}" for k, v in FACT.items()) + "; sukhaṃ = sự dễ chịu beside sukhindriyaṃ, otherwise "
          "hạnh phúc)",
          f"Tasseva lokuttarassa kusalassa kammassa katattā bhāvitattā vipākaṃ … = {K6.ALSO_WHEN} …, {OF_LOK_KAMMA}",
          f"{P_ASAVA.strip()} = {V_ASAVA}",
          "", "## Question sections", "",
          "Catunnaṃ appamaññānaṃ / Pañcannaṃ sikkhāpadānaṃ / Catunnaṃ paṭisambhidānaṃ kati …? = " + " / ".join(
              f"{a}, {b} …?" for a, b in GROUPS13_15.values()),
          "subjects: " + "; ".join(f"{k} = {v[0]}{' (+ thì)' if v[2] else ''}" for k, v in SUBJ13_15.items()),
          "Kenaci viññeyyā, kenaci na viññeyyā (mid-sentence) = " + "; ".join(
              f"ch. {c}: {K1.KENACI.replace('những khối', f'những {n}')}" for c, n in KENACI13_15.items()),
          f"Niruttipaṭisambhidā na vattabbā – Xtipi, … (dash in the Pāli) = {DASHED_NV[1]} “x”, …",
          ]
    return unicodedata.normalize("NFC", "\n".join(L) + "\n")


def main():
    dry = "--dry" in sys.argv
    install()
    for ch, part in PARTS.items():
        pali, h = build(ch)
        text = K10.render(pali, h)
        if not dry:
            (S.OUT / part).write_bytes(text.encode("utf-8"))
        print(f"{'built' if dry else 'wrote'} {part}: {len(h)} segments")
    n1, n2 = check_pi1(), check_pi2()
    if not dry:
        NOTES_PATH.write_bytes(notes_md().encode("utf-8"))
    print(f"pi-1 strings checked: {n1}; pi-2 strings checked: {n2}")
    for s in SLIPS + [x for x in K10.SLIPS if x not in K10_SLIPS0]:
        print("slip:", s)
    for s in MISFITS:
        print("misfit:", s)


if __name__ == "__main__":
    main()
