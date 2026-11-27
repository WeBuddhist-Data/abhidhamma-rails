"""Presence check of the pi-4 Burmese keyword mapping: a copy (not an import) of the ONE shared pi-3 check
(pi-3-my/mapper-my/presence_check.py), with its ending lists unchanged, plus the pi-4 endings marked «pi-4».

Defines functions only; nothing runs on import.

A value passes when every chunk of it occurs in the segment's Burmese, literally or by one of the ending rules:
ATTR_FROM: a chunk «Xသော» is accepted when the text has X + one of
  pi-1 / pi-2 sample N11 : သော် ၍ ပြီး သည် ခြင်း သူ ပြီ ကြသော ဘဲ သေးသော ၊ သည့်
  pi-2 12-14 M1          : လျက် ကုန်သော ကြသည် ၏ ကြ၏ ။ ”
  pi-2 15-16 P1          : ကြ ဟူ ဟု
  pi-2 17                : ကုန်
  pi-3 sample M7         : သနည်း ရာ သေးသည်
  pi-4 (rule P3)         : လည်း ကား သေး လျှင် စဉ် လိမ့်မည် သကဲ့သို့ (the text's «Xလည်း / Xကား» of «both … and» /
                           contrast clauses, the «not yet» negative «မXသေး», the condition «Xလျှင်», «while» «Xစဉ်»,
                           the future predicate «Xလိမ့်မည်», the simile «Xသကဲ့သို့», «because X» «Xသဖြင့်»)
VERB_FROM: a chunk «Xသည်» is accepted when the text has X + one of
  pi-1                   : ပါ၏ ၏ ပြီ သော ၍ ပြီး ခြင်း ရန် သည့် ကြ ၊ ဟူ လိမ့်မည် ။
  pi-2 12-14 M1          : ရာ ” သနည်း
  pi-2 15-16 P5, P6      : လျှင်
  pi-2 17 (N12)          : ပါစေ သမျှ ဟု ကုန် အံ့ လော့ မည်
  pi-4 (rule P3)         : လည်း ကား သူ ဘဲ ကာ သတတ် သကဲ့သို့ (the text's «Xလည်း V၏», «Xကား», the agent noun «Xသူ»,
                           «Xဘဲ», «Xကာ», the hearsay «Xသတတ်», the simile «Xသကဲ့သို့»)
Further rules (pi-2 / pi-3, unchanged): attr-fut, perf-pred, neg-verb, plural, neg-infix, neg-attr, quotes.
pi-4 P1 name-attr: a person-type NAME «Xသူ» is accepted against the text's «Xသော ပုဂ္ဂိုလ်» (the mātikā builds a name
  before «puggalo» as an adjective, my4-zeroshot-terms «The definition frame»; brief: the same NAME in mātikā, heading and
  definition).
"""
import re

NONE = "(no direct equivalent)"

ATTR_FROM = tuple(dict.fromkeys((
    "သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ကြသော", "ဘဲ", "သေးသော", "၊", "သည့်",   # pi-1 / sample N11
    "လျက်", "ကုန်သော", "ကြသည်", "၏", "ကြ၏", "။", "”",                                    # pi-2 12-14 M1
    "ကြ", "ဟူ", "ဟု",                                                                   # pi-2 15-16 P1
    "ကုန်",                                                                             # pi-2 17
    "သနည်း", "ရာ", "သေးသည်",                                                          # pi-3 M7
    "လည်း", "ကား", "သေး", "လျှင်", "စဉ်", "လိမ့်မည်", "သကဲ့သို့", "သဖြင့်",                          # pi-4 P3
)))
VERB_FROM = tuple(dict.fromkeys((
    "ပါ၏", "၏", "ပြီ", "သော", "၍", "ပြီး", "ခြင်း", "ရန်", "သည့်", "ကြ", "၊", "ဟူ", "လိမ့်မည်", "။",  # pi-1
    "ရာ", "”", "သနည်း",                                                                  # pi-2 12-14 M1
    "လျှင်",                                                                            # pi-2 15-16 P5 / P6
    "ပါစေ", "သမျှ", "ဟု", "ကုန်", "အံ့", "လော့", "မည်",                                     # pi-2 17
    "လည်း", "ကား", "သူ", "ဘဲ", "ကာ", "သတတ်", "သကဲ့သို့",                                  # pi-4 P3
)))


def chunk_present(c, text):
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
    if c.endswith("သူ") and len(c) > 2 and c[:-2] + "သော ပုဂ္ဂိုလ်" in text:
        return "name-attr"     # pi-4 P1: a person-type NAME «Xသူ» before «puggalo» in the mātikā is «Xသော ပုဂ္ဂိုလ်»
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
    nobr = re.sub(r" ?\[[^\]]*\]", "", text)     # pi-4 P3: a variant bracket is not a word boundary
    rules = []
    for part in re.split(r" … ", v):
        for c in part.split():
            c = c.strip("“”‘’()")
            if not c:
                continue
            r = chunk_present(c, text) or chunk_present(c, bare) or chunk_present(c, nobr)
            if r is None:
                return False, [(c, None)]
            if r != "exact":
                rules.append((c, r))
    return True, rules
