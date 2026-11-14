"""Builder for the Russian rails translation of pi-1 (Dhammasaṅgaṇī, plain audience), chapters 3-02 and 3-03
(Rūpavibhatti: the exposition of the pairs ^1-595 … ^1-743, of the triads ^1-744 … ^1-881 and the fours …
elevens ^1-882 … ^1-984: «Katamaṃ taṃ rūpaṃ …?» definitions of the sense bases, objects and other matter).

Writes (only when run as a script):
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/3-02-rupakandam.md
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/3-03-rupakandam.md
  0-INBOX/temp/pipeline/pi-1-ru/rails/notes-3-02_3-03.md

Every line is translated from the Pāli by fixed strings. The earlier rails builders are imported, never edited:
build_rails_sample_ru.py (S: frames, the synonym strings S_LAHUTA, S_MUDUTA, S_KAMMANNATA, S_JIVITA, headings)
and build_rails_3-01_ru.py (T: the material-form tables NOUN, ADJ, GEN, forms(), the counted headings and
closing lines), so every item 3-01 names reads the same here.
The sense-base and object definitions are rebuilt in Pāli from the same tables that give the Russian and looked
up by exact match; every list and predicate is tokenized against known Pāli; unknown Pāli raises an error.
Terms follow the locked termbase AI_translation/russian/pi-1-pali-russian-termbase-plain.md.

usage: python -I -X utf8 build_rails_3-02_3-03_ru.py
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)

_spec = importlib.util.spec_from_file_location("build_rails_3_01_ru", HERE / "build_rails_3-01_ru.py")
T = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T)        # importing writes nothing

PARTS = ["3-02-rupakandam.md", "3-03-rupakandam.md"]
cap = S.cap
PE, ELL = "…pe…", "…"
RUPA = T.RUPA                                      # материальная форма
ARE = ", – "                                       # «…, – это X.» (S.definition, T.UDDESO_R)

# =========================================================================================
# 1. Names of the classification predicates («Katamaṃ taṃ rūpaṃ X?» = «Что такое <name>?»)
#    pre:  a plain adjective, placed before «материальная форма»
#    post: a participial phrase after «материальная форма, …»
# =========================================================================================
PRE = {}
POST = {}
for _p, (_a, _pred, _ins) in T.ADJ.items():
    if _a.startswith(", "):
        POST[_p] = _a[2:]
    else:
        PRE[_p] = _a.strip()
POST["dūre"] = "находящаяся " + PRE.pop("dūre")          # вдали (3-01: «находится вдали»)
POST["santike"] = "находящаяся " + PRE.pop("santike")    # вблизи
assert T.ADJ["dūre"][1] == "находится вдали" and T.ADJ["santike"][1] == "находится вблизи"
POST["dhammāyatanapariyāpannaṃ"] = "принадлежащая" + T.DHAMMAYATANA[len("принадлежит"):]
assert POST["dhammāyatanapariyāpannaṃ"] == "принадлежащая к сфере объектов ума"

ITEM = {}                                          # pali item (lower case) -> nominative
for _k, (_n, _i) in T.NOUN.items():
    _kk = _k[0].lower() + _k[1:]
    ITEM[_kk] = _n
    _neg = ("rūpassa na " + _kk[len("rūpassa "):]) if _kk.startswith("rūpassa ") else "na " + _kk
    POST[_kk] = T.forms(_k)["attr"][2:]            # являющаяся X-instr.
    POST[_neg] = T.forms(_neg if not _k[0].isupper() else "na " + _k)["attr"][2:]
INS = {}                                           # pali noun -> instrumental (for …pe… chains)
for _k, (_n, _i) in T.NOUN.items():
    INS[_k[0].lower() + _k[1:]] = _i

# genitive chains before vatthu / ārammaṇaṃ (3-01 GEN)
GEN = dict(T.GEN)
REL = {"vatthu": T.HEADS["vatthu"][1], "ārammaṇaṃ": T.HEADS["ārammaṇaṃ"][1]}   # основой / объектом
COMPOSITE = {}
for _g in GEN:
    for _r in REL:
        for _neg in (False, True):
            COMPOSITE[f"{_g} {'na ' if _neg else ''}{_r}"] = (_g, _neg, _r)

VOCAB = set(PRE) | set(POST) | set(GEN) | set(COMPOSITE)
MAXW = max(len(k.split()) for k in VOCAB)


def tokenize(text, vocab, maxw):
    words, out, i = text.split(), [], 0
    while i < len(words):
        for n in range(min(maxw, len(words) - i), 0, -1):
            cand = " ".join(words[i:i + n])
            if cand in vocab:
                out.append(cand)
                i += n
                break
        else:
            raise KeyError(f"unknown Pāli at {words[i:]!r} in {text!r}")
    return out


def chain_phrase(chain):
    """A …pe… chain: genitives before one vatthu / ārammaṇaṃ composite, or a run of nouns."""
    if chain[-1] in COMPOSITE:
        g, neg, r = COMPOSITE[chain[-1]]
        assert all(c in GEN for c in chain[:-1]), chain
        gens = [GEN[c] for c in chain[:-1]] + [GEN[g]]
        return f"{'не ' if neg else ''}являющаяся {REL[r]} " + f"{ELL} ".join(gens)
    first = POST[chain[0]]
    rest = []
    for c in chain[1:]:
        neg = c.startswith("na ")
        rest.append(("не " if neg else "") + INS[c[3:] if neg else c])
    return first + "".join(f"{ELL} {x}" for x in rest)


def join_post(ph):
    if len(ph) == 1:
        return ph[0]
    if any(" и " in x or ", но " in x for x in ph):
        return ", ".join(ph)
    return ", ".join(ph[:-1]) + " и " + ph[-1]


def name_ru(pred):
    """Pāli predicate(s) of «Katamaṃ taṃ rūpaṃ …» -> Russian name «… материальная форма, …»."""
    pieces = [x.strip() for x in pred.split(PE)]
    toks = tokenize(pieces[0], VOCAB, MAXW)
    others = [tokenize(p, VOCAB, MAXW) for p in pieces[1:]]
    assert all(len(o) == 1 for o in others), pred
    if others:
        prefix, chain = toks[:-1], [toks[-1]] + [o[0] for o in others]
    elif toks[-1] in COMPOSITE:
        prefix, chain = toks[:-1], [toks[-1]]
    else:
        prefix, chain = toks, []
    pre = [PRE[t] for t in prefix if t in PRE]
    post = [POST[t] for t in prefix if t not in PRE]
    if chain:
        post.append(chain_phrase(chain))
    base = " ".join(pre + [RUPA])
    return base + (", " + join_post(post) if post else "")


# =========================================================================================
# 2. Item lists of the answers
# =========================================================================================
CLAUSE = "yaṃ vā panaññampi atthi rūpaṃ"
OTHER = f"или же какая бы другая {RUPA} ни была"          # cf. S.OTHERS «какие бы другие … ни были»
KAMMA = "вследствие совершённых действий"                 # kammassa katattā (termbase)
QUALS = {
    "kammassa katattā": KAMMA,
    "na kammassa katattā": "не " + KAMMA,
    "cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ": "рождённой умом, имеющей причиной ум, порождённой умом",
    "na cittajaṃ na cittahetukaṃ na cittasamuṭṭhānaṃ":
        "не рождённой умом, не имеющей причиной ум, не порождённой умом",
}
LEADS = {"kammassa katattā", "na kammassa katattā"}
LVOCAB = set(ITEM) | {CLAUSE} | set(QUALS)


def list_ru(a):
    a = a[0].lower() + a[1:]
    a = a.replace(PE, f" {PE} ").replace(",", " , ")
    words = a.split()
    toks, i = [], 0
    while i < len(words):
        if words[i] in (",", PE):
            toks.append(words[i])
            i += 1
            continue
        for n in range(min(6, len(words) - i), 0, -1):
            cand = " ".join(words[i:i + n])
            if cand in LVOCAB:
                toks.append(cand)
                i += n
                break
        else:
            raise KeyError(f"unknown list item at {words[i:]!r} in {a!r}")
    out, prev, j = "", None, 0
    while j < len(toks):
        t = toks[j]
        if t == ",":
            j += 1
            continue
        if t == PE:
            out += ELL
            prev = "pe"
            j += 1
            continue
        if t == CLAUSE:
            q = toks[j + 1]
            out += f", {OTHER} {QUALS[q]}:"
            prev = "colon"
            j += 2
            continue
        if t in LEADS and prev is None:
            out += QUALS[t] + ":"
            prev = "colon"
            j += 1
            continue
        if prev == "item":
            out += ", "
        elif prev in ("pe", "colon"):
            out += " "
        out += ITEM[t]
        prev = "item"
        j += 1
    return cap(out)


# =========================================================================================
# 3. The definitions of the sense organs and their objects (rebuilt in Pāli, looked up exactly)
# =========================================================================================
SANKH = "способн{} к соударению"
IA = {"m": "невидимый и способный к соударению", "n": "невидимое и способное к соударению",
      "f": "невидимая и способная к соударению"}
IA_INS = "невидимым и способным к соударению"                       # m. / n. instrumental
VA = {"nom": "видимая и способная к соударению", "acc": "видимую и способную к соударению"}
MAHA = "производн{} от четырёх великих элементов"                   # catunnaṃ mahābhūtānaṃ upādāya
SENS = (f"является чувствительностью, {MAHA.format('ой')}, принадлежащей к индивидуальному бытию, "
        "невидимой и способной к соударению")                        # pasādo attabhāvapariyāpanno …


def strike(g):   # paṭihaññi vā paṭihaññati vā paṭihaññissati vā paṭihaññe vā
    past = {"m": "ударялся", "f": "ударялась", "n": "ударялось"}[g]
    opt = {"m": "мог", "f": "могла", "n": "могло"}[g]
    return f"{past}, ударяется, ударится или {opt} бы удариться"


def arise(g):    # uppajji vā uppajjati vā uppajjissati vā uppajje vā
    past = {"m": "возникал", "f": "возникала", "n": "возникало"}[g]
    opt = {"m": "мог", "f": "могла", "n": "могло"}[g]
    return f"{past}, возникает, возникнет или {opt} бы возникнуть"


P_STRIKE = "paṭihaññi vā paṭihaññati vā paṭihaññissati vā paṭihaññe vā"
P_ARISE = "uppajji vā uppajjati vā uppajjissati vā uppajje vā"
NAMES_P = ("loko peso dvārā pesā samuddo peso paṇḍaraṃ petaṃ khettaṃ petaṃ vatthuṃ petaṃ {extra}"
           "orimaṃ tīraṃ petaṃ suñño gāmo peso")
NAMES_R = ("это мир, это врата, это океан, это чистота, это поле, это основа, {extra}"
           "это ближний берег, это пустая деревня")
EXTRA_P, EXTRA_R = "nettaṃ petaṃ nayanaṃ petaṃ ", "это проводник, это вожатый, "

# organ: pali forms, russian forms, sense verbs, its object
ORG = {
    "cakkhu": dict(
        rel="Yaṃ", nom="cakkhu", acc="cakkhuṃ", ins="cakkhunā", loc="cakkhumhi", rins="yena", rloc="yamhi",
        rc="yaṃ", adj_ins="anidassanena sappaṭighena", adj_loc="anidassanamhi sappaṭighamhi",
        adj_nom="anidassanaṃ sappaṭighaṃ", self="cakkhuṃ petaṃ", st="cakkhu", ind="cakkhundriyaṃ",
        bnom="cakkhuṃ", verbs="passi vā passati vā passissati vā passe vā", obj="rūpa", vinn="cakkhuviññāṇaṃ",
        r=dict(nom="глаз", gen="глаза", ins="глазом", o="о глаз", g="m", rel="который", rel_o="о который"),
        see=("видели", "видят", "увидят", "могли бы увидеть"), vinn_r="зрительное сознание"),
    "sota": dict(
        rel="Yaṃ", nom="sotaṃ", acc="sotaṃ", ins="sotena", loc="sotamhi", rins="yena", rloc="yamhi",
        rc="yaṃ", adj_ins="anidassanena sappaṭighena", adj_loc="anidassanamhi sappaṭighamhi",
        adj_nom="anidassanaṃ sappaṭighaṃ", self="sotaṃ petaṃ", st="sota", ind="sotindriyaṃ",
        bnom="sotaṃ", verbs="suṇi vā suṇāti vā suṇissati vā suṇe vā", obj="sadda", vinn="sotaviññāṇaṃ",
        r=dict(nom="ухо", gen="уха", ins="ухом", o="об ухо", g="n", rel="которое", rel_o="о которое"),
        see=("слышали", "слышат", "услышат", "могли бы услышать"), vinn_r="слуховое сознание"),
    "ghāna": dict(
        rel="Yaṃ", nom="ghānaṃ", acc="ghānaṃ", ins="ghānena", loc="ghānamhi", rins="yena", rloc="yamhi",
        rc="yaṃ", adj_ins="anidassanena sappaṭighena", adj_loc="anidassanamhi sappaṭighamhi",
        adj_nom="anidassanaṃ sappaṭighaṃ", self="ghānaṃ petaṃ", st="ghāna", ind="ghānindriyaṃ",
        bnom="ghānaṃ", verbs="ghāyi vā ghāyati vā ghāyissati vā ghāye vā", obj="gandha", vinn="ghānaviññāṇaṃ",
        r=dict(nom="нос", gen="носа", ins="носом", o="о нос", g="m", rel="который", rel_o="о который"),
        see=("обоняли", "обоняют", "будут обонять", "могли бы обонять"), vinn_r="обонятельное сознание"),
    "jivhā": dict(
        rel="Yā", nom="jivhā", acc="jivhaṃ", ins="jivhāya", loc="jivhāya", rins="yāya", rloc="yāya",
        rc="yā", adj_ins="anidassanāya sappaṭighāya", adj_loc="anidassanāya sappaṭighāya",
        adj_nom="anidassanā sappaṭighā", self="jivhā pesā", st="jivhā", ind="jivhindriyaṃ",
        bnom="jivhā", verbs="sāyi vā sāyati vā sāyissati vā sāye vā", obj="rasa", vinn="jivhāviññāṇaṃ",
        r=dict(nom="язык", gen="языка", ins="языком", o="о язык", g="m", rel="который", rel_o="о который"),
        see=("вкушали", "вкушают", "вкусят", "могли бы вкусить"), vinn_r="вкусовое сознание"),
    "kāya": dict(
        rel="Yo", nom="kāyo", acc="kāyaṃ", ins="kāyena", loc="kāyamhi", rins="yena", rloc="yamhi",
        rc="yo", adj_ins="anidassanena sappaṭighena", adj_loc="anidassanamhi sappaṭighamhi",
        adj_nom="anidassano sappaṭigho", self="kāyo peso", st="kāya", ind="kāyindriyaṃ",
        bnom="kāyo", verbs="phusi vā phusati vā phusissati vā phuse vā", obj="phoṭṭhabba", vinn="kāyaviññāṇaṃ",
        r=dict(nom="тело", gen="тела", ins="телом", o="о тело", g="n", rel="которое", rel_o="о которое"),
        see=("касались", "касаются", "коснутся", "могли бы коснуться"), vinn_r="осязательное сознание"),
}
for _o in ORG.values():
    assert T.GEN[f"{_o['st']}samphassassa"] == f"контакта {_o['r']['gen']}"

# object: pali forms, russian forms
OBJ = {
    "rūpa": dict(
        rel="yaṃ", nom="rūpaṃ", acc="rūpaṃ", loc="rūpamhi", q_acc="sanidassanaṃ sappaṭighaṃ",
        q_nom="sanidassanaṃ sappaṭighaṃ", q_loc="sanidassanamhi sappaṭighamhi", self="rūpaṃ petaṃ",
        organ="cakkhu",
        r=dict(nom="видимая форма", acc="видимую форму", g="f", q_nom=VA["nom"], q_acc=VA["acc"],
               rel="которая", racc="которую", rins="с которой", rel_o="о которую", o="о видимую форму",
               pl="видимых форм")),
    "sadda": dict(
        rel="yo", nom="saddo", acc="saddaṃ", loc="saddamhi", q_acc="anidassanaṃ sappaṭighaṃ",
        q_nom="anidassano sappaṭigho", q_loc="anidassanamhi sappaṭighamhi", self="saddo peso", organ="sota",
        r=dict(nom="звук", acc="звук", g="m", q_nom=IA["m"], q_acc=IA["m"], rel="который", racc="который",
               rins="с которым", rel_o="о который", o="о звук", pl="звуков")),
    "gandha": dict(
        rel="yo", nom="gandho", acc="gandhaṃ", loc="gandhamhi", q_acc="anidassanaṃ sappaṭighaṃ",
        q_nom="anidassano sappaṭigho", q_loc="anidassanamhi sappaṭighamhi", self="gandho peso", organ="ghāna",
        r=dict(nom="запах", acc="запах", g="m", q_nom=IA["m"], q_acc=IA["m"], rel="который", racc="который",
               rins="с которым", rel_o="о который", o="о запах", pl="запахов")),
    "rasa": dict(
        rel="yo", nom="raso", acc="rasaṃ", loc="rasamhi", q_acc="anidassanaṃ sappaṭighaṃ",
        q_nom="anidassano sappaṭigho", q_loc="anidassanamhi sappaṭighamhi", self="raso peso", organ="jivhā",
        r=dict(nom="вкус", acc="вкус", g="m", q_nom=IA["m"], q_acc=IA["m"], rel="который", racc="который",
               rins="с которым", rel_o="о который", o="о вкус", pl="вкусов")),
    "phoṭṭhabba": dict(
        rel="yo", nom="phoṭṭhabbo", acc="phoṭṭhabbaṃ", loc="phoṭṭhabbamhi", q_acc="anidassanaṃ sappaṭighaṃ",
        q_nom="anidassano sappaṭigho", q_loc="anidassanamhi sappaṭighamhi", self="phoṭṭhabbo peso",
        organ="kāya",
        r=dict(nom="осязаемое", acc="осязаемое", gen="осязаемого", g="n", q_nom=IA["n"], q_acc=IA["n"],
               q_gen="невидимого и способного к соударению", rel="которое", racc="которое", rgen="которого",
               rins="с которым", rel_o="о которое", o="об осязаемое", pl="осязаемого")),
}
for _k, _o in OBJ.items():
    assert T.NOUN[f"{_k}dhātu"][0] == f"элемент {_o['r']['pl']}"


def obj_arg(ob, case):
    """object noun + its quality, as governed by the organ's verb (касаться + gen.)."""
    r = ob["r"]
    if case == "gen":
        return f"{r['gen']}, {r['q_gen']}"
    return f"{r['acc']}, {r['q_acc']}"


def four(v):
    return f"{v[0]}, {v[1]}, {v[2]} или {v[3]}"


def organ_def(key, part, var_p="", var_r=""):
    o = ORG[key]
    ob = OBJ[o["obj"]]
    r, rb = o["r"], ob["r"]
    cont_p = f"{o['st']}samphass"
    cont_r = f"контакт {r['gen']}"
    head_p = f"{o['rel']} {o['nom']}{var_p} catunnaṃ mahābhūtānaṃ upādāya pasādo"
    head_r = f"{cap(r['nom'])}{var_r}, {r['rel']} является чувствительностью, {MAHA.format('ой')}"
    if part == "abbr":
        return f"{head_p}{PE} suñño gāmo peso", f"{head_r}{ELL} это пустая деревня"
    head_p += " attabhāvapariyāpanno anidassano sappaṭigho"
    head_r = f"{cap(r['nom'])}{var_r}, {r['rel']} {SENS}"
    case = "gen" if key == "kāya" else "acc"
    if part == "a":
        q = "anidassanasappaṭighaṃ" if key == "kāya" else ob["q_acc"]
        mid_p = f"{o['rins']} {o['ins']} {o['adj_ins']} {ob['acc']} {q} {o['verbs']}"
        mid_r = f"{r['nom']}, {IA[r['g']]}, которым {four(o['see'])} {obj_arg(ob, case)}"
    elif part == "b":
        mid_p = f"{o['rloc']} {o['loc']} {o['adj_loc']} {ob['nom']} {ob['q_nom']} {P_STRIKE}"
        mid_r = f"{r['nom']}, {IA[r['g']]}, {r['rel_o']} {strike(rb['g'])} {rb['nom']}, {rb['q_nom']}"
    elif part == "c":
        mid_p = f"{o['rc']} {o['nom']} {o['adj_nom']} {ob['loc']} {ob['q_loc']} {P_STRIKE}"
        mid_r = f"{r['nom']}, {IA[r['g']]}, {r['rel']} {strike(r['g'])} {rb['o']}, {rb['q_acc']}"
    elif part == "d":
        am = f"{o['obj'][:-1]}ārammaṇ"
        b1 = f"yaṃ {o['acc']} nissāya"
        mid_p = (f"{b1} {ob['acc']} ārabbha {cont_p}o {P_ARISE}{PE} "
                 f"{b1} {ob['acc']} ārabbha {cont_p}ajā vedanā{PE} saññā{PE} cetanā{PE} {o['vinn']} {P_ARISE}{PE} "
                 f"{b1} {am}o {cont_p}o {P_ARISE}{PE} "
                 f"{b1} {am}ā {cont_p}ajā vedanā{PE} saññā{PE} cetanā{PE} {o['vinn']} {P_ARISE}")
        b1r = f"{r['nom']}, в зависимости от которого"
        feel = f"рождённое контактом {r['gen']} чувство{ELL} восприятие{ELL} намерение{ELL} {o['vinn_r']}"
        mid_r = (f"{b1r}, имея объектом {rb['acc']}, {cont_r} {arise('m')}{ELL} "
                 f"{b1r}, имея объектом {rb['acc']}, {feel} {arise('n')}{ELL} "
                 f"{b1r} имеющий объектом {rb['acc']} {cont_r} {arise('m')}{ELL} "
                 f"{b1r} имеющее объектом {rb['acc']} {feel} {arise('n')}")
    else:
        raise KeyError(part)
    names_p = (f"{o['self']} {o['st'][:-1] if o['st'] != 'jivhā' else 'jivh'}āyatanaṃ petaṃ {o['st']}dhātu pesā "
               f"{o['ind']} petaṃ " + NAMES_P.format(extra=EXTRA_P if key == "cakkhu" else ""))
    names_r = (f"это {r['nom']}, это сфера {r['gen']}, это элемент {r['gen']}, это способность {r['gen']}, "
               + NAMES_R.format(extra=EXTRA_R if key == "cakkhu" else ""))
    assert T.NOUN[o["ind"]][0] == f"способность {r['gen']}"
    return f"{head_p}, {mid_p}, {names_p}", f"{head_r}; {mid_r}; {names_r}"


# the lists of the object definitions: (pali, russian)
COLOURS = [("nīlaṃ", "синее"), ("pītakaṃ", "жёлтое"), ("lohitakaṃ", "красное"), ("odātaṃ", "белое"),
           ("kāḷakaṃ", "чёрное"), ("mañjiṭṭhakaṃ{v1}", "малиновое{v1}"), ("hari", "зелёное"),
           ("harivaṇṇaṃ", "зеленоватое"), ("ambaṅkuravaṇṇaṃ", "цвета побегов манго"), ("dīghaṃ", "длинное"),
           ("rassaṃ", "короткое"), ("aṇuṃ", "мелкое"), ("thūlaṃ", "крупное"), ("vaṭṭaṃ", "округлое"),
           ("parimaṇḍalaṃ", "круглое"), ("caturaṃsaṃ{v2}", "четырёхугольное{v2}"), ("chaḷaṃsaṃ", "шестиугольное"),
           ("aṭṭhaṃsaṃ", "восьмиугольное"), ("soḷasaṃsaṃ", "шестнадцатиугольное"), ("ninnaṃ", "низина"),
           ("thalaṃ", "возвышенность"), ("chāyā", "тень"), ("ātapo", "солнечный свет"), ("āloko", "свет"),
           ("andhakāro", "тьма"), ("abbhā", "облака"), ("mahikā", "туман"), ("dhūmo", "дым"), ("rajo", "пыль"),
           ("candamaṇḍalassa vaṇṇanibhā", "цвет и облик лунного диска"),
           ("sūriyamaṇḍalassa{v3} vaṇṇanibhā", "цвет и облик солнечного диска{v3}"),
           ("tārakarūpānaṃ vaṇṇanibhā", "цвет и облик звёзд"),
           ("ādāsamaṇḍalassa vaṇṇanibhā", "цвет и облик зеркального диска"),
           ("maṇisaṅkhamuttāveḷuriyassa vaṇṇanibhā", "цвет и облик драгоценных камней, раковин, жемчуга и берилла"),
           ("jātarūparajatassa vaṇṇanibhā", "цвет и облик золота и серебра")]
COL_VAR_P = {"v1": " [mañjeṭṭhakaṃ (sī. syā.)]", "v2": " [caturassaṃ (sī. ka.)]",
             "v3": " [suriyamaṇḍalassa (sī. syā.)]"}
COL_VAR_R = {"v1": " " + S.spell("Sī., Syā.", "mañjeṭṭhakaṃ"), "v2": " " + S.spell("Sī., Ka.", "caturassaṃ"),
             "v3": " " + S.spell("Sī., Syā.", "suriyamaṇḍalassa")}
SOUNDS = [("bherisaddo", "звук больших барабанов"), ("mudiṅgasaddo", "звук малых барабанов"),
          ("saṅkhasaddo", "звук раковин"), ("paṇavasaddo", "звук бубнов"), ("gītasaddo", "звук пения"),
          ("vāditasaddo", "звук музыкальных инструментов"), ("sammasaddo", "звук тарелок"),
          ("pāṇisaddo", "звук хлопков в ладоши"), ("sattānaṃ nigghosasaddo", "звук голосов существ"),
          ("dhātūnaṃ sannighātasaddo", "звук соударения предметов"), ("vātasaddo", "звук ветра"),
          ("udakasaddo", "звук воды"), ("manussasaddo", "звук людей"),
          ("amanussasaddo", "звук нечеловеческих существ")]
SMELLS = [("mūlagandho", "запах корней"), ("sāragandho", "запах сердцевины дерева"), ("tacagandho", "запах коры"),
          ("pattagandho", "запах листьев"), ("pupphagandho", "запах цветов"), ("phalagandho", "запах плодов"),
          ("āmakagandho", "запах сырого мяса"), ("vissagandho", "запах гнили"), ("sugandho", "приятный запах"),
          ("duggandho", "неприятный запах")]
TASTES = [("mūlaraso", "вкус корней"), ("khandharaso", "вкус стеблей"), ("tacaraso", "вкус коры"),
          ("pattaraso", "вкус листьев"), ("puppharaso", "вкус цветов"), ("phalaraso", "вкус плодов"),
          ("ambilaṃ", "кислый"), ("madhuraṃ", "сладкий"), ("tittakaṃ", "горький"), ("kaṭukaṃ", "острый"),
          ("loṇikaṃ", "солёный"), ("khārikaṃ", "щелочной"), ("lambilaṃ{v1}", "кисловатый{v1}"),
          ("kasāvo", "вяжущий"), ("sādu", "вкусный"), ("asādu", "невкусный")]
TASTE_VAR_P, TASTE_VAR_R = {"v1": " [lapilakaṃ (sī.)]"}, {"v1": " " + S.reading("Sī.", "lapilakaṃ")}
TOUCH = [("Pathavīdhātu", T.NOUN["Pathavīdhātu"][0]), ("tejodhātu", T.NOUN["tejodhātu"][0]),
         ("vāyodhātu", T.NOUN["vāyodhātu"][0]), ("kakkhaḷaṃ", "твёрдое"), ("mudukaṃ", "мягкое"),
         ("saṇhaṃ", "гладкое"), ("pharusaṃ", "шероховатое"),
         ("sukhasamphassaṃ", "доставляющее удовольствие при контакте"),
         ("dukkhasamphassaṃ", "болезненное при контакте"), ("garukaṃ", "тяжёлое"), ("lahukaṃ", "лёгкое")]
assert T.SUKHA_DUKKHA_R.endswith("бывает доставляющей удовольствие при контакте, бывает болезненной при контакте")


def plist(lst, var_p=None, var_r=None, sep_p=" "):
    vp = var_p or {}
    vr = var_r or {}
    blank = {k: "" for k in ("v1", "v2", "v3")}
    p = sep_p.join(x for x, _ in lst).format(**{**blank, **vp})
    r = ", ".join(y for _, y in lst).format(**{**blank, **vr})
    return p, r


def object_head(key, variants):
    ob = OBJ[key]
    r = ob["r"]
    if key == "rūpa":
        col_p, col_r = plist(COLOURS, COL_VAR_P if variants else None, COL_VAR_R if variants else None)
        q_p = "catunnaṃ mahābhūtānaṃ upādāya vaṇṇanibhā sanidassanaṃ sappaṭighaṃ"
        q_r = f"цветом и обликом, {MAHA.format('ыми')}, видимыми и способными к соударению"
        p = f"Yaṃ rūpaṃ {q_p} {col_p}, yaṃ vā panaññampi atthi rūpaṃ {q_p}, "
        rr = (f"{cap(r['nom'])}, которая является {q_r}: {col_r}, или же какая бы другая {r['nom']} ни была "
              f"{q_r}")
        return p, rr
    if key == "phoṭṭhabba":
        p, rr = plist(TOUCH)
        return p + ", ", cap(rr)
    lst = {"sadda": SOUNDS, "gandha": SMELLS, "rasa": TASTES}[key]
    l_p, l_r = plist(lst, TASTE_VAR_P if (variants and key == "rasa") else None,
                     TASTE_VAR_R if (variants and key == "rasa") else None)
    q_p = "catunnaṃ mahābhūtānaṃ upādāya anidassano sappaṭigho"
    p = f"Yo {ob['nom']} {q_p} {l_p}, yo vā panaññopi atthi {ob['nom']} {q_p}, "
    rr = (f"{cap(r['nom'])}, {MAHA.format('ый')}, {IA['m']}: {l_r}, или же какой бы другой {r['nom']} ни был "
          f"{MAHA.format('ым')}, {IA_INS}")
    return p, rr


def object_def(key, part, variants=False):
    ob = OBJ[key]
    r = ob["r"]
    o = ORG[ob["organ"]]
    ro = o["r"]
    cont_p = f"{o['st']}samphass"
    cont_r = f"контакт {ro['gen']}"
    names_p = (f"{ob['self']} {key[:-1] if key != 'phoṭṭhabba' else 'phoṭṭhabb'}āyatanaṃ petaṃ {key}dhātu pesā"
               if key != "rūpa" else "rūpaṃ petaṃ rūpāyatanaṃ petaṃ rūpadhātu pesā")
    names_r = f"это {r['nom']}, это сфера {r['pl']}, это элемент {r['pl']}"
    if part == "abbr":
        if key == "rūpa":
            return ("Yaṃ rūpaṃ catunnaṃ mahābhūtānaṃ upādāya vaṇṇanibhā" + PE + " rūpadhātu pesā",
                    f"{cap(r['nom'])}, которая является цветом и обликом, {MAHA.format('ыми')}{ELL} "
                    f"это элемент {r['pl']}")
        assert key == "phoṭṭhabba"
        return f"Pathavīdhātu{PE} phoṭṭhabbadhātu pesā", f"{T.NOUN['Pathavīdhātu'][0].capitalize()}{ELL} это элемент {r['pl']}"
    head_p, head_r = object_head(key, variants)
    if part == "a":
        mid_p = f"yaṃ {ob['acc']} {ob['q_acc']} {o['ins']} {o['adj_ins']} {o['verbs']}"
        rel = r["rgen"] if key == "phoṭṭhabba" else r["racc"]
        mid_r = f"{r['nom']}, {r['q_nom']}, {rel} {four(o['see'])} {ro['ins']}, {IA_INS}"
    elif part == "b":
        mid_p = f"yamhi {ob['loc']} {ob['q_loc']} {o['bnom']} {o['adj_nom']} {P_STRIKE}"
        mid_r = f"{r['nom']}, {r['q_nom']}, {r['rel_o']} {strike(ro['g'])} {ro['nom']}, {IA[ro['g']]}"
    elif part == "c":
        mid_p = f"{ob['rel']} {ob['nom']} {ob['q_nom']} {o['loc']} {o['adj_loc']} {P_STRIKE}"
        mid_r = f"{r['nom']}, {r['q_nom']}, {r['rel']} {strike(r['g'])} {ro['o']}, {IA[ro['g']]}"
    elif part == "d":
        am = f"{key[:-1]}ārammaṇ"
        b2 = f"{o['acc']} nissāya"
        mid_p = (f"yaṃ {ob['acc']} ārabbha {b2} {cont_p}o {P_ARISE}{PE} "
                 f"yaṃ {ob['acc']} ārabbha {b2} {cont_p}ajā vedanā{PE} saññā{PE} cetanā{PE} {o['vinn']} {P_ARISE}{PE} "
                 f"yaṃ {am}o {b2} {cont_p}o {P_ARISE}{PE} "
                 f"yaṃ {am}ā {b2} {cont_p}ajā vedanā{PE} saññā{PE} cetanā{PE} {o['vinn']} {P_ARISE}")
        dep = f"в зависимости от {ro['gen']}"
        feel = f"рождённое контактом {ro['gen']} чувство{ELL} восприятие{ELL} намерение{ELL} {o['vinn_r']}"
        b1 = f"{r['nom']}, имея {r['racc']} объектом, {dep}"
        b3 = f"{r['nom']}, {r['rins']} как с объектом {dep}"
        mid_r = (f"{b1} {cont_r} {arise('m')}{ELL} {b1} {feel} {arise('n')}{ELL} "
                 f"{b3} {cont_r} {arise('m')}{ELL} {b3} {feel} {arise('n')}")
    else:
        raise KeyError(part)
    return f"{head_p}{mid_p}, {names_p}", f"{head_r}; {mid_r}; {names_r}"


# =========================================================================================
# 4. Short definitions (exact Pāli -> Russian)
# =========================================================================================
S_JIVITA_PLAIN = S.S_JIVITA.replace(" " + S.spell("Sī.", "irīyanā"), "")     # as build_rails_2-01_2-02_ru.py
assert "[" not in S_JIVITA_PLAIN
MINDS = "при благом уме, или при неблагом уме, или при этически неопределённом уме"
INTIM = "внешнее выражение, оповещение, состояние оповещённости"            # viññatti viññāpanā viññāpitattaṃ
SPEECH = "речь, слово, способ речи, произнесение, голос, звучание голоса, речь, членораздельная речь"
OWN = ", будь то внутри себя или вовне, охваченное цеплянием или не охваченное цеплянием"
ITTHI = ("То, что у женщины есть женская внешность, женский признак, женское поведение, женская манера, "
         "женственность, женское свойство")
SHORT = {
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo": ITTHI,
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo "
    "[itthittaṃ itthībhāvo (syā.)]": ITTHI + " " + S.spell("Syā.", "itthittaṃ itthībhāvo"),
    "Yaṃ purisassa purisaliṅgaṃ purisanimittaṃ purisakuttaṃ purisākappo purisattaṃ purisabhāvo":
        "То, что у мужчины есть мужская внешность, мужской признак, мужское поведение, мужская манера, "
        "мужественность, мужское свойство",
    "Yo tesaṃ rūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ":
        f"То, что у этих материальных явлений есть {S_JIVITA_PLAIN}",
    "Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā abhikkamantassa vā paṭikkamantassa vā "
    "ālokentassa vā vilokentassa vā samiñjentassa vā pasārentassa vā kāyassa thambhanā santhambhanā "
    "santhambhitattaṃ viññatti viññāpanā viññāpitattaṃ":
        f"То, что {MINDS} у идущего вперёд, или идущего назад, или смотрящего прямо, или смотрящего по сторонам, "
        f"или сгибающего, или разгибающего есть напряжённость тела, полная напряжённость, "
        f"состояние полной напряжённости, {INTIM}",
    "Yo ākāso ākāsagataṃ aghaṃ aghagataṃ vivaro vivaragataṃ asamphuṭṭhaṃ catūhi mahābhūtehi":
        "То, что есть пространство, считающееся пространством, незаполненное, считающееся незаполненным, просвет, "
        "считающееся просветом, не затронутое четырьмя великими элементами",
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa":
        "То, что есть вода, считающееся водой, влага, считающееся влагой, связующее свойство материальной формы",
    "Yā rūpassa lahutā lahupariṇāmatā adandhanatā avitthanatā": f"То, что у материальной формы есть {S.S_LAHUTA}",
    "Yā rūpassa mudutā maddavatā akakkhaḷatā akathinatā": f"То, что у материальной формы есть {S.S_MUDUTA}",
    "Yā rūpassa kammaññatā kammaññattaṃ kammaññabhāvo": f"То, что у материальной формы есть {S.S_KAMMANNATA}",
    "Yo āyatanānaṃ ācayo, so rūpassa upacayo":
        "То, что есть накопление сфер восприятия, является ростом материальной формы",
    "Yo rūpassa upacayo, sā rūpassa santati":
        "То, что есть рост материальной формы, является непрерывностью материальной формы",
    "Yā rūpassa jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni indriyānaṃ paripāko":
        "То, что у материальной формы есть старение, одряхление, сломанные зубы, седые волосы, морщинистая кожа, "
        "сокращение срока жизни, изношенность способностей",
    "Yo rūpassa khayo vayo bhedo paribhedo aniccatā antaradhānaṃ":
        "То, что у материальной формы есть уничтожение, угасание, распад, полный распад, непостоянство, исчезновение",
    "Yaṃ kakkhaḷaṃ kharagataṃ [kharigataṃ (ka.)] kakkhaḷattaṃ kakkhaḷabhāvo ajjhattaṃ vā bahiddhā vā "
    "upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        f"То, что есть твёрдое, считающееся жёстким {S.spell('Ka.', 'kharigataṃ')}, твёрдость, свойство твёрдости"
        + OWN,
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā "
    "anupādiṇṇaṃ vā":
        "То, что есть вода, считающееся водой, влага, считающееся влагой, связующее свойство материальной формы"
        + OWN,
    "Yaṃ tejo tejogataṃ usmā usmāgataṃ usumaṃ usumagataṃ ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        "То, что есть огонь, считающееся огнём, тепло, считающееся теплом, жар, считающееся жаром" + OWN,
    "Yaṃ vāyo vāyogataṃ thambhitattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        "То, что есть ветер, считающееся ветром, состояние напряжённости материальной формы" + OWN,
}
VACI_P = ("Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā vācā girā byappatho udīraṇaṃ {g} "
          "ghosakammaṃ vācā vacībhedo{sep} ayaṃ vuccati vācā. Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ")
VACI_HEAD = f"То, что {MINDS} есть {SPEECH}"
VACI_TAIL = f"это называется речью. То, что посредством этой речи есть {INTIM}"
SHORT[VACI_P.format(g="ghoso", sep=" –")] = f"{VACI_HEAD}, – {VACI_TAIL}"     # ^1-636
SHORT[VACI_P.format(g="ghoso", sep=",")] = f"{VACI_HEAD}, {VACI_TAIL}"       # ^1-722
SHORT[VACI_P.format(g="dhoso", sep=",")] = f"{VACI_HEAD}, {VACI_TAIL}"       # ^1-850 «dhoso» (termbase: голос)
KABALI_P = ("Odano kummāso sattu maccho maṃsaṃ khīraṃ dadhi sappi navanītaṃ telaṃ madhu phāṇitaṃ, yaṃ vā "
            "panaññampi atthi rūpaṃ yamhi yamhi janapade tesaṃ tesaṃ sattānaṃ mukhāsiyaṃ dantavikhādanaṃ "
            "galajjhoharaṇīyaṃ kucchivitthambhanaṃ, yāya ojāya sattā yāpenti")
FOOD = ("Варёный рис, каша, толокно, рыба, мясо, молоко, простокваша, топлёное масло, сливочное масло, "
        "растительное масло, мёд, патока")
KABALI_R = (f"{FOOD}, {OTHER} в той или иной местности для тех или иных существ, которую можно есть ртом, "
            "разжёвывать зубами, проглатывать через горло и которая наполняет живот, питательная сущность, "
            "которой существа поддерживают свою жизнь")
SHORT[KABALI_P] = KABALI_R

DEFS = dict(SHORT)
for _k in ORG:
    for _part in ("a", "b", "c", "d", "abbr"):
        _p, _r = organ_def(_k, _part)
        DEFS[_p] = _r
_p, _r = organ_def("cakkhu", "a", " [cakkhuṃ (sī. syā.)]", " " + S.spell("Sī., Syā.", "cakkhuṃ"))
DEFS[_p] = _r                                                                  # ^1-596
for _k in OBJ:
    for _part in ("a", "b", "c", "d"):
        for _v in ((False, True) if _k in ("rūpa", "rasa") else (False,)):
            _p, _r = object_def(_k, _part, _v)
            DEFS[_p] = _r
for _k in ("rūpa", "phoṭṭhabba"):
    _p, _r = object_def(_k, "abbr")
    DEFS[_p] = _r

# slips of spacing and punctuation, rendered as meant (reported)
SLIPS = {
    " " + PE: PE,                                             # «cetanāya …pe…», «Cakkhāyatanaṃ …pe…» …
    "gāmopeso": "gāmo peso",                                  # ^1-596, ^1-606
    "phuse vā phoṭṭhabbo peso": "phuse vā, phoṭṭhabbo peso",  # ^1-647, missing comma
    "kucchivitthambhanaṃ yāya": "kucchivitthambhanaṃ, yāya",  # ^1-880, missing comma
}


def norm(s):
    for a, b in SLIPS.items():
        s = s.replace(a, b)
    return s


# =========================================================================================
# 5. Fixed lines and headings
# =========================================================================================
H_DUKA_N = f"{T.NIDDESO} классификации по {T.NUM[1][2]}"        # Dukaniddeso
H_TIKA_N = f"{T.NIDDESO} классификации по {T.NUM[2][2]}"        # Tikaniddeso
H_UPADA = f"Разбор производной {T.RUPA_GEN}"                    # Upādābhājanīyaṃ (bhājanīyaṃ = разбор)
assert T.H_EKAKANIDDESO == f"{T.NIDDESO} классификации по одному"
BHANA_1 = f"{S.BHANAVARA_1} в разделе о материальной форме"    # Rūpakaṇḍe paṭhamabhāṇavāro.
BHANA_8 = "Восьмой раздел для чтения вслух"                     # Aṭṭhamabhāṇavāro.
assert S.CH_HEADINGS["Rūpakaṇḍaṃ"] == "Раздел о материальной форме"
DONE = "Раздел о материальной форме завершён"                   # Rūpakaṇḍaṃ niṭṭhitaṃ. (cf. 2-05)


def vin_is(subj, by):
    """X-viññeyyaṃ rūpaṃ as identity: «X есть материальная форма, познаваемая …» (termbase frame)."""
    return f"{subj} есть {T.vin(by)}"


AY = {k: T.NOUN[k][0] for k in ("rūpāyatanaṃ", "saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ",
                                 "phoṭṭhabbāyatanaṃ")}
BY = dict(zip(("rūpāyatanaṃ", "saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ", "phoṭṭhabbāyatanaṃ"),
              (b for _, b in T.VIÑÑEYYA)))
SABBA = T.SABBA_RUPA                                              # вся материальная форма
assert SABBA == "вся материальная форма"
FOUR_R = [vin_is(AY[k], BY[k]) for k in ("rūpāyatanaṃ", "saddāyatanaṃ", "gandhāyatanaṃ", "rasāyatanaṃ")]
TOUCH_R = vin_is(AY["phoṭṭhabbāyatanaṃ"], BY["phoṭṭhabbāyatanaṃ"])
MANODHATU_R = vin_is(", ".join(AY.values()), T.VIÑÑEYYA_MANO["manodhātu"])
LAST_MANO = vin_is(SABBA, T.VIÑÑEYYA_MANO["mano"])
LAST_MVD = vin_is(SABBA, T.VIÑÑEYYA_MANO["manoviññāṇadhātu"])
AGREE_R = [vin_is("желанное осязаемое, доставляющее удовольствие при контакте,", BY["phoṭṭhabbāyatanaṃ"]),
           vin_is("нежеланное осязаемое, болезненное при контакте,", BY["phoṭṭhabbāyatanaṃ"])]
_FIVE_P = ("Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, saddāyatanaṃ sotaviññeyyaṃ rūpaṃ, gandhāyatanaṃ ghānaviññeyyaṃ "
           "rūpaṃ, rasāyatanaṃ jivhāviññeyyaṃ rūpaṃ, ")
_MANODHATU_P = ("rūpāyatanaṃ saddāyatanaṃ gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ manodhātuviññeyyaṃ rūpaṃ, "
                "sabbaṃ rūpaṃ manoviññāṇadhātuviññeyyaṃ rūpaṃ.")

EXACT = {
    "##### Dukaniddeso": f"##### {H_DUKA_N}",
    "Dukaniddeso.": f"{H_DUKA_N}.",
    "###### Upādābhājanīyaṃ": f"###### {H_UPADA}",
    "Upādābhājanīyaṃ.": f"{H_UPADA}.",
    "Rūpakaṇḍe paṭhamabhāṇavāro.": f"{BHANA_1}.",
    "Idaṃ taṃ rūpaṃ upādā.": cap(S.a_form(name_ru("upādā"))),
    "Idaṃ taṃ rūpaṃ no upādā.": cap(S.a_form(name_ru("no upādā"))),
    "##### Tikaniddeso": f"##### {H_TIKA_N}",
    "Tikaniddeso.": f"{H_TIKA_N}.",
    "Aṭṭhamabhāṇavāro.": f"{BHANA_8}.",
    "Rūpavibhatti.": f"{T.H_VIBHATTI}.",
    "Rūpakaṇḍaṃ niṭṭhitaṃ.": f"{DONE}.",
    _FIVE_P + "phoṭṭhabbāyatanaṃ kāyaviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ manoviññeyyaṃ rūpaṃ.":
        cap("; ".join(FOUR_R + [TOUCH_R, LAST_MANO]) + "."),
    _FIVE_P + "phoṭṭhabbāyatanaṃ kāyaviññeyyaṃ rūpaṃ, " + _MANODHATU_P:
        cap("; ".join(FOUR_R + [TOUCH_R, MANODHATU_R, LAST_MVD]) + "."),
    _FIVE_P + "manāpiyo phoṭṭhabbo sukhasamphasso kāyaviññeyyaṃ rūpaṃ, amanāpiyo phoṭṭhabbo dukkhasamphasso "
              "kāyaviññeyyaṃ rūpaṃ, " + _MANODHATU_P:
        cap("; ".join(FOUR_R + AGREE_R + [MANODHATU_R, LAST_MVD]) + "."),
}
EXACT["Rūpāyatanaṃ diṭṭhaṃ, saddāyatanaṃ sutaṃ, gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ mutaṃ, "
      "sabbaṃ rūpaṃ manasā viññātaṃ rūpaṃ."] = cap(
    f"{AY['rūpāyatanaṃ']} есть увиденное; {AY['saddāyatanaṃ']} есть услышанное; "
    f"{AY['gandhāyatanaṃ']}, {AY['rasāyatanaṃ']}, {AY['phoṭṭhabbāyatanaṃ']} есть ощущённое; "
    f"{SABBA} есть {RUPA}, познанная умом.")
for _k, _v in T.EXACT.items():        # counted headings and closing lines of 3-01 (##### Catukkaṃ, Evaṃ …)
    if _k.startswith("#####") or _k.startswith("Evaṃ ") or (_k.endswith("kaṃ.") and len(_k) < 16):
        EXACT.setdefault(_k, _v)

# =========================================================================================
# 6. Question / answer lines
# =========================================================================================
QA_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (.+?)([?.]) (.+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")
NOQ_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (.+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")
BARE_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (.+?)\? (.+)\.$")


def answer_ru(a):
    if a in DEFS:
        return DEFS[a]
    return list_ru(a)


def qa_ru(line):
    line = norm(line)
    m = QA_RE.match(line)
    if m:
        q, qp, a, q2, ap = m.groups()
        assert q2 == q or q.endswith(q2) or q.endswith(q2.split()[-1]), line[:80]
        return f"Что такое {name_ru(q)}{qp} {answer_ru(a)}{ARE}это {name_ru(q2)}{ap}"
    if " – " not in line:                 # ^1-595, ^1-646: bare list, no closing formula
        m = BARE_RE.match(line)
        q, a = m.groups()
        return f"{S.q_form(name_ru(q))} {list_ru(a)}."
    m = NOQ_RE.match(line)                # ^1-895, ^1-939: no «?» after the question (as written)
    body, q2, ap = m.groups()
    assert body.startswith(q2 + " "), line[:80]
    a = body[len(q2) + 1:]
    ar = answer_ru(a)
    ar = ar[0].lower() + ar[1:]
    return f"Что такое {name_ru(q2)} {ar}{ARE}это {name_ru(q2)}{ap}"


def translate_line(line):
    if line in EXACT:
        return EXACT[line]
    if line.startswith("Katamaṃ taṃ rūpaṃ "):
        return qa_ru(line)
    raise KeyError("line: " + line[:80])


def render(segs):
    blocks = []
    for sid, plines in segs:
        rlines = []
        for p in plines:
            r = translate_line(p)
            assert r == cap(r), r[:40]
            T.check_ru(r)
            assert len(p) - len(p.lstrip("#")) == len(r) - len(r.lstrip("#")), sid
            assert p.count("–") + p.count("—") == r.count("–"), ("dash", sid, p[:60], r[:60])
            assert norm(p).count(PE) <= r.count(ELL), ("pe", sid)
            assert p.endswith("?") == r.endswith("?") and p.count("?") == r.count("?"), ("question", sid)
            assert "  " not in r and " ," not in r and ",," not in r and " … " not in r and "..." not in r, r
            assert ";;" not in r and ": ," not in r and ",:" not in r, r
            rlines.append(r)
        rlines[-1] += f" ^{sid}"
        blocks.append("\n".join(rlines))
    return blocks


def build(part):
    segs = T.segments(S.PALI / part)
    return "\n\n".join(render(segs)) + "\n", len(segs)


# =========================================================================================
# 7. Notes
# =========================================================================================
def notes():
    L = ["# pi-1 Russian rails: new formulas of 3-02 and 3-03", "",
         "Generated by build_rails_3-02_3-03_ru.py from its fixed strings; import that file instead of retyping. "
         "Strings already in ru-rails-formulas.md, the chapter-2 notes or notes-3-01.md are not repeated; the "
         "material-form items, predicates and vatthu / ārammaṇaṃ chains come from build_rails_3-01_ru.py.", "",
         "## Frames", "",
         "Katamaṃ taṃ rūpaṃ X? = Что такое <name X>?",
         "… – idaṃ taṃ rūpaṃ X. = …, – это <name X>.",
         "Idaṃ taṃ rūpaṃ upādā. / no upādā. = " + EXACT["Idaṃ taṃ rūpaṃ upādā."] + " / "
         + EXACT["Idaṃ taṃ rūpaṃ no upādā."],
         "<name>: plain adjectives before «материальная форма» (" + ", ".join(f"{k} {v}" for k, v in PRE.items())
         + "); all other predicates after it as participial phrases «материальная форма, A и B» (a phrase that "
         "already has «и» / «но» is joined with a comma)",
         "  examples: ajjhattikaṃ upādā = " + name_ru("ajjhattikaṃ upādā"),
         "  bāhiraṃ cakkhusamphassassa na vatthu = " + name_ru("bāhiraṃ cakkhusamphassassa na vatthu"),
         "  ajjhattikaṃ upādiṇṇupādāniyaṃ = " + name_ru("ajjhattikaṃ upādiṇṇupādāniyaṃ"),
         "  upādā oḷārikaṃ = " + name_ru("upādā oḷārikaṃ"),
         "  bāhiraṃ na sotāyatanaṃ…pe… na kāyāyatanaṃ = " + name_ru("bāhiraṃ na sotāyatanaṃ…pe… na kāyāyatanaṃ"),
         "  anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ = "
         + name_ru("anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ"),
         "dūre / santike (in a name) = " + POST["dūre"] + " / " + POST["santike"],
         "", "## Lists", "",
         f"yaṃ vā panaññampi atthi rūpaṃ Q: X, Y = , {OTHER} Q: X, Y"]
    for p, r in QUALS.items():
        L.append(f"  {p} = {r}")
    L += [f"Kammassa katattā X Y (as a list lead) = {cap(KAMMA)}: X, Y",
          "X Y Z (items without commas) = X, Y, Z; X…pe… Y = X… Y",
          "", "## Sense-organ definitions (cakkhu; the others alike)", ""]
    for part in ("a", "b", "c", "d", "abbr"):
        p, r = organ_def("cakkhu", part)
        L.append(f"[{part}] {p} = {r}")
    L += ["", "## Object definitions (rūpa; sadda, gandha, rasa, phoṭṭhabba alike)", ""]
    for part in ("a", "b", "c", "d", "abbr"):
        p, r = object_def("rūpa", part)
        L.append(f"[{part}] {p} = {r}")
    L.append(f"[sadda a] {object_def('sadda', 'a')[0]} = {object_def('sadda', 'a')[1]}")
    L.append(f"[phoṭṭhabba a] {object_def('phoṭṭhabba', 'a')[0]} = {object_def('phoṭṭhabba', 'a')[1]}")
    L += ["", "## Words and phrases of the definitions", ""]
    for lst in (COLOURS, SOUNDS, SMELLS, TASTES, TOUCH):
        for p, r in lst:
            L.append(f"{p.format(v1='', v2='', v3='')} = {r.format(v1='', v2='', v3='')}")
    L += ["catunnaṃ mahābhūtānaṃ upādāya = " + MAHA.format("ый/ая/ое"),
          "pasādo attabhāvapariyāpanno anidassano sappaṭigho = (является) " + SENS[len("является "):],
          "paṭihaññi vā paṭihaññati vā paṭihaññissati vā paṭihaññe vā = " + strike("m") + " (по роду)",
          "uppajji vā uppajjati vā uppajjissati vā uppajje vā = " + arise("m") + " (по роду)",
          "passi vā passati vā passissati vā passe vā = " + four(ORG["cakkhu"]["see"]),
          "suṇi … / ghāyi … / sāyi … / phusi … = " + " / ".join(four(ORG[k]["see"]) for k in
                                                             ("sota", "ghāna", "jivhā", "kāya")),
          "X nissāya = в зависимости от X; yaṃ X nissāya = X, в зависимости от которого",
          "Y ārabbha (organ definitions) = имея объектом Y; yaṃ Y ārabbha (object definitions) = Y, имея которую "
          "(который, которое) объектом",
          "Y-ārammaṇo / -ā (organ definitions) = имеющий / имеющее объектом Y; yaṃ Y-ārammaṇo (object definitions) "
          "= Y, с которой (которым) как с объектом",
          "cakkhuṃ petaṃ … suñño gāmo peso = это глаз, это сфера глаза, это элемент глаза, это способность глаза, "
          + NAMES_R.format(extra=EXTRA_R),
          "loko = мир; orimaṃ tīraṃ = ближний берег; vatthuṃ = основа; paṇḍaraṃ = чистота (as the citta string)",
          "", "## Short definitions", ""]
    for p, r in SHORT.items():
        L.append(f"{p} = {r}")
    L += ["", "## Headings and fixed lines", ""]
    for p, r in EXACT.items():
        if p not in T.EXACT:
            L.append(f"{p} = {r}")
    L += ["", "## Slips (rendered as meant or kept as written)", "",
          "stray space before «…pe…» (^1-680, ^1-689, ^1-699 …, ^1-976 …) = as «…pe…»",
          "«gāmopeso» (^1-596, ^1-606) = as «gāmo peso»",
          "^1-647 missing comma before «phoṭṭhabbo peso»; ^1-880 missing comma before «yāya ojāya»; "
          "^1-655 and ^1-666 commas = the same Russian as the parallels",
          "^1-750 question ends with «.»; ^1-765, ^1-773, ^1-788 the answer ends with «?»; ^1-895, ^1-939 no «?» "
          "after the question: kept as written",
          "^1-850 «dhoso» = «голос» (the termbase has dhoso = голос)"]
    (HERE / "notes-3-02_3-03.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print("wrote", HERE / "notes-3-02_3-03.md")


def main():
    for part in PARTS:
        text, n = build(part)
        (S.OUT / part).write_text(text, encoding="utf-8", newline="\n")
        print("wrote", S.OUT / part, n, "segments")
    notes()


if __name__ == "__main__":
    main()
