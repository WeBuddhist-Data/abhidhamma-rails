"""The ONE presence check of the pi-3 Burmese keyword mapping (map-harmonise decision 3).

Imported by the four mapping scripts (map_all.py, map_ch3-6-8-9.py, map_ch7-10-11.py, map_ch12-15.py); defines
nothing else and runs nothing on import. Before the map-harmonise pass each script carried its own copy; the four
copies were byte-identical (the parallel agents added no ending), so this module is that copy, unchanged.

A value passes when every chunk of it occurs in the segment's Burmese, literally or by one of the ending rules
below. The lists are pi-2's merged list (pi-2 presence_check.py) plus the three pi-3 sample endings (M7); every
entry names its origin. The documented list of presence-check endings for all pi-3 scripts:

ATTR_FROM: a chunk «Xသော» is accepted when the text has X + one of
  pi-1 / pi-2 sample N11 : သော် ၍ ပြီး သည် ခြင်း သူ ပြီ ကြသော ဘဲ သေးသော ၊ သည့်
  pi-2 12-14 M1          : လျက် ကုန်သော ကြသည် ၏ ကြ၏ ။ ”     (predicate / plural / quoted forms)
  pi-2 15-16 P1          : ကြ ဟူ ဟု                        (plural predicate «Xကြ(သည်)», quoted «Xဟု»)
  pi-2 17                : ကုန်
  pi-3 sample M7         : သနည်း ရာ သေးသည်                  (question «…သနည်း», «where» clause «…ရာ», «မသိရသေးသည်»)
VERB_FROM: a chunk «Xသည်» is accepted when the text has X + one of
  pi-1                   : ပါ၏ ၏ ပြီ သော ၍ ပြီး ခြင်း ရန် သည့် ကြ ၊ ဟူ လိမ့်မည် ။
  pi-2 12-14 M1          : ရာ ” သနည်း                       (verb of a «where …» clause, quoted, question)
  pi-2 15-16 P5, P6      : လျှင်                             (the condition «Xလျှင်»)
  pi-2 17 (N12)          : ပါစေ သမျှ ဟု ကုန် အံ့ လော့ မည်       (optative, imperative, future, quoted)
Further rules (pi-2, unchanged):
  attr-fut   «Xည့်» against the text's «Xည်»
  perf-pred  «Xပြီးသော» against the predicate «Xပြီး ဖြစ်…»
  neg-verb   «Xသည်» against the text's negated verb «မX» / infixed «…မ…» + a VERB_FROM ending (the positive verb is
             the value, pi-1 rule 8: labbhare / labbhati «မတွေ့ရ(ကြ)»)
  plural     «Xလိမ့်မည်» / «Xခဲ့သည်» against «Xကြလိမ့်မည်» / «Xခဲ့ကြ…»
  neg-infix, neg-attr (pi-1 rule 8) the positive part of a negated word (anaññāta, anuppanna, appaṭigha …)
  quotes     the text's quotation marks “ ” ‘ ’ are not a word boundary (a chunk is also matched against the text
             with them removed)
"""
import re

NONE = "(no direct equivalent)"

ATTR_FROM = tuple(dict.fromkeys((
    "သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ကြသော", "ဘဲ", "သေးသော", "၊", "သည့်",   # pi-1 / sample N11
    "လျက်", "ကုန်သော", "ကြသည်", "၏", "ကြ၏", "။", "”",                                    # pi-2 12-14 M1
    "ကြ", "ဟူ", "ဟု",                                                                   # pi-2 15-16 P1
    "ကုန်",                                                                             # pi-2 17
    "သနည်း", "ရာ", "သေးသည်",                                                          # pi-3 N-b
)))
VERB_FROM = tuple(dict.fromkeys((
    "ပါ၏", "၏", "ပြီ", "သော", "၍", "ပြီး", "ခြင်း", "ရန်", "သည့်", "ကြ", "၊", "ဟူ", "လိမ့်မည်", "။",  # pi-1
    "ရာ", "”", "သနည်း",                                                                  # pi-2 12-14 M1
    "လျှင်",                                                                            # pi-2 15-16 P5 / P6
    "ပါစေ", "သမျှ", "ဟု", "ကုန်", "အံ့", "လော့", "မည်",                                     # pi-2 17
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

