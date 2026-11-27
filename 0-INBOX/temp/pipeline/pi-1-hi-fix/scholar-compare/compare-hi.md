# Hindi pi-1 (plain) vs the English scholarly version: Mātikā (164 lines)

Input: `scholar-compare/side-by-side.jsonl`. Pāli checked against the vault commentary `1-SOURCES/Commentaries/pi-dhammasangani-atthakatha.md` (block IDs cited as comm. ^1-NNN), the scholarly termbase `pali-english/audience_requirments/termbase/termbase-pi-1-audience_scholarly.md` and the Hindi termbase `AI_translation/hindi/pi-1-pali-hindi-termbase-plain.md`. Read-only check: no translation file was changed.

## 1. Summary

| Verdict | Lines |
|---|---|
| `SAME` | 88 |
| `PLAINER` | 25 |
| `DIFFERS-HINDI` | 1 |
| `DIFFERS-ENGLISH` | 48 |
| `DIFFERS-BOTH-OK` | 2 |
| `MISSING` | 0 |
| `ADDED` | 0 |
| **Total** | 164 |

**Does the Hindi say the same as the scholar version?** Mostly yes, and where it does not, the Hindi is usually the one that matches the Pāli and the commentary. 113 of 164 lines say the same thing (88 SAME, 25 only plainer wording, as plain.md expects). Of the 51 lines whose meaning differs, 48 are errors in the English scholarly version, 2 are two defensible readings, and only 1 needs a fix in the Hindi: the third member of the *pahātabbahetuka* triad (1-M1-9 (ग)), where the Hindi takes the very reading the commentary rejects. Nothing is missing from or added to the Hindi.

The Hindi keeps every distinction the brief names: *sappaccaya* (कारणों पर निर्भर) vs *saṅkhata* (निर्मित); *sanidassana* (दिखाई देने वाली) vs *sappaṭigha* (टकराव वाली); *upādinna* (कर्म से उत्पन्न) vs *upādāniya* (आसक्ति का विषय); *āsava* (मन के मैल) vs *sāsava* (मन के मैलों का विषय); *hetu* (मूल रूपी) vs *sahetuka* (मूल वाली). It also keeps *aniyata* (अनिश्चित) apart from *abyākata* (नैतिक रूप से अनिर्धारित), *dassana* (सत्य-दर्शन) apart from *vipassanā* (अंतर्दृष्टि), and *ajjhatta* (स्वयं से संबंधित) apart from *ajjhattika* (आंतरिक). The English merges each of these last three pairs into one word.

## 2. Table, every line

Short forms: the trailing *dhammā* / 'phenomena' / परिघटनाएँ and the variant-reading brackets are dropped; members are separated by ` / `.

| ref | verdict | Pāli (short) | English scholarly (short) | Hindi (short) | note |
|---|---|---|---|---|---|
| 1-M1-1 | `PLAINER` | kusalā / akusalā / abyākatā | wholesome / unwholesome / indeterminate | हितकर / हानिकर / नैतिक रूप से अनिर्धारित | kusala/akusala → हितकर/हानिकर; abyākata 'indeterminate' → नैतिक रूप से अनिर्धारित (explained) |
| 1-M1-2 | `SAME` | sukhāya vedanāya sampayuttā / dukkhāya vedanāya sampayuttā / adukkhamasukhāya vedanāya sampayuttā | associated with pleasant feeling / associated with painful feeling / associated with neutral feeling | सुखद अनुभूति से जुड़ी / दुःखद अनुभूति से जुड़ी / न दुःखद, न सुखद अनुभूति से जुड़ी | Hindi gives adukkhamasukha literally (न दुःखद, न सुखद); English 'neutral' |
| 1-M1-3 | `DIFFERS-ENGLISH` | vipākā / vipākadhammadhammā / nevavipākanavipākadhammadhammā | resultant / resultant-state / neither resultant nor resultant-state | कर्म-फल रूपी / कर्म-फल उत्पन्न करने वाली / न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली | vipākadhammadhammā = having the nature to produce results (comm. ^1-522 vipākajanakaṭṭhena). English 'resultant-state' reads as another kind of result; Hindi 'कर्म-फल उत्पन्न करने वाली' is right |
| 1-M1-4 | `DIFFERS-ENGLISH` | upādiṇṇupādāniyā / anupādiṇṇupādāniyā / anupādiṇṇaanupādāniyā | grasped, appropriable / ungrasped, non-appropriable / ungrasped, non-appropriable | कर्म से उत्पन्न और आसक्ति का विषय बनने वाली / कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली / न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली | English (B) 'ungrasped, non-appropriable' is wrong (Pāli anupādiṇṇ-**upādāniyā**) and duplicates (C). Hindi (ख) correct. upādiṇṇa → कर्म से उत्पन्न is a plain gloss (comm. ^1-523 kammunā ādinnā) |
| 1-M1-5 | `DIFFERS-ENGLISH` | saṃkiliṭṭhasaṃkilesikā / asaṃkiliṭṭhasaṃkilesikā / asaṃkiliṭṭhaasaṃkilesikā | defiled, defiling / undefiled, non-defiling / undefiled, non-defiling | क्लेशों से मलिन और क्लेशों का विषय बनने वाली / क्लेशों से मलिन न होने वाली, पर क्लेशों का विषय बनने वाली / क्लेशों से मलिन न होने वाली और क्लेशों का विषय न बनने वाली | English (B) 'undefiled, non-defiling' is wrong (Pāli asaṃkiliṭṭha-**saṃkilesikā**), duplicates (C). Hindi (ख) correct; saṃkilesika = object of defilement (comm. ^1-524) |
| 1-M1-6 | `SAME` | savitakkasavicārā / avitakkavicāramattā / avitakkaavicārā | with initial and sustained application / with sustained application only / without initial or sustained application | आरंभिक विचार और सतत विचार वाली / आरंभिक विचार से रहित, केवल सतत विचार वाली / आरंभिक विचार और सतत विचार दोनों से रहित | vitakka/vicāra → आरंभिक/सतत विचार |
| 1-M1-7 | `SAME` | pītisahagatā / sukhasahagatā / upekkhāsahagatā | accompanied by rapture / accompanied by pleasure / accompanied by equanimity | उल्लास के साथ होने वाली / सुख के साथ होने वाली / समभाव के साथ होने वाली |  |
| 1-M1-8 | `PLAINER` | dassanena pahātabbā / bhāvanāya pahātabbā / neva dassanena na bhāvanāya pahātabbā | abandoned by insight / abandoned by cultivation / abandoned by neither insight nor cultivation | सत्य-दर्शन से छोड़ी जाने वाली / मानसिक अभ्यास से छोड़ी जाने वाली / न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली | bhāvanā 'cultivation' → मानसिक अभ्यास; dassana → सत्य-दर्शन (comm. ^1-527: dassana = first path). English 'insight' collides with vipassanā at 1-M2-132 |
| 1-M1-9 | `DIFFERS-HINDI` | dassanena pahātabbahetukā / bhāvanāya pahātabbahetukā / neva dassanena na bhāvanāya pahātabbahetukā | that are factors for abandonment through insight / that are factors for abandonment through cultivation / that are factors for abandonment through neither insight nor cultivation | सत्य-दर्शन से छोड़े जाने वाले मूलों वाली / मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली / न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली | (क)(ख) Hindi right, English 'factors for abandonment' wrong (pahātabba-hetukā = having roots to be abandoned). (ग) Hindi takes the reading comm. ^1-528 rejects; see Fixes. English (C) also wrong |
| 1-M1-10 | `SAME` | ācayagāmino / apacayagāmino / nevācayagāmināpacayagāmino | tending toward growth / tending toward decline / tending toward neither growth nor decline | संचय की ओर ले जाने वाली / संचय घटाने की ओर ले जाने वाली / न संचय की ओर, न संचय घटाने की ओर ले जाने वाली | ācaya/apacaya: English growth/decline, Hindi संचय / संचय घटाना; both fit comm. ^1-529 |
| 1-M1-11 | `PLAINER` | sekkhā / asekkhā / nevasekkhanāsekkhā | trainee / adept / neither trainee nor adept | सीखने के चरण की / सीखना पूरा होने के चरण की / न सीखने के चरण की, न सीखना पूरा होने के चरण की | sekkha/asekkha 'trainee/adept' → सीखने के चरण / सीखना पूरा होने के चरण |
| 1-M1-12 | `SAME` | parittā / mahaggatā / appamāṇā | limited / exalted / immeasurable | सीमित / उन्नत / अपरिमित |  |
| 1-M1-13 | `SAME` | parittārammaṇā / mahaggatārammaṇā / appamāṇārammaṇā | with limited object / with exalted object / with immeasurable object | सीमित विषय वाली / उन्नत विषय वाली / अपरिमित विषय वाली |  |
| 1-M1-14 | `SAME` | hīnā / majjhimā / paṇītā | inferior / middle / superior | हीन / मध्यम / उत्तम |  |
| 1-M1-15 | `SAME` | micchattaniyatā / sammattaniyatā / aniyatā | determined as wrong / determined as right / indeterminate | ग़लत दिशा में निश्चित / सही दिशा में निश्चित / अनिश्चित | English uses 'indeterminate' for both aniyata (here) and abyākata (1-M1-1); Hindi keeps them apart (अनिश्चित / नैतिक रूप से अनिर्धारित) |
| 1-M1-16 | `DIFFERS-ENGLISH` | maggārammaṇā / maggahetukā / maggādhipatino | with path as object / that are path factors / that are path-dominant | मार्ग को विषय बनाने वाली / मार्ग को मूल बनाने वाली / मार्ग की प्रधानता वाली | maggahetukā = having the path as root/condition (comm. ^1-535). English 'path factors' is wrong; Hindi 'मार्ग को मूल बनाने वाली' fits |
| 1-M1-17 | `DIFFERS-ENGLISH` | uppannā / anuppannā / uppādino | arisen / not arisen / productive | उत्पन्न हो चुकी / उत्पन्न न हुई / उत्पन्न होने वाली | uppādino = bound to arise (comm. ^1-536 avassaṃ uppajjissanti). English 'productive' is wrong; Hindi 'उत्पन्न होने वाली' fits (optional: 'अवश्य उत्पन्न होने वाली') |
| 1-M1-18 | `SAME` | atītā / anāgatā / paccuppannā | past / future / present | अतीत की / भविष्य की / वर्तमान की |  |
| 1-M1-19 | `SAME` | atītārammaṇā / anāgatārammaṇā / paccuppannārammaṇā | with past object / with future object / with present object | अतीत के विषय वाली / भविष्य के विषय वाली / वर्तमान के विषय वाली |  |
| 1-M1-20 | `PLAINER` | ajjhattā / bahiddhā / ajjhattabahiddhā | internal / external / internal and external | स्वयं से संबंधित / दूसरों से संबंधित / स्वयं और दूसरों दोनों से संबंधित | ajjhatta 'internal' → स्वयं से संबंधित: Hindi gives the comm. sense (^1-539 niyakajjhatta, one's own) and keeps it apart from ajjhattika (1-M2-66 आंतरिक); English uses 'internal' for both |
| 1-M1-21 | `PLAINER` | ajjhattārammaṇā / bahiddhārammaṇā / ajjhattabahiddhārammaṇā | with internal object / with external object / with internal and external object | स्वयं से संबंधित विषय वाली / दूसरों से संबंधित विषय वाली / स्वयं और दूसरों दोनों से संबंधित विषय वाली | as 1-M1-20 |
| 1-M1-22 | `SAME` | sanidassanasappaṭighā / anidassanasappaṭighā / anidassanaappaṭighā / Tikamātikā | that are manifest with resistance / that are non-manifest with resistance / that are non-manifest without resistance / Triad Matrix | दिखाई देने वाली और टकराव वाली / दिखाई न देने वाली, पर टकराव वाली / दिखाई न देने वाली और टकराव से रहित / तीन-तीन के वर्गीकरणों की मूल सूची | sanidassana/sappaṭigha kept apart on both sides (manifest/resistance; दिखाई देने वाली/टकराव) |
| 1-M2-1 | `DIFFERS-ENGLISH` | hetū / na hetū | that are reasons / that are not reasons | मूल रूपी / मूल रूपी न होने वाली | hetu here = root (comm. ^1-543 mūlaṭṭhena). English 'reasons' (termbase sense 'because') is the wrong sense; Hindi मूल is right |
| 1-M2-2 | `DIFFERS-ENGLISH` | sahetukā / ahetukā | with a reason / without a reason | मूल वाली / मूल से रहित | hetu/sahetuka distinction kept on both sides, but English 'with a reason' carries the wrong sense of hetu (see 1-M2-1) |
| 1-M2-3 | `DIFFERS-ENGLISH` | hetusampayuttā / hetuvippayuttā | associated with a reason / disassociated from a reason | मूलों से जुड़ी / मूलों से अलग | as 1-M2-2 |
| 1-M2-4 | `DIFFERS-ENGLISH` | hetū ceva dhammā sahetukā ca / sahetukā ceva dhammā na ca hetū | that are both reasons and with a reason / with a reason that are not reasons | मूल रूपी भी और मूल वाली भी / मूल वाली, पर स्वयं मूल रूपी न होने वाली | as 1-M2-2; structure the same |
| 1-M2-5 | `DIFFERS-ENGLISH` | hetū ceva dhammā hetusampayuttā ca / hetusampayuttā ceva dhammā na ca hetū | that are both reasons and associated with a reason / associated with a reason that are not reasons | मूल रूपी भी और मूलों से जुड़ी भी / मूलों से जुड़ी, पर स्वयं मूल रूपी न होने वाली | as 1-M2-2; structure the same |
| 1-M2-6 | `DIFFERS-ENGLISH` | na hetū kho pana dhammā sahetukāpi / ahetukāpi / Hetugocchakaṃ | disassociated from a reason yet with a reason / disassociated from a reason / Cause Classification | मूल रूपी न होने वाली, पर मूल वाली / मूल रूपी न होने वाली और मूल से रहित / मूलों का वर्ग | Pāli 'na hetū … sahetukāpi / ahetukāpi' = not roots, with roots / rootless (comm. ^1-543). English 'disassociated from a reason' is wrong (that is hetuvippayutta); Hindi correct |
| 1-M2-7 | `PLAINER` | sappaccayā / appaccayā | with a condition / without a condition | कारणों पर निर्भर रहने वाली / कारणों पर निर्भर न रहने वाली | paccaya 'condition' → कारण; sappaccaya (कारणों पर निर्भर) kept apart from saṅkhata (निर्मित) |
| 1-M2-8 | `SAME` | saṅkhatā / asaṅkhatā | conditioned / unconditioned | निर्मित / अनिर्मित | saṅkhata → निर्मित; distinct from sappaccaya |
| 1-M2-9 | `SAME` | sanidassanā / anidassanā | manifest / non-manifest | दिखाई देने वाली / दिखाई न देने वाली |  |
| 1-M2-10 | `SAME` | sappaṭighā / appaṭighā | with resistance / without resistance | टकराव वाली / टकराव से रहित |  |
| 1-M2-11 | `SAME` | rūpino / arūpino | material / immaterial | भौतिक / अभौतिक |  |
| 1-M2-12 | `SAME` | lokiyā / lokuttarā | mundane / supramundane | लौकिक / लोकोत्तर |  |
| 1-M2-13 | `DIFFERS-ENGLISH` | kenaci viññeyyā / kenaci na viññeyyā / Cūḷantaradukaṃ | knowable by someone / unknowable by someone / Minor Dyadic Classification | किसी एक प्रकार के विज्ञान से जानी जा सकने वाली / किसी एक प्रकार के विज्ञान से न जानी जा सकने वाली / बीच के छोटे दो-दो के वर्गीकरण | kenaci = by some one of eye-consciousness etc. (comm. ^1-545). English 'by someone' (a person; termbase sense) is wrong; Hindi 'किसी एक प्रकार के विज्ञान से' is right |
| 1-M2-14 | `PLAINER` | āsavā / no āsavā | that are taints / that are not taints | मन के मैल रूपी / मन के मैल रूपी न होने वाली | āsava 'taints' → मन के मैल |
| 1-M2-15 | `DIFFERS-ENGLISH` | sāsavā / anāsavā | defiled / untainted | मन के मैलों का विषय बनने वाली / मन के मैलों का विषय न बनने वाली | sāsava = with taints that take it as object (comm. ^1-546). English 'defiled' (termbase) collides with saṃkiliṭṭha and does not match its own 'untainted'; Hindi right |
| 1-M2-16 | `PLAINER` | āsavasampayuttā / āsavavippayuttā | associated with taints / disassociated from taints | मन के मैलों से जुड़ी / मन के मैलों से अलग | āsava → मन के मैल |
| 1-M2-17 | `DIFFERS-ENGLISH` | āsavā ceva dhammā sāsavā ca / sāsavā ceva dhammā no ca āsavā | that are both taints and defiled / that are defiled and not taints | मन के मैल रूपी भी और मन के मैलों का विषय बनने वाली भी / मन के मैलों का विषय बनने वाली, पर स्वयं मन के मैल रूपी न होने वाली | English 'defiled' for sāsava (see 1-M2-15) |
| 1-M2-18 | `PLAINER` | āsavā ceva dhammā āsavasampayuttā ca / āsavasampayuttā ceva dhammā no ca āsavā | that are both taints and associated with taints / associated with taints that are not taints | मन के मैल रूपी भी और मन के मैलों से जुड़ी भी / मन के मैलों से जुड़ी, पर स्वयं मन के मैल रूपी न होने वाली | āsava → मन के मैल |
| 1-M2-19 | `DIFFERS-ENGLISH` | āsavavippayuttā kho pana dhammā sāsavāpi / anāsavāpi / Āsavagocchakaṃ | disassociated from taints yet defiled / disassociated from taints / Taint Classification | मन के मैलों से अलग, पर उनका विषय बनने वाली / मन के मैलों से अलग और उनका विषय न बनने वाली / मन के मैलों का वर्ग | English 'defiled' for sāsava (see 1-M2-15) |
| 1-M2-20 | `SAME` | saṃyojanā / no saṃyojanā | that are fetters / that are not fetters | बंधन रूपी / बंधन रूपी न होने वाली |  |
| 1-M2-21 | `DIFFERS-ENGLISH` | saṃyojaniyā / asaṃyojaniyā | fettering / non-fettering | बंधनों का विषय बनने वाली / बंधनों का विषय न बनने वाली | English active 'fettering' blurs saṃyojana / saṃyojaniya; comm. ^1-547: object of the fetters (ārammaṇapaccaya). Hindi follows comm. |
| 1-M2-22 | `SAME` | saṃyojanasampayuttā / saṃyojanavippayuttā | associated with fetters / disassociated from fetters | बंधनों से जुड़ी / बंधनों से अलग |  |
| 1-M2-23 | `DIFFERS-ENGLISH` | saṃyojanā ceva dhammā saṃyojaniyā ca / saṃyojaniyā ceva dhammā no ca saṃyojanā | that are both fetters and fettering / that are fettering and not fetters | बंधन रूपी भी और बंधनों का विषय बनने वाली भी / बंधनों का विषय बनने वाली, पर स्वयं बंधन रूपी न होने वाली | English 'both fetters and fettering' loses the distinction (see 1-M2-21) |
| 1-M2-24 | `SAME` | saṃyojanā ceva dhammā saṃyojanasampayuttā ca / saṃyojanasampayuttā ceva dhammā no ca saṃyojanā | that are both fetters and associated with fetters / associated with fetters that are not fetters | बंधन रूपी भी और बंधनों से जुड़ी भी / बंधनों से जुड़ी, पर स्वयं बंधन रूपी न होने वाली |  |
| 1-M2-25 | `DIFFERS-ENGLISH` | saṃyojanavippayuttā kho pana dhammā saṃyojaniyāpi / asaṃyojaniyāpi / Saṃyojanagocchakaṃ | disassociated from fetters yet fettering / disassociated from fetters / Fetter Classification | बंधनों से अलग, पर उनका विषय बनने वाली / बंधनों से अलग और उनका विषय न बनने वाली / बंधनों का वर्ग | English 'fettering' (see 1-M2-21) |
| 1-M2-26 | `SAME` | ganthā / no ganthā | that are knots / that are not knots | गाँठ रूपी / गाँठ रूपी न होने वाली |  |
| 1-M2-27 | `DIFFERS-ENGLISH` | ganthaniyā / aganthaniyā | knotting / non-knotting | गाँठों का विषय बनने वाली / गाँठों का विषय न बनने वाली | English 'knotting' as agent; comm. ^1-548: ganthaniyā = to be gone to by the knots by taking them as object. Hindi follows comm. |
| 1-M2-28 | `SAME` | ganthasampayuttā / ganthavippayuttā | associated with knots / disassociated from knots | गाँठों से जुड़ी / गाँठों से अलग |  |
| 1-M2-29 | `DIFFERS-ENGLISH` | ganthā ceva dhammā ganthaniyā ca / ganthaniyā ceva dhammā no ca ganthā | that are both knots and knotting / that are knotting and not knots | गाँठ रूपी भी और गाँठों का विषय बनने वाली भी / गाँठों का विषय बनने वाली, पर स्वयं गाँठ रूपी न होने वाली | English 'knotting' (see 1-M2-27) |
| 1-M2-30 | `SAME` | ganthā ceva dhammā ganthasampayuttā ca / ganthasampayuttā ceva dhammā no ca ganthā | that are both knots and associated with knots / associated with knots that are not knots | गाँठ रूपी भी और गाँठों से जुड़ी भी / गाँठों से जुड़ी, पर स्वयं गाँठ रूपी न होने वाली |  |
| 1-M2-31 | `DIFFERS-ENGLISH` | ganthavippayuttā kho pana dhammā ganthaniyāpi / aganthaniyāpi / Ganthagocchakaṃ | disassociated from knots yet knotting / disassociated from knots / Knot Classification | गाँठों से अलग, पर उनका विषय बनने वाली / गाँठों से अलग और उनका विषय न बनने वाली / गाँठों का वर्ग | English 'knotting' (see 1-M2-27) |
| 1-M2-32 | `SAME` | oghā / no oghā | that are floods / that are not floods | बाढ़ रूपी / बाढ़ रूपी न होने वाली |  |
| 1-M2-33 | `DIFFERS-ENGLISH` | oghaniyā / anoghaniyā | flood-producing / non-flood-producing | बाढ़ों का विषय बनने वाली / बाढ़ों का विषय न बनने वाली | oghaniyā = to be crossed by the floods by taking them as object (comm. ^1-549 oghānaṃ ārammaṇadhammā). English 'flood-producing' is wrong; Hindi right |
| 1-M2-34 | `SAME` | oghasampayuttā / oghavippayuttā | associated with floods / disassociated from floods | बाढ़ों से जुड़ी / बाढ़ों से अलग |  |
| 1-M2-35 | `DIFFERS-ENGLISH` | oghā ceva dhammā oghaniyā ca / oghaniyā ceva dhammā no ca oghā | that are both floods and flood-producing / that are flood-producing and not floods | बाढ़ रूपी भी और बाढ़ों का विषय बनने वाली भी / बाढ़ों का विषय बनने वाली, पर स्वयं बाढ़ रूपी न होने वाली | English 'flood-producing' (see 1-M2-33) |
| 1-M2-36 | `SAME` | oghā ceva dhammā oghasampayuttā ca / oghasampayuttā ceva dhammā no ca oghā | that are both floods and associated with floods / associated with floods that are not floods | बाढ़ रूपी भी और बाढ़ों से जुड़ी भी / बाढ़ों से जुड़ी, पर स्वयं बाढ़ रूपी न होने वाली |  |
| 1-M2-37 | `DIFFERS-ENGLISH` | oghavippayuttā kho pana dhammā oghaniyāpi / anoghaniyāpi / Oghagocchakaṃ | disassociated from floods yet flood-producing / disassociated from floods / Flood Classification | बाढ़ों से अलग, पर उनका विषय बनने वाली / बाढ़ों से अलग और उनका विषय न बनने वाली / बाढ़ों का वर्ग | English 'flood-producing' (see 1-M2-33) |
| 1-M2-38 | `SAME` | yogā / no yogā | that are yokes / that are not yokes | जकड़न रूपी / जकड़न रूपी न होने वाली | yoga 'yokes' → जकड़न |
| 1-M2-39 | `DIFFERS-ENGLISH` | yoganiyā / ayoganiyā | yoke-producing / non-yoke-producing | जकड़नों का विषय बनने वाली / जकड़नों का विषय न बनने वाली | yoganiyā like oghaniyā (comm. ^1-550): object of the yokes. English 'yoke-producing' wrong |
| 1-M2-40 | `SAME` | yogasampayuttā / yogavippayuttā | associated with yokes / disassociated from yokes | जकड़नों से जुड़ी / जकड़नों से अलग |  |
| 1-M2-41 | `DIFFERS-ENGLISH` | yogā ceva dhammā yoganiyā ca / yoganiyā ceva dhammā no ca yogā | that are both yokes and yoke-producing / that are yoke-producing and not yokes | जकड़न रूपी भी और जकड़नों का विषय बनने वाली भी / जकड़नों का विषय बनने वाली, पर स्वयं जकड़न रूपी न होने वाली | English 'yoke-producing' (see 1-M2-39) |
| 1-M2-42 | `SAME` | yogā ceva dhammā yogasampayuttā ca / yogasampayuttā ceva dhammā no ca yogā | that are both yokes and associated with yokes / associated with yokes that are not yokes | जकड़न रूपी भी और जकड़नों से जुड़ी भी / जकड़नों से जुड़ी, पर स्वयं जकड़न रूपी न होने वाली |  |
| 1-M2-43 | `DIFFERS-ENGLISH` | yogavippayuttā kho pana dhammā yoganiyāpi / ayoganiyāpi / Yogagocchakaṃ | disassociated from yokes yet yoke-producing / disassociated from yokes / Yoke Classification | जकड़नों से अलग, पर उनका विषय बनने वाली / जकड़नों से अलग और उनका विषय न बनने वाली / जकड़नों का वर्ग | English 'yoke-producing' (see 1-M2-39) |
| 1-M2-44 | `SAME` | nīvaraṇā / no nīvaraṇā | that are hindrances / that are not hindrances | बाधा रूपी / बाधा रूपी न होने वाली |  |
| 1-M2-45 | `DIFFERS-ENGLISH` | nīvaraṇiyā / anīvaraṇiyā | hindering / non-hindering | बाधाओं का विषय बनने वाली / बाधाओं का विषय न बनने वाली | nīvaraṇiyā like saṃyojaniyā (comm. ^1-551): object of the hindrances. English 'hindering' reads as agent |
| 1-M2-46 | `SAME` | nīvaraṇasampayuttā / nīvaraṇavippayuttā | associated with hindrances / disassociated from hindrances | बाधाओं से जुड़ी / बाधाओं से अलग |  |
| 1-M2-47 | `DIFFERS-ENGLISH` | nīvaraṇā ceva dhammā nīvaraṇiyā ca / nīvaraṇiyā ceva dhammā no ca nīvaraṇā | that are both hindrances and hindering / that are hindering and not hindrances | बाधा रूपी भी और बाधाओं का विषय बनने वाली भी / बाधाओं का विषय बनने वाली, पर स्वयं बाधा रूपी न होने वाली | English 'both hindrances and hindering' loses the distinction (see 1-M2-45) |
| 1-M2-48 | `SAME` | nīvaraṇā ceva dhammā nīvaraṇasampayuttā ca / nīvaraṇasampayuttā ceva dhammā no ca nīvaraṇā | that are both hindrances and associated with hindrances / associated with hindrances that are not hindrances | बाधा रूपी भी और बाधाओं से जुड़ी भी / बाधाओं से जुड़ी, पर स्वयं बाधा रूपी न होने वाली |  |
| 1-M2-49 | `DIFFERS-ENGLISH` | nīvaraṇavippayuttā kho pana dhammā nīvaraṇiyāpi / anīvaraṇiyāpi / Nīvaraṇagocchakaṃ | disassociated from hindrances yet hindering / disassociated from hindrances / Hindrance Classification | बाधाओं से अलग, पर उनका विषय बनने वाली / बाधाओं से अलग और उनका विषय न बनने वाली / बाधाओं का वर्ग | English 'hindering' (see 1-M2-45) |
| 1-M2-50 | `PLAINER` | parāmāsā / no parāmāsā | that are seizings / that are not seizings | ग़लत धारणा रूपी / ग़लत धारणा रूपी न होने वाली | parāmāsa 'seizing' → ग़लत धारणा (explained as wrong view) |
| 1-M2-51 | `PLAINER` | parāmaṭṭhā / aparāmaṭṭhā | seized / unseized | ग़लत धारणा का विषय बनने वाली / ग़लत धारणा का विषय न बनने वाली | parāmaṭṭha 'seized' → ग़लत धारणा का विषय; both read it as object, so meaning the same |
| 1-M2-52 | `PLAINER` | parāmāsasampayuttā / parāmāsavippayuttā | associated with seizings / disassociated from seizings | ग़लत धारणा से जुड़ी / ग़लत धारणा से अलग | parāmāsa → ग़लत धारणा |
| 1-M2-53 | `PLAINER` | parāmāsā ceva dhammā parāmaṭṭhā ca / parāmaṭṭhā ceva dhammā no ca parāmāsā | that are both seizings and seized / that are seized and not seizings | ग़लत धारणा रूपी भी और ग़लत धारणा का विषय बनने वाली भी / ग़लत धारणा का विषय बनने वाली, पर स्वयं ग़लत धारणा रूपी न होने वाली | parāmāsa → ग़लत धारणा |
| 1-M2-54 | `PLAINER` | parāmāsavippayuttā kho pana dhammā parāmaṭṭhāpi / aparāmaṭṭhāpi / Parāmāsagocchakaṃ | disassociated from seizings yet seized / disassociated from seizings / Grasping Classification | ग़लत धारणा से अलग, पर उसका विषय बनने वाली / ग़लत धारणा से अलग और उसका विषय न बनने वाली / ग़लत धारणा का वर्ग | parāmāsa → ग़लत धारणा |
| 1-M2-55 | `SAME` | sārammaṇā / anārammaṇā | with an object / without an object | विषय वाली / विषय से रहित |  |
| 1-M2-56 | `SAME` | cittā / no cittā | that are minds / that are not minds | मन रूपी / मन रूपी न होने वाली |  |
| 1-M2-57 | `PLAINER` | cetasikā / acetasikā | mental factors / non-mental factors | मन की सहचर / मन की सहचर न होने वाली | cetasika 'mental factors' → मन की सहचर परिघटनाएँ |
| 1-M2-58 | `SAME` | cittasampayuttā / cittavippayuttā | associated with mind / disassociated from mind | मन से जुड़ी / मन से अलग |  |
| 1-M2-59 | `SAME` | cittasaṃsaṭṭhā / cittavisaṃsaṭṭhā | in close contact with mind / not in close contact with mind | मन से घुली-मिली / मन से घुली-मिली न होने वाली |  |
| 1-M2-60 | `SAME` | cittasamuṭṭhānā / no cittasamuṭṭhānā | arising from mind / not arising from mind | मन से उत्पन्न / मन से उत्पन्न न होने वाली |  |
| 1-M2-61 | `SAME` | cittasahabhuno / no cittasahabhuno | concurrent with mind / not concurrent with mind | मन के साथ-साथ होने वाली / मन के साथ-साथ न होने वाली |  |
| 1-M2-62 | `SAME` | cittānuparivattino / no cittānuparivattino | following in sequence with mind / not following in sequence with mind | मन का अनुसरण करने वाली / मन का अनुसरण न करने वाली | English 'following in sequence' hints at succession; comm. ^1-1657: lasts as long as the mind. Hindi neutral |
| 1-M2-63 | `SAME` | cittasaṃsaṭṭhasamuṭṭhānā / no cittasaṃsaṭṭhasamuṭṭhānā | in close contact with mind and arising from mind / not in close contact with mind and arising from mind | मन से घुली-मिली और मन से उत्पन्न / ऐसी परिघटनाएँ जो मन से घुली-मिली और मन से उत्पन्न नहीं हैं | Hindi (ख) negates the whole compound (correct); English (B) word order lets 'not' read as covering only the first member |
| 1-M2-64 | `SAME` | cittasaṃsaṭṭhasamuṭṭhānasahabhuno / no cittasaṃsaṭṭhasamuṭṭhānasahabhuno | in close contact with mind, arising from mind, and concurrent with mind / not in close contact with mind, arising from mind, and concurrent with mind | मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली / ऐसी परिघटनाएँ जो मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली नहीं हैं | as 1-M2-63 |
| 1-M2-65 | `SAME` | cittasaṃsaṭṭhasamuṭṭhānānuparivattino / no cittasaṃsaṭṭhasamuṭṭhānānuparivattino | in close contact with mind, arising from mind, and following in sequence with mind / not in close contact with mind, arising from mind, and following in sequence with mind | मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली / ऐसी परिघटनाएँ जो मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली नहीं हैं | as 1-M2-63 |
| 1-M2-66 | `SAME` | ajjhattikā / bāhirā | internal / external | आंतरिक / बाह्य | ajjhattika (internal sense bases) → आंतरिक |
| 1-M2-67 | `DIFFERS-ENGLISH` | upādā / no upādā | that are takings / that are not takings | व्युत्पन्न / व्युत्पन्न न होने वाली | upādā = derived (from the elements) (comm. ^1-553). English 'takings' (termbase sense) wrong; Hindi व्युत्पन्न right |
| 1-M2-68 | `PLAINER` | upādiṇṇā / anupādiṇṇā / Mahantaradukaṃ | grasped / ungrasped / Major Dyadic Classification | कर्म से उत्पन्न / कर्म से उत्पन्न न होने वाली / बीच के बड़े दो-दो के वर्गीकरण | upādiṇṇa 'grasped' → कर्म से उत्पन्न (comm. ^1-523) |
| 1-M2-69 | `SAME` | upādānā / no upādānā | that are clinging / that are not clinging | आसक्ति रूपी / आसक्ति रूपी न होने वाली |  |
| 1-M2-70 | `DIFFERS-ENGLISH` | upādāniyā / anupādāniyā | clinging-producing / non-clinging-producing | आसक्ति का विषय बनने वाली / आसक्ति का विषय न बनने वाली | upādāniyā = object of clinging (comm. ^1-523). English 'clinging-producing' wrong (and differs from its own 'appropriable' at 1-M1-4); Hindi right |
| 1-M2-71 | `SAME` | upādānasampayuttā / upādānavippayuttā | associated with clinging / disassociated from clinging | आसक्ति से जुड़ी / आसक्ति से अलग |  |
| 1-M2-72 | `DIFFERS-ENGLISH` | upādānā ceva dhammā upādāniyā ca / upādāniyā ceva dhammā no ca upādānā | that are both clinging and clinging-producing / that are clinging-producing and not clinging | आसक्ति रूपी भी और आसक्ति का विषय बनने वाली भी / आसक्ति का विषय बनने वाली, पर स्वयं आसक्ति रूपी न होने वाली | English 'clinging-producing' (see 1-M2-70) |
| 1-M2-73 | `SAME` | upādānā ceva dhammā upādānasampayuttā ca / upādānasampayuttā ceva dhammā no ca upādānā | that are both clinging and associated with clinging / associated with clinging that are not clinging | आसक्ति रूपी भी और आसक्ति से जुड़ी भी / आसक्ति से जुड़ी, पर स्वयं आसक्ति रूपी न होने वाली |  |
| 1-M2-74 | `DIFFERS-ENGLISH` | upādānavippayuttā kho pana dhammā upādāniyāpi / anupādāniyāpi / Upādānagocchakaṃ | disassociated from clinging yet clinging-producing / disassociated from clinging / Clinging Classification | आसक्ति से अलग, पर उसका विषय बनने वाली / आसक्ति से अलग और उसका विषय न बनने वाली / आसक्ति का वर्ग | English 'clinging-producing' (see 1-M2-70) |
| 1-M2-75 | `SAME` | kilesā / no kilesā | that are defilements / that are not defilements | मन के क्लेश रूपी / मन के क्लेश रूपी न होने वाली |  |
| 1-M2-76 | `DIFFERS-ENGLISH` | saṃkilesikā / asaṃkilesikā | defiling / non-defiling | क्लेशों का विषय बनने वाली / क्लेशों का विषय न बनने वाली | saṃkilesikā = object of defilement (comm. ^1-524). English 'defiling' reads as agent; Hindi right |
| 1-M2-77 | `SAME` | saṃkiliṭṭhā / asaṃkiliṭṭhā | defiled / undefiled | क्लेशों से मलिन / क्लेशों से मलिन न होने वाली |  |
| 1-M2-78 | `SAME` | kilesasampayuttā / kilesavippayuttā | associated with defilements / disassociated from defilements | क्लेशों से जुड़ी / क्लेशों से अलग |  |
| 1-M2-79 | `DIFFERS-ENGLISH` | kilesā ceva dhammā saṃkilesikā ca / saṃkilesikā ceva dhammā no ca kilesā | that are both defilements and defiling / that are defiling and not defilements | मन के क्लेश रूपी भी और क्लेशों का विषय बनने वाली भी / क्लेशों का विषय बनने वाली, पर स्वयं मन के क्लेश रूपी न होने वाली | English 'both defilements and defiling' (see 1-M2-76) |
| 1-M2-80 | `SAME` | kilesā ceva dhammā saṃkiliṭṭhā ca / saṃkiliṭṭhā ceva dhammā no ca kilesā | that are both defilements and defiled / that are defiled and not defilements | मन के क्लेश रूपी भी और क्लेशों से मलिन भी / क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने वाली |  |
| 1-M2-81 | `SAME` | kilesā ceva dhammā kilesasampayuttā ca / kilesasampayuttā ceva dhammā no ca kilesā | that are both defilements and associated with defilements / associated with defilements that are not defilements | मन के क्लेश रूपी भी और क्लेशों से जुड़ी भी / क्लेशों से जुड़ी, पर स्वयं मन के क्लेश रूपी न होने वाली |  |
| 1-M2-82 | `DIFFERS-ENGLISH` | kilesavippayuttā kho pana dhammā saṃkilesikāpi / asaṃkilesikāpi / Kilesagocchakaṃ | disassociated from defilements yet defiling / disassociated from defilements / Defilement Classification | क्लेशों से अलग, पर क्लेशों का विषय बनने वाली / क्लेशों से अलग और क्लेशों का विषय न बनने वाली / मन के क्लेशों का वर्ग | English 'defiling' (see 1-M2-76) |
| 1-M2-83 | `PLAINER` | dassanena pahātabbā / na dassanena pahātabbā | abandoned by insight / not abandoned by insight | सत्य-दर्शन से छोड़ी जाने वाली / सत्य-दर्शन से न छोड़ी जाने वाली | dassana → सत्य-दर्शन (see 1-M1-8) |
| 1-M2-84 | `PLAINER` | bhāvanāya pahātabbā / na bhāvanāya pahātabbā | abandoned by cultivation / not abandoned by cultivation | मानसिक अभ्यास से छोड़ी जाने वाली / मानसिक अभ्यास से न छोड़ी जाने वाली | bhāvanā → मानसिक अभ्यास |
| 1-M2-85 | `DIFFERS-ENGLISH` | dassanena pahātabbahetukā / na dassanena pahātabbahetukā | that are factors for abandonment by insight / that are not factors for abandonment by insight | सत्य-दर्शन से छोड़े जाने वाले मूलों वाली / सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित | English 'factors for abandonment' wrong (see 1-M1-9); Hindi (ख) 'मूलों से रहित' is the comm. reading |
| 1-M2-86 | `DIFFERS-ENGLISH` | bhāvanāya pahātabbahetukā / na bhāvanāya pahātabbahetukā | that are factors for abandonment by cultivation / that are not factors for abandonment by cultivation | मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली / मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित | as 1-M2-85 |
| 1-M2-87 | `SAME` | savitakkā / avitakkā | with initial application / without initial application | आरंभिक विचार वाली / आरंभिक विचार से रहित |  |
| 1-M2-88 | `SAME` | savicārā / avicārā | with sustained application / without sustained application | सतत विचार वाली / सतत विचार से रहित |  |
| 1-M2-89 | `SAME` | sappītikā / appītikā | accompanied by rapture / not accompanied by rapture | उल्लास वाली / उल्लास से रहित |  |
| 1-M2-90 | `SAME` | pītisahagatā / na pītisahagatā | accompanied by rapture / not accompanied by rapture | उल्लास के साथ होने वाली / उल्लास के साथ न होने वाली |  |
| 1-M2-91 | `SAME` | sukhasahagatā / na sukhasahagatā | accompanied by pleasure / not accompanied by pleasure | सुख के साथ होने वाली / सुख के साथ न होने वाली |  |
| 1-M2-92 | `SAME` | upekkhāsahagatā / na upekkhāsahagatā | accompanied by equanimity / not accompanied by equanimity | समभाव के साथ होने वाली / समभाव के साथ न होने वाली |  |
| 1-M2-93 | `PLAINER` | kāmāvacarā / na kāmāvacarā | of the sensual sphere / not of the sensual sphere | इंद्रिय-सुखों के लोक से संबंधित / इंद्रिय-सुखों के लोक से संबंधित न होने वाली | kāmāvacara 'sensual sphere' → इंद्रिय-सुखों के लोक |
| 1-M2-94 | `PLAINER` | rūpāvacarā / na rūpāvacarā | of the form sphere / not of the form sphere | सूक्ष्म भौतिक लोक से संबंधित / सूक्ष्म भौतिक लोक से संबंधित न होने वाली | rūpāvacara 'form sphere' → सूक्ष्म भौतिक लोक |
| 1-M2-95 | `SAME` | arūpāvacarā / na arūpāvacarā | of the formless sphere / not of the formless sphere | अभौतिक लोक से संबंधित / अभौतिक लोक से संबंधित न होने वाली |  |
| 1-M2-96 | `DIFFERS-ENGLISH` | pariyāpannā / apariyāpannā | determined / undetermined | अस्तित्व के लोकों में समाई हुई / अस्तित्व के लोकों में न समाई हुई | pariyāpanna = included in the three-plane round (comm. ^1-556). English 'determined' (would be niyata, 1-M2-98) wrong; Hindi right |
| 1-M2-97 | `PLAINER` | niyyānikā / aniyyānikā | leading-out / not-leading-out | मुक्ति की ओर ले जाने वाली / मुक्ति की ओर न ले जाने वाली | niyyānika 'leading-out' → मुक्ति की ओर ले जाने वाली |
| 1-M2-98 | `SAME` | niyatā / aniyatā | determinate / indeterminate | निश्चित / अनिश्चित |  |
| 1-M2-99 | `SAME` | sauttarā / anuttarā | with a superior / without a superior | सर्वोच्च न होने वाली / सर्वोच्च | Hindi recasts 'with a superior / without' as 'not supreme / supreme'; same meaning |
| 1-M2-100 | `DIFFERS-ENGLISH` | saraṇā / araṇā / Piṭṭhidukaṃ / Abhidhammadukamātikā | with a refuge / without a refuge / Conclusion Dyadic Classification / Abhidhamma Dyadic Matrix | संघर्ष वाली / संघर्ष से रहित / अंतिम दो-दो के वर्गीकरण / अभिधम्म के दो-दो के वर्गीकरणों की मूल सूची | saraṇa here = with raṇa (strife: lust etc.) (comm. ^1-556). English 'with a refuge' (termbase sense) is wrong; Hindi संघर्ष right |
| 1-M2-101 | `SAME` | vijjābhāgino / avijjābhāgino | connected with wisdom / connected with ignorance | विद्या की भागी / अज्ञान की भागी | English 'wisdom' for vijjā collides with paññā; Hindi विद्या |
| 1-M2-102 | `DIFFERS-ENGLISH` | vijjūpamā / vajirūpamā | comparable to wisdom / comparable to a diamond | बिजली जैसी / वज्र जैसी | vijjūpamā = like lightning (comm. ^1-558 vijju upamā). English 'comparable to wisdom' wrong; Hindi बिजली right |
| 1-M2-103 | `SAME` | bālā / paṇḍitā | foolish / wise | मूर्खतापूर्ण / बुद्धिमत्तापूर्ण |  |
| 1-M2-104 | `SAME` | kaṇhā / sukkā | dark / bright | काली / उजली |  |
| 1-M2-105 | `DIFFERS-ENGLISH` | tapanīyā / atapanīyā | blameworthy / blameless | संताप देने वाली / संताप न देने वाली | tapanīyā = tormenting here and hereafter (comm. ^1-558). English 'blameworthy' off; Hindi संताप देने वाली right |
| 1-M2-106 | `SAME` | adhivacanā / adhivacanapathā | nominal / path of nominal designation | नाम रूपी / नाम के मार्ग रूपी |  |
| 1-M2-107 | `DIFFERS-BOTH-OK` | nirutti / niruttipathā | etymological / path of etymology | अभिव्यक्ति रूपी / अभिव्यक्ति के मार्ग रूपी | comm. ^1-559: nirutti = expressions stated with their reason (e.g. 'abhisaṅkharontīti saṅkhārā'). English takes the etymological side, Hindi अभिव्यक्ति the 'expression' side |
| 1-M2-108 | `SAME` | paññatti / paññattipathā | conventional / path of convention | नामकरण रूपी / नामकरण के मार्ग रूपी | paññatti → नामकरण / 'conventional' |
| 1-M2-109 | `PLAINER` | nāmañca / rūpañca | name / form | अभौतिक पक्ष / भौतिक रूप | nāma 'name' → अभौतिक पक्ष (explained) |
| 1-M2-110 | `SAME` | avijjā ca / bhavataṇhā ca | ignorance / craving for becoming | अज्ञान / अस्तित्व की तृष्णा |  |
| 1-M2-111 | `SAME` | bhavadiṭṭhi ca / vibhavadiṭṭhi ca | being-view / non-being-view | अस्तित्व की दृष्टि / अनस्तित्व की दृष्टि |  |
| 1-M2-112 | `SAME` | sassatadiṭṭhi ca / ucchedadiṭṭhi ca | eternalism / annihilationism | शाश्वतता की दृष्टि / विनाश की दृष्टि |  |
| 1-M2-113 | `DIFFERS-ENGLISH` | antavā diṭṭhi ca / anantavā diṭṭhi ca | limited view / unlimited view | सीमित होने की दृष्टि / असीम होने की दृष्टि | antavā diṭṭhi = the view that (self/world) is finite (comm. ^1-560). English 'limited view' describes the view itself; Hindi right |
| 1-M2-114 | `SAME` | pubbantānudiṭṭhi ca / aparantānudiṭṭhi ca | speculation about the past / speculation about the future | अतीत के बारे में दृष्टि / भविष्य के बारे में दृष्टि |  |
| 1-M2-115 | `PLAINER` | ahirikañca / anottappañca | shamelessness / recklessness | निर्लज्जता / बुराई से न डरने की वृत्ति | anottappa 'recklessness' → बुराई से न डरने की वृत्ति |
| 1-M2-116 | `SAME` | hirī ca / ottappañca | shame / fear of blame | लज्जा / बुराई का डर |  |
| 1-M2-117 | `SAME` | dovacassatā ca / pāpamittatā ca | stubbornness / association with bad friends | सलाह न मानने की प्रवृत्ति / बुरे मित्रों की संगति | Hindi 'not heeding advice' is closer to dovacassa (comm. ^1-560: hard to speak to) than 'stubbornness' |
| 1-M2-118 | `SAME` | sovacassatā ca / kalyāṇamittatā ca | compliance / association with good friends | सलाह मानने की प्रवृत्ति / अच्छे मित्रों की संगति |  |
| 1-M2-119 | `SAME` | āpattikusalatā ca / āpattivuṭṭhānakusalatā ca | skill in transgressions / skill in recovery from transgressions | दोषों के विषय में कुशलता / दोषों से उबरने में कुशलता |  |
| 1-M2-120 | `DIFFERS-ENGLISH` | samāpattikusalatā ca / samāpattivuṭṭhānakusalatā ca | skill in attainments / skill in recovery from attainments | ध्यान-अवस्थाओं के विषय में कुशलता / ध्यान-अवस्थाओं से बाहर आने में कुशलता | samāpattivuṭṭhāna = emergence from attainments (comm. ^1-561). English 'recovery' implies the attainment is a fault; Hindi 'बाहर आने' right. Minor |
| 1-M2-121 | `SAME` | dhātukusalatā ca / manasikārakusalatā ca | skill in elements / skill in attention | तत्वों के विषय में कुशलता / मनोयोग के विषय में कुशलता |  |
| 1-M2-122 | `PLAINER` | āyatanakusalatā ca / paṭiccasamuppādakusalatā ca | skill in sense bases / skill in dependent origination | इंद्रिय-क्षेत्रों के विषय में कुशलता / कारणों पर आश्रित उत्पत्ति के विषय में कुशलता | āyatana → इंद्रिय-क्षेत्र; paṭiccasamuppāda → कारणों पर आश्रित उत्पत्ति |
| 1-M2-123 | `DIFFERS-ENGLISH` | ṭhānakusalatā ca / aṭṭhānakusalatā ca | skill in conditions for progress / skill in conditions for regress | संभव बातों के विषय में कुशलता / असंभव बातों के विषय में कुशलता | ṭhāna = cause, aṭṭhāna = non-cause (comm. ^1-561). English 'progress / regress' has no basis; Hindi 'संभव / असंभव' is the usual sense (optional closer: कारण / अकारण) |
| 1-M2-124 | `SAME` | ajjavo ca / maddavo ca | integrity / gentleness | सरलता / कोमलता |  |
| 1-M2-125 | `DIFFERS-BOTH-OK` | khanti ca / soraccañca | patience / modesty | सहनशीलता / सौम्यता | comm. ^1-1842: soracca = non-transgression in body and speech, being well withdrawn from evil. English 'modesty', Hindi सौम्यता (gentleness, the dictionary sense); neither is the comm. sense (optional Hindi: संयमशीलता) |
| 1-M2-126 | `DIFFERS-ENGLISH` | sākhalyañca / paṭisanthāro ca | friendliness / respect | मधुर व्यवहार / आदर-सत्कार | paṭisanthāra = kindly reception / hospitality (comm. ^1-1845; termbase 'friendly reception'). English 'respect' off; Hindi आदर-सत्कार right |
| 1-M2-127 | `SAME` | indriyesu aguttadvāratā ca / bhojane amattaññutā ca | unguarded sense doors / lack of moderation in food | इंद्रियों के द्वारों की रक्षा न करने की प्रवृत्ति / भोजन में मात्रा के ज्ञान का अभाव |  |
| 1-M2-128 | `SAME` | indriyesu guttadvāratā ca / bhojane mattaññutā ca | guarded sense doors / moderation in food | इंद्रियों के द्वारों की रक्षा करने की प्रवृत्ति / भोजन में मात्रा का ज्ञान |  |
| 1-M2-129 | `SAME` | muṭṭhasaccañca / asampajaññañca | loss of mindfulness / lack of clear comprehension | सजगता की कमी / स्पष्ट समझ का अभाव |  |
| 1-M2-130 | `SAME` | sati ca / sampajaññañca | mindfulness / clear comprehension | सजगता / स्पष्ट समझ |  |
| 1-M2-131 | `PLAINER` | paṭisaṅkhānabalañca / bhāvanābalañca | power of reflection / power of development | सोच-विचार का बल / मानसिक अभ्यास का बल | bhāvanā 'development' → मानसिक अभ्यास |
| 1-M2-132 | `SAME` | samatho ca / vipassanā ca | calm / insight | शांति / अंतर्दृष्टि |  |
| 1-M2-133 | `SAME` | samathanimittañca / paggāhanimittañca | signs conducive to calm / signs of exertion | शांति का चिह्न / तत्परता का चिह्न |  |
| 1-M2-134 | `SAME` | paggāho ca / avikkhepo ca | exertion / non-distraction | तत्परता / भटकाव का अभाव | paggāha 'exertion' → तत्परता (termbase) |
| 1-M2-135 | `SAME` | sīlavipatti ca / diṭṭhivipatti ca | moral failure / view failure | सदाचार में विफलता / दृष्टि में विफलता |  |
| 1-M2-136 | `SAME` | sīlasampadā ca / diṭṭhisampadā ca | moral perfection / view perfection | सदाचार की संपन्नता / दृष्टि की संपन्नता |  |
| 1-M2-137 | `SAME` | sīlavisuddhi ca / diṭṭhivisuddhi ca | moral purity / view purity | सदाचार की शुद्धि / दृष्टि की शुद्धि |  |
| 1-M2-138 | `SAME` | diṭṭhivisuddhi kho pana / yathādiṭṭhissa ca padhānaṃ | view purity / effort according to one's view | दृष्टि की शुद्धि / और अपनी दृष्टि के अनुरूप प्रयास |  |
| 1-M2-139 | `SAME` | saṃvego ca saṃvejaniyesu ṭhānesu / saṃviggassa ca yoniso padhānaṃ | urgency in cases that produce urgency / wise effort when stirred | झकझोर देने वाली बातों से मन का झकझोरा जाना / और झकझोरे गए व्यक्ति का उचित ढंग से किया गया प्रयास |  |
| 1-M2-140 | `DIFFERS-ENGLISH` | asantuṭṭhitā ca kusalesu dhammesu / appaṭivānitā ca padhānasmiṃ | dissatisfaction with wholesome states / lack of restraint in effort | हितकर परिघटनाओं से संतुष्ट न होना / प्रयास में पीछे न हटना | appaṭivānitā = not turning back in striving (comm. ^1-563 anivattanatā anosakkanatā). English 'lack of restraint in effort' wrong; Hindi पीछे न हटना right |
| 1-M2-141 | `SAME` | vijjā ca / vimutti ca | wisdom / liberation | विद्या / मुक्ति | English 'wisdom' for vijjā (see 1-M2-101) |
| 1-M2-142 | `SAME` | khaye ñāṇaṃ / anuppāde ñāṇanti / Suttantikadukamātikā / Mātikā niṭṭhitā | knowledge of destruction / knowledge of non-arising / Suttanic Dyadic Matrix / Matrix Concluded | क्षय का ज्ञान / उत्पन्न न होने का ज्ञान / उपदेशों के दो-दो के वर्गीकरणों की मूल सूची / मूल सूची पूरी हुई |  |

## 3. Fixes needed in the Hindi

Only one line. No `MISSING` or `ADDED` on the Hindi side.

### 1-M1-9 (ग): *neva dassanena na bhāvanāya pahātabbahetukā dhammā* (`DIFFERS-HINDI`)

- **Current Hindi:** न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली परिघटनाएँ।
  This says "phenomena that *have* roots which are abandoned neither by seeing nor by development".
- **Pāli justification:** the commentary (comm. ^1-528) rules this reading out by name. It says not to take the compound as "their root is to be abandoned neither by seeing nor by development", but as "they *have no* root that is to be abandoned by seeing or by development" (*neva dassanena na bhāvanāya pahātabbo hetu etesaṃ atthīti … ayamattho gahetabbo*). It gives two reasons. (1) The other reading would leave out the rootless (*ahetuka*) phenomena, which have no root at all to be abandoned. (2) It would make the roots, not the phenomena, the thing that is not abandoned. The current Hindi has the first problem: it requires the phenomena to have roots (मूलों वाली).
- **Fix:** सत्य-दर्शन से छोड़े जाने वाले मूलों से भी रहित और मानसिक अभ्यास से छोड़े जाने वाले मूलों से भी रहित परिघटनाएँ।
  This matches the Hindi's own pattern at 1-M2-85 (ख) and 1-M2-86 (ख) (…छोड़े जाने वाले मूलों से रहित), which is already correct. A shorter "न … न … छोड़े जाने वाले मूलों से रहित" would be ambiguous again, so it is better to say मूलों से भी रहित twice.
- **Follow-up (outside this comparison):** the same compound comes back where the body of pi-1 defines this triad. It is worth a grep for "न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली" in the Hindi pi-1 text and termbase.

### Optional, not needed (Hindi already right in meaning)

- 1-M1-17 (ग) *uppādino*: उत्पन्न होने वाली could be sharpened to अवश्य उत्पन्न होने वाली, following comm. ^1-536 (*avassaṃ uppajjissanti*).
- 1-M2-123 *ṭhāna / aṭṭhāna*: the commentary glosses *ṭhāna* as *kāraṇa* (comm. ^1-561). संभव / असंभव is the usual sense and is fine. कारण / अकारण would be the commentary's own wording.
- 1-M2-125 *soracca*: the commentary reads it as not transgressing in body and speech (comm. ^1-1842). सौम्यता is the dictionary sense. संयमशीलता would be closer to the commentary. This is recorded as `DIFFERS-BOTH-OK`.
- Label consistency: 1-M2-142 uses पाठभेद where every other line uses वर्तनी-भेद. पाठभेद is actually the better label here (*suttantamātikā* is a different reading, not a spelling), so no change is needed in meaning.

## 4. Points where the scholar version itself is off (`DIFFERS-ENGLISH`)

48 lines. In every one the Hindi matches the Pāli and the commentary. Several of these errors come straight from the scholarly termbase, which gives a general dictionary sense where the Mātikā needs the Abhidhamma sense. Examples: *hetu* "because", *kenaci* "someone", *saraṇa* "refuge", *pariyāpanna* "comprehensive", *upādā* "holding", *sāsava* "defiled".

### 4a. Systematic errors (one cause, many lines)

| Pattern | Lines | English | Pāli / commentary |
|---|---|---|---|
| *-niya / -ika* terms made into agents | 1-M2-21, 23, 25 (saṃyojaniya); 27, 29, 31 (ganthaniya); 33, 35, 37 (oghaniya); 39, 41, 43 (yoganiya); 45, 47, 49 (nīvaraṇiya); 70, 72, 74 (upādāniya); 76, 79, 82 (saṃkilesika) | "fettering", "knotting", "flood-producing", "yoke-producing", "hindering", "clinging-producing", "defiling" | The commentary defines each of these as the phenomena that are the **object** (*ārammaṇa-paccaya*) of the fetters, floods and so on: comm. ^1-523, ^1-524, ^1-547, ^1-548, ^1-549, ^1-550, ^1-551. "-producing" is simply wrong. The active "fettering" etc. erases the difference between *saṃyojanā* and *saṃyojaniyā*, which is exactly what pairs like 1-M2-23 "both fetters and fettering" exist to mark. Hindi: …का विषय बनने वाली (correct) |
| *sāsava* = "defiled" | 1-M2-15, 17, 19 | "defiled" (but "untainted" for *anāsava*) | comm. ^1-546: *sāsava* = with the taints that take it as object. "Defiled" is the word for *saṃkiliṭṭha* (1-M2-77), so the English merges *sāsava* with *saṃkiliṭṭha*. Hindi: मन के मैलों का विषय |
| *hetu* = "reason" | 1-M2-1 to 1-M2-5 | "reasons", "with a reason" | comm. ^1-543: *hetu* here means root (*mūlaṭṭhena*). The English keeps the *hetu* / *sahetuka* structure but gives the wrong sense. Hindi: मूल |
| *pahātabbahetuka* = "factors for abandonment" | 1-M1-9 (counted as `DIFFERS-HINDI` because of (ग), but its English is off too), 1-M2-85, 1-M2-86 | "factors for abandonment through insight" | comm. ^1-528: having **roots** that are to be abandoned. Hindi: …छोड़े जाने वाले मूलों वाली |
| Wrong second member of a triad | 1-M1-4 (B), 1-M1-5 (B) | "ungrasped, non-appropriable"; "undefiled, non-defiling" | The Pāli is *anupādiṇṇ-upādāniyā* and *asaṃkiliṭṭha-saṃkilesikā* (the second word is *not* negated). In the English, (B) and (C) are word-for-word the same. Hindi correct |

### 4b. Single-line sense errors

| ref | English | Should be (Pāli / commentary) | Hindi |
|---|---|---|---|
| 1-M1-3 | "resultant-state" (*vipākadhammadhammā*) | having the nature to produce results (comm. ^1-522) | कर्म-फल उत्पन्न करने वाली |
| 1-M1-16 | "path factors" (*maggahetukā*) | having the path as root or condition (comm. ^1-535) | मार्ग को मूल बनाने वाली |
| 1-M1-17 | "productive" (*uppādino*) | bound to arise (comm. ^1-536) | उत्पन्न होने वाली |
| 1-M2-6 | "disassociated from a reason" (*na hetū*) | not roots (that would be *hetuvippayutta*) (comm. ^1-543) | मूल रूपी न होने वाली |
| 1-M2-13 | "knowable by someone" (*kenaci viññeyyā*) | knowable by some one consciousness, eye-consciousness and so on (comm. ^1-545) | किसी एक प्रकार के विज्ञान से |
| 1-M2-67 | "takings" (*upādā*) | derived from the elements (comm. ^1-553) | व्युत्पन्न |
| 1-M2-96 | "determined" (*pariyāpannā*) | included in the three-plane round (comm. ^1-556). "Determined" is *niyata* (1-M2-98) | अस्तित्व के लोकों में समाई हुई |
| 1-M2-100 | "with a refuge" (*saraṇā*) | with strife (*raṇa* = lust and the rest) (comm. ^1-556) | संघर्ष वाली |
| 1-M2-102 | "comparable to wisdom" (*vijjūpamā*) | like lightning (*vijju*) (comm. ^1-558) | बिजली जैसी |
| 1-M2-105 | "blameworthy" (*tapanīyā*) | tormenting, here and hereafter (comm. ^1-558) | संताप देने वाली |
| 1-M2-113 | "limited view" (*antavā diṭṭhi*) | the view that self or world is finite (comm. ^1-560) | सीमित होने की दृष्टि |
| 1-M2-120 | "recovery from attainments" | emergence from attainments (comm. ^1-561). Minor | बाहर आने में |
| 1-M2-123 | "conditions for progress / regress" (*ṭhāna / aṭṭhāna*) | cause / non-cause (comm. ^1-561) | संभव / असंभव |
| 1-M2-126 | "respect" (*paṭisanthāra*) | kindly reception, hospitality (comm. ^1-1845; the scholarly termbase itself has "friendly reception") | आदर-सत्कार |
| 1-M2-140 | "lack of restraint in effort" (*appaṭivānitā*) | not turning back in striving (comm. ^1-563) | प्रयास में पीछे न हटना |

### 4c. Smaller English issues (not counted as differences; verdict stays `SAME` / `PLAINER`)

- **Collisions in the English:** "indeterminate" is used for both *abyākata* (1-M1-1) and *aniyata* (1-M1-15, 1-M2-98). "Insight" is used for both *dassana* (1-M1-8, 1-M2-83) and *vipassanā* (1-M2-132). "Internal" is used for both *ajjhatta* (1-M1-20/21) and *ajjhattika* (1-M2-66). "Wisdom" is used for *vijjā* (1-M2-101, 141), which collides with *paññā*. The Hindi keeps all four pairs apart.
- **Negation scope:** 1-M2-63 to 65 (B), e.g. "not in close contact with mind and arising from mind". The English word order lets "not" read as covering only the first member. The Pāli *no* negates the whole compound, and the Hindi (ऐसी परिघटनाएँ जो … नहीं हैं) gets this right.
- 1-M2-62 "following in sequence with mind": "in sequence" suggests succession. The commentary (^1-1657) means that it lasts as long as the mind lasts.
- The English drops all the variant-reading brackets (*syā.*, *sī.*, *ka.*) that the Pāli and the Hindi carry. This is editorial apparatus, not meaning, so it is not counted as `MISSING`.
