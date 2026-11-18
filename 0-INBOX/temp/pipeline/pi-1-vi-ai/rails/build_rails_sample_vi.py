"""Builder for the Vietnamese rails SAMPLE of pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng», plain audience).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/preamble.md
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/1-matika.md
  0-INBOX/temp/pipeline/pi-1-vi-ai/rails/sample-2-01/2-01-sample.md
  0-INBOX/temp/pipeline/pi-1-vi-ai/rails/vi-rails-formulas.md

All Vietnamese comes from the fixed strings below, so identical Pāli gives byte-identical Vietnamese.
Every term follows the locked termbase AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md
(+ pi-1-vi-ai/termbase/APPROVED.md). Translated fresh from the Pāli.
Later chapter builders may import the constants (TRIADS, PAIRS, q_form, a_form, FACTORS, FN, S_*, frame
functions); importing writes nothing.

usage: python -I -X utf8 build_rails_sample_vi.py
"""
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
PIPE = ROOT / "0-INBOX" / "temp" / "pipeline"
RAILS = PIPE / "pi-1-vi-ai" / "rails"
PALI_SAMPLE = PIPE / "pi-1-ru" / "ref" / "ch2-01-pali-1-122.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def cap(s):
    return s[0].upper() + s[1:]


# ================================================================== labels, variants
LAB = ["(a)", "(b)", "(c)"]          # (Ka) (Kha) (Ga)


def spell(sig, word):
    """Spelling-only variant: [vi (sī. syā.)] -> [khác chính tả (Sī., Syā.): vi]."""
    return f"[khác chính tả ({sig}): {word}]"


def reading(sig, word):
    """Variant with a different word or wording."""
    return f"[dị bản ({sig}): {word}]"


# ================================================================== text frame and headings
HOMAGE = "Kính lễ Đức Thế Tôn, bậc A-la-hán, bậc Tự Giác Ngộ Hoàn Toàn"
H_PITAKA = "Tạng Vi Diệu Pháp"                       # Abhidhammapiṭake
H_BOOK = "Liệt kê các hiện tượng"                     # Dhammasaṅgaṇīpāḷi
H_MATIKA = "Ma trận"                                  # Mātikā
TIKA = "Ma trận bộ ba"                                # Tikamātikā
DUKA = "Ma trận bộ đôi"                               # Dukamātikā
ABHI_DUKA = "Ma trận bộ đôi Vi Diệu Pháp"             # Abhidhammadukamātikā
SUTTA_DUKA = "Ma trận bộ đôi theo kinh"               # Suttantikadukamātikā
MATIKA_DONE = "Ma trận đã hoàn tất"                   # Mātikā niṭṭhitā
CUULANTARA = "Bộ đôi xen giữa nhỏ"                    # Cūḷantaradukaṃ
MAHANTARA = "Bộ đôi xen giữa lớn"                     # Mahantaradukaṃ
PITTHI = "Bộ đôi cuối"                                # Piṭṭhidukaṃ

CH_HEADINGS = {   # chapters 2-5 (### level)
    "Cittuppādakaṇḍaṃ": "Phần về sự sinh khởi của tâm",
    "Rūpakaṇḍaṃ": "Phần về vật chất",
    "Nikkhepakaṇḍaṃ": "Phần tóm lược",
    "Aṭṭhakathākaṇḍaṃ": "Phần giải thích",
}
H_KAMA_KUSALA = "Tâm thiện thuộc cõi dục lạc"         # Kāmāvacarakusalaṃ
H_PADABHAJANI = "Phân tích từng từ"                   # Padabhājanī / Padabhājanīyaṃ.
BHANAVARA_1 = "Phần tụng đọc thứ nhất"                # Paṭhamabhāṇavāro.

# ================================================================== matrix
# Item: (pali name as used after «Katame dhammā», Vietnamese attribute after «các hiện tượng», variant or "")
# Matrix line = "(a) Các hiện tượng " + attr + variant + "."
# Question  = «Những hiện tượng nào » + pred + «?»;  answer = «những hiện tượng này » + pred + «.»
# pred = attr, except the few listed in PRED (a bare adjective needs «là»; one passive recast).
PH = "Các hiện tượng"
PRED = {
    "kusalā": "là thiện",
    "akusalā": "là bất thiện",
    "arūpino": "là phi vật chất",
    "upādā": "là phái sinh",
    "kenaci viññeyyā": "có thể được một loại thức nào đó nhận biết",
    "kenaci na viññeyyā": "không thể được một loại thức nào đó nhận biết",
}


def pred_of(pali, attr):
    return PRED.get(pali, attr)


def q_form(pred):
    return f"Những hiện tượng nào {pred}?"


def a_form(pred):
    return f"những hiện tượng này {pred}."


T_SEE = "cần dứt bỏ bằng sự thấy chân lý"             # dassanena pahātabbā
T_DEV = "cần dứt bỏ bằng sự tu tập"                    # bhāvanāya pahātabbā
R_SEE = "có gốc rễ cần dứt bỏ bằng sự thấy chân lý"    # dassanena pahātabbahetukā
R_DEV = "có gốc rễ cần dứt bỏ bằng sự tu tập"          # bhāvanāya pahātabbahetukā
UPA = "là đối tượng của sự bám víu"                    # upādāniyā

TRIADS = {
    "1-M1-1": [("kusalā", "thiện", ""), ("akusalā", "bất thiện", ""),
               ("abyākatā", "không xác định về mặt đạo đức", "")],
    "1-M1-2": [("sukhāya vedanāya sampayuttā", "gắn liền với cảm giác dễ chịu", ""),
               ("dukkhāya vedanāya sampayuttā", "gắn liền với cảm giác khó chịu", ""),
               ("adukkhamasukhāya vedanāya sampayuttā",
                "gắn liền với cảm giác không khó chịu cũng không dễ chịu", "")],
    "1-M1-3": [("vipākā", "là quả của nghiệp", ""),
               ("vipākadhammadhammā", "có khả năng sinh ra quả", ""),
               ("nevavipākanavipākadhammadhammā",
                "không phải là quả của nghiệp cũng không có khả năng sinh ra quả", "")],
    "1-M1-4": [("upādiṇṇupādāniyā", f"do nghiệp tạo ra và {UPA}", spell("Syā.", "upādinnupādāniyā")),
               ("anupādiṇṇupādāniyā", f"không do nghiệp tạo ra nhưng {UPA}", ""),
               ("anupādiṇṇaanupādāniyā", "không do nghiệp tạo ra và không phải là đối tượng của sự bám víu",
                spell("Syā.", "anupādinnānupādāniyā"))],
    "1-M1-5": [("saṃkiliṭṭhasaṃkilesikā", "bị phiền não làm vẩn đục và là đối tượng của phiền não", ""),
               ("asaṃkiliṭṭhasaṃkilesikā", "không bị phiền não làm vẩn đục nhưng là đối tượng của phiền não", ""),
               ("asaṃkiliṭṭhaasaṃkilesikā",
                "không bị phiền não làm vẩn đục và không phải là đối tượng của phiền não",
                spell("Syā.", "asaṃkiliṭṭhāsaṃkilesikā"))],
    "1-M1-6": [("savitakkasavicārā", "có sự hướng tâm và sự duy trì tâm", ""),
               ("avitakkavicāramattā", "không có sự hướng tâm, chỉ có sự duy trì tâm", ""),
               ("avitakkaavicārā", "không có sự hướng tâm cũng không có sự duy trì tâm",
                spell("Syā.", "avitakkāvicārā"))],
    "1-M1-7": [("pītisahagatā", "có sự hân hoan đi kèm", ""),
               ("sukhasahagatā", "có hạnh phúc đi kèm", ""),
               ("upekkhāsahagatā", "có sự bình thản đi kèm", "")],
    "1-M1-8": [("dassanena pahātabbā", T_SEE, ""),
               ("bhāvanāya pahātabbā", T_DEV, ""),
               ("neva dassanena na bhāvanāya pahātabbā", f"không {T_SEE} cũng không {T_DEV}", "")],
    "1-M1-9": [("dassanena pahātabbahetukā", R_SEE, ""),
               ("bhāvanāya pahātabbahetukā", R_DEV, ""),
               ("neva dassanena na bhāvanāya pahātabbahetukā", f"không {R_SEE} cũng không {R_DEV}", "")],
    "1-M1-10": [("ācayagāmino", "dẫn đến sự tích lũy", ""),
                ("apacayagāmino", "dẫn đến sự giảm trừ", ""),
                ("nevācayagāmināpacayagāmino", "không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ",
                 spell("Syā.", "nevācayagāmino nāpacayagāmino"))],
    "1-M1-11": [("sekkhā", "thuộc về người còn đang tu học", ""),
                ("asekkhā", "thuộc về người đã hoàn tất tu học", ""),
                ("nevasekkhanāsekkhā",
                 "không thuộc về người còn đang tu học cũng không thuộc về người đã hoàn tất tu học",
                 spell("Sī., Syā.", "nevasekkhānāsekkhā"))],
    "1-M1-12": [("parittā", "hạn hẹp", ""), ("mahaggatā", "rộng lớn", ""),
                ("appamāṇā", "không thể đo lường", "")],
    "1-M1-13": [("parittārammaṇā", "có đối tượng hạn hẹp", ""),
                ("mahaggatārammaṇā", "có đối tượng rộng lớn", ""),
                ("appamāṇārammaṇā", "có đối tượng không thể đo lường", "")],
    "1-M1-14": [("hīnā", "thấp kém", ""), ("majjhimā", "trung bình", ""), ("paṇītā", "ưu việt", "")],
    "1-M1-15": [("micchattaniyatā", "cố định theo hướng sai lầm", ""),
                ("sammattaniyatā", "cố định theo hướng đúng đắn", ""),
                ("aniyatā", "không cố định", "")],
    "1-M1-16": [("maggārammaṇā", "lấy con đường làm đối tượng", ""),
                ("maggahetukā", "lấy con đường làm gốc rễ", ""),
                ("maggādhipatino", "lấy con đường làm yếu tố chủ đạo", "")],
    "1-M1-17": [("uppannā", "đã sinh khởi", ""), ("anuppannā", "chưa sinh khởi", ""),
                ("uppādino", "sẽ sinh khởi", "")],
    "1-M1-18": [("atītā", "thuộc quá khứ", ""), ("anāgatā", "thuộc tương lai", ""),
                ("paccuppannā", "thuộc hiện tại", "")],
    "1-M1-19": [("atītārammaṇā", "có đối tượng thuộc quá khứ", ""),
                ("anāgatārammaṇā", "có đối tượng thuộc tương lai", ""),
                ("paccuppannārammaṇā", "có đối tượng thuộc hiện tại", "")],
    "1-M1-20": [("ajjhattā", "ở nơi bản thân", ""), ("bahiddhā", "ở bên ngoài bản thân", ""),
                ("ajjhattabahiddhā", "ở nơi bản thân và ở bên ngoài bản thân", "")],
    "1-M1-21": [("ajjhattārammaṇā", "có đối tượng ở nơi bản thân", ""),
                ("bahiddhārammaṇā", "có đối tượng ở bên ngoài bản thân", ""),
                ("ajjhattabahiddhārammaṇā", "có đối tượng ở nơi bản thân và ở bên ngoài bản thân", "")],
    "1-M1-22": [("sanidassanasappaṭighā", "thấy được và có tính va chạm", ""),
                ("anidassanasappaṭighā", "không thấy được nhưng có tính va chạm", ""),
                ("anidassanaappaṭighā", "không thấy được và không có tính va chạm",
                 spell("Syā.", "anidassanāppaṭighā"))],
}

# ---- the clusters (gocchaka) share one shape
# pali: nom, neg ("no"/"na"), prone, notprone, assoc, dissoc, d6 head (the «X kho pana» word)
# vi: x (the cluster noun), is_/isnot, prone/notprone, assoc/dissoc, heading
CLUSTERS = {
    "hetu": dict(
        sids=["1-M2-1", "1-M2-2", "1-M2-3", "1-M2-4", "1-M2-5", "1-M2-6"],
        p_nom="hetū", p_neg="na", p_prone="sahetukā", p_notprone="ahetukā",
        p_assoc="hetusampayuttā", p_dissoc="hetuvippayuttā", p_d6="na hetū",
        x="gốc rễ", prone="có gốc rễ", notprone="không có gốc rễ",
        d6="không phải là gốc rễ", p_heading="Hetugocchakaṃ"),
    "asava": dict(
        sids=["1-M2-14", "1-M2-15", "1-M2-16", "1-M2-17", "1-M2-18", "1-M2-19"],
        p_nom="āsavā", p_neg="no", p_prone="sāsavā", p_notprone="anāsavā",
        p_assoc="āsavasampayuttā", p_dissoc="āsavavippayuttā", p_d6="āsavavippayuttā",
        x="ô nhiễm", p_heading="Āsavagocchakaṃ"),
    "samyojana": dict(
        sids=["1-M2-20", "1-M2-21", "1-M2-22", "1-M2-23", "1-M2-24", "1-M2-25"],
        p_nom="saṃyojanā", p_neg="no", p_prone="saṃyojaniyā", p_notprone="asaṃyojaniyā",
        p_assoc="saṃyojanasampayuttā", p_dissoc="saṃyojanavippayuttā", p_d6="saṃyojanavippayuttā",
        x="xiềng xích", p_heading="Saṃyojanagocchakaṃ"),
    "gantha": dict(
        sids=["1-M2-26", "1-M2-27", "1-M2-28", "1-M2-29", "1-M2-30", "1-M2-31"],
        p_nom="ganthā", p_neg="no", p_prone="ganthaniyā", p_notprone="aganthaniyā",
        p_assoc="ganthasampayuttā", p_dissoc="ganthavippayuttā", p_d6="ganthavippayuttā",
        x="nút thắt", p_heading="Ganthagocchakaṃ"),
    "ogha": dict(
        sids=["1-M2-32", "1-M2-33", "1-M2-34", "1-M2-35", "1-M2-36", "1-M2-37"],
        p_nom="oghā", p_neg="no", p_prone="oghaniyā", p_notprone="anoghaniyā",
        p_assoc="oghasampayuttā", p_dissoc="oghavippayuttā", p_d6="oghavippayuttā",
        x="dòng lũ", p_heading="Oghagocchakaṃ"),
    "yoga": dict(
        sids=["1-M2-38", "1-M2-39", "1-M2-40", "1-M2-41", "1-M2-42", "1-M2-43"],
        p_nom="yogā", p_neg="no", p_prone="yoganiyā", p_notprone="ayoganiyā",
        p_assoc="yogasampayuttā", p_dissoc="yogavippayuttā", p_d6="yogavippayuttā",
        x="ách", p_heading="Yogagocchakaṃ"),
    "nivarana": dict(
        sids=["1-M2-44", "1-M2-45", "1-M2-46", "1-M2-47", "1-M2-48", "1-M2-49"],
        p_nom="nīvaraṇā", p_neg="no", p_prone="nīvaraṇiyā", p_notprone="anīvaraṇiyā",
        p_assoc="nīvaraṇasampayuttā", p_dissoc="nīvaraṇavippayuttā", p_d6="nīvaraṇavippayuttā",
        x="chướng ngại", p_heading="Nīvaraṇagocchakaṃ"),
    "paramasa": dict(   # no «ceva … sampayuttā» pair: 5 segments
        sids=["1-M2-50", "1-M2-51", "1-M2-52", "1-M2-53", None, "1-M2-54"],
        p_nom="parāmāsā", p_neg="no", p_prone="parāmaṭṭhā", p_notprone="aparāmaṭṭhā",
        p_assoc="parāmāsasampayuttā", p_dissoc="parāmāsavippayuttā", p_d6="parāmāsavippayuttā",
        x="sự hiểu sai lệch", prone="bị sự hiểu sai lệch nắm giữ",
        notprone="không bị sự hiểu sai lệch nắm giữ", p_heading="Parāmāsagocchakaṃ"),
    "upadana": dict(
        sids=["1-M2-69", "1-M2-70", "1-M2-71", "1-M2-72", "1-M2-73", "1-M2-74"],
        p_nom="upādānā", p_neg="no", p_prone="upādāniyā", p_notprone="anupādāniyā",
        p_assoc="upādānasampayuttā", p_dissoc="upādānavippayuttā", p_d6="upādānavippayuttā",
        x="sự bám víu", p_heading="Upādānagocchakaṃ"),
}
for _c in CLUSTERS.values():
    x = _c["x"]
    _c.setdefault("is_", f"là {x}")
    _c.setdefault("isnot", f"không phải là {x}")
    _c.setdefault("prone", f"là đối tượng của {x}")
    _c.setdefault("notprone", f"không phải là đối tượng của {x}")
    _c.setdefault("assoc", f"gắn liền với {x}")
    _c.setdefault("dissoc", f"không gắn liền với {x}")
    _c.setdefault("d6", _c["dissoc"])
    _c.setdefault("heading", f"Nhóm về {x}")


def both(a, b):
    """X ceva … Y ca: «vừa X vừa Y» (the leading «là» of an «is» phrase stays)."""
    return f"vừa {a} vừa {b}"


def but_not(a, b):
    """X ceva … na/no ca Y: «X nhưng Y-negated»."""
    return f"{a} nhưng {b}"


def kho_pana_lines(d6, prone, notprone, heading):
    """(Ka) X kho pana dhammā Y-pi. (Kha) Z-pi. <Heading>."""
    return [f"{LAB[0]} Trong các hiện tượng {d6}, có những hiện tượng {prone}.",
            f"{LAB[1]} Cũng có những hiện tượng {notprone}.",
            f"{heading}."]


PAIRS = {}
MATRIX_LINES = {}       # sid -> full list of Vietnamese lines (without the block id)
EXTRA_NAMES = []        # (pali, pred) names used only in chapter frames (the «kho pana» pairs)


def cluster(c):
    s = c["sids"]
    PAIRS[s[0]] = [(c["p_nom"], c["is_"], ""), (f"{c['p_neg']} {c['p_nom']}", c["isnot"], "")]
    PAIRS[s[1]] = [(c["p_prone"], c["prone"], ""), (c["p_notprone"], c["notprone"], "")]
    PAIRS[s[2]] = [(c["p_assoc"], c["assoc"], ""), (c["p_dissoc"], c["dissoc"], "")]
    PAIRS[s[3]] = [(f"{c['p_nom']} ceva {c['p_prone']} ca", both(c["is_"], c["prone"]), ""),
                   (f"{c['p_prone']} ceva {c['p_neg']} ca {c['p_nom']}", but_not(c["prone"], c["isnot"]), "")]
    if s[4]:
        PAIRS[s[4]] = [(f"{c['p_nom']} ceva {c['p_assoc']} ca", both(c["is_"], c["assoc"]), ""),
                       (f"{c['p_assoc']} ceva {c['p_neg']} ca {c['p_nom']}", but_not(c["assoc"], c["isnot"]), "")]
    MATRIX_LINES[s[5]] = kho_pana_lines(c["d6"], c["prone"], c["notprone"], c["heading"])
    EXTRA_NAMES.append((f"{c['p_d6']} {c['p_prone']}", but_not(c["d6"], c["prone"])))
    EXTRA_NAMES.append((f"{c['p_d6']} {c['p_notprone']}", f"{c['d6']} và {c['notprone']}"))


for _c in CLUSTERS.values():
    cluster(_c)

KILESA = dict(x="phiền não", is_="là phiền não", isnot="không phải là phiền não",
              prone="là đối tượng của phiền não", notprone="không phải là đối tượng của phiền não",
              defiled="bị phiền não làm vẩn đục", undefiled="không bị phiền não làm vẩn đục",
              assoc="gắn liền với phiền não", dissoc="không gắn liền với phiền não",
              heading="Nhóm về phiền não")
_K = KILESA

PAIRS.update({
    # Cūḷantaradukaṃ
    "1-M2-7": [("sappaccayā", "có điều kiện", ""), ("appaccayā", "không có điều kiện", "")],
    "1-M2-8": [("saṅkhatā", "do điều kiện tạo thành", ""), ("asaṅkhatā", "không do điều kiện tạo thành", "")],
    "1-M2-9": [("sanidassanā", "thấy được", ""), ("anidassanā", "không thấy được", "")],
    "1-M2-10": [("sappaṭighā", "có tính va chạm", ""), ("appaṭighā", "không có tính va chạm", "")],
    "1-M2-11": [("rūpino", "thuộc vật chất", ""), ("arūpino", "phi vật chất", "")],
    "1-M2-12": [("lokiyā", "thuộc thế gian", ""), ("lokuttarā", "vượt thế gian", "")],
    "1-M2-13": [("kenaci viññeyyā", "mà một loại thức nào đó có thể nhận biết", ""),
                ("kenaci na viññeyyā", "mà một loại thức nào đó không thể nhận biết", "")],
    # Mahantaradukaṃ
    "1-M2-55": [("sārammaṇā", "có đối tượng", ""), ("anārammaṇā", "không có đối tượng", "")],
    "1-M2-56": [("cittā", "là tâm", ""), ("no cittā", "không phải là tâm", "")],
    "1-M2-57": [("cetasikā", "là yếu tố đồng hành với tâm", ""),
                ("acetasikā", "không phải là yếu tố đồng hành với tâm", "")],
    "1-M2-58": [("cittasampayuttā", "gắn liền với tâm", ""), ("cittavippayuttā", "không gắn liền với tâm", "")],
    "1-M2-59": [("cittasaṃsaṭṭhā", "hòa lẫn với tâm", ""), ("cittavisaṃsaṭṭhā", "không hòa lẫn với tâm", "")],
    "1-M2-60": [("cittasamuṭṭhānā", "do tâm sinh ra", ""), ("no cittasamuṭṭhānā", "không do tâm sinh ra", "")],
    "1-M2-61": [("cittasahabhuno", "cùng tồn tại với tâm", ""),
                ("no cittasahabhuno", "không cùng tồn tại với tâm", "")],
    "1-M2-62": [("cittānuparivattino", "vận hành theo tâm", ""),
                ("no cittānuparivattino", "không vận hành theo tâm", "")],
    "1-M2-63": [("cittasaṃsaṭṭhasamuṭṭhānā", "vừa hòa lẫn với tâm vừa do tâm sinh ra", ""),
                ("no cittasaṃsaṭṭhasamuṭṭhānā", "không phải vừa hòa lẫn với tâm vừa do tâm sinh ra", "")],
    "1-M2-64": [("cittasaṃsaṭṭhasamuṭṭhānasahabhuno",
                 "vừa hòa lẫn với tâm vừa do tâm sinh ra vừa cùng tồn tại với tâm", ""),
                ("no cittasaṃsaṭṭhasamuṭṭhānasahabhuno",
                 "không phải vừa hòa lẫn với tâm vừa do tâm sinh ra vừa cùng tồn tại với tâm", "")],
    "1-M2-65": [("cittasaṃsaṭṭhasamuṭṭhānānuparivattino",
                 "vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm", ""),
                ("no cittasaṃsaṭṭhasamuṭṭhānānuparivattino",
                 "không phải vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm", "")],
    "1-M2-66": [("ajjhattikā", "thuộc phần bên trong", ""), ("bāhirā", "thuộc phần bên ngoài", "")],
    "1-M2-67": [("upādā", "phái sinh", ""), ("no upādā", "không phải là phái sinh", "")],
    "1-M2-68": [("upādiṇṇā", "do nghiệp tạo ra", spell("Sī., Syā.", "upādinnā")),
                ("anupādiṇṇā", "không do nghiệp tạo ra", "")],
    # Kilesagocchakaṃ
    "1-M2-75": [("kilesā", _K["is_"], ""), ("no kilesā", _K["isnot"], "")],
    "1-M2-76": [("saṃkilesikā", _K["prone"], ""), ("asaṃkilesikā", _K["notprone"], "")],
    "1-M2-77": [("saṃkiliṭṭhā", _K["defiled"], ""), ("asaṃkiliṭṭhā", _K["undefiled"], "")],
    "1-M2-78": [("kilesasampayuttā", _K["assoc"], ""), ("kilesavippayuttā", _K["dissoc"], "")],
    "1-M2-79": [("kilesā ceva saṃkilesikā ca", both(_K["is_"], _K["prone"]), ""),
                ("saṃkilesikā ceva no ca kilesā", but_not(_K["prone"], _K["isnot"]), "")],
    "1-M2-80": [("kilesā ceva saṃkiliṭṭhā ca", both(_K["is_"], _K["defiled"]), ""),
                ("saṃkiliṭṭhā ceva no ca kilesā", but_not(_K["defiled"], _K["isnot"]), "")],
    "1-M2-81": [("kilesā ceva kilesasampayuttā ca", both(_K["is_"], _K["assoc"]), ""),
                ("kilesasampayuttā ceva no ca kilesā", but_not(_K["assoc"], _K["isnot"]), "")],
    # Piṭṭhidukaṃ
    "1-M2-83": [("dassanena pahātabbā", T_SEE, ""), ("na dassanena pahātabbā", f"không {T_SEE}", "")],
    "1-M2-84": [("bhāvanāya pahātabbā", T_DEV, ""), ("na bhāvanāya pahātabbā", f"không {T_DEV}", "")],
    "1-M2-85": [("dassanena pahātabbahetukā", R_SEE, ""),
                ("na dassanena pahātabbahetukā", f"không {R_SEE}", "")],
    "1-M2-86": [("bhāvanāya pahātabbahetukā", R_DEV, ""),
                ("na bhāvanāya pahātabbahetukā", f"không {R_DEV}", "")],
    "1-M2-87": [("savitakkā", "có sự hướng tâm", ""), ("avitakkā", "không có sự hướng tâm", "")],
    "1-M2-88": [("savicārā", "có sự duy trì tâm", ""), ("avicārā", "không có sự duy trì tâm", "")],
    "1-M2-89": [("sappītikā", "có sự hân hoan", ""), ("appītikā", "không có sự hân hoan", "")],
    "1-M2-90": [("pītisahagatā", "có sự hân hoan đi kèm", ""),
                ("na pītisahagatā", "không có sự hân hoan đi kèm", "")],
    "1-M2-91": [("sukhasahagatā", "có hạnh phúc đi kèm", ""),
                ("na sukhasahagatā", "không có hạnh phúc đi kèm", "")],
    "1-M2-92": [("upekkhāsahagatā", "có sự bình thản đi kèm", ""),
                ("na upekkhāsahagatā", "không có sự bình thản đi kèm", "")],
    "1-M2-93": [("kāmāvacarā", "thuộc cõi dục lạc", ""), ("na kāmāvacarā", "không thuộc cõi dục lạc", "")],
    "1-M2-94": [("rūpāvacarā", "thuộc cõi hình sắc", ""), ("na rūpāvacarā", "không thuộc cõi hình sắc", "")],
    "1-M2-95": [("arūpāvacarā", "thuộc cõi không hình sắc", ""),
                ("na arūpāvacarā", "không thuộc cõi không hình sắc", "")],
    "1-M2-96": [("pariyāpannā", "nằm trong các cõi tồn tại", ""),
                ("apariyāpannā", "không nằm trong các cõi tồn tại", "")],
    "1-M2-97": [("niyyānikā", "dẫn đến giải thoát", ""), ("aniyyānikā", "không dẫn đến giải thoát", "")],
    "1-M2-98": [("niyatā", "cố định", ""), ("aniyatā", "không cố định", "")],
    "1-M2-99": [("sauttarā", "còn có điều cao hơn", ""), ("anuttarā", "không có điều gì cao hơn", "")],
    "1-M2-100": [("saraṇā", "có xung đột", ""), ("araṇā", "không có xung đột", "")],
    # Suttantikadukamātikā: the «dhammā» pairs
    "1-M2-101": [("vijjābhāgino", "thuộc về phía hiểu biết chân thật", ""),
                 ("avijjābhāgino", "thuộc về phía vô minh", "")],
    "1-M2-102": [("vijjūpamā", "giống như tia chớp", ""), ("vajirūpamā", "giống như kim cương", "")],
    "1-M2-103": [("bālā", "thuộc về kẻ ngu", ""), ("paṇḍitā", "thuộc về người trí", "")],
    "1-M2-104": [("kaṇhā", "đen tối", ""), ("sukkā", "trong sáng", "")],
    "1-M2-105": [("tapanīyā", "gây dằn vặt", ""), ("atapanīyā", "không gây dằn vặt", "")],
    "1-M2-106": [("adhivacanā", "là tên gọi", ""), ("adhivacanapathā", "là phạm vi của tên gọi", "")],
    "1-M2-107": [("nirutti", "là cách diễn đạt", ""), ("niruttipathā", "là phạm vi của cách diễn đạt", "")],
    "1-M2-108": [("paññatti", "là khái niệm", ""), ("paññattipathā", "là phạm vi của khái niệm", "")],
})

# Suttanta pairs without «dhammā»: sid -> ((pali a, vi a), (pali b, vi b)); line = "(a) Vi."
SUTTA_ITEMS = {
    "1-M2-109": (("nāmañca", "Phần tinh thần"), ("rūpañca", "Vật chất")),
    "1-M2-110": (("avijjā ca", "Vô minh"), ("bhavataṇhā ca", "Khao khát được hiện hữu")),
    "1-M2-111": (("bhavadiṭṭhi ca", "Quan điểm về sự hiện hữu"),
                 ("vibhavadiṭṭhi ca", "Quan điểm về sự không hiện hữu")),
    "1-M2-112": (("sassatadiṭṭhi ca", "Quan điểm về sự trường tồn"),
                 ("ucchedadiṭṭhi ca", "Quan điểm về sự đoạn diệt")),
    "1-M2-113": (("antavā diṭṭhi ca", "Quan điểm về sự hữu hạn"),
                 ("anantavā diṭṭhi ca", "Quan điểm về sự vô hạn")),
    "1-M2-114": (("pubbantānudiṭṭhi ca", "Quan điểm về quá khứ"),
                 ("aparantānudiṭṭhi ca", "Quan điểm về tương lai")),
    "1-M2-115": (("ahirikañca", "Sự không biết hổ thẹn"), ("anottappañca", "Sự không biết ghê sợ tội lỗi")),
    "1-M2-116": (("hirī ca", "Sự biết hổ thẹn"), ("ottappañca", "Sự biết ghê sợ tội lỗi")),
    "1-M2-117": (("dovacassatā ca", "Sự khó dạy bảo"), ("pāpamittatā ca", "Sự kết bạn với người xấu")),
    "1-M2-118": (("sovacassatā ca", "Sự dễ dạy bảo"), ("kalyāṇamittatā ca", "Sự kết bạn với người tốt")),
    "1-M2-119": (("āpattikusalatā ca", "Sự thành thạo về các lỗi vi phạm"),
                 ("āpattivuṭṭhānakusalatā ca", "Sự thành thạo về việc ra khỏi lỗi vi phạm")),
    "1-M2-120": (("samāpattikusalatā ca", "Sự thành thạo về các thành tựu thiền"),
                 ("samāpattivuṭṭhānakusalatā ca", "Sự thành thạo về việc xuất khỏi các thành tựu thiền")),
    "1-M2-121": (("dhātukusalatā ca", "Sự thành thạo về các yếu tố"),
                 ("manasikārakusalatā ca", "Sự thành thạo về sự chú tâm")),
    "1-M2-122": (("āyatanakusalatā ca", "Sự thành thạo về các lĩnh vực nhận biết"),
                 ("paṭiccasamuppādakusalatā ca", "Sự thành thạo về sự sinh khởi tùy thuộc vào điều kiện")),
    "1-M2-123": (("ṭhānakusalatā ca", "Sự thành thạo về điều có thể xảy ra"),
                 ("aṭṭhānakusalatā ca", "Sự thành thạo về điều không thể xảy ra")),
    "1-M2-124": (("ajjavo ca", "Sự ngay thật"), ("maddavo ca", "Sự mềm mỏng")),
    "1-M2-125": (("khanti ca", "Sự nhẫn nại"), ("soraccañca", "Sự hiền hòa")),
    "1-M2-126": (("sākhalyañca", "Sự hòa nhã"),
                 ("paṭisanthāro ca", "Sự niềm nở tiếp đón " + spell("Ka.", "paṭisandhāro ca"))),
    "1-M2-127": (("indriyesu aguttadvāratā ca", "Sự không phòng hộ cửa các giác quan"),
                 ("bhojane amattaññutā ca", "Sự không biết tiết độ trong ăn uống")),
    "1-M2-128": (("indriyesu guttadvāratā ca", "Sự phòng hộ cửa các giác quan"),
                 ("bhojane mattaññutā ca", "Sự biết tiết độ trong ăn uống")),
    "1-M2-129": (("muṭṭhasaccañca", "Sự mất tỉnh thức"), ("asampajaññañca", "Sự thiếu hiểu biết rõ ràng")),
    "1-M2-130": (("sati ca", "Sự tỉnh thức"), ("sampajaññañca", "Sự hiểu biết rõ ràng")),
    "1-M2-131": (("paṭisaṅkhānabalañca", "Sức mạnh suy xét"), ("bhāvanābalañca", "Sức mạnh tu tập")),
    "1-M2-132": (("samatho ca", "Sự tĩnh lặng"), ("vipassanā ca", "Sự thấu suốt")),
    "1-M2-133": (("samathanimittañca", "Dấu hiệu của sự tĩnh lặng"),
                 ("paggāhanimittañca", "Dấu hiệu của sự dốc sức")),
    "1-M2-134": (("paggāho ca", "Sự dốc sức"), ("avikkhepo ca", "Sự không tán loạn")),
    "1-M2-135": (("sīlavipatti ca", "Sự suy đồi về giới hạnh"), ("diṭṭhivipatti ca", "Sự suy đồi về quan điểm")),
    "1-M2-136": (("sīlasampadā ca", "Sự thành tựu về giới hạnh"),
                 ("diṭṭhisampadā ca", "Sự thành tựu về quan điểm")),
    "1-M2-137": (("sīlavisuddhi ca", "Sự trong sạch về giới hạnh"),
                 ("diṭṭhivisuddhi ca", "Sự trong sạch về quan điểm")),
    "1-M2-138": (("diṭṭhivisuddhi kho pana", "Sự trong sạch về quan điểm"),
                 ("yathādiṭṭhissa ca padhānaṃ", "Và sự nỗ lực của người làm theo quan điểm của mình")),
    "1-M2-139": (("saṃvego ca saṃvejaniyesu ṭhānesu", "Sự xúc động trước những điều đáng xúc động"),
                 ("saṃviggassa ca yoniso padhānaṃ", "Và sự nỗ lực đúng cách của người đã xúc động")),
    "1-M2-140": (("asantuṭṭhitā ca kusalesu dhammesu", "Sự không tự mãn với các hiện tượng thiện"),
                 ("appaṭivānitā ca padhānasmiṃ", "Và sự không thối lui trong nỗ lực")),
    "1-M2-141": (("vijjā ca", "Hiểu biết chân thật"), ("vimutti ca", "Sự giải thoát")),
    "1-M2-142": (("khaye ñāṇaṃ", "Hiểu biết về sự diệt tận"),
                 ("anuppāde ñāṇanti", "Hiểu biết về sự không sinh khởi")),
}

# closing lines appended after the item lines
CLOSINGS = {
    "1-M1-22": [f"{TIKA}."],
    "1-M2-13": [f"{CUULANTARA}."],
    "1-M2-68": [f"{MAHANTARA}."],
    "1-M2-100": [f"{PITTHI}.", f"{ABHI_DUKA}."],
    "1-M2-142": [f"{SUTTA_DUKA} {reading('Syā.', 'suttantamātikā')}.", f"{MATIKA_DONE}."],
}
MATRIX_LINES["1-M2-82"] = kho_pana_lines(_K["dissoc"], _K["prone"], _K["notprone"], _K["heading"])
EXTRA_NAMES += [("kilesavippayuttā saṃkilesikā", but_not(_K["dissoc"], _K["prone"])),
                ("kilesavippayuttā asaṃkilesikā", f"{_K['dissoc']} và {_K['notprone']}")]

MATRIX_HEADINGS = {
    "1-M-0": f"### {H_MATIKA}",
    "1-M-1-0": f"#### {TIKA}",
    "1-M-2-0": f"#### {DUKA}",
    "1-M-2-1-0": f"##### {CLUSTERS['hetu']['heading']}",
    "1-M-2-2-0": f"##### {CUULANTARA}",
    "1-M-2-3-0": f"##### {CLUSTERS['asava']['heading']}",
    "1-M-2-4-0": f"##### {CLUSTERS['samyojana']['heading']}",
    "1-M-2-5-0": f"##### {CLUSTERS['gantha']['heading']}",
    "1-M-2-6-0": f"##### {CLUSTERS['ogha']['heading']}",
    "1-M-2-7-0": f"##### {CLUSTERS['yoga']['heading']}",
    "1-M-2-8-0": f"##### {CLUSTERS['nivarana']['heading']}",
    "1-M-2-9-0": f"##### {CLUSTERS['paramasa']['heading']}",
    "1-M-2-10-0": f"##### {MAHANTARA}",
    "1-M-2-11-0": f"##### {CLUSTERS['upadana']['heading']}",
    "1-M-2-12-0": f"##### {_K['heading']}",
    "1-M-2-13-0": f"##### {PITTHI}",
    "1-M-2-14-0": f"##### {SUTTA_DUKA}",
}


def all_names():
    """Every «dhammā» matrix name: [(sid, pali, attr, variant)] in matrix order."""
    out = []
    for sid, items in list(TRIADS.items()) + list(PAIRS.items()):
        for p, a, v in items:
            out.append((sid, p, a, v))
    return out


NAMES = {p: a for _, p, a, _ in all_names()}          # pali -> attr
PREDS = {p: pred_of(p, a) for p, a in NAMES.items()}   # pali -> pred
PREDS.update(dict(EXTRA_NAMES))


def matrix():
    m = dict((k, [v]) for k, v in MATRIX_HEADINGS.items())
    for sid, items in list(TRIADS.items()) + list(PAIRS.items()):
        lines = [f"{LAB[i]} {PH} {a}{(' ' + var) if var else ''}." for i, (_, a, var) in enumerate(items)]
        lines += CLOSINGS.get(sid) or []
        m[sid] = lines
    for sid, ((_, a), (_, b)) in SUTTA_ITEMS.items():
        m[sid] = [f"{LAB[0]} {a}.", f"{LAB[1]} {b}."] + (CLOSINGS.get(sid) or [])
    m.update(MATRIX_LINES)
    return m


# ================================================================== chapter 2 frames
TS = "vào lúc ấy"                        # tasmiṃ samaye
OPEN_1 = ("Vào lúc tâm thiện thuộc cõi dục lạc sinh khởi, có niềm vui đi kèm, gắn liền với hiểu biết, "
          "có đối tượng là hình sắc, hay âm thanh, hay mùi, hay vị, hay vật xúc chạm, hay đối tượng của ý, "
          "hoặc lấy bất cứ thứ gì làm đối tượng,")
# Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ
# rūpārammaṇaṃ vā … dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha,
OTHERS = ("vào lúc ấy còn có bất cứ hiện tượng phi vật chất nào khác "
          "sinh khởi tùy thuộc vào điều kiện")
# ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā
Q_KUSALA = q_form(PREDS["kusalā"])        # Katame dhammā kusalā?
A_KUSALA = a_form(PREDS["kusalā"])        # ime dhammā kusalā.
CLOSE_OTHERS = f"Hoặc {OTHERS} – {A_KUSALA}"   # Ye vā pana … dhammā – ime dhammā kusalā.

# the factor list of ^1-1, in order: (pali, vietnamese, variant)
FACTORS = [
    ("phasso", "sự tiếp xúc", ""), ("vedanā", "cảm giác", ""), ("saññā", "tri giác", ""),
    ("cetanā", "chủ ý", ""), ("cittaṃ", "tâm", ""), ("vitakko", "sự hướng tâm", ""),
    ("vicāro", "sự duy trì tâm", ""), ("pīti", "sự hân hoan", ""), ("sukhaṃ", "hạnh phúc", ""),
    ("cittassekaggatā", "sự nhất tâm", ""), ("saddhindriyaṃ", "năng lực niềm tin", ""),
    ("vīriyindriyaṃ", "năng lực tinh tấn", spell("Sī., Syā.", "viriyindriyaṃ")),
    ("satindriyaṃ", "năng lực tỉnh thức", ""), ("samādhindriyaṃ", "năng lực định tâm", ""),
    ("paññindriyaṃ", "năng lực trí tuệ", ""), ("manindriyaṃ", "năng lực ý", ""),
    ("somanassindriyaṃ", "năng lực niềm vui", ""), ("jīvitindriyaṃ", "năng lực sống", ""),
    ("sammādiṭṭhi", "quan điểm đúng đắn", ""), ("sammāsaṅkappo", "tư duy đúng đắn", ""),
    ("sammāvāyāmo", "nỗ lực đúng đắn", ""), ("sammāsati", "tỉnh thức đúng đắn", ""),
    ("sammāsamādhi", "định tâm đúng đắn", ""), ("saddhābalaṃ", "sức mạnh niềm tin", ""),
    ("vīriyabalaṃ", "sức mạnh tinh tấn", spell("Sī., Syā.", "viriyabalaṃ")),
    ("satibalaṃ", "sức mạnh tỉnh thức", ""), ("samādhibalaṃ", "sức mạnh định tâm", ""),
    ("paññābalaṃ", "sức mạnh trí tuệ", ""), ("hiribalaṃ", "sức mạnh biết hổ thẹn", ""),
    ("ottappabalaṃ", "sức mạnh biết ghê sợ tội lỗi", ""), ("alobho", "sự không tham lam", ""),
    ("adoso", "sự không sân hận", ""), ("amoho", "sự không si mê", ""),
    ("anabhijjhā", "sự không thèm muốn", ""), ("abyāpādo", "sự không ác ý", ""),
    ("sammādiṭṭhi", "quan điểm đúng đắn", ""), ("hirī", "sự biết hổ thẹn", ""),
    ("ottappaṃ", "sự biết ghê sợ tội lỗi", ""),
    ("kāyapassaddhi", "sự an tịnh của thân tinh thần", spell("Syā.", "kāyappassaddhi")),
    ("cittapassaddhi", "sự an tịnh của tâm", spell("Syā.", "cittappassaddhi")),
    ("kāyalahutā", "sự nhẹ nhàng của thân tinh thần", ""), ("cittalahutā", "sự nhẹ nhàng của tâm", ""),
    ("kāyamudutā", "sự mềm mại của thân tinh thần", ""), ("cittamudutā", "sự mềm mại của tâm", ""),
    ("kāyakammaññatā", "sự dễ vận dụng của thân tinh thần", ""),
    ("cittakammaññatā", "sự dễ vận dụng của tâm", ""),
    ("kāyapāguññatā", "sự thuần thục của thân tinh thần", ""),
    ("cittapāguññatā", "sự thuần thục của tâm", ""),
    ("kāyujukatā", "sự ngay thẳng của thân tinh thần", spell("Sī., Ka.", "kāyujjukatā")),
    ("cittujukatā", "sự ngay thẳng của tâm", spell("Sī., Ka.", "cittujjukatā")),
    ("sati", "sự tỉnh thức", ""), ("sampajaññaṃ", "sự hiểu biết rõ ràng", ""),
    ("samatho", "sự tĩnh lặng", ""), ("vipassanā", "sự thấu suốt", ""), ("paggāho", "sự dốc sức", ""),
    ("avikkhepo", "sự không tán loạn", ""),
]
FN = {p: r for p, r, _ in FACTORS}       # factor name lookup


def factor_list():
    """tasmiṃ samaye phasso hoti, vedanā hoti, … avikkhepo hoti  ->  vào lúc ấy có F, có G, …"""
    parts = [f"có {r}{(' ' + v) if v else ''}" for _, r, v in FACTORS]
    return f"thì {TS} " + ", ".join(parts)


SEG_1_1 = f"{Q_KUSALA} {OPEN_1} {factor_list()}; hoặc {OTHERS} – {A_KUSALA}"

# ---- fixed synonym strings (S): what follows «Yo/Yā/Yaṃ tasmiṃ samaye» up to the dash
TAJJA = "sinh từ sự tiếp xúc của yếu tố ý thức tương ứng"   # tajjāmanoviññāṇadhātusamphassaja-
S_PHASSA = "sự tiếp xúc, sự chạm, sự chạm đến, trạng thái đã chạm đến"
_SUKHA_TAIL = ("sự dễ chịu trong tâm, cảm nhận khoan khoái và dễ chịu sinh từ sự tiếp xúc của tâm, "
               "cảm giác khoan khoái và dễ chịu sinh từ sự tiếp xúc của tâm")
S_SUKHA = "sự khoan khoái trong tâm, " + _SUKHA_TAIL
S_VEDANA = f"sự khoan khoái trong tâm {TAJJA}, " + _SUKHA_TAIL
S_SANNA = f"tri giác {TAJJA}, sự nhận ra, trạng thái đã nhận ra"
S_CETANA = f"chủ ý {TAJJA}, sự cố ý, trạng thái đã cố ý " + reading("Syā.", "sañcetayitattaṃ")
S_CITTA = ("tâm, ý, tâm trí, tấm lòng, sự sáng ngời, ý, lĩnh vực ý, năng lực ý, "
           "thức, khối thức, yếu tố ý thức tương ứng")
S_VITAKKA = ("suy nghĩ, sự hướng tâm, tư duy, sự gắn tâm, sự gắn tâm chặt chẽ, "
             "sự đặt tâm vào đối tượng, tư duy đúng đắn")
S_VICARA = ("sự chuyển động của tâm, sự duy trì tâm, sự duy trì tâm liên tục, sự duy trì tâm sát sao, "
            "sự gắn kết liên tục của tâm với đối tượng, sự theo dõi sát đối tượng")
S_PITI = ("sự hân hoan, sự phấn khởi, sự vui vẻ, sự vui thích, sự tươi cười, sự rạng rỡ, "
          "sự mãn nguyện, sự phấn chấn, sự hài lòng của tâm")
S_SAMADHI = ("sự ổn định của tâm, sự vững vàng, sự vững chãi, sự không phân tán, sự không tán loạn, "
             "trạng thái tâm trí không phân tán, sự tĩnh lặng, năng lực định tâm, sức mạnh định tâm, "
             "định tâm đúng đắn")
S_SADDHA = ("niềm tin, sự tin tưởng, sự tin chắc, lòng tin sâu sắc, niềm tin, "
            "năng lực niềm tin, sức mạnh niềm tin")


def s_viriya(var=False):
    a = " " + spell("Sī., Syā.", "viriyārambho") if var else ""
    b = " " + spell("Sī.", "ussoḷhi") if var else ""
    return (f"sự khởi động tinh tấn trong tâm{a}, sự dấn bước, sự xông pha, sự gắng sức, sự nỗ lực, "
            f"sự hăng hái, sự bền chí{b}, sức bền, sự kiên trì, sự xông pha không lơi lỏng, "
            "sự không buông bỏ ý muốn, sự không buông bỏ gánh, sự dốc sức gánh vác, sự tinh tấn, "
            "năng lực tinh tấn, sức mạnh tinh tấn, nỗ lực đúng đắn")


S_VIRIYA = s_viriya()
S_VIRIYA_VAR = s_viriya(True)            # ^1-13 only
S_SATI = ("sự tỉnh thức, sự nhớ lại, sự hồi tưởng, sự tỉnh thức, sự ghi nhớ, sự gìn giữ trong trí nhớ, "
          "sự không hời hợt, sự không quên lãng, sự tỉnh thức, năng lực tỉnh thức, sức mạnh tỉnh thức, "
          "tỉnh thức đúng đắn")
S_PANNA = ("trí tuệ, sự hiểu rõ, sự tìm hiểu, sự tìm hiểu kỹ, sự tìm hiểu các hiện tượng, sự nhận xét, "
           "sự nhận diện, sự nhận diện chính xác, sự thông thái, sự khéo léo, sự tinh tường, "
           "sự phân biệt sáng suốt, sự suy tư, sự khảo sát, sự sâu rộng, sự thông minh, sự dẫn dắt, "
           "sự thấu suốt, sự hiểu biết rõ ràng, cây roi thúc, trí tuệ, năng lực trí tuệ, sức mạnh trí tuệ, "
           "thanh gươm trí tuệ, lâu đài trí tuệ, ánh sáng trí tuệ, hào quang trí tuệ, ngọn đuốc trí tuệ, "
           "viên ngọc trí tuệ, sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn")
S_JIVITA = ("tuổi thọ, sự tồn tại, sự tiếp diễn, sự kéo dài, sự vận động " + spell("Sī.", "irīyanā")
            + ", sự tiến triển, sự gìn giữ, sự sống, năng lực sống")
ROOT_OF = "tức gốc rễ thiện"             # X kusalamūlaṃ  ->  «X, tức gốc rễ thiện»
S_ALOBHA = ("sự không tham lam, sự không khởi lòng tham, trạng thái không khởi lòng tham, "
            "sự không say đắm, sự không bị cuốn hút, trạng thái không bị cuốn hút, "
            f"sự không thèm muốn, sự không tham lam, {ROOT_OF}")


def s_adosa(var=False):
    v = " " + spell("Syā.", "adūsanā adūsitattaṃ") if var else ""
    return (f"sự không sân hận, sự không khởi sân, trạng thái không khởi sân{v}, "
            f"sự không ác ý, sự không thù hằn, sự không sân hận, {ROOT_OF}")


S_ADOSA = s_adosa()
S_ADOSA_VAR = s_adosa(True)              # ^1-33 only
S_AMOHA = S_PANNA + f", sự không si mê, {ROOT_OF}"
HIRI_S = ("sự hổ thẹn trước điều đáng hổ thẹn, "
          "sự hổ thẹn nếu để các hiện tượng xấu ác bất thiện xảy ra nơi mình")
OTTAPPA_S = ("sự ghê sợ trước điều đáng ghê sợ, "
             "sự ghê sợ nếu để các hiện tượng xấu ác bất thiện xảy ra nơi mình")
KAYA_GEN = "của khối cảm giác, khối tri giác và khối tạo tác"   # vedanā- saññā- saṅkhārakkhandhassa
CITTA_GEN = "của khối thức"                                      # viññāṇakkhandhassa
JIVITA_AT = "ở những hiện tượng phi vật chất ấy"                 # tesaṃ arūpīnaṃ dhammānaṃ
REL = "Điều mà"                                                  # Yo / Yā / Yaṃ (opening a definition)


def s_passaddhi(var=False):
    v = (lambda w: " " + spell("Sī., Syā.", w)) if var else (lambda w: "")
    return (f"sự an tịnh, sự an tịnh hoàn toàn{v('paṭippassaddhi')}, sự lắng dịu, "
            f"sự lắng dịu hoàn toàn{v('paṭippassambhanā')}, "
            f"trạng thái đã lắng dịu hoàn toàn{v('paṭippassambhitattaṃ')}")


S_PASSADDHI = s_passaddhi()
S_PASSADDHI_VAR = s_passaddhi(True)      # ^1-40 only
S_LAHUTA = "sự nhẹ nhàng, sự chuyển đổi nhanh nhẹn, sự không chậm chạp, sự không trì trệ"
S_MUDUTA = "sự mềm mại, sự mềm mỏng, sự không thô cứng, sự không cứng nhắc"
S_KAMMANNATA = "sự dễ vận dụng, trạng thái dễ vận dụng, tính chất dễ vận dụng"
S_PAGUNATA = "sự thuần thục, trạng thái thuần thục, tính chất thuần thục"
S_UJUKATA = "sự thẳng, sự ngay thẳng, sự không quanh co, sự không cong queo, sự không vặn vẹo"


def body(s, gen=None):
    """Yo/Yā/Yaṃ tasmiṃ samaye [X-khandhassa] S  ->  «Điều mà vào lúc ấy là S [của khối …]»"""
    return f"{REL} {TS} là {s}{' ' + gen if gen else ''}"


def body_jivita(s):
    """Yo tesaṃ arūpīnaṃ dhammānaṃ S  ->  «Điều mà ở những hiện tượng phi vật chất ấy là S»"""
    return f"{REL} {JIVITA_AT} là {s}"


HIRI_BODY = body(HIRI_S)        # Yaṃ tasmiṃ samaye hirīyati hiriyitabbena hirīyati … samāpattiyā
OTTAPPA_BODY = body(OTTAPPA_S)  # Yaṃ tasmiṃ samaye ottappati ottappitabbena ottappati … samāpattiyā


def q_def(f):
    """Katamo/Katamā/Katamaṃ tasmiṃ samaye F hoti?"""
    return f"{cap(TS)}, {f} là gì?"


def a_def(f):
    """ayaṃ/idaṃ tasmiṃ samaye F hoti."""
    return f"đó là {f} {TS}."


def definition(factor, bod):
    """Katamo tasmiṃ samaye F hoti? <body> – ayaṃ/idaṃ tasmiṃ samaye F hoti."""
    f = FN[factor]
    return f"{q_def(f)} {bod} – {a_def(f)}"


def kaya(s):
    return body(s, KAYA_GEN)


def citta(s):
    return body(s, CITTA_GEN)


SAMPLE_DEFS = [   # (sid, factor, body)
    ("1-2", "phasso", body(S_PHASSA)),
    ("1-3", "vedanā", body(S_VEDANA)),
    ("1-4", "saññā", body(S_SANNA)),
    ("1-5", "cetanā", body(S_CETANA)),
    ("1-6", "cittaṃ", body(S_CITTA)),
    ("1-7", "vitakko", body(S_VITAKKA)),
    ("1-8", "vicāro", body(S_VICARA)),
    ("1-9", "pīti", body(S_PITI)),
    ("1-10", "sukhaṃ", body(S_SUKHA)),
    ("1-11", "cittassekaggatā", body(S_SAMADHI)),
    ("1-12", "saddhindriyaṃ", body(S_SADDHA)),
    ("1-13", "vīriyindriyaṃ", body(S_VIRIYA_VAR)),
    ("1-14", "satindriyaṃ", body(S_SATI)),
    ("1-15", "samādhindriyaṃ", body(S_SAMADHI)),
    ("1-16", "paññindriyaṃ", body(S_PANNA)),
    ("1-17", "manindriyaṃ", body(S_CITTA)),
    ("1-18", "somanassindriyaṃ", body(S_SUKHA)),
    ("1-19", "jīvitindriyaṃ", body_jivita(S_JIVITA)),
    ("1-20", "sammādiṭṭhi", body(S_PANNA)),
    ("1-21", "sammāsaṅkappo", body(S_VITAKKA)),
    ("1-22", "sammāvāyāmo", body(S_VIRIYA)),
    ("1-23", "sammāsati", body(S_SATI)),
    ("1-24", "sammāsamādhi", body(S_SAMADHI)),
    ("1-25", "saddhābalaṃ", body(S_SADDHA)),
    ("1-26", "vīriyabalaṃ", body(S_VIRIYA)),
    ("1-27", "satibalaṃ", body(S_SATI)),
    ("1-28", "samādhibalaṃ", body(S_SAMADHI)),
    ("1-29", "paññābalaṃ", body(S_PANNA)),
    ("1-30", "hiribalaṃ", HIRI_BODY),
    ("1-31", "ottappabalaṃ", OTTAPPA_BODY),
    ("1-32", "alobho", body(S_ALOBHA)),
    ("1-33", "adoso", body(S_ADOSA_VAR)),   # Pāli ends «hoti?»: kept as written, see sample()
    ("1-34", "amoho", body(S_AMOHA)),
    ("1-35", "anabhijjhā", body(S_ALOBHA)),
    ("1-36", "abyāpādo", body(S_ADOSA)),
    ("1-37", "sammādiṭṭhi", body(S_PANNA)),
    ("1-38", "hirī", HIRI_BODY),
    ("1-39", "ottappaṃ", OTTAPPA_BODY),
    ("1-40", "kāyapassaddhi", kaya(S_PASSADDHI_VAR)),
    ("1-41", "cittapassaddhi", citta(S_PASSADDHI)),
    ("1-42", "kāyalahutā", kaya(S_LAHUTA)),
    ("1-43", "cittalahutā", citta(S_LAHUTA)),
    ("1-44", "kāyamudutā", kaya(S_MUDUTA)),
    ("1-45", "cittamudutā", citta(S_MUDUTA)),
    ("1-46", "kāyakammaññatā", kaya(S_KAMMANNATA)),
    ("1-47", "cittakammaññatā", citta(S_KAMMANNATA)),
    ("1-48", "kāyapāguññatā", kaya(S_PAGUNATA)),
    ("1-49", "cittapāguññatā", citta(S_PAGUNATA)),
    ("1-50", "kāyujukatā", kaya(S_UJUKATA)),
    ("1-51", "cittujukatā", citta(S_UJUKATA)),
    ("1-52", "sati", body(S_SATI)),
    ("1-53", "sampajaññaṃ", body(S_PANNA)),
    ("1-54", "samatho", body(S_SAMADHI)),
    ("1-55", "vipassanā", body(S_PANNA)),
    ("1-56", "paggāho", body(S_VIRIYA)),
]


def sample():
    s = {
        "1-1-0": [f"### {CH_HEADINGS['Cittuppādakaṇḍaṃ']}"],
        "1-1-1-0": [f"#### {H_KAMA_KUSALA}"],
        "1-1-1-1-0": [f"##### {H_PADABHAJANI}"],
        "1-1": [SEG_1_1],
    }
    for sid, f, b in SAMPLE_DEFS:
        s[sid] = [definition(f, b)]
    # translate the source as written: the Pāli of ^1-33 ends «adoso hoti?»
    s["1-33"] = [s["1-33"][0][:-1] + "?"]
    s["1-57"] = [definition("avikkhepo", body(S_SAMADHI)), CLOSE_OTHERS,
                 f"{H_PADABHAJANI}.", f"{BHANAVARA_1}."]
    return s


PREAMBLE = {"T-1": [HOMAGE], "0": [f"# {H_PITAKA}"], "1-0": [f"## {H_BOOK}"]}


# ================================================================== output
def segments(path):
    out, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            out.append((m.group(1), buf))
            buf = []
    assert not buf, f"lines without id in {path}"
    return out


def emit(pali_path, vi, target):
    segs = segments(pali_path)
    ids = [i for i, _ in segs]
    assert set(ids) == set(vi), (sorted(set(ids) - set(vi))[:10], sorted(set(vi) - set(ids))[:10])
    blocks = []
    for sid, plines in segs:
        vlines = [unicodedata.normalize("NFC", x) for x in vi[sid]]
        assert len(plines) == len(vlines), (sid, len(plines), len(vlines))
        for a, b in zip(plines, vlines):
            assert len(a) - len(a.lstrip("#")) == len(b) - len(b.lstrip("#")), sid
            assert a.count("–") + a.count("—") == b.count("–") + b.count("—"), ("dash", sid)
        vlines[-1] = f"{vlines[-1]} ^{sid}"
        blocks.append("\n".join(vlines))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n\n".join(blocks) + "\n", encoding="utf-8", newline="\n")
    print("wrote", target, len(blocks), "segments")


def formulas():
    L = ["# pi-1 Dhammasaṅgaṇī: Vietnamese rails sentence formulas (binding for chapter agents)", "",
         "Format: Pāli = tiếng Việt, one per line. Generated by build_rails_sample_vi.py; import its constants "
         "rather than retyping. Termbase: AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md "
         "(+ pi-1-vi-ai/termbase/APPROVED.md). Style: 0-INBOX/temp/pipeline/vietnamese-style.md.", "",
         "## Text frame and headings", "",
         f"Namo tassa bhagavato arahato sammāsambuddhassa = {HOMAGE}",
         f"# Abhidhammapiṭake = # {H_PITAKA}",
         f"## Dhammasaṅgaṇīpāḷi = ## {H_BOOK} (mid-sentence: “{H_BOOK}”)",
         f"### Mātikā = ### {H_MATIKA}",
         f"#### Tikamātikā = #### {TIKA}",
         f"Tikamātikā. (closing line) = {TIKA}.",
         f"#### Dukamātikā = #### {DUKA}",
         f"Abhidhammadukamātikā. (closing line) = {ABHI_DUKA}.",
         f"##### Suttantikadukamātikā = ##### {SUTTA_DUKA}",
         f"Suttantikadukamātikā [suttantamātikā (syā.)]. = {SUTTA_DUKA} {reading('Syā.', 'suttantamātikā')}.",
         f"Mātikā niṭṭhitā. = {MATIKA_DONE}.",
         f"##### Cūḷantaradukaṃ / Cūḷantaradukaṃ. = ##### {CUULANTARA} / {CUULANTARA}.",
         f"##### Mahantaradukaṃ / Mahantaradukaṃ. = ##### {MAHANTARA} / {MAHANTARA}.",
         f"##### Piṭṭhidukaṃ / Piṭṭhidukaṃ. = ##### {PITTHI} / {PITTHI}.",
         ]
    for c in CLUSTERS.values():
        L.append(f"##### {c['p_heading']} / {c['p_heading']}. = ##### {c['heading']} / {c['heading']}.")
    L.append(f"##### Kilesagocchakaṃ / Kilesagocchakaṃ. = ##### {_K['heading']} / {_K['heading']}.")
    for p, r in CH_HEADINGS.items():
        L.append(f"### {p} = ### {r}")
    L += [f"#### Kāmāvacarakusalaṃ = #### {H_KAMA_KUSALA}",
          f"##### Padabhājanī = ##### {H_PADABHAJANI}",
          f"Padabhājanīyaṃ. (closing line) = {H_PADABHAJANI}.",
          f"Paṭhamabhāṇavāro. = {BHANAVARA_1}.",
          "", "## Line labels, variants, punctuation", "",
          "(Ka) / (Kha) / (Ga) = (a) / (b) / (c)",
          "[word (sī. syā.)] spelling only = [khác chính tả (Sī., Syā.): word] (sigla capitalised, comma-separated)",
          "[word (syā.)] different word or wording = [dị bản (Syā.): word]",
          "…pe… = … (same spot; never «….»)",
          "– (Pāli dash) = – (same spot, same count; never add one; no comma or colon before it)",
          "Statements end with «.»; questions end with «?» and carry a question word (gì, nào).",
          "X ceva … Y ca (both) = vừa X vừa Y;  X ceva … na/no ca Y (but not) = X nhưng không phải là Y",
          "X kho pana dhammā Y-pi. / Z-pi. (matrix) = (a) Trong các hiện tượng X, có những hiện tượng Y. / "
          "(b) Cũng có những hiện tượng Z.",
          "Matrix line = (a)/(b)/(c) + «Các hiện tượng » + attribute + variant + «.»",
          "kāya- in kāyapassaddhi etc. = thân tinh thần (sự an tịnh của thân tinh thần …)",
          "sukhaṃ as factor / jhāna factor = hạnh phúc; sukha of feeling (cetasikaṃ sukhaṃ, sukhā vedanā) = dễ chịu",
          "X kusalamūlaṃ (end of the alobha / adosa / amoha strings) = X, tức gốc rễ thiện",
          "", "## Question and answer frames", "",
          "Katame dhammā X? = Những hiện tượng nào X(pred)? (pred = the matrix attribute; see the list below)",
          "– ime dhammā X. = – những hiện tượng này X(pred).",
          f"Katame dhammā kusalā? = {Q_KUSALA}",
          f"– ime dhammā kusalā. = – {A_KUSALA}",
          f"Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ "
          f"rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
          f"dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha, = {OPEN_1}",
          "Yasmiṃ samaye … cittaṃ uppannaṃ hoti = Vào lúc tâm … sinh khởi",
          f"tasmiṃ samaye = {TS}",
          f"tasmiṃ samaye F hoti, G hoti, … (after the Yasmiṃ clause) = thì {TS} có F, có G, … («có» before every factor)",
          f"ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā = hoặc {OTHERS}",
          f"; ye vā pana … – ime dhammā kusalā. (end of ^1-1) = ; hoặc {OTHERS} – {A_KUSALA}",
          f"Ye vā pana … – ime dhammā kusalā. (own line, ^1-57) = {CLOSE_OTHERS}",
          "", "## Definition formulas (chapter 2)", "",
          f"Katamo/Katamā/Katamaṃ tasmiṃ samaye F hoti? = {q_def('F')}",
          f"Yo/Yā/Yaṃ tasmiṃ samaye S – = {body('S')} –",
          f"ayaṃ/idaṃ tasmiṃ samaye F hoti. = {a_def('F')}",
          f"Yā tasmiṃ samaye vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa S – = {kaya('S')} –",
          f"Yā tasmiṃ samaye viññāṇakkhandhassa S – = {citta('S')} –",
          f"Yo tesaṃ arūpīnaṃ dhammānaṃ S – = {body_jivita('S')} –",
          f"Yaṃ tasmiṃ samaye hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā – = {HIRI_BODY} –",
          f"Yaṃ tasmiṃ samaye ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā – = {OTTAPPA_BODY} –",
          f"alobho/adoso/amoho kusalamūlaṃ = sự không tham lam/sự không sân hận/sự không si mê, {ROOT_OF}",
          "Example ^1-2 = " + definition("phasso", body(S_PHASSA)),
          "^1-33 (Pāli ends «hoti?», kept as written) = … – đó là sự không sân hận vào lúc ấy?",
          "", "## Factor names (^1-1 order)", ""]
    seen = set()
    for p, r, v in FACTORS:
        if p in seen:
            continue
        seen.add(p)
        L.append(f"{p} = {r}" + (f"  (^1-1 variant: {v})" if v else ""))
    L += ["", "## Fixed synonym strings", "",
          f"phasso phusanā saṃphusanā saṃphusitattaṃ = {S_PHASSA}",
          f"tajjāmanoviññāṇadhātusamphassaja- (after its first noun) = {TAJJA}",
          f"tajjāmanoviññāṇadhātusamphassajaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā = {S_VEDANA}",
          f"cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā = {S_SUKHA}",
          f"tajjāmanoviññāṇadhātusamphassajā saññā sañjānanā sañjānitattaṃ = {S_SANNA}",
          f"tajjāmanoviññāṇadhātusamphassajā cetanā sañcetanā cetayitattaṃ [sañcetayitattaṃ (syā.)] = {S_CETANA}",
          f"cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho tajjāmanoviññāṇadhātu = {S_CITTA}",
          f"takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo = {S_VITAKKA}",
          f"cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā = {S_VICARA}",
          f"pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa = {S_PITI}",
          f"cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ sammāsamādhi = {S_SAMADHI}",
          f"saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ = {S_SADDHA}",
          f"cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo = {S_VIRIYA}",
          f"(^1-13 with variants) = {S_VIRIYA_VAR}",
          f"sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ sammāsati = {S_SATI}",
          f"paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ amoho dhammavicayo sammādiṭṭhi = {S_PANNA}",
          f"… sammādiṭṭhi amoho kusalamūlaṃ (the amoho definition) = {S_AMOHA}",
          f"āyu ṭhiti yapanā yāpanā iriyanā [irīyanā (sī.)] vattanā pālanā jīvitaṃ jīvitindriyaṃ = {S_JIVITA}",
          f"alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ = {S_ALOBHA}",
          f"adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ = {S_ADOSA}",
          f"(^1-33 with variant) = {S_ADOSA_VAR}",
          f"passaddhi paṭipassaddhi passambhanā paṭipassambhanā paṭipassambhitattaṃ = {S_PASSADDHI}",
          f"(^1-40 with variants) = {S_PASSADDHI_VAR}",
          f"lahutā lahupariṇāmatā adandhanatā avitthanatā = {S_LAHUTA}",
          f"mudutā maddavatā akakkhaḷatā akathinatā = {S_MUDUTA}",
          f"kammaññatā kammaññattaṃ kammaññabhāvo = {S_KAMMANNATA}",
          f"paguṇatā paguṇattaṃ paguṇabhāvo = {S_PAGUNATA}",
          f"ujutā ujukatā ajimhatā avaṅkatā akuṭilatā = {S_UJUKATA}",
          "", "## Matrix names with question and answer forms", "",
          "Matrix line = (a)/(b)/(c) + «Các hiện tượng » + attribute + variant + «.»", ""]
    for sid, p, a, var in all_names():
        dh = f"{p} dhammā"
        if " ceva " in p:     # matrix word order: X ceva dhammā Y ca
            x, rest = p.split(" ceva ", 1)
            dh = f"{x} ceva dhammā {rest}"
        L.append(f"{dh} [{sid}] = {PH} {a}" + (f" {var}" if var else ""))
        L.append(f"Katame dhammā {p}? = {q_form(PREDS[p])}")
        L.append(f"ime dhammā {p}. = {a_form(PREDS[p])}")
    L += ["", "### Names used only in later chapters (the «kho pana» pairs)", ""]
    for p, r in EXTRA_NAMES:
        L.append(f"Katame dhammā {p}? = {q_form(r)}")
        L.append(f"ime dhammā {p}. = {a_form(r)}")
    L += ["", "### Suttanta items without «dhammā»", ""]
    for sid, ((pa, ra), (pb, rb)) in SUTTA_ITEMS.items():
        L.append(f"{pa} [{sid}] = {ra}")
        L.append(f"{pb} [{sid}] = {rb}")
    L += ["", "### «kho pana» matrix lines", ""]
    for sid in sorted(MATRIX_LINES, key=lambda s: int(s.split("-")[-1])):
        L.append(f"[{sid}] = " + " / ".join(MATRIX_LINES[sid]))
    return unicodedata.normalize("NFC", "\n".join(L) + "\n")


def main():
    emit(PALI / "preamble.md", PREAMBLE, OUT / "preamble.md")
    emit(PALI / "1-matika.md", matrix(), OUT / "1-matika.md")
    emit(PALI_SAMPLE, sample(), RAILS / "sample-2-01" / "2-01-sample.md")
    (RAILS / "vi-rails-formulas.md").write_text(formulas(), encoding="utf-8", newline="\n")
    print("wrote", RAILS / "vi-rails-formulas.md")


if __name__ == "__main__":
    main()
