"""pi-5 Kathāvatthu, Vietnamese RAILS (plain audience): chapter 2, Parihānikathā (^5-2-0 … ^5-268).

Builds AI_translation/vietnamese/pi-5-vietnamese-plain-rails_split_chapters/2-parihanikatha.md from the fixed
strings below. Imports the approved sample builder READ-ONLY (its frames, constants, per-line checks and writer).
Every string marked (pi-1) … (pi-4) is asserted to occur in that book's approved Vietnamese rails.
New recurring strings: notes-rails-2.md.

usage: python -I -X utf8 -B build_rails_2_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
import build_rails_sample_vi as S  # noqa: E402
from build_rails_sample_vi import (  # noqa: E402
    Q, q, NANU, YES, NO, NO_PE, PE, ADMIT, RE, CIT, NANU_VUTTAM, ATTHEVA,
    cap, hanci, hanci_neg, tena_hi, tena_hi_na, na_vattabbam, katha, katha_end, var, var_sp, PN,
)

NAME = "2-parihanikatha.md"

# ---------------------------------------------------------------------------------------------------------------
# Persons, fruits, the thesis
# ---------------------------------------------------------------------------------------------------------------
AR, SO, SA, AN = PN["arahā"], PN["sotāpanno"], PN["sakadāgāmī"], PN["anāgāmī"]       # (pi-4)
ARAHATTA = "trạng thái A-la-hán"                                                       # arahattā (termbase)
WHO = {"ar": AR, "so": SO, "sa": SA, "an": AN}
FRUIT = {"ar": ARAHATTA, "so": "thành quả vào dòng", "sa": "thành quả trở lại một lần",
         "an": "thành quả không trở lại"}                                              # (pi-2 / pi-4)
SAM_A = "bậc A-la-hán được giải thoát theo từng thời điểm"          # samayavimutto arahā (termbase; pi-4)
ASAM_A = "bậc A-la-hán được giải thoát không theo từng thời điểm"   # asamayavimutto arahā (pi-4)
SAM_B = "vị tỳ-khưu được giải thoát theo từng thời điểm"            # samayavimuttassa bhikkhuno (termbase)


def dec(k, neg=False, who=None):    # parihāyati X X-phalā / na parihāyati …
    return f"{who or WHO[k]} {'không ' if neg else ''}sa sút khỏi {FRUIT[k]}"


def pm(k):                          # X X-phalā parihāyamāno
    return f"{WHO[k]} khi sa sút khỏi {FRUIT[k]}"


THESIS = dec("ar")                  # parihāyati arahā arahattā
ARP = pm("ar")                      # arahā arahattā parihāyamāno

# ---------------------------------------------------------------------------------------------------------------
# Headings
# ---------------------------------------------------------------------------------------------------------------
PARIHANI = "sự suy thoái"                                            # parihāni (termbase)
H_KATHA = katha(PARIHANI)                                            # Parihānikathā
H_VADA = "Sự suy thoái xét theo lập luận dựa trên học thuyết"        # Vādayuttiparihāni
H_ARIYA = "Sự suy thoái xét theo sự đối chiếu với các bậc thánh"     # Ariyapuggalasaṃsandanaparihāni
ARIYA_END = "Sự đối chiếu với các bậc thánh."                        # Ariyapuggalasaṃsandanaṃ.
H_SUTTA = "Sự suy thoái xét theo chứng cứ từ kinh"                   # Suttasādhanaparihāni

# ---------------------------------------------------------------------------------------------------------------
# Defilements (pi-1 names) and their compounds
# ---------------------------------------------------------------------------------------------------------------
RAGA, DOSA, MOHA, MANA, DITTHI = "sự tham đắm", "sự sân hận", "sự si mê", "sự kiêu mạn", "quan điểm"
VIC, THINA, UDDH, AHIR, ANOT = ("sự hoài nghi", "sự uể oải", "sự xao động", "sự không biết hổ thẹn",
                                "sự không biết ghê sợ tội lỗi")
SAKK = "quan điểm về tự ngã"                                         # sakkāyadiṭṭhi (pi-1)
SILAB = "sự hiểu sai lệch về giới hạnh và nghi thức"                 # sīlabbataparāmāso (pi-1)


def apaya(x):                       # apāyagamanīyo X
    return f"{x} dẫn đến cõi khổ"


OL_K, OL_B = "sự tham đắm dục lạc ở dạng thô", "ác ý ở dạng thô"     # oḷāriko kāmarāgo / byāpādo
ANU_K, ANU_B = "sự tham đắm dục lạc ở dạng nhỏ nhiệm", "ác ý ở dạng nhỏ nhiệm"   # aṇusahagato …
THINA_V = THINA + var_sp("Sī., Syā., Kaṃ., Pī.", "thīnaṃ")          # thinaṃ [thīnaṃ (sī. syā. kaṃ. pī.)]
AR_KIL = [RAGA, DOSA, MOHA, MANA, DITTHI, VIC, THINA, UDDH, AHIR, ANOT]
SO_KIL = [SAKK, VIC, SILAB, apaya(RAGA), apaya(DOSA), apaya(MOHA)]
SA_KIL = [SAKK, VIC, SILAB, OL_K, OL_B]
AN_KIL = [SAKK, VIC, SILAB, ANU_K, ANU_B]

PAHINA = "đã được dứt bỏ"                                            # pahīno / pahīnā / pahīnaṃ (termbase)


def ab_list(items, gen):            # X-ssa A pahīno…pe… B pahīno… C pahīno
    out = [f"{items[0]} của {gen} {PAHINA}"] + [f"{x} {PAHINA}" for x in items[1:]]
    return PE.join(out[:1]) + "".join(f"{PE} {x}" for x in out[1:])


def ab(k, items, neg=False, who=None):   # X-ssa A pahīno…, (na) parihāyati X X-phalā
    w = who or WHO[k]
    return f"{ab_list(items, w)}, {dec(k, neg, w)}"


# ---------------------------------------------------------------------------------------------------------------
# Seeing the truths; development
# ---------------------------------------------------------------------------------------------------------------
TRUTHS = ["khổ đau", "sự phát sinh", "sự chấm dứt", "con đường", "bốn sự thật"]   # dukkhaṃ … cattāri saccāni


def seen(k, x, neg=False):          # X-ena Y diṭṭhaṃ, (na) parihāyati X X-phalā
    return f"{WHO[k]} đã thấy {x}, {dec(k, neg)}"


def seen_chain(k, neg=False, short=False):
    xs = ["khổ đau", "bốn sự thật"] if short else TRUTHS[1:]
    return f"{WHO[k]} " + f"{PE} ".join(f"đã thấy {x}" for x in xs) + f", {dec(k, neg)}"


BHAV = ["các sự thiết lập tỉnh thức", "các nỗ lực đúng đắn", "các nền tảng thần thông", "các năng lực",
        "các sức mạnh", "các chi phần giác ngộ"]   # satipaṭṭhānā … bojjhaṅgā (pi-2)
MAGGA = "con đường"
BOJJ = BHAV[-1]


def tu(x):                          # X-bhāvanā
    return f"sự tu tập {x}"


def pahana(who, x, ys):             # who-ssa X-ppahānāya Y bhāvito…
    return f"{who}, để dứt bỏ {x}, " + f"{PE} ".join(f"đã tu tập {y}" for y in ys)


UCCH = ("đã bị cắt đứt tận gốc, đã bị làm như cây thốt nốt bị chặt ngọn, đã bị làm cho không còn hiện hữu, "
        "có bản chất không sinh khởi trong tương lai")
#   ucchinnamūlo tālāvatthukato anabhāvaṅkato āyatiṃ anuppādadhammo
UCCH_V = UCCH.replace("không còn hiện hữu,", "không còn hiện hữu" + var_sp("Sī.", "anabhāvakato") + ",")

EPI = ("đã lìa tham đắm, đã lìa sân hận, đã lìa si mê, đã làm xong việc cần làm, đã đặt gánh nặng xuống, "
       "đã đạt đến mục đích của mình, đã hoàn toàn diệt tận xiềng xích hiện hữu, được giải thoát nhờ hiểu biết "
       "trọn vẹn đúng đắn, đã nhấc bỏ thanh chắn, đã lấp hào, đã nhổ cột trụ, không còn then cửa, là bậc thánh, "
       "đã hạ ngọn cờ, đã hạ gánh nặng, đã thoát khỏi trói buộc, đã chiến thắng trọn vẹn")
#   vītarāgo … suvijitavijayo
EPI3 = "đã lìa tham đắm, đã lìa sân hận, đã lìa si mê"               # vītarāgo vītadoso vītamoho
FOUR = ("khổ đau đã được vị ấy hiểu biết trọn vẹn, sự phát sinh đã được dứt bỏ, sự chấm dứt đã được tự mình "
        "chứng nghiệm, con đường đã được tu tập")
#   dukkhaṃ tassa pariññātaṃ, samudayo pahīno, nirodho sacchikato, maggo bhāvito
TASKS = ("điều cần được hiểu biết trực tiếp đã được hiểu biết trực tiếp, điều cần được hiểu biết trọn vẹn đã "
         "được hiểu biết trọn vẹn, điều cần dứt bỏ đã được dứt bỏ, điều cần được tu tập đã được tu tập, "
         "điều cần được tự mình chứng nghiệm đã được tự mình chứng nghiệm")
#   abhiññeyyaṃ abhiññātaṃ … sacchikātabbaṃ sacchikataṃ
LAST = "điều cần được tự mình chứng nghiệm đã được tự mình chứng nghiệm"   # sacchikātabbaṃ sacchikataṃ

SETTHI = "phú hộ giữ địa vị phú hộ nhờ bốn trăm nghìn, khi một trăm nghìn mất đi"
#   catūhi satasahassehi seṭṭhī seṭṭhittaṃ kārento satasahasse parihīne
SABBASAP = "sa sút khỏi toàn bộ tài sản"                             # sabbasāpateyyā parihīno / parihāyituṃ

THERAS = ["trưởng lão Đại Mục-kiền-liên", "trưởng lão Đại Ca-diếp", "trưởng lão Đại Ca-chiên-diên",
          "trưởng lão Đại Câu-hi-la", "trưởng lão Đại Bàn-đặc"]
SARI = "trưởng lão Xá-lợi-phất"                                      # Sāriputto thero (termbase)
PARIH_PAST = "đã sa sút khỏi trạng thái A-la-hán"                    # parihāyittha arahattā
NPARIH_PAST = "đã không sa sút khỏi trạng thái A-la-hán"             # na parihāyittha arahattā

CHED = "đối với điều đã được cắt, có điều cần cắt"                   # atthi chinnassa chediyaṃ
KAT = "đối với điều đã làm, có sự bồi đắp thêm"                      # atthi katassa paticayo
MAHAVA = "Đại Phẩm"                                                  # mahāva. (citation)

KAMMA_AR = ["sự ưa thích công việc", "sự ưa thích nói chuyện", "sự ưa thích ngủ nghỉ", "sự ưa thích tụ tập"]
#   kammārāmatā, bhassārāmatā, niddārāmatā, saṅgaṇikārāmatā (pi-2)
KAMA7 = ("sự tham đắm, sự tham đắm dục lạc, sự ám ảnh của tham đắm dục lạc, xiềng xích tham đắm dục lạc, "
         "dòng lũ dục lạc, ách dục lạc, chướng ngại ý muốn dục lạc")
#   rāgo kāmarāgo kāmarāgapariyuṭṭhānaṃ kāmarāgasaṃyojanaṃ kāmogho kāmayogo kāmacchandanīvaraṇaṃ
ANUSAYA = "các khuynh hướng tiềm ẩn"                                 # anusayā
ANUSAYA7 = ("khuynh hướng tiềm ẩn tham đắm dục lạc, khuynh hướng tiềm ẩn ác cảm, khuynh hướng tiềm ẩn kiêu mạn, "
            "khuynh hướng tiềm ẩn quan điểm, khuynh hướng tiềm ẩn hoài nghi, khuynh hướng tiềm ẩn tham đắm hiện "
            "hữu, khuynh hướng tiềm ẩn vô minh")                     # (pi-2)
UPACAYA = "đi đến sự tích lũy"                                       # upacayaṃ gacchati

REUSED = [  # (Pāli, Vietnamese, book)
    ("sakkāyadiṭṭhi, vicikicchā, sīlabbataparāmāso", f"{SAKK}, {VIC}, {SILAB}", "1"),
    ("lobho, doso, moho, māno, diṭṭhi, vicikicchā, thinaṃ, uddhaccaṃ, ahirikaṃ, anottappaṃ",
     f"{DOSA}, {MOHA}, {MANA}, {DITTHI}, {VIC}, {THINA}, {UDDH}, {AHIR}, {ANOT}", "1"),
    ("kāmacchandanīvaraṇaṃ", "chướng ngại ý muốn dục lạc", "1"),
    ("kāmarāgasaṃyojanaṃ", "xiềng xích tham đắm dục lạc", "1"),
    ("kāmarāgo", "sự tham đắm dục lạc", "1"),
    ("oḷārikaṃ", "ở dạng thô", "1"),
    ("puthujjano", "người phàm phu", "1"),
    ("(sukha)bhūmiyaṃ", "ở cấp độ", "1"),
    ("avijjogho avijjāyogo … avijjāpariyuṭṭhānaṃ", "dòng lũ vô minh, ách vô minh", "1"),
    ("kammārāmatā, bhassārāmatā, niddārāmatā, saṅgaṇikārāmatā", ", ".join(KAMMA_AR), "2"),
    ("satipaṭṭhānā, sammappadhānā, iddhipādā", "sự thiết lập tỉnh thức, bốn nỗ lực đúng đắn, bốn nền tảng thần thông",
     "2"),
    ("pañca balāni, satta bojjhaṅgā", "năm sức mạnh, bảy chi phần giác ngộ", "2"),
    ("kāmarāgānusayo … avijjānusayo", ANUSAYA7, "2"),
    ("sotāpattiphale … anāgāmiphale", "thành quả vào dòng, trí tuệ trong con đường trở lại một lần, trí tuệ trong "
     "thành quả trở lại một lần, trí tuệ trong con đường không trở lại, trí tuệ trong thành quả không trở lại", "2"),
    ("samayavimutto / asamayavimutto", "được giải thoát theo từng thời điểm", "4"),
    ("asamayavimutto", "được giải thoát không theo từng thời điểm", "4"),
    ("parihāyeyya", "sa sút khỏi", "4"),
    ("adhimattaṃ", "vượt trội", "4"),
    ("sotāpattiphalaṃ sacchikaroti", "tự mình chứng nghiệm thành quả vào dòng", "4"),
    ("ariyapuggalā", "các bậc thánh", "4"),
    ("ma. ni. (citation)", "Trung Bộ Kinh", "2"),
    ("evamuparipi", "cũng vậy ở các chỗ sau", "2"),
]


def check_reused():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# The chapter
# ---------------------------------------------------------------------------------------------------------------
def build_ch2():
    segs = []

    def add(i, *lines):
        lines = list(lines)
        lines[-1] = lines[-1] + f" ^{i}"
        segs.append(lines)

    def head(i, level, text):
        add(i, "#" * level + " " + text)

    T = Q(THESIS)

    # ---- Vādayuttiparihāni -------------------------------------------------------------------------------------
    head("5-2-0", 3, H_KATHA)
    head("5-2-1-0", 4, H_VADA)
    L = []
    for adv in ("ở mọi nơi", "vào mọi lúc"):                      # Sabbattha / Sabbadā
        L.append(f"{T} {YES} {Q(f'{THESIS} {adv}')} {NO_PE} {q(f'{THESIS} {adv}')} {YES} "
                 f"{Q(f'{AR} có sự suy thoái {adv}')} {NO_PE}")
    ALL = f"tất cả các bậc A-la-hán đều sa sút khỏi {ARAHATTA}"       # sabbeva arahanto arahattā parihāyanti
    L.append(f"{T} {YES} {Q(ALL)} {NO_PE} {q(ALL)} {YES} {Q('tất cả các bậc A-la-hán đều có sự suy thoái')} {NO_PE}")
    L.append(f"{T} {YES} {Q(f'{ARP} thì sa sút khỏi bốn thành quả')} {NO_PE}")
    L.append(f"{Q(f'{SETTHI}, thì sa sút khỏi địa vị phú hộ')} {YES} {Q(SABBASAP)} {NO_PE}")
    L.append(f"{Q(f'{SETTHI}, có khả năng {SABBASAP}')} {YES} {Q(f'{ARP} có khả năng sa sút khỏi bốn thành quả')} "
             f"{NO_PE}")
    add("5-239", *L)

    # ---- Ariyapuggalasaṃsandanaparihāni -----------------------------------------------------------------------
    head("5-2-2-0", 4, H_ARIYA)
    pos = [("ar", "so"), ("ar", "sa"), ("ar", "an"), ("an", "so"), ("an", "sa"), ("sa", "so")]
    neg = [("so", "ar"), ("sa", "ar"), ("an", "ar"), ("so", "an"), ("sa", "an"), ("so", "sa")]
    add("5-240", *[f"{Q(dec(a))} {YES} {Q(dec(b))} {NO_PE}" for a, b in pos],
        *[f"{Q(dec(a, True))} {YES} {Q(dec(b, True))} {NO_PE}" for a, b in neg])

    P = (f"{pm('ar')} đứng vững ở {FRUIT['an']}, {pm('an')} đứng vững ở {FRUIT['sa']}, "
         f"{pm('sa')} đứng vững ở {FRUIT['so']}")
    PUTH = f"{pm('so')} đứng vững ở cấp độ người phàm phu"          # … puthujjanabhūmiyaṃ saṇṭhāti
    SO_F = FRUIT["so"]
    add("5-241",
        f"{T} {YES} {cap(pm('ar'))} thì đứng vững ở đâu? Ở {FRUIT['an']}. {cap(pm('an'))} thì đứng vững ở đâu? "
        f"Ở {FRUIT['sa']}. {cap(pm('sa'))} thì đứng vững ở đâu? Ở {FRUIT['so']}. "
        f"{Q(PUTH.replace(' đứng vững', ' thì đứng vững'))} {NO}",
        f"{ADMIT['niggaha']} {hanci(P, PUTH, sep=';')}",
        f"{Q(f'{ARP} thì đứng vững ở {SO_F}')} {YES} "
        f"{Q(f'ngay sau {SO_F}, tự mình chứng nghiệm chính {ARAHATTA}')} {NO_PE}")

    def kil(a, b):                  # … kassa bahutarā kilesā pahīnā a-ssa vā b-ssa vāti? a-ssa. Hañci …
        pa, pb = WHO[a], WHO[b]
        return (f"{Q(dec(a))} {YES} {Q(dec(b))} {NO_PE} phiền não của ai đã được dứt bỏ nhiều hơn, của {pa} hay "
                f"của {pb}? Của {pa}. {hanci(f'phiền não của {pa} đã được dứt bỏ nhiều hơn, {dec(a)}', dec(b), ';')}")

    add("5-242", kil("ar", "so"), kil("ar", "sa"), kil("ar", "an"), kil("an", "so"))
    add("5-243", kil("an", "sa"), kil("sa", "so"))

    def bhav(a, b, items, last=None, pe=False):   # … kassa adhimattā X-bhāvanā…pe… Y-bhāvanā a-ssa vā b-ssa vāti?
        pa, pb = WHO[a], WHO[b]
        last = last or items[-1]
        chain = f"{tu(items[0])} của ai vượt trội hơn" + "".join(f"{PE} {tu(x)}" for x in items[1:])
        tail = f"của {pa} hay của {pb}?" if len(items) == 1 else f", của {pa} hay của {pb}?"
        h = hanci(f"{tu(last)} của {pa} vượt trội hơn, {dec(a)}", dec(b), ";")
        if pe:
            h = h[:-1] + PE
        return f"{Q(dec(a))} {YES} {Q(dec(b))} {NO_PE} {chain}{', ' if len(items) == 1 else ''}{tail} Của {pa}. {h}"

    add("5-244", bhav("ar", "so", [MAGGA]), bhav("ar", "so", BHAV), bhav("ar", "sa", [MAGGA, BOJJ]),
        bhav("ar", "an", [MAGGA, BOJJ]))
    add("5-245", bhav("an", "so", [MAGGA, BOJJ]), bhav("an", "sa", [MAGGA, BOJJ]))
    add("5-246", bhav("sa", "so", [MAGGA, BOJJ], pe=True))

    # ---- seeing the truths ------------------------------------------------------------------------------------
    def sq(x, y):
        return f"{Q(x)} {YES} {Q(y)} {NO_PE}"

    add("5-247", *[sq(seen("ar", x), seen("so", x)) for x in TRUTHS],
        sq(seen("ar", TRUTHS[0]), seen("sa", TRUTHS[0])), sq(seen_chain("ar"), seen("sa", TRUTHS[-1])),
        sq(seen("ar", TRUTHS[0]), seen("an", TRUTHS[0])), sq(seen_chain("ar"), seen("an", TRUTHS[-1])))
    add("5-248", sq(seen("an", TRUTHS[0]), seen("so", TRUTHS[0])), sq(seen_chain("an"), seen("so", TRUTHS[-1])),
        sq(seen("an", TRUTHS[0]), seen("sa", TRUTHS[0])), sq(seen_chain("an"), seen("sa", TRUTHS[-1])))
    add("5-249", sq(seen("sa", TRUTHS[0]), seen("so", TRUTHS[0])), sq(seen_chain("sa"), seen("so", TRUTHS[-1])))
    add("5-250",
        sq(seen("so", TRUTHS[0], True), seen("ar", TRUTHS[0], True)),
        sq(seen_chain("so", True), seen("ar", TRUTHS[-1], True)),
        sq(seen_chain("sa", True, True), seen("ar", TRUTHS[-1], True)),
        sq(seen_chain("an", True, True), seen("ar", TRUTHS[-1], True)),
        f"{Q(seen_chain('so', True, True))} {YES}",
        f"{Q(seen_chain('an', True, True))} {NO_PE}",
        sq(seen_chain("sa", True, True), seen_chain("an", True, True)),
        sq(seen_chain("so", True, True), seen_chain("sa", True, True)))

    # ---- defilements given up ---------------------------------------------------------------------------------
    def aq(x, y, end=NO):
        return f"{Q(x)} {YES} {Q(y)} {end}"

    AR_KIL_78 = [x if x != THINA else THINA_V for x in AR_KIL[1:]]
    add("5-251",
        aq(ab("ar", [RAGA]), ab("so", [SAKK]), NO_PE),
        aq(ab("ar", [RAGA]), ab("so", SO_KIL[1:]), NO_PE),
        aq(ab("ar", AR_KIL_78), ab("so", [SAKK]), NO_PE),
        aq(ab("ar", [ANOT]), ab("so", SO_KIL[1:]), NO_PE),
        aq(ab("ar", [RAGA]), ab("sa", [SAKK])),
        aq(ab("ar", [RAGA]), ab("sa", SA_KIL[1:]), NO_PE),
        aq(ab("ar", [DOSA, ANOT]), ab("sa", [SAKK, OL_B])),
        aq(ab("ar", [RAGA]), ab("an", [SAKK]), NO_PE),
        aq(ab("ar", [RAGA]), ab("an", AN_KIL[1:])),
        aq(ab("ar", [DOSA, ANOT]), ab("an", [SAKK, ANU_B])))
    SO2, SA2, AN2 = [VIC, apaya(MOHA)], [VIC, OL_B], [VIC, ANU_B]
    add("5-252",
        aq(ab("an", [SAKK]), ab("so", [SAKK])), aq(ab("an", [SAKK]), ab("so", SO2)),
        aq(ab("an", AN2), ab("so", [SAKK, apaya(MOHA)])),
        aq(ab("an", [SAKK]), ab("sa", [SAKK])), aq(ab("an", [SAKK]), ab("sa", SA_KIL[1:])),
        aq(ab("an", AN2), ab("sa", [SAKK, OL_B])))
    add("5-253",
        aq(ab("sa", [SAKK]), ab("so", [SAKK])), aq(ab("sa", [SAKK]), ab("so", SO2)),
        aq(ab("sa", [VIC, OL_K, OL_B]), ab("so", [SAKK, apaya(MOHA)])))
    ARR = [RAGA, ANOT]
    add("5-254",
        aq(ab("so", [SAKK], True), ab("ar", [RAGA], True)),
        aq(ab("so", [SAKK], True), ab("ar", [DOSA, ANOT], True)),
        aq(ab("so", SO2, True), ab("ar", ARR, True)))
    add("5-255", aq(ab("sa", [SAKK], True), ab("ar", ARR, True)), aq(ab("sa", SA2, True), ab("ar", ARR, True)))
    add("5-256", aq(ab("an", [SAKK], True), ab("ar", ARR, True)), aq(ab("an", AN2, True), ab("ar", ARR, True)))
    add("5-257", aq(ab("so", [SAKK], True), ab("an", [SAKK, ANU_B], True)),
        aq(ab("so", SO2, True), ab("an", [SAKK, ANU_B], True)))
    add("5-258", aq(ab("sa", [SAKK], True), ab("an", [SAKK, ANU_B], True)),
        aq(ab("sa", SA2, True), ab("an", [SAKK, ANU_B], True)))
    add("5-259", aq(ab("so", [SAKK], True), ab("sa", [SAKK, OL_B], True)),
        aq(ab("so", SO2, True), ab("sa", [SAKK, OL_B], True)))

    # ---- Nanu … pahīno ucchinnamūlo …; path developed; the arahant's epithets -----------------------------------
    NOTE_RE = var("Syā., Pī.", "no vata re, cũng vậy ở các chỗ sau")      # [no vata re (syā. pī.) evamuparipi]
    l117 = (f"{T} {YES} {NANU(f'{RAGA} của {AR} {PAHINA}, {UCCH_V}')} {YES} "
            + hanci_neg(f"{RAGA} của {AR} {PAHINA}, {UCCH}", THESIS).replace("chắc chắn không", f"chắc chắn{NOTE_RE} không"))
    add("5-260", l117,
        f"{T} {YES} {NANU(ab_list(AR_KIL[1:], AR) + ', ' + UCCH)} {YES} "
        f"{hanci_neg(f'{ANOT} của {AR} {PAHINA}, {UCCH}', THESIS)}",
        f"{T} {YES} {NANU(pahana(AR, RAGA, [MAGGA]))} {YES} {hanci_neg(pahana(AR, RAGA, [MAGGA]), THESIS)}",
        f"{T} {YES} {NANU(pahana(AR, RAGA, BHAV))} {YES} {hanci_neg(pahana(AR, RAGA, [BOJJ]), THESIS)}",
        f"{T} {YES} {NANU(pahana(AR, f'{DOSA}{PE} để dứt bỏ {ANOT}', [MAGGA, BOJJ]))} {YES} "
        f"{hanci_neg(pahana(AR, ANOT, [BOJJ]), THESIS)}")
    add("5-261", f"{T} {YES} {NANU(f'{AR} {EPI}; {FOUR}, {TASKS}')} {YES} "
                 f"{hanci_neg(f'{AR} {EPI3}{PE} {LAST}', THESIS)}")

    # ---- samayavimutta / asamayavimutta -----------------------------------------------------------------------
    def sd(who, neg=False):
        return dec("ar", neg, who)

    def pah_s(who, x, ys, neg=False):
        return f"{pahana(who, x, ys)}, {sd(who, neg)}"

    def ab_s(who, items, neg=False):
        return ab("ar", items, neg, who)

    DOSA_ANOT = f"{DOSA}{PE} để dứt bỏ {ANOT}"
    add("5-262",
        f"{T} ( ){var('Ka.', '(āmantā)')} {cap(sd(SAM_A))}, {sd(ASAM_A, True)}. {Q(sd(SAM_A))} {YES} "
        f"Có phải {sd(ASAM_A)}{var('Ka.', 'na parihāyatīti')} không? {NO}",
        aq(sd(ASAM_A, True), sd(SAM_A, True)),
        aq(ab_s(SAM_A, [RAGA]), ab_s(ASAM_A, [RAGA])),
        aq(ab_s(SAM_A, [DOSA, ANOT]), ab_s(ASAM_A, [ANOT])),
        aq(pah_s(SAM_A, RAGA, [MAGGA]), pah_s(ASAM_A, RAGA, [MAGGA])),
        aq(pah_s(SAM_A, RAGA, BHAV), pah_s(ASAM_A, RAGA, [BHAV[0], BOJJ])),
        aq(pah_s(SAM_A, DOSA_ANOT, [MAGGA, BOJJ]), pah_s(ASAM_A, ANOT, [MAGGA, BOJJ]), NO_PE),
        aq(f"{SAM_A} {EPI}, {FOUR}, {TASKS}, {sd(SAM_A)}", f"{ASAM_A} {EPI3}{PE} {LAST}, {sd(ASAM_A)}"))
    add("5-263",
        aq(ab_s(ASAM_A, [RAGA], True), ab_s(SAM_A, [RAGA], True)),
        aq(ab_s(ASAM_A, [DOSA, ANOT], True), ab_s(SAM_A, [ANOT], True)),
        aq(pah_s(ASAM_A, RAGA, [MAGGA, BOJJ], True), pah_s(SAM_A, RAGA, [MAGGA, BOJJ], True)),
        aq(pah_s(ASAM_A, DOSA_ANOT, [MAGGA, BOJJ], True), pah_s(SAM_A, ANOT, [MAGGA, BOJJ], True)),
        aq(f"{ASAM_A} {EPI3}{PE} {LAST}, {sd(ASAM_A, True)}", f"{SAM_A} {EPI3}{PE} {LAST}, {sd(SAM_A, True)}",
           NO_PE))

    # ---- the elders --------------------------------------------------------------------------------------------
    TV = [THERAS[0] + var_sp("Ka.", "mahāmoggalāno"), THERAS[1],
          THERAS[2] + var_sp(f"{CIT['ma. ni.']} 1.202 và các chỗ khác", "mahākaccāno"),
          THERAS[3] + var_sp("Sī., Syā., Kaṃ., Pī.", "mahākoṭṭhito"), THERAS[4]]
    add("5-264",
        f"{T} {YES} {Q(f'{SARI} {PARIH_PAST}')} {NO} Có phải {f'{PE} '.join(TV)} {PARIH_PAST} không? {NO}",
        f"{Q(f'{SARI} {NPARIH_PAST}')} {YES} {hanci_neg(f'{SARI} {NPARIH_PAST}', THESIS)}",
        f"Có phải {f'{PE} '.join(THERAS)} {NPARIH_PAST} không? {YES} "
        f"{hanci_neg(f'{THERAS[-1]} {NPARIH_PAST}', THESIS)}",
        ARIYA_END)

    # ---- Suttasādhanaparihāni ---------------------------------------------------------------------------------
    head("5-2-3-0", 4, H_SUTTA)
    add("5-265",
        f"{T} {YES} {NANU_VUTTAM}",
        f"“Thật vậy, các cách thực hành cao và thấp{var_sp('Chú giải', 'paṭipādā')} đã được bậc sa-môn công bố;",
        f"Người ta không đến bờ bên kia hai lần, nhưng điều này cũng không được xem là một lần” "
        f"[{CIT['su. ni.']} 719, trong {CIT['su. ni.']}].",
        f"{ATTHEVA} {YES} {tena_hi_na(THESIS)}",
        f"{T} {YES} {Q(CHED)} {NO}",
        f"{Q(CHED)} {YES} {NANU_VUTTAM}",
        "“Người đã lìa khao khát, không nắm giữ, không có việc gì phải làm;",
        "Đối với điều đã được cắt, không có điều cần cắt, cạm bẫy của dòng lũ đã được nhổ bỏ”.",
        f"{ATTHEVA} {YES} {tena_hi_na(CHED)}")
    add("5-266",
        f"{T} {YES} {Q(KAT)} {NO}",
        f"{Q(KAT)} {YES} {NANU_VUTTAM}",
        "“Đối với vị tỳ-khưu ấy, đã được giải thoát đúng đắn, có tâm an tịnh;",
        "Đối với điều đã làm, không có sự bồi đắp thêm, không có việc cần làm.",
        "“Cũng như tảng đá liền một khối, không lay động vì gió;",
        "Cũng vậy, toàn bộ các hình sắc, các vị, các âm thanh, các mùi và các vật xúc chạm.",
        "“Các hiện tượng đáng mong muốn và không đáng mong muốn không làm rung động bậc như vậy;",
        f"Tâm vững vàng, được giải thoát, và vị ấy quán sát sự suy tàn của tâm ấy” [{MAHAVA} 244; {CIT['a. ni.']} 6.55].",
        f"{ATTHEVA} {YES} {tena_hi_na(KAT)}")
    FIVE = f"năm hiện tượng này dẫn đến {PARIHANI} của {SAM_B}"
    AR_HAS = f"{AR} có"
    add("5-267",
        f"{na_vattabbam(THESIS)} {YES} {NANU_VUTTAM} “Này các tỳ-khưu, {FIVE}. Năm hiện tượng nào? "
        f"{cap(', '.join(KAMMA_AR))}, không xem xét lại tâm theo như tâm đã được giải thoát. Này các tỳ-khưu, chính "
        f"{FIVE}” [{CIT['a. ni.']} 5.149]. {ATTHEVA} {YES} {tena_hi(THESIS)}",
        f"{Q(f'{AR_HAS} {KAMMA_AR[0]}')} {NO}",
        f"{Q(f'{AR_HAS} {KAMMA_AR[0]}')} {YES} {Q(f'{AR_HAS} {KAMA7}')} {NO}",
        f"{Q(', '.join(f'{AR_HAS} {x}' for x in KAMMA_AR[1:]))} {NO}",
        f"{Q(f'{AR_HAS} {KAMMA_AR[3]}')} {YES} {Q(f'{AR_HAS} {KAMA7}')} {NO}")

    def pari(x):                    # X-pariyuṭṭhito parihāyati
        return f"bị {x} ám ảnh mà sa sút"

    PARI_Q = "Sự ám ảnh sinh khởi tùy thuộc vào điều gì? Sinh khởi tùy thuộc vào khuynh hướng tiềm ẩn."
    #   Pariyuṭṭhānaṃ kiṃ paṭicca uppajjatīti? Anusayaṃ paṭicca uppajjatīti.
    HAS_ANU = Q(f"{AR_HAS} {ANUSAYA}")
    A7_PE = f"khuynh hướng tiềm ẩn tham đắm dục lạc{PE} khuynh hướng tiềm ẩn vô minh"
    U3 = f"có phải {SAKK} {UPACAYA}, {VIC} {UPACAYA}, {SILAB} {UPACAYA} không?"
    verbs = ["tích lũy", "giảm trừ", "dứt bỏ", "bám víu", "phân tán", "gom tụ", "dập tắt", "nhen nhóm"]
    #   ācinati apacinati pajahati upādiyati visineti ussineti vidhūpeti sandhūpeti
    stand = [("tích lũy", "giảm trừ", "giảm trừ"), ("dứt bỏ", "bám víu", "dứt bỏ"),
             ("phân tán", "gom tụ", "phân tán"), ("dập tắt", "nhen nhóm", "dập tắt")]
    L = [f"{T} {YES} {cap(ARP)} thì bị điều gì ám ảnh mà sa sút? {cap(pari(RAGA))}. {PARI_Q} {HAS_ANU} {NO}",
         f"{HAS_ANU} {YES} {Q(f'{AR_HAS} {ANUSAYA7}')} {NO}",
         f"{cap(pari(DOSA))}{PE} {pari(MOHA)}{PE} {PARI_Q} {HAS_ANU} {NO_PE}",
         f"{HAS_ANU} {YES} {Q(f'{AR_HAS} {A7_PE}')} {NO}",
         f"{T} {YES} Ở {ARP}, điều gì {UPACAYA}? {cap(RAGA)} {UPACAYA}. {cap(U3)} {NO} "
         f"{cap(DOSA)} {UPACAYA}{PE} {MOHA} {UPACAYA}, {U3} {NO}",
         f"{T} {YES} " + " ".join(f"{Q(f'{AR} {v}')} {NO}" for v in verbs)]
    for a, b, c in stand:
        P = f"{AR} không {a} cũng không {b}, đứng vững sau khi đã {c}"
        L.append(f"{NANU(P)} {YES} {hanci_neg(P, THESIS)}")
    L.append(katha_end(PARIHANI))
    add("5-268", *L)
    return segs


def main():
    S.check_reused()
    check_reused()
    S.write(NAME, build_ch2())
    adh = S.ROOT / "0-INBOX/temp/pipeline/pi-5-vi-ai/rails/adh-2"      # termbase-adherence copy (byte-identical)
    adh.mkdir(exist_ok=True)
    (adh / NAME).write_bytes((S.OUT_DIR / NAME).read_bytes())
    print("wrote", adh / NAME)


if __name__ == "__main__":
    main()
