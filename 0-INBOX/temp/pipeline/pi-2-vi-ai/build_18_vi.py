# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Vietnamese plain zero-shot: chapter 18 (Dhammahadayavibhaṅga), the last chapter.

usage: python -I -X utf8 build_18_vi.py [--dry]
Writes AI_translation\\vietnamese\\pi-2-vietnamese-plain-zeroshot_split_chapters\\18-dhammahadayavibhango.md (only when
run as a script without --dry; importing writes nothing).

Imports build_17_vi and through it S (sample), B (ch1), T (ch2-3), F (ch4-5) …; their tables are extended in memory only
(F.add_item into T's item tables), nothing of theirs is written. Reused strings: the aggregate / base / element / truth /
faculty names (S, T, F), the matrix predicates (B / T items, so every Pañhāpucchaka-type sentence keeps the ch1-5
wording), the feeling / perception / intention names (B.SUBJ), the nutriments (pi-1 ^1-70), the roots (pi-1 ^1-1059 …
^1-1077, 5-atthakatha «gốc rễ là quả của nghiệp»), the realm definitions (pi-1 ^1-1287 … ^1-1294), Sắc Cứu Cánh /
Tha Hóa Tự Tại / cõi Phạm Thiên / địa ngục Vô Gián (pi-1), the colophon pattern (pi-1 «Bộ “…” đã hoàn tất.»).
Every non-empty Pāli line is matched in order against a key; unknown Pāli raises KeyError. After the build every
Pāli sentence of the Pañhāpucchaka-type lines that also occurs in an earlier pi-2 chapter (or pi-1) is checked to have
byte-identical Vietnamese there.
"""
import importlib
import os
import re
import sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai"
sys.path.insert(0, HERE)
Z17 = importlib.import_module("build_17_vi")
S = importlib.import_module("build_ch1_sample_vi")
B = importlib.import_module("build_1_vi")
T = importlib.import_module("build_2-3_vi")
F = importlib.import_module("build_4-5_vi")

DASH = S.DASH
cap, low = S.cap, S.low
TATTHA, THI = S.TATTHA, S.THI
pi1, between, repl = T.pi1, T.between, T.repl
FN = "18-dhammahadayavibhango.md"
SLIPS = []


def called(x):
    return f"{S.VUCCATI} “{x}”"


def vi_file(fn):
    return open(os.path.join(S.VI_DIR, fn), encoding="utf-8").read()


# ================================================================ 1. names (reused, asserted)
KHP = ["rūpakkhandho", "vedanākkhandho", "saññākkhandho", "saṅkhārakkhandho", "viññāṇakkhandho"]
KHV = [S.AGG[a]["khandha"] for a in ("rupa", "vedana", "sanna", "sankhara", "vinnana")]
NAME = dict(zip(KHP, KHV))
NAME.update(T.AYATANA)
NAME.update({k: T.DHATU[k] for k in T.ORDER_D})
TRUTH = {low(k): low(v) for k, v in F.TRUTH_SUBJ.items() if k.endswith("saccaṃ")}
NAME.update(TRUTH)
NAME.update(F.IND)
NAME["rūpajīvitindriyaṃ"] = F.RUPA_JIV
_ch2, _ch3, _ch4, _ch5 = (vi_file(x) for x in ("2-ayatanavibhango.md", "3-dhatuvibhango.md", "4-saccavibhango.md",
                                                 "5-indriyavibhango.md"))
for _v in T.AYATANA.values():
    assert _v in _ch2, _v
for _k in T.ORDER_D:
    assert T.DHATU[_k] in _ch3, _k
for _v in TRUTH.values():
    assert cap(_v) in _ch4, _v
for _v in F.IND.values():
    assert _v in _ch5, _v

# contacts and what is born of them (ch4 «sự tiếp xúc của mắt»; B.SUBJ «… sinh từ sự tiếp xúc của yếu tố ý»)
DOORS7 = [(d, v) for d, v in B.DOORS7 if d != "mano"]
for _d, _v in DOORS7:
    NAME[f"{_d}samphasso"] = f"sự tiếp xúc của {_v}"
    for _pn in ("vedanā", "saññā", "cetanā"):
        NAME[f"{_d}samphassajā {_pn}"] = B.SUBJ[f"{_d}samphassajā {_pn}"]
assert "sự tiếp xúc của mắt" in _ch4 and "sự tiếp xúc của ý" in _ch4
NAME["kāyaviññāṇadhātusamphasso"] = "sự tiếp xúc của yếu tố thức qua thân"   # [new; pi-1 words]
# the seven "minds"
for _p, _v in zip(("cakkhuviññāṇaṃ", "sotaviññāṇaṃ", "ghānaviññāṇaṃ", "jivhāviññāṇaṃ", "kāyaviññāṇaṃ"),
                  S.VINNANA6.split(", ")[:5]):
    NAME[_p] = _v
# nutriments [pi-1 ^1-70; kabaḷīkāro āhāro = sample / APPROVED]
KABALI = "thức ăn trong vai trò dưỡng chất"
assert KABALI in S.FEMININITY_TO_FOOD
_ah = between(pi1("1-70"), "là những gì? ", ".").split(", ")
assert len(_ah) == 3 and _ah[0] == "Sự tiếp xúc trong vai trò dưỡng chất", _ah
NAME.update({"kabaḷīkārāhāro": KABALI, "kabaḷīkāro āhāro": KABALI, "phassāhāro": low(_ah[0]),
             "manosañcetanāhāro": _ah[1], "viññāṇāhāro": _ah[2]})
# roots [pi-1 ^1-1059, ^1-1060, ^1-1064; 5-atthakatha «gốc rễ là quả của nghiệp»]
KUS_H, AKUS_H, ABY_H = "gốc rễ thiện", "gốc rễ bất thiện", "gốc rễ không xác định về mặt đạo đức"
assert f"Ba {KUS_H}, ba {AKUS_H}, ba {ABY_H}" in pi1("1-1059")
VIP_H = "gốc rễ là quả của nghiệp"
assert VIP_H in F.pi1_line("5-atthakathakandam.md", "Alobho vipākahetu adoso vipākahetu")
ROOT = {"alobho": "sự không tham lam", "adoso": "sự không sân hận", "amoho": "sự không si mê",
        "lobho": "sự tham lam", "doso": "sự sân hận", "moho": "sự si mê"}
assert pi1("1-1060").endswith("Sự không tham lam, sự không sân hận, sự không si mê.")
assert pi1("1-1064").endswith("Sự tham lam, sự sân hận, sự si mê.")
ROLE = "trong vai trò"   # as pi-1 «thức ăn trong vai trò dưỡng chất» [new for roots: avoids «là … là»]
for _r, _v in ROOT.items():
    for _h, _hv in (("kusalahetu", KUS_H), ("akusalahetu", AKUS_H), ("vipākahetu", VIP_H)):
        NAME[f"{_r} {_h}"] = f"{_v} {ROLE} {_hv}"
ABY_BODY_KV = between(pi1("1-1068"), "là những gì? ", f" {DASH} đó là")   # … hoặc trong … mang tính chức năng
ABY_BODY_K = between(pi1("1-1077"), "là những gì? ", f" {DASH} đó là")    # … trong quả của các hiện tượng thiện

# counts
NUMV = {1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín", 10: "mười",
        11: "mười một", 12: "mười hai", 13: "mười ba", 14: "mười bốn", 15: "mười lăm", 16: "mười sáu",
        18: "mười tám", 22: "hai mươi hai"}
UNIT = {"khandha": "khối", "ayatana": "lĩnh vực nhận biết", "dhatu": "yếu tố", "sacca": "sự thật",
        "indriya": "năng lực", "hetu": "gốc rễ", "ahara": "loại dưỡng chất", "phassa": "loại tiếp xúc",
        "vedana": "loại cảm giác", "sanna": "loại tri giác", "cetana": "loại chủ ý", "citta": "loại tâm"}
ORDER12 = ["khandha", "ayatana", "dhatu", "sacca", "indriya", "hetu", "ahara", "phassa", "vedana", "sanna", "cetana",
           "citta"]
PNUM = {"eko": 1, "ekā": 1, "ekaṃ": 1, "dve": 2, "tayo": 3, "tīṇi": 3, "cattāro": 4, "catasso": 4, "cattāri": 4,
        "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8, "nava": 9, "dasa": 10, "ekādasa": 11, "terasa": 13,
        "aṭṭhārasa": 18}
PUNIT = {"khandhā": "khandha", "khandho": "khandha", "āyatanāni": "ayatana", "dhātuyo": "dhatu", "saccāni": "sacca",
         "saccaṃ": "sacca", "hetū": "hetu", "āhārā": "ahara", "phassā": "phassa", "phasso": "phassa",
         "vedanā": "vedana", "saññā": "sanna", "cetanā": "cetana", "cittāni": "citta", "cittaṃ": "citta"}
COMPOUND = {"pañcakkhandhā": (5, "khandha"), "dvādasāyatanāni": (12, "ayatana"),
            "ekādasāyatanāni": (11, "ayatana"), "dasāyatanāni": (10, "ayatana"), "navāyatanāni": (9, "ayatana"),
            "sattāyatanāni": (7, "ayatana"), "pañcāyatanāni": (5, "ayatana"), "bāvīsatindriyāni": (22, "indriya"),
            "cuddasindriyāni": (14, "indriya"), "terasindriyāni": (13, "indriya"),
            "dvādasindriyāni": (12, "indriya"), "ekādasindriyāni": (11, "indriya"), "dasindriyāni": (10, "indriya"),
            "navindriyāni": (9, "indriya"), "aṭṭhindriyāni": (8, "indriya"), "sattindriyāni": (7, "indriya"),
            "pañcindriyāni": (5, "indriya"), "cattārindriyāni": (4, "indriya"), "ekindriyaṃ": (1, "indriya")}


def count_vi(p):
    """Pāli count phrase (e.g. "aṭṭhārasa dhātuyo", "cuddasindriyāni", "satta cittāni") -> Vietnamese."""
    if p in COMPOUND:
        n, u = COMPOUND[p]
    else:
        a, b = p.split(" ")
        n, u = PNUM[a], PUNIT[b]
    return f"{NUMV[n]} {UNIT[u]}"


def chain_vi(p, fn=count_vi):
    """X…pe… Y… Z (counts or names joined by ellipses) -> «X… Y… Z»"""
    return "… ".join(fn(x) for x in re.split(r"\s?…(?:pe…)?\s?", p))


REALM = {"kāmadhātuyā": "cõi dục lạc", "rūpadhātuyā": "cõi hình sắc", "arūpadhātuyā": "cõi không hình sắc",
         "apariyāpanne": "phần không nằm trong các cõi tồn tại"}   # [new; pi-1 kāmāvacara «thuộc cõi dục lạc» …]
assert all(f"thuộc {v}" in pi1("1-990") for v in list(REALM.values())[:3])
assert "không nằm trong các cõi tồn tại" in pi1("1-990")

# variant brackets
VAR = {
    "[kabaḷiṃkāro āhāro (sī. syā.)]": "[khác chính tả (Sī., Syā.): kabaḷiṃkāro āhāro]",
    "[keci (syā.)]": "[dị bản (Syā.): keci]",
    "[avasesā sattā (?)]": "[dị bản (?): avasesā sattā]",
    "[sammatidevā (syā.)]": "[khác chính tả (Syā.): sammatidevā]",
    "[cātummahārājike (sī. syā.)]": "[khác chính tả (Sī., Syā.): cātummahārājike]",
    "[appaṃ vā bhiyyo vā (syā. ka.) dī. ni. 2.7]": "[dị bản (Syā., Ka.): appaṃ vā bhiyyo vā; dī. ni. 2.7]",
    "[rattidivo (ka.) a. ni. 3.71]": "[khác chính tả (Ka.): rattidivo; a. ni. 3.71]",
    "[chapi te (syā.)]": "[dị bản (Syā.): chapi te]",
    "[eko kappo (syā.)]": "[dị bản (Syā.): eko kappo]",
    "[bhavaggaṃ vāpi (syā.)]": "[dị bản (Syā.): bhavaggaṃ vāpi]",
    "[puna gacchanti (syā.)]": "[dị bản (Syā.): puna gacchanti]",
}


def item_vi(x):
    """One list member -> Vietnamese (names, "X vā Y vā", a trailing variant bracket, a missing comma)."""
    var = ""
    m = re.match(r"^(.*?) (\[[^\]]+\])$", x)
    if m:
        x, var = m.group(1), " " + VAR[m.group(2)]
    lx = low(x)
    m = re.match(r"^(\S+) vā (\S+) vā$", lx)
    if m:
        return f"{NAME[m.group(1)]} hoặc {NAME[m.group(2)]}" + var
    if lx in NAME:
        return NAME[lx] + var
    ws = lx.split(" ")
    if len(ws) > 1 and all(w in NAME for w in ws):
        SLIPS.append(f"missing comma (rendered with a comma): {x}")
        return ", ".join(NAME[w] for w in ws) + var
    raise KeyError("member: " + x)


def members_vi(s):
    parts = re.split(r"(, |\s?…(?:pe…)?\s?)", s)
    out = []
    for i, x in enumerate(parts):
        if i % 2:
            out.append(", " if x == ", " else "… ")
        else:
            out.append(item_vi(x))
    return "".join(out)


# ================================================================ 2. predicates (T / B items, extended in memory)
P = lambda k: T.ITEMS[k]["p"]  # noqa: E731
NEW_ITEMS = [   # [new] (key, Pāli surfaces, Vietnamese)
    ("c18_abhinneyya", ["abhiññeyyo"], "cần được hiểu biết trực tiếp"),        # abhiññā pi-1 «sự hiểu biết trực tiếp»
    ("c18_parinneyya", ["pariññeyyo"], "cần được hiểu biết trọn vẹn"),
    ("c18_pahatabba", ["pahātabbo"], "cần được dứt bỏ"),                        # pi-1 pahātabba «cần dứt bỏ»
    ("c18_na_pahatabba", ["na pahātabbo"], "không cần được dứt bỏ"),
    ("c18_bhavetabba", ["bhāvetabbo"], "cần được tu tập"),
    ("c18_na_bhavetabba", ["na bhāvetabbo"], "không cần được tu tập"),
    ("c18_sacchikatabba", ["sacchikātabbo"], "cần được tự mình chứng nghiệm"),  # sacchikiriyā ch9 «sự tự mình chứng nghiệm»
    ("c18_na_sacchikatabba", ["na sacchikātabbo"], "không cần được tự mình chứng nghiệm"),
    ("c18_dittha", ["diṭṭho"], "được thấy"),                                    # sample diṭṭhaṃ sutaṃ mutaṃ viññātaṃ
    ("c18_na_dittha", ["na diṭṭho"], "không được thấy"),
    ("c18_suta", ["suto"], "được nghe"),
    ("c18_na_suta", ["na suto"], "không được nghe"),
    ("c18_muta", ["muto"], "được cảm nhận"),
    ("c18_na_muta", ["na muto"], "không được cảm nhận"),
    ("c18_vinnata", ["viññāto"], "được nhận biết"),
    ("c18_na_vinnata", ["na viññāto"], "không được nhận biết"),
    ("c18_sarammanarammana", ["sārammaṇārammaṇo"], "lấy những gì có đối tượng làm đối tượng"),
    ("c18_anarammanarammana", ["anārammaṇārammaṇo"], "lấy những gì không có đối tượng làm đối tượng"),
    # as written (reported): "dukkhamasukhāya" (a- missing) = painful and not pleasant
    ("c18_dukkhamasukha_vs", ["dukkhamasukhāya vedanāya sampayutto"],
     "gắn liền với cảm giác khó chịu và không dễ chịu"),
]
for _r, _rv in (("kāma", "cõi dục lạc"), ("rūpa", "cõi hình sắc"), ("arūpa", "cõi không hình sắc")):
    NEW_ITEMS.append((f"c18_{_r}_pariy", [f"{_r}dhātupariyāpanno"], f"nằm trong {_rv}"))
    NEW_ITEMS.append((f"c18_na_{_r}_pariy", [f"na {_r}dhātupariyāpanno"], f"không nằm trong {_rv}"))
for _k, _s, _v in NEW_ITEMS:
    F.add_item(_k, _s, _v)
T.SURF["na arūpadhātupariyāpannāni"] = "c18_na_arūpa_pariy"   # neuter plural (Tīṇi saccāni …)
T.CANON[T.canon("na arūpadhātupariyāpannāni")] = "c18_na_arūpa_pariy"
assert P("c18_na_arūpa_pariy") == "không nằm trong cõi không hình sắc"


def lookup(p):
    return T.ITEMS[T.key_of(p)]["s"]


def words(s):
    """A predicate of one or more matrix-type words ("abhiññeyyo pariññeyyo na pahātabbo …") -> «…, …»."""
    try:
        return lookup(s)
    except KeyError:
        pass
    ws, out, i = s.split(" "), [], 0
    while i < len(ws):
        for j in range(len(ws), i, -1):
            try:
                v = lookup(" ".join(ws[i:j]))
                break
            except KeyError:
                continue
        else:
            raise KeyError("predicate: " + s)
        out.append(v)
        i = j
    return ", ".join(out)


# ================================================================ 3. subjects (ch1-5 strings; «thì» rules of F.Q)
SUBJ = {}


def add_s(p, v, single=False):
    SUBJ[low(p)] = (low(v), single)


for _p, _v in B.SUBJECTS.items():
    add_s(_p, _v)
add_s("Saṅkhārakkhandho", cap(NAME["saṅkhārakkhandho"]))
for _p, _v in T.SUBJECTS.items():
    add_s(_p, _v)
for _p in ("Gandhāyatanaṃ", "Rasāyatanaṃ", "Phoṭṭhabbāyatanaṃ"):
    add_s(_p, NAME[low(_p)])
add_s("Sattāyatanā", "Bảy lĩnh vực")
add_s("Dve āyatanā", "Hai lĩnh vực")
for _p in ("Gandhadhātu", "Rasadhātu", "Phoṭṭhabbadhātu"):
    add_s(_p, NAME[low(_p)])
add_s("Terasa dhātuyo", "Mười ba yếu tố")
for _p, _v in F.TRUTH_SUBJ.items():
    add_s(_p, _v, single=_p in F.TRUTH_SINGLE)
for _p, _v in F.IND_SUBJ.items():
    add_s(_p, _v, single=_p in F.IND_SINGLE)
add_s("Bāvīsatindriyā", "Hai mươi hai năng lực")
for _n, _np in ((3, "Tayo"), (6, "Cha"), (7, "Satta"), (9, "Nava")):
    add_s(f"{_np} hetū", f"{NUMV[_n]} gốc rễ")
for _h, _hv in (("kusalahetū", KUS_H), ("akusalahetū", AKUS_H), ("abyākatahetū", ABY_H)):
    add_s(f"Tayo {_h}", f"ba {_hv}")
for _p in ("doso akusalahetu", "moho akusalahetu", "kabaḷīkāro āhāro", "manoviññāṇadhātusamphasso",
           "kāyaviññāṇadhātusamphasso", "manodhātusamphasso", "manoviññāṇadhātusamphassajā vedanā",
           "manoviññāṇadhātusamphassajā saññā", "manoviññāṇadhātusamphassajā cetanā"):
    add_s(_p, NAME[_p])
for _n, _np in ((3, "Tayo"), (4, "Cattāro")):
    add_s(f"{_np} āhārā", f"{NUMV[_n]} {UNIT['ahara']}")
for _n, _np in ((5, "Pañca"), (6, "Cha"), (7, "Satta")):
    add_s(f"{_np} phassā", f"{NUMV[_n]} {UNIT['phassa']}")
    for _pn, _u in (("vedanā", "vedana"), ("saññā", "sanna"), ("cetanā", "cetana"), ("cittā", "citta")):
        add_s(f"{_np} {_pn}", f"{NUMV[_n]} {UNIT[_u]}")
for _p, (_v, _s) in list(SUBJ.items()):
    assert "  " not in _v and _v == _v.strip(), _p
_KEYS = "|".join(map(re.escape, sorted(SUBJ, key=len, reverse=True)))
CHAIN = re.compile(rf"^(?:{_KEYS})(?: ?…(?:pe…)? ?(?:{_KEYS}))*(?= )")
TI = re.compile(r"(n?)ti ?pi$|(n?)ti$")
NV = "không nên nói rằng"   # na vattabbā Xtipi (no dash, no quotes in this chapter) [ch9 notes: «không nên nói rằng X, hay rằng Y»]


def strip_ti(s):
    m = TI.search(s)
    assert m, s
    n = (m.group(1) or m.group(2) or "")
    return s[:m.start()] + ("ṃ" if n else "")


def subj_vi(p):
    parts = re.split(r" ?…(?:pe…)? ?", p)
    vs = [SUBJ[x] for x in parts]
    return "… ".join(v for v, _ in vs), len(vs) == 1 and vs[0][1]


def chunk(c, st):
    m = CHAIN.match(low(c))
    subj, single = None, False
    rest = low(c)
    if m:
        subj, single = subj_vi(m.group(0))
        rest = rest[m.end() + 1:]
    m = re.match(r"^(siyā )?na vattabb(?:o|ā|aṃ) (.+)$", rest)
    if m:
        vi = f"{NV} {lookup(strip_ti(m.group(2)))}"
        if m.group(1):
            vi = f"{B.SOMETIMES} {vi}"
        elif subj:
            vi = f"{THI} {vi}"
        st["nv"] = True
    elif st.get("nv"):
        vi = f"{B.OR} {lookup(strip_ti(rest))}"
    else:
        siya = rest.startswith("siyā ")
        vi = words(rest[5:] if siya else rest)
        if siya:
            vi = f"{B.SOMETIMES} {vi}"
    if subj is None:
        return vi
    if not vi.startswith(THI + " ") and ((single and not vi.startswith("là ")) or subj.endswith(" " + vi)):
        vi = f"{THI} {vi}"   # F.Q rule (single truth / faculty); «Ba gốc rễ thiện thì thiện»
    return f"{subj} {vi}"


FIXES = (   # punctuation / spacing in the Pāli, rendered as meant (reported)
    ("siyā kāmadhātu pariyāpanno", "siyā kāmadhātupariyāpanno"),
    ("siyā sārammaṇārammaṇo siyā anārammaṇārammaṇo", "siyā sārammaṇārammaṇo, siyā anārammaṇārammaṇo"),
    ("siyā vipākā siyā vipākadhammadhammā", "siyā vipākā, siyā vipākadhammadhammā"),
    ("siyā avitakkaavicāro siyā na vattabbo", "siyā avitakkaavicāro, siyā na vattabbo"),
    ("avitakkaavicārā manodhātu", "avitakkaavicārā, manodhātu"),
    ("satta cetanā satta cittā", "satta cetanā… satta cittā"),
    ("sampayuttoti pi", "sampayuttotipi"),
    ("lokuttarāti.", "lokuttarā."),
)


def ans(t):
    """A Pañhāpucchaka-type answer line (subjects + matrix-type predicates; "na vattabbā …tipi" without dash)."""
    for a, b in FIXES:
        if a in t:
            SLIPS.append(f"punctuation / spacing rendered as meant: '{a}'")
            t = t.replace(a, b)
    out = []
    for sent in re.split(r"(?<=\.) (?=[A-ZĀĪŪÑṬ])", t):
        assert sent.endswith("."), sent[-40:]
        tail = ""
        if sent.endswith(" 4."):   # stray digit in the Pāli: kept as written (reported)
            SLIPS.append("^2-1041 stray digit '4' after 'anupādinnupādāniyo': kept as written")
            sent, tail = sent[:-3] + ".", " 4"
        parts = re.split(r"(, |; )", sent[:-1])
        st, vi = {}, []
        for i, x in enumerate(parts):
            if i % 2:
                vi.append(x)
                if x == "; ":
                    st = {}
            else:
                if x.startswith("siyā ") is False and not x.startswith("na ") and CHAIN.match(low(x)):
                    st = {}   # a new subject starts a new clause
                vi.append(chunk(x, st))
        out.append(cap("".join(vi)) + tail + ".")
    return " ".join(out)


def pq(preds, last=None):
    """Pañcannaṃ khandhānaṃ kati X, kati Y…pe… sattannaṃ cittānaṃ kati X, kati Y?"""
    g1 = ", ".join(f"bao nhiêu khối {p}" for p in preds)
    g2 = ", ".join(f"bao nhiêu loại tâm {p}" for p in (last or preds))
    return f"Trong năm khối, {g1}… trong bảy loại tâm, {g2}?"


# ================================================================ 4. the planes (Uppattānuppatti / Dhammadassana)
RDEF = re.compile(r'^Tattha katam\w+ (kāmadhātuyā|rūpadhātuyā|arūpadhātuyā|apariyāpanne) ([^?]+)\? (.+) – '
                  r'(?:ime|imāni|imā|ayaṃ|idaṃ) vucca(?:nti|ti|tti) "(\w+) ([^"]+)"\.$')


def realm_def(t):
    m = RDEF.match(t)
    assert m and m.group(1) == m.group(4) and m.group(2) == m.group(5), t[:80]
    if "vuccatti" in t:
        SLIPS.append("^2-992 'imā vuccatti' (= vuccanti): rendered as meant")
    name = f"{count_vi(m.group(2))} trong {REALM[m.group(1)]}"
    return f"{TATTHA} {name} là gì? {cap(members_vi(m.group(3)))} {DASH} {called(name)}."


def realm_count_q(realm, units, pe_after=None):
    """Kāmadhātuyā kati khandhā, kati āyatanāni, …? -> «Trong cõi dục lạc có bao nhiêu khối, …?»"""
    body = ", ".join(f"bao nhiêu {UNIT[u]}" for u in units)
    if pe_after is not None:
        body = ", ".join(f"bao nhiêu {UNIT[u]}" for u in units[:pe_after]) + f"… bao nhiêu {UNIT[units[-1]]}"
    return f"Trong {REALM[realm]} có {body}?"


def realm_count_a(t):
    """Kāmadhātuyā pañcakkhandhā, dvādasāyatanāni, … -> «Trong cõi dục lạc có năm khối, …»"""
    m = re.match(r"^(Kāmadhātuyā|Rūpadhātuyā|Arūpadhātuyā|Apariyāpanne) (.+)\.$", t)
    return f"Trong {REALM[low(m.group(1))]} có " + ", ".join(count_vi(x) for x in m.group(2).split(", ")) + "."


UPK = "vào khoảnh khắc tái sinh"   # upapattikkhaṇe [new; pi-1 upapanna «đã tái sinh»]
APPEAR = "xuất hiện"                # pātubhavati [ch4 pātubhāva «sự xuất hiện»]
WHO = {"sabbesaṃ": "ở tất cả chúng sinh", "kassaci": "ở một số chúng sinh"}
ALL = WHO["sabbesaṃ"]
THESE = "ở những chúng sinh ấy"     # etesaṃ
ASANNA = "chư thiên Vô Tưởng"       # asaññasattā devā [new; traditional name, as pi-1 Sắc Cứu Cánh]
NOROOT = "sự xuất hiện không có gốc rễ"   # ahetukā pātubhavanti [new]


def rt(realm_p):
    return f"Trong {REALM[low(realm_p)]}, {UPK}"


def dd_question(realm_p):
    return f"{rt(realm_p)}, bao nhiêu {UNIT['khandha']} {APPEAR}… bao nhiêu {UNIT['citta']} {APPEAR}?"


def dd_count(t):
    """the long count line of a plane (clauses with sabbesaṃ / kassaci)."""
    m = re.match(r"^(Kāmadhātuyā|Rūpadhātuyā|Arūpadhātuyā) upapattikkhaṇe(, ṭhapetvā asaññasattānaṃ devānaṃ,)? "
                 r"(.+)\.$", t)
    head = rt(m.group(1)) + ", " + (f"ngoại trừ {ASANNA}, " if m.group(2) else "")
    sep = "; " if "; " in m.group(3) else ", "
    out = []
    for c in m.group(3).split(sep):
        if c == "kassaci [keci (syā.)] ahetukā pātubhavanti":
            out.append(f"{WHO['kassaci']} {VAR['[keci (syā.)]']}, {NOROOT}")
            continue
        mm = re.match(r"^(?:(sabbesaṃ|kassaci) )?(aparāni |aparā )?(.+?) pātubhava(?:nti|ti)$", c)
        cnt = chain_vi(mm.group(3)) + (" khác" if mm.group(2) else "")
        out.append((WHO[mm.group(1)] + ", " if mm.group(1) else "") + f"{cnt} {APPEAR}")
    return head + sep.join(out) + "."


# beings (genitive) [new unless marked]
GEN = [   # (Pāli, Vietnamese, is_noun)
    ("kāmāvacarānaṃ devānaṃ", "chư thiên thuộc cõi dục lạc", True),        # kāmāvacara pi-1
    ("paṭhamakappikānaṃ manussānaṃ", "loài người ở thời kỳ đầu của kiếp", True),   # kappa = kiếp [pi-1 core]
    ("opapātikānaṃ petānaṃ", "ngạ quỷ hóa sinh", True),                       # opapātika pi-1 «hóa sinh»; ch16 «ngạ quỷ»
    ("opapātikānaṃ asurānaṃ", "a-tu-la hóa sinh", True),
    ("opapātikānaṃ tiracchānagatānaṃ", "loài súc sinh hóa sinh", True),      # ch16 «loài súc sinh»
    ("nerayikānaṃ", "chúng sinh địa ngục", True),                            # ch16 «địa ngục»
    ("jaccandhabadhirānaṃ", "những chúng sinh vừa mù vừa điếc bẩm sinh", True),
    ("jaccandhānaṃ", "những chúng sinh mù bẩm sinh", True),
    ("jaccabadhirānaṃ", "những chúng sinh điếc bẩm sinh", True),
    ("gabbhaseyyakānaṃ sattānaṃ", "những chúng sinh sinh ra từ bào thai", True),
    ("ṭhapetvā napuṃsakānaṃ", "ngoại trừ những chúng sinh không có giới tính", False),
    ("paripuṇṇāyatanānaṃ", "có đầy đủ các lĩnh vực nhận biết", False),
    ("sahetukānaṃ ñāṇasampayuttānaṃ", "có gốc rễ, gắn liền với hiểu biết", False),     # pi-1 ñāṇasampayutta
    ("sahetukānaṃ ñāṇavippayuttānaṃ", "có gốc rễ, không gắn liền với hiểu biết", False),
    ("ahetukānaṃ", "không có gốc rễ", False),
    ("napuṃsakānaṃ", "không có giới tính", False),
]


def beings_vi(p):
    """genitive list -> «của X, của Y …» (attributes after their noun; a missing comma between nouns is added)."""
    segs = []
    for seg in low(p).split(", "):
        s, out = seg, []
        while s:
            for gp, gv, noun in GEN:
                if s == gp or s.startswith(gp + " "):
                    if noun and out and out[-1][1]:
                        SLIPS.append("^2-1009 … ^2-1012 comma missing between 'tiracchānagatānaṃ' and 'nerayikānaṃ' "
                                     "in several lines: rendered as a list")
                        segs.append(" ".join(x for x, _ in out))
                        out = []
                    out.append(("của " + gv if noun else gv, noun))
                    s = s[len(gp):].lstrip(" ")
                    break
            else:
                raise KeyError("beings: " + s)
        segs.append(" ".join(x for x, _ in out))
    return ", ".join(segs)


def dd_who(t):
    m = re.match(r"^(Kāmadhātuyā) upapattikkhaṇe kassa (aparāni |aparā )?(.+?) pātubhavanti\? (.+?),? "
                 r"upapattikkhaṇe (.+?) pātubhavanti – (.+?)\. Kāmadhātuyā upapattikkhaṇe etesaṃ "
                 r"(?:imāni|imā|ime) (.+?) pātubhavanti\.( Avasesānaṃ sattānaṃ \[avasesā sattā \(\?\)\] ahetukā "
                 r"pātubhavanti\.)?$", t)
    assert m and m.group(3) == m.group(5) == m.group(7), t[:90]
    cnt = count_vi(m.group(3))
    qv = cnt + (" khác" if m.group(2) else "")
    out = (f"{rt(m.group(1))}, {qv} {APPEAR} ở những ai? {UPK.capitalize()} {beings_vi(m.group(4))}, {cnt} {APPEAR} "
           f"{DASH} {members_vi(m.group(6))}. {rt(m.group(1))}, {cnt} này {APPEAR} {THESE}.")
    if m.group(8):
        out += f" Ở những chúng sinh còn lại {VAR['[avasesā sattā (?)]']}, {NOROOT}."
    return out


def dd_which(t):
    m = re.match(r"^(Kāmadhātuyā|Rūpadhātuyā|Arūpadhātuyā) upapattikkhaṇe (sabbesaṃ )?katam\w+ (.+?) "
                 r"pātubhava(?:nti|ti)([?.]) (.+) – (kāmadhātuyā|rūpadhātuyā|arūpadhātuyā) upapattikkhaṇe "
                 r"(sabbesaṃ )?(?:ime|imāni|imā|idaṃ|ayaṃ) (.+?) pātubhava(?:nti|ti)\.$", t)
    assert m and low(m.group(1)) == m.group(6) and m.group(2) == m.group(7), t[:90]
    if m.group(4) == ".":
        SLIPS.append("^2-1014 'katame cattāro āhārā pātubhavanti.' closes the question with '.': rendered with '?'")
    who = f" {ALL}" if m.group(2) else ""
    q = chain_vi(m.group(3))
    last = re.split(r"\s?…(?:pe…)?\s?", m.group(3))[-1]
    assert m.group(8) == last, (m.group(8), last)
    return (f"{rt(m.group(1))}, {q} nào {APPEAR}{who}? {cap(members_vi(m.group(5)))} {DASH} "
            f"{low(rt(m.group(1)))}, {count_vi(m.group(8))} này {APPEAR}{who}.")


# ================================================================ 5. hand lines (in order)
H = []


def h(key, vi):
    H.append((key, vi))


def hd(level, pali, vi):
    H.append(("#" * level + " " + pali, "#" * level + " " + vi))


def hutu_three(kind, which):
    """Tattha katame tayo kusalahetū? Alobho kusalahetu, … – ime tayo kusalahetū."""
    hv = {"kusalahetu": KUS_H, "akusalahetu": AKUS_H}[kind]
    roots = {"kusalahetu": ("alobho", "adoso", "amoho"), "akusalahetu": ("lobho", "doso", "moho")}[kind]
    rs = [r for r in roots if r in which]
    n = NUMV[len(rs)]
    lst = ", ".join(NAME[f"{r} {kind}"] for r in rs)
    return f"{TATTHA} {n} {hv} là gì? {cap(lst)} {DASH} đó là {n} {hv}."


def aby_three(body, close):
    return f"{TATTHA} ba {ABY_H} là gì? {body} {DASH} đó là ba {ABY_H}. {close}"


SEC = {   # #### headings (vāra = «mục», APPROVED) [new]
    "Sabbasaṅgāhikavāro": "Mục bao gồm tất cả",
    "Uppattānuppattivāro": "Mục về những gì sinh khởi và không sinh khởi",
    "Pariyāpannāpariyāpannavāro": "Mục về những gì nằm trong và không nằm trong",
    "Dhammadassanavāro": "Mục trình bày các hiện tượng",
    "Bhūmantaradassanavāro": "Mục trình bày sự khác biệt giữa các cõi",
    "Uppādakakammaāyuppamāṇavāro": "Mục về nghiệp tạo ra sự tái sinh và tuổi thọ",
    "Abhiññeyyādivāro": "Mục về những gì cần được hiểu biết trực tiếp và các điều khác",
    "Sārammaṇānārammaṇavāro": "Mục về những gì có đối tượng và không có đối tượng",
    "Diṭṭhasutādidassanavāro": "Mục trình bày những gì được thấy, được nghe và các điều khác",
    "Tikādidassanavāro": "Mục trình bày các bộ ba và các bộ khác",
}
SUB = {"Kāmadhātu": cap(REALM["kāmadhātuyā"]), "Rūpadhātu": cap(REALM["rūpadhātuyā"]),
       "Arūpadhātu": cap(REALM["arūpadhātuyā"]), "Apariyāpannaṃ": cap(REALM["apariyāpanne"])}

hd(3, "Dhammahadayavibhaṅgo", S.CHAPTER_TITLES[18])
# ---------------------------------------------------------------- Sabbasaṅgāhikavāro
hd(4, "Sabbasaṅgāhikavāro", SEC["Sabbasaṅgāhikavāro"])
h("Kati khandhā, kati āyatanāni", "Có " + ", ".join(f"bao nhiêu {UNIT[u]}" for u in ORDER12) + "?")
h("Pañcakkhandhā, dvādasāyatanāni", cap(", ".join(count_vi(x) for x in (
    "pañcakkhandhā", "dvādasāyatanāni", "aṭṭhārasa dhātuyo", "cattāri saccāni", "bāvīsatindriyāni", "nava hetū",
    "cattāro āhārā", "satta phassā", "satta vedanā", "satta saññā", "satta cetanā", "satta cittāni"))) + ".")


def all_def(count_p, members_p):
    name = count_vi(count_p)
    return f"{TATTHA} {name} là gì? {cap(members_vi(members_p))} {DASH} {called(name)}."


def all_line(t):
    m = re.match(r'^Tattha katam\w+ ([^?]+)\? (.+) – (?:ime|imāni|imā) vuccanti "([^"]+)"\.$', t)
    assert m and m.group(1) == m.group(3), t[:60]
    return all_def(m.group(1), m.group(2))


for _k in ("pañcakkhandhā", "dvādasāyatanāni", "aṭṭhārasa dhātuyo", "cattāri saccāni", "bāvīsatindriyāni"):
    h(f"Tattha katam\x00{_k}?", all_line)
h("Tattha katame nava hetū?", f"{TATTHA} chín gốc rễ là gì? Ba {KUS_H}, ba {AKUS_H}, ba {ABY_H}.")
h("Tattha katame tayo kusalahetū?", hutu_three("kusalahetu", ("alobho", "adoso", "amoho")))
h("Tattha katame tayo akusalahetū?", hutu_three("akusalahetu", ("lobho", "doso", "moho")))
h("Tattha katame tayo abyākatahetū?", aby_three(ABY_BODY_KV, f"{cap(called('chín gốc rễ'))}."))
for _k in ("cattāro āhārā", "satta phassā", "satta vedanā", "satta saññā", "satta cetanā", "satta cittāni"):
    h(f"Tattha katam\x00{_k}?", all_line)

# ---------------------------------------------------------------- Uppattānuppattivāro
hd(4, "Uppattānuppattivāro", SEC["Uppattānuppattivāro"])
hd(5, "Kāmadhātu", SUB["Kāmadhātu"])
h("Kāmadhātuyā kati khandhā", realm_count_q("kāmadhātuyā", ORDER12))
h("Kāmadhātuyā pañcakkhandhā", realm_count_a)
for _k in ("pañcakkhandhā", "dvādasāyatanāni", "aṭṭhārasa dhātuyo", "tīṇi saccāni", "bāvīsatindriyāni"):
    h(f"Tattha katam\x00kāmadhātuyā {_k}?", realm_def)
h("Tattha katame kāmadhātuyā nava hetū?",
  f"{TATTHA} chín gốc rễ trong {REALM['kāmadhātuyā']} là gì? Ba {KUS_H}, ba {AKUS_H}, ba {ABY_H}… "
  f"{called('chín gốc rễ trong ' + REALM['kāmadhātuyā'])}.")
for _k in ("cattāro āhārā", "satta phassā", "satta vedanā", "satta saññā", "satta cetanā", "satta cittāni"):
    h(f"Tattha katam\x00kāmadhātuyā {_k}?", realm_def)
hd(5, "Rūpadhātu", SUB["Rūpadhātu"])
h("Rūpadhātuyā kati khandhā", realm_count_q("rūpadhātuyā", ORDER12, pe_after=5))
h("Rūpadhātuyā pañcakkhandhā", realm_count_a)
for _k in ("pañcakkhandhā", "cha āyatanāni", "nava dhātuyo", "tīṇi saccāni", "cuddasindriyāni"):
    h(f"Tattha katam\x00rūpadhātuyā {_k}?", realm_def)
_R8 = f"tám gốc rễ trong {REALM['rūpadhātuyā']}"
h("Tattha katame rūpadhātuyā aṭṭha hetū?", f"{TATTHA} {_R8} là gì? Ba {KUS_H}, hai {AKUS_H}, ba {ABY_H}.")
h("Tattha katame tayo kusalahetū?", hutu_three("kusalahetu", ("alobho", "adoso", "amoho")))
h("Tattha katame dve akusalahetū?", hutu_three("akusalahetu", ("lobho", "moho")))
SLIPS.append("^2-994 'Ime vuccanti rūpadhātuyā aṭṭha hetū.' unquoted (the parallels quote): kept unquoted")
h("Tattha katame tayo abyākatahetū?", aby_three(ABY_BODY_KV, f"{cap(S.VUCCATI)} {_R8}."))
for _k in ("tayo āhārā", "cattāro phassā"):
    h(f"Tattha katam\x00rūpadhātuyā {_k}?", realm_def)
_R4 = f"bốn {UNIT['citta']} trong {REALM['rūpadhātuyā']}"
h("Tattha katamā rūpadhātuyā catasso vedanā…pe…",
  f"{TATTHA} {chain_vi('catasso vedanā…pe… catasso saññā…pe… catasso cetanā…pe… cattāri cittāni')} trong "
  f"{REALM['rūpadhātuyā']} là gì? {cap(members_vi('cakkhuviññāṇaṃ, sotaviññāṇaṃ, manodhātu, manoviññāṇadhātu'))} "
  f"{DASH} {called(_R4)}.")
hd(5, "Arūpadhātu", SUB["Arūpadhātu"])
h("Arūpadhātuyā kati khandhā…pe… kati cittāni?", realm_count_q("arūpadhātuyā", ["khandha", "citta"], pe_after=1))
h("Arūpadhātuyā cattāro khandhā", realm_count_a)
for _k in ("cattāro khandhā", "dve āyatanāni", "dve dhātuyo", "tīṇi saccāni", "ekādasindriyāni"):
    h(f"Tattha katam\x00arūpadhātuyā {_k}?", realm_def)
h("Tattha katame arūpadhātuyā aṭṭha hetū?",
  f"{TATTHA} tám gốc rễ trong {REALM['arūpadhātuyā']} là gì? Ba {KUS_H}, hai {AKUS_H}, ba {ABY_H}… "
  f"{called('tám gốc rễ trong ' + REALM['arūpadhātuyā'])}.")
for _k in ("tayo āhārā", "eko phasso"):
    h(f"Tattha katam\x00arūpadhātuyā {_k}?", realm_def)


def one_chain(realm_p):
    name = f"một {UNIT['citta']} trong {REALM[realm_p]}"
    return (f"{TATTHA} {chain_vi('ekā vedanā…pe… ekā saññā…pe… ekā cetanā…pe… ekaṃ cittaṃ')} trong {REALM[realm_p]} "
            f"là gì? {cap(NAME['manoviññāṇadhātu'])} {DASH} {called(name)}.")


h("Tattha katamā arūpadhātuyā ekā vedanā…pe…", one_chain("arūpadhātuyā"))
hd(5, "Apariyāpannaṃ", SUB["Apariyāpannaṃ"])
h("Apariyāpanne kati khandhā…pe… kati cittāni?", realm_count_q("apariyāpanne", ["khandha", "citta"], pe_after=1))
h("Apariyāpanne cattāro khandhā", realm_count_a)
for _k in ("cattāro khandhā", "dve āyatanāni", "dve dhātuyo", "dve saccāni", "dvādasindriyāni"):
    h(f"Tattha katam\x00apariyāpanne {_k}?", realm_def)
h("Tattha katame apariyāpanne cha hetū?",
  f"{TATTHA} sáu gốc rễ trong {REALM['apariyāpanne']} là gì? Ba {KUS_H}, ba {ABY_H}.")
h("Tattha katame tayo kusalahetū?", hutu_three("kusalahetu", ("alobho", "adoso", "amoho")))
h("Tattha katame tayo abyākatahetū?",
  aby_three(ABY_BODY_K, f"{cap(called('sáu gốc rễ trong ' + REALM['apariyāpanne']))}."))
for _k in ("tayo āhārā", "eko phasso"):
    h(f"Tattha katam\x00apariyāpanne {_k}?", realm_def)
h("Tattha katamā apariyāpanne ekā vedanā…pe…", one_chain("apariyāpanne"))

# ---------------------------------------------------------------- Pariyāpannāpariyāpannavāro
hd(4, "Pariyāpannāpariyāpannavāro", SEC["Pariyāpannāpariyāpannavāro"])
for _sub, _r in (("Kāmadhātu", "kāma"), ("Rūpadhātu", "rūpa"), ("Arūpadhātu", "arūpa")):
    hd(5, _sub, SUB[_sub])
    h(f"Pañcannaṃ khandhānaṃ kati {_r}dhātupariyāpannā",
      pq([P(f"c18_{_r}_pariy"), P(f"c18_na_{_r}_pariy")]))
    for _ in range({"kāma": 9, "rūpa": 9, "arūpa": 10}[_r]):
        h("", ans)
hd(5, "Pariyāpannāpariyāpannaṃ", "Nằm trong và không nằm trong các cõi tồn tại")
h("Pañcannaṃ khandhānaṃ kati pariyāpannā", pq([P("pariyapanna"), P("apariyapanna")]))
for _ in range(9):
    h("", ans)

# ---------------------------------------------------------------- Dhammadassanavāro
hd(4, "Dhammadassanavāro", SEC["Dhammadassanavāro"])
hd(5, "Kāmadhātu", SUB["Kāmadhātu"])
h("Kāmadhātuyā upapattikkhaṇe kati khandhā", dd_question("Kāmadhātuyā"))
h("Kāmadhātuyā upapattikkhaṇe sabbesaṃ pañcakkhandhā", dd_count)
h("Kāmadhātuyā upapattikkhaṇe sabbesaṃ katame pañcakkhandhā", dd_which)
for _ in range(10):
    h("Kāmadhātuyā upapattikkhaṇe kassa ", dd_who)
h("Kāmadhātuyā upapattikkhaṇe sabbesaṃ katamaṃ ekaṃ saccaṃ", dd_which)
for _ in range(14):
    h("Kāmadhātuyā upapattikkhaṇe kassa ", dd_who)
for _ in range(3):
    h("Kāmadhātuyā upapattikkhaṇe sabbesaṃ katam", dd_which)
hd(5, "Rūpadhātu", SUB["Rūpadhātu"])
h("Rūpadhātuyā upapattikkhaṇe kati khandhā", dd_question("Rūpadhātuyā"))
h("Rūpadhātuyā upapattikkhaṇe, ṭhapetvā", dd_count)
for _ in range(9):
    h("Rūpadhātuyā upapattikkhaṇe katam", dd_which)
hd(5, "Asaññasattā", "Chúng sinh Vô Tưởng")
_AS = f"{cap(UPK)} của {ASANNA}"
h("Asaññasattānaṃ devānaṃ upapattikkhaṇe kati khandhā",
  f"{_AS}, bao nhiêu {UNIT['khandha']} {APPEAR}… bao nhiêu {UNIT['citta']} {APPEAR}?")
h("Asaññasattānaṃ devānaṃ upapattikkhaṇe eko khandho",
  f"{_AS}, một khối {APPEAR} {DASH} {NAME['rūpakkhandho']}; hai lĩnh vực nhận biết {APPEAR} {DASH} "
  f"{NAME['rūpāyatanaṃ']}, {NAME['dhammāyatanaṃ']}; hai yếu tố {APPEAR} {DASH} {NAME['rūpadhātu']}, "
  f"{NAME['dhammadhātu']}; một sự thật {APPEAR} {DASH} {NAME['dukkhasaccaṃ']}; một năng lực {APPEAR} {DASH} "
  f"{F.RUPA_JIV}. {cap(ASANNA)} {APPEAR} mà không có gốc rễ, không có dưỡng chất, không có sự tiếp xúc, "
  f"không có cảm giác, không có tri giác, không có chủ ý, không có tâm.")
hd(5, "Arūpadhātu", SUB["Arūpadhātu"])
h("Arūpadhātuyā upapattikkhaṇe kati khandhā", dd_question("Arūpadhātuyā"))
h("Arūpadhātuyā upapattikkhaṇe cattāro khandhā", dd_count)
for _ in range(9):
    h("Arūpadhātuyā upapattikkhaṇe katam", dd_which)

# ---------------------------------------------------------------- Bhūmantaradassanavāro (pi-1 ^1-1287 … ^1-1294)
hd(4, "Bhūmantaradassanavāro", SEC["Bhūmantaradassanavāro"])
_mx = ["kamavacara", "na_kamavacara", "rupavacara", "na_rupavacara", "arupavacara", "na_arupavacara",
       "pariyapanna", "apariyapanna"]
h("Kāmāvacarā dhammā, na kāmāvacarā dhammā", cap(", ".join(f"những hiện tượng {P(k)}" for k in _mx)) + ".")
_PI1_REALM = {
    "1-1287": [(" [khác chính tả (Sī., Ka.): paranimmitavasavattideve]", "")],
    "1-1288": [],
    "1-1289": [(" [khác chính tả (Sī., Ka.): akaniṭṭhadeve]", ""), (" [dị bản (Ka.): diṭṭhadhammasukhavihārassa]", "")],
    "1-1290": [], "1-1291": [], "1-1292": [],
    "1-1293": [("khối vật chất… khối thức", ", ".join(KHV))],   # the pi-2 Pāli lists the five aggregates in full
    "1-1294": [],
}
_REALM_KEYS = ["Katame dhammā kāmāvacarā?", "Katame dhammā na kāmāvacarā?", "Katame dhammā rūpāvacarā?",
               "Katame dhammā na rūpāvacarā?", "Katame dhammā arūpāvacarā?", "Katame dhammā na arūpāvacarā?",
               "Katame dhammā pariyāpannā?", "Katame dhammā apariyāpannā?"]
for _bid, _key in zip(_PI1_REALM, _REALM_KEYS):
    _v = pi1(_bid)
    for _a, _b in _PI1_REALM[_bid]:
        _v = repl(_v, _a, _b)
    h(_key, _v)

# ---------------------------------------------------------------- Uppādakakammaāyuppamāṇavāro
hd(4, "Uppādakakammaāyuppamāṇavāro", SEC["Uppādakakammaāyuppamāṇavāro"])
hd(5, "Uppādakakammaṃ", "Nghiệp tạo ra sự tái sinh")
DEVA = "chư thiên"
D_SAMM, D_UPAP, D_VISU = "chư thiên theo quy ước", "chư thiên do tái sinh", "chư thiên do sự trong sạch"   # [new]
GODS = {   # traditional names, as pi-1 «Tha Hóa Tự Tại», «Sắc Cứu Cánh» [new]
    "cātu": "Tứ Đại Thiên Vương", "tāva": "Ba Mươi Ba", "yāma": "Dạ Ma", "tusita": "Đâu Suất",
    "nimmāna": "Hóa Lạc", "paranimmita": "Tha Hóa Tự Tại", "pārisajja": "Phạm Chúng", "purohita": "Phạm Phụ",
    "mahābrahma": "Đại Phạm", "parittābha": "Thiểu Quang", "appamāṇābha": "Vô Lượng Quang", "ābhassara": "Quang Âm",
    "parittasubha": "Thiểu Tịnh", "appamāṇasubha": "Vô Lượng Tịnh", "subhakiṇha": "Biến Tịnh",
    "asañña": "Vô Tưởng", "vehapphala": "Quảng Quả", "aviha": "Vô Phiền", "atappa": "Vô Nhiệt",
    "sudassa": "Thiện Hiện", "sudassī": "Thiện Kiến", "akaniṭṭha": "Sắc Cứu Cánh",
}
assert "chư thiên Tha Hóa Tự Tại" in pi1("1-1287") and "chư thiên Sắc Cứu Cánh" in pi1("1-1289")
assert f"{DEVA} {GODS['asañña']}" == ASANNA
FORMLESS = {   # pi-1 ^1-1291 «chư thiên sinh vào lĩnh vực …»
    "ākāsa": "chư thiên sinh vào lĩnh vực không gian vô tận", "viññāṇa": "chư thiên sinh vào lĩnh vực thức vô tận",
    "ākiñcañña": "chư thiên sinh vào lĩnh vực không có gì cả",
    "nevasaññā": "chư thiên sinh vào lĩnh vực không phải tri giác cũng không phải không tri giác",
}
assert FORMLESS["ākāsa"] in pi1("1-1291") and FORMLESS["nevasaññā"] in pi1("1-1291")
for _k in ("viññāṇa", "ākiñcañña"):
    assert FORMLESS[_k][len("chư thiên sinh vào "):] in _ch3 + vi_file("12-jhanavibhango.md"), _k


def god(k):
    return FORMLESS[k] if k in FORMLESS else f"{DEVA} {GODS[k]}"


REBORN = "tái sinh vào cộng đồng của"   # sahabyataṃ upapajjanti [new]
SOME = "một số người"                   # appekacce [new]
h("Devāti. Tayo devā",
  f"“{cap(DEVA)}”. Ba loại {DEVA} {DASH} {D_SAMM} {VAR['[sammatidevā (syā.)]']}, {D_UPAP}, {D_VISU}.")
h("Sammutidevā nāma", f"{cap(D_SAMM)} nghĩa là {DASH} các vị vua, các hoàng hậu, các hoàng tử.")
h("Upapattidevā nāma",
  f"{cap(D_UPAP)} nghĩa là {DASH} {DEVA} kể từ {god('cātu')} {VAR['[cātummahārājike (sī. syā.)]']} trở lên.")
h("Visuddhidevā nāma", f"{cap(D_VISU)} nghĩa là {DASH} các vị A-la-hán được gọi như vậy.")
_GIFT = "Sau khi bố thí, thọ trì giới hạnh, thực hiện việc giữ ngày trai giới"   # [new; samādiyati ch16 «thọ trì»]
_HUM = ["những người quý tộc giàu có", "những bà-la-môn giàu có", "những gia chủ giàu có"]   # [new; ch17 khattiya]
_SIX = ["cātu", "tāva", "yāma", "tusita", "nimmāna", "paranimmita"]
h("Dānaṃ datvā, sīlaṃ samādiyitvā",
  f"{_GIFT}, người ta tái sinh vào đâu? {_GIFT}, " +
  ", ".join(f"{SOME} {REBORN} {x}" for x in _HUM + [god(k) for k in _SIX]) + ".")
hd(5, "Āyuppamāṇaṃ", "Tuổi thọ")
AYU = "tuổi thọ"   # āyuppamāṇa [new]
h("Manussānaṃ kittakaṃ āyuppamāṇaṃ?",
  f"{cap(AYU)} của loài người là bao nhiêu? Một trăm năm, ít hơn hoặc nhiều hơn "
  f"{VAR['[appaṃ vā bhiyyo vā (syā. ka.) dī. ni. 2.7]']}.")
# human-count totals computed (as the English / Russian rails); checked: divine years × 360 × human years per day
_AY = [("cātu", "Năm mươi năm", 50, "năm trăm năm", 500, "Chín triệu năm", 9_000_000),
       ("tāva", "Một trăm năm", 100, "một nghìn năm", 1000, "Ba mươi sáu triệu năm", 36_000_000),
       ("yāma", "Hai trăm năm", 200, "hai nghìn năm", 2000, "Một trăm bốn mươi bốn triệu năm", 144_000_000),
       ("tusita", "Bốn trăm năm", 400, "bốn nghìn năm", 4000, "Năm trăm bảy mươi sáu triệu năm", 576_000_000),
       ("nimmāna", "Tám trăm năm", 800, "tám nghìn năm", 8000, "Hai tỷ ba trăm lẻ bốn triệu năm", 2_304_000_000),
       ("paranimmita", "Một nghìn sáu trăm năm", 1600, "mười sáu nghìn năm", 16000,
        "Chín tỷ hai trăm mười sáu triệu năm", 9_216_000_000)]
_KEYS_AY = ["Cātumahārājikānaṃ devānaṃ kittakaṃ", "Tāvatiṃsānaṃ devānaṃ kittakaṃ", "Yāmānaṃ devānaṃ kittakaṃ",
            "Tusitānaṃ devānaṃ kittakaṃ", "Nimmānaratīnaṃ devānaṃ kittakaṃ", "Paranimmitavasavattīnaṃ devānaṃ kittakaṃ"]
for (_g, _hy, _hn, _dy, _dn, _tot, _tn), _key in zip(_AY, _KEYS_AY):
    assert _dn * 360 * _hn == _tn, _g
    _var = f" {VAR['[rattidivo (ka.) a. ni. 3.71]']}" if _g == "cātu" else ""
    h(_key, f"{cap(AYU)} của {god(_g)} là bao nhiêu? {_hy} của loài người là một ngày một đêm{_var} của {god(_g)}. "
            f"Ba mươi đêm như thế là một tháng. Mười hai tháng như thế là một năm. Tính theo năm ấy, {_dy} cõi trời "
            f"là {AYU} của {god(_g)}. Theo cách tính của loài người thì là bao nhiêu? {_tot}.")
assert sum(x[-1] for x in _AY) == 1200 * 10_000_000 + 28 * 10_000_000 + 50 * 100_000
h("Cha ete [chapi te (syā.)] kāmāvacarā",
  f"Sáu hàng {DEVA} này {VAR['[chapi te (syā.)]']} thuộc cõi dục lạc, có đầy đủ mọi dục lạc;")
h("Sabbesaṃ ekasaṅkhāto", f"{cap(AYU)} của tất cả, khi tính gộp làm một, là bao nhiêu?")
SLIPS.append("^2-1023 verse 'āyu bhavati kittako.' (a question closed with '.'): rendered with '?'")
h("Dvādasa koṭisataṃ tesaṃ", f"{cap(AYU)} của họ là mười hai tỷ năm, cùng hai trăm tám mươi triệu năm;")
h("Paññāsa satasahassāni", "Thêm năm triệu năm, đã được công bố theo cách tính năm.")
_J = {"Paṭhamaṃ": "thứ nhất", "Dutiyaṃ": "thứ hai", "Tatiyaṃ": "thứ ba", "Catutthaṃ": "thứ tư"}   # [pi-1]
_LV = {"parittaṃ": P("paritta"), "majjhimaṃ": P("majjhima"), "paṇītaṃ": P("panita")}       # hạn hẹp / trung bình / ưu việt
_JG = [("Paṭhamaṃ", "parittaṃ", "pārisajja", "Một phần ba kiếp"), ("Paṭhamaṃ", "majjhimaṃ", "purohita", "Nửa kiếp"),
       ("Paṭhamaṃ", "paṇītaṃ", "mahābrahma", f"Một kiếp {VAR['[eko kappo (syā.)]']}"),
       ("Dutiyaṃ", "parittaṃ", "parittābha", "Hai kiếp"), ("Dutiyaṃ", "majjhimaṃ", "appamāṇābha", "Bốn kiếp"),
       ("Dutiyaṃ", "paṇītaṃ", "ābhassara", "Tám kiếp"), ("Tatiyaṃ", "parittaṃ", "parittasubha", "Mười sáu kiếp"),
       ("Tatiyaṃ", "majjhimaṃ", "appamāṇasubha", "Ba mươi hai kiếp"),
       ("Tatiyaṃ", "paṇītaṃ", "subhakiṇha", "Sáu mươi bốn kiếp")]
for _j, _l, _g, _a in _JG:
    _d = f"Sau khi tu tập tầng thiền {_J[_j]} ở mức {_LV[_l]}"
    h(f"{_j} jhānaṃ {_l} bhāvetvā kattha",
      f"{_d}, người ta tái sinh vào đâu? {_d}, người ta {REBORN} {god(_g)}. {cap(AYU)} của họ là bao nhiêu? {_a}.")
_DIFF = ["đối tượng", "sự chú tâm", "ý muốn", "sự mong cầu", "sự quyết định", "sự định hướng", "trí tuệ"]   # [new]
_G11 = ["asañña", "vehapphala", "aviha", "atappa", "sudassa", "sudassī", "akaniṭṭha", "ākāsa", "viññāṇa",
        "ākiñcañña", "nevasaññā"]
h("Catutthaṃ jhānaṃ bhāvetvā ārammaṇanānattatā",
  f"Sau khi tu tập tầng thiền {_J['Catutthaṃ']}, do " + ", ".join(f"sự khác biệt về {x}" for x in _DIFF) + ", "
  + ", ".join(f"{SOME} {REBORN} {god(k)}" for k in _G11) + ".")
h("Asaññasattānañca vehapphalānañca devānaṃ",
  f"{cap(AYU)} của {god('asañña')} và {god('vehapphala')} là bao nhiêu? Năm trăm kiếp.")
for _g, _key, _a in (("aviha", "Avihānaṃ", "Một nghìn kiếp"), ("atappa", "Atappānaṃ", "Hai nghìn kiếp"),
                     ("sudassa", "Sudassānaṃ", "Bốn nghìn kiếp"), ("sudassī", "Sudassīnaṃ", "Tám nghìn kiếp"),
                     ("akaniṭṭha", "Akaniṭṭhānaṃ", "Mười sáu nghìn kiếp"),
                     ("ākāsa", "Ākāsānañcāyatanūpagānaṃ", "Hai mươi nghìn kiếp"),
                     ("viññāṇa", "Viññāṇañcāyatanūpagānaṃ", "Bốn mươi nghìn kiếp"),
                     ("ākiñcañña", "Ākiñcaññāyatanūpagānaṃ", "Sáu mươi nghìn kiếp"),
                     ("nevasaññā", "Nevasaññānāsaññāyatanūpagānaṃ", "Tám mươi bốn nghìn kiếp")):
    h(f"{_key} devānaṃ kittakaṃ", f"{cap(AYU)} của {god(_g)} là bao nhiêu? {_a}.")
VERSE = [   # ^2-1029 [new]
    ("Ukkhittā puññatejena", "Được uy lực của phước nâng lên, họ đi đến cõi tái sinh thuộc dục lạc và hình sắc."),
    ("Bhavaggatampi", f"Dù đã đạt đến đỉnh cao của sự hiện hữu {VAR['[bhavaggaṃ vāpi (syā.)]']}, họ vẫn trở lại "
                      f"{VAR['[puna gacchanti (syā.)]']} cõi xấu."),
    ("Tāva dīghāyukā sattā", "Chúng sinh sống lâu đến thế, cũng chết đi khi tuổi thọ cạn kiệt;"),
    ("Natthi koci bhavo nicco", "Không có sự hiện hữu nào thường còn, bậc Đại Hiền đã nói như vậy."),
    ("Tasmā hi dhīrā nipakā", "Vì thế, những người trí, khôn ngoan, tinh tế, biết suy xét điều lợi ích;"),
    ("Jarāmaraṇamokkhāya", "Để giải thoát khỏi sự lão hóa và sự chết, tu tập con đường tối thượng."),
    ("Bhāvayitvā suciṃ maggaṃ", "Sau khi tu tập con đường trong sạch, dẫn sâu vào Niết-bàn;"),
    ("Sabbāsave pariññāya", "Sau khi hiểu biết trọn vẹn mọi ô nhiễm, họ không còn ô nhiễm, nhập Niết-bàn trọn vẹn."),
]
for _k, _v in VERSE:
    h(_k, _v)

# ---------------------------------------------------------------- Abhiññeyyādivāro
hd(4, "Abhiññeyyādivāro", SEC["Abhiññeyyādivāro"])
_NONE3 = f"{P('c18_na_pahatabba')}, {P('c18_na_bhavetabba')}, {P('c18_na_sacchikatabba')}"
_AB = [P("c18_abhinneyya"), P("c18_parinneyya"), P("c18_pahatabba"), P("c18_bhavetabba"), P("c18_sacchikatabba"),
       _NONE3]
h("Pañcannaṃ khandhānaṃ kati abhiññeyyā", pq(_AB))
for _ in range(9):
    h("", ans)

# ---------------------------------------------------------------- Sārammaṇānārammaṇavāro
hd(4, "Sārammaṇānārammaṇavāro", SEC["Sārammaṇānārammaṇavāro"])
h("Pañcannaṃ khandhānaṃ kati sārammaṇā, kati anārammaṇā", pq([P("sarammana"), P("anarammana")]))
for _ in range(5):
    h("", ans)
h("Pañcannaṃ khandhānaṃ kati sārammaṇārammaṇā", pq([P("c18_sarammanarammana"), P("c18_anarammanarammana")]))
for _ in range(6):
    h("", ans)

# ---------------------------------------------------------------- Diṭṭhasutādidassanavāro
hd(4, "Diṭṭhasutādidassanavāro", SEC["Diṭṭhasutādidassanavāro"])
_NONE4 = ", ".join(P(f"c18_na_{k}") for k in ("dittha", "suta", "muta", "vinnata"))
h("Pañcannaṃ khandhānaṃ kati diṭṭhā", pq([P(f"c18_{k}") for k in ("dittha", "suta", "muta", "vinnata")] + [_NONE4]))
for _ in range(5):
    h("", ans)

# ---------------------------------------------------------------- Tikādidassanavāro
hd(4, "Tikādidassanavāro", SEC["Tikādidassanavāro"])
hd(5, "Kusalattikaṃ", "Bộ ba về thiện")   # ch1 kusalattika «bộ ba về thiện»
h("Pañcannaṃ khandhānaṃ kati kusalā", pq([P("kusala"), P("akusala"), P("abyakata")]))
for _ in range(3):
    h("", ans)
hd(5, "Vedanātikaṃ", "Bộ ba về cảm giác")
h("Pañcannaṃ khandhānaṃ kati sukhāya", pq([P("sukha_vs"), P("dukkha_vs"), P("adm_vs")]))
for _ in range(9):
    h("", ans)
hd(5, "Vipākattikaṃ", "Bộ ba về quả của nghiệp")
h("Pañcannaṃ khandhānaṃ kati vipākā", pq([P("vipaka"), P("vipakadhamma"), P("nevavipaka")]))
for _ in range(7):
    h("", ans)
hd(5, "Upādinnattikaṃ", "Bộ ba về những gì do nghiệp tạo ra")
h("Pañcannaṃ khandhānaṃ kati upādinnupādāniyā",
  pq([P("upadinnupadaniya"), P("anupadinnupadaniya"), P("anupadinnaanupadaniya")]))
for _ in range(7):
    h("", ans)
hd(5, "Vitakkattikaṃ", "Bộ ba về sự hướng tâm")
h("Pañcannaṃ khandhānaṃ kati savitakkasavicārā",
  pq([P("savitakkasavicara"), P("avitakkavicaramatta"), P("avitakkaavicara")]))
for _ in range(6):
    h("", ans)
hd(5, "(1) Rūpadukaṃ", "(1) Bộ đôi về vật chất")
h("Pañcannaṃ khandhānaṃ kati rūpā", pq([P("rupi"), P("arupi")]))
h("", ans)
hd(5, "(2) Lokiyadukaṃ", "(2) Bộ đôi về thế gian")
_LK = f"bao nhiêu {{u}} {P('lokiya')}, bao nhiêu {{u}} {P('lokuttara')}"
h("Pañcannaṃ khandhānaṃ kati lokiyā",
  f"Trong năm khối, {_LK.format(u='khối')}? Trong mười hai lĩnh vực nhận biết, {_LK.format(u='lĩnh vực')}? "
  f"Trong mười tám yếu tố, {_LK.format(u='yếu tố')}? Trong bốn sự thật, {_LK.format(u='sự thật')}… "
  f"trong bảy loại tâm, {_LK.format(u='loại tâm')}?")
h("", ans)
h("", ans)
h("Abhiññā dve sārammaṇā", "Cần được hiểu biết trực tiếp, hai mục về đối tượng, được thấy, thiện, cảm giác;")
h("Vipākā ca upādinnā", "Quả của nghiệp và do nghiệp tạo ra, sự hướng tâm, vật chất, thuộc thế gian.")
h("Dhammahadayavibhaṅgo niṭṭhito.", S.CHAPTER_CLOSING.format(title=S.CHAPTER_TITLES[18]))
COLOPHON = f"Bộ “{S.BOOK_TITLE}” đã hoàn tất."   # Vibhaṅgapakaraṇaṃ niṭṭhitaṃ. [pi-1 pattern]
_pi1_colophon = F.pi1_line("5-atthakathakandam.md", "Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ")
assert _pi1_colophon == "Bộ “Liệt kê các hiện tượng” đã hoàn tất.", _pi1_colophon
h("Vibhaṅgapakaraṇaṃ niṭṭhitaṃ.", COLOPHON)


# ================================================================ 6. translate and checks
BAD = ("là là", "  ", "….", '"', " ,", " .", ":-", "thì thì", "\x00", " ;", ";;", ",,", "chánh niệm", "..", ", ,",
       "None", "—", "pe…", "“ ", " ”", "{", "}", "…,", "… ,", "đôi khi đôi khi")
PALI_LETTERS = re.compile(r"[āīūṃṅñṭḍṇḷ]")
ANS_LINES = []   # (Pāli, Vietnamese) of the Pañhāpucchaka-type lines, for the identity check


def key_ok(t, key):
    if key.startswith("#"):
        return t == key
    if "\x00" in key:
        a, b = key.split("\x00")
        return t.startswith(a) and t.startswith(b, t.index(" ", len(a) - 1) + 1)
    return t.startswith(key)


def translate(pali_lines):
    hq = list(H)
    out = []
    for pl in pali_lines:
        if not pl.strip():
            out.append("")
            continue
        m = S.ID.search(pl)
        t = S.ID.sub("", pl).rstrip()
        assert hq, ("no hand line left for", t[:80])
        key, vi = hq.pop(0)
        assert key_ok(t, key), ("line", t[:90], key)
        if callable(vi):
            vi = vi(t)
            if vi and (t.startswith(("Rūpakkhandho", "Dasāyatanā", "Dve khandhā", "Rūpakkhandho"))
                       or key == ""):
                ANS_LINES.append((t, vi))
        assert pl.count(DASH) == vi.count(DASH), ("dash count", t[:70], pl.count(DASH), vi.count(DASH), vi[:200])
        for bad in BAD:
            assert bad not in vi, (bad, vi[:200], t[:60])
        assert not PALI_LETTERS.search(re.sub(r"\[[^\]]*\]", "", vi)), ("Pāli letters", vi[:200])
        assert vi.count("“") == vi.count("”"), ("quotes", vi[:200])
        if t.endswith("?") and not t.startswith("#"):
            assert vi.endswith("?"), vi[-60:]
        out.append(vi + (" " + m.group(1) if m else ""))
    assert not hq, [x[0][:50] for x in hq]
    return out


def sentences(s):
    return re.split(r"(?<=[.?]) (?=[A-ZĀĪŪÑṬĐÂĂÊÔƠƯÁÀẢÃẠ])", s)


def identity_check():
    """Every Pāli sentence of a Pañhāpucchaka-type line that also occurs (as a whole sentence) in a line of an earlier
    pi-2 chapter must have the same Vietnamese there (sentence-aligned lines only)."""
    pairs = []
    for fn in sorted(os.listdir(S.PALI_DIR)):
        if not fn.endswith(".md") or fn.startswith(("18-", "preamble")):
            continue
        pl = [l for l in open(os.path.join(S.PALI_DIR, fn), encoding="utf-8").read().split("\n") if l.strip()]
        vl = [l for l in vi_file(fn).split("\n") if l.strip()]
        assert len(pl) == len(vl), fn
        for a, b in zip(pl, vl):
            ps, vs = sentences(S.ID.sub("", a)), sentences(S.ID.sub("", b))
            if len(ps) == len(vs):
                pairs.extend(zip(ps, vs))
    known = {}
    for p, v in pairs:
        known.setdefault(p, set()).add(v)
    hits, diffs = 0, []
    for t, vi in ANS_LINES:
        ps, vs = sentences(t), sentences(vi)
        if len(ps) != len(vs):
            continue
        for p, v in zip(ps, vs):
            if p in known:
                hits += 1
                if v not in known[p]:
                    diffs.append((p, v, sorted(known[p])))
    return hits, diffs


def build():
    pali = open(os.path.join(S.PALI_DIR, FN), encoding="utf-8").read().rstrip("\n").split("\n")
    return translate(pali)


HAND_SLIPS = [
    "^2-1031 'Tīṇindriyā … siyā na bhāvetabbā, sacchikātabbā' (the parallels: 'siyā na bhāvetabbā na sacchikātabbā'; "
    "a 'na' looks missing): kept as written «đôi khi không cần được tu tập, cần được tự mình chứng nghiệm»",
    "^2-1039 'Moho akusalahetu … siyā dukkhamasukhāya vedanāya sampayutto' (a- missing; adukkhamasukhāya expected): "
    "kept as written «gắn liền với cảm giác khó chịu và không dễ chịu»",
    "^2-984 / ^2-994 'Kusalānaṃ vā dhammānaṃ vipākato … alobho, adoso, amoho' = pi-1 ^1-1068 (commas only): pi-1 Vietnamese",
    "^2-1004 'Tīṇi saccāni na arūpadhātupariyāpannāni.' and 'Dukkhasaccaṃ siyā …' on two lines: kept",
    "^2-1020 the realm definitions = pi-1 ^1-1287 … ^1-1294 (spelling / punctuation only), pi-1 variant brackets dropped",
    "^2-1023 'tiṃsa rattiyo' / 'tiṃsarattiyo', 'cātumahārājikānaṃ' / 'cātummahārājikānaṃ': same Vietnamese; closing "
    "'…sahassānīti', '…kappasahassānīti', '…anāsavāti' (ti) dropped",
    "^2-993 'kati āyatanā' (= āyatanāni): no effect",
]


def main():
    lines = build()
    hits, diffs = identity_check()
    print(f"identity check: {hits} sentences shared with ch1-17, {len(diffs)} different")
    for p, v, k in diffs:
        print("  P:", p[:150])
        print("  V18:", v[:200])
        print("  Vold:", k[0][:200])
    assert not diffs
    dry = "--dry" in sys.argv
    path = os.path.join(S.VI_DIR, FN)
    if not dry:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines).rstrip("\n") + "\n")
    print("OK:" if not dry else "DRY:", path, "|", len([x for x in lines if x.strip()]), "non-empty lines")
    for s in sorted(set(SLIPS + HAND_SLIPS)):
        print("slip:", s)


if __name__ == "__main__":
    main()
