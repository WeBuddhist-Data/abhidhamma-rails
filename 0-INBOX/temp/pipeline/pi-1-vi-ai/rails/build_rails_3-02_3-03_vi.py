"""Builder for the Vietnamese rails translation of pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng», plain audience),
chapters 3-02 (exposition of the twofold classification of matter, ^1-595 … ^1-743) and 3-03 (exposition of the
three- to elevenfold classifications, ^1-744 … ^1-984).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/3-02-rupakandam.md
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/3-03-rupakandam.md
  0-INBOX/temp/pipeline/pi-1-vi-ai/rails/notes-3-02_3-03.md

Every line is translated from the Pāli by fixed strings. The earlier rails builders are imported, never edited:
build_rails_sample_vi.py (S) and build_rails_3-01_vi.py (R, which loads 2-05 = E, 2-04 = D, 2-03 = T,
2-01/2-02 = B). A check rebuilds 2-01 … 3-01 in memory and requires them to equal the finished files byte for byte.
The stand-alone matter predicates of 3-01 (R.mpred / R.pred_expr, R.MATTER_NOUN, R.GEN …) are the answers here,
imported, never retyped. ONE answer frame for «idaṃ taṃ rūpaṃ P»: «– vật chất này P.» (no «là» of its own, so the
predicate's own «là» is never doubled); the question frame is 3-01's «Vật chất nào P?».
Unknown Pāli raises KeyError, so nothing is guessed silently.
Terms follow the locked termbase AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md
(+ pi-1-vi-ai/termbase/APPROVED.md). Translated fresh from the Pāli.

usage: python -I -X utf8 build_rails_3-02_3-03_vi.py
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-vi-ai\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)

_spec = importlib.util.spec_from_file_location("build_rails_3_01_vi", HERE / "build_rails_3-01_vi.py")
R = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(R)        # importing writes nothing; R.E = 2-05, R.D = 2-04, R.T = 2-03, R.B = 2-01/2-02
B = R.B

PARTS = ["3-02-rupakandam.md", "3-03-rupakandam.md"]
cap = S.cap
PE, ELL, DASH = "…pe…", "…", "–"
RUPA = R.RUPA                                       # vật chất
MN = R.MATTER_NOUN
P = S.PREDS
REL = S.REL                                         # «Điều mà» (Yo / Yā / Yaṃ opening a definition)
SLIPS = []                                          # (segment, note)

# =========================================================================================
# 1. Question and answer frames
# =========================================================================================
THIS = f"{RUPA} này"                                # idaṃ taṃ rūpaṃ


def q_frame(pred, mark="?"):
    """Katamaṃ taṃ rūpaṃ X?  ->  «Vật chất nào X?» (3-01's frame)"""
    return f"{cap(RUPA)} nào {pred}{mark}"


def a_frame(pred, mark="."):
    """idaṃ taṃ rūpaṃ X.  ->  «vật chất này X.» (never «… này là là …»)"""
    return f"{THIS} {pred}{mark}"


# Combined predicates (3-03): «ajjhattikaṃ upādā» = «thuộc phần bên trong và là phái sinh»; a member that already
# carries «và» / «nhưng» / «cũng» or a comma is joined with «, » instead.
QUALS = sorted(["ajjhattikaṃ", "bāhiraṃ", "upādā", "no upādā", "upādiṇṇaṃ", "anupādiṇṇaṃ", "upādiṇṇupādāniyaṃ",
                "anupādiṇṇupādāniyaṃ", "sappaṭighaṃ", "appaṭighaṃ", "indriyaṃ", "na indriyaṃ", "mahābhūtaṃ",
                "na mahābhūtaṃ", "anidassanaṃ"], key=len, reverse=True)
AND = " và "


def joined(a, b):
    sep = ", " if any(x in f"{a} {b}" for x in (" và ", " nhưng ", ",", " cũng ")) else AND
    return a + sep + b


def norm_pred(s):
    s = re.sub(r"\s+…pe…", PE, s)                   # stray space before …pe… (reported per segment)
    return s.replace(" na ārammaṇaṃ", " nārammaṇaṃ")  # «na ārammaṇaṃ» (3-02/3-03) = 3-01's «nārammaṇaṃ»


def qpred(s):
    s = norm_pred(s)
    try:
        return R.pred_expr(s)
    except KeyError:
        pass
    for q in QUALS:
        if s.startswith(q + " "):
            return joined(R.mpred(q), qpred(s[len(q) + 1:]))
    raise KeyError("predicate: " + s)


assert qpred("upādā") == "là phái sinh" and qpred("cakkhusamphassassa na ārammaṇaṃ") == R.mpred(
    "cakkhusamphassassa nārammaṇaṃ")
assert qpred("ajjhattikaṃ upādā") == "thuộc phần bên trong và là phái sinh"

# =========================================================================================
# 2. Variant brackets and item lists
# =========================================================================================
SIG = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka."}
READING_WORDS = {"lapilakaṃ"}                       # a different word (lambilaṃ / lapilakaṃ): «dị bản»
BR = re.compile(r"\[([^\]]+?) \(([^)]+)\)\]")


def var_vi(words, sig):
    sig = ", ".join(SIG[x] for x in sig.split())
    return (S.reading if words in READING_WORDS else S.spell)(sig, words)


def tokens(text):
    out = []
    for m in re.finditer(r"\[[^\]]+\]|[^\s,]+", text):
        t = m.group(0)
        if t.startswith("["):
            out[-1][1].append(var_vi(*BR.fullmatch(t).groups()))
        else:
            out.append([t, []])
    return out


def seq_vi(text, table):
    """space- or comma-separated items, longest match (up to 3 words) in table; a variant follows its item"""
    toks, out, i = tokens(text), [], 0
    while i < len(toks):
        for n in (3, 2, 1):
            if i + n > len(toks):
                continue
            key = " ".join(t[0] for t in toks[i:i + n])
            key = key[0].lower() + key[1:]
            if key in table:
                out.append(table[key] + "".join(" " + v for t in toks[i:i + n] for v in t[1]))
                i += n
                break
        else:
            raise KeyError("item: " + " ".join(t[0] for t in toks[i:i + 3]))
    return out


def items_vi(text, table=MN):
    """«X Y…pe… Z» = «X, Y… Z» (items joined with «, »; …pe… = «…»)"""
    return f"{ELL} ".join(", ".join(seq_vi(c, table)) for c in text.split(PE))


# =========================================================================================
# 3. «yaṃ vā panaññampi atthi rūpaṃ Q: …» and «Kammassa katattā …»
# =========================================================================================
OTHER = f"hoặc còn có bất cứ {RUPA} nào khác"      # yaṃ vā panaññampi atthi rūpaṃ (as ch. 2 «ye vā pana … aññepi atthi»)
KAMMA = "do nghiệp đã được tạo"                     # kammassa katattā (termbase)
NA_KAMMA = "không " + KAMMA                         # na kammassa katattā
CITTAJA = "sinh từ tâm, có tâm làm gốc rễ, do tâm sinh ra"   # cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ (termbase)
NA_CITTAJA = "không sinh từ tâm, không có tâm làm gốc rễ, không do tâm sinh ra"
assert CITTAJA.endswith(R.MATTER_ADJ["cittasamuṭṭhānaṃ"]) and NA_CITTAJA.endswith(R.MATTER_ADJ["na cittasamuṭṭhānaṃ"])
QUAL_P = [("na cittajaṃ na cittahetukaṃ na cittasamuṭṭhānaṃ", NA_CITTAJA),
          ("cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ", CITTAJA),
          ("na kammassa katattā", NA_KAMMA), ("kammassa katattā", KAMMA)]
YVP_RE = re.compile(r"(.+?)(,?) yaṃ vā panaññampi atthi rūpaṃ (.+)")


def list_body_vi(body, sid):
    m = YVP_RE.fullmatch(body)
    if m:
        pre, comma, post = m.groups()
        if not comma:
            SLIPS.append((sid, "no comma before «yaṃ vā panaññampi»: rendered as meant (comma)"))
        for qp, qv in QUAL_P:
            if post.startswith(qp + " ") or post.startswith(qp + ", "):
                rest = post[len(qp):]
                if rest.startswith(","):
                    SLIPS.append((sid, f"comma after «{qp}»: the same Vietnamese as the parallels"))
                return f"{items_vi(pre)}, {OTHER} {qv}: {items_vi(rest.lstrip(', '))}"
        raise KeyError("yaṃ vā pana: " + post[:60])
    for qp, qv in QUAL_P[2:]:
        if body.startswith(cap(qp) + " "):
            return f"{cap(qv)}: {items_vi(body[len(qp) + 1:])}"   # Kammassa katattā X Y = «Do nghiệp đã được tạo: X, Y»
    return items_vi(body)


# =========================================================================================
# 4. The sense organs and their objects (^1-596 … ^1-631, ^1-647 … ^1-650 and the …pe… repeats)
# =========================================================================================
FOUR = f"bốn {MN['mahābhūtaṃ']}"                    # catunnaṃ mahābhūtānaṃ
IQ = P["anidassanasappaṭighā"]                      # anidassano sappaṭigho (termbase, as 1-matika)
VQ = P["sanidassanasappaṭighā"]                     # sanidassanaṃ sappaṭighaṃ
assert IQ == "không thấy được nhưng có tính va chạm" and VQ == "thấy được và có tính va chạm"
UPP_P = "uppajji vā uppajjati vā uppajjissati vā uppajje vā"
PAT_P = "paṭihaññi vā paṭihaññati vā paṭihaññissati vā paṭihaññe vā"


def tense(v):
    """X-i vā X-ti vā X-issati vā X-e vā = «đã X, đang X, sẽ X hoặc có thể X»"""
    return f"đã {v}, đang {v}, sẽ {v} hoặc có thể {v}"


UPP_V = tense("sinh khởi")                          # uppajji … (termbase uppajji «đã sinh khởi» …)
PAT_V = tense("va chạm")                            # paṭihaññi … (termbase «đã va chạm», «đang va chạm» …)
SENSE = {   # organ (o), object (x), object quality, verb; Pāli forms
    "cakkhu": dict(o="mắt", x="hình sắc", xq=VQ, verb="thấy", rel="Yaṃ cakkhu", acc="cakkhuṃ", sph="cakkhu",
                   xacc="rūpaṃ", xst="rūpa", ay="cakkhāyatanaṃ", dh="cakkhudhātu", ind="cakkhundriyaṃ",
                   n1="cakkhuṃ petaṃ", xay="rūpāyatanaṃ", xdh="rūpadhātu", xn1="rūpaṃ petaṃ"),
    "sota": dict(o="tai", x="âm thanh", xq=IQ, verb="nghe", rel="Yaṃ sotaṃ", acc="sotaṃ", sph="sota",
                 xacc="saddaṃ", xst="sadda", ay="sotāyatanaṃ", dh="sotadhātu", ind="sotindriyaṃ",
                 n1="sotaṃ petaṃ", xay="saddāyatanaṃ", xdh="saddadhātu", xn1="saddo peso"),
    "ghāna": dict(o="mũi", x="mùi", xq=IQ, verb="ngửi", rel="Yaṃ ghānaṃ", acc="ghānaṃ", sph="ghāna",
                  xacc="gandhaṃ", xst="gandha", ay="ghānāyatanaṃ", dh="ghānadhātu", ind="ghānindriyaṃ",
                  n1="ghānaṃ petaṃ", xay="gandhāyatanaṃ", xdh="gandhadhātu", xn1="gandho peso"),
    "jivhā": dict(o="lưỡi", x="vị", xq=IQ, verb="nếm", rel="Yā jivhā", acc="jivhaṃ", sph="jivhā",
                  xacc="rasaṃ", xst="rasa", ay="jivhāyatanaṃ", dh="jivhādhātu", ind="jivhindriyaṃ",
                  n1="jivhā pesā", xay="rasāyatanaṃ", xdh="rasadhātu", xn1="raso peso"),
    "kāya": dict(o="thân", x="vật xúc chạm", xq=IQ, verb="chạm", rel="Yo kāyo", acc="kāyaṃ", sph="kāya",
                 xacc="phoṭṭhabbaṃ", xst="phoṭṭhabba", ay="kāyāyatanaṃ", dh="kāyadhātu", ind="kāyindriyaṃ",
                 n1="kāyo peso", xay="phoṭṭhabbāyatanaṃ", xdh="phoṭṭhabbadhātu", xn1="phoṭṭhabbo peso"),
}
for _k, _s in SENSE.items():
    assert MN[_s["ay"]] == f"lĩnh vực {_s['o']}" and MN[_s["xay"]] == f"lĩnh vực {_s['x']}", _k
    _s["C"] = R.GEN[f"{_s['sph']}samphassassa"]                   # sự tiếp xúc của mắt
    _s["F"] = f"cảm giác sinh từ {_s['C']}"                       # …samphassajā vedanā
    _s["W"] = f"thức qua {_s['o']}"                               # …viññāṇaṃ
assert SENSE["cakkhu"]["F"] == R.GEN["cakkhusamphassajāya vedanāya"] and SENSE["kāya"]["W"] == R.GEN["kāyaviññāṇassa"]
SN, CE = S.FN["saññā"], S.FN["cetanā"]              # tri giác, chủ ý

# the clauses as written in the Pāli (a: perceives, b: object strikes the organ, c: organ strikes the object)
ORG_CL = {
    "cakkhu": {"a": "yena cakkhunā anidassanena sappaṭighena rūpaṃ sanidassanaṃ sappaṭighaṃ "
                    "passi vā passati vā passissati vā passe vā",
               "b": f"yamhi cakkhumhi anidassanamhi sappaṭighamhi rūpaṃ sanidassanaṃ sappaṭighaṃ {PAT_P}",
               "c": f"yaṃ cakkhu anidassanaṃ sappaṭighaṃ rūpamhi sanidassanamhi sappaṭighamhi {PAT_P}"},
    "sota": {"a": "yena sotena anidassanena sappaṭighena saddaṃ anidassanaṃ sappaṭighaṃ "
                  "suṇi vā suṇāti vā suṇissati vā suṇe vā",
             "b": f"yamhi sotamhi anidassanamhi sappaṭighamhi saddo anidassano sappaṭigho {PAT_P}",
             "c": f"yaṃ sotaṃ anidassanaṃ sappaṭighaṃ saddamhi anidassanamhi sappaṭighamhi {PAT_P}"},
    "ghāna": {"a": "yena ghānena anidassanena sappaṭighena gandhaṃ anidassanaṃ sappaṭighaṃ "
                   "ghāyi vā ghāyati vā ghāyissati vā ghāye vā",
              "b": f"yamhi ghānamhi anidassanamhi sappaṭighamhi gandho anidassano sappaṭigho {PAT_P}",
              "c": f"yaṃ ghānaṃ anidassanaṃ sappaṭighaṃ gandhamhi anidassanamhi sappaṭighamhi {PAT_P}"},
    "jivhā": {"a": "yāya jivhāya anidassanāya sappaṭighāya rasaṃ anidassanaṃ sappaṭighaṃ "
                   "sāyi vā sāyati vā sāyissati vā sāye vā",
              "bi": f"yāya jivhāya anidassanāya sappaṭighāya raso anidassano sappaṭigho {PAT_P}",
              "c": f"yā jivhā anidassanā sappaṭighā rasamhi anidassanamhi sappaṭighamhi {PAT_P}"},
    "kāya": {"a": "yena kāyena anidassanena sappaṭighena phoṭṭhabbaṃ anidassanasappaṭighaṃ "
                  "phusi vā phusati vā phusissati vā phuse vā",
             "b": f"yamhi kāyamhi anidassanamhi sappaṭighamhi phoṭṭhabbo anidassano sappaṭigho {PAT_P}",
             "c": f"yo kāyo anidassano sappaṭigho phoṭṭhabbamhi anidassanamhi sappaṭighamhi {PAT_P}"},
}
OBJ_CL = {
    "cakkhu": {"a": "yaṃ rūpaṃ sanidassanaṃ sappaṭighaṃ cakkhunā anidassanena sappaṭighena "
                    "passi vā passati vā passissati vā passe vā",
               "b": f"yamhi rūpamhi sanidassanamhi sappaṭighamhi cakkhuṃ anidassanaṃ sappaṭighaṃ {PAT_P}",
               "c": f"yaṃ rūpaṃ sanidassanaṃ sappaṭighaṃ cakkhumhi anidassanamhi sappaṭighamhi {PAT_P}"},
    "sota": {"a": "yaṃ saddaṃ anidassanaṃ sappaṭighaṃ sotena anidassanena sappaṭighena "
                  "suṇi vā suṇāti vā suṇissati vā suṇe vā",
             "b": f"yamhi saddamhi anidassanamhi sappaṭighamhi sotaṃ anidassanaṃ sappaṭighaṃ {PAT_P}",
             "c": f"yo saddo anidassano sappaṭigho sotamhi anidassanamhi sappaṭighamhi {PAT_P}"},
    "ghāna": {"a": "yaṃ gandhaṃ anidassanaṃ sappaṭighaṃ ghānena anidassanena sappaṭighena "
                   "ghāyi vā ghāyati vā ghāyissati vā ghāye vā",
              "b": f"yamhi gandhamhi anidassanamhi sappaṭighamhi ghānaṃ anidassanaṃ sappaṭighaṃ {PAT_P}",
              "c": f"yo gandho anidassano sappaṭigho ghānamhi anidassanamhi sappaṭighamhi {PAT_P}"},
    "jivhā": {"a": "yaṃ rasaṃ anidassanaṃ sappaṭighaṃ jivhāya anidassanāya sappaṭighāya "
                   "sāyi vā sāyati vā sāyissati vā sāye vā",
              "b": f"yamhi rasamhi anidassanamhi sappaṭighamhi jivhā anidassanā sappaṭighā {PAT_P}",
              "ci": f"yo raso anidassano sappaṭigho jivhāya anidassanāya sappaṭighāya {PAT_P}"},
    "kāya": {"a": "yaṃ phoṭṭhabbaṃ anidassanaṃ sappaṭighaṃ kāyena anidassanena sappaṭighena "
                  "phusi vā phusati vā phusissati vā phuse vā",
             "b": f"yamhi phoṭṭhabbamhi anidassanamhi sappaṭighamhi kāyo anidassano sappaṭigho {PAT_P}",
             "c": f"yo phoṭṭhabbo anidassano sappaṭigho kāyamhi anidassanamhi sappaṭighamhi {PAT_P}"},
}


def d_org_p(s):
    a, x, xs, sp = s["acc"], s["xacc"], s["xst"][:-1], s["sph"]     # rūpa + ārammaṇo = rūpārammaṇo
    return (f"yaṃ {a} nissāya {x} ārabbha {sp}samphasso {UPP_P}{PE} yaṃ {a} nissāya {x} ārabbha "
            f"{sp}samphassajā vedanā{PE} saññā{PE} cetanā{PE} {sp}viññāṇaṃ {UPP_P}{PE} yaṃ {a} nissāya "
            f"{xs}ārammaṇo {sp}samphasso {UPP_P}{PE} yaṃ {a} nissāya {xs}ārammaṇā {sp}samphassajā "
            f"vedanā{PE} saññā{PE} cetanā{PE} {sp}viññāṇaṃ {UPP_P}")


def d_obj_p(s):
    a, x, xs, sp = s["acc"], s["xacc"], s["xst"][:-1], s["sph"]     # rūpa + ārammaṇo = rūpārammaṇo
    return (f"yaṃ {x} ārabbha {a} nissāya {sp}samphasso {UPP_P}{PE} yaṃ {x} ārabbha {a} nissāya "
            f"{sp}samphassajā vedanā{PE} saññā{PE} cetanā{PE} {sp}viññāṇaṃ {UPP_P}{PE} yaṃ {xs}ārammaṇo "
            f"{a} nissāya {sp}samphasso {UPP_P}{PE} yaṃ {xs}ārammaṇā {a} nissāya {sp}samphassajā "
            f"vedanā{PE} saññā{PE} cetanā{PE} {sp}viññāṇaṃ {UPP_P}")


def chain(s):
    """…samphassajā vedanā…pe… saññā…pe… cetanā…pe… …viññāṇaṃ"""
    return f"{s['F']}{ELL} {SN}{ELL} {CE}{ELL} {s['W']}"


def org_cl_v(s, kind):
    o, x, xq = s["o"], s["x"], s["xq"]
    if kind == "a":     # yena cakkhunā … rūpaṃ … passi …
        return f"nhờ {o} {IQ} ấy, người ta {tense(s['verb'])} {x} {xq}"
    if kind in ("b", "bi"):     # yamhi cakkhumhi … rūpaṃ … paṭihaññi … (bi: instrumental yāya jivhāya, ^1-609)
        return f"{'với' if kind == 'bi' else 'vào'} {o} {IQ} ấy, {x} {xq} {PAT_V}"
    if kind == "c":     # yaṃ cakkhu … rūpamhi … paṭihaññi …
        return f"{o} {IQ} ấy {PAT_V} vào {x} {xq}"
    if kind == "d":     # yaṃ cakkhuṃ nissāya rūpaṃ ārabbha … / rūpārammaṇo …
        return (f"dựa vào {o} ấy và lấy {x} làm đối tượng, {s['C']} {UPP_V}{ELL} dựa vào {o} ấy và lấy {x} "
                f"làm đối tượng, {chain(s)} {UPP_V}{ELL} dựa vào {o} ấy, {s['C']} lấy {x} làm đối tượng {UPP_V}"
                f"{ELL} dựa vào {o} ấy, {s['F']} lấy {x} làm đối tượng{ELL} {SN}{ELL} {CE}{ELL} {s['W']} {UPP_V}")
    raise KeyError(kind)


def obj_cl_v(s, kind):
    o, x, xq = s["o"], s["x"], s["xq"]
    if kind == "a":     # yaṃ rūpaṃ … cakkhunā … passi …
        return f"người ta {tense(s['verb'])} {x} {xq} ấy bằng {o} {IQ}"
    if kind == "b":     # yamhi rūpamhi … cakkhuṃ … paṭihaññi …
        return f"vào {x} {xq} ấy, {o} {IQ} {PAT_V}"
    if kind in ("c", "ci"):     # yaṃ rūpaṃ … cakkhumhi … paṭihaññi … (ci: instrumental jivhāya, ^1-630)
        return f"{x} {xq} ấy {PAT_V} {'với' if kind == 'ci' else 'vào'} {o} {IQ}"
    if kind == "d":     # yaṃ rūpaṃ ārabbha cakkhuṃ nissāya … / yaṃ rūpārammaṇo cakkhuṃ nissāya …
        return (f"lấy {x} ấy làm đối tượng và dựa vào {o}, {s['C']} {UPP_V}{ELL} lấy {x} ấy làm đối tượng và "
                f"dựa vào {o}, {chain(s)} {UPP_V}{ELL} dựa vào {o}, {s['C']} lấy {x} ấy làm đối tượng {UPP_V}"
                f"{ELL} dựa vào {o}, {s['F']} lấy {x} ấy làm đối tượng{ELL} {SN}{ELL} {CE}{ELL} {s['W']} {UPP_V}")
    raise KeyError(kind)


# the fourteen names of the organ (cakkhuṃ petaṃ … suñño gāmo peso); nettaṃ / nayanaṃ only for the eye
COMMON_P = ("loko peso dvārā pesā samuddo peso paṇḍaraṃ petaṃ khettaṃ petaṃ vatthuṃ petaṃ{X} orimaṃ tīraṃ petaṃ "
            "suñño gāmo peso")
EYE_P = " nettaṃ petaṃ nayanaṃ petaṃ"
THIS_IS = "đây là"                                  # X petaṃ / peso / pesā
COMMON_V = ["thế gian", "cánh cửa", "đại dương", "sự sáng ngời", "cánh đồng", R.VATTHU]   # loko … vatthuṃ
EYE_V = ["cái dẫn đường", "cái chỉ lối"]            # nettaṃ, nayanaṃ
END_V = ["bờ bên này", "ngôi làng trống rỗng"]       # orimaṃ tīraṃ, suñño gāmo
assert S.S_CITTA.split(", ")[4] == "sự sáng ngời"   # paṇḍaraṃ as in the citta string


def names_org_p(k, s):
    return f"{s['n1']} {s['ay']} petaṃ {s['dh']} pesā {s['ind']} petaṃ " + COMMON_P.format(
        X=EYE_P if k == "cakkhu" else "")


def names_org_v(k, s):
    ns = [s["o"], MN[s["ay"]], MN[s["dh"]], MN[s["ind"]]] + COMMON_V + (EYE_V if k == "cakkhu" else []) + END_V
    return ", ".join(f"{THIS_IS} {n}" for n in ns)


def names_obj_p(s):
    return f"{s['xn1']} {s['xay']} petaṃ {s['xdh']} pesā"


def names_obj_v(s):
    return ", ".join(f"{THIS_IS} {n}" for n in (s["x"], MN[s["xay"]], MN[s["xdh"]]))


def org_head_p(s, full=True):
    tail = " attabhāvapariyāpanno anidassano sappaṭigho" if full else ""
    return f"{s['rel']} catunnaṃ mahābhūtānaṃ upādāya pasādo{tail}"


def org_head_v(s, var=""):
    # Yaṃ cakkhu catunnaṃ mahābhūtānaṃ upādāya pasādo attabhāvapariyāpanno anidassano sappaṭigho
    return (f"{cap(s['o'])}{var} là chất nhạy cảm phái sinh từ {FOUR}, nằm trong sự tồn tại cá nhân, {IQ}")


ORG_ABBR_V = "{O} là chất nhạy cảm phái sinh từ " + FOUR + ELL + " " + THIS_IS + " " + END_V[-1]


def organ_def(body, sid):
    var = ""
    if body.startswith("Yaṃ cakkhu [cakkhuṃ (sī. syā.)] "):
        body = body.replace(" [cakkhuṃ (sī. syā.)]", "", 1)
        var = " " + S.spell("Sī., Syā.", "cakkhuṃ")
    if "gāmopeso" in body:
        body = body.replace("gāmopeso", "gāmo peso")
        SLIPS.append((sid, "«gāmopeso» (no space): rendered as meant («gāmo peso»)"))
    for k, s in SENSE.items():
        if body == f"{org_head_p(s, False)}{PE} suñño gāmo peso":
            return ORG_ABBR_V.format(O=cap(s["o"]))
        head, names = org_head_p(s) + ", ", ", " + names_org_p(k, s)
        if not (body.startswith(head) and body.endswith(names)):
            continue
        cl = body[len(head):-len(names)]
        kinds = dict(ORG_CL[k], d=d_org_p(s))
        for kind, p in kinds.items():
            if cl == p:
                if kind == "bi":
                    SLIPS.append((sid, "«yāya jivhāya …» (instrumental where the parallels have the locative "
                                       "«yamhi …»): translated as written («với lưỡi …»)"))
                return f"{org_head_v(s, var)}; {org_cl_v(s, kind)}; {names_org_v(k, s)}"
        raise KeyError("organ clause: " + cl[:80])
    return None


# the objects: lists of colours, sounds, smells, tastes, tangibles
VN = "màu sắc và dáng vẻ"                           # vaṇṇanibhā (termbase)
OBJ_WORDS = {
    # visible forms
    "nīlaṃ": "màu xanh", "pītakaṃ": "màu vàng", "lohitakaṃ": "màu đỏ", "odātaṃ": "màu trắng", "kāḷakaṃ": "màu đen",
    "mañjiṭṭhakaṃ": "màu đỏ thẫm", "hari": "màu xanh lục", "harivaṇṇaṃ": "màu ánh lục",
    "ambaṅkuravaṇṇaṃ": "màu chồi xoài",
    "dīghaṃ": "dài", "rassaṃ": "ngắn", "aṇuṃ": "nhỏ", "thūlaṃ": "to",           # no termbase entries
    "vaṭṭaṃ": "tròn", "parimaṇḍalaṃ": "tròn trịa", "caturaṃsaṃ": "bốn góc", "chaḷaṃsaṃ": "sáu góc",
    "aṭṭhaṃsaṃ": "tám góc", "soḷasaṃsaṃ": "mười sáu góc",
    "ninnaṃ": "chỗ trũng", "thalaṃ": "chỗ cao",                                  # no termbase entries
    "chāyā": "bóng râm", "ātapo": "nắng", "āloko": "ánh sáng", "andhakāro": "bóng tối", "abbhā": "mây",
    "mahikā": "sương mù", "dhūmo": "khói", "rajo": "bụi",
    "candamaṇḍalassa vaṇṇanibhā": f"{VN} của vầng trăng",          # canda «trăng» + maṇḍalassa «vầng»
    "sūriyamaṇḍalassa vaṇṇanibhā": f"{VN} của vầng mặt trời",      # sūriya «mặt trời»
    "tārakarūpānaṃ vaṇṇanibhā": f"{VN} của các vì sao",
    "ādāsamaṇḍalassa vaṇṇanibhā": f"{VN} của vầng gương",          # ādāsa «gương» + maṇḍalassa «vầng»
    "maṇisaṅkhamuttāveḷuriyassa vaṇṇanibhā": f"{VN} của ngọc quý, vỏ ốc, ngọc trai và ngọc lưu ly",
    "jātarūparajatassa vaṇṇanibhā": f"{VN} của vàng và bạc",
    # sounds
    "bherisaddo": "tiếng trống lớn", "mudiṅgasaddo": "tiếng trống cơm", "saṅkhasaddo": "tiếng tù và",
    "paṇavasaddo": "tiếng trống con", "gītasaddo": "tiếng hát", "vāditasaddo": "tiếng nhạc cụ",
    "sammasaddo": "tiếng chũm chọe", "pāṇisaddo": "tiếng vỗ tay",
    "sattānaṃ nigghosasaddo": "tiếng ồn ào của chúng sinh", "dhātūnaṃ sannighātasaddo": "tiếng va đập của các vật",
    "vātasaddo": "tiếng gió", "udakasaddo": "tiếng nước", "manussasaddo": "tiếng người",
    "amanussasaddo": "tiếng của những loài không phải người",
    # smells
    "mūlagandho": "mùi rễ cây", "sāragandho": "mùi lõi cây", "tacagandho": "mùi vỏ cây", "pattagandho": "mùi lá",
    "pupphagandho": "mùi hoa", "phalagandho": "mùi trái cây", "āmakagandho": "mùi tanh",
    "vissagandho": "mùi ôi thiu", "sugandho": "mùi thơm", "duggandho": "mùi hôi",
    # tastes
    "mūlaraso": "vị rễ cây", "khandharaso": "vị thân cây", "tacaraso": "vị vỏ cây", "pattaraso": "vị lá",
    "puppharaso": "vị hoa", "phalaraso": "vị trái cây", "ambilaṃ": "vị chua", "madhuraṃ": "vị ngọt",
    "tittakaṃ": "vị đắng", "kaṭukaṃ": "vị cay", "loṇikaṃ": "vị mặn", "khārikaṃ": "vị kiềm",
    "lambilaṃ": "vị chua nhẹ", "kasāvo": "vị chát", "sādu": "vị ngon", "asādu": "vị không ngon",
    # tangibles
    "pathavīdhātu": MN["pathavīdhātu"], "tejodhātu": MN["tejodhātu"], "vāyodhātu": MN["vāyodhātu"],
    "kakkhaḷaṃ": "cái cứng", "mudukaṃ": "cái mềm", "saṇhaṃ": "cái mịn", "pharusaṃ": "cái thô ráp",
    "sukhasamphassaṃ": "cái mà " + R.MATTER_ADJ["sukhasamphassaṃ"],
    "dukkhasamphassaṃ": "cái mà " + R.MATTER_ADJ["dukkhasamphassaṃ"],
    "garukaṃ": "cái nặng", "lahukaṃ": "cái nhẹ",
}
TOUCH_P = ("Pathavīdhātu tejodhātu vāyodhātu kakkhaḷaṃ mudukaṃ saṇhaṃ pharusaṃ sukhasamphassaṃ dukkhasamphassaṃ "
           "garukaṃ lahukaṃ")


def obj_start_p(k, s):
    if k == "cakkhu":
        return ("Yaṃ rūpaṃ catunnaṃ mahābhūtānaṃ upādāya vaṇṇanibhā sanidassanaṃ sappaṭighaṃ",
                "yaṃ vā panaññampi atthi rūpaṃ catunnaṃ mahābhūtānaṃ upādāya vaṇṇanibhā sanidassanaṃ sappaṭighaṃ")
    nom = s["xn1"].split()[0]                       # saddo / gandho / raso
    return (f"Yo {nom} catunnaṃ mahābhūtānaṃ upādāya anidassano sappaṭigho",
            f"yo vā panaññopi atthi {nom} catunnaṃ mahābhūtānaṃ upādāya anidassano sappaṭigho")


def obj_head_v(k, s, lst):
    x = s["x"]
    if k == "cakkhu":   # Yaṃ rūpaṃ … upādāya vaṇṇanibhā sanidassanaṃ sappaṭighaṃ L, yaṃ vā panaññampi atthi rūpaṃ …
        return (f"{cap(x)} là {VN} phái sinh từ {FOUR}, {VQ}, như {lst}, hoặc còn có bất cứ {x} nào khác là {VN} "
                f"phái sinh từ {FOUR}, {VQ}")
    # Yo saddo … upādāya anidassano sappaṭigho L, yo vā panaññopi atthi saddo …
    return (f"{cap(x)} là điều phái sinh từ {FOUR}, {IQ}, như {lst}, hoặc còn có bất cứ {x} nào khác phái sinh "
            f"từ {FOUR}, {IQ}")


OBJ_ABBR = {
    "Yaṃ rūpaṃ catunnaṃ mahābhūtānaṃ upādāya vaṇṇanibhā…pe… rūpadhātu pesā":
        f"{cap(SENSE['cakkhu']['x'])} là {VN} phái sinh từ {FOUR}{ELL} {THIS_IS} {MN['rūpadhātu']}",
    "Pathavīdhātu…pe… phoṭṭhabbadhātu pesā": f"{cap(MN['pathavīdhātu'])}{ELL} {THIS_IS} {MN['phoṭṭhabbadhātu']}",
}


def object_def(body, sid):
    if body in OBJ_ABBR:
        return OBJ_ABBR[body]
    for k, s in SENSE.items():
        names = names_obj_p(s)
        if not body.endswith(names):
            continue
        if k == "kāya":
            if not body.startswith(TOUCH_P + ", "):
                continue
            head_v = ", ".join(seq_vi(TOUCH_P, OBJ_WORDS))
            rest = body[len(TOUCH_P) + 2:-len(names)]
        else:
            start, yvp = obj_start_p(k, s)
            m = re.fullmatch(re.escape(start) + r" (.+?), " + re.escape(yvp) + r", (.+)" + re.escape(names), body)
            if not m:
                continue
            head_v = obj_head_v(k, s, ", ".join(seq_vi(m.group(1), OBJ_WORDS)))
            rest = m.group(2)
        if rest.endswith(", "):
            cl = rest[:-2]
        else:
            cl = rest[:-1]
            SLIPS.append((sid, f"no comma before «{names.split()[0]} peso»: rendered as meant"))
        kinds = dict(OBJ_CL[k], d=d_obj_p(s))
        for kind, p in kinds.items():
            if cl == p:
                if kind == "ci":
                    SLIPS.append((sid, "«jivhāya anidassanāya sappaṭighāya» (instrumental where the parallels have "
                                       "the locative «…mhi»): translated as written («với lưỡi …»)"))
                return f"{head_v}; {obj_cl_v(s, kind)}; {names_obj_v(s)}"
        raise KeyError("object clause: " + cl[:80])
    return None


# =========================================================================================
# 5. The short definitions (fixed strings)
# =========================================================================================
CITTAS = "khi có tâm thiện, tâm bất thiện hoặc tâm không xác định về mặt đạo đức"   # kusalacittassa vā … vā
VACA = ("lời nói, lời lẽ, cách nói, sự thốt ra, tiếng nói, sự phát ra tiếng nói, lời nói, "
        "sự phát thành lời nói")                    # vācā girā byappatho udīraṇaṃ ghoso ghosakammaṃ vācā vacībhedo
CALLED_VACA = "đó được gọi là lời nói"              # ayaṃ vuccati vācā (3-01: idaṃ vuccati X = đó được gọi là X)
INTIM = "sự biểu lộ, sự làm cho biết, trạng thái đã làm cho biết"   # viññatti viññāpanā viññāpitattaṃ
VACA_INTIM = f"{REL} qua lời nói ấy là {INTIM}"     # Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ
RUPA_AT = f"ở {RUPA}"                               # Yā rūpassa … (as ch. 2 «Yo tesaṃ arūpīnaṃ dhammānaṃ» = «ở …»)
GATA = "điều được xem là"                           # -gataṃ (termbase)
ANY_P = "ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā"
ANY_V = (f"dù {S.PREDS['ajjhattā']} hay {S.PREDS['bahiddhā']}, dù {R.MATTER_ADJ['upādiṇṇaṃ']} hay "
         f"{R.MATTER_ADJ['anupādiṇṇaṃ']}")
assert ANY_V == "dù ở nơi bản thân hay ở bên ngoài bản thân, dù do nghiệp tạo ra hay không do nghiệp tạo ra"
APO_V = f"{REL} là nước, {GATA} nước, chất ẩm, {GATA} chất ẩm, tính kết dính của {RUPA}"
KAB_V = ("Cơm, cháo, bột rang, cá, thịt, sữa, sữa đông, bơ lỏng, bơ tươi, dầu, mật ong, mật mía, "
         f"{OTHER} mà ở mỗi vùng đất, đối với từng chúng sinh nơi đó, là thứ được đưa vào miệng, được nhai bằng răng, "
         "được nuốt qua cổ họng, làm căng đầy bụng, tức tinh chất nuôi dưỡng mà nhờ đó chúng sinh duy trì mạng sống")


def sex_v(at, s):
    """Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo"""
    return (f"{REL} ở {at} là hình tướng {s}, dấu hiệu {s}, cử chỉ {s}, dáng điệu {s}, trạng thái {s}, "
            f"tính chất {s}")


SHORT = {
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo":
        sex_v("người nữ", "nữ tính"),
    "Yaṃ purisassa purisaliṅgaṃ purisanimittaṃ purisakuttaṃ purisākappo purisattaṃ purisabhāvo":
        sex_v("người nam", "nam tính"),
    "Yo tesaṃ rūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ":
        f"{REL} ở những hiện tượng thuộc {RUPA} ấy là {B.S_JIVITA_PLAIN}",
    ("Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā abhikkamantassa vā paṭikkamantassa vā "
     "ālokentassa vā vilokentassa vā samiñjentassa vā pasārentassa vā kāyassa thambhanā santhambhanā "
     "santhambhitattaṃ viññatti viññāpanā viññāpitattaṃ"):
        (f"{REL}, {CITTAS}, ở người đang đi tới, đi lui, nhìn thẳng, nhìn sang bên, co lại hoặc duỗi ra, là "
         f"sự căng cứng, sự căng cứng toàn diện, trạng thái căng cứng toàn diện của thân, {INTIM}"),
    ("Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā vācā girā byappatho udīraṇaṃ ghoso ghosakammaṃ "
     "vācā vacībhedo – ayaṃ vuccati vācā. Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ"):
        f"{REL}, {CITTAS}, là {VACA} {DASH} {CALLED_VACA}. {VACA_INTIM}",
    ("Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā vācā girā byappatho udīraṇaṃ ghoso ghosakammaṃ "
     "vācā vacībhedo, ayaṃ vuccati vācā. Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ"):
        f"{REL}, {CITTAS}, là {VACA}, {CALLED_VACA}. {VACA_INTIM}",
    ("Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā vācā girā byappatho udīraṇaṃ dhoso ghosakammaṃ "
     "vācā vacībhedo, ayaṃ vuccati vācā. Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ"):   # ^1-850 «dhoso»
        f"{REL}, {CITTAS}, là {VACA}, {CALLED_VACA}. {VACA_INTIM}",
    "Yo ākāso ākāsagataṃ aghaṃ aghagataṃ vivaro vivaragataṃ asamphuṭṭhaṃ catūhi mahābhūtehi":
        (f"{REL} là không gian, {GATA} không gian, khoảng không, {GATA} khoảng không, kẽ hở, {GATA} kẽ hở, "
         f"điều không bị {FOUR} chạm đến"),
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa": APO_V,
    "Yā rūpassa lahutā lahupariṇāmatā adandhanatā avitthanatā": f"{REL} {RUPA_AT} là {S.S_LAHUTA}",
    "Yā rūpassa mudutā maddavatā akakkhaḷatā akathinatā": f"{REL} {RUPA_AT} là {S.S_MUDUTA}",
    "Yā rūpassa kammaññatā kammaññattaṃ kammaññabhāvo": f"{REL} {RUPA_AT} là {S.S_KAMMANNATA}",
    "Yo āyatanānaṃ ācayo, so rūpassa upacayo":
        f"{REL} là sự tích lũy của các lĩnh vực nhận biết thì đó là {MN['rūpassa upacayo']}",
    "Yo rūpassa upacayo, sā rūpassa santati":
        f"{REL} là {MN['rūpassa upacayo']} thì đó là {MN['rūpassa santati']}",
    "Yā rūpassa jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni indriyānaṃ paripāko":
        (f"{REL} {RUPA_AT} là sự lão hóa, sự hao mòn, răng gãy rụng, tóc bạc, da nhăn nheo, sự suy giảm tuổi thọ, "
         "sự chín muồi của các năng lực"),
    "Yo rūpassa khayo vayo bhedo paribhedo aniccatā antaradhānaṃ":
        f"{REL} {RUPA_AT} là sự hủy diệt, sự suy tàn, sự tan rã, sự tan rã hoàn toàn, tính vô thường, sự biến mất",
    ("Odano kummāso sattu maccho maṃsaṃ khīraṃ dadhi sappi navanītaṃ telaṃ madhu phāṇitaṃ, yaṃ vā panaññampi atthi "
     "rūpaṃ yamhi yamhi janapade tesaṃ tesaṃ sattānaṃ mukhāsiyaṃ dantavikhādanaṃ galajjhoharaṇīyaṃ "
     "kucchivitthambhanaṃ, yāya ojāya sattā yāpenti"): KAB_V,
    # the fivefold: the four great elements
    f"Yaṃ kakkhaḷaṃ kharagataṃ [kharigataṃ (ka.)] kakkhaḷattaṃ kakkhaḷabhāvo {ANY_P}":
        f"{REL} là cái cứng, {GATA} rắn {S.spell('Ka.', 'kharigataṃ')}, sự cứng, tính chất cứng, {ANY_V}",
    f"Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa {ANY_P}": f"{APO_V}, {ANY_V}",
    f"Yaṃ tejo tejogataṃ usmā usmāgataṃ usumaṃ usumagataṃ {ANY_P}":
        f"{REL} là lửa, {GATA} lửa, hơi ấm, {GATA} hơi ấm, hơi nóng, {GATA} hơi nóng, {ANY_V}",
    f"Yaṃ vāyo vāyogataṃ thambhitattaṃ rūpassa {ANY_P}":
        f"{REL} là gió, {GATA} gió, trạng thái căng cứng của {RUPA}, {ANY_V}",
}
_ITTHI = "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo"
SHORT[_ITTHI + " [itthittaṃ itthībhāvo (syā.)]"] = SHORT[_ITTHI] + " " + S.spell("Syā.", "itthittaṃ itthībhāvo")
_KAB = [k for k in SHORT if k.startswith("Odano")][0]
SHORT_SLIP = {   # source slips: the same Vietnamese as the parallel
    _KAB.replace("kucchivitthambhanaṃ, yāya", "kucchivitthambhanaṃ yāya"):
        (KAB_V, "no comma before «yāya ojāya»: rendered as meant (comma)"),
}

# =========================================================================================
# 6. Fixed lines: headings, closings, the four- to eightfold statements
# =========================================================================================
EXPO = {h: f"{R.NIDDESO} {R.CLASS[c][0].lower()}{R.CLASS[c][1:]}" for h, c in
        (("Dukaniddeso", "Dukaṃ"), ("Tikaniddeso", "Tikaṃ"))}
assert EXPO["Dukaniddeso"] == "Giải thích phân loại theo nhóm hai"
UPADA_BHAJ = f"Phân tích {RUPA} phái sinh"         # Upādābhājanīyaṃ (bhājanīyaṃ «phân tích», Upādā «phái sinh»)
H = dict(R.H)
H.update({
    "###### Upādābhājanīyaṃ": f"###### {UPADA_BHAJ}",
    "Upādābhājanīyaṃ.": f"{UPADA_BHAJ}.",
    "Rūpakaṇḍe paṭhamabhāṇavāro.": f"{S.BHANAVARA_1} trong {S.CH_HEADINGS['Rūpakaṇḍaṃ'][0].lower()}"
                                   f"{S.CH_HEADINGS['Rūpakaṇḍaṃ'][1:]}.",
    "Aṭṭhamabhāṇavāro.": S.BHANAVARA_1.replace("thứ nhất", "thứ tám") + ".",
    "Rūpavibhatti.": R.H["#### Rūpavibhatti"][5:] + ".",
    "Rūpakaṇḍaṃ niṭṭhitaṃ.": f"{S.CH_HEADINGS['Rūpakaṇḍaṃ']} đã hoàn tất.",
})
for _h, _v in EXPO.items():
    H[f"##### {_h}"] = f"##### {_v}"
    H[f"{_h}."] = f"{_v}."
assert H["Rūpakaṇḍe paṭhamabhāṇavāro."] == "Phần tụng đọc thứ nhất trong phần về vật chất."
assert H["Rūpavibhatti."] == "Phân tích vật chất." and H["Rūpakaṇḍaṃ niṭṭhitaṃ."] == "Phần về vật chất đã hoàn tất."

SEEN = {"diṭṭhaṃ": "được thấy", "sutaṃ": "được nghe", "mutaṃ": "được cảm nhận"}   # as 3-01 «Diṭṭhaṃ sutaṃ mutaṃ …»
assert all(v in R.H["Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ."] for v in SEEN.values())
THING = "điều"                                      # a bare participle as a noun: «điều được thấy»
SAB = R.SAB                                         # toàn bộ vật chất
DIT_P = ("Rūpāyatanaṃ diṭṭhaṃ, saddāyatanaṃ sutaṃ, gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ mutaṃ, "
         "sabbaṃ rūpaṃ manasā viññātaṃ rūpaṃ.")
DIT_V = (f"{cap(MN['rūpāyatanaṃ'])} là {THING} {SEEN['diṭṭhaṃ']}; {MN['saddāyatanaṃ']} là {THING} {SEEN['sutaṃ']}; "
         f"{MN['gandhāyatanaṃ']}, {MN['rasāyatanaṃ']}, {MN['phoṭṭhabbāyatanaṃ']} là {THING} {SEEN['mutaṃ']}; "
         f"{SAB} là {RUPA} được nhận biết bằng ý.")   # viññātaṃ «được nhận biết», manasā «ý» (instrumental)
H[DIT_P] = DIT_V

# «X Y-viññeyyaṃ rūpaṃ, …» (^1-972 … ^1-974): «X là vật chất mà Y có thể nhận biết; …»
TOUCH_SUBJ = {
    "manāpiyo phoṭṭhabbo sukhasamphasso": f"{MN['phoṭṭhabbāyatanaṃ'][9:]} dễ ưa, {R.MATTER_ADJ['sukhasamphassaṃ']},",
    "amanāpiyo phoṭṭhabbo dukkhasamphasso":
        f"{MN['phoṭṭhabbāyatanaṃ'][9:]} không dễ ưa, {R.MATTER_ADJ['dukkhasamphassaṃ']},",
}
assert TOUCH_SUBJ["manāpiyo phoṭṭhabbo sukhasamphasso"].startswith("vật xúc chạm dễ ưa")
VINN_ITEM = re.compile(r"(.+) (\S+viññeyyaṃ) rūpaṃ")


def vinn_vi(line):
    out = []
    for it in line[:-1].split(", "):
        subj, v = VINN_ITEM.fullmatch(it).groups()
        if subj == "sabbaṃ rūpaṃ":
            sv = SAB
        elif subj in TOUCH_SUBJ:
            sv = TOUCH_SUBJ[subj]
        else:
            sv = ", ".join(seq_vi(subj, MN))
        out.append(f"{sv} là {RUPA} {R.VINN_ATTR[v]}")
    return cap("; ".join(out)) + "."


# =========================================================================================
# 7. Question-and-answer lines
# =========================================================================================
QA_RE = re.compile(r"Katamaṃ taṃ rūpaṃ (.+?)([?.]) (.+?)(?: – idaṃ taṃ rūpaṃ (.+?))?([.?])$")
IDAM_RE = re.compile(r"Idaṃ taṃ rūpaṃ (.+)\.$")
NO_Q = {"1-895": "upādā sukhumaṃ", "1-939": "upādiṇṇupādāniyaṃ santike"}   # «?» missing after the question


def body_vi(body, sid):
    if body in SHORT:
        return SHORT[body]
    if body in SHORT_SLIP:
        v, note = SHORT_SLIP[body]
        SLIPS.append((sid, note))
        return v
    for f in (organ_def, object_def):
        v = f(body, sid)
        if v is not None:
            return v
    return list_body_vi(body, sid)


def qa_vi(line, sid):
    if sid in NO_Q:
        q = NO_Q[sid]
        head = f"Katamaṃ taṃ rūpaṃ {q} "
        assert line.startswith(head)
        line = f"{head[:-1]}? {cap(line[len(head):])}"
        SLIPS.append((sid, "no «?» after the question: rendered as meant («?»)"))
    m = QA_RE.fullmatch(line)
    if not m:
        raise KeyError("qa: " + line[:80])
    q, qm, body, a, end = m.groups()
    if qm == ".":
        SLIPS.append((sid, "the question ends with «.»: kept as written"))
    if end == "?":
        SLIPS.append((sid, "the answer ends with «?»: kept as written"))
    out = f"{q_frame(qpred(q), qm)} {cap(body_vi(body, sid))}"
    if a is None:
        return out + end
    return f"{out} {DASH} {a_frame(qpred(a), end)}"


def translate_line(line, sid):
    if re.search(r"\S\s+…pe…", line):
        SLIPS.append((sid, "a space before «…pe…»: dropped"))
    if line in H:
        return H[line]
    m = IDAM_RE.fullmatch(line)
    if m:
        return cap(a_frame(qpred(m.group(1))))
    if line.startswith("Katamaṃ taṃ rūpaṃ "):
        return qa_vi(line, sid)
    if VINN_ITEM.match(line) and "viññeyyaṃ rūpaṃ" in line:
        return vinn_vi(line)
    raise KeyError("line: " + line[:80])


# =========================================================================================
# 8. Render, checks, build
# =========================================================================================
def render(segs):
    blocks = []
    for sid, plines in segs:
        vlines = []
        for p in plines:
            v = unicodedata.normalize("NFC", cap(translate_line(p, sid)))
            B.check_vi(v)
            assert len(p) - len(p.lstrip("#")) == len(v) - len(v.lstrip("#")), sid
            assert p.count("–") + p.count("—") == v.count("–"), ("dash", sid, p[:60], v[:60])
            assert p.count("…pe…") <= v.count("…"), ("pe", sid)
            assert p.endswith("?") == v.endswith("?"), ("question", sid)
            assert v.endswith(".") or v.endswith("?") or v.startswith("#"), ("stop", sid, v[-40:])
            assert "  " not in v and " ," not in v and ",," not in v and "..." not in v and " ;" not in v, (
                "spacing", sid, v)
            assert ", ," not in v and ",:" not in v and ";," not in v and "…." not in v, ("punct", sid, v)
            assert "đau khổ" not in v and "khổ đau" not in v and "là là" not in v, sid
            assert "chánh niệm" not in v, sid
            vlines.append(v)
        vlines[-1] += f" ^{sid}"
        blocks.append("\n".join(vlines))
    return blocks


def check_earlier_unchanged():
    """Importing 3-01 (and through it 2-05 … 2-01) must leave their outputs exactly as finished."""
    R.check_earlier_unchanged()
    text, _ = R.build()
    assert unicodedata.normalize("NFC", text) == (S.OUT / "3-01-rupakandam.md").read_bytes().decode("utf-8")
    print("3-01: rebuilt in memory, byte-identical to the finished file")


def build(part):
    segs = B.segments(S.PALI / part)
    return "\n\n".join(render(segs)) + "\n", len(segs)


# =========================================================================================
# 9. Notes
# =========================================================================================
def notes():
    k, s = "cakkhu", SENSE["cakkhu"]
    L = ["# pi-1 Vietnamese rails: new formulas of 3-02 and 3-03", "",
         "Generated by build_rails_3-02_3-03_vi.py from its fixed strings; import that file instead of retyping "
         "(q_frame, a_frame, qpred, SENSE, ORG_CL, OBJ_CL, OBJ_WORDS, SHORT, H). Strings already in "
         "vi-rails-formulas.md, the chapter-2 notes or notes-3-01.md are not repeated; every predicate of matter "
         "is 3-01's stand-alone predicate (R.mpred / R.pred_expr), imported. Format: Pāli = tiếng Việt.", "",
         "## Frames", "",
         f"Katamaṃ taṃ rūpaṃ X? = {q_frame('pred(X)')}",
         f"… – idaṃ taṃ rūpaṃ X. = … – {a_frame('pred(X)')}  (the ONE answer frame: no «là» of its own, so a "
         "predicate «là …» is never doubled)",
         f"Idaṃ taṃ rūpaṃ upādā. = {cap(a_frame(qpred('upādā')))}",
         f"Idaṃ taṃ rūpaṃ no upādā. = {cap(a_frame(qpred('no upādā')))}",
         f"X Y (3-03 combined predicates) = pred(X){AND}pred(Y); «, » when a member already has «và» / «nhưng» / "
         "«cũng» or a comma; three members: «A, B và C»",
         f"  ajjhattikaṃ upādā = {qpred('ajjhattikaṃ upādā')}",
         f"  bāhiraṃ cakkhusamphassassa na vatthu = {qpred('bāhiraṃ cakkhusamphassassa na vatthu')}",
         f"  ajjhattikaṃ upādiṇṇupādāniyaṃ = {qpred('ajjhattikaṃ upādiṇṇupādāniyaṃ')}",
         f"  no upādā anupādiṇṇupādāniyaṃ = {qpred('no upādā anupādiṇṇupādāniyaṃ')}",
         f"  bāhiraṃ na sotāyatanaṃ…pe… na kāyāyatanaṃ = {qpred('bāhiraṃ na sotāyatanaṃ…pe… na kāyāyatanaṃ')}",
         f"  anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ = "
         f"{qpred('anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ')}",
         f"X na ārammaṇaṃ (two words) = as 3-01's X nārammaṇaṃ: {qpred('cakkhusamphassassa na ārammaṇaṃ')}",
         "", "## Lists", "",
         "X Y Z / X, Y, Z (items) = X, Y, Z (3-01's names); X…pe… Y = X… Y",
         f"…, yaṃ vā panaññampi atthi rūpaṃ Q X Y = …, {OTHER} Q: X, Y",
         f"  kammassa katattā = {KAMMA}", f"  na kammassa katattā = {NA_KAMMA}",
         f"  cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ = {CITTAJA}",
         f"  na cittajaṃ na cittahetukaṃ na cittasamuṭṭhānaṃ = {NA_CITTAJA}",
         f"Kammassa katattā X Y (opening an answer) = {cap(KAMMA)}: X, Y",
         f"Na kammassa katattā X Y (opening an answer) = {cap(NA_KAMMA)}: X, Y",
         "", "## Sense-organ definitions (the eye; ear, nose, tongue, body alike)", "",
         f"{org_head_p(s)} = {org_head_v(s)}"]
    for kind, p in dict(ORG_CL[k], d=d_org_p(s)).items():
        L.append(f"[{kind}] {p} = {org_cl_v(s, kind)}")
    L += [f"[bi, ^1-609] {ORG_CL['jivhā']['bi']} = {org_cl_v(SENSE['jivhā'], 'bi')}",
          f"{names_org_p(k, s)} = {names_org_v(k, s)}",
          f"{names_org_p('sota', SENSE['sota'])} = {names_org_v('sota', SENSE['sota'])}",
          f"Body = head, clause, names = «head; clause; names»",
          f"{org_head_p(s, False)}{PE} suñño gāmo peso = {ORG_ABBR_V.format(O=cap(s['o']))}",
          f"Yo kāyo catunnaṃ mahābhūtānaṃ upādāya pasādo{PE} suñño gāmo peso = "
          f"{ORG_ABBR_V.format(O=cap(SENSE['kāya']['o']))}",
          "", "## Object definitions (visible form; sound, smell, taste alike; tangibles)", "",
          f"{obj_start_p(k, s)[0]} L, {obj_start_p(k, s)[1]} = {obj_head_v(k, s, 'L')}",
          f"{obj_start_p('sota', SENSE['sota'])[0]} L, {obj_start_p('sota', SENSE['sota'])[1]} = "
          f"{obj_head_v('sota', SENSE['sota'], 'L')}",
          f"{TOUCH_P} = {', '.join(seq_vi(TOUCH_P, OBJ_WORDS))}"]
    for kind, p in dict(OBJ_CL[k], d=d_obj_p(s)).items():
        L.append(f"[{kind}] {p} = {obj_cl_v(s, kind)}")
    L += [f"[ci, ^1-630] {OBJ_CL['jivhā']['ci']} = {obj_cl_v(SENSE['jivhā'], 'ci')}",
          f"{names_obj_p(s)} = {names_obj_v(s)}"]
    for p, v in OBJ_ABBR.items():
        L.append(f"{p} = {v}")
    L += ["", "## Words of the object lists", ""]
    for p, v in OBJ_WORDS.items():
        L.append(f"{p} = {v}")
    L += ["", "## Short definitions", ""]
    for p, v in SHORT.items():
        L.append(f"{p} = {v}")
    L += ["", "## The four- to eightfold statements", "", f"{DIT_P} = {DIT_V}"]
    for p, v in TOUCH_SUBJ.items():
        L.append(f"{p} (subject) = {v}")
    L.append(f"X Y-viññeyyaṃ rūpaṃ, … = X là {RUPA} mà Y có thể nhận biết; … (items joined with «; »)")
    L += ["", "## Headings and closing lines", ""]
    for p in ("##### Dukaniddeso", "Dukaniddeso.", "###### Upādābhājanīyaṃ", "Upādābhājanīyaṃ.",
              "Rūpakaṇḍe paṭhamabhāṇavāro.", "##### Tikaniddeso", "Tikaniddeso.", "Aṭṭhamabhāṇavāro.",
              "Rūpavibhatti.", "Rūpakaṇḍaṃ niṭṭhitaṃ."):
        L.append(f"{p} = {H[p]}")
    L += ["", "## Source slips (translated as written; punctuation and spacing rendered as meant)", ""]
    by_note = {}
    for sid, note in dict.fromkeys(SLIPS):
        by_note.setdefault(note, []).append(f"^{sid}")
    for note, sids in by_note.items():
        L.append(f"{', '.join(sids)}: {note}")
    L += ["^1-850: «dhoso» = the termbase's dhoso «tiếng nói» (same Vietnamese as ghoso)", "",
          "## Termbase notes", "",
          "loko (organ names): no entry; closest sibling lokiya «thuộc thế gian» = «thế gian»",
          "vatthuṃ (organ names): no entry; closest sibling vatthūni «chỗ dựa» (as 3-01) = «chỗ dựa»",
          "orimaṃ tīraṃ: tīraṃ «bờ» + orimaṃ (no entry) = «bờ bên này»",
          "passi / passati / passissati / passe: no entries = «đã thấy, đang thấy, sẽ thấy hoặc có thể thấy»; the "
          "optatives (passe, suṇe, ghāye, sāye, phuse, paṭihaññe, uppajje) = «có thể …»",
          "uppajjati «sinh khởi», paṭihaññati «đang va chạm» …: in the past / present / future / optative series "
          "the tense words are the point (APPROVED citation-form rule)",
          "ārabbha «lấy … làm» and -ārammaṇo «lấy … làm đối tượng» both give «lấy X làm đối tượng»; the place "
          "keeps them apart: ārabbha opens the clause («dựa vào mắt ấy và lấy hình sắc làm đối tượng, …»), "
          "-ārammaṇo follows its noun («sự tiếp xúc của mắt lấy hình sắc làm đối tượng»)",
          "Yaṃ cakkhu … pasādo (organ definitions) = «Mắt là chất nhạy cảm …»: the relative «Yaṃ» (termbase «điều») "
          "is not written there (no keyword in those segments); the object and short definitions keep «điều» / "
          "«Điều mà»",
          "dīghaṃ, rassaṃ, aṇuṃ, thūlaṃ, ninnaṃ, thalaṃ, asādu, telaṃ, janapade, santhambhanā, viññāpitattaṃ, "
          "kakkhaḷabhāvo: no entries = «dài, ngắn, nhỏ, to, chỗ trũng, chỗ cao, vị không ngon, dầu, vùng đất, "
          "sự căng cứng toàn diện, trạng thái đã làm cho biết, tính chất cứng»",
          "candamaṇḍalassa / sūriyamaṇḍalassa / ādāsamaṇḍalassa: canda «trăng», sūriya «mặt trời», ādāsa «gương» "
          "+ maṇḍalassa «vầng» = «vầng trăng», «vầng mặt trời», «vầng gương» (the termbase's «vầng» kept for the "
          "mirror too)",
          "itthattaṃ / itthibhāvo, purisattaṃ / purisabhāvo: itthi «nữ tính» / purisa «nam tính» + -tta, bhāvo "
          "«tính chất» = «trạng thái nữ tính, tính chất nữ tính» …; itthiliṅgaṃ etc. = «hình tướng nữ tính» …",
          "kusalacittassa vā … abyākatacittassa vā (intimation) = «khi có tâm thiện, tâm bất thiện hoặc tâm không xác "
          "định về mặt đạo đức»",
          "sukhasamphassaṃ / dukkhasamphassaṃ as nouns (tangibles) = «cái mà» + 3-01's «khi tiếp xúc thì dễ chịu / "
          "khó chịu»",
          "rūpaṃ in the object definitions = the visible form «hình sắc» (termbase second sense); in the questions, "
          "answers and «yaṃ vā panaññampi atthi rūpaṃ» lists = matter «vật chất»"]
    (HERE / "notes-3-02_3-03.md").write_text(unicodedata.normalize("NFC", "\n".join(L) + "\n"), encoding="utf-8",
                                             newline="\n")
    print("wrote", HERE / "notes-3-02_3-03.md")


def main():
    check_earlier_unchanged()
    for part in PARTS:
        text, n = build(part)
        (S.OUT / part).write_text(unicodedata.normalize("NFC", text), encoding="utf-8", newline="\n")
        print("wrote", S.OUT / part, n, "segments")
    notes()


if __name__ == "__main__":
    main()
