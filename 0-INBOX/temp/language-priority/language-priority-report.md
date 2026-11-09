---
title: Abhidhamma translation — language priority ranking
date: 2026-11-06
status: draft
scope: supported languages minus pi (source) and en (done); i9 "i9138probe" excluded as a test entry
---

# Abhidhamma translation — which language next?

## Result

| Rank | Lang | Priority | Why |
|---|---|---|---|
| 1 | **Russian (ru)** | 0.87 | Highest reader interest among untranslated languages (20.7k Wikipedia views/yr on Abhidhamma topics, 2nd only to ja/zh). No Russian Abhidhamma translation found. |
| 2 | **Hindi (hi)** | 0.79 | No full translation found (only an *epitome*). Wikipedia undercounts Hindi readers (many read English Wikipedia). Devanagari also reaches Marathi and Nepali readers. |
| 3 | **Marathi (mr)** | 0.78 | 6.53 M Buddhists (77% of India's Buddhists) — the largest Buddhist community with **no** translation at all. |
| 4 | **French (fr)** | 0.74 | ~600k Buddhists; 16k/yr Theravāda article views; no translation found. |
| 5 | **Nepali (ne)** | 0.67 | 2.39 M Buddhists; no translation found; very low online signal. |
| 6 | Japanese (ja) | 0.49 | Top demand, but full translation exists (Nanden Daizōkyō vols 45–58) — pre-war literary Japanese, not modern. |
| 6 | Chinese (zh) | 0.49 | Top demand, but full translation exists (Yuan Heng Si, traditional characters; quality widely criticised). |
| 8 | Mongolian (mn) | 0.40 | 1.7 M Buddhists, zero measurable online interest; Tibetan-tradition (Abhidharmakośa) rather than Pāli. |
| 9 | Thai (th) | 0.19 | Complete Thai Tipiṭaka already exists. |
| 10 | Vietnamese (vi) | 0.18 | All seven books translated by HT Tịnh Sự (pub. 2011). |
| — | Tibetan (bo) | 0.00 | No measurable signal; no cited population figure. |
| — | Sanskrit (sa), Classical Chinese (lzh) | n/a | Classical languages: no living reader community to serve. Recommend dropping from this project. |

**Recommendation:** Tier 1 = **Russian, Hindi, Marathi** (scores within 0.1 of each other — treat as a three-way tie and pick by translator availability). Tier 2 = French, Nepali. Tier 3 = a *modern* Japanese / simplified-Chinese retranslation, only if the existing versions prove unusable.

## Method

`priority = demand × gap`

- **demand** = ½ reader interest + ½ community size, each log-scaled 0–1 across candidates.
  - *Reader interest*: Wikipedia user pageviews, Nov 2025–Oct 2026, summed over the articles *Abhidhamma Piṭaka*, *Abhidharma*, *Pali Canon* in each language edition (Wikimedia Pageviews API, via Wikidata sitelinks).
  - *Community size*: Buddhists whose main reading language is this one.
- **gap** = 1.0 no full translation found · 0.5 full translation exists but dated/criticised · 0.2 full and current.

Script: `score.py`; raw data: `wiki_pageviews.json`, `google_trends.md` (this folder).

## Data

### Wikipedia pageviews (12 months)

| Lang | Abhidhamma Piṭaka | Abhidharma | Pali Canon | Theravāda | Buddhism |
|---|---|---|---|---|---|
| en (ref) | 16,260 | 37,963 | 69,524 | 235,720 | 1,408,309 |
| ja | 1,847 | 8,084 | 17,514 | 68,221 | 168,129 |
| zh | 2,958 | 8,329 | 12,081 | 44,566 | 134,570 |
| ru | 1,640 | 4,298 | 14,767 | 46,295 | 297,845 |
| th | 7,688 | — | 5,331 | 14,306 | 40,166 |
| vi | 957 | 2,249 | 2,723 | 6,246 | 49,074 |
| hi | 1,950 | 363 | 536 | 2,785 | 59,779 |
| fr | — | 1,441 | 404 | 16,186 | 133,962 |
| mr | — | 1,253 | — | 506 | 12,339 |
| ne | 90 | — | 107 | 239 | 1,855 |
| bo | — | — | — | 99 | 756 |
| mn | — | — | — | — | 4,850 |
| lzh | — | — | — | — | 1,460 |
| sa | — | — | — | — | 632 |

"—" = article does not exist in that edition.

### Google Trends (worldwide, 12 months, one rescaled axis)
อภิธรรม (th) 162 — but dominated by funeral-chanting queries, not study · Abhidhamma (Latin) 64 · Abhidharma 33 · Vi Diệu Pháp (vi) 10 · 阿毘達磨 (zh-trad) 8 · 阿毗达磨 (zh-simp) 1 · अभिधम्म, アビダルマ, Абхидхарма 0.
Latin "Abhidhamma" by country intensity: Myanmar 100, Sri Lanka 48, Singapore 10, Korea/India/Vietnam/Indonesia 5.
Not used in the score (too sparse, and Google is blocked in mainland China).

### Community size

| Lang | Millions | Source |
|---|---|---|
| th | 68 | Pew 2025 (2020 data) |
| zh | 53 | Pew 2025 (2020 data) |
| ja | 41.4 | Pew-attributed secondary list — **unverified** |
| vi | 15.6 | Pew-attributed secondary list — **unverified** |
| mr | 6.53 | Census of India 2011 (Maharashtra) |
| ne | 2.39 | Nepal Census 2021 |
| hi | 1.91 | India 2011 (8.44 M) minus Maharashtra (6.53 M) — upper bound; Hindi Vipassana audience not counted |
| mn | 1.70 | Mongolia Census 2020 |
| ru | 0.9 | "ethnic Buddhists" in Buryatia/Kalmykia/Tuva (range 0.5–2 M) |
| fr | 0.6 | Union bouddhiste de France estimate |

### Existing translations

| Lang | Status | Source |
|---|---|---|
| th | Complete (Royal Thai edition, 80 vols, 1957; MCU edition 1996) | trueplookpanya.com; tci-thaijo.org |
| vi | Complete — 7 books, HT Tịnh Sự (Santakicco), Nxb Tôn giáo 2011 | thuvienhoasen.org |
| ja | Complete — Nanden Daizōkyō vols 45–58; not modern Japanese | NDL; Nagoya City Library |
| zh | Complete — Yuan Heng Si 漢譯南傳大藏經 nos. 24–30; quality criticised | Lin Chong-an (NCU); NTU Buddhism Library |
| hi | Epitome only (Rewatadhamma & Tripāṭhī) | UPenn catalogue |
| mr, ru, fr, ne, bo | None found | searches 2026-11-06 |
| mn | Not searched in depth | — |
| SuttaCentral | Dhammasaṅgaṇī in en + de only | suttacentral.net API |

## Caveats

1. **No site analytics.** SuttaCentral, tipitaka.org etc. do not publish visitor analytics. **Your own WeBuddhist / Daily Tipitaka analytics by language would beat every signal here** — add them as a third demand column if available.
2. Wikipedia undercounts South Asian languages (hi, mr, ne readers often use English Wikipedia).
3. "None found" means not found in web search in Hindi/Marathi/Nepali/Russian/French — not proof of absence. A catalogue check (e.g. Vipassana Research Institute, Marathi Buddhist presses) before committing is worthwhile.
4. Gap values are judgement calls. If ja/zh are given gap 0.7 instead of 0.5 (on the grounds that their translations are dated), they score 0.69 and move between French and Nepali.
5. Myanmar and Sri Lanka show the highest Abhidhamma search intensity, but Burmese and Sinhala are not on the supported list (and both already have translations).

## Sources
- Wikimedia Pageviews API — https://wikimedia.org/api/rest_v1/
- Google Trends — https://trends.google.com/trends/explore?date=today%2012-m&q=Abhidhamma
- Pew Research, Buddhist population change (2025) — https://www.pewresearch.org/religion/2025/06/09/buddhist-population-change/
- Pew-attributed 2025 list — https://www.findeasy.in/asia-population-by-religion/
- Marathi Buddhists (Census 2011) — https://en.wikipedia.org/wiki/Marathi_Buddhists ; https://ncert.nic.in/degsn/pdf/elementary-report.pdf
- Nepal Census 2021 — https://english.onlinekhabar.com/national-population-census-religion.html
- Mongolia Census 2020 — https://en.wikipedia.org/wiki/Religion_in_Mongolia
- Buddhism in Russia — https://en.wikipedia.org/wiki/Buddhism_in_Russia
- Buddhism in France — https://en.wikipedia.org/wiki/Buddhism_in_France
- Thai Tipiṭaka — https://www.trueplookpanya.com/knowledge/content/60108
- Vietnamese (Tịnh Sự) — https://thuvienhoasen.org/images/file/1nCO-JVO2QgQAOQK/bo-ngu-tong-1-bhikkhu-santakicco-tinh-su.pdf
- Japanese Nanden Daizōkyō — https://ndlsearch.ndl.go.jp/en/books/R100000002-I000001243807 ; https://www.library.city.nagoya.jp/img/reference/0301.pdf
- Chinese Yuan Heng Si — https://web.ss.ncu.edu.tw/~calin/article2008/28_2.pdf ; https://buddhism.lib.ntu.edu.tw/FT/JA/641204.pdf
- Hindi epitome — https://find.library.upenn.edu/catalog/997367683503681
- SuttaCentral — https://suttacentral.net/api/suttaplex/ds
