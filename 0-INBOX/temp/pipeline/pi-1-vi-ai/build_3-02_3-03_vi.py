"""Build the Vietnamese plain zero-shot of pi-1 parts 3-02 and 3-03 (Rūpakaṇḍa, Rūpavibhatti: the pairs,
the sets of three, four ... eleven; ^1-2-3-2-0 … ^1-984).

usage: python -I -X utf8 build_3-02_3-03_vi.py      (checks, then writes both parts)

Importing this file does NOT build anything.
Method: the approved builders are imported unchanged (build_matika_vi = M, build_ch2_01_sample_vi = C,
build_3-01_vi = R, which itself imports the 2-xx builders). Structure as ../pi-1-ru/build_3-02_3-03_ru.py and
../pi-1-ru/ref/en_build_3-02_3-03.py. Every classification term comes from build_3-01_vi (R.P / R.pred(), whose
matrix predicates come from M.PRED), every item name from R.N / R.RUPASSA, so the 3-01 item strings are reused
byte for byte. The long sense-base definitions are generated from Pāli templates together with their
Vietnamese; a source line is translated only if it equals a generated Pāli string exactly (after the few
normalisations listed in NORMALISE), otherwise the build stops.

Frames:
  Katamaṃ taṃ rūpaṃ X?            = Vật chất nào <pred X>?
  … – idaṃ taṃ rūpaṃ X.           = … – đây là loại vật chất <pred X>.   (as 3-01 «có loại vật chất <pred>»)
  two terms X Y                   = <pred X> và <pred Y>  (", " when one of them already holds «và» / «nhưng»)
"""
import importlib, pathlib, re, sys, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_vi as M  # noqa: E402  (importing does not write)
import build_ch2_01_sample_vi as C  # noqa: E402  (importing does not write)
R = importlib.import_module("build_3-01_vi")  # importing does not write

PARTS = ["3-02-rupakandam.md", "3-03-rupakandam.md"]
PALI_DIR, OUT_DIR = R.B.PALI_DIR, R.B.OUT_DIR
TERMS = HERE / "vi-zeroshot-terms.md"
DASH, PE, ELL = R.DASH, R.PE, R.ELL
RF, KIND = R.RF, R.KIND           # «vật chất», «loại vật chất»
RF_C = RF[0].upper() + RF[1:]


def cap(s):
    return s[0].upper() + s[1:]


# =========================================================================================
# 1. Classification terms (predicates of «vật chất»), all from build_3-01_vi
# =========================================================================================
SA = M.PRED[("1-M1-22", "a")]     # thấy được và có tính va chạm (sanidassana sappaṭigha)
IA = M.PRED[("1-M1-22", "b")]     # không thấy được nhưng có tính va chạm (anidassana sappaṭigha)
assert (SA, IA) == ("thấy được và có tính va chạm", "không thấy được nhưng có tính va chạm")
assert (SA, IA) == (f"{R.P['sanidassanaṃ']} và {R.P['sappaṭighaṃ']}",
                    f"{R.P['anidassanaṃ']} nhưng {R.P['sappaṭighaṃ']}")

EXTRA = {   # terms that 3-01 never uses as a predicate; same pattern «là <name>»
    "pathavīdhātu": f"là {R.N['pathavīdhātu']}",
    "tejodhātu": f"là {R.N['tejodhātu']}",
    "vāyodhātu": f"là {R.N['vāyodhātu']}",
    # the eleventh class of ^1-593: «không thấy được và không có tính va chạm, nằm trong lĩnh vực đối tượng của ý»
    "anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ":
        f"{M.PRED[('1-M1-22', 'c')]}, {' '.join(R.INCL)} {R.DHAMMAYATANA}",
}
assert EXTRA["anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ"] in R.LISTS[
    "Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, saddāyatanaṃ, "
    "gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, yañca rūpaṃ anidassanaappaṭighaṃ "
    "[anidassanaṃ appaṭighaṃ (sī. syā.)] dhammāyatanapariyāpannaṃ."].replace(
    M.V("s", "Sī., Syā.", "anidassanaṃ appaṭighaṃ"), "")

# first terms of the two-term classes (3-03)
PREFIXES = sorted(["ajjhattikaṃ", "bāhiraṃ", "upādā", "no upādā", "upādiṇṇaṃ", "anupādiṇṇaṃ",
                   "upādiṇṇupādāniyaṃ", "anupādiṇṇupādāniyaṃ", "sappaṭighaṃ", "appaṭighaṃ", "indriyaṃ",
                   "na indriyaṃ", "mahābhūtaṃ", "na mahābhūtaṃ"], key=len, reverse=True)


def one(q):
    """one classification term or one '…pe…' chain (3-01 R.pred); 'na ārammaṇaṃ' = 'nārammaṇaṃ'."""
    q = q.replace(" na ārammaṇaṃ", " nārammaṇaṃ")
    if q in EXTRA:
        return EXTRA[q]
    return R.pred(q)


def join2(a, b):
    if any(w in x for x in (a, b) for w in (" và ", " nhưng ")):
        return f"{a}, {b}"
    return f"{a} và {b}"


def term(q):
    """Pāli classification term(s) of a question / answer formula -> Vietnamese predicate."""
    q = q.strip()
    try:
        return one(q)
    except (KeyError, AttributeError, AssertionError):
        pass
    for p in PREFIXES:
        if q.startswith(p + " "):
            return join2(R.P[p], one(q[len(p) + 1:]))
    raise KeyError(f"unknown classification term {q!r}")


# =========================================================================================
# 2. Item names and answer lists
# =========================================================================================
ITEMS = dict(R.N)
for k, v in R.RUPASSA.items():
    ITEMS[f"rūpassa {k}"] = f"{v} của {RF}"
assert ITEMS["rūpassa upacayo"] == "sự tăng trưởng của vật chất"

CLAUSE = "yaṃ vā panaññampi atthi rūpaṃ"
ANY_OTHER = f"hoặc bất cứ {KIND} nào khác"   # as the sample's «hoặc bất cứ hiện tượng phi vật chất nào khác»
KAMMA = "do nghiệp đã được tạo"               # kammassa katattā (katattā = «đã được tạo», 2-04)
QUALS = {
    "kammassa katattā": f"sinh ra {KAMMA}",
    "na kammassa katattā": f"không sinh ra {KAMMA}",
    # cittaja = «sinh từ tâm» (-ja as «sinh từ sự tiếp xúc»), hetu = gốc rễ, cittasamuṭṭhāna = ^1-M2-60 (a)
    "cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ": f"sinh từ tâm, có tâm làm gốc rễ, {M.PRED[('1-M2-60', 'a')]}",
    "na cittajaṃ na cittahetukaṃ na cittasamuṭṭhānaṃ":
        f"không sinh từ tâm, không có tâm làm gốc rễ, {M.PRED[('1-M2-60', 'b')]}",
}
LEADS = {"kammassa katattā", "na kammassa katattā"}
LVOCAB = set(ITEMS) | {CLAUSE} | set(QUALS)
MAXW = max(len(k.split()) for k in LVOCAB)


def list_vi(a, lower=False):
    """Pāli item list -> Vietnamese ('…pe…' -> '…', a stray space before '…pe…' is mirrored)."""
    a = a[0].lower() + a[1:]
    a = re.sub(r"(\s*)…pe…\s*", lambda m: " \x01 " if m.group(1) else " \x00 ", a).replace(",", " , ")
    words = a.split()
    toks, i = [], 0
    while i < len(words):
        w = words[i]
        if w in (",", "\x00", "\x01"):
            toks.append(w)
            i += 1
            continue
        for n in range(min(MAXW, len(words) - i), 0, -1):
            cand = " ".join(words[i:i + n])
            if cand in LVOCAB:
                toks.append(cand)
                i += n
                break
        else:
            raise KeyError(f"unknown list item at {words[i:]!r}")
    toks = [t for t in toks if t != ","]
    if toks[0] in LEADS:   # «Kammassa katattā phoṭṭhabbāyatanaṃ āpodhātu»: the qualifier closes the list
        assert all(t in ITEMS for t in toks[1:]), toks
        out = ", ".join(ITEMS[t] for t in toks[1:]) + ", " + QUALS[toks[0]]
    else:
        out, prev, j = "", None, 0
        while j < len(toks):
            t = toks[j]
            if t in ("\x00", "\x01"):
                out += (" " if t == "\x01" else "") + ELL
                prev = "pe"
                j += 1
                continue
            if t == CLAUSE:
                q = toks[j + 1]
                assert q in QUALS, toks
                out += f", {ANY_OTHER} {QUALS[q]}:"
                prev = "colon"
                j += 2
                continue
            assert t in ITEMS, (t, toks)
            if prev == "item":
                out += ", "
            elif prev in ("pe", "colon"):
                out += " "
            out += ITEMS[t]
            prev = "item"
            j += 1
    return out if lower else cap(out)


# =========================================================================================
# 3. Definitions of the sense bases (Pāli templates + Vietnamese)
# =========================================================================================
UPP_P = "uppajji vā uppajjati vā uppajjissati vā uppajje vā"
HIT_P = "paṭihaññi vā paṭihaññati vā paṭihaññissati vā paṭihaññe vā"
ARISE = "đã sinh khởi, đang sinh khởi, sẽ sinh khởi hoặc có thể sinh khởi"
STRIKE = "đã va chạm, đang va chạm, sẽ va chạm hoặc có thể va chạm"   # paṭihaññati (sappaṭigha = có tính va chạm)
MAHA4 = R.MAHA4                                                     # bốn yếu tố cơ bản
UPADAYA = f"phái sinh từ {MAHA4}"                                   # catunnaṃ mahābhūtānaṃ upādāya (3-01)
PASADA = "chất nhạy cảm"                                            # pasāda
ATTABHAVA = "nằm trong sự tồn tại cá nhân"                          # attabhāvapariyāpanna (pariyāpanna = nằm trong)
assert R.INCL == ["nằm", "trong"]
VON = "vốn"   # sets the qualities off: «mắt, vốn không thấy được …» (never «mắt không thấy được» = 'cannot see')
PAND = C.WL["cittaṃ"][4]                                            # paṇḍaraṃ = sự sáng ngời (sample)
assert PAND == "sự sáng ngời"
NAMES_COMMON = ["thế giới", "cánh cửa", "đại dương", PAND, "cánh đồng", R.BASIS.split(" cho")[0]]
assert NAMES_COMMON[-1] == "chỗ dựa"   # vatthu (3-01)
NAMES_EYE = ["cái dẫn đường", "cái chỉ lối"]                         # nettaṃ, nayanaṃ
NAMES_TAIL = ["bờ bên này", "ngôi làng trống rỗng"]                  # orimaṃ tīraṃ, suñño gāmo
FEEL = C.N["vedanā"]                                                # cảm giác
CHAIN_MID = f"{ELL} {C.N['saññā']}{ELL} {C.N['cetanā']}{ELL} "       # …pe… saññā…pe… cetanā…pe…
OBJ_AS = "lấy {} làm đối tượng"                                     # -ārammaṇa (as rūpārammaṇaṃ, 2-04)
ABOUT = "liên quan đến"                                             # ārabbha
DEP = "dựa vào"                                                     # nissāya

# organs: Pāli forms + Vietnamese
ORG = {
    "cakkhu": dict(Y="Yaṃ cakkhu", acc="cakkhuṃ", relins="yena", ins="cakkhunā anidassanena sappaṭighena",
                   relloc="yamhi", loc="cakkhumhi anidassanamhi sappaṭighamhi", relnom="yaṃ",
                   nomq="cakkhu anidassanaṃ sappaṭighaṃ", nomq2="cakkhuṃ anidassanaṃ sappaṭighaṃ",
                   s="cakkhu", ay="cakkhāyatanaṃ", dh="cakkhudhātu", ind="cakkhundriyaṃ", first="cakkhuṃ petaṃ",
                   obj="rūpa", verbs="passi vā passati vā passissati vā passe vā", v="thấy"),
    "sota": dict(Y="Yaṃ sotaṃ", acc="sotaṃ", relins="yena", ins="sotena anidassanena sappaṭighena",
                 relloc="yamhi", loc="sotamhi anidassanamhi sappaṭighamhi", relnom="yaṃ",
                 nomq="sotaṃ anidassanaṃ sappaṭighaṃ", nomq2="sotaṃ anidassanaṃ sappaṭighaṃ",
                 s="sota", ay="sotāyatanaṃ", dh="sotadhātu", ind="sotindriyaṃ", first="sotaṃ petaṃ",
                 obj="sadda", verbs="suṇi vā suṇāti vā suṇissati vā suṇe vā", v="nghe"),
    "ghāna": dict(Y="Yaṃ ghānaṃ", acc="ghānaṃ", relins="yena", ins="ghānena anidassanena sappaṭighena",
                  relloc="yamhi", loc="ghānamhi anidassanamhi sappaṭighamhi", relnom="yaṃ",
                  nomq="ghānaṃ anidassanaṃ sappaṭighaṃ", nomq2="ghānaṃ anidassanaṃ sappaṭighaṃ",
                  s="ghāna", ay="ghānāyatanaṃ", dh="ghānadhātu", ind="ghānindriyaṃ", first="ghānaṃ petaṃ",
                  obj="gandha", verbs="ghāyi vā ghāyati vā ghāyissati vā ghāye vā", v="ngửi"),
    # the tongue has the instrumental «yāya jivhāya …» where the others have the locative (^1-609, ^1-630)
    "jivhā": dict(Y="Yā jivhā", acc="jivhaṃ", relins="yāya", ins="jivhāya anidassanāya sappaṭighāya",
                  relloc="yāya", loc="jivhāya anidassanāya sappaṭighāya", relnom="yā",
                  nomq="jivhā anidassanā sappaṭighā", nomq2="jivhā anidassanā sappaṭighā",
                  s="jivhā", ay="jivhāyatanaṃ", dh="jivhādhātu", ind="jivhindriyaṃ", first="jivhā pesā",
                  obj="rasa", verbs="sāyi vā sāyati vā sāyissati vā sāye vā", v="nếm"),
    "kāya": dict(Y="Yo kāyo", acc="kāyaṃ", relins="yena", ins="kāyena anidassanena sappaṭighena",
                 relloc="yamhi", loc="kāyamhi anidassanamhi sappaṭighamhi", relnom="yo",
                 nomq="kāyo anidassano sappaṭigho", nomq2="kāyo anidassano sappaṭigho",
                 s="kāya", ay="kāyāyatanaṃ", dh="kāyadhātu", ind="kāyindriyaṃ", first="kāyo peso",
                 obj="phoṭṭhabba", verbs="phusi vā phusati vā phusissati vā phuse vā", v="chạm"),
}
OBJ = {
    "rūpa": dict(acc="rūpaṃ sanidassanaṃ sappaṭighaṃ", nom="rūpaṃ sanidassanaṃ sappaṭighaṃ",
                 loc="rūpamhi sanidassanamhi sappaṭighamhi", abr="rūpaṃ", ar="rūpārammaṇ", relnom="yaṃ",
                 names="rūpaṃ petaṃ rūpāyatanaṃ petaṃ rūpadhātu pesā", org="cakkhu", q=SA),
    "sadda": dict(acc="saddaṃ anidassanaṃ sappaṭighaṃ", nom="saddo anidassano sappaṭigho",
                  loc="saddamhi anidassanamhi sappaṭighamhi", abr="saddaṃ", ar="saddārammaṇ", relnom="yo",
                  names="saddo peso saddāyatanaṃ petaṃ saddadhātu pesā", org="sota", q=IA),
    "gandha": dict(acc="gandhaṃ anidassanaṃ sappaṭighaṃ", nom="gandho anidassano sappaṭigho",
                   loc="gandhamhi anidassanamhi sappaṭighamhi", abr="gandhaṃ", ar="gandhārammaṇ", relnom="yo",
                   names="gandho peso gandhāyatanaṃ petaṃ gandhadhātu pesā", org="ghāna", q=IA),
    "rasa": dict(acc="rasaṃ anidassanaṃ sappaṭighaṃ", nom="raso anidassano sappaṭigho",
                 loc="rasamhi anidassanamhi sappaṭighamhi", abr="rasaṃ", ar="rasārammaṇ", relnom="yo",
                 names="raso peso rasāyatanaṃ petaṃ rasadhātu pesā", org="jivhā", q=IA),
    "phoṭṭhabba": dict(acc="phoṭṭhabbaṃ anidassanaṃ sappaṭighaṃ", nom="phoṭṭhabbo anidassano sappaṭigho",
                       loc="phoṭṭhabbamhi anidassanamhi sappaṭighamhi", abr="phoṭṭhabbaṃ",
                       ar="phoṭṭhabbārammaṇ", relnom="yo",
                       names="phoṭṭhabbo peso phoṭṭhabbāyatanaṃ petaṃ phoṭṭhabbadhātu pesā", org="kāya", q=IA),
}
ORG_OBJ_ACC = {"kāya": "phoṭṭhabbaṃ anidassanasappaṭighaṃ"}   # ^1-612: compound in the organ definition
for k, o in ORG.items():
    o["n"] = R.SENSE[k]                          # mắt, tai, mũi, lưỡi, thân
    o["contact"] = R.GEN[f"{k}samphassassa"]     # sự tiếp xúc của mắt
    o["feel"] = R.GEN[f"{k}samphassajāya vedanāya"]   # cảm giác sinh từ sự tiếp xúc của mắt
    o["cons"] = R.VINNANA[k]                     # thức qua mắt
    assert o["feel"] == f"{FEEL} sinh từ {o['contact']}"
for k, ob in OBJ.items():
    ob["n"] = R.OBJS[k]                          # hình sắc, âm thanh, mùi, vị, vật xúc chạm


def chain_p(o, lead):
    """the four '…pe…'-linked clauses of variant d (organ: lead=None; object: lead=object)."""
    s, acc = o["s"], o["acc"]
    sam = f"{s}samphasso"
    feel = f"{s}samphassajā vedanā{PE} saññā{PE} cetanā{PE} {s}viññāṇaṃ"
    if lead is None:
        ob = OBJ[o["obj"]]
        c = [f"yaṃ {acc} nissāya {ob['abr']} ārabbha {sam} {UPP_P}",
             f"yaṃ {acc} nissāya {ob['abr']} ārabbha {feel} {UPP_P}",
             f"yaṃ {acc} nissāya {ob['ar']}o {sam} {UPP_P}",
             f"yaṃ {acc} nissāya {ob['ar']}ā {feel} {UPP_P}"]
    else:
        ob = lead
        c = [f"yaṃ {ob['abr']} ārabbha {acc} nissāya {sam} {UPP_P}",
             f"yaṃ {ob['abr']} ārabbha {acc} nissāya {feel} {UPP_P}",
             f"yaṃ {ob['ar']}o {acc} nissāya {sam} {UPP_P}",
             f"yaṃ {ob['ar']}ā {acc} nissāya {feel} {UPP_P}"]
    return f"{PE} ".join(c)


def verbs_vi(v):
    return f"đã {v}, đang {v}, sẽ {v} hoặc có thể {v}"


def organ_names_p(o, eye):
    s = (f"{o['first']} {o['ay']} petaṃ {o['dh']} pesā {o['ind']} petaṃ loko peso dvārā pesā samuddo peso "
         f"paṇḍaraṃ petaṃ khettaṃ petaṃ vatthuṃ petaṃ ")
    if eye:
        s += "nettaṃ petaṃ nayanaṃ petaṃ "
    return s + "orimaṃ tīraṃ petaṃ suñño gāmo peso"


def organ_names_vi(k):
    o = ORG[k]
    n = [o["n"], R.N[o["ay"]], R.N[o["dh"]], R.N[o["ind"]]] + NAMES_COMMON
    if k == "cakkhu":
        n += NAMES_EYE
    n += NAMES_TAIL
    return ", ".join(f"đây là {x}" for x in n)


def organ_defs(k):
    """{Pāli definition: Vietnamese} for one organ: variants a, b, c, d (with and without the ^1-596
    variant bracket) and the abbreviated form."""
    o = ORG[k]
    ob = OBJ[o["obj"]]
    n, N_ = o["n"], cap(o["n"])
    oacc = ORG_OBJ_ACC.get(k, ob["acc"])
    head_rest = "catunnaṃ mahābhūtānaṃ upādāya pasādo attabhāvapariyāpanno anidassano sappaṭigho"
    mids_p = {
        "a": f"{o['relins']} {o['ins']} {oacc} {o['verbs']}",
        "b": f"{o['relloc']} {o['loc']} {ob['nom']} {HIT_P}",
        "c": f"{o['relnom']} {o['nomq']} {ob['loc']} {HIT_P}",
        "d": chain_p(o, None),
    }
    obj_q = f"{ob['n']}, {VON} {ob['q']}"
    org_q = f"{n}, {VON} {IA}"
    mids_v = {
        "a": f"{org_q}, mà nhờ nó người ta {verbs_vi(o['v'])} {obj_q}",
        "b": f"{org_q}, mà {obj_q}, {STRIKE} vào nó",
        "c": f"{org_q}, mà {STRIKE} vào {obj_q}",
        "d": (f"{n} mà {DEP} nó, {ABOUT} {ob['n']}, {o['contact']} {ARISE}{ELL} "
              f"{n} mà {DEP} nó, {ABOUT} {ob['n']}, {o['feel']}{CHAIN_MID}{o['cons']} {ARISE}{ELL} "
              f"{n} mà {DEP} nó, {o['contact']} {OBJ_AS.format(ob['n'])} {ARISE}{ELL} "
              f"{n} mà {DEP} nó, {o['feel']} {OBJ_AS.format(ob['n'])}{CHAIN_MID}{o['cons']} {ARISE}"),
    }
    out = {}
    names_p, names_v = organ_names_p(o, k == "cakkhu"), organ_names_vi(k)
    for var_p, var_v in (("", ""), (" [cakkhuṃ (sī. syā.)]", M.V("s", "Sī., Syā.", "cakkhuṃ"))):
        if var_p and k != "cakkhu":
            continue
        head_p = f"{o['Y']}{var_p} {head_rest}"
        head_v = f"{N_}{var_v} là {PASADA} {UPADAYA}, {ATTABHAVA}, {IA}"
        for x in "abcd":
            out[f"{head_p}, {mids_p[x]}, {names_p}"] = f"{head_v}; {mids_v[x]}; {names_v}"
    out[f"{o['Y']} catunnaṃ mahābhūtānaṃ upādāya pasādo{PE} suñño gāmo peso"] = (
        f"{N_} là {PASADA} {UPADAYA}{ELL} đây là {NAMES_TAIL[-1]}")
    return out


# object lists
VN = "màu sắc và dáng vẻ"   # vaṇṇanibhā
COLOURS_P = ("nīlaṃ pītakaṃ lohitakaṃ odātaṃ kāḷakaṃ mañjiṭṭhakaṃ{v1} hari harivaṇṇaṃ ambaṅkuravaṇṇaṃ dīghaṃ rassaṃ "
             "aṇuṃ thūlaṃ vaṭṭaṃ parimaṇḍalaṃ caturaṃsaṃ{v2} chaḷaṃsaṃ aṭṭhaṃsaṃ soḷasaṃsaṃ ninnaṃ thalaṃ chāyā "
             "ātapo āloko andhakāro abbhā mahikā dhūmo rajo candamaṇḍalassa vaṇṇanibhā sūriyamaṇḍalassa{v3} "
             "vaṇṇanibhā tārakarūpānaṃ vaṇṇanibhā ādāsamaṇḍalassa vaṇṇanibhā maṇisaṅkhamuttāveḷuriyassa "
             "vaṇṇanibhā jātarūparajatassa vaṇṇanibhā")
# colour words as the kasiṇa words of 2-02 (màu xanh / màu vàng / màu đỏ / màu trắng)
COLOURS_V = ("màu xanh, màu vàng, màu đỏ, màu trắng, màu đen, màu đỏ thẫm{v1}, màu xanh lục, màu ánh lục, "
             "màu chồi xoài, dài, ngắn, nhỏ, to, tròn, tròn trịa, bốn góc{v2}, sáu góc, tám góc, mười sáu góc, "
             "chỗ trũng, chỗ gò, bóng râm, nắng, ánh sáng, bóng tối, mây, sương mù, khói, bụi, "
             f"{VN} của vầng trăng, {VN} của vầng mặt trời{{v3}}, {VN} của các vì sao, {VN} của mặt gương, "
             f"{VN} của ngọc quý, vỏ ốc, ngọc trai và ngọc lưu ly, {VN} của vàng và bạc")
for kw in ("đỏ", "vàng", "trắng"):
    assert any(v.endswith("là màu " + kw) for v in R.B.PH.values()), kw
COL_VARS_P = dict(v1=" [mañjeṭṭhakaṃ (sī. syā.)]", v2=" [caturassaṃ (sī. ka.)]", v3=" [suriyamaṇḍalassa (sī. syā.)]")
COL_VARS_V = dict(v1=M.V("s", "Sī., Syā.", "mañjeṭṭhakaṃ"), v2=M.V("s", "Sī., Ka.", "caturassaṃ"),
                  v3=M.V("s", "Sī., Syā.", "suriyamaṇḍalassa"))
NO_VARS = dict(v1="", v2="", v3="")
SOUNDS_P = ("bherisaddo mudiṅgasaddo saṅkhasaddo paṇavasaddo gītasaddo vāditasaddo sammasaddo pāṇisaddo "
            "sattānaṃ nigghosasaddo dhātūnaṃ sannighātasaddo vātasaddo udakasaddo manussasaddo amanussasaddo")
SOUNDS_V = ("tiếng trống lớn, tiếng trống cơm, tiếng tù và, tiếng trống con, tiếng hát, tiếng nhạc cụ, "
            "tiếng chũm chọe, tiếng vỗ tay, tiếng ồn ào của chúng sinh, tiếng va đập của các vật, tiếng gió, "
            "tiếng nước, tiếng người, tiếng của những loài không phải người")
SMELLS_P = ("mūlagandho sāragandho tacagandho pattagandho pupphagandho phalagandho āmakagandho vissagandho "
            "sugandho duggandho")
SMELLS_V = ("mùi rễ cây, mùi lõi cây, mùi vỏ cây, mùi lá, mùi hoa, mùi trái cây, mùi tanh, mùi ôi thiu, "
            "mùi thơm, mùi hôi")
TASTES_P = ("mūlaraso khandharaso tacaraso pattaraso puppharaso phalaraso ambilaṃ madhuraṃ tittakaṃ kaṭukaṃ "
            "loṇikaṃ khārikaṃ lambilaṃ{v} kasāvo sādu asādu")
TASTES_V = ("vị rễ cây, vị thân cây, vị vỏ cây, vị lá, vị hoa, vị trái cây, vị chua, vị ngọt, vị đắng, vị cay, "
            "vị mặn, vị kiềm, vị chua nhẹ{v}, vị chát, vị ngon, vị dở")
TASTE_VAR_P, TASTE_VAR_V = " [lapilakaṃ (sī.)]", M.V("p", "Sī.", "lapilakaṃ")
TOUCH_P = ("Pathavīdhātu tejodhātu vāyodhātu kakkhaḷaṃ mudukaṃ saṇhaṃ pharusaṃ sukhasamphassaṃ dukkhasamphassaṃ "
           "garukaṃ lahukaṃ")
# sukhasamphassa / dukkhasamphassa = «tiếp xúc dễ chịu / khó chịu» (3-01 ^1-590)
TOUCH_V = (f"{cap(R.N['pathavīdhātu'])}, {R.N['tejodhātu']}, {R.N['vāyodhātu']}, cái cứng, cái mềm, cái mịn, "
           "cái thô ráp, cái có tiếp xúc dễ chịu, cái có tiếp xúc khó chịu, cái nặng, cái nhẹ")
assert "có loại tiếp xúc dễ chịu, có loại tiếp xúc khó chịu" in R.LISTS[[k for k in R.LISTS if "sukhasamphassaṃ" in k][0]]


def object_heads(k, with_vars):
    """(Pāli head, Vietnamese head) of an object definition."""
    ob = OBJ[k]
    if k == "rūpa":
        d_p = "catunnaṃ mahābhūtānaṃ upādāya vaṇṇanibhā sanidassanaṃ sappaṭighaṃ"
        col_p = COLOURS_P.format(**(COL_VARS_P if with_vars else NO_VARS))
        col_v = COLOURS_V.format(**(COL_VARS_V if with_vars else NO_VARS))
        d_v = f"{VN} {UPADAYA}, {SA}"
        return (f"Yaṃ rūpaṃ {d_p} {col_p}, yaṃ vā panaññampi atthi rūpaṃ {d_p}",
                f"{cap(ob['n'])} là {d_v}: {col_v}, hoặc bất cứ {ob['n']} nào khác là {d_v}")
    if k == "phoṭṭhabba":
        return TOUCH_P, TOUCH_V
    lst_p, lst_v = {"sadda": (SOUNDS_P, SOUNDS_V), "gandha": (SMELLS_P, SMELLS_V),
                    "rasa": (TASTES_P, TASTES_V)}[k]
    if k == "rasa":
        lst_p = lst_p.format(v=TASTE_VAR_P if with_vars else "")
        lst_v = lst_v.format(v=TASTE_VAR_V if with_vars else "")
    nom = ob["nom"].split()[0]                    # saddo / gandho / raso
    d_p = "catunnaṃ mahābhūtānaṃ upādāya anidassano sappaṭigho"
    d_v = f"{UPADAYA}, {IA}"
    return (f"Yo {nom} {d_p} {lst_p}, yo vā panaññopi atthi {nom} {d_p}",
            f"{cap(ob['n'])} {d_v}: {lst_v}, hoặc bất cứ {ob['n']} nào khác {d_v}")


def object_defs(k):
    ob = OBJ[k]
    o = ORG[ob["org"]]
    n = ob["n"]
    mids_p = {
        "a": f"yaṃ {ob['acc']} {o['ins']} {o['verbs']}",
        "b": f"yamhi {ob['loc']} {o['nomq2']} {HIT_P}",
        "c": f"{ob['relnom']} {ob['nom']} {o['loc']} {HIT_P}",
        "d": chain_p(o, ob),
    }
    obj_q = f"{n}, {VON} {ob['q']}"
    org_q = f"{o['n']}, {VON} {IA}"
    mids_v = {
        "a": f"{obj_q}, mà người ta {verbs_vi(o['v'])} bằng {org_q}",
        "b": f"{obj_q}, mà {org_q}, {STRIKE} vào nó",
        "c": f"{obj_q}, mà {STRIKE} vào {org_q}",
        "d": (f"{n} mà {ABOUT} nó, {DEP} {o['n']}, {o['contact']} {ARISE}{ELL} "
              f"{n} mà {ABOUT} nó, {DEP} {o['n']}, {o['feel']}{CHAIN_MID}{o['cons']} {ARISE}{ELL} "
              f"{n} mà, {DEP} {o['n']}, {o['contact']} {OBJ_AS.format('nó')} {ARISE}{ELL} "
              f"{n} mà, {DEP} {o['n']}, {o['feel']} {OBJ_AS.format('nó')}{CHAIN_MID}{o['cons']} {ARISE}"),
    }
    names_v = ", ".join(f"đây là {x}" for x in (n, R.N[f"{k[:-1]}āyatanaṃ"], R.N[f"{k}dhātu"]))
    out = {}
    for wv in (False, True):
        hp, hv = object_heads(k, wv)
        for x in "abcd":
            out[f"{hp}, {mids_p[x]}, {ob['names']}"] = f"{hv}; {mids_v[x]}; {names_v}"
    if k == "rūpa":
        out[f"Yaṃ rūpaṃ catunnaṃ mahābhūtānaṃ upādāya vaṇṇanibhā{PE} rūpadhātu pesā"] = (
            f"{cap(n)} là {VN} {UPADAYA}{ELL} đây là {R.N['rūpadhātu']}")
    if k == "phoṭṭhabba":
        out[f"Pathavīdhātu{PE} phoṭṭhabbadhātu pesā"] = (
            f"{cap(R.N['pathavīdhātu'])}{ELL} đây là {R.N['phoṭṭhabbadhātu']}")
    return out


DEFS = {}
for _k in ORG:
    DEFS.update(organ_defs(_k))
for _k in OBJ:
    DEFS.update(object_defs(_k))

# ---- short definitions ----------------------------------------------------------------------
RUPINO = M.BARE[("1-M2-11", "a")]   # các hiện tượng thuộc vật chất (rūpino dhammā)
assert RUPINO == "các hiện tượng thuộc vật chất" and C.G_JIVITA == "ở các hiện tượng phi vật chất ấy"
AT_RUPA = f"Điều có ở {RF}, tức là "          # Yā rūpassa S (frame of the sample's «Điều có ở …, tức là S»)
MINDS = "người có tâm thiện, hoặc tâm bất thiện, hoặc tâm không xác định về mặt đạo đức"
assert M.PRED[("1-M1-1", "c")] == "là không xác định về mặt đạo đức"
INTIM = f"{R.VINNATTI}, sự làm cho biết, trạng thái đã được làm cho biết"   # viññatti viññāpanā viññāpitattaṃ
SPEECH = ("lời nói, lời lẽ, cách nói, sự thốt ra, tiếng nói, sự phát ra tiếng nói, lời nói, sự phát thành lời")
VACA = "đây được gọi là lời nói"              # ayaṃ vuccati vācā (idaṃ vuccati = đây được gọi là, 3-01)
OWN = (f", dù {M.SELF} hay {M.OUTS}, dù {M.PRED[('1-M2-68', 'a')]} hay {M.PRED[('1-M2-68', 'b')]}")
assert OWN == ", dù thuộc về bản thân hay ở bên ngoài bản thân, dù do nghiệp tạo ra hay không do nghiệp tạo ra"
WATER = f"Nước, điều được xem là nước, chất ẩm, điều được xem là chất ẩm, tính kết dính của {RF}"
ITTHI = "Điều có ở người nữ, tức là hình tướng nữ, dấu hiệu nữ, cử chỉ nữ, dáng điệu nữ, trạng thái nữ, bản chất nữ"
PURISA = ("Điều có ở người nam, tức là hình tướng nam, dấu hiệu nam, cử chỉ nam, dáng điệu nam, trạng thái nam, "
          "bản chất nam")
KABALI = ("Cơm, cháo, bột rang, cá, thịt, sữa, sữa đông, bơ lỏng, bơ tươi, dầu, mật ong, mật mía, "
          f"{ANY_OTHER} mà ở xứ sở nào thì chúng sinh ở xứ sở ấy cũng đưa vào miệng, nhai bằng răng, nuốt qua cổ "
          "họng, làm căng đầy bụng, tức là tinh chất nuôi dưỡng nhờ đó chúng sinh duy trì mạng sống")
SHORT = {
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo": ITTHI,
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo "
    "[itthittaṃ itthībhāvo (syā.)]": ITTHI + M.V("s", "Syā.", "itthittaṃ itthībhāvo"),
    "Yaṃ purisassa purisaliṅgaṃ purisanimittaṃ purisakuttaṃ purisākappo purisattaṃ purisabhāvo": PURISA,
    "Yo tesaṃ rūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ":
        f"Điều có ở {RUPINO} ấy, tức là {C.S_JIVITA}",
    "Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā abhikkamantassa vā paṭikkamantassa vā "
    "ālokentassa vā vilokentassa vā samiñjentassa vā pasārentassa vā kāyassa thambhanā santhambhanā "
    "santhambhitattaṃ viññatti viññāpanā viññāpitattaṃ":
        (f"Điều có ở thân của {MINDS}, khi người ấy đi tới, hoặc đi lui, hoặc nhìn thẳng, hoặc nhìn sang bên, "
         f"hoặc co lại, hoặc duỗi ra, tức là sự căng cứng, sự căng cứng toàn diện, trạng thái căng cứng toàn diện, "
         f"{INTIM}"),
    "Yo ākāso ākāsagataṃ aghaṃ aghagataṃ vivaro vivaragataṃ asamphuṭṭhaṃ catūhi mahābhūtehi":
        (f"Không gian, điều được xem là không gian, khoảng không, điều được xem là khoảng không, kẽ hở, "
         f"điều được xem là kẽ hở, điều không bị {MAHA4} chạm đến"),
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa": WATER,
    "Yā rūpassa lahutā lahupariṇāmatā adandhanatā avitthanatā": AT_RUPA + C.S_LAHUTA,
    "Yā rūpassa mudutā maddavatā akakkhaḷatā akathinatā": AT_RUPA + C.S_MUDUTA,
    "Yā rūpassa kammaññatā kammaññattaṃ kammaññabhāvo": AT_RUPA + C.S_KAMMANNATA,
    # ācaya = sự tích lũy (matrix triad 10); āyatana = lĩnh vực nhận biết (core terms)
    "Yo āyatanānaṃ ācayo, so rūpassa upacayo":
        f"Sự tích lũy của các lĩnh vực nhận biết, đó là {ITEMS['rūpassa upacayo']}",
    "Yo rūpassa upacayo, sā rūpassa santati":
        f"{cap(ITEMS['rūpassa upacayo'])}, đó là {ITEMS['rūpassa santati']}",
    "Yā rūpassa jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni indriyānaṃ paripāko":
        AT_RUPA + ("sự già nua, sự hao mòn, răng gãy rụng, tóc bạc, da nhăn nheo, sự suy giảm tuổi thọ, "
                   "sự chín muồi của các năng lực"),
    "Yo rūpassa khayo vayo bhedo paribhedo aniccatā antaradhānaṃ":
        AT_RUPA + f"sự hủy diệt, sự suy tàn, sự tan rã, sự tan rã hoàn toàn, {R.RUPASSA['aniccatā']}, sự biến mất",
    "Yaṃ kakkhaḷaṃ kharagataṃ [kharigataṃ (ka.)] kakkhaḷattaṃ kakkhaḷabhāvo ajjhattaṃ vā bahiddhā vā "
    "upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        ("Cái cứng, điều được xem là rắn" + M.V("s", "Ka.", "kharigataṃ") + ", sự cứng, tính chất cứng" + OWN),
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā "
    "anupādiṇṇaṃ vā": WATER + OWN,
    "Yaṃ tejo tejogataṃ usmā usmāgataṃ usumaṃ usumagataṃ ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        ("Lửa, điều được xem là lửa, hơi ấm, điều được xem là hơi ấm, hơi nóng, điều được xem là hơi nóng" + OWN),
    "Yaṃ vāyo vāyogataṃ thambhitattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā":
        f"Gió, điều được xem là gió, trạng thái căng cứng của {RF}" + OWN,
}
_VACI_P = ("Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā vācā girā byappatho udīraṇaṃ ghoso "
           "ghosakammaṃ vācā vacībhedo{sep} ayaṃ vuccati vācā. Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ")
_VACI_V = (f"Điều có ở {MINDS}, tức là {SPEECH}{{sep}} {VACA}. Điều có qua lời nói ấy, tức là {INTIM}")
SHORT[_VACI_P.format(sep=" –")] = _VACI_V.format(sep=" " + DASH)
SHORT[_VACI_P.format(sep=",")] = _VACI_V.format(sep=",")
_KAB_P = ("Odano kummāso sattu maccho maṃsaṃ khīraṃ dadhi sappi navanītaṃ telaṃ madhu phāṇitaṃ, yaṃ vā "
          "panaññampi atthi rūpaṃ yamhi yamhi janapade tesaṃ tesaṃ sattānaṃ mukhāsiyaṃ dantavikhādanaṃ "
          "galajjhoharaṇīyaṃ kucchivitthambhanaṃ, yāya ojāya sattā yāpenti")
SHORT[_KAB_P] = KABALI

# source points normalised before the look-up (each one listed in notes-3-02_3-03.md)
NORMALISE = [
    ("gāmopeso", "gāmo peso"),                                 # ^1-596, ^1-606: run together
    ("phuse vā phoṭṭhabbo peso", "phuse vā, phoṭṭhabbo peso"),  # ^1-647: no comma before the names
    (" udīraṇaṃ dhoso ", " udīraṇaṃ ghoso "),                  # ^1-850: «dhoso» (slip for ghoso)
    ("kucchivitthambhanaṃ yāya", "kucchivitthambhanaṃ, yāya"),  # ^1-880: no comma before yāya
]


def def_vi(a):
    for x, y in NORMALISE:
        a = a.replace(x, y)
    if a in SHORT:
        return SHORT[a]
    return DEFS.get(a)


# =========================================================================================
# 4. Headings and fixed lines
# =========================================================================================
HEAD = {
    "##### Dukaniddeso": "##### Giải thích phân loại theo nhóm hai",
    "###### Upādābhājanīyaṃ": f"###### Phân tích {RF} {M.BARE[('1-M2-67', 'a')].removeprefix(M.DH + ' ')}",
    "##### Tikaniddeso": "##### Giải thích phân loại theo nhóm ba",
}
assert HEAD["###### Upādābhājanīyaṃ"] == "###### Phân tích vật chất phái sinh"
for _h in ("Catukkaṃ", "Pañcakaṃ", "Chakkaṃ", "Sattakaṃ", "Aṭṭhakaṃ", "Navakaṃ", "Dasakaṃ", "Ekādasakaṃ"):
    HEAD[f"##### {_h}"] = R.HEAD[f"##### {_h}"]


def check_headings():
    terms = {}
    for line in TERMS.read_text(encoding="utf-8").splitlines():
        m = re.fullmatch(r"(#+ .+?) = (#+ .+)", line)
        if m:
            terms.setdefault(m.group(1), m.group(2))
    for p, v in HEAD.items():
        assert terms[p] == v, (p, terms.get(p), v)
    return len(HEAD)


_KANDA = R.HEAD["### Rūpakaṇḍaṃ"].split(" ", 1)[1]   # Phần về vật chất
LINES = dict(R.CLOSE)   # «Evaṃ <N>vidhena rūpasaṅgaho.», «Catukkaṃ.» … «Ekādasakaṃ.»
LINES.update({
    "Idaṃ taṃ rūpaṃ upādā.": f"Đây là {KIND} {R.P['upādā']}.",
    "Idaṃ taṃ rūpaṃ no upādā.": f"Đây là {KIND} {R.P['no upādā']}.",
    "Upādābhājanīyaṃ.": HEAD["###### Upādābhājanīyaṃ"].split(" ", 1)[1] + ".",
    "Dukaniddeso.": HEAD["##### Dukaniddeso"].split(" ", 1)[1] + ".",
    "Tikaniddeso.": HEAD["##### Tikaniddeso"].split(" ", 1)[1] + ".",
    # «Nikkhepakaṇḍe dutiyabhāṇavāro. = Phần tụng đọc thứ hai của phần tóm lược.» (terms file pattern)
    "Rūpakaṇḍe paṭhamabhāṇavāro.": (C.END_BHANA1[:-1] + " của " + _KANDA[0].lower() + _KANDA[1:] + "."),
    "Aṭṭhamabhāṇavāro.": C.END_BHANA1.replace("thứ nhất", "thứ tám"),
    "Rūpavibhatti.": R.HEAD["#### Rūpavibhatti"].split(" ", 1)[1] + ".",
    # «<X>kaṇḍaṃ niṭṭhitaṃ. = <phần> đã hoàn tất.» (terms file)
    "Rūpakaṇḍaṃ niṭṭhitaṃ.": R.HEAD["### Rūpakaṇḍaṃ"].split(" ", 1)[1] + " đã hoàn tất.",
    # diṭṭhaṃ sutaṃ mutaṃ viññātaṃ as 3-01 ^1-586 («được thấy, được nghe, được cảm nhận, được nhận biết»)
    "Rūpāyatanaṃ diṭṭhaṃ, saddāyatanaṃ sutaṃ, gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ mutaṃ, "
    "sabbaṃ rūpaṃ manasā viññātaṃ rūpaṃ.":
        (f"{cap(R.N['rūpāyatanaṃ'])} là điều được thấy, {R.N['saddāyatanaṃ']} là điều được nghe, "
         f"{R.N['gandhāyatanaṃ']}, {R.N['rasāyatanaṃ']} và {R.N['phoṭṭhabbāyatanaṃ']} là điều được cảm nhận, "
         f"{R.ALL_RF} là {RF} được ý nhận biết."),
})
assert LINES["Rūpakaṇḍe paṭhamabhāṇavāro."] == "Phần tụng đọc thứ nhất của phần về vật chất."
assert "được thấy, được nghe, được cảm nhận, được nhận biết" in R.LISTS["Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ."]


def kn(subj, by):
    """'<subj> X-viññeyyaṃ rūpaṃ' = «<subj> là vật chất mà <by> có thể nhận biết» (3-01 WHICH)"""
    return f"{subj} là {RF} {R.WHICH.format(by)}"


FIVE_OBJ = [("rūpāyatanaṃ", "mắt"), ("saddāyatanaṃ", "tai"), ("gandhāyatanaṃ", "mũi"), ("rasāyatanaṃ", "lưỡi")]
assert [s for _, s in FIVE_OBJ] == list(R.SENSE.values())[:4]
_FOUR = ", ".join(kn(R.N[k], s) for k, s in FIVE_OBJ)
_BODY = kn(R.N["phoṭṭhabbāyatanaṃ"], R.SENSE["kāya"])
_FIVE_AY = (", ".join(R.N[k] for k, _ in FIVE_OBJ) + " và " + R.N["phoṭṭhabbāyatanaṃ"])
_MANODHATU = kn(_FIVE_AY, R.B.NAME["manodhātu"])
_LAST = kn(R.ALL_RF, R.B.NAME["manoviññāṇadhātu"]) + "."
# manāpa = dễ ưa; sukhasamphassa / dukkhasamphassa as 3-01
_AGREE = (kn(f"{R.N['phoṭṭhabbāyatanaṃ'].split(' ', 2)[2]} dễ ưa với tiếp xúc dễ chịu", R.SENSE["kāya"]) + ", "
          + kn(f"{R.N['phoṭṭhabbāyatanaṃ'].split(' ', 2)[2]} không dễ ưa với tiếp xúc khó chịu", R.SENSE["kāya"]))
assert _AGREE.startswith("vật xúc chạm dễ ưa")
_VK = ("Rūpāyatanaṃ cakkhuviññeyyaṃ rūpaṃ, saddāyatanaṃ sotaviññeyyaṃ rūpaṃ, gandhāyatanaṃ ghānaviññeyyaṃ rūpaṃ, "
       "rasāyatanaṃ jivhāviññeyyaṃ rūpaṃ, ")
LINES[_VK + "phoṭṭhabbāyatanaṃ kāyaviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ manoviññeyyaṃ rūpaṃ."] = (
    cap(_FOUR) + f", {_BODY}, " + kn(R.ALL_RF, "ý") + ".")
LINES[_VK + "phoṭṭhabbāyatanaṃ kāyaviññeyyaṃ rūpaṃ, rūpāyatanaṃ saddāyatanaṃ gandhāyatanaṃ rasāyatanaṃ "
      "phoṭṭhabbāyatanaṃ manodhātuviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ manoviññāṇadhātuviññeyyaṃ rūpaṃ."] = (
    cap(_FOUR) + f", {_BODY}, {_MANODHATU}, {_LAST}")
LINES[_VK + "manāpiyo phoṭṭhabbo sukhasamphasso kāyaviññeyyaṃ rūpaṃ, amanāpiyo phoṭṭhabbo dukkhasamphasso "
      "kāyaviññeyyaṃ rūpaṃ, rūpāyatanaṃ saddāyatanaṃ gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ "
      "manodhātuviññeyyaṃ rūpaṃ, sabbaṃ rūpaṃ manoviññāṇadhātuviññeyyaṃ rūpaṃ."] = (
    cap(_FOUR) + f", {_AGREE}, {_MANODHATU}, {_LAST}")

# =========================================================================================
# 5. Question / answer lines
# =========================================================================================
QA_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (.+?)([?.]) (.+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")
BARE_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (.+?)\? ([^–]+)\.$")   # ^1-595, ^1-646: list only, no closing formula
NOQ_RE = re.compile(r"^Katamaṃ taṃ rūpaṃ (\S+ \S+) (itthindriyaṃ…pe… kabaḷīkāro āhāro|"
                    r"cakkhāyatanaṃ…pe… kāyāyatanaṃ, .+) – idaṃ taṃ rūpaṃ (.+?)([.?])$")


def q_vi(q, end):
    return f"{RF_C} nào {term(q)}{end}"


def a_vi(q2, end):
    return f"đây là {KIND} {term(q2)}{end}"


def answer_vi(a, lower=False):
    v = def_vi(a)
    if v is None:
        v = list_vi(a, lower)
    return v


def qa_vi(line):
    m = QA_RE.match(line)
    if m:
        q, qe, a, q2, ae = m.groups()
        return f"{q_vi(q, qe)} {answer_vi(a)} {DASH} {a_vi(q2, ae)}"
    m = BARE_RE.match(line)
    if m:
        return f"{q_vi(m.group(1), '?')} {list_vi(m.group(2))}."
    m = NOQ_RE.match(line)   # ^1-895, ^1-939: no «?» after the question; the list runs on in lower case
    if m:
        q, a, q2, ae = m.groups()
        return f"{q_vi(q, '')} {answer_vi(a, lower=True)} {DASH} {a_vi(q2, ae)}"
    raise KeyError(f"no rule for {line!r}")


def translate_line(body):
    if body.startswith("#"):
        return HEAD[body]
    if body.startswith("Katamaṃ taṃ rūpaṃ"):
        return qa_vi(body)
    return LINES[body]


ID = re.compile(r"^(.*?)(\s*\^[0-9A-Za-z-]+)?$")


def build(part):
    out = []
    for line in (PALI_DIR / part).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            out.append("")
            continue
        m = ID.match(line)
        body, bid = m.group(1), m.group(2) or ""
        v = translate_line(body)
        assert v.count(DASH) == body.count(DASH), (body, v)
        assert v.count("?") == body.count("?"), (body, v)
        assert v.count(ELL) == body.count(PE), (body, v)
        assert ("[" in v) == ("[" in body), (body, v)
        out.append(v + bid)
    text = "\n".join(out).rstrip("\n") + "\n"
    assert "—" not in text and ":-" not in text and "pe…" not in text and "\n\n\n" not in text
    assert unicodedata.normalize("NFC", text) == text
    return text


if __name__ == "__main__":
    print("headings checked:", check_headings())
    for part in PARTS:
        t = build(part)
        (OUT_DIR / part).write_text(t, encoding="utf-8", newline="\n")
        print("wrote", OUT_DIR / part, "segments",
              sum(1 for l in t.splitlines() if re.search(r"\^[0-9A-Za-z-]+$", l)))
