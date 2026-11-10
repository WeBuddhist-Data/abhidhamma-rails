"""ITCC-weighted language priority (2026-11-09): priority = itcc x gap, ties broken by the 2026-11-06 demand score.

itcc = how strongly the language's readers are attested at the International Tipitaka Chanting Ceremony, Bodhgaya
       (no per-country headcounts are published; tiers from the evidence in language-priority-report.md):
       1.0 stated thousands (India: 20,000 Indian participants projected 2025, 10,000 from Maharashtra)
       0.6 major foreign sangha with its own 2026 chanting-book script (Thai, Burmese, Sinhala, Khmer, Bengali)
       0.4 listed every year, no own book (Lao, Vietnamese) ; 0.3 small / recent (Nepali, Indonesian)
       0.1 named only among "other participants" (French, Japanese) ; 0.05 not attested (Russian, Chinese, Tibetan)
gap  = do the readers already have the Abhidhamma in their language?
       1.0 none found ; 0.7 none, but readers commonly read a neighbouring translation (Lao -> Thai)
       0.5 exists but print/scan-only, dated or hard to obtain ; 0.3 exists and is online ; 0.2 several editions online
demand_old = demand column of the 2026-11-06 ranking (Wikipedia interest + community size), tie-breaker only.
"""
ITCC = {"mr": 1.0, "hi": 1.0, "th": 0.6, "my": 0.6, "si": 0.6, "km": 0.6, "bn": 0.6, "lo": 0.4, "vi": 0.4,
        "ne": 0.3, "id": 0.3, "fr": 0.1, "ja": 0.1, "ru": 0.05, "zh": 0.05, "bo": 0.05}
GAP = {"mr": 1.0, "hi": 1.0, "th": 0.2, "my": 0.5, "si": 0.3, "km": 0.5, "bn": 0.5, "lo": 0.7, "vi": 0.3,
       "ne": 1.0, "id": 1.0, "fr": 1.0, "ja": 0.5, "ru": 1.0, "zh": 0.5, "bo": 1.0}
DEMAND_OLD = {"mr": 0.78, "hi": 0.79, "th": 0.95, "vi": 0.9, "ne": 0.67, "fr": 0.74, "ja": 0.98, "ru": 0.87,
              "zh": 0.98, "bo": 0.0}
rows = sorted(ITCC, key=lambda c: (-round(ITCC[c] * GAP[c], 2), -ITCC[c], -DEMAND_OLD.get(c, 0.5)))
print("lang | itcc | gap | priority | old demand")
for c in rows:
    print(f"{c} | {ITCC[c]} | {GAP[c]} | {ITCC[c] * GAP[c]:.2f} | {DEMAND_OLD.get(c, '-')}")
