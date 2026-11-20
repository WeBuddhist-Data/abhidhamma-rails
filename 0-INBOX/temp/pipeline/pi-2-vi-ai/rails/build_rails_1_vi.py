"""Builder for the Vietnamese rails translation of pi-2 (Vibhaṅga, «Phân tích các hiện tượng», plain audience),
chapter 1 (Khandhavibhaṅgo, «Phân tích các khối»).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/1-khandhavibhango.md
      = 0-INBOX/temp/pipeline/pi-2-vi-ai/rails/sample-1/1-sample.md (byte-for-byte, ^2-1-0 … ^2-33)
        + the rest of the chapter (^2-1-2-2-0 … ^2-153) built here
  0-INBOX/temp/pipeline/pi-2-vi-ai/rails/notes-1.md   (new recurring formulas, Pāli = tiếng Việt)

Every Vietnamese string comes from the fixed tables and functions below, so identical Pāli gives identical
Vietnamese. The approved sample builder is imported read-only (S). The matrix predicates are the approved pi-1
Vietnamese rails names (AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/1-matika.md, after
the pi-1 review fixes); check_pi1() compares them line by line with that file and lists any difference.

Later chapters may import this module (importing writes nothing):
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-2-vi-ai\\rails")
    import build_rails_1_vi as K1
    K1.ITEMS (key = Pāli masculine singular -> attributive phrase), K1.pred(key) (predicative phrase),
    K1.item(key), K1.abhi_line(p), K1.panha_line(p), K1.panha_question(p), K1.FIXED, K1.APARO, K1.NUMX

usage: python -I -X utf8 build_rails_1_vi.py
"""
import pathlib
import re
import sys
import unicodedata

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)

PART = "1-khandhavibhango.md"
SRC = S.PALI / PART
TARGET = S.OUT / PART
SAMPLE_VI = RAILS / "sample-1" / "1-sample.md"
NOTES_PATH = RAILS / "notes-1.md"
PI1_VI = S.ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters" / "1-matika.md"
PI1_PA = S.ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / "1-matika.md"
cap = S.cap
SLIPS = []          # source slips met while building (reported)
MISFITS = []        # termbase gaps / misfits met while building (reported)


def low(s):
    return s[0].lower() + s[1:]


def note(lst, s):
    if s not in lst:
        lst.append(s)


# =========================================================================== matrix items
# key = Pāli masculine singular (as said of «-kkhandho»); value = the attributive phrase, as in the pi-1
# matrix «Các hiện tượng X» (= after «có loại …» here). PRED holds the few items that need «là» when they
# stand as the predicate (pi-1 PRED: «những hiện tượng này là thiện»).
ITEMS = {}
PRED = {}
T = {}   # triads in matrix order (Pāli keys)

T["kusala"] = ["kusalo", "akusalo", "abyākato"]
ITEMS.update(kusalo="thiện", akusalo="bất thiện", abyākato="không xác định về mặt đạo đức")
PRED.update(kusalo="là thiện", akusalo="là bất thiện")
FEEL3 = {"sukhāya": "cảm giác dễ chịu", "dukkhāya": "cảm giác khó chịu",
         "adukkhamasukhāya": "cảm giác không khó chịu cũng không dễ chịu"}
T["vedana"] = [f"{k} vedanāya sampayutto" for k in FEEL3]
for _k, _v in FEEL3.items():
    ITEMS[f"{_k} vedanāya sampayutto"] = f"gắn liền với {_v}"
T["vipaka"] = ["vipāko", "vipākadhammadhammo", "nevavipākanavipākadhammadhammo"]
ITEMS.update(vipāko="là quả của nghiệp", vipākadhammadhammo="có khả năng sinh ra quả",
             nevavipākanavipākadhammadhammo="không phải là quả của nghiệp cũng không có khả năng sinh ra quả")
UPA = "là đối tượng của sự bám víu"
T["upadinna"] = ["upādinnupādāniyo", "anupādinnupādāniyo", "anupādinnaanupādāniyo"]
ITEMS.update(upādinnupādāniyo=f"do nghiệp tạo ra và {UPA}", anupādinnupādāniyo=f"không do nghiệp tạo ra nhưng {UPA}",
             anupādinnaanupādāniyo="không do nghiệp tạo ra và không phải là đối tượng của sự bám víu")
T["sankilittha"] = ["saṃkiliṭṭhasaṃkilesiko", "asaṃkiliṭṭhasaṃkilesiko", "asaṃkiliṭṭhaasaṃkilesiko"]
ITEMS.update(saṃkiliṭṭhasaṃkilesiko="bị phiền não làm vẩn đục và là đối tượng của phiền não",
             asaṃkiliṭṭhasaṃkilesiko="không bị phiền não làm vẩn đục nhưng là đối tượng của phiền não",
             asaṃkiliṭṭhaasaṃkilesiko="không bị phiền não làm vẩn đục và không phải là đối tượng của phiền não")
T["vitakka"] = ["savitakkasavicāro", "avitakkavicāramatto", "avitakkaavicāro"]
ITEMS.update(savitakkasavicāro="có sự hướng tâm và sự duy trì tâm",
             avitakkavicāramatto="không có sự hướng tâm, chỉ có sự duy trì tâm",
             avitakkaavicāro="không có sự hướng tâm cũng không có sự duy trì tâm")
T["piti"] = ["pītisahagato", "sukhasahagato", "upekkhāsahagato"]
for _k, _v in zip(T["piti"], ["sự hân hoan", "hạnh phúc", "sự bình thản"]):
    ITEMS[_k] = f"có {_v} đi kèm"
    ITEMS["na " + _k] = f"không có {_v} đi kèm"
T_SEE = "cần dứt bỏ bằng sự thấy chân lý"             # dassanena pahātabbo
T_DEV = "cần dứt bỏ bằng sự tu tập"                    # bhāvanāya pahātabbo
R_SEE = "có gốc rễ cần dứt bỏ bằng sự thấy chân lý"    # dassanena pahātabbahetuko
R_DEV = "có gốc rễ cần dứt bỏ bằng sự tu tập"          # bhāvanāya pahātabbahetuko
NR_SEE = "không có gốc rễ nào cần dứt bỏ bằng sự thấy chân lý"    # pi-1 review fix r1#1
NR_DEV = "không có gốc rễ nào cần dứt bỏ bằng sự tu tập"
T["dassana"] = ["dassanena pahātabbo", "bhāvanāya pahātabbo", "neva dassanena na bhāvanāya pahātabbo"]
T["dassanahetu"] = ["dassanena pahātabbahetuko", "bhāvanāya pahātabbahetuko",
                    "neva dassanena na bhāvanāya pahātabbahetuko"]
ITEMS.update({"dassanena pahātabbo": T_SEE, "bhāvanāya pahātabbo": T_DEV,
              "neva dassanena na bhāvanāya pahātabbo": f"không {T_SEE} cũng không {T_DEV}",
              "na dassanena pahātabbo": f"không {T_SEE}", "na bhāvanāya pahātabbo": f"không {T_DEV}",
              "dassanena pahātabbahetuko": R_SEE, "bhāvanāya pahātabbahetuko": R_DEV,
              "neva dassanena na bhāvanāya pahātabbahetuko": f"{NR_SEE}, cũng {NR_DEV}",
              "na dassanena pahātabbahetuko": NR_SEE, "na bhāvanāya pahātabbahetuko": NR_DEV})
T["acaya"] = ["ācayagāmī", "apacayagāmī", "nevācayagāmināpacayagāmī"]
ITEMS.update(ācayagāmī="dẫn đến sự tích lũy", apacayagāmī="dẫn đến sự giảm trừ",
             nevācayagāmināpacayagāmī="không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ")
T["sekkha"] = ["sekkho", "asekkho", "nevasekkhanāsekkho"]
ITEMS.update(sekkho="thuộc về người còn đang tu học", asekkho="thuộc về người đã hoàn tất tu học",
             nevasekkhanāsekkho="không thuộc về người còn đang tu học cũng không thuộc về người đã hoàn tất tu học")
T["paritta"] = ["paritto", "mahaggato", "appamāṇo"]
ITEMS.update(paritto="hạn hẹp", mahaggato="rộng lớn", appamāṇo="không thể đo lường")
T["parittarammana"] = ["parittārammaṇo", "mahaggatārammaṇo", "appamāṇārammaṇo"]
ITEMS.update(parittārammaṇo="có đối tượng hạn hẹp", mahaggatārammaṇo="có đối tượng rộng lớn",
             appamāṇārammaṇo="có đối tượng không thể đo lường")
T["hina"] = ["hīno", "majjhimo", "paṇīto"]
ITEMS.update(hīno="thấp kém", majjhimo="trung bình", paṇīto="ưu việt")
T["miccha"] = ["micchattaniyato", "sammattaniyato", "aniyato"]
ITEMS.update(micchattaniyato="cố định theo hướng sai lầm", sammattaniyato="cố định theo hướng đúng đắn",
             aniyato="không cố định", niyato="cố định")
T["magga"] = ["maggārammaṇo", "maggahetuko", "maggādhipati"]
ITEMS.update(maggārammaṇo="lấy con đường làm đối tượng", maggahetuko="lấy con đường làm gốc rễ",
             maggādhipati="lấy con đường làm yếu tố chủ đạo")
T["uppanna"] = ["uppanno", "anuppanno", "uppādī"]
ITEMS.update(uppanno="đã sinh khởi", anuppanno="chưa sinh khởi", uppādī="sẽ sinh khởi")
T["atita"] = ["atīto", "anāgato", "paccuppanno"]
ITEMS.update(atīto="thuộc quá khứ", anāgato="thuộc tương lai", paccuppanno="thuộc hiện tại")
T["atitarammana"] = ["atītārammaṇo", "anāgatārammaṇo", "paccuppannārammaṇo"]
ITEMS.update(atītārammaṇo="có đối tượng thuộc quá khứ", anāgatārammaṇo="có đối tượng thuộc tương lai",
             paccuppannārammaṇo="có đối tượng thuộc hiện tại")
T["ajjhatta"] = ["ajjhatto", "bahiddho", "ajjhattabahiddho"]
ITEMS.update(ajjhatto="ở nơi bản thân", bahiddho="ở bên ngoài bản thân",
             ajjhattabahiddho="ở nơi bản thân và ở bên ngoài bản thân")
T["ajjhattarammana"] = ["ajjhattārammaṇo", "bahiddhārammaṇo", "ajjhattabahiddhārammaṇo"]
ITEMS.update(ajjhattārammaṇo="có đối tượng ở nơi bản thân", bahiddhārammaṇo="có đối tượng ở bên ngoài bản thân",
             ajjhattabahiddhārammaṇo="có đối tượng ở nơi bản thân và ở bên ngoài bản thân")
T["sanidassana"] = ["sanidassanasappaṭigho", "anidassanasappaṭigho", "anidassanaappaṭigho"]
ITEMS.update(sanidassanasappaṭigho="thấy được và có tính va chạm",
             anidassanasappaṭigho="không thấy được nhưng có tính va chạm",
             anidassanaappaṭigho="không thấy được và không có tính va chạm")
TRIAD_ORDER = list(T)

# ---- dyads: the roots group (pi-1 1-M2-1 … 1-M2-6; the «na hetu» pair as pi-1 ^1-1452)
ITEMS.update({"hetu": "là gốc rễ", "na hetu": "không phải là gốc rễ", "sahetuko": "có gốc rễ",
              "ahetuko": "không có gốc rễ", "hetusampayutto": "gắn liền với gốc rễ",
              "hetuvippayutto": "không gắn liền với gốc rễ",
              "hetu ceva sahetuko ca": "vừa là gốc rễ vừa có gốc rễ",
              "sahetuko ceva na ca hetu": "có gốc rễ nhưng không phải là gốc rễ",
              "hetu ceva hetusampayutto ca": "vừa là gốc rễ vừa gắn liền với gốc rễ",
              "hetusampayutto ceva na ca hetu": "gắn liền với gốc rễ nhưng không phải là gốc rễ",
              "na hetu sahetuko": "không phải là gốc rễ nhưng có gốc rễ",
              "na hetu ahetuko": "không phải là gốc rễ và không có gốc rễ"})
# ---- lesser intermediate pairs (1-M2-7 … 1-M2-13)
ITEMS.update(sappaccayo="có điều kiện", saṅkhato="do điều kiện tạo thành", sanidassano="thấy được",
             anidassano="không thấy được", sappaṭigho="có tính va chạm", appaṭigho="không có tính va chạm",
             lokiyo="thuộc thế gian", lokuttaro="vượt thế gian")
ITEMS["rūpaṃ"] = "vật chất"                        # Rūpakkhandho rūpaṃ (termbase rūpaṃ «vật chất»)
PRED["rūpaṃ"] = "là vật chất"
ITEMS["arūpo"] = "phi vật chất"                    # Cattāro khandhā arūpā (pi-1 arūpino)
PRED["arūpo"] = "là phi vật chất"
ITEMS["kenaci viññeyyo"] = "mà một loại thức nào đó có thể nhận biết"
ITEMS["kenaci na viññeyyo"] = "mà một loại thức nào đó không thể nhận biết"

# ---- the clusters (taints … defilements), pi-1 1-M2-14 … 1-M2-82
# (noun key, prone key, notprone key, stem, Vietnamese noun, prone phrase, notprone phrase)
CL = {
    "āsava": ("āsavo", "sāsavo", "anāsavo", "āsava", "ô nhiễm", None, None),
    "saṃyojana": ("saṃyojanaṃ", "saṃyojaniyo", "asaṃyojaniyo", "saṃyojana", "xiềng xích", None, None),
    "gantha": ("gantho", "ganthaniyo", "aganthaniyo", "gantha", "nút thắt", None, None),
    "ogha": ("ogho", "oghaniyo", "anoghaniyo", "ogha", "dòng lũ", None, None),
    "yoga": ("yogo", "yoganiyo", "ayoganiyo", "yoga", "ách", None, None),
    "nīvaraṇa": ("nīvaraṇaṃ", "nīvaraṇiyo", "anīvaraṇiyo", "nīvaraṇa", "chướng ngại", None, None),
    "parāmāsa": ("parāmāso", "parāmaṭṭho", "aparāmaṭṭho", "parāmāsa", "sự hiểu sai lệch",
                 "bị sự hiểu sai lệch nắm giữ", "không bị sự hiểu sai lệch nắm giữ"),
    "upādāna": ("upādānaṃ", "upādāniyo", "anupādāniyo", "upādāna", "sự bám víu", None, None),
    "kilesa": ("kileso", "saṃkilesiko", "asaṃkilesiko", "kilesa", "phiền não", None, None),
}


def _ceva(n):
    """Pāli «X ceva»: neuter -aṃ takes «-ñceva»"""
    return n[:-1] + "ñceva" if n.endswith("ṃ") else n + " ceva"


def both(a, b):
    """X ceva … Y ca: «vừa X vừa Y» (pi-1)"""
    return f"vừa {a} vừa {b}"


def but_not(a, b):
    """X ceva … na/no ca Y: «X nhưng Y-negated» (pi-1)"""
    return f"{a} nhưng {b}"


def _cluster(c):
    n, pr, npr, st, x, prone, notprone = CL[c]
    is_, isnot = f"là {x}", f"không phải là {x}"
    prone = prone or f"là đối tượng của {x}"
    notprone = notprone or f"không phải là đối tượng của {x}"
    assoc, dissoc = f"gắn liền với {x}", f"không gắn liền với {x}"
    ITEMS[n] = is_
    ITEMS["no " + n] = isnot
    ITEMS[pr] = prone
    ITEMS[npr] = notprone
    ITEMS[st + "sampayutto"] = assoc
    ITEMS[st + "vippayutto"] = dissoc
    ITEMS[f"{_ceva(n)} {pr} ca"] = both(is_, prone)
    ITEMS[f"{pr} ceva no ca {n}"] = but_not(prone, isnot)
    ITEMS[f"{_ceva(n)} {st}sampayutto ca"] = both(is_, assoc)
    ITEMS[f"{st}sampayutto ceva no ca {n}"] = but_not(assoc, isnot)
    ITEMS[f"{st}vippayutta{pr}"] = but_not(dissoc, prone)                    # pi-1 ^1-1476 …
    a = "" if npr.startswith("a") else "a"
    ITEMS[f"{st}vippayutta{a}{npr}"] = f"{dissoc} và {notprone}"


for _c in CL:
    _cluster(_c)
# kilesa: the «defiled» pairs (1-M2-77, 1-M2-80)
ITEMS.update(saṃkiliṭṭho="bị phiền não làm vẩn đục", asaṃkiliṭṭho="không bị phiền não làm vẩn đục")
ITEMS["kileso ceva saṃkiliṭṭho ca"] = both("là phiền não", "bị phiền não làm vẩn đục")
ITEMS["saṃkiliṭṭho ceva no ca kileso"] = but_not("bị phiền não làm vẩn đục", "không phải là phiền não")

# ---- greater intermediate pairs (1-M2-55 … 1-M2-68)
ITEMS.update(sārammaṇo="có đối tượng", anārammaṇo="không có đối tượng",
             cetasiko="là yếu tố đồng hành với tâm", acetasiko="không phải là yếu tố đồng hành với tâm",
             cittasampayutto="gắn liền với tâm", cittavippayutto="không gắn liền với tâm",
             cittasaṃsaṭṭho="hòa lẫn với tâm", cittavisaṃsaṭṭho="không hòa lẫn với tâm",
             cittasamuṭṭhāno="do tâm sinh ra", cittasahabhū="cùng tồn tại với tâm",
             cittānuparivatti="vận hành theo tâm",
             cittasaṃsaṭṭhasamuṭṭhāno="vừa hòa lẫn với tâm vừa do tâm sinh ra",
             cittasaṃsaṭṭhasamuṭṭhānasahabhū="vừa hòa lẫn với tâm vừa do tâm sinh ra vừa cùng tồn tại với tâm",
             cittasaṃsaṭṭhasamuṭṭhānānuparivatti="vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm",
             ajjhattiko="thuộc phần bên trong", bāhiro="thuộc phần bên ngoài",
             upādā="phái sinh", upādinno="do nghiệp tạo ra", anupādinno="không do nghiệp tạo ra")
ITEMS["no upādā"] = "không phải là phái sinh"
PRED["upādā"] = "là phái sinh"                      # pi-1 PRED, sample ^2-33 «thì là phái sinh»
ITEMS["cittaṃ"] = "là tâm"
ITEMS["no cittaṃ"] = "không phải là tâm"
for _k in ("cittasamuṭṭhāno", "cittasahabhū", "cittānuparivatti"):
    ITEMS["no " + _k] = "không " + ITEMS[_k]
for _k in ("cittasaṃsaṭṭhasamuṭṭhāno", "cittasaṃsaṭṭhasamuṭṭhānasahabhū", "cittasaṃsaṭṭhasamuṭṭhānānuparivatti"):
    ITEMS["no " + _k] = "không phải " + ITEMS[_k]
ITEMS["cittena sampayutto"] = ITEMS["cittasampayutto"]      # pi-1 ^1-1532
ITEMS["cittena vippayutto"] = ITEMS["cittavippayutto"]
ITEMS["cittena saṃsaṭṭho"] = ITEMS["cittasaṃsaṭṭho"]        # pi-1 ^1-1534
ITEMS["cittena visaṃsaṭṭho"] = ITEMS["cittavisaṃsaṭṭho"]

# ---- final pairs (1-M2-83 … 1-M2-100)
ITEMS.update(savitakko="có sự hướng tâm", avitakko="không có sự hướng tâm", savicāro="có sự duy trì tâm",
             avicāro="không có sự duy trì tâm", sappītiko="có sự hân hoan", appītiko="không có sự hân hoan",
             pariyāpanno="nằm trong các cõi tồn tại", apariyāpanno="không nằm trong các cõi tồn tại",
             niyyāniko="dẫn đến giải thoát", aniyyāniko="không dẫn đến giải thoát",
             sauttaro="còn có điều cao hơn", anuttaro="không có điều gì cao hơn",
             saraṇo="có xung đột", araṇo="không có xung đột")
for _k, _v in (("kāmāvacaro", "cõi dục lạc"), ("rūpāvacaro", "cõi hình sắc"), ("arūpāvacaro", "cõi không hình sắc")):
    ITEMS[_k] = f"thuộc {_v}"
    ITEMS["na " + _k] = f"không thuộc {_v}"

# ---- aggregate-specific classes (termbase)
ITEMS["phassasampayutto"] = "gắn liền với sự tiếp xúc"          # termbase phassasampayutto
for _k, _v in (("sukhindriya", "dễ chịu"), ("dukkhindriya", "khó chịu"), ("somanassindriya", "niềm vui"),
               ("domanassindriya", "nỗi buồn"), ("upekkhindriya", "bình thản")):
    ITEMS[_k + "ṃ"] = f"là năng lực {_v}"                         # termbase sukhindriyaṃ «năng lực dễ chịu» …
    ITEMS[_k + "sampayutto"] = f"gắn liền với năng lực {_v}"       # termbase sukhindriyasampayutto
# said of a noun phrase (vedanā / saññā / cetanā / viññāṇa of the body)
ITEMS["sukhā#np"] = "dễ chịu"                                    # kāyasamphassajā vedanā atthi sukhā
ITEMS["dukkhā#np"] = "khó chịu"                                  # … atthi dukkhā
ITEMS["sukhasahagata#np"] = "có sự dễ chịu đi kèm"               # termbase sukhasahagataṃ (body-consciousness)
ITEMS["dukkhasahagata#np"] = "có sự khó chịu đi kèm"             # pi-1 ^1-1388 «thức qua thân có sự khó chịu đi kèm»
ITEMS["pītisahagato na sukhasahagato na upekkhāsahagato"] = (
    "có sự hân hoan đi kèm nhưng không có hạnh phúc đi kèm và không có sự bình thản đi kèm")

ALIAS = {"na hetusahetuko": "na hetu sahetuko", "na hetuahetuko": "na hetu ahetuko",
         "āsavippayuttaanāsavo": "āsavavippayuttaanāsavo"}
ALIAS_SLIP = {
    "na hetusahetuko": "«na hetusahetuko / na hetuahetuko» written as one word (^2-36, 40, 45; ^2-131 has "
                       "«na hetuahetuko»); elsewhere «na hetu …»: plain spelling, rendered the same",
    "na hetuahetuko": "«na hetusahetuko / na hetuahetuko» written as one word (^2-36, 40, 45; ^2-131 has "
                      "«na hetuahetuko»); elsewhere «na hetu …»: plain spelling, rendered the same",
    "āsavippayuttaanāsavo": "^2-113 «āsavippayuttaanāsavo» for «āsavavippayuttaanāsavo» (spelling slip, "
                            "rendered as meant)"}


def item(key):
    if key in ALIAS_SLIP:
        note(SLIPS, ALIAS_SLIP[key])
    key = ALIAS.get(key, key)
    return ITEMS[key]


def pred(key):
    """the phrase as a predicate (after a subject or «đôi khi»)"""
    k = ALIAS.get(key, key)
    if k in PRED:
        return PRED[k]
    return item(key)


# ---- Pāli plural of a key (question section: «cattāro khandhā siyā kusalā» …)
_INVAR = {"ceva", "ca", "na", "no", "neva", "dassanena", "bhāvanāya", "sukhāya", "dukkhāya", "adukkhamasukhāya",
          "vedanāya", "kenaci", "cittena", "upādā"}


def _pl_word(w):
    if w in _INVAR:
        return w
    if w.endswith("ñceva"):
        return w[:-len("añceva")] + "ā ceva"
    for a, b in (("hetu", "hetū"), ("pati", "patino"), ("vatti", "vattino")):
        if w.endswith(a):
            return w[:-len(a)] + b
    if w.endswith("aṃ"):
        return w[:-2] + "ā"
    if w.endswith("o"):
        return w[:-1] + "ā"
    if w.endswith("ī"):
        return w[:-1] + "ino"
    if w.endswith("ū"):
        return w[:-1] + "uno"
    return w


def pali_plural(key):
    return " ".join(_pl_word(w) for w in key.split(" "))


PL_KEY = {}
for _k in list(ITEMS):
    if "#" not in _k:
        PL_KEY.setdefault(pali_plural(_k), _k)
PL_KEY["arūpā"] = "arūpo"
# source plural forms that keep a singular noun (^2-697 «upādānañceva upādāniyā», ^2-698 «kileso ceva saṃkiliṭṭhā»):
# the Vietnamese has no number, so they take the same phrase
PL_SPECIAL = {"upādānañceva upādāniyā ca": "upādānañceva upādāniyo ca",
              "kileso ceva saṃkiliṭṭhā ca": "kileso ceva saṃkiliṭṭho ca"}


# =========================================================================== Abhidhammabhājanīya lines
NUMX = {24: "theo nhóm hai mươi bốn", 30: "theo nhóm ba mươi", "many": "theo nhiều nhóm"}   # termbase


def by_n(n):
    return NUMX[n] if n in NUMX else S.by_n(n)


NUMP = {"eka": 1, "du": 2, "ti": 3, "catub": 4, "pañca": 5, "chab": 6, "satta": 7, "aṭṭha": 8, "nava": 9,
        "dasa": 10, "ekādasa": 11, "catuvīsati": 24, "tiṃsa": 30, "tiṃsati": 30, "bahu": "many"}
KHP = {"rūpakkhandho": "rupa", "vedanākkhandho": "vedana", "saññākkhandho": "sanna",
       "saṅkhārakkhandho": "sankhara", "viññāṇakkhandho": "vinnana"}
KH = {a: S.AGG[a]["k"] for a in S.FIVE}            # khối vật chất, khối cảm giác …
APARO = "Một cách khác,"                           # Aparopi (no termbase entry; reported)
DUKAMULA = "Phần dựa trên bộ đôi."                 # Dukamūlakaṃ. (termbase Duka «bộ đôi», mūlakaṃ «dựa trên»)
TIKAMULA = "Phần dựa trên bộ ba."                  # Tikamūlakaṃ. (Tika «bộ ba»)
UBHATO = "Phần mở rộng cả hai phía."               # Ubhatovaḍḍhakaṃ. (Ubhato «cả hai phía», vaḍḍhakaṃ «mở rộng»)
YATHA_KUSALATTIKE = ("(Như bộ ba về thiện đã được trình bày chi tiết, tất cả các bộ ba cũng nên được trình bày "
                     "chi tiết như vậy.)")         # (Yathā kusalattike vitthāro, evaṃ sabbepi tikā vitthāretabbā.)
TIKA_H = "Bộ ba"                                   # ##### Tikaṃ (termbase Tikaṃ «bộ ba»)
DUKA_H = "Bộ đôi"                                  # ##### Dukaṃ (termbase Dukaṃ «bộ đôi»)
DONE = "đã hoàn tất"                               # niṭṭhito (pi-1 «Ma trận đã hoàn tất»)
FIXED = {
    "Dukamūlakaṃ.": DUKAMULA,
    "Tikamūlakaṃ.": TIKAMULA,
    "Ubhatovaḍḍhakaṃ.": UBHATO,
    "(Yathā kusalattike vitthāro, evaṃ sabbepi tikā vitthāretabbā.)": YATHA_KUSALATTIKE,
    "Abhidhammabhājanīyaṃ.": f"{S.SEC_HEADINGS['Abhidhammabhājanīyaṃ']}.",
    "Suttantabhājanīyaṃ.": f"{S.SEC_HEADINGS['Suttantabhājanīyaṃ']}.",
    "Pañhāpucchakaṃ.": f"{S.SEC_HEADINGS['Pañhāpucchakaṃ']}.",
    "Khandhavibhaṅgo niṭṭhito.": f"{S.CH_HEADINGS['Khandhavibhaṅgo']} {DONE}.",
}

SENSE = {"cakkhu": "mắt", "sota": "tai", "ghāna": "mũi", "jivhā": "lưỡi", "kāya": "thân", "mano": "ý",
         "manodhātu": "yếu tố ý", "manoviññāṇadhātu": "yếu tố ý thức"}
JA_NOUN = {"vedanā": "cảm giác", "saññā": "tri giác", "cetanā": "chủ ý"}
VINN = {"cakkhu": "thức qua mắt", "sota": "thức qua tai", "ghāna": "thức qua mũi", "jivhā": "thức qua lưỡi",
        "kāya": "thức qua thân", "mano": "ý thức"}
NP_PACC = re.compile(r"^(cakkhu|sota|ghāna|jivhā|kāya|mano)samphassapaccayā(?: (\S+kkhandho))?$")
NP_JA = re.compile(r"^(cakkhu|sota|ghāna|jivhā|kāya|manoviññāṇadhātu|manodhātu|mano)samphassajā (vedanā|saññā|cetanā)$")
NP_VIN = re.compile(r"^(cakkhu|sota|ghāna|jivhā|kāya|mano)viññāṇaṃ$")


def paccaya_np(sense, kh=None):
    """Xsamphassapaccayā [Ykkhandho] = «[khối Y ]có sự tiếp xúc của X làm điều kiện»
    (termbase samphassa «sự tiếp xúc», paccayā «làm điều kiện cho»: «cho» drops in this word order)"""
    r = f"có sự tiếp xúc của {SENSE[sense]} làm điều kiện"
    return f"{KH[KHP[kh]]} {r}" if kh else r


def np_(t):
    """Pāli noun phrase -> (Vietnamese, is_paccaya) or None"""
    t = t[:1].lower() + t[1:]
    m = NP_PACC.match(t)
    if m:
        note(MISFITS, "paccayā (termbase «làm điều kiện cho», dependent-origination sense) in "
                      "«cakkhusamphassapaccayā vedanākkhandho» (^2-61, 91, 120, 149): written «khối cảm giác có sự "
                      "tiếp xúc của mắt làm điều kiện» («cho» cannot stand in this noun phrase)")
        return paccaya_np(m.group(1), m.group(2)), True
    m = NP_JA.match(t)
    if m:
        return f"{JA_NOUN[m.group(2)]} sinh từ sự tiếp xúc của {SENSE[m.group(1)]}", False
    m = NP_VIN.match(t)
    if m:
        return VINN[m.group(1)], False
    if t in ("manodhātu", "manoviññāṇadhātu"):
        return SENSE[t], False
    return None


def _atthi_key(k, ctx_np):
    """Pāli class word after «atthi» -> ITEMS key"""
    if ctx_np:
        for p, key in (("sukhasahagat", "sukhasahagata#np"), ("dukkhasahagat", "dukkhasahagata#np")):
            if k.startswith(p):
                return key
        if k in ("sukhā", "dukkhā"):
            return k + "#np"
    if k in ITEMS or k in ALIAS:
        return k
    for a, b in (("ā", "o"), ("aṃ", "o")):
        if k.endswith(a) and k[:-len(a)] + b in ITEMS:
            return k[:-len(a)] + b
    raise KeyError(k)


SOME = S.SOME                                       # «có loại» (sample / pi-1 atthi)
DELIM = {",": ",", ";": ";", ".": ".", "…pe…": "…"}


def chain(body, start_cap=False):
    """Translate an Abhidhammabhājanīya body (classes, noun phrases, «atthi …» runs).
    A noun phrase with an «atthi» tail becomes «NP: có loại X, có loại Y», and the comma after such a member
    becomes «;» (sample ^2-33, matter by eight)."""
    parts = re.split(r"(…pe…|[,;.])", body)
    E = []          # elements: dict(t=kind, s=text, lead=space before)
    ctx_np = False
    for i, p in enumerate(parts):
        if i % 2 == 1:
            E.append(dict(t="sep", s=p))
            if p in ".;":
                ctx_np = False
            continue
        if not p.strip():
            continue
        lead = p[:1] == " "
        t = p.strip()
        pieces = re.split(r"\s+(?=atthi\s)", t)
        first, rest = pieces[0], pieces[1:]
        if re.match(r"^[Aa]tthi\s", first):
            rest = pieces
        else:
            r = np_(first)
            if r:
                E.append(dict(t="np", s=r[0], lead=lead, pacc=r[1], tail=bool(rest)))
                ctx_np = not r[1]
            else:
                E.append(dict(t="pred", s=item(first), lead=lead))
            lead = False
        for j, a in enumerate(rest):
            if j > 0:
                note(SLIPS, f"missing comma before «{a}» (comma added, rendered as meant)")
                E.append(dict(t="sep", s=","))
                lead = True
            key = _atthi_key(re.sub(r"^[Aa]tthi\s+", "", a), ctx_np)
            if E and E[-1]["t"] == "np" and E[-1].get("tail") and j == 0:
                E.append(dict(t="colon"))
            E.append(dict(t="at", s=f"{SOME} {item(key)}", lead=lead))
            lead = False
    # the comma that closes a tailed noun phrase becomes «;» when another noun phrase follows
    in_tail = False
    for k, e in enumerate(E):
        if e["t"] == "np":
            in_tail = e.get("tail", False)
        elif e["t"] == "sep" and e["s"] == "," and in_tail and k + 1 < len(E) and E[k + 1]["t"] == "np":
            e["s"] = ";"
            in_tail = False
        elif e["t"] == "sep" and e["s"] in ".;":
            in_tail = False
    out, cap_next = [], start_cap
    for e in E:
        if e["t"] == "sep":
            out.append(DELIM[e["s"]])
            if e["s"] == ".":
                cap_next = True
            continue
        if e["t"] == "colon":
            out.append(":")
            continue
        s = e["s"]
        if cap_next:
            s = cap(s)
            cap_next = False
        lead = e.get("lead") or (out and out[-1] == ":")
        out.append((" " if lead else "") + s)
    return "".join(out)


HEAD = re.compile(r"^(Tattha katamo (\S+)\? )?(Aparopi )?(\S+?)[vb]idhena (\S+kkhandho)( – | |…pe…)(.*)$")
END = re.compile(r"^(.*?)\s*\b([Ee])vaṃ (\S+?)[vb]idhena (\S+kkhandho)\.$")


def vidha(n, k):
    """N-vidhena X-kkhandho –  ->  «Khối X theo nhóm N –» (sample vidha_open)"""
    return f"{cap(KH[k])} {by_n(n)} –"


def vidha_end(n, k):
    """Evaṃ N-vidhena X-kkhandho.  ->  «Như vậy là khối X theo nhóm N.» (sample vidha_close)"""
    return f"Như vậy là {KH[k]} {by_n(n)}."


def agg_q(k):
    """Tattha katamo X-kkhandho?  ->  «Ở đây, khối X là gì?»"""
    return f"{S.TATTHA} {KH[k]} {S.IS_WHAT}"


def abhi_line(p):
    if p in FIXED:
        return FIXED[p]
    m = re.match(r"^Ayaṃ vuccati (\S+kkhandho)\.$", p)
    if m:
        return f"{cap(S.CALLED_SG)} {KH[KHP[m.group(1)]]}."
    if p.startswith("Atthi "):           # continuation line of a long list of pairs
        return chain(p, start_cap=True)
    m = HEAD.match(p)
    assert m, p
    q, qkh, aparo, nw, kh, sep, body = m.groups()
    k = KHP[kh]
    out = f"{agg_q(k)} " if q else ""
    hd = vidha(NUMP[nw.lower()], k)
    if aparo:
        hd = f"{APARO} {low(hd)}"
        note(MISFITS, f"Aparopi (no termbase entry): «{APARO} khối … theo nhóm N –» (^2-61, 91, 120, 149)")
    if sep == " – ":
        out += hd + " "
    elif sep == " ":
        note(SLIPS, f"^2-101 no dash after «{nw}vidhena {kh}» (none added; «:» written as the missing "
                    f"punctuation)")
        out += hd[:-2] + ": "
    else:                                 # «…pe…» right after the aggregate (^2-70)
        out += hd[:-2] + "…"
        body = body.lstrip()
        if body:
            out += " "
    tail = ""
    me = END.match(body)
    if me:
        body = me.group(1)
        assert KHP[me.group(4)] == k, p
        tail = vidha_end(NUMP[me.group(3).lower()], k)
        if me.group(2) == "e":
            tail = low(tail)
    if body.endswith("…pe…."):          # «…pe…. Evaṃ …»: «…» then the closing sentence (pi-1: never «….»)
        body = body[:-1]
    r = chain(body) if body else ""
    if tail:
        r = (r + " " + tail) if r else tail
    return out + r


# =========================================================================== Pañhāpucchaka
SUBJ = {  # Pāli subject -> (Vietnamese, number)
    "Rūpakkhandho": (cap(KH["rupa"]), "s"), "Vedanākkhandho": (cap(KH["vedana"]), "s"),
    "Saññākkhandho": (cap(KH["sanna"]), "s"), "Saṅkhārakkhandho": (cap(KH["sankhara"]), "s"),
    "Viññāṇakkhandho": (cap(KH["vinnana"]), "s"),
    "Cattāro khandhā": ("Bốn khối", "p"), "Tayo khandhā": ("Ba khối", "p"), "Dve khandhā": ("Hai khối", "p"),
}
GROUP = {"Pañcannaṃ khandhānaṃ": "Trong năm khối"}       # kati … ? questions
KATI = "bao nhiêu khối"                                   # kati (with the group noun)
PRON = {"s": "nó", "p": "chúng"}                          # the subject again after a «Về X thì …» clause
SIYA = "đôi khi"                                          # siyā (termbase «khandhā siyā» «khối đôi khi»)
NV = "không nên nói –"                                    # na vattabbo / vattabbā – (pi-1 ^1-1452 …)
NV_TOPIC = "Về {s} thì " + NV                             # X na vattabbo – (pi-1 «Về X thì không nên nói – rằng …»)
SAPPACCAYA = "Đều có điều kiện, đều do điều kiện tạo thành."   # Sappaccayā, saṅkhatā. (said of all five)
FIXED_SENT = {"Sappaccayā, saṅkhatā.": SAPPACCAYA}
PANHA_FIX = [  # missing punctuation of the source, rendered as meant (reported)
    ('– kilesasampayuttā ceva no ca kilesā"ti', '– "kilesasampayuttā ceva no ca kilesā"ti',
     '^2-153 (line 6) «siyā na vattabbā – kilesasampayuttā ceva no ca kilesā"ti»: opening quote missing (added)'),
]
QUOTE = re.compile(r'^"([^"]+)"(ntipi|nti|tipi|ti pi|ti)?$')
KENACI = ("là những khối mà một loại thức nào đó có thể nhận biết, còn một loại thức nào đó "
          "không thể nhận biết")              # kenaci viññeyyā, kenaci na viññeyyā (pi-1 ^1-1464 after review r4#2)


def _qkey(text, num, suffix):
    t = text
    if suffix and suffix.startswith("n"):
        t += "ṃ"
    t = re.sub(r"cā$", "ca", t)
    if num == "s":
        t = re.sub(r"hetū$", "hetu", t)
        return ALIAS.get(t, t)
    if t in PL_SPECIAL:
        note(SLIPS, f"«{t}» with a plural subject keeps the singular noun (no number in Vietnamese; same phrase)")
        return PL_SPECIAL[t]
    return PL_KEY[t]


def _pred(word, num):
    if num == "s":
        if word not in ITEMS and word not in ALIAS and word.endswith("ā") and word[:-1] + "o" in ITEMS:
            note(SLIPS, f"«{word}» (plural form) with a singular subject (^2-153; no number in Vietnamese)")
            word = word[:-1] + "o"
        return pred(word)
    return pred(PL_KEY.get(word, word))


def _render_nv(nv):
    qs = [f"rằng “{pred(k)}”" for k in nv["q"]]
    return f"{nv['head']} " + ", hay ".join(qs)


def _sentence(sent):
    """one Pañhāpucchaka sentence (without its final full stop)"""
    if sent + "." in FIXED_SENT:
        return FIXED_SENT[sent + "."][:-1]
    m = re.match(r"^(" + "|".join(sorted(SUBJ, key=len, reverse=True)) + r") (.*)$", sent)
    assert m, sent
    subj, num = SUBJ[m.group(1)]
    body = m.group(2)
    if body.endswith("āti"):                       # closing «…ti» of the whole section
        body = body[:-2]
    toks = re.split(r"(, |; |…pe… )", body)
    out = []                                       # rendered clauses and separators
    first = True
    topic = False                                  # the sentence opened with «Về X thì không nên nói – …»
    nv = None                                      # open «na vattabbā» list: dict(head, q, pending)
    for i, tok in enumerate(toks):
        if i % 2 == 1:
            s = "…" if tok == "…pe… " else tok.strip()
            if nv is None:
                out.append(s)
            else:
                nv["pending"] = s
            continue
        qm = QUOTE.match(tok)
        if qm and qm.group(2) is None:
            # «na vattabbo – "A"ti, "B".» (fetters … defilements): B stands in quotes without «ti»; it is
            # what the subject IS (as the taint group «…ti, sāsavo ceva no ca āsavo»). The quotes stay
            # (punctuation kept as written): «…; nó “B”.»
            assert nv is not None, sent
            out.append(_render_nv(nv))
            out.append(";")
            nv = None
            key = _qkey(qm.group(1), num, None)
            out.append(f"{PRON[num]} “{pred(key)}”")
            note(SLIPS, "^2-153: «na vattabbo – \"A\"ti, \"B\".» (fetters, ties, hindrances, misapprehension, "
                        "clinging, defilements): B quoted without «ti», as written; rendered «…; nó “B”.», B "
                        "being what matter is (as the taint group, unquoted there)")
            continue
        if qm:                                     # next quoted item of an open «na vattabbā» list
            assert nv is not None, sent
            nv["q"].append(_qkey(qm.group(1), num, qm.group(2)))
            nv["pending"] = None
            continue
        if nv is not None:                         # close the open list
            out.append(_render_nv(nv))
            out.append(";" if topic and nv["pending"] == "," else (nv["pending"] or ","))
            nv = None
        mv = re.match(r'^(siyā )?na vattabb[oā] – (.*)$', tok)
        if mv:
            qm = QUOTE.match(mv.group(2))
            assert qm, tok
            key = _qkey(qm.group(1), num, qm.group(2))
            if mv.group(1):
                head = f"{SIYA} {NV}"
            else:
                assert first, sent
                head = NV_TOPIC.format(s=low(subj) if subj[0].isupper() else subj)
                topic = True
            nv = dict(head=head, q=[key], pending=None)
            first = False
            continue
        for sk in SUBJ:                            # a new subject after a comma (^2-153 «appītiko, cattāro khandhā …»)
            if tok.startswith(low(sk) + " "):
                note(SLIPS, f"^2-153 «…, {low(sk)} …»: a new sentence joined by a comma (kept, subject in "
                            f"lower case)")
                subj, num = low(SUBJ[sk][0]), SUBJ[sk][1]
                tok = tok[len(sk) + 1:]
                first, topic = True, False
                break
        if tok == "kenaci viññeyyā" and toks[i + 2:i + 3] == ["kenaci na viññeyyā"]:
            v = KENACI                             # «…; chúng là những khối mà …»
            if not first:
                topic = True
        elif tok == "kenaci na viññeyyā" and toks[i - 2] == "kenaci viññeyyā":
            out.pop()                              # the comma of the pair
            continue
        else:
            siya = tok.startswith("siyā ")
            word = tok[5:] if siya else tok
            v = _pred(word, num)
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
        out.append(_render_nv(nv))
    res = ""
    for x in out:
        if x in (",", ";", "…"):
            res += x
        else:
            res += (" " if res else "") + x
    return res


def panha_line(p):
    """a line of the question section: sentences split at «. » before a capital"""
    p = p.replace('"ti pi', '"tipi')
    for bad, good, nt in PANHA_FIX:
        if bad in p:
            p = p.replace(bad, good)
            note(SLIPS, nt)
    sents = re.split(r"(?<=\.) (?=[A-Z])", p)
    res = []
    for s in sents:
        assert s.endswith("."), s
        res.append(_sentence(s[:-1]) + ".")
    return " ".join(res)


def panha_question(p):
    """Pañcannaṃ khandhānaṃ kati kusalā, kati akusalā, … kati araṇā?
    = «Trong năm khối, bao nhiêu khối là thiện, bao nhiêu khối là bất thiện, … bao nhiêu khối không có xung đột?»"""
    m = re.match(r"^(.*?) (kati .*)\?$", p)
    grp, body = m.group(1), m.group(2)
    parts = re.split(r"(…pe…|, )", body)
    out = [f"{GROUP[grp]},"]
    for i, x in enumerate(parts):
        if i % 2 == 1:
            out.append("…" if x == "…pe…" else ",")
            continue
        x = x.strip()
        if not x:
            continue
        w = re.sub(r"^kati ", "", x)
        out.append(f" {KATI} {pred(PL_KEY[w])}")
    return "".join(out) + "?"


# =========================================================================== segments
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def segs(text):
    """[(block id, [non-empty lines])]"""
    res, cur = [], []
    for ln in text.splitlines():
        if not ln.strip():
            continue
        cur.append(ln)
        m = ID.search(ln)
        if m:
            res.append((m.group(1), cur))
            cur = []
    return res


def heading(ln):
    lvl, text = ln.split(" ", 1)
    if text == "Pañhāpucchakaṃ":
        return f"{lvl} {S.SEC_HEADINGS[text]}", "panha"
    if text == "Tikaṃ":
        return f"{lvl} {TIKA_H}", None
    if text == "Dukaṃ":
        return f"{lvl} {DUKA_H}", None
    return f"{lvl} {cap(KH[KHP[low(text)]])}", None


def build_rest():
    pali = SRC.read_text(encoding="utf-8")
    h = {}
    seen = False
    section = "abhi"
    for sid, lines in segs(pali):
        if sid == "2-33":
            seen = True
            continue
        if not seen:
            continue
        vi = []
        for ln in lines:
            ln = ID.sub("", ln)
            if ln.startswith("#"):
                t, sec = heading(ln)
                section = sec or section
                vi.append(t)
            elif ln.startswith("Pañcakkhandhā – "):
                vi.append(S.FIVE_LIST)
            elif section == "abhi":
                vi.append(abhi_line(ln))
            elif ln in FIXED:
                vi.append(FIXED[ln])
            elif ln.endswith("?"):
                vi.append(panha_question(ln))
            else:
                vi.append(panha_line(ln))
        h[sid] = vi
    return h, pali


def render_rest(pali, h):
    blocks = []
    seen = False
    for sid, plines in segs(pali):
        if sid == "2-33":
            seen = True
            continue
        if not seen:
            continue
        vi = h[sid]
        assert len(vi) == len(plines), (sid, len(vi), len(plines))
        lines = list(vi)
        lines[-1] = f"{lines[-1]} ^{sid}"
        blocks.append("\n".join(lines))
    return unicodedata.normalize("NFC", "\n\n".join(blocks) + "\n")


# =========================================================================== pi-1 comparison and notes
def check_pi1():
    """matrix names: my phrase vs the approved pi-1 Vietnamese matrix line (1-matika.md, after review fixes);
    returns [(pāli, pi-1, mine)] for every difference"""
    pa = [ln for ln in PI1_PA.read_text(encoding="utf-8").splitlines() if ln.strip()]
    vi = [ln for ln in PI1_VI.read_text(encoding="utf-8").splitlines() if ln.strip()]
    assert len(pa) == len(vi)
    diffs, seen = [], 0
    for p, v in zip(pa, vi):
        mp = re.match(r"^\((Ka|Kha|Ga)\) (.*)$", p)
        mv = re.match(r"^\((a|b|c)\) Các hiện tượng (.*)$", v)
        if not mp or not mv:
            continue
        name = ID.sub("", mp.group(2))
        name = re.sub(r"\s*\[[^\]]*\]", "", name).rstrip(".")
        name = name.replace(" dhammā", "").replace("upādiṇṇ", "upādinn")
        theirs = ID.sub("", mv.group(2))
        theirs = re.sub(r"\s*\[[^\]]*\]", "", theirs).rstrip(".")
        key = PL_KEY.get(name)
        if key is None:
            continue
        seen += 1
        mine = ITEMS[key]
        if mine != theirs:
            diffs.append((name, theirs, mine))
    return diffs, seen


def notes_md(diffs, seen):
    L = ["# pi-2 Vietnamese rails: new formulas of chapter 1 after the sample (^2-34 … ^2-153)", "",
         "Generated by build_rails_1_vi.py; import it (K1) instead of retyping. Strings already in "
         "vi-rails-formulas.md (sample) are not repeated. Format: Pāli = tiếng Việt.", "",
         "## Abhidhammabhājanīya", "",
         f"Tattha katamo vedanākkhandho? = {agg_q('vedana')}",
         f"Ekavidhena vedanākkhandho – phassasampayutto. = {abhi_line('Ekavidhena vedanākkhandho – phassasampayutto.')}",
         f"Ekavidhena saṅkhārakkhandho – cittasampayutto. = "
         f"{abhi_line('Ekavidhena saṅkhārakkhandho – cittasampayutto.')}",
         f"N-vidhena X-kkhandho – atthi A, atthi B. = {cap(KH['vedana'])} theo nhóm N – {SOME} A, {SOME} B.",
         f"Atthi A, atthi B. (continuing) = {cap(SOME)} A, {SOME} B.",
         f"Evaṃ N-vidhena X-kkhandho. / evaṃ … (after …pe…) = Như vậy là {KH['vedana']} theo nhóm N. / như vậy là …",
         "…pe…. Evaṃ … = … Như vậy là … (never «….»)",
         f"Catuvīsatividhena / Tiṃsa(ti)vidhena / Bahuvidhena = {NUMX[24]} / {NUMX[30]} / {NUMX['many']}",
         f"Aparopi N-vidhena X-kkhandho – = {APARO} {KH['vedana']} theo nhóm N –   (no termbase entry)",
         "NP atthi X, atthi Y (a list member) = NP: có loại X, có loại Y; (the comma after the tail becomes «;» "
         "before the next noun phrase; sample ^2-33)",
         f"cakkhu…manosamphassajā vedanā / saññā / cetanā = cảm giác / tri giác / chủ ý sinh từ sự tiếp xúc của "
         f"mắt / tai / mũi / lưỡi / thân / ý",
         "manodhātu- / manoviññāṇadhātusamphassajā vedanā = cảm giác sinh từ sự tiếp xúc của yếu tố ý / yếu tố ý thức",
         "manodhātu, manoviññāṇadhātu (in a list) = yếu tố ý, yếu tố ý thức",
         "cakkhuviññāṇaṃ … manoviññāṇaṃ = thức qua mắt, thức qua tai, thức qua mũi, thức qua lưỡi, thức qua thân, ý thức",
         f"cakkhusamphassapaccayā vedanākkhandho = {paccaya_np('cakkhu', 'vedanākkhandho')}",
         f"sotasamphassapaccayā (alone, in a …pe… run) = {paccaya_np('sota')}",
         "atthi sukhindriyaṃ … upekkhindriyaṃ = có loại là năng lực dễ chịu / khó chịu / niềm vui / nỗi buồn / bình thản",
         "atthi sukhindriyasampayutto … = có loại gắn liền với năng lực dễ chịu …",
         f"kāyasamphassajā vedanā atthi sukhā, atthi dukkhā = cảm giác sinh từ sự tiếp xúc của thân: {SOME} "
         f"{ITEMS['sukhā#np']}, {SOME} {ITEMS['dukkhā#np']}",
         f"kāyasamphassajā saññā / cetanā atthi sukhasahagatā, atthi dukkhasahagatā; kāyaviññāṇaṃ atthi "
         f"sukhasahagataṃ, atthi dukkhasahagataṃ = …: {SOME} {ITEMS['sukhasahagata#np']}, {SOME} "
         f"{ITEMS['dukkhasahagata#np']}",
         f"Ayaṃ vuccati vedanākkhandho. = {cap(S.CALLED_SG)} {KH['vedana']}.",
         f"Dukamūlakaṃ. = {DUKAMULA}", f"Tikamūlakaṃ. = {TIKAMULA}", f"Ubhatovaḍḍhakaṃ. = {UBHATO}",
         f"(Yathā kusalattike vitthāro, evaṃ sabbepi tikā vitthāretabbā.) = {YATHA_KUSALATTIKE}",
         f"Abhidhammabhājanīyaṃ. = {FIXED['Abhidhammabhājanīyaṃ.']}",
         "", "## Pañhāpucchaka", "",
         f"#### Pañhāpucchakaṃ = #### {S.SEC_HEADINGS['Pañhāpucchakaṃ']}; ##### Tikaṃ / Dukaṃ = ##### {TIKA_H} / {DUKA_H}",
         f"Pañcannaṃ khandhānaṃ kati X, kati Y …? = {GROUP['Pañcannaṃ khandhānaṃ']}, {KATI} X, {KATI} Y …?",
         "Rūpakkhandho / Vedanā- / Saññā- / Saṅkhāra- / Viññāṇakkhandho = Khối vật chất / cảm giác / tri giác / "
         "tạo tác / thức",
         "Cattāro / Tayo / Dve khandhā = Bốn / Ba / Hai khối",
         "Subject X. = Subject X(predicate form): «là thiện», «là bất thiện», «không xác định về mặt đạo đức», "
         "«là vật chất», «là phi vật chất», «là phái sinh»; otherwise the matrix phrase",
         f"siyā X, siyā Y = {SIYA} X, {SIYA} Y",
         f'X na vattabbo – "A"tipi, "B"tipi = {NV_TOPIC.format(s="X")} rằng “A”, hay rằng “B” (pi-1 ^1-1452)',
         f'X na vattabbo – "A"ti = {NV_TOPIC.format(s="X")} rằng “A”',
         f'siyā na vattabbo / vattabbā – "A"tipi … = {SIYA} {NV} rằng “A”, hay rằng …',
         f'X na vattabbo – "A"ti, siyā B … = {NV_TOPIC.format(s="X")} rằng “A”; {PRON["s"]} / {PRON["p"]} '
         f'{SIYA} B …',
         f'Rūpakkhandho na vattabbo – "A"ti, B. = {NV_TOPIC.format(s="khối vật chất")} rằng “A”; {PRON["s"]} B.',
         f'Rūpakkhandho na vattabbo – "A"ti, "B". (B quoted without «ti», as written) = '
         f'{NV_TOPIC.format(s="khối vật chất")} rằng “A”; {PRON["s"]} “B”.',
         f"kenaci viññeyyā, kenaci na viññeyyā (after siyā …;) = {PRON['p']} {KENACI} (pi-1 ^1-1464)",
         f"Sappaccayā, saṅkhatā. = {SAPPACCAYA}",
         f"Pañhāpucchakaṃ. = {FIXED['Pañhāpucchakaṃ.']}",
         f"Khandhavibhaṅgo niṭṭhito. = {FIXED['Khandhavibhaṅgo niṭṭhito.']}",
         "", "## Matrix items (key = Pāli masculine singular = attributive phrase; predicate form if different)", ""]
    for k, v in ITEMS.items():
        L.append(f"{k} = {v}" + (f" (predicate: {PRED[k]})" if k in PRED else ""))
    L += ["", f"## Differences from the pi-1 matrix names (pi-1 → pi-2; {seen} names compared)", ""]
    if not diffs:
        L.append("none")
    for pk, theirs, mine in diffs:
        L.append(f"{pk}: pi-1 «{theirs}» → pi-2 «{mine}»")
    return unicodedata.normalize("NFC", "\n".join(L) + "\n")


def main():
    h, pali = build_rest()
    rest = render_rest(pali, h)
    sample = SAMPLE_VI.read_bytes()
    assert sample.endswith(b"^2-33\n")
    data = sample + b"\n" + rest.encode("utf-8")
    TARGET.write_bytes(data)
    diffs, seen = check_pi1()
    NOTES_PATH.write_bytes(notes_md(diffs, seen).encode("utf-8"))
    print(f"wrote {TARGET.name}: {len(h)} segments after the sample; notes-1.md")
    print(f"pi-1 names compared: {seen}, differences: {len(diffs)}")
    for d in diffs:
        print("pi-1 diff:", d)
    for s in SLIPS:
        print("slip:", s)
    for s in MISFITS:
        print("misfit:", s)


if __name__ == "__main__":
    main()
