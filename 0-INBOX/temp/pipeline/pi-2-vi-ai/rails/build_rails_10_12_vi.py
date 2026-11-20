"""Builder for the Vietnamese rails translation of pi-2 (Vibhaṅga, «Phân tích các hiện tượng», plain audience),
chapters 10 (Bojjhaṅgavibhaṅgo ^2-10-0 … ^2-485), 11 (Maggaṅgavibhaṅgo ^2-11-0 … ^2-507) and 12 (Jhānavibhaṅgo
^2-12-0 … ^2-641).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/10-bojjhangavibhango.md
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/11-maggangavibhango.md
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/12-jhanavibhango.md
  0-INBOX/temp/pipeline/pi-2-vi-ai/rails/notes-10-12.md   (new recurring formulas, Pāli = tiếng Việt)

Translated fresh from the Pāli with the locked pi-2 termbase (X-sambojjhaṅgo «chi phần giác ngộ là X»; vossagga «sự
buông xả»; viharati «sống» for conduct, «an trú» in the jhānas; sukha «hạnh phúc» as a jhāna factor; Catukkaṃ /
Pañcakaṃ «Phương pháp chia bốn / năm»). Shared strings are imported read-only from the approved sample builder (S)
and the chapter 1, 2-3, 4-5, 6 and 7-9 builders (K1, K23, K45, K6, K79). Passages that repeat the Dhammasaṅgaṇī reuse
the approved pi-1 Vietnamese rails (marked pi1() and asserted to occur there by check_pi1()); strings taken from the
earlier pi-2 chapters are marked pi2() and checked by check_pi2(). Every Vietnamese line is checked against its Pāli
line for the dash count and for left-over Pāli letters. Importing this module writes nothing.

usage: python -I -X utf8 build_rails_10_12_vi.py
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
import build_rails_4_5_vi as K45   # noqa: E402  (importing writes nothing; extends K23 tables in memory)
import build_rails_6_vi as K6      # noqa: E402  (importing writes nothing)
import build_rails_7_9_vi as K79   # noqa: E402  (importing writes nothing)

PARTS = {10: "10-bojjhangavibhango.md", 11: "11-maggangavibhango.md", 12: "12-jhanavibhango.md"}
PI1_VI = S.ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
NOTES_PATH = RAILS / "notes-10-12.md"
cap, low, q = S.cap, K1.low, K23.q
CALLED, CALLED_PL = S.CALLED_SG, S.CALLED_PL          # «đó được gọi là» / «những điều này được gọi là»
WHICH = K23.WHICH                                     # Yo / Yā / Yaṃ … (definition) «Điều mà là»
TENA = K6.TENA                                        # Tena vuccati "…"ti «Vì thế, điều này được gọi là “…”»
SLIPS = []          # source slips met while building (reported)
MISFITS = []        # termbase gaps / misfits / sense choices (reported)
PI1_USED = []       # strings taken from the approved pi-1 Vietnamese rails (checked by check_pi1)
PI2_USED = []       # strings taken from the approved earlier pi-2 chapters (checked by check_pi2)


def note(lst, s):
    if s not in lst:
        lst.append(s)


def slip(s):
    note(SLIPS, s)


def misfit(s):
    note(MISFITS, s)


def pi1(s):
    """mark a string as taken unchanged from the approved pi-1 Vietnamese rails (checked by check_pi1)"""
    if s not in PI1_USED:
        PI1_USED.append(s)
    return s


def pi2(s):
    """mark a string as taken unchanged from the approved earlier pi-2 Vietnamese chapters (checked by check_pi2)"""
    if s not in PI2_USED:
        PI2_USED.append(s)
    return s


def p1_list(bid, start, end):
    """the part of an approved pi-1 Vietnamese line between two markers (start included, end excluded)"""
    t = K23.p1(bid)
    i = t.index(start)
    j = t.index(end, i)
    return pi1(t[i:j])


# =========================================================================== shared strings (imported)
PF = K45.PF                                     # the eight path factors (pi-1 ^1-277 names)
PATH8 = K45.PATH8
PATH5 = K45.PATH5
PATH_TAIL = K45.PATH_TAIL                       # maggaṅgaṃ maggapariyāpannaṃ «chi phần của con đường, nằm trong …»
MONK_WHEN = K79.MONK_WHEN                       # «Ở đây, vào lúc một vị tỳ-khưu»
SUPRA = pi2(K45.SUPRA)                          # lokuttaraṃ jhānaṃ … dandhābhiññaṃ, tasmiṃ samaye (… «thì vào lúc ấy»)
SUPRA_CORE = K79.SUPRA_CORE                     # the same without «, thì vào lúc ấy»
THEN = K6.THEN                                  # «thì vào lúc ấy»
WHAT_AT_TIME = K79.WHAT_AT_TIME                 # «thì điều mà vào lúc ấy là»
CONTACT_PE = K6.CONTACT_PE                      # «có sự tiếp xúc… có sự không tán loạn» (pi-1)
ARE_KUSALA = K6.ARE_KUSALA                      # «những hiện tượng này là thiện» (pi-1)
TASSEVA_LOK = {False: K6.TASSEVA["Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ "
                                 f"{K6.P_J1} dukkhapaṭipadaṃ dandhābhiññaṃ"],
               True: K6.TASSEVA["Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ "
                                f"{K6.P_J1} dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ"]}
TOPIC_W, TOPIC_C = K79.TOPIC_W, K79.TOPIC_C     # «Về từ “x”:» / «Về câu “x”:»
UPETO, UPETO_PE = K79.UPETO, K79.UPETO_PE       # the possession string «có được, có được trọn vẹn, …»
VIHARATI = pi2(K79.VIHARATI)                    # Iriyati … viharati. «Vị ấy vận động, …, sống.»
SATI_PE = K79.SATI_PE                           # sati anussati…pe… sammāsati
SATI_PATH = K79.SATI_PATH                       # sati anussati sammāsati satisambojjhaṅgo maggaṅgaṃ …
SATI_FULL = K45.SATI                            # sati anussati paṭissati … sammāsati (pi-1 ^1-1358)
PANNA_SHORT = K45.PANNA_SHORT                   # paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi (pi-1)
PANNA_PATH = K6.PANNA_PATH                      # … sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ
VIRIYA_PE = K79.VIRIYA_PE                       # cetasiko vīriyārambho…pe… sammāvāyāmo
VIRIYA_PATH = K79.VIRIYA_PATH                   # … sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ
SAMADHI_FULL = K45.SAMADHI                      # cittassa ṭhiti … sammāsamādhi (pi-1 ^1-11)
SAMADHI_PE = K79.SAMADHI_PE                     # cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi
CITTA_PE = K79.CITTA_PE                         # cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu
RAGA_PE = K79.RAGA_PE                           # rāgo sārāgo…pe… cittassa sārāgo
FEEL = K23.FEELING_P1                           # the pi-1 feeling definitions (sukha / dukkha / somanassa / …)
ARDENT = K79.ARDENT                             # ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ
FIVE_UPA = K45.FIVE_UPA                         # pañcupādānakkhandhā «năm khối làm đối tượng cho sự bám víu»
SAMADHI_ST = "sự ổn định của tâm"               # cittassa ṭhiti…pe… (ch. 4 «sự ổn định của tâm… định tâm đúng đắn»)
assert K45.FACTOR_BODY["cittassa ṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo"].startswith(SAMADHI_ST + "…")

# the four jhānas of the Suttanta (ch. 4 ^2-205, pi-1 wording)
JH1, JH2, JH3, JH4 = K45.JH1, K45.JH2, K45.JH3, K45.JH4
JH3_NODASH = JH3.replace(" – “", ": “")          # «… mô tả người ấy: “…”» where the Pāli has no dash (^2-487)
assert JH3_NODASH != JH3
# the four formless attainments (pi-1 ^1-265 … wording, «vị ấy» added as in JH2)
OVERCOME_R = pi1("nhờ hoàn toàn vượt qua các tri giác về hình sắc, nhờ các tri giác về sự va chạm biến mất, nhờ "
                 "không chú tâm đến các tri giác về sự đa dạng")
AY_INF = {"ākāsa": "lĩnh vực không gian vô tận", "viññāṇa": "lĩnh vực thức vô tận",
          "ākiñcañña": "lĩnh vực không có gì cả",
          "nevasaññā": "lĩnh vực không phải tri giác cũng không phải không tri giác"}   # termbase (pi-1)
ENTER = "chứng nhập và an trú"                  # upasampajja viharati (termbase; pi-1)
THOUGHT = {"ākāsa": "Không gian là vô tận", "viññāṇa": "Thức là vô tận", "ākiñcañña": "Không có gì cả"}
# "ananto ākāso"ti / "anantaṃ viññāṇa"nti / "natthi kiñcī"ti (ananto «vô tận», natthi kiñcī «không có gì cả»)
AR1 = f"{OVERCOME_R}, với ý nghĩ “{THOUGHT['ākāsa']}”, vị ấy {ENTER} {AY_INF['ākāsa']}"
AR2 = (f"{pi1('hoàn toàn vượt qua lĩnh vực không gian vô tận')}, với ý nghĩ “{THOUGHT['viññāṇa']}”, vị ấy {ENTER} "
       f"{AY_INF['viññāṇa']}")
AR3 = (f"hoàn toàn vượt qua {AY_INF['viññāṇa']}, với ý nghĩ “{THOUGHT['ākiñcañña']}”, vị ấy {ENTER} "
       f"{AY_INF['ākiñcañña']}")
AR4 = f"{pi1('hoàn toàn vượt qua lĩnh vực không có gì cả')}, vị ấy {ENTER} {AY_INF['nevasaññā']}"

# =========================================================================== chapter 10: the awakening factors
BOJJH = dict(K79.BOJJH)    # sati «sự tỉnh thức», dhammavicaya «sự tìm hiểu các hiện tượng», … upekkhā «sự bình thản»
BJ_ORDER = list(BOJJH)


def bj(k):
    """Xsambojjhaṅgo «chi phần giác ngộ là X» (termbase)"""
    return f"chi phần giác ngộ là {BOJJH[k]}"


SEVEN_BJ = "bảy chi phần giác ngộ"               # satta bojjhaṅgā (Satta «bảy», bojjhaṅgā «chi phần giác ngộ»)
SIX_BJ = "sáu chi phần giác ngộ"                 # cha bojjhaṅgā
BJ7_FULL = f"{cap(SEVEN_BJ)} – " + ", ".join(bj(k) for k in BJ_ORDER) + "."
BJ7_PE = f"{cap(SEVEN_BJ)} – {bj('sati')}… {bj('upekkhā')}."
NISSITA = "dựa vào sự tách biệt, dựa vào sự phai nhạt, dựa vào sự chấm dứt, hướng đến sự buông xả"
# vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ (viveka «sự tách biệt», virāga «phai nhạt»,
# nirodha «sự chấm dứt», vossagga «sự buông xả», pariṇāmiṃ «hướng đến»; nissita: no entry, from nissāya «dựa vào»)
misfit("nissitaṃ (^2-471, ^2-489, «vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ»): no entry; "
       "«dựa vào» from the sibling nissāya «dựa vào»: «dựa vào sự tách biệt, dựa vào sự phai nhạt, dựa vào sự chấm "
       "dứt, hướng đến sự buông xả»")
NOUN = {  # Pāli as asked / named in quotes -> (Vietnamese, quote in questions)
    "satta bojjhaṅgā": (SEVEN_BJ, False),
    "aṭṭhaṅgiko maggo": ("con đường gồm tám chi phần", False),
    "pañcaṅgiko maggo": ("con đường gồm năm chi phần", False),
}
for _k in BJ_ORDER:
    NOUN[f"{_k}sambojjhaṅgo"] = (bj(_k), True)   # awakening-factor names in quotes as question topics (APPROVED)
for _k, _v in PF.items():
    NOUN[_k] = (_v, False)


def ask(name):
    """Tattha katamo X? -> «Ở đây, X là gì?» (awakening-factor names quoted)"""
    v, quoted = NOUN[name]
    return q(f"“{v}”" if quoted else v)


def called_n(name, quoted=True):
    v = NOUN[name][0]
    return f"– {CALLED} “{v}”." if quoted else f"– {CALLED} {v}."


# ^2-467: the Suttanta sequence (one sentence each)
L467 = [
    (f"Ở đây, vị tỳ-khưu có sự tỉnh thức, được trang bị sự tỉnh thức và sự khôn ngoan tột bậc, nhớ được, nhớ lại được "
     f"cả những việc đã làm từ lâu, cả những lời đã nói từ lâu"),
    "Khi sống tỉnh thức như vậy, vị ấy dùng trí tuệ tìm hiểu, xem xét, thẩm xét toàn diện hiện tượng ấy",
    ("Khi vị ấy dùng trí tuệ tìm hiểu, xem xét, thẩm xét toàn diện hiện tượng ấy, sự tinh tấn không chùng xuống được "
     "khởi động nơi vị ấy"),
    "Nơi người đã khởi động tinh tấn, sự hân hoan không có tính trần tục sinh khởi",
    "Nơi người có tâm hân hoan, cả thân cũng lắng dịu, cả tâm cũng lắng dịu",
    "Nơi người có thân đã an tịnh, có hạnh phúc, tâm được định tâm",
    "Vị ấy nhìn tâm đã được định tâm như vậy một cách kỹ lưỡng với sự bình thản trọn vẹn",
]
# satimā «có sự tỉnh thức», paramena «tột bậc», satinepakkena (sati + nepakkena «sự khôn ngoan»), samannāgato «được
# trang bị», saritā «nhớ được», anussaritā «nhớ lại được», cirakatampi «những việc đã làm từ lâu»; viharanto «khi
# sống», pavicinati «tìm hiểu», pavicarati «xem xét», parivīmaṃsamāpajjati «thẩm xét toàn diện», āraddhaṃ «được khởi
# động», asallīnaṃ «không chùng xuống», nirāmisā «không có tính trần tục», Pītimanassa «có tâm hân hoan», passambhati
# «lắng dịu», sukhino «có hạnh phúc», samāhitaṃ «được định tâm», ajjhupekkhitā «nhìn với sự bình thản trọn vẹn»
misfit("cirabhāsitampi (^2-467): no entry; «những lời đã nói từ lâu» beside cirakatampi «những việc đã làm từ lâu»")
misfit("tathā (^2-467 «So tathā sato viharanto», «So tathā samāhitaṃ cittaṃ»): the termbase sense 'likewise' «cũng "
       "vậy» does not fit 'thus'; written «như vậy»")
misfit("samādhiyati (^2-467 «cittaṃ samādhiyati»): no entry; «được định tâm» from samāhitaṃ «được định tâm»")
misfit("passaddhakāyassa (^2-467): no entry; «có thân đã an tịnh» (passaddhi «sự an tịnh»)")
misfit("sādhukaṃ (^2-467 «sādhukaṃ ajjhupekkhitā hoti»): no entry; «một cách kỹ lưỡng»")
L469_ITEMS = {  # Atthi X, atthi Y (ch. 10 ^2-469): Pāli -> Vietnamese
    "ajjhattaṃ dhammesu sati": "sự tỉnh thức đối với các hiện tượng ở nơi bản thân",
    "bahiddhā dhammesu sati": "sự tỉnh thức đối với các hiện tượng ở bên ngoài bản thân",
    "ajjhattaṃ dhammesu pavicayo": "sự tìm hiểu kỹ đối với các hiện tượng ở nơi bản thân",
    "bahiddhā dhammesu pavicayo": "sự tìm hiểu kỹ đối với các hiện tượng ở bên ngoài bản thân",
    "kāyikaṃ vīriyaṃ": "sự tinh tấn nơi thân", "cetasikaṃ vīriyaṃ": "sự tinh tấn trong tâm",
    "savitakkasavicārā pīti": "sự hân hoan có sự hướng tâm và sự duy trì tâm",
    "avitakkaavicārā pīti": "sự hân hoan không có sự hướng tâm cũng không có sự duy trì tâm",
    "kāyapassaddhi": pi1("sự an tịnh của thân tinh thần"), "cittapassaddhi": "sự an tịnh của tâm",
    "savitakko savicāro samādhi": "định tâm có sự hướng tâm và sự duy trì tâm",
    "avitakko avicāro samādhi": "định tâm không có sự hướng tâm cũng không có sự duy trì tâm",
    "ajjhattaṃ dhammesu upekkhā": "sự bình thản đối với các hiện tượng ở nơi bản thân",
    "bahiddhā dhammesu upekkhā": "sự bình thản đối với các hiện tượng ở bên ngoài bản thân",
}
LEADS = "dẫn đến sự hiểu biết trực tiếp, đến sự giác ngộ hoàn toàn, đến Niết-bàn"
# abhiññāya sambodhāya nibbānāya saṃvattati (abhiññāya «sự hiểu biết trực tiếp», sambodhāya «sự giác ngộ hoàn toàn»,
# saṃvattati «dẫn đến»; nibbānāya: Niết-bàn, core term)
PITI_LIST = pi1("sự hân hoan, sự phấn khởi, sự vui vẻ, sự vui thích, sự tươi cười, sự rạng rỡ, sự mãn nguyện, sự "
                "phấn chấn, sự hài lòng của tâm")                              # pi-1 ^1-9
ODAGGA_VAR = S.spell("Sī.", "odaggaṃ") [:-1] + "; xem “Liệt kê các hiện tượng” 9]"   # [odaggaṃ (sī.) dha. sa. 9]
PITI_LIST_V = PITI_LIST.replace("sự phấn chấn", f"sự phấn chấn {ODAGGA_VAR}")
PASSADDHI = ("sự an tịnh, sự an tịnh hoàn toàn, sự lắng dịu, sự lắng dịu hoàn toàn, trạng thái đã lắng dịu hoàn toàn "
             "của khối cảm giác, khối tri giác, khối tạo tác và khối thức")
# pi-1 ^1-40 kāyapassaddhi wording with the fourth aggregate added (passaddhi paṭippassaddhi passambhanā …)
UPEKKHA_LIST = "sự bình thản, sự giữ bình thản, sự bình thản trọn vẹn, sự cân bằng của tâm"
# upekkhā «sự bình thản», upekkhanā «sự giữ bình thản», ajjhupekkhanā «sự bình thản trọn vẹn», majjhattatā cittassa
# «sự cân bằng» of the mind (termbase)

# =========================================================================== chapter 11: the path factors
ABST = {k: K45.ABSTAIN.format(x=pi1(x), v="") for k, x in (
    ("vācā", "bốn hành vi xấu bằng lời nói"), ("kamma", "ba hành vi xấu bằng thân"), ("ājīva", "sinh kế sai lầm"))}
VITAKKA_FULL = f"{K23.VITAKKA6}, {PF['sammāsaṅkappo']}"          # takko … abhiniropanā sammāsaṅkappo (pi-1 ^1-7)
ARIYO8 = f"Con đường gồm tám chi phần cao quý, cụ thể là – {PATH8}."   # Ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – …
AT8 = f"Con đường gồm tám chi phần – {PATH8}."                      # Aṭṭhaṅgiko maggo – …
AT8_PE = f"Con đường gồm tám chi phần – {PF['sammādiṭṭhi']}… {PF['sammāsamādhi']}."
AT5 = f"Con đường gồm năm chi phần – {PATH5}."                      # Pañcaṅgiko maggo – …
L487_EFF = (f"{q(PF['sammāvāyāmo'])} Ở đây, {K79.efforts(K79.EFF_FULL, 'vị tỳ-khưu')} – {CALLED} "
            f"“{PF['sammāvāyāmo']}”.")
L487_SATI = (f"{q(PF['sammāsati'])} Ở đây, "
             + "; ".join(f"{K79.lives(loc, '', 'vị tỳ-khưu' if n == 0 else 'vị ấy')}, {ARDENT}"
                         for n, loc in enumerate(("kāye", "vedanāsu", "citte", "dhammesu")))
             + f" – {CALLED} “{PF['sammāsati']}”.")
L487_SAMADHI = (f"{q(PF['sammāsamādhi'])} Ở đây, vị tỳ-khưu {JH1}; {JH2}; {JH3_NODASH}; {JH4} – {CALLED} "
                f"“{PF['sammāsamādhi']}”.")
slip("^2-487 sammāsamādhi «yaṃ taṃ ariyā ācikkhanti \"upekkhako satimā sukhavihārī\"ti» without the dash of ch. 4 "
     "^2-205 and ch. 12 ^2-508: no dash, «:» before the quote")

# =========================================================================== answer bodies (after «Yo / Yā …»)
BODY = {
    "sati anussati…pe… sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        f"{K45.FACTOR_BODY['sati anussati…pe… sammāsati satisambojjhaṅgo']}, {PATH_TAIL}",
    "sati anussati sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": SATI_PATH,
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        PANNA_PATH,
    "cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": VIRIYA_PATH,
    "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ [odaggaṃ (sī.) dha. sa. 9] attamanatā cittassa "
    "pītisambojjhaṅgo": f"{PITI_LIST_V}, {bj('pīti')}",
    "vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa viññāṇakkhandhassa passaddhi paṭippassaddhi passambhanā "
    "paṭippassambhanā paṭippassambhitattaṃ passaddhisambojjhaṅgo": f"{PASSADDHI}, {bj('passaddhi')}",
    "cittassa ṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        f"{K45.FACTOR_BODY['cittassa ṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo']}, {PATH_TAIL}",
    "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ "
    "sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": f"{SAMADHI_FULL}, {bj('samādhi')}, {PATH_TAIL}",
    "upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa upekkhāsambojjhaṅgo": f"{UPEKKHA_LIST}, {bj('upekkhā')}",
    "upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa": UPEKKHA_LIST,
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ":
        f"{VITAKKA_FULL}, {PATH_TAIL}",
    "takko vitakko…pe… sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ":
        f"{K45.FACTOR_BODY['takko vitakko…pe… sammāsaṅkappo']}, {PATH_TAIL}",
    "catūhi vacīduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
    "sammāvācā maggaṅgaṃ maggapariyāpannaṃ": f"{ABST['vācā']}, {PF['sammāvācā']}, {PATH_TAIL}",
    "tīhi kāyaduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
    "sammākammanto maggaṅgaṃ maggapariyāpannaṃ": f"{ABST['kamma']}, {PF['sammākammanto']}, {PATH_TAIL}",
    "micchāājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto sammāājīvo "
    "maggaṅgaṃ maggapariyāpannaṃ": f"{ABST['ājīva']}, {PF['sammāājīvo']}, {PATH_TAIL}",
}

# =========================================================================== the sentence engine (ch. 10-11)
SPLIT_RX = K79.SPLIT_RX
SUPRA_P = K79.SUPRA_P
TASSEVA_P = {True: K79.TASSEVA_P, False: K79.TASSEVA_P[:-len(" suññataṃ")]}
Q_RX = re.compile(r"^Tattha katam(?:o|ā|aṃ|e) (.+?)\?$")
A_RX = re.compile(r'^(.*) – (ayaṃ|idaṃ) vuccati "(.+?)"(…pe…)?\.$')
SENT = {
    "Suttantabhājanīyaṃ.": K1.FIXED["Suttantabhājanīyaṃ."],
    "Abhidhammabhājanīyaṃ.": K1.FIXED["Abhidhammabhājanīyaṃ."],
    "Pañhāpucchakaṃ.": K1.FIXED["Pañhāpucchakaṃ."],
    "Ime dhammā kusalā.": f"{cap(ARE_KUSALA)}.",
    "Satta bojjhaṅgā – satisambojjhaṅgo, dhammavicayasambojjhaṅgo, vīriyasambojjhaṅgo, pītisambojjhaṅgo, "
    "passaddhisambojjhaṅgo, samādhisambojjhaṅgo, upekkhāsambojjhaṅgo.": BJ7_FULL,
    "Satta bojjhaṅgā – satisambojjhaṅgo…pe… upekkhāsambojjhaṅgo.": BJ7_PE,
    "Ime vuccanti satta bojjhaṅgā.": f"{cap(CALLED_PL)} {SEVEN_BJ}.",
    'Ime vuccanti "satta bojjhaṅgā".': f"{cap(CALLED_PL)} “{SEVEN_BJ}”.",
    'Ayaṃ vuccati "aṭṭhaṅgiko maggo".': f"{cap(CALLED)} “{NOUN['aṭṭhaṅgiko maggo'][0]}”.",
    'Ayaṃ vuccati "pañcaṅgiko maggo".': f"{cap(CALLED)} “{NOUN['pañcaṅgiko maggo'][0]}”.",
    ("Ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – sammādiṭṭhi, sammāsaṅkappo, sammāvācā, sammākammanto, sammāājīvo, "
     "sammāvāyāmo, sammāsati, sammāsamādhi."): ARIYO8,
    ("Aṭṭhaṅgiko maggo – sammādiṭṭhi, sammāsaṅkappo, sammāvācā, sammākammanto, sammāājīvo, sammāvāyāmo, sammāsati, "
     "sammāsamādhi."): AT8,
    "Aṭṭhaṅgiko maggo – sammādiṭṭhi…pe… sammāsamādhi.": AT8_PE,
    "Pañcaṅgiko maggo – sammādiṭṭhi, sammāsaṅkappo, sammāvāyāmo, sammāsati, sammāsamādhi.": AT5,
}
for _n in ("Bojjhaṅgavibhaṅgo", "Maggaṅgavibhaṅgo", "Jhānavibhaṅgo"):
    SENT[f"{_n} niṭṭhito."] = f"{S.CH_HEADINGS[_n]} {K1.DONE}."
LINE = {  # whole Pāli lines -> Vietnamese (ch. 11 Suttanta lines that differ from ch. 4)
    "sammāvāyāmo": L487_EFF, "sammāsati": L487_SATI, "sammāsamādhi": L487_SAMADHI,
}
L467_P = [
    "Idha bhikkhu satimā hoti paramena satinepakkena samannāgato, cirakatampi cirabhāsitampi saritā hoti anussaritā",
    "So tathā sato viharanto taṃ dhammaṃ paññāya pavicinati pavicarati parivīmaṃsamāpajjati",
    "Tassa taṃ dhammaṃ paññāya pavicinato pavicarato parivīmaṃsamāpajjato āraddhaṃ hoti vīriyaṃ asallīnaṃ",
    "Āraddhavīriyassa uppajjati pīti nirāmisā",
    "Pītimanassa kāyopi passambhati, cittampi passambhati",
    "Passaddhakāyassa sukhino cittaṃ samādhiyati",
    "So tathā samāhitaṃ cittaṃ sādhukaṃ ajjhupekkhitā hoti",
]
L467_MAP = dict(zip(L467_P, L467))
INSTR = {  # Avasesā dhammā X(-ena / -ya) sampayuttā: the Pāli word(s) before «sampayuttā»
    "sattahi bojjhaṅgehi": SEVEN_BJ, "aṭṭhaṅgikena maggena": NOUN["aṭṭhaṅgiko maggo"][0],
    "pañcaṅgikena maggena": NOUN["pañcaṅgiko maggo"][0],
    "sammādiṭṭhiyā": PF["sammādiṭṭhi"], "sammāsaṅkappena": PF["sammāsaṅkappo"], "sammāvāyāmena": PF["sammāvāyāmo"],
    "sammāsatiyā": PF["sammāsati"], "sammāsamādhinā": PF["sammāsamādhi"],
}
for _k in BJ_ORDER:
    INSTR[f"{_k}sambojjhaṅga"] = bj(_k)               # Xsambojjhaṅgasampayuttā (compound)
ACC = {f"{_k}sambojjhaṅgaṃ": bj(_k) for _k in BJ_ORDER}   # Xṃ bhāveti
ACC.update({"sammādiṭṭhiṃ": PF["sammādiṭṭhi"], "sammāsaṅkappaṃ": PF["sammāsaṅkappo"], "sammāvācaṃ": PF["sammāvācā"],
            "sammākammantaṃ": PF["sammākammanto"], "sammāājīvaṃ": PF["sammāājīvo"],
            "sammāvāyāmaṃ": PF["sammāvāyāmo"], "sammāsatiṃ": PF["sammāsati"], "sammāsamādhiṃ": PF["sammāsamādhi"]})
NISSITA_P = "vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ"


def rest_chain(s):
    """Avasesā dhammā Xsampayuttā…pe… avasesā dhammā Y sampayuttā. -> «Các hiện tượng còn lại gắn liền với x… …»"""
    parts = [x.strip() for x in s[:-1].split("…pe…")]
    out = []
    for n, p in enumerate(parts):
        m = re.match(r"^[Aa]vasesā dhammā (.+?) ?sampayuttā$", p)
        assert m, p
        x = m.group(1)
        v = f"các hiện tượng còn lại gắn liền với {INSTR[x]}"
        out.append(cap(v) if n == 0 else v)
    return "… ".join(out) + "."


def develop(s):
    """Idha bhikkhu Xṃ bhāveti vivekanissitaṃ …, Yṃ bhāveti…pe… … Zṃ bhāveti vivekanissitaṃ … (^2-471, ^2-489)"""
    body = s[len("Idha bhikkhu "):-1]
    toks = re.split(r"(…pe… |… |, )", body)
    out = ""
    for i, t in enumerate(toks):
        if i % 2:
            out += "; " if t == ", " else "… "
            continue
        m = re.match(r"^(\S+) bhāveti( " + NISSITA_P + ")?$", t)
        assert m, t
        out += f"tu tập {ACC[m.group(1)]}" + (f", {NISSITA}" if m.group(2) else "")
    return f"Ở đây, vị tỳ-khưu {out}."


def body_vi(b):
    m = re.match(r"^(Yo|Yā|Yaṃ) (.*)$", b)
    if m:
        return f"{WHICH} {BODY[m.group(2)]}"
    return L467_MAP[b]


def at_time(rest, sid):
    """the part after the opener («, tasmiṃ samaye …» / «, yā tasmiṃ samaye …») -> Vietnamese (from «, thì …»)"""
    if rest == ", tasmiṃ samaye satta bojjhaṅgā honti – satisambojjhaṅgo…pe… upekkhāsambojjhaṅgo.":
        return f", {THEN} có {SEVEN_BJ} – {bj('sati')}… {bj('upekkhā')}."
    for pa, vi in K45.SUPRA_TAIL[1:3]:                     # aṭṭhaṅgiko / pañcaṅgiko maggo hoti – …
        if rest == f", tasmiṃ samaye {pa}":
            return f", {THEN} {vi}"
    if rest == ", tasmiṃ samaye phasso hoti…pe… avikkhepo hoti.":
        return f", {THEN} {CONTACT_PE}."
    if rest == ", yo tasmiṃ samaye phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā.":
        return f", {THEN} {CONTACT_PE} – {ARE_KUSALA}."
    m = re.match(r'^, (?:yo|yā|yaṃ) tasmiṃ samaye (.*) – (?:ayaṃ|idaṃ) vuccati "(.+?)"\.$', rest)
    assert m, (sid, rest)
    return f", {WHAT_AT_TIME} {BODY[m.group(1)]} {called_n(m.group(2))}"


def opener(s, sid):
    if " …pe…" in s:
        slip(f"^{sid}: a space before «…pe…» (ignored)")
        s = s.replace(" …pe…", "…pe…")
    if s.startswith(SUPRA_P):
        rest = at_time(s[len(SUPRA_P):], sid)
        if rest.startswith(f", {THEN} "):
            return f"{MONK_WHEN} {SUPRA}{rest[len(', ' + THEN):]}"
        return f"{MONK_WHEN} {SUPRA_CORE}{rest}"
    for empty, tp in TASSEVA_P.items():
        if s.startswith(tp + ","):
            return f"{TASSEVA_LOK[empty]}{at_time(s[len(tp):], sid)}"
    raise KeyError((sid, s))


def sentence(s, sid):
    if s in SENT:
        return SENT[s]
    if s.startswith((SUPRA_P, TASSEVA_P[False])) or s.replace(" …pe…", "…pe…").startswith(SUPRA_P):
        return opener(s, sid)
    if s.startswith(("Avasesā dhammā", "avasesā dhammā")):
        return rest_chain(s)
    if s.startswith("Idha bhikkhu ") and NISSITA_P in s:
        return develop(s)
    m = Q_RX.match(s)
    if m:
        return ask(m.group(1))
    m = re.match(r"^Atthi (.+?)( \[[^\]]+\])?, atthi (.+?)( \[[^\]]+\])?\.$", s)
    if m:
        a, va, b, vb = m.groups()
        return (f"Có {L469_ITEMS[a]}{K79.variant(va) if va else ''}, có {L469_ITEMS[b]}"
                f"{K79.variant(vb) if vb else ''}.")
    m = re.match(r"^Yadapi (.+?) tadapi (\S+)sambojjhaṅgo abhiññāya sambodhāya nibbānāya saṃvattati\.$", s)
    if m:
        return f"{cap(L469_ITEMS[m.group(1)])} cũng là {bj(m.group(2))}, {LEADS}."
    m = A_RX.match(s)
    if m:
        body, _, name, pe = m.groups()
        return f"{body_vi(body)} {called_n(name)[:-1]}{'…' if pe else '.'}"
    raise KeyError((sid, s))


def def_line(ln, sid):
    m = re.match(r"^Tattha katam(?:o|ā) (sammāvāyāmo|sammāsati|sammāsamādhi)\? Idha bhikkhu (?!yasmiṃ)", ln)
    if m:
        assert ln.endswith(f'– ayaṃ vuccati "{m.group(1)}".'), ln
        return LINE[m.group(1)]
    return " ".join(sentence(s, sid) for s in SPLIT_RX.split(ln))


# =========================================================================== Pañhāpucchaka (ch. 10-11)
# As ch. 7-9 (K79): «na vattabbā X-ti» stands without the dash, so the Vietnamese has none («không nên nói rằng
# “…”»); a predicate said of all the factors without «siyā» takes «Đều …»; a sentence opening with «siyā» opens with
# «Đôi khi …». New here: named subjects (a single factor, «cha bojjhaṅgā», «satta maggaṅgā») and clauses joined by «;».
# A single awakening factor as subject already contains «là» («chi phần giác ngộ là sự hân hoan»), so «thì» marks
# where its predicate begins (no doubled «là»).
GROUPS = {"Sattannaṃ bojjhaṅgānaṃ": ("Trong bảy chi phần giác ngộ", "bao nhiêu chi phần"),
          "Aṭṭhannaṃ maggaṅgānaṃ": ("Trong tám chi phần của con đường", "bao nhiêu chi phần")}
KENACI_NOUN = {10: "chi phần giác ngộ", 11: "chi phần của con đường"}
SUBJ = {  # Pāli subject (lower case) -> (Vietnamese, number, «thì» after it)
    "pītisambojjhaṅgo": (bj("pīti"), "s", True), "dhammavicayasambojjhaṅgo": (bj("dhammavicaya"), "s", True),
    "cha bojjhaṅgā": (SIX_BJ, "p", False),
    "sammāsaṅkappo": (PF["sammāsaṅkappo"], "s", False), "sammādiṭṭhi": (PF["sammādiṭṭhi"], "s", False),
    "satta maggaṅgā": ("bảy chi phần của con đường", "p", False),      # termbase maggaṅgā «chi phần của con đường»
}
SUBJ_RX = re.compile(r"^(" + "|".join(sorted(SUBJ, key=len, reverse=True)) + r") (.*)$", re.I)
ALL, SIYA, PRON = K79.ALL, K79.SIYA, K79.PRON          # «Đều», «đôi khi», {"s": "nó", "p": "chúng"}
NV = K79.NV79                                          # na vattabbā «không nên nói» (no dash)
PANHA_FIX = [  # (bad, good, slip note): source punctuation rendered as meant
    ("Anāsavā āsavavippayuttā.", "Anāsavā, āsavavippayuttā.",
     "^2-485 «Anāsavā āsavavippayuttā.»: the full stop between the two dyad answers is missing (ch. 11 ^2-507 "
     "«Anāsavā. Āsavavippayuttā.»); rendered as two predicates"),
]
MISSING_NV = "Āsavā ceva āsavasampayuttā cātipi, āsavasampayuttā ceva no ca āsavātipi"


SUBJ.update({  # ch. 12
    "tīṇi jhānāni": ("ba tầng thiền", "p", False), "dve jhānāni": ("hai tầng thiền", "p", False),
    "catutthaṃ jhānaṃ": ("tầng thiền thứ tư", "s", False), "paṭhamaṃ jhānaṃ": ("tầng thiền thứ nhất", "s", False),
})
SUBJ_RX = re.compile(r"^(" + "|".join(sorted(SUBJ, key=len, reverse=True)) + r") (.*)$", re.I)
GROUPS["Catunnaṃ jhānānaṃ"] = ("Trong bốn tầng thiền", "bao nhiêu tầng thiền")
KENACI_NOUN[12] = "tầng thiền"
ETTHU = {"sukhaṃ vedanaṃ": "cảm giác dễ chịu", "adukkhamasukhaṃ vedanaṃ": "cảm giác không khó chịu cũng không dễ chịu",
         "vitakkavicāre": "sự hướng tâm và sự duy trì tâm", "pītiṃ": "sự hân hoan", "sukhaṃ": "hạnh phúc",
         "upekkhaṃ": "sự bình thản", "vitakkaṃ": "sự hướng tâm", "vicāraṃ": "sự duy trì tâm"}
# X – etthuppannaṃ Y ṭhapetvā Z (Ṭhapetvā «ngoại trừ», etthuppannaṃ «sinh khởi trong đó»; termbase)
PRED_LOCAL = {"savitakkaṃ savicāraṃ": K1.pred("savitakkasavicāro")}   # two words in ^2-640


def strip_ti(w):
    """«…cāti» / «…tipi» / «…ntipi» / «…nti» -> the quoted predicate"""
    for suf, add in (("ntipi", "ṃ"), ("nti", "ṃ"), ("tipi", ""), ("ti", "")):
        if w.endswith(suf):
            return re.sub(r"cā$", "ca", w[:-len(suf)] + add)
    raise ValueError(w)


def pred(word, num):
    """a matrix predicate (Pāli, lower case) said of a plural / singular subject -> Vietnamese"""
    if word in PRED_LOCAL:
        return PRED_LOCAL[word]
    if num == "s":
        return K23.get(K23.sg_key(word))
    return K79.pred79(word, "p")


def panha_clause(s, ch, cur=None):
    """one clause (no «; ») of a question-section sentence -> (Vietnamese, not capitalised; current subject)"""
    if s in K79.PANHA_SENT:
        return K79.PANHA_SENT[s], None
    if s == "Kenaci viññeyyā, kenaci na viññeyyā":
        return f"{ALL} {K1.KENACI.replace('những khối', f'những {KENACI_NOUN[ch]}')}", None
    toks = re.split(r"(, |…pe… )", s)
    units, seps = toks[0::2], [""] + toks[1::2]
    cl = []
    for u, sep in zip(units, seps):
        subj = None
        m = SUBJ_RX.match(u)
        if m:
            subj, u = m.group(1).lower(), m.group(2)
        me = re.match(r"^– etthuppann\S+ (.+?) ṭhapetvā (.+)$", u)
        if me:
            cl.append(dict(kind="etthu", what=me.group(1), word=me.group(2), subj=subj, sep=sep, siya=False))
            continue
        if u == "kenaci viññeyyā":
            cl.append(dict(kind="kenaci", subj=subj, sep=sep, siya=False))
            continue
        if u == "kenaci na viññeyyā" and cl and cl[-1]["kind"] == "kenaci":
            continue
        mv = re.match(r"^(siyā |Siyā )?[Nn]a vattabb(?:o|ā|aṃ) (.*)$", u)
        if mv:
            cl.append(dict(kind="nv", siya=bool(mv.group(1)), items=[strip_ti(mv.group(2))], subj=subj, sep=sep))
            continue
        if cl and cl[-1]["kind"] == "nv" and subj is None and sep == ", " and u.endswith("tipi"):
            cl[-1]["items"].append(strip_ti(u))
            continue
        siya = u.startswith(("siyā ", "Siyā "))
        cl.append(dict(kind="pred", siya=siya, word=low(u[5:] if siya else u), subj=subj, sep=sep))
    out, num, topic_open, semi = "", (SUBJ[cur][1] if cur else "p"), False, False
    for i, c in enumerate(cl):
        if c["subj"]:
            cur = c["subj"]
            num = SUBJ[cur][1]
        sv, thi = (SUBJ[cur][0], SUBJ[cur][2]) if cur else (None, False)
        sep = "" if i == 0 else ("…" if c["sep"].startswith("…pe…") else ("; " if semi else ",")[0])
        semi = False
        if c["kind"] == "etthu":
            text = f"{sv} – ngoại trừ {ETTHU[c['what']]} sinh khởi trong đó, {pred(c['word'], num)}"
            semi = True                                # the next unit follows a «;»
        elif c["kind"] == "kenaci":
            text = K1.KENACI.replace("những khối", f"những {KENACI_NOUN[ch]}")
        elif c["kind"] == "nv":
            quoted = ", hay ".join(f"rằng “{pred(k, num)}”" for k in c["items"])
            if c["siya"]:
                text = f"{SIYA} {NV} {quoted}"
            elif c["subj"] or i == 0:
                text = f"về {sv} thì {NV} {quoted}" if sv else f"{NV} {quoted}"
                topic_open = True
            else:
                text, sep = f"{NV} {quoted}", ";"
                topic_open = True
        else:
            v = pred(c["word"], num)
            v = f"{SIYA} {v}" if c["siya"] else v
            if c["subj"]:
                text = f"{sv}{' thì' if thi else ''} {v}"
                topic_open = False
            elif i == 0:
                text = v if c["siya"] or cur else f"{ALL} {v}"
            elif topic_open:
                text, sep = f"{PRON[num]} {v}", ";"
                topic_open = False
            else:
                text = v
        if i and c["subj"]:
            text = "còn " + text                      # a second subject in the same sentence: «…, còn …»
        out += (sep + " " if i else "") + text
    return out, cur


def panha_sentence(s, ch, sid):
    if s.endswith(("Araṇāti", "araṇāti")):            # the closing «ti» of the whole section
        s = s[:-2]
    if s == MISSING_NV:
        slip(f"^{sid} «Āsavā ceva āsavasampayuttā cātipi, āsavasampayuttā ceva no ca āsavātipi.»: «na vattabbā» "
             "missing (the preceding sentence and ch. 11 ^2-507 have it); translated as written, without the "
             "negation: «Rằng “…”, hay rằng “…”.»")
        a, b = [low(strip_ti(x)) for x in s.split(", ")]
        return f"Rằng “{pred(a, 'p')}”, hay rằng “{pred(b, 'p')}”"
    out, cur = [], None
    for c in s.split("; "):
        carry = cur if c.startswith("siyā na vattabbaṃ") else None   # neuter: still the singular subject
        v, cur = panha_clause(c, ch, carry)
        out.append(v)
    return "; ".join(out)


PANHA_FIX += [
    ('"', "", None),                                   # ch. 12: «na vattabbā "X"ti» quoted (the words are the same)
    ("maggahetukantipi maggādhipatītipi", "maggahetukantipi, maggādhipatītipi",
     "^2-640 «maggahetukantipi maggādhipatītipi»: comma missing (added)"),
    ("paccuppannāramaṇantipi", "paccuppannārammaṇantipi",
     "^2-640 «paccuppannāramaṇantipi» for paccuppannārammaṇantipi (spelling slip, rendered as meant)"),
    ("āsavavippayuttā sāsavā", "āsavavippayuttasāsavā",
     "^2-641 «āsavavippayuttā sāsavā / anāsavā» written as two words (matrix: āsavavippayuttasāsavā; same "
     "Vietnamese)"),
    ("āsavavippayuttā anāsavā", "āsavavippayuttaanāsavā", None),
    (", tīṇi jhānāni upekkhāsahagatā, na kāmāvacarā", ", tīṇi jhānāni upekkhāsahagatā; na kāmāvacarā",
     "^2-641 «catutthaṃ jhānaṃ … upekkhāsahagataṃ, tīṇi jhānāni upekkhāsahagatā»: the negation of the parallels "
     "(«na …sahagatā») is missing; translated as written «còn ba tầng thiền có sự bình thản đi kèm»"),
    (", tīṇi jhānāni na arūpāvacarā", "; tīṇi jhānāni na arūpāvacarā", None),
    (", siyā pariyāpannā", "; siyā pariyāpannā", None),
    (", araṇāti.", "; araṇāti.", None),
]


def panha_line(p, sid, ch):
    for bad, good, nt in PANHA_FIX + K79.LINE_FIX:
        if bad in p:
            p = p.replace(bad, good)
            if nt:
                slip(nt)
    out = []
    for s in re.split(r"(?<=\.) (?=[A-ZĀĪŪṬÑṆḌḶṂ])", p):
        assert s.endswith("."), s
        out.append(cap(panha_sentence(s[:-1], ch, sid)) + ".")
    return " ".join(out)


def panha_question(p):
    """Sattannaṃ bojjhaṅgānaṃ kati kusalā, … kati araṇā? (as K79.panha_question)"""
    m = re.match(r"^(.*?) (kati .*)\?$", p)
    grp, body = m.groups()
    head, kati = GROUPS[grp]
    parts = re.split(r"(…pe…|, )", body)
    out = [f"{head},"]
    for i, x in enumerate(parts):
        if i % 2 == 1:
            out.append("…" if x == "…pe…" else ",")
            continue
        x = x.strip()
        if x:
            out.append(f" {kati} {K1.pred(K1.PL_KEY[re.sub(r'^kati ', '', x)])}")
    return "".join(out) + "?"


# =========================================================================== chapter 12: Suttanta strings
SANTA = ("đã lắng yên, đã được làm lắng dịu, đã lắng dịu hoàn toàn, đã biến mất, đã biến mất hoàn toàn, đã đi đến "
         "kết thúc, đã đi đến kết thúc hoàn toàn, đã bị làm khô cạn, đã bị làm khô cạn hoàn toàn, đã bị làm cho tiêu "
         "tan")      # santā samitā vūpasantā … byantīkatā (ch. 7 VINITA without vinītā paṭivinītā)
assert SANTA in K79.VINITA
pi2(SANTA)
CLEANSE = ("làm trong sạch, làm trong sạch hẳn, làm trong sạch hoàn toàn, làm cho thoát khỏi, làm cho thoát hẳn, làm "
           "cho thoát hoàn toàn")
# sodheti «làm trong sạch», parisodheti «làm trong sạch hoàn toàn», moceti «làm cho thoát khỏi», vimoceti «làm cho
# thoát hẳn», parimoceti «làm cho thoát hoàn toàn» (termbase); visodheti: no entry, «làm trong sạch hẳn»
misfit("visodheti (^2-541, 545, 551, 556, 560): no entry; «làm trong sạch hẳn», parallel to vimoceti «làm cho thoát "
       "hẳn»")
GIVEN_UP = ("đã được từ bỏ, đã được nhả ra, đã được thả ra, đã được dứt bỏ, đã được buông bỏ, đã được dứt bỏ và buông "
            "bỏ")
# cattattā (no entry: «đã được từ bỏ»), vantattā «đã được nhả ra», muttattā «đã được thả ra», pahīnattā «đã được dứt
# bỏ», paṭinissaṭṭhattā «đã được buông bỏ», pahīnapaṭinissaṭṭhattā (built from the two)
misfit("cattattā (^2-547, ^2-553): no entry; «đã được từ bỏ»")
GAIN = "sự đạt được, sự có được, sự đạt đến, sự đạt đến trọn vẹn, sự chạm, sự tự mình chứng nghiệm, sự chứng nhập"
# lābho paṭilābho patti sampatti phusanā sacchikiriyā upasampadā (ch. 9 iddhi definition terms)
assert GAIN in K79.IDDHI_DEF
pi2(GAIN)
OVERCOME = "đã vượt qua, đã vượt khỏi, đã vượt qua hoàn toàn"   # atikkanto vītikkanto samatikkanto (termbase)
JATA = "đã sinh ra, đã sinh thành, đã phát sinh, đã phát sinh rõ rệt, đã hiện ra"   # jātā … pātubhūtā (user)
assert JATA == S.PRES_S.split(", đã sinh khởi")[0].replace(" đã trở thành,", "")   # sample string without bhūta
SAMAPANNA = ("của người đã chứng nhập {x}, hoặc của người đã tái sinh vào đó, hoặc của người an trú trong hạnh phúc "
             "ngay trong đời này")
# X samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā (samāpannassa «người đã chứng nhập», upapannassa
# «người đã tái sinh»; diṭṭhadhammasukhavihāra as pi-1 «an trú trong hạnh phúc ngay trong đời này»)
CITTACET = "tâm và các yếu tố đồng hành với tâm"   # cittacetasikā dhammā (citta «tâm», cetasikā «yếu tố đồng hành …»)
SANNA3 = "tri giác, sự nhận ra, trạng thái đã nhận ra"   # saññā sañjānanā sañjānitattaṃ (pi-1 ^1-61)
pi1(SANNA3)
VICARA = pi1("sự chuyển động của tâm, sự duy trì tâm, sự duy trì tâm liên tục, sự duy trì tâm sát sao, sự gắn kết "
             "liên tục của tâm với đối tượng, sự theo dõi sát đối tượng")         # pi-1 ^1-8
VICARA_ANU = VICARA.replace("sự chuyển động của tâm, ", "sự chuyển động của tâm, sự chuyển động tiếp nối, ")
SADDHA4 = "niềm tin, sự tin tưởng, sự tin chắc, lòng tin sâu sắc"   # saddhā saddahanā okappanā abhippasādo (pi-1 ^1-12)
assert K45.SADDHA.startswith(SADDHA4)
PANNA_FULL = p1_list("1-16", "trí tuệ, sự hiểu rõ, sự tìm hiểu,", " – đó là")   # paññā pajānanā vicayo … sammādiṭṭhi
DOSA = p1_list("1-1066", "sự oán giận của tâm", " – đó được gọi là")           # cittassa āghāto … anattamanatā cittassa
DOSA_V = DOSA.replace("trạng thái khởi sân,", f"trạng thái khởi sân {S.spell('Syā.', 'dūsanā dūsitattaṃ')},")
DOSA_PE = "sự oán giận của tâm… " + ", ".join(DOSA.split(", ")[-3:])   # āghāto…pe… caṇḍikkaṃ asuropo anattamanatā
assert DOSA_PE.endswith("sự hung dữ, sự nói năng cộc cằn, sự không hài lòng của tâm"), DOSA_PE
THINA = p1_list("1-1162", "sự không khỏe khoắn của tâm", " – đó được gọi là")
THINA_V = THINA.replace("trạng thái khởi uể oải của tâm",
                        f"trạng thái khởi uể oải {S.spell('Sī., Syā.', 'thīyanā thīyitattaṃ')} của tâm")
MIDDHA = p1_list("1-1163", "sự không khỏe khoắn của thân tinh thần", " – đó được gọi là")
UDDHACCA = p1_list("1-1165", "sự xao động của tâm", " – đó được gọi là")
KUKKUCCA_PRE = p1_list("1-1166", "Tri giác điều không được phép", ". Điều mà thuộc loại")
KUKKUCCA_LIST = p1_list("1-1166", "sự hối tiếc, sự khởi hối tiếc", " – đó được gọi là")
VICIKICCHA = p1_list("1-1008", "sự nghi ngờ, sự khởi nghi ngờ", " – đó được gọi là")
VICIKICCHA_SHORT = "sự nghi ngờ, sự khởi nghi ngờ, trạng thái khởi nghi ngờ, trạng thái cứng đờ của tâm, sự giằng xé của ý"
ASPACE = p1_list("1-637", "Không gian, điều được xem là không gian", " – vật chất này")
VITAKKA_FULL12 = VITAKKA_FULL                   # takko vitakko … sammāsaṅkappo (pi-1 ^1-7)
VITAKKA_PE = f"suy nghĩ, sự hướng tâm… {PF['sammāsaṅkappo']}"   # takko vitakko…pe… sammāsaṅkappo (ch. 4)
SATI_PE3 = f"sự tỉnh thức, sự nhớ lại, sự hồi tưởng… {PF['sammāsati']}"   # sati anussati paṭissati…pe… sammāsati
SAMPAJ = {  # the clear-comprehension activities (So abhikkante … sampajānakārī hoti)
    "abhikkante paṭikkante": "khi đi tới, khi đi lui", "ālokite vilokite": "khi nhìn thẳng, khi nhìn quanh",
    "samiñjite pasārite": "khi co tay chân, khi duỗi tay chân",
    "saṅghāṭipattacīvaradhāraṇe": "khi mang y ngoài, bình bát và y phục",   # saṅghāṭi «y ngoài», cīvara «y phục»
    "asite pīte khāyite sāyite": "khi ăn, khi uống, khi nhai, khi nếm",
    "uccārapassāvakamme": "khi đại tiện, tiểu tiện",
    "gate ṭhite nisinne sutte jāgarite bhāsite tuṇhībhāve": ("khi đi, khi đứng, khi ngồi, khi ngủ, khi thức, khi nói, "
                                                          "khi im lặng"),
}
misfit("uccārapassāvakamme (^2-508, 523, 525): no entry; «khi đại tiện, tiểu tiện»")
SAMPAJ_KARI = "hành động với sự hiểu biết rõ ràng"          # sampajānakārī (termbase)
SATO_KARI = "hành động với sự tỉnh thức và hiểu biết rõ ràng"   # sato sampajānakārī (termbase)
SATO_SAMP = "tỉnh thức và hiểu biết rõ ràng"                # sato sampajāno (sato «tỉnh thức», sampajāno «hiểu …»)
MOVES = ["khi đi tới", "khi đi lui", "khi nhìn thẳng", "khi nhìn quanh", "khi co tay chân", "khi duỗi tay chân"]
# sato sampajāno abhikkamati «đi tới» / paṭikkamati «đi lui» / āloketi «nhìn thẳng» / viloketi «nhìn quanh» /
# samiñjeti «co tay chân» / pasāreti «duỗi tay chân»
SAMPAJ_Q = (f"{SAMPAJ_KARI} {SAMPAJ['abhikkante paṭikkante']}; {SAMPAJ_KARI} {SAMPAJ['ālokite vilokite']}; "
            f"{SAMPAJ_KARI} {SAMPAJ['samiñjite pasārite']}; {SAMPAJ_KARI} {SAMPAJ['saṅghāṭipattacīvaradhāraṇe']}; "
            f"{SAMPAJ_KARI} {SAMPAJ['asite pīte khāyite sāyite']}; {SAMPAJ_KARI} {SAMPAJ['uccārapassāvakamme']}; "
            f"{SAMPAJ_KARI} {SAMPAJ['gate ṭhite nisinne sutte jāgarite bhāsite tuṇhībhāve']}")


def sato_moves(last_sato):
    """Idha / Evaṃ bhikkhu sato sampajāno abhikkamati, … tuṇhībhāve (sato) sampajānakārī hoti(ti)"""
    a = ", ".join(f"{SATO_SAMP} {x}" for x in MOVES)
    b = "; ".join([SATO_KARI] + [f"{SATO_KARI} {SAMPAJ[k]}" for k in (
        "saṅghāṭipattacīvaradhāraṇe", "asite pīte khāyite sāyite", "uccārapassāvakamme")])
    c = f"{SATO_KARI if last_sato else SAMPAJ_KARI} {SAMPAJ['gate ṭhite nisinne sutte jāgarite bhāsite tuṇhībhāve']}"
    return f"vị tỳ-khưu {a}; {b}; {c}"


RESORT = "hạnh kiểm đúng đắn và nơi lui tới thích hợp"    # ācāragocara (ācāro, gocaro: termbase)
PATIMOKKHA = "bộ giới luật căn bản"                        # pātimokkha (termbase)
P_SAMVARA = f"sự thu thúc theo {PATIMOKKHA}"               # pātimokkhasaṃvaro (saṃvaro «sự thu thúc»)
SENSE_DOOR = "phòng hộ cửa các giác quan"                  # indriyesu guttadvāro (guttadvāratā «sự phòng hộ cửa»)
FOOD_MEASURE = "biết tiết độ trong ăn uống"                # bhojane mattaññū (termbase)
WAKE = "chuyên tâm thực hành việc thức canh vào đầu đêm và cuối đêm"   # pubbarattāpararattaṃ jāgariyānuyogamanuyutto
BODHI = "các hiện tượng hỗ trợ cho sự giác ngộ"             # bodhipakkhikā dhammā (termbase)
BODHI_YOGA = f"chuyên tâm thực hành việc tu tập {BODHI}"    # bodhipakkhikānaṃ dhammānaṃ bhāvanānuyogamanuyutto
SIKKHA = "thọ trì và tu học trong các điều tu học"          # samādāya sikkhati sikkhāpadesu (Sikkhāpada «điều tu học»)
BHAYA = "thấy sự nguy hiểm trong những lỗi nhỏ nhặt"        # aṇumattesu vajjesu bhayadassāvī
misfit("bhayadassāvī, vajjadassāvī, ādīnavadassāvī, nissaraṇadassāvī (^2-508, ^2-515): no entries; «thấy sự nguy "
       "hiểm», «thấy lỗi lầm» (vajja «lỗi lầm»), «thấy sự tai hại», «thấy lối thoát»")
SECLUDED = ("rừng, gốc cây, núi, khe núi, hang núi, bãi tha ma, rừng sâu, khoảng trời trống, đống rơm")
CHANGES = {  # the hindrance clauses of ^2-508 (sentence) -> Vietnamese
    "So abhijjhaṃ loke pahāya vigatābhijjhena cetasā viharati, abhijjhāya cittaṃ parisodheti.":
        ("Sau khi dứt bỏ sự thèm muốn đối với thế gian, vị ấy sống với tâm đã lìa sự thèm muốn, làm trong sạch hoàn "
         "toàn tâm khỏi sự thèm muốn."),
    ("Byāpādapadosaṃ pahāya abyāpannacitto viharati sabbapāṇabhūtahitānukampī, byāpādapadosā cittaṃ "
     "parisodheti."):
        ("Sau khi dứt bỏ ác ý và sự sân hận dữ dội, vị ấy sống với tâm không ác ý, thương xót và mong điều lợi ích cho "
         "mọi chúng sinh, muôn loài, làm trong sạch hoàn toàn tâm khỏi ác ý và sự sân hận dữ dội."),
    ("Thinamiddhaṃ pahāya vigatathinamiddho viharati ālokasaññī sato sampajāno, thinamiddhā cittaṃ "
     "parisodheti."):
        ("Sau khi dứt bỏ sự uể oải và đờ đẫn, vị ấy sống đã lìa sự uể oải và đờ đẫn, có tri giác về ánh sáng, tỉnh "
         "thức và hiểu biết rõ ràng, làm trong sạch hoàn toàn tâm khỏi sự uể oải và đờ đẫn."),
    ("Uddhaccakukkuccaṃ pahāya anuddhato viharati ajjhattaṃ vūpasantacitto, uddhaccakukkuccā cittaṃ "
     "parisodheti."):
        ("Sau khi dứt bỏ sự xao động và hối tiếc, vị ấy sống không xao động, có tâm đã lắng dịu hoàn toàn ở nơi bản "
         "thân, làm trong sạch hoàn toàn tâm khỏi sự xao động và hối tiếc."),
    "Vicikicchaṃ pahāya tiṇṇavicikiccho viharati akathaṃkathī kusalesu dhammesu, vicikicchāya cittaṃ parisodheti.":
        ("Sau khi dứt bỏ sự hoài nghi, vị ấy sống đã vượt qua sự hoài nghi, không còn băn khoăn đối với các hiện "
         "tượng thiện, làm trong sạch hoàn toàn tâm khỏi sự hoài nghi."),
}
misfit("sabbapāṇabhūtahitānukampī (^2-508): no entry; built from pāṇa «chúng sinh», bhūta «muôn loài»: «thương xót "
       "và mong điều lợi ích cho mọi chúng sinh, muôn loài»")
L508_JHANA_P = ("So ime pañca nīvaraṇe pahāya cetaso upakkilese paññāya dubbalīkaraṇe vivicceva kāmehi vivicca "
                "akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ upasampajja viharati; ")
L508_JHANA = (f"Sau khi dứt bỏ năm chướng ngại này, là những thứ làm vẩn đục tâm, làm suy yếu trí tuệ, vị ấy {JH1}; "
              f"{JH2}; {JH3}; {JH4}; {AR1}; {AR2}; {AR3}; {AR4}.")
slip("^2-508 «\"natthi kiñcī\"ti ākiñcāyatanaṃ upasampajja viharati»: «ākiñcāyatanaṃ» for ākiñcaññāyatanaṃ (spelling "
     "slip, rendered as meant «lĩnh vực không có gì cả»)")
# ---- topics: Pāli quoted word or phrase (first letter lower case, «ṃ» restored for «…nti») -> (kind, Vietnamese)
TOPICS = {
    "idha": ("w", "ở đây"), "bhikkhu": ("w", "tỳ-khưu"), "pātimokkhaṃ": ("w", PATIMOKKHA),
    "saṃvaro": ("w", "sự thu thúc"), "saṃvuto": ("w", "được thu thúc"),
    "pātimokkhasaṃvarasaṃvuto": ("c", f"được thu thúc bằng {P_SAMVARA}"),
    "viharati": ("w", "sống"), "ācāragocarasampanno": ("c", f"thành tựu {RESORT}"),
    "gocaro": ("w", "nơi lui tới thích hợp"), "aṇumattesu vajjesu bhayadassāvī": ("c", BHAYA),
    "samādāya sikkhati sikkhāpadesu": ("c", SIKKHA), "indriyesu guttadvāro": ("c", SENSE_DOOR),
    "bhojane mattaññū": ("c", FOOD_MEASURE), "sātaccaṃ": ("w", "sự liên tục"), "nepakkaṃ": ("w", "sự khôn ngoan"),
    "bodhipakkhikānaṃ dhammānaṃ bhāvanānuyogamanuyutto": ("c", BODHI_YOGA),
    "sampajāno": ("w", "hiểu biết rõ ràng"), "vivittaṃ": ("w", "thanh vắng"), "senāsanaṃ": ("w", "chỗ ở"),
    "vivittaṃ senāsanaṃ bhajati": ("c", "lui tới chỗ ở thanh vắng"), "araññaṃ": ("w", "rừng"),
    "rukkhamūlaṃ": ("w", "gốc cây"), "vanapatthaṃ": ("w", "rừng sâu"), "appasaddaṃ": ("w", "ít tiếng động"),
    "appanigghosaṃ": ("w", "ít ồn ào"),                        # nigghosaṃ «ồn ào»
    "araññagato vā rukkhamūlagato vā suññāgāragato vā": ("c", "đi đến rừng, hoặc đi đến gốc cây, hoặc đi đến ngôi "
                                                              "nhà trống"),
    "nisīdati pallaṅkaṃ ābhujitvā": ("c", "ngồi xuống, xếp chân kiết già"),
    "ujuṃ kāyaṃ paṇidhāya": ("c", "đặt thân ngay thẳng"),
    "parimukhaṃ satiṃ upaṭṭhapetvā": ("c", "thiết lập sự tỉnh thức trước mặt"),
    "abhijjhaṃ loke pahāya": ("c", "sau khi dứt bỏ sự thèm muốn đối với thế gian"),
    "vigatābhijjhena cetasā": ("c", "với tâm đã lìa sự thèm muốn"),
    "abhijjhāya cittaṃ parisodheti": ("c", "làm trong sạch hoàn toàn tâm khỏi sự thèm muốn"),
    "byāpādapadosaṃ pahāya": ("c", "sau khi dứt bỏ ác ý và sự sân hận dữ dội"),
    "abyāpannacitto": ("w", "với tâm không ác ý"),
    "byāpādapadosā cittaṃ parisodheti": ("c", "làm trong sạch hoàn toàn tâm khỏi ác ý và sự sân hận dữ dội"),
    "thinamiddhaṃ pahāya": ("c", "sau khi dứt bỏ sự uể oải và đờ đẫn"),
    "vigatathinamiddho": ("w", "đã lìa sự uể oải và đờ đẫn"), "ālokasaññī": ("w", "có tri giác về ánh sáng"),
    "sato sampajāno": ("c", SATO_SAMP),
    "thinamiddhā cittaṃ parisodheti": ("c", "làm trong sạch hoàn toàn tâm khỏi sự uể oải và đờ đẫn"),
    "uddhaccakukkuccaṃ pahāya": ("c", "sau khi dứt bỏ sự xao động và hối tiếc"),
    "anuddhato": ("w", "không xao động"), "vūpasantacitto": ("w", "có tâm đã lắng dịu hoàn toàn"),
    "ajjhattaṃ vūpasantacitto": ("c", "có tâm đã lắng dịu hoàn toàn ở nơi bản thân"),
    "uddhaccakukkuccā cittaṃ parisodheti": ("c", "làm trong sạch hoàn toàn tâm khỏi sự xao động và hối tiếc"),
    "vicikicchaṃ pahāya": ("c", "sau khi dứt bỏ sự hoài nghi"),
    "tiṇṇavicikiccho": ("w", "đã vượt qua sự hoài nghi"),
    "akathaṃkathī kusalesu dhammesu": ("c", "không còn băn khoăn đối với các hiện tượng thiện"),
    "vicikicchāya cittaṃ parisodheti": ("c", "làm trong sạch hoàn toàn tâm khỏi sự hoài nghi"),
    "ime pañca nīvaraṇe pahāya": ("c", "sau khi dứt bỏ năm chướng ngại này"),
    "cetaso upakkilese": ("c", "những thứ làm vẩn đục tâm"), "paññāya dubbalīkaraṇe": ("c", "làm suy yếu trí tuệ"),
    "vivicceva kāmehi vivicca akusalehi dhammehi": ("c", pi1("hoàn toàn tách khỏi các dục lạc, tách khỏi các hiện "
                                                             "tượng bất thiện")),
    "savitakkaṃ savicāraṃ": ("c", "có sự hướng tâm và sự duy trì tâm"),
    "vivekajaṃ": ("w", "sinh từ sự tách biệt"), "pītisukhaṃ": ("c", "sự hân hoan và hạnh phúc"),
    "paṭhamaṃ": ("w", "thứ nhất"), "dutiyaṃ": ("w", "thứ hai"), "tatiyaṃ": ("w", "thứ ba"),
    "catutthaṃ": ("w", "thứ tư"), "jhānaṃ": ("w", "tầng thiền"), "upasampajja": ("w", "chứng nhập"),
    "vitakkavicārānaṃ vūpasamā": ("c", pi1("nhờ sự hướng tâm và sự duy trì tâm lắng xuống")),
    "ajjhattaṃ": ("w", "ở nơi bản thân"), "sampasādanaṃ": ("w", "sự trong sáng"),
    "cetaso ekodibhāvaṃ": ("c", pi1("sự hợp nhất của tâm")),
    "avitakkaṃ avicāraṃ": ("c", pi1("không có sự hướng tâm cũng không có sự duy trì tâm")),
    "samādhijaṃ": ("w", "sinh từ định tâm"), "pītiyā ca virāgā": ("c", pi1("nhờ sự hân hoan phai nhạt")),
    "upekkhako": ("w", "bình thản"), "sato ca sampajāno": ("c", SATO_SAMP),
    "sukhañca kāyena paṭisaṃvedeti": ("c", pi1("cảm nhận hạnh phúc bằng thân")),
    "yaṃ taṃ ariyā ācikkhanti": ("c", pi1("là trạng thái mà nhờ đó các bậc thánh mô tả người ấy")),
    "upekkhako satimā sukhavihārī": ("c", pi1("Người bình thản, có sự tỉnh thức, an trú trong hạnh phúc")),
    "sukhassa ca pahānā dukkhassa ca pahānā": ("c", pi1("nhờ dứt bỏ sự dễ chịu và dứt bỏ sự khó chịu")),
    "pubbeva somanassadomanassānaṃ atthaṅgamā": ("c", pi1("nhờ niềm vui và nỗi buồn đã biến mất từ trước")),
    "adukkhamasukhaṃ": ("c", "không khó chịu cũng không dễ chịu"),
    "upekkhāsatipārisuddhiṃ": ("c", pi1("có sự tỉnh thức hoàn toàn trong sạch nhờ sự bình thản")),
    "sabbaso rūpasaññānaṃ samatikkamā": ("c", "nhờ hoàn toàn vượt qua các tri giác về hình sắc"),
    "paṭighasaññānaṃ atthaṅgamā": ("c", "nhờ các tri giác về sự va chạm biến mất"),
    "nānattasaññānaṃ amanasikārā": ("c", "nhờ không chú tâm đến các tri giác về sự đa dạng"),
    "ananto ākāso": ("c", THOUGHT["ākāsa"]), "ākāsānañcāyatanaṃ": ("c", AY_INF["ākāsa"]),
    "sabbaso ākāsānañcāyatanaṃ samatikkamma": ("c", f"hoàn toàn vượt qua {AY_INF['ākāsa']}"),
    "anantaṃ viññāṇaṃ": ("c", THOUGHT["viññāṇa"]), "viññāṇañcāyatanaṃ": ("c", AY_INF["viññāṇa"]),
    "sabbaso viññāṇañcāyatanaṃ samatikkamma": ("c", f"hoàn toàn vượt qua {AY_INF['viññāṇa']}"),
    "natthi kiñci": ("c", THOUGHT["ākiñcañña"]), "ākiñcaññāyatanaṃ": ("c", AY_INF["ākiñcañña"]),
    "sabbaso ākiñcaññāyatanaṃ samatikkamma": ("c", f"hoàn toàn vượt qua {AY_INF['ākiñcañña']}"),
    "nevasaññīnāsaññī": ("c", "không phải có tri giác cũng không phải không có tri giác"),
    "nevasaññānāsaññāyatanaṃ": ("c", AY_INF["nevasaññā"]),
}
for _k in ("sabbaso rūpasaññānaṃ samatikkamā", "paṭighasaññānaṃ atthaṅgamā", "nānattasaññānaṃ amanasikārā"):
    assert TOPICS[_k][1] in OVERCOME_R
JHANA_SIDS = {"2-571", "2-582", "2-585", "2-593", "2-601", "2-608", "2-613", "2-618", "2-622"}
VIHARATI_J = VIHARATI[:-len("sống.")] + "an trú."      # the jhāna sense (user: «an trú» in the jhānas)
misfit("viharati in the jhāna glosses (^2-571 … ^2-622, and ^2-589 «… carati viharati» of sukhavihārī): the "
       "termbase sense 'dwells in a meditative attainment' «an trú» is used as topic, list word and in «Tena vuccati»; "
       "the conduct glosses (^2-512, 540, 544, 548, 554) keep «sống» (user)")


def topic_key(t, n):
    t = low(t)
    return t + ("ṃ" if n else "")


def topic_vi(key, sid):
    if key == "viharatī":
        key = "viharati"
    for long_, short in (("ī", "i"), ("ā", "a"), ("ū", "u")):    # the lengthened final vowel before «ti»
        if key not in TOPICS and key.endswith(long_) and key[:-1] + short in TOPICS:
            key = key[:-1] + short
    kind, v = TOPICS[key]
    if key == "viharati" and sid in JHANA_SIDS:
        v = "an trú"
    return kind, v, key


# ---- ch. 12 sentences (Pāli, capitalised) -> Vietnamese (capitalised); topic bodies are looked up capitalised
def _neg_gifts(neg):
    """the wrong livelihoods of ^2-513 (vā … / na …)"""
    items = ["việc biếu tre", "việc biếu lá", "việc biếu hoa", "việc biếu trái cây", "việc biếu đồ tắm gội",
             "việc biếu cây chà răng", "lời nịnh bợ", "lời nửa thật nửa giả", "việc chăm bẵm con trẻ",
             "việc chạy việc vặt"]
    if neg:
        return ", ".join(f"không bằng {x}" for x in items)
    items[7] += " " + S.spell("Sī.", "muggasuppatāya")
    return ", ".join(("bằng " if n == 0 else "hoặc bằng ") + x for n, x in enumerate(items))


misfit("veḷudānena … dantakaṭṭhadānena, jaṅghapesanikena, buddhapaṭikuṭṭhena (^2-513): no entries; «việc biếu tre, "
       "lá, hoa, trái cây, đồ tắm gội, cây chà răng», «việc chạy việc vặt», «bị Đức Phật chê trách»")
RESORTS = ["nhà kỹ nữ", "nhà góa phụ", "nhà thiếu nữ đã lớn tuổi", "nhà người ái nam ái nữ", "chỗ tỳ-khưu-ni",
           "quán rượu"]
misfit("vesiyāgocaro … pānāgāragocaro, rājamahāmattehi, titthiyasāvakehi, anopānabhūtāni, akkosakaparibhāsakāni, "
       "kāsāvapajjotāni, isivātapaṭivātāni (^2-514): no entries; built from their members and the commentary sense")
COMPANY = ("với vua chúa, với quan đại thần của vua, với các đạo sĩ ngoại đạo, với đệ tử của các đạo sĩ ngoại đạo, bằng "
           "sự giao du không thích đáng")
FOR4 = "cho các tỳ-khưu, tỳ-khưu-ni, nam cư sĩ, nữ cư sĩ"
FAMILIES = "vị ấy gần gũi, lui tới, thường xuyên lui tới hầu cận những gia đình như vậy"   # sevati bhajati payirupāsati
L_AGOCARA = ("Ở đây, có người lui tới " + ", hoặc lui tới ".join(RESORTS) + f"; sống giao du {COMPANY}; hoặc có những "
             "gia đình không có niềm tin, không có lòng tin trong sáng, không phải là nơi nương tựa như giếng nước, hay "
             "mắng nhiếc và lăng mạ, mong điều không lợi ích, mong điều không tốt lành, mong điều không thoải mái, mong "
             f"điều không an ổn {FOR4}; {FAMILIES}")
L_GOCARA = ("Ở đây, có người không lui tới " + ", không lui tới ".join(RESORTS) + f"; sống không giao du {COMPANY}; "
            "hoặc có những gia đình có niềm tin, có lòng tin trong sáng, là nơi nương tựa như giếng nước, rực sáng ánh y "
            "cà-sa, có làn gió của các bậc ẩn sĩ thổi qua lại, mong điều lợi ích, mong điều tốt lành, mong điều thoải "
            f"mái, mong điều an ổn {FOR4}; {FAMILIES}")
EYE_TAIL = {  # Yatvādhikaraṇamenaṃ X asaṃvutaṃ viharantaṃ … (negative / positive)
    False: ("Vì nếu người ấy sống với {i} không được thu thúc thì sự thèm muốn và nỗi buồn, những hiện tượng bất thiện "
            "xấu ác, có thể tràn vào, nên người ấy không thực hành để thu thúc năng lực ấy, không bảo vệ {i}, không "
            "thực hiện sự thu thúc nơi {i}."),
    True: ("Vì nếu người ấy sống với {i} không được thu thúc thì sự thèm muốn và nỗi buồn, những hiện tượng bất thiện "
           "xấu ác, có thể tràn vào, nên người ấy thực hành để thu thúc năng lực ấy, bảo vệ {i}, thực hiện sự thu thúc "
           "nơi {i}."),
}
SENSES5 = ("Khi nghe âm thanh bằng tai… khi ngửi mùi bằng mũi… khi nếm vị bằng lưỡi… khi chạm vật xúc chạm bằng thân… "
           "khi nhận biết đối tượng của ý bằng ý thì người ấy")
GRASP = {False: "nắm giữ dấu hiệu tổng quát, nắm giữ các chi tiết",
         True: "không nắm giữ dấu hiệu tổng quát, không nắm giữ các chi tiết"}
misfit("nimittaggāhī, anubyañjanaggāhī (^2-517): no entries; built from nimitta «dấu hiệu tổng quát», gāhī «nắm "
       "giữ»: «nắm giữ dấu hiệu tổng quát», «nắm giữ các chi tiết»")
CUT = {"sīlaṃ": "giới hạnh"}
SENT12 = {
    # ^2-508
    ("Idha bhikkhu pātimokkhasaṃvarasaṃvuto viharati, ācāragocarasampanno, aṇumattesu vajjesu bhayadassāvī, samādāya "
     "sikkhati sikkhāpadesu indriyesu guttadvāro bhojane mattaññū pubbarattāpararattaṃ jāgariyānuyogamanuyutto "
     "sātaccaṃ nepakkaṃ bodhipakkhikānaṃ dhammānaṃ bhāvanānuyogamanuyutto."):
        (f"Ở đây, vị tỳ-khưu sống được thu thúc bằng {P_SAMVARA}, thành tựu {RESORT}, {BHAYA}, {SIKKHA}, {SENSE_DOOR}, "
         f"{FOOD_MEASURE}, {WAKE}, {BODHI_YOGA} với sự liên tục và sự khôn ngoan."),
    ("So abhikkante paṭikkante sampajānakārī hoti, ālokite vilokite sampajānakārī hoti, samiñjite [sammiñjite (sī. "
     "syā.)] pasārite sampajānakārī hoti, saṅghāṭipattacīvaradhāraṇe sampajānakārī hoti, asite pīte khāyite sāyite "
     "sampajānakārī hoti, uccārapassāvakamme sampajānakārī hoti, gate ṭhite nisinne sutte jāgarite bhāsite "
     "tuṇhībhāve sampajānakārī hoti."):
        "Vị ấy " + SAMPAJ_Q.replace("khi co tay chân", f"khi co tay chân {S.spell('Sī., Syā.', 'sammiñjite')}", 1)
        + ".",
    ("So vivittaṃ senāsanaṃ bhajati araññaṃ rukkhamūlaṃ pabbataṃ kandaraṃ giriguhaṃ susānaṃ vanapatthaṃ abbhokāsaṃ "
     "palālapuñjaṃ appasaddaṃ appanigghosaṃ vijanavātaṃ manussarāhasseyyakaṃ [manussarāhaseyyakaṃ (sī. syā.)] "
     "paṭisallānasāruppaṃ."):
        (f"Vị ấy lui tới chỗ ở thanh vắng: {SECLUDED}, nơi ít tiếng động, ít ồn ào, vắng hơi người, kín đáo đối với "
         f"con người {S.spell('Sī., Syā.', 'manussarāhaseyyakaṃ')}, thích hợp cho sự độc cư."),
    ("So araññagato vā rukkhamūlagato vā suññāgāragato vā nisīdati pallaṅkaṃ ābhujitvā ujuṃ kāyaṃ paṇidhāya "
     "parimukhaṃ satiṃ upaṭṭhapetvā."):
        ("Vị ấy đi đến rừng, hoặc đi đến gốc cây, hoặc đi đến ngôi nhà trống, ngồi xuống, xếp chân kiết già, đặt thân "
         "ngay thẳng, thiết lập sự tỉnh thức trước mặt."),
    # ^2-509 … ^2-511
    ("Imissā diṭṭhiyā, imissā khantiyā, imissā ruciyā, imasmiṃ ādāye, imasmiṃ dhamme, imasmiṃ vinaye, imasmiṃ "
     "dhammavinaye, imasmiṃ pāvacane, imasmiṃ brahmacariye, imasmiṃ satthusāsane."):
        ("Theo quan điểm này, theo sự chấp nhận này, theo sự ưa thích này, trong sự tiếp nhận này, trong Giáo Pháp "
         "này, trong Giới Luật này, trong Giáo Pháp và Giới Luật này, trong lời dạy này, trong đời sống tu hành trong "
         "sạch này, trong giáo huấn của Bậc Đạo Sư này."),
    ("Samaññāya bhikkhu, paṭiññāya bhikkhu, bhikkhatīti bhikkhu, bhikkhakoti bhikkhu, bhikkhācariyaṃ ajjhupagatoti "
     "bhikkhu, bhinnapaṭadharoti bhikkhu, bhindati pāpake akusale dhammeti bhikkhu, bhinnattā pāpakānaṃ akusalānaṃ "
     "dhammānaṃ bhikkhu, odhiso kilesānaṃ pahānā bhikkhu, anodhiso kilesānaṃ pahānā bhikkhu, sekkho bhikkhu, asekkho "
     "bhikkhu, nevasekkhanāsekkho bhikkhu, aggo bhikkhu, bhadro bhikkhu, maṇḍo bhikkhu, sāro bhikkhu, samaggena "
     "saṅghena ñatticatutthena kammena akuppena ṭhānārahena upasampanno bhikkhu."):
        ("Là tỳ-khưu theo danh xưng, là tỳ-khưu theo sự tự xưng, là tỳ-khưu vì “đi khất thực”, là tỳ-khưu vì là "
         "“người khất thực”, là tỳ-khưu vì “đã chấp nhận đời sống khất thực”, là tỳ-khưu vì “mặc y may từ những "
         "mảnh vải vụn”, là tỳ-khưu vì “phá vỡ các hiện tượng bất thiện xấu ác”, là tỳ-khưu vì đã phá vỡ các hiện "
         "tượng bất thiện xấu ác, là tỳ-khưu do dứt bỏ một phần các phiền não, là tỳ-khưu do dứt bỏ toàn bộ các "
         "phiền não; tỳ-khưu thuộc về người còn đang tu học, tỳ-khưu thuộc về người đã hoàn tất tu học, tỳ-khưu không "
         "thuộc về người còn đang tu học cũng không thuộc về người đã hoàn tất tu học; tỳ-khưu hàng đầu, tỳ-khưu hiền "
         "thiện, tỳ-khưu tinh hoa, tỳ-khưu cốt lõi; tỳ-khưu đã được thọ giới đầy đủ bởi Tăng đoàn hòa hợp, bằng tăng "
         "sự gồm một lời đề nghị và ba lần tuyên bố, không thể bị hủy bỏ, xứng đáng được duy trì."),
    "Sīlaṃ patiṭṭhā ādi caraṇaṃ saṃyamo saṃvaro mokkhaṃ pāmokkhaṃ kusalānaṃ dhammānaṃ samāpattiyā.":
        ("Giới hạnh, nền tảng, khởi đầu, sự thực hành, sự tự chế, sự thu thúc, điều cao nhất, điều đứng đầu để các "
         "hiện tượng thiện xảy ra nơi mình."),
    "Kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo.":
        "Sự không vi phạm bằng thân, sự không vi phạm bằng lời nói, sự không vi phạm bằng thân và lời nói.",
    # ^2-513, ^2-514
    "Atthi ācāro, atthi anācāro.": "Có hạnh kiểm đúng đắn, có hạnh kiểm sai trái.",
    "Kāyiko vītikkamo, vācasiko vītikkamo, kāyikavācasiko vītikkamo":
        "Sự vi phạm bằng thân, sự vi phạm bằng lời nói, sự vi phạm bằng thân và lời nói",
    "Kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo":
        "Sự không vi phạm bằng thân, sự không vi phạm bằng lời nói, sự không vi phạm bằng thân và lời nói",
    "Sabbampi dussīlyaṃ anācāro.": "Mọi sự phạm giới cũng là hạnh kiểm sai trái.",
    "Sabbopi sīlasaṃvaro ācāro.": "Mọi sự thu thúc trong giới hạnh cũng là hạnh kiểm đúng đắn.",
    ("Idhekacco veḷudānena vā pattadānena vā pupphadānena vā phaladānena vā sinānadānena vā dantakaṭṭhadānena vā "
     "cāṭukamyatāya vā muggasūpyatāya [muggasuppatāya (sī.)] vā pāribhaṭayatāya vā jaṅghapesanikena vā "
     "aññataraññatarena vā buddhapaṭikuṭṭhena micchāājīvena jīvikaṃ kappeti"):
        (f"Ở đây, có người nuôi sống bản thân {_neg_gifts(False)}, hoặc bằng sinh kế sai lầm này hay sinh kế sai lầm "
         f"khác bị Đức Phật chê trách"),
    ("Idhekacco na veḷudānena na pattadānena na pupphadānena na phaladānena na sinānadānena na dantakaṭṭhadānena na "
     "cāṭukamyatāya na muggasūpyatāya na pāribhaṭayatāya na jaṅghapesanikena na aññataraññatarena buddhapaṭikuṭṭhena "
     "micchāājīvena jīvikaṃ kappeti"):
        (f"Ở đây, có người nuôi sống bản thân {_neg_gifts(True)}, không bằng sinh kế sai lầm này hay sinh kế sai lầm "
         f"khác bị Đức Phật chê trách"),
    "Atthi gocaro, atthi agocaro.": "Có nơi lui tới thích hợp, có nơi lui tới không thích hợp.",
    ("Idhekacco vesiyāgocaro vā hoti vidhavāgocaro vā thullakumārigocaro vā paṇḍakagocaro vā bhikkhunigocaro vā "
     "pānāgāragocaro vā, saṃsaṭṭho viharati rājūhi rājamahāmattehi titthiyehi titthiyasāvakehi ananulomikena "
     "saṃsaggena; yāni vā pana tāni kulāni assaddhāni appasannāni anopānabhūtāni akkosakaparibhāsakāni "
     "anatthakāmāni ahitakāmāni aphāsukakāmāni ayogakkhemakāmāni bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ upāsikānaṃ, "
     "tathārūpāni kulāni sevati bhajati payirupāsati"): L_AGOCARA,
    ("Idhekacco na vesiyāgocaro hoti na vidhavāgocaro na thullakumārigocaro na paṇḍakagocaro na bhikkhunigocaro na "
     "pānāgāragocaro, asaṃsaṭṭho viharati rājūhi rājamahāmattehi titthiyehi titthiyasāvakehi ananulomikena "
     "saṃsaggena; yāni vā pana tāni kulāni saddhāni pasannāni opānabhūtāni kāsāvapajjotāni isivātapaṭivātāni "
     "atthakāmāni hitakāmāni phāsukakāmāni yogakkhemakāmāni bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ upāsikānaṃ, "
     "tathārūpāni kulāni sevati bhajati payirupāsati"): L_GOCARA,
    # ^2-515, ^2-516
    ("Yāni tāni vajjāni appamattakāni oramattakāni lahusāni lahusammatāni saṃyamakaraṇīyāni saṃvarakaraṇīyāni "
     "cittuppādakaraṇīyāni manasikārapaṭibaddhāni"):
        ("Những lỗi nào nhỏ, nhỏ bé, nhẹ, được xem là nhẹ, cần được xử lý bằng sự tự chế, cần được xử lý bằng sự thu "
         "thúc, cần được xử lý bằng sự khởi tâm, gắn liền với sự chú tâm"),
    ("Iti imesu aṇumattesu vajjesu vajjadassāvī ca hoti bhayadassāvī ca ādīnavadassāvī ca nissaraṇadassāvī ca."):
        ("Như vậy, trong những lỗi nhỏ nhặt này, vị ấy thấy lỗi lầm, thấy sự nguy hiểm, thấy sự tai hại và thấy lối "
         "thoát."),
    ("Catasso sikkhā – bhikkhūnaṃ bhikkhusikkhā, bhikkhunīnaṃ bhikkhunisikkhā, upāsakānaṃ upāsakasikkhā, upāsikānaṃ "
     "upāsikasikkhā."):
        ("Bốn sự tu học – sự tu học của tỳ-khưu dành cho các tỳ-khưu, sự tu học của tỳ-khưu-ni dành cho các tỳ-khưu-ni, "
         "sự tu học của nam cư sĩ dành cho các nam cư sĩ, sự tu học của nữ cư sĩ dành cho các nữ cư sĩ."),
    "Iti imāsu sikkhāsu sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ samādāya vattati.":
        ("Như vậy, vị ấy thọ trì và thực hành những sự tu học này một cách toàn bộ, về mọi mặt, không thiếu sót, không "
         "sót lại gì."),
    # ^2-517
    "Atthi indriyesu guttadvāratā, atthi aguttadvāratā.":
        "Có sự phòng hộ cửa các giác quan, có sự không phòng hộ cửa.",
    "Idhekacco cakkhunā rūpaṃ disvā nimittaggāhī hoti anubyañjanaggāhī.":
        f"Ở đây, có người khi thấy hình sắc bằng mắt thì {GRASP[False]}.",
    "Idhekacco cakkhunā rūpaṃ disvā na nimittaggāhī hoti nānubyañjanaggāhī.":
        f"Ở đây, có người khi thấy hình sắc bằng mắt thì {GRASP[True]}.",
    ("Sotena saddaṃ sutvā…pe… ghānena gandhaṃ ghāyitvā…pe… jivhāya rasaṃ sāyitvā…pe… kāyena phoṭṭhabbaṃ "
     "phusitvā…pe… manasā dhammaṃ viññāya nimittaggāhī hoti anubyañjanaggāhī."): f"{SENSES5} {GRASP[False]}.",
    ("Sotena saddaṃ sutvā…pe… ghānena gandhaṃ ghāyitvā…pe… jivhāya rasaṃ sāyitvā…pe… kāyena phoṭṭhabbaṃ "
     "phusitvā…pe… manasā dhammaṃ viññāya na nimittaggāhī hoti nānubyañjanaggāhī."): f"{SENSES5} {GRASP[True]}.",
    "Yā imesaṃ channaṃ indriyānaṃ agutti agopanā anārakkho asaṃvaro":
        ("Điều mà đối với sáu năng lực này là sự không canh giữ, sự không bảo vệ, sự không che chở, sự không thu "
         "thúc"),
    "Yā imesaṃ channaṃ indriyānaṃ gutti gopanā ārakkho saṃvaro":
        "Điều mà đối với sáu năng lực này là sự canh giữ, sự bảo vệ, sự che chở, sự thu thúc",
    # ^2-518, ^2-519
    "Atthi bhojane mattaññutā, atthi bhojane amattaññutā.":
        "Có sự biết tiết độ trong ăn uống, có sự không biết tiết độ trong ăn uống.",
    "Idhekacco appaṭisaṅkhā ayoniso āhāraṃ āhāreti davāya madāya maṇḍanāya vibhūsanāya.":
        ("Ở đây, có người ăn thức ăn không suy xét, không đúng cách, để vui đùa, để say sưa, để trang điểm, để làm "
         "đẹp."),
    "Yā tattha asantuṭṭhitā amattaññutā appaṭisaṅkhā bhojane":
        "Điều mà ở đây là sự không biết đủ, sự không biết tiết độ, sự không suy xét trong ăn uống",
    "Yā tattha santuṭṭhitā mattaññutā paṭisaṅkhā bhojane":
        "Điều mà ở đây là sự biết đủ, sự biết tiết độ, sự suy xét trong ăn uống",
    ('Idhekacco paṭisaṅkhā yoniso āhāraṃ āhāreti – "neva davāya na madāya na maṇḍanāya na vibhūsanāya, yāvadeva '
     "imassa kāyassa ṭhitiyā yāpanāya vihiṃsūparatiyā brahmacariyānuggahāya, iti purāṇañca vedanaṃ paṭihaṅkhāmi "
     'navañca vedanaṃ na uppādessāmi yātrā ca me bhavissati anavajjatā ca phāsu vihāro cā"ti.'):
        ("Ở đây, có người suy xét, ăn thức ăn đúng cách – “Không phải để vui đùa, không phải để say sưa, không phải để "
         "trang điểm, không phải để làm đẹp, mà chỉ để thân này được duy trì, được kéo dài, để chấm dứt sự bức bách, để "
         "hỗ trợ đời sống tu hành trong sạch; như vậy, tôi sẽ đẩy lui cảm giác cũ và không làm sinh khởi cảm giác mới, "
         "và tôi sẽ có sự duy trì mạng sống, sự không có lỗi và sự an trú thoải mái”."),
    "Kathañca bhikkhu pubbarattāpararattaṃ jāgariyānuyogamanuyutto hoti?": f"Và vị tỳ-khưu {WAKE} như thế nào?",
    ("Idha bhikkhu divasaṃ caṅkamena nisajjāya āvaraṇīyehi dhammehi cittaṃ parisodheti, rattiyā paṭhamayāmaṃ "
     "caṅkamena nisajjāya āvaraṇīyehi dhammehi cittaṃ parisodheti, rattiyā majjhimayāmaṃ dakkhiṇena passena "
     "sīhaseyyaṃ kappeti pāde pādaṃ [pādena pādaṃ (syā.)] accādhāya sato sampajāno uṭṭhānasaññaṃ manasikaritvā, "
     "rattiyā pacchimayāmaṃ paccuṭṭhāya caṅkamena nisajjāya āvaraṇīyehi dhammehi cittaṃ parisodheti."):
        ("Ở đây, ban ngày, bằng việc đi kinh hành và ngồi, vị tỳ-khưu làm trong sạch hoàn toàn tâm khỏi các hiện tượng "
         "gây chướng ngại; vào canh đầu của đêm, bằng việc đi kinh hành và ngồi, vị ấy làm trong sạch hoàn toàn tâm "
         "khỏi các hiện tượng gây chướng ngại; vào canh giữa của đêm, vị ấy nằm nghiêng bên phải theo tư thế sư tử, "
         f"đặt chân này lên chân kia {S.reading('Syā.', 'pādena pādaṃ')}, {SATO_SAMP}, sau khi chú tâm đến tri giác "
         "về việc thức dậy; vào canh cuối của đêm, sau khi thức dậy, bằng việc đi kinh hành và ngồi, vị ấy làm trong "
         "sạch hoàn toàn tâm khỏi các hiện tượng gây chướng ngại."),
    "Evaṃ bhikkhu pubbarattāpararattaṃ jāgariyānuyogamanuyutto.": f"Như vậy, vị tỳ-khưu {WAKE}.",
    # ^2-522 … ^2-525
    ("Satta bojjhaṅgā – satisambojjhaṅgo, dhammavicayasambojjhaṅgo, vīriyasambojjhaṅgo, pītisambojjhaṅgo, "
     "passaddhisambojjhaṅgo, samādhisambojjhaṅgo, upekkhāsambojjhaṅgo."): BJ7_FULL,
    "Iti te bodhipakkhike dhamme āsevati bhāveti bahulīkaroti.":
        f"Như vậy, vị ấy thực hành, tu tập, làm đi làm lại những {BODHI[4:]} ấy.",
    ("Kathañca bhikkhu abhikkante paṭikkante sampajānakārī hoti, ālokite vilokite sampajānakārī hoti, samiñjite "
     "pasārite sampajānakārī hoti, saṅghāṭipattacīvaradhāraṇe sampajānakārī hoti, asite pīte khāyite sāyite "
     "sampajānakārī hoti, uccārapassāvakamme sampajānakārī hoti; gate ṭhite nisinne sutte jāgarite bhāsite "
     "tuṇhībhāve sampajānakārī hoti?"): f"Và vị tỳ-khưu {SAMPAJ_Q} như thế nào?",
    ("Idha bhikkhu sato sampajāno abhikkamati, sato sampajāno paṭikkamati, sato sampajāno āloketi, sato sampajāno "
     "viloketi, sato sampajāno samiñjeti, sato sampajāno pasāreti, sato sampajānakārī hoti, "
     "saṅghāṭipattacīvaradhāraṇe sato sampajānakārī hoti, asite pīte khāyite sāyite sato sampajānakārī hoti, "
     "uccārapassāvakamme sato sampajānakārī hoti, gate ṭhite nisinne sutte jāgarite bhāsite tuṇhībhāve sato "
     "sampajānakārī hotīti."): f"Ở đây, {sato_moves(True)}.",
    ("Evaṃ bhikkhu sato sampajāno abhikkamati, sato sampajāno paṭikkamati, sato sampajāno āloketi, sato sampajāno "
     "viloketi, sato sampajāno samiñjeti, sato sampajāno pasāreti, sato sampajānakārī hoti, "
     "saṅghāṭipattacīvaradhāraṇe sato sampajānakārī hoti, asite pīte khāyite sāyite sato sampajānakārī hoti, "
     "uccārapassāvakamme sato sampajānakārī hoti, gate ṭhite nisinne sutte jāgarite bhāsite tuṇhībhāve "
     "sampajānakārī hoti."): f"Như vậy, {sato_moves(False)}.",
    # ^2-526 … ^2-536
    "Santike cepi senāsanaṃ hoti, tañca anākiṇṇaṃ gahaṭṭhehi pabbajitehi.":
        "Dù chỗ ở ở gần, nhưng nơi ấy không bị người tại gia và người xuất gia chen chúc.",
    "Dūre cepi senāsanaṃ hoti, tañca anākiṇṇaṃ gahaṭṭhehi pabbajitehi.":
        "Dù chỗ ở ở xa, nhưng nơi ấy không bị người tại gia và người xuất gia chen chúc.",
    "Tena taṃ vivittaṃ.": "Vì thế, chỗ ấy thanh vắng.",
    "Tena taṃ appasaddaṃ.": "Vì thế, chỗ ấy ít tiếng động.",
    ("Mañcopi senāsanaṃ, pīṭhampi senāsanaṃ, bhisipi senāsanaṃ, bibbohanampi [bimbohanampi (sī. syā.)] senāsanaṃ, "
     "vihāropi senāsanaṃ, aḍḍhayogopi senāsanaṃ, pāsādopi senāsanaṃ, aṭṭopi senāsanaṃ, māḷopi senāsanaṃ, leṇampi "
     "senāsanaṃ, guhāpi senāsanaṃ, rukkhamūlampi senāsanaṃ, veḷugumbopi senāsanaṃ."):
        ", ".join(f"{x} cũng là chỗ ở" for x in (
            "Giường", "ghế", "nệm", f"gối {S.spell('Sī., Syā.', 'bimbohanampi')}", "tịnh xá", "nhà một mái",
            "lâu đài", "tháp canh", "nhà mái tròn", "động đá", "hang", "gốc cây", "bụi tre")) + ".",
    "Yattha vā pana bhikkhū paṭikkamanti sabbametaṃ senāsanaṃ.":
        "Hoặc bất cứ nơi nào các tỳ-khưu lui về, tất cả nơi ấy đều là chỗ ở.",
    "Imaṃ vivittaṃ senāsanaṃ bhajati sambhajati sevati nisevati saṃsevati.":
        ("Vị ấy lui tới, lui tới thường xuyên, gần gũi, gần gũi thường xuyên, gần gũi trọn vẹn chỗ ở thanh vắng "
         "này."),
    "Nikkhamitvā bahi indakhīlā sabbametaṃ araññaṃ.":
        "Sau khi đi ra ngoài cột trụ ở cổng làng, tất cả nơi ấy đều là rừng.",
    "Rukkhamūlaṃyeva rukkhamūlaṃ.": "Chính gốc cây là gốc cây.", "Pabbatoyeva pabbato.": "Chính núi là núi.",
    "Kandarāyeva kandarā.": "Chính khe núi là khe núi.", "Giriguhāyeva giriguhā.": "Chính hang núi là hang núi.",
    "Susānaṃyeva susānaṃ.": "Chính bãi tha ma là bãi tha ma.",
    "Abbhokāsoyeva abbhokāso.": "Chính khoảng trời trống là khoảng trời trống.",
    "Palālapuñjoyeva palālapuñjo.": "Chính đống rơm là đống rơm.",
    "Dūrānametaṃ senāsanānaṃ adhivacanaṃ.": "Đây là tên gọi của những chỗ ở xa xôi.",
    "Vanasaṇḍānametaṃ senāsanānaṃ adhivacanaṃ.": "Đây là tên gọi của những chỗ ở giữa lùm rừng.",
    "Bhīsanakānametaṃ [bhiṃsanakānametaṃ (sī. syā.)] senāsanānaṃ adhivacanaṃ.":
        f"Đây là tên gọi của những chỗ ở đáng sợ {S.spell('Sī., Syā.', 'bhiṃsanakānametaṃ')}.",
    "Salomahaṃsānametaṃ senāsanānaṃ adhivacanaṃ.": "Đây là tên gọi của những chỗ ở làm sởn tóc gáy.",
    "Pariyantānametaṃ senāsanānaṃ adhivacanaṃ.": "Đây là tên gọi của những chỗ ở ở vùng biên.",
    "Na manussūpacārānametaṃ senāsanānaṃ adhivacanaṃ.": "Đây là tên gọi của những chỗ ở không có người qua lại.",
    "Durabhisambhavānametaṃ senāsanānaṃ adhivacanaṃ.": "Đây là tên gọi của những chỗ ở khó chịu đựng.",
    "Yadeva taṃ appasaddaṃ tadeva taṃ appanigghosaṃ.": "Chính nơi ít tiếng động ấy là nơi ít ồn ào.",
    "Yadeva taṃ appanigghosaṃ tadeva taṃ vijanavātaṃ.": "Chính nơi ít ồn ào ấy là nơi vắng hơi người.",
    "Yadeva taṃ vijanavātaṃ tadeva taṃ manussarāhasseyyakaṃ.":
        "Chính nơi vắng hơi người ấy là nơi kín đáo đối với con người.",
    "Yadeva taṃ manussarāhasseyyakaṃ tadeva taṃ paṭisallānasāruppaṃ.":
        "Chính nơi kín đáo đối với con người ấy là nơi thích hợp cho sự độc cư.",
    "Araññagato vā hoti rukkhamūlagato vā suññāgāragato vā.":
        "Vị ấy đi đến rừng, hoặc đi đến gốc cây, hoặc đi đến ngôi nhà trống.",
    "Nisinno hoti pallaṅkaṃ ābhujitvā.": "Vị ấy đã ngồi, xếp chân kiết già.",
    "Ujuko hoti kāyo ṭhito paṇihito.": "Thân ngay thẳng, được giữ vững, được đặt đúng cách.",
    "Ayaṃ sati upaṭṭhitā hoti supaṭṭhitā nāsikagge vā mukhanimitte vā.":
        "Sự tỉnh thức này được thiết lập, được thiết lập vững vàng nơi chóp mũi hoặc nơi vùng miệng.",
}
misfit("paṇidhāya (^2-508, ^2-536 «ujuṃ kāyaṃ paṇidhāya»): the termbase sense 'aspiring to' «với ước nguyện» does not "
       "fit 'having set (the body)'; «đặt thân ngay thẳng» (paṇihito «được đặt đúng cách»)")
misfit("Yadeva (^2-533 «yadeva taṃ appasaddaṃ tadeva taṃ appanigghosaṃ»): the termbase sense 'because' «bởi vì» does "
       "not fit the correlative 'that very … is'; «Chính nơi … ấy là nơi …»")
misfit("mukhanimitte (^2-537): no entry; built from mukha «miệng», nimitte «vùng»: «nơi vùng miệng» (the "
       "commentary: the upper lip)")
ORD = {"paṭhamaṃ": "thứ nhất", "dutiyaṃ": "thứ hai", "tatiyaṃ": "thứ ba", "catutthaṃ": "thứ tư"}
GANANA_V = " " + S.spell("Syā.", "gaṇanānupubbato")[:-1] + ", cũng vậy ở các chỗ sau]"   # (syā.) evamuparipi
for _p, _v in ORD.items():
    SENT12[f"Gaṇanānupubbatā {_p}."] = f"{cap(_v)} theo thứ tự đếm."
    SENT12[f"Idaṃ {_p} samāpajjatīti {_p}."] = f"Là {_v} vì đây là điều được chứng nhập {_v}."
SENT12["Gaṇanānupubbatā [gaṇanānupubbato (syā.) evamuparipi] paṭhamaṃ."] = f"Thứ nhất theo thứ tự đếm{GANANA_V}."
SENT12["Gaṇanānupubbatā catutthaṃ, idaṃ catutthaṃ samāpajjatīti catutthaṃ."] = (
    "Thứ tư theo thứ tự đếm, là thứ tư vì đây là điều được chứng nhập thứ tư.")
misfit("Idaṃ paṭhamaṃ samāpajjatīti paṭhamaṃ (^2-568 …): samāpajjati «chứng nhập» (termbase samāpajjatīti); "
       "«Là thứ nhất vì đây là điều được chứng nhập thứ nhất.»")
FACTORS = {"vitakko": "sự hướng tâm", "vicāro": "sự duy trì tâm", "pīti": "sự hân hoan", "sukhaṃ": "hạnh phúc",
           "cittassekaggatā": "sự nhất tâm", "upekkhā": "sự bình thản", "sati": "sự tỉnh thức",
           "sampajaññaṃ": "sự hiểu biết rõ ràng", "sampasādo": "sự trong sáng", "pītisukhaṃ": "sự hân hoan và hạnh phúc"}
# the jhāna factors (pi-1 ^1-83 «Sự hướng tâm, sự duy trì tâm, sự hân hoan, hạnh phúc, sự nhất tâm»)


def factors(p):
    """«vitakko, vicāro, pīti, sukhaṃ, cittassekaggatā» (commas optional) -> Vietnamese, lower case"""
    return ", ".join(FACTORS[w] for w in re.split(r",? ", p))


assert cap(factors("vitakko, vicāro, pīti, sukhaṃ, cittassekaggatā")) == pi1(
    "Sự hướng tâm, sự duy trì tâm, sự hân hoan, hạnh phúc, sự nhất tâm")
SENT12.update({
    # ^2-537 … ^2-560
    "Yo byāpādo so padoso, yo padoso so byāpādo.":
        "Ác ý chính là sự sân hận dữ dội, sự sân hận dữ dội chính là ác ý.",
    "Atthi byāpādo, atthi padoso.": "Có ác ý, có sự sân hận dữ dội.",
    "Atthi thinaṃ [thīnaṃ (sī. syā.)], atthi middhaṃ.":
        f"Có sự uể oải {S.spell('Sī., Syā.', 'thīnaṃ')}, có sự đờ đẫn.",
    "Atthi thinaṃ, atthi middhaṃ.": "Có sự uể oải, có sự đờ đẫn.",
    "Atthi uddhaccaṃ, atthi kukkuccaṃ.": "Có sự xao động, có sự hối tiếc.",
    "Atthi vitakko, atthi vicāro.": "Có sự hướng tâm, có sự duy trì tâm.",
    "Atthi pīti, atthi sukhaṃ.": "Có sự hân hoan, có hạnh phúc.",
    "Atthi sukhaṃ, atthi dukkhaṃ.": "Có sự dễ chịu, có sự khó chịu.",
    "Atthi somanassaṃ, atthi domanassaṃ.": "Có niềm vui, có nỗi buồn.",
    "Idaṃ cittaṃ vigatābhijjhaṃ hoti.": "Tâm này đã lìa sự thèm muốn.",
    "Idaṃ cittaṃ abyāpannaṃ hoti.": "Tâm này không có ác ý.",
    "Idaṃ cittaṃ ajjhattaṃ santaṃ hoti samitaṃ vūpasantaṃ.":
        "Tâm này đã lắng yên, đã được làm lắng dịu, đã lắng dịu hoàn toàn ở nơi bản thân.",
    "Ayaṃ saññā ālokā hoti vivaṭā parisuddhā pariyodātā.":
        "Tri giác này sáng sủa, được khai mở, trong sạch, sáng tỏ.",
    ("Akappiye kappiyasaññitā, kappiye akappiyasaññitā, avajje vajjasaññitā, vajje avajjasaññitā, yaṃ evarūpaṃ "
     "kukkuccaṃ kukkuccāyanā kukkuccāyitattaṃ cetaso vippaṭisāro manovilekhā"):
        f"{KUKKUCCA_PRE}, điều mà thuộc loại như vậy là {KUKKUCCA_LIST}",
    "Imaṃ vicikicchaṃ tiṇṇo hoti uttiṇṇo nittiṇṇo pāraṅgato pāramanuppatto.":
        ("Vị ấy đã vượt qua sự hoài nghi này, đã vượt lên, đã vượt thoát, đã đi đến bờ bên kia, đã đạt đến bờ bên "
         "kia."),
    ("Imāya vicikicchāya kusalesu dhammesu na kaṅkhati na vicikicchati akathaṃkathī hoti nikkathaṃkathī "
     "vikathaṃkatho."):
        ("Với sự hoài nghi này, vị ấy không nghi ngờ, không hoài nghi đối với các hiện tượng thiện; vị ấy không còn "
         "băn khoăn, hết băn khoăn, lìa băn khoăn."),
    # ^2-561 … ^2-567
    "Ime pañca nīvaraṇā cittassa upakkilesā.": "Năm chướng ngại này là những thứ làm vẩn đục tâm.",
    "Imehi pañcahi nīvaraṇehi anuppannā ceva paññā na uppajjati uppannā ca paññā nirujjhati.":
        "Do năm chướng ngại này, trí tuệ chưa sinh khởi không sinh khởi và trí tuệ đã sinh khởi thì chấm dứt.",
    "Chando kāmo, rāgo kāmo, chandarāgo kāmo, saṅkappo kāmo, rāgo kāmo, saṅkapparāgo kāmo":
        ("Ý muốn là dục lạc, sự tham đắm là dục lạc, sự tham đắm do ý muốn là dục lạc, tư duy là dục lạc, sự tham đắm "
         "là dục lạc, sự tham đắm do tư duy là dục lạc"),
    "Kāmacchando, byāpādo, thinaṃ, middhaṃ, uddhaccaṃ, kukkuccaṃ, vicikicchā":
        "Ý muốn dục lạc, ác ý, sự uể oải, sự đờ đẫn, sự xao động, sự hối tiếc, sự hoài nghi",
    "Iti imehi ca kāmehi imehi ca akusalehi dhammehi vivitto hoti.":
        "Như vậy, vị ấy tách khỏi các dục lạc này và các hiện tượng bất thiện này.",
    "Vitakko, vicāro, pīti, sukhaṃ, cittassekaggatā – te imasmiṃ viveke jātā honti sañjātā nibbattā abhinibbattā "
    "pātubhūtā.": f"{cap(factors('vitakko vicāro pīti sukhaṃ cittassekaggatā'))} – chúng {JATA} trong sự tách biệt này.",
    "Sampasādo pītisukhaṃ – te imasmiṃ samādhimhi jātā honti sañjātā nibbattā abhinibbattā pātubhūtā.":
        f"{cap(factors('sampasādo pītisukhaṃ'))} – chúng {JATA} trong định tâm này.",
    "Idaṃ sukhaṃ imāya pītiyā sahagataṃ hoti sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ.":
        "Hạnh phúc này đi kèm, cùng sinh, hòa lẫn, gắn liền với sự hân hoan này.",
    # ^2-569 … ^2-622
    "Vitakko, vicāro, pīti, sukhaṃ, cittassekaggatā.": f"{cap(factors('vitakko vicāro pīti sukhaṃ cittassekaggatā'))}.",
    "Sampasādo, pītisukhaṃ, cittassekaggatā.": f"{cap(factors('sampasādo pītisukhaṃ cittassekaggatā'))}.",
    "Upekkhā, sati, sampajaññaṃ, sukhaṃ, cittassekaggatā.":
        f"{cap(factors('upekkhā sati sampajaññaṃ sukhaṃ cittassekaggatā'))}.",
    "Upekkhā, sati, cittassekaggatā.": f"{cap(factors('upekkhā sati cittassekaggatā'))}.",
    "Yaṃ ajjhattaṃ paccattaṃ.": "Điều ở nơi bản thân, riêng từng người.",
    "Saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho": "Khối tri giác, khối tạo tác, khối thức",
    "Idaṃ sukhaṃ iminā kāyena paṭisaṃvedeti.": "Vị ấy cảm nhận hạnh phúc này bằng thân này.",
    "Ariyā vuccanti buddhā ca buddhasāvakā ca.": "Các bậc thánh được gọi là các Đức Phật và các đệ tử của Đức Phật.",
    "Te imaṃ ācikkhanti desenti paññapenti [paññāpenti (sī. syā.)] paṭṭhapenti vivaranti vibhajanti uttāniṃ karonti "
    "pakāsenti.": (f"Các vị ấy mô tả, thuyết giảng, trình bày {S.spell('Sī., Syā.', 'paññāpenti')}, xác lập, khai mở, "
                   f"phân tích, làm sáng tỏ, công bố điều này."),
    ("Iti imāya ca upekkhāya imāya ca satiyā iminā ca sukhena samannāgato iriyati vattati pāleti yapeti yāpeti carati "
     "viharati."):
        f"Như vậy, được trang bị sự bình thản này, sự tỉnh thức này và hạnh phúc này, {low(VIHARATI_J)}",
    "Ayaṃ sati imāya upekkhāya vivaṭā hoti parisuddhā pariyodātā.":
        "Sự tỉnh thức này nhờ sự bình thản này mà được khai mở, trong sạch, sáng tỏ.",
    ("Rūpāvacarasamāpattiṃ samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā saññā sañjānanā "
     "sañjānitattaṃ"): f"{cap(SANNA3)} {SAMAPANNA.format(x='thành tựu thiền thuộc cõi hình sắc')}",
    "Imā rūpasaññāyo atikkanto hoti vītikkanto samatikkanto.":
        f"Vị ấy {OVERCOME} các tri giác về hình sắc này.",
    "Rūpasaññā saddasaññā…pe… phoṭṭhabbasaññā": "Tri giác về hình sắc, tri giác về âm thanh… tri giác về vật xúc chạm",
    ("Asamāpannassa manodhātu samaṅgissa vā manoviññāṇadhātu samaṅgissa vā saññā sañjānanā sañjānitattaṃ"):
        f"{cap(SANNA3)} của người chưa chứng nhập, là người có được yếu tố ý hoặc người có được yếu tố ý thức",
    "Imā nānattasaññāyo na manasi karoti.": "Vị ấy không chú tâm đến các tri giác về sự đa dạng này.",
    "Tasmiṃ ākāse cittaṃ ṭhapeti saṇṭhapeti anantaṃ pharati.":
        "Vị ấy đặt tâm, đặt tâm vững chắc vào không gian ấy, lan tỏa khắp vô tận.",
    "Taṃyeva ākāsaṃ viññāṇena phuṭṭhaṃ manasi karoti anantaṃ pharati.":
        "Vị ấy chú tâm đến chính không gian ấy được thức chạm đến, lan tỏa khắp vô tận.",
    'Taṃyeva viññāṇaṃ bhāveti vibhāveti antarabhāveti, "natthi kiñcī"ti passati.':
        (f"Vị ấy làm cho chính thức ấy không còn hiện hữu, làm cho tan biến, làm cho biến mất, thấy rằng "
         f"“{THOUGHT['ākiñcañña']}”."),
    "Taṃyeva ākiñcaññāyatanaṃ santato manasi karoti saṅkhārāvasesasamāpattiṃ bhāveti.":
        (f"Vị ấy chú tâm đến chính {AY_INF['ākiñcañña']} như là điều an tịnh, tu tập thành tựu thiền còn sót lại các "
         f"sự tạo tác."),
})
misfit("bhāveti (^2-615 «taṃyeva viññāṇaṃ bhāveti vibhāveti antarabhāveti»): the termbase sense 'develops' «tu tập» "
       "does not fit 'makes non-existent' (the commentary's abhāveti); «làm cho … không còn hiện hữu»; vibhāveti «làm "
       "cho tan biến» (termbase), antarabhāveti: no entry, «làm cho biến mất»")
misfit("saṅkhārāvasesasamāpattiṃ (^2-619): termbase «sự chứng đạt còn sót lại các sự tạo tác»; samāpatti follows the "
       "user decision «thành tựu thiền»: «thành tựu thiền còn sót lại các sự tạo tác»")
misfit("Rūpāvacarasamāpattiṃ (^2-602): samāpatti «thành tựu thiền» (user decision): «thành tựu thiền thuộc cõi hình "
       "sắc»")
BODY12 = {  # Pāli after «Yo / Yā / Yaṃ» -> Vietnamese (after «Điều mà là»)
    "sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammusanatā sati satindriyaṃ satibalaṃ sammāsati":
        SATI_FULL,
    "sati anussati paṭissati…pe… sammāsati": SATI_PE3,
    "sati anussati…pe… sammāsati": SATI_PE,
    ("paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
     "nepuññaṃ vebhabyā cintā upaparikkhā bhūrīmedhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā paññindriyaṃ "
     "paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ amoho dhammavicayo "
     "sammādiṭṭhi"): PANNA_FULL,
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": PANNA_SHORT,
    "cetasiko vīriyārambho…pe… sammāvāyāmo": VIRIYA_PE,
    "rāgo sārāgo…pe… cittassa sārāgo": RAGA_PE,
    "cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu": CITTA_PE,
    ("cittassa āghāto paṭighāto paṭighaṃ paṭivirodho kopo pakopo sampakopo doso padoso sampadoso cittassa byāpatti "
     "manopadoso kodho kujjhanā kujjhitattaṃ doso dussanā dussitattaṃ [dūsanā dūsitattaṃ (syā.)] byāpatti byāpajjanā "
     "byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa"): DOSA_V,
    "cittassa āghāto…pe… caṇḍikkaṃ asuropo anattamanatā cittassa": DOSA_PE,
    ("cittassa akalyatā akammaññatā olīyanā sallīyanā līnaṃ līyanā līyitattaṃ thinaṃ thiyanā thiyitattaṃ [thīyanā "
     "thīyitattaṃ (sī. syā.)] cittassa"): THINA_V,
    ("kāyassa akalyatā akammaññatā onāho pariyonāho antosamorodho middhaṃ suppaṃ pacalāyikā suppaṃ suppanā "
     "suppitattaṃ"): MIDDHA,
    "saññā sañjānanā sañjānitattaṃ": SANNA3,
    "cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": UDDHACCA,
    ("kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvidhāpatho saṃsayo anekaṃsaggāho āsappanā "
     "parisappanā apariyogāhaṇā chambhitattaṃ cittassa manovilekho"): VICIKICCHA,
    "kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ chambhitattaṃ cittassa manovilekho": VICIKICCHA_SHORT,
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo": VITAKKA_FULL12,
    "takko vitakko…pe… sammāsaṅkappo": VITAKKA_PE,
    "cāro vicāro anuvicāro upavicāro cittassa anusandhanatā anupekkhanatā": VICARA,
    "cāro anucāro vicāro anuvicāro upavicāro cittassa anusandhanatā anupekkhanatā": VICARA_ANU,
    "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa": PITI_LIST,
    ("cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā "
     "vedanā"): FEEL["somanassa"],
    "kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā":
        FEEL["sukha"],
    ("kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā "
     "vedanā"): FEEL["dukkha"],
    ("cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā "
     "vedanā"): FEEL["domanassa"],
    ("cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā "
     "vedanā"): FEEL["upekkhā"],
    "upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa": UPEKKHA_LIST,
    "ākāso ākāsagataṃ aghaṃ aghagataṃ vivaro vivaragataṃ asamphuṭṭhaṃ catūhi mahābhūtehi": low(ASPACE),
    "saddhā saddahanā okappanā abhippasādo": SADDHA4,
    "cittassa ṭhiti…pe… sammāsamādhi": f"{SAMADHI_ST}… {PF['sammāsamādhi']}",
}
slip("^2-557 «dvidhāpatho … apariyogāhaṇā chambhitattaṃ» (pi-1 ^1-1008 «dvedhāpatho … apariyogāhanā "
     "thambhitattaṃ»): spelling variants of the same words; pi-1 Vietnamese kept")
NAMES12 = {  # Pāli (as asked or quoted) -> Vietnamese
    "anācāro": "hạnh kiểm sai trái", "ācāro": "hạnh kiểm đúng đắn", "agocaro": "nơi lui tới không thích hợp",
    "gocaro": "nơi lui tới thích hợp", "aṇumattā vajjā": "những lỗi nhỏ nhặt", "sikkhā": "sự tu học",
    "sikkhāyo": "các sự tu học", "indriyesu aguttadvāratā": "sự không phòng hộ cửa các giác quan",
    "indriyesu guttadvāratā": "sự phòng hộ cửa các giác quan",
    "bhojane amattaññutā": "sự không biết tiết độ trong ăn uống", "bhojane mattaññutā": "sự biết tiết độ trong ăn uống",
    "bodhipakkhikā dhammā": BODHI, "sati": "sự tỉnh thức", "sampajaññaṃ": "sự hiểu biết rõ ràng",
    "abhijjhā": "sự thèm muốn", "loko": "thế gian", "cittaṃ": "tâm", "byāpādo": "ác ý",
    "padoso": "sự sân hận dữ dội", "thinaṃ": "sự uể oải", "middhaṃ": "sự đờ đẫn", "saññā": "tri giác",
    "uddhaccaṃ": "sự xao động", "kukkuccaṃ": "sự hối tiếc", "vicikicchā": "sự hoài nghi", "kāmā": "các dục lạc",
    "akusalā dhammā": "các hiện tượng bất thiện", "vitakko": "sự hướng tâm", "vicāro": "sự duy trì tâm",
    "pīti": "sự hân hoan", "sukhaṃ": "hạnh phúc", "dukkhaṃ": "sự khó chịu", "somanassaṃ": "niềm vui",
    "domanassaṃ": "nỗi buồn", "upekkhā": "sự bình thản", "kāyo": "thân", "ariyā": "các bậc thánh",
    "rūpasaññā": "tri giác về hình sắc", "rūpasaññāyo": "các tri giác về hình sắc",
    "paṭighasaññā": "tri giác về sự va chạm", "paṭighasaññāyo": "các tri giác về sự va chạm",
    "nānattasaññā": "tri giác về sự đa dạng", "nānattasaññāyo": "các tri giác về sự đa dạng", "ākāso": "không gian",
    "paṭhamaṃ jhānaṃ": "tầng thiền thứ nhất", "dutiyaṃ jhānaṃ": "tầng thiền thứ hai",
    "tatiyaṃ jhānaṃ": "tầng thiền thứ ba", "catutthaṃ jhānaṃ": "tầng thiền thứ tư",
    "pañcamaṃ jhānaṃ": "tầng thiền thứ năm",
}
SUKHA_BODILY = {"2-594"}          # sukhaṃ = bodily pleasure there (termbase: «dễ chịu» in the feeling definitions)
SANTA_SUBJ = {  # subject of «… santā hoti / honti samitā … byantīkatā.»
    "Ayaṃ abhijjhā imamhi loke": "Sự thèm muốn này trong thế gian này",
    "Iti ayañca byāpādo ayañca padoso": "Như vậy, ác ý này và sự sân hận dữ dội này",
    "Iti idañca thinaṃ idañca middhaṃ": "Như vậy, sự uể oải này và sự đờ đẫn này",
    "Iti idañca uddhaccaṃ idañca kukkuccaṃ": "Như vậy, sự xao động này và sự hối tiếc này",
    "Ayaṃ vicikicchā": "Sự hoài nghi này", "Ime pañca nīvaraṇā": "Năm chướng ngại này",
    "Iti ayañca vitakko ayañca vicāro": "Như vậy, sự hướng tâm này và sự duy trì tâm này",
    "Ayaṃ pīti": "Sự hân hoan này",
    "Iti idañca sukhaṃ idañca dukkhaṃ": "Như vậy, sự dễ chịu này và sự khó chịu này",
    "Iti idañca somanassaṃ idañca domanassaṃ pubbeva": "Như vậy, niềm vui này và nỗi buồn này từ trước",
    "Imā paṭighasaññāyo": "Các tri giác về sự va chạm này",
}
CLEANSE_OBJ = {"imāya abhijjhāya": "sự thèm muốn này", "imamhā byāpādapadosā": "ác ý và sự sân hận dữ dội này",
               "imamhā thinamiddhā": "sự uể oải và đờ đẫn này", "imamhā uddhaccakukkuccā": "sự xao động và hối tiếc này",
               "imāya vicikicchāya": "sự hoài nghi này"}
UPETO_OBJ = {"Iminā pātimokkhasaṃvarena": f"{P_SAMVARA} này",
             "Iti iminā ca ācārena iminā ca gocarena": "hạnh kiểm đúng đắn này và nơi lui tới thích hợp này",
             "Imāya indriyesu guttadvāratāya": "sự phòng hộ cửa các giác quan này",
             "Imāya bhojane mattaññutāya": "sự biết tiết độ trong ăn uống này",
             "Iti imāya ca satiyā iminā ca sampajaññena": "sự tỉnh thức này và sự hiểu biết rõ ràng này",
             "Iti iminā ca vitakkena iminā ca vicārena": "sự hướng tâm này và sự duy trì tâm này",
             "Imāya upekkhāya": "sự bình thản này"}
GIVEN_SUBJ = {"thinamiddhassa": "sự uể oải và đờ đẫn", "uddhaccakukkuccassa": "sự xao động và hối tiếc"}
GEN = {"paṭhamassa jhānassa": "tầng thiền thứ nhất", "dutiyassa jhānassa": "tầng thiền thứ hai",
       "tatiyassa jhānassa": "tầng thiền thứ ba", "catutthassa jhānassa": "tầng thiền thứ tư",
       "ākāsānañcāyatanassa": AY_INF["ākāsa"], "viññāṇañcāyatanassa": AY_INF["viññāṇa"],
       "ākiñcaññāyatanassa": AY_INF["ākiñcañña"], "nevasaññānāsaññāyatanassa": AY_INF["nevasaññā"]}
ACCAY = {"ākāsānañcāyatanaṃ": AY_INF["ākāsa"], "viññāṇañcāyatanaṃ": AY_INF["viññāṇa"],
         "ākiñcaññāyatanaṃ": AY_INF["ākiñcañña"], "nevasaññānāsaññāyatanaṃ": AY_INF["nevasaññā"]}
NOTE_619 = ("[đoạn văn này không có trong ma trận, nhưng ở phần giải thích thì có trong mọi bản]")
# [ayaṃ pāṭho mātikāyaṃ natthi, niddese pana sabbapotthakesu dissati] (editorial note, translated)
TOPIC_RX = re.compile(r'^"(.+?)"(n?)ti(?:\.|,)?(?: (.+))?$')          # "X"ti … / "X"nti. (quoted topic)
TOPIC0_RX = re.compile(r'^([^"\s]+?)ti\.$')                              # Saṃvaroti. / Saṃvutoti. (no quotes)
SENT12["Pañcupādānakkhandhā loko"] = f"{cap(FIVE_UPA)} là thế gian"   # Pañcupādānakkhandhā loko – ayaṃ vuccati …
Q12_RX = re.compile(r"^Tattha katam(?:o|ā|aṃ|e) (.+?)(\?|…pe… (?:ayaṃ|idaṃ) vuccati \"(.+?)\"\.)$")
A12_RX = re.compile(r'^(.*) – (ayaṃ|idaṃ|ime|imā) (vuccati|vuccanti) ("?)(.+?)"?(ti)?\.$')


def name12(n, sid):
    if n == "sukhaṃ" and sid in SUKHA_BODILY:
        return "sự dễ chịu"
    return NAMES12[n]


def body12(b, sid):
    if b in SENT12:
        return SENT12[b]
    m = re.match(r"^(Yo|Yā|Yaṃ) (.*)$", b)
    assert m, (sid, b)
    return f"{WHICH} {BODY12[m.group(2)]}"


def sentence12(s, sid):
    """one Pāli sentence of the ch. 12 Suttanta -> (Vietnamese, topic flag: the next sentence starts in lower case)"""
    if s in SENT12:
        return SENT12[s], False
    if s in CHANGES:
        return CHANGES[s], False
    if s.startswith(L508_JHANA_P):
        return L508_JHANA, False
    m = re.match(r'^"Viharatī"ti ?…pe… tena vuccati "viharatī"ti\.$', s)
    if m:
        kind, v, _ = topic_vi("viharatī", sid)
        return f"{K79.topic(kind, v)[:-1]}… {low(TENA)} “{v}”.", False
    m = TOPIC_RX.match(s)
    if m:
        t, n, rest = m.groups()
        kind, v, _ = topic_vi(topic_key(t, n), sid)
        tv = K79.topic(kind, v)
        if rest is None:
            return tv, True
        r, _ = sentence12(cap(rest), sid)
        return f"{tv} {low(r)}", False
    m = re.match(r'^Tena vuccati "(.+?)"(n?)ti( \[ayaṃ pāṭho mātikāyaṃ natthi, niddese pana sabbapotthakesu '
                 r'dissati\])?\.$', s)
    if m:
        kind, v, _ = topic_vi(topic_key(m.group(1), m.group(2)), sid)
        return f"{TENA} “{v}”{' ' + NOTE_619 if m.group(3) else ''}.", False
    m = re.match(r'^[Ii]riyati vattati pāleti yapeti yāpeti carati viharati\.$', s)
    if m:
        return (VIHARATI_J if sid in JHANA_SIDS else VIHARATI), False
    m = Q12_RX.match(s)
    if m:
        n, tail, n2 = m.groups()
        v = name12(n, sid)
        if n == "ariyā":
            return f"{S.TATTHA} {v} là những ai?", False
        if tail == "?":
            return q(v), False
        assert n2 == n, s
        return f"{q(v)[:-1]}… {CALLED} “{v}”.", False
    m = re.match(r"^(.*) (santā|santaṃ) (hoti|honti) samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā "
                 r"sositā visositā byantīkatā\.$", s)
    if m:
        return f"{SANTA_SUBJ[m.group(1)]} {SANTA}.", False
    m = re.match(r"^Idaṃ cittaṃ (\S+ \S+) sodheti visodheti parisodheti moceti vimoceti parimoceti\.$", s)
    if m:
        return f"Vị ấy {CLEANSE} tâm này khỏi {CLEANSE_OBJ[m.group(1)]}.", False
    m = re.match(r"^(.*?) upeto hoti(…pe…| samupeto…pe…| samupeto upāgato samupāgato upapanno sampanno) "
                 r"samannāgato\.$", s)
    if m:
        obj, mid = m.groups()
        verbs = {"…pe…": UPETO_PE, " samupeto…pe…": "có được, có được trọn vẹn… được trang bị"}.get(mid, UPETO)
        iti = obj.startswith("Iti ")
        return f"{'Như vậy, v' if iti else 'V'}ị ấy {verbs} {UPETO_OBJ[obj]}.", False
    m = re.match(r"^Tassa (\S+) cattattā vantattā muttattā pahīnattā paṭinissaṭṭhattā pahīnapaṭinissaṭṭhattā\.$", s)
    if m:
        return f"Vì {GIVEN_SUBJ[m.group(1)]} ấy {GIVEN_UP}.", False
    m = re.match(r"^Yo (.+?) lābho paṭilābho patti sampatti phusanā sacchikiriyā upasampadā\.$", s)
    if m:
        return f"{WHICH} {GAIN} {GEN[m.group(1)]}.", False
    m = re.match(r"^(\S+) samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā cittacetasikā dhammā\.$", s)
    if m:
        return f"{cap(CITTACET)} {SAMAPANNA.format(x=ACCAY[low(m.group(1))])}.", False
    m = re.match(r"^Imaṃ (\S+) atikkanto hoti vītikkanto samatikkanto\.$", s)
    if m:
        return f"Vị ấy {OVERCOME} {ACCAY[m.group(1)]} này.", False
    m = re.match(r"^([YÑ])atvādhikaraṇamenaṃ (cakkhundriyaṃ|manindriyaṃ) asaṃvutaṃ viharantaṃ abhijjhādomanassā "
                 r"pāpakā akusalā dhammā anvāssaveyyuṃ, tassa saṃvarāya (na )?paṭipajjati, (?:na )?rakkhati \2, "
                 r"\S+ (?:na )?saṃvaraṃ āpajjati\.$", s)
    if m:
        y, ind, neg = m.groups()
        if y == "Ñ":
            slip(f"^{sid} «Ñatvādhikaraṇamenaṃ» for Yatvādhikaraṇamenaṃ (spelling slip, rendered as meant)")
        return EYE_TAIL[not neg].format(i=K45.IND[ind]), False
    m = A12_RX.match(s)
    if m:
        body, pron, _, qt, n, ti = m.groups()
        frame = CALLED_PL if pron in ("ime", "imā") else CALLED
        nv = name12(n, sid)
        if not qt:
            slip(f"^{sid} «… vuccati {n}» without quotation marks: kept without “ ”")
            return f"{body12(body, sid)} – {frame} {nv}.", False
        return f"{body12(body, sid)} – {frame} “{nv}”.", False
    m = re.match(r'^(Ayaṃ|Idaṃ|Ime|Imā) (vuccati|vuccanti) "(.+?)"\.$', s)
    if m:
        frame = CALLED_PL if m.group(1) in ("Ime", "Imā") else CALLED
        return f"{cap(frame)} “{name12(m.group(3), sid)}”.", False
    m = re.match(r"^(Yo|Yā|Yaṃ) (.*)\.$", s)
    if m:
        return f"{WHICH} {BODY12[m.group(2)]}.", False
    m = TOPIC0_RX.match(s)
    if m:
        kind, v, _ = topic_vi(topic_key(m.group(1), ""), sid)
        return K79.topic(kind, v), True
    m = TOPIC_RX.match(s)
    if m:
        t, n, rest = m.groups()
        kind, v, _ = topic_vi(topic_key(t, n), sid)
        tv = K79.topic(kind, v)
        if rest is None:
            return tv, True
        r, _ = sentence12(cap(rest), sid)
        return f"{tv} {low(r)}", False
    raise KeyError((sid, s))


def line12(ln, sid):
    if " …pe…" in ln:
        slip(f"^{sid}: a space before «…pe…» (ignored)")
        ln = ln.replace(" …pe…", "…pe…")
    if ln == '"Byāpādapadosā cittaṃ parisodhetī"ti. Atthi byāpādo atthi padoso.':
        slip("^2-545 «Atthi byāpādo atthi padoso.»: comma missing (added, as ^2-542)")
        ln = '"Byāpādapadosā cittaṃ parisodhetī"ti. Atthi byāpādo, atthi padoso.'
    out, lower_next = [], False
    for s in SPLIT_RX.split(ln):
        v, tp = sentence12(s, sid)
        out.append(low(v) if lower_next else v)
        lower_next = tp
    assert not lower_next, ln
    return " ".join(out)


# =========================================================================== chapter 12: Abhidhamma lines
WHEN = "Vào lúc một người "
OPENERS = {  # Pāli after «Idha bhikkhu yasmiṃ samaye» -> Vietnamese after «Ở đây, vào lúc một vị tỳ-khưu»
    "rūpūpapattiyā maggaṃ bhāveti": K6.RUPA_PATH[len(WHEN):],
    "arūpūpapattiyā maggaṃ bhāveti": K6.ARUPA_PATH[len(WHEN):],
    K6.P_SUPRA: K6.SUPRA[len(WHEN):],
    "rūpāvacaraṃ " + K6.P_KIR: K6.KIRIYA_R[len(WHEN):],
    "arūpāvacaraṃ " + K6.P_KIR: K6.KIRIYA_A[len(WHEN):],
}
LEAD = {"vivicceva kāmehi": pi1("hoàn toàn tách khỏi các dục lạc"),
        "vitakkavicārānaṃ vūpasamā": pi1("nhờ sự hướng tâm và sự duy trì tâm lắng xuống"),
        "pītiyā ca virāgā": pi1("nhờ sự hân hoan phai nhạt"), "sukhassa ca pahānā": pi1("nhờ dứt bỏ sự dễ chịu")}
ORDN = {"paṭhamaṃ": "thứ nhất", "dutiyaṃ": "thứ hai", "tatiyaṃ": "thứ ba", "catutthaṃ": "thứ tư",
        "pañcamaṃ": "thứ năm"}
CLAUSE = {
    ("vivicceva kāmehi vivicca akusalehi dhammehi avitakkaṃ vicāramattaṃ vivekajaṃ pītisukhaṃ dutiyaṃ jhānaṃ "
     "upasampajja viharati"):
        (f"{TOPICS['vivicceva kāmehi vivicca akusalehi dhammehi'][1]}, {ENTER} tầng thiền thứ hai, "
         + pi1("không có sự hướng tâm, chỉ có sự duy trì tâm") + ", có sự hân hoan và hạnh phúc sinh từ sự tách biệt"),
    ("vitakkavicārānaṃ vūpasamā…pe… dutiyaṃ jhānaṃ…pe… tatiyaṃ jhānaṃ…pe… catutthaṃ jhānaṃ…pe… paṭhamaṃ jhānaṃ…pe… "
     "pañcamaṃ jhānaṃ upasampajja viharati"):
        pi1("nhờ sự hướng tâm và sự duy trì tâm lắng xuống… tầng thiền thứ hai… tầng thiền thứ ba… tầng thiền thứ tư… "
            "tầng thiền thứ nhất… chứng nhập và an trú tầng thiền thứ năm"),
    K6.P_J4: K6.J4,
}
misfit("^2-625, ^2-629 pañcaka second jhāna «vivicceva kāmehi vivicca akusalehi dhammehi avitakkaṃ vicāramattaṃ "
       "vivekajaṃ pītisukhaṃ dutiyaṃ jhānaṃ»: not in pi-1 in this form; built from the pi-1 pieces")
FIELD12 = {"pathavīkasiṇaṃ": f", {K6.KASINA}", "dukkhapaṭipadaṃ dandhābhiññaṃ": f", {K6.MODE}",
           "dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ": f", {K6.MODE}, {K6.EMPTY}", "": ""}
TASSEVA12 = {"Tasseva rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ": K6.OF_RUPA,
             "Tasseva arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ": K6.OF_ARUPA,
             "Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ": K6.OF_LOK}
ANGA = {"pañcaṅgikaṃ": "gồm năm chi phần", "caturaṅgikaṃ": "gồm bốn chi phần", "tivaṅgikaṃ": "gồm ba chi phần",
        "duvaṅgikaṃ": "gồm hai chi phần"}                # termbase pañcaṅgikaṃ jhānaṃ «tầng thiền gồm năm chi phần» …
JHANA4 = "Bốn tầng thiền – " + ", ".join(f"tầng thiền {ORDN[k]}" for k in list(ORDN)[:4]) + "."
L638 = f"Bốn tầng thiền – ở đây, vị tỳ-khưu {JH1}… {JH2}… {JH3}… {JH4}."
REST_J = "Các hiện tượng còn lại gắn liền với tầng thiền"   # Avasesā dhammā jhānasampayuttā
SENT_A12 = {
    "Cattāri jhānāni – paṭhamaṃ jhānaṃ, dutiyaṃ jhānaṃ, tatiyaṃ jhānaṃ, catutthaṃ jhānaṃ.": JHANA4,
    "Catukkaṃ.": pi1("Phương pháp chia bốn."), "Pañcakaṃ.": pi1("Phương pháp chia năm."),   # user: jhāna method
    "Ime dhammā kusalā.": f"{cap(ARE_KUSALA)}.",
    "Avasesā dhammā jhānasampayuttā.": f"{REST_J}.", "Avasesā dhammā jhānasampayuttā…pe….": f"{REST_J}…",
    "Avasesā dhammā jhānasampayuttāti.": f"{REST_J}.",
    "Abhidhammabhājanīyaṃ.": K1.FIXED["Abhidhammabhājanīyaṃ."],
}


def clause12(c):
    if c in CLAUSE:
        return CLAUSE[c]
    m = re.match(r"^(vivicceva kāmehi|vitakkavicārānaṃ vūpasamā|pītiyā ca virāgā|sukhassa ca pahānā)…pe… (\S+) jhānaṃ "
                 r"upasampajja viharati$", c)
    assert m, c
    return f"{LEAD[m.group(1)]}… {ENTER} tầng thiền {ORDN[m.group(2)]}"


CLAUSE_RX = re.compile(r"^(.*?upasampajja viharati) ?(pathavīkasiṇaṃ|dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ|"
                       r"dukkhapaṭipadaṃ dandhābhiññaṃ|)$")


def jhana_tail(t, sid):
    """«phasso hoti…pe… avikkhepo hoti.» / «N jhānaṃ hoti – F.» -> Vietnamese (after «thì vào lúc ấy»)"""
    if t == "phasso hoti…pe… avikkhepo hoti.":
        return f"{CONTACT_PE}."
    m = re.match(r"^(\S+) jhānaṃ hoti( –)? (.*)\.$", t)
    assert m, t
    n, dash, f = m.groups()
    if not dash:
        slip(f"^{sid} «caturaṅgikaṃ jhānaṃ hoti vicāro pīti sukhaṃ cittassekaggatā»: no dash and no commas (the "
             "parallels have «hoti – vicāro, pīti, …»); no dash added, «:» written, commas rendered as meant")
        return f"có tầng thiền {ANGA[n]}: {factors(f)}."
    return f"có tầng thiền {ANGA[n]} – {factors(f)}."


def abhi12_sentence(s, sid):
    if s in SENT_A12:
        return SENT_A12[s]
    m = re.match(r'^Idaṃ vuccati "(\S+ jhānaṃ)"\.$', s)
    if m:
        return f"{cap(CALLED)} “{NAMES12[m.group(1)]}”."
    m = re.match(r"^Tattha katamaṃ (\S+ jhānaṃ)\?$", s)
    if m:
        return q(NAMES12[m.group(1)])
    m = re.match(r"^Idha bhikkhu yasmiṃ samaye (.*?), tasmiṃ samaye (.*)$", s)
    if m:
        head, tail = m.groups()
        op = next(k for k in OPENERS if head.startswith(k + " "))
        cm = CLAUSE_RX.match(head[len(op) + 1:])
        assert cm, head
        return f"{MONK_WHEN} {OPENERS[op]}, {clause12(cm.group(1))}{FIELD12[cm.group(2)]}, {THEN} {jhana_tail(tail, sid)}"
    m = re.match(r"^(Tasseva .*? vipākaṃ) (.*?), tasmiṃ samaye (.*)$", s)
    if m:
        ts, head, tail = m.groups()
        cm = CLAUSE_RX.match(head)
        assert cm, head
        return (f"{K6.ALSO_WHEN} {clause12(cm.group(1))}{FIELD12[cm.group(2)]}, {TASSEVA12[ts]}, {THEN} "
                f"{jhana_tail(tail, sid)}")
    raise KeyError((sid, s))


def abhi12_line(ln, sid):
    if " …pe…" in ln:
        slip(f"^{sid}: a space before «…pe…» (ignored)")
        ln = ln.replace(" …pe…", "…pe…")
    return " ".join(abhi12_sentence(s, sid) for s in SPLIT_RX.split(ln))


# =========================================================================== build and render
FOREIGN = K79.FOREIGN
EARLIER = {}            # identical Pāli lines of the approved earlier pi-2 chapters -> their Vietnamese


def load_earlier():
    for f in ("4-saccavibhango.md", "5-indriyavibhango.md", "7-satipatthanavibhango.md",
              "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md"):
        pa = (S.PALI / f).read_text(encoding="utf-8")
        vi = (S.OUT / f).read_text(encoding="utf-8")
        ps, vs = K1.segs(pa), K1.segs(vi)
        for (sid, pl), (sid2, vl) in zip(ps, vs):
            assert sid == sid2, (f, sid, sid2)
            for p, v in zip(pl, vl):
                p, v = K1.ID.sub("", p), K1.ID.sub("", v)
                if not p.startswith("#"):
                    EARLIER.setdefault(p, v)


def heading(ln, ch):
    lvl, text = ln.split(" ", 1)
    t = {"Bojjhaṅgavibhaṅgo": S.CH_HEADINGS["Bojjhaṅgavibhaṅgo"], "Maggaṅgavibhaṅgo": S.CH_HEADINGS["Maggaṅgavibhaṅgo"],
         "Jhānavibhaṅgo": S.CH_HEADINGS["Jhānavibhaṅgo"], "Tikaṃ": K1.TIKA_H, "Dukaṃ": K1.DUKA_H,
         "Mātikā": "Ma trận",                                            # termbase Mātikā «ma trận»
         "Rūpāvacarakusalaṃ": pi1("Tâm thiện thuộc cõi hình sắc"),
         "Arūpāvacarakusalaṃ": pi1("Tâm thiện thuộc cõi không hình sắc"),
         "Lokuttarakusalaṃ": pi1("Tâm thiện vượt thế gian"),
         "Rūpāvacaravipākā": pi1("Quả của nghiệp thuộc cõi hình sắc"),
         "Arūpāvacaravipākā": pi1("Quả của nghiệp thuộc cõi không hình sắc"),
         "Lokuttaravipākā": pi1("Quả của nghiệp vượt thế gian"),
         "Rūpārūpāvacarakiriyā": "Tâm mang tính chức năng thuộc cõi hình sắc và cõi không hình sắc"}   # termbase
    t.update(S.SEC_HEADINGS)
    return f"{lvl} {t[text]}"


def check_line(sid, p, v):
    assert K79.dashes(p) == K79.dashes(v), (sid, "dash count", K79.dashes(p), K79.dashes(v), v[:160])
    assert ":-" not in v and "—" not in v and "…." not in v, (sid, v[:160])
    body = re.sub(r"\[[^\]]*\]", "", v)
    assert not FOREIGN.search(body), (sid, FOREIGN.search(body).group(0), v[:200])
    assert "  " not in v and not v.endswith(" "), (sid, v[:160])
    assert v.count("“") == v.count("”"), (sid, "quotes", v[:200])
    assert "là là" not in v, (sid, v[:160])
    if not p.startswith("#"):
        assert v[-1] in ".?…", (sid, v[-40:])
        assert p.endswith("?") == v.endswith("?"), (sid, v[-40:])


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
            h[sid] = [heading(lines[0], ch)]
            continue
        vi = []
        for ln in lines:
            if ln in SENT:
                vi.append(SENT[ln])
            elif ln in EARLIER:
                vi.append(pi2(EARLIER[ln]))
            elif section == "Pañhāpucchakaṃ":
                if ln.startswith("Cattāri jhānāni – idha bhikkhu"):
                    vi.append(L638)
                elif ln.endswith("?"):
                    vi.append(panha_question(ln))
                else:
                    vi.append(panha_line(ln, sid, ch))
            elif ch == 12 and section == "Suttantabhājanīyaṃ":
                vi.append(line12(ln, sid))
            elif ch == 12:
                vi.append(abhi12_line(ln, sid))
            else:
                vi.append(def_line(ln, sid))
        h[sid] = vi
    for sid, lines in K1.segs(pali):
        for p, v in zip([K1.ID.sub("", ln) for ln in lines], h[sid]):
            check_line(sid, p, v)
    return pali, h


def render(pali, h):
    blocks = []
    for sid, plines in K1.segs(pali):
        vi = h[sid]
        assert len(vi) == len(plines), (sid, len(vi), len(plines))
        if plines[0].startswith("#"):
            assert vi[0].split(" ", 1)[0] == plines[0].split(" ", 1)[0], (sid, "heading level")
        lines = list(vi)
        lines[-1] = f"{lines[-1]} ^{sid}"
        blocks.append("\n".join(lines))
    return unicodedata.normalize("NFC", "\n\n".join(blocks) + "\n")


def check_pi1():
    text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI1_VI.glob("*.md")))
    missing = [s for s in PI1_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    return len(PI1_USED)


def check_pi2():
    files = ["1-khandhavibhango.md", "4-saccavibhango.md", "5-indriyavibhango.md", "6-paticcasamuppadavibhango.md",
             "7-satipatthanavibhango.md", "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md"]
    text = "\n".join((S.OUT / f).read_text(encoding="utf-8") for f in files)
    missing = [s for s in PI2_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    return len(PI2_USED)


# =========================================================================== notes
def notes_md():
    L = ["# pi-2 Vietnamese rails: new formulas of chapters 10-12 (^2-10-0 … ^2-641)", "",
         "Generated by build_rails_10_12_vi.py; import it instead of retyping. Strings already in vi-rails-formulas.md "
         "(sample) or notes-1 … notes-7-9 are not repeated (the supramundane opener and path factors come from ch. 4, "
         "the jhāna openers and the Tasseva … vipākaṃ openers from ch. 6, the possession string, the topic frames and "
         "«Tena vuccati» from ch. 6-9). Format: Pāli = tiếng Việt.", "",
         "## Headings and closing labels", "",
     ] + [f"### {n} = ### {S.CH_HEADINGS[n]}; closing «{n} niṭṭhito.» = «{S.CH_HEADINGS[n]} {K1.DONE}.»"
          for n in ("Bojjhaṅgavibhaṅgo", "Maggaṅgavibhaṅgo", "Jhānavibhaṅgo")] + [
         "##### " + " / ".join(("Mātikā", "Rūpāvacarakusalaṃ", "Arūpāvacarakusalaṃ", "Lokuttarakusalaṃ",
                                "Rūpāvacaravipākā", "Arūpāvacaravipākā", "Lokuttaravipākā", "Rūpārūpāvacarakiriyā"))
         + " = ##### " + " / ".join(heading(f"##### {x}", 12)[6:] for x in (
             "Mātikā", "Rūpāvacarakusalaṃ", "Arūpāvacarakusalaṃ", "Lokuttarakusalaṃ", "Rūpāvacaravipākā",
             "Arūpāvacaravipākā", "Lokuttaravipākā", "Rūpārūpāvacarakiriyā")),
         f"Catukkaṃ. / Pañcakaṃ. = {SENT_A12['Catukkaṃ.']} / {SENT_A12['Pañcakaṃ.']} (pi-1; user: jhāna method)",
         "", "## Awakening factors (ch. 10)", "",
         f"Satta bojjhaṅgā – satisambojjhaṅgo, … = {BJ7_FULL}",
         f"Satta bojjhaṅgā – satisambojjhaṅgo…pe… upekkhāsambojjhaṅgo. = {BJ7_PE}",
         "Xsambojjhaṅgo = " + "; ".join(f"{k} = {bj(k)}" for k in BJ_ORDER),
         f"Tattha katamo satisambojjhaṅgo? = {ask('satisambojjhaṅgo')} (factor names quoted as question topics)",
     ] + [f"{p} – ayaṃ vuccati \"…\". = {v} – {CALLED} “…”." for p, v in L467_MAP.items()] + [
         "Atthi X, atthi Y. = Có x, có y.",
         f"Yadapi X tadapi Ysambojjhaṅgo abhiññāya sambodhāya nibbānāya saṃvattati. = X cũng là y, {LEADS}.",
     ] + [f"{k} = {v}" for k, v in L469_ITEMS.items()] + [
         f"Xṃ bhāveti {NISSITA_P} = tu tập x, {NISSITA}; Xṃ bhāveti, Yṃ bhāveti…pe… = tu tập x; tu tập y…",
         f"Ime vuccanti (\"…\") satta bojjhaṅgā. = {SENT['Ime vuccanti satta bojjhaṅgā.']}",
         f"Avasesā dhammā sattahi bojjhaṅgehi sampayuttā. = Các hiện tượng còn lại gắn liền với {SEVEN_BJ}.",
         "Avasesā dhammā Xsambojjhaṅgasampayuttā…pe… avasesā dhammā … = Các hiện tượng còn lại gắn liền với x… các "
         "hiện tượng còn lại gắn liền với …",
         f"…, tasmiṃ samaye satta bojjhaṅgā honti – satisambojjhaṅgo…pe… upekkhāsambojjhaṅgo. = …, {THEN} có "
         f"{SEVEN_BJ} – {bj('sati')}… {bj('upekkhā')}.",
         f"…, yo tasmiṃ samaye phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā. = …, {THEN} {CONTACT_PE} – "
         f"{ARE_KUSALA}.",
         "", "## Path factors (ch. 11)", "",
         f"Ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – … = {ARIYO8}", f"Aṭṭhaṅgiko maggo – … = {AT8}",
         f"Aṭṭhaṅgiko maggo – sammādiṭṭhi…pe… sammāsamādhi. = {AT8_PE}", f"Pañcaṅgiko maggo – … = {AT5}",
         f"Tattha katamo sammāvāyāmo? Idha bhikkhu … (comma-joined) – ayaṃ vuccati \"sammāvāyāmo\". = {L487_EFF}",
         f"Tattha katamā sammāsati? Idha bhikkhu kāye … (comma-joined) = {L487_SATI}",
         f"Tattha katamo sammāsamādhi? Idha bhikkhu vivicceva kāmehi …; … (no dash before the quote) = {L487_SAMADHI}",
         "Avasesā dhammā aṭṭhaṅgikena / pañcaṅgikena maggena / sammādiṭṭhiyā / sammāsaṅkappena … sampayuttā. = Các "
         "hiện tượng còn lại gắn liền với con đường gồm tám / năm chi phần / quan điểm đúng đắn / tư duy đúng đắn …",
         "", "## Answer bodies (after «Điều mà là»)", "",
     ] + [f"{k} = {v}" for k, v in BODY.items()] + [f"{k} = {v}" for k, v in BODY12.items()] + [
         "", "## Jhāna Suttanta (ch. 12)", "",
         "\"X\"ti … (one word) = Về từ “x”: …; (a phrase) = Về câu “x”: … ; \"X\"ti. = Về từ “x”: (next sentence lower "
         "case)",
         f"\"Viharatī\"ti…pe… tena vuccati \"viharatī\"ti. = Về từ “sống / an trú”… {low(TENA)} “sống / an trú”.",
         f"Iriyati vattati pāleti yapeti yāpeti carati viharati. = {VIHARATI} (conduct) / {VIHARATI_J} (jhāna)",
     ] + [f"{k}ti = {K79.topic(*v)}" for k, v in TOPICS.items()] + [
         f"X santā hoti / honti samitā vūpasantā … byantīkatā. = X {SANTA}.",
     ] + [f"{k} = {v}" for k, v in SANTA_SUBJ.items()] + [
         f"Idaṃ cittaṃ imāya / imamhā X sodheti visodheti parisodheti moceti vimoceti parimoceti. = Vị ấy {CLEANSE} "
         f"tâm này khỏi x này.",
         f"<X> upeto hoti samupeto upāgato … samannāgato. = Vị ấy {UPETO} x. (…pe… = {UPETO_PE})",
     ] + [f"{k} = {v}" for k, v in UPETO_OBJ.items()] + [
         f"Tassa X cattattā vantattā muttattā pahīnattā paṭinissaṭṭhattā pahīnapaṭinissaṭṭhattā. = Vì x ấy {GIVEN_UP}.",
         f"Yo X-assa lābho paṭilābho patti sampatti phusanā sacchikiriyā upasampadā. = {WHICH} {GAIN} x.",
         "Gaṇanānupubbatā paṭhamaṃ. Idaṃ paṭhamaṃ samāpajjatīti paṭhamaṃ. = Thứ nhất theo thứ tự đếm. Là thứ nhất vì "
         "đây là điều được chứng nhập thứ nhất.",
         f"[gaṇanānupubbato (syā.) evamuparipi] = {GANANA_V.strip()}",
         f"X – te imasmiṃ viveke / samādhimhi jātā honti sañjātā nibbattā abhinibbattā pātubhūtā. = X – chúng {JATA} "
         f"trong sự tách biệt này / trong định tâm này.",
         f"X samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā cittacetasikā dhammā. = {cap(CITTACET)} "
         f"{SAMAPANNA.format(x='x')}.",
         f"Imaṃ X atikkanto hoti vītikkanto samatikkanto. = Vị ấy {OVERCOME} x này.",
         f"the formless attainments (^2-508) = {AR1}; {AR2}; {AR3}; {AR4}",
         f"So abhikkante paṭikkante sampajānakārī hoti, … = Vị ấy {SAMPAJ_Q}.",
         f"Idha bhikkhu sato sampajāno abhikkamati, … = Ở đây, {sato_moves(True)}.",
         "", "## Jhāna Abhidhamma (ch. 12)", "",
         f"Cattāri jhānāni – paṭhamaṃ jhānaṃ, … = {JHANA4}",
         "Idha bhikkhu yasmiṃ samaye <opener> <jhāna> <field>, tasmiṃ samaye … = Ở đây, vào lúc một vị tỳ-khưu "
         "<opener>, <jhāna><field>, thì vào lúc ấy …",
     ] + [f"opener {k} = {v}" for k, v in OPENERS.items()] + [f"{k}…pe… Nṃ jhānaṃ upasampajja viharati = {v}… "
                                                              f"{ENTER} tầng thiền N" for k, v in LEAD.items()] + [
         f"{k} = {v}" for k, v in CLAUSE.items()] + [f"field {k} = {v}" for k, v in FIELD12.items() if k] + [
         f"{k} = {K6.ALSO_WHEN} <jhāna><field>, {v}" for k, v in TASSEVA12.items()] + [
         f"tasmiṃ samaye Nṅgikaṃ jhānaṃ hoti – F. = thì vào lúc ấy có tầng thiền gồm N chi phần – f. (" + "; ".join(
             f"{k} = {v}" for k, v in FACTORS.items()) + ")",
         f"Idaṃ vuccati \"paṭhamaṃ jhānaṃ\". = {cap(CALLED)} “{NAMES12['paṭhamaṃ jhānaṃ']}”.",
         f"Avasesā dhammā jhānasampayuttā. = {REST_J}.",
         "", "## Question sections", "",
         "Sattannaṃ bojjhaṅgānaṃ / Aṭṭhannaṃ maggaṅgānaṃ / Catunnaṃ jhānānaṃ kati …? = " + " / ".join(
             f"{a}, {b} …?" for a, b in GROUPS.values()),
         "subjects: " + "; ".join(f"{k} = {v[0]}{' (+ thì)' if v[2] else ''}" for k, v in SUBJ.items()),
         "X – etthuppannaṃ Y ṭhapetvā Z = X – ngoại trừ y sinh khởi trong đó, z (" + "; ".join(
             f"{k} = {v}" for k, v in ETTHU.items()) + ")",
         "Kenaci viññeyyā, kenaci na viññeyyā (mid-sentence) = " + K1.KENACI.replace("những khối", "những <noun>"),
         f"na vattabbā \"X\"ti (ch. 12, quoted) = {NV} rằng “x” (no dash)",
     ]
    return unicodedata.normalize("NFC", "\n".join(L) + "\n")


def main():
    load_earlier()
    for ch, part in PARTS.items():
        pali, h = build(ch)
        text = render(pali, h)
        (S.OUT / part).write_bytes(text.encode("utf-8"))
        print(f"wrote {part}: {len(h)} segments")
    n1, n2 = check_pi1(), check_pi2()
    NOTES_PATH.write_bytes(notes_md().encode("utf-8"))
    print(f"pi-1 strings checked: {n1}; pi-2 strings checked: {n2}; notes-10-12.md written")
    for s in SLIPS:
        print("slip:", s)
    for s in MISFITS:
        print("misfit:", s)


if __name__ == "__main__":
    main()

