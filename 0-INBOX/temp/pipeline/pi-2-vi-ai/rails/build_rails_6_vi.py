"""Builder for the Vietnamese rails translation of pi-2 (Vibhaṅga, «Phân tích các hiện tượng», plain audience),
chapter 6 (Paṭiccasamuppādavibhaṅgo, «Phân tích sự sinh khởi tùy thuộc vào điều kiện»).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/6-paticcasamuppadavibhango.md (^2-6-0 … ^2-354)
  0-INBOX/temp/pipeline/pi-2-vi-ai/rails/notes-6.md   (new recurring formulas, Pāli = tiếng Việt)

Translated fresh from the Pāli with the locked pi-2 termbase (X-paccayā «X làm điều kiện cho», hetuka «có … làm
nguyên nhân», sampayutta «gắn liền với», nāma / rūpa «phần tinh thần / phần vật chất», pasāda «lòng tin trong sáng»).
Shared strings are imported read-only from the approved sample builder (S) and the chapter 1, 2-3 and 4-5 builders
(K1, K23, K45: the jāti / jarā / maraṇa / soka … definitions of ch. 4, the pi-1 feeling and mind definitions).
Passages that repeat the Dhammasaṅgaṇī reuse the approved pi-1 Vietnamese rails (every such string is marked pi1()
and asserted to occur there by check_pi1(); the Suttanta chain is read from pi-1 ^1-1343). Every Vietnamese line is
checked against its Pāli line for the dash count and for left-over Pāli letters. Importing this module writes nothing.

usage: python -I -X utf8 build_rails_6_vi.py
"""
import pathlib
import re
import sys
import unicodedata

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)
import build_rails_1_vi as K1      # noqa: E402  (importing writes nothing)
import build_rails_2_3_vi as K23   # noqa: E402  (importing writes nothing)
import build_rails_4_5_vi as K45   # noqa: E402  (importing writes nothing)

PART = "6-paticcasamuppadavibhango.md"
PI1_VI = S.ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
NOTES_PATH = RAILS / "notes-6.md"
cap, low = S.cap, K1.low
TATTHA, IS_WHAT, CALLED, CALLED_PL = S.TATTHA, S.IS_WHAT, S.CALLED_SG, S.CALLED_PL
WHICH = K23.WHICH                                   # Yaṃ / Yā / Yo … (definition) «Điều mà là»
SLIPS = []          # source slips met while building (reported)
MISFITS = []        # termbase gaps / misfits / sense choices (reported)
PI1_USED = []       # strings taken from the approved pi-1 Vietnamese rails (checked by check_pi1)


def note(lst, s):
    if s not in lst:
        lst.append(s)


def slip(s):
    note(SLIPS, s)


def misfit(s):
    note(MISFITS, s)


def pi1(s):
    """mark a string as taken unchanged from the approved pi-1 Vietnamese rails (checked by check_pi1)"""
    if s not in PI1_USED:
        PI1_USED.append(s)
    return s


# =========================================================================== the links of the chain (termbase)
N = {
    "avijjā": "vô minh",                                 # Avijjā / Avijjāpaccayā
    "saṅkhāro": "sự tạo tác",                            # saṅkhāro (Abhidhamma method: one formation)
    "saṅkhārā": "các sự tạo tác",                        # saṅkhārā (Suttanta: pi-1 ^1-1343)
    "viññāṇaṃ": "thức",
    "nāmaṃ": "phần tinh thần",                           # nāmaṃ (user pair «phần tinh thần / phần vật chất»)
    "nāmarūpaṃ": "phần tinh thần và vật chất",           # nāmarūpaṃ (termbase; pi-1 ^1-1343)
    "chaṭṭhāyatanaṃ": "lĩnh vực nhận biết thứ sáu",
    "saḷāyatanaṃ": "sáu lĩnh vực nhận biết",
    "phasso": "sự tiếp xúc",
    "vedanā": "cảm giác",
    "taṇhā": "khao khát",
    "upādānaṃ": "sự bám víu",
    "bhavo": "sự hiện hữu",
    "jāti": "sự sinh",
    "jarāmaraṇaṃ": "sự lão hóa và sự chết",
    "adhimokkho": "sự quyết định",                       # adhimokkhapaccayā «sự quyết định làm điều kiện cho»
    "pasādo": "lòng tin trong sáng",                     # pasādo, sense 'clear confidence' (not «chất nhạy cảm»)
    "paṭighaṃ": "sự ác cảm",
    "vicikicchā": "sự hoài nghi",
    "uddhaccaṃ": "sự xao động",
    "kusalamūlā": "các gốc rễ thiện",                    # kusalamūlā «gốc rễ thiện» (plural: the roots)
    "akusalamūlā": "các gốc rễ bất thiện",
}
STEM = {  # compound stem (X-paccayā, X-hetuko, X-sampayutto) -> noun key
    "avijjā": "avijjā", "saṅkhāra": "saṅkhāro", "viññāṇa": "viññāṇaṃ", "nāma": "nāmaṃ", "nāmarūpa": "nāmarūpaṃ",
    "chaṭṭhāyatana": "chaṭṭhāyatanaṃ", "saḷāyatana": "saḷāyatanaṃ", "phassa": "phasso", "vedanā": "vedanā",
    "taṇhā": "taṇhā", "upādāna": "upādānaṃ", "bhava": "bhavo", "jāti": "jāti", "adhimokkha": "adhimokkho",
    "pasāda": "pasādo", "paṭigha": "paṭighaṃ", "vicikicchā": "vicikicchā", "uddhacca": "uddhaccaṃ",
    "kusalamūla": "kusalamūlā", "akusalamūla": "akusalamūlā",
}
COND = "làm điều kiện cho"            # X-paccayā (termbase «X làm điều kiện cho»)
ALSO = "cũng"                          # X-paccayāpi (Aññamaññacatukka) «X cũng làm điều kiện cho»
CAUSE = "có {z} làm nguyên nhân"       # Y X-hetuko (termbase «sự tạo tác có vô minh làm nguyên nhân»; hetu = cause)
CONJ = "gắn liền với {z}"              # Y X-sampayutto (sampayutto «gắn liền», pi-1 «gắn liền với»)
WHEREIN = "trong đó"                   # «nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ»: the part that is conjoined is named

CLAUSE_RX = re.compile(r"^(?P<c>\S+?)paccayā(?P<pi>pi)? (?P<r>\S+)"
                       r"(?: (?P<m>\S+?)(?P<mk>hetuk|sampayutt)(?:o|ā|aṃ))?(?: (?P<w>nāmaṃ|chaṭṭhāyatanaṃ))?$")


def noun(key, sut=False):
    if sut and key == "saṅkhāro":
        key = "saṅkhārā"
    return N[key]


def parse(t):
    m = CLAUSE_RX.match(t)
    assert m, t
    return m


def clause(t, sut=False):
    """«Xpaccayā[pi] Y [Zhetuko|Zsampayutto] [W]» -> «x làm điều kiện cho y …» (lower case)"""
    m = parse(t)
    c = noun(STEM[low(m.group("c"))], sut)
    r = noun(m.group("r"), sut)
    if m.group("pi"):
        return f"{c} {ALSO} {COND} {r}"
    out = f"{c} {COND} {r}"
    z = N[STEM[m.group("m")]] if m.group("m") else None
    if m.group("w"):
        return f"{out}, {WHEREIN} {N[m.group('w')]} {CONJ.format(z=z)}"
    if m.group("mk") == "hetuk":
        out += " " + CAUSE.format(z=z)
    elif m.group("mk") == "sampayutt":
        out += " " + CONJ.format(z=z)
    return out


def moded(t):
    m = parse(t)
    return bool(m.group("mk"))


SEP_RX = re.compile(r"(…pe…\s?|;\s|,\s)")


def chain(text, sut=False):
    """«Avijjāpaccayā saṅkhāro, …, jātipaccayā jarāmaraṇaṃ» (no final punctuation) -> Vietnamese, lower case.
    Clauses that carry a hetuka / sampayutta qualifier are separated by «;» (their inner «, trong đó» needs it)."""
    if "saṅkhārahetukaṃ viññāṇapaccayā" in text:
        text = text.replace("saṅkhārahetukaṃ viññāṇapaccayā", "saṅkhārahetukaṃ, viññāṇapaccayā")
        slip("^2-262 «saṅkhārapaccayā viññāṇaṃ saṅkhārahetukaṃ viññāṇapaccayā nāmarūpaṃ»: comma missing between the "
             "clauses (added, rendered as meant)")
    if "taṇhāpaccayā upādānaṃ upādānasampayuttaṃ" in text:
        slip("^2-245 (4th line) «taṇhāpaccayā upādānaṃ upādānasampayuttaṃ» where the parallel lines have "
             "taṇhāsampayuttaṃ: translated as written «sự bám víu gắn liền với sự bám víu»")
    parts = SEP_RX.split(text)
    clauses, seps = parts[0::2], parts[1::2]
    vi = [clause(c, sut) for c in clauses]
    out = vi[0]
    for i, s in enumerate(seps):
        if s.startswith("…pe…"):
            out += "… "
        elif s.startswith(";") or moded(clauses[i]) or moded(clauses[i + 1]):
            out += "; "
        else:
            out += ", "
        out += vi[i + 1]
    return low(out)


# =========================================================================== fixed strings
EVAM = "như vậy là sự phát sinh của toàn bộ khối khổ đau này"     # Evametassa kevalassa … samudayo hoti (pi-1 ^1-1343)
EVAM_DH = "như vậy là sự phát sinh của những hiện tượng này"       # Evametesaṃ dhammānaṃ samudayo hoti
MEANS = "là sự gần gũi, là sự tụ hợp, là sự xuất hiện"            # samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti
EVAM_MEANS = f"như vậy là sự kết hợp của toàn bộ khối khổ đau này, {MEANS}"   # … saṅgati hoti, …
EVAM_DH_MEANS = f"như vậy là sự kết hợp của những hiện tượng này, {MEANS}"
TOPIC = "Về câu “{x}”:"                 # «X-ti.» (a quoted statement taken up for explanation); next sentence lower case
TENA = "Vì thế, điều này được gọi là"   # Tena vuccati "…"ti (Tena «vì thế», vuccati «được gọi là»)
AT_TIME = "vào lúc ấy"                  # tasmiṃ samaye (termbase samaye «vào lúc ấy»; pi-1)
THEN = "thì vào lúc ấy"                 # …, tasmiṃ samaye (opening frame, pi-1 ^1-1)
NAMA, RUPA = N["nāmaṃ"], "phần vật chất"   # nāmaṃ / rūpaṃ in the nāma-rūpa pair (pi-1 ^1-1316, ^1-1317)
JARA, MARANA = K45.JARA, K45.MARANA     # «sự lão hóa», «sự chết»
KAMMABHAVA = "sự hiện hữu dưới dạng nghiệp"           # kammabhavo (termbase)
UPAPATTIBHAVA = "sự hiện hữu dưới dạng tái sinh"      # upapattibhavo (termbase)
PUNNA = "sự tạo tác thuộc về phước"                    # Puññābhisaṅkhāro (termbase)
APUNNA = "sự tạo tác không thuộc về phước"             # apuññābhisaṅkhāro (termbase)
ANENJA = "sự tạo tác dẫn đến trạng thái bất động"      # āneñjābhisaṅkhāro (termbase)
KAYA_S = "sự tạo tác bằng thân"                        # kāyasaṅkhāro (termbase)
VACI_S = "sự tạo tác bằng lời nói"                     # vacīsaṅkhāro (vacī «lời nói»; no headword)
CITTA_S = "sự tạo tác bằng tâm"                        # cittasaṅkhāro (citta «tâm»; no headword)
ROOTS = {"alobho": "sự không tham lam", "adoso": "sự không sân hận", "amoho": "sự không si mê"}   # pi-1 ^1-32 …
SIMPLE = {  # simple terms of the questions and closings (Pāli nominative) -> Vietnamese
    "avijjā": N["avijjā"], "saṅkhāro": N["saṅkhāro"], "nāmaṃ": NAMA, "rūpaṃ": RUPA, "nāmarūpaṃ": N["nāmarūpaṃ"],
    "jarā": JARA, "maraṇaṃ": MARANA, "soko": K45.SOKA, "paridevo": K45.PARIDEVA, "dukkhaṃ": K45.PAIN,
    "domanassaṃ": K45.DOMANASSA, "upāyāso": K45.UPAYASA, "kammabhavo": KAMMABHAVA, "upapattibhavo": UPAPATTIBHAVA,
    "puññābhisaṅkhāro": PUNNA, "apuññābhisaṅkhāro": APUNNA, "āneñjābhisaṅkhāro": ANENJA, "kāyasaṅkhāro": KAYA_S,
    "kusalamūlā": N["kusalamūlā"], **ROOTS,
}
BHAVA2 = (f"{cap(N['bhavo'])} {K1.by_n(2)} – {S.SOME} là {KAMMABHAVA}, {S.SOME} là {UPAPATTIBHAVA}.")
# Bhavo duvidhena – atthi kammabhavo, atthi upapattibhavo. (as ch. 5 LIFE2 «… theo nhóm hai – có loại là …»)
ALL_KAMMA = f"Mọi nghiệp dẫn đến sự hiện hữu cũng đều là {KAMMABHAVA}."     # Sabbampi bhavagāmikammaṃ kammabhavo.
KAYA3 = (f"Sự cố ý bằng thân là {KAYA_S}, sự cố ý bằng lời nói là {VACI_S}, sự cố ý bằng ý là {CITTA_S}.")
# Kāyasañcetanā kāyasaṅkhāro, vacīsañcetanā vacīsaṅkhāro, manosañcetanā cittasaṅkhāro. (sañcetanā «sự cố ý»)
SANKHARA6 = f"{cap(PUNNA)}, {APUNNA}, {ANENJA}, {KAYA_S}, {VACI_S}, {CITTA_S}."
ROOTS3 = f"{cap(ROOTS['alobho'])}, {ROOTS['adoso']}, {ROOTS['amoho']}"
ROOTS2 = f"{cap(ROOTS['alobho'])}, {ROOTS['adoso']}"

SUBHEAD = {  # ##### headings and their closing labels (termbase: catukkaṃ «bộ bốn», niddeso «giải thích»)
    "Paccayacatukkaṃ": "Bộ bốn về điều kiện",                       # termbase
    "Hetucatukkaṃ": "Bộ bốn về nguyên nhân",                        # catukkaṃ «bộ bốn» + Hetu «nguyên nhân»
    "Sampayuttacatukkaṃ": "Bộ bốn về sự gắn liền",                  # termbase
    "Aññamaññacatukkaṃ": "Bộ bốn về sự tương hỗ",                   # termbase
    "Mātikā": "Ma trận",                                            # termbase
    "Akusalaniddeso": "Giải thích về điều bất thiện",               # niddeso «giải thích», Akusala «bất thiện»
    "Kusalaniddeso": "Giải thích về điều thiện",
    "Abyākataniddeso": "Giải thích về điều không xác định về mặt đạo đức",
    "Avijjāmūlakakusalaniddeso": "Giải thích về điều thiện dựa trên vô minh",        # mūlaka «dựa trên»
    "Kusalamūlakavipākaniddeso": "Giải thích phần quả dựa trên gốc rễ thiện",       # vipākaniddeso «giải thích phần
    "Akusalamūlakavipākaniddeso": "Giải thích phần quả dựa trên gốc rễ bất thiện",  # quả», mūlakavipāka «quả dựa trên»
}
COLOPHON_P = "Paṭiccasamuppādavibhaṅgo [paccayākāravibhaṅgo (sī. syā.)] niṭṭhito."
COLOPHON = (f"{S.CH_HEADINGS['Paṭiccasamuppādavibhaṅgo']} {S.reading('Sī., Syā.', 'paccayākāravibhaṅgo')} "
            f"{K1.DONE}.")
SENT = {  # whole Pāli sentences -> Vietnamese
    "Atthi nāmaṃ, atthi rūpaṃ.": f"Có {NAMA}, có {RUPA}.",
    "Atthi jarā, atthi maraṇaṃ.": f"Có {JARA}, có {MARANA}.",
    "Iti idañca nāmaṃ, idañca rūpaṃ.": f"Như vậy, đây là {NAMA} và đây là {RUPA}.",
    "Iti ayañca jarā, idañca maraṇaṃ.": f"Như vậy, đây là {JARA} và đây là {MARANA}.",
    "Iti ayañca kammabhavo, ayañca upapattibhavo.": f"Như vậy, đây là {KAMMABHAVA} và đây là {UPAPATTIBHAVA}.",
    "Bhavo duvidhena – atthi kammabhavo, atthi upapattibhavo.": BHAVA2,
    "Sabbampi bhavagāmikammaṃ kammabhavo.": ALL_KAMMA,
    "Kāyasañcetanā kāyasaṅkhāro, vacīsañcetanā vacīsaṅkhāro, manosañcetanā cittasaṅkhāro.": KAYA3,
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro, kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāro.": SANKHARA6,
    "Alobho, adoso, amoho.": ROOTS3 + ".",
    "Alobho, adoso.": ROOTS2 + ".",
    "Evametassa kevalassa dukkhakkhandhassa samudayo hoti.": cap(EVAM) + ".",
    "Evametesaṃ dhammānaṃ samudayo hoti.": cap(EVAM_DH) + ".",
    "Evametassa kevalassa dukkhakkhandhassa saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.":
        cap(EVAM_MEANS) + ".",
    "Evametesaṃ dhammānaṃ saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.": cap(EVAM_DH_MEANS) + ".",
    "Suttantabhājanīyaṃ.": K1.FIXED["Suttantabhājanīyaṃ."],
    "Abhidhammabhājanīyaṃ.": K1.FIXED["Abhidhammabhājanīyaṃ."],
    COLOPHON_P: COLOPHON,
}
for _p, _v in SUBHEAD.items():
    SENT[f"{_p}."] = f"{_v}."
SENT[("Evametassa kevalassa dukkhakkhandhassa samudayo hotīti, evametassa kevalassa dukkhakkhandhassa saṅgati hoti, "
      "samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.")] = f"{TOPIC.format(x=EVAM)} {EVAM_MEANS}."   # ^2-242
TOPIC_SENT = {  # «…hotīti.» sentences taken up for explanation (the next sentence starts in lower case)
    "Evametassa kevalassa dukkhakkhandhassa samudayo hotīti.": EVAM,
    "Evametesaṃ dhammānaṃ samudayo hotīti.": EVAM_DH,
}

# =========================================================================== answer bodies (definitions)
SENSES = ["mắt", "tai", "mũi", "lưỡi", "thân", "ý"]
_SP = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "mano"]
VINN6 = ", ".join(K1.VINN[k] for k in _SP)                                    # thức qua mắt … ý thức
AY6 = ", ".join(K23.AY[k] for k in ("cakkhu", "sota", "ghāna", "jivhā", "kāya", "mana"))   # lĩnh vực mắt …
CONTACT6 = ", ".join(f"sự tiếp xúc của {s}" for s in SENSES)                  # termbase Cakkhusamphasso …
FEEL6 = ", ".join(f"cảm giác sinh từ sự tiếp xúc của {s}" for s in SENSES)    # termbase cakkhusamphassajā vedanā …
TANHA6 = pi1("khao khát hình sắc, khao khát âm thanh, khao khát mùi, khao khát vị, khao khát vật xúc chạm, khao khát "
             "đối tượng của ý")                                                # pi-1 ^1-1065 (rūpataṇhā … dhammataṇhā)
UPADANA4 = ("sự bám víu vào dục lạc, sự bám víu vào quan điểm, sự bám víu vào giới hạnh và nghi thức, sự bám víu vào "
            "học thuyết về tự ngã")                                            # termbase Kāmupādānaṃ …
BHAVA9 = ("sự hiện hữu ở cõi dục lạc, sự hiện hữu ở cõi hình sắc, sự hiện hữu ở cõi không hình sắc, sự hiện hữu có tri "
          "giác, sự hiện hữu không có tri giác, sự hiện hữu không phải có tri giác cũng không phải không có tri giác, "
          "sự hiện hữu gồm một khối, sự hiện hữu gồm bốn khối, sự hiện hữu gồm năm khối")
# Kāmabhavo … pañcavokārabhavo: built from bhavo «sự hiện hữu» + kāma/rūpa/arūpa plane «cõi …», asaññā «không có tri
# giác», nevasaññānāsaññā «không phải có tri giác cũng không phải không có tri giác», eka/catu/pañcavokāra «gồm … khối»
KH3 = f"{K1.KH['vedana']}, {K1.KH['sanna']}, {K1.KH['sankhara']}"                # vedanā-, saññā-, saṅkhārakkhandho
KH4 = f"{KH3}, {K1.KH['vinnana']}"
KH3_SNV = f"{K1.KH['sanna']}, {K1.KH['sankhara']}, {K1.KH['vinnana']}"
NOT_KNOW4 = pi1("Sự không biết về khổ đau, sự không biết về sự phát sinh của khổ đau, sự không biết về sự chấm dứt khổ "
                "đau, sự không biết về cách thực hành dẫn đến sự chấm dứt khổ đau")   # pi-1 ^1-1067
MAHABHUTA = pi1("Bốn yếu tố cơ bản và vật chất phái sinh từ bốn yếu tố cơ bản")        # pi-1 ^1-1317
MARANA_V = K45.MARANA_LIST.replace("sự qua đời", "sự qua đời " + S.spell("Ka.", "kālaṃkiriyā"), 1)
PARIDEVA_L = K45.PARIDEVA_LIST.split(" [", 1)[0]    # the ch. 4 list without the ch. 4 variant bracket
MOHA_PE = pi1("Điều mà là sự không biết, sự không thấy… then cài vô minh, sự si mê, tức gốc rễ bất thiện")  # ^1-1318
CETANA3 = pi1("chủ ý, sự cố ý, trạng thái đã cố ý")       # cetanā sañcetanā (sañ)cetayitattaṃ (pi-1 ^1-110)
PHASSA4 = pi1("sự tiếp xúc, sự chạm, sự chạm đến, trạng thái đã chạm đến")      # pi-1 ^1-2
RAGA7 = (pi1("sự tham đắm, sự say đắm, sự chiều theo, sự xuôi theo, sự thích thú, sự tham đắm vì thích thú") + ", "
         + pi1("sự say đắm của tâm"))                                          # pi-1 ^1-1065 (first seven)
DITTHI16 = pi1("quan điểm, sự mắc kẹt trong các quan điểm, rừng rậm quan điểm, hoang mạc quan điểm, sự quanh co của "
               "quan điểm, sự dao động của quan điểm, xiềng xích quan điểm, sự nắm giữ, sự bám chặt, sự cố chấp, sự hiểu "
               "sai lệch, con đường lệch lạc, lối đi sai lầm, sự sai lầm, lĩnh vực của các học thuyết ngoại đạo, sự nắm "
               "giữ điều đảo ngược")                                           # pi-1 ^1-1122
ADHIMOKKHA3 = "sự quyết định của tâm, sự khởi quyết định, trạng thái đã quyết định về điều đó"
# cittassa adhimokkho adhimuccanā tadadhimuttatā (adhimokkha- «sự quyết định», adhimuccanā «sự khởi quyết định»,
# tadadhimuttatā «trạng thái đã quyết định về điều đó»)
SADDHA4 = pi1("niềm tin, sự tin tưởng, sự tin chắc, lòng tin sâu sắc")          # pi-1 ^1-12 (first four)
UDDHACCA4 = pi1("sự xao động của tâm, sự không lắng xuống, sự tán loạn của tâm, trạng thái rối loạn của tâm")  # ^1-429
VICIKICCHA = (pi1("sự nghi ngờ, sự khởi nghi ngờ, trạng thái khởi nghi ngờ, sự phân vân, sự hoài nghi, sự lưỡng lự, sự "
                  "đứng trước ngã ba đường") + " " + S.spell("Sī., Syā.", "dvedhāpatho") + ", "
              + pi1("sự ngờ vực, sự không nắm giữ được điều chắc chắn, sự chần chừ, sự do dự, sự không đi sâu") + " "
              + S.spell("Sī., Syā., Ka.", "apariyogāhanā") + ", " + pi1("trạng thái cứng đờ của tâm, sự giằng xé của ý"))
# pi-1 ^1-425 (chambhitattaṃ here, thambhitattaṃ there: the same termbase word «trạng thái cứng đờ»)
PATIGHA_PE = (pi1("sự oán giận của tâm") + "… " + pi1("sự hung dữ, sự nói năng cộc cằn") + " "
              + S.spell("Syā.", "asulopo") + ", " + pi1("sự không hài lòng của tâm"))      # pi-1 ^1-1066
ALOBHA = pi1("sự không tham lam, sự không khởi lòng tham, trạng thái không khởi lòng tham, sự không say đắm, sự không "
             "bị cuốn hút, trạng thái không bị cuốn hút, sự không thèm muốn, sự không tham lam, tức gốc rễ thiện")  # ^1-32
ADOSA = (pi1("sự không sân hận, sự không khởi sân, trạng thái không khởi sân") + ", "
         + pi1("sự không ác ý, sự không thù hằn, sự không sân hận, tức gốc rễ thiện"))  # pi-1 ^1-33 (without its variant)
PANNA_PATH = f"{K45.PANNA_SHORT}, {pi1('chi phần giác ngộ là sự tìm hiểu các hiện tượng')}, {K45.PATH_TAIL}"
DH_OF = "Điều mà ở từng hiện tượng ấy là"           # Yā/Yo tesaṃ tesaṃ dhammānaṃ … (tesaṃ tesaṃ «từng»)
JATI5 = "sự sinh, sự sinh ra, sự phát khởi, sự hình thành, sự xuất hiện"   # jāti sañjāti nibbatti abhinibbatti pātubhāvo
JARA3 = "sự lão hóa, sự hao mòn, sự suy giảm tuổi thọ"          # jarā jīraṇatā āyuno saṃhāni (pi-1 ^1-643 items)
KHAYA6 = "sự hủy diệt, sự suy tàn, sự tan rã, sự tan rã hoàn toàn, tính vô thường, sự biến mất"
# khayo vayo bhedo paribhedo aniccatā antaradhānaṃ (termbase)
OTHER_CITTAJA = pi1("hoặc còn có bất cứ vật chất nào khác sinh từ tâm, có tâm làm nguyên nhân, do tâm sinh ra")  # ^1-666
UPACAYA5 = ", ".join(f"sự tăng trưởng của {K23.AY[k]}" for k in ("cakkhu", "sota", "ghāna", "jivhā", "kāya"))
# Cakkhāyatanassa upacayo … (upacayo «sự tăng trưởng», pi-1 «sự tăng trưởng của vật chất»)
DEPENDS = "vật chất mà yếu tố ý thức dựa vào để vận hành"   # yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati
# (termbase rūpaṃ nissāya «vật chất mà … dựa vào», vattati «vận hành»)
CITTA_FULL = f"{WHICH} {K23.CITTA_SYN}, {K23.DH['manoviññāṇa']} {K23.TAJJA}"   # pi-1 ^1-6 (… tajjāmanoviññāṇadhātu)
STRUCK_P = ("Ñātibyasanena vā phuṭṭhassa, bhogabyasanena vā phuṭṭhassa, rogabyasanena vā phuṭṭhassa, sīlabyasanena "
            "vā phuṭṭhassa, diṭṭhibyasanena vā phuṭṭhassa, aññataraññatarena byasanena samannāgatassa, "
            "aññataraññatarena dukkhadhammena phuṭṭhassa ")
STRUCK_TAIL = {   # ch. 4 strings (K45)
    "soko socanā socitattaṃ antosoko antoparisoko cetaso parijjhāyanā domanassaṃ sokasallaṃ": K45.SOKA_LIST,
    ("ādevo paridevo ādevanā paridevanā ādevitattaṃ paridevitattaṃ vācā palāpo vippalāpo lālappo lālappanā "
     "lālappitattaṃ"): PARIDEVA_L,
    "āyāso upāyāso āyāsitattaṃ upāyāsitattaṃ": K45.UPAYASA_LIST,
}
FEEL = K23.FEELING_P1
BODY = {  # Pāli answer body (before « – ayaṃ/idaṃ/ime vuccati») -> Vietnamese
    # Suttantabhājanīya
    ("Dukkhe aññāṇaṃ, dukkhasamudaye aññāṇaṃ, dukkhanirodhe aññāṇaṃ, dukkhanirodhagāminiyā paṭipadāya aññāṇaṃ"):
        NOT_KNOW4,
    "Kusalā cetanā kāmāvacarā rūpāvacarā dānamayā sīlamayā bhāvanāmayā":
        ("Chủ ý thiện thuộc cõi dục lạc, thuộc cõi hình sắc, hình thành từ sự bố thí, hình thành từ giới hạnh, hình "
         "thành từ sự tu tập"),
    "Akusalā cetanā kāmāvacarā": "Chủ ý bất thiện thuộc cõi dục lạc",
    "Kusalā cetanā arūpāvacarā": "Chủ ý thiện thuộc cõi không hình sắc",
    "Cakkhuviññāṇaṃ, sotaviññāṇaṃ, ghānaviññāṇaṃ, jivhāviññāṇaṃ, kāyaviññāṇaṃ, manoviññāṇaṃ": cap(VINN6),
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho": cap(KH3),
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho": cap(KH4),
    "Cattāro mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ": MAHABHUTA,
    "Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, manāyatanaṃ": cap(AY6),
    "Cakkhusamphasso sotasamphasso ghānasamphasso jivhāsamphasso kāyasamphasso manosamphasso": cap(CONTACT6),
    ("Cakkhusamphassajā vedanā, sotasamphassajā vedanā, ghānasamphassajā vedanā, jivhāsamphassajā vedanā, "
     "kāyasamphassajā vedanā, manosamphassajā vedanā"): cap(FEEL6),
    "Rūpataṇhā, saddataṇhā, gandhataṇhā, rasataṇhā, phoṭṭhabbataṇhā, dhammataṇhā": cap(TANHA6),
    "Kāmupādānaṃ, diṭṭhupādānaṃ, sīlabbatupādānaṃ, attavādupādānaṃ": cap(UPADANA4),
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro": f"{cap(PUNNA)}, {APUNNA}, {ANENJA}",
    ("Kāmabhavo, rūpabhavo, arūpabhavo, saññābhavo, asaññābhavo, nevasaññānāsaññābhavo, ekavokārabhavo, "
     "catuvokārabhavo, pañcavokārabhavo"): cap(BHAVA9),
    ("Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jāti sañjāti okkanti abhinibbatti, khandhānaṃ pātubhāvo, "
     "āyatanānaṃ paṭilābho"): f"Điều mà, {K45.EACH}, là {K45.JATI_LIST}",      # ch. 4 ^2-190 …
    ("Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni "
     "indriyānaṃ paripāko"): f"Điều mà, {K45.EACH}, là {K45.JARA_LIST}",
    ("Yā tesaṃ tesaṃ sattānaṃ tamhā tamhā sattanikāyā cuti cavanatā bhedo antaradhānaṃ maccu maraṇaṃ kālakiriyā "
     "[kālaṃkiriyā (ka.)] khandhānaṃ bhedo kaḷevarassa nikkhepo jīvitindriyassupacchedo"):
        f"Điều mà, đối với từng chúng sinh, là {MARANA_V}",
    ("Yaṃ kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā "
     "vedanā"): f"{WHICH} {FEEL['dukkha']}",
    ("Yaṃ cetasikaṃ asātaṃ, cetasikaṃ dukkhaṃ, cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ, cetosamphassajā asātā "
     "dukkhā vedanā"): f"{WHICH} {FEEL['domanassa']}",
    # Abhidhammabhājanīya
    "Yaṃ aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusalamūlaṃ": MOHA_PE,
    "Yaṃ aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusamūlaṃ": MOHA_PE,           # ^2-276 slip (reported)
    "Yā cetanā sañcetanā sañcetayitattaṃ": f"{WHICH} {CETANA3}",
    "Yā cetanā sañcetanā sañcetayitattaṃ [cetayitattaṃ (sī. ka.)]":
        f"{WHICH} {CETANA3} {S.reading('Sī., Ka.', 'cetayitattaṃ')}",
    ("Yaṃ cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
     "tajjāmanoviññāṇadhātu"): CITTA_FULL,
    "Yo phasso phusanā samphusanā samphusitattaṃ": f"{WHICH} {PHASSA4}",
    "Yaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        f"{WHICH} {FEEL['somanassa']}",
    ("Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā "
     "vedanā"): f"{WHICH} {FEEL['upekkhā']}",
    ("Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ, cetosamphassajā adukkhamasukhā "
     "vedanā"): f"{WHICH} {FEEL['upekkhā']}",
    ("Yaṃ cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā "
     "vedanā"): f"{WHICH} {FEEL['domanassa']}",
    "Yaṃ kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā":
        f"{WHICH} {FEEL['sukha']}",
    "Yo rāgo sārāgo anunayo anurodho nandī nandirāgo cittassa sārāgo": f"{WHICH} {RAGA7}",
    "Yo rāgo sārāgo…pe… cittassa sārāgo": f"{WHICH} sự tham đắm, sự say đắm… sự say đắm của tâm",
    "Yo rāgo…pe… cittassa sārāgo": f"{WHICH} sự tham đắm… sự say đắm của tâm",
    ("Yā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho "
     "patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho "
     "[vipariyesaggāho (bahūsu)]"): f"{WHICH} {DITTHI16} {S.spell('nhiều ấn bản', 'vipariyesaggāho')}",
    "Yā diṭṭhi diṭṭhigataṃ…pe… titthāyatanaṃ vipariyāsaggāho":
        (f"{WHICH} quan điểm, sự mắc kẹt trong các quan điểm… lĩnh vực của các học thuyết ngoại đạo, sự nắm giữ điều "
         f"đảo ngược"),
    "Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbatti pātubhāvo": f"{DH_OF} {JATI5}",
    "Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbati pātubhāvo": f"{DH_OF} {JATI5}",   # ^2-273 slip
    "Yā tesaṃ tesaṃ dhammānaṃ jarā jīraṇatā āyuno saṃhāni": f"{DH_OF} {JARA3}",
    "Yo tesaṃ tesaṃ dhammānaṃ khayo vayo bhedo paribhedo aniccatā antaradhānaṃ": f"{DH_OF} {KHAYA6}",
    ("Cakkhāyatanassa upacayo, sotāyatanassa upacayo, ghānāyatanassa upacayo, jivhāyatanassa upacayo, "
     "kāyāyatanassa upacayo, yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ"):
        f"{cap(UPACAYA5)}, {OTHER_CITTAJA}",
    "Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati": cap(DEPENDS),
    "Cattāro ca mahābhūtā, yañca rūpaṃ nissāya manoviññāṇadhātu vattati": f"Bốn yếu tố cơ bản và {DEPENDS}",
    "Yo cittassa adhimokkho adhimuccanā tadadhimuttatā": f"{WHICH} {ADHIMOKKHA3}",
    "Yā saddhā saddahanā okappanā abhippasādo": f"{WHICH} {SADDHA4}",
    "Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": f"{WHICH} {UDDHACCA4}",
    "Yo cittassa āghāto…pe… caṇḍikkaṃ asuropo [asulopo (syā.)] anattamanatā cittassa": f"{WHICH} {PATIGHA_PE}",
    ("Yā kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvidhāpatho [dvedhāpatho (sī. syā.)] saṃsayo "
     "anekaṃsaggāho āsappanā parisappanā apariyogāhaṇā [apariyogāhanā (sī. syā. ka.)] chambhitattaṃ cittassa "
     "manovilekho"): f"{WHICH} {VICIKICCHA}",
    "Yo alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ":
        f"{WHICH} {ALOBHA}",
    "Yo adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ": f"{WHICH} {ADOSA}",
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": f"{WHICH} {K45.PANNA_SHORT}",
    ("Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"):
        f"{WHICH} {PANNA_PATH}",
    "Alobho, adoso, amoho": ROOTS3,
    "Alobho, adoso": ROOTS2,
}
EXCEPT = {"upādānaṃ": N["upādānaṃ"], "phassaṃ": N["phasso"], "adhimokkhaṃ": N["adhimokkho"],
          "vicikicchaṃ": N["vicikicchā"], "vedanaṃ": N["vedanā"]}     # Ṭhapetvā X «Ngoại trừ X ra» (pi-1 ^1-1122)
for _x, _v in EXCEPT.items():
    _rest_p = ("saññākkhandho saṅkhārakkhandho viññāṇakkhandho" if _x == "vedanaṃ"
               else "vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho")
    BODY[f"Ṭhapetvā {_x}, {_rest_p}"] = f"Ngoại trừ {_v} ra, {KH3_SNV if _x == 'vedanaṃ' else KH4}"
BODY["Ṭhapetvā adhimokkhaṃ, vedanākkhandho saññākkhandho saṅkhārakkhandho, viññāṇakkhandho"] = \
    f"Ngoại trừ {EXCEPT['adhimokkhaṃ']} ra, {KH4}"                     # ^2-318 extra comma (same Vietnamese)
CITTA_PE_RX = re.compile(r"^Yaṃ cittaṃ mano mānasaṃ ?…pe… tajjā(\S+?)dhātu$")


def body_vi(b, sid):
    if "akusamūlaṃ" in b:
        slip(f"^{sid} «avijjālaṅgī moho akusamūlaṃ» (akusa- for akusala-): plain spelling slip, rendered as meant "
             f"«gốc rễ bất thiện»")
    if "abhinibbati " in b:
        slip(f"^{sid} «nibbatti abhinibbati» (abhinibbatti elsewhere; the termbase has both, «sự hình thành»): same "
             f"Vietnamese")
    if b in BODY:
        return BODY[b]
    m = CITTA_PE_RX.match(b)
    if m:
        if "mānasaṃ …pe…" in b:
            slip(f"^{sid} «mānasaṃ …pe…»: space before …pe… (ignored)")
        return f"{WHICH} {K23.CITTA_SHORT} {K23.DH[m.group(1)]} {K23.TAJJA}"
    if b.startswith(STRUCK_P):
        return f"{K45.AFFLICT} {STRUCK_TAIL[b[len(STRUCK_P):]]}"
    raise KeyError(b)


# =========================================================================== mind-type openers (pi-1 wording)
KIND_Q = {"akusalā": pi1("Những hiện tượng nào là bất thiện?"), "kusalā": pi1("Những hiện tượng nào là thiện?"),
          "abyākatā": pi1("Những hiện tượng nào không xác định về mặt đạo đức?")}   # pi-1 ^1-365, ^1-1, ^1-431
WHEN = "Vào lúc"                                    # Yasmiṃ samaye (pi-1)
ARISES = "sinh khởi"                                # uppannaṃ / uppannā hoti (pi-1 «… sinh khởi»)
SUBJ = {  # <X> uppann(aṃ|ā) hoti (pi-1 ^1-365, ^1-1, ^1-431, ^1-455, ^1-469)
    "akusalaṃ cittaṃ": "tâm bất thiện", "kāmāvacaraṃ kusalaṃ cittaṃ": "tâm thiện thuộc cõi dục lạc",
    "cakkhuviññāṇaṃ": K1.VINN["cakkhu"], "sotaviññāṇaṃ": K1.VINN["sota"], "ghānaviññāṇaṃ": K1.VINN["ghāna"],
    "jivhāviññāṇaṃ": K1.VINN["jivhā"], "kāyaviññāṇaṃ": K1.VINN["kāya"],
    "manodhātu": K23.DH["mano"], "manoviññāṇadhātu": K23.DH["manoviññāṇa"],
}
SAHA = {"somanassa": "có niềm vui đi kèm", "upekkhā": "có sự bình thản đi kèm", "domanassa": "có nỗi buồn đi kèm",
        "sukha": "có sự dễ chịu đi kèm", "dukkha": "có sự khó chịu đi kèm"}      # pi-1 ^1-1, 150, 413, 443, 556
SAMP = {"diṭṭhigata": "sự mắc kẹt trong các quan điểm", "paṭigha": "sự ác cảm", "vicikicchā": "sự hoài nghi",
        "uddhacca": "sự xao động", "ñāṇa": "hiểu biết"}                        # «gắn liền với …» (pi-1)
OBJ = {"rūpa": "hình sắc", "sadda": "âm thanh", "gandha": "mùi", "rasa": "vị", "phoṭṭhabba": "vật xúc chạm",
       "dhamma": "đối tượng của ý"}
KAMMA = {"kāmāvacarassa kusalassa": pi1("là quả của nghiệp thiện thuộc cõi dục lạc đã được tạo và tích lũy"),
         "akusalassa": pi1("là quả của nghiệp bất thiện đã được tạo và tích lũy")}   # pi-1 ^1-431, ^1-556
FUNCTIONAL_Q = pi1("mang tính chức năng, không phải thiện, không phải bất thiện, cũng không phải quả của nghiệp")
PROMPTED = "có sự thúc đẩy"                          # sasaṅkhārena (pi-1)
ANY_OBJ = pi1("hoặc lấy bất cứ thứ gì làm đối tượng")      # yaṃ yaṃ vā panārabbha


def quals(body):
    """the qualifier string after «Yasmiṃ samaye» (pi-1 ^1-399 / ^1-431 / ^1-498 / ^1-556 shapes): pieces joined by
    «… », items inside a piece by «, »"""
    m = re.match(r"^(kāmāvacarassa kusalassa|akusalassa) kammassa katattā upacitattā (.*)$", body)
    kamma = None
    if m:
        kamma, body = KAMMA[m.group(1)], m.group(2)
    out = []
    for n, piece in enumerate(p.strip() for p in body.split("…pe…")):
        toks, i, vi, objs = piece.split(" "), 0, [], 0
        while i < len(toks):
            rest = " ".join(toks[i:])
            ms = re.match(r"^(vipākaṃ |vipākā )?(akusalaṃ cittaṃ|kāmāvacaraṃ kusalaṃ cittaṃ|\S+viññāṇaṃ|manodhātu|"
                          r"manoviññāṇadhātu) uppann(?:aṃ|ā) hoti", rest)
            if ms:
                vi.append(f"{SUBJ[ms.group(2)]} {ARISES}")
                if kamma and n == 0:
                    vi.append(kamma)
                i += len(ms.group(0).split(" "))
                continue
            if rest.startswith("kiriyā neva kusalā nākusalā na ca kammavipākā"):
                vi.append(FUNCTIONAL_Q)
                i += 7
                continue
            t = toks[i]
            mt = re.match(r"^(\S+?)sahagat(?:aṃ|ā)$", t)
            if mt:
                vi.append(SAHA[mt.group(1)])
                i += 1
                continue
            mt = re.match(r"^(\S+?)(sampayutt|vippayutt)(?:aṃ|ā)$", t)
            if mt:
                neg = "không " if mt.group(2) == "vippayutt" else ""
                vi.append(f"{neg}gắn liền với {SAMP[mt.group(1)]}")
                i += 1
                continue
            if t == "sasaṅkhārena":
                vi.append(PROMPTED)
                i += 1
                continue
            mt = re.match(r"^(\S+?)ārammaṇ(?:aṃ|ā)$", t)
            if mt:
                o = OBJ[mt.group(1) + "a"]                    # rūp + a … (rūpārammaṇa)
                vi.append(f"có đối tượng là {o}" if objs == 0 and vi else f"hay {o}")
                objs += 1
                i += 1
                if i < len(toks) and toks[i] == "vā":
                    i += 1
                continue
            if rest == "yaṃ yaṃ vā panārabbha":
                vi.append(ANY_OBJ)
                break
            raise ValueError((t, piece))
        out.append(", ".join(vi))
    return "… ".join(out)


# jhāna openers: pi-1 ^1-160 / ^1-268 / ^1-277 / ^1-345 / ^1-499 / ^1-501 / ^1-505 / ^1-577 / ^1-579 wording
J1 = pi1("hoàn toàn tách khỏi các dục lạc… chứng nhập và an trú tầng thiền thứ nhất")
J4 = pi1("hoàn toàn vượt qua lĩnh vực không có gì cả, có tri giác về lĩnh vực không phải tri giác cũng không phải "
         "không tri giác đi kèm, nhờ dứt bỏ sự dễ chịu… chứng nhập và an trú tầng thiền thứ tư")
KASINA = pi1("với đề mục bao trùm là đất")
KASINA_V = " " + S.spell("Sī., Syā.", "paṭhavīkasiṇaṃ")
MODE = pi1("với cách thực hành khó khăn và sự hiểu biết trực tiếp chậm chạp")
EMPTY = pi1("có tính chất trống rỗng")              # suññataṃ
RUPA_PATH = pi1("Vào lúc một người tu tập con đường dẫn đến tái sinh vào cõi hình sắc")
ARUPA_PATH = pi1("Vào lúc một người tu tập con đường dẫn đến tái sinh vào cõi không hình sắc")
SUPRA = pi1("Vào lúc một người tu tập tầng thiền vượt thế gian dẫn đến giải thoát và dẫn đến sự giảm trừ, để dứt bỏ sự "
            "mắc kẹt trong các quan điểm, để đạt đến giai đoạn thứ nhất")
KIRIYA_R = pi1("Vào lúc một người tu tập tầng thiền thuộc cõi hình sắc, mang tính chức năng, không phải thiện, không phải "
               "bất thiện, cũng không phải quả của nghiệp, để an trú trong hạnh phúc ngay trong đời này")
KIRIYA_A = pi1("Vào lúc một người tu tập tầng thiền thuộc cõi không hình sắc, mang tính chức năng, không phải thiện, "
               "không phải bất thiện, cũng không phải quả của nghiệp, để an trú trong hạnh phúc ngay trong đời này")
ALSO_WHEN = pi1("Còn khi một người")                 # Tasseva … vipākaṃ … (pi-1 ^1-499)
OF_RUPA = pi1("là quả của chính nghiệp thiện thuộc cõi hình sắc ấy đã được tạo và tích lũy")
OF_ARUPA = pi1("là quả của chính nghiệp thiện thuộc cõi không hình sắc ấy đã được tạo và tích lũy")
OF_LOK = pi1("là quả của chính tầng thiền thiện vượt thế gian ấy đã được tạo và tu tập")
P_J1 = "vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati"
P_J4 = ("sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… catutthaṃ "
        "jhānaṃ upasampajja viharati")
P_SUPRA = "lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā"
P_KIR = "jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ"
JHANA = {  # Pāli after «Yasmiṃ samaye» -> Vietnamese (sentence start)
    f"rūpūpapattiyā maggaṃ bhāveti {P_J1} pathavīkasiṇaṃ [paṭhavīkasiṇaṃ (sī. syā.)]":
        f"{RUPA_PATH}, {J1}, {KASINA}{KASINA_V}",
    f"rūpūpapattiyā maggaṃ bhāveti {P_J1} pathavīkasiṇaṃ": f"{RUPA_PATH}, {J1}, {KASINA}",
    f"arūpūpapattiyā maggaṃ bhāveti {P_J4}": f"{ARUPA_PATH}, {J4}",
    f"{P_SUPRA} {P_J1} dukkhapaṭipadaṃ dandhābhiññaṃ": f"{SUPRA}, {J1}, {MODE}",
    f"rūpāvacaraṃ {P_KIR} {P_J1} pathavīkasiṇaṃ": f"{KIRIYA_R}, {J1}, {KASINA}",
    f"arūpāvacaraṃ {P_KIR} {P_J4}": f"{KIRIYA_A}, {J4}",
}
TASSEVA = {
    f"Tasseva rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ {P_J1} pathavīkasiṇaṃ":
        f"{ALSO_WHEN} {J1}, {KASINA}, {OF_RUPA}",
    f"Tasseva arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ {P_J4}": f"{ALSO_WHEN} {J4}, {OF_ARUPA}",
    f"Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ {P_J1} dukkhapaṭipadaṃ dandhābhiññaṃ":
        f"{ALSO_WHEN} {J1}, {MODE}, {OF_LOK}",
    f"Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ {P_J1} dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ":
        f"{ALSO_WHEN} {J1}, {MODE}, {EMPTY}, {OF_LOK}",
}
CONTACT_PE = pi1("có sự tiếp xúc… có sự không tán loạn")        # phasso hoti…pe… avikkhepo hoti (pi-1)
ARE_KUSALA = pi1("những hiện tượng này là thiện")                 # ime dhammā kusalā (pi-1)
KUSALA_TAIL = "phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā."


def head(p, sid):
    """«Katame dhammā X? Yasmiṃ samaye …» / «Tasseva …» (everything before «, tasmiṃ samaye») -> Vietnamese"""
    if "kāmehi …pe…" in p:
        p = p.replace("kāmehi …pe…", "kāmehi…pe…")
        slip(f"^{sid} «vivicceva kāmehi …pe…»: space before …pe… (ignored)")
    if p in TASSEVA:
        return TASSEVA[p]
    m = re.match(r"^Katame dhammā (\S+)\? Yasmiṃ samaye (.*)$", p)
    assert m, p
    kind, body = m.groups()
    if body in JHANA:
        return f"{KIND_Q[kind]} {JHANA[body]}"
    return f"{KIND_Q[kind]} {WHEN} {quals(body)}"


# =========================================================================== chain lines
SUTTA_CHAIN_P = ("Avijjāpaccayā saṅkhārā, saṅkhārapaccayā viññāṇaṃ, viññāṇapaccayā nāmarūpaṃ, nāmarūpapaccayā "
                 "saḷāyatanaṃ, saḷāyatanapaccayā phasso, phassapaccayā vedanā, vedanāpaccayā taṇhā, taṇhāpaccayā "
                 "upādānaṃ, upādānapaccayā bhavo, bhavapaccayā jāti, jātipaccayā jarāmaraṇaṃ "
                 "sokaparidevadukkhadomanassupāyāsā sambhavanti. Evametassa kevalassa dukkhakkhandhassa samudayo hoti.")


def sutta_chain():
    """pi-1 ^1-1343: «“Vô minh làm điều kiện cho các sự tạo tác, … sinh khởi; như vậy là … này”» -> the chain part"""
    t = K23.p1("1-1343")
    i = t.index("“Vô minh làm điều kiện cho các sự tạo tác")
    j = t.index(f"; {EVAM}”", i)
    return t[i + 1:j]


def chain_line(text, sut=False):
    """«<chain>. Evame… hoti.» -> Vietnamese (lower case start)"""
    m = re.match(r"^(.*?)\. (Evame\S+ .*)$", text)
    assert m, text
    return f"{chain(m.group(1), sut)}. {SENT[m.group(2)]}"


# =========================================================================== sentences of the definitions
Q_RX = re.compile(r"^Tattha (?:katamo|katamā|katamaṃ|katame) (.+?)(\?)?$")
A_RX = re.compile(r"^(.*) – (ayaṃ|idaṃ|ime) (vuccati|vuccanti) (– )?(.*)$")
V_RX = re.compile(r"^(ayaṃ|idaṃ|ime|Ayaṃ|Idaṃ|Ime) (vuccati|vuccanti) (– )?(.*)$")
T_RX = re.compile(r"^[Tt]ena vuccati (.*)$")
TOPIC_RX = re.compile(r"^(\S+paccayā(?:pi)? .*?)(n?)ti\.$")


def term_vi(t, sut):
    """a term (chain statement or simple name) -> Vietnamese, lower case"""
    return clause(t, sut) if "paccayā" in t else SIMPLE[t]


def called(raw, pron, dash, sid, sut):
    """«"X".» / «X.» / «"X"…pe…» … after «ayaṃ/idaṃ/ime vuccati [–]» -> «đó được gọi là “x”.»"""
    m = re.match(r"^(.*?)(…pe…)?(\.?)$", raw)
    t, pe, dot = m.groups()
    q1, q2 = t.startswith('"'), t.endswith('"')
    t = t.strip('"').rstrip(".")
    if q1 != q2:
        slip(f"^{sid} «… vuccati {raw[:50]}»: one quotation mark missing (missing punctuation, rendered with both)")
    if not (q1 or q2):
        slip(f"^{sid} «… vuccati {t}» without quotation marks: kept without “ ”")
    term = term_vi(t, sut)
    term = f"“{term}”" if (q1 or q2) else term
    tail = "…" if pe else ("." if (dot or raw.endswith('.')) else "")
    return f"{CALLED_PL if pron == 'ime' else CALLED} {'– ' if dash else ''}{term}{tail}"


def tena(raw, sid):
    m = re.match(r'^("?)(evametassa kevalassa dukkhakkhandhassa samudayo hot[īi]|evametesaṃ dhammānaṃ samudayo hotī)'
                 r'"ti\.$', raw)
    assert m, raw
    if not m.group(1):
        slip(f"^{sid} «Tena vuccati evametassa … hotī\"ti»: opening quotation mark missing (rendered with both)")
    if m.group(2).endswith("hoti"):
        slip(f"^{sid} «…samudayo hoti\"ti» (hotī elsewhere): the same Vietnamese")
    phrase = EVAM_DH if "evametesaṃ" in m.group(2) else EVAM
    return f"{TENA} “{phrase}”."


def piece(p, sid, sut, first):
    """one fragment of a sentence (fragments are joined by …pe…)"""
    m = T_RX.match(p)
    if m:
        r = tena(m.group(1), sid)
        return r if p[0] == "T" else low(r)
    m = V_RX.match(p)
    if m:
        r = called(m.group(4), low(m.group(1)), m.group(3), sid, sut)
        return cap(r) if p[0].isupper() else r
    m = A_RX.match(p)
    if m:
        body, pron, _, dash, raw = m.groups()
        return f"{body_vi(body, sid)} – {called(raw, pron, dash, sid, sut)}"
    m = Q_RX.match(p)
    if m:
        t, qm = m.groups()
        names = [x.strip() for x in t.split("…pe…")]
        qm = "?" if qm else ""
        if len(names) == 1 and "paccayā" in names[0]:
            return f"{TATTHA} thế nào là “{clause(names[0], sut)}”{qm}"   # (ch. 4 stmt_q)
        return f"{TATTHA} {'… '.join(SIMPLE[x] for x in names)} {IS_WHAT[:-1]}{qm}"
    if not first:
        return f"“{term_vi(p, sut)}”"                # a bare term inside a …pe… run of questions
    raise KeyError(p)


SPLIT_RX = re.compile(r"(?<=[.?])\s+(?=[A-ZĀĪŪṬÑṆḌḶṂ])")


def sentence(s, sid, sut):
    """-> (Vietnamese, topic flag: the next sentence starts in lower case)"""
    if s in SENT:
        return SENT[s], False
    if s in TOPIC_SENT:
        return TOPIC.format(x=TOPIC_SENT[s]), True
    m = TOPIC_RX.match(s)
    if m:
        t = m.group(1) + ("ṃ" if m.group(2) else "")
        return TOPIC.format(x=clause(t, sut)), True
    if '" …pe…' in s:
        s = s.replace('" …pe…', '"…pe…')
        slip(f"^{sid} «\" …pe…»: space before …pe… (ignored)")
    if s.startswith("Tattha katam") and "?" not in s:
        frags = [x.strip() for x in re.split(r"…pe…", s)]
        frags = [x for x in frags if x]
    else:
        frags = [x.strip() for x in re.split(r"…pe…\s?(?=(?:tena|ayaṃ|idaṃ) vuccati)", s)]
    return "… ".join(piece(f, sid, sut, i == 0) for i, f in enumerate(frags)), False


def def_line(ln, sid, sut):
    out, lower_next = [], False
    for s in SPLIT_RX.split(ln):
        v, topic = sentence(s, sid, sut)
        out.append(low(v) if lower_next else v)
        lower_next = topic
    assert not lower_next, ln
    return " ".join(out)


# =========================================================================== lines and chapter
OPEN_RX = re.compile(r"^((?:Katame dhammā \S+\? Yasmiṃ samaye|Tasseva) .*?), tasmiṃ samaye (.*)$")


def line6(ln, sid, section):
    sut = section == "Suttantabhājanīyaṃ"
    if ln in SENT:
        return SENT[ln]
    if ln == SUTTA_CHAIN_P:
        return f"{sutta_chain()}. {cap(EVAM)}."
    m = OPEN_RX.match(ln)
    if m:
        h, rest = m.groups()
        if rest == KUSALA_TAIL:
            return f"{head(h, sid)}, {THEN} {CONTACT_PE} – {ARE_KUSALA}."
        return f"{head(h, sid)}, {THEN} {chain_line(rest)}"
    m = re.match(r"^Tasmiṃ samaye (.*)$", ln)
    if m:
        return f"{cap(AT_TIME)}, {chain_line(m.group(1))}"
    if re.match(r"^(Avijjāpaccayā|Saṅkhārapaccayā avijjā)", ln):
        return cap(chain_line(ln))
    return def_line(ln, sid, sut)


def heading(ln):
    lvl, text = ln.split(" ", 1)
    t = {"Paṭiccasamuppādavibhaṅgo": S.CH_HEADINGS["Paṭiccasamuppādavibhaṅgo"]}
    t.update(S.SEC_HEADINGS)
    t.update(SUBHEAD)
    return f"{lvl} {t[text]}"


FOREIGN = re.compile(r"[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶfjwzFJWZ]")


def dashes(s):
    return s.count("–") + s.count("—")


def check_line(sid, p, v):
    assert dashes(p) == dashes(v), (sid, "dash count", dashes(p), dashes(v), v[:160])
    assert ":-" not in v and "—" not in v and "…." not in v, (sid, v[:160])
    body = re.sub(r"\[[^\]]*\]", "", v)
    assert not FOREIGN.search(body), (sid, FOREIGN.search(body).group(0), v[:200])
    assert "  " not in v and not v.endswith(" "), (sid, v[:160])
    assert v.count("“") == v.count("”"), (sid, "quotes", v[:200])
    if not p.startswith("#"):
        if p.endswith("…pe…") or p.endswith("…pe…."):
            assert v.endswith("…"), (sid, v[-40:])
        else:
            assert v[-1] in ".?!" or v.endswith("”."), (sid, v[-40:])


def build():
    pali = (S.PALI / PART).read_text(encoding="utf-8")
    h, section = {}, None
    for sid, lines in K1.segs(pali):
        lines = [K1.ID.sub("", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            text = lines[0].split(" ", 1)[1]
            if text in ("Suttantabhājanīyaṃ", "Abhidhammabhājanīyaṃ"):
                section = text
            h[sid] = [heading(lines[0])]
            continue
        h[sid] = [line6(ln, sid, section) for ln in lines]
    for sid, lines in K1.segs(pali):
        for p, v in zip([K1.ID.sub("", ln) for ln in lines], h[sid]):
            check_line(sid, p, v)
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


# =========================================================================== pi-1 check
def check_pi1():
    """every string marked pi1() must occur in the approved pi-1 Vietnamese rails (first letter either case)"""
    text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(PI1_VI.glob("*.md")))
    missing = [s for s in PI1_USED if s not in text and cap(s) not in text and low(s) not in text]
    assert not missing, missing
    assert f"{EVAM}”" in text
    return len(PI1_USED)


misfit("samāgamo (^2-242, 249, 273, 305, 354: «… saṅgati hoti, samāgamo hoti …» of the mass of suffering): the only "
       "termbase sense is 'meeting, association with' «sự gần gũi»; kept (as ch. 4 ^2-199), though 'coming together' "
       "fits the context better")
misfit("rūpataṇhā (^2-232 rūpa-, sadda- … dhammataṇhā = craving for visible forms …): the termbase sense 'craving for "
       "the fine-material sphere' «khao khát cõi hình sắc» does not fit; «khao khát hình sắc» as ch. 4 and pi-1 ^1-1065")
misfit("dānamayā sīlamayā bhāvanāmayā (^2-226): no entry for -maya; built «hình thành từ sự bố thí / giới hạnh / sự tu "
       "tập» from dāna «sự bố thí», bhāvanā «sự tu tập»")
misfit("vacīsaṅkhāro, cittasaṅkhāro, kāya-/vacī-/manosañcetanā (^2-226): no headwords; built like kāyasaṅkhāro «sự "
       "tạo tác bằng thân»: «sự tạo tác bằng lời nói / bằng tâm», «sự cố ý bằng thân / bằng lời nói / bằng ý»")
misfit("kāmabhavo … pañcavokārabhavo (^2-234), bhavagāmikammaṃ: no headwords; built from bhavo «sự hiện hữu», the plane "
       "«cõi …», asaññā, nevasaññānāsaññā, eka/catu/pañcavokāra «gồm một / bốn / năm khối», gāmi «dẫn đến»")
misfit("adhimokkho (^2-280 …): no headword; «sự quyết định» from adhimokkhapaccayā «sự quyết định làm điều kiện cho»")
misfit("vuccati in «Tena vuccati \"…\"ti» (it is said): only the closing-formula sense «được gọi là»; written «Vì thế, "
       "điều này được gọi là “…”»")
misfit("hetuka in the Hetucatukka: the dependent-origination sense «có … làm nguyên nhân» (not «có gốc rễ»); the "
       "heading «Bộ bốn về nguyên nhân» from catukkaṃ «bộ bốn» + Hetu «nguyên nhân»")


# =========================================================================== notes
def notes_md():
    ex = "avijjāpaccayā saṅkhāro"
    L = ["# pi-2 Vietnamese rails: new formulas of chapter 6 (^2-6-0 … ^2-354)", "",
         "Generated by build_rails_6_vi.py; import it instead of retyping. Strings already in vi-rails-formulas.md "
         "(sample), notes-1.md, notes-2-3.md or notes-4-5.md are not repeated. Format: Pāli = tiếng Việt.", "",
         "## Headings and closing labels", "",
         f"### Paṭiccasamuppādavibhaṅgo = ### {S.CH_HEADINGS['Paṭiccasamuppādavibhaṅgo']}",
     ] + [f"##### {k} = ##### {v} (closing label «{k}.» = «{v}.»)" for k, v in SUBHEAD.items()] + [
         f"{COLOPHON_P} = {COLOPHON}",
         "", "## The chain", "",
         f"X-paccayā Y (chain clause) = x {COND} y, e.g. «{chain('avijjāpaccayā saṅkhāro, saṅkhārapaccayā viññāṇaṃ')}»",
         f"Suttanta: saṅkhārā / saṅkhārapaccayā = {N['saṅkhārā']} (pi-1 ^1-1343); Abhidhamma method: saṅkhāro = "
         f"{N['saṅkhāro']}",
         f"Avijjāpaccayā saṅkhārā, … sambhavanti. = {sutta_chain()}. (pi-1 ^1-1343)",
         f"X-paccayāpi Y = x {ALSO} {COND} y, e.g. «{clause('saṅkhārapaccayāpi avijjā')}»",
         f"Y X-hetuko = y {CAUSE.format(z='x')}, e.g. «{clause('avijjāpaccayā saṅkhāro avijjāhetuko')}»",
         f"Y X-sampayutto = y {CONJ.format(z='x')}, e.g. «{clause('avijjāpaccayā saṅkhāro avijjāsampayutto')}»",
         f"viññāṇapaccayā nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ = "
         f"{clause('viññāṇapaccayā nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ')}",
         f"nāmarūpapaccayā saḷāyatanaṃ nāmasampayuttaṃ chaṭṭhāyatanaṃ = "
         f"{clause('nāmarūpapaccayā saḷāyatanaṃ nāmasampayuttaṃ chaṭṭhāyatanaṃ')}",
         "chain separators: «, » as the Pāli; «; » between clauses carrying a hetuka / sampayutta qualifier; …pe… = …",
         "chain nouns: " + "; ".join(f"{k} = {v}" for k, v in N.items()),
         f"Evametassa kevalassa dukkhakkhandhassa samudayo hoti. = {cap(EVAM)}. (pi-1 ^1-1343)",
         f"Evametesaṃ dhammānaṃ samudayo hoti. = {cap(EVAM_DH)}.",
         f"Tasmiṃ samaye <chain>. = {cap(AT_TIME)}, <chain>.",
         f"Katame dhammā …? Yasmiṃ samaye …, tasmiṃ samaye <chain>. = … Vào lúc …, {THEN} <chain>.",
         "", "## Frames", "",
         f"Tattha katamo {ex}? (a chain statement as topic) = {TATTHA} thế nào là “{clause(ex)}”? (ch. 4 stmt_q)",
         f"– ayaṃ vuccati \"{ex}\". = – {CALLED} “{clause(ex)}”.",
         f"Nāmapaccayā phassoti. (topic, next sentence in lower case) = {TOPIC.format(x=clause('nāmapaccayā phasso'))}",
         f"Evametassa … samudayo hotīti[,.] evametassa … saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo "
         f"hoti. = {TOPIC.format(x=EVAM)} {EVAM_MEANS}.",
         f"Evametesaṃ dhammānaṃ samudayo hotīti. Evametesaṃ dhammānaṃ saṅgati hoti, … = {TOPIC.format(x=EVAM_DH)} "
         f"{EVAM_DH_MEANS}.",
         f"Tena vuccati \"evametassa … hotī\"ti. = {TENA} “{EVAM}”.",
     ] + [f"{k} = {v}" for k, v in SENT.items() if k.startswith(("Atthi", "Iti", "Bhavo", "Sabbampi", "Kāyasañcetanā",
                                                                    "Puññā", "Alobho"))] + [
         f"Ṭhapetvā X, vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho = Ngoại trừ x ra, {KH4}",
         f"Ṭhapetvā vedanaṃ, saññākkhandho saṅkhārakkhandho viññāṇakkhandho = Ngoại trừ {N['vedanā']} ra, {KH3_SNV}",
         f"phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā. = {CONTACT_PE} – {ARE_KUSALA}. (pi-1)",
         "", "## Definitions (answer bodies)", "",
     ] + [f"{k} = {v}" for k, v in BODY.items() if not k.startswith("Ṭhapetvā")] + [
         f"Yaṃ cittaṃ mano mānasaṃ…pe… tajjā<X>dhātu = {WHICH} {K23.CITTA_SHORT} <X> {K23.TAJJA}",
         f"Ñātibyasanena vā phuṭṭhassa … soko … / ādevo … / āyāso … = ch. 4 strings (K45.AFFLICT + lists)",
         "", "## Mind-type openers (pi-1 ^1-1, 365, 399, 431, 455, 498, 556, 566 shapes)", "",
         "Katame dhammā akusalā / kusalā / abyākatā? = " + " / ".join(KIND_Q.values()),
         f"Yasmiṃ samaye <X> uppannaṃ hoti …, tasmiṃ samaye = {WHEN} <x> {ARISES}, …, {THEN}",
     ] + [f"{k} uppann(aṃ|ā) hoti = {v} {ARISES}" for k, v in SUBJ.items()] + [
         f"kāmāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ … = …, {KAMMA['kāmāvacarassa kusalassa']}, …",
         f"akusalassa kammassa katattā upacitattā vipākaṃ … = …, {KAMMA['akusalassa']}, …",
         f"kiriyā neva kusalā nākusalā na ca kammavipākā = {FUNCTIONAL_Q}",
     ] + [f"{k}sahagataṃ/ā = {v}" for k, v in SAHA.items()] + [
         f"{k}sampayuttaṃ/ā / {k}vippayuttaṃ/ā = gắn liền với {v} / không gắn liền với {v}" for k, v in SAMP.items()] + [
         f"sasaṅkhārena = {PROMPTED}",
         "<O>ārammaṇaṃ vā … = có đối tượng là <o>, hay <o> …; after …pe… at the start of a piece: hay <o>",
         f"yaṃ yaṃ vā panārabbha = {ANY_OBJ}",
     ] + [f"Yasmiṃ samaye {k} = {v}" for k, v in JHANA.items()] + [f"{k} = {v}" for k, v in TASSEVA.items()]
    return unicodedata.normalize("NFC", "\n".join(L) + "\n")


def main():
    pali, h = build()
    text = render(pali, h)
    (S.OUT / PART).write_bytes(text.encode("utf-8"))
    print(f"wrote {PART}: {len(h)} segments")
    n = check_pi1()
    NOTES_PATH.write_bytes(notes_md().encode("utf-8"))
    print(f"pi-1 strings checked: {n}; notes-6.md written")
    for s in SLIPS:
        print("slip:", s)
    for s in MISFITS:
        print("misfit:", s)


if __name__ == "__main__":
    main()
