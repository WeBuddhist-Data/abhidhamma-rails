"""Pāli->Vietnamese keyword map, pi-6 chapter 10-02-indriyayamaka (Indriyayamaka: end of the paṇṇattivāra
(suddhindriyamūlacakka) and the pavattivāra, uppādavāra (1) paccuppanna), and the FRAME TABLES of the Indriyayamaka
attribute beings and citta kinds for the later chapters 10-03 … 10-13.

usage: python -I -X utf8 -B map_10-02_vi.py                  (writes 10-02-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-02_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-02_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Later Indriya chapters load it with importlib:

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\mapper-vi")
    J = importlib.import_module("map_10-02_vi")
    J.ATTR10         the attribute beings of the Indriyayamaka answers («Ở những người đang tái sinh có mắt và không phải
                     là người nữ …»): itthīnaṃ «người nữ», purisānaṃ «người nam», somanassena «có niềm vui đi kèm»,
                     upekkhāya «có sự bình thản đi kèm», sahetukānaṃ / ahetukānaṃ «có / không có gốc rễ»,
                     ñāṇasampayuttānaṃ / ñāṇavippayuttānaṃ «gắn liền / không gắn liền với hiểu biết», upapajjantīnaṃ
                     «đang tái sinh», tāsaṃ «người ấy» (+ proposals for 10-03 …: itthiyo, purisā, cavantīnaṃ, Itarāsaṃ)
    J.BEINGS_ATTR    ATTR10 + map_3-01_vi.ATTR (sacakkhukānaṃ «có mắt», asotakānaṃ «không có tai», sacittakānaṃ …)
    J.CITTA_MEMBER   somanassa «niềm vui», upekkhā «sự bình thản», saddhā «niềm tin», ñāṇa «hiểu biết» (domanassa
                     «nỗi buồn»: proposal)
    J.CITTA_ASSOC    sampayutta «gắn liền với», vippayutta «không gắn liền với»
    J.citta10(word)  <X>sampayutta / <X>vippayutta chains + citta(ssa / e / ṃ) -> «tâm gắn liền với niềm vui và không
                     gắn liền với niềm tin» (parts joined «và», Pāli order); cittassa alone «tâm»; None if not one
    J.moment10(kw, text)   «<citta> uppādakkhaṇe / bhaṅgakkhaṇe» -> «khoảnh khắc sinh khởi / tan rã của <tâm …>»
                     (map_8_vi.moment_value; the «vào» of the locative is frame)
    J.mulaka10(kw)   X-indriyamūlakaṃ -> «phần dựa trên năng lực X» (3-01 forms(): «(Phần dựa trên năng lực mắt)»)
    J.T10_02         this chapter's fixed values (ATTR10, pavatte «đời sống» = map_5-01_vi.PLANES5)
    J.value1002(kw, kws, vi, pi, table=None)
                     your table -> T10_02 -> map_10-01_vi.T10_01 -> mulaka10 -> moment10 -> map_10-01_vi.faculty_value
                     -> map_3-03_vi.value303 (3-02 accusative / ablative planes, 3-01 ATTR / PLANE_LOC / BEINGS_GEN with
                     the position and Itaresaṃ rules, map_2-01_vi.frames201: verbs through verb_value, planes,
                     persons, relatives) -> map_sample_vi.value6
Values are the words of the zero-shot translation as build_10-02_vi.py writes them (ATTR10, citta_kind); the
translation file is the truth, so every later chapter checks them against its segments (the presence check does).
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md, notes-map-10-01.md, notes-map-2-01.md, notes-map-3-01.md,
notes-map-3-03.md, notes-map-5-01.md, notes-map-8.md, notes-map-10-02.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from map_common_vi import (NDE, build_part, en, lc, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)

I = importlib.import_module("map_10-01_vi")        # the Indriyayamaka members (FACULTIES, faculty_value, T10_01)
A3 = importlib.import_module("map_3-01_vi")         # ATTR (sacakkhuka …), PLANE_LOC, BEINGS_GEN
A33 = importlib.import_module("map_3-03_vi")        # value303 (position rule + Itaresaṃ rule on top of 3-02 / 2-01)
T5 = importlib.import_module("map_5-01_vi")         # pavatte «đời sống», citta5; T5.C = map_8_vi (moments)
C = T5.C

PART = "10-02-indriyayamaka"

# ---------------------------------------------------------------------------- attribute beings (Indriyayamaka)
# «Ở những người đang tái sinh có mắt và không phải là người nữ, …»: «Ở» and the leading «những» are frame, «và»
# joins the attributes (3-01), the copula «là» of «là người nữ» is the predicate frame (pi-1 value form); a separate
# negator before the attribute (na itthīnaṃ «không phải là người nữ», vinā somanassena «không có niềm vui đi kèm»)
# keeps its own «không» / «không phải là»: the keyword takes the positive value (coordinator rule for a separate na).
# somanassena / upekkhāya: the instrumental «with joy» is rendered «có … đi kèm» and kept (as the instrumental
# Xmūlena «xét theo …», pi-6 conventions; pi-1 somanassasahagata «có niềm vui đi kèm»).
ATTR10 = {
    "itthīnaṃ": "người nữ", "purisānaṃ": "người nam",
    "somanassena": "có niềm vui đi kèm", "upekkhāya": "có sự bình thản đi kèm",
    "sahetukānaṃ": "có gốc rễ", "ahetukānaṃ": "không có gốc rễ",               # sample FORMULAS sahetukaṃ / Ahetukaṃ
    "ñāṇasampayuttānaṃ": "gắn liền với hiểu biết",                              # pi-1 ñāṇasampayutta
    "ñāṇavippayuttānaṃ": "không gắn liền với hiểu biết",                        # pi-1 ñāṇavippayuttaṃ
    "upapajjantīnaṃ": "đang tái sinh",              # feminine of upapajjantānaṃ (2-01 PERSONS); no gender in Vietnamese
    "tāsaṃ": "người ấy",                            # feminine of tesaṃ «ở những người ấy» (2-01 RELATIVES)
    # proposals for 10-03 … 10-13 (not keywords in 10-02; check against your segment)
    "cavantīnaṃ": "đang chết đi",                   # feminine of cavantānaṃ (2-01 PERSONS)
    "itarāsaṃ": "người khác",                       # feminine of itaresaṃ (2-01 PERSONS, «những người khác»)
    "itthiyo": "người nữ", "purisā": "người nam",   # nominative plural («những người nữ …»: «những» frame)
}
BEINGS_ATTR = {**A3.ATTR, **ATTR10}

# ---------------------------------------------------------------------------- citta kinds (pavatte … uppādakkhaṇe)
# «trong đời sống, vào khoảnh khắc sinh khởi của tâm gắn liền với niềm vui và không gắn liền với niềm tin»
# (build_10-02_vi citta_kind: pi-1 sampayutta «gắn liền với» / vippayutta «không gắn liền với»; parts joined «và» in
# the Pāli order, as map_5-01_vi.CITTA_KIND5)
CITTA_MEMBER = {
    "somanassa": "niềm vui", "upekkhā": "sự bình thản", "saddhā": "niềm tin", "ñāṇa": "hiểu biết",
    "domanassa": "nỗi buồn",                        # proposal (not in 10-02)
}
CITTA_ASSOC = {"sampayutta": "gắn liền với", "vippayutta": "không gắn liền với"}
_MEMBER_ORDER = sorted(CITTA_MEMBER, key=len, reverse=True)
_CITTA_ENDS = ("cittassa", "citte", "cittaṃ", "cittā", "citta")


def _kind_chain(pre):
    """«somanassasampayuttasaddhāvippayutta» -> «gắn liền với niềm vui và không gắn liền với niềm tin»; None if the
    prefix is not a chain of <member><sampayutta|vippayutta>."""
    parts = []
    while pre:
        for m in _MEMBER_ORDER:
            if pre.startswith(m):
                rest = pre[len(m):]
                for a, av in CITTA_ASSOC.items():
                    if rest.startswith(a):
                        parts.append(av + " " + CITTA_MEMBER[m])
                        pre = rest[len(a):]
                        break
                else:
                    return None
                break
        else:
            return None
    return " và ".join(parts) if parts else None


def citta10(word):
    """<chain>cittassa / -citte / -cittaṃ -> «tâm <chain>»; cittassa alone -> «tâm»; other kinds via
    map_5-01_vi.citta5 (map_8_vi.citta_value). None if not a citta word."""
    k = lc(word).lower()
    for e in _CITTA_ENDS:
        if k.endswith(e):
            pre = k[: -len(e)]
            if pre == "":
                return "tâm"
            v = _kind_chain(pre)
            if v:
                return "tâm " + v
            return T5.citta5(word)
    return None


def moment10(kw, text):
    """«<citta> uppādakkhaṇe / bhaṅgakkhaṇe» = «khoảnh khắc sinh khởi / tan rã của <tâm …>» (map_8_vi moments: «Vào»
    of the locative is frame). None if not such a two-word keyword."""
    words = kw.split()
    if len(words) != 2:
        return None
    m = C.moment_value(words[1], text)
    if not m:
        return None
    owner = citta10(words[0])
    return (m + " của " + owner) if owner else None


def mulaka10(kw):
    """(Cakkhundriyamūlakaṃ) «(Phần dựa trên năng lực mắt)» = phần dựa trên <faculty name> (3-01 forms() rule)."""
    k = lc(kw).lower()
    if not k.endswith("mūlakaṃ"):
        return None
    stem = k[: -len("mūlakaṃ")]
    if stem in I.FACULTY_NAME:
        return "phần dựa trên " + I.FACULTY_NAME[stem]
    return None


# ---------------------------------------------------------------------------- this chapter's fixed values
T10_02 = {
    **ATTR10,
    "pavatte": T5.PLANES5["pavatte"],               # «trong đời sống»: the locative «trong» is frame (5-01 / 9-01)
    "(no direct equivalent)": NDE,                  # the keyword-file placeholder (coordinator rule)
}


def value1002(kw, kws, vi, pi, table=None):
    """your table -> T10_02 -> T10_01 -> mulaka10 -> moment10 -> faculty_value -> map_3-03_vi.value303."""
    k = lc(kw).lower()
    if table:
        for x in (kw, lc(kw), k):
            if x in table:
                return table[x]
    if k in T10_02:
        return T10_02[k]
    if k in I.T10_01:
        return I.T10_01[k]
    v = mulaka10(kw)
    if v:
        return v
    v = moment10(kw, vi)
    if v:
        return v
    v = I.faculty_value(kw)
    if v is not None:
        return v
    return A33.value303(kw, kws, vi, pi)


# per-segment choices (none needed)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value1002(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(only_miss=False, part=PART):
    res, vi = resolver(part), read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            v = res(bid, kw, kws)
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v != NDE and not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        e = en(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  en:{e}" if e else "") + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi, with_pali=False, part=PART):
    res, vi, pi = resolver(part), read_vietnamese(part), read_pali(part)
    for i, (bid, kws) in enumerate(read_keywords(part)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            if with_pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"-- VI {vi.get(bid, '')}")
            out = []
            for kw in kws:
                v = res(bid, kw, kws)
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                out.append(f"{kw}={v}{flag}")
            print("   " + " | ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
