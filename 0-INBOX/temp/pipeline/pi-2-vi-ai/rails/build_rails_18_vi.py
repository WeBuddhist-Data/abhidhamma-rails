"""Builder for the Vietnamese rails translation of pi-2 (Vibhaṅga, «Phân tích các hiện tượng», plain audience),
chapter 18 (Dhammahadayavibhaṅgo ^2-18-0 … ^2-1044), the last chapter, with the book colophon.

Writes (only when run as a script, without --dry):
  AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/18-dhammahadayavibhango.md
(the new formulas are listed by hand in rails/notes-18.md).

Translated fresh from the Pāli with the locked pi-2 termbase: the planes «cõi dục lạc / cõi hình sắc / cõi không hình
sắc» (Dhātu «cõi» here, unlike ch. 3's elements «yếu tố»); apariyāpanna «không nằm trong các cõi tồn tại»; the god and
realm names of the termbase, pi-1 wording where pi-1 has the name (^1-1287 … ^1-1293); koṭi converted into millions
(«triệu», arithmetic exact, user decision); abhiññeyya … sacchikātabba from the termbase; the colophon «Bộ “Phân tích
các hiện tượng” đã hoàn tất.». Sentences whose Pāli is identical to a sentence of the approved pi-1 rails or of the
finished pi-2 chapters 1-17 are taken from those files (sentence map, read-only; only the dash of «không nên nói –
rằng» is dropped where this chapter's Pāli has no dash). The question sections are translated by a small
subject + predicate table (SUBJ, CLAUSE, ITEM) whose strings repeat the ch. 1-5 «Phần hỏi đáp» wording.
Importing this module writes nothing.

usage: python -I -X utf8 build_rails_18_vi.py [--dry] [--report]
"""
import pathlib
import re
import sys
import unicodedata

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-vi-ai\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)

PART = "18-dhammahadayavibhango.md"
PI1_PALI = S.ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
PI1_VI = S.ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-rails_split_chapters"
PI1_FILES = ["1-matika.md", "2-01-cittuppadakandam.md", "2-02-cittuppadakandam.md", "2-03-cittuppadakandam.md",
             "2-04-cittuppadakandam.md", "2-05-cittuppadakandam.md", "3-01-rupakandam.md", "3-02-rupakandam.md",
             "3-03-rupakandam.md", "4-01-nikkhepakandam.md", "4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md",
             "5-atthakathakandam.md"]
PI2_DONE = ["1-khandhavibhango.md", "2-ayatanavibhango.md", "3-dhatuvibhango.md", "4-saccavibhango.md",
            "5-indriyavibhango.md", "6-paticcasamuppadavibhango.md", "7-satipatthanavibhango.md",
            "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md", "10-bojjhangavibhango.md",
            "11-maggangavibhango.md", "12-jhanavibhango.md", "13-appamannavibhango.md", "14-sikkhapadavibhango.md",
            "15-patisambhidavibhango.md", "16-nanavibhango.md", "17-khuddakavatthuvibhango.md"]
cap = S.cap
SLIPS, MISFITS, PI1_USED, PI2_USED, PARSED = [], [], [], [], []
IDRX = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
SPL = re.compile(r"(?<=[.?!])\s+")


def note(lst, s):
    if s not in lst:
        lst.append(s)


def slip(s):
    note(SLIPS, s)


def misfit(s):
    note(MISFITS, s)


def low(s):
    return s[:1].lower() + s[1:]


# =========================================================================== the Pāli source, by segment
def pali_segments():
    segs, cur = {}, []
    for ln in (S.PALI / PART).read_text(encoding="utf-8").split("\n"):
        if not ln.strip():
            continue
        m = S.ID.search(ln)
        cur.append(IDRX.sub("", ln))
        if m:
            segs[m.group(1)] = cur
            cur = []
    return segs


PS = pali_segments()


# =========================================================================== sentence map (pi-1, pi-2 ch. 1-17)
def _nonempty(p):
    return [ln for ln in p.read_text(encoding="utf-8").split("\n") if ln.strip()]


def key(s):
    s = IDRX.sub("", s).strip()
    s = s.replace('"', "").replace("“", "").replace("”", "").replace(" – ", " ").replace("ti pi", "tipi")
    s = re.sub(r"\s+", " ", s)
    return s[:1].lower() + s[1:]


def build_map():
    m = {}
    for tag, pd, vd, names in (("pi-1", PI1_PALI, PI1_VI, PI1_FILES), ("pi-2", S.PALI, S.OUT, PI2_DONE)):
        for n in names:
            pa, vi = _nonempty(pd / n), _nonempty(vd / n)
            assert len(pa) == len(vi), n
            for p, v in zip(pa, vi):
                ps, vs = SPL.split(IDRX.sub("", p).strip()), SPL.split(IDRX.sub("", v).strip())
                if len(ps) != len(vs):
                    continue
                for a, b in zip(ps, vs):
                    m.setdefault(key(a), (f"{tag}/{n}", b))
    return m


MAP = build_map()


def V(pali, required=True):
    """the approved Vietnamese of an identical Pāli sentence (pi-1 rails or pi-2 ch. 1-17), dash fixed for ch. 18"""
    r = MAP.get(key(pali))
    if not r:
        assert not required, pali
        return None
    src, vi = r
    if "–" not in pali:
        vi = vi.replace("nói – rằng", "nói rằng")
    assert vi.count("–") == pali.count("–"), (pali, vi)
    (PI1_USED if src.startswith("pi-1") else PI2_USED).append((src, pali))
    if pali[:1].islower():
        vi = low(vi)
    return vi


# =========================================================================== vocabulary
NUMW = {"eka": "một", "dve": "hai", "tayo": "ba", "tīṇi": "ba", "tisso": "ba", "cattāro": "bốn", "catasso": "bốn",
        "cattāri": "bốn", "pañca": "năm", "cha": "sáu", "satta": "bảy", "aṭṭha": "tám", "nava": "chín",
        "dasa": "mười", "ekādasa": "mười một", "dvādasa": "mười hai", "terasa": "mười ba", "cuddasa": "mười bốn",
        "pannarasa": "mười lăm", "soḷasa": "mười sáu", "aṭṭhārasa": "mười tám", "bāvīsati": "hai mươi hai"}
# the twelve categories of the chapter, as counted nouns
KH, AY, AYN, DH, SC, IN, HE, AH, PH, VE, SA, CE, CI = ("khối", "lĩnh vực", "lĩnh vực nhận biết", "yếu tố", "sự thật",
                                                       "năng lực", "gốc rễ", "loại dưỡng chất", "loại tiếp xúc",
                                                       "loại cảm giác", "loại tri giác", "loại chủ ý", "loại tâm")
CATS = [KH, AYN, DH, SC, IN, HE, AH, PH, VE, SA, CE, CI]


def n(num, noun):
    return f"{NUMW[num]} {noun}"


# items
KHANDHA = {"rūpa": "khối vật chất", "vedanā": "khối cảm giác", "saññā": "khối tri giác", "saṅkhāra": "khối tạo tác",
           "viññāṇa": "khối thức"}
AYAT = {"cakkh": "lĩnh vực mắt", "rūp": "lĩnh vực hình sắc", "sot": "lĩnh vực tai", "sadd": "lĩnh vực âm thanh",
        "ghān": "lĩnh vực mũi", "gandh": "lĩnh vực mùi", "jivh": "lĩnh vực lưỡi", "ras": "lĩnh vực vị",
        "kāy": "lĩnh vực thân", "phoṭṭhabb": "lĩnh vực vật xúc chạm", "man": "lĩnh vực ý",
        "dhamm": "lĩnh vực đối tượng của ý"}
DHATU = {"cakkhu": "yếu tố mắt", "rūpa": "yếu tố hình sắc", "cakkhuviññāṇa": "yếu tố thức qua mắt",
         "sota": "yếu tố tai", "sadda": "yếu tố âm thanh", "sotaviññāṇa": "yếu tố thức qua tai",
         "ghāna": "yếu tố mũi", "gandha": "yếu tố mùi", "ghānaviññāṇa": "yếu tố thức qua mũi",
         "jivhā": "yếu tố lưỡi", "rasa": "yếu tố vị", "jivhāviññāṇa": "yếu tố thức qua lưỡi",
         "kāya": "yếu tố thân", "phoṭṭhabba": "yếu tố vật xúc chạm", "kāyaviññāṇa": "yếu tố thức qua thân",
         "mano": "yếu tố ý", "dhamma": "yếu tố đối tượng của ý", "manoviññāṇa": "yếu tố ý thức"}
SACCA = {"dukkha": "sự thật về khổ đau", "samudaya": "sự thật về sự phát sinh", "nirodha": "sự thật về sự chấm dứt",
         "magga": "sự thật về con đường"}
INDR = {"cakkhu": "năng lực mắt", "sot": "năng lực tai", "ghān": "năng lực mũi", "jivh": "năng lực lưỡi",
        "kāy": "năng lực thân", "man": "năng lực ý", "itth": "năng lực nữ tính", "puris": "năng lực nam tính",
        "jīvit": "năng lực sống", "sukh": "năng lực dễ chịu", "dukkh": "năng lực khó chịu",
        "somanass": "năng lực niềm vui", "domanass": "năng lực nỗi buồn", "upekkh": "năng lực bình thản",
        "saddh": "năng lực niềm tin", "vīriy": "năng lực tinh tấn", "sat": "năng lực tỉnh thức",
        "samādh": "năng lực định tâm", "paññ": "năng lực trí tuệ",
        "anaññātaññassāmīt": "năng lực biết được điều chưa từng biết", "aññ": "năng lực hiểu biết trọn vẹn",
        "aññātāv": "năng lực của người đã hiểu biết trọn vẹn", "rūpajīvit": "năng lực sống thuộc vật chất"}
DOORS = {"cakkhu": "mắt", "sota": "tai", "ghāna": "mũi", "jivhā": "lưỡi", "kāya": "thân", "manodhātu": "yếu tố ý",
         "manoviññāṇadhātu": "yếu tố ý thức", "kāyaviññāṇadhātu": "yếu tố thức qua thân"}
SEVEN = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "manodhātu", "manoviññāṇadhātu"]


def phassa(d):
    return f"sự tiếp xúc của {DOORS[d]}"                                   # Cakkhusamphasso … (termbase)


def born(noun, d):
    return f"{noun} sinh từ sự tiếp xúc của {DOORS[d]}"                    # cakkhusamphassajā vedanā … (pi-2 ch. 1)


CITTA7 = ["thức qua mắt", "thức qua tai", "thức qua mũi", "thức qua lưỡi", "thức qua thân", "yếu tố ý",
          "yếu tố ý thức"]                                                 # PI1 ^1-1193
FOOD = S.FOOD                                                              # PI1 kabaḷīkāro āhāro
AHARA3 = ["sự tiếp xúc trong vai trò dưỡng chất", "chủ ý của ý trong vai trò dưỡng chất",
          "thức trong vai trò dưỡng chất"]                                 # PI1 phassāhāro … viññāṇāhāro (termbase)
ROOT_K = ["sự không tham lam", "sự không sân hận", "sự không si mê"]       # PI1 alobho, adoso, amoho
ROOT_A = ["sự tham lam", "sự sân hận", "sự si mê"]                         # PI1 lobho, doso, moho
AS = "trong vai trò"                    # X-hetu «X trong vai trò gốc rễ …» (as FOOD «… trong vai trò dưỡng chất»)
HETU_K, HETU_A, HETU_ABY = "gốc rễ thiện", "gốc rễ bất thiện", "gốc rễ không xác định về mặt đạo đức"
HETU_VIP = "gốc rễ là quả của nghiệp"                                      # vipākahetu (termbase)


def hetu(root, kind):
    """alobho kusalahetu  ->  «sự không tham lam trong vai trò gốc rễ thiện»"""
    return f"{root} {AS} {kind}"


# =========================================================================== question sections: subjects
NOUN = {"khandhā": KH, "āyatanā": AY, "dhātuyo": DH, "saccā": SC, "saccāni": SC, "indriyā": IN, "hetū": HE,
        "āhārā": AH, "phassā": PH, "vedanā": VE, "saññā": SA, "cetanā": CE, "cittā": CI}
SUBJ = {}
for _num in NUMW:
    for _noun, _vi in NOUN.items():
        SUBJ[f"{_num} {_noun}"] = n(_num, _vi)
for _pa, _num in (("das", "dasa"), ("dv", "dve"), ("pañc", "pañca"), ("satt", "satta")):
    SUBJ[f"{_pa}āyatanā"] = n(_num, AY)                                   # Dasāyatanā «Mười lĩnh vực» (pi-2 ch. 2)
for _pa, _num in (("das", "dasa"), ("tīṇ", "tīṇi"), ("nav", "nava"), ("teras", "terasa"), ("cuddas", "cuddasa"),
                  ("aṭṭh", "aṭṭha"), ("satt", "satta"), ("pañc", "pañca"), ("dv", "dve"), ("dvādas", "dvādasa"),
                  ("ekādas", "ekādasa"), ("cattār", "cattāri"), ("bāvīsat", "bāvīsati")):
    SUBJ[f"{_pa}indriyā"] = n(_num, IN)                                   # Dasindriyā «Mười năng lực» (pi-2 ch. 5)
for _kind, _vi in (("kusala", HETU_K), ("akusala", HETU_A), ("abyākata", HETU_ABY)):
    SUBJ[f"tayo {_kind}hetū"] = f"ba {_vi}"                                # PI1 tayo kusalahetū «ba gốc rễ thiện»
SUBJ.update({
    "rūpakkhandho": KHANDHA["rūpa"], "saṅkhārakkhandho": KHANDHA["saṅkhāra"],
    "manāyatanaṃ": AYAT["man"], "dhammāyatanaṃ": AYAT["dhamm"], "saddāyatanaṃ": AYAT["sadd"],
    "rūpāyatanaṃ": AYAT["rūp"], "gandhāyatanaṃ": AYAT["gandh"], "rasāyatanaṃ": AYAT["ras"],
    "phoṭṭhabbāyatanaṃ": AYAT["phoṭṭhabb"],
    "manoviññāṇadhātu": DHATU["manoviññāṇa"], "dhammadhātu": DHATU["dhamma"], "manodhātu": DHATU["mano"],
    "kāyaviññāṇadhātu": DHATU["kāyaviññāṇa"], "rūpadhātu": DHATU["rūpa"], "saddadhātu": DHATU["sadda"],
    "gandhadhātu": DHATU["gandha"], "rasadhātu": DHATU["rasa"], "phoṭṭhabbadhātu": DHATU["phoṭṭhabba"],
    "samudayasaccaṃ": SACCA["samudaya"], "maggasaccaṃ": SACCA["magga"], "nirodhasaccaṃ": SACCA["nirodha"],
    "dukkhasaccaṃ": SACCA["dukkha"],
    "jīvitindriyaṃ": INDR["jīvit"], "domanassindriyaṃ": INDR["domanass"], "upekkhindriyaṃ": INDR["upekkh"],
    "anaññātaññassāmītindriyaṃ": INDR["anaññātaññassāmīt"], "aññindriyaṃ": INDR["aññ"],
    "aññātāvindriyaṃ": INDR["aññātāv"],
    "doso akusalahetu": hetu(ROOT_A[1], HETU_A), "moho akusalahetu": hetu(ROOT_A[2], HETU_A),
    "kabaḷīkāro āhāro": FOOD,
    "manoviññāṇadhātusamphasso": phassa("manoviññāṇadhātu"), "manodhātusamphasso": phassa("manodhātu"),
    "kāyaviññāṇadhātusamphasso": phassa("kāyaviññāṇadhātu"),
    "manoviññāṇadhātusamphassajā vedanā": born("cảm giác", "manoviññāṇadhātu"),
    "manoviññāṇadhātusamphassajā saññā": born("tri giác", "manoviññāṇadhātu"),
    "manoviññāṇadhātusamphassajā cetanā": born("chủ ý", "manoviññāṇadhātu"),
})
SUBJ_KEYS = sorted(SUBJ, key=len, reverse=True)
ELL = re.compile(r"\s*…(?:pe…)?\s*")


def subject(s):
    """the longest run of subjects joined by «…» / «…pe…» at the start of s -> (Vietnamese, rest of s)"""
    parts, rest = [], s
    while True:
        lr = low(rest)
        k = next((k for k in SUBJ_KEYS if lr.startswith(k + " ") or lr.startswith(k + "…")), None)
        if not k:
            break
        vi = SUBJ[k]
        parts.append(cap(vi) if rest[:1].isupper() else vi)
        rest = rest[len(k):]
        m = ELL.match(rest)
        if m and m.group(0).strip():
            rest = rest[m.end():]
            continue
        rest = rest.lstrip()
        break
    if not parts:
        return None, s
    return "… ".join(parts), rest


# =========================================================================== question sections: predicates
CLAUSE = {
    "kusalā": "là thiện", "akusalā": "là bất thiện", "abyākatā": "không xác định về mặt đạo đức",
    "sukhāya vedanāya sampayuttā": "gắn liền với cảm giác dễ chịu",
    "dukkhāya vedanāya sampayuttā": "gắn liền với cảm giác khó chịu",
    "adukkhamasukhāya vedanāya sampayuttā": "gắn liền với cảm giác không khó chịu cũng không dễ chịu",
    "dukkhamasukhāya vedanāya sampayuttā": "gắn liền với cảm giác khó chịu và không dễ chịu",   # ^2-1039 slip
    "vipākā": "là quả của nghiệp", "vipākadhammadhammā": "có khả năng sinh ra quả",
    "nevavipākanavipākadhammadhammā": "không phải là quả của nghiệp cũng không có khả năng sinh ra quả",
    "upādinnupādāniyā": "do nghiệp tạo ra và là đối tượng của sự bám víu",
    "anupādinnupādāniyā": "không do nghiệp tạo ra nhưng là đối tượng của sự bám víu",
    "anupādinnaanupādāniyā": "không do nghiệp tạo ra và không phải là đối tượng của sự bám víu",
    "savitakkasavicārā": "có sự hướng tâm và sự duy trì tâm",
    "avitakkavicāramattā": "không có sự hướng tâm, chỉ có sự duy trì tâm",
    "avitakkaavicārā": "không có sự hướng tâm cũng không có sự duy trì tâm",
    "rūpā": "là vật chất", "arūpā": "là phi vật chất",
    "lokiyā": "thuộc thế gian", "lokuttarā": "vượt thế gian",
    "sārammaṇā": "có đối tượng", "anārammaṇā": "không có đối tượng",
    "sārammaṇārammaṇā": "lấy những gì có đối tượng làm đối tượng",
    "anārammaṇārammaṇā": "lấy những gì không có đối tượng làm đối tượng",
    "pariyāpannā": "nằm trong các cõi tồn tại", "apariyāpannā": "không nằm trong các cõi tồn tại",
}
PLANE = {"kāmadhātu": "cõi dục lạc", "rūpadhātu": "cõi hình sắc", "arūpadhātu": "cõi không hình sắc"}
for _pl, _vi in PLANE.items():
    CLAUSE[f"{_pl}pariyāpannā"] = f"nằm trong {_vi}"
    CLAUSE[f"na {_pl}pariyāpannā"] = f"không nằm trong {_vi}"
ITEM = {   # one gerundive / participle: (positive, negated with na)
    "abhiññeyyā": ("cần được hiểu biết trực tiếp", "không cần được hiểu biết trực tiếp"),
    "pariññeyyā": ("cần được hiểu biết trọn vẹn", "không cần được hiểu biết trọn vẹn"),
    "pahātabbā": ("cần dứt bỏ", "không cần dứt bỏ"),
    "bhāvetabbā": ("cần được tu tập", "không cần được tu tập"),
    "sacchikātabbā": ("cần được tự mình chứng nghiệm", "không cần được tự mình chứng nghiệm"),
    "diṭṭhā": ("được thấy", "không được thấy"), "sutā": ("được nghe", "không được nghe"),
    "mutā": ("được cảm nhận", "không được cảm nhận"), "viññātā": ("được nhận biết", "không được nhận biết"),
}
SAY = "không nên nói rằng"                    # na vattabbo X-tipi (no dash in ch. 18; ch. 7-9 «không nên nói rằng “X”»)


def nw(w):
    """gender/number of a predicate word normalised to the masculine plural"""
    p = w[-1] if w[-1] in ",;." else ""
    w = w[:-1] if p else w
    for a, b in (("antipi", "ātipi"), ("otipi", "ātipi"), ("ātipi", "ātipi"), ("āni", "ā"), ("aṃ", "ā"), ("o", "ā")):
        if w.endswith(a):
            return w[: -len(a)] + b + p
    return w + p


def norm_pred(p):
    return " ".join(nw(w) for w in p.split())


def items(content):
    """«abhiññeyyā pariññeyyā na pahātabbā …» -> Vietnamese, all-negative?, all-positive?"""
    out, neg = [], False
    for w in content.split():
        if w == "na":
            neg = True
            continue
        out.append((neg, ITEM[w][1 if neg else 0]))
        neg = False
    vis = [v for _, v in out]
    if len(out) >= 2 and out[-1][0] and out[-2][0]:
        text = ", ".join(vis[:-1]) + " cũng " + vis[-1]
    else:
        text = ", ".join(vis)
    return text, all(x for x, _ in out), not any(x for x, _ in out)


def predicate(p, subj_vi):
    """the predicate p (Pāli, final punctuation removed) of a sentence whose subject is subj_vi"""
    p = norm_pred(p)
    groups = p.split(", ")
    out, prev_neg, i = [], False, 0
    while i < len(groups):
        g = groups[i]
        siya = g.startswith("siyā ")
        c = g[5:] if siya else g
        tail = ""
        if c.endswith(" 4"):                                             # ^2-1041 stray digit, kept
            c, tail = c[:-2], " 4"
        if c.startswith("na vattabbā "):
            qs = [c[len("na vattabbā "):]] + groups[i + 1:]
            assert all(x.endswith("ātipi") for x in qs), qs
            v = f"{SAY} " + ", hay rằng ".join(f"“{CLAUSE[x[:-4]]}”" for x in qs)
            if siya:
                out.append("đôi khi " + v)
            elif not out:
                return None, f"Về {low(subj_vi)} thì {v}"
            else:
                raise ValueError(p)
            break
        lr = low(g)
        sk = next((k for k in SUBJ_KEYS if lr.startswith(k + " ")), None)
        if sk and out:                                                   # a new subject after a comma
            sv, rest = subject(g)
            pv, whole = predicate(rest, sv)
            assert whole is None
            out.append(f"{sv} {pv}")
            i += 1
            continue
        if c in CLAUSE:
            v, allneg, allpos = CLAUSE[c], False, True
        else:
            v, allneg, allpos = items(c)
        v += tail
        if siya:
            v = "đôi khi " + v
        elif prev_neg and allpos and out:
            v = "nhưng " + v
        out.append(v)
        prev_neg = allneg
        i += 1
    return ", ".join(out), None


FIX = [   # source slips repaired before parsing (missing punctuation / words written apart), reported
    ("kāmadhātu pariyāpanno", "kāmadhātupariyāpanno",
     "^2-1000 «siyā kāmadhātu pariyāpanno» written apart (= kāmadhātupariyāpanno), rendered as meant"),
    ("sampayuttoti pi,", "sampayuttotipi,", "^2-1039 «sampayuttoti pi» written apart (= sampayuttotipi)"),
    ("sārammaṇārammaṇo siyā", "sārammaṇārammaṇo, siyā", "^2-1035 «siyā sārammaṇārammaṇo siyā …»: comma missing"),
    ("siyā vipākā siyā vipākadhammadhammā", "siyā vipākā, siyā vipākadhammadhammā",
     "^2-1040 «Dve dhātuyo siyā vipākā siyā vipākadhammadhammā»: comma missing"),
    ("avitakkaavicāro siyā na","avitakkaavicāro, siyā na", "^2-1042 «… siyā avitakkaavicāro siyā na vattabbo»: "
     "comma missing"),
    ("avitakkaavicārā manodhātu", "avitakkaavicārā, manodhātu", "^2-1042 «… pañca cittā avitakkaavicārā "
     "manodhātu savitakkasavicārā»: punctuation missing between two statements (rendered with a comma)"),
    ("satta cetanā satta cittā", "satta cetanā… satta cittā", "^2-1043 «satta cetanā satta cittā»: the «…» of the "
     "run is missing (rendered with «…»)"),
]


OVR = {   # identical subject and predicate words: «thì» keeps the sentence readable
    "Tayo abyākatahetū abyākatā.": f"Ba {HETU_ABY} thì không xác định về mặt đạo đức.",
}


def T(line):
    """one Pāli line of a question section -> Vietnamese, sentence by sentence"""
    line = line.replace("siyā lokuttarāti.", "siyā lokuttarā.")       # ^2-1044 closing iti of the run (no word)
    for a, b, msg in FIX:
        if a in line:
            line = line.replace(a, b)
            slip(msg)
    out = []
    for s in re.split(r"(?<=[.?;])\s+", line.strip()):
        vi = OVR.get(s) or V(s, required=False)
        if vi is None:
            end = s[-1]
            assert end in ".;?", s
            sv, rest = subject(s[:-1])
            assert sv, s
            pv, whole = predicate(rest, sv)
            vi = (whole if whole else f"{sv} {pv}") + end
            PARSED.append((s, vi))
        out.append(vi)
    return " ".join(out)


# =========================================================================== lists and frames
L_KH5 = ", ".join(KHANDHA.values())                                                  # S.FIVE_LIST
L_AY12 = ", ".join(AYAT[k] for k in ["cakkh", "rūp", "sot", "sadd", "ghān", "gandh", "jivh", "ras", "kāy",
                                       "phoṭṭhabb", "man", "dhamm"])                  # pi-2 ch. 2
L_DH18 = ", ".join(DHATU[k] for k in ["cakkhu", "rūpa", "cakkhuviññāṇa", "sota", "sadda", "sotaviññāṇa", "ghāna",
                                        "gandha", "ghānaviññāṇa", "jivhā", "rasa", "jivhāviññāṇa", "kāya",
                                        "phoṭṭhabba", "kāyaviññāṇa", "mano", "dhamma", "manoviññāṇa"])  # pi-2 ch. 3
IN22 = ["cakkhu", "sot", "ghān", "jivh", "kāy", "man", "itth", "puris", "jīvit", "sukh", "dukkh", "somanass",
        "domanass", "upekkh", "saddh", "vīriy", "sat", "samādh", "paññ", "anaññātaññassāmīt", "aññ", "aññātāv"]
L_IN22 = ", ".join(INDR[k] for k in IN22)                                             # pi-2 ch. 5


def ilist(keys):
    """an indriya list; «itth|puris» and «somanass|upekkh» are the «… vā … vā» pairs"""
    out = []
    for k in keys:
        if "|" in k:
            a, b = k.split("|")
            out.append(f"{INDR[a]} hoặc {INDR[b]}")
        else:
            out.append(INDR[k])
    return ", ".join(out)


def L7(noun=None):
    """the seven contacts / feelings / perceptions / intentions (noun None = the contacts themselves)"""
    if noun is None:
        return ", ".join(phassa(d) for d in SEVEN)
    return ", ".join(born(noun, d) for d in SEVEN)


L_SC4 = ", ".join(SACCA[k] for k in ["dukkha", "samudaya", "nirodha", "magga"])
L_AH4 = ", ".join([FOOD] + AHARA3)
L_CI7 = ", ".join(CITTA7)
PI1_ABY = None                       # set in pi1_strings(): «Sự không tham lam … mang tính chức năng»


def tq(x):
    return f"Ở đây, {x} là những gì?"             # Tattha katame/katamāni/katamā N X? (counted, user decision)


def tq1(x):
    return f"Ở đây, {x} là gì?"                   # PI1 Tattha katamo/katamā/katamaṃ X?


def these(x, quoted=True):
    """– ime/imāni/imā vuccanti "X".  ->  «– những điều này được gọi là “X”.»  (S.CALLED_PL)"""
    return f"– {S.CALLED_PL} “{x}”." if quoted else f"– {S.CALLED_PL} {x}."


def that(x):
    """– ayaṃ/idaṃ vuccati "X".  ->  «– đó được gọi là “X”.»  (S.CALLED_SG)"""
    return f"– {S.CALLED_SG} “{x}”."


def is_these(x):
    """– ime tayo kusalahetū.  ->  «– đó là ba gốc rễ thiện.»  (PI1 ^1-1068)"""
    return f"– đó là {x}."


def head(level, text, bid):
    assert PS[bid][0].startswith("#" * level + " "), bid
    return S.H(level, text, bid)


def seg(bid, lines):
    assert len(lines) == len(PS[bid]), (bid, len(lines), len(PS[bid]))
    for p, v in zip(PS[bid], lines):
        assert p.count("–") == v.count("–"), (bid, p, v)
    return (lines, bid)


def pi1_line(fname, bid):
    """the approved pi-1 Vietnamese line ending in ^bid (read-only), without the ID"""
    for ln in (PI1_VI / fname).read_text(encoding="utf-8").split("\n"):
        if ln.rstrip().endswith(f"^{bid}"):
            PI1_USED.append((f"pi-1/{fname}", f"^{bid}"))
            return IDRX.sub("", ln)
    raise KeyError(bid)


# =========================================================================== headings
HEAD = {
    "2-18-0": (3, S.CH_HEADINGS["Dhammahadayavibhaṅgo"]),
    "2-18-1-0": (4, "Mục bao gồm tất cả"),                                         # Sabbasaṅgāhikavāro (new)
    "2-18-2-0": (4, "Mục về những gì sinh khởi và không sinh khởi"),               # Uppattānuppattivāro (tb)
    "2-18-2-1-0": (5, "Cõi dục lạc"), "2-18-2-2-0": (5, "Cõi hình sắc"),          # Kāmadhātu, Rūpadhātu (tb plane)
    "2-18-2-3-0": (5, "Cõi không hình sắc"),                                       # Arūpadhātu (tb)
    "2-18-2-4-0": (5, "Không nằm trong các cõi tồn tại"),                          # Apariyāpannaṃ (tb)
    "2-18-3-0": (4, "Mục về những gì nằm trong và không nằm trong các cõi tồn tại"),  # Pariyāpannāpariyāpannavāro
    "2-18-3-1-0": (5, "Cõi dục lạc"), "2-18-3-2-0": (5, "Cõi hình sắc"), "2-18-3-3-0": (5, "Cõi không hình sắc"),
    "2-18-3-4-0": (5, "Nằm trong và không nằm trong các cõi tồn tại"),             # Pariyāpannāpariyāpannaṃ (new)
    "2-18-4-0": (4, "Mục trình bày các hiện tượng"),                               # Dhammadassanavāro (new)
    "2-18-4-1-0": (5, "Cõi dục lạc"), "2-18-4-2-0": (5, "Cõi hình sắc"),
    "2-18-4-3-0": (5, "Chúng sinh Vô Tưởng"),                                      # Asaññasattā (tb asaññasatta)
    "2-18-4-4-0": (5, "Cõi không hình sắc"),
    "2-18-5-0": (4, "Mục trình bày sự khác biệt giữa các cõi"),                    # Bhūmantaradassanavāro (tb)
    "2-18-6-0": (4, "Mục về nghiệp tạo ra sự tái sinh và tuổi thọ"),               # Uppādakakammaāyuppamāṇavāro
    "2-18-6-1-0": (5, "Nghiệp tạo ra sự tái sinh"),                                # Uppādakakammaṃ (tb)
    "2-18-6-2-0": (5, "Tuổi thọ"),                                                 # Āyuppamāṇaṃ (tb)
    "2-18-7-0": (4, "Mục về những gì cần được hiểu biết trực tiếp và các điều khác"),   # Abhiññeyyādivāro (tb)
    "2-18-8-0": (4, "Mục về những gì có đối tượng và không có đối tượng"),         # Sārammaṇānārammaṇavāro (tb)
    "2-18-9-0": (4, "Mục trình bày những gì được thấy được nghe và các điều khác"),    # Diṭṭhasutādidassanavāro (tb)
    "2-18-10-0": (4, "Mục trình bày các bộ ba và các bộ khác"),                    # Tikādidassanavāro (tb)
    "2-18-10-1-0": (5, "Bộ ba về thiện"),                                          # Kusalattikaṃ (Tikaṃ «bộ ba»)
    "2-18-10-2-0": (5, "Bộ ba về cảm giác"),                                       # Vedanātikaṃ
    "2-18-10-3-0": (5, "Bộ ba về quả của nghiệp"),                                 # Vipākattikaṃ (tb)
    "2-18-10-4-0": (5, "Bộ ba về những gì do nghiệp tạo ra"),                      # Upādinnattikaṃ
    "2-18-10-5-0": (5, "Bộ ba về sự hướng tâm"),                                   # Vitakkattikaṃ
    "2-18-10-6-0": (5, "(1) Bộ đôi về vật chất"),                                  # (1) Rūpadukaṃ (Dukaṃ «bộ đôi»)
    "2-18-10-7-0": (5, "(2) Bộ đôi về thế gian"),                                  # (2) Lokiyadukaṃ
}


# =========================================================================== the counts (^2-978 … ^2-998)
KATI = [f"bao nhiêu {c}" for c in CATS]


def kati_q(prefix, upto=None):
    """kati khandhā, kati āyatanāni, …[…pe…] kati cittāni?  (upto = index after which «…» skips to the last)"""
    if upto is None:
        body = ", ".join(KATI)
    else:
        body = ", ".join(KATI[:upto]) + "… " + KATI[-1]
    return f"{prefix} có {body}?" if prefix else cap(f"có {body}?")


def counts(nums):
    return ", ".join(f"{NUMW[a]} {c}" for a, c in zip(nums, CATS))


ALL12 = ["pañca", "dvādasa", "aṭṭhārasa", "cattāri", "bāvīsati", "nava", "cattāro", "satta", "satta", "satta",
         "satta", "satta"]


def seg_978():
    return seg("2-978", [kati_q(None), cap(counts(ALL12)) + "."])


def seg_979_990():
    out = [
        seg("2-979", [f"{tq('năm khối')} {cap(L_KH5)} {these('năm khối')}"]),
        seg("2-980", [f"{tq('mười hai lĩnh vực nhận biết')} {cap(L_AY12)} {these('mười hai lĩnh vực nhận biết')}"]),
        seg("2-981", [f"{tq('mười tám yếu tố')} {cap(L_DH18)} {these('mười tám yếu tố')}"]),
        seg("2-982", [f"{tq('bốn sự thật')} {cap(L_SC4)} {these('bốn sự thật')}"]),
        seg("2-983", [f"{tq('hai mươi hai năng lực')} {cap(L_IN22)} {these('hai mươi hai năng lực')}"]),
        seg("2-984", [hetu9_q(), hetu3("kusala"), hetu3("akusala"),
                      f"{V('Tattha katame tayo abyākatahetū?')} {PI1_ABY} {is_these('ba ' + HETU_ABY)} "
                      f"Những điều này được gọi là “chín gốc rễ”."]),
        seg("2-985", [f"{tq('bốn loại dưỡng chất')} {cap(FOOD)} {S.spell('Sī., Syā.', 'kabaḷiṃkāro āhāro')}, "
                      f"{', '.join(AHARA3)} {these('bốn loại dưỡng chất')}"]),
        seg("2-986", [f"{tq('bảy loại tiếp xúc')} {cap(L7())} {these('bảy loại tiếp xúc')}"]),
        seg("2-987", [f"{tq('bảy loại cảm giác')} {cap(L7('cảm giác'))} {these('bảy loại cảm giác')}"]),
        seg("2-988", [f"{tq('bảy loại tri giác')} {cap(L7('tri giác'))} {these('bảy loại tri giác')}"]),
        seg("2-989", [f"{tq('bảy loại chủ ý')} {cap(L7('chủ ý'))} {these('bảy loại chủ ý')}"]),
        seg("2-990", [f"{tq('bảy loại tâm')} {cap(L_CI7)} {these('bảy loại tâm')}"]),
    ]
    return out


def hetu9_q(loc=""):
    """Tattha katame [loc] nava hetū? Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū."""
    return f"{tq('chín gốc rễ' + loc)} {V('Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū.')}"


def hetu3(kind, two=False):
    """Tattha katame tayo/dve (a)kusalahetū? Alobho kusalahetu, … – ime tayo/dve (a)kusalahetū."""
    vi_kind = HETU_K if kind == "kusala" else HETU_A
    roots = ROOT_K if kind == "kusala" else ROOT_A
    if two:                                                                  # lobho, moho
        roots = [ROOT_A[0], ROOT_A[2]]
    num = "hai" if two else "ba"
    q = tq(f"{num} {vi_kind}") if two else V(f"Tattha katame tayo {kind}hetū?")
    body = cap(", ".join(hetu(r, vi_kind) for r in roots))
    return f"{q} {body} {is_these(f'{num} {vi_kind}')}"


_ABY = pi1_line("4-01-nikkhepakandam.md", "1-1068")                          # PI1 ^1-1068
PI1_ABY = _ABY.split(" là những gì? ", 1)[1].rsplit(" – đó là", 1)[0]        # Kusalānaṃ vā … alobho adoso amoho
PI1_ABY_K = PI1_ABY.split(" hoặc ", 1)[0]                                     # Kusalānaṃ dhammānaṃ vipākato alobho …
LOC = {"k": "trong cõi dục lạc", "r": "trong cõi hình sắc", "a": "trong cõi không hình sắc",
       "ap": "thuộc phạm vi không nằm trong các cõi tồn tại"}                  # Kāmadhātuyā … / Apariyāpanne
QPRE = {"k": "Trong cõi dục lạc", "r": "Trong cõi hình sắc", "a": "Trong cõi không hình sắc",
        "ap": "Trong phạm vi không nằm trong các cõi tồn tại"}
SAC3 = ", ".join(SACCA[k] for k in ["dukkha", "samudaya", "magga"])
HETU_8 = f"Ba {HETU_K}, hai {HETU_A}, ba {HETU_ABY}"                          # Tayo kusalahetū, dve akusalahetū, …


def dl(cnt, pl, body, noun_end=True):
    """Tattha katame <pl> N X? <body> – ime vuccanti "<pl> N X"."""
    x = f"{cnt} {LOC[pl]}"
    return f"{tq(x)} {cap(body)} {these(x)}"


def ekam(pl):
    """Tattha katamā <pl> ekā vedanā…pe… ekā saññā…pe… ekā cetanā…pe… ekaṃ cittaṃ? Manoviññāṇadhātu – idaṃ vuccati"""
    x = "một loại cảm giác… một loại tri giác… một loại chủ ý… một loại tâm " + LOC[pl]
    return f"{tq1(x)} {cap(DHATU['manoviññāṇa'])} {that('một loại tâm ' + LOC[pl])}"


def eko_phasso(pl):
    x = f"một loại tiếp xúc {LOC[pl]}"
    return f"{tq1(x)} {cap(phassa('manoviññāṇadhātu'))} {that(x)}"


def seg_991_998():
    k, r, a, ap = "k", "r", "a", "ap"
    out = [head(*HEAD["2-18-2-1-0"], "2-18-2-1-0")]
    out.append(seg("2-991", [kati_q(QPRE[k]), f"{QPRE[k]} có " + counts(
        ["pañca", "dvādasa", "aṭṭhārasa", "tīṇi", "bāvīsati", "nava", "cattāro", "satta", "satta", "satta", "satta",
         "satta"]) + "."]))
    slip("^2-992 «Cakkhusamphasso sotasamphasso, …»: comma missing between the first two items (rendered as two items)")
    slip("^2-992 «imā vuccatti» (for vuccanti): spelling slip, rendered as meant")
    out.append(seg("2-992", [
        dl("năm khối", k, L_KH5), dl("mười hai lĩnh vực nhận biết", k, L_AY12), dl("mười tám yếu tố", k, L_DH18),
        dl("ba sự thật", k, SAC3),
        dl("hai mươi hai năng lực", k, f"{INDR['cakkhu']}, {INDR['sot']}… {INDR['aññātāv']}"),
        f"{tq('chín gốc rễ ' + LOC[k])} Ba {HETU_K}, ba {HETU_A}, ba {HETU_ABY}… "
        f"{S.CALLED_PL} “chín gốc rễ {LOC[k]}”.",
        dl("bốn loại dưỡng chất", k, L_AH4), dl("bảy loại tiếp xúc", k, L7()),
        dl("bảy loại cảm giác", k, L7("cảm giác")), dl("bảy loại tri giác", k, L7("tri giác")),
        dl("bảy loại chủ ý", k, L7("chủ ý")), dl("bảy loại tâm", k, L_CI7)]))
    out.append(S.H(5, HEAD["2-18-2-2-0"][1], "2-18-2-2-0"))
    out.append(seg("2-993", [kati_q(QPRE[r], upto=5), f"{QPRE[r]} có " + counts(
        ["pañca", "cha", "nava", "tīṇi", "cuddasa", "aṭṭha", "tayo", "cattāro", "catasso", "catasso", "catasso",
         "cattāri"]) + "."]))
    slip("^2-993 «kati āyatanā» (for āyatanāni, as in ^2-978): same meaning, rendered as the other questions")
    slip("^2-994 «Ime vuccanti rūpadhātuyā aṭṭha hetū.» has no quotation marks (kept without them)")
    out.append(seg("2-994", [
        dl("năm khối", r, L_KH5),
        dl("sáu lĩnh vực nhận biết", r, ", ".join(AYAT[x] for x in ["cakkh", "rūp", "sot", "sadd", "man", "dhamm"])),
        dl("chín yếu tố", r, ", ".join(DHATU[x] for x in ["cakkhu", "rūpa", "cakkhuviññāṇa", "sota", "sadda",
                                                          "sotaviññāṇa", "mano", "dhamma", "manoviññāṇa"])),
        dl("ba sự thật", r, SAC3),
        dl("mười bốn năng lực", r, ilist(["cakkhu", "sot", "man", "jīvit", "somanass", "upekkh", "saddh", "vīriy",
                                           "sat", "samādh", "paññ", "anaññātaññassāmīt", "aññ", "aññātāv"])),
        f"{tq('tám gốc rễ ' + LOC[r])} {HETU_8}.",
        hetu3("kusala"), hetu3("akusala", two=True),
        f"{V('Tattha katame tayo abyākatahetū?')} {PI1_ABY} {is_these('ba ' + HETU_ABY)} "
        f"{cap(S.CALLED_PL)} tám gốc rễ {LOC[r]}.",
        dl("ba loại dưỡng chất", r, ", ".join(AHARA3)),
        dl("bốn loại tiếp xúc", r, ", ".join(phassa(d) for d in ["cakkhu", "sota", "manodhātu", "manoviññāṇadhātu"])),
        f"{tq('bốn loại cảm giác… bốn loại tri giác… bốn loại chủ ý… bốn loại tâm ' + LOC[r])} "
        f"{cap(', '.join([CITTA7[0], CITTA7[1], CITTA7[5], CITTA7[6]]))} {these('bốn loại tâm ' + LOC[r])}"]))
    out.append(S.H(5, HEAD["2-18-2-3-0"][1], "2-18-2-3-0"))
    one5 = ["eka"] * 5
    out.append(seg("2-995", [kati_q(QPRE[a], upto=1), f"{QPRE[a]} có " + counts(
        ["cattāro", "dve", "dve", "tīṇi", "ekādasa", "aṭṭha", "tayo"] + one5) + "."]))
    K4 = ", ".join(KHANDHA[x] for x in ["vedanā", "saññā", "saṅkhāra", "viññāṇa"])
    A2 = f"{AYAT['man']}, {AYAT['dhamm']}"
    D2 = f"{DHATU['manoviññāṇa']}, {DHATU['dhamma']}"
    out.append(seg("2-996", [
        dl("bốn khối", a, K4), dl("hai lĩnh vực nhận biết", a, A2), dl("hai yếu tố", a, D2), dl("ba sự thật", a, SAC3),
        dl("mười một năng lực", a, ilist(["man", "jīvit", "somanass", "upekkh", "saddh", "vīriy", "sat", "samādh",
                                          "paññ", "aññ", "aññātāv"])),
        f"{tq('tám gốc rễ ' + LOC[a])} {HETU_8}… {S.CALLED_PL} “tám gốc rễ {LOC[a]}”.",
        dl("ba loại dưỡng chất", a, ", ".join(AHARA3)), eko_phasso(a), ekam(a)]))
    out.append(S.H(5, HEAD["2-18-2-4-0"][1], "2-18-2-4-0"))
    out.append(seg("2-997", [kati_q(QPRE[ap], upto=1), f"{QPRE[ap]} có " + counts(
        ["cattāro", "dve", "dve", "dve", "dvādasa", "cha", "tayo"] + one5) + "."]))
    out.append(seg("2-998", [
        dl("bốn khối", ap, K4), dl("hai lĩnh vực nhận biết", ap, A2), dl("hai yếu tố", ap, D2),
        dl("hai sự thật", ap, f"{SACCA['magga']}, {SACCA['nirodha']}"),
        dl("mười hai năng lực", ap, ilist(["man", "jīvit", "somanass", "upekkh", "saddh", "vīriy", "sat", "samādh",
                                           "paññ", "anaññātaññassāmīt", "aññ", "aññātāv"])),
        f"{tq('sáu gốc rễ ' + LOC[ap])} Ba {HETU_K}, ba {HETU_ABY}.",
        hetu3("kusala"),
        f"{V('Tattha katame tayo abyākatahetū?')} {PI1_ABY_K} {is_these('ba ' + HETU_ABY)} "
        f"{cap(S.CALLED_PL)} “sáu gốc rễ {LOC[ap]}”.",
        dl("ba loại dưỡng chất", ap, ", ".join(AHARA3)), eko_phasso(ap), ekam(ap)]))
    return out


# =========================================================================== included / not included (^2-999 … ^2-1006)
def qcount(preds, first="Trong năm khối", last="trong bảy loại tâm"):
    """Pañcannaṃ khandhānaṃ kati X, kati Y…pe… sattannaṃ cittānaṃ kati X, kati Y?"""
    a = ", ".join(f"bao nhiêu khối {p}" for p in preds)
    b = ", ".join(f"bao nhiêu loại {p}" for p in preds)
    return f"{first}, {a}… {last}, {b}?"


def seg_999_1006():
    out = []
    for (qbid, abid, hbid), (pos, neg) in zip(
            [("2-999", "2-1000", "2-18-3-1-0"), ("2-1001", "2-1002", "2-18-3-2-0"),
             ("2-1003", "2-1004", "2-18-3-3-0"), ("2-1005", "2-1006", "2-18-3-4-0")],
            [(CLAUSE["kāmadhātupariyāpannā"], CLAUSE["na kāmadhātupariyāpannā"]),
             (CLAUSE["rūpadhātupariyāpannā"], CLAUSE["na rūpadhātupariyāpannā"]),
             (CLAUSE["arūpadhātupariyāpannā"], CLAUSE["na arūpadhātupariyāpannā"]),
             (CLAUSE["pariyāpannā"], CLAUSE["apariyāpannā"])]):
        out.append(head(*HEAD[hbid], hbid))
        out.append(seg(qbid, [qcount([pos, neg])]))
        out.append(seg(abid, [T(ln) for ln in PS[abid]]))
    return out


# =========================================================================== rebirth (^2-1007 … ^2-1019)
AT = {p: f"{QPRE[p]}, vào khoảnh khắc tái sinh," for p in ("k", "r", "a")}   # Kāmadhātuyā upapattikkhaṇe
ALL_B, SOME_B = "ở tất cả chúng sinh", "ở một số chúng sinh"                # sabbesaṃ (tb Sabba) / kassaci
DEV_K = "chư thiên thuộc cõi dục lạc"                                        # Kāmāvacarānaṃ devānaṃ
MAN1 = "loài người thuộc kiếp đầu tiên"                                      # paṭhamakappikānaṃ manussānaṃ
OPA = "ngạ quỷ hóa sinh, a-tu-la hóa sinh, loài súc sinh hóa sinh"            # opapātikānaṃ petānaṃ … tiracchānagatānaṃ
NER = "chúng sinh địa ngục"                                                  # nerayikānaṃ
GAB = "chúng sinh sinh ra từ bào thai"                                       # Gabbhaseyyakānaṃ sattānaṃ
FULL = "có đầy đủ các lĩnh vực nhận biết"                                    # paripuṇṇāyatanānaṃ
BLIND, DEAF, BLIND_DEAF = "mù bẩm sinh", "điếc bẩm sinh", "mù và điếc bẩm sinh"   # jacc-andha / -badhira
ROOT_W, ROOT_KN = "có gốc rễ", "có gốc rễ, gắn liền với hiểu biết"          # sahetukānaṃ ñāṇasampayuttānaṃ
ROOT_KV = "có gốc rễ, không gắn liền với hiểu biết"                         # sahetukānaṃ ñāṇavippayuttānaṃ
NOROOT = "không có gốc rễ"                                                   # ahetukānaṃ / ahetukā
HELL4 = f"{OPA}, {NER}"


def who(*parts):
    return "Ở " + ", ".join(parts) + ","


def kassa_line(pl, what, aparam, beings, what_body, lst):
    """Kāmadhātuyā upapattikkhaṇe kassa [aparāni] N X pātubhavanti? <beings> upapattikkhaṇe N X pātubhavanti – <lst>.
    Kāmadhātuyā upapattikkhaṇe etesaṃ imāni N X pātubhavanti."""
    q = f"{AT[pl]} {what}{' khác' if aparam else ''} xuất hiện ở những chúng sinh nào?"
    a = f"{beings} vào khoảnh khắc tái sinh, {what_body} xuất hiện – {lst}."
    c = f"{AT[pl]} {what} này xuất hiện ở những chúng sinh ấy."
    return f"{q} {a} {c}"


def ay_list(keys):
    return ", ".join(AYAT[x] for x in keys)


def dh_list(keys):
    return ", ".join(DHATU[x] for x in keys)


EVERY = ("một loại cảm giác… một loại tri giác… một loại chủ ý… một loại tâm")   # ekā vedanā… ekā saññā… … ekaṃ cittaṃ


def sabbesam_q(pl, what, sg=False, all_b=True, end="?"):
    """[Kāmadhātuyā] upapattikkhaṇe [sabbesaṃ] katame N X pātubhavanti?"""
    x = f"{what} xuất hiện{' ' + ALL_B if all_b else ''}"
    return f"{AT[pl]} {x} {'là gì' if sg else 'là những gì'}{end}"


def sabbesam_c(pl, what, all_b=True):
    """– kāmadhātuyā upapattikkhaṇe [sabbesaṃ] ime N X pātubhavanti."""
    return f"– {low(AT[pl])} {what} này xuất hiện{' ' + ALL_B if all_b else ''}."


def def_rebirth(pl, what, body, sg=False, all_b=True, end="?", closing_what=None):
    return (f"{sabbesam_q(pl, what, sg, all_b, end)} {cap(body)} "
            f"{sabbesam_c(pl, closing_what or what, all_b)}")


def seg_1007_1019():
    k, r, a = "k", "r", "a"
    out = [head(*HEAD["2-18-4-0"], "2-18-4-0"), head(*HEAD["2-18-4-1-0"], "2-18-4-1-0")]
    q = f"{AT[k]} có bao nhiêu khối xuất hiện… bao nhiêu loại tâm xuất hiện?"
    parts = [f"{ALL_B}, năm khối xuất hiện"]
    for x in ["mười một lĩnh vực nhận biết", "mười lĩnh vực nhận biết", "mười lĩnh vực nhận biết khác",
              "chín lĩnh vực nhận biết", "bảy lĩnh vực nhận biết", "mười một yếu tố", "mười yếu tố", "mười yếu tố khác",
              "chín yếu tố", "bảy yếu tố"]:
        parts.append(f"{SOME_B}, {x} xuất hiện")
    parts.append(f"{ALL_B}, một sự thật xuất hiện")
    for x in ["mười bốn năng lực", "mười ba năng lực", "mười ba năng lực khác", "mười hai năng lực", "mười năng lực",
              "chín năng lực", "chín năng lực khác", "tám năng lực", "tám năng lực khác", "bảy năng lực",
              "năm năng lực", "bốn năng lực", "ba gốc rễ", "hai gốc rễ"]:
        parts.append(f"{SOME_B}, {x} xuất hiện")
    parts.append(f"{SOME_B} {S.reading('Syā.', 'keci')}, những gì xuất hiện đều {NOROOT}")
    parts.append(f"{ALL_B}, bốn loại dưỡng chất xuất hiện")
    parts.append(f"{ALL_B}, một loại tiếp xúc xuất hiện")
    parts.append(f"{ALL_B}, {EVERY} xuất hiện")
    out.append(seg("2-1007", [q, f"{AT[k]} " + "; ".join(parts) + "."]))
    out.append(seg("2-1008", [def_rebirth(k, "năm khối", f"{KHANDHA['rūpa']}… {KHANDHA['viññāṇa']}")]))
    # ^2-1009 sense bases
    A11 = ["cakkh", "rūp", "sot", "ghān", "gandh", "jivh", "ras", "kāy", "phoṭṭhabb", "man", "dhamm"]
    b_full = who(DEV_K, MAN1, OPA, NER, FULL)
    b_blind, b_deaf, b_bd = who(HELL4, BLIND), who(HELL4, DEAF), who(HELL4, BLIND_DEAF)
    b_gab = who(GAB)
    slip("^2-1009 / 1010 / 1012 «opapātikānaṃ tiracchānagatānaṃ nerayikānaṃ»: comma missing before nerayikānaṃ "
         "(present in the first list; rendered as a list item)")
    out.append(seg("2-1009", [
        kassa_line(k, "mười một lĩnh vực nhận biết", False, b_full, "mười một lĩnh vực nhận biết", ay_list(A11)),
        kassa_line(k, "mười lĩnh vực nhận biết", False, b_blind, "mười lĩnh vực nhận biết", ay_list(A11[1:])),
        kassa_line(k, "mười lĩnh vực nhận biết", True, b_deaf, "mười lĩnh vực nhận biết",
                   ay_list(["cakkh", "rūp"] + A11[3:])),
        kassa_line(k, "chín lĩnh vực nhận biết", False, b_bd, "chín lĩnh vực nhận biết", ay_list(["rūp"] + A11[3:])),
        kassa_line(k, "bảy lĩnh vực nhận biết", False, b_gab, "bảy lĩnh vực nhận biết",
                   ay_list(["rūp", "gandh", "ras", "kāy", "phoṭṭhabb", "man", "dhamm"]))]))
    D11 = ["cakkhu", "rūpa", "sota", "ghāna", "gandha", "jivhā", "rasa", "kāya", "phoṭṭhabba", "manoviññāṇa", "dhamma"]
    out.append(seg("2-1010", [
        kassa_line(k, "mười một yếu tố", False, b_full, "mười một yếu tố", dh_list(D11)),
        kassa_line(k, "mười yếu tố", False, b_blind, "mười yếu tố", dh_list(D11[1:])),
        kassa_line(k, "mười yếu tố", True, b_deaf, "mười yếu tố", dh_list(["cakkhu", "rūpa"] + D11[3:])),
        kassa_line(k, "chín yếu tố", False, b_bd, "chín yếu tố", dh_list(["rūpa"] + D11[3:])),
        kassa_line(k, "bảy yếu tố", False, b_gab, "bảy yếu tố",
                   dh_list(["rūpa", "gandha", "rasa", "kāya", "phoṭṭhabba", "manoviññāṇa", "dhamma"]))]))
    out.append(seg("2-1011", [f"{sabbesam_q(k, 'một sự thật', sg=True)} {cap(SACCA['dukkha'])} "
                              f"{sabbesam_c(k, 'một sự thật')}"]))
    # ^2-1012 faculties
    FIVE_S = ["cakkhu", "sot", "ghān", "jivh", "kāy", "man"]
    SEX, FEEL = "itth|puris", "somanass|upekkh"
    FAITH5 = ["saddh", "vīriy", "sat", "samādh", "paññ"]
    I14 = FIVE_S + [SEX, "jīvit", FEEL] + FAITH5
    I13 = FIVE_S + [SEX, "jīvit", FEEL] + FAITH5[:4]
    I13b = FIVE_S + ["jīvit", FEEL] + FAITH5
    I12 = FIVE_S + ["jīvit", FEEL] + FAITH5[:4]
    I10 = ["kāy", "man", SEX, "jīvit", FEEL] + FAITH5
    I9 = ["kāy", "man", SEX, "jīvit", FEEL] + FAITH5[:4]
    I9b = FIVE_S + [SEX, "jīvit", "upekkh"]
    I8 = ["sot", "ghān", "jivh", "kāy", "man", SEX, "jīvit", "upekkh"]
    I8b = ["cakkhu", "ghān", "jivh", "kāy", "man", SEX, "jīvit", "upekkh"]
    I7 = ["ghān", "jivh", "kāy", "man", SEX, "jīvit", "upekkh"]
    I5 = ["kāy", "man", SEX, "jīvit", "upekkh"]
    I4 = ["kāy", "man", "jīvit", "upekkh"]
    slip("^2-1012 «… kāyindriyaṃ manindriyaṃ …» (aparāni aṭṭhindriyāni): comma missing (rendered as two items)")
    out.append(seg("2-1012", [
        kassa_line(k, "mười bốn năng lực", False, who(DEV_K, ROOT_KN), "mười bốn năng lực", ilist(I14)),
        kassa_line(k, "mười ba năng lực", False, who(DEV_K, ROOT_KV), "mười ba năng lực", ilist(I13)),
        kassa_line(k, "mười ba năng lực", True, who(MAN1, ROOT_KN), "mười ba năng lực", ilist(I13b)),
        kassa_line(k, "mười hai năng lực", False, who(MAN1, ROOT_KV), "mười hai năng lực", ilist(I12)),
        kassa_line(k, "mười năng lực", False, who(GAB, ROOT_KN), "mười năng lực", ilist(I10)),
        kassa_line(k, "chín năng lực", False, who(GAB, ROOT_KV), "chín năng lực", ilist(I9)),
        kassa_line(k, "chín năng lực", True, who(OPA, NER, FULL), "chín năng lực", ilist(I9b)),
        kassa_line(k, "tám năng lực", False, b_blind, "tám năng lực", ilist(I8)),
        kassa_line(k, "tám năng lực", True, b_deaf, "tám năng lực", ilist(I8b)),
        kassa_line(k, "bảy năng lực", False, b_bd, "bảy năng lực", ilist(I7)),
        kassa_line(k, "năm năng lực", False, who(GAB, NOROOT, "ngoại trừ những chúng sinh không có giới tính"),
                   "năm năng lực", ilist(I5)),
        kassa_line(k, "bốn năng lực", False, who(GAB, NOROOT, "không có giới tính"), "bốn năng lực",
                   ilist(I4))]))
    # ^2-1013 roots
    vh = [hetu(x, HETU_VIP) for x in ROOT_K]
    out.append(seg("2-1013", [
        kassa_line(k, "ba gốc rễ", False, who(DEV_K, MAN1, GAB, ROOT_KN), "ba gốc rễ", ", ".join(vh)),
        kassa_line(k, "hai gốc rễ", False, who(DEV_K, MAN1, GAB, ROOT_KV), "hai gốc rễ", ", ".join(vh[:2]))
        + f" Ở các chúng sinh còn lại {S.reading('?', 'avasesā sattā')}, những gì xuất hiện đều {NOROOT}."]))
    slip("^2-1014 «… sabbesaṃ katame cattāro āhārā pātubhavanti.»: a question closed with a full stop (kept «.»)")
    out.append(seg("2-1014", [
        def_rebirth(k, "bốn loại dưỡng chất", L_AH4, end="."),
        def_rebirth(k, "một loại tiếp xúc", phassa("manoviññāṇadhātu"), sg=True),
        def_rebirth(k, EVERY, DHATU["manoviññāṇa"], sg=True, closing_what="một loại tâm")]))
    # rūpadhātu
    out.append(head(*HEAD["2-18-4-2-0"], "2-18-4-2-0"))
    q = f"{AT[r]} có bao nhiêu khối xuất hiện… bao nhiêu loại tâm xuất hiện?"
    ap = (f"{AT[r]} ngoại trừ chư thiên Vô Tưởng, năm khối xuất hiện, năm lĩnh vực nhận biết xuất hiện, năm yếu tố "
          f"xuất hiện, một sự thật xuất hiện, mười năng lực xuất hiện, ba gốc rễ xuất hiện, ba loại dưỡng chất xuất "
          f"hiện, một loại tiếp xúc xuất hiện, {EVERY} xuất hiện.")
    out.append(seg("2-1015", [q, ap]))
    rb = dict(all_b=False)
    out.append(seg("2-1016", [
        def_rebirth(r, "năm khối", L_KH5, **rb),
        def_rebirth(r, "năm lĩnh vực nhận biết", ay_list(["cakkh", "rūp", "sot", "man", "dhamm"]), **rb),
        def_rebirth(r, "năm yếu tố", dh_list(["cakkhu", "rūpa", "sota", "manoviññāṇa", "dhamma"]), **rb),
        def_rebirth(r, "một sự thật", SACCA["dukkha"], sg=True, **rb),
        def_rebirth(r, "mười năng lực", ilist(["cakkhu", "sot", "man", "jīvit", FEEL] + FAITH5), **rb),
        def_rebirth(r, "ba gốc rễ", ", ".join(vh), **rb),
        def_rebirth(r, "ba loại dưỡng chất", ", ".join(AHARA3), **rb),
        def_rebirth(r, "một loại tiếp xúc", phassa("manoviññāṇadhātu"), sg=True, **rb),
        def_rebirth(r, EVERY, DHATU["manoviññāṇa"], sg=True, closing_what="một loại tâm", **rb)]))
    # asaññasattā
    out.append(head(*HEAD["2-18-4-3-0"], "2-18-4-3-0"))
    ASN = "chư thiên Vô Tưởng"                                                 # asaññasattānaṃ devānaṃ (tb)
    out.append(seg("2-1017", [
        f"Ở {ASN}, vào khoảnh khắc tái sinh, có bao nhiêu khối xuất hiện… bao nhiêu loại tâm xuất hiện?",
        f"Ở {ASN}, vào khoảnh khắc tái sinh, một khối xuất hiện – {KHANDHA['rūpa']}; hai lĩnh vực nhận biết xuất "
        f"hiện – {AYAT['rūp']}, {AYAT['dhamm']}; hai yếu tố xuất hiện – {DHATU['rūpa']}, {DHATU['dhamma']}; một sự "
        f"thật xuất hiện – {SACCA['dukkha']}; một năng lực xuất hiện – {INDR['rūpajīvit']}. {cap(ASN)} xuất hiện mà "
        f"{NOROOT}, không có dưỡng chất, không có sự tiếp xúc, không có cảm giác, không có tri giác, không có chủ ý, "
        f"không có tâm."]))
    # arūpadhātu
    out.append(head(*HEAD["2-18-4-4-0"], "2-18-4-4-0"))
    q = f"{AT[a]} có bao nhiêu khối xuất hiện… bao nhiêu loại tâm xuất hiện?"
    ap = (f"{AT[a]} bốn khối xuất hiện, hai lĩnh vực nhận biết xuất hiện, hai yếu tố xuất hiện, một sự thật xuất "
          f"hiện, tám năng lực xuất hiện, ba gốc rễ xuất hiện, ba loại dưỡng chất xuất hiện, một loại tiếp xúc xuất "
          f"hiện, {EVERY} xuất hiện.")
    out.append(seg("2-1018", [q, ap]))
    K4 = ", ".join(KHANDHA[x] for x in ["vedanā", "saññā", "saṅkhāra", "viññāṇa"])
    out.append(seg("2-1019", [
        def_rebirth(a, "bốn khối", K4, **rb),
        def_rebirth(a, "hai lĩnh vực nhận biết", ay_list(["man", "dhamm"]), **rb),
        def_rebirth(a, "hai yếu tố", dh_list(["manoviññāṇa", "dhamma"]), **rb),
        def_rebirth(a, "một sự thật", SACCA["dukkha"], sg=True, **rb),
        def_rebirth(a, "tám năng lực", ilist(["man", "jīvit", "upekkh"] + FAITH5), **rb),
        def_rebirth(a, "ba gốc rễ", ", ".join(vh), **rb),
        def_rebirth(a, "ba loại dưỡng chất", ", ".join(AHARA3), **rb),
        def_rebirth(a, "một loại tiếp xúc", phassa("manoviññāṇadhātu"), sg=True, **rb),
        def_rebirth(a, EVERY, DHATU["manoviññāṇa"], sg=True, closing_what="một loại tâm", **rb)]))
    return out


# =========================================================================== planes (^2-1020)
def hits(line):
    return " ".join(V(s) for s in SPL.split(line.strip()))


def seg_1020():
    P = PS["2-1020"]
    m = [("thuộc", "cõi dục lạc"), ("không thuộc", "cõi dục lạc"), ("thuộc", "cõi hình sắc"),
         ("không thuộc", "cõi hình sắc"), ("thuộc", "cõi không hình sắc"), ("không thuộc", "cõi không hình sắc")]
    matrix = ", ".join(f"các hiện tượng {a} {b}" for a, b in m) + (", các hiện tượng nằm trong các cõi tồn tại, "
                                                                   "các hiện tượng không nằm trong các cõi tồn tại")
    kama = pi1_line("4-02-nikkhepakandam.md", "1-1287").replace(
        " " + S.spell("Sī., Ka.", "paranimmitavasavattideve"), "")                 # PI1 ^1-1287 (no variant here)
    rupa = (pi1_line("4-02-nikkhepakandam.md", "1-1289")
            .replace(" " + S.spell("Sī., Ka.", "akaniṭṭhadeve"), "")
            .replace(" " + S.reading("Ka.", "diṭṭhadhammasukhavihārassa"), ""))     # PI1 ^1-1289
    arupa = pi1_line("4-02-nikkhepakandam.md", "1-1291")                          # PI1 ^1-1291
    for x in (kama, rupa, arupa):
        assert "[" not in x, x
    par = (f"{V('Katame dhammā pariyāpannā?')} Các hiện tượng thiện, bất thiện và không xác định về mặt đạo đức là "
           f"đối tượng của ô nhiễm, thuộc cõi dục lạc, thuộc cõi hình sắc hoặc thuộc cõi không hình sắc: "
           f"{L_KH5.rsplit(', ', 1)[0]} và {KHANDHA['viññāṇa']} – những hiện tượng này nằm trong các cõi tồn tại.")
    #  PI1 ^1-1293 with the full aggregate list of ^1-998
    return [head(*HEAD["2-18-5-0"], "2-18-5-0"),
            seg("2-1020", [cap(matrix) + ".", kama, hits(P[2]), rupa, hits(P[4]), arupa, hits(P[6]), par,
                           hits(P[8])])]


# =========================================================================== gods and lifespans (^2-1021 … ^2-1029)
GOD = {   # termbase names (chư thiên + name); names the termbase lacks are built from its members (reported)
    "cātumahārājika": "chư thiên Tứ Đại Thiên Vương", "tāvatiṃsa": "chư thiên Ba Mươi Ba", "yāma": "chư thiên Dạ Ma",
    "tusita": "chư thiên Đâu Suất", "nimmānarati": "chư thiên Hóa Lạc",
    "paranimmitavasavattī": "chư thiên Tha Hóa Tự Tại",
    "brahmapārisajja": "chư thiên Phạm Chúng", "brahmapurohita": "chư thiên Phạm Phụ",
    "mahābrahmā": "chư thiên Đại Phạm",
    "parittābha": "chư thiên Thiểu Quang", "appamāṇābha": "chư thiên Vô Lượng Quang", "ābhassara": "chư thiên Quang Âm",
    "parittasubha": "chư thiên Thiểu Tịnh", "appamāṇasubha": "chư thiên Vô Lượng Tịnh",
    "subhakiṇha": "chư thiên Biến Tịnh",
    "asaññasatta": "chư thiên Vô Tưởng", "vehapphala": "chư thiên Quảng Quả", "aviha": "chư thiên Vô Phiền",
    "atappa": "chư thiên Vô Nhiệt", "sudassa": "chư thiên Thiện Hiện", "sudassī": "chư thiên Thiện Kiến",
    "akaniṭṭha": "chư thiên Sắc Cứu Cánh",
    "ākāsānañcāyatanūpaga": "chư thiên sinh vào lĩnh vực không gian vô tận",                       # PI1 ^1-1291
    "viññāṇañcāyatanūpaga": "chư thiên sinh vào lĩnh vực thức vô tận",
    "ākiñcaññāyatanūpaga": "chư thiên sinh vào lĩnh vực không có gì cả",
    "nevasaññānāsaññāyatanūpaga": "chư thiên sinh vào lĩnh vực không phải tri giác cũng không phải không tri giác",  # PI1
}
for _g in ("Tứ (cātu-, with the termbase «Đại Thiên Vương»)", "brahmapārisajja «Phạm Chúng»",
           "brahmapurohita «Phạm Phụ»", "parittābha «Thiểu Quang» (beside the termbase «Vô Lượng Quang»)",
           "parittasubha / appamāṇasubha «Thiểu Tịnh / Vô Lượng Tịnh» (termbase member subha «Tịnh»)",
           "subhakiṇha «Biến Tịnh»"):
    misfit(f"god name not in the termbase, built in the termbase's Sino-Vietnamese style: {_g}")
COMM = "một số người tái sinh vào cộng đồng của"                         # appekacce X sahabyataṃ upapajjanti
GIVE = "Sau khi bố thí, thọ trì giới hạnh, thực hiện việc hành trì ngày trai giới"   # Dānaṃ datvā, sīlaṃ …, uposatha…
misfit("^2-1021 upādāya «kể từ» in «cātumahārājike deve upādāya tadupari devā» (starting from): none of the "
       "termbase senses (phái sinh từ / dựa vào / tùy thuộc vào) fits")
misfit("^2-1021 sahabyataṃ upapajjanti (no entry): «tái sinh vào cộng đồng của …»")


def seg_1021_1023():
    out = [head(*HEAD["2-18-6-0"], "2-18-6-0"), head(*HEAD["2-18-6-1-0"], "2-18-6-1-0")]
    whom = (["những người quý tộc giàu có", "những bà-la-môn giàu có", "những gia chủ giàu có"]
            + [GOD[g] for g in ("cātumahārājika", "tāvatiṃsa", "yāma", "tusita", "nimmānarati",
                                "paranimmitavasavattī")])
    out.append(seg("2-1021", [
        f"“Chư thiên”. Có ba loại chư thiên – chư thiên theo quy ước {S.spell('Syā.', 'sammatidevā')}, "
        f"chư thiên do tái sinh, chư thiên do sự trong sạch.",
        "Gọi là chư thiên theo quy ước – các vua, các hoàng hậu, các hoàng tử.",
        f"Gọi là chư thiên do tái sinh – kể từ {GOD['cātumahārājika']} "
        f"{S.spell('Sī., Syā.', 'cātummahārājike')}, chư thiên từ đó trở lên.",
        "Gọi là chư thiên do sự trong sạch – các bậc A-la-hán được gọi như vậy.",
        f"{GIVE}, người ta tái sinh ở đâu? {GIVE}, " + ", ".join(f"{COMM} {w}" for w in whom) + "."]))
    out.append(head(*HEAD["2-18-6-2-0"], "2-18-6-2-0"))
    out.append(seg("2-1022", [f"Tuổi thọ của loài người là bao nhiêu? Một trăm năm, ít hơn hoặc nhiều hơn "
                              f"{S.reading('Syā., Ka.', 'appaṃ vā bhiyyo vā; Trường Bộ Kinh 2.7')}."]))

    def life(g, human, divine, total, var=""):
        G = GOD[g]
        return (f"Tuổi thọ của {G} là bao nhiêu? {human} của loài người, đó là một ngày một đêm{var} của {G}. "
                f"Tính theo đêm ấy, ba mươi đêm là một tháng. Tính theo tháng ấy, mười hai tháng là một năm. "
                f"Tính theo năm ấy, {divine} cõi trời là tuổi thọ của {G}. "
                f"Theo cách tính của loài người thì là bao nhiêu? {total}.")

    # koṭi = 10 million, satasahassa = 100,000 (user: counts in millions «triệu», arithmetic exact)
    # 500 x 360 x 50 = 9,000,000 = navuti satasahassāni; 1000 x 360 x 100 = 36 M = 3 koṭi + 60 x 100,000; …
    assert 500 * 360 * 50 == 90 * 100_000
    assert 1000 * 360 * 100 == 3 * 10**7 + 60 * 100_000
    assert 2000 * 360 * 200 == 14 * 10**7 + 40 * 100_000
    assert 4000 * 360 * 400 == 57 * 10**7 + 60 * 100_000
    assert 8000 * 360 * 800 == 200 * 10**7 + 30 * 10**7 + 40 * 100_000
    assert 16000 * 360 * 1600 == 900 * 10**7 + 21 * 10**7 + 60 * 100_000
    assert 9 + 36 + 144 + 576 + 2304 + 9216 == 1200 * 10 + 28 * 10 + 5         # the verse: 12,285 million
    out.append(seg("2-1023", [
        life("cātumahārājika", "Năm mươi năm", "năm trăm năm", "Chín triệu năm",
             " " + S.spell("Ka.", "rattidivo; Tăng Chi Bộ Kinh 3.71")),
        life("tāvatiṃsa", "Một trăm năm", "một nghìn năm", "Ba mươi triệu cộng sáu triệu năm"),
        life("yāma", "Hai trăm năm", "hai nghìn năm", "Một trăm bốn mươi triệu cộng bốn triệu năm"),
        life("tusita", "Bốn trăm năm", "bốn nghìn năm", "Năm trăm bảy mươi triệu cộng sáu triệu năm"),
        life("nimmānarati", "Tám trăm năm", "tám nghìn năm",
             "Hai nghìn triệu cộng ba trăm triệu cộng bốn triệu năm"),
        life("paranimmitavasavattī", "Một nghìn sáu trăm năm", "mười sáu nghìn năm",
             "Chín nghìn triệu cộng hai trăm mười triệu cộng sáu triệu năm"),
        f"Sáu hàng chư thiên này {S.reading('Syā.', 'chapi te')} thuộc cõi dục lạc, có đầy đủ tất cả các dục lạc;",
        "Tuổi thọ của tất cả, tính gộp làm một, là bao nhiêu.",
        "Mười hai nghìn triệu của họ, cộng hai trăm tám mươi triệu;",
        "Cộng năm triệu, đã được công bố tính theo số năm."]))
    slip("^2-1023 verse «Sabbesaṃ ekasaṅkhāto, āyu bhavati kittako.»: a question closed with a full stop (kept «.»)")
    slip("^2-1023 «cātumahārājikānaṃ» in the question vs «cātummahārājikānaṃ» in the answer: spelling only, one name")
    return out


ORDN = {"Paṭhamaṃ": "thứ nhất", "Dutiyaṃ": "thứ hai", "Tatiyaṃ": "thứ ba"}
LEVEL = {"parittaṃ": "hạn hẹp", "majjhimaṃ": "trung bình", "paṇītaṃ": "ưu việt"}


def jhana_line(o, lv, god, span):
    j = f"Sau khi tu tập tầng thiền {ORDN[o]} ở mức {LEVEL[lv]}"
    return (f"{j}, người ta tái sinh ở đâu? {j}, người ta tái sinh vào cộng đồng của {GOD[god]}. "
            f"Tuổi thọ của họ là bao nhiêu? {span}.")


def life_q(gods, span):
    return f"Tuổi thọ của {' và '.join(GOD[g] for g in gods)} là bao nhiêu? {span}."


def seg_1024_1029():
    out = [seg("2-1024", [jhana_line("Paṭhamaṃ", "parittaṃ", "brahmapārisajja", "Một phần ba của kiếp"),
                          jhana_line("Paṭhamaṃ", "majjhimaṃ", "brahmapurohita", "Nửa kiếp"),
                          jhana_line("Paṭhamaṃ", "paṇītaṃ", "mahābrahmā",
                                     f"Một kiếp {S.reading('Syā.', 'eko kappo')}")]),
           seg("2-1025", [jhana_line("Dutiyaṃ", "parittaṃ", "parittābha", "Hai kiếp"),
                          jhana_line("Dutiyaṃ", "majjhimaṃ", "appamāṇābha", "Bốn kiếp"),
                          jhana_line("Dutiyaṃ", "paṇītaṃ", "ābhassara", "Tám kiếp")]),
           seg("2-1026", [jhana_line("Tatiyaṃ", "parittaṃ", "parittasubha", "Mười sáu kiếp"),
                          jhana_line("Tatiyaṃ", "majjhimaṃ", "appamāṇasubha", "Ba mươi hai kiếp"),
                          jhana_line("Tatiyaṃ", "paṇītaṃ", "subhakiṇha", "Sáu mươi bốn kiếp")])]
    diff = ", ".join(f"sự khác biệt về {x}" for x in ("đối tượng", "sự chú tâm", "ý muốn", "sự mong cầu",
                                                       "sự quyết định", "sự định hướng", "trí tuệ"))
    gods4 = ["asaññasatta", "vehapphala", "aviha", "atappa", "sudassa", "sudassī", "akaniṭṭha",
             "ākāsānañcāyatanūpaga", "viññāṇañcāyatanūpaga", "ākiñcaññāyatanūpaga", "nevasaññānāsaññāyatanūpaga"]
    out.append(seg("2-1027", [
        f"Sau khi tu tập tầng thiền thứ tư, do {diff}, " + ", ".join(f"{COMM} {GOD[g]}" for g in gods4) + ".",
        life_q(["asaññasatta", "vehapphala"], "Năm trăm kiếp"),
        life_q(["aviha"], "Một nghìn kiếp"), life_q(["atappa"], "Hai nghìn kiếp"),
        life_q(["sudassa"], "Bốn nghìn kiếp"), life_q(["sudassī"], "Tám nghìn kiếp"),
        life_q(["akaniṭṭha"], "Mười sáu nghìn kiếp")]))
    out.append(seg("2-1028", [
        life_q(["ākāsānañcāyatanūpaga"], "Hai mươi nghìn kiếp"),
        life_q(["viññāṇañcāyatanūpaga"], "Bốn mươi nghìn kiếp"),
        life_q(["ākiñcaññāyatanūpaga"], "Sáu mươi nghìn kiếp"),
        life_q(["nevasaññānāsaññāyatanūpaga"], "Tám mươi bốn nghìn kiếp")]))
    out.append(seg("2-1029", [
        "Được uy lực của phước nâng lên, họ đi đến cõi tái sinh dục lạc và hình sắc.",
        f"Dù đã đạt đến cả đỉnh cao của sự hiện hữu {S.reading('Syā.', 'bhavaggaṃ vāpi')}, họ vẫn trở lại "
        f"{S.reading('Syā.', 'puna gacchanti')} cõi xấu.",
        "Chúng sinh sống lâu đến thế vẫn chết đi khi tuổi thọ cạn kiệt;",
        "Không có sự hiện hữu nào là thường còn, bậc Đại Hiền đã nói như vậy.",
        "Vì thế, những người trí khôn ngoan, tinh tế, biết suy xét về lợi ích;",
        "Để giải thoát khỏi sự lão hóa và sự chết, tu tập con đường tối thượng.",
        "Sau khi tu tập con đường trong sạch, dẫn sâu vào Niết-bàn;",
        "Sau khi hiểu biết trọn vẹn tất cả ô nhiễm, họ nhập Niết-bàn trọn vẹn, không còn ô nhiễm."]))
    return out


# =========================================================================== question sections (^2-1030 … ^2-1044)
NA3 = "không cần dứt bỏ, không cần được tu tập cũng không cần được tự mình chứng nghiệm"
SEEN4 = "không được thấy, không được nghe, không được cảm nhận cũng không được nhận biết"


def seg_1030_1044():
    out = [head(*HEAD["2-18-7-0"], "2-18-7-0"),
           seg("2-1030", [qcount([ITEM[x][0] for x in ("abhiññeyyā", "pariññeyyā", "pahātabbā", "bhāvetabbā",
                                                       "sacchikātabbā")] + [NA3])]),
           seg("2-1031", [T(ln) for ln in PS["2-1031"]])]
    slip("^2-1031 «Tīṇindriyā … siyā na bhāvetabbā, sacchikātabbā»: na missing before sacchikātabbā (as written: "
         "«đôi khi không cần được tu tập, nhưng cần được tự mình chứng nghiệm»)")
    out += [head(*HEAD["2-18-8-0"], "2-18-8-0"),
            seg("2-1032", [qcount([CLAUSE["sārammaṇā"], CLAUSE["anārammaṇā"]])]),
            seg("2-1033", [T(ln) for ln in PS["2-1033"]]),
            seg("2-1034", [qcount([CLAUSE["sārammaṇārammaṇā"], CLAUSE["anārammaṇārammaṇā"]])]),
            seg("2-1035", [T(ln) for ln in PS["2-1035"]]),
            head(*HEAD["2-18-9-0"], "2-18-9-0"),
            seg("2-1036", [qcount([ITEM[x][0] for x in ("diṭṭhā", "sutā", "mutā", "viññātā")] + [SEEN4])]),
            seg("2-1037", [T(ln) for ln in PS["2-1037"]]),
            head(*HEAD["2-18-10-0"], "2-18-10-0")]
    TRI = {"2-1038": ["kusalā", "akusalā", "abyākatā"],
           "2-1039": ["sukhāya vedanāya sampayuttā", "dukkhāya vedanāya sampayuttā",
                      "adukkhamasukhāya vedanāya sampayuttā"],
           "2-1040": ["vipākā", "vipākadhammadhammā", "nevavipākanavipākadhammadhammā"],
           "2-1041": ["upādinnupādāniyā", "anupādinnupādāniyā", "anupādinnaanupādāniyā"],
           "2-1042": ["savitakkasavicārā", "avitakkavicāramattā", "avitakkaavicārā"],
           "2-1043": ["rūpā", "arūpā"]}
    hb = {"2-1038": "2-18-10-1-0", "2-1039": "2-18-10-2-0", "2-1040": "2-18-10-3-0", "2-1041": "2-18-10-4-0",
          "2-1042": "2-18-10-5-0", "2-1043": "2-18-10-6-0"}
    for bid, preds in TRI.items():
        out.append(head(*HEAD[hb[bid]], hb[bid]))
        out.append(seg(bid, [qcount([CLAUSE[p] for p in preds])] + [T(ln) for ln in PS[bid][1:]]))
    slip("^2-1039 «Moho akusalahetu … siyā dukkhamasukhāya vedanāya sampayutto» (initial a- missing): kept as written "
         "(«cảm giác khó chịu và không dễ chịu»)")
    slip("^2-1039 / ^2-1042 «…, kāyaviññāṇadhātu / manoviññāṇadhātu siyā …»: a new subject after a comma (kept)")
    slip("^2-1041 «… siyā anupādinnupādāniyo 4.»: a stray digit «4» (kept as written)")
    out.append(head(*HEAD["2-18-10-7-0"], "2-18-10-7-0"))
    lq = [("Trong năm khối", "khối"), ("Trong mười hai lĩnh vực nhận biết", "lĩnh vực"),
          ("Trong mười tám yếu tố", "yếu tố")]
    pos, neg = CLAUSE["lokiyā"], CLAUSE["lokuttarā"]
    q = " ".join(f"{a}, bao nhiêu {b} {pos}, bao nhiêu {b} {neg}?" for a, b in lq)
    q += (f" Trong bốn sự thật, bao nhiêu sự thật {pos}, bao nhiêu sự thật {neg}… trong bảy loại tâm, "
          f"bao nhiêu loại {pos}, bao nhiêu loại {neg}?")
    out.append(seg("2-1044", [
        q, T(PS["2-1044"][1]), T(PS["2-1044"][2]),
        "Cần được hiểu biết trực tiếp, hai mục về đối tượng, được thấy, thiện, cảm giác;",
        "Quả của nghiệp và do nghiệp tạo ra, sự hướng tâm, vật chất và thế gian.",
        f"{S.CH_HEADINGS['Dhammahadayavibhaṅgo']} đã hoàn tất.",
        f"Bộ “{S.H_BOOK}” đã hoàn tất."]))
    return out


# =========================================================================== assemble
def segments():
    segs = [head(*HEAD["2-18-0"], "2-18-0"), head(*HEAD["2-18-1-0"], "2-18-1-0"), seg_978()]
    segs += seg_979_990()
    segs += [head(*HEAD["2-18-2-0"], "2-18-2-0")] + seg_991_998()
    segs += [head(*HEAD["2-18-3-0"], "2-18-3-0")] + seg_999_1006()
    segs += seg_1007_1019() + seg_1020() + seg_1021_1023() + seg_1024_1029() + seg_1030_1044()
    assert [b for _, b in segs] == list(PS), [b for _, b in segs if b not in PS]
    return segs


def build():
    text = S.render(segments())
    assert "—" not in text and ":-" not in text and "….." not in text
    return text


def main():
    text = build()
    if "--dry" not in sys.argv:
        (S.OUT / PART).write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {PART}: {sum(1 for ln in text.splitlines() if ln.strip())} non-empty lines")
    if "--report" in sys.argv:
        print("## slips"), [print(" ", x) for x in SLIPS]
        print("## misfits"), [print(" ", x) for x in MISFITS]
        print(f"## pi-1 sentences reused: {len(PI1_USED)}; pi-2 ch. 1-17 sentences reused: {len(PI2_USED)}; "
              f"parsed: {len(PARSED)}")
        for src in sorted({s for s, _ in PI1_USED}):
            print("  ", src, sorted({p for s, p in PI1_USED if s == src})[:8])


if __name__ == "__main__":
    main()
