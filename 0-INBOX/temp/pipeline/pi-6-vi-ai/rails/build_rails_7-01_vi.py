"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 7-01 (Anusayayamaka: uppattiṭṭhānavāra + anusayavāra, anuloma)
and the FAMILY C module (anusayayamaka) that chapters 7-02 … 7-11 import.

Import READ-ONLY (importing writes nothing; outputs are written only under `if __name__ == "__main__":`):
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; C = importlib.import_module("build_rails_7-01_vi")

What the module gives later chapters (all byte-fixed; never retype the strings):
  ANUSAYA / anusaya_of()          the seven tendencies (every case form) → Vietnamese name
  VERB / verb_of()                anuseti / anusenti / nānuseti / nānusenti (+ the -ti question forms)
  FAMILY_TERMS                    termbase strings of the other family-C verbs and adjectives (sānusayo, pajahati …)
  PERSON_GEN / PLACE_LOC / PRON   answer heads (persons, places, resumptive pronouns)
  pair_q() / kattha_q()           the shared person / place question shell (coordinator) and «… ở đâu?»
  parse_tp() / tp_vi()            a run of tendencies: "A ca B ca", "A…pe… B", "A ca…pe… F ca"
  parse_clause() / clause_vi()    "<tendencies> <verb>" (one group) and the both-frame "A ca V B ca V"
  neg_clause_vi()                 the "no ca <pron> …" part ("neither" frame for lists; «vẫn» for a negative verb)
  sentence() / answers()          one answer sentence / a run of them
  question()                      a whole yassa / yattha / yassa yattha question line (+ its answers)
  MULAKA / mulaka_label()         (Ekamūlakaṃ) … (Chakkamūlakaṃ) closing labels (pi-3)
  heading()                       chapter headings (S.LATER_HEADINGS + FAMILY_HEADINGS from the termbase)
  tr_line() / build() / write()   the line translator and writer (S's per-line checks)
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_7-01_vi.py
"""
import pathlib
import re
import sys
import unicodedata

RAILS_DIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
if str(RAILS_DIR) not in sys.path:
    sys.path.insert(0, str(RAILS_DIR))
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)

CHAPTER = "7-01-anusayayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-7-01.md"
ADH_DIR = RAILS_DIR / "adh-7-01"
cap = S.cap

# ---------------------------------------------------------------------------------------------------------------
# 1. The seven tendencies (pi-6 termbase; = pi-2 16-nanavibhango / 17-khuddakavatthuvibhango, pi-5 2-parihanikatha)
# ---------------------------------------------------------------------------------------------------------------
ANUSAYA = {   # key = Pāli stem before -ānusay-  →  Vietnamese name (the same in every case form)
    "kāmarāg": "khuynh hướng tiềm ẩn tham đắm dục lạc",
    "paṭigh": "khuynh hướng tiềm ẩn ác cảm",
    "mān": "khuynh hướng tiềm ẩn kiêu mạn",
    "diṭṭh": "khuynh hướng tiềm ẩn quan điểm",
    "vicikicch": "khuynh hướng tiềm ẩn hoài nghi",
    "bhavarāg": "khuynh hướng tiềm ẩn tham đắm hiện hữu",
    "avijj": "khuynh hướng tiềm ẩn vô minh",
}
STEM_SLIPS = {"kāmārāg": "kāmarāg"}        # kāmārāgānusayo (7-01 ^6-7-21, ^6-7-25): spelling slip, rendered as meant
ANUSAYA_CASES = ("o", "ena", "aṃ", "añca", "āti", "oti")   # nominative, instrumental, accusative, acc. + ca, -ti
ANUSAYA_RE = re.compile(r"(" + "|".join(list(ANUSAYA) + list(STEM_SLIPS)) + r")ānusay(" +
                        "|".join(sorted(ANUSAYA_CASES, key=len, reverse=True)) + r")")
SATTANUSAYA = "Bảy khuynh hướng tiềm ẩn"   # Sattānusayā (pi-2)
# Sattānusayā – kāmarāgānusayo, … avijjānusayo.  (pi-2 16-nanavibhango ^2-816, identical Pāli)
SATTANUSAYA_LINE = f"{SATTANUSAYA} – " + ", ".join(ANUSAYA.values()) + "."

SLIPS_SEEN = []                             # (Pāli word, as meant) collected while building, printed by main()


def anusaya_of(word):
    """'kāmarāgānusayo' / 'mānānusayena' / 'diṭṭhānusayaṃ' … → Vietnamese name; anything else raises."""
    m = ANUSAYA_RE.fullmatch(word)
    if not m:
        raise ValueError(f"not a tendency word: {word!r}")
    stem = m.group(1)
    if stem in STEM_SLIPS:
        SLIPS_SEEN.append((word, word.replace(stem, STEM_SLIPS[stem], 1)))
        stem = STEM_SLIPS[stem]
    return ANUSAYA[stem]


def is_anusaya(word):
    return bool(ANUSAYA_RE.fullmatch(word))


# ---------------------------------------------------------------------------------------------------------------
# 2. Verbs. anuseti «nằm sẵn», nānuseti «không nằm sẵn» (termbase). Number is checked against the subject.
# ---------------------------------------------------------------------------------------------------------------
LIE_LATENT = "nằm sẵn"                     # anuseti / anusenti (pi-2 «… nằm sẵn»)
VERB = {     # Pāli → (Vietnamese, number 1 / 2, positive?)
    "anuseti": (LIE_LATENT, 1, True), "anusenti": (LIE_LATENT, 2, True),
    "nānuseti": ("không " + LIE_LATENT, 1, False), "nānusenti": ("không " + LIE_LATENT, 2, False),
}
VERB_POSITIVE = {"nānuseti": "anuseti", "nānusenti": "anusenti"}
VERB_SLIPS = {"anusanti": "anusenti"}      # 7-01 ^6-7-34 … ^6-7-35 last line: slip, rendered as meant
VERB_RE = re.compile(r" (" + "|".join(sorted(list(VERB) + list(VERB_SLIPS), key=len, reverse=True)) + r")(?= |$)")
STILL = "vẫn"                              # after "no ca" a negative verb is denied: «vẫn nằm sẵn» (coordinator)

# Other family-C verbs and adjectives, termbase / coordinator wording (for 7-03 … 7-11; frames set by those agents
# with the helpers below; listed here so every chapter takes the same strings).
FAMILY_TERMS = {
    "sānusayo": "có",                       # + the tendency: «có khuynh hướng tiềm ẩn …» (coordinator: sānusayo «có»)
    "niranusayo": "không có",
    "pajahati": "dứt bỏ", "nappajahati": "không dứt bỏ", "nappajahissanti": "sẽ không dứt bỏ",
    "parijānāti": "hiểu biết trọn vẹn", "na parijānāti": "không hiểu biết trọn vẹn",
    "pahīno": "đã được dứt bỏ", "appahīno": "chưa được dứt bỏ",
    "uppajjati": "sinh khởi", "uppajjittha": "đã sinh khởi", "uppajjissati": "sẽ sinh khởi",   # family B (2-01)
    "upapajjati": "tái sinh",
    "na vattabbo": "không nên nói là",
    "Natthi (in 7-11: anusayā bhaṅgā natthi)": "không có",
    "bhaṅgā": "phải phân chia",
    "kassaci": "ở một số chúng sinh",
}


def strip_ti(word):
    """Question-final word with the quotation particle: anusetīti → anuseti, anusentīti → anusenti,
    pahīnoti → pahīno, sānusayāti → sānusayā. Raises if there is no -ti."""
    if word.endswith("īti"):
        return word[:-3] + "i"
    if word.endswith(("oti", "āti")):
        return word[:-2]
    raise ValueError(f"no -ti on question word {word!r}")


def verb_of(word):
    """Pāli verb → (Vietnamese, number, positive?, positive Vietnamese)."""
    if word in VERB_SLIPS:
        SLIPS_SEEN.append((word, VERB_SLIPS[word]))
        word = VERB_SLIPS[word]
    if word not in VERB:
        raise ValueError(f"unknown verb {word!r}")
    vi, num, pos = VERB[word]
    return vi, num, pos, VERB[VERB_POSITIVE.get(word, word)][0]


# ---------------------------------------------------------------------------------------------------------------
# 3. Answer heads: persons (genitive), places (locative), pronouns. Termbase + pi-1 … pi-5 rails.
# ---------------------------------------------------------------------------------------------------------------
PERSON_GEN = {   # Pāli (sentence-initial form) → (Vietnamese, number)
    "Anāgāmissa": ("bậc không trở lại", 1),            # termbase
    "Puthujjanassa": ("người phàm phu", 1),            # termbase (pi-1, pi-5 «người phàm phu»)
    "Arahato": ("bậc A-la-hán", 1),                    # termbase (arahato as a person in the Anusayayamaka)
    "Dvinnaṃ puggalānaṃ": ("hai hạng người", 2),       # pi-4 «hai hạng người»
    "Tiṇṇaṃ puggalānaṃ": ("ba hạng người", 2),
    "Catunnaṃ puggalānaṃ": ("bốn hạng người", 2),
    "Tesaññeva puggalānaṃ": ("chính những hạng người ấy", 2),   # tesaṃyeva «chính những người ấy» + puggala
    "Tesaṃyeva puggalānaṃ": ("chính những hạng người ấy", 2),
    "Tasseva puggalassa": ("chính hạng người ấy", 1),
}
PLACE_LOC = {    # Pāli (lower-case first letter) → Vietnamese (each place keeps its own «ở»)
    "kāmadhātuyā dvīsu vedanāsu": "hai loại cảm giác trong cõi dục lạc",   # dvīsu vedanāsu «hai loại cảm giác»
    "kāmadhātuyā tīsu vedanāsu": "ba loại cảm giác trong cõi dục lạc",     # tīsu vedanāsu «ba loại cảm giác»
    "dukkhāya vedanāya": "cảm giác khó chịu",                              # (pi-1)
    "rūpadhātuyā": "cõi hình sắc",
    "arūpadhātuyā": "cõi không hình sắc",
    "sabbasakkāyapariyāpannesu dhammesu": "tất cả các hiện tượng nằm trong tự ngã",   # sakkāya «tự ngã», pariyāpanna «nằm trong» (pi-5)
}
AT = "ở"
PRON = {"tassa": "người ấy", "tesaṃ": "những người ấy", "tattha": "nơi ấy"}   # resumptive / "no ca" pronouns
ETTHA = "thì ở đó"                          # ettha (pi-2 «thì ở đó … nằm sẵn»)
THEN = "thì"
BUT = "nhưng"                               # no ca
ALSO = "cũng"                               # both-frame: «A nằm sẵn, B cũng nằm sẵn»
NEITHER_FIRST, NEITHER_NEXT = "không có", "cũng không có"   # "no ca A ca B ca V" = «không có A, cũng không có B V»
AND = "và"

# answers
YES = S.YES                                 # Āmantā. «Đúng vậy.» (pi-5)
ANS_NO = "Không."                           # No.
ANS_NATTHI = "Không có."                    # Natthi. (pi-3, termbase «không có»)
EXACT = {"Āmantā.": YES, "No.": ANS_NO, "Natthi.": ANS_NATTHI}


def pron_vi(pron):
    """'tassa' / 'tesaṃ' / 'tattha' / 'tassa tattha' / 'tesaṃ tattha' → «người ấy» … «người ấy, ở nơi ấy»."""
    return f", {AT} ".join(PRON[w] for w in pron.split())


# ---------------------------------------------------------------------------------------------------------------
# 4. The shared person / place question shell (rails-coordinator-rules.md) and the Kattha question
# ---------------------------------------------------------------------------------------------------------------
Q_REL = {   # relative → (who / where, that one / there)
    "yassa": ("người nào", "người ấy"),
    "yattha": ("nơi nào", "nơi ấy"),
    "yassa yattha": ("người nào, ở nơi nào", "người ấy, ở nơi ấy"),
}
Q_COR = {"yassa": "tassa", "yattha": "tattha", "yassa yattha": "tassa tattha"}
VA_PANA = "Còn"                             # (Kha) … vā pana …
WHERE = "ở đâu"                             # Kattha … ? (pi-2 «… ở đâu?»)


def pair_q(rel, a, b, label=None, vapana=False):
    """(Ka) Yassa A …, tassa B …ti? = «(a) Ở người nào mà A …, thì ở người ấy có phải B … không?»
    (Kha) Yassa vā pana … = «(b) Còn ở người nào mà …»; yattha «ở nơi nào» / «ở nơi ấy»;
    yassa yattha «ở người nào, ở nơi nào» / «thì ở người ấy, ở nơi ấy»."""
    who, that = Q_REL[rel]
    s = f"{VA_PANA + ' ' + AT if vapana else cap(AT)} {who} mà {a}, {THEN} {AT} {that} có phải {b} không?"
    return f"{S.LABEL[label]} {s}" if label else s


def kattha_q(subject_vi, verb_vi):         # Kattha X anuseti? = «X nằm sẵn ở đâu?»
    return f"{cap(subject_vi)} {verb_vi} {WHERE}?"


# ---------------------------------------------------------------------------------------------------------------
# 5. Runs of tendencies and clauses
# ---------------------------------------------------------------------------------------------------------------
PE_RE = re.compile(r"( ?)…pe…|[^\s…]+")


def parse_tp(text, subject=is_anusaya, name=anusaya_of):
    """'A ca B ca' / 'A' / 'A ca' / 'A…pe… B' / 'A …pe… B' / 'A ca…pe… F ca' →
    dict(names=[…], conj=bool, pe={gap index: spaced?}). `subject` / `name` may be swapped by later chapters
    (e.g. instrumental or accusative forms) as long as they raise on unknown words."""
    names, has_ca, pe = [], [], {}
    for m in PE_RE.finditer(text):
        tok = m.group(0)
        if tok.strip().startswith("…"):
            if not names:
                raise ValueError(f"…pe… before any item: {text!r}")
            pe[len(names) - 1] = m.group(1) == " "
        elif tok == "ca":
            if not names or has_ca[-1]:
                raise ValueError(f"misplaced 'ca' in {text!r}")
            has_ca[-1] = True
        elif subject(tok):
            names.append(name(tok))
            has_ca.append(False)
        else:
            raise ValueError(f"unknown word {tok!r} in {text!r}")
    if not names:
        raise ValueError(f"empty run {text!r}")
    if any(has_ca) and not all(has_ca):
        raise ValueError(f"mixed 'ca' in {text!r}")
    if len(names) > 1 and not all(has_ca) and len(pe) != len(names) - 1:
        raise ValueError(f"list without 'ca' or …pe… in {text!r}")
    return {"names": names, "conj": all(has_ca), "pe": pe}


def tp_vi(tp):
    """Vietnamese run: «A», «A và B», «A, B và C», «A… B» (…pe… cut), «A… và F» ('A ca…pe… F ca')."""
    n = tp["names"]
    out = n[0]
    for i in range(1, len(n)):
        if i - 1 in tp["pe"]:
            gap = " … " if tp["pe"][i - 1] else "… "
            if tp["conj"] and i == len(n) - 1:
                gap += AND + " "
        else:
            gap = f" {AND} " if i == len(n) - 1 else ", "
        out += gap + n[i]
    return out


def parse_clause(text):
    """'<run> <verb> [<run> <verb>]' → [(tp, verb tuple), …]."""
    parts = VERB_RE.split(" " + text.strip())
    if parts[-1].strip():
        raise ValueError(f"clause does not end in a verb: {text!r}")
    groups = []
    for run, verb in zip(parts[0:-1:2], parts[1::2]):
        tp = parse_tp(run.strip())
        v = verb_of(verb)
        # a list ('A ca B ca', 'A ca…pe… F ca') takes the plural; one item or a …pe… cut ('A…pe… B') the singular
        plural = len(tp["names"]) > 1 and tp["conj"]
        if (v[1] == 2) != plural:
            raise ValueError(f"verb number does not fit its subject: {text!r}")
        groups.append((tp, v))
    return groups


def clause_vi(groups):
    """One group: «<run> nằm sẵn». Two groups, each with 'ca' (A ca V B ca V): «A nằm sẵn, B cũng nằm sẵn»."""
    if len(groups) == 1:
        tp, v = groups[0]
        return f"{tp_vi(tp)} {v[0]}"
    if len(groups) == 2 and all(tp["conj"] for tp, _ in groups) and all(v[2] for _, v in groups):
        (t1, v1), (t2, v2) = groups
        return f"{tp_vi(t1)} {v1[0]}, {tp_vi(t2)} {ALSO} {v2[0]}"
    raise ValueError("unknown clause shape: " + repr(groups))


def neg_clause_vi(groups):
    """After 'no ca <pron>': positive verb → «không có A[, cũng không có B …] nằm sẵn» ("neither");
    negative verb, one item → «A vẫn nằm sẵn» (coordinator); a negative verb with a list must be decided first."""
    if len(groups) != 1:
        raise ValueError("no ca with more than one verb: " + repr(groups))
    tp, v = groups[0]
    if tp["pe"]:
        raise ValueError("…pe… inside a 'no ca' part: " + repr(tp))
    if v[2]:
        return f"{NEITHER_FIRST} " + f", {NEITHER_NEXT} ".join(tp["names"]) + f" {v[0]}"
    if len(tp["names"]) == 1:
        return f"{tp['names'][0]} {STILL} {v[3]}"
    raise ValueError("no ca + negative verb + list: not decided (ask the coordinator): " + repr(tp))


# ---------------------------------------------------------------------------------------------------------------
# 6. Answer sentences
# ---------------------------------------------------------------------------------------------------------------
def _take(txt, keys, fold=False):
    for k in sorted(keys, key=len, reverse=True):
        cand = txt[:1].lower() + txt[1:] if fold else txt
        if cand == k or cand.startswith(k + " "):
            return k, txt[len(k):].strip()
    return None, txt


def parse_head(txt):
    """'<person>? <places>* <resumptive>?' → (person key | None, [place keys], resumptive | '')."""
    person, rest = _take(txt, PERSON_GEN)
    places = []
    while rest:
        p, rest2 = _take(rest, PLACE_LOC, fold=True)
        if not p:
            break
        places.append(p)
        rest = rest2
    if rest not in ("", "ettha", "tassa tattha", "tesaṃ tattha"):
        raise ValueError(f"unknown answer head {txt!r} (left: {rest!r})")
    if person and places and rest not in ("tassa tattha", "tesaṃ tattha"):
        raise ValueError(f"person + place without 'tassa / tesaṃ tattha': {txt!r}")
    if person and not places and rest:
        raise ValueError(f"person head with a resumptive: {txt!r}")
    if not person and places and rest != "ettha":
        raise ValueError(f"place head without 'ettha': {txt!r}")
    if not person and not places:
        raise ValueError(f"empty answer head: {txt!r}")
    if person and rest and rest.split()[0] != ("tassa" if PERSON_GEN[person][1] == 1 else "tesaṃ"):
        raise ValueError(f"resumptive number does not fit the person: {txt!r}")
    return person, places, rest


def head_vi(person, places, resumptive):
    parts = ([f"{AT} {PERSON_GEN[person][0]}"] if person else []) + [f"{AT} {PLACE_LOC[p]}" for p in places]
    out = cap(", ".join(parts)) + ", "
    if resumptive == "ettha":
        out += ETTHA + " "
    elif resumptive:
        out += f"{THEN} {AT} {pron_vi(resumptive)} "
    return out


SENT_RE = re.compile(r"(.+?)(?:, no ca (tassa tattha|tesaṃ tattha|tassa|tesaṃ|tattha) (.+))?\.")


def sentence(s):
    """One answer sentence: Āmantā. / No. / Natthi. / <head> <clause>[, no ca <pron> <clause>]."""
    if s in EXACT:
        return EXACT[s]
    m = SENT_RE.fullmatch(s)
    if not m:
        raise ValueError(f"unknown sentence {s!r}")
    words = m.group(1).split()
    i = next((k for k, w in enumerate(words) if is_anusaya(w.split("…")[0])), None)
    if not i:
        raise ValueError(f"no head / no tendency in {s!r}")
    person, places, res = parse_head(" ".join(words[:i]))
    out = head_vi(person, places, res) + clause_vi(parse_clause(" ".join(words[i:])))
    if m.group(2):
        pron = m.group(2)
        want = (res if res and res != "ettha" else
                ("tattha" if not person else ("tassa" if PERSON_GEN[person][1] == 1 else "tesaṃ")))
        if pron != want:
            raise ValueError(f"'no ca {pron}' does not fit the head ({want}): {s!r}")
        out += f", {BUT} {AT} {pron_vi(pron)} {neg_clause_vi(parse_clause(m.group(3)))}"
    return out + "."


def answers(text):
    parts = [x for x in re.split(r"(?<=\.) ", text.strip()) if x]
    return " ".join(sentence(x) for x in parts)


# ---------------------------------------------------------------------------------------------------------------
# 7. Questions
# ---------------------------------------------------------------------------------------------------------------
Q_RE = re.compile(r"(?:\((Ka|Kha)\) )?([Yy])(assa|attha)( vā pana)?( yattha)? (.+?) (tassa tattha|tassa|tattha) "
                  r"(.+?)\?(?: (.+))?")
KATTHA_RE = re.compile(r"Kattha (\S+) (\S+)\? (.+)")


def question(body, clause=lambda t: clause_vi(parse_clause(t)), last_word=strip_ti):
    """A yassa / yattha / yassa yattha pair-question line (+ answers on the same line), or None if `body` is
    not one. `clause` renders the A / B slots (later chapters pass their own slot function)."""
    m = Q_RE.fullmatch(body)
    if not m:
        return None
    label, y, rel1, vapana, yattha, a, cor, b, rest = m.groups()
    rel = ("y" + rel1) + (" yattha" if yattha else "")
    if yattha and rel1 != "assa":
        raise ValueError(f"bad relative in {body!r}")
    if Q_COR[rel] != cor:
        raise ValueError(f"relative {rel!r} with correlative {cor!r}: {body!r}")
    if bool(label) != (y == "y"):
        raise ValueError(f"label / capital mismatch: {body!r}")
    if label and (label == "Kha") != bool(vapana):
        raise ValueError(f"label {label} with vā pana={bool(vapana)}: {body!r}")
    bw = b.split()
    bw[-1] = last_word(bw[-1])
    out = pair_q(rel, clause(a), clause(" ".join(bw)), label, bool(vapana))
    return out + (" " + answers(rest) if rest else "")


def kattha(body):
    m = KATTHA_RE.fullmatch(body)
    if not m:
        return None
    v = verb_of(m.group(2))
    return f"{kattha_q(anusaya_of(m.group(1)), v[0])} {answers(m.group(3))}"


# ---------------------------------------------------------------------------------------------------------------
# 8. Closing labels, headings, fixed lines
# ---------------------------------------------------------------------------------------------------------------
MULAKA = {   # (Xmūlakaṃ) closing labels: pi-3 2-pathamanayo «(Phần xét từng mục một.)» … «(… nhóm bốn.)»
    "Eka": "Phần xét từng mục một", "Duka": "Phần xét từng nhóm hai", "Tika": "Phần xét từng nhóm ba",
    "Catukka": "Phần xét từng nhóm bốn", "Pañcaka": "Phần xét từng nhóm năm", "Chakka": "Phần xét từng nhóm sáu",
}
MULAKA_RE = re.compile(r" \((" + "|".join(MULAKA) + r")mūlakaṃ( ?)(\.?)\)$")


def mulaka_label(m):   # the Pāli's own final «.» kept / absent; the stray space in «(Ekamūlakaṃ )» dropped (slip)
    if m.group(2):
        SLIPS_SEEN.append((m.group(0).strip(), f"({m.group(1)}mūlakaṃ{m.group(3)})"))
    return f"({MULAKA[m.group(1)]}{m.group(3)})"


MAHAVARO = "Mục lớn"                         # Mahāvāro (termbase «mục lớn»)
ANUSAYAVARO = "Mục về khuynh hướng tiềm ẩn"  # anusayavāro / Anusayavāra / Anusayavāre (termbase)
UPPATTITTHANAVARO = "Mục về nơi sinh khởi"   # Uppattiṭṭhānavāro (termbase)
FAMILY_HEADINGS = {   # termbase headings of family C not in S.LATER_HEADINGS (capitalised as S does)
    "Uppattiṭṭhānavāro": UPPATTITTHANAVARO,
    "Anusayavāra": ANUSAYAVARO,
    "Sānusayavāro": "Mục về sự có khuynh hướng tiềm ẩn", "Sānusayavāra": "Mục về sự có khuynh hướng tiềm ẩn",
    "Pajahanavāra": "Mục về sự dứt bỏ", "Pariññāvāra": "Mục về sự hiểu biết trọn vẹn",
    "Pahīnavāra": "Mục về những gì đã được dứt bỏ", "Uppajjanavāro": "Mục về sự sinh khởi",
    "paṭilomapuggalo": "Chiều ngược theo người", "paṭilomaokāso": "Chiều ngược theo nơi chốn",
    "paṭilomapuggalokāsā": "Chiều ngược theo người và nơi chốn",
}


def _later():
    d = {}
    for p, v in S.LATER_HEADINGS:
        ps = [re.sub(r"^\((?:Ka|Kha)\) ", "", x) for x in p.split(" / ")]
        vs = [re.sub(r"^\([ab]\) ", "", x) for x in v.split(" / ")]
        if "<" in p:
            continue
        if len(vs) == 1:
            vs = vs * len(ps)
        assert len(ps) == len(vs), (p, v)
        d.update(zip(ps, vs))
    return d


HEADINGS = {**_later(), **FAMILY_HEADINGS}


def heading(text):
    """Heading text (no #s, no ID) → Vietnamese. '(Ka) anulomapuggalo' → «(a) Chiều thuận theo người»."""
    if text == "Anusayayamakaṃ":
        return S.yamaka_title("Anusaya")
    if m := re.fullmatch(r"Mahāvāro (\d+)\. anusayavāro", text):
        return f"{MAHAVARO} {m.group(1)}. {ANUSAYAVARO[0].lower()}{ANUSAYAVARO[1:]}"   # lower-case as written
    m = re.fullmatch(r"(?:\((Ka|Kha|Ga|Gha|Ṅa|Ca)\) )?(\S+)", text)
    if m and m.group(2) in HEADINGS:
        h = HEADINGS[m.group(2)]
        return f"{S.LABEL[m.group(1)]} {h}" if m.group(1) else h
    raise ValueError(f"unknown heading {text!r}")


FIXED = {
    "Sattānusayā – kāmarāgānusayo, paṭighānusayo, mānānusayo, diṭṭhānusayo, vicikicchānusayo, bhavarāgānusayo, "
    "avijjānusayo.": SATTANUSAYA_LINE,
    "Uppattiṭṭhānavāro.": UPPATTITTHANAVARO + ".",                       # closing label of the section
    "Anusayavāre anulomaṃ.": f"{HEADINGS['anulomaṃ']} trong {ANUSAYAVARO[0].lower()}{ANUSAYAVARO[1:]}.",
}


# ---------------------------------------------------------------------------------------------------------------
# 9. Line translator, build, checks
# ---------------------------------------------------------------------------------------------------------------
def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    else:
        label = ""
        if mm := MULAKA_RE.search(body):
            label = " " + mulaka_label(mm)
            body = body[:mm.start()]
        if body in FIXED:
            out = FIXED[body]
        elif (q := question(body)) is not None:
            out = q
        elif (k := kattha(body)) is not None:
            out = k
        else:
            out = answers(body)
        out += label
    return f"{out} {bid}" if bid else out


def build(name=CHAPTER):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln))
            except ValueError as e:
                raise ValueError(f"{name}: cannot place line {ln[:120]!r}: {e}") from None
        segs.append(out)
    return segs


# strings taken unchanged from the pi-1 … pi-5 Vietnamese rails (asserted at build time)
REUSED = [
    ("Sattānusayā – kāmarāgānusayo, … avijjānusayo.", SATTANUSAYA_LINE, "2"),
    ("ettha … anusayo anuseti", f"{ETTHA} khuynh hướng tiềm ẩn", "2"),
    ("… anuseti", f"{LIE_LATENT}.", "2"),
    ("Kattha … ?", f"{WHERE}?", "2"),
    ("Kāmadhātuyā", "trong cõi dục lạc", "2"),
    ("dukkhāya vedanāya", "cảm giác khó chịu", "1"),
    ("rūpadhātu / arūpadhātu (planes)", "cõi hình sắc và cõi không hình sắc", "5"),
    ("puthujjano", "người phàm phu", "1"),
    ("Dvinnaṃ puggalānaṃ", "hai hạng người", "4"),
    ("sakkāya", "tự ngã", "1"),
    ("pariyāpanna", "nằm trong", "2"),
    ("Natthi.", ANS_NATTHI, "3"),
    ("Āmantā.", YES, "5"),
    ("(Ekamūlakaṃ.)", f"({MULAKA['Eka']}.)", "3"),
    ("(Dukamūlakaṃ.)", f"({MULAKA['Duka']}.)", "3"),
    ("(Tikamūlakaṃ.)", f"({MULAKA['Tika']}.)", "3"),
    ("(Catukkamūlakaṃ.)", f"({MULAKA['Catukka']}.)", "3"),
]
TERMBASE = S.ROOT / "AI_translation/vietnamese/pi-6-pali-vietnamese-termbase-plain.md"
TERMBASE_USED = [   # pi-6 termbase entries used verbatim (asserted: «Pāli: {… : Vietnamese}»)
    ("Sattānusayā", "bảy khuynh hướng tiềm ẩn"), ("kāmarāgānusayo", ANUSAYA["kāmarāg"]),
    ("paṭighānusayo", ANUSAYA["paṭigh"]), ("mānānusayo", ANUSAYA["mān"]), ("diṭṭhānusayo", ANUSAYA["diṭṭh"]),
    ("vicikicchānusayo", ANUSAYA["vicikicch"]), ("bhavarāgānusayo", ANUSAYA["bhavarāg"]),
    ("avijjānusayo", ANUSAYA["avijj"]), ("anuseti", LIE_LATENT), ("anusenti", LIE_LATENT),
    ("nānuseti", "không " + LIE_LATENT), ("Uppattiṭṭhānavāro", "mục về nơi sinh khởi"),
    ("Mahāvāro", "mục lớn"), ("anusayavāro", "mục về khuynh hướng tiềm ẩn"),
    ("Anusayavāre", "mục về khuynh hướng tiềm ẩn"), ("anulomaṃ", "chiều thuận"),
    ("Kāmadhātuyā", "cõi dục lạc"), ("rūpadhātuyā", "cõi hình sắc"), ("arūpadhātuyā", "cõi không hình sắc"),
    ("dvīsu vedanāsu", "hai loại cảm giác"), ("tīsu vedanāsu", "ba loại cảm giác"),
    ("Dukkhāya vedanāya", "cảm giác khó chịu"), ("Anāgāmissa", "bậc không trở lại"),
    ("Puthujjanassa", "người phàm phu"), ("puggalānaṃ", "hạng người"), ("puggalassa", "hạng người"),
    ("tesaṃyeva", "chính những người ấy"), ("Natthi", "không có"), ("arahato", "bậc A-la-hán"),
    ("sānusayo", "có"), ("niranusayo", "không có"), ("nappajahati", "không dứt bỏ"), ("pahīno", "đã được dứt bỏ"),
    ("appahīno", "chưa được dứt bỏ"), ("Sānusayavāro", "mục về sự có khuynh hướng tiềm ẩn"),
    ("paṭilomapuggalo", "chiều ngược theo người"), ("Uppajjanavāro", "mục về sự sinh khởi"),
]


def check_reused():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    tb = TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M)]
    assert not bad, "termbase strings not found: " + repr(bad)


def write(name, segs, extra_dirs=()):
    S.check_against_pali(name, segs)
    text = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in segs) + "\n")
    assert "\n\n\n" not in text and "\r" not in text
    for d in (S.OUT_DIR, *extra_dirs):
        d.mkdir(parents=True, exist_ok=True)
        (d / name).write_text(text, encoding="utf-8", newline="\n")
        print("wrote", d / name, f"({len(segs)} segments)")


# ---------------------------------------------------------------------------------------------------------------
# 10. Notes file (new recurring strings, "Pāli = tiếng Việt")
# ---------------------------------------------------------------------------------------------------------------
def notes():
    o = ["# Rails 7-01 (Anusayayamaka): family C frames and fixed strings", "",
         "Generated by build_rails_7-01_vi.py (family C setter). Later chapters import the module "
         "(importlib.import_module(\"build_rails_7-01_vi\")) and take these strings from it; never retype them. "
         "(pi-N) = taken unchanged from that book's approved rails (asserted).", ""]

    def row(p, v):
        o.append(f"{p} = {v}")

    def h(t):
        o.extend(["", f"## {t}", ""])

    h("Tendencies (all case forms: -o, -ena, -aṃ, -añca)")
    row("Sattānusayā – kāmarāgānusayo, … avijjānusayo.", SATTANUSAYA_LINE + " (pi-2)")
    for k, v in ANUSAYA.items():
        row(f"{k}ānusayo", v)
    row("kāmārāgānusayo (slip)", ANUSAYA["kāmarāg"])
    row("A ca B ca / A ca B ca C ca", f"A {AND} B / A, B {AND} C")
    row("A…pe… B (cut) / A …pe… B", "A… B / A … B")
    row("A ca…pe… F ca", f"A… {AND} F")
    h("Verbs (number checked against the subject)")
    for k, (v, n, pos) in VERB.items():
        row(k, v)
    row("anusanti (slip for anusenti)", LIE_LATENT)
    row("no ca … <negative verb> (one item)", f"A {STILL} {LIE_LATENT}  (coordinator rule; lists: not decided)")
    h("Family C terms for 7-02 … 7-11 (termbase / coordinator)")
    for k, v in FAMILY_TERMS.items():
        row(k, v)
    h("Question shell (coordinator) and Kattha")
    row("(Ka) yassa A anuseti tassa B anusetīti?", pair_q("yassa", "A nằm sẵn", "B nằm sẵn", "Ka"))
    row("(Kha) yassa vā pana B anuseti tassa A anusetīti?", pair_q("yassa", "B nằm sẵn", "A nằm sẵn", "Kha", True))
    row("Yassa … tassa …ti? (no label)", pair_q("yassa", "A nằm sẵn", "B nằm sẵn"))
    row("Yassa vā pana … (no label)", pair_q("yassa", "B nằm sẵn", "A nằm sẵn", None, True))
    row("(Ka) yattha … tattha …ti?", pair_q("yattha", "A nằm sẵn", "B nằm sẵn", "Ka"))
    row("(Ka) yassa yattha … tassa tattha …ti?", pair_q("yassa yattha", "A nằm sẵn", "B nằm sẵn", "Ka"))
    row("Kattha X anuseti?", kattha_q("X", LIE_LATENT))
    h("Answers")
    for k, v in EXACT.items():
        row(k, v)
    for k, (v, n) in PERSON_GEN.items():
        row(f"{k} … (answer head)", f"{cap(AT)} {v}, …")
    for k, v in PLACE_LOC.items():
        row(f"{k} … (answer head; each place its own «ở»)", f"{AT} {v}")
    row("<places> ettha …", f"{cap(AT)} <nơi>, {AT} <nơi>, {ETTHA} …")
    row("<person> <places> tassa tattha …", f"{cap(AT)} <người>, {AT} <nơi>, {THEN} {AT} {pron_vi('tassa tattha')} …")
    row("<person> <places> tesaṃ tattha …", f"{cap(AT)} <người>, {AT} <nơi>, {THEN} {AT} {pron_vi('tesaṃ tattha')} …")
    row("A anuseti", f"A {LIE_LATENT}")
    row("A ca anuseti B ca anuseti (both)", f"A {LIE_LATENT}, B {ALSO} {LIE_LATENT}")
    row("A ca anuseti B ca C ca anusenti", f"A {LIE_LATENT}, B {AND} C {ALSO} {LIE_LATENT}")
    for p in ("tassa", "tesaṃ", "tattha", "tassa tattha", "tesaṃ tattha"):
        row(f", no ca {p} A anuseti", f", {BUT} {AT} {pron_vi(p)} {NEITHER_FIRST} A {LIE_LATENT}")
    row(", no ca tassa A ca B ca anusenti (neither)",
        f", {BUT} {AT} người ấy {NEITHER_FIRST} A, {NEITHER_NEXT} B {LIE_LATENT}")
    o.append("")
    o.append("Examples (built by the module):")
    for p in ("Anāgāmissa mānānusayo anuseti, no ca tassa kāmarāgānusayo anuseti.",
              "Tiṇṇaṃ puggalānaṃ avijjānusayo ca anuseti kāmarāgānusayo ca paṭighānusayo ca anusenti.",
              "Rūpadhātuyā arūpadhātuyā ettha mānānusayo anuseti, no ca tattha kāmarāgānusayo ca paṭighānusayo ca anusenti.",
              "Tesaññeva puggalānaṃ kāmadhātuyā dvīsu vedanāsu tesaṃ tattha mānānusayo ca anuseti kāmarāgānusayo ca anuseti."):
        row(p, sentence(p))
    h("Closing labels and headings")
    for k, v in MULAKA.items():
        row(f"({k}mūlakaṃ)", f"({v})" + (" (pi-3)" if k in ("Eka", "Duka", "Tika", "Catukka") else ""))
    row("Uppattiṭṭhānavāro (heading / closing)", f"{UPPATTITTHANAVARO} / {FIXED['Uppattiṭṭhānavāro.']}")
    row("Mahāvāro 1. anusayavāro", heading("Mahāvāro 1. anusayavāro"))
    row("Anusayavāre anulomaṃ.", FIXED["Anusayavāre anulomaṃ."])
    for k, v in FAMILY_HEADINGS.items():
        row(f"{k} (heading, termbase)", v)
    h("Strings shared with 2-01 (families A, B) and 8 (family D): the coordinator aligns these")
    row("question shell", "pair_q() (coordinator wording)")
    row("No. / Natthi. / Āmantā.", f"{ANS_NO} / {ANS_NATTHI} / {YES}")
    row("answer head", f"«{cap(AT)} <person>, …» / «…, {THEN} {AT} {pron_vi('tassa tattha')} …» / «{ETTHA}» (ettha)")
    row("no ca <pron> <subject> <verb>", f"«…, {BUT} {AT} {pron_vi('tesaṃ')} {NEITHER_FIRST} <subject> <verb>»")
    row("both-frame A ca V B ca V", f"«A V, B {ALSO} V»")
    row("tassa / tesaṃ / tattha", " / ".join(PRON.values()))
    row("uppajjati / uppajjittha / uppajjissati (family B verbs)", " / ".join(
        FAMILY_TERMS[k] for k in ("uppajjati", "uppajjittha", "uppajjissati")))
    o.append("")
    return "\n".join(o)


def main():
    check_reused()
    segs = build(CHAPTER)
    write(CHAPTER, segs, extra_dirs=(ADH_DIR,))
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for p, v in sorted(set(SLIPS_SEEN)):
        print("slip rendered as meant:", p, "→", v)


if __name__ == "__main__":
    main()
