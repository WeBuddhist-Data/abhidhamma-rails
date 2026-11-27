"""pi-6 Burmese rails: the bilingual-review fixes (review/report-A.md A1 … A6, report-B.md B1 … B7, report-C.md C1 … C9;
decisions in review/fix-brief.md, results in review/fix-notes.md). Model: pi-5-my/rails/apply_fixes.py (read only).

The fixes that change a frame built by one generator string are rails-layer patches (my_formulas_rails.py, families
L02 … L09: C1, B2, B4, A1, B1, A2 / B6 / C5, C6, A4). This file holds the rest, applied to the built text:
  - single-segment rules (scope = a list of segment IDs): B3, A3, A5, C7, C9;
  - frame rules (scope = every segment of the book, keyed on a Pāli frame): C2 / C3 / B5 (genitive persons before a
    moment), C4 (the restated answer's «ကြ») and B4-ext
    (F08–F10, coordinator follow-up 2026-11-23: the tesaṃ / tāsaṃ + participle apposition without «အနက်» book-wide). These frames are assembled by the lead / answer code of five
    different generators (make_ch2-02-4-5, make_ch6-8, make_ch9-10a, make_ch10b, make_ch10c), so the one place that
    reaches every repetition with one rule is the built text, keyed on the Pāli: each rule fires on every line whose
    Pāli has the frame, the same Pāli gets the same change (align_check stays at 0 differing);
  - the quote rule Q (A6 / B7 / C8): no quote mark where the Pāli has none, except the kept kinds.

usage: python3 -I -X utf8 apply_fixes.py
Run by regen_rails.sh right after apply_termbase.py (build_rails.py rewrites every chapter first, so a rebuild always
starts from the same input). Reads and rewrites AI_translation/burmese/pi-6-burmese-plain-rails_split_chapters.

Every rule, applied line by line (Pāli and Burmese lines are aligned inside each segment):
  - scope: a list of segment IDs, or None = every segment;
  - trigger: a regex the aligned Pāli line (variant brackets removed) must match, else the line is not touched;
  - change: a list of exact Burmese old → new pairs, applied in order;
  - hit: if True, each line must get exactly as many replacements as the Pāli trigger has hits;
  - expected replacement count over the whole book: the run fails (and writes nothing) if the count differs;
  - every changed line keeps its «[» / «…» / «–» / «“» / «”» counts (the quote rule only changes quote marks).
Book-wide checks (book_checks) count every instance of each pattern by script over all chapters (Pāli and Burmese;
layer families included) and require the old forms to be gone.
Every replacement is logged in rails/fixes-log.tsv (ch, id, line, old, new, rule); line = line number in the file.
Deterministic: no randomness, files and rules in fixed order.
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation/pali/pi-6_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-6-burmese-plain-rails_split_chapters"
LOG = HERE / "fixes-log.tsv"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731

AYAT = "“အာရုံခံ နယ်ပယ်များကို အတွဲလိုက် မေးဖြေခြင်း”"
DHAT = "“ဓာတ်များကို အတွဲလိုက် မေးဖြေခြင်း”"

# C2 / C3 / B5: a genitive plural of persons right before a moment phrase (no «pavatte» / place between), picked up
# by tesaṃ: the persons take «…တို့၏». (Script: the only person words that stand right before a moment phrase.)
GEN_PERS = r"(?:suddhāvāsānaṃ|arahantānaṃ|kāmāvacarānaṃ|samāpannānaṃ|anabhisametāvīnaṃ|abhisametāvīnaṃ|itaresaṃ)"
GEN_MOM = r"(?:\w+ )?\w+(?:ssa|ānaṃ|āya) (?:uppāda|bhaṅga)kkhaṇe|(?:\w+ ){1,3}vattamāne"
GEN_RX = rf"(?i)\b{GEN_PERS} (?!kāmāvacarānaṃ |suddhāvāsānaṃ )(?:{GEN_MOM})"
GEN_PAIRS = [
    # two separate groups before the Suddhāvāsa moment: the «၏» must not reach the jhāna group (Pāli lists them)
    ("ဝင်စားနေသူတို့နှင့် သုဒ္ဓါဝါသ ဘုံ၌ ရှိသူတို့၊ ဒုတိယ", "ဝင်စားနေသူတို့၊ သုဒ္ဓါဝါသ ဘုံ၌ ရှိသူတို့၏ ဒုတိယ"),
    ("သုဒ္ဓါဝါသ ဘုံ၌ ရှိသူတို့၊ ဒုတိယ", "သုဒ္ဓါဝါသ ဘုံ၌ ရှိသူတို့၏ ဒုတိယ"),
    ("သုဒ္ဓါဝါသ ဘုံ၌ ရှိသူတို့၊ ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်၏", "သုဒ္ဓါဝါသ ဘုံ၌ ရှိသူတို့၏ ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်၏"),
    ("ရဟန္တာတို့၊ စိတ်၏", "ရဟန္တာတို့၏ စိတ်၏"),
    ("ကာမဘုံ၌ ရှိသူတို့၊ နောက်ဆုံး စိတ်၏", "ကာမဘုံ၌ ရှိသူတို့၏ နောက်ဆုံး စိတ်၏"),
    ("ကာမဘုံ၌ ရှိသူတို့၊ ဝင်လေ ထွက်လေတို့၏", "ကာမဘုံ၌ ရှိသူတို့၏ ဝင်လေ ထွက်လေတို့၏"),
    ("ဝင်စားနေသူတို့၊ ဝင်လေ ထွက်လေတို့၏", "ဝင်စားနေသူတို့၏ ဝင်လေ ထွက်လေတို့၏"),
    ("သိမြင်ပြီးသူတို့၊ တပ်မက်မှု၏", "သိမြင်ပြီးသူတို့၏ တပ်မက်မှု၏"),
    ("မသိမြင်ရသေးသူတို့၊ တပ်မက်မှု၏", "မသိမြင်ရသေးသူတို့၏ တပ်မက်မှု၏"),
    ("အခြားသူတို့၊ စိတ်၏", "အခြားသူတို့၏ စိတ်၏"),
    ("အခြားသူတို့၊ ကုသိုလ်စိတ်၏", "အခြားသူတို့၏ ကုသိုလ်စိတ်၏"),
    ("အခြားသူတို့၊ ရာဂ ရှိသော စိတ်၏", "အခြားသူတို့၏ ရာဂ ရှိသော စိတ်၏"),
    ("အခြားသူတို့၊ ကုသိုလ် သဘောတရားတို့၏", "အခြားသူတို့၏ ကုသိုလ် သဘောတရားတို့၏"),
    ("အခြားသူတို့၊ အကုသိုလ် သဘောတရားတို့၏", "အခြားသူတို့၏ အကုသိုလ် သဘောတရားတို့၏"),
    ("အခြားသူတို့၊ စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့၏", "အခြားသူတို့၏ စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့၏"),
]

B4X_FC, B4X_FU, B4X_M = 10, 16, 196      # by script: = the 222 «…တို့အနက်» of the pre-fix rails outside 6-01 / 6-02

# (rule, segment ids or None or ("except", id prefix), Pāli trigger regex, [(old, new)], expected, hit)
RULES = [
    # ---------------------------------------------------------------- meaning
    ("F01 B3 ^6-6-147 uppādavāranirodhavārepi = the one combined section «ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်၌လည်း» "
     "(= ^6-6-158), not two sections",
     ["6-6-147"], r"uppādavāranirodhavārepi",
     [("ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်နှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်၌လည်း",
       "ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်၌လည်း")], 1, True),
    # ---------------------------------------------------------------- consistency (frame rules, the whole book)
    ("F02 C2 / C3 / B5 genitive persons before a moment («Suddhāvāsānaṃ dutiye citte vattamāne», «Itaresaṃ cittassa "
     "uppādakkhaṇe», «arahantānaṃ cittassa …», «(an)abhisametāvīnaṃ taṇhāya …», «… samāpannānaṃ (kāmāvacarānaṃ) "
     "assāsapassāsānaṃ …», «Kāmāvacarānaṃ pacchimacittassa …»), picked up by tesaṃ: «…တို့၏ …» (as «Sabbesaṃ cittassa "
     "bhaṅgakkhaṇe» «သူအားလုံးတို့၏ စိတ်၏ …»); «pavatte» / a place between keeps «၊» (separate items); stacked "
     "samāpannānaṃ kāmāvacarānaṃ keep the text's «…တို့နှင့် …တို့»",
     None, GEN_RX, GEN_PAIRS, 255, True),
    ("F03 C4 the restated answer «Uppajjittha.» / «Nirujjhittha.» after «… dhammā na uppajjitthāti?» takes «ကြ» as its "
     "question's verb (same subject dhammā): «ဖြစ်ပေါ်ခဲ့ကြသည်။» / «ချုပ်ငြိမ်းခဲ့ကြသည်။»",
     None, r"dhammā na (?:uppajjitth|nirujjhitth)āti\? (?:Uppajjittha|Nirujjhittha)\.",
     [("ခဲ့ကြသလော။ ဖြစ်ပေါ်ခဲ့သည်။", "ခဲ့ကြသလော။ ဖြစ်ပေါ်ခဲ့ကြသည်။"),
      ("ခဲ့ကြသလော။ ချုပ်ငြိမ်းခဲ့သည်။", "ခဲ့ကြသလော။ ချုပ်ငြိမ်းခဲ့ကြသည်။")], 30, True),
    ("F04 C7 the 9-01 padasodhana (^6-9-1 … ^6-9-8): bare abyākatā = «ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော အရာ», "
     "the number-neutral head of the majority form (bare kusalā «ကုသိုလ်», akusalā «အကုသိုလ်», na kusalā «… မဟုတ်သော "
     "အရာ»); was «… အရာများ»",
     [f"6-9-{i}" for i in range(1, 9)], r"\babyākatā(?! dhammā)",
     [("မဟုတ်သော အရာများ", "မဟုတ်သော အရာ")], 8, True),
    ("F05 C9 «၊» before «သို့သော်» in the split answers that lacked it (script: 8, the reviewer's 6 + ^6-7-122, ^6-7-148)",
     ["6-8-83", "6-8-104", "6-10-318", "6-10-387", "6-10-452", "6-10-477", "6-7-122", "6-7-148"], r"\bno ca\b",
     [("မလွန်မြောက် သို့သော်", "မလွန်မြောက်၊ သို့သော်"), ("မဖြစ်ပေါ်လိမ့်မည် သို့သော်", "မဖြစ်ပေါ်လိမ့်မည်၊ သို့သော်"),
      ("မဖြစ်ပေါ် သို့သော်", "မဖြစ်ပေါ်၊ သို့သော်"), ("ပွားများကြလိမ့်မည် သို့သော်", "ပွားများကြလိမ့်မည်၊ သို့သော်"),
      ("ဖြစ်သည် သို့သော်", "ဖြစ်သည်၊ သို့သော်"), ("ပယ်သည် သို့သော်", "ပယ်သည်၊ သို့သော်")], 8, False),
    # ---------------------------------------------------------------- minor
    ("F06 A3 ^6-4-10 the X-sadisa notes name the sections: «(… အပိုင်းသည် / အပိုင်းလည်း … အပိုင်းနှင့် တူညီသည်)»",
     ["6-4-10"], r"ghāna(?:dhātu)?sadis",
     [("(အသံသည် နှာခေါင်းနှင့် တူညီသည်)", "(အသံ အပိုင်းသည် နှာခေါင်း အပိုင်းနှင့် တူညီသည်)"),
      ("(လျှာလည်း နှာခေါင်း ဓာတ်နှင့် တူညီသည်)", "(လျှာ အပိုင်းလည်း နှာခေါင်း ဓာတ် အပိုင်းနှင့် တူညီသည်)"),
      ("(အထိအတွေ့သည် နှာခေါင်းနှင့် တူညီသည်)", "(အထိအတွေ့ အပိုင်းသည် နှာခေါင်း အပိုင်းနှင့် တူညီသည်)")], 3, True),
    ("F07 A5 ^6-4-12 «Yathā āyatanayamake paṇṇatti evaṃ dhātuyamakepi paṇṇatti» = ^6-4-17's rendering of the same sense "
     "(«X၏ သတ်မှတ်ချက်ကဲ့သို့ Y၏ သတ်မှတ်ချက်ကို(လည်း) အကျယ် ချဲ့ရမည်»; the elliptical verb as ^6-4-17 vitthāretabbā)",
     ["6-4-12"], r"dhātuyamakepi paṇṇatti",
     [(f"{AYAT}၌ သတ်မှတ်ချက် ရှိသကဲ့သို့ {DHAT}၌လည်း သတ်မှတ်ချက် ရှိသည်။",
       f"{AYAT}၏ သတ်မှတ်ချက်ကဲ့သို့ {DHAT}၏ သတ်မှတ်ချက်ကိုလည်း အကျယ် ချဲ့ရမည်။")], 1, True),
    # ---------------------------------------------------------------- coordinator follow-up 2026-11-23: B4 book-wide
    ("F08 B4-ext the apposition «yā ca itthiyo … parinibbāyissanti tāsaṃ cavantīnaṃ» without «အနက်» "
     "(as the B2 lines): «… မိန်းမတို့၊ စုတေဆဲ ထိုမိန်းမတို့» (tāsaṃ «ထိုမိန်းမတို့», as in the text)",
     ("except", "6-6-"), r"(?i)\btāsaṃ cavantīnaṃ\b",
     [("မိန်းမတို့အနက် စုတေဆဲသူတို့", "မိန်းမတို့၊ စုတေဆဲ ထိုမိန်းမတို့")], B4X_FC, True),
    ("F10 B4-ext the same with «tāsaṃ upapajjantīnaṃ»: «… မိန်းမတို့၊ ပြန်လည် ဖြစ်ပေါ်ဆဲ ထိုမိန်းမတို့» (one rule per "
     "participle, so that a line with both tāsaṃ and tesaṃ appositions changes each by its own Pāli)",
     ("except", "6-6-"), r"(?i)\btāsaṃ upapajjantīnaṃ\b",
     [("မိန်းမတို့အနက် ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့", "မိန်းမတို့၊ ပြန်လည် ဖြစ်ပေါ်ဆဲ ထိုမိန်းမတို့")], B4X_FU, True),
    ("F09 B4-ext the apposition «ye (ca) … -issanti tesaṃ cavantānaṃ / upapajjantānaṃ» (the persons named by a relative "
     "clause, picked up by tesaṃ + participle) without «အနက်», book-wide (as the B2 lines, layer L04): «…သူတို့၊ စုတေဆဲ / "
     "ပြန်လည် ဖြစ်ပေါ်ဆဲ ထိုသူတို့»; the Pāli has no partitive (no yesaṃ) in any of these lines",
     ("except", "6-6-"), r"(?i)\btesaṃ (?:cavantānaṃ|upapajjantānaṃ)\b",
     [("တို့အနက် စုတေဆဲသူတို့", "တို့၊ စုတေဆဲ ထိုသူတို့"),
      ("တို့အနက် ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့", "တို့၊ ပြန်လည် ဖြစ်ပေါ်ဆဲ ထိုသူတို့")], B4X_M, True),
]

# ---------------------------------------------------------------- the quote rule (A6 / B7 / C8)
Q_RULE = ("Q01 A6 / B7 / C8 no quote mark where the Pāli has none (section labels, chapter names and quoted answers in "
          "the notes, yāva saraṇaaraṇā); kept: the chapter / book end «“X” (ကျမ်း) ပြီးဆုံးပြီ» and the word-play glosses "
          "«“သောတ” (…)», «“ရူပ” (…)»")
Q_SPAN = re.compile(r"“([^“”]*)”")
Q_KEEP_AFTER = re.compile(r"^(?: ကျမ်း)? ပြီးဆုံးပြီ")
Q_KEEP_WORDS = {"သောတ", "ရူပ"}
Q_EXPECT = 94


def quote_fix(line):
    """-> (new line, [(old span, new span)]): drop the marks of every span that is not a kept kind; «”␣“» between two
    dropped spans (a two-item list, yāva saraṇaaraṇā) becomes «၊␣»."""
    spans = list(Q_SPAN.finditer(line))
    drop = [m for m in spans if m.group(1) not in Q_KEEP_WORDS and not Q_KEEP_AFTER.match(line[m.end():])]
    if not drop:
        return line, []
    out, pos, done = [], 0, []
    ids = {id(m) for m in drop}
    for k, m in enumerate(spans):
        if id(m) not in ids:
            continue
        out.append(line[pos:m.start()])
        inner = m.group(1)
        nxt = spans[k + 1] if k + 1 < len(spans) else None
        if nxt is not None and id(nxt) in ids and line[m.end():nxt.start()] == " ":
            out.append(inner + "၊")
            done.append((m.group(0) + " ", inner + "၊ "))
        else:
            out.append(inner)
            done.append((m.group(0), inner))
        pos = m.end()
    out.append(line[pos:])
    return "".join(out), done


def segs(lines):
    """[(id, [line indexes])] in file order."""
    out, buf = [], []
    for k, l in enumerate(lines):
        if not l.strip():
            continue
        buf.append(k)
        m = ID.search(l)
        if m:
            out.append((m.group(1), buf))
            buf = []
    return out


def marks(s, quotes=True):
    return tuple(s.count(c) for c in ("[…–“”‘’" if quotes else "[…–"))


def nobr(s):
    return re.sub(r"\s*\[[^\]]*\]", "", s)


def qcount(s, burmese):
    s = nobr(s)
    return len(re.findall(r"[“”‘’]" if burmese else r"[\"“”‘’']", s))


def book_checks(files, pali, text):
    """every instance by script; returns (errors, info lines)."""
    err, info = [], []
    pairs = [(f, k, N(nobr(p)), N(text[f][k])) for f in files for k, p in enumerate(pali[f]) if p.strip()]

    def count(rx_p, rx_m, label, ge=False):
        np_ = sum(len(re.findall(rx_p, p)) for f, k, p, m in pairs)
        nm = sum(len(re.findall(rx_m, m)) for f, k, p, m in pairs if re.search(rx_p, p))
        short = [f"{f[:-3]}:{k + 1}" for f, k, p, m in pairs if len(re.findall(rx_m, m)) < len(re.findall(rx_p, p))]
        info.append(f"{label}: Pāli {np_}, Burmese {nm}")
        if (np_ != nm and not ge) or short:
            err.append(f"{label}: Pāli {np_} ≠ Burmese {nm} {short[:6]}")

    def gone(rx_m, label):
        left = [f"{f[:-3]}:{k + 1}" for f, k, p, m in pairs if re.search(rx_m, m)]
        info.append(f"{label}: old form left on {len(left)} lines")
        if left:
            err.append(f"{label}: old form left on {left[:8]}")

    # L02 C1: every «S ṭhapetvā avasesa N, na S» keeps N; no «ကြွင်းကျန်သော အရာ(များ)သည် N ဖြစ်»
    count(r"ṭhapetvā avases(?:o|ā|aṃ) (?!na\b)(?!(?:khandhā|indriyā|āyatanā|dhātū|saccā|dhammā|puggalā)\b)\w+,? na\b",
          r"ကြွင်းကျန်သော (?!အရာ)\S+(?: \S+)?သည် ", "L02 C1 «ṭhapetvā avasesa N, na S» head noun kept")
    gone(r"ကြွင်းကျန်သော အရာ(?:များ)?သည် (?:\[[^\]]*\] )?\S+(?: \S+)? (?:\[[^\]]*\] )?ဖြစ်(?:ကြ)?သည်", "L02 C1 «ကြွင်းကျန်သော အရာ(များ)သည် N ဖြစ်»")
    # L03 / L04 B2 / B4
    count(r"(?i)anantarā kāmāvacarānaṃ pacchimacittaṃ", r"နောက်ဆုံး စိတ် \S+မည့် ကာမဘုံ၌ ရှိသူတို့", "L03 B2 kāmāvacarānaṃ pacchimacittaṃ")
    gone(r"ကာမဘုံနှင့် ဆိုင်သော နောက်ဆုံး စိတ်", "L03 B2")
    for f, k, p, m in pairs:
        if re.search(r"(?i)anantarā kāmāvacarānaṃ pacchimacittaṃ", p) and "cavantānaṃ" in p and "သူတို့အနက်" in m:
            err.append(f"L04 B4 {f[:-3]}:{k + 1}: «အနက်» left in the B2 frame")
    nr = sum(1 for f, k, p, m in pairs if re.search(r"(?i)\b(?:rūp|arūp)āvacarānaṃ pacchimacittaṃ", p))
    info.append(f"L03 B2 rūpāvacarānaṃ / arūpāvacarānaṃ pacchimacittaṃ frames: {nr}")
    # B3
    count(r"uppādavāranirodhavārepi", r"ဖြစ်ပေါ်ခြင်းနှင့် ချုပ်ငြိမ်းခြင်းအလိုက် ဖော်ပြချက်၌လည်း", "F01 B3 uppādavāranirodhavārepi")
    # L05 A1 + the sota gloss
    count(r"Piyarūpaṃ sātarūpaṃ (?:na rūpakkhandho, )?rūpaṃ", r"“ရူပ” \(ရုပ် သို့မဟုတ် သဘော\)", "L05 A1 rūpa word-play")
    count(r"(?i)Dibbasotaṃ taṇhāsotaṃ (?:na \w+, )?sotaṃ", r"“သောတ” \(နား သို့မဟုတ် ရေစီး\)", "sota word-play (kept)")
    # F02 C2 / C3 / B5
    count(GEN_RX, r"တို့၏ ", "F02 C2/C3/B5 genitive persons before a moment «…တို့၏»", ge=True)
    for f, k, p, m in pairs:
        if re.search(GEN_RX, p):
            for old, new in GEN_PAIRS:
                if old in m:
                    err.append(f"F02 {f[:-3]}:{k + 1}: «{old}» left")
    # F08 / F09 B4-ext (+ L04): the apposition tesaṃ / tāsaṃ + participle after a relative, no «အနက်» book-wide
    count(r"(?i)\b(?:tesaṃ|tāsaṃ) (?:cavant|upapajjant)\w+ (?=tesaṃ|tāsaṃ|pavatte)",
          r"တို့၊ (?:စုတေဆဲ|ပြန်လည် ဖြစ်ပေါ်ဆဲ) ထို(?:သူ|မိန်းမ)တို့", "F08/F09/L04 B4 apposition without «အနက်»")
    gone(r"တို့အနက် ", "F08/F09/L04 B4 «…တို့အနက်»")
    # F03 C4: a restated answer takes «ကြ» exactly when its question's verb has it
    c4 = 0
    for f, k, p, m in pairs:
        if re.search(r"\? [A-Z]\w+\.(?:\s|$)", p) and not re.search(r"\? (?:Āmantā|Natthi|No)\.", p):
            for q, a in re.findall(r"(\S+)လော။ ([^။]+)။", m):
                c4 += 1
                if ("ကြ" in q) != ("ကြ" in a):
                    err.append(f"F03 C4 {f[:-3]}:{k + 1}: answer «{a}» vs question «{q}»")
    info.append(f"F03 C4 restated answers checked: {c4}")
    # L06 B1
    count(r"(?:dhātuyā|vedanāya|vedanāsu),? a(?:pa)?riyāpann", r"၊ ဘဝဘုံတို့၌ အကျုံးမဝင်", "L06 B1 «၊» before the apariyāpanna item of a list")
    gone(r"နှင့် ဘဝဘုံတို့၌ အကျုံးမဝင်", "L06 B1")
    # L07 A2
    count(r"\bSabbesaṃ (?:\w+ )?\w+(?:ssa|ānaṃ) (?:uppāda|bhaṅga)kkhaṇe|\bsabbesaṃ (?:\w+ )?\w+(?:ssa|ānaṃ) (?:uppāda|bhaṅga)kkhaṇe",
          r"သူအားလုံးတို့၏ ", "L07 A2 bare Sabbesaṃ before a moment «သူအားလုံးတို့၏»", ge=True)
    gone(r"(?:^|[ ၊(])သူ အားလုံးတို့", "L07 A2 «သူ အားလုံးတို့»")
    # L08 C6
    count(r"(?i)pacchimacittaṃ (?:uppajjissati|nirujjhissati) tassa cittassa", r"မည့် ထိုစိတ်၏ ", "L08 C6 attributive «…မည့် ထိုစိတ်၏»")
    gone(r"နောက်ဆုံး စိတ် \S+လိမ့်မည်၊ ထိုစိတ်၏", "L08 C6")
    # F04 C7
    seg9 = [(f, k, p, m) for f, k, p, m in pairs if f.startswith("9-01")][:40]
    gone9 = [f"{f[:-3]}:{k + 1}" for f, k, p, m in seg9 if k < 60 and "မဟုတ်သော အရာများ" in m]
    if gone9:
        err.append(f"F04 C7 «… အရာများ» left in the padasodhana: {gone9}")
    # F05 C9
    gone(r"[^၊] သို့သော် ", "F05 C9 «သို့သော်» without «၊»")
    # L09 A4, F06 A3
    count(r"(?i)cakkaṃ bandhitabb", r"လှည့်ပတ်ခြင်းကို (?:မရောထွေးစေဘဲ )?ဖွဲ့ရမည်", "L09 A4 cakkaṃ bandhitabbaṃ")
    gone(r"အပြည့်အစုံ", "L09 A4 «အပြည့်အစုံ»")
    count(r"ghāna(?:dhātu)?sadis", r"အပိုင်း(?:သည်|လည်း) နှာခေါင်း (?:ဓာတ် )?အပိုင်းနှင့် တူညီသည်", "F06 A3 sadisa notes")
    # Q01: quote counts per line = the Pāli, except the kept kinds
    left = []
    for f, k, p, m in pairs:
        extra = sum(2 for s in Q_SPAN.finditer(nobr(m)) if s.group(1) in Q_KEEP_WORDS or Q_KEEP_AFTER.match(nobr(m)[s.end():]))
        if qcount(m, True) - extra != qcount(pali[f][k], False):
            left.append(f"{f[:-3]}:{k + 1}")
    info.append(f"Q01 lines whose quote count differs from the Pāli (kept kinds aside): {len(left)}")
    if left:
        err.append(f"Q01: quote counts differ on {left[:10]}")
    return err, info


def main():
    files = sorted(p.name for p in PALI.glob("*.md"))
    pali = {f: N((PALI / f).read_text(encoding="utf-8-sig")).split("\n") for f in files}
    text = {f: N((OUT / f).read_text(encoding="utf-8")).split("\n") for f in files}
    pseg = {f: segs(pali[f]) for f in files}
    mseg = {f: dict(segs(text[f])) for f in files}
    log, errors, counts = [], [], {}
    for rule, ids, trig, chg, expect, hit in RULES:
        trig_re = re.compile(trig)
        done, found = 0, set()
        for f in files:
            for i, pidx in pseg[f]:
                if isinstance(ids, tuple):
                    if i.startswith(ids[1]):
                        continue
                elif ids is not None and i not in ids:
                    continue
                found.add(i)
                midx = mseg[f].get(i)
                if midx is None or len(midx) != len(pidx):
                    errors.append(f"{rule[:3]}: {f} {i}: segment missing or not line-aligned")
                    continue
                for pk, mk in zip(pidx, midx):
                    np_ = len(trig_re.findall(nobr(pali[f][pk])))
                    if not np_:
                        continue
                    before, got = text[f][mk], 0
                    for old, new in chg:
                        n = text[f][mk].count(old)
                        if n:
                            text[f][mk] = text[f][mk].replace(old, new)
                            got += n
                            log += [(f[:-3], i, str(mk + 1), old, new, rule.split(" ")[0])] * n
                    if hit and got != np_:
                        errors.append(f"{rule[:3]}: {f[:-3]} {i} line {mk + 1}: {got} replacements, Pāli {np_}")
                    if marks(before) != marks(text[f][mk]):
                        errors.append(f"{rule[:3]}: {f[:-3]} {i} line {mk + 1}: «[ … – “ ”» counts changed")
                    done += got
        if isinstance(ids, list) and found != set(ids):
            errors.append(f"{rule[:3]}: segments not found: {sorted(set(ids) - found)}")
        counts[rule] = done
        if done != expect:
            errors.append(f"{rule[:3]}: {done} replacements, expected {expect}")
    # the quote rule: every line whose Burmese has more quote marks than its Pāli
    qdone = 0
    for f in files:
        for i, pidx in pseg[f]:
            for pk, mk in zip(pidx, mseg[f].get(i, [])):
                p, m = pali[f][pk], text[f][mk]
                if qcount(m, True) <= qcount(p, False):
                    continue
                if qcount(p, False):
                    errors.append(f"Q01: {f[:-3]} {i} line {mk + 1}: the Pāli has quotes too (not handled)")
                    continue
                new, done = quote_fix(m)
                if done:
                    if marks(m, False) != marks(new, False):
                        errors.append(f"Q01: {f[:-3]} {i} line {mk + 1}: «[ … –» counts changed")
                    text[f][mk] = new
                    qdone += len(done)
                    log += [(f[:-3], i, str(mk + 1), o, n, "Q01") for o, n in done]
    counts[Q_RULE] = qdone
    if qdone != Q_EXPECT:
        errors.append(f"Q01: {qdone} spans, expected {Q_EXPECT}")
    berr, info = book_checks(files, pali, text)
    errors += berr
    for rule, n in counts.items():
        print(f"{n:6d}  {rule[:110]}")
    for x in info:
        print(f"        check: {x}")
    if errors:
        print("\n".join(errors[:40]))
        print(f"{len(errors)} errors")
        sys.exit(1)
    for f in files:
        (OUT / f).write_text("\n".join(text[f]), encoding="utf-8")
    with open(LOG, "w", encoding="utf-8") as fh:
        fh.write("ch\tid\tline\told\tnew\trule\n")
        for row in log:
            fh.write("\t".join(row) + "\n")
    print(f"{len(RULES) + 1} rules; {len(log)} replacements; {len({(r[0], r[2]) for r in log})} lines changed")


main()
