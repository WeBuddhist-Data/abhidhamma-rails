"""Book-wide alignments of the pi-3 Burmese keyword mapping (map-harmonise pass; reasons in map-harmonise-notes.md).

Imported by the three chapter scripts (map_ch3-6-8-9.py, map_ch7-10-11.py, map_ch12-15.py) and applied in their
lookup(): every value V that a script computes for keyword K in segment S (inner lookups of compose rules included)
goes through apply(K, S, V, pali, my). Nothing runs on import. The approved sample script map_all.py does not import
this module: the sample values (preamble, 1-uddeso, 2-pathamanayo) stay as approved.

The merged rule list of the three parallel agents (decision 3) is documented in map-harmonise-notes.md
(«One merged rule list»); this module holds only the rules that CHANGE a value:

R  The relative clause «ye dhammā vippayuttā» (ch7-10-11 M2; = pi-1 dhammā saṅkhatā «ပြုပြင်ဖန်တီးထားသော
   သဘောတရား»): where the Pāli segment has the adjacent «ye dhammā vippayuttā» and the text its relative clause
   «ကင်းကွာသော သဘောတရား», the biterm dhammā vippayuttā = «ကင်းကွာသော သဘောတရား» (the clause's Burmese order, its
   first occurrence). The subject + predicate frame «te dhammā … P» = «သဘောတရား … Pသော» (sample P1, ch3-6-8-9 M12)
   stays for dhammā saṅgahitā / asaṅgahitā, whose Pāli has no adjacent «ye dhammā P». Changes ch8 (11 uses).
V  Item + verb biterms «X-ena / X-ehi (ye dhammā) vippayuttā | sampayuttā» (ch3-6-8-9 M12 = ch7-10-11 M2 / M3 =
   ch12-15 Q2): the item's Burmese with the «နှင့်» the text attaches to it (an inner plural «များ» before «နှင့်»
   stays, pi-1 vitakkavicāravippayuttā «…တို့နှင့် ကင်းကွာသော»; the object keeps its «နှင့်», pi-1 rule 3), then
   « ကင်းကွာသော» where contiguous, « … ကင်းကွာသော» where other items stand between (pi-1 rule 10); where the text
   attaches no «နှင့်» to the item's Burmese (Kusalehi: «ကုသိုလ် သဘောတရားများနှင့်»), «X … ကင်းကွာသော». The first
   occurrence decides (one sense per segment): dhammehi vippayuttā = the item «X-ehi dhammehi ye dhammā vippayuttā»
   «…သဘောတရားများနှင့် ကင်းကွာသော» (ch11 and ch15 alike; not the later «tehi dhammehi …» «ထိုသဘောတရားတို့နှင့်»).
   Changes ch11: dhammehi vippayuttā (38), bhavena vippayuttā (2), viññāṇena vippayuttā (1).
S  sukha, one sense per segment by the compound the FRAGMENT belongs to (sample f_sukha, pi-1 harmonise decision
   3): where the keyword list has sukhāya / Sukhāya (vedanāya) as a keyword of its own, that word does not decide
   the fragment's sense; the fragment is the member of sukhasahagata «သာယာမှုနှင့်အတူ ဖြစ်သော» = «သာယာမှု», as the
   same long dyad-list segments 3-227, 3-447, 3-455 and the sample's 3-91 (sukhasahagatā). Changes ch6 3-210, ch13
   3-437, ch14 3-451 (3 uses).
"""
import re

NONE = "(no direct equivalent)"
VERB = {"vippayuttā": "ကင်းကွာသော", "sampayuttā": "ယှဉ်တွဲသော"}
ITEM = re.compile(r"^(\S+?(?:ena|ehi|āya|iyā|uyā|ūhi|īhi))\s+(vippayuttā|sampayuttā)$")


def low(w):
    return w[:1].lower() + w[1:]


def rule_R(kw, sid, v, pali, my):
    if low(kw) == "dhammā vippayuttā" and re.search(r"\bye dhammā vippayuttā\b", pali) \
            and "ကင်းကွာသော သဘောတရား" in my:
        return "ကင်းကွာသော သဘောတရား"
    return v


def rule_V(kw, sid, v, pali, my):
    m = ITEM.match(low(kw))
    if not m or v == NONE:
        return v
    pred = VERB[m.group(2)]
    if not (v.endswith(" " + pred) or v.endswith(" … " + pred)):
        return v
    item = v[: -len(pred)].rstrip(" …")
    for suf in ("များနှင့်", "နှင့်"):
        if item.endswith(suf):
            item = item[: -len(suf)]
            break
    for suf in ("နှင့်", "များနှင့်"):                       # contiguous first
        if f"{item}{suf} {pred}" in my:
            return f"{item}{suf} {pred}"
    for suf in ("နှင့်", "များနှင့်"):
        if f"{item}{suf}" in my:
            return f"{item}{suf} … {pred}"
    return f"{item} … {pred}"


def rule_S(kw, sid, v, pali, my):
    if kw == "sukha" and v == "သာယာသော" and re.search(r"sukhasahagat", pali, flags=re.I) \
            and "သာယာမှုနှင့်" in my:
        return "သာယာမှု"
    return v


RULES = (rule_R, rule_V, rule_S)


def apply(kw, sid, v, pali, my):
    """-> the aligned value of keyword kw in segment sid (v unchanged when no rule applies)."""
    for r in RULES:
        v = r(kw, sid, v, pali, my)
    return v


# reasons for the map-table «differs from pi-1 / pi-2» rows of the values these rules produce
REASONS = {
    "dhammā vippayuttā": "map-harmonise R: the relative clause «ye dhammā vippayuttā» «ကင်းကွာသော သဘောတရား» (pi-1 "
                         "dhammā saṅkhatā order); the frame «te dhammā … vippayuttā» is not the adjacent biterm",
    "dhammehi vippayuttā": "map-harmonise V: the item «X-ehi dhammehi ye dhammā vippayuttā» «…သဘောတရားများနှင့် "
                           "ကင်းကွာသော» (inner plural stays, pi-1 vitakkavicāravippayuttā)",
}

TABLE_NOTE = """
## map-harmonise (book-wide alignments, harmonise_rules.py)

This script's lookup() passes every value through `harmonise_rules.apply()` (rules R, V, S in that module, reasons in
`map-harmonise-notes.md`): R the relative clause «ye dhammā vippayuttā» = «ကင်းကွာသော သဘောတရား»; V item + verb
biterms «X-ena / X-ehi vippayuttā» = «Xနှင့် (…) ကင်းကွာသော» as the text attaches «နှင့်» (inner «များ» stays);
S the sukha fragment of sukhasahagata = «သာယာမှု» where sukhāya is a keyword of its own. The presence check is the
ONE shared `presence_check.py`.
"""
