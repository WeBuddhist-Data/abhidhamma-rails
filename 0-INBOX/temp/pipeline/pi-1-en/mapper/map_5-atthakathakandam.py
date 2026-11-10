"""English->Pali keyword map for pi-1 chapter `5-atthakathakandam` (Atthakathakandam).

usage: python -I -X utf8 map_5-atthakathakandam.py [--dump [bid ...]]
Writes 5-atthakathakandam.mapped.md next to the keywords file.

Conventions: map-conventions.md (incl. section 8: no non-word compound fragments).
How a value is found:
  1. EXPLICIT[bid][keyword.lower()] (matrix-item phrases and one-off fragments), else
  2. the generic table G: every spec is a regex over THAT segment's Pali (variant brackets,
     labels and heading marks removed); each hit gives a value taken letter for letter from the
     text (a few sandhi members are written in their own form, see map-conventions 1.4).
     The hit of the lowest tier wins; inside it the FIRST hit (Pali order) per lemma; different
     lemmas are joined with " / " (map-conventions 4). Tier 1 = implicit renderings (e.g. "mind"
     in "the wholesome mind" = kusalam), used only when no explicit word is present.
     A table entry with NDE_OK falls back to "(no direct equivalent)" when nothing is found.
Because values are computed from the Pali text, identical Pali segments get identical values.
Values never contain ", " (commas inside a stretch are dropped) and enclitic -ti/-pi of
"...tipi" quotations is dropped where it does not change letters.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
CH = "5-atthakathakandam"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / f"{CH}.md"
NDE = "(no direct equivalent)"
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")
SEP = " ,.?;:–…"


def segments():
    segs, buf = {}, []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        mm = ID.search(line)
        buf.append(line[:mm.start()] if mm else line)
        if mm:
            t = " ".join(buf)
            t = re.sub(r"\s*\[[^\]]*\]", "", t)
            t = re.sub(r"\((Ka|Kha|Ga)\)", " ", t)
            t = re.sub(r"^#+\s*|\s#+\s", " ", t)
            segs[mm.group(1)] = re.sub(r"\s+", " ", t).strip()
            buf = []
    return segs


# ------------------------------------------------------------------ value normalisation
def strip_encl(w):
    if w.endswith("tipi") and len(w) > 5:
        w = w[:-2]
    if w.endswith("ti") and len(w) > 4 and w[-3] in "āo":
        w = w[:-2]
    return w


def norm(v):
    for ch in "–,;?":
        v = v.replace(ch, " ")
    ws = [strip_encl(w) for w in v.split()]
    while len(ws) > 1 and ws[-1] in ("ca", "cā"):
        ws.pop()
    return " ".join(ws)


def word_at(text, i):
    a = i
    while a > 0 and text[a - 1] not in SEP:
        a -= 1
    b = i
    while b < len(text) and text[b] not in SEP:
        b += 1
    return text[a:b]


class R:
    """regex spec. val: None (named group v or whole match), str, or callable(match)."""

    def __init__(self, pat, val=None, lemma=None, tier=0, excl=None):
        self.rx = re.compile(pat)
        self.val, self.lemma, self.tier = val, lemma, tier
        self.excl = re.compile(excl) if excl else None

    def hits(self, text):
        for m in self.rx.finditer(text):
            if self.excl and self.excl.fullmatch(word_at(text, m.start())):
                continue
            if callable(self.val):
                v = self.val(m)
            elif isinstance(self.val, str):
                v = self.val
            elif "v" in self.rx.groupindex:
                v = m.group("v")
            else:
                v = m.group(0)
            yield self.tier, m.start(), self.lemma, norm(v)


def lem(root, endings, stem="a", lemma=None, tier=0, excl=None):
    """A compound member / word with root `root`: whole ending kept when the word ends there
    (enclitic -ti/-pi aside), otherwise the stem (root + stem)."""
    pat = rf"(?P<r>{root})(?P<e>{'|'.join(endings)})(?P<t>\w*)"

    def val(m):
        t = m.group("t")
        if t in ("", "tipi", "ti", "pi"):
            return m.group("r") + m.group("e")
        if t in ("nti", "ntipi"):
            return m.group("r") + m.group("e") + "nti"
        return m.group("r") + stem
    return R(pat, val, lemma, tier, excl)


def aval(m):
    """sandhi: a member whose initial a- is fused with a preceding vowel (kiriyābyākatam)."""
    s = m.group(0)
    return "a" + s[1:] if s[0] in "āa" else s


NDE_OK = "NDE_OK"


# ------------------------------------------------------------------ kusala / akusala finder
class Kusal:
    """sel(neg, ending, tail, pre) -> bool ; value: (a)kusal+ending, or (a)kusala as a member."""

    def __init__(self, sel, tier=0, lemma=None, member=None):
        self.sel, self.tier, self.lemma, self.member = sel, tier, lemma, member

    def hits(self, text):
        for m in re.finditer(r"kusal", text):
            s = m.start()
            a = s
            while a > 0 and text[a - 1] not in SEP:
                a -= 1
            b = m.end()
            while b < len(text) and text[b] not in SEP:
                b += 1
            pre, rest = text[a:s], text[m.end():b]
            neg = pre in ("a", "A") or pre.endswith("ā")
            for e in ("esu", "assa", "ato", "aṃ", "ā", "a"):
                if rest.startswith(e):
                    break
            else:
                e = ""
            tail = rest[len(e):]
            if not self.sel(neg, e, tail, pre):
                continue
            if tail in ("", "tipi", "ti", "pi"):
                core = "kusal" + e
            elif self.member:
                core = self.member(e, tail)
            else:
                core = "kusala"
            yield self.tier, s, self.lemma, ("a" if neg else "") + core


def kmember(e, tail):
    if tail.startswith("citt"):
        return "kusalacitta"
    return "kusala"


POS_ANY = Kusal(lambda n, e, t, p: not n)
NEG_ANY = Kusal(lambda n, e, t, p: n)
# "the wholesome mind": kusalam (any), kamavacarakusalato / -kusalassa (compound)
POS_MIND = Kusal(lambda n, e, t, p: not n and t == "" and
                 (e == "aṃ" or (e in ("ato", "assa") and p.lower().endswith("kāmāvacara"))))
NEG_MIND = Kusal(lambda n, e, t, p: n and ((t == "" and e in ("aṃ", "ato", "assa")) or t.startswith("citt")),
                 member=kmember)
POS_MINDS = Kusal(lambda n, e, t, p: not n and e == "esu")
NEG_MINDS = Kusal(lambda n, e, t, p: n and e == "esu")

# tier-1 (implicit) sources of "mind"
KIRIYATO = r"(?<!kusalato ca vipākato ca )(?<!kusalato ca )(?<!vipākato ca )kiriyato|(?<=kusalassa vipākato ca )kiriyato"
MIND_IMPLICIT = [
    Kusal(lambda n, e, t, p: t == "" and (e in ("aṃ", "esu", "assa") or (e == "ato" and (n or p.lower().endswith("kāmāvacara")))),
          tier=1, lemma="impl"),
    R(r"kiriyābyākataṃ", None, "impl", 1),
    R(KIRIYATO, None, "impl", 1),
    R(r"kiriyesu", None, "impl", 1),
]

# ------------------------------------------------------------------ generic table
G = {}


def g(kw, *specs):
    G[kw] = list(specs)


SAHA = r"(?:esu|aṃ|ā|o|a)"
g("planes", R(r"bhūmīsu"))
g("except", R(r"[Ṭṭ]hapetvā"))
g("sometimes", R(r"(?<!\w)siyā(?!\w)"))
g("counted", R(r"vattabb(?:ā|o|aṃ)"))
g("counted among states", R(r"vattabb(?:ā|o|aṃ) (?:– )?(?:\S+ ){0,3}?\S+?(?:tipi|ti)(?=[\s,.;–]|$)"))
g("described", R(r"vattabbaṃ"))
g("remaining", R(r"avases(?:aṃ|añca)"))
g("remaining unwholesome", R(r"avasesaṃ akusalaṃ"))
g("remaining unwholesome mind", R(r"avasesaṃ akusalaṃ"))
g("remaining material", R(r"avasesañca rūpaṃ"))
g("remaining material form", R(r"avasesañca rūpaṃ"))
g("every", R(r"sabbaṃ(?= akusalaṃ)"))
g("whatever", R(r"(?<!\w)(?:yañca|yaṃ)(?!\w)"))
g("due to past", R(r"kammassa katattā"))
g("past action", R(r"kammassa", lemma="kamma"))
g("arisen", R(r"uppann(?:aṃ|e|o|ā|a)"))
g("arise", R(r"uppajjanti|uppādino"))
g("arises", R(r"uppajjati"))
g("arisings", R(r"(?<=citt)uppād(?:esu|ā|e)(?!\w)"))
g("arising", R(r"(?<=citt)uppādo(?!\w)", lemma="uppada"), lem(r"samuṭṭhān", ["aṃ", "ā", "a"], lemma="samutthana"))
g("arisings of mind", R(r"cittuppād(?:esu|ā|e)(?!\w)"))
g("arising of mind", R(r"cittuppādo"))
g("mind accompanied", R(r"sahagat(?:a|esu |o )citt", lambda m: m.group(0) + "a"))
g("mind dissociated", R(r"vippayutt(?:a|e |esu )citt", lambda m: m.group(0) + "a"))
g("mind without roots", R(r"ahetuke citt", lambda m: m.group(0) + "a"))
g("accompanied", R(r"sahagat" + SAHA))
for kw, x in [("doubt", "[Vv]icikicchā"), ("equanimity", "[Uu]pekkhā"), ("greed", "lobha"), ("happiness", "sukha"),
              ("joy", "somanassa"), ("rapture", "pīti"), ("restlessness", "[Uu]ddhacca"), ("sadness", "domanassa")]:
    g("accompanied by " + kw, R(rf"(?<!\w)(?:dukkha)?{x}sahagat{SAHA}" if kw == "happiness" else rf"{x}sahagat{SAHA}"))
G["accompanied by happiness"] = [R(r"(?<!\w)sukhasahagat" + SAHA)]
g("doubt", R(r"[Vv]icikicchā"))
g("restlessness", R(r"[Uu]ddhacc(?:añca|aṃ|a)"))
g("joy", R(r"somanassa"))
g("sadness", R(r"domanassa"))
g("greed", R(r"[Ll]obh(?:o|aṃ|a)", excl=r"[Aa]lobho"))
g("delusion", R(r"[Mm]oh(?:o|aṃ)", excl=r"[Aa]moho"))
g("hate", R(r"[Dd]oso", excl=r"[Aa]doso"))
g("equanimity", R(r"[Uu]pekkh(?:aṃ|ā)"))
g("rapture", R(r"[Pp]īti(?:kā|ṃ)?"))
g("happiness", R(r"(?<![\wā])[Ss]ukh(?:añca|aṃ(?! vedanaṃ)|a(?=sahagat))"))
g("pleasant", R(r"(?<!\w)sukhāya|(?<!\w)sukhaṃ(?= vedanaṃ)"), R(r"adukkhamasukh(?:āya|aṃ)"))
g("painful", R(r"(?<!\w)dukkhāya|(?<!\w)dukkhaṃ(?= vedanaṃ)"), R(r"adukkhamasukh(?:āya|aṃ)"))
g("pleasant feeling", R(r"(?<!\w)sukhāya vedanāya|(?<!\w)sukhaṃ vedanaṃ"))
g("painful feeling", R(r"(?<!\w)dukkhāya vedanāya|(?<!\w)dukkhaṃ vedanaṃ"))
g("painful nor pleasant", R(r"adukkhamasukh(?:āya|aṃ)"))
g("feeling", R(r"[Vv]edan(?:āya|aṃ|ā)"))
g("feelings", R(r"(?<=Tisso ca )vedanā"))
g("pain", R(r"dukkha(?=sahagat)"))
g("body-consciousness", R(r"kāyaviññāṇaṃ"))
g("eye-consciousness", R(r"[Cc]akkhuviññāṇaṃ"))
g("ear-consciousness", R(r"sotaviññāṇaṃ"))
g("nose-consciousness", R(r"ghānaviññāṇaṃ"))
g("tongue-consciousness", R(r"jivhāviññāṇaṃ"))
g("consciousness", R(r"(?<=pañca)viññāṇāni"), R(r"[Vv]iññāṇañcāyatanaṃ"))
g("kinds", R(r"pañcaviññāṇāni", lemma="vinnana"), lem(r"[Uu]pādān", ["āni", "ā", "e"], lemma="upadana"))
g("sense", R(r"([Kk])āmāvacar", lambda m: m.group(1) + "āma"), R(r"pañcaviññāṇāni", tier=1))
g("sensual", R(r"(?<!\w)([Kk])ām(?!āvacar)", lambda m: m.group(1) + "āma"))
g("sense sphere", R(r"[Kk]āmāvacar(?:assa|aṃ|ā|a)"))
g("sphere", R(r"āvacar(?:assa|aṃ|ā|a)", aval))
g("fine-material", R(r"(?<![Aa])([Rr])ūpāvacar", lambda m: m.group(1) + "ūpa"))
g("fine-material sphere", R(r"(?<![Aa])[Rr]ūpāvacar(?:aṃ|ā|a)"))
g("immaterial", R(r"(?<!\w)([Aa])rūpāvacar", lambda m: m.group(1) + "rūpa", "arupa"), R(r"āruppā", lemma="arupa"),
  R(r"arūpino", lemma="arupa"))
g("immaterial sphere", R(r"(?<!\w)[Aa]rūpāvacar(?:ā|a)"))
g("immaterial attainments", R(r"āruppā"))
g("attainments", R(r"āruppā"))
g("world-transcending", R(r"lokuttar(?:aṃ|a)"))
g("world-transcending absorption", R(r"lokuttaraṃ \w+ jhānaṃ|lokuttarapañcakanaye dutiyaṃ jhānaṃ|lokuttaraekakadukajjhānā"))
g("world-transcending absorptions", R(r"lokuttara(?:tika|duka)(?:catukka|tika|duka)jjhānā"))
g("absorption", R(r"jhān(?:aṃ|e|assa)(?!\w)"), R(r"(?<=ekakadu)kajjhānā", "jhānā"))
g("absorptions", R(r"(?<!ekaka)(?:tika|duka|catukka|pañcaka)jjhānā", "jhānā"))
g("fourth absorption", R(r"catutth(?:aṃ jhānaṃ|assa jhānassa)"))
g("fivefold", R(r"pañcaka(?=naye)"), NDE_OK)
g("fivefold method", R(r"pañcakanaye"), NDE_OK)
g("method", R(r"(?<=pañcaka)naye"), NDE_OK)
g("fourfold", NDE_OK)
g("fourfold method", NDE_OK)
g("resultant", R(r"(?<=kusalato ca )vipākato"), R(r"vipāka(?=hetu)"))
g("resultant and functional", R(r"(?<=kusalato ca )vipākato ca kiriyato"))
g("wholesome and resultant", R(r"kusalato ca vipākato"))
g("functional", R(r"kiriy(?:ato|esu|ā|a)"))
g("functional mind", R(r"kiriyābyākataṃ"), R(KIRIYATO), R(r"kiriyāmano"))
g("functional minds", R(r"kiriyesu"))
g("indeterminate", R(r"[āa]byākat(?:aṃ|ā|a)", aval))
g("indeterminate functional", R(r"kiriyābyākataṃ"))
g("indeterminate functional mind", R(r"kiriyābyākataṃ"))
g("wholesome", POS_ANY)
g("unwholesome", NEG_ANY)
g("wholesome mind", POS_MIND)
g("unwholesome mind", NEG_MIND)
g("wholesome minds", POS_MINDS)
g("unwholesome minds", NEG_MINDS)
g("minds", POS_MINDS, NEG_MINDS, R(r"kiriyesu"), R(r"(?<=cattāro )arūpāvacarā"))
g("mind",
  R(r"[Cc]itt(?:añca|aṃ|ā|ena)(?!\w)", lemma="citta"), R(r"[Cc]itta(?=\w)", lemma="citta"),
  R(r"([Cc])itt(?=uppād|ānu)", lambda m: m.group(1) + "itta", "citta"),
  R(r"mano(?=dhātu)", lemma="mano"), R(r"man(?=āyatan)", "mano", "mano"),
  *MIND_IMPLICIT)
g("material form", R(r"[Rr]ūpa(?:ñca|ṃ|ssa)(?!\w)"))
g("form", R(r"[Rr]ūpa(?:ñca|ṃ|ssa)(?!\w)"))
g("material", R(r"[Rr]ūpa(?:ñca|ṃ|ssa)(?!\w)"), R(r"(?<!a)rūpino"))
g("form and nibbāna", R(r"[Rr]ūpa(?:ñca|ṃ),? nibbānañca"))
g("life and nibbāna", R(r"sāmaññaphalāni,? nibbānañca"))
g("nibbāna are states", R(r"nibbānañca anārammaṇā"))
g("contemplative", R(r"sāmañña(?=phal)"))
g("life", R(r"sāmañña(?=phal)"))
g("fruits", R(r"phalāni"))
g("fruit", R(r"phalaṃ"))
g("paths", R(r"maggā(?!\w)"))
g("paths not included", R(r"maggā apariyāpannā"))
g("existence", R(r"([Bb])hav(?=āsavo|arāga)", lambda m: m.group(1) + "hava"), NDE_OK)
g("spheres", NDE_OK)
g("spheres of existence", NDE_OK)
g("dissociated", R(r"vippayutt(?:ā|e|o|a)"))
g("associated", R(r"sampayutt(?:ā|e|o|a)"))
g("dissociated from knowledge", R(r"ñāṇavippayutt(?:e|a)"))
g("knowledge", R(r"ñāṇa"))
g("dissociated from wrong", R(r"diṭṭhigatavippayutt(?:ā|a)"))
g("greed and dissociated", R(r"vippayutt(?:a|ā )lobha"))
g("wrong", R(r"diṭṭhigata"))
g("wrong view", R(r"diṭṭhigata"))
g("view", R(r"diṭṭhigata", lemma="ditthi"), R(r"(?<!\w)[Dd]iṭṭhi(?!gata|saṃyojan)", lemma="ditthi"))
g("views", R(r"diṭṭhi(?=saṃyojan)"), R(r"([Dd])iṭṭh(?=āsavo|upādān)", lambda m: m.group(1) + "iṭṭhi"))
g("seeing", R(r"dassanena"))
g("abandoned", R(r"pahātabb[āa]"))
g("abandoned by development", R(r"bhāvanāya pahātabb[āa]"))
g("object", R(r"ārammaṇ(?:ā|a)"))
g("states as object", R(r"ārammaṇā"))
g("ten", R(r"(?<!\w)[Dd]asa(?!\w)"))
g("twelve", R(r"([Dd])vādas", lambda m: m.group(1) + "vādasa"))
g("eleven", R(r"ekādasa"))
g("noble", R(r"ariya(?=magg)"))
g("highest", R(r"Upariṭṭhimaṃ"))
g("arahantship", R(r"arahatta"))
g("invariably", R(r"Niyogā"))
g("others", R(r"bahiddhā"))
g("others' states", R(r"bahiddhā"))
g("bound", R(r"uppādino"), R(r"baddha"))
g("faculties", R(r"indriya"))
g("faculties and nibbāna", R(r"indriyabaddharūpañca nibbānañca"))
g("aggregate", R(r"kkhandho", "khandho"))
g("aggregate of feeling", R(r"Vedanākkhandho"))
g("aggregate of mental", R(r"saṅkhārakkhandho"))
g("aggregate of perception", R(r"saññākkhandho"))
g("mental formations", R(r"saṅkhāra(?=kkhandho)"))
g("formations", R(r"saṅkhāra(?=kkhandho)"))
g("perception", R(r"(?<=neva)saññā|saññā(?=kkhandho)"))
g("non-perception", R(r"(?<=n)āsaññā", "asaññā"))
g("mental", R(r"cetasikā", lemma="cetasika"), R(r"saṅkhāra(?=kkhandho)", lemma="sankhara"))
g("mental factors", R(r"cetasikā"))
g("factors", R(r"cetasikā"))
g("mental-object", R(r"dhamm(?=āyatan)", "dhamma"))
g("mental-object base", R(r"dhammāyatan(?:aṃ|a)"))
g("eye", R(r"([Cc])akkhāyatan", lambda m: m.group(1) + "akkhu"))
g("eye base", R(r"[Cc]akkhāyatanaṃ"))
g("touch", R(r"phoṭṭhabb(?=āyatan)", "phoṭṭhabba"))
g("touch base", R(r"phoṭṭhabbāyatanaṃ"))
g("visible-form", R(r"([Rr])ūp(?=āyatan)", lambda m: m.group(1) + "ūpa"))
g("visible-form base", R(r"[Rr]ūpāyatanaṃ"))
g("sound", R(r"sadd(?=āyatan)", "sadda"))
g("sound base", R(r"saddāyatanaṃ"))
g("smell", R(r"gandh(?=āyatan)", "gandha"))
g("smell base", R(r"gandhāyatanaṃ"))
g("taste", R(r"ras(?=āyatan)", "rasa"))
g("taste base", R(r"rasāyatanaṃ"))
g("space", R(r"ākās(?=a|ā)", "ākāsa"))
g("space element", R(r"ākāsadhātu"))
g("water", R(r"āpo(?=dhātu)"))
g("water element", R(r"āpodhātu"))
g("element", R(r"dhātu(?!yo)"))
g("elements", R(r"dhātuyo", lemma="dhatu"), R(r"(?<=mahā)bhūt(?:ā|ānaṃ)", lemma="bhuta"))
g("great elements", R(r"mahābhūt(?:ā|ānaṃ)"))
g("mind elements", R(r"manodhātuyo"))
g("mind element", R(r"manodhātu(?!yo)"))
g("functional mind element", R(r"kiriyāmanodhātu"))
g("mind-consciousness", R(r"manoviññāṇ(?=a)", "manoviññāṇa"))
g("mind-consciousness element", R(r"manoviññāṇadhātu(?:yo)?"))
g("functional mind-consciousness", R(r"kiriyāhetukamanoviññāṇ(?=a)", "kiriyāhetukamanoviññāṇa"))
g("functional mind-consciousness element", R(r"kiriyāhetukamanoviññāṇadhātu"))
g("element accompanied", R(r"dhātu \w+sahagatā"))
g("mind-consciousness element accompanied", R(r"manoviññāṇadhātu \w+sahagatā"))
g("base of infinite", R(r"[Vv]iññāṇañcāyatanaṃ", lemma="inf"), R(r"(?<=ākās)ānañcāyatanaṃ", lemma="inf"))
g("infinite", R(r"[Vv]iññāṇañcāyatanaṃ", lemma="inf"), R(r"(?<=ākās)ānañc(?=ā)", "ānañca", lemma="inf"))
g("nothingness", R(r"([Āā])kiñcaññ(?=ā)", lambda m: m.group(1) + "kiñcañña"))
g("edible", R(r"kabaḷīkāro"))
g("edible food", R(r"kabaḷīkāro āhāro"))
g("food", R(r"āhāro"))
g("lightness", R(r"lahutā"))
g("lightness of material", R(r"rūpassa lahutā"))
g("pliancy", R(r"mudutā"))
g("pliancy of material", R(r"rūpassa mudutā"))
g("workability", R(r"kammaññatā"))
g("workability of material", R(r"rūpassa kammaññatā"))
g("growth of material", R(r"rūpassa upacayo"))
g("continuity", R(r"santati"))
g("continuity of material", R(r"rūpassa santati"))
g("born", R(r"cittajaṃ"))
g("caused", R(r"(?<=citta)hetukaṃ"))
g("bodily", R(r"kāya(?=viññatti|gantho)"))
g("bodily intimation", R(r"kāyaviññatti"))
g("intimation", R(r"(?<=kāya)viññatti"))
g("verbal", R(r"vacī(?=viññatti)"))
g("verbal intimation", R(r"vacīviññatti"))
g("remorse", R(r"kukkucca"))
g("torpor", R(r"middha"))
g("sloth", R(r"[Tt]hin(?:aṃ|a)"))
g("prompted", R(r"sasaṅkhārikesu"))
g("ill", R(r"[Bb]yāpād(?:o|a)"))
g("covetousness", R(r"[Aa]bhijjhā"))
g("conceit", R(r"[Mm]āna(?=saṃyojan)|(?<!\w)[Mm]āno(?!\w)"))
g("aversion", R(r"[Pp]aṭigh(?:aṃ|a)"))
g("envy", R(r"[Ii]ssā"))
g("stinginess", R(r"macchariya"))
g("lust", R(r"rāga"))
g("sensual lust", R(r"[Kk]āmarāga"))
g("ignorance", R(r"[Aa]vijjā"))
g("shamelessness", R(r"ahirik(?:añca|aṃ)"))
g("fearlessness", R(r"anottapp(?:añca|aṃ)"))
g("fearlessness of wrongdoing", R(r"anottapp(?:añca|aṃ)"))
g("wrongdoing", R(r"anottapp(?:añca|aṃ)"))
g("bases", R(r"vatthūni"))
g("defilement", R(r"saṃkilesikā"), R(r"kilesa(?=vatthūni)"))
g("doctrine", R(r"vād(?=upādān)", "vāda"))
g("self", R(r"atta(?=vād)"))
g("pleasures", R(r"kām(?=upādān)", "kāma"))
g("sensual pleasures", R(r"kām(?=upādān)", "kāma"))
g("clinging to sensual", R(r"[Kk]āmupādānaṃ"))
g("clinging to views", R(r"diṭṭhupādānaṃ"))
g("clinging to rules", R(r"sīlabbatupādānaṃ"))
g("rules", R(r"[Ss]īla(?=bbat)"))
g("observances", R(r"(?<=[Ss]īla)bbat", "vata"))
g("rules and observances", R(r"[Ss]īlabbat", lambda m: m.group(0) + "a"))
g("misapprehension of rules", R(r"[Ss]īlabbataparāmās(?:o|a)"))
g("desire", R(r"chanda"), R(r"(?<!\w)([Kk])ām(?=āsavo)", lambda m: m.group(1) + "āma"))
g("sensual desire", R(r"[Kk]āmacchanda"), R(r"(?<!\w)([Kk])ām(?=āsavo)", lambda m: m.group(1) + "āma"))
g("taint", R(r"āsavo"))
g("taint of sensual", R(r"[Kk]āmāsavo"))
g("taint of existence", R(r"[Bb]havāsavo"))
g("taint of views", R(r"diṭṭhāsavo"))
g("taint of ignorance", R(r"[Aa]vijjāsavo"))
g("fetter", R(r"saṃyojanaṃ(?!\w)"))
g("fetter of sensual", R(r"[Kk]āmarāgasaṃyojanaṃ"))
g("fetter of aversion", R(r"[Pp]aṭighasaṃyojanaṃ"))
g("fetter of conceit", R(r"[Mm]ānasaṃyojanaṃ"))
g("fetter of views", R(r"[Dd]iṭṭhisaṃyojanaṃ"))
g("fetter of doubt", R(r"[Vv]icikicchāsaṃyojanaṃ"))
g("fetter of misapprehension", R(r"parāmāsasaṃyojanaṃ"))
g("fetter of lust", R(r"(?<=bhava)rāgasaṃyojanaṃ"))
g("fetter of envy", R(r"[Ii]ssāsaṃyojanaṃ"))
g("fetter of stinginess", R(r"macchariyasaṃyojanaṃ"))
g("fetter of ignorance", R(r"[Aa]vijjāsaṃyojanaṃ"))
g("hindrance", R(r"nīvaraṇaṃ(?!\w)"))
g("hindrance of sensual", R(r"[Kk]āmacchandanīvaraṇaṃ"))
g("hindrance of ill", R(r"byāpādanīvaraṇaṃ"))
g("hindrance of sloth", R(r"thinamiddhanīvaraṇaṃ"))
g("hindrance of restlessness", R(r"uddhaccakukkuccanīvaraṇaṃ"))
g("hindrance of remorse", R(r"kukkuccanīvaraṇaṃ"))
g("hindrance of doubt", R(r"vicikicchānīvaraṇaṃ"))
g("hindrance of ignorance", R(r"avijjānīvaraṇaṃ"))
g("tie", R(r"gantho"))
g("bodily tie", R(r"kāyagantho"))
g("tie of covetousness", R(r"[Aa]bhijjhākāyagantho"))
g("tie of ill", R(r"[Bb]yāpādo kāyagantho"))
g("tie of misapprehension", R(r"parāmāso kāyagantho"))
g("tie of dogmatic", R(r"(?<=sacc)ābhiniveso kāyagantho", aval))
g("dogmatic", R(r"(?<=sacc)ābhiniveso", "abhiniveso"))
g("belief", R(r"(?<=sacc)ābhiniveso", "abhiniveso"))
g("true", R(r"(?<=idaṃ)sacc(?=ā)", "sacca"))
g("delusion accompanied", R(r"sahagat(?:o|aṃ) (?:\w+ )?moh(?:o|aṃ)"))
g("together", R(r"(?<!\w)ekato(?!\w)"), R(r"(?<=Vitakka)sahajāto"))
g("applied", R(r"vitakk(?:ā|o|e|aṃ|a)"))
g("applied thought", R(r"vitakk(?:ā|o|e|aṃ|a)"))
g("sustained", R(r"vicār(?:ā|o|e|aṃ|a)"))
g("sustained thought", R(r"vicār(?:ā|o|e|aṃ|a)"))
g("thought", R(r"vitakk(?:ā|o|e|aṃ|a)", lemma="vitakka"), R(r"vicār(?:ā|o|e|aṃ|a)", lemma="vicara"))
g("thought arisen", R(r"uppann\w* (?:ca )?(?:vitakka)?vi(?:cār|takk)\w*"))
g("sustained thought arisen", R(r"uppann\w* (?:ca )?(?:vitakka)?vicār\w*"))
g("states with applied", R(r"dhammā savitakk\w*|savitakk\w*"))
g("states without applied", R(r"dhammā avitakk\w*|avitakk\w*"))
g("states with sustained", R(r"dhammā savicārā"))
g("states without sustained", R(r"dhammā avicārā"))
g("states with rapture", R(r"dhammā sappītikā"))
g("states without rapture", R(r"dhammā appītikā"))
g("states accompanied", R(r"dhammā \w*sahagatā"))
g("states not accompanied", R(r"dhammā na \w*sahagatā"))
g("defiled", R(r"(?<![Aa])saṃkiliṭṭh(?:ā|a)"))
g("undefiled", R(r"[Aa]saṃkiliṭṭh(?:ā|a)"))
g("defiled states", R(r"dhammā saṃkiliṭṭhā"))
g("undefiled states", R(r"dhammā asaṃkiliṭṭhā|Asaṃkiliṭṭhā dhammā"))
g("alone", NDE_OK)
g("prompted", R(r"sasaṅkhārikesu"))
g("variant", NDE_OK)
g("sabbeva", NDE_OK)

# ---- group nouns (cut at the root; prefix sa-/a(n)- stripped, map-conventions 2)
g("taints", lem(r"[Āā]sav", ["ā", "o", "e", "a"]))
g("fetters", lem(r"[Ss]aṃyojan", ["iyā", "āni", "ā", "añca", "aṃ", "e", "a"]))
g("ties", lem(r"[Gg]anth", ["aniyā", "ā", "e", "o", "a"]))
g("hindrances", lem(r"[Nn]īvaraṇ", ["iyā", "āni", "ā", "aṃ", "e", "a"]))
g("clinging", lem(r"[Uu]pādān", ["iyā", "āni", "ā", "añca", "aṃ", "e", "a"]))
g("kinds of clinging", lem(r"[Uu]pādān", ["āni", "ā", "e"]))
g("defilements", lem(r"(?<!saṃ)[Kk]iles", ["ā", "e", "a"]))
g("misapprehensions", R(r"[Pp]arāmāsā(?!\w)|[Pp]arāmāsātipi"))
g("misapprehension", R(r"[Pp]arāmās(?:aṃ|o|a)"))
g("misapprehended", R(r"parāmaṭṭh(?:ā|o)"))
GROUPS = [("taints", "āsavā", "[Āā]sava", "sāsavā", "anāsavā"),
          ("fetters", "saṃyojanā", "[Ss]aṃyojana", "saṃyojaniyā", "asaṃyojaniyā"),
          ("ties", "ganthā", "[Gg]antha", "ganthaniyā", "aganthaniyā"),
          ("hindrances", "nīvaraṇā", "[Nn]īvaraṇa", "nīvaraṇiyā", "anīvaraṇiyā"),
          ("clinging", "upādānā", "[Uu]pādāna", "upādāniyā", "anupādāniyā"),
          ("defilements", "kilesā", "[Kk]ilesa", "saṃkilesikā", "asaṃkilesikā"),
          ("defilement", "kilesā", "[Kk]ilesa", "saṃkilesikā", "asaṃkilesikā"),
          ("misapprehension", "parāmāsā", "[Pp]arāmāsa", "parāmaṭṭhā", "aparāmaṭṭhā")]
for n, plain, member, subj, nsubj in GROUPS:
    if n != "defilement":
        g(f"dissociated from {n}", R(rf"{member}vippayutt(?:ā|o)"))
        g(f"{n} and subject", R(rf"{plain} ceva {subj}"))
        g(f"{n} but subject", R(rf"{member}vippayuttā {subj}"))
        g(f"{n} are states", R(r"(?:Tāneva|Teva) (?P<v>\S+ \S+)"))
    if n in ("fetters", "ties", "hindrances"):
        g(f"subject to {n}", R(subj))
g("subject to taints", R(r"[Ss]āsavā"))
g("subject to defilement", R(r"saṃkilesikā"))
g("subject to clinging", R(r"upādāniyā"))
g("free", R(r"[Aa]nāsavā"))
g("free of taints", R(r"[Aa]nāsavā"))
g("states free", R(r"dhammā anāsavā|Anāsavā dhammā"))
SUBJ = "(?:sāsavā|saṃyojaniyā|ganthaniyā|nīvaraṇiyā|upādāniyā|saṃkilesikā)"
NSUBJ = "(?:saṃyojaniyā|ganthaniyā|nīvaraṇiyā|nupādāniyā|saṃkilesikā)"
g("states subject", R(rf"dhammā {SUBJ}"))
g("states not subject", R(rf"dhammā a{NSUBJ}|A{NSUBJ} dhammā"))
g("states dissociated", R(r"dhammā (?:no |na )?\w*vippayuttā"), R(r"vippayuttā (?:kho pana )?dhammā"))
g("roots", lem(r"hetu", ["kā", "ke", "ka"], stem="ka", excl=r"maggahetuk\w*"), R(r"hetū(?!\w)"),
  R(r"([Hh])etu(?=sampayutt|vippayutt)", lambda m: m.group(1) + "etu"))
g("roots arise", R(r"hetū ekato uppajjanti"))
g("roots arisen", R(r"(?<=etth)uppanne hetū"))
g("states whose roots", R(r"dhammā [^?–]*?pahātabbahetukā"))


# ------------------------------------------------------------------ explicit values
EXPLICIT = {}


def E(bid, **kw):
    EXPLICIT.setdefault(bid, {}).update({k.replace("_", " "): v for k, v in kw.items()})


def X(bid, d):
    EXPLICIT.setdefault(bid, {}).update(d)


exec((HERE / "map_5-atthakathakandam_items.py").read_text(encoding="utf-8"))


# ------------------------------------------------------------------ build
def resolve(kw, text):
    specs = G.get(kw)
    if specs is None:
        return None, []
    hits = []
    for sp in specs:
        if sp == NDE_OK:
            continue
        hits += list(sp.hits(text))
    if not hits:
        return (NDE if NDE_OK in specs else None), []
    t = min(h[0] for h in hits)
    hs = sorted((h for h in hits if h[0] == t), key=lambda h: h[1])
    first = {}
    for h in hs:
        first.setdefault(h[2] or kw, h)
    vals = []
    for h in sorted(first.values(), key=lambda h: h[1]):
        if h[3] not in vals:
            vals.append(h[3])
    return " / ".join(vals), hs


def build(dump=None):
    segs = segments()
    src = (HERE / f"{CH}.keywords.md").read_text(encoding="utf-8").splitlines()
    out, missing, unused = [], [], []
    for line in src:
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        text = segs[bid]
        ex = EXPLICIT.get(bid, {})
        kws = [k.strip() for k in rest.split(", ")]
        pairs = []
        for k in kws:
            kl = k.lower()
            how = "E"
            v = ex.get(kl)
            if v is None:
                v, _ = resolve(kl, text)
                how = "G"
            if v is None:
                missing.append((bid, k))
                v = "???"
            assert ", " not in v, (bid, k, v)
            pairs.append(f"{v}={k}")
            if dump is not None and (not dump or bid in dump):
                print(f"  {bid} {how} {k!r:40} -> {v}")
        used = {k.lower() for k in kws}
        unused += [(bid, k) for k in ex if k not in used]
        out.append(f"[{bid}] " + ", ".join(pairs))
    if missing:
        print("MISSING", len(missing))
        for bid, k in missing:
            print("   ", bid, k)
    if unused:
        print("UNUSED explicit keys", unused)
    if not missing:
        (HERE / f"{CH}.mapped.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
        print(CH, "lines", len(out), "written")


if __name__ == "__main__":
    a = sys.argv[1:]
    build(dump=a[1:] if a and a[0] == "--dump" else None)
