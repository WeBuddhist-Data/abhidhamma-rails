"""Burmese zero-shot of pi-3 (Dhātukathā, «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»), chapters 12-15
(Ekādasama … Cuddasama naya).

usage: python3 -I -X utf8 make_ch12-15.py [chapter ...]
Every line is generated from the Pāli by my3_formulas.translate_line() (imported, never edited); this file only ADDS
to its tables in memory (HEAD, FIXED) and adds the frames of methods 11-14 to F.EXTRA_RULES. A sentence no frame or
table entry matches stops the run (F.Miss), nothing is guessed. A chapter is written only when every line passed; on a
stop the lines that passed go to scratch/partial-<chapter> and the failing line is printed.
This file never writes my3-zeroshot-terms.md (new strings are logged in notes-ch12-15.md).
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my3_formulas as F  # noqa: E402

F.install()          # the book-wide values of the consistency pass (harmonise-notes.md)

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-3_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["12-ekadasamanayo.md", "13-dvadasamanayo.md", "14-terasamanayo.md", "15-cuddasamanayo.md"]

C, END, PE, DH, DHP, CL = F.C, F.END, F.PE, F.DH, F.DHP, F.CL
NUM_MY = dict(F.NUM_MY)          # with the verse numbers 30, 43, 47 (my3_formulas.install())

# ===================================================================================== new words (logged in notes)
WITH = F.WITH                                    # instrumental «X-ena» with saṅgahita / sampayutta = «Xနှင့်»
TE = f"{F.TE}{F.SUBJ_MARK}"                      # te dhammā = «ထိုသဘောတရားများသည်» (pi-1 ime dhammā «ဤသဘောတရားများ»)
F.witness("1", "^1-57", "ime dhammā kusalā", f"ဤ{DHP}သည်")
KEHICI = "အချို့"                                # kehici (partly: «… တို့၏ အချို့နှင့်»)
NATTHI = F.NATTHI                                # «Natthi.» (answer: none)
GEN, GEN_PL = "၏", "တို့၏"
assert f"{GEN} {KEHICI}" == F.SOME
WITH_PL = "တို့" + WITH
Q_ASSOC = F.Q1_MY[:-len(F.IN_PL)] + WITH_PL       # «… ဓာတ် မည်မျှတို့နှင့်»
assert F.Q1_MY.endswith(F.IN_PL)
SANGAHA_N = F.NOUN_W["saṅgaho"]                  # «အကျုံးဝင်ခြင်း»
REL_KIND = {"k": F.KHANDHA, "a": F.AYATANA, "d": F.DHATU}   # khandha- / āyatana- / dhātusaṅgahena

# verbs of these methods (subject always plural: te dhammā / ye dhammā)
V_ST = {"saṅgahitā": F.VERB[True]["st"]["pl"], "asaṅgahitā": F.VERB[False]["st"]["pl"],
        "sampayuttā": F.SAMPAYUTTA_V + "ကြသည်", "vippayuttā": F.VIPPAYUTTA_V + "ကြသည်"}
V_Q = {"saṅgahitā": F.VERB[True]["q"]["pl"], "asaṅgahitā": F.VERB[False]["q"]["pl"],
       "sampayuttā": F.SAMPAYUTTA_V + "ကြသနည်း", "vippayuttā": F.VIPPAYUTTA_V + "ကြသနည်း"}
V_REL = {"sampayuttā": F.SAMPAYUTTA_V + "သော", "vippayuttā": F.VIPPAYUTTA_V + "သော"}
assert F.P1.SAMP == WITH + " " + V_REL["sampayuttā"] and F.P1.VIPP == WITH + " " + V_REL["vippayuttā"]

# ===================================================================================== headings, fixed lines
# Khandhādi, Saccādi, Phassādisattakaṃ and the book colophon (pi-1 ^1-1616, pi-2 ^2-1044 pattern):
# my3_formulas.install() (consistency pass, B6)
assert F.HEAD["Khandhādi"] == f"{F.KHANDHA} စသည်" and F.HEAD["Paṭiccasamuppādādi"].endswith(" စသည်")

MAHANTARA = F.heads("1", "Mahantaradukaṃ")      # «ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး» (verse name, for the reuse test)
PITTHI = F.heads("1", "Piṭṭhidukaṃ")            # «နောက်ဆုံး နှစ်မျိုးတွဲများ»
VERSES = F.VERSES      # every summary verse of the book: my3_formulas.install() (consistency pass, B5)

# ===================================================================================== instrumental items -> topic
INSTR_ITEM = {   # irregular «X-ena / X-ehi» items -> nominative subject key (as in 2-pathamanayo)
    "pañcahi indriyehi": "pañcindriyāni", "pañcahi balehi": "pañca balāni", "sattahi bojjhaṅgehi": "satta bojjhaṅgā",
    "ariyena aṭṭhaṅgikena maggena": "ariyo aṭṭhaṅgiko maggo", "upādādhammehi": "upādā dhammā",
    "vipākadhammadhammehi": "vipākadhammadhammā",
    "nevavipākanavipākadhammadhammehi": "nevavipākanavipākadhammadhammā",
    "na hetusahetukehi dhammehi": "na hetū sahetukā dhammā",      # pi-3 writes «hetusahetuka» as one word
    "na hetuahetukehi dhammehi": "na hetū ahetukā dhammā",
}


# ^3-453 «āsavavippayuttehi ceva no ca āsavehi» (only here; pi-1 has «āsavasampayuttā ceva no ca āsavā»): source slip,
# translated as written, built from the pi-1 term with «ယှဉ်တွဲ» -> «ကင်းကွာ» (new)
_ASP = F.subject("āsavasampayuttā ceva no ca āsavā dhammā")[0]
assert _ASP.count(F.SAMPAYUTTA_V) == 1
NEW_SUBJ = {"āsavavippayuttā ceva no ca āsavā dhammā": _ASP.replace(F.SAMPAYUTTA_V, F.VIPPAYUTTA_V)}
for _k, _v in NEW_SUBJ.items():
    F.SUBJ[_k] = (_v, "pl")


def _word_nom(w):
    """one word of a «… dhammehi» item -> nominative plural."""
    if w in ("ceva", "ca", "na", "no", "neva", "sukhāya", "dukkhāya", "adukkhamasukhāya", "vedanāya", "dassanena",
             "bhāvanāya"):
        return w
    if w == "hetūhi":
        return "hetū"
    if w.endswith("bhūhi"):
        return w[:-4] + "huno"           # cittasahabhūhi -> cittasahabhuno
    if w.endswith("īhi"):
        return w[:-3] + "ino"            # ācayagāmīhi -> ācayagāmino, rūpīhi -> rūpino
    if w.endswith("āhi"):
        return w[:-2]                    # bahiddhāhi -> bahiddhā
    if w.endswith("ehi"):
        return w[:-3] + "ā"
    raise F.Miss("item word: " + w)


def item_nom(x):
    """«Samudayasaccena» / «hetūhi ceva sahetukehi ca dhammehi» -> the nominative subject key."""
    k = x[0].lower() + x[1:]
    if k in INSTR_ITEM:
        return INSTR_ITEM[k]
    if k.endswith(" dhammehi"):
        return " ".join(_word_nom(w) for w in k[:-len(" dhammehi")].split()) + " dhammā"
    ws = k.split()
    last = ws[-1]
    cands = []
    for suf, reps in (("ena", ("o", "aṃ")), ("āya", ("ā",)), ("iyā", ("i",)), ("uyā", ("u",)), ("ehi", ("ā",))):
        if last.endswith(suf):
            cands += [" ".join(ws[:-1] + [last[:-len(suf)] + r]) for r in reps]
    hits = [c for c in cands if c in F.SUBJ]
    if len(hits) != 1:
        raise F.Miss(f"item {x}: {cands}")
    return hits[0]


def item_my(x):
    return F.subject_my(item_nom(x))[0]


# ===================================================================================== frames of methods 11-14
VERBS = "saṅgahitā|asaṅgahitā|sampayuttā|vippayuttā"
REL_SG = (r"khandhasaṅgahena (?P<n1>a?)saṅgahitā āyatanasaṅgahena (?P<n2>a?)saṅgahitā "
          r"dhātusaṅg(?P<ok>ah)?ena (?P<n3>a?)saṅgahitā")        # ^3-454 «dhātusaṅgena» (slip)
REL_RE = rf"(?:{REL_SG}|(?P<sv>sampayuttā|vippayuttā))"
CHAIN_RE = re.compile(rf"(?P<head>.+) ye(?P<dh> dhammā)? (?P<rel>{REL_RE})(?P<conn>…pe…, |…, |…pe… |… |, | )"
                      rf"te dhammā (?P<rest>.+)")
ITEM_SEP = re.compile(r" ye dhammā ?(?:…pe…|…) ?")
Q_RE = re.compile(rf"{F.Q1_P} (?P<v>{VERBS})(?:ti)?\?")
PART_RE = re.compile(rf"(?P<thap>{re.escape(F.THAP_P)} )?(?P<c>{F.COUNTS_RE.pattern}) (?P<keh>kehici )?(?P<v>{VERBS})",
                     re.IGNORECASE)
CONN_MY = {"…pe…, ": PE + C + " ", "…, ": PE + C + " ", "…pe… ": PE + " ", "… ": PE + " ", ", ": C + " ",
           " ": " "}              # « te dhammā» without a mark (^3-413): as written, no «၊» added (A1, as ^3-225)


def rel_my(m):
    if m["sv"]:
        return f"{V_REL[m['sv']]} {DHP}"
    neg = {m["n1"], m["n2"], m["n3"]}
    if len(neg) != 1:
        raise F.Miss("mixed relative polarity")
    v = F.ASANGAHA_V if neg == {"a"} else F.SANGAHA_V
    return f"{C} ".join(f"{REL_KIND[k]} {SANGAHA_N}ဖြင့် {v}" for k in "kad") + f"သော {DHP}"


def assoc_my(cs, verb, keh):
    if any(n == 0 for _, n in cs):
        raise F.Miss("zero count with sampayutta / vippayutta")
    lst = f"{C} ".join(F.count_my(k, n) for k, n in cs)
    single = len(cs) == 1 and cs[0][1] == 1
    if keh:
        post = (GEN if single else GEN_PL) + f" {KEHICI}{WITH}"
    else:
        post = WITH if single else WITH_PL
    return f"{lst}{post} {V_ST[verb]}"


def answer_my(a):
    """«[asaṅkhataṃ khandhato ṭhapetvā] COUNTS [kehici] VERB; … .» -> Burmese (subject plural)."""
    if not a.endswith("."):
        raise F.Miss("answer end: " + a)
    out = []
    for part in a[:-1].split("; "):
        m = PART_RE.fullmatch(part)
        if not m:
            raise F.Miss("answer part: " + part)
        cs = F.counts_parse(m["c"])
        v = m["v"].lower()
        pre = F.THAPETVA + " " if m["thap"] else ""
        if v in ("saṅgahitā", "asaṅgahitā"):
            if m["keh"]:
                raise F.Miss("kehici with saṅgahita")
            out.append(pre + F.counts_my(cs, v == "saṅgahitā", "pl"))
        else:
            out.append(pre + assoc_my(cs, v, bool(m["keh"])))
    return f"{C} ".join(out) + END


def question_my(v):
    return f"{F.Q1_MY if v in ('saṅgahitā', 'asaṅgahitā') else Q_ASSOC} {V_Q[v]}{END}"


def rest_my(r):
    m = Q_RE.fullmatch(r)
    if m:
        if m["v"] not in ("saṅgahitā", "sampayuttā"):
            raise F.Miss("question polarity: " + r)
        return question_my(m["v"])
    return answer_my(r)


def chain_rule(m):
    items = ITEM_SEP.split(m["head"])
    seps = ITEM_SEP.findall(m["head"])
    if len(items) != len(seps) + 1:
        raise F.Miss("chain: " + m["head"])
    my = [F.chain_item_my(item_my(x)) for x in items]
    head = my[0]
    for x in my[1:]:
        head += PE + " " + x
    return f"{head} {rel_my(m)}{CONN_MY[m['conn']]}{TE} {rest_my(m['rest'])}"


def te_rule(m):
    return f"{TE} {answer_my(m['a'])}"


def katihi_rule(m):
    v = m["v"]
    if v in ("saṅgahitā", "sampayuttā"):
        raise F.Miss("katihi polarity")
    return (f"{F.KATI}{F.IN_PL} " if v == "asaṅgahitā" else f"{F.KATI}{WITH_PL} ") + V_Q[v] + END


def bare_rule(m):
    if not F.COUNTS_RE.match(m[0]):
        return None
    return answer_my(m[0])


F.EXTRA_RULES += [
    (CHAIN_RE, chain_rule),
    (re.compile(r"Te dhammā (?P<a>.+\.)"), te_rule),
    (re.compile(rf"Katihi (?P<v>{VERBS})\?"), katihi_rule),
    (re.compile(r"Natthi[.?]"), lambda m: NATTHI + END),       # ^3-450 «Natthi?» (slip): the same answer
    (re.compile(r".+\."), bare_rule),
]


# ===================================================================================== generator (as make_sample.py)
def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def bids(lines):
    bid_of, cur = {}, []
    for i, line in enumerate(lines):          # block ID of each line = the ID that closes its segment
        if line.strip():
            cur.append(i)
            m = F.ID_RE.search(line)
            if m:
                for j in cur:
                    bid_of[j] = m.group(1)
                cur = []
    return bid_of


def render(name):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    bid_of = bids(lines)
    return [F.translate_line(line, bid_of.get(i)) for i, line in enumerate(lines)]


def chapter(name):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    bid_of = bids(lines)
    done = []
    for i, line in enumerate(lines):
        try:
            done.append(F.translate_line(line, bid_of.get(i)))
        except F.Miss as e:
            part = HERE / "scratch" / ("partial-" + name)
            part.parent.mkdir(exist_ok=True)
            part.write_text("\n".join(done) + "\n", encoding="utf-8")
            print(f"STOP {name} line {i + 1}: {e}\n  {line[:200]}\n  ({len(done)} lines kept in {part})")
            return False
    write(name, "\n".join(done).rstrip("\n") + "\n")
    return True


if __name__ == "__main__":
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES_OUT
    for n in names:
        if n not in NAMES_OUT:
            raise SystemExit(f"not my chapter: {n}")
    OUT.mkdir(parents=True, exist_ok=True)
    ok = True
    for n in names:
        ok = chapter(n) and ok
    sys.exit(0 if ok else 1)
