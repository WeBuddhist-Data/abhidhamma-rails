"""Burmese zero-shot SAMPLE of pi-6 (Yamaka, «အတွဲလိုက် မေးဖြေခြင်း»): preamble, 1-mulayamaka, 2-01-khandhayamaka.

usage: python3 -I -X utf8 make_sample.py [chapter ...] [--misses]
Every line is generated from the Pāli by my6_formulas.translate_line() through the frames and tables of my6_formulas.py
(which reads / checks the FINAL pi-1 … pi-5 Burmese, read only) and the table of this script: LINES_SAMPLE (unique
whole lines no frame builds; empty in this sample: every line of the three files comes from a frame or a shared
table). A sentence that no frame / table entry matches stops the run (my6_formulas.Miss): nothing is guessed. Each
line is also checked here against its Pāli (dash count, ellipsis count, «[» count, item number / label, block ID, no
«?», no «।», no «:-», no Latin letters outside variant brackets); a chapter is written only when every line passed.
--misses lists every unmatched line and writes nothing.
Model for later chapters: copy this file, set NAMES_OUT, put the chapter's unique lines into LINES_SAMPLE and its new
terms / subjects / places / headings into the module tables (add_term(), add_subject(), PLACES, H, COLO), never
changing an existing value without the user's approval.
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my6_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-6_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["preamble.md", "1-mulayamaka.md", "2-01-khandhayamaka.md"]

# ===================================================================================== unique lines of the sample
LINES_SAMPLE = {}            # Pāli line (no ID, no label) -> Burmese; none needed in this sample
F.LINES.update(LINES_SAMPLE)

# preamble: the book frame (same three segments as the pi-1 … pi-5 preambles)
H_PRE = {"Abhidhammapiṭake": F.ABHI, "Yamakapāḷi": F.TITLE}
F.H.update(H_PRE)


# ===================================================================================== per-line check
def num(l):
    m = re.match(r"\((\d+)\)", l)
    return m[1] if m else None


def line_check(p, m):
    e = []
    for mark in ("–", "—"):
        if p.count(mark) != m.count(mark):
            e.append(f"dash {mark}")
    if p.replace("…pe…", "…").replace("…Pe…", "…").count("…") != m.count("…"):
        e.append("ellipsis")
    if p.count("[") != m.count("[") or p.count("]") != m.count("]"):
        e.append("brackets")
    if num(p) != num(m):
        e.append("item number")
    lp, lm = F.LABEL_RE.match(p), re.match(r"^\(([က-အ])\) ", m)
    if bool(lp) != bool(lm) or (lp and F.AKKHARA[lp[1]] != lm[1]):
        e.append("label")
    ip, im = F.ID_RE.search(p), F.ID_RE.search(m)
    if bool(ip) != bool(im) or (ip and ip[1] != im[1]):
        e.append("block ID")
    hp, hm = re.match(r"^(#+) ", p), re.match(r"^(#+) ", m)
    if (hp and hp[1]) != (hm and hm[1]):
        e.append("heading level")
    for bad in ("?", "।", ":-"):
        if bad in m:
            e.append(f"«{bad}»")
    if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", re.sub(r"\[[^\]]*\]", "", F.strip_id(m))):
        e.append("Latin letters")
    if not hm and not F.strip_id(m).rstrip().endswith(("။", "…")) and F.strip_id(p).rstrip()[-1:] in ".?":
        e.append("no final «။»")
    return e


def run(name):
    """-> (Burmese text, number of bad lines); raises Miss on an unmatched sentence."""
    src = (PALI / name).read_text(encoding="utf-8-sig")
    out = F.translate_text(src)
    nbad = 0
    P = [l for l in src.splitlines() if l.strip()]
    M = [l for l in out.splitlines() if l.strip()]
    if len(P) != len(M):
        print(f"{name}: {len(P)} vs {len(M)} lines")
        nbad += 1
    for i, (p, m) in enumerate(zip(P, M), 1):
        e = line_check(p, m)
        if e:
            nbad += 1
            print(f"{name}:{i} {e}\n  {p}\n  {m}")
    return out, nbad


def misses(name):
    n = 0
    for i, l in enumerate((PALI / name).read_text(encoding="utf-8-sig").splitlines(), 1):
        try:
            F.translate_line(l)
        except F.Miss as ex:
            n += 1
            print(f"{name}:{i} {ex}")
    return n


# ===================================================================================== the terms file
def terms_md():
    """Write my6-zeroshot-terms.md from the module values (every formula rendered by the real functions)."""
    w = F.WITNESS

    def src(k):
        return f" (pi-{w[k][0]} {w[k][1]})" if k in w else ""
    L = ["# pi-6 Burmese zero-shot: formulas and key terms (Pāli = Burmese)", "",
         "Written by `make_sample.py --terms` from `my6_formulas.py` (import the module; do not retype). «(pi-N ^id)» = the "
         "FINAL rails segment the value was read from / checked against at import; NEW = proposed in this sample; "
         "PROPOSED = for the later chapters, not used in the sample. Binding style: `0-INBOX/temp/pipeline/burmese-style.md`.",
         "", "## 1. Book title and frame",
         f"- Yamakapāḷi (book title, Burmese only) = {F.TITLE} (NEW: \"question and answer in pairs\")",
         f"- Namo tassa bhagavato arahato sammāsambuddhassa = {F.NAMO}{src('Namo tassa bhagavato arahato sammāsambuddhassa')}"
         " (no «။», as in every preamble; also the last line of ch. 1)",
         f"- Abhidhammapiṭake = {F.ABHI}{src('Abhidhammapiṭake')}",
         f"- Xyamakaṃ (chapter) = «Xများ{F.YAMAKA}» -> " + "; ".join(
             f"{k}yamakaṃ = {F.H[k + 'yamakaṃ']}" + ("" if k in ("Mūla", "Khandha") else " (PROPOSED)") for k in F.TOPICS),
         f"- Mūlayamakapāḷi niṭṭhitā. = {F.COLO['Mūlayamakapāḷi niṭṭhitā.']}; X niṭṭhito / niṭṭhitā / niṭṭhitaṃ. = "
         f"«“X” ပြီးဆုံးပြီ။»{src('X niṭṭhito.')}",
         "", "## 2. Headings (vāra, naya, uddesa / niddesa) and colophons",
         f"- uddeso = {F.UDDESO}{src('Uddeso')}; niddeso = {F.NIDDESO}{src('niddeso')}; -vāro = «Xအလိုက် {F.VARA}» or «X {F.VARA}»"
         f"{src('Xvāro')}; -nayo = «X {F.NAYA}»{src('naya')}; -ādi = «X {F.ADI}»{src('-ādi')}",
         f"- labels: " + "; ".join(f"({k}) = {F.label(k)}" for k in list(F.AKKHARA)[:8]) + " …" + src("(Ka)")]
    L += [f"- {k} = {v}" for k, v in F.H.items() if not k.endswith("yamakaṃ")]
    L += [f"- {k} = {v}" for k, v in F.COLO.items() if "yamaka" not in k]
    L += ["", "## 3. Answers, particles, variants",
          f"- Āmantā. = {F.YES}{src('Āmantā')}; Natthi. = {F.NATTHI}{src('Natthi.')} (there is no such person / case); "
          f"No. = {F.NO} (PROPOSED)",
          f"- …pe… / …Pe… = {F.PE} (one «…»); questions end in «လော။» (no «?»); statements in «။»",
          f"- vā pana ((Kha) questions) = {F.VA_PANA}; no ca / na ca = {F.BUT}; sabbe te = {F.ALL}; ye keci = «… {F.WHATEVER}»"
          f"{src('ye keci …, sabbe te …')} (pattern adapted: «မည်သူမဆို» for persons, «မည်သည်တို့မဆို» for phenomena)",
          f"- variant: [reading (sī. syā.)] = [{F.VAR_P} (Sī., Syā.): reading]; spelling only [{F.VAR_L} (…): …]; "
          f"evamuparipi = {F.EVAM_UPARI}{src('evamuparipi')}",
          "", "## 4. Pavattivāra: verbs in every tense and polarity (my_verb(root, tense, neg, form))"]
    for root, pres, past, fut in (("uppajj", "uppajjati", "uppajjittha", "uppajjissati"),
                                  ("nirujjh", "nirujjhati", "nirujjhittha", "nirujjhissati")):
        for tense, pw in (("pres", pres), ("past", past), ("fut", fut)):
            negw = ("n" + pw) if root == "uppajj" else ("na " + pw)
            L.append(f"- {pw} = stmt {F.my_verb(root, tense)} / clause {F.my_verb(root, tense, form='cl')} / question "
                     f"{F.my_verb(root, tense, form='q')}; {negw} = {F.my_verb(root, tense, True)} / "
                     f"{F.my_verb(root, tense, True, 'cl')} / {F.my_verb(root, tense, True, 'q')}; "
                     f"no ca … {negw} = {F.not_so(root, tense)}")
    L += [f"- uppajjati{src('uppajjati')}, nirujjhati{src('nirujjhati')}; nirujjhattha (slip, ^6-2-111) read as nirujjhittha",
          "", "## 5. Pavattivāra: question and answer frames"]
    ex = [("yassa", "rūpakkhandho", "uppajjati", "tassa", "vedanākkhandho", "uppajjatīti"),
          ("yassa vā pana", "vedanākkhandho", "uppajjati", "tassa", "rūpakkhandho", "uppajjatīti"),
          ("yattha", "rūpakkhandho", "uppajjittha", "tattha", "vedanākkhandho", "uppajjitthāti"),
          ("yattha vā pana", "vedanākkhandho", "nuppajjissati", "tattha", "rūpakkhandho", "nuppajjissatīti"),
          ("yassa yattha", "rūpakkhandho", "nirujjhati", "tassa tattha", "vedanākkhandho", "nirujjhatīti"),
          ("yassa vā pana yattha", "vedanākkhandho", "na nirujjhittha", "tassa tattha", "rūpakkhandho",
           "na nirujjhitthāti")]
    for e in ex:
        L.append(f"- {e[0]} {e[1]} {e[2]} {e[3]} {e[4]} {e[5]}? = {F.q_pavatti(*e)}")
    L += [f"- Asaññasattaṃ upapajjantānaṃ tesaṃ X uppajjati, no ca tesaṃ Y uppajjati. = "
          f"{F.a_but('Asaññasattaṃ upapajjantānaṃ', 'tesaṃ', 'rūpakkhandho', 'uppajjati', 'tesaṃ', 'vedanākkhandho', 'uppajjati')}",
          f"- … X nuppajjati, no ca tesaṃ Y nuppajjati. (double negative) = "
          f"{F.a_but('Arūpaṃ upapajjantānaṃ', 'tesaṃ', 'rūpakkhandho', 'nuppajjati', 'tesaṃ', 'vedanākkhandho', 'nuppajjati')}",
          f"- … tesaṃ X ca uppajjati Y ca uppajjittha. = "
          f"{F.a_both('Pañcavokāraṃ upapajjantānaṃ', 'tesaṃ', 'rūpakkhandho', 'uppajjati', 'vedanākkhandho', 'uppajjittha')}",
          f"- Asaññasatte tattha X uppajjati, no ca tattha Y uppajjati. = "
          f"{F.a_but('Asaññasatte', 'tattha', 'rūpakkhandho', 'uppajjati', 'tattha', 'vedanākkhandho', 'uppajjati')}",
          f"- tesaṃ / tesaṃ tattha / tattha (second clause) = " + " / ".join(F.PRO.values()),
          f"- Uppajjati. / Uppajjittha. / Uppajjissati. / Nirujjhati. (short answer) = {F.V('Uppajjati')}။ / "
          f"{F.V('Uppajjittha')}။ / {F.V('Uppajjissati')}။ / {F.V('Nirujjhati')}။",
          "", "## 6. Person and place types (… tesaṃ = «…အား»; bare place + tattha = «…၌»)"]
    L += [f"- {k} = {v}" for k, v in F.PLACES.items()]
    L += [f"- {SATTA} (being) = {F.SATTA_ASANNA}" for SATTA in ["asaññasatta"]]
    gex = ["Asaññasattaṃ upapajjantānaṃ", "Pañcavokāraṃ upapajjantānaṃ", "Catuvokāraṃ pañcavokāraṃ upapajjantānaṃ",
           "Arūpaṃ upapajjantānaṃ", "Suddhāvāsaṃ upapajjantānaṃ", "Sabbesaṃ upapajjantānaṃ", "Sabbesaṃ cavantānaṃ",
           "Asaññasattā cavantānaṃ", "Pañcavokārā cavantānaṃ", "Catuvokārā pañcavokārā cavantānaṃ", "Arūpā cavantānaṃ",
           "Parinibbantānaṃ", "Pañcavokāre parinibbantānaṃ", "Suddhāvāse parinibbantānaṃ", "Pacchimabhavikānaṃ",
           "Pacchimabhavikānaṃ upapajjantānaṃ", "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ",
           "Pañcavokāre pacchimabhavikānaṃ", "arūpe pacchimabhavikānaṃ", "Asaññasattānaṃ", "Pañcavokārānaṃ",
           "catuvokārānaṃ pañcavokārānaṃ", "Arūpānaṃ", "Suddhāvāsānaṃ", "Itaresaṃ", "Itaresaṃ pañcavokāraṃ upapajjantānaṃ",
           "Itaresaṃ catuvokārānaṃ pañcavokārānaṃ", "Itaresaṃ pañcavokārānaṃ", "Ye arūpaṃ upapajjitvā parinibbāyissanti",
           "Sabbesaṃ cavantānaṃ arūpaṃ upapajjantānaṃ",
           "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ asaññasattā cavantānaṃ"]
    L += [f"- {e} (tesaṃ) = {F.group_my(e)}{F.DAT}" for e in gex]
    L += [f"- participles: upapajjantānaṃ{src('upapattikkhaṇe')} / cavantānaṃ{src('cavanti')} / parinibbantānaṃ"
          f"{src('parinibbāyī')} = «… ဆဲ» (pi-4 cavamāne «သေဆဲ»); pacchimabhavika = {F.PACCHIMA}သူ (NEW); itara = "
          f"{F.OTHERS} (NEW); suddhāvāsa = {F.PLACES['suddhāvāsa']} (NEW, name kept)",
          "", "## 7. Ch. 1 Mūlayamaka: bases, root predicates, frames"]
    L += [f"- {k}: before «{F.DHAMMA}» {v[0]}; before a root {v[1]}; as a noun {v[2]}" for k, v in F.BASE.items()]
    for p in ("kusalamūlā", "kusalamūlena ekamūlā", "kusalamūlena aññamaññamūlā", "kusalamūlamūlā",
              "kusalamūlena ekamūlamūlā", "kusalamūlena aññamaññamūlamūlā", "kusalamūlakā", "kusalamūlena ekamūlakā",
              "kusalamūlena aññamaññamūlakā", "kusalamūlamūlakā", "kusalamūlena ekamūlamūlakā",
              "kusalamūlena aññamaññamūlamūlakā"):
        pr = F.pred(p)
        L.append(f"- {p} = question {pr.q()} / statement {pr.stmt()} / na … {pr.neg()} / relative {pr.attr()}")
    L += [f"- kusalamūla{src('kusalamūla')}; akusalamūla{src('akusalamūla')}; mūlamūla = {F.MULAMULA} (NEW); eka- = {F.EKA} "
          f"(NEW); aññamañña = {F.ANNA}{src('aññamañña')}; -mūlaka = «…ကို {F.KA_VERB}» (NEW)",
          f"- (Ka) ye keci kusalā dhammā, sabbe te kusalamūlā? = (က) {F.ye_keci('kusalā', 'kusalamūlā')}",
          f"- (Kha) ye vā pana kusalamūlā, sabbe te dhammā kusalā? = (ခ) {F.ye_va_pana('kusalamūlā', 'kusalā')}"]
    for s in ("Tīṇeva kusalamūlāni.", "Naveva nāmamūlāni.", "Avasesā kusalā dhammā na kusalamūlā.",
              "Kusalasamuṭṭhānaṃ rūpaṃ kusalamūlena ekamūlaṃ, na kusalaṃ.",
              "Kusalaṃ kusalamūlena ekamūlañceva kusalañca.",
              "Mūlāni yāni ekato uppajjanti kusalamūlāni ekamūlāni ceva aññamaññamūlāni ca.",
              "Avasesā kusalamūlasahajātā dhammā kusalamūlena ekamūlā, na ca aññamaññamūlā.",
              "Ahetukaṃ akusalaṃ akusalamūlena na ekamūlaṃ.", "Sahetukaṃ abyākataṃ abyākatamūlakaṃ."):
        L.append(f"- {s} = {F.ch1_sentence(s)}")
    L += [f"- ahetuka / sahetuka = {F.AHETUKA} / {F.SAHETUKA}{src('ahetukā dhammā')}; -samuṭṭhānaṃ rūpaṃ = «X{F.SAMUTTHANA} "
          f"{F.RUPA_W}»{src('samuṭṭhāna')}; -sahajāta = «X{F.SAHAJATA}»{src('sahajātā')}; ekato = {F.EKATO}{src('ekato')}; "
          f"avasesā = {F.AVASESA}{src('avasesā paññā')}",
          "- hetuvāra synonym list (each Pāli word its own Burmese): " + "; ".join(
              f"{k} = {v}" for k, v in zip(("mūla", "hetu", "nidāna", "sambhava", "pabhava", "samuṭṭhāna", "āhāra",
                                         "ārammaṇa", "paccaya", "samudaya"), F.HETU.values())),
          f"- Mūlaṃ hetu nidānañca, sambhavo pabhavena ca; = {F.HETU_VERSE[0]}",
          f"- Samuṭṭhānāhārārammaṇā, paccayo samudayena cāti. = {F.HETU_VERSE[1].format(v='')}",
          "", "## 8. Ch. 2 Khandhayamaka: terms and paṇṇattivāra frames",
          f"- Pañcakkhandhā = {F.KHANDHA_H}; " + "; ".join(f"{k} = {v}" for k, v in F.KHANDHA.items()) + src("rūpakkhandho"),
          "- bare terms: " + "; ".join(f"{k} = {v[0]}" for k, v in F.PT.items() if "kkhandh" not in k)
          + src("rūpaṃ, vedanā, saññā, saṅkhārā, viññāṇaṃ"),
          f"- Piyarūpaṃ sātarūpaṃ = {F.PIYA}{src('piyarūpaṃ sātarūpaṃ')}; Diṭṭhisaññā = {F.SPECIAL_SUBJ['Diṭṭhisaññā']} (NEW)",
          f"- ṭhapetvā = {F.THAPETVA}{src('ṭhapetvā')}",
          f"- (Ka) rūpaṃ rūpakkhandho? = (က) {F.q_term('rūpaṃ', 'rūpakkhandho')}",
          f"- (Kha) khandhā vedanākkhandho? = (ခ) {F.q_term('khandhā', 'vedanākkhandho')}",
          f"- (Ka) na rūpaṃ na rūpakkhandho? = (က) {F.q_term('rūpaṃ', 'rūpakkhandho', True)}"]
    for s in ("Piyarūpaṃ sātarūpaṃ rūpaṃ, na rūpakkhandho.", "Rūpakkhandho rūpañceva rūpakkhandho ca.",
              "Saṅkhārakkhandhaṃ ṭhapetvā avasesā saṅkhārā, na saṅkhārakkhandho.",
              "Avasesā khandhā na vedanākkhandho.", "Piyarūpaṃ sātarūpaṃ na rūpakkhandho, rūpaṃ.",
              "Rūpaṃ ṭhapetvā avasesā khandhā na rūpaṃ, khandhā.",
              "Rūpañca rūpakkhandhañca ṭhapetvā avasesā na ceva rūpaṃ na ca rūpakkhandho."):
        L.append(f"- {s} = {F.pannatti_sentence(s)}")
    L += ["", "## 9. All values read from pi-1 … pi-5 FINAL at import (WITNESS)"]
    L += [f"- {k} = {v[2]} (pi-{v[0]} {v[1]})" for k, v in sorted(w.items())]
    (HERE / "my6-zeroshot-terms.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    return len(L)


if __name__ == "__main__":
    if "--terms" in sys.argv:
        print("my6-zeroshot-terms.md:", terms_md(), "lines")
        sys.exit(0)
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    names = args or NAMES_OUT
    if "--misses" in sys.argv:
        print("misses:", sum(misses(n) for n in names))
        sys.exit(0)
    OUT.mkdir(parents=True, exist_ok=True)
    for n in names:
        text, nbad = run(n)
        if nbad:
            sys.exit(f"{n}: {nbad} bad lines, nothing written")
        (OUT / n).write_text(text, encoding="utf-8")
        print(f"{n}: written, {len([l for l in text.splitlines() if l.strip()])} lines")
