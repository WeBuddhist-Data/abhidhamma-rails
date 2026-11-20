# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Vietnamese plain zero-shot: chapters 2 (Āyatanavibhaṅga) and 3 (Dhātuvibhaṅga).

usage: python -I -X utf8 build_2-3_vi.py [--unused]
Writes AI_translation\\vietnamese\\pi-2-vietnamese-plain-zeroshot_split_chapters\\2-ayatanavibhango.md
and 3-dhatuvibhango.md (only when run as a script; importing writes nothing).

Imports build_ch1_sample_vi (S) and build_1_vi (B) and reuses their strings and matrix-item tables.
Pāli strings that occur in pi-1 are copied from the reviewed pi-1 Vietnamese rails by block ID at build time
(pi1(), asserted). Pañhāpucchaka: B's phrase-level method; any Pāli inflection (neuter -aṃ, feminine dhātu
forms, -ñca / -ñceva) is reduced to one canonical form (canon()) and looked up in B.SURF, so identical items
give identical Vietnamese. Unknown Pāli raises KeyError (nothing is guessed). Block IDs come from the Pāli.
"""
import os, re, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai"
sys.path.insert(0, HERE)
import build_ch1_sample_vi as S  # noqa: E402
import build_1_vi as B  # noqa: E402

DASH = S.DASH
cap, low = S.cap, S.low
VUCCATI = S.VUCCATI          # đó được gọi là
TATTHA = S.TATTHA            # Ở đây,
TOGETHER = S.KHANDHA_TOGETHER  # khi gom tất cả lại làm một và thu tóm lại


def q(name):
    """Tattha katamo/katamā/katamaṃ X?  ->  Ở đây, X là gì?"""
    return f"{TATTHA} {name} là gì?"


def called(name, quoted=True):
    return f"{VUCCATI} “{name}”" if quoted else f"{VUCCATI} {name}"


def listing(names):
    """A, B, …, Y và Z (as S.FIVE_AGGREGATES)."""
    return ", ".join(names[:-1]) + " và " + names[-1]


# ---------------------------------------------------------------- 1. pi-1 strings by block ID
_PI1 = {}


def pi1(bid):
    if not _PI1:
        for fn in sorted(os.listdir(S.PI1_VI_DIR)):
            if fn.endswith(".md"):
                for line in open(os.path.join(S.PI1_VI_DIR, fn), encoding="utf-8").read().split("\n"):
                    m = S.ID.search(line)
                    if m:
                        _PI1[m.group(1)[1:]] = S.ID.sub("", line)
    return _PI1[bid]


def between(s, a, b):
    i = s.index(a) + len(a)
    return s[i:s.index(b, i)]


def repl(s, old, new):
    assert s.count(old) == 1, (old, s[:80])
    return s.replace(old, new)


# ---------------------------------------------------------------- 2. names
AYATANA = {  # [pi-1]
    "cakkhāyatanaṃ": "lĩnh vực mắt", "sotāyatanaṃ": "lĩnh vực tai", "ghānāyatanaṃ": "lĩnh vực mũi",
    "jivhāyatanaṃ": "lĩnh vực lưỡi", "kāyāyatanaṃ": "lĩnh vực thân", "manāyatanaṃ": "lĩnh vực ý",
    "rūpāyatanaṃ": "lĩnh vực hình sắc", "saddāyatanaṃ": "lĩnh vực âm thanh", "gandhāyatanaṃ": "lĩnh vực mùi",
    "rasāyatanaṃ": "lĩnh vực vị", "phoṭṭhabbāyatanaṃ": "lĩnh vực vật xúc chạm",
    "dhammāyatanaṃ": "lĩnh vực đối tượng của ý",
}
TWELVE = "Mười hai lĩnh vực nhận biết"   # Dvādasāyatanāni [new; āyatana pi-1]
DOOR = {"cakkhu": "mắt", "sota": "tai", "ghāna": "mũi", "jivhā": "lưỡi", "kāya": "thân", "mano": "ý"}
OBJ = {"rūpa": "hình sắc", "sadda": "âm thanh", "gandha": "mùi", "rasa": "vị", "phoṭṭhabba": "vật xúc chạm",
       "dhamma": "đối tượng của ý"}
DHATU = {}   # [pi-1 words]
for d, v in DOOR.items():
    if d != "mano":
        DHATU[d + "dhātu"] = "yếu tố " + v
        DHATU[d + "viññāṇadhātu"] = "yếu tố thức qua " + v           # pi-1 ^1-433 «yếu tố thức qua mắt»
for o, v in OBJ.items():
    DHATU[o + "dhātu"] = "yếu tố " + v
DHATU.update({
    "manodhātu": "yếu tố ý", "manoviññāṇadhātu": "yếu tố ý thức",                    # [pi-1]
    "pathavīdhātu": "yếu tố đất", "āpodhātu": "yếu tố nước", "tejodhātu": "yếu tố lửa",  # [pi-1]
    "vāyodhātu": "yếu tố gió", "ākāsadhātu": "yếu tố không gian", "viññāṇadhātu": "yếu tố thức",
    "sukhadhātu": "yếu tố dễ chịu", "dukkhadhātu": "yếu tố khó chịu",                   # [new; pi-1 indriya words]
    "somanassadhātu": "yếu tố niềm vui", "domanassadhātu": "yếu tố nỗi buồn",
    "upekkhādhātu": "yếu tố bình thản", "avijjādhātu": "yếu tố vô minh",
    "kāmadhātu": "yếu tố dục lạc", "byāpādadhātu": "yếu tố ác ý",                       # [new; pi-1 kāma, byāpāda]
    "vihiṃsādhātu": "yếu tố hãm hại", "nekkhammadhātu": "yếu tố từ bỏ",
    "abyāpādadhātu": "yếu tố không ác ý", "avihiṃsādhātu": "yếu tố không hãm hại",
    "asaṅkhatā dhātu": "yếu tố không do điều kiện tạo thành",                          # [pi-1 ^1-583]
})
EIGHTEEN = "Mười tám yếu tố"   # Aṭṭhārasa dhātuyo [new]
NAME = dict(AYATANA)
NAME.update(DHATU)
for _pa, _a in B.AGG_PALI.items():
    NAME[_pa + "kkhandho"] = S.AGG[_a]["khandha"]

ASANKHATA = DHATU["asaṅkhatā dhātu"]
assert "và " + ASANKHATA in pi1("1-583")
DHAMMA_MEMBERS = (f"{cap(S.AGG['vedana']['khandha'])}, {S.AGG['sanna']['khandha']}, {S.AGG['sankhara']['khandha']}, "
                  "loại vật chất không thấy được và không có tính va chạm, nằm trong lĩnh vực đối tượng của ý, "
                  f"và {ASANKHATA}")   # [pi-1 ^1-583 / RUPA_EKADASA words]
RUPA_NN = "vật chất không thấy được và không có tính va chạm, nằm trong lĩnh vực đối tượng của ý"
assert RUPA_NN in S.RUPA_EKADASA
NIBBANA3 = "Sự diệt tận tham đắm, sự diệt tận sân hận, sự diệt tận si mê"   # Rāgakkhayo, dosakkhayo, mohakkhayo [new; pi-1 words]

# ---------------------------------------------------------------- 3. sense-base bodies (pi-1 ^1-596 … ^1-647)


def base_body(bid):
    return between(pi1(bid), "? ", " " + DASH + " vật chất này là")


EYE = repl(base_body("1-596"), " [khác chính tả (Sī., Syā.): cakkhuṃ]",
           " [khác chính tả (Sī., Syā., Ka.): cakkhuṃ; dha. sa. 596-599]")
EAR, NOSE, TONGUE, BODY = (base_body(x) for x in ("1-600", "1-604", "1-608", "1-612"))
FORM = base_body("1-616")
FORM = repl(FORM, "màu đỏ, màu trắng", "màu đỏ [khác chính tả (Sī.): pītaṃ lohitaṃ], màu trắng")
FORM = repl(FORM, " [khác chính tả (Sī., Ka.): caturassaṃ]", "")
FORM = repl(FORM, "[khác chính tả (Sī., Syā.): suriyamaṇḍalassa]", "[khác chính tả (Sī., Syā., Kaṃ.): suriyamaṇḍalassa]")
SOUND = repl(base_body("1-620"), "tiếng trống cơm,", "tiếng trống cơm [khác chính tả (Sī.): mutiṅgasaddho],")
SMELL = base_body("1-624")
TASTE = repl(base_body("1-628"), "vị mặn, vị kiềm, vị chua nhẹ [dị bản (Sī.): lapilakaṃ]",
             "vị mặn [dị bản (Sī.): lapilakaṃ; (Ka., Sī.): lampikaṃ], vị kiềm, vị chua nhẹ")
TOUCH = base_body("1-647")


def base_line(key, body):
    """Tattha katamaṃ X? <body>. Idaṃ vuccati "X"."""
    return f"{q(NAME[key])} {body}. {cap(called(NAME[key]))}."


def short_body(body, cut, tail):
    """Yaṃ cakkhu catunnaṃ mahābhūtānaṃ upādāya pasādo…pe… suñño gāmopeso -> «Mắt là … cơ bản… đây là …»"""
    return body[:body.index(cut)] + "… " + tail


# ---------------------------------------------------------------- 4. chapter 2 Suttanta
IMP = "là vô thường, là khổ đau, không phải là tự ngã, có bản chất biến đổi"   # aniccaṃ dukkhaṃ anattā vipariṇāmadhammaṃ [new]
IMP_SUBJ = {"Cakkhuṃ": "Mắt", "Rūpā": "Các hình sắc", "Sotaṃ": "Tai", "Saddā": "Các âm thanh", "Ghānaṃ": "Mũi",
            "Gandhā": "Các mùi", "Jivhā": "Lưỡi", "Rasā": "Các vị", "Kāyo": "Thân", "Phoṭṭhabbā": "Các vật xúc chạm",
            "Mano": "Ý", "Dhammā": "Các đối tượng của ý"}


def imp_line(t):
    out = []
    for sent in re.split(r"(?<=\.) ", t):
        m = re.match(r"^(\w+) anicc\w+ dukkh\w+ anattā vipariṇāmadhamm\w+\.$", sent)
        out.append(f"{IMP_SUBJ[m.group(1)]} {IMP}.")
    return " ".join(out)


def twelve(order):
    return f"{TWELVE} {DASH} " + listing([AYATANA[k] for k in order]) + "."


ORDER_S = ["cakkhāyatanaṃ", "rūpāyatanaṃ", "sotāyatanaṃ", "saddāyatanaṃ", "ghānāyatanaṃ", "gandhāyatanaṃ",
           "jivhāyatanaṃ", "rasāyatanaṃ", "kāyāyatanaṃ", "phoṭṭhabbāyatanaṃ", "manāyatanaṃ", "dhammāyatanaṃ"]
ORDER_A = ORDER_S[0::2][:5] + ["manāyatanaṃ"] + ORDER_S[1::2][:5] + ["dhammāyatanaṃ"]
ORDER_D = ["cakkhudhātu", "rūpadhātu", "cakkhuviññāṇadhātu", "sotadhātu", "saddadhātu", "sotaviññāṇadhātu",
           "ghānadhātu", "gandhadhātu", "ghānaviññāṇadhātu", "jivhādhātu", "rasadhātu", "jivhāviññāṇadhātu",
           "kāyadhātu", "phoṭṭhabbadhātu", "kāyaviññāṇadhātu", "manodhātu", "dhammadhātu", "manoviññāṇadhātu"]


def eighteen():
    return f"{EIGHTEEN} {DASH} " + listing([DHATU[k] for k in ORDER_D]) + "."


# ---------------------------------------------------------------- 5. chapter 3 Suttanta: elements
def elem_str(bid, end):
    return low(between(pi1(bid), "? ", end))


PATHAVI = repl(elem_str("1-967", ", dù ở nơi bản thân"), " [khác chính tả (Ka.): kharigataṃ]", "")
APO = elem_str("1-726", " " + DASH + " vật chất này")
TEJO = elem_str("1-969", ", dù ở nơi bản thân")
VAYO = elem_str("1-970", ", dù ở nơi bản thân")
AKASA_EXT = elem_str("1-637", " " + DASH + " vật chất này")
AKASA_INT = repl(AKASA_EXT, "bốn yếu tố cơ bản chạm đến", "thịt và máu chạm đến")   # asamphuṭṭhaṃ maṃsalohitehi [new]
APO_VAR = repl(APO, "điều được xem là chất ẩm,", "điều được xem là chất ẩm [khác chính tả (Syā.): sneho snehagataṃ],")

SEYYATHIDAM = "cụ thể là " + DASH        # seyyathidaṃ – [new]
OTHER = "hoặc còn có bất cứ điều gì khác"  # yaṃ vā panaññampi atthi [sample FAR_OTHER words]
INT = "ở nơi bản thân, riêng từng người"   # ajjhattaṃ paccattaṃ [pi-1 SELF words]
INT_END = "ở nơi bản thân, do nghiệp tạo ra"        # ajjhattaṃ upādinnaṃ [pi-1]
EXT = "thuộc phần bên ngoài"                         # bāhiraṃ [pi-1]
EXT_END = "ở bên ngoài bản thân, không do nghiệp tạo ra"   # bahiddhā anupādinnaṃ [pi-1]
FOOD4 = "những gì đã ăn, đã uống, đã nhai, đã nếm"   # asitapītakhāyitasāyitaṃ [new]

LISTS = {
    "pathavi_int": ("tóc, lông, móng, răng, da, thịt, gân [khác chính tả (Sī.): nahāru], xương, "
                    "tủy xương [khác chính tả (Sī.): aṭṭhimiñjā], thận, tim, gan, màng hoành, lá lách, phổi, ruột, "
                    "màng ruột, thức ăn trong dạ dày, phân"),
    "pathavi_ext": ("sắt, đồng, thiếc, chì, bạc [khác chính tả (Syā.): sajjhu], ngọc trai, ngọc quý, ngọc lưu ly, "
                    "vỏ ốc, đá, san hô, bạc, vàng, hồng ngọc [khác chính tả (Syā., Ka.): lohitaṅgo; (?): lohitako], "
                    "ngọc mắt mèo, cỏ, gỗ, sỏi, mảnh sành [khác chính tả (Ka.): kathalaṃ], đất, đá tảng, núi"),
    "apo_int": "mật, đờm, mủ, máu, mồ hôi, mỡ, nước mắt, mỡ lỏng, nước bọt, nước mũi, dịch khớp, nước tiểu",
    "apo_ext": ("nhựa rễ cây, nhựa thân cây, nhựa vỏ cây, nhựa lá, nhựa hoa, nhựa trái cây, sữa, sữa đông, bơ lỏng, "
                "bơ tươi, dầu, mật ong, mật mía, nước trên mặt đất hay nước trên bầu trời"),
    "tejo_int": ("cái làm cho người ta ấm lên, cái làm cho người ta già đi, cái làm cho người ta nóng rực, "
                 f"và cái làm cho {FOOD4} được tiêu hóa đúng cách"),
    "tejo_ext": ("lửa củi, lửa rơm [dị bản (tất cả các ấn bản): sakalikaggi], lửa cỏ, lửa phân bò, lửa trấu, lửa rác, "
                 "lửa sét, sức nóng của lửa, sức nóng của mặt trời, sức nóng của đống củi, sức nóng của đống cỏ, "
                 "sức nóng của đống thóc, sức nóng của đống hàng hóa"),
    "vayo_int": ("gió đi lên, gió đi xuống, gió trong bụng, gió trong ruột [khác chính tả (Sī., Syā.): koṭṭhasayā], "
                 "gió chạy khắp các chi, gió như dao cắt, gió như dao cạo, gió như kim châm, hơi thở vào, hơi thở ra, "
                 "hay những thứ như thế"),
    "vayo_ext": ("gió đông, gió tây, gió bắc, gió nam, gió có bụi, gió không bụi, gió lạnh, gió nóng, gió nhẹ, "
                 "gió mạnh, gió bão, gió trên tầng cao, gió do cánh chim, gió do chim thần Ga-ru-đa, "
                 "gió từ quạt lá cọ, gió từ quạt tay"),
    "akasa_int": (f"lỗ tai, lỗ mũi, cửa miệng, chỗ mà qua đó {FOOD4} được nuốt vào, chỗ mà ở đó {FOOD4} nằm lại, "
                  f"chỗ mà qua đó {FOOD4} thoát ra ở phần dưới"),
}


def int_part(name, x1, x2, lst):
    """Tattha katamā ajjhattikā X? Yaṃ ajjhattaṃ paccattaṃ <x> ajjhattaṃ upādinnaṃ, seyyathidaṃ – <list>,
    yaṃ vā panaññampi atthi ajjhattaṃ paccattaṃ <x> ajjhattaṃ upādinnaṃ – ayaṃ vuccati ‘ajjhattikā X’."""
    n = f"{name} {B.P('ajjhattika')}"
    return (f"{q(n)} Điều mà {INT}, là {x1}, {INT_END}, {SEYYATHIDAM} {lst}, {OTHER} {INT}, là {x2}, {INT_END} "
            f"{DASH} {called(n)}.")


def ext_part(name, x, lst):
    n = f"{name} {B.P('bahira')}"
    body = f"Điều mà {EXT}, là {x}, {EXT_END}"
    if lst:
        body += f", {SEYYATHIDAM} {lst}, {OTHER} {EXT}, là {x}, {EXT_END}"
    return f"{q(n)} {body} {DASH} {called(n)}."


def elem_lines(key, x_int, x_int2, x_ext, lst_int, lst_ext):
    name = DHATU[key]
    two = f"{cap(name)} có hai loại {DASH} {B.ATTHI} {B.P('ajjhattika')}, {B.ATTHI} {B.P('bahira')}."   # Xdvayaṃ – atthi ajjhattikā, atthi bāhirā
    together = (f"{cap(name)} {B.P('ajjhattika')} và {name} {B.P('bahira')}, {TOGETHER} {DASH} {called(name)}.")
    return [f"{q(name)} {two} {int_part(name, x_int, x_int2, lst_int)}",
            f"{ext_part(name, x_ext, lst_ext)} {together}"]


# feelings (pi-1 ^1-445, ^1-558, ^1-3, ^1-415, ^1-152 without the «tajjā…» phrase)
TAJJA_K = " sinh từ sự tiếp xúc của yếu tố thức qua thân tương ứng"
TAJJA_M = " sinh từ sự tiếp xúc của yếu tố ý thức tương ứng"


def feel_body(bid, tajja):
    s = between(pi1(bid), "Điều mà vào lúc ấy là ", " " + DASH + " đó là cảm giác vào lúc ấy")
    return repl(s, tajja, "")


AVIJJA = between(pi1("1-390"), "Điều mà vào lúc ấy là ", " " + DASH + " đó là sự si mê vào lúc ấy")
VITAKKA7 = between(pi1("1-7"), "Điều mà vào lúc ấy là ", " " + DASH)   # suy nghĩ, sự hướng tâm, …, tư duy đúng đắn
assert VITAKKA7.endswith(", tư duy đúng đắn")
VIT6 = VITAKKA7[:-len(", tư duy đúng đắn")]
RIGHT, WRONG = "tư duy đúng đắn", "tư duy sai lầm"   # sammā / micchāsaṅkappo [pi-1 ^1-7, ^1-365]
assert "có " + WRONG in pi1("1-365")


def vitakka(conn, last, full=True):
    """Xpaṭisaṃyutto takko vitakko saṅkappo … micchā/sammāsaṅkappo  (…pe… when not full)"""
    first, rest = VIT6.split(", ", 1)
    if full:
        return f"{cap(first)} liên quan đến {conn}, {rest}, {last}"
    return f"{cap(first)} liên quan đến {conn}, {rest.split(', ')[0]}… {last}"


KAMA_REALM = repl(between(pi1("1-1287"), "? ", " " + DASH + " những hiện tượng này"),
                  " [khác chính tả (Sī., Ka.): paranimmitavasavattideve]", "")
KAMA_REALM = repl(KAMA_REALM, "tức vật chất,", "tức vật chất [dị bản (Syā.): rūpaṃ],")
DOSA = between(pi1("1-1066"), "Điều mà thuộc loại như vậy là ", " " + DASH + " đó được gọi là sự sân hận")
DOSA = repl(DOSA, "sự khởi thù hằn, trạng thái khởi thù hằn, ", "sự khởi thù hằn, ")   # pi-2 has no byāpajjitattaṃ
METTA3 = "lòng từ ái, sự khởi lòng từ ái, trạng thái khởi lòng từ ái"   # metti mettāyanā mettāyitattaṃ [pi-1 ^1-1062]
assert METTA3 in pi1("1-1062")
KARUNA3 = "lòng trắc ẩn, sự khởi lòng trắc ẩn, trạng thái khởi lòng trắc ẩn"   # [new, same pattern; karuṇā pi-1]
CETOVIMUTTI = "sự giải thoát của tâm nhờ"   # Xcetovimutti [new]
IDHEKACCO = "Ở đời này, có người"            # [pi-1 ^1-1355]
assert pi1("1-1355").count(IDHEKACCO) == 1
SIX = "Đây là sáu yếu tố."                     # Imā cha dhātuyo. [new]
SIX_MORE = "Thêm sáu yếu tố khác"              # Aparāpi cha dhātuyo [new]

# ---------------------------------------------------------------- 6. chapter 3 Abhidhamma: consciousness
CITTA10 = between(pi1("1-6"), "Điều mà vào lúc ấy là ", ", yếu tố ý thức tương ứng")   # cittaṃ mano … viññāṇakkhandho
CITTA3 = ", ".join(CITTA10.split(", ")[:3])     # cittaṃ mano mānasaṃ…pe…


def arises(dhatu_vi):
    """uppajjati cittaṃ mano … viññāṇakkhandho tajjā-X"""
    return f"sinh khởi {CITTA10}, {dhatu_vi} tương ứng"


def after(x):
    """X-dhātuyā uppajjitvā niruddhasamanantarā  [new]"""
    return f"ngay sau khi {x} đã sinh khởi rồi chấm dứt"


def vinnana_line(d):
    obj = {"cakkhu": "rūpa", "sota": "sadda", "ghāna": "gandha", "jivhā": "rasa", "kāya": "phoṭṭhabba"}[d]
    n = DHATU[d + "viññāṇadhātu"]
    return (f"{q(n)} Tùy thuộc vào {DOOR[d]} và các {OBJ[obj]} mà {arises(n)} {DASH} {called(n)}.")


def mano_dhatu_line():
    m = DHATU["manodhātu"]
    mid = " ".join(f"ngay sau khi {DHATU[d + 'viññāṇadhātu']}…" for d in ("sota", "ghāna", "jivhā"))
    return (f"{q(m)} {cap(after(DHATU['cakkhuviññāṇadhātu']))}, {arises(m)}; {mid} "
            f"{after(DHATU['kāyaviññāṇadhātu'])}, {arises(m)}, hoặc đối với mọi hiện tượng, sinh khởi "
            f"sự lưu ý đầu tiên, tức {CITTA10}, {m} tương ứng {DASH} {called(m)}.")


def mano_vinnana_line():
    m, mv = DHATU["manodhātu"], DHATU["manoviññāṇadhātu"]
    short = f"sinh khởi {CITTA3}… {mv} tương ứng"
    mid = " ".join(f"ngay sau khi {DHATU[d + 'viññāṇadhātu']}…" for d in ("sota", "ghāna", "jivhā"))
    return (f"{q(mv)} {cap(after(DHATU['cakkhuviññāṇadhātu']))}, sinh khởi {m}, {after(m)}, {short}; {mid} "
            f"{after(DHATU['kāyaviññāṇadhātu'])}, sinh khởi {m}, ngay sau khi cả {m} cũng đã sinh khởi rồi chấm dứt, "
            f"{short}; tùy thuộc vào ý và các đối tượng của ý mà {arises(mv)} {DASH} {called(mv)}.")


# ---------------------------------------------------------------- 7. Abhidhammabhājanīya classification lines
SURF = dict(B.SURF)
ITEMS = dict(B.ITEMS)


def item(key, surfaces, p):
    ITEMS[key] = dict(p=p, s=p)
    for x in surfaces:
        assert x not in SURF, x
        SURF[x] = key


item("appaccaya", ["appaccayā", "appaccayaṃ"], "không có điều kiện")                 # [new; pi-1 sappaccaya]
item("asankhata", ["asaṅkhatā", "asaṅkhataṃ"], ASANKHATA[len("yếu tố "):])          # [pi-1]
# as written in the Pāli (reported): upādāniyañceva upādānasampayuttañca; upādānasampayuttaupādāniyā
item("upadana_niya_samp", ["upādāniyo ceva upādānasampayutto ca"],
     "vừa là đối tượng của sự bám víu vừa gắn liền với sự bám víu")
item("upadana_samp_niya", ["upādānasampayuttaupādāniyo"],
     "gắn liền với sự bám víu và là đối tượng của sự bám víu")
# slips rendered as meant (reported)
SLIP_ALIAS = {"na hetūahetukā": "nahetu_ahetuka", "kilesasampayuttā ceva no ca na kilesā": "kilesa_samp_notN",
              "saṃyojanañceva saṃyojaniyaṃ": "samyojana_N_niya", "ahetu": "na_hetu"}
SURF.update(SLIP_ALIAS)

KEEP = {"na", "no", "neva", "ca", "ceva", "vā"}
SUFFIX = (("inī", "i"), ("ino", "i"), ("uno", "u"), ("ī", "i"), ("ū", "u"), ("aṃ", "#"), ("o", "#"), ("ā", "#"))


def canon(s):
    """One form for every gender / number / sandhi variant of a matrix-item surface."""
    s = re.sub(r"ñ(ceva|ca)\b", r"ṃ \1", s)
    out = []
    for w in s.split(" "):
        if w not in KEEP:
            for suf, rep in SUFFIX:
                if w.endswith(suf) and len(w) > len(suf) + 1:
                    w = w[:-len(suf)] + rep
                    break
        out.append(w)
    return " ".join(out)


CANON = {}
for _s, _k in SURF.items():
    _c = canon(_s)
    assert CANON.get(_c, _k) == _k, ("canon collision", _s, _c, CANON[_c], _k)
    CANON[_c] = _k
UNUSED = set(SURF)


def key_of(surface):
    UNUSED.discard(surface)
    if surface in SURF:
        return SURF[surface]
    k = CANON[canon(surface)]
    for s2, k2 in SURF.items():
        if k2 == k and canon(s2) == canon(surface):
            UNUSED.discard(s2)
    return k


ATTHI_N = dict(B.ATTHI_N)
BARE = {"phassasampayutto": "gắn liền với sự tiếp xúc", "phassasampayuttaṃ": "gắn liền với sự tiếp xúc",
        "cittasampayutto": "gắn liền với tâm"}
FSUBJ = {"manāyatanaṃ": AYATANA["manāyatanaṃ"]}
for _pa, _a in B.AGG_PALI.items():
    FSUBJ[_pa + "kkhandho"] = S.AGG[_a]["khandha"]
_FS = "|".join(map(re.escape, sorted(FSUBJ, key=len, reverse=True)))
FRAME = re.compile(r"^(Aparopi )?(\w+?)[vb]idhena (" + _FS + ")")
CLOSE = re.compile(r"^([Ee])vaṃ (\w+?)[vb]idhena (" + _FS + ")$")
PE = B.PE
SLIPS = []


def fopen(subj, n):
    """Ekavidhena X  ->  Phân loại X theo nhóm một (B.frame_open, any subject)"""
    return f"Phân loại {FSUBJ[subj]} " + B.by_groups(B.NUMKEY[n.lower()])


def fclose(subj, n):
    return f"Như vậy là phân loại {FSUBJ[subj]} " + B.by_groups(B.NUMKEY[n.lower()])


for _a in S.AGG:   # identical to the approved frames
    _k = [k for k, v in B.AGG_PALI.items() if v == _a][0] + "kkhandho"
    assert fopen(_k, "Du") == B.frame_open(_a, 2) and fclose(_k, "dasa") == B.frame_close(_a, 10)


def atthi_pred(surface):
    if surface in ATTHI_N:
        return ATTHI_N[surface]
    return ITEMS[key_of(surface)]["p"]


def chunk_abhi(c):
    m = CLOSE.match(c)
    if m:
        vi = fclose(m.group(3), m.group(2))
        return (vi if m.group(1) == "E" else low(vi)), False
    if low(c) in B.SUBJ:
        return cap(B.SUBJ[low(c)]) if c[:1].isupper() else B.SUBJ[low(c)], False
    if c in BARE:
        return BARE[c], False
    m = re.match(r"^()[Aa]tthi (.+)$", c) or re.match(r"^(.*?) atthi (.+)$", c)
    if not m:
        raise KeyError("abhi chunk: " + c)
    subj, preds = m.group(1), m.group(2).split(" atthi ")
    body = ", ".join(f"{B.ATTHI} {atthi_pred(x)}" for x in preds)
    vi = f"{B.SUBJ[subj]}: {body}" if subj else body
    return (cap(vi) if c[:1].isupper() else vi), True


def body_abhi(body):
    body = body.replace(" …pe…", "…pe…").replace("…pe…", PE)
    parts = re.split(r"(\x01\.? ?|, |; |\. |\.$)", body)
    out, prev = [], False
    for i, x in enumerate(parts):
        if i % 2:
            out.append(B.sep_vi(x))
        elif x:
            vi, atthi = chunk_abhi(x)
            if out and out[-1] == ", " and prev and not atthi:
                out[-1] = "; "
            out.append(vi)
            prev = atthi
    return "".join(out)


ANS_RE = re.compile(r'^(.*) ' + DASH + r' (?:ayaṃ|idaṃ) vuccati "([^"]+)"\.$')
ANS_ALONE = re.compile(r'^(?:Ayaṃ|Idaṃ) vuccati "([^"]+)"\.$')


def abhi_sent(x):
    m = ANS_ALONE.match(x)
    if m:
        return cap(called(NAME[m.group(1)])) + "."
    tail = ""
    m = ANS_RE.match(x)
    if m:
        x, tail = m.group(1), f" {DASH} {called(NAME[m.group(2)])}."
    m = CLOSE.match(x.rstrip("."))
    if m and not FRAME.match(x):
        return fclose(m.group(3), m.group(2)) + ("." if x.endswith(".") else "") + tail
    m = FRAME.match(x)
    if not m:
        raise KeyError("abhi sentence: " + x[:80])
    vi = ("Một cách khác để p" + fopen(m.group(3), m.group(2))[1:]) if m.group(1) else fopen(m.group(3), m.group(2))
    rest = x[m.end():]
    assert rest.startswith(" " + DASH + " "), rest[:40]
    return vi + f" {DASH} " + body_abhi(rest[3:]) + tail


def abhi_line(t):
    pre = ""
    m = re.match(r"^Tattha katam(?:o|aṃ) (\w+)\? ", t)
    if m and m.group(1) in FSUBJ:
        pre, t = q(FSUBJ[m.group(1)]) + " ", t[m.end():]
    return pre + " ".join(abhi_sent(s) for s in re.split(r"(?<=\.) (?=[A-Z])", t))


# ---------------------------------------------------------------- 8. Pañhāpucchaka (B.line_q method)
NUMW = {"Dasa": "Mười", "Dve": "Hai", "Pañca": "Năm", "Cha": "Sáu", "Satta": "Bảy", "Aṭṭha": "Tám", "Nava": "Chín",
        "Tisso": "Ba", "Ekādasa": "Mười một", "Dvādasa": "Mười hai", "Pannarasa": "Mười lăm", "Soḷasa": "Mười sáu",
        "Sattarasa": "Mười bảy"}
SUBJECTS = {"Dasāyatanā": "Mười lĩnh vực", "Dvāyatanā": "Hai lĩnh vực", "Pañcāyatanā": "Năm lĩnh vực",
            "Cattāro āyatanā": "Bốn lĩnh vực", "Ekādasāyatanā": "Mười một lĩnh vực", "Navāyatanā": "Chín lĩnh vực",
            "Chāyatanā": "Sáu lĩnh vực"}
for _k in ("Manāyatanaṃ", "Dhammāyatanaṃ", "Saddāyatanaṃ", "Rūpāyatanaṃ"):
    SUBJECTS[_k] = cap(AYATANA[low(_k)])
for _n, _v in NUMW.items():
    SUBJECTS[f"{_n} dhātuyo"] = f"{_v} yếu tố"
SUBJECTS["Sattadhātuyo"] = "Bảy yếu tố"   # spacing slip in the Pāli (reported)
for _k in ("Kāyaviññāṇadhātu", "Manoviññāṇadhātu", "Dhammadhātu", "Manodhātu", "Saddadhātu", "Rūpadhātu"):
    SUBJECTS[_k] = cap(DHATU[low(_k)])
SUBJ_RE = re.compile(r"^(" + "|".join(map(re.escape, sorted(SUBJECTS, key=len, reverse=True))) + r") (.+)$")
QUOTE_RE = B.QUOTE_RE
BODY_SUKHA = B.ATTHI_N["sukhasahagatā"]   # body context: «có sự dễ chịu đi kèm» (notes-1; APPROVED sukha decision)


def pred_vi(surface, state):
    k = key_of(surface)
    if state.get("body") and k == "sukhasahagata":
        return BODY_SUKHA
    return ITEMS[k]["s"]


def quoted(qq, n, state):
    qq = qq + ("ṃ" if n else "")
    qq = re.sub(r"cā$", "ca", qq)
    k = key_of(qq)
    p = BODY_SUKHA if (state.get("body") and k == "sukhasahagata") else ITEMS[k]["p"]
    return "“" + p + "”"


def chunk_q(c, state):
    subj = ""
    m = SUBJ_RE.match(c)
    if m:
        subj, c = SUBJECTS[m.group(1)], m.group(2)
    m = re.match(r"^(siyā )?na vattabb(?:o|ā|aṃ) " + DASH + r" (.+)$", c)
    if m:
        qm = QUOTE_RE.match(m.group(2))
        vi = f"{B.NV} {quoted(qm.group(1), qm.group(2), state)}"
        if m.group(1):
            vi = f"{B.SOMETIMES} {vi}"
        elif subj:
            vi = f"{S.THI} {vi}"
        state["nv"] = True
    elif QUOTE_RE.match(c):
        qm = QUOTE_RE.match(c)
        vi = f"{B.OR} {quoted(qm.group(1), qm.group(2), state)}"
        state["nv"] = True
    else:
        if re.match(r'^"[^"]*"$', c):
            SLIPS.append("quoted affirmative without ti: " + c)
            c = c[1:-1]
        if c.startswith("siyā "):
            vi = f"{B.SOMETIMES} {pred_vi(c[5:], state)}"
        else:
            vi = pred_vi(c, state)
            if state.get("nv"):
                vi = "mà " + vi
        state["nv"] = False
    return f"{subj} {vi}" if subj else vi


FIXES = ((DASH + ' "parāmāsā ceva parāmaṭṭhā cāti parāmaṭṭhā ceva no ca parāmāsā"',
          DASH + ' "parāmāsā ceva parāmaṭṭhā cā"ti, "parāmaṭṭhā ceva no ca parāmāsā"'),
         ("siyā araṇāti.", "siyā araṇā."))


def line_q(t):
    for a, b in FIXES:
        if a in t:
            SLIPS.append("punctuation: " + a)
            t = t.replace(a, b)
    out = []
    for sent in re.split(r"(?<=\.) (?=[A-ZĀ])", t):
        assert sent.endswith("."), sent[-40:]
        body = sent[:-1].replace("…pe…", PE)
        parts = re.split(r"(, |; |\x01 ?)", body)
        state = {"body": sent.startswith("Kāyaviññāṇadhātu ")}
        vi = []
        for i, x in enumerate(parts):
            if i % 2:
                vi.append(B.sep_vi(x))
                if x.startswith(PE) or x == "; ":
                    state["nv"] = False
            else:
                vi.append(chunk_q(x, state))
        out.append(cap("".join(vi)) + ".")
    return " ".join(out)


def question_q(total, unit):
    """Dvādasannaṃ āyatanānaṃ kati kusalā …? (B.LABELS frame)"""
    P = B.P
    return (f"Trong {total}, bao nhiêu {unit} {P('kusala')}, bao nhiêu {unit} {P('akusala')}, "
            f"bao nhiêu {unit} {P('abyakata')}… bao nhiêu {unit} {P('sarana')}, bao nhiêu {unit} {P('arana')}?")


# ---------------------------------------------------------------- 9. labels and hand lines
SEC = S.SECTION_TITLES
LABELS = {
    "#### Suttantabhājanīyaṃ": "#### " + SEC["Suttantabhājanīyaṃ"],
    "#### Abhidhammabhājanīyaṃ": "#### " + SEC["Abhidhammabhājanīyaṃ"],
    "#### Pañhāpucchakaṃ": "#### " + SEC["Pañhāpucchakaṃ"],
    "Suttantabhājanīyaṃ.": SEC["Suttantabhājanīyaṃ"] + ".",
    "Abhidhammabhājanīyaṃ.": SEC["Abhidhammabhājanīyaṃ"] + ".",
    "Pañhāpucchakaṃ.": SEC["Pañhāpucchakaṃ"] + ".",
    "##### Tikaṃ": B.LABELS["##### Tikaṃ"],
    "##### Dukaṃ": B.LABELS["##### Dukaṃ"],
    "### Āyatanavibhaṅgo": "### " + S.CHAPTER_TITLES[2],
    "### Dhātuvibhaṅgo": "### " + S.CHAPTER_TITLES[3],
    "Āyatanavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[2]),
    "Dhātuvibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[3]),
    "Dvādasannaṃ āyatanānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        question_q(low(TWELVE), "lĩnh vực"),
    "Aṭṭhārasannaṃ dhātūnaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        question_q(low(EIGHTEEN), "yếu tố"),
    "Imā cha dhātuyo.": SIX,
}

dhamma_q = {"āyatana": q(AYATANA["dhammāyatanaṃ"]), "dhātu": q(DHATU["dhammadhātu"])}
RUPA_NN_Q = f"{TATTHA} {RUPA_NN}, là gì?"   # Tattha katamaṃ rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ?
RUPA_NN_A = f"{VUCCATI} vật chất “{RUPA_NN[len('vật chất '):]}”"   # idaṃ vuccati rūpaṃ "…"
ASANKHATA_LINE = f"{q(ASANKHATA)} {NIBBANA3} {DASH} {called(ASANKHATA)}."
FEM_TO_FOOD = S.FEMININITY_TO_FOOD.replace("Năng lực nữ tính…", "Năng lực nữ tính, năng lực nam tính…")

HAND2 = [
    ("Dvādasāyatanāni – cakkhāyatanaṃ, rūpāyatanaṃ", twelve(ORDER_S)),
    ("Cakkhuṃ aniccaṃ", None),   # imp_line
    ("Dvādasāyatanāni – cakkhāyatanaṃ, sotāyatanaṃ", twelve(ORDER_A)),
    ("Tattha katamaṃ cakkhāyatanaṃ?", base_line("cakkhāyatanaṃ", EYE)),
    ("Tattha katamaṃ sotāyatanaṃ?", base_line("sotāyatanaṃ", EAR)),
    ("Tattha katamaṃ ghānāyatanaṃ?", base_line("ghānāyatanaṃ", NOSE)),
    ("Tattha katamaṃ jivhāyatanaṃ?", base_line("jivhāyatanaṃ", TONGUE)),
    ("Tattha katamaṃ kāyāyatanaṃ?", base_line("kāyāyatanaṃ", BODY)),
    ("Tattha katamaṃ rūpāyatanaṃ?", base_line("rūpāyatanaṃ", FORM)),
    ("Tattha katamaṃ saddāyatanaṃ?", base_line("saddāyatanaṃ", SOUND)),
    ("Tattha katamaṃ gandhāyatanaṃ?", base_line("gandhāyatanaṃ", SMELL)),
    ("Tattha katamaṃ rasāyatanaṃ?", base_line("rasāyatanaṃ", TASTE)),
    ("Tattha katamaṃ phoṭṭhabbāyatanaṃ?", base_line("phoṭṭhabbāyatanaṃ", TOUCH)),
    ("Tattha katamaṃ dhammāyatanaṃ?", f"{dhamma_q['āyatana']} {DHAMMA_MEMBERS}."),
    ("Tattha katamaṃ rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ? Itthindriyaṃ purisindriyaṃ",
     f"{RUPA_NN_Q} {FEM_TO_FOOD}. {cap(RUPA_NN_A)}."),
    ("Tattha katamā asaṅkhatā dhātu?", ASANKHATA_LINE),
    ("Idaṃ vuccati dhammāyatanaṃ.", cap(called(AYATANA["dhammāyatanaṃ"], quoted=False)) + "."),
    ("Dvādasāyatanāni – cakkhāyatanaṃ, rūpāyatanaṃ", twelve(ORDER_S)),
]

E = DHATU
HAND3 = [
    ("Cha dhātuyo – pathavīdhātu", f"Sáu yếu tố {DASH} " + listing(
        [E["pathavīdhātu"] + " [khác chính tả (Sī., Syā.): paṭhavīdhātu; cũng vậy ở các chỗ sau]"]
        + [E[k] for k in ("āpodhātu", "tejodhātu", "vāyodhātu", "ākāsadhātu", "viññāṇadhātu")]) + "."),
    ("Tattha katamā pathavīdhātu?", None), ("Tattha katamā bāhirā pathavīdhātu?", None),
    ("Tattha katamā āpodhātu?", None), ("Tattha katamā bāhirā āpodhātu?", None),
    ("Tattha katamā tejodhātu?", None), ("Tattha katamā bāhirā tejodhātu?", None),
    ("Tattha katamā vāyodhātu?", None), ("Tattha katamā bāhirā vāyodhātu?", None),
    ("Tattha katamā ākāsadhātu?", None), ("Tattha katamā bāhirā ākāsadhātu?", None),
    ("Tattha katamā viññāṇadhātu?", f"{q(E['viññāṇadhātu'])} "
     + cap(", ".join(E[d + "viññāṇadhātu"] for d in ("cakkhu", "sota", "ghāna", "jivhā", "kāya")))
     + f", {E['manoviññāṇadhātu']} {DASH} {called(E['viññāṇadhātu'])}."),
    ("Aparāpi cha dhātuyo – sukhadhātu", f"{SIX_MORE} {DASH} " + listing(
        [E[k] for k in ("sukhadhātu", "dukkhadhātu", "somanassadhātu", "domanassadhātu", "upekkhādhātu",
                        "avijjādhātu")]) + "."),
    ("Tattha katamā sukhadhātu?", f"{q(E['sukhadhātu'])} Điều mà là {feel_body('1-445', TAJJA_K)} {DASH} "
     f"{called(E['sukhadhātu'])}."),
    ("Tattha katamā dukkhadhātu?", f"{q(E['dukkhadhātu'])} Điều mà là {feel_body('1-558', TAJJA_K)} {DASH} "
     f"{called(E['dukkhadhātu'])}."),
    ("Tattha katamā somanassadhātu?", f"{q(E['somanassadhātu'])} Điều mà là {feel_body('1-3', TAJJA_M)} {DASH} "
     f"{called(E['somanassadhātu'])}."),
    ("Tattha katamā domanassadhātu?", f"{q(E['domanassadhātu'])} Điều mà là {feel_body('1-415', TAJJA_M)} {DASH} "
     f"{called(E['domanassadhātu'])}."),
    ("Tattha katamā upekkhādhātu?", f"{q(E['upekkhādhātu'])} Điều mà là {feel_body('1-152', TAJJA_M)} {DASH} "
     f"{called(E['upekkhādhātu'])}."),
    ("Tattha katamā avijjādhātu?", f"{q(E['avijjādhātu'])} Điều mà là {AVIJJA} {DASH} {called(E['avijjādhātu'])}."),
    ("Aparāpi cha dhātuyo – kāmadhātu", f"{SIX_MORE} {DASH} " + listing(
        [E[k] for k in ("kāmadhātu", "byāpādadhātu", "vihiṃsādhātu", "nekkhammadhātu", "abyāpādadhātu",
                        "avihiṃsādhātu")]) + "."),
    ("Tattha katamā kāmadhātu?", f"{q(E['kāmadhātu'])} {vitakka('dục lạc', WRONG)} {DASH} "
     f"{called(E['kāmadhātu'], quoted=False)}. {KAMA_REALM} {DASH} {called(E['kāmadhātu'])}."),
    ("Tattha katamā byāpādadhātu?", f"{q(E['byāpādadhātu'])} {vitakka('ác ý', WRONG, False)} {DASH} "
     f"{called(E['byāpādadhātu'])}. Hoặc đối với mười căn cứ của sự oán giận, {DOSA} {DASH} "
     f"{called(E['byāpādadhātu'])}."),
    ("Tattha katamā vihiṃsādhātu?", f"{q(E['vihiṃsādhātu'])} {vitakka('sự hãm hại', WRONG, False)} {DASH} "
     f"{called(E['vihiṃsādhātu'])}. {IDHEKACCO} quấy hại chúng sinh bằng tay, bằng cục đất, bằng gậy, "
     "bằng vũ khí, bằng dây thừng hoặc bằng thứ này hay thứ khác, điều mà thuộc loại như vậy là sự quấy hại, "
     "sự quấy hại nặng nề, sự làm hại, sự hãm hại, sự làm khổ, sự làm khổ nặng nề, sự gây hại cho người khác "
     f"{DASH} {called(E['vihiṃsādhātu'])}."),
    ("Tattha katamā nekkhammadhātu?", f"{q(E['nekkhammadhātu'])} {vitakka('sự từ bỏ', RIGHT, False)} {DASH} "
     f"{called(E['nekkhammadhātu'])}. Tất cả các hiện tượng thiện cũng là “{E['nekkhammadhātu']}”."),
    ("Tattha katamā abyāpādadhātu?", f"{q(E['abyāpādadhātu'])} {vitakka('sự không ác ý', RIGHT, False)} {DASH} "
     f"{called(E['abyāpādadhātu'])}. Điều mà là {METTA3.replace('lòng từ ái', 'lòng từ ái đối với chúng sinh', 1)}, "
     f"{CETOVIMUTTI} lòng từ ái {DASH} {called(E['abyāpādadhātu'])}."),
    ("Tattha katamā avihiṃsādhātu?", f"{q(E['avihiṃsādhātu'])} {vitakka('sự không hãm hại', RIGHT)} {DASH} "
     f"{called(E['avihiṃsādhātu'])}. Điều mà là "
     f"{KARUNA3.replace('lòng trắc ẩn', 'lòng trắc ẩn đối với chúng sinh', 1)}, {CETOVIMUTTI} lòng trắc ẩn {DASH} "
     f"{called(E['avihiṃsādhātu'])}."),
    ("Iti imāni tīṇi chakkāni", f"Như vậy, ba nhóm sáu này, {TOGETHER}, thành mười tám yếu tố."),
    ("Aṭṭhārasa dhātuyo – cakkhudhātu", eighteen()),
    ("Tattha katamā cakkhudhātu?", f"{q(E['cakkhudhātu'])} "
     f"{short_body(repl(base_body('1-596'), ' [khác chính tả (Sī., Syā.): cakkhuṃ]', ''), ', nằm trong', 'đây là ngôi làng trống rỗng')} "
     f"{DASH} {called(E['cakkhudhātu'])}."),
    ("Tattha katamā rūpadhātu?", f"{q(E['rūpadhātu'])} "
     f"{short_body(FORM, ', thấy được', 'đây là yếu tố hình sắc')} {DASH} {called(E['rūpadhātu'])}."),
    ("Tattha katamā cakkhuviññāṇadhātu?", vinnana_line("cakkhu")),
    ("Tattha katamā sotadhātu?", f"{q(E['sotadhātu'])} "
     f"{short_body(EAR, ', nằm trong', 'đây là ngôi làng trống rỗng')} {DASH} {called(E['sotadhātu'])}."),
    ("Tattha katamā saddadhātu?", f"{q(E['saddadhātu'])} "
     f"{short_body(SOUND, ', như tiếng', 'đây là yếu tố âm thanh')} {DASH} {called(E['saddadhātu'])}."),
    ("Tattha katamā sotaviññāṇadhātu?", vinnana_line("sota")),
    ("Tattha katamā ghānadhātu?", f"{q(E['ghānadhātu'])} "
     f"{short_body(NOSE, ', nằm trong', 'đây là ngôi làng trống rỗng')} {DASH} {called(E['ghānadhātu'])}."),
    ("Tattha katamā gandhadhātu?", f"{q(E['gandhadhātu'])} "
     f"{short_body(SMELL, ', như mùi', 'đây là yếu tố mùi')} {DASH} {called(E['gandhadhātu'])}."),
    ("Tattha katamā ghānaviññāṇadhātu?", vinnana_line("ghāna")),
    ("Tattha katamā jivhādhātu?", f"{q(E['jivhādhātu'])} "
     f"{short_body(TONGUE, ', nằm trong', 'đây là ngôi làng trống rỗng')} {DASH} {called(E['jivhādhātu'])}."),
    ("Tattha katamā rasadhātu?", f"{q(E['rasadhātu'])} "
     f"{short_body(TASTE, ', như vị', 'đây là yếu tố vị')} {DASH} {called(E['rasadhātu'])}."),
    ("Tattha katamā jivhāviññāṇadhātu?", vinnana_line("jivhā")),
    ("Tattha katamā kāyadhātu?", f"{q(E['kāyadhātu'])} "
     f"{short_body(BODY, ', nằm trong', 'đây là ngôi làng trống rỗng')} {DASH} {called(E['kāyadhātu'])}."),
    ("Tattha katamā phoṭṭhabbadhātu?", f"{q(E['phoṭṭhabbadhātu'])} "
     f"{short_body(TOUCH, ', yếu tố lửa', 'đây là yếu tố vật xúc chạm')} {DASH} {called(E['phoṭṭhabbadhātu'])}."),
    ("Tattha katamā kāyaviññāṇadhātu?", vinnana_line("kāya")),
    ("Tattha katamā manodhātu?", mano_dhatu_line()),
    ("Tattha katamā dhammadhātu?", f"{dhamma_q['dhātu']} {DHAMMA_MEMBERS}."),
    ("Tattha katamaṃ rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ? Itthindriyaṃ…pe…",
     f"{RUPA_NN_Q} {S.FEMININITY_TO_FOOD} {DASH} {RUPA_NN_A}."),
    ("Tattha katamā asaṅkhatā dhātu?", ASANKHATA_LINE + " " + cap(called(E["dhammadhātu"])) + "."),
    ("Tattha katamā manoviññāṇadhātu?", mano_vinnana_line()),
    ("Aṭṭhārasa dhātuyo – cakkhudhātu", eighteen()),
]
ELEM = {   # key -> (internal X 1st, internal X 2nd, external X, internal list, external list)
    "pathavīdhātu": (PATHAVI, PATHAVI, PATHAVI, LISTS["pathavi_int"], LISTS["pathavi_ext"]),
    "āpodhātu": (APO_VAR, APO, APO, LISTS["apo_int"], LISTS["apo_ext"]),
    "tejodhātu": (TEJO, TEJO, TEJO, LISTS["tejo_int"], LISTS["tejo_ext"]),
    "vāyodhātu": (VAYO, VAYO, VAYO, LISTS["vayo_int"], LISTS["vayo_ext"]),
    "ākāsadhātu": (AKASA_INT, AKASA_INT, AKASA_EXT, LISTS["akasa_int"], None),
}
_EL = {}
for _k, _v in ELEM.items():
    _a, _b = elem_lines(_k, *_v)
    _EL[f"Tattha katamā {_k}?"] = _a
    _EL[f"Tattha katamā bāhirā {_k}?"] = _b
HAND3 = [(p, _EL[p] if v is None else v) for p, v in HAND3]
HAND2 = [(p, v) for p, v in HAND2]


# ---------------------------------------------------------------- 10. build
def translate(pali_lines, hand):
    hand = list(hand)
    out, section = [], "sutta"
    for pl in pali_lines:
        if not pl.strip():
            out.append("")
            continue
        m = S.ID.search(pl)
        t = S.ID.sub("", pl).rstrip()
        if t.startswith("#### Pañhāpucchakaṃ"):
            section = "q"
        if t in LABELS:
            vi = LABELS[t]
        elif t.startswith("Cakkhuṃ aniccaṃ"):
            vi = imp_line(t)
            hand = [h for h in hand if h[0] != "Cakkhuṃ aniccaṃ"]
        elif hand and t.startswith(hand[0][0]):
            vi = hand.pop(0)[1]
        elif section == "q":
            vi = line_q(t)
        else:
            vi = abhi_line(t)
        assert pl.count(DASH) + pl.count("—") == vi.count(DASH) and "—" not in vi, ("dash count", t[:70], vi[:90])
        for bad in ("là là", "  ", "….", '"', " ,", " .", ":-"):
            assert bad not in vi, (bad, vi[:120])
        out.append(vi + (" " + m.group(1) if m else ""))
    assert not hand, [h[0] for h in hand]
    return out


CHAPTERS = (("2-ayatanavibhango.md", HAND2), ("3-dhatuvibhango.md", HAND3))


def build():
    res = {}
    for fn, hand in CHAPTERS:
        pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().rstrip("\n").split("\n")
        res[os.path.join(S.VI_DIR, fn)] = translate(pali, hand)
    return res


def main():
    res = build()
    for path, lines in res.items():
        text = "\n".join(lines).rstrip("\n") + "\n"
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("OK:", path, "|", len([l for l in lines if l.strip()]), "non-empty lines")
    for s in sorted(set(SLIPS)):
        print("slip:", s)
    if "--unused" in sys.argv:
        print("unused surfaces:", sorted(UNUSED)[:50])


if __name__ == "__main__":
    main()
