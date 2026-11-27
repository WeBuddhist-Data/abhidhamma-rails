"""Writes mapper-my/map-table.md for phase 1 (preamble, 1-puggalakatha). Called by map_ch1.py; no work on import."""
import collections
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

RULES = """## Rules used (binding, unchanged)

The value is the word or phrase of THAT segment's Burmese (the FINAL pi-5 text) that carries the keyword, in the
dictionary form of the approved Burmese mappings:

- **pi-1** `map-table.md` rules 1–11 (approved 2026-11-17): rule 1 nouns without final case particles / plural markers
  (inner particles of a phrase stay); rule 2 a noun predicated of a subject = the noun; rule 3 adjectives / participles
  «…သော» (gerundives «…မည့်»); rule 4 verbs «…သည်»; rule 5 «X dhammā» and negatives; rule 6 sentence-final material
  dropped; rule 7 titles whole; rule 8 fragments that lost a negative = the positive part; rule 9 particles; rule 10
  discontinuous parts « … », no « / », no «, » / «၊» inside a value; rule 11 sense by context. The agreed later pi-1
  rules: absolutives keep «…၍»; relative pronouns = (no direct equivalent) where the Burmese builds the clause with
  «ရှိသော / ရှိသမျှ»; one sense per segment (decision 3); counts keep the text's classifier (decision 5).
- **pi-2** N1–N11 (approved 2026-11-18) and the harmonise decisions (compound members inside one Burmese word: one
  member gets the word, the other (no direct equivalent); «vuccati X» = «Xဟု ခေါ်သည်»; pi-2 «na uppajjati = … မဖြစ်ပေါ်»).
- **pi-3** M1–M9 (approved 2026-11-19): the « … » gap; a translated editors' note gets values, a Roman-script variant =
  (no direct equivalent) (M9 / M2); the presence check endings of M7.
- **pi-4** P1–P8 and A2: person-type names (P1), agent nouns «…သူ» (P6), the presence endings of P3, «X၍» against
  «မXဘဲ» (A2), «puggalo P» = «ပုဂ္ဂိုလ် … P» in text order (P8).
- **pi-1 … pi-4 values**: every keyword not in this run's tables is looked up in the FINAL pi-1 … pi-4 Burmese mappings
  (`AI_translation/burmese/pi-{1,2,3,4}-keywords-by-reference-pali-burmese-plain.md`; order pi-2, pi-3, pi-4, pi-1:
  pi-2 first where pi-1 and pi-2 differ, as the brief says): the most frequent value that the segment's Burmese has as a
  phrase, then one whose chunks are all literal, then (verbs, and phrases with another attributive ending) one present by
  an ending rule. A pi-1 … pi-4 multiword value present by an ending rule wins over a composed value.
- **pi-5 forms**: `my5-zeroshot-terms.md` single forms (persons, names, the propositions of §8 / §9), used where the
  segment has them.

## How the module is built (`map5_rules.py`, imported by phase 2)

Lookup per keyword: CTX[segment] → the chapter's own table → FRAME (dialectic machinery) → STOCK (core terms of the
book) → pi-5 terms (literal) → pi-1 … pi-4 value as a phrase → pi-5 terms (by an ending rule) → pi-1 … pi-4 multiword
value (by an ending rule) → compose (members joined, Q3 / Q4 / Q5) → counts → pi-1 … pi-4 value by an ending rule.
A value «@name» calls a context function (FUNCS) with the keyword, the Pāli segment and the Burmese segment; every
function checks its value against the text and falls back to the text's other word. Nothing runs on import (files are
read lazily); `Mapper(chapter_tables=…, ctx=…, funcs=…)` is the entry point, `verify_file(ch)` the verifier.

## NEW rules (beyond pi-1 … pi-4), for review

Q1. **Presence check, more endings** (`map5_rules.py`, each marked «pi-5»): «Xသော» and «Xသည်» also against the
    question form «Xသလော» (every proposition of the book is asked as «… ဖြစ်သလော / တွေ့ရသလော»); «Xသည်» also against
    the polite imperative «Xပါ» ([ṭīkā oloketabbā] «ဋီကာကို ကြည့်ပါ») and the elided series item «X…» (my5-zeroshot-
    terms §4: «… တွေ့ရ…»); an absolutive «X၍» also against the text's «Xပြီးမှ / Xပြီးလျှင် / Xပြီး / Xလျက်» (hutvā =
    ဖြစ်၍ against «လူ ဖြစ်ပြီးမှ»; sandhāvitvāna = ကူးသွား၍ against «ကူးသွားပြီးလျှင်») and the past negative
    «မXခဲ့ဘဲ» (pi-4 A2 extended: «na mātā hutvā» «အမိ မဖြစ်ခဲ့ဘဲ»).
Q2. **The answer formula** Āmantā = «ဟုတ်ပါသည်» whole (my5-zeroshot-terms §3 «Āmantā. = ဟုတ်ပါသည်။»): a fixed
    answer, not a verb whose ending rule 4 normalises (the full stop goes, rule 6).
Q3. **Multiword keywords in text order** (pi-1 rule 10, pi-4 P8): the members' values in the order of their tightest
    window in the segment's Burmese (the members of one phrase stand together); a finite verb «…သည်» goes last
    (Burmese is verb-final: Puggalo upalabbhati = ပုဂ္ဂိုလ် … တွေ့ရသည်, never «တွေ့ရသည် … ပုဂ္ဂိုလ်»); a part that has
    a value of its own is joined as a whole (nibbānassa paṭisaṃvedī upalabbhati = နိဗ္ဗာန်ကို ခံစားသူကို တွေ့ရသည်); an
    inner particle between adjacent members stays (rule 1: puggalassa paññatti = ပုဂ္ဂိုလ်၏ သတ်မှတ်ချက်, Rūpaṃ upādāya =
    ရုပ်ကို မှီ၍); members the text writes as one word join without a space (dibbena cakkhunā = နတ်မျက်စိ).
Q4. **The «လည်း» of ca / pi** is not part of a multiword keyword: where a member is followed by «…လည်း» the members
    are joined with « … » (rūpaṃ upalabbhati in «ရုပ်ကိုလည်း … တွေ့ရ» = ရုပ် … တွေ့ရသည်; puggalo saphalo «ပုဂ္ဂိုလ်သည်လည်း
    အသီးအပွင့် ရှိသော» = ပုဂ္ဂိုလ် … အသီးအပွင့် ရှိသော). The «လည်း» of «neither … nor» stays (pi-1 rule 6: puggalo neva
    saṅkhato = ပုဂ္ဂိုလ်သည် ပြုပြင်ဖန်တီးထားသော အရာလည်း မဟုတ်).
Q5. **Negated verbs**: a keyword with the negative (Puggalo nupalabbhati) = the text's «မ + verb» without «သည်» (pi-2
    «na uppajjati = … မဖြစ်ပေါ်»: Puggalo nupalabbhati = ပုဂ္ဂိုလ် … မတွေ့ရ); the bare upalabbhati of a negated
    segment keeps the positive «တွေ့ရသည်» (rule 8).
Q6. **The dialectic frame words** (FRAME table, one value book-wide; my5-zeroshot-terms §3 / §5): niggaha(ṃ) =
    ချေပချက်, paṭikamma(ṃ / e) = ပြန်လှန် ချေပချက်, upanayana = ဆက်စပ် အသုံးချချက်, niggamana = နိဂုံးချုပ်ချက်,
    paṭipādanā = ဆက်စပ် တင်ပြချက်; Ājānāhi = လက်ခံသည် (rule 4); vata of «vata re» = အမှန်ပင် (the vow vata keeps the pi-1
    «အကျင့်ဝတ်»); micchā = the verdict «…ti micchā» မှားသည် / «idaṃ te micchā» အမှား / the compound member
    မှားယွင်းသော (one sense per segment, the first in the Pāli); Tena hi = သို့ဖြစ်လျှင် (Tena hi P / na vattabbaṃ) or
    သို့ဖြစ်၍ (Tena hi ye kate niggahe …), the first in the text; Nanu = မဟုတ်လော; niggahetabbe / -ā = ချေပရမည့် (the
    text «… ချေပရမည်») or ချေပရသည် where the text has only «မချေပရ»; saccikaṭṭhaparamatthena = အမှန်တကယ် အဆုံးစွန်
    အနက် (the instrumental «အားဖြင့်» goes, rule 1), paramatthena = အဆုံးစွန် အနက်, atthena = အနက်, parama = အဆုံးစွန်,
    paramattho = အဆုံးစွန် အရာ, saccikaṭṭho = အမှန်တကယ် အရာ; the X-dhamma lists (khaya- / vaya- / virāga- /
    nirodhadhamma) = «Xတတ်သော သဘော … ရှိသော», the last (vipariṇāmadhamma) contiguous «… သဘော ရှိသော» (pi-2 value).
Q7. **Correlatives**: yo / yaṃ / yena = အကြင်သူ / အကြင်အရာ where the text has the correlative «အကြင်» (^5-118,
    ^5-119; pi-1 has «အကြင်» once); otherwise (no direct equivalent) (pi-1: the clause built with «…သူ / ရှိသော»).
Q8. **-ī adjectives** of the book (paṭisaṃvedī, vipākapaṭisaṃvedī, the -vādī epithets, kāmī, rūpavā) = «…သော»
    (pi-4 rule 3, parinibbāyī = ပရိနိဗ္ဗာန် ပြုသော; pi-4 paṭisaṃvedī = ခံစားသော), the text's «…သူ» normalised, even
    where my5-zeroshot-terms lists «…သူ»; agent nouns in -tar / -aka stay «…သူ» (pi-4 P6: kattā = ပြုလုပ်သူ, kāretā =
    ပြုလုပ်စေသူ, kārako = ပြုသူ); person-type names stay names (P1: dhammānusārī, kāyasakkhi, aññātāvī of pi-1).
"""

REASONS = {
    "Aññā": "the feminine «other» (aññaṃ … aññā vedanā), not aññā «final knowledge»",
    "Mānusakaṃ": "the text's «လူတို့၏ ချမ်းသာ» (my5-zeroshot-terms); pi-2 «လူ့» is another compound",
    "Sabbattha": "«everywhere» «နေရာတိုင်း» (my5-zeroshot-terms §7); pi-2 «in all planes» is another context",
    "Saṃkhittaṃ": "the editors' «(Saṃkhittaṃ)» = «(အကျဉ်းချုပ်)» (§3); pi-2 saṃkhittaṃ cittaṃ (contracted) is another sense",
    "abhiññā": "the heading noun «ထူးကဲစွာ သိခြင်း» (Abhiññānuyoga); pi-2 has the absolutive abhiññāya",
    "anuyoga": "the heading word «စစ်ဆေးမေးမြန်းခြင်း» (Ñātakānuyogādi); pi-4 P4 (cognate object) does not apply",
    "atthato": "«atthato ekaṃ» = «အဓိပ္ပာယ်အားဖြင့် တူသည်» (§6); pi-4 another sense",
    "aññatra": "«aññatra rūpā» = «ရုပ်မှ အခြား၌» (the text's word); pi-2 «လွဲ၍» another construction",
    "aṭṭhaka": "Aṭṭhakaniggaho = «ချေပချက် ရှစ်ပါးအစု» (§5); pi-2 «ရှစ်မျိုးတွဲ» is the table octad",
    "bahiddhā": "«bahiddhā nikkhamitvā» = «အပြင်သို့ ထွက်၍» (outside the body); pi-2 N10 is the qualifier «external»",
    "bhagavā": "the subject «မြတ်စွာဘုရား» (pi-1 bhagavato); pi-? «ဘုန်းတော်ရှင်» is the epithet in the iti pi so list",
    "bhattaṃ": "niccabhattaṃ «အမြဲ ထမင်း»; pi-? «ဆွမ်းစား» another compound",
    "buddha": "«buddhuppāda» = «ဘုရား ပွင့်ပေါ်ခြင်း» (the text's word)",
    "cakkhumā": "my5-zeroshot-terms «cakkhumā puggalo = မျက်စိ ရှိသော ပုဂ္ဂိုလ်»; pi-4 «sharp-sighted» another sense",
    "cakkhusamphasso": "the text has no genitive: «မျက်စိ တွေ့ထိမှု»", "manosamphasso": "likewise «မနော တွေ့ထိမှု»",
    "catukka": "Catukkanaya = «နည်း လေးပါး» (the heading); pi-2 «လေးမျိုးတွဲ» is the tetrad",
    "cavati": "the text's «စုတေ» (my5-zeroshot-terms §7 cavati = စုတေ)", "dhuvo": "the text's «ခိုင်ခံ့သော»",
    "dukkhaṃ": "pain as the opposite of pleasure «ဆင်းရဲ» (sukhadukkha, āpāyika dukkha: my5-zeroshot-terms §7 / §8); "
               "f_dukkha keeps «ဒုက္ခ» / «နာကျင်သော» where the text has them",
    "gati": "the text's «လားရာ» (Gatianuyoga); pi-2 «လားရာ ဘဝ» is not in the segment",
    "hitāya": "«attahitāya» = «မိမိ၏ အကျိုးအတွက်»; pi-? «အစီးအပွား» not in the segment",
    "iddhiṃ": "the text's «ဣဒ္ဓိ» (my5-zeroshot-terms §8)", "jāto": "the text's «မွေးဖွားလာ…»",
    "jāyati": "«jāyati jīyati mīyati» = «မွေးဖွား၊ အို၊ သေဆုံး» (birth); pi-2 «ဖြစ်ပေါ်သည်» another sense",
    "karitvā": "«appiyaṃ karitvā» = «ဦးစားမပေးဘဲ»: one Burmese verb phrase renders appiyaṃ karitvā (pi-4 P4 / pi-1 caya)",
    "karoti": "the text's verb (pi-4 had (no direct equivalent) where karoti stood only in a variant)",
    "kathā": "the heading word «ဆွေးနွေးချက်» (Xkathā = X အကြောင်း ဆွေးနွေးချက်, §2); «ဆွေးနွေးခြင်း» stays in the title",
    "koci": "a person «တစ်စုံတစ်ယောက်» (§7); pi-2 «တစ်စုံတစ်ရာ» a thing",
    "kumārikā": "the text's «သူငယ်မ»", "lohitaṃ": "the colour «အနီ»; pi-? «သွေး» (blood) another sense",
    "micchā": "Q6: the verdict «…ti micchā» = «မှားသည်»; the compound member keeps «မှားယွင်းသော»",
    "naya": "the text's «နည်း» (Catukkanaya); pi-3 M8 «ခွဲနည်း» was the pi-3 text's word",
    "nicca": "niccabhattaṃ «အမြဲ ထမင်း» (^5-238, first in the Pāli); «မြဲသော» elsewhere",
    "nikkhamitvā": "absolutive keeps «…၍» (pi-1), the text's «ထွက်၍»",
    "paccaya": "aparappaccaya «သူတစ်ပါးကို မမှီသော» (rule 8: the positive part «မှီသော»)",
    "pana": "«Idha pana» = «တစ်ဖန် ဤလောက၌» (the text has a word; pi-4 had none)",
    "para": "paracittaṃ «အခြားသူ၏ စိတ်» (the text's word); «သူတစ်ပါး» stays for paraṅkāra",
    "parama": "the frame's «အဆုံးစွန်» (paramattha); pi-2 «အမြတ်ဆုံး» another sense",
    "paṭiññāya": "the text's noun «ဝန်ခံချက်»", "puriso": "the text's «ယောက်ျား»", "puñjo": "the text's «အစုအပုံ»",
    "pātubhavanti": "the text's «ပေါ်ပေါက်»",
    "sacca": "saccavādī «မှန်သော စကားကို …»; the «အမှန်» of the segment belongs to saccikaṭṭha / vata, not sacca",
    "sama": "samabhāge «အချိုး တူသော» (sama = «တူသော»)", "samasamo": "the text's «အလွန် တူညီစွာ»",
    "sassato": "the predicate adjective «ထာဝရ တည်မြဲသော» (rule 3; puggalo sassato); the view clause keeps «…သည်»",
    "sayaṃ": "the text's «မိမိ» (sayaṃkataṃ)", "saṃvijjamāno": "the text's «ထင်ရှား ရှိနေသော»",
    "suddhika": "the heading «ရိုးရိုး နှိုင်းယှဉ်ခြင်း»", "sukhāya": "bahujanasukhāya «လူအများ၏ ချမ်းသာအတွက်» (not feeling)",
    "sāyati": "harmonise B2 F.SAYATI «လျက်» (pi-1 / pi-2 ^2-517 first); pi-1 ^1-608 «မြည်း» another passage",
    "tasmā": "the text's «…သောကြောင့်»", "taṇhā": "the sutta's «တဏှာ နှောင်ကြိုး» (^5-75); «တပ်မက်မှု» elsewhere",
    "tiṭṭhati": "the text's «တည်»", "upacchedo": "the text's «ပြတ်ခြင်း»",
    "upapajjati": "my5-zeroshot-terms §7 «ပြန်လည် ဖြစ်ပေါ်»", "upapanno": "likewise (devalokaṃ upapanno)",
    "uppajjati": "^5-230 «uppajjamāno uppajjati» = «ပေါ်ပေါက်လာ…» (CTX)", "uppādo": "the text's «ဖြစ်ခြင်း»",
    "upādā": "anupādāparinibbāna «စွဲလမ်းမှု မရှိဘဲ» (rule 8) / Upādāpaññatti «မှီ၍»; pi-1 upādā rūpa is another term",
    "vata": "Q6: «vata re» «အမှန်ပင်»; the vow keeps pi-1 «အကျင့်ဝတ်»",
    "vatthu": "the book title member «အငြင်းပွားရာ အကြောင်းအရာ» (rule 7)",
    "vedayitaṃ": "the text's «ခံစားရမှု»",
    "vipariṇāmadhammā": "the text's «ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော» (= pi-2 vipariṇāmadhammaṃ)",
    "virāga": "the list member «ပြယ်ပျောက်(တတ်သော)»; pi-2 «ပြယ်ပျောက်ခြင်း» not in the segment",
    "vādī": "Q8 / the speakers' note «မိမိဘက် / တစ်ဖက်သား» (§6); pi-2 «ပြောသော» not in the segment",
    "yaṃ": "Q7", "yena": "Q7", "yo": "Q7", "ṭhānaṃ": "diṭṭhiṭṭhānaṃ «အယူ၏ တည်ရာ» (the text's word)",
    "Abyākataṃ": "rule 6 abyākata (pi-1)", "anattā": "rule 3",
}


def write(M, out):
    import map5_rules as R
    table = collections.defaultdict(collections.Counter)
    src = collections.Counter()
    same = diffu = new = tot = 0
    diff = collections.defaultdict(collections.Counter)
    ruled = collections.Counter()
    ruled_ex = collections.defaultdict(set)
    nde = []
    for ch, (lines, _, _, nne) in out.items():
        my = R.burmese(ch)
        for l in lines:
            sid, rest = l[1:].split("] ", 1)
            for kv in rest.split(", "):
                k, v = kv.split("=", 1)
                tot += 1
                table[k][v] += 1
                src[M.SRC.get((sid, k), "?").split(":")[0]] += 1
                pv = R.prev_vals(k)
                if not pv:
                    new += 1
                elif v in pv:
                    same += 1
                else:
                    diffu += 1
                    diff[k][v] += 1
                if v == R.NONE:
                    nde.append((ch, sid, k))
                for c, r in R.presence(v, my[sid])[1]:
                    ruled[r] += 1
                    if len(ruled_ex[r]) < 6:
                        ruled_ex[r].add(f"{k} «{c}» ^{sid}")
    L = ["# pi-5 Burmese keyword mapping, PHASE 1: rules and review table (Kathāvatthu «အငြင်းပွားရာ အကြောင်းအရာများကို "
         "ဆွေးနွေးခြင်း»: preamble, 1-puggalakatha)", "",
         "Written by `map_ch1.py` (tables of the preamble and the Puggalakathā) with the shared module `map5_rules.py`. "
         "Burmese from the FINAL text of this track only (`AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_"
         "chapters`), `my5-zeroshot-terms.md` and the final pi-1 … pi-4 Burmese mappings; no other Burmese source.", "",
         "## Numbers", ""]
    for ch, (lines, _, _, nne) in out.items():
        n, bad, fails, punct, rl = R.verify_file(ch)
        L.append(f"- `{ch}.mapped.md`: {n} lines, keyword preservation `bad {bad}`, presence failures {len(fails)}, "
                 f"«, » / «၊» / « / » in a value {len(punct)}, (no direct equivalent) {nne}, chunks matched by an "
                 f"ending rule {len(rl)}.")
    L += [f"- Keyword uses {tot}: the same value as a pi-1 … pi-4 mapping for that keyword {same}; a keyword that "
          f"pi-1 … pi-4 never mapped {new}; a value different from pi-1 … pi-4 {diffu} (in {len(diff)} keywords, "
          "listed below with the reason).",
          "- Source of the values (uses): " + ", ".join(f"{k} {v}" for k, v in src.most_common()) +
          " (frame / stock = the module tables, table = the chapter table, ctx = per-segment override, pi-N = the "
          "pi-N mapping, terms = my5-zeroshot-terms, compose = members joined).", "", RULES,
          "## Frame and stock keywords (module tables, `map5_rules.FRAME` / `STOCK`) with their ch1 values", "",
          "A value «@name» in the module is a context function; the column shows the values it gave in phase 1.", "",
          "| Pāli keyword | module entry | Burmese in preamble / ch1 (uses) |", "|---|---|---|"]
    for name, tab in (("FRAME", R.FRAME), ("STOCK", R.STOCK)):
        for k, v in tab.items():
            got = table.get(k)
            shown = "; ".join(f"{x} ({c})" for x, c in got.most_common()) if got else "—"
            L.append(f"| {k} | {name}: {v if not v.startswith('@') else 'function ' + v} | {shown} |")
    L += ["", "## Values different from pi-1 … pi-4 for the same keyword", "",
          "| keyword | pi-5 value (uses) | pi-1 … pi-4 values (uses) | reason |", "|---|---|---|---|"]
    for k in sorted(diff, key=str.lower):
        pv = R.prev_vals(k)
        L.append(f"| {k} | " + "; ".join(f"{x} ({c})" for x, c in diff[k].most_common()) + " | " +
                 "; ".join(f"{x} ({c})" for x, c in pv.most_common(3)) + " | " + REASONS.get(k, "the text's word") + " |")
    L += ["", "## Presence: chunks matched by an ending rule (not literally in the segment)", "",
          "Every other chunk occurs literally in its segment's Burmese. Counts per rule, with examples:", "",
          "| rule | chunks | examples |", "|---|---|---|"]
    for r, c in ruled.most_common():
        L.append(f"| {r} | {c} | " + "; ".join(sorted(ruled_ex[r])) + " |")
    L += ["", "## (no direct equivalent)", "", "| segment | keyword | why |", "|---|---|---|"]
    why = {"karitvā": "appiyaṃ karitvā = one verb phrase «ဦးစားမပေးဘဲ» (given to appiyaṃ)",
           "suniggahitova": "only inside a Roman-script variant (pi-3 M2)",
           "ohacca": "only inside a Roman-script variant", "uhacca": "only inside a Roman-script variant",
           "sammati": "only inside a Roman-script variant", "Yo": "the text builds the clause with «…သူ» (pi-1 rule)",
           "yo": "the text builds the clause with «…သူ» (pi-1 rule)"}
    for ch, sid, k in nde:
        L.append(f"| ^{sid} | {k} | {why.get(k, 'no Burmese word in the segment')} |")
    L += ["", "## Keyword → Burmese (preamble + ch1, number of uses)", "",
          "Several values = the keyword reads differently by context (one sense per segment) or by construction.", "",
          "| Pāli keyword | Burmese (uses) |", "|---|---|"]
    for k in sorted(table, key=lambda x: x.lower()):
        L.append(f"| {k} | " + "; ".join(f"{v} ({c})" for v, c in table[k].most_common()) + " |")
    (HERE / "map-table.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("map-table.md written:", tot, "uses;", same, "same as pi-1 … pi-4;", new, "new keywords;", diffu, "different")
