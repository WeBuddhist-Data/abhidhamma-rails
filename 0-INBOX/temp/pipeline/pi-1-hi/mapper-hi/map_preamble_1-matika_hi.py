"""Map the preamble and 1-matika keywords to the Hindi translation.

usage: python -I -X utf8 map_preamble_1-matika_hi.py
The matrix is mapped line by line (MAP below, one entry per segment: kw=value | kw=value ...);
G() fills the eight 'cluster' (gocchaka) segments that share one shape.
Also exposes MATRIX_NAMES (matrix item names) for reuse by later parts.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import build_part, verify  # noqa: E402

MAP_PREAMBLE = """
0 | Abhidhamma=अभिधम्म | Abhidhammapiṭake=अभिधम्म पिटक
1-0 | saṅgaṇī=गणना | Dhammasaṅgaṇī=परिघटनाओं की गणना | Dhamma=परिघटना
T-1 | sambuddhassa=जागृत बुद्ध | bhagavato=भगवान | sammā=पूर्ण रूप से | sammāsambuddhassa=पूर्ण रूप से जागृत बुद्ध | Namo=नमन | arahato=अर्हत्
"""

P = "परिघटना"
MAP_MATIKA = f"""
1-M-0 | Mātikā=मूल सूची
1-M-1-0 | mātikā=सूची
1-M-2-0 | mātikā=सूची | Duka=दो-दो के वर्गीकरण
1-M-2-1-0 | Hetu=मूल
1-M-2-2-0 | antara=बीच का | antaradukaṃ=बीच के … दो-दो के वर्गीकरण | dukaṃ=दो-दो के वर्गीकरण
1-M-2-3-0 | Āsava=मन के मैल
1-M-2-4-0 | Saṃyojana=बंधन
1-M-2-5-0 | Gantha=गाँठ
1-M-2-6-0 | Ogha=बाढ़
1-M-2-7-0 | Yoga=जकड़न
1-M-2-8-0 | Nīvaraṇa=बाधा
1-M-2-9-0 | Parāmāsa=ग़लत धारणा
1-M-2-10-0 | antara=बीच का | antaradukaṃ=बीच के … दो-दो के वर्गीकरण | dukaṃ=दो-दो के वर्गीकरण
1-M-2-11-0 | Upādāna=आसक्ति
1-M-2-12-0 | Kilesa=मन के क्लेश
1-M-2-13-0 | Piṭṭhi=अंतिम | dukaṃ=दो-दो के वर्गीकरण
1-M-2-14-0 | Suttantika=उपदेश | mātikā=सूची | duka=दो-दो के वर्गीकरण
1-M1-1 | abyākatā=नैतिक रूप से अनिर्धारित | abyākatā dhammā=नैतिक रूप से अनिर्धारित {P} | akusalā=हानिकर | akusalā dhammā=हानिकर {P} | kusalā=हितकर | kusalā dhammā=हितकर {P}
1-M1-2 | sampayuttā=जुड़ा | vedanāya=अनुभूति | dukkhāya=दुःखद | dukkhāya vedanāya=दुःखद अनुभूति | adukkhamasukhāya=न दुःखद न सुखद | sukhāya=सुखद | sukhāya vedanāya=सुखद अनुभूति
1-M1-3 | vipākadhamma=कर्म-फल उत्पन्न करने वाला | vipākadhammadhammā=कर्म-फल उत्पन्न करने वाली {P}
1-M1-4 | upādiṇṇupādāniyā=कर्म से उत्पन्न और आसक्ति का विषय बनने वाला | anupādiṇṇupādāniyā=कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला | upādāniyā=आसक्ति का विषय बनने वाला | upādiṇṇa=कर्म से उत्पन्न | anupādiṇṇaanupādāniyā dhammā=न कर्म से उत्पन्न न आसक्ति का विषय बनने वाली {P} | anupādiṇṇupādāniyā dhammā=कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली {P} | upādiṇṇupādāniyā dhammā=कर्म से उत्पन्न और आसक्ति का विषय बनने वाली {P}
1-M1-5 | saṃkiliṭṭha=क्लेशों से मलिन | saṃkilesikā=क्लेशों की ओर ले जाने वाला | asaṃkiliṭṭha=क्लेशों से मलिन न होने वाला
1-M1-6 | vitakka=आरंभिक विचार | savitakkasavicārā dhammā=आरंभिक विचार और सतत विचार वाली {P} | avitakkavicāramattā dhammā=आरंभिक विचार से रहित केवल सतत विचार वाली {P} | vicāra=सतत विचार
1-M1-7 | sahagatā=के साथ होने वाला | upekkhāsahagatā=समभाव के साथ होने वाला | sukhasahagatā=सुख के साथ होने वाला | pītisahagatā=उल्लास के साथ होने वाला | upekkhā=समभाव | sukha=सुख | pīti=उल्लास | sahagatā dhammā=के साथ होने वाली {P}
1-M1-8 | pahātabbā=छोड़ा जाने वाला | bhāvanāya pahātabbā=मानसिक अभ्यास से छोड़ा जाने वाला | dassanena=सत्य-दर्शन
1-M1-9 | pahātabba=छोड़ा जाने वाला | bhāvanāya pahātabba=मानसिक अभ्यास से छोड़ा जाने वाला | hetukā=मूलों वाला | dassanena=सत्य-दर्शन | hetukā dhammā=मूलों वाली {P}
1-M1-10 | ācaya=संचय | apacaya=संचय घटाना | gāmino dhammā=की ओर ले जाने वाली {P}
1-M1-11 | asekkhā=सीखना पूरा होने के चरण का | sekkhā=सीखने के चरण का
1-M1-12 | mahaggatā=उन्नत | mahaggatā dhammā=उन्नत {P} | appamāṇā=अपरिमित | appamāṇā dhammā=अपरिमित {P} | parittā=सीमित | parittā dhammā=सीमित {P}
1-M1-13 | mahaggata=उन्नत | mahaggatārammaṇā=उन्नत विषय वाला | appamāṇa=अपरिमित | appamāṇārammaṇā=अपरिमित विषय वाला | paritta=सीमित | parittārammaṇā=सीमित विषय वाला | ārammaṇā=विषय वाला
1-M1-14 | hīnā=हीन | hīnā dhammā=हीन {P} | majjhimā=मध्यम | majjhimā dhammā=मध्यम {P} | paṇītā=उत्तम | paṇītā dhammā=उत्तम {P}
1-M1-15 | niyatā=निश्चित | sammatta=सही दिशा | niyatā dhammā=निश्चित {P} | micchatta=ग़लत दिशा
1-M1-16 | adhipatino=प्रधानता वाला | ārammaṇā=विषय बनाने वाला | magga=मार्ग | hetukā=मूल बनाने वाला
1-M1-17 | uppādino=उत्पन्न होने वाला | uppannā=उत्पन्न हो चुका | uppannā dhammā=उत्पन्न हो चुकी {P}
1-M1-18 | anāgatā dhammā=भविष्य की {P} | atītā dhammā=अतीत की {P} | paccuppannā dhammā=वर्तमान की {P}
1-M1-19 | anāgatārammaṇā=भविष्य के विषय वाला | ārammaṇā=विषय वाला | atītārammaṇā=अतीत के विषय वाला | paccuppannārammaṇā=वर्तमान के विषय वाला
1-M1-20 | bahiddhā=दूसरों से संबंधित | bahiddhā dhammā=दूसरों से संबंधित {P}
1-M1-21 | ārammaṇā=विषय वाला | bahiddhā=दूसरों से संबंधित
1-M1-22 | anidassana=दिखाई न देने वाला | sappaṭighā=टकराव वाला | mātikā=सूची | sanidassana=दिखाई देने वाला
1-M2-1 | hetū=मूल
1-M2-2 | hetukā=मूल वाला | sahetukā dhammā=मूल वाली {P} | ahetukā dhammā=मूल से रहित {P}
1-M2-3 | sampayuttā=जुड़ा | vippayuttā=अलग | hetu=मूल | vippayuttā dhammā=अलग {P}
1-M2-4 | hetū=मूल
1-M2-5 | sampayuttā=जुड़ा | hetū=मूल
1-M2-6 | hetū=मूल
1-M2-7 | appaccayā dhammā=कारणों पर निर्भर न रहने वाली {P}
1-M2-8 | saṅkhatā=निर्मित | saṅkhatā dhammā=निर्मित {P} | asaṅkhatā=अनिर्मित | asaṅkhatā dhammā=अनिर्मित {P}
1-M2-9 | anidassanā=दिखाई न देने वाला | anidassanā dhammā=दिखाई न देने वाली {P} | sanidassanā=दिखाई देने वाला | sanidassanā dhammā=दिखाई देने वाली {P}
1-M2-10 | sappaṭighā=टकराव वाला | sappaṭighā dhammā=टकराव वाली {P}
1-M2-11 | arūpino=अभौतिक | arūpino dhammā=अभौतिक {P} | rūpino=भौतिक | rūpino dhammā=भौतिक {P}
1-M2-12 | lokuttarā dhammā=लोकोत्तर {P} | uttarā=लोकोत्तर | lokiyā=लौकिक | lokiyā dhammā=लौकिक {P}
1-M2-13 | na=न | antara=बीच का | antaradukaṃ=बीच के … दो-दो के वर्गीकरण | viññeyyā=जाना जा सकने वाला | dukaṃ=दो-दो के वर्गीकरण
1-M2-55 | ārammaṇā=विषय वाला
1-M2-56 | cittā=मन
1-M2-57 | cetasikā=मन का सहचर
1-M2-58 | sampayuttā=जुड़ा | vippayuttā=अलग | cittavippayuttā=मन से अलग | citta=मन | vippayuttā dhammā=अलग {P}
1-M2-59 | saṃsaṭṭhā=घुला-मिला | cittasaṃsaṭṭhā=मन से घुला-मिला | citta=मन | saṃsaṭṭhā dhammā=घुली-मिली {P} | visaṃsaṭṭhā dhammā=घुली-मिली न होने वाली {P}
1-M2-60 | samuṭṭhānā=उत्पन्न | cittasamuṭṭhānā=मन से उत्पन्न | citta=मन | samuṭṭhānā dhammā=उत्पन्न {P} | no cittasamuṭṭhānā dhammā=मन से उत्पन्न न होने वाली {P}
1-M2-61 | cittasahabhuno=मन के साथ-साथ होने वाला | citta=मन | cittasahabhuno dhammā=मन के साथ-साथ होने वाली {P} | no cittasahabhuno dhammā=मन के साथ-साथ न होने वाली {P}
1-M2-62 | anuparivattino=अनुसरण करने वाला | cittānuparivattino=मन का अनुसरण करने वाला | citta=मन | anuparivattino dhammā=अनुसरण करने वाली {P} | cittānuparivattino dhammā=मन का अनुसरण करने वाली {P} | no cittānuparivattino dhammā=मन का अनुसरण न करने वाली {P}
1-M2-63 | samuṭṭhānā=उत्पन्न | cittasaṃsaṭṭhasamuṭṭhānā=मन से घुला-मिला और मन से उत्पन्न | saṃsaṭṭha=घुला-मिला | citta=मन | saṃsaṭṭhasamuṭṭhānā dhammā=घुली-मिली और मन से उत्पन्न {P} | no cittasaṃsaṭṭhasamuṭṭhānā dhammā=ऐसी {P} जो मन से घुली-मिली और मन से उत्पन्न नहीं है
1-M2-64 | samuṭṭhāna=उत्पन्न | sahabhuno=साथ-साथ होने वाला | saṃsaṭṭha=घुला-मिला | citta=मन | saṃsaṭṭhasamuṭṭhānasahabhuno dhammā=घुली-मिली मन से उत्पन्न और मन के साथ-साथ होने वाली {P} | no cittasaṃsaṭṭhasamuṭṭhānasahabhuno dhammā=ऐसी {P} जो मन से घुली-मिली मन से उत्पन्न और मन के साथ-साथ होने वाली नहीं है
1-M2-65 | anuparivattino=अनुसरण करने वाला | cittasaṃsaṭṭhasamuṭṭhānānuparivattino=मन से घुला-मिला मन से उत्पन्न और मन का अनुसरण करने वाला | samuṭṭhāna=उत्पन्न | saṃsaṭṭha=घुला-मिला | citta=मन | saṃsaṭṭhasamuṭṭhānānuparivattino dhammā=घुली-मिली मन से उत्पन्न और मन का अनुसरण करने वाली {P} | no cittasaṃsaṭṭhasamuṭṭhānānuparivattino dhammā=ऐसी {P} जो मन से घुली-मिली मन से उत्पन्न और मन का अनुसरण करने वाली नहीं है
1-M2-66 | bāhirā=बाह्य | bāhirā dhammā=बाह्य {P} | ajjhattikā=आंतरिक | ajjhattikā dhammā=आंतरिक {P}
1-M2-67 | upādā=व्युत्पन्न | upādā dhammā=व्युत्पन्न {P}
1-M2-68 | antara=बीच का | antaradukaṃ=बीच के … दो-दो के वर्गीकरण | dukaṃ=दो-दो के वर्गीकरण | upādiṇṇā=कर्म से उत्पन्न | anupādiṇṇā dhammā=कर्म से उत्पन्न न होने वाली {P} | upādiṇṇā dhammā=कर्म से उत्पन्न {P}
1-M2-75 | kilesā=मन के क्लेश
1-M2-76 | saṃkilesikā=क्लेशों की ओर ले जाने वाला | asaṃkilesikā dhammā=क्लेशों की ओर न ले जाने वाली {P} | saṃkilesikā dhammā=क्लेशों की ओर ले जाने वाली {P}
1-M2-77 | saṃkiliṭṭhā=क्लेशों से मलिन | saṃkiliṭṭhā dhammā=क्लेशों से मलिन {P} | asaṃkiliṭṭhā=क्लेशों से मलिन न होने वाला | asaṃkiliṭṭhā dhammā=क्लेशों से मलिन न होने वाली {P}
1-M2-78 | sampayuttā=जुड़ा | kilesa=क्लेश | vippayuttā=अलग | kilesavippayuttā=क्लेशों से अलग | vippayuttā dhammā=अलग {P}
1-M2-79 | saṃkilesikā=क्लेशों की ओर ले जाने वाला | kilesā=मन के क्लेश
1-M2-80 | saṃkiliṭṭhā=क्लेशों से मलिन | kilesā=मन के क्लेश
1-M2-81 | sampayuttā=जुड़ा | kilesā=मन के क्लेश
1-M2-82 | saṃkilesikā=क्लेशों की ओर ले जाने वाला | kilesa=क्लेश | kilesavippayuttā=क्लेशों से अलग | vippayuttā=अलग | dhammā={P}
1-M2-83 | pahātabbā=छोड़ा जाने वाला | dassanena=सत्य-दर्शन
1-M2-84 | pahātabbā=छोड़ा जाने वाला | bhāvanāya pahātabbā=मानसिक अभ्यास से छोड़ा जाने वाला
1-M2-85 | pahātabba=छोड़ा जाने वाला | hetukā=मूलों वाला | dassanena=सत्य-दर्शन | hetukā dhammā=मूलों वाली {P}
1-M2-86 | pahātabba=छोड़ा जाने वाला | bhāvanāya pahātabba=मानसिक अभ्यास से छोड़ा जाने वाला | hetukā=मूलों वाला | hetukā dhammā=मूलों वाली {P}
1-M2-87 | vitakkā=आरंभिक विचार | savitakkā dhammā=आरंभिक विचार वाली {P} | avitakkā dhammā=आरंभिक विचार से रहित {P}
1-M2-88 | savicārā dhammā=सतत विचार वाली {P} | avicārā dhammā=सतत विचार से रहित {P} | vicārā=सतत विचार
1-M2-89 | pītikā=उल्लास वाला | sappītikā dhammā=उल्लास वाली {P} | appītikā dhammā=उल्लास से रहित {P}
1-M2-90 | sahagatā=के साथ होने वाला | pītisahagatā=उल्लास के साथ होने वाला | pīti=उल्लास | sahagatā dhammā=के साथ होने वाली {P} | na pītisahagatā dhammā=उल्लास के साथ न होने वाली {P}
1-M2-91 | sahagatā=के साथ होने वाला | sukhasahagatā=सुख के साथ होने वाला | sukha=सुख | sahagatā dhammā=के साथ होने वाली {P} | na sukhasahagatā dhammā=सुख के साथ न होने वाली {P}
1-M2-92 | sahagatā=के साथ होने वाला | upekkhāsahagatā=समभाव के साथ होने वाला | upekkhā=समभाव | sahagatā dhammā=के साथ होने वाली {P} | na upekkhāsahagatā dhammā=समभाव के साथ न होने वाली {P}
1-M2-93 | kāma=इंद्रिय-सुख | kāmāvacarā=इंद्रिय-सुखों के लोक से संबंधित | avacarā=लोक से संबंधित
1-M2-94 | rūpa=सूक्ष्म भौतिक | rūpāvacarā=सूक्ष्म भौतिक लोक से संबंधित | avacarā=लोक से संबंधित
1-M2-95 | arūpa=अभौतिक | arūpāvacarā=अभौतिक लोक से संबंधित | avacarā=लोक से संबंधित
1-M2-96 | pariyāpannā dhammā=अस्तित्व के लोकों में समाई हुई {P} | apariyāpannā dhammā=अस्तित्व के लोकों में न समाई हुई {P}
1-M2-97 | niyyānikā=मुक्ति की ओर ले जाने वाला | niyyānikā dhammā=मुक्ति की ओर ले जाने वाली {P}
1-M2-98 | niyatā=निश्चित | niyatā dhammā=निश्चित {P}
1-M2-99 | sauttarā=सर्वोच्च न होने वाला | sauttarā dhammā=सर्वोच्च न होने वाली {P} | anuttarā=सर्वोच्च | anuttarā dhammā=सर्वोच्च {P}
1-M2-100 | Abhidhamma=अभिधम्म | Piṭṭhi=अंतिम | raṇā=संघर्ष | mātikā=सूची | dukaṃ=दो-दो के वर्गीकरण | saraṇā dhammā=संघर्ष वाली {P} | araṇā dhammā=संघर्ष से रहित {P}
1-M2-101 | avijjā=अज्ञान | vijjā=विद्या | bhāgino dhammā=भागी {P}
1-M2-102 | vajira=वज्र | vijju=बिजली | upamā=जैसा | vijjūpamā dhammā=बिजली जैसी {P}
1-M2-103 | bālā=मूर्खतापूर्ण | bālā dhammā=मूर्खतापूर्ण {P} | paṇḍitā=बुद्धिमत्तापूर्ण | paṇḍitā dhammā=बुद्धिमत्तापूर्ण {P}
1-M2-104 | sukkā=उजला | sukkā dhammā=उजली {P} | kaṇhā=काला | kaṇhā dhammā=काली {P}
1-M2-105 | tapanīyā=संताप देने वाला
1-M2-106 | adhivacanā=नाम | pathā=मार्ग
1-M2-107 | nirutti=अभिव्यक्ति | pathā=मार्ग
1-M2-108 | paññatti=नामकरण | pathā=मार्ग
1-M2-109 | rūpañca=भौतिक रूप | nāmañca=मानसिक पक्ष
1-M2-110 | bhava=अस्तित्व | taṇhā=तृष्णा | avijjā=अज्ञान
1-M2-111 | bhava=अस्तित्व | vibhava=अनस्तित्व | diṭṭhi=दृष्टि
1-M2-112 | uccheda=विनाश | ucchedadiṭṭhi=विनाश की दृष्टि | sassata=शाश्वतता | sassatadiṭṭhi=शाश्वतता की दृष्टि | diṭṭhi=दृष्टि
1-M2-113 | diṭṭhi=दृष्टि
1-M2-114 | anudiṭṭhi=के बारे में दृष्टि | diṭṭhi=दृष्टि
1-M2-115 | anottappañca=बुराई के प्रति निडरता | ahirikañca=निर्लज्जता
1-M2-116 | ottappañca=बुराई का डर | hirī=लज्जा
1-M2-117 | pāpa=बुरा | vacassatā=सलाह मानने की प्रवृत्ति | mittatā=मित्रों की संगति | dovacassatā=सलाह न मानने की प्रवृत्ति
1-M2-118 | vacassatā=सलाह मानने की प्रवृत्ति | sovacassatā=सलाह मानने की प्रवृत्ति | mittatā=मित्रों की संगति
1-M2-119 | vuṭṭhāna=उबरना | āpatti=दोष | kusalatā=कुशलता | vuṭṭhānakusalatā=उबरने में कुशलता
1-M2-120 | samāpatti=ध्यान-अवस्था | vuṭṭhāna=बाहर आना | kusalatā=कुशलता | vuṭṭhānakusalatā=बाहर आने में कुशलता
1-M2-121 | manasikāra=मनोयोग | dhātu=तत्व | kusalatā=कुशलता | manasikārakusalatā=मनोयोग के विषय में कुशलता
1-M2-122 | āyatana=इंद्रिय-क्षेत्र | paṭicca=परस्पर-आश्रित | samuppāda=उत्पत्ति | kusalatā=कुशलता
1-M2-123 | aṭṭhāna=असंभव बात | kusalatā=कुशलता
1-M2-124 | maddavo=कोमलता | ajjavo=सरलता
1-M2-125 | soraccañca=सौम्यता | khanti=सहनशीलता
1-M2-126 | sākhalyañca=मधुर व्यवहार | paṭisanthāro=आदर-सत्कार
1-M2-127 | dvāratā=द्वार | bhojane=भोजन | gutta=रक्षा करना | mattaññutā=मात्रा का ज्ञान | indriyesu=इंद्रिय
1-M2-128 | dvāratā=द्वार | bhojane=भोजन | gutta=रक्षा करना | mattaññutā=मात्रा का ज्ञान | indriyesu=इंद्रिय
1-M2-129 | sampajaññañca=स्पष्ट समझ | muṭṭhasaccañca=सजगता की कमी | asampajaññañca=स्पष्ट समझ का अभाव
1-M2-130 | sampajaññañca=स्पष्ट समझ | sati=सजगता
1-M2-131 | balañca=बल | paṭisaṅkhāna=सोच-विचार
1-M2-132 | samatho=शांति | vipassanā=अंतर्दृष्टि
1-M2-133 | samatha=शांति | paggāha=तत्परता | nimittañca=चिह्न
1-M2-134 | paggāho=तत्परता | avikkhepo=भटकाव का अभाव
1-M2-135 | vipatti=विफलता | sīla=सदाचार | diṭṭhi=दृष्टि
1-M2-136 | sampadā=संपन्नता | sīla=सदाचार | diṭṭhi=दृष्टि
1-M2-137 | sīla=सदाचार | visuddhi=शुद्धि | diṭṭhi=दृष्टि
1-M2-138 | padhānaṃ=प्रयास | yathā=के अनुरूप | visuddhi=शुद्धि | diṭṭhi=दृष्टि
1-M2-139 | padhānaṃ=प्रयास | saṃvego=मन का झकझोरा जाना | saṃvejaniyesu=झकझोर देने वाला | saṃviggassa=झकझोरा गया व्यक्ति | ṭhānesu=बात | yoniso=उचित ढंग से
1-M2-140 | santuṭṭhitā=संतुष्ट होना | padhānasmiṃ=प्रयास | kusalesu=हितकर | kusalesu dhammesu=हितकर {P}
1-M2-141 | vijjā=विद्या | vimutti=मुक्ति
1-M2-142 | niṭṭhitā=पूरा हुआ | khaye=क्षय | Suttantika=उपदेश | ñāṇaṃ=ज्ञान | mātikā=मूल सूची | anuppāde=उत्पन्न न होना | duka=दो-दो के वर्गीकरण
"""

# The eight clusters (gocchaka) of the matrix share one shape. Per cluster:
# (Pāli stem, Pāli -niya adjective, Hindi term as named in the «X रूपी» items, Hindi plural oblique base,
#  pronoun used in the closing pair, first ID number)
CLUSTERS = [
    ("āsava", None, "मन के मैल", "मन के मैलों", "उनका", 14),
    ("saṃyojana", "saṃyojaniyā", "बंधन", "बंधनों", "उनका", 20),
    ("gantha", "ganthaniyā", "गाँठ", "गाँठों", "उनका", 26),
    ("ogha", "oghaniyā", "बाढ़", "बाढ़ों", "उनका", 32),
    ("yoga", "yoganiyā", "जकड़न", "जकड़नों", "उनका", 38),
    ("nīvaraṇa", "nīvaraṇiyā", "बाधा", "बाधाओं", "उनका", 44),
    ("parāmāsa", "parāmaṭṭhā", "ग़लत धारणा", "ग़लत धारणा", "उसका", 50),
    ("upādāna", "upādāniyā", "आसक्ति", "आसक्ति", "उसका", 69),
]


def cluster_maps():
    """Per-segment dicts for the cluster segments (keywords not listed here fall to MAP_MATIKA)."""
    out = {}
    for stem, niya, term, obl, pron, n in CLUSTERS:
        obj = f"{obl} का विषय बनने वाला"
        obj_f = f"{obl} का विषय बनने वाली {P}"
        neg_f = f"{obl} का विषय न बनने वाली {P}"
        if stem == "āsava":
            # sāsava / anāsava instead of -niya
            pos, neg = "sāsavā", "anāsavā"
        else:
            pos, neg = niya, ("an" + niya if niya[0] in "aāiīuūeo" else "a" + niya)
        d = {
            stem[:-1] + "ā": term, stem: term,
            pos: obj, f"{pos} dhammā": obj_f, f"{neg} dhammā": neg_f,
            neg: f"{obl} का विषय न बनने वाला",
            "sampayuttā": "जुड़ा", "vippayuttā": "अलग", f"{stem}vippayuttā": f"{obl} से अलग",
            "vippayuttā dhammā": f"अलग {P}", "dhammā": P,
        }
        ids = [f"1-M2-{n + i}" for i in range(6 if stem != "parāmāsa" else 5)]
        for bid in ids:
            out[bid] = dict(d)
        # closing pair: «X से अलग, पर उनका/उसका विषय बनने वाली / और उनका/उसका विषय न बनने वाली»
        last = ids[-1]
        out[last][pos] = f"{pron} विषय बनने वाला"
        out[last][neg] = f"{pron} विषय न बनने वाला"
    return out


def parse(block):
    m = {}
    for line in block.strip().splitlines():
        bid, *pairs = [x.strip() for x in line.split(" | ")]
        d = {}
        for p in pairs:
            k, v = p.split("=", 1)
            d[k] = v
        m[bid] = d
    return m


PRE = parse(MAP_PREAMBLE)
MAT = parse(MAP_MATIKA)
CL = cluster_maps()


def resolver_pre(bid, kw, kws):
    return PRE[bid][kw]


def resolver_mat(bid, kw, kws):
    if bid in MAT and kw in MAT[bid]:
        return MAT[bid][kw]
    return CL[bid][kw]


# matrix item names for reuse (Pāli matrix keyword -> Hindi), e.g. in 3-01 / 4-0x / 5
MATRIX_NAMES = {}
for _d in list(MAT.values()) + list(CL.values()):
    for _k, _v in _d.items():
        MATRIX_NAMES.setdefault(_k, _v)

if __name__ == "__main__":
    build_part("preamble", resolver_pre)
    verify("preamble")
    build_part("1-matika", resolver_mat)
    verify("1-matika")
