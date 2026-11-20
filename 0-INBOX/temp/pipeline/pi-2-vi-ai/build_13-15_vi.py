# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Vietnamese plain zero-shot: chapters 13 (Appamaññā), 14 (Sikkhāpada), 15 (Paṭisambhidā).

usage: python -I -X utf8 build_13-15_vi.py [--dry]
Writes AI_translation\\vietnamese\\pi-2-vietnamese-plain-zeroshot_split_chapters\\13-appamannavibhango.md,
14-sikkhapadavibhango.md and 15-patisambhidavibhango.md (only when run as a script without --dry; importing
writes nothing).

Imports build_10-12_vi (X) and through it S, B, T, F, G, H; their tables (X.NAME, X.BODY, X.AVA, X.SUFFIX,
X.START_VI, X.RESULT, X.SENT, X.FIXES, G.TOKENS) are extended in memory only, nothing of theirs is rewritten.
pi-1 strings (the mettā / karuṇā / muditā / upekkhā jhāna openings, the mind-type openings, the vipāka / kiriya
lists "phasso hoti, vedanā hoti, …", the abstention words of ^1-299 … ^1-301, cetanā ^1-5, the citta synonyms
^1-6) are copied from the pi-1 Vietnamese rails or from the earlier builders and asserted; the extended composers
are re-checked against every pi-1 opening they can parse. Unknown Pāli raises KeyError (nothing is guessed).
"""
import importlib
import os
import re
import sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai"
sys.path.insert(0, HERE)
X = importlib.import_module("build_10-12_vi")
S, B, T, F, G, H = X.S, X.B, X.T, X.F, X.G, X.H

DASH = S.DASH
cap, low = S.cap, S.low
in_pi1, pi1, between, repl = G.in_pi1, T.pi1, T.between, T.repl
called, q = T.called, X.q
TATTHA, IDHA, BHIKKHU, WHAT, TENA = X.TATTHA, X.IDHA, X.BHIKKHU, X.WHAT, X.TENA
SLIPS = []
PI1_P = os.path.join(S.ROOT, r"AI_translation\pali\pi-1_split_chapters")
PI1_V = os.path.join(S.ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")


def vi_out(fn):
    """an earlier pi-2 Vietnamese chapter (read only, for asserting reused strings)"""
    return open(os.path.join(S.VI_DIR, fn), encoding="utf-8").read()


def in_out(fn, *parts):
    txt = vi_out(fn)
    for p in parts:
        assert p in txt, (fn, p[:80])


# ================================================================ 1. shared names
APP = {"mettā": "lòng từ ái", "karuṇā": "lòng trắc ẩn", "muditā": "niềm vui đồng cảm", "upekkhā": "sự bình thản"}
for _k, _v in APP.items():
    in_pi1(f"có {_v} đi kèm")                                               # [pi-1 ^1-251 … ^1-262]
APP_KEYS = list(APP)
APP3 = {"mettā": T.METTA3, "karuṇā": T.KARUNA3,                             # [pi-1 ^1-1062 / ch3]
        "muditā": "niềm vui đồng cảm, sự khởi niềm vui đồng cảm, trạng thái khởi niềm vui đồng cảm",   # [new, ch3 pattern]
        "upekkhā": "sự bình thản, sự khởi bình thản, trạng thái khởi bình thản"}                     # [new]
CETO = {k: f"{T.CETOVIMUTTI} {v}" for k, v in APP.items()}                 # Xcetovimutti [ch3]
DEF_A = {k: f"{APP3[k]}, {CETO[k]}" for k in APP}                           # (yā tasmiṃ samaye) X Xāyanā … Xcetovimutti
DEF_S = {k: f"{APP[k]} đối với chúng sinh{APP3[k][len(APP[k]):]}, {CETO[k]}" for k in APP}   # Yā sattesu X …
in_out("3-dhatuvibhango.md", WHAT + DEF_S["mettā"] + " " + DASH, WHAT + DEF_S["karuṇā"] + " " + DASH)
FOUR_APP = "bốn trạng thái không thể đo lường"                              # catasso appamaññāyo [heading words]
APP_UNIT = "trạng thái không thể đo lường"
in_pi1("không thể đo lường")

VIR = {"pāṇātipātā": "việc sát hại sinh mạng", "adinnādānā": "việc lấy của không được cho",
       "kāmesumicchācārā": "hành vi sai trái trong các dục lạc", "musāvādā": "việc nói dối",
       "surāmerayamajjapamādaṭṭhānā": "việc dùng rượu nấu, rượu men và chất gây say dẫn đến sự buông thả"}
for _k in ("pāṇātipātā", "adinnādānā", "kāmesumicchācārā"):
    assert "ự kiềm chế " + VIR[_k] in F.ACTION3                             # [ch4]
assert "ự kiềm chế " + VIR["musāvādā"] in F.SPEECH4                         # [ch4]
VIR_ORDER = list(VIR)
SIKKHAPADA = "điều tu học"                                                  # sikkhāpada [terms file ch. 14; ch12]
in_out("12-jhanavibhango.md", "các điều tu học")


def sk(obj):
    """X veramaṇī sikkhāpadaṃ"""
    return f"{SIKKHAPADA} về sự kiềm chế {VIR[obj]}"


VIRATI_REST = between(F._SK, "sự tránh xa ba hành vi xấu bằng thân, ", ", hành động đúng đắn")   # [pi-1 ^1-300]
assert VIRATI_REST.startswith("sự kiêng tránh, sự kiêng tránh hoàn toàn, sự kiềm chế") and \
    VIRATI_REST.endswith("sự phá bỏ cây cầu"), VIRATI_REST
CETANA3 = G.BODY["Yā cetanā sañcetanā sañcetayitattaṃ"][len(WHAT):]        # chủ ý, sự cố ý, trạng thái đã cố ý [pi-1 ^1-5]
PHASSA_PE = H.PHASSA_PE                                                     # sự tiếp xúc… sự dốc sức, sự không tán loạn

PS = {"attha": "hiểu biết thông suốt về ý nghĩa", "dhamma": "hiểu biết thông suốt về các hiện tượng",
      "nirutti": "hiểu biết thông suốt về cách diễn đạt",
      "paṭibhāna": "hiểu biết thông suốt về tài ứng đáp"}                   # [new; nirutti pi-1 «cách diễn đạt»]
in_pi1("cách diễn đạt", "lời diễn tả", "khái niệm")
PS_ORDER = list(PS)
PS_UNIT = "loại hiểu biết thông suốt"                                       # heading «các loại hiểu biết thông suốt»


# ================================================================ 2. extensions of the ch. 10-12 tables (memory only)
def _pali_def(k):
    """metti mettāyanā mettāyitattaṃ mettācetovimutti (karuṇā …, muditā …, upekkhā …)"""
    r = k[:-1]
    return f"{'metti' if k == 'mettā' else k} {r}āyanā {r}āyitattaṃ {r}ācetovimutti"


for _k in APP:
    X.NAME[_k] = (APP[_k], False)
    X.BODY[_pali_def(_k)] = DEF_A[_k]
    X.AVA[_k[:-1] + "āya"] = APP[_k]
X.AVA["veramaṇiyā"] = "sự kiềm chế"                                         # [pi-1 veramaṇī]
X.AVA["cetanāya"] = "chủ ý"                                                 # [pi-1]
for _k in APP:
    X.SUFFIX[f" {_k}sahagataṃ"] = f", có {APP[_k]} đi kèm"                   # [pi-1 ^1-251 …]
X.START_VI["sukhassa ca pahānā dukkhassa ca pahānā"] = X.LJ["sukhassa"]     # [pi-1 jhāna formula]
X.JBODY = re.compile(r"^(" + "|".join(map(re.escape, sorted(X.START_VI, key=len, reverse=True))) + r")…pe… "
                     r"((?:\w+ jhānaṃ…pe… )*)(\w+) jhānaṃ upasampajja viharati$")
X.RESULT["lokuttarassa kusalassa kammassa katattā bhāvitattā vipākaṃ "] = \
    "là quả của chính nghiệp thiện vượt thế gian ấy đã được tạo và tu tập"  # ^2-740 kammassa (pi-1 jhānassa), as written
X.SENT["Tattha katamā karuṇā…pe… tattha katamā muditā…pe… tattha katamā upekkhā?"] = \
    f"{TATTHA} {APP['karuṇā']} là gì… {low(TATTHA)} {APP['muditā']} là gì… {low(TATTHA)} {APP['upekkhā']} là gì?"
X.FIXES.append(("muditāyatanā", "muditāyanā"))                              # ^2-688 spelling, as meant
N_OPEN = X.check_openings()                                                 # composer still reproduces pi-1 (now with mettā …)

# mind-type tokens for the ch. 14 openings (pi-1 ^1-269 words), added to the ch. 6 composer
ADHI = {"chand": "ý muốn", "vīriy": "tinh tấn", "citt": "tâm", "vīmaṃs": "sự thẩm xét"}   # X-ādhipateyyaṃ
in_pi1(*(f"lấy {v} làm yếu tố chủ đạo" for v in ADHI.values()))
in_pi1("thấp kém… trung bình… ưu việt")
G.TOKENS.extend([
    (re.compile(r"hīnaṃ"), lambda m: "thấp kém"), (re.compile(r"majjhimaṃ"), lambda m: "trung bình"),
    (re.compile(r"paṇītaṃ"), lambda m: "ưu việt"),
    (re.compile(r"(chand|vīriy|citt|vīmaṃs)ādhipateyyaṃ"),
     lambda m: f"lấy {ADHI[m.group(1)]} làm yếu tố chủ đạo"),
])
N_COMPOSE = G.check_compose()


def compose(p):
    """mind-type opening (pi-2 "… " separators read as "…pe…", same Vietnamese «… »)."""
    p2 = re.sub(r" …(?!pe…)", "…", p)                                      # stray space before "…" (punctuation)
    if p2 != p:
        SLIPS.append("space before …: " + p[max(0, p.index(" …") - 20):][:45])
    p2 = re.sub(r"(?<!pe)…(?!pe…) ", "…pe… ", p2)
    return G.opening(p2)


def opening_any(p):
    """text after "Yasmiṃ samaye" -> Vietnamese after «Vào lúc » (pi-1 when identical)."""
    try:
        return X.jopen(p)
    except KeyError:
        return compose(p)


# ================================================================ 3. pi-1 "phasso hoti, vedanā hoti, …" lists
def _pi1_lists():
    out = {}
    for fn in sorted(os.listdir(PI1_P)):
        if not fn.endswith(".md"):
            continue
        pl = [x for x in open(os.path.join(PI1_P, fn), encoding="utf-8").read().split("\n") if x.strip()]
        vl = [x for x in open(os.path.join(PI1_V, fn), encoding="utf-8").read().split("\n") if x.strip()]
        assert len(pl) == len(vl), fn
        for p, v in zip(pl, vl):
            if "tasmiṃ samaye phasso hoti, vedanā hoti," in p and "; ye vā pana" in p:
                pk = between(p, "tasmiṃ samaye phasso hoti, ", "; ye vā pana").replace(",", "")
                vk = between(v, "thì vào lúc ấy có sự tiếp xúc, ", "; hoặc vào lúc ấy")
                assert out.get(pk, vk) == vk, pk
                out[pk] = vk
    return out


PI1_LISTS = _pi1_lists()
ARUPINO = "hoặc vào lúc ấy còn có bất cứ hiện tượng phi vật chất nào khác sinh khởi tùy thuộc vào điều kiện"
in_pi1(ARUPINO)
YE_VA = ", ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"


def tail(r):
    """text after "tasmiṃ samaye" -> «thì vào lúc ấy có …»"""
    if r == "phasso hoti…pe… avikkhepo hoti":
        return f"thì vào lúc ấy có {X.CONTACT}"
    assert r.startswith("phasso hoti, ") and r.endswith(YE_VA), r[-60:]
    key = r[len("phasso hoti, "):-len(YE_VA)].replace(",", "")
    return f"thì vào lúc ấy có sự tiếp xúc, {PI1_LISTS[key]}, {ARUPINO}"


# ================================================================ 4. chapter 13
ONE = {k: f"an trú sau khi lan tỏa khắp một phương với tâm có {APP[k]} đi kèm" for k in APP}   # ekaṃ disaṃ pharitvā viharati
TATHA = "cũng vậy phương thứ hai, cũng vậy phương thứ ba, cũng vậy phương thứ tư"   # tathā dutiyaṃ, … catutthaṃ [new]
VAR_CATUTTHI = " [khác chính tả (Sī.): catutthiṃ]"
SABBA2 = "khắp mọi nơi, đối với tất cả như đối với chính mình"            # sabbadhi sabbattatāya [new]
SABBADHI = "phía trên, phía dưới, chiều ngang, " + SABBA2                  # uddhamadho tiriyaṃ sabbadhi sabbattatāya
LOKA = "toàn thể thế gian"                                                  # sabbāvantaṃ lokaṃ [new]
VIPULA5 = "rộng rãi, rộng lớn, không thể đo lường, không thù địch, không thù hằn"   # vipulena … abyāpajjena [pi-1 words]
in_pi1("Các hiện tượng rộng lớn", "sự không thù hằn")
VAR_ABY = {"abyāpajjena": " [khác chính tả (Sī., Syā.): abyāpajjhena]", "abyāpajjo": " [khác chính tả (Sī., Syā.): abyāpajjho]"}


def whole(k, var=""):
    """Iti uddhamadho … lokaṃ Xsahagatena cetasā vipulena … abyāpajjena pharitvā viharati"""
    return (f"như vậy, {SABBADHI}, vị ấy an trú sau khi lan tỏa khắp {LOKA} với tâm có {APP[k]} đi kèm, "
            f"{VIPULA5}{var}")


P642 = (f"{cap(FOUR_APP)} {DASH} {low(IDHA)}, {BHIKKHU} {ONE['mettā']}, {TATHA}{VAR_CATUTTHI}. "
        f"{cap(whole('mettā', VAR_ABY['abyāpajjena']))}. "
        + " ".join(f"Vị ấy {ONE[k]}, {TATHA}. {cap(whole(k))}." for k in APP_KEYS[1:]))
P699 = (f"{cap(FOUR_APP)} {DASH} {low(IDHA)}, {BHIKKHU} {ONE['mettā']}, {TATHA}, {whole('mettā')}; "
        + "; ".join(f"vị ấy {ONE[k]}, {TATHA}, {whole(k)}" for k in APP_KEYS[1:]) + ".")
LABEL_699 = ("Catasso appamaññāyo – idha bhikkhu " + "; ".join(
    f"{k}sahagatena cetasā ekaṃ disaṃ pharitvā viharati tathā dutiyaṃ tathā tatiyaṃ tathā catutthaṃ, iti uddhamadho "
    f"tiriyaṃ sabbadhi sabbattatāya sabbāvantaṃ lokaṃ {k}sahagatena cetasā vipulena mahaggatena appamāṇena averena "
    f"abyāpajjena pharitvā viharati" for k in APP_KEYS) + ".")
SIMILE = {   # Seyyathāpi nāma ekaṃ puggalaṃ … disvā …, evameva sabbe satte Xāya pharati [new]
    "mettā": "một người đáng yêu quý, đáng ưa thích, người ta sẽ khởi lòng từ ái",
    "karuṇā": "một người khốn khổ, bất hạnh, người ta sẽ khởi lòng trắc ẩn",
    "muditā": "một người đáng yêu quý, đáng ưa thích, người ta sẽ vui mừng",
    "upekkhā": "một người không đáng ưa thích cũng không phải không đáng ưa thích, người ta sẽ bình thản",
}
CITTA_FULL = G.BODY["Yaṃ cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
                    "tajjāmanoviññāṇadhātu"]                                 # [pi-1 ^1-6]
CITTA_PE = WHAT + X.CITTA_PE


def with_mind(k):
    return f"với tâm có {APP[k]} đi kèm"


def citta_line(k, full):
    return (f"{q('tâm')} {CITTA_FULL if full else CITTA_PE} {DASH} {called('tâm')}. Tâm này có {APP[k]} này đi kèm, "
            f"cùng sinh với nó, hòa lẫn với nó, gắn liền với nó. {TENA} “{with_mind(k)}”.")


def def_line(k, lemma=False):
    body = f"{q(APP[k])} {WHAT}{DEF_S[k]} {DASH} {called(APP[k])}."
    return f"{X.lem(with_mind(k))}: {low(body)}" if lemma else body


SABBENA = "một cách toàn bộ, về mọi mặt, trọn vẹn, không thiếu sót, không sót lại gì"   # sabbena sabbaṃ … nissesaṃ [ch12]
in_out("12-jhanavibhango.md", SABBENA)
SAB_LEMMA = f"{SABBA2}, {LOKA}"                                            # "Sabbadhi sabbattatāya sabbāvantaṃ loka"nti
DISA = ("hoặc phương đông, hoặc phương tây, hoặc phương bắc, hoặc phương nam, hoặc phía trên, hoặc phía dưới, "
        "hoặc chiều ngang, hoặc phương trung gian")                          # [new]
PHARITVA = "sau khi lan tỏa khắp"
VIPULA_DEF = ("điều gì rộng rãi thì điều ấy rộng lớn, điều gì rộng lớn thì điều ấy không thể đo lường, điều gì không thể "
              "đo lường thì điều ấy không thù địch, điều gì không thù địch thì điều ấy không thù hằn")   # [ch12 PADOSA frame]


def sutta13(t):
    k = None
    m = re.search(r"(mettā|karuṇā|muditā|upekkhā)(?:sahagatena|ya sahagataṃ)", t)
    if m:
        k = m.group(1)
    if t.startswith("Catasso appamaññāyo – idha bhikkhu mettāsahagatena cetasā ekaṃ disaṃ pharitvā viharati, tathā"):
        return P642
    if t.startswith("Kathañca bhikkhu "):
        sim = {"mettā": "piyaṃ manāpaṃ disvā mettāyeyya", "karuṇā": "duggataṃ durūpetaṃ disvā karuṇāyeyya",
               "muditā": "piyaṃ manāpaṃ disvā mudito assa",
               "upekkhā": "neva manāpaṃ na amanāpaṃ disvā upekkhako assa"}[k]
        assert t == (f"Kathañca bhikkhu {k}sahagatena cetasā ekaṃ disaṃ pharitvā viharati? Seyyathāpi nāma ekaṃ "
                     f"puggalaṃ {sim}, evameva sabbe satte {k[:-1]}āya pharati."), t
        return (f"Và {BHIKKHU} {ONE[k]} như thế nào? Giống như khi thấy {SIMILE[k]}, cũng vậy, vị ấy lan tỏa khắp "
                f"tất cả chúng sinh bằng {APP[k]}.")
    if re.match(r"^Tattha katamā (mettā|karuṇā|muditā|upekkhā)\? Yā sattesu ", t):
        k = t.split()[2][:-1]
        assert t == f"Tattha katamā {k}? Yā sattesu {_pali_def(k)} – ayaṃ vuccati \"{k}\".", t
        return def_line(k)
    if t.startswith("Tattha katamaṃ cittaṃ? Yaṃ cittaṃ mano mānasaṃ"):
        full = "hadayaṃ paṇḍaraṃ" in t
        return citta_line(k, full)
    if t.startswith('"Ekaṃ disa"nti '):
        assert t == ('"Ekaṃ disa"nti puratthimaṃ vā disaṃ pacchimaṃ vā disaṃ uttaraṃ vā disaṃ dakkhiṇaṃ vā disaṃ '
                     'uddhaṃ vā adho vā tiriyaṃ vā vidisaṃ vā.'), t
        return f"{X.lem('một phương')}: {DISA}."
    if t == '"Pharitvā"ti pharitvā adhimuccitvā.':
        return f"{X.lem(PHARITVA)}: {PHARITVA}, sau khi quyết định."
    if t == '"Viharatī"ti iriyati vattati pāleti yapeti yāpeti carati viharati. Tena vuccati "viharatī"ti.':
        return X.viharati_full(True)
    if t in ('"Viharatī"ti…pe… tena vuccati "viharatī"ti.', '"Viharatī"ti …pe… tena vuccati "viharatī"ti.'):
        if " …pe…" in t:
            SLIPS.append("^2-672 space before …pe… (punctuation)")
        return X.viharati_pe(True)
    if t.startswith('"Tathā dutiya"nti '):
        assert t == ('"Tathā dutiya"nti yatheva ekaṃ disaṃ tathā dutiyaṃ disaṃ tathā tatiyaṃ disaṃ tathā catutthaṃ '
                     'disaṃ tathā uddhaṃ tathā adho tathā tiriyaṃ tathā vidisaṃ.'), t
        return (f"{X.lem('cũng vậy phương thứ hai')}: giống như một phương, {TATHA}, cũng vậy phía trên, cũng vậy "
                "phía dưới, cũng vậy chiều ngang, cũng vậy phương trung gian.")
    if t.startswith('"Sabbadhi '):
        assert t == ('"Sabbadhi sabbattatāya sabbāvantaṃ loka"nti sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ. '
                     'Pariyādāyavacanametaṃ – "sabbadhi sabbattatāya sabbāvantaṃ loka"nti.'), t
        return (f"{X.lem(SAB_LEMMA)}: {SABBENA}. Đây là cách nói bao hàm tất cả {DASH} “{SAB_LEMMA}”.")
    m2 = re.match(r'^"(\w+)sahagatena cetasā"ti,? tattha katamā (\w+)\? Yā sattesu (.+) – ayaṃ vuccati "(\w+)"\.$', t)
    if m2:
        k = m2.group(2)
        assert m2.group(1).lower() == k and m2.group(3) == _pali_def(k) and m2.group(4) == k, t
        return def_line(k, lemma=True)
    if t.startswith('"Vipulenā"ti '):
        var = VAR_ABY["abyāpajjo"] if "[abyāpajjho (sī. syā.)]" in t else ""
        assert t.replace(" [abyāpajjho (sī. syā.)]", "") == (
            '"Vipulenā"ti yaṃ vipulaṃ taṃ mahaggataṃ, yaṃ mahaggataṃ taṃ appamāṇaṃ, yaṃ appamāṇaṃ so avero, '
            'yo avero so abyāpajjo.'), t
        return f"{X.lem('rộng rãi')}: {VIPULA_DEF}{var}."
    if t == "Suttantabhājanīyaṃ.":
        return X.LABELS[t]
    raise KeyError("sutta13: " + t[:90])


# ================================================================ 5. chapter 14
SK_Q = re.compile(r"^Tattha katamaṃ (\w+) veramaṇī sikkhāpadaṃ((?:…pe… \w+ veramaṇī sikkhāpadaṃ)*)\?$")
SK_OPEN = re.compile(r'^Yasmiṃ samaye (.+?) (\w+) viramantassa(, yā tasmiṃ samaye |, yo tasmiṃ samaye | )(.+) – idaṃ '
                     r'vuccati "(\w+) veramaṇī sikkhāpadaṃ"\.$')
SK_TAIL = re.compile(r'^Avasesā dhammā veramaṇiyā sampayuttā…pe… avasesā dhammā cetanāya sampayuttā…pe… phasso…pe… '
                     r'paggāho avikkhepo – idaṃ vuccati "(\w+) veramaṇī sikkhāpadaṃ"\.$')
SK_FIX = [("sikkhāpadaṃ, yasmiṃ samaye", "sikkhāpadaṃ? Yasmiṃ samaye"),     # ^2-706 question mark
          ("Yasmiṃ samaye kāmāvacare kusalaṃ", "Yasmiṃ samaye kāmāvacaraṃ kusalaṃ"),   # ^2-711 spelling
          ("sampayuttā …pe…", "sampayuttā…pe…")]                            # ^2-710 space


def sk_body(obj, b):
    if b == f"{obj} ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto":
        return f"thì điều mà vào lúc ấy là sự tránh xa {VIR[obj]}, {VIRATI_REST}"
    if b == "cetanā sañcetanā sañcetayitattaṃ":
        return f"thì điều mà vào lúc ấy là {CETANA3}"
    if b == "phasso…pe… paggāho avikkhepo":
        return f"thì những gì có vào lúc ấy, {PHASSA_PE}"
    raise KeyError("sikkhāpada body: " + b[:60])


def s14(s):
    m = SK_Q.match(s)
    if m:
        objs = [m.group(1)] + re.findall(r"…pe… (\w+) veramaṇī sikkhāpadaṃ", m.group(2))
        names = [sk(o) for o in objs]
        if len(names) == 1:
            return q(names[0]) if "," not in names[0] else f"{TATTHA} {names[0]}, là gì?"
        return f"{TATTHA} " + "… ".join(names) + ", là gì?"
    m = SK_OPEN.match(s)
    if m:
        op, obj, kind, body, nobj = m.groups()
        assert nobj == obj, s
        head = f"Vào lúc {opening_any(op)}, ở người đang kiêng tránh {VIR[obj]}, "
        if kind == " ":                                                      # ^2-705 no "yo tasmiṃ samaye" (as written)
            assert body == "phasso…pe… paggāho avikkhepo", body
            SLIPS.append("^2-705 'viramantassa phasso…pe…' without 'yo tasmiṃ samaye' (as written)")
            mid = PHASSA_PE
        else:
            mid = sk_body(obj, body)
        return f"{head}{mid} {DASH} {called(sk(obj))}."
    if s in ("Avasesā dhammā veramaṇiyā sampayuttā.", "Avasesā dhammā cetanāya sampayuttā."):
        return X.avasesa(s[:-1]) + "."
    m = SK_TAIL.match(s)
    if m:
        return (f"{X.avasesa('Avasesā dhammā veramaṇiyā sampayuttā…pe… avasesā dhammā cetanāya sampayuttā')}… "
                f"{PHASSA_PE} {DASH} {called(sk(m.group(1)))}.")
    if s == "Katame dhammā sikkhā?":
        return "Những hiện tượng nào là sự tu học?"                         # [new; pi-1 frame, sikkhā pi-1]
    if s == "Ime dhammā sikkhā.":
        return "Những hiện tượng này là sự tu học."
    m = re.match(r"^Yasmiṃ samaye (.+), tasmiṃ samaye phasso hoti…pe… avikkhepo hoti\.$", s)
    if m:
        return f"Vào lúc {opening14(m.group(1))}, {tail('phasso hoti…pe… avikkhepo hoti')}."
    raise KeyError("s14: " + s[:90])


RUPA_UP = X.PREFIX["rūpūpapattiyā maggaṃ bhāveti "][len(X.MOT):-2]          # tu tập con đường … cõi hình sắc
ARUPA_UP = repl(RUPA_UP, "cõi hình sắc", "cõi không hình sắc")
in_pi1("một người " + ARUPA_UP)
LOK_OPEN = X.jopen(H.LOKP)


def opening14(p):
    pre = "rūpūpapattiyā maggaṃ bhāveti…pe… arūpūpapattiyā maggaṃ bhāveti…pe… "
    if p.startswith(pre):
        lok = X.jopen(p[len(pre):])
        assert lok.startswith(X.MOT + "tu tập tầng thiền vượt thế gian"), lok
        return f"{X.MOT}{RUPA_UP}… {ARUPA_UP}… {lok[len(X.MOT):]}"
    return opening_any(p)


def abhi14(t):
    for a, b in SK_FIX:
        if a in t:
            SLIPS.append(f"ch14 {a!r} -> {b!r}")
            t = t.replace(a, b)
    return " ".join(s14(s) for s in X.SPLIT.split(t))


# ================================================================ 6. chapter 15
KATAME = {"kusalā": "Những hiện tượng nào là thiện?", "akusalā": "Những hiện tượng nào là bất thiện?",
          "abyākatā": "Những hiện tượng nào không xác định về mặt đạo đức?"}   # [pi-1]
IME = {"kusalā": "Những hiện tượng này là thiện.", "akusalā": "Những hiện tượng này là bất thiện.",
       "abyākatā": "Những hiện tượng này không xác định về mặt đạo đức."}
in_pi1(*KATAME.values())
in_pi1(*(low(v[:-1]) for v in IME.values()))
assert X.SENT["Ime dhammā kusalā."] == IME["kusalā"]
VAR_PATI = " [khác chính tả (Syā.): paṭibhāṇapaṭisambhidā; cũng vậy ở các chỗ sau]"


CATASSO = f"Bốn {PS_UNIT} {DASH} {T.listing([PS[k] for k in PS_ORDER])}."
CATASSO_VAR = f"Bốn {PS_UNIT} {DASH} {T.listing([PS[k] for k in PS_ORDER])}{VAR_PATI}."
TISSO = f"Ba {PS_UNIT} {DASH} {T.listing([PS[k] for k in ('attha', 'nirutti', 'paṭibhāna')])}."
KN = "sự hiểu biết về"                                                      # X-e ñāṇaṃ [ch4 «Sự hiểu biết về khổ đau»]
in_out("4-saccavibhango.md", "Sự hiểu biết về khổ đau, sự hiểu biết về sự phát sinh của khổ đau, sự hiểu biết về sự "
       "chấm dứt khổ đau, sự hiểu biết về cách thực hành dẫn đến sự chấm dứt khổ đau")
NIR = f"{KN} lời diễn tả cách diễn đạt các hiện tượng ở đó là {PS['nirutti']}"   # tatra dhammaniruttābhilāpe ñāṇaṃ … [new]
PAT = f"{KN} các sự hiểu biết là {PS['paṭibhāna']}"                         # ñāṇesu ñāṇaṃ … [new]
YAYA = "nhờ cách diễn đạt nào mà có khái niệm về những hiện tượng ấy, thì"  # yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti
YENA = (f"Sự hiểu biết mà nhờ đó người ta biết những sự hiểu biết ấy {DASH} “Những sự hiểu biết này làm sáng tỏ ý "
        f"nghĩa này”, tức {PAT}.")                                          # Yena ñāṇena tāni ñāṇāni jānāti – … [new]


def kn(x, k):
    """X-e ñāṇaṃ Y-paṭisambhidā -> «sự hiểu biết về X là Y»"""
    return f"{KN} {x} là {PS[k]}"


def four_truths(n):
    """X, X-samudaya, X-nirodha, X-nirodhagāminī paṭipadā (attha, dhamma, attha, dhamma) [ch4 words]"""
    return (f"{kn(n, 'attha')}, {kn('sự phát sinh của ' + n, 'dhamma')}, {kn('sự chấm dứt ' + n, 'attha')}, "
            f"{kn('cách thực hành dẫn đến sự chấm dứt ' + n, 'dhamma')}")


JATA6 = "đã sinh, đã trở thành, đã sinh ra, đã phát khởi, đã hình thành, đã xuất hiện"   # jātā bhūtā sañjātā … [ch12 + pi-1]
assert X.JATA == JATA6.replace("đã trở thành, ", "")
in_pi1("đã trở thành")
LINKS = ["sự sinh", "sự hiện hữu", "sự bám víu", "khao khát", "cảm giác", "sự tiếp xúc", "sáu lĩnh vực nhận biết",
         "phần tinh thần và vật chất", "thức"]                              # [pi-1 / ch6 G.N]
for _x, _p in zip(LINKS, ("jāti", "bhavo", "upādānaṃ", "taṇhā", "vedanā", "phasso", "saḷāyatanaṃ", "nāmarūpaṃ",
                          "viññāṇaṃ")):
    assert G.N[_p] == _x, _p
ANGA9 = ("kinh, văn xuôi xen kệ, lời giải thích, kệ, lời cảm hứng, lời đã được nói như vậy, chuyện tiền thân, "
         "chuyện kỳ diệu chưa từng có, lời vấn đáp")                         # suttaṃ … vedallaṃ [new]
HAND15 = [
    ("Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā "
     "[paṭibhāṇapaṭisambhidā (syā.) evamuparipi]. Atthe ñāṇaṃ",
     f"{CATASSO_VAR} {cap(kn('ý nghĩa', 'attha'))}, {kn('các hiện tượng', 'dhamma')}, {NIR}, {PAT}. "
     "Đây là mục tổng hợp."),
    ("Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā. "
     "Dukkhe ñāṇaṃ",
     f"{CATASSO} {cap(four_truths('khổ đau'))}, {NIR}, {PAT}. Đây là mục về các sự thật."),
    ("Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā niruttipaṭisambhidā, paṭibhānapaṭisambhidā. "
     "Hetumhi ñāṇaṃ",
     f"{CATASSO} {cap(kn('nguyên nhân', 'dhamma'))}, {kn('quả của nguyên nhân', 'attha')}, {NIR}, {PAT}. "
     "Đây là mục về nguyên nhân."),
    ("Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā. "
     "Ye dhammā jātā",
     f"{CATASSO} Những hiện tượng nào {JATA6}, thì {kn('những hiện tượng này', 'attha')}; những hiện tượng ấy "
     f"{JATA6} từ những hiện tượng nào, thì {kn('những hiện tượng ấy', 'dhamma')}; {NIR}; {PAT}. "
     "Đây là mục về các hiện tượng."),
    ("Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā. "
     "Jarāmaraṇe ñāṇaṃ",
     f"{CATASSO} {cap(four_truths('sự lão hóa và sự chết'))}, {NIR}, {PAT}."),
    ("Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā. "
     "Jātiyā ñāṇaṃ",
     f"{CATASSO} " + cap("… ".join(f"{KN} {x}" for x in LINKS)) + "… "
     + f"{four_truths('các sự tạo tác')}, {NIR}, {PAT}. "
     "Đây là mục về sự sinh khởi tùy thuộc vào điều kiện."),
    ("Tattha katamā dhammapaṭisambhidā? Idha bhikkhu dhammaṃ jānāti",
     f"{q(PS['dhamma'])} {IDHA}, {BHIKKHU} biết Giáo Pháp {DASH} {ANGA9}. {cap(called(PS['dhamma']))}. Vị ấy biết ý "
     f"nghĩa của từng lời đã được nói ấy {DASH} “Đây là ý nghĩa của lời đã được nói này, đây là ý nghĩa của lời đã "
     f"được nói này”. {cap(called(PS['attha']))}. {cap(NIR)}. {cap(PAT)}. Đây là mục về việc học hỏi Giáo Pháp."),
]
_P724 = ('Tattha katamā dhammapaṭisambhidā? Idha bhikkhu dhammaṃ jānāti – suttaṃ geyyaṃ veyyākaraṇaṃ gāthaṃ udānaṃ '
         'itivuttakaṃ jātakaṃ abbhutadhammaṃ vedallaṃ. Ayaṃ vuccati "dhammapaṭisambhidā". So tassa tasseva bhāsitassa '
         'atthaṃ jānāti – "ayaṃ imassa bhāsitassa attho, ayaṃ imassa bhāsitassa attho"ti. Ayaṃ vuccati '
         '"atthapaṭisambhidā". Tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā. Ñāṇesu ñāṇaṃ '
         'paṭibhānapaṭisambhidā. Ayaṃ pariyattivāro.')
_FIXED15 = {   # the Suttanta lines checked word for word (the parts after the opening list)
    "Atthe ñāṇaṃ": "Atthe ñāṇaṃ atthapaṭisambhidā, dhamme ñāṇaṃ dhammapaṭisambhidā, tatra dhammaniruttābhilāpe ñāṇaṃ "
                   "niruttipaṭisambhidā, ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā. Ayaṃ saṅgahavāro.",
    "Dukkhe ñāṇaṃ": "Dukkhe ñāṇaṃ atthapaṭisambhidā, dukkhasamudaye ñāṇaṃ dhammapaṭisambhidā, dukkhanirodhe ñāṇaṃ "
                    "atthapaṭisambhidā, dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ dhammapaṭisambhidā, tatra "
                    "dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā, ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā. Ayaṃ saccavāro.",
    "Hetumhi ñāṇaṃ": "Hetumhi ñāṇaṃ dhammapaṭisambhidā, hetuphale ñāṇaṃ atthapaṭisambhidā, tatra dhammaniruttābhilāpe "
                     "ñāṇaṃ niruttipaṭisambhidā, ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā. Ayaṃ hetuvāro.",
    "Ye dhammā jātā": "Ye dhammā jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā, imesu dhammesu ñāṇaṃ "
                      "atthapaṭisambhidā; yamhā dhammā te dhammā jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā, "
                      "tesu dhammesu ñāṇaṃ dhammapaṭisambhidā; tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā; "
                      "ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā. Ayaṃ dhammavāro.",
    "Jarāmaraṇe ñāṇaṃ": "Jarāmaraṇe ñāṇaṃ atthapaṭisambhidā, jarāmaraṇasamudaye ñāṇaṃ dhammapaṭisambhidā, "
                        "jarāmaraṇanirodhe ñāṇaṃ atthapaṭisambhidā, jarāmaraṇanirodhagāminiyā paṭipadāya ñāṇaṃ "
                        "dhammapaṭisambhidā, tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā, ñāṇesu ñāṇaṃ "
                        "paṭibhānapaṭisambhidā.",
    "Jātiyā ñāṇaṃ": "Jātiyā ñāṇaṃ…pe… bhave ñāṇaṃ…pe… upādāne ñāṇaṃ…pe… taṇhāya ñāṇaṃ…pe… vedanāya ñāṇaṃ…pe… phasse "
                    "ñāṇaṃ…pe… saḷāyatane ñāṇaṃ…pe… nāmarūpe ñāṇaṃ…pe… viññāṇe ñāṇaṃ…pe… saṅkhāresu ñāṇaṃ "
                    "atthapaṭisambhidā, saṅkhārasamudaye ñāṇaṃ dhammapaṭisambhidā, saṅkhāranirodhe ñāṇaṃ "
                    "atthapaṭisambhidā, saṅkhāranirodhagāminiyā paṭipadāya ñāṇaṃ dhammapaṭisambhidā, tatra "
                    "dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā, ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā. Ayaṃ "
                    "paṭiccasamuppādavāro.",
}


def check15(t, key):
    """hand line: the Pāli after the opening list must be exactly the checked text."""
    if key in _FIXED15:
        assert t.endswith(_FIXED15[key]), (key, t[-120:])
    elif key.startswith("Tattha katamā dhammapaṭisambhidā"):
        assert t == _P724, t


TISSO_P = "Tisso paṭisambhidā – atthapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā."
CATASSO_P = "Catasso paṭisambhidā – atthapaṭisambhidā, dhammapaṭisambhidā, niruttipaṭisambhidā, paṭibhānapaṭisambhidā."
YENA_P = ('Yena ñāṇena tāni ñāṇāni jānāti – "imāni ñāṇāni idamatthajotakānī"ti, ñāṇesu ñāṇaṃ '
          'paṭibhānapaṭisambhidā.')
YAYA_P = "Yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā."
OPEN15 = re.compile(r"^Yasmiṃ samaye (.+?), tasmiṃ samaye (.+?)(, ime dhammā kusalā)?\.$")
TAS15 = re.compile(r"^Tasseva (.+?), tasmiṃ samaye (.+)\.$")
P745_SPLIT = "…pe… rūpāvacaraṃ jhānaṃ bhāveti…pe… "
KIRIYA_RUPA = between(X.PREFIX["rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ "
                               "diṭṭhadhammasukhavihāraṃ "], X.MOT, ", mang tính chức năng")   # tu tập tầng thiền thuộc cõi hình sắc


def opening15(p):
    if P745_SPLIT in p:   # ^2-745: kiriya mind types…pe… rūpāvacara…pe… arūpāvacara jhāna (one opening)
        a, b = p.split(P745_SPLIT)
        pre = "arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ"
        assert b.startswith(pre + "…pe… "), b[:80]
        bv = X.jopen(pre + " " + b[len(pre) + len("…pe… "):])
        bv = repl(bv, "ngay trong đời này, hoàn toàn vượt qua", "ngay trong đời này… hoàn toàn vượt qua")
        assert bv.startswith(X.MOT)
        return f"{compose(a)}… {KIRIYA_RUPA}… {bv[len(X.MOT):]}"
    return opening_any(p)


ATTHA_UPP = ("Ba loại hiểu biết thông suốt sinh khởi trong bốn loại tâm thiện thuộc cõi dục lạc gắn liền với hiểu biết, "
             "trong bốn loại tâm mang tính chức năng gắn liền với hiểu biết.")   # [new; cittuppāda pi-1 «loại tâm»]
ATTHA_UPP2 = ("Hiểu biết thông suốt về ý nghĩa sinh khởi trong chính những loại tâm này, và sinh khởi trong bốn con "
              "đường và bốn thành quả.")                                     # [new; magga / phala pi-1]
in_pi1("loại tâm thiện thuộc cõi dục lạc", "loại tâm mang tính chức năng", "Bốn con đường")


def s15(s):
    if s == CATASSO_P:
        return CATASSO
    if s == TISSO_P:
        return TISSO
    m = re.match(r"^Katame dhammā (kusalā|akusalā|abyākatā)\?$", s)
    if m:
        return KATAME[m.group(1)]
    m = re.match(r"^Ime dhammā (kusalā|akusalā|abyākatā)\.$", s)
    if m:
        return IME[m.group(1)]
    m = OPEN15.match(s)
    if m:
        op, r, ime = m.groups()
        vi = f"Vào lúc {opening15(op)}, {tail(r)}"
        if ime:   # ^2-725 ", ime dhammā kusalā" (comma; elsewhere a new sentence): as written
            SLIPS.append("^2-725 ', ime dhammā kusalā' (comma, as written)")
            vi += ", " + low(IME["kusalā"][:-1])
        return vi + "."
    m = TAS15.match(s)
    if m:
        return f"{X.jtas(m.group(1))}, {tail(m.group(2))}."
    m = re.match(r"^Imesu dhammesu ñāṇaṃ (attha|dhamma)paṭisambhidā\.$", s)
    if m:
        return cap(kn("những hiện tượng này", m.group(1))) + "."
    if s == "Tesaṃ vipāke ñāṇaṃ atthapaṭisambhidā.":
        return cap(kn("quả của chúng", "attha")) + "."
    if s == ("Tesaṃ vipāke ñāṇaṃ atthapaṭisambhidā, yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti, tatra "
             "dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā."):
        return f"{cap(kn('quả của chúng', 'attha'))}, {YAYA} {NIR}."
    if s == YAYA_P:
        SLIPS.append("comma missing before 'tatra dhammaniruttābhilāpe' (punctuation; added)")
        return f"{cap(YAYA)} {NIR}."
    if s == YENA_P:
        return YENA
    if s == ("Tisso paṭisambhidā kāmāvacarakusalato catūsu ñāṇasampayuttesu cittuppādesu, kiriyato catūsu "
             "ñāṇasampayuttesu cittuppādesu uppajjanti."):
        return ATTHA_UPP
    if s == "Atthapaṭisambhidā etesu ceva uppajjati, catūsu maggesu catūsu phalesu ca uppajjati.":
        return ATTHA_UPP2
    raise KeyError("s15: " + s[:90])


def abhi15(t):
    if X.NOSPACE.search(t):
        SLIPS.append("space before …pe… (ch15)")
        t = X.NOSPACE.sub("…pe…", t)
    return " ".join(s15(s) for s in X.SPLIT.split(t))


# ================================================================ 7. Pañhāpucchaka
VAR_ASAVO = " [āsavā (sī.) dhātuvibhaṅge pana pāṭhanānattaṃ natthi]"
VAR_ASAVO_VI = (" [dị bản (Sī.): āsavā; nhưng trong “Phân tích các yếu tố” không có sự khác biệt về văn bản]")
assert S.CHAPTER_TITLES[3] == "Phân tích các yếu tố"
NV_DASH = re.compile(r"^(.*?)((?:siyā )?na vattabb(?:o|ā|aṃ)) " + DASH + r" (?!\")(.+)$")


class QV(X.QV):
    def chunk(self, c, state, first):
        if VAR_ASAVO in c:
            i = c.index(VAR_ASAVO)
            rest = c[i + len(VAR_ASAVO):]
            vi = self.chunk(c.replace(VAR_ASAVO, ""), state, first)
            if rest:   # āsavo [ … ] ceva sāsavā: after the first «ô nhiễm»
                assert vi.count("vừa là ô nhiễm") == 1, vi
                return vi.replace("vừa là ô nhiễm", "vừa là ô nhiễm" + VAR_ASAVO_VI)
            assert vi.endswith("ô nhiễm"), vi
            return vi + VAR_ASAVO_VI
        m = NV_DASH.match(c)
        if m:   # "na vattabbā – Xtipi" (unquoted, with a dash): dash kept («không nên nói – rằng …»)
            vi = super().chunk(f"{m.group(1)}{m.group(2)} {m.group(3)}", state, first)
            assert vi.count(H.NV0) == 1, vi
            return vi.replace(H.NV0, B.NV)
        return super().chunk(c, state, first)


F.add_item("na_maggahetuka", ["na maggahetukā"], "không " + B.P("maggahetuka"))   # ^2-749 [new; ch5 pattern]
QFIX = [   # spelling / spacing slips in the Pāli (rendered as meant, reported)
    ("Na hetū sahetukā, hetusampayuttā.", "Na hetū, sahetukā, hetusampayuttā."),   # ^2-717 comma (as ch12 / ch13)
    ("na hetu sahetūkā", "na hetu sahetukā"),                               # ^2-717
    ("na bhāvanāyapahātabbā", "na bhāvanāya pahātabbā"),                     # ^2-717
    ("Anidassanaapaṭighā", "Anidassanaappaṭighā"),                           # ^2-749
    ("nahetūahetukātipi", "na hetū ahetukātipi"),                            # ^2-750
    ("Āsavavippayuttā sāsavā", "Āsavavippayuttasāsavā"),                     # ^2-702, ^2-717 two words (as ch12)
    ("no parāmāsā …pe…", "no parāmāsā…pe…"),                                 # ^2-702 space
]


def qline(qv, t):
    for a, b in QFIX:
        if a in t:
            SLIPS.append(f"Pañhāpucchaka {a!r} -> {b!r}")
            t = t.replace(a, b)
    return qv.line(t)


SUBJ13 = {"Tisso appamaññāyo": "Ba trạng thái không thể đo lường", "tisso appamaññāyo": "ba trạng thái không thể đo lường",
          "Mettā": cap(APP["mettā"]), "mettā": APP["mettā"], "Upekkhā": cap(APP["upekkhā"]), "upekkhā": APP["upekkhā"]}
SINGLE13 = {"Mettā", "mettā", "Upekkhā", "upekkhā"}
SUBJ15 = {"Tisso paṭisambhidā": f"Ba {PS_UNIT}", "tisso paṭisambhidā": f"ba {PS_UNIT}",
          "dve paṭisambhidā": f"hai {PS_UNIT}", "atthapaṭisambhidā": PS["attha"], "Atthapaṭisambhidā": cap(PS["attha"]),
          "Niruttipaṭisambhidā": cap(PS["nirutti"])}
SINGLE15 = {"atthapaṭisambhidā", "Atthapaṭisambhidā", "Niruttipaṭisambhidā"}
QQ = {13: QV(SUBJ13, SINGLE13), 14: QV({}, set()), 15: QV(SUBJ15, SINGLE15)}

# ================================================================ 8. labels
LABELS = dict(X.LABELS)
for _n, _p in ((13, "Appamaññāvibhaṅgo"), (14, "Sikkhāpadavibhaṅgo"), (15, "Paṭisambhidāvibhaṅgo")):
    LABELS["### " + _p] = "### " + S.CHAPTER_TITLES[_n]
    LABELS[_p + " niṭṭhito."] = S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[_n])
for _k in APP:
    LABELS["##### " + cap(_k)] = "##### " + cap(APP[_k])
LABELS[LABEL_699] = P699
LABELS["Catasso appamaññāyo – mettā, karuṇā, muditā, upekkhā."] = \
    f"{cap(FOUR_APP)} {DASH} {T.listing([APP[k] for k in APP_KEYS])}."
LABELS["Catunnaṃ appamaññānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?"] = \
    T.question_q(FOUR_APP, APP_UNIT)
_SK5 = ", ".join(f"{o} veramaṇī sikkhāpadaṃ" for o in VIR_ORDER)
LABELS[f"Pañca sikkhāpadāni – {_SK5}."] = \
    f"Năm {SIKKHAPADA} {DASH} " + "; ".join(sk(o) for o in VIR_ORDER[:-1]) + f"; và {sk(VIR_ORDER[-1])}."
LABELS["Pañcannaṃ sikkhāpadānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?"] = \
    T.question_q(f"năm {SIKKHAPADA}", SIKKHAPADA)
LABELS[CATASSO_P] = CATASSO
LABELS["Catunnaṃ paṭisambhidānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?"] = \
    T.question_q(f"bốn {PS_UNIT}", PS_UNIT)
VARA = {"Saṅgahavāro": "Mục tổng hợp", "Saccavāro": "Mục về các sự thật", "Hetuvāro": "Mục về nguyên nhân",
        "Dhammavāro": "Mục về các hiện tượng", "Paṭiccasamuppādavāro": "Mục về sự sinh khởi tùy thuộc vào điều kiện",
        "Pariyattivāro": "Mục về việc học hỏi Giáo Pháp", "Kusalavāro": "Mục về thiện", "Akusalavāro": "Mục về bất thiện",
        "Vipākavāro": "Mục về quả của nghiệp", "Kiriyavāro": "Mục về chức năng"}   # vāra «mục» [APPROVED; new]
in_pi1("##### Mục về các thành phần")
for _k, _v in VARA.items():
    LABELS["##### " + _k] = "##### " + _v

# ================================================================ 9. build
CHAPTERS = (("13-appamannavibhango.md", 13), ("14-sikkhapadavibhango.md", 14), ("15-patisambhidavibhango.md", 15))
BAD = ("là là", "  ", "….", '"', " ,", " .", ":-", "thì thì", "\x01", " ;", ";;", ",,", "chánh niệm", "..", ", ,",
       "None", "—")


def translate(pali_lines, ch):
    hand = list(HAND15) if ch == 15 else []
    out, section = [], None
    for pl in pali_lines:
        if not pl.strip():
            out.append("")
            continue
        m = S.ID.search(pl)
        t = S.ID.sub("", pl).rstrip()
        if t.startswith("#### "):
            section = {"Suttantabhājanīyaṃ": "sutta", "Abhidhammabhājanīyaṃ": "abhi", "Pañhāpucchakaṃ": "q"}[t[5:]]
        if t in LABELS:
            vi = LABELS[t]
        elif section == "sutta" and ch == 13:
            vi = sutta13(t)
        elif section == "sutta" and ch == 15:
            assert hand and t.startswith(hand[0][0]), (t[:90], hand[0][0][:60] if hand else None)
            key = [k for k in list(_FIXED15) + ["Tattha katamā dhammapaṭisambhidā"] if k in t]
            check15(t, key[0] if key else "")
            vi = hand.pop(0)[1]
        elif section == "q":
            vi = qline(QQ[ch], t)
        elif ch == 13:
            vi = X.abhi_line(t)
        elif ch == 14:
            vi = abhi14(t)
        else:
            vi = abhi15(t)
        assert pl.count(DASH) + pl.count("—") == vi.count(DASH), ("dash count", t[:70], vi[:90])
        for bad in BAD:
            assert bad not in vi, (bad, vi[:160])
        out.append(vi + (" " + m.group(1) if m else ""))
    assert not hand, [h[0][:50] for h in hand]
    return out


HAND_SLIPS = [
    "^2-720 'dhammapaṭisambhidā niruttipaṭisambhidā' (comma missing; rendered with the comma)",
    "^2-699 'pharitvā viharati tathā dutiyaṃ tathā tatiyaṃ …' (commas missing; rendered with commas)",
    "^2-686 line 2 karuṇā 'pītiyā ca virāgā…pe… dutiyaṃ jhānaṃ' (mettā / muditā: vitakkavicārānaṃ vūpasamā), as written",
    "^2-740 'Tasseva lokuttarassa kusalassa kammassa katattā bhāvitattā' (pi-1 jhānassa), as written «nghiệp thiện»",
]


def build():
    SLIPS.extend(HAND_SLIPS)
    res = {}
    for fn, ch in CHAPTERS:
        pali = open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().rstrip("\n").split("\n")
        res[os.path.join(S.VI_DIR, fn)] = translate(pali, ch)
    return res


def main():
    res = build()
    dry = "--dry" in sys.argv
    for path, lines in res.items():
        if not dry:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write("\n".join(lines).rstrip("\n") + "\n")
        print("OK:" if not dry else "DRY:", path, "|", len([x for x in lines if x.strip()]), "non-empty lines")
    print("pi-1 openings recomposed:", N_OPEN, "| mind-type openings recomposed:", N_COMPOSE)
    for s in sorted(set(SLIPS + X.SLIPS)):
        print("slip:", s)


if __name__ == "__main__":
    main()
