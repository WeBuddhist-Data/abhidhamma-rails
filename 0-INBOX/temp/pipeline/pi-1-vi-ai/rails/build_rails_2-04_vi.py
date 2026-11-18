"""Builder for the Vietnamese rails translation of pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng», plain audience),
chapter 2-04 (the twelve unwholesome minds and the first wholesome-resultant minds, ^1-1-6-0 … ^1-504).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/2-04-cittuppadakandam.md
  0-INBOX/temp/pipeline/pi-1-vi-ai/rails/notes-2-04.md

Every line is translated from the Pāli by fixed strings. The earlier rails builders are imported, never edited:
build_rails_sample_vi.py (S), build_rails_2-01_2-02_vi.py (B) and build_rails_2-03_vi.py (T, which loads B and
extends its tables in memory). B's tables NAMES and STR are extended in memory with the 2-04 material below, and
B.tail_vi is wrapped so that the «ime dhammā akusalā / abyākatā» closings and «X abyākatamūlaṃ» are translated
first (the wrapper changes nothing for lines without them). A check rebuilds 2-01, 2-02 and 2-03 in memory with
the extended tables and requires them to equal the finished files byte for byte.
Unknown Pāli raises KeyError, so nothing is guessed silently.
Terms follow the locked termbase AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md
(+ pi-1-vi-ai/termbase/APPROVED.md: bodily/mental pain dukkha = «khó chịu»; pleasant feeling = «dễ chịu», so the
body-consciousness ^1-443 … ^1-454 takes «sự dễ chịu» for sukhaṃ). Translated fresh from the Pāli.
Later chapter builders may import this file (importing writes nothing).

usage: python -I -X utf8 build_rails_2-04_vi.py
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-vi-ai\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)

_spec = importlib.util.spec_from_file_location("build_rails_2_03_vi", HERE / "build_rails_2-03_vi.py")
T = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T)        # importing writes nothing; T.B is the extended 2-01/2-02 builder
B = T.B

PART = "2-04-cittuppadakandam.md"
PALI = S.PALI / PART
OUT = S.OUT / PART
TS = S.TS
cap = S.cap
PE, ELL, DASH = "…pe…", "…", "–"

# =========================================================================================
# 1. Matrix predicates (from 1-matika) and the closings
# =========================================================================================
Q_AKUSALA = S.q_form(S.PREDS["akusalā"])          # Những hiện tượng nào là bất thiện?
A_AKUSALA = S.a_form(S.PREDS["akusalā"])[:-1]     # những hiện tượng này là bất thiện
Q_ABY = S.q_form(S.PREDS["abyākatā"])             # Những hiện tượng nào không xác định về mặt đạo đức?
A_ABY = S.a_form(S.PREDS["abyākatā"])[:-1]        # những hiện tượng này không xác định về mặt đạo đức
Q = {"akusalā": Q_AKUSALA, "abyākatā": Q_ABY}
ABY = "không xác định về mặt đạo đức"
ROOT_AKUSALA = "tức gốc rễ bất thiện"             # X akusalamūlaṃ -> «X, tức gốc rễ bất thiện»
ROOT_ABY = f"tức gốc rễ {ABY}"                    # X abyākatamūlaṃ -> «X, tức gốc rễ không xác định …»
assert S.ROOT_OF == "tức gốc rễ thiện"

# =========================================================================================
# 2. New names (nominative)
# =========================================================================================
NEW_NAMES = {
    "micchādiṭṭhi": "quan điểm sai lầm",
    "micchāsaṅkappo": "tư duy sai lầm",
    "micchāvāyāmo": "nỗ lực sai lầm",
    "micchāsamādhi": "định tâm sai lầm",
    "ahirikabalaṃ": "sức mạnh không biết hổ thẹn",
    "anottappabalaṃ": "sức mạnh không biết ghê sợ tội lỗi",
    "lobho": "sự tham lam",
    "moho": "sự si mê",
    "abhijjhā": "sự thèm muốn",
    "ahirikaṃ": "sự không biết hổ thẹn",
    "anottappaṃ": "sự không biết ghê sợ tội lỗi",
    "doso": "sự sân hận",
    "byāpādo": "sự ác ý",
    "dukkhaṃ": "sự khó chịu",                     # APPROVED: pain = «khó chịu»
    "domanassindriyaṃ": "năng lực nỗi buồn",       # as somanassindriyaṃ «năng lực niềm vui»
    "vicikicchā": "sự hoài nghi",
    "uddhaccaṃ": "sự xao động",
    "sukhindriyaṃ": "năng lực dễ chịu",            # APPROVED: pleasant feeling = «dễ chịu»
    "pañcindriyāni": "năm năng lực",
    "cattāri indriyāni": "bốn năng lực",
    "tīṇindriyāni": "ba năng lực",
    "cattāri balāni": "bốn sức mạnh",
    "tīṇi balāni": "ba sức mạnh",
    "tivaṅgiko maggo": "con đường gồm ba chi phần",
    "duvaṅgiko maggo": "con đường gồm hai chi phần",
    "eko hetu": "một gốc rễ",
    "ekā cakkhuviññāṇadhātu": "một yếu tố thức qua mắt",
    "ekā kāyaviññāṇadhātu": "một yếu tố thức qua thân",
    "ekā manodhātu": "một yếu tố ý",
}
for _k in NEW_NAMES:
    assert _k not in B.NAMES, _k
B.NAMES.update(NEW_NAMES)
SUKHA_BODY = "sự dễ chịu"     # sukhaṃ of the body-consciousness (^1-443 … ^1-454), APPROVED decision 2
BODY_SEGS = {f"1-{i}" for i in range(443, 455)}

# =========================================================================================
# 3. Synonym strings (placed after «Điều mà vào lúc ấy là »)
# =========================================================================================


def _cut(s, tail):
    assert s.endswith(tail), (s, tail)
    return s[:-len(tail)]


def tajja(x):
    """tajjā-X-samphassaja- -> «sinh từ sự tiếp xúc của X tương ứng»"""
    return f"sinh từ sự tiếp xúc của {x} tương ứng"


assert tajja("yếu tố ý thức") == S.TAJJA
TAJJA_DH = {   # tajjā-X-dhātu: the element whose contact the feeling/perception/volition is born of
    "tajjāmanoviññāṇadhātu": "yếu tố ý thức",
    "tajjācakkhuviññāṇadhātu": "yếu tố thức qua mắt",
    "tajjākāyaviññāṇadhātu": "yếu tố thức qua thân",
    "tajjāmanodhātu": "yếu tố ý",
}
VITAKKA_P = "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā"
SAMADHI_P = ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ "
             "samādhibalaṃ")
VIRIYA_P = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti "
            "asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ "
            "vīriyabalaṃ")
VITAKKA_V = _cut(S.S_VITAKKA, ", tư duy đúng đắn")
SAMADHI_V = _cut(S.S_SAMADHI, ", định tâm đúng đắn")
VIRIYA_V = _cut(S.S_VIRIYA, ", nỗ lực đúng đắn")

DITTHI_P = ("diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ "
            "gāho patiṭṭhāho{A} abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ "
            "vipariyāsaggāho{B}")
DITTHI_V = ("quan điểm, sự mắc kẹt trong các quan điểm, rừng rậm quan điểm, hoang mạc quan điểm, "
            "sự quanh co của quan điểm, sự dao động của quan điểm, xiềng xích quan điểm, sự nắm giữ, "
            "sự bám chặt{A}, sự cố chấp, sự hiểu sai lệch, con đường lệch lạc, lối đi sai lầm, sự sai lầm, "
            "lĩnh vực của các học thuyết ngoại đạo, sự nắm giữ điều đảo ngược{B}")
DITTHI_VAR_P = {"A": " [paṭiggāho (sī. syā.)]", "B": " [vipariyesagāho (ka.)]"}
DITTHI_VAR_V = {"A": " " + S.reading("Sī., Syā.", "paṭiggāho"),     # a different word
                "B": " " + S.spell("Ka.", "vipariyesagāho")}         # spelling only
LOBHA_P = "lobho lubbhanā lubbhitattaṃ sārāgo sārajjanā sārajjitattaṃ abhijjhā lobho akusalamūlaṃ"
LOBHA_V = ("sự tham lam, sự khởi lòng tham, trạng thái khởi lòng tham, sự say đắm, sự bị cuốn hút, "
           f"trạng thái bị cuốn hút, sự thèm muốn, sự tham lam, {ROOT_AKUSALA}")
MOHA_P = ("aññāṇaṃ adassanaṃ anabhisamayo ananubodho asambodho appaṭivedho asaṃgāhanā apariyogāhanā "
          "asamapekkhanā apaccavekkhanā apaccakkhakammaṃ dummejjhaṃ bālyaṃ asampajaññaṃ moho pamoho sammoho "
          "avijjā avijjogho avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ avijjālaṅgī moho akusalamūlaṃ")
MOHA_V = ("sự không biết, sự không thấy, sự không thấu hiểu, sự không hiểu ra, sự không tỉnh ngộ, "
          "sự không thấu triệt, sự không nắm bắt, sự không đi sâu, sự không xem xét, sự không xem xét lại, "
          "sự không tự mình thấy rõ, sự ngu muội, sự khờ dại, sự thiếu hiểu biết rõ ràng, sự si mê, sự mê muội, "
          "sự mê lầm, vô minh, dòng lũ vô minh, ách vô minh, khuynh hướng tiềm ẩn vô minh, "
          f"sự ám ảnh của vô minh, then cài vô minh, sự si mê, {ROOT_AKUSALA}")
DOSA_P = ("doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo "
          "anattamanatā cittassa")
DOSA_V = ("sự sân hận, sự khởi sân, trạng thái khởi sân, sự thù hằn, sự khởi thù hằn, trạng thái khởi thù hằn, "
          "sự chống đối, sự đối nghịch, sự hung dữ, sự thô lỗ, sự không hài lòng của tâm")
VICIKICCHA_P = ("kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvedhāpatho saṃsayo anekaṃsaggāho "
                "āsappanā parisappanā apariyogāhanā thambhitattaṃ cittassa manovilekho")
VICIKICCHA_V = ("sự nghi ngờ, sự khởi nghi ngờ, trạng thái khởi nghi ngờ, sự phân vân, sự hoài nghi, sự lưỡng lự, "
                "sự đứng trước ngã ba đường, sự ngờ vực, sự không nắm giữ được điều chắc chắn, sự chần chừ, "
                "sự do dự, sự không đi sâu, trạng thái cứng đờ của tâm, sự giằng xé của ý")
UDDHACCA_P = "cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa"
UDDHACCA_V = "sự xao động của tâm, sự không lắng xuống, sự tán loạn của tâm, trạng thái rối loạn của tâm"
# painful mental feeling (parallel to S.S_SUKHA «sự khoan khoái trong tâm, sự dễ chịu trong tâm, …»)
P_DUKKHA = ("cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ "
            "cetosamphassajā asātā dukkhā vedanā")
DUK_HEAD = "sự bứt rứt trong tâm"
DUK_TAIL = ("sự khó chịu trong tâm, cảm nhận bứt rứt và khó chịu sinh từ sự tiếp xúc của tâm, "
            "cảm giác bứt rứt và khó chịu sinh từ sự tiếp xúc của tâm")
# pleasant bodily feeling (APPROVED: «dễ chịu»; kāyikaṃ = «nơi thân», kāyasamphassaja = «sinh từ sự tiếp xúc của thân»)
P_KSUKHA = ("kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ "
            "kāyasamphassajā sātā sukhā vedanā")
KSUK_HEAD = "sự khoan khoái nơi thân"
KSUK_TAIL = ("sự dễ chịu nơi thân, cảm nhận khoan khoái và dễ chịu sinh từ sự tiếp xúc của thân, "
             "cảm giác khoan khoái và dễ chịu sinh từ sự tiếp xúc của thân")
HIRI_NEG_P = "na hirīyati hiriyitabbena na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā"
OTTAPPA_NEG_P = "na ottappati ottappitabbena na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā"
HIRI_NEG_V = S.HIRI_S.replace("sự hổ thẹn", "sự không hổ thẹn")
OTTAPPA_NEG_V = S.OTTAPPA_S.replace("sự ghê sợ", "sự không ghê sợ")
assert HIRI_NEG_V.count("sự không hổ thẹn") == 2 and OTTAPPA_NEG_V.count("sự không ghê sợ") == 2

NEW_STR = {
    VITAKKA_P: VITAKKA_V,
    VITAKKA_P + " micchāsaṅkappo": VITAKKA_V + ", " + NEW_NAMES["micchāsaṅkappo"],
    SAMADHI_P + " micchāsamādhi": SAMADHI_V + ", " + NEW_NAMES["micchāsamādhi"],
    VIRIYA_P + " micchāvāyāmo": VIRIYA_V + ", " + NEW_NAMES["micchāvāyāmo"],
    "cittassa ṭhiti": "sự ổn định của tâm",       # the abbreviated concentration string
    DITTHI_P.format(A="", B=""): DITTHI_V.format(A="", B=""),
    DITTHI_P.format(**DITTHI_VAR_P): DITTHI_V.format(**DITTHI_VAR_V),
    LOBHA_P: LOBHA_V,
    MOHA_P: MOHA_V,
    DOSA_P: DOSA_V,
    VICIKICCHA_P: VICIKICCHA_V,
    UDDHACCA_P: UDDHACCA_V,
    P_DUKKHA: f"{DUK_HEAD}, {DUK_TAIL}",
    "tajjāmanoviññāṇadhātusamphassajaṃ " + P_DUKKHA: f"{DUK_HEAD} {S.TAJJA}, {DUK_TAIL}",
    P_KSUKHA: f"{KSUK_HEAD}, {KSUK_TAIL}",
    "tajjākāyaviññāṇadhātusamphassajaṃ " + P_KSUKHA:
        f"{KSUK_HEAD} {tajja(TAJJA_DH['tajjākāyaviññāṇadhātu'])}, {KSUK_TAIL}",
    HIRI_NEG_P: HIRI_NEG_V,
    OTTAPPA_NEG_P: OTTAPPA_NEG_V,
}
# the «tajjā-X-dhātu» strings of the other elements (feeling of equanimity, perception, volition, mind)
CITTA_HEAD_P = ("cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho ")
assert S.S_CITTA.endswith(", yếu tố ý thức tương ứng")
for _p, _x in TAJJA_DH.items():
    if _p == "tajjāmanoviññāṇadhātu":
        continue                                   # already in B.STR / T.NEW_BASES
    NEW_STR[f"{_p}samphassajaṃ {B.P_UPEKKHA}"] = f"{B.UPE_HEAD} {tajja(_x)}, {B.UPE_TAIL}"
    NEW_STR[f"{_p}samphassajā saññā sañjānanā sañjānitattaṃ"] = S.S_SANNA.replace(S.TAJJA, tajja(_x))
    NEW_STR[f"{_p}samphassajā cetanā sañcetanā cetayitattaṃ"] = T.S_CETANA_TAJJA.replace(S.TAJJA, tajja(_x))
    NEW_STR[CITTA_HEAD_P + _p] = _cut(S.S_CITTA, "yếu tố ý thức tương ứng") + f"{_x} tương ứng"
for _k in NEW_STR:
    assert _k not in B.STR, _k
B.STR.update(NEW_STR)

# =========================================================================================
# 4. Tails: the akusalā / abyākatā closings, wrapped around B.tail_vi
# =========================================================================================
TAIL_REPL = [
    ("alobho abyākatamūlaṃ", f"{S.FN['alobho']}, {ROOT_ABY}"),
    ("adoso abyākatamūlaṃ", f"{S.FN['adoso']}, {ROOT_ABY}"),
    ("ime dhammā akusalā", A_AKUSALA),
    ("ime dhammā abyākatā", A_ABY),
]
_TAIL_ORIG = B.tail_vi


def tail_vi(t):
    for p, v in TAIL_REPL:
        t = t.replace(p, v)
    return _TAIL_ORIG(t)


B.tail_vi = tail_vi          # B's answer_vi / summary_vi / qa_vi and T's ann_vi now see the wrapper

# =========================================================================================
# 5. «Katame dhammā akusalā / abyākatā? Yasmiṃ samaye …» sentences
# =========================================================================================
# attributes after the opening (a copy of B.ATTR, never mutated)
NEW_ATTR = {
    "diṭṭhigatasampayuttaṃ": "gắn liền với sự mắc kẹt trong các quan điểm",
    "diṭṭhigatavippayuttaṃ": "không gắn liền với sự mắc kẹt trong các quan điểm",
    "domanassasahagataṃ": "có nỗi buồn đi kèm",
    "paṭighasampayuttaṃ": "gắn liền với sự ác cảm",
    "vicikicchāsampayuttaṃ": "gắn liền với sự hoài nghi",
    "uddhaccasampayuttaṃ": "gắn liền với sự xao động",
    "yaṃ yaṃ vā panārabbha": "hoặc lấy bất cứ thứ gì làm đối tượng",
    # the resultant minds (neuter viññāṇaṃ / feminine dhātu: the same Vietnamese)
    "rūpārammaṇaṃ": "có đối tượng là hình sắc",
    "saddārammaṇaṃ": "có đối tượng là âm thanh",
    "gandhārammaṇaṃ": "có đối tượng là mùi",
    "rasārammaṇaṃ": "có đối tượng là vị",
    "phoṭṭhabbārammaṇaṃ": "có đối tượng là vật xúc chạm",
    "sukhasahagataṃ": f"có {SUKHA_BODY} đi kèm",          # body-consciousness only (APPROVED decision 2)
    "ghānaviññāṇaṃ uppannaṃ hoti": "thức qua mũi sinh khởi",
    "jivhāviññāṇaṃ uppannaṃ hoti": "thức qua lưỡi sinh khởi",
    "kāyaviññāṇaṃ uppannaṃ hoti": "thức qua thân sinh khởi",
    "upekkhāsahagatā": B.ATTR["upekkhāsahagataṃ"],
    "somanassasahagatā": B.ATTR["somanassasahagataṃ"],
    "ñāṇasampayuttā": B.ATTR["ñāṇasampayuttaṃ"],
    "ñāṇavippayuttā": B.ATTR["ñāṇavippayuttaṃ"],
    "rūpārammaṇā vā": B.ATTR["rūpārammaṇaṃ vā"],
    "dhammārammaṇā vā yaṃ yaṃ vā panārabbha": B.ATTR["dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"],
    "phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha": "hay vật xúc chạm, hoặc lấy bất cứ thứ gì làm đối tượng",
}
for _k in NEW_ATTR:
    assert _k not in B.ATTR, _k
ATTR = dict(B.ATTR)
ATTR.update(NEW_ATTR)
assert B.OBJ_FULL_V.split(", ")[4] == "hay vật xúc chạm"

KAMMA_P = "kāmāvacarassa kusalassa kammassa katattā upacitattā "
VIP_KAMA = "là quả của nghiệp thiện thuộc cõi dục lạc đã được tạo và tích lũy"   # (…) kammassa katattā upacitattā vipāka-
VIP_SUBJ = {   # resultant subject (Pāli between the kamma phrase and «uppannaṃ/uppannā hoti»)
    "vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti": "thức qua mắt",
    "vipākaṃ sotaviññāṇaṃ uppannaṃ hoti": "thức qua tai",
    "vipākā manodhātu uppannā hoti": "yếu tố ý",
    "vipākā manoviññāṇadhātu uppannā hoti": "yếu tố ý thức",
}
INTROS = {   # Pāli opening (after «Yasmiṃ samaye ») -> (Vietnamese opening, table of the pieces that follow)
    "akusalaṃ cittaṃ uppannaṃ hoti ": ("Vào lúc tâm bất thiện sinh khởi, ", ATTR),
}
for _p, _v in VIP_SUBJ.items():
    INTROS[f"{KAMMA_P}{_p} "] = (f"Vào lúc {_v} sinh khởi, {VIP_KAMA}, ", ATTR)
for _p, _v in B.INTROS.items():
    INTROS[_p] = (_v, B.PIECES)
WHO_RES = "khi một người"
SPHERE = {"rūpāvacarassa": "thuộc cõi hình sắc", "arūpāvacarassa": "thuộc cõi không hình sắc"}
TASSEVA = {}  # Tasseva X kusalassa kammassa katattā upacitattā vipākaṃ <jhāna> -> «Là quả của chính nghiệp thiện …»
for _p, _v in SPHERE.items():
    TASSEVA[f"Tasseva {_p} kusalassa kammassa katattā upacitattā vipākaṃ "] = (
        f"Là quả của chính nghiệp thiện {_v} ấy đã được tạo và tích lũy, {WHO_RES} ", B.PIECES)
INTROS.update(TASSEVA)


def clause(s):
    """one «Yasmiṃ samaye …» or «Tasseva …» clause up to its closing"""
    for p, (intro, table) in sorted(INTROS.items(), key=lambda kv: -len(kv[0])):
        if s.startswith(p):
            s = s[len(p):]
            break
    else:
        raise KeyError("intro: " + s[:80])
    idx = s.index(" tasmiṃ samaye ")
    x, rest = s[:idx].rstrip(), s[idx + len(" tasmiṃ samaye "):]
    if x.endswith(DASH):
        sep, x = " " + DASH, x[:-1].rstrip()
    else:
        assert x.endswith(","), x[-40:]
        sep, x = ",", x[:-1]
    m = re.fullmatch(r"(.*? hoti)\s*(…pe…\s*ime dhammā (?:kusalā|akusalā|abyākatā).*|; ye vā pana.*)", rest)
    return (intro + B.chunks(x, table) + sep + f" thì {TS} " + B.there_list(m.group(1))
            + B.tail_vi(m.group(2)))


OPEN_RE = re.compile(r"Katame dhammā (akusalā|abyākatā)\? Yasmiṃ samaye (.+)$")


def open_vi(line):
    kind, body = OPEN_RE.fullmatch(line).groups()
    parts = body.split(" Tasseva ")
    assert len(parts) <= 2
    out = Q[kind] + " " + clause(parts[0])
    if len(parts) == 2:
        assert parts[0].endswith("ime dhammā kusalā."), parts[0][-40:]
        out += " " + clause("Tasseva " + parts[1])
    return out


# ^1-473: «Katamā tasmiṃ samaye cetanā hoti. Yā …» (a full stop for the question mark, kept as written)
DOT_Q_RE = re.compile(r"Katam(?:o|ā|aṃ) tasmiṃ samaye (\S+) hoti\. (.+)$")


def dot_q_vi(m):
    return B.q_vi(m.group(1), "hoti") + ". " + B.answer_vi(m.group(2))


# =========================================================================================
# 6. Headings and closing lines
# =========================================================================================
VIP_K = "là quả của nghiệp thiện"                  # Kusalavipāka-
H = {
    "#### Dvādasa akusalāni": "#### Mười hai tâm bất thiện",
    "Dvādasa akusalacittāni.": "Mười hai loại tâm bất thiện.",
    "#### Abyākatavipāko": f"#### Quả của nghiệp {ABY}",           # termbase heading entry
    "##### Kusalavipākapañcaviññāṇāni": f"##### Năm loại thức {VIP_K}",
    "Kusalavipākāni pañcaviññāṇāni.": f"Năm loại thức {VIP_K}.",
    "##### Kusalavipākamanodhātu": f"##### Yếu tố ý {VIP_K}",
    "Kusalavipākā manodhātu.": f"Yếu tố ý {VIP_K}.",
    "##### Kusalavipākamanoviññāṇadhātusomanassasahagatā":
        f"##### Yếu tố ý thức {VIP_K}, {B.ATTR['somanassasahagataṃ']}",
    "Kusalavipākā manoviññāṇadhātu somanassasahagatā.": f"Yếu tố ý thức {VIP_K}, {B.ATTR['somanassasahagataṃ']}.",
    "##### Kusalavipākamanoviññāṇadhātuupekkhāsahagatā":
        f"##### Yếu tố ý thức {VIP_K}, {B.ATTR['upekkhāsahagataṃ']}",
    "Kusalavipākā upekkhāsahagatā manoviññāṇadhātu.": f"Yếu tố ý thức {VIP_K}, {B.ATTR['upekkhāsahagataṃ']}.",
    "##### Aṭṭhamahāvipākā": "##### Tám quả nghiệp lớn",
    "Aṭṭhamahāvipākā.": "Tám quả nghiệp lớn.",
    "##### Rūpāvacaravipākā": f"##### Quả của nghiệp {SPHERE['rūpāvacarassa']}",
    "Rūpāvacaravipākā.": f"Quả của nghiệp {SPHERE['rūpāvacarassa']}.",
    "##### Arūpāvacaravipākā": f"##### Quả của nghiệp {SPHERE['arūpāvacarassa']}",
    "Arūpāvacaravipākā.": f"Quả của nghiệp {SPHERE['arūpāvacarassa']}.",
}
for _k in H:
    assert _k not in B.EXACT, _k


# =========================================================================================
# 7. Line dispatch, render, build
# =========================================================================================
def translate_line(line):
    if line in H:
        return H[line]
    if OPEN_RE.fullmatch(line):
        return open_vi(line)
    m = DOT_Q_RE.fullmatch(line)
    if m:
        return dot_q_vi(m)
    return T.translate_line(line)


def render(segs):
    blocks = []
    for sid, plines in segs:
        vlines = []
        saved = B.NAMES["sukhaṃ"]
        if sid in BODY_SEGS:
            B.NAMES["sukhaṃ"] = SUKHA_BODY
        try:
            for p in plines:
                v = unicodedata.normalize("NFC", cap(translate_line(p)))
                B.check_vi(v)
                assert len(p) - len(p.lstrip("#")) == len(v) - len(v.lstrip("#")), sid
                assert p.count("–") + p.count("—") == v.count("–"), ("dash", sid, p[:60], v[:60])
                assert p.count("…pe…") <= v.count("…"), ("pe", sid)
                assert p.endswith("?") == v.endswith("?"), ("question", sid)
                assert p.endswith(PE + ".") or p.endswith(".") == v.endswith("."), ("stop", sid)
                assert "  " not in v and " ," not in v and ",," not in v and "..." not in v, ("spacing", sid, v)
                assert "hạnh phúc" not in v or sid not in BODY_SEGS, ("sukha body", sid)
                vlines.append(v)
        finally:
            B.NAMES["sukhaṃ"] = saved
        vlines[-1] += f" ^{sid}"
        blocks.append("\n".join(vlines))
    return blocks


def check_earlier_unchanged():
    """The extended tables and the tail wrapper must leave 2-01, 2-02 and 2-03 exactly as finished."""
    for fn_name, fn in (("2-01-cittuppadakandam.md", B.build_2_01), ("2-02-cittuppadakandam.md", B.build_2_02),
                        ("2-03-cittuppadakandam.md", T.build)):
        text, _ = fn()
        assert unicodedata.normalize("NFC", text) == (S.OUT / fn_name).read_bytes().decode("utf-8"), fn_name
    print("2-01, 2-02, 2-03: rebuilt in memory with the 2-04 tables, byte-identical to the finished files")


def build():
    segs = B.segments(PALI)
    return "\n\n".join(render(segs)) + "\n", len(segs)


def notes():
    L = ["# pi-1 Vietnamese rails: new formulas of 2-04", "",
         "Generated by build_rails_2-04_vi.py from its fixed strings; import that file instead of retyping. "
         "Strings already in vi-rails-formulas.md, notes-2-01_2-02.md or notes-2-03.md are not repeated. "
         "Format: Pāli = tiếng Việt.", "",
         "## Frames", "",
         f"Katame dhammā akusalā? = {Q_AKUSALA}",
         f"Katame dhammā abyākatā? = {Q_ABY}",
         f"ime dhammā akusalā = {A_AKUSALA}",
         f"ime dhammā abyākatā = {A_ABY}",
         f"X akusalamūlaṃ (end of the lobha / moha strings) = X, {ROOT_AKUSALA}",
         f"…pe… alobho abyākatamūlaṃ…pe… adoso abyākatamūlaṃ…pe… = … {TAIL_REPL[0][1]}… {TAIL_REPL[1][1]}…",
         "Yasmiṃ samaye akusalaṃ cittaṃ uppannaṃ hoti A, tasmiṃ samaye … = "
         f"{INTROS['akusalaṃ cittaṃ uppannaṃ hoti '][0]}A, thì {TS} …",
         f"Yasmiṃ samaye {KAMMA_P}vipākaṃ/vipākā X uppannaṃ/uppannā hoti A, tasmiṃ samaye … = "
         f"Vào lúc X sinh khởi, {VIP_KAMA}, A, thì {TS} …",
         f"{KAMMA_P}vipāka- = {VIP_KAMA}"]
    for p, (v, _) in TASSEVA.items():
        L.append(f"… ime dhammā kusalā. {p.strip()} J, tasmiṃ samaye … = … {A_KUSALA_K}. {v}J, thì {TS} …")
    L += [f"Katamā tasmiṃ samaye cetanā hoti. Yā … (^1-473, «.» as written) = {B.q_vi('cetanā', 'hoti')}. Điều mà …",
          "«X hoti …pe…» with a space (^1-429, ^1-498): the space before «…pe…» is dropped, as in 2-01",
          f"sukhaṃ of the body-consciousness (^1-443 … ^1-454, defined as kāyikaṃ sukhaṃ) = {SUKHA_BODY} "
          "(APPROVED decision 2); elsewhere sukhaṃ as factor stays «hạnh phúc»",
          "", "### Attributes and pieces of the openings", ""]
    for p, v in NEW_ATTR.items():
        L.append(f"{p} = {v}")
    for p, v in VIP_SUBJ.items():
        L.append(f"{p} = {v} sinh khởi ({VIP_KAMA} follows after a comma)")
    L += ["", "## Synonym strings", ""]
    for p, v in NEW_STR.items():
        L.append(f"{p} = {v}")
    L += ["", "## Names", ""]
    for p, v in NEW_NAMES.items():
        L.append(f"{p} = {v}")
    L.append(f"sukhaṃ (body-consciousness ^1-443 … ^1-454 only) = {SUKHA_BODY}")
    L += ["", "## Headings and closing lines", ""]
    for p, v in H.items():
        L.append(f"{p} = {v}")
    (HERE / "notes-2-04.md").write_text(unicodedata.normalize("NFC", "\n".join(L) + "\n"), encoding="utf-8",
                                        newline="\n")
    print("wrote", HERE / "notes-2-04.md")


A_KUSALA_K = S.A_KUSALA[:-1]


def main():
    text, n = build()
    check_earlier_unchanged()
    OUT.write_text(unicodedata.normalize("NFC", text), encoding="utf-8", newline="\n")
    print("wrote", OUT, n, "segments")
    notes()


if __name__ == "__main__":
    main()
