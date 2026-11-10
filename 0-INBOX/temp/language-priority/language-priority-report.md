---
title: Abhidhamma translation language priority ranking
date: 2026-11-09
status: draft
supersedes: the 2026-11-06 ranking (kept below under "Previous ranking")
scope: reading languages of the International Tipiṭaka Chanting Ceremony (ITCC) communities, plus the earlier candidates
---

# Abhidhamma translation: which language next?

## Result: ranked by ITCC attendance

The Daily Tipitaka prepares ITCC participants for the December 2026 Abhidhamma chanting in Bodhgayā. Each day it gives a "Reading for Meaning" in the reader's own language. The ranking therefore weights the languages of the communities that actually attend.

| Rank | Language | ITCC presence | Abhidhamma already in this language? | Priority |
|---|---|---|---|---|
| 1 | **Hindi (hi)** | India is the largest bloc: about 20,000 Indian participants projected for 2025, and India is principal organiser in 2025–26. Evening Dhamma talks are in Hindi and English. | Dt + Pp only: one print translation (2000, in copyright). The other five books: none found. Nothing hostable. | 1.00 |
| 1 | **Marathi (mr)** | 10,000 devotees from Maharashtra projected for 2025, the largest sub-group on record. | None found. | 1.00 |
| 3 | Burmese (my) | Major sangha on the ITCC permanent board, with its own 2026 Burmese-script chanting book. | Religious Affairs translation; Ds, Vb, Pp, Kv are online as text on Myanmar Wikisource. | 0.30 |
| 3 | Khmer (km) | Cambodia was chief organiser in 2023 and 2024, and has its own Khmer chanting book. | Buddhist Institute Tipiṭaka, 1931–69; scans only. | 0.30 |
| 3 | Bengali (bn) | Bangladesh sits on the permanent board; Bengali-script chanting book. | A complete Bangladesh translation is claimed (Tripitaka Publishing Society); its site is unreachable. | 0.30 |
| 6 | Nepali (ne) | Listed every year 2022–26; size not reported. | None in Nepali. Ds, Dt, Pp and Ya exist in Nepal Bhasa (Newari), the language of many Nepalese Theravādins (2007–19, scans on dhamma.digital). | 0.30 |
| 6 | Indonesian (id) | About 50 participants in its first year; it has its own tent. | Dhammasaṅgaṇī only (2018). | 0.30 |
| 8 | Lao (lo) | Listed every year; no Lao-script chanting book. | None confirmed; Lao readers commonly read Thai. | 0.28 |
| 9 | Sinhala (si) | Major sangha with its own chanting book (LBDFI funds at least 15 monks a year). | Buddha Jayanti Tipiṭaka, online at tipitaka.lk. | 0.18 |
| 10 | Thai (th) | Major sangha, always named first, with its own chanting book. | Several complete editions online (Royal, MCU, Mahamakut). | 0.12 |
| 10 | Vietnamese (vi) | Listed every year; nuns chanted from the Roman book in 2023. | Complete (HT Tịnh Sự), PDFs online. | 0.12 |
| 12 | French (fr) | Named only among small "other participants" in 2025. | None found. | 0.10 |
| 13 | Japanese (ja) | Named only among "other participants". | Nanden Daizōkyō, 1935–41. | 0.05 |
| 13 | Russian (ru) | Not attested. | None, apart from a 2019 dissertation fragment of Kv 1.1. | 0.05 |
| 13 | Tibetan (bo) | Not attested at the main ceremony. | None. | 0.05 |
| 16 | Chinese (zh) | Not attested. | Yuan Heng Si (元亨寺), complete. | 0.03 |

**Recommendation:**
- **Tier 1: Hindi and Marathi.** They have the most participants and no reusable translation. Hindi has only a 2000 print translation of Dt + Pp that is still in copyright, so the score keeps gap = 1.0. Hindi pi-3, pi-4 and pi-5 are now fully translated and reviewed. Marathi should be next. It shares Devanagari with Hindi, and its readers are the largest single group on record.
- **Tier 2: Burmese, Khmer, Bengali.** These are large foreign sanghas whose translations exist. Check whether those translations can be licensed before translating anew (see "Existing translations of the seven books"). The Burmese government translation may already be public domain.
- **Tier 3: Nepali, Indonesian, Lao.** These are smaller delegations.
- **Low:**
  - Sinhala, Thai and Vietnamese already have good translations online.
  - Russian, French, Japanese and Chinese have little or no ITCC presence. The Russian translation already made serves general readers, not ITCC.

**Change from the previous ranking (2026-11-06):** Russian falls from 1st to 13th because its readers are not attested at ITCC. Hindi and Marathi move to the top. Burmese, Khmer, Bengali, Lao, Sinhala and Indonesian are new candidates. The earlier list was restricted to the platform's supported languages, so Burmese, Sinhala, Khmer, Lao, Bengali and Indonesian may also need platform support.

## Method

`priority = itcc × gap`. Ties are ordered by ITCC presence, then by the earlier reader-demand score. The script is `score_itcc.py`.

**itcc** measures how strongly the language's readers are attested at ITCC. No source publishes delegation sizes by country, so the values are tiers:

| Value | Evidence |
|---|---|
| 1.0 | Thousands stated in a source (India / Maharashtra) |
| 0.6 | Major foreign sangha with its own 2026 chanting-book script |
| 0.4 | Listed every year, with no book of its own |
| 0.3 | Small or recent delegation |
| 0.1 | Named only among "other participants" |
| 0.05 | Not attested |

**gap** measures whether readers already have the Abhidhamma in their language:

| Value | Situation |
|---|---|
| 1.0 | No translation found |
| 0.7 | None, but readers use a neighbouring language's translation |
| 0.5 | Exists, but print-only, scan-only or hard to obtain |
| 0.3 | Exists and is online |
| 0.2 | Several editions online |

## ITCC: who attends

The ceremony is organised by LBDFI and held each December at the Mahābodhi Temple. Each country chants Pāli in its own tent, in its own script and pronunciation. The 2026 theme is "Different Languages, One Meaning".

**Attendance:**

| Year | Attendance | Countries |
|---|---|---|
| 2006 | 250 monks | – |
| 2015 | about 4,500 | – |
| 2019 | over 2,000 | 9 |
| 2022 | about 5,000 | 10–11 |
| 2023 | reported as 4,000 to 10,000 | 10 |
| 2024 | about 10,000 | – |
| 2025 | about 20,000 | 17–27 (sources differ) |
| 2026 | about 25,000 expected | over 27 |

**2026 chanting books:** Pāli in seven scripts, namely Khmer, Sinhala, Roman, Thai, Devanagari, Bengali and Burmese. These are Pāli, not translations. Lao has no book of its own, and Vietnamese and Indonesian participants use the Roman book.

**Communities:**
- India, about 20,000 projected for 2025:
  - Maharashtra: 10,000 projected.
  - Tai Khamti delegation from Arunachal.
  - Ladakh: Ven. Sanghasena heads the India core committee.
- Thailand, Myanmar and Sri Lanka are named in every report.
- Cambodia was chief organiser in 2023 and 2024.
- Bangladesh and Myanmar sit on the permanent board.
- Laos, Vietnam, Nepal and Indonesia are listed each year.
- USA, Malaysia, Germany, Japan, Korea, Bhutan, France, Sweden and Canada appear as "other participants".
- Tibetan and Chinese groups are not attested at the main ceremony.

**Caveats:**
- Most figures are organiser projections or paid press releases, and the totals disagree between sources.
- No per-country headcounts are published, so the ranking among foreign sanghas is by tier only.
- Script is not reading language. Devanagari serves Hindi, Marathi and Nepali readers; Bengali script serves Bangladesh and Indian Bengali readers.

**Sources:**
- https://www.lbdfi.org/india-leads-historic-20th-tipitaka-chanting-ceremony-reawakening-buddhisms-motherland/
- https://www.tribuneindia.com/news/world/buddhist-groups-from-across-india-come-together-to-organise-20th-annual-international-tipitaka-chanting-ceremony
- https://lbdfi.org/e-dharma-books/
- https://www.lbdfi.org/bodhgaya/
- https://lbdfi.org/sri-lanka/
- https://lbdfi.org/indonesia/
- https://lbdfi.org/chanting-programs-international-tipitaka-chanting-ceremony/
- https://lbdfi.org/tipitaka-chanting-to-begin-in-bodh-gaya-on-december-2/
- https://tricycle.org/article/tipitaka-chanting-program/
- https://www.buddhistdoor.net/news/19th-international-tipitaka-chanting-ceremony-begins-in-bodh-gaya/
- https://bodhgayatemple.com/20th-international-tipitaka-chanting-ceremony-begins-in-bodhgaya-with-global-participation/
- https://www.etvbharat.com/en/state/gayaji-buddhism-tripitaka-puja-2025-buddhist-devotees-from-27-countries-gathered-enn25120203078
- https://english.punjabkesari.com/business/historic-first-india-hosts-worlds-largest-buddhist-congregation-at-bodhgaya
- https://www.globalbuddhism.org/article/download/1223/1058
- https://www.dieungu.org/images/file/21xqcxn52wgQAM13/trung-tung-tam-tang-tipitaka-dec-2023-tn-gioi-huong.pdf

## Existing translations of the seven books (licence check, 2026-11-10)

The question is which existing translations of the Abhidhamma Piṭaka the library could host in its app and website.
- **Hostable:** public domain, CC0, CC BY and CC BY-SA. Hosting the text unchanged is "verbatim redistribution", which CC BY-ND also allows.
- **Not hostable without permission:**
  - NC licences allow hosting only if the platform is non-commercial;
  - in-copyright works with no licence need permission;
  - being free to download is not a licence.

**Counting rules:**
- Only real translations count. Editions that print the Pāli in another script (transliterations) are listed separately at the end.
- Each entry was checked against a catalogue record, a publisher's page or the text itself; the search ran on 2026-11-10.
- "Not found" means not found, not that none exists.

Books: Ds Dhammasaṅgaṇī · Vb Vibhaṅga · Dt Dhātukathā · Pp Puggalapaññatti · Kv Kathāvatthu · Ya Yamaka · Pt Paṭṭhāna.

### Overview

✓ = full translation exists · ½ = partial · – = none found

| Language | Ds | Vb | Dt | Pp | Kv | Ya | Pt | Can we host it? |
|---|---|---|---|---|---|---|---|---|
| English | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ½ | Ds and Kv freely (public domain); others non-commercial |
| Japanese | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Dt only (public domain) |
| Chinese | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Non-commercial, unchanged text |
| Thai | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Royal edition possibly public domain; confirm |
| Burmese | ✓ | ✓ | ? | ✓ | ✓ | ? | ? | Possibly public domain (government work); confirm dates |
| Sinhala | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ? | Unchanged text only (CC BY-ND), subject to the 2019 gazette |
| Khmer | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Permission (Buddhist Institute) |
| Vietnamese | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Permission |
| Bengali | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Permission |
| Nepal Bhasa (Newari) | ✓ | – | ✓ | ✓ | – | ✓ | ½ | Permission (likely: given away as Dhamma gifts) |
| Hindi | – | – | ✓ | ✓ | – | – | – | Permission (print only, 2000) |
| Indonesian | ✓ | – | – | – | – | – | – | Permission |
| Korean | ✓ | – | – | – | – | – | – | No (2016, in copyright) |
| German | ✓ | – | – | ✓ | – | – | ½ | Pp public domain in US only |
| Russian | – | – | – | – | ½ | – | – | Fragments only, non-commercial |
| Nepali (Khas) | – | – | – | – | – | – | ½ | Permission |
| Marathi, Lao, Shan, Tibetan, French, Spanish, Portuguese, Italian, Gujarati, Odia, Tamil, Kannada | – | – | – | – | – | – | – | – |

### Details

| Language | Translation | Licence / status | Verdict |
|---|---|---|---|
| English | Ds: C.A.F. Rhys Davids, *A Buddhist Manual of Psychological Ethics*, PTS 1900 (2nd edn 1923) | Translator d. 1942: public domain in US, UK, EU. PTS's CC BY-NC 3.0 (2013) label adds nothing over the old text; take it from the 1900/1923 scans | **OK** |
| English | Kv: Shwe Zan Aung (d. 1932) & C.A.F. Rhys Davids (d. 1942), *Points of Controversy*, PTS 1915 | Public domain in US, UK, EU. Take it from the HathiTrust/archive.org scan, not SuttaCentral's copy (CC BY-NC label) | **OK** |
| English | Ds mātikā only: Bhikkhu Sujato, 2014 (SuttaCentral) | CC0 | **OK** (partial) |
| English | Ds mātikā, Vb 6 and 7, Pt Paccayuddesa-niddesa: Ānandajoti (ancient-buddhist-texts.net, SuttaCentral) | CC BY-SA 3.0 | **OK** (partial; share-alike) |
| English | Vb: U Thittila, *The Book of Analysis*, PTS 1969 | CC BY-NC 3.0 (PTS, 2013) | Non-commercial |
| English | Dt: U Nārada, *Discourse on Elements*, PTS 1962 | CC BY-NC 3.0 (PTS, 2013) | Non-commercial |
| English | Pp: B.C. Law, *Designation of Human Types*, PTS 1924 | Translator d. 1969: public domain in US; UK/EU from 2040; otherwise CC BY-NC 3.0 | Non-commercial (US: OK) |
| English | Pt (Tika-paṭṭhāna part): U Nārada, *Conditional Relations*, PTS 1969/81 | CC BY-NC 3.0 (PTS, 2013) | Non-commercial |
| English | Ya: U Nārada, U Kumārābhivaṁsa & U Nandamedha, *The Book of Pairs* (2020 digital, SuttaCentral) | CC BY-NC 4.0 | Non-commercial |
| English | Ya: Shaw & Cousins, PTS 2018–21 | In copyright | No |
| Japanese | Dt: 界論, 末永眞海 (d. 1940), 南伝大蔵経 vol. 47, 1940 | Public domain in Japan, US, EU. The NDL scan is in-library only, so a clean copy has to be found; the rest of vol. 47 is still in copyright | **OK** |
| Japanese | Vb: 佐藤密雄 (d. 2000); Ya: 渡邊照宏 (d. 1977) (vol. 48上 translator unverified); Pt: 山崎良順 (d. 1996); Kv: 佐藤密雄 & 佐藤良智 (d. 1978) | In copyright | No |
| Japanese | Ds: vol. 45, translator unverified; Pp: 平松友嗣 (b. 1903, death year unknown) | Unknown | Unknown |
| Chinese | All 7: 郭哲彰, 元亨寺 漢譯南傳大藏經 (CBETA N0024–N0030), translated from the Japanese Nanden | CBETA category A: CC BY-NC-SA 4.0, unchanged content, notice kept | Non-commercial |
| Chinese | Pt (partial): 范寄東 1944 (CBETA B0007), from the Japanese | CC BY-NC-SA 4.0 (CBETA category A) | Non-commercial |
| Chinese | Pp: 覺惠 2003 | © 十方法界; no licence | No |
| Thai | All 7: Royal edition (ฉบับหลวง), Dept of Religious Affairs; 4th printing 1982, first printing probably 1971 (etipitaka.com, 84000.org) | Thai government-commissioned works last 50 years from publication (Copyright Act 2537, s.14, s.23). If first printed in 1971 and unrevised, it may already be public domain | Confirm with the Dept of Religious Affairs |
| Thai | All 7: MCU 1996; Mahamakut (about 1987, with commentaries) | No licence; in copyright | Permission (MCU: tipitaka.tsj@mcu.ac.th) |
| Burmese | Ds, Vb, Pp, Kv (likely Dt too, same volume as Pp): ပိဋကတ်တော် မြန်မာပြန်, Dept of Religious Affairs; digital text on Myanmar Wikisource | Undated; no licence tag. Government works last 50 years from publication (2019 law, s.17(a)(5)) | Possibly public domain; confirm first-edition dates |
| Burmese | Palm-leaf *nissaya* (word-by-word translations) of all books (BDRC on archive.org; British Library EAP) | Old manuscripts; images only | Not practical |
| Sinhala | Ds, Vb, Dt, Pp, Kv, Ya: Buddha Jayanti Tipiṭaka Sinhala translation (tipitaka.lk; Kv = vol. 45, 1968). Pt: the Sinhala side is empty online | tipitaka.lk licenses the BJT Sinhala translation (not only the Pāli) as CC BY-ND 4.0. A 2019 gazette requires approval to reprint the Canon and its Sinhala version | Unchanged text: likely OK under ND; confirm with tipitaka.lk and the Tripitaka Conservation Board |
| Sinhala | A.P. de Zoysa, *Sinhala Tripiṭakaya* (incl. Pt, 1959) | Translator d. 1968: in copyright to 2038 | No |
| Khmer | All 7: Buddhist Institute bilingual edition, vols 78–110 (1950s–60s); scans on 5000-years.org and Wikisource | No notice; likely in copyright into the 2030s–40s | Permission (Buddhist Institute) |
| Vietnamese | All 7: HT Tịnh Sự (Santakicco) (archive.org PDFs from theravada.vn; Pt audio only) | No licence; life + 50 (death year unconfirmed) | Permission |
| Bengali | All 7: *Pabitra Tripitak*, Tripitaka Publishing Society, Rangamati, 25 vols, 2017 | No licence | Permission |
| Bengali | Ds, Vb, Dt, Pp, Kv, Ya (PDFs, Rajban Vihara blogs, 2014); Pt "Bengali-Pali" volumes | Translators unknown; Pt may be transliteration | Unknown |
| Nepal Bhasa | Ds: Anagārikā Aggañāṇī, 2017 · Dt: Bhikkhu Dharmagupta, 2019 · Pp: Bhikkhu Dharmagupta, 2007 · Ya: Anagārikā Vimalañāṇī, 2018 · Pt conditions section: Bhikṣu Buddhaghoṣa (about 1982), Bhikṣu Gyānapūrṇika (1987). All on dhamma.digital | No licence; in copyright | Permission (Vīr Pūrṇa Pustak Saṅgrahālaya / dhamma.digital) |
| Nepali | Pt: *Paṭṭhāna Pāli Desanā*, ed. Dolendra Ratna Shakya, 2013 (an exposition, not a full translation) | No licence | Permission |
| Hindi | Dt + Pp: Om Prakash Pathak (tr.) & Veena Gaur (ed.), New Bharatiya Book, Delhi, 2000, ISBN 8187418141. CiNii: "In Pali and Hindi". Exotic India's NAJ549 is a different book (Eastern Book Linkers, English translation). Print only | In copyright | Permission |
| Indonesian | Ds: Chaidir Thamrin, Indonesia Tipitaka Center, Medan, 2018 | "Free distribution" (unconfirmed); no licence | Permission |
| Korean | Ds: 각묵, 초기불전연구원, 2 vols, 2016 | In copyright | No |
| German | Pp: Nyanatiloka, 1910 (d. 1957) | Public domain in US; EU from 2028 | US only |
| German | Ds: Nyanaponika (© Buddhist Publication Society); Pt 1.1–1.3: Agganyani (no licence) | In copyright | No / Unknown |
| Russian | Kv fragments: Ložkina 2021 (CC BY-NC 4.0); her 2019 dissertation (Kv I.1, no licence) | | Non-commercial / Unknown |
| Mon | "Tipitaka Mon" app claims Abhidhamma translations; books unnamed | © Mon Tipitaka Translate Group | Permission |

**Transliterations, not translations** (Pāli in another script, no translation):
- the Nālandā Devanāgarī Pāli series, ed. Bhikkhu J. Kashyap, 1958–61, all 7 books (2017 Nava Nalanda reprint); Digital Library of India scans on archive.org are mislabelled "hin" or "san";
- Bapat & Vadekar, Dhammasaṅgaṇī, BORI Pune 1940 (Devanāgarī Pāli with an English introduction);
- Vipassana Vishodhan Vinyas Devanāgarī CST, 1998 (Hindi summaries, no translation);
- tipitaka.app (CST Pāli in 22 scripts, no translations);
- LBDFI/ITCC chanting books in all scripts;
- the Thai Siam-raṭṭha Pāli, the Burmese Chaṭṭha Saṅgāyana Pāli, tipitaka.org's Khmer-script Pāli, the Pāli side of BJT, and the 2024 Pali-Lao script edition (most likely Pāli only);
- guides that are not translations: Nyanatiloka's *Guide through the Abhidhamma-Piṭaka*, U Nārada's *Guide to Conditional Relations*.

**Not the seven books** (Abhidhammattha-saṅgaha and commentaries, for a commentary track):
- English: *Compendium of Philosophy* (Shwe Zan Aung & Rhys Davids, 1910), **public domain**.
- English: *Dispeller of Delusion* (Ñāṇamoli, Vb commentary), CC BY-NC 4.0.
- Hindi: Abhidhammattha-saṅgaha by Revatadhamma & Tripathi (Sampurnanand).
- Nepal Bhasa and Nepali: Abhidhammattha-saṅgaha translations on dhamma.digital.
- Vietnamese: Tịnh Sự's *Siêu Lý Hiệp Đồng*.

**Conclusion:**
- **Hostable now, freely:**
  - English Dhammasaṅgaṇī (1900) and Kathāvatthu (1915);
  - the Japanese Dhātukathā (1940), once a clean scan is found;
  - short English sections by Sujato (CC0) and Ānandajoti (CC BY-SA).
- **Hostable only if the platform is non-commercial:** the other PTS English translations and the Chinese 元亨寺 set.
- **Worth confirming, because they may already be public domain as government works:**
  - the Thai Royal edition (all 7);
  - the Burmese Religious Affairs translation;
  - the Sinhala BJT translation, already CC BY-ND, which allows unchanged hosting.
- **Hindi:** only the Dhātukathā and Puggalapaññatti exist (2000, print, in copyright). The other five books have no Hindi translation, and nothing Hindi is free to host. Marathi has nothing.
- **Best permission requests:**
  - Nepal Bhasa: four complete books, already given away free;
  - the Bengali *Pabitra Tripitak*: all 7;
  - the Khmer Buddhist Institute: all 7.

**Pāli base text.** SuttaCentral's Mahāsaṅgīti Pāli is CC0. tipitaka.org (VRI CST), the source of this vault's root texts, states no licence and only encourages academic, personal and monastic use. tipitaka.app, which reuses the same CST text, describes it as free for non-commercial use. The vault's root-text frontmatter says `license: cc0`, which should be checked.

**Sources:**
- Licences:
  - https://palitextsociety.org/copyright-information/
  - https://www.cbeta.org/copyright
  - https://raw.githubusercontent.com/pathnirvana/tipitaka.lk/master/LICENSE.md
  - https://ancient-buddhist-texts.net/Miscellaneous/Copyright-Notice.htm
  - https://tipitaka.app/deva/about
- SuttaCentral:
  - https://suttacentral.net/api/suttaplex/kv1.1
  - https://suttacentral.net/api/suttas/ds1.1/sujato?lang=en
  - https://suttacentral.net/api/suttas/ya1.1.1/unarada?lang=en
- Public-domain scans and translator death years:
  - https://catalog.hathitrust.org/Record/103027737
  - https://catalog.hathitrust.org/Record/102047083
  - https://en.wikipedia.org/wiki/Caroline_Rhys_Davids
  - https://en.wikipedia.org/wiki/Shwe_Zan_Aung
  - https://royalasiaticcollections.org/ras-01-009-bimala-churn-law-1892-1969-indologist/
- Japanese Nanden translators:
  - https://ndlsearch.ndl.go.jp/en/books/R100000126-I20001527
  - https://ndlsearch.ndl.go.jp/en/books/R100000126-I20001537
  - https://ndlsearch.ndl.go.jp/en/books/R100000126-I20001538
- Chinese: https://cbdata.dila.edu.tw/stable/works?work=N0024
- Thai: https://etipitaka.com and https://ndlsearch.ndl.go.jp/en/books/R100000002-Ia1000046132
- Thai copyright law: https://en.wikisource.org/wiki/Translation:Copyright_Act,_2537_BE
- Burmese: https://my.wikisource.org/wiki/ဓမ္မသင်္ဂဏီပါဠိတော်
- Copyright terms by country: https://commons.wikimedia.org/wiki/Commons:Copyright_rules_by_territory/Myanmar
- Sinhala:
  - https://www.sjp.ac.lk/news/download-theravada-tripitaka/
  - https://opac.busl.ac.lk/bib/18922
  - https://www.ft.lk/News/Tripitaka-Conservation-Board-appointed/56-683104
- Khmer:
  - https://discourse.suttacentral.net/t/help-me-find-ebts-in-khmer/22954
  - https://akp.gov.kh/post/detail/361725
- Vietnamese: https://archive.org/details/1-abhi-phap-tu
- Bengali:
  - https://www.buddhisttimes.news/bangla-translation-of-the-entire-pali-tripitaka-presented-in-bangladesh/
  - https://discourse.suttacentral.net/t/the-entire-tipitaka-has-been-translated-in-bangla/19495
- Nepal Bhasa:
  - https://dhamma.digital/sae_books/dhamrmasangini/
  - https://dhamma.digital/sae_books/dhatukatha/
  - https://dhamma.digital/sae_books/bhikkhu_dhammagupta_puggalapanyati/
  - https://dhamma.digital/sae_books/yamaka-anagarika-vimalanani/
  - https://ramroonline.com/news/abhidhmm-pitkko-sandrbhikta
- Hindi:
  - https://ci.nii.ac.jp/ncid/BA49053865
  - https://www.exoticindiaart.com/book/details/puggalapannattipali-abhidhammapitake-naj549/
  - https://archive.org/details/in.ernet.dli.2015.321073
- Marathi: https://www2.buddhistdoor.net/news/government-of-maharashtra-approves-project-to-translate-tripitaka-into-marathi
- Lao: https://kpl.gov.la/En/detail.aspx?id=88023
- Korean: https://seoul.co.kr/news/life/2016/06/02/20160602500181
- Russian: https://frai.iphras.ru/article/view/6177

This is not legal advice.

## Previous ranking (2026-11-06, general reader demand)

The earlier score was `demand × gap`, where demand was Wikipedia pageviews plus community size (script `score.py`; data in `wiki_pageviews.json` and `google_trends.md`). It ranked:

| Rank | Language | Score |
|---|---|---|
| 1 | Russian | 0.87 |
| 2 | Hindi | 0.79 |
| 3 | Marathi | 0.78 |
| 4 | French | 0.74 |
| 5 | Nepali | 0.67 |
| 6 | Japanese | 0.49 |
| 6 | Chinese | 0.49 |
| 8 | Mongolian | 0.40 |
| 9 | Thai | 0.19 |
| 10 | Vietnamese | 0.18 |

It still describes general online demand. The ITCC ranking above replaces it for the Daily Tipitaka audience.
