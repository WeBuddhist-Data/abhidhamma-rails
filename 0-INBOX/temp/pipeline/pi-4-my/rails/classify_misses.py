"""Classify every termbase-adherence miss of the pi-4 Burmese zero-shot: GENUINE / INFLECTION / ARTEFACT; and every
miss the rails introduce (a miss of the rails that the zero-shot did not have). Model: pi-3-my/rails/classify_misses.py
and pi-2-my/rails/classify_misses.py (read only).

usage: python3 -I -X utf8 classify_misses.py   (after build_rails.py + apply_termbase.py + the rails adherence run)
Inputs: rails/adherence-zeroshot.txt (fixed input, re-run with each approved termbase change), rails/adherence-rails.txt,
rails/layer-log.tsv, rails/apply-log.tsv, rails/fixes-log.tsv (the review fixes, apply_fixes.py),
the zero-shot keyword map AI_translation/burmese/pi-4-keywords-by-reference-pali-burmese-plain.md (the zero-shot's own
form of each keyword in each segment).
Writes rails/adherence-classified.tsv (id, keyword, termbase term, text form, class, reason, ch, src).
  * GENUINE row (zero-shot miss fixed in the rails): its keyword belongs to a family (FAM: keyword -> Lnn / Rnn) whose
    layer patch or residual rule was applied in this build (layer-log / apply-log.tsv); the zero-shot form (keyword
    map) occurs in the zero-shot segment; and the keyword passes in the rails segment (adherence_my.occurs).
  * INFLECTION / ARTEFACT row: its text-form regex must match the segment (the rails segment when the miss is left, the
    zero-shot segment when an unrelated rails change makes the keyword pass), the keyword map's zero-shot form for that
    keyword must be one of the stated forms (where given), and its Pāli check must match the segment's Pāli.
Any other row is UNVERIFIED and the run fails (exit 1).
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402

PALI = ROOT / "AI_translation/pali/pi-4_split_chapters"
ZS = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
RL = ROOT / "AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters"
TB = ROOT / "AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md"
KMAP = ROOT / "AI_translation/burmese/pi-4-keywords-by-reference-pali-burmese-plain.md"
OUT = HERE / "adherence-classified.tsv"
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
W = "a-zA-Zāīūṃṅñṭḍṇḷ"

# --- GENUINE families: keyword -> layer patch (my_formulas_rails.py); apply_termbase.py has no rule (no residual case)
FAM = {
    "ṭhito": "L01",
    "pakāsenti": "L05", "brahmacariyaṃ pakāsenti": "L05",
    "dīgharattaṃ": "L06",
    "dubbaṇṇo": "L07", "dubbaṇṇatāya": "L07",
    "abhisamayo": "L12", "puggalassa abhisamayo": "L12",
    "atthe": "L13", "atthaṃ": "L13", "attha": "L13",
    "byañjanaṃ": "L14",
    "paṭipannānaṃ": "L15", "duppaṭipannānaṃ": "L15", "micchāpaṭipannānaṃ": "L15", "sammāpaṭipannā": "L15",
    "sammāpaṭipannānaṃ": "L15", "paṭipanno": "L15",
    "abhirūpo": "L16",
    "kasira": "L17", "kasirena": "L17",
    "ābādho": "L18",
    "ajinaṃ": "L19",
    "sappi": "L20",
    "rūpa": "L21",
    "raja": "L22",
    "ekanta": "L23",
    # review fixes (apply_fixes.py, fixes-log.tsv) for the termbase change of 2026-11-20
    "narassa": "F03",
    "sāci": "F05",
}

# --- INFLECTION / ARTEFACT families:
#     (keyword regex, class, text-form regex, map forms (tuple) or None, reason, Pāli check)
NEG = rf"(?<![{W}])"
OTHER = [
    # ---- INFLECTION: the same word, another Burmese grammatical form (the loose test does not strip it)
    *[(kw, "INFLECTION", form + r"(?!့)", (mform,),
       "finite «…ရမည်» (the gerundive ends the sentence) of the attributive termbase form «…ရမည့်»" + extra, pcheck)
      for kw, form, mform, extra, pcheck in (
          ("cintetabbā", r"စဉ်းစားရမည်", "စဉ်းစားရမည့်", " (the translated bracket note ^4-62)", r"cintetabbā"),
          ("upaṭṭhātabbā", r"လုပ်ကျွေးပြုစုရမည်", "လုပ်ကျွေးပြုစုရမည့်", "", r"upaṭṭhātabbā"),
          ("daṭṭhabbo", r"သိမှတ်ရမည်", "သိမှတ်ရမည့်", "", r"daṭṭhabb[oā]"),
          ("desetabbo", r"တရား ဟောရမည်", "ဟောကြားရမည့်",
           "; the verb itself was changed by L04 «ဟောကြား» → «ဟော» (the termbase word), the finite ending is left",
           r"dhammo desetabbo"))],
    (r"byāpajjati", "INFLECTION", r"ဒဏ်ရာ ရ၏", ("ဒဏ်ရာ ရသည်",),
     "finite «ဒဏ်ရာ ရ၏» of the termbase «ဒဏ်ရာ ရသည်» (sense 2, wounded in battle; «ရသည်» is not stripped by the test)",
     r"haññati byāpajjati"),
    (r"saṅkhaṃ gacchati", "INFLECTION", r"အမည် ရ၏", ("အမည် ရသည်",),
     "finite «အမည် ရ၏» of the termbase «အမည် ရသည်»", r"saṅkhaṃ gacchati"),
    (r"vippaṭisārī", "INFLECTION", r"နောင်တ ရသူ", ("နောင်တ ရသော",),
     "agent «နောင်တ ရသူ» (predicate «vippaṭisārī hoti» of a person) of the attributive termbase «နောင်တ ရသော»",
     r"vippaṭisārī"),
    (r"phāsu", "INFLECTION", r"ချမ်းသာ ဖြစ်လိမ့်မည်", ("ချမ်းသာ",),
     "predicate «… ချမ်းသာ ဖြစ်လိမ့်မည်» (sā ca no phāsu bhavissati) of the adverbial termbase «ချမ်းသာစွာ» "
     "(decision phāsu|0: the same word as predicate)", r"phāsu bhavissati"),
    # ---- ARTEFACT: privative fragments (style rule a- / an- / du- = «မ» + verb or the entry of the negative word)
    (r"pahīno|pahīnāni|pahīnā|pahīnaṃ", "ARTEFACT", r"မပယ်ရသေး", ("ပယ်ရသော",),
     "privative: the keyword is the fragment of appahīno / appahīnā / appahīnaṃ / appahīnāni «မပယ်ရသေး» (decisions "
     "pahīno|0 … pahīnāni|0: «ပယ်ရသော» is only the positive part of appahīn-, pi-3 uppannā model); no free pahīn- word",
     rf"(?s)^(?!.*{NEG}pahīn).*appahīn"),
    (r"āvattidhammo|āvatti", "ARTEFACT", r"ပြန်မလာတတ်သော သဘော ရှိ", ("ပြန်လာတတ်သော သဘော ရှိသော", "ပြန်လာတတ်သော"),
     "privative: the keyword is the positive part of anāvattidhammo «ပြန်မလာတတ်သော သဘော ရှိသူ» (style rule an- = «မ» + "
     "verb); no free āvatti word", rf"(?s)^(?!.*{NEG}āvatti).*anāvatti"),
    (r"vaco", "ARTEFACT", r"သွန်သင်ချက်ကို နားမထောင်", ("သွန်သင်ချက်ကို နားထောင်သော",),
     "privative: dubbaco has its own entry «သွန်သင်ချက်ကို နားမထောင်သူ»; vaco «… နားထောင်သော» is suvaco's part",
     r"(?s)^(?!.*suvaco).*dubbaco"),
    (r"dhāraṇatā", "ARTEFACT", r"စွဲမှတ် မထားခြင်း", ("စွဲမှတ်ထားခြင်း",),
     "privative: adhāraṇatā «စွဲမှတ် မထားခြင်း» (the negation «မ» before the verb ထား); no free dhāraṇatā",
     rf"(?s)^(?!.*{NEG}dhāraṇatā).*adhāraṇatā"),
    (r"maccharī", "ARTEFACT", r"ဝန်မတိုတတ်သူ", ("ဝန်တိုတတ်သူ",),
     "privative: amaccharī has its own entry «ဝန်မတိုတတ်သူ»", rf"(?s)^(?!.*{NEG}maccharī).*amaccharī"),
    (r"pameyyo", "ARTEFACT", r"ချိန်ဆ၍ မရနိုင်သူ", ("ချိန်ဆ၍ ရနိုင်သော",),
     "privative: appameyyo has its own entry «ချိန်ဆ၍ မရနိုင်သူ» (decision pameyyo|0)",
     rf"(?s)^(?!.*{NEG}(?:su|du)?pameyyo).*appameyyo"),
    (r"manasi", "ARTEFACT", r"နှလုံး မသွင်း", ("နှလုံး",),
     "privative fragment: «နှလုံး» is only the part before the negated verb in «နှလုံး မသွင်း» (neva … manasi karoti; "
     "decision manasi|0)", r"neva ādiṃ manasi karoti"),
    # ---- ARTEFACT: compounds / phrases with their own entry or word
    (r"paññatti|Puggalapaññatti", "ARTEFACT", r"ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း",
     ("သတ်မှတ်ဖော်ပြခြင်း", "ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း"),
     "the approved BOOK TITLE «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း» at ^4-0 (book-title rule; decisions paññatti|0 / "
     "puggalapaññatti|0 keep it)", r"Puggalapaññattipāḷi"),
    (r"paññatti|puggalapaññatti", "ARTEFACT", r"“ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း” ခေါင်းစဉ်စာရင်း",
     ("သတ်မှတ်ချက်", "ပုဂ္ဂိုလ် သတ်မှတ်ချက်"),
     "review fix A1 (F01): the mātikā colophon ^4-M-16 names the book by its approved BOOK TITLE «ပုဂ္ဂိုလ်များကို "
     "သတ်မှတ်ဖော်ပြခြင်း», as the colophon ^4-209 (book-title rule); the term «ပုဂ္ဂိုလ် သတ်မှတ်ချက်» is the designation "
     "itself", r"Puggalapaññattimātikā niṭṭhitā"),
    (r"sambuddho", "ARTEFACT", r"ပစ္စေကဗုဒ္ဓါ", ("(no direct equivalent)",),
     "paccekasambuddho has its own entry «ပစ္စေကဗုဒ္ဓါ»; no free sambuddho", rf"(?s)^(?!.*{NEG}sambuddho).*paccekasambuddho"),
    (r"pāpa", "ARTEFACT", r"ယုတ်မာသော", ("ယုတ်မာသော",),
     "pāpadhammo / pāpiccho: their own word «ယုတ်မာသော …» (entries pāpadhammo, pāpakā, pāpaṃ; decision pāpa|0: the "
     "termbase «ဆိုး» is the compound member of pāpamittatā); no pāpamitt- word", r"(?s)^(?!.*pāpamitt).*pāp(?:adhamm|icch)"),
    (r"kārī", "ARTEFACT", r"ကောင်းစွာ ဆင်ခြင်သိမြင်လျက် ပြုလေ့ရှိ", ("ပြုလေ့ရှိသော",),
     "sampajānakārī has its own entry «ကောင်းစွာ ဆင်ခြင်သိမြင်လျက် ပြုလေ့ရှိသော» (decision kārī|0)", r"sampajānakārī"),
    (r"vaṇṇa", "ARTEFACT", r"ချီးမွမ်း", ("ချီးမွမ်း",),
     "spoken praise: the phrases vaṇṇaṃ bhāsitā / vaṇṇārahassa have their own entries «ချီးမွမ်း …» (decision vaṇṇa|0)",
     r"vaṇṇārahassa vaṇṇaṃ bhāsitā"),
    (r"gilāna", "ARTEFACT", r"လူနာ", ("လူနာ",),
     "the sick person: gilāno / gilānūpamā «လူနာ» (entry gilāno); the termbase gilāna «သူနာ» is the requisite idiom "
     "gilānapaccaya only (decision gilāna|0, H11); no gilānapaccaya in the segment",
     r"(?s)^(?!.*gilāna-?p?paccaya).*gilān"),
    (r"bhūta", "ARTEFACT", r"ခပ်သိမ်းသော သတ္တဝါ|ဟုတ်မှန်|အမှန်", ("(no direct equivalent)",),
     "not bhūtagāma (the termbase sense «အပင်»): sabbapāṇabhūta «ခပ်သိမ်းသော သတ္တဝါ», bhūtavādī, sucibhūtena, "
     "yathābhūtaṃ, mudubhūte have no word bhūta of their own", r"(?s)^(?!.*bhūtagām).*bhūt"),
    (r"para", "ARTEFACT", r"ပရနိမ္မိတ", ("ပရ",),
     "proper name Paranimmitavasavattī «ပရနိမ္မိတဝသဝတ္တီ» (pi-1 rule: proper names stay names; decision para|0)",
     r"(?s)^(?!.*{0}para(?!nimmit)).*[Pp]aranimmit".format(NEG)),
    (r"evaṃ|evameva", "ARTEFACT", r"ဤနည်းတူ\]", ("ဤနည်းတူ",),
     "the bracket note «… evaṃ / evamuparipi / evameva» «… ဤနည်းတူ]» (harmonise B7; decisions evaṃ|0 / evameva|0: "
     "«ဤနည်းတူ» is only the bracket note)", r"\[[^\]]*eva[mṃ]"),
    (r"aggaṃ", "ARTEFACT", r"ဖုန်လုံး ဟူသည်", ("(no direct equivalent)",),
     "rajaggasmiṃ = rajaggaṃ, which has its own entry «ဖုန်လုံး» (decision raja|0; mapper: rajagga has no word "
     "of its own); aggaṃ «ဖျား» is dhajaggaṃ «အလံဖျား» (doubt 4)", r"Kimassa rajaggasmiṃ"),
    # ---- ARTEFACT: approved rails-step notes of the termbase (termbase/APPROVED.md)
    (r"phalaṃ", "ARTEFACT", r"အကျိုး ကြီးမား", ("အကျိုး",),
     "approved rails-step note: phalaṃ at ^4-116 / ^4-117 (mahapphalaṃ, the fruit of a gift) = «အကျိုး» (sense "
     "phala «result»), not this headword's term «အသီးအပွင့်»", r"mahapphalaṃ"),
    (r"indriyānaṃ", "ARTEFACT", r"စွမ်းရည်", ("စွမ်းရည်",),
     "approved rails-step note: indriyānaṃ at ^4-M-6 = the 22 faculties «စွမ်းရည်» (indriya «faculties as a "
     "category»), not the sense organs «အာရုံခံ အင်္ဂါ»", r"bāvīsatindriyāni"),
    # ---- ARTEFACT: another sense the term does not cover (kept, termbase doubts)
    (r"attanā", "ARTEFACT", r"(?:ဖြစ်ပြီးသော|စင်ကြယ်သော) မိမိကိုယ်ဖြင့်", ("မိမိကိုယ်",),
     "«X-bhūtena attanā viharati» = «… မိမိကိုယ်ဖြင့် နေ၏» (the self as instrument, decision attanā|0 names it for "
     "the speaker to check); the term «မိမိကိုယ်တိုင်» (personally) would change the meaning (doubt 2)",
     r"bhūtena attanā"),
    (r"vācāya", "ARTEFACT", r"(?:ကုန်းတိုက်|ကြမ်းတမ်း)သော စကား", ("စကား",),
     "pisuṇāya / pharusāya vācāya = the speech itself «… စကား» (vācā / vācaṃ «စကား»), not the door of speech "
     "«နှုတ်» (decision vācāya|0: the rails step writes «စကား» here; doubt 3)", r"(?:pisuṇāya|pharusāya) vācāya"),
    (r"gahapati", "ARTEFACT", r"သူကြွယ်ဖြစ်စေ", ("သူကြွယ်",),
     "the householder himself «gahapati vā gahapatiputto vā» «သူကြွယ်ဖြစ်စေ» (decision gahapati|0 names it); the "
     "term «သူကြွယ်မျိုး» is the compound member of gahapatimahāsāla (doubt 1)", r"gahapati vā gahapatiputto"),
    (r"eva", "ARTEFACT", r"ဖုန်လုံးကိုပင် မြင်၍", ("ပင်",),
     "the identifying emphatic «ပင်» (rajaggaññeva «at the very sight of», tameva «that very»; = pi-2 diṭṭheva dhamme "
     "«မျက်မှောက်ဘဝ၌ပင်»); the term «သာ» (only) would change «tameva saṅgāmasīsaṃ»; the whole simile ^4-193 … "
     "^4-198 keeps one form (doubt 7)", r"rajaggaññeva disvā"),
]


def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for l in N(p.read_text(encoding="utf-8-sig")).splitlines():
            if not l.strip():
                continue
            buf.append(l)
            m = A.ID.search(l)
            if m:
                out[m.group(1)] = (p.name.split("-")[0].split(".")[0], " ".join(buf))
                buf = []
    return out


def pali_ok(check, text):
    if check is None:
        return True
    if check.startswith("!"):
        return re.search(check[1:], text) is None
    return re.search(check, text) is not None


def misses(path):
    out = []
    for l in open(path, encoding="utf-8"):
        f = N(l).rstrip("\n").strip().split("\t")
        if len(f) == 3 and f[0][:1].isdigit():
            out.append(tuple(f))
    return out


def applied_ids():
    ids = set()
    for name in ("layer-log.tsv", "apply-log.tsv", "fixes-log.tsv"):
        for l in open(HERE / name, encoding="utf-8").read().splitlines()[1:]:
            ids.update(re.findall(r"(?:^|[;,] )([LRF]\d\d) ", l.split("\t")[-1]))   # every family a reason names
    return ids


def kmap():
    kv = {}
    for l in open(KMAP, encoding="utf-8"):
        m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
        if m:
            for x in m.group(2).split(", "):
                if "=" in x:
                    k, v = x.split("=", 1)
                    kv[(m.group(1), k)] = v
    return kv


def main():
    tb = A.parse_termbase(TB)
    P, Z, R = segs(PALI), segs(ZS), segs(RL)
    done, KV = applied_ids(), kmap()
    zs = misses(HERE / "adherence-zeroshot.txt")
    rl = misses(HERE / "adherence-rails.txt")
    zkeys = {(i, k) for i, k, _ in zs}
    rkeys = {(i, k) for i, k, _ in rl}
    todo = [(r, "zeroshot") for r in zs] + [(r, "rails") for r in rl if (r[0], r[1]) not in zkeys]
    rows, counts, bad = [], {}, 0
    for (i, kw, term), src in todo:
        ch, zt = Z[i]
        rt, pt = R[i][1], P[i][1]
        left = (i, kw) in rkeys
        text = rt if left or src == "rails" else zt
        old = KV.get((i, kw), "")
        row = None
        if not left and src == "zeroshot":                      # fixed in the rails: a GENUINE family
            lid = FAM.get(kw)
            fixed = any(A.occurs(t, rt) for t in tb.get(kw.lower(), []))
            seen = bool(old) and (A.occurs(old, zt) or re.sub(r"(?:သည်|၏)$", "", old) in zt)
            if lid and lid in done and fixed and seen:
                row = (i, kw, term, old, "GENUINE", f"{lid}: zero-shot «{old}» → termbase «{term}»")
        if row is None:
            for rkw, cls, form, mforms, reason, pcheck in OTHER:
                if re.fullmatch(rkw, kw):
                    fm = re.search(form, text)
                    if fm and (mforms is None or old in mforms) and pali_ok(pcheck, pt):
                        note = "" if left or src == "rails" else (" [no longer a miss in the rails only because an "
                                                                   "unrelated layer word now occurs in the segment]")
                        row = (i, kw, term, fm.group(0).strip(), cls, reason + note)
                        break
        if row is None:
            row = (i, kw, term, "", "UNVERIFIED", "no class")
        bad += row[4] == "UNVERIFIED"
        counts[row[4]] = counts.get(row[4], 0) + 1
        rows.append(row + (ch, src))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("id\tkeyword\ttermbase term\ttext form\tclass\treason\tch\tsrc\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    nz = sum(1 for r in rows if r[7] == "zeroshot")
    print(f"{nz} zero-shot misses + {len(rows) - nz} rails-introduced:",
          ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none")
    for r in rows:
        if r[4] == "UNVERIFIED":
            print("UNVERIFIED", r[0], r[1], r[7], "|", r[2], "| map", KV.get((r[0], r[1])))
    sys.exit(1 if bad else 0)


main()
