# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Vietnamese plain zero-shot: chapters 7 (Satipaṭṭhāna), 8 (Sammappadhāna), 9 (Iddhipāda).

usage: python -I -X utf8 build_7-9_vi.py
Writes AI_translation\\vietnamese\\pi-2-vietnamese-plain-zeroshot_split_chapters\\7-satipatthanavibhango.md,
8-sammappadhanavibhango.md and 9-iddhipadavibhango.md (only when run as a script; importing writes nothing).

Imports build_ch1_sample_vi (S), build_1_vi (B), build_2-3_vi (T), build_4-5_vi (F) and build_6_vi (G) and reuses
their strings (nothing of theirs is rewritten; T's item tables are extended in memory only). pi-1 strings (the four
efforts ^1-1377, the sati / vīriya / samādhi / paññā bodies, the awakening-factor names, the hindrances, the root
formulas ^1-985 / ^1-986, the supramundane jhāna frame ^1-277 and its result clause ^1-505) are copied from the
reviewed pi-1 Vietnamese rails and asserted. Every sentence is built from fixed strings by clause-level parsers,
so identical Pāli gives identical Vietnamese; unknown Pāli raises KeyError (nothing is guessed).
"""
import importlib
import os
import re
import sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai"
sys.path.insert(0, HERE)
import build_ch1_sample_vi as S  # noqa: E402
import build_1_vi as B  # noqa: E402
T = importlib.import_module("build_2-3_vi")
F = importlib.import_module("build_4-5_vi")
G = importlib.import_module("build_6_vi")

DASH = S.DASH
cap, low = S.cap, S.low
pi1, between, repl = T.pi1, T.between, T.repl
q, called = T.q, T.called
in_pi1 = G.in_pi1
SLIPS = []
IDHA, BHIKKHU = F.IDHA, F.BHIKKHU                 # Ở đời này / vị tỳ-khưu [pi-1]
WHAT = G.WHAT                                     # Điều mà là
TENA = cap(G.TENA)                                # Vì thế nên mới nói rằng [ch6]

# ================================================================ 1. names
LOC = {"kāya": "thân", "vedanā": "các cảm giác", "citta": "tâm", "dhamma": "các hiện tượng"}   # [ch4 MINDFUL]
LOC_P = {"kāya": ("kāye", "kāyānupassī"), "vedanā": ("vedanāsu", "vedanānupassī"), "citta": ("citte", "cittānupassī"),
         "dhamma": ("dhammesu", "dhammānupassī")}
ASPECTS = ("kāya", "vedanā", "citta", "dhamma")
W = {"": "", "ajjhattaṃ": " " + B.P("ajjhatta"), "bahiddhā": " " + B.P("bahiddha"),
     "ajjhattabahiddhā": " " + B.P("ajjhattabahiddha")}   # ở nơi bản thân / ở bên ngoài bản thân / … và … [pi-1]
SATI_TAIL = F.SATI_TAIL   # nhiệt tâm, hiểu biết rõ ràng, có sự tỉnh thức, sau khi chế ngự … đối với thế gian [ch4]
P_TAIL = "ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ"


def anup(asp, w="", live=True):
    """(ajjhattaṃ) kāye kāyānupassī (viharati) -> «đối với thân (ở nơi bản thân), (sống) quán sát thân»"""
    return f"đối với {LOC[asp]}{W[w]}, {'sống ' if live else ''}quán sát {LOC[asp]}"


assert f"{BHIKKHU}, {anup('kāya')}, {SATI_TAIL}" in F.MINDFUL
SATIPATTHANA = "sự thiết lập tỉnh thức"            # [pi-1 ^1-? lokuttaraṃ satipaṭṭhānaṃ]
SAMMAPPADHANA = "nỗ lực đúng đắn"                  # [pi-1 APPROVED, = sammāvāyāma]
IDDHIPADA = "nền tảng thần thông"                  # [pi-1]
in_pi1("tu tập " + SATIPATTHANA + " vượt thế gian", "tu tập " + SAMMAPPADHANA + " vượt thế gian",
       "tu tập " + IDDHIPADA + " vượt thế gian")
LOKA = "thế gian"                                  # loko [ch4]
ABHIJJHA, DOMANASSA = "sự thèm muốn", F.SADNESS    # [pi-1 ^1-1352 «sự thèm muốn và nỗi buồn»]
UPK = F.UPK                                        # làm đối tượng cho sự bám víu [ch4]

# iddhipāda: chanda / vīriya / citta / vīmaṃsā [pi-1 ^1-269 «lấy ý muốn / tinh tấn / tâm / sự thẩm xét làm yếu tố chủ đạo»]
X_VI = {"chanda": "ý muốn", "vīriya": "tinh tấn", "citta": "tâm", "vīmaṃsā": "sự thẩm xét"}
for _x in X_VI.values():
    in_pi1(f"lấy {_x} làm yếu tố chủ đạo")
X_ACC = {"Chandaṃ": "chanda", "Vīriyaṃ": "vīriya", "Cittaṃ": "citta", "Vīmaṃsaṃ": "vīmaṃsā"}
SAMX = {k: f"định tâm nhờ {v}" for k, v in X_VI.items()}             # Xsamādhi [new]
PSANKHARA, PSANKHARA_PL = "sự tạo tác bằng nỗ lực", "các sự tạo tác bằng nỗ lực"   # padhānasaṅkhāro / -ā [new; ch6 «bằng»]
EQUIPPED = "được trang bị"                                           # samannāgata [new]
IDP_NAME = {"chandiddhipādo": "chanda", "vīriyiddhipādo": "vīriya", "cittiddhipādo": "citta", "vīmaṃsiddhipādo": "vīmaṃsā"}
IDP = {k: f"{IDDHIPADA} bằng {X_VI[v]}" for k, v in IDP_NAME.items()}   # Xiddhipādo [new]


def samannagata(x):
    """Xsamādhipadhānasaṅkhārasamannāgata -> «được trang bị định tâm nhờ X và sự tạo tác bằng nỗ lực»"""
    return f"{EQUIPPED} {SAMX[x]} và {PSANKHARA}"


def idp_full(x):
    return f"{IDDHIPADA} {samannagata(x)}"


X_P = {"chanda": "chanda", "vīriya": "vīriya", "citta": "citta", "vīmaṃsā": "vīmaṃsā"}   # Pāli stems

# ================================================================ 2. pi-1 bodies
VIRIYA_FULL = F.VIRIYA + ", nỗ lực đúng đắn"       # pi-2 ^2-433 has sammāvāyāmo (ch5 ^2-220 had not)
assert VIRIYA_FULL.endswith("sức mạnh tinh tấn, nỗ lực đúng đắn")
VIRIYA_PE = F.pe_cut(VIRIYA_FULL, 1, "nỗ lực đúng đắn")             # vīriyārambho…pe… sammāvāyāmo
SATI_PE = F.pe_cut(F.SATI, 2, "tỉnh thức đúng đắn")                  # sati anussati…pe… sammāsati
SAMADHI_PE = F.pe_cut(F.SAMADHI, 2, "định tâm đúng đắn")             # cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi
_ST = F.PF["sammāsati"][1]                                           # pi-1 ^1-303 body (with sambojjhaṅgo …)
_sti = _ST.split(", ")
SATI_LOK = f"{_sti[0]}, {_sti[1]}, " + _ST[_ST.index("tỉnh thức đúng đắn"):]   # sati anussati sammāsati satisambojjhaṅgo …
assert SATI_LOK == ("sự tỉnh thức, sự nhớ lại, tỉnh thức đúng đắn, chi phần giác ngộ là sự tỉnh thức, "
                    "chi phần của con đường, nằm trong con đường"), SATI_LOK
CITTA_PE = f"{T.CITTA3}… yếu tố ý thức tương ứng"   # cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu [ch6]
assert G.BODY["Yaṃ cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu"] == WHAT + CITTA_PE
CHANDA = "ý muốn, sự khởi ý muốn, sự muốn hành động, ý muốn thiện đối với các hiện tượng"   # [new; chanda pi-1]
CHANDA_VAR = repl(CHANDA, "sự khởi ý muốn,", "sự khởi ý muốn [khác chính tả (Syā.): chandīkatā],")
AB = F.ABHI_BODY
BODYP = {   # Pāli definition body (after Yo / Yā / Yaṃ, or after "yo tasmiṃ samaye") -> Vietnamese
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": F.PANNA,
    "cetasiko vīriyārambho…pe… sammāvāyāmo": VIRIYA_PE,
    ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo ṭhiti asithilaparakkamatā "
     "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo"): VIRIYA_FULL,
    "sati anussati…pe… sammāsati": SATI_PE,
    "sati anussati sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": SATI_LOK,
    "rāgo sārāgo…pe… cittassa sārāgo": F.pe_cut(G.RAGA, 2, "sự say đắm của tâm"),
    ("cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā "
     "vedanā"): G.FEEL["domanassa"],
    "chando chandikatā [chandīkatā (syā.)] kattukamyatā kusalo dhammacchando": CHANDA_VAR,
    "chando chandikatā kattukamyatā kusalo dhammacchando": CHANDA,
    "cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu": CITTA_PE,
    ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ "
     "sammāsamādhi"): F.SAMADHI,
    "cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi": SAMADHI_PE,
}
for _k, _v in AB.items():   # the lokuttara bodies with "…sambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ" [ch4]
    if _k.startswith(("Yā paññā", "Yo cetasiko vīriyārambho…pe…", "Yā cittassa ṭhiti saṇṭhiti…pe…")):
        BODYP[_k.split(" ", 1)[1]] = _v
assert G.BODY["Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi"] == WHAT + F.PANNA
in_pi1("sự khởi động tinh tấn trong tâm", "sự ổn định của tâm, sự vững vàng")

# pi-1 ^1-1377: the four right efforts, one string per purpose
VV = "khởi lên ý muốn, nỗ lực, khởi động tinh tấn, nâng tâm lên, ra sức nỗ lực"   # chandaṃ janeti … padahati
PV = "chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati"
NP = ["các hiện tượng xấu ác bất thiện chưa sinh khởi", "các hiện tượng xấu ác bất thiện đã sinh khởi",
      "các hiện tượng thiện chưa sinh khởi", "các hiện tượng thiện đã sinh khởi"]
PP = ["anuppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ anuppādāya", "uppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ pahānāya",
      "anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya",
      "uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā"]
PNOM = ["anuppannā pāpakā akusalā dhammā", "uppannā pāpakā akusalā dhammā", "anuppannā kusalā dhammā",
        "uppannā kusalā dhammā"]
MAINT = "được duy trì, không bị mai một, được tăng trưởng, được lớn mạnh, được tu tập, được hoàn thiện"


def goal(i, np):
    return [f"để {np} không sinh khởi", f"để dứt bỏ {np}", f"để {np} được sinh khởi", f"để {np} {MAINT}"][i]


def this_np(i):
    """imesaṃ …: «những hiện tượng … này»"""
    return "những " + NP[i][len("các "):] + " này"


EFF = [f"{VV} {goal(i, NP[i])}" for i in range(4)]
assert "; ".join(EFF) == between(pi1("1-1377"), f"ở đời này, {BHIKKHU} ", "."), "; ".join(EFF)
EFF_ALL = "; ".join(EFF)
EFF_PE = f"{EFF[0]}; {goal(1, NP[1])}… {goal(2, NP[2])}… {EFF[3]}"   # P1 V, P2…pe… P3…pe… P4 V
P_EFF = [f"{PP[i]} {PV}" for i in range(4)]
P_EFF_ALL = ", ".join(P_EFF)
P_EFF_PE = f"{P_EFF[0]}, {PP[1]}…pe… {PP[2]}…pe… {P_EFF[3]}"

# pi-1 ^1-985 / ^1-986: roots, defilements, associated aggregates, the action they originate
_a986, _a985 = pi1("1-986"), pi1("1-985")
AKUSALAMULA3 = between(_a986, "? ", ";")                           # Ba gốc rễ bất thiện – sự tham lam, …
KUSALAMULA3 = between(_a985, "? ", ";")
assert AKUSALAMULA3 == f"Ba gốc rễ bất thiện {DASH} sự tham lam, sự sân hận, sự si mê", AKUSALAMULA3
assert KUSALAMULA3 == f"Ba gốc rễ thiện {DASH} sự không tham lam, sự không sân hận, sự không si mê", KUSALAMULA3
KILESA = "và các phiền não cùng hiện diện với chúng"                 # tadekaṭṭhā ca kilesā
AGG4_SAMP = "khối cảm giác, khối tri giác, khối tạo tác và khối thức gắn liền với chúng"   # taṃsampayutto …
KAMMA3 = "nghiệp bằng thân, nghiệp bằng lời nói, nghiệp bằng ý do chúng sinh ra"          # taṃsamuṭṭhānaṃ …
for _x in (KILESA, AGG4_SAMP, KAMMA3):
    assert _x in _a986, _x
assert AGG4_SAMP in _a985 and KAMMA3 in _a985

# body parts (ch3 lists: the pathavī and āpo internal lists, same Pāli order)
BODY32_VAR = T.LISTS["pathavi_int"] + ", " + T.LISTS["apo_int"]
BODY32 = BODY32_VAR.replace(" [khác chính tả (Sī.): nahāru]", "").replace(" [khác chính tả (Sī.): aṭṭhimiñjā]", "")
P_BODY32_VAR = ("kesā lomā nakhā dantā taco maṃsaṃ nhāru [nahāru (sī.)] aṭṭhi aṭṭhimiñjaṃ [aṭṭhimiñjā (sī.)] vakkaṃ "
                "hadayaṃ yakanaṃ kilomakaṃ pihakaṃ papphāsaṃ antaṃ antaguṇaṃ udariyaṃ karīsaṃ pittaṃ semhaṃ pubbo "
                "lohitaṃ sedo medo assu vasā kheḷo siṅghāṇikā lasikā mutta")
P_BODY32 = P_BODY32_VAR.replace(" [nahāru (sī.)]", "").replace(" [aṭṭhimiñjā (sī.)]", "")


def check_ch3_lists():
    """the ch. 7 body-part list has the ch. 3 Pāli (pathavī internal list, then āpo internal list)."""
    p3 = open(os.path.join(S.PALI_DIR, "3-dhatuvibhango.md"), encoding="utf-8").read()
    a, b = P_BODY32_VAR.split(" pittaṃ ")
    assert a in p3 and ("pittaṃ " + b) in p3, "ch3 lists"
    assert len(BODY32.split(", ")) == len(P_BODY32.split(" ")) == 31


# awakening factors and hindrances [pi-1]
BOJJH = {"sati": "sự tỉnh thức", "dhammavicaya": "sự tìm hiểu các hiện tượng", "vīriya": "sự tinh tấn",
         "pīti": "sự hân hoan", "passaddhi": "sự an tịnh", "samādhi": "định tâm", "upekkhā": "sự bình thản"}
for _k, _v in BOJJH.items():
    if _k != "upekkhā":   # upekkhāsambojjhaṅga is not in the pi-1 rails: same pattern, pi-1 upekkhā «sự bình thản»
        in_pi1("chi phần giác ngộ là " + _v)
DH_NAME = {"kāmacchand": "ý muốn dục lạc", "byāpād": "ác ý", "thinamiddh": "sự uể oải và đờ đẫn",
           "uddhaccakukkucc": "sự xao động và hối tiếc", "vicikicch": "sự hoài nghi"}   # [pi-1 ^1-1158 …]
in_pi1("chướng ngại ý muốn dục lạc, chướng ngại ác ý, chướng ngại uể oải và đờ đẫn, chướng ngại xao động và hối tiếc, "
       "chướng ngại hoài nghi")
for _k, _v in BOJJH.items():
    DH_NAME[_k + "sambojjhaṅg"] = "chi phần giác ngộ là " + _v
DH_END = {"kāmacchand": ("aṃ", "o", "assa"), "byāpād": ("aṃ", "o", "assa"), "thinamiddh": ("aṃ", "aṃ", "assa"),
          "uddhaccakukkucc": ("aṃ", "aṃ", "assa"), "vicikicch": ("aṃ", "ā", "āya")}
for _k in BOJJH:
    DH_END[_k + "sambojjhaṅg"] = ("aṃ", "o", "assa")
VAR = {   # variant brackets in these chapters
    "[thīnamiddhaṃ (sī. syā.)]": "[khác chính tả (Sī., Syā.): thīnamiddhaṃ]",
    "[viriyasambojjhaṅgaṃ (sī. syā.)]": "[khác chính tả (Sī., Syā.): viriyasambojjhaṅgaṃ]",
    "[katamaṃ ātāpaṃ (sabbattha)]": "[dị bản (tất cả các ấn bản): katamaṃ ātāpaṃ]",
    "[cittassa ekaggataṃ (sī. syā.)]": "[khác chính tả (Sī., Syā.): cittassa ekaggataṃ]",
    "[saṅkhaṃ (sī.)]": "[khác chính tả (Sī.): saṅkhaṃ]",
    "[uṭṭhāpeti samuṭṭhāpeti (syā.) evamuparipi]": "[khác chính tả (Syā.): uṭṭhāpeti samuṭṭhāpeti; cũng vậy ở các chỗ sau]",
}

# ================================================================ 3. fixed sentences
NIM1 = "Vị ấy thực hành dấu hiệu ấy, tu tập, làm đi làm lại, xác định cho thật rõ ràng."   # [new; pi-1 words]
in_pi1("sự thực hành, sự tu tập, sự làm đi làm lại", "dấu hiệu")
NIM2 = "Sau khi thực hành dấu hiệu ấy, tu tập, làm đi làm lại, xác định cho thật rõ ràng, vị ấy đưa tâm đến {}."
UPETO = "vị ấy là người có được, có được trọn vẹn, đã tiếp cận, đã tiếp cận trọn vẹn, đã đạt đến, đã thành tựu, " + EQUIPPED
UPETO_PE = "vị ấy là người có được… " + EQUIPPED
P_UPETO = "upeto hoti samupeto upāgato samupāgato upapanno sampanno samannāgato"
P_UPETO_PE = "upeto hoti…pe… samannāgato"
INSTR = {"anupassanāya": "sự quán sát", "ātāpena": "sự nhiệt tâm", "sampajaññena": "sự hiểu biết rõ ràng",
         "satiyā": "sự tỉnh thức", "vāyāmena": "sự nỗ lực", "padhānena": "sự nỗ lực",
         "chandena": "ý muốn", "vīriyena": "sự tinh tấn", "cittena": "tâm", "vīmaṃsāya": "sự thẩm xét"}
VINITA = ("Như vậy, sự thèm muốn này và nỗi buồn này đối với thế gian này đã được chế ngự, đã được chế ngự hoàn toàn, "
          "đã lắng yên, đã được làm lắng dịu, đã lắng dịu hoàn toàn, đã biến mất, đã biến mất hoàn toàn, "
          "đã đi đến kết thúc, đã đi đến kết thúc hoàn toàn, đã bị làm khô cạn, đã bị làm khô cạn hoàn toàn, "
          "đã bị làm cho tiêu tan.")   # [new; «đã biến mất, đã biến mất hoàn toàn» pi-1 ^1-1044]
in_pi1("đã biến mất, đã biến mất hoàn toàn")
ASP_GEN = {"kāya": "Sveva kāyo loko.", "vedanā": "Sāyeva vedanā loko.", "citta": "Taṃyeva cittaṃ loko.",
           "dhamma": "Teva dhammā loko."}
PANCA_LOKA = f"Cả năm khối {UPK} cũng là {LOKA}"
IDDHI_DEF = ("Điều mà ở những hiện tượng ấy là thần thông, sự thịnh đạt, sự thành tựu, sự thành tựu trọn vẹn, "
             "sự đạt được, sự có được, sự đạt đến, sự đạt đến trọn vẹn, sự chạm, sự tự mình chứng nghiệm, "
             "sự chứng nhập.")   # [new; paṭilābha ch4 «sự có được», phusanā pi-1 «sự chạm»]
in_pi1("sự tiếp xúc, sự chạm, sự chạm đến", "tự mình chứng nghiệm")
TATHA = "của người đã trở nên như vậy"            # tathābhūtassa [new]
AGG4 = G.AGG4                                     # khối cảm giác, khối tri giác, khối tạo tác, khối thức [ch6]
AGG4_PE = f"{S.AGG['vedana']['khandha']}… {S.AGG['vinnana']['khandha']}"
PHASSA_PE = "sự tiếp xúc… sự dốc sức, sự không tán loạn"   # phasso…pe… paggāho avikkhepo [pi-1]
in_pi1("có sự dốc sức, có sự không tán loạn")
TOGETHER = S.KHANDHA_TOGETHER                     # khi gom tất cả lại làm một và thu tóm lại [sample]
COUNTED = "thì được tính"                         # saṅkhyaṃ gacchati [new]
IMAM = {   # Imaṃ X … (verb lists) [new; pi-1 ^1-1377 verbs]
    ("Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti [uṭṭhāpeti samuṭṭhāpeti (syā.) evamuparipi] nibbatteti "
     "abhinibbatteti."):
        "Vị ấy khởi lên ý muốn này, làm sinh ra, làm trỗi dậy, làm trỗi dậy trọn vẹn "
        + VAR["[uṭṭhāpeti samuṭṭhāpeti (syā.) evamuparipi]"] + ", làm phát khởi, làm hình thành.",
    "Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti nibbatteti abhinibbatteti.":
        "Vị ấy khởi lên ý muốn này, làm sinh ra, làm trỗi dậy, làm trỗi dậy trọn vẹn, làm phát khởi, làm hình thành.",
    "Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti.":
        "Vị ấy khởi động sự tinh tấn này, khởi động trọn vẹn, thực hành, tu tập, làm đi làm lại.",
    "Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti.":
        "Vị ấy nâng tâm này lên, nâng lên trọn vẹn, nâng đỡ, nâng đỡ vững chắc.",
}

LEMMA = {   # "X"ti / Xti (the word explained) [new; ch4 / pi-1 words]
    "anupassī": "quán sát", "viharatī": "sống", "ātāpī": "nhiệt tâm", "sampajāno": "hiểu biết rõ ràng",
    "satimā": "có sự tỉnh thức",
    "vineyya loke abhijjhādomanassaṃ": "sau khi chế ngự sự thèm muốn và nỗi buồn đối với thế gian",
    "chandaṃ janetī": "khởi lên ý muốn", "vāyamatī": "nỗ lực", "vīriyaṃ ārabhatī": "khởi động tinh tấn",
    "cittaṃ paggaṇhātī": "nâng tâm lên", "padahatī": "ra sức nỗ lực", "ṭhitiyā": "để được duy trì",
    "iddhī": "thần thông", "iddhipādo": IDDHIPADA, "iddhipādaṃ bhāvetī": "tu tập " + IDDHIPADA,
}
for _x in X_VI:
    LEMMA[f"{_x}samādhipadhānasaṅkhārasamannāgato"] = samannagata(_x)
assert LEMMA["vineyya loke abhijjhādomanassaṃ"] == SATI_TAIL[SATI_TAIL.index("sau khi"):]
NAME = {   # Tattha katamo X? / … vuccati "X"
    "anupassanā": "sự quán sát", "ātāpo": "sự nhiệt tâm", "sampajaññaṃ": "sự hiểu biết rõ ràng",
    "sati": "sự tỉnh thức", "loko": LOKA, "abhijjhā": ABHIJJHA, "domanassaṃ": DOMANASSA,
    "satipaṭṭhānaṃ": SATIPATTHANA, "sammappadhānaṃ": SAMMAPPADHANA,
    "chando": "ý muốn", "vāyāmo": "sự nỗ lực", "vīriyaṃ": "sự tinh tấn", "cittaṃ": "tâm", "padhānaṃ": "sự nỗ lực",
    "samādhi": "định tâm", "vīmaṃsā": "sự thẩm xét", "padhānasaṅkhāro": PSANKHARA, "padhānasaṅkhārā": PSANKHARA_PL,
}
for _i in range(4):
    NAME[PNOM[_i]] = NP[_i]
for _x in X_VI:
    NAME[f"{_x}samādhi"] = SAMX[_x]
NAME.update(IDP)
in_pi1("sự hiểu biết rõ ràng", "sự nhất tâm", "ý muốn")

SENT = {
    "Ime dhammā kusalā.": "Những hiện tượng này là thiện.",                                    # [pi-1]
    "Tīṇi akusalamūlāni – lobho, doso, moho.": AKUSALAMULA3 + ".",
    "Tīṇi kusalamūlāni – alobho, adoso, amoho.": KUSALAMULA3 + ".",
    "Tadekaṭṭhā ca kilesā.": cap(KILESA) + ".",
    "Taṃsampayutto vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.": cap(AGG4_SAMP) + ".",
    "So taṃ nimittaṃ āsevati bhāveti bahulīkaroti svāvatthitaṃ vavatthapeti.": NIM1,
    "Iriyati vattati pāleti yapeti yāpeti carati viharati.":
        "Vị ấy vận động, tiến triển, gìn giữ, tiếp diễn, kéo dài, đi lại, sống.",   # [pi-1 ^1-19 words]
    "Pañcapi upādānakkhandhā loko.": PANCA_LOKA + ".",
    "Pañcapi upādānakkhandhā loko – tattha katamā abhijjhā?":                           # ^2-366 as written
        f"{PANCA_LOKA} {DASH} {low(q(ABHIJJHA))}",
    ("Iti ayañca abhijjhā idañca domanassaṃ imamhi loke vinītā honti paṭivinītā santā samitā vūpasantā atthaṅgatā "
     "abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā."): VINITA,
    "Yā ṭhiti so asammoso, yo asammoso so bhiyyobhāvo, yo bhiyyobhāvo taṃ vepullaṃ, yaṃ vepullaṃ sā bhāvanā, "
    "yā bhāvanā sā pāripūrī.":
        "Sự duy trì là sự không mai một, sự không mai một là sự tăng trưởng, sự tăng trưởng là sự lớn mạnh, "
        "sự lớn mạnh là sự tu tập, sự tu tập là sự hoàn thiện.",                        # [new; pi-1 ^1-1377 words]
    "Yā tesaṃ dhammānaṃ iddhi samiddhi ijjhanā samijjhanā lābho paṭilābho patti sampatti phusanā sacchikiriyā "
    "upasampadā.": IDDHI_DEF,
    "Tathābhūtassa vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.": f"{cap(AGG4)} {TATHA}.",
    "Tathābhūtassa vedanākkhandho…pe… viññāṇakkhandho.": f"{cap(AGG4_PE)} {TATHA}.",
    "Tathābhūtassa phasso…pe… paggāho avikkhepo.": f"{cap(PHASSA_PE)} {TATHA}.",
    "Te dhamme āsevati bhāveti bahulīkaroti.": "Vị ấy thực hành những hiện tượng ấy, tu tập, làm đi làm lại.",
}
SENT.update(IMAM)
for _a in ASPECTS:
    SENT[ASP_GEN[_a]] = {"kāya": "Chính thân ấy", "vedanā": "Chính cảm giác ấy", "citta": "Chính tâm ấy",
                         "dhamma": "Chính các hiện tượng ấy"}[_a] + f" là {LOKA}."

# ================================================================ 4. sentence parsers
FIXES = [   # (Pāli as written, as meant): punctuation / spelling only (reported)
    ("Siyā vipākā siyā vipākadhammadhammā", "Siyā vipākā, siyā vipākadhammadhammā"),       # ^2-388 comma
    ("sāsavācātipi", "sāsavā cātipi"), ("āsavasampayuttācātipi", "āsavasampayuttā cātipi"),   # ^2-389 spaces
    ("viññāṇakhandho.", "viññāṇakkhandho."),                                                # ^2-443 spelling
    ("Tathābhūtasa ", "Tathābhūtassa "),                                                    # ^2-450 spelling
    ("maggariyāpannaṃ", "maggapariyāpannaṃ"),                                               # ^2-459 spelling
    ("abhisaññahitvā", "abhisaññūhitvā"),                                                   # ^2-432 spelling
    ('samannāgato"ti', 'samannāgato"ti.'),                                                   # ^2-455 full stop (see line())
]
NOSPACE_PE = re.compile(r"(?<=[^\]]) …pe…")
SPLIT = re.compile(r'(?<=[.?])\s+(?=[A-ZĀĪŪṬḌÑṆṄ"])')
LOKP = ("lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā "
        "vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ")
LOK_VI = f"{IDHA}, vào lúc {BHIKKHU} {F.JHANA_LOK}"        # … chậm chạp,  [pi-1 ^1-277 via ch4]
TAS_P = ("lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja "
         "viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ")
TAS_VI = G.PI1_TASSEVA[TAS_P]                              # Còn khi một người … đã được tạo và tu tập [pi-1 ^1-505]
YAM_SAMAYE = "thì điều mà vào lúc ấy là"                    # yo / yā / yaṃ tasmiṃ samaye … [pi-1 «Điều mà vào lúc ấy là»]
ANS = re.compile(r'^(.+) – (?:ayaṃ vuccati|idaṃ vuccati|ime vuccanti) ("?)([^"]+)("?)\.$')
TATTHA_ = S.TATTHA
ANS_ALONE = re.compile(r'^(?:Ayaṃ|Idaṃ) vuccati "([^"]+)"\.$|^Ime vuccanti "([^"]+)"\.$')
ASP_OF = {LOC_P[a][0] + " " + LOC_P[a][1]: a for a in ASPECTS}


def answer_tail(s):
    """'<body> – ayaṃ vuccati "X".' -> (<body>, « – đó được gọi là “X”.»)"""
    m = ANS.match(s)
    if not m:
        raise KeyError("answer: " + s[-80:])
    body, q1, name, q2 = m.groups()
    assert q1 == q2, s
    return body, f" {DASH} {called(NAME[name], bool(q1))}."


def anup_sent(asp, w, tail):
    return f"{anup(asp, w)}{tail}"


def lemma_key(x):
    m = re.match(r'^"?([^"]+?)"?(n?)ti$', x)
    return low(m.group(1)) + ("ṃ" if m.group(2) else "") if m else None


def lemma(x):
    return LEMMA[lemma_key(x)]


def lok_rest(rest):
    """the text after "Idha bhikkhu yasmiṃ samaye <LOKP>" (or after "Tasseva … suññataṃ")."""
    m = re.match(r"^, tasmiṃ samaye (.+)\.$", rest)
    if m:
        t = m.group(1)
        if t == "phasso hoti…pe… avikkhepo hoti":
            return f" thì vào lúc ấy có {F.CONTACT_TO}."
        if t == P_EFF[0] or t in P_EFF:
            return f" thì vào lúc ấy vị ấy {EFF[P_EFF.index(t)]}."
        m2 = re.match(r"^(\w+?)samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti$", t)
        if m2:
            return f" thì vào lúc ấy vị ấy tu tập {idp_full(m2.group(1))}."
        raise KeyError("tasmiṃ samaye: " + t[:80])
    m = re.match(r"^(?: (\w+ \w+))?, y(?:o|ā|aṃ) tasmiṃ samaye (.+)$", rest)
    if not m:
        raise KeyError("lok rest: " + rest[:80])
    body, tail = answer_tail(m.group(2))
    pre = f" {anup(ASP_OF[m.group(1)], '', False)}," if m.group(1) else ""
    return f"{pre} {YAM_SAMAYE} {BODYP[body]}{tail}"


def sentence(s):
    if s in SENT:
        return SENT[s]
    # Kathañca bhikkhu …?
    m = re.match(r"^Kathañca bhikkhu (?:(ajjhattaṃ|bahiddhā|ajjhattabahiddhā) )?(\w+ \w+) viharati\?$", s)
    if m:
        return f"Và {BHIKKHU}, {anup(ASP_OF[m.group(2)], m.group(1) or '')} như thế nào?"
    m = re.match(r"^Kathañca bhikkhu (.+) padahati\?$", s)
    if m:
        return f"Và {BHIKKHU} {EFF[P_EFF.index(m.group(1) + ' padahati')]} như thế nào?"
    m = re.match(r"^Kathañca bhikkhu (\w+?)samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti\?$", s)
    if m:
        return f"Và {BHIKKHU} tu tập {idp_full(m.group(1))} như thế nào?"
    # Tattha katamo …?
    m = re.match(r"^Tattha katam(?:o|ā|aṃ|e) (.+?)( \[[^\]]+\])?\?$", s)
    if m:
        name = NAME[m.group(1)]
        return f"{TATTHA_} {name}{' ' + VAR[m.group(2).strip()] if m.group(2) else ''} là gì?"
    # lemmas
    m = re.match(r'^"?([^"]+?)"?(n?)ti\.$', s)
    if m and low(m.group(1)) + ("ṃ" if m.group(2) else "") in LEMMA:
        return f"“{cap(lemma(s[:-1]))}”."
    parts = re.split(r"…pe… ?", s[:-1])
    if len(parts) > 1 and all(lemma_key(x) in LEMMA for x in parts):   # Anupassīti…pe… viharatīti…pe… …nti.
        return "“" + "”… “".join([cap(lemma(parts[0]))] + [lemma(x) for x in parts[1:]]) + "”."
    m = re.match(r'^Tena vuccati "(.+?)"(n?)ti\.$', s)
    if m:
        k = m.group(1) + ("ṃ" if m.group(2) else "")
        return f"{TENA} “{LEMMA[k]}”."
    # Imāya / Iminā X upeto hoti …
    m = re.match(r"^(?:Imāya|Iminā) (\w+) (" + re.escape(P_UPETO) + "|" + re.escape(P_UPETO_PE) + r")\.$", s)
    if m:
        return f"Với {INSTR[m.group(1)]} này, {UPETO if m.group(2) == P_UPETO else UPETO_PE}."
    m = re.match(r"^Iti (?:imāya|iminā) ca (\w+), iminā ca samādhinā, iminā ca padhānasaṅkhārena (" + re.escape(P_UPETO)
                 + "|" + re.escape(P_UPETO_PE) + r")\.$", s)
    if m:
        return (f"Như vậy, với {INSTR[m.group(1)]} này, với định tâm này và với {PSANKHARA} này, "
                f"{UPETO if m.group(2) == P_UPETO else UPETO_PE}.")
    # definitions "Yo / Yā / Yaṃ … – ayaṃ vuccati "X"."
    m = re.match(r"^(?:Yo|Yā|Yaṃ) (.+)$", s)
    if m and " – " in s:
        body, tail = answer_tail(m.group(1))
        return f"{WHAT}{BODYP[body]}{tail}"
    m = ANS_ALONE.match(s)
    if m:
        return cap(called(NAME[m.group(1) or m.group(2)])) + "."
    # body contemplation
    m = re.match(r'^Idha bhikkhu (ajjhattaṃ|bahiddhā|ajjhattabahiddhā) kāyaṃ uddhaṃ pādatalā adho kesamatthakā '
                 r'tacapariyantaṃ pūraṃ nānappakārassa asucino paccavekkhati – "(atthi imasmiṃ kāye|atthissa kāye) '
                 r'(.+)"nti\.$', s)
    if m:
        lst = {P_BODY32_VAR: BODY32_VAR, P_BODY32: BODY32}[m.group(3)]
        who = {"atthi imasmiṃ kāye": "Trong thân này có", "atthissa kāye": "Trong thân của người ấy có"}[m.group(2)]
        return (f"{IDHA}, {BHIKKHU} quán xét thân{W[m.group(1)]}, từ lòng bàn chân trở lên, từ đỉnh tóc trở xuống, "
                f"được bao bọc bởi da, chứa đầy nhiều loại bất tịnh {DASH} “{who} {lst}”.")   # [new]
    m = re.match(r"^So taṃ nimittaṃ āsevitvā bhāvetvā bahulīkaritvā svāvatthitaṃ vavatthapetvā "
                 r"(bahiddhā|ajjhattabahiddhā) (\w+) cittaṃ upasaṃharati\.$", s)
    if m:
        asp = {LOC_P[a][0]: a for a in ASPECTS}[m.group(2)]
        return NIM2.format(LOC[asp] + W[m.group(1)])
    m = re.match(r"^Evaṃ bhikkhu ajjhattabahiddhā (\w+ \w+) viharati " + P_TAIL + r"\.$", s)
    if m:
        return f"Như vậy, {BHIKKHU}, {anup(ASP_OF[m.group(1)], 'ajjhattabahiddhā')}, {SATI_TAIL}."
    # efforts
    m = re.match(r"^Iti imesaṃ (.+)\.$", s)
    if m:
        i = P_EFF.index(m.group(1))
        return f"Như vậy, vị ấy {VV} {goal(i, this_np(i))}."
    m = re.match(r"^So (.+)\.$", s)
    if m and m.group(1) in (P_EFF_ALL, P_EFF_PE):
        return f"Vị ấy {EFF_ALL if m.group(1) == P_EFF_ALL else EFF_PE}."
    m = re.match(r"^Taṃsampayutto vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho, taṃsamuṭṭhānaṃ "
                 r"kāyakammaṃ vacīkammaṃ manokammaṃ (– .+)$", s)
    if m:
        _, tail = answer_tail("x " + m.group(1))
        return f"{cap(AGG4_SAMP)}; {KAMMA3}{tail}"
    m = re.match(r"^Taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ, manokammaṃ (– .+)$", s)
    if m:
        _, tail = answer_tail("x " + m.group(1))
        return f"{cap(KAMMA3)}{tail}"
    # iddhipāda
    m = re.match(r"^(\w+) ce bhikkhu adhipatiṃ karitvā labhati samādhiṃ,? labhati cittassekaggataṃ( \[[^\]]+\])? "
                 r"– ayaṃ vuccati \"(\w+)samādhi\"\.$", s)
    if m:
        x = X_ACC[m.group(1)]
        assert m.group(3) == x
        v = " " + VAR[m.group(2).strip()] if m.group(2) else ""
        return (f"Nếu {BHIKKHU}, sau khi lấy {X_VI[x]} làm yếu tố chủ đạo, đạt được định tâm, đạt được sự nhất tâm{v} "
                f"{DASH} {called(SAMX[x])}.")
    m = re.match(r"^Iti ayañca (\w+?)samādhi, ime ca padhānasaṅkhārā(\.|; tadekajjhaṃ .+\.)$", s)
    if m:
        head = f"Như vậy, đây là {SAMX[m.group(1)]}, và đây là {PSANKHARA_PL}"
        if m.group(2) == ".":
            return head + "."
        return head + "; " + low(together(m.group(2)[2:]))
    if s.startswith("Tadekajjhaṃ "):
        return together(s)
    # supramundane jhāna frame
    m = re.match(r"^Idha bhikkhu yasmiṃ samaye " + re.escape(LOKP) + r"(.*)$", s)
    if m:
        return LOK_VI + lok_rest(m.group(1))            # LOK_VI ends with «chậm chạp,»
    m = re.match(r"^Tasseva " + re.escape(TAS_P) + r"(.*)$", s)
    if m:
        return TAS_VI + "," + lok_rest(m.group(1))
    if re.match(r"^Avasesā dhammā (\w+)sampayuttā\.$", s):
        k = re.match(r"^Avasesā dhammā (\w+)sampayuttā\.$", s).group(1)
        n = {"satipaṭṭhāna": SATIPATTHANA, "sammappadhāna": SAMMAPPADHANA}.get(k) or IDP[k[:-1] + "o"]
        return f"Các hiện tượng còn lại gắn liền với {n}."   # [ch4 AVASESA frame]
    raise KeyError("sentence: " + s[:120])


def together(s):
    m = re.match(r"^[Tt]adekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā (\w+?)samādhipadhānasaṅkhārotveva saṅkhyaṃ"
                 r"( \[[^\]]+\])? gacchati\.$", s)
    if not m:
        raise KeyError("together: " + s[:80])
    v = " " + VAR[m.group(2).strip()] if m.group(2) else ""
    return f"{cap(TOGETHER)}, {COUNTED}{v} là “{SAMX[m.group(1)]} và {PSANKHARA}”."


# ---------------------------------------------------------------- the "Idha bhikkhu … pajānāti" lines (ch. 7)
FEEL_ACC = {"sukhaṃ": "sukha", "dukkhaṃ": "dukkha", "adukkhamasukhaṃ": "adm"}
FEEL_NOM = {"sukha": "sukhā", "dukkha": "dukkhā", "adm": "adukkhamasukhā"}
FEEL_VI = {"sukha": "cảm giác dễ chịu", "dukkha": "cảm giác khó chịu",
           "adm": "cảm giác không khó chịu cũng không dễ chịu"}                  # [pi-1, S.FEELINGS3]
assert ", ".join(FEEL_VI.values()) == S.FEELINGS3
SAMISA = {"sāmisaṃ": ("sāmisā", "có tính trần tục"), "nirāmisaṃ": ("nirāmisā", "không có tính trần tục")}   # [new]
CITTA_ADJ = {"sarāga": "có tham đắm", "vītarāga": "đã lìa tham đắm", "sadosa": "có sân hận",
             "vītadosa": "đã lìa sân hận", "samoha": "có si mê", "vītamoha": "đã lìa si mê",
             "saṃkhitta": "co rút", "vikkhitta": "tán loạn", "mahaggata": B.P("mahaggata"),
             "amahaggata": "không " + B.P("mahaggata"), "sauttara": B.P("sauttara"), "anuttara": B.P("anuttara"),
             "samāhita": "được định tâm", "asamāhita": "không được định tâm", "vimutta": "được giải thoát",
             "avimutta": "không được giải thoát"}                                    # [new; pi-1 matrix words]
OR = "hoặc "


def clause(c, mode):
    """one clause of a ch. 7 contemplation line -> Vietnamese (without the leading «Ở đời này, vị tỳ-khưu»)."""
    # feelings
    m = re.match(r'^(sāmisaṃ vā |nirāmisaṃ vā )?(sukhaṃ|dukkhaṃ|adukkhamasukhaṃ) vedanaṃ (vedayamāno |vedayamānaṃ )?'
                 r'"(.+)"ti pajānāti$', c)
    if m:
        sa, fa, part, quote = m.groups()
        f = FEEL_ACC[fa]
        sam = sa.split(" ")[0] if sa else ""
        fv = FEEL_VI[f] + (" " + SAMISA[sam][1] if sam else "")
        o = OR if sa else ""
        if part == "vedayamāno ":
            assert quote == f"{sam + ' ' if sam else ''}{fa} vedanaṃ vedayāmī", quote
            return f"{o}khi cảm nhận {fv}, hiểu rõ rằng “Tôi đang cảm nhận {fv}”"
        if part == "vedayamānaṃ ":
            assert quote == f"{sam + ' ' if sam else ''}{fa} vedanaṃ vedayatī", quote
            return f"{o}đối với người đang cảm nhận {fv}, hiểu rõ rằng “Người ấy đang cảm nhận {fv}”"
        assert quote == f"{SAMISA[sam][0] + ' ' if sam else ''}{FEEL_NOM[f]} vedanā", quote
        return f"{o}hiểu rõ {fv} là “{fv}”"
    # mind
    m = re.match(r'^(\w+)ṃ vā(ssa)? cittaṃ "(\w+?)(ṃ me|massa|ṃ) citta"nti pajānāti$', c)
    if m:
        a, ssa, a2, who = m.groups()
        assert a == a2 and (who == "massa") == bool(ssa), c
        adj = CITTA_ADJ[a]
        if who == "ṃ me":
            return f"{OR}đối với tâm {adj}, hiểu rõ rằng “Tâm tôi {adj}”"
        if who == "massa":
            return f"{OR}đối với tâm {adj} của người ấy, hiểu rõ rằng “Tâm của người ấy {adj}”"
        return f"{OR}hiểu rõ tâm {adj} là “tâm {adj}”"
    # phenomena: (a)santaṃ vā(ssa) (ajjhattaṃ) X ["(n)atthi … X"ti pajānāti]
    m = re.match(r'^([Ss]antaṃ|[Aa]santaṃ) vā(ssa)? (ajjhattaṃ )?(\w+?)aṃ( \[[^\]]+\])?'
                 r'(?: "(n?atthi)( me ajjhattaṃ|ssa)? (\w+)"ti pajānāti)?$', c)
    if m:
        sa, ssa, ajj, stem, var, nat, who, nom = m.groups()
        name = DH_NAME[stem] + (" " + VAR[var.strip()] if var else "")
        has = "có" if low(sa) == "santaṃ" else "không có"
        if ssa:
            where, qwhere = "người ấy ", "Người ấy "
        elif ajj:
            where, qwhere = "ở nơi bản thân ", "Ở nơi bản thân tôi "
        else:
            where, qwhere = "", ""
        assert (mode == "bahiddhā") == bool(ssa) and (mode == "ajjhattaṃ") == bool(ajj), c
        vi = f"{OR}khi {where}{has} {name}"
        if nat:
            assert nom == stem + DH_END[stem][1] and (nat == "atthi") == (has == "có"), c
            assert (who or "") == {"ajjhattaṃ": " me ajjhattaṃ", "bahiddhā": "ssa", "ajjhattabahiddhā": ""}[mode], c
            vi += f", hiểu rõ rằng “{cap(qwhere + has) if qwhere else cap(has)} {DH_NAME[stem]}”"
        return vi
    m = re.match(r"^yathā ca (anuppann|uppann|pahīn)(?:assa|āya) (\w+?)(?:assa|āya) "
                 r"(uppādo|pahānaṃ|āyatiṃ anuppādo|bhāvanāya pāripūrī) hoti tañca pajānāti$", c)
    if m:
        st, stem, ev = m.groups()
        n = DH_NAME[stem]
        vi = {("anuppann", "uppādo"): f"{n} chưa sinh khởi nảy sinh",
              ("uppann", "pahānaṃ"): f"{n} đã sinh khởi được dứt bỏ",
              ("pahīn", "āyatiṃ anuppādo"): f"{n} đã được dứt bỏ không nảy sinh trở lại trong tương lai",
              ("uppann", "bhāvanāya pāripūrī"): f"{n} đã sinh khởi được tu tập đến chỗ hoàn thiện"}[(st, ev)]
        return f"cũng hiểu rõ {vi} như thế nào"                                          # [new]
    raise KeyError("clause: " + c[:90])


def contemplation(s, mode):
    """"Idha bhikkhu <clause>, <clause>…pe… <clause>." -> «Ở đời này, vị tỳ-khưu, …; …… ….»"""
    body = s[:-1]
    lead = body.startswith("Idha bhikkhu ")
    if lead:
        body = body[len("Idha bhikkhu "):]
    parts = re.split(r"(, | ?…pe… ?)", body)
    out = []
    for i, x in enumerate(parts):
        if i % 2:
            out.append("; " if x == ", " else "… ")
        else:
            out.append(clause(x, mode))
    vi = "".join(out)
    if lead:
        comma = vi.startswith(("khi ", "hoặc khi ", "đối với ", "hoặc đối với "))
        return f"{IDHA}, {BHIKKHU}{',' if comma else ''} {vi}."
    return cap(vi) + "."


def is_contemplation(s):
    return s.endswith("pajānāti.") or (s.startswith(("Santaṃ vā", "Idha bhikkhu santaṃ")) and "…pe…" in s)


# ---------------------------------------------------------------- line
def line(t, mode):
    for a, b in FIXES:
        if a in t and not (a == 'samannāgato"ti' and not t.endswith(a)):
            SLIPS.append(f"{a!r} -> {b!r}")
            t = t.replace(a, b)
    if NOSPACE_PE.search(t):
        SLIPS.append("space before …pe…: " + t[max(0, NOSPACE_PE.search(t).start() - 30):][:50])
        t = NOSPACE_PE.sub("…pe…", t)
    out = []
    for s in SPLIT.split(t):
        if is_contemplation(s):
            out.append(contemplation(s, mode))
        else:
            out.append(sentence(s))
    return " ".join(out)


# ================================================================ 5. labels and openings
SEC = S.SECTION_TITLES
NIDDESA = {"Kāyānupassanāniddeso": "Giải thích sự quán sát thân",                  # [new; ch6 niddesa «Giải thích …»]
           "Vedanānupassanāniddeso": "Giải thích sự quán sát các cảm giác",
           "Cittānupassanāniddeso": "Giải thích sự quán sát tâm",
           "Dhammānupassanāniddeso": "Giải thích sự quán sát các hiện tượng"}
LABELS = {}
for _k, _v in SEC.items():
    LABELS["#### " + _k] = "#### " + _v
    LABELS[_k + "."] = _v + "."
for _k, _v in NIDDESA.items():
    LABELS["##### " + _k] = "##### " + _v
    LABELS[_k + "."] = _v + "."
for _k, _v in IDP.items():
    LABELS["##### " + cap(_k)] = "##### " + cap(_v)
LABELS["##### Tikaṃ"] = B.LABELS["##### Tikaṃ"]
LABELS["##### Dukaṃ"] = B.LABELS["##### Dukaṃ"]
for _n, _p in ((7, "Satipaṭṭhānavibhaṅgo"), (8, "Sammappadhānavibhaṅgo"), (9, "Iddhipādavibhaṅgo")):
    LABELS["### " + _p] = "### " + S.CHAPTER_TITLES[_n]
    LABELS[_p + " niṭṭhito."] = S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[_n])

# Cattāro satipaṭṭhānā – …
_P355 = "Cattāro satipaṭṭhānā – idha bhikkhu " + ", ".join(
    " ".join(f"{w} {LOC_P[a][0]} {LOC_P[a][1]} viharati" for w in ("ajjhattaṃ", "bahiddhā", "ajjhattabahiddhā"))
    + " " + P_TAIL for a in ASPECTS) + "."
LABELS[_P355] = f"Bốn {SATIPATTHANA} {DASH} {low(IDHA)}, {BHIKKHU}, " + "; ".join(
    "; ".join(anup(a, w) for w in ("ajjhattaṃ", "bahiddhā", "ajjhattabahiddhā")) + ", " + SATI_TAIL
    for a in ASPECTS) + "."
_P374 = "Cattāro satipaṭṭhānā – idha bhikkhu " + ", ".join(f"{LOC_P[a][0]} {LOC_P[a][1]} viharati"
                                                            for a in ASPECTS) + "."
LABELS[_P374] = f"Bốn {SATIPATTHANA} {DASH} {low(IDHA)}, {BHIKKHU}, " + "; ".join(anup(a) for a in ASPECTS) + "."
_P386 = "Cattāro satipaṭṭhānā – idha bhikkhu " + ", ".join(f"{LOC_P[a][0]} {LOC_P[a][1]} viharati {P_TAIL}"
                                                            for a in ASPECTS) + "."
LABELS[_P386] = f"Bốn {SATIPATTHANA} {DASH} {low(IDHA)}, {BHIKKHU}, " + "; ".join(
    f"{anup(a)}, {SATI_TAIL}" for a in ASPECTS) + "."
# Cattāro sammappadhānā – …
LABELS[f"Cattāro sammappadhānā – idha bhikkhu {P_EFF_ALL}."] = \
    f"Bốn {SAMMAPPADHANA} {DASH} {low(IDHA)}, {BHIKKHU} {EFF_ALL}."
LABELS[f"Cattāro sammappadhānā – idha bhikkhu {P_EFF_PE}."] = \
    f"Bốn {SAMMAPPADHANA} {DASH} {low(IDHA)}, {BHIKKHU} {EFF_PE}."
# Cattāro iddhipādā – …
_XS = list(X_VI)
LABELS["Cattāro iddhipādā – idha bhikkhu " + ", ".join(
    f"{x}samādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti" for x in _XS) + "."] = \
    f"Bốn {IDDHIPADA} {DASH} {low(IDHA)}, {BHIKKHU} " + "; ".join(f"tu tập {idp_full(x)}" for x in _XS) + "."
LABELS[("Cattāro iddhipādā – idha bhikkhu chandasamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti, "
        "vīriyasamādhi…pe… cittasamādhi…pe… vīmaṃsāsamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti.")] = \
    (f"Bốn {IDDHIPADA} {DASH} {low(IDHA)}, {BHIKKHU} tu tập {idp_full('chanda')}; {SAMX['vīriya']}… "
     f"{SAMX['citta']}… tu tập {idp_full('vīmaṃsā')}.")
LABELS["Cattāro iddhipādā – chandiddhipādo, vīriyiddhipādo, cittiddhipādo, vīmaṃsiddhipādo."] = \
    f"Bốn {IDDHIPADA} {DASH} " + T.listing([IDP[k] for k in IDP]) + "."
for _pa, _tot, _unit in (("satipaṭṭhānānaṃ", "bốn " + SATIPATTHANA, SATIPATTHANA),
                         ("sammappadhānānaṃ", "bốn " + SAMMAPPADHANA, SAMMAPPADHANA),
                         ("iddhipādānaṃ", "bốn " + IDDHIPADA, IDDHIPADA)):
    LABELS[f"Catunnaṃ {_pa} kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?"] = \
        T.question_q(_tot, _unit)
LABELS["Ṭhitiyāti. Yā ṭhiti so asammoso, yo asammoso so bhiyyobhāvo, yo bhiyyobhāvo taṃ vepullaṃ, yaṃ vepullaṃ "
       "sā bhāvanā, yā bhāvanā sā pāripūrī."] = (
    f"“{cap(LEMMA['ṭhitiyā'])}”. " + SENT["Yā ṭhiti so asammoso, yo asammoso so bhiyyobhāvo, yo bhiyyobhāvo taṃ "
                                          "vepullaṃ, yaṃ vepullaṃ sā bhāvanā, yā bhāvanā sā pāripūrī."])

# ================================================================ 6. Pañhāpucchaka
P = B.P
F.add_item("kusala_eva", ["kusalāyeva"], "chỉ là thiện")                              # Kusalāyeva [new]
F.add_item("na_maggadhipati", ["na maggādhipatino"], "không " + P("maggadhipati"))   # [new]
NV0 = "không nên nói rằng"   # na vattabbā Xti (no dash, no quotes in the Pāli: none added) [new; B.NV without dash]
QT = re.compile(r"^(.+?)(n?)ti(pi)?$")
QFIXES = [("Araṇāti.", "Araṇā.")]   # closing "ti" of the question list (punctuation)
SUBJ9 = {"Vīmaṃsiddhipādo": cap(IDP["vīmaṃsiddhipādo"]), "vīmaṃsiddhipādo": IDP["vīmaṃsiddhipādo"],
         "Cittiddhipādo": cap(IDP["cittiddhipādo"]), "cittiddhipādo": IDP["cittiddhipādo"],
         "Tayo iddhipādā": f"Ba {IDDHIPADA}", "tayo iddhipādā": f"ba {IDDHIPADA}"}
SINGLE9 = {"Vīmaṃsiddhipādo", "vīmaṃsiddhipādo", "Cittiddhipādo", "cittiddhipādo"}


def bare(x, n):
    x = x + ("ṃ" if n else "")
    x = re.sub(r" cā$", " ca", x)
    return T.ITEMS[T.key_of(x)]["p"]


class QX(F.Q):
    def chunk(self, c, state, first):
        subj, one = "", False
        m = self.rx.match(c) if self.subjects else None
        if m:
            subj, one, c = self.subjects[m.group(1)], m.group(1) in self.single, m.group(2)
        elif first:
            c = low(c)
        assert DASH not in c, c
        m = re.match(r"^(siyā )?na vattabb(?:o|ā|aṃ) (.+)$", c)
        if m:
            qm = QT.match(m.group(2))
            vi = f"{NV0} {bare(qm.group(1), qm.group(2))}"
            if m.group(1):
                vi = f"{B.SOMETIMES} {vi}"
            state["nv"] = True
        elif state.get("nv") and c.endswith("tipi"):
            qm = QT.match(c)
            vi = f"{B.OR} {bare(qm.group(1), qm.group(2))}"
        else:
            if c.startswith("siyā "):
                vi = f"{B.SOMETIMES} {T.pred_vi(c[5:], {})}"
            else:
                vi = T.pred_vi(c, {})
                if state.get("nv"):
                    vi = "mà " + vi
            state["nv"] = False
        if not subj:
            return vi
        if (one and not vi.startswith("là ")) or vi.startswith(NV0):
            vi = f"{S.THI} {vi}"
        return f"{subj} {vi}"

    def line(self, t):
        for a, b in QFIXES + [x for x in FIXES if x[0].startswith(("Siyā vipākā", "sāsavā", "āsavasampayuttā"))]:
            if a in t:
                SLIPS.append(f"{a!r} -> {b!r}")
                t = t.replace(a, b)
        out = []
        for sent in re.split(r"(?<=\.) (?=[A-ZĀ])", t):
            assert sent.endswith("."), sent[-40:]
            parts = re.split(r"(, |; |\x01 ?)", sent[:-1].replace("…pe…", B.PE))
            state, vi = {}, []
            for i, x in enumerate(parts):
                if i % 2:
                    vi.append(B.sep_vi(x))
                    if x.startswith(B.PE) or x == "; ":
                        state["nv"] = False
                else:
                    vi.append(self.chunk(x, state, i == 0))
            out.append(cap("".join(vi)) + ".")
        return " ".join(out)


Q78 = QX({}, set())
Q9 = QX(SUBJ9, SINGLE9)

# ================================================================ 7. build
CHAPTERS = (("7-satipatthanavibhango.md", 7), ("8-sammappadhanavibhango.md", 8), ("9-iddhipadavibhango.md", 9))
MODE_RE = re.compile(r"^Kathañca bhikkhu (ajjhattaṃ|bahiddhā|ajjhattabahiddhā) ")


def translate(pali_lines, ch):
    out, section, mode = [], "sutta", ""
    for pl in pali_lines:
        if not pl.strip():
            out.append("")
            continue
        m = S.ID.search(pl)
        t = S.ID.sub("", pl).rstrip()
        if t == "#### Pañhāpucchakaṃ":
            section = "q"
        mm = MODE_RE.match(t)
        if mm:
            mode = mm.group(1)
        if t in LABELS:
            vi = LABELS[t]
        elif section == "q":
            vi = (Q9 if ch == 9 else Q78).line(t)
        else:
            vi = line(t, mode)
        assert pl.count(DASH) + pl.count("—") == vi.count(DASH) and "—" not in vi, ("dash count", t[:70], vi[:90])
        for bad in ("là là", "  ", "….", '"', " ,", " .", ":-", "thì thì", "\x01", " ;", ";;", ",,", "chánh niệm"):
            assert bad not in vi, (bad, vi[:160])
        out.append(vi + (" " + m.group(1) if m else ""))
    return out


def build():
    check_ch3_lists()
    res = {}
    for fn, ch in CHAPTERS:
        pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().rstrip("\n").split("\n")
        res[os.path.join(S.VI_DIR, fn)] = translate(pali, ch)
    return res


def main():
    res = build()
    for path, lines in res.items():
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines).rstrip("\n") + "\n")
        print("OK:", path, "|", len([l for l in lines if l.strip()]), "non-empty lines")
    for s in sorted(set(SLIPS)):
        print("slip:", s)


if __name__ == "__main__":
    main()
