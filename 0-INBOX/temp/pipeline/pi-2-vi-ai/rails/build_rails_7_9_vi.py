"""Builder for the Vietnamese rails translation of pi-2 (Vibhaṅga, «Phân tích các hiện tượng», plain audience),
chapters 7 (Satipaṭṭhānavibhaṅgo ^2-7-0 … ^2-389), 8 (Sammappadhānavibhaṅgo ^2-8-0 … ^2-430) and 9
(Iddhipādavibhaṅgo ^2-9-0 … ^2-465).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/7-satipatthanavibhango.md
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/8-sammappadhanavibhango.md
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/9-iddhipadavibhango.md
  0-INBOX/temp/pipeline/pi-2-vi-ai/rails/notes-7-9.md   (new recurring formulas, Pāli = tiếng Việt)

Translated fresh from the Pāli with the locked pi-2 termbase (viharati «sống» in the satipaṭṭhāna formula, «an trú»
in the attainments; vāyāma / padhāna «sự nỗ lực» vs vīriya «sự tinh tấn»; sāmisa / nirāmisa «có / không có tính
trần tục»; chandasamādhi «định tâm nhờ ý muốn», padhānasaṅkhāro «sự tạo tác bằng nỗ lực», iddhipāda «nền tảng thần
thông»). Shared strings are imported read-only from the approved sample builder (S) and the chapter 1, 2-3, 4-5 and 6
builders (K1, K23, K45, K6): the satipaṭṭhāna and right-effort formulas of ch. 4 (^2-205), the supramundane jhāna
openers, the wisdom / energy / concentration / mindfulness lists, the matrix predicates, «Ở đây, X là gì?», «Vì thế,
điều này được gọi là “…”». Passages that repeat the Dhammasaṅgaṇī reuse the approved pi-1 Vietnamese rails (marked
pi1() and asserted to occur there by check_pi1()). Every Vietnamese line is checked against its Pāli line for the dash
count and for left-over Pāli letters. Importing this module writes nothing.

usage: python -I -X utf8 build_rails_7_9_vi.py
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

PARTS = {7: "7-satipatthanavibhango.md", 8: "8-sammappadhanavibhango.md", 9: "9-iddhipadavibhango.md"}
PI1_VI = S.ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
NOTES_PATH = RAILS / "notes-7-9.md"
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


# =========================================================================== shared strings (imported)
EFFORT = pi2(K45.EFFORT)            # chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati (ch. 4)
EVIL, GOOD = K45.EVIL, K45.GOOD     # pāpakānaṃ akusalānaṃ dhammānaṃ / kusalānaṃ dhammānaṃ
ARDENT = pi2(K45.ARDENT)            # ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ (ch. 4 ^2-205)
VINEYYA = ARDENT.split(", ", 3)[3]  # vineyya loke abhijjhādomanassaṃ
assert VINEYYA == "sau khi chế ngự sự thèm muốn và nỗi buồn đối với thế gian", VINEYYA
PF = K45.PF                         # the path factors (sammāvāyāmo «nỗ lực đúng đắn» …)
PATH_TAIL = K45.PATH_TAIL           # maggaṅgaṃ maggapariyāpannaṃ (pi-1)
SUPRA = pi2(K45.SUPRA)              # Idha bhikkhu yasmiṃ samaye lokuttaraṃ … dandhābhiññaṃ, tasmiṃ samaye (ch. 4)
SUPRA_END = ", thì vào lúc ấy"
assert SUPRA.endswith(SUPRA_END)
SUPRA_CORE = SUPRA[:-len(SUPRA_END)]          # … chậm chạp (before a field or «yo tasmiṃ samaye …»)
MONK_WHEN = "Ở đây, vào lúc một vị tỳ-khưu"   # Idha bhikkhu yasmiṃ samaye (ch. 4 supra_line)
TASSEVA = K6.TASSEVA[("Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… "
                      "paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ")]
CONTACT_PE = K6.CONTACT_PE          # phasso hoti…pe… avikkhepo hoti «có sự tiếp xúc… có sự không tán loạn» (pi-1)
ARE_KUSALA = K6.ARE_KUSALA          # ime dhammā kusalā «những hiện tượng này là thiện» (pi-1)
WHAT_AT_TIME = "thì điều mà vào lúc ấy là"   # yo / yā / yaṃ tasmiṃ samaye … (after the opener)
KH4 = K6.KH4                        # khối cảm giác, khối tri giác, khối tạo tác, khối thức
TOGETHER = pi2(K23.TOGETHER)        # tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā (sample)
FIVE_UPA = K45.FIVE_UPA             # pañcupādānakkhandhā «năm khối làm đối tượng cho sự bám víu»
TOPIC_C = K6.TOPIC                  # «X-ti.» of a phrase: «Về câu “x”:» (ch. 6); the next sentence in lower case
TOPIC_W = "Về từ “{x}”:"            # «X-ti.» of a single Pāli word (new): «Về từ “x”:»

# =========================================================================== names and nouns
SATIP4 = "Bốn sự thiết lập tỉnh thức"           # Cattāro satipaṭṭhānā (termbase satipaṭṭhānā)
SAMMAP4 = "Bốn nỗ lực đúng đắn"                 # Cattāro sammappadhānā (termbase sammappadhānā)
IDDHIP4 = "Bốn nền tảng thần thông"             # Cattāro iddhipādā (termbase iddhipādā)
IP = "nền tảng thần thông"                      # iddhipādo
IPN = {"chand": f"{IP} bằng ý muốn", "vīriy": f"{IP} bằng tinh tấn", "citt": f"{IP} bằng tâm",
       "vīmaṃs": f"{IP} bằng sự thẩm xét"}       # termbase Chandiddhipādo … Vīmaṃsiddhipādo
SAMADHI_BY = {"chanda": "ý muốn", "vīriya": "tinh tấn", "citta": "tâm", "vīmaṃsā": "sự thẩm xét"}
# termbase chandasamādhi «định tâm nhờ ý muốn», vīriyasamādhi «… nhờ tinh tấn», cittasamādhi «… nhờ tâm»,
# vīmaṃsāsamādhi «… nhờ sự thẩm xét»
PS = "sự tạo tác bằng nỗ lực"                   # padhānasaṅkhāro (termbase)


def samadhi_n(k):
    return f"định tâm nhờ {SAMADHI_BY[k]}"


def sps(k):
    """Xsamādhipadhānasaṅkhāro «định tâm nhờ X và sự tạo tác bằng nỗ lực»"""
    return f"{samadhi_n(k)} và {PS}"


def ip_endowed(k):
    """Xsamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ (termbase …samannāgataṃ «được trang bị định tâm … và sự tạo
    tác bằng nỗ lực»)"""
    return f"{IP} được trang bị {sps(k)}"


NOUN = {  # Pāli term (as asked and as named in «vuccati "X"») -> Vietnamese
    "anupassanā": "sự quán sát", "ātāpo": "sự nhiệt tâm", "sampajaññaṃ": "sự hiểu biết rõ ràng",
    "sati": "sự tỉnh thức", "loko": "thế gian", "abhijjhā": "sự thèm muốn", "domanassaṃ": "nỗi buồn",
    "chando": "ý muốn", "vāyāmo": "sự nỗ lực", "vīriyaṃ": "sự tinh tấn", "cittaṃ": "tâm", "padhānaṃ": "sự nỗ lực",
    "sammappadhānaṃ": "nỗ lực đúng đắn", "satipaṭṭhānaṃ": "sự thiết lập tỉnh thức", "samādhi": "định tâm",
    "padhānasaṅkhāro": PS, "padhānasaṅkhārā": f"các {PS}", "vīmaṃsā": "sự thẩm xét",
    "anuppannā pāpakā akusalā dhammā": f"{EVIL} chưa sinh khởi",
    "uppannā pāpakā akusalā dhammā": f"{EVIL} đã sinh khởi",
    "anuppannā kusalā dhammā": f"{GOOD} chưa sinh khởi",
    "uppannā kusalā dhammā": f"{GOOD} đã sinh khởi",
}
for _k, _v in IPN.items():
    NOUN[f"{_k}iddhipādo"] = _v
for _k in SAMADHI_BY:
    NOUN[f"{_k}samādhi"] = samadhi_n(_k)
DEM = {  # Imāya / Iminā X (instrumental) -> the noun (with «này» added)
    "anupassanāya": "anupassanā", "ātāpena": "ātāpo", "sampajaññena": "sampajaññaṃ", "satiyā": "sati",
    "vāyāmena": "vāyāmo", "padhānena": "padhānaṃ", "chandena": "chando", "samādhinā": "samādhi",
    "padhānasaṅkhārena": "padhānasaṅkhāro", "vīriyena": "vīriyaṃ", "cittena": "cittaṃ", "vīmaṃsāya": "vīmaṃsā",
}
UPETO = "có được, có được trọn vẹn, đã tiếp cận, đã tiếp cận trọn vẹn, đã đạt đến, thành tựu, được trang bị"
UPETO_PE = "có được… được trang bị"
# upeto «có được», samupeto «có được trọn vẹn», upapanno «đã đạt đến», sampanno «thành tựu», samannāgato «được
# trang bị» (termbase); upāgato / samupāgato have no entry: «đã tiếp cận» / «đã tiếp cận trọn vẹn» (reported)
misfit("upāgato, samupāgato (^2-357 … ^2-455, the possession string «upeto hoti samupeto upāgato samupāgato upapanno "
       "sampanno samannāgato»): no termbase entry; «đã tiếp cận», «đã tiếp cận trọn vẹn» beside upeto «có được», "
       "samupeto «có được trọn vẹn», upapanno «đã đạt đến»")

# topics: Pāli (lower case, «ti» removed, niggahīta restored) -> (kind, Vietnamese)
TOPICS = {
    "anupassī": ("w", "quán sát"), "viharatī": ("w", "sống"), "ātāpī": ("w", "nhiệt tâm"),
    "sampajāno": ("w", "hiểu biết rõ ràng"), "satimā": ("w", "có sự tỉnh thức"),
    "vineyya loke abhijjhādomanassaṃ": ("c", VINEYYA),
    "chandaṃ janetī": ("c", "khởi lên ý muốn"), "vāyamatī": ("w", "nỗ lực"),
    "vīriyaṃ ārabhatī": ("c", "khởi động tinh tấn"), "cittaṃ paggaṇhātī": ("c", "nâng tâm lên"),
    "padahatī": ("w", "ra sức nỗ lực"), "ṭhitiyā": ("w", "được duy trì"),
    "iddhī": ("w", "thần thông"), "iddhipādo": ("w", IP), "iddhipādaṃ bhāvetī": ("c", f"tu tập {IP}"),
}
TENA_T = {k: v for k, (_, v) in TOPICS.items()}       # Tena vuccati "X"ti
for _k in SAMADHI_BY:
    TENA_T[f"{_k}samādhipadhānasaṅkhārasamannāgato"] = f"được trang bị {sps(_k)}"
misfit("Iddhi (^2-434 …, «Iddhīti. Yā tesaṃ dhammānaṃ iddhi samiddhi ijjhanā …», iddhi as 'success'): the only "
       "termbase sense is the compound member «thần thông»; kept «thần thông» as topic and first list word, the "
       "rest of the list (samiddhi «sự thịnh đạt», ijjhanā «sự thành tựu» …) gives the sense")


def topic(kind, vi):
    return (TOPIC_W if kind == "w" else TOPIC_C).format(x=vi)


# =========================================================================== the four foundations (fields)
FIELD = {"kāye": ("thân", "thân"), "vedanāsu": ("các cảm giác", "các cảm giác"), "citte": ("tâm", "tâm"),
         "dhammesu": ("các hiện tượng", "các hiện tượng")}
# termbase kāye kāyānupassī «thân … quán sát thân», vedanāsu vedanānupassī «cảm giác … quán sát các cảm giác», …;
# ch. 4 ^2-205 «đối với thân, vị tỳ-khưu sống quán sát thân»
SIDE = {"": "", "ajjhattaṃ": " ở nơi bản thân", "bahiddhā": " ở bên ngoài bản thân",
        "ajjhattabahiddhā": " ở nơi bản thân và ở bên ngoài bản thân"}
# termbase ajjhattaṃ kāye «thân ở nơi bản thân», bahiddhā kāye «thân ở bên ngoài bản thân», ajjhattabahiddhā kāye
# «thân ở nơi bản thân và ở bên ngoài bản thân»
FIELD_RX = r"(ajjhattaṃ |bahiddhā |ajjhattabahiddhā )?(kāye|vedanāsu|citte|dhammesu) (?:kāy|vedan|citt|dhamm)ānupassī"


def lives(loc, side, who="vị tỳ-khưu"):
    """«(side) X Xānupassī viharati» -> «đối với X (side), <who> sống quán sát X»"""
    place, obj = FIELD[loc]
    return f"đối với {place}{SIDE[side]}, {who} sống quán sát {obj}"


def contemplating(loc):
    """Abhidhamma opener: «… dandhābhiññaṃ kāye kāyānupassī» -> «, quán sát thân đối với thân»"""
    place, obj = FIELD[loc]
    return f"quán sát {obj} đối với {place}"


def satip4(p):
    """Cattāro satipaṭṭhānā – idha bhikkhu … (^2-355, 374, 380, 386)"""
    body = p[len("Cattāro satipaṭṭhānā – idha bhikkhu "):-1]
    if body.startswith("ajjhattaṃ"):                  # ^2-355: three sides per field, the qualities after the third
        groups = re.findall(r"ajjhattaṃ (\S+) \S+ viharati bahiddhā \1 \S+ viharati ajjhattabahiddhā \1 \S+ viharati "
                            r"ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ", body)
        assert len(groups) == 4, p
        out = []
        for n, loc in enumerate(groups):
            first = lives(loc, "ajjhattaṃ", "vị tỳ-khưu" if n == 0 else "vị ấy")
            out.append(f"{first}; {lives(loc, 'bahiddhā', 'vị ấy')}; {lives(loc, 'ajjhattabahiddhā', 'vị ấy')}, "
                       f"{ARDENT}")
        return f"{SATIP4} – ở đây, {'; '.join(out)}."
    ardent = "ātāpī" in body
    locs = re.findall(r"(kāye|vedanāsu|citte|dhammesu) \S+ viharati", body)
    assert len(locs) == 4, p
    out = [lives(loc, "", "vị tỳ-khưu" if n == 0 else "vị ấy") + (f", {ARDENT}" if ardent else "")
           for n, loc in enumerate(locs)]
    return f"{SATIP4} – ở đây, {'; '.join(out)}."


# =========================================================================== the four right efforts
AIM = {  # Pāli aim -> Vietnamese «để …» with {t} for «này» (Iti imesaṃ …); ch. 4 ^2-205 wording
    "anuppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ anuppādāya": f"để {EVIL} chưa sinh khởi{{t}} không sinh khởi",
    "uppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ pahānāya": f"để dứt bỏ {EVIL} đã sinh khởi{{t}}",
    "anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya": f"để {GOOD} chưa sinh khởi{{t}} được sinh khởi",
    ("uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā"):
        (f"để {GOOD} đã sinh khởi{{t}} được duy trì, không bị mai một, được tăng trưởng, được lớn mạnh, được tu tập "
         f"và được hoàn thiện"),
}
for _v in AIM.values():                                # the ch. 4 strings (asserted)
    assert _v.format(t="") in K45.L205_7, _v
    pi2(_v.format(t=""))
AIM_ORDER = list(AIM)
EFFORT_P = "chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati"
AIM_RX = "(" + "|".join(re.escape(k) for k in sorted(AIM, key=len, reverse=True)) + ")"


def aim(p, these=False):
    return AIM[p].format(t=" này" if these else "")


def efforts(body, who_first):
    """«A1 E, A2 E, A3 E, A4 E» or «A1 E, A2…pe… A3…pe… A4 E» -> Vietnamese (no final stop)"""
    full = ", ".join(f"{a} {EFFORT_P}" for a in AIM_ORDER)
    if body == full:
        return "; ".join(f"{who_first if n == 0 else 'vị ấy'} {EFFORT} {aim(a)}" for n, a in enumerate(AIM_ORDER))
    pe = f"{AIM_ORDER[0]} {EFFORT_P}, {AIM_ORDER[1]}…pe… {AIM_ORDER[2]}…pe… {AIM_ORDER[3]} {EFFORT_P}"
    assert body == pe, body
    return (f"{who_first} {EFFORT} {aim(AIM_ORDER[0])}; {aim(AIM_ORDER[1])}… {aim(AIM_ORDER[2])}… vị ấy {EFFORT} "
            f"{aim(AIM_ORDER[3])}")


# =========================================================================== the four bases of power
IP_KEYS = {"chanda": "chand", "vīriya": "vīriy", "citta": "citt", "vīmaṃsā": "vīmaṃs"}
IP_ENDOWED_RX = r"(chanda|vīriya|citta|vīmaṃsā)samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti"
ADHIPATI = {"Chandaṃ": "ý muốn", "Vīriyaṃ": "sự tinh tấn", "Cittaṃ": "tâm", "Vīmaṃsaṃ": "sự thẩm xét"}
# Xṃ ce bhikkhu adhipatiṃ karitvā (pi-1 ^1-1040 «lấy … làm yếu tố chủ đạo»; ce «nếu»)
ONE_POINT = pi1("sự nhất tâm")                       # cittassekaggataṃ (termbase; pi-1 ^1-1 cittassekaggatā)


def iddhip4(p):
    """Cattāro iddhipādā – idha bhikkhu … (^2-431, 444, 462)"""
    body = p[len("Cattāro iddhipādā – idha bhikkhu "):-1]
    ks = re.findall(IP_ENDOWED_RX, body)
    if len(ks) == 4:
        return f"{IDDHIP4} – ở đây, vị tỳ-khưu " + ", ".join(f"tu tập {ip_endowed(k)}" for k in ks) + "."
    pe = ("chandasamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti, vīriyasamādhi…pe… cittasamādhi…pe… "
          "vīmaṃsāsamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti")
    assert body == pe, body
    return (f"{IDDHIP4} – ở đây, vị tỳ-khưu tu tập {ip_endowed('chanda')}, {samadhi_n('vīriya')}… "
            f"{samadhi_n('citta')}… tu tập {ip_endowed('vīmaṃsā')}.")


# =========================================================================== definitions (answer bodies)
CHANDA = "ý muốn, sự khởi ý muốn, sự mong muốn hành động, ý muốn thiện đối với các hiện tượng"
# chando «ý muốn», chandikatā «sự khởi ý muốn», kattukamyatā (no entry: kattu «hành động» + kamyatā «sự mong muốn»,
# user decision), kusalo dhammacchando «ý muốn thiện đối với các hiện tượng» (termbase)
misfit("kattukamyatā (^2-392 …, the chanda string): no entry; built from kattu «hành động» + kamyatā «sự mong muốn» "
       "(user decision): «sự mong muốn hành động»")
CHANDA_V = CHANDA.replace("sự khởi ý muốn", "sự khởi ý muốn " + S.spell("Syā.", "chandīkatā"), 1)
VIRIYA_PE = f"{K45.VIRIYA_HEAD}… {PF['sammāvāyāmo']}"                  # cetasiko vīriyārambho…pe… sammāvāyāmo
VIRIYA_PATH = f"{K45.FACTOR_BODY['cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo']}, {PATH_TAIL}"
VIRIYA_FULL = f"{K45.VIRIYA}, {PF['sammāvāyāmo']}"                       # ch. 5 ^2-220 energy list + sammāvāyāmo
SATI_PE = f"{pi1('sự tỉnh thức, sự nhớ lại')}… {PF['sammāsati']}"        # sati anussati…pe… sammāsati
SATI_PATH = (f"sự tỉnh thức, sự nhớ lại, {PF['sammāsati']}, {pi1('chi phần giác ngộ là sự tỉnh thức')}, "
             f"{PATH_TAIL}")                                              # sati anussati sammāsati satisambojjhaṅgo …
SAMADHI_PE = f"{pi1('sự ổn định của tâm, sự vững vàng')}… {PF['sammāsamādhi']}"
SAMADHI_PATH = f"{K45.FACTOR_BODY['cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo']}, {PATH_TAIL}"
CITTA_PE = f"{K23.CITTA_SHORT} {K23.DH['manoviññāṇa']} {K23.TAJJA}"     # cittaṃ mano mānasaṃ…pe… tajjā…dhātu
RAGA_PE = K6.BODY["Yo rāgo sārāgo…pe… cittassa sārāgo"][len(WHICH) + 1:]   # sự tham đắm, sự say đắm… (ch. 6)
SAMPAY = pi1("khối cảm giác, khối tri giác, khối tạo tác và khối thức gắn liền với chúng")   # pi-1 ^1-985
SAMUTTH = pi1("nghiệp bằng thân, nghiệp bằng lời nói, nghiệp bằng ý do chúng sinh ra")       # pi-1 ^1-985
ENERGY_P = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo ṭhiti asithilaparakkamatā "
            "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ")
BODY = {  # Pāli after «Yo / Yā / Yaṃ» -> Vietnamese (after «Điều mà là»)
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": K45.PANNA_SHORT,
    ("paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ "
     "maggapariyāpannaṃ"): K6.PANNA_PATH,
    "cetasiko vīriyārambho…pe… sammāvāyāmo": VIRIYA_PE,
    "cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": VIRIYA_PATH,
    f"{ENERGY_P} sammāvāyāmo": VIRIYA_FULL,
    "sati anussati…pe… sammāsati": SATI_PE,
    "sati anussati sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": SATI_PATH,
    "rāgo sārāgo…pe… cittassa sārāgo": RAGA_PE,
    ("cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā "
     "vedanā"): K23.FEELING_P1["domanassa"],
    "chando chandikatā kattukamyatā kusalo dhammacchando": CHANDA,
    "chando chandikatā [chandīkatā (syā.)] kattukamyatā kusalo dhammacchando": CHANDA_V,
    "cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu": CITTA_PE,
    ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ "
     "sammāsamādhi"): K45.SAMADHI,
    "cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi": SAMADHI_PE,
    "cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": SAMADHI_PATH,
}
BODY_CAP = {  # answer bodies that are not «Yo / Yā / Yaṃ …» (already sentence-initial)
    ("Taṃsampayutto vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho, taṃsamuṭṭhānaṃ kāyakammaṃ "
     "vacīkammaṃ manokammaṃ"): f"{cap(SAMPAY)}; {SAMUTTH}",
    "Taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ, manokammaṃ": cap(SAMUTTH),
}


def body_vi(b):
    if b in BODY_CAP:
        return BODY_CAP[b]
    m = re.match(r"^(Yo|Yā|Yaṃ) (.*)$", b)
    assert m, b
    return f"{WHICH} {BODY[m.group(2)]}"


# =========================================================================== fixed sentences
VIHARATI = "Vị ấy vận động, tiến triển, gìn giữ, tiếp diễn, kéo dài, đi lại, sống."
# Iriyati «vận động», vattati «tiến triển», pāleti «gìn giữ», yapeti «tiếp diễn», yāpeti «kéo dài», carati «đi lại»,
# viharati «sống» (termbase senses 'in the synonyms of viharati')
NIMITTA = "Vị ấy thực hành dấu hiệu ấy, tu tập, làm đi làm lại và xác định nó một cách vững chắc."
NIMITTA_THEN = ("Sau khi thực hành dấu hiệu ấy, tu tập, làm đi làm lại và xác định nó một cách vững chắc, vị ấy đưa "
                "tâm đến {t}.")
# taṃ nimittaṃ āsevati «thực hành dấu hiệu ấy», bhāveti «tu tập», bahulīkaroti «làm đi làm lại», vavatthapeti «xác
# định», cittaṃ upasaṃharati «đưa tâm đến» (termbase); svāvatthitaṃ: no entry, «một cách vững chắc» (reported)
misfit("svāvatthitaṃ (^2-356 …, «svāvatthitaṃ vavatthapeti»): no entry; «xác định nó một cách vững chắc»")
VINITA = ("Như vậy, sự thèm muốn này và nỗi buồn này trong thế gian này đã được chế ngự, đã được chế ngự hoàn toàn, đã "
          "lắng yên, đã được làm lắng dịu, đã lắng dịu hoàn toàn, đã biến mất, đã biến mất hoàn toàn, đã đi đến kết "
          "thúc, đã đi đến kết thúc hoàn toàn, đã bị làm khô cạn, đã bị làm khô cạn hoàn toàn, đã bị làm cho tiêu tan.")
# vinītā: no entry, «đã được chế ngự» (paṭivinītā «đã được chế ngự hoàn toàn», vineyya «sau khi chế ngự»); the rest
# termbase (santā «đã lắng yên», samitā «đã được làm lắng dịu», vūpasantā «đã lắng dịu hoàn toàn» …)
misfit("vinītā (^2-362 …): no entry; «đã được chế ngự», from paṭivinītā «đã được chế ngự hoàn toàn»")
misfit("loko (^2-362 …, «Tattha katamo loko?»): no headword; «thế gian» from loke «thế gian»")
VINITA_P = ("Iti ayañca abhijjhā idañca domanassaṃ imamhi loke vinītā honti paṭivinītā santā samitā vūpasantā "
            "atthaṅgatā abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā.")
CHANDA_VERB = ("Vị ấy khởi lên ý muốn này, làm sinh ra, làm trỗi dậy, làm trỗi dậy trọn vẹn{v}, làm phát khởi, làm phát "
               "khởi trọn vẹn.")
# Imaṃ chandaṃ janeti «khởi lên ý muốn này», sañjaneti «làm sinh ra», samuṭṭhapeti «làm trỗi dậy trọn vẹn»,
# nibbatteti «làm phát khởi» (termbase); uṭṭhapeti, abhinibbatteti: no entry («làm trỗi dậy», «làm phát khởi trọn
# vẹn», from their siblings)
misfit("uṭṭhapeti, abhinibbatteti (^2-392 …, «Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti nibbatteti "
       "abhinibbatteti»): no entries; «làm trỗi dậy», «làm phát khởi trọn vẹn» from samuṭṭhapeti «làm trỗi dậy trọn "
       "vẹn», nibbatteti «làm phát khởi»")
CHANDA_VAR = " [khác chính tả (Syā.): uṭṭhāpeti samuṭṭhāpeti, cũng vậy ở các chỗ sau]"   # (syā.) evamuparipi
VIRIYA_VERB = "Vị ấy khởi động sự tinh tấn này, khởi động trọn vẹn, thực hành, tu tập, làm đi làm lại."
# Imaṃ vīriyaṃ ārabhati «khởi động sự tinh tấn này», samārabhati «khởi động trọn vẹn», āsevati, bhāveti, bahulīkaroti
CITTA_VERB = "Vị ấy nâng tâm này lên, nâng lên trọn vẹn, nâng đỡ, nâng đỡ vững chắc."
# Imaṃ cittaṃ paggaṇhāti «nâng tâm này lên», sampaggaṇhāti «nâng lên trọn vẹn», upatthambheti «nâng đỡ»,
# paccupatthambheti «nâng đỡ vững chắc» (termbase)
TE_DHAMME = "Vị ấy thực hành những hiện tượng ấy, tu tập, làm đi làm lại."    # Te dhamme āsevati bhāveti bahulīkaroti.
THITI_CHAIN = ("Sự duy trì chính là sự không mai một, sự không mai một chính là sự tăng trưởng, sự tăng trưởng chính là "
               "sự lớn mạnh, sự lớn mạnh chính là sự tu tập, sự tu tập chính là sự hoàn thiện.")
# ṭhiti «sự duy trì» (persistence of wholesome states, user decision), asammoso «sự không mai một», vepullaṃ «sự lớn
# mạnh», bhāvanā «sự tu tập», pāripūrī «sự hoàn thiện»; bhiyyobhāvo: no entry, «sự tăng trưởng» (ch. 4 bhiyyobhāvāya
# «được tăng trưởng»)
misfit("bhiyyobhāvo (^2-406, ^2-420): no entry; «sự tăng trưởng», from ch. 4 bhiyyobhāvāya «được tăng trưởng»")
IDDHI_DEF = ("Điều mà ở những hiện tượng ấy là thần thông, sự thịnh đạt, sự thành tựu, sự thành tựu trọn vẹn, sự đạt "
             "được, sự có được, sự đạt đến, sự đạt đến trọn vẹn, sự chạm, sự tự mình chứng nghiệm, sự chứng nhập.")
# Yā tesaṃ dhammānaṃ iddhi samiddhi ijjhanā samijjhanā lābho paṭilābho patti sampatti phusanā sacchikiriyā upasampadā
TATHA = "của người đã trở thành như vậy"            # Tathābhūtassa (bhūta «đã trở thành», sample)
misfit("Tathābhūtassa (^2-434 …): no entry; «của người đã trở thành như vậy» (bhūta «đã trở thành», sample)")
ROOTS_A = pi1("Ba gốc rễ bất thiện – sự tham lam, sự sân hận, sự si mê")       # pi-1 ^1-986
ROOTS_K = pi1("Ba gốc rễ thiện – sự không tham lam, sự không sân hận, sự không si mê")   # pi-1 ^1-985
TADEKATTHA = pi1("và các phiền não cùng hiện diện với chúng")                  # pi-1 ^1-986
LOKO = {"Sveva kāyo loko.": "Chính thân ấy là thế gian.", "Sāyeva vedanā loko.": "Chính cảm giác ấy là thế gian.",
        "Taṃyeva cittaṃ loko.": "Chính tâm ấy là thế gian.", "Teva dhammā loko.": "Chính các hiện tượng ấy là thế gian."}
FIVE_LOKO = f"{cap(FIVE_UPA)} cũng là thế gian"     # Pañcapi upādānakkhandhā loko

SUBHEAD = {
    "Kāyānupassanāniddeso": "Giải thích sự quán sát thân",                # termbase
    "Vedanānupassanāniddeso": "Giải thích sự quán sát các cảm giác",
    "Cittānupassanāniddeso": "Giải thích sự quán sát tâm",
    "Dhammānupassanāniddeso": "Giải thích sự quán sát các hiện tượng",
}
for _k, _v in IPN.items():
    SUBHEAD[f"{cap(_k)}iddhipādo"] = cap(_v)                             # termbase Chandiddhipādo …
CH_NAME = {7: "Satipaṭṭhānavibhaṅgo", 8: "Sammappadhānavibhaṅgo", 9: "Iddhipādavibhaṅgo"}

SENT = {
    "Suttantabhājanīyaṃ.": K1.FIXED["Suttantabhājanīyaṃ."],
    "Abhidhammabhājanīyaṃ.": K1.FIXED["Abhidhammabhājanīyaṃ."],
    "Pañhāpucchakaṃ.": K1.FIXED["Pañhāpucchakaṃ."],
    "Ime dhammā kusalā.": f"{cap(ARE_KUSALA)}.",
    "Iriyati vattati pāleti yapeti yāpeti carati viharati.": VIHARATI,
    "So taṃ nimittaṃ āsevati bhāveti bahulīkaroti svāvatthitaṃ vavatthapeti.": NIMITTA,
    "Pañcapi upādānakkhandhā loko.": f"{FIVE_LOKO}.",
    VINITA_P: VINITA,
    "Tīṇi akusalamūlāni – lobho, doso, moho.": f"{ROOTS_A}.",
    "Tīṇi kusalamūlāni – alobho, adoso, amoho.": f"{ROOTS_K}.",
    "Tadekaṭṭhā ca kilesā.": f"{cap(TADEKATTHA)}.",
    "Taṃsampayutto vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.": f"{cap(SAMPAY)}.",
    ("Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti [uṭṭhāpeti samuṭṭhāpeti (syā.) evamuparipi] nibbatteti "
     "abhinibbatteti."): CHANDA_VERB.format(v=CHANDA_VAR),
    "Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti nibbatteti abhinibbatteti.": CHANDA_VERB.format(v=""),
    "Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti.": VIRIYA_VERB,
    "Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti.": CITTA_VERB,
    ("Yā ṭhiti so asammoso, yo asammoso so bhiyyobhāvo, yo bhiyyobhāvo taṃ vepullaṃ, yaṃ vepullaṃ sā bhāvanā, yā "
     "bhāvanā sā pāripūrī."): THITI_CHAIN,
    'Ime vuccanti "padhānasaṅkhārā".': f"{cap(CALLED_PL)} “{NOUN['padhānasaṅkhārā']}”.",
    ("Yā tesaṃ dhammānaṃ iddhi samiddhi ijjhanā samijjhanā lābho paṭilābho patti sampatti phusanā sacchikiriyā "
     "upasampadā."): IDDHI_DEF,
    "Tathābhūtassa vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.": f"{cap(KH4)} {TATHA}.",
    "Tathābhūtassa vedanākkhandho…pe… viññāṇakkhandho.": f"Khối cảm giác… khối thức {TATHA}.",
    "Tathābhūtassa phasso…pe… paggāho avikkhepo.": f"Sự tiếp xúc… sự dốc sức, sự không tán loạn {TATHA}.",
    "Te dhamme āsevati bhāveti bahulīkaroti.": TE_DHAMME,
    "Cattāro iddhipādā – chandiddhipādo, vīriyiddhipādo, cittiddhipādo, vīmaṃsiddhipādo.":
        f"{IDDHIP4} – {', '.join(IPN.values())}.",
}
SENT.update(LOKO)
for _ch, _n in CH_NAME.items():
    SENT[f"{_n} niṭṭhito."] = f"{S.CH_HEADINGS[_n]} {K1.DONE}."
for _p, _v in SUBHEAD.items():
    SENT[f"{_p}."] = f"{_v}."


# =========================================================================== chapter 7: the Suttanta practice lines
BODY31_P_V = ("kesā lomā nakhā dantā taco maṃsaṃ nhāru [nahāru (sī.)] aṭṭhi aṭṭhimiñjaṃ [aṭṭhimiñjā (sī.)] vakkaṃ "
              "hadayaṃ yakanaṃ kilomakaṃ pihakaṃ papphāsaṃ antaṃ antaguṇaṃ udariyaṃ karīsaṃ pittaṃ semhaṃ pubbo "
              "lohitaṃ sedo medo assu vasā kheḷo siṅghāṇikā lasikā mutta")
BODY31_P = re.sub(r" \[[^\]]*\]", "", BODY31_P_V)
BODY31_V = f"{pi2(K23.LISTS['pathavī_i'])}, {pi2(K23.LISTS['āpo_i'])}"   # the ch. 3 earth and water lists, in order
BODY31 = re.sub(r" \[[^\]]*\]", "", BODY31_V)
SCAN = "từ lòng bàn chân trở lên, từ đỉnh tóc trở xuống, được bao bọc bởi da, chứa đầy những thứ bất tịnh đủ loại"
# uddhaṃ pādatalā adho kesamatthakā tacapariyantaṃ pūraṃ nānappakārassa asucino (termbase kesamatthakā «đỉnh tóc»,
# pariyantaṃ «được bao bọc bởi», taco «da», asucino «bất tịnh»; pādatalā, pūraṃ, nānappakārassa: no entries)
misfit("pādatalā, pūraṃ, nānappakārassa (^2-356): no entries; «từ lòng bàn chân trở lên», «chứa đầy những thứ bất tịnh "
       "đủ loại»")
IN_BODY = {"atthi imasmiṃ kāye": "Trong thân này có", "atthissa kāye": "Trong thân của người ấy có"}
# atthissa «của người ấy có» (termbase)
SCAN_RX = re.compile(r'^Idha bhikkhu (ajjhattaṃ|bahiddhā|ajjhattabahiddhā) kāyaṃ uddhaṃ pādatalā adho kesamatthakā '
                     r'tacapariyantaṃ pūraṃ nānappakārassa asucino paccavekkhati – "(atthi imasmiṃ kāye|atthissa kāye) '
                     r'(.*)"nti\.$')
THEN_RX = re.compile(r"^So taṃ nimittaṃ āsevitvā bhāvetvā bahulīkaritvā svāvatthitaṃ vavatthapetvā "
                     r"(bahiddhā|ajjhattabahiddhā) (kāye|vedanāsu|citte|dhammesu) cittaṃ upasaṃharati\.$")
EVAM_RX = re.compile(r"^Evaṃ bhikkhu ajjhattabahiddhā (kāye|vedanāsu|citte|dhammesu) \S+ viharati ātāpī sampajāno "
                     r"satimā vineyya loke abhijjhādomanassaṃ\.$")
HOW_RX = re.compile(r"^Kathañca bhikkhu " + FIELD_RX + r" viharati\?$")


def scan(s):
    m = SCAN_RX.match(s)
    side, ib, lst = m.groups()
    vi = {BODY31_P_V: BODY31_V, BODY31_P: BODY31}[lst]
    return f"Ở đây, vị tỳ-khưu quán xét thân{SIDE[side]}, {SCAN} – “{IN_BODY[ib]} {vi}”."


FEEL_B = {"sukhaṃ": "cảm giác dễ chịu", "dukkhaṃ": "cảm giác khó chịu",
          "adukkhamasukhaṃ": "cảm giác không khó chịu cũng không dễ chịu"}
FEEL_NOM = {"sukhaṃ": "sukhā", "dukkhaṃ": "dukkhā", "adukkhamasukhaṃ": "adukkhamasukhā"}
FEEL_Q = {"": "", "sāmisaṃ": " có tính trần tục", "nirāmisaṃ": " không có tính trần tục"}
# termbase sāmisaṃ sukhaṃ vedanaṃ «cảm giác dễ chịu có tính trần tục», nirāmisaṃ … «… không có tính trần tục»;
# vedayamāno «khi cảm nhận», vedayāmī «tôi đang cảm nhận», vedayatī «người ấy đang cảm nhận», pajānāti «hiểu rõ»
FEEL_ITEM = re.compile(r'^(?:(sāmisaṃ|nirāmisaṃ) vā )?(sukhaṃ|dukkhaṃ|adukkhamasukhaṃ) vedanaṃ '
                       r'(vedayamāno |vedayamānaṃ )?"(.*)"ti pajānāti$')


def feel_sentence(s):
    """Idha bhikkhu sukhaṃ vedanaṃ vedayamāno "…"ti pajānāti, … (^2-363, three lines)"""
    items = s[len("Idha bhikkhu "):-1].split(", ")
    out = []
    for n, it in enumerate(items):
        m = FEEL_ITEM.match(it)
        assert m, it
        qual, base, mode, quote = m.groups()
        qual = qual or ""
        f = FEEL_B[base] + FEEL_Q[qual]
        who = "vị tỳ-khưu" if n == 0 else "vị ấy"
        pre = "hoặc " if qual else ""
        qp = f"{qual} " if qual else ""
        if mode == "vedayamāno ":
            assert quote == f"{qp}{base} vedanaṃ vedayāmī", it
            out.append(f"{pre}khi cảm nhận {f}, {who} hiểu rõ: “Tôi đang cảm nhận {f}”")
        elif mode == "vedayamānaṃ ":
            assert quote == f"{qp}{base} vedanaṃ vedayatī", it
            out.append(f"{pre}về người đang cảm nhận {f}, {who} hiểu rõ: “Người ấy đang cảm nhận {f}”")
        else:
            qn = f"{qual[:-2]}ā " if qual else ""
            assert quote == f"{qn}{FEEL_NOM[base]} vedanā", it
            out.append(f"{pre}{who} hiểu rõ {f} là “{f}”")
    return "Ở đây, " + "; ".join(out) + "."


MIND = {"sarāgaṃ": "có tham đắm", "vītarāgaṃ": "đã lìa tham đắm", "sadosaṃ": "có sân hận",
        "vītadosaṃ": "đã lìa sân hận", "samohaṃ": "có si mê", "vītamohaṃ": "đã lìa si mê", "saṃkhittaṃ": "co rút",
        "vikkhittaṃ": "tán loạn", "mahaggataṃ": "rộng lớn", "amahaggataṃ": "không rộng lớn",
        "sauttaraṃ": "còn có điều cao hơn", "anuttaraṃ": "không có điều gì cao hơn", "samāhitaṃ": "được định tâm",
        "asamāhitaṃ": "không được định tâm", "vimuttaṃ": "được giải thoát", "avimuttaṃ": "không được giải thoát"}
# termbase sarāgaṃ vā cittaṃ «hoặc … tâm có tham đắm» … (vā «hoặc»)
MIND_ITEM = re.compile(r'^(\S+) (vā|vāssa) cittaṃ "(\S+?)( me |massa | )citta"nti pajānāti$')


def mind_sentence(s):
    """Idha bhikkhu sarāgaṃ vā cittaṃ "sarāgaṃ me citta"nti pajānāti, … (^2-365, three lines)"""
    items = s[len("Idha bhikkhu "):-1].split(", ")
    out = []
    for n, it in enumerate(items):
        m = MIND_ITEM.match(it)
        assert m, it
        a, va, qa, kind = m.groups()
        assert qa == (a[:-1] if kind == "massa " else a), it
        assert (va == "vāssa") == (kind == "massa "), it
        mv = MIND[a]
        who = "vị tỳ-khưu" if n == 0 else "vị ấy"
        pre = "hoặc " if n else ""
        if kind == " me ":
            out.append(f"{pre}khi tâm {mv}, {who} hiểu rõ: “Tâm tôi {mv}”")
        elif kind == "massa ":
            out.append(f"{pre}khi tâm của người ấy {mv}, {who} hiểu rõ: “Tâm của người ấy {mv}”")
        else:
            out.append(f"{pre}khi tâm {mv}, {who} hiểu rõ: “Tâm {mv}”")
    return "Ở đây, " + "; ".join(out) + "."


DH_NOUN = {"kāmacchand": "ý muốn dục lạc", "byāpād": "ác ý", "thinamiddh": "sự uể oải và đờ đẫn",
           "uddhaccakukkucc": "sự xao động và hối tiếc", "vicikicch": "sự hoài nghi"}      # termbase (accusatives)
BOJJH = {"sati": "sự tỉnh thức", "dhammavicaya": "sự tìm hiểu các hiện tượng", "vīriya": "sự tinh tấn",
         "pīti": "sự hân hoan", "passaddhi": "sự an tịnh", "samādhi": "định tâm", "upekkhā": "sự bình thản"}
for _k, _v in BOJJH.items():
    DH_NOUN[f"{_k}sambojjhaṅg"] = f"chi phần giác ngộ là {_v}"                   # termbase Xsambojjhaṅgaṃ
DH_NOM = {"kāmacchand": "kāmacchando", "vicikicch": "vicikicchā"}
for _k in BOJJH:
    DH_NOM[f"{_k}sambojjhaṅg"] = f"{_k}sambojjhaṅgo"
UNIT_S = re.compile(r'^(santaṃ|asantaṃ) (vā ajjhattaṃ|vāssa|vā) (\S+?)aṃ( \[[^\]]+\])?(?: "(.*)"ti pajānāti)?$')
UNIT_Y = re.compile(r"^yathā ca (anuppann|uppann|pahīn)(?:assa|āya) (\S+?)(?:assa|āya) (uppādo hoti|pahānaṃ hoti|"
                    r"āyatiṃ anuppādo hoti|bhāvanāya pāripūrī hoti) tañca pajānāti$")
PTCP = {"anuppann": "chưa sinh khởi", "uppann": "đã sinh khởi", "pahīn": "đã được dứt bỏ"}
EVENT = {  # yathā ca <ptcp> X <event> hoti tañca pajānāti -> «vị ấy cũng hiểu rõ …» (termbase uppādo «nảy sinh»,
    # anuppādo «không nảy sinh», pahānaṃ «sự dứt bỏ», satisambojjhaṅgassa bhāvanāya pāripūrī «… được tu tập đến chỗ
    # hoàn thiện»; āyatiṃ: no entry, «trong tương lai»)
    "uppādo hoti": "{x} {p} nảy sinh như thế nào",
    "pahānaṃ hoti": "sự dứt bỏ {x} {p} diễn ra như thế nào",
    "āyatiṃ anuppādo hoti": "{x} {p} không nảy sinh trong tương lai như thế nào",
    "bhāvanāya pāripūrī hoti": "{x} {p} được tu tập đến chỗ hoàn thiện như thế nào",
}


def sigla(s):
    """«sī. syā.» -> «Sī., Syā.»"""
    return ", ".join(cap(x) for x in s.split())


def variant(br):
    """« [word (sī. syā.)]» (spelling only) -> « [khác chính tả (Sī., Syā.): word]»"""
    m = re.match(r"^ \[(\S+) \(([^)]+)\)\]$", br)
    assert m, br
    return " " + S.spell(sigla(m.group(2)), m.group(1))


def dh_unit(u, first, lead):
    m = UNIT_S.match(u)
    if m:
        st, side, stem, br, quote = m.groups()
        has = "có" if st == "santaṃ" else "không có"
        x = DH_NOUN[stem]
        xv = x + (variant(br) if br else "")
        pre = "" if lead else "hoặc "
        who = "vị tỳ-khưu" if lead else "vị ấy"
        if side == "vā ajjhattaṃ":
            cond, qv = f"khi {has} {xv} ở nơi bản thân", f"Ở nơi bản thân tôi {has} {x}"
            qp = f"{'atthi' if has == 'có' else 'natthi'} me ajjhattaṃ {DH_NOM.get(stem)}"
        elif side == "vāssa":
            cond, qv = f"khi người ấy {has} {xv}", f"Người ấy {has} {x}"
            qp = f"{'atthissa' if has == 'có' else 'natthissa'} {DH_NOM.get(stem)}"
        else:
            cond, qv = f"khi {has} {xv}", f"{cap(has)} {x}"
            qp = f"{'atthi' if has == 'có' else 'natthi'} {DH_NOM.get(stem)}"
        if quote is None:
            return f"{pre}{cond}"
        assert quote == qp, (u, qp)
        return f"{pre}{cond}, {who} hiểu rõ: “{qv}”"
    m = UNIT_Y.match(u)
    assert m, u
    p, stem, ev = m.groups()
    return "vị ấy cũng hiểu rõ " + EVENT[ev].format(x=DH_NOUN[stem], p=PTCP[p])


def dh_sentence(s):
    """Idha bhikkhu santaṃ vā … / Santaṃ vā … (^2-367): units joined by «, » and «…pe… »"""
    lead = s.startswith("Idha bhikkhu ")
    body = s[len("Idha bhikkhu "):] if lead else low(s)
    assert body.endswith("."), s
    toks = re.split(r"(…pe… |, )", body[:-1])
    out = ""
    for i, t in enumerate(toks):
        if i % 2:
            out += "… " if t.startswith("…pe…") else "; "
            continue
        out += dh_unit(t, i == 0, lead and i == 0)
    return ("Ở đây, " + out if lead else cap(out)) + "."


# =========================================================================== the supramundane opener lines
SUPRA_P = ("Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya "
           "paṭhamāya bhūmiyā pattiyā vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ "
           "dandhābhiññaṃ")
TASSEVA_P = ("Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ "
             "upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ")
FIELD_TAIL_RX = re.compile(r"^(?: (kāye|vedanāsu|citte|dhammesu) \S+ānupassī)?, (?:yo|yā|yaṃ) tasmiṃ samaye (.*) – "
                           r"(?:ayaṃ|idaṃ) vuccati (\"?)(\S+?)\"?\.$")


def called(name, quoted, sid):
    """«– ayaṃ/idaṃ vuccati "X".» -> «– đó được gọi là “x”.» (without the quotes where the source has none)"""
    if not quoted:
        slip(f"^{sid} «… vuccati {name}» without quotation marks: kept without “ ”")
        return f"– {CALLED} {NOUN[name]}."
    return f"– {CALLED} “{NOUN[name]}”."


def field_tail(rest, sid):
    m = FIELD_TAIL_RX.match(rest)
    assert m, rest
    loc, body, qt, name = m.groups()
    fld = f", {contemplating(loc)}" if loc else ""
    return f"{fld}, {WHAT_AT_TIME} {BODY[body]} {called(name, bool(qt), sid)}"


def at_time_clause(c):
    """the clause after «…, tasmiṃ samaye» in the right-effort and power lines (no final stop) -> «vị ấy …»"""
    m = re.match(r"^" + AIM_RX + " " + EFFORT_P + "$", c)
    if m:
        return f"vị ấy {EFFORT} {aim(m.group(1))}"
    m = re.match(r"^" + IP_ENDOWED_RX + "$", c)
    if m:
        return f"vị ấy tu tập {ip_endowed(m.group(1))}"
    raise KeyError(c)


def supra_sentence(s, sid):
    if s.startswith(SUPRA_P):
        rest = s[len(SUPRA_P):]
        if rest == ", tasmiṃ samaye phasso hoti…pe… avikkhepo hoti.":
            return f"{MONK_WHEN} {SUPRA} {CONTACT_PE}."
        m = re.match(r"^, tasmiṃ samaye (.*)\.$", rest)
        if m:
            return f"{MONK_WHEN} {SUPRA} {at_time_clause(m.group(1))}."
        return f"{MONK_WHEN} {SUPRA_CORE}{field_tail(rest, sid)}"
    assert s.startswith(TASSEVA_P), s
    return f"{TASSEVA}{field_tail(s[len(TASSEVA_P):], sid)}"


# =========================================================================== the sentence engine
SPLIT_RX = re.compile(r'(?<=[.?])\s+(?=["A-ZĀĪŪṬÑṆḌḶṂ])')
Q_RX = re.compile(r"^Tattha (?:katamo|katamā|katamaṃ|katame) (.+?)( \[[^\]]+\])?\?$")
A_RX = re.compile(r'^(.*) – (ayaṃ|idaṃ|ime) (vuccati|vuccanti) ("?)(.+?)"?\.$')
UP_RX = re.compile(r"^(Iti )?(.*?) upeto hoti(…pe…| samupeto upāgato samupāgato upapanno sampanno) samannāgato\.$")
TOPIC_RX = re.compile(r'^"?(.+?)"?(n?)ti\.$')
ADH_RX = re.compile(r"^(Chandaṃ|Vīriyaṃ|Cittaṃ|Vīmaṃsaṃ) ce bhikkhu adhipatiṃ karitvā labhati samādhiṃ, labhati "
                    r"cittassekaggataṃ( \[cittassa ekaggataṃ \(sī\. syā\.\)\])? – ayaṃ vuccati \"(\S+)samādhi\"\.$")
ITI_RX = re.compile(r"^Iti ayañca (\S+)samādhi, ime ca padhānasaṅkhārā(\.|; tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā "
                    r"\1samādhipadhānasaṅkhārotveva saṅkhyaṃ gacchati\.)$")
TADEK_RX = re.compile(r"^Tadekajjhaṃ (abhisaññahitvā|abhisaññūhitvā) abhisaṅkhipitvā (\S+)samādhipadhānasaṅkhārotveva "
                      r"saṅkhyaṃ( \[saṅkhaṃ \(sī\.\)\])? gacchati\.$")
RECKONED = "chúng được tính{v} là “{x}”"            # …otveva saṅkhyaṃ gacchati (termbase saṅkhyaṃ gacchati «được tính»)


def topic_key(raw):
    """«Anupassī» / «vineyya loke abhijjhādomanassa» + «n» -> TOPICS key"""
    m = TOPIC_RX.match(raw + ("." if not raw.endswith(".") else ""))
    assert m, raw
    t, n = m.groups()
    return low(t) + ("ṃ" if n else "")


def topic_run(s):
    """«Anupassīti…pe… viharatīti…pe… … vineyya loke abhijjhādomanassanti.» -> «Về từ “…”… về câu “…”:»"""
    parts = [x.strip() for x in s[:-1].split("…pe…")]
    vi = []
    for n, p in enumerate(parts):
        kind, v = TOPICS[topic_key(p + "." if p.endswith("ti") else p)]
        t = topic(kind, v)
        if n < len(parts) - 1:
            t = t[:-1]                                  # «:» only after the last
        vi.append(t if n == 0 else low(t))
    return "… ".join(vi)


def upeto(s):
    m = UP_RX.match(s)
    assert m, s
    iti, objs, mid = m.groups()
    ws = re.findall(r"(?:Imāya|Iminā|imāya|iminā) (?:ca )?(\S+?),?(?= |$)", objs)
    assert ws, s
    nouns = [f"{NOUN[DEM[w]]} này" for w in ws]
    obj = nouns[0] if len(nouns) == 1 else ", ".join(nouns[:-1]) + " và " + nouns[-1]
    verbs = UPETO_PE if mid == "…pe…" else UPETO
    return f"{'Như vậy, ' if iti else ''}{'v' if iti else 'V'}ị ấy {verbs} {obj}."


def sentence(s, sid):
    """one Pāli sentence -> (Vietnamese, topic flag: the next sentence starts in lower case)"""
    if s in SENT:
        return SENT[s], False
    if s == "Pañcapi upādānakkhandhā loko – tattha katamā abhijjhā?":
        slip(f"^{sid} «Pañcapi upādānakkhandhā loko – tattha katamā abhijjhā?»: «Ayaṃ vuccati \"loko\".» of the "
             "parallels is missing and a dash joins the next question (translated as written, dash kept)")
        return f"{FIVE_LOKO} – {low(q(NOUN['abhijjhā']))}", False
    if s.startswith("Cattāro satipaṭṭhānā – "):
        return satip4(s), False
    if s.startswith("Cattāro sammappadhānā – idha bhikkhu "):
        return f"{SAMMAP4} – ở đây, {efforts(s[len('Cattāro sammappadhānā – idha bhikkhu '):-1], 'vị tỳ-khưu')}.", False
    if s.startswith("Cattāro iddhipādā – idha bhikkhu "):
        return iddhip4(s), False
    if s.startswith("So ") and EFFORT_P in s:
        return f"{cap(efforts(s[3:-1], 'vị ấy'))}.", False
    if s.startswith((SUPRA_P, TASSEVA_P)):
        return supra_sentence(s, sid), False
    if SCAN_RX.match(s):
        return scan(s), False
    m = THEN_RX.match(s)
    if m:
        side, loc = m.groups()
        return NIMITTA_THEN.format(t=f"{FIELD[loc][0]}{SIDE[side]}"), False
    m = EVAM_RX.match(s)
    if m:
        return f"Như vậy, {lives(m.group(1), 'ajjhattabahiddhā')}, {ARDENT}.", False
    m = HOW_RX.match(s)
    if m:
        side, loc = m.groups()
        return f"Và {lives(loc, (side or '').strip())} như thế nào?", False
    m = re.match(r"^Kathañca bhikkhu " + AIM_RX + " " + EFFORT_P + r"\?$", s)
    if m:
        return f"Và vị tỳ-khưu {EFFORT} {aim(m.group(1))} như thế nào?", False
    m = re.match(r"^Kathañca bhikkhu " + IP_ENDOWED_RX + r"\?$", s)
    if m:
        return f"Và vị tỳ-khưu tu tập {ip_endowed(m.group(1))} như thế nào?", False
    m = re.match(r"^Iti imesaṃ " + AIM_RX + " " + EFFORT_P + r"\.$", s)
    if m:
        return f"Như vậy, vị ấy {EFFORT} {aim(m.group(1), these=True)}.", False
    if s.startswith("Idha bhikkhu ") and " vedanaṃ " in s:
        return feel_sentence(s), False
    if s.startswith("Idha bhikkhu ") and " cittaṃ \"" in s:
        return mind_sentence(s), False
    if s.startswith(("Idha bhikkhu santaṃ", "Santaṃ")):
        return dh_sentence(s), False
    m = re.match(r"^Avasesā dhammā (\S+)sampayuttā\.$", s)
    if m:
        st = m.group(1)
        n = NOUN.get(st + "ṃ") or NOUN[st[:-1] + "o"]          # satipaṭṭhāna(ṃ) / chandiddhipād(o)
        return f"Các hiện tượng còn lại gắn liền với {n}.", False
    m = ADH_RX.match(s)
    if m:
        a, br, k = m.groups()
        assert k == {"Chandaṃ": "chanda", "Vīriyaṃ": "vīriya", "Cittaṃ": "citta", "Vīmaṃsaṃ": "vīmaṃsā"}[a], s
        v = " " + S.spell("Sī., Syā.", "cittassa ekaggataṃ") if br else ""
        return (f"Nếu vị tỳ-khưu lấy {ADHIPATI[a]} {pi1('làm yếu tố chủ đạo')} mà đạt được định tâm, đạt được "
                f"{ONE_POINT}{v} – {CALLED} “{samadhi_n(k)}”."), False
    m = ITI_RX.match(s)
    if m:
        k, tail = m.groups()
        out = f"Như vậy, đây là {samadhi_n(k)} và đây là {NOUN['padhānasaṅkhārā']}"
        if tail == ".":
            return out + ".", False
        return f"{out}; {low(TOGETHER)}, {RECKONED.format(v='', x=sps(k))}.", False
    m = TADEK_RX.match(s)
    if m:
        verb, k, br = m.groups()
        v = " " + S.spell("Sī.", "saṅkhaṃ") if br else ""
        return f"{cap(TOGETHER)}, {RECKONED.format(v=v, x=sps(k))}.", False
    m = re.match(r'^Tena vuccati "(.+?)"(n?)ti\.$', s)
    if m:
        t = low(m.group(1)) + ("ṃ" if m.group(2) else "")
        return f"{TENA} “{TENA_T[t]}”.", False
    m = re.match(r'^(?:Ayaṃ|Idaṃ) vuccati "(\S+)"\.$', s)
    if m:
        return f"{cap(CALLED)} “{NOUN[m.group(1)]}”.", False
    m = UP_RX.match(s)
    if m:
        return upeto(s), False
    m = Q_RX.match(s)
    if m:
        name, br = m.groups()
        if br:
            assert br == " [katamaṃ ātāpaṃ (sabbattha)]", br
            return f"{S.TATTHA} {NOUN[name]} {S.reading('mọi bản', 'katamaṃ ātāpaṃ')} {S.IS_WHAT}", False
        return q(NOUN[name]), False
    m = A_RX.match(s)
    if m:
        body, pron, _, qt, name = m.groups()
        frame = CALLED_PL if pron == "ime" else CALLED
        if not qt:
            slip(f"^{sid} «… vuccati {name}» without quotation marks: kept without “ ”")
            return f"{body_vi(body)} – {frame} {NOUN[name]}.", False
        return f"{body_vi(body)} – {frame} “{NOUN[name]}”.", False
    if "…pe…" in s and re.match(r'^[^?]*n?ti\.$', s) and s.count("ti…pe…") >= 1:
        return topic_run(s), True
    m = TOPIC_RX.match(s)
    if m:
        kind, v = TOPICS[topic_key(s)]
        return topic(kind, v), True
    raise KeyError((sid, s))


LINE_FIX = [  # (bad, good, slip note): source slips rendered as meant / ignored spacing
    ("maggariyāpannaṃ", "maggapariyāpannaṃ", "^2-459 «maggariyāpannaṃ» for maggapariyāpannaṃ (spelling slip, rendered "
                                             "as meant «nằm trong con đường»)"),
    ("viññāṇakhandho", "viññāṇakkhandho", "^2-443 «viññāṇakhandho» (single k; viññāṇakkhandho elsewhere, both in the "
                                          "termbase «khối thức»): same Vietnamese"),
    ("Tathābhūtasa ", "Tathābhūtassa ", "^2-450 «Tathābhūtasa» for Tathābhūtassa (spelling slip, rendered as meant)"),
    ("labhati samādhiṃ labhati", "labhati samādhiṃ, labhati", "^2-435, 438, 441 «labhati samādhiṃ labhati "
                                                              "cittassekaggataṃ»: the comma of ^2-432 missing "
                                                              "(added, same Vietnamese)"),
    ("Siyā vipākā siyā", "Siyā vipākā, siyā", "^2-388 «Siyā vipākā siyā vipākadhammadhammā»: comma missing (added)"),
    ("sāsavācātipi", "sāsavā cātipi", "^2-389 «sāsavācātipi» written as one word (= sāsavā cātipi)"),
    ("āsavasampayuttācātipi", "āsavasampayuttā cātipi",
     "^2-389 «āsavasampayuttācātipi» written as one word (= āsavasampayuttā cātipi)"),
]


def def_line(ln, sid):
    if ln.endswith('samannāgato"ti'):
        slip(f"^{sid} «…samannāgato\"ti» without the final full stop: rendered with it")
        ln += "."
    if " …pe…" in ln:
        slip(f"^{sid}: a space before «…pe…» (ignored)")
        ln = ln.replace(" …pe…", "…pe…")
    out, lower_next = [], False
    for s in SPLIT_RX.split(ln):
        v, tp = sentence(s, sid)
        out.append(low(v) if lower_next else v)
        lower_next = tp
    assert not lower_next, ln
    return " ".join(out)


# =========================================================================== Pañhāpucchaka
# The question sections of ch. 7-9 have no subject (said of all four) except some ch. 9 dyads; «na vattabbā X ti»
# stands without the dash of chapters 1-5, so the Vietnamese has none («không nên nói rằng “…”»). A predicate said of
# all four without «siyā» takes «Đều …» as in ch. 5 («Đều có điều kiện.»); a sentence opening with «siyā» opens with
# «Đôi khi …».
GROUPS79 = {"Catunnaṃ satipaṭṭhānānaṃ": ("Trong bốn sự thiết lập tỉnh thức", "bao nhiêu sự thiết lập"),
            "Catunnaṃ sammappadhānānaṃ": ("Trong bốn nỗ lực đúng đắn", "bao nhiêu nỗ lực"),
            "Catunnaṃ iddhipādānaṃ": ("Trong bốn nền tảng thần thông", "bao nhiêu nền tảng")}
KENACI_NOUN = {7: "sự thiết lập tỉnh thức", 8: "nỗ lực đúng đắn", 9: "nền tảng thần thông"}
SUBJ79 = {"vīmaṃsiddhipādo": (IPN["vīmaṃs"], "s"), "cittiddhipādo": (IPN["citt"], "s"),
          "tayo iddhipādā": (f"ba {IP}", "p")}
SUBJ_RX = re.compile(r"^(vīmaṃsiddhipādo|cittiddhipādo|tayo iddhipādā|Vīmaṃsiddhipādo|Cittiddhipādo|Tayo iddhipādā) "
                     r"(.*)$")
ALL = "Đều"                                          # subjectless predicate said of all four (ch. 5 «Đều …»)
SIYA, PRON = K1.SIYA, K1.PRON                        # «đôi khi»; {"s": "nó", "p": "chúng"}
NV79 = "không nên nói"                               # na vattabbā (termbase «nên nói»), no dash in ch. 7-9
LOCAL79 = {"na maggādhipati": "không lấy con đường làm yếu tố chủ đạo"}   # negated sibling of maggādhipati
PLK79 = dict(K23.PLK)
for _k in list(K23.LOCAL) + list(LOCAL79):
    PLK79.setdefault(K1.pali_plural(_k), _k)
PANHA_SENT = {"Kusalāyeva": "Chỉ là thiện"}           # termbase Kusalāyeva «chỉ là thiện»


def pred79(word, num):
    """a matrix predicate (Pāli, lower case) said of a plural / singular subject -> Vietnamese"""
    key = PLK79[word] if num == "p" else word
    if key in LOCAL79:
        return LOCAL79[key]
    if key in K23.LOCAL:
        return K23.get(key)
    return K1.pred(key)


def strip_ti(w):
    """«hetū ceva sahetukā cāti» / «maggahetukātipi» / «uppādinoti» -> the quoted predicate"""
    for suf in ("tipi", "ti"):
        if w.endswith(suf):
            w = w[:-len(suf)]
            break
    else:
        raise ValueError(w)
    return re.sub(r"cā$", "ca", w)


def panha_parse(s):
    toks = re.split(r"(, |…pe… )", s)
    units, seps = toks[0::2], [""] + toks[1::2]
    cl = []
    for u, sep in zip(units, seps):
        subj = None
        m = SUBJ_RX.match(u)
        if m:
            subj, u = low(m.group(1)), m.group(2)
        mv = re.match(r"^(siyā |Siyā )?[Nn]a vattabb[oā] (.*)$", u)
        if mv:
            cl.append(dict(kind="nv", siya=bool(mv.group(1)), items=[strip_ti(mv.group(2))], subj=subj, sep=sep))
            continue
        if cl and cl[-1]["kind"] == "nv" and subj is None and sep == ", " and u.endswith("tipi"):
            cl[-1]["items"].append(strip_ti(u))
            continue
        siya = u.startswith(("siyā ", "Siyā "))
        cl.append(dict(kind="pred", siya=siya, word=low(u[5:] if siya else u), subj=subj, sep=sep))
    return cl


def panha_sentence(s, ch):
    """one question-section sentence (without its final full stop)"""
    if s.endswith("Araṇāti"):                        # the closing «ti» of the whole section
        s = s[:-2]
    if s in PANHA_SENT:
        return PANHA_SENT[s]
    if s == "Kenaci viññeyyā, kenaci na viññeyyā":
        return f"{ALL} {K1.KENACI.replace('những khối', f'những {KENACI_NOUN[ch]}')}"
    out, cur, num, topic_open = "", None, "p", False
    for i, c in enumerate(panha_parse(s)):
        if c["subj"]:
            cur = c["subj"]
            num = SUBJ79[cur][1]
        sv = SUBJ79[cur][0] if cur else None
        sep = "" if i == 0 else ("…" if c["sep"].startswith("…pe…") else ",")
        if c["kind"] == "nv":
            quoted = ", hay ".join(f"rằng “{pred79(k, num)}”" for k in c["items"])
            if c["siya"]:
                text = f"{SIYA} {NV79} {quoted}"
            elif c["subj"] or i == 0:
                text = f"Về {sv} thì {NV79} {quoted}" if sv else f"{cap(NV79)} {quoted}"
                topic_open = True
            else:                                    # «…, siyā Y, na vattabbā Z-ti» (no siyā, no subject)
                text, sep = f"{NV79} {quoted}", ";"
        else:
            v = pred79(c["word"], num)
            v = f"{SIYA} {v}" if c["siya"] else v
            if c["subj"]:
                text = f"{cap(sv)} {v}"
                topic_open = False
            elif i == 0:
                text = cap(v) if c["siya"] or cur else f"{ALL} {v}"
            elif topic_open:
                text, sep = f"{PRON[num]} {v}", ";"
                topic_open = False
            else:
                text = v
        if i and c["subj"]:
            text = "còn " + low(text)                # a second subject in the same sentence: «…, còn …»
        out += (sep + " " if i else "") + text
    return out


def panha_line(p, sid, ch):
    for bad, good, nt in LINE_FIX:
        if bad in p:
            p = p.replace(bad, good)
            slip(nt)
    out = []
    for s in re.split(r"(?<=\.) (?=[A-ZĀĪŪṬÑṆḌḶṂ])", p):
        assert s.endswith("."), s
        out.append(panha_sentence(s[:-1], ch) + ".")
    return " ".join(out)


def panha_question(p):
    """Catunnaṃ satipaṭṭhānānaṃ kati kusalā, … kati araṇā? (as K23.panha_question)"""
    m = re.match(r"^(.*?) (kati .*)\?$", p)
    grp, body = m.groups()
    head, kati = GROUPS79[grp]
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


# =========================================================================== build and render
FOREIGN = re.compile(r"[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶfjwzFJWZ]")


def dashes(s):
    return s.count("–") + s.count("—")


def check_line(sid, p, v):
    assert dashes(p) == dashes(v), (sid, "dash count", dashes(p), dashes(v), v[:160])
    assert ":-" not in v and "—" not in v and "…." not in v, (sid, v[:160])
    body = re.sub(r"\[[^\]]*\]", "", v)
    assert not FOREIGN.search(body), (sid, FOREIGN.search(body).group(0), v[:200])
    assert "  " not in v and not v.endswith(" "), (sid, v[:160])
    assert v.count("“") == v.count("”"), (sid, "quotes", v[:200])
    assert "là là" not in v, (sid, v[:160])
    if not p.startswith("#"):
        assert v[-1] in ".?", (sid, v[-40:])
        assert p.endswith("?") == v.endswith("?"), (sid, v[-40:])


def heading(ln, ch):
    lvl, text = ln.split(" ", 1)
    t = {CH_NAME[ch]: S.CH_HEADINGS[CH_NAME[ch]], "Tikaṃ": K1.TIKA_H, "Dukaṃ": K1.DUKA_H}
    t.update(S.SEC_HEADINGS)
    t.update(SUBHEAD)
    return f"{lvl} {t[text]}"


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
            elif section == "Pañhāpucchakaṃ" and not ln.startswith("Cattāro"):
                vi.append(panha_question(ln) if ln.endswith("?") else panha_line(ln, sid, ch))
            else:
                for bad, good, nt in LINE_FIX:
                    if bad in ln:
                        ln = ln.replace(bad, good)
                        slip(nt)
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


# =========================================================================== pi-1 / pi-2 checks
def check_pi1():
    """every string marked pi1() must occur in the approved pi-1 Vietnamese rails (first letter either case)"""
    text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI1_VI.glob("*.md")))
    missing = [s for s in PI1_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    return len(PI1_USED)


def check_pi2():
    """every string marked pi2() must occur in the approved earlier pi-2 Vietnamese chapters (1-6)"""
    files = ["1-khandhavibhango.md", "3-dhatuvibhango.md", "4-saccavibhango.md", "5-indriyavibhango.md",
             "6-paticcasamuppadavibhango.md"]
    text = "\n".join((S.OUT / f).read_text(encoding="utf-8") for f in files)
    missing = [s for s in PI2_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    return len(PI2_USED)


# =========================================================================== notes
def notes_md():
    a1 = AIM_ORDER[0]
    L = ["# pi-2 Vietnamese rails: new formulas of chapters 7-9 (^2-7-0 … ^2-465)", "",
         "Generated by build_rails_7_9_vi.py; import it instead of retyping. Strings already in vi-rails-formulas.md "
         "(sample), notes-1.md, notes-2-3.md, notes-4-5.md or notes-6.md are not repeated (the satipaṭṭhāna and "
         "right-effort formulas come from ch. 4 ^2-205, the supramundane opener from ch. 4, the Tasseva … vipākaṃ "
         "opener from ch. 6). Format: Pāli = tiếng Việt.", "",
         "## Headings and closing labels", "",
     ] + [f"### {n} = ### {S.CH_HEADINGS[n]}; closing «{n} niṭṭhito.» = «{S.CH_HEADINGS[n]} {K1.DONE}.»"
          for n in CH_NAME.values()] + [
         f"##### {k} = ##### {v} (closing label «{k}.» = «{v}.»)" for k, v in SUBHEAD.items()] + [
         "", "## Topics and closings", "",
         f"<one Pāli word>ti. (topic) = {TOPIC_W.format(x='…')} (next sentence in lower case)",
         f"<phrase>ti. (topic) = {TOPIC_C.format(x='…')} (ch. 6 frame)",
         "Xti…pe… Yti…pe… Zti. = Về từ “x”… về từ “y”… về câu “z”:",
     ] + [f"{k}ti = {topic(*v)}" for k, v in TOPICS.items()] + [
         f"Tena vuccati \"X\"ti. = {TENA} “x”. (ch. 6)",
     ] + [f"Tena vuccati \"{k}\"ti. = {TENA} “{v}”." for k, v in TENA_T.items() if "samādhipadhāna" in k] + [
         f"Imāya / Iminā X upeto hoti samupeto upāgato samupāgato upapanno sampanno samannāgato. = Vị ấy {UPETO} x "
         f"này.",
         f"Iminā X upeto hoti…pe… samannāgato. = Vị ấy {UPETO_PE} x này.",
         f"Iti iminā ca X-ena, iminā ca samādhinā, iminā ca padhānasaṅkhārena upeto hoti … = Như vậy, vị ấy {UPETO} x "
         f"này, định tâm này và {PS} này.",
         f"– ayaṃ / idaṃ vuccati \"X\". = – {CALLED} “x”. ; – ime vuccanti \"X\". = – {CALLED_PL} “x”.",
         "", "## Satipaṭṭhāna", "",
         f"Cattāro satipaṭṭhānā – idha bhikkhu kāye kāyānupassī viharati, … = {satip4(SATIP4_P[1])}",
         f"Cattāro satipaṭṭhānā – idha bhikkhu kāye kāyānupassī viharati ātāpī … = {satip4(SATIP4_P[2])}",
         f"(side) kāye kāyānupassī viharati = đối với thân(side), vị tỳ-khưu / vị ấy sống quán sát thân; sides: "
         f"ajjhattaṃ ={SIDE['ajjhattaṃ']}, bahiddhā ={SIDE['bahiddhā']}, ajjhattabahiddhā ={SIDE['ajjhattabahiddhā']}",
         "vedanāsu / citte / dhammesu = đối với các cảm giác / tâm / các hiện tượng … sống quán sát các cảm giác / tâm / "
         "các hiện tượng",
         f"Kathañca bhikkhu (side) kāye kāyānupassī viharati? = Và {lives('kāye', 'ajjhattaṃ')} như thế nào?",
         f"Evaṃ bhikkhu ajjhattabahiddhā kāye kāyānupassī viharati ātāpī … = Như vậy, "
         f"{lives('kāye', 'ajjhattabahiddhā')}, {ARDENT}.",
         f"Idha bhikkhu ajjhattaṃ kāyaṃ uddhaṃ pādatalā … paccavekkhati – \"atthi imasmiṃ kāye kesā … mutta\"nti. = Ở "
         f"đây, vị tỳ-khưu quán xét thân{SIDE['ajjhattaṃ']}, {SCAN} – “{IN_BODY['atthi imasmiṃ kāye']} …”.",
         f"atthi imasmiṃ kāye / atthissa kāye = {IN_BODY['atthi imasmiṃ kāye']} / {IN_BODY['atthissa kāye']}",
         f"So taṃ nimittaṃ āsevati bhāveti bahulīkaroti svāvatthitaṃ vavatthapeti. = {NIMITTA}",
         f"So taṃ nimittaṃ āsevitvā … bahiddhā kāye cittaṃ upasaṃharati. = "
         f"{NIMITTA_THEN.format(t='thân' + SIDE['bahiddhā'])}",
         f"sukhaṃ vedanaṃ vedayamāno \"sukhaṃ vedanaṃ vedayāmī\"ti pajānāti = khi cảm nhận cảm giác dễ chịu, vị ấy "
         f"hiểu rõ: “Tôi đang cảm nhận cảm giác dễ chịu”",
         "sukhaṃ vedanaṃ vedayamānaṃ \"… vedayatī\"ti pajānāti = về người đang cảm nhận cảm giác dễ chịu, vị ấy hiểu "
         "rõ: “Người ấy đang cảm nhận cảm giác dễ chịu”",
         "sukhaṃ vedanaṃ \"sukhā vedanā\"ti pajānāti = vị ấy hiểu rõ cảm giác dễ chịu là “cảm giác dễ chịu”",
         f"sāmisaṃ / nirāmisaṃ vā X vedanaṃ = hoặc … cảm giác X{FEEL_Q['sāmisaṃ']} / cảm giác "
         f"X{FEEL_Q['nirāmisaṃ']}",
         "sarāgaṃ vā cittaṃ \"sarāgaṃ me citta\"nti pajānāti = (hoặc) khi tâm có tham đắm, vị ấy hiểu rõ: “Tâm tôi có "
         "tham đắm”; vāssa … \"sarāgamassa citta\"nti = khi tâm của người ấy có tham đắm, … “Tâm của người ấy có tham "
         "đắm”; \"sarāgaṃ citta\"nti = … “Tâm có tham đắm”",
     ] + [f"{k} (cittaṃ) = {v}" for k, v in MIND.items()] + [
         "santaṃ vā ajjhattaṃ X \"atthi me ajjhattaṃ X\"ti pajānāti = khi có x ở nơi bản thân, vị ấy hiểu rõ: “Ở nơi "
         "bản thân tôi có x”; asantaṃ … natthi … = hoặc khi không có x …: “… không có x”",
         "santaṃ vāssa X \"atthissa X\"ti = khi người ấy có x, …: “Người ấy có x”; santaṃ vā X \"atthi X\"ti = khi có "
         "x, …: “Có x”",
     ] + [f"yathā ca … X … {k} tañca pajānāti = vị ấy cũng hiểu rõ {v.format(x='x', p='(chưa sinh khởi / đã sinh khởi / đã được dứt bỏ)')}"
          for k, v in EVENT.items()] + [
         "hindrances / awakening factors: " + "; ".join(f"{k}aṃ = {v}" for k, v in DH_NOUN.items()),
         f"Sveva kāyo loko. … Teva dhammā loko. = " + " / ".join(LOKO.values()),
         f"Pañcapi upādānakkhandhā loko. = {FIVE_LOKO}.",
         f"{VINITA_P} = {VINITA}",
         f"Iriyati vattati pāleti yapeti yāpeti carati viharati. = {VIHARATI}",
         f"Avasesā dhammā satipaṭṭhānasampayuttā. = Các hiện tượng còn lại gắn liền với {NOUN['satipaṭṭhānaṃ']}.",
         "", "## Abhidhamma openers", "",
         f"Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ … dandhābhiññaṃ kāye kāyānupassī, yā tasmiṃ samaye … = "
         f"{MONK_WHEN} {SUPRA_CORE}, {contemplating('kāye')}, {WHAT_AT_TIME} …",
         f"… dandhābhiññaṃ, tasmiṃ samaye phasso hoti…pe… avikkhepo hoti. Ime dhammā kusalā. = {MONK_WHEN} {SUPRA} "
         f"{CONTACT_PE}. {cap(ARE_KUSALA)}.",
         f"Tasseva … suññataṃ kāye kāyānupassī, yā tasmiṃ samaye … = {TASSEVA}, {contemplating('kāye')}, "
         f"{WHAT_AT_TIME} …",
         f"… dandhābhiññaṃ, tasmiṃ samaye <right effort> = {MONK_WHEN} {SUPRA} vị ấy {EFFORT} …",
         f"… dandhābhiññaṃ, tasmiṃ samaye X…samannāgataṃ iddhipādaṃ bhāveti. = {MONK_WHEN} {SUPRA} vị ấy tu tập "
         f"{ip_endowed('chanda')}.",
         "", "## Right efforts", "",
         f"Cattāro sammappadhānā – idha bhikkhu … (full) = {SAMMAP4} – ở đây, {efforts(EFF_FULL, 'vị tỳ-khưu')}.",
         f"Cattāro sammappadhānā – idha bhikkhu … pahānāya…pe… uppādāya…pe… … = {SAMMAP4} – ở đây, "
         f"{efforts(EFF_PE, 'vị tỳ-khưu')}.",
         f"Kathañca bhikkhu {a1} chandaṃ janeti …? = Và vị tỳ-khưu {EFFORT} {aim(a1)} như thế nào?",
         f"Iti imesaṃ {a1} chandaṃ janeti … = Như vậy, vị ấy {EFFORT} {aim(a1, True)}.",
     ] + [f"{k} = {v.format(t='')} (Iti imesaṃ …: {v.format(t=' này')})" for k, v in AIM.items()] + [
         f"Tattha katame anuppannā pāpakā akusalā dhammā? = {q(NOUN['anuppannā pāpakā akusalā dhammā'])}",
         f"Tīṇi akusalamūlāni – lobho, doso, moho. = {ROOTS_A}. (pi-1 ^1-986)",
         f"Tīṇi kusalamūlāni – alobho, adoso, amoho. = {ROOTS_K}. (pi-1 ^1-985)",
         f"Tadekaṭṭhā ca kilesā. = {cap(TADEKATTHA)}. (pi-1)",
         f"Taṃsampayutto vedanākkhandho … viññāṇakkhandho, taṃsamuṭṭhānaṃ kāyakammaṃ vacīkammaṃ manokammaṃ = "
         f"{BODY_CAP[list(BODY_CAP)[0]]} (pi-1)",
         f"Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti nibbatteti abhinibbatteti. = {CHANDA_VERB.format(v='')}",
         f"[uṭṭhāpeti samuṭṭhāpeti (syā.) evamuparipi] = {CHANDA_VAR.strip()}",
         f"Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti. = {VIRIYA_VERB}",
         f"Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti. = {CITTA_VERB}",
         f"Yā ṭhiti so asammoso, … yā bhāvanā sā pāripūrī. = {THITI_CHAIN}",
         f"Avasesā dhammā sammappadhānasampayuttā. = Các hiện tượng còn lại gắn liền với {NOUN['sammappadhānaṃ']}.",
         "", "## Bases of power", "",
         f"Cattāro iddhipādā – idha bhikkhu chandasamādhi… iddhipādaṃ bhāveti, … = {iddhip4(IDDHIP4_P[0])}",
         f"Cattāro iddhipādā – idha bhikkhu …, vīriyasamādhi…pe… cittasamādhi…pe… … = {iddhip4(IDDHIP4_P[1])}",
         f"Cattāro iddhipādā – chandiddhipādo, vīriyiddhipādo, cittiddhipādo, vīmaṃsiddhipādo. = "
         f"{SENT['Cattāro iddhipādā – chandiddhipādo, vīriyiddhipādo, cittiddhipādo, vīmaṃsiddhipādo.']}",
     ] + [f"{k}samādhi / {k}samādhipadhānasaṅkhāro / {k}samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ = "
          f"{samadhi_n(k)} / {sps(k)} / {ip_endowed(k)}" for k in SAMADHI_BY] + [
         f"padhānasaṅkhāro / padhānasaṅkhārā = {PS} / {NOUN['padhānasaṅkhārā']}",
         f"Kathañca bhikkhu chandasamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti? = Và vị tỳ-khưu tu tập "
         f"{ip_endowed('chanda')} như thế nào?",
         f"Chandaṃ ce bhikkhu adhipatiṃ karitvā labhati samādhiṃ, labhati cittassekaggataṃ – ayaṃ vuccati "
         f"\"chandasamādhi\". = Nếu vị tỳ-khưu lấy {ADHIPATI['Chandaṃ']} làm yếu tố chủ đạo mà đạt được định tâm, đạt "
         f"được {ONE_POINT} – {CALLED} “{samadhi_n('chanda')}”.",
         "Vīriyaṃ / Cittaṃ / Vīmaṃsaṃ ce bhikkhu adhipatiṃ karitvā = " + " / ".join(
             f"lấy {ADHIPATI[k]} làm yếu tố chủ đạo" for k in ("Vīriyaṃ", "Cittaṃ", "Vīmaṃsaṃ")),
         f"Ime vuccanti \"padhānasaṅkhārā\". = {SENT[IME_PS_P]}",
         f"Iti ayañca chandasamādhi, ime ca padhānasaṅkhārā. = Như vậy, đây là {samadhi_n('chanda')} và đây là "
         f"{NOUN['padhānasaṅkhārā']}.",
         f"Tadekajjhaṃ abhisaññahitvā (abhisaññūhitvā) abhisaṅkhipitvā chandasamādhipadhānasaṅkhārotveva saṅkhyaṃ "
         f"gacchati. = {cap(TOGETHER)}, {RECKONED.format(v='', x=sps('chanda'))}.",
         f"[saṅkhaṃ (sī.)] = {S.spell('Sī.', 'saṅkhaṃ')}",
         f"Yā tesaṃ dhammānaṃ iddhi samiddhi … upasampadā. = {IDDHI_DEF}",
         f"Tathābhūtassa vedanākkhandho, … viññāṇakkhandho. = {cap(KH4)} {TATHA}.",
         f"Tathābhūtassa phasso…pe… paggāho avikkhepo. = {SENT['Tathābhūtassa phasso…pe… paggāho avikkhepo.']}",
         f"Te dhamme āsevati bhāveti bahulīkaroti. = {TE_DHAMME}",
         f"Avasesā dhammā chandiddhipādasampayuttā. = Các hiện tượng còn lại gắn liền với {IPN['chand']}.",
         "", "## Definitions (answer bodies, after «Điều mà là»)", "",
     ] + [f"{k} = {v}" for k, v in BODY.items()] + [
         "yo / yā / yaṃ tasmiṃ samaye <body> (after an opener) = " + WHAT_AT_TIME + " <body>",
         "", "## Question sections (no subject: said of all four)", "",
         "Catunnaṃ satipaṭṭhānānaṃ / sammappadhānānaṃ / iddhipādānaṃ kati …? = " + " / ".join(
             f"{a}, {b} …?" for a, b in GROUPS79.values()),
         f"<predicate>. (no siyā) = {ALL} <predicate>. (ch. 5)",
         f"Siyā X, siyā Y. = {cap(SIYA)} x, {SIYA} y.",
         f"Na vattabbā X-ti, Y-tipi. = {cap(NV79)} rằng “x”, hay rằng “y”. (no dash: none in the Pāli)",
         f"Na vattabbā X cāti, Y. = {cap(NV79)} rằng “x”; {PRON['p']} y.",
         f"…, na vattabbā X-ti (mid-sentence) = …; {NV79} rằng “x”",
         f"Kusalāyeva. = {PANHA_SENT['Kusalāyeva']}.",
         f"Kenaci viññeyyā, kenaci na viññeyyā. = {ALL} " + K1.KENACI.replace("những khối", "những <noun>") + ".",
         f"na maggādhipatino = {LOCAL79['na maggādhipati']}",
         "Vīmaṃsiddhipādo / Cittiddhipādo / Tayo iddhipādā (subjects) = " + " / ".join(
             cap(v[0]) for v in SUBJ79.values()),
         f"X …, tayo iddhipādā … (second subject) = X …, còn ba {IP} …; … na vattabbā … = …, còn về x thì {NV79} …",
    ]
    return unicodedata.normalize("NFC", "\n".join(L) + "\n")


IME_PS_P = 'Ime vuccanti "padhānasaṅkhārā".'
SATIP4_P = [None,
            ("Cattāro satipaṭṭhānā – idha bhikkhu kāye kāyānupassī viharati, vedanāsu vedanānupassī viharati, citte "
             "cittānupassī viharati, dhammesu dhammānupassī viharati."),
            ("Cattāro satipaṭṭhānā – idha bhikkhu kāye kāyānupassī viharati ātāpī sampajāno satimā vineyya loke "
             "abhijjhādomanassaṃ, vedanāsu vedanānupassī viharati ātāpī sampajāno satimā vineyya loke "
             "abhijjhādomanassaṃ, citte cittānupassī viharati ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ, "
             "dhammesu dhammānupassī viharati ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ.")]
EFF_FULL = ", ".join(f"{a} {EFFORT_P}" for a in AIM_ORDER)
EFF_PE = f"{AIM_ORDER[0]} {EFFORT_P}, {AIM_ORDER[1]}…pe… {AIM_ORDER[2]}…pe… {AIM_ORDER[3]} {EFFORT_P}"
IDDHIP4_P = [("Cattāro iddhipādā – idha bhikkhu " + ", ".join(
                 f"{k}samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti" for k in SAMADHI_BY) + "."),
             ("Cattāro iddhipādā – idha bhikkhu chandasamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti, "
              "vīriyasamādhi…pe… cittasamādhi…pe… vīmaṃsāsamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti.")]


def main():
    for ch, part in PARTS.items():
        pali, h = build(ch)
        text = render(pali, h)
        (S.OUT / part).write_bytes(text.encode("utf-8"))
        print(f"wrote {part}: {len(h)} segments")
    n1, n2 = check_pi1(), check_pi2()
    NOTES_PATH.write_bytes(notes_md().encode("utf-8"))
    print(f"pi-1 strings checked: {n1}; pi-2 strings checked: {n2}; notes-7-9.md written")
    for s in SLIPS:
        print("slip:", s)
    for s in MISFITS:
        print("misfit:", s)


if __name__ == "__main__":
    main()
