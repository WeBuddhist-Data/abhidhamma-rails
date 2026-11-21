"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 29, Ekavīsatimavaggo (^5-29-0 … ^5-891): eight
kathās (200-207) with the repeated "Ekavīsatimavaggo" sub-headings, the vagga close and the uddāna.

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/29-ekavisatimavaggo.md from the fixed
strings below, importing the approved sample builder READ-ONLY (frames Q, q, NANU, hanci, hanci_neg, na_vattabbam,
tena_hi, katha, katha_end, var …). Strings taken from pi-1 … pi-4 rails are asserted there (REUSED29); strings
shared with the finished pi-5 rails chapters are asserted in those chapter files (SHARED). The per-line dash /
quote / NFC / id checks of S.check_against_pali run before writing.
New recurring strings: notes-rails-29.md.

usage: python -I -X utf8 -B build_rails_29_vi.py          (writes the chapter and the adherence copy rails\\adh-29\\)
       python -I -X utf8 -B build_rails_29_vi.py --find <regex> [max_hits] [maxchars]
              (helper: the line of the finished pi-5 rails chapters 1-24 for a Pāli pattern; named files only)
"""
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402

NAME = "29-ekavisatimavaggo.md"
Q, q, NANU, PE, YES, NO, NO_PE = S.Q, S.q, S.NANU, S.PE, S.YES, S.NO, S.NO_PE

DONE = ["1-puggalakatha.md", "2-parihanikatha.md", "3-brahmacariyakatha.md", "4-jahatikatha.md",
        "5-sabbamatthitikatha.md", "6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md",
        "8-satipatthanakatha.md", "9-hevatthikatha.md", "10-dutiyavaggo.md", "11-tatiyavaggo.md",
        "12-catutthavaggo.md", "13-pancamavaggo.md", "14-chatthavaggo.md", "15-sattamavaggo.md",
        "16-atthamavaggo.md", "17-navamavaggo.md", "18-dasamavaggo.md", "19-ekadasamavaggo.md",
        "20-dvadasamavaggo.md", "21-terasamavaggo.md", "22-cuddasamavaggo.md", "23-pannarasamavaggo.md",
        "24-solasamavaggo.md"]


def nanu_l(x):                      # nanu Xti? (after …pe…, lower case)
    return f"chẳng phải {x} sao?"


# ---------------------------------------------------------------------------------------------------------------
# Shared vocabulary (termbase; pi-1 … pi-4; finished pi-5 chapters)
# ---------------------------------------------------------------------------------------------------------------
VAGGA = "Chương thứ hai mươi mốt"                                       # Ekavīsatimavaggo (termbase)
TASSUDDANAM = "Tóm tắt của chương này –"                                # Tassuddānaṃ – (ch9)

# kathā 1: sāsana
SAS = "giáo huấn"                                                        # sāsanaṃ (termbase)
TG = f"{SAS} của Như Lai"                                                # tathāgatassa sāsanaṃ (ch20 Như Lai)
T1A = f"{SAS} đã được làm mới"                                           # sāsanaṃ navaṃ kataṃ (kataṃ «đã được làm»)
T1B = f"có ai đó làm mới {TG}"                                           # atthi koci tathāgatassa sāsanaṃ navaṃ karoti
T1C = f"có thể làm mới lại {TG}"                                         # labbhā … puna navaṃ kātuṃ (ch19 labbhā)
SP = "các sự thiết lập tỉnh thức"                                        # satipaṭṭhānā (ch8)
BP = "nỗ lực đúng đắn… nền tảng thần thông… năng lực… sức mạnh… chi phần giác ngộ"   # sammappadhānā…pe… bojjhaṅgā
SAV = ("là đối tượng của ô nhiễm… là đối tượng của xiềng xích, là đối tượng của nút thắt, là đối tượng của dòng lũ, "
       "là đối tượng của ách, là đối tượng của chướng ngại, bị sự hiểu sai lệch nắm giữ, là đối tượng của sự bám víu… "
       "là đối tượng của phiền não")                                     # sāsavaṃ…pe… saṃyojaniyaṃ … saṃkilesikaṃ (ch4)
SAV_S = "là đối tượng của ô nhiễm… là đối tượng của phiền não"           # sāsavaṃ…pe… saṃkilesikaṃ
NSK = "không phải là đối tượng của phiền não"                            # asaṃkilesikaṃ (ch4 / ch8)
AK = "điều trước đây là bất thiện, sau đó"                               # pubbe akusalaṃ pacchā
PS = "điều trước đây"                                                    # pubbe (termbase «trước đây»)

# kathā 2: avivitta
PP = "người phàm phu"                                                    # puthujjano (termbase)
T2 = f"{PP} không tách khỏi các hiện tượng thuộc ba cõi"                 # tedhātukehi dhammehi avivitto (termbase)
T2K = f"{PP} không tách khỏi các nghiệp thuộc ba cõi"                    # tedhātukehi kammehi avivitto
L3 = "thuộc ba cõi"
CN = "chứng nhập và an trú"                                              # upasampajja viharati (pi-1)
JH1, JH4 = "tầng thiền thứ nhất", "tầng thiền thứ tư"                    # paṭhamaṃ / catutthaṃ jhānaṃ (pi-1)
AKASA = "lĩnh vực không gian vô tận"                                     # ākāsānañcāyatanaṃ (ch10)
NEVA = "lĩnh vực không phải tri giác cũng không phải không tri giác"     # nevasaññānāsaññāyatanaṃ (ch10)
KHANA = "vào khoảnh khắc"                                                # yasmiṃ khaṇe … tasmiṃ khaṇe (termbase khaṇe)
UPAGA = "nghiệp đi đến cõi hình sắc và cõi không hình sắc"               # rūpadhātuarūpadhātūpagaṃ kammaṃ (termbase)

# kathā 3: saṃyojana
CB = "khi chưa dứt bỏ"                                                   # appahāya (ch12)
T3 = f"có sự đạt đến trạng thái A-la-hán {CB} một xiềng xích nào đó"     # atthi kiñci saṃyojanaṃ appahāya arahattappatti
ARA = "bậc A-la-hán"                                                     # arahā (pi-4)
Q8 = ["tham đắm", "sân hận", "si mê", "kiêu mạn", "gièm pha", "ganh đua", "tuyệt vọng", "phiền não"]
#   (sa- / ni-) rāgo dosa moha māna makkha paḷāsa upāyāsa kilesa (termbase; pi-4 «người có tham đắm … có kiêu mạn»)
SAR = f"{ARA} " + ", ".join(f"có {x}" for x in Q8)
NIR = f"{ARA} " + ", ".join(f"không có {x}" for x in Q8)
NIR_S = f"{ARA} không có {Q8[0]}{PE} không có {Q8[-1]}"

# kathā 4: iddhi
T4 = "có thần thông theo ý định của chư Phật hay của các đệ tử"          # atthi adhippāyaiddhi buddhānaṃ vā sāvakānaṃ vā
MONG = "Mong"                                                            # 3rd-person imperative / mā wish (pi-2 «Mong …»)
PIL = "tôn giả Pi-lin-đa-vác-cha"                                        # āyasmā pilindavaccho (termbase)
KING = "cung điện của vua xứ Ma-kiệt-đà Sê-ni-gia Tần-bà-sa-la"         # rañño māgadhassa seniyassa bimbisārassa pāsādaṃ
CIT_PARA = "Các tội bị trục xuất"                                        # pārā. (termbase pārājika «tội bị trục xuất»)
CIT_MV = "Đại Phẩm"                                                      # mahāva. (ch2 / ch10)

# kathā 5: buddha
T5 = "chư Phật có sự thấp kém và vượt trội so với chư Phật"             # atthi buddhānaṃ buddhehi hīnātirekatā (termbase)
XV = "xét về"                                                            # -to (in respect of)
B5 = (f"{XV} nỗ lực đúng đắn… nền tảng thần thông… năng lực… sức mạnh… chi phần giác ngộ… sự làm chủ… "
      "sự hiểu biết và thấy rõ về sự toàn tri")                          # sammappadhānato…pe… sabbaññutañāṇadassanato

# kathā 6: sabbadisā
BU = "Đức Phật"                                                          # buddho (termbase)
TT = "tồn tại"                                                           # tiṭṭhati / tiṭṭhanti (termbase buddho / buddhā tiṭṭhati)
T6 = f"chư Phật {TT} ở tất cả các phương"                                # sabbā disā buddhā tiṭṭhanti


def loc(d):                         # X-āya disāya buddho tiṭṭhati
    return f"{BU} {TT} ở phương {d}"


KIN = ("Đức Thế Tôn ấy tên là gì, thuộc giai cấp nào, thuộc họ nào, cha mẹ của Đức Thế Tôn ấy tên là gì, "
       "cặp đệ tử chính của Đức Thế Tôn ấy tên là gì, người thị giả của Đức Thế Tôn ấy tên là gì, "
       "mặc y phục như thế nào, mang bình bát như thế nào, ở làng, hay thị trấn, hay thành phố, hay vương quốc, "
       "hay xứ nào?")                                                    # Kinnāmo so bhagavā … janapade vāti?
KIN_S = "Đức Thế Tôn ấy tên là gì… hay xứ nào?"                          # Kinnāmo so bhagavā…pe… janapade vāti?
HEAV = ["Tứ Đại Thiên Vương", "Ba Mươi Ba", "Dạ Ma", "Đâu Suất", "Hóa Lạc", "Tha Hóa Tự Tại", "Phạm Thiên"]
#   cātumahārājike … paranimmitavasavattiyā (ch10 god names), brahmaloke «cõi Phạm Thiên» (ch4 / ch10)

# kathās 7-8: niyata
CD = "cố định"                                                           # niyata (termbase / APPROVED)
MI, SA = f"{CD} theo hướng sai lầm", f"{CD} theo hướng đúng đắn"         # micchatta- / sammattaniyata (pi-1)
AN = f"nhóm không {CD}"                                                  # aniyato rāsi (termbase rāsi «nhóm»)
RASI3 = f"nhóm {MI}, nhóm {SA}, {AN}"
VR = f"Đức Thế Tôn đã nói đến ba nhóm – {RASI3}"                         # tayo rāsī vuttā bhagavatā – …
DH = f"tất cả các hiện tượng đều {CD}"                                  # sabbe dhammā niyatā
KM = f"tất cả các nghiệp đều {CD}"                                      # sabbe kammā niyatā
R7 = f"vật chất {CD} theo nghĩa vật chất"                                # rūpaṃ rūpaṭṭhena niyataṃ (aṭṭhena «nghĩa»)
V7 = f"thức {CD} theo nghĩa thức"                                        # viññāṇaṃ viññāṇaṭṭhena niyataṃ
VSS = "cảm giác… tri giác… các tạo tác…"                                 # vedanā…pe… saññā…pe… saṅkhārā…pe…
DV, UV, AV = ("được cảm nhận ngay trong đời này", "được cảm nhận khi tái sinh",
              "được cảm nhận trong các đời kế tiếp")                     # diṭṭhadhamma- / upapajja- / aparāpariyavedanīyaṃ
DN = f"nghiệp {DV} {CD} theo nghĩa {DV}"
AN8 = f"nghiệp {AV} {CD} theo nghĩa {AV}"

KATHA = {1: SAS, 2: "sự không tách khỏi", 3: "xiềng xích", 4: "thần thông", 5: BU, 6: "tất cả các phương",
         7: "các hiện tượng", 8: "nghiệp"}
#   Sāsana-, Avivitta-, Saṃyojana-, Iddhi- (termbase heading), Buddha- (termbase), Sabbadisā-, Dhamma- (termbase
#   heading), Kammakathā (termbase heading; ch20 «Bàn về nghiệp»)
UDDANA = (f"{S.cap(T1A)}, {T1B}, {T1C}, {T2}, {T3}, {T4}, {T5}, {T6}, {DH}, {KM}.")

REUSED29 = [  # (Pāli, Vietnamese, book)
    ("paṭhamaṃ jhānaṃ upasampajja viharati", f"{CN} {JH1}", "1"),
    ("catutthaṃ jhānaṃ upasampajja viharati", f"{CN} {JH4}", "1"),
    ("micchattaniyatā dhammā", f"các hiện tượng {MI}", "1"),
    ("sammattaniyatā dhammā", f"các hiện tượng {SA}", "1"),
    ("aniyatā dhammā", "các hiện tượng không cố định", "1"),
    ("Tikamātikā", "Ma trận bộ ba", "1"),
    ("sarāgo, sadoso, samoho, samāno", "người có tham đắm, người có sân hận, người có si mê, người có kiêu mạn", "4"),
    ("vimuttiñāṇadassana", "sự hiểu biết và thấy rõ về", "4"),
    ("'… maṃ jano jānātū'ti (3rd-person imperative)", "“Mong người ta biết", "2"),
    ("arahā", ARA, "4"),
]

SHARED = [  # (Pāli, Vietnamese, finished pi-5 rails chapter)
    ("Tassuddānaṃ –", TASSUDDANAM, "9-hevatthikatha.md"),
    ("sāsavo saṃyojaniyo…pe… saṃkilesiyo", "là đối tượng của ô nhiễm, là đối tượng của xiềng xích… "
     "là đối tượng của phiền não", "4-jahatikatha.md"),
    ("anāsavo … aparāmaṭṭho anupādāniyo asaṃkilesiyo", "là đối tượng của chướng ngại, không bị sự hiểu sai lệch "
     "nắm giữ, không phải là đối tượng của sự bám víu, không phải là đối tượng của phiền não", "4-jahatikatha.md"),
    ("puthujjano", PP, "4-jahatikatha.md"),
    ("satipaṭṭhānā", SP, "8-satipatthanakatha.md"),
    ("satipaṭṭhānaṃ… sammappadhānaṃ… iddhipādo… indriyaṃ… balaṃ… bojjhaṅgo",
     "sự thiết lập tỉnh thức… " + BP, "12-catutthavaggo.md"),
    ("cīvara-piṇḍapāta-senāsana-gilānapaccayabhesajjaparikkhāra",
     "y phục, đồ ăn khất thực, chỗ ở, thuốc men và vật dụng chữa bệnh", "10-dutiyavaggo.md"),
    ("ākāsānañcāyatanaṃ … nevasaññānāsaññāyatanaṃ", f"{AKASA}… lĩnh vực thức vô tận… lĩnh vực không có gì cả… {NEVA}",
     "10-dutiyavaggo.md"),
    ("sakkāyadiṭṭhi", "quan điểm về tự ngã", "2-parihanikatha.md"),
    ("sīlabbataparāmāsa", "sự hiểu sai lệch về giới hạnh và nghi thức", "3-brahmacariyakatha.md"),
    ("gihisaṃyojanaṃ appahāya", "khi chưa dứt bỏ xiềng xích", "12-catutthavaggo.md"),
    ("rāgaṃ … dosaṃ … mohaṃ … anottappaṃ (pajahati)",
     "dứt bỏ sự tham đắm, dứt bỏ sự sân hận, dứt bỏ sự si mê, dứt bỏ sự không biết ghê sợ tội lỗi",
     "12-catutthavaggo.md"),
    ("vicikicchā", "sự hoài nghi", "2-parihanikatha.md"),
    ("uppanno phasso mā nirujjhi", "sự tiếp xúc đã sinh khởi đừng chấm dứt", "19-ekadasamavaggo.md"),
    ("rūpaṃ niccaṃ hotu", "vật chất thường còn", "19-ekadasamavaggo.md"),
    ("Jātidhammā sattā mā jāyiṃsu … maraṇadhammā sattā mā mīyiṃsu",
     "các chúng sinh có bản chất phải lão hóa đừng lão hóa… "
     "các chúng sinh có bản chất phải bệnh đừng bệnh… các chúng sinh có bản chất phải chết đừng chết",
     "19-ekadasamavaggo.md"),
    ("Jātidhammā sattā mā jāyiṃsu", "các chúng sinh có bản chất phải sinh đừng sinh ra", "19-ekadasamavaggo.md"),
    ("mahāva. (citation)", f"[{CIT_MV} ", "2-parihanikatha.md"),
    ("pattadhāraṇā / kāsāvadhāraṇā", "sự mặc y cà-sa, sự mang bình bát", "3-brahmacariyakatha.md"),
    ("sāvakayugaṃ", "cặp đệ tử chính", "3-brahmacariyakatha.md"),
    ("cātumahārājikānaṃ … paranimmitavasavattīnaṃ devānaṃ",
     "chư thiên Tứ Đại Thiên Vương… chư thiên Ba Mươi Ba… chư thiên Dạ Ma… chư thiên Đâu Suất… chư thiên Hóa Lạc… "
     "chư thiên Tha Hóa Tự Tại", "10-dutiyavaggo.md"),
    ("brahmaloke", "ở cõi Phạm Thiên", "10-dutiyavaggo.md"),
    ("kenaṭṭhena", "theo nghĩa nào", "3-brahmacariyakatha.md"),
    ("Micchattaniyato / sammattaniyato", f"người {MI} bước vào sự cố định theo hướng đúng đắn, người {SA}",
     "21-terasamavaggo.md"),
    ("tathāgatassa", "của Như Lai", "20-dvadasamavaggo.md"),
    ("Kammakathā", S.katha("nghiệp"), "20-dvadasamavaggo.md"),
    ("Nanu āyasmā X …", "Chẳng phải tôn giả", "5-sabbamatthitikatha.md"),
    ("labbhā iddhiyā paggahetuṃ", "Có phải có thể nhờ thần thông", "19-ekadasamavaggo.md"),
    ("Arahā … jānāti / passati", f"{ARA} phải được người khác dẫn dắt", "10-dutiyavaggo.md"),
    ("Tena hi Xti…pe….", "Vậy thì năm loại thức có sự chú hướng…", "18-dasamavaggo.md"),
    ("dukkhassantakaroti [ma. ni. 2.186]? (question word after the citation)", "[Trung Bộ Kinh 2.186] không?",
     "12-catutthavaggo.md"),
]


def check_strings():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8")
                                                       for p in sorted(d.glob("*.md")))).lower()
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED29 if unicodedata.normalize("NFC", v).lower() not in texts[b]]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    bad = []
    for p, v, f in SHARED:
        t = unicodedata.normalize("NFC", (S.OUT_DIR / f).read_text(encoding="utf-8"))
        if unicodedata.normalize("NFC", v) not in t:
            bad.append((p, v, f))
    assert not bad, "shared strings not found in their chapters: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def heading(i, level, text):
        add(i, "#" * level + " " + text)

    def sub(n, num):
        heading(f"5-29-{n}-0", 4, VAGGA)
        heading(f"5-29-{n}-1-0", 5, f"({num}) {n}. {S.katha(KATHA[n])}")

    heading("5-29-0", 3, VAGGA)

    # ---- (200) 1. Sāsanakathā ------------------------------------------------------------------------------------
    heading("5-29-1-0", 4, f"(200) 1. {S.katha(KATHA[1])}")
    add("5-878",
        f"{Q(T1A)} {YES} {Q(f'{SP} đã được làm mới')} {NO_PE} {q(T1A)} {YES} {Q(f'{BP} đã được làm mới')} {NO_PE} "
        f"{q(f'{AK} đã được làm thành thiện')} {NO_PE} {q(f'{PS} {SAV}, sau đó đã được làm thành {NSK}')} {NO_PE}",
        f"{Q(T1B)} {YES} {Q(f'có ai đó làm mới {SP}')} {NO_PE} {q(f'có ai đó làm mới {BP}')} {NO_PE} "
        f"{q(f'có ai đó làm cho {AK} thành thiện')} {NO_PE} "
        f"{q(f'có ai đó làm cho {PS} {SAV_S}, sau đó thành {NSK}')} {NO_PE}",
        f"{Q(T1C)} {YES} {Q(f'có thể làm mới lại {SP}')} {NO_PE} {q(f'có thể làm mới lại {BP}')} {NO_PE} "
        f"{q(f'có thể làm cho {AK} thành thiện')} {NO_PE} "
        f"{q(f'có thể làm cho {PS} {SAV_S}, sau đó thành {NSK}')} {NO_PE}",
        S.katha_end(KATHA[1]))

    # ---- (201) 2. Avivittakathā ----------------------------------------------------------------------------------
    sub(2, 201)
    L14 = (f"{PP} không tách khỏi sự tiếp xúc {L3}{PE} cảm giác {L3}{PE} tri giác{PE} chủ ý{PE} tâm{PE} niềm tin{PE} "
           f"sự tinh tấn{PE} sự tỉnh thức{PE} sự định tâm{PE} trí tuệ {L3}")
    A15 = f"{KHANA} {PP} cho y phục, thì {KHANA} ấy {CN} {JH1}{PE} {CN} {AKASA}"
    B15 = (f"{KHANA} {PP} cho đồ ăn khất thực{PE} cho chỗ ở{PE} cho thuốc men và vật dụng chữa bệnh, thì {KHANA} ấy "
           f"{CN} {JH4}{PE} {CN} {NEVA}")
    add("5-879",
        f"{Q(T2)} {YES} {Q(L14)} {NO_PE}",
        f"{Q(T2K)} {YES} {Q(A15)} {NO_PE} {q(B15)} {NO_PE}")
    add("5-880",
        f"{S.na_vattabbam(T2K)} {YES} {Q(f'{UPAGA} của {PP} đã được hiểu biết trọn vẹn')} {NO} "
        f"{S.tena_hi(T2K)[:-1]}{PE}",
        S.katha_end(KATHA[2]))

    # ---- (202) 3. Saṃyojanakathā ---------------------------------------------------------------------------------
    sub(3, 202)
    L24 = (f"có sự đạt đến trạng thái A-la-hán {CB} một quan điểm về tự ngã nào đó{PE} {CB} sự hoài nghi{PE} "
           f"{CB} sự hiểu sai lệch về giới hạnh và nghi thức{PE} {CB} sự tham đắm{PE} {CB} sự sân hận{PE} "
           f"{CB} sự si mê{PE} {CB} sự không biết ghê sợ tội lỗi")
    add("5-881",
        f"{Q(T3)} {YES} {Q(L24)} {NO_PE}",
        f"{Q(T3)} {YES} {Q(SAR)} {NO_PE} {nanu_l(NIR)} {YES} {S.hanci_neg(NIR_S, T3)}")
    add("5-882",
        f"{S.na_vattabbam(T3)} {YES} {Q(f'{ARA} biết tất cả phạm vi của {BU}')} {NO} {S.tena_hi(T3)}",
        S.katha_end(KATHA[3]))

    # ---- (203) 4. Iddhikathā -------------------------------------------------------------------------------------
    sub(4, 203)
    mg = MONG.lower()
    add("5-883",
        f"{Q(T4)} {YES} “{MONG} cây cối luôn có lá” – {q(T4)} {NO_PE} {mg} cây cối luôn có hoa{PE} "
        f"{mg} cây cối luôn có quả{PE} {mg} luôn có ánh trăng{PE} {mg} luôn an ổn{PE} {mg} luôn no đủ{PE} "
        f"“{mg} luôn an lành{S.var('Syā.', 'suvuṭṭhikaṃ')}” – {q(T4)} {NO_PE}",
        f"{Q(T4)} {YES} “{MONG} sự tiếp xúc đã sinh khởi đừng chấm dứt” – {q(T4)} {NO_PE}",
        f"{MONG} cảm giác đã sinh khởi{PE} tri giác{PE} chủ ý{PE} tâm{PE} niềm tin{PE} sự tinh tấn{PE} sự tỉnh thức{PE} "
        f"sự định tâm{PE} trí tuệ đừng chấm dứt – {q(T4)} {NO_PE}",
        f"{Q(T4)} {YES} “{MONG} vật chất thường còn” – có phải có thần thông theo ý định{PE} {VSS} "
        f"“{mg} thức thường còn” – {q(T4)} {NO_PE}",
        f"{Q(T4)} {YES} “{MONG} các chúng sinh có bản chất phải sinh đừng sinh ra”, có phải có{PE} "
        f"“{mg} các chúng sinh có bản chất phải lão hóa đừng lão hóa”{PE} "
        f"“{mg} các chúng sinh có bản chất phải bệnh đừng bệnh”{PE} "
        f"“{mg} các chúng sinh có bản chất phải chết đừng chết” – {q(T4)} {NO_PE}")
    P40 = f"{PIL} đã dứt khoát hướng tâm rằng {KING} chính là vàng, và nó quả thật đã là vàng"
    N40 = (f"Chẳng phải {PIL} đã dứt khoát hướng tâm rằng {KING} chính là “vàng”, và nó quả thật đã là vàng "
           f"[{CIT_PARA} 621; {CIT_MV} 271] sao?")
    add("5-884",
        f"{S.na_vattabbam(T4)} {YES} {N40} {YES} {S.hanci(P40, T4)}",
        S.katha_end(KATHA[4]))

    # ---- (204) 5. Buddhakathā ------------------------------------------------------------------------------------
    sub(5, 204)
    add("5-885",
        f"{Q(T5)} {YES} {Q(f'{XV} sự thiết lập tỉnh thức')} {NO_PE} {q(B5)} {NO_PE}",
        S.katha_end(KATHA[5]))

    # ---- (205) 6. Sabbadisākathā ---------------------------------------------------------------------------------
    sub(6, 205)
    HV = f"{PE} ".join(f"{TT} ở cõi {h}" for h in HEAV)
    add("5-886",
        f"{Q(T6)} {YES} {Q(loc('đông'))} {NO_PE} {q(loc('đông'))} {YES} {KIN} {NO_PE}",
        f"{Q(f'{BU} {TT} ở phương nam{PE} ở phương tây{PE} ở phương bắc{PE} ở phương dưới')} {NO_PE} "
        f"{q(loc('dưới'))} {YES} {KIN_S} {NO_PE}",
        f"{Q(loc('trên'))} {NO_PE} {Q(loc('trên'))} {YES} {Q(f'Ngài {HV}')} {NO_PE}",
        S.katha_end(KATHA[6]))

    # ---- (206) 7. Dhammakathā; (207) 8. Kammakathā ---------------------------------------------------------------
    def rasi_lines(t, cit):
        l1 = (f"{Q(t)} {YES} {Q(f'chúng {MI}')} {NO_PE} {q(f'chúng {SA}')} {NO_PE} {q(f'không có {AN}')} {NO_PE} "
              f"{nanu_l(f'có {AN}')} {YES} {S.hanci_neg(f'có {AN}', t)}")
        l2 = f"{Q(t)} {YES} Chẳng phải {VR}{cit} sao? {YES} {S.hanci_neg(VR, t)}"
        return l1, l2

    def ms():                       # Micchattaniyatanti? … sammattaniyatanti? Na hevaṃ vattabbe…pe….
        return f"{Q(f'nó {MI}')} {NO_PE} {q(f'nó {SA}')} {NO_PE}"

    sub(7, 206)
    l1, l2 = rasi_lines(DH, " [Liệt kê các hiện tượng, Ma trận bộ ba 15]")
    add("5-887",
        l1, l2,
        f"{Q(R7)} {YES} {ms()} {q(f'{VSS} {V7}')} {YES} {ms()}")
    RV = f"{R7}{PE} {VSS} {V7}"
    BEC = (f"vật chất trở thành cảm giác{PE} trở thành tri giác{PE} trở thành các tạo tác{PE} trở thành thức{PE} "
           f"{VSS} thức trở thành vật chất{PE} trở thành cảm giác{PE} trở thành tri giác{PE} trở thành các tạo tác")
    add("5-888",
        f"{S.na_vattabbam(RV)} {YES} {Q(BEC)} {NO} {S.tena_hi(f'{R7}, {VSS} {V7}')}",
        S.katha_end(KATHA[7]))

    sub(8, 207)
    l1, l2 = rasi_lines(KM, "")
    add("5-889", l1, l2)
    add("5-890",
        f"{Q(DN)} {YES} {ms()} {Q(f'nghiệp {UV}{PE} {AN8}')} {YES} {ms()}")
    L79 = f"{DN}, nghiệp {UV}{PE} {AN8}"
    BEC2 = (f"nghiệp {DV} trở thành {UV}, trở thành {AV}{PE} nghiệp {UV} trở thành {DV}, trở thành {AV}{PE} "
            f"nghiệp {AV} trở thành {DV}, trở thành {UV}")
    add("5-891",
        f"{S.na_vattabbam(L79)} {YES} {Q(BEC2)} {NO} {S.tena_hi(L79)}",
        S.katha_end(KATHA[8]),
        f"{VAGGA}.",
        TASSUDDANAM,
        UDDANA)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# Helper: look up identical Pāli in the finished pi-5 rails chapters (named files only)
# ---------------------------------------------------------------------------------------------------------------
def _lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


def find(pat, maxhits=8, maxc=700):
    pat = re.compile(pat)
    hits = 0
    for name in DONE:
        pl, vl = _lines(S.PALI_DIR / name), _lines(S.OUT_DIR / name)
        for i, ln in enumerate(pl):
            m = pat.search(ln)
            if not m:
                continue
            s = max(0, m.start() - 150)
            print(f"[{name} line {i + 1}]")
            print("  PI:", ln[s:s + 400])
            print("  VI:", (vl[i] if i < len(vl) else "<missing>")[:maxc])
            hits += 1
            if hits >= maxhits:
                return


def main():
    check_strings()
    S.check_reused()
    segs = build()
    S.check_against_pali(NAME, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    (S.OUT_DIR / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", S.OUT_DIR / NAME)
    adh = S.FORMULAS_MD.parent / "adh-29"           # byte-identical copy for termbase_adherence_vi.py
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", adh / NAME)


if __name__ == "__main__":
    if sys.argv[1:2] == ["--find"]:
        find(sys.argv[2], *(int(x) for x in sys.argv[3:5]))
    else:
        main()
