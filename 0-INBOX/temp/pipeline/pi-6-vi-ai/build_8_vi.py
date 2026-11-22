# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 8-cittayamaka.md: FRAME-SETTER of family D (Cittayamaka).

Family D = puggalavāra / dhammavāra / puggaladhammavāra, the fourteen time sections, uppajjamāna /
nirujjhamāna, uppanna / niruddha, atikkantakāla, the suttanta / abhidhamma mixtures. Every frame is a module
constant or helper function; later agents import this module and use them VERBATIM:

    import sys; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    import build_8_vi as C
    C.VERB["uppajjissati"]; C.NEGVERB["uppannaṃ"]; C.phrase("uppajjati na nirujjhati")
    C.question("P", "uppajjati", "uppannaṃ", kha=False, label="Ka"); C.answer_sentence("…")

The tense / aspect contrasts (each Pāli form has its own Vietnamese, never shared):
    uppajjati «sinh khởi»          na «không sinh khởi»                  (present)
    uppajjamāna «đang sinh khởi»   na «không đang sinh khởi»             (present participle, in progress)
    uppanna «ở trạng thái đã sinh khởi»  na «không ở trạng thái đã sinh khởi»  (arisen and not yet ceased)
    uppajjittha «đã sinh khởi»     na «chưa từng sinh khởi»              (past, = 2-01; no ca + na: «đã từng …»)
    uppajjissati «sẽ sinh khởi»    na «sẽ không sinh khởi»               (future)
    the same for nirujjhati «chấm dứt» … niruddha «ở trạng thái đã chấm dứt».

Chapter 8 is translated by a sentence parser (translate_line), as in the sample: each Pāli sentence must match
one fixed frame, else the build stops. Importing writes nothing; run  python -I -X utf8 -B build_8_vi.py  to
write the chapter. At build time the sample's cross-book asserts and this chapter's own (CROSS_BOOK_8) run,
and every output line is checked with the sample's check_lines (IDs, dash / quote / "?" counts, NFC, Latin).
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

CH = "8-cittayamaka.md"
cap, low = S.cap, S.low

# ================================================================ verbs: tense / aspect (family D core)
VERB = {
    "uppajjati": "sinh khởi",                       # present (pi-5 «sinh khởi»)
    "nirujjhati": "chấm dứt",                       # present (pi-5 «chấm dứt»; nirodha «sự chấm dứt» pi-1)
    "uppajjittha": "đã sinh khởi",                  # past (aorist) = 2-01 TENSE_POS["past"]
    "nirujjhittha": "đã chấm dứt",
    "uppajjissati": "sẽ sinh khởi",                 # future (pi-5 «sẽ sinh khởi»)
    "nirujjhissati": "sẽ chấm dứt",
    "uppajjamānaṃ": "đang sinh khởi",               # present participle (pi-5 vimuccamāna «đang được giải thoát»)
    "nirujjhamānaṃ": "đang chấm dứt",
    "uppannaṃ": "ở trạng thái đã sinh khởi",        # past participle = arisen and not yet ceased (aṭṭhakathā ^6-163)
    "niruddhaṃ": "ở trạng thái đã chấm dứt",
}
NEGVERB = {
    "uppajjati": "không sinh khởi",
    "nirujjhati": "không chấm dứt",
    "uppajjittha": "chưa từng sinh khởi",
    "nirujjhittha": "chưa từng chấm dứt",
    "uppajjissati": "sẽ không sinh khởi",           # pi-5 «sẽ không sinh khởi»
    "nirujjhissati": "sẽ không chấm dứt",
    "uppajjamānaṃ": "không đang sinh khởi",
    "nirujjhamānaṃ": "không đang chấm dứt",
    "uppannaṃ": "không ở trạng thái đã sinh khởi",
    "niruddhaṃ": "không ở trạng thái đã chấm dứt",
}
VERB_RE = "|".join(sorted(VERB, key=len, reverse=True))
TOK_RE = rf"(?:na )?(?:{VERB_RE})"
PH_RE = rf"{TOK_RE}(?: {TOK_RE})*"
JOIN = " nhưng "              # X na Y / na X Y (two predicates in one clause): «sinh khởi nhưng không chấm dứt»
# (not «mà»: the 7-01 person frame already has «Ở người nào mà …»)
# no ca … (7-01 rule): a denied positive is said negatively, a denied negative is said plainly with «vẫn»
DENIED = {v: "vẫn " + VERB[v] for v in VERB}       # = 2-01 DENY_NEG («vẫn sinh khởi», «vẫn sẽ sinh khởi»)
DENIED["uppajjittha"] = "đã từng sinh khởi"         # = 2-01 DENY_NEG["past"]
DENIED["nirujjhittha"] = "đã từng chấm dứt"


def tok(t):
    """one Pāli predicate token, optional «na», ti-forms already removed"""
    t = t.strip()
    if t.startswith("na "):
        return NEGVERB[t[3:]]
    return VERB[t]


def phrase(p):
    """«uppajjati na nirujjhati» -> «sinh khởi mà không chấm dứt»"""
    toks = re.findall(TOK_RE, p)
    assert " ".join(toks) == p.strip(), f"unparsed phrase {p!r}"
    return JOIN.join(tok(t) for t in toks)


def denied(p):
    """the predicate after «no ca …»: «uppajjati» -> «không sinh khởi»; «na uppannaṃ» -> «vẫn ở trạng thái đã …»"""
    p = p.strip()
    assert re.fullmatch(TOK_RE, p), f"no ca takes one predicate: {p!r}"
    return DENIED[p[3:]] if p.startswith("na ") else NEGVERB[p]


def unti(s):
    """drop the quotation «ti» before the final «?»: uppajjatīti? -> uppajjati?, uppannanti? -> uppannaṃ?"""
    return re.sub(r"(\S+?)(īti|āti|nti)\?$",
                  lambda m: m[1] + {"īti": "i", "āti": "a", "nti": "ṃ"}[m[2]] + "?", s)


def restore(stem):
    """uppanna(ñceva) -> uppannaṃ; uppajjamāna(ñca) -> uppajjamānaṃ; plain verbs unchanged"""
    neg = stem.startswith("na ")
    w = stem[3:] if neg else stem
    if w not in VERB and w + "ṃ" in VERB:
        w += "ṃ"
    return ("na " if neg else "") + w


# ================================================================ answers
ANS = {
    "Āmantā.": S.AMANTA,          # Đúng vậy. (pi-5, sample)
    "No.": "Không.",              # No. (new)
    "Natthi.": "Không có.",       # Natthi. (pi-3 «Không có.»)
}
# one-word answers naming the predicate: Uppajjittha. = Đã từng sinh khởi. / Uppannaṃ. = Ở trạng thái đã sinh khởi.
for _v in VERB:
    ANS[cap(_v) + "."] = cap(VERB[_v]) + "."
for _v in ("uppajjati", "nirujjhati"):                # 2-01 SHORT["pres"]: Uppajjati. = Có sinh khởi.
    ANS[cap(_v) + "."] = f"Có {VERB[_v]}."

# ================================================================ citta kinds (suttanta / abhidhamma mixtures)
KIND = {
    # suttanta (pi-2 Satipaṭṭhānavibhaṅga / Ñāṇavibhaṅga «Tâm có tham đắm» …)
    "sarāgaṃ": "có tham đắm", "vītarāgaṃ": "đã lìa tham đắm", "sadosaṃ": "có sân hận",
    "vītadosaṃ": "đã lìa sân hận", "samohaṃ": "có si mê", "vītamohaṃ": "đã lìa si mê",
    "saṃkhittaṃ": "co rút", "vikkhittaṃ": "tán loạn", "mahaggataṃ": "rộng lớn",
    "amahaggataṃ": "không rộng lớn", "sauttaraṃ": "còn có điều cao hơn",
    "anuttaraṃ": "không có điều gì cao hơn", "samāhitaṃ": "được định tâm",
    "asamāhitaṃ": "không được định tâm", "vimuttaṃ": "được giải thoát", "avimuttaṃ": "không được giải thoát",
    # abhidhamma (pi-1 matrix)
    "kusalaṃ": S.CAT["kusala"]["adj"], "akusalaṃ": S.CAT["akusala"]["adj"],
    "abyākataṃ": S.CAT["abyākata"]["adj"],
    "sukhāya vedanāya sampayuttaṃ": "gắn liền với cảm giác dễ chịu",
    "saraṇaṃ": "có xung đột", "araṇaṃ": "không có xung đột",
}
KIND_STEM = {k[:-1]: v for k, v in KIND.items() if k.endswith("ṃ") and " " not in k}   # sarāga…, kusala…
KIND_RE = "|".join(sorted(map(re.escape, KIND), key=len, reverse=True))
SUTTANTA_KINDS = ["sarāgaṃ", "vītarāgaṃ", "sadosaṃ", "vītadosaṃ", "samohaṃ", "vītamohaṃ", "saṃkhittaṃ",
                  "vikkhittaṃ", "mahaggataṃ", "amahaggataṃ", "sauttaraṃ", "anuttaraṃ", "samāhitaṃ",
                  "asamāhitaṃ", "vimuttaṃ", "avimuttaṃ"]
ABHIDHAMMA_KINDS = ["kusalaṃ", "akusalaṃ", "abyākataṃ", "sukhāya vedanāya sampayuttaṃ"]


def citta(kind=None, last=False):
    """tâm [kind] [cuối cùng]: kusalaṃ cittaṃ = tâm thiện; pacchimacitta = tâm cuối cùng"""
    s = "tâm"
    if kind:
        s += " " + (KIND.get(kind) or KIND_STEM[kind])
    if last:
        s += " " + PACCHIMA
    return s


PACCHIMA = "cuối cùng"        # pacchima (-citta): the final citta (aṭṭhakathā ^6-162: the arahant's last death-citta)

# ================================================================ the three great sections: who is asked about
# mode P = puggalavāra (yassa … tassa …), D = dhammavāra (yaṃ … taṃ …), PD = puggaladhammavāra (yassa yaṃ … tassa taṃ …)
# person frame aligned with 7-01 (coordinator rules «From 7-01»): yassa … tassa … = Ở người nào mà … thì ở người ấy …
WHO = {      # (opening, «where» before «có phải», resumptive citta)   k = citta noun phrase
    "P": ("Ở người nào mà {k}", "ở người ấy ", "{k}"),
    "D": ("{k} nào", "", "{k} ấy"),
    "PD": ("Ở người nào mà {k} nào", "ở người ấy ", "{k} ấy"),
}
KHA_PREFIX = "Còn "           # yassa vā pana / yaṃ vā pana (sample KHA_Q, 7-01 «Còn ở người nào mà …»)
Q = "{s} {a}, thì {w}có phải {c} {b} không?"                    # yassa cittaṃ A tassa cittaṃ B(ti)?
Q_NOCA = "{s} {a}, {nc}, thì {w}có phải {c} {b} không?"
# yassa cittaṃ A no ca tassa cittaṃ N, tassa cittaṃ B(ti)?   (11) atītānāgatavāra
NO_CA = "nhưng {x}"           # no ca R N = «nhưng R <denied N>» (7-01: «nhưng ở người ấy B không …» / «vẫn …»)
Q_SHORT = "Cái {a} thì có phải {b} không?"                      # (12)/(13): uppannaṃ uppajjamānaṃ(ti)?
# (14) atikkantakāla: «uppajjamānaṃ khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ» (aṭṭhakathā ^6-165:
# uppajjamānaṃ khaṇaṃ = the arising moment; khaṇaṃ vītikkantaṃ atikkantakālaṃ = having passed it, its time gone)
MOMENT_M = {"uppajjamānaṃ": "khoảnh khắc đang sinh khởi", "nirujjhamānaṃ": "khoảnh khắc đang chấm dứt"}
ATI = "về {m}, {neg}đã vượt qua khoảnh khắc ấy và thời của nó đã qua"
ATI_NEG = "không phải là "    # na uppajjamānaṃ khaṇaṃ … (one «na» over the whole phrase)
Q_ATI = "{s}, {a1}, {a2}, thì {w}{c} có như vậy không?"        # yassa cittaṃ <ati1>, <ati2> tassa cittaṃ(ti)?


def ati(neg, m):
    return ATI.format(m=MOMENT_M[m], neg=ATI_NEG if neg else "")


def labelled(text, label, kha):
    text = (KHA_PREFIX + low(text)) if kha else cap(text)
    return f"{S.LABEL[label]} {text}" if label else text


def who(mode, kind=None):
    k = citta(kind)
    s, w, c = WHO[mode]
    return s.format(k=k), w, c.format(k=k)


def question(mode, a, b, kha=False, label=None, kind=None, noca=None):
    """a, b: Pāli predicate phrases (e.g. «uppajjati na nirujjhati», «na uppannaṃ»)"""
    s, w, c = who(mode, kind)
    if noca is not None:
        nc = NO_CA.format(x=f"{w}{c} {denied(noca)}")
        t = Q_NOCA.format(s=s, a=phrase(a), nc=nc, w=w, c=c, b=phrase(b))
    else:
        t = Q.format(s=s, a=phrase(a), w=w, c=c, b=phrase(b))
    return labelled(t, label, kha)


Q_RE = re.compile(
    rf"(?:\((?P<l>Ka|Kha)\) )?(?P<h>[Yy]assa vā pana yaṃ|[Yy]assa yaṃ|[Yy]assa vā pana|[Yy]assa|[Yy]aṃ vā pana|[Yy]aṃ)"
    rf" (?:(?P<k>{KIND_RE}) )?cittaṃ (?P<a>.+?)"
    rf"(?: no ca (?P<r1>tassa taṃ|tassa|taṃ) cittaṃ (?P<n>{PH_RE}),)?"
    rf" (?P<r>tassa taṃ|tassa|taṃ) (?:(?P<k2>{KIND_RE}) )?cittaṃ(?: (?P<b>{PH_RE}))?\?")
ATI_RE = re.compile(rf"(?P<n1>na )?(?P<m1>uppajjamānaṃ|nirujjhamānaṃ) khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ, "
                    rf"(?P<n2>na )?(?P<m2>uppajjamānaṃ|nirujjhamānaṃ) khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ")
SHORT_RE = re.compile(rf"\((?P<l>Ka|Kha)\) (?P<a>{TOK_RE}) (?P<b>{TOK_RE})\?")


def mode_of(h):
    h = h.lower()
    if h.startswith("yassa") and "yaṃ" in h:
        return "PD"
    return "P" if h.startswith("yassa") else "D"


def translate_question(s):
    s = unti(s)
    m = SHORT_RE.fullmatch(s)
    if m:
        return f"{S.LABEL[m['l']]} " + Q_SHORT.format(a=tok(m["a"]), b=tok(m["b"]))
    m = Q_RE.fullmatch(s)
    if not m:
        return None
    mode, kha, label = mode_of(m["h"]), "vā pana" in m["h"], m["l"]
    assert m["k"] == m["k2"], s
    am = ATI_RE.fullmatch(m["a"])
    if am:
        assert not m["b"], s
        sv, wv, cv = who(mode, m["k"])
        t = Q_ATI.format(s=sv, a1=ati(am["n1"], am["m1"]), a2=ati(am["n2"], am["m2"]), w=wv, c=cv)
        return labelled(t, label, kha)
    return question(mode, m["a"], m["b"], kha=kha, label=label, kind=m["k"], noca=m["n"])


# ================================================================ answer subjects
MOMENT = {"uppāda": "khoảnh khắc sinh khởi", "bhaṅga": "khoảnh khắc tan rã"}   # uppādakkhaṇa / bhaṅgakkhaṇa (pi-5)
AT = "vào {x}"                                             # <X>kkhaṇe (locative of time)
OF = "{x} của {c}"                                         # cittassa uppādakkhaṇe = khoảnh khắc sinh khởi của tâm
FOR = "ở {x}"                                              # genitive of persons (7-01 «Ở người phàm phu»)
THEY = "những người ấy"                                    # tesaṃ (resumptive; 7-01 «ở những người ấy»)
OTHERS = "những người khác"                                # itaresaṃ (itara «khác»)
NIRODHA_PERSONS = "những người nhập thành tựu thiền chấm dứt"   # nirodhasamāpannānaṃ (pi-5 «thành tựu thiền chấm dứt»)
ASANNA_BEINGS = "chúng sinh Vô Tưởng"                      # asaññasattānaṃ (pi-5; = 2-01 BEINGS)
SAMANGI = "những người có được {c}"                        # Xsamaṅgīnaṃ (pi-5 samaṅgī «người có được»)


def when(moment, kind=None, last=False):
    """Pacchimacittassa uppādakkhaṇe = vào khoảnh khắc sinh khởi của tâm cuối cùng"""
    return AT.format(x=OF.format(x=MOMENT[moment], c=citta(kind, last)))


def for_(x):
    return FOR.format(x=x)


LIST_SEP = ", "               # asyndetic genitive lists under one «ở» (2-01 LIST_SEP / WHO_HEAD)
NIRODHA_ASANNA = for_(LIST_SEP.join((NIRODHA_PERSONS, ASANNA_BEINGS)))   # nirodhasamāpannānaṃ asaññasattānaṃ

# puggalavāra answer subjects (the words before «tesaṃ [kind] cittaṃ»)
P_SUBJ = {
    "Pacchimacittassa uppādakkhaṇe": when("uppāda", last=True),
    "Pacchimacittassa bhaṅgakkhaṇe": when("bhaṅga", last=True),
    "Itaresaṃ cittassa uppādakkhaṇe": f"{for_(OTHERS)}, {when('uppāda')}",
    "Itaresaṃ cittassa bhaṅgakkhaṇe": f"{for_(OTHERS)}, {when('bhaṅga')}",
    "Cittassa uppādakkhaṇe": when("uppāda"),
    "Cittassa bhaṅgakkhaṇe": when("bhaṅga"),
    "Nirodhasamāpannānaṃ asaññasattānaṃ": NIRODHA_ASANNA,
    "Cittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ": f"{when('uppāda')}, {NIRODHA_ASANNA}",
    "Cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ": f"{when('bhaṅga')}, {NIRODHA_ASANNA}",
    "Pacchimacittasamaṅgīnaṃ": for_(SAMANGI.format(c=citta(last=True))),
    "Cittasamaṅgīnaṃ": for_(SAMANGI.format(c=citta())),
    "Itaresaṃ cittasamaṅgīnaṃ": for_(f"{OTHERS} có được {citta()}"),
    "Itaresaṃ": for_(OTHERS),
    "Sarāgapacchimacittassa uppādakkhaṇe": when("uppāda", "sarāga", last=True),
    "Pacchimakusalacittassa uppādakkhaṇe": when("uppāda", "kusala", last=True),
}
# dhammavāra / puggaladhammavāra answer subjects (the words before «cittaṃ»): which citta
TIME = {"Atītaṃ": "thuộc quá khứ", "Anāgataṃ": "thuộc tương lai", "Paccuppannaṃ": "thuộc hiện tại",   # pi-1 matrix
        "Atītānāgataṃ": "thuộc quá khứ và tương lai"}
AT_MOMENT_CITTA = "tâm vào {x}"                            # Bhaṅgakkhaṇe cittaṃ = tâm vào khoảnh khắc tan rã
AND = "{a} và {b}"                                         # Xkkhaṇe anāgatañca cittaṃ (aṭṭhakathā ^6-164: two cittas)
D_SUBJ = {
    "Bhaṅgakkhaṇe": AT_MOMENT_CITTA.format(x=MOMENT["bhaṅga"]),
    "Uppādakkhaṇe": AT_MOMENT_CITTA.format(x=MOMENT["uppāda"]),
}
for _t, _v in TIME.items():
    D_SUBJ[_t] = f"tâm {_v}"
for _m, _x in (("Bhaṅgakkhaṇe", "anāgatañca"), ("Uppādakkhaṇe", "anāgatañca"), ("Bhaṅgakkhaṇe", "atītañca")):
    D_SUBJ[f"{_m} {_x}"] = AND.format(a=D_SUBJ[_m], b="tâm " + TIME[cap(_x[:-3]) + "ṃ"])
BARE_SUBJ = {"Bhaṅgakkhaṇe": AT.format(x=MOMENT["bhaṅga"]),      # (12)/(13) without «cittaṃ»
             "Uppādakkhaṇe": AT.format(x=MOMENT["uppāda"])}
RESUME = {"tesaṃ cittaṃ": f"{for_(THEY)} tâm",              # no ca tesaṃ cittaṃ = nhưng ở những người ấy tâm …
          "taṃ cittaṃ": "tâm ấy",                          # no ca taṃ cittaṃ = nhưng tâm ấy …
          "tassa taṃ cittaṃ": "ở người ấy tâm ấy",         # no ca tassa taṃ cittaṃ = nhưng ở người ấy tâm ấy …
          None: ""}

# answer predicates (no subject). A sentence is then
#   puggalavāra:  «<head>, thì ở những người ấy tâm <pred>.»   (2-01 / 7-01 STATEMENT_RES «{head}, thì {res} {clause}.»)
#   dhammavāra / puggaladhammavāra / (12)(13):  «<which citta / when> thì <pred>.»   (sample BOTH / BUT_NOT «thì»)
P_ANS = "{head}, thì {res} {c} {p}."                       # G tesaṃ [K] cittaṃ P.
D_ANS = "{s} thì {p}."                                     # S cittaṃ P. / Bhaṅgakkhaṇe P.
PRED_BUT = "{a}, " + NO_CA                                 # A, no ca R B.  (x = R + denied B)
PRED_BOTH = "vừa {a} vừa {b}"                              # Añceva Bñca / A ceva B ca (sample BOTH)
PRED_NEITHER = "{a}, cũng {b}"                             # na ceva A na ca B.  (a, b: the negated forms)
PRED_PAIR = "{a}, {b}"                                     # A na B, C na D. / A na B, C ceva D ca.
assert D_ANS.format(s="{s}", p=PRED_BOTH) == S.BOTH        # the dhammavāra «both» line is the sample's BOTH frame

CEVA_RE = rf"(?P<ca>(?:na )?\S+?)(?:ñceva| ceva) (?P<cb>(?:na )?\S+?)(?:ñca| ca)"


def pred(p):
    """answer predicate (Pāli, no final '.') -> Vietnamese predicate"""
    m = re.fullmatch(rf"(?P<a>{PH_RE}), no ca (?:(?P<r>tesaṃ cittaṃ|tassa taṃ cittaṃ|taṃ cittaṃ) )?(?P<b>{PH_RE})", p)
    if m:
        r = RESUME[m["r"]]
        return PRED_BUT.format(a=phrase(m["a"]), x=(r + " " if r else "") + denied(m["b"]))
    m = re.fullmatch(CEVA_RE, p)
    if m:
        return PRED_BOTH.format(a=tok(restore(m["ca"])), b=tok(restore(m["cb"])))
    m = re.fullmatch(r"na ceva (?P<a>\S+) na ca (?P<b>\S+)", p)
    if m:
        return PRED_NEITHER.format(a=tok("na " + m["a"]), b=tok("na " + m["b"]))
    m = re.fullmatch(rf"(?P<a>{PH_RE}), (?P<b>{PH_RE})", p)
    if m:
        return PRED_PAIR.format(a=phrase(m["a"]), b=phrase(m["b"]))
    m = re.fullmatch(rf"(?P<a>{PH_RE}), {CEVA_RE}", p)
    if m:
        return PRED_PAIR.format(a=phrase(m["a"]),
                                b=PRED_BOTH.format(a=tok(restore(m["ca"])), b=tok(restore(m["cb"]))))
    raise ValueError(f"unparsed answer predicate {p!r}")


P_SUBJ_RE = "|".join(sorted(map(re.escape, P_SUBJ), key=len, reverse=True))
D_SUBJ_RE = "|".join(sorted(map(re.escape, D_SUBJ), key=len, reverse=True))
ANS_P_RE = re.compile(rf"(?P<s>{P_SUBJ_RE}) tesaṃ (?:(?P<k>{KIND_RE}) )?cittaṃ (?P<p>.+)\.")
ANS_D_RE = re.compile(rf"(?P<s>{D_SUBJ_RE}) cittaṃ (?P<p>.+)\.")
ANS_BARE_RE = re.compile(r"(?P<s>Bhaṅgakkhaṇe|Uppādakkhaṇe) (?P<p>.+)\.")
PE_OTHERS_RE = re.compile(r"Itaresaṃ (?P<k>sarāga|kusala)cittassa uppādakkhaṇe tesaṃ…pe…\.")
PE = "…"                      # …pe… (sample)


def translate_answer(s):
    if s in ANS:
        return ANS[s]
    m = ANS_P_RE.fullmatch(s)
    if m:
        return P_ANS.format(head=cap(P_SUBJ[m["s"]]), res=for_(THEY), c=citta(m["k"]), p=pred(m["p"]))
    m = ANS_D_RE.fullmatch(s)
    if m:
        return D_ANS.format(s=cap(D_SUBJ[m["s"]]), p=pred(m["p"]))
    m = ANS_BARE_RE.fullmatch(s)
    if m:
        return D_ANS.format(s=cap(BARE_SUBJ[m["s"]]), p=pred(m["p"]))
    m = PE_OTHERS_RE.fullmatch(s)
    if m:
        return cap(f"{for_(OTHERS)}, {when('uppāda', m['k'])}, thì {for_(THEY)}{PE}")
    return None


# ================================================================ (14) atikkantakāla answers
PASSED, NOT_PASSED = "đã vượt qua", "chưa vượt qua"          # vītikkanta / avītikkanta


def _pass(neg, moment):
    return f"{NOT_PASSED if neg else PASSED} {MOMENT[moment]}"


ATI_ANS_1 = (f"{cap(D_SUBJ['Bhaṅgakkhaṇe'])} thì {_pass(0, 'uppāda')}, {_pass(1, 'bhaṅga')}, "
             f"{D_SUBJ['Atītaṃ']} thì vừa {_pass(0, 'uppāda')} vừa {_pass(0, 'bhaṅga')}.")
# «no ca uppādakkhaṇaṃ avītikkantaṃ»: denied «chưa vượt qua» said plainly = «đã vượt qua» (7-01 no-ca rule)
ATI_ANS_4 = (f"{cap(D_SUBJ['Bhaṅgakkhaṇe'])} thì {_pass(1, 'bhaṅga')}, {NO_CA.format(x=_pass(0, 'uppāda'))}, "
             f"{D_SUBJ['Uppādakkhaṇe anāgatañca']} thì vừa {_pass(1, 'bhaṅga')} vừa {_pass(1, 'uppāda')}.")
EXACT_SENT = {
    # ^6-8-83 «vītakkantaṃ» (spelling slip, rendered as meant) / ^6-8-104 «vītikkantaṃ»
    ("Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītakkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca "
     "vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ."): ATI_ANS_1,
    ("Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītikkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca "
     "vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ."): ATI_ANS_1,
    "Atītaṃ cittaṃ.": cap(D_SUBJ["Atītaṃ"]) + ".",
    "Uppādakkhaṇe anāgataṃ cittaṃ.": f"{cap(D_SUBJ['Uppādakkhaṇe'])}, tâm {TIME['Anāgataṃ']}.",
    ("Bhaṅgakkhaṇe cittaṃ bhaṅgakkhaṇaṃ avītikkantaṃ no ca uppādakkhaṇaṃ avītikkantaṃ, uppādakkhaṇe anāgatañca "
     "cittaṃ bhaṅgakkhaṇañca avītikkantaṃ uppādakkhaṇañca avītikkantaṃ."): ATI_ANS_4,
}

# ================================================================ headings
SUDDHA = "Tâm thuần túy nói chung"                         # Suddhacittasāmaññaṃ / -sāmañña (suddha «thuần túy» pi-5)
TRANG_THAI = "trạng thái {x}"                              # uppanna / uppajjamāna … as section-title nouns
UPP_N, NIR_N = "sự sinh khởi", "sự chấm dứt"                # uppāda / nirodha (pi-1)
UPPANNA_N = TRANG_THAI.format(x=VERB["uppannaṃ"][len("ở trạng thái "):])           # trạng thái đã sinh khởi
NIRUDDHA_N = TRANG_THAI.format(x=VERB["niruddhaṃ"][len("ở trạng thái "):])         # trạng thái đã chấm dứt
UPPAJJAMANA_N = TRANG_THAI.format(x=VERB["uppajjamānaṃ"])                          # trạng thái đang sinh khởi
NIRUJJHAMANA_N = TRANG_THAI.format(x=VERB["nirujjhamānaṃ"])                        # trạng thái đang chấm dứt
V = S.VARO.format
TIME_SECTION = {
    "Uppādanirodhakālasambhedavāro": V(x=f"sự kết hợp các thời của {UPP_N} và {NIR_N}"),
    "Uppāduppannavāro": V(x=f"{UPP_N} và {UPPANNA_N}"),
    "Nirodhuppannavāro": V(x=f"{NIR_N} và {UPPANNA_N}"),
    "Uppādavāro": V(x=UPP_N),
    "Nirodhavāro": V(x=NIR_N),
    "Uppādanirodhavāro": S.SECTION["Uppādanirodhavāro"],
    "Uppajjamāna-nanirodhavāro": V(x=f"{UPPAJJAMANA_N} và sự không chấm dứt"),
    "Uppajjamānananirodhavāro": V(x=f"{UPPAJJAMANA_N} và sự không chấm dứt"),
    "Uppajjamānuppannavāro": V(x=f"{UPPAJJAMANA_N} và {UPPANNA_N}"),
    "Nirujjhamānuppannavāro": V(x=f"{NIRUJJHAMANA_N} và {UPPANNA_N}"),
    "Uppannuppādavāro": V(x=f"{UPPANNA_N} và {UPP_N}"),
    "Atītānāgatavāro": S.SECTION["Atītānāgatavāro"],
    "Uppannuppajjamānavāro": V(x=f"{UPPANNA_N} và {UPPAJJAMANA_N}"),
    "Niruddhanirujjhamānavāro": V(x=f"{NIRUDDHA_N} và {NIRUJJHAMANA_N}"),
    "Atikkantakālavāro": V(x="thời đã qua"),
}
GREAT_SECTION = {"Puggalavāro": V(x="người"), "Dhammavāro": V(x="hiện tượng"),
                 "Puggaladhammavāro": V(x="người và hiện tượng")}
MISSAKA = "Trường hợp đặc biệt kết hợp với các loại tâm {x}"   # <X>cittamissakaviseso
HEAD = {
    "Cittayamakaṃ": S.YAMAKA["Cittayamakaṃ"],
    "(Ka) uddeso": S.EXACT["(Ka) uddeso"],
    "(Kha) niddeso": S.EXACT["(Kha) niddeso"],
    "Suddhacittasāmaññaṃ": SUDDHA, "Suddhacittasāmañña": SUDDHA,
    "Suttantacittamissakaviseso": MISSAKA.format(x="theo kinh"),                 # suttanta «theo kinh» pi-1 / pi-2
    "Abhidhammacittamissakaviseso": MISSAKA.format(x="theo Vi Diệu Pháp"),       # «theo Vi Diệu Pháp» pi-2
}
HEAD.update(GREAT_SECTION)
for _p, _v in TIME_SECTION.items():
    HEAD[_p] = _v


def heading(t):
    if t in HEAD:
        return HEAD[t]
    m = re.fullmatch(r"\((?P<n>\d+)\) (?P<w>\S+)", t)
    if m and m["w"] in TIME_SECTION:
        return f"({m['n']}) {TIME_SECTION[m['w']]}"
    raise ValueError(f"unmatched heading {t!r}")


# ================================================================ exact lines (uddesa mixtures, editorial notes, end)
def p_open(kind):
    return WHO["P"][0].format(k=citta(kind))        # tâm có tham đắm của người nào


SARANA_ARANA = f"các loại {KIND['saraṇaṃ']} và {KIND['araṇaṃ']}"   # saraṇaaraṇā (pi-1 «có xung đột» / «không có …»)
EXACT_LINE = {
    # ^6-8-61
    ("Yassa sarāgaṃ cittaṃ uppajjati…pe… yassa vītarāgaṃ cittaṃ uppajjati… yassa sadosaṃ cittaṃ uppajjati… "
     "yassa vītadosaṃ cittaṃ uppajjati… yassa samohaṃ cittaṃ uppajjati… yassa vītamohaṃ cittaṃ uppajjati … "
     "yassa saṃkhittaṃ cittaṃ uppajjati… yassa vikkhittaṃ cittaṃ uppajjati… yassa mahaggataṃ cittaṃ uppajjati… "
     "yassa amahaggataṃ cittaṃ uppajjati… yassa sauttaraṃ cittaṃ uppajjati… yassa anuttaraṃ cittaṃ uppajjati… "
     "yassa samāhitaṃ cittaṃ uppajjati… yassa asamāhitaṃ cittaṃ uppajjati… yassa vimuttaṃ cittaṃ uppajjati… "
     "yassa avimuttaṃ cittaṃ uppajjati…?"):
        cap(f"{PE} ".join(f"{p_open(k)} {VERB['uppajjati']}" for k in SUTTANTA_KINDS)) + f"{PE}?",
    # ^6-8-62
    ("Yassa kusalaṃ cittaṃ uppajjati…pe… yassa akusalaṃ cittaṃ uppajjati… yassa abyākataṃ cittaṃ uppajjati… "
     "yassa sukhāya vedanāya sampayuttaṃ cittaṃ uppajjati…?"):
        cap(f"{PE} ".join(f"{p_open(k)} {VERB['uppajjati']}" for k in ABHIDHAMMA_KINDS)) + f"{PE}?",
    "(Etena upāyena yāva saraṇaaraṇā uddharitabbā.)": f"(Theo cách này, cần trình bày cho đến {SARANA_ARANA}.)",
    # ^6-8-113
    "(Yassa cittake sakabhāvena niddiṭṭhe, yaṃ cittake ca yassa yaṃ cittake ca ekattena niddiṭṭhe.)":
        (f"(Phần về tâm {for_('người nào')} được giải thích theo cách riêng của nó, phần về "
         f"{WHO['D'][0].format(k='tâm')} và phần về {WHO['D'][0].format(k='tâm')} {for_('người nào')} "
         f"được giải thích chung làm một.)"),
    # ^6-8-115
    "Yassa vā pana…pe…? Āmantā …pe….": f"{KHA_PREFIX}{for_('người nào')}{PE}? {S.AMANTA[:-1]}{PE}",
    # ^6-8-116
    "Yassa akusalaṃ cittaṃ uppajjati na nirujjhati…pe…. Yassa abyākataṃ cittaṃ uppajjati na nirujjhati…pe….":
        " ".join(cap(f"{p_open(k)} {phrase('uppajjati na nirujjhati')}{PE}") for k in ("akusalaṃ", "abyākataṃ")),
    "(Mūlayamakaṃ cittayamakaṃ dhammayamakanti tīṇi yamakāni yāva saraṇaaraṇā gacchanti.)":
        (f"(Ba phần, {low(S.YAMAKA['Mūlayamakaṃ'])}, {low(S.YAMAKA['Cittayamakaṃ'])} và "
         f"{low(S.YAMAKA['Dhammayamakaṃ'])}, đều đi cho đến {SARANA_ARANA}.)"),
    "Cittayamakaṃ niṭṭhitaṃ.": S.yamaka_end("Cittayamakaṃ"),
    # ^6-8-82: a plain line in the Pāli (no #####), kept plain
    "(14) Atikkantakālavāro": f"(14) {TIME_SECTION['Atikkantakālavāro']}",
}


# ================================================================ line translation
def translate_sentence(s):
    if s in EXACT_SENT:
        return EXACT_SENT[s]
    if s.endswith("?"):
        v = translate_question(s)
    else:
        v = translate_answer(s)
    if v is None:
        raise ValueError(f"unmatched sentence: {s!r}")
    return v


def translate_line(line):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in EXACT_LINE:
        return EXACT_LINE[t] + sid
    sents = re.split(r"(?<=[?.])\s+(?=\S)", t)
    return " ".join(translate_sentence(s) for s in sents) + sid


def translate_file(name=CH):
    src = (S.PALI_DIR / name).read_text(encoding="utf-8")
    out = [translate_line(line) if line.strip() else "" for line in src.splitlines()]
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ cross-book asserts (this chapter)
CROSS_BOOK_8 = [
    ("sinh khởi", 5), ("chấm dứt", 5), ("sẽ sinh khởi", 5), ("sẽ không sinh khởi", 5), ("đã chấm dứt", 5),
    ("đã sinh khởi", 5), ("đang được giải thoát", 5), ("khoảnh khắc sinh khởi", 5), ("khoảnh khắc tan rã", 5),
    ("thành tựu thiền chấm dứt", 5), ("các chúng sinh Vô Tưởng", 5), ("người có được", 5), ("Không có.", 3),
    ("Tâm có tham đắm", 2), ("Tâm đã lìa tham đắm", 2), ("Tâm có sân hận", 2), ("Tâm đã lìa sân hận", 2),
    ("Tâm có si mê", 2), ("Tâm đã lìa si mê", 2), ("Tâm co rút", 2), ("Tâm tán loạn", 2), ("Tâm rộng lớn", 2),
    ("Tâm không rộng lớn", 2), ("Tâm còn có điều cao hơn", 2), ("Tâm không có điều gì cao hơn", 2),
    ("Tâm được định tâm", 2), ("Tâm không được định tâm", 2), ("Tâm được giải thoát", 2),
    ("Tâm không được giải thoát", 2), ("tâm có tham đắm", 5),
    ("tâm thiện", 1), ("tâm bất thiện", 1), ("tâm không xác định về mặt đạo đức", 1),
    ("Các hiện tượng gắn liền với cảm giác dễ chịu", 1), ("Các hiện tượng có xung đột", 1),
    ("Các hiện tượng không có xung đột", 1), ("Các hiện tượng thuộc quá khứ", 1),
    ("Các hiện tượng thuộc tương lai", 1), ("Các hiện tượng thuộc hiện tại", 1),
    ("Ma trận bộ đôi theo kinh", 1), ("Phân tích theo kinh", 2), ("Phân tích theo Vi Diệu Pháp", 2),
    ("thuần túy", 5), ("người", 5), ("hiện tượng", 1),
]


def check_cross_book_8():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK_8 if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"chapter 8 cross-book asserts: {len(CROSS_BOOK_8)} strings found in pi-1..5 rails")


def check_distinct():
    """the ten tense / aspect forms and their negations must all differ"""
    vals = list(VERB.values()) + list(NEGVERB.values())
    assert len(set(vals)) == len(vals), "tense forms not distinct"


def main():
    S.check_cross_book()
    check_cross_book_8()
    check_distinct()
    text = unicodedata.normalize("NFC", translate_file(CH))
    probs = S.check_lines((S.PALI_DIR / CH).read_text(encoding="utf-8"), text, CH)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    if probs:
        sys.exit(1)
    with open(S.OUT_DIR / CH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {CH}: {len([l for l in text.splitlines() if l.strip()])} lines, {segs} segments")


if __name__ == "__main__":
    main()
