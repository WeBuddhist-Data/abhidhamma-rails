"""Consistency (harmonise) pass for the pi-7 Hindi plain zero-shot (Paṭṭhāna).

Applies fixed old -> new strings (some regex patterns, kind "rx"; kind "fn" rules get the whole Hindi line and
return (line, n)) to the Hindi chapter files. A rule touches a Hindi line ONLY when the aligned Pāli line
(non-empty line i <-> non-empty line i) matches the rule's Pāli pattern, and only in the files whose name starts
with one of the rule's prefixes (None = all files).
Line counts, block IDs, heading levels, dashes and '[' counts are never touched (asserted per changed line).
Protected (user-approved, never changed): preamble.md, 1-00-paccaya.md, 1-01-kusalattika.md non-empty lines
1-190 and 1235-1262 (the sample).
Backup of the pre-pass files: backup-pre-harmonise/ (made once, if missing). The pass always reads from the
backup, so rerunning it rebuilds the same output. Log: harmonise-log.tsv (rule, file, replacements, lines).

usage: python -I -B -X utf8 harmonise_hi.py [--dry]
"""
import os, re, sys, shutil, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hz7_common as C  # noqa: E402
from hz7_common import PARTS, PDIR, HDIR, BAK  # noqa: E402

PROTECTED = {"preamble": None, "1-00-paccaya": None, "1-01-kusalattika": [(1, 190), (1235, 1262)]}
DEV = "ऀ-ॣ०-ॿ"  # Devanagari letters and digits, not the dandas
E = r"(?![" + DEV + r"])"       # end of a Devanagari word
B = r"(?<![" + DEV + r"-])"      # start of a Devanagari word

R = []  # (id, pali_regex, old, new, kind, prefixes)


def rule(rid, pali, old, new, kind="str", files=None):
    R.append((rid, pali, old, new, kind, files))


# ============================================================================================= 1. names
# One name per triad / dyad = the name in its own file (1-xx/2-xx triads, 3-xx/4-01 dyads); names that are a
# participle with a complement + «वाला» («कर्म से उत्पन्न वाला») get the pi-1 item noun «परिघटनाओं».
# "{v}" = the agreeing «वाला/वाले» inside a name.
TIKA = {
    "kusalattika": "हितकर",
    "vedanāttika": "अनुभूति",
    "vipākattika": "कर्म-फल",
    "upādinnattika": "कर्म से उत्पन्न परिघटनाओं",
    "saṃkiliṭṭhattika": "क्लेशों से मलिन परिघटनाओं",
    "vitakkattika": "आरंभिक विचार",
    "pītittika": "उल्लास",
    "dassanenapahātabbattika": "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं",
    "dassanenapahātabbahetukattika": "सत्य-दर्शन से छोड़े जाने वाले मूलों",
    "ācayagāmittika": "संचय की ओर ले जाने",
    "sekkhattika": "सीखने के चरण",
    "parittattika": "सीमित",
    "parittārammaṇattika": "सीमित विषय",
    "hīnattika": "हीन",
    "micchattaniyatattika": "ग़लत दिशा में निश्चित परिघटनाओं",
    "maggārammaṇattika": "मार्ग को विषय बनाने",
    "uppannattika": "उत्पन्न",
    "atītattika": "अतीत",
    "atītārammaṇattika": "अतीत के विषय",
    "ajjhattattika": "स्वयं से संबंधित परिघटनाओं",
    "ajjhattārammaṇattika": "स्वयं से संबंधित विषय",
    "sanidassanasappaṭighattika": "दिखाई देने {v} और टकराव",
}
TIKA_ALIAS = {"dassanattika": "dassanenapahātabbattika", "dassanahetuttika": "dassanenapahātabbahetukattika",
              "dassanahetukattika": "dassanenapahātabbahetukattika", "micchattattika": "micchattaniyatattika",
              "sanidassanattika": "sanidassanasappaṭighattika"}
DUKA = {
    "hetuduka": "मूल",
    "sahetukaduka": "मूल वाली परिघटनाओं",
    "hetusampayuttaduka": "मूलों से जुड़ी परिघटनाओं",
    "hetusahetukaduka": "मूल रूपी भी और मूल वाली भी परिघटनाओं",
    "hetuhetusampayuttaduka": "मूल रूपी भी और मूलों से जुड़ी भी परिघटनाओं",
    "nahetusahetukaduka": "मूल रूपी न होने वाली, पर मूल वाली परिघटनाओं",
    "sappaccayaduka": "कारणों पर निर्भर रहने वाली परिघटनाओं",
    "saṅkhataduka": "निर्मित परिघटनाओं",
    "sanidassanaduka": "दिखाई देने वाली परिघटनाओं",
    "sappaṭighaduka": "टकराव वाली परिघटनाओं",
    "rūpīduka": "भौतिक परिघटनाओं",
    "lokiyaduka": "लौकिक परिघटनाओं",
    "kenaciviññeyyaduka": "किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाओं",
    "āsavaduka": "मन के मैल",
    "sāsavaduka": "मन के मैलों के विषय",
    "āsavasampayuttaduka": "मन के मैलों से जुड़ाव",
    "āsavasāsavaduka": "मन के मैल और मन के मैलों के विषय",
    "āsavaāsavasampayuttaduka": "मन के मैल और मन के मैलों से जुड़ाव",
    "āsavavippayuttasāsavaduka": "मन के मैलों से अलगाव और मन के मैलों के विषय",
    "saññojanaduka": "बंधन",
    "saññojaniyaduka": "बंधनों के विषय",
    "saññojanasampayuttaduka": "बंधनों से जुड़ाव",
    "saññojanasaññojaniyaduka": "बंधन और बंधनों के विषय",
    "saññojanasaññojanasampayuttaduka": "बंधन और बंधनों से जुड़ाव",
    "saññojanavippayuttasaññojaniyaduka": "बंधनों से अलगाव और बंधनों के विषय",
    "ganthaduka": "गाँठ",
    "ganthaniyaduka": "गाँठों के विषय",
    "ganthasampayuttaduka": "गाँठों से जुड़ाव",
    "ganthaganthaniyaduka": "गाँठ और गाँठों के विषय",
    "ganthaganthasampayuttaduka": "गाँठ और गाँठों से जुड़ाव",
    "ganthavippayuttaganthaniyaduka": "गाँठों से अलगाव और गाँठों के विषय",
    "nīvaraṇaduka": "बाधा",
    "nīvaraṇiyaduka": "बाधाओं के विषय",
    "nīvaraṇasampayuttaduka": "बाधाओं से जुड़ाव",
    "nīvaraṇanīvaraṇiyaduka": "बाधा और बाधाओं के विषय",
    "nīvaraṇanīvaraṇasampayuttaduka": "बाधा और बाधाओं से जुड़ाव",
    "nīvaraṇavippayuttanīvaraṇiyaduka": "बाधाओं से अलगाव और बाधाओं के विषय",
    "parāmāsaduka": "ग़लत धारणा",
    "parāmaṭṭhaduka": "ग़लत धारणा के विषय",
    "parāmāsasampayuttaduka": "ग़लत धारणा से जुड़ाव",
    "parāmāsaparāmaṭṭhaduka": "ग़लत धारणा और ग़लत धारणा के विषय",
    "parāmāsavippayuttaparāmaṭṭhaduka": "ग़लत धारणा से अलगाव और ग़लत धारणा के विषय",
    "sārammaṇaduka": "विषय वाली परिघटनाओं",
    "cittaduka": "मन रूपी परिघटनाओं",
    "cetasikaduka": "मन की सहचर परिघटनाओं",
    "cittasampayuttaduka": "मन से जुड़ी परिघटनाओं",
    "cittasaṃsaṭṭhaduka": "मन से घुली-मिली परिघटनाओं",
    "cittasamuṭṭhānaduka": "मन से उत्पन्न परिघटनाओं",
    "cittasahabhūduka": "मन के साथ-साथ होने वाली परिघटनाओं",
    "cittānuparivattiduka": "मन का अनुसरण करने वाली परिघटनाओं",
    "cittasaṃsaṭṭhasamuṭṭhānaduka": "मन से घुली-मिली और मन से उत्पन्न परिघटनाओं",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhūduka": "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली परिघटनाओं",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattiduka": "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली परिघटनाओं",
    "ajjhattikaduka": "आंतरिक परिघटनाओं",
    "upādāduka": "व्युत्पन्न परिघटनाओं",
    "upādinnaduka": "कर्म से उत्पन्न परिघटनाओं",
    "upādānaduka": "आसक्ति",
    "upādāniyaduka": "आसक्ति का विषय बनने वाली परिघटनाओं",
    "upādānasampayuttaduka": "आसक्ति से जुड़ी परिघटनाओं",
    "upādānaupādāniyaduka": "आसक्ति रूपी भी और आसक्ति का विषय बनने वाली भी परिघटनाओं",
    "upādānaupādānasampayuttaduka": "आसक्ति रूपी भी और आसक्ति से जुड़ी भी परिघटनाओं",
    "upādānavippayuttaupādāniyaduka": "आसक्ति से अलग, पर उसका विषय बनने वाली परिघटनाओं",
    "kilesaduka": "मन के क्लेश",
    "saṃkilesikaduka": "क्लेशों का विषय बनने",
    "saṃkiliṭṭhaduka": "क्लेशों से मलिन परिघटनाओं",
    "kilesasampayuttaduka": "क्लेशों से जुड़ाव",
    "kilesasaṃkilesikaduka": "मन के क्लेश और क्लेशों का विषय बनने",
    "kilesasaṃkiliṭṭhaduka": "मन के क्लेश और क्लेशों से मलिन परिघटनाओं",
    "kilesakilesasampayuttaduka": "मन के क्लेश और क्लेशों से जुड़ाव",
    "kilesavippayuttasaṃkilesikaduka": "क्लेशों से अलगाव और क्लेशों का विषय बनने",
    "dassanenapahātabbaduka": "सत्य-दर्शन से छोड़े जाने",
    "bhāvanāyapahātabbaduka": "मानसिक अभ्यास से छोड़े जाने",
    "dassanenapahātabbahetukaduka": "सत्य-दर्शन से छोड़े जाने वाले मूलों",
    "bhāvanāyapahātabbahetukaduka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों",
    "savitakkaduka": "आरंभिक विचार",
    "savicāraduka": "सतत विचार",
    "sappītikaduka": "उल्लास",
    "pītisahagataduka": "उल्लास के साथ होने",
    "sukhasahagataduka": "सुख के साथ होने",
    "upekkhāsahagataduka": "समभाव के साथ होने",
    "kāmāvacaraduka": "इंद्रिय-सुखों के लोक",
    "rūpāvacaraduka": "सूक्ष्म भौतिक लोक",
    "arūpāvacaraduka": "अभौतिक लोक",
    "pariyāpannaduka": "अस्तित्व के लोकों में समाए होने",
    "niyyānikaduka": "मुक्ति की ओर ले जाने",
    "niyataduka": "निश्चित",
    "sauttaraduka": "सर्वोच्च न होने",
    "saraṇaduka": "संघर्ष",
}
DUKA_ALIAS = {"saṃkilesasaṃkilesikaduka": "kilesasaṃkilesikaduka"}
# extra variants seen outside headings (cross-references, notes)
EXTRA = {"micchattaniyatattika": ["ग़लत दिशा", "ग़लत दिशा में निश्चितता"],
         "saṃkiliṭṭhattika": ["क्लेशों से मलिनता"], "saṃkiliṭṭhaduka": ["क्लेशों से मलिनता"],
         "kilesasaṃkiliṭṭhaduka": ["मन के क्लेश और क्लेशों से मलिनता"],
         # forms in «…ādidukāni» headings (not in the inventory, which skips ādi headings)
         "saññojanaduka": ["बंधन रूपी परिघटनाओं"], "upādānaduka": ["आसक्ति रूपी परिघटनाओं"],
         "ganthaduka": ["गाँठ रूपी परिघटनाओं"], "nīvaraṇaduka": ["बाधा रूपी परिघटनाओं"],
         "parāmāsaduka": ["ग़लत धारणा रूपी परिघटनाओं"], "kilesaduka": ["मन के क्लेश रूपी परिघटनाओं"],
         "āsavaduka": ["मन के मैल रूपी परिघटनाओं"], "sahetukaduka": ["मूल-सहित"]}


def _stem_rx(stem):
    if stem.endswith("ttika"):
        base, tail = stem[:-5], r"-?t?tik"
    elif stem.endswith("duka"):
        base, tail = stem[:-4], r"-?duk"
    else:
        raise ValueError(stem)
    if base.endswith("a"):
        return re.compile(re.escape(base[:-1]) + r"(?:a|ādi)" + tail)
    return re.compile(re.escape(base) + r"(?:ādi)?" + tail)


def _vrx(x):
    """name text -> regex; inner «वाला/वाले» (and {v}) agree with the suffix"""
    s = re.escape(x.replace("{v}", "वाला"))
    return s.replace("वाला", "वा(?:ला|ले)")


SUF = {"t": r" वा(ला|ले) (दोनों )?तीन (का|के) वर्गीकरण", "d": r" वा(ला|ले) (दोनों )?दो (का|के) वर्गीकरण"}
NAMES = []  # (pali_rx, kind, canonical, [variant regexes])


def _build_names():
    import hz7_names
    save = C.CUR["hdir"]
    C.CUR["hdir"] = BAK
    inv, _ = hz7_names.collect()
    C.CUR["hdir"] = save
    var = collections.defaultdict(set)
    for stem, forms in inv.items():
        base = TIKA_ALIAS.get(stem, DUKA_ALIAS.get(stem, stem))
        if base.endswith("ttikadvaya"):
            base = base[:-5]
        for h in forms:
            h = h.strip("“”")
            m = re.match(r"^(.*?) वा(?:ला|ले) (?:दोनों )?(?:तीन|दो) (?:का|के) वर्गीकरण(?: आदि)?$", h)
            if m:
                var[base].add(m.group(1))
    for stem, x in list(TIKA.items()) + list(DUKA.items()):
        kind = "t" if stem in TIKA else "d"
        stems = [stem] + [a for a, b in list(TIKA_ALIAS.items()) + list(DUKA_ALIAS.items()) if b == stem]
        vs = (var.get(stem, set()) | set(EXTRA.get(stem, []))) - {x.replace("{v}", "वाला")}
        NAMES.append(([_stem_rx(s) for s in stems], kind, x, sorted(vs, key=len, reverse=True)))


OKPREV = ("और", "तथा", "जैसे", "भी")


def _left_ok(h, start):
    pre = h[:start].rstrip(" ")
    if not pre:
        return True
    if pre[-1] in "#*(“.,:;।–-[0123456789":
        return True
    w = pre.split(" ")[-1]
    return w in OKPREV


def names_fn(h, p, ctx):
    pl = p.lower()
    cands = []
    for rxs, kind, x, vs in NAMES:
        if not any(r.search(pl) for r in rxs):
            continue
        cands.append((x, kind, x))
        for v in vs:
            cands.append((v, kind, x))
    if not cands:
        return h, 0
    cands.sort(key=lambda c: -len(c[0]))
    claimed = []  # (start, end, replacement)
    for v, kind, x in cands:
        rx = re.compile(_vrx(v) + SUF[kind])
        for m in rx.finditer(h):
            s, e = m.start(), m.end()
            if any(not (e <= a or s >= b) for a, b, _ in claimed):
                continue
            if not _left_ok(h, s):
                continue
            full = m.group(0)
            suffix = full[len(_strip_x(full)):]
            g = re.match(r" वा(ला|ले)", suffix).group(1)
            claimed.append((s, e, x.replace("{v}", "वा" + g) + suffix))
    n = 0
    out = h
    for s, e, rep in sorted(claimed, key=lambda c: -c[0]):
        if out[s:e] != rep:
            out = out[:s] + rep + out[e:]
            n += 1
    return out, n


def _strip_x(full):
    """return the length of the name part (before the suffix) of a matched name"""
    m = re.search(r" वा(?:ला|ले) (?:दोनों )?(?:तीन|दो) (?:का|के) वर्गीकरण$", full)
    return full[:m.start()]


rule("N1-names", r".", None, names_fn, "fnp")

# quotes around a whole name in closing lines (2-01..2-03: «“<name>” समाप्त»)
rule("N2-closing-quotes", r"niṭṭhit", r"“([^“”]*(?:वर्गीकरण|वर्ग))” (समाप्त|पूरा हुआ|पूरे हुए)", r"\1 \2", "rx")

# ============================================================================================= 2. frames
# Paccanīyuddhāro = 1-01 «नकारात्मक क्रम के लिए कारणों की छँटाई»
rule("F1-paccaniyuddhara", r"Paccanīyuddhār",
     r"नकारात्मक क्रम के लिए (?:छँटाई|चयन|कारणों का चयन|कारणों का संकलन|उद्धरण)" + E,
     "नकारात्मक क्रम के लिए कारणों की छँटाई", "rx")
# niṭṭhitaṃ / niṭṭhito = 1-01 «समाप्त»
rule("F2-nitthita", r"niṭṭhit", r"(?:पूरा हुआ|पूरे हुए|पूरी हुई)" + E, "समाप्त", "rx")

# pañhāvāra sub-kind labels = 1-01 «सह-उत्पत्ति / पूर्व-उत्पत्ति / पश्चात्-उत्पत्ति / आहार / क्षमता / भिन्न क्षण»
LABEL_P = (r"(^|[.–,;…] ?|\(\d\) )([Ss]ahajāt(aṃ|ā|o)|[Pp]urejātaṃ|[Pp]acchājāt(aṃ|ā|o)|[Nn]ānākkhaṇikā|"
           r"[Āā]hāraṃ|[Ii]ndriyaṃ)\s*[–,.]")
LAB_END = r"(?=[,।:;…)]| –|$| \(| भी| \[)"
rule("F3-labels", LABEL_P, B + r"(सह-उत्पत्ति|पूर्व-उत्पत्ति|पश्चात्-उत्पत्ति|आहार|क्षमता|भिन्न क्षण) रूपी" + LAB_END,
     r"\1", "rx")
rule("F3-labels", r"[Nn]ānākkhaṇik", r"(?:भिन्न क्षणों वाला|भिन्न-क्षणिक)" + LAB_END, "भिन्न क्षण", "rx")

# moment words (1-01): anuloma «अनुरूपता», cuti «मृत्यु का मन», upapatti «जन्म का मन», parikamma «प्रारंभिक तैयारी»
rule("M1-anuloma", r"[Aa]nuloma[ṃ]? (gotrabhu|vodān|phalasam|maggassa|arahatt)", r"अनुकूलता(?: का क्षण)?" + E, "अनुरूपता", "rx")
rule("M2-cuti", r"[Cc]uticitt", r"मृत्यु-क्षण (का|के) मन" + E, r"मृत्यु \1 मन", "rx")
rule("M3-upapatti", r"[Uu]papatticitt", B + r"(?:जन्म-क्षण|उत्पत्ति) (का|के) मन" + E, r"जन्म \1 मन", "rx")
rule("M4-parikamma", r"[Pp]arikamm", r"प्रारंभिक अभ्यास" + E, "प्रारंभिक तैयारी", "rx")
rule("M4-parikamma", r"[Pp]arikamm", r"(?<!प्रारंभिक )" + B + r"तैयारी" + E, "प्रारंभिक तैयारी", "rx")
# vuṭṭhāna = 1-01 «बाहर आना / बाहर आने के लिए»
rule("M5-vutthana", r"[Vv]uṭṭhān", B + r"उत्थान के लिए", "बाहर आने के लिए", "rx")
rule("M5-vutthana", r"[Vv]uṭṭhān", B + r"उत्थान भी", "बाहर आना भी", "rx")
rule("M5-vutthana", r"[Vv]uṭṭhān", r"बाहर आने वाले मन के लिए", "बाहर आने के लिए", "str")
rule("M5-vutthana", r"[Vv]uṭṭhān", r"बाहर आने वाले (सीमित|उन्नत|अपरिमित) मन के लिए", r"\1 बाहर आने के लिए", "rx")
# nirodhā vuṭṭhahantassa = 1-01 «समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में»
rule("M6-nirodha", r"vuṭṭhahantassa",
     r"(?:समाप्ति की ध्यान-अवस्था|निरोध की ध्यान-अवस्था|निरोध) से (?:उठने वाले|बाहर आ रहे|बाहर आने वाले) (?:व्यक्ति (?:में|का|के लिए)|के लिए)",
     "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में", "rx")

# ghaṭanā = 1-01 «संयोजन»; sāmañña «सामान्य»; sabhāga «साथी कारण»
rule("G1-ghatana", r"ghaṭan", r"(\S+-कारण) वाले साझा मेल" + E, r"\1 के सामान्य संयोजन", "rx")
rule("G1-ghatana", r"ghaṭan", r"(\S+-कारण) वाले (मेल|संयोजन)" + E, r"\1 के संयोजन", "rx")
rule("G1-ghatana", r"[Pp]akiṇṇakaghaṭan", r"मिश्रित संयोजन" + E, "फुटकर संयोजन", "rx")
rule("G1-ghatana", r"ghaṭan", r"(?<!कारणों का )" + B + r"मेल" + E, "संयोजन", "rx")
NTI = r"-\s?[A-Za-zĀāĪīŪūṃñṅṭḍṇḷ]+nti\b"
rule("G2-ghatana-count", NTI, r"“([^“”]*)” के (?:मेल|संयोजन)", r"\1 के संयोजन", "rx")
rule("G3-sabhaga", r"sabhāg", "सहभागी कारण", "साथी कारण", "str")

# gamana = «प्रसंग» (majority; «क्रम» is the word for anuloma / paccanīya)
rule("G4-gamana", r"gaman", B + r"(वही|पहले|पहला|दूसरे|दूसरा|पिछले|यह|तीन|समान|का|के|वाले) (?:क्रम|दौर)(?=[ )।,]|$)", r"\1 प्रसंग", "rx")

# cakkaṃ = 1-01 «चक्र» («Cakkaṃ bandhitabbaṃ = चक्र बाँधना चाहिए»)
rule("G5-cakka", r"\([Cc]akkaṃ\)", "(बारी-बारी से)", "(चक्र)", "str")
rule("G5-cakka", r"[Cc]akkaṃ bandhitabb", "चक्र जोड़ना चाहिए", "चक्र बाँधना चाहिए", "str")
rule("G5-cakka", r"[Cc]akkaṃ", "सबको बारी-बारी से करना चाहिए", "सबका चक्र बनाना चाहिए", "str")
rule("G5-cakka", r"[Cc]akkaṃ", "बारी-बारी से करना चाहिए", "चक्र बनाना चाहिए", "str")
rule("G5-cakka", r"[Cc]akkaṃ", r"\(बारी-बारी से(?=[।,])", "(चक्र", "rx")
# ninnānākaraṇaṃ / ninnānaṃ = «बिना किसी अंतर के» (58 of 84)
rule("G7-ninnana", r"ninnān", r"बिना किसी भिन्नता के|बिना अंतर के|कोई अंतर नहीं" + E, "बिना किसी अंतर के", "rx")

# sabhāga, mūla (series start): «… से शुरू होने वाली शृंखला (में)» (terms file: Āsevanamūlake)
rule("G6-mulaka", r"mūlake", r"से शुरू होने वाले में" + E, "से शुरू होने वाली शृंखला में", "rx")
rule("G6-mula-sentence", r"[Mm]ūlaṃ (kātabb|pucchitabb)", r"(?:आरंभिक पद|मूल पद)" + E, "मूल वाक्य", "rx")

# double negation and negated items: no quotation marks around items (5-13..5-20)
F5 = ("5-13", "5-14", "5-15", "5-16", "5-17", "5-18", "5-19", "5-20")
NEGQ = re.compile(r"“([^“”]+)” न होने वा(ली|ले|ला)")


def negq_fn(h, ctx):
    n, s = 0, h
    while True:  # nested quotes («““X” न होने वाली” न होने वाली») need several passes
        s2, k = NEGQ.subn(r"\1 न होने वा\2", s)
        if not k:
            break
        s, n = s2, n + k
    return s, n


rule("D1-neg-quotes", r".", None, negq_fn, "fn", F5)

# mūla (start of a series, item-based) in 5-13..5-20: «<item> परिघटना वाले आरंभ-बिंदु» = «… से शुरू होने वाली
# शृंखला» (terms file: Āsevanamūlake = «पुनरावृत्ति-कारण से शुरू होने वाली शृंखला में»)
MUL = r"mūl"
rule("G6-mula-series", MUL, "वाला एक आरंभ-बिंदु", "से शुरू होने वाली एक शृंखला", "str", F5)
rule("G6-mula-series", MUL, r"वाले आरंभ-बिंदु (सात ही|,)", r"से शुरू होने वाली शृंखलाएँ \1", "rx", F5)
rule("G6-mula-series", MUL, "वाले आरंभ-बिंदु भी बनाने चाहिए", "से शुरू होने वाली शृंखला भी बनानी चाहिए", "str", F5)
rule("G6-mula-series", MUL, "वाले आरंभ-बिंदु", "से शुरू होने वाली शृंखला", "str", F5)
rule("G6-mula-series", MUL, r"(दो|तीन) आरंभ-बिंदु", r"\1 शृंखलाएँ", "rx", F5)

# na + an item that is itself a pi-1 matrix item (dyads 83-86, 90-92: «सत्य-दर्शन से न छोड़ी जाने वाली»,
# «… मूलों से रहित», «उल्लास के साथ न होने वाली»): the pi-1 wording (5-04, 5-13..5-20), not «<item> न होने वाली»
AGR = {"ली": "ी", "ले": "े", "ला": "ा"}
rule("D2-pi1-na-items", r"\b[Nn]a ?(dassanena|bhāvanāya) pahātabbahetuk",
     r"(?<!न )(सत्य-दर्शन|मानसिक अभ्यास) से छोड़े जाने वाले मूलों वा(?:ली|ले|ला) न होने वा(?:ली|ले|ला)" + E,
     r"\1 से छोड़े जाने वाले मूलों से रहित", "rx")
rule("D2-pi1-na-items", r"\b[Nn]a ?(dassanena|bhāvanāya) pahātabb(?!ahetuk)",
     re.compile(r"(?<!न )(सत्य-दर्शन|मानसिक अभ्यास) से छोड़(?:ी|े|ा) जाने वा(?:ली|ले|ला) न होने वा(ली|ले|ला)" + E),
     lambda m: f"{m.group(1)} से न छोड़{AGR[m.group(2)]} जाने वा{m.group(2)}", "rxf")
rule("D2-pi1-na-items", r"\b[Nn]a ?(pīti|sukha|upekkhā)sahagat",
     r"(उल्लास|सुख|समभाव) के साथ होने वा(?:ली|ले|ला) न होने वा(ली|ले|ला)" + E, r"\1 के साथ न होने वा\2", "rx")

# āvajjanā = 1-01 «मन को विषय की ओर मोड़ना» (2-04..2-08 had «… मोड़ने की क्रिया»)
rule("M7-avajjana", r"[Āā]vajjan", r"मन को विषय की ओर मोड़ने की (\S+ विषय) वाली क्रिया के लिए",
     r"\1 वाले मन को विषय की ओर मोड़ने के लिए", "rx")
rule("M7-avajjana", r"[Āā]vajjan", r"मन को विषय की ओर मोड़ने की क्रिया ([^।;…–,]*?)कारण होती है",
     r"मन को विषय की ओर मोड़ना \1कारण होता है", "rx")
rule("M7-avajjana", r"[Āā]vajjan", r"मन को विषय की ओर मोड़ने की क्रिया" + E, "मन को विषय की ओर मोड़ना", "rx")


# bhavaṅga = 1-01 «जीवन-धारा» (feminine, as 1-01..1-05); other files had «जीवन-धारा का मन» / «जीवन-प्रवाह» (masc.)
def bhavanga_fn(h, ctx):
    s = h
    s = re.sub(r"जीवन-धारा का (उन्नत|सीमित|अपरिमित)( विषय वाला)? मन" + E,
               lambda m: m.group(1) + (" विषय वाली" if m.group(2) else "") + " जीवन-धारा", s)
    s = s.replace("जीवन-धारा के मन के", "जीवन-धारा के").replace("जीवन-धारा का मन", "जीवन-धारा")
    s = re.sub(r"जीवन-धारा के मन" + E, "जीवन-धारा", s)
    s = s.replace("जीवन-प्रवाह", "जीवन-धारा")
    s = re.sub(B + r"(वाला|वाले) जीवन-धारा", "वाली जीवन-धारा", s)
    s = re.sub(B + r"(जुड़ा|जुड़े) जीवन-धारा", "जुड़ी जीवन-धारा", s)
    s = re.sub(B + r"वाल[ाे]( और|,) ((?:(?!वाल[ाे])[^…,।;–])*?) जीवन-धारा", r"वाली\1 \2 जीवन-धारा", s)
    # verb of a clause whose subject is the bhavaṅga
    s = re.sub(r"((?:^|[।;…–]\s*|होता है\s+)(?:(?!के लिए|परिघटना|[।;…–]).)*?जीवन-धारा (?!के )(?:(?![।;…–,]).)*?)कारण होता है",
               r"\1कारण होती है", s)
    return s, int(s != h)


rule("M8-bhavanga", r"[Bb]havaṅg", None, bhavanga_fn, "fn")

# 3-01, 3-02, 3-10 put the verb once at the end of a pañhā chain («X-कारण के रूप में… Y-कारण के रूप में कारण होती
# है»); 1-01 and every other file repeat it after each condition
rule("P1-chain-verb", r"paccayena paccayo\s*(…|…pe…|,)",
     r"((?:पूर्ण |प्रबल )?\S+-कारण(?: के अभाव)? के रूप में)(?=(?:…|, | …)[^।;–?]*? के रूप में कारण (होता|होती|होते) (हैं|है))",
     r"\1 कारण \2 \3", "rx", ("3-01", "3-02", "3-10"))

# section names: «2-6. … और जुड़ाव का खंड» (vāro, singular; 11 of 19 headings)
rule("S1-vara", r"^#.*sampayuttavāro", "और जुड़ाव के खंड", "और जुड़ाव का खंड", "str")
# «X-कारण, Y-कारण आदि» headings = terms file «Hetu-ārammaṇapaccayā = मूल-कारण और विषय-कारण»
CN = r"(?:पूर्ण |प्रबल )?\S+-कारण(?: का अभाव)?"
rule("S2-adi-heading", r"^#.*paccayādi", r"(" + CN + r"), (" + CN + r") आदि", r"\1 और \2 आदि", "rx")
# «X का खंड के समान» (2-10, 2-15) = «X के खंड के समान»
rule("S3-sadisa-oblique", r"vārasadis", r"(\S+) का खंड के समान", r"\1 के खंड के समान", "rx")


# {…} editorial notes / queries without a siglum: «[पाठभेद: <Pāli>]» like the sigla variants (5-15)
def brace_fn(h, p, ctx):
    pb = re.findall(r"\{([^}]*)\}", p)
    hb = list(re.finditer(r"\[[^\]]*\]", h))
    if len(pb) != len(hb):
        return h, 0
    out, last, n = "", 0, 0
    for inner, m in zip(pb, hb):
        new = m.group(0)
        if "(" not in inner and not m.group(0).startswith("[पाठभेद"):
            new = f"[पाठभेद: {inner.strip()}]"
            n += 1
        out += h[last:m.start()] + new
        last = m.end()
    return out + h[last:], n


rule("B1-brace-notes", r"\{[^}(]*\}", None, brace_fn, "fnp")

# count lines: no comma between consecutive locatives where the Pāli has none (sample count_hi; 4-02..4-07 added them)
LOCS = ("hetuyā|ārammaṇe|adhipatiyā|anantare|samanantare|sahajāte|aññamaññe|nissaye|upanissaye|purejāte|"
        "pacchājāte|āsevane|kamme|vipāke|āhāre|indriye|jhāne|magge|sampayutte|vippayutte|atthiyā|natthiyā|"
        "vigate|avigate")
PLOC = re.compile(r"(?<![\w-])(?:[Nn][ao] ?)?(?:" + LOCS + r")(?![\w-])", re.I)
HLOC = re.compile(r"(?:पूर्ण |प्रबल )?\S+-कारण(?: के अभाव)? में")


def count_comma_fn(h, p, ctx):
    pm = list(PLOC.finditer(p))
    hm = list(HLOC.finditer(h))
    if len(pm) < 2 or len(pm) != len(hm):
        return h, 0
    out, n = h, 0
    for i in range(len(pm) - 1, 0, -1):
        between_p = p[pm[i - 1].end():pm[i].start()]
        a, b = hm[i - 1].end(), hm[i].start()
        if between_p.strip() == "" and out[a:b] == ", ":
            out = out[:a] + " " + out[b:]
            n += 1
    return out, n


rule("C1-count-commas", r"^[^–]*\b(" + LOCS + r") (" + LOCS + r")\b", None, count_comma_fn, "fnp",
     ("4-02", "4-03", "4-04", "4-05", "4-06", "4-07"))

# ============================================================================================= 3. whole lines
# identical Pāli -> identical Hindi: (ref part, ref non-empty line, literal or None). Every line whose Pāli equals the
# ref's Pāli (ID and final count marker aside) gets the ref's Hindi body (after the rules above), or the literal.
WL = [
    ("4-02-dukatika-hetuduka", 59, None),          # Yathā kusalattike … gaṇitaṃ, evaṃ gaṇetabbaṃ (73 of 83)
    ("4-02-dukatika-hetuduka", 1079, None),        # … gaṇitaṃ evaṃ gaṇetabbaṃ (no comma)
    ("4-13-dukatika-dassanenapahatabbaduka", 78, None),   # Yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ (52 of 83)
    ("4-13-dukatika-dassanenapahatabbaduka", 103, None),  # … pañhāvāraṃ evaṃ vitthāretabbaṃ
    ("4-15-tikaduka-hetuduka", 1104, None),        # Sahajātavārampi…pe… sampayuttavārampi paṭiccavārasadisaṃ
    ("4-01-kilesagocchaka", 82, None),             # Evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo (11 of 20)
    ("4-01-kilesagocchaka", 72, None),             # Evaṃ itare dve gaṇanāpi nissayavāropi kātabbo
    ("4-01-kilesagocchaka", 360, None),            # Evaṃ itare dve gaṇanāpi sahajātavāropi … paṭiccavārasadisā
    ("3-04-sannojanagocchaka", 258, "(अन्य दो गणनाएँ भी और जुड़ाव का खंड भी तैयार करना चाहिए।)"),
    ("3-08-paramasagocchaka", 217, "(इसी तरह अन्य दो गणनाएँ भी और जुड़ाव के खंड भी तैयार करने चाहिए।)"),
    ("4-09-dukatika-paramasaduka", 40, None),      # Sahajātavārepi …pe… pañhāvārepi sabbattha ekaṃ
    ("5-02-anuloma-dukaduka", 17, None),           # … paṭiccavārasadisaṃ (commas)
    ("2-02-pitittika", 65, None),                  # … paṭiccavārasadisā
    ("4-02-dukatika-hetuduka", 28, None),          # … paṭiccavārasadisā vitthāretabbā
    ("4-15-tikaduka-hetuduka", 488, None),         # … paṭiccavārasadisaṃ vitthāretabbaṃ
    ("5-17-paccaniyanuloma-dukatika", 321, None),  # … sampayuttavārampi vitthāretabbaṃ
    ("4-01-kilesagocchaka", 163, None),            # (anulomamātikā kātabbā): 1-01 kātabba = बनाना
    ("3-07-nivaranagocchaka", 161, None),          # (anulomamātikā)
    ("2-03-dassanenapahatabbattika", 150, None),   # count line with note «(इसी तरह …»
    ("4-01-kilesagocchaka", 487, None),            # purimā purimā … without commas (sample)
    ("3-06-oghayogagocchaka", 2, None),            # heading Oghādidukāni (own file)
    ("3-04-sannojanagocchaka", 338, None),         # Natthipaccayena paccayo… (continuation; subject «X और Y परिघटनाएँ» = plural)
]


# ============================================================================================= runner
def nonempty_idx(lines):
    return [i for i, l in enumerate(lines) if l.strip()]


def dashes(t):
    return t.count("—") + t.count("–")


def protected(part, k):
    if part not in PROTECTED:
        return False
    rng = PROTECTED[part]
    return rng is None or any(a <= k + 1 <= b for a, b in rng)


def main(dry=False):
    if not os.path.isdir(BAK):
        os.makedirs(BAK)
        for part in PARTS:
            shutil.copy2(os.path.join(HDIR, part + ".md"), os.path.join(BAK, part + ".md"))
        print("backup made:", BAK)
    _build_names()
    log = collections.defaultdict(lambda: [0, 0])  # (rid, part) -> [replacements, lines]
    changed_lines = collections.Counter()
    hit_idx = set()
    blocked = []
    comp = []
    for rid, p, old, new, kind, files in R:
        o = re.compile(old) if kind == "rx" else old
        comp.append((rid, re.compile(p), o, new, kind, files))
    data = {}
    # ---- phase 1: rules
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        raw = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        bom = raw.startswith("﻿")
        text = raw.lstrip("﻿")
        assert "\r" not in text, part
        el = text.split("\n")
        idx = nonempty_idx(el)
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        orig = list(el)
        for k, li in enumerate(idx):
            p, e0 = pl[k], el[li]
            e = e0
            for ri, (rid, pr, old, new, kind, files) in enumerate(comp):
                if files and not part.startswith(files):
                    continue
                if not pr.search(p):
                    continue
                if kind == "fn":
                    e2, n = new(e, f"{part}:{k + 1}")
                elif kind == "fnp":
                    e2, n = new(e, p, f"{part}:{k + 1}")
                elif kind in ("rx", "rxf"):
                    e2, n = old.subn(new, e)
                    if e2 == e:
                        n = 0
                else:
                    n = e.count(old)
                    e2 = e.replace(old, new)
                if n:
                    e = e2
                    hit_idx.add(ri)
                    log[(rid, part)][0] += n
                    log[(rid, part)][1] += 1
            el[li] = e
        data[part] = (pl, el, idx, orig, bom)
    # ---- phase 2: whole lines (identical Pāli -> the ref's Hindi body)
    def body(line):
        m = re.match(r"^(#*\s*\*?(?:[\d\-–]+\.\s*)?)(.*?)(\*?\s*(?:\(\d+\)\s*)?(?:\^[\w-]+)?\s*)$", line)
        return m.group(1), m.group(2), m.group(3)

    def pkey(p):
        return re.sub(r"\s+", " ", body(p)[1]).strip()

    wl_hit = set()
    for wi, (rpart, rline, lit) in enumerate(WL):
        rpl, rel, ridx, _, _ = data[rpart]
        key = pkey(rpl[rline - 1])
        canon = lit if lit else body(rel[ridx[rline - 1]])[1]
        for part in PARTS:
            pl, el, idx, _, _ = data[part]
            for k, li in enumerate(idx):
                if pkey(pl[k]) != key or "[" in el[li]:
                    continue
                a, b_, c = body(el[li])
                new = a + canon + c
                if new != el[li]:
                    el[li] = new
                    wl_hit.add(wi)
                    log[("W1-whole-line", part)][0] += 1
                    log[("W1-whole-line", part)][1] += 1
    for wi, w in enumerate(WL):
        if wi not in wl_hit:
            print("WL NO HIT:", w)
    # ---- checks and write
    for part in PARTS:
        pl, el, idx, orig, bom = data[part]
        for k, li in enumerate(idx):
            e, e0 = el[li], orig[li]
            if e != e0:
                if protected(part, k):
                    blocked.append((part, k + 1))
                    el[li] = e0
                    continue
                assert dashes(e) == dashes(e0), (part, k + 1, "dash count changed", e0, e)
                assert re.findall(r"\^[\w-]+\s*$", e) == re.findall(r"\^[\w-]+\s*$", e0), (part, k + 1, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k + 1, "heading")
                assert e.count("[") == e0.count("["), (part, k + 1, "brackets")
                changed_lines[part] += 1
        if not dry:
            out = ("﻿" if bom else "") + "\n".join(el)
            open(os.path.join(HDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(out)
    if not dry:
        with open(os.path.join(HERE, "harmonise-log.tsv"), "w", encoding="utf-8") as f:
            f.write("rule\tfile\treplacements\tlines\n")
            for (rid, part), (n, l) in sorted(log.items(), key=lambda kv: (kv[0][0], PARTS.index(kv[0][1]))):
                f.write(f"{rid}\t{part}\t{n}\t{l}\n")
    tot = collections.defaultdict(lambda: [0, 0])
    for (rid, part), (n, l) in log.items():
        tot[rid][0] += n
        tot[rid][1] += l
    for rid in sorted(tot):
        print(f"{rid:24s} repl={tot[rid][0]:5d} lines={tot[rid][1]:5d}")
    print("lines changed:", sum(changed_lines.values()), "in", len(changed_lines), "files")
    if blocked:
        print("BLOCKED (protected lines a rule would have changed):", blocked[:50], len(blocked))
    for ri, r in enumerate(R):
        if ri not in hit_idx:
            print("NO HIT:", r[0], "|", str(r[2])[:100])


FIXED = {"upādinnattika", "saṃkiliṭṭhattika", "micchattaniyatattika", "ajjhattattika", "saṃkiliṭṭhaduka",
         "kilesasaṃkiliṭṭhaduka"}


def names_table():
    al = collections.defaultdict(list)
    for a, b in list(TIKA_ALIAS.items()) + list(DUKA_ALIAS.items()):
        al[b].append(a)
    print("| Pāli | Hindi |")
    print("|---|---|")
    for d, num in ((TIKA, "तीन"), (DUKA, "दो")):
        for k, x in d.items():
            also = f" (also {', '.join(al[k])})" if k in al else ""
            mark = " (fixed: «परिघटनाओं» added)" if k in FIXED else ""
            print(f"| {k[0].upper() + k[1:]}ṃ{also} | {x.replace('{v}', 'वाला')} वाला {num} का वर्गीकरण{mark} |")


if __name__ == "__main__":
    if "--names-table" in sys.argv:
        names_table()
    else:
        main(dry="--dry" in sys.argv)
