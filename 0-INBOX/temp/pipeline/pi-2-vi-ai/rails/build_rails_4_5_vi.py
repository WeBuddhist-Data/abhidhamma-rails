"""Builder for the Vietnamese rails translation of pi-2 (Vibhaṅga, «Phân tích các hiện tượng», plain audience),
chapters 4 (Saccavibhaṅgo, «Phân tích các sự thật») and 5 (Indriyavibhaṅgo, «Phân tích các năng lực»).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/4-saccavibhango.md   (^2-4-0 … ^2-218)
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/5-indriyavibhango.md  (^2-5-0 … ^2-224)
  0-INBOX/temp/pipeline/pi-2-vi-ai/rails/notes-4-5.md   (new recurring formulas, Pāli = tiếng Việt)

Translated fresh from the Pāli with the locked pi-2 termbase. Shared strings are imported read-only from the approved
sample builder (S), the chapter-1 builder (K1: matrix items, chain(), fixed strings) and the chapters 2-3 builder
(K23: the question-section sentence engine, dh_pe(), the pi-1 feeling definitions); their tables are extended only in
memory, here. Passages that repeat the Dhammasaṅgaṇī reuse the approved pi-1 Vietnamese rails (every such string is
marked pi1() and asserted to occur there by check_pi1()). Every Vietnamese line is checked against its Pāli line for
the dash count and for left-over Pāli letters. Importing this module writes nothing.

usage: python -I -X utf8 build_rails_4_5_vi.py
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

PI1_VI = S.ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
NOTES_PATH = RAILS / "notes-4-5.md"
cap, low, q, called_q = S.cap, K1.low, K23.q, K23.called_q
TATTHA, IS_WHAT, CALLED, CALLED_PL = S.TATTHA, S.IS_WHAT, S.CALLED_SG, S.CALLED_PL
WHICH = K23.WHICH                                   # Yaṃ / Yā / Yo … (definition) «Điều mà là»
SLIPS = []          # source slips met while building (reported)
MISFITS = []        # termbase gaps / misfits / sense choices (reported)
PI1_USED = []       # strings taken from the approved pi-1 Vietnamese rails (checked by check_pi1)


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


def vlist(items):
    """«a, b và c»; members that contain a comma are separated by «;» (pi-1 ^1-583 layout)"""
    if len(items) == 1:
        return items[0]
    if any("," in x for x in items):
        return "; ".join(items[:-1]) + "; và " + items[-1]
    return ", ".join(items[:-1]) + " và " + items[-1]


# =========================================================================== chapter 4: names
DUKKHA = "khổ đau"                  # dukkhaṃ, suffering in general (termbase dukkhaṃ sense 2; 'dukkhaṃ ariyasaccaṃ')
PAIN = "sự khó chịu"                # dukkhaṃ, bodily pain (^2-196; user decision: pain = «sự khó chịu»)
SAMUDAYA = "sự phát sinh của khổ đau"           # dukkhasamudayo / dukkhasamudayaṃ (termbase)
NIRODHA = "sự chấm dứt khổ đau"                 # dukkhanirodho / dukkhanirodhaṃ (termbase)
PATIPADA = "cách thực hành dẫn đến sự chấm dứt khổ đau"   # dukkhanirodhagāminī paṭipadā (paṭipadā «cách thực hành»,
                                                          # gāminī «dẫn đến»)
NOBLE = "sự thật cao quý"                       # ariyasaccaṃ (termbase)
ARIYA = {"dukkha": f"{NOBLE} về {DUKKHA}", "samudaya": f"{NOBLE} về {SAMUDAYA}",
         "nirodha": f"{NOBLE} về {NIRODHA}", "magga": f"{NOBLE} về {PATIPADA}"}
TRUTH = {  # Dukkhasaccaṃ «sự thật về khổ đau» (termbase); the others built the same way from their members
    "Dukkhasaccaṃ": "Sự thật về khổ đau", "Samudayasaccaṃ": "Sự thật về sự phát sinh",
    "Nirodhasaccaṃ": "Sự thật về sự chấm dứt", "Maggasaccaṃ": "Sự thật về con đường"}
VAR_SAMUDAYA = S.spell("Syā.", "dukkhasamudayo")    # [dukkhasamudayo (syā.)]
VAR_NIRODHA = S.spell("Syā.", "dukkhanirodho")      # [dukkhanirodho (syā.)]
NOBLE4 = (f"Bốn {NOBLE} – {ARIYA['dukkha']}, {ARIYA['samudaya']}{{v1}}, {ARIYA['nirodha']}{{v2}}, "
          f"{ARIYA['magga']}.")                     # Cattāri ariyasaccāni – … (^2-189, ^2-215)
TRUTHS4 = f"Bốn sự thật – {DUKKHA}, {SAMUDAYA}, {NIRODHA}, {PATIPADA}."   # Cattāri saccāni – dukkhaṃ, … paṭipadā.


def stmt_q(x):
    """Tattha katamo appiyehi sampayogo dukkho? (a topic that is itself a statement) -> «Ở đây, thế nào là “X”?»"""
    return f"{TATTHA} thế nào là “{x}”?"


# =========================================================================== chapter 4: Suttantabhājanīya
SORROW5 = "sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng"   # sokaparidevadukkhadomanassupāyāsā
APPIYA = "gắn bó với những gì mình không yêu quý là khổ đau"     # appiyehi sampayogo dukkho
PIYA = "xa lìa những gì mình yêu quý là khổ đau"                 # piyehi vippayogo dukkho
YAMPI = "không đạt được điều mình mong cầu, điều đó cũng là khổ đau"   # yampicchaṃ na labhati tampi dukkhaṃ
UPA_KH = {a: f"{S.AGG[a]['k']} làm đối tượng cho sự bám víu" for a in S.FIVE}   # rūpupādānakkhandho … (termbase)
FIVE_UPA = "năm khối làm đối tượng cho sự bám víu"              # pañcupādānakkhandhā
BRIEF = f"nói tóm lại, {FIVE_UPA} là khổ đau"                    # saṃkhittena pañcupādānakkhandhā dukkhā
L190 = (f"{q(ARIYA['dukkha'])} Sự sinh cũng là {DUKKHA}, sự lão hóa cũng là {DUKKHA}, sự chết cũng là {DUKKHA}, "
        f"{SORROW5} cũng là {DUKKHA}, {APPIYA}, {PIYA}, {YAMPI}, {BRIEF}.")
EACH = "đối với từng chúng sinh trong từng loài chúng sinh"     # tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye
JATI = "sự sinh"                                                 # Jāti (termbase «sự sinh»)
JARA = "sự lão hóa"                                              # jarā
MARANA = "sự chết"                                               # maraṇaṃ
JATI_LIST = ("sự sinh, sự sinh ra, sự nhập thai, sự hình thành, sự xuất hiện của các khối, sự có được các lĩnh vực "
             "nhận biết")      # jāti sañjāti okkanti abhinibbatti khandhānaṃ pātubhāvo āyatanānaṃ paṭilābho
JARA_LIST = pi1("sự lão hóa, sự hao mòn, răng gãy rụng, tóc bạc, da nhăn nheo, sự suy giảm tuổi thọ, sự chín muồi "
                "của các năng lực")                              # pi-1 ^1-643
MARANA_LIST = ("sự chết, trạng thái lìa khỏi từng loài chúng sinh, sự tan rã, sự biến mất, sự tử vong, sự chết, "
               "sự qua đời, sự tan rã của các khối, sự bỏ lại thân xác, sự cắt đứt năng lực sống")
# tamhā tamhā sattanikāyā cuti cavanatā bhedo antaradhānaṃ maccu maraṇaṃ kālakiriyā khandhānaṃ bhedo kaḷevarassa
# nikkhepo jīvitindriyassupacchedo (cuti «sự chết», user decision aligned to pi-1; maraṇaṃ «sự chết», termbase)
AFFLICT = ("Ở người gặp phải tổn hại về người thân, hoặc gặp phải tổn hại về tài sản, hoặc gặp phải tổn hại về bệnh tật, "
           "hoặc gặp phải tổn hại về giới hạnh, hoặc gặp phải tổn hại về quan điểm, vướng phải tổn hại này hay tổn hại "
           "khác, gặp phải điều khổ đau này hay điều khổ đau khác, có")   # Ñāti «người thân», dhammena «điều»
# Ñātibyasanena vā phuṭṭhassa … aññataraññatarena byasanena samannāgatassa aññataraññatarena dukkhadhammena phuṭṭhassa
SOKA_LIST = ("sự sầu muộn, sự buồn rầu, trạng thái buồn rầu, nỗi sầu bên trong, nỗi sầu thấm sâu bên trong, sự héo "
             "hon của tâm, nỗi buồn, mũi tên sầu muộn")
PARIDEVA_LIST = ("sự kêu khóc, sự than khóc, hành động kêu khóc, hành động than khóc, trạng thái kêu khóc, trạng thái "
                 "than khóc, lời nói, lời lảm nhảm, lời lảm nhảm không ngớt, sự rên rỉ, hành động rên rỉ, trạng thái "
                 "rên rỉ " + S.spell("Syā.", "lālapo lālapanā lālapitattaṃ"))
UPAYASA_LIST = "sự phiền muộn, sự tuyệt vọng, trạng thái phiền muộn, trạng thái tuyệt vọng"
SOKA, PARIDEVA, DOMANASSA, UPAYASA = "sự sầu muộn", "sự than khóc", "nỗi buồn", "sự tuyệt vọng"
OBJ5 = S.OBJECTS5                                                # rūpā saddā gandhā rasā phoṭṭhabbā
L199 = (f"{stmt_q(APPIYA)} Ở đây, người nào có những {OBJ5} không đáng mong muốn, không đáng yêu mến, không đáng ưa "
        f"thích, hoặc có những người mong điều không lợi ích, mong điều không tốt lành, mong điều không thoải mái, mong điều "
        f"không an ổn cho người ấy; sự kết hợp, sự gần gũi, sự tụ hợp, sự hòa lẫn với những điều ấy – {CALLED} "
        f"“{APPIYA}”.")
L200 = (f"{stmt_q(PIYA)} Ở đây, người nào có những {OBJ5} đáng mong muốn, đáng yêu mến, đáng ưa thích, hoặc có "
        f"những người mong điều lợi ích, mong điều tốt lành, mong điều thoải mái, mong điều an ổn cho người ấy, như "
        f"mẹ, hay cha, hay anh em trai, hay chị em gái, hay bạn bè, hay đồng sự, hay bà con, hay người ruột thịt; sự "
        f"không kết hợp, sự không gần gũi, sự không tụ hợp, sự không hòa lẫn với những điều ấy – {CALLED} “{PIYA}”.")
WISH = "sự mong muốn như thế này sinh khởi –"                   # evaṃ icchā uppajjati –
NOT_BY_WISH = "Nhưng điều này không thể đạt được bằng sự mong muốn."   # Na kho panetaṃ icchāya pattabbaṃ.
THIS_TOO = f"Đây cũng là “{YAMPI}”."                             # Idampi "yampicchaṃ na labhati tampi dukkhaṃ".
SUBJECT_TO = {"jāti": "có bản chất phải sinh", "jarā": "có bản chất phải lão hóa", "byādhi": "có bản chất phải bệnh",
              "maraṇa": "có bản chất phải chết", "soka": f"có bản chất phải chịu {SORROW5}"}   # X-dhammā
L201A = (f"Ở những chúng sinh {SUBJECT_TO['jāti']}, {WISH} “Ôi, ước gì chúng ta không {SUBJECT_TO['jāti']}; ước "
         f"gì {JATI} không đến với chúng ta!” {NOT_BY_WISH} {THIS_TOO}")
L201B = (f"Ở những chúng sinh {SUBJECT_TO['jarā']}… ở những chúng sinh {SUBJECT_TO['byādhi']}… ở những chúng sinh "
         f"{SUBJECT_TO['maraṇa']}… ở những chúng sinh {SUBJECT_TO['soka']}, {WISH} “Ôi, ước gì chúng ta không "
         f"{SUBJECT_TO['soka']}; ước gì {SORROW5} không đến với chúng ta!” {NOT_BY_WISH} {THIS_TOO}")
L202A = (f"{stmt_q(BRIEF)} Cụ thể là – {', '.join(UPA_KH[a] for a in S.FIVE)}. {cap(CALLED_PL)} “{BRIEF}”.")
L202B = f"{cap(CALLED)} “{ARIYA['dukkha']}”."

# ---- origin and cessation: craving and where it arises / ceases
TANHA = "khao khát"                                              # taṇhā
CRAVING_DEF = (f"Đó là {TANHA} dẫn đến sự hiện hữu mới {S.spell('Syā., Ka.', 'ponobbhavikā')}, đi kèm với sự thích "
               f"thú và tham đắm, tìm vui thích chỗ này chỗ kia, cụ thể là – khao khát dục lạc, khao khát được hiện hữu, "
               f"khao khát không còn hiện hữu.")
# Yāyaṃ taṇhā ponobhavikā [ponobbhavikā (syā. ka.)] nandirāgasahagatā tatratatrābhinandinī, seyyathidaṃ – kāmataṇhā,
# bhavataṇhā, vibhavataṇhā.
CESS_DEF = (f"Đó là sự phai nhạt và chấm dứt không còn dư sót của chính {TANHA} ấy, sự xả bỏ, sự buông bỏ, sự giải "
            f"thoát, sự không còn bám chấp.")   # Yo tassāyeva taṇhāya asesavirāganirodho cāgo paṭinissaggo mutti anālayo.
WHERE_ARISE = f"Vậy {TANHA} này khi sinh khởi thì sinh khởi ở đâu, khi bám rễ thì bám rễ ở đâu?"
WHERE_CEASE = f"Vậy {TANHA} này khi được dứt bỏ thì được dứt bỏ ở đâu, khi chấm dứt thì chấm dứt ở đâu?"
THERE_ARISE = f"ở đó {TANHA} này khi sinh khởi thì sinh khởi, ở đó khi bám rễ thì bám rễ."
# Etthesā taṇhā uppajjamānā uppajjati, ettha nivisamānā nivisati.
THERE_CEASE = f"ở đó {TANHA} này khi được dứt bỏ thì được dứt bỏ, ở đó khi chấm dứt thì chấm dứt."
# Etthesā taṇhā pahīyamānā pahīyati, ettha nirujjhamānā nirujjhati.
DEAR = "là điều đáng yêu, là điều khoan khoái"                       # piyarūpaṃ sātarūpaṃ (termbase «điều đáng yêu»,
                                                                 # «điều khoan khoái»)
IN_WORLD = "trong thế gian"                                      # loke
WHAT_DEAR = f"Và điều gì {IN_WORLD} {DEAR}?"                     # Kiñca loke piyarūpaṃ sātarūpaṃ?
WHATEVER_DEAR = f"Điều gì {IN_WORLD} {DEAR}, thì "               # Yaṃ loke piyarūpaṃ sātarūpaṃ, etthesā …
SENSE6 = ["mắt", "tai", "mũi", "lưỡi", "thân", "ý"]
OBJ6 = ["hình sắc", "âm thanh", "mùi", "vị", "vật xúc chạm", "đối tượng của ý"]
LOKE = {}   # Pāli nominative (lower case) -> Vietnamese (lower case)
for _p, _v in zip(["cakkhuṃ", "sotaṃ", "ghānaṃ", "jivhā", "kāyo", "mano"], SENSE6):
    LOKE[_p] = _v
for _p, _v in zip(["rūpā", "saddā", "gandhā", "rasā", "phoṭṭhabbā", "dhammā"], OBJ6):
    LOKE[_p] = f"các {_v}"
_ST = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "mano"]
_OB = ["rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba", "dhamma"]
for _p, _v in zip(_ST, SENSE6):
    LOKE[f"{_p}viññāṇaṃ"] = K1.VINN[_p]                               # thức qua mắt … ý thức
    LOKE[f"{_p}samphasso"] = f"sự tiếp xúc của {_v}"                    # termbase Cakkhusamphasso …
    LOKE[f"{_p}samphassajā vedanā"] = f"cảm giác sinh từ sự tiếp xúc của {_v}"
for _p, _v in zip(_OB, OBJ6):
    LOKE[f"{_p}saññā"] = f"tri giác về {_v}"                 # (Kāmasaññā «tri giác về dục lạc»)
    LOKE[f"{_p}sañcetanā"] = f"sự cố ý về {_v}"              # sañcetanā «sự cố ý»
    LOKE[f"{_p}taṇhā"] = f"khao khát {_v}"                   # (phoṭṭhabbataṇhā «khao khát vật xúc chạm»)
    LOKE[f"{_p}vitakko"] = f"sự hướng tâm đến {_v}"          # (Kāmavitakko «sự hướng tâm đến dục lạc»)
    LOKE[f"{_p}vicāro"] = f"sự duy trì tâm trên {_v}"        # vicāro «sự duy trì tâm»
LOKE_RX = re.compile(r"(\S+(?: vedanā)?) loke(…pe…|…| piyarūpaṃ sātarūpaṃ\.)")


def loke_line(p, there):
    """the six-item rows of ^2-203 / ^2-204 («X loke…pe… y loke… z loke piyarūpaṃ sātarūpaṃ. Etthesā …»)"""
    def rep(m):
        w = m.group(1)
        v = LOKE[w[:1].lower() + w[1:]]
        if w[0].isupper():
            v = cap(v)
        if m.group(2).startswith(" "):
            return f"{v} {IN_WORLD} {DEAR}."
        return f"{v} {IN_WORLD}…"
    if "rūpataṇhā" in p.lower():
        misfit("rūpataṇhā (^2-203, ^2-204, the row rūpa-, sadda- … dhammataṇhā = craving for visible forms …): the "
               "termbase sense 'craving for the fine-material sphere' «khao khát cõi hình sắc» does not fit; built "
               "like the sibling phoṭṭhabbataṇhā «khao khát vật xúc chạm»: «khao khát hình sắc»")
    out = LOKE_RX.sub(rep, p)
    for pa, vi in (("Etthesā taṇhā uppajjamānā uppajjati, ettha nivisamānā nivisati.", cap(THERE_ARISE)),
                   ("Etthesā taṇhā pahīyamānā pahīyati, ettha nirujjhamānā nirujjhati.", cap(THERE_CEASE)),
                   ("Kiñca loke piyarūpaṃ sātarūpaṃ?", WHAT_DEAR)):
        out = out.replace(pa, vi)
    return out


# ---- the path: the eight factors (pi-1 ^1-277 names)
PF = dict(zip(["sammādiṭṭhi", "sammāsaṅkappo", "sammāvācā", "sammākammanto", "sammāājīvo", "sammāvāyāmo",
               "sammāsati", "sammāsamādhi"],
              [pi1(x) for x in ("quan điểm đúng đắn", "tư duy đúng đắn", "lời nói đúng đắn", "hành động đúng đắn",
                                "sinh kế đúng đắn", "nỗ lực đúng đắn", "tỉnh thức đúng đắn", "định tâm đúng đắn")]))
PATH8 = ", ".join(PF.values())
L205_1 = (f"{q(ARIYA['magga'])} Chính là con đường gồm tám chi phần cao quý này, cụ thể là – {PATH8}.")
# Ayameva ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – … (Ariyo «cao quý», aṭṭhaṅgiko maggo «con đường gồm tám chi phần»)
L205_2 = (f"{q(PF['sammādiṭṭhi'])} Hiểu biết về {DUKKHA}, hiểu biết về {SAMUDAYA}, hiểu biết về {NIRODHA}, hiểu biết "
          f"về {PATIPADA} – {CALLED} “{PF['sammādiṭṭhi']}”.")
L205_3 = (f"{q(PF['sammāsaṅkappo'])} Tư duy về sự từ bỏ, tư duy về sự không ác ý, tư duy về sự không hãm hại – "
          f"{CALLED} “{PF['sammāsaṅkappo']}”.")       # Nekkhammasaṅkappo, abyāpādasaṅkappo, avihiṃsāsaṅkappo
ABST = "sự kiềm chế"                                 # veramaṇī (termbase; pi-1 ^1-299)
L205_4 = (f"{q(PF['sammāvācā'])} {cap(ABST)} việc nói dối, {ABST} lời nói chia rẽ, {ABST} lời nói thô ác, {ABST} "
          f"việc nói lời phù phiếm – {CALLED} “{PF['sammāvācā']}”.")
L205_5 = (f"{q(PF['sammākammanto'])} {cap(ABST)} việc sát hại sinh mạng, {ABST} việc lấy của không được cho, {ABST} "
          f"hành vi sai trái trong các dục lạc – {CALLED} “{PF['sammākammanto']}”.")
# termbase: Musāvādā / pisuṇāya vācāya / pharusāya vācāya / samphappalāpā / Pāṇātipātā / adinnādānā /
# kāmesumicchācārā veramaṇī
L205_6 = (f"{q(PF['sammāājīvo'])} Ở đây, vị đệ tử của bậc thánh, sau khi dứt bỏ sinh kế sai lầm, nuôi sống bản thân "
          f"bằng sinh kế đúng đắn – {CALLED} “{PF['sammāājīvo']}”.")
# Idha ariyasāvako micchāājīvaṃ pahāya sammāājīvena jīvikaṃ kappeti
EFFORT = "khởi lên ý muốn, nỗ lực, khởi động tinh tấn, nâng tâm lên, ra sức nỗ lực"
# chandaṃ janeti, vāyamati, vīriyaṃ ārabhati, cittaṃ paggaṇhāti, padahati (termbase)
EVIL = "các hiện tượng bất thiện xấu ác"             # pāpakānaṃ akusalānaṃ dhammānaṃ
GOOD = "các hiện tượng thiện"                        # kusalānaṃ dhammānaṃ
L205_7 = (f"{q(PF['sammāvāyāmo'])} Ở đây, vị tỳ-khưu {EFFORT} để {EVIL} chưa sinh khởi không sinh khởi. Vị ấy "
          f"{EFFORT} để dứt bỏ {EVIL} đã sinh khởi. Vị ấy {EFFORT} để {GOOD} chưa sinh khởi được sinh khởi. Vị ấy "
          f"{EFFORT} để {GOOD} đã sinh khởi được duy trì, không bị mai một, được tăng trưởng, được lớn mạnh, được tu "
          f"tập và được hoàn thiện. {cap(CALLED)} “{PF['sammāvāyāmo']}”.")
# ṭhitiyā «được duy trì» (ṭhiti, persistence of wholesome states: user sense), asammosāya, bhiyyobhāvāya, vepullāya,
# bhāvanāya, pāripūriyā
ARDENT = "nhiệt tâm, hiểu biết rõ ràng, có sự tỉnh thức, sau khi chế ngự sự thèm muốn và nỗi buồn đối với thế gian"
# ātāpī sampajāno satimā, vineyya loke abhijjhādomanassaṃ (termbase)
L205_8 = (f"{q(PF['sammāsati'])} Ở đây, đối với thân, vị tỳ-khưu sống quán sát thân, {ARDENT}. Đối với các cảm giác… "
          f"đối với tâm… đối với các hiện tượng, vị ấy sống quán sát các hiện tượng, {ARDENT}. {cap(CALLED)} "
          f"“{PF['sammāsati']}”.")
# kāye kāyānupassī viharati (viharati «sống», user; kāyānupassī viharati «sống quán sát thân»)
JH1 = (pi1("hoàn toàn tách khỏi các dục lạc, tách khỏi các hiện tượng bất thiện, chứng nhập và an trú tầng thiền thứ "
           "nhất") + pi1(", có sự hướng tâm và sự duy trì tâm, có sự hân hoan và hạnh phúc sinh từ sự tách biệt"))
JH2 = (pi1("nhờ sự hướng tâm và sự duy trì tâm lắng xuống") + ", vị ấy "
       + pi1("chứng nhập và an trú tầng thiền thứ hai")
       + pi1(", có sự trong sáng ở nơi bản thân, có sự hợp nhất của tâm, không có sự hướng tâm cũng không có sự duy "
             "trì tâm, có sự hân hoan và hạnh phúc sinh từ định tâm"))
JH3 = (pi1("nhờ sự hân hoan phai nhạt") + ", vị ấy "
       + pi1("an trú bình thản, tỉnh thức và hiểu biết rõ ràng, cảm nhận hạnh phúc bằng thân, là trạng thái mà nhờ đó "
             "các bậc thánh mô tả người ấy – “Người bình thản, có sự tỉnh thức, an trú trong hạnh phúc”, chứng nhập và "
             "an trú tầng thiền thứ ba"))
JH4 = (pi1("nhờ dứt bỏ sự dễ chịu và dứt bỏ sự khó chịu, nhờ niềm vui và nỗi buồn đã biến mất từ trước") + ", vị ấy "
       + pi1("chứng nhập và an trú tầng thiền thứ tư")
       + pi1(", không khó chịu cũng không dễ chịu, có sự tỉnh thức hoàn toàn trong sạch nhờ sự bình thản"))
L205_9 = (f"{q(PF['sammāsamādhi'])} Ở đây, vị tỳ-khưu {JH1}. {cap(JH2)}. {cap(JH3)}. {cap(JH4)}. {cap(CALLED)} "
          f"“{PF['sammāsamādhi']}”.")
L205_10 = f"{cap(CALLED)} “{ARIYA['magga']}”."

SUTTANTA4 = {  # Pāli line (without id) -> Vietnamese, for the unique lines of ^2-189 … ^2-205
    "189": NOBLE4.format(v1=" " + VAR_SAMUDAYA, v2=" " + VAR_NIRODHA),
}


# =========================================================================== chapter 4: Abhidhammabhājanīya
FUNCTIONAL = pi1("những hiện tượng mang tính chức năng, không phải thiện, không phải bất thiện, cũng không phải quả "
                 "của nghiệp")                       # ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā (^1-583)
SASAVA = "mà là đối tượng của ô nhiễm"               # sāsava (termbase kusalamūlāni sāsavāni «gốc rễ thiện mà là …»)
MEMBER = {  # list members, «ca» removed, first letter lower case -> Vietnamese (nominative and genitive forms)
    "taṇhā": TANHA, "taṇhāya": TANHA,
    "avasesā kilesā": "các phiền não còn lại", "avasesānaṃ kilesānaṃ": "các phiền não còn lại",
    "avasesā akusalā dhammā": "các hiện tượng bất thiện còn lại",
    "avasesānaṃ akusalānaṃ dhammānaṃ": "các hiện tượng bất thiện còn lại",
    "tīṇi kusalamūlāni sāsavāni": f"ba gốc rễ thiện {SASAVA}", "tiṇṇaṃ kusalamūlānaṃ sāsavānaṃ": f"ba gốc rễ thiện {SASAVA}",
    "avasesā sāsavā kusalā dhammā": f"các hiện tượng thiện còn lại {SASAVA}",
    "avasesānaṃ sāsavānaṃ kusalānaṃ dhammānaṃ": f"các hiện tượng thiện còn lại {SASAVA}",
    "sāsavā kusalākusalānaṃ dhammānaṃ vipākā": f"những quả của các hiện tượng thiện và bất thiện {SASAVA}",
    "ye dhammā kiriyā neva kusalā nākusalā na kammavipākā": FUNCTIONAL,
    "sabbaṃ rūpaṃ": pi1("toàn bộ vật chất"),
}


def _member_key(m):
    m = m.strip()
    m = re.sub(r"(\S)ñca\b", r"\1ṃ", m)              # avasesānañca -> avasesānaṃ, sabbañca -> sabbaṃ
    m = re.sub(r"\bca\b", "", m)
    m = re.sub(r"\s+", " ", m).strip()
    return m[:1].lower() + m[1:]


def members(body):
    """«Taṇhā ca avasesā ca kilesā, avasesā ca …» -> [Vietnamese members]"""
    parts = [x for x in re.split(r", ", body) if x.strip()]
    out = []
    for x in parts:
        k = _member_key(x)
        if k == "taṇhā avasesā kilesā":                  # «Taṇhā ca avasesā ca kilesā» (no comma)
            out += [MEMBER["taṇhā"], MEMBER["avasesā kilesā"]]
            continue
        out.append(MEMBER[k])
    return out


TRUTH_ABHI = {"dukkhasamudayo": SAMUDAYA, "dukkhaṃ": DUKKHA, "dukkhanirodho": NIRODHA,
              "dukkhanirodhagāminī paṭipadā": PATIPADA}
LIST_RX = re.compile(r'^Tattha katam(?:o|aṃ|ā) (dukkhasamudayo|dukkhaṃ|dukkhanirodho)\? (.*?)( pahānaṃ)? – '
                     r'(?:ayaṃ|idaṃ) vuccati "(\S+)"\.$')


def list_line(p):
    m = LIST_RX.match(p)
    assert m, p
    t, body, pahana, t2 = m.groups()
    assert t == t2, p
    ms = members(body)
    v = vlist(ms)
    v = f"Sự dứt bỏ {v}" if pahana else cap(v)       # Taṇhāya pahānaṃ (termbase «sự dứt bỏ khao khát»)
    return f"{q(TRUTH_ABHI[t])} {v} – {CALLED} “{TRUTH_ABHI[t]}”."


SUPRA = pi1("tu tập tầng thiền vượt thế gian dẫn đến giải thoát và dẫn đến sự giảm trừ, để dứt bỏ sự mắc kẹt trong "
            "các quan điểm, để đạt đến giai đoạn thứ nhất, hoàn toàn tách khỏi các dục lạc… chứng nhập và an trú tầng "
            "thiền thứ nhất, với cách thực hành khó khăn và sự hiểu biết trực tiếp chậm chạp, thì vào lúc ấy")   # ^1-277
SUPRA_RX = re.compile(r"^Tattha katamā dukkhanirodhagāminī paṭipadā\? Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ "
                      r"bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā(,?) vivicceva "
                      r"kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ, tasmiṃ samaye "
                      r"(.*)$")
PATH5 = ", ".join(PF[k] for k in ("sammādiṭṭhi", "sammāsaṅkappo", "sammāvāyāmo", "sammāsati", "sammāsamādhi"))
REST_CONJ = f"Các hiện tượng còn lại gắn liền với {PATIPADA}."   # Avasesā dhammā … paṭipadāya sampayuttā.
SUPRA_TAIL = [  # (Pāli, Vietnamese), applied in order
    ("aṭṭhaṅgiko maggo hoti sammādiṭṭhi…pe… sammāsamādhi.",
     f"có con đường gồm tám chi phần: {PF['sammādiṭṭhi']}… {PF['sammāsamādhi']}."),
    ("aṭṭhaṅgiko maggo hoti – sammādiṭṭhi…pe… sammāsamādhi.",
     f"có con đường gồm tám chi phần – {PF['sammādiṭṭhi']}… {PF['sammāsamādhi']}."),
    ("pañcaṅgiko maggo hoti – sammādiṭṭhi, sammāsaṅkappo, sammāvāyāmo, sammāsati, sammāsamādhi.",
     f"có con đường gồm năm chi phần – {PATH5}."),
    ("phasso hoti…pe… avikkhepo hoti.", "có sự tiếp xúc… có sự không tán loạn."),     # pi-1 ^1-339
    (' Ayaṃ vuccati – "dukkhanirodhagāminī paṭipadā".', f" {cap(CALLED)} – “{PATIPADA}”."),
    (' Ayaṃ vuccati "dukkhanirodhagāminī paṭipadā".', f" {cap(CALLED)} “{PATIPADA}”."),
    (" Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā.", f" {REST_CONJ}"),
]


def tail_sub(t):
    for pa, vi in SUPRA_TAIL:
        t = t.replace(pa, vi)
    return t


def supra_line(p):
    m = SUPRA_RX.match(p)
    assert m, p
    if not m.group(1):
        slip("^2-208, 209, 213, 214: no comma after «pattiyā» (^2-206, 207, 210 … have one): rendered with the comma, "
             "as pi-1 ^1-277")
    if "maggo hoti sammādiṭṭhi" in p:
        slip("^2-206 «aṭṭhaṅgiko maggo hoti sammādiṭṭhi…pe…» has no dash (^2-207 … have «hoti –»): no dash added, «:» "
             "written instead")
    return f"{q(PATIPADA)} Ở đây, vào lúc một vị tỳ-khưu {SUPRA} {tail_sub(m.group(2))}"


PATH_TAIL = pi1("chi phần của con đường, nằm trong con đường")        # maggaṅgaṃ maggapariyāpannaṃ
PANNA_SHORT = pi1("trí tuệ, sự hiểu rõ… sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn")   # ^1-1359
ABSTAIN = "sự tránh xa {x}, sự kiêng tránh, sự kiêng tránh hoàn toàn, sự kiềm chế{v}" + pi1(
    ", sự không làm, sự không thực hiện, sự không rơi vào lỗi vi phạm, sự không vượt quá giới hạn, sự phá bỏ cây cầu")
VERAMANI_VAR = " [khác chính tả (Ka.): veramaṇi, cũng vậy ở các chỗ sau]"   # [veramaṇi (ka.) evamuparipi]
VIRIYA_HEAD = pi1("sự khởi động tinh tấn trong tâm")                    # cetasiko vīriyārambho
FACTOR_BODY = {  # the Abhidhamma path-factor definitions: body between «Yo/Yā» and «maggaṅgaṃ maggapariyāpannaṃ»
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo":
        f"{PANNA_SHORT}, " + pi1("chi phần giác ngộ là sự tìm hiểu các hiện tượng"),
    "takko vitakko…pe… sammāsaṅkappo": f"{pi1('suy nghĩ, sự hướng tâm')}… {PF['sammāsaṅkappo']}",
    "catūhi vacīduccaritehi ārati virati paṭivirati veramaṇī [veramaṇi (ka.) evamuparipi] akiriyā akaraṇaṃ anajjhāpatti "
    "velāanatikkamo setughāto sammāvācā":
        ABSTAIN.format(x=pi1("bốn hành vi xấu bằng lời nói"), v=VERAMANI_VAR) + f", {PF['sammāvācā']}",
    "tīhi kāyaduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
    "sammākammanto":
        ABSTAIN.format(x=pi1("ba hành vi xấu bằng thân"), v="") + f", {PF['sammākammanto']}",
    "micchā ājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto sammāājīvo":
        ABSTAIN.format(x=pi1("sinh kế sai lầm"), v="") + f", {PF['sammāājīvo']}",
    "cetasiko vīriyārambho [viriyārambho (sī. syā.)] …pe… sammāvāyāmo vīriyasambojjhaṅgo":
        f"{VIRIYA_HEAD} {S.spell('Sī., Syā.', 'viriyārambho')}… {PF['sammāvāyāmo']}, "
        + pi1("chi phần giác ngộ là sự tinh tấn"),
    "cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo":
        f"{VIRIYA_HEAD}… {PF['sammāvāyāmo']}, chi phần giác ngộ là sự tinh tấn",
    "sati anussati…pe… sammāsati satisambojjhaṅgo":
        f"{pi1('sự tỉnh thức, sự nhớ lại')}… {PF['sammāsati']}, " + pi1("chi phần giác ngộ là sự tỉnh thức"),
    "cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo":
        f"{pi1('sự ổn định của tâm, sự vững vàng')}… {PF['sammāsamādhi']}, " + pi1("chi phần giác ngộ là định tâm"),
    "cittassa ṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo":
        f"sự ổn định của tâm… {PF['sammāsamādhi']}, chi phần giác ngộ là định tâm",
}
FACTOR_RX = re.compile(r'^Tattha katam[oā] (\S+)\? Y[oā] (.*) maggaṅgaṃ maggapariyāpannaṃ – ayaṃ vuccati "(\S+)"\.'
                       r'( .*)?$')


def factor_line(p):
    m = FACTOR_RX.match(p)
    assert m, p
    name, body, name2, tail = m.groups()
    assert name == name2, p
    if body.startswith("micchā ājīvā"):
        slip("^2-206 «micchā ājīvā» written as two words (pi-1 ^1-301 «micchāājīvā»): same Vietnamese «sinh kế sai "
             "lầm»")
    out = f"{q(PF[name])} {WHICH} {FACTOR_BODY[body]}, {PATH_TAIL} – {CALLED} “{PF[name]}”."
    if tail:
        out += tail_sub(tail)
    return out


def abhi4(p):
    if p.startswith("Cattāri saccāni – "):
        return TRUTHS4
    if LIST_RX.match(p):
        return list_line(p)
    if SUPRA_RX.match(p):
        return supra_line(p)
    if FACTOR_RX.match(p):
        return factor_line(p)
    if p.startswith("Ayaṃ vuccati ") or p.startswith("Avasesā "):
        return tail_sub(" " + p).strip()
    raise ValueError(p)


# =========================================================================== chapter 5: Abhidhammabhājanīya
IND = {  # the 22 faculties (termbase)
    "cakkhundriyaṃ": "năng lực mắt", "sotindriyaṃ": "năng lực tai", "ghānindriyaṃ": "năng lực mũi",
    "jivhindriyaṃ": "năng lực lưỡi", "kāyindriyaṃ": "năng lực thân", "manindriyaṃ": "năng lực ý",
    "itthindriyaṃ": "năng lực nữ tính", "purisindriyaṃ": "năng lực nam tính", "jīvitindriyaṃ": "năng lực sống",
    "sukhindriyaṃ": "năng lực dễ chịu", "dukkhindriyaṃ": "năng lực khó chịu", "somanassindriyaṃ": "năng lực niềm vui",
    "domanassindriyaṃ": "năng lực nỗi buồn", "upekkhindriyaṃ": "năng lực bình thản",
    "saddhindriyaṃ": "năng lực niềm tin", "vīriyindriyaṃ": "năng lực tinh tấn", "satindriyaṃ": "năng lực tỉnh thức",
    "samādhindriyaṃ": "năng lực định tâm", "paññindriyaṃ": "năng lực trí tuệ",
    "anaññātaññassāmītindriyaṃ": "năng lực biết được điều chưa từng biết", "aññindriyaṃ": "năng lực hiểu biết trọn vẹn",
    "aññātāvindriyaṃ": "năng lực của người đã hiểu biết trọn vẹn",
    "rūpajīvitindriyaṃ": "năng lực sống thuộc vật chất", "arūpajīvitindriyaṃ": "năng lực sống phi vật chất",
}
IND22 = list(IND)[:22]
VIRIYA_VAR = S.spell("Sī., Syā.", "viriyindriyaṃ")      # [viriyindriyaṃ (sī. syā.)]


def ind22(var=False):
    """Bāvīsatindriyāni – … (^2-219 with the variant, ^2-221 without)"""
    items = [IND[k] + (" " + VIRIYA_VAR if var and k == "vīriyindriyaṃ" else "") for k in IND22]
    return f"Hai mươi hai năng lực – {', '.join(items)}."


def ind_q(k):
    return q(IND[k])


def ind_called(k, quoted=True):
    return f"– {CALLED} “{IND[k]}”." if quoted else f"– {CALLED} {IND[k]}."


MANI = IND["manindriyaṃ"]
MANI_RX = re.compile(r"^(\S+?)[vb]idhena manindriyaṃ – (.*)$")


def mani_sentence(s):
    """one sentence of the manindriya classification (K1.chain for the body; as ^2-161 manāyatana)"""
    m = re.match(r"^Evaṃ (\S+?)[vb]idhena manindriyaṃ\.$", s)
    if m:
        return f"Như vậy là {MANI} {K1.by_n(K1.NUMP[m.group(1).lower()])}."
    m = MANI_RX.match(s)
    assert m, s
    nw, body = m.groups()
    body = re.sub(r"^phassasampayuttaṃ\.$", "phassasampayutto.", body)    # neuter of the K1 item key
    return f"{cap(MANI)} {K1.by_n(K1.NUMP[nw.lower()])} – {K1.chain(body)}"


def mani_line(p):
    head = ""
    if p.startswith("Tattha katamaṃ manindriyaṃ? "):
        head = f"{ind_q('manindriyaṃ')} "
        p = p[len("Tattha katamaṃ manindriyaṃ? "):]
    tail = ""
    m = re.match(r'^(.*)…pe… evaṃ bahuvidhena manindriyaṃ\. Idaṃ vuccati "manindriyaṃ"\.$', p)
    if m:                                     # «… Evaṃ dasavidhena manindriyaṃ…pe… evaṃ bahuvidhena …»
        p = m.group(1) + "."
        tail = f"… {low('Như vậy là')} {MANI} {K1.by_n('many')}. {cap(CALLED)} “{MANI}”."
    sents = re.split(r"(?<=\.) (?=[A-Z])", p)
    out = " ".join(mani_sentence(s) for s in sents)
    if tail:
        assert out.endswith("."), out
        out = out[:-1] + tail
    return head + out


FEM = pi1("Điều mà ở người nữ là hình tướng nữ tính, dấu hiệu nữ tính, cử chỉ nữ tính, dáng điệu nữ tính, trạng thái "
          "nữ tính, tính chất nữ tính")                                   # pi-1 ^1-632
MASC = pi1("Điều mà ở người nam là hình tướng nam tính, dấu hiệu nam tính, cử chỉ nam tính, dáng điệu nam tính, trạng "
           "thái nam tính, tính chất nam tính")                           # pi-1 ^1-633
LIFE = pi1("tuổi thọ, sự tồn tại, sự tiếp diễn, sự kéo dài, sự vận động, sự tiến triển, sự gìn giữ, sự sống, năng lực "
           "sống")                    # āyu ṭhiti … jīvitindriyaṃ (pi-1 ^1-634; ṭhiti «sự tồn tại», user decision)
LIFE_RUPA = pi1("Điều mà ở những hiện tượng thuộc vật chất ấy là") + f" {LIFE}"     # Yo tesaṃ rūpīnaṃ dhammānaṃ …
LIFE_ARUPA = pi1("Điều mà ở những hiện tượng phi vật chất ấy là") + f" {LIFE}"     # Yo tesaṃ arūpīnaṃ dhammānaṃ …
LIFE2 = (f"{cap(IND['jīvitindriyaṃ'])} {K1.by_n(2)} – {S.SOME} là {IND['rūpajīvitindriyaṃ']}, {S.SOME} là "
         f"{IND['arūpajīvitindriyaṃ']}.")   # Jīvitindriyaṃ duvidhena – atthi rūpajīvitindriyaṃ, atthi arūpajīvitindriyaṃ.
SADDHA = pi1("niềm tin, sự tin tưởng, sự tin chắc, lòng tin sâu sắc, niềm tin, năng lực niềm tin, sức mạnh niềm tin")
VIRIYA_A = pi1("sự khởi động tinh tấn trong tâm, sự dấn bước, sự xông pha, sự gắng sức, sự nỗ lực, sự hăng hái, sự "
               "bền chí, sức bền")
VIRIYA_B = pi1("sự xông pha không lơi lỏng, sự không buông bỏ ý muốn, sự không buông bỏ gánh, sự dốc sức gánh vác, sự "
               "tinh tấn, năng lực tinh tấn, sức mạnh tinh tấn")
THITI_VIRIYA = "sự ổn định"          # ṭhiti in the energy list (^2-220 «thāmo ṭhiti»; pi-1 ^1-22 «thāmo dhiti»)
VIRIYA = f"{VIRIYA_A}, {THITI_VIRIYA}, {VIRIYA_B}"
SATI = pi1("sự tỉnh thức, sự nhớ lại, sự hồi tưởng, sự tỉnh thức, sự ghi nhớ, sự gìn giữ trong trí nhớ, sự không hời "
           "hợt, sự không quên lãng, sự tỉnh thức, năng lực tỉnh thức, sức mạnh tỉnh thức, tỉnh thức đúng đắn")  # ^1-1358
SAMADHI = pi1("sự ổn định của tâm, sự vững vàng, sự vững chãi, sự không phân tán, sự không tán loạn, trạng thái tâm "
              "trí không phân tán, sự tĩnh lặng, năng lực định tâm, sức mạnh định tâm, định tâm đúng đắn")    # ^1-11
KNOW = {   # Yā tesaṃ dhammānaṃ … sacchikiriyāya paññā … (pi-1 ^1-296, ^1-364 wording)
    "anaññātaññassāmītindriyaṃ": pi1("Điều mà, để tự mình chứng nghiệm những hiện tượng ấy vốn chưa được biết, chưa "
                                     "được thấy, chưa được đạt đến, chưa được nhận biết và chưa được tự mình chứng "
                                     "nghiệm, là trí tuệ, sự hiểu rõ"),
    "aññindriyaṃ": pi1("Điều mà, để tự mình chứng nghiệm những hiện tượng ấy vốn đã được biết, đã được thấy, đã được "
                       "đạt đến, đã được nhận biết và đã được tự mình chứng nghiệm, là trí tuệ, sự hiểu rõ"),
    # pi-2 ^2-220 «tesaṃ dhammānaṃ aññātāvīnaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya» (pi-1 ^1-555
    # «tesaṃ aññātāvīnaṃ dhammānaṃ aññā»): built on the aññindriya frame, aññātāvīnaṃ «đã được hiểu biết trọn vẹn»
    "aññātāvindriyaṃ": ("Điều mà, để tự mình chứng nghiệm những hiện tượng ấy vốn đã được hiểu biết trọn vẹn, đã được "
                        "thấy, đã được đạt đến, đã được nhận biết và đã được tự mình chứng nghiệm, là trí tuệ, sự hiểu rõ"),
}
KNOW_TAIL = pi1("… sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn") + ", " + pi1(
    "chi phần giác ngộ là sự tìm hiểu các hiện tượng, chi phần của con đường, nằm trong con đường")


def feeling(k, ind):
    """Tattha katamaṃ sukhindriyaṃ? Yaṃ kāyikaṃ sātaṃ … – idaṃ vuccati "sukhindriyaṃ"."""
    return f"{ind_q(ind)} {WHICH} {K23.FEELING_P1[k]} {ind_called(ind)}"


def build_ch5_abhi():
    """^2-220: the 30 lines of the Abhidhammabhājanīya, in order"""
    L = []
    L.append(f"{ind_q('cakkhundriyaṃ')} {K23.dh_pe('cakkhu')} {ind_called('cakkhundriyaṃ')}")
    L.append(f"{TATTHA} {IND['sotindriyaṃ']}… {IND['ghānindriyaṃ']}… {IND['jivhindriyaṃ']}… {IND['kāyindriyaṃ']} "
             f"{IS_WHAT} {K23.dh_pe('kāya')} {ind_called('kāyindriyaṃ')}")
    L += ["#MANI"] * 5                                         # filled from the Pāli by mani_line()
    L.append(f"{ind_q('itthindriyaṃ')} {FEM} {ind_called('itthindriyaṃ')}")
    L.append(f"{ind_q('purisindriyaṃ')} {MASC} {ind_called('purisindriyaṃ')}")
    L.append(f"{ind_q('jīvitindriyaṃ')} {LIFE2}")
    L.append(f"{ind_q('rūpajīvitindriyaṃ')} {LIFE_RUPA} {ind_called('rūpajīvitindriyaṃ')}")
    slip("^2-220 «idaṃ vuccati \"arūpajīvatindriyaṃ\"» for «arūpajīvitindriyaṃ» (plain spelling slip, rendered as "
         "meant «năng lực sống phi vật chất»)")
    L.append(f"{ind_q('arūpajīvitindriyaṃ')} {LIFE_ARUPA} {ind_called('arūpajīvitindriyaṃ')} {cap(CALLED)} "
             f"“{IND['jīvitindriyaṃ']}”.")
    for k, ind in (("sukha", "sukhindriyaṃ"), ("dukkha", "dukkhindriyaṃ"), ("somanassa", "somanassindriyaṃ"),
                   ("domanassa", "domanassindriyaṃ"), ("upekkhā", "upekkhindriyaṃ")):
        L.append(feeling(k, ind))
    L.append(f"{ind_q('saddhindriyaṃ')} {WHICH} {SADDHA} {ind_called('saddhindriyaṃ')}")
    misfit(f"ṭhiti in the energy list (^2-220 «thāmo ṭhiti», where pi-1 ^1-22 has «thāmo dhiti» «sự kiên trì»): "
           f"translated as written; none of the three user senses (concentration «sự ổn định», persistence of "
           f"wholesome states «sự duy trì», life «sự tồn tại») is tagged for energy; the closest, steadiness, gives "
           f"«{THITI_VIRIYA}»")
    slip("^2-220 vīriyindriya list «thāmo ṭhiti» (pi-1 ^1-22, ^1-289 «thāmo dhiti»): a one-letter difference that "
         "changes the word; kept as written («sức bền, sự ổn định»)")
    L.append(f"{ind_q('vīriyindriyaṃ')} {WHICH} {VIRIYA} {ind_called('vīriyindriyaṃ')}")
    L.append(f"{ind_q('satindriyaṃ')} {WHICH} {SATI} {ind_called('satindriyaṃ')}")
    L.append(f"{ind_q('samādhindriyaṃ')} {WHICH} {SAMADHI} {ind_called('samādhindriyaṃ')}")
    L.append(f"{ind_q('paññindriyaṃ')} {WHICH} {PANNA_SHORT} {ind_called('paññindriyaṃ')}")
    L.append(f"{ind_q('anaññātaññassāmītindriyaṃ')} {KNOW['anaññātaññassāmītindriyaṃ']}{KNOW_TAIL} "
             f"{ind_called('anaññātaññassāmītindriyaṃ')}")
    slip("^2-220 «– idaṃ vuccati aññindriyaṃ.» without the quote marks the other faculties have: kept as written "
         "(no quotes)")
    L.append(f"{ind_q('aññindriyaṃ')} {KNOW['aññindriyaṃ']}{KNOW_TAIL} {ind_called('aññindriyaṃ', quoted=False)}")
    L.append(f"{ind_q('aññātāvindriyaṃ')} {KNOW['aññātāvindriyaṃ']}{KNOW_TAIL} {ind_called('aññātāvindriyaṃ')}")
    L.append(K1.FIXED["Abhidhammabhājanīyaṃ."])
    return L


# =========================================================================== chapter 4: the Suttanta dispatcher
def suttanta4(p):
    """one Pāli line of the Suttantabhājanīya of chapter 4 -> Vietnamese"""
    if p.startswith("Cattāri ariyasaccāni – "):
        if "[" in p:
            return NOBLE4.format(v1=" " + VAR_SAMUDAYA, v2=" " + VAR_NIRODHA)
        return NOBLE4.format(v1="", v2="")
    fixed = {
        "Tattha katamaṃ dukkhaṃ ariyasaccaṃ? Jātipi": L190,
        "Tattha katamā jāti? ": f"{q(JATI)} Điều mà, {EACH}, là {JATI_LIST} – {CALLED} “{JATI}”.",
        "Tattha katamā jarā? ": f"{q(JARA)} Điều mà, {EACH}, là {JARA_LIST} – {CALLED} “{JARA}”.",
        "Tattha katamaṃ maraṇaṃ? ": f"{q(MARANA)} Điều mà, đối với từng chúng sinh, là {MARANA_LIST} – {CALLED} "
                                    f"“{MARANA}”.",
        "Tattha katamo soko? ": f"{q(SOKA)} {AFFLICT} {SOKA_LIST} – {CALLED} “{SOKA}”.",
        "Tattha katamo paridevo? ": f"{q(PARIDEVA)} {AFFLICT} {PARIDEVA_LIST} – {CALLED} “{PARIDEVA}”.",
        "Tattha katamaṃ dukkhaṃ? Yaṃ kāyikaṃ": f"{q(PAIN)} {WHICH} {K23.FEELING_P1['dukkha']} – {CALLED} “{PAIN}”.",
        "Tattha katamaṃ domanassaṃ? ": f"{q(DOMANASSA)} {WHICH} {K23.FEELING_P1['domanassa']} – {CALLED} "
                                       f"“{DOMANASSA}”.",
        "Tattha katamo upāyāso? ": f"{q(UPAYASA)} {AFFLICT} {UPAYASA_LIST} – {CALLED} “{UPAYASA}”.",
        "Tattha katamo appiyehi": L199,
        "Tattha katamo piyehi": L200,
        "Tattha katamaṃ yampicchaṃ": f"{stmt_q(YAMPI)} {L201A}",
        "Jarādhammānaṃ sattānaṃ": L201B,
        "Tattha katame saṃkhittena": L202A,
        'Idaṃ vuccati "dukkhaṃ ariyasaccaṃ".': L202B,
        "Tattha katamaṃ dukkhasamudayaṃ ariyasaccaṃ? ": f"{q(ARIYA['samudaya'])} {CRAVING_DEF}",
        "Sā kho panesā taṇhā kattha uppajjamānā": f"{WHERE_ARISE} {WHATEVER_DEAR}{THERE_ARISE}",
        'Idaṃ vuccati "dukkhasamudayaṃ ariyasaccaṃ".': f"{cap(CALLED)} “{ARIYA['samudaya']}”.",
        "Tattha katamaṃ dukkhanirodhaṃ ariyasaccaṃ? ": f"{q(ARIYA['nirodha'])} {CESS_DEF}",
        "Sā kho panesā taṇhā kattha pahīyamānā": f"{WHERE_CEASE} {WHATEVER_DEAR}{THERE_CEASE}",
        'Idaṃ vuccati "dukkhanirodhaṃ ariyasaccaṃ".': f"{cap(CALLED)} “{ARIYA['nirodha']}”.",
        "Tattha katamaṃ dukkhanirodhagāminī paṭipadā ariyasaccaṃ? ": L205_1,
        "Tattha katamā sammādiṭṭhi? Dukkhe": L205_2,
        "Tattha katamo sammāsaṅkappo? Nekkhamma": L205_3,
        "Tattha katamā sammāvācā? Musāvādā": L205_4,
        "Tattha katamo sammākammanto? Pāṇātipātā": L205_5,
        "Tattha katamo sammāājīvo? Idha": L205_6,
        "Tattha katamo sammāvāyāmo? Idha": L205_7,
        "Tattha katamā sammāsati? Idha": L205_8,
        "Tattha katamo sammāsamādhi? Idha": L205_9,
        'Idaṃ vuccati "dukkhanirodhagāminī paṭipadā ariyasaccaṃ".': L205_10,
    }
    hits = [v for k, v in fixed.items() if p.startswith(k)]
    if hits:
        assert len(hits) == 1, p
        if p.startswith("Tattha katamaṃ yampicchaṃ"):
            slip("^2-201 «yampicchaṃ» (^2-190 «yaṃ picchaṃ»): the same phrase, same Vietnamese")
        return hits[0]
    if " loke" in p:
        return loke_line(p, None)
    raise ValueError(p)


# =========================================================================== Pañhāpucchaka (both chapters)
# the K23 question-section engine, its tables extended here in memory only
for _k, _v in TRUTH.items():
    K23.SUBJ[_k] = (_v, "s", "sự thật")
K23.SUBJ["Dve saccā"] = ("Hai sự thật", "p", "sự thật")                # termbase saccā «sự thật»
K23.SUBJ["Tīṇi saccāni"] = ("Ba sự thật", "p", "sự thật")
IND_NUM = {"Dvindriyā": "Hai", "Tīṇindriyā": "Ba", "Cattārindriyā": "Bốn", "Pañcindriyā": "Năm", "Cha indriyā": "Sáu",
           "Sattindriyā": "Bảy", "Aṭṭhindriyā": "Tám", "Navindriyā": "Chín", "Dasindriyā": "Mười",
           "Ekādasindriyā": "Mười một", "Dvādasindriyā": "Mười hai", "Terasindriyā": "Mười ba",
           "Cuddasindriyā": "Mười bốn", "Pannarasindriyā": "Mười lăm", "Soḷasindriyā": "Mười sáu",
           "Sattarasindriyā": "Mười bảy", "Aṭṭhārasindriyā": "Mười tám", "Ekavīsatindriyā": "Hai mươi mốt"}
for _k, _v in IND_NUM.items():
    K23.SUBJ[_k] = (f"{_v} năng lực", "p", "năng lực")                 # termbase Dasindriyā «mười năng lực» …
for _k in ("domanassindriyaṃ", "anaññātaññassāmītindriyaṃ", "jīvitindriyaṃ", "aññindriyaṃ", "aññātāvindriyaṃ",
           "somanassindriyaṃ", "upekkhindriyaṃ", "manindriyaṃ"):
    K23.SUBJ[cap(_k)] = (cap(IND[_k]), "s", "năng lực")
K23.SUBJ["SABBE"] = ("Đều", "p", "năng lực")      # subjectless sentence said of all 22 (K1 «Đều có điều kiện, …»)
K23.SUBJ["TE"] = ("Chúng", "p", "năng lực")       # subjectless sentence continuing the previous subject
K23.LOCAL.update({
    "mahaggatārammaṇo na appamāṇārammaṇo": "có đối tượng rộng lớn nhưng không có đối tượng không thể đo lường",
    "na appamāṇārammaṇo": "không có đối tượng không thể đo lường",
    "na maggārammaṇo": "không lấy con đường làm đối tượng",
    "na maggārammaṇo maggahetuko": "không lấy con đường làm đối tượng nhưng lấy con đường làm gốc rễ",
    "maggārammaṇo na maggahetuko": "lấy con đường làm đối tượng nhưng không lấy con đường làm gốc rễ",
})
K23.PLK["arūpāni"] = "arūpo"                     # Tīṇi saccāni arūpāni (neuter plural)
K23.GROUPS["Catunnaṃ ariyasaccānaṃ"] = (f"Trong bốn {NOBLE}", "bao nhiêu sự thật")
K23.GROUPS["Bāvīsatīnaṃ indriyānaṃ"] = ("Trong hai mươi hai năng lực", "bao nhiêu năng lực")
PFIX = [  # (bad, good, slip note or None): punctuation of the source, rendered as meant
    ('" tipi', '"tipi', "«\" tipi» with a space (^2-217 upādāna and kilesa lines): read as «\"tipi»"),
    ('"nti pi', '"ntipi', "^2-223 «\"mahaggatārammaṇa\"nti pi» with a space: read as «ntipi»"),
    ("nīvaraṇiyā dve saccā anīvaraṇiyā", "nīvaraṇiyā. Dve saccā anīvaraṇiyā",
     "^2-217 «Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā»: full stop missing (added, rendered as meant)"),
    ("siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ", "siyā parittārammaṇaṃ, siyā mahaggatārammaṇaṃ",
     "^2-223 «Domanassindriyaṃ siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ»: comma missing (added)"),
    ('"gantho ceva ganthasampayutta"ñcāti', '"gantho ceva ganthasampayuttañcā"ti',
     "^2-223 «\"gantho ceva ganthasampayutta\"ñcāti»: closing quote misplaced (read as «…ñcā\"ti»)"),
    ("siyā araṇanti.", "siyā araṇaṃ.", None),     # the closing «ti» of the whole section (^2-218)
]
def _has_subject(s):
    keys = sorted(K23.SUBJ, key=len, reverse=True)
    return re.match(r"^(" + "|".join(map(re.escape, keys)) + r") ", s) is not None


def panha_sentence(s):
    """one question-section sentence (without its full stop)"""
    m = re.match(r"^(.*), (aṭṭhindriyā siyā .*)$", s)
    if m:                                         # ^2-223 «…, aṭṭhindriyā siyā …»: a new subject after a comma
        slip("^2-223 «…, aṭṭhindriyā siyā ajjhattārammaṇā …»: a new sentence joined by a comma (kept, subject in "
             "lower case)")
        return f"{panha_sentence(m.group(1))}, {low(panha_sentence(cap(m.group(2))))}"
    if _has_subject(s):
        return K23.sentence(s)
    if s == "Sahetukā ceva na ca hetū":
        slip("^2-223 (dyads) «… na vattabbā – \"hetū ceva sahetukā cā\"ti. Sahetukā ceva na ca hetū.»: a full stop "
             "where the parallels have a comma; kept as its own sentence «Chúng có gốc rễ nhưng không phải là gốc rễ.»")
        return K23.sentence("TE " + low(s))
    return K23.sentence("SABBE " + low(s))       # Sappaccayā. / No āsavā. … (said of all 22 faculties)


def panha_line(p):
    for bad, good, nt in PFIX:
        if bad in p:
            p = p.replace(bad, good)
            if nt:
                slip(nt)
    p = p.replace('"ti pi', '"tipi')
    if "siyā ajjhattaṃ, siyā bāhiraṃ" in p:
        slip("^2-218 dyads «Dukkhasaccaṃ siyā ajjhattaṃ, siyā bāhiraṃ» (the dyad elsewhere ajjhattikā / bāhirā): "
             "ajjhattaṃ translated as written «ở nơi bản thân» (termbase), bāhiraṃ «thuộc phần bên ngoài»")
    out = []
    for s in re.split(r"(?<=\.) (?=[A-Z])", p):
        assert s.endswith("."), s
        out.append(panha_sentence(s[:-1]) + ".")
    return " ".join(out)


# =========================================================================== build and render
FIXED = dict(K23.FIXED)
FIXED.update({
    "Saccavibhaṅgo niṭṭhito.": f"{S.CH_HEADINGS['Saccavibhaṅgo']} {K1.DONE}.",
    "Indriyavibhaṅgo niṭṭhito.": f"{S.CH_HEADINGS['Indriyavibhaṅgo']} {K1.DONE}.",
})
HEAD_T = {"Saccavibhaṅgo": S.CH_HEADINGS["Saccavibhaṅgo"], "Indriyavibhaṅgo": S.CH_HEADINGS["Indriyavibhaṅgo"],
          "Tikaṃ": K1.TIKA_H, "Dukaṃ": K1.DUKA_H}
HEAD_T.update(S.SEC_HEADINGS)
HEAD_T.update(TRUTH)
FOREIGN = re.compile(r"[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶfjwzFJWZ]")


def dashes(s):
    return s.count("–") + s.count("—")


def check_line(sid, p, v):
    assert dashes(p) == dashes(v), (sid, "dash count", dashes(p), dashes(v), v[:120])
    assert ":-" not in v and "—" not in v and "…." not in v, (sid, v[:120])
    body = re.sub(r"\[[^\]]*\]", "", v)
    assert not FOREIGN.search(body), (sid, FOREIGN.search(body).group(0), v[:160])
    assert "  " not in v and not v.endswith(" "), (sid, v[:120])
    if not p.startswith("#"):
        assert v[-1] in ".?!”" or v.endswith("”."), (sid, v[-40:])


def build(part, chapter):
    pali = (S.PALI / part).read_text(encoding="utf-8")
    h = {}
    section = None
    for sid, lines in K1.segs(pali):
        lines = [K1.ID.sub("", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            lvl, text = lines[0].split(" ", 1)
            if text in S.SEC_HEADINGS:
                section = text
            h[sid] = [f"{lvl} {HEAD_T[text]}"]
            continue
        if chapter == 5 and sid == "2-220":
            tmpl = build_ch5_abhi()
            assert len(tmpl) == len(lines), (len(tmpl), len(lines))
            h[sid] = [mani_line(p) if t == "#MANI" else t for t, p in zip(tmpl, lines)]
            continue
        vi = []
        for ln in lines:
            if ln in FIXED:
                vi.append(FIXED[ln])
            elif section == "Pañhāpucchakaṃ":
                if ln.startswith("Cattāri ariyasaccāni – "):
                    vi.append(suttanta4(ln))
                elif ln.startswith("Bāvīsatindriyāni – "):
                    vi.append(ind22(var="[" in ln))
                elif ln.endswith("?"):
                    vi.append(K23.panha_question(ln))
                else:
                    vi.append(panha_line(ln))
            elif section == "Suttantabhājanīyaṃ" or (chapter == 4 and section is None):
                vi.append(suttanta4(ln))
            elif chapter == 5 and ln.startswith("Bāvīsatindriyāni – "):
                vi.append(ind22(var="[" in ln))
            else:
                vi.append(abhi4(ln))
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


# =========================================================================== pi-1 check
def check_pi1():
    """every string marked pi1() must occur in the approved pi-1 Vietnamese rails (first letter either case)"""
    text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI1_VI.glob("*.md")))
    missing = [s for s in PI1_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    return len(PI1_USED)


# =========================================================================== notes
def notes_md():
    L = ["# pi-2 Vietnamese rails: new formulas of chapters 4 and 5 (^2-189 … ^2-224)", "",
         "Generated by build_rails_4_5_vi.py; import it instead of retyping. Strings already in vi-rails-formulas.md "
         "(sample), notes-1.md or notes-2-3.md are not repeated. Format: Pāli = tiếng Việt.", "",
         "## Saccavibhaṅga: names and headings", "",
         "##### Dukkhasaccaṃ / Samudayasaccaṃ / Nirodhasaccaṃ / Maggasaccaṃ = ##### " + " / ".join(TRUTH.values())
         + " (also the question-section subjects)",
         f"dukkhaṃ ariyasaccaṃ / dukkhasamudayaṃ … / dukkhanirodhaṃ … / dukkhanirodhagāminī paṭipadā ariyasaccaṃ = "
         + " / ".join(ARIYA.values()),
         f"Cattāri ariyasaccāni – … = {NOBLE4.format(v1='', v2='')}",
         f"[dukkhasamudayo (syā.)] / [dukkhanirodho (syā.)] = {VAR_SAMUDAYA} / {VAR_NIRODHA}",
         f"Cattāri saccāni – dukkhaṃ, dukkhasamudayo, dukkhanirodho, dukkhanirodhagāminī paṭipadā. = {TRUTHS4}",
         f"dukkhaṃ (suffering) / dukkhaṃ (bodily pain, ^2-196) = {DUKKHA} / {PAIN}",
         f"Dve saccā / Tīṇi saccāni = Hai sự thật / Ba sự thật",
         f"Catunnaṃ ariyasaccānaṃ kati …? = {K23.GROUPS['Catunnaṃ ariyasaccānaṃ'][0]}, "
         f"{K23.GROUPS['Catunnaṃ ariyasaccānaṃ'][1]} …?",
         "", "## Saccavibhaṅga: Suttantabhājanīya", "",
         f"Jātipi dukkhā, … saṃkhittena pañcupādānakkhandhā dukkhā. = {L190.split('? ', 1)[1]}",
         f"sokaparidevadukkhadomanassupāyāsā = {SORROW5}",
         f"appiyehi sampayogo dukkho / piyehi vippayogo dukkho / yampicchaṃ na labhati tampi dukkhaṃ / saṃkhittena "
         f"pañcupādānakkhandhā dukkhā = {APPIYA} / {PIYA} / {YAMPI} / {BRIEF}",
         f"Tattha katamo appiyehi sampayogo dukkho? (a statement as topic) = {stmt_q(APPIYA)}",
         f"pañcupādānakkhandhā / rūpupādānakkhandho … = {FIVE_UPA} / {UPA_KH['rupa']} …",
         f"tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye = {EACH}",
         f"jāti sañjāti okkanti abhinibbatti khandhānaṃ pātubhāvo āyatanānaṃ paṭilābho = {JATI_LIST}",
         f"jarā jīraṇatā … indriyānaṃ paripāko = {JARA_LIST} (pi-1 ^1-643)",
         f"tamhā tamhā sattanikāyā cuti cavanatā … jīvitindriyassupacchedo = {MARANA_LIST}",
         f"Ñātibyasanena vā phuṭṭhassa … aññataraññatarena dukkhadhammena phuṭṭhassa = {AFFLICT} …",
         f"soko socanā … sokasallaṃ = {SOKA_LIST}",
         f"ādevo paridevo … lālappitattaṃ [lālapo lālapanā lālapitattaṃ (syā.)] = {PARIDEVA_LIST}",
         f"āyāso upāyāso āyāsitattaṃ upāyāsitattaṃ = {UPAYASA_LIST}",
         f"Tattha katamaṃ dukkhaṃ? Yaṃ kāyikaṃ asātaṃ … – idaṃ vuccati \"dukkhaṃ\". = {q(PAIN)} {WHICH} … – {CALLED} "
         f"“{PAIN}”.",
         f"Idha yassa te honti aniṭṭhā … missībhāvo = {L199.split('? ', 1)[1].rsplit(' – ', 1)[0]}",
         f"Idha yassa te honti iṭṭhā … amissībhāvo = {L200.split('? ', 1)[1].rsplit(' – ', 1)[0]}",
         f"X-dhammānaṃ sattānaṃ evaṃ icchā uppajjati – \"aho vata …\"ti! = Ở những chúng sinh có bản chất phải X, "
         f"{WISH} “Ôi, ước gì chúng ta không có bản chất phải X; ước gì X không đến với chúng ta!”",
         f"Na kho panetaṃ icchāya pattabbaṃ. = {NOT_BY_WISH}",
         f"Idampi \"yampicchaṃ na labhati tampi dukkhaṃ\". = {THIS_TOO}",
         f"Yāyaṃ taṇhā ponobhavikā … vibhavataṇhā. = {CRAVING_DEF}",
         f"Yo tassāyeva taṇhāya asesavirāganirodho cāgo paṭinissaggo mutti anālayo. = {CESS_DEF}",
         f"Sā kho panesā taṇhā kattha uppajjamānā uppajjati, kattha nivisamānā nivisati? = {WHERE_ARISE}",
         f"Sā kho panesā taṇhā kattha pahīyamānā pahīyati, kattha nirujjhamānā nirujjhati? = {WHERE_CEASE}",
         f"Yaṃ loke piyarūpaṃ sātarūpaṃ, etthesā … = {WHATEVER_DEAR}{THERE_ARISE}",
         f"Etthesā taṇhā uppajjamānā uppajjati, ettha nivisamānā nivisati. = {cap(THERE_ARISE)}",
         f"Etthesā taṇhā pahīyamānā pahīyati, ettha nirujjhamānā nirujjhati. = {cap(THERE_CEASE)}",
         f"Kiñca loke piyarūpaṃ sātarūpaṃ? = {WHAT_DEAR}",
         f"X loke piyarūpaṃ sātarūpaṃ. / X loke…pe… = X {IN_WORLD} {DEAR}. / X {IN_WORLD}…",
         "Rūpasaññā / Rūpasañcetanā / Rūpataṇhā / Rūpavitakko / Rūpavicāro = " + " / ".join(
             cap(LOKE[f"rūpa{x}"]) for x in ("saññā", "sañcetanā", "taṇhā", "vitakko", "vicāro")),
         f"Ayameva ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – … = {L205_1.split('? ', 1)[1]}",
         f"Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ, … = {L205_2.split('? ', 1)[1].rsplit(' – ', 1)[0]}",
         f"Nekkhammasaṅkappo, abyāpādasaṅkappo, avihiṃsāsaṅkappo = {L205_3.split('? ', 1)[1].rsplit(' – ', 1)[0]}",
         f"Musāvādā veramaṇī, … samphappalāpā veramaṇī = {L205_4.split('? ', 1)[1].rsplit(' – ', 1)[0]}",
         f"Pāṇātipātā veramaṇī, … kāmesumicchācārā veramaṇī = {L205_5.split('? ', 1)[1].rsplit(' – ', 1)[0]}",
         f"Idha ariyasāvako micchāājīvaṃ pahāya sammāājīvena jīvikaṃ kappeti = "
         f"{L205_6.split('? ', 1)[1].rsplit(' – ', 1)[0]}",
         f"chandaṃ janeti, vāyamati, vīriyaṃ ārabhati, cittaṃ paggaṇhāti, padahati = {EFFORT}",
         "uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā = để các "
         "hiện tượng thiện đã sinh khởi được duy trì, không bị mai một, được tăng trưởng, được lớn mạnh, được tu tập và "
         "được hoàn thiện",
         f"kāye kāyānupassī viharati ātāpī sampajāno satimā, vineyya loke abhijjhādomanassaṃ = đối với thân, … sống "
         f"quán sát thân, {ARDENT}",
         f"Vedanāsu…pe… citte…pe… dhammesu dhammānupassī viharati … = Đối với các cảm giác… đối với tâm… đối với các "
         f"hiện tượng, vị ấy sống quán sát các hiện tượng, {ARDENT}",
         f"the four jhānas (Idha bhikkhu vivicceva kāmehi …) = Ở đây, vị tỳ-khưu {JH1}. {cap(JH2)}. {cap(JH3)}. "
         f"{cap(JH4)}. (pi-1 ^1-160 … wording, «vị ấy» added)",
         "", "## Saccavibhaṅga: Abhidhammabhājanīya", "",
     ] + [f"{k} = {v}" for k, v in MEMBER.items()] + [
         f"X pahānaṃ = Sự dứt bỏ X; members joined «a, b và c» («a; b; và c» when a member has a comma)",
         f"Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti … dandhābhiññaṃ, tasmiṃ samaye = Ở đây, vào lúc một "
         f"vị tỳ-khưu {SUPRA} (pi-1 ^1-277)",
     ] + [f"{pa.strip()} = {vi.strip()}" for pa, vi in SUPRA_TAIL] + [
         f"[veramaṇi (ka.) evamuparipi] = {VERAMANI_VAR.strip()}",
     ] + [f"Yo/Yā {pa} maggaṅgaṃ maggapariyāpannaṃ = {WHICH} {vi}, {PATH_TAIL}" for pa, vi in FACTOR_BODY.items()] + [
         "", "## Indriyavibhaṅga", "",
         f"Bāvīsatindriyāni – … = {ind22(True)}",
         f"Tattha katamaṃ Xindriyaṃ? … – idaṃ vuccati \"Xindriyaṃ\". = {TATTHA} năng lực X {IS_WHAT} … – {CALLED} "
         f"“năng lực X”.",
         f"Yaṃ cakkhu catunnaṃ mahābhūtānaṃ upādāya pasādo…pe… suñño gāmopeso = {K23.dh_pe('cakkhu')} (K23)",
         f"N-vidhena manindriyaṃ – … / Evaṃ N-vidhena manindriyaṃ. = {cap(MANI)} {K1.by_n(2)} – … / Như vậy là "
         f"{MANI} {K1.by_n(2)}.",
         f"Yaṃ itthiyā itthiliṅgaṃ … itthibhāvo = {FEM} (pi-1 ^1-632)",
         f"Yaṃ purisassa purisaliṅgaṃ … purisabhāvo = {MASC} (pi-1 ^1-633)",
         f"Jīvitindriyaṃ duvidhena – atthi rūpajīvitindriyaṃ, atthi arūpajīvitindriyaṃ. = {LIFE2}",
         f"Yo tesaṃ rūpīnaṃ / arūpīnaṃ dhammānaṃ āyu ṭhiti … jīvitindriyaṃ = {LIFE_RUPA} / {LIFE_ARUPA}",
         f"Yā saddhā saddahanā … saddhābalaṃ = {WHICH} {SADDHA} (pi-1 ^1-12)",
         f"Yo cetasiko vīriyārambho … thāmo ṭhiti … vīriyabalaṃ = {WHICH} {VIRIYA}",
         f"Yā sati anussati … sammāsati = {WHICH} {SATI} (pi-1 ^1-1358)",
         f"Yā cittassa ṭhiti … sammāsamādhi = {WHICH} {SAMADHI} (pi-1 ^1-11)",
         f"Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi = {WHICH} {PANNA_SHORT} (pi-1 ^1-1359)",
     ] + [f"Yā tesaṃ dhammānaṃ … sacchikiriyāya paññā pajānanā…pe… maggapariyāpannaṃ ({k}) = {v}{KNOW_TAIL}"
          for k, v in KNOW.items()] + [
         f"Bāvīsatīnaṃ indriyānaṃ kati …? = {K23.GROUPS['Bāvīsatīnaṃ indriyānaṃ'][0]}, "
         f"{K23.GROUPS['Bāvīsatīnaṃ indriyānaṃ'][1]} …?",
         "Dvindriyā … Ekavīsatindriyā = " + " / ".join(K23.SUBJ[k][0] for k in IND_NUM),
         "subjectless sentences (Sappaccayā. / No āsavā. …, said of all 22) = Đều …: «Đều có điều kiện.», «Đều không "
         "phải là ô nhiễm.»; «Sahetukā ceva na ca hetū.» (continuing «Tīṇindriyā …») = Chúng có gốc rễ nhưng không "
         "phải là gốc rễ.",
         "", "## Question-section items added here", "",
     ] + [f"{k} = {K23.LOCAL[k]}" for k in ("mahaggatārammaṇo na appamāṇārammaṇo", "na appamāṇārammaṇo",
                                            "na maggārammaṇo", "na maggārammaṇo maggahetuko",
                                            "maggārammaṇo na maggahetuko")]
    return unicodedata.normalize("NFC", "\n".join(L) + "\n")


def main():
    for part, ch in (("4-saccavibhango.md", 4), ("5-indriyavibhango.md", 5)):
        pali, h = build(part, ch)
        text = render(pali, h)
        (S.OUT / part).write_bytes(text.encode("utf-8"))
        print(f"wrote {part}: {len(h)} segments")
    n = check_pi1()
    NOTES_PATH.write_bytes(notes_md().encode("utf-8"))
    print(f"pi-1 strings checked: {n}; notes-4-5.md written")
    for s in SLIPS + K1.SLIPS + K23.SLIPS:
        print("slip:", s)
    for s in MISFITS + K1.MISFITS + K23.MISFITS:
        print("misfit:", s)


if __name__ == "__main__":
    main()
