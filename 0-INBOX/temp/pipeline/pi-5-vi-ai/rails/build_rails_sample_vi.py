"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): SAMPLE builder (preamble, 1-puggalakatha).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/preamble.md, 1-puggalakatha.md
and 0-INBOX/temp/pipeline/pi-5-vi-ai/rails/vi-rails-formulas.md from the fixed strings below.
Chapter agents (ch2-31) import the constants and frame functions:

    import sys; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-5-vi-ai\\rails")
    from build_rails_sample_vi import Q, NANU, pentad, hanci, noce, yam, rq, tvam_ce, ese_ce, na_niggahetabbe, ...

Importing writes nothing (outputs only under __main__). At build time every string marked (pi-1) … (pi-4) is
asserted to occur in that book's approved Vietnamese rails, and every output line is checked against its Pāli
line (dash count, balanced quotes, NFC, no "—", no ":-", no "….").
Termbase: AI_translation/vietnamese/pi-5-pali-vietnamese-termbase-plain.md (+ pi-5-vi-ai/termbase/APPROVED.md).
Style: 0-INBOX/temp/pipeline/vietnamese-style.md.

Quote levels: a string may carry an inner quote written «…». rq(s, 0) renders it “…”, rq(s, 1) ‘…’, rq(s, 2)
drops the marks (third level unquoted). The pentad sentences render their slots at the right level.

usage: python -I -X utf8 -B build_rails_sample_vi.py
"""
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI_DIR = ROOT / "AI_translation/pali/pi-5_split_chapters"
OUT_DIR = ROOT / "AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters"
FORMULAS_MD = ROOT / "0-INBOX/temp/pipeline/pi-5-vi-ai/rails/vi-rails-formulas.md"
RAILS = {b: ROOT / f"AI_translation/vietnamese/pi-{b}-vietnamese-plain-rails_split_chapters" for b in "1234"}


def cap(s):
    return s[:1].upper() + s[1:]


def rq(s, lvl):
    """Render the «…» inner quote of s at nesting level lvl (0 “…”, 1 ‘…’, 2 unquoted)."""
    o, c = {0: ("“", "”"), 1: ("‘", "’"), 2: ("", "")}[lvl]
    return s.replace("«", o).replace("»", c)


# ---------------------------------------------------------------------------------------------------------------
# Book frame and headings (user-approved 2026-11-21, verbatim)
# ---------------------------------------------------------------------------------------------------------------
HOMAGE = "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"           # Namo tassa … (pi-1)
H_ABHI = "# Tạng Vi Diệu Pháp"                                                   # # Abhidhammapiṭake (pi-1)
H_BOOK = "## Các vấn đề tranh luận"                                              # ## Kathāvatthupāḷi


def katha(x):                       # <X>kathā (heading)
    return f"Bàn về {x}"


def katha_end(x):                   # <X>kathā niṭṭhitā.
    return f"Phần bàn về {x} đã hoàn tất."


ORD = {1: "nhất", 2: "hai", 3: "ba", 4: "tư", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười"}


def vaggo(n):                       # N-vaggo (Paṭhamo vaggo …)
    return f"Chương thứ {ORD[n]}"


SAMKHITTAM = "(Tóm lược)"           # (Saṃkhittaṃ)
KA, KHA, GA = "(a)", "(b)", "(c)"   # (Ka) (Kha) (Ga)

# Chapter 1 headings (### / #### / #####)
H = {
    "Puggalakathā": katha("người"),
    "Suddhasaccikaṭṭho": "Thực tại chân thật thuần túy",
    "okāsasaccikaṭṭho": "Thực tại chân thật xét theo nơi chốn",
    "kālasaccikaṭṭho": "Thực tại chân thật xét theo thời gian",
    "avayavasaccikaṭṭho": "Thực tại chân thật xét theo các bộ phận",
    "Anulomapaccanīkaṃ": "Chiều thuận và chiều nghịch",
    "Paccanīkānulomaṃ": "Chiều nghịch và chiều thuận",
    "Suddhikasaṃsandanaṃ": "Sự đối chiếu thuần túy",
    "Opammasaṃsandanaṃ": "Sự đối chiếu bằng phép so sánh",
    "Catukkanayasaṃsandanaṃ": "Sự đối chiếu theo phương pháp bốn cách",
    "Lakkhaṇayuttikathā": "Bàn về lập luận dựa trên đặc tính",
    "Vacanasodhanaṃ": "Sự làm sáng tỏ từ ngữ",
}


def anuyogo(x):                     # X-anuyogo
    return f"Chất vấn về {x}"


ANUYOGA = {
    "Paññattānuyogo": "sự định danh",
    "Gatianuyogo": "cõi tái sinh",
    "Upādāpaññattānuyogo": "sự định danh phụ thuộc",
    "Purisakārānuyogo": "việc làm của con người",
    "Abhiññānuyogo": "các loại hiểu biết trực tiếp",
    "Ñātakānuyogādi": "người thân và các mục khác",
    "Paṭivedhānuyogo": "sự thấu triệt",
    "Saṅghānuyogo": "Tăng đoàn",
    "Saccikaṭṭhasabhāgānuyogo": "những gì cùng bản chất với thực tại chân thật",
}
for _k, _v in ANUYOGA.items():
    H[_k] = anuyogo(_v)


def closer(pali_heading):           # a closing label = the heading + "."
    return H[pali_heading] + "."


KALYANAVAGGO = "Chương thứ nhất về điều tốt đẹp."     # Kalyāṇavaggo paṭhamo.

# ---------------------------------------------------------------------------------------------------------------
# Thesis, answers, questions, quotes (user-approved 2026-11-21, verbatim)
# ---------------------------------------------------------------------------------------------------------------
YES = "Đúng vậy."                   # Āmantā.
YES_Q = "Đúng vậy?"                 # Āmantā? (as written)
NO = "Không nên nói như vậy."       # Na hevaṃ vattabbe.
NO_PE = "Không nên nói như vậy…"    # Na hevaṃ vattabbe…pe….
SHOULD = "Nên nói."                 # Vattabbaṃ.
PE = "…"                            # …pe… (never «.…» / «….»)


def Q(x):                           # "X"ti?
    return f"Có phải {x} không?"


def q(x):                           # the same question after …pe… (lower case)
    return f"có phải {x} không?"


def NANU(x):                        # Nanu Xti?
    return f"Chẳng phải {x} sao?"


NANU_VUTTAM = "Chẳng phải Đức Thế Tôn đã nói thế này sao –"   # Nanu vuttaṃ bhagavatā – "…"
VUTTAM = "Đức Thế Tôn đã nói –"                               # Vuttaṃ bhagavatā – "…"


def na_vattabbam(x):                # Na vattabbaṃ – "X"ti?
    return f"Có phải không nên nói – “{x}” không?"


ATTHEVA = "Có bài kinh như vậy thật không?"                   # Attheva suttantoti?


def tena_hi(x):                     # Tena hi Xti.
    return f"Vậy thì {x}."


def tena_hi_na(x):                  # Tena hi na vattabbaṃ – "X"ti.
    return f"Vậy thì không nên nói – “{x}”."


def katva(x, y):                    # Xti katvā tena ca kāraṇena Yti?
    return f"Có phải vì cho rằng {x}, và vì lý do ấy, {y} không?"


def neu(x, y):                      # Xti, Yti?
    return f"Có phải nếu {x}, thì {y} không?"


def vattabbo(x):                    # "X"ti vattabbo
    return f"nên gọi là “{x}”"


def anna(x, y):                     # Aññaṃ X añño Y
    return f"{x} là khác, {y} là khác"


# ---------------------------------------------------------------------------------------------------------------
# Rebuttal pentad (user-approved; slots P, Q; quote-order repair: the Pāli's garbled "’ is rendered ’”)
# ---------------------------------------------------------------------------------------------------------------
ADMIT = {"niggaha": "Hãy thừa nhận sự bác bỏ.",      # Ājānāhi niggahaṃ.
         "patikamma": "Hãy thừa nhận sự phản bác."}  # Ājānāhi paṭikammaṃ.
RE = "này bạn"                                       # re


def hanci(P, Qs, sep=","):          # Hañci P, tena vata re vattabbe – "Q"ti.
    return f"Nếu {rq(P, 0)}{sep} thì {RE}, chắc chắn nên nói – “{rq(Qs, 1)}”."


def hanci_neg(P, Qs, sep=","):      # Hañci P, no ca vata re vattabbe – "Q"ti.
    return f"Nếu {rq(P, 0)}{sep} thì {RE}, chắc chắn không nên nói – “{rq(Qs, 1)}”."


def noce(P, Qs, note=""):           # No ce pana vattabbe – "Q"ti, no ca vata re vattabbe – "P"ti.
    return f"Còn nếu không nên nói – “{rq(Qs, 1)}”, thì {RE}, chắc chắn{note} không nên nói – “{rq(P, 1)}”."


def yam(P, Qs, te=False, pe=False):  # Yaṃ tattha vadesi – "vattabbe kho – ‘P’, no ca vattabbe – ‘Q’"ti (idaṃ te) micchā.
    head = "Điều bạn nói ở đây là sai lầm của bạn" if te else "Điều bạn nói ở đây là sai"
    return f"{head} – “nên nói – ‘{rq(P, 2)}’, nhưng không nên nói – ‘{rq(Qs, 2)}’”" + (PE if pe else ".")


def pentad(P, Qs, kind="niggaha", label=None, pe=False, line1=None, sep=",", te=False, note3=""):
    """The three (four) lines of an anuloma / paccanīka pentad."""
    l1 = line1 or f"{Q(rq(P, 0))} {YES} {Q(rq(Qs, 0))} {NO}"
    l2 = f"{ADMIT[kind]} {hanci(P, Qs, sep)} {yam(P, Qs, te)}"
    l3 = f"{noce(P, Qs, note3)} {yam(P, Qs, te, pe)}"
    return [l1, l2, l3] + ([label] if label else [])


def tvam_ce(P, Qs, n1="", n2="", n3=""):   # Tvaṃ ce pana maññasi – … Suniggahito ca hosi.
    return (f"Còn nếu bạn cho rằng – “nên nói – ‘{rq(P, 2)}’, nhưng không nên nói – ‘{rq(Qs, 2)}’”, "
            f"thì với chính lời khẳng định này của bạn{n1} ở đây, bạn, người thừa nhận như vậy{n2}, "
            f"nên bị bác bỏ như vậy. Do đó, chúng tôi bác bỏ bạn. Và bạn bị bác bỏ một cách đúng đắn{n3}.")


def ese_ce(P, Qs, n1="", n2=""):           # Ese ce dunniggahite … Dunniggahitā ca homa.
    return (f"Nếu điều này bị bác bỏ một cách sai trái, thì hãy xem ở đây cũng y như vậy{n1}. "
            f"Nên nói – “{rq(P, 1)}”, nhưng không nên nói – “{rq(Qs, 1)}”. "
            f"Và với chính lời khẳng định này ở đây, chúng tôi, những người thừa nhận như vậy, "
            f"không nên bị bạn bác bỏ như vậy. Vậy mà bạn bác bỏ tôi. "
            f"Và chúng tôi bị bác bỏ một cách sai trái{n2}.")


def na_niggahetabbe(P, Qs):                # Na hevaṃ niggahetabbe. Tena hi yaṃ niggaṇhāsi – "hañci … micchā.
    return (f"Không nên bị bác bỏ như vậy. Vậy thì, điều bạn đã bác bỏ – “nếu {rq(P, 1)}, thì {RE}, "
            f"chắc chắn nên nói – ‘{rq(Qs, 2)}’. Điều bạn nói ở đây là sai – "
            f"‘nên nói – {rq(P, 2)}, nhưng không nên nói – {rq(Qs, 2)}’”.")


KATE = ("Vậy thì, sự bác bỏ nào đã được thực hiện, sự bác bỏ ấy được thực hiện sai trái. "
        "Sự phản bác được thực hiện đúng đắn. Việc dẫn dắt lập luận được thực hiện đúng đắn.")
#   Tena hi ye kate niggahe se niggahe dukkaṭe. Sukate paṭikamme. Sukatā paṭipādanāti.

LABEL = {
    "Anulomapañcakaṃ": "Nhóm năm phần theo chiều thuận.",
    "Paccanīkapañcakaṃ": "Nhóm năm phần theo chiều nghịch.",
    "Paṭikammacatukkaṃ": "Nhóm bốn phần về sự phản bác.",
    "Niggahacatukkaṃ": "Nhóm bốn phần về sự bác bỏ.",
    "Upanayanacatukkaṃ": "Nhóm bốn phần về sự áp dụng.",
    "Niggamanacatukkaṃ": "Nhóm bốn phần về sự kết luận.",
    "Aṭṭhakaniggaho": "Nhóm tám sự bác bỏ.",
}


def niggaho(n):                     # Paṭhamo … Sattamo niggaho.
    return f"Sự bác bỏ thứ {ORD[n]}."


# Speaker notes and editorial brackets
NOTE_SAKA = "[với dấu hiệu này, câu hỏi của người theo học thuyết của chúng ta được trình bày]"
NOTE_PARA = "[với dấu hiệu này, câu hỏi của người theo học thuyết khác được trình bày]"
TIKA = "cần tham khảo Phụ chú giải"  # ṭīkā oloketabbā


def var_sp(sigla, word):            # spelling-only variant
    return f" [khác chính tả ({sigla}): {word}]"


def var(sigla, word):               # other variant
    return f" [dị bản ({sigla}): {word}]"


# Citations (inside brackets)
CIT = {"ma. ni.": "Trung Bộ Kinh", "a. ni.": "Tăng Chi Bộ Kinh", "saṃ. ni.": "Tương Ưng Bộ Kinh",
       "su. ni.": "Kinh Tập", "dha. pa.": "Kinh Pháp Cú", "itivu.": "Kinh Phật Thuyết Như Vậy",
       "cūḷani.": "Tiểu Nghĩa Thích", "pu. pa.": "Định danh các hạng người", "bahūsu": "Nhiều bản"}

# ---------------------------------------------------------------------------------------------------------------
# Core terms of the debate (user-approved 2026-11-21)
# ---------------------------------------------------------------------------------------------------------------
SP = "như một thực tại chân thật và tối hậu"      # saccikaṭṭhaparamatthena
PERSON = "người"                                   # puggalo
SAKAVADI = "người theo học thuyết của chúng ta"   # sakavādī
PARAVADI = "người theo học thuyết khác"           # paravādī


def up(x, neg=False, sp=True):      # X upalabbhati (saccikaṭṭhaparamatthena)
    return f"{x} {'không ' if neg else ''}được tìm thấy" + (f" {SP}" if sp else "")


P_UP = up(PERSON)                   # puggalo upalabbhati saccikaṭṭhaparamatthena
P_NUP = up(PERSON, True)            # puggalo nupalabbhati saccikaṭṭhaparamatthena


def yo_tato(neg=False):             # yo saccikaṭṭho paramattho, tato so puggalo (n)upalabbhati saccikaṭṭhaparamatthena
    return f"người ấy {'không ' if neg else ''}được tìm thấy {SP} theo cùng cách như một thực tại chân thật và tối hậu được tìm thấy"


SUTTA_ATTHI = "Đức Thế Tôn đã nói – «có người thực hành vì lợi ích của bản thân»"
#   vuttaṃ bhagavatā – "atthi puggalo attahitāya paṭipanno"   (the sutta words: pi-4)
ATTHI_ATTAHITA = "có người thực hành vì lợi ích của bản thân"                     # (pi-4)
BHAGAVA_SACCA = ("Đức Thế Tôn là người nói sự thật, nói đúng lúc, nói điều có thật, nói đúng như thật, "
                 "nói không sai lệch, nói không khác đi")
#   bhagavā saccavādī kālavādī bhūtavādī tathavādī avitathavādī anaññathavādī

# Aggregates, bases, elements, faculties (names as in pi-1 / pi-2 rails; Kathāvatthu order)
RUPA, VEDANA, SANNA, SANKHARA, VINNANA = "vật chất", "cảm giác", "tri giác", "các tạo tác", "thức"
AYATANA = [("cakkhāyatana", "lĩnh vực mắt"), ("sotāyatana", "lĩnh vực tai"), ("ghānāyatana", "lĩnh vực mũi"),
           ("jivhāyatana", "lĩnh vực lưỡi"), ("kāyāyatana", "lĩnh vực thân"), ("rūpāyatana", "lĩnh vực hình sắc"),
           ("saddāyatana", "lĩnh vực âm thanh"), ("gandhāyatana", "lĩnh vực mùi"), ("rasāyatana", "lĩnh vực vị"),
           ("phoṭṭhabbāyatana", "lĩnh vực vật xúc chạm"), ("manāyatana", "lĩnh vực ý"),
           ("dhammāyatana", "lĩnh vực đối tượng của ý")]                                        # (pi-1)
DHATU = [("cakkhudhātu", "yếu tố mắt"), ("sotadhātu", "yếu tố tai"), ("ghānadhātu", "yếu tố mũi"),
         ("jivhādhātu", "yếu tố lưỡi"), ("kāyadhātu", "yếu tố thân"), ("rūpadhātu", "yếu tố hình sắc"),
         ("saddadhātu", "yếu tố âm thanh"), ("gandhadhātu", "yếu tố mùi"), ("rasadhātu", "yếu tố vị"),
         ("phoṭṭhabbadhātu", "yếu tố vật xúc chạm"), ("cakkhuviññāṇadhātu", "yếu tố thức qua mắt"),
         ("sotaviññāṇadhātu", "yếu tố thức qua tai"), ("ghānaviññāṇadhātu", "yếu tố thức qua mũi"),
         ("jivhāviññāṇadhātu", "yếu tố thức qua lưỡi"), ("kāyaviññāṇadhātu", "yếu tố thức qua thân"),
         ("manodhātu", "yếu tố ý"), ("manoviññāṇadhātu", "yếu tố ý thức"),
         ("dhammadhātu", "yếu tố đối tượng của ý")]                                            # (pi-2)
INDRIYA = [("cakkhundriya", "năng lực mắt"), ("sotindriya", "năng lực tai"), ("ghānindriya", "năng lực mũi"),
           ("jivhindriya", "năng lực lưỡi"), ("kāyindriya", "năng lực thân"), ("manindriya", "năng lực ý"),
           ("jīvitindriya", "năng lực sống"), ("itthindriya", "năng lực nữ tính"),
           ("purisindriya", "năng lực nam tính"), ("sukhindriya", "năng lực dễ chịu"),
           ("dukkhindriya", "năng lực khó chịu"), ("somanassindriya", "năng lực niềm vui"),
           ("domanassindriya", "năng lực nỗi buồn"), ("upekkhindriya", "năng lực bình thản"),
           ("saddhindriya", "năng lực niềm tin"), ("vīriyindriya", "năng lực tinh tấn"),
           ("satindriya", "năng lực tỉnh thức"), ("samādhindriya", "năng lực định tâm"),
           ("paññindriya", "năng lực trí tuệ"), ("anaññātaññassāmītindriya", "năng lực biết được điều chưa từng biết"),
           ("aññindriya", "năng lực hiểu biết trọn vẹn"),
           ("aññātāvindriya", "năng lực của người đã hiểu biết trọn vẹn")]                    # (pi-2)
A = dict(AYATANA)
D = dict(DHATU)
I = dict(INDRIYA)
ANNATAVI = I["aññātāvindriya"]
ANNI = I["aññindriya"]
MICCHA = ["quan điểm sai lầm", "tư duy sai lầm", "lời nói sai lầm", "hành động sai lầm", "sinh kế sai lầm",
          "nỗ lực sai lầm", "tỉnh thức sai lầm", "định tâm sai lầm"]                            # (pi-2)
SAMMA = ["quan điểm đúng đắn", "tư duy đúng đắn", "lời nói đúng đắn", "hành động đúng đắn", "sinh kế đúng đắn",
         "nỗ lực đúng đắn", "tỉnh thức đúng đắn", "định tâm đúng đắn"]                           # (pi-1)
ANICCA = ("vô thường, do điều kiện tạo thành, sinh khởi tùy thuộc vào điều kiện, có bản chất diệt tận, "
          "có bản chất suy tàn, có bản chất phai nhạt, có bản chất chấm dứt, có bản chất biến đổi")
#   aniccaṃ saṅkhataṃ paṭiccasamuppannaṃ khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhammaṃ vipariṇāmadhammaṃ
SAPHALA_K = ("có kết quả, có quả trổ, có kết quả đáng mong muốn, có kết quả đáng yêu mến, có kết quả đáng ưa thích, "
             "có kết quả không pha tạp, đưa đến sự dễ chịu, có quả trổ dễ chịu")
#   saphalā savipākā iṭṭhaphalā kantaphalā manuññaphalā asecanakaphalā sukhudrayā sukhavipākā
SAPHALA_A = ("có kết quả, có quả trổ, có kết quả không đáng mong muốn, có kết quả không đáng yêu mến, "
             "có kết quả không đáng ưa thích, có kết quả pha tạp, đưa đến sự khó chịu, có quả trổ khó chịu")
#   saphalā savipākā aniṭṭhaphalā akantaphalā amanuññaphalā secanakaphalā dukkhudrayā dukkhavipākā
LOKA = "từ thế gian này sang thế gian khác, từ thế gian khác sang thế gian này"
#   asmā lokā paraṃ lokaṃ, parasmā lokā imaṃ lokaṃ   («thế gian này»: pi-4)
SANDHAVATI = f"người trôi lăn {LOKA}"                       # puggalo sandhāvati …
SVEVA = f"chính người ấy trôi lăn {LOKA}"                    # sveva puggalo sandhāvati …
KK = "người làm và người khiến làm"                          # kattā kāretā
KALYANA_KAMMA = "các nghiệp tốt đẹp và xấu ác"               # kalyāṇapāpakāni kammāni
TASSA_TASSEVA = ("đối với từng người như vậy, không có sự đi đến tận cùng của khổ đau, không có sự cắt đứt "
                 "vòng luân chuyển, không có sự nhập Niết-bàn trọn vẹn không còn bám víu")
#   Tassa tasseva natthi dukkhassa antakiriyā, natthi vaṭṭupacchedo, natthi anupādāparinibbānaṃ
NATURE = [("Mahāpathavī", "đại địa"), ("mahāsamuddo", "đại dương"),
          ("sinerupabbatarājā", "núi Tu-di, vua của các ngọn núi"), ("āpo", "nước"), ("tejo", "lửa"),
          ("vāyo", "gió")]
TINA = "cỏ, gỗ và cây rừng"                                  # tiṇakaṭṭhavanappatayo
KAYA_K = ("gọi là thân hay gọi là thân thể, gọi là thân thể hay gọi là thân, khi xem thân như một "
          "không thể tách rời, thì đều là một, cùng một nghĩa, như nhau, ngang nhau, cùng một loại")
#   kāyoti vā sarīranti vā, sarīranti vā kāyoti vā, kāyaṃ appiyaṃ karitvā esese ekaṭṭhe same samabhāge tajjāte
JIVA_K = ("gọi là người hay gọi là linh hồn, gọi là linh hồn hay gọi là người, khi xem người như một "
          "không thể tách rời, thì đều là một, cùng một nghĩa, như nhau, ngang nhau, cùng một loại")
TAM_JIVAM = "linh hồn cũng chính là thân thể"                # taṃ jīvaṃ taṃ sarīraṃ
ANNAM_JIVAM = anna("linh hồn", "thân thể")                   # aññaṃ jīvaṃ aññaṃ sarīraṃ
SENIYA = "Sê-ni-gia"
SACCATO = "đề ra tự ngã như là sự thật, như là điều chắc chắn"                               # (pi-4)
DITTHE = "ngay trong đời này"                                                                 # (pi-4)
ABHISAMPARAYA = "trong đời sau"                                                               # (pi-4)
SASSATAVADO = "bậc đạo sư theo học thuyết về sự trường tồn"                                   # (pi-4)
UCCHEDAVADO = "bậc đạo sư theo học thuyết về sự đoạn diệt"                                    # (pi-4)
TINAM_ONE = "ba bậc đạo sư"                                                                   # (pi-4)

# Person types (pi-4 names)
PERSONS = [("sotāpanno", "bậc vào dòng"), ("sakadāgāmī", "bậc trở lại một lần"), ("anāgāmī", "bậc không trở lại"),
           ("arahā", "bậc A-la-hán"), ("ubhatobhāgavimutto", "người được giải thoát theo cả hai cách"),
           ("paññāvimutto", "người được giải thoát nhờ trí tuệ"), ("kāyasakkhi", "người chứng nghiệm bằng thân"),
           ("diṭṭhippatto", "người đạt đến quan điểm"), ("saddhāvimutto", "người được giải thoát nhờ niềm tin"),
           ("dhammānusārī", "người đi theo Giáo Pháp"), ("saddhānusārī", "người đi theo niềm tin")]   # (pi-4)
PN = dict(PERSONS)
KIN = [("mātā", "mẹ"), ("pitā", "cha"), ("bhātā", "anh em trai"), ("bhaginī", "chị em gái"),
       ("khattiyo", "người thuộc giai cấp quý tộc"), ("brāhmaṇo", "bà-la-môn"),
       ("vesso", "người thuộc giai cấp thương nhân"), ("suddo", "người thuộc giai cấp lao động"),
       ("gahaṭṭho", "người tại gia"), ("pabbajito", "người xuất gia"), ("devo", "vị trời"), ("manusso", "con người")]
KN = dict(KIN)

# ---------------------------------------------------------------------------------------------------------------
# Strings taken unchanged from the approved pi-1 … pi-4 Vietnamese rails (asserted at build time)
# ---------------------------------------------------------------------------------------------------------------
REUSED = [  # (Pāli, Vietnamese, book)
    ("Namo tassa bhagavato arahato sammāsambuddhassa", HOMAGE, "1"),
    ("# Abhidhammapiṭake", H_ABHI, "1"),
] + [(p, v, "1") for p, v in AYATANA] + [(p, v, "2") for p, v in DHATU] + [(p, v, "2") for p, v in INDRIYA] + [
    ("micchādiṭṭhi … micchāsamādhi (one by one)", v, "2") for v in MICCHA] + [
    ("sammādiṭṭhi … sammāsamādhi (one by one)", v, "1") for v in SAMMA] + [
    ("rūpakkhandha … (aggregate names)", "khối vật chất, khối cảm giác, khối tri giác, khối tạo tác, khối thức", "2"),
    ("atthi(ekacco) puggalo attahitāya paṭipanno", ATTHI_ATTAHITA, "4"),
    ("(diṭṭhe ceva dhamme) attānaṃ saccato thetato paññapeti", SACCATO, "4"),
    ("diṭṭhe ceva dhamme", DITTHE, "4"),
    ("abhisamparāyaṃ", "như là điều chắc chắn trong đời sau", "4"),
    ("sassatavādo satthā", SASSATAVADO, "4"),
    ("ucchedavādo satthā", UCCHEDAVADO, "4"),
    ("Tatra yvāyaṃ satthā", "Trong số đó, bậc đạo sư nào", "4"),
    ("Idha panekacco satthā", "ở đời này, có bậc đạo sư", "4"),
    ("tayo satthāro", TINAM_ONE, "4"),
    ("imaṃ lokaṃ", "thế gian này", "4"),
    ("dukkhassantakaro hoti", "trở thành người đi đến tận cùng của khổ đau", "4"),
    ("Puggalapaññatti (book title)", "Định danh các hạng người", "4"),
    ("mātikā", "ma trận", "1"),
    ("Māra", "Ma vương", "4"),
    ("ma. ni. (citation)", "Trung Bộ Kinh", "2"),
    ("a. ni. (citation)", "Tăng Chi Bộ Kinh", "2"),
    ("nīlaṃ pītakaṃ lohitakaṃ odātaṃ", "màu xanh, màu vàng, màu đỏ, màu trắng", "1"),
    ("sanidassana", "thấy được", "1"),
    ("anidassana", "không thấy được", "1"),
    ("sappaṭigha", "có tính va chạm", "1"),
    ("appaṭigha", "không có tính va chạm", "1"),
    ("ekavokārabhavo", "sự hiện hữu gồm một khối", "2"),
    ("catuvokārabhavo", "sự hiện hữu gồm bốn khối", "2"),
    ("pañcavokārabhavo", "sự hiện hữu gồm năm khối", "2"),
    ("asaṅkhatā dhātu", "yếu tố không do điều kiện tạo thành", "1"),
    ("anattā", "không phải là tự ngã", "2"),
    ("kāye kāyānupassī viharati", "đối với thân", "2"),
    ("kāyānupassī viharati", "sống quán sát thân", "2"),
    ("dhammesu dhammānupassī viharati", "đối với các hiện tượng, vị ấy sống quán sát các hiện tượng", "2"),
    ("vedanāsu…pe… citte…", "đối với các cảm giác", "2"),
    ("peto / nerayiko / tiracchānagato", "ngạ quỷ", "2"),
    ("nerayiko", "chúng sinh địa ngục", "2"),
    ("tiracchānagato", "loài súc sinh", "2"),
    ("gahaṭṭho / pabbajito", "người tại gia và người xuất gia", "2"),
    ("brāhmaṇo", "bà-la-môn", "2"),
    ("sukhaṃ … adukkhamasukhaṃ vā", "dễ chịu, hoặc khó chịu, hoặc không khó chịu cũng không dễ chịu", "2"),
    ("sukhā vedanā", "cảm giác dễ chịu", "2"),
    ("dukkhā vedanā", "cảm giác khó chịu", "2"),
    ("adukkhamasukhā vedanā", "cảm giác không khó chịu cũng không dễ chịu", "2"),
    ("kusalā / akusalā / abyākatā vedanā", "cảm giác bất thiện", "2"),
    ("abyākatā vedanā", "cảm giác không xác định về mặt đạo đức", "2"),
    ("saccato thetato", "như là sự thật, như là điều chắc chắn", "2"),
] + [(p, v, "4") for p, v in PERSONS]

# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------


def build_preamble():
    return [[HOMAGE + " ^T-1"], [H_ABHI + " ^0"], [H_BOOK + " ^5-0"]]


def build_ch1():
    S = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        S.append(lines)

    def head(i, level, text):
        add(i, "#" * level + " " + text)

    # ---- Suddhasaccikaṭṭho, anuloma ---------------------------------------------------------------------------
    head("5-1-0", 3, H["Puggalakathā"])
    head("5-1-1-0", 4, H["Suddhasaccikaṭṭho"])
    head("5-1-1-1-0", 5, H["Anulomapaccanīkaṃ"])
    Y, YN = yo_tato(), yo_tato(True)
    l = pentad(P_UP, Y, label=LABEL["Anulomapañcakaṃ"], note3=var("Syā., Pī.", "no vata re"))
    l[0] = (f"{NOTE_SAKA} Có phải {P_UP}{var_sp('Syā., Pī., Ka., Sī.', 'saccikaṭṭhaparamaṭṭhenāti')} không? "
            f"{YES} {Q(Y)} {NO}")
    add("5-1", *l)
    l = pentad(P_NUP, YN, kind="patikamma", label=LABEL["Paṭikammacatukkaṃ"])
    l[0] = f"{NOTE_PARA} " + l[0]
    add("5-2", *l)

    def niggaha4(P, Qs, label, first, notes=False):
        if first == "tvam":
            l1 = tvam_ce(P, Qs, var("Syā.", "tvaṃ") [:-1] + f"; {TIKA}]" if notes else "",
                         f" [{TIKA}]" if notes else "", var("Syā.", "suniggahitova") if notes else "")
        else:
            l1 = ese_ce(P, Qs, var_sp("Syā.", "hevameva") if notes else "",
                        var("Syā.", "dunniggahitāva") if notes else "")
        out = [l1, f"{hanci(P, Qs)} {yam(P, Qs)}", f"{noce(P, Qs)} {yam(P, Qs, te=True)}"]
        return out + ([label] if label else [])

    add("5-3", *niggaha4(P_NUP, YN, LABEL["Niggahacatukkaṃ"], "tvam", notes=True))
    add("5-4", *niggaha4(P_UP, Y, LABEL["Upanayanacatukkaṃ"], "ese", notes=True))

    def niggamana(P, Qs, n):
        return [na_niggahetabbe(P, Qs), f"{noce(P, Qs)} {yam(P, Qs, te=True)} {KATE}",
                LABEL["Niggamanacatukkaṃ"], niggaho(n)]

    add("5-5", *niggamana(P_UP, Y, 1))

    # ---- Suddhasaccikaṭṭho, paccanīka ---------------------------------------------------------------------------
    head("5-1-2-0", 4, H["Suddhasaccikaṭṭho"])
    head("5-1-2-1-0", 5, H["Paccanīkānulomaṃ"])
    add("5-6", *pentad(P_NUP, YN, label=LABEL["Paccanīkapañcakaṃ"]))
    add("5-7", *pentad(P_UP, Y, kind="patikamma", label=LABEL["Paṭikammacatukkaṃ"]))
    add("5-8", *niggaha4(P_UP, Y, None, "tvam"))
    add("5-9", *niggaha4(P_NUP, YN, LABEL["Upanayanacatukkaṃ"], "ese"))
    add("5-10", *niggamana(P_NUP, YN, 2))

    # ---- okāsa / kāla / avayava ----------------------------------------------------------------------------------
    where = [("okāsasaccikaṭṭho", "ở mọi nơi"), ("kālasaccikaṭṭho", "vào mọi lúc"),
             ("avayavasaccikaṭṭho", "trong mọi thứ")]               # sabbattha / sabbadā / sabbesu
    n, sid, hid = 3, 11, 3
    for neg, mark, method in ((False, KA, "Anulomapaccanīkaṃ"), (True, KHA, "Paccanīkānulomaṃ")):
        for key, adv in where:
            head(f"5-1-{hid}-0", 4, f"{mark} {H[key]}")
            head(f"5-1-{hid}-1-0", 5, H[method])
            P = P_NUP if neg else P_UP
            Qs = f"{P} {adv}"
            lab = LABEL["Aṭṭhakaniggaho"] if n == 8 else niggaho(n)
            add(f"5-{sid}", *pentad(P, Qs, pe=True, label=lab))
            n, sid, hid = n + 1, sid + 1, hid + 1

    # ---- Suddhikasaṃsandanaṃ --------------------------------------------------------------------------------------
    head("5-1-9-0", 4, H["Suddhikasaṃsandanaṃ"])
    P = f"{P_UP}, và {up(RUPA)}"
    add("5-17", *pentad(P, anna(RUPA, PERSON), pe=True))
    l1 = (f"Có phải {P_UP}, và {up(VEDANA)}{PE} và {up(SANNA, sp=False)}{PE} và {up(SANKHARA, sp=False)}{PE} "
          f"và {up(VINNANA)} không? {YES} {Q(anna(VINNANA, PERSON))} {NO}")
    P = f"{P_UP}, và {up(VINNANA)}"
    add("5-18", *pentad(P, anna(VINNANA, PERSON), pe=True, line1=l1))
    ay = [v for _, v in AYATANA]
    add("5-19", f"{cap(P_UP)}, và {up(ay[0])}{PE} " + f"{PE} ".join(f"và {up(x, sp=False)}" for x in ay[1:-1])
        + f"{PE} và {up(ay[-1])}{PE}")
    dh = [v for _, v in DHATU]
    add("5-20", f"Và {up(dh[0])}{PE} " + f"{PE} ".join(f"và {up(x, sp=False)}" for x in dh[1:-1])
        + f"{PE} và {up(dh[-1])}{PE}")
    ind = [v for _, v in INDRIYA]
    l1 = (f"Và có phải {up(ind[0])}{PE} " + f"{PE} ".join(f"và {up(x, sp=False)}" for x in ind[1:-1])
          + f"{PE} và {up(ind[-1])} không? {YES} {Q(anna(ANNATAVI, PERSON))} {NO}")
    add("5-21", *pentad(f"{P_UP}, và {up(ANNATAVI)}", anna(ANNATAVI, PERSON), pe=True, line1=l1))
    cite = f"[{CIT['pu. pa.']}, ma trận 4.24; {CIT['a. ni.']} 4.95-96]"
    P = f"{SUTTA_ATTHI}, và {up(RUPA)}"
    l1 = f"{cite} {Q(P_NUP)} {YES} {Q(rq(P, 0))} {YES} {Q(anna(RUPA, PERSON))} {NO}"
    add("5-22", *pentad(P, anna(RUPA, PERSON), kind="patikamma", pe=True, line1=l1))
    P = f"{SUTTA_ATTHI}, và {up(VINNANA)}"
    l1 = (f"{Q(P_NUP)} {YES} Có phải {rq(SUTTA_ATTHI, 0)}, và {up(VEDANA, sp=False)}{PE} và "
          f"{up(SANNA, sp=False)}{PE} và {up(SANKHARA, sp=False)}{PE} và {up(VINNANA)} không? {YES} "
          f"{Q(anna(VINNANA, PERSON))} {NO}")
    add("5-23", *pentad(P, anna(VINNANA, PERSON), kind="patikamma", pe=True, line1=l1))
    add("5-24", f"{Q(P_NUP)} {YES} {rq(SUTTA_ATTHI, 0)}, và {up(A['cakkhāyatana'])}{PE} "
        f"và {up(A['sotāyatana'], sp=False)}{PE} và {up(A['dhammāyatana'])}{PE}")
    add("5-25", f"Và {up(D['cakkhudhātu'])}{PE} " + f"{PE} ".join(
        f"và {up(D[k], sp=False)}" for k in ("kāyadhātu", "rūpadhātu", "phoṭṭhabbadhātu", "cakkhuviññāṇadhātu",
                                             "manoviññāṇadhātu")) + f"{PE} và {up(D['dhammadhātu'])}{PE}")
    add("5-26", f"Và {up(I['cakkhundriya'])}{PE} và {up(I['sotindriya'])}{PE} và {ANNI}"
        f"{var(CIT['bahūsu'], 'aññātāvindriyañca')} được tìm thấy {SP}{PE}")
    P = f"{SUTTA_ATTHI}, và {up(ANNATAVI)}"
    l1 = f"{Q(P_NUP)} {YES} {Q(rq(P, 0))} {YES} {Q(anna(ANNATAVI, PERSON))} {NO}"
    add("5-27", *pentad(P, anna(ANNATAVI, PERSON), kind="patikamma", pe=True, line1=l1,
                        label=closer("Suddhikasaṃsandanaṃ")))

    # ---- Opammasaṃsandanaṃ -------------------------------------------------------------------------------------------
    head("5-1-10-0", 4, H["Opammasaṃsandanaṃ"])

    def opamma(a, b, sutta=False, chain="", kind=None, label=None, i=None):
        """a / b: the two compared items; chain: the …pe… part of line 1 between a and b."""
        first = f"{up(a)}, và {up(b)}, {anna(a, b)}"
        q1 = f"{up(a)}{chain}, và {up(b)}, {anna(a, b)}" if not chain else f"{up(a)}, {chain}, {anna(a, b)}"
        second = (f"{SUTTA_ATTHI}, và {up(a)}" if sutta else f"{P_UP}, và {up(a)}")
        P = f"{first}, {second}"
        l1 = f"{Q(q1)} {YES} {Q(rq(second, 0))} {YES} {Q(anna(a, PERSON))} {NO}"
        return pentad(P, anna(a, PERSON), kind=kind or ("patikamma" if sutta else "niggaha"), pe=True,
                      line1=l1, sep=";", label=label)

    add("5-28", *opamma(RUPA, VEDANA))
    ch = f"và {up(SANNA, sp=False)}{PE} và {up(SANKHARA, sp=False)}{PE} và {up(VINNANA)}"
    add("5-29", *opamma(RUPA, VINNANA, chain=ch))
    add("5-30", f"{cap(up(VEDANA))}, và {up(SANNA, sp=False)}{PE} và {up(SANKHARA, sp=False)}{PE} "
        f"và {up(VINNANA, sp=False)}{PE} và {up(RUPA)}{PE}")
    add("5-31", f"{cap(up(SANNA))}, và {up(SANKHARA, sp=False)}{PE} và {up(VINNANA, sp=False)}{PE} "
        f"và {up(RUPA, sp=False)}{PE} và {up(VEDANA)}{PE}")
    add("5-32", f"{cap(up(SANKHARA))}, và {up(VINNANA, sp=False)}{PE} và {up(RUPA, sp=False)}{PE} "
        f"và {up(VEDANA, sp=False)}{PE} và {up(SANNA)}{PE}")
    ch = f"và {up(RUPA, sp=False)}{PE} và {up(VEDANA, sp=False)}{PE} và {up(SANNA, sp=False)}{PE} và {up(SANKHARA)}"
    l = opamma(VINNANA, SANKHARA, chain=ch)
    add("5-33", *l)
    add("5-34", f"{cap(up(A['cakkhāyatana']))}, và {up(A['sotāyatana'], sp=False)}{PE} và "
        f"{up(A['dhammāyatana'])}{PE} {up(A['sotāyatana'], sp=False)}{PE} {up(A['dhammāyatana'])}, và "
        f"{up(A['cakkhāyatana'], sp=False)}{PE} và {up(A['manāyatana'])}{PE}")
    add("5-35", f"{cap(up(D['cakkhudhātu']))}, và {up(D['sotadhātu'], sp=False)}{PE} và "
        f"{up(D['dhammadhātu'])}{PE} {up(D['sotadhātu'], sp=False)}{PE} {up(D['dhammadhātu'])}, và "
        f"{up(D['cakkhudhātu'], sp=False)}{PE} và {up(D['manoviññāṇadhātu'])}{PE}")
    first = f"{up(ANNATAVI)}, và {up(ANNI)}, {anna(ANNATAVI, ANNI)}"
    second = f"{P_UP}, và {up(ANNATAVI)}"
    l1 = (f"Có phải {up(I['cakkhundriya'])}, và {up(I['sotindriya'], sp=False)}{PE} và {up(ANNATAVI)}{PE} "
          f"{up(I['sotindriya'], sp=False)}{PE} {up(ANNATAVI)}{PE} và {up(I['cakkhundriya'], sp=False)}{PE} "
          f"và {up(ANNI)}, {anna(ANNATAVI, ANNI)} không? {YES} {Q(second)} {YES} {Q(anna(ANNATAVI, PERSON))} {NO}")
    add("5-36", *pentad(f"{first}, {second}", anna(ANNATAVI, PERSON), pe=True, line1=l1, sep=";"))
    add("5-37", *opamma(RUPA, VEDANA, sutta=True))
    add("5-38", f"{cap(up(RUPA))}, và {up(SANNA, sp=False)}{PE} và {up(SANKHARA, sp=False)}{PE} "
        f"và {up(VINNANA)}{PE}")
    add("5-39", f"{cap(up(VEDANA))}, và {up(SANNA, sp=False)}{PE} và {up(SANKHARA, sp=False)}{PE} "
        f"và {up(VINNANA, sp=False)}{PE} và {up(RUPA)}{PE}")
    add("5-40", f"{cap(up(SANNA))}, và {up(SANKHARA, sp=False)}{PE} và {up(VINNANA, sp=False)}{PE} "
        f"và {up(RUPA, sp=False)}{PE} và {up(VEDANA)}{PE}")
    add("5-41", f"{cap(up(SANKHARA))}, và {up(VINNANA, sp=False)}{PE} và {up(RUPA, sp=False)}{PE} "
        f"và {up(VEDANA, sp=False)}{PE} và {up(SANNA)}{PE}")
    add("5-42", f"{cap(up(VINNANA))}, và {up(RUPA, sp=False)}{PE} và {up(VEDANA, sp=False)}{PE} "
        f"và {up(SANNA, sp=False)}{PE} và {up(SANKHARA)}{PE}")
    add("5-43", f"{cap(up(A['cakkhāyatana']))}, và {up(A['sotāyatana'], sp=False)}{PE} và "
        f"{up(A['dhammāyatana'])}{PE} {up(A['sotāyatana'], sp=False)}{PE} {up(A['dhammāyatana'])}, và "
        f"{up(A['cakkhāyatana'], sp=False)}{PE} và {up(A['manāyatana'])}{PE}")
    add("5-44", f"{cap(up(D['cakkhudhātu']))}, và {up(D['sotadhātu'], sp=False)}{PE} và "
        f"{up(D['dhammadhātu'])}{PE} {up(D['sotadhātu'])}{PE} {up(D['dhammadhātu'])}, và "
        f"{up(D['cakkhudhātu'], sp=False)}{PE} và {up(D['manoviññāṇadhātu'])}{PE}")
    second = f"{SUTTA_ATTHI}, và {up(ANNATAVI)}"
    l1 = (f"Có phải {up(I['cakkhundriya'])}, và {up(I['sotindriya'], sp=False)}{PE} và {up(ANNATAVI)}{PE} "
          f"{up(I['sotindriya'], sp=False)}{PE} {up(ANNATAVI)}, và {up(I['cakkhundriya'], sp=False)}{PE} "
          f"và {up(ANNI)}; {anna(ANNATAVI, ANNI)} không? {YES} {Q(rq(second, 0))} {YES} "
          f"{Q(anna(ANNATAVI, PERSON))} {NO}")
    add("5-45", *pentad(f"{first}, {second}", anna(ANNATAVI, PERSON), kind="patikamma", pe=True, line1=l1,
                        sep=";", label=closer("Opammasaṃsandanaṃ")))

    # ---- Catukkanayasaṃsandanaṃ ----------------------------------------------------------------------------------------
    head("5-1-11-0", 4, H["Catukkanayasaṃsandanaṃ"])

    def is_p(x):                    # X puggalo
        return f"{x} là người"

    def in_x(x):                    # Xsmiṃ puggalo
        return f"người ở trong {x}"

    def apart(x):                   # aññatra X puggalo
        return f"người tách rời khỏi {x}"

    def in_p(x):                    # puggalasmiṃ X
        return f"{x} ở trong người"

    def four(x, skip_first=False):
        parts = ([] if skip_first else [is_p(x)]) + [in_x(x), apart(x), in_p(x)]
        return f"{PE} ".join(parts)

    add("5-46", *pentad(P_UP, is_p(RUPA), pe=True))
    l1 = f"{Q(P_UP)} {YES} Có phải {four(RUPA, True)} không? {NO}"
    add("5-47", *pentad(P_UP, in_p(RUPA), pe=True, line1=l1))
    l = pentad(P_UP, in_p(VINNANA), pe=True)
    add("5-48", f"{Q(P_UP)} {YES} Có phải {four(VEDANA)}{PE}", f"{cap(four(SANNA))}{PE}",
        f"{cap(four(SANKHARA))}{PE}", f"{cap(four(VINNANA))} không? {NO}", l[1], l[2])
    l = pentad(P_UP, in_p(ANNATAVI), pe=True)
    add("5-49", f"{Q(P_UP)} {YES} Có phải {four(A['cakkhāyatana'])}{PE} {four(A['dhammāyatana'])}{PE}",
        f"{cap(four(D['cakkhudhātu']))}{PE} {four(D['dhammadhātu'])}{PE}",
        f"{cap(four(I['cakkhundriya']))}{PE} {four(ANNATAVI)} không? {NO}", l[1], l[2])
    QS = Q(rq(SUTTA_ATTHI, 0))
    add("5-50", *pentad(SUTTA_ATTHI, is_p(RUPA), kind="patikamma", pe=True,
                        line1=f"{Q(P_NUP)} {YES} {QS} {YES} {Q(is_p(RUPA))} {NO}"))
    l = pentad(SUTTA_ATTHI, in_p(VINNANA), kind="patikamma", pe=True)
    add("5-51", f"{Q(P_NUP)} {YES} {QS} {YES} Có phải {four(RUPA, True)}{PE}", f"{cap(four(VEDANA))}{PE}",
        f"{cap(four(SANNA))}{PE}", f"{cap(four(SANKHARA))}{PE}", f"{cap(four(VINNANA))} không? {NO}", l[1], l[2])
    l = pentad(SUTTA_ATTHI, in_p(ANNATAVI), kind="patikamma", pe=True)
    add("5-52", f"{Q(P_NUP)} {YES} {QS} {YES} Có phải {four(A['cakkhāyatana'])}{PE} {four(A['dhammāyatana'])}{PE}",
        f"{cap(four(D['cakkhudhātu']))}{PE} {four(D['dhammadhātu'])}{PE}",
        f"{cap(four(I['cakkhundriya']))}{PE} {four(ANNATAVI)} không? {NO}", l[1], l[2],
        closer("Catukkanayasaṃsandanaṃ"))

    # ---- Lakkhaṇayuttikathā -----------------------------------------------------------------------------------------
    head("5-1-12-0", 4, H["Lakkhaṇayuttikathā"])
    marks = f"{PE} ".join(f"người {m}" for m in (
        "có điều kiện", "không có điều kiện", "do điều kiện tạo thành", "không do điều kiện tạo thành",
        "trường tồn", "không trường tồn", "có dấu hiệu", "không có dấu hiệu"))
    #   puggalo sappaccayo … appaccayo … saṅkhato … asaṅkhato … sassato … asassato … sanimitto … animitto
    add("5-53", f"{Q(P_UP)} {YES} Có phải {marks} không? {NO} {SAMKHITTAM}")
    add("5-54", f"{Q(P_NUP)} {YES} {QS} {YES} Có phải {marks} không? {NO} {SAMKHITTAM}",
        closer("Lakkhaṇayuttikathā"))

    # ---- Vacanasodhanaṃ ----------------------------------------------------------------------------------------------
    head("5-1-13-0", 4, H["Vacanasodhanaṃ"])
    KEHICI = "trong một số trường hợp"

    def sodhana(pos, neg, thing):
        """pos: predicate ('được tìm thấy'); neg: its negation; thing: 'cái được tìm thấy'."""
        return (f"Có phải người {pos}, và {thing} là người không? Người {pos}, còn {thing} thì {KEHICI} là người, "
                f"{KEHICI} không phải là người. Có phải người {KEHICI} {pos}, {KEHICI} {neg} không? {NO_PE}")

    add("5-55", sodhana("được tìm thấy", "không được tìm thấy", "cái được tìm thấy"))
    add("5-56", sodhana("là thực tại chân thật", "không phải là thực tại chân thật", "thực tại chân thật"))
    add("5-57", sodhana("hiện hữu", "không hiện hữu", "cái hiện hữu"))
    add("5-58", sodhana("thực sự hiện hữu", "không thực sự hiện hữu", "cái thực sự hiện hữu"))
    add("5-59", sodhana("tồn tại", "không tồn tại", "cái tồn tại"))
    add("5-60", f"Có phải người tồn tại, và không phải tất cả cái tồn tại đều là người không? Đúng vậy{PE} "
        f"có phải người không tồn tại, và không phải tất cả cái không tồn tại đều là người không? {NO} {SAMKHITTAM}",
        closer("Vacanasodhanaṃ"))

    # ---- Paññattānuyogo ------------------------------------------------------------------------------------------------
    head("5-1-14-0", 4, H["Paññattānuyogo"])
    RUPADH, KAMADH, ARUPADH = "cõi hình sắc", "cõi dục lạc", "cõi không hình sắc"
    add("5-61", f"{Q(f'trong {RUPADH}, người có hình sắc')} {YES} {Q(f'trong {KAMADH}, người có dục lạc')} {NO_PE}")
    add("5-62", f"{Q(f'trong {RUPADH}, chúng sinh có hình sắc')} {YES} "
        f"{Q(f'trong {KAMADH}, chúng sinh có dục lạc')} {NO_PE}")
    add("5-63", f"{Q(f'trong {ARUPADH}, người không có hình sắc')} {YES} "
        f"{Q(f'trong {KAMADH}, người có dục lạc')} {NO_PE}")
    add("5-64", f"{Q(f'trong {ARUPADH}, chúng sinh không có hình sắc')} {YES} "
        f"{Q(f'trong {KAMADH}, chúng sinh có dục lạc')} {NO_PE}")
    koci = f"có ai đó chết ở {RUPADH} rồi tái sinh vào {ARUPADH}"   # atthi ca koci rūpadhātuyā cuto arūpadhātuṃ upapajjati
    add("5-65", f"{Q(f'trong {RUPADH}, người có hình sắc, trong {ARUPADH}, người không có hình sắc, và {koci}')} "
        f"{YES} {Q('người có hình sắc đã bị cắt đứt, người không có hình sắc đã sinh ra')} {NO_PE}")
    add("5-66", f"{Q(f'trong {RUPADH}, chúng sinh có hình sắc, trong {ARUPADH}, chúng sinh không có hình sắc, và {koci}')} "
        f"{YES} {Q('chúng sinh có hình sắc đã bị cắt đứt, chúng sinh không có hình sắc đã sinh ra')} {NO_PE}")
    P = f"{KAYA_K}, {JIVA_K}, {anna('thân', PERSON)}"
    l1 = (f"{Q(KAYA_K)} {YES} {Q(JIVA_K)} {YES} {Q(anna('thân', PERSON))} {YES} {Q(ANNAM_JIVAM)} {NO}")
    add("5-67", *pentad(P, ANNAM_JIVAM, pe=True, line1=l1, sep=";"))
    P = f"{KAYA_K}, {SUTTA_ATTHI}"
    l1 = f"{Q(KAYA_K)} {YES} {Q(rq(SUTTA_ATTHI, 0))} {YES} {Q(anna('thân', PERSON))} {NO}"
    l = pentad(P, anna("thân", PERSON), kind="patikamma", line1=l1)
    l[2] = l[2] + f" {SAMKHITTAM}"
    add("5-68", *l, closer("Paññattānuyogo"))

    # ---- Gatianuyogo -----------------------------------------------------------------------------------------------------
    head("5-1-15-0", 4, H["Gatianuyogo"])
    QSAND = Q(SANDHAVATI)
    add("5-69", f"{QSAND} {YES} {Q(f'người ấy trôi lăn {LOKA}')} {NO_PE}")
    add("5-70", f"{QSAND} {YES} {Q(f'người khác trôi lăn {LOKA}')} {NO_PE}")
    add("5-71", f"{QSAND} {YES} {Q(f'cả người ấy và người khác trôi lăn {LOKA}')} {NO_PE}")
    add("5-72", f"{QSAND} {YES} {Q(f'người ấy không trôi lăn, người khác cũng không trôi lăn {LOKA}')} {NO_PE}")
    add("5-73", f"{QSAND} {YES} {Q(f'người ấy trôi lăn, người khác trôi lăn, cả người ấy và người khác trôi lăn, người ấy không trôi lăn và người khác cũng không trôi lăn {LOKA}')} {NO_PE}")
    add("5-74", f"{na_vattabbam(SANDHAVATI)} {YES} {NANU_VUTTAM}",
        "“Người ấy, sau khi trôi lăn tối đa bảy lần;",
        f"Trở thành người đi đến tận cùng của khổ đau, nhờ diệt tận mọi xiềng xích” "
        f"[{CIT['saṃ. ni.']} 2.133; {CIT['itivu.']} 24, cũng có trong {CIT['itivu.']}].",
        f"{ATTHEVA} {YES} {tena_hi(SANDHAVATI)}")
    add("5-75", f"{na_vattabbam(SANDHAVATI)} {YES} {NANU_VUTTAM} “Này các tỳ-khưu, vòng luân hồi này không có "
        f"khởi điểm có thể biết được{var_sp('Ka.', 'anamataggāyaṃ')}. Điểm khởi đầu không được nhận ra đối với "
        f"những chúng sinh bị vô minh làm chướng ngại, bị khao khát trói buộc như xiềng xích, đang trôi lăn, "
        f"đang luân chuyển” [{CIT['saṃ. ni.']} 2.124]! {ATTHEVA} {YES} {tena_hi(SANDHAVATI)}")
    add("5-76", f"{QSAND} {YES} {Q(SVEVA)} {NO_PE}")
    QSV = Q(SVEVA)

    def becomes(x, ys):             # atthi koci X hutvā Y hoti, Z hoti …
        return f"có ai đó là {x} rồi " + ", ".join(f"trở thành {y}" for y in ys)

    def same(x, y):                 # sveva X so Y
        return f"chính {x} ấy là {y} ấy"

    add("5-77", f"{QSV} {YES} {Q(becomes(KN['manusso'], [KN['devo']]))} {YES} {Q(same(KN['manusso'], KN['devo']))} "
        f"{NO_PE}")

    def micchavada(y):              # manusso hutvā Y hoti … svevāyaṃ sandhāvatīti micchā
        return (f"{Q(same(KN['manusso'], y))} {YES} Là con người rồi trở thành {y}, là {y} rồi trở thành con người, "
                f"người đã từng là con người là khác, {y} là khác, nói rằng chính người đã từng là con người này "
                f"trôi lăn là sai{PE}")

    SACE = ("Vì nếu chính người ấy trôi lăn, chết ở đây rồi sang thế gian khác mà không khác đi, thì như vậy sẽ "
            "không có sự chết, và việc sát hại sinh mạng cũng không được tìm thấy. Nghiệp tồn tại, quả của nghiệp "
            "tồn tại, quả của các nghiệp đã làm tồn tại; khi thiện và bất thiện đang trổ quả, nói rằng chính người "
            "này trôi lăn là sai.")
    add("5-78", micchavada(KN["devo"]), SACE)
    beings = ["dạ-xoa", "ngạ quỷ", "chúng sinh địa ngục", "loài súc sinh", "lạc đà", "bò", "lừa", "heo",
              "trâu" + var_sp("Sī., Syā., Kaṃ., Pī.", "mahiso")]
    add("5-79", f"{QSV} {YES} {Q(becomes(KN['manusso'], beings))} {YES} {Q(same(KN['manusso'], 'con trâu'))} {NO_PE}")
    add("5-80", micchavada("con trâu"), SACE)
    K, B, V, Su = KN["khattiyo"], "vị bà-la-môn", KN["vesso"], KN["suddo"]
    add("5-81", f"{QSV} {YES} {Q(becomes(K, ['bà-la-môn']))} {YES} {Q(same(K, B))} {NO_PE}")
    add("5-82", f"{Q(becomes(K, [V, Su]))} {YES} {Q(same(K, Su))} {NO_PE}")
    add("5-83", f"{Q(becomes('bà-la-môn', [V, Su, K]))} {YES} {Q(same(B, K))} {NO_PE}")
    add("5-84", f"{Q(becomes(V, [Su, K, 'bà-la-môn']))} {YES} {Q(same(V, B))} {NO_PE}")
    add("5-85", f"{Q(becomes(Su, [K, 'bà-la-môn', V]))} {YES} {Q(same(Su, V))} {NO_PE}")
    MAIMED = (f"người bị chặt tay vẫn là người bị chặt tay, người bị chặt chân vẫn là người bị chặt chân, "
              f"người bị chặt tay chân vẫn là người bị chặt tay chân, người bị chặt tai{PE} người bị chặt mũi{PE} "
              f"người bị chặt tai và mũi{PE} người bị chặt ngón tay{PE} người bị chặt ngón cái{PE} "
              f"người bị chặt gân{PE} người có bàn tay co quắp{PE} người có bàn tay dính ngón{PE} "
              f"người bị bệnh phong{PE} người bị mụn nhọt{PE} người bị bệnh bạch biến{PE} người bị bệnh lao{PE} "
              f"người bị động kinh{PE} lạc đà{PE} bò{PE} lừa{PE} heo{PE} trâu vẫn là trâu")
    add("5-86", f"{QSV} {YES} {Q(MAIMED)} {NO_PE}")
    SOTA = (f"{PN['sotāpanno']}, sau khi chết ở thế giới loài người và tái sinh vào thế giới chư thiên, ở đó cũng "
            f"vẫn là {PN['sotāpanno']}")
    add("5-87", f"{na_vattabbam(SVEVA)} {YES} {NANU(SOTA)} {YES}", hanci(SOTA, SVEVA))
    SOTA_M = (f"{PN['sotāpanno']}, sau khi chết ở thế giới loài người và tái sinh vào thế giới chư thiên, ở đó cũng "
              f"là con người")
    add("5-88", f"{katva(SOTA, SVEVA)} {YES} Có phải vì cho rằng {SOTA_M} không? {NO_PE}")
    ANANNO = "trôi lăn mà không khác đi, không mất đi"          # anañño avigato sandhāvati
    add("5-89", f"{QSV} {YES} {Q(ANANNO)} {NO_PE}")
    add("5-90", f"{Q(ANANNO)} {YES} {Q(MAIMED)} {NO_PE}")

    def with_(xs, neg=False):       # sarūpo … sandhāvati / arūpo … sandhāvati
        p = "mà không có" if neg else "cùng với"
        return "trôi lăn " + f"{PE} ".join(f"{p if k == 0 else p.replace('mà ', '')} {x}" for k, x in enumerate(xs))

    SK = "sự tạo tác"                                            # sasaṅkhāro / asaṅkhāro
    for i, neg, tail in (("5-91", False, TAM_JIVAM), ("5-92", True, ANNAM_JIVAM)):
        r1, rr = with_([RUPA], neg), with_([VEDANA, SANNA, SK, VINNANA], neg)
        last = with_([VINNANA], neg)
        add(i, f"{QSV} {YES} {Q(r1)} {NO_PE} {q(r1)} {YES} {Q(tail)} {NO_PE}",
            f"{Q(rr)} {NO_PE} {q(last)} {YES} {Q(tail)} {NO_PE}")
    for i, neg, tail in (("5-93", False, TAM_JIVAM), ("5-94", True, ANNAM_JIVAM)):
        v = "không trôi lăn" if neg else "trôi lăn"
        l2end = f"{NO} {SAMKHITTAM}." if neg else NO_PE
        lines = [f"{QSV} {YES} {Q(f'{RUPA} {v}')} {NO_PE} {q(f'{RUPA} {v}')} {YES} {Q(tail)} {NO_PE}",
                 f"Có phải {VEDANA}{PE} {SANNA}{PE} {SANKHARA}{PE} {VINNANA} {v} không? {NO_PE} "
                 f"{q(f'{VINNANA} {v}')} {YES} {Q(tail)} {l2end}"]
        if neg:
            lines += ["Khi các khối đang tan rã, nếu người ấy tan rã;",
                      "Thì thành quan điểm về sự đoạn diệt, điều Đức Phật đã loại bỏ.",
                      "Khi các khối đang tan rã, nếu người ấy không tan rã;",
                      "Thì người trở thành trường tồn, hoàn toàn ngang bằng với Niết-bàn.",
                      closer("Gatianuyogo")]
        add(i, *lines)

    # ---- Upādāpaññattānuyogo ------------------------------------------------------------------------------------------
    head("5-1-16-0", 4, H["Upādāpaññattānuyogo"])

    def dua(x, y="người"):          # X upādāya Y-assa paññatti
        return f"dựa vào {x} mà có sự định danh {y}"

    def chain_dua(xs, y="người"):   # X upādāya… Y upādāya… Z upādāya W-assa paññatti
        return f"{PE} ".join(f"dựa vào {x}" for x in xs[:-1]) + f"{PE} {dua(xs[-1], y)}"

    add("5-95", f"{Q(dua(RUPA))} {YES} {Q(f'{RUPA} là {ANICCA}')} {YES_Q} {Q(f'người cũng là {ANICCA}')} {NO_PE}")
    add("5-96", f"Có phải {chain_dua([VEDANA, SANNA, SANKHARA, VINNANA])} không? {YES} "
        f"{Q(f'{VINNANA} là {ANICCA}')} {YES} {Q(f'người cũng là {ANICCA}')} {NO_PE}")
    cols = ["màu vàng", "màu đỏ", "màu trắng", "thấy được", "không thấy được", "có tính va chạm"]
    add("5-97", f"{Q(dua(RUPA))} {YES} {Q(dua(RUPA + ' màu xanh', 'người màu xanh'))} {NO_PE} có phải "
        + f"{PE} ".join(f"dựa vào {RUPA} {c}" for c in cols)
        + f"{PE} {dua(RUPA + ' không có tính va chạm', 'người không có tính va chạm')} không? {NO_PE}")

    def ethical(kind_vi, obj, pred_obj, pred_p, pl="cảm giác"):
        x = f"{obj} {kind_vi}"
        return (f"{Q(dua(obj))} {YES} {Q(dua(x, 'người ' + kind_vi))} {NO_PE} {q(dua(x, 'người ' + kind_vi))} "
                f"{YES} {Q(f'{x} {pred_obj}')} {YES} {Q(f'người {kind_vi} cũng {pred_p}')} {NO_PE}")

    add("5-98", ethical("thiện", VEDANA, SAPHALA_K, SAPHALA_K))
    add("5-99", ethical("bất thiện", VEDANA, SAPHALA_A, SAPHALA_A))
    ABY = "không xác định về mặt đạo đức"
    add("5-100", ethical(ABY, VEDANA, f"là {ANICCA}", f"là {ANICCA}"))
    l = ethical("thiện", VINNANA, SAPHALA_K, SAPHALA_K)
    add("5-101", l.replace(f"{Q(dua(VINNANA))}", f"Có phải {chain_dua([SANNA, SANKHARA, VINNANA])} không?", 1))
    add("5-102", ethical("bất thiện", VINNANA, SAPHALA_A, SAPHALA_A))
    add("5-103", ethical(ABY, VINNANA, f"là {ANICCA}", f"là {ANICCA}"))

    def goi(base, name):            # X upādāya "Y"ti vattabbo
        return f"dựa vào {base} mà {vattabbo(name)}"

    def niruddha(base, name):       # Xmhi niruddhe "Y niruddho"ti vattabbo
        return f"khi {base} đã chấm dứt thì {vattabbo(name + ' đã chấm dứt')}"

    add("5-104", f"{Q(goi('mắt', 'người có mắt'))} {YES} {Q(niruddha('mắt', 'người có mắt'))} {NO_PE} có phải "
        + f"{PE} ".join(f"dựa vào {x}" for x in ("tai", "mũi", "lưỡi", "thân"))
        + f"{PE} {goi('ý', 'người có ý')} không? {YES} {Q(niruddha('ý', 'người có ý'))} {NO}")

    def path(lst, pe_first):
        a, z = lst[0], lst[-1]
        sep1 = NO_PE + " có phải " if pe_first else NO + " Có phải "
        return (f"{Q(goi(a, 'người có ' + a))} {YES} {Q(niruddha(a, 'người có ' + a))} {sep1}"
                + f"{PE} ".join(f"dựa vào {x}" for x in lst[1:-1])
                + f"{PE} {goi(z, 'người có ' + z)} không? {YES} {Q(niruddha(z, 'người có ' + z))} "
                + (NO_PE if pe_first else NO))

    add("5-105", path(MICCHA, False))
    add("5-106", path(SAMMA, True))

    def count(two, all_, k2, kn, n_all):
        return (f"{Q(dua(two))} {YES} {Q(dua(f'hai {k2}', 'hai người'))} {NO_PE} {q(dua(all_))} {YES} "
                f"{Q(dua(f'{n_all} {kn}', n_all + ' người'))} {NO_PE}")

    add("5-107", count(f"{RUPA}, dựa vào {VEDANA}",
                       f"{RUPA}, dựa vào {VEDANA}, dựa vào {SANNA}, dựa vào {SANKHARA}, dựa vào {VINNANA}",
                       "khối", "khối", "năm"))
    add("5-108", count(f"{A['cakkhāyatana']}, dựa vào {A['sotāyatana']}",
                       f"{A['cakkhāyatana']}, dựa vào {A['sotāyatana']}{PE} dựa vào {A['dhammāyatana']}",
                       "lĩnh vực nhận biết", "lĩnh vực nhận biết", "mười hai"))
    add("5-109", count(f"{D['cakkhudhātu']}, dựa vào {D['sotadhātu']}",
                       f"{D['cakkhudhātu']}, dựa vào {D['sotadhātu']}{PE} dựa vào {D['dhammadhātu']}",
                       "yếu tố", "yếu tố", "mười tám"))
    l = count(f"{I['cakkhundriya']}, dựa vào {I['sotindriya']}",
              f"{I['cakkhundriya']}, dựa vào {I['sotindriya']}{PE} dựa vào {ANNATAVI}",
              "năng lực", "năng lực", "hai mươi hai")
    add("5-110", l.replace("dựa vào hai mươi hai năng lực", "dựa vào hai mươi hai"
                           + var("?", "bāvīsatiyā") + " năng lực"))
    VOK = {1: "sự hiện hữu gồm một khối", 4: "sự hiện hữu gồm bốn khối", 5: "sự hiện hữu gồm năm khối"}
    add("5-111", f"{Q(dua(VOK[1], 'một người'))} {YES} {Q(dua(VOK[4], 'bốn người'))} {NO_PE} "
        f"{q(dua(VOK[1], 'một người'))} {YES} {Q(dua(VOK[5], 'năm người'))} {NO_PE} "
        f"{q(f'trong {VOK[1]} chỉ có một người')} {YES} "
        f"{Q(f'trong {VOK[4]} chỉ có bốn' + var('?', 'cattāro') + ' người')} {NO_PE} "
        f"{q(f'trong {VOK[1]} chỉ có một người')} {YES} {Q(f'trong {VOK[5]} chỉ có năm người')} {NO_PE}")
    YATHA = "cũng như"                                           # yathā
    EVAM = "cũng y như vậy"                                      # evamevaṃ
    R_P = dua(RUPA)

    def simile(base, extra=""):
        return f"{YATHA} {base}{extra}, {EVAM}, {R_P}"

    tree = dua("cái cây", "bóng râm")
    add("5-112", f"{Q(simile(tree))} ( ) [(Đúng vậy) (?), cũng vậy trong cả ba lượt kế tiếp] "
        f"{Q(simile(tree, ', cây cũng vô thường, bóng râm cũng vô thường') + ', vật chất cũng vô thường, người cũng vô thường')} "
        f"{NO_PE} {q(simile(tree, ', ' + anna('cây', 'bóng râm')) + ', ' + anna(RUPA, PERSON))} {NO_PE}")
    for i, base, a1, a2 in (("5-113", dua("làng", "dân làng"), "làng", "dân làng"),
                            ("5-114", dua("đất nước", "vua"), "đất nước", "vua")):
        add(i, f"{Q(simile(base))} {Q(simile(base, ', ' + anna(a1, a2)) + ', ' + anna(RUPA, PERSON))} {NO_PE}")
    NIG = "cái cùm không phải là người bị cùm, ai có cái cùm thì người ấy là người bị cùm"
    RV = "vật chất không phải là người có vật chất, ai có vật chất thì người ấy là người có vật chất"
    add("5-115", f"{Q(f'{YATHA} {NIG}, {EVAM}, {RV}')} "
        f"{Q(f'{YATHA} {NIG}, ' + anna('cái cùm', 'người bị cùm') + f', {EVAM}, {RV}, ' + anna(RUPA, 'người có vật chất'))} "
        f"{NO_PE}")
    C2 = "khi tâm thứ hai đã sinh khởi"                          # dutiye citte uppanne
    SO = "người ấy hay người khác"                               # soti vā aññoti vā
    KU = "bé trai hay bé gái"                                    # kumārakoti vā kumārikāti vā
    DM = "vị trời hay con người"                                 # devoti vā manussoti vā

    def citta2(opp, opp_full, nopen, pe):
        """opp: the pair asked about (KU / DM); nopen: line 1 with or without the dash form."""
        a = f"{C2}, không nên nói – “{SO}”"
        b = f"{C2}, nên nói – “{opp}”"
        claim = f"‘{C2} không nên nói – {SO}, {C2} nên nói – {opp}’"
        l2 = (f"{ADMIT['niggaha']} Nếu {a}, thì {RE}, chắc chắn nên nói – “{C2} không nên nói – ‘{opp}’”. "
              f"Điều bạn nói ở đây là sai – “nên nói – {claim}”.")
        l3 = (f"Hoặc nếu {b}, thì {RE}, chắc chắn nên nói – “{C2} nên nói – ‘{SO}’”. "
              f"Điều bạn nói ở đây là sai – “nên nói – {claim}”" + (PE if pe else "."))
        return [nopen, l2, l3]

    l1 = (f"{Q('ở mỗi tâm đều có sự định danh người')} {YES} "
          f"{Q('ở mỗi tâm, người sinh ra, già đi, qua đời, chết đi, tái sinh')} {NO_PE} "
          f"{q(f'{C2} thì không nên nói là {SO}')} {YES} {Q(f'{C2} thì không nên nói là {KU}')} {SHOULD}")
    add("5-116", *citta2(KU, KU, l1, False))
    l1 = (f"Có phải {C2} không nên nói – “{SO}” không? {YES} Có phải {C2} không nên nói – "
          f"“phụ nữ hay đàn ông hay người tại gia hay người xuất gia hay vị trời hay con người” không? {SHOULD}")
    add("5-117", *citta2(DM, DM, l1, True))
    SEE = ("ai thấy, thấy cái gì, nhờ cái gì mà thấy, thì người ấy thấy, thấy cái đó, nhờ cái đó mà thấy")
    SEE_H = "ai thấy, thấy cái gì, nhờ cái gì mà thấy, người ấy thấy, thấy cái đó, nhờ cái đó mà thấy"
    NV = na_vattabbam(P_UP)
    add("5-118", f"{NV} {YES} {NANU(SEE)} {YES} {hanci(SEE_H, P_UP, ';')}")
    KNOW = (f"ai nghe{PE} ai ngửi{PE} ai nếm{PE} ai chạm{PE} ai nhận biết, nhận biết cái gì, nhờ cái gì mà nhận "
            f"biết, thì người ấy nhận biết, nhận biết cái đó, nhờ cái đó mà nhận biết")
    KNOW_H = ("ai nhận biết, nhận biết cái gì, nhờ cái gì mà nhận biết, người ấy nhận biết, nhận biết cái đó, "
              "nhờ cái đó mà nhận biết")
    add("5-119", f"{NV} {YES} {NANU(KNOW)} {YES} {hanci(KNOW_H, P_UP, ';')}")
    NSEE = ("ai không thấy, không thấy cái gì, nhờ cái gì mà không thấy, thì người ấy không thấy, không thấy cái đó, "
            "nhờ cái đó mà không thấy")
    NSEE_H = NSEE.replace(", thì người ấy", ", người ấy")
    NKNOW = (f"ai không nghe{PE} ai không ngửi{PE} ai không nếm{PE} ai không chạm{PE} ai không nhận biết, không "
             f"nhận biết cái gì, nhờ cái gì mà không nhận biết, thì người ấy không nhận biết, không nhận biết cái đó, "
             f"nhờ cái đó mà không nhận biết")
    NKNOW_H = ("ai không nhận biết, không nhận biết cái gì, nhờ cái gì mà không nhận biết, người ấy không nhận biết, "
               "không nhận biết cái đó, nhờ cái đó mà không nhận biết")
    add("5-120", f"{Q(P_UP)} {YES} {NANU(NSEE)} {YES} {hanci_neg(NSEE_H, P_UP, ';')}",
        f"{Q(P_UP)} {YES} {NANU(NKNOW)} {YES} {hanci_neg(NKNOW_H, P_UP, ';')}")
    DIBBA_S = ("Này các tỳ-khưu, với thiên nhãn thanh tịnh, vượt quá mắt người, Ta thấy chúng sinh đang chết đi, "
               "đang tái sinh, thấp kém, ưu việt, đẹp đẽ, xấu xí, ở cõi tốt lành, ở cõi xấu; Ta hiểu rõ chúng sinh "
               "đi theo nghiệp của mình")
    add("5-121", f"{NV} {YES} {NANU_VUTTAM} “{DIBBA_S}” [{CIT['ma. ni.']} 1.213, hơi khác một chút]! "
        f"{ATTHEVA} {YES} {tena_hi(P_UP)}")
    DE = "Đức Thế Tôn, với thiên nhãn thanh tịnh, vượt quá mắt người, thấy hình sắc hay thấy người?"
    add("5-122",
        f"Có phải vì cho rằng {VUTTAM} “{DIBBA_S}”, chính vì lý do ấy, {P_UP} không? "
        f"{YES} {DE} Thấy hình sắc. Có phải hình sắc là người, hình sắc chết đi, hình sắc tái sinh, hình sắc đi theo "
        f"nghiệp của mình không? {NO}",
        f"{DE} Thấy người. Có phải người là hình sắc, là lĩnh vực hình sắc, là yếu tố hình sắc, là màu xanh, màu vàng, "
        f"màu đỏ, màu trắng, được nhận biết bằng mắt, va chạm vào mắt, đi vào tầm của mắt không? {NO}",
        f"{DE} Thấy cả hai. Có phải cả hai là hình sắc, là lĩnh vực hình sắc, là yếu tố hình sắc, cả hai là màu xanh, "
        f"cả hai là màu vàng, cả hai là màu đỏ, cả hai là màu trắng, cả hai được nhận biết bằng mắt, cả hai va chạm "
        f"vào mắt, cả hai đi vào tầm của mắt, cả hai chết đi, cả hai tái sinh, cả hai đi theo nghiệp của mình không? "
        f"{NO}",
        closer("Upādāpaññattānuyogo"))

    # ---- Purisakārānuyogo ---------------------------------------------------------------------------------------------
    head("5-1-17-0", 4, H["Purisakārānuyogo"])
    KUP = up(KALYANA_KAMMA, sp=False)                               # kalyāṇapāpakāni kammāni upalabbhanti
    KKUP = up(f"{KK} {KALYANA_KAMMA}", sp=False)                    # … kattā kāretā upalabbhati
    NEU_KK = neu(KUP, KKUP)
    TASSA = Q(TASSA_TASSEVA)

    nat_up = [(p, up(v, sp=False)) for p, v in NATURE]

    # kamma: kattā kāretā
    add("5-123", f"{Q(KUP)} {YES} {Q(KKUP)} {NO_PE}")
    add("5-124", f"{NEU_KK} {YES} {Q(up(KK + ' ra người ấy', sp=False))} {NO_PE}")
    add("5-125", f"{Q(up(KK + ' ra người ấy', sp=False))} {YES} {TASSA} {NO_PE}")
    add("5-126", f"{NEU_KK} {YES} {neu(up(PERSON, sp=False), up(KK + ' ra người', sp=False))} {NO_PE}")
    add("5-127", f"{NEU_KK} {YES} {neu(up('Niết-bàn', sp=False), up(KK + ' ra Niết-bàn', sp=False))} {NO_PE}")
    sid = 128
    for _, v in NATURE:
        add(f"5-{sid}", f"{NEU_KK} {YES} {neu(up(v, sp=False), up(f'{KK} ra {v}', sp=False))} {NO_PE}")
        sid += 1
    add("5-134", f"{NEU_KK} {YES} {neu(up(TINA, sp=False), up(f'{KK} ra {TINA}', sp=False))} {NO_PE}")
    add("5-135", f"{NEU_KK} {YES} {Q(anna(KALYANA_KAMMA, f'{KK} {KALYANA_KAMMA}'))} {NO_PE}")

    # vipāka / sukha / dukkha: paṭisaṃvedī
    def ps_block(start, thing, ps_thing, nat_pe, anna_sep=", ", first_no_pe=True):
        """thing: 'quả của các nghiệp tốt đẹp và xấu ác' etc.; ps_thing: 'người cảm nhận …'."""
        T, PS = up(thing, sp=False), up(ps_thing, sp=False)
        NE = neu(T, PS)
        tassa = up("người cảm nhận người ấy", sp=False)
        s = start
        rows = []
        rows.append([f"{Q(T)} {YES} {Q(PS)} {NO_PE if first_no_pe else NO}"])
        rows.append([f"{NE} {YES} {Q(tassa)} {NO_PE}"])
        rows.append([f"{Q(tassa)} {YES} {TASSA} {NO_PE}"])
        rows.append([f"{NE} {YES} {neu(up(PERSON, sp=False), up('người cảm nhận người', sp=False))} {NO_PE}"])
        rows.append([f"{NE} {YES} {neu(up('Niết-bàn', sp=False), up('người cảm nhận Niết-bàn', sp=False))} {NO_PE}"])
        ch = nat_pe(nat_up)
        rows.append([f"{NE} {YES} Có phải nếu {ch} {up(TINA, sp=False)}, thì "
                     f"{up('người cảm nhận ' + TINA, sp=False)} không? {NO_PE}"])
        rows.append([f"{NE} {YES} {Q(anna(thing, ps_thing))} {NO_PE}"])
        return rows

    def chain_a(items):             # Mahāpathavī upalabbhatīti…pe… mahāsamuddo… sinerupabbatarājā… āpo… tejo… vāyo…pe…
        return f"{PE} ".join(v for _, v in items) + PE

    VIP = f"quả của {KALYANA_KAMMA}"
    rows = ps_block(136, VIP, f"người cảm nhận {VIP}", chain_a)
    for k, r in enumerate(rows):
        add(f"5-{136 + k}", *r)
    for start, thing in ((143, "hạnh phúc cõi trời"), (150, "hạnh phúc cõi người"),
                         (157, "khổ đau ở cõi khổ"), (164, "khổ đau ở địa ngục")):
        rows = ps_block(start, thing, f"người cảm nhận {thing}", chain_a, first_no_pe=(start != 164))
        if start == 164:            # ^5-164 holds two lines (the first without …pe…)
            rows = [rows[0] + rows[1]] + rows[2:]
            add(f"5-{start}", *rows[0])
            for k, r in enumerate(rows[1:], 1):
                add(f"5-{start + k}", *r)
        else:
            for k, r in enumerate(rows):
                add(f"5-{start + k}", *r)
    KKV = up(f"{KK} {KALYANA_KAMMA}, người cảm nhận quả", sp=False)  # kattā kāretā vipākapaṭisaṃvedī upalabbhati
    NEU_KKV = neu(KUP, KKV)
    SO_K, SO_P = "người ấy làm", "người ấy cảm nhận"
    SD = "sự dễ chịu và sự khó chịu"                                 # sukhadukkhaṃ
    SAY, PAR = "do tự mình làm ra", "do người khác làm ra"           # sayaṅkataṃ / paraṅkataṃ
    ADH = "không do tự mình làm ra, không do người khác làm ra, mà sinh khởi một cách tình cờ"
    #   asayaṅkāraṃ aparaṅkāraṃ adhiccasamuppannaṃ
    W1 = f"{SO_K}, {SO_P}"                                           # so karoti so paṭisaṃvedeti
    W2 = "một người làm, một người khác cảm nhận"                    # añño karoti añño paṭisaṃvedeti
    W3 = "người ấy và người khác cùng làm, người ấy và người khác cùng cảm nhận"
    W4 = "người ấy không làm và người ấy không cảm nhận, người khác không làm và người khác không cảm nhận"
    add("5-170", f"{NEU_KKV} {YES} {Q(W1)} {NO_PE}")
    add("5-171", f"{Q(W1)} {YES} {Q(f'{SD} là {SAY}')} {NO_PE}")
    add("5-172", f"{NEU_KKV} {YES} {Q(W2)} {NO_PE}")
    add("5-173", f"{Q(W2)} {YES} {Q(f'{SD} là {PAR}')} {NO_PE}")
    add("5-174", f"{NEU_KKV} {YES} {Q(W3)} {NO_PE}")
    add("5-175", f"{Q(W3)} {YES} {Q(f'{SD} là {SAY} và {PAR}')} {NO_PE}")
    add("5-176", f"{NEU_KKV} {YES} {Q(W4)} {NO_PE}")
    add("5-177", f"{Q(W4)} {YES} {Q(f'{SD} {ADH}')} {NO_PE}")
    WALL = f"{W1}, {W2}, {W3}, {W4}"
    add("5-178", f"{NEU_KKV} {YES} {Q(WALL)} {NO_PE}")
    add("5-179", f"{Q(WALL)} {YES} {Q(f'{SD} là {SAY}, {SD} là {PAR}, {SD} là {SAY} và {PAR}, {SD} {ADH}')} {NO_PE}")

    def ex(x):                      # X atthi
        return f"{x} tồn tại"

    NEU_K = neu(ex("nghiệp"), ex("người tạo nghiệp"))
    add("5-180", f"{Q(ex('nghiệp'))} {YES} {Q(ex('người tạo nghiệp'))} {NO_PE}")
    add("5-181", f"{NEU_K} {YES} {Q(ex('người tạo ra người ấy'))} {NO_PE}")
    add("5-182", f"{Q(ex('người tạo ra người ấy'))} {YES} {TASSA} {NO_PE}")
    add("5-183", f"{NEU_K} {YES} {neu(ex(PERSON), ex('người tạo ra người'))} {NO_PE}")
    add("5-184", f"{NEU_K} {YES} {neu(ex('Niết-bàn'), ex('người tạo ra Niết-bàn'))} {NO_PE}")
    nat_ex = f"{PE} ".join(ex(v) for _, v in NATURE) + PE
    add("5-185", f"{NEU_K} {YES} Có phải nếu {nat_ex} {ex(TINA)}, thì {ex('người tạo ra ' + TINA)} không? {NO_PE}")
    add("5-186", f"{NEU_K} {YES} {Q(anna('nghiệp', 'người tạo nghiệp'))} {NO_PE}")
    NEU_V = neu(ex("quả"), ex("người cảm nhận quả"))
    add("5-187", f"{Q(ex('quả'))} {YES} {Q(ex('người cảm nhận quả'))} {NO_PE}")
    add("5-188", f"{NEU_V} {YES} {Q(ex('người cảm nhận người ấy'))} {NO_PE}")
    add("5-189", f"{Q(ex('người cảm nhận người ấy'))} {YES} {TASSA} {NO_PE} {neu(ex('quả'), ex('người cảm nhận quả'))[0].lower()}"
        f"{neu(ex('quả'), ex('người cảm nhận quả'))[1:]} {YES} {neu(ex(PERSON), ex('người cảm nhận người'))} {NO_PE}")
    add("5-190", f"{NEU_V} {YES} {neu(ex('Niết-bàn'), ex('người cảm nhận Niết-bàn'))} {NO_PE}")
    add("5-191", f"{NEU_V} {YES} Có phải nếu {nat_ex} {ex(TINA)}, thì {ex('người cảm nhận ' + TINA)} không? {NO_PE}")
    add("5-192", f"{NEU_V} {YES} {Q(anna('quả', 'người cảm nhận quả'))} {NO} {SAMKHITTAM}",
        closer("Purisakārānuyogo"), KALYANAVAGGO)

    # ---- Abhiññānuyogo ------------------------------------------------------------------------------------------------
    head("5-1-18-0", 4, H["Abhiññānuyogo"])
    IDDHI = "có ai đó thi triển thần thông"
    add("5-193", f"{NV} {YES} {NANU(IDDHI)} {YES} {hanci(IDDHI, P_UP)}")
    ABH = [("dibbasota", "nghe âm thanh bằng yếu tố tai thuộc cõi trời"),
           ("paracitta", "nhận biết tâm của người khác"),
           ("pubbenivāsa", "nhớ lại các đời sống trước đây"),
           ("dibbacakkhu", "thấy hình sắc bằng thiên nhãn"),
           ("āsavakkhaya", "tự mình chứng nghiệm sự diệt tận các ô nhiễm")]
    last = ABH[-1][1]
    add("5-194", f"{NV} {YES} Chẳng phải có ai đó " + f"{PE} ".join(v for _, v in ABH) + f" sao? {YES} "
        f"{hanci('có ai đó ' + last, P_UP)}")
    add("5-195", f"{katva(IDDHI, P_UP)} {YES} Ai thi triển thần thông, có phải chính người ấy là người không? "
        f"Ai không thi triển thần thông, người ấy không phải là người sao? {NO_PE}")
    add("5-196", "Ai " + f"{PE} ai ".join(v for _, v in ABH) + ", có phải chính người ấy là người không? "
        f"Ai không {last}, người ấy không phải là người sao? {NO_PE}", closer("Abhiññānuyogo"))

    # ---- Ñātakānuyogādi ------------------------------------------------------------------------------------------------
    head("5-1-19-0", 4, "15-18. " + H["Ñātakānuyogādi"])
    add("5-197", f"{NV} {YES} {NANU(ex('mẹ'))} {YES} {hanci(ex('mẹ'), P_UP)}")
    kin = [v for _, v in KIN[1:]]
    add("5-198", f"{NV} {YES} Chẳng phải " + f"{PE} ".join(ex(v) for v in kin) + f" sao? {YES} "
        f"{hanci(ex('con người'), P_UP)}")
    KATVA_M = katva(ex("mẹ"), P_UP)
    NP = "có ai đó không phải là người rồi trở thành người"
    PN_ = "có ai đó là người rồi trở thành không phải người"
    add("5-199", f"{KATVA_M} {YES} {Q('có ai đó không phải là mẹ rồi trở thành mẹ')} {YES} {Q(NP)} {NO_PE} "
        f"có phải có ai đó không phải là cha rồi{PE} "
        + f"{PE} ".join(f"không phải là {v} rồi" for v in kin[1:-1])
        + f"{PE} không phải là con người rồi trở thành con người không? {YES} {Q(NP)} {NO_PE}")
    add("5-200", f"{KATVA_M} {YES} {Q('có ai đó là mẹ rồi trở thành không phải mẹ')} {YES} {Q(PN_)} {NO_PE}",
        "Có phải có ai đó là cha rồi" + PE + " " + f"{PE} ".join(f"là {v} rồi" for v in kin[1:-1])
        + f"{PE} là con người rồi trở thành không phải con người không? {YES} {Q(PN_)} {NO_PE}")

    # ---- Paṭivedhānuyogo -----------------------------------------------------------------------------------------------
    head("5-1-20-0", 4, H["Paṭivedhānuyogo"])
    SOT = PN["sotāpanno"]
    add("5-201", f"{NV} {YES} {NANU(ex(SOT))} {YES} {hanci(ex(SOT), P_UP)}")
    rest = [v for _, v in PERSONS[1:]]
    lst = [ex(v) for v in rest]
    lst[5] = f"{rest[5]}{var_sp('Syā.', 'kāyasakkhī')} tồn tại"
    add("5-202", f"{NV} {YES} Chẳng phải " + f"{PE} ".join(lst) + f" sao? {YES}",
        hanci(ex(PN["saddhānusārī"]), P_UP))
    KATVA_S = katva(ex(SOT), P_UP)
    add("5-203", f"{KATVA_S} {YES} {Q(f'có ai đó không phải là {SOT} rồi trở thành {SOT}')} {YES} {Q(NP)} {NO_PE}")
    add("5-204", "Có phải có ai đó " + f"{PE} ".join(f"không phải là {v} rồi" for v in rest[:-1])
        + f"{PE} không phải là {rest[-1]} rồi trở thành {rest[-1]} không? {YES} {Q(NP)} {NO_PE}")
    add("5-205", f"{KATVA_S} {YES} {Q(f'có ai đó là {SOT} rồi trở thành không phải {SOT}')} {YES} {Q(PN_)} {NO_PE}",
        f"Có phải có ai đó là {PN['sakadāgāmī']} rồi{PE} là {PN['anāgāmī']} rồi trở thành không phải "
        f"{PN['anāgāmī']} không? {YES} {Q(PN_)} {NO_PE}", closer("Paṭivedhānuyogo"))

    # ---- Saṅghānuyogo ----------------------------------------------------------------------------------------------------
    head("5-1-21-0", 4, H["Saṅghānuyogo"])
    YUGA = "bốn đôi người, tám hạng người"                       # cattāro purisayugā aṭṭha purisapuggalā
    add("5-206", f"{NV} {YES} {NANU(ex(YUGA))} {YES} {hanci(ex(YUGA), P_UP)}")
    BP = "do sự xuất hiện của Đức Phật"                          # buddhapātubhāvā
    add("5-207", f"{katva(ex(YUGA), P_UP)} {YES} {Q(f'{YUGA} xuất hiện {BP}')} {YES} {Q(f'người xuất hiện {BP}')} "
        f"{NO_PE}",
        f"{Q(f'người xuất hiện {BP}')} {YES} "
        f"{Q('khi Đức Phật, Đức Thế Tôn, đã nhập Niết-bàn trọn vẹn, thì người bị đoạn diệt, người không tồn tại')} "
        f"{NO_PE}", closer("Saṅghānuyogo"))

    # ---- Saccikaṭṭhasabhāgānuyogo -----------------------------------------------------------------------------------
    head("5-1-22-0", 4, H["Saccikaṭṭhasabhāgānuyogo"])
    SK_, ASK = "do điều kiện tạo thành", "không do điều kiện tạo thành"
    NEVA = f"người không phải {SK_} cũng không phải {ASK}"     # puggalo neva saṅkhato nāsaṅkhato
    add("5-208", f"{Q(P_UP)} {YES} {Q(f'người {SK_}')} {NO_PE} {q(f'người {ASK}')} {NO_PE} {q(NEVA)} {NO}")
    KOTI = f"ngoại trừ điều {SK_} và điều {ASK}, có một phạm trù thứ ba khác"
    add("5-209", f"{Q(NEVA)} {YES} {Q(KOTI)} {NO_PE}")
    add("5-210", f"{Q(KOTI)} {YES} {NANU_VUTTAM} “Này các tỳ-khưu, có hai yếu tố này. Hai yếu tố nào? Yếu tố {SK_} "
        f"và yếu tố {ASK}. Này các tỳ-khưu, đây là hai yếu tố” [{CIT['ma. ni.']} 1.125, chỉ khác ở lời xưng hô]! "
        f"{ATTHEVA} {YES} {tena_hi_na(KOTI)}")
    add("5-211", f"{Q(NEVA)} {YES} {Q(f'điều {SK_} là khác, điều {ASK} là khác, người là khác')} {NO_PE}")
    add("5-212", f"{Q(f'các khối {SK_}, Niết-bàn {ASK}, {NEVA}')} {YES} "
        f"{Q('các khối là khác, Niết-bàn là khác, người là khác')} {NO_PE}")
    add("5-213", f"{Q(f'{RUPA} {SK_}, Niết-bàn {ASK}, {NEVA}')} {YES} "
        f"{Q(f'{RUPA} là khác, Niết-bàn là khác, người là khác')} {NO} "
        f"Có phải {VEDANA}{PE} {SANNA}{PE} {SANKHARA}{PE} {VINNANA} {SK_}, Niết-bàn {ASK}, {NEVA} không? {YES} "
        f"{Q(f'{VINNANA} là khác, Niết-bàn là khác, người là khác')} {NO_PE}")
    UP3 = ("sự sinh khởi của người được nhận ra, sự suy tàn được nhận ra, sự đổi khác của cái đang duy trì "
           "được nhận ra")
    NUP3 = ("sự sinh khởi của người không được nhận ra, sự suy tàn không được nhận ra, sự đổi khác của cái đang "
            "duy trì không được nhận ra")
    add("5-214", f"{Q(UP3)} {YES} {Q(f'người {SK_}')} {NO_PE} {VUTTAM} “Này các tỳ-khưu, đây là ba đặc tính {SK_} "
        f"của cái {SK_}. Này các tỳ-khưu, đối với các hiện tượng {SK_}"
        f"{var(CIT['a. ni.'] + ' 3.47', 'katamāni tīṇi')}, sự sinh khởi được nhận ra, sự suy tàn được nhận ra, sự "
        f"đổi khác của những cái đang duy trì được nhận ra” [{CIT['a. ni.']} 3.47]. {cap(UP3)}; vậy thì người {SK_}.")
    add("5-215", f"{Q(NUP3)} {YES} {Q(f'người {ASK}')} {NO_PE} {VUTTAM} “Này các tỳ-khưu, đây là ba đặc tính "
        f"{ASK} của cái {ASK}. Này các tỳ-khưu, đối với các hiện tượng {ASK}, sự sinh khởi không được nhận ra, sự "
        f"suy tàn không được nhận ra, sự đổi khác của những cái đang duy trì không được nhận ra” "
        f"[{CIT['a. ni.']} 3.48]. {cap(NUP3)}; vậy thì người {ASK}.")
    PB = "người đã nhập Niết-bàn trọn vẹn"
    add("5-216", f"{cap(PB)} còn tồn tại hay không còn tồn tại? Còn tồn tại. {Q(f'{PB} là trường tồn')} {NO_PE} "
        f"không còn tồn tại. {Q(f'{PB} bị đoạn diệt')} {NO_PE}")
    add("5-217", f"Người nương vào gì mà duy trì? Nương vào sự hiện hữu mà duy trì. "
        f"{Q(f'sự hiện hữu là {ANICCA}')} {YES} {Q(f'người cũng là {ANICCA}')} {NO_PE}")
    SV, DV, AV = "cảm giác dễ chịu", "cảm giác khó chịu", "cảm giác không khó chịu cũng không dễ chịu"

    def know(x, neg=False):         # X-ṃ vedanaṃ vediyamāno "X-ṃ vedanaṃ vediyāmī"ti (na) pajānāti
        return f"khi đang cảm nhận {x}, {'không ' if neg else ''}hiểu rõ “tôi đang cảm nhận {x}”"

    add("5-218", f"{NV} {YES} {NANU('có ai đó, ' + know(SV))} {YES} {hanci('có ai đó, ' + know(SV), P_UP)}")
    add("5-219", f"{NV} {YES} Chẳng phải có ai đó, khi đang cảm nhận {DV}{PE} {know(AV)} sao? {YES} "
        f"{hanci('có ai đó, ' + know(AV), P_UP)}")
    KATVA_V = katva("có ai đó, " + know(SV), P_UP)
    add("5-220", f"{KATVA_V} {YES} Có phải ai, {know(SV)}, thì chính người ấy là người; ai, {know(SV, True)}, thì "
        f"người ấy không phải là người không? {NO_PE}",
        f"Có phải ai, khi đang cảm nhận {DV}{PE} ai, {know(AV)}, thì chính người ấy là người; ai, {know(AV, True)}, "
        f"thì người ấy không phải là người không? {NO_PE}")
    add("5-221", f"{KATVA_V} {YES} {Q(f'{SV} là khác, người {know(SV)} là khác')} {NO_PE} có phải {DV} là khác{PE} "
        f"{AV} là khác, người {know(AV)} là khác không? {NO_PE}")
    KAYE = "có ai đó, đối với thân, sống quán sát thân"
    add("5-222", f"{NV} {YES} {NANU(KAYE)} {YES} {hanci(KAYE, P_UP)}")
    DHE = "có ai đó, đối với các hiện tượng, sống quán sát các hiện tượng"
    add("5-223", f"{NV} {YES} Chẳng phải có ai đó, đối với các cảm giác{PE} đối với tâm{PE} đối với các hiện tượng, "
        f"sống quán sát các hiện tượng sao? {YES} {hanci(DHE, P_UP)}")
    KATVA_K = katva(KAYE, P_UP)
    add("5-224", f"{KATVA_K} {YES} Có phải ai, đối với thân, sống quán sát thân, thì chính người ấy là người; ai, đối "
        f"với thân, không sống quán sát thân, thì người ấy không phải là người không? {NO_PE}",
        f"Có phải ai, đối với các cảm giác{PE} đối với tâm{PE} đối với các hiện tượng, sống quán sát các hiện tượng, "
        f"thì chính người ấy là người; ai, đối với các hiện tượng, không sống quán sát các hiện tượng, thì người ấy "
        f"không phải là người không? {NO_PE}")
    add("5-225", f"{KATVA_K} {YES} {Q('thân là khác, người đối với thân sống quán sát thân là khác')} {NO_PE} "
        f"có phải cảm giác là khác{PE} tâm là khác{PE} các hiện tượng là khác, người đối với các hiện tượng sống "
        f"quán sát các hiện tượng là khác không? {NO_PE}")
    MOGHA = "Mô-gha-ra-gia"
    add("5-226", f"{Q(P_UP)} {YES} {NANU_VUTTAM}",
        f"“Hãy nhìn thế gian là trống rỗng, này {MOGHA}, luôn luôn tỉnh thức;",
        f"Nhổ bỏ quan điểm về tự ngã [khác chính tả (Syā.): ohacca; (Ka.): uhacca], như vậy có thể vượt qua sự chết;",
        f"Người nhìn thế gian như vậy, vua của sự chết không thấy” [{CIT['su. ni.']} 1125; {CIT['cūḷani.']} 88, "
        f"phần giải thích câu hỏi của thanh niên {MOGHA}].",
        f"{ATTHEVA} {YES} {tena_hi_na(P_UP)}")
    add("5-227", f"{Q('người nhìn')} {YES} Người nhìn cùng với vật chất hay nhìn không có vật chất? Nhìn cùng với vật "
        f"chất. {Q(TAM_JIVAM)} {NO_PE} {neu('nhìn không có vật chất', ANNAM_JIVAM)[0].lower()}"
        f"{neu('nhìn không có vật chất', ANNAM_JIVAM)[1:]} {NO_PE}")
    add("5-228", f"{Q('người nhìn')} {YES} Người nhìn khi ở bên trong hay nhìn sau khi ra bên ngoài? Nhìn khi ở bên "
        f"trong. {Q(TAM_JIVAM)} {NO_PE} {neu('nhìn sau khi ra bên ngoài', ANNAM_JIVAM)[0].lower()}"
        f"{neu('nhìn sau khi ra bên ngoài', ANNAM_JIVAM)[1:]} {NO_PE}")
    NB = NANU(BHAGAVA_SACCA)
    add("5-229", f"{NV} {YES} {NB} {YES} {VUTTAM} “{ATTHI_ATTAHITA}”. {ATTHEVA} {YES} {tena_hi(P_UP)}")
    add("5-230", f"{NV} {YES} {NB} {YES} {VUTTAM} “Này các tỳ-khưu, có một người khi sinh ra trên thế gian thì sinh "
        f"ra vì lợi ích của số đông, vì hạnh phúc của số đông, vì lòng thương xót thế gian, vì sự tốt lành, vì lợi "
        f"ích và vì hạnh phúc của chư thiên và loài người” [{CIT['a. ni.']} 1.162-169]. {ATTHEVA} {YES} "
        f"{tena_hi(P_UP)}")
    add("5-231", f"{Q(P_UP)} {YES} {NB} {YES} {VUTTAM} “tất cả các hiện tượng đều không phải là tự ngã” "
        f"[{CIT['ma. ni.']} 1.356; {CIT['dha. pa.']} 279, trong {CIT['dha. pa.']}]. {ATTHEVA} {YES} "
        f"{tena_hi_na(P_UP)}")
    add("5-232", f"{Q(P_UP)} {YES} {NB} {YES} {VUTTAM} “Người ấy không nghi ngờ, không hoài nghi rằng chỉ có khổ đau "
        f"khi sinh khởi thì sinh khởi, chỉ có khổ đau{var(CIT['saṃ. ni.'] + ' 2.15', 'dukkhaṃ')} khi đang chấm dứt "
        f"thì chấm dứt; người ấy có hiểu biết về điều này mà không lấy người khác làm điều kiện. Này Ca-chiên-diên, "
        f"đến mức ấy là có quan điểm đúng đắn” [{CIT['saṃ. ni.']} 2.15]. {ATTHEVA} {YES} {tena_hi_na(P_UP)}")
    add("5-233", f"{Q(P_UP)} {YES} Chẳng phải tỳ-khưu-ni Va-di-ra đã nói với Ma vương ác độc điều này sao –",
        "“Vì sao ngươi cho rằng có chúng sinh, này Ma vương, phải chăng đó là sự mắc kẹt trong các quan điểm của ngươi;",
        "Đây chỉ là một đống các tạo tác thuần túy, ở đây không có chúng sinh nào được tìm thấy.",
        f"“Cũng như khi các chi phần được ráp lại{var(CIT['bahūsu'], 'yathāpi')}, thì có từ gọi là cỗ xe;",
        f"Cũng vậy, khi có các khối, thì có quy ước gọi là chúng sinh{var_sp('Syā., Kaṃ.', 'sammati')}.",
        "“Thật vậy, chỉ có khổ đau sinh ra, khổ đau duy trì và tan biến;",
        f"Ngoài khổ đau, không gì sinh ra, ngoài khổ đau, không gì chấm dứt” [{CIT['saṃ. ni.']} 1.171].",
        f"{ATTHEVA} {YES} {tena_hi_na(P_UP)}")
    TU = "trống rỗng tự ngã hay những gì thuộc về tự ngã"           # suññaṃ attena vā attaniyena vā
    VED = "dễ chịu, hay khó chịu, hay không khó chịu cũng không dễ chịu"

    def feel(contact):
        return (f"bất cứ cảm nhận nào mà {contact} làm điều kiện cho sinh khởi, {VED}, cảm nhận ấy cũng {TU}")

    SUN = "‘thế gian là trống rỗng’"
    add("5-234", f"{Q(P_UP)} {YES} Chẳng phải tôn giả A-nan đã nói với Đức Thế Tôn điều này sao – “Bạch Thế Tôn, "
        f"người ta nói ‘thế gian là trống rỗng, thế gian là trống rỗng’. Bạch Thế Tôn, đến mức nào thì được gọi là "
        f"{SUN}”? “Này A-nan, vì {TU}, vì vậy được gọi là {SUN}. Này A-nan, cái gì {TU}? Này A-nan, mắt {TU}, các hình "
        f"sắc trống rỗng{PE} thức qua mắt trống rỗng{PE} sự tiếp xúc của mắt trống rỗng{PE} "
        f"{feel('sự tiếp xúc của mắt')}; tai trống rỗng{PE} các âm thanh trống rỗng{PE} mũi trống rỗng{PE} các mùi "
        f"trống rỗng{PE} lưỡi trống rỗng{PE} các vị trống rỗng{PE} thân trống rỗng{PE} các vật xúc chạm trống rỗng{PE} "
        f"ý trống rỗng{PE} các đối tượng của ý trống rỗng{PE} ý thức trống rỗng{PE} sự tiếp xúc của ý trống rỗng{PE} "
        f"{feel('sự tiếp xúc của ý')}. Này A-nan, vì {TU}, vì vậy được gọi là {SUN}” [{CIT['saṃ. ni.']} 4.85]. "
        f"{ATTHEVA} {YES} {tena_hi_na(P_UP)}")
    add("5-235", f"{Q(P_UP)} {YES} {NB} {YES} {VUTTAM} “Này các tỳ-khưu, khi có tự ngã, thì có thể có ý nghĩ ‘cái "
        f"thuộc về tự ngã của tôi’ không?” “Thưa vâng, bạch Thế Tôn”. “Này các tỳ-khưu, khi có cái thuộc về tự ngã, "
        f"thì có thể có ý nghĩ ‘tự ngã của tôi’ không?” “Thưa vâng, bạch Thế Tôn”. “Này các tỳ-khưu, khi tự ngã và "
        f"cái thuộc về tự ngã không được tìm thấy như là sự thật, như là điều chắc chắn"
        f"{var(CIT['ma. ni.'] + ' 1.244', 'anupalabbhamāne')}, thì nền tảng của quan điểm này"
        f" [dị bản (Syā.): yamidaṃ; ({CIT['ma. ni.']} 1.244): yampitaṃ] cho rằng thế gian ấy chính là tự ngã ấy, sau "
        f"khi chết tôi sẽ là cái ấy, thường còn, bền vững, trường tồn, không có bản chất biến đổi, tôi sẽ duy trì cũng "
        f"vậy, ngang bằng với sự vĩnh cửu – ‘này các tỳ-khưu, chẳng phải đó hoàn toàn là một giáo pháp của kẻ ngu si "
        f"trọn vẹn sao’”? “Bạch Thế Tôn, sao lại không như vậy được, bạch Thế Tôn, đó hoàn toàn là một giáo pháp của "
        f"kẻ ngu si trọn vẹn” [{CIT['ma. ni.']} 1.244]. {ATTHEVA} {YES} {tena_hi_na(P_UP)}")
    add("5-236", f"{Q(P_UP)} {YES} {NB} {YES} {VUTTAM} “Này {SENIYA}, có ba bậc đạo sư này đang có mặt, thực sự "
        f"hiện hữu ở thế gian. Ba bậc nào? Này {SENIYA}, ở đời này, có bậc đạo sư {SACCATO} {DITTHE}, và {SACCATO} "
        f"{ABHISAMPARAYA}.",
        f"“Lại nữa, này {SENIYA}, ở đời này, có bậc đạo sư {SACCATO} {DITTHE}, nhưng quả thật không {SACCATO} "
        f"{ABHISAMPARAYA}.",
        f"“Lại nữa, này {SENIYA}, ở đời này, có bậc đạo sư không {SACCATO} {DITTHE}, và không {SACCATO} "
        f"{ABHISAMPARAYA}.",
        f"“Này {SENIYA}, trong số đó, bậc đạo sư nào {SACCATO} {DITTHE}, và {SACCATO} {ABHISAMPARAYA} – này "
        f"{SENIYA}, vị này được gọi là {SASSATAVADO}.",
        f"“Này {SENIYA}, trong số đó, bậc đạo sư nào {SACCATO} {DITTHE}, nhưng quả thật không {SACCATO} "
        f"{ABHISAMPARAYA} – này {SENIYA}, vị này được gọi là {UCCHEDAVADO}.",
        f"“Này {SENIYA}, trong số đó, bậc đạo sư nào không {SACCATO} {DITTHE}, và không {SACCATO} {ABHISAMPARAYA} – "
        f"này {SENIYA}, vị này được gọi là bậc đạo sư, bậc Tự Giác Ngộ Hoàn Toàn. Này {SENIYA}, đây là "
        f"{TINAM_ONE} đang có mặt, thực sự hiện hữu ở thế gian” [{CIT['pu. pa.']} 131, trong "
        f"{CIT['pu. pa.']}, giống nhau về ý nghĩa]. {ATTHEVA} {YES} {tena_hi_na(P_UP)}")
    add("5-237", f"{Q(P_UP)} {YES} {NB} {YES} {Q(VUTTAM + ' “hũ bơ lỏng”')} {YES} "
        f"{Q('có ai đó làm ra hũ bằng bơ lỏng')} {NO_PE} {tena_hi_na(P_UP)[0].lower()}{tena_hi_na(P_UP)[1:]}")
    jars = ["hũ dầu", "hũ mật ong", "hũ đường mía", "hũ sữa", "hũ nước", "đĩa nước uống", "chén nước uống",
            "bát nước uống", "bữa ăn thường còn", "cháo bền vững"]
    add("5-238", f"{Q(P_UP)} {YES} {NB} {YES} Có phải {VUTTAM} “" + f"{PE} ".join(jars) + f"” không? {YES} "
        f"{Q('có thứ cháo nào thường còn, bền vững, trường tồn, không có bản chất biến đổi')} {NO_PE} "
        f"{tena_hi_na(P_UP)} {SAMKHITTAM}",
        "Nhóm tám sự bác bỏ, các phần lặp lại, sự trôi lăn, sự dựa vào;",
        "Với tâm là thứ năm, điều tốt đẹp, thần thông, với việc dẫn kinh là thứ tám.",
        closer("Saccikaṭṭhasabhāgānuyogo"), katha_end("người"))
    return S


# ---------------------------------------------------------------------------------------------------------------
# Checks (per line: dash count vs the Pāli line, balanced quotes per segment, NFC; plus the reuse assertion)
# ---------------------------------------------------------------------------------------------------------------
DASHES = ("–", "—")


def dash_count(t):
    return sum(t.count(d) for d in DASHES)


def dash_ok(pali_line, vi_line):
    return dash_count(pali_line) == dash_count(vi_line)


def quotes_ok(text):
    """Balanced “” and ‘’ (checked per segment, since verse quotes span lines). A stanza or paragraph of a
    multi-paragraph quote re-opens with “ at its line start (Pāli convention); such re-openings are not counted."""
    lines = text.split("\n")
    body = "\n".join([lines[0]] + [ln[1:] if ln.startswith("“") and _open_before(lines[:k + 1]) else ln
                                   for k, ln in enumerate(lines[1:])])
    return body.count("“") == body.count("”") and body.count("‘") == body.count("’")


def _open_before(prev):
    t = "\n".join(prev)
    return t.count("“") > t.count("”")


def nfc_ok(t):
    return unicodedata.normalize("NFC", t) == t


def check_reused():
    texts = {}
    for b, d in RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def check_against_pali(name, segs):
    pl = [x for x in (PALI_DIR / name).read_text(encoding="utf-8").splitlines() if x.strip()]
    vl = [x for s in segs for x in s]
    assert len(pl) == len(vl), (name, len(pl), len(vl))
    probs = []
    for k, (p, v) in enumerate(zip(pl, vl), 1):
        if not dash_ok(p, v):
            probs.append(f"line {k}: dashes pali {dash_count(p)} vi {dash_count(v)}")
        if not nfc_ok(v):
            probs.append(f"line {k}: not NFC")
        pid, vid = re.search(r"\^\S+$", p), re.search(r"\^\S+$", v)
        if (pid and pid.group(0)) != (vid and vid.group(0)):
            probs.append(f"line {k}: id {pid and pid.group(0)} vs {vid and vid.group(0)}")
        for bad in ("—", ":-", "….", ".…", "  ", "chánh niệm"):
            if bad in v:
                probs.append(f"line {k}: {bad!r}")
        if re.search(r"[āīūṃṅñṭḍṇḷfjwzFJWZ]", re.sub(r"\[[^\]]*\]", "", re.sub(r"\^\S+$", "", v))):
            probs.append(f"line {k}: foreign letter")
    for s in segs:
        if not quotes_ok("\n".join(s)):
            probs.append(f"unbalanced quotes in segment ending {s[-1][-12:]}")
    assert not probs, f"{name}:\n" + "\n".join(probs[:40])


def write(name, segs):
    check_against_pali(name, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text
    (OUT_DIR / name).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT_DIR / name)


# ---------------------------------------------------------------------------------------------------------------
# Formula file
# ---------------------------------------------------------------------------------------------------------------
def formulas():
    tag = {v: b for _, v, b in REUSED}
    out = ["# pi-5 Kathāvatthu: Vietnamese rails formulas and fixed strings (binding for ch2-31)", "",
           "Format: Pāli = tiếng Việt, one per line; (pi-1) … (pi-4) = taken unchanged from that book's approved "
           "Vietnamese rails (asserted by the builder). Generated by build_rails_sample_vi.py: import its constants "
           "and frame functions (pentad, hanci, noce, yam, tvam_ce, ese_ce, na_niggahetabbe, Q, NANU, katva, neu, "
           "rq …) rather than retyping. P / Q are slots; «…» inside a slot is its inner quote, rendered one level "
           "deeper (rq). Termbase: AI_translation/vietnamese/pi-5-pali-vietnamese-termbase-plain.md "
           "(+ pi-5-vi-ai/termbase/APPROVED.md). Style: 0-INBOX/temp/pipeline/vietnamese-style.md.", ""]

    def row(p, v, note=""):
        t = f" ({'pi-' + tag[v]})" if v in tag else ""
        out.append(f"{p} = {v}{t}{note}")

    out += ["## Book frame and headings", ""]
    row("Namo tassa bhagavato arahato sammāsambuddhassa", HOMAGE)
    row("# Abhidhammapiṭake", H_ABHI)
    row("## Kathāvatthupāḷi", H_BOOK)
    row("<X>kathā (heading)", katha("<X>"))
    row("<X>kathā niṭṭhitā.", katha_end("<X>"))
    row("Paṭhamo / Dutiyo … vaggo (N-vaggo)", vaggo(1) + " / " + vaggo(2) + " …")
    row("Kalyāṇavaggo paṭhamo.", KALYANAVAGGO)
    row("(Saṃkhittaṃ)", SAMKHITTAM)
    row("(Ka) / (Kha) / (Ga)", f"{KA} / {KHA} / {GA}")
    for k in ("Puggalakathā", "Suddhasaccikaṭṭho", "okāsasaccikaṭṭho", "kālasaccikaṭṭho", "avayavasaccikaṭṭho",
              "Anulomapaccanīkaṃ", "Paccanīkānulomaṃ", "Suddhikasaṃsandanaṃ", "Opammasaṃsandanaṃ",
              "Catukkanayasaṃsandanaṃ", "Lakkhaṇayuttikathā", "Vacanasodhanaṃ"):
        row(k, H[k])
    row("X-anuyogo", anuyogo("X"))
    for k in ANUYOGA:
        row(k, H[k])
    row("closing label (Suddhikasaṃsandanā., Gatianuyogo. …)", "the heading + «.» (Sự đối chiếu thuần túy. …)")
    out += ["", "## Thesis, answers, questions", ""]
    row('"X"ti?', Q("X"))
    row('…pe… "x"ti? (new question after …pe…)', q("x"))
    row("Āmantā.", YES)
    row("Āmantā? (as written)", YES_Q)
    row("Na hevaṃ vattabbe.", NO)
    row("Na hevaṃ vattabbe…pe….", NO_PE)
    row("Vattabbaṃ.", SHOULD)
    row("…pe…", PE + "  (same spot; never «.…» / «….»; a final «.» after …pe… is absorbed)")
    row("Nanu Xti?", NANU("X"))
    row('Nanu vuttaṃ bhagavatā – "…"', NANU_VUTTAM + " “…”  (keep the Pāli's final . / ! / ?)")
    row('Vuttaṃ bhagavatā – "…"', VUTTAM + " “…”")
    row('Vuttaṃ bhagavatā – "…"ti? (question)', "Có phải Đức Thế Tôn đã nói – “…” không?")
    row('Na vattabbaṃ – "X"ti?', na_vattabbam("X"))
    row("Attheva suttantoti?", ATTHEVA)
    row("Tena hi Xti.", tena_hi("X"))
    row('Tena hi na vattabbaṃ – "X"ti.', tena_hi_na("X"))
    row("Xti katvā tena ca kāraṇena Yti?", katva("X", "Y"))
    row("Xti katvā teneva kāraṇena Yti?", "Có phải vì cho rằng X, chính vì lý do ấy, Y không?")
    row("Xti, Yti?", neu("X", "Y"))
    row('"X"ti vattabbo', vattabbo("X"))
    row("Aññaṃ X añño Y", anna("X", "Y"))
    row("X … Y …ti? (alternative question: rūpaṃ passati puggalaṃ passatīti?)", "… X hay … Y?")
    row("Yo X, sveva puggalo; yo na X, na so puggaloti?",
        "Có phải ai X, thì chính người ấy là người; ai không X, thì người ấy không phải là người không?")
    row("Yo X, sveva puggalo? Yo na X, na so puggaloti?",
        "Ai X, có phải chính người ấy là người không? Ai không X, người ấy không phải là người sao?")
    row("Nanu bhagavā saccavādī kālavādī bhūtavādī tathavādī avitathavādī anaññathavādīti?", NANU(BHAGAVA_SACCA))
    row("bhikkhave", "Này các tỳ-khưu");  row("bhante", "bạch Thế Tôn")
    out += ["", "## Rebuttal pentad (slots P, Q)", ""]
    row("Ājānāhi niggahaṃ.", ADMIT["niggaha"])
    row("Ājānāhi paṭikammaṃ.", ADMIT["patikamma"])
    row('Hañci P, tena vata re vattabbe – "Q"ti.', hanci("P", "Q"))
    row('Hañci P; tena vata re vattabbe – "Q"ti.', hanci("P", "Q", ";"))
    row('Hañci P, no ca vata re vattabbe – "Q"ti.', hanci_neg("P", "Q"))
    row('No ce pana vattabbe – "Q"ti, no ca vata re vattabbe – "P"ti.', noce("P", "Q"))
    row('Yaṃ tattha vadesi – "vattabbe kho – ‘P’, no ca vattabbe – ‘Q’"ti micchā.', yam("P", "Q"))
    row('… "’ti idaṃ te micchā.', yam("P", "Q", te=True))
    row("… micchā…pe….", yam("P", "Q", pe=True))
    row('Tvaṃ ce pana maññasi – "vattabbe kho – ‘P’, no ca vattabbe – ‘Q’ti, tena tava tattha hetāya paṭiññāya '
        'hevaṃ paṭijānantaṃ hevaṃ niggahetabbe. Atha taṃ niggaṇhāma. Suniggahito ca hosi.', tvam_ce("P", "Q"))
    row('Ese ce dunniggahite hevamevaṃ tattha dakkha. Vattabbe kho – "P," no ca vattabbe – "Q"ti. No ca mayaṃ tayā '
        'tattha hetāya paṭiññāya hevaṃ paṭijānantā hevaṃ niggahetabbā. Atha maṃ niggaṇhāsi. Dunniggahitā ca homa.',
        ese_ce("P", "Q"))
    row('Na hevaṃ niggahetabbe. Tena hi yaṃ niggaṇhāsi – "hañci P, tena vata re vattabbe – ‘Q’ti. Yaṃ tattha vadesi '
        '– "vattabbe kho – ‘P, no ca vattabbe – Q"’ti micchā.', na_niggahetabbe("P", "Q"))
    row("Tena hi ye kate niggahe se niggahe dukkaṭe. Sukate paṭikamme. Sukatā paṭipādanāti.", KATE)
    for k, v in LABEL.items():
        row(k + ".", v)
    row("Paṭhamo / Dutiyo / Tatiyo / Catuttho / Pañcamo / Chaṭṭho / Sattamo niggaho.",
        " / ".join(niggaho(n) for n in range(1, 8)))
    row("quote-order repair", "the Pāli's garbled close \"’ is rendered ’” (inner quote closes first); "
        "missing quote marks / commas of a repeated formula are supplied as meant")
    out += ["", "## Speaker notes, variants, citations", ""]
    row("[iminā lakkhaṇena sakavādīpucchā dassitā]", NOTE_SAKA)
    row("[iminā lakkhaṇena paravādīpucchā dassitā]", NOTE_PARA)
    row("[ṭīkā oloketabbā]", f"[{TIKA}]")
    row("[word (sī. syā.)] spelling only", var_sp("Sī., Syā.", "word").strip())
    row("[word (sī.)] other word", var("Sī.", "word").strip())
    row("[word (bahūsu)]", var(CIT["bahūsu"], "word").strip())
    row("[word (?)]", var("?", "word").strip())
    for k, v in CIT.items():
        if k != "bahūsu":
            row(f"{k} N.N (citation)", f"{v} N.N")
    row("… thokaṃ visadisaṃ (citation note)", "…, hơi khác một chút")
    row("… ālapanamattameva nānaṃ (citation note)", "…, chỉ khác ở lời xưng hô")
    row("… atthato ekaṃ (citation note)", "…, giống nhau về ý nghĩa")
    out += ["", "## Core terms of the debate", ""]
    row("saccikaṭṭhaparamatthena", SP)
    row("saccikaṭṭha / paramattha", "thực tại chân thật / thực tại tối hậu")
    row("upalabbhati / nupalabbhati", "được tìm thấy / không được tìm thấy")
    row("puggalo upalabbhati saccikaṭṭhaparamatthena", P_UP)
    row("puggalo nupalabbhati saccikaṭṭhaparamatthena", P_NUP)
    row("yo saccikaṭṭho paramattho, tato so puggalo upalabbhati saccikaṭṭhaparamatthena", yo_tato())
    row("sabbattha / sabbadā / sabbesu (puggalo upalabbhati …)", "… ở mọi nơi / vào mọi lúc / trong mọi thứ")
    row("sakavādī / paravādī", f"{SAKAVADI} / {PARAVADI}")
    row("puggalo", PERSON)
    row("re", RE)
    row('vuttaṃ bhagavatā – "atthi puggalo attahitāya paṭipanno"', rq(SUTTA_ATTHI, 0))
    row("atthi puggalo attahitāya paṭipanno", ATTHI_ATTAHITA)
    row("X ca upalabbhati (in a list)", "và X được tìm thấy")
    row("X puggalo / Xsmiṃ puggalo / aññatra X puggalo / puggalasmiṃ X",
        "X là người / người ở trong X / người tách rời khỏi X / X ở trong người")
    row("rūpa / vedanā / saññā / saṅkhārā / viññāṇa (aggregates)", f"{RUPA} / {VEDANA} / {SANNA} / {SANKHARA} / {VINNANA}")
    for p, v in AYATANA + DHATU + INDRIYA:
        row(p, v)
    row("micchādiṭṭhi … micchāsamādhi", ", ".join(MICCHA) + " (pi-2)")
    row("sammādiṭṭhi … sammāsamādhi", ", ".join(SAMMA) + " (pi-1)")
    row("aniccaṃ saṅkhataṃ paṭiccasamuppannaṃ khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhammaṃ "
        "vipariṇāmadhammaṃ", ANICCA)
    row("saphalā savipākā iṭṭhaphalā kantaphalā manuññaphalā asecanakaphalā sukhudrayā sukhavipākā", SAPHALA_K)
    row("saphalā savipākā aniṭṭhaphalā akantaphalā amanuññaphalā secanakaphalā dukkhudrayā dukkhavipākā", SAPHALA_A)
    row("X upādāya Y-assa paññatti", "dựa vào X mà có sự định danh Y")
    row("Yathā X, evamevaṃ Y", f"{YATHA_DOC} X, cũng y như vậy, Y")
    row("saṅkhato / asaṅkhato", "do điều kiện tạo thành / không do điều kiện tạo thành")
    row("puggalo neva saṅkhato nāsaṅkhato", "người không phải do điều kiện tạo thành cũng không phải không do điều kiện tạo thành")
    row("asmā lokā paraṃ lokaṃ, parasmā lokā imaṃ lokaṃ", LOKA)
    row("puggalo sandhāvati … / sveva puggalo sandhāvati …", f"{SANDHAVATI} / {SVEVA}")
    row("so puggalo / añño puggalo / so ca añño ca", "người ấy / người khác / cả người ấy và người khác")
    row("atthi koci X hutvā Y hoti", "có ai đó là X rồi trở thành Y")
    row("sveva X so Y", "chính X ấy là Y ấy")
    row("taṃ jīvaṃ taṃ sarīraṃ / aññaṃ jīvaṃ aññaṃ sarīraṃ", f"{TAM_JIVAM} / {ANNAM_JIVAM}")
    row("kāyoti vā sarīranti vā … tajjāte", KAYA_K)
    row("kalyāṇapāpakāni kammāni", KALYANA_KAMMA)
    row("kattā kāretā", KK + " (+ «ra X» for a non-kamma object)")
    row("(vipāka)paṭisaṃvedī", "người cảm nhận (quả / X)")
    row("Tassa tasseva natthi dukkhassa antakiriyā, natthi vaṭṭupacchedo, natthi anupādāparinibbānaṃ", TASSA_TASSEVA)
    row("mahāpathavī / mahāsamuddo / sinerupabbatarājā / āpo / tejo / vāyo / tiṇakaṭṭhavanappatayo",
        " / ".join(v for _, v in NATURE) + " / " + TINA)
    row("X atthi (existence thesis)", "X tồn tại")
    row("dibbaṃ / mānusakaṃ sukhaṃ; āpāyikaṃ / nerayikaṃ dukkhaṃ",
        "hạnh phúc cõi trời / cõi người; khổ đau ở cõi khổ / ở địa ngục")
    row("sukhaṃ vedanaṃ vediyamāno \"sukhaṃ vedanaṃ vediyāmī\"ti pajānāti",
        "khi đang cảm nhận cảm giác dễ chịu, hiểu rõ “tôi đang cảm nhận cảm giác dễ chịu”")
    row("kāye kāyānupassī viharati", "đối với thân, sống quán sát thân (pi-2)")
    for p, v in PERSONS:
        row(p, v)
    for p, v in KIN:
        row(p, v)
    row("Seniya / Ānanda / Kaccāna / Mogharāja / Vajirā / Māra",
        f"{SENIYA} / A-nan / Ca-chiên-diên / Mô-gha-ra-gia / Va-di-ra / Ma vương")
    row("attānaṃ saccato thetato paññāpeti", SACCATO)
    row("diṭṭheva dhamme / diṭṭhe ceva dhamme", DITTHE)
    row("abhisamparāyaṃ", ABHISAMPARAYA)
    row("sassatavādo / ucchedavādo satthā", f"{SASSATAVADO} / {UCCHEDAVADO}")
    return "\n".join(out) + "\n"


YATHA_DOC = "cũng như"


def main():
    check_reused()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write("preamble.md", build_preamble())
    write("1-puggalakatha.md", build_ch1())
    FORMULAS_MD.write_text(unicodedata.normalize("NFC", formulas()), encoding="utf-8", newline="\n")
    print("wrote", FORMULAS_MD)


if __name__ == "__main__":
    main()
