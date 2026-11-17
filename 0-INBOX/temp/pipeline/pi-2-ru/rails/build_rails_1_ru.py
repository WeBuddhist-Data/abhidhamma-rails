"""Builder for the Russian rails translation of pi-2 (Vibhaṅga, plain audience), chapter 1 (Khandhavibhaṅgo).

Writes (only when run as a script):
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/1-khandhavibhango.md
      = 0-INBOX/temp/pipeline/pi-2-ru/rails/sample-1/1-sample.md (byte-for-byte, ^2-1-0 … ^2-33)
        + the rest of the chapter (^2-1-2-2-0 … ^2-153) built here
  0-INBOX/temp/pipeline/pi-2-ru/rails/notes-1.md   (new recurring formulas, Pāli = Russian)

Every Russian string comes from the fixed tables and functions below, so identical Pāli gives identical Russian.
The approved sample builder is imported read-only (S); the pi-1 matrix names (pi-1 build_rails_sample_ru.py, P1)
are the base of the matrix predicates: ITEMS holds each matrix item in the forms the Vibhaṅga needs
(feminine singular for «совокупность», plural for «четыре совокупности», instrumental after «бывает» /
«является», finite predicates for the question section). check_pi1() compares them with the pi-1 names.

Later chapters import this module (importing writes nothing):
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-2-ru\\rails")
    import build_rails_1_ru as K1
    K1.ITEMS, K1.item(key), K1.atthi(key, g), K1.abhi_line(p), K1.panha_line(p, subjects),
    K1.panha_question(p, groups), K1.SUBJ, K1.GROUP_GEN, K1.FIXED, K1.APARO, K1.DUKAMULA, K1.TIKAMULA, K1.UBHATO

usage: python -I -X utf8 build_rails_1_ru.py
"""
import importlib.util
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)

_P1_PATH = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails\build_rails_sample_ru.py")
_spec = importlib.util.spec_from_file_location("pi1_build_rails_sample_ru", _P1_PATH)
P1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P1)       # importing writes nothing

PART = "1-khandhavibhango.md"
SRC = S.PALI / PART
TARGET = S.OUT / PART
SAMPLE_RU = S.SAMPLE / "1-sample.md"
NOTES_PATH = RAILS / "notes-1.md"
cap, KH = S.cap, S.KH
SLIPS = []          # source slips met while building (reported)


def low(s):
    return s[0].lower() + s[1:]


# =========================================================================== Russian inflection of the item phrases
_HUSH = "гкхжшщч"


def _wpl(w):            # feminine nominative singular -> nominative plural
    if w.endswith("аяся"):
        return w[:-4] + "иеся"
    if w.endswith("яя"):
        return w[:-2] + "ие"
    if w.endswith("ая"):
        s = w[:-2]
        return s + ("ие" if s[-1] in _HUSH else "ые")
    return w


def _wins(w):           # feminine nominative singular -> feminine instrumental singular
    if w.endswith("аяся"):
        return w[:-4] + "ейся"
    if w.endswith("яя"):
        return w[:-2] + "ей"
    if w.endswith("ая"):
        s = w[:-2]
        return s + ("ей" if s[-1] in "жшщчц" else "ой")
    return w


def _wnins(w):          # feminine nominative singular -> masculine / neuter instrumental singular
    if w.endswith("аяся"):
        return w[:-4] + "имся"
    if w.endswith("яя"):
        return w[:-2] + "им"
    if w.endswith("ая"):
        s = w[:-2]
        return s + ("им" if s[-1] in _HUSH else "ым")
    return w


def _winsp(w):          # nominative plural -> instrumental plural
    if w.endswith("иеся"):
        return w[:-4] + "имися"
    if w.endswith("ые"):
        return w[:-2] + "ыми"
    if w.endswith("ие") and w not in ("явление",):
        return w[:-2] + "ими"
    return w


def _infl(phrase, fn):
    return re.sub(r"[А-Яа-яЁё]+", lambda m: fn(m.group(0)), phrase)


CONJ = {"является": "являются", "связана": "связаны", "имеет": "имеют", "сопровождается": "сопровождаются",
        "устраняется": "устраняются", "ведёт": "ведут", "относится": "относятся", "принадлежит": "принадлежат",
        "служит": "служат", "сопутствует": "сопутствуют", "способна": "способны", "подвержена": "подвержены",
        "затронута": "затронуты", "свободна": "свободны", "порождена": "порождены", "соединена": "соединены",
        "следует": "следуют", "сосуществует": "сосуществуют", "познаваема": "познаваемы", "охвачена": "охвачены",
        "находится": "находятся", "омрачена": "омрачены"}


def conj(v):
    """finite predicate singular -> plural (verbs and short forms only; nouns stay)"""
    return " ".join(CONJ.get(w, w) for w in v.split(" "))


# =========================================================================== matrix items
# key = Pāli masculine singular (as said of «-kkhandho»); value = dict of Russian forms:
#   f    nominative feminine singular (agrees with «совокупность»; used inside «…» quotes for a singular subject)
#   pl   nominative plural (quotes for a plural subject; = the pi-1 matrix name without «явления»)
#   ins  feminine instrumental singular (after «бывает» / «является»)
#   nins masculine / neuter instrumental singular (after «который / которое бывает»)
#   insp instrumental plural (after «являются»)
#   v / vp  finite predicate, singular / plural subject (question section, «по одному – …»)
ITEMS = {}


def A(f, v=None, pl=None, vp=None, ins=None, insp=None, nins=None):
    """adjective / participle item"""
    pl = pl or _infl(f, _wpl)
    ins = ins or _infl(f, _wins)
    insp = insp or _infl(pl, _winsp)
    nins = nins or _infl(f, _wnins)
    if v is None:
        v, vp = f"является {ins}", vp or f"являются {insp}"
    else:
        vp = vp or conj(v)
    return dict(f=f, pl=pl, ins=ins, insp=insp, nins=nins, v=v, vp=vp)


def P(tail):
    """«явление с …» item (matrix names with a prepositional phrase; sample «является явлением с …»)"""
    return dict(f=f"явление {tail}", pl=f"явления {tail}", ins=f"явлением {tail}", insp=f"явлениями {tail}",
                nins=f"явлением {tail}", v=f"является явлением {tail}", vp=f"являются явлениями {tail}")


def N(ins_s, ins_p=None, neg=False):
    """noun item («корнем», «влечением»): «бывает корнем», «является корнем», quote «являющаяся корнем»"""
    ins_p = ins_p or ins_s
    ne = "не " if neg else ""
    return dict(f=f"{ne}являющаяся {ins_s}", pl=f"{ne}являющиеся {ins_p}", ins=f"{ne}{ins_s}", insp=f"{ne}{ins_p}",
                nins=f"{ne}{ins_s}", v=f"{ne}является {ins_s}", vp=f"{ne}являются {ins_p}")


def _put(**kw):
    ITEMS.update(kw)


T = {}  # triads (Pāli keys in matrix order) – exported for later chapters
T["kusala"] = ["kusalo", "akusalo", "abyākato"]
ITEMS["kusalo"] = A("благая")
ITEMS["akusalo"] = A("неблагая")
ITEMS["abyākato"] = A("этически неопределённая")
T["vedana"] = ["sukhāya vedanāya sampayutto", "dukkhāya vedanāya sampayutto", "adukkhamasukhāya vedanāya sampayutto"]
for _k, _t in zip(T["vedana"], ["с приятным чувством", "с болезненным чувством", f"с {S.ADM_INS}"]):
    ITEMS[_k] = A(f"связанная {_t}", v=f"связана {_t}")
T["vipaka"] = ["vipāko", "vipākadhammadhammo", "nevavipākanavipākadhammadhammo"]
ITEMS["vipāko"] = A("являющаяся результатом действий", ins="результатом действий", insp="результатом действий",
                    nins="результатом действий", v="является результатом действий", vp="являются результатом действий")
ITEMS["vipākadhammadhammo"] = A("способная приносить результаты", v="способна приносить результаты")
ITEMS["nevavipākanavipākadhammadhammo"] = A(
    "не являющаяся результатом действий и не способная приносить результаты",
    v="не является результатом действий и не способна приносить результаты")
T["upadinna"] = ["upādinnupādāniyo", "anupādinnupādāniyo", "anupādinnaanupādāniyo"]
ITEMS["upādinnupādāniyo"] = A("охваченная цеплянием и служащая его объектом")
ITEMS["anupādinnupādāniyo"] = A("не охваченная цеплянием, но служащая его объектом")
ITEMS["anupādinnaanupādāniyo"] = A("не охваченная цеплянием и не служащая его объектом")
T["sankilittha"] = ["saṃkiliṭṭhasaṃkilesiko", "asaṃkiliṭṭhasaṃkilesiko", "asaṃkiliṭṭhaasaṃkilesiko"]
ITEMS["saṃkiliṭṭhasaṃkilesiko"] = A("омрачённая и подверженная омрачению")
ITEMS["asaṃkiliṭṭhasaṃkilesiko"] = A("неомрачённая, но подверженная омрачению")
ITEMS["asaṃkiliṭṭhaasaṃkilesiko"] = A("неомрачённая и не подверженная омрачению")
T["vitakka"] = ["savitakkasavicāro", "avitakkavicāramatto", "avitakkaavicāro"]
ITEMS["savitakkasavicāro"] = P("с направленной мыслью и удержанием мысли")
ITEMS["avitakkavicāramatto"] = P("без направленной мысли, только с удержанием мысли")
ITEMS["avitakkaavicāro"] = P("без направленной мысли и без удержания мысли")
T["piti"] = ["pītisahagato", "sukhasahagato", "upekkhāsahagato"]
for _k, _t in zip(T["piti"], ["восторгом", "счастьем", "невозмутимостью"]):
    ITEMS[_k] = A(f"сопровождаемая {_t}", v=f"сопровождается {_t}")
    ITEMS["na " + _k] = A(f"не сопровождаемая {_t}", v=f"не сопровождается {_t}")
T["dassana"] = ["dassanena pahātabbo", "bhāvanāya pahātabbo", "neva dassanena na bhāvanāya pahātabbo"]
T["dassanahetu"] = [k + "hetuko" for k in ("dassanena pahātabba", "bhāvanāya pahātabba",
                                            "neva dassanena na bhāvanāya pahātabba")]
for _p, _t in (("dassanena", "видением истины"), ("bhāvanāya", "развитием ума")):
    ITEMS[f"{_p} pahātabbo"] = A(f"устраняемая {_t}", v=f"устраняется {_t}")
    ITEMS[f"na {_p} pahātabbo"] = A(f"не устраняемая {_t}", v=f"не устраняется {_t}")
    ITEMS[f"{_p} pahātabbahetuko"] = A(f"относящаяся к явлениям, чьи корни устраняются {_t}",
                                       v=f"относится к явлениям, чьи корни устраняются {_t}")
    ITEMS[f"na {_p} pahātabbahetuko"] = A(f"относящаяся к явлениям, чьи корни не устраняются {_t}",
                                          v=f"относится к явлениям, чьи корни не устраняются {_t}")
_NEITHER = "ни видением истины, ни развитием ума"
ITEMS["neva dassanena na bhāvanāya pahātabbo"] = A(f"не устраняемая {_NEITHER}", v=f"не устраняется {_NEITHER}")
ITEMS["neva dassanena na bhāvanāya pahātabbahetuko"] = A(
    f"относящаяся к явлениям, чьи корни не устраняются {_NEITHER}",
    v=f"относится к явлениям, чьи корни не устраняются {_NEITHER}")
T["acaya"] = ["ācayagāmī", "apacayagāmī", "nevācayagāmināpacayagāmī"]
ITEMS["ācayagāmī"] = A("ведущая к накоплению", v="ведёт к накоплению")
ITEMS["apacayagāmī"] = A("ведущая к убыванию", v="ведёт к убыванию")
ITEMS["nevācayagāmināpacayagāmī"] = A("не ведущая ни к накоплению, ни к убыванию",
                                      v="не ведёт ни к накоплению, ни к убыванию")
T["sekkha"] = ["sekkho", "asekkho", "nevasekkhanāsekkho"]
ITEMS["sekkho"] = A("относящаяся к обучающимся", v="относится к обучающимся")
ITEMS["asekkho"] = A("относящаяся к завершившим обучение", v="относится к завершившим обучение")
ITEMS["nevasekkhanāsekkho"] = A("не относящаяся ни к обучающимся, ни к завершившим обучение",
                                v="не относится ни к обучающимся, ни к завершившим обучение")
T["paritta"] = ["paritto", "mahaggato", "appamāṇo"]
_put(paritto=A("ограниченная"), mahaggato=A("возвышенная"), appamāṇo=A("безмерная"))
T["parittarammana"] = ["parittārammaṇo", "mahaggatārammaṇo", "appamāṇārammaṇo"]
_put(parittārammaṇo=P("с ограниченным объектом"), mahaggatārammaṇo=P("с возвышенным объектом"),
     appamāṇārammaṇo=P("с безмерным объектом"))
T["hina"] = ["hīno", "majjhimo", "paṇīto"]
_put(hīno=A("низшая"), majjhimo=A("средняя"), paṇīto=A("высшая"))
T["miccha"] = ["micchattaniyato", "sammattaniyato", "aniyato"]
_put(micchattaniyato=A("предопределённо ведущая к ложному", v="предопределённо ведёт к ложному"),
     sammattaniyato=A("предопределённо ведущая к правильному", v="предопределённо ведёт к правильному"),
     aniyato=A("непредопределённая"), niyato=A("предопределённая"))
T["magga"] = ["maggārammaṇo", "maggahetuko", "maggādhipati"]
_put(maggārammaṇo=A("имеющая объектом путь", v="имеет объектом путь"),
     maggahetuko=A("имеющая корнем путь", v="имеет корнем путь"),
     maggādhipati=A("находящаяся под главенством пути", v="находится под главенством пути"))
T["uppanna"] = ["uppanno", "anuppanno", "uppādī"]
_put(uppanno=A("возникшая"), anuppanno=A("невозникшая"))
ITEMS["uppādī"] = dict(f="та, которой предстоит возникнуть", pl="те, которым предстоит возникнуть",
                       ins="той, которой предстоит возникнуть", insp="теми, которым предстоит возникнуть",
                       nins="тем, которому предстоит возникнуть", v="является той, которой предстоит возникнуть",
                       vp="являются теми, которым предстоит возникнуть")
T["atita"] = ["atīto", "anāgato", "paccuppanno"]
_put(atīto=A("прошлая"), anāgato=A("будущая"), paccuppanno=A("настоящая"))
T["atitarammana"] = ["atītārammaṇo", "anāgatārammaṇo", "paccuppannārammaṇo"]
_put(atītārammaṇo=P("с прошлым объектом"), anāgatārammaṇo=P("с будущим объектом"),
     paccuppannārammaṇo=P("с настоящим объектом"))
T["ajjhatta"] = ["ajjhatto", "bahiddho", "ajjhattabahiddho"]
_put(ajjhatto=A("внутренняя"), bahiddho=A("внешняя"), ajjhattabahiddho=A("внутренняя и внешняя"))
T["ajjhattarammana"] = ["ajjhattārammaṇo", "bahiddhārammaṇo", "ajjhattabahiddhārammaṇo"]
_put(ajjhattārammaṇo=P("с внутренним объектом"), bahiddhārammaṇo=P("с внешним объектом"),
     ajjhattabahiddhārammaṇo=P("с внутренним и внешним объектом"))
T["sanidassana"] = ["sanidassanasappaṭigho", "anidassanasappaṭigho", "anidassanaappaṭigho"]
_put(sanidassanasappaṭigho=A("видимая и способная к соударению"),
     anidassanasappaṭigho=A("невидимая, но способная к соударению"),
     anidassanaappaṭigho=A("невидимая и не способная к соударению"))
TRIAD_ORDER = ["kusala", "vedana", "vipaka", "upadinna", "sankilittha", "vitakka", "piti", "dassana", "dassanahetu",
               "acaya", "sekkha", "paritta", "parittarammana", "hina", "miccha", "magga", "uppanna", "atita",
               "atitarammana", "ajjhatta", "ajjhattarammana", "sanidassana"]

# ---- dyads: roots group
ITEMS["hetu"] = N("корнем", "корнями")
ITEMS["na hetu"] = N("корнем", "корнями", neg=True)
_put(sahetuko=A("имеющая корни", v="имеет корни"), ahetuko=A("не имеющая корней", v="не имеет корней"),
     hetusampayutto=A("связанная с корнями", v="связана с корнями"),
     hetuvippayutto=A("не связанная с корнями", v="не связана с корнями"))
ITEMS["hetu ceva sahetuko ca"] = A("являющаяся корнем и имеющая корни", pl="являющиеся корнями и имеющие корни",
                                   v="является корнем и имеет корни", vp="являются корнями и имеют корни")
ITEMS["sahetuko ceva na ca hetu"] = A("имеющая корни, но не являющаяся корнем",
                                      pl="имеющие корни, но не являющиеся корнями",
                                      v="имеет корни, но не является корнем", vp="имеют корни, но не являются корнями")
ITEMS["hetu ceva hetusampayutto ca"] = A("являющаяся корнем и связанная с корнями",
                                         pl="являющиеся корнями и связанные с корнями",
                                         v="является корнем и связана с корнями",
                                         vp="являются корнями и связаны с корнями")
ITEMS["hetusampayutto ceva na ca hetu"] = A("связанная с корнями, но не являющаяся корнем",
                                            pl="связанные с корнями, но не являющиеся корнями",
                                            v="связана с корнями, но не является корнем",
                                            vp="связаны с корнями, но не являются корнями")
ITEMS["na hetu sahetuko"] = A("не являющаяся корнем, но имеющая корни", pl="не являющиеся корнями, но имеющие корни",
                              v="не является корнем, но имеет корни", vp="не являются корнями, но имеют корни")
ITEMS["na hetu ahetuko"] = A("не являющаяся корнем и не имеющая корней",
                             pl="не являющиеся корнями и не имеющие корней",
                             v="не является корнем и не имеет корней", vp="не являются корнями и не имеют корней")
# ---- lesser intermediate pairs
_put(sappaṭigho=A("способная к соударению", v="способна к соударению"),
     appaṭigho=A("не способная к соударению", v="не способна к соударению"),
     sanidassano=A("видимая"), anidassano=A("невидимая"),
     lokiyo=A("мирская"), lokuttaro=A("надмирская"))
ITEMS["rūpaṃ"] = A("материальная")             # Rūpakkhandho rūpaṃ (sample «является материальной»)
ITEMS["arūpo"] = A("нематериальная")           # Cattāro khandhā arūpā
ITEMS["kenaci viññeyyo"] = A("познаваемая тем или иным видом сознания", v="познаваема тем или иным видом сознания")
ITEMS["kenaci na viññeyyo"] = A("не познаваемая тем или иным видом сознания",
                                v="не познаваема тем или иным видом сознания")

# ---- the clusters (taints … defilements): Russian pieces follow pi-1 P1.CLUSTERS
# (noun key, prone key, notprone key, stem, ins sg, ins pl, prone f, prone v, notprone f, notprone v)
CL = {
    "āsava": ("āsavo", "sāsavo", "anāsavo", "āsava", "влечением", "влечениями",
              "подверженная влечениям", "подвержена влечениям", "свободная от влечений", "свободна от влечений"),
    "saṃyojana": ("saṃyojanaṃ", "saṃyojaniyo", "asaṃyojaniyo", "saṃyojana", "оковами", "оковами",
                  "подверженная оковам", "подвержена оковам", "не подверженная оковам", "не подвержена оковам"),
    "gantha": ("gantho", "ganthaniyo", "aganthaniyo", "gantha", "узами", "узами",
               "подверженная узам", "подвержена узам", "не подверженная узам", "не подвержена узам"),
    "ogha": ("ogho", "oghaniyo", "anoghaniyo", "ogha", "потоком", "потоками",
             "подверженная потокам", "подвержена потокам", "не подверженная потокам", "не подвержена потокам"),
    "yoga": ("yogo", "yoganiyo", "ayoganiyo", "yoga", "ярмом", "ярмами",
             "подверженная ярмам", "подвержена ярмам", "не подверженная ярмам", "не подвержена ярмам"),
    "nīvaraṇa": ("nīvaraṇaṃ", "nīvaraṇiyo", "anīvaraṇiyo", "nīvaraṇa", "помехой", "помехами",
                 "подверженная помехам", "подвержена помехам", "не подверженная помехам", "не подвержена помехам"),
    "parāmāsa": ("parāmāso", "parāmaṭṭho", "aparāmaṭṭho", "parāmāsa", "искажением", "искажениями",
                 "затронутая искажениями", "затронута искажениями",
                 "не затронутая искажениями", "не затронута искажениями"),
    "upādāna": ("upādānaṃ", "upādāniyo", "anupādāniyo", "upādāna", "цеплянием", "цепляниями",
                "служащая объектом цепляния", "служит объектом цепляния",
                "не служащая объектом цепляния", "не служит объектом цепляния"),
    "kilesa": ("kileso", "saṃkilesiko", "asaṃkilesiko", "kilesa", "омрачением", "омрачениями",
               "подверженная омрачению", "подвержена омрачению",
               "не подверженная омрачению", "не подвержена омрачению"),
}
CLUSTER_KEYS = {}   # cluster -> keys in the order of the Abhidhamma lists


def _ceva(n):
    """Pāli «X ceva»: neuter -aṃ takes «-ñceva»"""
    return n[:-1] + "ñceva" if n.endswith("ṃ") else n + " ceva"


def _cluster(c):
    n, pr, npr, st, ins_s, ins_p, prf, prv, nprf, nprv = CL[c]
    obj = ins_p                                         # «с влечениями», «с оковами» …
    ITEMS[n] = N(ins_s, ins_p)
    ITEMS["no " + n] = N(ins_s, ins_p, neg=True)
    ITEMS[pr] = A(prf, v=prv)
    ITEMS[npr] = A(nprf, v=nprv)
    ITEMS[st + "sampayutto"] = A(f"связанная с {obj}", v=f"связана с {obj}")
    ITEMS[st + "vippayutto"] = A(f"не связанная с {obj}", v=f"не связана с {obj}")
    prpl, pr_vp = _infl(prf, _wpl), conj(prv)
    ITEMS[f"{_ceva(n)} {pr} ca"] = A(f"являющаяся {ins_s} и {prf}", pl=f"являющиеся {ins_p} и {prpl}",
                                     v=f"является {ins_s} и {prv}", vp=f"являются {ins_p} и {pr_vp}")
    ITEMS[f"{pr} ceva no ca {n}"] = A(f"{prf}, но не являющаяся {ins_s}", pl=f"{prpl}, но не являющиеся {ins_p}",
                                      v=f"{prv}, но не является {ins_s}", vp=f"{pr_vp}, но не являются {ins_p}")
    ITEMS[f"{_ceva(n)} {st}sampayutto ca"] = A(f"являющаяся {ins_s} и связанная с {obj}",
                                               pl=f"являющиеся {ins_p} и связанные с {obj}",
                                               v=f"является {ins_s} и связана с {obj}",
                                               vp=f"являются {ins_p} и связаны с {obj}")
    ITEMS[f"{st}sampayutto ceva no ca {n}"] = A(f"связанная с {obj}, но не являющаяся {ins_s}",
                                                pl=f"связанные с {obj}, но не являющиеся {ins_p}",
                                                v=f"связана с {obj}, но не является {ins_s}",
                                                vp=f"связаны с {obj}, но не являются {ins_p}")
    ITEMS[f"{st}vippayutta{pr}"] = A(f"не связанная с {obj}, но {prf}", v=f"не связана с {obj}, но {prv}")
    a = "" if npr.startswith("a") else "a"
    ITEMS[f"{st}vippayutta{a}{npr}"] = A(f"не связанная с {obj} и {nprf}", v=f"не связана с {obj} и {nprv}")
    CLUSTER_KEYS[c] = [n, "no " + n, pr, npr, st + "sampayutto", st + "vippayutto", f"{_ceva(n)} {pr} ca",
                       f"{pr} ceva no ca {n}", f"{_ceva(n)} {st}sampayutto ca", f"{st}sampayutto ceva no ca {n}",
                       f"{st}vippayutta{pr}", f"{st}vippayutta{a}{npr}"]


for _c in CL:
    _cluster(_c)
# kilesa: the «defiled» pairs
_put(saṃkiliṭṭho=A("омрачённая"), asaṃkiliṭṭho=A("неомрачённая"))
ITEMS["kileso ceva saṃkiliṭṭho ca"] = A("являющаяся омрачением и омрачённая", pl="являющиеся омрачениями и омрачённые",
                                        v="является омрачением и омрачена", vp="являются омрачениями и омрачены")
ITEMS["saṃkiliṭṭho ceva no ca kileso"] = A("омрачённая, но не являющаяся омрачением",
                                           pl="омрачённые, но не являющиеся омрачениями",
                                           v="омрачена, но не является омрачением",
                                           vp="омрачены, но не являются омрачениями")

# ---- greater intermediate pairs
_put(sārammaṇo=A("имеющая объект", v="имеет объект"), anārammaṇo=A("не имеющая объекта", v="не имеет объекта"),
     cetasiko=A("сопутствующая уму", v="сопутствует уму"), acetasiko=A("не сопутствующая уму", v="не сопутствует уму"),
     cittasampayutto=A("связанная с умом", v="связана с умом"),
     cittavippayutto=A("не связанная с умом", v="не связана с умом"),
     cittasaṃsaṭṭho=A("соединённая с умом", v="соединена с умом"),
     cittavisaṃsaṭṭho=A("не соединённая с умом", v="не соединена с умом"),
     cittasamuṭṭhāno=A("порождённая умом", v="порождена умом"),
     cittasahabhū=A("сосуществующая с умом", v="сосуществует с умом"),
     cittānuparivatti=A("следующая за умом", v="следует за умом"),
     cittasaṃsaṭṭhasamuṭṭhāno=A("соединённая с умом и порождённая им", v="соединена с умом и порождена им"),
     cittasaṃsaṭṭhasamuṭṭhānasahabhū=A("соединённая с умом, порождённая им и сосуществующая с ним",
                                        v="соединена с умом, порождена им и сосуществует с ним"),
     cittasaṃsaṭṭhasamuṭṭhānānuparivatti=A("соединённая с умом, порождённая им и следующая за ним",
                                            v="соединена с умом, порождена им и следует за ним"),
     ajjhattiko=A("относящаяся к внутреннему", v="относится к внутреннему"),
     bāhiro=A("относящаяся к внешнему", v="относится к внешнему"),
     upādā=A("производная"),
     upādinno=A("охваченная цеплянием", v="охвачена цеплянием"),
     anupādinno=A("не охваченная цеплянием", v="не охвачена цеплянием"))
ITEMS["cittaṃ"] = N("умом")
ITEMS["no cittaṃ"] = N("умом", neg=True)
ITEMS["no upādā"] = A("непроизводная")
for _k in ("cittasamuṭṭhāno", "cittasahabhū", "cittānuparivatti"):
    _i = ITEMS[_k]
    ITEMS["no " + _k] = A("не " + _i["f"], v="не " + _i["v"])
for _k, _tail in (("cittasaṃsaṭṭhasamuṭṭhāno", "соединённой с умом и порождённой им"),
                  ("cittasaṃsaṭṭhasamuṭṭhānasahabhū", "соединённой с умом, порождённой им и сосуществующей с ним"),
                  ("cittasaṃsaṭṭhasamuṭṭhānānuparivatti", "соединённой с умом, порождённой им и следующей за ним")):
    _plt = {"соединённой с умом и порождённой им": "соединёнными с умом и порождёнными им",
            "соединённой с умом, порождённой им и сосуществующей с ним":
                "соединёнными с умом, порождёнными им и сосуществующими с ним",
            "соединённой с умом, порождённой им и следующей за ним":
                "соединёнными с умом, порождёнными им и следующими за ним"}[_tail]
    ITEMS["no " + _k] = A(f"не являющаяся {_tail}", pl=f"не являющиеся {_plt}",
                          v=f"не является {_tail}", vp=f"не являются {_plt}")
ITEMS["cittena sampayutto"] = ITEMS["cittasampayutto"]
ITEMS["cittena vippayutto"] = ITEMS["cittavippayutto"]
ITEMS["cittena saṃsaṭṭho"] = ITEMS["cittasaṃsaṭṭho"]
ITEMS["cittena visaṃsaṭṭho"] = ITEMS["cittavisaṃsaṭṭho"]

# ---- final pairs
_put(savitakko=P("с направленной мыслью"), avitakko=P("без направленной мысли"),
     savicāro=P("с удержанием мысли"), avicāro=P("без удержания мысли"),
     sappītiko=P("с восторгом"), appītiko=P("без восторга"))
for _k, _t in (("kāmāvacaro", "к миру чувственных желаний"), ("rūpāvacaro", "к миру форм"),
               ("arūpāvacaro", "к миру без форм")):
    ITEMS[_k] = A(f"относящаяся {_t}", v=f"относится {_t}")
    ITEMS["na " + _k] = A(f"не относящаяся {_t}", v=f"не относится {_t}")
_put(pariyāpanno=A("принадлежащая к кругам существования", v="принадлежит к кругам существования"),
     apariyāpanno=A("не принадлежащая к кругам существования", v="не принадлежит к кругам существования"),
     niyyāniko=A("ведущая к освобождению", v="ведёт к освобождению"),
     aniyyāniko=A("не ведущая к освобождению", v="не ведёт к освобождению"),
     sauttaro=A("имеющая над собой высшее", v="имеет над собой высшее"),          # termbase sauttaro (pi-1 differs)
     anuttaro=A("не имеющая над собой высшего", v="не имеет над собой высшего"),  # termbase anuttarā (pi-1 differs)
     saraṇo=A("сопряжённая с борьбой"), araṇo=A("свободная от борьбы"))

# ---- aggregate-specific classes
ITEMS["phassasampayutto"] = A("связанная с контактом", v="связана с контактом")
for _k, _t in (("sukhindriya", "удовольствия"), ("dukkhindriya", "боли"), ("somanassindriya", "радости"),
               ("domanassindriya", "уныния"), ("upekkhindriya", "невозмутимости")):
    ITEMS[_k + "ṃ"] = N(f"способностью {_t}")
    ITEMS[_k + "sampayutto"] = A(f"связанная со способностью {_t}", v=f"связана со способностью {_t}")
# said of a noun phrase (after «которое / который бывает …»)
ITEMS["sukhā#np"] = A("приятная")                         # kāyasamphassajā vedanā atthi sukhā
ITEMS["dukkhā#np"] = A("болезненная")                     # … atthi dukkhā
ITEMS["sukhasahagata#np"] = A("сопровождаемая удовольствием")   # kāyasamphassajā saññā / kāyaviññāṇaṃ (bodily)
ITEMS["dukkhasahagata#np"] = A("сопровождаемая болью")
ITEMS["pītisahagato na sukhasahagato na upekkhāsahagato"] = A(
    "сопровождаемая восторгом, но не сопровождаемая счастьем и не сопровождаемая невозмутимостью",
    v="сопровождается восторгом, но не сопровождается счастьем и не сопровождается невозмутимостью")

ALIAS = {"na hetusahetuko": "na hetu sahetuko", "na hetuahetuko": "na hetu ahetuko",
         "āsavippayuttaanāsavo": "āsavavippayuttaanāsavo"}
ALIAS_SLIP = {"na hetuahetuko": "«na hetusahetuko / na hetuahetuko» written as one word in ^2-36, 40, 45, 131 (elsewhere «na hetu …»; rendered the same)",
              "āsavippayuttaanāsavo": "^2-113 «āsavippayuttaanāsavo» for «āsavavippayuttaanāsavo» (rendered as meant)"}


def item(key):
    if key in ALIAS_SLIP and ALIAS_SLIP[key] not in SLIPS:
        SLIPS.append(ALIAS_SLIP[key])
    key = ALIAS.get(key, key)
    return ITEMS[key]


# ---- Pāli plural of a key (question section: «cattāro khandhā siyā kusalā» …)
_INVAR = {"ceva", "ca", "na", "no", "neva", "dassanena", "bhāvanāya", "sukhāya", "dukkhāya", "adukkhamasukhāya",
          "vedanāya", "kenaci", "cittena", "upādā"}


def _pl_word(w):
    if w in _INVAR:
        return w
    if w.endswith("ñceva"):
        return w[:-len("añceva")] + "ā ceva"
    for a, b in (("hetu", "hetū"), ("pati", "patino"), ("vatti", "vattino")):
        if w.endswith(a):
            return w[:-len(a)] + b
    if w.endswith("aṃ"):
        return w[:-2] + "ā"
    if w.endswith("o"):
        return w[:-1] + "ā"
    if w.endswith("ī"):
        return w[:-1] + "ino"
    if w.endswith("ū"):
        return w[:-1] + "uno"
    return w


def pali_plural(key):
    return " ".join(_pl_word(w) for w in key.split(" "))


PL_KEY = {}
for _k in list(ITEMS):
    if "#" not in _k:
        PL_KEY.setdefault(pali_plural(_k), _k)
PL_KEY["arūpā"] = "arūpo"
# source plural forms that keep a singular noun (^2-697 «upādānañceva upādāniyā», ^2-698 «kileso ceva saṃkiliṭṭhā»)
PL_SPECIAL = {"upādānañceva upādāniyā ca": "являющиеся цеплянием и служащие объектом цепляния",
              "kileso ceva saṃkiliṭṭhā ca": "являющиеся омрачением и омрачённые"}


# =========================================================================== Abhidhammabhājanīya lines
NUMW = dict(S.NUMW)
NUMW.update({24: "на двадцать четыре вида", 30: "на тридцать видов", "many": "на многие виды"})
NUMP = {"eka": 1, "du": 2, "ti": 3, "catub": 4, "pañca": 5, "chab": 6, "satta": 7, "aṭṭha": 8, "nava": 9,
        "dasa": 10, "ekādasa": 11, "catuvīsati": 24, "tiṃsa": 30, "tiṃsati": 30, "bahu": "many"}
KHP = {"rūpakkhandho": "rupa", "vedanākkhandho": "vedana", "saññākkhandho": "sanna",
       "saṅkhārakkhandho": "sankhara", "viññāṇakkhandho": "vinnana"}
APARO = "Иначе"                                  # Aparopi (no termbase entry)
DUKAMULA = "На основе пар."                      # Dukamūlakaṃ. (termbase Duka «пары», mūlakaṃ «основа»)
TIKAMULA = "На основе троек."                    # Tikamūlakaṃ.
UBHATO = "Наращивание с обеих сторон."           # Ubhatovaḍḍhakaṃ. (termbase Ubhato, vaḍḍhakaṃ)
YATHA_KUSALATTIKE = "(Как подробно изложено в тройке о благом, так же следует подробно излагать и все тройки.)"
FIXED = {
    "Dukamūlakaṃ.": DUKAMULA,
    "Tikamūlakaṃ.": TIKAMULA,
    "Ubhatovaḍḍhakaṃ.": UBHATO,
    "(Yathā kusalattike vitthāro, evaṃ sabbepi tikā vitthāretabbā.)": YATHA_KUSALATTIKE,
    "Abhidhammabhājanīyaṃ.": f"{S.ABHI_BH}.",
    "Suttantabhājanīyaṃ.": f"{S.SUTTANTA_BH}.",
    "Pañhāpucchakaṃ.": f"{S.PANHA}.",
    "Khandhavibhaṅgo niṭṭhito.": f"{S.CH_TITLE[1][1]} {S.DONE}.",
}

SENSE_GEN = {"cakkhu": "глаза", "sota": "уха", "ghāna": "носа", "jivhā": "языка", "kāya": "тела", "mano": "ума",
             "manodhātu": "элемента ума", "manoviññāṇadhātu": "элемента умственного сознания"}
JA_NOUN = {"vedanā": "чувство", "saññā": "восприятие", "cetanā": "намерение"}     # all neuter
VINN = {"cakkhu": "зрительное сознание", "sota": "слуховое сознание", "ghāna": "обонятельное сознание",
        "jivhā": "вкусовое сознание", "kāya": "осязательное сознание", "mano": "умственное сознание"}
REL = {"f": "которая", "n": "которое", "m": "который"}
NP_PACC = re.compile(r"^(cakkhu|sota|ghāna|jivhā|kāya|mano)samphassapaccayā(?: (\S+kkhandho))?$")
NP_JA = re.compile(r"^(cakkhu|sota|ghāna|jivhā|kāya|manoviññāṇadhātu|manodhātu|mano)samphassajā (vedanā|saññā|cetanā)$")
NP_VIN = re.compile(r"^(cakkhu|sota|ghāna|jivhā|kāya|mano)viññāṇaṃ$")


def np_(t):
    """Pāli noun phrase -> (Russian, gender, is_paccaya) or None"""
    t = t[:1].lower() + t[1:]
    m = NP_PACC.match(t)
    if m:
        r = f"обусловленная контактом {SENSE_GEN[m.group(1)]}"
        if m.group(2):
            r = f"{KH[KHP[m.group(2)]]}, {r}"
        return r, "f", True
    m = NP_JA.match(t)
    if m:
        return f"рождённое контактом {SENSE_GEN[m.group(1)]} {JA_NOUN[m.group(2)]}", "n", False
    m = NP_VIN.match(t)
    if m:
        return VINN[m.group(1)], "n", False
    if t == "manodhātu":
        return "элемент ума", "m", False
    if t == "manoviññāṇadhātu":
        return "элемент умственного сознания", "m", False
    return None


def _atthi_key(k, ctx_np):
    """Pāli class word after «atthi» -> ITEMS key"""
    if ctx_np:
        for p, key in (("sukhasahagat", "sukhasahagata#np"), ("dukkhasahagat", "dukkhasahagata#np")):
            if k.startswith(p):
                return key
        if k in ("sukhā", "dukkhā"):
            return k + "#np"
    if k in ITEMS or k in ALIAS:
        return k
    for a, b in (("ā", "o"), ("aṃ", "o")):
        if k.endswith(a) and k[:-len(a)] + b in ITEMS:
            return k[:-len(a)] + b
    raise KeyError(k)


def atthi(key, g="f"):
    """«atthi X» = «бывает X(instrumental)», agreeing with «совокупность» (f) or a neuter / masculine noun"""
    it = item(key)
    return f"бывает {it['ins'] if g == 'f' else it['nins']}"


DELIM = {",": ",", ";": ";", ".": ".", "…pe…": "…"}


def chain(body, start_cap=False):
    """Translate an Abhidhammabhājanīya body (classes, noun phrases, «atthi …» runs)."""
    parts = re.split(r"(…pe…|[,;.])", body)
    E = []          # elements: dict(t=kind, s=text, lead=space before, ...)
    g, ctx_np, paccaya = "f", False, False
    for i, p in enumerate(parts):
        if i % 2 == 1:
            E.append(dict(t="sep", s=p))
            if p in ".;":
                g, ctx_np, paccaya = "f", False, False
            continue
        if not p.strip():
            continue
        lead = p[:1] == " "
        t = p.strip()
        pieces = re.split(r"\s+(?=atthi\s)", t)
        first, rest = pieces[0], pieces[1:]
        if re.match(r"^[Aa]tthi\s", first):
            rest = pieces
        else:
            r = np_(first)
            if r:
                E.append(dict(t="np", s=r[0], lead=lead, pacc=r[2], rel=False))
                g, ctx_np, paccaya = r[1], not r[2], r[2]
                if rest:
                    E[-1]["rel"] = not r[2]
                    E[-1]["s"] += (", " if r[2] else f", {REL[r[1]]} ")
                    if r[2]:
                        E[-1]["s"] += ""
                lead = False
            else:
                E.append(dict(t="pred", s=item(first)["v"], lead=lead))
                lead = False
        for j, a in enumerate(rest):
            if j > 0:
                SLIPS.append(f"missing comma before «{a}» (comma added)")
                E.append(dict(t="sep", s=","))
                lead = True
            key = _atthi_key(re.sub(r"^[Aa]tthi\s+", "", a), ctx_np)
            E.append(dict(t="at", s=atthi(key, g), lead=lead, np_tail=ctx_np or paccaya))
            lead = False
    # attach «atthi» tails to their noun phrase; find runs of plain noun phrases
    members = []    # (index of np element, index of last element of the member)
    i = 0
    while i < len(E):
        if E[i]["t"] == "np" and not E[i]["pacc"]:
            j = i
            if j + 1 < len(E) and E[j + 1]["t"] == "at":
                j += 1
            while j + 2 < len(E) and E[j + 1]["t"] == "sep" and E[j + 1]["s"] == "," and E[j + 2]["t"] == "at" \
                    and E[i]["rel"]:
                j += 2
            members.append((i, j))
            i = j + 1
        else:
            i += 1
    runs, cur = [], []
    for m in members:
        if cur and m[0] == cur[-1][1] + 2 and E[cur[-1][1] + 1]["t"] == "sep" and E[cur[-1][1] + 1]["s"] in (",", "…pe…"):
            cur.append(m)
        else:
            if cur:
                runs.append(cur)
            cur = [m]
    if cur:
        runs.append(cur)
    for run in runs:
        if len(run) < 2:
            continue
        seps = [run[k][1] + 1 for k in range(len(run) - 1)]
        if any(E[a]["rel"] for a, _ in run):
            for s in seps:
                if E[s]["s"] == ",":
                    E[s]["s"] = ";"
            continue
        after = run[-1][1] + 1
        closing = after >= len(E) or (E[after]["t"] == "sep" and E[after]["s"] in ".;")
        if closing and E[seps[-1]]["s"] == ",":
            E[seps[-1]]["s"] = "and"
    out, cap_next = [], start_cap
    for e in E:
        if e["t"] == "sep":
            out.append(" и" if e["s"] == "and" else DELIM[e["s"]])
            if e["s"] == ".":
                cap_next = True
            continue
        s = e["s"]
        if cap_next:
            s = cap(s)
            cap_next = False
        out.append((" " if e.get("lead") else "") + s)
    return "".join(out)


HEAD = re.compile(r"^(Tattha katamo (\S+)\? )?(Aparopi )?(\S+?)[vb]idhena (\S+kkhandho)( – | |…pe…)(.*)$")
END = re.compile(r"^(.*?)\s*\b([Ee])vaṃ (\S+?)[vb]idhena (\S+kkhandho)\.$")


def vidha(n, k):
    return f"{cap(KH[k])} {NUMW[n]} –"


def vidha_end(n, k):
    return f"Такова {KH[k]} {NUMW[n]}."


def abhi_line(p):
    if p in FIXED:
        return FIXED[p]
    m = re.match(r"^Ayaṃ vuccati (\S+kkhandho)\.$", p)
    if m:
        return f"Это называется {S.kh_ins(KHP[m.group(1)])}."
    if p.startswith("Atthi "):           # continuation line of a long list of pairs
        return chain(p, start_cap=True)
    m = HEAD.match(p)
    assert m, p
    q, qkh, aparo, nw, kh, sep, body = m.groups()
    k = KHP[kh]
    out = f"{S.agg_q(k)} " if q else ""
    hd = vidha(NUMP[nw.lower()], k)
    if aparo:
        hd = f"{APARO} {low(hd)}"
    if sep == " – ":
        out += hd + " "
    elif sep == " ":
        SLIPS.append(f"no dash after «{nw}vidhena {kh}» (none added)")
        out += hd[:-2] + " "
    else:                                 # «…pe…» right after the aggregate
        out += hd[:-2] + "…"
        body = body.lstrip()
        if body:
            out += " "
    tail = ""
    me = END.match(body)
    if me:
        body = me.group(1)
        assert KHP[me.group(4)] == k, p
        tail = vidha_end(NUMP[me.group(3).lower()], k)
        if me.group(2) == "e":
            tail = low(tail)
    r = chain(body) if body else ""
    if tail:
        r = (r + " " + tail) if r else tail
    return out + r


# =========================================================================== Pañhāpucchaka
SUBJ = {  # Pāli subject -> (Russian, number)
    "Rūpakkhandho": (cap(KH["rupa"]), "s"), "Vedanākkhandho": (cap(KH["vedana"]), "s"),
    "Saññākkhandho": (cap(KH["sanna"]), "s"), "Saṅkhārakkhandho": (cap(KH["sankhara"]), "s"),
    "Viññāṇakkhandho": (cap(KH["vinnana"]), "s"),
    "Cattāro khandhā": ("Четыре совокупности", "p"), "Tayo khandhā": ("Три совокупности", "p"),
    "Dve khandhā": ("Две совокупности", "p"),
}
GROUP_GEN = {"Pañcannaṃ khandhānaṃ": "из пяти совокупностей"}   # kati … ? questions
PRON = {"s": "её", "p": "их"}
NV = "нельзя определить –"                 # na vattabbo / vattabbā – (pi-1 «X нельзя определить – ни как …»)
SAPPACCAYA = "Имеют условия, являются обусловленными."   # Sappaccayā, saṅkhatā. (said of all five)
FIXED_SENT = {"Sappaccayā, saṅkhatā.": SAPPACCAYA}
PANHA_FIX = [  # plain typographic slips of the source, rendered as meant (reported)
    ('– kilesasampayuttā ceva no ca kilesā"ti', '– "kilesasampayuttā ceva no ca kilesā"ti',
     '^2-153 «siyā na vattabbā – kilesasampayuttā ceva no ca kilesā"ti»: opening quote missing (balanced in Russian)'),
]
QUOTE = re.compile(r'^"([^"]+)"(ntipi|nti|tipi|ti pi|ti)?$')


def _qkey(text, num, suffix):
    t = text
    if suffix and suffix.startswith("n"):
        t += "ṃ"
    t = re.sub(r"cā$", "ca", t)
    if num == "s":
        t = re.sub(r"hetū$", "hetu", t)
        return ALIAS.get(t, t), None
    if t in PL_SPECIAL:
        SLIPS.append(f"«{t}» with a plural subject keeps the singular noun (translated as written)")
        return None, PL_SPECIAL[t]
    return PL_KEY[t], None


def _pred(word, num):
    if num == "s":
        if word not in ITEMS and word.endswith("ā") and word[:-1] + "o" in ITEMS:
            SLIPS.append(f"«{word}» (plural form) with a singular subject (rendered in the singular)")
            word = word[:-1] + "o"
        return item(word)["v"]
    return item(PL_KEY.get(word, word))["vp"]


def _quote(key, num, special):
    if special:
        return f"«{special}»"
    it = item(key)
    return f"«{it['f'] if num == 's' else it['pl']}»"


def _sentence(sent):
    """one Pañhāpucchaka sentence (without its final full stop)"""
    if sent + "." in FIXED_SENT:
        return FIXED_SENT[sent + "."][:-1]
    m = re.match(r"^(" + "|".join(sorted(SUBJ, key=len, reverse=True)) + r") (.*)$", sent)
    assert m, sent
    subj, num = SUBJ[m.group(1)]
    body = m.group(2)
    if body.endswith("āti"):                       # closing «…ti» of the whole section
        body = body[:-2]
    toks = re.split(r"(, |; |…pe… )", body)
    out = []                                       # rendered clauses and separators
    prev_v = None                                  # previous predicate (for eliding a repeated «является(-ются)»)
    first = True
    nv = None                                      # open «na vattabbā» list: dict(items, many)
    for i, tok in enumerate(toks):
        if i % 2 == 1:
            if nv is None:
                out.append("…" if tok == "…pe… " else tok.strip())
            else:
                nv["pending"] = "…" if tok == "…pe… " else tok.strip()
            if tok.strip() == ";":
                prev_v = None
            continue
        qm = QUOTE.match(tok)
        if qm and qm.group(2) is None:
            # «na vattabbo – "A"ti, "B".» (fetters … defilements): the quoted B without «ti» is what the subject IS
            # (coordinator decision): rendered like the taint group's plain «…ti, sāsavo ceva no ca āsavo»
            assert nv is not None, sent
            out.append(_render_nv(nv))
            out.append(nv["pending"] or ",")
            nv, prev_v = None, None
            key, _ = _qkey(qm.group(1), num, None)
            out.append(item(key)["v" if num == "s" else "vp"])
            continue
        if qm:                                     # next quoted item of an open «na vattabbā» list
            assert nv is not None, sent
            key, sp = _qkey(qm.group(1), num, qm.group(2))
            nv["q"].append((_quote(key, num, sp), qm.group(2)))
            nv["pending"] = None
            continue
        if nv is not None:                         # close the open list
            out.append(_render_nv(nv))
            if nv["pending"]:
                out.append(nv["pending"])
            nv = None
            prev_v = None
        mv = re.match(r'^(siyā )?na vattabb[oā] – (.*)$', tok)
        if mv:
            qm = QUOTE.match(mv.group(2))
            assert qm, tok
            key, sp = _qkey(qm.group(1), num, qm.group(2))
            if mv.group(1):
                head = f"иногда {PRON[num]} {NV}"
            else:
                assert first, sent
                head = f"{subj} {NV}"
            nv = dict(head=head, q=[(_quote(key, num, sp), qm.group(2))], pending=None)
            first = False
            continue
        for sk in SUBJ:                            # a new subject after a comma (^2-153 «appītiko, cattāro khandhā …»)
            if tok.startswith(low(sk) + " "):
                SLIPS.append(f"«…, {low(sk)} …»: a new sentence joined by a comma (kept, subject in lower case)")
                subj, num = low(SUBJ[sk][0]), SUBJ[sk][1]
                tok = tok[len(sk) + 1:]
                first, prev_v = True, None
                break
        siya = tok.startswith("siyā ")
        word = tok[5:] if siya else tok
        v = _pred(word, num)
        shown = v
        if prev_v is not None and prev_v[1] == siya:
            for verb in ("является ", "являются "):
                if v.startswith(verb) and prev_v[0].startswith(verb):
                    shown = v[len(verb):]
        prev_v = (v, siya)
        shown = ("иногда " + shown) if siya else shown
        out.append(f"{subj} {shown}" if first else shown)
        first = False
    if nv is not None:
        out.append(_render_nv(nv))
    # glue clauses with their separators
    res = ""
    for x in out:
        if x in (",", ";", "…"):
            res += x
        else:
            res += (" " if res else "") + x
    # pi-1 ^1-? «познаваемы … и не познаваемы …» (Sabbe dhammā kenaci viññeyyā, kenaci na viññeyyā)
    res = res.replace("познаваемы тем или иным видом сознания, не познаваемы",
                      "познаваемы тем или иным видом сознания и не познаваемы")
    return res


def _render_nv(nv):
    many = any(s and s.startswith(("tipi", "ti pi", "ntipi")) for _, s in nv["q"])
    if many:
        body = ", ".join(f"ни как {q}" for q, _ in nv["q"])
    else:
        body = "как " + ", ".join(q for q, _ in nv["q"])
    return f"{nv['head']} {body}"


def panha_line(p):
    """a line of the question section: sentences split at «. » before a capital"""
    p = p.replace('"ti pi', '"tipi')
    for bad, good, note in PANHA_FIX:
        if bad in p:
            p = p.replace(bad, good)
            SLIPS.append(note)
    sents = re.split(r"(?<=\.) (?=[A-Z])", p)
    res = []
    for s in sents:
        assert s.endswith("."), s
        res.append(_sentence(s[:-1]) + ".")
    return " ".join(res)


def panha_question(p, groups=None):
    """Pañcannaṃ khandhānaṃ kati kusalā, kati akusalā, … kati araṇā? = Сколько из пяти совокупностей являются …"""
    groups = groups or GROUP_GEN
    m = re.match(r"^(.*?) (kati .*)\?$", p)
    grp, body = m.group(1), m.group(2)
    parts = re.split(r"(…pe…|, )", body)
    out = []
    for i, x in enumerate(parts):
        if i % 2 == 1:
            out.append("…" if x == "…pe…" else ",")
            continue
        x = x.strip()
        if not x:
            continue
        w = re.sub(r"^kati ", "", x)
        ins = item(PL_KEY[w])["insp"]
        out.append(f"Сколько {groups[grp]} являются {ins}" if not out else f" сколько {ins}")
    return "".join(out) + "?"


# =========================================================================== segments
def segs(text):
    return S.segs(text)


def build_rest():
    pali = SRC.read_text(encoding="utf-8")
    h = {}
    seen = False
    section = "abhi"
    for sid, lines in segs(pali):
        if sid == "2-33":
            seen = True
            continue
        if not seen:
            continue
        ru = []
        for ln in lines:
            ln = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln)
            if ln.startswith("#"):
                lvl, text = ln.split(" ", 1)
                if text == "Pañhāpucchakaṃ":
                    section = "panha"
                    ru.append(f"{lvl} {S.PANHA}")
                elif text == "Tikaṃ":
                    ru.append(f"{lvl} {S.TIKA_H}")
                elif text == "Dukaṃ":
                    ru.append(f"{lvl} {S.DUKA_H}")
                else:
                    ru.append(f"{lvl} {cap(KH[KHP[low(text)]])}")
                continue
            if ln.startswith("Pañcakkhandhā – "):
                ru.append(S.FIVE)
            elif section == "abhi":
                ru.append(abhi_line(ln))
            elif ln in FIXED:
                ru.append(FIXED[ln])
            elif ln.endswith("?"):
                ru.append(panha_question(ln))
            else:
                ru.append(panha_line(ln))
        h[sid] = ru
    return h, pali


def render_rest(pali, h):
    blocks = []
    seen = False
    for sid, plines in segs(pali):
        if sid == "2-33":
            seen = True
            continue
        if not seen:
            continue
        ru = h[sid]
        assert len(ru) == len(plines), (sid, len(ru), len(plines))
        lines = list(ru)
        lines[-1] = f"{lines[-1]} ^{sid}"
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks) + "\n"


# =========================================================================== pi-1 comparison and notes
def check_pi1():
    """matrix names: my plural form vs the pi-1 matrix name; returns the list of differences"""
    names = {}
    for sid, its in list(P1.TRIADS.items()) + list(P1.PAIRS.items()):
        for p, ru, _ in its:
            names[p] = ru
    for p, ru in P1.EXTRA_NAMES:
        names[p] = ru
    diffs = []
    for key, it in ITEMS.items():
        if "#" in key:
            continue
        pk = pali_plural(key).replace("upādinn", "upādiṇṇ")
        if pk not in names:
            continue
        mine = it["pl"]
        theirs = names[pk]
        cand = {f"явления, {mine}", f"{mine} явления", mine.replace("явления ", "явления ")}
        if mine.startswith("явления "):
            cand.add(mine)
        if theirs not in cand and theirs.replace("явления, ", "") != mine:
            diffs.append((pk, theirs, mine))
    return diffs


def notes_md(diffs):
    L = ["# pi-2 Russian rails: new formulas of chapter 1 after the sample (^2-34 … ^2-153)", "",
         "Generated by build_rails_1_ru.py; import it (K1) instead of retyping. Strings already in ru-rails-formulas.md "
         "(sample) are not repeated. Matrix items: ITEMS[key] with the forms f / pl / ins / nins / insp / v / vp.", "",
         "## Abhidhammabhājanīya", "",
         "atthi X, atthi Y (classes of an aggregate) = бывает X(ins, feminine), бывает Y(ins)",
         "NP atthi X, atthi Y (a list member) = NP, которое (который) бывает X(ins, neuter / masculine), бывает Y",
         "Xsamphassapaccayā Ykkhandho atthi … = Y, обусловленная контактом X(gen), бывает …",
         "Xsamphassapaccayā (alone, in a …pe… run) = обусловленная контактом X(gen)",
         "manodhātusamphassajā vedanā / saññā / cetanā = рождённое контактом элемента ума чувство / восприятие / намерение",
         "manoviññāṇadhātusamphassajā vedanā = рождённое контактом элемента умственного сознания чувство",
         "manodhātu, manoviññāṇadhātu (in a list) = элемент ума, элемент умственного сознания",
         "noun-phrase lists: «, » before the last member becomes « и »; if a member has a «которое бывает …» clause, "
         "the commas between the members become «;» (sample ^2-33 KNOW8)",
         f"Ekavidhena vedanākkhandho – phassasampayutto. = {cap(KH['vedana'])} по одному – связана с контактом.",
         f"Ekavidhena saṅkhārakkhandho – cittasampayutto. = {cap(KH['sankhara'])} по одному – связана с умом.",
         f"Catuvīsatividhena / Tiṃsa(ti)vidhena / Bahuvidhena = {NUMW[24]} / {NUMW[30]} / {NUMW['many']}",
         f"Aparopi <N>vidhena X – = {APARO} X <N> –   (no termbase entry)",
         f"Evaṃ … / evaṃ … (lower case after …pe…) = Такова … / такова …",
         f"Dukamūlakaṃ. = {DUKAMULA}", f"Tikamūlakaṃ. = {TIKAMULA}", f"Ubhatovaḍḍhakaṃ. = {UBHATO}",
         f"(Yathā kusalattike vitthāro, evaṃ sabbepi tikā vitthāretabbā.) = {YATHA_KUSALATTIKE}",
         "atthi sukhindriyaṃ … upekkhindriyaṃ = бывает способностью удовольствия / боли / радости / уныния / невозмутимости",
         "atthi sukhindriyasampayutto … = бывает связанной со способностью удовольствия …",
         "kāyasamphassajā vedanā atthi sukhā, atthi dukkhā = рождённое контактом тела чувство, которое бывает приятным, бывает болезненным",
         "kāyasamphassajā saññā / cetanā atthi sukhasahagatā, atthi dukkhasahagatā = …, которое бывает сопровождаемым удовольствием, бывает сопровождаемым болью",
         "kāyaviññāṇaṃ atthi sukhasahagataṃ, atthi dukkhasahagataṃ = осязательное сознание, которое бывает сопровождаемым удовольствием, бывает сопровождаемым болью",
         "", "## Pañhāpucchaka", "",
         f"#### Pañhāpucchakaṃ = #### {S.PANHA}; ##### Tikaṃ / Dukaṃ = ##### {S.TIKA_H} / {S.DUKA_H}",
         "Pañcannaṃ khandhānaṃ kati X, kati Y …? = Сколько из пяти совокупностей являются X(ins pl), сколько Y(ins pl) …?",
         "Rūpakkhandho / Vedanā- / Saṅkhāra- / Viññāṇakkhandho = Совокупность материальной формы / чувств / формирующих факторов / сознания",
         "Cattāro / Tayo / Dve khandhā = Четыре / Три / Две совокупности",
         "Subject X. = Subject <finite predicate> (ITEMS v / vp): «является благой», «не имеет корней», «связана с корнями» …",
         "siyā X, siyā Y = иногда X, иногда Y (a repeated «является / являются» is dropped after the first)",
         'na vattabbo – "X"tipi, "Y"tipi = нельзя определить – ни как «X», ни как «Y» (quote in the subject\'s gender and number)',
         'na vattabbo – "X"ti = нельзя определить – как «X»',
         'siyā na vattabbo / vattabbā – … = иногда её / их нельзя определить – …',
         'na vattabbo – "A"ti, "B". (fetters, ties, hindrances, misapprehension, clinging, defilements: B quoted '
         'without «ti») = нельзя определить – как «A», B(finite predicate). (coordinator decision: same as the taint '
         'group «…ti, sāsavo ceva no ca āsavo»; e.g. «Совокупность материальной формы нельзя определить – как '
         '«являющаяся оковами и подверженная оковам», подвержена оковам, но не является оковами.»)',
         f"Sappaccayā, saṅkhatā. = {SAPPACCAYA}",
         "kenaci viññeyyā, kenaci na viññeyyā = познаваемы тем или иным видом сознания и не познаваемы тем или иным видом сознания (pi-1)",
         f"Pañhāpucchakaṃ. = {S.PANHA}.", f"Khandhavibhaṅgo niṭṭhito. = {FIXED['Khandhavibhaṅgo niṭṭhito.']}",
         "", "## Matrix items (key = Pāli masculine singular; f / pl / ins / v)", ""]
    for k, it in ITEMS.items():
        L.append(f"{k} = {it['f']} / {it['pl']} / {it['ins']} / {it['v']}")
    L += ["", "## Differences from the pi-1 matrix names (pi-1 → pi-2)", ""]
    for pk, theirs, mine in diffs:
        L.append(f"{pk}: pi-1 «{theirs}» → pi-2 «{mine}»")
    return "\n".join(L) + "\n"


def main():
    h, pali = build_rest()
    rest = render_rest(pali, h)
    sample = SAMPLE_RU.read_bytes()
    assert sample.endswith(b"^2-33\n")
    data = sample + b"\n" + rest.encode("utf-8")
    TARGET.write_bytes(data)
    diffs = check_pi1()
    NOTES_PATH.write_text(notes_md(diffs), encoding="utf-8", newline="\n")
    print(f"wrote {TARGET.name}: {len(h)} segments after the sample; notes-1.md")
    for d in diffs:
        print("pi-1 diff:", d)
    for s in dict.fromkeys(SLIPS):
        print("slip:", s)


if __name__ == "__main__":
    main()
