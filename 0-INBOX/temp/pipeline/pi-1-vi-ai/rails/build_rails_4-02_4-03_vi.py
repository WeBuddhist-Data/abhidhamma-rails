"""Builder for the Vietnamese rails translation of pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng», plain audience),
chapters 4-02 and 4-03 (the rest of the summary chapter: the flood, yoke, hindrance, misapprehension, clinging and
defilement clusters, the great intermediate and closing pairs ^1-1156 … ^1-1302, the Suttanta pairs ^1-1303 … ^1-1383).

Writes (only when run as a script):
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/4-02-nikkhepakandam.md
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/4-03-nikkhepakandam.md
  0-INBOX/temp/pipeline/pi-1-vi-ai/rails/notes-4-02_4-03.md

Every line is translated from the Pāli by fixed strings. The 4-01 builder (F, which loads 3-02/3-03 = Q, 3-01 = R,
2-05 = E, 2-04 = D, 2-01/2-02 = B and the approved sample S) is imported, never edited: its frames, answer pieces,
patterns, definition strings (lobha, dosa, moha, vicikicchā, diṭṭhi, māna, the ten views, the grounds of annoyance,
the identity-view and rites openings), names and runs are reused, and its tables get NEW keys only. Before and after
the extension, 2-01 … 3-03 and 4-01 are rebuilt in memory and must equal the finished files byte for byte.
The question and answer frames are 1-matika's (S.q_form / S.a_form with S.PREDS); the Suttanta item names come
verbatim from 1-matika (S.SUTTA_ITEMS). Unknown Pāli raises KeyError, so nothing is guessed silently.
Terms follow the locked termbase AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md
(+ pi-1-vi-ai/termbase/APPROVED.md). Translated fresh from the Pāli.

usage: python -I -X utf8 build_rails_4-02_4-03_vi.py
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

_spec = importlib.util.spec_from_file_location("build_rails_4_01_vi", HERE / "build_rails_4-01_vi.py")
F = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(F)        # importing writes nothing; F.Q = 3-02/3-03, F.R = 3-01, F.E, F.D, F.B
Q, R, E, D, B = F.Q, F.R, F.E, F.D, F.B

PARTS = ["4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"]
PART_401 = "4-01-nikkhepakandam.md"
cap = S.cap
PE, ELL, DASH = "…pe…", "…", "–"
P = S.PREDS
NAMES = S.NAMES
SNAP = {k: dict(getattr(F, k)) for k in ("FIXED", "STRS", "PRE", "NM", "H", "FIXED_SENT", "EXTRA", "TEHI",
                                         "BHUMI", "EXCL", "KH_LISTS", "INSTR")}


def slip(note):
    F.slip(note)


def add(table, key, value):
    """new keys only; an existing key must already carry the same value"""
    if key in table:
        assert table[key] == value, (key, table[key], value)
    table[key] = value


# =========================================================================================
# 1. Names (NM): «Ở đây, X là gì?», «đó được gọi là X», the runs
# =========================================================================================
NEW_NM = {
    # hindrances (termbase)
    "kāmacchandanīvaraṇaṃ": "chướng ngại ý muốn dục lạc",
    "byāpādanīvaraṇaṃ": "chướng ngại ác ý",
    "thinamiddhanīvaraṇaṃ": "chướng ngại uể oải và đờ đẫn",
    "uddhaccakukkuccanīvaraṇaṃ": "chướng ngại xao động và hối tiếc",
    "vicikicchānīvaraṇaṃ": "chướng ngại hoài nghi",
    "avijjānīvaraṇaṃ": "chướng ngại vô minh",
    "uddhaccanīvaraṇaṃ": "chướng ngại xao động",
    "kukkuccanīvaraṇaṃ": "chướng ngại hối tiếc",
    "thinaṃ": "sự uể oải", "middhaṃ": "sự đờ đẫn",
    "uddhaccaṃ": B.NAMES["uddhaccaṃ"], "kukkuccaṃ": "sự hối tiếc",
    # misapprehension, clinging, defilements (termbase)
    "diṭṭhiparāmāso": "sự hiểu sai lệch dưới dạng quan điểm",
    "kāmupādānaṃ": "sự bám víu vào dục lạc",
    "diṭṭhupādānaṃ": "sự bám víu vào quan điểm",
    "sīlabbatupādānaṃ": "sự bám víu vào giới hạnh và nghi thức",
    "attavādupādānaṃ": "sự bám víu vào học thuyết về tự ngã",
    "māno": "sự kiêu mạn", "diṭṭhi": "quan điểm",
    "ahirikaṃ": B.NAMES["ahirikaṃ"], "anottappaṃ": B.NAMES["anottappaṃ"],
}
assert NEW_NM["uddhaccaṃ"] == "sự xao động" and NEW_NM["ahirikaṃ"] == "sự không biết hổ thẹn"
# the Suttanta items: 1-matika verbatim (first letter lowered, the variant bracket dropped)
for _sid, _pair in S.SUTTA_ITEMS.items():
    for _p, _v in _pair:
        if _p.endswith("ñca"):
            _k = _p[:-3] + "ṃ"
        elif _p.endswith(" ca"):
            _k = _p[:-3]
        else:
            continue                                # «saṃvego ca saṃvejaniyesu …», «khaye ñāṇaṃ» … (own lines)
        if " " in _k and _k not in ("antavā diṭṭhi", "anantavā diṭṭhi", "indriyesu aguttadvāratā",
                                    "bhojane amattaññutā", "indriyesu guttadvāratā", "bhojane mattaññutā"):
            continue
        _v = re.sub(r" \[[^\]]*\]$", "", _v)
        NEW_NM[_k] = _v[0].lower() + _v[1:]
assert NEW_NM["nāmaṃ"] == "phần tinh thần" and NEW_NM["paṭisanthāro"] == "sự niềm nở tiếp đón"
assert NEW_NM["indriyesu aguttadvāratā"] == "sự không phòng hộ cửa các giác quan"
for _k, _v in NEW_NM.items():
    add(F.NM, _k, _v)
NM = F.NM

# the runs «X Y-ena Z ceva Z-sampayutto ca» (^1-1176, ^1-1231, ^1-1257): instrumental -> nominative
for _k in list(NEW_NM):
    if _k.endswith("nīvaraṇaṃ") or _k.endswith("upādānaṃ"):
        add(F.INSTR, _k[:-2] + "ena", _k)
for _i, _n in {"mānena": "māno", "diṭṭhiyā": "diṭṭhi", "vicikicchāya": "vicikicchā", "thinena": "thinaṃ",
               "uddhaccena": "uddhaccaṃ", "ahirikena": "ahirikaṃ", "anottappena": "anottappaṃ"}.items():
    add(F.INSTR, _i, _n)
RUN_SG = {   # singular Pāli predicate of a run item -> the plural matrix name (its Vietnamese, P)
    "nīvaraṇañceva nīvaraṇasampayuttañca": "nīvaraṇā ceva nīvaraṇasampayuttā ca",
    "upādānañceva upādānasampayuttañca": "upādānā ceva upādānasampayuttā ca",
    "kileso ceva kilesasampayutto ca": "kilesā ceva kilesasampayuttā ca",
    "kileso ceva kilesasampayuttā ca": "kilesā ceva kilesasampayuttā ca",     # diṭṭhi, vicikicchā (feminine)
    "kileso ceva kilesasampayuttañca": "kilesā ceva kilesasampayuttā ca",     # thinaṃ, uddhaccaṃ … (neuter)
}

# =========================================================================================
# 2. Pieces of the answers
# =========================================================================================
KH3V = f"{B.NAMES['vedanākkhandho']}, {B.NAMES['saññākkhandho']} và {B.NAMES['saṅkhārakkhandho']}"
assert KH3V == "khối cảm giác, khối tri giác và khối tạo tác"
add(F.KH_LISTS, "vedanākkhandho, saññākkhandho, saṅkhārakkhandho", KH3V)
add(F.KH_LISTS, "vedanākkhandho …pe… viññāṇakkhandho", F.KH4_PE)    # ^1-1246, ^1-1267: a space before …pe…
TBL = dict(R.MATTER_NOUN)                            # item table for the …pe… ranges
TBL.update({"manāyatanaṃ": B.NAMES["manāyatanaṃ"], "dhammāyatanaṃ": B.NAMES["dhammāyatanaṃ"]})
VINN6 = ["cakkhuviññāṇaṃ", "sotaviññāṇaṃ", "ghānaviññāṇaṃ", "jivhāviññāṇaṃ", "kāyaviññāṇaṃ"]
VINN6_V = ["thức qua mắt", "thức qua tai", "thức qua mũi", "thức qua lưỡi", "thức qua thân"]   # termbase
CITTA_LIST_P = cap(", ".join(VINN6 + ["manodhātu", "manoviññāṇadhātu"]))
CITTA_LIST_V = ", ".join(VINN6_V + ["yếu tố ý", B.NAMES["manoviññāṇadhātu"]])
CITTAJA_P = ("yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ rūpāyatanaṃ saddāyatanaṃ "
             "gandhāyatanaṃ rasāyatanaṃ phoṭṭhabbāyatanaṃ ākāsadhātu āpodhātu rūpassa lahutā rūpassa mudutā "
             "rūpassa kammaññatā rūpassa upacayo rūpassa santati kabaḷīkāro āhāro")
CITTAJA_V = (f"{Q.OTHER} {Q.CITTAJA}: " +
             Q.items_vi(CITTAJA_P.split(f"{Q.QUAL_P[1][0]} ", 1)[1]))   # as ^1-666 «hoặc còn có bất cứ …: …»
VINNATTI2 = f"{R.MATTER_NOUN['kāyaviññatti']}, {R.MATTER_NOUN['vacīviññatti']}"
MAGGA = "con đường"
WISDOM_IN = "trí tuệ trong"
DUCC = {"kāya": "bằng thân", "vacī": "bằng lời nói", "mano": "bằng ý"}   # as kāyakammaṃ «nghiệp bằng thân» …
NAMING_P = ("Yā tesaṃ tesaṃ dhammānaṃ saṅkhā samaññā paññatti vohāro nāmaṃ nāmakammaṃ nāmadheyyaṃ nirutti "
            "byañjanaṃ abhilāpo")
NAMING_V = (f"{S.REL} là sự định danh, danh xưng chung, khái niệm, cách gọi thông thường, tên, sự đặt tên, "
            "danh hiệu, cách diễn đạt, từ ngữ, lời diễn tả của từng hiện tượng ấy")
CC = F.CITTACETASIKA
WHO3 = ("của người đã chứng nhập, hoặc của người đã tái sinh, hoặc của người an trú trong hạnh phúc ngay trong "
        "đời này")                                   # samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā
assert E.DDSV_V == "để an trú trong hạnh phúc ngay trong đời này"
IN_RANGE = "những điều trong khoảng giữa ấy thuộc cõi này, nằm trong cõi này"   # yaṃ «điều» etasmiṃ antare …
SPH_BODY = {
    ("Heṭṭhato avicinirayaṃ pariyantaṃ karitvā, uparito paranimmitavasavattī deve [paranimmitavasavattideve "
     "(sī. ka.)] anto karitvā, yaṃ etasmiṃ antare etthāvacarā ettha pariyāpannā khandhadhātu āyatanā, rūpaṃ "
     "vedanā saññā saṅkhārā viññāṇaṃ"):
        ("Lấy địa ngục Vô Gián ở bên dưới làm giới hạn, bao gồm cả chư thiên Tha Hóa Tự Tại "
         f"{S.spell('Sī., Ka.', 'paranimmitavasavattideve')} ở bên trên, {IN_RANGE}: các khối, các yếu tố và "
         f"các lĩnh vực nhận biết, tức {F.FIVE_V}"),
    ("Heṭṭhato brahmalokaṃ pariyantaṃ karitvā, uparito akaniṭṭhe deve [akaniṭṭhadeve (sī. ka.)] anto karitvā, "
     "yaṃ etasmiṃ antare etthāvacarā ettha pariyāpannā samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa "
     "[diṭṭhadhammasukhavihārassa (ka.)] vā cittacetasikā dhammā"):
        ("Lấy cõi Phạm Thiên ở bên dưới làm giới hạn, bao gồm cả chư thiên Sắc Cứu Cánh "
         f"{S.spell('Sī., Ka.', 'akaniṭṭhadeve')} ở bên trên, {IN_RANGE}: {CC} "
         f"{WHO3} {S.reading('Ka.', 'diṭṭhadhammasukhavihārassa')}"),
    ("Heṭṭhato ākāsānañcāyatanupage deve pariyantaṃ karitvā, uparito nevasaññānāsaññāyatanupage deve anto "
     "karitvā, yaṃ etasmiṃ antare etthāvacarā ettha pariyāpannā samāpannassa vā upapannassa vā "
     "diṭṭhadhammasukhavihārissa vā cittacetasikā dhammā"):
        (f"Lấy chư thiên sinh vào {B.ARUPA['ākāsānañcāyatana']} ở bên dưới làm giới hạn, bao gồm cả chư thiên "
         f"sinh vào {B.ARUPA['nevasaññānāsaññāyatana']} ở bên trên, {IN_RANGE}: {CC} {WHO3}"),
}
NEW_FIXED = {
    "Sabbañca rūpaṃ, asaṅkhatā ca dhātu": F.FIXED["sabbañca rūpaṃ, asaṅkhatā ca dhātu"],
    CITTA_LIST_P: ("x", CITTA_LIST_V),
    "Cittañca": ("x", B.NAMES["cittaṃ"] if "cittaṃ" in B.NAMES else "tâm"),
    "avasesañca rūpaṃ": ("x", f"{R.RUPA} {F.REMAINING}"),
    "kāyaviññatti, vacīviññatti": ("x", VINNATTI2),
    "kāyaviññatti vacīviññatti": ("x", VINNATTI2),
    CITTAJA_P: ("x", CITTAJA_V),
    "Cakkhāyatanaṃ…pe… manāyatanaṃ": ("x", f"{TBL['cakkhāyatanaṃ']}{ELL} {TBL['manāyatanaṃ']}"),
    "Rūpāyatanaṃ…pe… dhammāyatanaṃ": ("x", f"{TBL['rūpāyatanaṃ']}{ELL} {TBL['dhammāyatanaṃ']}"),
    "Cakkhāyatanaṃ…pe… kabaḷīkāro āhāro": ("x", f"{TBL['cakkhāyatanaṃ']}{ELL} {TBL['kabaḷīkāro āhāro']}"),
    "cattāro ca mahābhūtā": ("x", f"bốn {R.MATTER_NOUN['mahābhūtaṃ']}"),
    "apariyāpannā maggā ca, maggaphalāni ca, asaṅkhatā ca dhātu": ("x", F.PATHS),
    "Maggā ca, maggaphalāni ca, asaṅkhatā ca dhātu": ("x", f"các {MAGGA}, các thành quả của {MAGGA} và "
                                                            f"{F.ASANKHATA}"),
    "vitakko ca": ("x", S.FN["vitakko"]), "vicāro ca": ("x", S.FN["vicāro"]), "pīti ca": ("x", S.FN["pīti"]),
    "sukhañca": ("x", S.FN["sukhaṃ"]), "upekkhā ca": ("x", B.NAMES["upekkhā"]),
    "Pañca kammāni ānantarikāni, yā ca micchādiṭṭhi niyatā":
        F.FIXED["Pañca kammāni ānantarikāni, yā ca micchādiṭṭhiniyatā"],
    "cattāro maggā apariyāpannā": F.FIXED["Cattāro maggā apariyāpannā"],
    "Tīṇi akusalamūlāni lobho, doso, moho": ("x", f"ba gốc rễ bất thiện: {F.ROOTS_A}"),   # ^1-1301: no dash
    "Avaseso lobho doso moho": F.FIXED["Avaseso lobho, doso, moho"],
    "Tadekaṭṭho lobho doso moho": F.FIXED["Tadekaṭṭho lobho, doso, moho"],
    "taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ manokammaṃ": F.FIXED["taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ, "
                                                                "manokammaṃ"],
    "Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ":
        F.FIXED["Cattāro ca mahābhūtā catunnañca mahābhūtānaṃ upādāya rūpaṃ"],
    # the Suttanta pairs
    "Vijjāya sampayuttakā dhammā": ("x", "những hiện tượng gắn liền với hiểu biết chân thật"),
    "Avijjāya sampayuttakā dhammā": ("x", "những hiện tượng gắn liền với vô minh"),
    "Heṭṭhimesu tīsu ariyamaggesu paññā": ("x", f"{WISDOM_IN} ba {MAGGA} cao quý thấp hơn"),
    "Upariṭṭhime arahattamagge paññā": ("x", f"{WISDOM_IN} {MAGGA} A-la-hán cao nhất"),
    "Ahirīkañca anottappañca": ("x", f"{B.NAMES['ahirikaṃ']} và {B.NAMES['anottappaṃ']}"),
    "Hirī ca ottappañca": ("x", f"{S.FN['hirī']} và {S.FN['ottappaṃ']}"),
    "Kāyaduccaritaṃ, vacīduccaritaṃ, manoduccaritaṃ": ("x", ", ".join(f"hành vi xấu {v}" for v in DUCC.values())),
    "Kāyasucaritaṃ, vacīsucaritaṃ, manosucaritaṃ": ("x", ", ".join(f"hành vi tốt {v}" for v in DUCC.values())),
    NAMING_P: ("x", NAMING_V),
}
for _p, _v in SPH_BODY.items():
    NEW_FIXED[_p] = ("x", _v)
for _k, _v in NEW_FIXED.items():
    add(F.FIXED, _k, _v)
SLIP_PIECES = {
    "taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ manokammaṃ": "no comma between «vacīkammaṃ» and «manokammaṃ»: "
                                                        "the same Vietnamese as the parallels",
    "Tīṇi akusalamūlāni lobho, doso, moho": "no dash after «Tīṇi akusalamūlāni» (^1-1249 has one): «:» "
                                            "(the dash rule allows no added dash)",
}

# Tehi dhammehi ye dhammā Y (the clusters of this chapter)
for _y in ("nīvaraṇiyā", "upādāniyā", "saṃkilesikā"):
    add(F.TEHI, _y, f"là đối tượng của {F.THOSE}")
add(F.TEHI, "parāmaṭṭhā", f"bị {F.THOSE} nắm giữ")              # 1-matika «bị sự hiểu sai lệch nắm giữ»
add(F.TEHI, "saṃkiliṭṭhā", f"bị {F.THOSE} làm vẩn đục")         # 1-matika «bị phiền não làm vẩn đục»

# the bhūmi phrases of the closing pairs (^1-1275 … ^1-1286)
NEW_BHUMI = {
    ("Savitakka", "vitakkaṃ"): P["savitakkā"], ("Avitakka", None): P["avitakkā"],
    ("Savicāra", "vicāraṃ"): P["savicārā"], ("Avicāra", None): P["avicārā"],
    ("Sappītika", "pītiṃ"): P["sappītikā"], ("Appītika", None): P["appītikā"],
}
for _k, _v in NEW_BHUMI.items():
    add(F.BHUMI, _k, _v)
add(F.EXCL, "vitakkaṃ", S.FN["vitakko"])
BHUMI_NA = {"pīti": F.BHUMI[("Pīti", "pītiṃ")], "sukha": F.BHUMI[("Sukha", "sukhaṃ")],
            "upekkhā": F.BHUMI[("Upekkhā", "upekkhaṃ")]}   # Na X-bhūmiyaṃ = «không ở cấp độ có X»


# =========================================================================================
# 3. Patterns: the 4-01 list, with wider alternatives and three new kinds
# =========================================================================================
def _pat(kind):
    return [i for i, (k, _) in enumerate(F.PAT) if k == kind][0]


F.KHALT = "|".join(re.escape(k) for k in sorted(F.KH_LISTS, key=len, reverse=True))
F.PAT[_pat("kh")] = ("kh", re.compile(rf"(?P<tam>[Tt]aṃsampayutto )?(?P<kh>(?i:{F.KHALT}))"))
F.PAT[_pat("tp")] = ("tp", re.compile(
    rf"Tehi dhammehi ye dhammā (?P<y>sāsavā|saṃyojaniyā|ganthaniyā|nīvaraṇiyā|parāmaṭṭhā|upādāniyā|saṃkilesikā), "
    rf"te dhamme ṭhapetvā avasesā (?P<sas>sāsavā )(?P<q>{F.QW}) dhammā (?P<sph>{F.SPH})"))
F.PAT[_pat("tehi")] = ("tehi", re.compile(
    r"Tehi dhammehi ye dhammā (?P<y>na hetū sahetukā|na hetū ahetukā|sahetukā|ahetukā|sampayuttā|vippayuttā|"
    r"saṃkiliṭṭhā)(?P<ex>,? te dhamme ṭhapetvā)?"))
RUN_RE = re.compile(r"(?P<a>\S+) (?P<b>\S+) (?P<z>" + "|".join(re.escape(z) for z in RUN_SG) + r")(?=,| –|$)")
F.PAT.insert(0, ("run", RUN_RE))
F.PAT.append(("nabhumi", re.compile(rf"Na (?P<b>\S+?)bhūmiyaṃ (?P<sph>{F.SPH})")))
F.PAT.append(("sphonly", re.compile(rf"(?P<sph>{F.SPH})$")))
_PIECE_ORIG = F.piece_vi


def piece_vi(kind, m):
    g = m.groupdict()
    if kind == "run":
        a = g["a"][0].lower() + g["a"][1:]
        return "x", f"{NM[a]}, {F.REL_TO} {NM[F.INSTR[g['b']]]}, {P[RUN_SG[g['z']]]}"
    if kind == "nabhumi":
        return "desc", f"không {F.LEVEL} {BHUMI_NA[g['b']]}, {F.sph_vi(g['sph'])}"
    if kind == "sphonly":
        return "x", f"những hiện tượng {F.sph_vi(g['sph'])}"
    return _PIECE_ORIG(kind, m)


F.piece_vi = piece_vi
_SPH_ORIG = F.sph_vi


def sph_vi(text):
    """the locative lists of the bhūmi phrases are written without commas throughout: no slip for those"""
    if text.split()[0].endswith("e"):
        n = len(F.SLIPS)
        out = _SPH_ORIG(text)
        del F.SLIPS[n:]
        return out
    return _SPH_ORIG(text)


F.sph_vi = sph_vi
F.FIXED_KEYS = sorted(F.FIXED, key=len, reverse=True)
_BODY_ORIG = F.body_vi


def body_vi(b):
    for k, note in SLIP_PIECES.items():
        if k in b:
            slip(note)
    if " …pe…" in b:
        slip("a space before «…pe…»: rendered as the parallels")
    return _BODY_ORIG(b)


F.body_vi = body_vi

# =========================================================================================
# 4. Definition strings (after «Điều mà [thuộc loại như vậy] là»; a value starting «,» carries its own frame)
# =========================================================================================
PANNA_ABBR_P = "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi"
PANNA_ABBR = B.S_PANNA_ABBR                          # trí tuệ, sự hiểu rõ… sự không si mê, …, quan điểm đúng đắn
assert B.STR[PANNA_ABBR_P] == PANNA_ABBR
HERE_IS = ", ở đây, là"                              # yā tattha S (tattha «ở đây»)
DITTHI_ITEMS = F.DITTHI_V0.split(", ")
MOHA_ITEMS = D.MOHA_V.split(", ")
SATI_ITEMS = S.S_SATI.split(", ")
KAMMA_KAYA = "sự không vi phạm bằng thân, sự không vi phạm bằng lời nói, sự không vi phạm bằng thân và lời nói"
NEW_STRS = {
    # thina, middha, kukkucca (termbase); uddhacca comes from 2-04 (B.STR)
    "cittassa akallatā akammaññatā olīyanā sallīyanā līnaṃ līyanā līyitattaṃ thinaṃ thiyanā thiyitattaṃ cittassa":
        ("sự không khỏe khoắn của tâm, sự không dễ vận dụng, sự chùng xuống, sự chùng xuống hoàn toàn, sự co rút, "
         "sự khởi co rút, trạng thái khởi co rút, sự uể oải, sự khởi uể oải, trạng thái khởi uể oải của tâm"),
    ("kāyassa akallatā akammaññatā onāho pariyonāho antosamorodho middhaṃ soppaṃ pacalāyikā soppaṃ supanā "
     "supitattaṃ"):
        ("sự không khỏe khoắn của thân tinh thần, sự không dễ vận dụng, sự bao phủ, sự bao phủ hoàn toàn, "
         "sự bế tắc bên trong, sự đờ đẫn, giấc ngủ, sự gà gật, giấc ngủ, sự ngủ, trạng thái đã ngủ"),
    "kukkuccaṃ kukkuccāyanā kukkuccāyitattaṃ cetaso vippaṭisāro manovilekho":
        "sự hối tiếc, sự khởi hối tiếc, trạng thái khởi hối tiếc, sự ân hận của tâm, sự giằng xé của ý",
    D.VICIKICCHA_P.replace("saṃsayo anekaṃsaggāho", "saṃsayo, anekaṃsaggāho"): D.VICIKICCHA_V,
    "māno maññanā maññitattaṃ unnati unnamo dhajo sampaggāho ketukamyatā cittassa":
        F.STRS["māno maññanā maññitattaṃ unnati unnamo [uṇṇati uṇṇāmo (syā.)] dhajo sampaggāho ketukamyatā "
               "cittassa"].replace(" " + S.spell("Syā.", "uṇṇati uṇṇāmo"), ""),
    "hirīyati hiriyitabbena, hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": S.HIRI_S,
    "ottappati ottappitabbena, ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": S.OTTAPPA_S,
    "na hirīyati hiriyitabbena, na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": D.HIRI_NEG_V,
    "na ottappati ottappitabbena, na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": D.OTTAPPA_NEG_V,
    # the abbreviated strings
    "diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho": f"{DITTHI_ITEMS[0]}, {DITTHI_ITEMS[1]}{ELL} {DITTHI_ITEMS[-1]}",
    "aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusalamūlaṃ":
        f"{MOHA_ITEMS[0]}, {MOHA_ITEMS[1]}{ELL} {', '.join(MOHA_ITEMS[-3:])}",
    "cittassa ṭhiti…pe… sammāsamādhi": f"{B.STR['cittassa ṭhiti']}{ELL} {S.FN['sammāsamādhi']}",
    "cetasiko vīriyārambho…pe… sammāvāyāmo": f"{S.S_VIRIYA.split(', ')[0]}{ELL} {S.FN['sammāvāyāmo']}",
    "bhavesu bhavachando…pe… bhavajjhosānaṃ":
        (lambda v: v.split(", là ")[0] + ", là " + v.split(", là ")[1].split(", ")[0] + ELL + " " +
         v.split(", ")[-1])(F.STRS[F.kama_bhava("bhava")[0]]),
    # the Suttanta strings
    ("tesaṃ sevanā nisevanā saṃsevanā bhajanā sambhajanā bhatti sambhatti taṃsampavaṅkatā"):
        ("sự giao du với họ, sự thường xuyên giao du, sự giao du mật thiết, sự gần gũi, sự gần gũi mật thiết, "
         "sự gắn bó, sự gắn bó mật thiết, sự nghiêng về phía họ"),
    f"tāsaṃ āpattīnaṃ āpattikusalatā {PANNA_ABBR_P}": f"sự thành thạo về các lỗi vi phạm ấy, {PANNA_ABBR}",
    f"tāhi āpattīhi vuṭṭhānakusalatā {PANNA_ABBR_P}":
        f"sự thành thạo về việc ra khỏi các lỗi vi phạm ấy, {PANNA_ABBR}",
    f"tāsaṃ samāpattīnaṃ samāpattikusalatā {PANNA_ABBR_P}":
        f"sự thành thạo về các thành tựu thiền ấy, {PANNA_ABBR}",
    f"tāhi samāpattīhi vuṭṭhānakusalatā {PANNA_ABBR_P}":
        f"sự thành thạo về việc xuất khỏi các thành tựu thiền ấy, {PANNA_ABBR}",
    f"tāsaṃ dhātūnaṃ dhātukusalatā {PANNA_ABBR_P}": f"sự thành thạo về các yếu tố ấy, {PANNA_ABBR}",
    f"tāsaṃ dhātūnaṃ manasikārakusalatā {PANNA_ABBR_P}":
        f"sự thành thạo về sự chú tâm đến các yếu tố ấy, {PANNA_ABBR}",
    f"tesaṃ āyatanānaṃ āyatanakusalatā {PANNA_ABBR_P}":
        f"sự thành thạo về các lĩnh vực nhận biết ấy, {PANNA_ABBR}",
    f"tattha {PANNA_ABBR_P}": f"{HERE_IS} {PANNA_ABBR}",
    "ajjavatā ajimhatā avaṅkatā akuṭilatā": "tính ngay thật, sự không quanh co, sự không cong queo, sự không vặn vẹo",
    "mudutā maddavatā akakkhaḷatā akathinatā nīcacittatā": f"{S.S_MUDUTA}, sự khiêm nhường của tâm",
    "khanti khamanatā adhivāsanatā acaṇḍikkaṃ anasuropo attamanatā cittassa":
        "sự nhẫn nại, sự bao dung, sự chịu đựng, sự không hung dữ, sự không thô lỗ, sự hài lòng của tâm",
    "kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo": KAMMA_KAYA,
    "kāyiko vītikkamo, vācasiko vītikkamo, kāyikavācasiko vītikkamo": KAMMA_KAYA.replace("sự không vi phạm",
                                                                                         "sự vi phạm"),
    "imesaṃ channaṃ indriyānaṃ agutti agopanā anārakkho asaṃvaro":
        "sự không canh giữ, sự không bảo vệ, sự không che chở, sự không thu thúc đối với sáu năng lực này",
    "imesaṃ channaṃ indriyānaṃ gutti gopanā ārakkho saṃvaro":
        "sự canh giữ, sự bảo vệ, sự che chở, sự thu thúc đối với sáu năng lực này",
    "tattha asantuṭṭhitā amattaññutā appaṭisaṅkhā bhojane":
        f"{HERE_IS} sự không biết đủ, sự không biết tiết độ, sự không suy xét trong ăn uống",
    "tattha santuṭṭhitā mattaññutā paṭisaṅkhā bhojane":
        f"{HERE_IS} sự biết đủ, sự biết tiết độ, sự suy xét trong ăn uống",
    "asati ananussati appaṭissati asati asaraṇatā adhāraṇatā pilāpanatā sammusanatā":
        ", ".join(["sự không tỉnh thức", "sự không nhớ lại", "sự không hồi tưởng", "sự không tỉnh thức",
                   "sự không ghi nhớ", "sự không gìn giữ trong trí nhớ", "sự hời hợt", "sự quên lãng"]),
    ("sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammusanatā sati satindriyaṃ satibalaṃ "
     "sammāsati"): S.S_SATI,                         # ch. 2 «asammussanatā»: one word, the same Vietnamese
    "kusalānaṃ dhammānaṃ āsevanā bhāvanā bahulīkammaṃ":
        "sự thực hành, sự tu tập, sự làm đi làm lại các hiện tượng thiện",
}
assert NEW_STRS["bhavesu bhavachando…pe… bhavajjhosānaṃ"] == (
    ", đối với sự hiện hữu, là ý muốn hiện hữu… sự đắm chìm trong hiện hữu")
assert NEW_STRS["diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho"] == (
    "quan điểm, sự mắc kẹt trong các quan điểm… sự nắm giữ điều đảo ngược")
assert NEW_STRS["aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusalamūlaṃ"] == (
    "sự không biết, sự không thấy… then cài vô minh, sự si mê, tức gốc rễ bất thiện")
assert NEW_STRS["cetasiko vīriyārambho…pe… sammāvāyāmo"] == "sự khởi động tinh tấn trong tâm… nỗ lực đúng đắn"
assert NEW_STRS["cittassa ṭhiti…pe… sammāsamādhi"] == "sự ổn định của tâm… định tâm đúng đắn"
assert SATI_ITEMS[6:8] == ["sự không hời hợt", "sự không quên lãng"]
for _k, _v in NEW_STRS.items():
    add(F.STRS, _k, _v)
SLIP_STRS = {
    D.VICIKICCHA_P.replace("saṃsayo anekaṃsaggāho", "saṃsayo, anekaṃsaggāho"):
        "a comma inside the doubt string («saṃsayo, anekaṃsaggāho»): the same Vietnamese",
}

# =========================================================================================
# 5. Openings before «Yo/Yā/Yaṃ …» (Pāli without its final mark -> Vietnamese without its final mark)
# =========================================================================================
SAK_FIRST_P = F.SAKKAYA_P.split(". ")[0]
SAK_FIRST_V = F.SAKKAYA_V.split(". ")[0]
SAK_ABBR_P = (f"{SAK_FIRST_P}. Vedanaṃ…pe… saññaṃ…pe… saṅkhāre…pe… viññāṇaṃ attato samanupassati, "
              "viññāṇavantaṃ vā attānaṃ, attani vā viññāṇaṃ, viññāṇasmiṃ vā attānaṃ")
_AGG = [a[4] for a in F.AGG]                         # vật chất, cảm giác, tri giác, các sự tạo tác, thức
SAK_ABBR_V = (f"{SAK_FIRST_V}. Xem {_AGG[1]}{ELL} {_AGG[2]}{ELL} {_AGG[3]}{ELL} {_AGG[4]} là {F.SELF}, "
              f"hoặc {F.SELF} có {_AGG[4]}, hoặc {_AGG[4]} ở trong {F.SELF}, hoặc {F.SELF} ở trong {_AGG[4]}")
assert SAK_FIRST_V.endswith("hoặc tự ngã ở trong vật chất")
GROUNDS_SEMI_P = F.GROUNDS_P.replace("caratīti āghāto jāyati, anatthaṃ me carissatīti",
                                     "caratīti āghāto jāyati; anatthaṃ me carissatīti", 1).replace(
    "carissatīti āghāto jāyati, piyassa", "carissatīti āghāto jāyati; piyassa", 1)
GROUNDS_SEMI_V = F.GROUNDS_V.replace("đang gây hại cho tôi”, ", "đang gây hại cho tôi”; ", 1).replace(
    "sẽ gây hại cho tôi”, ", "sẽ gây hại cho tôi”; ", 1)
assert GROUNDS_SEMI_V.count("”; ") == 2
assert GROUNDS_SEMI_P != F.GROUNDS_P and GROUNDS_SEMI_V != F.GROUNDS_V
WORLD = "thế gian"                                   # loko (3-02, 4-01)


def wrong_view(neg):
    """Natthi dinnaṃ … pavedentīti (neg) / Atthi dinnaṃ … (not neg)"""
    n = "không có" if neg else "có"                  # natthi «không có», atthi «có» (termbase)
    items = ["sự bố thí", "sự cúng tế", "sự cúng dường", "quả và kết quả của các nghiệp làm tốt và làm xấu",
             f"{WORLD} này", f"{WORLD} khác", "mẹ", "cha", "chúng sinh hóa sinh",
             f"các sa-môn và bà-la-môn trong {WORLD} đã đi đúng đắn{{V}}, thực hành đúng đắn, những người đã tự mình "
             f"hiểu biết trực tiếp, chứng nghiệm {WORLD} này và {WORLD} khác rồi tuyên bố"]
    return "“" + cap(", ".join(f"{n} {i}" for i in items)) + "”"


def wv_p(neg, var="", comma=","):
    n = "natthi" if neg else "atthi"
    return (cap(f"{n} dinnaṃ, {n} yiṭṭhaṃ, {n} hutaṃ, {n} sukatadukkaṭānaṃ kammānaṃ phalaṃ vipāko, {n} ayaṃ loko, "
                f"{n} paro loko, {n} mātā, {n} pitā, {n} sattā opapātikā, {n} loke samaṇabrāhmaṇā sammaggatā{var} "
                f"sammāpaṭipannā{comma} ye imañca lokaṃ parañca lokaṃ sayaṃ abhiññā sacchikatvā pavedentīti"))


VIEW_SELF = {   # X attā ca loko cāti
    "Bhavissati": "sẽ tồn tại", "Na bhavissati": "sẽ không tồn tại", "Sassato": "là trường tồn",
    "Ucchijjissati": "sẽ bị đoạn diệt", "Antavā": "là hữu hạn", "Anantavā": "là vô hạn",
}
DHATU18 = [("cakkhu", "mắt", "hình sắc", "rūpa"), ("sota", "tai", "âm thanh", "sadda"),
           ("ghāna", "mũi", "mùi", "gandha"), ("jivhā", "lưỡi", "vị", "rasa"), ("kāya", "thân", "vật xúc chạm",
                                                                                "phoṭṭhabba")]
DHATU18_P = ("Aṭṭhārasa dhātuyo " + ", ".join(f"{a}dhātu {d}dhātu {a}viññāṇadhātu" for a, _, _, d in DHATU18) +
             ", manodhātu dhammadhātu manoviññāṇadhātu")
DHATU18_V = ("Mười tám yếu tố: " + "; ".join(f"yếu tố {b}, yếu tố {c}, yếu tố thức qua {b}" for _, b, c, _ in DHATU18) +
             f"; yếu tố ý, {B.NAMES['dhammadhātu']}, {B.NAMES['manoviññāṇadhātu']}")
AYAT12 = ["cakkhāyatanaṃ", "rūpāyatanaṃ", "sotāyatanaṃ", "saddāyatanaṃ", "ghānāyatanaṃ", "gandhāyatanaṃ",
          "jivhāyatanaṃ", "rasāyatanaṃ", "kāyāyatanaṃ", "phoṭṭhabbāyatanaṃ", "manāyatanaṃ", "dhammāyatanaṃ"]
PS_LINKS = [("Avijjā", "vô minh"), ("saṅkhārā", "các sự tạo tác"), ("viññāṇaṃ", "thức"),
            ("nāmarūpaṃ", "phần tinh thần và vật chất"), ("saḷāyatanaṃ", "sáu lĩnh vực nhận biết"),
            ("phasso", "sự tiếp xúc"), ("vedanā", "cảm giác"), ("taṇhā", "khao khát"), ("upādānaṃ", "sự bám víu"),
            ("bhavo", "sự hiện hữu"), ("jāti", "sự sinh")]
PS_P = ("Avijjāpaccayā saṅkhārā, saṅkhārapaccayā viññāṇaṃ, viññāṇapaccayā nāmarūpaṃ, nāmarūpapaccayā saḷāyatanaṃ, "
        "saḷāyatanapaccayā phasso, phassapaccayā vedanā, vedanāpaccayā taṇhā, taṇhāpaccayā upādānaṃ, "
        "upādānapaccayā bhavo, bhavapaccayā jāti, jātipaccayā jarāmaraṇaṃ sokaparidevadukkhadomanassupāyāsā "
        "sambhavanti; evametassa kevalassa dukkhakkhandhassa samudayo hotīti")
COND = "làm điều kiện cho"                           # X-paccayā (termbase paccayā «làm điều kiện cho»)
PS_V = ("“" + cap(", ".join(f"{a} {COND} {b}" for (_, a), (_, b) in zip(PS_LINKS, PS_LINKS[1:]))) +
        f", sự sinh {COND} sự lão hóa và sự chết, sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng "
        "sinh khởi; như vậy là sự phát sinh của toàn bộ khối khổ đau này”")
INDR = [("Sotena saddaṃ sutvā", "khi nghe âm thanh bằng tai"), ("ghānena gandhaṃ ghāyitvā", "khi ngửi mùi bằng mũi"),
        ("jivhāya rasaṃ sāyitvā", "khi nếm vị bằng lưỡi"),
        ("kāyena phoṭṭhabbaṃ phusitvā", "khi chạm vật xúc chạm bằng thân")]
BAD = "các hiện tượng xấu ác bất thiện"            # pāpakā akusalā dhammā (as S.HIRI_S «… xấu ác bất thiện …»)
assert BAD in S.HIRI_S
INVADE = f"thì {BAD} là sự thèm muốn và nỗi buồn có thể tràn vào người ấy"


def guard(neg):
    """indriyesu (a)guttadvāratā: the opening (^1-1352 / ^1-1354)"""
    nh, nn = ("", "") if neg else ("na ", "na ")
    na = "na " if neg else ""

    def p_sense(organ, loc):
        return (f"Yatvādhikaraṇamenaṃ {organ} asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā "
                f"anvāssaveyyuṃ, tassa saṃvarāya {na}paṭipajjati, {na}rakkhati {organ}, {loc} {na}saṃvaraṃ "
                "āpajjati")
    grasp1 = f"{nh}nimittaggāhī hoti {nn}anubyañjanaggāhī"
    grasp2 = f"{nh}nimittaggāhī hoti {'' if neg else 'nā'}{'anubyañjanaggāhī' if neg else 'nubyañjanaggāhī'}"
    p = (f"Idhekacco cakkhunā rūpaṃ disvā {grasp1}. {p_sense('cakkhundriyaṃ', 'cakkhundriye')}. "
         + f"{PE} ".join(a for a, _ in INDR) + f"{PE} manasā dhammaṃ viññāya {grasp2}. "
         + p_sense("manindriyaṃ", "manindriye"))
    g_v = ("nắm giữ dấu hiệu tổng quát, nắm giữ các chi tiết" if neg
           else "không nắm giữ dấu hiệu tổng quát, không nắm giữ các chi tiết")
    k = "không " if neg else ""
    so = "thế mà" if neg else "vì vậy"

    def v_sense(organ):
        return (f"Nếu sống với {organ} không được thu thúc {INVADE}, {so} người ấy {k}thực hành để thu thúc năng lực "
                f"ấy, {k}bảo vệ {organ}, {k}thực hiện sự thu thúc nơi {organ}")
    eye, mind = R.MATTER_NOUN["cakkhundriyaṃ"], B.NAMES.get("manindriyaṃ", "năng lực ý")
    v = (f"Ở đời này, có người khi thấy hình sắc bằng mắt thì {g_v}. {v_sense(eye)}. " +
         cap(f"{ELL} ".join(b for _, b in INDR)) + f"{ELL} khi nhận biết đối tượng của ý bằng ý thì {g_v}. "
         + v_sense(mind))
    return p, v


assert R.MATTER_NOUN["cakkhundriyaṃ"] == "năng lực mắt" and B.NAMES["manindriyaṃ"] == "năng lực ý"
PS_ABOUT = "là nguyên nhân, là điều kiện cho sự sinh khởi"   # hetū «nguyên nhân», paccayā, uppādāya «sự sinh khởi»
NEW_PRE = {
    GROUNDS_SEMI_P: GROUNDS_SEMI_V,
    "Akappiye kappiyasaññitā, kappiye akappiyasaññitā, avajje vajjasaññitā, vajje avajjasaññitā":
        ("Tri giác điều không được phép là được phép, tri giác điều được phép là không được phép, tri giác điều "
         "không đáng chê trách là đáng chê trách, tri giác điều đáng chê trách là không đáng chê trách"),
    F.VICI_P.replace("saṅghe kaṅkhati vicikicchati, sikkhāya", "saṅghe kaṅkhati vicikicchati sikkhāya"): F.VICI_V,
    SAK_ABBR_P: SAK_ABBR_V,
    SAK_ABBR_P.replace("attani vā viññāṇaṃ, viññāṇasmiṃ", "attani vā viññāṇaṃ viññāṇasmiṃ"): SAK_ABBR_V,
    wv_p(True, " [samaggatā (ka.)]"): wrong_view(True).replace("{V}", " " + S.reading("Ka.", "samaggatā")),
    wv_p(True, "", ""): wrong_view(True).replace("{V}", ""),
    wv_p(False, "", ""): wrong_view(False).replace("{V}", ""),
    "Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi, vatena suddhi, sīlabbatena suddhīti": F.RITES_V,
    "Pañcapi āpattikkhandhā āpattiyo, sattapi āpattikkhandhā āpattiyo":
        "Cả năm nhóm lỗi vi phạm đều là lỗi vi phạm, cả bảy nhóm lỗi vi phạm đều là lỗi vi phạm",
    ("Atthi savitakkasavicārā samāpatti, atthi avitakkavicāramattā samāpatti, atthi avitakkaavicārā samāpatti"):
        "; ".join(cap(f"có thành tựu thiền {P[x]}") if i == 0 else f"có thành tựu thiền {P[x]}"
                  for i, x in enumerate(("savitakkasavicārā", "avitakkavicāramattā", "avitakkaavicārā"))),
    DHATU18_P: DHATU18_V,
    "Dvādasāyatanāni – " + ", ".join(AYAT12):
        f"Mười hai lĩnh vực nhận biết {DASH} " + ", ".join(TBL[a] for a in AYAT12),
    PS_P: PS_V,
    "Ye ye dhammā yesaṃ yesaṃ dhammānaṃ hetū paccayā uppādāya [upādāya (sī. ka.)] taṃ taṃ ṭhānanti":
        (f"“Những hiện tượng nào {PS_ABOUT} {S.reading('Sī., Ka.', 'upādāya')} của những hiện tượng nào, thì đó là "
         "điều có thể xảy ra”"),
    "Ye ye dhammā yesaṃ yesaṃ dhammānaṃ na hetū na paccayā uppādāya taṃ taṃ aṭṭhānanti":
        ("“Những hiện tượng nào không phải là nguyên nhân, không phải là điều kiện cho sự sinh khởi của những hiện "
         "tượng nào, thì đó là điều không thể xảy ra”"),
    "Ye te puggalā assaddhā dussīlā appassutā maccharino duppaññā":
        "Có những người không có niềm tin, phạm giới, ít học hỏi, keo kiệt, kém trí tuệ",
    "Ye te puggalā saddhā sīlavanto bahussutā cāgavanto paññavanto":
        "Có những người có niềm tin, giữ giới, học hỏi nhiều, rộng lượng, có trí tuệ",
    guard(True)[0]: guard(True)[1],
    guard(False)[0]: guard(False)[1],
    "Idhekacco appaṭisaṅkhā ayoniso āhāraṃ āhāreti davāya madāya maṇḍanāya vibhūsanāya":
        ("Ở đời này, có người ăn thức ăn mà không suy xét, không đúng cách, để vui đùa, để say sưa, để trang điểm, "
         "để làm đẹp"),
    ("Idhekacco paṭisaṅkhā yoniso āhāraṃ āhāreti – neva davāya na madāya na maṇḍanāya na vibhūsanāya yāvadeva "
     "imassa kāyassa ṭhitiyā yāpanāya vihiṃsūparatiyā brahmacariyānuggahāya, iti purāṇañca vedanaṃ paṭihaṅkhāmi, "
     "navañca vedanaṃ na uppādessāmi, yātrā ca me bhavissati anavajjatā ca phāsuvihāro cāti"):
        (f"Ở đời này, có người suy xét và ăn thức ăn đúng cách {DASH} không phải để vui đùa, không phải để say sưa, "
         "không phải để trang điểm, không phải để làm đẹp, mà chỉ để thân này được duy trì và kéo dài, để chấm dứt "
         "sự bức bách, để hỗ trợ đời sống tu hành trong sạch, với ý nghĩ “Như vậy, ta sẽ diệt trừ cảm giác cũ, sẽ "
         "không làm sinh khởi cảm giác mới, và ta sẽ có sự duy trì mạng sống, sự không có lỗi và sự an trú thoải "
         "mái”"),
}
for _x, _v in VIEW_SELF.items():
    NEW_PRE[f"{_x} attā ca loko cāti"] = f"“Tự ngã và {WORLD} {_v}”"
for _k, _v in NEW_PRE.items():
    add(F.PRE, _k, _v)
SLIP_PRE = {
    GROUNDS_SEMI_P: "«;» after the second and third grounds of annoyance (the parallels have «,»): mirrored",
    F.VICI_P.replace("saṅghe kaṅkhati vicikicchati, sikkhāya", "saṅghe kaṅkhati vicikicchati sikkhāya"):
        "no comma before «sikkhāya kaṅkhati»: the same Vietnamese as the parallels",
    SAK_ABBR_P.replace("attani vā viññāṇaṃ, viññāṇasmiṃ", "attani vā viññāṇaṃ viññāṇasmiṃ"):
        "no comma before «viññāṇasmiṃ vā attānaṃ»: the same Vietnamese as the parallels",
    wv_p(True, "", ""): "no comma before «ye imañca lokaṃ» (^1-1221 has one): the same Vietnamese",
    wv_p(False, "", ""): "no comma before «ye imañca lokaṃ» (^1-1221 has one): the same Vietnamese",
}

# whole heads (everything before « – ayaṃ/idaṃ vuccati»), where no «Yo/Yā/Yaṃ» splits them
FULL = {
    "Satthari kaṅkhati vicikicchati…pe… thambhitattaṃ cittassa manovilekho":
        f"{F.VICI_V.split(', ')[0]}{ELL} {', '.join(D.VICIKICCHA_V.split(', ')[-2:])}",
    "Pubbantaṃ ārabbha yā uppajjati diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho":
        f"{S.REL} sinh khởi liên quan đến quá khứ là {NEW_STRS['diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho']}",
    "Aparantaṃ ārabbha yā uppajjati diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho":
        f"{S.REL} sinh khởi liên quan đến tương lai là {NEW_STRS['diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho']}",
    ("Sahadhammike vuccamāne dovacassāyaṃ dovacassiyaṃ dovacassatā vippaṭikūlaggāhitā vipaccanīkasātatā "
     "anādariyaṃ anādaratā agāravatā appaṭissavatā"):
        ("Khi được nhắc nhở đúng theo Giáo Pháp mà có sự khó bảo, tính khó bảo, sự khó dạy bảo, sự tiếp nhận ngang "
         "trái, sự thích thú việc làm trái, sự thiếu tôn trọng, thái độ thiếu tôn trọng, sự thiếu kính trọng, "
         "sự không vâng lời"),
    ("Sahadhammike vuccamāne sovacassāyaṃ sovacassiyaṃ sovacassatā appaṭikūlaggāhitā avipaccanīkasātatā "
     "sagāravatā sādariyaṃ sādaratā sappaṭissavatā"):
        ("Khi được nhắc nhở đúng theo Giáo Pháp mà có sự dễ bảo, tính dễ bảo, sự dễ dạy bảo, sự không tiếp nhận "
         "ngang trái, sự không thích thú việc làm trái, sự kính trọng, sự tôn trọng, thái độ tôn trọng, "
         "sự vâng lời"),
    ("Yā sā vācā aṇḍakā kakkasā parakaṭukā parābhisajjanī kodhasāmantā asamādhisaṃvattanikā, tathārūpiṃ vācaṃ "
     "pahāya yā sā vācā neḷā kaṇṇasukhā pemanīyā hadayaṅgamā porī bahujanakantā bahujanamanāpā tathārūpiṃ vācaṃ "
     "bhāsitā hoti; yā tattha saṇhavācatā sakhilavācatā apharusavācatā"):
        ("Từ bỏ lời nói thô cộc, cay nghiệt, làm người khác đau lòng, xúc phạm người khác, gần với sự giận dữ, "
         "không đưa đến định tâm, người ấy nói lời không có lỗi, dễ chịu với tai, dễ mến, thấm vào lòng, lịch sự, "
         f"được nhiều người yêu mến, được nhiều người ưa thích; {S.REL.lower()}{HERE_IS} sự dịu dàng trong lời nói, "
         "sự hòa nhã trong lời nói, sự không thô ác trong lời nói"),
    ("Dve paṭisanthārā – āmisapaṭisanthāro ca dhammapaṭisanthāro ca. Idhekacco paṭisanthārako hoti "
     "āmisapaṭisanthārena vā dhammapaṭisanthārena vā"):
        (f"Có hai loại niềm nở tiếp đón {DASH} niềm nở tiếp đón bằng vật phẩm và niềm nở tiếp đón bằng Giáo Pháp. "
         "Ở đời này, có người niềm nở tiếp đón bằng vật phẩm hoặc bằng Giáo Pháp"),
}

# =========================================================================================
# 6. Sentences and whole lines
# =========================================================================================
EVERY_WRONG = cap(F.EVERY_WRONG)                     # Mọi quan điểm sai lầm đều là
SILA_SAMVARA = "sự thu thúc theo giới hạnh"          # sīlasaṃvaro (sīla «giới hạnh» + saṃvaro «sự thu thúc»)
NEW_SENT = {
    "Atthi thinaṃ, atthi middhaṃ.": f"Có {NM['thinaṃ']}, có {NM['middhaṃ']}.",
    "Atthi uddhaccaṃ, atthi kukkuccaṃ.": f"Có {NM['uddhaccaṃ']}, có {NM['kukkuccaṃ']}.",
    "Iti idañca thinaṃ, idañca middhaṃ – idaṃ vuccati thinamiddhanīvaraṇaṃ.":
        f"Như vậy, {NM['thinaṃ']} này và {NM['middhaṃ']} này {DASH} {F.CALLED} {NM['thinamiddhanīvaraṇaṃ']}.",
    "Iti idañca uddhaccaṃ, idañca kukkuccaṃ – idaṃ vuccati uddhaccakukkuccanīvaraṇaṃ.":
        (f"Như vậy, {NM['uddhaccaṃ']} này và {NM['kukkuccaṃ']} này {DASH} {F.CALLED} "
         f"{NM['uddhaccakukkuccanīvaraṇaṃ']}."),
    ("Cha nīvaraṇā [nīvaraṇāni (syā.)] – kāmacchandanīvaraṇaṃ, byāpādanīvaraṇaṃ, thinamiddhanīvaraṇaṃ, "
     "uddhaccakukkuccanīvaraṇaṃ, vicikicchānīvaraṇaṃ, avijjānīvaraṇaṃ."):
        (f"Sáu chướng ngại {S.reading('Syā.', 'nīvaraṇāni')} {DASH} " +
         ", ".join(NM[k] for k in ("kāmacchandanīvaraṇaṃ", "byāpādanīvaraṇaṃ", "thinamiddhanīvaraṇaṃ",
                                   "uddhaccakukkuccanīvaraṇaṃ", "vicikicchānīvaraṇaṃ", "avijjānīvaraṇaṃ")) + "."),
    "Diṭṭhiparāmāso.": cap(NM["diṭṭhiparāmāso"]) + ".",
    ("Cattāri upādānāni – kāmupādānaṃ, diṭṭhupādānaṃ, sīlabbatupādānaṃ, attavādupādānaṃ [kāmūpādānaṃ diṭṭhūpādānaṃ "
     "sīlabbatūpādānaṃ attavādūpādānaṃ (sī.)]."):
        (f"Bốn sự bám víu {DASH} " + ", ".join(NM[k] for k in ("kāmupādānaṃ", "diṭṭhupādānaṃ", "sīlabbatupādānaṃ",
                                                              "attavādupādānaṃ")) +
         " " + S.spell("Sī.", "kāmūpādānaṃ diṭṭhūpādānaṃ sīlabbatūpādānaṃ attavādūpādānaṃ") + "."),
    ("Dasa kilesavatthūni – lobho, doso, moho, māno, diṭṭhi, vicikicchā, thinaṃ, uddhaccaṃ, ahirīkaṃ, "
     "anottappaṃ."):
        (f"Mười chỗ dựa của phiền não {DASH} " +
         ", ".join(NM[k] for k in ("lobho", "doso", "moho", "māno", "diṭṭhi", "vicikicchā", "thinaṃ", "uddhaccaṃ",
                                   "ahirikaṃ", "anottappaṃ")) + "."),
    "Tāneva nīvaraṇāni nīvaraṇā ceva nīvaraṇiyā ca.": f"Chính các chướng ngại ấy {P['nīvaraṇā ceva nīvaraṇiyā ca']}.",
    "Sveva parāmāso parāmāso ceva parāmaṭṭho ca.":
        f"Chính sự hiểu sai lệch ấy {P['parāmāsā ceva parāmaṭṭhā ca']}.",
    "Tāneva upādānāni upādānā ceva upādāniyā ca.": f"Chính các sự bám víu ấy {P['upādānā ceva upādāniyā ca']}.",
    "Teva kilesā kilesā ceva saṃkilesikā ca.": f"Chính các phiền não ấy {P['kilesā ceva saṃkilesikā ca']}.",
    "Teva kilesā kilesā ceva saṃkiliṭṭhā ca.": f"Chính các phiền não ấy {P['kilesā ceva saṃkiliṭṭhā ca']}.",
    "Cittaṃ na vattabbaṃ – cittena sampayuttantipi, cittena vippayuttantipi.":
        f"Về tâm thì không nên nói {DASH} rằng {P['cittasampayuttā']}, hay rằng {P['cittavippayuttā']}.",
    "Cittaṃ na vattabbaṃ – cittena saṃsaṭṭhantipi, cittena visaṃsaṭṭhantipi.":
        f"Về tâm thì không nên nói {DASH} rằng {P['cittasaṃsaṭṭhā']}, hay rằng {P['cittavisaṃsaṭṭhā']}.",
    "Sabbāpi micchādiṭṭhi diṭṭhiparāmāso.": f"{EVERY_WRONG} {NM['diṭṭhiparāmāso']}.",
    "Sabbāpi micchādiṭṭhi diṭṭhi.": f"{EVERY_WRONG} {NM['diṭṭhi']}.",
    "Sabbāpi micchādiṭṭhi diṭṭhivipatti.": f"{EVERY_WRONG} {NM['diṭṭhivipatti']}.",
    "Ṭhapetvā sīlabbatupādānañca attavādupādānañca sabbāpi micchādiṭṭhi diṭṭhupādānaṃ.":
        (f"Ngoại trừ {NM['sīlabbatupādānaṃ']}, và {NM['attavādupādānaṃ']}, {F.EVERY_WRONG} "
         f"{NM['diṭṭhupādānaṃ']}."),
    "Sabbāpi sammādiṭṭhi diṭṭhisampadā.": f"Mọi {S.FN['sammādiṭṭhi']} đều là {NM['diṭṭhisampadā']}.",
    "Sabbampi dussilyaṃ sīlavipatti.": f"Mọi sự phạm giới đều là {NM['sīlavipatti']}.",
    "Sattapi bojjhaṅgā bhāvanābalaṃ.": f"Cả bảy chi phần giác ngộ đều là {NM['bhāvanābalaṃ']}.",
    "Kammassakatañāṇaṃ saccānulomikañāṇaṃ maggasamaṅgissa ñāṇaṃ phalasamaṅgissa ñāṇaṃ.":
        ("Hiểu biết rằng nghiệp là tài sản của chính mình, hiểu biết thuận theo sự thật, hiểu biết của người có "
         "được con đường, hiểu biết của người có được thành quả."),
}
for _x in ("soraccaṃ", "sīlasampadā", "sīlavisuddhi"):
    NEW_SENT[f"Sabbopi sīlasaṃvaro {_x}."] = f"Mọi {SILA_SAMVARA} đều là {NM[_x]}."
for _k, _v in NEW_SENT.items():
    add(F.FIXED_SENT, _k, _v)
ABBR_CLUSTER_RE = re.compile(r"Cattāro (oghā|yogā)…pe… ime dhammā (.+)\.")
SABBEPI_RE = re.compile(r"Sabbepi (kusalā|akusalā) dhammā (\S+)\.")
SABBEVA_RE = re.compile(r"Sabbeva dhammā (\S+)\.")
ANS_Q_RE = re.compile(r"(.+) – ime dhammā (.+)\?")
CLUSTER_X = {"oghā": S.CLUSTERS["ogha"]["x"], "yogā": S.CLUSTERS["yoga"]["x"]}
_SENT_ORIG = F.sentence_vi


def sentence_vi(s):
    if s in F.FIXED_SENT:
        return F.FIXED_SENT[s]
    m = ABBR_CLUSTER_RE.fullmatch(s)
    if m:
        return f"Bốn {CLUSTER_X[m.group(1)]}{ELL} {S.a_form(F.pred(m.group(2)))}"
    m = SABBEPI_RE.fullmatch(s)
    if m:
        return f"Tất cả các hiện tượng {NAMES[m.group(1)]} đều {P[m.group(2)]}."
    m = SABBEVA_RE.fullmatch(s)
    if m:
        return f"Tất cả các hiện tượng đều {P[m.group(1)]}."
    m = ANS_Q_RE.fullmatch(s)
    if m:
        slip("«ime dhammā sukkā?» ends with «?» (a source slip): kept as written")
        return f"{F.body_vi(m.group(1))} {DASH} {S.a_form(F.pred(m.group(2)))[:-1]}?"
    return _SENT_ORIG(s)


F.sentence_vi = sentence_vi
F.SENT_SPLIT = re.compile(r"(?<=[.?]) (?=[A-ZĀĪŪṬḌṆÑ])")   # also after «?» (^1-1310)

# the Suttanta lines that open with the quoted matrix item (^1-1374 … ^1-1383)
MT = {k: v for _, pair in S.SUTTA_ITEMS.items() for k, v in pair}


BRACKET_END = re.compile(r" \[[^\]]*\]$")


def q(item):
    return "“" + BRACKET_END.sub("", MT[item]) + "”"


FEAR = "nỗi sợ"                                      # bhayaṃ
ENERGY4 = "khởi lên ý muốn, nỗ lực, khởi động tinh tấn, nâng tâm lên, ra sức nỗ lực"
# chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati (termbase)
EN_P = "chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati"
GOOD = "các hiện tượng thiện"
LINES = {
    "Diṭṭhivisuddhi kho panāti – yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi.":
        f"{q('diṭṭhivisuddhi kho pana')} {DASH} {S.REL.lower()} là {PANNA_ABBR}.",
    "Yathādiṭṭhissa ca padhānanti – yo cetasiko vīriyārambho…pe… sammāvāyāmo.":
        (f"{q('yathādiṭṭhissa ca padhānaṃ')} {DASH} {S.REL.lower()} là "
         f"{NEW_STRS['cetasiko vīriyārambho…pe… sammāvāyāmo']}."),
    ("Saṃvegoti – jātibhayaṃ jarābhayaṃ byādhibhayaṃ maraṇabhayaṃ. Saṃvejaniyaṃ [saṃvejanīyaṃ (sī.)] ṭhānanti – "
     "jāti jarā byādhi maraṇaṃ."):
        (f"“Sự xúc động” {DASH} {FEAR} sinh, {FEAR} lão hóa, {FEAR} bệnh, {FEAR} chết. “Điều đáng xúc động "
         f"{S.spell('Sī.', 'saṃvejanīyaṃ')}” {DASH} sự sinh, sự lão hóa, bệnh, sự chết."),
    ("Saṃviggassa ca yoniso padhānanti – idha bhikkhu anuppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ anuppādāya "
     f"{EN_P}, uppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ pahānāya {EN_P}, anuppannānaṃ kusalānaṃ dhammānaṃ "
     f"uppādāya {EN_P}, uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya "
     f"pāripūriyā {EN_P}."):
        (f"{q('saṃviggassa ca yoniso padhānaṃ')} {DASH} ở đời này, vị tỳ-khưu {ENERGY4} để {BAD} chưa sinh khởi "
         f"không sinh khởi; {ENERGY4} để dứt bỏ {BAD} đã sinh khởi; {ENERGY4} để {GOOD} chưa sinh khởi được sinh "
         f"khởi; {ENERGY4} để {GOOD} đã sinh khởi được duy trì, không bị mai một, được tăng trưởng, được lớn mạnh, "
         "được tu tập, được hoàn thiện."),
    "Asantuṭṭhitā ca kusalesu dhammesūti – yā kusalānaṃ dhammānaṃ bhāvanāya asantuṭṭhassa bhiyyokamyatā.":
        (f"{q('asantuṭṭhitā ca kusalesu dhammesu')} {DASH} {S.REL.lower()} là sự mong muốn nhiều hơn nữa của người "
         f"không tự mãn trong việc tu tập {GOOD}."),
    ("Appaṭivānitā ca padhānasminti – yā kusalānaṃ dhammānaṃ bhāvanāya sakkaccakiriyatā sātaccakiriyatā "
     "aṭṭhitakiriyatā anolīnavuttitā anikkhittachandatā anikkhittadhuratā āsevanā bhāvanā bahulīkammaṃ."):
        (f"{q('appaṭivānitā ca padhānasmiṃ')} {DASH} {S.REL.lower()}, trong việc tu tập {GOOD}, là sự làm chu đáo, "
         "sự làm liên tục, sự làm không ngừng nghỉ, sự hành xử không chùng xuống, sự không buông bỏ ý muốn, "
         "sự không buông bỏ gánh, sự thực hành, sự tu tập, sự làm đi làm lại."),
    ("Vijjāti – tisso vijjā – pubbenivāsānussati ñāṇaṃ vijjā, sattānaṃ cutūpapāte ñāṇaṃ vijjā, āsavānaṃ khaye "
     "ñāṇaṃ vijjā."):
        (f"{q('vijjā ca')} {DASH} có ba loại hiểu biết chân thật {DASH} hiểu biết về sự nhớ lại các đời sống trước là "
         "hiểu biết chân thật, hiểu biết về sự chết và sự tái sinh của chúng sinh là hiểu biết chân thật, hiểu biết "
         "về sự diệt tận các ô nhiễm là hiểu biết chân thật."),
    "Vimuttīti – dve vimuttiyo – cittassa [cittassa ca (sī. syā.)] adhimutti, nibbānañca.":
        (f"{q('vimutti ca')} {DASH} có hai loại giải thoát {DASH} sự thoát ly của tâm "
         f"{S.reading('Sī., Syā.', 'cittassa ca')} và Niết-bàn."),
    "Khaye ñāṇanti – maggasamaṅgissa ñāṇaṃ.": f"{q('khaye ñāṇaṃ')} {DASH} hiểu biết của người có được con đường.",
    "Anuppāde ñāṇanti – phalasamaṅgissa ñāṇaṃ.":
        f"{q('anuppāde ñāṇanti')} {DASH} hiểu biết của người có được thành quả.",
}
assert q("diṭṭhivisuddhi kho pana") == "“Sự trong sạch về quan điểm”"
assert q("anuppāde ñāṇanti") == "“Hiểu biết về sự không sinh khởi”"
NEW_H = {
    "##### Oghagocchakaṃ": f"##### {S.CLUSTERS['ogha']['heading']}",
    "##### Yogagocchakaṃ": f"##### {S.CLUSTERS['yoga']['heading']}",
    "##### Nīvaraṇagocchakaṃ": f"##### {S.CLUSTERS['nivarana']['heading']}",
    "##### Parāmāsagocchakaṃ": f"##### {S.CLUSTERS['paramasa']['heading']}",
    "##### Mahantaradukaṃ": f"##### {S.MAHANTARA}",
    "##### Upādānagocchakaṃ": f"##### {S.CLUSTERS['upadana']['heading']}",
    "##### Kilesagocchakaṃ": f"##### {S.KILESA['heading']}",
    "##### Piṭṭhidukaṃ": f"##### {S.PITTHI}",
    "#### Suttantikadukanikkhepaṃ": f"#### {F.H['#### Dukanikkhepaṃ'][5:]} theo kinh",   # 1-matika «… theo kinh»
    "Nikkhepakaṇḍe dutiyabhāṇavāro.": F.H["Nikkhepakaṇḍe paṭhamabhāṇavāro."].replace("thứ nhất", "thứ hai"),
    "Abhidhammadukaṃ.": "Bộ đôi Vi Diệu Pháp.",      # as «Tikaṃ.» = «Bộ ba.» (1-matika «… Vi Diệu Pháp»)
    "Nikkhepakaṇḍaṃ niṭṭhitaṃ.": f"{S.CH_HEADINGS['Nikkhepakaṇḍaṃ']} đã hoàn tất.",
}
assert NEW_H["#### Suttantikadukanikkhepaṃ"] == "#### Tóm lược bộ đôi theo kinh"
assert NEW_H["Nikkhepakaṇḍe dutiyabhāṇavāro."] == "Phần tụng đọc thứ hai trong phần tóm lược."
for _k, _v in NEW_H.items():
    add(F.H, _k, _v)

# =========================================================================================
# 7. The definition frame (4-01's def_vi, extended: a lazy head, whole heads, a dash before «yā evarūpā»,
#    no relative pronoun, any extra sentence)
# =========================================================================================
DEF_LAZY = re.compile(r"(?P<head>.+?) – (?:ayaṃ|idaṃ) vuccati (?P<x>.+?)\.(?: (?P<extra>.+))?$")


def def_vi(rest):
    m = DEF_LAZY.fullmatch(rest)
    if not m:
        return F.rest_vi(rest)
    head, x, extra = m.group("head"), m.group("x"), m.group("extra")
    if head in FULL:
        out = FULL[head]
    else:
        r = F.REL_RE.search(head)
        if r is None:                                # «Vedanākkhandho, … – idaṃ vuccati nāmaṃ.»
            out = F.body_vi(head)
        else:
            pre, body = head[:r.start()].rstrip(), head[r.end():]
            out, rel = "", F.REL
            if pre:
                mark = ""
                if pre[-1] in ".,;ः":
                    pre, mark = pre[:-1], pre[-1]
                elif pre.endswith(f" {DASH}"):
                    pre, mark = pre[:-2], DASH
                if mark == "ः":
                    slip("the devanāgarī visarga «ः» stands for a punctuation mark: rendered «;»")
                if "acarī ti" in pre:
                    slip("«acarī ti» (a space inside the word): rendered as «acarīti»")
                if pre in SLIP_PRE:
                    slip(SLIP_PRE[pre])
                out = F.PRE[pre] + {".": ".", DASH: f" {DASH}"}.get(mark, ";") + " "
                if mark != ".":
                    rel = F.REL[0].lower() + F.REL[1:]
            if body in SLIP_STRS:
                slip(SLIP_STRS[body])
            sv = F.str_vi(body)
            if sv.startswith(","):
                out += f"{rel}{sv}"
            elif r.group("ev"):
                out += f"{rel} {F.SUCH} là {sv}"
            else:
                out += f"{rel} là {sv}"
    out += f" {DASH} {F.CALLED} {NM[x]}."
    if extra:
        out += " " + (F.EXTRA[extra] if extra in F.EXTRA else F.rest_vi(extra))
    return out


F.def_vi = def_vi
_LINE_ORIG = F.translate_line


def translate_line(line):
    if line in LINES:
        return LINES[line]
    return _LINE_ORIG(line)


F.translate_line = translate_line


# =========================================================================================
# 8. Build and checks
# =========================================================================================
def build(part):
    segs = B.segments(S.PALI / part)
    return "\n\n".join(F.render(segs)) + "\n", len(segs)


def check_401():
    text, _ = F.build()
    assert unicodedata.normalize("NFC", text) == (S.OUT / PART_401).read_bytes().decode("utf-8"), PART_401
    print(f"{PART_401}: rebuilt in memory, byte-identical to the finished file")


def notes():
    def new(name):
        return [(k, v) for k, v in getattr(F, name).items() if k not in SNAP[name]]

    L = ["# pi-1 Vietnamese rails: new formulas of 4-02 and 4-03", "",
         "Generated by build_rails_4-02_4-03_vi.py from its fixed strings; import that file instead of retyping. "
         "It extends the tables of build_rails_4-01_vi.py in memory (new keys only) and reuses its frames: "
         "«Những hiện tượng nào X?» / «– những hiện tượng này X.» (1-matika, S.q_form / S.a_form), «Ở đây, X là gì?», "
         "«Điều mà [thuộc loại như vậy] là S – đó được gọi là X.», taṃsampayutto «… gắn liền với chúng», "
         "taṃsamuṭṭhānaṃ «… do chúng sinh ra», tadekaṭṭhā ca kilesā «và các phiền não cùng hiện diện với chúng», the "
         "lobha / dosa / moha / vicikicchā / diṭṭhi / māna strings, the ten views, the grounds of annoyance. Strings "
         "already in vi-rails-formulas.md or the earlier notes are not repeated. Suttanta item names: 1-matika "
         "verbatim. Format: Pāli = tiếng Việt.", "",
         "## Frames", "",
         f"PRE – yā evarūpā S – ayaṃ vuccati X. = PRE {DASH} {F.REL.lower()} {F.SUCH} là S {DASH} {F.CALLED} X.",
         f"Iti idañca X, idañca Y – idaṃ vuccati Z. = Như vậy, X này và Y này {DASH} {F.CALLED} Z.",
         f"X Y-ena kileso / nīvaraṇañceva / upādānañceva … sampayutto ca = X, {F.REL_TO} Y, vừa là … vừa gắn liền "
         "với … (pairs joined with «; »; -o / -ā / -añca endings: one Vietnamese)",
         f"Cattāro oghā / yogā…pe… ime dhammā X. = Bốn dòng lũ / ách{ELL} những hiện tượng này X.",
         "Sabbepi kusalā / akusalā dhammā X. = Tất cả các hiện tượng thiện / bất thiện đều X.",
         "Sabbeva dhammā X. = Tất cả các hiện tượng đều X.",
         f"Sabbopi sīlasaṃvaro X. = Mọi {SILA_SAMVARA} đều là X.",
         f"Na X-bhūmiyaṃ SPH = không {F.LEVEL} có X, SPH",
         "SPH alone (Rūpāvacarā, arūpāvacarā, apariyāpannā) = những hiện tượng SPH",
         f"yā tattha S = {F.REL.lower()}{HERE_IS} S", "",
         "## Pieces of the answers", ""]
    L += [f"{k} = {v[1]}" for k, v in new("FIXED")]
    L += [f"KH: {k} = {v}" for k, v in new("KH_LISTS")]
    L += [f"Tehi dhammehi ye dhammā {k} = những hiện tượng {v}" for k, v in new("TEHI")]
    L += [f"{b}bhūmiyaṃ{' (… ' + e + ' ṭhapetvā)' if e else ''} = {cap(F.LEVEL)} {v}" for (b, e), v in new("BHUMI")]
    L += [f"Na {b}bhūmiyaṃ = Không {F.LEVEL} {v}" for b, v in BHUMI_NA.items()]
    L += [f"{k} ṭhapetvā = ngoại trừ {v}" for k, v in new("EXCL")]
    L += ["", "## Definitions: the strings", ""] + [f"{k} = {v}" for k, v in new("STRS")]
    L += ["", "## Definitions: the openings", ""] + [f"{k} = {v}" for k, v in new("PRE")]
    L += ["", "## Definitions: whole heads (before « – ayaṃ/idaṃ vuccati»)", ""] + [f"{k} = {v}" for k, v in FULL.items()]
    L += ["", "## Sentences", ""] + [f"{k} = {v}" for k, v in new("FIXED_SENT")]
    L += ["", "## Whole lines (^1-1374 … ^1-1383)", ""] + [f"{k} = {v}" for k, v in LINES.items()]
    L += ["", "## Names", ""] + [f"{k} = {v}" for k, v in new("NM")]
    L += [f"{k} (instrumental) = {NM[v]}" for k, v in new("INSTR")]
    L += ["", "## Headings and closing lines", ""] + [f"{k} = {v}" for k, v in new("H")]
    L += ["", "## Source slips and marks (translated as written; punctuation rendered as meant)", ""]
    by_note = {}
    for sid, note in dict.fromkeys(F.SLIPS):
        if sid.startswith("1-") and int(sid.split("-")[1]) >= 1156:
            by_note.setdefault(note, []).append(f"^{sid}")
    for note, sids in by_note.items():
        L.append(f"{', '.join(sids)}: {note}")
    L += ["^1-1235 «ahirīkaṃ», ^1-1307 / 1309 «Ahirīkañca» (elsewhere «ahirikaṃ»): one word, the same Vietnamese",
          "^1-1358 «asammusanatā» (chapter 2 «asammussanatā»): one word, the same Vietnamese",
          "^1-1176: the run names uddhaccanīvaraṇaṃ and kukkuccanīvaraṇaṃ separately (the list of six joins them): "
          "as written",
          "^1-1178, ^1-1259: «kusalābyākatā» where the sibling pairs have «kusalākusalābyākatā»: as written",
          "^1-1285, ^1-1286: the spheres listed the other way round from the sibling pairs: as written",
          "^1-1283, ^1-1285: the associated aggregates start from «saññākkhandho»: as written",
          "^1-1167, ^1-1238: a full stop before «Yā / Yaṃ evarūpā» where the parallels ^1-1241, ^1-1168 have «ः»: "
          "mirrored",
          "", "## Termbase notes", "",
          "rūpaṃ in ^1-1317 «… idaṃ vuccati rūpaṃ»: the termbase closing formula has «được gọi là phần vật chất», but "
          "1-matika (verbatim, binding) names the item «Vật chất»: «đó được gọi là vật chất»",
          "nāmaṃ in the naming list (^1-1313 … 1315) = «tên»: the termbase has only «phần tinh thần» (nāmarūpa)",
          "dukkha in «sokaparidevadukkhadomanassupāyāsā» (^1-1343) = «sự khó chịu» (bodily pain, APPROVED decision 1); "
          "dukkhakkhandhassa = «khối khổ đau» (suffering in general)",
          "kilesavatthūni (^1-1235) = «chỗ dựa của phiền não» (termbase vatthūni «chỗ dựa»)",
          "Sappītikabhūmiyaṃ and Pītibhūmiyaṃ: both «ở cấp độ có sự hân hoan» (1-matika sappītikā «có sự hân hoan»; "
          "4-01 Pītibhūmiyaṃ); Na X-bhūmiyaṃ = «không ở cấp độ có X»",
          "No entries, built from the members or the closest sibling: dinnaṃ «sự bố thí», yiṭṭhaṃ «sự cúng tế», "
          "vipāko «kết quả», sukata «làm tốt», sammaggatā «đã đi đúng đắn» (gatā «đi»), assaddhā «không có niềm tin», "
          "appassutā «ít học hỏi», sambhatti «sự gắn bó mật thiết», taṃsampavaṅkatā «sự nghiêng về phía họ», "
          "ajjavatā «tính ngay thật», pariyonāho «sự bao phủ hoàn toàn», līyitattaṃ «trạng thái khởi co rút», "
          "kukkuccāyitattaṃ «trạng thái khởi hối tiếc», anubyañjana «các chi tiết», Yatvādhikaraṇamenaṃ (rendered by "
          "the sentence «Nếu sống với … thì …»), byañjanaṃ «từ ngữ», gutti «sự canh giữ», paṭihaṅkhāmi «diệt trừ», "
          "vihiṃsūparati «chấm dứt sự bức bách», bhiyyokamyatā «sự mong muốn nhiều hơn nữa», aṭṭhitakiriyatā «sự làm "
          "không ngừng nghỉ», anolīnavuttitā «sự hành xử không chùng xuống», sucarita «hành vi tốt», upaga «sinh vào», "
          "jarāmaraṇaṃ «sự lão hóa và sự chết», nāmarūpaṃ «phần tinh thần và vật chất», saḷāyatanaṃ «sáu lĩnh vực "
          "nhận biết», sambhavanti «sinh khởi», sīlasaṃvaro «sự thu thúc theo giới hạnh», dussilyaṃ «sự phạm giới»",
          "Names: Akaniṭṭha «chư thiên Sắc Cứu Cánh» and brahmaloka «cõi Phạm Thiên» (no entries; termbase brahma "
          "«Phạm Thiên»), paranimmitavasavattī «chư thiên Tha Hóa Tự Tại» (termbase Tha / Hóa / Tự Tại), "
          "avicinirayaṃ «địa ngục Vô Gián» (termbase)",
          "kāyassa in the torpor string (^1-1163) = «thân tinh thần» (termbase sense 2, the mental body); in the "
          "food passage (^1-1355) «thân» (the physical body)",
          "Variant labels: nīvaraṇāni (Syā.), samaggatā (Ka.), upādāya (Sī., Ka.), cittassa ca (Sī., Syā.), "
          "diṭṭhadhammasukhavihārassa (Ka.) = «dị bản» (another word or form, as 4-01 rūpā); kāmūpādānaṃ … (Sī.), "
          "paranimmitavasavattideve, akaniṭṭhadeve (Sī., Ka.), saṃvejanīyaṃ (Sī.) = «khác chính tả»"]
    (HERE / "notes-4-02_4-03.md").write_text(unicodedata.normalize("NFC", "\n".join(L) + "\n"), encoding="utf-8",
                                             newline="\n")
    print("wrote", HERE / "notes-4-02_4-03.md")


def main():
    F.check_earlier_unchanged()                      # 2-01 … 3-03 (their own tables, untouched): unchanged
    check_401()                                      # 4-01 rendered with this file's extensions: unchanged
    for part in PARTS:
        text, n = build(part)
        (S.OUT / part).write_text(unicodedata.normalize("NFC", text), encoding="utf-8", newline="\n")
        print("wrote", S.OUT / part, n, "segments")
    notes()


if __name__ == "__main__":
    main()
