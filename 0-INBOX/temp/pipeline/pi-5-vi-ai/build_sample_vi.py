# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot SAMPLE builder: preamble.md and 1-puggalakatha.md.

The debate formulas of the whole book are module constants / helper functions. Chapter agents import this
module and use them VERBATIM:

    import sys; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-5-vi-ai")
    import build_sample_vi as S
    S.Q(x); S.AMANTA; S.NA_HEVAM; S.line_b("n", p, q); S.line_c(p, q, idam=True); S.yam(p, q) ...

Propositions (p, q, x) are passed lowercase, without final punctuation; the frames add capitals,
the question words, the dashes and the quotes. Quote levels: “…” outer, ‘…’ inner, the third level
unquoted (as the Pāli). The Pāli's odd closing order "’ is always rendered in the nested order ’”.

Importing does not write anything; run  python -I -X utf8 build_sample_vi.py  to rebuild the two files.
At build time every string claimed from pi-1 / pi-2 / pi-3 / pi-4 (CROSS_BOOK) is asserted to occur in those
rails files, and every output line is checked against its Pāli line (dash count, quote counts, IDs).
"""
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI_DIR = ROOT / "AI_translation/pali/pi-5_split_chapters"
OUT_DIR = ROOT / "AI_translation/vietnamese/pi-5-vietnamese-plain-zeroshot_split_chapters"
RAILS_DIR = {b: ROOT / f"AI_translation/vietnamese/pi-{b}-vietnamese-plain-rails_split_chapters" for b in (1, 2, 3, 4)}


def cap(s):
    return s[:1].upper() + s[1:]


# ================================================================ book frame
HOMAGE = "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"   # pi-1..4 ^T-1
PITAKA = "Tạng Vi Diệu Pháp"                                               # pi-1..4 ^0
BOOK_TITLE = "Các vấn đề tranh luận"                                       # Kathāvatthupāḷi (new)
BOOK_TITLE_ALTERNATIVES = ("Những điểm tranh luận", "Các chủ đề thảo luận")
KATHA = "Bàn về {x}"                                  # <X>kathā (chapter / kathā heading)
KATHA_END = "Phần bàn về {x} đã hoàn tất."            # <X>kathā niṭṭhitā. (niṭṭhita = «đã hoàn tất», pi-1)
NUM = {1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười",
       11: "mười một", 12: "mười hai", 13: "mười ba", 14: "mười bốn", 15: "mười lăm", 16: "mười sáu",
       17: "mười bảy", 18: "mười tám", 19: "mười chín", 20: "hai mươi", 21: "hai mươi mốt", 22: "hai mươi hai",
       23: "hai mươi ba"}
ORD = {1: "thứ nhất", 2: "thứ hai", 3: "thứ ba", 4: "thứ tư", 5: "thứ năm", 6: "thứ sáu", 7: "thứ bảy",
       8: "thứ tám", 9: "thứ chín", 10: "thứ mười"}
ORD.update({n: f"thứ {NUM[n]}" for n in range(11, 24)})
VAGGA = {n: f"Chương {ORD[n]}" for n in range(1, 24)}  # Dutiyavaggo = «Chương thứ hai» … Tevīsatimavaggo
KALYANAVAGGO_PATHAMO = "Chương về điều tốt, chương thứ nhất."   # Kalyāṇavaggo paṭhamo. (ch1 ^5-192)
SAMKHITTAM = "(Tóm lược)"                                         # (Saṃkhittaṃ)

# ================================================================ core terms
PUGGALA = "người"                                   # puggala (core term)
SACCIKATTHA = "thực tại chân thật"                  # saccikaṭṭha
PARAMATTHA = "thực tại tối hậu"                     # paramattha
CT = "như một thực tại chân thật và tối hậu"         # saccikaṭṭhaparamatthena
YO_CT = "theo đúng cách mà thực tại chân thật, tối hậu được tìm thấy"  # yo saccikaṭṭho paramattho, tato …
UP = "được tìm thấy"                                # upalabbhati / upalabbhanti
NUP = "không được tìm thấy"                         # nupalabbhati
SAKAVADI = "người theo học thuyết của chúng ta"     # sakavādī
PARAVADI = "người theo học thuyết khác"             # paravādī
SAKAVADI_NOTE = f"[với dấu hiệu này, câu hỏi của {SAKAVADI} được trình bày]"   # [iminā lakkhaṇena sakavādīpucchā dassitā]
PARAVADI_NOTE = f"[với dấu hiệu này, câu hỏi của {PARAVADI} được trình bày]"   # [iminā lakkhaṇena paravādīpucchā dassitā]
TIKA_NOTE = "cần tham khảo Phụ chú giải"            # ṭīkā oloketabbā
VAR = "dị bản"                                      # word-level variant label
SPELL = "khác chính tả"                             # spelling-only variant label

P_UP = f"người {UP} {CT}"                           # puggalo upalabbhati saccikaṭṭhaparamatthena
P_NUP = f"người {NUP} {CT}"                         # puggalo nupalabbhati saccikaṭṭhaparamatthena
YO_UP = f"người ấy {UP} {CT}, {YO_CT}"              # yo saccikaṭṭho paramattho, tato so puggalo upalabbhati …
YO_NUP = f"người ấy {NUP} {CT}, {YO_CT}"            # … tato so puggalo nupalabbhati …

# ================================================================ answers and question frames
AMANTA = "Đúng vậy."                     # Āmantā.
NA_HEVAM = "Không nên nói như vậy."      # Na hevaṃ vattabbe.
NA_HEVAM_PE = "Không nên nói như vậy…"   # Na hevaṃ vattabbe…pe… (never «.…» or «….»)
AMANTA_PE = "Đúng vậy…"                 # Āmantā…pe…
VATTABBAM = "Nên nói."                   # Vattabbaṃ. (answer)
ATTHEVA = "Có bài kinh như vậy thật không?"    # Attheva suttantoti?
NANU_VUTTAM = "Chẳng phải Đức Thế Tôn đã nói thế này sao –"   # Nanu vuttaṃ bhagavatā –
VUTTAM = "Đức Thế Tôn đã nói –"          # Vuttaṃ bhagavatā – (statement)
BHAGAVA_SACCAVADI = ("Chẳng phải Đức Thế Tôn là người nói sự thật, nói đúng lúc, nói điều có thật, nói đúng như "
                     "thật, nói không sai lệch, nói không khác đi sao?")
# Nanu bhagavā saccavādī kālavādī bhūtavādī tathavādī avitathavādī anaññathavādīti?


def Q(x):
    """"X"ti? / Xti? (thesis question)."""
    return f"Có phải {x} không?"


def q(x):
    """The same question after …pe… (lowercase start)."""
    return f"có phải {x} không?"


def NANU(x):
    """Nanu Xti? (rhetorical question)."""
    return f"Chẳng phải {x} sao?"


def NA_VATTABBAM_Q(x):
    """Na vattabbaṃ – "X"ti?"""
    return f"Có phải không nên nói – “{x}” không?"


def TENA_HI(x):
    """Tena hi Xti. (conclusion)"""
    return f"Vậy thì {x}."


def TENA_HI_NA(x):
    """Tena hi na vattabbaṃ – "X"ti."""
    return f"Vậy thì không nên nói – “{x}”."


def KATVA(x, y, teneva=False):
    """Xti katvā tena ca kāraṇena Yti? / … teneva kāraṇena …"""
    link = "chính vì lý do ấy" if teneva else "và vì lý do ấy"
    return f"Có phải vì cho rằng {x}, {link}, {y} không?"


# ================================================================ rebuttal pentad (anuloma … niggamana)
AJANAHI = {"n": "Hãy thừa nhận sự bác bỏ.", "p": "Hãy thừa nhận sự phản bác."}  # Ājānāhi niggahaṃ / paṭikammaṃ.
HANCI = "Nếu {p}, thì này bạn, chắc chắn nên nói – “{q}”."                    # Hañci P, tena vata re vattabbe – "Q"ti.
HANCI_VA_PANA = "Hoặc nếu {p}, thì này bạn, chắc chắn nên nói – “{q}”."       # Hañci vā pana P, tena vata re vattabbe – "Q"ti.
NO_CE = "Còn nếu không nên nói – “{q}”, thì này bạn, chắc chắn không nên nói – “{p}”."
# No ce pana vattabbe – "Q"ti, no ca vata re vattabbe – "P"ti.
TENA_VATA = "thì này bạn, chắc chắn nên nói –"          # tena vata re vattabbe –
NO_CA_VATA = "thì này bạn, chắc chắn không nên nói –"   # no ca vata re vattabbe –
YAM_TATTHA = "Điều bạn nói ở đây là sai"                # Yaṃ tattha vadesi – "…"ti micchā (verdict fronted: no extra dash)
YAM_IDAM_TE = "Điều bạn nói ở đây là sai lầm của bạn"   # Yaṃ tattha vadesi – "…"ti idaṃ te micchā
VATTABBE_KHO = "nên nói – ‘{p}’, nhưng không nên nói – ‘{q}’"   # vattabbe kho – ‘P,’ no ca vattabbe – ‘Q’
# Niggaha / paṭikamma catukka lines
TVAM_CE_1 = ("Nhưng nếu bạn cho rằng – “nên nói – ‘{p}’, nhưng không nên nói – ‘{q}’, thì dựa trên chính lời "
             "khẳng định này của bạn{v1} ở đây, bạn, người thừa nhận như vậy{v2}, nên bị bác bỏ như vậy. "
             "Vậy chúng tôi bác bỏ bạn. Và bạn đã bị bác bỏ một cách đúng đắn{v3}.")
# Tvaṃ ce pana maññasi – "vattabbe kho – ‘P,’ no ca vattabbe – ‘Q’ti, tena tava tattha hetāya paṭiññāya hevaṃ
# paṭijānantaṃ hevaṃ niggahetabbe. Atha taṃ niggaṇhāma. Suniggahito ca hosi.   (^5-3: the outer quote is not closed)
TVAM_CE_2 = ("Nhưng nếu bạn cho rằng – “nên nói – ‘{p}’, nhưng không nên nói – ‘{q}’”, thì dựa trên chính lời "
             "khẳng định này của bạn ở đây, bạn, người thừa nhận như vậy, nên bị bác bỏ như vậy. "
             "Vậy chúng tôi bác bỏ bạn. Và bạn đã bị bác bỏ một cách đúng đắn.")          # ^5-8 (quote closed)
ESE_CE = ("Nếu điều này bị bác bỏ một cách sai trái, thì ở đây hãy nhìn nhận cũng y như vậy{v1}. "
          "Nên nói – “{p}”, nhưng không nên nói – “{q}”. Nhưng dựa trên chính lời khẳng định này ở đây, "
          "chúng tôi, những người thừa nhận như vậy, không nên bị bạn bác bỏ như vậy. Vậy mà bạn bác bỏ tôi. "
          "Và chúng tôi đã bị bác bỏ một cách sai trái{v2}.")
# Ese ce dunniggahite hevamevaṃ tattha dakkha. Vattabbe kho – "P," no ca vattabbe – "Q"ti. No ca mayaṃ tayā tattha
# hetāya paṭiññāya hevaṃ paṭijānantā hevaṃ niggahetabbā. Atha maṃ niggaṇhāsi. Dunniggahitā ca homa.
NA_HEVAM_NIGGAHETABBE = "Không nên bác bỏ như vậy."            # Na hevaṃ niggahetabbe.
TENA_HI_YAM_NIGGANHASI = "Vậy thì, lời bác bỏ mà bạn đã đưa ra –"  # Tena hi yaṃ niggaṇhāsi –
NIGGAMANA_END = ("Vậy thì, sự bác bỏ đã được thực hiện ấy là sự bác bỏ được thực hiện sai trái. "
                 "Sự phản bác được thực hiện đúng đắn. Việc dẫn dắt lập luận được thực hiện đúng đắn.")
# Tena hi ye kate niggahe se niggahe dukkaṭe. Sukate paṭikamme. Sukatā paṭipādanāti.

# section labels
ANULOMAPANCAKAM = "Nhóm năm phần theo chiều thuận."          # Anulomapañcakaṃ.
PACCANIKAPANCAKAM = "Nhóm năm phần theo chiều nghịch."       # Paccanīkapañcakaṃ.
PATIKAMMACATUKKAM = "Nhóm bốn phần về sự phản bác."          # Paṭikammacatukkaṃ.
NIGGAHACATUKKAM = "Nhóm bốn phần về sự bác bỏ."              # Niggahacatukkaṃ.
UPANAYANACATUKKAM = "Nhóm bốn phần về sự áp dụng."           # Upanayanacatukkaṃ.
NIGGAMANACATUKKAM = "Nhóm bốn phần về sự kết luận."          # Niggamanacatukkaṃ.
NIGGAHO = {n: f"Sự bác bỏ {ORD[n]}." for n in range(1, 8)}   # Paṭhamo … Sattamo niggaho.
ATTHAKANIGGAHO = "Nhóm tám sự bác bỏ."                       # Aṭṭhakaniggaho. (as written, in place of «Aṭṭhamo»)
ANULOMAPACCANIKAM = "Chiều thuận và chiều nghịch"            # ##### Anulomapaccanīkaṃ
PACCANIKANULOMAM = "Chiều nghịch và chiều thuận"             # ##### Paccanīkānulomaṃ

# ch1 sub-headings (= closing labels with a full stop)
H = {
    "Puggalakathā": "Bàn về người",
    "Suddhasaccikaṭṭho": "Thực tại chân thật thuần túy",
    "okāsasaccikaṭṭho": "Thực tại chân thật xét theo nơi chốn",
    "kālasaccikaṭṭho": "Thực tại chân thật xét theo thời gian",
    "avayavasaccikaṭṭho": "Thực tại chân thật xét theo các bộ phận",
    "Suddhikasaṃsandanaṃ": "Sự đối chiếu thuần túy",
    "Opammasaṃsandanaṃ": "Sự đối chiếu bằng phép so sánh",
    "Catukkanayasaṃsandanaṃ": "Sự đối chiếu theo phương pháp bốn cách",
    "Lakkhaṇayuttikathā": "Bàn về lập luận dựa trên đặc tính",
    "Vacanasodhanaṃ": "Sự làm sáng tỏ từ ngữ",
    "Paññattānuyogo": "Chất vấn về sự định danh",
    "Gatianuyogo": "Chất vấn về cõi tái sinh",
    "Upādāpaññattānuyogo": "Chất vấn về sự định danh phụ thuộc",
    "Purisakārānuyogo": "Chất vấn về việc làm của con người",
    "Abhiññānuyogo": "Chất vấn về các loại hiểu biết trực tiếp",
    "Ñātakānuyogādi": "Chất vấn về người thân và các mục khác",
    "Paṭivedhānuyogo": "Chất vấn về sự thấu triệt",
    "Saṅghānuyogo": "Chất vấn về Tăng đoàn",
    "Saccikaṭṭhasabhāgānuyogo": "Chất vấn về những gì cùng bản chất với thực tại chân thật",
}


def hanci(p, qq, frame=HANCI):
    return frame.format(p=p, q=qq)


def no_ce(qq, p, variant=""):
    s = NO_CE.format(q=qq, p=p)
    if variant:
        s = s.replace("thì này bạn,", f"thì này bạn {variant},", 1)
    return s


def yam(p, qq, idam=False, end="."):
    """Yaṃ tattha vadesi – "vattabbe kho – ‘P,’ no ca vattabbe – ‘Q"’ti micchā (end="…" for micchā…pe….)."""
    head = YAM_IDAM_TE if idam else YAM_TATTHA
    return f"{head} – “{VATTABBE_KHO.format(p=p, q=qq)}”{end}"


def line_a(p, qq, ans=NA_HEVAM, pre=""):
    """"P"ti? Āmantā. "Q"ti? Na hevaṃ vattabbe."""
    return f"{pre}{Q(p)} {AMANTA} {Q(qq)} {ans}"


def line_b(kind, p, qq, end="."):
    """Ājānāhi niggahaṃ/paṭikammaṃ. Hañci P, tena vata re vattabbe – "Q"ti. Yaṃ tattha vadesi – … micchā."""
    return f"{AJANAHI[kind]} {hanci(p, qq)} {yam(p, qq, end=end)}"


def line_b0(p, qq, idam=False, end="."):
    """Hañci P, … micchā. (without Ājānāhi)"""
    return f"{hanci(p, qq)} {yam(p, qq, idam, end)}"


def line_c(p, qq, idam=False, end=".", variant=""):
    """No ce pana vattabbe – "Q"ti, no ca vata re vattabbe – "P"ti. Yaṃ tattha vadesi – … micchā."""
    return f"{no_ce(qq, p, variant)} {yam(p, qq, idam, end)}"


def niggamana_1(p, qq, inner_single=False):
    """Na hevaṃ niggahetabbe. Tena hi yaṃ niggaṇhāsi – "hañci P, tena vata re vattabbe – ‘Q’ti. Yaṃ tattha vadesi –
    "vattabbe kho – ‘P, no ca vattabbe – Q"’ti micchā.   (^5-10: the second level opens with ‘ instead of ")"""
    if inner_single:
        tail = f"{YAM_TATTHA} – ‘nên nói – {p}, nhưng không nên nói – {qq}’”."
    else:
        tail = f"{YAM_TATTHA} – “nên nói – ‘{p}, nhưng không nên nói – {qq}’”."
    return (f"{NA_HEVAM_NIGGAHETABBE} {TENA_HI_YAM_NIGGANHASI} “nếu {p}, {TENA_VATA} ‘{qq}’. " + tail)


def chain(items, sep="… "):
    return sep.join(items)


# ================================================================ vocabulary (cross-book where marked)
RUPA = "vật chất"; VEDANA = "cảm giác"; SANNA = "tri giác"; SANKHARA = "các tạo tác"; VINNANA = "thức"  # pi-2 ^2-1
KHANDHA = "khối"
AYATANA = ["lĩnh vực mắt", "lĩnh vực tai", "lĩnh vực mũi", "lĩnh vực lưỡi", "lĩnh vực thân",
           "lĩnh vực hình sắc", "lĩnh vực âm thanh", "lĩnh vực mùi", "lĩnh vực vị", "lĩnh vực vật xúc chạm",
           "lĩnh vực ý", "lĩnh vực đối tượng của ý"]                                       # pi-2 ^2 āyatana list
DHATU = ["yếu tố mắt", "yếu tố tai", "yếu tố mũi", "yếu tố lưỡi", "yếu tố thân", "yếu tố hình sắc",
         "yếu tố âm thanh", "yếu tố mùi", "yếu tố vị", "yếu tố vật xúc chạm", "yếu tố thức qua mắt",
         "yếu tố thức qua tai", "yếu tố thức qua mũi", "yếu tố thức qua lưỡi", "yếu tố thức qua thân",
         "yếu tố ý", "yếu tố ý thức", "yếu tố đối tượng của ý"]                               # pi-2 ^2-183
INDRIYA = ["năng lực mắt", "năng lực tai", "năng lực mũi", "năng lực lưỡi", "năng lực thân", "năng lực ý",
           "năng lực sống", "năng lực nữ tính", "năng lực nam tính", "năng lực dễ chịu", "năng lực khó chịu",
           "năng lực niềm vui", "năng lực nỗi buồn", "năng lực bình thản", "năng lực niềm tin",
           "năng lực tinh tấn", "năng lực tỉnh thức", "năng lực định tâm", "năng lực trí tuệ",
           "năng lực biết được điều chưa từng biết", "năng lực hiểu biết trọn vẹn",
           "năng lực của người đã hiểu biết trọn vẹn"]                                          # pi-2 ^2-219 (pi-5 order)
ANNATAVI = "năng lực của người đã hiểu biết trọn vẹn"   # aññātāvindriya
ANNINDRIYA = "năng lực hiểu biết trọn vẹn"              # aññindriya
MICCHA = ["quan điểm sai lầm", "tư duy sai lầm", "lời nói sai lầm", "hành động sai lầm", "sinh kế sai lầm",
          "nỗ lực sai lầm", "tỉnh thức sai lầm", "định tâm sai lầm"]                            # pi-2 ^2-956
SAMMA = ["quan điểm đúng đắn", "tư duy đúng đắn", "lời nói đúng đắn", "hành động đúng đắn", "sinh kế đúng đắn",
         "nỗ lực đúng đắn", "tỉnh thức đúng đắn", "định tâm đúng đắn"]
ANICCA = ("vô thường, do điều kiện tạo thành, sinh khởi tùy thuộc vào điều kiện, có bản chất diệt tận, "
          "có bản chất suy tàn, có bản chất phai nhạt, có bản chất chấm dứt, có bản chất biến đổi")
# anicca saṅkhata paṭiccasamuppanna khaya- vaya- virāga- nirodha- vipariṇāmadhamma (pi-1 / pi-2)
NICCO_DHUVO = "thường còn, bền vững, trường tồn, có bản chất không biến đổi"   # nicco dhuvo sassato avipariṇāmadhammo (pi-2)
ATTHI_PUGGALO = "có người thực hành vì lợi ích của bản thân"   # atthi puggalo attahitāya paṭipanno (pi-4 ^4 matrix 4.24)
VB = f"{VUTTAM} “{ATTHI_PUGGALO}”"          # vuttaṃ bhagavatā – "atthi puggalo attahitāya paṭipanno"
VB_IN = f"{VUTTAM} ‘{ATTHI_PUGGALO}’"       # second quote level
VB_IN2 = f"{VUTTAM} {ATTHI_PUGGALO}"        # third level (unquoted, as the Pāli)
SANDHAVATI = "trôi lăn"                     # sandhāvati (pi-4 sandhāvitvā «trôi lăn»)
LOKA = "từ thế gian này sang thế gian khác, từ thế gian khác sang thế gian này"
# asmā lokā paraṃ lokaṃ, parasmā lokā imaṃ lokaṃ (ayaṃ loko / paro loko = «thế gian này / thế gian khác», pi-1)
SANDH = f"{SANDHAVATI} {LOKA}"
TAM_JIVAM = "linh hồn và thân thể là một"              # taṃ jīvaṃ taṃ sarīraṃ (pi-1 ^1 diṭṭhāsava)
ANNAM_JIVAM = "linh hồn là khác, thân thể là khác"     # aññaṃ jīvaṃ aññaṃ sarīraṃ (pi-1)
KHATTIYO = "người thuộc giai cấp quý tộc"; BRAHMANO = "bà-la-môn"; VESSO = "người thuộc giai cấp thương nhân"
SUDDO = "người thuộc giai cấp lao động"; GAHATTHO = "người tại gia"; PABBAJITO = "người xuất gia"
DEVO = "vị trời"; MANUSSO = "con người"                                                    # pi-2 ^2 (itthasmi)
KPK = "các nghiệp tốt đẹp và xấu ác"        # kalyāṇapāpakāni kammāni (pi-2 kalyāṇapāpakānaṃ kammānaṃ)
UPD = "dựa vào {x} mà có sự định danh {who}"   # X upādāya Y-assa paññatti (paññatti «sự định danh», pi-4)


def upd(x, who="người"):
    return UPD.format(x=x, who=who)


# ================================================================ cross-book asserts
CROSS_BOOK = [
    (HOMAGE, 1), (PITAKA, 1), ("Định danh các hạng người", 4), ("Tăng Chi Bộ Kinh", 4), ("Trung Bộ Kinh", 4),
    ("khối vật chất, khối cảm giác, khối tri giác, khối tạo tác, khối thức", 2),
    ("lĩnh vực mắt, lĩnh vực hình sắc, lĩnh vực tai, lĩnh vực âm thanh, lĩnh vực mũi, lĩnh vực mùi, lĩnh vực "
     "lưỡi, lĩnh vực vị, lĩnh vực thân, lĩnh vực vật xúc chạm, lĩnh vực ý, lĩnh vực đối tượng của ý", 2),
    ("yếu tố mắt, yếu tố hình sắc, yếu tố thức qua mắt, yếu tố tai, yếu tố âm thanh, yếu tố thức qua tai, yếu tố "
     "mũi, yếu tố mùi, yếu tố thức qua mũi, yếu tố lưỡi, yếu tố vị, yếu tố thức qua lưỡi, yếu tố thân, yếu tố vật "
     "xúc chạm, yếu tố thức qua thân, yếu tố ý, yếu tố đối tượng của ý, yếu tố ý thức", 2),
    ("năng lực mắt, năng lực tai, năng lực mũi, năng lực lưỡi, năng lực thân, năng lực ý, năng lực nữ tính, năng "
     "lực nam tính, năng lực sống, năng lực dễ chịu, năng lực khó chịu, năng lực niềm vui, năng lực nỗi buồn, "
     "năng lực bình thản, năng lực niềm tin, năng lực tinh tấn", 2),
    ("năng lực tỉnh thức, năng lực định tâm, năng lực trí tuệ, năng lực biết được điều chưa từng biết, năng lực "
     "hiểu biết trọn vẹn, năng lực của người đã hiểu biết trọn vẹn", 2),
    ("Quan điểm sai lầm, tư duy sai lầm, lời nói sai lầm, hành động sai lầm, sinh kế sai lầm, nỗ lực sai lầm, "
     "tỉnh thức sai lầm, định tâm sai lầm", 2),
    ("quan điểm đúng đắn", 1), ("tư duy đúng đắn", 1), ("lời nói đúng đắn", 2), ("hành động đúng đắn", 2),
    ("sinh kế đúng đắn", 2), ("nỗ lực đúng đắn", 1), ("tỉnh thức đúng đắn", 1), ("định tâm đúng đắn", 1),
    ("có bản chất diệt tận, có bản chất suy tàn, có bản chất phai nhạt, có bản chất chấm dứt", 2),
    ("có bản chất biến đổi", 2), ("sinh khởi tùy thuộc vào điều kiện", 1), ("do điều kiện tạo thành", 1),
    ("yếu tố không do điều kiện tạo thành", 1), ("Các hiện tượng có điều kiện", 3),
    (NICCO_DHUVO, 2), ("quả của các nghiệp tốt đẹp và xấu ác", 2),
    ("Có người thực hành vì lợi ích của bản thân", 4),
    ("người được giải thoát theo cả hai cách, người được giải thoát nhờ trí tuệ, người chứng nghiệm bằng thân, "
     "người đạt đến quan điểm, người được giải thoát nhờ niềm tin, người đi theo Giáo Pháp, người đi theo niềm tin", 4),
    ("bậc vào dòng", 4), ("bậc trở lại một lần", 4), ("bậc không trở lại", 4), ("bậc A-la-hán", 4),
    ("có bậc đạo sư đề ra tự ngã như là sự thật, như là điều chắc chắn ngay trong đời này, và đề ra tự ngã như "
     "là sự thật, như là điều chắc chắn trong đời sau", 4),
    ("có bậc đạo sư đề ra tự ngã như là sự thật, như là điều chắc chắn ngay trong đời này, nhưng quả thật không "
     "đề ra tự ngã như là sự thật, như là điều chắc chắn trong đời sau", 4),
    ("có bậc đạo sư không đề ra tự ngã như là sự thật, như là điều chắc chắn ngay trong đời này, và không đề ra "
     "tự ngã như là sự thật, như là điều chắc chắn trong đời sau", 4),
    ("bậc đạo sư nào đề ra tự ngã như là sự thật, như là điều chắc chắn ngay trong đời này, và đề ra tự ngã như "
     "là sự thật, như là điều chắc chắn trong đời sau", 4),
    ("bậc đạo sư theo học thuyết về sự trường tồn", 4), ("bậc đạo sư theo học thuyết về sự đoạn diệt", 4),
    ("bậc Tự Giác Ngộ Hoàn Toàn", 4), ("Lại có ba bậc đạo sư khác", 4),
    ("bằng thiên nhãn thanh tịnh, vượt quá mắt người", 2),
    ("thấy chúng sinh đang chết đi, đang tái sinh, thấp kém, ưu việt, đẹp đẽ, xấu xí, ở cõi tốt lành, ở cõi xấu, "
     "và hiểu rõ các chúng sinh đi theo nghiệp của mình", 2),
    ("Linh hồn và thân thể là một", 1), ("Linh hồn là khác, thân thể là khác", 1), ("trường tồn", 1),
    ("người thuộc giai cấp quý tộc", 2), ("bà-la-môn", 2), ("người thuộc giai cấp thương nhân", 2),
    ("người thuộc giai cấp lao động", 2), ("người tại gia", 2), ("người xuất gia", 2), ("vị trời", 2),
    ("con người", 2), ("người có hình sắc", 2), ("người không có hình sắc", 2),
    ("ngạ quỷ", 2), ("loài súc sinh", 2), ("chúng sinh địa ngục", 2), ("việc sát hại sinh mạng", 2),
    ("mẹ, hay cha, hay anh em trai, hay chị em gái", 2),
    ("trôi lăn", 4), ("đi đến tận cùng của khổ đau", 4), ("nhập Niết-bàn trọn vẹn", 4),
    ("sự hiện hữu gồm một khối, sự hiện hữu gồm bốn khối, sự hiện hữu gồm năm khối", 2),
    ("không thấy được nhưng có tính va chạm", 1), ("thấy được và có tính va chạm", 1),
    ("màu xanh, màu vàng, màu đỏ, màu trắng", 1),
    ("sự diệt tận các ô nhiễm", 2), ("sự nhớ lại các đời sống trước", 2), ("tâm người khác", 2),
    ("hiểu biết trực tiếp", 2), ("thần thông", 1), ("chứng nghiệm", 2),
    ("như là sự thật, như là điều chắc chắn", 2), ("thế giới loài người", 2), ("thế giới chư thiên", 2),
    ("sự tiếp xúc của mắt", 1), ("thức qua mắt", 2), ("không khó chịu cũng không dễ chịu", 1),
    ("cõi hình sắc", 1), ("cõi không hình sắc", 1), ("cõi dục lạc", 1), ("hạng người", 4),
    ("sống quán sát thân", 2), ("sống quán sát các hiện tượng", 2), ("đại dương", 1),
    ("chướng ngại vô minh", 1), ("không phải là tự ngã", 2), ("bóng râm", 1),
    ("đời sống tu hành trong sạch", 1), ("sự thiết lập tỉnh thức", 1), ("suy thoái", 2), ("giáo huấn", 2),
    ("đã hoàn tất", 1), ("khuynh hướng tiềm ẩn", 2), ("đã sinh khởi", 1), ("có điều kiện", 3),
    ("sự sinh khởi", 1), ("sự chấm dứt", 1), ("được gộp vào", 3), ("sự định danh", 4),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))) for b, d in RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts: {len(CROSS_BOOK)} strings found in pi-1..4 rails")


# ================================================================ chapter builders
class Doc:
    def __init__(self):
        self.blocks = []

    def seg(self, sid, *lines):
        lines = list(lines)
        lines[-1] = f"{lines[-1]} ^{sid}"
        self.blocks.append(lines)

    def head(self, level, text, sid):
        self.blocks.append([f"{'#' * level} {text} ^{sid}"])

    def text(self):
        return "\n\n".join("\n".join(b) for b in self.blocks) + "\n"


def build_preamble():
    d = Doc()
    d.seg("T-1", HOMAGE)
    d.head(1, PITAKA, "0")
    d.head(2, BOOK_TITLE, "5-0")
    return d.text()


def build_ch1():
    d = Doc()
    d.head(3, H["Puggalakathā"], "5-1-0")
    # ------------------------------------------------ 1. Suddhasaccikaṭṭho, anuloma
    d.head(4, H["Suddhasaccikaṭṭho"], "5-1-1-0")
    d.head(5, ANULOMAPACCANIKAM, "5-1-1-1-0")
    d.seg("5-1",
          f"{SAKAVADI_NOTE} Có phải {P_UP} [{SPELL} (Syā., Pī., Ka., Sī.): saccikaṭṭhaparamaṭṭhenāti] không? "
          f"{AMANTA} {Q(YO_UP)} {NA_HEVAM}",
          line_b("n", P_UP, YO_UP),
          line_c(P_UP, YO_UP, variant=f"[{VAR} (Syā., Pī.): no vata re]"),
          ANULOMAPANCAKAM)
    d.seg("5-2",
          line_a(P_NUP, YO_NUP, pre=PARAVADI_NOTE + " "),
          line_b("p", P_NUP, YO_NUP),
          line_c(P_NUP, YO_NUP),
          PATIKAMMACATUKKAM)
    d.seg("5-3",
          TVAM_CE_1.format(p=P_NUP, q=YO_NUP, v1=f" [{VAR} (Syā.): tvaṃ; {TIKA_NOTE}]", v2=f" [{TIKA_NOTE}]",
                           v3=f" [{VAR} (Syā.): suniggahitova]"),
          line_b0(P_NUP, YO_NUP),
          line_c(P_NUP, YO_NUP, idam=True),
          NIGGAHACATUKKAM)
    d.seg("5-4",
          ESE_CE.format(p=P_UP, q=YO_UP, v1=f" [{SPELL} (Syā.): hevameva]", v2=f" [{VAR} (Syā.): dunniggahitāva]"),
          line_b0(P_UP, YO_UP),
          line_c(P_UP, YO_UP, idam=True),
          UPANAYANACATUKKAM)
    d.seg("5-5",
          niggamana_1(P_UP, YO_UP),
          f"{line_c(P_UP, YO_UP, idam=True)} {NIGGAMANA_END}",
          NIGGAMANACATUKKAM,
          NIGGAHO[1])
    # ------------------------------------------------ 2. Suddhasaccikaṭṭho, paccanīka
    d.head(4, H["Suddhasaccikaṭṭho"], "5-1-2-0")
    d.head(5, PACCANIKANULOMAM, "5-1-2-1-0")
    d.seg("5-6", line_a(P_NUP, YO_NUP), line_b("n", P_NUP, YO_NUP), line_c(P_NUP, YO_NUP), PACCANIKAPANCAKAM)
    d.seg("5-7", line_a(P_UP, YO_UP), line_b("p", P_UP, YO_UP), line_c(P_UP, YO_UP), PATIKAMMACATUKKAM)
    d.seg("5-8", TVAM_CE_2.format(p=P_UP, q=YO_UP), line_b0(P_UP, YO_UP), line_c(P_UP, YO_UP, idam=True))
    d.seg("5-9", ESE_CE.format(p=P_NUP, q=YO_NUP, v1="", v2=""), line_b0(P_NUP, YO_NUP),
          line_c(P_NUP, YO_NUP, idam=True), UPANAYANACATUKKAM)
    d.seg("5-10",
          niggamana_1(P_NUP, YO_NUP, inner_single=True),
          f"{line_c(P_NUP, YO_NUP, idam=True)} {NIGGAMANA_END}",
          NIGGAMANACATUKKAM,
          NIGGAHO[2])
    # ------------------------------------------------ 3-8. okāsa / kāla / avayava
    adv = [("okāsasaccikaṭṭho", "ở mọi nơi"), ("kālasaccikaṭṭho", "vào mọi lúc"), ("avayavasaccikaṭṭho", "trong mọi thứ")]
    n = 3
    for letter, neg, sub in (("a", False, ANULOMAPACCANIKAM), ("b", True, PACCANIKANULOMAM)):
        for key, a in adv:
            hid = n + 0
            d.head(4, f"({letter}) {H[key]}", f"5-1-{hid}-0")
            d.head(5, sub, f"5-1-{hid}-1-0")
            p = P_NUP if neg else P_UP
            s = f"người {NUP if neg else UP} {a} {CT}"
            label = NIGGAHO[n] if n < 8 else ATTHAKANIGGAHO
            d.seg(f"5-{n + 8}", line_a(p, s), line_b("n", p, s), line_c(p, s, end="…"), label)
            n += 1
    # ------------------------------------------------ Suddhikasaṃsandanaṃ
    d.head(4, H["Suddhikasaṃsandanaṃ"], "5-1-9-0")
    rupa_ca = f"{RUPA} cũng {UP} {CT}"
    ar = f"{RUPA} là khác, người là khác"
    pp = f"{P_UP}, {rupa_ca}"
    d.seg("5-17", line_a(pp, ar), line_b("n", pp, ar), line_c(pp, ar, end="…"))
    vin_ca = f"{VINNANA} cũng {UP} {CT}"
    tk = f"{VINNANA} là khác, người là khác"
    pp2 = f"{P_UP}, {vin_ca}"
    d.seg("5-18",
          f"Có phải {P_UP}, {VEDANA} cũng {UP} {CT}… {SANNA} cũng {UP}… {SANKHARA} cũng {UP}… {vin_ca} không? "
          f"{AMANTA} {Q(tk)} {NA_HEVAM}",
          line_b("n", pp2, tk), line_c(pp2, tk, end="…"))
    ay = [f"{AYATANA[0]} cũng {UP} {CT}"] + [f"{x} cũng {UP}" for x in AYATANA[1:-1]] + [f"{AYATANA[-1]} cũng {UP} {CT}"]
    d.seg("5-19", f"{cap(P_UP)}, {chain(ay)}…")
    dh = [f"{cap(DHATU[0])} cũng {UP} {CT}"] + [f"{x} cũng {UP}" for x in DHATU[1:-1]] + [f"{DHATU[-1]} cũng {UP} {CT}"]
    d.seg("5-20", f"{chain(dh)}…")
    ind = [f"{INDRIYA[0]} cũng {UP} {CT}"] + [f"{x} cũng {UP}" for x in INDRIYA[1:-1]] + [f"{INDRIYA[-1]} cũng {UP} {CT}"]
    aai = f"{ANNATAVI} là khác, người là khác"
    aai_ca = f"{ANNATAVI} cũng {UP} {CT}"
    pp3 = f"{P_UP}, {aai_ca}"
    d.seg("5-21",
          f"Có phải {chain(ind)} không? {AMANTA} {Q(aai)} {NA_HEVAM}",
          line_b("n", pp3, aai), line_c(pp3, aai, end="…"))

    def vb_b(x, y, end="."):
        return (f"{AJANAHI['p']} Nếu {VB}, {x}, {TENA_VATA} “{y}”. "
                f"{YAM_TATTHA} – “nên nói – ‘{VB_IN2}, {x}’, nhưng không nên nói – ‘{y}’”{end}")

    def vb_c(x, y, end="."):
        return (f"Còn nếu không nên nói – “{y}”, {NO_CA_VATA} “{VB_IN}, {x}”. "
                f"{YAM_TATTHA} – “nên nói – ‘{VB_IN2}, {x}’, nhưng không nên nói – ‘{y}’”{end}")

    d.seg("5-22",
          f"[Định danh các hạng người, ma trận 4.24; Tăng Chi Bộ Kinh 4.95-96] {Q(P_NUP)} {AMANTA} "
          f"Có phải {VB}, {rupa_ca} không? {AMANTA} {Q(ar)} {NA_HEVAM}",
          vb_b(rupa_ca, ar), vb_c(rupa_ca, ar, end="…"))
    d.seg("5-23",
          f"{Q(P_NUP)} {AMANTA} Có phải {VB}, {VEDANA} cũng {UP}… {SANNA} cũng {UP}… {SANKHARA} cũng {UP}… "
          f"{vin_ca} không? {AMANTA} {Q(tk)} {NA_HEVAM}",
          vb_b(vin_ca, tk),
          f"Còn nếu không nên nói – “{tk}”, {NO_CA_VATA} “{VB_IN}, {vin_ca}”. "
          f"{YAM_TATTHA} – “nên nói – ‘{VB_IN2}’, {vin_ca}, nhưng không nên nói – ‘{tk}’”…")
    d.seg("5-24", f"{Q(P_NUP)} {AMANTA} {VB}, {AYATANA[0]} cũng {UP} {CT}… {AYATANA[1]} cũng {UP}… "
                  f"{AYATANA[-1]} cũng {UP} {CT}…")
    d.seg("5-25", f"{cap(DHATU[0])} cũng {UP} {CT}… {DHATU[4]} cũng {UP}… {DHATU[5]} cũng {UP}… {DHATU[9]} cũng "
                  f"{UP}… {DHATU[10]} cũng {UP}… {DHATU[16]} cũng {UP}… {DHATU[17]} cũng {UP} {CT}…")
    d.seg("5-26", f"{cap(INDRIYA[0])} cũng {UP} {CT}… {INDRIYA[1]} cũng {UP} {CT}… {ANNINDRIYA} "
                  f"[{VAR} (nhiều bản): aññātāvindriyañca] cũng {UP} {CT}…")
    d.seg("5-27",
          f"{Q(P_NUP)} {AMANTA} Có phải {VB}, {aai_ca} không? {AMANTA} {Q(aai)} {NA_HEVAM}",
          vb_b(aai_ca, aai), vb_c(aai_ca, aai, end="…"),
          f"{H['Suddhikasaṃsandanaṃ']}.")
    # ------------------------------------------------ Opammasaṃsandanaṃ
    d.head(4, H["Opammasaṃsandanaṃ"], "5-1-10-0")
    rv = f"{RUPA} {UP} {CT}, {VEDANA} cũng {UP} {CT}, {RUPA} là khác, {VEDANA} là khác"
    d.seg("5-28", f"{Q(rv)} {AMANTA} {Q(pp)} {AMANTA} {Q(ar)} {NA_HEVAM}",
          line_b("n", f"{rv}, {pp}", ar), line_c(f"{rv}, {pp}", ar, end="…"))
    rvi = f"{RUPA} {UP} {CT}, {vin_ca}, {RUPA} là khác, {VINNANA} là khác"
    d.seg("5-29",
          f"Có phải {RUPA} {UP} {CT}, {SANNA} cũng {UP}… {SANKHARA} cũng {UP}… {vin_ca}, {RUPA} là khác, "
          f"{VINNANA} là khác không? {AMANTA} {Q(pp)} {AMANTA} {Q(ar)} {NA_HEVAM}",
          line_b("n", f"{rvi}, {pp}", ar), line_c(f"{rvi}, {pp}", ar, end="…"))
    d.seg("5-30", f"{cap(VEDANA)} {UP} {CT}, {SANNA} cũng {UP}… {SANKHARA} cũng {UP}… {VINNANA} cũng {UP}… {rupa_ca}…")
    d.seg("5-31", f"{cap(SANNA)} {UP} {CT}, {SANKHARA} cũng {UP}… {VINNANA} cũng {UP}… {RUPA} cũng {UP}… "
                  f"{VEDANA} cũng {UP} {CT}…")
    d.seg("5-32", f"{cap(SANKHARA)} {UP} {CT}, {VINNANA} cũng {UP}… {RUPA} cũng {UP}… {VEDANA} cũng {UP}… "
                  f"{SANNA} cũng {UP} {CT}…")
    pp_vin = f"{P_UP}, {vin_ca}"
    vs = f"{VINNANA} {UP} {CT}, {SANKHARA} cũng {UP} {CT}, {VINNANA} là khác, {SANKHARA} là khác"
    d.seg("5-33",
          f"Có phải {VINNANA} {UP} {CT}, {RUPA} cũng {UP}… {VEDANA} cũng {UP}… {SANNA} cũng {UP}… {SANKHARA} cũng "
          f"{UP} {CT}, {VINNANA} là khác, {SANKHARA} là khác không? {AMANTA} {Q(pp_vin)} {AMANTA} {Q(tk)} {NA_HEVAM}",
          line_b("n", f"{vs}, {pp_vin}", tk), line_c(f"{vs}, {pp_vin}", tk, end="…"))
    ay_cross = (f"{cap(AYATANA[0])} {UP} {CT}, {AYATANA[1]} cũng {UP}… {AYATANA[-1]} cũng {UP} {CT}… "
                f"{AYATANA[1]} {UP}… {AYATANA[-1]} {UP} {CT}, {AYATANA[0]} cũng {UP}… {AYATANA[-2]} cũng {UP} {CT}…")
    d.seg("5-34", ay_cross)
    dh_cross = (f"{cap(DHATU[0])} {UP} {CT}, {DHATU[1]} cũng {UP}… {DHATU[-1]} cũng {UP} {CT}… "
                f"{DHATU[1]} {UP}… {DHATU[-1]} {UP} {CT}, {DHATU[0]} cũng {UP}… {DHATU[-2]} cũng {UP} {CT}…")
    d.seg("5-35", dh_cross)
    aai_ai = f"{ANNATAVI} {UP} {CT}, {ANNINDRIYA} cũng {UP} {CT}, {ANNATAVI} là khác, {ANNINDRIYA} là khác"
    ind_cross = (f"{INDRIYA[0]} {UP} {CT}, {INDRIYA[1]} cũng {UP}… {ANNATAVI} cũng {UP} {CT}… {INDRIYA[1]} {UP}… "
                 f"{ANNATAVI} {UP} {CT}")
    d.seg("5-36",
          f"Có phải {ind_cross}… {INDRIYA[0]} cũng {UP}… {ANNINDRIYA} cũng {UP} {CT}, {ANNATAVI} là khác, "
          f"{ANNINDRIYA} là khác không? {AMANTA} {Q(pp3)} {AMANTA} {Q(aai)} {NA_HEVAM}",
          line_b("n", f"{aai_ai}, {pp3}", aai), line_c(f"{aai_ai}, {pp3}", aai, end="…"))
    d.seg("5-37",
          f"{Q(rv)} {AMANTA} Có phải {VB}, {rupa_ca} không? {AMANTA} {Q(ar)} {NA_HEVAM}",
          f"{AJANAHI['p']} Nếu {rv}, {VB}, {rupa_ca}, {TENA_VATA} {ar}. "
          f"{YAM_TATTHA} – “nên nói – ‘{rv}, {VB_IN2}, {rupa_ca}’, nhưng không nên nói – ‘{ar}’”.",
          f"Còn nếu không nên nói – “{ar}”, {NO_CA_VATA} “{rv}, {VB_IN}, {rupa_ca}”. "
          f"{YAM_TATTHA} – “nên nói – ‘{rv}, {VB_IN2}, {rupa_ca}’, nhưng không nên nói – ‘{ar}’”…")
    d.seg("5-38", f"{cap(RUPA)} {UP} {CT}, {SANNA} cũng {UP}… {SANKHARA} cũng {UP}… {vin_ca}…")
    d.seg("5-39", f"{cap(VEDANA)} {UP} {CT}, {SANNA} cũng {UP}… {SANKHARA} cũng {UP}… {VINNANA} cũng {UP}… {rupa_ca}…")
    d.seg("5-40", f"{cap(SANNA)} {UP} {CT}, {SANKHARA} cũng {UP}… {VINNANA} cũng {UP}… {RUPA} cũng {UP}… "
                  f"{VEDANA} cũng {UP} {CT}…")
    d.seg("5-41", f"{cap(SANKHARA)} {UP} {CT}, {VINNANA} cũng {UP}… {RUPA} cũng {UP}… {VEDANA} cũng {UP}… "
                  f"{SANNA} cũng {UP} {CT}…")
    d.seg("5-42", f"{cap(VINNANA)} {UP} {CT}, {RUPA} cũng {UP}… {VEDANA} cũng {UP}… {SANNA} cũng {UP}… "
                  f"{SANKHARA} cũng {UP} {CT}…")
    d.seg("5-43", ay_cross)
    d.seg("5-44", dh_cross)
    d.seg("5-45",
          f"Có phải {ind_cross}, {INDRIYA[0]} cũng {UP}… {ANNINDRIYA} cũng {UP} {CT}; {ANNATAVI} là khác, "
          f"{ANNINDRIYA} là khác không? {AMANTA} Có phải {VB}, {aai_ca} không? {AMANTA} {Q(aai)} {NA_HEVAM}",
          f"{AJANAHI['p']} Nếu {aai_ai}, {VB}, {aai_ca}, {TENA_VATA} “{aai}”. "
          f"{YAM_TATTHA} – “nên nói – ‘{aai_ai}, {VB_IN2}, {aai_ca}’, nhưng không nên nói – ‘{aai}’”.",
          f"Còn nếu không nên nói – “{aai}”, {NO_CA_VATA} “{aai_ai}, {VB_IN}, {aai_ca}”. "
          f"{YAM_TATTHA} – “nên nói – ‘{aai_ai}, {VB_IN2}, {aai_ca}’, nhưng không nên nói – ‘{aai}’”…",
          f"{H['Opammasaṃsandanaṃ']}.")
    # ------------------------------------------------ Catukkanayasaṃsandanaṃ
    d.head(4, H["Catukkanayasaṃsandanaṃ"], "5-1-11-0")

    def four(x, loc=None, abl=None):
        """X puggalo / Xsmiṃ puggalo / aññatra X puggalo / puggalasmiṃ X"""
        return [f"{x} là người", f"người ở trong {x}", f"người tách rời khỏi {x}", f"{x} ở trong người"]

    rp = f"{RUPA} là người"
    d.seg("5-46", line_a(P_UP, rp), line_b("n", P_UP, rp), line_c(P_UP, rp, end="…"))
    r4 = four(RUPA)
    d.seg("5-47", f"{Q(P_UP)} {AMANTA} Có phải {chain(r4[1:])} không? {NA_HEVAM}",
          line_b("n", P_UP, r4[3]), line_c(P_UP, r4[3], end="…"))
    v4, s4, k4, n4 = four(VEDANA), four(SANNA), four(SANKHARA), four(VINNANA)
    d.seg("5-48",
          f"{Q(P_UP)} {AMANTA} {cap(chain(v4))}…",
          f"{cap(chain(s4))}…",
          f"{cap(chain(k4))}…",
          f"Có phải {chain(n4)} không? {NA_HEVAM}",
          line_b("n", P_UP, n4[3]), line_c(P_UP, n4[3], end="…"))
    a4 = four(AYATANA[0]) + four(AYATANA[-1])
    d4 = four(DHATU[0]) + four(DHATU[-1])
    i4 = four(INDRIYA[0]) + four(ANNATAVI)
    d.seg("5-49",
          f"{Q(P_UP)} {AMANTA} {cap(chain(a4))}…",
          f"{cap(chain(d4))}…",
          f"Có phải {chain(i4)} không? {NA_HEVAM}",
          line_b("n", P_UP, i4[7]), line_c(P_UP, i4[7], end="…"))

    def vb_b0(y, end="."):
        return (f"{AJANAHI['p']} Nếu {VB}, {TENA_VATA} “{y}”. "
                f"{YAM_TATTHA} – “nên nói – ‘{VB_IN2}’, nhưng không nên nói – ‘{y}’”{end}")

    def vb_c0(y, end="."):
        return (f"Còn nếu không nên nói – “{y}”, {NO_CA_VATA} “{VB_IN}”. "
                f"{YAM_TATTHA} – “nên nói – ‘{VB_IN2}’, nhưng không nên nói – ‘{y}’”{end}")

    vbq = f"{Q(P_NUP)} {AMANTA} {Q(VB)} {AMANTA}"
    d.seg("5-50", f"{vbq} {Q(rp)} {NA_HEVAM}", vb_b0(rp), vb_c0(rp, end="…"))
    d.seg("5-51",
          f"{vbq} {cap(chain(r4[1:]))}…",
          f"{cap(chain(v4))}…", f"{cap(chain(s4))}…", f"{cap(chain(k4))}…",
          f"Có phải {chain(n4)} không? {NA_HEVAM}",
          vb_b0(n4[3]), vb_c0(n4[3], end="…"))
    d.seg("5-52",
          f"{vbq} {cap(chain(a4))}…",
          f"{cap(chain(d4))}…",
          f"Có phải {chain(i4)} không? {NA_HEVAM}",
          vb_b0(i4[7]), vb_c0(i4[7], end="…"),
          f"{H['Catukkanayasaṃsandanaṃ']}.")
    # ------------------------------------------------ Lakkhaṇayuttikathā
    d.head(4, H["Lakkhaṇayuttikathā"], "5-1-12-0")
    lk = chain(["người có điều kiện", "người không có điều kiện", "người do điều kiện tạo thành",
                "người không do điều kiện tạo thành", "người trường tồn", "người không trường tồn",
                "người có dấu hiệu", "người không có dấu hiệu"])
    d.seg("5-53", f"{Q(P_UP)} {AMANTA} Có phải {lk} không? {NA_HEVAM} {SAMKHITTAM}")
    d.seg("5-54", f"{vbq} Có phải {lk} không? {NA_HEVAM} {SAMKHITTAM}", f"{H['Lakkhaṇayuttikathā']}.")
    # ------------------------------------------------ Vacanasodhanaṃ
    d.head(4, H["Vacanasodhanaṃ"], "5-1-13-0")
    KEHICI = "trong một số trường hợp"
    for sid, pred, subj, neg in (("5-55", UP, f"cái {UP}", NUP),                       # upalabbhati
                                 ("5-56", f"là {SACCIKATTHA}", SACCIKATTHA, f"không phải là {SACCIKATTHA}"),
                                 ("5-57", "hiện hữu", "cái hiện hữu", "không hiện hữu"),         # vijjamāno
                                 ("5-58", "thực sự hiện hữu", "cái thực sự hiện hữu", "không thực sự hiện hữu"),
                                 ("5-59", "tồn tại", "cái tồn tại", "không tồn tại")):          # atthi / natthi
        d.seg(sid,
              f"Người {pred}, vậy {subj} có phải là người không? "
              f"Người {pred}, còn {subj} thì {KEHICI} là người, {KEHICI} không phải là người. "
              f"Có phải người {KEHICI} {pred}, {KEHICI} {neg} không? {NA_HEVAM_PE}")
    d.seg("5-60",
          f"Người tồn tại, vậy có phải cái tồn tại không phải tất cả đều là người không? {AMANTA_PE} "
          f"người không tồn tại, vậy có phải cái không tồn tại không phải tất cả đều là người không? "
          f"{NA_HEVAM} {SAMKHITTAM}",
          f"{H['Vacanasodhanaṃ']}.")
    # ------------------------------------------------ Paññattānuyogo
    d.head(4, H["Paññattānuyogo"], "5-1-14-0")
    RD, AD, KD = "ở cõi hình sắc", "ở cõi không hình sắc", "ở cõi dục lạc"
    d.seg("5-61", f"{Q(RD + ', người có hình sắc')} {AMANTA} {Q(KD + ', người có dục lạc')} {NA_HEVAM_PE}")
    d.seg("5-62", f"{Q(RD + ', chúng sinh có hình sắc')} {AMANTA} {Q(KD + ', chúng sinh có dục lạc')} {NA_HEVAM_PE}")
    d.seg("5-63", f"{Q(AD + ', người không có hình sắc')} {AMANTA} {Q(KD + ', người có dục lạc')} {NA_HEVAM_PE}")
    d.seg("5-64", f"{Q(AD + ', chúng sinh không có hình sắc')} {AMANTA} {Q(KD + ', chúng sinh có dục lạc')} {NA_HEVAM_PE}")
    cuto = "có ai đó chết ở cõi hình sắc rồi tái sinh vào cõi không hình sắc"
    d.seg("5-65", f"{Q(RD + ', người có hình sắc, ' + AD + ', người không có hình sắc, và ' + cuto)} {AMANTA} "
                  f"{Q('người có hình sắc đã bị cắt đứt, người không có hình sắc đã sinh ra')} {NA_HEVAM_PE}")
    d.seg("5-66", f"{Q(RD + ', chúng sinh có hình sắc, ' + AD + ', chúng sinh không có hình sắc, và ' + cuto)} "
                  f"{AMANTA} {Q('chúng sinh có hình sắc đã bị cắt đứt, chúng sinh không có hình sắc đã sinh ra')} "
                  f"{NA_HEVAM_PE}")
    same = "khi xem {x} là một không thể tách rời, đó chính là cùng một thứ, cùng một nghĩa, như nhau, ngang nhau, cùng một loại"
    pk = f"gọi là thân hay gọi là thân thể, gọi là thân thể hay gọi là thân, {same.format(x='thân')}"
    pj = f"gọi là người hay gọi là linh hồn, gọi là linh hồn hay gọi là người, {same.format(x='người')}"
    kp = "thân là khác, người là khác"
    d.seg("5-67", f"{Q(pk)} {AMANTA} {Q(pj)} {AMANTA} {Q(kp)} {AMANTA} {Q(ANNAM_JIVAM)} {NA_HEVAM}",
          line_b("n", f"{pk}, {pj}, {kp}", ANNAM_JIVAM), line_c(f"{pk}, {pj}, {kp}", ANNAM_JIVAM, end="…"))
    d.seg("5-68",
          f"{Q(pk)} {AMANTA} {Q(VB)} {AMANTA} {Q(kp)} {NA_HEVAM}",
          f"{AJANAHI['p']} Nếu {pk}, {VB}, {TENA_VATA} “{kp}”. "
          f"{YAM_TATTHA} – “nên nói – ‘{pk}, {VB_IN2}’, nhưng không nên nói – ‘{kp}’”.",
          f"Còn nếu không nên nói – “{kp}”, {NO_CA_VATA} “{pk}, {VB_IN}”. "
          f"{YAM_TATTHA} – “nên nói – ‘{pk}, {VB_IN2}’, nhưng không nên nói – ‘{kp}’”. {SAMKHITTAM}",
          f"{H['Paññattānuyogo']}.")
    # ------------------------------------------------ Gatianuyogo
    d.head(4, H["Gatianuyogo"], "5-1-15-0")
    PS = Q(f"người {SANDH}")
    d.seg("5-69", f"{PS} {AMANTA} {Q('người ấy ' + SANDH)} {NA_HEVAM_PE}")
    d.seg("5-70", f"{PS} {AMANTA} {Q('một người khác ' + SANDH)} {NA_HEVAM_PE}")
    d.seg("5-71", f"{PS} {AMANTA} {Q('cả người ấy lẫn người khác ' + SANDH)} {NA_HEVAM_PE}")
    neva = "người ấy không trôi lăn, người khác cũng không trôi lăn"
    d.seg("5-72", f"{PS} {AMANTA} {Q(neva + ' ' + LOKA)} {NA_HEVAM_PE}")
    d.seg("5-73", f"{PS} {AMANTA} "
                  f"{Q('người ấy trôi lăn, một người khác trôi lăn, cả người ấy lẫn người khác trôi lăn, ' + neva + ' ' + LOKA)} "
                  f"{NA_HEVAM_PE}")
    d.seg("5-74",
          f"{NA_VATTABBAM_Q('người ' + SANDH)} {AMANTA} {NANU_VUTTAM}",
          "“Người ấy, sau khi trôi lăn tối đa bảy lần;",
          "Đi đến tận cùng của khổ đau, nhờ diệt tận mọi xiềng xích” "
          "[Tương Ưng Bộ Kinh 2.133; Kinh Phật Thuyết Như Vậy 24, cũng có trong Kinh Phật Thuyết Như Vậy].",
          f"{ATTHEVA} {AMANTA} {TENA_HI('người ' + SANDH)}")
    d.seg("5-75",
          f"{NA_VATTABBAM_Q('người ' + SANDH)} {AMANTA} {NANU_VUTTAM} “Này các tỳ-khưu, vòng luân hồi này không có "
          f"khởi điểm có thể biết được [{VAR} (Ka.): anamataggāyaṃ]. Điểm khởi đầu không được nhận ra, đối với các "
          f"chúng sinh có vô minh làm chướng ngại, có khao khát làm xiềng xích, đang trôi lăn, đang luân chuyển” "
          f"[Tương Ưng Bộ Kinh 2.124]! {ATTHEVA} {AMANTA} {TENA_HI('người ' + SANDH)}")
    SV = f"chính người ấy {SANDH}"
    d.seg("5-76", f"{PS} {AMANTA} {Q(SV)} {NA_HEVAM_PE}")

    def became(a, bs):
        return f"có ai đó là {a} rồi " + ", ".join(f"trở thành {b}" for b in bs)

    d.seg("5-77", f"{Q(SV)} {AMANTA} {Q(became(MANUSSO, [DEVO]))} {AMANTA} "
                  f"{Q(f'chính {MANUSSO} ấy là {DEVO} ấy')} {NA_HEVAM_PE}")
    SACE_HI = ("Bởi vì nếu chính người ấy, sau khi chết ở đây, trôi lăn sang thế gian khác mà không khác, thì như vậy "
               "sẽ không có sự chết, và việc sát hại sinh mạng cũng không được tìm thấy. Nghiệp tồn tại, quả của "
               "nghiệp tồn tại, quả của các nghiệp đã làm tồn tại; khi thiện và bất thiện đang trổ quả, nói rằng "
               "chính người ấy trôi lăn là sai.")

    def manussa_line(b):
        return (f"{Q(f'chính {MANUSSO} ấy là {b} ấy')} {AMANTA} Là {MANUSSO} rồi trở thành {b}, là {b} rồi trở thành "
                f"{MANUSSO}; người từng là {MANUSSO} là khác, {b} là khác; nói rằng chính người từng là {MANUSSO} "
                f"ấy trôi lăn là sai…")

    d.seg("5-78", manussa_line(DEVO), SACE_HI)
    beasts = ["dạ-xoa", "ngạ quỷ", "chúng sinh địa ngục", "loài súc sinh", "lạc đà", "bò", "lừa", "heo",
              f"trâu [{SPELL} (Sī., Syā., Kaṃ., Pī.): mahiso]"]
    d.seg("5-79", f"{Q(SV)} {AMANTA} {Q(became(MANUSSO, beasts))} {AMANTA} "
                  f"{Q(f'chính {MANUSSO} ấy là con trâu ấy')} {NA_HEVAM_PE}")
    d.seg("5-80", manussa_line("con trâu"), SACE_HI)
    d.seg("5-81", f"{Q(SV)} {AMANTA} {Q(became(KHATTIYO, [BRAHMANO]))} {AMANTA} "
                  f"{Q(f'chính {KHATTIYO} ấy là {BRAHMANO} ấy')} {NA_HEVAM_PE}")
    for sid, a, bs, last in (("5-82", KHATTIYO, [VESSO, SUDDO], SUDDO),
                             ("5-83", BRAHMANO, [VESSO, SUDDO, KHATTIYO], KHATTIYO),
                             ("5-84", VESSO, [SUDDO, KHATTIYO, BRAHMANO], BRAHMANO),
                             ("5-85", SUDDO, [KHATTIYO, BRAHMANO, VESSO], VESSO)):
        d.seg(sid, f"{Q(became(a, bs))} {AMANTA} {Q(f'chính {a} ấy là {last} ấy')} {NA_HEVAM_PE}")
    maimed = ("người bị chặt tay vẫn là người bị chặt tay, người bị chặt chân vẫn là người bị chặt chân, người bị "
              "chặt tay chân vẫn là người bị chặt tay chân, người bị cắt tai… người bị cắt mũi… người bị cắt tai mũi… "
              "người bị chặt ngón tay… người bị chặt ngón cái… người bị đứt gân… người có bàn tay co quắp… người có "
              "bàn tay dính ngón… người bị bệnh phong… người bị mụn nhọt… người bị bệnh bạch biến… người bị bệnh "
              "lao… người bị động kinh… lạc đà… bò… lừa… heo… trâu vẫn là trâu")
    d.seg("5-86", f"{Q(SV)} {AMANTA} {Q(maimed)} {NA_HEVAM_PE}")
    sota = "bậc vào dòng, sau khi chết ở thế giới loài người và tái sinh vào thế giới chư thiên, ở đó vẫn là bậc vào dòng"
    d.seg("5-87",
          f"{NA_VATTABBAM_Q(SV)} {AMANTA} {NANU(sota)} {AMANTA}",
          hanci(sota, SV))
    sota_m = "bậc vào dòng, sau khi chết ở thế giới loài người và tái sinh vào thế giới chư thiên, ở đó cũng là con người"
    d.seg("5-88", f"{KATVA(sota, SV)} {AMANTA} Có phải vì cho rằng {sota_m} không? {NA_HEVAM_PE}")
    d.seg("5-89", f"{Q(SV)} {AMANTA} {Q('trôi lăn mà không khác, không mất đi')} {NA_HEVAM_PE}")
    d.seg("5-90", f"{Q('trôi lăn mà không khác, không mất đi')} {AMANTA} {Q(maimed)} {NA_HEVAM_PE}")

    def kh_line(first, x_q, x_last, ident):
        return (f"{first}{Q(x_q)} {NA_HEVAM_PE} {q(x_q)} {AMANTA} {Q(ident)} {NA_HEVAM_PE}")

    d.seg("5-91",
          kh_line(f"{Q(SV)} {AMANTA} ", "trôi lăn cùng với vật chất", None, TAM_JIVAM),
          f"Có phải cùng với cảm giác… cùng với tri giác… cùng với các tạo tác… trôi lăn cùng với thức không? "
          f"{NA_HEVAM_PE} {q('trôi lăn cùng với thức')} {AMANTA} {Q(TAM_JIVAM)} {NA_HEVAM_PE}")
    d.seg("5-92",
          kh_line(f"{Q(SV)} {AMANTA} ", "trôi lăn mà không có vật chất", None, ANNAM_JIVAM),
          f"Có phải không có cảm giác… không có tri giác… không có các tạo tác… trôi lăn mà không có thức không? "
          f"{NA_HEVAM_PE} {q('trôi lăn mà không có thức')} {AMANTA} {Q(ANNAM_JIVAM)} {NA_HEVAM_PE}")
    d.seg("5-93",
          kh_line(f"{Q(SV)} {AMANTA} ", f"{RUPA} trôi lăn", None, TAM_JIVAM),
          f"Có phải {VEDANA}… {SANNA}… {SANKHARA}… {VINNANA} trôi lăn không? "
          f"{NA_HEVAM_PE} {q(VINNANA + ' trôi lăn')} {AMANTA} {Q(TAM_JIVAM)} {NA_HEVAM_PE}")
    d.seg("5-94",
          kh_line(f"{Q(SV)} {AMANTA} ", f"{RUPA} không trôi lăn", None, ANNAM_JIVAM),
          f"Có phải {VEDANA}… {SANNA}… {SANKHARA}… {VINNANA} không trôi lăn không? "
          f"{NA_HEVAM_PE} {q(VINNANA + ' không trôi lăn')} {AMANTA} {Q(ANNAM_JIVAM)} {NA_HEVAM} {SAMKHITTAM}.",
          "Khi các khối đang tan rã, nếu người ấy cũng tan rã;",
          "Thì thành quan điểm về sự đoạn diệt, điều mà Đức Phật đã loại bỏ.",
          "Khi các khối đang tan rã, nếu người ấy không tan rã;",
          "Thì người là trường tồn, hoàn toàn ngang bằng với Niết-bàn.",
          f"{H['Gatianuyogo']}.")
    # ------------------------------------------------ Upādāpaññattānuyogo
    d.head(4, H["Upādāpaññattānuyogo"], "5-1-16-0")
    d.seg("5-95", f"{Q(upd(RUPA))} {AMANTA} {Q(f'{RUPA} là {ANICCA}')} Đúng vậy? "
                  f"{Q(f'người cũng là {ANICCA}')} {NA_HEVAM_PE}")
    khs = chain([f"dựa vào {VEDANA}", f"dựa vào {SANNA}", f"dựa vào {SANKHARA}", upd(VINNANA)])
    d.seg("5-96", f"Có phải {khs} không? {AMANTA} {Q(f'{VINNANA} là {ANICCA}')} {AMANTA} "
                  f"{Q(f'người cũng là {ANICCA}')} {NA_HEVAM_PE}")
    cols = chain([f"dựa vào {RUPA} màu vàng", f"dựa vào {RUPA} màu đỏ", f"dựa vào {RUPA} màu trắng",
                  f"dựa vào {RUPA} thấy được", f"dựa vào {RUPA} không thấy được", f"dựa vào {RUPA} có tính va chạm",
                  upd(f"{RUPA} không có tính va chạm", "người không có tính va chạm")])
    d.seg("5-97", f"{Q(upd(RUPA))} {AMANTA} {Q(upd(RUPA + ' màu xanh', 'người màu xanh'))} {NA_HEVAM_PE} "
                  f"{q(cols)} {NA_HEVAM_PE}")
    GOOD = ("có kết quả, có quả trổ, có kết quả đáng mong muốn, có kết quả đáng yêu mến, có kết quả đáng ưa thích, "
            "có kết quả không pha tạp, đưa đến sự dễ chịu, có quả trổ dễ chịu")
    BAD = ("có kết quả, có quả trổ, có kết quả không đáng mong muốn, có kết quả không đáng yêu mến, có kết quả "
           "không đáng ưa thích, có kết quả pha tạp, đưa đến sự khó chịu, có quả trổ khó chịu")
    ETH = {"k": ("thiện", GOOD), "a": ("bất thiện", BAD), "b": ("không xác định về mặt đạo đức", None)}

    def eth_line(first, base, e):
        name, qual = ETH[e]
        x = upd(f"{base} {name}", f"người {name}")
        qual_b = f"là {ANICCA}" if qual is None else qual
        return (f"{first}{Q(x)} {NA_HEVAM_PE} {q(x)} {AMANTA} {Q(f'{base} {name} {qual_b}')} {AMANTA} "
                f"{Q(f'người {name} cũng {qual_b}')} {NA_HEVAM_PE}")

    for sid, e in (("5-98", "k"), ("5-99", "a"), ("5-100", "b")):
        d.seg(sid, eth_line(f"{Q(upd(VEDANA))} {AMANTA} ", VEDANA, e))
    khs3 = chain([f"dựa vào {SANNA}", f"dựa vào {SANKHARA}", upd(VINNANA)])
    d.seg("5-101", eth_line(f"Có phải {khs3} không? {AMANTA} ", VINNANA, "k"))
    d.seg("5-102", eth_line(f"{Q(upd(VINNANA))} {AMANTA} ", VINNANA, "a"))
    d.seg("5-103", eth_line(f"{Q(upd(VINNANA))} {AMANTA} ", VINNANA, "b"))

    def called(base, name, last_pe=True):
        return (f"dựa vào {base} mà nên gọi là “{name}”", f"khi {base} đã chấm dứt, nên gọi là “{name} đã chấm dứt”")

    c1, c2 = called("mắt", "người có mắt")
    m1, m2 = called("ý", "người có ý")
    d.seg("5-104", f"{Q(c1)} {AMANTA} {Q(c2)} {NA_HEVAM_PE} "
                   f"{q(chain(['dựa vào tai', 'dựa vào mũi', 'dựa vào lưỡi', 'dựa vào thân', m1]))} {AMANTA} "
                   f"{Q(m2)} {NA_HEVAM}")
    for sid, lst, sep in (("5-105", MICCHA, ". "), ("5-106", SAMMA, "… ")):
        f1, f2 = called(lst[0], f"người có {lst[0]}")
        l1, l2 = called(lst[-1], f"người có {lst[-1]}")
        mid = chain([f"dựa vào {x}" for x in lst[1:-1]] + [l1])
        qmid = Q(mid) if sep == ". " else q(mid)
        tail = f"{NA_HEVAM}" if sep == ". " else f"{NA_HEVAM_PE}"
        d.seg(sid, f"{Q(f1)} {AMANTA} {Q(f2)} {NA_HEVAM[:-1]}{sep}{qmid} {AMANTA} {Q(l2)} {tail}")
    d.seg("5-107",
          f"{Q(upd(chain([f'{RUPA}', f'dựa vào {VEDANA}'], ', ')))} {AMANTA} "
          f"{Q(upd(f'hai {KHANDHA}', 'hai người'))} {NA_HEVAM_PE} "
          f"{q(upd(', '.join([RUPA, 'dựa vào ' + VEDANA, 'dựa vào ' + SANNA, 'dựa vào ' + SANKHARA, 'dựa vào ' + VINNANA])))} "
          f"{AMANTA} {Q(upd(f'năm {KHANDHA}', 'năm người'))} {NA_HEVAM_PE}")
    for sid, first, second, last, kind, nn in (
            ("5-108", AYATANA[0], AYATANA[1], AYATANA[-1], "lĩnh vực nhận biết", "mười hai"),
            ("5-109", DHATU[0], DHATU[1], DHATU[-1], "yếu tố", "mười tám"),
            ("5-110", INDRIYA[0], INDRIYA[1], ANNATAVI, "năng lực", None)):
        if nn is None:
            many = upd(f"hai mươi hai [{VAR} (?): bāvīsatiyā] {kind}", "hai mươi hai người")
        else:
            many = upd(f"{nn} {kind}", f"{nn} người")
        d.seg(sid,
              f"{Q(upd(f'{first}, dựa vào {second}'))} {AMANTA} {Q(upd(f'hai {kind}', 'hai người'))} {NA_HEVAM_PE} "
              f"có phải dựa vào {first}, dựa vào {second}… {upd(last)} không? {AMANTA} {Q(many)} {NA_HEVAM_PE}")
    eka = "sự hiện hữu gồm một khối"
    d.seg("5-111",
          f"{Q(upd(eka, 'một người'))} {AMANTA} {Q(upd('sự hiện hữu gồm bốn khối', 'bốn người'))} {NA_HEVAM_PE} "
          f"{q(upd(eka, 'một người'))} {AMANTA} {Q(upd('sự hiện hữu gồm năm khối', 'năm người'))} {NA_HEVAM_PE} "
          f"{q('trong ' + eka + ' chỉ có một người')} {AMANTA} "
          f"{Q(f'trong sự hiện hữu gồm bốn khối chỉ có bốn [{VAR} (?): cattāro] người')} {NA_HEVAM_PE} "
          f"{q('trong ' + eka + ' chỉ có một người')} {AMANTA} "
          f"{Q('trong sự hiện hữu gồm năm khối chỉ có năm người')} {NA_HEVAM_PE}")
    yatha_r = f"giống như {upd('cái cây', 'bóng râm')}"
    ev = f"cũng vậy, {upd(RUPA)}"
    d.seg("5-112",
          f"{Q(f'{yatha_r}, {ev}')} ( ) [(āmantā) (?) ba lượt kế tiếp cũng vậy] "
          f"{Q(f'{yatha_r}, cây là vô thường, bóng râm cũng vô thường, {ev}, vật chất cũng vô thường, người cũng vô thường')} "
          f"{NA_HEVAM_PE} "
          f"{q(f'{yatha_r}, cây là khác, bóng râm là khác, {ev}, {ar}')} {NA_HEVAM_PE}")
    for sid, place, who, a1, a2 in (("5-113", "làng", "dân làng", "làng", "dân làng"),
                                     ("5-114", "đất nước", "vua", "đất nước", "vua")):
        ya = f"giống như {upd(place, who)}"
        d.seg(sid, f"{Q(f'{ya}, {ev}')} {Q(f'{ya}, {a1} là khác, {a2} là khác, {ev}, {ar}')} {NA_HEVAM_PE}")
    nig = "giống như cái cùm không phải là người bị cùm, ai có cái cùm thì người ấy là người bị cùm"
    rv2 = "cũng vậy, vật chất không phải là người có vật chất, ai có vật chất thì người ấy là người có vật chất"
    d.seg("5-115", f"{Q(f'{nig}, {rv2}')} "
                   f"{Q(f'{nig}, cái cùm là khác, người bị cùm là khác, {rv2}, vật chất là khác, người có vật chất là khác')} "
                   f"{NA_HEVAM_PE}")
    d2 = "khi tâm thứ hai đã sinh khởi"
    so_anno = "người ấy hay người khác"
    kum = "bé trai hay bé gái"
    d.seg("5-116",
          f"{Q('với mỗi tâm đều có sự định danh người')} {AMANTA} "
          f"{Q('với mỗi tâm, người sinh ra, già đi, qua đời, chết đi, tái sinh')} {NA_HEVAM_PE} "
          f"{q(f'{d2}, không nên nói là {so_anno}')} {AMANTA} {Q(f'{d2}, không nên nói là {kum}')} {VATTABBAM}",
          f"{AJANAHI['n']} Nếu {d2}, không nên nói – “{so_anno}”, {TENA_VATA} “{d2}, không nên nói – ‘{kum}’”. "
          f"{YAM_TATTHA} – “nên nói – ‘{d2}, không nên nói – {so_anno}, {d2}, nên nói – {kum}’”.",
          f"Hoặc nếu {d2}, nên nói – “{kum}”, {TENA_VATA} “{d2}, nên nói – ‘{so_anno}’”. "
          f"{YAM_TATTHA} – “nên nói – ‘{d2}, không nên nói – {so_anno}, {d2}, nên nói – {kum}’”.")
    dm = "vị trời hay con người"
    six = "phụ nữ hay đàn ông hay người tại gia hay người xuất gia hay vị trời hay con người"
    d.seg("5-117",
          f"Có phải {d2}, không nên nói – “{so_anno}” không? {AMANTA} "
          f"Có phải {d2}, không nên nói – “{six}” không? {VATTABBAM}",
          f"{AJANAHI['n']} Nếu {d2}, không nên nói – “{so_anno}”, {TENA_VATA} “{d2}, không nên nói – ‘{dm}’”. "
          f"{YAM_TATTHA} – “nên nói – ‘{d2}, không nên nói – {so_anno}, {d2}, nên nói – {dm}’”.",
          f"Hoặc nếu {d2}, nên nói – “{dm}”, {TENA_VATA} “{d2}, nên nói – ‘{so_anno}’”. "
          f"{YAM_TATTHA} – “nên nói – ‘{d2}, không nên nói – {so_anno}, {d2}, nên nói – {dm}’”…")

    def sees(v, neg=False):
        n_ = "không " if neg else ""
        return f"ai {n_}{v}, {n_}{v} cái gì, {n_}{v} nhờ cái gì, người ấy {n_}{v}, {n_}{v} cái ấy, {n_}{v} nhờ cái ấy"

    d.seg("5-118", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU(sees('thấy'))} {AMANTA} "
                   f"Nếu {sees('thấy')}; {TENA_VATA} “{P_UP}”.")
    d.seg("5-119", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} Chẳng phải ai nghe… ai ngửi… ai nếm… ai chạm… "
                   f"{sees('nhận biết')} sao? {AMANTA} Nếu {sees('nhận biết')}; {TENA_VATA} “{P_UP}”.")
    d.seg("5-120",
          f"{Q(P_UP)} {AMANTA} {NANU(sees('thấy', True))} {AMANTA} Nếu {sees('thấy', True)}; {NO_CA_VATA} “{P_UP}”.",
          f"{Q(P_UP)} {AMANTA} Chẳng phải ai không nghe… ai không ngửi… ai không nếm… ai không chạm… "
          f"{sees('nhận biết', True)} sao? {AMANTA} Nếu {sees('nhận biết', True)}; {NO_CA_VATA} “{P_UP}”.")
    passami = ("Này các tỳ-khưu, bằng thiên nhãn thanh tịnh, vượt quá mắt người, Ta thấy chúng sinh đang chết đi, "
               "đang tái sinh, thấp kém, ưu việt, đẹp đẽ, xấu xí, ở cõi tốt lành, ở cõi xấu, và hiểu rõ các chúng sinh "
               "đi theo nghiệp của mình")
    d.seg("5-121", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU_VUTTAM} “{passami}” [Trung Bộ Kinh 1.213, hơi khác một chút]! "
                   f"{ATTHEVA} {AMANTA} {TENA_HI(P_UP)}")
    dibba = "Đức Thế Tôn, bằng thiên nhãn thanh tịnh, vượt quá mắt người, thấy hình sắc hay thấy người?"
    d.seg("5-122",
          f"{KATVA(f'{VUTTAM} “{passami[0].lower() + passami[1:]}”', P_UP, teneva=True)} {AMANTA} {dibba} "
          f"Thấy hình sắc. {Q('hình sắc là người, hình sắc chết đi, hình sắc tái sinh, hình sắc đi theo nghiệp của mình')} "
          f"{NA_HEVAM}",
          f"{dibba} Thấy người. {Q('người là hình sắc, lĩnh vực hình sắc, yếu tố hình sắc, màu xanh, màu vàng, màu đỏ, màu trắng, được nhận biết bằng mắt, va chạm vào mắt, đi vào phạm vi của mắt')} "
          f"{NA_HEVAM}",
          f"{dibba} Thấy cả hai. Có phải cả hai đều là hình sắc, lĩnh vực hình sắc, yếu tố hình sắc, cả hai đều màu "
          f"xanh, cả hai đều màu vàng, cả hai đều màu đỏ, cả hai đều màu trắng, cả hai đều được nhận biết bằng mắt, "
          f"cả hai đều va chạm vào mắt, cả hai đều đi vào phạm vi của mắt, cả hai đều chết đi, cả hai đều tái sinh, "
          f"cả hai đều đi theo nghiệp của mình không? {NA_HEVAM}",
          f"{H['Upādāpaññattānuyogo']}.")
    # ------------------------------------------------ Purisakārānuyogo
    d.head(4, H["Purisakārānuyogo"], "5-1-17-0")
    kk = f"người làm và người khiến làm {KPK}"
    kpk_up = f"{KPK} {UP}"
    cond = f"nếu {kpk_up}, thì {kk} {UP}"
    TASSA = ("đối với từng người như vậy, không có sự đi đến tận cùng của khổ đau, không có sự cắt đứt vòng luân "
             "chuyển, không có sự nhập Niết-bàn trọn vẹn không còn bám víu")
    d.seg("5-123", f"{Q(kpk_up)} {AMANTA} {Q(f'{kk} {UP}')} {NA_HEVAM_PE}")
    d.seg("5-124", f"{Q(cond)} {AMANTA} {Q(f'người làm và người khiến làm ra người ấy {UP}')} {NA_HEVAM_PE}")
    d.seg("5-125", f"{Q(f'người làm và người khiến làm ra người ấy {UP}')} {AMANTA} {Q(TASSA)} {NA_HEVAM_PE}")
    things = [("người", "người"), ("Niết-bàn", "Niết-bàn"), ("đại địa", "đại địa"), ("đại dương", "đại dương"),
              ("núi Tu-di, vua của các ngọn núi,", "núi Tu-di, vua của các ngọn núi,"), ("nước", "nước"),
              ("lửa", "lửa"), ("gió", "gió"), ("cỏ, gỗ và cây rừng", "cỏ, gỗ và cây rừng")]
    for i, (a, b) in enumerate(things):
        d.seg(f"5-{126 + i}", f"{Q(cond)} {AMANTA} "
                              f"{Q(f'nếu {a} {UP}, thì người làm và người khiến làm ra {b} {UP}')} {NA_HEVAM_PE}")
    d.seg("5-135", f"{Q(cond)} {AMANTA} {Q(f'{KPK} là khác, {kk} là khác')} {NA_HEVAM_PE}")

    def experience_block(start, x, xp, xp_name, cond_x, list_pe_first=True):
        """vipāka / dibbaṃ sukhaṃ / … blocks; returns list of (lines) for 7 segments."""
        segs = []
        segs.append([f"{Q(f'{x} {UP}')} {AMANTA} {Q(f'{xp} {UP}')} {NA_HEVAM_PE}"])
        segs.append([f"{Q(cond_x)} {AMANTA} {Q(f'người cảm nhận người ấy {UP}')} {NA_HEVAM_PE}"])
        segs.append([f"{Q(f'người cảm nhận người ấy {UP}')} {AMANTA} {Q(TASSA)} {NA_HEVAM_PE}"])
        segs.append([f"{Q(cond_x)} {AMANTA} {Q(f'nếu người {UP}, thì người cảm nhận người {UP}')} {NA_HEVAM_PE}"])
        segs.append([f"{Q(cond_x)} {AMANTA} {Q(f'nếu Niết-bàn {UP}, thì người cảm nhận Niết-bàn {UP}')} {NA_HEVAM_PE}"])
        sep0 = "…" if list_pe_first else "…"
        segs.append([f"{Q(cond_x)} {AMANTA} Có phải nếu đại địa {UP}… nếu đại dương {UP}… nếu núi Tu-di, vua của "
                     f"các ngọn núi, {UP}… nếu nước {UP}… nếu lửa {UP}… nếu gió {UP}… nếu cỏ, gỗ và cây rừng {UP}, "
                     f"thì người cảm nhận cỏ, gỗ và cây rừng {UP} không? {NA_HEVAM_PE}"])
        segs.append([f"{Q(f'{x} là khác, {xp} là khác')} {NA_HEVAM_PE}"])
        return segs

    blocks = [
        (136, f"quả của {KPK}", f"người cảm nhận quả của {KPK}"),
        (143, "hạnh phúc cõi trời", "người cảm nhận hạnh phúc cõi trời"),
        (150, "hạnh phúc cõi người", "người cảm nhận hạnh phúc cõi người"),
        (157, "khổ đau ở cõi khổ", "người cảm nhận khổ đau ở cõi khổ"),
        (164, "khổ đau ở địa ngục", "người cảm nhận khổ đau ở địa ngục"),
    ]
    for start, x, xp in blocks:
        cond_x = f"nếu {x} {UP}, thì {xp} {UP}"
        segs = experience_block(start, x, xp, None, cond_x)
        # the 7th: "Cond? Āmantā. Añño X, añño Xp?"
        segs[6] = [f"{Q(cond_x)} {AMANTA} {Q(f'{x} là khác, {xp} là khác')} {NA_HEVAM_PE}"]
        if start == 164:   # nerayika: the first two segments are one (two lines), ^5-164
            segs = [[segs[0][0].replace(f"{NA_HEVAM_PE}", NA_HEVAM), segs[1][0]]] + segs[2:]
        for i, lines in enumerate(segs):
            d.seg(f"5-{start + i}", *lines)
    kkv = f"người làm, người khiến làm, người cảm nhận quả của {KPK}"
    cond_v = f"nếu {kpk_up}, thì {kkv} {UP}"
    s1, s2 = "người ấy làm, người ấy cảm nhận", "một người làm, một người khác cảm nhận"
    s3 = "cả người ấy lẫn người khác cùng làm, cả người ấy lẫn người khác cùng cảm nhận"
    s4 = "người ấy không làm, người ấy không cảm nhận, người khác không làm, người khác không cảm nhận"
    SD = "sự dễ chịu và sự khó chịu"
    t1, t2 = f"{SD} do tự mình làm ra", f"{SD} do người khác làm ra"
    t3 = f"{SD} vừa do tự mình làm ra vừa do người khác làm ra"
    t4 = f"{SD} không do tự mình làm ra, không do người khác làm ra, tình cờ sinh khởi"
    for i, (s, t) in enumerate(((s1, t1), (s2, t2), (s3, t3), (s4, t4))):
        d.seg(f"5-{170 + 2 * i}", f"{Q(cond_v)} {AMANTA} {Q(s)} {NA_HEVAM_PE}")
        d.seg(f"5-{171 + 2 * i}", f"{Q(s)} {AMANTA} {Q(t)} {NA_HEVAM_PE}")
    s_all = f"{s1}, {s2}, {s3}, {s4}"
    t_all = (f"{SD} do tự mình làm ra, {SD} do người khác làm ra, {SD} vừa do tự mình làm ra vừa do người khác làm "
             f"ra, {SD} không do tự mình làm ra, không do người khác làm ra, tình cờ sinh khởi")
    d.seg("5-178", f"{Q(cond_v)} {AMANTA} {Q(s_all)} {NA_HEVAM_PE}")
    d.seg("5-179", f"{Q(s_all)} {AMANTA} {Q(t_all)} {NA_HEVAM_PE}")
    AT = "tồn tại"
    for base, (x, xp, maker) in ((180, ("nghiệp", "người tạo nghiệp", "người tạo ra")),
                                 (187, ("quả", "người cảm nhận quả", "người cảm nhận"))):
        cnd = f"nếu {x} {AT}, thì {xp} {AT}"
        seg_lines = [
            [f"{Q(f'{x} {AT}')} {AMANTA} {Q(f'{xp} {AT}')} {NA_HEVAM_PE}"],
            [f"{Q(cnd)} {AMANTA} {Q(f'{maker} người ấy {AT}')} {NA_HEVAM_PE}"],
            [f"{Q(f'{maker} người ấy {AT}')} {AMANTA} {Q(TASSA)} {NA_HEVAM_PE}"],
            [f"{Q(cnd)} {AMANTA} {Q(f'nếu người {AT}, thì {maker} người {AT}')} {NA_HEVAM_PE}"],
            [f"{Q(cnd)} {AMANTA} {Q(f'nếu Niết-bàn {AT}, thì {maker} Niết-bàn {AT}')} {NA_HEVAM_PE}"],
            [f"{Q(cnd)} {AMANTA} Có phải nếu đại địa {AT}… nếu đại dương {AT}… nếu núi Tu-di, vua của các ngọn núi, "
             f"{AT}… nếu nước {AT}… nếu lửa {AT}… nếu gió {AT}… nếu cỏ, gỗ và cây rừng {AT}, thì {maker} cỏ, gỗ "
             f"và cây rừng {AT} không? {NA_HEVAM_PE}"],
            [f"{Q(cnd)} {AMANTA} {Q(f'{x} là khác, {xp} là khác')} {NA_HEVAM_PE}"],
        ]
        if base == 187:   # ^5-189 = segments 3 + 4 on one line; the last closes the Purisakārānuyogo
            seg_lines = [seg_lines[0], seg_lines[1],
                         [seg_lines[2][0] + " " + seg_lines[3][0][0].lower() + seg_lines[3][0][1:]],
                         seg_lines[4], seg_lines[5],
                         [seg_lines[6][0].replace(f"{NA_HEVAM_PE}", f"{NA_HEVAM} {SAMKHITTAM}"),
                          f"{H['Purisakārānuyogo']}.", KALYANAVAGGO_PATHAMO]]
        for i, lines in enumerate(seg_lines):
            d.seg(f"5-{base + i}", *lines)
    # ------------------------------------------------ Abhiññānuyogo
    d.head(4, H["Abhiññānuyogo"], "5-1-18-0")
    iddhi = "có ai đó thi triển thần thông"
    d.seg("5-193", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU(iddhi)} {AMANTA} {hanci(iddhi, P_UP)}")
    abh = ["nghe âm thanh bằng yếu tố tai thuộc cõi trời", "nhận biết tâm người khác", "nhớ lại các đời sống trước",
           "thấy hình sắc bằng thiên nhãn", "chứng nghiệm sự diệt tận các ô nhiễm"]
    d.seg("5-194", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU('có ai đó ' + chain(abh))} {AMANTA} "
                   f"{hanci('có ai đó ' + abh[-1], P_UP)}")
    SVP = "thì chính người ấy là người"
    NSP = "thì người ấy không phải là người"
    d.seg("5-195", f"{KATVA(iddhi, P_UP)} {AMANTA} Ai thi triển thần thông {SVP} sao? "
                   f"Ai không thi triển thần thông {NSP} sao? {NA_HEVAM_PE}")
    d.seg("5-196", f"Ai {chain(abh, '… ai ')} {SVP} sao? Ai không {abh[-1]} {NSP} sao? {NA_HEVAM_PE}",
          f"{H['Abhiññānuyogo']}.")
    # ------------------------------------------------ 15-18. Ñātakānuyogādi
    d.head(4, f"15-18. {H['Ñātakānuyogādi']}", "5-1-19-0")
    d.seg("5-197", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU('người mẹ tồn tại')} {AMANTA} "
                   f"{hanci('người mẹ tồn tại', P_UP)}")
    kin = ["người cha", "anh em trai", "chị em gái", KHATTIYO, BRAHMANO, VESSO, SUDDO, GAHATTHO, PABBAJITO, DEVO,
           MANUSSO]
    d.seg("5-198", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU(chain([f'{k} tồn tại' for k in kin]))} {AMANTA} "
                   f"{hanci(f'{MANUSSO} tồn tại', P_UP)}")
    kin2 = ["cha", "anh em trai", "chị em gái", KHATTIYO, BRAHMANO, VESSO, SUDDO, GAHATTHO, PABBAJITO, DEVO]
    nap = "có ai đó không phải là người rồi trở thành người"
    pan = "có ai đó là người rồi trở thành không phải là người"
    d.seg("5-199", f"{KATVA('người mẹ tồn tại', P_UP)} {AMANTA} {Q('có ai đó không phải là mẹ rồi trở thành mẹ')} "
                   f"{AMANTA} {Q(nap)} {NA_HEVAM_PE} có phải có ai đó "
                   f"{chain([f'không phải là {k} rồi' for k in kin2])}… không phải là {MANUSSO} rồi trở thành "
                   f"{MANUSSO} không? {AMANTA} {Q(nap)} {NA_HEVAM_PE}")
    d.seg("5-200", f"{KATVA('người mẹ tồn tại', P_UP)} {AMANTA} {Q('có ai đó là mẹ rồi trở thành không phải là mẹ')} "
                   f"{AMANTA} {Q(pan)} {NA_HEVAM_PE}",
          f"Có phải có ai đó {chain([f'là {k} rồi' for k in kin2])}… là {MANUSSO} rồi trở thành không phải là "
          f"{MANUSSO} không? {AMANTA} {Q(pan)} {NA_HEVAM_PE}")
    # ------------------------------------------------ Paṭivedhānuyogo
    d.head(4, H["Paṭivedhānuyogo"], "5-1-20-0")
    d.seg("5-201", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU('bậc vào dòng tồn tại')} {AMANTA} "
                   f"{hanci('bậc vào dòng tồn tại', P_UP)}")
    ariya = ["bậc trở lại một lần", "bậc không trở lại", "bậc A-la-hán", "người được giải thoát theo cả hai cách",
             "người được giải thoát nhờ trí tuệ", f"người chứng nghiệm bằng thân [{SPELL} (Syā.): kāyasakkhī]",
             "người đạt đến quan điểm", "người được giải thoát nhờ niềm tin", "người đi theo Giáo Pháp",
             "người đi theo niềm tin"]
    d.seg("5-202", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU(chain([f'{a} tồn tại' for a in ariya]))} {AMANTA}",
          hanci("người đi theo niềm tin tồn tại", P_UP))
    d.seg("5-203", f"{KATVA('bậc vào dòng tồn tại', P_UP)} {AMANTA} "
                   f"{Q('có ai đó không phải là bậc vào dòng rồi trở thành bậc vào dòng')} {AMANTA} {Q(nap)} {NA_HEVAM_PE}")
    ariya2 = [a.replace(f" [{SPELL} (Syā.): kāyasakkhī]", "") for a in ariya]
    d.seg("5-204", f"Có phải có ai đó {chain([f'không phải là {a} rồi' for a in ariya2[:-1]])}… không phải là "
                   f"{ariya2[-1]} rồi trở thành {ariya2[-1]} không? {AMANTA} {Q(nap)} {NA_HEVAM_PE}")
    d.seg("5-205", f"{KATVA('bậc vào dòng tồn tại', P_UP)} {AMANTA} "
                   f"{Q('có ai đó là bậc vào dòng rồi trở thành không phải là bậc vào dòng')} {AMANTA} {Q(pan)} {NA_HEVAM_PE}",
          f"Có phải có ai đó là bậc trở lại một lần rồi… là bậc không trở lại rồi trở thành không phải là bậc không "
          f"trở lại không? {AMANTA} {Q(pan)} {NA_HEVAM_PE}",
          f"{H['Paṭivedhānuyogo']}.")
    # ------------------------------------------------ Saṅghānuyogo
    d.head(4, H["Saṅghānuyogo"], "5-1-21-0")
    py = "bốn đôi người, tám hạng người"
    d.seg("5-206", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU(py + ' tồn tại')} {AMANTA} {hanci(py + ' tồn tại', P_UP)}")
    bp = "xuất hiện nhờ sự xuất hiện của Đức Phật"
    d.seg("5-207", f"{KATVA(py + ' tồn tại', P_UP)} {AMANTA} {Q(py + ' ' + bp)} {AMANTA} {Q('người ' + bp)} {NA_HEVAM_PE}",
          f"{Q('người ' + bp)} {AMANTA} "
          f"{Q('khi Đức Phật Thế Tôn đã nhập Niết-bàn trọn vẹn, người bị đoạn diệt, người không tồn tại')} {NA_HEVAM_PE}",
          f"{H['Saṅghānuyogo']}.")
    # ------------------------------------------------ Saccikaṭṭhasabhāgānuyogo
    d.head(4, H["Saccikaṭṭhasabhāgānuyogo"], "5-1-22-0")
    SK, ASK = "do điều kiện tạo thành", "không do điều kiện tạo thành"
    ns = f"người không phải {SK} cũng không phải {ASK}"
    d.seg("5-208", f"{Q(P_UP)} {AMANTA} {Q('người ' + SK)} {NA_HEVAM_PE} {q('người ' + ASK)} {NA_HEVAM_PE} "
                   f"{q(ns)} {NA_HEVAM}")
    koti = f"ngoài cái {SK} và cái {ASK}, còn có một phạm trù thứ ba khác"
    d.seg("5-209", f"{Q(ns)} {AMANTA} {Q(koti)} {NA_HEVAM_PE}")
    d.seg("5-210", f"{Q(koti)} {AMANTA} {NANU_VUTTAM} “Này các tỳ-khưu, có hai yếu tố này. Hai yếu tố nào? Yếu tố {SK} "
                   f"và yếu tố {ASK}. Này các tỳ-khưu, đây là hai yếu tố” [Trung Bộ Kinh 1.125, chỉ khác ở lời xưng hô]! "
                   f"{ATTHEVA} {AMANTA} {TENA_HI_NA(koti)}")
    d.seg("5-211", f"{Q(ns)} {AMANTA} {Q(f'cái {SK} là khác, cái {ASK} là khác, người là khác')} {NA_HEVAM_PE}")
    d.seg("5-212", f"{Q(f'các khối {SK}, Niết-bàn {ASK}, {ns}')} {AMANTA} "
                   f"{Q('các khối là khác, Niết-bàn là khác, người là khác')} {NA_HEVAM_PE}")
    d.seg("5-213", f"{Q(f'{RUPA} {SK}, Niết-bàn {ASK}, {ns}')} {AMANTA} "
                   f"{Q(f'{RUPA} là khác, Niết-bàn là khác, người là khác')} {NA_HEVAM} "
                   f"Có phải {VEDANA}… {SANNA}… {SANKHARA}… {VINNANA} {SK}, Niết-bàn {ASK}, {ns} không? {AMANTA} "
                   f"{Q(f'{VINNANA} là khác, Niết-bàn là khác, người là khác')} {NA_HEVAM_PE}")
    lak = ("sự sinh khởi của người được nhận ra, sự suy tàn được nhận ra, sự đổi khác của cái đang duy trì được "
           "nhận ra")
    lak_n = ("sự sinh khởi của người không được nhận ra, sự suy tàn không được nhận ra, sự đổi khác của cái đang "
             "duy trì không được nhận ra")
    d.seg("5-214", f"{Q(lak)} {AMANTA} {Q('người ' + SK)} {NA_HEVAM_PE} {VUTTAM} “Này các tỳ-khưu, cái {SK} có ba "
                   f"đặc tính này của cái {SK}. Này các tỳ-khưu, đối với các hiện tượng {SK} "
                   f"[{VAR} (Tăng Chi Bộ Kinh 3.47): katamāni tīṇi], sự sinh khởi được nhận ra, sự suy tàn được nhận "
                   f"ra, sự đổi khác của những cái đang duy trì được nhận ra” [Tăng Chi Bộ Kinh 3.47]. "
                   f"{cap(lak)}; vậy thì người {SK}.")
    d.seg("5-215", f"{Q(lak_n)} {AMANTA} {Q('người ' + ASK)} {NA_HEVAM_PE} {VUTTAM} “Này các tỳ-khưu, cái {ASK} có ba "
                   f"đặc tính này của cái {ASK}. Này các tỳ-khưu, đối với các hiện tượng {ASK}, sự sinh khởi không "
                   f"được nhận ra, sự suy tàn không được nhận ra, sự đổi khác của những cái đang duy trì không được "
                   f"nhận ra” [Tăng Chi Bộ Kinh 3.48]. {cap(lak_n)}; vậy thì người {ASK}.")
    pnb = "người đã nhập Niết-bàn trọn vẹn"
    d.seg("5-216", f"{cap(pnb)} còn tồn tại hay không còn tồn tại? Còn tồn tại. {Q(pnb + ' là trường tồn')} "
                   f"{NA_HEVAM_PE} không còn tồn tại. {Q(pnb + ' đã bị đoạn diệt')} {NA_HEVAM_PE}")
    d.seg("5-217", f"Người nương vào cái gì mà duy trì? Nương vào sự hiện hữu mà duy trì. "
                   f"{Q('sự hiện hữu là ' + ANICCA)} {AMANTA} {Q('người cũng là ' + ANICCA)} {NA_HEVAM_PE}")

    def feel(v, know=True):
        k = "hiểu rõ" if know else "không hiểu rõ"
        return f"khi đang cảm nhận cảm giác {v}, {k} “tôi đang cảm nhận cảm giác {v}”"

    SU, DU, AD = "dễ chịu", "khó chịu", "không khó chịu cũng không dễ chịu"
    d.seg("5-218", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU('có ai đó, ' + feel(SU))} {AMANTA} "
                   f"{hanci('có ai đó, ' + feel(SU), P_UP)}")
    d.seg("5-219", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} Chẳng phải có ai đó, khi đang cảm nhận cảm giác {DU}… "
                   f"{feel(AD)} sao? {AMANTA} {hanci('có ai đó, ' + feel(AD), P_UP)}")
    d.seg("5-220", f"{KATVA('có ai đó, ' + feel(SU), P_UP)} {AMANTA} Ai, {feel(SU)}, {SVP}; ai, {feel(SU, False)}, "
                   f"{NSP} sao? {NA_HEVAM_PE}",
          f"Ai, khi đang cảm nhận cảm giác {DU}… ai, {feel(AD)}, {SVP}; ai, {feel(AD, False)}, {NSP} sao? {NA_HEVAM_PE}")
    d.seg("5-221", f"{KATVA('có ai đó, ' + feel(SU), P_UP)} {AMANTA} "
                   f"{Q(f'cảm giác {SU} là khác, người {feel(SU)} là khác')} {NA_HEVAM_PE} cảm giác {DU} là khác… "
                   f"{q(f'cảm giác {AD} là khác, người {feel(AD)} là khác')} {NA_HEVAM_PE}")
    kaye = "đối với thân sống quán sát thân"
    dham = "đối với các hiện tượng sống quán sát các hiện tượng"
    d.seg("5-222", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU('có ai đó ' + kaye)} {AMANTA} {hanci('có ai đó ' + kaye, P_UP)}")
    d.seg("5-223", f"{NA_VATTABBAM_Q(P_UP)} {AMANTA} {NANU('có ai đó đối với các cảm giác… đối với tâm… ' + dham)} "
                   f"{AMANTA} {hanci('có ai đó ' + dham, P_UP)}")
    d.seg("5-224", f"{KATVA('có ai đó ' + kaye, P_UP)} {AMANTA} Ai {kaye} {SVP}; ai không {kaye} {NSP} sao? {NA_HEVAM_PE}",
          f"Ai đối với các cảm giác… đối với tâm… {dham} {SVP}; ai không {dham} {NSP} sao? {NA_HEVAM_PE}")
    d.seg("5-225", f"{KATVA('có ai đó ' + kaye, P_UP)} {AMANTA} {Q('thân là khác, người ' + kaye + ' là khác')} "
                   f"{NA_HEVAM_PE} cảm giác là khác… tâm là khác… "
                   f"{q('các hiện tượng là khác, người ' + dham + ' là khác')} {NA_HEVAM_PE}")
    d.seg("5-226", f"{Q(P_UP)} {AMANTA} {NANU_VUTTAM}",
          "“Hãy nhìn thế gian là trống rỗng, này Mô-gha-ra-gia, luôn luôn tỉnh thức;",
          f"Nhổ bỏ quan điểm về tự ngã [{SPELL} (Syā.): ohacca; (Ka.): uhacca], như thế có thể vượt qua sự chết;",
          "Người nhìn thế gian như vậy, vua của sự chết không thấy được” "
          "[Kinh Tập 1125; Tiểu Nghĩa Thích 88, phần giải thích câu hỏi của thanh niên Mô-gha-ra-gia].",
          f"{ATTHEVA} {AMANTA} {TENA_HI_NA(P_UP)}")
    for sid, a, b, ans in (("5-227", "nhìn cùng với vật chất", "nhìn không có vật chất", "Nhìn cùng với vật chất."),
                           ("5-228", "nhìn khi ở bên trong", "nhìn sau khi ra bên ngoài", "Nhìn khi ở bên trong.")):
        d.seg(sid, f"{Q('người nhìn')} {AMANTA} {cap(a)} hay {b}? {ans} {Q(TAM_JIVAM)} {NA_HEVAM_PE} "
                   f"nếu {b}, thì có phải {ANNAM_JIVAM} không? {NA_HEVAM_PE}")
    sacca = f"{AMANTA} {BHAGAVA_SACCAVADI} {AMANTA}"
    d.seg("5-229", f"{NA_VATTABBAM_Q(P_UP)} {sacca} {VB}. {ATTHEVA} {AMANTA} {TENA_HI(P_UP)}")
    eka_p = ("Này các tỳ-khưu, có một người, khi sinh ra trên thế gian, sinh ra vì lợi ích của nhiều người, vì hạnh "
             "phúc của nhiều người, vì lòng thương xót thế gian, vì sự tốt đẹp, lợi ích và hạnh phúc của chư thiên "
             "và loài người")
    d.seg("5-230", f"{NA_VATTABBAM_Q(P_UP)} {sacca} {VUTTAM} “{eka_p}” [Tăng Chi Bộ Kinh 1.162-169]. "
                   f"{ATTHEVA} {AMANTA} {TENA_HI(P_UP)}")
    d.seg("5-231", f"{Q(P_UP)} {sacca} {VUTTAM} “tất cả các hiện tượng đều không phải là tự ngã” "
                   f"[Trung Bộ Kinh 1.356; Kinh Pháp Cú 279, trong Kinh Pháp Cú]. {ATTHEVA} {AMANTA} {TENA_HI_NA(P_UP)}")
    kacc = (f"Vị ấy không nghi ngờ, không hoài nghi rằng khi sinh khởi, chỉ có khổ đau sinh khởi; khi chấm dứt, chỉ "
            f"có khổ đau [{VAR} (Tương Ưng Bộ Kinh 2.15): dukkhaṃ] chấm dứt; nơi vị ấy, về điều này, có sự hiểu biết "
            f"không dựa vào người khác. Này Ca-chiên-diên, đến mức ấy là có quan điểm đúng đắn")
    d.seg("5-232", f"{Q(P_UP)} {sacca} {VUTTAM} “{kacc}” [Tương Ưng Bộ Kinh 2.15]. {ATTHEVA} {AMANTA} {TENA_HI_NA(P_UP)}")
    d.seg("5-233", f"{Q(P_UP)} {AMANTA} Chẳng phải tỳ-khưu-ni Va-gi-ra đã nói với Ma vương ác độc thế này sao –",
          "“Vì sao ngươi cho rằng có chúng sinh, này Ma vương, ngươi đã mắc kẹt trong quan điểm chăng;",
          "Đây chỉ là một đống tạo tác thuần túy, ở đây chúng sinh không được tìm thấy.",
          f"“Như khi các bộ phận được ráp lại [{VAR} (nhiều bản): yathāpi], thì có từ gọi là cỗ xe;",
          f"Cũng vậy, khi có các khối, thì có sự quy ước gọi là chúng sinh [{VAR} (Syā., Kaṃ.): sammati].",
          "“Quả thật, chỉ có khổ đau sinh ra, khổ đau duy trì rồi tan biến;",
          "Ngoài khổ đau, không gì sinh ra, ngoài khổ đau, không gì chấm dứt” [Tương Ưng Bộ Kinh 1.171].",
          f"{ATTHEVA} {AMANTA} {TENA_HI_NA(P_UP)}")
    TR = "thế gian là trống rỗng"
    ATT = "tự ngã hay những gì thuộc về tự ngã"

    def sunna(x):
        return f"{x} trống rỗng"

    eye = [sunna("các hình sắc"), sunna("thức qua mắt"), sunna("sự tiếp xúc của mắt")]
    rest = [sunna("tai"), sunna("các âm thanh"), sunna("mũi"), sunna("các mùi"), sunna("lưỡi"), sunna("các vị"),
            sunna("thân"), sunna("các vật xúc chạm"), sunna("ý"), sunna("các đối tượng của ý"), sunna("ý thức"),
            sunna("sự tiếp xúc của ý")]
    ved = ("cảm nhận nào sinh khởi do sự tiếp xúc của {x} làm điều kiện, dễ chịu, khó chịu, hay không khó chịu cũng "
           "không dễ chịu, điều ấy cũng trống rỗng " + ATT)
    ananda = (f"Chẳng phải tôn giả A-nan đã nói với Đức Thế Tôn thế này sao – “‘{TR}, {TR}’, bạch Thế Tôn, người ta "
              f"nói như vậy. Bạch Thế Tôn, đến mức nào thì gọi là ‘{TR}’?” “Này A-nan, vì trống rỗng {ATT}, nên gọi "
              f"là ‘{TR}’. Và này A-nan, cái gì trống rỗng {ATT}? Này A-nan, mắt trống rỗng {ATT}, "
              f"{eye[0]}… {eye[1]}… {eye[2]}… {ved.format(x='mắt')}; {rest[0]}… {chain(rest[1:])}… "
              f"{ved.format(x='ý')}. Này A-nan, vì trống rỗng {ATT}, nên gọi là ‘{TR}’” [Tương Ưng Bộ Kinh 4.85].")
    d.seg("5-234", f"{Q(P_UP)} {AMANTA} {ananda} {ATTHEVA} {AMANTA} {TENA_HI_NA(P_UP)}")
    attani = (f"{VUTTAM} “Này các tỳ-khưu, khi có tự ngã, thì có phải sẽ có ‘cái thuộc về tự ngã của tôi’ không?” "
              f"“Bạch Thế Tôn, đúng như vậy”. “Này các tỳ-khưu, khi có cái thuộc về tự ngã, thì có phải sẽ có ‘tự ngã "
              f"của tôi’ không?” “Bạch Thế Tôn, đúng như vậy”. “Này các tỳ-khưu, khi tự ngã và cái thuộc về tự ngã "
              f"không được tìm thấy như là sự thật, như là điều chắc chắn [{VAR} (Trung Bộ Kinh 1.244): "
              f"anupalabbhamāne], thì chính nền tảng quan điểm này [{VAR} (Syā.): yamidaṃ; (Trung Bộ Kinh 1.244): "
              f"yampitaṃ], rằng thế gian ấy là tự ngã ấy, sau khi chết tôi sẽ là cái ấy, {NICCO_DHUVO}, tôi sẽ duy "
              f"trì y như vậy ngang bằng với sự vĩnh cửu – ‘này các tỳ-khưu, chẳng phải đây hoàn toàn là một giáo lý "
              f"ngu si trọn vẹn sao’?” “Bạch Thế Tôn, sao lại không phải, bạch Thế Tôn, đó hoàn toàn là một giáo lý "
              f"ngu si trọn vẹn” [Trung Bộ Kinh 1.244].")
    d.seg("5-235", f"{Q(P_UP)} {sacca} {attani} {ATTHEVA} {AMANTA} {TENA_HI_NA(P_UP)}")
    T1 = ("đề ra tự ngã như là sự thật, như là điều chắc chắn ngay trong đời này, và đề ra tự ngã như là sự thật, "
          "như là điều chắc chắn trong đời sau")
    T2 = ("đề ra tự ngã như là sự thật, như là điều chắc chắn ngay trong đời này, nhưng quả thật không đề ra tự ngã "
          "như là sự thật, như là điều chắc chắn trong đời sau")
    T3 = ("không đề ra tự ngã như là sự thật, như là điều chắc chắn ngay trong đời này, và không đề ra tự ngã như là "
          "sự thật, như là điều chắc chắn trong đời sau")
    d.seg("5-236",
          f"{Q(P_UP)} {sacca} {VUTTAM} “Này Seniya, có ba bậc đạo sư này đang có mặt, thực sự hiện hữu trên thế "
          f"gian. Ba bậc nào? Này Seniya, ở đời này, có bậc đạo sư {T1}.",
          f"“Lại nữa, này Seniya, ở đời này, có bậc đạo sư {T2}.",
          f"“Lại nữa, này Seniya, ở đời này, có bậc đạo sư {T3}.",
          f"“Trong số đó, này Seniya, bậc đạo sư nào {T1} – này Seniya, bậc đạo sư ấy được gọi là bậc đạo sư theo "
          f"học thuyết về sự trường tồn.",
          f"“Trong số đó, này Seniya, bậc đạo sư nào {T2} – này Seniya, bậc đạo sư ấy được gọi là bậc đạo sư theo "
          f"học thuyết về sự đoạn diệt.",
          f"“Trong số đó, này Seniya, bậc đạo sư nào {T3} – này Seniya, bậc đạo sư ấy được gọi là bậc Tự Giác Ngộ "
          f"Hoàn Toàn. Này Seniya, đây là ba bậc đạo sư đang có mặt, thực sự hiện hữu trên thế gian” "
          f"[Định danh các hạng người 131; trong Định danh các hạng người, giống nhau về ý nghĩa]. "
          f"{ATTHEVA} {AMANTA} {TENA_HI_NA(P_UP)}")
    d.seg("5-237", f"{Q(P_UP)} {sacca} {Q(VUTTAM + ' “hũ bơ lỏng”')} {AMANTA} "
                   f"{Q('có ai đó làm ra cái hũ bằng bơ lỏng')} {NA_HEVAM_PE} vậy thì không nên nói – “{P_UP}”.")
    kumbha = chain(["hũ dầu", "hũ mật ong", "hũ đường mía", "hũ sữa", "hũ nước", "đĩa nước uống", "chén nước uống",
                    "bát nước uống", "bữa ăn thường còn", "cháo bền vững"])
    d.seg("5-238",
          f"{Q(P_UP)} {sacca} {Q(VUTTAM + ' “' + kumbha + '”')} {AMANTA} "
          f"{Q('có thứ cháo nào ' + NICCO_DHUVO)} {NA_HEVAM_PE} {TENA_HI_NA(P_UP)} {SAMKHITTAM}",
          "Phần lặp lại của tám sự bác bỏ, sự trôi lăn, sự dựa vào;",
          "Với tâm là thứ năm, điều tốt, với thần thông và việc dẫn kinh là thứ tám.",
          f"{H['Saccikaṭṭhasabhāgānuyogo']}.",
          KATHA_END.format(x="người"))
    return d.text()


# ================================================================ line checks against the Pāli
FOREIGN = re.compile(r"[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶfjwzFJWZ]")
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def _strip(line):
    return ID.sub("", re.sub(r"\[[^\]]*\]", "", line))


def check_lines(pali_text, vi_text, name):
    pl = [l for l in pali_text.splitlines() if l.strip()]
    vl = [l for l in vi_text.splitlines() if l.strip()]
    probs, repaired = [], []
    if len(pl) != len(vl):
        probs.append(f"{name}: line count {len(pl)} vs {len(vl)}")
    for i, (p, v) in enumerate(zip(pl, vl), 1):
        pid, vid = re.search(r"\^([0-9A-Za-z-]+)\s*$", p), re.search(r"\^([0-9A-Za-z-]+)\s*$", v)
        if (pid and pid.group(1)) != (vid and vid.group(1)):
            probs.append(f"{name} line {i}: ID {pid and pid.group(1)} vs {vid and vid.group(1)}")
        dp = p.count("–") + p.count("—")
        dv = v.count("–") + v.count("—")
        if dp != dv:
            probs.append(f"{name} line {i} (^{vid and vid.group(1)}): dashes {dp} vs {dv}")
        sp, sv = _strip(p), _strip(v)
        qp = (sp.count('"'), sp.count("‘") + sp.count("’"))
        qv = (sv.count("“") + sv.count("”"), sv.count("‘") + sv.count("’"))
        if qp != qv:
            probs.append(f"{name} line {i}: quotes pali {qp} vs vi {qv}")
        if '"’' in p:
            repaired.append(i)
        if FOREIGN.search(sv):
            probs.append(f"{name} line {i}: foreign letter {FOREIGN.search(sv).group(0)!r}")
        if any(s in v for s in ("là là", ". .", "….", ".…", "?…", ",…", "  ", ":-", '"', "'", " ,", " .")):
            probs.append(f"{name} line {i}: bad sequence")
        if v != unicodedata.normalize("NFC", v):
            probs.append(f"{name} line {i}: not NFC")
    return probs, repaired


def main():
    check_cross_book()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    allprobs = []
    for name, builder in (("preamble.md", build_preamble), ("1-puggalakatha.md", build_ch1)):
        text = unicodedata.normalize("NFC", builder())
        probs, repaired = check_lines((PALI_DIR / name).read_text(encoding="utf-8"), text, name)
        allprobs += probs
        (OUT_DIR / name).write_bytes(text.encode("utf-8"))
        print(f"wrote {name}: {len([l for l in text.splitlines() if l.strip()])} lines; "
              f"Pāli lines with the odd closing order \"’ repaired to ’”: {len(repaired)}")
    for p in allprobs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not allprobs else f"{len(allprobs)} problems")
    sys.exit(1 if allprobs else 0)


if __name__ == "__main__":
    main()
