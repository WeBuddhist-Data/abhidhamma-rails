"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 8 (Cittayamaka) and the FAMILY D module (cittayamaka frames:
puggalavāra, dhammavāra, puggaladhammavāra, the fourteen time sections, uppajjamāna / nirujjhamāna / uppanna /
niruddha, the suttanta / abhidhamma mixtures) that later chapters import.

Import READ-ONLY (importing writes nothing; outputs are written only under `if __name__ == "__main__":`):
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import build_rails_8_vi as D          (or importlib.import_module("build_rails_8_vi"))

What the module gives later chapters (all byte-fixed; never retype the strings):
  VERB_POS / VERB_NEG / vkey()         the ten aspect forms (uppajjati … nirujjhamānaṃ, + -ti / -ñca / -ñceva forms)
  pos() / neg() / still()              positive, separate-"na" negative, and the «vẫn» form after "no ca … na"
  pred_vi()                            a predicate run: "A na B", "A ceva B ca", "na ceva A na ca B" …
  verb_answer()                        one-word verb answers (Uppajjittha. / Nirujjhati. …)
  MIND_ADJ / mind_vi() / mind_gen_vi() the kinds of mind (sarāga … avimutta, kusala …, araṇa …) as subject / genitive
  MOMENT / TIME_KIND / kind_subject()  moments (uppādakkhaṇe …) and time kinds (atītaṃ …) of the dhammavāra answers
  PERSON / head_vi()                   answer heads: persons (genitive pl.), «vào khoảnh khắc … của tâm …»
  question()                           the yassa / yaṃ / yassa yaṃ question frames (incl. atītānāgata, atikkantakāla,
                                       the bare uppanna / niruddha pairs) + answers on the same line
  sentence() / sentences()             one answer sentence / a run of them
  chain()                              the cut uddesa chains "Yassa X cittaṃ uppajjati…pe… yassa Y … …?"
  heading() / VARO                     chapter headings
  tr_line() / build()                  the line translator (S's per-line checks run in S.write)
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_8_vi.py
"""
import importlib
import pathlib
import re
import sys
import unicodedata

RAILS_DIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
if str(RAILS_DIR) not in sys.path:
    sys.path.insert(0, str(RAILS_DIR))
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)

CHAPTER = "8-cittayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-8.md"
ADH_DIR = RAILS_DIR / "adh-8"
cap = S.cap
PE = S.PE
YES = S.YES

SLIPS_SEEN = []                               # (Pāli, as meant), printed by main()

# ---------------------------------------------------------------------------------------------------------------
# 1. Words shared with the other wave-1 families (2-01: families A, B; 7-01: family C). Coordinator aligns these.
# ---------------------------------------------------------------------------------------------------------------
# Binding shared shapes (rails-coordinator-rules.md "From rails 7-01"): taken from the 7-01 module, READ-ONLY.
C = importlib.import_module("build_rails_7-01_vi")
AT = C.AT                                     # «ở»: person head «Ở <person>, …»
THEN = C.THEN                                 # «thì»
BUT = C.BUT                                   # «nhưng»: no ca; also between two juxtaposed verbs "uppajjati na nirujjhati"
STILL = C.STILL                               # «vẫn»: after "no ca" a negative verb is denied
ALSO = C.ALSO                                 # «cũng»: "na ceva A na ca B" = «không A, cũng không B»
NONE = C.NEITHER_FIRST                        # «không có»: "no ca tassa / tesaṃ A V" = «nhưng ở người ấy không có A V»
AND = C.AND                                   # «và»
PRON = {k: C.PRON[k] for k in ("tassa", "tesaṃ")}   # «người ấy» / «những người ấy»
VA_PANA = C.VA_PANA                           # «Còn»: (Kha) … vā pana …
ANS_NO = C.ANS_NO                             # No. «Không.»
ANS_NATTHI = C.ANS_NATTHI                     # Natthi. «Không có.» (pi-3)
BOTH = "vừa"                                  # one subject, two verbs "V1 ceva V2 ca" = «vừa V1 vừa V2» (sample; not the
                                              # 7-01 two-subject frame "A ca V B ca V" «A V, B cũng V»)
EXACT = {"Āmantā.": YES, "No.": ANS_NO, "Natthi.": ANS_NATTHI}

# The ten aspect forms of uppajjati / nirujjhati. The six finite tenses come from family B (2-01 VERB_TABLE, READ-ONLY);
# the four participles are family D (termbase wording).
B = importlib.import_module("build_rails_2-01_vi")
FINITE = ("uppajjati", "nirujjhati", "uppajjittha", "nirujjhittha", "uppajjissati", "nirujjhissati")
PARTICIPLE_POS = {
    "uppannaṃ": "ở trạng thái đã sinh khởi", "niruddhaṃ": "ở trạng thái đã chấm dứt",   # termbase (kept apart
    "uppajjamānaṃ": "đang sinh khởi", "nirujjhamānaṃ": "đang chấm dứt",                 #  from uppajjittha)
}
PARTICIPLE_NEG = {   # a separate "na" negates the positive term (coordinator)
    "uppannaṃ": "không ở trạng thái đã sinh khởi", "niruddhaṃ": "không ở trạng thái đã chấm dứt",
    "uppajjamānaṃ": "không phải đang sinh khởi", "nirujjhamānaṃ": "không phải đang chấm dứt",
}
VERB_POS = {k: B.verb(k)[2] for k in FINITE} | PARTICIPLE_POS   # sinh khởi / đã … / sẽ … (2-01)
VERB_NEG = {k: B.verb(k)[3] for k in FINITE} | PARTICIPLE_NEG   # không … / chưa từng … / sẽ không … (2-01)
PRESENT = ("uppajjati", "nirujjhati")
HAS = "Có"                                    # a bare present-tense verb answer: Nirujjhati. = «Có chấm dứt.» (2-01)


def _ti(v):                                   # question-final form: uppajjatīti, uppajjitthāti, uppannanti
    if v.endswith("ti"):
        return v[:-1] + "īti"
    if v.endswith("a"):
        return v[:-1] + "āti"
    if v.endswith("ṃ"):
        return v[:-1] + "nti"
    raise ValueError(v)


VKEY = {v: v for v in VERB_POS} | {_ti(v): v for v in VERB_POS}


def vkey(w):
    """Pāli verb word (with or without -ti) → key of VERB_POS; anything else raises."""
    if w not in VKEY:
        raise ValueError(f"unknown verb word {w!r}")
    return VKEY[w]


def pos(w):
    return VERB_POS[vkey(w)]


def neg(w):
    return VERB_NEG[vkey(w)]


def still(w):
    """"no ca … na V" (2-01 denied_vi, coordinator): present «vẫn V», future «vẫn sẽ V», past «đã từng V»;
    participles «vẫn ở trạng thái đã …» / «vẫn đang …»."""
    return B.denied_vi(pos(w))


def verb_answer(w):
    """Uppajjittha. «Đã sinh khởi.»; Nirujjhati. «Có chấm dứt.» (2-01 short_answer); Uppannaṃ. «Ở trạng thái đã
    sinh khởi.» (participle: no «Có»)."""
    k = vkey(w)
    if k in FINITE:
        return B.short_answer(VERB_POS[k])
    return f"{cap(VERB_POS[k])}."


def split_ca(w):
    """'uppannañceva' → ['uppannaṃ', 'ceva']; 'uppajjamānañca' → ['uppajjamānaṃ', 'ca']."""
    for suf, part in (("ñceva", "ceva"), ("ñca", "ca")):
        if w.endswith(suf):
            return [w[:-len(suf)] + "ṃ", part]
    return [w]


def ptoks(text):
    out = []
    for w in text.split():
        out += split_ca(w)
    return out


def _units(toks):
    """['na', 'uppajjati', 'nirujjhati'] → [['na', 'uppajjati'], ['nirujjhati']]."""
    out, cur = [], []
    for t in toks:
        cur.append(t)
        if t != "na":
            vkey(t)
            out.append(cur)
            cur = []
    if cur:
        raise ValueError(f"dangling 'na' in {toks!r}")
    return out


def simple(u):                                # [na] V
    if u[0] == "na":
        if len(u) != 2:
            raise ValueError(u)
        return neg(u[1])
    if len(u) != 1:
        raise ValueError(u)
    return pos(u[0])


def pred_vi(toks):
    """Predicate run → Vietnamese.
    "V" / "na V"                        → «V» / «không V»
    "A na B" / "na A B"                 → «A nhưng không B» / «không A nhưng B»
    "A ceva B ca" / "Añceva Bñca"       → «vừa A vừa B»   (A may be "na V")
    "na ceva A na ca B"                 → «không A, cũng không B»"""
    t = list(toks)
    if t[:2] == ["na", "ceva"]:
        i = t.index("na", 2)
        if t[i + 1] != "ca":
            raise ValueError(t)
        a, b = _units(t[2:i]), _units(t[i + 2:])
        if len(a) != 1 or len(b) != 1:
            raise ValueError(t)
        return f"{neg(a[0][0])}, {ALSO} {neg(b[0][0])}"
    if "ceva" in t:
        i = t.index("ceva")
        if t[-1] != "ca":
            raise ValueError(t)
        a, b = _units(t[:i]), _units(t[i + 1:-1])
        if len(a) != 1 or len(b) != 1:
            raise ValueError(t)
        return f"{BOTH} {simple(a[0])} {BOTH} {simple(b[0])}"
    us = _units(t)
    if len(us) == 1:
        return simple(us[0])
    if len(us) == 2:
        return f"{simple(us[0])} {BUT} {simple(us[1])}"
    raise ValueError(f"unknown predicate {toks!r}")


# ---------------------------------------------------------------------------------------------------------------
# 2. Kinds of mind (termbase; = pi-2 7-satipatthanavibhango / 16-nanavibhango, pi-1 mātikā)
# ---------------------------------------------------------------------------------------------------------------
MIND = "tâm"                                  # cittaṃ (termbase)
MIND_ADJ = {   # stem → Vietnamese, placed after «tâm»
    "sarāga": "có tham đắm", "vītarāga": "đã lìa tham đắm", "sadosa": "có sân hận", "vītadosa": "đã lìa sân hận",
    "samoha": "có si mê", "vītamoha": "đã lìa si mê", "saṃkhitta": "co rút", "vikkhitta": "tán loạn",
    "mahaggata": "rộng lớn", "amahaggata": "không rộng lớn", "sauttara": "còn có điều cao hơn",
    "anuttara": "không có điều gì cao hơn", "samāhita": "được định tâm", "asamāhita": "không được định tâm",
    "vimutta": "được giải thoát", "avimutta": "không được giải thoát",                       # (pi-2)
    "kusala": "thiện", "akusala": "bất thiện", "abyākata": "không xác định về mặt đạo đức",   # termbase «tâm thiện» …
    "sukhāya vedanāya sampayutta": "gắn liền với cảm giác dễ chịu",                         # (pi-1)
    "araṇa": "không có xung đột", "saraṇa": "có xung đột",                                  # (pi-1)
}
FINAL = "cuối cùng"                           # pacchima- (termbase Pacchimacittassa «tâm cuối cùng»)


def mind_vi(adj_acc=""):
    """'' → «tâm»; 'sarāgaṃ' → «tâm có tham đắm»; 'sukhāya vedanāya sampayuttaṃ' → «tâm gắn liền với …»."""
    if not adj_acc:
        return MIND
    if not adj_acc.endswith("ṃ"):
        raise ValueError(f"not a neuter accusative mind adjective: {adj_acc!r}")
    stem = adj_acc[:-1]
    if stem not in MIND_ADJ:
        raise ValueError(f"unknown kind of mind {adj_acc!r}")
    return f"{MIND} {MIND_ADJ[stem]}"


def mind_gen_vi(word):
    """'Cittassa' «tâm», 'Pacchimacittassa' «tâm cuối cùng», 'Sarāgapacchimacittassa' «tâm có tham đắm cuối cùng»,
    'kusalacittassa' «tâm thiện», 'Pacchimakusalacittassa' «tâm thiện cuối cùng»."""
    w = word[0].lower() + word[1:]
    if not w.endswith("cittassa"):
        raise ValueError(word)
    stem = w[:-len("cittassa")]
    final = "pacchima" in stem
    stem = stem.replace("pacchima", "")
    out = MIND
    if stem:
        if stem not in MIND_ADJ:
            raise ValueError(f"unknown kind of mind {word!r}")
        out += " " + MIND_ADJ[stem]
    return out + (" " + FINAL if final else "")


# ---------------------------------------------------------------------------------------------------------------
# 3. Moments, time kinds, persons (termbase; pi-5 «vào khoảnh khắc sinh khởi / tan rã»)
# ---------------------------------------------------------------------------------------------------------------
MOMENT = {"uppādakkhaṇe": "khoảnh khắc sinh khởi", "bhaṅgakkhaṇe": "khoảnh khắc tan rã"}        # locative
MOMENT_ACC = {"uppādakkhaṇaṃ": "khoảnh khắc sinh khởi", "bhaṅgakkhaṇaṃ": "khoảnh khắc tan rã"}  # accusative
AT_TIME = "vào"                               # «vào khoảnh khắc …» (pi-5)
OF = "của"
TIME_KIND = {"atītaṃ": "thuộc quá khứ", "anāgataṃ": "thuộc tương lai", "paccuppannaṃ": "thuộc hiện tại",
             "atītānāgataṃ": "thuộc quá khứ và tương lai"}                                     # termbase
PEOPLE = B.PERSON                             # «những người»: head noun of a person group (2-01)
PERSON = {   # genitive plural (lower-case first letter) → Vietnamese (one «ở» for a run; groups joined as 2-01)
    "nirodhasamāpannānaṃ": "những người nhập thành tựu thiền chấm dứt",   # termbase «người nhập …» + 2-01 head
    "asaññasattānaṃ": "chúng sinh Vô Tưởng",                              # termbase Asaññasattānaṃ (= 2-01)
    "pacchimacittasamaṅgīnaṃ": "những người có được tâm cuối cùng",       # termbase
    "cittasamaṅgīnaṃ": "những người có được tâm",                         # termbase / coordinator
    "itaresaṃ": "những người khác",                                       # termbase «người khác» (= 2-01 Itaresaṃ)
}
assert all(v.startswith(PEOPLE) for k, v in PERSON.items() if k != "asaññasattānaṃ")
OTHERS_WITH_MIND = "những người khác có được tâm"   # Itaresaṃ cittasamaṅgīnaṃ (one group)


def _lc(w):
    return w[0].lower() + w[1:]


def moment_phrase(moment_loc, mind_gen=None):
    """'uppādakkhaṇe' → «vào khoảnh khắc sinh khởi»; with a mind: «vào khoảnh khắc sinh khởi của tâm …»."""
    m = MOMENT[_lc(moment_loc)]
    return f"{AT_TIME} {m} {OF} {mind_gen_vi(mind_gen)}" if mind_gen else f"{AT_TIME} {m}"


def kind_item(w):
    """Dhammavāra subject item → («tâm vào khoảnh khắc …» | «tâm thuộc …», has ca?)."""
    lw = _lc(w)
    ca = lw.endswith("ñca")
    if ca:
        lw = lw[:-3] + "ṃ"
    if lw in MOMENT:
        return f"{MIND} {moment_phrase(lw)}", ca
    if lw in TIME_KIND:
        return f"{MIND} {TIME_KIND[lw]}", ca
    raise ValueError(f"unknown kind of mind (time) {w!r}")


def kind_subject(words):
    """['Bhaṅgakkhaṇe', 'anāgatañca'] → «tâm vào khoảnh khắc tan rã và tâm thuộc tương lai»;
    ['Uppādakkhaṇe', 'anāgataṃ'] (no ca) → «tâm vào khoảnh khắc sinh khởi, tâm thuộc tương lai»."""
    items = [kind_item(w) for w in words]
    if not items:
        raise ValueError("empty subject")
    out = items[0][0]
    for vi, ca in items[1:]:
        out += (f" {AND} " if ca else ", ") + vi
    return out


def head_vi(words):
    """Answer head before 'tesaṃ': [Itaresaṃ] [<mind>cittassa <moment>] [persons …] → list of Vietnamese parts."""
    parts, i = [], 0
    if i < len(words) and _lc(words[i]) == "itaresaṃ":
        if i + 1 < len(words) and words[i + 1] == "cittasamaṅgīnaṃ":
            parts.append(f"{AT} {OTHERS_WITH_MIND}")
            i += 2
        else:
            parts.append(f"{AT} {PERSON['itaresaṃ']}")
            i += 1
    if i + 1 < len(words) and words[i].lower().endswith("cittassa") and _lc(words[i + 1]) in MOMENT:
        parts.append(moment_phrase(words[i + 1], words[i]))
        i += 2
    group = []
    while i < len(words):
        lw = _lc(words[i])
        if lw not in PERSON or lw == "itaresaṃ":
            raise ValueError(f"unknown answer head word {words[i]!r} in {words!r}")
        group.append(PERSON[lw])
        i += 1
    if group:
        parts.append(f"{AT} " + B.join_and(group))                # «A và B», «A, B và C» (2-01 / 7-01)
    if not parts:
        raise ValueError(f"empty answer head {words!r}")
    return parts


# ---------------------------------------------------------------------------------------------------------------
# 4. Question frames (coordinator person shell; yaṃ / yassa yaṃ by analogy; set here for family D)
# ---------------------------------------------------------------------------------------------------------------
WHICH, THAT = "nào", "ấy"
WHO, THAT_ONE = "người nào", "người ấy"
RES = {"P": "tassa", "D": "taṃ", "PD": "tassa taṃ"}


def subj(mode, part, s):
    """Mind subject inside a frame: part 1 = relative («tâm nào»), part 2 = correlative («tâm ấy»), mode P: «tâm»."""
    if mode == "P":
        return s
    return f"{s} {WHICH if part == 1 else THAT}"


def frame(mode, kha, a, b):
    """mode P:  (Ka) yassa S A tassa S B?        = «Ở người nào mà S A, thì ở người ấy có phải S B không?»
    mode D:  (Ka) yaṃ S A taṃ S B?             = «S nào A, thì có phải S ấy B không?»
    mode PD: (Ka) yassa yaṃ S A tassa taṃ S B? = «Ở người nào mà S nào A, thì ở người ấy có phải S ấy B không?»
    (a, b: Vietnamese subject + predicate). kha adds «Còn …»."""
    if mode == "D":
        s = f"{a}, {THEN} có phải {b} không?"
    else:
        s = f"{AT} {WHO} mà {a}, {THEN} {AT} {THAT_ONE} có phải {b} không?"
    return f"{VA_PANA} {s[0].lower() + s[1:]}" if kha else cap(s)


def no_ca_vi(res, s, toks):
    """The clause after "no ca <res> <subject>" (without «nhưng»), 7-01 shapes for a person pronoun:
    res 'tassa' / 'tesaṃ' / 'tassa taṃ' + V    → «ở người ấy / ở những người ấy không có <S> V»
                                    + na V → «ở người ấy / ở những người ấy <S> vẫn V»
    res 'taṃ' (no person)            + V    → «<S> ấy không V»;  + na V → «<S> ấy vẫn V»
    res '' (bare, (12) / (13))       + V    → «không V»;         + na V → «vẫn V»"""
    us = _units(list(toks))
    if len(us) != 1:
        raise ValueError(toks)
    u = us[0]
    negative = u[0] == "na"
    v = u[-1]
    if res == "":
        return still(v) if negative else neg(v)
    if res == "taṃ":
        return f"{s} {THAT} {still(v) if negative else neg(v)}"
    pron = PRON["tesaṃ" if res == "tesaṃ" else "tassa"]
    sv = f"{s} {THAT}" if res == "tassa taṃ" else s
    return f"{AT} {pron} {sv} {still(v)}" if negative else f"{AT} {pron} {NONE} {sv} {pos(v)}"


def parse_sp(text):
    """'araṇaṃ cittaṃ uppajjati na nirujjhati' → ('araṇaṃ', ['uppajjati', 'na', 'nirujjhati'])."""
    w = text.split()
    if "cittaṃ" not in w:
        raise ValueError(f"no 'cittaṃ' in {text!r}")
    k = w.index("cittaṃ")
    return " ".join(w[:k]), ptoks(" ".join(w[k + 1:]))


Q_HEAD_RE = re.compile(r"([Yy]assa|yaṃ)( vā pana)?( yaṃ)? (.+)")

# atikkantakāla (14)
MOMENT_PROG = {"uppajjamānaṃ": "khoảnh khắc đang sinh khởi", "nirujjhamānaṃ": "khoảnh khắc đang chấm dứt"}
PASSED, NOT_PASSED = "đã vượt khỏi", "chưa vượt khỏi"        # vītikkanta (pi-2 vītikkanto «đã vượt khỏi»)
STILL_PASSED = B.denied_vi(PASSED)                            # no ca … avītikkantaṃ = «đã từng vượt khỏi» (past rule)
GONE = "khoảnh khắc ấy thuộc thời đã qua"                     # khaṇaṃ … atikkantakālaṃ (Atikkantakālavāro «thời đã qua»)
NOT_GONE = "khoảnh khắc ấy không thuộc thời đã qua"
ATK_TAIL = {"P": f"{THEN} có phải đó là {MIND} {OF} {THAT_ONE} không?",
            "D": f"{THEN} có phải đó là {MIND} {THAT} không?",
            "PD": f"{THEN} có phải đó là {MIND} {THAT} {OF} {THAT_ONE} không?"}
ATK_Q_RE = re.compile(
    r"([Yy]assa|yaṃ)( vā pana)?( yaṃ)? cittaṃ (na )?(uppajjamānaṃ|nirujjhamānaṃ) khaṇaṃ khaṇaṃ vītikkantaṃ "
    r"atikkantakālaṃ, (na )?(uppajjamānaṃ|nirujjhamānaṃ) khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ "
    r"(tassa taṃ|tassa|taṃ) citta(?:ṃ|nti)")
STATUS = {"vītikkantaṃ": PASSED, "avītikkantaṃ": NOT_PASSED}
STATUS_SLIPS = {"vītakkantaṃ": "vītikkantaṃ"}                 # 8 ^6-8-83 first answer: slip, rendered as meant
BARE_THING = "cái"                                            # (12) / (13) "(Ka) uppannaṃ uppajjamānaṃ?" (no subject)


def passed_phrase(negative, part):
    """uppajjamānaṃ khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ = «đã vượt khỏi khoảnh khắc đang sinh khởi, khoảnh
    khắc ấy thuộc thời đã qua»; with "na": «chưa vượt khỏi …, khoảnh khắc ấy không thuộc thời đã qua»."""
    return f"{NOT_PASSED if negative else PASSED} {MOMENT_PROG[part]}, {NOT_GONE if negative else GONE}"


def mode_of(rel, yam):
    if _lc(rel) == "yassa":
        return "PD" if yam else "P"
    if yam:
        raise ValueError("yaṃ yaṃ")
    return "D"


def question(q, label=None):
    """One question (without '?') → Vietnamese ending «… không?»."""
    lab = f"{S.LABEL[label]} " if label else ""
    if m := ATK_Q_RE.fullmatch(q):
        mode, kha = mode_of(m.group(1), m.group(3)), bool(m.group(2))
        if m.group(8) != RES[mode]:
            raise ValueError(f"correlative mismatch: {q!r}")
        open_ = f"{AT} {WHO} mà {MIND}" if mode != "D" else MIND
        if mode != "P":
            open_ += f" {WHICH}"
        s = (f"{open_} {passed_phrase(bool(m.group(4)), m.group(5))}, "
             f"{passed_phrase(bool(m.group(6)), m.group(7))}, {ATK_TAIL[mode]}")
        return lab + (f"{VA_PANA} {s[0].lower() + s[1:]}" if kha else cap(s))
    if m := re.fullmatch(r"(na )?(\S+) (na )?(\S+)", q):       # (12) / (13): uppannaṃ uppajjamānaṃ?
        if m.group(2) in VKEY and m.group(4) in VKEY:
            a = neg(m.group(2)) if m.group(1) else pos(m.group(2))
            b = neg(m.group(4)) if m.group(3) else pos(m.group(4))
            return lab + f"Có phải {BARE_THING} {a} {THEN} {b} không?"
    m = Q_HEAD_RE.fullmatch(q)
    if not m:
        raise ValueError(f"unknown question {q!r}")
    mode, kha, rest = mode_of(m.group(1), m.group(3)), bool(m.group(2)), m.group(4)
    if label and (label == "Kha") != kha:
        raise ValueError(f"label / vā pana mismatch: {q!r}")
    res = RES[mode]
    if " no ca " in rest:                                       # (11) atītānāgata
        a, b = rest.split(" no ca ", 1)
        nb, c = b.split(", ", 1)
        if not (nb.startswith(res + " ") and c.startswith(res + " ")):
            raise ValueError(f"correlative mismatch: {q!r}")
        s1, p1 = parse_sp(a)
        s2, p2 = parse_sp(nb[len(res) + 1:])
        s3, p3 = parse_sp(c[len(res) + 1:])
        if not s1 == s2 == s3:
            raise ValueError(f"subject mismatch: {q!r}")
        sv = mind_vi(s1)
        a_vi = f"{subj(mode, 1, sv)} {pred_vi(p1)} {BUT} {no_ca_vi(res, sv, p2)}"
        return lab + frame(mode, kha, a_vi, f"{subj(mode, 2, sv)} {pred_vi(p3)}")
    a, c = rest.rsplit(f" {res} ", 1)
    s1, p1 = parse_sp(a)
    s3, p3 = parse_sp(c)
    if s1 != s3:
        raise ValueError(f"subject mismatch: {q!r}")
    sv = mind_vi(s1)
    return lab + frame(mode, kha, f"{subj(mode, 1, sv)} {pred_vi(p1)}", f"{subj(mode, 2, sv)} {pred_vi(p3)}")


# ---------------------------------------------------------------------------------------------------------------
# 5. Answer sentences
# ---------------------------------------------------------------------------------------------------------------
NO_CA_RES = {"tesaṃ": f"{AT} {PRON['tesaṃ']}", "taṃ": None, "tassa taṃ": None, "": ""}


def atk_answer(core):
    """Atikkantakāla answers: 'Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītikkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ
    cittaṃ uppādakkhaṇañca vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ'."""
    out = []
    for clause in core.split(", "):
        w = clause.split()
        k = w.index("cittaṃ")
        subject, rest, pairs, i = kind_subject(w[:k]), w[k + 1:], [], 0
        while i < len(rest):
            conj = None
            if rest[i] == "no":
                if rest[i + 1] != "ca":
                    raise ValueError(clause)
                conj, i = "no ca", i + 2
            mom, st = rest[i], rest[i + 1]
            i += 2
            if st in STATUS_SLIPS:
                SLIPS_SEEN.append((st, STATUS_SLIPS[st]))
                st = STATUS_SLIPS[st]
            both = mom.endswith("ñca")
            mom = mom[:-3] + "ṃ" if both else mom
            pairs.append((conj, both, MOMENT_ACC[mom], st))
        vi = ""
        for n, (conj, both, mom, st) in enumerate(pairs):
            if conj == "no ca":
                if st != "avītikkantaṃ":
                    raise ValueError(clause)
                vi += f" {BUT} {STILL_PASSED} {mom}"
            elif n == 0:
                vi = f"{STATUS[st]} {mom}"
            elif both and pairs[n - 1][1]:
                vi += f" {AND} {STATUS[st]} {mom}"
            else:
                vi += f" mà {STATUS[st]} {mom}"
        out.append(f"{subject} {vi}")
    return cap(", ".join(out))


def body_vi(body, mode_res):
    """'<pred>[, <pred>]' or '<pred>, no ca <res> <subject> <pred>'."""
    if ", no ca " in body:
        a, b = body.split(", no ca ", 1)
        for r in ("tassa taṃ", "tesaṃ", "taṃ"):
            if b.startswith(r + " "):
                res, b = r, b[len(r) + 1:]
                break
        else:
            res = ""
        if mode_res is not None and res != mode_res:
            raise ValueError(f"'no ca {res}' after a '{mode_res}' answer: {body!r}")
        if res == "":
            return f"{pred_vi(ptoks(a))}, {BUT} {no_ca_vi('', None, ptoks(b))}"
        s, p = parse_sp(b)
        return f"{pred_vi(ptoks(a))}, {BUT} {no_ca_vi(res, mind_vi(s), p)}"
    return ", ".join(pred_vi(ptoks(x)) for x in body.split(", "))


def sentence(s):
    """One answer sentence (ends with «.», or a cut «…pe….») → Vietnamese."""
    if s in EXACT:
        return EXACT[s]
    if re.fullmatch(r"\S+\.", s) and s[:-1].lower() in VKEY:
        return verb_answer(s[:-1].lower())
    if not s.endswith("."):
        raise ValueError(f"sentence without '.': {s!r}")
    core, cut = s[:-1], False
    if core.endswith("…pe…"):
        core, cut = core[:-len("…pe…")], True
    if "kkantaṃ" in core:                                       # atikkantakāla answers
        return atk_answer(core) + "."
    if core.split()[-1] == "cittaṃ":                            # "Atītaṃ cittaṃ." (a kind of mind named)
        return cap(kind_subject(core.split()[:-1])) + "."
    w = core.split()
    if "tesaṃ" in w:                                            # puggala answers
        k = w.index("tesaṃ")
        parts = head_vi(w[:k])
        rest = " ".join(w[k + 1:])
        if cut:
            if rest:
                raise ValueError(s)
            return cap(", ".join(parts)) + f", {THEN} {AT} {PRON['tesaṃ']}{PE}"
        sw, pw = parse_sp(rest)
        rest_words = rest.split()
        body = " ".join(rest_words[rest_words.index("cittaṃ") + 1:])
        out = f"{cap(', '.join(parts))}, {THEN} {AT} {PRON['tesaṃ']} {mind_vi(sw)} {body_vi(body, 'tesaṃ')}"
        return out + (PE if cut else ".")
    if cut:
        raise ValueError(f"cut sentence outside the puggala frame: {s!r}")
    if "cittaṃ" in w:                                           # dhammavāra / puggaladhammavāra answers
        k = w.index("cittaṃ")
        body = " ".join(w[k + 1:])
        return f"{cap(kind_subject(w[:k]))} {body_vi(body, None)}."   # no ca taṃ / tassa taṃ / bare
    if _lc(w[0]) in MOMENT:                                     # (12) / (13) bare answers
        return f"{cap(moment_phrase(w[0]))} {THEN} {body_vi(' '.join(w[1:]), '')}."
    raise ValueError(f"unknown sentence {s!r}")


def sentences(rest):
    parts = [x for x in re.split(r"(?<=\.) ", rest.strip()) if x]
    return " ".join(sentence(x) for x in parts)


# ---------------------------------------------------------------------------------------------------------------
# 6. Cut chains (uddesa special cases), editorial notes, fixed lines
# ---------------------------------------------------------------------------------------------------------------
CHAIN_SEP = re.compile(r"(…pe…\.?|…)")


def chain_clause(t):
    """'yassa sarāgaṃ cittaṃ uppajjati' / 'Yassa akusalaṃ cittaṃ uppajjati na nirujjhati' → «ở người nào mà …»."""
    m = re.fullmatch(r"([Yy])assa (.+)", t)
    if not m:
        raise ValueError(f"unknown chain clause {t!r}")
    s, p = parse_sp(m.group(2))
    vi = f"{AT} {WHO} mà {mind_vi(s)} {pred_vi(p)}"
    return cap(vi) if m.group(1) == "Y" else vi


def chain(body):
    """'Yassa X cittaṃ uppajjati…pe… yassa Y cittaṃ uppajjati… …?' → «Ở người nào mà … sinh khởi… … không?»."""
    q = body.endswith("?")
    if q:
        body = body[:-1]
    out = []
    for n, piece in enumerate(CHAIN_SEP.split(body)):
        if n % 2:
            out.append(PE)
            continue
        if not piece.strip():
            out.append(piece)
            continue
        lead = piece[:len(piece) - len(piece.lstrip())]
        tail = piece[len(piece.rstrip()):]
        out.append(lead + chain_clause(piece.strip()) + tail)
    vi = "".join(out)
    return vi + (" không?" if q else "")


CONFLICT = "loại có xung đột và không có xung đột"            # saraṇaaraṇā (termbase)
SHOULD_DRAW = "Theo cách này, cần nêu ra cho đến"             # Etena upāyena yāva … uddharitabbā
FIXED = {
    "(Etena upāyena yāva saraṇaaraṇā uddharitabbā.)": f"({SHOULD_DRAW} {CONFLICT}.)",
    "(Yassa cittake sakabhāvena niddiṭṭhe, yaṃ cittake ca yassa yaṃ cittake ca ekattena niddiṭṭhe.)":
        (f"(Phần “{AT} {WHO} mà {MIND}” được trình bày theo bản chất riêng của nó, còn phần “{MIND} {WHICH}” "
         f"và phần “{AT} {WHO} mà {MIND} {WHICH}” được trình bày như là một.)"),
    "(Mūlayamakaṃ cittayamakaṃ dhammayamakanti tīṇi yamakāni yāva saraṇaaraṇā gacchanti.)":
        (f"(“{S.yamaka_title('Mūla')}”, “{S.yamaka_title('Citta')}”, “{S.yamaka_title('Dhamma')}”: "
         f"ba phần này đi đến tận {CONFLICT}.)"),
    "Cittayamakaṃ niṭṭhitaṃ.": S.yamaka_end("Citta"),
    "Yassa vā pana…pe…? Āmantā …pe….": f"{VA_PANA} {AT} {WHO} mà{PE} không? {YES[:-1]} {PE}",
}

# ---------------------------------------------------------------------------------------------------------------
# 7. Headings (termbase; S.LATER_HEADINGS where they cover the word)
# ---------------------------------------------------------------------------------------------------------------
LATER = dict(S.LATER_HEADINGS)
VARO = {   # (n) <X>vāro of the fourteen time sections
    "Uppādanirodhakālasambhedavāro": "Mục về sự kết hợp các thời của sự sinh khởi và sự chấm dứt",
    "Uppāduppannavāro": "Mục về sự sinh khởi và trạng thái đã sinh khởi",
    "Nirodhuppannavāro": "Mục về sự chấm dứt và trạng thái đã sinh khởi",
    "Uppādavāro": cap(LATER["uppādavāro"]),
    "Nirodhavāro": cap(LATER["nirodhavāro"]),
    "Uppādanirodhavāro": "Mục về sự sinh khởi và sự chấm dứt",
    "Uppajjamāna-nanirodhavāro": "Mục về trạng thái đang sinh khởi và sự không chấm dứt",
    "Uppajjamānananirodhavāro": "Mục về trạng thái đang sinh khởi và sự không chấm dứt",
    "Uppajjamānuppannavāro": "Mục về trạng thái đang sinh khởi và trạng thái đã sinh khởi",
    "Nirujjhamānuppannavāro": "Mục về trạng thái đang chấm dứt và trạng thái đã sinh khởi",
    "Uppannuppādavāro": "Mục về trạng thái đã sinh khởi và sự sinh khởi",
    "Atītānāgatavāro": "Mục về quá khứ và tương lai",
    "Uppannuppajjamānavāro": "Mục về trạng thái đã sinh khởi và trạng thái đang sinh khởi",
    "Niruddhanirujjhamānavāro": "Mục về trạng thái đã chấm dứt và trạng thái đang chấm dứt",
    "Atikkantakālavāro": "Mục về thời đã qua",
}
HEADINGS = {
    "Cittayamakaṃ": S.yamaka_title("Citta"),
    "(Ka) uddeso": f"{S.LABEL['Ka']} {S.UDDESO}",
    "(Kha) niddeso": f"{S.LABEL['Kha']} {S.NIDDESO}",
    "Suddhacittasāmaññaṃ": "Tâm thuần túy nói chung",
    "Suddhacittasāmañña": "Tâm thuần túy nói chung",
    "Puggalavāro": "Mục về người",
    "Dhammavāro": "Mục về hiện tượng",
    "Puggaladhammavāro": "Mục về người và hiện tượng",
    "Suttantacittamissakaviseso": "Trường hợp đặc biệt kết hợp với các loại tâm theo kinh",
    "Abhidhammacittamissakaviseso": "Trường hợp đặc biệt kết hợp với các loại tâm theo Vi Diệu Pháp",
}


def heading(text):
    if text in HEADINGS:
        return HEADINGS[text]
    if m := re.fullmatch(r"\((\d+)\) (\S+)", text):
        if m.group(2) in VARO:
            return f"({m.group(1)}) {VARO[m.group(2)]}"
    raise ValueError(f"unknown heading {text!r}")


# ---------------------------------------------------------------------------------------------------------------
# 8. Line translator
# ---------------------------------------------------------------------------------------------------------------
def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    elif body in FIXED:
        out = FIXED[body]
    elif re.fullmatch(r"\(\d+\) \S+vāro", body):                 # a section title run into a segment (^6-8-82)
        out = heading(body)
    elif re.match(r"Yassa ", body) and "…" in body and " tassa " not in body:
        out = chain(body)
    elif "?" in body:
        q, rest = body.split("?", 1)
        lm = re.match(r"\((Ka|Kha)\) ", q)
        label = lm.group(1) if lm else None
        if lm:
            q = q[lm.end():]
        out = question(q, label)
        if rest.strip():
            out += " " + sentences(rest)
    else:
        out = sentences(body)
    return f"{out} {bid}" if bid else out


def build(name=CHAPTER):
    return [[tr_line(ln) for ln in seg] for seg in S.segments_of(name)]


# ---------------------------------------------------------------------------------------------------------------
# 9. Strings taken from pi-1 … pi-5 rails (asserted) and the strings shared with 7-01 (checked when it is present)
# ---------------------------------------------------------------------------------------------------------------
REUSED = [
    ("Āmantā.", YES, "5"),
    ("Natthi.", ANS_NATTHI, "3"),
    ("Uppādakkhaṇe … bhaṅgakkhaṇe … (pi-5 11-tatiyavaggo ^5-366)", "vào khoảnh khắc sinh khởi", "5"),
    ("bhaṅgakkhaṇe", "vào khoảnh khắc tan rã", "5"),
    ("sarāgaṃ … avimuttaṃ cittaṃ (pi-2 7-satipatthanavibhango)", "tâm có tham đắm", "2"),
] + [(f"{k}aṃ cittaṃ", f"{MIND} {v}", "2") for k, v in list(MIND_ADJ.items())[1:16]] + [
    ("saraṇā dhammā", "các hiện tượng có xung đột", "1"),
    ("araṇā dhammā", "các hiện tượng không có xung đột", "1"),
    ("sukhāya vedanāya sampayuttā dhammā", "gắn liền với cảm giác dễ chịu", "1"),
    ("Asaññasattānaṃ (beings)", "chúng sinh Vô Tưởng", "5"),
    ("vītikkanto", "đã vượt khỏi", "2"),
]


def check_reused():
    texts = {}
    for b, d in S.RAILS.items():
        texts[b] = unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def check_shared_with_7_01():
    """The coordinator shell and answer words must equal 7-01's (family C) where both builders define them."""
    try:
        C = importlib.import_module("build_rails_7-01_vi")
    except ModuleNotFoundError:
        print("7-01 builder not present: shared-string check skipped")
        return
    pairs = [("AT", AT, C.AT), ("THEN", THEN, C.THEN), ("BUT", BUT, C.BUT), ("STILL", STILL, C.STILL),
             ("VA_PANA", VA_PANA, C.VA_PANA), ("ANS_NO", ANS_NO, C.ANS_NO), ("ANS_NATTHI", ANS_NATTHI, C.ANS_NATTHI),
             ("PRON tassa", PRON["tassa"], C.PRON["tassa"]), ("PRON tesaṃ", PRON["tesaṃ"], C.PRON["tesaṃ"])]
    for k in ("uppajjati", "uppajjittha", "uppajjissati"):
        pairs.append((k, VERB_POS[k], C.FAMILY_TERMS[k]))
    mine = frame("P", False, "A", "B")
    theirs = C.pair_q("yassa", "A", "B")
    pairs.append(("person shell", mine, theirs))
    bad = [x for x in pairs if x[1] != x[2]]
    assert not bad, "strings differ from 7-01: " + repr(bad)
    print("shared strings equal to 7-01:", len(pairs))


# ---------------------------------------------------------------------------------------------------------------
# 10. Notes file (Pāli = tiếng Việt)
# ---------------------------------------------------------------------------------------------------------------
def notes():
    out = ["# Rails 8 (Cittayamaka): family D frames and fixed strings", "",
           "Generated by build_rails_8_vi.py (family D setter). Later chapters import the module "
           "(`import build_rails_8_vi as D` with rails\\ on sys.path) and take these strings from it; never retype "
           "them. (pi-N) = taken unchanged from that book's approved rails (asserted)."]

    def h(t):
        out.extend(["", f"## {t}", ""])

    def row(p, v):
        out.append(f"{p} = {v}")

    h("Verbs in their aspects (VERB_POS / VERB_NEG; -ti, -ñca, -ñceva forms the same)")
    for k in VERB_POS:
        row(f"{k} / na {k}", f"{VERB_POS[k]} / {VERB_NEG[k]}")
    row("no ca … na V", f"{STILL} V  (e.g. no ca tesaṃ cittaṃ na uppannaṃ = {AT} {PRON['tesaṃ']} {MIND} "
                        f"{still('uppannaṃ')})")
    row("A na B / na A B (two verbs, one subject)", f"A {BUT} không B / không A {BUT} B  (e.g. "
        f"{pred_vi(['uppajjati', 'na', 'nirujjhati'])})")
    row("A ceva B ca / Añceva Bñca", f"{BOTH} A {BOTH} B  (e.g. {pred_vi(ptoks('uppannañceva uppajjati ca'))})")
    row("na ceva A na ca B", f"không A, {ALSO} không B  (e.g. {pred_vi(ptoks('na ceva uppajjati na ca uppannaṃ'))})")
    h("Answers")
    for p, v in EXACT.items():
        row(p, v)
    for v in ("Uppajjittha", "Nirujjhittha", "Uppajjissati", "Nirujjhissati", "Nirujjhati", "Uppannaṃ"):
        row(f"{v}.", verb_answer(v.lower()))
    h("Question frames")
    row("(Ka) yassa cittaṃ A tassa cittaṃ B(ti)?", f"{S.LABEL['Ka']} {frame('P', False, f'{MIND} A', f'{MIND} B')}")
    row("(Kha) yassa vā pana cittaṃ B tassa cittaṃ A(ti)?", f"{S.LABEL['Kha']} {frame('P', True, f'{MIND} B', f'{MIND} A')}")
    row("(Ka) yaṃ cittaṃ A taṃ cittaṃ B(ti)?", f"{S.LABEL['Ka']} {frame('D', False, f'{MIND} {WHICH} A', f'{MIND} {THAT} B')}")
    row("(Kha) yaṃ vā pana cittaṃ …", f"{S.LABEL['Kha']} {frame('D', True, f'{MIND} {WHICH} B', f'{MIND} {THAT} A')}")
    row("(Ka) yassa yaṃ cittaṃ A tassa taṃ cittaṃ B(ti)?",
        f"{S.LABEL['Ka']} {frame('PD', False, f'{MIND} {WHICH} A', f'{MIND} {THAT} B')}")
    row("Yassa sarāgaṃ cittaṃ … (no label; kinds of mind)", question(
        "Yassa sarāgaṃ cittaṃ uppajjati na nirujjhati tassa sarāgaṃ cittaṃ nirujjhissati na uppajjissatīti"))
    for q in ("yassa cittaṃ uppajjittha no ca tassa cittaṃ uppannaṃ, tassa cittaṃ uppajjissati",
              "yaṃ cittaṃ na uppajjittha no ca taṃ cittaṃ na uppannaṃ, taṃ cittaṃ na uppajjissati",
              "yassa yaṃ cittaṃ uppajjittha no ca tassa taṃ cittaṃ uppannaṃ, tassa taṃ cittaṃ uppajjissati",
              "uppannaṃ uppajjamānaṃ", "na niruddhaṃ na nirujjhamānaṃ",
              "yassa cittaṃ uppajjamānaṃ khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ, nirujjhamānaṃ khaṇaṃ khaṇaṃ "
              "vītikkantaṃ atikkantakālaṃ tassa cittaṃ",
              "yaṃ cittaṃ na uppajjamānaṃ khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ, na nirujjhamānaṃ khaṇaṃ khaṇaṃ "
              "vītikkantaṃ atikkantakālaṃ taṃ cittaṃ"):
        row(f"(Ka) {q}?", question(q, "Ka"))
    row("tassa cittaṃ? / taṃ cittaṃ? / tassa taṃ cittaṃ? (atikkantakāla tail)", " / ".join(ATK_TAIL.values()))
    h("Answer heads, subjects")
    row("<head> tesaṃ cittaṃ …", f"<Head>, {THEN} {AT} {PRON['tesaṃ']} {MIND} …")
    for r in ("tesaṃ", "tassa", "taṃ", "tassa taṃ"):
        row(f"…, no ca {r} cittaṃ uppajjati / na uppannaṃ",
            f"…, {BUT} {no_ca_vi(r, MIND, ['uppajjati'])} / {BUT} {no_ca_vi(r, MIND, ['na', 'uppannaṃ'])}")
    row("…, no ca uppajjamānaṃ / no ca na uppannaṃ (bare)",
        f"…, {BUT} {no_ca_vi('', None, ['uppajjamānaṃ'])} / {BUT} {no_ca_vi('', None, ['na', 'uppannaṃ'])}")
    for k, v in PERSON.items():
        row(k, f"{AT} {v}")
    row("Itaresaṃ cittasamaṅgīnaṃ", f"{AT} {OTHERS_WITH_MIND}")
    row("nirodhasamāpannānaṃ asaññasattānaṃ", f"{AT} {PERSON['nirodhasamāpannānaṃ']} {AND} {PERSON['asaññasattānaṃ']}")
    for g in ("Cittassa", "Pacchimacittassa", "Sarāgapacchimacittassa", "sarāgacittassa", "Pacchimakusalacittassa"):
        row(f"{g} uppādakkhaṇe", moment_phrase("uppādakkhaṇe", g))
    row("Cittassa bhaṅgakkhaṇe", moment_phrase("bhaṅgakkhaṇe", "Cittassa"))
    row("Bhaṅgakkhaṇe / Uppādakkhaṇe (bare, (12) (13))", f"{cap(moment_phrase('bhaṅgakkhaṇe'))} {THEN} … / "
        f"{cap(moment_phrase('uppādakkhaṇe'))} {THEN} …")
    for ws in (["Bhaṅgakkhaṇe"], ["Atītaṃ"], ["Paccuppannaṃ"], ["Atītānāgataṃ"], ["Bhaṅgakkhaṇe", "anāgatañca"],
               ["Uppādakkhaṇe", "anāgatañca"], ["Bhaṅgakkhaṇe", "atītañca"], ["Uppādakkhaṇe", "anāgataṃ"]):
        row(" ".join(ws) + " cittaṃ", cap(kind_subject(ws)))
    h("Kinds of mind (subject «tâm …»)")
    for k, v in MIND_ADJ.items():
        row(f"{k}ṃ cittaṃ" if " " not in k else f"{k}ṃ cittaṃ", f"{MIND} {v}")
    row("pacchima- (… cittassa)", f"{MIND} … {FINAL}")
    h("Atikkantakāla answers")
    row("uppādakkhaṇaṃ vītikkantaṃ / avītikkantaṃ / no ca … avītikkantaṃ",
        f"{PASSED} … / {NOT_PASSED} … / {BUT} {STILL_PASSED} …")
    row("A … B … (juxtaposed) / Añca … Bñca …", "… mà … / … và …")
    h("Headings")
    for p, v in HEADINGS.items():
        row(p, v)
    for p, v in VARO.items():
        row(p, v)
    h("Fixed lines")
    for p, v in FIXED.items():
        row(p, v)
    h("Strings shared with 2-01 (families A, B) and 7-01 (family C): the coordinator aligns these")
    row("AT / THEN / BUT / STILL / ALSO / VA_PANA", " / ".join((AT, THEN, BUT, STILL, ALSO, VA_PANA)))
    row("tassa / tesaṃ", " / ".join(PRON.values()))
    row("No. / Natthi. / Āmantā.", f"{ANS_NO} / {ANS_NATTHI} / {YES}")
    row("uppajjati / uppajjittha / uppajjissati", " / ".join(VERB_POS[k] for k in ("uppajjati", "uppajjittha", "uppajjissati")))
    row("nirujjhati / nirujjhittha / nirujjhissati", " / ".join(VERB_POS[k] for k in ("nirujjhati", "nirujjhittha", "nirujjhissati")))
    row("na uppajjati / na uppajjittha / na uppajjissati (separate na)",
        " / ".join(VERB_NEG[k] for k in ("uppajjati", "uppajjittha", "uppajjissati")))
    row("na nirujjhati / na nirujjhittha / na nirujjhissati (separate na)",
        " / ".join(VERB_NEG[k] for k in ("nirujjhati", "nirujjhittha", "nirujjhissati")))
    row("one-word verb answers", f"{verb_answer('uppajjittha')} / {verb_answer('nirujjhati')} (present: «{HAS} …»)")
    row("person answer head + resumptive tesaṃ", f"«{cap(AT)} <người>, {THEN} {AT} {PRON['tesaṃ']} {MIND} …»")
    row("two person groups juxtaposed", f"«{AT} <A> {AND} <B>»")
    row("nirodhasamāpannānaṃ / asaññasattānaṃ / Itaresaṃ",
        f"{PERSON['nirodhasamāpannānaṃ']} / {PERSON['asaññasattānaṃ']} / {PERSON['itaresaṃ']}")
    out.append("")
    return "\n".join(out)


def main():
    check_reused()
    check_shared_with_7_01()
    segs = build()
    S.write(CHAPTER, segs)
    ADH_DIR.mkdir(exist_ok=True)                              # termbase-adherence copy (byte-identical)
    (ADH_DIR / CHAPTER).write_bytes((S.OUT_DIR / CHAPTER).read_bytes())
    print("wrote", ADH_DIR / CHAPTER)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    if SLIPS_SEEN:
        print("slips rendered as meant:", sorted(set(SLIPS_SEEN)))


if __name__ == "__main__":
    main()
