"""Builder for the Vietnamese rails translation of pi-1 (Dhammasaṅgaṇī, «Liệt kê các hiện tượng», plain audience),
chapters 2-01 (after the approved sample, ^1-1-1-2-0 onward) and 2-02.

Writes (only when run as a script):
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/2-01-cittuppadakandam.md
      (= sample-2-01/2-01-sample.md byte-for-byte + the rest of the chapter)
  AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/2-02-cittuppadakandam.md
  0-INBOX/temp/pipeline/pi-1-vi-ai/rails/notes-2-01_2-02.md

Every line is translated from the Pāli by fixed strings: the sample constants (imported from
build_rails_sample_vi.py, never edited) plus the tables below. Unknown Pāli raises KeyError, so nothing is
guessed silently; identical Pāli gives byte-identical Vietnamese.
Terms follow the locked termbase AI_translation/vietnamese/pi-1-pali-vietnamese-termbase-plain.md
(+ pi-1-vi-ai/termbase/APPROVED.md). Translated fresh from the Pāli.
Later chapter builders may import this file (importing writes nothing): NAMES, STR, there_list, name_list,
tail_vi, qa_vi, kusala_vi, summary_vi, EXACT, ATTR, PIECES, DESC, translate_line.

usage: python -I -X utf8 build_rails_2-01_2-02_vi.py
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-vi-ai\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_vi as S  # noqa: E402  (importing writes nothing)

PALI = S.PALI
OUT = S.OUT
SAMPLE = HERE / "sample-2-01" / "2-01-sample.md"
PE, ELL, DASH = "…pe…", "…", "–"
cap = S.cap
TS = S.TS                                     # vào lúc ấy

# =========================================================================================
# 1. Names: Pāli nominative -> Vietnamese (Q/A frames, lists, summaries)
# =========================================================================================
NAMES = dict(S.FN)
NAMES.update({
    "upekkhā": "sự bình thản",
    "upekkhindriyaṃ": "năng lực bình thản",
    "vedanākkhandho": "khối cảm giác",
    "saññākkhandho": "khối tri giác",
    "saṅkhārakkhandho": "khối tạo tác",
    "viññāṇakkhandho": "khối thức",
    "manāyatanaṃ": "lĩnh vực ý",
    "dhammāyatanaṃ": "lĩnh vực đối tượng của ý",
    "manoviññāṇadhātu": "yếu tố ý thức",
    "dhammadhātu": "yếu tố đối tượng của ý",
    # āhāra: the approved pattern of «kabaḷīkāro āhāro» = «thức ăn trong vai trò dưỡng chất»
    "phassāhāro": "sự tiếp xúc trong vai trò dưỡng chất",
    "manosañcetanāhāro": "chủ ý của ý trong vai trò dưỡng chất",
    "viññāṇāhāro": "thức trong vai trò dưỡng chất",
    # Koṭṭhāsavāra: counted groups
    "cattāro khandhā": "bốn khối",
    "dvāyatanāni": "hai lĩnh vực nhận biết",
    "dve dhātuyo": "hai yếu tố",
    "tayo āhārā": "ba loại dưỡng chất",
    "aṭṭhindriyāni": "tám năng lực",
    "sattindriyāni": "bảy năng lực",
    "satta balāni": "bảy sức mạnh",
    "cha balāni": "sáu sức mạnh",
    "tayo hetū": "ba gốc rễ",
    "dve hetū": "hai gốc rễ",
    "pañcaṅgikaṃ jhānaṃ": "tầng thiền gồm năm chi phần",
    "caturaṅgikaṃ jhānaṃ": "tầng thiền gồm bốn chi phần",
    "tivaṅgikaṃ jhānaṃ": "tầng thiền gồm ba chi phần",
    "duvaṅgikaṃ jhānaṃ": "tầng thiền gồm hai chi phần",
    "pañcaṅgiko maggo": "con đường gồm năm chi phần",
    "caturaṅgiko maggo": "con đường gồm bốn chi phần",
    # Koṭṭhāsavāra: «eko/ekā/ekaṃ X»
    "eko phasso": "một sự tiếp xúc",
    "ekā vedanā": "một cảm giác",
    "ekā saññā": "một tri giác",
    "ekā cetanā": "một chủ ý",
    "ekaṃ cittaṃ": "một tâm",
    "eko vedanākkhandho": "một khối cảm giác",
    "eko saññākkhandho": "một khối tri giác",
    "eko saṅkhārakkhandho": "một khối tạo tác",
    "eko viññāṇakkhandho": "một khối thức",
    "ekaṃ manāyatanaṃ": "một lĩnh vực ý",
    "ekaṃ manindriyaṃ": "một năng lực ý",
    "ekā manoviññāṇadhātu": "một yếu tố ý thức",
    "ekaṃ dhammāyatanaṃ": "một lĩnh vực đối tượng của ý",
    "ekā dhammadhātu": "một yếu tố đối tượng của ý",
    # Suññatavāra: bare group names
    "dhammā": "các hiện tượng",
    "khandhā": "các khối",
    "āyatanāni": "các lĩnh vực nhận biết",
    "dhātuyo": "các yếu tố",
    "āhārā": "các loại dưỡng chất",
    "indriyāni": "các năng lực",
    "jhānaṃ": "tầng thiền",
    "maggo": "con đường",
    "balāni": "các sức mạnh",
    "hetū": "các gốc rễ",
})


def name(p):
    p = p[0].lower() + p[1:]
    return NAMES[p]


# =========================================================================================
# 2. Synonym strings: Pāli (between «Yo/Yā/Yaṃ tasmiṃ samaye» and the dash) -> Vietnamese
# =========================================================================================
def _strip_prefix(s, prefix):
    assert s.startswith(prefix), (s, prefix)
    return s[len(prefix):]


S_SANNA_PLAIN = "tri giác, " + _strip_prefix(S.S_SANNA, f"tri giác {S.TAJJA}, ")        # tri giác, sự nhận ra, …
S_CETANA_PLAIN = "chủ ý, " + _strip_prefix(S.S_CETANA, f"chủ ý {S.TAJJA}, ").replace(
    " " + S.reading("Syā.", "sañcetayitattaṃ"), "")                                      # no variant
S_JIVITA_PLAIN = S.S_JIVITA.replace(" " + S.spell("Sī.", "irīyanā"), "")                  # no variant
assert "[" not in S_CETANA_PLAIN + S_JIVITA_PLAIN, (S_CETANA_PLAIN, S_JIVITA_PLAIN)
# cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā
UPE_HEAD = "trạng thái trong tâm không khoan khoái cũng không bứt rứt"
UPE_TAIL = ("cảm nhận không khó chịu cũng không dễ chịu sinh từ sự tiếp xúc của tâm, "
            "cảm giác không khó chịu cũng không dễ chịu sinh từ sự tiếp xúc của tâm")
S_UPEKKHA = f"{UPE_HEAD}, {UPE_TAIL}"
S_UPEKKHA_TAJJA = f"{UPE_HEAD} {S.TAJJA}, {UPE_TAIL}"
S_PANNA_ABBR = "trí tuệ, sự hiểu rõ… sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn"
assert S.S_PANNA.startswith("trí tuệ, sự hiểu rõ, ") and S.S_PANNA.endswith(
    ", sự không si mê, sự tìm hiểu các hiện tượng, quan điểm đúng đắn")

P_UPEKKHA = ("cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ "
             "cetosamphassajā adukkhamasukhā vedanā")
P_SUKHA = ("cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ "
           "cetosamphassajā sātā sukhā vedanā")
P_PANNA = ("paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ "
           "kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo "
           "paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto "
           "paññāratanaṃ amoho dhammavicayo sammādiṭṭhi")
TAJJA_P = "tajjāmanoviññāṇadhātusamphassaj"
STR = {   # Pāli string -> Vietnamese string (placed after «Điều mà vào lúc ấy là »)
    "phasso phusanā saṃphusanā saṃphusitattaṃ": S.S_PHASSA,
    P_SUKHA: S.S_SUKHA,
    TAJJA_P + "aṃ " + P_SUKHA: S.S_VEDANA,
    "saññā sañjānanā sañjānitattaṃ": S_SANNA_PLAIN,
    TAJJA_P + "ā saññā sañjānanā sañjānitattaṃ": S.S_SANNA,
    "cetanā sañcetanā cetayitattaṃ": S_CETANA_PLAIN,
    "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
    "tajjāmanoviññāṇadhātu": S.S_CITTA,
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo": S.S_VITAKKA,
    "cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā": S.S_VICARA,
    "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa": S.S_PITI,
    "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ "
    "samādhibalaṃ sammāsamādhi": S.S_SAMADHI,
    "saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ": S.S_SADDHA,
    "cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā "
    "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo":
        S.S_VIRIYA,
    "sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ "
    "sammāsati": S.S_SATI,
    P_PANNA: S.S_PANNA,
    P_PANNA + " amoho kusalamūlaṃ": S.S_AMOHA,
    "paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": S_PANNA_ABBR,
    "alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ":
        S.S_ALOBHA,
    "adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ": S.S_ADOSA,
    P_UPEKKHA: S_UPEKKHA,
    TAJJA_P + "aṃ " + P_UPEKKHA: S_UPEKKHA_TAJJA,
}
HIRI_P = "hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā"
OTTAPPA_P = "ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā"
JIVITA_P = "āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ"

# =========================================================================================
# 3. Tails: «ye vā pana …», «ayaṃ tasmiṃ samaye X hoti», «ime dhammā kusalā», «…pe…», dash
# =========================================================================================
YVP_P = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"
YVP_V = "hoặc " + S.OTHERS
THAP_P = "ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
THAP_V = "ngoại trừ khối cảm giác, ngoại trừ khối tri giác, ngoại trừ khối thức"
THAP_PV = "ṭhapetvā [thapetvā (ka.)] vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ"
THAP_VV = THAP_V.replace("ngoại trừ ", "ngoại trừ " + S.spell("Ka.", "thapetvā") + " ", 1)
KUSALA_P = "ime dhammā kusalā"
KUSALA_V = S.A_KUSALA[:-1]                    # những hiện tượng này là thiện
assert S.CLOSE_OTHERS == cap(YVP_V) + " – " + KUSALA_V + "."


def this_vi(m):
    return f"đó là {name(m.group(2))} {TS}"


def tail_vi(t):
    t = t.replace(YVP_P + " " + THAP_PV, YVP_V + ", " + THAP_VV)
    t = t.replace(YVP_P + " " + THAP_P, YVP_V + ", " + THAP_V)
    t = t.replace(YVP_P, YVP_V)
    t = re.sub(r"(?<!\S)(ayaṃ|idaṃ|ime|imāni|imā) tasmiṃ samaye (.+?) (hoti|honti)", this_vi, t)
    t = t.replace(KUSALA_P, KUSALA_V)
    t = re.sub(r"\s*…pe…", ELL, t)             # a space before «…pe…» is dropped
    t = t.replace(ELL + ".", ELL)              # «…pe….» -> «…» (never «….»)
    return t


# =========================================================================================
# 4. Lists
# =========================================================================================
def there_list(s):
    """'phasso hoti, vedanā hoti…pe… avikkhepo hoti' -> 'có sự tiếp xúc, có cảm giác… có …'.
    A missing comma between two «… hoti» items (source slip) is rendered as meant (comma)."""
    parts = re.split(r"(?:(?<=hoti)|(?<=honti))(…pe…\s*|,\s*|\s+)", s.strip())
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(ELL + " " if PE in p else ", ")
        else:
            m = re.fullmatch(r"(.+) (hoti|honti)", p)
            out.append("có " + name(m.group(1)))
    return "".join(out)


def name_list(s):
    """'Phasso cetanā…pe… avikkhepo' / 'Vedanākkhandho, saññākkhandho' -> Vietnamese names with commas"""
    parts = re.split(r"(…pe…\s*|,\s*|\s+)", s.strip())
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(ELL + " " if PE in p else ", ")
        else:
            out.append(name(p))
    return cap("".join(out))


# =========================================================================================
# 5. Q/A frames (Koṭṭhāsavāra, Suññatavāra, «Katamo tasmiṃ samaye X hoti?» lines)
# =========================================================================================
QRE = re.compile(r"Katam(?:o|ā|aṃ|e|āni) tasmiṃ samaye (.+?) (hoti|honti)(\?|…pe…)\s*(.*)$")
ARE = re.compile(r"(?:Yo|Yā|Yaṃ) tasmiṃ samaye (.+?) – ((?:ayaṃ|idaṃ) tasmiṃ samaye .+)$")
JRE = re.compile(r"Yo tesaṃ arūpīnaṃ dhammānaṃ (.+?) – (idaṃ tasmiṃ samaye .+)$")
LRE = re.compile(r"(.+?)(\s–\s.*|;.*|\.)$")


def answer_vi(a):
    m = ARE.fullmatch(a)
    if m:
        s, rest = m.groups()
        if s == HIRI_P:
            bod = S.HIRI_BODY
        elif s == OTTAPPA_P:
            bod = S.OTTAPPA_BODY
        else:
            bod = S.body(STR[s])
        return bod + " – " + tail_vi(rest)
    m = JRE.fullmatch(a)
    if m:
        s, rest = m.groups()
        assert s == JIVITA_P, s
        return S.body_jivita(S_JIVITA_PLAIN) + " – " + tail_vi(rest)
    m = LRE.fullmatch(a)
    names, rest = m.groups()
    return name_list(names) + tail_vi(rest)


def q_vi(nm, verb):
    """Katamo/… tasmiṃ samaye X hoti -> «Vào lúc ấy, X là gì»; plural (honti) -> «… là những gì»"""
    return f"{cap(TS)}, {name(nm)} là {'những gì' if verb == 'honti' else 'gì'}"


def qa_vi(line):
    m = QRE.fullmatch(line)
    nm, verb, mark, rest = m.groups()
    q = q_vi(nm, verb)
    if mark == "?":
        return q + "? " + answer_vi(rest)
    return q + ELL + " " + tail_vi(rest)


SUMMARY_V = f"{cap(TS).replace('lúc', 'chính lúc')}"   # Tasmiṃ kho pana samaye -> «Vào chính lúc ấy»


def summary_vi(line):
    """'Tasmiṃ kho pana samaye cattāro khandhā honti, …; ye vā pana …' (Koṭṭhāsa/Suññata summaries)"""
    body = line[len("Tasmiṃ kho pana samaye "):]
    items, rest = body.split(";", 1)
    return f"{SUMMARY_V} " + there_list(items) + ";" + tail_vi(rest)


# =========================================================================================
# 6. «Katame dhammā kusalā? Yasmiṃ samaye …» sentences
# =========================================================================================
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "bahūsu": "nhiều ấn bản"}


def var_vi(br):
    """[word (sī. syā.)] -> [khác chính tả (Sī., Syā.): word] (all variants here are spelling-only)"""
    m = re.fullmatch(r"\[(.+?) \(([^)]*)\)\]", br)
    words, sig = m.groups()
    sig = sig.strip()
    return S.spell(SIGLA[sig] if sig in SIGLA else ", ".join(SIGLA[s] for s in sig.split()), words)


def vars_in(text):
    return re.sub(r"\[[^\]]*\]", lambda m: var_vi(m.group(0)), text)


ORD = {"paṭhamaṃ": "thứ nhất", "dutiyaṃ": "thứ hai", "tatiyaṃ": "thứ ba", "catutthaṃ": "thứ tư",
       "pañcamaṃ": "thứ năm"}
JH = "tầng thiền"
ENTER = "chứng nhập và an trú"               # upasampajja viharati


def enter(o, quals=()):
    """N jhānaṃ upasampajja viharati (+ its qualities) -> «chứng nhập và an trú tầng thiền thứ N, …»"""
    return f"{ENTER} {JH} {ORD[o]}{{V}}" + "".join(", " + q for q in quals)


VIVEKA = "có sự hân hoan và hạnh phúc sinh từ sự tách biệt"           # vivekajaṃ pītisukhaṃ
SAMADHIJA = "có sự hân hoan và hạnh phúc sinh từ định tâm"            # samādhijaṃ pītisukhaṃ
O_KAMA = "hoàn toàn tách khỏi các dục lạc"                            # vivicceva kāmehi
O_VITAKKA = "nhờ sự hướng tâm và sự duy trì tâm lắng xuống"           # vitakkavicārānaṃ vūpasamā
O_PITI = "nhờ sự hân hoan phai nhạt"                                  # pītiyā ca virāgā
O_SUKHA = "nhờ dứt bỏ sự dễ chịu"                                     # sukhassa ca pahānā
SEEN = "không có tri giác về hình sắc ở nơi bản thân, thấy ở bên ngoài bản thân"  # ajjhattaṃ arūpasaññī bahiddhā … passati
FORMS = "những hình sắc"                                              # rūpāni


def colours(c):
    """nīlāni nīlavaṇṇāni nīlanidassanāni nīlanibhāsāni"""
    return f"{FORMS} {c}, có màu {c}, trông {c}, tỏa ánh {c}"


def col_p(stem):
    return f"{stem}āni {stem}avaṇṇāni {stem}anidassanāni {stem}anibhāsāni"


COL = {"nīl": "xanh", "pīt": "vàng", "lohitak": "đỏ", "odāt": "trắng"}
DUBBANNA = "có màu đẹp và màu xấu"                                    # suvaṇṇadubbaṇṇāni

PIECES = {   # Pāli word sequence -> list of Vietnamese pieces (joined by «, »); {V} = place of a variant
    # --- the absorption formulas, in full
    "vivicceva kāmehi vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ "
    "upasampajja viharati":
        [f"{O_KAMA}, tách khỏi các hiện tượng bất thiện",
         enter("paṭhamaṃ", ["có sự hướng tâm và sự duy trì tâm", VIVEKA])],
    "vitakkavicārānaṃ vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ "
    "pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        [O_VITAKKA,
         enter("dutiyaṃ", ["có sự trong sáng ở nơi bản thân", "có sự hợp nhất của tâm",
                           "không có sự hướng tâm cũng không có sự duy trì tâm", SAMADHIJA])],
    "pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti yaṃ taṃ ariyā "
    "ācikkhanti – \"upekkhako satimā sukhavihārī\"ti tatiyaṃ jhānaṃ upasampajja viharati":
        [f"{O_PITI}, an trú bình thản, tỉnh thức và hiểu biết rõ ràng, cảm nhận hạnh phúc bằng thân, "
         "điều mà các bậc thánh mô tả – “Người bình thản, có sự tỉnh thức, an trú trong hạnh phúc”",
         enter("tatiyaṃ")],
    "sukhassa ca pahānā dukkhassa ca pahānā pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ "
    "upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja viharati":
        [f"{O_SUKHA} và dứt bỏ sự khó chịu, nhờ niềm vui và nỗi buồn đã biến mất từ trước",
         enter("catutthaṃ", ["không khó chịu cũng không dễ chịu",
                             "có sự tỉnh thức hoàn toàn trong sạch nhờ sự bình thản"])],
    "avitakkaṃ vicāramattaṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ upasampajja viharati":
        [enter("dutiyaṃ", ["không có sự hướng tâm, chỉ có sự duy trì tâm", SAMADHIJA])],
    # --- opening words only (before …pe…)
    "vivicceva kāmehi": [O_KAMA],
    "vitakkavicārānaṃ vūpasamā": [O_VITAKKA],
    "pītiyā ca virāgā": [O_PITI],
    "sukhassa ca pahānā": [O_SUKHA],
    # --- bases of mastery and liberations
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati": [f"{SEEN} {FORMS}"],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati parittāni": [f"{SEEN} {FORMS} hạn hẹp"],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati appamāṇāni": [f"{SEEN} {FORMS} không thể đo lường"],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati parittāni suvaṇṇadubbaṇṇāni":
        [f"{SEEN} {FORMS} hạn hẹp, {DUBBANNA}"],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati appamāṇāni suvaṇṇadubbaṇṇāni":
        [f"{SEEN} {FORMS} không thể đo lường, {DUBBANNA}"],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati " + col_p("nīl"): [f"{SEEN} {colours(COL['nīl'])}"],
    "ajjhattaṃ arūpasaññī bahiddhā rūpāni passati " + col_p("pīt"): [f"{SEEN} {colours(COL['pīt'])}"],
    col_p("lohitak"): [colours(COL["lohitak"])],
    col_p("odāt"): [colours(COL["odāt"])],
    "tāni abhibhuyya jānāmi passāmīti": ["chế ngự chúng với ý nghĩ “Tôi biết, tôi thấy”"],
    "rūpī rūpāni passati": [f"có hình sắc, thấy {FORMS}"],
    "subhanti": ["với ý nghĩ “Đẹp đẽ”"],
    # --- the immaterial absorptions
    "sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā":
        ["nhờ hoàn toàn vượt qua các tri giác về hình sắc, nhờ các tri giác về sự va chạm biến mất, "
         "nhờ không chú tâm đến các tri giác về sự đa dạng"],
}
ARUPA = {   # the four immaterial bases
    "ākāsānañcāyatana": "lĩnh vực không gian vô tận",
    "viññāṇañcāyatana": "lĩnh vực thức vô tận",
    "ākiñcaññāyatana": "lĩnh vực không có gì cả",
    "nevasaññānāsaññāyatana": "lĩnh vực không phải tri giác cũng không phải không tri giác",
}
for _p, _v in ARUPA.items():
    PIECES[f"{_p}saññāsahagataṃ"] = [f"có tri giác về {_v} đi kèm"]
    PIECES[f"sabbaso {_p}ṃ samatikkamma"] = [f"hoàn toàn vượt qua {_v}"]
for _p in ORD:
    PIECES[f"{_p} jhānaṃ upasampajja viharati"] = [enter(_p)]
    PIECES[f"{_p} jhānaṃ"] = [f"{JH} {ORD[_p]}{{V}}"]

# descriptions of the absorption (after the jhāna or standing alone in a …pe… run)
KASINA = "đề mục bao trùm"
ASUBHA_OBJ = {
    "uddhumātaka": "xác chết trương phình", "vinīlaka": "xác chết bầm tím", "vipubbaka": "xác chết mưng mủ",
    "vicchiddaka": "xác chết bị cắt đứt", "vikkhāyitaka": "xác chết bị thú vật ăn dở",
    "vikkhittaka": "xác chết bị vương vãi", "hatavikkhittaka": "xác chết bị chặt và vương vãi",
    "lohitaka": "xác chết đẫm máu", "puḷavaka": "xác chết đầy giòi", "aṭṭhika": "bộ xương",
}
DESC = {
    "pathavīkasiṇaṃ": f"với {KASINA} là đất",
    "āpokasiṇaṃ": f"với {KASINA} là nước",
    "tejokasiṇaṃ": f"với {KASINA} là lửa",
    "vāyokasiṇaṃ": f"với {KASINA} là gió",
    "nīlakasiṇaṃ": f"với {KASINA} màu xanh",
    "pītakasiṇaṃ": f"với {KASINA} màu vàng",
    "lohitakasiṇaṃ": f"với {KASINA} màu đỏ",
    "odātakasiṇaṃ": f"với {KASINA} màu trắng",
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "với cách thực hành khó khăn{V} và sự hiểu biết trực tiếp chậm chạp",
    "dukkhapaṭipadaṃ khippābhiññaṃ": "với cách thực hành khó khăn{V} và sự hiểu biết trực tiếp nhanh chóng",
    "sukhapaṭipadaṃ dandhābhiññaṃ": "với cách thực hành dễ dàng{V} và sự hiểu biết trực tiếp chậm chạp",
    "sukhapaṭipadaṃ khippābhiññaṃ": "với cách thực hành dễ dàng{V} và sự hiểu biết trực tiếp nhanh chóng",
    "parittaṃ parittārammaṇaṃ": "hạn hẹp và có đối tượng hạn hẹp",
    "parittaṃ appamāṇārammaṇaṃ": "hạn hẹp và có đối tượng không thể đo lường",
    "appamāṇaṃ parittārammaṇaṃ": "không thể đo lường và có đối tượng hạn hẹp",
    "appamāṇaṃ appamāṇārammaṇaṃ": "không thể đo lường và có đối tượng không thể đo lường",
    "mettāsahagataṃ": "có lòng từ ái đi kèm",
    "karuṇāsahagataṃ": "có lòng trắc ẩn đi kèm",
    "muditāsahagataṃ": "có niềm vui đồng cảm đi kèm",
    "upekkhāsahagataṃ": "có sự bình thản đi kèm",
    "hīnaṃ": "thấp kém",
    "majjhimaṃ": "trung bình",
    "paṇītaṃ": "ưu việt",
}
for _p, _v in ASUBHA_OBJ.items():
    DESC[f"{_p}saññāsahagataṃ"] = f"có tri giác về {_v} đi kèm"
ADHIP = {"chandādhipateyyaṃ": "lấy ý muốn làm yếu tố chủ đạo",
         "vīriyādhipateyyaṃ": "lấy tinh tấn làm yếu tố chủ đạo",
         "cittādhipateyyaṃ": "lấy tâm làm yếu tố chủ đạo",
         "vīmaṃsādhipateyyaṃ": "lấy sự thẩm xét làm yếu tố chủ đạo"}
DESC.update(ADHIP)
for _k, _v in DESC.items():
    PIECES[_k] = [_v]

# attributes of the sense-sphere mind (after «Vào lúc tâm thiện thuộc cõi dục lạc sinh khởi, »)
OBJ_FULL_P = ("rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā "
              "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha")
OBJ_FULL_V = ("có đối tượng là hình sắc, hay âm thanh, hay mùi, hay vị, hay vật xúc chạm, hay đối tượng của ý, "
              "hoặc lấy bất cứ thứ gì làm đối tượng")
ATTR = {
    "somanassasahagataṃ": "có niềm vui đi kèm",
    "upekkhāsahagataṃ": "có sự bình thản đi kèm",
    "ñāṇasampayuttaṃ": "gắn liền với hiểu biết",
    "ñāṇavippayuttaṃ": "không gắn liền với hiểu biết",
    "sasaṅkhārena": "có sự thúc đẩy",
    OBJ_FULL_P: OBJ_FULL_V,
    "rūpārammaṇaṃ vā": "có đối tượng là hình sắc",
    "dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha": "hay đối tượng của ý, hoặc lấy bất cứ thứ gì làm đối tượng",
    "hīnaṃ": "thấp kém",
    "majjhimaṃ": "trung bình",
    "paṇītaṃ": "ưu việt",
}
ATTR.update(ADHIP)
KAMA_P = "kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti "
KAMA_V = "Vào lúc tâm thiện thuộc cõi dục lạc sinh khởi, "
INTROS = {
    "rūpūpapattiyā maggaṃ bhāveti ": "Vào lúc một người tu tập con đường dẫn đến tái sinh vào cõi hình sắc, ",
    "arūpūpapattiyā maggaṃ bhāveti ": "Vào lúc một người tu tập con đường dẫn đến tái sinh vào cõi không hình sắc, ",
}
assert S.OPEN_1 == (KAMA_V + ATTR["somanassasahagataṃ"] + ", " + ATTR["ñāṇasampayuttaṃ"] + ", "
                    + OBJ_FULL_V + ","), S.OPEN_1


def words_of(part):
    """split a pe-free Pāli chunk into [word, [variants]]"""
    words = []
    for t in re.findall(r"\[[^\]]*\]|[^\s\[]+", part):
        if t.startswith("["):
            words[-1][1].append(var_vi(t))
        else:
            words.append([t.rstrip(","), []])
    return words


def match(words, table):
    """greedy longest match; returns [(key, variants)]"""
    mx = max(len(k.split()) for k in table)
    res, i = [], 0
    while i < len(words):
        for L in range(min(mx, len(words) - i), 0, -1):
            key = " ".join(w for w, _ in words[i:i + L])
            if key in table:
                break
        else:
            raise KeyError("phrase: " + " ".join(w for w, _ in words[i:]))
        res.append((key, " ".join(v for _, vv in words[i:i + L] for v in vv)))
        i += L
    return res


def put_v(pieces, v):
    """place the variant at {V} (exactly one piece may carry it), else after the last piece"""
    holders = [i for i, p in enumerate(pieces) if "{V}" in p]
    assert len(holders) <= 1
    out = [p.replace("{V}", (" " + v) if v else "") for p in pieces]
    if v and not holders:
        out[-1] += " " + v
    return out


def chunks(x, table):
    out = []
    for i, part in enumerate(re.split(r"(\s*…pe…\s*)", x)):
        if i % 2:
            out.append(ELL + " ")
        elif part.strip():
            res = []
            for key, v in match(words_of(part), table):
                val = table[key]
                res += put_v(val if isinstance(val, list) else [val], v)
            out.append(", ".join(res))
    return "".join(out)


def kusala_vi(line):
    body = line[len("Katame dhammā kusalā? Yasmiṃ samaye "):]
    if body.startswith(KAMA_P):
        body, intro, table = body[len(KAMA_P):], KAMA_V, ATTR
    else:
        for p, r in INTROS.items():
            if body.startswith(p):
                body, intro, table = body[len(p):], r, PIECES
                break
        else:
            raise KeyError("intro: " + body[:60])
    idx = body.index(" tasmiṃ samaye ")
    x, rest = body[:idx].rstrip(), body[idx + len(" tasmiṃ samaye "):]
    if x.endswith(DASH):
        sep, x = " " + DASH, x[:-1].rstrip()
    else:
        sep = ","        # «,» in the Pāli; a missing comma (^1-189) is rendered as meant
        x = x[:-1] if x.endswith(",") else x
    m = re.fullmatch(r"(.*? hoti)(…pe… ime dhammā kusalā.*|; ye vā pana.*)", rest)
    return (S.Q_KUSALA + " " + intro + chunks(x, table) + sep + f" thì {TS} " + there_list(m.group(1))
            + tail_vi(m.group(2)))


# =========================================================================================
# 7. Headings and closing lines (exact)
# =========================================================================================
SIXTEEN = "phân tích theo mười sáu cách"
EIGHT = "phân tích theo tám cách"
H_RUPA_KUSALA = "Tâm thiện thuộc cõi hình sắc"
H_ARUPA_KUSALA = "Tâm thiện thuộc cõi không hình sắc"
BRAHMA = "Bốn tầng thiền về nơi an trú cao thượng"
ASUBHA = "Tầng thiền về sự không đẹp đẽ"
ARUPA4 = "Bốn tầng thiền không hình sắc"
KOTTHASA = "Mục về các thành phần"
SUNNATA = "Mục về sự trống rỗng"
EXACT = {
    # 2-01
    "##### Koṭṭhāsavāro": f"##### {KOTTHASA}",
    "Koṭṭhāsavāro.": f"{KOTTHASA}.",
    "##### Suññatavāro": f"##### {SUNNATA}",
    "Suññatavāro.": f"{SUNNATA}.",
    "Paṭhamaṃ cittaṃ.": "Tâm thứ nhất.",
    "Dutiyaṃ cittaṃ.": "Tâm thứ hai.",
    "Tatiyaṃ cittaṃ.": "Tâm thứ ba.",
    "Catutthaṃ cittaṃ.": "Tâm thứ tư.",
    "Pañcamaṃ cittaṃ.": "Tâm thứ năm.",
    "Chaṭṭhaṃ cittaṃ.": "Tâm thứ sáu.",
    "Sattamaṃ cittaṃ.": "Tâm thứ bảy.",
    "Aṭṭhamaṃ cittaṃ.": "Tâm thứ tám.",
    "Aṭṭha kāmāvacaramahākusalacittāni.": "Tám loại tâm thiện lớn thuộc cõi dục lạc.",
    "Dutiyabhāṇavāro.": "Phần tụng đọc thứ hai.",
    # 2-02
    "#### Rūpāvacarakusalaṃ": f"#### {H_RUPA_KUSALA}",
    "#### Arūpāvacarakusalaṃ": f"#### {H_ARUPA_KUSALA}",
    "#### Tebhūmakakusalaṃ": "#### Tâm thiện thuộc ba cõi",
    "##### Kāmāvacarakusalaṃ": f"##### {S.H_KAMA_KUSALA}",
    "##### Rūpāvacarakusalaṃ": f"##### {H_RUPA_KUSALA}",
    "##### Arūpāvacarakusalaṃ": f"##### {H_ARUPA_KUSALA}",
    "Kāmāvacarakusalaṃ.": f"{S.H_KAMA_KUSALA}.",
    "Rūpāvacarakusalaṃ.": f"{H_RUPA_KUSALA}.",
    "Arūpāvacarakusalaṃ.": f"{H_ARUPA_KUSALA}.",
    "##### Catukkanayo": "##### Phương pháp chia bốn",
    "Catukkanayo.": "Phương pháp chia bốn.",
    "##### Pañcakanayo": "##### Phương pháp chia năm",
    "Pañcakanayo.": "Phương pháp chia năm.",
    "##### Catasso paṭipadā": "##### Bốn cách thực hành",
    "Catasso paṭipadā.": "Bốn cách thực hành.",
    "##### Cattāri ārammaṇāni": "##### Bốn loại đối tượng",
    "Cattāri ārammaṇāni.": "Bốn loại đối tượng.",
    "##### Dve ārammaṇāni": "##### Hai loại đối tượng",
    "Dve ārammaṇāni.": "Hai loại đối tượng.",
    "##### Soḷasakkhattukaṃ": f"##### {cap(SIXTEEN)}",
    "Soḷasakkhattukaṃ.": f"{cap(SIXTEEN)}.",
    "##### Aṭṭhakkhattukaṃ": f"##### {cap(EIGHT)}",
    "Aṭṭhakkhattukaṃ.": f"{cap(EIGHT)}.",
    "##### Idampi aṭṭhakkhattukaṃ": f"##### Đây cũng là {EIGHT}",
    "Idampi aṭṭhakkhattukaṃ.": f"Đây cũng là {EIGHT}.",
    "##### Aparampi aṭṭhakkhattukaṃ": f"##### Thêm một {EIGHT}",
    "Aparampi aṭṭhakkhattukaṃ.": f"Thêm một {EIGHT}.",
    "##### Aṭṭhakasiṇaṃ soḷasakkhattukaṃ": f"##### Tám {KASINA}, {SIXTEEN}",
    "Aṭṭhakasiṇaṃ soḷasakkhattukaṃ.": f"Tám {KASINA}, {SIXTEEN}.",
    "##### Abhibhāyatanāni parittāni": "##### Các lĩnh vực chế ngự hạn hẹp",
    "##### Appamāṇāni": "##### Loại không thể đo lường",
    "Imānipi abhibhāyatanāni soḷasakkhattukāni.": f"Đây cũng là các lĩnh vực chế ngự, {SIXTEEN}.",
    "##### Tīṇi vimokkhāni soḷasakkhattukāni": f"##### Ba sự giải thoát, {SIXTEEN}",
    "Imānipi tīṇi vimokkhāni soḷasakkhattukāni.": f"Đây cũng là ba sự giải thoát, {SIXTEEN}.",
    "##### Cattāri brahmavihārajhānāni soḷasakkhattukāni": f"##### {BRAHMA}, {SIXTEEN}",
    "Cattāri brahmavihārajhānāni [brahmavihārajjhānāni (sī. syā.)] soḷasakkhattukāni.":
        f"{BRAHMA} {S.spell('Sī., Syā.', 'brahmavihārajjhānāni')}, {SIXTEEN}.",
    "##### Asubhajhānaṃ soḷasakkhattukaṃ": f"##### {ASUBHA}, {SIXTEEN}",
    "Asubhajhānaṃ [asubhajjhānaṃ (sī. syā.)] soḷasakkhattukaṃ.":
        f"{ASUBHA} {S.spell('Sī., Syā.', 'asubhajjhānaṃ')}, {SIXTEEN}.",
    "##### Cattāri arūpajhānāni [arūpajjhānāni (sī. syā.)] soḷasakkhattukāni":
        f"##### {ARUPA4} {S.spell('Sī., Syā.', 'arūpajjhānāni')}, {SIXTEEN}",
    "Cattāri arūpajhānāni soḷasakkhattukāni.": f"{ARUPA4}, {SIXTEEN}.",
}


# =========================================================================================
# 8. Line dispatch, segments, build
# =========================================================================================
def translate_line(line):
    if line in EXACT:
        return EXACT[line]
    if line.startswith("Katame dhammā kusalā? Yasmiṃ samaye "):
        return kusala_vi(line)
    if line.startswith("Tasmiṃ kho pana samaye "):
        return summary_vi(line)
    if QRE.fullmatch(line):
        return qa_vi(line)
    if line.startswith("Ye vā pana ") or re.match(r"(Ime|Imāni|Imā|Idaṃ|Ayaṃ) tasmiṃ samaye ", line):
        return cap(tail_vi(line[0].lower() + line[1:]))
    raise KeyError("line: " + line[:80])


FOREIGN = re.compile(r"[a-zA-Z]*[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶfjwzFJWZ]")


def check_vi(r):
    bare = re.sub(r"\[[^\]]*\]", "", r)
    assert not FOREIGN.search(bare), (FOREIGN.search(bare).group(0), r[:160])
    assert "—" not in r and ":-" not in r and "…." not in r and '"' not in r, r[:80]
    assert "là là" not in r, r[:120]


def render(segs):
    blocks = []
    for sid, plines in segs:
        vlines = []
        for p in plines:
            v = unicodedata.normalize("NFC", cap(translate_line(p)))
            check_vi(v)
            assert len(p) - len(p.lstrip("#")) == len(v) - len(v.lstrip("#")), sid
            assert p.count("–") + p.count("—") == v.count("–"), ("dash", sid, p[:60], v[:60])
            vlines.append(v)
        vlines[-1] += f" ^{sid}"
        blocks.append("\n".join(vlines))
    return blocks


def segments(path):
    out, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = S.ID.search(line)
        if m:
            buf.append(line[:m.start()].rstrip())
            out.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line.rstrip())
    assert not buf
    return out


def selftest():
    """Run the translators on the sample's Pāli; every line must equal the approved sample except the
    lines with variant brackets or slips handled by hand there (^1-1, ^1-5, ^1-13, ^1-19, ^1-33),
    the kāya/citta frame (^1-40 … ^1-51, sample-only) and the headings / closings of ^1-57."""
    pal = segments(PALI / "2-01-cittuppadakandam.md")
    pal = pal[:[b for b, _ in pal].index("1-57") + 1]
    vi = segments(SAMPLE)
    skip = {"1-1-0", "1-1-1-0", "1-1-1-1-0", "1-1", "1-5", "1-13", "1-19", "1-33", "1-57"}
    skip |= {f"1-{i}" for i in range(40, 52)}
    ok = bad = 0
    for (b, pl), (b2, vl) in zip(pal, vi):
        assert b == b2
        if b in skip:
            continue
        for p, v in zip(pl, vl):
            if cap(translate_line(p)) == v:
                ok += 1
            else:
                bad += 1
                print("SELFTEST MISMATCH", b, "\n  got:", cap(translate_line(p)), "\n  exp:", v)
    p57, v57 = pal[-1][1], vi[-1][1]
    for i in (0, 1):
        if cap(translate_line(p57[i])) == v57[i]:
            ok += 1
        else:
            bad += 1
            print("SELFTEST MISMATCH 1-57", i, "\n  got:", cap(translate_line(p57[i])), "\n  exp:", v57[i])
    print(f"selftest: {ok} lines identical to the approved sample, {bad} mismatches")
    return bad == 0


def build_2_01():
    segs = segments(PALI / "2-01-cittuppadakandam.md")
    ids = [b for b, _ in segs]
    k = ids.index("1-57") + 1
    sample = SAMPLE.read_bytes().decode("utf-8")
    assert sample.endswith(" ^1-57\n") and "\r" not in sample
    return sample + "\n" + "\n\n".join(render(segs[k:])) + "\n", len(segs)


def build_2_02():
    segs = segments(PALI / "2-02-cittuppadakandam.md")
    return "\n\n".join(render(segs)) + "\n", len(segs)


def notes():
    """New recurring formulas of 2-01/2-02 (Pāli = Vietnamese), generated from the tables above."""
    sample_names = set(S.FN)
    sample_strs = (S.S_PHASSA, S.S_SUKHA, S.S_VEDANA, S.S_SANNA, S.S_CITTA, S.S_VITAKKA, S.S_VICARA, S.S_PITI,
                   S.S_SAMADHI, S.S_SADDHA, S.S_VIRIYA, S.S_SATI, S.S_PANNA, S.S_AMOHA, S.S_ALOBHA, S.S_ADOSA)
    L = ["# pi-1 Vietnamese rails: new formulas of 2-01 (after ^1-57) and 2-02", "",
         "Generated by build_rails_2-01_2-02_vi.py from its fixed strings; import that file instead of "
         "retyping. Strings already in vi-rails-formulas.md are not repeated. Format: Pāli = tiếng Việt.", "",
         "## Frames", "",
         f"Tasmiṃ kho pana samaye X hoti/honti, …; ye vā pana … = {SUMMARY_V} có X, …; {YVP_V} – …",
         f"Katamo/Katamā/Katamaṃ tasmiṃ samaye X hoti? = {q_vi('phasso', 'hoti').replace('sự tiếp xúc', 'X')}?",
         f"Katame/Katamāni/Katamā tasmiṃ samaye X honti? = {q_vi('dhammā', 'honti').replace('các hiện tượng', 'X')}?",
         f"ayaṃ/idaṃ/ime/imāni/imā tasmiṃ samaye X hoti/honti = đó là X {TS}",
         f"Ime/Imāni/Imā/Idaṃ/Ayaṃ tasmiṃ samaye X honti/hoti. (own line) = Đó là X {TS}.",
         f"Katamo tasmiṃ samaye X hoti…pe… ayaṃ tasmiṃ samaye X hoti. = {cap(TS)}, X là gì… đó là X {TS}.",
         "Name lists (Phasso cetanā … / Vedanākkhandho, saññākkhandho …) = names joined with «, », first capitalised",
         f"Name list – idaṃ tasmiṃ samaye X hoti. = Name list – đó là X {TS}.",
         f"{YVP_P} {THAP_P} = {YVP_V}, {THAP_V}",
         f"(^1-62 with variant) = {YVP_V}, {THAP_VV}",
         f"Yo tesaṃ arūpīnaṃ dhammānaṃ {JIVITA_P} – = {S.body_jivita(S_JIVITA_PLAIN)} –",
         f"– ime dhammā kusalā…pe…. = – {KUSALA_V}…",
         "…pe… = … ; «…pe….» = «…»; a missing comma between «X hoti Y hoti» (^1-150, ^1-165) and before "
         "«tasmiṃ samaye» (^1-189) is rendered as meant (comma); a space before «…pe…» is dropped",
         "", "## Synonym strings", ""]
    for p, r in STR.items():
        if r not in sample_strs:
            L.append(f"{p} = {r}")
    L += ["", "## Names", ""]
    for p, r in NAMES.items():
        if p not in sample_names:
            L.append(f"{p} = {r}")
    L += ["", "## «Katame dhammā kusalā? Yasmiṃ samaye …» sentences", "",
          f"Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti … = {KAMA_V}…"]
    for p, r in INTROS.items():
        L.append(f"Yasmiṃ samaye {p.strip()} … = {r}…")
    L += [f"…, tasmiṃ samaye F hoti… = …, thì {TS} có F…  (after «–»: … – thì {TS} có F…)",
          "Joining: every piece and every description is joined with «, »; «…pe…» between pieces = «… ».",
          f"N jhānaṃ upasampajja viharati = {enter('paṭhamaṃ').replace('{V}', '')} (N: "
          + ", ".join(f"{p} = {w}" for p, w in ORD.items()) + "); its qualities follow it, joined with «, »",
          f"N jhānaṃ (bare, in a …pe… run) = {JH} N"]
    for p, pcs in PIECES.items():
        if p in DESC or re.fullmatch(r"\S+ jhānaṃ(?: upasampajja viharati)?", p):
            continue
        L.append(f"{p} = " + " | ".join(x.replace("{V}", "") for x in pcs))
    L += ["", "### Descriptions of the absorption", ""]
    for p, r in DESC.items():
        L.append(f"{p} = {r.replace('{V}', '')}")
    L += ["", "### Attributes of the sense-sphere mind", ""]
    for p, r in ATTR.items():
        L.append(f"{p} = {r}")
    L += ["", "## Headings and closing lines", ""]
    for p, r in EXACT.items():
        L.append(f"{p} = {r}")
    L += ["", "## Variant sigla", "", "(bahūsu) = (nhiều ấn bản)", ""]
    (HERE / "notes-2-01_2-02.md").write_text(unicodedata.normalize("NFC", "\n".join(L)), encoding="utf-8",
                                             newline="\n")
    print("wrote", HERE / "notes-2-01_2-02.md")


def main():
    assert selftest()
    notes()
    for fn_name, fn in (("2-01-cittuppadakandam.md", build_2_01), ("2-02-cittuppadakandam.md", build_2_02)):
        text, n = fn()
        (OUT / fn_name).write_text(unicodedata.normalize("NFC", text), encoding="utf-8", newline="\n")
        print("wrote", OUT / fn_name, n, "segments")


if __name__ == "__main__":
    main()
