"""Builder for AI_translation/hindi/pi-1-hindi-plain-rails_split_chapters/2-04-cittuppadakandam.md.

Every line is parsed from the Pāli and rendered from fixed strings, so identical Pāli gives byte-identical
Hindi and an unknown Pāli string stops the build. Strings shared with the approved sample are imported
from build_rails_sample.py (import only).

usage: python -I -X utf8 build_rails_2-04.py
"""
import pathlib
import re
import sys

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\rails"
sys.path.insert(0, RAILS_DIR)
import build_rails_sample as B  # noqa: E402

CH = "2-04-cittuppadakandam.md"
F, S = B.F, B.S
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")

# ------------------------------------------------------------------ factors new in this chapter
F.update({
    "micchādiṭṭhi": ("ग़लत दृष्टि", "f"),
    "micchāsaṅkappo": ("ग़लत संकल्प", "m"),
    "micchāvāyāmo": ("ग़लत प्रयास", "m"),
    "micchāsamādhi": ("ग़लत एकाग्रता", "f"),
    "ahirikabalaṃ": ("निर्लज्जता का बल", "m"),
    "anottappabalaṃ": ("बुराई के प्रति निडरता का बल", "m"),
    "lobho": ("लोभ", "m"),
    "doso": ("द्वेष", "m"),
    "moho": ("मोह", "m"),
    "abhijjhā": ("लालच", "m"),
    "byāpādo": ("दुर्भावना", "f"),
    "ahirikaṃ": ("निर्लज्जता", "f"),
    "anottappaṃ": ("बुराई के प्रति निडरता", "f"),
    "upekkhā": ("समभाव", "m"),
    "upekkhindriyaṃ": ("समभाव की क्षमता", "f"),
    "dukkhaṃ": ("दुःख", "m"),
    "domanassindriyaṃ": ("उदासी की क्षमता", "f"),
    "sukhindriyaṃ": ("सुख की क्षमता", "f"),
    "vicikicchā": ("संशय", "m"),
    "uddhaccaṃ": ("बेचैनी", "f"),
    "saṅkhārakkhandho": ("मानसिक रचनाओं का समूह", "m"),
})

# ------------------------------------------------------------------ synonym strings
TN = {  # tajjā-element: Hindi "corresponding element"
    "tajjāmanoviññāṇadhātu": "उसके अनुरूप मन की चेतना का तत्व",
    "tajjācakkhuviññāṇadhātu": "उसके अनुरूप आँख की चेतना का तत्व",
    "tajjākāyaviññāṇadhātu": "उसके अनुरूप शरीर की चेतना का तत्व",
    "tajjāmanodhātu": "उसके अनुरूप मन का तत्व",
}
CONTACT = {k: v.replace(" का तत्व", " के तत्व के संपर्क से उत्पन्न") for k, v in TN.items()}
assert CONTACT["tajjāmanoviññāṇadhātu"] == B.TAJJA

P_SUKHA = "cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā"
P_DUKKHA = "cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā vedanā"
P_NEUTRAL = "cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā"
P_KAYA = "kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā"
H_SUKHA = B.SUKHA_TAIL
H_DUKKHA = ("मानसिक असुहावनापन, मानसिक दुःख, मन के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, "
            "मन के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति")
H_NEUTRAL = ("न मानसिक सुहावनापन, न मानसिक असुहावनापन, मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभव, "
             "मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभूति")
H_KAYA = ("शारीरिक सुहावनापन, शारीरिक सुख, शरीर के संपर्क से उत्पन्न सुहावना सुखद अनुभव, "
          "शरीर के संपर्क से उत्पन्न सुहावनी सुखद अनुभूति")

DITTHI = ("दृष्टि, दृष्टियों में फँसना, दृष्टि का घना जंगल, दृष्टि का बीहड़, दृष्टि का टेढ़ापन, दृष्टि की छटपटाहट, "
          "दृष्टि का बंधन, पकड़, कसकर पकड़ना{v1}, आग्रह, ग़लत धारणा, कुमार्ग, ग़लत रास्ता, ग़लतपन, मतवादों का आधार, उलटी पकड़{v2}")
LOBHA = "लोभ, लोभ करना, लोभ से भरा होना, प्रबल राग, राग करना, राग से भरा होना, लालच, लोभ रूपी हानिकर मूल"
MOHA = ("न जानना, न देखना, सत्य तक न पहुँचना, बोध न होना, पूर्ण बोध न होना, भेद न पाना, न समेट पाना, गहराई में न उतर पाना, "
        "निष्पक्ष रूप से न देखना, पुनः विचार न करना, प्रत्यक्ष न करना, दुर्बुद्धि, मूर्खता, स्पष्ट समझ का अभाव, मोह, गहरा मोह, घोर मोह, "
        "अज्ञान, अज्ञान की बाढ़, अज्ञान की जकड़न, अज्ञान की सुप्त प्रवृत्ति, अज्ञान का आवेश, अज्ञान की रुकावट, मोह रूपी हानिकर मूल")
DOSA = ("द्वेष, द्वेष करना, द्वेष से भरा होना, दुर्भावना, दुर्भावना रखना, दुर्भावना से भरा होना, विरोध, प्रतिविरोध, उग्रता, "
        "कटु वचन, मन की अप्रसन्नता")
VICI = ("शंका, शंका करना, शंका से भरा होना, दुविधा, संशय, दुचित्तापन, दोराहा, संदेह, किसी एक बात को पक्का न पकड़ पाना, "
        "हिचकिचाना, बार-बार हिचकिचाना, गहराई में न उतर पाना, मन का जड़ हो जाना, मन की खरोंच")
UDDH = "मन की बेचैनी, अशांति, मन का भटकाव, मन का डाँवाडोल होना"
AHIRI = "जिस बात से लज्जा आनी चाहिए उससे लज्जा न आना, बुरी हानिकर परिघटनाओं को अपनाने से लज्जा न आना"
ANOTT = "जिस बात से डरना चाहिए उससे न डरना, बुरी हानिकर परिघटनाओं को अपनाने से न डरना"

P_VITAKKA = "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā"
P_VICARA = "cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā"
P_PITI = "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa"
P_SAMADHI = "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ micchāsamādhi"
P_VIRIYA = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā "
            "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ micchāvāyāmo")
P_DITTHI = ("diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho "
            "patiṭṭhāho{v1} abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho{v2}")
P_MOHA = ("aññāṇaṃ adassanaṃ anabhisamayo ananubodho asambodho appaṭivedho asaṃgāhanā apariyogāhanā asamapekkhanā "
          "apaccavekkhanā apaccakkhakammaṃ dummejjhaṃ bālyaṃ asampajaññaṃ moho pamoho sammoho avijjā avijjogho avijjāyogo "
          "avijjānusayo avijjāpariyuṭṭhānaṃ avijjālaṅgī moho akusalamūlaṃ")
P_DOSA = "doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa"
P_VICI = ("kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvedhāpatho saṃsayo anekaṃsaggāho āsappanā parisappanā "
          "apariyogāhanā thambhitattaṃ cittassa manovilekho")
P_CITTA = "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
P_LIFE = "āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ"

TAJJA_CITTA = TN["tajjāmanoviññāṇadhātu"]
assert S["cittaṃ"].endswith(TAJJA_CITTA)
assert S["vitakko"].endswith(", सही संकल्प")
assert S["samādhi"].endswith("सही एकाग्रता")
assert S["vīriya_plain"].endswith("सही प्रयास")

SYN = {
    "phasso phusanā saṃphusanā saṃphusitattaṃ": S["phasso"],
    P_SUKHA: H_SUKHA,
    P_DUKKHA: H_DUKKHA,
    P_NEUTRAL: H_NEUTRAL,
    P_KAYA: H_KAYA,
    P_VITAKKA + " micchāsaṅkappo": S["vitakko"].replace("सही संकल्प", "ग़लत संकल्प"),
    P_VITAKKA: S["vitakko"][: -len(", सही संकल्प")],
    P_VICARA: S["vicāro"],
    P_PITI: S["pīti"],
    P_SAMADHI: S["samādhi"].replace("सही एकाग्रता", "ग़लत एकाग्रता"),
    P_VIRIYA: S["vīriya_plain"].replace("सही प्रयास", "ग़लत प्रयास"),
    "cittassa ṭhiti": "मन की स्थिरता",
    P_DITTHI.format(v1=" [paṭiggāho (sī. syā.)]", v2=" [vipariyesagāho (ka.)]"): DITTHI.format(
        v1=" [पाठभेद (Sī., Syā.): paṭiggāho]", v2=" [वर्तनी-भेद (Ka.): vipariyesagāho]"),
    P_DITTHI.format(v1="", v2=""): DITTHI.format(v1="", v2=""),
    "lobho lubbhanā lubbhitattaṃ sārāgo sārajjanā sārajjitattaṃ abhijjhā lobho akusalamūlaṃ": LOBHA,
    P_MOHA: MOHA,
    P_DOSA: DOSA,
    P_VICI: VICI,
    "cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": UDDH,
}
for t, name in TN.items():
    cont = CONTACT[t]
    SYN[f"{t}samphassajaṃ {P_SUKHA}"] = f"{cont} {H_SUKHA}"
    SYN[f"{t}samphassajaṃ {P_DUKKHA}"] = f"{cont} {H_DUKKHA}"
    SYN[f"{t}samphassajaṃ {P_NEUTRAL}"] = f"{cont} {H_NEUTRAL}"
    SYN[f"{t}samphassajaṃ {P_KAYA}"] = f"{cont} {H_KAYA}"
    SYN[f"{t}samphassajā saññā sañjānanā sañjānitattaṃ"] = f"{cont} पहचान, पहचानना, पहचान चुका होना"
    SYN[f"{t}samphassajā cetanā sañcetanā cetayitattaṃ"] = f"{cont} इरादा, इरादा करना, इरादा कर चुका होना"
    SYN[P_CITTA + t] = S["cittaṃ"].replace(TAJJA_CITTA, name)

LIFE_H = S["jīvita_var"].replace(" [वर्तनी-भेद (Sī.): irīyanā]", "")
BARE = {  # definitions with no «जो … है»
    "na hirīyati hiriyitabbena na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": AHIRI,
    "na ottappati ottappitabbena na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": ANOTT,
}

# ------------------------------------------------------------------ frames and openings
OTH_P = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā"
CLOSE = {"akusalā": "ये हानिकर परिघटनाएँ हैं", "kusalā": "ये हितकर परिघटनाएँ हैं",
         "abyākatā": "ये नैतिक रूप से अनिर्धारित परिघटनाएँ हैं"}
Q = {"akusalā": "हानिकर परिघटनाएँ कौन-सी हैं?", "kusalā": "हितकर परिघटनाएँ कौन-सी हैं?",
     "abyākatā": "नैतिक रूप से अनिर्धारित परिघटनाएँ कौन-सी हैं?"}
EXCEPT = "अनुभूति के समूह को छोड़कर, पहचान के समूह को छोड़कर, चेतना के समूह को छोड़कर"

P_ARM = {
    "rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha":
        "जिसका विषय दृश्य रूप हो, या ध्वनि, या गंध, या स्वाद, या स्पर्श, या मन का विषय, या जिस किसी को भी वह विषय बनाए",
    "rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha":
        "जिसका विषय दृश्य रूप हो… या मन का विषय, या जिस किसी को भी वह विषय बनाए",
    "rūpārammaṇaṃ vā…pe… yaṃ yaṃ vā panārabbha":
        "जिसका विषय दृश्य रूप हो… या जिस किसी को भी वह विषय बनाए",
    "rūpārammaṇā vā…pe… dhammārammaṇā vā yaṃ yaṃ vā panārabbha":
        "जिसका विषय दृश्य रूप हो… या मन का विषय, या जिस किसी को भी वह विषय बनाए",
    "rūpārammaṇā vā…pe… phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha":
        "जिसका विषय दृश्य रूप हो… या स्पर्श, या जिस किसी को भी वह विषय बनाए",
}
SAH = {"somanassasahagataṃ": "प्रसन्नता के साथ होने वाला", "upekkhāsahagataṃ": "समभाव के साथ होने वाला",
       "domanassasahagataṃ": "उदासी के साथ होने वाला"}
SAMP = {"diṭṭhigatasampayuttaṃ": "ग़लत दृष्टि से जुड़ा", "diṭṭhigatavippayuttaṃ": "ग़लत दृष्टि से अलग",
        "paṭighasampayuttaṃ": "चिढ़ से जुड़ा", "vicikicchāsampayuttaṃ": "संशय से जुड़ा", "uddhaccasampayuttaṃ": "बेचैनी से जुड़ा"}
PROMPT = "प्रेरणा सहित"

OPEN = {}
for ps, hs in SAH.items():
    for pm, hm in SAMP.items():
        for arm_p, arm_h in P_ARM.items():
            OPEN[f"akusalaṃ cittaṃ uppannaṃ hoti {ps} {pm} {arm_p}"] = (
                f"जिस समय हानिकर मन उत्पन्न होता है, जो {hs} और {hm} होता है और {arm_h}")
            OPEN[f"akusalaṃ cittaṃ uppannaṃ hoti {ps} {pm} sasaṅkhārena {arm_p}"] = (
                f"जिस समय हानिकर मन उत्पन्न होता है, जो {hs}, {hm} और {PROMPT} होता है और {arm_h}")

KCAUSE = "इंद्रिय-सुखों के लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण"
PK = "kāmāvacarassa kusalassa kammassa katattā upacitattā"
PV = "कर्म के फल रूपी"
OPEN[f"{PK} vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ rūpārammaṇaṃ"] = (
    f"जिस समय {KCAUSE} {PV} आँख की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली होती है और जिसका विषय दृश्य रूप होता है")
OPEN[(f"{PK} vipākaṃ sotaviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ saddārammaṇaṃ…pe… ghānaviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ "
      "gandhārammaṇaṃ…pe… jivhāviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ rasārammaṇaṃ…pe… kāyaviññāṇaṃ uppannaṃ hoti sukhasahagataṃ "
      "phoṭṭhabbārammaṇaṃ")] = (
    f"जिस समय {KCAUSE} {PV} कान की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली होती है और जिसका विषय ध्वनि होती है… "
    "नाक की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली होती है और जिसका विषय गंध होती है… "
    "जीभ की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली होती है और जिसका विषय स्वाद होता है… "
    "शरीर की चेतना उत्पन्न होती है, जो सुख के साथ होने वाली होती है और जिसका विषय स्पर्श होता है")
OPEN[f"{PK} vipākā manodhātu uppannā hoti upekkhāsahagatā rūpārammaṇā vā…pe… phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha"] = (
    f"जिस समय {KCAUSE} {PV} मन का तत्व उत्पन्न होता है, जो समभाव के साथ होने वाला होता है और जिसका विषय दृश्य रूप हो… "
    "या स्पर्श, या जिस किसी को भी वह विषय बनाए")
for ps, hs in (("somanassasahagatā", "प्रसन्नता के साथ होने वाला"), ("upekkhāsahagatā", "समभाव के साथ होने वाला")):
    OPEN[f"{PK} vipākā manoviññāṇadhātu uppannā hoti {ps} rūpārammaṇā vā…pe… dhammārammaṇā vā yaṃ yaṃ vā panārabbha"] = (
        f"जिस समय {KCAUSE} {PV} मन की चेतना का तत्व उत्पन्न होता है, जो {hs} होता है और जिसका विषय दृश्य रूप हो… "
        "या मन का विषय, या जिस किसी को भी वह विषय बनाए")

# Kaṇḍa-summary line: «Tasmiṃ kho pana samaye …»
KOTT = {
    "cattāro khandhā honti": "चार समूह होते हैं",
    "dvāyatanāni honti": "दो इंद्रिय-क्षेत्र होते हैं",
    "dve dhātuyo honti": "दो तत्व होते हैं",
    "tayo āhārā honti": "तीन आहार होते हैं",
    "pañcindriyāni honti": "पाँच क्षमताएँ होती हैं",
    "cattāri indriyāni honti": "चार क्षमताएँ होती हैं",
    "tīṇindriyāni honti": "तीन क्षमताएँ होती हैं",
    "pañcaṅgikaṃ jhānaṃ hoti": "पाँच अंगों वाला ध्यान होता है",
    "caturaṅgikaṃ jhānaṃ hoti": "चार अंगों वाला ध्यान होता है",
    "caturaṅgiko maggo hoti": "चार अंगों वाला मार्ग होता है",
    "tivaṅgiko maggo hoti": "तीन अंगों वाला मार्ग होता है",
    "duvaṅgiko maggo hoti": "दो अंगों वाला मार्ग होता है",
    "cattāri balāni honti": "चार बल होते हैं",
    "tīṇi balāni honti": "तीन बल होते हैं",
    "dve hetū honti": "दो मूल होते हैं",
    "eko hetu hoti": "एक मूल होता है",
    "eko phasso hoti": "एक संपर्क होता है",
    "ekaṃ dhammāyatanaṃ hoti": "मन के विषयों का एक इंद्रिय-क्षेत्र होता है",
    "ekā dhammadhātu hoti": "मन के विषयों का एक तत्व होता है",
    "ekā cakkhuviññāṇadhātu hoti": "आँख की चेतना का एक तत्व होता है",
    "ekā kāyaviññāṇadhātu hoti": "शरीर की चेतना का एक तत्व होता है",
    "ekā manodhātu hoti": "मन का एक तत्व होता है",
    "ekā manoviññāṇadhātu hoti": "मन की चेतना का एक तत्व होता है",
}
KOTT_OPEN = "और उस समय"

EXACT = {
    "#### Dvādasa akusalāni": "#### बारह हानिकर मन",
    "Dvādasa akusalacittāni.": "बारह हानिकर मन।",
    "#### Abyākatavipāko": "#### नैतिक रूप से अनिर्धारित कर्म-फल",
    "##### Kusalavipākapañcaviññāṇāni": "##### हितकर कर्म के फल रूपी पाँच प्रकार की चेतना",
    "Kusalavipākāni pañcaviññāṇāni.": "हितकर कर्म के फल रूपी पाँच प्रकार की चेतना।",
    "##### Kusalavipākamanodhātu": "##### हितकर कर्म के फल रूपी मन का तत्व",
    "Kusalavipākā manodhātu.": "हितकर कर्म के फल रूपी मन का तत्व।",
    "##### Kusalavipākamanoviññāṇadhātusomanassasahagatā": "##### हितकर कर्म के फल रूपी प्रसन्नता के साथ होने वाला मन की चेतना का तत्व",
    "Kusalavipākā manoviññāṇadhātu somanassasahagatā.": "हितकर कर्म के फल रूपी प्रसन्नता के साथ होने वाला मन की चेतना का तत्व।",
    "##### Kusalavipākamanoviññāṇadhātuupekkhāsahagatā": "##### हितकर कर्म के फल रूपी समभाव के साथ होने वाला मन की चेतना का तत्व",
    "Kusalavipākā upekkhāsahagatā manoviññāṇadhātu.": "हितकर कर्म के फल रूपी समभाव के साथ होने वाला मन की चेतना का तत्व।",
    "##### Aṭṭhamahāvipākā": "##### आठ बड़े कर्म-फल",
    "Aṭṭhamahāvipākā.": "आठ बड़े कर्म-फल।",
    "##### Rūpāvacaravipākā": "##### सूक्ष्म भौतिक लोक से संबंधित कर्म-फल",
    "Rūpāvacaravipākā.": "सूक्ष्म भौतिक लोक से संबंधित कर्म-फल।",
    "##### Arūpāvacaravipākā": "##### अभौतिक लोक से संबंधित कर्म-फल",
    "Arūpāvacaravipākā.": "अभौतिक लोक से संबंधित कर्म-फल।",
}

# ------------------------------------------------------------------ the jhāna segments (^1-498 to ^1-504)
P_FACT = "phasso hoti…pe… avikkhepo hoti…pe…"
H_FACT = "संपर्क होता है… भटकाव का अभाव होता है…"
RUP = "सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है"
ARUP = "अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है"
RCAUSE = "उसी सूक्ष्म भौतिक लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण"
ACAUSE = "उसी अभौतिक लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण"
DWELL = "प्राप्त करके उसमें रहता है"
EARTH = "जो पृथ्वी के ध्यान-मंडल पर आधारित होता है"
ARU1 = ("पूरी तरह भौतिक रूप की पहचानों को पार कर जाने से, टकराव की पहचानों के मिट जाने से, "
        "विविधता की पहचानों पर मनोयोग न करने से, सुख को छोड़ने से…")
Q_ABY = Q["abyākatā"]
END_K = f"उस समय {H_FACT} {CLOSE['kusalā']}।"
END_A = f"उस समय {H_FACT} {CLOSE['abyākatā']}।"


def arupa(cross, base):
    """One immaterial segment: cross = what is surmounted (Hindi, with trailing «…»), base = «X के क्षेत्र की पहचान …»."""
    jh = f"{base} के साथ होने वाले चौथे ध्यान को {DWELL}"
    vjh = f"{PV} और {base} के साथ होने वाले चौथे ध्यान को {DWELL}"
    return (f"{Q_ABY} जिस समय कोई {ARUP}, {cross} {jh}, {END_K} "
            f"{ACAUSE} जिस समय वह {cross} {vjh}, {END_A}")


SPECIAL = {
    "1-498": [
        (f"{Q_ABY} जिस समय {KCAUSE} {PV} मन की चेतना का तत्व उत्पन्न होता है, जो प्रसन्नता के साथ होने वाला और ज्ञान से जुड़ा होता है… "
         "जो प्रसन्नता के साथ होने वाला, ज्ञान से जुड़ा और प्रेरणा सहित होता है… जो प्रसन्नता के साथ होने वाला और ज्ञान से अलग होता है… "
         "जो प्रसन्नता के साथ होने वाला, ज्ञान से अलग और प्रेरणा सहित होता है… जो समभाव के साथ होने वाला और ज्ञान से जुड़ा होता है… "
         "जो समभाव के साथ होने वाला, ज्ञान से जुड़ा और प्रेरणा सहित होता है… जो समभाव के साथ होने वाला और ज्ञान से अलग होता है… "
         "जो समभाव के साथ होने वाला, ज्ञान से अलग और प्रेरणा सहित होता है और जिसका विषय दृश्य रूप हो… या मन का विषय, या जिस किसी को भी वह विषय बनाए, "
         f"उस समय {H_FACT} {CLOSE['abyākatā']}… लोभ का अभाव रूपी नैतिक रूप से अनिर्धारित मूल… "
         f"द्वेष का अभाव रूपी नैतिक रूप से अनिर्धारित मूल… {CLOSE['abyākatā']}।"),
        EXACT["Aṭṭhamahāvipākā."],
    ],
    "1-499": [
        f"{Q_ABY} जिस समय कोई {RUP}, इंद्रिय-सुखों से अलग होकर… पहले ध्यान को {DWELL}, {EARTH}, {END_K} "
        f"{RCAUSE} जिस समय वह इंद्रिय-सुखों से अलग होकर… {PV} पहले ध्यान को {DWELL}, {EARTH}, {END_A}",
    ],
    "1-500": [
        (f"{Q_ABY} जिस समय कोई {RUP}, आरंभिक विचार और सतत विचार के शांत होने से… दूसरे ध्यान को… तीसरे ध्यान को… चौथे ध्यान को… "
         f"पहले ध्यान को… पाँचवें ध्यान को {DWELL}, {EARTH}, {END_K} "
         f"{RCAUSE} जिस समय वह सुख को छोड़ने से… {PV} पाँचवें ध्यान को {DWELL}, {EARTH}, {END_A}"),
        EXACT["Rūpāvacaravipākā."],
    ],
    "1-501": [arupa(ARU1, "अनंत आकाश के क्षेत्र की पहचान")],
    "1-502": [arupa("पूरी तरह अनंत आकाश के क्षेत्र को पार करके, सुख को छोड़ने से…", "अनंत चेतना के क्षेत्र की पहचान")],
    "1-503": [arupa("पूरी तरह अनंत चेतना के क्षेत्र को पार करके, सुख को छोड़ने से…", "कुछ भी न होने के क्षेत्र की पहचान")],
    "1-504": [arupa("पूरी तरह कुछ भी न होने के क्षेत्र को पार करके, सुख को छोड़ने से…", "न पहचान, न अ-पहचान के क्षेत्र की पहचान"),
              EXACT["Arūpāvacaravipākā."]],
}

# ------------------------------------------------------------------ line parser
DEF = re.compile(r"^Katam(?:o|ā|aṃ) tasmiṃ samaye (\S+) hoti[?.] (Yo|Yā|Yaṃ) (tasmiṃ samaye|tesaṃ arūpīnaṃ dhammānaṃ) (.+?) – (?:ayaṃ|idaṃ) tasmiṃ samaye \1 hoti(.*)$")
SANKH = re.compile(r"^Katamo tasmiṃ samaye saṅkhārakkhandho hoti\? (.+?); " + re.escape(OTH_P) + r" ṭhapetvā vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti(.*)$")
OPENLINE = re.compile(r"^Katame dhammā (akusalā|abyākatā)\? Yasmiṃ samaye (.+?), tasmiṃ samaye (.+)$")
KOTTLINE = re.compile(r"^Tasmiṃ kho pana samaye (.+?)(; " + re.escape(OTH_P) + r" – ime dhammā (?:akusalā|abyākatā)…pe…\.)$")
ANY_LATIN = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷ]")


def tail(t):
    """Everything after the last «hoti»."""
    t = t.replace(" …pe…", "…pe…").replace(OTH_P, B.CLOSE_OTHERS)
    t = re.sub(r"ime dhammā (akusalā|kusalā|abyākatā)", lambda m: CLOSE[m.group(1)], t)
    t = t.replace("…pe….", "…।")
    t = t.replace("…pe…", "…")
    if t.endswith("."):
        t = t[:-1] + "।"
    assert not ANY_LATIN.search(t), t
    return t


def factor_sequence(rest):
    """Parse «phasso hoti, vedanā hoti …pe… X hoti» and return (Hindi, remaining tail)."""
    out = []
    while True:
        m = re.match(r"([^\s,;…]+) hoti", rest)
        assert m, rest[:60]
        name, g = F[m.group(1)]
        out.append(f"{name} {B.hoti(g)}")
        rest = rest[m.end():]
        if rest.startswith(", "):
            out.append(", ")
            rest = rest[2:]
            continue
        m2 = re.match(r" ?…pe… (?=[^\s,;…]+ hoti)", rest)
        if m2:
            out.append("… ")
            rest = rest[m2.end():]
            continue
        return "".join(out), rest


def kott(body):
    parts = re.split(r", |…pe… ", body)
    seps = re.findall(r", |…pe… ", body)
    out = [KOTT[parts[0]]]
    for sep, p in zip(seps, parts[1:]):
        out.append((", " if sep == ", " else "… ") + KOTT[p])
    return "".join(out)


def question(x):
    return B.question(x)


def tr(line):
    if line in EXACT:
        return EXACT[line]
    m = DEF.match(line)
    if m:
        x, rel, scope, body, t = m.groups()
        q = question(x)
        name, g = F[x]
        end = f"यह उस समय {name} {B.hoti(g)}{tail(t)}"
        if scope.startswith("tesaṃ"):
            assert body == P_LIFE, body
            return f"{q} उन अभौतिक परिघटनाओं की जो {LIFE_H} है – {end}"
        if body in BARE:
            return f"{q} उस समय {BARE[body]} – {end}"
        return f"{q} उस समय जो {SYN[body]} है – {end}"
    m = SANKH.match(line)
    if m:
        lst, t = m.groups()
        names = ", ".join(F[w[:1].lower() + w[1:]][0] for w in lst.split())
        name, g = F["saṅkhārakkhandho"]
        return (f"{question('saṅkhārakkhandho')} {names}; {B.CLOSE_OTHERS}, {EXCEPT} – "
                f"यह उस समय {name} {B.hoti(g)}{tail(t)}")
    m = OPENLINE.match(line)
    if m:
        kind, op, rest = m.groups()
        fs, t = factor_sequence(rest)
        return f"{Q[kind]} {OPEN[op]}, उस समय {fs}{tail(t)}"
    m = KOTTLINE.match(line)
    if m:
        body, t = m.groups()
        return f"{KOTT_OPEN} {kott(body)}{tail(t)}"
    raise SystemExit(f"UNPARSED: {line[:160]}")


def main():
    src = B.PALI / CH
    hindi = {}
    for sid, lines in B.segments(src):
        lines = [ID.sub("", l).rstrip() for l in lines]
        if sid in SPECIAL:
            hindi[sid] = SPECIAL[sid]
        else:
            hindi[sid] = [tr(l) for l in lines]
    B.emit(src, hindi, B.OUT / CH)


if __name__ == "__main__":
    main()
