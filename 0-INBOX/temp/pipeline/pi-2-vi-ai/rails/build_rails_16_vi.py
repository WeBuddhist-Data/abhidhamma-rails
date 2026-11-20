"""Builder for the Vietnamese rails translation of pi-2 (Vibhaṅga, «Phân tích các hiện tượng», plain audience),
chapter 16 (Ñāṇavibhaṅgo ^2-16-0 … ^2-831).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/16-nanavibhango.md
  0-INBOX/temp/pipeline/pi-2-vi-ai/rails/notes-16.md   (new recurring formulas, Pāli = tiếng Việt)

Translated fresh from the Pāli with the locked pi-2 termbase (paññā «trí tuệ»; ñāṇaṃ «hiểu biết», as a noun «sự hiểu
biết»; ñāṇavatthu «chỗ dựa của sự hiểu biết»; tathāgatabala «sức mạnh Như Lai»; āsaya / anusaya / carita / adhimutti
«thiên hướng / khuynh hướng tiềm ẩn / tính hạnh / chí hướng»; the matrix headings «Ma trận bộ N» vs the exposition
headings and closing labels «(Giải thích) phân loại theo nhóm N»). The matrix items are the approved pi-1 / pi-2 ch. 1
items (K1.ITEMS) said of «trí tuệ»; the onefold list repeats the pi-1 ^1-584 strings; shared strings are imported
read-only from the sample builder (S) and the chapter builders (K1, K23, K45, K6, K79, K10, K13). Strings reused from
the approved pi-1 Vietnamese rails are marked pi1() and checked by check_pi1(); strings from earlier pi-2 chapters are
marked pi2() and checked by check_pi2(). Importing this module writes nothing.

usage: python -I -X utf8 build_rails_16_vi.py [--dry]
"""
import pathlib
import re
import sys
import unicodedata

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)
import build_rails_1_vi as K1      # noqa: E402
import build_rails_2_3_vi as K23   # noqa: E402
import build_rails_4_5_vi as K45   # noqa: E402
import build_rails_6_vi as K6      # noqa: E402
import build_rails_7_9_vi as K79   # noqa: E402
import build_rails_10_12_vi as K10  # noqa: E402
import build_rails_13_15_vi as K13  # noqa: E402

PART = "16-nanavibhango.md"
PI1_VI = S.ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
NOTES_PATH = RAILS / "notes-16.md"
cap, low, q = S.cap, K1.low, K23.q
CALLED = S.CALLED_SG                                   # «đó được gọi là»
SLIPS, MISFITS, PI1_USED, PI2_USED = [], [], [], []
NOTES = []                                             # (Pāli, tiếng Việt) new formulas for notes-16.md


def note(lst, s):
    if s not in lst:
        lst.append(s)


def slip(s):
    note(SLIPS, s)


def misfit(s):
    note(MISFITS, s)


def pi1(s):
    note(PI1_USED, s)
    return s


def pi2(s):
    note(PI2_USED, s)
    return s


def nf(p, v):
    """record a new formula for the notes file; returns v"""
    if (p, v) not in NOTES:
        NOTES.append((p, v))
    return v


# =========================================================================== core vocabulary
PANNA = pi1(K45.PANNA_SHORT)       # paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi (pi-1 ^1-1359)
YA_TATTHA = pi1("điều mà, ở đây, là")   # yā tattha paññā … (pi-1 ^1-1343, ^1-1344)
SUCH = pi1("điều mà thuộc loại như vậy là")   # yā evarūpā … (pi-1 ^1-1221)
ARISES = nf("yā uppajjati paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi",
            "điều mà sinh khởi là " + PANNA)
NANA = nf("ñāṇavatthu", "chỗ dựa của sự hiểu biết")    # termbase ñāṇavatthu
KN = "sự hiểu biết"                                     # ñāṇaṃ as a noun (termbase phrases «sự hiểu biết về …»)
PN = "trí tuệ"                                          # paññā
LABEL = {"Ka": "a", "Kha": "b", "Ga": "c", "Gha": "d", "Kha-gha": "b-d"}


def vidha(n):
    return nf("<N>vidhena ñāṇavatthu –", f"{cap(NANA)} {S.by_n(n)} –")


def vidha_end(n):
    return nf("Evaṃ <N>vidhena ñāṇavatthu.", f"Như vậy là {NANA} {S.by_n(n)}.")


def P(attr):
    """«trí tuệ» + a matrix attribute (termbase: «trí tuệ mà là …» before «là» / «không phải là»)"""
    return f"{PN} {'mà ' if attr.startswith(('là ', 'không phải là ')) else ''}{attr}"


FEM_SPECIAL = {"maggādhipatinī": "maggādhipati"}
FEM_SLIP = {"ajjhatā": ("ajjhatto", "^2-753 (62) «atthi ajjhatā» for ajjhattā: spelling slip, rendered as meant"),
            "anuppādinnupādāniyā": ("anupādinnupādāniyo", "^2-753 (40) «anuppādinnupādāniyā, anuppādinnaanupādāniyā» "
                                    "(double pp) for anupādinn-: spelling slip, rendered as meant"),
            "anuppādinnaanupādāniyā": ("anupādinnaanupādāniyo", None)}


def fem_key(f):
    """feminine / plural Pāli matrix item -> the K1.ITEMS key (masculine singular)"""
    f = f.strip()
    w = f.split(" ")
    if len(w) == 2 and w[0].lower().endswith("vippayuttā"):
        w = [w[0][:-1] + "a" + w[1]]
    last = w[-1].lower()
    if last in FEM_SLIP:
        k, s = FEM_SLIP[last]
        if s:
            slip(s)
        w[-1] = k
    elif last in FEM_SPECIAL:
        w[-1] = FEM_SPECIAL[last]
    elif last.endswith("inī"):
        w[-1] = last[:-3] + "ī"
    elif last.endswith("ino"):
        w[-1] = last[:-3] + "ī"
    elif last.endswith("ā"):
        w[-1] = last[:-1] + "o"
    else:
        w[-1] = last
    w[0] = w[0].lower()
    return " ".join(w)


def attr(f):
    return K1.item(fem_key(f))


def item(f):
    """«X paññā» (or a bare feminine item) -> «trí tuệ …»"""
    f = re.sub(r" paññā$", "", f.strip())
    return P(attr(f))


def label(ln):
    """«(1. Ka) rest» / «(Kha) rest» / «(12-21) Rest» -> («(1. a)», rest)"""
    m = re.match(r"^\((\d+(?:-\d+)?)?(?:\. )?([A-Za-z-]+)?\) (.*)$", ln)
    if not m:
        return "", ln
    n, k, rest = m.groups()
    if k:
        lab = f"({n}. {LABEL[k]})" if n else f"({LABEL[k]})"
    else:
        lab = f"({n})"
    return lab, rest


def with_label(lab, vi):
    return f"{lab} {cap(vi)}" if lab else cap(vi)


# =========================================================================== the onefold matrix (five consciousnesses)
E = S.EKAKA                                            # pi-1 ^1-584 onefold strings (sabbaṃ rūpaṃ na hetu, …)
FIVE = "năm loại thức"                                 # pañca viññāṇā (termbase viññāṇā «loại thức»)
EKA = [  # (Pāli plural, -meva form, Vietnamese predicate)
    ("na hetū", "na hetumeva", E[0]), ("ahetukā", "ahetukameva", E[1]),
    ("hetuvippayuttā", "hetuvippayuttameva", E[2]), ("sappaccayā", "sappaccayameva", E[3]),
    ("saṅkhatā", "saṅkhatameva", E[4]), ("arūpā", "arūpameva", K1.PRED["arūpo"]),
    ("lokiyā", "lokiyameva", E[6]), ("sāsavā", "sāsavameva", E[7]), ("saṃyojaniyā", "saṃyojaniyameva", E[8]),
    ("ganthaniyā", "ganthaniyameva", E[9]), ("oghaniyā", "oghaniyameva", E[10]),
    ("yoganiyā", "yoganiyameva", E[11]), ("nīvaraṇiyā", "nīvaraṇiyameva", E[12]),
    ("parāmaṭṭhā", "parāmaṭṭhameva", E[13]), ("upādāniyā", "upādāniyameva", E[14]),
    ("saṃkilesikā", "saṃkilesikameva", E[15]), ("abyākatā", "abyākatameva", E[16]),
    ("sārammaṇā", "sārammaṇameva", K1.ITEMS["sārammaṇo"]), ("acetasikā", "acetasikameva", E[18]),
    ("vipākā", "vipākameva", K1.ITEMS["vipāko"]),
    ("upādinnupādāniyā", "upādinnupādāniyameva", K1.ITEMS["upādinnupādāniyo"]),
    ("asaṃkiliṭṭhasaṃkilesikā", "asaṃkiliṭṭhasaṃkilesikameva", E[21]),
    ("na savitakkasavicārā", "na savitakkasavicārameva", E[22]),
    ("na avitakkavicāramattā", "na avitakkavicāramattameva", E[23]),
    ("avitakkaavicārā", "avitakkaavicārameva", E[24]), ("na pītisahagatā", "na pītisahagatameva", E[25]),
    ("neva dassanena na bhāvanāya pahātabbā", "neva dassanena na bhāvanāya pahātabbameva", E[28]),
    ("neva dassanena na bhāvanāya pahātabbahetukā", "neva dassanena na bhāvanāya pahātabbahetukameva", E[29]),
    ("nevācayagāmināpacayagāmino", "nevācayagāmināpacayagāmimeva", E[30]),
    ("nevasekkhanāsekkhā", "nevasekkhanāsekkhameva", E[31]), ("parittā", "parittameva", E[32]),
    ("kāmāvacarā", "kāmāvacarameva", E[33]), ("na rūpāvacarā", "na rūpāvacarameva", E[34]),
    ("na arūpāvacarā", "na arūpāvacarameva", E[35]), ("pariyāpannā", "pariyāpannameva", E[36]),
    ("no apariyāpannā", "no apariyāpannameva", E[37]), ("aniyatā", "aniyatameva", E[38]),
    ("aniyyānikā", "aniyyānikameva", E[39]),
]
for _p, _m, _v in EKA:
    if _v in E:
        pi1(_v)
CERTAIN = "chắc chắn"                                  # -meva (termbase: hetumeva «chắc chắn … gốc rễ» …)
MEVA_OVERRIDE = {"arūpameva": "chắc chắn phi vật chất", "parittameva": "chắc chắn là hạn hẹp",
                 "abyākatameva": "chắc chắn là không xác định về mặt đạo đức"}   # termbase wording
MEVA_TAIL = [("uppannaṃ manoviññāṇaviññeyyameva", "khi đã sinh khởi thì chắc chắn có thể được ý thức nhận biết"),
             ("aniccameva", "chắc chắn là vô thường"), ("jarābhibhūtameva", "chắc chắn bị sự lão hóa chế ngự")]
# uppannaṃ … viññeyyaṃ (pi-1 «khi đã sinh khởi thì có thể được sáu loại thức nhận biết»); manoviññāṇa «ý thức»
EKA_P = ", ".join(p for p, _, _ in EKA)
EKA_VI = "; ".join(v for _, _, v in EKA)
MEVA_P = ", ".join([m for _, m, _ in EKA] + [m for m, _ in MEVA_TAIL])
MEVA_VI = "; ".join([MEVA_OVERRIDE.get(m, f"{CERTAIN} {v}") for _, m, v in EKA] + [v for _, v in MEVA_TAIL])

BY5 = "bằng năm loại thức, một người"                  # Pañcahi viññāṇehi … (3rd sg., no subject)
AFTER5 = "ngay cả liền sau năm loại thức, một người cũng"   # Pañcannaṃ viññāṇānaṃ samanantarāpi …
MANO5 = "liền sau năm loại thức, ngay cả bằng yếu tố ý, một người cũng"   # … samanantarā manodhātuyāpi …
ACTS = {  # Pāli predicate -> Vietnamese
    "na kañci dhammaṃ paṭivijānāti": "không nhận biết rõ bất cứ hiện tượng nào",
    "na kañci iriyāpathaṃ kappeti": "không thực hiện bất cứ tư thế nào",
    "na kāyakammaṃ na vacīkammaṃ paṭṭhapeti": "không khởi lập nghiệp bằng thân, không khởi lập nghiệp bằng lời nói",
    "na kusalākusalaṃ dhammaṃ samādiyati": "không thọ trì hiện tượng thiện hay bất thiện",
    "na samāpajjati na vuṭṭhāti": "không chứng nhập thành tựu thiền, không xuất khỏi thành tựu thiền",
    "na cavati na uppajjati": "không chết, không tái sinh",
    "na supati na paṭibujjhati na supinaṃ passati": "không ngủ, không thức dậy, không nằm mơ",
}
misfit("samādiyati (^2-751, ^2-766): no entry; «thọ trì» (ch. 12 samādāya «thọ trì»)")
POSTURES = "đi, đứng, ngồi hay nằm"                    # gamanaṃ vā ṭhānaṃ vā nisajjaṃ vā seyyaṃ vā (termbase)
YATHAVA = "trí tuệ làm sáng tỏ chỗ dựa đúng như thật"   # yāthāvakavatthuvibhāvanā paññā (yāthāvaka, vatthu, vibhāvanā)
MAT1 = {  # the onefold matrix lines (without the number)
    "Uppannavatthukā uppannārammaṇā,": "Có chỗ dựa đã sinh khởi và có đối tượng đã sinh khởi.",
    "Purejātavatthukā purejātārammaṇā": "Có chỗ dựa đã sinh ra trước và có đối tượng đã sinh ra trước.",
    "Ajjhattikavatthukā bāhirārammaṇā": "Có chỗ dựa thuộc phần bên trong và có đối tượng thuộc phần bên ngoài.",
    "Asambhinnavatthukā asambhinnārammaṇā": "Có chỗ dựa chưa tan rã và có đối tượng chưa tan rã.",
    "Nānāvatthukā nānārammaṇā": "Có chỗ dựa khác nhau và có đối tượng khác nhau.",
    "Na aññamaññassa gocaravisayaṃ paccanubhonti": "Không trải nghiệm phạm vi hoạt động của nhau.",
    "Na asamannāhārā uppajjanti": "Không sinh khởi khi không có sự lưu ý.",
    "Na amanasikārā uppajjanti": "Không sinh khởi khi không chú tâm.",
    "Na abbokiṇṇā uppajjanti": "Không sinh khởi liền mạch.",
    "Na apubbaṃ acarimaṃ uppajjanti": "Không sinh khởi không trước không sau.",
    "Na aññamaññassa samanantarā uppajjanti": "Không sinh khởi liền sau nhau.",
    "Pañca viññāṇā anābhogā": f"{cap(FIVE)} không có sự chú hướng.",
    "Pañcahi viññāṇehi na kañci [kiñci (sī. ka.)] dhammaṃ paṭivijānāti aññatra abhinipātamattā":
        f"{cap(BY5)} không nhận biết rõ bất cứ hiện tượng nào {S.spell('Sī., Ka.', 'kiñci')}, ngoại trừ khi chỉ có "
        "sự va chạm.",
}
misfit("abbokiṇṇā / apubbaṃ acarimaṃ (^2-751, ^2-764): termbase «liền mạch», «không trước», «không sau»; the "
       "niddesa glosses them «na paṭipāṭiyā» / «na ekakkhaṇe»: kept literal «không sinh khởi liền mạch», «không sinh "
       "khởi không trước không sau»")
for _a, _v in ACTS.items():
    MAT1[f"Pañcahi viññāṇehi {_a}"] = f"{cap(BY5)} {_v}."
    MAT1[f"Pañcannaṃ viññāṇānaṃ samanantarāpi {_a}"] = f"{cap(AFTER5)} {_v}."
MAT1["Pañcannaṃ viññāṇānaṃ samanantarāpi na supati na paṭibujjhati na supinaṃ passati, yāthāvakavatthuvibhāvanā "
     "paññā"] = f"{cap(AFTER5)} {ACTS['na supati na paṭibujjhati na supinaṃ passati']}; {YATHAVA}."


def seg_751(lines):
    out = []
    first = lines[0]
    assert first == f"Ekavidhena ñāṇavatthu – pañca viññāṇā {EKA_P},", first
    out.append(f"{vidha(1)} {FIVE} {EKA_VI}.")
    for ln in lines[1:-1]:
        lab, rest = label(ln)
        out.append(f"{lab} {MAT1[rest]}" if lab else MAT1[rest])
    assert lines[-1] == "Evaṃ ekavidhena ñāṇavatthu."
    out.append(vidha_end(1))
    nf("pañca viññāṇā na hetū, ahetukā, … aniyyānikā", f"{FIVE} {EKA_VI}")
    return out


def topic(x):
    return K79.TOPIC_C.format(x=x)                     # «Về câu “x”:» (ch. 6-15)


def mat_topic(key):
    """the matrix sentence as a quoted topic (lower case, no full stop)"""
    return topic(low(MAT1[key][:-1]))


def seg_761(lines):
    (ln,) = lines
    assert ln == f"Pañca viññāṇā {MEVA_P}.", ln
    return [f"{cap(FIVE)} {MEVA_VI}."]


VK = {"cakkhu": "thức qua mắt", "sota": "thức qua tai", "ghāna": "thức qua mũi", "jivhā": "thức qua lưỡi",
      "kāya": "thức qua thân"}                         # termbase cakkhuviññāṇaṃ …


def seg_762(lines):
    out = []
    pairs = [("uppannavatthukā, uppannārammaṇā", "có chỗ dựa đã sinh khởi, có đối tượng đã sinh khởi",
              "chúng sinh khởi trên chỗ dựa đã sinh khởi, trên đối tượng đã sinh khởi"),
             ("Purejātavatthukā, purejātārammaṇā", "có chỗ dựa đã sinh ra trước, có đối tượng đã sinh ra trước",
              "chúng sinh khởi trên chỗ dựa đã sinh ra trước, trên đối tượng đã sinh ra trước"),
             ("Ajjhattikavatthukā, bāhirārammaṇā", "có chỗ dựa thuộc phần bên trong, có đối tượng thuộc phần bên "
              "ngoài", "chỗ dựa của năm loại thức thì thuộc phần bên trong, các đối tượng thì thuộc phần bên ngoài"),
             ("Asambhinnavatthukā, asambhinnārammaṇā", "có chỗ dựa chưa tan rã, có đối tượng chưa tan rã",
              "chúng sinh khởi trên chỗ dựa chưa tan rã, trên đối tượng chưa tan rã"),
             ("Nānāvatthukā, nānārammaṇā", "có chỗ dựa khác nhau, có đối tượng khác nhau",
              ", ".join(f"chỗ dựa và đối tượng của {VK[k]} là khác" for k in VK))]
    for ln, (p, t, e) in zip(lines, pairs):
        assert p in ln, (p, ln)
        if p.startswith("uppanna"):
            t = f"{FIVE} {t}"
        out.append(f"{topic(t)} {e}.")
    return out


def cross(sid, ln, kind):
    """^2-763 (gocaravisaya) / ^2-765 (uppannasamanantarā): the five consciousnesses taken pairwise"""
    order = list(VK)

    def pair(a, b):
        if kind == "g":
            return (f"phạm vi hoạt động của {VK[a]} thì {VK[b]} không trải nghiệm, và phạm vi hoạt động của {VK[b]} "
                    f"thì {VK[a]} cũng không trải nghiệm")
        return (f"ngay liền sau khi {VK[a]} sinh khởi, {VK[b]} không sinh khởi, và ngay liền sau khi {VK[b]} sinh "
                f"khởi, {VK[a]} cũng không sinh khởi")
    sents = [pair("cakkhu", b) for b in order[1:]]
    if kind == "g":
        mid = ("Phạm vi hoạt động của thức qua tai… của thức qua mũi… của thức qua lưỡi… của thức qua thân thì thức "
               "qua mắt không trải nghiệm, và phạm vi hoạt động của thức qua mắt thì thức qua thân cũng không trải "
               "nghiệm")
    else:
        mid = ("Ngay liền sau khi thức qua tai… thức qua mũi… thức qua lưỡi… thức qua thân sinh khởi, thức qua mắt "
               "không sinh khởi, và ngay liền sau khi thức qua mắt sinh khởi, thức qua thân cũng không sinh khởi")
    sents += [mid] + [pair("kāya", b) for b in order[1:4]]
    key = ("Na aññamaññassa gocaravisayaṃ paccanubhonti" if kind == "g"
           else "Na aññamaññassa samanantarā uppajjanti")
    body = ". ".join(cap(s) for s in sents)
    return f"{mat_topic(key)} {low(body)}."


def seg_764(lines):
    exp = ["chúng sinh khởi nơi người đang lưu ý", "chúng sinh khởi nơi người đang chú tâm",
           "chúng không sinh khởi theo thứ tự lần lượt", "chúng không sinh khởi trong cùng một khoảnh khắc"]
    keys = ["Na asamannāhārā uppajjanti", "Na amanasikārā uppajjanti", "Na abbokiṇṇā uppajjanti",
            "Na apubbaṃ acarimaṃ uppajjanti"]
    out = []
    for ln, k, e in zip(lines, keys, exp):
        assert ln.startswith(k[:-1] + "īti "), ln
        out.append(f"{mat_topic(k)} {e}.")
    return out


def seg_766(lines):
    out = []
    for ln in lines:
        if ln.startswith("Pañca viññāṇā anābhogāti"):
            out.append(f"{mat_topic('Pañca viññāṇā anābhogā')} nơi năm loại thức không có sự hướng đến, sự chú "
                       "hướng, sự lưu ý hay sự chú tâm.")
            continue
        if ln == "Aññatra abhinipātamattāti aññatra āpātamattā.":
            out.append(f"{topic('ngoại trừ khi chỉ có sự va chạm')} ngoại trừ khi chỉ có sự hiện ra.")
            continue
        if ln == "Evaṃ ekavidhena ñāṇavatthu.":
            out.append(vidha_end(1))
            continue
        if ln == "Ekakaṃ.":
            out.append(CLOSE[1])
            continue
        tail = ""
        if ln.endswith(" Evaṃ yāthāvakavatthuvibhāvanā paññā."):
            ln = ln[:-len(" Evaṃ yāthāvakavatthuvibhāvanā paññā.")]
            tail = f" Như vậy là {YATHAVA}."
        m = re.match(r"^(Pañcahi viññāṇehi|Pañcannaṃ viññāṇānaṃ samanantarāpi) (.+?)īti (.+)\.$", ln)
        assert m, ln
        head, a, expl = m.groups()
        pa = a + "i"
        assert pa in ACTS, pa
        mano = "samanantarā manodhātuyāpi" in expl
        assert mano == head.startswith("Pañcannaṃ"), ln
        dash = ""
        if expl.endswith(" – gamanaṃ vā ṭhānaṃ vā nisajjaṃ vā seyyaṃ vā"):
            dash = f" – {POSTURES}"
        key = f"{head} {pa}"
        who = BY5 if head.startswith("Pañcahi") else MANO5
        out.append(f"{mat_topic(key)} {who} {ACTS[pa]}{dash}.{tail}")
    return out


# =========================================================================== wisdom items, names, locations
LOCAL = {  # items said of «trí tuệ» that the pi-1 matrix does not have (masculine keys), termbase phrases
    "atthajāpiko": "tạo ra lợi ích", "jāpitattho": "có lợi ích đã được tạo ra",
    "cintāmayo": "được tạo nên từ sự suy tư", "sutamayo": "được tạo nên từ sự lắng nghe",
    "bhāvanāmayo": "được tạo nên từ sự tu tập", "dānamayo": "được tạo nên từ sự bố thí",
    "sīlamayo": "được tạo nên từ giới hạnh",
    "hānabhāgī": "thuộc về phía suy giảm", "ṭhitibhāgī": "thuộc về phía duy trì",
    "visesabhāgī": "thuộc về phía thăng tiến", "nibbedhabhāgī": "thuộc về phía xuyên thấu",
}
misfit("bhāvanāmayā paññā (^2-753, ^2-768, ^2-769): no phrase entry; «trí tuệ được tạo nên từ sự tu tập» after "
       "the sibling phrases cintāmayā / sutamayā / dānamayā paññā and bhāvanāya «sự tu tập»")
_item_k1 = K1.item


def attr(f):  # noqa: F811  (extends the matrix lookup with LOCAL)
    k = fem_key(f)
    return LOCAL[k] if k in LOCAL else _item_k1(k)


SOME = S.SOME                                          # «có loại» (atthi …)
CLOSE = {n: f"Phân loại theo nhóm {S.NUM[n]}." for n in range(1, 11)}   # Ekakaṃ. … Dasakaṃ. (termbase)
CLOSE_P = {1: "Ekakaṃ.", 2: "Dukaṃ.", 3: "Tikaṃ.", 4: "Catukkaṃ.", 5: "Pañcakaṃ.", 6: "Chakkaṃ.", 7: "Sattakaṃ.",
           8: "Aṭṭhakaṃ.", 9: "Navakaṃ.", 10: "Dasakaṃ."}
assert CLOSE[1] == pi1("Phân loại theo nhóm một.")    # pi-1 ^1-584
BO = {1: "một", 2: "đôi", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười"}
PREF = {1: "Ekaka", 2: "Duka", 3: "Tika", 4: "Catukka", 5: "Pañcaka", 6: "Chakka", 7: "Sattaka", 8: "Aṭṭhaka",
        9: "Navaka", 10: "Dasaka"}
HEAD = {"Ñāṇavibhaṅgo": S.CH_HEADINGS["Ñāṇavibhaṅgo"], "Mātikā": "Ma trận"}
for _n in PREF:
    HEAD[f"{PREF[_n]}mātikā"] = f"Ma trận bộ {BO[_n]}"            # pi-1 «Ma trận bộ ba / bộ đôi»; termbase bộ sáu …
    HEAD[f"{PREF[_n]}niddeso"] = f"Giải thích phân loại theo nhóm {S.NUM[_n]}"   # pi-1 ^1-2-3-1-0 … ^1-2-3-3-0
pi1("Ma trận bộ ba")
pi1("Ma trận bộ đôi")
pi1("Giải thích phân loại theo nhóm một")

KAMMASSAKA = "sự hiểu biết rằng nghiệp là tài sản của chính mình"   # kammassakatañāṇaṃ (termbase kammassakataṃ)
SACCANU = "sự hiểu biết thuận theo sự thật"                         # saccānulomikaṃ ñāṇaṃ
MAGGASAM = "sự hiểu biết của người có được con đường"               # maggasamaṅgissa ñāṇaṃ (samaṅgissa «người có được»)
PHALASAM = "sự hiểu biết của người có được thành quả"
DHAMMASAM = "sự hiểu biết của người có được Giáo Pháp"              # Dhammasamaṅgissa ñāṇaṃ (^2-803)
DHAMME = "sự hiểu biết về Giáo Pháp"                                # dhamme ñāṇaṃ (path-knowledge set; user note)
ANVAYE = "sự hiểu biết bằng suy diễn"                               # anvaye ñāṇaṃ (termbase)
PARIYE = "sự hiểu biết bao quát tâm"                                # pariye ñāṇaṃ (termbase)
SAMMUTI = "sự hiểu biết theo quy ước"                               # sammutiñāṇaṃ (sammuti «quy ước»)
KNOW = dict(K13.KNOW)                                               # ch. 15 locatives before ñāṇaṃ («về X»)


def kn(x):
    """«X ñāṇaṃ» -> «sự hiểu biết về X» (termbase phrases Jarāmaraṇe ñāṇaṃ, viññāṇe ñāṇaṃ …)"""
    return f"{KN} về {KNOW[low(x)]}"


def kn_also(x):
    """«Xpetaṃ ñāṇaṃ» -> «cũng là sự hiểu biết về X» (termbase viññāṇepetaṃ ñāṇaṃ)"""
    return f"cũng là {kn(x)}"


CYCLE = {  # paññā X no Y … (termbase ācayāya / apacayāya / nibbidāya / paṭivedhāya «dẫn đến …»)
    "ācayāya no apacayāya": "dẫn đến sự tích lũy chứ không dẫn đến sự giảm trừ",
    "apacayāya no ācayāya": "dẫn đến sự giảm trừ chứ không dẫn đến sự tích lũy",
    "ācayāya ceva apacayāya ca": "vừa dẫn đến sự tích lũy vừa dẫn đến sự giảm trừ",
    "nevācayāya no apacayāya": "không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ",
    "neva ācayāya no apacayāya": "không dẫn đến sự tích lũy cũng không dẫn đến sự giảm trừ",
    "nibbidāya no paṭivedhāya": "dẫn đến sự nhàm chán chứ không dẫn đến sự thấu triệt",
    "paṭivedhāya no nibbidāya": "dẫn đến sự thấu triệt chứ không dẫn đến sự nhàm chán",
    "nibbidāya ceva paṭivedhāya ca": "vừa dẫn đến sự nhàm chán vừa dẫn đến sự thấu triệt",
    "neva nibbidāya no paṭivedhāya": "không dẫn đến sự nhàm chán cũng không dẫn đến sự thấu triệt",
}
MODE = {k: pi1(v) for k, v in {   # dukkhapaṭipadā dandhābhiññā … (pi-1 ^1-? «với cách thực hành … »)
    "dukkhapaṭipadā dandhābhiññā": "với cách thực hành khó khăn và sự hiểu biết trực tiếp chậm chạp",
    "dukkhapaṭipadā khippābhiññā": "với cách thực hành khó khăn và sự hiểu biết trực tiếp nhanh chóng",
    "sukhapaṭipadā dandhābhiññā": "với cách thực hành dễ dàng và sự hiểu biết trực tiếp chậm chạp",
    "sukhapaṭipadā khippābhiññā": "với cách thực hành dễ dàng và sự hiểu biết trực tiếp nhanh chóng"}.items()}
OBJ4 = {"parittā parittārammaṇā": "hạn hẹp và có đối tượng hạn hẹp",
        "parittā appamāṇārammaṇā": "hạn hẹp và có đối tượng không thể đo lường",
        "appamāṇā parittārammaṇā": "không thể đo lường và có đối tượng hạn hẹp",
        "appamāṇā appamāṇārammaṇā": "không thể đo lường và có đối tượng không thể đo lường"}
pi1(OBJ4["parittā parittārammaṇā"])
FOUR_PS = pi2(K13.FOUR_PS)                             # «Bốn loại hiểu biết thông suốt»
FOUR_MODES = "Bốn cách thực hành"                      # catasso paṭipadā (termbase paṭipadā «cách thực hành»)
FOUR_OBJ = "Bốn đối tượng"                             # cattāri ārammaṇāni (termbase ārammaṇāni «đối tượng»)
PANCANGA = "định tâm đúng đắn gồm năm chi phần"        # pañcaṅgiko sammāsamādhi (termbase pañcaṅgiko)
PANCANANA = "định tâm đúng đắn gồm năm sự hiểu biết"   # pañcañāṇiko sammāsamādhi (termbase pañcañāṇiko)
SIX = "trí tuệ trong sáu loại hiểu biết trực tiếp"     # chasu abhiññāsu paññā (termbase abhiññāsu)
SS77 = "bảy mươi bảy chỗ dựa của sự hiểu biết"         # sattasattati ñāṇavatthūni
EIGHT = "trí tuệ trong bốn con đường và bốn thành quả"   # catūsu maggesu catūsu phalesu paññā (ch. 15 wording)
NINE = "trí tuệ trong chín thành tựu thiền an trú tuần tự"   # navasu anupubbavihārasamāpattīsu paññā
misfit("anupubbavihārasamāpatti (^2-759, ^2-808, ^2-828): no entry; anupubba «tuần tự» + vihāra «an trú» + "
       "samāpatti «thành tựu thiền» (user: samāpatti «thành tựu thiền», over the termbase forms samāpattiṃ / "
       "…samāpattiyā «sự chứng đạt»): «chín thành tựu thiền an trú tuần tự»")

NAMES = {  # Pāli name (lower case, as in the questions and the quoted closings) -> Vietnamese
    "cintāmayā paññā": P(LOCAL["cintāmayo"]), "sutamayā paññā": P(LOCAL["sutamayo"]),
    "bhāvanāmayā paññā": P(LOCAL["bhāvanāmayo"]), "dānamayā paññā": P(LOCAL["dānamayo"]),
    "sīlamayā paññā": P(LOCAL["sīlamayo"]),
    "adhisīle paññā": "trí tuệ trong giới hạnh cao thượng", "adhicitte paññā": "trí tuệ trong tâm cao thượng",
    "adhipaññāya paññā": "trí tuệ trong trí tuệ cao thượng",       # termbase Adhisīle / adhipaññāya paññā
    "āyakosallaṃ": "sự khéo léo về sự tiến bộ", "apāyakosallaṃ": "sự khéo léo về sự suy thoái",
    "upāyakosallaṃ": "sự khéo léo về phương cách",                  # kosallaṃ «sự khéo léo», upāya «phương cách»
    "kammassakatañāṇaṃ": KAMMASSAKA, "saccānulomikaṃ ñāṇaṃ": SACCANU,
    "dhamme ñāṇaṃ": DHAMME, "anvaye ñāṇaṃ": ANVAYE, "pariye ñāṇaṃ": PARIYE,
    "catasso paṭisambhidā": low(FOUR_PS), "catasso paṭipadā": low(FOUR_MODES),
    "cattāri ārammaṇāni": low(FOUR_OBJ), "pañcaṅgiko sammāsamādhi": PANCANGA,
    "pañcañāṇiko sammāsamādhi": PANCANANA, "chasu abhiññāsu paññā": SIX, "sattasattati ñāṇavatthūni": SS77,
    "catūsu maggesu catūsu phalesu paññā": EIGHT, "navasu anupubbavihārasamāpattīsu paññā": NINE,
    "hānabhāginī paññā": P(LOCAL["hānabhāgī"]),
}
misfit("āya / apāya in āyakosallaṃ / apāyakosallaṃ (^2-753, ^2-771): no entry; «sự khéo léo về sự tiến bộ / về sự "
       "suy thoái» (kosallaṃ «sự khéo léo»; upāyakosallaṃ «sự khéo léo về phương cách» from upāya «phương cách»)")
for _k in ("parittārammaṇā", "mahaggatārammaṇā", "appamāṇārammaṇā", "maggārammaṇā", "maggādhipatinī",
           "atītārammaṇā", "anāgatārammaṇā", "paccuppannārammaṇā", "ajjhattārammaṇā", "bahiddhārammaṇā",
           "ajjhattabahiddhārammaṇā"):
    NAMES[f"{_k} paññā"] = item(_k)
for _k, _v in CYCLE.items():
    NAMES[f"paññā {_k}"] = f"{PN} {_v}"
for _k, _v in MODE.items():
    NAMES[f"{_k} paññā"] = f"{PN} {_v}"
for _k, _v in OBJ4.items():
    NAMES[f"{_k} paññā"] = f"{PN} {_v}"
for _k in KNOW:
    NAMES.setdefault(f"{_k} ñāṇaṃ", kn(_k))

# locations of wisdom (termbase gapped phrases «trí tuệ trong tâm thiện … thuộc … cõi», «trí tuệ trong … con đường»)
TOK = re.compile(r"(tīsu|catūsu) bhūmīsu (kusalābyākate|kusale|vipāke|kiriyābyākate)|(tīsu|catūsu) (maggesu|phalesu)"
                 r"|(kāmāvacara|rūpāvacarārūpāvacara|rūpāvacara|arūpāvacara)(kusalābyākate|kusale)")
NUMV = {"tīsu": "ba", "catūsu": "bốn"}
MIND = {"kusalābyākate": "tâm thiện và không xác định về mặt đạo đức", "kusale": "tâm thiện",
        "vipāke": "quả của nghiệp", "kiriyābyākate": "tâm mang tính chức năng không xác định về mặt đạo đức"}
SPHERE = {"kāmāvacara": "cõi dục lạc", "rūpāvacara": "cõi hình sắc", "arūpāvacara": "cõi không hình sắc",
          "rūpāvacarārūpāvacara": "cõi hình sắc và cõi không hình sắc"}
SAMP = {  # X-sampayuttā / -vippayuttā paññā (termbase phrases)
    "vitakkasampayuttā": "gắn liền với sự hướng tâm", "vitakkavippayuttā": "không gắn liền với sự hướng tâm",
    "vicārasampayuttā": "gắn liền với sự duy trì tâm", "vicāravippayuttā": "không gắn liền với sự duy trì tâm",
    "pītisampayuttā": "gắn liền với sự hân hoan", "pītivippayuttā": "không gắn liền với sự hân hoan",
    "sukhasampayuttā": "gắn liền với hạnh phúc", "sukhavippayuttā": "không gắn liền với hạnh phúc",
    "upekkhāsampayuttā": "gắn liền với sự bình thản", "upekkhāvippayuttā": "không gắn liền với sự bình thản",
    "vitakkavicārasampayuttā": "gắn liền với sự hướng tâm và sự duy trì tâm",
    "vitakkavippayuttā vicārasampayuttā": "không gắn liền với sự hướng tâm gắn liền với sự duy trì tâm",
    "vitakkavicāravippayuttā": "không gắn liền với sự hướng tâm và sự duy trì tâm",
}


def loc(s):
    """a Pāli location (tīsu bhūmīsu kusalābyākate catūsu maggesu …) -> «trong …, trong …»"""
    s = s.strip()
    s = s[0].lower() + s[1:]
    toks = list(TOK.finditer(s))
    assert " ".join(t.group(0) for t in toks) == s, s
    parts, i = [], 0
    while i < len(toks):
        g = toks[i].groups()
        if g[0]:
            parts.append(f"trong {MIND[g[1]]} thuộc {NUMV[g[0]]} cõi")
        elif g[2]:
            if g[3] == "maggesu" and i + 1 < len(toks) and toks[i + 1].group(4) == "phalesu":
                parts.append(f"trong {NUMV[g[2]]} con đường và {NUMV[toks[i + 1].group(3)]} thành quả")
                i += 1
            else:
                parts.append(f"trong {NUMV[g[2]]} {'con đường' if g[3] == 'maggesu' else 'thành quả'}")
        else:
            parts.append(f"trong {MIND[g[5]]} thuộc {SPHERE[g[4]]}")
        i += 1
    return ", ".join(parts)


def subj(s):
    """the subject before «paññā»: a location or an X-sampayuttā phrase -> «trí tuệ …»"""
    k = s.strip()
    k = k[0].lower() + k[1:]
    if k in SAMP:
        return f"{PN} {SAMP[k]}"
    return f"{PN} {loc(k)}"


def clause(c):
    """«LOC paññā X paññā» -> «trí tuệ LOC là trí tuệ X»"""
    m = re.match(r"^(.+?) paññā (.+ paññā)$", c.strip())
    assert m, c
    return f"{subj(m.group(1))} là {item(m.group(2))}"


def predication(ln):
    """«(n[. Ka]) C1, C2.» -> «(n[. a]) Trí tuệ … là trí tuệ …; trí tuệ … là trí tuệ ….»"""
    lab, rest = label(ln)
    assert rest.endswith("."), ln
    vi = "; ".join(clause(c) for c in rest[:-1].split(", "))
    return with_label(lab, vi) + "."


# =========================================================================== the matrices ^2-752 … ^2-760
def name_or_item(x):
    x = x.strip()
    k = x[0].lower() + x[1:]
    return NAMES[k] if k in NAMES else item(k)


def atthi_line(rest):
    """«[X paññā [Y paññā]] atthi A, atthi B, atthi C» -> «[Trí tuệ X [và trí tuệ Y] thì] có loại a, có loại b, …»"""
    m = re.match(r"^(.*?)\s*\b[Aa]tthi (.*)$", rest)
    head, body = m.groups()
    kinds = ", ".join(f"{SOME} {attr(a)}" for a in body.split(", atthi "))
    if not head:
        return cap(kinds)
    subj_vi = " và ".join(item(x) for x in re.findall(r"(\S+) paññā", head))
    assert len(re.findall(r"paññā", head)) == len(subj_vi.split(" và trí tuệ")), head
    return f"{cap(subj_vi)} thì {kinds}"


def pe_list(t):
    """«A ñāṇaṃ…pe… B ñāṇaṃ, C ñāṇaṃ» -> names joined by «… » / «, »"""
    toks = re.split(r"(…pe… |, )", t)
    out = ""
    for i, x in enumerate(toks):
        out += ("… " if x.startswith("…pe…") else ", ") if i % 2 else name_or_item(x)
    return out


def mat_line(ln):
    lab, rest = label(ln)
    if re.search(r"\b[Aa]tthi ", rest) and "paññā ācayāya" not in rest and "paññā nibbidāya" not in rest:
        return f"{lab} {atthi_line(rest)}."
    if rest.startswith("Atthi paññā "):
        return f"{lab} " + cap(", ".join(f"có {PN} {CYCLE[x]}" for x in rest[len("Atthi paññā "):].split(
            ", atthi paññā "))) + "."
    return f"{lab} {cap(pe_list(rest))}."


MAT_SPECIAL = {
    "(1) Kammassakatañāṇaṃ, saccānulomikaṃ ñāṇaṃ, maggasamaṅgissa ñāṇaṃ, phalasamaṅgissa ñāṇaṃ":
        f"(1) {cap(KAMMASSAKA)}, {SACCANU}, {MAGGASAM}, {PHALASAM}.",
    ("(4) Dhamme ñāṇaṃ, anvaye ñāṇaṃ, pariye [paricce (sabbattha) passa dīghanikāye] ñāṇaṃ, sammutiñāṇaṃ "
     "[sammatiñāṇaṃ (syā.) passa dīghanikāye]"):
        (f"(4) {cap(DHAMME)}, {ANVAYE}, {PARIYE} {S.reading('mọi bản', 'paricce')[:-1]}; xem Trường Bộ Kinh], "
         f"{SAMMUTI} {S.spell('Syā.', 'sammatiñāṇaṃ')[:-1]}; xem Trường Bộ Kinh]."),
    "(8) Catasso paṭisambhidā": f"(8) {FOUR_PS}.", "(9) Catasso paṭipadā": f"(9) {FOUR_MODES}.",
    "(10) Cattāri ārammaṇāni": f"(10) {FOUR_OBJ}.",
    "(1) Pañcaṅgiko sammāsamādhi (2) pañcañāṇiko sammāsamādhi": f"(1) {cap(PANCANGA)} (2) {PANCANANA}.",
    "(1) Chasu abhiññāsu paññā": f"(1) {cap(SIX)}.", "(1) Sattasattati ñāṇavatthūni": f"(1) {cap(SS77)}.",
    "(1) Catūsu maggesu, catūsu phalesu paññā": "(1) Trí tuệ trong bốn con đường, trong bốn thành quả.",
    "(1) Navasu anupubbavihārasamāpattīsu paññā": f"(1) {cap(NINE)}.",
    "(3) Adhisīle paññā, adhicitte paññā, adhipaññāya paññā":
        f"(3) {cap(NAMES['adhisīle paññā'])}, {NAMES['adhicitte paññā']}, {NAMES['adhipaññāya paññā']}.",
    "(4) Āyakosallaṃ, apāyakosallaṃ, upāyakosallaṃ":
        f"(4) {cap(NAMES['āyakosallaṃ'])}, {NAMES['apāyakosallaṃ']}, {NAMES['upāyakosallaṃ']}.",
}
nf("passa dīghanikāye (variant note)", "xem Trường Bộ Kinh")
nf("(sabbattha) (variant sigla)", "(mọi bản)")


def seg_matrix(n, lines):
    out = [vidha(n) if lines[0].endswith("–") else None]
    assert lines[0] == f"{S.VIDHA[n]} ñāṇavatthu –", lines[0]
    for ln in lines[1:-1]:
        if ln in MAT_SPECIAL:
            out.append(MAT_SPECIAL[ln])
        else:
            out.append(mat_line(ln))
    if lines[-1].startswith("(12-21)"):
        out.append(None)
        ln = lines[-1]
        body, end = ln.split(". Evaṃ ")
        out[-1] = f"(12-21) {cap(pe_list(body[len('(12-21) '):]))}. {vidha_end(4)}"
    else:
        assert lines[-1] == f"Evaṃ {S.VIDHA[n][0].lower() + S.VIDHA[n][1:]} ñāṇavatthu.", lines[-1]
        out.append(vidha_end(n))
    return out


# ---- the ten powers (^2-760)
OBJ = {
    1: "điều có thể xảy ra như là điều có thể xảy ra, và điều không thể xảy ra như là điều không thể xảy ra",
    2: "quả của các nghiệp đã thực hiện trong quá khứ, tương lai và hiện tại, theo hoàn cảnh, theo nguyên nhân",
    3: "cách thực hành dẫn đến mọi nơi",
    4: "thế gian có nhiều yếu tố, có các yếu tố khác nhau",
    5: "chí hướng khác nhau của chúng sinh",
    6: "mức độ cao thấp của các năng lực nơi các chúng sinh khác, những người khác",
    7: ("sự vẩn đục, sự trong sạch, sự xuất khỏi của các tầng thiền, các sự giải thoát, các định tâm và các thành "
        "tựu thiền"),
    8: "sự nhớ lại các đời sống trước",
    9: "sự chết và sự tái sinh của chúng sinh",
    10: "sự diệt tận các ô nhiễm",
}
# ṭhāna / aṭṭhāna «điều có thể / không thể xảy ra» (pi-1 ^1-1344; termbase aṭṭhānato); kammasamādānānaṃ «nghiệp đã
# thực hiện», ṭhānaso «theo hoàn cảnh», hetuso «theo nguyên nhân» (hetu sense 'cause'); sabbattha «mọi nơi»;
# nānādhimuttikataṃ (adhimutti «chí hướng»); saṃkilesaṃ «sự vẩn đục», vodānaṃ «sự trong sạch», vuṭṭhānaṃ «sự xuất
# khỏi»; pubbenivāsānussatiṃ «sự nhớ lại các đời sống trước»; cutūpapātaṃ «sự chết và sự tái sinh»; khayaṃ «sự
# diệt tận»
misfit("indriyaparopariyattaṃ (^2-760, ^2-814, ^2-827): no entry; «mức độ cao thấp của các năng lực»")
misfit("anekadhātu nānādhātulokaṃ (^2-760, ^2-812): no entry; «thế gian có nhiều yếu tố, có các yếu tố khác nhau» "
       "(dhātu «yếu tố», loka «thế gian»)")
OBJ7Q = "sự vẩn đục, sự trong sạch của các tầng thiền, các sự giải thoát, các định tâm và các thành tựu thiền"
VAR4 = S.reading("Syā.", "anekadhātuṃ nānādhātuṃ lokaṃ")[:-1] + "; Trung Bộ Kinh 1.148]"
nf("ma. ni. 1.148 (citation in a variant note)", "Trung Bộ Kinh 1.148")
POWERS = nf("dasa tathāgatassa tathāgatabalāni yehi balehi samannāgato tathāgato āsabhaṃ ṭhānaṃ paṭijānāti, "
            "parisāsu sīhanādaṃ nadati, brahmacakkaṃ pavatteti",
            "mười sức mạnh Như Lai mà Như Lai có; được trang bị những sức mạnh ấy, Như Lai tuyên bố vị trí của bậc "
            "dẫn đầu, rống tiếng rống sư tử trong các hội chúng, chuyển bánh xe cao thượng")
TAIL10 = nf("idampi tathāgatassa tathāgatabalaṃ hoti, yaṃ balaṃ āgamma tathāgato āsabhaṃ ṭhānaṃ paṭijānāti, …",
            "đó cũng là một sức mạnh Như Lai mà Như Lai có; nhờ dựa vào sức mạnh ấy mà Như Lai tuyên bố vị trí của "
            "bậc dẫn đầu, rống tiếng rống sư tử trong các hội chúng, chuyển bánh xe cao thượng")


def power_name(n, q7=False):
    return f"sự hiểu biết đúng như thật của Như Lai về {OBJ7Q if q7 else OBJ[n]}"


def seg_760(lines):
    assert lines[0].startswith("Dasavidhena ñāṇavatthu – dasa tathāgatassa") and lines[0].endswith("Katamāni dasa?")
    out = [f"{vidha(10)} {POWERS}. Mười sức mạnh ấy là gì?"]
    for n, ln in zip(range(1, 11), lines[1:11]):
        assert ln.startswith(f"({n}) "), ln
        first = OBJ[n] + (f" {VAR4}" if n == 4 else "")
        if n == 4:
            assert "[anekadhātuṃ nānādhātuṃ lokaṃ (syā.) ma. ni. 1.148]" in ln
        opener = "Ở đây," if n == 1 else "Lại nữa,"
        v = f"({n}) {opener} Như Lai hiểu rõ đúng như thật {first}. Việc Như Lai hiểu rõ đúng như thật {OBJ[n]}, {TAIL10}."
        if n == 10:
            assert ln.endswith("Imāni dasa tathāgatassa tathāgatabalāni, yehi balehi samannāgato tathāgato āsabhaṃ "
                               "ṭhānaṃ paṭijānāti, parisāsu sīhanādaṃ nadati, brahmacakkaṃ pavatteti.")
            v += f" Đây là {POWERS}."
        out.append(v)
    assert lines[11] == "Evaṃ dasavidhena ñāṇavatthu."
    out.append(vidha_end(10))
    return out


# =========================================================================== the expositions: sentence engine
OBJN = {  # X ārabbha «liên quan đến X»
    "dukkhaṃ": "khổ đau", "dukkhasamudayaṃ": "sự phát sinh của khổ đau", "dukkhanirodhaṃ": "sự chấm dứt khổ đau",
    "dukkhanirodhagāminiṃ paṭipadaṃ": "cách thực hành dẫn đến sự chấm dứt khổ đau",
    "jarāmaraṇaṃ": "sự lão hóa và sự chết", "jarāmaraṇasamudayaṃ": "sự phát sinh của sự lão hóa và sự chết",
    "jarāmaraṇanirodhaṃ": "sự chấm dứt sự lão hóa và sự chết",
    "jarāmaraṇanirodhagāminiṃ paṭipadaṃ": "cách thực hành dẫn đến sự chấm dứt sự lão hóa và sự chết",
    "saṅkhāre": "các sự tạo tác", "saṅkhārasamudayaṃ": "sự phát sinh của các sự tạo tác",
    "saṅkhāranirodhaṃ": "sự chấm dứt các sự tạo tác",
    "saṅkhāranirodhagāminiṃ paṭipadaṃ": "cách thực hành dẫn đến sự chấm dứt các sự tạo tác",
    "paritte dhamme": "các hiện tượng hạn hẹp", "mahaggate dhamme": "các hiện tượng rộng lớn",
    "appamāṇe dhamme": "các hiện tượng không thể đo lường", "atīte dhamme": "các hiện tượng thuộc quá khứ",
    "anāgate dhamme": "các hiện tượng thuộc tương lai", "paccuppanne dhamme": "các hiện tượng thuộc hiện tại",
    "ajjhatte dhamme": "các hiện tượng ở nơi bản thân", "bahiddhādhamme": "các hiện tượng ở bên ngoài bản thân",
    "ajjhattabahiddhā dhamme": "các hiện tượng ở nơi bản thân và ở bên ngoài bản thân",
    "ariyamaggaṃ": "con đường cao quý",
}
ABOUT = "liên quan đến"                                # ārabbha (termbase)
PATIMOKKHA = pi2("sự thu thúc theo bộ giới luật căn bản")   # pātimokkhasaṃvara (ch. 12 ^2-508)
CONDF = {
    "Dānaṃ ārabbha dānādhigaccha": f"{ABOUT} sự bố thí, nhờ sự bố thí",      # ādhigaccha «nhờ»
    "Sīlaṃ ārabbha sīlādhigaccha": f"{ABOUT} giới hạnh, nhờ giới hạnh",
    "Pātimokkhasaṃvaraṃ saṃvarantassa": f"nơi người đang thu thúc bằng {PATIMOKKHA}",
    "Rūpāvacarārūpāvacarasamāpattiṃ samāpajjantassa":
        "nơi người đang chứng nhập thành tựu thiền thuộc cõi hình sắc và cõi không hình sắc",
    "Ariyamaggaṃ adhipatiṃ karitvā": "lấy con đường cao quý làm yếu tố chủ đạo",   # karitvā «lấy … làm»
}
for _a, _av in (("Kicchena kasirena", "một cách khó nhọc, vất vả"), ("Akicchena akasirena",
                                                                     "một cách không khó nhọc, không vất vả")):
    for _b, _bv in (("dandhaṃ", "chậm chạp"), ("khippaṃ", "nhanh chóng")):
        CONDF[f"{_a} samādhiṃ uppādentassa {_b} taṇṭhānaṃ abhijānantassa"] = (
            f"nơi người làm sinh khởi định tâm {_av}, và hiểu biết trực tiếp trạng thái ấy một cách {_bv}")
for _a, _av in (("Samādhissa na nikāmalābhissa", "nơi người không đạt được định tâm theo ý muốn"),
                ("Samādhissa nikāmalābhissa", "nơi người đạt được định tâm theo ý muốn")):
    for _b, _bv in (("thokaṃ", "nhỏ"), ("vipulaṃ", "rộng rãi")):
        CONDF[f"{_a} ārammaṇaṃ {_b} pharantassa"] = f"{_av}, lan tỏa đối tượng ra một phạm vi {_bv}"
misfit("taṇṭhānaṃ (^2-801): no entry; «trạng thái ấy» (tad + ṭhāna)")
misfit("thokaṃ (^2-802): no entry; «một phạm vi nhỏ» beside vipulaṃ «rộng rãi»")


def cond(c):
    c = c.strip()
    if c in CONDF:
        return CONDF[c]
    out = []
    for piece in c.split("…pe… "):
        m = re.match(r"^(.+) ārabbha$", piece.strip())
        assert m, (c, piece)
        out.append(f"{ABOUT} {OBJN[low(m.group(1))]}")
    return "… ".join(out)


ARISE_RX = re.compile(r'^(.+?) yā uppajjati paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi – (?:ayaṃ|idaṃ) '
                      r'vuccati "(.+?)"\.$')
Q_RX = re.compile(r"^[Tt]attha katam(?:ā|aṃ|o|āni) (.+)\?$")
SENT = {}                                              # whole sentences (after the label) -> Vietnamese


def sentence(s):
    if s in SENT:
        return SENT[s]
    m = Q_RX.match(s)
    if m:
        return q(name_or_item(m.group(1)))
    m = ARISE_RX.match(s)
    if m:
        c, n = m.groups()
        return f"{cap(cond(c))}, {ARISES} – {CALLED} “{name_or_item(n)}”."
    if re.match(r"^.+ paññā .+ paññā\.$", s):
        return predication(s)
    raise KeyError(s)


def nid_line(ln):
    ln = ln.replace("pajānanā …pe…", "pajānanā…pe…")
    lab, rest = label(ln)
    rest = rest[0].upper() + rest[1:]
    out = " ".join(sentence(s) for s in K79.SPLIT_RX.split(rest))
    return f"{lab} {out}" if lab else out


def petam(ln):
    """«(N) Maggasamaṅgissa / Dhammasamaṅgissa ñāṇaṃ Xpetaṃ ñāṇaṃ, …» -> «(N) Sự hiểu biết của … cũng là …, …»"""
    lab, rest = label(ln)
    m = re.match(r"^(Maggasamaṅgissa|Dhammasamaṅgissa) ñāṇaṃ (.+)\.$", rest)
    who, body = m.groups()
    toks = re.split(r"(…pe… |, )", body)
    vi = ""
    for i, x in enumerate(toks):
        if i % 2:
            vi += "… " if x.startswith("…pe…") else ", "
        else:
            assert x.endswith("petaṃ ñāṇaṃ"), x
            vi += kn_also(x[:-len("petaṃ ñāṇaṃ")])
    head = MAGGASAM if who == "Maggasamaṅgissa" else DHAMMASAM
    if who == "Dhammasamaṅgissa":
        slip("^2-803 «(12-21) Dhammasamaṅgissa ñāṇaṃ jātiyāpetaṃ ñāṇaṃ…» where the parallel lines (^2-794, ^2-802) "
             "have «Maggasamaṅgissa»: translated as written «sự hiểu biết của người có được Giáo Pháp»")
    return f"{lab} {cap(head)} {vi}."


# ---- fixed sentences of the expositions
SKILL3 = ("trong các ngành nghề được tạo dựng bằng sự khéo léo, trong các ngành thủ công được tạo dựng bằng sự khéo "
          "léo, hoặc trong các lĩnh vực học thuật được tạo dựng bằng sự khéo léo")
# yogavihitesu vā kammāyatanesu … sippāyatanesu … vijjāṭṭhānesu (āyatanesu «ngành», sippāyatanesu «ngành thủ công»)
misfit("yogavihitesu, kammāyatanesu, vijjāṭṭhānesu (^2-768): no whole-word entries; built from yoga «sự khéo léo», "
       "vihitesu «được tạo dựng», āyatanesu «ngành», ṭṭhānesu «lĩnh vực»: «… được tạo dựng bằng sự khéo léo», «ngành "
       "nghề», «lĩnh vực học thuật»")
ANICCA_RUN = ("hoặc rằng “vật chất là vô thường”, hoặc cảm giác… tri giác… các sự tạo tác… hoặc rằng “thức là vô "
              "thường”")                         # rūpaṃ aniccanti vā vedanā…pe… saññā… saṅkhārā… viññāṇaṃ aniccanti vā
KHANTI = ("sự chấp nhận thuận theo, quan điểm, sự ưa thích, sự tán thành, sự xem xét, sự chấp nhận qua việc suy ngẫm "
          "các hiện tượng")
# anulomikaṃ khantiṃ diṭṭhiṃ ruciṃ mudiṃ pekkhaṃ dhammanijjhānakkhantiṃ (termbase; dhammanijjhānakkhanti: no entry)
misfit("dhammanijjhānakkhanti (^2-768, ^2-793): no whole-word entry; «sự chấp nhận qua việc suy ngẫm các hiện tượng» "
       "(khanti «sự chấp nhận», nijjhāna «suy ngẫm», dhamma «hiện tượng»)")
CONTENT3 = f"hoặc về việc nghiệp là tài sản của chính mình, hoặc về điều thuận theo sự thật, {ANICCA_RUN}"


def learnt(heard):
    how = "do nghe từ người khác" if heard else "không phải do nghe từ người khác"
    n = "sutamayā paññā" if heard else "cintāmayā paññā"
    return (f"{cap(SKILL3)}, {CONTENT3}, {SUCH} {KHANTI} mà một người có được {how} – {CALLED} “{NAMES[n]}”.")


SENT.update({
    ('Yogavihitesu vā kammāyatanesu yogavihitesu vā sippāyatanesu yogavihitesu vā vijjāṭṭhānesu kammassakataṃ vā '
     'saccānulomikaṃ vā rūpaṃ aniccanti vā vedanā…pe… saññā… saṅkhārā… viññāṇaṃ aniccanti vā, yaṃ evarūpiṃ '
     'anulomikaṃ khantiṃ diṭṭhiṃ ruciṃ mudiṃ pekkhaṃ dhammanijjhānakkhantiṃ parato assutvā paṭilabhati – ayaṃ '
     'vuccati "cintāmayā paññā".'): learnt(False),
    ('Yogavihitesu vā kammāyatanesu yogavihitesu vā sippāyatanesu yogavihitesu vā vijjāṭṭhānesu kammassakataṃ vā '
     'saccānulomikaṃ vā rūpaṃ aniccanti vā vedanā…pe… saññā… saṅkhārā… viññāṇaṃ aniccanti vā, yaṃ evarūpiṃ '
     'anulomikaṃ khantiṃ diṭṭhiṃ ruciṃ mudiṃ pekkhaṃ dhammanijjhānakkhantiṃ parato sutvā paṭilabhati – ayaṃ '
     'vuccati "sutamayā paññā".'): learnt(True),
    "Sabbāpi samāpannassa paññā bhāvanāmayā paññā.":
        f"Mọi trí tuệ của người đã chứng nhập đều là {NAMES['bhāvanāmayā paññā']}.",
    'Catūsu maggesu catūsu phalesu paññā – ayaṃ vuccati "adhipaññāya paññā".':
        f"{cap(EIGHT)} – {CALLED} “{NAMES['adhipaññāya paññā']}”.",
    "Sabbāpi tatrupāyā paññā upāyakosallaṃ.":
        f"Mọi trí tuệ về phương cách cho việc ấy đều là {NAMES['upāyakosallaṃ']}.",   # tatrupāyā (termbase)
    "Catūsu maggesu catūsu phalesu paññā dhamme ñāṇaṃ.": f"{cap(EIGHT)} là {DHAMME}.",
    "Catūsu maggesu paññā maggasamaṅgissa ñāṇaṃ.": f"Trí tuệ trong bốn con đường là {MAGGASAM}.",
    "Catūsu phalesu paññā phalasamaṅgissa ñāṇaṃ.": f"Trí tuệ trong bốn thành quả là {PHALASAM}.",
    "Ṭhapetvā dhamme ñāṇaṃ anvaye ñāṇaṃ pariye ñāṇaṃ, avasesā paññā sammutiñāṇaṃ.":
        f"Ngoại trừ {DHAMME}, {ANVAYE}, {PARIYE}, trí tuệ còn lại là {SAMMUTI}.",
    "Kāmāvacarakusale paññā ācayāya no apacayāya.":
        f"{cap(subj('Kāmāvacarakusale'))} thì {CYCLE['ācayāya no apacayāya']}.",
    "Catūsu maggesu paññā apacayāya no ācayāya.":
        f"{cap(subj('catūsu maggesu'))} thì {CYCLE['apacayāya no ācayāya']}.",
    "Rūpāvacarārūpāvacarakusale paññā ācayāya ceva apacayāya ca.":
        f"{cap(subj('rūpāvacarārūpāvacarakusale'))} thì {CYCLE['ācayāya ceva apacayāya ca']}.",
    "Avasesā paññā neva ācayāya no apacayāya.": f"Trí tuệ còn lại thì {CYCLE['neva ācayāya no apacayāya']}.",
    "Catūsu maggesu paññā nibbidāya ceva paṭivedhāya ca.":
        f"{cap(subj('catūsu maggesu'))} thì {CYCLE['nibbidāya ceva paṭivedhāya ca']}.",
    "Avasesā paññā neva nibbidāya no paṭivedhāya.": f"Trí tuệ còn lại thì {CYCLE['neva nibbidāya no paṭivedhāya']}.",
    "Imā catasso paṭipadā.": f"Đây là {low(FOUR_MODES)}.",
    "Imāni cattāri ārammaṇāni.": f"Đây là {low(FOUR_OBJ)}.",
    ("Dukkhapaṭipadā dandhābhiññā paññā, dukkhapaṭipadā khippābhiññā paññā, sukhapaṭipadā dandhābhiññā paññā, "
     "sukhapaṭipadā khippābhiññā paññā."): cap(", ".join(f"{PN} {v}" for v in MODE.values())) + ".",
    ("Parittā parittārammaṇā paññā, parittā appamāṇārammaṇā paññā, appamāṇā parittārammaṇā paññā, appamāṇā "
     "appamāṇārammaṇā paññā."): cap(", ".join(f"{PN} {v}" for v in OBJ4.values())) + ".",
    "Evaṃ duvidhena ñāṇavatthu.": vidha_end(2), "Evaṃ tividhena ñāṇavatthu.": vidha_end(3),
    "Dukaṃ.": CLOSE[2], "Tikaṃ.": CLOSE[3], "Catukkaṃ.": CLOSE[4], "Pañcakaṃ.": CLOSE[5],
    "Chakkaṃ.": CLOSE[6], "Sattakaṃ.": CLOSE[7], "Aṭṭhakaṃ.": CLOSE[8], "Navakaṃ.": CLOSE[9], "Dasakaṃ.": CLOSE[10],
})
for _n, _p in CLOSE_P.items():
    nf(_p + " (closing label)", CLOSE[_n])
SENT["Evaṃ catubbidhena ñāṇavatthu."] = vidha_end(4)

# =========================================================================== explicit lines of the expositions
NV = "không nên nói rằng"                              # na vattabbā "…"ti (ch. 15 «thì không nên nói rằng»)
SIYA = K1.SIYA                                         # siyā «đôi khi»
POSITIVE = K23.p1("1-1221")
POSITIVE = POSITIVE[POSITIVE.index("“Không có sự bố thí"):POSITIVE.index("rồi tuyên bố”") + len("rồi tuyên bố”")]
POSITIVE = POSITIVE.replace(" [dị bản (Ka.): samaggatā]", "").replace("“Không có", "“Có").replace("không có ", "có ")
assert "không" not in POSITIVE, POSITIVE
# ^2-793 «Atthi dinnaṃ, atthi yiṭṭhaṃ, …» = the pi-1 ^1-1221 wrong view «Natthi dinnaṃ …» put positively
FOUR_T = ["khổ đau", "sự phát sinh của khổ đau", "sự chấm dứt khổ đau", "cách thực hành dẫn đến sự chấm dứt khổ đau"]
V_ABBH = S.spell("Syā.", "abbhaññiṃsu")[:-1] + ", cũng vậy ở các chỗ sau]"    # [abbhaññiṃsu (syā.) evamuparipi]
assert V_ABBH.endswith(pi2(", cũng vậy ở các chỗ sau]"))


def inference_line():
    def knew(tense, var=""):
        verb = "đã hiểu biết trực tiếp" if tense == "p" else "sẽ hiểu biết trực tiếp"
        when = "trong thời quá khứ" if tense == "p" else "trong thời tương lai"
        first = f"{verb} {FOUR_T[0]}" + (f" {var}" if var else "")
        a = ", ".join([first] + [f"{verb} {t}" for t in FOUR_T[1:]])
        b = ", ".join(f"{verb} chính {t} này" for t in FOUR_T)
        return f"Bất cứ sa-môn hay bà-la-môn nào {when} {a}, thì họ {b}"
    return (f"(b) Bằng Giáo Pháp này, đã được biết, đã được thấy, đã được đạt đến, đã được hiểu, đã được thâm nhập, "
            f"vị ấy suy ra đối với quá khứ và tương lai: “{knew('p', V_ABBH)}. {knew('f')}” – {YA_TATTHA} {PANNA} – "
            f"{CALLED} “{ANVAYE}”.")


misfit("^2-796 «so iminā dhammena ñātena …» (termbase dhammena «điều»): «bằng Giáo Pháp này», as dhamme ñāṇaṃ of the "
       "same path-knowledge set («sự hiểu biết về Giáo Pháp», user note); ñātena «đã được biết», pariyogāḷhena «đã "
       "được thâm nhập», nayaṃ neti «suy ra»")
STATES = [("sarāgaṃ", "có tham đắm"), ("vītarāgaṃ", "đã lìa tham đắm"), ("sadosaṃ", "có sân hận"),
          ("vītadosaṃ", "đã lìa sân hận"), ("samohaṃ", "có si mê"), ("vītamohaṃ", "đã lìa si mê"),
          ("saṃkhittaṃ", "co rút"), ("vikkhittaṃ", "tán loạn"), ("mahaggataṃ", "rộng lớn"),
          ("amahaggataṃ", "không rộng lớn"), ("sauttaraṃ", "còn có điều cao hơn"),
          ("anuttaraṃ", "không có điều gì cao hơn"), ("samāhitaṃ", "được định tâm"),
          ("asamāhitaṃ", "không được định tâm"), ("vimuttaṃ", "được giải thoát"),
          ("avimuttaṃ", "không được giải thoát")]       # termbase «tâm có tham đắm» … (ch. 7 ^2-? wording)
MINDS = "; ".join(f"{'hoặc ' if i else ''}khi tâm {v}, vị ấy hiểu rõ: “Tâm {v}”" for i, (_, v) in enumerate(STATES))
pi2("hoặc khi tâm đã lìa tham đắm, vị ấy hiểu rõ: “Tâm")


def pariye_line():
    return (f"(c) {q(PARIYE)} Ở đây, vị tỳ-khưu dùng tâm bao quát tâm của các chúng sinh khác, của những người khác "
            f"mà hiểu rõ. {cap(MINDS)} – {YA_TATTHA} {PANNA} – {CALLED} “{PARIYE}”.")


HANA, THITI = P(LOCAL["hānabhāgī"]), P(LOCAL["ṭhitibhāgī"])
VISESA, NIBBEDHA = P(LOCAL["visesabhāgī"]), P(LOCAL["nibbedhabhāgī"])
SAHA = {"kāma": "có dục lạc đi kèm", "avitakka": "không có sự hướng tâm đi kèm",
        "vitakka": "có sự hướng tâm đi kèm", "upekkhā": "có sự bình thản đi kèm",
        "pītisukha": "có sự hân hoan và hạnh phúc đi kèm",
        "adukkhamasukha": "có cảm giác không khó chịu cũng không dễ chịu đi kèm",
        "rūpa": "có hình sắc đi kèm", "ākāsa": f"có {K10.AY_INF['ākāsa']} đi kèm",
        "viññāṇa": f"có {K10.AY_INF['viññāṇa']} đi kèm", "ākiñcañña": f"có {K10.AY_INF['ākiñcañña']} đi kèm",
        "nevasaññā": f"có {K10.AY_INF['nevasaññā']} đi kèm"}
# kāmasahagatā saññāmanasikārā «tri giác và sự chú tâm có dục lạc đi kèm» (termbase), samudācaranti «khởi lên»,
# lābhiṃ «người đã đạt được», tadanudhammatā sati santiṭṭhati «sự tỉnh thức phù hợp với điều ấy đứng vững»,
# virāgūpasañhitā «liên quan đến sự phai nhạt»
misfit("avitakkasahagatā (^2-799): no entry; «không có sự hướng tâm đi kèm» (sahagata «có … đi kèm»)")


def hana(att, saha):
    return f"Khi tri giác và sự chú tâm {SAHA[saha]} khởi lên nơi người đã đạt được {att}, đó là {HANA}."


THITI_S = f"Khi sự tỉnh thức phù hợp với điều ấy đứng vững, đó là {THITI}."


def visesa(saha):
    return f"Khi tri giác và sự chú tâm {SAHA[saha]} khởi lên, đó là {VISESA}."


NIBBEDHA_S = (f"Khi tri giác và sự chú tâm có sự nhàm chán đi kèm, liên quan đến sự phai nhạt, khởi lên, đó là "
              f"{NIBBEDHA}.")
LEVELS = [("tầng thiền thứ hai", "vitakka", "upekkhā"), ("tầng thiền thứ ba", "pītisukha", "adukkhamasukha"),
          ("tầng thiền thứ tư", "upekkhā", "ākāsa"), (K10.AY_INF["ākāsa"], "rūpa", "viññāṇa"),
          (K10.AY_INF["viññāṇa"], "ākāsa", "ākiñcañña"), (K10.AY_INF["ākiñcañña"], "viññāṇa", "nevasaññā")]


def seg_799(lines):
    assert lines[3].count("samudācaranti") == 1 + 3 * 6 and lines[3].count("santiṭṭhati") == 6
    l4 = [NIBBEDHA_S]
    for att, h, v in LEVELS:
        l4 += [hana(att, h), THITI_S, visesa(v), NIBBEDHA_S]
    return [f"(7. a) {q(HANA)} {hana('tầng thiền thứ nhất', 'kāma')}", f"(b) {THITI_S}",
            f"(c) {visesa('avitakka')}", "(d) " + " ".join(l4)]


ADH = {  # the dispositions of beings (^2-813, ^2-818)
    "low": "những chúng sinh có chí hướng thấp kém", "high": "những chúng sinh có chí hướng ưu việt"}
# hīnādhimuttikā «có chí hướng thấp kém», paṇītādhimuttikā «có chí hướng ưu việt»; sevanti «gần gũi», bhajanti «lui
# tới», payirupāsanti «thường xuyên lui tới hầu cận» (and the aorist / future forms)
VERB = {"pres": "gần gũi, lui tới, thường xuyên lui tới hầu cận",
        "past": "đã gần gũi, đã lui tới, đã thường xuyên lui tới hầu cận",
        "fut": "sẽ gần gũi, sẽ lui tới, sẽ thường xuyên lui tới hầu cận"}
THERE_ARE = f"Có {ADH['low']}, có {ADH['high']}."


def consort(t, who):
    return f"{ADH[who]} {VERB[t]} {ADH[who]}"


def adh_lines(quoted):
    o = "“" if quoted else ""
    l1 = f"{o}{THERE_ARE} {cap(consort('pres', 'low'))}. {cap(consort('pres', 'high'))}."
    if quoted:
        l2 = f"“Cả trong thời quá khứ, {consort('past', 'low')}, {consort('past', 'high')}."
        l3 = f"“Cả trong thời tương lai, {consort('fut', 'low')}, {consort('fut', 'high')}”."
    else:
        l2 = f"Cả trong thời quá khứ, {consort('past', 'low')}. {cap(consort('past', 'high'))}."
        l3 = f"Cả trong thời tương lai, {consort('fut', 'low')}. {cap(consort('fut', 'high'))}."
    return l1, l2, l3


ASAYA, ANUSAYA, CARITA, ADHIMUTTI = "thiên hướng", "khuynh hướng tiềm ẩn", "tính hạnh", "chí hướng"
DUST_HI, DUST_LO = "có nhiều bụi trong mắt", "có ít bụi trong mắt"     # mahārajakkhā / apparajakkhā (rajakkhā)
SHARP, DULL = "có các năng lực sắc bén", "có các năng lực non yếu"     # tikkhindriyā / mudindriyā
GOOD, BAD = "có phẩm chất tốt", "có phẩm chất xấu"                     # svākārā / dvākārā
EASY, HARD = "dễ hướng dẫn", "khó hướng dẫn"                           # suviññāpayā / duviññāpayā
ABLE, UNABLE = "có khả năng", "không có khả năng"                      # bhabbā / abhabbā
misfit("apparajakkha / mahārajakkha (^2-814 …): rajakkhā «bụi trong mắt»; «có ít / có nhiều bụi trong mắt»")
VIEWS = K23.p1("1-1105")
VIEWS = pi1(VIEWS[VIEWS.index("“Thế gian là trường tồn”"):VIEWS.index("; điều mà")])
IDAP = pi1("quy luật tùy thuộc vào điều kiện và các hiện tượng sinh khởi tùy thuộc vào điều kiện")   # pi-1 ^1-1008
KILESA10 = K23.p1("1-1235")
KILESA10 = pi1(KILESA10[KILESA10.index("Mười chỗ dựa của phiền não"):])
assert KILESA10.endswith("sự không biết ghê sợ tội lỗi."), KILESA10
FIVE_IND = ("Năm năng lực – năng lực niềm tin, năng lực tinh tấn, năng lực tỉnh thức, năng lực định tâm, năng lực "
            "trí tuệ.")                                # Pañcindriyāni – saddhindriyaṃ … paññindriyaṃ (termbase)
PRACT = "được thực hành, được tu tập, được làm đi làm lại, trở nên nổi trội"   # āsevitāni … ussadagatāni (termbase)
NOPRACT = "không được thực hành, không được tu tập, không được làm đi làm lại, không trở nên nổi trội"
PATHS = [("vào dòng"), ("trở lại một lần"), ("không trở lại"), ("A-la-hán")]   # Sotāpatti, sakadāgāmi, anāgāmi, arahatta
ORD4 = ["thứ nhất", "thứ hai", "thứ ba", "thứ tư"]
SAMAP9 = ([f"thành tựu thiền của tầng thiền {o}" for o in ORD4]
          + [f"thành tựu thiền của {K10.AY_INF[k]}" for k in ("ākāsa", "viññāṇa", "ākiñcañña", "nevasaññā")]
          + ["thành tựu thiền chấm dứt tri giác và cảm giác"])
# paṭhamajjhānasamāpatti … saññāvedayitanirodhasamāpatti (user: samāpatti «thành tựu thiền»; saññā «tri giác»,
# vedayita «cảm giác», nirodha «sự chấm dứt»)
misfit("…samāpattiyā (^2-808: ākāsānañcāyatanasamāpattiyā … nevasaññānāsaññāyatanasamāpattiyā, termbase «sự chứng "
       "đạt …»): written «thành tựu thiền của …» after the user decision samāpatti «thành tựu thiền» (pi-1 aligned) "
       "and the ch. 12 wording; samāpattiṃ (^2-767) likewise «thành tựu thiền»")
DEP = [("jāti", "jarāmaraṇaṃ"), ("bhava", "jāti"), ("upādāna", "bhavo"), ("taṇhā", "upādānaṃ"),
       ("vedanā", "taṇhā"), ("phassa", "vedanā"), ("saḷāyatana", "phasso"), ("nāmarūpa", "saḷāyatanaṃ"),
       ("viññāṇa", "nāmarūpaṃ"), ("saṅkhāra", "viññāṇaṃ"), ("avijjā", "saṅkhārā")]


def link(c, r):
    return K6.clause(f"{c}paccayā {r}", sut=True)     # «sự sinh làm điều kiện cho sự lão hóa và sự chết» (pi-1)


def know_that(x):
    return f"{KN} rằng {x}"


STAB = ("sự hiểu biết rằng sự hiểu biết ấy của vị ấy về tính ổn định của các hiện tượng, điều đó cũng có bản chất "
        "diệt tận, có bản chất suy tàn, có bản chất phai nhạt, có bản chất chấm dứt")
# Yampissa taṃ dhammaṭṭhitiñāṇaṃ tampi khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhammanti ñāṇaṃ (khaya «diệt
# tận», vaya «suy tàn», virāga «phai nhạt», nirodha «sự chấm dứt»; ṭhiti «sự ổn định»)
misfit("dhammaṭṭhitiñāṇaṃ (^2-806): no whole-word entry; «sự hiểu biết về tính ổn định của các hiện tượng» (ṭṭhiti "
       "«tính ổn định»; tampi «điều đó cũng»)")


def six_dep(c, r):
    nc = K6.N[K6.STEM[c]] if c != "saṅkhāra" else "các sự tạo tác"
    nr = K6.noun(r, True) if r != "saṅkhārā" else "các sự tạo tác"
    l, neg = link(c, r), f"khi không có {nc} thì không có {nr}"
    return [know_that(l), know_that(neg), know_that(f"cả trong thời quá khứ, {l}"), know_that(neg),
            know_that(f"cả trong thời tương lai, {l}"), know_that(neg)]


def seg_806(lines):
    first, last = DEP[0], DEP[-1]
    mid = "… ".join(know_that(link(c, r)) for c, r in DEP[1:-1])
    l1 = (f"{q(SS77)} {cap(', '.join(six_dep(*first)))}. {cap(STAB)}; {mid}… {', '.join(six_dep(*last))}. "
          f"{cap(STAB)}. Đây là {SS77}. {vidha_end(7)}")
    assert lines[0].count("…pe…") == 9, lines[0]
    return [l1, CLOSE[7]]


CLOSE_PANNA = f"{cap(YA_TATTHA)} {PANNA}"             # Yā tattha paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi


def sphere_line(ln):
    """(28)-(30) «Xāvacarakusalābyākate paññā Xāvacarā paññā, A paññā B paññā C paññā na Xāvacarā paññā.»"""
    lab, rest = label(ln)
    first, others = rest[:-1].split(", ", 1)
    m = re.match(r"^(.*) paññā (na \S+) paññā$", others)
    subs = re.findall(r"(\S+) paññā", m.group(1) + " paññā")
    return f"{lab} {cap(clause(first))}; {', '.join(item(s) for s in subs)} là {item(m.group(2))}."


A35 = (f"{cap(subj('Catūsu bhūmīsu kusale'))}, và trí tuệ trong {MIND['kiriyābyākate']} của bậc A-la-hán đang làm sinh "
       f"khởi sự hiểu biết trực tiếp, đang làm sinh khởi thành tựu thiền, là {item('atthajāpikā')}; "
       f"{subj('catūsu bhūmīsu vipāke')}, và trí tuệ trong {MIND['kiriyābyākate']} của bậc A-la-hán khi sự hiểu biết "
       f"trực tiếp đã sinh khởi, khi thành tựu thiền đã sinh khởi, là {item('jāpitatthā')}.")
# arahato «bậc A-la-hán», abhiññaṃ «sự hiểu biết trực tiếp», uppādentassa «làm sinh khởi», uppannāya «đã sinh khởi»


def seg_767(lines):
    out = []
    for i, ln in enumerate(lines):
        if ln.startswith("(2) Sabbāva paññā kenaci viññeyyā"):
            out.append("(2) Mọi trí tuệ đều là điều mà một loại thức nào đó có thể nhận biết, và một loại thức nào đó "
                       "không thể nhận biết.")
        elif re.match(r"^\((28|29|30)\)", ln):
            out.append(sphere_line(ln))
        elif ln.startswith("Catūsu bhūmīsu kusale arahato"):
            out.append(A35)
        elif ln in SENT:
            out.append(SENT[ln])
        else:
            out.append(nid_line(ln))
    return out


AYA_TEXT = {
    "āya": ("“Khi chú tâm đến những hiện tượng này, các hiện tượng bất thiện chưa sinh khởi không sinh khởi, và các hiện "
            "tượng bất thiện đã sinh khởi được dứt bỏ. Hoặc khi chú tâm đến những hiện tượng này, các hiện tượng thiện "
            "chưa sinh khởi sinh khởi, và các hiện tượng thiện đã sinh khởi dẫn đến chỗ được tăng trưởng, được lớn "
            "mạnh, được tu tập, được hoàn thiện”"),
    "apāya": ("“Khi chú tâm đến những hiện tượng này, các hiện tượng thiện chưa sinh khởi không sinh khởi, và các hiện "
              "tượng thiện đã sinh khởi chấm dứt. Hoặc khi chú tâm đến những hiện tượng này, các hiện tượng bất thiện "
              "chưa sinh khởi sinh khởi, và các hiện tượng bất thiện đã sinh khởi dẫn đến chỗ được tăng trưởng, được "
              "lớn mạnh”")}
# manasikaroto «chú tâm», pahīyanti «được dứt bỏ», nirujjhanti «chấm dứt», saṃvattanti «dẫn đến», bhiyyobhāvāya
# vepullāya bhāvanāya pāripūriyā «được tăng trưởng, được lớn mạnh, được tu tập, được hoàn thiện» (pi-1 ^1-1377)


def kosalla(k, lab):
    n = NAMES[f"{k}kosallaṃ"]
    return f"{lab} {q(n)} {AYA_TEXT[k]} – {YA_TATTHA} {PANNA} – {CALLED} “{n}”."


NOBLE, WORLDLING = "người thành tựu về quan điểm", "người phàm phu"   # diṭṭhisampanno puggalo / puthujjano
DES = "quả đáng mong muốn, đáng yêu mến, đáng ưa thích"               # iṭṭho kanto manāpo vipāko
UND = "quả không đáng mong muốn, không đáng yêu mến, không đáng ưa thích"
HEAVEN = "cõi tốt lành, thế giới cõi trời"                            # sugatiṃ saggaṃ lokaṃ
HELL = "cõi khổ, cõi xấu, nơi đọa lạc, địa ngục"                      # apāyaṃ duggatiṃ vinipātaṃ nirayaṃ
misfit("apāyaṃ (^2-809, ^2-830): no entry; «cõi khổ» beside duggatiṃ «cõi xấu», vinipātaṃ «nơi đọa lạc»")


def imp(x):
    return nf("aṭṭhānametaṃ anavakāso yaṃ X, netaṃ ṭhānaṃ vijjatī\"ti pajānāti",
              "Như Lai hiểu rõ: “Đây là điều không thể xảy ra, không có cơ hội, rằng {x}; điều ấy không thể xảy ra”."
              ).format(x=x)


def pos(x):
    return nf("ṭhānañca kho etaṃ vijjati yaṃ X, ṭhānametaṃ vijjatī\"ti pajānāti",
              "Như Lai hiểu rõ: “Nhưng đây là điều có thể xảy ra, rằng {x}; điều ấy có thể xảy ra”.").format(x=x)


def reborn(who, dest):
    return f"{who}, do nguyên nhân ấy, do điều kiện ấy, khi thân tan rã, sau khi chết, tái sinh vào {dest}"
# X-samaṅgī «người có X», tannidānaṃ tappaccayā «do nguyên nhân ấy, do điều kiện ấy», kāyassa bhedā paraṃ maraṇā
# «khi thân tan rã, sau khi chết», upapajjeyya «tái sinh»


YE_YE = ("“Những hiện tượng nào là nguyên nhân, là điều kiện của những hiện tượng nào, thì tùy thuộc vào đó mà có điều "
         "có thể xảy ra tương ứng; những hiện tượng nào không phải là nguyên nhân, không phải là điều kiện của những "
         "hiện tượng nào, thì tùy thuộc vào đó mà có điều không thể xảy ra tương ứng”.")
misfit("^2-809 appaccayā in «na hetū appaccayā upādāya taṃ taṃ aṭṭhānaṃ» (termbase «không có điều kiện», the adverb "
       "of 'ahetu appaccayā'): «không phải là điều kiện» (predicate beside na hetū «không phải là nguyên nhân»); "
       "upādāya «tùy thuộc vào» (termbase); pi-1 ^1-1344 has «uppādāya» «cho sự sinh khởi» in the same sentence")
CONDUCT = {"kd": "hành vi xấu bằng thân", "vd": "hành vi xấu bằng lời nói", "md": "hành vi xấu bằng ý",
           "ks": "hành vi tốt bằng thân", "vs": "hành vi tốt bằng lời nói", "ms": "hành vi tốt bằng ý"}


def seg_809(lines):
    L = []
    L.append(f"(1) {q(power_name(1))} Ở đây, " + imp(f"{NOBLE} xem một sự tạo tác nào đó là thường hằng") + " "
             + " ".join([pos(f"{WORLDLING} xem một sự tạo tác nào đó là thường hằng"),
                         imp(f"{NOBLE} xem một sự tạo tác nào đó là hạnh phúc"),
                         pos(f"{WORLDLING} xem một sự tạo tác nào đó là hạnh phúc"),
                         imp(f"{NOBLE} xem một hiện tượng nào đó là ý nghĩa"),
                         pos(f"{WORLDLING} xem một hiện tượng nào đó là ý nghĩa"),
                         imp(f"{NOBLE} tước đoạt mạng sống của mẹ"), pos(f"{WORLDLING} tước đoạt mạng sống của mẹ")]))
    L.append(imp(f"{NOBLE} tước đoạt mạng sống của cha… tước đoạt mạng sống của một bậc A-la-hán… với tâm độc ác làm "
                 "cho máu của Như Lai chảy… chia rẽ Tăng đoàn… tôn một vị khác làm bậc đạo sư… tạo ra lần hiện hữu "
                 "thứ tám") + " " + pos(f"{WORLDLING} tạo ra lần hiện hữu thứ tám"))
    L.append(" ".join([imp("trong một thế giới, hai bậc A-la-hán, Tự Giác Ngộ Hoàn Toàn, xuất hiện không trước không "
                           "sau"), pos("trong một thế giới, một bậc A-la-hán, Tự Giác Ngộ Hoàn Toàn, xuất hiện"),
                       imp(f"trong một thế giới, hai vị vua chuyển luân {S.spell('Sī., Syā.', 'cakkavatti')} xuất "
                           "hiện không trước không sau"), pos("trong một thế giới, một vị vua chuyển luân xuất hiện")]))
    L.append(" ".join([imp("một người nữ là bậc A-la-hán, Tự Giác Ngộ Hoàn Toàn"),
                       pos("một người nam là bậc A-la-hán, Tự Giác Ngộ Hoàn Toàn"),
                       imp("một người nữ là vua chuyển luân"), pos("một người nam là vua chuyển luân"),
                       imp("một người nữ giữ địa vị Đế Thích, giữ địa vị Ma vương, giữ địa vị Phạm thiên"),
                       pos("một người nam giữ địa vị Đế Thích, giữ địa vị Ma vương, giữ địa vị Phạm thiên")]))
    for a, good, bad in (("d", DES, UND), ("s", UND, DES)):
        L.append(" ".join([imp(f"{CONDUCT['k' + a]} tạo ra {good}"), pos(f"{CONDUCT['k' + a]} tạo ra {bad}"),
                           imp(f"{CONDUCT['v' + a]}… {CONDUCT['m' + a]} tạo ra {good}"),
                           pos(f"{CONDUCT['v' + a]}… {CONDUCT['m' + a]} tạo ra {bad}")]))
    for a, good, bad in (("d", HEAVEN, HELL), ("s", HELL, HEAVEN)):
        one = f"người có {CONDUCT['k' + a]}"
        pe = f"người có {CONDUCT['v' + a]}… người có {CONDUCT['m' + a]}"
        L.append(" ".join([imp(reborn(one, good)), pos(reborn(one, bad)), imp(reborn(pe, good)),
                           pos(reborn(pe, bad))]))
    L[-1] += f" {YE_YE} {CLOSE_PANNA} – đây là {power_name(1)}."
    slip("^2-809 (2nd line) «Aṭṭhānametaṃ anavakāso yaṃ … pitaraṃ …»: opening quotation mark missing (rendered as "
         "meant)")
    slip("^2-809 «kañci dhammaṃ atthato upagaccheyya»: atthato translated as written «là ý nghĩa» (user note; the "
         "termbase reads it as attato «tự ngã»)")
    return L


KIND = {"pāpakāni": "xấu ác", "kalyāṇāni": "tốt đẹp"}
FACT = [("gati", "cõi tái sinh"), ("upadhi", "thân thể"), ("kāla", "thời điểm"), ("payoga", "sự nỗ lực")]
misfit("kāla in kālasampatti / kālavipatti (^2-810): no entry; «thời điểm»")


def karma(k, c, blocked):
    if blocked:
        return " ".join(f"Có những nghiệp {KIND[k]} đã thực hiện bị ngăn trở bởi {c} về {f} nên không trổ quả."
                        for _, f in FACT)
    return " ".join(f"Có những nghiệp {KIND[k]} đã thực hiện nhờ dựa vào {c} về {f} mà trổ quả." for _, f in FACT)
# atthekaccāni «có những», kammasamādānāni «nghiệp đã thực hiện», paṭibāḷhāni «ngăn trở», vipaccanti «trổ quả»,
# āgamma «nhờ dựa vào», sampatti «sự thuận lợi», vipatti «sự bất lợi»


def seg_810(lines):
    last = karma("kalyāṇāni", "sự thuận lợi", False)
    return [f"(2) {q(power_name(2))} Ở đây, Như Lai hiểu rõ – “{karma('pāpakāni', 'sự thuận lợi', True)}",
            f"“{karma('pāpakāni', 'sự bất lợi', False)}", f"“{karma('kalyāṇāni', 'sự bất lợi', True)}",
            f"“{last[:-1]}”. {CLOSE_PANNA} – đây là {power_name(2)}."]


def seg_811(lines):
    tg = ["địa ngục", "cõi súc sinh", "cõi ngạ quỷ", "thế giới loài người", "thế giới chư thiên", "Niết-bàn"]
    v1 = S.reading("Syā.", "nirayagāminīti")
    v2 = S.reading("Syā.", "tiracchānagāminīti")[:-1] + ", cũng vậy ở các chỗ sau; nên xem chú giải]"
    parts = []
    for i, t in enumerate(tg):
        s = f"hiểu rõ: “Đây là con đường, đây là cách thực hành dẫn đến {t}”"
        s += f" {v1}" if i == 0 else f" {v2}" if i == 1 else ""
        parts.append(s)
    nf("aṭṭhakathā oloketabbā (variant note)", "nên xem chú giải")
    return [f"(3) {q(power_name(3))} Ở đây, Như Lai {', '.join(parts)}. {CLOSE_PANNA} – đây là {power_name(3)}."]


def seg_812(lines):
    kinds = ["các khối", "các lĩnh vực nhận biết", "các yếu tố", OBJ[4]]
    body = ", ".join(f"hiểu rõ sự khác nhau của {k}" for k in kinds)
    return [f"(4) {q(power_name(4))} Ở đây, Như Lai {body}. {CLOSE_PANNA} – đây là {power_name(4)}."]


def seg_813(lines):
    l1, l2, l3 = adh_lines(True)
    return [f"(5) {q(power_name(5))} Ở đây, Như Lai hiểu rõ – {l1}", l2,
            f"{l3} {CLOSE_PANNA} – đây là {power_name(5)}."]


def seg_818(lines):
    l1, l2, l3 = adh_lines(False)
    return [f"{cap(ADHIMUTTI)} của chúng sinh là gì? {l1}", l2, f"{l3} Đây là {ADHIMUTTI} của chúng sinh."]


ONE_LINE = {
    "2-814": (f"(6) {q(power_name(6))} Ở đây, Như Lai hiểu rõ {ASAYA} của chúng sinh, hiểu rõ {ANUSAYA}, hiểu rõ "
              f"{CARITA}, hiểu rõ {ADHIMUTTI}, hiểu rõ các chúng sinh {DUST_LO}, {DUST_HI}, {SHARP}, {DULL}, {GOOD}, "
              f"{BAD}, {EASY}, {HARD}, {ABLE} và {UNABLE}."),
    "2-815": (f"{cap(ASAYA)} của chúng sinh là gì? {VIEWS}; như vậy, chúng sinh hoặc nương tựa vào quan điểm về sự "
              "hiện hữu, hoặc nương tựa vào quan điểm về sự không còn hiện hữu. Hoặc, không đi đến hai cực đoan này, "
              f"họ đạt được sự chấp nhận thuận theo đối với {IDAP}, tức sự hiểu biết đúng như thật. Đây là {ASAYA} "
              "của chúng sinh."),
    "2-816": (f"{cap(ANUSAYA)} của chúng sinh là gì? Bảy khuynh hướng tiềm ẩn – khuynh hướng tiềm ẩn tham đắm dục lạc, "
              "khuynh hướng tiềm ẩn ác cảm, khuynh hướng tiềm ẩn kiêu mạn, khuynh hướng tiềm ẩn quan điểm, khuynh "
              "hướng tiềm ẩn hoài nghi, khuynh hướng tiềm ẩn tham đắm sự hiện hữu, khuynh hướng tiềm ẩn vô minh. "
              f"{pi2('Điều gì trong thế gian là điều đáng yêu, là điều khoan khoái, thì ở đó')} khuynh hướng tiềm ẩn "
              "tham đắm của chúng sinh nằm sẵn. Điều gì trong thế gian là điều không đáng yêu, là điều không khoan "
              "khoái, thì ở đó khuynh hướng tiềm ẩn ác cảm của chúng sinh nằm sẵn. Như vậy, vô minh đi theo hai hiện "
              "tượng này. Sự kiêu mạn, quan điểm và sự hoài nghi nên được xem là cùng hiện diện với nó. Đây là "
              f"{ANUSAYA} của chúng sinh."),
    "2-817": (f"{cap(CARITA)} của chúng sinh là gì? "
              f"{pi2('Sự tạo tác thuộc về phước, sự tạo tác không thuộc về phước, sự tạo tác dẫn đến trạng thái bất động')}"
              f", thuộc cấp độ nhỏ hoặc thuộc cấp độ lớn – đây là {CARITA} của chúng sinh."),
    "2-819": (f"Những chúng sinh {DUST_HI} là những ai? {KILESA10} Nơi những chúng sinh nào mười chỗ dựa của phiền não "
              f"này {PRACT}, thì những chúng sinh ấy {DUST_HI}."),
    "2-820": (f"Những chúng sinh {DUST_LO} là những ai? Nơi những chúng sinh nào mười chỗ dựa của phiền não này "
              f"{NOPRACT}, thì những chúng sinh ấy {DUST_LO}."),
    "2-821": (f"Những chúng sinh {DULL} là những ai? {FIVE_IND} Nơi những chúng sinh nào năm năng lực này {NOPRACT}, "
              f"thì những chúng sinh ấy {DULL}."),
    "2-822": (f"Những chúng sinh {SHARP} là những ai? Nơi những chúng sinh nào năm năng lực này {PRACT}, thì những "
              f"chúng sinh ấy {SHARP}."),
    "2-823": (f"Những chúng sinh {BAD} là những ai? Những chúng sinh nào có thiên hướng xấu ác, có khuynh hướng tiềm ẩn "
              f"xấu ác, có tính hạnh xấu ác, có chí hướng xấu ác, {DUST_HI}, {DULL}, thì những chúng sinh ấy {BAD}."),
    "2-824": (f"Những chúng sinh {GOOD} là những ai? Những chúng sinh nào có thiên hướng tốt đẹp, có tính hạnh tốt đẹp, "
              f"có chí hướng tốt đẹp, {DUST_LO}, {SHARP}, thì những chúng sinh ấy {GOOD}."),
    "2-825": (f"Những chúng sinh {HARD} là những ai? Những chúng sinh nào {BAD}, chính những chúng sinh ấy {HARD}. "
              f"Những chúng sinh nào {GOOD}, chính những chúng sinh ấy {EASY}."),
    "2-826": (f"Những chúng sinh {UNABLE} là những ai? Những chúng sinh nào mang sự ngăn che do nghiệp, mang sự ngăn "
              "che do phiền não, mang sự ngăn che do quả của nghiệp, không có niềm tin, không có ý muốn, kém trí tuệ, "
              "không có khả năng bước vào sự cố định, tức sự đúng đắn trong các hiện tượng thiện, thì những chúng sinh "
              f"ấy {UNABLE}."),
    "2-827": (f"Những chúng sinh {ABLE} là những ai? Những chúng sinh nào không mang sự ngăn che do nghiệp, không mang "
              "sự ngăn che do phiền não, không mang sự ngăn che do quả của nghiệp, có niềm tin, có ý muốn, có trí tuệ, "
              "có khả năng bước vào sự cố định, tức sự đúng đắn trong các hiện tượng thiện, thì những chúng sinh ấy "
              f"{ABLE}. {CLOSE_PANNA} – đây là {power_name(6)}."),
}
misfit("pāpāsayā / pāpānusayā / pāpacaritā / pāpādhimuttikā (^2-823): termbase pāpa «người xấu» (compound member); "
       "written «có thiên hướng xấu ác …» (pāpakāni «xấu ác»), since the beings themselves are meant")
misfit("bhavarāgānusayo (^2-816): no entry; «khuynh hướng tiềm ẩn tham đắm sự hiện hữu» (Kāmarāgānusayo, rāgānusayo)")
misfit("avijjānupatitā (^2-816): no entry; «vô minh đi theo»")
misfit("vipākāvaraṇena (^2-826): no entry; «sự ngăn che do quả của nghiệp» (kammāvaraṇena, kilesāvaraṇena)")
JH = "người hành thiền"                                 # jhāyī (termbase)


def seg_828(lines):
    T = K79.TOPIC_W.format
    f1 = [f"có {JH} cho rằng điều vốn là sự thành công {S.spell('Ka.', 'sampattiyeva')} là sự thất bại",
          f"có {JH} cho rằng điều vốn là sự thất bại {S.spell('Ka.', 'vipattiyeva')} là sự thành công",
          f"có {JH} cho rằng điều vốn là sự thành công là sự thành công",
          f"có {JH} cho rằng điều vốn là sự thất bại là sự thất bại"]
    f2 = [f"có {JH} chứng nhập chậm chạp, xuất khỏi nhanh chóng", f"có {JH} chứng nhập nhanh chóng, xuất khỏi chậm chạp",
          f"có {JH} chứng nhập chậm chạp, xuất khỏi chậm chạp", f"có {JH} chứng nhập nhanh chóng, xuất khỏi nhanh chóng"]
    sk = "khéo léo về định tâm trong định tâm"            # samādhismiṃ samādhikusalo (termbase phrase)
    sp = "khéo léo về sự chứng đạt trong định tâm"        # samādhismiṃ samāpattikusalo (termbase phrase)
    f3 = [f"có {JH} {sk} nhưng không {sp}", f"có {JH} {sp} nhưng không {sk}",
          f"có {JH} vừa {sk} vừa {sp}", f"có {JH} không {sk} cũng không {sp}"]
    four = f"đây là bốn {JH}."
    vim = ["Người có hình sắc thấy các hình sắc", "Người có tri giác về phi hình sắc ở nơi bản thân thấy các hình sắc "
           "ở bên ngoài bản thân", "Người chỉ quyết định hướng đến điều đẹp", cap(K10.AR1), cap(K10.AR2),
           cap(K10.AR3), cap(K10.AR4), f"Hoàn toàn vượt qua {K10.AY_INF['nevasaññā']}, vị ấy chứng nhập và an trú "
           "sự chấm dứt tri giác và cảm giác"]
    for a in (K10.AR1, K10.AR2, K10.AR3, K10.AR4):
        pi2(a)
    ords = ["thứ nhất", "thứ hai", "thứ ba", "thứ tư", "thứ năm", "thứ sáu", "thứ bảy", "thứ tám"]
    L = [f"(7) {q(power_name(7, q7=True))} {T(x=JH)} có bốn {JH}. {cap('; '.join(f1))} – {four}",
         f"Lại có bốn {JH} khác. {cap('; '.join(f2))} – {four}",
         f"Lại có bốn {JH} khác. {cap('; '.join(f3))} – {four}",
         f"{T(x='tầng thiền')} {low(pi2(K10.JHANA4))}"]
    for i, (v, o) in enumerate(zip(vim, ords)):
        s = f"{v} – đây là sự giải thoát {o}."
        L.append(f"{T(x='sự giải thoát')} tám sự giải thoát. {s}" if i == 0 else s)
    L.append(f"{T(x='định tâm')} ba loại định tâm – định tâm có sự hướng tâm và sự duy trì tâm, định tâm không có sự "
             "hướng tâm chỉ có sự duy trì tâm, định tâm không có sự hướng tâm cũng không có sự duy trì tâm.")
    L.append(f"{T(x='thành tựu thiền')} chín thành tựu thiền an trú tuần tự – {', '.join(SAMAP9)}.")
    L.append(f"{T(x='sự vẩn đục')} hiện tượng thuộc về phía suy giảm. {T(x='sự trong sạch')} hiện tượng thuộc về "
             f"phía thăng tiến. {T(x='sự xuất khỏi')} sự trong sạch cũng là sự xuất khỏi, sự xuất khỏi từng định tâm "
             f"ấy cũng là sự xuất khỏi. {CLOSE_PANNA} – đây là {power_name(7)}.")
    slip("^2-828 «sampattiyeva [sampattiyeva (ka.)]»: the Ka. variant repeats the text word (kept as printed)")
    slip("^2-828 the question «… saṃkilesaṃ vodānaṃ yathābhūtaṃ ñāṇaṃ?» lacks «vuṭṭhānaṃ», which the closing and the "
         "matrix have: translated as written")
    return L


PAST = ("một đời, hai đời, ba đời, bốn đời, năm đời, mười đời, hai mươi đời, ba mươi đời, bốn mươi đời, năm mươi đời, "
        "một trăm đời, một nghìn đời, một trăm nghìn đời, nhiều kiếp thế giới tan hoại, nhiều kiếp thế giới hình "
        "thành, nhiều kiếp thế giới tan hoại và hình thành")
LIFE = ("tôi có tên như vậy, thuộc dòng họ như vậy, có dung mạo như vậy, ăn thức ăn như vậy, cảm nhận hạnh phúc và khổ "
        "đau như vậy, có tuổi thọ đến mức như vậy")
RECALL = "Như Lai nhớ lại nhiều đời sống trước theo nhiều cách"   # anekavihitaṃ pubbenivāsaṃ anussarati
EYE = ("bằng thiên nhãn thanh tịnh, vượt quá mắt người, Như Lai thấy chúng sinh đang chết đi, đang tái sinh, thấp kém, "
       "ưu việt, đẹp đẽ, xấu xí, ở cõi tốt lành, ở cõi xấu, và hiểu rõ các chúng sinh đi theo nghiệp của mình")
misfit("saṃvaṭṭakappe / vivaṭṭakappe (^2-829): no whole-word entries; saṃvaṭṭa «tan hoại», vivaṭṭa «hình thành», "
       "kappe «kiếp thế giới»")


def seg_829(lines):
    return [f"(8) {q(power_name(8))} Ở đây, {RECALL}, cụ thể là – {PAST}: “Ở nơi kia, {LIFE}; chết từ nơi ấy, tôi "
            f"đã sinh ra ở nơi kia; ở nơi kia, {LIFE.replace('tôi có tên', 'tôi cũng có tên')}; chết từ nơi ấy, tôi "
            f"đã tái sinh ở đây”. Như vậy, {RECALL}, với các nét đặc trưng và chi tiết. {CLOSE_PANNA} – đây là "
            f"{power_name(8)}."]


def seg_830(lines):
    bad = ("mang hành vi xấu bằng thân, mang hành vi xấu bằng lời nói, mang hành vi xấu bằng ý, phỉ báng các bậc "
           "thánh, có quan điểm sai lầm, thực hiện nghiệp theo quan điểm sai lầm")
    good = ("mang hành vi tốt bằng thân, mang hành vi tốt bằng lời nói, mang hành vi tốt bằng ý, không phỉ báng các "
            "bậc thánh, có quan điểm đúng đắn, thực hiện nghiệp theo quan điểm đúng đắn")
    misfit("^2-830 «ime vata bhonto sattā» / «ime vā pana bhonto sattā»: bhonto rendered with the termbase sense of "
           "bho «thưa ngài» (polite address) as the plural «thưa các ngài»; vata «quả thật»")
    return [f"(9) {q(power_name(9))} Ở đây, {EYE} – “Quả thật, thưa các ngài, những chúng sinh này {bad}. Khi thân "
            f"tan rã, sau khi chết, họ đã tái sinh vào {HELL}. Hoặc, thưa các ngài, những chúng sinh này {good}. Khi "
            "thân tan rã, sau khi chết, họ "
            f"đã tái sinh vào {HEAVEN}”. Như vậy, {EYE}. {CLOSE_PANNA} – đây là {power_name(9)}."]


def seg_831(lines):
    return [f"(10) {q(power_name(10))} Ở đây, nhờ sự diệt tận các ô nhiễm, Như Lai ngay trong đời này tự mình hiểu "
            "biết trực tiếp, chứng nghiệm, chứng nhập và an trú sự giải thoát của tâm, sự giải thoát nhờ trí tuệ, "
            f"không còn ô nhiễm. {CLOSE_PANNA} – đây là {power_name(10)}.", CLOSE[10],
            f"{S.CH_HEADINGS['Ñāṇavibhaṅgo']} {K1.DONE}."]


# ---- the remaining explicit lines
SUFFUSE = ["sự lan tỏa của sự hân hoan", "sự lan tỏa của hạnh phúc", "sự lan tỏa của tâm", "sự lan tỏa của ánh sáng",
           "dấu hiệu xem xét lại"]
# pītipharaṇatā … ālokapharaṇatā (pharaṇatā «sự lan tỏa»), paccavekkhaṇānimittaṃ (paccavekkhaṇā «xem xét lại»,
# nimittaṃ «dấu hiệu»); Dibbacakkhu «thiên nhãn» (dibbena «thiên», cakkhunā «nhãn»); paccavekkhaṇāñāṇaṃ «sự hiểu
# biết xem xét lại»
L804_1 = (f"(1) {q(PANCANGA)} {cap(', '.join(SUFFUSE))}. Trí tuệ trong hai tầng thiền là {SUFFUSE[0]}. Trí tuệ trong "
          f"ba tầng thiền là {SUFFUSE[1]}. Sự hiểu biết về tâm người khác là {SUFFUSE[2]}. Thiên nhãn là {SUFFUSE[3]}. "
          f"Sự hiểu biết xem xét lại của người đã xuất khỏi từng định tâm ấy là {SUFFUSE[4]}. {cap(CALLED)} "
          f"{PANCANGA}.")
FIVE_K = ["Định tâm này vừa có hạnh phúc trong hiện tại, vừa có quả là hạnh phúc trong tương lai",
          "Định tâm này cao quý, không có tính trần tục", "Định tâm này được những người không hèn kém thực hành",
          ("Định tâm này an tịnh, ưu việt, đạt được nhờ sự lắng dịu hoàn toàn, đạt đến sự hợp nhất của tâm, không phải đạt được "
           "nhờ sự kiềm chế và ngăn chặn có sự thúc đẩy"),
          "Tôi tỉnh thức chứng nhập định tâm này, tỉnh thức xuất khỏi định tâm này"]
# paccuppannasukho, āyatiñca sukhavipāko, ariyo «cao quý», nirāmiso «không có tính trần tục», akāpurisasevito, santo
# «an tịnh», paṇīto «ưu việt», paṭippassaddhaladdho (no entry: «đạt được nhờ sự lắng dịu»), ekodibhāvādhigato,
# sasaṅkhāraniggayhavāritagato (termbase), sato «tỉnh thức», samāpajjāmi «chứng nhập», vuṭṭhahāmi «xuất khỏi»
misfit("paṭippassaddhaladdho (^2-804): no whole-word entry; «đạt được nhờ sự lắng dịu hoàn toàn» (paṭippassaddha)")
L804_2 = (f"(2) {q(PANCANANA)} " + " ".join(f"Ngay nơi tự thân, sự hiểu biết sinh khởi rằng: “{x}”." for x in FIVE_K)
          + f" Đây là {PANCANANA}. {vidha_end(5)}")
SIX_LIST = [f"{KN} về các loại thần thông", f"{KN} về sự trong sạch của yếu tố tai", f"{KN} về tâm người khác",
            f"{KN} về sự nhớ lại các đời sống trước", f"{KN} về sự chết và sự tái sinh của chúng sinh",
            f"{KN} về sự diệt tận các ô nhiễm"]
# Iddhividhe (Iddhi «thần thông»), sotadhātuvisuddhiyā (sotadhātu «yếu tố tai»), paracitte «tâm người khác»,
# pubbenivāsānussatiyā, cutūpapāte, khaye (termbase)
L805 = f"{q(SIX)} {cap(', '.join(SIX_LIST))} – đây là {SIX}. {vidha_end(6)}"
PATHS8 = []
for _p in PATHS:
    PATHS8 += [f"trí tuệ trong con đường {_p}", f"trí tuệ trong thành quả {_p}"]
L807 = f"{q(EIGHT)} {cap(', '.join(PATHS8))} – đây là {EIGHT}. {vidha_end(8)}"
L808 = (f"{q(NINE)} {cap(', '.join(f'trí tuệ trong {s}' for s in SAMAP9[:8]))}, sự hiểu biết xem xét lại của người "
        f"đã xuất khỏi {SAMAP9[8]} – đây là {NINE}. {vidha_end(9)}")
L800 = (f"(8) {q(low(FOUR_PS))} {cap(', '.join(K13.PS[k] for k in K13.PS_ORDER))}. "
        + pi2(K13.ps_list("Atthe ñāṇaṃ atthapaṭisambhidā, dhamme ñāṇaṃ dhammapaṭisambhidā, tatra dhammaniruttābhilāpe "
                          "ñāṇaṃ niruttipaṭisambhidā, ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā", "2-800"))
        + f". Đây là {low(FOUR_PS)}.")
L793_1 = (f"(1. a) {q(KAMMASSAKA)} {POSITIVE} – {SUCH} {PANNA} – {CALLED} “{KAMMASSAKA}”. Ngoại trừ {SACCANU}, mọi "
          f"trí tuệ thiện mà là đối tượng của ô nhiễm đều là {KAMMASSAKA}.")
L793_2 = f"(b) {q(SACCANU)} {cap(ANICCA_RUN)}, {SUCH} {KHANTI} – {CALLED} “{SACCANU}”."
L798_1 = (f"(6. a) {q(NAMES['paññā nibbidāya no paṭivedhāya'])} Nhờ trí tuệ nào mà một người lìa tham đắm đối với "
          "các dục lạc, nhưng không thấu triệt các loại hiểu biết trực tiếp, cũng không thấu triệt các sự thật – "
          f"{CALLED} “{NAMES['paññā nibbidāya no paṭivedhāya']}”.")
L798_2 = ("(b) Chính người ấy, vốn đã lìa tham đắm đối với các dục lạc nhờ trí tuệ, thấu triệt các loại hiểu biết trực "
          "tiếp nhưng không thấu triệt các sự thật – "
          f"{CALLED} “{NAMES['paññā paṭivedhāya no nibbidāya']}”.")
# vītarāgo «lìa tham đắm», kāmesu «dục lạc», abhiññāyo «loại hiểu biết trực tiếp», paṭivijjhati «thấu triệt»,
# saccāni «sự thật», samāno «vốn là»
L784 = (f"(14) {cap(subj('Catūsu bhūmīsu vipāke'))} {SIYA} {K1.ITEMS['uppanno']}, {SIYA} {K1.ITEMS['uppādī']}, "
        f"{NV} “{K1.ITEMS['anuppanno']}”. {cap(subj('catūsu bhūmīsu kusale tīsu bhūmīsu kiriyābyākate'))} {SIYA} "
        f"{K1.ITEMS['uppanno']}, {SIYA} {K1.ITEMS['anuppanno']}, {NV} “{K1.ITEMS['uppādī']}”.")
L785 = f"(15) Mọi trí tuệ {SIYA} {K1.ITEMS['atīto']}, {SIYA} {K1.ITEMS['anāgato']}, {SIYA} {K1.ITEMS['paccuppanno']}."
L789 = (f"(17) Mọi trí tuệ {SIYA} {K1.ITEMS['ajjhatto']}, {SIYA} {K1.ITEMS['bahiddho']}, {SIYA} "
        f"{K1.ITEMS['ajjhattabahiddho']}.")
L777 = (f"(b) Trí tuệ trong {pi1('thành quả A-la-hán cao nhất')} {S.reading('Syā.', 'upariṭṭhime')[:-1]}; (Ka.): "
        f"upariṭṭhimaṃ] là {item('asekkhā')}.")


slip("^2-804 «So kho panāhaṃ imaṃ samādhiṃ sato samāpajjāmi sato vuṭṭhahāmī\"ti»: opening quotation mark missing "
     "(rendered as meant)")
slip("^2-815 «\"hoti tathāgato paraṃ maraṇāti vā»: closing quotation mark missing (rendered as meant, pi-1 ^1-1105 "
     "wording)")
slip("^2-751 the first two matrix lines carry no numbers «(1)», «(2)» (the list starts at «(3)»): kept as printed")


def fix_803(ln):
    bad = 'paṭipadāya ñāṇaṃ. Evaṃ catubbidhena ñāṇavatthu.'
    if bad in ln:
        slip('^2-803 «idaṃ vuccati "saṅkhāranirodhagāminiyā paṭipadāya ñāṇaṃ. Evaṃ …»: closing quotation mark '
             'missing (rendered as meant)')
        ln = ln.replace(bad, 'paṭipadāya ñāṇaṃ". Evaṃ catubbidhena ñāṇavatthu.')
    return ln


OVR = {
    ("2-771", 0): lambda ln: kosalla("āya", "(4. a)"), ("2-771", 1): lambda ln: kosalla("apāya", "(b)"),
    ("2-777", 1): lambda ln: L777, ("2-784", 0): lambda ln: L784, ("2-785", 0): lambda ln: L785,
    ("2-789", 0): lambda ln: L789, ("2-793", 0): lambda ln: L793_1, ("2-793", 1): lambda ln: L793_2,
    ("2-794", 0): petam, ("2-796", 1): lambda ln: inference_line(), ("2-796", 2): lambda ln: pariye_line(),
    ("2-798", 0): lambda ln: L798_1, ("2-798", 1): lambda ln: L798_2, ("2-800", 0): lambda ln: L800,
    ("2-802", 5): petam, ("2-803", 0): petam, ("2-803", 2): lambda ln: nid_line(fix_803(ln)),
    ("2-804", 0): lambda ln: L804_1, ("2-804", 1): lambda ln: L804_2, ("2-804", 2): lambda ln: CLOSE[5],
    ("2-805", 0): lambda ln: L805, ("2-805", 1): lambda ln: CLOSE[6],
    ("2-807", 0): lambda ln: L807, ("2-807", 1): lambda ln: CLOSE[8],
    ("2-808", 0): lambda ln: L808, ("2-808", 1): lambda ln: CLOSE[9],
}
PREFIX = {  # a guard against drift: the Pāli line must start so
    ("2-771", 0): "(4. Ka) tattha katamaṃ āyakosallaṃ?", ("2-771", 1): "(Kha) tattha katamaṃ apāyakosallaṃ?",
    ("2-777", 1): "(Kha) upariṭṭhimā", ("2-784", 0): "(14) Catūsu bhūmīsu vipāke", ("2-785", 0): "(15) Sabbāva",
    ("2-789", 0): "(17) Sabbāva", ("2-793", 0): "(1. Ka) tattha katamaṃ kammassakatañāṇaṃ?",
    ("2-793", 1): "(Kha) tattha katamaṃ saccānulomikaṃ", ("2-796", 1): "(Kha) so iminā dhammena",
    ("2-796", 2): "(Ga) tattha katamaṃ pariye ñāṇaṃ?", ("2-798", 0): "(6. Ka)", ("2-798", 1): "(Kha) sveva",
    ("2-800", 0): "(8) Tattha katamā catasso paṭisambhidā?", ("2-804", 0): "(1) Tattha katamo pañcaṅgiko",
    ("2-804", 1): "(2) Tattha katamo pañcañāṇiko", ("2-804", 2): "Pañcakaṃ.",
    ("2-805", 0): "Tattha katamā chasu abhiññāsu paññā?", ("2-805", 1): "Chakkaṃ.",
    ("2-807", 0): "Tattha katamā catūsu maggesu", ("2-807", 1): "Aṭṭhakaṃ.",
    ("2-808", 0): "Tattha katamā navasu", ("2-808", 1): "Navakaṃ.",
}
SEGS = {"2-751": seg_751, "2-760": seg_760, "2-761": seg_761, "2-762": seg_762,
        "2-763": lambda ls: [cross("2-763", ls[0], "g")], "2-764": seg_764,
        "2-765": lambda ls: [cross("2-765", ls[0], "s")], "2-766": seg_766, "2-767": seg_767, "2-799": seg_799,
        "2-806": seg_806, "2-809": seg_809, "2-810": seg_810, "2-811": seg_811, "2-812": seg_812, "2-813": seg_813,
        "2-818": seg_818, "2-828": seg_828, "2-829": seg_829, "2-830": seg_830, "2-831": seg_831}
for _n in range(2, 10):
    SEGS[f"2-{750 + _n}"] = (lambda n: (lambda ls: seg_matrix(n, ls)))(_n)
for _sid, _v in ONE_LINE.items():
    SEGS[_sid] = (lambda v: (lambda ls: [v]))(_v)


# =========================================================================== build and checks
def heading(ln):
    lvl, text = ln.split(" ", 1)
    return f"{lvl} {HEAD[text]}"


def check16(sid, p, v):
    assert K79.dashes(p) == K79.dashes(v), (sid, "dash count", K79.dashes(p), K79.dashes(v), v[:200])
    assert ":-" not in v and "—" not in v and "…." not in v, (sid, v[:160])
    body = re.sub(r"\[[^\]]*\]", "", v)
    assert not K10.FOREIGN.search(body), (sid, K10.FOREIGN.search(body).group(0), v[:200])
    assert "  " not in v and not v.endswith(" "), (sid, v[:160])
    assert "là là" not in v, (sid, v[:160])
    if p.count('"') % 2 == 0:
        assert v.count("“") == v.count("”"), (sid, "quotes", v[:200])
    if not p.startswith("#"):
        assert v[-1] in ".?…–", (sid, v[-40:])
        assert p.endswith("?") == v.endswith("?"), (sid, v[-40:])
        assert p.endswith("–") == v.endswith("–"), (sid, v[-40:])


def build():
    pali = (S.PALI / PART).read_text(encoding="utf-8")
    h = {}
    for sid, lines in K1.segs(pali):
        lines = [K1.ID.sub("", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            h[sid] = [heading(lines[0])]
            continue
        if sid in SEGS:
            vi = SEGS[sid](lines)
        else:
            vi = []
            for i, ln in enumerate(lines):
                if (sid, i) in OVR:
                    assert ln.startswith(PREFIX.get((sid, i), "")), (sid, i, ln[:80])
                    vi.append(OVR[(sid, i)](ln))
                elif ln in SENT:
                    vi.append(SENT[ln])
                else:
                    vi.append(nid_line(ln))
        assert len(vi) == len(lines), (sid, len(vi), len(lines))
        h[sid] = [unicodedata.normalize("NFC", x) for x in vi]
    for sid, lines in K1.segs(pali):
        for p, v in zip([K1.ID.sub("", ln) for ln in lines], h[sid]):
            check16(sid, p, v)
    return pali, h


def check_pi1():
    text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI1_VI.glob("*.md")))
    missing = [s for s in PI1_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    return len(PI1_USED)


def check_pi2():
    files = ["1-khandhavibhango.md", "2-ayatanavibhango.md", "3-dhatuvibhango.md", "4-saccavibhango.md",
             "5-indriyavibhango.md", "6-paticcasamuppadavibhango.md", "7-satipatthanavibhango.md",
             "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md", "10-bojjhangavibhango.md",
             "11-maggangavibhango.md", "12-jhanavibhango.md", "13-appamannavibhango.md",
             "14-sikkhapadavibhango.md", "15-patisambhidavibhango.md"]
    text = "\n".join((S.OUT / f).read_text(encoding="utf-8") for f in files)
    missing = [s for s in PI2_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    return len(PI2_USED)


# =========================================================================== notes
def notes_md():
    L = ["# pi-2 Vietnamese rails: new formulas of chapter 16 (^2-16-0 … ^2-831)", "",
         "Generated by build_rails_16_vi.py; import it instead of retyping. Strings already in vi-rails-formulas.md "
         "(sample) or notes-1 … notes-13-15 are not repeated (the matrix items come from ch. 1 / pi-1, the paṭisambhidā "
         "names from ch. 15, the formless attainments and «Bốn tầng thiền» from ch. 12, the topic frames from ch. 6-9). "
         "Format: Pāli = tiếng Việt.", "", "## Headings and closing labels", ""]
    L += [f"#### / ##### {p} = {v}" for p, v in HEAD.items()]
    L += ["", "## Frames, names and recurring strings", ""]
    L += [f"{p} = {v}" for p, v in NOTES]
    L += [f"X paññā (matrix item) = {PN} + the ch. 1 item; «mà» before «là» / «không phải là» (termbase «trí tuệ mà là "
          "đối tượng của ô nhiễm»)",
          f"[X] atthi A, atthi B, atthi C = [Trí tuệ X thì] {SOME} a, {SOME} b, {SOME} c",
          "LOC paññā X paññā, … = Trí tuệ LOC là trí tuệ X; … (LOC: «trong tâm thiện và không xác định về mặt đạo đức "
          "thuộc ba cõi», «trong bốn con đường và bốn thành quả», «trong quả của nghiệp thuộc bốn cõi», «trong tâm mang "
          "tính chức năng không xác định về mặt đạo đức thuộc ba cõi», «trong tâm thiện thuộc cõi dục lạc» …)",
          "X-sampayuttā / -vippayuttā paññā = " + "; ".join(f"{k} = {PN} {v}" for k, v in SAMP.items()),
          "X ñāṇaṃ = sự hiểu biết về x; Xpetaṃ ñāṇaṃ = cũng là sự hiểu biết về x",
          f"Tattha katamā/katamaṃ X? … X ārabbha yā uppajjati paññā … – ayaṃ/idaṃ vuccati \"X\". = Ở đây, x là gì? "
          f"{cap(ABOUT)} …, {ARISES} – {CALLED} “x”.",
          f"Yā tattha paññā pajānanā…pe… sammādiṭṭhi – idaṃ … = {CLOSE_PANNA} – đây là …",
          f"yā evarūpā paññā … = {SUCH} {PANNA}",
          "names: " + "; ".join(f"{k} = {v}" for k, v in NAMES.items()),
          "conditions: " + "; ".join(f"{k} = {v}" for k, v in CONDF.items()),
          "ārabbha objects: " + "; ".join(f"{k} = {v}" for k, v in OBJN.items()),
          "the five consciousnesses: " + "; ".join(f"{k} = {v}" for k, v in MAT1.items()),
          f"pañca viññāṇā na hetumeva, … jarābhibhūtameva = {FIVE} {MEVA_VI}",
          f"Pañcahi viññāṇehi … / samanantarāpi … / samanantarā manodhātuyāpi … = {BY5} … / {AFTER5} … / {MANO5} …",
          f"yāthāvakavatthuvibhāvanā paññā = {YATHAVA}",
          "the ten powers (objects): " + "; ".join(f"({n}) {v}" for n, v in OBJ.items()),
          "power name = sự hiểu biết đúng như thật của Như Lai về <object>",
          f"(Ka) aṭṭhānametaṃ … = see imp(); kammasamādāna lines: {karma('pāpakāni', 'sự thuận lợi', True)}",
          f"the dispositions: {THERE_ARE} {cap(consort('pres', 'low'))}.",
          f"āsaya / anusaya / carita / adhimutti = {ASAYA} / {ANUSAYA} / {CARITA} / {ADHIMUTTI}",
          f"apparajakkhā / mahārajakkhā / tikkhindriyā / mudindriyā / svākārā / dvākārā / suviññāpayā / duviññāpayā / "
          f"bhabbā / abhabbā = {DUST_LO} / {DUST_HI} / {SHARP} / {DULL} / {GOOD} / {BAD} / {EASY} / {HARD} / {ABLE} / "
          f"{UNABLE}",
          f"āsevitāni … ussadagatāni / anāsevitāni … = {PRACT} / {NOPRACT}",
          f"hāna / ṭhiti / visesa / nibbedha-bhāginī paññā = {HANA} / {THITI} / {VISESA} / {NIBBEDHA}",
          f"pañcaṅgiko sammāsamādhi factors = {', '.join(SUFFUSE)}",
          f"the nine attainments = {', '.join(SAMAP9)}",
          f"Xpaccayā Yti ñāṇaṃ / asati X natthi Yti ñāṇaṃ = {know_that(link('jāti', 'jarāmaraṇaṃ'))} / "
          f"{know_that('khi không có sự sinh thì không có sự lão hóa và sự chết')}",
          f"Yampissa taṃ dhammaṭṭhitiñāṇaṃ … nirodhadhammanti ñāṇaṃ = {STAB}",
          f"pubbenivāsa list = {PAST}; amutrāsiṃ evaṃnāmo … = {LIFE}",
          f"dibbena cakkhunā … pajānāti = {EYE}"]
    return unicodedata.normalize("NFC", "\n".join(L) + "\n")


def main():
    dry = "--dry" in sys.argv
    pali, h = build()
    text = K10.render(pali, h)
    if not dry:
        (S.OUT / PART).write_bytes(text.encode("utf-8"))
    print(f"{'built' if dry else 'wrote'} {PART}: {len(h)} segments")
    n1, n2 = check_pi1(), check_pi2()
    if not dry:
        NOTES_PATH.write_bytes(notes_md().encode("utf-8"))
    print(f"pi-1 strings checked: {n1}; pi-2 strings checked: {n2}")
    for s in SLIPS:
        print("slip:", s)
    for s in MISFITS:
        print("misfit:", s)


if __name__ == "__main__":
    main()
