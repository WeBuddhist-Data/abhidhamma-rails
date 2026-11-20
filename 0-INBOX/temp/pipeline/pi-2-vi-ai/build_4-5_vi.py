# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Vietnamese plain zero-shot: chapters 4 (Saccavibhaṅga) and 5 (Indriyavibhaṅga).

usage: python -I -X utf8 build_4-5_vi.py [--unused]
Writes AI_translation\\vietnamese\\pi-2-vietnamese-plain-zeroshot_split_chapters\\4-saccavibhango.md
and 5-indriyavibhango.md (only when run as a script; importing writes nothing).

Imports build_ch1_sample_vi (S), build_1_vi (B) and build_2-3_vi (T) and reuses their strings, matrix-item
tables and frames (T's tables are extended in memory only). Pāli strings that occur in pi-1 are copied from the
reviewed pi-1 Vietnamese rails at build time (by block ID, or by the aligned line) and asserted. Every line is
built from fixed strings, so identical Pāli gives identical Vietnamese. Unknown Pāli raises KeyError (nothing is
guessed). Block IDs come from the Pāli.
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

DASH = S.DASH
cap, low = S.cap, S.low
q, called, listing, pi1, between, repl = T.q, T.called, T.listing, T.pi1, T.between, T.repl
TATTHA, THI, PE = S.TATTHA, S.THI, B.PE
SLIPS = []
PI1_PALI_DIR = os.path.join(S.ROOT, r"AI_translation\pali\pi-1_split_chapters")


def pi1_line(fn, needle):
    """pi-1 Vietnamese line aligned with the first pi-1 Pāli line containing needle (lines without a block ID)."""
    pl = [l for l in open(os.path.join(PI1_PALI_DIR, fn), encoding="utf-8").read().split("\n") if l.strip()]
    vl = [l for l in open(os.path.join(S.PI1_VI_DIR, fn), encoding="utf-8").read().split("\n") if l.strip()]
    assert len(pl) == len(vl)
    hits = [i for i, l in enumerate(pl) if needle in l]
    assert hits, needle
    return S.ID.sub("", vl[hits[0]])


def pe_cut(body, n, tail):
    """«a, b, c, … x, y»  ->  «a, b… x, y» (Pāli "a b…pe… x y"): the first n items, then from tail on."""
    assert body.count(tail) == 1, tail
    return ", ".join(body.split(", ")[:n]) + "… " + body[body.index(tail):]


def join_ca(items):
    """X ca, Y ca, … Z ca  ->  «X, Y … và Z»; «; » between items (and «; và») when an item has its own commas
    (pi-1 ^1-583)."""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} và {items[1]}"
    if any(", " in x for x in items):
        return "; ".join(items[:-1]) + "; và " + items[-1]
    return ", ".join(items[:-1]) + " và " + items[-1]


# ================================================================ chapter 4: names
SUFFERING = "khổ đau"                                        # dukkha (suffering) [pi-1 APPROVED]
ORIGIN = "sự phát sinh của khổ đau"                          # dukkhasamudaya [pi-1 ^1-1238]
CESSATION = "sự chấm dứt khổ đau"                            # dukkhanirodha [pi-1 ^1-1238]
WAY = "cách thực hành dẫn đến sự chấm dứt khổ đau"           # dukkhanirodhagāminī paṭipadā [pi-1 ^1-1238]
for _x in (ORIGIN, CESSATION, WAY):
    assert "sự không biết về " + _x in pi1("1-1238"), _x
NOBLE = "sự thật cao quý về "                                # ariyasacca [pi-1 core: sự thật cao quý]
TRUTH_SUBJ = {   # Pañhāpucchaka subjects and the ##### headings (single truths take «thì», see notes)
    "Dukkhasaccaṃ": "Sự thật về khổ đau", "Samudayasaccaṃ": "Sự thật về sự phát sinh",
    "Nirodhasaccaṃ": "Sự thật về sự chấm dứt", "Maggasaccaṃ": "Sự thật về con đường",
    "Dve saccā": "Hai sự thật", "Tīṇi saccāni": "Ba sự thật",
}


def four_noble(var=False):
    v1 = " [khác chính tả (Syā.): dukkhasamudayo]" if var else ""
    v2 = " [khác chính tả (Syā.): dukkhanirodho]" if var else ""
    return (f"Bốn sự thật cao quý {DASH} " + listing([NOBLE + SUFFERING, NOBLE + ORIGIN + v1, NOBLE + CESSATION + v2,
                                                       NOBLE + WAY]) + ".")


FOUR = f"Bốn sự thật {DASH} " + listing([SUFFERING, ORIGIN, CESSATION, WAY]) + "."   # Cattāri saccāni – …

# ---------------------------------------------------------------- Suttanta: suffering
SOKA5 = "sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng"   # sokaparidevadukkhadomanassupāyāsā
assert SOKA5 in pi1("1-1343")
APPIYA = "gặp gỡ những gì mình không yêu quý"     # appiyehi sampayogo [new]
PIYA_V = "xa lìa những gì mình yêu quý"           # piyehi vippayogo [new]
APPIYA_N, PIYA_N = SUFFERING + " vì " + APPIYA, SUFFERING + " vì " + PIYA_V   # … dukkho (as a name)
ICCHA = "không đạt được điều mình mong cầu cũng là khổ đau"   # yaṃ picchaṃ na labhati tampi dukkhaṃ [new]
UPK = "làm đối tượng cho sự bám víu"              # upādānakkhandha [new; upādāna pi-1]
UPK5 = f"nói tóm lại, năm khối {UPK} là khổ đau"  # saṃkhittena pañcupādānakkhandhā dukkhā [new]
WHO = "ở từng chúng sinh, trong từng loài chúng sinh"   # tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye [new]
JARA = between(pi1("1-643"), "Điều mà ở vật chất là ", f" {DASH} vật chất này")   # jarā … paripāko [pi-1]
BYASANA = ("Ở người gặp phải tổn hại về người thân, hoặc gặp phải tổn hại về tài sản, hoặc gặp phải tổn hại do "
           "bệnh tật, hoặc gặp phải tổn hại về giới hạnh, hoặc gặp phải tổn hại về quan điểm, ở người vướng phải "
           "tổn hại này hay tổn hại khác, gặp phải điều khổ đau này hay điều khổ đau khác, có")   # [new]
OBJ5 = S.FIVE_OBJECTS                                # rūpā saddā gandhā rasā phoṭṭhabbā [pi-1 words]
UNWANTED = "không đáng mong muốn, không đáng yêu mến, không đáng ưa thích"   # aniṭṭhā akantā amanāpā [sample]
WANTED = "đáng mong muốn, đáng yêu mến, đáng ưa thích"                       # iṭṭhā kantā manāpā [sample]
assert UNWANTED in S.HINA_BODY and WANTED in S.PANITA_BODY
MEET = "sự gặp gỡ, sự gần gũi, sự tụ hợp, sự hòa lẫn"                       # saṅgati samāgamo samodhānaṃ missībhāvo
NOMEET = "sự không gặp gỡ, sự không gần gũi, sự không tụ hợp, sự không hòa lẫn"
IDHA = "Ở đời này"                                   # Idha [pi-1 ^1-1355 / ^1-1377]
BHIKKHU = "vị tỳ-khưu"                               # [pi-1 ^1-1377]
assert "ở đời này, vị tỳ-khưu" in pi1("1-1377")
WISH = "khởi lên mong muốn như vầy"                  # evaṃ icchā uppajjati [new]
NOT_BY_WISH = "Nhưng điều này không thể đạt được bằng sự mong muốn."   # Na kho panetaṃ icchāya pattabbaṃ. [new]
THIS_TOO = f"Đây cũng là “{ICCHA}”."                 # Idampi "yampicchaṃ …". [new]
DHAMMA_OF = {"jāti": "phải sinh", "jarā": "phải già", "byādhi": "phải bệnh", "maraṇa": "phải chết",
             "soka": "phải chịu " + SOKA5}           # X-dhammānaṃ sattānaṃ = ở những chúng sinh có bản chất X [new]
FEEL_DUKKHA = T.feel_body("1-558", T.TAJJA_K)        # Yaṃ kāyikaṃ asātaṃ … (as ch. 3 dukkhadhātu)
FEEL_DOMAN = T.feel_body("1-415", T.TAJJA_M)         # Yaṃ cetasikaṃ asātaṃ … (as ch. 3 domanassadhātu)
PAIN, SADNESS, DESPAIR = "sự khó chịu", "nỗi buồn", "sự tuyệt vọng"   # dukkha (bodily) / domanassa / upāyāsa [pi-1]

# ---------------------------------------------------------------- Suttanta: craving
NANDIRAGA = "sự tham đắm vì thích thú"               # nandirāga [pi-1 ^1-1065]
TANHA3 = "khao khát dục lạc, khao khát được hiện hữu, khao khát không còn hiện hữu"   # [pi-1 ^1-1065]
for _x in (NANDIRAGA, TANHA3):
    assert _x in pi1("1-1065"), _x
PIYA = "là điều đáng yêu, là điều khoan khoái"       # piyarūpaṃ sātarūpaṃ [new; sāta pi-1 «khoan khoái»]
LOKE = "trong thế gian"                              # loke
UP = "Ở đó, khao khát này khi sinh khởi thì sinh khởi, ở đó, khi bám rễ thì bám rễ."
NIR = "Ở đó, khao khát này khi được dứt bỏ thì được dứt bỏ, ở đó, khi chấm dứt thì chấm dứt."
FIXED4 = {
    "Etthesā taṇhā uppajjamānā uppajjati, ettha nivisamānā nivisati.": UP,
    "Etthesā taṇhā pahīyamānā pahīyati, ettha nirujjhamānā nirujjhati.": NIR,
    "Sā kho panesā taṇhā kattha uppajjamānā uppajjati, kattha nivisamānā nivisati?":
        "Vậy khao khát này khi sinh khởi thì sinh khởi ở đâu, khi bám rễ thì bám rễ ở đâu?",
    "Sā kho panesā taṇhā kattha pahīyamānā pahīyati, kattha nirujjhamānā nirujjhati?":
        "Vậy khao khát này khi được dứt bỏ thì được dứt bỏ ở đâu, khi chấm dứt thì chấm dứt ở đâu?",
    "Yaṃ loke piyarūpaṃ sātarūpaṃ, etthesā taṇhā uppajjamānā uppajjati, ettha nivisamānā nivisati.":
        f"Điều gì {LOKE} {PIYA}, thì {low(UP)}",
    "Yaṃ loke piyarūpaṃ sātarūpaṃ, etthesā taṇhā pahīyamānā pahīyati, ettha nirujjhamānā nirujjhati.":
        f"Điều gì {LOKE} {PIYA}, thì {low(NIR)}",
    "Kiñca loke piyarūpaṃ sātarūpaṃ?": f"Và điều gì {LOKE} {PIYA}?",
}
DOOR_P = ("cakkhu", "sota", "ghāna", "jivhā", "kāya", "mano")
SUBJ4 = {"cakkhuṃ": "mắt", "sotaṃ": "tai", "ghānaṃ": "mũi", "jivhā": "lưỡi", "kāyo": "thân", "mano": "ý"}
for _o, _v in T.OBJ.items():
    SUBJ4[_o[:-1] + "ā"] = "các " + _v                                            # rūpā … dhammā
    SUBJ4[_o + "saññā"] = "tri giác về " + _v                                     # [new]
    SUBJ4[_o + "sañcetanā"] = "sự cố ý về " + _v                                  # [new; APPROVED sañcetanā]
    SUBJ4[_o + "taṇhā"] = "khao khát " + _v                                       # [pi-1 ^1-1065]
    SUBJ4[_o + "vitakko"] = "sự hướng tâm đến " + _v                              # [new]
    SUBJ4[_o + "vicāro"] = "sự duy trì tâm trên " + _v                            # [new]
    assert "khao khát " + _v in pi1("1-1065")
for _d, _v in zip(DOOR_P, S.DOORS):
    SUBJ4[_d + "viññāṇaṃ"] = B.SUBJ[_d + "viññāṇaṃ"]
    SUBJ4[_d + "samphasso"] = "sự tiếp xúc của " + _v                              # [pi-1 words]
    SUBJ4[_d + "samphassajā vedanā"] = B.SUBJ[_d + "samphassajā vedanā"]


def piya_line(t):
    out = []
    for sent in re.split(r"(?<=[.?]) ", t):
        if sent in FIXED4:
            out.append(FIXED4[sent])
            continue
        m = re.match(r"^(.*) piyarūpaṃ sātarūpaṃ\.$", sent)
        if not m:
            raise KeyError("piya sentence: " + sent[:60])
        parts = re.split(r"(…pe… |… )", m.group(1))
        s = ""
        for i, p in enumerate(parts):
            if i % 2:
                s += "… "
            else:
                assert p.endswith(" loke"), p
                s += f"{SUBJ4[low(p[:-5])]} {LOKE}"
        out.append(f"{cap(s)} {PIYA}.")
    return " ".join(out)


# ---------------------------------------------------------------- Suttanta: path
PF = {}   # pi-1 path-factor names and definitions (^1-297 … ^1-304) without «vào lúc ấy»
for _bid, _p in zip(range(297, 305), ("sammādiṭṭhi", "sammāsaṅkappo", "sammāvācā", "sammākammanto", "sammāājīvo",
                                       "sammāvāyāmo", "sammāsati", "sammāsamādhi")):
    _v = pi1(f"1-{_bid}")
    PF[_p] = (between(_v, "Vào lúc ấy, ", " là gì?"), between(_v, "Điều mà vào lúc ấy là ", f" {DASH} đó là"))
FNAME = {k: v[0] for k, v in PF.items()}
PATH8 = ", ".join(FNAME.values())                       # sammādiṭṭhi, … sammāsamādhi
PATH5 = between(pi1("1-89"), "là gì? ", ".")            # pañcaṅgiko maggo [pi-1 ^1-89]
assert low(PATH5) == ", ".join(FNAME[k] for k in ("sammādiṭṭhi", "sammāsaṅkappo", "sammāvāyāmo", "sammāsati",
                                                      "sammāsamādhi"))
PATH5 = low(PATH5)
MAGGA8 = "con đường gồm tám chi phần"                   # aṭṭhaṅgiko maggo [pi-1 ^1-337]
MAGGA5 = "con đường gồm năm chi phần"                   # pañcaṅgiko maggo [pi-1 ^1-89]
assert MAGGA8 in pi1("1-337") and MAGGA5 in pi1("1-89")
INTENTION3 = "Tư duy về sự từ bỏ, tư duy về sự không ác ý, tư duy về sự không hãm hại"   # [new; ch. 3 words]
SPEECH4 = ("Sự kiềm chế việc nói dối, sự kiềm chế việc nói lời chia rẽ, sự kiềm chế việc nói lời thô ác, "
           "sự kiềm chế việc nói lời phù phiếm")                          # [new; veramaṇī pi-1 «sự kiềm chế»]
ACTION3 = ("Sự kiềm chế việc sát hại sinh mạng, sự kiềm chế việc lấy của không được cho, "
           "sự kiềm chế hành vi sai trái trong các dục lạc")              # [new]
LIVELIHOOD = ("Ở đời này, vị đệ tử của bậc thánh, sau khi dứt bỏ sinh kế sai lầm, nuôi sống bản thân bằng "
              "sinh kế đúng đắn")                                          # [new; pi-1 words]
_eff = between(pi1("1-1377"), "ở đời này, vị tỳ-khưu ", ".").split("; ")
assert len(_eff) == 4
EFFORT4 = [f"{IDHA}, {BHIKKHU} {_eff[0]}."] + [f"Vị ấy {x}." for x in _eff[1:]]   # [pi-1 ^1-1377, one per sentence]
SATI_TAIL = ("nhiệt tâm, hiểu biết rõ ràng, có sự tỉnh thức, sau khi chế ngự sự thèm muốn và nỗi buồn "
             "đối với thế gian")                    # ātāpī sampajāno satimā, vineyya loke abhijjhādomanassaṃ [new]
assert "sự thèm muốn và nỗi buồn" in pi1("1-1352")
MINDFUL = (f"{IDHA}, {BHIKKHU}, đối với thân, sống quán sát thân, {SATI_TAIL}. Đối với các cảm giác… đối với tâm… "
           f"đối với các hiện tượng, vị ấy sống quán sát các hiện tượng, {SATI_TAIL}.")   # [new]
_j1 = pi1("1-160")
J1 = repl(between(_j1, "cõi hình sắc, ", ", với đề mục"), " [khác chính tả (Sī.): paṭhamajjhānaṃ]", "")
_j2 = pi1_line("2-02-cittuppadakandam.md", "maggaṃ bhāveti vitakkavicārānaṃ vūpasamā ajjhattaṃ")
J2 = repl(between(_j2, "cõi hình sắc, ", ", với đề mục"), " [khác chính tả (Sī.): dutiyajjhānaṃ]", "")
_j3 = pi1_line("2-02-cittuppadakandam.md", "maggaṃ bhāveti pītiyā ca virāgā upekkhako ca viharati")
J3 = repl(between(_j3, "cõi hình sắc, ", ", với đề mục"), " [khác chính tả (Sī.): tatiyajjhānaṃ]", "")
_j4 = pi1_line("2-02-cittuppadakandam.md", "maggaṃ bhāveti sukhassa ca pahānā dukkhassa ca pahānā")
J4 = repl(between(_j4, "cõi hình sắc, ", ", với đề mục"), " [khác chính tả (Sī.): catutthajjhānaṃ]", "")
JHANA4 = (f"{IDHA}, {BHIKKHU} {J1}. {cap(repl(J2, ', chứng nhập', ', vị ấy chứng nhập'))}. "
          f"{cap(repl(J3, 'phai nhạt, an trú', 'phai nhạt, vị ấy an trú'))}. "
          f"{cap(repl(J4, ', chứng nhập', ', vị ấy chứng nhập'))}.")   # [pi-1 ^1-160 and the 2nd–4th jhāna lines]
assert JHANA4.count(DASH) == 1

# ---------------------------------------------------------------- Abhidhamma (ch. 4)
ITEM4 = {   # Pāli list item (nominative or genitive, «ca» removed) -> Vietnamese
    "taṇhā": "khao khát", "taṇhāya": "khao khát",
    "avasesā kilesā": "các phiền não còn lại", "avasesānaṃ kilesānaṃ": "các phiền não còn lại",
    "avasesā akusalā dhammā": "các hiện tượng bất thiện còn lại",
    "avasesānaṃ akusalānaṃ dhammānaṃ": "các hiện tượng bất thiện còn lại",
    "tīṇi kusalamūlāni sāsavāni": "ba gốc rễ thiện mà là đối tượng của ô nhiễm",
    "tiṇṇaṃ kusalamūlānaṃ sāsavānaṃ": "ba gốc rễ thiện mà là đối tượng của ô nhiễm",
    "avasesā sāsavā kusalā dhammā": "các hiện tượng thiện còn lại mà là đối tượng của ô nhiễm",
    "avasesānaṃ sāsavānaṃ kusalānaṃ dhammānaṃ": "các hiện tượng thiện còn lại mà là đối tượng của ô nhiễm",
    "sāsavā kusalākusalānaṃ dhammānaṃ vipākā":
        "các quả của các hiện tượng thiện và bất thiện mà là đối tượng của ô nhiễm",
    "ye dhammā kiriyā neva kusalā nākusalā na kammavipākā":
        between(pi1("1-583"), "; ", "; toàn bộ vật chất"),           # [pi-1 ^1-583]
    "sabbaṃ rūpaṃ": "toàn bộ vật chất",                                 # [pi-1 ^1-583]
}
assert ITEM4["ye dhammā kiriyā neva kusalā nākusalā na kammavipākā"].startswith("những hiện tượng mang tính chức năng")
assert "các hiện tượng thiện và bất thiện" in pi1("1-583") and "là đối tượng của ô nhiễm" == S.QUAL["sasava"]


def items4(s):
    s = re.sub(r"^Taṇhā ca avasesā", "Taṇhā ca, avasesā", s)
    out = []
    for x in s.split(", "):
        x = low(x)
        x = re.sub(r"ñca\b", "ṃ", x)          # avasesānañca -> avasesānaṃ, sabbañca -> sabbaṃ, tiṇṇañca
        x = re.sub(r" ca\b", "", x)           # avasesā ca kilesā -> avasesā kilesā; na ca kammavipākā
        out.append(ITEM4[x])
    return out


AVASESA = f"Các hiện tượng còn lại gắn liền với {WAY}."   # Avasesā dhammā … sampayuttā. [new]
JHANA_LOK = between(pi1("1-277"), "Vào lúc một người ", " thì vào lúc ấy có sự tiếp xúc")   # [pi-1 ^1-277]
assert JHANA_LOK.endswith("chậm chạp,")
CONTACT_TO = "sự tiếp xúc… có sự không tán loạn"         # phasso hoti…pe… avikkhepo hoti [pi-1 ^1-160]
assert "có " + CONTACT_TO in pi1("1-160")
PATH_TAIL = {
    "aṭṭhaṅgiko maggo hoti sammādiṭṭhi…pe… sammāsamādhi.":   # dash missing in the Pāli (reported): a colon
        f"{MAGGA8}: {FNAME['sammādiṭṭhi']}… {FNAME['sammāsamādhi']}.",
    "aṭṭhaṅgiko maggo hoti – sammādiṭṭhi…pe… sammāsamādhi.":
        f"{MAGGA8} {DASH} {FNAME['sammādiṭṭhi']}… {FNAME['sammāsamādhi']}.",
    "pañcaṅgiko maggo hoti – sammādiṭṭhi, sammāsaṅkappo, sammāvāyāmo, sammāsati, sammāsamādhi.":
        f"{MAGGA5} {DASH} {PATH5}.",
    "phasso hoti…pe… avikkhepo hoti.": CONTACT_TO + ".",
}
PATH_HEAD = re.compile(r"^Tattha katamā dukkhanirodhagāminī paṭipadā\? Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ "
                       r"bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā,? "
                       r"vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ, "
                       r"tasmiṃ samaye (.+)$")


def path_sent(s):
    m = PATH_HEAD.match(s)
    return (f"{q(WAY)} {IDHA}, vào lúc {BHIKKHU} {JHANA_LOK} thì vào lúc ấy có {PATH_TAIL[m.group(1)]}")


_SD, _SS, _SV, _SK, _SA, _SY, _ST, _SM = (PF[k][1] for k in PF)
ABHI_BODY = {   # Pāli definition body -> Vietnamese (after «Điều mà là»)
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        pe_cut(_SD, 2, "sự không si mê"),
    "Yo takko vitakko…pe… sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ": pe_cut(_SS, 2, FNAME["sammāsaṅkappo"]),
    ("Yā catūhi vacīduccaritehi ārati virati paṭivirati veramaṇī [veramaṇi (ka.) evamuparipi] akiriyā akaraṇaṃ "
     "anajjhāpatti velāanatikkamo setughāto sammāvācā maggaṅgaṃ maggapariyāpannaṃ"):
        repl(_SV, "sự kiềm chế,", "sự kiềm chế [khác chính tả (Ka.): veramaṇi; cũng vậy ở các chỗ sau],"),
    ("Yā tīhi kāyaduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo "
     "setughāto sammākammanto maggaṅgaṃ maggapariyāpannaṃ"): _SK,
    ("Yā micchā ājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
     "sammāājīvo maggaṅgaṃ maggapariyāpannaṃ"): _SA,
    ("Yo cetasiko vīriyārambho [viriyārambho (sī. syā.)] …pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ "
     "maggapariyāpannaṃ"): repl(pe_cut(_SY, 1, FNAME["sammāvāyāmo"]), "trong tâm…",
                                 "trong tâm [khác chính tả (Sī., Syā.): viriyārambho]…"),
    "Yo cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        pe_cut(_SY, 1, FNAME["sammāvāyāmo"]),
    "Yā sati anussati…pe… sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ": pe_cut(_ST, 2, FNAME["sammāsati"]),
    "Yā cittassa ṭhiti saṇṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        pe_cut(_SM, 2, FNAME["sammāsamādhi"]),
    "Yā cittassa ṭhiti…pe… sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        pe_cut(_SM, 1, FNAME["sammāsamādhi"]),
}
DEF_RE = re.compile(r'^Tattha katam(?:o|ā|aṃ) (.+?)\? (.+) ' + DASH + r' (?:ayaṃ|idaṃ) vuccati "([^"]+)"\.$')


def abhi4_sent(s):
    if s == "Cattāri saccāni – dukkhaṃ, dukkhasamudayo, dukkhanirodho, dukkhanirodhagāminī paṭipadā.":
        return FOUR
    if s == 'Ayaṃ vuccati "dukkhanirodhagāminī paṭipadā".':
        return f"{cap(called(WAY))}."
    if s == 'Ayaṃ vuccati – "dukkhanirodhagāminī paṭipadā".':
        return f"{cap(T.VUCCATI)} {DASH} “{WAY}”."
    if s == "Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā.":
        return AVASESA
    if PATH_HEAD.match(s):
        return path_sent(s)
    m = DEF_RE.match(s)
    if not m:
        raise KeyError("abhi4: " + s[:80])
    name, body, ans = m.groups()
    assert name == ans, (name, ans)
    if name == "dukkhasamudayo":
        return f"{q(ORIGIN)} {cap(join_ca(items4(body)))} {DASH} {called(ORIGIN)}."
    if name == "dukkhaṃ":
        return f"{q(SUFFERING)} {cap(join_ca(items4(body)))} {DASH} {called(SUFFERING)}."
    if name == "dukkhanirodho":
        assert body.endswith(" pahānaṃ")
        return f"{q(CESSATION)} Sự dứt bỏ {join_ca(items4(body[:-len(' pahānaṃ')]))} {DASH} {called(CESSATION)}."
    return f"{q(FNAME[name])} Điều mà là {ABHI_BODY[body]} {DASH} {called(FNAME[name])}."


def abhi4_line(t):
    sents = re.split(r'(?<=\.) (?=(?:Ayaṃ|Idaṃ) vuccati|Avasesā dhammā)', t)
    return " ".join(abhi4_sent(s) for s in sents)


# ---------------------------------------------------------------- Suttanta lines (ch. 4), in order
HAND4 = [
    ("Tattha katamaṃ dukkhaṃ ariyasaccaṃ? Jātipi dukkhā",
     f"{q(NOBLE + SUFFERING)} Sự sinh cũng là khổ đau, sự lão hóa cũng là khổ đau, sự chết cũng là khổ đau, "
     f"{SOKA5} cũng là khổ đau, {APPIYA} là khổ đau, {PIYA_V} là khổ đau, {ICCHA}, {UPK5}."),
    ("Tattha katamā jāti?",
     f"{q('sự sinh')} Điều mà {WHO}, là sự sinh, sự sinh ra, sự nhập thai, sự hình thành, sự xuất hiện của các khối, "
     f"sự có được các lĩnh vực nhận biết {DASH} {called('sự sinh')}."),
    ("Tattha katamā jarā?", f"{q('sự lão hóa')} Điều mà {WHO}, là {JARA} {DASH} {called('sự lão hóa')}."),
    ("Tattha katamaṃ maraṇaṃ?",
     f"{q('sự chết')} Điều mà ở từng chúng sinh là sự lìa khỏi từng loài chúng sinh, trạng thái lìa khỏi, "
     "sự tan rã, sự biến mất, sự tử vong, sự chết, sự qua đời, sự tan rã của các khối, sự bỏ lại thân xác, "
     f"sự cắt đứt năng lực sống {DASH} {called('sự chết')}."),
    ("Tattha katamo soko?",
     f"{q('sự sầu muộn')} {BYASANA} sự sầu muộn, sự buồn rầu, trạng thái buồn rầu, nỗi sầu bên trong, "
     "nỗi sầu thấm sâu bên trong, sự héo hon của tâm, nỗi buồn, mũi tên sầu muộn "
     f"{DASH} {called('sự sầu muộn')}."),
    ("Tattha katamo paridevo?",
     f"{q('sự than khóc')} {BYASANA} sự kêu khóc, sự than khóc, hành động kêu khóc, hành động than khóc, "
     "trạng thái kêu khóc, trạng thái than khóc, lời nói, lời lảm nhảm, lời lảm nhảm không ngớt, sự rên rỉ, "
     "hành động rên rỉ, trạng thái rên rỉ [khác chính tả (Syā.): lālapo lālapanā lālapitattaṃ] "
     f"{DASH} {called('sự than khóc')}."),
    ("Tattha katamaṃ dukkhaṃ? Yaṃ kāyikaṃ asātaṃ",
     f"{q(PAIN)} Điều mà là {FEEL_DUKKHA} {DASH} {called(PAIN)}."),
    ("Tattha katamaṃ domanassaṃ?", f"{q(SADNESS)} Điều mà là {FEEL_DOMAN} {DASH} {called(SADNESS)}."),
    ("Tattha katamo upāyāso?",
     f"{q(DESPAIR)} {BYASANA} sự phiền muộn, sự tuyệt vọng, trạng thái phiền muộn, trạng thái tuyệt vọng "
     f"{DASH} {called(DESPAIR)}."),
    ("Tattha katamo appiyehi sampayogo dukkho?",
     f"{q(APPIYA_N)} {IDHA}, đối với người nào mà các {OBJ5} là {UNWANTED}, hoặc có những người mong điều không "
     "lợi ích, mong điều không tốt lành, mong điều không thoải mái, mong điều không an ổn cho người ấy; "
     f"{MEET} với chúng {DASH} {called(APPIYA_N)}."),
    ("Tattha katamo piyehi vippayogo dukkho?",
     f"{q(PIYA_N)} {IDHA}, đối với người nào mà các {OBJ5} là {WANTED}, hoặc có những người mong điều lợi ích, "
     "mong điều tốt lành, mong điều thoải mái, mong điều an ổn cho người ấy: mẹ, hoặc cha, hoặc anh em trai, "
     "hoặc chị em gái, hoặc bạn bè, hoặc đồng sự, hoặc bà con, hoặc người ruột thịt; "
     f"{NOMEET} với chúng {DASH} {called(PIYA_N)}."),
    ("Tattha katamaṃ yampicchaṃ na labhati tampi dukkhaṃ?",
     f"{TATTHA} “{ICCHA}” là gì? Ở những chúng sinh có bản chất {DHAMMA_OF['jāti']}, {WISH} {DASH} "
     f"“Ôi, ước gì chúng ta không có bản chất {DHAMMA_OF['jāti']}; và ước gì sự sinh không đến với chúng ta”! "
     f"{NOT_BY_WISH} {THIS_TOO}"),
    ("Jarādhammānaṃ sattānaṃ…pe…",
     f"Ở những chúng sinh có bản chất {DHAMMA_OF['jarā']}… ở những chúng sinh có bản chất {DHAMMA_OF['byādhi']}… "
     f"ở những chúng sinh có bản chất {DHAMMA_OF['maraṇa']}… ở những chúng sinh có bản chất {DHAMMA_OF['soka']}, "
     f"{WISH} {DASH} “Ôi, ước gì chúng ta không có bản chất {DHAMMA_OF['soka']}; và ước gì {SOKA5} không đến "
     f"với chúng ta”! {NOT_BY_WISH} {THIS_TOO}"),
    ("Tattha katame saṃkhittena pañcupādānakkhandhā dukkhā?",
     f"{TATTHA} “{UPK5}” là gì? Cụ thể là {DASH} "
     + ", ".join(f"{S.AGG[a]['khandha']} {UPK}" for a in ("rupa", "vedana", "sanna", "sankhara", "vinnana"))
     + f". {cap(called(UPK5))}."),
    ('Idaṃ vuccati "dukkhaṃ ariyasaccaṃ".', f"{cap(called(NOBLE + SUFFERING))}."),
    ("Tattha katamaṃ dukkhasamudayaṃ ariyasaccaṃ?",
     f"{q(NOBLE + ORIGIN)} Đó là khao khát dẫn đến sự hiện hữu mới [khác chính tả (Syā., Ka.): ponobbhavikā], "
     f"có {NANDIRAGA} đi kèm, tìm vui thích ở chỗ này chỗ kia, cụ thể là {DASH} {TANHA3}."),
    ('Idaṃ vuccati "dukkhasamudayaṃ ariyasaccaṃ".', f"{cap(called(NOBLE + ORIGIN))}."),
    ("Tattha katamaṃ dukkhanirodhaṃ ariyasaccaṃ?",
     f"{q(NOBLE + CESSATION)} Đó là sự phai nhạt và chấm dứt không còn dư sót của chính khao khát ấy, "
     "sự xả bỏ, sự buông bỏ, sự giải thoát, sự không còn bám chấp."),
    ('Idaṃ vuccati "dukkhanirodhaṃ ariyasaccaṃ".', f"{cap(called(NOBLE + CESSATION))}."),
    ("Tattha katamaṃ dukkhanirodhagāminī paṭipadā ariyasaccaṃ?",
     f"{q(NOBLE + WAY)} Đó chính là con đường cao quý gồm tám chi phần, cụ thể là {DASH} {PATH8}."),
    ("Tattha katamā sammādiṭṭhi? Dukkhe ñāṇaṃ",
     f"{q(FNAME['sammādiṭṭhi'])} " + cap(", ".join(f"sự hiểu biết về {x}" for x in (SUFFERING, ORIGIN, CESSATION, WAY)))
     + f" {DASH} {called(FNAME['sammādiṭṭhi'])}."),
    ("Tattha katamo sammāsaṅkappo? Nekkhammasaṅkappo",
     f"{q(FNAME['sammāsaṅkappo'])} {INTENTION3} {DASH} {called(FNAME['sammāsaṅkappo'])}."),
    ("Tattha katamā sammāvācā? Musāvādā",
     f"{q(FNAME['sammāvācā'])} {SPEECH4} {DASH} {called(FNAME['sammāvācā'])}."),
    ("Tattha katamo sammākammanto? Pāṇātipātā",
     f"{q(FNAME['sammākammanto'])} {ACTION3} {DASH} {called(FNAME['sammākammanto'])}."),
    ("Tattha katamo sammāājīvo? Idha ariyasāvako",
     f"{q(FNAME['sammāājīvo'])} {LIVELIHOOD} {DASH} {called(FNAME['sammāājīvo'])}."),
    ("Tattha katamo sammāvāyāmo? Idha bhikkhu",
     f"{q(FNAME['sammāvāyāmo'])} " + " ".join(EFFORT4) + f" {cap(called(FNAME['sammāvāyāmo']))}."),
    ("Tattha katamā sammāsati? Idha bhikkhu",
     f"{q(FNAME['sammāsati'])} {MINDFUL} {cap(called(FNAME['sammāsati']))}."),
    ("Tattha katamo sammāsamādhi? Idha bhikkhu",
     f"{q(FNAME['sammāsamādhi'])} {JHANA4} {cap(called(FNAME['sammāsamādhi']))}."),
    ('Idaṃ vuccati "dukkhanirodhagāminī paṭipadā ariyasaccaṃ".', f"{cap(called(NOBLE + WAY))}."),
]

# ================================================================ chapter 5: names
IND = {   # [pi-1]
    "cakkhundriyaṃ": "năng lực mắt", "sotindriyaṃ": "năng lực tai", "ghānindriyaṃ": "năng lực mũi",
    "jivhindriyaṃ": "năng lực lưỡi", "kāyindriyaṃ": "năng lực thân", "manindriyaṃ": "năng lực ý",
    "itthindriyaṃ": "năng lực nữ tính", "purisindriyaṃ": "năng lực nam tính", "jīvitindriyaṃ": "năng lực sống",
    "sukhindriyaṃ": "năng lực dễ chịu", "dukkhindriyaṃ": "năng lực khó chịu", "somanassindriyaṃ": "năng lực niềm vui",
    "domanassindriyaṃ": "năng lực nỗi buồn", "upekkhindriyaṃ": "năng lực bình thản",
    "saddhindriyaṃ": "năng lực niềm tin", "vīriyindriyaṃ": "năng lực tinh tấn", "satindriyaṃ": "năng lực tỉnh thức",
    "samādhindriyaṃ": "năng lực định tâm", "paññindriyaṃ": "năng lực trí tuệ",
    "anaññātaññassāmītindriyaṃ": "năng lực biết được điều chưa từng biết",
    "aññindriyaṃ": "năng lực hiểu biết trọn vẹn", "aññātāvindriyaṃ": "năng lực của người đã hiểu biết trọn vẹn",
}
for _k in ("saddhindriyaṃ", "vīriyindriyaṃ", "satindriyaṃ", "samādhindriyaṃ", "paññindriyaṃ", "manindriyaṃ",
           "somanassindriyaṃ", "jīvitindriyaṃ", "anaññātaññassāmītindriyaṃ"):
    assert "có " + IND[_k] + "," in pi1("1-277"), _k
assert ", ".join(IND[k] for k in ("cakkhundriyaṃ", "sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ")) \
    in low(S.RUPA_NAVA)
RUPA_JIV, ARUPA_JIV = "năng lực sống thuộc vật chất", "năng lực sống phi vật chất"   # [new; pi-1 rūpino / arūpino]
IND_ORDER = list(IND)
TWENTY_TWO = "Hai mươi hai năng lực"                                               # Bāvīsatindriyāni [new]


def twenty_two(var=False):
    names = [IND[k] for k in IND_ORDER]
    if var:
        names[IND_ORDER.index("vīriyindriyaṃ")] += " [khác chính tả (Sī., Syā.): viriyindriyaṃ]"
    return f"{TWENTY_TWO} {DASH} " + listing(names) + "."


def body(bid):
    return between(pi1(bid), "Điều mà vào lúc ấy là ", f" {DASH} đó là")


def ind_def(key, bod):
    return f"{q(IND[key])} {bod} {DASH} {called(IND[key])}."


SADDHA = body("1-12")
VIRIYA = body("1-13")
for _a, _b in ((" [khác chính tả (Sī., Syā.): viriyārambho]", ""), (" [khác chính tả (Sī.): ussoḷhi]", ""),
               ("sức bền, sự kiên trì,", "sức bền, sự ổn định,")):   # pi-2 thāmo ṭhiti (pi-1 thāmo dhiti): as written
    VIRIYA = repl(VIRIYA, _a, _b)
assert VIRIYA.endswith(", nỗ lực đúng đắn")
VIRIYA = VIRIYA[:-len(", nỗ lực đúng đắn")]   # pi-2 has no sammāvāyāmo here
SATI, SAMADHI = body("1-14"), body("1-15")
PANNA = pe_cut(body("1-16"), 2, "sự không si mê")
_an = between(pi1("1-296"), "là gì? ", f" {DASH} đó là")
ANANNATA = _an[:_an.index(", sự tìm hiểu, ")] + "… " + _an[_an.index("sự không si mê"):]
_ann = between(pi1_line("2-03-cittuppadakandam.md", "Katamaṃ tasmiṃ samaye aññindriyaṃ hoti?"), "là gì? ",
               ", đó là năng lực")
ANNA = _ann[:_ann.index(", sự tìm hiểu, ")] + "… " + _ann[_ann.index("sự không si mê"):]
ANNATAVI = repl(ANNA, "vốn đã được biết, đã được thấy", "vốn đã hiểu biết trọn vẹn, đã được thấy")   # aññātāvīnaṃ [new]
ITTHI = between(pi1("1-714"), "? ", f" {DASH} vật chất này")
PURISA = between(pi1("1-716"), "? ", f" {DASH} vật chất này")
JIV_R = between(pi1("1-718"), "? ", f" {DASH} vật chất này")
JIV_A = repl(between(pi1("1-19"), "? ", f" {DASH} đó là"), " [khác chính tả (Sī.): irīyanā]", "")
EYE_SHORT = T.short_body(repl(T.base_body("1-596"), " [khác chính tả (Sī., Syā.): cakkhuṃ]", ""), ", nằm trong",
                         "đây là ngôi làng trống rỗng")
BODY_SHORT = T.short_body(T.BODY, ", nằm trong", "đây là ngôi làng trống rỗng")

# manindriya classification: T's Abhidhammabhājanīya machinery with «năng lực ý» as subject
T.FSUBJ["manindriyaṃ"] = IND["manindriyaṃ"]
T.NAME["manindriyaṃ"] = IND["manindriyaṃ"]
_FS = "|".join(map(re.escape, sorted(T.FSUBJ, key=len, reverse=True)))
T.FRAME = re.compile(r"^(Aparopi )?(\w+?)[vb]idhena (" + _FS + ")")
T.CLOSE = re.compile(r"^([Ee])vaṃ (\w+?)[vb]idhena (" + _FS + ")$")


def mano_line(t):
    """…Evaṃ dasavidhena manindriyaṃ…pe… evaṃ bahuvidhena manindriyaṃ. -> «… như vậy là … theo nhiều nhóm.»"""
    joint = "manindriyaṃ…pe… evaṃ bahuvidhena"
    if joint in t:
        t = t.replace(joint, "manindriyaṃ. Evaṃ bahuvidhena")
        vi = T.abhi_line(t)
        a = f"{T.fclose('manindriyaṃ', 'dasa')}. {T.fclose('manindriyaṃ', 'bahu')}"
        assert vi.count(a) == 1
        return vi.replace(a, f"{T.fclose('manindriyaṃ', 'dasa')}… {low(T.fclose('manindriyaṃ', 'bahu'))}")
    return T.abhi_line(t)


HAND5 = [
    ("Tattha katamaṃ cakkhundriyaṃ?", ind_def("cakkhundriyaṃ", EYE_SHORT)),
    ("Tattha katamaṃ sotindriyaṃ…pe…",
     f"{TATTHA} {IND['sotindriyaṃ']}… {IND['ghānindriyaṃ']}… {IND['jivhindriyaṃ']}… {IND['kāyindriyaṃ']} là gì? "
     f"{BODY_SHORT} {DASH} {called(IND['kāyindriyaṃ'])}."),
    ("Tattha katamaṃ itthindriyaṃ?", ind_def("itthindriyaṃ", ITTHI)),
    ("Tattha katamaṃ purisindriyaṃ?", ind_def("purisindriyaṃ", PURISA)),
    ("Tattha katamaṃ jīvitindriyaṃ?",
     f"{q(IND['jīvitindriyaṃ'])} Phân loại {IND['jīvitindriyaṃ']} {B.by_groups(2)} {DASH} "
     f"{B.ATTHI} là {RUPA_JIV}, {B.ATTHI} là {ARUPA_JIV}."),
    ("Tattha katamaṃ rūpajīvitindriyaṃ?", f"{q(RUPA_JIV)} {JIV_R} {DASH} {called(RUPA_JIV)}."),
    ("Tattha katamaṃ arūpajīvitindriyaṃ?",   # answer "arūpajīvatindriyaṃ": spelling slip, rendered as meant
     f"{q(ARUPA_JIV)} {JIV_A} {DASH} {called(ARUPA_JIV)}. {cap(called(IND['jīvitindriyaṃ']))}."),
    ("Tattha katamaṃ sukhindriyaṃ?", ind_def("sukhindriyaṃ", "Điều mà là " + T.feel_body("1-445", T.TAJJA_K))),
    ("Tattha katamaṃ dukkhindriyaṃ?", ind_def("dukkhindriyaṃ", "Điều mà là " + FEEL_DUKKHA)),
    ("Tattha katamaṃ somanassindriyaṃ?", ind_def("somanassindriyaṃ", "Điều mà là " + T.feel_body("1-3", T.TAJJA_M))),
    ("Tattha katamaṃ domanassindriyaṃ?", ind_def("domanassindriyaṃ", "Điều mà là " + FEEL_DOMAN)),
    ("Tattha katamaṃ upekkhindriyaṃ?", ind_def("upekkhindriyaṃ", "Điều mà là " + T.feel_body("1-152", T.TAJJA_M))),
    ("Tattha katamaṃ saddhindriyaṃ?", ind_def("saddhindriyaṃ", "Điều mà là " + SADDHA)),
    ("Tattha katamaṃ vīriyindriyaṃ?", ind_def("vīriyindriyaṃ", "Điều mà là " + VIRIYA)),
    ("Tattha katamaṃ satindriyaṃ?", ind_def("satindriyaṃ", "Điều mà là " + SATI)),
    ("Tattha katamaṃ samādhindriyaṃ?", ind_def("samādhindriyaṃ", "Điều mà là " + SAMADHI)),
    ("Tattha katamaṃ paññindriyaṃ?", ind_def("paññindriyaṃ", "Điều mà là " + PANNA)),
    ("Tattha katamaṃ anaññātaññassāmītindriyaṃ?", ind_def("anaññātaññassāmītindriyaṃ", ANANNATA)),
    ("Tattha katamaṃ aññindriyaṃ?",   # answer unquoted in the Pāli: kept unquoted
     f"{q(IND['aññindriyaṃ'])} {ANNA} {DASH} {called(IND['aññindriyaṃ'], quoted=False)}."),
    ("Tattha katamaṃ aññātāvindriyaṃ?", ind_def("aññātāvindriyaṃ", ANNATAVI)),
]
# ================================================================ Pañhāpucchaka (ch. 4 and 5)
SURF, ITEMS, CANON = T.SURF, T.ITEMS, T.CANON


def add_item(key, surfaces, p):
    ITEMS[key] = dict(p=p, s=p)
    for x in surfaces:
        assert x not in SURF, x
        SURF[x] = key
        c = T.canon(x)
        assert CANON.get(c, key) == key, ("canon collision", x)
        CANON[c] = key


P = lambda k: ITEMS[k]["p"]  # noqa: E731
add_item("na_maggarammana", ["na maggārammaṇaṃ"], "không " + P("maggarammana"))
add_item("na_maggarammana_maggahetuka", ["na maggārammaṇaṃ maggahetukaṃ"],
         f"không {P('maggarammana')}, {P('maggahetuka')}")
add_item("maggarammana_na_maggahetuka", ["maggārammaṇaṃ na maggahetukaṃ"],
         f"{P('maggarammana')}, không {P('maggahetuka')}")
add_item("na_appamanarammana", ["na appamāṇārammaṇaṃ"], "không " + P("appamanarammana"))
add_item("mahaggata_na_appamana", ["mahaggatārammaṇaṃ na appamāṇārammaṇaṃ"],
         f"{P('mahaggatarammana')}, không {P('appamanarammana')}")
SURF["arūpāni"] = "arupi"   # neuter plural (Tīṇi saccāni arūpāni)
CANON[T.canon("arūpāni")] = "arupi"

FIXES = (   # punctuation slips in the Pāli (reported)
    ("Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā.", "Dve saccā nīvaraṇiyā. Dve saccā anīvaraṇiyā."),
    ("siyā araṇanti.", "siyā araṇaṃ."), ("siyā araṇāti.", "siyā araṇā."),
    ('" tipi', '"tipi'), ('"nti pi', '"ntipi'),
    ("siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ,", "siyā parittārammaṇaṃ, siyā mahaggatārammaṇaṃ,"),
    ('"gantho ceva ganthasampayutta"ñcāti', '"gantho ceva ganthasampayuttañcā"ti'),
)

NUM_IND = {"Dv": "Hai", "Tīṇ": "Ba", "Cattār": "Bốn", "Pañc": "Năm", "Satt": "Bảy", "Aṭṭh": "Tám", "Nav": "Chín",
           "Das": "Mười", "Ekādas": "Mười một", "Dvādas": "Mười hai", "Teras": "Mười ba", "Cuddas": "Mười bốn",
           "Pannaras": "Mười lăm", "Soḷas": "Mười sáu", "Sattaras": "Mười bảy", "Aṭṭhāras": "Mười tám",
           "Ekavīsat": "Hai mươi mốt"}
IND_SUBJ = {f"{k}indriyā": f"{v} năng lực" for k, v in NUM_IND.items()}
IND_SUBJ["Cha indriyā"] = "Sáu năng lực"
IND_SUBJ["aṭṭhindriyā"] = "tám năng lực"   # after a comma (reported: comma where a full stop is expected)
IND_SINGLE = {cap(k): cap(IND[k]) for k in ("domanassindriyaṃ", "anaññātaññassāmītindriyaṃ", "jīvitindriyaṃ",
                                             "aññindriyaṃ", "somanassindriyaṃ", "upekkhindriyaṃ",
                                             "aññātāvindriyaṃ", "manindriyaṃ")}
IND_SUBJ.update(IND_SINGLE)
TRUTH_SINGLE = {k for k in TRUTH_SUBJ if k.endswith("saccaṃ")}


class Q:
    def __init__(self, subjects, single):
        self.subjects, self.single = subjects, single
        self.rx = re.compile(r"^(" + "|".join(map(re.escape, sorted(subjects, key=len, reverse=True))) + r") (.+)$")

    def chunk(self, c, state, first):
        subj, one = "", False
        m = self.rx.match(c)
        if m:
            subj, one, c = self.subjects[m.group(1)], m.group(1) in self.single, m.group(2)
        elif first:
            c = low(c)   # a sentence without a subject ("Sappaccayā.", "No āsavā.", "Sahetukā ceva na ca hetū.")
        m = re.match(r"^(siyā )?na vattabb(?:o|ā|aṃ) " + DASH + r" (.+)$", c)
        if m:
            qm = B.QUOTE_RE.match(m.group(2))
            vi = f"{B.NV} {T.quoted(qm.group(1), qm.group(2), {})}"
            if m.group(1):
                vi = f"{B.SOMETIMES} {vi}"
            state["nv"] = True
        elif B.QUOTE_RE.match(c):
            qm = B.QUOTE_RE.match(c)
            vi = f"{B.OR} {T.quoted(qm.group(1), qm.group(2), {})}"
            state["nv"] = True
        else:
            if re.match(r'^"[^"]*"$', c):
                SLIPS.append("quoted affirmative without ti: " + c)
                c = c[1:-1]
            if c.startswith("siyā "):
                vi = f"{B.SOMETIMES} {T.pred_vi(c[5:], {})}"
            else:
                vi = T.pred_vi(c, {})
                if state.get("nv"):
                    vi = "mà " + vi
            state["nv"] = False
        if not subj:
            return vi
        # «thì» after a single named truth / faculty (keeps «Sự thật về con đường thì thiện» a statement), and,
        # as in ch. 1–3, after any subject before «không nên nói»; never before «là …»
        if (one and not vi.startswith("là ")) or vi.startswith(B.NV):
            vi = f"{THI} {vi}"
        return f"{subj} {vi}"

    def line(self, t):
        for a, b in FIXES:
            if a in t:
                SLIPS.append("punctuation: " + a)
                t = t.replace(a, b)
        out = []
        for sent in re.split(r"(?<=\.) (?=[A-ZĀ])", t):
            assert sent.endswith("."), sent[-40:]
            parts = re.split(r"(, |; |\x01 ?)", sent[:-1].replace("…pe…", PE))
            state, vi = {}, []
            for i, x in enumerate(parts):
                if i % 2:
                    vi.append(B.sep_vi(x))
                    if x.startswith(PE) or x == "; ":
                        state["nv"] = False
                else:
                    vi.append(self.chunk(x, state, i == 0))
            out.append(cap("".join(vi)) + ".")
        return " ".join(out)


Q4 = Q(TRUTH_SUBJ, TRUTH_SINGLE)
Q5 = Q(IND_SUBJ, set(IND_SINGLE))

# ================================================================ labels and build
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
    "### Saccavibhaṅgo": "### " + S.CHAPTER_TITLES[4],
    "### Indriyavibhaṅgo": "### " + S.CHAPTER_TITLES[5],
    "Saccavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[4]),
    "Indriyavibhaṅgo niṭṭhito.": S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[5]),
    ("Cattāri ariyasaccāni – dukkhaṃ ariyasaccaṃ, dukkhasamudayaṃ [dukkhasamudayo (syā.)] ariyasaccaṃ, "
     "dukkhanirodhaṃ [dukkhanirodho (syā.)] ariyasaccaṃ, dukkhanirodhagāminī paṭipadā ariyasaccaṃ."): four_noble(True),
    ("Cattāri ariyasaccāni – dukkhaṃ ariyasaccaṃ, dukkhasamudayaṃ ariyasaccaṃ, dukkhanirodhaṃ ariyasaccaṃ, "
     "dukkhanirodhagāminī paṭipadā ariyasaccaṃ."): four_noble(),
    "Catunnaṃ ariyasaccānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.question_q("bốn sự thật cao quý", "sự thật"),
    "Bāvīsatīnaṃ indriyānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        T.question_q(low(TWENTY_TWO), "năng lực"),
}
for _k in ("Dukkhasaccaṃ", "Samudayasaccaṃ", "Nirodhasaccaṃ", "Maggasaccaṃ"):
    LABELS["##### " + _k] = "##### " + TRUTH_SUBJ[_k]
_IND_LIST = ", ".join(k for k in IND_ORDER)
LABELS["Bāvīsatindriyāni – " + _IND_LIST.replace("vīriyindriyaṃ", "vīriyindriyaṃ [viriyindriyaṃ (sī. syā.)]")
       + "."] = twenty_two(True)
LABELS["Bāvīsatindriyāni – " + _IND_LIST + "."] = twenty_two()


def translate(pali_lines, chapter):
    hand = list(HAND4 if chapter == 4 else HAND5)
    out, section = [], "sutta"
    for pl in pali_lines:
        if not pl.strip():
            out.append("")
            continue
        m = S.ID.search(pl)
        t = S.ID.sub("", pl).rstrip()
        if t.startswith("#### Abhidhammabhājanīyaṃ"):
            section = "abhi"
        elif t.startswith("#### Pañhāpucchakaṃ"):
            section = "q"
        if t in LABELS:
            vi = LABELS[t]
        elif hand and t.startswith(hand[0][0]):
            vi = hand.pop(0)[1]
        elif section == "q":
            vi = (Q4 if chapter == 4 else Q5).line(t)
        elif chapter == 4 and section == "sutta":
            vi = piya_line(t)
        elif chapter == 4:
            vi = abhi4_line(t)
        else:
            vi = mano_line(t)
        assert pl.count(DASH) + pl.count("—") == vi.count(DASH) and "—" not in vi, ("dash count", t[:70], vi[:90])
        for bad in ("là là", "  ", "….", '"', " ,", " .", ":-", "thì thì"):
            assert bad not in vi, (bad, vi[:120])
        out.append(vi + (" " + m.group(1) if m else ""))
    assert not hand, [h[0] for h in hand]
    return out


CHAPTERS = (("4-saccavibhango.md", 4), ("5-indriyavibhango.md", 5))


def build():
    res = {}
    for fn, ch in CHAPTERS:
        pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().rstrip("\n").split("\n")
        res[os.path.join(S.VI_DIR, fn)] = translate(pali, ch)
    return res


def check_same_pali():
    """The ch. 4/5 feeling and eye/body definitions have the same Pāli as ch. 3 (so the same Vietnamese)."""
    p3 = open(os.path.join(S.PALI_DIR, "3-dhatuvibhango.md"), encoding="utf-8").read()
    p4 = open(os.path.join(S.PALI_DIR, "4-saccavibhango.md"), encoding="utf-8").read()
    p5 = open(os.path.join(S.PALI_DIR, "5-indriyavibhango.md"), encoding="utf-8").read()

    def bod(text, head):
        return between(text, head, " " + DASH + " ")
    pairs = ((p4, "Tattha katamaṃ dukkhaṃ? ", "Tattha katamā dukkhadhātu? "),
             (p4, "Tattha katamaṃ domanassaṃ? ", "Tattha katamā domanassadhātu? "),
             (p5, "Tattha katamaṃ sukhindriyaṃ? ", "Tattha katamā sukhadhātu? "),
             (p5, "Tattha katamaṃ dukkhindriyaṃ? ", "Tattha katamā dukkhadhātu? "),
             (p5, "Tattha katamaṃ somanassindriyaṃ? ", "Tattha katamā somanassadhātu? "),
             (p5, "Tattha katamaṃ domanassindriyaṃ? ", "Tattha katamā domanassadhātu? "),
             (p5, "Tattha katamaṃ upekkhindriyaṃ? ", "Tattha katamā upekkhādhātu? "),
             (p5, "Tattha katamaṃ cakkhundriyaṃ? ", "Tattha katamā cakkhudhātu? "))
    for text, h, h3 in pairs:
        assert bod(text, h) == bod(p3, h3), (h, bod(text, h)[:60], bod(p3, h3)[:60])


def main():
    check_same_pali()
    res = build()
    for path, lines in res.items():
        text = "\n".join(lines).rstrip("\n") + "\n"
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("OK:", path, "|", len([l for l in lines if l.strip()]), "non-empty lines")
    for s in sorted(set(SLIPS)):
        print("slip:", s)


if __name__ == "__main__":
    main()
