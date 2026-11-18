"""Build the Vietnamese plain zero-shot of pi-1 part 2-04 (twelve unwholesome minds; results of the wholesome,
^1-1-6-0 … ^1-504).

usage: python -I -X utf8 build_2-04_vi.py      (checks, then writes the part)

Importing this file does NOT build anything.
Method: the approved builders are imported unchanged (build_matika_vi = M, build_ch2_01_sample_vi = C,
build_2-01_2-02_vi = B, build_2-03_vi = D). This part only ADDS entries to B's / D's formula tables (in memory;
an existing entry is never changed) plus the opening-sentence frames of unwholesome minds and of results.
Every Q/A line, list, summary and koṭṭhāsa line goes through B's own translators, and the wholesome half of
^1-499 … ^1-504 through B.kusala_vi, so every formula shared with the earlier parts stays byte-identical.
A cross-check compares every Pāli line that also occurs in 2-01 / 2-02 / 2-03 with the Vietnamese already
published for it.

Reusable pieces: NEW_NAMES, NEW_COUNTED, NEW_STR, NEW_TOKENS, NEW_PH, TAJJA_OF(), RESULT_KAMA, TASSEVA(),
AKUSALA_V, ABYAKATA_V, ABY_ROOT, open_vi(), rest_vi(), sphere_vi(), translate_line().
"""
import importlib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_matika_vi as M  # noqa: E402  (importing does not write)
import build_ch2_01_sample_vi as C  # noqa: E402  (importing does not write)
B = importlib.import_module("build_2-01_2-02_vi")  # importing does not write
D = importlib.import_module("build_2-03_vi")       # importing does not write (adds 2-03 entries to B)

PART = "2-04-cittuppadakandam.md"
PALI_DIR, OUT_DIR = B.PALI_DIR, B.OUT_DIR
DASH, PE, ELL, TASMIM = B.DASH, B.PE, B.ELL, B.TASMIM
add = D.add   # add entries to a table; never overwrite an existing entry

# =========================================================================================
# 1. Answers «ime dhammā akusalā / abyākatā» (matrix triad 1 (b) / (c))
# =========================================================================================
AKUSALA_V = M.ANSWER_BARE(C.AKUSALA)    # đây là các hiện tượng bất thiện
ABYAKATA_V = M.ANSWER_BARE(C.ABYAKATA)  # đây là các hiện tượng không xác định về mặt đạo đức
assert AKUSALA_V == "đây là các hiện tượng bất thiện"
assert ABYAKATA_V == "đây là các hiện tượng không xác định về mặt đạo đức"
KIND = {"kusalā": C.KUSALA, "akusalā": C.AKUSALA, "abyākatā": C.ABYAKATA}


def presub(s):
    """'ime dhammā akusalā / abyākatā' -> Vietnamese (B.tail_vi knows only 'ime dhammā kusalā')"""
    return s.replace("ime dhammā akusalā", AKUSALA_V).replace("ime dhammā abyākatā", ABYAKATA_V)


# =========================================================================================
# 2. Names
# =========================================================================================
WRONG = "sai lầm"   # micchā- (micchatta = sai lầm, matrix triad 15; micchāsati = tỉnh thức sai lầm)
AHIRIKA = M.BARE[("1-M2-115", "a")]     # sự không biết hổ thẹn
ANOTTAPPA = M.BARE[("1-M2-115", "b")]   # sự không biết ghê sợ tội lỗi
assert (AHIRIKA, ANOTTAPPA) == ("sự không biết hổ thẹn", "sự không biết ghê sợ tội lỗi")
EYE, EAR, NOSE, TONGUE, BODY = "thức qua mắt", "thức qua tai", "thức qua mũi", "thức qua lưỡi", "thức qua thân"
NEW_NAMES = {
    "micchādiṭṭhi": f"quan điểm {WRONG}",
    "micchāsaṅkappo": f"tư duy {WRONG}",
    "micchāvāyāmo": f"nỗ lực {WRONG}",
    "micchāsamādhi": f"định tâm {WRONG}",
    "ahirikabalaṃ": "sức mạnh không biết hổ thẹn",              # as hiribalaṃ = sức mạnh biết hổ thẹn
    "anottappabalaṃ": "sức mạnh không biết ghê sợ tội lỗi",     # as ottappabalaṃ
    "ahirikaṃ": AHIRIKA,
    "anottappaṃ": ANOTTAPPA,
    "lobho": "sự tham lam",
    "doso": "sự sân hận",
    "moho": "sự si mê",
    "abhijjhā": "sự thèm muốn",      # anabhijjhā = sự không thèm muốn
    "byāpādo": "sự ác ý",            # abyāpādo = sự không ác ý
    "vicikicchā": "sự hoài nghi",    # kept apart from kaṅkhā = sự nghi ngờ
    "uddhaccaṃ": "sự xao động",      # as 2-03 (uddhacca)
    "dukkhaṃ": "sự đau khổ",         # the factor (sukhaṃ = hạnh phúc); the feeling quality is «khó chịu»
    "domanassindriyaṃ": "năng lực nỗi buồn",   # somanassindriyaṃ = năng lực niềm vui
    "sukhindriyaṃ": "năng lực dễ chịu",        # sukha as a quality of feeling = dễ chịu (core terms)
    "cakkhuviññāṇadhātu": "yếu tố " + EYE,
    "kāyaviññāṇadhātu": "yếu tố " + BODY,
    "manodhātu": "yếu tố ý",                   # core terms: manodhātu = yếu tố ý
}
for k in NEW_NAMES:
    assert k not in B.NAME, k
add(B.NAME, NEW_NAMES)
assert B.NAME["upekkhā"] == "sự bình thản" and B.NAME["upekkhindriyaṃ"] == "năng lực bình thản"
assert B.NAME["saṅkhārakkhandho"] == "khối tạo tác" and B.NAME["manoviññāṇadhātu"] == "yếu tố ý thức"

NEW_COUNTED = {
    "pañcindriyāni": "năm năng lực",
    "cattāri indriyāni": "bốn năng lực",
    "tīṇindriyāni": "ba năng lực",
    "tivaṅgiko maggo": "con đường gồm ba chi phần",
    "duvaṅgiko maggo": "con đường gồm hai chi phần",
    "cattāri balāni": "bốn sức mạnh",
    "tīṇi balāni": "ba sức mạnh",
    "eko hetu": "một gốc rễ",
}
add(B.COUNTED, NEW_COUNTED)
assert B.COUNTED["caturaṅgiko maggo"] == "con đường gồm bốn chi phần"

# =========================================================================================
# 3. Synonym strings
# =========================================================================================
UNROOT = "gốc rễ bất thiện"                               # akusalamūlaṃ (kusalamūlaṃ = gốc rễ thiện)
ABY_ROOT = "gốc rễ không xác định về mặt đạo đức"         # abyākatamūlaṃ
assert C.ROOT == "gốc rễ thiện"


def strip_end(s, tail):
    assert s.endswith(tail), (s[-60:], tail)
    return s[:-len(tail)]


# the sample strings without their closing path factor (the bases the micchā- tokens attach to)
VIT_P = "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā"
SAM_P = ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho "
         "samādhindriyaṃ samādhibalaṃ")
VIR_P = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti "
         "asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ "
         "vīriyindriyaṃ vīriyabalaṃ")
assert VIT_P + " sammāsaṅkappo" in B.STR and SAM_P + " sammāsamādhi" in B.STR and VIR_P + " sammāvāyāmo" in B.STR
VIT_V = strip_end(C.S_VITAKKA, ", " + C.N["sammāsaṅkappo"])
SAM_V = strip_end(C.S_SAMADHI, ", " + C.N["sammāsamādhi"])
VIR_V = strip_end(C.S_VIRIYA, ", " + C.N["sammāvāyāmo"])
THITI_V = C.WL["cittassa"][0]   # cittassa ṭhiti = sự ổn định của tâm (first item of the samādhi string)
assert THITI_V == "sự ổn định của tâm"

# the feeling strings (pattern of the sample's sāta string)
S_DUKKHA = ("sự bứt rứt trong tâm, sự khó chịu trong tâm, "
            "cảm nhận bứt rứt và khó chịu sinh từ sự tiếp xúc của tâm, "
            "cảm giác bứt rứt và khó chịu sinh từ sự tiếp xúc của tâm")
S_KAYASUKHA = ("sự khoan khoái nơi thân, sự dễ chịu nơi thân, "
               "cảm nhận khoan khoái và dễ chịu sinh từ sự tiếp xúc của thân, "
               "cảm giác khoan khoái và dễ chịu sinh từ sự tiếp xúc của thân")
assert C.S_SUKHA == S_KAYASUKHA.replace("nơi thân", "trong tâm").replace("tiếp xúc của thân", "tiếp xúc của tâm")
assert C.S_SUKHA == (S_DUKKHA.replace("bứt rứt", "khoan khoái").replace("khó chịu", "dễ chịu"))

# lobha: the sample's alobha string turned positive
W_LOBHA = ["sự tham lam", "sự khởi lòng tham", "trạng thái khởi lòng tham", "sự say đắm", "sự bị cuốn hút",
           "trạng thái bị cuốn hút", "sự thèm muốn", "sự tham lam", UNROOT]
assert C.WL["alobho"][:8] == [w.replace("sự ", "sự không ", 1).replace("trạng thái ", "trạng thái không ", 1)
                              for w in W_LOBHA[:8]]
# dosa: the pattern of the sample's adosa string
W_DOSA = ["sự sân hận", "sự khởi sân", "trạng thái khởi sân", "sự thù hằn", "sự khởi thù hằn",
          "trạng thái khởi thù hằn", "sự chống đối", "sự đối nghịch", "sự hung dữ", "sự thô lỗ",
          "sự không hài lòng của tâm"]
assert C.WL["adoso"][:3] == ["sự không sân hận", "sự không khởi sân", "trạng thái không khởi sân"]
assert C.WL["pīti"][-1] == "sự hài lòng của tâm"      # attamanatā cittassa
# moha
W_MOHA = ["sự không biết", "sự không thấy", "sự không thấu hiểu", "sự không hiểu ra", "sự không tỉnh ngộ",
          "sự không thấu triệt", "sự không nắm bắt", "sự không đi sâu", "sự không xem xét",
          "sự không xem xét lại", "sự không tự mình thấy rõ", "sự ngu muội", "sự khờ dại",
          M.BARE[("1-M2-129", "b")],                                  # asampajaññaṃ = sự thiếu hiểu biết rõ ràng
          "sự si mê", "sự mê muội", "sự mê lầm", "vô minh", "dòng lũ vô minh", "ách vô minh",
          "khuynh hướng tiềm ẩn của vô minh", "sự ám ảnh của vô minh", "then cài của vô minh",
          "sự si mê", UNROOT]
assert W_MOHA[13] == "sự thiếu hiểu biết rõ ràng" and M.BARE[("1-M2-110", "a")] == "vô minh"
# diṭṭhi (diṭṭhigata = sự mắc kẹt trong các quan điểm, as 2-03; parāmāsa = sự hiểu sai lệch, core terms)
W_DITTHI = ["quan điểm", "sự mắc kẹt trong các quan điểm", "rừng rậm quan điểm", "hoang mạc quan điểm",
            "sự quanh co của quan điểm", "sự dao động của quan điểm", "xiềng xích quan điểm", "sự nắm giữ",
            "sự bám chặt", "sự cố chấp", "sự hiểu sai lệch", "con đường lệch lạc", f"lối đi {WRONG}",
            f"sự {WRONG}", "nền tảng của các học thuyết ngoại đạo", "sự nắm giữ điều đảo ngược"]
# vicikicchā (kaṅkhā = sự nghi ngờ, vicikicchā = sự hoài nghi, kept apart)
W_VICIKICCHA = ["sự nghi ngờ", "sự khởi nghi ngờ", "trạng thái khởi nghi ngờ", "sự phân vân", "sự hoài nghi",
                "sự lưỡng lự", "sự đứng trước ngã ba đường", "sự ngờ vực",
                "sự không nắm giữ được điều chắc chắn", "sự chần chừ", "sự do dự", "sự không đi sâu",
                "trạng thái cứng đờ của tâm", "sự giằng xé trong ý"]
assert W_VICIKICCHA[11] == W_MOHA[7]   # apariyogāhanā in both strings
# uddhacca (vūpasama = lắng xuống, as 2-02; avikkhepo = sự không tán loạn)
W_UDDHACCA = ["sự xao động của tâm", "sự không lắng xuống", "sự tán loạn của tâm", "trạng thái rối loạn của tâm"]
# ahirika / anottappa: the sample's hirī / ottappa clauses negated
S_AHIRIKA = C.S_HIRI.replace("người ta hổ thẹn", "người ta không hổ thẹn", 1).replace(
    ", hổ thẹn khi", ", không hổ thẹn khi", 1)
S_ANOTTAPPA = C.S_OTTAPPA.replace("người ta ghê sợ", "người ta không ghê sợ", 1).replace(
    ", ghê sợ khi", ", không ghê sợ khi", 1)
assert S_AHIRIKA.count("không hổ thẹn") == 2 and S_ANOTTAPPA.count("không ghê sợ") == 2

LOBHA_P = "lobho lubbhanā lubbhitattaṃ sārāgo sārajjanā sārajjitattaṃ abhijjhā lobho akusalamūlaṃ"
DOSA_P = ("doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo "
          "anattamanatā cittassa")
MOHA_P = ("aññāṇaṃ adassanaṃ anabhisamayo ananubodho asambodho appaṭivedho asaṃgāhanā apariyogāhanā "
          "asamapekkhanā apaccavekkhanā apaccakkhakammaṃ dummejjhaṃ bālyaṃ asampajaññaṃ moho pamoho sammoho "
          "avijjā avijjogho avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ avijjālaṅgī moho akusalamūlaṃ")
DITTHI_P = ("diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ "
            "diṭṭhisaṃyojanaṃ gāho patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ "
            "titthāyatanaṃ vipariyāsaggāho")
DITTHI_PV = DITTHI_P.replace("patiṭṭhāho", "patiṭṭhāho [paṭiggāho (sī. syā.)]").replace(
    "vipariyāsaggāho", "vipariyāsaggāho [vipariyesagāho (ka.)]")
VICI_P = ("kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvedhāpatho saṃsayo anekaṃsaggāho "
          "āsappanā parisappanā apariyogāhanā thambhitattaṃ cittassa manovilekho")
UDDH_P = "cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa"
# word counts (phrase units: «thambhitattaṃ cittassa», «cittassa uddhaccaṃ», «cetaso vikkhepo»,
# «bhantattaṃ cittassa», «anattamanatā cittassa»)
for p, w, units in ((LOBHA_P, W_LOBHA, 0), (DOSA_P, W_DOSA, 1), (MOHA_P, W_MOHA, 0), (DITTHI_P, W_DITTHI, 0),
                    (VICI_P, W_VICIKICCHA, 1), (UDDH_P, W_UDDHACCA, 3)):
    assert len(p.split()) - units == len(w), (p[:30], len(p.split()), len(w))
DITTHI_WV = list(W_DITTHI)
DITTHI_WV[8] += M.V("p", "Sī., Syā.", "paṭiggāho")        # a different word
DITTHI_WV[15] += M.V("s", "Ka.", "vipariyesagāho")       # spelling only
assert B.var_vi("[vipariyesagāho (ka.)]") == M.V("s", "Ka.", "vipariyesagāho").strip()

_CITTA_P = "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho"
_CITTA_V = strip_end(C.S_CITTA, ", yếu tố ý thức tương ứng")
CORR = "tương ứng"   # tajjā-
NEW_STR = {
    VIT_P: VIT_V,
    SAM_P: SAM_V,
    VIR_P: VIR_V,
    "cittassa ṭhiti": THITI_V,
    "cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā "
    "vedanā": S_DUKKHA,
    "kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā":
        S_KAYASUKHA,
    LOBHA_P: ", ".join(W_LOBHA),
    DOSA_P: ", ".join(W_DOSA),
    MOHA_P: ", ".join(W_MOHA),
    DITTHI_P: ", ".join(W_DITTHI),
    DITTHI_PV: ", ".join(DITTHI_WV),
    VICI_P: ", ".join(W_VICIKICCHA),
    UDDH_P: ", ".join(W_UDDHACCA),
    "na hirīyati hiriyitabbena na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": S_AHIRIKA,
    "na ottappati ottappitabbena na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": S_ANOTTAPPA,
    _CITTA_P + " tajjācakkhuviññāṇadhātu": f"{_CITTA_V}, yếu tố {EYE} {CORR}",
    _CITTA_P + " tajjākāyaviññāṇadhātu": f"{_CITTA_V}, yếu tố {BODY} {CORR}",
    _CITTA_P + " tajjāmanodhātu": f"{_CITTA_V}, yếu tố ý {CORR}",
}
add(B.STR, NEW_STR)
assert C.S_CITTA == f"{_CITTA_V}, yếu tố ý thức {CORR}"
SHAME_P = ("na hirīyati", "na ottappati")

# suffix tokens for D.compose (base string + «, <token>»)
NEW_TOKENS = {
    "micchāsaṅkappo": NEW_NAMES["micchāsaṅkappo"],
    "micchāsamādhi": NEW_NAMES["micchāsamādhi"],
    "micchāvāyāmo": NEW_NAMES["micchāvāyāmo"],
}
add(D.TOKENS, NEW_TOKENS)
assert D.compose(VIT_P + " sammāsaṅkappo") == C.S_VITAKKA   # the longest base wins


# qualifiers between «Điều có mặt vào lúc ấy» and «, tức là» (the sample's TAJJA pattern)
def TAJJA_OF(element):
    return f"sinh từ sự tiếp xúc của {element} {CORR}"


assert TAJJA_OF("yếu tố ý thức") == C.TAJJA
for el_p, el_v in (("cakkhuviññāṇadhātu", "yếu tố " + EYE), ("kāyaviññāṇadhātu", "yếu tố " + BODY),
                   ("manodhātu", "yếu tố ý")):
    for end in ("aṃ", "ā"):
        B.STR_PREFIX.append((f"tajjā{el_p}samphassaj{end} ", " và " + TAJJA_OF(el_v)))

# =========================================================================================
# 4. Phrases of the opening sentences (B.PH, joined with «, » by B.chunk_vi)
# =========================================================================================
ACC = {   # -sahagata (matrix triad 7: «có X đi kèm»)
    "somanassa": "có niềm vui đi kèm",
    "upekkhā": M.PRED[("1-M1-7", "c")],
    "domanassa": "có nỗi buồn đi kèm",           # domanassa = nỗi buồn (2-02)
    "sukha": M.PRED[("1-M1-7", "b")],             # có hạnh phúc đi kèm
}
assert ACC["upekkhā"] == "có sự bình thản đi kèm" and ACC["sukha"] == "có hạnh phúc đi kèm"
assert C.ACC_SOMA_NANA.startswith(ACC["somanassa"] + ", ")
ASSOC = "gắn liền với"   # -sampayutta (matrix: «gắn liền với»)
DITTHIGATA = W_DITTHI[1]  # sự mắc kẹt trong các quan điểm
NANA = B.NANA             # gắn liền với hiểu biết
OBJ = {"rūpa": "hình sắc", "sadda": "âm thanh", "gandha": "mùi", "rasa": "vị", "phoṭṭhabba": "vật xúc chạm",
       "dhamma": "đối tượng của ý"}
assert C.ARAMMANA == ("lấy " + ", hoặc ".join(OBJ.values()) + ", hay bất cứ thứ gì làm đối tượng")
ANY = "hay bất cứ thứ gì làm đối tượng"   # yaṃ yaṃ vā panārabbha
NEW_PH = {
    "somanassasahagataṃ": ACC["somanassa"],
    "domanassasahagataṃ": ACC["domanassa"],
    "sukhasahagataṃ": ACC["sukha"],
    "upekkhāsahagatā": ACC["upekkhā"],
    "somanassasahagatā": ACC["somanassa"],
    "diṭṭhigatasampayuttaṃ": f"{ASSOC} {DITTHIGATA}",
    "diṭṭhigatavippayuttaṃ": f"không {ASSOC} {DITTHIGATA}",
    "paṭighasampayuttaṃ": f"{ASSOC} sự ác cảm",        # paṭigha (mental) = sự ác cảm
    "vicikicchāsampayuttaṃ": f"{ASSOC} {NEW_NAMES['vicikicchā']}",
    "uddhaccasampayuttaṃ": f"{ASSOC} {NEW_NAMES['uddhaccaṃ']}",
    "ñāṇasampayuttā": NANA,
    "ñāṇavippayuttā": f"không {NANA}",
    "rūpārammaṇā vā": B.PH["rūpārammaṇaṃ vā"],                       # lấy hình sắc
    "dhammārammaṇā vā yaṃ yaṃ vā panārabbha": B.PH["dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"],
    "phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha": f"hoặc {OBJ['phoṭṭhabba']}, {ANY}",
    "yaṃ yaṃ vā panārabbha": ANY,
    "ghānaviññāṇaṃ uppannaṃ hoti": f"{NOSE} sinh khởi",
    "jivhāviññāṇaṃ uppannaṃ hoti": f"{TONGUE} sinh khởi",
    "kāyaviññāṇaṃ uppannaṃ hoti": f"{BODY} sinh khởi",
}
for k, o in OBJ.items():
    if k != "dhamma":
        NEW_PH[f"{k[:-1]}ārammaṇaṃ"] = f"lấy {o} làm đối tượng"   # one object only (cf. matrix triad 16 «lấy … làm …»)
add(B.PH, NEW_PH)
assert B.PH["dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"] == f"hoặc {OBJ['dhamma']}, {ANY}"
B.PH_MAX = max(B.PH_MAX, max(len(k.split()) for k in NEW_PH))
# the eight-fold qualifiers in feminine form read as the neuter ones of 2-01
assert B.chunk_vi("somanassasahagatā ñāṇasampayuttā") == C.ACC_SOMA_NANA
assert B.chunk_vi("upekkhāsahagatā ñāṇavippayuttā sasaṅkhārena") == (
    B.PH["upekkhāsahagataṃ ñāṇavippayuttaṃ"] + ", " + B.PH["sasaṅkhārena"])

# =========================================================================================
# 5. Opening sentences: «Katame dhammā akusalā / abyākatā? Yasmiṃ samaye …, tasmiṃ samaye …»
# =========================================================================================
RESULT_KAMA = "như là quả của nghiệp thiện thuộc cõi dục lạc đã được tạo và tích lũy"
KAMMA_P = "kāmāvacarassa kusalassa kammassa katattā upacitattā "
OPEN_INTROS = [
    ("akusalaṃ cittaṃ uppannaṃ hoti ", "Vào lúc tâm bất thiện sinh khởi, "),
    (KAMMA_P + "vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti ", f"Vào lúc {EYE} sinh khởi {RESULT_KAMA}, "),
    (KAMMA_P + "vipākaṃ sotaviññāṇaṃ uppannaṃ hoti ", f"Vào lúc {EAR} sinh khởi {RESULT_KAMA}, "),
    (KAMMA_P + "vipākā manodhātu uppannā hoti ", f"Vào lúc yếu tố ý sinh khởi {RESULT_KAMA}, "),
    (KAMMA_P + "vipākā manoviññāṇadhātu uppannā hoti ", f"Vào lúc yếu tố ý thức sinh khởi {RESULT_KAMA}, "),
]
assert C.OPEN_KAMA_KUSALA == "Vào lúc tâm thiện thuộc cõi dục lạc sinh khởi"
PIECES = {
    "ime dhammā kusalā": B.KUSALA_V,
    AKUSALA_V: AKUSALA_V,
    ABYAKATA_V: ABYAKATA_V,
    "alobho abyākatamūlaṃ": f"{C.N['alobho']}, {ABY_ROOT}",   # as «amoho kusalamūlaṃ» = «…, gốc rễ thiện»
    "adoso abyākatamūlaṃ": f"{C.N['adoso']}, {ABY_ROOT}",
}


def rest_vi(rest):
    """What follows 'tasmiṃ samaye' in an opening sentence."""
    r = presub(rest)
    if "; ye vā pana " in r:
        lst, tail = r.split("; ", 1)
        return B.there_list(lst) + B.tail_vi("; " + tail)
    assert r.endswith("."), r
    out = []
    for i, p in enumerate(re.split(r"(\s*…pe…\s*)", r[:-1])):
        if i % 2:
            out.append(p.replace(PE, ELL))
        elif not p:
            continue
        elif re.fullmatch(r"\S+ hoti", p):
            out.append(B.there_vi(p[:-len(" hoti")]))
        else:
            out.append(PIECES[p])
    return "".join(out) + "."


# rest_vi agrees with B.kusala_vi's own list + tail
assert rest_vi("phasso hoti…pe… avikkhepo hoti…pe… ime dhammā kusalā.") == (
    B.there_list("phasso hoti…pe… avikkhepo hoti") + B.tail_vi("…pe… ime dhammā kusalā."))
OPEN_RE = re.compile(r"Katame dhammā (akusalā|abyākatā)\? Yasmiṃ samaye (.*)$")


def open_vi(line):
    """B.kusala_vi's frame for the unwholesome minds and the results of the sense-pleasure realm."""
    kind, body = OPEN_RE.fullmatch(line).groups()
    for p, r in OPEN_INTROS:
        if body.startswith(p):
            body, intro = body[len(p):], r
            break
    else:
        raise KeyError("intro: " + body[:80])
    idx = body.index(" tasmiṃ samaye ")
    x, rest = body[:idx].rstrip(), body[idx + len(" tasmiṃ samaye "):]
    assert x.endswith(","), x
    return M.QUESTION(KIND[kind]) + " " + intro + B.x_vi(x[:-1]) + f", {C.THEN} " + rest_vi(rest)


# the wholesome frame and this one agree (same Pāli, same Vietnamese)
_k = ("Katame dhammā kusalā? Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ "
      "ñāṇavippayuttaṃ sasaṅkhārena rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha, tasmiṃ samaye "
      "phasso hoti…pe… avikkhepo hoti…pe… ime dhammā kusalā.")
assert B.kusala_vi(_k).endswith(", " + B.x_vi("somanassasahagataṃ ñāṇavippayuttaṃ sasaṅkhārena rūpārammaṇaṃ vā…pe… "
                                              "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha") + f", {C.THEN} "
                                + rest_vi("phasso hoti…pe… avikkhepo hoti…pe… ime dhammā kusalā."))

# =========================================================================================
# 6. Results of the fine-material and immaterial spheres: the wholesome sentence (B.kusala_vi,
#    byte-identical to 2-02's frame) + «Tasseva … vipākaṃ …» (its result)
# =========================================================================================
SPHERE = {"rūpāvacarassa": "cõi hình sắc", "arūpāvacarassa": "cõi không hình sắc"}


def TASSEVA(sphere):
    """'Tasseva <sphere> kusalassa kammassa katattā upacitattā vipākaṃ …'"""
    return f"Như là quả của chính nghiệp thiện thuộc {sphere} ấy đã được tạo và tích lũy, khi một người"


assert RESULT_KAMA.endswith(" đã được tạo và tích lũy") and TASSEVA("x").startswith("Như là quả của ")
SPHERE_RE = re.compile(
    r"Katame dhammā abyākatā\? (Yasmiṃ samaye .*? ime dhammā kusalā\.) Tasseva (rūpāvacarassa|arūpāvacarassa) "
    r"kusalassa kammassa katattā upacitattā vipākaṃ (.*?), tasmiṃ samaye (.*)$")


def sphere_vi(line):
    m = SPHERE_RE.fullmatch(line)
    if not m:
        return None
    kus_p, sphere, x, rest = m.groups()
    kus = B.kusala_vi("Katame dhammā kusalā? " + kus_p)
    assert kus.startswith(B.Q_KUSALA + " ")
    kus = kus[len(B.Q_KUSALA) + 1:]
    xv = B.x_vi(x)
    lead = ", " if xv.startswith("khi ") else " "   # «khi một người, khi đã …, chứng nhập …»
    return (M.QUESTION(C.ABYAKATA) + " " + kus + " " + TASSEVA(SPHERE[sphere]) + lead + xv
            + f", {C.THEN} " + rest_vi(rest))


# =========================================================================================
# 7. Headings and closing lines (headings verbatim from vi-zeroshot-terms.md; B.check_headings checks them)
# =========================================================================================
VIPAKA = "là quả của nghiệp thiện"
HEAD = {
    "#### Dvādasa akusalāni": "#### Mười hai loại tâm bất thiện",
    "#### Abyākatavipāko": "#### Quả của nghiệp, không xác định về mặt đạo đức",
    "##### Kusalavipākapañcaviññāṇāni": f"##### Năm loại thức {VIPAKA}",
    "##### Kusalavipākamanodhātu": f"##### Yếu tố ý {VIPAKA}",
    "##### Kusalavipākamanoviññāṇadhātusomanassasahagatā": f"##### Yếu tố ý thức {VIPAKA}, {ACC['somanassa']}",
    "##### Kusalavipākamanoviññāṇadhātuupekkhāsahagatā": f"##### Yếu tố ý thức {VIPAKA}, {ACC['upekkhā']}",
    "##### Aṭṭhamahāvipākā": "##### Tám quả nghiệp lớn",
    "##### Rūpāvacaravipākā": "##### Các quả nghiệp thuộc cõi hình sắc",
    "##### Arūpāvacaravipākā": "##### Các quả nghiệp thuộc cõi không hình sắc",
}
CLOSE = {
    "Dvādasa akusalacittāni.": "Mười hai loại tâm bất thiện.",
    "Kusalavipākāni pañcaviññāṇāni.": f"Năm loại thức {VIPAKA}.",
    "Kusalavipākā manodhātu.": f"Yếu tố ý {VIPAKA}.",
    "Kusalavipākā manoviññāṇadhātu somanassasahagatā.": f"Yếu tố ý thức {VIPAKA}, {ACC['somanassa']}.",
    "Kusalavipākā upekkhāsahagatā manoviññāṇadhātu.": f"Yếu tố ý thức {VIPAKA}, {ACC['upekkhā']}.",
    "Aṭṭhamahāvipākā.": "Tám quả nghiệp lớn.",
    "Rūpāvacaravipākā.": "Các quả nghiệp thuộc cõi hình sắc.",
    "Arūpāvacaravipākā.": "Các quả nghiệp thuộc cõi không hình sắc.",
}
add(B.EXACT, HEAD)
add(B.EXACT, CLOSE)


# =========================================================================================
# 8. Line dispatch and build
# =========================================================================================
SHAME_RE = re.compile(r"Yaṃ tasmiṃ samaye ((?:na hirīyati|na ottappati) .+?) – ((?:ayaṃ|idaṃ) tasmiṃ samaye .+)$")
QDOT_RE = re.compile(r"(Katam(?:o|ā|aṃ) tasmiṃ samaye \S+ hoti)\. (Y.*)$")   # ^1-473: «hoti.» for «hoti?»


def translate_line(line):
    if line in B.EXACT:
        return B.EXACT[line]
    r = sphere_vi(line)
    if r is not None:
        return r
    if OPEN_RE.fullmatch(line):
        return open_vi(line)
    m = QDOT_RE.fullmatch(line)
    if m:   # translated with «?», then the question mark set back to the Pāli «.»
        v = translate_line(f"{m.group(1)}? {m.group(2)}")
        q = v.index("? ")
        return v[:q] + ". " + v[q + 2:]
    m = B.QRE.fullmatch(line)
    if m:
        name, _, mark, rest = m.groups()
        s = SHAME_RE.fullmatch(rest)
        if s:   # the sample's hirī / ottappa frame «Việc vào lúc ấy S – …»
            assert mark == "?"
            return f"{B.q_vi(name)}? Việc {TASMIM} {B.STR[s.group(1)]} {DASH} " + B.tail_vi(presub(s.group(2)))
    return D.translate_line(presub(line))


def render(segs):
    out = []
    for bid, lines in segs:
        vi = [B.cap(translate_line(l)) for l in lines]
        for p, r in zip(lines, vi):
            B.check_line(p, r)
            assert "…pe…" not in r and "pe…" not in r, (bid, r[:120])
        vi[-1] += f" ^{bid}"
        out.append("\n".join(vi))
    return out


def earlier_pairs():
    """Pāli line -> published Vietnamese line, from the finished parts 2-01, 2-02 and 2-03"""
    pairs = {}
    for name in ("2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md", "2-03-cittuppadakandam.md"):
        ps = B.segments((PALI_DIR / name).read_text(encoding="utf-8"))
        vs = B.segments((OUT_DIR / name).read_text(encoding="utf-8"))
        for (b1, pl), (b2, vl) in zip(ps, vs):
            assert b1 == b2 and len(pl) == len(vl)
            for p, v in zip(pl, vl):
                pairs.setdefault(p, v)
    return pairs


def build():
    segs = B.segments((PALI_DIR / PART).read_text(encoding="utf-8"))
    out = render(segs)
    text = "\n\n".join(out) + "\n"
    prev = earlier_pairs()
    shared = 0
    for (bid, pl), seg in zip(segs, out):
        vl = re.sub(r" \^[0-9A-Za-z-]+$", "", seg).split("\n")
        for p, v in zip(pl, vl):
            if p in prev:
                assert prev[p] == v, (bid, p[:80], v[:120], prev[p][:120])
                shared += 1
    # every earlier Pāli line still renders as published (the added entries changed nothing)
    rechecked = skipped = 0
    for p, v in prev.items():
        if p.startswith("#") or p in B.EXACT:
            continue
        try:
            got = B.cap(D.translate_line(p))
        except Exception:   # a few 2-01 sample lines are hand-built (variant brackets); skip them
            skipped += 1
            continue
        if "[" in p and got != v:
            skipped += 1
            continue
        assert got == v, ("earlier line changed", p[:80], got[:120], v[:120])
        rechecked += 1
    print(f"earlier parts: {rechecked} lines re-rendered identically, {skipped} hand-built lines skipped")
    return text, len(segs), shared


if __name__ == "__main__":
    print("headings equal the terms file:", B.check_headings())
    text, n, shared = build()
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text and ":-" not in text
    (OUT_DIR / PART).write_bytes(text.encode("utf-8"))
    print("wrote", OUT_DIR / PART, n, "segments;", shared, "lines identical to the same Pāli in 2-01/2-02/2-03")
