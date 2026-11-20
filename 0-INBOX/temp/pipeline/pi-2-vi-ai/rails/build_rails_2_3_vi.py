"""Builder for the Vietnamese rails translation of pi-2 (Vibhaṅga, «Phân tích các hiện tượng», plain audience),
chapters 2 (Āyatanavibhaṅgo, «Phân tích các lĩnh vực nhận biết») and 3 (Dhātuvibhaṅgo, «Phân tích các yếu tố»).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/2-ayatanavibhango.md   (^2-2-0 … ^2-171)
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/3-dhatuvibhango.md     (^2-3-0 … ^2-188)
  0-INBOX/temp/pipeline/pi-2-vi-ai/rails/notes-2-3.md   (new recurring formulas, Pāli = tiếng Việt)

Translated fresh from the Pāli with the locked pi-2 termbase. Shared strings are imported read-only from the approved
sample builder (S) and the chapter-1 builder (K1); passages that repeat the Dhammasaṅgaṇī reuse the approved pi-1
Vietnamese rails lines (read from AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters by block id;
check_pi1() asserts every hard-coded pi-1 string is present there). Importing this module writes nothing.

usage: python -I -X utf8 build_rails_2_3_vi.py
"""
import itertools
import pathlib
import re
import sys
import unicodedata

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)
import build_rails_1_vi as K1      # noqa: E402  (importing writes nothing)

PI1_PA = S.ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
PI1_VI = S.ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
NOTES_PATH = RAILS / "notes-2-3.md"
cap, low = S.cap, K1.low
SLIPS = []          # source slips met while building (reported)
MISFITS = []        # termbase gaps / misfits / sense choices (reported)
PI1_USED = []       # pi-1 strings reused (checked by check_pi1)


def note(lst, s):
    if s not in lst:
        lst.append(s)


def slip(s):
    note(SLIPS, s)


def misfit(s):
    note(MISFITS, s)


# =========================================================================== pi-1 lines by block id
_PI1 = {}


def _load_pi1():
    if _PI1:
        return
    for f in sorted(PI1_PA.glob("*.md")):
        pa = f.read_text(encoding="utf-8").splitlines()
        vi = (PI1_VI / f.name).read_text(encoding="utf-8").splitlines()
        assert len(pa) == len(vi), f.name
        for p, v in zip(pa, vi):
            m = S.ID.search(p)
            if m:
                _PI1[m.group(1)] = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", v)


def p1(bid):
    """the approved pi-1 Vietnamese line of a block (without the id)"""
    _load_pi1()
    return _PI1[bid]


def p1_body(bid):
    """pi-1 «Vật chất nào là X? BODY – vật chất này là X.» -> BODY"""
    ln = p1(bid)
    body = ln.split("? ", 1)[1]
    return body.rsplit(" – ", 1)[0]


def pi1(s):
    """mark a hard-coded string as taken from the approved pi-1 Vietnamese rails (checked by check_pi1)"""
    if s not in PI1_USED:
        PI1_USED.append(s)
    return s


def sub1(text, old, new):
    assert text.count(old) == 1, (old, text[:80])
    return text.replace(old, new)


# =========================================================================== names
TATTHA, IS_WHAT, CALLED = S.TATTHA, S.IS_WHAT, S.CALLED_SG     # «Ở đây,» «là gì?» «đó được gọi là»
AY = {  # āyatana names (termbase: Cakkhāyatanaṃ «lĩnh vực mắt» … dhammāyatanaṃ «lĩnh vực đối tượng của ý»)
    "cakkhu": "lĩnh vực mắt", "rūpa": "lĩnh vực hình sắc", "sota": "lĩnh vực tai", "sadda": "lĩnh vực âm thanh",
    "ghāna": "lĩnh vực mũi", "gandha": "lĩnh vực mùi", "jivhā": "lĩnh vực lưỡi", "rasa": "lĩnh vực vị",
    "kāya": "lĩnh vực thân", "phoṭṭhabba": "lĩnh vực vật xúc chạm", "mana": "lĩnh vực ý",
    "dhamma": "lĩnh vực đối tượng của ý",
}
AY_ORDER_S = ["cakkhu", "rūpa", "sota", "sadda", "ghāna", "gandha", "jivhā", "rasa", "kāya", "phoṭṭhabba", "mana",
              "dhamma"]
AY_ORDER_A = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "mana", "rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba",
              "dhamma"]
DH = {  # dhātu names (termbase)
    "pathavī": "yếu tố đất", "āpo": "yếu tố nước", "tejo": "yếu tố lửa", "vāyo": "yếu tố gió",
    "ākāsa": "yếu tố không gian", "viññāṇa": "yếu tố thức",
    "sukha": "yếu tố dễ chịu", "dukkha": "yếu tố khó chịu", "somanassa": "yếu tố niềm vui",
    "domanassa": "yếu tố nỗi buồn", "upekkhā": "yếu tố bình thản", "avijjā": "yếu tố vô minh",
    "kāma": "yếu tố dục lạc", "byāpāda": "yếu tố ác ý", "vihiṃsā": "yếu tố hãm hại", "nekkhamma": "yếu tố từ bỏ",
    "abyāpāda": "yếu tố không ác ý", "avihiṃsā": "yếu tố không hãm hại",
    "cakkhu": "yếu tố mắt", "rūpa": "yếu tố hình sắc", "cakkhuviññāṇa": "yếu tố thức qua mắt",
    "sota": "yếu tố tai", "sadda": "yếu tố âm thanh", "sotaviññāṇa": "yếu tố thức qua tai",
    "ghāna": "yếu tố mũi", "gandha": "yếu tố mùi", "ghānaviññāṇa": "yếu tố thức qua mũi",
    "jivhā": "yếu tố lưỡi", "rasa": "yếu tố vị", "jivhāviññāṇa": "yếu tố thức qua lưỡi",
    "kāya": "yếu tố thân", "phoṭṭhabba": "yếu tố vật xúc chạm", "kāyaviññāṇa": "yếu tố thức qua thân",
    "mano": "yếu tố ý", "dhamma": "yếu tố đối tượng của ý", "manoviññāṇa": "yếu tố ý thức",
    "asaṅkhatā": "yếu tố không do điều kiện tạo thành",
}
DH18 = ["cakkhu", "rūpa", "cakkhuviññāṇa", "sota", "sadda", "sotaviññāṇa", "ghāna", "gandha", "ghānaviññāṇa",
        "jivhā", "rasa", "jivhāviññāṇa", "kāya", "phoṭṭhabba", "kāyaviññāṇa", "mano", "dhamma", "manoviññāṇa"]


def q(name):
    """Tattha katamaṃ/katamā X?  ->  «Ở đây, X là gì?»"""
    return f"{TATTHA} {name} {IS_WHAT}"


def called_q(name, dash=True):
    """– ayaṃ/idaṃ vuccati "X".  ->  «– đó được gọi là “X”.» / own sentence «Đó được gọi là “X”.»"""
    return f"– {CALLED} “{name}”." if dash else f"{cap(CALLED)} “{name}”."


def called_sq(name):
    """– ayaṃ vuccati ‘X’. (single quotes in the source)"""
    return f"– {CALLED} ‘{name}’."


# =========================================================================== chapter 2: Suttantabhājanīya
AY12_S = f"Mười hai lĩnh vực nhận biết – {', '.join(AY[k] for k in AY_ORDER_S)}."   # Dvādasāyatanāni – …
AY12_A = f"Mười hai lĩnh vực nhận biết – {', '.join(AY[k] for k in AY_ORDER_A)}."   # (Abhidhamma order)
# X aniccaṃ dukkhaṃ anattā vipariṇāmadhammaṃ / aniccā dukkhā anattā vipariṇāmadhammā (termbase aniccaṃ «vô thường»,
# dukkhaṃ «khổ đau» (suffering in general, 'aniccaṃ dukkhaṃ'), anattā «không phải là tự ngã», vipariṇāmadhammaṃ
# «có bản chất biến đổi»)
IMPERM = "là vô thường, là khổ đau, không phải là tự ngã và có bản chất biến đổi"
IMPERM_ITEMS = ["Mắt", "Các hình sắc", "Tai", "Các âm thanh", "Mũi", "Các mùi", "Lưỡi", "Các vị", "Thân",
                "Các vật xúc chạm", "Ý", "Các đối tượng của ý"]
IMPERM_LINE = " ".join(f"{n} {IMPERM}." for n in IMPERM_ITEMS)

# ---- the sense-base definitions = the pi-1 rūpakaṇḍa bodies, with the pi-2 variant brackets
SENSE_P1 = {"cakkhu": "1-596", "sota": "1-600", "ghāna": "1-604", "jivhā": "1-608", "kāya": "1-612",
            "rūpa": "1-616", "sadda": "1-620", "gandha": "1-624", "rasa": "1-628", "phoṭṭhabba": "1-647"}
EYE_VAR_P1 = "[khác chính tả (Sī., Syā.): cakkhuṃ]"
# [cakkhuṃ (sī. syā. ka.) dha. sa. 596-599]: dha. sa. = Dhammasaṅgaṇī, pi-1 title «Liệt kê các hiện tượng»
EYE_VAR = "[khác chính tả (Sī., Syā., Ka.): cakkhuṃ; xem “Liệt kê các hiện tượng” 596-599]"


def ay_body(k):
    """pi-2 answer of «Tattha katamaṃ <X>āyatanaṃ?» (= pi-1 body with the pi-2 variants)"""
    b = p1_body(SENSE_P1[k])
    if k == "cakkhu":
        b = sub1(b, EYE_VAR_P1, EYE_VAR)
    elif k == "rūpa":
        b = sub1(b, "màu vàng, màu đỏ, màu trắng", "màu vàng, màu đỏ [dị bản (Sī.): pītaṃ lohitaṃ], màu trắng")
        b = sub1(b, " [khác chính tả (Sī., Ka.): caturassaṃ]", "")
        b = sub1(b, "[khác chính tả (Sī., Syā.): suriyamaṇḍalassa]", "[khác chính tả (Sī., Syā., Kaṃ.): suriyamaṇḍalassa]")
    elif k == "sadda":
        b = sub1(b, "tiếng trống cơm,", "tiếng trống cơm [khác chính tả (Sī.): mutiṅgasaddho],")
    elif k == "rasa":
        b = sub1(b, "vị mặn, vị kiềm, vị chua nhẹ [dị bản (Sī.): lapilakaṃ],",
                 "vị mặn [dị bản (Sī.): lapilakaṃ; (Ka., Sī.): lampikaṃ], vị kiềm, vị chua nhẹ,")
    return b


def ay_segment(k):
    """Tattha katamaṃ X? Yaṃ … suñño gāmopeso. Idaṃ vuccati "X"."""
    return f"{q(AY[k])} {ay_body(k)}. {called_q(AY[k], dash=False)}"


def dh_pe(k):
    """Abhidhamma of ch. 3: the same definitions cut by …pe… («Yaṃ cakkhu … pasādo…pe… suñño gāmopeso»)"""
    if k == "phoṭṭhabba":
        return f"{cap(DH['pathavī'])}… đây là {DH['phoṭṭhabba']}"            # Pathavīdhātu…pe… phoṭṭhabbadhātupesā
    b = re.sub(r" \[[^\]]*\]", "", p1_body(SENSE_P1[k]))
    if k in ("cakkhu", "sota", "ghāna", "jivhā", "kāya"):
        head = b.split("phái sinh từ bốn yếu tố cơ bản", 1)[0] + "phái sinh từ bốn yếu tố cơ bản"
        return f"{head}… đây là ngôi làng trống rỗng"
    if k == "rūpa":
        head = b.split("phái sinh từ bốn yếu tố cơ bản", 1)[0] + "phái sinh từ bốn yếu tố cơ bản"
        return f"{head}… đây là {DH['rūpa']}"
    head = b.split("không thấy được nhưng có tính va chạm", 1)[0] + "không thấy được nhưng có tính va chạm"
    return f"{head}… đây là {DH[k]}"


# =========================================================================== Abhidhammabhājanīya helpers
MANA = AY["mana"]


def mana_head(n):
    """N-vidhena manāyatanaṃ –  ->  «Lĩnh vực ý theo nhóm N –»"""
    return f"{cap(MANA)} {K1.by_n(n)} –"


def mana_end(n):
    """Evaṃ N-vidhena manāyatanaṃ.  ->  «Như vậy là lĩnh vực ý theo nhóm N.»"""
    return f"Như vậy là {MANA} {K1.by_n(n)}."


MANA_RX = re.compile(r"^(Tattha katamaṃ manāyatanaṃ\? )?(\S+?)[vb]idhena manāyatanaṃ – (.*?)"
                     r"(?: Evaṃ (\S+?)[vb]idhena manāyatanaṃ\.)?$")


def mana_line(p):
    """the manāyatana classification lines of ^2-161 (K1.chain for the bodies)"""
    tail = ""
    m13 = re.match(r'^(.*)…pe…\. Evaṃ bahuvidhena manāyatanaṃ\. Idaṃ vuccati "manāyatanaṃ"\.$', p)
    if m13:
        p = m13.group(1)
        tail = f"… {mana_end('many')} {called_q(MANA, dash=False)}"
    m = MANA_RX.match(p)
    assert m, p
    qq, nw, body, nw2 = m.groups()
    body = re.sub(r"^phassasampayuttaṃ\.$", "phassasampayutto.", body)    # neuter of the K1 item key
    out = f"{q(MANA)} " if qq else ""
    out += f"{mana_head(K1.NUMP[nw.lower()])} {K1.chain(body)}"
    if nw2:
        assert nw2.lower() == nw.lower(), p
        out += f" {mana_end(K1.NUMP[nw2.lower()])}"
    return out + tail


KH_RX = re.compile(r'^Tattha katamo (\S+kkhandho)\? (Ekavidhena .*?\.) (Duvidhena .*?\.) (Tividhena \S+ – .*?)'
                   r'…pe… evaṃ dasavidhena (\S+)…pe… evaṃ bahuvidhena (\S+)( – ayaṃ vuccati|\. Ayaṃ vuccati) "(\S+)"\.$')


def khandha_line(p):
    """Tattha katamo vedanākkhandho? Ekavidhena … …pe… evaṃ bahuvidhena vedanākkhandho. Ayaṃ vuccati "…"."""
    if "atthi hetu, atthi ahetu." in p:
        slip("^2-184 «atthi hetu, atthi ahetu» (^2-167 has «atthi na hetu»): «ahetu» 'a non-root' translated as "
             "written, which gives the same Vietnamese «có loại không phải là gốc rễ»")
        p = p.replace("atthi hetu, atthi ahetu.", "atthi hetu, atthi na hetu.")
    m = KH_RX.match(p)
    assert m, p
    kh, eka, du, ti, kh10, khb, sep, khq = m.groups()
    k = K1.KHP[kh]
    assert K1.KHP[kh10] == K1.KHP[khb] == K1.KHP[khq] == k, p
    end10 = low(K1.vidha_end(10, k))[:-1]
    endb = low(K1.vidha_end("many", k))[:-1]
    close = f". {called_q(K1.KH[k], dash=False)}" if sep.startswith(".") else f" {called_q(K1.KH[k])}"
    return f"{K1.agg_q(k)} {K1.abhi_line(eka)} {K1.abhi_line(du)} {K1.abhi_line(ti)}… {end10}… {endb}{close}"


# Vedanākkhandho, saññākkhandho, saṅkhārakkhandho, yañca rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ,
# asaṅkhatā ca dhātu. (pi-1 ^1-1094 layout; the matter clause as pi-1 3-01-rupakandam line 176, which follows the
# termbase anidassanaappaṭighaṃ «không thấy được và không có tính va chạm»; pi-1 ^1-1094 / 3-03 line 515 have
# «không thấy được, không có tính va chạm và nằm trong …»: the termbase wins)
ANID = (pi1("không thấy được và không có tính va chạm") + ", " + pi1("nằm trong lĩnh vực đối tượng của ý"))
DHAMMA_MEMBERS = (f"{cap(K1.KH['vedana'])}, {K1.KH['sanna']}, {K1.KH['sankhara']}; "
                  + pi1("và loại vật chất không thấy được và không có tính va chạm") + ", "
                  + pi1("nằm trong lĩnh vực đối tượng của ý; và yếu tố không do điều kiện tạo thành"))
FEM_FOOD = pi1("Năng lực nữ tính… thức ăn trong vai trò dưỡng chất")       # Itthindriyaṃ…pe… kabaḷīkāro āhāro
FEM_PUR_FOOD = f"Năng lực nữ tính, năng lực nam tính… {S.FOOD}"   # Itthindriyaṃ purisindriyaṃ…pe… kabaḷīkāro āhāro
# Rāgakkhayo, dosakkhayo, mohakkhayo (termbase khayo «sự hủy diệt», Rāga «tham đắm», doso «sự sân hận»,
# moho «sự si mê»; compound members bare)
NIBBANA = "Sự hủy diệt tham đắm, sự hủy diệt sân hận, sự hủy diệt si mê"


def anid_line(chapter):
    """Tattha katamaṃ rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ? … vuccati rūpaṃ "…"."""
    head = f"{TATTHA} vật chất {ANID} {IS_WHAT}"
    called = f"{CALLED} vật chất “{ANID}”."
    if chapter == 2:     # «Itthindriyaṃ purisindriyaṃ…pe… kabaḷīkāro āhāro. Idaṃ vuccati …»
        return f"{head} {FEM_PUR_FOOD}. {cap(called)}"
    return f"{head} {FEM_FOOD} – {called}"


# =========================================================================== chapter 3: Suttantabhājanīya
# the cores of the element definitions (pi-1 ^1-967, 968, 969, 970, 637 wording, small letter, no variant)
CORE = {
    "pathavī": pi1("cái cứng, điều được xem là rắn") + ", " + pi1("sự cứng, tính chất cứng"),
    "āpo": pi1("nước, điều được xem là nước, chất ẩm, điều được xem là chất ẩm") + "{v}, "
           + pi1("tính kết dính của vật chất"),
    "tejo": pi1("lửa, điều được xem là lửa, hơi ấm, điều được xem là hơi ấm, hơi nóng, điều được xem là hơi nóng"),
    "vāyo": pi1("gió, điều được xem là gió, trạng thái căng cứng của vật chất"),
    "ākāsa": pi1("không gian, điều được xem là không gian, khoảng không, điều được xem là khoảng không, kẽ hở, "
                 "điều được xem là kẽ hở, điều không bị") + " {by} chạm đến",
}
SNEHO_VAR = " [khác chính tả (Syā.): sneho snehagataṃ]"
BY_FLESH = "thịt và máu"                            # maṃsalohitehi (termbase maṃsa «thịt», lohitaṃ «máu»)
BY_GREAT = "bốn yếu tố cơ bản"                      # catūhi mahābhūtehi (pi-1 ^1-637)
INT_SELF = "ở nơi bản thân, riêng từng người"       # ajjhattaṃ paccattaṃ
INT_ATTR = "ở nơi bản thân, do nghiệp tạo ra"       # ajjhattaṃ upādinnaṃ
EXT_SELF = "thuộc phần bên ngoài"                   # bāhiraṃ
EXT_ATTR = "ở bên ngoài bản thân, không do nghiệp tạo ra"   # bahiddhā anupādinnaṃ
NAMELY = "cụ thể là –"                              # seyyathidaṃ – (termbase «cụ thể là»)
OTHER = "hoặc bất cứ điều nào khác"                 # yaṃ vā panaññampi atthi (termbase «hoặc … bất cứ … nào khác»)


def head_int(core):
    """Yaṃ ajjhattaṃ paccattaṃ <core> ajjhattaṃ upādinnaṃ"""
    return f"Điều {INT_SELF}, là {core}, {INT_ATTR}"


def other_int(core):
    return f"{OTHER} {INT_SELF}, là {core}, {INT_ATTR}"


def head_ext(core):
    """Yaṃ bāhiraṃ <core> bahiddhā anupādinnaṃ"""
    return f"Điều {EXT_SELF}, là {core}, {EXT_ATTR}"


def other_ext(core):
    return f"{OTHER} {EXT_SELF}, là {core}, {EXT_ATTR}"


def int_name(k):
    """ajjhattikā pathavīdhātu = «yếu tố đất thuộc phần bên trong» (termbase ajjhattikā tejodhātu …)"""
    return f"{DH[k]} thuộc phần bên trong"


def ext_name(k):
    return f"{DH[k]} thuộc phần bên ngoài"


EATEN = "những gì đã ăn, đã uống, đã nhai, đã nếm"   # asitapītakhāyitasāyitaṃ (no termbase entry)
LISTS = {
    "pathavī_i": ("tóc, lông, móng, răng, da, thịt, gân [khác chính tả (Sī.): nahāru], xương, tủy xương "
                  "[khác chính tả (Sī.): aṭṭhimiñjā], thận, tim, gan, màng hoành, lá lách, phổi, ruột, màng ruột, "
                  "thức ăn trong dạ dày, phân"),
    "pathavī_e": ("sắt, đồng, thiếc, chì, bạc [dị bản (Syā.): sajjhu], ngọc trai, ngọc quý, ngọc lưu ly, vỏ ốc, đá, "
                  "san hô, đồng tiền, vàng, hồng ngọc [khác chính tả (Syā., Ka.): lohitaṅgo; dị bản (?): lohitako], "
                  "ngọc mắt mèo, cỏ, gỗ, sỏi, mảnh sành [khác chính tả (Ka.): kathalaṃ], đất, đá tảng, núi"),
    "āpo_i": "mật, đờm, mủ, máu, mồ hôi, mỡ, nước mắt, mỡ lỏng, nước bọt, nước mũi, dịch khớp, nước tiểu",
    "āpo_e": ("nhựa rễ cây, nhựa thân cây, nhựa vỏ cây, nhựa lá, nhựa hoa, nhựa trái cây, sữa, sữa đông, bơ lỏng, "
              "bơ tươi, dầu, mật ong, mật mía, nước trên mặt đất hoặc nước trên bầu trời"),
    "tejo_i": (f"cái làm cho người ta ấm lên, cái làm cho người ta già đi, cái làm cho người ta nóng rực, và cái "
               f"làm cho {EATEN} được tiêu hóa đúng đắn"),
    "tejo_e": ("lửa củi, lửa rơm [dị bản (mọi bản): sakalikaggi], lửa cỏ, lửa phân bò, lửa trấu, lửa rác, lửa sét, "
               "sức nóng của lửa, sức nóng của mặt trời, sức nóng của đống củi, sức nóng của đống cỏ, sức nóng của "
               "đống lúa, sức nóng của đống hàng hóa"),
    "vāyo_i": ("gió đi lên, gió đi xuống, gió trong bụng, gió trong ruột [khác chính tả (Sī., Syā.): koṭṭhasayā], "
               "gió chạy khắp các chi, gió như dao cắt, gió như dao cạo, gió như kim châm, hơi thở vào, hơi thở ra, "
               "hoặc những gì như vậy"),      # termbase satthaka «dao cắt», khuraka «dao cạo», uppalaka «kim châm»
    "vāyo_e": ("gió đông, gió tây, gió bắc, gió nam, gió có bụi, gió không bụi, gió lạnh, gió nóng, gió nhẹ, "
               "gió mạnh, gió bão, gió trên tầng cao, gió từ cánh chim, gió từ chim thần Ga-ru-đa, gió từ quạt lá "
               "cọ, gió từ quạt tay"),        # termbase kāḷa «bão», verambha, pakkha, supaṇṇa, tālavaṇṭa, vidhūpana
    "ākāsa_i": (f"lỗ tai, lỗ mũi, cửa miệng, chỗ mà qua đó {EATEN} được nuốt vào, chỗ mà ở đó {EATEN} nằm lại, "
                f"và chỗ mà qua đó {EATEN} thoát ra phía dưới"),
}
TOGETHER = "gom tất cả lại làm một và thu tóm lại"   # tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā (sample)
SOME = S.SOME                                       # atthi «có loại»


def element_segment(k):
    """^2-173 … ^2-177: the four great elements and space, two lines each"""
    core = CORE[k].format(v=SNEHO_VAR if k == "āpo" else "", by=BY_FLESH)
    core_plain = CORE[k].format(v="", by=BY_FLESH)
    core_e = CORE[k].format(v="", by=BY_GREAT)
    l1 = (f"{q(DH[k])} {cap(DH[k])} có hai loại – {SOME} thuộc phần bên trong, {SOME} thuộc phần bên ngoài. "
          f"{q(int_name(k))} {head_int(core)}, {NAMELY} {LISTS[k + '_i']}, {other_int(core_plain)} "
          f"{called_sq(int_name(k))}")
    if k == "ākāsa":
        ext_body = head_ext(core_e)
    else:
        ext_body = f"{head_ext(core_e)}, {NAMELY} {LISTS[k + '_e']}, {other_ext(core_e)}"
    l2 = (f"{q(ext_name(k))} {ext_body} {called_sq(ext_name(k))} "
          f"{cap(int_name(k))} và {ext_name(k)}, {TOGETHER} {called_q(DH[k])}")
    return [l1, l2]


SIX_A = ["pathavī", "āpo", "tejo", "vāyo", "ākāsa", "viññāṇa"]
SIX_B = ["sukha", "dukkha", "somanassa", "domanassa", "upekkhā", "avijjā"]
SIX_C = ["kāma", "byāpāda", "vihiṃsā", "nekkhamma", "abyāpāda", "avihiṃsā"]
THESE_SIX = "Đây là sáu yếu tố."                    # Imā cha dhātuyo.
MORE_SIX = "Sáu yếu tố khác nữa –"                  # Aparāpi cha dhātuyo –
VINN6 = ", ".join(DH[k + "viññāṇa"] for k in ("cakkhu", "sota", "ghāna", "jivhā", "kāya", "mano"))
WHICH = "Điều mà là"                                # Yaṃ / Yā … (pi-1 nikkhepa «Điều mà là …», ^1-1062)

FEELING_P1 = {  # Yaṃ kāyikaṃ sātaṃ … vedanā (pi-1 ^1-445, 558, 3, 415, 405 without the «tajjā…samphassajaṃ» prefix)
    "sukha": pi1("sự khoan khoái nơi thân") + ", " + pi1(
        "sự dễ chịu nơi thân, cảm nhận khoan khoái và dễ chịu sinh từ sự tiếp xúc của thân, cảm giác khoan khoái và "
        "dễ chịu sinh từ sự tiếp xúc của thân"),
    "dukkha": pi1("sự bứt rứt nơi thân") + ", " + pi1(
        "sự khó chịu nơi thân, cảm nhận bứt rứt và khó chịu sinh từ sự tiếp xúc của thân, cảm giác bứt rứt và khó "
        "chịu sinh từ sự tiếp xúc của thân"),
    "somanassa": pi1("sự khoan khoái trong tâm") + ", " + pi1(
        "sự dễ chịu trong tâm, cảm nhận khoan khoái và dễ chịu sinh từ sự tiếp xúc của tâm, cảm giác khoan khoái và "
        "dễ chịu sinh từ sự tiếp xúc của tâm"),
    "domanassa": pi1("sự bứt rứt trong tâm") + ", " + pi1(
        "sự khó chịu trong tâm, cảm nhận bứt rứt và khó chịu sinh từ sự tiếp xúc của tâm, cảm giác bứt rứt và khó "
        "chịu sinh từ sự tiếp xúc của tâm"),
    "upekkhā": pi1("trạng thái trong tâm không khoan khoái cũng không bứt rứt") + ", " + pi1(
        "cảm nhận không khó chịu cũng không dễ chịu sinh từ sự tiếp xúc của tâm, cảm giác không khó chịu cũng không "
        "dễ chịu sinh từ sự tiếp xúc của tâm"),
}
MOHA_P1 = pi1(   # Yaṃ aññāṇaṃ adassanaṃ … avijjālaṅgī moho akusalamūlaṃ (pi-1 ^1-390)
    "sự không biết, sự không thấy, sự không thấu hiểu, sự không hiểu ra, sự không tỉnh ngộ, sự không thấu triệt, "
    "sự không nắm bắt, sự không đi sâu, sự không xem xét, sự không xem xét lại, sự không tự mình thấy rõ, sự ngu "
    "muội, sự khờ dại, sự thiếu hiểu biết rõ ràng, sự si mê, sự mê muội, sự mê lầm, vô minh, dòng lũ vô minh, ách vô "
    "minh, khuynh hướng tiềm ẩn vô minh, sự ám ảnh của vô minh, then cài vô minh, sự si mê, tức gốc rễ bất thiện")
VITAKKA6 = pi1("suy nghĩ, sự hướng tâm, tư duy, sự gắn tâm, sự gắn tâm chặt chẽ, sự đặt tâm vào đối tượng")  # ^1-461
MICCHA = "tư duy sai lầm"                           # micchāsaṅkappo (pi-1 ^1-371)
SAMMA = "tư duy đúng đắn"                           # sammāsaṅkappo (pi-1 ^1-7)
CONNECTED = {  # X-paṭisaṃyutto (termbase paṭisaṃyutto «liên quan đến», Kāmapaṭisaṃyutto «liên quan đến dục lạc»)
    "kāma": "liên quan đến dục lạc", "byāpāda": "liên quan đến ác ý", "vihiṃsā": "liên quan đến sự hãm hại",
    "nekkhamma": "liên quan đến sự từ bỏ", "abyāpāda": "liên quan đến sự không ác ý",
    "avihiṃsā": "liên quan đến sự không hãm hại"}
DOSA_LIST = (   # Dasasu vā āghātavatthūsu cittassa āghāto … anattamanatā cittassa (pi-1 ^1-1066 list without
                # byāpajjitattaṃ, which the pi-2 text lacks)
    "Hoặc sự oán giận của tâm đối với mười chỗ dựa của sự oán giận, "
    + pi1("sự phẫn uất, sự ác cảm, sự đối nghịch, sự nổi nóng, sự nổi nóng dữ dội, sự nổi nóng tột độ, sự sân hận, "
          "sự sân hận dữ dội, sự sân hận tột độ, sự thù hằn của tâm, sự sân hận dữ dội của ý, sự giận dữ, sự khởi "
          "giận, trạng thái khởi giận, sự sân hận, sự khởi sân, trạng thái khởi sân, sự thù hằn, sự khởi thù hằn")
    + ", " + pi1("sự chống đối, sự đối nghịch, sự hung dữ, sự nói năng cộc cằn, sự không hài lòng của tâm"))


def thought(k, full):
    """Xpaṭisaṃyutto takko vitakko (saṅkappo … abhiniropanā | …pe…) micchā/sammāsaṅkappo"""
    last = MICCHA if k in ("kāma", "byāpāda", "vihiṃsā") else SAMMA
    series = f"{VITAKKA6}, {last}" if full else f"suy nghĩ, sự hướng tâm… {last}"
    return f"{cap(series)}, {CONNECTED[k]}"


def called_dh(k):
    return called_q(DH[k])


# =========================================================================== Abhidhamma of ch. 3: the mind series
CITTA_SYN = pi1("tâm, ý, tâm trí, tấm lòng, sự sáng ngời, ý, lĩnh vực ý, năng lực ý, thức, khối thức")   # ^1-370
CITTA_SHORT = "tâm, ý, tâm trí…"                    # cittaṃ mano mānasaṃ…pe…
TAJJA = "tương ứng"                                 # tajjā- (pi-1 «yếu tố ý thức tương ứng»)
ARISES = "sinh khởi"                                # uppajjati (termbase «uppajjati cittaṃ» «sinh khởi tâm»)
AFTER = "liền sau khi {x} sinh khởi rồi chấm dứt"   # X-dhātuyā uppajjitvā niruddhasamanantarā
DEPEND = {"cakkhu": "mắt và các hình sắc", "sota": "tai và các âm thanh", "ghāna": "mũi và các mùi",
          "jivhā": "lưỡi và các vị", "kāya": "thân và các vật xúc chạm", "mano": "ý và các đối tượng của ý"}
PATICCA = "Tùy thuộc vào"                           # Cakkhuñca paṭicca rūpe ca (Paṭicca: compound-member entry only)
FIRST_ADVERT = "hoặc, như sự lưu ý đầu tiên đối với mọi hiện tượng,"   # sabbadhammesu vā pana paṭhamasamannāhāro


def arises(tajja_name, short=False):
    """uppajjati cittaṃ … tajjā<X>  ->  «sinh khởi tâm, ý, …, X tương ứng»"""
    if short:
        return f"{ARISES} {CITTA_SHORT} {tajja_name} {TAJJA}"
    return f"{ARISES} {CITTA_SYN}, {tajja_name} {TAJJA}"


def after(k):
    return AFTER.format(x=DH[k])


def vinnana_line(k):
    nm = DH[k + "viññāṇa"]
    misfit("paṭicca in «Cakkhuñca paṭicca rūpe ca» (^2-184): the termbase has only the compound-member sense "
           "«tùy thuộc vào điều kiện» (paṭiccasamuppāda); written «Tùy thuộc vào mắt và các hình sắc, …»")
    return f"{q(nm)} {PATICCA} {DEPEND[k]}, {arises(nm)} {called_q(nm)}"


def manodhatu_line():
    t = DH["mano"]
    slip("^2-184 manodhātu: «… tajjāmanodhātu sabbadhammesu vā pana …» has no punctuation before «sabbadhammesu» "
         "(comma added, rendered as meant)")
    return (f"{q(t)} {cap(after('cakkhuviññāṇa'))}, {arises(t)}; sau {DH['sotaviññāṇa']}… sau {DH['ghānaviññāṇa']}… "
            f"sau {DH['jivhāviññāṇa']}… {after('kāyaviññāṇa')}, {arises(t)}, {FIRST_ADVERT} {arises(t)} "
            f"{called_q(t)}")


def manovinnana_line():
    t = DH["manoviññāṇa"]
    slip("^2-184 manoviññāṇadhātu: «… tajjāmanoviññāṇadhātu manañca paṭicca …» has no punctuation before "
         "«manañca» (comma added, rendered as meant)")
    return (f"{q(t)} {cap(after('cakkhuviññāṇa'))}, {ARISES} {DH['mano']}, {after('mano')}, {arises(t, True)}; "
            f"sau {DH['sotaviññāṇa']}… sau {DH['ghānaviññāṇa']}… sau {DH['jivhāviññāṇa']}… "
            f"{after('kāyaviññāṇa')}, {ARISES} {DH['mano']}, {AFTER.format(x='cả ' + DH['mano'])}, {arises(t, True)}, "
            f"{low(PATICCA)} {DEPEND['mano']}, {arises(t)} {called_q(t)}")


# =========================================================================== chapter 3: the six-element sets
KAMA2 = ("Lấy địa ngục Vô Gián ở bên dưới làm giới hạn, tính cả chư thiên Tha Hóa Tự Tại ở bên trên vào bên trong, "
         "những gì ở trong khoảng giữa ấy, thuộc cõi này, nằm trong cõi này: các khối, yếu tố và lĩnh "
         "vực nhận biết, những gì thuộc vật chất [dị bản (Syā.): rūpaṃ], cảm giác, tri giác, các sự tạo tác, thức")
# Heṭṭhato avīcinirayaṃ pariyantaṃ karitvā uparito paranimmitavasavattī deve anto karitvā yaṃ etasmiṃ antare
# etthāvacarā ettha pariyāpannā khandhadhātuāyatanā rūpā [rūpaṃ (syā.)] vedanā saññā saṅkhārā viññāṇaṃ
# (termbase nirayaṃ «địa ngục», pariyantaṃ «giới hạn», karitvā «lấy … làm», uparito «ở bên trên», paranimmitavasavattī
# deve «chư thiên Tha Hóa Tự Tại», antare «khoảng giữa», rūpā 'in a list of the aggregates' «thuộc vật chất»)
VIHIMSA2 = ("Ở đời này, có người quấy hại chúng sinh bằng tay, bằng cục đất, bằng gậy, bằng vũ khí, bằng dây thừng "
            "hoặc bằng thứ này hay thứ khác; sự quấy hại, sự quấy hại nặng nề, sự làm hại, sự hãm hại, sự làm khổ, "
            "sự làm khổ nặng nề, sự gây hại cho người khác thuộc loại như vậy")
# Idhekacco pāṇinā vā leḍḍunā vā daṇḍena vā satthena vā rajjuyā vā aññataraññatarena satte viheṭheti, yā evarūpā
# heṭhanā viheṭhanā hiṃsanā vihiṃsanā rosanā virosanā parūpaghāto
METTA = (f"{WHICH} lòng từ ái đối với chúng sinh, sự khởi lòng từ ái, trạng thái khởi lòng từ ái, sự giải thoát "
         f"của tâm nhờ lòng từ ái")      # Yā sattesu metti mettāyanā mettāyitattaṃ mettācetovimutti
KARUNA = (f"{WHICH} lòng trắc ẩn đối với chúng sinh, sự khởi lòng trắc ẩn, trạng thái khởi lòng trắc ẩn, sự giải "
          f"thoát của tâm nhờ lòng trắc ẩn")   # Yā sattesu karuṇā karuṇāyanā karuṇāyitattaṃ karuṇācetovimutti
NEKKHAMMA2 = f"Tất cả các hiện tượng thiện cũng là “{DH['nekkhamma']}”."   # Sabbepi kusalā dhammā "nekkhammadhātu".
EIGHTEEN = (f"Như vậy, ba nhóm sáu này, {TOGETHER}, thành mười tám yếu tố.")
# Iti imāni tīṇi chakkāni tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā aṭṭhārasa dhātuyo honti. (no dash in the Pāli)
DH18_LINE = f"Mười tám yếu tố – {', '.join(DH[k] for k in DH18)}."                 # Aṭṭhārasa dhātuyo – …


def build_ch2_fixed():
    h = {}
    h["2-154"] = [AY12_S, IMPERM_LINE, f"{S.SEC_HEADINGS['Suttantabhājanīyaṃ']}."]
    h["2-155"] = [AY12_A]
    for sid, k in (("2-156", "cakkhu"), ("2-157", "sota"), ("2-158", "ghāna"), ("2-159", "jivhā"), ("2-160", "kāya"),
                   ("2-162", "rūpa"), ("2-163", "sadda"), ("2-164", "gandha"), ("2-165", "rasa"),
                   ("2-166", "phoṭṭhabba")):
        h[sid] = [ay_segment(k)]
    slip("^2-159 «jīvhindriyampetaṃ» for «jivhindriyampetaṃ» (plain spelling, rendered «năng lực lưỡi» as pi-1)")
    return h


def build_ch3_fixed():
    h = {}
    h["2-172"] = [f"Sáu yếu tố – {DH['pathavī']} [khác chính tả (Sī., Syā.): paṭhavīdhātu, cũng vậy ở các chỗ sau], "
                  + ", ".join(DH[k] for k in SIX_A[1:]) + "."]
    for sid, k in (("2-173", "pathavī"), ("2-174", "āpo"), ("2-175", "tejo"), ("2-176", "vāyo"), ("2-177", "ākāsa")):
        h[sid] = element_segment(k)
    h["2-178"] = [f"{q(DH['viññāṇa'])} {cap(VINN6)} {called_dh('viññāṇa')}", THESE_SIX]
    h["2-179"] = [f"{MORE_SIX} {', '.join(DH[k] for k in SIX_B)}."]
    L = [f"{q(DH[k])} {WHICH} {FEELING_P1[k]} {called_dh(k)}" for k in SIX_B[:5]]
    L.append(f"{q(DH['avijjā'])} {WHICH} {MOHA_P1} {called_dh('avijjā')}")
    L.append(THESE_SIX)
    h["2-180"] = L
    h["2-181"] = [f"{MORE_SIX} {', '.join(DH[k] for k in SIX_C)}."]
    h["2-182"] = [
        f"{q(DH['kāma'])} {thought('kāma', True)} – {CALLED} {DH['kāma']}. {KAMA2} {called_dh('kāma')}",
        f"{q(DH['byāpāda'])} {thought('byāpāda', False)} {called_dh('byāpāda')} {DOSA_LIST} {called_dh('byāpāda')}",
        f"{q(DH['vihiṃsā'])} {thought('vihiṃsā', False)} {called_dh('vihiṃsā')} {VIHIMSA2} {called_dh('vihiṃsā')}",
        f"{q(DH['nekkhamma'])} {thought('nekkhamma', False)} {called_dh('nekkhamma')} {NEKKHAMMA2}",
        f"{q(DH['abyāpāda'])} {thought('abyāpāda', False)} {called_dh('abyāpāda')} {METTA} {called_dh('abyāpāda')}",
        f"{q(DH['avihiṃsā'])} {thought('avihiṃsā', True)} {called_dh('avihiṃsā')} {KARUNA} "
        f"{called_dh('avihiṃsā')}",
        THESE_SIX,
        EIGHTEEN,
        f"{S.SEC_HEADINGS['Suttantabhājanīyaṃ']}.",
    ]
    h["2-183"] = [DH18_LINE]
    misfit("rūpā in the kāmadhātu list (^2-182): termbase sense 'in a list of the aggregates' «thuộc vật chất»; "
           "written «những gì thuộc vật chất» so the noun list reads naturally")
    return h


# =========================================================================== Pañhāpucchaka
GROUPS = {"Dvādasannaṃ āyatanānaṃ": ("Trong mười hai lĩnh vực nhận biết", "bao nhiêu lĩnh vực"),
          "Aṭṭhārasannaṃ dhātūnaṃ": ("Trong mười tám yếu tố", "bao nhiêu yếu tố")}
SUBJ = {}   # Pāli subject -> (Vietnamese, number s/p, noun for «những … mà»)
for _p, _n in (("Dasāyatanā", "Mười"), ("Ekādasāyatanā", "Mười một"), ("Pañcāyatanā", "Năm"), ("Navāyatanā", "Chín"),
               ("Chāyatanā", "Sáu"), ("Dvāyatanā", "Hai"), ("Cattāro āyatanā", "Bốn")):
    SUBJ[_p] = (f"{_n} lĩnh vực", "p", "lĩnh vực")       # termbase Dasāyatanā «mười lĩnh vực», Ekādasāyatanā …
for _p, _k in (("Manāyatanaṃ", "mana"), ("Dhammāyatanaṃ", "dhamma"), ("Saddāyatanaṃ", "sadda"),
               ("Rūpāyatanaṃ", "rūpa")):
    SUBJ[_p] = (cap(AY[_k]), "s", "lĩnh vực")
for _p, _n in (("Soḷasa", "Mười sáu"), ("Dasa", "Mười"), ("Pañca", "Năm"), ("Pannarasa", "Mười lăm"), ("Cha", "Sáu"),
               ("Sattarasa", "Mười bảy"), ("Nava", "Chín"), ("Aṭṭha", "Tám"), ("Satta", "Bảy"),
               ("Ekādasa", "Mười một"), ("Dvādasa", "Mười hai"), ("Dve", "Hai"), ("Tisso", "Ba")):
    SUBJ[f"{_p} dhātuyo"] = (f"{_n} yếu tố", "p", "yếu tố")   # termbase Soḷasa dhātuyo «mười sáu yếu tố» …
SUBJ["Sattadhātuyo"] = ("Bảy yếu tố", "p", "yếu tố")      # the source writes it as one word (^2-188)
for _p, _k in (("Kāyaviññāṇadhātu", "kāyaviññāṇa"), ("Manoviññāṇadhātu", "manoviññāṇa"), ("Dhammadhātu", "dhamma"),
               ("Manodhātu", "mano"), ("Saddadhātu", "sadda"), ("Rūpadhātu", "rūpa")):
    SUBJ[_p] = (cap(DH[_k]), "s", "yếu tố")
PRON = K1.PRON                                          # {"s": "nó", "p": "chúng"}
SIYA, NV, NV_TOPIC = K1.SIYA, K1.NV, K1.NV_TOPIC        # «đôi khi», «không nên nói –», «Về X thì không nên nói –»


def kenaci(noun):
    """kenaci viññeyyā, kenaci na viññeyyā (K1.KENACI with the chapter's noun instead of «khối»)"""
    return K1.KENACI.replace("những khối", f"những {noun}")


# ---- items missing from K1, and the source slips translated as written
LOCAL = {
    "appaccayo": "không có điều kiện",                  # termbase appaccayā «không có điều kiện» (closest sibling)
    "asaṅkhato": "không do điều kiện tạo thành",        # termbase asaṅkhataṃ
    # ^2-171 Manāyatanaṃ na vattabbaṃ – "upādāniyañceva upādānasampayuttañcā"ti (pattern: upādānañceva …)
    "upādāniyo ceva upādānasampayutto ca": K1.both("là đối tượng của sự bám víu", "gắn liền với sự bám víu"),
    # ^2-171 Dvāyatanā siyā upādānasampayuttaupādāniyā (pattern: upādānavippayutta…)
    "upādānasampayuttaupādāniyo": "gắn liền với sự bám víu và là đối tượng của sự bám víu",
    # ^2-171 "kilesasampayuttā ceva no ca na kilesā"tipi: the doubled negation translated literally (user rule)
    "kilesasampayutto ceva no ca na kileso": "gắn liền với phiền não nhưng không phải là không phải phiền não",
}
LOCAL_SLIP = {
    "upādāniyo ceva upādānasampayutto ca":
        "^2-171 Manāyatanaṃ na vattabbaṃ – \"upādāniyañceva upādānasampayuttañcā\"ti (the parallel lines have "
        "upādānañceva): translated as written «vừa là đối tượng của sự bám víu vừa gắn liền với sự bám víu»",
    "upādānasampayuttaupādāniyo":
        "^2-171 Dvāyatanā siyā upādānasampayuttaupādāniyā (the parallel lines have upādānavippayutta…): translated "
        "as written «gắn liền với sự bám víu và là đối tượng của sự bám víu»",
    "kilesasampayutto ceva no ca na kileso":
        "^2-171 \"kilesasampayuttā ceva no ca na kilesā\"tipi: doubled negation translated literally «gắn liền với "
        "phiền não nhưng không phải là không phải phiền não»",
    "appaccayo": None,
    "asaṅkhato": None,
}
# subject-specific sense: sukhasahagata said of body-consciousness = bodily pleasure (termbase sukhasahagataṃ sense 2)
SUBJ_SENSE = {("Kāyaviññāṇadhātu", "sukhasahagato"): "có sự dễ chịu đi kèm"}


def known(key):
    return key in LOCAL or key in K1.ITEMS or key in K1.ALIAS


def get(key):
    if key in LOCAL:
        if LOCAL_SLIP.get(key):
            slip(LOCAL_SLIP[key])
        if key == "appaccayo":
            misfit("appaccayaṃ (^2-171, ^2-188, 'unconditioned' in the dyad sappaccaya/appaccaya) has no entry; used "
                   "the sibling appaccayā «không có điều kiện» (termbase, adverb in 'ahetu appaccayā')")
        return LOCAL[key]
    if key in K1.ALIAS:
        slip(f"«{key}» written as one word (elsewhere «{K1.ALIAS[key]}»; rendered the same, as in chapter 1)")
    return K1.pred(key)


PLK = dict(K1.PL_KEY)
for _k in LOCAL:
    PLK.setdefault(K1.pali_plural(_k), _k)
PLK["kilesasampayuttā ceva no ca na kilesā"] = "kilesasampayutto ceva no ca na kileso"
PLK["na hetūahetukā"] = "na hetuahetuko"            # one word in the source (ch. 2)
PLK["na hetuahetukā"] = "na hetuahetuko"            # one word in the source (ch. 3)


def _word_opts(w):
    o = [w]
    if w.endswith("añceva"):
        o.append(w[:-6] + "o ceva")
    if w.endswith("añca"):
        o.append(w[:-4] + "o ca")
    if w.endswith("aṃ"):
        o.append(w[:-2] + "o")
    if w.endswith("ā"):
        o += [w[:-1] + "o", w[:-1] + "aṃ"]
    if w.endswith("inī"):
        o.append(w[:-3] + "ī")
    elif w.endswith("ī"):
        o.append(w[:-1] + "i")
    if w.endswith("i") and not w.endswith("hetu"):
        o.append(w[:-1] + "ī")
    return o


NOUNS = {K1.CL[c][0] for c in K1.CL} | {"cittaṃ"}


def sg_key(t):
    """Pāli predicate said of a singular subject (neuter -aṃ, feminine -ā or masculine) -> item key"""
    t = re.sub(r"hetū$", "hetu", t)
    if known(t):
        return t
    words = t.split(" ")
    cands = []
    for combo in itertools.product(*[_word_opts(w) for w in words]):
        c = " ".join(combo)
        if known(c):
            cands.append((sum(a != b for a, b in zip(combo, words)), c))
    if not cands:
        for combo in itertools.product(*[_word_opts(w) for w in words]):
            c = " ".join(combo) + " ca"
            if known(c):
                slip(f"«{t}» in a quote without «ca» (rendered like «{c}»)")
                return c
    assert cands, t
    key = sorted(cands)[0][1]
    kw = key.split(" ")
    if kw[-1] in NOUNS and len(kw) <= 2 and t == K1.pali_plural(key) and t != key:
        slip(f"«{t}» (plural noun) with a singular subject (no number in Vietnamese; same phrase)")
    return key


def pl_key(t):
    if t in PLK:
        return PLK[t]
    t2 = re.sub(r"^hetu ", "hetū ", t)
    if t2 in PLK:
        slip(f"«{t}» with a plural subject («hetu» for «hetū»; same phrase)")
        return PLK[t2]
    raise KeyError(t)


def pred(word, num, subj):
    key = sg_key(word) if num == "s" else pl_key(word)
    if (subj, key) in SUBJ_SENSE:
        misfit("sukhasahagatā said of Kāyaviññāṇadhātu (^2-187): termbase sense 'accompanied by bodily pleasure, of "
               "body-consciousness' «có sự dễ chịu đi kèm» (elsewhere the matrix name «có hạnh phúc đi kèm»)")
        return SUBJ_SENSE[(subj, key)]
    return get(key)


def qword(text, suffix):
    """the quoted Pāli word as a predicate word («"…"nti» adds the niggahīta, «cā» -> «ca»)"""
    t = text
    if suffix and suffix.startswith("n"):
        t += "ṃ"
    return re.sub(r"cā$", "ca", t)


QUOTE = K1.QUOTE
PANHA_FIX = [  # missing quote marks of the source, rendered as meant (reported)
    ('"parāmāsā ceva parāmaṭṭhā cāti parāmaṭṭhā ceva no ca parāmāsā"',
     '"parāmāsā ceva parāmaṭṭhā cā"ti, "parāmaṭṭhā ceva no ca parāmāsā"',
     '^2-188 "parāmāsā ceva parāmaṭṭhā cāti parāmaṭṭhā ceva no ca parāmāsā": both items inside one quote (missing '
     'quote marks); rendered as the parallel line of ^2-171 («rằng “A”; chúng “B”»)'),
]


def render_nv(nv, num, subj):
    qs = [f"rằng “{pred(w, num, subj)}”" for w in nv["q"]]
    return f"{nv['head']} " + ", hay ".join(qs)


def sentence(sent):
    """one Pañhāpucchaka sentence without its final full stop (port of K1._sentence for āyatana / dhātu subjects,
    neuter and feminine Pāli predicates)"""
    m = re.match(r"^(" + "|".join(sorted(SUBJ, key=len, reverse=True)) + r") (.*)$", sent)
    assert m, sent
    psubj = m.group(1)
    subj, num, noun = SUBJ[psubj]
    if psubj == "Sattadhātuyo":
        slip("^2-188 «Sattadhātuyo» written as one word (= Satta dhātuyo «Bảy yếu tố»)")
    body = m.group(2)
    if body.endswith("āti"):                       # closing «…ti» of the whole section
        body = body[:-2]
    toks = re.split(r"(, |; |…pe… )", body)
    out, first, topic, nv = [], True, False, None
    for i, tok in enumerate(toks):
        if i % 2 == 1:
            s = "…" if tok == "…pe… " else tok.strip()
            if nv is None:
                out.append(s)
            else:
                nv["pending"] = s
            continue
        qm = QUOTE.match(tok)
        if qm and qm.group(2) is None:             # «na vattabbā – "A"ti, "B".»: B quoted without «ti» (as written)
            assert nv is not None, sent
            out.append(render_nv(nv, num, psubj))
            out.append(";")
            nv = None
            out.append(f"{PRON[num]} “{pred(qword(qm.group(1), None), num, psubj)}”")
            slip("«na vattabbā – \"A\"ti, \"B\".» (B quoted without «ti», as written): rendered «…; chúng / nó “B”.» "
                 "as in chapter 1")
            continue
        if qm:                                     # next quoted item of an open «na vattabbā» list
            assert nv is not None, sent
            nv["q"].append(qword(qm.group(1), qm.group(2)))
            nv["pending"] = None
            continue
        if nv is not None:                         # close the open list
            out.append(render_nv(nv, num, psubj))
            out.append(";" if topic and nv["pending"] == "," else (nv["pending"] or ","))
            nv = None
        mv = re.match(r'^(siyā )?na vattabb(?:o|ā|aṃ) – (.*)$', tok)
        if mv:
            qm = QUOTE.match(mv.group(2))
            assert qm, tok
            w = qword(qm.group(1), qm.group(2))
            if mv.group(1):
                head = f"{SIYA} {NV}"
            elif first:
                head = NV_TOPIC.format(s=low(subj))
                topic = True
            else:                                  # «…, siyā Y, na vattabbā – "Z"ti» (no siyā): «…; về chúng thì …»
                assert out and out[-1] == ",", sent
                out[-1] = ";"
                head = low(NV_TOPIC.format(s=PRON[num]))
            nv = dict(head=head, q=[w], pending=None)
            first = False
            continue
        if tok == "kenaci viññeyyā" and toks[i + 2:i + 3] == ["kenaci na viññeyyā"]:
            v = kenaci(noun)                       # «…; chúng là những lĩnh vực / yếu tố mà …»
            if not first:
                topic = True
        elif tok == "kenaci na viññeyyā" and toks[i - 2] == "kenaci viññeyyā":
            out.pop()                              # the comma of the pair
            continue
        else:
            siya = tok.startswith("siyā ")
            word = tok[5:] if siya else tok
            v = pred(word, num, psubj)
            v = f"{SIYA} {v}" if siya else v
        if first:
            out.append(f"{subj} {v}")
        elif topic:
            out.append(f"{PRON[num]} {v}")
            topic = False
        else:
            out.append(v)
        first = False
    if nv is not None:
        out.append(render_nv(nv, num, psubj))
    res = ""
    for x in out:
        if x in (",", ";", "…"):
            res += x
        else:
            res += (" " if res else "") + x
    return res


def panha_line(p):
    p = p.replace('"ti pi', '"tipi')
    for bad, good, nt in PANHA_FIX:
        if bad in p:
            p = p.replace(bad, good)
            slip(nt)
    sents = re.split(r"(?<=\.) (?=[A-Z])", p)
    res = []
    for s in sents:
        assert s.endswith("."), s
        res.append(sentence(s[:-1]) + ".")
    return " ".join(res)


def panha_question(p):
    """Dvādasannaṃ āyatanānaṃ kati kusalā, … kati araṇā?  ->  «Trong mười hai lĩnh vực nhận biết, bao nhiêu lĩnh
    vực là thiện, … bao nhiêu lĩnh vực không có xung đột?»"""
    m = re.match(r"^(.*?) (kati .*)\?$", p)
    grp, body = m.group(1), m.group(2)
    head, kati = GROUPS[grp]
    parts = re.split(r"(…pe…|, )", body)
    out = [f"{head},"]
    for i, x in enumerate(parts):
        if i % 2 == 1:
            out.append("…" if x == "…pe…" else ",")
            continue
        x = x.strip()
        if not x:
            continue
        w = re.sub(r"^kati ", "", x)
        out.append(f" {kati} {K1.pred(K1.PL_KEY[w])}")
    return "".join(out) + "?"


# =========================================================================== chapters
FIXED = dict(K1.FIXED)
FIXED.update({
    "Āyatanavibhaṅgo niṭṭhito.": f"{S.CH_HEADINGS['Āyatanavibhaṅgo']} {K1.DONE}.",
    "Dhātuvibhaṅgo niṭṭhito.": f"{S.CH_HEADINGS['Dhātuvibhaṅgo']} {K1.DONE}.",
    "Imā cha dhātuyo.": THESE_SIX,
    "Idaṃ vuccati dhammāyatanaṃ.": f"{cap(CALLED)} {AY['dhamma']}.",
})
HEAD_T = {"Āyatanavibhaṅgo": S.CH_HEADINGS["Āyatanavibhaṅgo"], "Dhātuvibhaṅgo": S.CH_HEADINGS["Dhātuvibhaṅgo"],
          "Tikaṃ": K1.TIKA_H, "Dukaṃ": K1.DUKA_H}
HEAD_T.update(S.SEC_HEADINGS)
DH_PE_RX = re.compile(r"^Tattha katamā (\S+)dhātu\? (.*?) – ayaṃ vuccati \"\S+\"\.$")
VINN_RX = re.compile(r"^Tattha katamā (cakkhu|sota|ghāna|jivhā|kāya)viññāṇadhātu\? ")


def abhi(ln, chapter):
    """Abhidhammabhājanīya lines of both chapters"""
    if ln.startswith("Tattha katamaṃ manāyatanaṃ?") or re.match(r"^\S+?[vb]idhena manāyatanaṃ – ", ln):
        return mana_line(ln)
    if ln.startswith("Tattha katamo ") and "kkhandho?" in ln:
        return khandha_line(ln)
    if ln.startswith("Tattha katamaṃ dhammāyatanaṃ?") or ln.startswith("Tattha katamā dhammadhātu?"):
        name = AY["dhamma"] if chapter == 2 else DH["dhamma"]
        return f"{q(name)} {DHAMMA_MEMBERS}."
    if ln.startswith("Tattha katamaṃ rūpaṃ anidassanaappaṭighaṃ"):
        return anid_line(chapter)
    if ln.startswith("Tattha katamā asaṅkhatā dhātu?"):
        out = f"{q(DH['asaṅkhatā'])} {NIBBANA} {called_q(DH['asaṅkhatā'])}"
        if ln.endswith('Ayaṃ vuccati "dhammadhātu".'):
            out += f" {called_q(DH['dhamma'], dash=False)}"
        return out
    if ln.startswith("Tattha katamā manodhātu?"):
        return manodhatu_line()
    if ln.startswith("Tattha katamā manoviññāṇadhātu?"):
        return manovinnana_line()
    m = VINN_RX.match(ln)
    if m:
        return vinnana_line(m.group(1))
    m = DH_PE_RX.match(ln)
    if m:
        k = m.group(1)
        return f"{q(DH[k])} {dh_pe(k)} {called_q(DH[k])}"
    raise ValueError(ln)


def build(part, chapter):
    pali = (S.PALI / part).read_text(encoding="utf-8")
    h = build_ch2_fixed() if chapter == 2 else build_ch3_fixed()
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
        if sid in h:
            continue
        vi = []
        for ln in lines:
            if ln in FIXED:
                vi.append(FIXED[ln])
            elif section == "Pañhāpucchakaṃ":
                if ln.startswith("Dvādasāyatanāni – "):
                    vi.append(AY12_S)
                elif ln.startswith("Aṭṭhārasa dhātuyo – "):
                    vi.append(DH18_LINE)
                elif ln.endswith("?"):
                    vi.append(panha_question(ln))
                else:
                    vi.append(panha_line(ln))
            else:
                vi.append(abhi(ln, chapter))
        h[sid] = vi
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


# =========================================================================== pi-1 check and notes
def check_pi1():
    """every string marked pi1() must occur in the approved pi-1 Vietnamese rails (first letter either case)"""
    text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI1_VI.glob("*.md")))
    missing = [s for s in PI1_USED if s not in text and cap(s) not in text]
    assert not missing, missing
    for bid in SENSE_P1.values():
        p1_body(bid)
    return len(PI1_USED)


def notes_md():
    L = ["# pi-2 Vietnamese rails: new formulas of chapters 2 and 3 (^2-154 … ^2-188)", "",
         "Generated by build_rails_2_3_vi.py; import it instead of retyping. Strings already in vi-rails-formulas.md "
         "(sample) or notes-1.md are not repeated. Format: Pāli = tiếng Việt.", "",
         "## Āyatanavibhaṅga", "",
         f"Dvādasāyatanāni – cakkhāyatanaṃ, rūpāyatanaṃ, … dhammāyatanaṃ. = {AY12_S}",
         f"(Abhidhamma order) = {AY12_A}",
         f"Cakkhuṃ aniccaṃ dukkhaṃ anattā vipariṇāmadhammaṃ. / Rūpā aniccā … vipariṇāmadhammā. = Mắt {IMPERM}. / "
         f"Các hình sắc {IMPERM}.",
         f"Tattha katamaṃ <X>āyatanaṃ? = {q('lĩnh vực X')}",
         f"Idaṃ vuccati \"<X>āyatanaṃ\". = {called_q('lĩnh vực X', dash=False)}",
         "Yaṃ cakkhu … suñño gāmopeso / Yaṃ rūpaṃ … rūpadhātupesā (sense-base definitions) = the pi-1 Vietnamese "
         "body (^1-596, 600, 604, 608, 612, 616, 620, 624, 628, 647) with the pi-2 variant brackets",
         f"[cakkhuṃ (sī. syā. ka.) dha. sa. 596-599] = {EYE_VAR}",
         "[pītaṃ lohitaṃ (sī.)] = [dị bản (Sī.): pītaṃ lohitaṃ]; [mutiṅgasaddho (sī.)] = [khác chính tả (Sī.): "
         "mutiṅgasaddho]; [lapilakaṃ (sī.), lampikaṃ (ka. sī.)] = [dị bản (Sī.): lapilakaṃ; (Ka., Sī.): lampikaṃ]",
         f"N-vidhena manāyatanaṃ – … / Evaṃ N-vidhena manāyatanaṃ. = {mana_head(2)} … / {mana_end(2)}",
         f"…pe…. Evaṃ bahuvidhena manāyatanaṃ. Idaṃ vuccati \"manāyatanaṃ\". = … {mana_end('many')} "
         f"{called_q(MANA, dash=False)}",
         f"Tattha katamo vedanākkhandho? Ekavidhena … …pe… evaṃ dasavidhena vedanākkhandho…pe… evaṃ bahuvidhena "
         f"vedanākkhandho. Ayaṃ vuccati \"vedanākkhandho\". = {K1.agg_q('vedana')} … … "
         f"{low(K1.vidha_end(10, 'vedana'))[:-1]}… {low(K1.vidha_end('many', 'vedana'))[:-1]}. "
         f"{called_q(K1.KH['vedana'], dash=False)}",
         f"Tattha katamaṃ dhammāyatanaṃ? Vedanākkhandho, saññākkhandho, saṅkhārakkhandho, yañca rūpaṃ "
         f"anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ, asaṅkhatā ca dhātu. = {q(AY['dhamma'])} {DHAMMA_MEMBERS}.",
         f"Tattha katamaṃ rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ? Itthindriyaṃ purisindriyaṃ…pe… "
         f"kabaḷīkāro āhāro. Idaṃ vuccati rūpaṃ \"…\". = {anid_line(2)}",
         f"Tattha katamā asaṅkhatā dhātu? Rāgakkhayo, dosakkhayo, mohakkhayo – ayaṃ vuccati \"asaṅkhatā dhātu\". = "
         f"{q(DH['asaṅkhatā'])} {NIBBANA} {called_q(DH['asaṅkhatā'])}",
         f"Idaṃ vuccati dhammāyatanaṃ. = {FIXED['Idaṃ vuccati dhammāyatanaṃ.']}",
         f"Āyatanavibhaṅgo niṭṭhito. = {FIXED['Āyatanavibhaṅgo niṭṭhito.']}",
         "", "## Dhātuvibhaṅga", "",
         f"Cha dhātuyo – pathavīdhātu … viññāṇadhātu. = Sáu yếu tố – {', '.join(DH[k] for k in SIX_A)}.",
         "[paṭhavīdhātu (sī. syā.) evamuparipi] = [khác chính tả (Sī., Syā.): paṭhavīdhātu, cũng vậy ở các chỗ sau]",
         "Pathavīdhātudvayaṃ – atthi ajjhattikā, atthi bāhirā. = Yếu tố đất có hai loại – có loại thuộc phần bên "
         "trong, có loại thuộc phần bên ngoài.",
         f"ajjhattikā / bāhirā pathavīdhātu = {int_name('pathavī')} / {ext_name('pathavī')}",
         f"Yaṃ ajjhattaṃ paccattaṃ <core> ajjhattaṃ upādinnaṃ, seyyathidaṃ – … = {head_int('<core>')}, {NAMELY} …",
         f"yaṃ vā panaññampi atthi ajjhattaṃ paccattaṃ <core> ajjhattaṃ upādinnaṃ = {other_int('<core>')}",
         f"Yaṃ bāhiraṃ <core> bahiddhā anupādinnaṃ = {head_ext('<core>')}",
         f"– ayaṃ vuccati ‘ajjhattikā pathavīdhātu’. = {called_sq(int_name('pathavī'))}",
         f"Yā ca ajjhattikā pathavīdhātu yā ca bāhirā pathavīdhātu, tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā – "
         f"ayaṃ vuccati \"pathavīdhātu\". = {cap(int_name('pathavī'))} và {ext_name('pathavī')}, {TOGETHER} "
         f"{called_q(DH['pathavī'])}",
     ] + [f"core {k} = {CORE[k].format(v='', by='<by>')}" for k in CORE] + [
         f"maṃsalohitehi / catūhi mahābhūtehi (asamphuṭṭhaṃ) = {BY_FLESH} / {BY_GREAT}",
         f"asitapītakhāyitasāyitaṃ = {EATEN}",
     ] + [f"list {k} = {v}" for k, v in LISTS.items()] + [
         f"Imā cha dhātuyo. = {THESE_SIX}",
         f"Aparāpi cha dhātuyo – = {MORE_SIX}",
         f"Tattha katamā sukhadhātu? Yaṃ kāyikaṃ sātaṃ … – ayaṃ vuccati \"sukhadhātu\". = {q(DH['sukha'])} {WHICH} "
         f"… {called_dh('sukha')}",
     ] + [f"feeling {k} = {v}" for k, v in FEELING_P1.items()] + [
         f"Yaṃ aññāṇaṃ … akusalamūlaṃ = {WHICH} {MOHA_P1}",
         f"Kāmapaṭisaṃyutto takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā micchāsaṅkappo = "
         f"{thought('kāma', True)}",
         f"Byāpādapaṭisaṃyutto takko vitakko…pe… micchāsaṅkappo = {thought('byāpāda', False)}",
     ] + [f"X-paṭisaṃyutto ({k}) = {v}" for k, v in CONNECTED.items()] + [
         f"Heṭṭhato avīcinirayaṃ … saṅkhārā viññāṇaṃ = {KAMA2}",
         f"Dasasu vā āghātavatthūsu cittassa āghāto … anattamanatā cittassa = {DOSA_LIST}",
         f"Idhekacco pāṇinā vā … parūpaghāto = {VIHIMSA2}",
         f"Sabbepi kusalā dhammā \"nekkhammadhātu\". = {NEKKHAMMA2}",
         f"Yā sattesu metti … mettācetovimutti = {METTA}",
         f"Yā sattesu karuṇā … karuṇācetovimutti = {KARUNA}",
         f"Iti imāni tīṇi chakkāni tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā aṭṭhārasa dhātuyo honti. = {EIGHTEEN}",
         f"Aṭṭhārasa dhātuyo – cakkhudhātu … manoviññāṇadhātu. = {DH18_LINE}",
         f"Yaṃ cakkhu catunnaṃ mahābhūtānaṃ upādāya pasādo…pe… suñño gāmopeso = {dh_pe('cakkhu')}",
         f"Yaṃ rūpaṃ … vaṇṇanibhā…pe… rūpadhātupesā = {dh_pe('rūpa')}",
         f"Yo saddo … anidassano sappaṭigho…pe… saddadhātupesā = {dh_pe('sadda')}",
         f"Pathavīdhātu…pe… phoṭṭhabbadhātupesā = {dh_pe('phoṭṭhabba')}",
         f"Cakkhuñca paṭicca rūpe ca uppajjati cittaṃ … tajjācakkhuviññāṇadhātu = {PATICCA} {DEPEND['cakkhu']}, "
         f"{arises(DH['cakkhuviññāṇa'])}",
         f"cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho = {CITTA_SYN}",
         f"cittaṃ mano mānasaṃ…pe… = {CITTA_SHORT}",
         f"X-dhātuyā uppajjitvā niruddhasamanantarā = {AFTER.format(x='X')}",
         f"sabbadhammesu vā pana paṭhamasamannāhāro = {FIRST_ADVERT}",
         f"Ayaṃ vuccati \"dhammadhātu\". = {called_q(DH['dhamma'], dash=False)}",
         f"Dhātuvibhaṅgo niṭṭhito. = {FIXED['Dhātuvibhaṅgo niṭṭhito.']}",
         "", "## Pañhāpucchaka (both chapters)", "",
     ] + [f"{p} … ? = {v[0]}, {v[1]} …?" for p, v in GROUPS.items()] + [
         "Dasāyatanā / Dvāyatanā / Ekādasāyatanā / Pañcāyatanā / Cattāro āyatanā / Navāyatanā / Chāyatanā = Mười / Hai "
         "/ Mười một / Năm / Bốn / Chín / Sáu lĩnh vực",
         "Manāyatanaṃ / Dhammāyatanaṃ / Saddāyatanaṃ / Rūpāyatanaṃ = " + " / ".join(
             cap(AY[k]) for k in ("mana", "dhamma", "sadda", "rūpa")),
         "Soḷasa / Dasa / Pañca / Pannarasa / Cha / Sattarasa / Nava / Aṭṭha / Satta / Ekādasa / Dvādasa / Dve / Tisso "
         "dhātuyo = Mười sáu / Mười / Năm / Mười lăm / Sáu / Mười bảy / Chín / Tám / Bảy / Mười một / Mười hai / Hai "
         "/ Ba yếu tố",
         "Kāyaviññāṇadhātu / Manoviññāṇadhātu / Dhammadhātu / Manodhātu / Saddadhātu / Rūpadhātu = " + " / ".join(
             cap(DH[k]) for k in ("kāyaviññāṇa", "manoviññāṇa", "dhamma", "mano", "sadda", "rūpa")),
         f"X siyā A, siyā B, na vattabbā – \"C\"ti. = X đôi khi A, đôi khi B; {low(NV_TOPIC.format(s='chúng'))} "
         f"rằng “C”.",
         f"kenaci viññeyyā, kenaci na viññeyyā (after siyā …;) = chúng {kenaci('lĩnh vực')} / chúng {kenaci('yếu tố')}",
         f"sappaccayo / appaccayo; saṅkhato / asaṅkhato = có điều kiện / {LOCAL['appaccayo']}; do điều kiện tạo thành "
         f"/ {LOCAL['asaṅkhato']}",
         f"sukhasahagatā said of Kāyaviññāṇadhātu = {SUBJ_SENSE[('Kāyaviññāṇadhātu', 'sukhasahagato')]}",
         "", "## Slips of the source translated as written (^2-171)", "",
     ] + [f"{k} = {v}" for k, v in LOCAL.items() if LOCAL_SLIP.get(k)]
    return unicodedata.normalize("NFC", "\n".join(L) + "\n")


def main():
    for part, ch in (("2-ayatanavibhango.md", 2), ("3-dhatuvibhango.md", 3)):
        pali, h = build(part, ch)
        text = render(pali, h)
        (S.OUT / part).write_bytes(text.encode("utf-8"))
        print(f"wrote {part}: {len(h)} segments")
    n = check_pi1()
    NOTES_PATH.write_bytes(notes_md().encode("utf-8"))
    print(f"pi-1 strings checked: {n}; notes-2-3.md written")
    for s in SLIPS:
        print("slip:", s)
    for s in MISFITS:
        print("misfit:", s)


if __name__ == "__main__":
    main()
