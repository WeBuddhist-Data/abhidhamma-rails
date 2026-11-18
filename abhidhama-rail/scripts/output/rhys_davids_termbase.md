---
title: TF-IDF Vocabulary Analysis — Rhys Davids Dhammasaṅgaṇī (1900)
source: 1-SOURCES/Translations/English/en-1-rhys_davids.md
corpus: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth_idf=True)
method: TF × IDF — term frequency in translation vs. inverse document frequency in Reuters corpus
generated: 2026-06-04
unique_terms: 2247
total_content_tokens: 20,711
status: draft
---

# TF-IDF Vocabulary Analysis — Rhys Davids Translation

Generated **2026-06-04** · source: `en-1-rhys_davids.md` · **2,247 unique content terms** ranked.

This report answers two questions:

1. **Which words in this translation are most frequent here but rare in everyday English?**  
   → High TF-IDF score. These are the lexical signatures of the text.
2. **Which words appear in the text but are also very common in general English?**  
   → Low TF-IDF score. These look familiar but carry specialist meaning here.

---

## Methodology

**Term Frequency (TF)** — count of each word in the translation, normalised by total content-token count.
Frontmatter, verse markers (`^1-2`), numbers and markdown syntax are stripped before counting.

**Inverse Document Frequency (IDF)** — computed from the Reuters-21578 newswire corpus
(10,788 documents, ~1.3 M tokens) using sklearn's smooth IDF formula:
`idf(t) = log((1 + N) / (1 + df(t))) + 1`. Corpus maximum ≈ 9.59. Scale:

| IDF range | Meaning |
|-----------|---------|
| 1.0 – 1.5 | Function word — present in virtually every document |
| 1.5 – 3.0 | Common content word — high general-English frequency |
| 3.0 – 6.0 | Moderately rare — limited domain or register |
| 6.0 – 9.0 | Uncommon / archaic — rare in Reuters |
| 9.59 (max) | Absent from Reuters — domain-exclusive, coined, or Pāli |

**TF-IDF score** = TF × IDF × 10⁶ (scaled for readability).

**Colour bands** used in the table:

| Band | Score range | Interpretation |
|------|-------------|----------------|
| 🔴 | ≥ 50,000 | Text-exclusive — word essentially does not exist outside this translation |
| 🟠 | 10,000 – 49,999 | Domain-specific — Buddhist / Abhidhamma vocabulary |
| 🟡 | 3,000 – 9,999 | Specialist register — unusual in general English |
| 🟢 | 500 – 2,999 | Moderately distinctive — identifiable domain presence |
| 🔵 | 50 – 499 | Moderately common — has general English presence |
| ⚪ | 0 – 49 | Universal / function word |

---

## Distribution by Band

| Band | Terms | % of vocabulary |
|------|-------|----------------|
| 🔴 extremely high — text-exclusive | 17 | 0.8% |
| 🟠 very high — domain-specific | 161 | 7.2% |
| 🟡 high — specialist register | 279 | 12.4% |
| 🟢 medium — moderately distinctive | 802 | 35.7% |
| 🔵 low — common in general English | 988 | 44.0% |
| ⚪ very low — function / universal word | 0 | 0.0% |

---

## Most Distinctive Words (highest TF-IDF)

Words that appear **frequently in this text** yet are **rare or absent in general English**.
These are the genuine lexical fingerprints of the Rhys Davids translation.

**1. states** — count: 743, TF-IDF: 143,110, IDF: 3.989173 🔴 extremely high — text-exclusive
**2. form** — count: 560, TF-IDF: 139,104, IDF: 5.144619 🔴 extremely high — text-exclusive
**3. occasion** — count: 308, TF-IDF: 120,295, IDF: 8.089058 🔴 extremely high — text-exclusive
**4. material** — count: 348, TF-IDF: 102,187, IDF: 6.08159 🔴 extremely high — text-exclusive
**5. sphere** — count: 207, TF-IDF: 95,849, IDF: 9.59 🔴 extremely high — text-exclusive
**6. contact** — count: 258, TF-IDF: 86,628, IDF: 6.954078 🔴 extremely high — text-exclusive
**7. bodily** — count: 182, TF-IDF: 84,273, IDF: 9.59 🔴 extremely high — text-exclusive
**8. thought** — count: 244, TF-IDF: 70,965, IDF: 6.023602 🔴 extremely high — text-exclusive
**9. element** — count: 192, TF-IDF: 69,655, IDF: 7.513694 🔴 extremely high — text-exclusive
**10. faculty** — count: 143, TF-IDF: 66,215, IDF: 9.59 🔴 extremely high — text-exclusive
**11. jhāna** — count: 143, TF-IDF: 66,215, IDF: 9.59 🔴 extremely high — text-exclusive
**12. skandhas** — count: 134, TF-IDF: 62,047, IDF: 9.59 🔴 extremely high — text-exclusive
**13. etc** — count: 129, TF-IDF: 57,226, IDF: 9.18767 🔴 extremely high — text-exclusive
**14. mental** — count: 118, TF-IDF: 54,656, IDF: 9.593135 🔴 extremely high — text-exclusive
**15. indeterminate** — count: 115, TF-IDF: 53,249, IDF: 9.59 🔴 extremely high — text-exclusive
**16. feeling** — count: 149, TF-IDF: 53,208, IDF: 7.395911 🔴 extremely high — text-exclusive
**17. consciousness** — count: 114, TF-IDF: 52,804, IDF: 9.593135 🔴 extremely high — text-exclusive
**18. mind** — count: 141, TF-IDF: 48,682, IDF: 7.150788 🟠 very high — domain-specific
**19. object** — count: 117, TF-IDF: 45,696, IDF: 8.089058 🟠 very high — domain-specific
**20. spheres** — count: 97, TF-IDF: 44,915, IDF: 9.59 🟠 very high — domain-specific
**21. nutriment** — count: 97, TF-IDF: 44,915, IDF: 9.59 🟠 very high — domain-specific
**22. perception** — count: 117, TF-IDF: 42,811, IDF: 7.578232 🟠 very high — domain-specific
**23. born** — count: 92, TF-IDF: 42,614, IDF: 9.593135 🟠 very high — domain-specific
**24. aloof** — count: 86, TF-IDF: 39,821, IDF: 9.59 🟠 very high — domain-specific
**25. indifference** — count: 84, TF-IDF: 38,895, IDF: 9.59 🟠 very high — domain-specific
**26. karma** — count: 84, TF-IDF: 38,895, IDF: 9.59 🟠 very high — domain-specific
**27. volition** — count: 83, TF-IDF: 38,445, IDF: 9.593135 🟠 very high — domain-specific
**28. having** — count: 136, TF-IDF: 36,985, IDF: 5.632322 🟠 very high — domain-specific
**29. cognition** — count: 78, TF-IDF: 36,117, IDF: 9.59 🟠 very high — domain-specific
**30. formless** — count: 77, TF-IDF: 35,654, IDF: 9.59 🟠 very high — domain-specific
**31. bad** — count: 117, TF-IDF: 34,886, IDF: 6.175409 🟠 very high — domain-specific
**32. accompanied** — count: 90, TF-IDF: 34,693, IDF: 7.983697 🟠 very high — domain-specific
**33. answer** — count: 106, TF-IDF: 34,598, IDF: 6.759922 🟠 very high — domain-specific
**34. visible** — count: 99, TF-IDF: 34,181, IDF: 7.150788 🟠 very high — domain-specific
**35. taste** — count: 77, TF-IDF: 34,158, IDF: 9.18767 🟠 very high — domain-specific
**36. reacting** — count: 91, TF-IDF: 32,747, IDF: 7.453069 🟠 very high — domain-specific
**37. arisen** — count: 82, TF-IDF: 32,493, IDF: 8.206841 🟠 very high — domain-specific
**38. invisible** — count: 80, TF-IDF: 32,216, IDF: 8.340372 🟠 very high — domain-specific
**39. sense** — count: 98, TF-IDF: 31,586, IDF: 6.675364 🟠 very high — domain-specific
**40. whatever** — count: 91, TF-IDF: 31,232, IDF: 7.108229 🟠 very high — domain-specific
**41. sensuous** — count: 67, TF-IDF: 31,024, IDF: 9.59 🟠 very high — domain-specific
**42. abides** — count: 67, TF-IDF: 31,024, IDF: 9.59 🟠 very high — domain-specific
**43. tangible** — count: 81, TF-IDF: 30,198, IDF: 7.721333 🟠 very high — domain-specific
**44. associated** — count: 105, TF-IDF: 29,870, IDF: 5.891833 🟠 very high — domain-specific
**45. synergies** — count: 69, TF-IDF: 29,651, IDF: 8.899988 🟠 very high — domain-specific
**46. skandha** — count: 64, TF-IDF: 29,634, IDF: 9.59 🟠 very high — domain-specific
**47. enters** — count: 67, TF-IDF: 28,791, IDF: 8.899988 🟠 very high — domain-specific
**48. unincluded** — count: 62, TF-IDF: 28,708, IDF: 9.59 🟠 very high — domain-specific
**49. answers** — count: 66, TF-IDF: 28,362, IDF: 8.899988 🟠 very high — domain-specific
**50. concentration** — count: 69, TF-IDF: 28,300, IDF: 8.494523 🟠 very high — domain-specific

---

## Least Distinctive Words (lowest TF-IDF)

Words that appear in this text but are also extremely common in general English,
giving them a near-zero TF-IDF score despite sometimes occurring hundreds of times here.

**1. said** — count: 2, TF-IDF: 141.36, IDF: 1.463813 🔵 low — common in general English
**2. stock** — count: 1, TF-IDF: 147.30, IDF: 3.050663 🔵 low — common in general English
**3. current** — count: 1, TF-IDF: 167.00, IDF: 3.458653 🔵 low — common in general English
**4. includes** — count: 1, TF-IDF: 184.68, IDF: 3.824814 🔵 low — common in general English
**5. time** — count: 1, TF-IDF: 185.51, IDF: 3.842151 🔵 low — common in general English
**6. around** — count: 1, TF-IDF: 186.99, IDF: 3.872823 🔵 low — common in general English
**7. including** — count: 1, TF-IDF: 197.47, IDF: 4.089838 🔵 low — common in general English
**8. firm** — count: 1, TF-IDF: 205.71, IDF: 4.260416 🔵 low — common in general English
**9. tender** — count: 1, TF-IDF: 205.82, IDF: 4.262835 🔵 low — common in general English
**10. held** — count: 1, TF-IDF: 206.06, IDF: 4.267689 🔵 low — common in general English
**11. subject** — count: 1, TF-IDF: 213.95, IDF: 4.43121 🔵 low — common in general English
**12. issue** — count: 1, TF-IDF: 214.51, IDF: 4.442738 🔵 low — common in general English
**13. days** — count: 1, TF-IDF: 215.36, IDF: 4.460282 🔵 low — common in general English
**14. decline** — count: 1, TF-IDF: 219.21, IDF: 4.540079 🔵 low — common in general English
**15. low** — count: 1, TF-IDF: 219.37, IDF: 4.543279 🔵 low — common in general English
**16. used** — count: 1, TF-IDF: 220.46, IDF: 4.565971 🔵 low — common in general English
**17. within** — count: 1, TF-IDF: 220.78, IDF: 4.57255 🔵 low — common in general English
**18. number** — count: 1, TF-IDF: 221.58, IDF: 4.589189 🔵 low — common in general English
**19. account** — count: 1, TF-IDF: 227.07, IDF: 4.702786 🔵 low — common in general English
**20. inflation** — count: 1, TF-IDF: 233.88, IDF: 4.843865 🔵 low — common in general English
**21. gold** — count: 1, TF-IDF: 234.94, IDF: 4.865747 🔵 low — common in general English
**22. ending** — count: 1, TF-IDF: 236.02, IDF: 4.88812 🔵 low — common in general English
**23. response** — count: 1, TF-IDF: 238.94, IDF: 4.948744 🔵 low — common in general English
**24. seeking** — count: 1, TF-IDF: 239.88, IDF: 4.968162 🔵 low — common in general English
**25. small** — count: 1, TF-IDF: 239.88, IDF: 4.968162 🔵 low — common in general English
**26. company** — count: 2, TF-IDF: 241.79, IDF: 2.503892 🔵 low — common in general English
**27. adding** — count: 1, TF-IDF: 242.56, IDF: 5.023592 🔵 low — common in general English
**28. rises** — count: 1, TF-IDF: 243.57, IDF: 5.044535 🔵 low — common in general English
**29. again** — count: 1, TF-IDF: 244.60, IDF: 5.065927 🔵 low — common in general English
**30. consider** — count: 1, TF-IDF: 246.46, IDF: 5.104499 🔵 low — common in general English
**31. quoted** — count: 1, TF-IDF: 247.28, IDF: 5.121496 🔵 low — common in general English
**32. heavy** — count: 1, TF-IDF: 247.56, IDF: 5.127227 🔵 low — common in general English
**33. producing** — count: 1, TF-IDF: 253.46, IDF: 5.24933 🔵 low — common in general English
**34. changed** — count: 1, TF-IDF: 253.77, IDF: 5.255844 🔵 low — common in general English
**35. principle** — count: 1, TF-IDF: 257.71, IDF: 5.337522 🔵 low — common in general English
**36. performance** — count: 1, TF-IDF: 259.10, IDF: 5.366301 🔵 low — common in general English
**37. limit** — count: 1, TF-IDF: 260.17, IDF: 5.388443 🔵 low — common in general English
**38. find** — count: 1, TF-IDF: 263.15, IDF: 5.45 🔵 low — common in general English
**39. needs** — count: 1, TF-IDF: 267.56, IDF: 5.54135 🔵 low — common in general English
**40. rest** — count: 1, TF-IDF: 267.98, IDF: 5.550084 🔵 low — common in general English
**41. series** — count: 1, TF-IDF: 267.98, IDF: 5.550084 🔵 low — common in general English
**42. mine** — count: 1, TF-IDF: 268.83, IDF: 5.567784 🔵 low — common in general English
**43. outside** — count: 1, TF-IDF: 269.70, IDF: 5.585802 🔵 low — common in general English
**44. items** — count: 1, TF-IDF: 269.70, IDF: 5.585802 🔵 low — common in general English
**45. bond** — count: 1, TF-IDF: 271.04, IDF: 5.613454 🔵 low — common in general English
**46. property** — count: 1, TF-IDF: 272.41, IDF: 5.641891 🔵 low — common in general English
**47. developing** — count: 1, TF-IDF: 273.35, IDF: 5.66131 🔵 low — common in general English
**48. opening** — count: 1, TF-IDF: 273.82, IDF: 5.671162 🔵 low — common in general English
**49. building** — count: 1, TF-IDF: 274.30, IDF: 5.681112 🔵 low — common in general English
**50. generally** — count: 1, TF-IDF: 276.28, IDF: 5.721934 🔵 low — common in general English

---

## Full Ranked Table

All 2,247 content terms, sorted by TF-IDF descending.

| Rank | Word | Count | TF-IDF | IDF | Band |
|------|------|-------|--------|-----|------|
| 1 | **states** | 743 | 143,110.21 | 3.989173 | 🔴 extremely high — text-exclusive |
| 2 | **form** | 560 | 139,104.18 | 5.144619 | 🔴 extremely high — text-exclusive |
| 3 | **occasion** | 308 | 120,295.01 | 8.089058 | 🔴 extremely high — text-exclusive |
| 4 | **material** | 348 | 102,186.92 | 6.08159 | 🔴 extremely high — text-exclusive |
| 5 | **sphere** | 207 | 95,849.07 | 9.59 | 🔴 extremely high — text-exclusive |
| 6 | **contact** | 258 | 86,627.98 | 6.954078 | 🔴 extremely high — text-exclusive |
| 7 | **bodily** | 182 | 84,273.09 | 9.59 | 🔴 extremely high — text-exclusive |
| 8 | **thought** | 244 | 70,965.13 | 6.023602 | 🔴 extremely high — text-exclusive |
| 9 | **element** | 192 | 69,655.22 | 7.513694 | 🔴 extremely high — text-exclusive |
| 10 | **faculty** | 143 | 66,214.57 | 9.59 | 🔴 extremely high — text-exclusive |
| 11 | **jhāna** | 143 | 66,214.57 | 9.59 | 🔴 extremely high — text-exclusive |
| 12 | **skandhas** | 134 | 62,047.22 | 9.59 | 🔴 extremely high — text-exclusive |
| 13 | **etc** | 129 | 57,226.08 | 9.18767 | 🔴 extremely high — text-exclusive |
| 14 | **mental** | 118 | 54,656.46 | 9.593135 | 🔴 extremely high — text-exclusive |
| 15 | **indeterminate** | 115 | 53,249.48 | 9.59 | 🔴 extremely high — text-exclusive |
| 16 | **feeling** | 149 | 53,207.99 | 7.395911 | 🔴 extremely high — text-exclusive |
| 17 | **consciousness** | 114 | 52,803.70 | 9.593135 | 🔴 extremely high — text-exclusive |
| 18 | **mind** | 141 | 48,682.40 | 7.150788 | 🟠 very high — domain-specific |
| 19 | **object** | 117 | 45,696.48 | 8.089058 | 🟠 very high — domain-specific |
| 20 | **spheres** | 97 | 44,914.78 | 9.59 | 🟠 very high — domain-specific |
| 21 | **nutriment** | 97 | 44,914.78 | 9.59 | 🟠 very high — domain-specific |
| 22 | **perception** | 117 | 42,810.74 | 7.578232 | 🟠 very high — domain-specific |
| 23 | **born** | 92 | 42,613.51 | 9.593135 | 🟠 very high — domain-specific |
| 24 | **aloof** | 86 | 39,821.35 | 9.59 | 🟠 very high — domain-specific |
| 25 | **indifference** | 84 | 38,895.27 | 9.59 | 🟠 very high — domain-specific |
| 26 | **karma** | 84 | 38,895.27 | 9.59 | 🟠 very high — domain-specific |
| 27 | **volition** | 83 | 38,444.80 | 9.593135 | 🟠 very high — domain-specific |
| 28 | **having** | 136 | 36,984.97 | 5.632322 | 🟠 very high — domain-specific |
| 29 | **cognition** | 78 | 36,117.04 | 9.59 | 🟠 very high — domain-specific |
| 30 | **formless** | 77 | 35,654.00 | 9.59 | 🟠 very high — domain-specific |
| 31 | **bad** | 117 | 34,885.95 | 6.175409 | 🟠 very high — domain-specific |
| 32 | **accompanied** | 90 | 34,693.29 | 7.983697 | 🟠 very high — domain-specific |
| 33 | **answer** | 106 | 34,597.64 | 6.759922 | 🟠 very high — domain-specific |
| 34 | **visible** | 99 | 34,181.26 | 7.150788 | 🟠 very high — domain-specific |
| 35 | **taste** | 77 | 34,158.21 | 9.18767 | 🟠 very high — domain-specific |
| 36 | **reacting** | 91 | 32,747.30 | 7.453069 | 🟠 very high — domain-specific |
| 37 | **arisen** | 82 | 32,492.92 | 8.206841 | 🟠 very high — domain-specific |
| 38 | **invisible** | 80 | 32,216.20 | 8.340372 | 🟠 very high — domain-specific |
| 39 | **sense** | 98 | 31,586.39 | 6.675364 | 🟠 very high — domain-specific |
| 40 | **whatever** | 91 | 31,232.14 | 7.108229 | 🟠 very high — domain-specific |
| 41 | **sensuous** | 67 | 31,023.61 | 9.59 | 🟠 very high — domain-specific |
| 42 | **abides** | 67 | 31,023.61 | 9.59 | 🟠 very high — domain-specific |
| 43 | **tangible** | 81 | 30,197.86 | 7.721333 | 🟠 very high — domain-specific |
| 44 | **associated** | 105 | 29,870.24 | 5.891833 | 🟠 very high — domain-specific |
| 45 | **synergies** | 69 | 29,650.87 | 8.899988 | 🟠 very high — domain-specific |
| 46 | **skandha** | 64 | 29,634.49 | 9.59 | 🟠 very high — domain-specific |
| 47 | **enters** | 67 | 28,791.42 | 8.899988 | 🟠 very high — domain-specific |
| 48 | **unincluded** | 62 | 28,708.42 | 9.59 | 🟠 very high — domain-specific |
| 49 | **answers** | 66 | 28,361.70 | 8.899988 | 🟠 very high — domain-specific |
| 50 | **concentration** | 69 | 28,300.04 | 8.494523 | 🟠 very high — domain-specific |
| 51 | **life** | 106 | 28,185.93 | 5.507159 | 🟠 very high — domain-specific |
| 52 | **insight** | 59 | 27,319.30 | 9.59 | 🟠 very high — domain-specific |
| 53 | **dullness** | 59 | 27,319.30 | 9.59 | 🟠 very high — domain-specific |
| 54 | **absence** | 79 | 27,113.62 | 7.108229 | 🟠 very high — domain-specific |
| 55 | **vision** | 69 | 26,949.21 | 8.089058 | 🟠 very high — domain-specific |
| 56 | **grasped** | 58 | 26,856.26 | 9.59 | 🟠 very high — domain-specific |
| 57 | **unconditioned** | 58 | 26,856.26 | 9.59 | 🟠 very high — domain-specific |
| 58 | **mindfulness** | 58 | 26,856.26 | 9.59 | 🟠 very high — domain-specific |
| 59 | **self-collectedness** | 57 | 26,393.22 | 9.59 | 🟠 very high — domain-specific |
| 60 | **knowledge** | 67 | 25,827.23 | 7.983697 | 🟠 very high — domain-specific |
| 61 | **views** | 80 | 25,784.81 | 6.675364 | 🟠 very high — domain-specific |
| 62 | **universe** | 55 | 25,475.47 | 9.593135 | 🟠 very high — domain-specific |
| 63 | **evil** | 55 | 25,475.47 | 9.593135 | 🟠 very high — domain-specific |
| 64 | **causally** | 55 | 25,467.14 | 9.59 | 🟠 very high — domain-specific |
| 65 | **cultivates** | 54 | 25,004.10 | 9.59 | 🟠 very high — domain-specific |
| 66 | **visual** | 56 | 24,842.33 | 9.18767 | 🟠 very high — domain-specific |
| 67 | **grasping** | 53 | 24,541.07 | 9.59 | 🟠 very high — domain-specific |
| 68 | **phenomena** | 52 | 24,085.90 | 9.593135 | 🟠 very high — domain-specific |
| 69 | **zest** | 52 | 24,078.03 | 9.59 | 🟠 very high — domain-specific |
| 70 | **intuition** | 52 | 24,078.03 | 9.59 | 🟠 very high — domain-specific |
| 71 | **senses** | 52 | 24,078.03 | 9.59 | 🟠 very high — domain-specific |
| 72 | **worlds** | 54 | 23,955.10 | 9.18767 | 🟠 very high — domain-specific |
| 73 | **disconnected** | 51 | 23,614.99 | 9.59 | 🟠 very high — domain-specific |
| 74 | **arises** | 54 | 23,205.03 | 8.899988 | 🟠 very high — domain-specific |
| 75 | **āsavas** | 50 | 23,151.95 | 9.59 | 🟠 very high — domain-specific |
| 76 | **sound** | 68 | 23,075.50 | 7.028186 | 🟠 very high — domain-specific |
| 77 | **hate** | 49 | 22,696.33 | 9.593135 | 🟠 very high — domain-specific |
| 78 | **derived** | 56 | 22,551.34 | 8.340372 | 🟠 very high — domain-specific |
| 79 | **ideal** | 60 | 22,368.79 | 7.721333 | 🟠 very high — domain-specific |
| 80 | **faculties** | 48 | 22,225.87 | 9.59 | 🟠 very high — domain-specific |
| 81 | **sustained** | 65 | 21,939.02 | 6.990446 | 🟠 very high — domain-specific |
| 82 | **external** | 77 | 21,814.16 | 5.867442 | 🟠 very high — domain-specific |
| 83 | **wrong** | 59 | 21,588.32 | 7.578232 | 🟠 very high — domain-specific |
| 84 | **attain** | 56 | 21,586.94 | 7.983697 | 🟠 very high — domain-specific |
| 85 | **smell** | 46 | 21,299.79 | 9.59 | 🟠 very high — domain-specific |
| 86 | **incorporeal** | 45 | 20,836.75 | 9.59 | 🟠 very high — domain-specific |
| 87 | **opinion** | 67 | 20,686.06 | 6.394462 | 🟠 very high — domain-specific |
| 88 | **shape** | 53 | 20,430.49 | 7.983697 | 🟠 very high — domain-specific |
| 89 | **intimation** | 44 | 20,373.71 | 9.59 | 🟠 very high — domain-specific |
| 90 | **away** | 72 | 20,194.30 | 5.808946 | 🟠 very high — domain-specific |
| 91 | **wrought** | 48 | 20,109.53 | 8.676844 | 🟠 very high — domain-specific |
| 92 | **induced** | 43 | 19,917.18 | 9.593135 | 🟠 very high — domain-specific |
| 93 | **connexion** | 43 | 19,910.68 | 9.59 | 🟠 very high — domain-specific |
| 94 | **desires** | 46 | 19,767.25 | 8.899988 | 🟠 very high — domain-specific |
| 95 | **applied** | 63 | 19,212.37 | 6.31599 | 🟠 very high — domain-specific |
| 96 | **progress** | 69 | 19,204.77 | 5.764494 | 🟠 very high — domain-specific |
| 97 | **paths** | 43 | 19,075.36 | 9.18767 | 🟠 very high — domain-specific |
| 98 | **odour** | 41 | 18,990.80 | 9.593135 | 🟠 very high — domain-specific |
| 99 | **body-sensibility** | 41 | 18,984.60 | 9.59 | 🟠 very high — domain-specific |
| 100 | **self** | 44 | 18,907.80 | 8.899988 | 🟠 very high — domain-specific |
| 101 | **fetters** | 40 | 18,521.56 | 9.59 | 🟠 very high — domain-specific |
| 102 | **rebirth** | 40 | 18,521.56 | 9.59 | 🟠 very high — domain-specific |
| 103 | **ease** | 64 | 18,168.70 | 5.879563 | 🟠 very high — domain-specific |
| 104 | **sight** | 51 | 18,078.99 | 7.341843 | 🟠 very high — domain-specific |
| 105 | **rapt** | 39 | 18,058.52 | 9.59 | 🟠 very high — domain-specific |
| 106 | **meditation** | 39 | 18,058.52 | 9.59 | 🟠 very high — domain-specific |
| 107 | **arise** | 42 | 18,048.36 | 8.899988 | 🟠 very high — domain-specific |
| 108 | **words** | 48 | 17,723.28 | 7.647225 | 🟠 very high — domain-specific |
| 109 | **roots** | 38 | 17,601.23 | 9.593135 | 🟠 very high — domain-specific |
| 110 | **gladness** | 38 | 17,595.48 | 9.59 | 🟠 very high — domain-specific |
| 111 | **blame** | 47 | 17,354.04 | 7.647225 | 🟠 very high — domain-specific |
| 112 | **balance** | 77 | 17,346.96 | 4.665882 | 🟠 very high — domain-specific |
| 113 | **jhānas** | 37 | 17,132.44 | 9.59 | 🟠 very high — domain-specific |
| 114 | **ignorance** | 36 | 16,669.40 | 9.59 | 🟠 very high — domain-specific |
| 115 | **grasp** | 36 | 16,669.40 | 9.59 | 🟠 very high — domain-specific |
| 116 | **sensual** | 36 | 16,669.40 | 9.59 | 🟠 very high — domain-specific |
| 117 | **emptiness** | 35 | 16,206.36 | 9.59 | 🟠 very high — domain-specific |
| 118 | **thereto** | 35 | 16,206.36 | 9.59 | 🟠 very high — domain-specific |
| 119 | **sense-objects** | 35 | 16,206.36 | 9.59 | 🟠 very high — domain-specific |
| 120 | **path** | 43 | 16,197.15 | 7.801376 | 🟠 very high — domain-specific |
| 121 | **body** | 51 | 15,599.78 | 6.335039 | 🟠 very high — domain-specific |
| 122 | **energy** | 71 | 15,531.28 | 4.53054 | 🟠 very high — domain-specific |
| 123 | **favourable** | 48 | 15,017.23 | 6.47962 | 🟠 very high — domain-specific |
| 124 | **personal** | 51 | 14,975.67 | 6.08159 | 🟠 very high — domain-specific |
| 125 | **right** | 60 | 14,904.02 | 5.144619 | 🟠 very high — domain-specific |
| 126 | **repeat** | 38 | 14,841.59 | 8.089058 | 🟠 very high — domain-specific |
| 127 | **vices** | 32 | 14,817.25 | 9.59 | 🟠 very high — domain-specific |
| 128 | **put** | 64 | 14,362.77 | 4.647928 | 🟠 very high — domain-specific |
| 129 | **cognizable** | 31 | 14,354.21 | 9.59 | 🟠 very high — domain-specific |
| 130 | **ideas** | 41 | 14,335.96 | 7.24176 | 🟠 very high — domain-specific |
| 131 | **modes** | 30 | 13,895.71 | 9.593135 | 🟠 very high — domain-specific |
| 132 | **wit** | 30 | 13,895.71 | 9.593135 | 🟠 very high — domain-specific |
| 133 | **continue** | 68 | 13,592.62 | 4.139953 | 🟠 very high — domain-specific |
| 134 | **unconscientiousness** | 29 | 13,428.13 | 9.59 | 🟠 very high — domain-specific |
| 135 | **whereto** | 29 | 13,428.13 | 9.59 | 🟠 very high — domain-specific |
| 136 | **fetter** | 29 | 13,428.13 | 9.59 | 🟠 very high — domain-specific |
| 137 | **whether** | 58 | 13,006.31 | 4.644375 | 🟠 very high — domain-specific |
| 138 | **power** | 51 | 12,991.07 | 5.275647 | 🟠 very high — domain-specific |
| 139 | **vocal** | 28 | 12,969.33 | 9.593135 | 🟠 very high — domain-specific |
| 140 | **davids** | 28 | 12,965.09 | 9.59 | 🟠 very high — domain-specific |
| 141 | **pali** | 28 | 12,965.09 | 9.59 | 🟠 very high — domain-specific |
| 142 | **heavens** | 28 | 12,965.09 | 9.59 | 🟠 very high — domain-specific |
| 143 | **kinds** | 34 | 12,675.65 | 7.721333 | 🟠 very high — domain-specific |
| 144 | **greed** | 27 | 12,506.14 | 9.593135 | 🟠 very high — domain-specific |
| 145 | **fivefold** | 27 | 12,506.14 | 9.593135 | 🟠 very high — domain-specific |
| 146 | **hindrances** | 27 | 12,502.05 | 9.59 | 🟠 very high — domain-specific |
| 147 | **painful** | 29 | 12,461.96 | 8.899988 | 🟠 very high — domain-specific |
| 148 | **moral** | 28 | 12,421.17 | 9.18767 | 🟠 very high — domain-specific |
| 149 | **disregard** | 28 | 12,421.17 | 9.18767 | 🟠 very high — domain-specific |
| 150 | **summary** | 33 | 12,074.82 | 7.578232 | 🟠 very high — domain-specific |
| 151 | **perversion** | 26 | 12,039.01 | 9.59 | 🟠 very high — domain-specific |
| 152 | **infinite** | 27 | 11,977.55 | 9.18767 | 🟠 very high — domain-specific |
| 153 | **endeavour** | 29 | 11,894.22 | 8.494523 | 🟠 very high — domain-specific |
| 154 | **thinking** | 32 | 11,609.20 | 7.513694 | 🟠 very high — domain-specific |
| 155 | **plasticity** | 25 | 11,575.97 | 9.59 | 🟠 very high — domain-specific |
| 156 | **distraction** | 25 | 11,575.97 | 9.59 | 🟠 very high — domain-specific |
| 157 | **wieldiness** | 25 | 11,575.97 | 9.59 | 🟠 very high — domain-specific |
| 158 | **unaimed-at** | 25 | 11,575.97 | 9.59 | 🟠 very high — domain-specific |
| 159 | **higher** | 61 | 11,435.72 | 3.882708 | 🟠 very high — domain-specific |
| 160 | **sluggish** | 35 | 11,374.76 | 6.730934 | 🟠 very high — domain-specific |
| 161 | **text** | 28 | 11,275.67 | 8.340372 | 🟠 very high — domain-specific |
| 162 | **space** | 32 | 10,919.66 | 7.067407 | 🟠 very high — domain-specific |
| 163 | **theory** | 26 | 10,892.66 | 8.676844 | 🟠 very high — domain-specific |
| 164 | **identical** | 27 | 10,698.89 | 8.206841 | 🟠 very high — domain-specific |
| 165 | **under** | 66 | 10,675.30 | 3.34994 | 🟠 very high — domain-specific |
| 166 | **fluid** | 26 | 10,663.78 | 8.494523 | 🟠 very high — domain-specific |
| 167 | **foregoing** | 23 | 10,649.90 | 9.59 | 🟠 very high — domain-specific |
| 168 | **perplexity** | 23 | 10,649.90 | 9.59 | 🟠 very high — domain-specific |
| 169 | **onward** | 24 | 10,646.71 | 9.18767 | 🟠 very high — domain-specific |
| 170 | **subsistence** | 24 | 10,646.71 | 9.18767 | 🟠 very high — domain-specific |
| 171 | **faith** | 27 | 10,407.99 | 7.983697 | 🟠 very high — domain-specific |
| 172 | **instigated** | 22 | 10,186.86 | 9.59 | 🟠 very high — domain-specific |
| 173 | **undoing** | 22 | 10,186.86 | 9.59 | 🟠 very high — domain-specific |
| 174 | **root-conditions** | 22 | 10,186.86 | 9.59 | 🟠 very high — domain-specific |
| 175 | **desire** | 31 | 10,162.86 | 6.789775 | 🟠 very high — domain-specific |
| 176 | **relate** | 26 | 10,154.77 | 8.089058 | 🟠 very high — domain-specific |
| 177 | **remaining** | 41 | 10,104.99 | 5.104499 | 🟠 very high — domain-specific |
| 178 | **ties** | 29 | 10,012.69 | 7.150788 | 🟠 very high — domain-specific |
| 179 | **society** | 28 | 9,998.82 | 7.395911 | 🟡 high — specialist register |
| 180 | **depending** | 32 | 9,848.69 | 6.374259 | 🟡 high — specialist register |
| 181 | **forth** | 22 | 9,759.49 | 9.18767 | 🟡 high — specialist register |
| 182 | **lightness** | 21 | 9,723.82 | 9.59 | 🟡 high — specialist register |
| 183 | **fourfold** | 21 | 9,723.82 | 9.59 | 🟡 high — specialist register |
| 184 | **conversely** | 21 | 9,723.82 | 9.59 | 🟡 high — specialist register |
| 185 | **impinge** | 21 | 9,723.82 | 9.59 | 🟡 high — specialist register |
| 186 | **dominant** | 27 | 9,571.23 | 7.341843 | 🟡 high — specialist register |
| 187 | **eye** | 25 | 9,521.98 | 7.888387 | 🟡 high — specialist register |
| 188 | **exists** | 26 | 9,513.50 | 7.578232 | 🟡 high — specialist register |
| 189 | **case** | 36 | 9,418.90 | 5.418748 | 🟡 high — specialist register |
| 190 | **phenomenon** | 24 | 9,373.64 | 8.089058 | 🟡 high — specialist register |
| 191 | **opinions** | 23 | 9,262.16 | 8.340372 | 🟡 high — specialist register |
| 192 | **sprung** | 20 | 9,260.78 | 9.59 | 🟡 high — specialist register |
| 193 | **conscientiousness** | 20 | 9,260.78 | 9.59 | 🟡 high — specialist register |
| 194 | **intellection** | 20 | 9,260.78 | 9.59 | 🟡 high — specialist register |
| 195 | **impinged** | 20 | 9,260.78 | 9.59 | 🟡 high — specialist register |
| 196 | **themselves** | 29 | 9,169.51 | 6.548613 | 🟡 high — specialist register |
| 197 | **integration** | 25 | 8,996.51 | 7.453069 | 🟡 high — specialist register |
| 198 | **best** | 34 | 8,960.02 | 5.457969 | 🟡 high — specialist register |
| 199 | **substituting** | 21 | 8,797.92 | 8.676844 | 🟡 high — specialist register |
| 200 | **covetousness** | 19 | 8,797.74 | 9.59 | 🟡 high — specialist register |
| 201 | **serenity** | 19 | 8,797.74 | 9.59 | 🟡 high — specialist register |
| 202 | **lust** | 19 | 8,797.74 | 9.59 | 🟡 high — specialist register |
| 203 | **auditory** | 19 | 8,797.74 | 9.59 | 🟡 high — specialist register |
| 204 | **impinges** | 19 | 8,797.74 | 9.59 | 🟡 high — specialist register |
| 205 | **whereby** | 20 | 8,594.46 | 8.899988 | 🟡 high — specialist register |
| 206 | **way** | 37 | 8,512.31 | 4.764821 | 🟡 high — specialist register |
| 207 | **result** | 41 | 8,467.78 | 4.277469 | 🟡 high — specialist register |
| 208 | **hearing** | 28 | 8,464.39 | 6.260931 | 🟡 high — specialist register |
| 209 | **phrase** | 19 | 8,428.65 | 9.18767 | 🟡 high — specialist register |
| 210 | **factors** | 33 | 8,405.98 | 5.275647 | 🟡 high — specialist register |
| 211 | **relating** | 24 | 8,337.88 | 7.19524 | 🟡 high — specialist register |
| 212 | **easeful** | 18 | 8,334.70 | 9.59 | 🟡 high — specialist register |
| 213 | **belong** | 19 | 8,164.73 | 8.899988 | 🟡 high — specialist register |
| 214 | **state** | 39 | 8,054.72 | 4.277469 | 🟡 high — specialist register |
| 215 | **preceding** | 21 | 7,998.46 | 7.888387 | 🟡 high — specialist register |
| 216 | **shapes** | 18 | 7,985.03 | 9.18767 | 🟡 high — specialist register |
| 217 | **tastes** | 19 | 7,960.02 | 8.676844 | 🟡 high — specialist register |
| 218 | **influence** | 25 | 7,904.75 | 6.548613 | 🟡 high — specialist register |
| 219 | **ear** | 17 | 7,874.24 | 9.593135 | 🟡 high — specialist register |
| 220 | **malice** | 17 | 7,871.66 | 9.59 | 🟡 high — specialist register |
| 221 | **disinterestedness** | 17 | 7,871.66 | 9.59 | 🟡 high — specialist register |
| 222 | **passion** | 17 | 7,871.66 | 9.59 | 🟡 high — specialist register |
| 223 | **ritual** | 17 | 7,871.66 | 9.59 | 🟡 high — specialist register |
| 224 | **going** | 31 | 7,735.84 | 5.168289 | 🟡 high — specialist register |
| 225 | **type** | 23 | 7,683.68 | 6.918987 | 🟡 high — specialist register |
| 226 | **stage** | 26 | 7,579.67 | 6.037787 | 🟡 high — specialist register |
| 227 | **sex** | 17 | 7,541.42 | 9.18767 | 🟡 high — specialist register |
| 228 | **called** | 33 | 7,535.70 | 4.729454 | 🟡 high — specialist register |
| 229 | **touch** | 20 | 7,533.56 | 7.801376 | 🟡 high — specialist register |
| 230 | **fruits** | 19 | 7,528.85 | 8.206841 | 🟡 high — specialist register |
| 231 | **olfactory** | 16 | 7,408.62 | 9.59 | 🟡 high — specialist register |
| 232 | **gustatory** | 16 | 7,408.62 | 9.59 | 🟡 high — specialist register |
| 233 | **nose** | 16 | 7,408.62 | 9.59 | 🟡 high — specialist register |
| 234 | **ill** | 22 | 7,386.88 | 6.954078 | 🟡 high — specialist register |
| 235 | **wisdom** | 18 | 7,382.62 | 8.494523 | 🟡 high — specialist register |
| 236 | **aspect** | 17 | 7,305.29 | 8.899988 | 🟡 high — specialist register |
| 237 | **root** | 19 | 7,236.70 | 7.888387 | 🟡 high — specialist register |
| 238 | **latter** | 20 | 7,197.21 | 7.453069 | 🟡 high — specialist register |
| 239 | **tongue** | 16 | 7,097.81 | 9.18767 | 🟡 high — specialist register |
| 240 | **basis** | 32 | 7,080.30 | 4.5825 | 🟡 high — specialist register |
| 241 | **limited** | 28 | 6,963.14 | 5.150484 | 🟡 high — specialist register |
| 242 | **buddhist** | 15 | 6,947.85 | 9.593135 | 🟡 high — specialist register |
| 243 | **ideation** | 15 | 6,945.58 | 9.59 | 🟡 high — specialist register |
| 244 | **guilt** | 15 | 6,945.58 | 9.59 | 🟡 high — specialist register |
| 245 | **manual** | 15 | 6,945.58 | 9.59 | 🟡 high — specialist register |
| 246 | **impermanence** | 15 | 6,945.58 | 9.59 | 🟡 high — specialist register |
| 247 | **sentient** | 15 | 6,945.58 | 9.59 | 🟡 high — specialist register |
| 248 | **āsava** | 15 | 6,945.58 | 9.59 | 🟡 high — specialist register |
| 249 | **causes** | 18 | 6,855.82 | 7.888387 | 🟡 high — specialist register |
| 250 | **something** | 22 | 6,792.44 | 6.394462 | 🟡 high — specialist register |
| 251 | **quiet** | 19 | 6,688.26 | 7.29055 | 🟡 high — specialist register |
| 252 | **decay** | 15 | 6,654.20 | 9.18767 | 🟡 high — specialist register |
| 253 | **moreover** | 18 | 6,646.23 | 7.647225 | 🟡 high — specialist register |
| 254 | **forms** | 19 | 6,600.82 | 7.19524 | 🟡 high — specialist register |
| 255 | **speculative** | 21 | 6,570.04 | 6.47962 | 🟡 high — specialist register |
| 256 | **vicious** | 16 | 6,562.33 | 8.494523 | 🟡 high — specialist register |
| 257 | **tie** | 17 | 6,553.18 | 7.983697 | 🟡 high — specialist register |
| 258 | **dissociated** | 14 | 6,484.66 | 9.593135 | 🟡 high — specialist register |
| 259 | **rhys** | 14 | 6,484.66 | 9.593135 | 🟡 high — specialist register |
| 260 | **organ** | 14 | 6,484.66 | 9.593135 | 🟡 high — specialist register |
| 261 | **hindrance** | 14 | 6,484.66 | 9.593135 | 🟡 high — specialist register |
| 262 | **graspings** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 263 | **constituent** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 264 | **ethics** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 265 | **rys** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 266 | **dhammasaṅgaṇī** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 267 | **compendium** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 268 | **litt** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 269 | **reprinted** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 270 | **attribution-noncommercial** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 271 | **by-nc** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 272 | **http** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 273 | **earth-gazing** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 274 | **non-reacting** | 14 | 6,482.55 | 9.59 | 🟡 high — specialist register |
| 275 | **described** | 22 | 6,444.36 | 6.066775 | 🟡 high — specialist register |
| 276 | **consequence** | 16 | 6,443.24 | 8.340372 | 🟡 high — specialist register |
| 277 | **ends** | 24 | 6,411.31 | 5.532692 | 🟡 high — specialist register |
| 278 | **representative** | 23 | 6,233.86 | 5.613454 | 🟡 high — specialist register |
| 279 | **intention** | 21 | 6,228.87 | 6.143148 | 🟡 high — specialist register |
| 280 | **caroline** | 14 | 6,210.58 | 9.18767 | 🟡 high — specialist register |
| 281 | **included** | 26 | 6,165.13 | 4.911004 | 🟡 high — specialist register |
| 282 | **system** | 30 | 6,092.92 | 4.206349 | 🟡 high — specialist register |
| 283 | **elements** | 17 | 6,026.33 | 7.341843 | 🟡 high — specialist register |
| 284 | **distress** | 13 | 6,021.47 | 9.593135 | 🟡 high — specialist register |
| 285 | **superlative** | 13 | 6,019.51 | 9.59 | 🟡 high — specialist register |
| 286 | **odours** | 13 | 6,019.51 | 9.59 | 🟡 high — specialist register |
| 287 | **woman-faculty** | 13 | 6,019.51 | 9.59 | 🟡 high — specialist register |
| 288 | **fluidity** | 13 | 6,019.51 | 9.59 | 🟡 high — specialist register |
| 289 | **excepted** | 13 | 6,019.51 | 9.59 | 🟡 high — specialist register |
| 290 | **stolidity** | 13 | 6,019.51 | 9.59 | 🟡 high — specialist register |
| 291 | **objects** | 14 | 6,016.12 | 8.899988 | 🟡 high — specialist register |
| 292 | **creative** | 14 | 6,016.12 | 8.899988 | 🟡 high — specialist register |
| 293 | **respectively** | 25 | 6,014.89 | 4.982977 | 🟡 high — specialist register |
| 294 | **together** | 22 | 6,013.66 | 5.66131 | 🟡 high — specialist register |
| 295 | **application** | 20 | 5,963.41 | 6.175409 | 🟡 high — specialist register |
| 296 | **fear** | 19 | 5,866.20 | 6.394462 | 🟡 high — specialist register |
| 297 | **cultivation** | 14 | 5,865.28 | 8.676844 | 🟡 high — specialist register |
| 298 | **appearance** | 14 | 5,865.28 | 8.676844 | 🟡 high — specialist register |
| 299 | **appropriate** | 20 | 5,803.31 | 6.009616 | 🟡 high — specialist register |
| 300 | **inferior** | 13 | 5,766.97 | 9.18767 | 🟡 high — specialist register |
| 301 | **efficacy** | 13 | 5,766.97 | 9.18767 | 🟡 high — specialist register |
| 302 | **making** | 26 | 5,715.63 | 4.552941 | 🟡 high — specialist register |
| 303 | **truth** | 12 | 5,558.28 | 9.593135 | 🟡 high — specialist register |
| 304 | **cultivated** | 12 | 5,558.28 | 9.593135 | 🟡 high — specialist register |
| 305 | **pleasant** | 12 | 5,556.47 | 9.59 | 🟡 high — specialist register |
| 306 | **concomitant** | 12 | 5,556.47 | 9.59 | 🟡 high — specialist register |
| 307 | **conjoined** | 12 | 5,556.47 | 9.59 | 🟡 high — specialist register |
| 308 | **wherein** | 12 | 5,556.47 | 9.59 | 🟡 high — specialist register |
| 309 | **enumerated** | 12 | 5,556.47 | 9.59 | 🟡 high — specialist register |
| 310 | **conceit** | 12 | 5,556.47 | 9.59 | 🟡 high — specialist register |
| 311 | **signless** | 12 | 5,556.47 | 9.59 | 🟡 high — specialist register |
| 312 | **belongs** | 14 | 5,547.57 | 8.206841 | 🟡 high — specialist register |
| 313 | **concerning** | 18 | 5,539.89 | 6.374259 | 🟡 high — specialist register |
| 314 | **fourth** | 24 | 5,530.80 | 4.772854 | 🟡 high — specialist register |
| 315 | **questions** | 17 | 5,479.27 | 6.675364 | 🟡 high — specialist register |
| 316 | **psychological** | 14 | 5,467.95 | 8.089058 | 🟡 high — specialist register |
| 317 | **come** | 23 | 5,443.54 | 4.901787 | 🟡 high — specialist register |
| 318 | **conjunction** | 15 | 5,441.81 | 7.513694 | 🟡 high — specialist register |
| 319 | **difficult** | 21 | 5,441.18 | 5.366301 | 🟡 high — specialist register |
| 320 | **see** | 24 | 5,419.51 | 4.676811 | 🟡 high — specialist register |
| 321 | **licence** | 14 | 5,332.31 | 7.888387 | 🟡 high — specialist register |
| 322 | **inoperative** | 12 | 5,323.36 | 9.18767 | 🟡 high — specialist register |
| 323 | **world** | 28 | 5,276.31 | 3.902776 | 🟡 high — specialist register |
| 324 | **above** | 24 | 5,246.35 | 4.527381 | 🟡 high — specialist register |
| 325 | **sounds** | 13 | 5,235.13 | 8.340372 | 🟡 high — specialist register |
| 326 | **powers** | 16 | 5,222.29 | 6.759922 | 🟡 high — specialist register |
| 327 | **pursuit** | 12 | 5,156.67 | 8.899988 | 🟡 high — specialist register |
| 328 | **rule** | 17 | 5,139.10 | 6.260931 | 🟡 high — specialist register |
| 329 | **omitting** | 11 | 5,095.09 | 9.593135 | 🟡 high — specialist register |
| 330 | **subtle** | 11 | 5,095.09 | 9.593135 | 🟡 high — specialist register |
| 331 | **craving** | 11 | 5,093.43 | 9.59 | 🟡 high — specialist register |
| 332 | **springing** | 11 | 5,093.43 | 9.59 | 🟡 high — specialist register |
| 333 | **afore-named** | 11 | 5,093.43 | 9.59 | 🟡 high — specialist register |
| 334 | **commons** | 14 | 5,038.05 | 7.453069 | 🟡 high — specialist register |
| 335 | **buoyancy** | 12 | 5,027.38 | 8.676844 | 🟡 high — specialist register |
| 336 | **skill** | 11 | 4,879.74 | 9.18767 | 🟡 high — specialist register |
| 337 | **perfect** | 11 | 4,879.74 | 9.18767 | 🟡 high — specialist register |
| 338 | **belonging** | 12 | 4,832.43 | 8.340372 | 🟡 high — specialist register |
| 339 | **fitness** | 12 | 4,832.43 | 8.340372 | 🟡 high — specialist register |
| 340 | **second** | 23 | 4,806.18 | 4.327858 | 🟡 high — specialist register |
| 341 | **heart** | 14 | 4,725.33 | 6.990446 | 🟡 high — specialist register |
| 342 | **soil** | 13 | 4,716.24 | 7.513694 | 🟡 high — specialist register |
| 343 | **remote** | 12 | 4,686.82 | 8.089058 | 🟡 high — specialist register |
| 344 | **taken** | 20 | 4,681.77 | 4.848203 | 🟡 high — specialist register |
| 345 | **say** | 22 | 4,642.06 | 4.37008 | 🟡 high — specialist register |
| 346 | **sensation** | 10 | 4,631.90 | 9.593135 | 🟡 high — specialist register |
| 347 | **vitiated** | 10 | 4,630.39 | 9.59 | 🟡 high — specialist register |
| 348 | **sorrow** | 10 | 4,630.39 | 9.59 | 🟡 high — specialist register |
| 349 | **mastery** | 10 | 4,630.39 | 9.59 | 🟡 high — specialist register |
| 350 | **triplet** | 10 | 4,630.39 | 9.59 | 🟡 high — specialist register |
| 351 | **underived** | 10 | 4,630.39 | 9.59 | 🟡 high — specialist register |
| 352 | **torpor** | 10 | 4,630.39 | 9.59 | 🟡 high — specialist register |
| 353 | **understanding** | 14 | 4,610.48 | 6.820546 | 🟡 high — specialist register |
| 354 | **medium** | 15 | 4,437.79 | 6.127399 | 🟡 high — specialist register |
| 355 | **intelligence** | 13 | 4,436.11 | 7.067407 | 🟡 high — specialist register |
| 356 | **combinations** | 11 | 4,429.73 | 8.340372 | 🟡 high — specialist register |
| 357 | **empty** | 11 | 4,429.73 | 8.340372 | 🟡 high — specialist register |
| 358 | **pass** | 13 | 4,411.49 | 7.028186 | 🟡 high — specialist register |
| 359 | **death** | 11 | 4,358.81 | 8.206841 | 🟡 high — specialist register |
| 360 | **end** | 24 | 4,273.41 | 3.687773 | 🟡 high — specialist register |
| 361 | **searching** | 11 | 4,189.67 | 7.888387 | 🟡 high — specialist register |
| 362 | **things** | 14 | 4,174.39 | 6.175409 | 🟡 high — specialist register |
| 363 | **joy** | 9 | 4,168.71 | 9.593135 | 🟡 high — specialist register |
| 364 | **corpse** | 9 | 4,167.35 | 9.59 | 🟡 high — specialist register |
| 365 | **enlightenment** | 9 | 4,167.35 | 9.59 | 🟡 high — specialist register |
| 366 | **pairs** | 9 | 4,167.35 | 9.59 | 🟡 high — specialist register |
| 367 | **co-intoxicant** | 9 | 4,167.35 | 9.59 | 🟡 high — specialist register |
| 368 | **man-faculty** | 9 | 4,167.35 | 9.59 | 🟡 high — specialist register |
| 369 | **smells** | 9 | 4,167.35 | 9.59 | 🟡 high — specialist register |
| 370 | **concomitants** | 9 | 4,167.35 | 9.59 | 🟡 high — specialist register |
| 371 | **soul** | 9 | 4,167.35 | 9.59 | 🟡 high — specialist register |
| 372 | **regards** | 11 | 4,143.46 | 7.801376 | 🟡 high — specialist register |
| 373 | **published** | 14 | 4,081.36 | 6.037787 | 🟡 high — specialist register |
| 374 | **corresponding** | 12 | 4,029.21 | 6.954078 | 🟡 high — specialist register |
| 375 | **sort** | 12 | 4,029.21 | 6.954078 | 🟡 high — specialist register |
| 376 | **beyond** | 13 | 4,026.66 | 6.415081 | 🟡 high — specialist register |
| 377 | **stored** | 11 | 4,024.94 | 7.578232 | 🟡 high — specialist register |
| 378 | **group** | 26 | 4,014.52 | 3.197874 | 🟡 high — specialist register |
| 379 | **infected** | 9 | 3,992.52 | 9.18767 | 🟡 high — specialist register |
| 380 | **easy** | 11 | 3,990.66 | 7.513694 | 🟡 high — specialist register |
| 381 | **former** | 15 | 3,924.54 | 5.418748 | 🟡 high — specialist register |
| 382 | **third** | 18 | 3,921.16 | 4.511731 | 🟡 high — specialist register |
| 383 | **culture** | 9 | 3,867.50 | 8.899988 | 🟡 high — specialist register |
| 384 | **village** | 9 | 3,867.50 | 8.899988 | 🟡 high — specialist register |
| 385 | **operative** | 9 | 3,770.54 | 8.676844 | 🟡 high — specialist register |
| 386 | **question** | 14 | 3,722.67 | 5.507159 | 🟡 high — specialist register |
| 387 | **doctrine** | 8 | 3,705.52 | 9.593135 | 🟡 high — specialist register |
| 388 | **attaining** | 8 | 3,705.52 | 9.593135 | 🟡 high — specialist register |
| 389 | **inclination** | 8 | 3,705.52 | 9.593135 | 🟡 high — specialist register |
| 390 | **offences** | 8 | 3,704.31 | 9.59 | 🟡 high — specialist register |
| 391 | **conscientious** | 8 | 3,704.31 | 9.59 | 🟡 high — specialist register |
| 392 | **scruple** | 8 | 3,704.31 | 9.59 | 🟡 high — specialist register |
| 393 | **rectitude** | 8 | 3,704.31 | 9.59 | 🟡 high — specialist register |
| 394 | **path-component** | 8 | 3,704.31 | 9.59 | 🟡 high — specialist register |
| 395 | **disorder** | 8 | 3,704.31 | 9.59 | 🟡 high — specialist register |
| 396 | **distressful** | 8 | 3,704.31 | 9.59 | 🟡 high — specialist register |
| 397 | **sapid** | 8 | 3,704.31 | 9.59 | 🟡 high — specialist register |
| 398 | **individuality** | 8 | 3,704.31 | 9.59 | 🟡 high — specialist register |
| 399 | **sensuality** | 8 | 3,704.31 | 9.59 | 🟡 high — specialist register |
| 400 | **released** | 14 | 3,694.85 | 5.466001 | 🟡 high — specialist register |
| 401 | **consecutive** | 11 | 3,693.44 | 6.954078 | 🟡 high — specialist register |
| 402 | **felt** | 12 | 3,670.54 | 6.335039 | 🟡 high — specialist register |
| 403 | **comes** | 12 | 3,648.67 | 6.297298 | 🟡 high — specialist register |
| 404 | **quick** | 11 | 3,639.38 | 6.852295 | 🟡 high — specialist register |
| 405 | **worry** | 10 | 3,627.88 | 7.513694 | 🟡 high — specialist register |
| 406 | **purity** | 9 | 3,624.32 | 8.340372 | 🟡 high — specialist register |
| 407 | **lack** | 12 | 3,587.62 | 6.191938 | 🟡 high — specialist register |
| 408 | **arising** | 10 | 3,571.01 | 7.395911 | 🟡 high — specialist register |
| 409 | **due** | 20 | 3,570.43 | 3.697356 | 🟡 high — specialist register |
| 410 | **ten** | 12 | 3,568.62 | 6.159148 | 🟡 high — specialist register |
| 411 | **grip** | 9 | 3,566.30 | 8.206841 | 🟡 high — specialist register |
| 412 | **capable** | 10 | 3,544.90 | 7.341843 | 🟡 high — specialist register |
| 413 | **itself** | 13 | 3,541.33 | 5.641891 | 🟡 high — specialist register |
| 414 | **combination** | 12 | 3,473.99 | 5.995823 | 🟡 high — specialist register |
| 415 | **speech** | 12 | 3,466.11 | 5.982217 | 🟡 high — specialist register |
| 416 | **springs** | 8 | 3,351.59 | 8.676844 | 🟡 high — specialist register |
| 417 | **word** | 9 | 3,323.11 | 7.647225 | 🟡 high — specialist register |
| 418 | **fixed** | 13 | 3,311.45 | 5.275647 | 🟡 high — specialist register |
| 419 | **formula** | 10 | 3,293.20 | 6.820546 | 🟡 high — specialist register |
| 420 | **thoughts** | 7 | 3,242.33 | 9.593135 | 🟡 high — specialist register |
| 421 | **walking** | 7 | 3,242.33 | 9.593135 | 🟡 high — specialist register |
| 422 | **constitutes** | 7 | 3,242.33 | 9.593135 | 🟡 high — specialist register |
| 423 | **happiness** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 424 | **perverted** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 425 | **agitation** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 426 | **pleasurable** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 427 | **proficiency** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 428 | **sixteenfold** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 429 | **corporeal** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 430 | **indigo** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 431 | **nineteen** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 432 | **scuffling** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 433 | **tenacity** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 434 | **by-path** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 435 | **wrongness** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 436 | **passim** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 437 | **eternal** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 438 | **birth** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 439 | **deed** | 7 | 3,241.27 | 9.59 | 🟡 high — specialist register |
| 440 | **section** | 10 | 3,236.33 | 6.702763 | 🟡 high — specialist register |
| 441 | **colour** | 8 | 3,221.62 | 8.340372 | 🟡 high — specialist register |
| 442 | **gross** | 13 | 3,193.53 | 5.087785 | 🟡 high — specialist register |
| 443 | **without** | 14 | 3,191.77 | 4.721762 | 🟡 high — specialist register |
| 444 | **fruit** | 9 | 3,190.41 | 7.341843 | 🟡 high — specialist register |
| 445 | **investigation** | 10 | 3,173.54 | 6.57271 | 🟡 high — specialist register |
| 446 | **condition** | 11 | 3,163.10 | 5.955549 | 🟡 high — specialist register |
| 447 | **exclusive** | 9 | 3,146.92 | 7.24176 | 🟡 high — specialist register |
| 448 | **properties** | 12 | 3,130.79 | 5.40348 | 🟡 high — specialist register |
| 449 | **known** | 11 | 3,109.95 | 5.855466 | 🟡 high — specialist register |
| 450 | **consequences** | 9 | 3,107.39 | 7.150788 | 🟡 high — specialist register |
| 451 | **noble** | 7 | 3,105.29 | 9.18767 | 🟡 high — specialist register |
| 452 | **attained** | 7 | 3,105.29 | 9.18767 | 🟡 high — specialist register |
| 453 | **factor** | 11 | 3,091.31 | 5.820374 | 🟡 high — specialist register |
| 454 | **related** | 12 | 3,060.60 | 5.282336 | 🟡 high — specialist register |
| 455 | **diet** | 7 | 3,008.06 | 8.899988 | 🟡 high — specialist register |
| 456 | **love** | 7 | 3,008.06 | 8.899988 | 🟡 high — specialist register |
| 457 | **wilderness** | 7 | 3,008.06 | 8.899988 | 🟡 high — specialist register |
| 458 | **action** | 14 | 2,993.43 | 4.428349 | 🟢 medium — moderately distinctive |
| 459 | **results** | 15 | 2,990.66 | 4.129303 | 🟢 medium — moderately distinctive |
| 460 | **concept** | 8 | 2,953.88 | 7.647225 | 🟢 medium — moderately distinctive |
| 461 | **conscious** | 7 | 2,932.64 | 8.676844 | 🟢 medium — moderately distinctive |
| 462 | **thing** | 9 | 2,924.94 | 6.730934 | 🟢 medium — moderately distinctive |
| 463 | **ought** | 8 | 2,902.30 | 7.513694 | 🟢 medium — moderately distinctive |
| 464 | **living** | 9 | 2,877.91 | 6.622721 | 🟢 medium — moderately distinctive |
| 465 | **near** | 12 | 2,867.31 | 4.948744 | 🟢 medium — moderately distinctive |
| 466 | **given** | 13 | 2,833.90 | 4.514841 | 🟢 medium — moderately distinctive |
| 467 | **solid** | 8 | 2,816.11 | 7.29055 | 🟢 medium — moderately distinctive |
| 468 | **extension** | 9 | 2,796.83 | 6.436135 | 🟢 medium — moderately distinctive |
| 469 | **contained** | 9 | 2,796.83 | 6.436135 | 🟢 medium — moderately distinctive |
| 470 | **made** | 16 | 2,781.46 | 3.600421 | 🟢 medium — moderately distinctive |
| 471 | **exception** | 8 | 2,779.29 | 7.19524 | 🟢 medium — moderately distinctive |
| 472 | **category** | 8 | 2,779.29 | 7.19524 | 🟢 medium — moderately distinctive |
| 473 | **pleasure** | 6 | 2,779.14 | 9.593135 | 🟢 medium — moderately distinctive |
| 474 | **discrimination** | 6 | 2,779.14 | 9.593135 | 🟢 medium — moderately distinctive |
| 475 | **succession** | 6 | 2,779.14 | 9.593135 | 🟢 medium — moderately distinctive |
| 476 | **unaccompanied** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 477 | **remorse** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 478 | **pliancy** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 479 | **solitude** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 480 | **rūpāni** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 481 | **eightfold** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 482 | **dying** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 483 | **livelihood** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 484 | **sectarianism** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 485 | **self-state** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 486 | **beings** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 487 | **apprehended** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 488 | **wicked** | 6 | 2,778.23 | 9.59 | 🟢 medium — moderately distinctive |
| 489 | **struggle** | 7 | 2,773.79 | 8.206841 | 🟢 medium — moderately distinctive |
| 490 | **kind** | 9 | 2,752.90 | 6.335039 | 🟢 medium — moderately distinctive |
| 491 | **substituted** | 6 | 2,661.68 | 9.18767 | 🟢 medium — moderately distinctive |
| 492 | **become** | 11 | 2,651.86 | 4.992978 | 🟢 medium — moderately distinctive |
| 493 | **statement** | 14 | 2,648.51 | 3.918095 | 🟢 medium — moderately distinctive |
| 494 | **purely** | 7 | 2,636.75 | 7.801376 | 🟢 medium — moderately distinctive |
| 495 | **passing** | 7 | 2,636.75 | 7.801376 | 🟢 medium — moderately distinctive |
| 496 | **follow** | 9 | 2,629.98 | 6.052176 | 🟢 medium — moderately distinctive |
| 497 | **height** | 6 | 2,578.34 | 8.899988 | 🟢 medium — moderately distinctive |
| 498 | **tend** | 7 | 2,561.33 | 7.578232 | 🟢 medium — moderately distinctive |
| 499 | **besides** | 7 | 2,539.51 | 7.513694 | 🟢 medium — moderately distinctive |
| 500 | **jungle** | 7 | 2,481.43 | 7.341843 | 🟢 medium — moderately distinctive |
| 501 | **order** | 10 | 2,464.63 | 5.104499 | 🟢 medium — moderately distinctive |
| 502 | **road** | 7 | 2,464.09 | 7.29055 | 🟢 medium — moderately distinctive |
| 503 | **attention** | 8 | 2,454.52 | 6.354457 | 🟢 medium — moderately distinctive |
| 504 | **past** | 11 | 2,453.69 | 4.619856 | 🟢 medium — moderately distinctive |
| 505 | **tied** | 7 | 2,447.60 | 7.24176 | 🟢 medium — moderately distinctive |
| 506 | **except** | 8 | 2,432.45 | 6.297298 | 🟢 medium — moderately distinctive |
| 507 | **achievement** | 6 | 2,416.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 508 | **wholly** | 8 | 2,326.73 | 6.023602 | 🟢 medium — moderately distinctive |
| 509 | **resultant** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 510 | **sublime** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 511 | **perversions** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 512 | **conduce** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 513 | **attainments** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 514 | **theoretic** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 515 | **persistence** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 516 | **hatred** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 517 | **composure** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 518 | **viz** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 519 | **cattāri** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 520 | **unconscious** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 521 | **aṭṭhakkhattukaṃ** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 522 | **successively** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 523 | **sensory** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 524 | **manifold** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 525 | **unbounded** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 526 | **repugnance** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 527 | **life-faculty** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 528 | **feminine** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 529 | **masculine** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 530 | **viscid** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 531 | **triplets** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 532 | **analogous** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 533 | **derivation** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 534 | **classed** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 535 | **delight** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 536 | **intoxicant** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 537 | **dogmatize** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 538 | **therein** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 539 | **unrestrained** | 5 | 2,315.19 | 9.59 | 🟢 medium — moderately distinctive |
| 540 | **effect** | 10 | 2,267.05 | 4.695295 | 🟢 medium — moderately distinctive |
| 541 | **himself** | 6 | 2,260.07 | 7.801376 | 🟢 medium — moderately distinctive |
| 542 | **know** | 8 | 2,257.21 | 5.843631 | 🟢 medium — moderately distinctive |
| 543 | **excess** | 8 | 2,239.45 | 5.797646 | 🟢 medium — moderately distinctive |
| 544 | **false** | 6 | 2,236.88 | 7.721333 | 🟢 medium — moderately distinctive |
| 545 | **groups** | 8 | 2,235.13 | 5.786473 | 🟢 medium — moderately distinctive |
| 546 | **taking** | 9 | 2,228.05 | 5.127227 | 🟢 medium — moderately distinctive |
| 547 | **unpleasant** | 5 | 2,218.07 | 9.18767 | 🟢 medium — moderately distinctive |
| 548 | **characteristics** | 5 | 2,218.07 | 9.18767 | 🟢 medium — moderately distinctive |
| 549 | **search** | 6 | 2,215.41 | 7.647225 | 🟢 medium — moderately distinctive |
| 550 | **towards** | 8 | 2,210.20 | 5.721934 | 🟢 medium — moderately distinctive |
| 551 | **speculation** | 8 | 2,179.28 | 5.641891 | 🟢 medium — moderately distinctive |
| 552 | **relation** | 6 | 2,176.73 | 7.513694 | 🟢 medium — moderately distinctive |
| 553 | **connected** | 6 | 2,176.73 | 7.513694 | 🟢 medium — moderately distinctive |
| 554 | **language** | 6 | 2,159.16 | 7.453069 | 🟢 medium — moderately distinctive |
| 555 | **exist** | 6 | 2,159.16 | 7.453069 | 🟢 medium — moderately distinctive |
| 556 | **present** | 9 | 2,108.69 | 4.85256 | 🟢 medium — moderately distinctive |
| 557 | **unfavourable** | 5 | 2,094.74 | 8.676844 | 🟢 medium — moderately distinctive |
| 558 | **means** | 8 | 2,081.38 | 5.388443 | 🟢 medium — moderately distinctive |
| 559 | **conduct** | 6 | 2,047.44 | 7.067407 | 🟢 medium — moderately distinctive |
| 560 | **holds** | 8 | 2,043.00 | 5.28907 | 🟢 medium — moderately distinctive |
| 561 | **single** | 7 | 2,031.16 | 6.009616 | 🟢 medium — moderately distinctive |
| 562 | **calm** | 6 | 2,004.44 | 6.918987 | 🟢 medium — moderately distinctive |
| 563 | **else** | 6 | 2,004.44 | 6.918987 | 🟢 medium — moderately distinctive |
| 564 | **caused** | 8 | 1,989.47 | 5.150484 | 🟢 medium — moderately distinctive |
| 565 | **every** | 7 | 1,959.52 | 5.797646 | 🟢 medium — moderately distinctive |
| 566 | **doubt** | 6 | 1,918.61 | 6.622721 | 🟢 medium — moderately distinctive |
| 567 | **because** | 11 | 1,912.25 | 3.600421 | 🟢 medium — moderately distinctive |
| 568 | **reflection** | 5 | 1,883.39 | 7.801376 | 🟢 medium — moderately distinctive |
| 569 | **friendship** | 4 | 1,852.76 | 9.593135 | 🟢 medium — moderately distinctive |
| 570 | **courtesy** | 4 | 1,852.76 | 9.593135 | 🟢 medium — moderately distinctive |
| 571 | **sixteen** | 4 | 1,852.76 | 9.593135 | 🟢 medium — moderately distinctive |
| 572 | **sky** | 4 | 1,852.76 | 9.593135 | 🟢 medium — moderately distinctive |
| 573 | **pair** | 4 | 1,852.76 | 9.593135 | 🟢 medium — moderately distinctive |
| 574 | **manifest** | 4 | 1,852.76 | 9.593135 | 🟢 medium — moderately distinctive |
| 575 | **fever** | 4 | 1,852.76 | 9.593135 | 🟢 medium — moderately distinctive |
| 576 | **envy** | 4 | 1,852.76 | 9.593135 | 🟢 medium — moderately distinctive |
| 577 | **ill-will** | 4 | 1,852.76 | 9.593135 | 🟢 medium — moderately distinctive |
| 578 | **cūḷantaradukaṃ** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 579 | **unperverted** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 580 | **piṭṭhidukaṃ** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 581 | **partake** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 582 | **causal** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 583 | **immoderation** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 584 | **perceiving** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 585 | **rejoicing** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 586 | **scruples** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 587 | **hating** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 588 | **calming** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 589 | **tranquillizing** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 590 | **tranquillity** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 591 | **recitation** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 592 | **nutriments** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 593 | **instigation** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 594 | **suppressing** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 595 | **catasso** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 596 | **paṭipadā** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 597 | **soḷasakkhattukaṃ** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 598 | **deliverance** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 599 | **conception** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 600 | **nothingness** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 601 | **non-perception** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 602 | **passions** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 603 | **inverted** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 604 | **uprising** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 605 | **root-condition** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 606 | **sapids** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 607 | **tactile** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 608 | **deportment** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 609 | **rūpassa** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 610 | **femininity** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 611 | **spatial** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 612 | **non-faculty** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 613 | **sixfold** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 614 | **recluses** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 615 | **brahmins** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 616 | **afore-mentioned** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 617 | **conversant** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 618 | **re-created** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 619 | **supervened** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 620 | **cessation** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 621 | **fondness** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 622 | **finite** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 623 | **shiftiness** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 624 | **theories** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 625 | **meanness** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 626 | **co-āsava** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 627 | **entranced** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 628 | **covetous** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 629 | **dejected** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 630 | **dwell** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 631 | **dread** | 4 | 1,852.16 | 9.59 | 🟢 medium — moderately distinctive |
| 632 | **existence** | 5 | 1,846.17 | 7.647225 | 🟢 medium — moderately distinctive |
| 633 | **categories** | 5 | 1,846.17 | 7.647225 | 🟢 medium — moderately distinctive |
| 634 | **further** | 10 | 1,832.63 | 3.795559 | 🟢 medium — moderately distinctive |
| 635 | **training** | 5 | 1,829.52 | 7.578232 | 🟢 medium — moderately distinctive |
| 636 | **judgment** | 5 | 1,829.52 | 7.578232 | 🟢 medium — moderately distinctive |
| 637 | **full** | 9 | 1,805.59 | 4.155056 | 🟢 medium — moderately distinctive |
| 638 | **procedure** | 5 | 1,785.50 | 7.395911 | 🟢 medium — moderately distinctive |
| 639 | **reaction** | 6 | 1,784.31 | 6.159148 | 🟢 medium — moderately distinctive |
| 640 | **vice** | 7 | 1,783.09 | 5.275647 | 🟢 medium — moderately distinctive |
| 641 | **disposing** | 4 | 1,774.45 | 9.18767 | 🟢 medium — moderately distinctive |
| 642 | **hears** | 4 | 1,774.45 | 9.18767 | 🟢 medium — moderately distinctive |
| 643 | **occupation** | 4 | 1,774.45 | 9.18767 | 🟢 medium — moderately distinctive |
| 644 | **proximity** | 4 | 1,774.45 | 9.18767 | 🟢 medium — moderately distinctive |
| 645 | **analysis** | 5 | 1,760.07 | 7.29055 | 🟢 medium — moderately distinctive |
| 646 | **understood** | 5 | 1,760.07 | 7.29055 | 🟢 medium — moderately distinctive |
| 647 | **disposition** | 5 | 1,760.07 | 7.29055 | 🟢 medium — moderately distinctive |
| 648 | **research** | 7 | 1,748.83 | 5.174295 | 🟢 medium — moderately distinctive |
| 649 | **harm** | 5 | 1,748.29 | 7.24176 | 🟢 medium — moderately distinctive |
| 650 | **set** | 9 | 1,727.94 | 3.976364 | 🟢 medium — moderately distinctive |
| 651 | **preservation** | 4 | 1,718.89 | 8.899988 | 🟢 medium — moderately distinctive |
| 652 | **attributes** | 4 | 1,718.89 | 8.899988 | 🟢 medium — moderately distinctive |
| 653 | **namely** | 4 | 1,718.89 | 8.899988 | 🟢 medium — moderately distinctive |
| 654 | **united** | 9 | 1,704.86 | 3.923254 | 🟢 medium — moderately distinctive |
| 655 | **freedom** | 5 | 1,696.73 | 7.028186 | 🟢 medium — moderately distinctive |
| 656 | **nature** | 5 | 1,696.73 | 7.028186 | 🟢 medium — moderately distinctive |
| 657 | **true** | 5 | 1,687.62 | 6.990446 | 🟢 medium — moderately distinctive |
| 658 | **leading** | 7 | 1,685.86 | 4.987965 | 🟢 medium — moderately distinctive |
| 659 | **focussing** | 4 | 1,675.79 | 8.676844 | 🟢 medium — moderately distinctive |
| 660 | **omitted** | 4 | 1,675.79 | 8.676844 | 🟢 medium — moderately distinctive |
| 661 | **notion** | 4 | 1,675.79 | 8.676844 | 🟢 medium — moderately distinctive |
| 662 | **female** | 4 | 1,675.79 | 8.676844 | 🟢 medium — moderately distinctive |
| 663 | **vacuum** | 4 | 1,675.79 | 8.676844 | 🟢 medium — moderately distinctive |
| 664 | **gotten** | 4 | 1,675.79 | 8.676844 | 🟢 medium — moderately distinctive |
| 665 | **impact** | 7 | 1,656.73 | 4.901787 | 🟢 medium — moderately distinctive |
| 666 | **method** | 5 | 1,646.60 | 6.820546 | 🟢 medium — moderately distinctive |
| 667 | **excluded** | 5 | 1,646.60 | 6.820546 | 🟢 medium — moderately distinctive |
| 668 | **coming** | 6 | 1,612.99 | 5.567784 | 🟢 medium — moderately distinctive |
| 669 | **moderation** | 4 | 1,610.81 | 8.340372 | 🟢 medium — moderately distinctive |
| 670 | **keeps** | 4 | 1,610.81 | 8.340372 | 🟢 medium — moderately distinctive |
| 671 | **turning** | 5 | 1,598.84 | 6.622721 | 🟢 medium — moderately distinctive |
| 672 | **among** | 7 | 1,592.02 | 4.710333 | 🟢 medium — moderately distinctive |
| 673 | **relates** | 4 | 1,585.02 | 8.206841 | 🟢 medium — moderately distinctive |
| 674 | **got** | 5 | 1,553.80 | 6.436135 | 🟢 medium — moderately distinctive |
| 675 | **perceived** | 4 | 1,541.92 | 7.983697 | 🟢 medium — moderately distinctive |
| 676 | **qualities** | 4 | 1,541.92 | 7.983697 | 🟢 medium — moderately distinctive |
| 677 | **gain** | 8 | 1,531.75 | 3.965514 | 🟢 medium — moderately distinctive |
| 678 | **sections** | 4 | 1,523.52 | 7.888387 | 🟢 medium — moderately distinctive |
| 679 | **restrain** | 4 | 1,506.71 | 7.801376 | 🟢 medium — moderately distinctive |
| 680 | **future** | 7 | 1,495.75 | 4.425496 | 🟢 medium — moderately distinctive |
| 681 | **yellow** | 4 | 1,491.25 | 7.721333 | 🟢 medium — moderately distinctive |
| 682 | **against** | 9 | 1,489.06 | 3.426667 | 🟢 medium — moderately distinctive |
| 683 | **seeing** | 4 | 1,476.94 | 7.647225 | 🟢 medium — moderately distinctive |
| 684 | **developed** | 5 | 1,464.63 | 6.066775 | 🟢 medium — moderately distinctive |
| 685 | **ones** | 4 | 1,463.61 | 7.578232 | 🟢 medium — moderately distinctive |
| 686 | **man** | 4 | 1,439.44 | 7.453069 | 🟢 medium — moderately distinctive |
| 687 | **precious** | 4 | 1,417.96 | 7.341843 | 🟢 medium — moderately distinctive |
| 688 | **watch** | 4 | 1,417.96 | 7.341843 | 🟢 medium — moderately distinctive |
| 689 | **unknown** | 4 | 1,398.63 | 7.24176 | 🟢 medium — moderately distinctive |
| 690 | **part** | 7 | 1,397.08 | 4.13355 | 🟢 medium — moderately distinctive |
| 691 | **amity** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 692 | **inception** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 693 | **glory** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 694 | **constituents** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 695 | **respecting** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 696 | **indifferent** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 697 | **renounce** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 698 | **abstain** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 699 | **trespass** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 700 | **visibility** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 701 | **perplexed** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 702 | **attainment** | 3 | 1,389.57 | 9.593135 | 🟢 medium — moderately distinctive |
| 703 | **hetugocchakaṃ** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 704 | **mundane** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 705 | **cognized** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 706 | **āsavagocchakaṃ** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 707 | **saṃyojanagocchakaṃ** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 708 | **ganthagocchakaṃ** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 709 | **oghagocchakaṃ** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 710 | **yogagocchakaṃ** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 711 | **nīvaraṇagocchakaṃ** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 712 | **parāmāsagocchakaṃ** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 713 | **mahantaradukaṃ** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 714 | **detached** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 715 | **upādānagocchakaṃ** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 716 | **kilesagocchakaṃ** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 717 | **annihilation** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 718 | **suavity** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 719 | **fallacy** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 720 | **directness** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 721 | **purposefulness** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 722 | **superposing** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 723 | **solidity** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 724 | **steadfastness** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 725 | **unfaltering** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 726 | **unflinching** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 727 | **endurance** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 728 | **superficiality** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 729 | **discernment** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 730 | **differentiation** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 731 | **erudition** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 732 | **subtlety** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 733 | **breadth** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 734 | **sagacity** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 735 | **splendour** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 736 | **continuance** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 737 | **smoothness** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 738 | **rigidity** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 739 | **seq** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 740 | **dwelling** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 741 | **ārammaṇāni** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 742 | **parittāni** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 743 | **beautiful** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 744 | **ugly** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 745 | **appamāṇāni** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 746 | **soḷasakkhattukāni** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 747 | **equanimity** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 748 | **believing** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 749 | **awakening** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 750 | **averse** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 751 | **undone** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 752 | **transgress** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 753 | **causeway** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 754 | **arahantship** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 755 | **hostility** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 756 | **abruptness** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 757 | **scarifying** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 758 | **vii** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 759 | **viii** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 760 | **sensibility** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 761 | **earthy** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 762 | **masculinity** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 763 | **tangibles** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 764 | **answered** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 765 | **exposition** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 766 | **corruptions** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 767 | **assignable** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 768 | **holiness** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 769 | **appertaining** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 770 | **personal-external** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 771 | **languishing** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 772 | **cleaving** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 773 | **longing** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 774 | **consort** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 775 | **māra** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 776 | **rapacity** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 777 | **pleasures** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 778 | **immoral** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 779 | **alms** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 780 | **sacrifice** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 781 | **deeds** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 782 | **mother** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 783 | **unguarded** | 3 | 1,389.12 | 9.59 | 🟢 medium — moderately distinctive |
| 784 | **work** | 6 | 1,386.23 | 4.785024 | 🟢 medium — moderately distinctive |
| 785 | **door** | 4 | 1,381.06 | 7.150788 | 🟢 medium — moderately distinctive |
| 786 | **heard** | 4 | 1,381.06 | 7.150788 | 🟢 medium — moderately distinctive |
| 787 | **make** | 7 | 1,364.21 | 4.036307 | 🟢 medium — moderately distinctive |
| 788 | **fifth** | 4 | 1,350.09 | 6.990446 | 🟢 medium — moderately distinctive |
| 789 | **name** | 6 | 1,343.43 | 4.637308 | 🟢 medium — moderately distinctive |
| 790 | **terms** | 7 | 1,331.88 | 3.940646 | 🟢 medium — moderately distinctive |
| 791 | **discreet** | 3 | 1,330.84 | 9.18767 | 🟢 medium — moderately distinctive |
| 792 | **patience** | 3 | 1,330.84 | 9.18767 | 🟢 medium — moderately distinctive |
| 793 | **sluggishness** | 3 | 1,330.84 | 9.18767 | 🟢 medium — moderately distinctive |
| 794 | **cohesiveness** | 3 | 1,330.84 | 9.18767 | 🟢 medium — moderately distinctive |
| 795 | **content** | 4 | 1,329.74 | 6.885085 | 🟢 medium — moderately distinctive |
| 796 | **cause** | 5 | 1,323.51 | 5.482261 | 🟢 medium — moderately distinctive |
| 797 | **next** | 7 | 1,322.52 | 3.912963 | 🟢 medium — moderately distinctive |
| 798 | **light** | 5 | 1,317.65 | 5.457969 | 🟢 medium — moderately distinctive |
| 799 | **methods** | 4 | 1,299.97 | 6.730934 | 🟢 medium — moderately distinctive |
| 800 | **foolish** | 3 | 1,289.17 | 8.899988 | 🟢 medium — moderately distinctive |
| 801 | **expression** | 3 | 1,289.17 | 8.899988 | 🟢 medium — moderately distinctive |
| 802 | **restoration** | 3 | 1,289.17 | 8.899988 | 🟢 medium — moderately distinctive |
| 803 | **opposite** | 3 | 1,289.17 | 8.899988 | 🟢 medium — moderately distinctive |
| 804 | **substitution** | 3 | 1,289.17 | 8.899988 | 🟢 medium — moderately distinctive |
| 805 | **pity** | 3 | 1,289.17 | 8.899988 | 🟢 medium — moderately distinctive |
| 806 | **bias** | 3 | 1,289.17 | 8.899988 | 🟢 medium — moderately distinctive |
| 807 | **father** | 3 | 1,289.17 | 8.899988 | 🟢 medium — moderately distinctive |
| 808 | **respect** | 4 | 1,279.07 | 6.622721 | 🟢 medium — moderately distinctive |
| 809 | **dark** | 3 | 1,256.85 | 8.676844 | 🟢 medium — moderately distinctive |
| 810 | **sword** | 3 | 1,256.85 | 8.676844 | 🟢 medium — moderately distinctive |
| 811 | **destroy** | 3 | 1,256.85 | 8.676844 | 🟢 medium — moderately distinctive |
| 812 | **concepts** | 3 | 1,256.85 | 8.676844 | 🟢 medium — moderately distinctive |
| 813 | **pain** | 3 | 1,256.85 | 8.676844 | 🟢 medium — moderately distinctive |
| 814 | **excitement** | 3 | 1,256.85 | 8.676844 | 🟢 medium — moderately distinctive |
| 815 | **excited** | 3 | 1,256.85 | 8.676844 | 🟢 medium — moderately distinctive |
| 816 | **guarded** | 3 | 1,256.85 | 8.676844 | 🟢 medium — moderately distinctive |
| 817 | **kept** | 4 | 1,255.78 | 6.502093 | 🟢 medium — moderately distinctive |
| 818 | **idea** | 4 | 1,255.78 | 6.502093 | 🟢 medium — moderately distinctive |
| 819 | **individual** | 4 | 1,251.44 | 6.47962 | 🟢 medium — moderately distinctive |
| 820 | **working** | 5 | 1,250.62 | 5.180337 | 🟢 medium — moderately distinctive |
| 821 | **putting** | 4 | 1,247.19 | 6.457641 | 🟢 medium — moderately distinctive |
| 822 | **thoroughly** | 3 | 1,230.44 | 8.494523 | 🟢 medium — moderately distinctive |
| 823 | **sees** | 6 | 1,227.33 | 4.236549 | 🟢 medium — moderately distinctive |
| 824 | **created** | 4 | 1,227.26 | 6.354457 | 🟢 medium — moderately distinctive |
| 825 | **feel** | 4 | 1,212.68 | 6.278949 | 🟢 medium — moderately distinctive |
| 826 | **inertia** | 3 | 1,208.11 | 8.340372 | 🟢 medium — moderately distinctive |
| 827 | **accumulation** | 3 | 1,208.11 | 8.340372 | 🟢 medium — moderately distinctive |
| 828 | **age** | 3 | 1,208.11 | 8.340372 | 🟢 medium — moderately distinctive |
| 829 | **portion** | 4 | 1,202.42 | 6.225839 | 🟢 medium — moderately distinctive |
| 830 | **incur** | 3 | 1,188.77 | 8.206841 | 🟢 medium — moderately distinctive |
| 831 | **floods** | 3 | 1,171.70 | 8.089058 | 🟢 medium — moderately distinctive |
| 832 | **develop** | 4 | 1,171.70 | 6.066775 | 🟢 medium — moderately distinctive |
| 833 | **bulk** | 4 | 1,158.00 | 5.995823 | 🟢 medium — moderately distinctive |
| 834 | **bright** | 3 | 1,156.44 | 7.983697 | 🟢 medium — moderately distinctive |
| 835 | **absorbed** | 3 | 1,156.44 | 7.983697 | 🟢 medium — moderately distinctive |
| 836 | **stone** | 3 | 1,156.44 | 7.983697 | 🟢 medium — moderately distinctive |
| 837 | **eighth** | 3 | 1,156.44 | 7.983697 | 🟢 medium — moderately distinctive |
| 838 | **gets** | 4 | 1,155.37 | 5.982217 | 🟢 medium — moderately distinctive |
| 839 | **toward** | 4 | 1,145.20 | 5.929574 | 🟢 medium — moderately distinctive |
| 840 | **conditions** | 5 | 1,142.71 | 4.733323 | 🟢 medium — moderately distinctive |
| 841 | **processes** | 3 | 1,130.03 | 7.801376 | 🟢 medium — moderately distinctive |
| 842 | **fixing** | 3 | 1,130.03 | 7.801376 | 🟢 medium — moderately distinctive |
| 843 | **seventh** | 3 | 1,130.03 | 7.801376 | 🟢 medium — moderately distinctive |
| 844 | **must** | 5 | 1,129.95 | 4.68048 | 🟢 medium — moderately distinctive |
| 845 | **seen** | 5 | 1,122.09 | 4.647928 | 🟢 medium — moderately distinctive |
| 846 | **takes** | 4 | 1,121.91 | 5.808946 | 🟢 medium — moderately distinctive |
| 847 | **give** | 5 | 1,119.53 | 4.637308 | 🟢 medium — moderately distinctive |
| 848 | **certain** | 5 | 1,116.15 | 4.623322 | 🟢 medium — moderately distinctive |
| 849 | **anyone** | 3 | 1,107.70 | 7.647225 | 🟢 medium — moderately distinctive |
| 850 | **refrain** | 3 | 1,097.71 | 7.578232 | 🟢 medium — moderately distinctive |
| 851 | **exactly** | 3 | 1,097.71 | 7.578232 | 🟢 medium — moderately distinctive |
| 852 | **bearing** | 3 | 1,088.36 | 7.513694 | 🟢 medium — moderately distinctive |
| 853 | **flood** | 3 | 1,088.36 | 7.513694 | 🟢 medium — moderately distinctive |
| 854 | **science** | 3 | 1,088.36 | 7.513694 | 🟢 medium — moderately distinctive |
| 855 | **flow** | 4 | 1,082.35 | 5.604151 | 🟢 medium — moderately distinctive |
| 856 | **iii** | 3 | 1,079.58 | 7.453069 | 🟢 medium — moderately distinctive |
| 857 | **clear** | 4 | 1,073.61 | 5.558895 | 🟢 medium — moderately distinctive |
| 858 | **effort** | 4 | 1,071.91 | 5.550084 | 🟢 medium — moderately distinctive |
| 859 | **considered** | 4 | 1,065.25 | 5.515598 | 🟢 medium — moderately distinctive |
| 860 | **aspects** | 3 | 1,063.47 | 7.341843 | 🟢 medium — moderately distinctive |
| 861 | **bases** | 3 | 1,063.47 | 7.341843 | 🟢 medium — moderately distinctive |
| 862 | **manner** | 3 | 1,056.04 | 7.29055 | 🟢 medium — moderately distinctive |
| 863 | **view** | 4 | 1,040.69 | 5.388443 | 🟢 medium — moderately distinctive |
| 864 | **ocean** | 3 | 1,035.80 | 7.150788 | 🟢 medium — moderately distinctive |
| 865 | **another** | 5 | 1,029.71 | 4.265259 | 🟢 medium — moderately distinctive |
| 866 | **usual** | 3 | 1,023.72 | 7.067407 | 🟢 medium — moderately distinctive |
| 867 | **happened** | 3 | 1,023.72 | 7.067407 | 🟢 medium — moderately distinctive |
| 868 | **general** | 5 | 999.46 | 4.139953 | 🟢 medium — moderately distinctive |
| 869 | **mark** | 4 | 997.02 | 5.162318 | 🟢 medium — moderately distinctive |
| 870 | **chapter** | 3 | 992.56 | 6.852295 | 🟢 medium — moderately distinctive |
| 871 | **criticism** | 3 | 987.96 | 6.820546 | 🟢 medium — moderately distinctive |
| 872 | **purpose** | 3 | 970.90 | 6.702763 | 🟢 medium — moderately distinctive |
| 873 | **matters** | 3 | 966.93 | 6.675364 | 🟢 medium — moderately distinctive |
| 874 | **realized** | 3 | 966.93 | 6.675364 | 🟢 medium — moderately distinctive |
| 875 | **conditioned** | 3 | 959.30 | 6.622721 | 🟢 medium — moderately distinctive |
| 876 | **addition** | 4 | 944.94 | 4.892655 | 🟢 medium — moderately distinctive |
| 877 | **calling** | 3 | 935.39 | 6.457641 | 🟢 medium — moderately distinctive |
| 878 | **produces** | 3 | 935.39 | 6.457641 | 🟢 medium — moderately distinctive |
| 879 | **repeated** | 3 | 932.28 | 6.436135 | 🟢 medium — moderately distinctive |
| 880 | **red** | 3 | 932.28 | 6.436135 | 🟢 medium — moderately distinctive |
| 881 | **explanations** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 882 | **striving** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 883 | **remembering** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 884 | **omission** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 885 | **experiences** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 886 | **utter** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 887 | **uncommitted** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 888 | **evasion** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 889 | **stiffness** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 890 | **perfected** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 891 | **noise** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 892 | **relatives** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 893 | **corrupt** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 894 | **piling** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 895 | **loving** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 896 | **gifts** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 897 | **distinguish** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 898 | **sleep** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 899 | **recognizes** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 900 | **sport** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 901 | **struggles** | 2 | 926.38 | 9.593135 | 🟢 medium — moderately distinctive |
| 902 | **mātikā** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 903 | **wrongfulness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 904 | **righteousness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 905 | **harmless** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 906 | **thunderbolt** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 907 | **eternalism** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 908 | **contumacy** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 909 | **affirming** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 910 | **negating** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 911 | **upright** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 912 | **loveableness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 913 | **gateways** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 914 | **forgetfulness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 915 | **unintelligence** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 916 | **morals** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 917 | **agitated** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 918 | **discontent** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 919 | **kāmāvacarakusalaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 920 | **cittaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 921 | **vitakko** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 922 | **vicāro** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 923 | **mirth** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 924 | **merriment** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 925 | **felicity** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 926 | **exultation** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 927 | **sukhaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 928 | **cittass** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 929 | **ekaggatā** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 930 | **unperturbed** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 931 | **exertion** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 932 | **zeal** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 933 | **ardour** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 934 | **vigour** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 935 | **fortitude** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 936 | **recollecting** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 937 | **obliviousness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 938 | **jīvitindriyaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 939 | **greediness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 940 | **infatuation** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 941 | **infatuated** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 942 | **straightness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 943 | **twist** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 944 | **crookedness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 945 | **manāyatanaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 946 | **manoviññāṇadhātu** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 947 | **suññatavāro** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 948 | **constituting** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 949 | **upekkhā** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 950 | **rūpāvacarakusalaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 951 | **self-evolved** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 952 | **self-aware** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 953 | **sense-consciousness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 954 | **whereof** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 955 | **dwelleth** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 956 | **pañcakanayo** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 957 | **artifices** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 958 | **aṭṭhakasiṇaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 959 | **abhibhāyatanāni** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 960 | **mastery-formula** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 961 | **dve** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 962 | **suvaṇṇa-dubbaṇṇāni** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 963 | **idampi** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 964 | **deliverances** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 965 | **tīṇi** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 966 | **vimokkhāni** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 967 | **divine** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 968 | **brahmavihārajhānāni** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 969 | **discursive** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 970 | **sympathy** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 971 | **foul** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 972 | **arūpāvacarakusalaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 973 | **suddhikapaṭipadā** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 974 | **self-awareness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 975 | **incitement** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 976 | **truths** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 977 | **suññataṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 978 | **appaṇihitaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 979 | **vīsati** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 980 | **mahānayā** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 981 | **residuum** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 982 | **lusting** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 983 | **lustfulness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 984 | **badness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 985 | **childishness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 986 | **obsession** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 987 | **dukkhaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 988 | **churlishness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 989 | **disgust** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 990 | **dubiety** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 991 | **puzzlement** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 992 | **cross-roads** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 993 | **incapacity** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 994 | **disquietude** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 995 | **schematized** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 996 | **suddhika-suññataṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 997 | **catukkaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 998 | **pañcakaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 999 | **chakkaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1000 | **sattakaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1001 | **aṭṭhakaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1002 | **navakaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1003 | **dasakaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1004 | **ekādasakaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1005 | **studentship** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1006 | **lucent** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1007 | **hither** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1008 | **impingeing** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1009 | **smelt** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1010 | **tasted** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1011 | **bark** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1012 | **upādāniyaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1013 | **reacts-and-impinges** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1014 | **react-or-impinge** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1015 | **indriyaṃ** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1016 | **potentialities** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1017 | **viññatti** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1018 | **vatthu** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1019 | **descriptions** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1020 | **threefold** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1021 | **opposites** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1022 | **above-named** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1023 | **potentiality** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1024 | **imagined** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1025 | **flame** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1026 | **sevenfold** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1027 | **comprehensible** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1028 | **agreeable** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1029 | **disagreeable** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1030 | **ninefold** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1031 | **tenfold** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1032 | **elevenfold** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1033 | **baneful** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1034 | **perceives** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1035 | **comprehends** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1036 | **rites** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1037 | **topmost** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1038 | **firstly** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1039 | **cultivating** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1040 | **unborn** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1041 | **dissolved** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1042 | **self-referable** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1043 | **considerateness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1044 | **causation** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1045 | **affection** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1046 | **mumbling** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1047 | **hungering** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1048 | **envying** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1049 | **yoke** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1050 | **latent** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1051 | **avarice** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1052 | **abhijjhā** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1053 | **annoyance** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1054 | **uncompounded** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1055 | **repulsion** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1056 | **jealousy** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1057 | **reverence** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1058 | **aforementioned** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1059 | **kāyagantho** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1060 | **indisposition** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1061 | **unwieldiness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1062 | **lawful** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1063 | **unlawful** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1064 | **sense-desires** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1065 | **kilesā** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1066 | **heaven** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1067 | **devas** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1068 | **inclusive** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1069 | **happily** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1070 | **likeness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1071 | **norm** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1072 | **captiousness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1073 | **deference** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1074 | **gentle** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1075 | **charm** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1076 | **attains** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1077 | **sickness** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1078 | **emancipation** | 2 | 926.08 | 9.59 | 🟢 medium — moderately distinctive |
| 1079 | **main** | 4 | 918.71 | 4.756853 | 🟢 medium — moderately distinctive |
| 1080 | **alone** | 3 | 917.63 | 6.335039 | 🟢 medium — moderately distinctive |
| 1081 | **details** | 4 | 916.42 | 4.745019 | 🟢 medium — moderately distinctive |
| 1082 | **getting** | 3 | 906.90 | 6.260931 | 🟢 medium — moderately distinctive |
| 1083 | **stated** | 3 | 901.82 | 6.225839 | 🟢 medium — moderately distinctive |
| 1084 | **passed** | 3 | 901.82 | 6.225839 | 🟢 medium — moderately distinctive |
| 1085 | **highest** | 3 | 889.84 | 6.143148 | 🟢 medium — moderately distinctive |
| 1086 | **entail** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1087 | **dissolution** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1088 | **incompatible** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1089 | **mindful** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1090 | **watchful** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1091 | **hesitation** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1092 | **thirteen** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1093 | **void** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1094 | **touches** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1095 | **obtainable** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1096 | **trained** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1097 | **secondly** | 2 | 887.23 | 9.18767 | 🟢 medium — moderately distinctive |
| 1098 | **leave** | 3 | 885.31 | 6.111895 | 🟢 medium — moderately distinctive |
| 1099 | **soft** | 3 | 880.92 | 6.08159 | 🟢 medium — moderately distinctive |
| 1100 | **old** | 3 | 872.52 | 6.023602 | 🟢 medium — moderately distinctive |
| 1101 | **omissions** | 2 | 859.45 | 8.899988 | 🟢 medium — moderately distinctive |
| 1102 | **waning** | 2 | 859.45 | 8.899988 | 🟢 medium — moderately distinctive |
| 1103 | **mode** | 2 | 859.45 | 8.899988 | 🟢 medium — moderately distinctive |
| 1104 | **tense** | 2 | 859.45 | 8.899988 | 🟢 medium — moderately distinctive |
| 1105 | **appetite** | 2 | 859.45 | 8.899988 | 🟢 medium — moderately distinctive |
| 1106 | **consideration** | 3 | 853.44 | 5.891833 | 🟢 medium — moderately distinctive |
| 1107 | **determined** | 3 | 853.44 | 5.891833 | 🟢 medium — moderately distinctive |
| 1108 | **air** | 3 | 846.45 | 5.843631 | 🟢 medium — moderately distinctive |
| 1109 | **following** | 4 | 843.49 | 4.367389 | 🟢 medium — moderately distinctive |
| 1110 | **quality** | 3 | 839.79 | 5.797646 | 🟢 medium — moderately distinctive |
| 1111 | **reactions** | 2 | 837.90 | 8.676844 | 🟢 medium — moderately distinctive |
| 1112 | **discretion** | 2 | 837.90 | 8.676844 | 🟢 medium — moderately distinctive |
| 1113 | **flowers** | 2 | 837.90 | 8.676844 | 🟢 medium — moderately distinctive |
| 1114 | **mere** | 2 | 837.90 | 8.676844 | 🟢 medium — moderately distinctive |
| 1115 | **hospitality** | 2 | 837.90 | 8.676844 | 🟢 medium — moderately distinctive |
| 1116 | **devoted** | 2 | 837.90 | 8.676844 | 🟢 medium — moderately distinctive |
| 1117 | **failure** | 3 | 834.99 | 5.764494 | 🟢 medium — moderately distinctive |
| 1118 | **done** | 3 | 824.37 | 5.691163 | 🟢 medium — moderately distinctive |
| 1119 | **pieces** | 2 | 820.29 | 8.494523 | 🟢 medium — moderately distinctive |
| 1120 | **rid** | 2 | 820.29 | 8.494523 | 🟢 medium — moderately distinctive |
| 1121 | **rough** | 2 | 820.29 | 8.494523 | 🟢 medium — moderately distinctive |
| 1122 | **entrance** | 2 | 820.29 | 8.494523 | 🟢 medium — moderately distinctive |
| 1123 | **enthusiastic** | 2 | 820.29 | 8.494523 | 🟢 medium — moderately distinctive |
| 1124 | **others** | 3 | 818.63 | 5.651553 | 🟢 medium — moderately distinctive |
| 1125 | **equivalent** | 3 | 815.85 | 5.632322 | 🟢 medium — moderately distinctive |
| 1126 | **recovery** | 3 | 815.85 | 5.632322 | 🟢 medium — moderately distinctive |
| 1127 | **source** | 3 | 813.11 | 5.613454 | 🟢 medium — moderately distinctive |
| 1128 | **high** | 4 | 807.59 | 4.181489 | 🟢 medium — moderately distinctive |
| 1129 | **lightning** | 2 | 805.41 | 8.340372 | 🟢 medium — moderately distinctive |
| 1130 | **expressions** | 2 | 805.41 | 8.340372 | 🟢 medium — moderately distinctive |
| 1131 | **sustaining** | 2 | 805.41 | 8.340372 | 🟢 medium — moderately distinctive |
| 1132 | **errors** | 2 | 805.41 | 8.340372 | 🟢 medium — moderately distinctive |
| 1133 | **diminished** | 2 | 805.41 | 8.340372 | 🟢 medium — moderately distinctive |
| 1134 | **upset** | 2 | 805.41 | 8.340372 | 🟢 medium — moderately distinctive |
| 1135 | **derivatives** | 2 | 805.41 | 8.340372 | 🟢 medium — moderately distinctive |
| 1136 | **guidance** | 2 | 805.41 | 8.340372 | 🟢 medium — moderately distinctive |
| 1137 | **dual** | 2 | 805.41 | 8.340372 | 🟢 medium — moderately distinctive |
| 1138 | **shore** | 2 | 805.41 | 8.340372 | 🟢 medium — moderately distinctive |
| 1139 | **male** | 2 | 805.41 | 8.340372 | 🟢 medium — moderately distinctive |
| 1140 | **hard** | 3 | 803.93 | 5.550084 | 🟢 medium — moderately distinctive |
| 1141 | **follows** | 3 | 800.17 | 5.524108 | 🟢 medium — moderately distinctive |
| 1142 | **twelve** | 2 | 792.51 | 8.206841 | 🟢 medium — moderately distinctive |
| 1143 | **acts** | 2 | 792.51 | 8.206841 | 🟢 medium — moderately distinctive |
| 1144 | **clause** | 2 | 781.14 | 8.089058 | 🟢 medium — moderately distinctive |
| 1145 | **penetration** | 2 | 781.14 | 8.089058 | 🟢 medium — moderately distinctive |
| 1146 | **hear** | 2 | 781.14 | 8.089058 | 🟢 medium — moderately distinctive |
| 1147 | **touched** | 2 | 781.14 | 8.089058 | 🟢 medium — moderately distinctive |
| 1148 | **white** | 3 | 779.44 | 5.381008 | 🟢 medium — moderately distinctive |
| 1149 | **act** | 3 | 772.12 | 5.330455 | 🟢 medium — moderately distinctive |
| 1150 | **harmful** | 2 | 770.96 | 7.983697 | 🟢 medium — moderately distinctive |
| 1151 | **varying** | 2 | 770.96 | 7.983697 | 🟢 medium — moderately distinctive |
| 1152 | **grows** | 2 | 770.96 | 7.983697 | 🟢 medium — moderately distinctive |
| 1153 | **inclusion** | 2 | 770.96 | 7.983697 | 🟢 medium — moderately distinctive |
| 1154 | **stability** | 3 | 766.12 | 5.28907 | 🟢 medium — moderately distinctive |
| 1155 | **offering** | 3 | 766.12 | 5.28907 | 🟢 medium — moderately distinctive |
| 1156 | **applying** | 2 | 761.76 | 7.888387 | 🟢 medium — moderately distinctive |
| 1157 | **barrier** | 2 | 761.76 | 7.888387 | 🟢 medium — moderately distinctive |
| 1158 | **turmoil** | 2 | 761.76 | 7.888387 | 🟢 medium — moderately distinctive |
| 1159 | **human** | 2 | 761.76 | 7.888387 | 🟢 medium — moderately distinctive |
| 1160 | **frequent** | 2 | 761.76 | 7.888387 | 🟢 medium — moderately distinctive |
| 1161 | **persons** | 2 | 761.76 | 7.888387 | 🟢 medium — moderately distinctive |
| 1162 | **similar** | 3 | 757.57 | 5.230037 | 🟢 medium — moderately distinctive |
| 1163 | **take** | 4 | 756.06 | 3.914671 | 🟢 medium — moderately distinctive |
| 1164 | **absolutely** | 2 | 753.36 | 7.801376 | 🟢 medium — moderately distinctive |
| 1165 | **like** | 3 | 752.14 | 5.192532 | 🟢 medium — moderately distinctive |
| 1166 | **substitute** | 2 | 745.63 | 7.721333 | 🟢 medium — moderately distinctive |
| 1167 | **inability** | 2 | 745.63 | 7.721333 | 🟢 medium — moderately distinctive |
| 1168 | **forming** | 2 | 745.63 | 7.721333 | 🟢 medium — moderately distinctive |
| 1169 | **doors** | 2 | 745.63 | 7.721333 | 🟢 medium — moderately distinctive |
| 1170 | **want** | 3 | 739.39 | 5.104499 | 🟢 medium — moderately distinctive |
| 1171 | **adjusting** | 2 | 738.47 | 7.647225 | 🟢 medium — moderately distinctive |
| 1172 | **men** | 2 | 738.47 | 7.647225 | 🟢 medium — moderately distinctive |
| 1173 | **origins** | 2 | 738.47 | 7.647225 | 🟢 medium — moderately distinctive |
| 1174 | **guide** | 2 | 731.81 | 7.578232 | 🟢 medium — moderately distinctive |
| 1175 | **principles** | 2 | 731.81 | 7.578232 | 🟢 medium — moderately distinctive |
| 1176 | **declare** | 2 | 725.58 | 7.513694 | 🟢 medium — moderately distinctive |
| 1177 | **standing** | 2 | 725.58 | 7.513694 | 🟢 medium — moderately distinctive |
| 1178 | **hot** | 2 | 725.58 | 7.513694 | 🟢 medium — moderately distinctive |
| 1179 | **range** | 3 | 722.51 | 4.987965 | 🟢 medium — moderately distinctive |
| 1180 | **bound** | 2 | 719.72 | 7.453069 | 🟢 medium — moderately distinctive |
| 1181 | **heat** | 2 | 719.72 | 7.453069 | 🟢 medium — moderately distinctive |
| 1182 | **stages** | 2 | 719.72 | 7.453069 | 🟢 medium — moderately distinctive |
| 1183 | **arrived** | 2 | 719.72 | 7.453069 | 🟢 medium — moderately distinctive |
| 1184 | **compliance** | 2 | 719.72 | 7.453069 | 🟢 medium — moderately distinctive |
| 1185 | **accordance** | 2 | 719.72 | 7.453069 | 🟢 medium — moderately distinctive |
| 1186 | **resort** | 2 | 719.72 | 7.453069 | 🟢 medium — moderately distinctive |
| 1187 | **types** | 2 | 714.20 | 7.395911 | 🟢 medium — moderately distinctive |
| 1188 | **someone** | 2 | 714.20 | 7.395911 | 🟢 medium — moderately distinctive |
| 1189 | **regard** | 2 | 714.20 | 7.395911 | 🟢 medium — moderately distinctive |
| 1190 | **division** | 3 | 713.39 | 4.92499 | 🟢 medium — moderately distinctive |
| 1191 | **anger** | 2 | 708.98 | 7.341843 | 🟢 medium — moderately distinctive |
| 1192 | **continuous** | 2 | 694.82 | 7.19524 | 🟢 medium — moderately distinctive |
| 1193 | **stations** | 2 | 690.53 | 7.150788 | 🟢 medium — moderately distinctive |
| 1194 | **associate** | 2 | 690.53 | 7.150788 | 🟢 medium — moderately distinctive |
| 1195 | **feels** | 2 | 690.53 | 7.150788 | 🟢 medium — moderately distinctive |
| 1196 | **dependent** | 2 | 686.42 | 7.108229 | 🟢 medium — moderately distinctive |
| 1197 | **spirit** | 2 | 682.48 | 7.067407 | 🟢 medium — moderately distinctive |
| 1198 | **sixth** | 2 | 678.69 | 7.028186 | 🟢 medium — moderately distinctive |
| 1199 | **neutral** | 2 | 675.05 | 6.990446 | 🟢 medium — moderately distinctive |
| 1200 | **tension** | 2 | 675.05 | 6.990446 | 🟢 medium — moderately distinctive |
| 1201 | **easily** | 2 | 675.05 | 6.990446 | 🟢 medium — moderately distinctive |
| 1202 | **reached** | 3 | 674.29 | 4.655071 | 🟢 medium — moderately distinctive |
| 1203 | **reply** | 2 | 671.53 | 6.954078 | 🟢 medium — moderately distinctive |
| 1204 | **entirely** | 2 | 671.53 | 6.954078 | 🟢 medium — moderately distinctive |
| 1205 | **additional** | 3 | 668.69 | 4.616401 | 🟢 medium — moderately distinctive |
| 1206 | **nine** | 4 | 668.40 | 3.460822 | 🟢 medium — moderately distinctive |
| 1207 | **divisions** | 2 | 668.15 | 6.918987 | 🟢 medium — moderately distinctive |
| 1208 | **excellent** | 2 | 661.71 | 6.852295 | 🟢 medium — moderately distinctive |
| 1209 | **sour** | 2 | 658.64 | 6.820546 | 🟢 medium — moderately distinctive |
| 1210 | **according** | 3 | 656.25 | 4.53054 | 🟢 medium — moderately distinctive |
| 1211 | **burden** | 2 | 649.99 | 6.730934 | 🟢 medium — moderately distinctive |
| 1212 | **sweet** | 2 | 647.27 | 6.702763 | 🟢 medium — moderately distinctive |
| 1213 | **leaves** | 2 | 644.62 | 6.675364 | 🟢 medium — moderately distinctive |
| 1214 | **changing** | 2 | 642.04 | 6.648696 | 🟢 medium — moderately distinctive |
| 1215 | **scheme** | 2 | 637.09 | 6.597403 | 🟢 medium — moderately distinctive |
| 1216 | **maintenance** | 2 | 634.71 | 6.57271 | 🟢 medium — moderately distinctive |
| 1217 | **involving** | 2 | 625.72 | 6.47962 | 🟢 medium — moderately distinctive |
| 1218 | **showing** | 2 | 617.49 | 6.394462 | 🟢 medium — moderately distinctive |
| 1219 | **list** | 2 | 615.54 | 6.374259 | 🟢 medium — moderately distinctive |
| 1220 | **collapse** | 2 | 615.54 | 6.374259 | 🟢 medium — moderately distinctive |
| 1221 | **sure** | 2 | 611.76 | 6.335039 | 🟢 medium — moderately distinctive |
| 1222 | **won** | 2 | 611.76 | 6.335039 | 🟢 medium — moderately distinctive |
| 1223 | **advance** | 2 | 609.92 | 6.31599 | 🟢 medium — moderately distinctive |
| 1224 | **uncertainty** | 2 | 604.60 | 6.260931 | 🟢 medium — moderately distinctive |
| 1225 | **exercise** | 2 | 602.89 | 6.243231 | 🟢 medium — moderately distinctive |
| 1226 | **stand** | 2 | 599.56 | 6.208745 | 🟢 medium — moderately distinctive |
| 1227 | **sets** | 3 | 598.75 | 4.13355 | 🟢 medium — moderately distinctive |
| 1228 | **doing** | 2 | 596.34 | 6.175409 | 🟢 medium — moderately distinctive |
| 1229 | **intermediate** | 2 | 594.77 | 6.159148 | 🟢 medium — moderately distinctive |
| 1230 | **lowest** | 2 | 585.85 | 6.066775 | 🟢 medium — moderately distinctive |
| 1231 | **opposition** | 2 | 581.68 | 6.023602 | 🟢 medium — moderately distinctive |
| 1232 | **effects** | 2 | 581.68 | 6.023602 | 🟢 medium — moderately distinctive |
| 1233 | **sign** | 2 | 580.33 | 6.009616 | 🟢 medium — moderately distinctive |
| 1234 | **water** | 2 | 577.68 | 5.982217 | 🟢 medium — moderately distinctive |
| 1235 | **strength** | 2 | 573.85 | 5.942477 | 🟢 medium — moderately distinctive |
| 1236 | **entire** | 2 | 572.60 | 5.929574 | 🟢 medium — moderately distinctive |
| 1237 | **access** | 2 | 571.37 | 5.916835 | 🟢 medium — moderately distinctive |
| 1238 | **facility** | 2 | 567.77 | 5.879563 | 🟢 medium — moderately distinctive |
| 1239 | **bonds** | 2 | 566.60 | 5.867442 | 🟢 medium — moderately distinctive |
| 1240 | **purposes** | 2 | 566.60 | 5.867442 | 🟢 medium — moderately distinctive |
| 1241 | **mean** | 2 | 565.45 | 5.855466 | 🟢 medium — moderately distinctive |
| 1242 | **different** | 2 | 562.06 | 5.820374 | 🟢 medium — moderately distinctive |
| 1243 | **associates** | 2 | 555.62 | 5.753683 | 🟢 medium — moderately distinctive |
| 1244 | **immediate** | 2 | 554.58 | 5.742988 | 🟢 medium — moderately distinctive |
| 1245 | **concerned** | 2 | 553.56 | 5.732405 | 🟢 medium — moderately distinctive |
| 1246 | **field** | 2 | 549.58 | 5.691163 | 🟢 medium — moderately distinctive |
| 1247 | **activities** | 2 | 547.65 | 5.671162 | 🟢 medium — moderately distinctive |
| 1248 | **brought** | 2 | 545.75 | 5.651553 | 🟢 medium — moderately distinctive |
| 1249 | **process** | 2 | 540.29 | 5.594934 | 🟢 medium — moderately distinctive |
| 1250 | **specific** | 2 | 538.53 | 5.576752 | 🟢 medium — moderately distinctive |
| 1251 | **benefit** | 2 | 535.11 | 5.54135 | 🟢 medium — moderately distinctive |
| 1252 | **while** | 3 | 528.75 | 3.650336 | 🟢 medium — moderately distinctive |
| 1253 | **law** | 2 | 525.53 | 5.442095 | 🟢 medium — moderately distinctive |
| 1254 | **rules** | 2 | 525.53 | 5.442095 | 🟢 medium — moderately distinctive |
| 1255 | **efforts** | 2 | 511.40 | 5.29585 | 🟢 medium — moderately distinctive |
| 1256 | **potential** | 2 | 505.05 | 5.230037 | 🟢 medium — moderately distinctive |
| 1257 | **makes** | 2 | 503.22 | 5.211109 | 🟢 medium — moderately distinctive |
| 1258 | **people** | 2 | 503.22 | 5.211109 | 🟢 medium — moderately distinctive |
| 1259 | **capacity** | 2 | 501.43 | 5.192532 | 🟢 medium — moderately distinctive |
| 1260 | **free** | 2 | 497.37 | 5.150484 | 🔵 low — common in general English |
| 1261 | **place** | 2 | 496.24 | 5.138788 | 🔵 low — common in general English |
| 1262 | **food** | 2 | 487.14 | 5.044535 | 🔵 low — common in general English |
| 1263 | **get** | 2 | 482.16 | 4.992978 | 🔵 low — common in general English |
| 1264 | **short** | 2 | 478.82 | 4.958406 | 🔵 low — common in general English |
| 1265 | **better** | 2 | 478.82 | 4.958406 | 🔵 low — common in general English |
| 1266 | **lead** | 2 | 474.69 | 4.915644 | 🔵 low — common in general English |
| 1267 | **base** | 2 | 473.80 | 4.906385 | 🔵 low — common in general English |
| 1268 | **term** | 2 | 472.47 | 4.892655 | 🔵 low — common in general English |
| 1269 | **hold** | 2 | 471.60 | 4.883605 | 🔵 low — common in general English |
| 1270 | **worth** | 2 | 469.44 | 4.861332 | 🔵 low — common in general English |
| 1271 | **trusting** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1272 | **competence** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1273 | **cracked** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1274 | **infested** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1275 | **wont** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1276 | **comprehend** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1277 | **connotation** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1278 | **formulae** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1279 | **passages** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1280 | **retribution** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1281 | **circular** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1282 | **smoky** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1283 | **stars** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1284 | **acrid** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1285 | **recedes** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1286 | **fixes** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1287 | **expresses** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1288 | **softness** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1289 | **flesh** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1290 | **positives** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1291 | **lastly** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1292 | **compassion** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1293 | **slough** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1294 | **children** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1295 | **confer** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1296 | **dislike** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1297 | **fuming** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1298 | **comprehension** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1299 | **stiffening** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1300 | **slumbering** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1301 | **rendered** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1302 | **misconduct** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1303 | **designation** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1304 | **denomination** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1305 | **entangled** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1306 | **refraining** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1307 | **attractions** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1308 | **suffice** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1309 | **earnest** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1310 | **practised** | 1 | 463.19 | 9.593135 | 🔵 low — common in general English |
| 1311 | **homage** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1312 | **blessed** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1313 | **arahant** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1314 | **enlightened** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1315 | **abhidhammapiṭake** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1316 | **dhammasaṅgaṇīpāḷi** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1317 | **tikamātikā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1318 | **adept** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1319 | **dukamātikā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1320 | **immaterial** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1321 | **supramundane** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1322 | **suttantikadukamātikā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1323 | **infiniteness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1324 | **finiteness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1325 | **indiscretion** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1326 | **unguardedness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1327 | **guardedness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1328 | **unfalteringness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1329 | **cittuppādakaṇḍaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1330 | **padabhājanī** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1331 | **phasso** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1332 | **vedana** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1333 | **saññā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1334 | **cetanā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1335 | **pīti** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1336 | **saddhindriyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1337 | **professing** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1338 | **viriyindriyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1339 | **satindriyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1340 | **samādhindriyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1341 | **paññindriyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1342 | **goad** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1343 | **imagination** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1344 | **manindriyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1345 | **somanassin-driyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1346 | **sammā-diṭṭhi** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1347 | **sammā-sankappo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1348 | **sammā-vāyāmo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1349 | **sammāsati** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1350 | **sammā-samādhi** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1351 | **saddhābalaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1352 | **viriyabalaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1353 | **sati-balaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1354 | **samādhi-balaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1355 | **paññābalaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1356 | **hiribalaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1357 | **ottappabalaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1358 | **alobho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1359 | **greedy** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1360 | **adoso** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1361 | **spleen** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1362 | **amoho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1363 | **anabh-ijjhā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1364 | **avyāpādo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1365 | **sammādiṭṭhi** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1366 | **hiri** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1367 | **ottappaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1368 | **repose** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1369 | **kāyappassaddhi** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1370 | **cittapassaddhi** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1371 | **kāyalahutā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1372 | **alertness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1373 | **cittalahutā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1374 | **kāyamudutā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1375 | **cittamudutā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1376 | **kāyakammaññatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1377 | **tractableness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1378 | **workableness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1379 | **cittakammaññatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1380 | **kayapāguññatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1381 | **cittapāguññatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1382 | **kāyujjukatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1383 | **deflection** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1384 | **cittujjukatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1385 | **sati** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1386 | **sampajaññaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1387 | **samatho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1388 | **vipassanā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1389 | **paggāho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1390 | **avikkhepo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1391 | **pada-bhājaniyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1392 | **sangahavāraṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1393 | **koṭṭhāsavāraṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1394 | **koṭṭhāsavāro** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1395 | **āyatanāni** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1396 | **dhātuyo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1397 | **āhārā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1398 | **indriyāni** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1399 | **balāni** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1400 | **hetu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1401 | **dhammāyatanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1402 | **dhammadhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1403 | **phassāharo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1404 | **manosañcetanāhāro** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1405 | **purposiveness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1406 | **cogitation** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1407 | **viññāṇāhāro** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1408 | **pañcangikaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1409 | **jhānaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1410 | **pañcangiko** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1411 | **maggo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1412 | **tayohetū** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1413 | **distinguishable** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1414 | **sankhāra-skandha** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1415 | **intuitio** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1416 | **catukkanayo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1417 | **formulation** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1418 | **āramaṇāni** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1419 | **soḷasakkhat-tukaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1420 | **artifice** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1421 | **blue-black** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1422 | **induction** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1423 | **aparampi** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1424 | **nīlāni** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1425 | **expanse** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1426 | **luminousness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1427 | **pītāni** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1428 | **mettā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1429 | **unbiassed** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1430 | **karūṇā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1431 | **muditā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1432 | **fullness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1433 | **asubha-jhānaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1434 | **asubhajhānaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1435 | **discoloured** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1436 | **festering** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1437 | **gnawn** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1438 | **mangled** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1439 | **mutilated** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1440 | **bloody** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1441 | **worms** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1442 | **skeleton** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1443 | **arūpajhānāni** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1444 | **arūpajjhānāni** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1445 | **syā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1446 | **imbued** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1447 | **viññāṇañcāyatanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1448 | **boundless** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1449 | **ākiñcaññāyatanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1450 | **neva-saññā-nāsaññāyatanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1451 | **tebhūmakakusalaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1452 | **lokuttarakusalaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1453 | **elation** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1454 | **anaññātaññassāmītindriyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1455 | **uncomprehended** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1456 | **unattained** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1457 | **undiscerned** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1458 | **sammā-vācā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1459 | **sammā-kammanto** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1460 | **sammā-ājīvo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1461 | **unpractised** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1462 | **characterizing** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1463 | **schemata** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1464 | **suññatamūlakapaṭipadā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1465 | **suññata-mūlaka-paṭipadā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1466 | **aimless** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1467 | **appaṇihitamūlakapaṭipadā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1468 | **appaṇihita-mūlaka-paṭipadā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1469 | **adhipati** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1470 | **mystic** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1471 | **potencies** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1472 | **adhipaṭi** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1473 | **dvādasa** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1474 | **akusalāni** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1475 | **micchāsankappo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1476 | **miccha-diṭṭhi** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1477 | **ahirikabalaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1478 | **anottappabalaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1479 | **folly** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1480 | **vagueness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1481 | **obfuscation** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1482 | **inserted** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1483 | **domanassindriyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1484 | **disordered** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1485 | **syntheses** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1486 | **vicikicchā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1487 | **hesitating** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1488 | **uddhaccaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1489 | **abyākatavipāko** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1490 | **kusalavipākapañcaviññāṇāni** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1491 | **kusalavipākā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1492 | **manodhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1493 | **kusalavipākamanodhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1494 | **directing** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1495 | **self-collected-ness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1496 | **kusala-vipākamanoviññāṇadhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1497 | **kusalavipākamanoviññāṇadhātusomanassasahagatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1498 | **kusalavipākamanoviññāṇadhātuupekkhāsahagatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1499 | **aṭṭha** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1500 | **mahāvipākā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1501 | **aṭṭhamahāvipākā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1502 | **rūpāvacaravipākā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1503 | **arūpāvacaravipākā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1504 | **lokuttaravipāka-paṭhamamaggavipākā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1505 | **suddhikasuññataṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1506 | **suññata-paṭipāda** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1507 | **suññatapaṭipadā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1508 | **suddhika-appaṇihitaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1509 | **suddhikaappaṇihitaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1510 | **appaṇihita-paṭipadā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1511 | **appaṇihitapaṭipadā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1512 | **exercises** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1513 | **chandādhipateyyaṃ-suddhika-paṭipāda** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1514 | **chandādhipateyyasuddhikapaṭipadā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1515 | **chandādhipateyyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1516 | **chandādhipateyyasuddhikasuññatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1517 | **pro-gress** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1518 | **dutiyādimaggavipāko** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1519 | **aññatāvindriyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1520 | **doctrines** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1521 | **akusalavipākaabyākataṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1522 | **akusalavipākapañcaviññāṇāni** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1523 | **akusalavipākamanodhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1524 | **akusalavipākamanoviññāṇadhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1525 | **ahetukakiriyāabyākataṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1526 | **kiriyāmanodhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1527 | **kiriyāmanoviññāṇadhātusomanassasahagatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1528 | **imperturbed** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1529 | **kiriyāmanoviññāṇadhātuupekkhāsahagatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1530 | **sahetukakāmāvacarakiriyā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1531 | **rūpāvacarakiriyā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1532 | **arūpā-vacara-kiriyā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1533 | **arūpāvacarakiriyā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1534 | **rūpakaṇḍaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1535 | **uddeso** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1536 | **ekakaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1537 | **sabbaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1538 | **rūpaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1539 | **dukaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1540 | **tikaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1541 | **mātika** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1542 | **uncorrelated** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1543 | **dichotomized** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1544 | **singly** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1545 | **affording** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1546 | **inductive** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1547 | **fifthly** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1548 | **rūpavibhatti** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1549 | **ekakaniddeso** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1550 | **dukaniddeso** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1551 | **upādābhājanīyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1552 | **endowed** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1553 | **entailing** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1554 | **unavailing** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1555 | **ethical** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1556 | **impermanent** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1557 | **duvidhena** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1558 | **rūpa-sangaho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1559 | **cakkhāyatanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1560 | **crimson** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1561 | **bronze** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1562 | **green-coloured** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1563 | **hue** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1564 | **mango-bud** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1565 | **oval** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1566 | **hexagonal** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1567 | **octagonal** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1568 | **hekkaidecagonal** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1569 | **shady** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1570 | **glowing** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1571 | **frosty** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1572 | **dusty** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1573 | **moon** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1574 | **tabors** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1575 | **chank-shells** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1576 | **tom-toms** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1577 | **singing** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1578 | **clashing** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1579 | **concussion** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1580 | **sap** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1581 | **verminous** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1582 | **putrid** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1583 | **pungent** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1584 | **saline** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1585 | **alkaline** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1586 | **astringent** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1587 | **nauseous** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1588 | **itthindriyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1589 | **purisindriyaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1590 | **kāyaviññatti** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1591 | **intentness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1592 | **gaze** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1593 | **glances** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1594 | **retracts** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1595 | **vaciviññatti** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1596 | **enunciation** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1597 | **utterance** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1598 | **noises** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1599 | **articulate** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1600 | **ākāsa-dhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1601 | **lahutā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1602 | **non-rigidity** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1603 | **serviceableness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1604 | **upacayo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1605 | **santati** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1606 | **jaratā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1607 | **decrepitude** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1608 | **hoariness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1609 | **wrinkles** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1610 | **hypermaturity** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1611 | **aniccatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1612 | **breaking-up** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1613 | **kabaḷinkāro** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1614 | **āhāro** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1615 | **boiled** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1616 | **gruel** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1617 | **curds** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1618 | **tila-oil** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1619 | **cane-syrup** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1620 | **chewed** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1621 | **digested** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1622 | **upāda** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1623 | **phoṭṭhabbāyatanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1624 | **lambent** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1625 | **calorific** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1626 | **gaseous** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1627 | **aqueous** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1628 | **āpodhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1629 | **viscous** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1630 | **upādiṇṇaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1631 | **upādiṇṇ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1632 | **anupādiṇṇ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1633 | **sappaṭighaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1634 | **woman** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1635 | **mahābhūtaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1636 | **citta-samuṭṭhānaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1637 | **citta-saha-bhū** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1638 | **ānuparivatti** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1639 | **ajjhattikaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1640 | **bāhiraṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1641 | **oḷārikaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1642 | **sukhumaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1643 | **dūre** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1644 | **santike** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1645 | **cakkhusamphassassa** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1646 | **ārammaṇaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1647 | **āyatanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1648 | **dhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1649 | **insertion** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1650 | **contradictories** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1651 | **analogously** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1652 | **tikaniddeso** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1653 | **sex-faculty** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1654 | **intension** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1655 | **inquired** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1656 | **schema** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1657 | **earth-element** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1658 | **paṭhavī-dhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1659 | **hardness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1660 | **fluid-element** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1661 | **apodhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1662 | **heat-element** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1663 | **tejodhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1664 | **air-element** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1665 | **vāyodhātu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1666 | **vision-faculty** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1667 | **hearing-faculty** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1668 | **smell-faculty** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1669 | **taste-faculty** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1670 | **body-faculty** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1671 | **vision-sphere** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1672 | **hearing-sphere** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1673 | **smell-sphere** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1674 | **taste-sphere** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1675 | **body-sphere** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1676 | **shape-sphere** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1677 | **sound-sphere** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1678 | **odour-sphere** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1679 | **sapid-sphere** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1680 | **tangible-sphere** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1681 | **nikkhepakaṇḍaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1682 | **tikanikkhepaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1683 | **ease-yielding** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1684 | **ignorant** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1685 | **appertain** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1686 | **recluse** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1687 | **perceptual** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1688 | **peculiar** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1689 | **path-causes** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1690 | **path-governed** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1691 | **extinct** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1692 | **exterminated** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1693 | **forbearance** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1694 | **malignity** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1695 | **dukanikkhepaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1696 | **rāgo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1697 | **sarāgo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1698 | **seducing** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1699 | **anunayo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1700 | **anurodho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1701 | **delighting** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1702 | **nandī** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1703 | **lustful** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1704 | **nandī-rāgo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1705 | **cittassasarāgo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1706 | **icchā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1707 | **mucchā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1708 | **gulping** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1709 | **devouring** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1710 | **ajjhosānaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1711 | **cupidity** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1712 | **gedho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1713 | **voracity** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1714 | **paligedho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1715 | **saṇgo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1716 | **panko** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1717 | **ejā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1718 | **māyā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1719 | **genitrix** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1720 | **janikā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1721 | **progenitrix** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1722 | **sañjananī** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1723 | **seamstress** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1724 | **sibbanī** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1725 | **ensnares** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1726 | **jālinī** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1727 | **saritā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1728 | **diffused** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1729 | **visattikā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1730 | **thread** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1731 | **suttaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1732 | **diffusion** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1733 | **visatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1734 | **āyūhanī** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1735 | **dutiyā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1736 | **paniḍhi** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1737 | **bhavanetti** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1738 | **vanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1739 | **vanatho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1740 | **intimacy** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1741 | **santhavo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1742 | **sineho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1743 | **apekkhā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1744 | **paṭibandhu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1745 | **āsā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1746 | **āsiṃsanā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1747 | **āsiṃsitattaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1748 | **rūpāsā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1749 | **jappā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1750 | **muttering** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1751 | **murmuring** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1752 | **self-indulgence** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1753 | **loluppaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1754 | **self-indulging** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1755 | **intemperateness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1756 | **puñcikatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1757 | **sādukamyatā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1758 | **incestuous** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1759 | **adhammarāgo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1760 | **lawless** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1761 | **visamalobho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1762 | **nikanti** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1763 | **nikāmanā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1764 | **entreating** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1765 | **patthanā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1766 | **pihanā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1767 | **imploring** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1768 | **sampatthanā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1769 | **indulgence** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1770 | **kāmataṇhā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1771 | **bhavataṇhā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1772 | **non-existence** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1773 | **vibhava-taṇhā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1774 | **immateriality** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1775 | **dhammataṇhā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1776 | **ogho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1777 | **yogo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1778 | **gantho** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1779 | **upādānaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1780 | **obstruction** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1781 | **āvaraṇaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1782 | **nīvaraṇaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1783 | **chadanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1784 | **bondage** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1785 | **bandhanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1786 | **depravity** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1787 | **upakkileso** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1788 | **anusayo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1789 | **pariyuṭṭhānaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1790 | **creeper** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1791 | **latā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1792 | **vevicchaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1793 | **dukkhanidānaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1794 | **dukkhappabhavo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1795 | **trap** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1796 | **mārapāso** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1797 | **fish-hook** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1798 | **mārabalisaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1799 | **domain** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1800 | **māravisayo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1801 | **flux** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1802 | **sandataṇhā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1803 | **fishing-net** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1804 | **jalaṃtaṇhā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1805 | **leash** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1806 | **gaddulataṇhā** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1807 | **samuddo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1808 | **dear** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1809 | **conferred** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1810 | **conferring** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1811 | **groundlessly** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1812 | **vexation** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1813 | **resentment** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1814 | **ill-temper** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1815 | **irritation** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1816 | **indignation** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1817 | **antipathy** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1818 | **abhorrence** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1819 | **detestation** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1820 | **wrath** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1821 | **derangement** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1822 | **sounding** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1823 | **perspicacity** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1824 | **unwisdom** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1825 | **stupidity** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1826 | **obtuseness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1827 | **obsessed** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1828 | **indeterminates** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1829 | **kāmavacarahetū** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1830 | **supra-mundane** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1831 | **āsava-gocchakaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1832 | **thirst** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1833 | **yearning** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1834 | **rebirths** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1835 | **saṃyojana-gocchakaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1836 | **languor** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1837 | **lowly** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1838 | **overweening** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1839 | **conceitedness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1840 | **loftiness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1841 | **haughtiness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1842 | **flaunting** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1843 | **self-advertisement** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1844 | **issāsaṃyojanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1845 | **enviousness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1846 | **worship** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1847 | **maccharisaṃyojanaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1848 | **meannesses** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1849 | **grudging** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1850 | **ignobleness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1851 | **niggardliness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1852 | **generosity** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1853 | **gantha-gocchakaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1854 | **vyāpādo** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1855 | **excepting** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1856 | **ogha-gocchakaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1857 | **yoga-gocchakaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1858 | **cohering** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1859 | **clinging** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1860 | **stickiness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1861 | **shrouding** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1862 | **enveloping** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1863 | **barricading** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1864 | **drowsiness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1865 | **somnolence** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1866 | **fidgeting** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1867 | **over-scrupulousness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1868 | **conscience** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1869 | **parāmāsa-gocchakaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1870 | **contagion** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1871 | **ahantara-dukaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1872 | **sense-cognition** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1873 | **ideational** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1874 | **intellect** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1875 | **upādāna-gocchakaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1876 | **puppet-show** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1877 | **fording-place** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1878 | **kilesa-gocchakaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1879 | **severally** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1880 | **etymologically** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1881 | **kilesa** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1882 | **pāli** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1883 | **vinaya** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1884 | **dhamma** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1885 | **unregenerate** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1886 | **congenial** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1887 | **uncongenial** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1888 | **waveless** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1889 | **woe** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1890 | **parinimittavasavatti** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1891 | **brahma-world** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1892 | **akaniṭṭha** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1893 | **gods** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1894 | **denizens** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1895 | **suttantikadukanikkhepaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1896 | **enumeration** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1897 | **assigning** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1898 | **distinctive** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1899 | **discourse** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1900 | **non-rebirth** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1901 | **hereafter** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1902 | **futurity** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1903 | **surly** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1904 | **refractious** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1905 | **contumacious** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1906 | **contrariness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1907 | **unbelievers** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1908 | **uneducated** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1909 | **mean-spirited** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1910 | **witless** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1911 | **tractable** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1912 | **contradiction** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1913 | **devotion** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1914 | **believers** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1915 | **virtuous** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1916 | **eighteen** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1917 | **odorous** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1918 | **grief** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1919 | **lamentation** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1920 | **despair** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1921 | **discerning** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1922 | **uprightness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1923 | **deflexion** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1924 | **gentleness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1925 | **lowliness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1926 | **long-suffering** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1927 | **rudeness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1928 | **complacency** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1929 | **self-restraint** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1930 | **lovely** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1931 | **insolent** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1932 | **scabrous** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1933 | **vituperative** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1934 | **conducive** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1935 | **innocuous** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1936 | **affectionate** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1937 | **urbane** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1938 | **polished** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1939 | **untended** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1940 | **unwatched** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1941 | **carelessness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1942 | **adornment** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1943 | **insatiableness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1944 | **sustenance** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1945 | **allaying** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1946 | **pangs** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1947 | **blamelessness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1948 | **unmindfulness** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1949 | **non-recollection** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1950 | **non-remembrance** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1951 | **oblivion** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1952 | **computation** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1953 | **multiplying** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1954 | **immorality** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1955 | **fallacies** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1956 | **bhikkhu** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1957 | **abound** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1958 | **a-going** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1959 | **persevering** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1960 | **unresting** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1961 | **assiduous** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1962 | **reminiscent** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1963 | **births** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1964 | **decease** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1965 | **renascence** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1966 | **intoxicants** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1967 | **twofold** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1968 | **nirvāna** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1969 | **deposition** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1970 | **aṭṭhakathākaṇḍaṃ** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1971 | **tikaatthuddhāro** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1972 | **dukaatthuddhāro** | 1 | 463.04 | 9.59 | 🔵 low — common in general English |
| 1973 | **point** | 2 | 457.08 | 4.733323 | 🔵 low — common in general English |
| 1974 | **remain** | 2 | 449.87 | 4.658661 | 🔵 low — common in general English |
| 1975 | **systems** | 2 | 448.15 | 4.640835 | 🔵 low — common in general English |
| 1976 | **pulling** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1977 | **bloated** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1978 | **skin** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1979 | **co-ordination** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1980 | **repeating** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1981 | **exclusion** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1982 | **classifications** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1983 | **tending** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1984 | **substances** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1985 | **workable** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1986 | **shrinkage** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1987 | **cheese** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1988 | **eaten** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1989 | **swallowed** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1990 | **contradictory** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1991 | **illusion** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1992 | **amenable** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1993 | **educated** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1994 | **wise** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1995 | **aiding** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1996 | **subdue** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1997 | **comfort** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1998 | **repetition** | 1 | 443.61 | 9.18767 | 🔵 low — common in general English |
| 1999 | **computing** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2000 | **touching** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2001 | **species** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2002 | **awareness** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2003 | **quantitative** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2004 | **sights** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2005 | **dim** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2006 | **ageing** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2007 | **aerial** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2008 | **evolution** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2009 | **vitality** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2010 | **emotional** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2011 | **thirdly** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2012 | **feelings** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2013 | **perceptions** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2014 | **judging** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2015 | **refers** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2016 | **dissatisfied** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2017 | **thorough** | 1 | 429.72 | 8.899988 | 🔵 low — common in general English |
| 2018 | **below** | 2 | 423.58 | 4.386385 | 🔵 low — common in general English |
| 2019 | **resemble** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2020 | **unrealized** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2021 | **peace** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2022 | **paragraph** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2023 | **dull** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2024 | **mirror** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2025 | **pearl** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2026 | **drums** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2027 | **stretches** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2028 | **destruction** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2029 | **citt** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2030 | **triple** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2031 | **wealth** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2032 | **accruing** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2033 | **attribute** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2034 | **ninth** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2035 | **tenth** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2036 | **generous** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2037 | **bordering** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2038 | **implies** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2039 | **stagnation** | 1 | 418.95 | 8.676844 | 🔵 low — common in general English |
| 2040 | **occasions** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2041 | **temper** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2042 | **frame** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2043 | **gem** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2044 | **cat** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2045 | **music** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2046 | **nice** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2047 | **nutrition** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2048 | **matured** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2049 | **wanting** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2050 | **harsh** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2051 | **spoken** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2052 | **lapse** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2053 | **confused** | 1 | 410.15 | 8.494523 | 🔵 low — common in general English |
| 2054 | **previous** | 2 | 408.66 | 4.231843 | 🔵 low — common in general English |
| 2055 | **average** | 2 | 408.66 | 4.231843 | 🔵 low — common in general English |
| 2056 | **alive** | 1 | 402.70 | 8.340372 | 🔵 low — common in general English |
| 2057 | **beneath** | 1 | 402.70 | 8.340372 | 🔵 low — common in general English |
| 2058 | **interpretation** | 1 | 402.70 | 8.340372 | 🔵 low — common in general English |
| 2059 | **hunger** | 1 | 402.70 | 8.340372 | 🔵 low — common in general English |
| 2060 | **perfectly** | 1 | 396.26 | 8.206841 | 🔵 low — common in general English |
| 2061 | **realization** | 1 | 396.26 | 8.206841 | 🔵 low — common in general English |
| 2062 | **demonstrate** | 1 | 396.26 | 8.206841 | 🔵 low — common in general English |
| 2063 | **contents** | 1 | 396.26 | 8.206841 | 🔵 low — common in general English |
| 2064 | **reputation** | 1 | 396.26 | 8.206841 | 🔵 low — common in general English |
| 2065 | **edition** | 1 | 396.26 | 8.206841 | 🔵 low — common in general English |
| 2066 | **shrinking** | 1 | 396.26 | 8.206841 | 🔵 low — common in general English |
| 2067 | **dealt** | 1 | 390.57 | 8.089058 | 🔵 low — common in general English |
| 2068 | **disc** | 1 | 390.57 | 8.089058 | 🔵 low — common in general English |
| 2069 | **smooth** | 1 | 390.57 | 8.089058 | 🔵 low — common in general English |
| 2070 | **supplement** | 1 | 390.57 | 8.089058 | 🔵 low — common in general English |
| 2071 | **earliest** | 1 | 390.57 | 8.089058 | 🔵 low — common in general English |
| 2072 | **supplementary** | 1 | 390.57 | 8.089058 | 🔵 low — common in general English |
| 2073 | **watched** | 1 | 390.57 | 8.089058 | 🔵 low — common in general English |
| 2074 | **cut** | 2 | 386.30 | 4.000284 | 🔵 low — common in general English |
| 2075 | **blue** | 1 | 385.48 | 7.983697 | 🔵 low — common in general English |
| 2076 | **stems** | 1 | 385.48 | 7.983697 | 🔵 low — common in general English |
| 2077 | **bitter** | 1 | 385.48 | 7.983697 | 🔵 low — common in general English |
| 2078 | **master** | 1 | 385.48 | 7.983697 | 🔵 low — common in general English |
| 2079 | **adhering** | 1 | 385.48 | 7.983697 | 🔵 low — common in general English |
| 2080 | **square** | 1 | 380.88 | 7.888387 | 🔵 low — common in general English |
| 2081 | **eleven** | 1 | 380.88 | 7.888387 | 🔵 low — common in general English |
| 2082 | **families** | 1 | 380.88 | 7.888387 | 🔵 low — common in general English |
| 2083 | **nearer** | 1 | 380.88 | 7.888387 | 🔵 low — common in general English |
| 2084 | **restrained** | 1 | 380.88 | 7.888387 | 🔵 low — common in general English |
| 2085 | **frequently** | 1 | 380.88 | 7.888387 | 🔵 low — common in general English |
| 2086 | **lower** | 2 | 377.37 | 3.907856 | 🔵 low — common in general English |
| 2087 | **voice** | 1 | 376.68 | 7.801376 | 🔵 low — common in general English |
| 2088 | **butter** | 1 | 376.68 | 7.801376 | 🔵 low — common in general English |
| 2089 | **mood** | 1 | 376.68 | 7.801376 | 🔵 low — common in general English |
| 2090 | **termed** | 1 | 376.68 | 7.801376 | 🔵 low — common in general English |
| 2091 | **tended** | 1 | 376.68 | 7.801376 | 🔵 low — common in general English |
| 2092 | **regarded** | 1 | 372.81 | 7.721333 | 🔵 low — common in general English |
| 2093 | **fluctuation** | 1 | 372.81 | 7.721333 | 🔵 low — common in general English |
| 2094 | **discipline** | 1 | 372.81 | 7.721333 | 🔵 low — common in general English |
| 2095 | **ultimate** | 1 | 372.81 | 7.721333 | 🔵 low — common in general English |
| 2096 | **reaches** | 1 | 372.81 | 7.721333 | 🔵 low — common in general English |
| 2097 | **explanation** | 1 | 369.23 | 7.647225 | 🔵 low — common in general English |
| 2098 | **modified** | 1 | 369.23 | 7.647225 | 🔵 low — common in general English |
| 2099 | **compare** | 1 | 369.23 | 7.647225 | 🔵 low — common in general English |
| 2100 | **length** | 1 | 369.23 | 7.647225 | 🔵 low — common in general English |
| 2101 | **exclusively** | 1 | 369.23 | 7.647225 | 🔵 low — common in general English |
| 2102 | **specified** | 1 | 369.23 | 7.647225 | 🔵 low — common in general English |
| 2103 | **memory** | 1 | 369.23 | 7.647225 | 🔵 low — common in general English |
| 2104 | **pursuing** | 1 | 369.23 | 7.647225 | 🔵 low — common in general English |
| 2105 | **down** | 2 | 368.75 | 3.818584 | 🔵 low — common in general English |
| 2106 | **constitute** | 1 | 365.90 | 7.578232 | 🔵 low — common in general English |
| 2107 | **wind** | 1 | 365.90 | 7.578232 | 🔵 low — common in general English |
| 2108 | **milk** | 1 | 365.90 | 7.578232 | 🔵 low — common in general English |
| 2109 | **definition** | 1 | 365.90 | 7.578232 | 🔵 low — common in general English |
| 2110 | **anticipation** | 1 | 365.90 | 7.578232 | 🔵 low — common in general English |
| 2111 | **mass** | 1 | 365.90 | 7.578232 | 🔵 low — common in general English |
| 2112 | **stream** | 1 | 362.79 | 7.513694 | 🔵 low — common in general English |
| 2113 | **aiming** | 1 | 362.79 | 7.513694 | 🔵 low — common in general English |
| 2114 | **production** | 2 | 362.65 | 3.755405 | 🔵 low — common in general English |
| 2115 | **productive** | 1 | 359.86 | 7.453069 | 🔵 low — common in general English |
| 2116 | **leads** | 1 | 359.86 | 7.453069 | 🔵 low — common in general English |
| 2117 | **fish** | 1 | 357.10 | 7.395911 | 🔵 low — common in general English |
| 2118 | **yielding** | 1 | 357.10 | 7.395911 | 🔵 low — common in general English |
| 2119 | **experienced** | 1 | 357.10 | 7.395911 | 🔵 low — common in general English |
| 2120 | **flowing** | 1 | 357.10 | 7.395911 | 🔵 low — common in general English |
| 2121 | **forest** | 1 | 357.10 | 7.395911 | 🔵 low — common in general English |
| 2122 | **efficient** | 1 | 354.49 | 7.341843 | 🔵 low — common in general English |
| 2123 | **component** | 1 | 354.49 | 7.341843 | 🔵 low — common in general English |
| 2124 | **influences** | 1 | 354.49 | 7.341843 | 🔵 low — common in general English |
| 2125 | **afford** | 1 | 354.49 | 7.341843 | 🔵 low — common in general English |
| 2126 | **usage** | 1 | 354.49 | 7.341843 | 🔵 low — common in general English |
| 2127 | **vehicle** | 1 | 352.01 | 7.29055 | 🔵 low — common in general English |
| 2128 | **uses** | 1 | 352.01 | 7.29055 | 🔵 low — common in general English |
| 2129 | **hoping** | 1 | 345.27 | 7.150788 | 🔵 low — common in general English |
| 2130 | **juice** | 1 | 343.21 | 7.108229 | 🔵 low — common in general English |
| 2131 | **wish** | 1 | 343.21 | 7.108229 | 🔵 low — common in general English |
| 2132 | **individuals** | 1 | 341.24 | 7.067407 | 🔵 low — common in general English |
| 2133 | **fit** | 1 | 341.24 | 7.067407 | 🔵 low — common in general English |
| 2134 | **finally** | 1 | 339.35 | 7.028186 | 🔵 low — common in general English |
| 2135 | **involve** | 1 | 339.35 | 7.028186 | 🔵 low — common in general English |
| 2136 | **assurance** | 1 | 337.52 | 6.990446 | 🔵 low — common in general English |
| 2137 | **table** | 1 | 337.52 | 6.990446 | 🔵 low — common in general English |
| 2138 | **react** | 1 | 337.52 | 6.990446 | 🔵 low — common in general English |
| 2139 | **deep** | 1 | 337.52 | 6.990446 | 🔵 low — common in general English |
| 2140 | **physical** | 1 | 335.77 | 6.954078 | 🔵 low — common in general English |
| 2141 | **disease** | 1 | 335.77 | 6.954078 | 🔵 low — common in general English |
| 2142 | **flour** | 1 | 335.77 | 6.954078 | 🔵 low — common in general English |
| 2143 | **mixed** | 1 | 334.07 | 6.918987 | 🔵 low — common in general English |
| 2144 | **friendly** | 1 | 332.44 | 6.885085 | 🔵 low — common in general English |
| 2145 | **arm** | 1 | 330.85 | 6.852295 | 🔵 low — common in general English |
| 2146 | **flag** | 1 | 329.32 | 6.820546 | 🔵 low — common in general English |
| 2147 | **experience** | 1 | 327.83 | 6.789775 | 🔵 low — common in general English |
| 2148 | **acceptable** | 1 | 327.83 | 6.789775 | 🔵 low — common in general English |
| 2149 | **practice** | 1 | 327.83 | 6.789775 | 🔵 low — common in general English |
| 2150 | **works** | 1 | 324.99 | 6.730934 | 🔵 low — common in general English |
| 2151 | **advances** | 1 | 324.99 | 6.730934 | 🔵 low — common in general English |
| 2152 | **attend** | 1 | 324.99 | 6.730934 | 🔵 low — common in general English |
| 2153 | **item** | 1 | 323.63 | 6.702763 | 🔵 low — common in general English |
| 2154 | **restricted** | 1 | 322.31 | 6.675364 | 🔵 low — common in general English |
| 2155 | **entitled** | 1 | 322.31 | 6.675364 | 🔵 low — common in general English |
| 2156 | **presence** | 1 | 319.77 | 6.622721 | 🔵 low — common in general English |
| 2157 | **assumption** | 1 | 319.77 | 6.622721 | 🔵 low — common in general English |
| 2158 | **twice** | 1 | 318.55 | 6.597403 | 🔵 low — common in general English |
| 2159 | **remainder** | 1 | 317.35 | 6.57271 | 🔵 low — common in general English |
| 2160 | **actually** | 1 | 316.19 | 6.548613 | 🔵 low — common in general English |
| 2161 | **black** | 1 | 316.19 | 6.548613 | 🔵 low — common in general English |
| 2162 | **comparable** | 1 | 313.94 | 6.502093 | 🔵 low — common in general English |
| 2163 | **apparent** | 1 | 313.94 | 6.502093 | 🔵 low — common in general English |
| 2164 | **sun** | 1 | 313.94 | 6.502093 | 🔵 low — common in general English |
| 2165 | **fire** | 1 | 311.80 | 6.457641 | 🔵 low — common in general English |
| 2166 | **urges** | 1 | 310.76 | 6.436135 | 🔵 low — common in general English |
| 2167 | **goes** | 1 | 310.76 | 6.436135 | 🔵 low — common in general English |
| 2168 | **so-called** | 1 | 307.77 | 6.374259 | 🔵 low — common in general English |
| 2169 | **shell** | 1 | 306.82 | 6.354457 | 🔵 low — common in general English |
| 2170 | **terminated** | 1 | 306.82 | 6.354457 | 🔵 low — common in general English |
| 2171 | **care** | 1 | 305.88 | 6.335039 | 🔵 low — common in general English |
| 2172 | **covering** | 1 | 304.06 | 6.297298 | 🔵 low — common in general English |
| 2173 | **carried** | 1 | 300.61 | 6.225839 | 🔵 low — common in general English |
| 2174 | **shows** | 1 | 300.61 | 6.225839 | 🔵 low — common in general English |
| 2175 | **side** | 1 | 299.78 | 6.208745 | 🔵 low — common in general English |
| 2176 | **silver** | 1 | 298.17 | 6.175409 | 🔵 low — common in general English |
| 2177 | **confidence** | 1 | 296.61 | 6.143148 | 🔵 low — common in general English |
| 2178 | **turn** | 1 | 294.37 | 6.096628 | 🔵 low — common in general English |
| 2179 | **fair** | 1 | 292.93 | 6.066775 | 🔵 low — common in general English |
| 2180 | **brings** | 1 | 292.22 | 6.052176 | 🔵 low — common in general English |
| 2181 | **original** | 1 | 291.53 | 6.037787 | 🔵 low — common in general English |
| 2182 | **willing** | 1 | 288.19 | 5.968794 | 🔵 low — common in general English |
| 2183 | **region** | 1 | 287.55 | 5.955549 | 🔵 low — common in general English |
| 2184 | **active** | 1 | 287.55 | 5.955549 | 🔵 low — common in general English |
| 2185 | **rice** | 1 | 286.30 | 5.929574 | 🔵 low — common in general English |
| 2186 | **risen** | 1 | 285.08 | 5.904256 | 🔵 low — common in general English |
| 2187 | **course** | 1 | 285.08 | 5.904256 | 🔵 low — common in general English |
| 2188 | **negative** | 1 | 284.48 | 5.891833 | 🔵 low — common in general English |
| 2189 | **governor** | 1 | 284.48 | 5.891833 | 🔵 low — common in general English |
| 2190 | **forward** | 1 | 281.59 | 5.831935 | 🔵 low — common in general English |
| 2191 | **transport** | 1 | 280.48 | 5.808946 | 🔵 low — common in general English |
| 2192 | **ways** | 1 | 279.93 | 5.797646 | 🔵 low — common in general English |
| 2193 | **positive** | 1 | 278.33 | 5.764494 | 🔵 low — common in general English |
| 2194 | **named** | 1 | 277.29 | 5.742988 | 🔵 low — common in general English |
| 2195 | **big** | 1 | 276.78 | 5.732405 | 🔵 low — common in general English |
| 2196 | **indicated** | 1 | 276.78 | 5.732405 | 🔵 low — common in general English |
| 2197 | **whole** | 1 | 276.78 | 5.732405 | 🔵 low — common in general English |
| 2198 | **generally** | 1 | 276.28 | 5.721934 | 🔵 low — common in general English |
| 2199 | **building** | 1 | 274.30 | 5.681112 | 🔵 low — common in general English |
| 2200 | **opening** | 1 | 273.82 | 5.671162 | 🔵 low — common in general English |
| 2201 | **developing** | 1 | 273.35 | 5.66131 | 🔵 low — common in general English |
| 2202 | **property** | 1 | 272.41 | 5.641891 | 🔵 low — common in general English |
| 2203 | **bond** | 1 | 271.04 | 5.613454 | 🔵 low — common in general English |
| 2204 | **items** | 1 | 269.70 | 5.585802 | 🔵 low — common in general English |
| 2205 | **outside** | 1 | 269.70 | 5.585802 | 🔵 low — common in general English |
| 2206 | **mine** | 1 | 268.83 | 5.567784 | 🔵 low — common in general English |
| 2207 | **series** | 1 | 267.98 | 5.550084 | 🔵 low — common in general English |
| 2208 | **rest** | 1 | 267.98 | 5.550084 | 🔵 low — common in general English |
| 2209 | **needs** | 1 | 267.56 | 5.54135 | 🔵 low — common in general English |
| 2210 | **find** | 1 | 263.15 | 5.45 | 🔵 low — common in general English |
| 2211 | **limit** | 1 | 260.17 | 5.388443 | 🔵 low — common in general English |
| 2212 | **performance** | 1 | 259.10 | 5.366301 | 🔵 low — common in general English |
| 2213 | **principle** | 1 | 257.71 | 5.337522 | 🔵 low — common in general English |
| 2214 | **changed** | 1 | 253.77 | 5.255844 | 🔵 low — common in general English |
| 2215 | **producing** | 1 | 253.46 | 5.24933 | 🔵 low — common in general English |
| 2216 | **heavy** | 1 | 247.56 | 5.127227 | 🔵 low — common in general English |
| 2217 | **quoted** | 1 | 247.28 | 5.121496 | 🔵 low — common in general English |
| 2218 | **consider** | 1 | 246.46 | 5.104499 | 🔵 low — common in general English |
| 2219 | **again** | 1 | 244.60 | 5.065927 | 🔵 low — common in general English |
| 2220 | **rises** | 1 | 243.57 | 5.044535 | 🔵 low — common in general English |
| 2221 | **adding** | 1 | 242.56 | 5.023592 | 🔵 low — common in general English |
| 2222 | **company** | 2 | 241.79 | 2.503892 | 🔵 low — common in general English |
| 2223 | **small** | 1 | 239.88 | 4.968162 | 🔵 low — common in general English |
| 2224 | **seeking** | 1 | 239.88 | 4.968162 | 🔵 low — common in general English |
| 2225 | **response** | 1 | 238.94 | 4.948744 | 🔵 low — common in general English |
| 2226 | **ending** | 1 | 236.02 | 4.88812 | 🔵 low — common in general English |
| 2227 | **gold** | 1 | 234.94 | 4.865747 | 🔵 low — common in general English |
| 2228 | **inflation** | 1 | 233.88 | 4.843865 | 🔵 low — common in general English |
| 2229 | **account** | 1 | 227.07 | 4.702786 | 🔵 low — common in general English |
| 2230 | **number** | 1 | 221.58 | 4.589189 | 🔵 low — common in general English |
| 2231 | **within** | 1 | 220.78 | 4.57255 | 🔵 low — common in general English |
| 2232 | **used** | 1 | 220.46 | 4.565971 | 🔵 low — common in general English |
| 2233 | **low** | 1 | 219.37 | 4.543279 | 🔵 low — common in general English |
| 2234 | **decline** | 1 | 219.21 | 4.540079 | 🔵 low — common in general English |
| 2235 | **days** | 1 | 215.36 | 4.460282 | 🔵 low — common in general English |
| 2236 | **issue** | 1 | 214.51 | 4.442738 | 🔵 low — common in general English |
| 2237 | **subject** | 1 | 213.95 | 4.43121 | 🔵 low — common in general English |
| 2238 | **held** | 1 | 206.06 | 4.267689 | 🔵 low — common in general English |
| 2239 | **tender** | 1 | 205.82 | 4.262835 | 🔵 low — common in general English |
| 2240 | **firm** | 1 | 205.71 | 4.260416 | 🔵 low — common in general English |
| 2241 | **including** | 1 | 197.47 | 4.089838 | 🔵 low — common in general English |
| 2242 | **around** | 1 | 186.99 | 3.872823 | 🔵 low — common in general English |
| 2243 | **time** | 1 | 185.51 | 3.842151 | 🔵 low — common in general English |
| 2244 | **includes** | 1 | 184.68 | 3.824814 | 🔵 low — common in general English |
| 2245 | **current** | 1 | 167.00 | 3.458653 | 🔵 low — common in general English |
| 2246 | **stock** | 1 | 147.30 | 3.050663 | 🔵 low — common in general English |
| 2247 | **said** | 2 | 141.36 | 1.463813 | 🔵 low — common in general English |

---

## Observations

### 1. Text-exclusive coinages dominate the top
The highest-scoring terms are overwhelmingly **Rhys Davids coinages** — Victorian English vocabulary pressed into service for Pāli Abhidhamma concepts.
Words like *self-collectedness*, *wieldiness*, *tractableness*, *pliancy* barely exist outside this translation, giving them near-maximum IDF.

### 2. Buddhist technical register
A tight cluster — *skandha*, *jhāna*, *āsava*, *supramundane*, *incorporeal* — forms the Buddhist technical register. These score extremely high because they belong to a specialist domain absent from general English, and they recur in every paragraph.

### 3. The 'falsely familiar' vocabulary problem
Rhys Davids consciously chose ordinary English words — *zest*, *ease*, *synergies*, *contact*, *feeling* — to avoid Pāli transliteration. These occupy a mid-tier TF-IDF band: very frequent here, but their IDF is moderate because they do have a general English presence. They look everyday but carry specialist meaning.

### 4. Repetition as structure inflates TF
The *Dhammasaṅgaṇī* is formally repetitive by design (Buddhist catechism). Every mental factor is defined with the same formula across hundreds of consciousness types. Even moderately rare words (*volition*, *mindfulness*, *concomitant*) achieve unusually high raw frequencies relative to any other English text of equivalent length.

---

*Corpus reference: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth\_idf=True, lowercase=True).*  
*Generated 2026-06-04 by `generate_termbase.py`.*