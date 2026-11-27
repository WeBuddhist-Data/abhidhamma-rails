"""The ONE presence check of the pi-2 Burmese keyword mapping (map-harmonise decision 3).

Imported by every mapping script (map_all.py, map_2-4.py, map_5-7-11.py, map_6.py, map_12-14.py, map_15-16.py,
map_17.py, map_18.py); defines nothing else and runs nothing on import.

A value passes when every chunk of it occurs in the segment's Burmese, literally or by one of the ending rules
below. The ending lists are the pi-1 lists (sample rules 3, 4, 8; 4-01 rules 12, 16; 5 rule 22; pi-2 sample N11
«သည့်») merged with the endings the pi-2 agents added for their chapters; every addition names its origin:

ATTR_FROM: a chunk «Xသော» is accepted when the text has X + one of
  pi-1 / sample : သော် ၍ ပြီး သည် ခြင်း သူ ပြီ ကြသော ဘဲ သေးသော ၊ သည့် (N11)
  12-14 M1      : လျက် ကုန်သော ကြသည် ၏ ကြ၏ ။ ”        (predicate / plural / quoted forms)
  15-16 P1      : ကြ ဟူ ဟု ၏                       (plural predicate «Xကြ(သည်)», quoted «Xဟု»)
  17 (N12)      : ဟူ ကုန် လျက် ၏
  18            : ကြသည်                            (plural predicate, samiddhino)
VERB_FROM: a chunk «Xသည်» is accepted when the text has X + one of
  pi-1 / sample : ပါ၏ ၏ ပြီ သော ၍ ပြီး ခြင်း ရန် သည့် ကြ ၊ ဟူ လိမ့်မည် ။
  12-14 M1      : ရာ ” သနည်း                        (verb of a «where …» clause, quoted, question)
  15-16 P5, P6  : လျှင် ရာ                           (the condition «Xလျှင်»; the optative «Xရာ၏»)
  17 (N12)      : ပါစေ သမျှ ဟု ကုန် အံ့ လော့ မည်        (optative, imperative, future, quoted)
Further rules:
  attr-fut  (pi-1)       «Xည့်» against the text's «Xည်»
  perf-pred (5-7-11)     «Xပြီးသော» against the predicate «Xပြီး ဖြစ်…»
  neg-verb  (15-16 P2, 17 N13) «Xသည်» against the text's negated verb «မX» / infixed «…မ…» + a VERB_FROM ending
            (the keyword has no na; the positive verb is the value, as pi-1 rule 8)
  plural    (15-16 P4)   «Xလိမ့်မည်» / «Xခဲ့သည်» against «Xကြလိမ့်မည်» / «Xခဲ့ကြ…»
  neg-infix, neg-attr (pi-1 rule 8) the positive part of a negated word
  quotes    (15-16 P3)   the text's quotation marks “ ” ‘ ’ are not a word boundary (a chunk is also matched against
            the text with them removed)
"""
import re

NONE = "(no direct equivalent)"

ATTR_FROM = tuple(dict.fromkeys((
    "သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ကြသော", "ဘဲ", "သေးသော", "၊", "သည့်",   # pi-1 / sample N11
    "လျက်", "ကုန်သော", "ကြသည်", "၏", "ကြ၏", "။", "”",                                    # 12-14 M1
    "ကြ", "ဟူ", "ဟု",                                                                   # 15-16 P1
    "ကုန်",                                                                             # 17
)))
VERB_FROM = tuple(dict.fromkeys((
    "ပါ၏", "၏", "ပြီ", "သော", "၍", "ပြီး", "ခြင်း", "ရန်", "သည့်", "ကြ", "၊", "ဟူ", "လိမ့်မည်", "။",  # pi-1
    "ရာ", "”", "သနည်း",                                                                  # 12-14 M1
    "လျှင်",                                                                            # 15-16 P5 (P6 = ရာ)
    "ပါစေ", "သမျှ", "ဟု", "ကုန်", "အံ့", "လော့", "မည်",                                     # 17
)))


def chunk_present(c, text):
    """-> rule name ('exact', 'attr', 'verb', 'attr-fut', 'perf-pred', 'neg-verb', 'plural', 'neg-infix',
    'neg-attr') or None."""
    if c in text:
        return "exact"
    if c.endswith("သော") and len(c) > 3:
        st = c[:-3]
        if any(st + e in text for e in ATTR_FROM):
            return "attr"
    if c.endswith("သည်") and len(c) > 3:
        st = c[:-3]
        if any(st + e in text for e in VERB_FROM):
            return "verb"
    if c.endswith("ည့်") and c[:-3] + "ည်" in text:
        return "attr-fut"
    if c.endswith("ပြီးသော") and c[:-3] + " ဖြစ်" in text:
        return "perf-pred"
    if c.endswith("သည်") and len(c) > 3:
        st = c[:-3]
        if "မ" + st in text:
            return "neg-verb"
        for i in range(0, len(st)):
            if any(st[:i] + "မ" + st[i:] + e in text for e in VERB_FROM):
                return "neg-verb"
    for t in ("လိမ့်မည်", "ခဲ့သည်"):
        if c.endswith(t) and c[:-len(t)] + "ကြ" + t.replace("ခဲ့သည်", "ခဲ့") in text.replace("ခဲ့ကြ", "ကြခဲ့"):
            return "plural"
    for i in range(1, len(c)):
        if c[:i] + "မ" + c[i:] in text or c[:i] + " မ" + c[i:] in text:
            return "neg-infix"
    if c.endswith("သော") and len(c) > 3:
        st = c[:-3]
        for i in range(0, len(st)):
            if any((st[:i] + "မ" + st[i:]) + e in text for e in ATTR_FROM):
                return "neg-attr"
    return None


def presence(v, text):
    """-> (ok, [(chunk, rule) for every chunk not found literally])"""
    if v == NONE:
        return True, []
    bare = re.sub("[“”‘’]", "", text)
    rules = []
    for part in re.split(r" … ", v):
        for c in part.split():
            c = c.strip("“”‘’()")
            if not c:
                continue
            r = chunk_present(c, text) or chunk_present(c, bare)
            if r is None:
                return False, [(c, None)]
            if r != "exact":
                rules.append((c, r))
    return True, rules
