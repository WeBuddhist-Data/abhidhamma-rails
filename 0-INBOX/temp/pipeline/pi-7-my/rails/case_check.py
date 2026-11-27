"""pi-7 Burmese rails: the CASE CHECK of the pañhāvāra example clauses (review/fix-brief.md, B1–B9, A1, C1).

Every Pāli clause «SUBJ DAT Xpaccayena paccayo» (also inside «…»-cut lists and after «–») is paired with its Burmese
clause «SUBJ-သည် / SUBJ-လည်းကောင်း … DAT-အား … Xဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်» on the aligned line (the n-th
«paccayena paccayo» of a Pāli line = the n-th «အကြောင်းဖြင့် အကြောင်း (မ)ဖြစ်» of its Burmese line; the two counts are
equal on every line).

Pāli side (by script, no lexicon): the clause starts after «– », «. », «; », «, », «? » or the previous clause; the
words before the condition word are split at the first genitive / dative word (-ssa, -ānaṃ, -īnaṃ, -ūnaṃ, -nnaṃ,
-esaṃ, -āya, -iyā, -uyā, with «-ñca» / «ca»; nominative neuters jhānaṃ, nibbānaṃ, dānaṃ … are not genitive): before =
the conditioning subject, from there = the conditioned recipients. Items are counted per «…»-segment by «ca»: a
segment whose first word carries «ca» / «-ñca» has one item per «ca», else one more («tiṇṇannaṃ khandhānaṃ X-assa ca
Y-ānañca rūpānaṃ» = 3; «ceva … na ca» is one item).

Burmese side: the recipients are the last D items marked «…အား» before the condition name (D = the Pāli count).
A clause is LEFT (an error) when:
  - S0  the Pāli has a subject but the Burmese text before the first recipient does not end in a subject marker
        «သည်» / «လည်းကောင်း» (subject dropped, merged into the recipients, or marked «ကို» / left an adjective);
  - S1  a single Pāli subject («X» with no «ca» in its last segment) ends in «လည်းကောင်း» where no co-subject is
        written, or a co-subject list («X ca Y ca», «X Y-ñca») has fewer «လည်းကောင်း» items than the Pāli (nor the
        shared-head «A Nနှင့် B Nတို့သည်» form);
  - D0  the Burmese clause has more «…အား» items than the Pāli recipients (a conditioning item put among them);
  - D1  fewer «…အား» items than the Pāli recipients (a recipient dropped / merged), where the Pāli recipients are not
        joined by «နှင့်» in the Burmese (the shared-head «A Nနှင့် B Nအား» of the titles).
usage: case_check.py [chapter-folder] [--list]   (default: the rails folder; prints «case check: N clauses, L left»)
Importable: run(folder) -> (n_clauses, [left rows]).
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
RAILS = ROOT / "AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters"
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731

P_COND = re.compile(r"(?:\bna )?\b(\w+) ?paccayena paccay[oa]\b")
B_COND = re.compile(r"(?:\S+ ){0,6}?\S*ဟူသော အကြောင်းဖြင့် အကြောင်း (?:မ)?ဖြစ်")
B_COND_END = re.compile(r"အကြောင်းဖြင့် အကြောင်း (?:မ)?ဖြစ်(?:သည်|ကြသည်)?")
P_START = re.compile(r"(?:– |\. |; |, |\? |^)")
NOM_NAANAM = {"jhānaṃ", "nibbānaṃ", "dānaṃ", "ṭhānaṃ", "pahānaṃ", "upādānaṃ", "nidānaṃ", "vodānaṃ", "ñāṇaṃ",
              "jhānañca", "nibbānañca", "upādānañca", "pāṇaṃ"}
GEN_END = re.compile(r"(?:ssa|ānaṃ|īnaṃ|ūnaṃ|nnaṃ|esaṃ|āya|iyā|uyā|ssāpi|ānampi|ssa\)?)$")
SKIP_W = {"kesañci", "aññamaññaṃ", "kiñci", "kāle", "na", "pi"}
DAT = re.compile(r"(?<=[^\s၊…])အား(?=လည်းကောင်း|[\s၊…]|$)")


def core(w):
    return w.replace("…pe…", "…").strip("…,.;()").replace("…", "")


def is_gen(w):
    c = core(w)
    if c.endswith("sseva"):
        c = c[:-3] + "a"                            # tasseva = tassa + eva
    if c.endswith("ñceva"):
        c = c[:-5] + "ṃ"
    if c.endswith("ñca"):
        c = c[:-3] + "ṃ"
    if c in NOM_NAANAM or c.lower().endswith(("ndriyā", "dānaṃ", "jhānaṃ", "pahānaṃ")):
        return False                                # nominative neuters in «-ānaṃ» (adinnādānaṃ, upādānaṃ …)
    return bool(GEN_END.search(c))


HEADS = ("khandh", "dhamm", "het", "citt", "cetan", "moh", "lobh", "paṭigh", "dos", "vitakk", "vicār", "paññ",
         "patthan", "senāsan", "sukh", "dukkh", "āsav", "kiles", "upādān", "ganth", "saññojan", "nīvaraṇ",
         "indriy", "adhipat", "āhār", "magg", "phal", "jhān", "vuṭṭhān", "gotrabh", "vodān", "āvajjan", "samāpatt",
         "dhāt", "viññāṇ", "ñāṇ", "āyatan", "mahābhūt", "rūp", "kāy", "vedan", "parikamm", "bhavaṅg", "diṭṭh",
         "avijj", "vatth", "anulom", "cakkh", "aṅg", "paṭisambhid", "kosall", "sīl", "sut", "cāg", "saddh", "rāg", "mān", "ut", "bhojan",
         "parāmās", "abhijjh", "byāpād", "pīt", "upekkh", "sot", "ghān", "jivh", "man", "ndriy")
ADJ_RE_PLACEHOLDER = None
NOCLOSE = re.compile(r"^(?:dhamm|sampayutt|vippayutt|sahagat|taṃsampayutt)")
ADJ_FEM = {"sukhāya", "dukkhāya", "adukkhamasukhāya", "nasukhāya", "nadukkhāya", "naadukkhamasukhāya"}
ENDS = ("ānaṃ", "īnaṃ", "ūnaṃ", "assa", "ussa", "issa", "ssa", "āya", "iyā", "uyā", "āni", "aṃ", "uṃ", "iṃ", "o",
        "ā", "e", "u", "ū", "i", "ī")


ADJ_EXTRA = {"sāsav", "anāsav", "sārammaṇ", "anārammaṇ", "sappaccay", "appaccay", "sauttar", "anuttar"}
ADJ_RE = None
HEAD_A = {"alobh", "ados", "amoh", "abhijjh", "avijj", "anulom", "abyāpād", "anottapp", "ahirik"}


def _adj_re():
    h = "|".join(sorted(HEADS, key=len, reverse=True))
    return re.compile(r"(?:(?:sa|sap|sam|a|ap|an|na|no|naa|nasa|nava)(?:" + h + r")(?:a|ā)?)+")


def is_head(t):
    global ADJ_RE
    if ADJ_RE is None:
        ADJ_RE = _adj_re()
    t = t.lower()
    if t.endswith("ñca"):
        t = t[:-3] + "ṃ"
    if "dhammadhamm" in t or "nidassan" in t or "ppaṭigh" in t:
        return False
    if t in ADJ_FEM or t.endswith(("sahagatā", "sahagatānaṃ", "sahagato", "sampayuttakānaṃ", "sampayuttā",
                                    "sampayutto", "sampayuttassa")):
        return False
    stems = []
    if t.endswith("ānaṃ"):
        stems.append(t[:-2])                        # nominative «-ānaṃ» (upādānaṃ) as well as genitive plural
    for e in ENDS:
        if t.endswith(e) and len(t) > len(e) + 1:
            stems.append(t[:-len(e)])
            break
    for st in stems or [t]:
        if st in HEAD_A:
            return True
        if ADJ_RE.fullmatch(st) or st in ADJ_EXTRA:
            continue                                # bahubbīhi / negated adjectives: savitakka, sappaṭigha, nahetu …
        if st.endswith(HEADS):
            return True
    return False


def stem(t):
    t = t.lower()
    if t.endswith("ñca"):
        t = t[:-3] + "ṃ"
    for e in ENDS:
        if t.endswith(e) and len(t) > len(e) + 1:
            return t[:-len(e)]
    return t


EXCL_PAIRS = {("ajjhattik", "bāhir"), ("ajjhatt", "bahiddh"), ("upādinn", "anupādinn")}


def exclusive(a, b):
    """two qualifiers that cannot both hold of one thing: X / no-X, sa-X / a-X, …"""
    sa, sb = stem(a), stem(b)
    if (sa, sb) in EXCL_PAIRS or (sb, sa) in EXCL_PAIRS:
        return True
    for x, y in ((sa, sb), (sb, sa)):
        if x != y and x.endswith(y) and x[:len(x) - len(y)] in ("no", "na", "a", "an", "s", "sa", "nava", "ne"):
            return True
        if x != y and y.endswith(x) is False:
            pass
    return False


def count_items(words, gen_list=None):
    """conjuncts of a list (one «…» / comma segment): a conjunct closes after a head noun that is followed by more
    words; «ca» / «-ñca» (after its first word or after the conjunct) marks it; a last bare head after marked conjuncts
    is their shared head («hetussa ca nahetussa ca dhammassa» = 2); «X ceva Y ca» is one item; «A ca B ca N» with two
    qualifiers that can both hold (pītisahagatā ca sukhasahagatā ca khandhā) is one item, with exclusive ones
    (ajjhattikā ca bāhirā ca, X ca noX ca) two. In a subject list a genitive modifier never closes a conjunct."""
    toks = [core(w) for w in words]
    toks = [t for t in toks if t]
    if not toks:
        return 0
    if "ceva" in toks or any(t.endswith("ñceva") for t in toks):
        return sum(1 for t in toks if t == "ceva" or t.endswith("ñceva"))
    flags = []                                      # [(word, marked)]
    for t in toks:
        if t == "ca":
            if flags:
                flags[-1] = (flags[-1][0], True)
            continue
        flags.append((t, t.endswith("ñca")))
    if not any(m for _, m in flags):
        return 1                                    # no «ca»: one item (an asyndetic list is one Burmese list)
    # «A ca B ca N» qualifier pair
    ws = [t for t, _ in flags]
    marks = [m for _, m in flags]
    for k in range(len(flags) - 2):
        if marks[k] and marks[k + 1] and not is_head(ws[k]) and not is_head(ws[k + 1]) and \
                not exclusive(ws[k], ws[k + 1]):
            if not marks[k + 2]:
                flags[k + 1] = (ws[k + 1], False)   # one item: both qualifiers hold of N
    n, cur, cur_marked, any_marked = 0, 0, False, False
    for k, (t, m) in enumerate(flags):
        cur += 1
        cur_marked = cur_marked or m
        last = k == len(flags) - 1
        nxt = flags[k + 1] if not last else None
        if gen_list is False and is_gen(t):
            continue                                # a genitive modifier inside a subject conjunct
        if is_head(t) and not last and not (NOCLOSE.match(nxt[0].lower()) and not nxt[1]) \
                and not (is_head(nxt[0]) and not nxt[1]) and not APPOS.search(nxt[0]):
            n += 1
            any_marked = any_marked or cur_marked
            cur, cur_marked = 0, False
    if cur:
        shared = cur == 1 and not cur_marked and any_marked and n >= 1
        if not shared:
            n += 1
        cur_marks = sum(1 for _, m in flags[len(flags) - cur:] if m)
        n += max(0, cur_marks - 1)                  # «A ca B ca N» in the last conjunct: one item per qualifier
    return max(n, 1, sum(1 for _, m in flags if m))


APPOS = re.compile(r"^\w*kāyagant")


def segments(words):
    """split a word list at «…» / «…pe…» cuts and at commas: -> [[words]]"""
    segs, cur = [], []
    for w in words:
        cut_after = w.endswith("…") or w.endswith("…pe…") or w.endswith(",")
        cut_before = w.startswith("…")
        if cut_before and cur:
            segs.append(cur)
            cur = []
        cur.append(w)
        if cut_after:
            segs.append(cur)
            cur = []
    if cur:
        segs.append(cur)
    return segs


def units(words):
    """split at «…» / «…pe…» cuts only (the Burmese «…»): -> [[words]]"""
    segs, cur = [], []
    for w in words:
        if w in ("…", "…pe…"):                     # a free-standing cut closes the unit
            if cur:
                cur[-1] = cur[-1] + "…"
                segs.append(cur)
                cur = []
            elif not segs:
                segs.append([w])
            continue
        if w.startswith("…") and cur:
            segs.append(cur)
            cur = []
        cur.append(w)
        if w.endswith("…") or w.endswith("…pe…"):
            segs.append(cur)
            cur = []
    if cur:
        segs.append(cur)
    return segs


def pali_clauses(line):
    """-> [(clause text, [unit word lists])] for every «Xpaccayena paccayo» of the line. A clause starts after
    «– », «. », «; », «? » or the previous clause, and after «, » unless a genitive follows (a comma list of
    recipients «gotrabhussa, vodānassa, …»)."""
    out, prev = [], 0
    for m in P_COND.finditer(line):
        txt = line[prev:m.start()]
        prev = m.end()
        starts = [x.end() for x in P_START.finditer(txt)
                  if not (x.group(0) == ", " and txt[x.end():].split(" ")[0] and is_gen(txt[x.end():].split(" ")[0]))]
        st = max(starts) if starts else 0
        clause = txt[st:]
        clause = re.sub(r"\([^)]*\)", " ", clause)
        words = [w for w in clause.split() if core(w) not in SKIP_W or w.endswith("…")]
        out.append((clause.strip(), units(words)))
    return out


def burmese_clauses(line):
    """-> [text before each condition phrase, from the previous condition phrase]"""
    out, prev = [], 0
    for m in B_COND_END.finditer(line):
        out.append(line[prev:m.start()])
        prev = m.end()
    return out


SUBJ_MARK = re.compile(r"(?<!အား)(?:သည်|လည်းကောင်း)(?=[ …]|$)(?! မဟုတ်)")


NEUTRAL = re.compile(r"^(?:n?a?(?:neva)?dassanena|n?a?bhāvanāya|nevadassanena|nirodhā|jhānā|maggā|kaṭattā|"
                     r"\w*kkhaṇe|\w*kkhaṇepi|n?o?upādā|\w+ena|bahiddhā|ajjhattaṃ|ajjhattā|\w+e)$", re.I)


def wclass(w):
    c = core(w)
    if not c or c in ("ca", "ceva", "no", "nana"):
        return "c"
    if NEUTRAL.match(c):
        return "x"
    return "g" if is_gen(w) else "n"


def split_unit(u):
    """dat = the trailing run of genitive / neutral words (with «ca») holding a genitive; subj = the words before
    (a genitive modifying a nominative subject, «paṭhamassa maggassa parikammaṃ», stays in the subject)."""
    cl = [wclass(w) for w in u]
    k = len(u)
    while k > 0 and cl[k - 1] in "gxc":
        k -= 1
    while k < len(u) and cl[k] == "c":          # a «ca» right after the subject closes the subject
        k += 1
    if "g" not in cl[k:]:
        return u, []
    # the sukhāya-vedanāya type: «X-āya vedanāya sampayutto» is a subject qualifier (the run ends at a nominative)
    subj = u[:k]
    while subj and wclass(subj[0]) == "x":
        subj = subj[1:]
    return subj, u[k:]


SUBJ_MARK2 = re.compile(r"(?<!အား)(?:သည်|လည်းကောင်း)(?:(?=[ …]|$)(?! မဟုတ်)|၊(?= ))")


def check_clause(pc, bc):
    """-> [(code, Pāli unit, Burmese unit)] for one clause pair."""
    ptxt, us = pc
    out = []
    if us and us[-1] and us[-1][-1].endswith("…"):
        us = us + [[]]                              # «X… Ypaccayena»: the Burmese «…» before the condition name
    if not any(split_unit(u)[1] for u in us):
        return out
    rs = max([0] + [m.end() for m in re.finditer(r"– |။ ", bc)])
    reg = bc[rs:].rstrip()
    reg = re.sub(r"\S*ဟူသော$", "", reg)
    bu = reg.split("…")
    if len(bu) < len(us):
        return [("UNITS", ptxt, reg)]
    bu = ["…".join(bu[:len(bu) - len(us) + 1])] + bu[len(bu) - len(us) + 1:]
    for k, (u, b) in enumerate(zip(us, bu)):
        errs = []
        subj, dat = split_unit(u)
        has_subj = bool([w for w in subj if core(w)])
        d_items = sum(count_items(s) for s in segments(dat)) if dat else 0
        if not dat:
            if DAT.search(b) and not any((re.search(r"(?:paccay|upanissay)\w*…", w) or re.search(r"\w(?:ti|nti)$", core(w))) for w in u):
                out.append(("D0s", " ".join(u), b))
            continue
        # the subject marker: the last «သည်» / «လည်းကောင်း» (also «လည်းကောင်း၊») before the first recipient
        fd = list(DAT.finditer(b))
        first = fd[-min(len(fd), d_items)].start() if fd and d_items else len(b)
        vb = [m.end() for m in re.finditer(r"(?:ကြ၏|ကြသည်|သည်)၊ ", b[:first])]
        b0 = max(vb) if vb else 0
        sm = [m for m in SUBJ_MARK2.finditer(b) if b0 <= m.start() and m.end() <= first]
        after = b[sm[-1].end():] if (sm and has_subj) else b
        nb = len(DAT.findall(after))
        joins = len(re.findall(r"၊|နှင့်", after))
        if has_subj and not sm:
            errs.append("S0")
        if has_subj and sm and sm[-1].group(0).endswith("၊"):
            errs.append("S2")
        d_hi = sum(max(count_items(sg), sum(1 for w in sg if core(w) and is_head(core(w)))) for sg in segments(dat))
        if nb > d_hi:
            errs.append("D0")
        cut_end = dat[-1].endswith("…") or dat[-1].endswith("…pe…")
        if (nb + joins < d_items or (d_items and not nb)) and not cut_end:
            errs.append("D1")
        if has_subj and sm:
            s_items = count_items(segments(subj)[-1], gen_list=False)
            seg_b = b[b0:sm[-1].end()]
            n_lk = len(re.findall(r"(?<!အား)လည်းကောင်း", seg_b))
            if s_items >= 2 and n_lk < s_items and not re.search(r"နှင့် .*တို့သည်$", seg_b):
                errs.append("S1")
            if s_items == 1 and n_lk >= 2:
                errs.append("S1")
        for e in errs:
            out.append((e, " ".join(u), b))
    return out


# units kept as they are, with the reason (reported as «explained», not «left»)
EXPLAINED = {
    "Sekkhā phalasamāpattiyā kāyikassa sukhassa":
        "2-06 ^7-12-53 source oddity: the only nominative is the persons «sekkhā», which cannot be the condition; the "
        "text reads «the trainees' fruition attainment» (genitive of persons, as «ariyānaṃ» elsewhere)",
}


def run_texts(texts):
    """texts: {file name: Burmese text} -> (n clauses, [left rows]); explained rows are dropped (see EXPLAINED)."""
    rows, n = [], 0
    for p in sorted(PALI.glob("*.md")):
        pl = N(p.read_text(encoding="utf-8-sig")).split("\n")
        bl = N(texts[p.name]).split("\n")
        for k, (a, b) in enumerate(zip(pl, bl), 1):
            pcs = pali_clauses(a)
            if not pcs:
                continue
            bcs = burmese_clauses(b)
            if len(bcs) != len(pcs):
                rows.append((p.name[:-3], k, "ALIGN", f"{len(pcs)} vs {len(bcs)}", ""))
                continue
            for pc, bc in zip(pcs, bcs):
                n += 1
                for code, pu, bu in check_clause(pc, bc):
                    if pu.strip() in EXPLAINED:
                        continue
                    rows.append((p.name[:-3], k, code, pu.strip(), bu.strip()))
    return n, rows


def run(folder=RAILS):
    return run_texts({p.name: (folder / p.name).read_text(encoding="utf-8") for p in sorted(PALI.glob("*.md"))})


if __name__ == "__main__":
    folder = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else RAILS
    if not folder.is_absolute():
        folder = ROOT / folder
    n, rows = run(folder)
    if "--list" in sys.argv:
        for r in rows:
            print("\t".join(map(str, r)))
    print(f"case check: {n} clauses, {len(rows)} left ({len(EXPLAINED)} explained)")
