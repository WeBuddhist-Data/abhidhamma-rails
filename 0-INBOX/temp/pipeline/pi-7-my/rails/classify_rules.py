"""INFLECTION / ARTEFACT rules of classify_misses.py (pi-7 Burmese rails; model pi-6-my/rails/classify_rules.py, read
only): (keyword regex, class, text-form regex that must match the segment, keyword-map forms (tuple) or None, reason,
Pāli check regex (a leading «!» = must NOT match) or None). The first matching rule classifies the row.
The Paṭṭhāna is formulaic (179,700 keyword uses): the rules are grammar patterns of one locked term each, built here
from the termbase itself (one rule per gerundive and per condition headword), checked on the segment text and its
Pāli:
  * GER: a gerundive «-tabba» whose termbase term is the attributive «…ရမည့်» stands in the text as the finite
    «…ရမည်» (the note's verb: «(evaṃ vitthāretabbaṃ)» «(ဤသို့ အကျယ် ချဲ့ရမည်)») or its negative «…ရမည် မဟုတ်»
    (na pahātabba, the triad terms). Text form: the term's verb + «ရမည်» not followed by «့».
  * COND: a condition word in «-paccayā» whose term is the ablative «Nဟူသော အကြောင်းကြောင့် (မဟုတ်)» stands in a heading
    (the hyphen chains «Hetu-ārammaṇapaccayā» = «Nဟူသော အကြောင်းနှင့် …») or in a note (as the subject / object /
    place: «yathā ārammaṇapaccayā» «… အကြောင်းကဲ့သို့», «Idha pana hetupaccayā» «… အကြောင်း၌») by its frame form, the
    bare name «Nဟူသော အကြောင်း» (na-: «… အကြောင်း မဟုတ်ခြင်း»), APPROVED.md key choice «condition forms» (the bare
    name N for bare stems / headings). Pāli check: the keyword in a heading or inside a «( … )» note.
  * the act compound «uposathakammaṃ katvā» «ဥပုသ်ကို စောင့်ထိန်း၍» (§A8: the compound carries its verb; katvā is its
    «၍»).
"""
import pathlib
import re
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
TB = HERE.parents[4] / "AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md"
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731


def _senses():
    out = []
    for l in open(TB, encoding="utf-8"):
        m = re.match(r"^(.*?): \{(.*)\}\s*$", N(l.rstrip("\n")))
        if not m:
            continue
        cur = ""
        for part in m.group(2).split("; "):
            cur = part if not cur else cur + "; " + part
            if ": " in cur:
                out.append((m.group(1), cur.rsplit(": ", 1)[1].strip()))
                cur = ""
    return out


OTHER = []
for _kw, _t in _senses():
    if _t.endswith("ရမည့်") and re.search(r"(?i)tabb", _kw):
        OTHER.append(("(?i)" + re.escape(_kw), "INFLECTION", re.escape(_t[:-len("ရမည့်")]) + "ရမည်(?!့)", None,
                      f"finite «{_t[:-1]}» / negative «{_t[:-1]} မဟုတ်» of the attributive termbase gerundive «{_t}» "
                      "(the note's verb or the na-X triad term; the loose test does not strip «ရမည်»)",
                      r"(?i)tabb"))
for _kw, _t in _senses():
    _m = re.fullmatch(r"(.+ဟူသော အကြောင်း)ကြောင့်( မဟုတ်)?", _t)
    if _m and re.search(r"(?i)paccayā$", _kw):
        form = re.escape(_m.group(1)) + (r" မဟုတ်ခြင်း" if _m.group(2) else r"(?!ကြောင့်)")
        OTHER.append(("(?i)" + re.escape(_kw), "INFLECTION", form, None,
                      f"frame form «{_m.group(1)}{' မဟုတ်ခြင်း' if _m.group(2) else ''}» (heading hyphen chain or note: "
                      f"subject / object / place) of the ablative termbase «{_t}» (APPROVED.md, condition forms: the "
                      "bare name for headings and bare stems)",
                      r"(?i)^#.*" + re.escape(_kw) + r"|\*[^*\n]*" + re.escape(_kw) + r"[^*\n]*\*|\([^()]*" + re.escape(_kw)
                      + r"[^()]*\)"))
OTHER.append((r"katvā", "ARTEFACT", r"ဥပုသ်ကို စောင့်ထိန်း၍", None,
              "the act compound «uposathakammaṃ katvā» «ဥပုသ်ကို စောင့်ထိန်း၍» (§A8 decided: the act compound carries its "
              "verb; katvā is its absolutive «၍», as dānaṃ datvā «… ပြု၍»); termbase doubt: katvā's gloss names "
              "uposathakammaṃ katvā", r"uposathakammaṃ katvā"))
STALE_SUBS = []      # no stale phrase entry
STALE_NO = set()
CONTEXT = []         # no context sense
