# Segment tables for build_4-01_hi.py (pi-7 4-01-kilesagocchaka, Hindi plain zero-shot).
# Keys are Pāli segments after item normalization: {P:tag}/{N:tag} = the current dyad's two items,
# {K:tag} = the bare noun kilesa ("मन के क्लेश") outside the kilesa dyad (inside it, {P:..} keys fall back
# to the {K:..} entries). Values are Hindi with {Pf} {Pm} {Pms} {Pn} {Pno} / {Nf} ... / {Kn} {Kno} {Ks} {Kso}
# (feminine / masculine pl. or oblique / masc. sg. / noun / noun oblique), {DEP} = the dependence word of
# the line's frame ("पर निर्भर होकर", "के कारण", ...), {KO} = "का"/"को" before assādeti / other verbs.
# Executed by the builder with S = build_sample_hi in scope.
import re

V = S.VARA
H = {
    "(Catuttho bhāgo)": S.BHAGA[4],
    "Dhammānulome dukapaṭṭhānaṃ": f"{S.DHAMMANULOMA}: {S.DUKAPATTHANA}",
    "Kilesagocchakaṃ": "मन के क्लेशों का वर्ग",
    "Piṭṭhidukaṃ": "अंतिम दो-दो के वर्गीकरण",
    "Paṭiccavāro": V["paṭicca"], "Sahajātavāro": V["sahajāta"], "Paccayavāro": V["paccaya"],
    "Nissayavāro": V["nissaya"], "Saṃsaṭṭhavāro": V["saṃsaṭṭha"], "Sampayuttavāro": V["sampayutta"],
    "Pañhāvāro": V["pañhā"], "Vibhaṅgavāro": V["vibhaṅga"], "Saṅkhyāvāro": V["saṅkhyā"],
    "Paṭiccavārādi": "निर्भरता का खंड आदि",
    "Paccayānulomaṃ": S.PACCAYANULOMA, "Paccayapaccanīyaṃ": S.PACCAYAPACCANIYA,
    "Paccayānulomapaccanīyaṃ": S.PACCAYANULOMAPACCANIYA, "Paccayapaccanīyānulomaṃ": S.PACCAYAPACCANIYANULOMA,
    "Paccayānulomādi": S.PACCAYANULOMA + " आदि",
    "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Paccanīyaṃ": S.PACCANIYA,
    "Suddhaṃ": S.SUDDHA,
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए चयन",
    "Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro": "सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "Nissaya-saṃsaṭṭhavāro": "आश्रय और घुले-मिले होने का खंड",
    "Hetudukaṃ": S.DUKANI("hetu"),
    "Nahetudukaṃ": S.DUKANI("hetu", neg=True),
    "Pacchājātāsevanapaccayā": f"{S.NAME('pacchājāta')} और {S.NAME('āsevana')}",
    "Nahetu-naārammaṇapaccayā": f"{S.NNAME('hetu')} और {S.NNAME('ārammaṇa')}",
}
for _k in S.COND_KEYS:
    _p = S.NEG_PREFIX_PALI[_k]
    _cap = _k[0].upper() + _k[1:]
    H[f"{_cap}paccayo"] = S.NAME(_k)
    H[f"{_cap}paccayādi"] = S.NAME(_k) + " आदि"
    H[f"{_p.capitalize()}{_k}paccayo"] = S.NNAME(_k)
    H[f"{_p.capitalize()}{_k}paccayādi"] = S.NNAME(_k) + " आदि"
HEAD = H


def L(*xs):
    xs = [x for x in xs if x]
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " और " + xs[-1]


INS = S.INS
SKH = "जुड़े हुए समूहों के लिए"                  # sampayuttakānaṃ khandhānaṃ
CSRF = "मन से उत्पन्न भौतिक रूपों के लिए"         # cittasamuṭṭhānānaṃ rūpānaṃ
KTRF = "किए गए कर्म से उत्पन्न भौतिक रूपों के लिए"  # kaṭattārūpānaṃ / kaṭattā ca rūpānaṃ
VIPF = "कर्म के फल रूपी समूहों के लिए"            # vipākānaṃ khandhānaṃ
CSR = S.CSR
SAMP = "जुड़े हुए समूह"                           # sampayuttakā (ca) khandhā
SAMPO = "जुड़े हुए समूहों"                         # sampayuttake (ca) khandhe
CETANA_S = "जुड़ा हुआ इरादा"                       # sampayuttakā cetanā
VU_KH = S.KHANDHE_VU                              # vicikicchāsahagate uddhaccasahagate khandhe
VU_MOHA = S.MOHA_VU                               # vicikicchāsahagato uddhaccasahagato moho
V_MOHA = "संशय के साथ होने वाला मोह"
U_MOHA = "बेचैनी के साथ होने वाला मोह"
V_KH = "संशय के साथ होने वाले समूहों"
U_KH = "बेचैनी के साथ होने वाले समूहों"
AV = S.AVAJJANA_FOR                               # āvajjanāya
ASSADA = "उसका रस लेता है, उसमें आनंद लेता है"    # assādeti abhinandati (object taṃ)
ASSADA_PL = "उनका रस लेता है, उनमें आनंद लेता है"  # with a plural object
REV, REVP = S.REVIEW_SG, S.REVIEW_PL

# ---- defilement words ------------------------------------------------------------------
KACC = {"lobhaṃ": "लोभ", "dosaṃ": "द्वेष", "vicikicchaṃ": "संशय", "uddhaccaṃ": "बेचैनी", "mohaṃ": "मोह",
        "diṭṭhiṃ": "दृष्टि", "mānaṃ": "अहंकार", "rāgaṃ": "राग"}
KNOM = {"moho": "मोह", "diṭṭhi": "दृष्टि", "thinaṃ": "आलस्य", "uddhaccaṃ": "बेचैनी", "ahirikaṃ": "निर्लज्जता",
        "anottappaṃ": "बुराई के प्रति निडरता", "māno": "अहंकार", "lobho": "लोभ", "doso": "द्वेष",
        "vicikicchā": "संशय"}
DEPW = {"paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "saṃsaṭṭho": "से घुल-मिलकर",
        "saṃsaṭṭhā": "से घुल-मिलकर", "nissāya": "के आश्रय से", "sampayutto": "से जुड़कर",
        "sampayuttā": "से जुड़कर", "sahajāto": "के साथ जन्म लेकर", "sahajātā": "के साथ जन्म लेकर"}
K6 = L("मोह", "दृष्टि", "आलस्य", "बेचैनी", "निर्लज्जता", "बुराई के प्रति निडरता")   # moho … anottappaṃ
K6L = ["मोह", "दृष्टि", "आलस्य", "बेचैनी", "निर्लज्जता", "बुराई के प्रति निडरता"]


def kseq(key):
    """'(arūpe) lobhaṃ paṭicca moho diṭṭhi … anottappaṃ' -> Hindi list (or None)."""
    w = key.split()
    pre = ""
    if w and w[0] == "arūpe":
        pre, w = "अभौतिक लोक में ", w[1:]
    if len(w) < 3 or w[0] not in KACC or w[1] not in DEPW:
        return None
    items = []
    for t in w[2:]:
        if t.startswith("⟦"):
            items[-1] += " " + t
        elif t in KNOM:
            items.append(KNOM[t])
        else:
            return None
    return f"{pre}{KACC[w[0]]} {DEPW[w[1]]} {L(*items)}"


PREFIX = [("ahetukapaṭisandhikkhaṇe ", S.AHETUKA_PATISANDHI + " "), ("paṭisandhikkhaṇe ", S.PATISANDHI + " "),
          ("arūpe ", S.ARUPE + " "), ("ahetukaṃ {", S.AHETUKA + ", {"), ("ahetukaṃ ", S.AHETUKA + " ")]


# ---- rule-generated pañhāvāra sentences --------------------------------------------------
IT = r"\{[PNK]:[^}]*\}"
SUBJ = [  # (regex, Hindi, gender/number: "pl" / "m" / "f")
    (r"purimā purimā (\{[PN]):ā\} khandhā ca \{T:nom\} ca", r"पहले-पहले के \1m} समूह और {T}", "pl"),
    (r"purimā purimā (\{[PN]):ā\} khandhā", r"पहले-पहले के \1m} समूह", "pl"),
    (r"purimā purimā \{T:nom\}", "पहले-पहले का {T}", "m"),
    (r"purimo purimo \{T:nom\}", "पहले-पहले का {T}", "m"),
    (r"(\{[PN]):ā\} hetū", r"\1m} मूल", "pl"),
    (r"(\{[PN]):ā\} khandhā ca \{T:nom\} ca", r"\1m} समूह और {T}", "pl"),
    (r"(\{[PN]):ā\} khandhā ca vatthu ca", r"\1m} समूह और आधार", "pl"),
    (r"(\{[PN]):ā\} khandhā ca mahābhūtā ca", r"\1m} समूह और महाभूत", "pl"),
    (r"(\{[PN]):ā\} khandhā", r"\1m} समूह", "pl"),
    (r"(\{[PN]):o\} eko khandho ca \{T:nom\} ca", r"\1ms} एक समूह और {T}", "pl"),
    (r"(\{[PN]):o\} eko khandho ca vatthu ca", r"\1ms} एक समूह और आधार", "pl"),
    (r"(\{[PN]):ādhipati\}", r"\1f} प्रधानता", "f"),
    (r"(\{[PN]):ā\} cetanā", r"\1ms} इरादा", "m"),
    (r"\{T:nom\}", "{T}", "m"),
    (r"vatthu", "आधार", "m"),
    (r"āvajjanā", "मन को विषय की ओर मोड़ना", "m"),
]
DAT = [  # (regex, Hindi oblique noun phrase)
    (r"pacchimānaṃ pacchimānaṃ (\{[PN]):ānaṃ\} khandhānaṃ", r"बाद-बाद के \1m} समूहों"),
    (r"pacchimānaṃ pacchimānaṃ (\{K):ānaṃ\}", r"बाद-बाद के \1no}"),
    (r"pacchim\w+ pacchim\w+ \{T:dat\}", "बाद-बाद के {T}"),
    (r"sampayuttakānañca khandhānaṃ|sampayuttakānaṃ khandhānaṃ", "जुड़े हुए समूहों"),
    (r"sampayuttakānaṃ (\{K):ānaṃ\}", r"जुड़े हुए \1no}"),
    (r"cittasamuṭṭhānānañca rūpānaṃ|cittasamuṭṭhānānaṃ rūpānaṃ", "मन से उत्पन्न भौतिक रूपों"),
    (r"kaṭattā ca rūpānaṃ|kaṭattārūpānaṃ", "किए गए कर्म से उत्पन्न भौतिक रूपों"),
    (r"vipākānaṃ (\{[PN]):ānaṃ\} khandhānaṃ", r"कर्म के फल रूपी, \1m} समूहों"),
    (r"vipākānaṃ khandhānaṃ", "कर्म के फल रूपी समूहों"),
    (r"(\{[PN]):ānaṃ\} khandhānaṃ", r"\1m} समूहों"),
    (r"(\{K):ānaṃ\}(?: ca)?", r"\1no}"),
    (r"\{T:dat\}(?: ca)?", "{T}"),
    (r"mohassa(?: ca)?", "मोह"),
    (r"tiṇṇannaṃ khandhānaṃ", "तीन समूहों"),
    (r"(\{[PN]):assa\} vuṭṭhānassa", r"\1m} बाहर आने"),
    (r"vuṭṭhānassa", "बाहर आने"),
]
VERB3 = {"pl": "होते हैं", "m": "होता है", "f": "होती है"}


def gen_panha(key):
    m = re.match(r"^(.*) (\w+)paccayena paccayo$", key)
    if not m or m.group(2) not in S.COND_KEYS:
        return None
    body, k = m.group(1), m.group(2)
    for rx, hs, g in SUBJ:
        ms = re.match("^" + rx + " ", body)
        if not ms:
            continue
        subj = ms.expand(hs)
        rest = body[ms.end():]
        dats = []
        while rest:
            for rd, hd in DAT:
                md = re.match("^(?:" + rd + r")(?: |$)", rest)
                if md:
                    dats.append(md.expand(hd))
                    rest = rest[md.end():]
                    break
            else:
                return None
        if not dats:
            return None
        return f"{subj} {L(*[d + ' के लिए' for d in dats])} {S.INS(k)} {VERB3[g]}"
    return None


OBJ_R = [
    (r"vatthuṃ (\{[PN]):e\} khandhe ca \{T:acc\} ca", r"आधार, \1m} समूहों और {T}"),
    (r"(\{[PN]):e\} khandhe ca \{T:acc\} ca", r"\1m} समूहों और {T}"),
    (r"vatthuṃ (\{[PN]):e\} khandhe ca mohañca", r"आधार, \1m} समूहों और मोह"),
    (r"(\{[PN]):e\} khandhe", r"\1m} समूहों"),
    (r"vicikicchāsahagate khandhe ca mohañca", f"{V_KH} और मोह"),
    (r"uddhaccasahagate khandhe ca mohañca", f"{U_KH} और मोह"),
    (r"\{T:acc\}", "{T}"),
    (r"taṃ", "उस"),
]
RES_R = [
    (r"(\{[PN]):ā\} khandhā ca \{T:nom\} ca uppajjanti", r"\1m} समूह और {T} उत्पन्न होते हैं"),
    (r"(\{[PN]):ā\} khandhā ca moho ca uppajjanti", r"\1m} समूह और मोह उत्पन्न होते हैं"),
    (r"(\{[PN]):ā\} khandhā uppajjanti", r"\1m} समूह उत्पन्न होते हैं"),
    (r"\{T:nom\} ca sampayuttakā ca khandhā uppajjanti", f"{{T}} और {SAMP} उत्पन्न होते हैं"),
    (r"\{T:nom\} ca sampayuttakā khandhā ca uppajjanti", f"{{T}} और {SAMP} उत्पन्न होते हैं"),
    (r"\{T:nom\} uppajjati", "{T} उत्पन्न होता है"),
]


def gen_arabbha(key):
    m = re.match(r"^(.*?) (ārabbha|garuṃ katvā) (.*)$", key)
    if not m:
        return None
    o = next((re.fullmatch(rx, m.group(1)) and re.fullmatch(rx, m.group(1)).expand(h) for rx, h in OBJ_R
              if re.fullmatch(rx, m.group(1))), None)
    r = next((re.fullmatch(rx, m.group(3)).expand(h) for rx, h in RES_R if re.fullmatch(rx, m.group(3))), None)
    if o is None or r is None:
        return None
    if o == "उस":
        o = "उसे"
    else:
        o += " को"
    v = "विषय बनाकर" if m.group(2) == "ārabbha" else "महत्व देकर"
    return f"{o} {v} {r}"


def GEN(key, dkey):
    h = kseq(key)
    if h is not None:
        return h
    h = gen_panha(key) or gen_arabbha(key)
    if h is not None:
        return h
    for p, hp in PREFIX:
        if key.startswith(p) and len(key) > len(p):
            rest = key[len(p) - 1:] if p.endswith("{") else key[len(p):]
            r = G.get(rest) or GEN(rest, dkey)
            if r is not None:
                return hp[:-1] + r if p.endswith("{") else hp + r
    # the same sentence in another dependent section: look up the paṭicca form and swap the word
    for p, hh in DEPW.items():
        if p == "paṭicca" or not re.search(r"\b" + p + r"\b", key):
            continue
        k2 = re.sub(r"\b" + p + r"\b", "paṭicca", key)
        if k2 in G:
            return G[k2].replace("पर निर्भर होकर", hh)
    return None


PAREN = {
    "cakkaṃ": "बारी-बारी से",
    "cakkaṃ, saṃkhittaṃ": "बारी-बारी से, संक्षिप्त",
    "saṃkhittaṃ": "संक्षिप्त",
    "yāva asaññasattā": "पहचान-रहित प्राणियों तक",
    "yāva ajjhattikā mahābhūtā": "आंतरिक महाभूतों तक",
    "arūpe dosamūlakaṃ natthi": "अभौतिक लोक में द्वेष से शुरू होने वाली शृंखला नहीं है",
    "evaṃ navapi pañhā kātabbā": "इसी तरह नौ के नौ प्रश्न तैयार करने चाहिए",
    "evaṃ sabbe paccayā kātabbā.": "इसी तरह सभी कारणों के साथ करना चाहिए।",
    "evaṃ itare dve gaṇanāpi sahajātavāropi kātabbo.":
        "इसी तरह अन्य दो गणनाएँ भी और सह-उत्पत्ति का खंड भी तैयार करना चाहिए।",
    "evaṃ itare dve gaṇanāpi nissayavāropi kātabbo.":
        "इसी तरह अन्य दो गणनाएँ भी और आश्रय का खंड भी तैयार करना चाहिए।",
    "evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo.":
        "इसी तरह अन्य दो गणनाएँ भी और जुड़ाव का खंड भी तैयार करना चाहिए।",
    "paṭiccasadisā": "निर्भरता के खंड के समान",
    "paṭiccasadisaṃ": "निर्भरता के खंड के समान",
    "paṭiccavārasadisaṃ": "निर्भरता के खंड के समान",
    "ārammaṇapaccaye {N:amūle} pañca viññāṇā kātabbā.":
        "विषय-कारण में {Nm} पद से शुरू होने वाली शृंखला में पाँच प्रकार की चेतना को शामिल करना चाहिए।",
    "cakkaṃ. Evaṃ nava pañhā kātabbā.": "बारी-बारी से। इसी तरह नौ प्रश्न तैयार करने चाहिए।",
    "evaṃ nahetupañhā cattāri kātabbā.": "इसी तरह मूल-कारण के अभाव वाले चार प्रश्न तैयार करने चाहिए।",
    "mūlaṃ pucchitabbaṃ.": "मूल वाक्य पूछना चाहिए।",
    "mūlaṃ kātabbaṃ.": "मूल वाक्य बनाना चाहिए।",
    "ārammaṇādhipatiyeva": "केवल विषय रूपी प्रधानता",
    "saṃkhittaṃ. Vitthāretabbaṃ.": "संक्षिप्त। विस्तार करना चाहिए।",
    "saṃkhittaṃ. Sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ.":
        "संक्षिप्त। सह-उत्पत्ति रूपी भाग सह-उत्पत्ति-कारण के समान है, पूर्व-उत्पत्ति रूपी भाग पूर्व-उत्पत्ति-कारण के समान है।",
    "sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ.":
        "सह-उत्पत्ति रूपी भाग सह-उत्पत्ति-कारण के समान है, पूर्व-उत्पत्ति रूपी भाग पूर्व-उत्पत्ति-कारण के समान है।",
    "anulomamātikā kātabbā": "सकारात्मक क्रम की मूल सूची बनानी चाहिए",
    "anulomamātikā": "सकारात्मक क्रम की मूल सूची",
    "anulomamātikā gahetabbā": "सकारात्मक क्रम की मूल सूची लेनी चाहिए",
    "yathā lokiyadukaṃ, evaṃ ninnānākaraṇaṃ.":
        "जैसे लौकिक वाला दो का वर्गीकरण है, वैसे ही, बिना किसी भिन्नता के।",
}
for _w, _n in S.NUM.items():
    PAREN[f"sabbattha {_w}"] = f"हर जगह {_n}"

G = {
    # ---------------- kilesa dyad: paṭicca / paccaya / saṃsaṭṭha sections
    "{K:aṃ} paṭicca sampayuttakā khandhā cittasamuṭṭhānañca rūpaṃ": f"{{Kso}} पर निर्भर होकर {SAMP} और {CSR}",
    "lobhaṃ paṭicca moho diṭṭhi thinaṃ uddhaccaṃ ahirikaṃ anottappaṃ sampayuttakā ca khandhā cittasamuṭṭhānañca rūpaṃ":
        "लोभ पर निर्भर होकर " + L(*K6L, SAMP, CSR),
    "lobhaṃ paṭicca moho diṭṭhi thinaṃ uddhaccaṃ ahirikaṃ anottappaṃ sampayuttakā ca khandhā":
        "लोभ पर निर्भर होकर " + L(*K6L, SAMP),
    "{N:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"{{Nm}} एक समूह पर निर्भर होकर तीन समूह और {CSR}",
    "{P:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"{{Pm}} एक समूह पर निर्भर होकर तीन समूह और {CSR}",
    "{N:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā": "{Nm} एक समूह पर निर्भर होकर तीन समूह",
    "{P:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā": "{Pm} एक समूह पर निर्भर होकर तीन समूह",
    "ahetukaṃ {N:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"{S.AHETUKA}, {{Nm}} एक समूह पर निर्भर होकर तीन समूह और {CSR}",
    "ahetukaṃ {N:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā": f"{S.AHETUKA}, {{Nm}} एक समूह पर निर्भर होकर तीन समूह",
    "ahetukaṃ {N:aṃ}": f"{S.AHETUKA}, {{Nm}} एक समूह {{DEP}}",
    "dve khandhe": "दो समूहों {DEP}",
    "dve khandhe ca": "दो समूहों और",
    "paṭisandhikkhaṇe": S.PATISANDHI,
    "ahetukapaṭisandhikkhaṇe": S.AHETUKA_PATISANDHI,
    "khandhe paṭicca vatthu": "समूहों पर निर्भर होकर आधार",
    "vatthuṃ paṭicca khandhā": "आधार पर निर्भर होकर समूह",
    "ekaṃ mahābhūtaṃ": "एक महाभूत {DEP}",
    "{N:e} khandhe paṭicca {K:ā}": "{Nm} समूहों पर निर्भर होकर {Kn}",
    "{N:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā {K:ā} ca cittasamuṭṭhānañca rūpaṃ":
        f"{{Nm}} एक समूह पर निर्भर होकर तीन समूह, {{Kn}} और {CSR}",
    "{N:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā {K:ā} ca": "{Nm} एक समूह पर निर्भर होकर तीन समूह और {Kn}",
    "lobhañca sampayuttake ca khandhe paṭicca moho diṭṭhi thinaṃ uddhaccaṃ ahirikaṃ anottappaṃ":
        f"लोभ और {SAMPO} पर निर्भर होकर {K6}",
    "{N:aṃ} ekaṃ khandhañca {K:e} ca paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"{{Nm}} एक समूह और {{Kno}} पर निर्भर होकर तीन समूह और {CSR}",
    "{N:aṃ} ekaṃ khandhañca {K:e} ca paṭicca tayo khandhā": "{Nm} एक समूह और {Kno} पर निर्भर होकर तीन समूह",
    "{K:e} ca mahābhūte ca paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{{Kno}} और महाभूतों पर निर्भर होकर {CSR}",
    "{N:aṃ} ekaṃ khandhañca lobhañca paṭicca tayo khandhā moho diṭṭhi thinaṃ uddhaccaṃ ahirikaṃ anottappaṃ cittasamuṭṭhānañca rūpaṃ":
        "{Nm} एक समूह और लोभ पर निर्भर होकर " + L("तीन समूह", *K6L, CSR),
    "{N:aṃ} ekaṃ khandhañca lobhañca paṭicca tayo khandhā moho diṭṭhi thinaṃ uddhaccaṃ ahirikaṃ anottappaṃ":
        "{Nm} एक समूह और लोभ पर निर्भर होकर " + L("तीन समूह", *K6L),
    "vicikicchaṃ paṭicca moho": "संशय पर निर्भर होकर मोह",
    "uddhaccaṃ paṭicca moho": "बेचैनी पर निर्भर होकर मोह",
    "vicikicchaṃ paṭicca vicikicchāsahagato moho": f"संशय पर निर्भर होकर {V_MOHA}",
    "uddhaccaṃ paṭicca uddhaccasahagato moho": f"बेचैनी पर निर्भर होकर {U_MOHA}",
    "vicikicchāsahagate uddhaccasahagate khandhe paṭicca vicikicchāsahagato uddhaccasahagato moho":
        f"{VU_KH} पर निर्भर होकर {VU_MOHA}",
    "vicikicchāsahagate khandhe ca vicikicchañca paṭicca vicikicchāsahagato moho":
        f"{V_KH} और संशय पर निर्भर होकर {V_MOHA}",
    "uddhaccasahagate khandhe ca uddhaccañca paṭicca uddhaccasahagato moho":
        f"{U_KH} और बेचैनी पर निर्भर होकर {U_MOHA}",
    "vicikicchāsahagate khandhe paṭicca vicikicchāsahagato moho": f"{V_KH} पर निर्भर होकर {V_MOHA}",
    "uddhaccasahagate khandhe paṭicca uddhaccasahagato moho": f"{U_KH} पर निर्भर होकर {U_MOHA}",
    "vicikicchāsahagate uddhaccasahagate khandhe ca vicikicchañca uddhaccañca paṭicca vicikicchāsahagato uddhaccasahagato moho":
        f"{VU_KH}, संशय और बेचैनी पर निर्भर होकर {VU_MOHA}",
    "{K:e} paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{{Kno}} पर निर्भर होकर {CSR}",
    "{K:e} paṭicca sampayuttakā khandhā": f"{{Kno}} पर निर्भर होकर {SAMP}",
    "{K:e} paṭicca sampayuttakā khandhā cittasamuṭṭhānañca rūpaṃ": f"{{Kno}} पर निर्भर होकर {SAMP} और {CSR}",
    "{N:e} khandhe paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{{Nm}} समूहों पर निर्भर होकर {CSR}",
    "{P:e} khandhe paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{{Pm}} समूहों पर निर्भर होकर {CSR}",
    "{P:e} khandhe ca mahābhūte ca paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{{Pm}} समूहों और महाभूतों पर निर्भर होकर {CSR}",
    "{K:e} ca sampayuttake ca khandhe paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{{Kno}} और {SAMPO} पर निर्भर होकर {CSR}",
    "arūpe {K:e} paṭicca sampayuttakā khandhā": f"{S.ARUPE} {{Kno}} पर निर्भर होकर {SAMP}",
    "{K:e} paṭicca sampayuttakā cetanā": f"{{Kno}} पर निर्भर होकर {CETANA_S}",
    "{N:e} khandhe paṭicca sampayuttakā cetanā": f"{{Nm}} समूहों पर निर्भर होकर {CETANA_S}",
    "{K:e} ca sampayuttake ca khandhe paṭicca sampayuttakā cetanā": f"{{Kno}} और {SAMPO} पर निर्भर होकर {CETANA_S}",
    "bāhiraṃ": S.BAHIRA, "āhārasamuṭṭhānaṃ": S.AHARASAM, "utusamuṭṭhānaṃ": S.UTUSAM,
    "vatthuṃ paccayā {N:ā} khandhā": "आधार के कारण {Nm} समूह",
    "vatthuṃ paccayā {P:ā} khandhā": "आधार के कारण {Pm} समूह",
    "vatthuṃ paccayā {K:ā}": "आधार के कारण {Kn}",
    "mahābhūte paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"महाभूतों पर निर्भर होकर {CSR}",
    "vatthuṃ paccayā {K:ā} ca sampayuttakā ca khandhā": f"आधार के कारण {{Kn}} और {SAMP}",
    "lobhañca vatthuñca paccayā {K:ā}": "लोभ और आधार के कारण {Kn}",
    "{N:aṃ} ekaṃ khandhañca {K:aṃ} ca paccayā tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"{{Nm}} एक समूह और {{Kso}} के कारण तीन समूह और {CSR}",
    "{K:e} ca vatthuñca paccayā {N:ā} khandhā": "{Kno} और आधार के कारण {Nm} समूह",
    "lobhañca vatthuñca paccayā moho diṭṭhi thinaṃ uddhaccaṃ ahirikaṃ anottappaṃ sampayuttakā ca khandhā":
        "लोभ और आधार के कारण " + L(*K6L, SAMP),
    "cakkhāyatanaṃ paccayā cakkhuviññāṇaṃ": "आँख के इंद्रिय-क्षेत्र के कारण आँख की चेतना",
    "kāyāyatanaṃ": "शरीर का इंद्रिय-क्षेत्र",
    "kāyāyatanaṃ paccayā kāyaviññāṇaṃ": "शरीर के इंद्रिय-क्षेत्र के कारण शरीर की चेतना",
    "vatthuṃ paccayā ahetukā {N:ā} khandhā": f"आधार के कारण {S.AHETUKA}, {{Nm}} समूह",
    "vicikicchāsahagate uddhaccasahagate khandhe ca vatthuñca paccayā vicikicchāsahagato uddhaccasahagato moho":
        f"{VU_KH} और आधार के कारण {VU_MOHA}",
    "vicikicchañca sampayuttake ca khandhe vatthuñca paccayā vicikicchāsahagato moho":
        f"संशय, {SAMPO} और आधार के कारण {V_MOHA}",
    "uddhaccañca sampayuttake ca khandhe vatthuñca paccayā uddhaccasahagato moho":
        f"बेचैनी, {SAMPO} और आधार के कारण {U_MOHA}",
    "vatthuṃ paccayā vicikicchāsahagato uddhaccasahagato moho": f"आधार के कारण {VU_MOHA}",
    "anulomaṃ": S.ANULOMA,
    "paccanīyaṃ": S.PACCANIYA,
    # ---------------- pañhāvāra
    "{P:ā} hetū sampayuttakānaṃ {P:ānaṃ} hetupaccayena paccayo":
        f"{{Pm}} मूल जुड़े हुए {{Kno}} के लिए {INS('hetu')} होते हैं",
    "{P:ā} hetū sampayuttakānaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ hetupaccayena paccayo":
        f"{{Pm}} मूल {SKH} और {CSRF} {INS('hetu')} होते हैं",
    "{N:ā} hetū sampayuttakānaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ hetupaccayena paccayo":
        f"{{Nm}} मूल {SKH} और {CSRF} {INS('hetu')} होते हैं",
    "{P:ā} hetū sampayuttakānaṃ khandhānaṃ {P:ānaṃ} cittasamuṭṭhānānañca rūpānaṃ hetupaccayena paccayo":
        f"{{Pm}} मूल {SKH}, {{Kno}} के लिए और {CSRF} {INS('hetu')} होते हैं",
    "{P:ā} hetū sampayuttakānaṃ khandhānaṃ hetupaccayena paccayo": f"{{Pm}} मूल {SKH} {INS('hetu')} होते हैं",
    "{P:ā} hetū cittasamuṭṭhānānaṃ rūpānaṃ hetupaccayena paccayo": f"{{Pm}} मूल {CSRF} {INS('hetu')} होते हैं",
    "{K:e} ārabbha {K:ā} uppajjanti": "{Kno} को विषय बनाकर {Kn} उत्पन्न होते हैं",
    "{K:e} ārabbha {N:ā} khandhā uppajjanti": "{Kno} को विषय बनाकर {Nm} समूह उत्पन्न होते हैं",
    "{K:e} ārabbha {K:ā} ca sampayuttakā ca khandhā uppajjanti": f"{{Kno}} को विषय बनाकर {{Kn}} और {SAMP} उत्पन्न होते हैं",
    "dānaṃ": "दान", "sīlaṃ": "सदाचार", "uposathakammaṃ": "उपवास-व्रत",
    "pubbe suciṇṇāni": "पहले भली-भाँति किए गए कार्य",
    "pubbe": "पहले", "jhānā": "ध्यान से", "jhānaṃ": "ध्यान",
    "jhānā vuṭṭhahitvā": "ध्यान से उठकर",
    "jhānā vuṭṭhahitvā jhānaṃ paccavekkhati assādeti abhinandati":
        f"ध्यान से उठकर ध्यान पर {REV}, {ASSADA}",
    "jhānā vuṭṭhahitvā jhānaṃ assādeti abhinandati": "ध्यान से उठकर ध्यान का रस लेता है, उसमें आनंद लेता है",
    "jhānā vuṭṭhahitvā jhānaṃ paccavekkhati": f"ध्यान से उठकर ध्यान पर {REV}",
    "taṃ ārabbha rāgo": "उसे विषय बनाकर राग",
    "taṃ ārabbha rāgo uppajjati": "उसे विषय बनाकर राग उत्पन्न होता है",
    "diṭṭhi": "दृष्टि", "vicikicchā": "संशय", "uddhaccaṃ": "बेचैनी", "uddhacca": "बेचैनी",
    "domanassaṃ uppajjati": "उदासी उत्पन्न होती है",
    "uddhaccaṃ uppajjati": "बेचैनी उत्पन्न होती है",
    "diṭṭhi uppajjati": "दृष्टि उत्पन्न होती है",
    "jhāne parihīne vippaṭisārissa domanassaṃ uppajjati": "ध्यान के छूट जाने पर ग्लानि से भरे व्यक्ति में उदासी उत्पन्न होती है",
    "ariyā maggā vuṭṭhahitvā…pe… phalassa, āvajjanāya ārammaṇapaccayena paccayo":
        f"आर्य मार्ग से उठकर… फल के लिए, {AV} {INS('ārammaṇa')} होता है",
    "ariyā maggā vuṭṭhahitvā": "आर्य मार्ग से उठकर",
    "cakkhuṃ": "आँख {KO}",
    "cakkhuṃ…pe… vatthuṃ {N:e} khandhe aniccato…pe… domanassaṃ uppajjati":
        "आँख को… आधार को, {Nm} समूहों को अनित्य… उदासी उत्पन्न होती है",
    "dibbena cakkhunā rūpaṃ passati, dibbāya sotadhātuyā saddaṃ suṇāti…pe… anāgataṃsañāṇassa, āvajjanāya ārammaṇapaccayena paccayo":
        f"दिव्य आँख से दृश्य रूप देखता है, दिव्य कान के तत्व से ध्वनि सुनता है… {S.ANAGATAMSA_OBL} के लिए, {AV} {INS('ārammaṇa')} होते हैं",
    "dibbena cakkhunā rūpaṃ passati": "दिव्य आँख से दृश्य रूप देखता है",
    "dibbāya sotadhātuyā saddaṃ suṇāti": "दिव्य कान के तत्व से ध्वनि सुनता है",
    "vatthuṃ {N:e} khandhe assādeti abhinandati": f"आधार का, {{Nm}} समूहों का रस लेता है, उनमें आनंद लेता है",
    "vatthuṃ {P:e} khandhe assādeti abhinandati": f"आधार का, {{Pm}} समूहों का रस लेता है, उनमें आनंद लेता है",
    "taṃ ārabbha {K:ā} ca sampayuttakā ca khandhā uppajjanti": f"उसे विषय बनाकर {{Kn}} और {SAMP} उत्पन्न होते हैं",
    "ārammaṇādhipati": S.ARAMMANADHIPATI, "sahajātādhipati": S.SAHAJATADHIPATI,
    "{K:e} garuṃ katvā {K:ā} uppajjanti": "{Kno} को महत्व देकर {Kn} उत्पन्न होते हैं",
    "uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati assādeti abhinandati":
        f"उपवास-व्रत का पालन करके, उसे महत्व देकर उस पर {REV}, {ASSADA}",
    "taṃ garuṃ katvā rāgo uppajjati": "उसे महत्व देकर राग उत्पन्न होता है",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā paccavekkhanti": f"आर्य मार्ग से उठकर मार्ग को महत्व देकर उस पर {REVP}",
    "phalassa adhipatipaccayena paccayo": f"फल के लिए {INS('adhipati')} होता है",
    "vatthuṃ {N:e} khandhe garuṃ katvā assādeti abhinandati": f"आधार को, {{Nm}} समूहों को महत्व देकर {ASSADA_PL}",
    "vatthuṃ {P:e} khandhe garuṃ katvā assādeti abhinandati": f"आधार को, {{Pm}} समूहों को महत्व देकर {ASSADA_PL}",
    "{N:ādhipati} sampayuttakānaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ adhipatipaccayena paccayo":
        f"{{Nf}} प्रधानता {SKH} और {CSRF} {INS('adhipati')} होती है",
    "{P:ādhipati} sampayuttakānaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ adhipatipaccayena paccayo":
        f"{{Pf}} प्रधानता {SKH} और {CSRF} {INS('adhipati')} होती है",
    "{P:ādhipati} sampayuttakānaṃ khandhānaṃ adhipatipaccayena paccayo": f"{{Pf}} प्रधानता {SKH} {INS('adhipati')} होती है",
    "{P:ādhipati} cittasamuṭṭhānānaṃ rūpānaṃ adhipatipaccayena paccayo": f"{{Pf}} प्रधानता {CSRF} {INS('adhipati')} होती है",
    "{N:ādhipati} sampayuttakānaṃ {K:ānaṃ} adhipatipaccayena paccayo":
        f"{{Nf}} प्रधानता जुड़े हुए {{Kno}} के लिए {INS('adhipati')} होती है",
    "taṃ garuṃ katvā {K:ā} ca sampayuttakā ca khandhā uppajjanti": f"उसे महत्व देकर {{Kn}} और {SAMP} उत्पन्न होते हैं",
    "{N:ādhipati} sampayuttakānaṃ khandhānaṃ {K:ānaṃ} ca cittasamuṭṭhānānañca rūpānaṃ adhipatipaccayena paccayo":
        f"{{Nf}} प्रधानता {SKH}, {{Kno}} के लिए और {CSRF} {INS('adhipati')} होती है",
    "purimā purimā {K:ā} pacchimānaṃ pacchimānaṃ {K:ānaṃ} anantarapaccayena paccayo":
        f"पहले-पहले के {{Kn}} बाद-बाद के {{Kno}} के लिए {INS('anantara')} होते हैं",
    "purimā purimā {K:ā} pacchimānaṃ pacchimānaṃ {N:ānaṃ} khandhānaṃ anantarapaccayena paccayo":
        f"पहले-पहले के {{Kn}} बाद-बाद के {{Nm}} समूहों के लिए {INS('anantara')} होते हैं",
    "{K:ā} vuṭṭhānassa anantarapaccayena paccayo": f"{{Kn}} बाहर आने के लिए {INS('anantara')} होते हैं",
    "purimā purimā {K:ā} pacchimānaṃ pacchimānaṃ {K:ānaṃ} sampayuttakānañca khandhānaṃ anantarapaccayena paccayo":
        f"पहले-पहले के {{Kn}} बाद-बाद के {{Kno}} के लिए और {SKH} {INS('anantara')} होते हैं",
    "purimā purimā {N:ā} khandhā pacchimānaṃ pacchimānaṃ {N:ānaṃ} khandhānaṃ anantarapaccayena paccayo":
        f"पहले-पहले के {{Nm}} समूह बाद-बाद के {{Nm}} समूहों के लिए {INS('anantara')} होते हैं",
    "purimā purimā {P:ā} khandhā pacchimānaṃ pacchimānaṃ {P:ānaṃ} khandhānaṃ anantarapaccayena paccayo":
        f"पहले-पहले के {{Pm}} समूह बाद-बाद के {{Pm}} समूहों के लिए {INS('anantara')} होते हैं",
    "purimā purimā {N:ā} khandhā pacchimānaṃ pacchimānaṃ {N:ānaṃ} khandhānaṃ":
        "पहले-पहले के {Nm} समूह बाद-बाद के {Nm} समूहों के लिए",
    "phalasamāpattiyā anantarapaccayena paccayo": f"फल की ध्यान-अवस्था के लिए {INS('anantara')} होते हैं",
    "purimā purimā {N:ā} khandhā pacchimānaṃ pacchimānaṃ {K:ānaṃ} anantarapaccayena paccayo":
        f"पहले-पहले के {{Nm}} समूह बाद-बाद के {{Kno}} के लिए {INS('anantara')} होते हैं",
    "āvajjanā {K:ānaṃ} anantarapaccayena paccayo": f"मन को विषय की ओर मोड़ना {{Kno}} के लिए {INS('anantara')} होता है",
    "purimā purimā {N:ā} khandhā pacchimānaṃ pacchimānaṃ {K:ānaṃ} sampayuttakānañca khandhānaṃ anantarapaccayena paccayo":
        f"पहले-पहले के {{Nm}} समूह बाद-बाद के {{Kno}} के लिए और {SKH} {INS('anantara')} होते हैं",
    "āvajjanā {K:ānaṃ} sampayuttakānañca khandhānaṃ anantarapaccayena paccayo":
        f"मन को विषय की ओर मोड़ना {{Kno}} के लिए और {SKH} {INS('anantara')} होता है",
    "purimā purimā {K:ā} ca sampayuttakā ca khandhā pacchimānaṃ pacchimānaṃ {K:ānaṃ} anantarapaccayena paccayo":
        f"पहले-पहले के {{Kn}} और {SAMP} बाद-बाद के {{Kno}} के लिए {INS('anantara')} होते हैं",
    "purimā purimā {K:ā} ca sampayuttakā ca khandhā pacchimānaṃ pacchimānaṃ {N:ānaṃ} khandhānaṃ anantarapaccayena paccayo":
        f"पहले-पहले के {{Kn}} और {SAMP} बाद-बाद के {{Nm}} समूहों के लिए {INS('anantara')} होते हैं",
    "{K:ā} ca sampayuttakā ca khandhā vuṭṭhānassa anantarapaccayena paccayo":
        f"{{Kn}} और {SAMP} बाहर आने के लिए {INS('anantara')} होते हैं",
    "purimā purimā {K:ā} ca sampayuttakā ca khandhā pacchimānaṃ pacchimānaṃ {K:ānaṃ} sampayuttakānañca khandhānaṃ anantarapaccayena paccayo":
        f"पहले-पहले के {{Kn}} और {SAMP} बाद-बाद के {{Kno}} के लिए और {SKH} {INS('anantara')} होते हैं",
    "ārammaṇūpanissayo": S.ARAMMANUPANISSAYA, "anantarūpanissayo": S.ANANTARUPANISSAYA,
    "pakatūpanissayo": S.PAKATUPANISSAYA,
    "{K:ā} {K:ānaṃ} upanissayapaccayena paccayo": f"{{Kn}} {{Kno}} के लिए {INS('upanissaya')} होते हैं",
    "saddhaṃ upanissāya dānaṃ deti": "श्रद्धा के प्रबल आश्रय से दान देता है",
    "mānaṃ jappeti": "अहंकार पालता है", "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "paññaṃ": "प्रज्ञा", "rāgaṃ": "राग", "dosaṃ": "द्वेष", "mohaṃ": "मोह", "mānaṃ": "अहंकार",
    "diṭṭhiṃ": "दृष्टि", "patthanaṃ": "कामना", "kāyikaṃ sukhaṃ": "शारीरिक सुख", "kāyikaṃ dukkhaṃ": "शारीरिक दुःख",
    "utuṃ": "तापमान", "bhojanaṃ": "भोजन",
    "senāsanaṃ upanissāya dānaṃ deti": "निवास-स्थान के प्रबल आश्रय से दान देता है",
    "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "saddhā": "श्रद्धा",
    "senāsanaṃ saddhāya": "निवास-स्थान श्रद्धा के लिए",
    "phalasamāpattiyā upanissayapaccayena paccayo": f"फल की ध्यान-अवस्था के लिए {INS('upanissaya')} होते हैं",
    "saddhaṃ upanissāya mānaṃ jappeti": "श्रद्धा के प्रबल आश्रय से अहंकार पालता है",
    "senāsanaṃ upanissāya pāṇaṃ hanati": "निवास-स्थान के प्रबल आश्रय से प्राणी की हत्या करता है",
    "senāsanaṃ {K:ānaṃ} upanissayapaccayena paccayo": f"निवास-स्थान {{Kno}} के लिए {INS('upanissaya')} होते हैं",
    "senāsanaṃ {K:ānaṃ} sampayuttakānañca khandhānaṃ upanissayapaccayena paccayo":
        f"निवास-स्थान {{Kno}} के लिए और {SKH} {INS('upanissaya')} होते हैं",
    "ārammaṇapurejātaṃ": S.ARAMMANAPUREJATA, "vatthupurejātaṃ": S.VATTHUPUREJATA,
    "cakkhuṃ…pe… vatthuṃ aniccato…pe… domanassaṃ uppajjati, dibbena cakkhunā rūpaṃ passati, dibbāya sotadhātuyā saddaṃ suṇāti":
        "आँख को… आधार को अनित्य… उदासी उत्पन्न होती है, दिव्य आँख से दृश्य रूप देखता है, दिव्य कान के तत्व से ध्वनि सुनता है",
    "rūpāyatanaṃ cakkhuviññāṇassa": "दृश्य रूप का इंद्रिय-क्षेत्र आँख की चेतना के लिए",
    "phoṭṭhabbāyatanaṃ kāyaviññāṇassa": "स्पर्श का इंद्रिय-क्षेत्र शरीर की चेतना के लिए",
    "cakkhāyatanaṃ cakkhuviññāṇassa": "आँख का इंद्रिय-क्षेत्र आँख की चेतना के लिए",
    "kāyāyatanaṃ kāyaviññāṇassa": "शरीर का इंद्रिय-क्षेत्र शरीर की चेतना के लिए",
    "vatthu {N:ānaṃ} khandhānaṃ purejātapaccayena paccayo": f"आधार {{Nm}} समूहों के लिए {INS('purejāta')} होता है",
    "vatthu {P:ānaṃ} khandhānaṃ purejātapaccayena paccayo": f"आधार {{Pm}} समूहों के लिए {INS('purejāta')} होता है",
    "vatthuṃ assādeti abhinandati": "आधार का रस लेता है, उसमें आनंद लेता है",
    "vatthu {K:ānaṃ} purejātapaccayena paccayo": f"आधार {{Kno}} के लिए {INS('purejāta')} होता है",
    "taṃ ārabbha {K:ā} ca sampayuttakā ca khandhā uppajjanti": f"उसे विषय बनाकर {{Kn}} और {SAMP} उत्पन्न होते हैं",
    "vatthu {K:ānaṃ} sampayuttakānañca khandhānaṃ purejātapaccayena paccayo":
        f"आधार {{Kno}} के लिए और {SKH} {INS('purejāta')} होता है",
    "sahajātā": "सह-उत्पत्ति रूपी", "nānākkhaṇikā": "भिन्न क्षण रूपी",
    "sahajātaṃ": "सह-उत्पत्ति रूपी", "pacchājātaṃ": "पश्चात्-उत्पत्ति रूपी", "purejātaṃ": "पूर्व-उत्पत्ति रूपी",
    "āhāraṃ": "आहार रूपी", "indriyaṃ": "क्षमता रूपी", "sahajāto": "सह-उत्पत्ति रूपी",
    "pacchājātā": "पश्चात्-उत्पत्ति रूपी",
    "{N:ā} cetanā sampayuttakānaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ kammapaccayena paccayo":
        f"{{Nms}} इरादा {SKH} और {CSRF} {INS('kamma')} होता है",
    "{P:ā} cetanā sampayuttakānaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ kammapaccayena paccayo":
        f"{{Pms}} इरादा {SKH} और {CSRF} {INS('kamma')} होता है",
    "{N:ā} cetanā vipākānaṃ khandhānaṃ kaṭattā ca rūpānaṃ kammapaccayena paccayo":
        f"{{Nms}} इरादा {VIPF} और {KTRF} {INS('kamma')} होता है",
    "{P:ā} cetanā vipākānaṃ khandhānaṃ kaṭattā ca rūpānaṃ kammapaccayena paccayo":
        f"{{Pms}} इरादा {VIPF} और {KTRF} {INS('kamma')} होता है",
    "{N:ā} cetanā {K:ānaṃ} kammapaccayena paccayo": f"{{Nms}} इरादा {{Kno}} के लिए {INS('kamma')} होता है",
    "{N:ā} cetanā sampayuttakānaṃ khandhānaṃ {K:ānaṃ} cittasamuṭṭhānānañca rūpānaṃ kammapaccayena paccayo":
        f"{{Nms}} इरादा {SKH}, {{Kno}} के लिए और {CSRF} {INS('kamma')} होता है",
    "{P:ā} cetanā sampayuttakānaṃ khandhānaṃ kammapaccayena paccayo": f"{{Pms}} इरादा {SKH} {INS('kamma')} होता है",
    "{P:ā} cetanā cittasamuṭṭhānānaṃ rūpānaṃ kammapaccayena paccayo": f"{{Pms}} इरादा {CSRF} {INS('kamma')} होता है",
    "vatthu {K:ānaṃ} vippayuttapaccayena paccayo": f"आधार {{Kno}} के लिए {INS('vippayutta')} होता है",
    "vatthu {K:ānaṃ} sampayuttakānañca khandhānaṃ vippayuttapaccayena paccayo":
        f"आधार {{Kno}} के लिए और {SKH} {INS('vippayutta')} होता है",
    "vatthu {P:ānaṃ} khandhānaṃ vippayuttapaccayena paccayo": f"आधार {{Pm}} समूहों के लिए {INS('vippayutta')} होता है",
    "lobho ca sampayuttakā ca khandhā mohassa, diṭṭhiyā, thinassa, uddhaccassa, ahirikassa, anottappassa atthipaccayena paccayo":
        f"लोभ और {SAMP} मोह, दृष्टि, आलस्य, बेचैनी, निर्लज्जता, बुराई के प्रति निडरता के लिए {INS('atthi')} होते हैं",
    "lobho ca vatthu ca mohassa, diṭṭhiyā, thinassa, uddhaccassa, ahirikassa, anottappassa atthipaccayena paccayo":
        f"लोभ और आधार मोह, दृष्टि, आलस्य, बेचैनी, निर्लज्जता, बुराई के प्रति निडरता के लिए {INS('atthi')} होते हैं",
    "{N:o} eko khandho ca {K:o} ca tiṇṇannaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ atthipaccayena paccayo":
        f"{{Nms}} एक समूह और {{Ks}} तीन समूहों के लिए और {CSRF} {INS('atthi')} होते हैं",
    "dve khandhā ca": "दो समूह और",
    "{K:ā} ca mahābhūtā ca cittasamuṭṭhānānaṃ rūpānaṃ atthipaccayena paccayo":
        f"{{Kn}} और महाभूत {CSRF} {INS('atthi')} होते हैं",
    "{K:ā} ca vatthu ca {N:ānaṃ} khandhānaṃ atthipaccayena paccayo":
        f"{{Kn}} और आधार {{Nm}} समूहों के लिए {INS('atthi')} होते हैं",
    "{K:ā} ca sampayuttakā khandhā ca purejātassa imassa kāyassa atthipaccayena paccayo":
        f"{{Kn}} और {SAMP} पहले उत्पन्न इस शरीर के लिए {INS('atthi')} होते हैं",
    "{K:ā} ca sampayuttakā ca khandhā kabaḷīkāro āhāro ca imassa kāyassa atthipaccayena paccayo":
        f"{{Kn}}, {SAMP} और कौर-कौर खाया जाने वाला भोजन इस शरीर के लिए {INS('atthi')} होते हैं",
    "{K:ā} ca sampayuttakā ca khandhā rūpajīvitindriyañca kaṭattārūpānaṃ atthipaccayena paccayo":
        f"{{Kn}}, {SAMP} और {S.RUPAJIVITINDRIYA} {KTRF} {INS('atthi')} होते हैं",
    "{N:o} eko khandho ca lobho ca tiṇṇannaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ mohassa ca, diṭṭhiyā, thinassa, uddhaccassa, ahirikassa, anottappassa atthipaccayena paccayo":
        f"{{Nms}} एक समूह और लोभ तीन समूहों के लिए, {CSRF} और मोह, दृष्टि, आलस्य, बेचैनी, निर्लज्जता, बुराई के प्रति निडरता के लिए {INS('atthi')} होते हैं",
    "lobho ca vatthu ca mohassa, diṭṭhiyā, thinassa, uddhaccassa, ahirikassa, anottappassa sampayuttakānañca khandhānaṃ atthipaccayena paccayo":
        f"लोभ और आधार मोह, दृष्टि, आलस्य, बेचैनी, निर्लज्जता, बुराई के प्रति निडरता के लिए और {SKH} {INS('atthi')} होते हैं",
}
KD = "मन के क्लेश वाले दो के वर्गीकरण"   # kilesaduka (oblique)
G.update({
    "{P:aṃ} ekaṃ khandhañca vatthuñca paccayā tayo khandhā": "{Pm} एक समूह और आधार के कारण तीन समूह",
    "{N:aṃ} ekaṃ khandhañca vatthuñca paccayā tayo khandhā": "{Nm} एक समूह और आधार के कारण तीन समूह",
    "rāgaṃ assādeti abhinandati": "राग का रस लेता है, उसमें आनंद लेता है",
    "diṭṭhiṃ assādeti": "दृष्टि का रस लेता है",
    "vicikicchaṃ ārabbha": "संशय को विषय बनाकर",
    "uddhaccaṃ ārabbha": "बेचैनी को विषय बनाकर",
    "ariyā pahīne kilese paccavekkhanti": f"आर्य छोड़े जा चुके मन के क्लेशों पर {REVP}",
    "ariyā pahīne {K:e} paccavekkhanti": f"आर्य छोड़े जा चुके मन के क्लेशों पर {REVP}",
    "vikkhambhite kilese": "दबाए जा चुके मन के क्लेशों पर",
    "vikkhambhite {K:e}": "दबाए जा चुके मन के क्लेशों पर",
    "pubbe samudāciṇṇe": "पहले बार-बार उठे",
    "{P:e} khandhe aniccato": "{Pm} समूहों को अनित्य",
    "{N:e} khandhe aniccato": "{Nm} समूहों को अनित्य",
    "vatthuṃ {N:e} khandhe aniccato": "आधार को, {Nm} समूहों को अनित्य",
    "vatthuṃ {P:e} khandhe aniccato": "आधार को, {Pm} समूहों को अनित्य",
    "vipassati": S.VIPASSATI, "vipassanti": S.VIPASSANTI,
    "cetopariyañāṇena {P:acittasamaṅgissa} cittaṃ jānāti": f"{S.CETOPARIYENA} {{Pm}} मन से युक्त व्यक्ति के मन को जानता है",
    "cetopariyañāṇena {N:acittasamaṅgissa} cittaṃ jānāti": f"{S.CETOPARIYENA} {{Nm}} मन से युक्त व्यक्ति के मन को जानता है",
    "{P:ā} khandhā cetopariyañāṇassa, pubbenivāsānussatiñāṇassa, yathākammūpagañāṇassa, anāgataṃsañāṇassa, āvajjanāya ārammaṇapaccayena paccayo":
        f"{{Pm}} समूह {S.CETOPARIYA_OBL} के लिए, {S.PUBBENIVASA_OBL} के लिए, {S.YATHAKAMMUPAGA_OBL} के लिए, {S.ANAGATAMSA_OBL} के लिए, {AV} {INS('ārammaṇa')} होते हैं",
    "{N:ā} khandhā cetopariyañāṇassa, pubbenivāsānussatiñāṇassa, yathākammūpagañāṇassa, anāgataṃsañāṇassa, āvajjanāya ārammaṇapaccayena paccayo":
        f"{{Nm}} समूह {S.CETOPARIYA_OBL} के लिए, {S.PUBBENIVASA_OBL} के लिए, {S.YATHAKAMMUPAGA_OBL} के लिए, {S.ANAGATAMSA_OBL} के लिए, {AV} {INS('ārammaṇa')} होते हैं",
    "pubbenivāsānussatiñāṇassa": f"{S.PUBBENIVASA_OBL} के लिए",
    "yathākammūpagañāṇassa": f"{S.YATHAKAMMUPAGA_OBL} के लिए",
    "anāgataṃsañāṇassa": f"{S.ANAGATAMSA_OBL} के लिए",
    "cetopariyañāṇassa": f"{S.CETOPARIYA_OBL} के लिए",
    "āvajjanāya ārammaṇapaccayena paccayo": f"{AV} {INS('ārammaṇa')} होता है",
    "anāgataṃsañāṇassa, āvajjanāya ārammaṇapaccayena paccayo":
        f"{S.ANAGATAMSA_OBL} के लिए, {AV} {INS('ārammaṇa')} होते हैं",
    "ariyā maggā vuṭṭhahitvā maggaṃ paccavekkhanti": f"आर्य मार्ग से उठकर मार्ग पर {REVP}",
    "rāgaṃ garuṃ katvā assādeti abhinandati": "राग को महत्व देकर " + ASSADA,
    "diṭṭhiṃ garuṃ katvā assādeti abhinandati": "दृष्टि को महत्व देकर " + ASSADA,
    "jhānā vuṭṭhahitvā jhānaṃ garuṃ katvā paccavekkhati": f"ध्यान से उठकर ध्यान को महत्व देकर उस पर {REV}",
    "nibbānaṃ phalassa adhipatipaccayena paccayo": f"निर्वाण फल के लिए {INS('adhipati')} होता है",
    "{P:ā} khandhā vuṭṭhānassa anantarapaccayena paccayo": f"{{Pm}} समूह बाहर आने के लिए {INS('anantara')} होते हैं",
    "{N:ā} khandhā vuṭṭhānassa anantarapaccayena paccayo": f"{{Nm}} समूह बाहर आने के लिए {INS('anantara')} होते हैं",
    "āvajjanā {P:ānaṃ} khandhānaṃ anantarapaccayena paccayo":
        f"मन को विषय की ओर मोड़ना {{Pm}} समूहों के लिए {INS('anantara')} होता है",
    "āvajjanā {N:ānaṃ} khandhānaṃ anantarapaccayena paccayo":
        f"मन को विषय की ओर मोड़ना {{Nm}} समूहों के लिए {INS('anantara')} होता है",
    "rāgaṃ upanissāya pāṇaṃ hanati": "राग के प्रबल आश्रय से प्राणी की हत्या करता है",
    "patthanaṃ upanissāya pāṇaṃ hanati": "कामना के प्रबल आश्रय से प्राणी की हत्या करता है",
    "rāgo": "राग", "patthanā rāgassa": "कामना राग के लिए",
    "patthanāya upanissayapaccayena paccayo": f"कामना के लिए {INS('upanissaya')} होते हैं",
    "rāgaṃ upanissāya dānaṃ deti": "राग के प्रबल आश्रय से दान देता है",
    "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है",
    "patthanaṃ upanissāya dānaṃ deti": "कामना के प्रबल आश्रय से दान देता है",
    "patthanā saddhāya": "कामना श्रद्धा के लिए",
    "paññāya kāyikassa sukhassa": "प्रज्ञा के लिए, शारीरिक सुख के लिए",
    "kāyikassa dukkhassa": "शारीरिक दुःख के लिए",
    "maggassa": "मार्ग के लिए",
    "senāsanaṃ rāgassa": "निवास-स्थान राग के लिए",
    "{P:o} eko khandho ca vatthu ca tiṇṇannaṃ khandhānaṃ atthipaccayena paccayo":
        f"{{Pms}} एक समूह और आधार तीन समूहों के लिए {INS('atthi')} होते हैं",
    "{P:ā} khandhā ca mahābhūtā ca cittasamuṭṭhānānaṃ rūpānaṃ atthipaccayena paccayo":
        f"{{Pm}} समूह और महाभूत {CSRF} {INS('atthi')} होते हैं",
    "{P:ā} khandhā ca kabaḷīkāro āhāro ca imassa kāyassa atthipaccayena paccayo":
        f"{{Pm}} समूह और कौर-कौर खाया जाने वाला भोजन इस शरीर के लिए {INS('atthi')} होते हैं",
    "{P:ā} khandhā ca rūpajīvitindriyañca kaṭattārūpānaṃ atthipaccayena paccayo":
        f"{{Pm}} समूह और {S.RUPAJIVITINDRIYA} {KTRF} {INS('atthi')} होते हैं",
    "{P:ā} hetū sampayuttakānaṃ {K:ānaṃ} hetupaccayena paccayo": f"{{Pm}} मूल जुड़े हुए {{Kno}} के लिए {INS('hetu')} होते हैं",
    "assādeti abhinandati": ASSADA,
    "ariyā gotrabhuṃ paccavekkhanti": f"आर्य {S.GOTRABHU} पर {REVP}",
    "vodānaṃ paccavekkhanti": f"{S.VODANA} पर {REVP}",
    "sekkhā gotrabhuṃ garuṃ katvā paccavekkhanti": f"{S.SEKKHA} {S.GOTRABHU} को महत्व देकर उस पर {REVP}",
    "vodānaṃ garuṃ katvā paccavekkhanti": f"{S.VODANA} को महत्व देकर उस पर {REVP}",
    "vatthuṃ {N:e} khandhe garuṃ katvā {N:ā} khandhā uppajjanti": "आधार को, {Nm} समूहों को महत्व देकर {Nm} समूह उत्पन्न होते हैं",
    "vatthuṃ {P:e} khandhe garuṃ katvā {P:ā} khandhā uppajjanti": "आधार को, {Pm} समूहों को महत्व देकर {Pm} समूह उत्पन्न होते हैं",
    "anulomaṃ gotrabhussa": f"अनुकूलता {S.GOTRABHU} के लिए",
    "anulomaṃ vodānassa": f"अनुकूलता {S.VODANA} के लिए",
    "{P:ā} hetū sampayuttakānaṃ khandhānaṃ {K:ānaṃ} ca hetupaccayena paccayo":
        f"{{Pm}} मूल {SKH} और {{Kno}} के लिए {INS('hetu')} होते हैं",
    "{K:e} ārabbha {K:ā} ca sampayuttakā khandhā ca uppajjanti": f"{{Kno}} को विषय बनाकर {{Kn}} और {SAMP} उत्पन्न होते हैं",
    "{N:e} khandhe ārabbha {N:ā} khandhā uppajjanti": "{Nm} समूहों को विषय बनाकर {Nm} समूह उत्पन्न होते हैं",
    "{P:e} khandhe ārabbha {P:ā} khandhā uppajjanti": "{Pm} समूहों को विषय बनाकर {Pm} समूह उत्पन्न होते हैं",
    "{N:e} khandhe ārabbha {K:ā} uppajjanti": "{Nm} समूहों को विषय बनाकर {Kn} उत्पन्न होते हैं",
    "{N:e} khandhe ārabbha {K:ā} ca sampayuttakā khandhā ca uppajjanti":
        f"{{Nm}} समूहों को विषय बनाकर {{Kn}} और {SAMP} उत्पन्न होते हैं",
    "{N:e} khandhe garuṃ katvā": "{Nm} समूहों को महत्व देकर",
    "{P:e} khandhe garuṃ katvā": "{Pm} समूहों को महत्व देकर",
    "nava pañhā": "नौ प्रश्न",
    "{N:ā} cetanā sampayuttakānaṃ khandhānaṃ kammapaccayena paccayo": f"{{Nms}} इरादा {SKH} {INS('kamma')} होता है",
    "{N:ā} cetanā sampayuttakānaṃ {K:ānaṃ} kammapaccayena paccayo": f"{{Nms}} इरादा जुड़े हुए {{Kno}} के लिए {INS('kamma')} होता है",
    "{N:ā} cetanā sampayuttakānaṃ khandhānaṃ {K:ānaṃ} ca kammapaccayena paccayo":
        f"{{Nms}} इरादा {SKH} और {{Kno}} के लिए {INS('kamma')} होता है",
})
PAREN.update({
    "kusalattikasadisaṃ": "हितकर वाले तीन के वर्गीकरण के समान",
    "{P:adukaṃ} saṃkiliṭṭhadukasadisaṃ, ninnānākaraṇaṃ.":
        "क्लेशों से जुड़ाव वाला दो का वर्गीकरण क्लेशों से मलिन वाले दो के वर्गीकरण के समान है, बिना किसी भिन्नता के।",
    "evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi kilesadukasadisā. Ninnānākaraṇaṃ. Āmasanaṃ nānaṃ.":
        f"इसी तरह निर्भरता का खंड भी, सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, घुले-मिले होने का खंड भी और जुड़ाव का खंड भी {KD} के समान हैं। कोई भिन्नता नहीं। केवल पदों का उल्लेख अलग है।",
    "evaṃ cattāri, kilesadukasadisaṃ.": f"इसी तरह चार, {KD} के समान।",
    "itare dve kilesadukasadisā, ghaṭanārammaṇāpi kilesadukasadisā":
        f"अन्य दो {KD} के समान हैं, संयुक्त पदों वाला विषय-कारण भी {KD} के समान है",
    "itare dvepi kilesadukasadisā. Ghaṭanādhipatipi.": f"अन्य दो भी {KD} के समान हैं। संयुक्त पदों वाली प्रधानता भी।",
    "kilesadukasadisā": f"{KD} के समान",
    "itare dve anantarā kilesadukasadisā, ninnānākaraṇā. Ghaṭanānantarampi sabbe paccayā kilesadukasadisā, ninnānākaraṇā. Upanissaye lokuttaraṃ natthi, idaṃ dukaṃ kilesadukasadisaṃ, ninnānākaraṇaṃ.":
        f"अन्य दो निकटता-कारण {KD} के समान हैं, बिना किसी भिन्नता के। संयुक्त पदों वाला निकटता-कारण भी और सभी कारण भी {KD} के समान हैं, बिना किसी भिन्नता के। प्रबल आश्रय-कारण में लोकोत्तर नहीं है, यह दो का वर्गीकरण {KD} के समान है, बिना किसी भिन्नता के।",
    "evaṃ itare dve gaṇanāpi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā.":
        "इसी तरह अन्य दो गणनाएँ भी, सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, घुले-मिले होने का खंड भी और जुड़ाव का खंड भी निर्भरता के खंड के समान हैं।",
    "itarepi tīṇi kātabbā.": "अन्य तीन भी तैयार करने चाहिए।",
    "dve adhipati tīṇipi kātabbā, itare dvepi tīṇi kātabbā.":
        "दोनों प्रधानताओं के साथ तीनों तैयार करने चाहिए, अन्य दो के भी तीन तैयार करने चाहिए।",
    "navapi kātabbā, āvajjanāpi vuṭṭhānampi natthi": "नौ के नौ तैयार करने चाहिए, मन को विषय की ओर मोड़ना भी और बाहर आना भी नहीं है",
    "purejātapaccayo pacchājātapaccayopi natthi": "पूर्व-उत्पत्ति-कारण और पश्चात्-उत्पत्ति-कारण भी नहीं है",
    "navapi, tīṇiyeva padā kātabbā.": "नौ के नौ, केवल तीन पद तैयार करने चाहिए।",
    "kilesasaṃkiliṭṭhadukasadisaṃ ninnānākaraṇaṃ, sabbe vārā.":
        "मन के क्लेश और क्लेशों से मलिन वाले दो के वर्गीकरण के समान, बिना किसी भिन्नता के, सभी खंड।",
})
def PN(k, v):
    """Register a key written with {X:..} / {X..} for both items P and N."""
    for side in "PN":
        G[k.replace("{X:", "{" + side + ":")] = v.replace("{X", "{" + side)


DS = "सत्य-दर्शन से छोड़े जाने वाला दो का वर्गीकरण"
DSO = "सत्य-दर्शन से छोड़े जाने वाले दो के वर्गीकरण"
for _k, _v in {
    "{X:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca": "{Xm} एक समूह पर निर्भर होकर तीन समूह और मन से उत्पन्न",
    "ahetukaṃ {X:aṃ} ekaṃ khandhaṃ": f"{S.AHETUKA}, {{Xm}} एक समूह {{DEP}}",
    "{X:aṃ} rāgaṃ assādeti abhinandati": "{Xm} राग का रस लेता है, उसमें आनंद लेता है",
    "taṃ ārabbha {X:o} rāgo uppajjati": "उसे विषय बनाकर {Xms} राग उत्पन्न होता है",
    "taṃ ārabbha {X:o} rāgo": "उसे विषय बनाकर {Xms} राग",
    "{X:aṃ} domanassaṃ uppajjati": "{Xf} उदासी उत्पन्न होती है",
    "{X:aṃ} diṭṭhiṃ assādeti abhinandati": "{Xf} दृष्टि का रस लेता है, उसमें आनंद लेता है",
    "{X:aṃ} domanassaṃ ārabbha {X:aṃ} domanassaṃ uppajjati": "{Xf} उदासी को विषय बनाकर {Xf} उदासी उत्पन्न होती है",
    "ariyā {X:e} pahīne kilese paccavekkhanti": f"आर्य {{Xm}} छोड़े जा चुके मन के क्लेशों पर {REVP}",
    "ariyā {X:e} pahīne kilese": "आर्य {Xm} छोड़े जा चुके मन के क्लेशों पर",
    "{X:ā} khandhā cetopariyañāṇassa": f"{{Xm}} समूह {S.CETOPARIYA_OBL} के लिए",
    "taṃ ārabbha {X:o} rāgo uppajjati": "उसे विषय बनाकर {Xms} राग उत्पन्न होता है",
    "{X:aṃ} rāgaṃ garuṃ katvā assādeti abhinandati": "{Xm} राग को महत्व देकर " + ASSADA,
    "taṃ garuṃ katvā {X:o} rāgo uppajjati": "उसे महत्व देकर {Xms} राग उत्पन्न होता है",
    "purimā purimā {X:ā} khandhā": "पहले-पहले के {Xm} समूह",
    "{X:aṃ} rāgaṃ upanissāya pāṇaṃ hanati": "{Xm} राग के प्रबल आश्रय से प्राणी की हत्या करता है",
    "{X:aṃ} rāgaṃ upanissāya dānaṃ deti": "{Xm} राग के प्रबल आश्रय से दान देता है",
    "{X:aṃ} dosaṃ": "{Xms} द्वेष", "{X:o} rāgo": "{Xms} राग", "{X:aṃ} rāgaṃ": "{Xms} राग",
    "patthanā {X:assa} rāgassa": "कामना {Xm} राग के लिए",
    "samāpattiṃ uppādeti {X:aṃ} dosaṃ": "ध्यान-अवस्था उत्पन्न करता है, {Xms} द्वेष",
    "paññāya {X:assa} rāgassa": "प्रज्ञा के लिए, {Xm} राग के लिए",
    "paññāya {X:assa}": "प्रज्ञा के लिए, {Xm} के लिए",
    "senāsanaṃ {X:assa} rāgassa": "निवास-स्थान {Xm} राग के लिए",
    "vatthuṃ {X:e} khandhe assādeti abhinandati": "आधार का, {Xm} समूहों का रस लेता है, उनमें आनंद लेता है",
}.items():
    PN(_k, _v)
G.update({
    "vicikicchā uppajjati": "संशय उत्पन्न होता है",
    "vicikicchaṃ ārabbha vicikicchā uppajjati": "संशय को विषय बनाकर संशय उत्पन्न होता है",
    "uddhaccaṃ ārabbha uddhaccaṃ uppajjati": "बेचैनी को विषय बनाकर बेचैनी उत्पन्न होती है",
    "uposathakammaṃ katvā taṃ paccavekkhati assādeti abhinandati":
        f"उपवास-व्रत का पालन करके उस पर {REV}, {ASSADA}",
    "phalassa āvajjanāya ārammaṇapaccayena paccayo": f"फल के लिए और {AV} {INS('ārammaṇa')} होता है",
    "phalassa": "फल के लिए",
    "vipassati assādeti abhinandati": f"{S.VIPASSATI}, {ASSADA_PL}",
    "diṭṭhiṃ garuṃ katvā": "दृष्टि को महत्व देकर",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā": "आर्य मार्ग से उठकर मार्ग को महत्व देकर",
    "dānaṃ datvā": "दान देकर", "dānaṃ datvā sīlaṃ": "दान देकर, सदाचार",
    "dosassa": "द्वेष के लिए", "mohassa": "मोह के लिए", "mānassa": "अहंकार के लिए", "rāgassa": "राग के लिए",
    "patthanāya": "कामना के लिए", "kāyikassa sukhassa": "शारीरिक सुख के लिए", "diṭṭhiyā": "दृष्टि के लिए",
    "paññā": "प्रज्ञा", "patthanā": "कामना", "doso": "द्वेष", "moho": "मोह", "māno": "अहंकार",
    "saddhaṃ upanissāya diṭṭhiṃ gaṇhāti": "श्रद्धा के प्रबल आश्रय से दृष्टि ग्रहण करता है",
    "paññaṃ upanissāya diṭṭhiṃ gaṇhāti": "प्रज्ञा के प्रबल आश्रय से दृष्टि ग्रहण करता है",
    "vatthuṃ aniccato": "आधार को अनित्य",
    "pāṇaṃ hanati": "प्राणी की हत्या करता है",
    "senāsanaṃ upanissāya mānaṃ jappeti": "निवास-स्थान के प्रबल आश्रय से अहंकार पालता है",
    "ārammaṇādhipati sahajātādhipati": f"{S.ARAMMANADHIPATI}, {S.SAHAJATADHIPATI}",
    "mahābhūte paccayā cittasamuṭṭhānaṃ": "महाभूतों के कारण मन से उत्पन्न",
    "vatthuṃ paccayā uddhaccasahagato moho": f"आधार के कारण {U_MOHA}",
    "vatthuṃ paccayā vicikicchāsahagato moho": f"आधार के कारण {V_MOHA}",
    "vicikicchāsahagate khandhe ca vatthuñca paccayā vicikicchāsahagato moho": f"{V_KH} और आधार के कारण {V_MOHA}",
    "uddhaccasahagate khandhe ca vatthuñca paccayā uddhaccasahagato moho": f"{U_KH} और आधार के कारण {U_MOHA}",
    "vicikicchāsahagataṃ mohaṃ paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"संशय के साथ होने वाले मोह पर निर्भर होकर {CSR}",
    "vicikicchāsahagataṃ mohaṃ paṭicca sampayuttakā khandhā": f"संशय के साथ होने वाले मोह पर निर्भर होकर {SAMP}",
    "vicikicchāsahagataṃ mohaṃ paṭicca sampayuttakā khandhā cittasamuṭṭhānañca rūpaṃ":
        f"संशय के साथ होने वाले मोह पर निर्भर होकर {SAMP} और {CSR}",
    "vicikicchāsahagataṃ ekaṃ khandhañca mohañca paṭicca tayo khandhā":
        "संशय के साथ होने वाले एक समूह और मोह पर निर्भर होकर तीन समूह",
    "vicikicchāsahagate khandhe ca mohañca paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{V_KH} और मोह पर निर्भर होकर {CSR}",
    "vicikicchāsahagataṃ ekaṃ khandhañca mohañca paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"संशय के साथ होने वाले एक समूह और मोह पर निर्भर होकर तीन समूह और {CSR}",
})
PAREN.update({
    "itare dve gaṇanāpi sahajātavāropi kātabbo.": "अन्य दो गणनाएँ भी और सह-उत्पत्ति का खंड भी तैयार करना चाहिए।",
    "itare dve gaṇanāpi nissayavāropi kātabbo.": "अन्य दो गणनाएँ भी और आश्रय का खंड भी तैयार करना चाहिए।",
    "itare dve gaṇanāpi sampayuttavāropi kātabbo.": "अन्य दो गणनाएँ भी और जुड़ाव का खंड भी तैयार करना चाहिए।",
    "saṃkhittaṃ, purejātasadisaṃ": "संक्षिप्त, पूर्व-उत्पत्ति-कारण के समान",
    "yathā dassanadukaṃ, evaṃ vitthāretabbaṃ, ninnānākaraṇaṃ":
        f"जैसे {DS}, वैसे ही विस्तार करना चाहिए, बिना किसी भिन्नता के",
    "paccayavārapaccanīye nahetupaccaye uddhaccasahagate tīṇi, moho uddharitabbo. Sabbepi vārā dassanadukasadisā, uddhaccapaccanīyampi nānaṃ.":
        f"कारण के खंड के नकारात्मक क्रम में, मूल-कारण के अभाव में, बेचैनी के साथ होने वाले में तीन, मोह को अलग करके लेना चाहिए। सभी खंड भी {DSO} के समान हैं, बेचैनी वाला नकारात्मक क्रम भी अलग है।",
    "dassanadukasadisā bhāvanā ninnānākaraṇā": f"मानसिक अभ्यास वाला भाग {DSO} के समान है, बिना किसी भिन्नता के",
    "sabbapaccayā dassanadukasadisā, bhāvanā ninnānākaraṇā.":
        f"सभी कारण {DSO} के समान हैं, मानसिक अभ्यास वाला भाग बिना किसी भिन्नता के।",
    "paccanīyavibhaṅgo dassanadukasadiso vibhajitabbo. Evaṃ tīṇi gaṇanāpi gaṇetabbā.":
        f"नकारात्मक क्रम का विश्लेषण {DSO} के समान करना चाहिए। इसी तरह तीनों गणनाएँ भी गिननी चाहिए।",
})
DHO = "सत्य-दर्शन से छोड़े जाने वाले मूलों वाले दो के वर्गीकरण"
VS = "संशय के साथ होने वाले"
US = "बेचैनी के साथ होने वाले"
VIT = "आरंभिक विचार"
for _k, _v in {
    "{X:e} khandhe ārabbha {Y:ā} khandhā ca moho ca uppajjanti": "{Xm} समूहों को विषय बनाकर {Ym} समूह और मोह उत्पन्न होते हैं",
    "{X:ā} khandhā {Y:ānaṃ} khandhānaṃ upanissayapaccayena paccayo": f"{{Xm}} समूह {{Ym}} समूहों के लिए {INS('upanissaya')} होते हैं",
    "{X:ā} khandhā {Y:ānaṃ} khandhānaṃ mohassa ca upanissayapaccayena paccayo":
        f"{{Xm}} समूह {{Ym}} समूहों के लिए और मोह के लिए {INS('upanissaya')} होते हैं",
    "{X:e} khandhe garuṃ katvā {Y:ā} khandhā uppajjanti": "{Xm} समूहों को महत्व देकर {Ym} समूह उत्पन्न होते हैं",
}.items():
    for _a in "PN":
        for _b in "PN":
            G[_k.replace("{X:", "{" + _a + ":").replace("{Y:", "{" + _b + ":")] = \
                _v.replace("{X", "{" + _a).replace("{Y", "{" + _b)
for _k, _v in {
    "{X:e} khandhe ārabbha vicikicchāsahagatā khandhā ca moho ca uppajjanti": f"{{Xm}} समूहों को विषय बनाकर {VS} समूह और मोह उत्पन्न होते हैं",
    "vatthuṃ {X:e} khandhe ca mohañca aniccato": "आधार को, {Xm} समूहों और मोह को अनित्य",
    "vatthuṃ {X:e} khandhe ca mohañca assādeti abhinandati": "आधार का, {Xm} समूहों और मोह का रस लेता है, उनमें आनंद लेता है",
    "vatthuṃ {X:e} khandhe ca mohañca ārabbha vicikicchāsahagatā khandhā ca moho ca uppajjanti":
        f"आधार को, {{Xm}} समूहों और मोह को विषय बनाकर {VS} समूह और मोह उत्पन्न होते हैं",
    "vatthuṃ {X:e} khandhe ca mohañca ārabbha uddhaccasahagatā khandhā ca moho ca uppajjanti":
        f"आधार को, {{Xm}} समूहों और मोह को विषय बनाकर {US} समूह और मोह उत्पन्न होते हैं",
    "vicikicchāsahagate khandhe ca mohañca ārabbha {X:ā} khandhā uppajjanti": f"{V_KH} और मोह को विषय बनाकर {{Xm}} समूह उत्पन्न होते हैं",
    "vicikicchāsahagate khandhe ca mohañca ārabbha {X:ā} khandhā ca moho ca uppajjanti":
        f"{V_KH} और मोह को विषय बनाकर {{Xm}} समूह और मोह उत्पन्न होते हैं",
    "{X:ā} khandhā vicikicchāsahagatānaṃ khandhānaṃ mohassa ca upanissayapaccayena paccayo":
        f"{{Xm}} समूह {VS} समूहों के लिए और मोह के लिए {INS('upanissaya')} होते हैं",
    "{X:ā} khandhā uddhaccasahagatānaṃ khandhānaṃ mohassa ca upanissayapaccayena paccayo":
        f"{{Xm}} समूह {US} समूहों के लिए और मोह के लिए {INS('upanissaya')} होते हैं",
    "vicikicchāsahagatā khandhā ca moho ca {X:ānaṃ} khandhānaṃ upanissayapaccayena paccayo":
        f"{VS} समूह और मोह {{Xm}} समूहों के लिए {INS('upanissaya')} होते हैं",
    "vicikicchāsahagatā khandhā ca moho ca {X:ānaṃ} khandhānaṃ mohassa ca upanissayapaccayena paccayo":
        f"{VS} समूह और मोह {{Xm}} समूहों के लिए और मोह के लिए {INS('upanissaya')} होते हैं",
    "{X:assa} rāgassa": "{Xm} राग के लिए",
    "{X:e} khandhe paṭicca vitakko cittasamuṭṭhānañca rūpaṃ": f"{{Xm}} समूहों पर निर्भर होकर {VIT} और {CSR}",
    "{X:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā vitakko ca cittasamuṭṭhānañca rūpaṃ":
        f"{{Xm}} एक समूह पर निर्भर होकर तीन समूह, {VIT} और {CSR}",
    "{X:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā kaṭattā ca rūpaṃ": f"{{Xm}} एक समूह पर निर्भर होकर तीन समूह और {S.KTR}",
    "vatthuṃ paṭicca {X:ā} khandhā": "आधार पर निर्भर होकर {Xm} समूह",
    "vitakkaṃ paṭicca {X:ā} khandhā": f"{VIT} पर निर्भर होकर {{Xm}} समूह",
    "{X:aṃ} ekaṃ khandhañca vitakkañca paṭicca tayo khandhā": f"{{Xm}} एक समूह और {VIT} पर निर्भर होकर तीन समूह",
    "{X:aṃ} ekaṃ khandhañca vatthuñca paṭicca tayo khandhā": "{Xm} एक समूह और आधार पर निर्भर होकर तीन समूह",
    "{X:e} khandhe ca vitakkañca mahābhūte ca paṭicca cittasamuṭṭhānaṃ rūpaṃ":
        f"{{Xm}} समूहों, {VIT} और महाभूतों पर निर्भर होकर {CSR}",
    "{X:e} khandhe ca vitakkañca mahābhūte ca paṭicca kaṭattārūpaṃ":
        f"{{Xm}} समूहों, {VIT} और महाभूतों पर निर्भर होकर {S.KTR}",
    "{X:e} khandhe ca vatthuñca paṭicca vitakko": f"{{Xm}} समूहों और आधार पर निर्भर होकर {VIT}",
    "{X:aṃ} ekaṃ khandhañca vitakkañca paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"{{Xm}} एक समूह और {VIT} पर निर्भर होकर तीन समूह और {CSR}",
    "{X:aṃ} ekaṃ khandhañca vitakkañca paṭicca tayo khandhā kaṭattā ca rūpaṃ":
        f"{{Xm}} एक समूह और {VIT} पर निर्भर होकर तीन समूह और {S.KTR}",
    "{X:aṃ} ekaṃ khandhañca vatthuñca paṭicca tayo khandhā vitakko ca": f"{{Xm}} एक समूह और आधार पर निर्भर होकर तीन समूह और {VIT}",
    "{X:aṃ} ekaṃ khandhañca vatthuñca vitakkañca paṭicca tayo khandhā": f"{{Xm}} एक समूह, आधार और {VIT} पर निर्भर होकर तीन समूह",
    "vatthuṃ paṭicca ahetukā {X:ā} khandhā": f"आधार पर निर्भर होकर {S.AHETUKA}, {{Xm}} समूह",
}.items():
    PN(_k, _v)
G.update({
    "{N:aṃ} dhammaṃ paṭicca {N:o} dhammo uppajjati nahetupaccayā ahetukaṃ {N:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"{{Nf}} परिघटना पर निर्भर होकर {{Nf}} परिघटना {S.NABL('hetu')} उत्पन्न होती है, {S.AHETUKA}, {{Nm}} एक समूह पर निर्भर होकर तीन समूह और {CSR}",
    "vicikicchāsahagataṃ ekaṃ khandhaṃ paṭicca tayo khandhā moho ca": f"{VS} एक समूह पर निर्भर होकर तीन समूह और मोह",
    "vicikicchāsahagataṃ ekaṃ khandhañca vatthuñca paccayā tayo khandhā": f"{VS} एक समूह और आधार के कारण तीन समूह",
    "vicikicchāsahagataṃ ekaṃ khandhañca vatthuñca paccayā tayo khandhā moho ca": f"{VS} एक समूह और आधार के कारण तीन समूह और मोह",
    "vatthuṃ paccayā vicikicchāsahagatā khandhā ca moho ca": f"आधार के कारण {VS} समूह और मोह",
    "vicikicchāsahagato moho cittasamuṭṭhānānaṃ rūpānaṃ hetupaccayena paccayo": f"{V_MOHA} {CSRF} {INS('hetu')} होता है",
    "vicikicchāsahagato moho sampayuttakānaṃ khandhānaṃ hetupaccayena paccayo": f"{V_MOHA} {SKH} {INS('hetu')} होता है",
    "vicikicchāsahagato moho sampayuttakānaṃ khandhānaṃ cittasamuṭṭhānānañca rūpānaṃ hetupaccayena paccayo":
        f"{V_MOHA} {SKH} और {CSRF} {INS('hetu')} होता है",
    "uposathakammaṃ katvā taṃ paccavekkhati": f"उपवास-व्रत का पालन करके उस पर {REV}",
    "uposathakammaṃ katvā": "उपवास-व्रत का पालन करके",
    "pubbe samudāciṇṇe kilese jānanti": "पहले बार-बार उठे मन के क्लेशों को जानते हैं",
    "āvajjanāya": AV,
    "mohassa ca ārammaṇapaccayena paccayo": f"और मोह के लिए {INS('ārammaṇa')} होते हैं",
    "vicikicchāsahagate khandhe ca mohañca ārabbha vicikicchāsahagatā khandhā ca moho ca uppajjanti":
        f"{V_KH} और मोह को विषय बनाकर {VS} समूह और मोह उत्पन्न होते हैं",
    "purimā purimā vicikicchāsahagatā khandhā pacchimassa pacchimassa vicikicchāsahagatassa mohassa anantarapaccayena paccayo":
        f"पहले-पहले के {VS} समूह बाद-बाद के {VS} मोह के लिए {INS('anantara')} होते हैं",
    "purimā purimā vicikicchāsahagatā khandhā pacchimānaṃ pacchimānaṃ vicikicchāsahagatānaṃ khandhānaṃ mohassa ca anantarapaccayena paccayo":
        f"पहले-पहले के {VS} समूह बाद-बाद के {VS} समूहों के लिए और मोह के लिए {INS('anantara')} होते हैं",
    "purimā purimā vicikicchāsahagatā khandhā pacchimānaṃ pacchimānaṃ vicikicchāsahagatānaṃ khandhānaṃ anantarapaccayena paccayo":
        f"पहले-पहले के {VS} समूह बाद-बाद के {VS} समूहों के लिए {INS('anantara')} होते हैं",
    "purimo purimo vicikicchāsahagato moho pacchimassa pacchimassa vicikicchāsahagatassa mohassa anantarapaccayena paccayo":
        f"पहले-पहले का {V_MOHA} बाद-बाद के {VS} मोह के लिए {INS('anantara')} होता है",
    "purimo purimo vicikicchāsahagato moho pacchimānaṃ pacchimānaṃ vicikicchāsahagatānaṃ khandhānaṃ anantarapaccayena paccayo":
        f"पहले-पहले का {V_MOHA} बाद-बाद के {VS} समूहों के लिए {INS('anantara')} होता है",
    "purimo purimo vicikicchāsahagato moho pacchimānaṃ pacchimānaṃ vicikicchāsahagatānaṃ khandhānaṃ mohassa ca anantarapaccayena paccayo":
        f"पहले-पहले का {V_MOHA} बाद-बाद के {VS} समूहों के लिए और मोह के लिए {INS('anantara')} होता है",
    "āvajjanā vicikicchāsahagatānaṃ khandhānaṃ mohassa ca anantarapaccayena paccayo":
        f"मन को विषय की ओर मोड़ना {VS} समूहों के लिए और मोह के लिए {INS('anantara')} होता है",
    "purimā purimā vicikicchāsahagatā khandhā ca moho ca pacchimānaṃ pacchimānaṃ vicikicchāsahagatānaṃ khandhānaṃ anantarapaccayena paccayo":
        f"पहले-पहले के {VS} समूह और मोह बाद-बाद के {VS} समूहों के लिए {INS('anantara')} होते हैं",
    "purimā purimā vicikicchāsahagatā khandhā ca moho ca pacchimassa pacchimassa vicikicchāsahagatassa mohassa anantarapaccayena paccayo":
        f"पहले-पहले के {VS} समूह और मोह बाद-बाद के {VS} मोह के लिए {INS('anantara')} होते हैं",
    "vicikicchāsahagatā khandhā ca moho ca vuṭṭhānassa anantarapaccayena paccayo":
        f"{VS} समूह और मोह बाहर आने के लिए {INS('anantara')} होते हैं",
    "purimā purimā vicikicchāsahagatā khandhā ca moho ca pacchimānaṃ pacchimānaṃ vicikicchāsahagatānaṃ khandhānaṃ mohassa ca anantarapaccayena paccayo":
        f"पहले-पहले के {VS} समूह और मोह बाद-बाद के {VS} समूहों के लिए और मोह के लिए {INS('anantara')} होते हैं",
    "samāpattiṃ uppādeti mānaṃ jappeti": "ध्यान-अवस्था उत्पन्न करता है, अहंकार पालता है",
    "patthanāya phalasamāpattiyā upanissayapaccayena paccayo": f"कामना के लिए, फल की ध्यान-अवस्था के लिए {INS('upanissaya')} होते हैं",
    "senāsanaṃ": "निवास-स्थान",
    "vicikicchāsahagatānaṃ khandhānaṃ mohassa ca upanissayapaccayena paccayo":
        f"{VS} समूहों के लिए और मोह के लिए {INS('upanissaya')} होते हैं",
    "vicikicchāsahagatā khandhā ca moho ca vicikicchāsahagatānaṃ khandhānaṃ mohassa ca upanissayapaccayena paccayo":
        f"{VS} समूह और मोह {VS} समूहों के लिए और मोह के लिए {INS('upanissaya')} होते हैं",
    "dibbena": "दिव्य",
    "vatthuṃ ārabbha vicikicchāsahagatā khandhā ca moho ca uppajjanti": f"आधार को विषय बनाकर {VS} समूह और मोह उत्पन्न होते हैं",
    "vicikicchāsahagato eko khandho ca moho ca tiṇṇannaṃ khandhānaṃ atthipaccayena paccayo":
        f"संशय के साथ होने वाला एक समूह और मोह तीन समूहों के लिए {INS('atthi')} होते हैं",
    "ariyā maggā": "आर्य मार्ग से",
    "sakabhaṇḍe chandarāgo parabhaṇḍe chandarāgassa upanissayapaccayena paccayo":
        f"अपनी वस्तुओं के प्रति चाह भरा राग पराई वस्तुओं के प्रति चाह भरे राग के लिए {INS('upanissaya')} होता है",
    "sakapariggahe chandarāgo parapariggahe chandarāgassa upanissayapaccayena paccayo":
        f"अपनी अधिकार की चीज़ों के प्रति चाह भरा राग दूसरों के अधिकार की चीज़ों के प्रति चाह भरे राग के लिए {INS('upanissaya')} होता है",
    "paññāya": "प्रज्ञा के लिए",
    "senāsanaṃ uddhaccasahagatānaṃ khandhānaṃ mohassa ca upanissayapaccayena paccayo":
        f"निवास-स्थान {US} समूहों के लिए और मोह के लिए {INS('upanissaya')} होते हैं",
    "novigatapaccayena paccayo": f"{S.NNAME_OBL('vigata')} के रूप में कारण होती है",
    "nadassanena pahātabbo dhammo nadassanena pahātabbassa dhammassa":
        "सत्य-दर्शन से न छोड़ी जाने वाली परिघटना, सत्य-दर्शन से न छोड़ी जाने वाली परिघटना के लिए",
    "bhāvanāya pahātabbo dhammo nabhāvanāya pahātabbassa dhammassa":
        "मानसिक अभ्यास से छोड़ी जाने वाली परिघटना, मानसिक अभ्यास से न छोड़ी जाने वाली परिघटना के लिए",
    "vitakkaṃ paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{VIT} पर निर्भर होकर {CSR}",
    "vitakkaṃ paṭicca kaṭattārūpaṃ": f"{VIT} पर निर्भर होकर {S.KTR}",
    "vitakkaṃ paṭicca vatthu": f"{VIT} पर निर्भर होकर आधार",
    "vatthuṃ paṭicca vitakko": f"आधार पर निर्भर होकर {VIT}",
    "vitakkaṃ paṭicca sampayuttakā khandhā": f"{VIT} पर निर्भर होकर {SAMP}",
    "vitakkaṃ paṭicca sampayuttakā khandhā cittasamuṭṭhānañca rūpaṃ": f"{VIT} पर निर्भर होकर {SAMP} और {CSR}",
    "vitakkaṃ paṭicca sampayuttakā khandhā kaṭattā ca rūpaṃ": f"{VIT} पर निर्भर होकर {SAMP} और {S.KTR}",
    "mahābhūte paṭicca kaṭattārūpaṃ": f"महाभूतों पर निर्भर होकर {S.KTR}",
    "vatthuṃ paṭicca vitakko sampayuttakā ca khandhā": f"आधार पर निर्भर होकर {VIT} और {SAMP}",
    "vitakkaṃ paṭicca vicikicchāsahagato uddhaccasahagato moho": f"{VIT} पर निर्भर होकर {VU_MOHA}",
    "vicikicchāsahagate uddhaccasahagate khandhe ca vitakkañca paṭicca vicikicchāsahagato uddhaccasahagato moho":
        f"{VU_KH} और {VIT} पर निर्भर होकर {VU_MOHA}",
})
PAREN.update({
    "saṃkhittaṃ.": "संक्षिप्त।",
    "sahajātavāro paṭiccavārasadiso.": "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है।",
    "paṭiccasadisaṃ, saṃkhittaṃ": "निर्भरता के खंड के समान, संक्षिप्त",
    "sampayuttavāro saṃsaṭṭhavārasadiso.": "जुड़ाव का खंड घुले-मिले होने के खंड के समान है।",
    "avasesesu dvīsu anantarūpanissayo, pakatūpanissayo.": f"बाकी दो में {S.ANANTARUPANISSAYA}, {S.PAKATUPANISSAYA}।",
    "saṃkhittaṃ. Vatthupurejātaṃ saṃkhittaṃ.": f"संक्षिप्त। {S.VATTHUPUREJATA} संक्षिप्त।",
    "vatthupurejātaṃ saṃkhittaṃ.": f"{S.VATTHUPUREJATA} संक्षिप्त।",
    "evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi dassanena pahātabbahetukadukasadisā. Uddhaccasahagato moho vicikicchāsahagatamohaṭṭhāne ṭhapetabbo.":
        f"इसी तरह निर्भरता का खंड भी, सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, घुले-मिले होने का खंड भी और जुड़ाव का खंड भी {DHO} के समान हैं। {VS} मोह के स्थान पर {U_MOHA} रखना चाहिए।",
    "dassanena pahātabbahetukadukasadisā": f"{DHO} के समान",
    "ārabbha dassanena pahātabbahetukadukasadisā": f"विषय बनाने वाला भाग {DHO} के समान",
    "ghaṭanārammaṇā tīṇipi kātabbā": "संयुक्त पदों वाले विषय-कारण के भी तीनों तैयार करने चाहिए",
    "anantarapaccaye {N:akāraṇā} vicikicchāsahagato moho na kātabbo, uddhaccasahagato moho kātabbo.":
        f"निकटता-कारण में {{Nm}} पद के कारण {V_MOHA} नहीं लेना चाहिए, {U_MOHA} लेना चाहिए।",
    "ghaṭanūpanissayāpi tīṇipi kātabbā": "संयुक्त पदों वाले प्रबल आश्रय के भी तीनों तैयार करने चाहिए",
    "nabhāvanāya pahātabbabhājanakāraṇe nānākkhaṇikā labbhati ":
        "मानसिक अभ्यास से न छोड़े जाने वाले के विभाजन के कारण भिन्न क्षण रूपी मिलता है ",
    "saṃkhittaṃ. Yathā dassanena pahātabbahetukadukaṃ evaṃ {P:apaccayāpi} paccanīyāpi vibhāgopi gaṇanāpi ninnānākaraṇā.":
        "संक्षिप्त। जैसे सत्य-दर्शन से छोड़े जाने वाले मूलों वाला दो का वर्गीकरण, वैसे ही {Pm} पद के कारण भी, नकारात्मक क्रम भी, विभाजन भी और गणना भी, बिना किसी भिन्नता के।",
    "parantena sakabhaṇḍachandarāgopi kātabbo.": "अंत में अपनी वस्तुओं के प्रति चाह भरा राग भी लेना चाहिए।",
    'parantena "sakabhaṇḍachandarāgo"ti kātabbaṃ.': "अंत में “अपनी वस्तुओं के प्रति चाह भरा राग” लेना चाहिए।",
    "{P:amūlakā} avasesā dve pañhā kātabbā, ahetukaṃ ninnānaṃ.":
        "{Pm} पद से शुरू होने वाले बाकी दो प्रश्न तैयार करने चाहिए, मूल से रहित, बिना किसी भिन्नता के।",
    'saṃkhittaṃ. Hetupaccayasadisaṃ. "Ahetuka"nti niyāmetabbaṃ.':
        "संक्षिप्त। मूल-कारण के समान। “मूल से रहित” इस प्रकार निर्दिष्ट करना चाहिए।",
    "avasesā dve pañhā hetupaccayasadisā ninnānā, ahetukanti niyāmetabbaṃ.":
        "बाकी दो प्रश्न मूल-कारण के समान हैं, बिना किसी भिन्नता के, मूल से रहित ऐसा निर्दिष्ट करना चाहिए।",
    "paṭiccavārasadisā": "निर्भरता के खंड के समान",
})
_TC = {"o": "nom", "": "nom", "ā": "nom", "aṃ": "acc", "ṃ": "acc", "assa": "dat", "yā": "dat", "āya": "dat"}


def _tsub(m):
    end, ca = m.group(1), False
    if end.endswith("ñca"):
        end, ca = end[:-3] + "ṃ", True
    return "{T:" + _TC.get(end, end) + "}" + (" ca" if ca else "")


def T_FORM(table, stem, hindi):
    """Re-register entries written with a concrete third term (vitakka) in the generic {T:..} form."""
    for k in list(table):
        if re.search(r"\b" + stem, k):
            k2 = re.sub(r"\b" + stem + r"(\w*)", _tsub, k)
            table.setdefault(k2, table[k].replace(hindi, "{T}"))


def PN2(k, v):
    for _a in "PN":
        for _b in "PN":
            G[k.replace("{X:", "{" + _a + ":").replace("{Y:", "{" + _b + ":")] = \
                v.replace("{X", "{" + _a).replace("{Y", "{" + _b)


PREFIX.append(("ahetuke {", S.AHETUKA + ", {"))
G["āvajjanāya ārammaṇapaccayena paccayo"] = f"{AV} {INS('ārammaṇa')} {{VB}}"
VSV = "आरंभिक विचार वाले दो के वर्गीकरण"
CUTI, UPAP, BHAV = "मृत्यु-क्षण का मन", "जन्म-क्षण के मन", "जीवन-प्रवाह"
PARI = "का प्रारंभिक अभ्यास"
for _k, _v in {
    "ariyā {X:ā} jhānā vuṭṭhahitvā {Y:aṃ} jhānaṃ paccavekkhanti": f"आर्य {{Xm}} ध्यान से उठकर {{Ym}} ध्यान पर {REVP}",
    "{X:aṃ} cuticittaṃ {Y:assa} upapatticittassa anantarapaccayena paccayo": f"{{Xms}} {CUTI} {{Ym}} {UPAP} के लिए {INS('anantara')} होता है",
    "{X:aṃ} cuticittaṃ {Y:assa} upapatticittassa": f"{{Xms}} {CUTI} {{Ym}} {UPAP} के लिए",
    "{X:aṃ} cuticittañca {T:nom} ca {Y:assa} upapatticittassa": f"{{Xms}} {CUTI} और {{T}} {{Ym}} {UPAP} के लिए",
    "{X:ā} khandhā {Y:assa} vuṭṭhānassa": "{Xm} समूह {Ym} बाहर आने के लिए",
    "{X:ā} khandhā ca {T:nom} ca {Y:assa} vuṭṭhānassa": "{Xm} समूह और {T} {Ym} बाहर आने के लिए",
    "{X:aṃ} bhavaṅgaṃ {Y:assa} bhavaṅgassa": f"{{Xms}} {BHAV} {{Ym}} {BHAV} के लिए",
    "{X:aṃ} bhavaṅgañca {T:nom} ca {Y:assa} bhavaṅgassa": f"{{Xms}} {BHAV} और {{T}} {{Ym}} {BHAV} के लिए",
    "{X:aṃ} kusalākusalaṃ {Y:assa} vuṭṭhānassa": "{Xms} हितकर या हानिकर मन {Ym} बाहर आने के लिए",
    "{X:aṃ} kusalākusalañca {T:nom} ca {Y:assa} vuṭṭhānassa": "{Xms} हितकर या हानिकर मन और {T} {Ym} बाहर आने के लिए",
    "{X:aṃ} saddhaṃ upanissāya {Y:aṃ} jhānaṃ uppādeti": "{Xf} श्रद्धा के प्रबल आश्रय से {Yms} ध्यान उत्पन्न करता है",
    "senāsanaṃ {T:acc} upanissāya {Y:aṃ} jhānaṃ uppādeti": "निवास-स्थान, {T} के प्रबल आश्रय से {Yms} ध्यान उत्पन्न करता है",
    "{X:aṃ} saddhaṃ upanissāya {Y:ena} cittena dānaṃ deti": "{Xf} श्रद्धा के प्रबल आश्रय से {Ym} मन से दान देता है",
    "ariyā {X:ena} cittena {Y:e} pahīne kilese": "आर्य {Xm} मन से {Ym} छोड़े जा चुके मन के क्लेशों पर",
    "ariyā {X:ena} cittena {Y:e} pahīne kilese paccavekkhanti": f"आर्य {{Xm}} मन से {{Ym}} छोड़े जा चुके मन के क्लेशों पर {REVP}",
    "vatthuṃ {Y:e} khandhe ca {T:acc} ca {X:ena} cittena aniccato": "आधार को, {Ym} समूहों और {T} को {Xm} मन से अनित्य",
    "vatthuṃ {Y:e} khandhe ca {T:acc} ca {X:ena} cittena garuṃ katvā assādeti abhinandati":
        f"आधार को, {{Ym}} समूहों और {{T}} को {{Xm}} मन से महत्व देकर {ASSADA_PL}",
    "diṭṭhi uppajjati {X:e} khandhe ca {T:acc} ca garuṃ katvā {Y:ā} khandhā ca {T:nom} ca uppajjanti":
        "दृष्टि उत्पन्न होती है, {Xm} समूहों और {T} को महत्व देकर {Ym} समूह और {T} उत्पन्न होते हैं",
}.items():
    PN2(_k, _v)
for _k, _v in {
    "vatthuṃ {X:e} khandhe ca {T:acc} ca aniccato": "आधार को, {Xm} समूहों और {T} को अनित्य",
    "{X:ā} khandhā iddhividhañāṇassa": f"{{Xm}} समूह {S.IDDHIVIDHA_OBL} के लिए",
    "{X:ā} khandhā iddhividhañāṇassa cetopariyañāṇassa": f"{{Xm}} समूह {S.IDDHIVIDHA_OBL} के लिए, {S.CETOPARIYA_OBL} के लिए",
    "ariyā {X:ā} jhānā vuṭṭhahitvā": "आर्य {Xm} ध्यान से उठकर",
    "{X:ā} jhānā vuṭṭhahitvā": "{Xm} ध्यान से उठकर", "{X:ā} jhānā": "{Xm} ध्यान से",
    "{X:assa} maggassa": "{Xm} मार्ग के लिए",
    "nibbānaṃ {X:assa} maggassa": "निर्वाण {Xm} मार्ग के लिए",
    "nibbānaṃ {X:assa} gotrabhussa": f"निर्वाण {{Xm}} {S.GOTRABHU} के लिए",
    "vatthuṃ {X:e} khandhe ca {T:acc} ca garuṃ katvā assādeti abhinandati": f"आधार को, {{Xm}} समूहों और {{T}} को महत्व देकर {ASSADA_PL}",
    "gotrabhu {X:assa} maggassa": f"{S.GOTRABHU} {{Xm}} मार्ग के लिए",
    "vodānaṃ {X:assa} maggassa": f"{S.VODANA} {{Xm}} मार्ग के लिए",
    "anulomaṃ {X:āya} phalasamāpattiyā anantarapaccayena paccayo": f"अनुकूलता {{Xf}} फल की ध्यान-अवस्था के लिए {INS('anantara')} होती है",
    "{X:o} maggo {X:assa} phalassa": "{Xms} मार्ग {Xm} फल के लिए",
    "{X:aṃ} phalaṃ {X:assa} phalassa": "{Xms} फल {Xm} फल के लिए",
    "nirodhā vuṭṭhahantassa nevasaññānāsaññāyatanaṃ {X:āya} phalasamāpattiyā anantarapaccayena paccayo":
        f"निरोध से उठने वाले व्यक्ति में न पहचान न अ-पहचान का क्षेत्र {{Xf}} फल की ध्यान-अवस्था के लिए {INS('anantara')} होता है",
    "{X:aṃ} bhavaṅgaṃ āvajjanāya": f"{{Xms}} {BHAV} {AV}",
    "{X:aṃ} bhavaṅgañca {T:nom} ca āvajjanāya": f"{{Xms}} {BHAV} और {{T}} {AV}",
    "anulomañca {T:nom} ca {X:āya} phalasamāpattiyā anantarapaccayena paccayo":
        f"अनुकूलता और {{T}} {{Xf}} फल की ध्यान-अवस्था के लिए {INS('anantara')} होते हैं",
    "{X:aṃ} sīlaṃ": "{Xms} सदाचार", "{X:ā} saddhā": "{Xf} श्रद्धा",
    "senāsanaṃ {T:nom} ca {X:āya} saddhāya": "निवास-स्थान और {T} {Xf} श्रद्धा के लिए",
    "{X:aṃ} saddhaṃ upanissāya dānaṃ deti": "{Xf} श्रद्धा के प्रबल आश्रय से दान देता है",
    "{X:aṃ} jhānaṃ uppādeti": "{Xms} ध्यान उत्पन्न करता है", "{X:aṃ} jhānaṃ": "{Xms} ध्यान",
    "patthanāya {X:assa} maggassa": "कामना के लिए, {Xm} मार्ग के लिए",
    "{X:ā} khandhā ca {T:nom} ca purejātassa imassa kāyassa atthipaccayena paccayo":
        f"{{Xm}} समूह और {{T}} पहले उत्पन्न इस शरीर के लिए {INS('atthi')} होते हैं",
    "{X:ā} khandhā ca {T:nom} ca kabaḷīkāro āhāro ca imassa kāyassa atthipaccayena paccayo":
        f"{{Xm}} समूह, {{T}} और कौर-कौर खाया जाने वाला भोजन इस शरीर के लिए {INS('atthi')} होते हैं",
    "{X:ā} khandhā ca {T:nom} ca rūpajīvitindriyañca kaṭattārūpānaṃ atthipaccayena paccayo":
        f"{{Xm}} समूह, {{T}} और {S.RUPAJIVITINDRIYA} {KTRF} {INS('atthi')} होते हैं",
    "{X:e} khandhe ca {T:acc} ca paccayā cittasamuṭṭhānaṃ rūpaṃ": f"{{Xm}} समूहों और {{T}} के कारण {CSR}",
    "{X:aṃ} ekaṃ khandhañca {T:acc} ca vatthuñca paccayā tayo khandhā": "{Xm} एक समूह, {T} और आधार के कारण तीन समूह",
    "{X:e} khandhe saṃsaṭṭho {T:nom}": "{Xm} समूहों से घुल-मिलकर {T}",
    "{X:aṃ} ekaṃ khandhaṃ saṃsaṭṭhā tayo khandhā {T:nom} ca": "{Xm} एक समूह से घुल-मिलकर तीन समूह और {T}",
    "{X:e} khandhe paṭicca {T:nom} ca cittasamuṭṭhānañca rūpaṃ": f"{{Xm}} समूहों पर निर्भर होकर {{T}} और {CSR}",
    "{X:aṃ} ekaṃ khandhaṃ paṭicca tayo khandhā {T:nom} ca cittasamuṭṭhānañca rūpaṃ":
        f"{{Xm}} एक समूह पर निर्भर होकर तीन समूह, {{T}} और {CSR}",
    "{T:acc} paṭicca {X:ā} khandhā cittasamuṭṭhānañca rūpaṃ": f"{{T}} पर निर्भर होकर {{Xm}} समूह और {CSR}",
    "{X:e} khandhe ca {T:acc} ca paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{{Xm}} समूहों और {{T}} पर निर्भर होकर {CSR}",
    "{X:e} khandhe ca mahābhūte ca paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{{Xm}} समूहों और महाभूतों पर निर्भर होकर {CSR}",
    "{X:aṃ} ekaṃ khandhañca {T:acc} ca paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"{{Xm}} एक समूह और {{T}} पर निर्भर होकर तीन समूह और {CSR}",
    "vatthuṃ paccayā ahetukā {X:ā} khandhā {T:nom} ca": f"आधार के कारण {S.AHETUKA}, {{Xm}} समूह और {{T}}",
    "{X:ena} cittena dānaṃ datvā sīlaṃ": "{Xm} मन से दान देकर, सदाचार",
    "{X:ena} cittena dānaṃ": "{Xm} मन से दान",
    "uposathakammaṃ katvā {X:ena} cittena paccavekkhati": f"उपवास-व्रत का पालन करके {{Xm}} मन से उस पर {REV}",
    "phalā vuṭṭhahitvā {X:ena} cittena phalaṃ paccavekkhati": f"फल से उठकर {{Xm}} मन से फल पर {REV}",
    "phalā vuṭṭhahitvā {X:ena} cittena phalaṃ garuṃ katvā paccavekkhati": f"फल से उठकर {{Xm}} मन से फल को महत्व देकर उस पर {REV}",
    "ariyā {X:ena} cittena nibbānaṃ paccavekkhanti": f"आर्य {{Xm}} मन से निर्वाण पर {REVP}",
    "ariyā {X:ena} cittena nibbānaṃ garuṃ katvā paccavekkhanti": f"आर्य {{Xm}} मन से निर्वाण को महत्व देकर उस पर {REVP}",
    "{X:ena} cittena paccavekkhati assādeti abhinandati": f"{{Xm}} मन से उस पर {REV}, {ASSADA}",
    "{X:ena} cittena taṃ garuṃ katvā paccavekkhati assādeti abhinandati": f"{{Xm}} मन से उसे महत्व देकर उस पर {REV}, {ASSADA}",
    "{X:ā} vipākamanoviññāṇadhātu ca {T:nom} ca kiriyamanoviññāṇadhātuyā":
        f"{{Xms}} कर्म-फल रूपी {S.MVD} और {{T}} केवल क्रिया रूपी {S.MVD_OBL} के लिए",
    "vipākamanodhātu {X:āya} vipākamanoviññāṇadhātuyā": f"कर्म-फल रूपी {S.MANODHATU} {{Xm}} कर्म-फल रूपी {S.MVD_OBL} के लिए",
    "āvajjanā {X:ānaṃ} khandhānaṃ": "मन को विषय की ओर मोड़ना {Xm} समूहों के लिए",
    "{X:āya} phalasamāpattiyā {T:dat} ca anantarapaccayena paccayo": f"{{Xf}} फल की ध्यान-अवस्था के लिए और {{T}} के लिए {INS('anantara')} होता है",
    "{T:acc} upanissāya {X:ena} cittena dānaṃ deti": "{T} के प्रबल आश्रय से {Xm} मन से दान देता है",
    "senāsanaṃ {T:acc} upanissāya {X:ena} cittena dānaṃ deti": "निवास-स्थान, {T} के प्रबल आश्रय से {Xm} मन से दान देता है",
    "{X:ena} cittena adinnaṃ ādiyati": "{Xm} मन से बिना दिया हुआ लेता है",
    "vatthuṃ {X:ena} cittena aniccato": "आधार को {Xm} मन से अनित्य",
}.items():
    PN(_k, _v)
G.update({
    "ekaṃ mahābhūtaṃ paccayā tayo mahābhūtā": "एक महाभूत के कारण तीन महाभूत",
    "maggā vuṭṭhahitvā maggaṃ paccavekkhanti": f"मार्ग से उठकर मार्ग पर {REVP}",
    "phalā vuṭṭhahitvā phalaṃ paccavekkhanti": f"फल से उठकर फल पर {REVP}",
    "nibbānaṃ paccavekkhanti": f"निर्वाण पर {REVP}",
    "{T:dat} ca ārammaṇapaccayena paccayo": f"और {{T}} के लिए {INS('ārammaṇa')} {{VB}}",
    "{T:dat} ca adhipatipaccayena paccayo": f"और {{T}} के लिए {INS('adhipati')} {{VB}}",
    "mohassa ca ārammaṇapaccayena paccayo": f"और मोह के लिए {INS('ārammaṇa')} {{VB}}",
    "āvajjanāya {T:dat} ca ārammaṇapaccayena paccayo": f"{AV} और {{T}} के लिए {INS('ārammaṇa')} {{VB}}",
    "ākāsānañcāyatanaṃ": S.ARUPA_AYATANA["ākāsānañca"], "ākiñcaññāyatanaṃ": S.ARUPA_AYATANA["ākiñcañña"],
    "phoṭṭhabbāyatanaṃ": S.AYA_OBJ("phoṭṭhabba"),
    "pubbenivāsānussatiñāṇassa yathākammūpagañāṇassa": f"{S.PUBBENIVASA_OBL} के लिए, {S.YATHAKAMMUPAGA_OBL} के लिए",
    "maggā vuṭṭhahitvā": "मार्ग से उठकर", "maggā": "मार्ग से",
    "nibbānaṃ gotrabhussa": f"निर्वाण {S.GOTRABHU} के लिए", "vodānassa": f"{S.VODANA} के लिए",
    "phalā vuṭṭhahitvā phalaṃ garuṃ katvā paccavekkhanti": f"फल से उठकर फल को महत्व देकर उस पर {REVP}",
    "nibbānaṃ garuṃ katvā paccavekkhanti": f"निर्वाण को महत्व देकर उस पर {REVP}",
    "āvajjanā pañcannaṃ viññāṇānaṃ anantarapaccayena paccayo": f"मन को विषय की ओर मोड़ना पाँच प्रकार की चेतनाओं के लिए {INS('anantara')} होता है",
    "āvajjanā ca {T:nom} ca pañcannaṃ viññāṇānaṃ": "मन को विषय की ओर मोड़ना और {T} पाँच प्रकार की चेतनाओं के लिए",
    "dutiyassa jhānassa parikammaṃ dutiyassa jhānassa anantarapaccayena paccayo":
        f"दूसरे ध्यान {PARI} दूसरे ध्यान के लिए {INS('anantara')} होता है",
    "dutiyassa jhānassa parikammañca {T:nom} ca": f"दूसरे ध्यान {PARI} और {{T}}",
    "tatiyassa jhānassa parikammaṃ": f"तीसरे ध्यान {PARI}",
    "nevasaññānāsaññāyatanassa parikammaṃ nevasaññānāsaññāyatanassa":
        f"{S.ARUPA_OBL('nevasaññānāsañña')} {PARI} {S.ARUPA_OBL('nevasaññānāsañña')} के लिए",
    "dibbassa cakkhussa parikammaṃ": f"दिव्य आँख {PARI}",
    "dibbāya sotadhātuyā parikammaṃ": f"दिव्य कान के तत्व {PARI}",
    "iddhividhañāṇassa parikammaṃ": f"{S.IDDHIVIDHA_OBL} {PARI}",
    "cetopariyañāṇassa parikammaṃ": f"{S.CETOPARIYA_OBL} {PARI}",
    "pubbenivāsānussatiñāṇassa parikammaṃ": f"{S.PUBBENIVASA_OBL} {PARI}",
    "yathākammūpagañāṇassa parikammaṃ yathākammūpagañāṇassa": f"{S.YATHAKAMMUPAGA_OBL} {PARI} {S.YATHAKAMMUPAGA_OBL} के लिए",
    "anāgataṃsañāṇassa parikammaṃ anāgataṃsañāṇassa anantarapaccayena paccayo":
        f"{S.ANAGATAMSA_OBL} {PARI} {S.ANAGATAMSA_OBL} के लिए {INS('anantara')} होता है",
    "maggaṃ uppādeti": "मार्ग उत्पन्न करता है", "abhiññaṃ uppādeti": "उच्च ज्ञान उत्पन्न करता है",
    "maggaṃ": "मार्ग", "abhiññaṃ": "उच्च ज्ञान", "vipassanaṃ": "अंतर्दृष्टि",
    "sīlaṃ samādiyati": "सदाचार ग्रहण करता है", "uposathakammaṃ karoti": "उपवास-व्रत का पालन करता है",
    "senāsanaṃ {T:acc} upanissāya dānaṃ deti": "निवास-स्थान, {T} के प्रबल आश्रय से दान देता है",
    "phalasamāpattiyā {T:dat} ca upanissayapaccayena paccayo": f"फल की ध्यान-अवस्था के लिए और {{T}} के लिए {INS('upanissaya')} होते हैं",
    "maggassa phalasamāpattiyā {T:dat} ca upanissayapaccayena paccayo":
        f"मार्ग के लिए, फल की ध्यान-अवस्था के लिए और {{T}} के लिए {INS('upanissaya')} होते हैं",
    "dve khandhe paṭicca dve khandhā kaṭattā ca rūpaṃ": f"दो समूहों पर निर्भर होकर दो समूह और {S.KTR}",
    "phoṭṭhabbāyatanaṃ kāyaviññāṇassa ārammaṇapaccayena paccayo": f"{S.AYA_OBJ('phoṭṭhabba')} शरीर की चेतना के लिए {INS('ārammaṇa')} होता है",
    "phalassa ārammaṇapaccayena paccayo": f"फल के लिए {INS('ārammaṇa')} होता है",
    "{T:sahagatā} vipākamanoviññāṇadhātu kiriyamanoviññāṇadhātuyā":
        f"{{T}} के साथ होने वाला कर्म-फल रूपी {S.MVD} केवल क्रिया रूपी {S.MVD_OBL} के लिए",
    "kiriyaṃ vuṭṭhānassa": "केवल क्रिया रूपी मन बाहर आने के लिए",
    "kiriyañca {T:nom} ca vuṭṭhānassa": "केवल क्रिया रूपी मन और {T} बाहर आने के लिए",
    "phalaṃ vuṭṭhānassa anantarapaccayena paccayo": f"फल बाहर आने के लिए {INS('anantara')} होता है",
    "phalañca {T:nom} ca vuṭṭhānassa anantarapaccayena paccayo": f"फल और {{T}} बाहर आने के लिए {INS('anantara')} होते हैं",
    "musā": "झूठ", "pisuṇaṃ": "चुगली", "samphaṃ": "व्यर्थ बकवास", "sandhiṃ": "सेंध", "nillopaṃ": "लूटपाट",
    "ekāgārikaṃ": "एक ही घर में डाका", "paripanthe": "रास्ते में घात", "paradāraṃ": "पराई स्त्री",
    "gāmaghātaṃ": "गाँव पर हमला", "nigamaghātaṃ karoti": "कस्बे पर हमला करता है",
    "paññāya rāgassa": "प्रज्ञा के लिए, राग के लिए",
    "{T:nom} uppajjati": "{T} उत्पन्न होता है",
})
PAREN.update({
    "paṭisandhiyāpi dve": "पुनर्जन्म में भी दो",
    "paṭisandhiyāpi pavattisadisāyeva": "पुनर्जन्म में भी जीवन-काल के समान ही",
    "paṭisandhikkhaṇe dve kātabbā": "पुनर्जन्म के क्षण में दो तैयार करने चाहिए",
    "tīṇi, paṭisandhiyāpi": "तीन, पुनर्जन्म में भी",
    'nava pañhā kātabbā. "Ahetukā"ti niyāmetabbā tīṇiyeva. Moho uddharitabbo, yathā paṭiccavāre hetupaccayasadisāyeva pañhā pañcaviññāṇā atirekā moho {T:acc}.':
        "नौ प्रश्न तैयार करने चाहिए। “मूल से रहित” ऐसा केवल तीन में निर्दिष्ट करना चाहिए। मोह को अलग करके लेना चाहिए, जैसे निर्भरता के खंड में, मूल-कारण के समान ही प्रश्न, पाँच प्रकार की चेतना अतिरिक्त, मोह, {T}।",
    "evaṃ cha pañhā kātabbā anulomasadisā, ahetukāti niyāmetabbā, tīṇiyeva, moho uddharitabbo.":
        "इसी तरह छह प्रश्न सकारात्मक क्रम के समान तैयार करने चाहिए, मूल से रहित ऐसा निर्दिष्ट करना चाहिए, केवल तीन में, मोह को अलग करके लेना चाहिए।",
    "heṭṭhā likhitaṃ lekhaṃ iminā kāraṇena daṭṭhabbaṃ": "पहले लिखे गए पाठ को इसी तरीके से समझना चाहिए",
    "tīṇipi upanissayā sabbattha kātabbā": "तीनों प्रबल आश्रय हर जगह लेने चाहिए",
    "dutiyavāre likhitapadā sabbe kātabbā": "दूसरे खंड में लिखे गए सभी पद लेने चाहिए",
    "tīṇi, pacchājātā": "तीन, पश्चात्-उत्पत्ति रूपी",
    "evaṃ cattāri, sahajātāpi nānākkhaṇikāpi kātabbā.": "इसी तरह चार, सह-उत्पत्ति रूपी भी और भिन्न क्षण रूपी भी तैयार करने चाहिए।",
    "ekaṃ, paṭiccasadisaṃ": "एक, निर्भरता के खंड के समान",
    "paṭisandhikkhaṇe sahajātāpi dvepi kātabbā": "पुनर्जन्म के क्षण में सह-उत्पत्ति रूपी दोनों भी तैयार करने चाहिए",
    "paṭisandhikkhaṇe, tīṇi": "पुनर्जन्म के क्षण में, तीन",
    "anulomamātikā vitthāretabbā": "सकारात्मक क्रम की मूल सूची का विस्तार करना चाहिए",
    "yathā savitakkadukaṃ, evaṃ kātabbaṃ, ninnānākaraṇaṃ. Idha magge cattāri kātabbāni. {P:aduke} imaṃ nānākaraṇaṃ.":
        "जैसे आरंभिक विचार वाला दो का वर्गीकरण, वैसे ही करना चाहिए, बिना किसी भिन्नता के। यहाँ मार्ग-कारण में चार तैयार करने चाहिए। सतत विचार वाले दो के वर्गीकरण में यह भिन्नता है।",
    "yathā savitakkadukaṃ sabbattha, evaṃ {P:adukaṃ} kātabbaṃ, sabbattha pavattipaṭisandhi navapi pañhā.":
        "जैसे हर जगह आरंभिक विचार वाला दो का वर्गीकरण, वैसे ही उल्लास वाला दो का वर्गीकरण तैयार करना चाहिए, हर जगह जीवन-काल और पुनर्जन्म में नौ के नौ प्रश्न।",
    "yāva asaññasattāpi": "पहचान-रहित प्राणियों तक भी",
    "saṃkhittaṃ. Yathā savitakkaduke anulomapaccayavāraṃ, evaṃ pavattipaṭisandhi nava pañhā paripuṇṇā {T:nom} ninnānākaraṇā.":
        f"संक्षिप्त। जैसे {VSV} में सकारात्मक क्रम का कारण का खंड, वैसे ही जीवन-काल और पुनर्जन्म में नौ प्रश्न पूरे हैं, {{T}} बिना किसी भिन्नता के।",
    "pavattipaṭisandhi kātabbā paṭiccavārasadisā, yāva asaññasattā.":
        "जीवन-काल और पुनर्जन्म निर्भरता के खंड के समान तैयार करने चाहिए, पहचान-रहित प्राणियों तक।",
    "anulomasadisā nava pañhā, pavattiyeva paṭisandhi natthi, ekoyeva moho.":
        "सकारात्मक क्रम के समान नौ प्रश्न, केवल जीवन-काल में, पुनर्जन्म नहीं है, मोह एक ही है।",
    "tīṇi upanissayā": "तीनों प्रबल आश्रय", "tīṇipi upanissayā": "तीनों प्रबल आश्रय",
    "dutiyavārasadisaṃ": "दूसरे खंड के समान",
    "sahajātāpi nānākkhaṇikāpi kātabbā… dve nānākkhaṇikā": "सह-उत्पत्ति रूपी भी और भिन्न क्षण रूपी भी तैयार करने चाहिए… दो भिन्न क्षण रूपी",
    "saṃkhittaṃ. Savitakkadukasadisaṃ kātabbaṃ.": f"संक्षिप्त। {VSV} के समान करना चाहिए।",
    "paccanīyavibhaṅgagaṇanāpi savitakkadukasadisā. Yadipi na sameti imaṃ anulomaṃ paccavekkhitvā gaṇetabbaṃ, itare dve gaṇanā gaṇetabbā.":
        f"नकारात्मक क्रम का विश्लेषण और गणना भी {VSV} के समान है। यदि मेल न खाए, तो इस सकारात्मक क्रम की जाँच करके गिनना चाहिए, अन्य दो गणनाएँ गिननी चाहिए।",
    "evaṃ {P:adukaṃ} vitthāretabbaṃ, sappītikadukasadisaṃ ninnānākaraṇaṃ, āmasanaṃ ninnānaṃ.":
        "इसी तरह उल्लास के साथ होने वाले दो के वर्गीकरण का विस्तार करना चाहिए, उल्लास वाले दो के वर्गीकरण के समान, बिना किसी भिन्नता के, उल्लेख भी अलग नहीं।",
})
PREFIX += [("vipākaṃ {", "कर्म के फल रूपी, {"), ("vipāke {", "कर्म के फल रूपी, {")]
SPD = "उल्लास वाले दो के वर्गीकरण"
MVDV = f"कर्म-फल रूपी {S.MVD}"
G["anāgataṃsañāṇassa ārammaṇapaccayena paccayo"] = f"{S.ANAGATAMSA_OBL} के लिए {INS('ārammaṇa')} होते हैं"
for _k, _v in {
    "{X:aṃ} ekaṃ khandhaṃ paṭicca dve khandhā": "{Xm} एक समूह पर निर्भर होकर दो समूह",
    "{X:e} khandhe paṭicca {T:nom} cittasamuṭṭhānañca rūpaṃ": f"{{Xm}} समूहों पर निर्भर होकर {{T}} और {CSR}",
    "{X:aṃ} ekaṃ khandhaṃ paṭicca dve khandhā {T:nom} ca cittasamuṭṭhānañca rūpaṃ": f"{{Xm}} एक समूह पर निर्भर होकर दो समूह, {{T}} और {CSR}",
    "{X:aṃ} kāyaviññāṇaṃ vipākamanodhātuyā": f"{{Xf}} शरीर की चेतना कर्म-फल रूपी {S.MANODHATU_OBL} के लिए",
    "{X:aṃ} kāyaviññāṇañca {T:nom} ca vipākamanodhātuyā": f"{{Xf}} शरीर की चेतना और {{T}} कर्म-फल रूपी {S.MANODHATU_OBL} के लिए",
    "{X:ā} vipākamanoviññāṇadhātu kiriyamanoviññāṇadhātuyā": f"{{Xms}} {MVDV} केवल क्रिया रूपी {S.MVD_OBL} के लिए",
    "purimā purimā {X:ā}": "पहले-पहले के {Xm}",
    "senāsanaṃ {T:nom} ca {X:āya}": "निवास-स्थान और {T} {Xf}",
    "vicikicchāsahagataṃ uddhaccasahagataṃ {T:nom} paṭicca vicikicchāsahagato uddhaccasahagato moho": "",
    "{X:aṃ} ekaṃ khandhañca {T:nom} ca paṭicca dve khandhā": "{Xm} एक समूह और {T} पर निर्भर होकर दो समूह",
    "{X:aṃ} ekaṃ khandhañca vatthuñca paṭicca dve khandhā": "{Xm} एक समूह और आधार पर निर्भर होकर दो समूह",
    "{X:e} khandhe ca {T:nom} ca paṭicca kaṭattārūpaṃ": f"{{Xm}} समूहों और {{T}} पर निर्भर होकर {S.KTR}",
    "{X:e} khandhe ca mahābhūte ca paṭicca kaṭattārūpaṃ": f"{{Xm}} समूहों और महाभूतों पर निर्भर होकर {S.KTR}",
    "{X:e} khandhe paṭicca kaṭattārūpaṃ": f"{{Xm}} समूहों पर निर्भर होकर {S.KTR}",
    "{X:aṃ} ekaṃ khandhañca {T:nom} ca paṭicca dve khandhā cittasamuṭṭhānañca rūpaṃ": f"{{Xm}} एक समूह और {{T}} पर निर्भर होकर दो समूह और {CSR}",
    "{X:aṃ} ekaṃ khandhañca {T:nom} ca paṭicca dve khandhā kaṭattā ca rūpaṃ": f"{{Xm}} एक समूह और {{T}} पर निर्भर होकर दो समूह और {S.KTR}",
    "{X:aṃ} ekaṃ khandhañca vatthuñca paṭicca dve khandhā {T:nom} ca": "{Xm} एक समूह और आधार पर निर्भर होकर दो समूह और {T}",
    "āvajjanā ca {T:nom} ca {X:ānaṃ} khandhānaṃ": "मन को विषय की ओर मोड़ना और {T} {Xm} समूहों के लिए",
    "vipākamanodhātu ca {T:nom} ca {X:āya} vipākamanoviññāṇadhātuyā": f"कर्म-फल रूपी {S.MANODHATU} और {{T}} {{Xm}} कर्म-फल रूपी {S.MVD_OBL} के लिए",
    "nirodhā vuṭṭhahantassa nevasaññānāsaññāyatanañca {T:nom} ca {X:āya} phalasamāpattiyā anantarapaccayena paccayo":
        f"निरोध से उठने वाले व्यक्ति में न पहचान न अ-पहचान का क्षेत्र और {{T}} {{Xf}} फल की ध्यान-अवस्था के लिए {INS('anantara')} होते हैं",
    "{X:e} khandhe paṭicca {X:ādhipati}": "{Xm} समूहों पर निर्भर होकर {Xf} प्रधानता",
    "vatthuṃ paccayā vipākā {X:ā} khandhā": "आधार के कारण कर्म के फल रूपी, {Xm} समूह",
    "vatthuṃ paccayā {X:ādhipati}": "आधार के कारण {Xf} प्रधानता",
    "{X:e} khandhe ca vatthuñca paccayā {X:ādhipati}": "{Xm} समूहों और आधार के कारण {Xf} प्रधानता",
    "{X:aṃ} ekaṃ khandhaṃ paccayā": "{Xm} एक समूह के कारण",
    "senāsanaṃ {X:āya} saddhāya": "निवास-स्थान {Xf} श्रद्धा के लिए",
    "senāsanaṃ upanissāya {X:aṃ} jhānaṃ uppādeti": "निवास-स्थान के प्रबल आश्रय से {Xms} ध्यान उत्पन्न करता है",
    "{X:aṃ} saddhaṃ upanissāya jhānaṃ uppādeti": "{Xf} श्रद्धा के प्रबल आश्रय से ध्यान उत्पन्न करता है",
    "paññaṃ upanissāya {X:aṃ} jhānaṃ uppādeti": "प्रज्ञा के प्रबल आश्रय से {Xms} ध्यान उत्पन्न करता है",
    "paññā {X:āya} saddhāya": "प्रज्ञा {Xf} श्रद्धा के लिए",
    "{N:e} khandhe garuṃ katvā assādeti abhinandati taṃ garuṃ katvā rāgo uppajjati": "",
}.items():
    PN(_k, _v)
for _s in "PN":
    G[f"vicikicchāsahagataṃ uddhaccasahagataṃ {{T:nom}} paṭicca vicikicchāsahagato uddhaccasahagato moho"] = \
        f"संशय के साथ होने वाले या बेचैनी के साथ होने वाले {{T}} पर निर्भर होकर {VU_MOHA}"
    G[f"{{{_s}:e}} khandhe garuṃ katvā assādeti abhinandati taṃ garuṃ katvā rāgo uppajjati"] = \
        f"{{{_s}m}} समूहों को महत्व देकर {ASSADA_PL}, उसे महत्व देकर राग उत्पन्न होता है"
PN2("{X:aṃ} cuticittañca {T:nom} ca {Y:assa} upapatticittassa {X:aṃ} bhavaṅgañca {T:nom} ca āvajjanāya",
    f"{{Xms}} {CUTI} और {{T}} {{Ym}} {UPAP} के लिए, {{Xms}} {BHAV} और {{T}} {AV}")
G.update({
    "dve khandhe paṭicca eko khandho": "दो समूहों पर निर्भर होकर एक समूह",
    "kāyikaṃ {T:nom}": "शारीरिक {T}", "kāyikassa {T:dat}": "शारीरिक {T} के लिए",
    "maggassa phalasamāpattiyā upanissayapaccayena paccayo": f"मार्ग के लिए, फल की ध्यान-अवस्था के लिए {INS('upanissaya')} होते हैं",
    "saddhāya": "श्रद्धा के लिए",
    "taṃ ārabbha {T:nom} ca sampayuttakā khandhā ca uppajjanti": f"उसे विषय बनाकर {{T}} और {SAMP} उत्पन्न होते हैं",
    "vatthuṃ paṭicca {T:nom} ca sampayuttakā ca khandhā": f"आधार पर निर्भर होकर {{T}} और {SAMP}",
    "phalaṃ vuṭṭhānassa": "फल बाहर आने के लिए",
    "phalañca {T:nom} ca vuṭṭhānassa": "फल और {T} बाहर आने के लिए",
    "anulomaṃ phalasamāpattiyā anantarapaccayena paccayo": f"अनुकूलता फल की ध्यान-अवस्था के लिए {INS('anantara')} होती है",
    "kāyaviññāṇadhātu vipākamanodhātuyā": f"शरीर की चेतना का तत्व कर्म-फल रूपी {S.MANODHATU_OBL} के लिए",
    "musā bhaṇati": "झूठ बोलता है",
    "pubbe suciṇṇāni paccavekkhati assādeti abhinandati": f"{S.SUCINNA} पर {REV}, {ASSADA_PL}",
    "pubbe suciṇṇāni garuṃ katvā paccavekkhati assādeti abhinandati": f"{S.SUCINNA} को महत्व देकर उन पर {REV}, {ASSADA_PL}",
    "pahīne kilese": "छोड़े जा चुके मन के क्लेशों पर",
    "nibbānaṃ maggassa": "निर्वाण मार्ग के लिए",
    "ākāsānañcāyatanaṃ viññāṇañcāyatanassa": f"{S.ARUPA_AYATANA['ākāsānañca']} {S.ARUPA_OBL('viññāṇañca')} के लिए",
    "ākiñcaññāyatanaṃ nevasaññānāsaññāyatanassa": f"{S.ARUPA_AYATANA['ākiñcañña']} {S.ARUPA_OBL('nevasaññānāsañña')} के लिए",
    "ākiñcaññāyatanaṃ nevasaññānāsaññāyatanassa upanissayapaccayena paccayo":
        f"{S.ARUPA_AYATANA['ākiñcañña']} {S.ARUPA_OBL('nevasaññānāsañña')} के लिए {INS('upanissaya')} होता है",
    "phalaṃ": "फल",
    "ākāsānañcāyatanaṃ paccavekkhati": f"{S.ARUPA_OBL('ākāsānañca')} पर {REV}",
    "viññāṇañcāyatanaṃ paccavekkhati": f"{S.ARUPA_OBL('viññāṇañca')} पर {REV}",
    "ākiñcaññāyatanaṃ paccavekkhati": f"{S.ARUPA_OBL('ākiñcañña')} पर {REV}",
    "nevasaññānāsaññāyatanaṃ paccavekkhati": f"{S.ARUPA_OBL('nevasaññānāsañña')} पर {REV}",
    "dibbaṃ cakkhuṃ paccavekkhati": f"दिव्य आँख पर {REV}",
    "dibbaṃ sotadhātuṃ paccavekkhati": f"दिव्य कान के तत्व पर {REV}",
    "iddhividhañāṇaṃ paccavekkhati": f"{S.IDDHIVIDHA_OBL} पर {REV}",
    "cetopariyañāṇaṃ": S.CETOPARIYA, "pubbenivāsānussatiñāṇaṃ": "पूर्व जन्मों के अनुस्मरण का ज्ञान",
    "yathākammūpagañāṇaṃ": "प्राणियों के अपने कर्मों के अनुसार जाने का ज्ञान",
    "anāgataṃsañāṇaṃ paccavekkhati": f"{S.ANAGATAMSA_OBL} पर {REV}",
    "jhānā vuṭṭhahitvā jhānaṃ garuṃ katvā paccavekkhati assādeti abhinandati": f"ध्यान से उठकर ध्यान को महत्व देकर उस पर {REV}, {ASSADA}",
    "vodānassa adhipatipaccayena paccayo": f"{S.VODANA} के लिए {INS('adhipati')} होता है",
    "ākāsānañcāyatanaṃ garuṃ katvā paccavekkhati viññāṇañcāyatanaṃ":
        f"{S.ARUPA_OBL('ākāsānañca')} को महत्व देकर उस पर {REV}, {S.ARUPA_AYATANA['viññāṇañca']}",
    "nevasaññānāsaññāyatanaṃ garuṃ katvā paccavekkhati": f"{S.ARUPA_OBL('nevasaññānāsañña')} को महत्व देकर उस पर {REV}",
    "dibbaṃ cakkhuṃ": "दिव्य आँख", "dibbaṃ sotadhātuṃ": "दिव्य कान का तत्व", "iddhividhañāṇaṃ": "अलौकिक शक्तियों का ज्ञान",
    "anāgataṃsañāṇaṃ garuṃ katvā paccavekkhati": f"{S.ANAGATAMSA_OBL} को महत्व देकर उस पर {REV}",
    "paṭhamassa jhānassa parikammaṃ paṭhamassa jhānassa anantarapaccayena paccayo":
        f"पहले ध्यान {PARI} पहले ध्यान के लिए {INS('anantara')} होता है",
    "paṭhamassa jhānassa parikammaṃ paṭhamassa jhānassa": f"पहले ध्यान {PARI} पहले ध्यान के लिए",
    "catutthassa jhānassa": "चौथे ध्यान के लिए",
    "nevasaññānāsaññāyatanassa parikammaṃ": f"{S.ARUPA_OBL('nevasaññānāsañña')} {PARI}",
    "dibbassa cakkhussa": "दिव्य आँख के लिए", "dibbāya sotadhātuyā": "दिव्य कान के तत्व के लिए",
    "iddhividhañāṇassa": f"{S.IDDHIVIDHA_OBL} के लिए",
    "gotrabhu maggassa": f"{S.GOTRABHU} मार्ग के लिए", "vodānaṃ maggassa": f"{S.VODANA} मार्ग के लिए",
    "maggo phalassa": "मार्ग फल के लिए", "phalaṃ phalassa": "फल फल के लिए",
    "nirodhā vuṭṭhahantassa": "निरोध से उठने वाले व्यक्ति में",
    "nevasaññānāsaññāyatanaṃ phalasamāpattiyā anantarapaccayena paccayo":
        f"{S.ARUPA_AYATANA['nevasaññānāsañña']} फल की ध्यान-अवस्था के लिए {INS('anantara')} होता है",
    "vipassanaṃ uppādeti": "अंतर्दृष्टि उत्पन्न करता है",
    "kāyikassa dukkhassa upanissayapaccayena paccayo": f"शारीरिक दुःख के लिए {INS('upanissaya')} होते हैं",
    "ākāsānañcāyatanassa": f"{S.ARUPA_OBL('ākāsānañca')} के लिए",
    "paṭhamassa maggassa": "पहले मार्ग के लिए",
    "catutthassa maggassa parikammaṃ catutthassa maggassa upanissayapaccayena paccayo":
        f"चौथे मार्ग {PARI} चौथे मार्ग के लिए {INS('upanissaya')} होता है",
    "paṭhamaṃ jhānaṃ dutiyassa jhānassa upanissayapaccayena paccayo": f"पहला ध्यान दूसरे ध्यान के लिए {INS('upanissaya')} होता है",
    "tatiyaṃ jhānaṃ": "तीसरा ध्यान", "catutthaṃ jhānaṃ": "चौथा ध्यान",
    "paṭhamo maggo dutiyassa maggassa": "पहला मार्ग दूसरे मार्ग के लिए",
    "dutiyo maggo tatiyassa maggassa": "दूसरा मार्ग तीसरे मार्ग के लिए",
    "tatiyo maggo catutthassa maggassa upanissayapaccayena paccayo": f"तीसरा मार्ग चौथे मार्ग के लिए {INS('upanissaya')} होता है",
    "maggo phalasamāpattiyā upanissayapaccayena paccayo": f"मार्ग फल की ध्यान-अवस्था के लिए {INS('upanissaya')} होता है",
    "paññaṃ upanissāya dānaṃ deti": "प्रज्ञा के प्रबल आश्रय से दान देता है",
    "patthanāya kāyikassa sukhassa": "कामना के लिए, शारीरिक सुख के लिए",
    "ariyā maggaṃ upanissāya saṅkhāre aniccato": "आर्य मार्ग के प्रबल आश्रय से निर्मित परिघटनाओं को अनित्य",
    "maggo ariyānaṃ atthapaṭisambhidāya": "मार्ग आर्यों के लिए अर्थ के विश्लेषणात्मक ज्ञान के लिए",
    "dhammapaṭisambhidāya": "परिघटनाओं के विश्लेषणात्मक ज्ञान के लिए",
    "niruttipaṭisambhidāya": "भाषा के विश्लेषणात्मक ज्ञान के लिए",
    "paṭibhānapaṭisambhidāya": "सूझ-बूझ के विश्लेषणात्मक ज्ञान के लिए",
    "ṭhānāṭhānakosallassa upanissayapaccayena paccayo": f"संभव और असंभव को जानने की कुशलता के लिए {INS('upanissaya')} होता है",
    "phalasamāpatti kāyikassa sukhassa upanissayapaccayena paccayo": f"फल की ध्यान-अवस्था शारीरिक सुख के लिए {INS('upanissaya')} होती है",
})
PAREN.update({
    "evaṃ {P:adukaṃ} vitthāretabbaṃ, yathā sappītikadukassa anulomapaṭiccavāro.":
        f"इसी तरह सुख के साथ होने वाले दो के वर्गीकरण का विस्तार करना चाहिए, जैसे {SPD} का सकारात्मक क्रम वाला निर्भरता का खंड।",
    "yathā sappītike nahetupaccayasadisaṃ, ninnānaṃ sabbatthameva nava pañhā.":
        "जैसे उल्लास वाले में मूल-कारण के अभाव के समान, बिना भिन्नता के, हर जगह नौ प्रश्न।",
    "evaṃ itare dve gaṇanāpi sahajātavāropi paṭiccavārasadisā. Paccayavāre pavattipi paṭisandhipi vitthāretabbā, yathā sappītikadukapaccayavārapaccanīyepi pavatte vatthu ca vitthāretabbaṃ, yathā sappītikaduke ekoyeva moho, evaṃ itare dve gaṇanāpi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi yathā sappītikadukaṃ, evaṃ kātabbaṃ.":
        f"इसी तरह अन्य दो गणनाएँ भी और सह-उत्पत्ति का खंड भी निर्भरता के खंड के समान हैं। कारण के खंड में जीवन-काल का भी और पुनर्जन्म का भी विस्तार करना चाहिए, जैसे {SPD} के कारण के खंड के नकारात्मक क्रम में भी जीवन-काल में आधार का भी विस्तार करना चाहिए, जैसे {SPD} में मोह एक ही है, वैसे ही अन्य दो गणनाएँ भी, आश्रय का खंड भी, घुले-मिले होने का खंड भी और जुड़ाव का खंड भी, जैसे उल्लास वाला दो का वर्गीकरण, वैसे ही तैयार करना चाहिए।",
    "ārammaṇepi adhipatiyāpi sappītikadukasadisā, {T:anti} nānākaraṇaṃ.":
        f"विषय-कारण में भी और प्रधानता-कारण में भी {SPD} के समान, केवल {{T}} की भिन्नता है।",
    "mūlaṃ. Tīṇipi sappītikadukasadisā.": f"मूल वाक्य। तीनों भी {SPD} के समान।",
    "dutiyagamanasadisaṃ": "दूसरे क्रम के समान",
    "cha kammāni cattāri sahajātāpi nānākkhaṇikāpi kātabbā, dve nānākkhaṇikā.":
        "छह कर्म-कारण वाले प्रश्न, चार सह-उत्पत्ति रूपी भी और भिन्न क्षण रूपी भी तैयार करने चाहिए, दो भिन्न क्षण रूपी।",
    "evaṃ paccanīyavibhaṅgopi gaṇanāpi sappītikadukasadisaṃ kātabbaṃ, yadipi vimati atthi anulomaṃ passitvā gaṇetabbaṃ.":
        f"इसी तरह नकारात्मक क्रम का विश्लेषण भी और गणना भी {SPD} के समान करना चाहिए, यदि संदेह हो तो सकारात्मक क्रम देखकर गिनना चाहिए।",
    "sappītikadukasadisaṃ, anulome navapi pañhā.": f"{SPD} के समान, सकारात्मक क्रम में नौ के नौ प्रश्न।",
    'yathā savitakkadukasadisaṃ paccayavāre nānākaraṇaṃ. "{T:a}"nti navapi pañhā kātabbā, paṭisandhipavattipi vatthupi.':
        f"जैसे {VSV} के समान, कारण के खंड में भिन्नता है। “{{T}}” के साथ नौ के नौ प्रश्न तैयार करने चाहिए, पुनर्जन्म और जीवन-काल भी, आधार भी।",
    "evaṃ navapi pañhā pavattipaṭisandhiyo yathā savitakkadukassa evaṃ kātabbā. Tīṇiyeva moho, pavatte vatthupi kātabbā.":
        f"इसी तरह नौ के नौ प्रश्न, जीवन-काल और पुनर्जन्म, जैसे {VSV} के, वैसे ही तैयार करने चाहिए। मोह केवल तीन में, जीवन-काल में आधार भी लेना चाहिए।",
    "yathā savitakkadukaṃ sampayuttavāro evaṃ kātabbo.": "जैसे आरंभिक विचार वाला दो का वर्गीकरण, वैसे ही जुड़ाव का खंड तैयार करना चाहिए।",
    "evaṃ pañca pañhā yathā savitakkaduke evaṃ kātabbā.": f"इसी तरह पाँच प्रश्न, जैसे {VSV} में, वैसे ही तैयार करने चाहिए।",
    "evaṃ cattāri pañhā yathā savitakkadukassa.": f"इसी तरह चार प्रश्न, जैसे {VSV} के।",
    'yathā sappītikadukaṃ evaṃ ārammaṇampi adhipatipi vitthāretabbā, "{T:nom}"ti nānaṃ.':
        "जैसे उल्लास वाला दो का वर्गीकरण, वैसे ही विषय-कारण का भी और प्रधानता-कारण का भी विस्तार करना चाहिए, “{T}” इतना अलग है।",
    "tīṇi upanissayā dutiyagamanasadisā": "तीनों प्रबल आश्रय, दूसरे क्रम के समान",
    "sappītikadukasadisā": f"{SPD} के समान",
    "cattāri sahajātā nānākkhaṇikā kātabbā, dve nānākkhaṇikā ca.": "चार सह-उत्पत्ति रूपी और भिन्न क्षण रूपी तैयार करने चाहिए, और दो भिन्न क्षण रूपी।",
    "imāni paccayāni sappītikakaraṇena vibhajitabbāni.": "इन कारणों का विभाजन उल्लास वाले के तरीके से करना चाहिए।",
    "evaṃ paccanīyavibhaṅgopi itare tīṇi gaṇanāpi sappītikadukasadisā kātabbā.":
        f"इसी तरह नकारात्मक क्रम का विश्लेषण भी और अन्य तीन गणनाएँ भी {SPD} के समान तैयार करनी चाहिए।",
    "itare dve pākatikā": "अन्य दो सामान्य हैं",
    "mūlaṃ kātabbaṃ": "मूल वाक्य बनाना चाहिए",
    "avasesā tīṇi pākatikā. Saṃkhittaṃ.": "बाकी तीन सामान्य हैं। संक्षिप्त।",
    "avasesā gaṇanāpi sahajātavāropi kātabbo.": "बाकी गणनाएँ भी और सह-उत्पत्ति का खंड भी तैयार करना चाहिए।",
    "paṭiccasadisā. Mūlaṃ kātabbaṃ.": "निर्भरता के खंड के समान। मूल वाक्य बनाना चाहिए।",
    'suddhake arūpamissake ca "vipāka"nti niyāmetabbaṃ, rūpamissake natthi. Saṃkhittaṃ':
        "शुद्ध पद में और अभौतिक-मिश्रित पद में “कर्म के फल रूपी” ऐसा निर्दिष्ट करना चाहिए, भौतिक-मिश्रित में नहीं है। संक्षिप्त",
    "purejātasadisaṃ": "पूर्व-उत्पत्ति-कारण के समान",
    "vippayuttasadisaṃ": "अलगाव-कारण के समान",
})
OBJ_R[:] = [(rx.replace(r"\{T:acc\}", r"\{T:nom\}"), h) for rx, h in OBJ_R]
ARD = "अभौतिक लोक वाले दो के वर्गीकरण"
LKD = "लौकिक वाले दो के वर्गीकरण"
for _k, _v in {
    "{X:ā} khandhā purejātassa imassa kāyassa vippayuttapaccayena paccayo":
        f"{{Xm}} समूह पहले उत्पन्न इस शरीर के लिए {INS('vippayutta')} होते हैं",
    "{X:ā} khandhā ca kabaḷīkāro āhāro ca imassa kāyassa atthipaccayena paccayo":
        f"{{Xm}} समूह और कौर-कौर खाया जाने वाला भोजन इस शरीर के लिए {INS('atthi')} होते हैं",
    "{X:ā} khandhā ca kabaḷīkāro āhāro ca purejātassa imassa kāyassa atthipaccayena paccayo":
        f"{{Xm}} समूह और कौर-कौर खाया जाने वाला भोजन पहले उत्पन्न इस शरीर के लिए {INS('atthi')} होते हैं",
    "{X:ā} khandhā ca rūpajīvitindriyañca kaṭattārūpānaṃ atthipaccayena paccayo":
        f"{{Xm}} समूह और {S.RUPAJIVITINDRIYA} {KTRF} {INS('atthi')} होते हैं",
    "{X:e} khandhe paṭicca {X:ādhipati} vipākaṃ": "{Xm} समूहों पर निर्भर होकर {Xf} प्रधानता, कर्म के फल रूपी",
    "{X:e} khandhe garuṃ katvā assādeti abhinandati": f"{{Xm}} समूहों को महत्व देकर {ASSADA_PL}",
    "paññaṃ upanissāya {X:aṃ} jhānaṃ": "प्रज्ञा के प्रबल आश्रय से {Xms} ध्यान",
    "senāsanaṃ upanissāya {X:aṃ} jhānaṃ": "निवास-स्थान के प्रबल आश्रय से {Xms} ध्यान",
    "{X:aṃ} saddhaṃ upanissāya dānaṃ": "{Xf} श्रद्धा के प्रबल आश्रय से दान",
    "{X:aṃ} ekaṃ khandhaṃ": "{Xm} एक समूह {DEP}",
    "arūpe {X:aṃ} ekaṃ khandhaṃ": f"{S.ARUPE} {{Xm}} एक समूह {{DEP}}",
    "{X:ā} cetanā phalassa kammapaccayena paccayo": f"{{Xms}} इरादा फल के लिए {INS('kamma')} होता है",
    "{X:e} pahīne kilese paccavekkhanti": f"{{Xm}} छोड़े जा चुके मन के क्लेशों पर {REVP}",
    "{X:aṃ} rāgaṃ upanissāya mātaraṃ jīvitā voropeti": "{Xm} राग के प्रबल आश्रय से माता की हत्या करता है",
    "{X:e} khandhe assādeti abhinandati": "{Xm} समूहों का रस लेता है, उनमें आनंद लेता है",
}.items():
    PN(_k, _v)
PN2("{X:aṃ} saddhaṃ upanissāya {Y:aṃ} jhānaṃ", "{Xf} श्रद्धा के प्रबल आश्रय से {Yms} ध्यान")
G.update({
    "{N:aṃ} domanassaṃ {P:assa} domanassassa": "{Nf} उदासी {Pf} उदासी के लिए",
    "{N:ā} micchādiṭṭhi {P:amicchādiṭṭhiyā} anantarapaccayena paccayo":
        f"{{Nf}} ग़लत दृष्टि {{Pf}} ग़लत दृष्टि के लिए {INS('anantara')} होती है",
    "{P:amicchādiṭṭhiyā} upanissayapaccayena paccayo": f"{{Pf}} ग़लत दृष्टि के लिए {INS('upanissaya')} होते हैं",
    "asaññasattānaṃ": S.ASANNASATTA,
    "paṭhamaṃ jhānaṃ paccavekkhati": f"पहले ध्यान पर {REV}",
    "catutthaṃ jhānaṃ paccavekkhati": f"चौथे ध्यान पर {REV}",
    "phalaṃ paccavekkhanti": f"फल पर {REVP}",
    "ariyā pahīne kilese": "आर्य छोड़े जा चुके मन के क्लेशों पर",
    "paṭhamaṃ jhānaṃ garuṃ katvā paccavekkhati": f"पहले ध्यान को महत्व देकर उस पर {REV}",
    "anāgataṃsañāṇaṃ garuṃ katvā paccavekkhati assādeti abhinandati": f"{S.ANAGATAMSA_OBL} को महत्व देकर उस पर {REV}, {ASSADA}",
    "ākāsānañcāyatanaṃ garuṃ katvā paccavekkhati": f"{S.ARUPA_OBL('ākāsānañca')} को महत्व देकर उस पर {REV}",
    "parikammaṃ anāgataṃsañāṇassa anantarapaccayena paccayo": f"प्रारंभिक अभ्यास {S.ANAGATAMSA_OBL} के लिए {INS('anantara')} होता है",
    "paññāya upanissayapaccayena paccayo": f"प्रज्ञा के लिए {INS('upanissaya')} होते हैं",
    "dutiyaṃ jhānaṃ tatiyassa jhānassa": "दूसरा ध्यान तीसरे ध्यान के लिए",
    "tatiyaṃ jhānaṃ catutthassa jhānassa upanissayapaccayena paccayo": f"तीसरा ध्यान चौथे ध्यान के लिए {INS('upanissaya')} होता है",
    "paṭhamassa jhānassa parikammaṃ paṭhamassa jhānassa upanissayapaccayena paccayo":
        f"पहले ध्यान {PARI} पहले ध्यान के लिए {INS('upanissaya')} होता है",
    "anāgataṃsañāṇassa parikammaṃ anāgataṃsañāṇassa upanissayapaccayena paccayo":
        f"{S.ANAGATAMSA_OBL} {PARI} {S.ANAGATAMSA_OBL} के लिए {INS('upanissaya')} होता है",
    "phoṭṭhabbāyatanaṃ kāyaviññāṇassa purejātapaccayena paccayo": f"{S.AYA_OBJ('phoṭṭhabba')} शरीर की चेतना के लिए {INS('purejāta')} होता है",
    "kāyāyatanaṃ kāyaviññāṇassa purejātapaccayena paccayo": f"{S.AYA_SENSE('kāya')} शरीर की चेतना के लिए {INS('purejāta')} होता है",
    "ākāsānañcāyatanaṃ viññāṇañcāyatanassa ārammaṇapaccayena paccayo":
        f"{S.ARUPA_AYATANA['ākāsānañca']} {S.ARUPA_OBL('viññāṇañca')} के लिए {INS('ārammaṇa')} होता है",
    "ākiñcaññāyatanaṃ nevasaññānāsaññāyatanassa ārammaṇapaccayena paccayo":
        f"{S.ARUPA_AYATANA['ākiñcañña']} {S.ARUPA_OBL('nevasaññānāsañña')} के लिए {INS('ārammaṇa')} होता है",
    "viññāṇañcāyatanaṃ": S.ARUPA_AYATANA["viññāṇañca"],
    "nirodhā vuṭṭhahantassa nevasaññānāsaññāyatanaṃ phalasamāpattiyā anantarapaccayena paccayo":
        f"निरोध से उठने वाले व्यक्ति में {S.ARUPA_AYATANA['nevasaññānāsañña']} फल की ध्यान-अवस्था के लिए {INS('anantara')} होता है",
    "ākāsānañcāyatanassa parikammaṃ ākāsānañcāyatanassa anantarapaccayena paccayo":
        f"{S.ARUPA_OBL('ākāsānañca')} {PARI} {S.ARUPA_OBL('ākāsānañca')} के लिए {INS('anantara')} होता है",
    "viññāṇañcāyatanassa": f"{S.ARUPA_OBL('viññāṇañca')} के लिए",
    "ākiñcaññāyatanassa": f"{S.ARUPA_OBL('ākiñcañña')} के लिए",
    "nevasaññānāsaññāyatanassa parikammaṃ nevasaññānāsaññāyatanassa anantarapaccayena paccayo":
        f"{S.ARUPA_OBL('nevasaññānāsañña')} {PARI} {S.ARUPA_OBL('nevasaññānāsañña')} के लिए {INS('anantara')} होता है",
    "ākāsānañcāyatanaṃ viññāṇañcāyatanassa upanissayapaccayena paccayo":
        f"{S.ARUPA_AYATANA['ākāsānañca']} {S.ARUPA_OBL('viññāṇañca')} के लिए {INS('upanissaya')} होता है",
    "viññāṇañcāyatanaṃ ākiñcaññāyatanassa": f"{S.ARUPA_AYATANA['viññāṇañca']} {S.ARUPA_OBL('ākiñcañña')} के लिए",
    "ākāsānañcāyatanassa parikammaṃ ākāsānañcāyatanassa upanissayapaccayena paccayo":
        f"{S.ARUPA_OBL('ākāsānañca')} {PARI} {S.ARUPA_OBL('ākāsānañca')} के लिए {INS('upanissaya')} होता है",
    "nevasaññānāsaññāyatanassa parikammaṃ nevasaññānāsaññāyatanassa upanissayapaccayena paccayo":
        f"{S.ARUPA_OBL('nevasaññānāsañña')} {PARI} {S.ARUPA_OBL('nevasaññānāsañña')} के लिए {INS('upanissaya')} होता है",
    "ariyā phalaṃ paccavekkhanti": f"आर्य फल पर {REVP}",
    "vikkhambhite": "दबाए जा चुके",
    "nibbānaṃ maggassa ārammaṇapaccayena paccayo": f"निर्वाण मार्ग के लिए {INS('ārammaṇa')} होता है",
    "ariyā phalaṃ garuṃ katvā paccavekkhanti": f"आर्य फल को महत्व देकर उस पर {REVP}",
    "nibbānaṃ maggassa adhipatipaccayena paccayo": f"निर्वाण मार्ग के लिए {INS('adhipati')} होता है",
    "maggo phalassa anantarapaccayena paccayo": f"मार्ग फल के लिए {INS('anantara')} होता है",
    "anulomaṃ phalasamāpattiyā": "अनुकूलता फल की ध्यान-अवस्था के लिए",
    "vodānaṃ maggassa anantarapaccayena paccayo": f"{S.VODANA} मार्ग के लिए {INS('anantara')} होती है",
    "paṭhamo maggo dutiyassa maggassa upanissayapaccayena paccayo": f"पहला मार्ग दूसरे मार्ग के लिए {INS('upanissaya')} होता है",
    "ariyā maggaṃ upanissāya anuppannaṃ samāpattiṃ uppādenti": "आर्य मार्ग के प्रबल आश्रय से उत्पन्न न हुई ध्यान-अवस्था उत्पन्न करते हैं",
    "uppannaṃ samāpajjanti": "उत्पन्न हुई में प्रवेश करते हैं",
    "saṅkhāre aniccato": "निर्मित परिघटनाओं को अनित्य",
    "paṭibhānapaṭisambhidāya ṭhānāṭhānakosallassa upanissayapaccayena paccayo":
        f"सूझ-बूझ के विश्लेषणात्मक ज्ञान के लिए, संभव और असंभव को जानने की कुशलता के लिए {INS('upanissaya')} होता है",
    "jhānaṃ uppādeti": "ध्यान उत्पन्न करता है",
    "paṭhamassa maggassa parikammaṃ paṭhamassa maggassa upanissayapaccayena paccayo":
        f"पहले मार्ग {PARI} पहले मार्ग के लिए {INS('upanissaya')} होता है",
    "paṭhamassa maggassa parikammaṃ paṭhamassa maggassa": f"पहले मार्ग {PARI} पहले मार्ग के लिए",
    "ekaṃyeva": "एक ही",
    "rūpajīvitindriyaṃ mātughātikammassa": f"{S.RUPAJIVITINDRIYA} माता की हत्या के कर्म के लिए",
    "pitughātikammassa": "पिता की हत्या के कर्म के लिए",
    "arahantaghātikammassa": "अर्हत् की हत्या के कर्म के लिए",
    "ruhiruppādakammassa ārammaṇapaccayena paccayo": f"बुद्ध का खून बहाने के कर्म के लिए {INS('ārammaṇa')} होती है",
    "ruhiruppādakammassa purejātapaccayena paccayo": f"बुद्ध का खून बहाने के कर्म के लिए {INS('purejāta')} होती है",
    "ruhiruppādakammassa": "बुद्ध का खून बहाने के कर्म के लिए",
    "yaṃ vatthuṃ āmasantassa micchattaniyatā khandhā uppajjanti":
        "जिस आधार को छूते हुए व्यक्ति में ग़लत दिशा में निश्चित समूह उत्पन्न होते हैं",
    "taṃ vatthu micchattaniyatānaṃ khandhānaṃ ārammaṇapaccayena paccayo":
        f"वह आधार ग़लत दिशा में निश्चित समूहों के लिए {INS('ārammaṇa')} होता है",
    "mātughātikammaṃ mātughātikammassa": "माता की हत्या का कर्म माता की हत्या के कर्म के लिए",
    "saṅghabhedakammassa": "संघ में फूट डालने के कर्म के लिए",
    "mātaraṃ jīvitā voropetvā": "माता की हत्या करके",
    "saṅghaṃ bhinditvā tassa paṭighātatthāya dānaṃ deti": "संघ में फूट डालकर उसके प्रतिकार के लिए दान देता है",
    "senāsanaṃ upanissāya mātaraṃ jīvitā voropeti": "निवास-स्थान के प्रबल आश्रय से माता की हत्या करता है",
    "senāsanaṃ mātughātikammassa": "निवास-स्थान माता की हत्या के कर्म के लिए",
    "saṅghabhedakammassa upanissayapaccayena paccayo": f"संघ में फूट डालने के कर्म के लिए {INS('upanissaya')} होते हैं",
    "vatthuṃ paccayā ahetukā khandhā": f"आधार के कारण {S.AHETUKA} समूह",
    "diṭṭhiṃ assādeti abhinandati": "दृष्टि का रस लेता है, उसमें आनंद लेता है",
    "domanassaṃ ārabbha domanassaṃ uppajjati": "उदासी को विषय बनाकर उदासी उत्पन्न होती है",
    "uposathakammaṃ katvā taṃ assādeti abhinandati": f"उपवास-व्रत का पालन करके {ASSADA}",
    "vatthuṃ": "आधार {KO}",
    "uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati": f"उपवास-व्रत का पालन करके, उसे महत्व देकर उस पर {REV}",
    "uposathakammaṃ katvā taṃ garuṃ katvā assādeti abhinandati": f"उपवास-व्रत का पालन करके, उसे महत्व देकर {ASSADA}",
})
PAREN.update({
    "nakāmāvacaraṃ paṭiccavārasadisaṃ ninnānaṃ, idha sabbe mahābhūtā kātabbā.":
        "इंद्रिय-सुखों के लोक से संबंधित न होने वाली परिघटना निर्भरता के खंड के समान, बिना भिन्नता के, यहाँ सभी महाभूत लेने चाहिए।",
    "yāva asaññasattā, itare pañcapi pañhā, anulomaṃ kātabbaṃ":
        "पहचान-रहित प्राणियों तक, अन्य पाँच प्रश्न भी, सकारात्मक क्रम तैयार करना चाहिए",
    "saṃkhittaṃ. Mūlaṃ. Itarepi pañhā kātabbā": "संक्षिप्त। मूल वाक्य। अन्य प्रश्न भी तैयार करने चाहिए",
    "yāva ajjhattikaṃ mahābhūtaṃ": "आंतरिक महाभूत तक",
    'suddhike arūpe ca missake ca "vipāka"nti niyāmetabbaṃ':
        "शुद्ध पद में, अभौतिक में और मिश्रित में “कर्म के फल रूपी” ऐसा निर्दिष्ट करना चाहिए",
    "anulomaṃ": S.ANULOMA, "paccanīyaṃ": S.PACCANIYA,
    "yathā cūḷantaraduke lokiyadukaṃ. Evaṃ imampi dukaṃ kātabbaṃ, ninnānākaraṇaṃ.":
        "जैसे बीच के छोटे दो-दो के वर्गीकरणों में लौकिक वाला दो का वर्गीकरण। इसी तरह यह दो का वर्गीकरण भी तैयार करना चाहिए, बिना किसी भिन्नता के।",
    "yāva asaññasattā kātabbā": "पहचान-रहित प्राणियों तक तैयार करने चाहिए",
    "arūpadukasadisā kātabbā": f"{ARD} के समान तैयार करने चाहिए",
    "arūpadukasadisā kātabbā, āmasanā nānāpadāyeva": f"{ARD} के समान तैयार करने चाहिए, केवल उल्लेख के पद अलग हैं",
    "saṃkhittaṃ. Pañcapi pañhā kātabbā. Yathā niyyānikadukaṃ evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi kātabbā, ninnānākaraṇaṃ āmasanaṃ nānaṃ":
        "संक्षिप्त। पाँचों प्रश्न तैयार करने चाहिए। जैसे मुक्ति की ओर ले जाने वाला दो का वर्गीकरण, वैसे ही निर्भरता का खंड भी, सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, घुले-मिले होने का खंड भी और जुड़ाव का खंड भी तैयार करने चाहिए, बिना किसी भिन्नता के, केवल उल्लेख अलग है",
    "niyyānikadukasadisā ninnānākaraṇā": "मुक्ति की ओर ले जाने वाले दो के वर्गीकरण के समान, बिना किसी भिन्नता के",
    "arūpadukasadisaṃ": f"{ARD} के समान",
    "arūpāvacaradukasadisaṃ": f"{ARD} के समान",
    "yāva ajjhattikā mahābhūtā. Yathā cūḷantaraduke lokiyadukasadisaṃ ninnānākaraṇaṃ.":
        f"आंतरिक महाभूतों तक। जैसे बीच के छोटे दो-दो के वर्गीकरणों में {LKD} के समान, बिना किसी भिन्नता के।",
    "pañca pañhā arūpāvacaradukasadisā, anulomapaṭiccasadisā.":
        f"पाँच प्रश्न {ARD} के समान, सकारात्मक क्रम वाले निर्भरता के खंड के समान।",
    "yathā arūpāvacaradukassa paccayavāropi evaṃ kātabbo": f"जैसे {ARD} का कारण का खंड भी, वैसे ही तैयार करना चाहिए",
    "evaṃ itare dve gaṇanāpi nissayavāropi kātabbo, saṃsaṭṭhavārepi dve pañhā kātabbā sabbattha.":
        "इसी तरह अन्य दो गणनाएँ भी और आश्रय का खंड भी तैयार करना चाहिए, घुले-मिले होने के खंड में भी हर जगह दो प्रश्न तैयार करने चाहिए।",
    "arūpadukasadisaṃ, cattāri": f"{ARD} के समान, चार",
    "arūpadukasadisā": f"{ARD} के समान",
})
DY = {}
LINE = {}
# (batches above this line; the {T:..} conversion runs at the end of the file)

T_FORM(G, 'vitakk', VIT)

for _tab in (G, PAREN):
    for _k in [k for k in _tab if "{T:acc}" in k]:
        _tab.setdefault(_k.replace("{T:acc}", "{T:nom}"), _tab[_k])
