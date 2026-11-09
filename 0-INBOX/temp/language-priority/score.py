"""Score candidate languages: priority = demand x gap.

demand = 0.5 * reader_interest + 0.5 * community_size, each log-scaled to 0..1
reader_interest = Wikipedia user pageviews (Nov 2025-Oct 2026) of Abhidhamma Pitaka +
                  Abhidharma + Pali Canon articles in that language edition.
community_size  = Buddhists whose main reading language is this one (millions).
gap             = 1.0 no full translation found; 0.5 full but dated / criticised;
                  0.2 full and current.
"""
import json, math, sys

wp = json.load(open(sys.argv[1], encoding="utf-8"))
def wiki(code):
    return sum((wp["topics"][t]["langs"][code]["views"] or 0)
               for t in ("abhidhamma", "abhidharma", "pali_canon"))

# millions; None = no cited figure
COMMUNITY = {"th": 68, "zh": 53, "ja": 41.4, "vi": 15.6, "mr": 6.53, "ne": 2.39,
             "hi": 1.91, "mn": 1.70, "ru": 0.9, "fr": 0.6, "bo": None}
GAP = {"th": 0.2, "vi": 0.2, "ja": 0.5, "zh": 0.5, "hi": 1.0, "mr": 1.0, "ne": 1.0,
       "ru": 1.0, "fr": 1.0, "mn": 1.0, "bo": 1.0}

def lognorm(vals):
    lv = {k: math.log10(v + 1) for k, v in vals.items()}
    hi = max(lv.values())
    return {k: v / hi for k, v in lv.items()}

w = lognorm({c: wiki(c) for c in GAP})
p = lognorm({c: (COMMUNITY[c] or 0) * 1e6 for c in GAP})
rows = []
for c in GAP:
    demand = 0.5 * w[c] + 0.5 * p[c]
    rows.append((c, wiki(c), COMMUNITY[c], round(w[c], 2), round(p[c], 2),
                 round(demand, 2), GAP[c], round(demand * GAP[c], 2)))
rows.sort(key=lambda r: -r[-1])
print("lang | wiki views | community M | wiki_n | comm_n | demand | gap | priority")
for r in rows:
    print(" | ".join(str(x) for x in r))
