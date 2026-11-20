# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Vietnamese plain zero-shot: chapter 6 (Paṭiccasamuppādavibhaṅga).

usage: python -I -X utf8 build_6_vi.py
Writes AI_translation\\vietnamese\\pi-2-vietnamese-plain-zeroshot_split_chapters\\6-paticcasamuppadavibhango.md
(only when run as a script; importing writes nothing).

Imports build_ch1_sample_vi (S), build_1_vi (B), build_2-3_vi (T) and build_4-5_vi (F) and reuses their strings
(nothing of theirs is rewritten). The dependent-origination chain is pi-1 ^1-1343 («Vô minh làm điều kiện cho các
sự tạo tác, …»), asserted word for word. Mind-type and jhāna openings are taken verbatim from the pi-1 Vietnamese
rails when the Pāli opening is identical; the other openings are composed from fixed tokens, and the composer is
checked against every pi-1 opening it can parse. Definitions (moho, cetanā, citta, phassa, vedanā, rāga, diṭṭhi,
dosa, vicikicchā, uddhacca, alobha, adosa, amoha, saddhā, upacaya, aniccatā …) are pi-1 strings, asserted. Every
link is generated from fixed noun tables, so every repeat is identical. Unknown Pāli raises KeyError.
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

DASH = S.DASH
cap, low = S.cap, S.low
pi1, between, repl = T.pi1, T.between, T.repl
TATTHA, VUCCATI = S.TATTHA, S.VUCCATI
FN = "6-paticcasamuppadavibhango.md"
SLIPS = []
PI1_PALI_DIR = os.path.join(S.ROOT, r"AI_translation\pali\pi-1_split_chapters")


def _pairs():
    for fn in sorted(os.listdir(PI1_PALI_DIR)):
        if not fn.endswith(".md"):
            continue
        pl = [l for l in open(os.path.join(PI1_PALI_DIR, fn), encoding="utf-8").read().split("\n") if l.strip()]
        vl = [l for l in open(os.path.join(S.PI1_VI_DIR, fn), encoding="utf-8").read().split("\n") if l.strip()]
        assert len(pl) == len(vl), fn
        for a, b in zip(pl, vl):
            yield S.ID.sub("", a), S.ID.sub("", b)


PI1_ALL = "\n".join(v for _, v in _pairs())


def in_pi1(*parts):
    for p in parts:
        assert p in PI1_ALL, "not in pi-1: " + p[:90]


# ================================================================ 1. link nouns  [pi-1 ^1-1343 unless marked]
N = {
    "avijjā": "vô minh",
    "saṅkhāro": "sự tạo tác",                         # sg (Abhidhamma) [pi-1 saṅkhāra]
    "saṅkhārā": "các sự tạo tác",                     # pl (Suttanta) [pi-1 ^1-1343]
    "viññāṇaṃ": "thức",
    "nāmaṃ": "phần tinh thần",                        # [pi-1 ^1-1316]
    "rūpaṃ": "vật chất",
    "nāmarūpaṃ": "phần tinh thần và vật chất",
    "saḷāyatanaṃ": "sáu lĩnh vực nhận biết",
    "chaṭṭhāyatanaṃ": "lĩnh vực nhận biết thứ sáu",   # [new]
    "phasso": "sự tiếp xúc",
    "vedanā": "cảm giác",
    "taṇhā": "khao khát",
    "upādānaṃ": "sự bám víu",
    "bhavo": "sự hiện hữu",
    "jāti": "sự sinh",
    "jarāmaraṇaṃ": "sự lão hóa và sự chết",
    "adhimokkho": "sự quyết định",                    # [new]
    "paṭighaṃ": "sự ác cảm",                          # [pi-1 ^1-413 paṭighasampayutta]
    "vicikicchā": "sự hoài nghi",                     # [pi-1 termbase]
    "uddhaccaṃ": "sự xao động",                       # [pi-1 termbase]
    "pasādo": "lòng tin trong sáng",                  # [new]
}
STEM = {"avijjā": "avijjā", "saṅkhāra": "saṅkhāro", "viññāṇa": "viññāṇaṃ", "nāma": "nāmaṃ", "nāmarūpa": "nāmarūpaṃ",
        "chaṭṭhāyatana": "chaṭṭhāyatanaṃ", "saḷāyatana": "saḷāyatanaṃ", "phassa": "phasso", "vedanā": "vedanā",
        "taṇhā": "taṇhā", "upādāna": "upādānaṃ", "bhava": "bhavo", "jāti": "jāti", "adhimokkha": "adhimokkho",
        "paṭigha": "paṭighaṃ", "vicikicchā": "vicikicchā", "uddhacca": "uddhaccaṃ", "pasāda": "pasādo"}
KUSALAMULA = "các gốc rễ thiện"            # kusalamūlā [pi-1 «gốc rễ thiện»; «các» as the plural answer]
AKUSALAMULA = "các gốc rễ bất thiện"       # akusalamūla- [pi-1 words]
COND_EXTRA = {"kusalamūla": KUSALAMULA, "akusalamūla": AKUSALAMULA}
SUTTA = {"on": False}   # Suttantabhājanīya: saṅkhāra- as a condition is plural (pi-1 «các sự tạo tác làm điều kiện cho»)
CAUSE = "làm nguyên nhân"     # Xhetuka = «có X làm nguyên nhân» [pi-1 APPROVED cittahetukaṃ «có tâm làm nguyên nhân»]
in_pi1("có tâm làm nguyên nhân")
SAMP = "gắn liền với"         # Xsampayutta [pi-1]
COND = "làm điều kiện cho"    # Xpaccayā Y (chain) [pi-1 ^1-1343]
BY = "làm điều kiện"          # Y do X làm điều kiện (name) [ch1 «… do sự tiếp xúc của mắt làm điều kiện»]


def cond(stem):
    if stem in COND_EXTRA:
        return COND_EXTRA[stem]
    if stem == "saṅkhāra" and SUTTA["on"]:
        return N["saṅkhārā"]
    return N[STEM[stem]]


LINK = re.compile(r"^(\w+?)paccayā(pi)? (\w+)(?: (\w+?)(hetuk|sampayutt)(?:o|aṃ|ā))?(?: (nāmaṃ|chaṭṭhāyatanaṃ))?$")
GRIEF_LINK = "jātipaccayā jarāmaraṇaṃ sokaparidevadukkhadomanassupāyāsā sambhavanti"
GRIEF_LINK_VI = f"{N['jāti']} {COND} {N['jarāmaraṇaṃ']}, {F.SOKA5} sinh khởi"   # [pi-1 ^1-1343]


def link(s, mode):
    """mode "chain": «X làm điều kiện cho Y …»; mode "nom": «Y do X làm điều kiện …» (question / answer name)."""
    if s == GRIEF_LINK and mode == "chain":
        return GRIEF_LINK_VI
    m = LINK.match(s)
    if not m:
        raise KeyError("link: " + s)
    stem, pi, res, qstem, qkind, apo = m.groups()
    c, y = cond(stem), N[res]
    if mode == "chain":
        out = f"{c} {'cũng ' if pi else ''}{COND} {y}"
    else:
        out = f"{y} {'cũng ' if pi else ''}do {c} {BY}"
    if qkind and apo:   # "nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ": its nāma is associated with viññāṇa
        out += f", trong đó {N[apo]} {SAMP} {N[STEM[qstem]]}"
    elif qkind:
        z = N[STEM[qstem]]
        tail = f"có {z} {CAUSE}" if qkind == "hetuk" else f"{SAMP} {z}"
        out += f" {tail}" if mode == "chain" else f", {tail}"
    return out


def chain(s):
    """links separated by ', ' / '; ' / '…pe… ' (Pāli punctuation kept)."""
    parts = re.split(r"(, |; |…pe… )", low(s))
    out = []
    for p in parts:
        if p in (", ", "; "):
            out.append(p)
        elif p == "…pe… ":
            out.append("… ")
        else:
            out.append(link(p, "chain"))
    return "".join(out)


# ================================================================ 2. fixed sentences
EVAM_LOW = "như vậy là sự phát sinh của toàn bộ khối khổ đau này"   # [pi-1 ^1-1343]
in_pi1(EVAM_LOW)
EVAM = cap(EVAM_LOW) + "."
EVAM_D_LOW = "như vậy là sự phát sinh của những hiện tượng này"    # Evametesaṃ dhammānaṃ samudayo hoti [new]
EVAM_D = cap(EVAM_D_LOW) + "."
HOTI4 = "có sự kết hợp, có sự hội tụ, có sự tụ hợp, có sự xuất hiện"   # saṅgati hoti, samāgamo hoti, samodhānaṃ hoti,
MEANS = f"như vậy {HOTI4} của toàn bộ khối khổ đau này"                 # pātubhāvo hoti [new; samodhāna ch4 «sự tụ hợp»]
MEANS_D = f"như vậy {HOTI4} của những hiện tượng này"
TENA = "vì thế nên mới nói rằng"                                        # tena vuccati "…"ti [new]
KAMMABHAVA, UPAPATTIBHAVA = "sự hiện hữu dưới dạng nghiệp", "sự hiện hữu dưới dạng tái sinh"   # [new]
ABHI = {"puñña": "sự tạo tác thuộc về phước", "apuñña": "sự tạo tác không thuộc về phước",      # [new]
        "āneñja": "sự tạo tác dẫn đến trạng thái bất động"}
KSANKHARA = {"kāya": "sự tạo tác bằng thân", "vacī": "sự tạo tác bằng lời nói", "citta": "sự tạo tác bằng tâm"}   # [new;
SANCETANA = {"kāya": "sự cố ý bằng thân", "vacī": "sự cố ý bằng lời nói", "mano": "sự cố ý bằng ý"}   # pi-1 viññatti «bằng»]
in_pi1("sự biểu lộ bằng thân", "sự biểu lộ bằng lời nói")
ALOBHA_N, ADOSA_N, AMOHA_N = "sự không tham lam", "sự không sân hận", "sự không si mê"   # [pi-1 ^1-32 … ^1-34]
SENT = {
    "Evametassa kevalassa dukkhakkhandhassa samudayo hoti.": EVAM,
    "Evametesaṃ dhammānaṃ samudayo hoti.": EVAM_D,
    ("Evametassa kevalassa dukkhakkhandhassa samudayo hotīti, evametassa kevalassa dukkhakkhandhassa saṅgati hoti, "
     "samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti."): f"“{cap(EVAM_LOW)}”: {MEANS}.",
    "Evametassa kevalassa dukkhakkhandhassa samudayo hotīti.": f"“{cap(EVAM_LOW)}”.",
    "Evametassa kevalassa dukkhakkhandhassa saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.":
        f"{cap(MEANS)}.",
    "Evametesaṃ dhammānaṃ samudayo hotīti.": f"“{cap(EVAM_D_LOW)}”.",
    "Evametesaṃ dhammānaṃ saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.": f"{cap(MEANS_D)}.",
    'Tena vuccati "evametassa kevalassa dukkhakkhandhassa samudayo hotī"ti.': f"{cap(TENA)} “{EVAM_LOW}”.",
    'Tena vuccati "evametesaṃ dhammānaṃ samudayo hotī"ti.': f"{cap(TENA)} “{EVAM_D_LOW}”.",
    "Atthi nāmaṃ, atthi rūpaṃ.": f"Có {N['nāmaṃ']}, có {N['rūpaṃ']}.",
    "Atthi jarā, atthi maraṇaṃ.": "Có sự lão hóa, có sự chết.",
    "Iti idañca nāmaṃ, idañca rūpaṃ.": f"Như vậy, đây là {N['nāmaṃ']}, và đây là {N['rūpaṃ']}.",
    "Iti ayañca jarā, idañca maraṇaṃ.": "Như vậy, đây là sự lão hóa, và đây là sự chết.",
    "Iti ayañca kammabhavo, ayañca upapattibhavo.": f"Như vậy, đây là {KAMMABHAVA}, và đây là {UPAPATTIBHAVA}.",
    "Bhavo duvidhena – atthi kammabhavo, atthi upapattibhavo.":
        f"Phân loại {N['bhavo']} {B.by_groups(2)} {DASH} {B.ATTHI} là {KAMMABHAVA}, {B.ATTHI} là {UPAPATTIBHAVA}.",
    "Sabbampi bhavagāmikammaṃ kammabhavo.": f"Tất cả nghiệp dẫn đến sự hiện hữu cũng đều là {KAMMABHAVA}.",
    "Kāyasañcetanā kāyasaṅkhāro, vacīsañcetanā vacīsaṅkhāro, manosañcetanā cittasaṅkhāro.":
        (f"{cap(SANCETANA['kāya'])} là {KSANKHARA['kāya']}, {SANCETANA['vacī']} là {KSANKHARA['vacī']}, "
         f"{SANCETANA['mano']} là {KSANKHARA['citta']}."),
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro, kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāro.":
        cap(", ".join(list(ABHI.values()) + list(KSANKHARA.values()))) + ".",
    "Alobho, adoso, amoho.": cap(f"{ALOBHA_N}, {ADOSA_N}, {AMOHA_N}") + ".",
    "Alobho, adoso.": cap(f"{ALOBHA_N}, {ADOSA_N}") + ".",
    "Katame dhammā akusalā?": "Những hiện tượng nào là bất thiện?",                       # [pi-1 ^1-365]
    "Katame dhammā kusalā?": "Những hiện tượng nào là thiện?",                            # [pi-1 ^1-1]
    "Katame dhammā abyākatā?": "Những hiện tượng nào không xác định về mặt đạo đức?",     # [pi-1 ^1-431]
    "Tattha katamo alobho…pe… adoso…pe… amoho?": f"{TATTHA} {ALOBHA_N}… {ADOSA_N}… {AMOHA_N} là gì?",
}
in_pi1(*(SENT[k] for k in ("Katame dhammā akusalā?", "Katame dhammā kusalā?", "Katame dhammā abyākatā?")))

TERM = {   # names in questions / answers
    "puññābhisaṅkhāro": ABHI["puñña"], "apuññābhisaṅkhāro": ABHI["apuñña"], "āneñjābhisaṅkhāro": ABHI["āneñja"],
    "kāyasaṅkhāro": KSANKHARA["kāya"],
    "kammabhavo": KAMMABHAVA, "upapattibhavo": UPAPATTIBHAVA,
    "jarā": "sự lão hóa", "maraṇaṃ": "sự chết",                                  # [pi-1 / ch4]
    "soko": "sự sầu muộn", "paridevo": "sự than khóc", "dukkhaṃ": F.PAIN,          # [ch4]
    "domanassaṃ": F.SADNESS, "upāyāso": F.DESPAIR,
    "kusalamūlā": KUSALAMULA,
    "alobho": ALOBHA_N, "adoso": ADOSA_N, "amoho": AMOHA_N,
}
for _k in ("avijjā", "saṅkhāro", "nāmaṃ", "rūpaṃ", "nāmarūpaṃ"):
    TERM[_k] = N[_k]


def term(t):
    return TERM[t] if t in TERM else link(t, "nom")


def called(t, quoted=True, dash=False):
    d = f" {DASH}" if dash else ""
    name = term(t)
    return f"{VUCCATI}{d} “{name}”" if quoted else f"{VUCCATI}{d} {name}"


def question(t):
    name = term(t)
    return f"{TATTHA} {name}{',' if ',' in name else ''} là gì?"   # (ch2 RUPA_NN_Q: comma before «là gì» after a comma)


# ================================================================ 3. answer bodies  [pi-1 strings unless marked]
WHAT = "Điều mà là "                                                       # Yo / Yā / Yaṃ … [ch3-5]
CITTA10, CITTA3 = T.CITTA10, T.CITTA3
TAJJA = {"manoviññāṇa": "yếu tố ý thức", "mano": "yếu tố ý", "cakkhuviññāṇa": "yếu tố thức qua mắt",
         "kāyaviññāṇa": "yếu tố thức qua thân"}
for _v in TAJJA.values():
    in_pi1(_v + " tương ứng")
MOHA_PE = F.pe_cut(T.AVIJJA, 2, "then cài vô minh")                      # aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusalamūlaṃ
assert MOHA_PE == "sự không biết, sự không thấy… then cài vô minh, sự si mê, tức gốc rễ bất thiện", MOHA_PE
CETANA = between(pi1("1-5"), "Điều mà vào lúc ấy là ", f" {DASH} đó là")
CETANA = repl(repl(CETANA, " sinh từ sự tiếp xúc của yếu tố ý thức tương ứng", ""),
              " [dị bản (Syā.): sañcetayitattaṃ]", "")
assert CETANA == "chủ ý, sự cố ý, trạng thái đã cố ý", CETANA            # cetanā sañcetanā (sañ)cetayitattaṃ
VAR_CETAYI = " [dị bản (Sī., Ka.): cetayitattaṃ]"                         # as pi-1 ^1-5 «dị bản»
PHASSA = between(pi1("1-2"), "Điều mà vào lúc ấy là ", f" {DASH} đó là")   # phasso phusanā samphusanā samphusitattaṃ
RAGA = repl(between(pi1("1-1065"), "Điều mà là ", ", sự mong muốn"), " [khác chính tả (Sī.): nandirāgo]", "")
assert RAGA.endswith("sự tham đắm vì thích thú, sự say đắm của tâm") and RAGA.count(", ") == 6, RAGA
DITTHI = between(pi1("1-392"), "Điều mà vào lúc ấy là ", f" {DASH} đó là quan điểm sai lầm")
DITTHI_PE = F.pe_cut(DITTHI, 2, "lĩnh vực của các học thuyết ngoại đạo")
VAR_VIPARIYESA = " [khác chính tả (nhiều ấn bản): vipariyesaggāho]"       # (bahūsu)
DOSA_HEAD, DOSA_TAIL = "sự oán giận của tâm", "sự hung dữ, sự nói năng cộc cằn, sự không hài lòng của tâm"   # ^1-1066
assert "là " + DOSA_HEAD in pi1("1-1066") and DOSA_TAIL + f" {DASH}" in pi1("1-1066")
VICI = between(F.pi1_line("2-04-cittuppadakandam.md", "Katamā tasmiṃ samaye vicikicchā hoti?"),
               "Điều mà vào lúc ấy là ", f" {DASH} đó là sự hoài nghi")
UDDH = between(F.pi1_line("2-04-cittuppadakandam.md", "Katamaṃ tasmiṃ samaye uddhaccaṃ hoti?"),
               "Điều mà vào lúc ấy là ", f" {DASH} đó là sự xao động")
ALOBHA = between(pi1("1-32"), "Điều mà vào lúc ấy là ", f" {DASH} đó là")
ADOSA = repl(between(pi1("1-33"), "Điều mà vào lúc ấy là ", f" {DASH} đó là"),
             " [khác chính tả (Syā.): adūsanā adūsitattaṃ]", "")
SADDHA4 = ", ".join(between(pi1("1-12"), "Điều mà vào lúc ấy là ", f" {DASH}").split(", ")[:4])
assert SADDHA4 == "niềm tin, sự tin tưởng, sự tin chắc, lòng tin sâu sắc", SADDHA4
ADHIMOKKHA = "sự quyết định của tâm, sự khởi quyết định, trạng thái đã quyết định về điều đó"   # [new]
AVIJJA4 = between(pi1("1-1238"), "là gì? ", ", sự không biết về quá khứ")   # Dukkhe aññāṇaṃ, … paṭipadāya aññāṇaṃ
assert low(AVIJJA4).count("sự không biết về") == 4 and AVIJJA4.startswith("Sự"), AVIJJA4
AGG = {k: S.AGG[k]["khandha"] for k in ("vedana", "sanna", "sankhara", "vinnana")}
AGG3 = f"{AGG['vedana']}, {AGG['sanna']}, {AGG['sankhara']}"
AGG4 = f"{AGG3}, {AGG['vinnana']}"
EXCEPT = "ngoại trừ"                                                     # ṭhapetvā [pi-1 termbase]
in_pi1("ngoại trừ khối cảm giác")
OF_EACH = "Điều mà ở từng hiện tượng là "                                 # Yā/Yo tesaṃ tesaṃ dhammānaṃ … [new; ch4 «ở từng chúng sinh»]
JATI_D = "sự sinh, sự sinh ra, sự phát khởi, sự hình thành, sự xuất hiện"   # jāti sañjāti nibbatti abhinibbatti pātubhāvo
JARA_D = "sự lão hóa, sự hao mòn, sự suy giảm tuổi thọ"                    # jarā jīraṇatā āyuno saṃhāni [pi-1 ^1-643 words]
MARANA_D = between(pi1("1-644"), "Điều mà ở vật chất là ", f" {DASH} vật chất này")   # khayo vayo … antaradhānaṃ [^1-644]
assert MARANA_D == "sự hủy diệt, sự suy tàn, sự tan rã, sự tan rã hoàn toàn, tính vô thường, sự biến mất", MARANA_D
for _x in JARA_D.split(", "):
    assert _x in F.JARA, _x
UPACAYA = (", ".join(f"sự tăng trưởng của {T.AYATANA[a]}" for a in ("cakkhāyatanaṃ", "sotāyatanaṃ", "ghānāyatanaṃ",
                                                                    "jivhāyatanaṃ", "kāyāyatanaṃ"))
           + ", hoặc còn có bất cứ vật chất nào khác sinh từ tâm, có tâm làm nguyên nhân, do tâm sinh ra")
in_pi1("sự tăng trưởng của vật chất",
       "hoặc còn có bất cứ vật chất nào khác sinh từ tâm, có tâm làm nguyên nhân, do tâm sinh ra")   # ^1-641, ^1-666
NISSAYA = "vật chất mà yếu tố ý thức dựa vào để vận hành"                  # yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati [new]
VINN6 = cap(S.VINNANA6)
AYAT6 = cap(", ".join(T.AYATANA[a] for a in ("cakkhāyatanaṃ", "sotāyatanaṃ", "ghānāyatanaṃ", "jivhāyatanaṃ",
                                              "kāyāyatanaṃ", "manāyatanaṃ")))
PHASSA6 = cap(", ".join(F.SUBJ4[d + "samphasso"] for d in F.DOOR_P))
VEDANA6 = cap(", ".join(B.SUBJ[d + "samphassajā vedanā"] for d in F.DOOR_P))
TANHA6 = cap(", ".join(F.SUBJ4[o + "taṇhā"] for o in T.OBJ))
in_pi1(low(TANHA6))
UPADANA4 = between(pi1("1-1219"), f"Bốn sự bám víu {DASH} ", " [khác chính tả")
BHAVA9 = ("Sự hiện hữu trong cõi dục lạc, sự hiện hữu trong cõi hình sắc, sự hiện hữu trong cõi không hình sắc, "
          "sự hiện hữu có tri giác, sự hiện hữu không có tri giác, sự hiện hữu không phải có tri giác cũng không phải "
          "không có tri giác, sự hiện hữu gồm một khối, sự hiện hữu gồm bốn khối, sự hiện hữu gồm năm khối")   # [new]
KUSALA_CETANA = ("Chủ ý thiện thuộc cõi dục lạc, thuộc cõi hình sắc, được tạo nên từ sự bố thí, được tạo nên từ "
                 "giới hạnh, được tạo nên từ sự tu tập")                   # [new; pi-1 kāmāvacara / rūpāvacara]
in_pi1("thuộc cõi dục lạc", "thuộc cõi hình sắc", "thuộc cõi không hình sắc")


def hand4_body(prefix):
    """the ch. 4 Vietnamese definition body (between «là gì? » and « – đó được gọi là»)."""
    hits = [v for p, v in F.HAND4 if p.startswith(prefix)]
    assert len(hits) == 1, prefix
    return between(hits[0], "là gì? ", f" {DASH} {VUCCATI}")


JATI_S = hand4_body("Tattha katamā jāti?")
JARA_S = hand4_body("Tattha katamā jarā?")
MARANA_S = repl(hand4_body("Tattha katamaṃ maraṇaṃ?"), "sự qua đời,", "sự qua đời [khác chính tả (Ka.): kālaṃkiriyā],")
SOKA_S = hand4_body("Tattha katamo soko?")
PARIDEVA_S = repl(hand4_body("Tattha katamo paridevo?"), " [khác chính tả (Syā.): lālapo lālapanā lālapitattaṃ]", "")
UPAYASA_S = hand4_body("Tattha katamo upāyāso?")
FEEL = {"somanassa": T.feel_body("1-3", T.TAJJA_M), "upekkha": T.feel_body("1-152", T.TAJJA_M),
        "domanassa": F.FEEL_DOMAN, "sukha": T.feel_body("1-445", T.TAJJA_K), "dukkha": F.FEEL_DUKKHA}

BYA = ("Ñātibyasanena vā phuṭṭhassa, bhogabyasanena vā phuṭṭhassa, rogabyasanena vā phuṭṭhassa, sīlabyasanena vā "
       "phuṭṭhassa, diṭṭhibyasanena vā phuṭṭhassa, aññataraññatarena byasanena samannāgatassa, aññataraññatarena "
       "dukkhadhammena phuṭṭhassa ")
BODY = {
    # --- Suttantabhājanīya
    "Dukkhe aññāṇaṃ, dukkhasamudaye aññāṇaṃ, dukkhanirodhe aññāṇaṃ, dukkhanirodhagāminiyā paṭipadāya aññāṇaṃ": AVIJJA4,
    "Kusalā cetanā kāmāvacarā rūpāvacarā dānamayā sīlamayā bhāvanāmayā": KUSALA_CETANA,
    "Akusalā cetanā kāmāvacarā": "Chủ ý bất thiện thuộc cõi dục lạc",
    "Kusalā cetanā arūpāvacarā": "Chủ ý thiện thuộc cõi không hình sắc",
    "Cakkhuviññāṇaṃ, sotaviññāṇaṃ, ghānaviññāṇaṃ, jivhāviññāṇaṃ, kāyaviññāṇaṃ, manoviññāṇaṃ": VINN6,
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho": cap(AGG3),
    "Cattāro mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ": cap(S.MAHABHUTA),
    "Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, manāyatanaṃ": AYAT6,
    "Cakkhusamphasso sotasamphasso ghānasamphasso jivhāsamphasso kāyasamphasso manosamphasso": PHASSA6,
    ("Cakkhusamphassajā vedanā, sotasamphassajā vedanā, ghānasamphassajā vedanā, jivhāsamphassajā vedanā, "
     "kāyasamphassajā vedanā, manosamphassajā vedanā"): VEDANA6,
    "Rūpataṇhā, saddataṇhā, gandhataṇhā, rasataṇhā, phoṭṭhabbataṇhā, dhammataṇhā": TANHA6,
    "Kāmupādānaṃ, diṭṭhupādānaṃ, sīlabbatupādānaṃ, attavādupādānaṃ": cap(UPADANA4),
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro": cap(", ".join(ABHI.values())),
    ("Kāmabhavo, rūpabhavo, arūpabhavo, saññābhavo, asaññābhavo, nevasaññānāsaññābhavo, ekavokārabhavo, "
     "catuvokārabhavo, pañcavokārabhavo"): BHAVA9,
    ("Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jāti sañjāti okkanti abhinibbatti, khandhānaṃ pātubhāvo, "
     "āyatanānaṃ paṭilābho"): JATI_S,
    ("Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni "
     "indriyānaṃ paripāko"): JARA_S,
    ("Yā tesaṃ tesaṃ sattānaṃ tamhā tamhā sattanikāyā cuti cavanatā bhedo antaradhānaṃ maccu maraṇaṃ kālakiriyā "
     "[kālaṃkiriyā (ka.)] khandhānaṃ bhedo kaḷevarassa nikkhepo jīvitindriyassupacchedo"): MARANA_S,
    BYA + "soko socanā socitattaṃ antosoko antoparisoko cetaso parijjhāyanā domanassaṃ sokasallaṃ": SOKA_S,
    (BYA + "ādevo paridevo ādevanā paridevanā ādevitattaṃ paridevitattaṃ vācā palāpo vippalāpo lālappo lālappanā "
     "lālappitattaṃ"): PARIDEVA_S,
    "Yaṃ kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā vedanā":
        WHAT + FEEL["dukkha"],
    ("Yaṃ cetasikaṃ asātaṃ, cetasikaṃ dukkhaṃ, cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ, cetosamphassajā asātā "
     "dukkhā vedanā"): WHAT + FEEL["domanassa"],
    BYA + "āyāso upāyāso āyāsitattaṃ upāyāsitattaṃ": UPAYASA_S,
    # --- Abhidhammabhājanīya
    "Yaṃ aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusalamūlaṃ": WHAT + MOHA_PE,
    "Yā cetanā sañcetanā sañcetayitattaṃ [cetayitattaṃ (sī. ka.)]": WHAT + CETANA + VAR_CETAYI,
    "Yā cetanā sañcetanā sañcetayitattaṃ": WHAT + CETANA,
    ("Yaṃ cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
     "tajjāmanoviññāṇadhātu"): f"{WHAT}{CITTA10}, {TAJJA['manoviññāṇa']} tương ứng",
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho": cap(AGG4),
    "Yo phasso phusanā samphusanā samphusitattaṃ": WHAT + PHASSA,
    "Yaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        WHAT + FEEL["somanassa"],
    "Yaṃ cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā vedanā":
        WHAT + FEEL["domanassa"],
    ("Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā "
     "vedanā"): WHAT + FEEL["upekkha"],
    ("Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ, cetosamphassajā adukkhamasukhā "
     "vedanā"): WHAT + FEEL["upekkha"],
    "Yaṃ kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā":
        WHAT + FEEL["sukha"],
    "Yo rāgo sārāgo anunayo anurodho nandī nandirāgo cittassa sārāgo": WHAT + RAGA,
    "Yo rāgo sārāgo…pe… cittassa sārāgo": WHAT + F.pe_cut(RAGA, 2, "sự say đắm của tâm"),
    "Yo rāgo…pe… cittassa sārāgo": WHAT + F.pe_cut(RAGA, 1, "sự say đắm của tâm"),
    ("Yā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho "
     "patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho "
     "[vipariyesaggāho (bahūsu)]"): WHAT + DITTHI + VAR_VIPARIYESA,
    "Yā diṭṭhi diṭṭhigataṃ…pe… titthāyatanaṃ vipariyāsaggāho": WHAT + DITTHI_PE,
    "Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbatti pātubhāvo": OF_EACH + JATI_D,
    "Yā tesaṃ tesaṃ dhammānaṃ jarā jīraṇatā āyuno saṃhāni": OF_EACH + JARA_D,
    "Yo tesaṃ tesaṃ dhammānaṃ khayo vayo bhedo paribhedo aniccatā antaradhānaṃ": OF_EACH + MARANA_D,
    ("Cakkhāyatanassa upacayo, sotāyatanassa upacayo, ghānāyatanassa upacayo, jivhāyatanassa upacayo, "
     "kāyāyatanassa upacayo, yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ"): cap(UPACAYA),
    "Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati": cap(NISSAYA),
    "Cattāro ca mahābhūtā, yañca rūpaṃ nissāya manoviññāṇadhātu vattati": f"Bốn yếu tố cơ bản, và {NISSAYA}",
    "Yo cittassa adhimokkho adhimuccanā tadadhimuttatā": WHAT + ADHIMOKKHA,
    "Yo cittassa āghāto…pe… caṇḍikkaṃ asuropo [asulopo (syā.)] anattamanatā cittassa":
        f"{WHAT}{DOSA_HEAD}… " + repl(DOSA_TAIL, "cộc cằn,", "cộc cằn [khác chính tả (Syā.): asulopo],"),
    ("Yā kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvidhāpatho [dvedhāpatho (sī. syā.)] saṃsayo "
     "anekaṃsaggāho āsappanā parisappanā apariyogāhaṇā [apariyogāhanā (sī. syā. ka.)] chambhitattaṃ cittassa "
     "manovilekho"):
        WHAT + repl(repl(VICI, "ngã ba đường,", "ngã ba đường [khác chính tả (Sī., Syā.): dvedhāpatho],"),
                    "không đi sâu,", "không đi sâu [khác chính tả (Sī., Syā., Ka.): apariyogāhanā],"),
    "Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": WHAT + UDDH,
    "Yo alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ": WHAT + ALOBHA,
    "Yo adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ": WHAT + ADOSA,
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": WHAT + F.PANNA,
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        WHAT + F.ABHI_BODY["Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ "
                           "maggapariyāpannaṃ"],
    "Yā saddhā saddahanā okappanā abhippasādo": WHAT + SADDHA4,
    "Alobho, adoso, amoho": cap(f"{ALOBHA_N}, {ADOSA_N}, {AMOHA_N}"),
    "Alobho, adoso": cap(f"{ALOBHA_N}, {ADOSA_N}"),
}
for _d, _k in (("manodhātu", "mano"), ("manoviññāṇadhātu", "manoviññāṇa"), ("cakkhuviññāṇadhātu", "cakkhuviññāṇa"),
               ("kāyaviññāṇadhātu", "kāyaviññāṇa")):
    BODY[f"Yaṃ cittaṃ mano mānasaṃ…pe… tajjā{_d}"] = f"{WHAT}{CITTA3}… {TAJJA[_k]} tương ứng"
for _x, _v in (("upādānaṃ", N["upādānaṃ"]), ("phassaṃ", N["phasso"]), ("adhimokkhaṃ", N["adhimokkho"]),
               ("vicikicchaṃ", N["vicikicchā"])):
    BODY[f"Ṭhapetvā {_x}, vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho"] = \
        f"{cap(EXCEPT)} {_v}, {AGG4}"
BODY["Ṭhapetvā adhimokkhaṃ, vedanākkhandho saññākkhandho saṅkhārakkhandho, viññāṇakkhandho"] = \
    f"{cap(EXCEPT)} {N['adhimokkho']}, {AGG4}"
BODY["Ṭhapetvā vedanaṃ, saññākkhandho saṅkhārakkhandho viññāṇakkhandho"] = \
    f"{cap(EXCEPT)} {N['vedanā']}, {AGG['sanna']}, {AGG['sankhara']}, {AGG['vinnana']}"
assert ALOBHA.startswith(ALOBHA_N + ",") and ADOSA.startswith(ADOSA_N + ",")
assert F.PANNA.startswith("trí tuệ, sự hiểu rõ…") and F.PANNA.endswith("sự không si mê, sự tìm hiểu các hiện tượng, "
                                                                      "quan điểm đúng đắn")


def check_ch4_bodies():
    """the ch. 6 Suttanta bodies have the ch. 4 Pāli (commas and the kālaṃkiriyā variant aside)."""
    p4 = open(os.path.join(S.PALI_DIR, "4-saccavibhango.md"), encoding="utf-8").read()
    for k in BODY:
        if k.startswith(("Yā tesaṃ tesaṃ sattānaṃ", "Ñātibyasanena", "Yaṃ kāyikaṃ asātaṃ", "Yaṃ cetasikaṃ asātaṃ,")):
            bare = k.replace(",", "").replace(" [kālaṃkiriyā (ka.)]", "")
            assert bare in p4.replace(",", ""), k[:60]


# ================================================================ 4. mind-type and jhāna openings
def _openings():
    """pi-1 Pāli opening -> Vietnamese, for "Yasmiṃ samaye …, tasmiṃ samaye" and "Tasseva …, tasmiṃ samaye"."""
    yas, tas = {}, {}
    for p, v in _pairs():
        if "Yasmiṃ samaye " in p and ", tasmiṃ samaye" in p and "Vào lúc " in v and ", thì vào lúc ấy" in v:
            pk = between(p, "Yasmiṃ samaye ", ", tasmiṃ samaye")
            vk = between(v, "Vào lúc ", ", thì vào lúc ấy")
            assert yas.get(pk, vk) == vk, pk
            yas[pk] = vk
        if "Tasseva " in p and "Còn khi " in v:
            pk = between(p, "Tasseva ", ", tasmiṃ samaye")
            vk = "Còn khi " + between(v, "Còn khi ", ", thì vào lúc ấy")
            assert tas.get(pk, vk) == vk, pk
            tas[pk] = vk
    return yas, tas


PI1_OPEN, PI1_TASSEVA = _openings()
SUBJ_C = {"cakkhuviññāṇaṃ": "thức qua mắt", "sotaviññāṇaṃ": "thức qua tai", "ghānaviññāṇaṃ": "thức qua mũi",
          "jivhāviññāṇaṃ": "thức qua lưỡi", "kāyaviññāṇaṃ": "thức qua thân", "manodhātu": "yếu tố ý",
          "manoviññāṇadhātu": "yếu tố ý thức"}                                            # [pi-1]
VIP = {"kāmāvacarassa kusalassa": "là quả của nghiệp thiện thuộc cõi dục lạc đã được tạo và tích lũy",
       "akusalassa": "là quả của nghiệp bất thiện đã được tạo và tích lũy"}              # [pi-1 ^1-431, ^1-556]
KIRIYA = "mang tính chức năng, không phải thiện, không phải bất thiện, cũng không phải quả của nghiệp"   # [pi-1]
SAHA = {"somanassa": "niềm vui", "upekkhā": "sự bình thản", "domanassa": "nỗi buồn",
        "sukha": "sự dễ chịu", "dukkha": "sự khó chịu"}   # sukha / dukkha only with body consciousness (pi-1 ^1-443, ^1-556)
SAMPA = {"diṭṭhigata": "sự mắc kẹt trong các quan điểm", "paṭigha": "sự ác cảm", "vicikicchā": "sự hoài nghi",
         "uddhacca": "sự xao động", "ñāṇa": "hiểu biết"}
OBJ_V = {"rūp": "hình sắc", "sadd": "âm thanh", "gandh": "mùi", "ras": "vị", "phoṭṭhabb": "vật xúc chạm",
         "dhamm": "đối tượng của ý"}
OBJ_KEYS = ("rūp", "sadd", "gandh", "ras", "phoṭṭhabb", "dhamm")
A = r"(?:aṃ|ā)"
HAS = "có đối tượng là "
ANY = "hoặc lấy bất cứ thứ gì làm đối tượng"
FULL6 = "".join(f"{s}ārammaṇ{A} vā " for s in OBJ_KEYS) + "yaṃ yaṃ vā panārabbha"
FULL5 = "".join(f"{s}ārammaṇ{A} vā " for s in OBJ_KEYS[:5]) + "yaṃ yaṃ vā panārabbha"
TOKENS = [   # (regex, function(match) -> Vietnamese)
    (r"(kāmāvacarassa kusalassa|akusalassa) kammassa katattā upacitattā vipāk" + A + r" (\w+) uppann" + A + " hoti",
     lambda m: f"{SUBJ_C[m.group(2)]} sinh khởi, {VIP[m.group(1)]}"),
    (r"kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti", lambda m: "tâm thiện thuộc cõi dục lạc sinh khởi"),
    (r"akusalaṃ cittaṃ uppannaṃ hoti", lambda m: "tâm bất thiện sinh khởi"),
    (r"(\w+) uppann" + A + r" hoti kiriyā neva kusalā nākusalā na ca kammavipākā",
     lambda m: f"{SUBJ_C[m.group(1)]} sinh khởi, {KIRIYA}"),
    (r"(\w+) uppann" + A + r" hoti", lambda m: f"{SUBJ_C[m.group(1)]} sinh khởi"),
    (r"(somanassa|upekkhā|domanassa|sukha|dukkha)sahagat" + A, lambda m: f"có {SAHA[m.group(1)]} đi kèm"),
    (r"(diṭṭhigata|paṭigha|vicikicchā|uddhacca|ñāṇa)(sam|vip)payutt" + A,
     lambda m: ("" if m.group(2) == "sam" else "không ") + f"{SAMP} {SAMPA[m.group(1)]}"),
    (r"sasaṅkhārena", lambda m: "có sự thúc đẩy"),
    (FULL6, lambda m: HAS + ", hay ".join(OBJ_V[k] for k in OBJ_KEYS) + ", " + ANY),
    (FULL5, lambda m: HAS + ", hay ".join(OBJ_V[k] for k in OBJ_KEYS[:5]) + ", " + ANY),
    (r"rūpārammaṇ" + A + r" vā…pe… (dhamm|phoṭṭhabb)ārammaṇ" + A + r" vā yaṃ yaṃ vā panārabbha",
     lambda m: f"{HAS}hình sắc… hay {OBJ_V[m.group(1)]}, {ANY}"),
    (r"rūpārammaṇ" + A + r" vā…pe… yaṃ yaṃ vā panārabbha", lambda m: f"{HAS}hình sắc… {ANY}"),
    (r"rūpārammaṇ" + A + r" vā…pe… (dhamm|phoṭṭhabb)ārammaṇ" + A + r" vā(?=…pe…)",
     lambda m: f"{HAS}hình sắc… hay {OBJ_V[m.group(1)]}"),
    (r"rūpārammaṇ" + A + r" vā(?=…pe…)", lambda m: f"{HAS}hình sắc"),
    (r"(rūp|sadd|gandh|ras|phoṭṭhabb)ārammaṇaṃ", lambda m: HAS + OBJ_V[m.group(1)]),
]
TOKENS = [(re.compile(p), f) for p, f in TOKENS]


def compose(s):
    """kāma-sphere mind-type openings -> «tâm bất thiện sinh khởi, có niềm vui đi kèm, …» (after «Vào lúc »)."""
    out, rest, join = [], s, None
    while rest:
        for rx, fn in TOKENS:
            m = rx.match(rest)
            if m:
                if out:
                    out.append(join)
                out.append(fn(m))
                rest = rest[m.end():]
                break
        else:
            raise KeyError("opening: " + rest[:80])
        if not rest:
            break
        if rest.startswith("…pe… ") or rest.startswith(" …pe… "):
            rest, join = rest[rest.index("…pe… ") + len("…pe… "):], "… "
        elif rest.startswith(" "):
            rest, join = rest[1:], ", "
        else:
            raise KeyError("opening separator: " + rest[:80])
    return "".join(out)


def check_compose():
    """the token composer reproduces every pi-1 opening it can parse (so composed openings match pi-1 style)."""
    n = 0
    for p, v in PI1_OPEN.items():
        if "jhānaṃ" in p or "bhāveti" in p:
            continue
        try:
            c = compose(p)
        except KeyError:
            continue
        assert c == v, (p[:80], c[:120], v[:120])
        n += 1
    assert n >= 20, n
    return n


EARTH = "với đề mục bao trùm là đất"
VAR_PATHAVI = " [khác chính tả (Sī., Syā.): paṭhavīkasiṇaṃ]"
SUNNA = ", có tính chất trống rỗng"


def opening(p):
    if p in PI1_OPEN:
        return PI1_OPEN[p]
    if p.endswith("pathavīkasiṇaṃ [paṭhavīkasiṇaṃ (sī. syā.)]"):
        return repl(PI1_OPEN[p.replace(" [paṭhavīkasiṇaṃ (sī. syā.)]", "")], EARTH, EARTH + VAR_PATHAVI)
    if p.replace("kāmehi …pe…", "kāmehi…pe…") in PI1_OPEN:   # stray space (punctuation only)
        SLIPS.append("space before …pe…: " + p[:60])
        return PI1_OPEN[p.replace("kāmehi …pe…", "kāmehi…pe…")]
    return compose(p)


def tasseva(p):
    if p in PI1_TASSEVA:
        return PI1_TASSEVA[p]
    if p + " suññataṃ" in PI1_TASSEVA:   # lokuttara result without "suññataṃ" (^2-323)
        return repl(PI1_TASSEVA[p + " suññataṃ"], SUNNA, "")
    raise KeyError("Tasseva: " + p[:80])


PHASSA_PE = "phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā"
PHASSA_PE_VI = f"có sự tiếp xúc… có sự không tán loạn {DASH} những hiện tượng này là thiện"
in_pi1("thì vào lúc ấy có sự tiếp xúc… có sự không tán loạn… những hiện tượng này là thiện")


def tasmim(rest):
    return PHASSA_PE_VI if rest == PHASSA_PE else chain(rest)


# ================================================================ 5. sentences and lines
FIXES = [   # (Pāli as written, as meant): punctuation / spelling slips only (reported)
    ('ayaṃ vuccati paridevo".', 'ayaṃ vuccati "paridevo".'),                                  # ^2-238 opening quote
    ("saṅkhārahetukaṃ viññāṇapaccayā", "saṅkhārahetukaṃ, viññāṇapaccayā"),                     # ^2-262 comma
    ('"taṇhāpaccayā upādānaṃ taṇhāsampayuttaṃ" …pe…', '"taṇhāpaccayā upādānaṃ taṇhāsampayuttaṃ"…pe…'),   # ^2-265 space
    ("mānasaṃ …pe…", "mānasaṃ…pe…"),                                                           # ^2-269 space
    ("akusamūlaṃ", "akusalamūlaṃ"),                                                            # ^2-277 spelling
    ('ayaṃ vuccati "avijjāpaccayā saṅkhāro.', 'ayaṃ vuccati "avijjāpaccayā saṅkhāro".'),         # ^2-277 closing quote
    ("abhinibbati pātubhāvo", "abhinibbatti pātubhāvo"),                                       # ^2-273 spelling
    ('Tena vuccati evametassa', 'Tena vuccati "evametassa'),                                   # ^2-354 opening quote
]
HEAD = {   # [new; catukka «bộ bốn» as ch1 «bộ ba / bộ đôi»; niddesa pi-1 «Giải thích …»; mūlaka ch1 «dựa trên»]
    "Paccayacatukkaṃ": "Bộ bốn về điều kiện", "Hetucatukkaṃ": "Bộ bốn về nguyên nhân",
    "Sampayuttacatukkaṃ": "Bộ bốn về sự gắn liền", "Aññamaññacatukkaṃ": "Bộ bốn về sự tương hỗ",
    "Mātikā": "Ma trận",                                                                       # [pi-1]
    "Akusalaniddeso": "Giải thích phần bất thiện", "Kusalaniddeso": "Giải thích phần thiện",
    "Abyākataniddeso": "Giải thích phần không xác định về mặt đạo đức",
    "Avijjāmūlakakusalaniddeso": "Giải thích phần thiện dựa trên vô minh",
    "Kusalamūlakavipākaniddeso": "Giải thích phần quả dựa trên các gốc rễ thiện",
    "Akusalamūlakavipākaniddeso": "Giải thích phần quả dựa trên các gốc rễ bất thiện",
}
in_pi1("##### Giải thích phân loại theo nhóm ba", "Cách thực hành dựa trên sự trống rỗng")
SEC = S.SECTION_TITLES
SPLIT = re.compile(r'(?<=[.?])\s+(?=[A-ZĀĪŪṬḌÑṆṄ])')
Q = re.compile(r"^Tattha katam(?:o|ā|aṃ|e) (.+)\?$")
ANS = re.compile(r'^(.*?) – (?:ayaṃ|idaṃ|ime) (?:vuccati|vuccanti)( –)? ("?)([^"…]+?)("?)((?:…pe….*)?\.)$')
PE_TAIL = re.compile(r'^…pe… (?:tena vuccati "(.+)"ti|(?:ayaṃ|idaṃ) vuccati( –)? "(.+)")\.$')
LEMMA = re.compile(r"^(\S+paccayā(?:pi)? .+?)(nti|ti)\.$")
TAIL_EVAM = {"evametassa kevalassa dukkhakkhandhassa samudayo hotī": EVAM_LOW,
             "evametassa kevalassa dukkhakkhandhassa samudayo hoti": EVAM_LOW,       # ^2-257 short i
             "evametesaṃ dhammānaṃ samudayo hotī": EVAM_D_LOW}


def pe_tail(r):
    """the text after the answer name: '.', '…pe….', '…pe… tena vuccati "…"ti.', '…pe… ayaṃ vuccati "X".'"""
    if r == ".":
        return "."
    if r == "…pe….":
        return "…"   # «….» never (notes-1)
    m = PE_TAIL.match(r)
    if not m:
        raise KeyError("tail: " + r)
    if m.group(1):
        return f"… {TENA} “{TAIL_EVAM[m.group(1)]}”."
    return f"… {called(m.group(3), dash=bool(m.group(2)))}."


def answer(s):
    m = ANS.match(s)
    if not m:
        raise KeyError("answer: " + s[:100])
    body, d, q1, t, q2, rest = m.groups()
    assert q1 == q2, s
    if not body:
        raise KeyError("answer without body: " + s[:80])
    return f"{BODY[body]} {DASH} {called(t, bool(q1), bool(d))}{pe_tail(rest)}"


def sentence(s):
    if s in SENT:
        return SENT[s]
    m = Q.match(s)
    if m:
        return question(m.group(1))
    m = re.match(r"^(?:Idaṃ|Ayaṃ) vuccati \"(.+)\"\.$|^Ime vuccanti \"(.+)\"\.$", s)
    if m:
        return cap(called(m.group(1) or m.group(2))) + "."
    m = re.match(r"^Yasmiṃ samaye (.+?), tasmiṃ samaye (.+)\.$", s)
    if m:
        return f"Vào lúc {opening(m.group(1))}, thì vào lúc ấy {tasmim(m.group(2))}."
    m = re.match(r"^Tasseva (.+?), tasmiṃ samaye (.+)\.$", s)
    if m:
        return f"{tasseva(m.group(1))}, thì vào lúc ấy {tasmim(m.group(2))}."
    m = re.match(r"^Tasmiṃ samaye (.+)\.$", s)
    if m:
        return f"Vào lúc ấy, {chain(m.group(1))}."
    if re.match(r"^(Avijjāpaccayā|Saṅkhārapaccayā avijjā)", s):
        return cap(chain(s[:-1])) + "."
    m = LEMMA.match(s)
    if m:
        lk = low(m.group(1) + ("ṃ" if m.group(2) == "nti" else ""))
        return f"“{cap(link(lk, 'chain'))}”."
    if f" {DASH} " in s:
        return answer(s)
    raise KeyError("sentence: " + s[:100])


def special(t):
    """Lines that do not split into the usual sentences."""
    if t == 'Tattha katamā avijjā…pe… tena vuccati "evametassa kevalassa dukkhakkhandhassa samudayo hotī"ti.':
        return f"{TATTHA} {N['avijjā']} là gì… {TENA} “{EVAM_LOW}”."   # ^2-285 (no "?" in the Pāli)
    m = re.match(r'^Tattha katamaṃ (.+)…pe… ayaṃ vuccati "(.+)"\.$', t)
    if m and "?" not in t:   # ^2-293: "Tattha katamaṃ saṅkhārapaccayā viññāṇaṃ…pe… viññāṇapaccayā nāmaṃ…pe… …"
        links = m.group(1).split("…pe… ")
        names = [link(x, "nom") for x in links]
        return f"{TATTHA} {names[0]} là gì… " + "… ".join(names[1:]) + f"… {called(m.group(2))}."
    return None


def line(t):
    for a, b in FIXES:
        if a in t:
            SLIPS.append(f"{a!r} -> {b!r}")
            t = t.replace(a, b)
    r = special(t)
    if r:
        return r
    return " ".join(sentence(s) for s in SPLIT.split(t))


def translate(pali_lines):
    out = []
    for pl in pali_lines:
        if not pl.strip():
            out.append("")
            continue
        m = S.ID.search(pl)
        t = S.ID.sub("", pl).rstrip()
        if t == "### Paṭiccasamuppādavibhaṅgo":
            vi = "### " + S.CHAPTER_TITLES[6]
        elif t.startswith("#### "):
            SUTTA["on"] = t[5:] == "Suttantabhājanīyaṃ"
            vi = "#### " + SEC[t[5:]]
        elif t.startswith("##### "):
            vi = "##### " + HEAD[t[6:]]
        elif t.endswith(".") and t[:-1] in HEAD:
            vi = HEAD[t[:-1]] + "."
        elif t.endswith(".") and t[:-1] in SEC:
            vi = SEC[t[:-1]] + "."
        elif t == "Paṭiccasamuppādavibhaṅgo [paccayākāravibhaṅgo (sī. syā.)] niṭṭhito.":
            vi = S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[6] + " [dị bản (Sī., Syā.): paccayākāravibhaṅgo]")
        else:
            vi = line(t)
        assert pl.count(DASH) + pl.count("—") == vi.count(DASH) and "—" not in vi, ("dash count", t[:70], vi[:90])
        for bad in ("là là", "  ", "….", '"', " ,", " .", ":-", "thì thì", "\x01", "  "):
            assert bad not in vi, (bad, vi[:120])
        out.append(vi + (" " + m.group(1) if m else ""))
    return out


def check_chain():
    """the Suttanta chain equals pi-1 ^1-1343 word for word (its ';' is a '.' in pi-2)."""
    SUTTA["on"] = True
    p = ("Avijjāpaccayā saṅkhārā, saṅkhārapaccayā viññāṇaṃ, viññāṇapaccayā nāmarūpaṃ, nāmarūpapaccayā saḷāyatanaṃ, "
         "saḷāyatanapaccayā phasso, phassapaccayā vedanā, vedanāpaccayā taṇhā, taṇhāpaccayā upādānaṃ, upādānapaccayā "
         "bhavo, bhavapaccayā jāti, " + GRIEF_LINK)
    assert "“" + cap(chain(p)) + "; " + EVAM_LOW + "”" in pi1("1-1343"), cap(chain(p))
    SUTTA["on"] = False


def build():
    check_chain()
    check_ch4_bodies()
    n = check_compose()
    pali = open(os.path.join(S.PALI_DIR, FN), encoding="utf-8").read().rstrip("\n").split("\n")
    return translate(pali), n


def main():
    lines, n = build()
    path = os.path.join(S.VI_DIR, FN)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines).rstrip("\n") + "\n")
    print("OK:", path, "|", len([l for l in lines if l.strip()]), "non-empty lines |", n, "pi-1 openings recomposed")
    for s in sorted(set(SLIPS)):
        print("slip:", s)


if __name__ == "__main__":
    main()
