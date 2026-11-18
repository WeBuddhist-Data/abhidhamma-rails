"""Build the Vietnamese plain zero-shot of pi-1 chapter 1 (the matrix, 1-matika.md).

usage: python -I -X utf8 build_matika_vi.py
Reads the Pāli split chapter, attaches each block ID to the Vietnamese segment with the same ID,
checks line counts, and writes the Vietnamese split chapter. Importing this module does not write.

Exposes for later chapters:
  MATRIX_ITEMS_VI  list of (block id, letter, Pāli, Vietnamese line text)
                   e.g. ("1-M1-1", "a", "kusalā dhammā.", "Các hiện tượng thiện.")
  ITEMS            dict (block id, letter) -> Item (nom with variant slot, pred, var)
  BARE             dict (block id, letter) -> item name, lower-case start, no variant bracket, no "."
                   e.g. "các hiện tượng thiện", "các hiện tượng gắn liền với cảm giác dễ chịu"
  PRED             dict (block id, letter) -> predicate for the question frame (None for ^1-M2-109 ff.)
                   e.g. "là thiện", "gắn liền với cảm giác dễ chịu"
  QUESTION(key)    "Katame dhammā X?"  -> "Những hiện tượng nào là thiện?"
  ANSWER(key)      "ime dhammā X."     -> "đây là các hiện tượng thiện."  (the caller writes the Pāli "–" before it)
  ANSWER_BARE(key) the same without the final "."
  key = (block id, letter), e.g. ("1-M1-1", "a"); QUESTION/ANSWER also accept an Item.
  V(kind, sigla, text) variant bracket: kind "p" = dị bản (a word differs), "s" = khác chính tả (spelling only).
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[4]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / "1-matika.md"
OUT = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-zeroshot_split_chapters" / "1-matika.md"

# ---- fixed names reused by later chapters -------------------------------------------
H_MATIKA = "### Ma trận"
H_TIKA = "#### Ma trận bộ ba"
H_DUKA = "#### Ma trận bộ đôi"
END_TIKA = "Ma trận bộ ba."
END_ABHI_DUKA = "Ma trận bộ đôi theo Vi Diệu Pháp."
END_MATIKA = "Ma trận đã hoàn tất."


def V(kind, sigla, text):
    """Variant bracket: kind 'p' = dị bản (a word differs), 's' = khác chính tả (spelling only)."""
    label = "dị bản" if kind == "p" else "khác chính tả"
    return f" [{label} ({sigla}): {text}]"


GROUPS = {
    # heading id: (heading, closing line)
    "1-M-2-1-0": ("##### Nhóm về gốc rễ", "Nhóm về gốc rễ."),
    "1-M-2-2-0": ("##### Các bộ đôi xen giữa nhỏ", "Các bộ đôi xen giữa nhỏ."),
    "1-M-2-3-0": ("##### Nhóm về ô nhiễm", "Nhóm về ô nhiễm."),
    "1-M-2-4-0": ("##### Nhóm về xiềng xích", "Nhóm về xiềng xích."),
    "1-M-2-5-0": ("##### Nhóm về nút thắt", "Nhóm về nút thắt."),
    "1-M-2-6-0": ("##### Nhóm về dòng lũ", "Nhóm về dòng lũ."),
    "1-M-2-7-0": ("##### Nhóm về ách", "Nhóm về ách."),
    "1-M-2-8-0": ("##### Nhóm về chướng ngại", "Nhóm về chướng ngại."),
    "1-M-2-9-0": ("##### Nhóm về sự hiểu sai lệch", "Nhóm về sự hiểu sai lệch."),
    "1-M-2-10-0": ("##### Các bộ đôi xen giữa lớn", "Các bộ đôi xen giữa lớn."),
    "1-M-2-11-0": ("##### Nhóm về sự bám víu", "Nhóm về sự bám víu."),
    "1-M-2-12-0": ("##### Nhóm về phiền não", "Nhóm về phiền não."),
    "1-M-2-13-0": ("##### Các bộ đôi cuối", "Các bộ đôi cuối."),
    "1-M-2-14-0": ("##### Ma trận bộ đôi theo kinh",
                   "Ma trận bộ đôi theo kinh" + V("p", "Syā.", "suttantamātikā") + "."),
}

SLOT = "{V}"  # where a variant bracket goes inside an item name (default: at the end)
DH = "các hiện tượng"  # dhammā in the matrix items


class Item:
    """nom: the item name (lower-case start) with an optional SLOT for the variant bracket;
    pred: what follows «Những hiện tượng nào …?» in the question frame (None: no question form)."""

    def __init__(self, nom, pred, var=""):
        if SLOT not in nom:
            nom += SLOT
        self.nom, self.pred, self.var = nom, pred, var

    def v(self, kind, sigla, text):
        return Item(self.nom, self.pred, V(kind, sigla, text))

    @property
    def bare(self):
        return self.nom.replace(SLOT, "")

    @property
    def line(self):
        t = self.nom.replace(SLOT, self.var)
        return t[0].upper() + t[1:] + "."


def A(adj):
    """single adjective after «các hiện tượng»: «các hiện tượng thiện»; question «là thiện»."""
    return Item(f"{DH} {adj}", f"là {adj}")


def P(qual):
    """verb phrase after «các hiện tượng»; the phrase itself is the question predicate:
    «các hiện tượng gắn liền với …» / «Những hiện tượng nào gắn liền với …?»"""
    return Item(f"{DH} {qual}", qual)


def NOUN(text):
    """discourse pairs ^1-M2-109 ff.: a bare noun phrase, no «các hiện tượng», no question frame."""
    return Item(text, None)


# ---- the triads -----------------------------------------------------------------------
SEE = "sự thấy chân lý"   # dassana (pahātabba)
DEV = "sự tu tập"         # bhāvanā (pahātabba)
TRAIN = "người còn đang tu học"      # sekkha
DONE = "người đã hoàn tất tu học"    # asekkha
SELF = "thuộc về bản thân"           # ajjhatta
OUTS = "ở bên ngoài bản thân"        # bahiddhā

TRIADS = {
    1: [A("thiện"), A("bất thiện"), A("không xác định về mặt đạo đức")],
    2: [P("gắn liền với cảm giác dễ chịu"), P("gắn liền với cảm giác khó chịu"),
        P("gắn liền với cảm giác không khó chịu cũng không dễ chịu")],
    3: [P("là quả của nghiệp"), P("có khả năng sinh ra quả"),
        P("không phải là quả của nghiệp cũng không có khả năng sinh ra quả")],
    4: [P("do nghiệp tạo ra và là đối tượng của sự bám víu").v("s", "Syā.", "upādinnupādāniyā"),
        P("không do nghiệp tạo ra nhưng là đối tượng của sự bám víu"),
        P("không do nghiệp tạo ra và không phải là đối tượng của sự bám víu"
          ).v("s", "Syā.", "anupādinnānupādāniyā")],
    5: [P("bị phiền não làm vẩn đục và là đối tượng của phiền não"),
        P("không bị phiền não làm vẩn đục nhưng là đối tượng của phiền não"),
        P("không bị phiền não làm vẩn đục và không phải là đối tượng của phiền não"
          ).v("s", "Syā.", "asaṃkiliṭṭhāsaṃkilesikā")],
    6: [P("có sự hướng tâm và sự duy trì tâm"),
        P("không có sự hướng tâm, chỉ có sự duy trì tâm"),
        P("không có sự hướng tâm cũng không có sự duy trì tâm").v("s", "Syā.", "avitakkāvicārā")],
    7: [P("có sự hân hoan đi kèm"), P("có hạnh phúc đi kèm"), P("có sự bình thản đi kèm")],
    8: [P(f"cần dứt bỏ bằng {SEE}"), P(f"cần dứt bỏ bằng {DEV}"),
        P(f"không cần dứt bỏ bằng {SEE} cũng không bằng {DEV}")],
    # pahātabbahetukā: the roots are what is abandoned (as the approved Russian)
    9: [P(f"có gốc rễ cần dứt bỏ bằng {SEE}"), P(f"có gốc rễ cần dứt bỏ bằng {DEV}"),
        P(f"có gốc rễ không cần dứt bỏ bằng {SEE} cũng không bằng {DEV}")],
    10: [P("dẫn đến sự tích lũy"), P("dẫn đến sự giảm trừ"),
         P("không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ"
           ).v("s", "Syā.", "nevācayagāmino nāpacayagāmino")],
    11: [P(f"thuộc về {TRAIN}"), P(f"thuộc về {DONE}"),
         P(f"không thuộc về {TRAIN} cũng không thuộc về {DONE}").v("s", "Sī., Syā.", "nevasekkhānāsekkhā")],
    12: [A("hạn hẹp"), A("rộng lớn"), P("không thể đo lường")],
    13: [P("có đối tượng hạn hẹp"), P("có đối tượng rộng lớn"), P("có đối tượng không thể đo lường")],
    14: [A("thấp kém"), A("trung bình"), A("ưu việt")],
    15: [P("cố định theo hướng sai lầm"), P("cố định theo hướng đúng đắn"), P("không cố định")],
    16: [P("lấy con đường làm đối tượng"), P("lấy con đường làm gốc rễ"),
         P("lấy con đường làm yếu tố chủ đạo")],
    17: [P("đã sinh khởi"), P("chưa sinh khởi"), P("sẽ sinh khởi")],
    18: [P("thuộc quá khứ"), P("thuộc tương lai"), P("thuộc hiện tại")],
    19: [P("có đối tượng thuộc quá khứ"), P("có đối tượng thuộc tương lai"), P("có đối tượng thuộc hiện tại")],
    20: [P(SELF), P(OUTS), P(f"vừa {SELF} vừa {OUTS}")],
    21: [P(f"có đối tượng {SELF}"), P(f"có đối tượng {OUTS}"), P(f"có đối tượng vừa {SELF} vừa {OUTS}")],
    22: [P("thấy được và có tính va chạm"), P("không thấy được nhưng có tính va chạm"),
         P("không thấy được và không có tính va chạm").v("s", "Syā.", "anidassanāppaṭighā")],
}


def group(x, sub=None, nsub=None, with_e=True):
    """The pairs of a group (taints, fetters, ...).
    x: the group noun ('ô nhiễm'); sub / nsub: the -niya / a-…-niya qualifier
    (default 'là đối tượng của X' / 'không phải là đối tượng của X')."""
    sub = sub or f"là đối tượng của {x}"
    nsub = nsub or f"không phải là đối tượng của {x}"
    g = [
        [P(f"là {x}"), P(f"không phải là {x}")],
        [P(sub), P(nsub)],
        [P(f"gắn liền với {x}"), P(f"không gắn liền với {x}")],
        [P(f"vừa là {x} vừa {sub}"), P(f"{sub} nhưng không phải là {x}")],
    ]
    if with_e:
        g.append([P(f"vừa là {x} vừa gắn liền với {x}"), P(f"gắn liền với {x} nhưng không phải là {x}")])
    g.append([P(f"không gắn liền với {x} nhưng {sub}"), P(f"không gắn liền với {x} và {nsub}")])
    return g


H = "gốc rễ"
PAIRS = {}
# roots
PAIRS.update({
    1: [P(f"là {H}"), P(f"không phải là {H}")],
    2: [P(f"có {H}"), P(f"không có {H}")],
    3: [P(f"gắn liền với {H}"), P(f"không gắn liền với {H}")],
    4: [P(f"vừa là {H} vừa có {H}"), P(f"có {H} nhưng không phải là {H}")],
    5: [P(f"vừa là {H} vừa gắn liền với {H}"), P(f"gắn liền với {H} nhưng không phải là {H}")],
    # the Pāli (Kha) line is elliptical ("ahetukāpi"); both items written out, as in the Russian
    6: [P(f"không phải là {H} nhưng có {H}"), P(f"không phải là {H} và không có {H}")],
})
# short intermediate pairs
PAIRS.update({
    7: [P("có điều kiện"), P("không có điều kiện")],
    8: [P("do điều kiện tạo thành"), P("không do điều kiện tạo thành")],
    9: [P("thấy được"), P("không thấy được")],
    10: [P("có tính va chạm"), P("không có tính va chạm")],
    11: [P("thuộc vật chất"), A("phi vật chất")],
    12: [P("thuộc thế gian"), P("vượt thế gian")],
    13: [P("mà một loại thức nào đó có thể nhận biết"), P("mà một loại thức nào đó không thể nhận biết")],
})
PARA = "sự hiểu sai lệch"
for start, g in ((14, group("ô nhiễm")),
                 (20, group("xiềng xích")),
                 (26, group("nút thắt")),
                 (32, group("dòng lũ")),
                 (38, group("ách")),
                 (44, group("chướng ngại")),
                 (50, group(PARA, f"bị {PARA} nắm giữ", f"không bị {PARA} nắm giữ", with_e=False)),
                 (69, group("sự bám víu"))):
    for i, p in enumerate(g):
        PAIRS[start + i] = p
# long intermediate pairs
C = "tâm"
PAIRS.update({
    55: [P("có đối tượng"), P("không có đối tượng")],
    56: [P(f"là {C}"), P(f"không phải là {C}")],
    57: [P(f"đồng hành với {C}"), P(f"không đồng hành với {C}")],
    58: [P(f"gắn liền với {C}"), P(f"không gắn liền với {C}")],
    59: [P(f"hòa lẫn với {C}"), P(f"không hòa lẫn với {C}")],
    60: [P(f"do {C} sinh ra"), P(f"không do {C} sinh ra")],
    61: [P(f"cùng tồn tại với {C}"), P(f"không cùng tồn tại với {C}")],
    62: [P(f"vận hành theo {C}"), P(f"không vận hành theo {C}")],
    63: [P(f"vừa hòa lẫn với {C} vừa do {C} sinh ra"),
         P(f"không phải vừa hòa lẫn với {C} vừa do {C} sinh ra")],
    64: [P(f"vừa hòa lẫn với {C}, vừa do {C} sinh ra, vừa cùng tồn tại với {C}"),
         P(f"không phải vừa hòa lẫn với {C}, vừa do {C} sinh ra, vừa cùng tồn tại với {C}")],
    65: [P(f"vừa hòa lẫn với {C}, vừa do {C} sinh ra, vừa vận hành theo {C}"),
         P(f"không phải vừa hòa lẫn với {C}, vừa do {C} sinh ra, vừa vận hành theo {C}")],
    66: [P("thuộc phần bên trong"), P("thuộc phần bên ngoài")],
    67: [A("phái sinh"), P("không phải là phái sinh")],
    68: [P("do nghiệp tạo ra").v("s", "Sī., Syā.", "upādinnā"), P("không do nghiệp tạo ra")],
})
# defilements (eight pairs)
K = "phiền não"
SK = f"là đối tượng của {K}"
NSK = f"không phải là đối tượng của {K}"
DEF = f"bị {K} làm vẩn đục"
PAIRS.update({
    75: [P(f"là {K}"), P(f"không phải là {K}")],
    76: [P(SK), P(NSK)],
    77: [P(DEF), P(f"không {DEF}")],
    78: [P(f"gắn liền với {K}"), P(f"không gắn liền với {K}")],
    79: [P(f"vừa là {K} vừa {SK}"), P(f"{SK} nhưng không phải là {K}")],
    80: [P(f"vừa là {K} vừa {DEF}"), P(f"{DEF} nhưng không phải là {K}")],
    81: [P(f"vừa là {K} vừa gắn liền với {K}"), P(f"gắn liền với {K} nhưng không phải là {K}")],
    82: [P(f"không gắn liền với {K} nhưng {SK}"), P(f"không gắn liền với {K} và {NSK}")],
})
# closing pairs (identical Pāli = identical Vietnamese: 83a = triad 8a, 85a = 9a, 90a = 7a, 98b = 15c ...)
PAIRS.update({
    83: [TRIADS[8][0], P(f"không cần dứt bỏ bằng {SEE}")],
    84: [TRIADS[8][1], P(f"không cần dứt bỏ bằng {DEV}")],
    85: [TRIADS[9][0], P(f"không có gốc rễ cần dứt bỏ bằng {SEE}")],
    86: [TRIADS[9][1], P(f"không có gốc rễ cần dứt bỏ bằng {DEV}")],
    87: [P("có sự hướng tâm"), P("không có sự hướng tâm")],
    88: [P("có sự duy trì tâm"), P("không có sự duy trì tâm")],
    89: [P("có sự hân hoan"), P("không có sự hân hoan")],
    90: [TRIADS[7][0], P("không có sự hân hoan đi kèm")],
    91: [TRIADS[7][1], P("không có hạnh phúc đi kèm")],
    92: [TRIADS[7][2], P("không có sự bình thản đi kèm")],
    93: [P("thuộc cõi dục lạc"), P("không thuộc cõi dục lạc")],
    94: [P("thuộc cõi hình sắc"), P("không thuộc cõi hình sắc")],
    95: [P("thuộc cõi không hình sắc"), P("không thuộc cõi không hình sắc")],
    96: [P("nằm trong các cõi tồn tại"), P("không nằm trong các cõi tồn tại")],
    97: [P("dẫn đến giải thoát"), P("không dẫn đến giải thoát")],
    98: [P("cố định"), TRIADS[15][2]],
    99: [P("còn có điều cao hơn"), P("không có điều gì cao hơn")],
    100: [P("có xung đột"), P("không có xung đột")],
})
# discourse pairs
PAIRS.update({
    101: [P("thuộc về phía hiểu biết chân thật"), P("thuộc về phía vô minh")],
    102: [P("giống như tia chớp"), P("giống như kim cương")],
    103: [P("thuộc về kẻ ngu"), P("thuộc về người trí")],
    104: [A("đen tối"), A("trong sáng")],
    105: [P("gây dằn vặt"), P("không gây dằn vặt")],
    106: [P("là tên gọi"), P("là phạm vi của tên gọi")],
    107: [P("là cách diễn đạt"), P("là phạm vi của cách diễn đạt")],
    108: [P("là khái niệm"), P("là phạm vi của khái niệm")],
    109: [NOUN("phần tinh thần"), NOUN("phần vật chất")],
    110: [NOUN("vô minh"), NOUN("khao khát được hiện hữu")],
    111: [NOUN("quan điểm về sự hiện hữu"), NOUN("quan điểm về sự không hiện hữu")],
    112: [NOUN("quan điểm về sự trường tồn"), NOUN("quan điểm về sự đoạn diệt")],
    113: [NOUN("quan điểm về sự hữu hạn"), NOUN("quan điểm về sự vô hạn")],
    114: [NOUN("quan điểm về quá khứ"), NOUN("quan điểm về tương lai")],
    115: [NOUN("sự không biết hổ thẹn"), NOUN("sự không biết ghê sợ tội lỗi")],
    116: [NOUN("sự biết hổ thẹn"), NOUN("sự biết ghê sợ tội lỗi")],
    117: [NOUN("sự khó dạy bảo"), NOUN("sự kết bạn với người xấu")],
    118: [NOUN("sự dễ dạy bảo"), NOUN("sự kết bạn với người tốt")],
    119: [NOUN("sự thành thạo về các lỗi vi phạm"), NOUN("sự thành thạo về việc ra khỏi lỗi vi phạm")],
    120: [NOUN("sự thành thạo về các thành tựu thiền"),
          NOUN("sự thành thạo về việc xuất khỏi các thành tựu thiền")],
    121: [NOUN("sự thành thạo về các yếu tố"), NOUN("sự thành thạo về sự chú tâm")],
    122: [NOUN("sự thành thạo về các lĩnh vực nhận biết"),
          NOUN("sự thành thạo về sự sinh khởi tùy thuộc vào điều kiện")],
    123: [NOUN("sự thành thạo về điều có thể xảy ra"), NOUN("sự thành thạo về điều không thể xảy ra")],
    124: [NOUN("sự ngay thật"), NOUN("sự mềm mỏng")],
    125: [NOUN("sự nhẫn nại"), NOUN("sự hiền hòa")],
    126: [NOUN("sự hòa nhã"), NOUN("sự niềm nở tiếp đón").v("s", "Ka.", "paṭisandhāro ca")],
    127: [NOUN("sự không phòng hộ các cửa giác quan"), NOUN("sự không biết tiết độ trong ăn uống")],
    128: [NOUN("sự phòng hộ các cửa giác quan"), NOUN("sự biết tiết độ trong ăn uống")],
    129: [NOUN("sự mất tỉnh thức"), NOUN("sự thiếu hiểu biết rõ ràng")],
    130: [NOUN("sự tỉnh thức"), NOUN("sự hiểu biết rõ ràng")],
    131: [NOUN("sức mạnh suy xét"), NOUN("sức mạnh tu tập")],
    132: [NOUN("sự tĩnh lặng"), NOUN("sự thấu suốt")],
    133: [NOUN("dấu hiệu của sự tĩnh lặng"), NOUN("dấu hiệu của sự dốc sức")],
    134: [NOUN("sự dốc sức"), NOUN("sự không tán loạn")],
    135: [NOUN("sự suy đồi về giới hạnh"), NOUN("sự suy đồi về quan điểm")],
    136: [NOUN("sự thành tựu về giới hạnh"), NOUN("sự thành tựu về quan điểm")],
    137: [NOUN("sự trong sạch về giới hạnh"), NOUN("sự trong sạch về quan điểm")],
    138: [NOUN("sự trong sạch về quan điểm"), NOUN("và sự nỗ lực của người sống theo quan điểm của mình")],
    139: [NOUN("sự xúc động trước những điều đáng xúc động"),
          NOUN("và sự nỗ lực đúng cách của người đã xúc động")],
    140: [NOUN("sự không tự mãn với các hiện tượng thiện"), NOUN("sự không chùn bước trong nỗ lực")],
    141: [NOUN("hiểu biết chân thật"), NOUN("sự giải thoát")],
    142: [NOUN("hiểu biết về sự diệt tận"), NOUN("hiểu biết về sự không sinh khởi")],
})

LETTERS = "abc"
PALI_LETTERS = ["(Ka)", "(Kha)", "(Ga)"]

# closing lines that follow the last item of a group, keyed by the block id that carries them
TAILS = {
    "1-M1-22": [END_TIKA],
    "1-M2-6": [GROUPS["1-M-2-1-0"][1]],
    "1-M2-13": [GROUPS["1-M-2-2-0"][1]],
    "1-M2-19": [GROUPS["1-M-2-3-0"][1]],
    "1-M2-25": [GROUPS["1-M-2-4-0"][1]],
    "1-M2-31": [GROUPS["1-M-2-5-0"][1]],
    "1-M2-37": [GROUPS["1-M-2-6-0"][1]],
    "1-M2-43": [GROUPS["1-M-2-7-0"][1]],
    "1-M2-49": [GROUPS["1-M-2-8-0"][1]],
    "1-M2-54": [GROUPS["1-M-2-9-0"][1]],
    "1-M2-68": [GROUPS["1-M-2-10-0"][1]],
    "1-M2-74": [GROUPS["1-M-2-11-0"][1]],
    "1-M2-82": [GROUPS["1-M-2-12-0"][1]],
    "1-M2-100": [GROUPS["1-M-2-13-0"][1], END_ABHI_DUKA],
    "1-M2-142": [GROUPS["1-M-2-14-0"][1], END_MATIKA],
}

ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def _item(x):
    return x if isinstance(x, Item) else ITEMS[x]


def QUESTION(x):
    """'Katame dhammā X?' -> 'Những hiện tượng nào <pred>?'"""
    it = _item(x)
    assert it.pred, ("no question form", it.bare)
    return f"Những hiện tượng nào {it.pred}?"


def ANSWER_BARE(x):
    """'ime dhammā X' (no final '.'); the caller puts the Pāli dash before it."""
    return f"đây là {_item(x).bare}"


def ANSWER(x):
    return ANSWER_BARE(x) + "."


def pali_segments():
    segs, buf = [], []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = ID.search(line)
        if m:
            buf.append(line[:m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf, "trailing lines without id"
    return segs


def vietnamese_segment(bid):
    if bid == "1-M-0":
        return [H_MATIKA]
    if bid == "1-M-1-0":
        return [H_TIKA]
    if bid == "1-M-2-0":
        return [H_DUKA]
    if bid in GROUPS:
        return [GROUPS[bid][0]]
    m = re.fullmatch(r"1-M([12])-(\d+)", bid)
    assert m, bid
    items = (TRIADS if m.group(1) == "1" else PAIRS)[int(m.group(2))]
    lines = [f"({LETTERS[i]}) {t.line}" for i, t in enumerate(items)]
    return lines + TAILS.get(bid, [])


MATRIX_ITEMS_VI = []  # (block id, letter, pali, vietnamese line text)
ITEMS, BARE, PRED = {}, {}, {}


def build():
    out = []
    for bid, plines in pali_segments():
        vlines = vietnamese_segment(bid)
        assert len(vlines) == len(plines), (bid, plines, vlines)
        if re.fullmatch(r"1-M[12]-\d+", bid):
            items = (TRIADS if bid.startswith("1-M1") else PAIRS)[int(bid.rsplit("-", 1)[1])]
        for p, r in zip(plines, vlines):
            assert ("[" in p) == ("[" in r), (bid, p, r)
            assert p.startswith("#") == r.startswith("#"), (bid, p, r)
            if p.startswith("#"):
                assert len(p) - len(p.lstrip("#")) == len(r) - len(r.lstrip("#")), (bid, p, r)
            for i, pl in enumerate(PALI_LETTERS):
                if p.startswith(pl + " "):
                    pref = f"({LETTERS[i]}) "
                    assert r.startswith(pref), (bid, p, r)
                    key = (bid, LETTERS[i])
                    MATRIX_ITEMS_VI.append((bid, LETTERS[i], p[len(pl) + 1:], r[len(pref):]))
                    ITEMS[key] = items[i]
                    BARE[key] = items[i].bare
                    PRED[key] = items[i].pred
        vlines = vlines[:-1] + [vlines[-1] + f" ^{bid}"]
        out.append("\n".join(vlines))
    return "\n\n".join(out) + "\n"


TEXT = build()
assert len(MATRIX_ITEMS_VI) == 22 * 3 + 142 * 2, len(MATRIX_ITEMS_VI)
assert "–" not in TEXT and "—" not in TEXT and ":-" not in TEXT
assert all(PRED[(f"1-M2-{n}", l)] is None for n in range(109, 143) for l in "ab")
assert all(PRED[k] for k in PRED if not (k[0].startswith("1-M2-") and int(k[0].split("-")[2]) >= 109))

if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT, "items", len(MATRIX_ITEMS_VI))
