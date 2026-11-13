"""Check number words beyond tevīsati: for each Pāli number word, the Hindi lines must contain the expected word."""
import sys, re, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz7_common import PARTS, pairs, short

NUM = {"ekūnavīsa": "उन्नीस", "ekūnavīsati": "उन्नीस", "vīsa": "बीस", "vīsati": "बीस", "ekavīsa": "इक्कीस",
       "ekavīsati": "इक्कीस", "bāvīsa": "बाईस", "dvāvīsa": "बाईस", "bāvīsati": "बाईस", "dvāvīsati": "बाईस",
       "tevīsa": "तेईस", "tevīsati": "तेईस", "catuvīsa": "चौबीस", "catuvīsati": "चौबीस", "pañcavīsa": "पच्चीस",
       "pañcavīsati": "पच्चीस", "chabbīsa": "छब्बीस", "chabbīsati": "छब्बीस", "sattavīsa": "सत्ताईस",
       "sattavīsati": "सत्ताईस", "aṭṭhavīsa": "अट्ठाईस", "aṭṭhavīsati": "अट्ठाईस", "ekūnatiṃsa": "उनतीस",
       "tiṃsa": "तीस", "ekatiṃsa": "इकतीस", "dvattiṃsa": "बत्तीस", "tettiṃsa": "तैंतीस", "catuttiṃsa": "चौंतीस",
       "pañcatiṃsa": "पैंतीस", "chattiṃsa": "छत्तीस", "sattatiṃsa": "सैंतीस", "aṭṭhatiṃsa": "अड़तीस",
       "ekūnacattālīsa": "उनतालीस", "cattālīsa": "चालीस", "aṭṭhacattālīsa": "अड़तालीस",
       "ekūnapaññāsa": "उनचास", "paññāsa": "पचास"}
bad = collections.Counter()
ok = collections.Counter()
for part in PARTS:
    for i, (p, h) in enumerate(pairs(part)):
        for w in re.findall(r"\b(\w+)\b", p):
            lw = w.lower()
            if lw in NUM:
                if NUM[lw] in h:
                    ok[lw] += 1
                else:
                    bad[lw] += 1
                    if bad[lw] <= 3:
                        print(f"{short(part)}:{i+1} {w}: {h[:200]}")
print("ok", dict(ok))
print("missing", dict(bad))
