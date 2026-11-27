"""pi-4 Burmese rails: the bilingual-review fixes (review/report-A.md A1 … A6, review/report-B.md B1 … B6, rails doubt 5
of rails/notes-rails.md; decisions in review/fix-brief.md, results and the KEEP items in review/fix-notes.md).
Model: pi-3-my/rails/apply_fixes.py, pi-2-my/rails/apply_fixes.py (read only).

The two fixes that change a repeated formula are rails-layer patches (my_formulas_rails.py): L26 = B2 (^4-166, the
vaṇṇopi / avaṇṇopi formula, 4 lines), L27 = B4 (^4-164 / ^4-165, the pasāda / appasāda quote endings, 4 lines).
The single-segment fixes are the explicit rules F01 … F05 here:
  F01 A1 ^4-M-16, F02 A6 ^4-94, F03 B1 ^4-176 (termbase narassa «မြို့»), F04 B6 ^4-175, F05 rails doubt 5 ^4-179
  (termbase sāci «ကွေ့ဝိုက်သော»).
Not changed (checked here, book-wide): B3 (the ^4-171 list already has each termbase term at its Pāli slot) and B5
(^4-178 already has pi-1 ^1-1350's form of the identical Pāli frame; see fix-notes.md).

usage: python3 -I -X utf8 apply_fixes.py
Run by regen_rails.sh right after apply_termbase.py (build_rails.py rewrites every chapter first, so a rebuild always
starts from the same input). Reads and rewrites AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters.

Every rule, applied line by line (Pāli and Burmese lines are aligned inside each segment):
  - scope: a list of segment IDs;
  - trigger: a regex the aligned Pāli line must match, else the line is not touched;
  - change: a list of exact Burmese old → new pairs; each Pāli trigger hit must give exactly one replacement;
  - expected replacement count over the whole book: the run fails (and writes nothing) if the count differs;
  - every changed line keeps its «[» / «…» / «–» / «“» / «”» counts.
Book-wide checks (book_checks): every instance of each pattern is found by script over all chapters (Pāli and
Burmese), and the layer fixes L26 / L27 and the two unchanged items B3 / B5 are verified there too.
Every replacement is logged in rails/fixes-log.tsv (ch, id, line, old, new, rule); line = line number in the chapter file.
Deterministic: no randomness, files and rules in fixed order.
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation/pali/pi-4_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters"
TB = ROOT / "AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md"
PI1_PALI = ROOT / "AI_translation/pali/pi-1_split_chapters/4-03-nikkhepakandam.md"
PI1_MY = ROOT / "AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters/4-03-nikkhepakandam.md"
LOG = HERE / "fixes-log.tsv"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731

_TITLE = "“ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း”"          # the approved book title (^4-0, ^4-209)
_OLD_M16 = "“ပုဂ္ဂိုလ် သတ်မှတ်ချက် ခေါင်းစဉ်စာရင်း” ပြီးဆုံးပြီ"
_NEW_M16 = f"{_TITLE} ခေါင်းစဉ်စာရင်း ပြီးဆုံးပြီ"
_OLD_B6 = "သို့မဟုတ် ကြမ်းကြုတ်သော အလုပ် ရှိကြသော အခြားသူတို့လည်း ဖြစ်ကြ၏"
_NEW_B6 = "သို့မဟုတ် ကြမ်းကြုတ်သော အလုပ် ရှိသော အခြား တစ်စုံတစ်ယောက် ဖြစ်၏"

# (rule, segment ids, Pāli trigger regex, [(old, new)], expected)
RULES = [
    ("F01 A1 ^4-M-16 Puggalapaññattimātikā niṭṭhitā: the book name is the approved title (as the colophon ^4-209 "
     "«“ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း” ကျမ်း ပြီးဆုံးပြီ»), «ခေါင်းစဉ်စာရင်း» = mātikā outside the quotes",
     ["4-M-16"], r"Puggalapaññattimātikā niṭṭhitā", [(_OLD_M16, _NEW_M16)], 1),
    ("F02 A6 ^4-94 Evamevaṃ tayo gilānūpamā puggalā (no ime): no added «ဤ»",
     ["4-94"], r"Evamevaṃ (?:\[[^\]]*\] )?tayo gilānūpamā puggalā",
     [("လူနာနှင့် တူသော ဤပုဂ္ဂိုလ် သုံးယောက်တို့သည်", "လူနာနှင့် တူသော ပုဂ္ဂိုလ် သုံးယောက်တို့သည်")], 1),
    ("F03 B1 ^4-176 puratthimena narassa = «မြို့၏ အရှေ့ဘက်၌» (termbase narassa|0 «မြို့», changed 2026-11-20: the "
     "fragment of nagarassa)",
     ["4-176"], r"puratthimena narassa", [("လူ၏ အရှေ့ဘက်၌", "မြို့၏ အရှေ့ဘက်၌")], 1),
    ("F04 B6 ^4-175 ye vā panaññepi keci kurūrakammantā: one more person of the list, no subject switch: «… သို့မဟုတ် "
     "ကြမ်းကြုတ်သော အလုပ် ရှိသော အခြား တစ်စုံတစ်ယောက် ဖြစ်၏» (termbase kurūra «ကြမ်းကြုတ်သော» + kammantā «အလုပ် "
     "ရှိသော» kept)",
     ["4-175"], r"ye vā panaññepi keci kurūrakammantā", [(_OLD_B6, _NEW_B6)], 1),
    ("F05 rails doubt 5 ^4-179 sāciyoga = «ကွေ့ဝိုက်သော နည်းလမ်း» (termbase sāci|0 «ကွေ့ဝိုက်သော», changed "
     "2026-11-20); nikati keeps «ကောက်ကျစ်ခြင်း» (L24)",
     ["4-179"], r"nikatisāciyogā",
     [("ကောက်ကျစ်ခြင်း၊ ကောက်ကျစ်သော နည်းလမ်း", "ကောက်ကျစ်ခြင်း၊ ကွေ့ဝိုက်သော နည်းလမ်း")], 1),
]


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


def marks(s):
    return tuple(s.count(c) for c in "[…–“”")


def termbase():
    tb = {}
    for l in open(TB, encoding="utf-8"):
        m = re.match(r"^(.*?): \{(.*)\}\s*$", N(l.rstrip("\n")))
        if m:
            tb[m.group(1)] = [p.rsplit(": ", 1)[1].strip() for p in m.group(2).split("; ") if ": " in p]
    return tb


def book_checks(files, pali, text):
    """every instance by script; returns (errors, info lines)."""
    err, info = [], []
    pairs = [(f, k, N(re.sub(r"\[[^\]]*\]", "", p)), N(text[f][k])) for f in files
             for k, p in enumerate(pali[f]) if p.strip()]

    def count(rx_p, rx_m, label, lines=None):
        np_ = sum(len(re.findall(rx_p, p)) for f, k, p, m in pairs)
        nm = sum(len(re.findall(rx_m, m)) for f, k, p, m in pairs if re.search(rx_p, p))
        info.append(f"{label}: Pāli {np_}, Burmese {nm}")
        if np_ != nm:
            err.append(f"{label}: Pāli {np_} ≠ Burmese {nm}")

    def gone(rx_m, label):
        left = [f"{f[:-3]}:{k + 1}" for f, k, p, m in pairs if re.search(rx_m, m)]
        if left:
            err.append(f"{label}: old form left on {left}")

    # F01 A1: the M-16 title = the colophon title; no «ပုဂ္ဂိုလ် သတ်မှတ်ချက် ခေါင်းစဉ်စာရင်း» left
    count(r"Puggalapaññattimātikā niṭṭhitā", re.escape(_NEW_M16), "F01 A1 mātikā colophon")
    count(r"Puggalapaññattipakaraṇaṃ niṭṭhitaṃ", re.escape(_TITLE) + " ကျမ်း ပြီးဆုံးပြီ", "F01 A1 = book colophon ^4-209")
    gone(r"ပုဂ္ဂိုလ် သတ်မှတ်ချက် ခေါင်းစဉ်စာရင်း", "F01 A1")
    # F02 A6: «… တူသော ဤပုဂ္ဂိုလ် N-ယောက်» exactly where the simile's Evamevaṃ has ime
    count(r"Evamevaṃ (?:tayome|cattārome|pañcime) ", r"တူသော ဤပုဂ္ဂိုလ်", "F02 A6 Evamevaṃ … -(i)me = «ဤ»")
    count(r"Evamevaṃ\s+(?:tayo|cattāro|pañca) ", r"ထို့အတူပင် [^၊။]*တူသော ပုဂ္ဂိုလ်", "F02 A6 Evamevaṃ without ime, no «ဤ»")
    # F03 B1 narassa
    count(r"\bnarassa\b", r"မြို့၏ အရှေ့ဘက်၌", "F03 B1 narassa «မြို့»")
    gone(r"လူ၏ အရှေ့ဘက်", "F03 B1")
    # F04 B6
    count(r"panaññepi keci kurūrakammantā", re.escape(_NEW_B6), "F04 B6 kurūrakammantā")
    gone(r"အခြားသူတို့လည်း ဖြစ်ကြ၏", "F04 B6")
    # F05 sāci (nikati kept)
    count(r"sāciyog", r"ကွေ့ဝိုက်သော နည်းလမ်း", "F05 sāci «ကွေ့ဝိုက်သော»")
    count(r"nikati", r"ကောက်ကျစ်ခြင်း", "F05 nikati keeps «ကောက်ကျစ်ခြင်း»")
    gone(r"ကောက်ကျစ်သော", "F05")
    # L26 B2 (layer): ^4-166
    count(r"vaṇṇopi saṃvijjati avaṇṇopi saṃvijjati",
          r"ဤလောက၌ အချို့သော ပုဂ္ဂိုလ်အဖို့ ချီးမွမ်းဖွယ်လည်း ရှိ၏၊ ကဲ့ရဲ့ဖွယ်လည်း ရှိ၏။", "L26 B2 vaṇṇopi … saṃvijjati")
    count(r"[Yy]o(?:pi)? tattha a?vaṇṇo", r"ထိုတို့အနက် (?:ကဲ့ရဲ့|ချီးမွမ်း)ဖွယ် ရှိသမျှကို", "L26 B2 yo tattha (a)vaṇṇo")
    gone(r"ထိုသူ၌ (?:ကဲ့ရဲ့|ချီးမွမ်း)ဖွယ်|ပုဂ္ဂိုလ်သည် ချီးမွမ်းဖွယ်လည်း", "L26 B2")
    # L27 B4 (layer): every «… janeti – "…" itipi …» line ends with its own janeti phrase; the bhāsati lines keep «ပြောဆို၏»
    n_j = 0
    for f, k, p, m in pairs:
        for v in re.findall(r"\b(pasādaṃ|appasādaṃ) janeti – ", p):
            n_j += 1
            want = ("မ" if v == "appasādaṃ" else "") + "ကြည်ညိုမှုကို ဖြစ်စေ၏"
            mm = re.search(r"(\S+ ဖြစ်စေ၏) – .*ဟူ၍လည်း (\S+ ဖြစ်စေ၏)။", m)
            if not mm or mm.group(1) != want or mm.group(2) != want or "ဟူ၍လည်း ပြောဆို၏" in m:
                err.append(f"L27 B4 {f[:-3]}:{k + 1}: the line does not end with its own janeti phrase «{want}»")
    info.append(f"L27 B4 janeti – lines: {n_j}")
    count(r"\bbhāsati – ", r"ဟူ၍လည်း ပြောဆို၏", "L27 B4 bhāsati – lines keep «ပြောဆို၏»")
    # B3 (no change): the ^4-171 list = the termbase terms in the Pāli order
    tb = termbase()
    lst = "၊ ".join(tb[w][0] for w in ("vaṇṇanāya", "thomanāya", "pasaṃsanāya", "vaṇṇahārikāya"))
    count(r"paravaṇṇanāya parathomanāya parapasaṃsanāya paravaṇṇahārikāya", re.escape(lst),
          f"B3 (kept) the list in the Pāli order = termbase «{lst}»")
    # B5 (no change): ^4-178 = pi-1 ^1-1350's Burmese of the identical frame «yā sā vācā neḷā … tathārūpiṃ vācaṃ bhāsitā hoti»
    p1 = N(PI1_PALI.read_text(encoding="utf-8-sig"))
    m1 = N(PI1_MY.read_text(encoding="utf-8"))
    pl = [l for l in p1.splitlines() if l.rstrip().endswith("^1-1350")]
    ml = [l for l in m1.splitlines() if l.rstrip().endswith("^1-1350")]
    fr = re.search(r"(?:အပြစ်ကင်းသော၊ [^၊]*(?:၊ [^၊]*)*?) စကား ရှိ၏ ထိုသို့သော စကားကို ပြောဆိုသူ ဖြစ်၏", ml[0] if ml else "")
    if not (pl and "bahujanamanāpā tathārūpiṃ vācaṃ bhāsitā hoti" in pl[0] and fr):
        err.append("B5: pi-1 ^1-1350 frame not found")
    else:
        count(r"[Yy]ā sā vācā nelā [^.]*bahujanamanāpā tathārūpiṃ vācaṃ bhāsitā hoti", re.escape(fr.group(0)),
              "B5 (kept) yā sā vācā … tathārūpiṃ = pi-1 ^1-1350 «… စကား ရှိ၏ ထိုသို့သော …»")
    return err, info


def main():
    files = sorted(p.name for p in PALI.glob("*.md"))
    pali = {f: (PALI / f).read_text(encoding="utf-8-sig").split("\n") for f in files}
    text = {f: (OUT / f).read_text(encoding="utf-8").split("\n") for f in files}
    pseg = {f: segs(pali[f]) for f in files}
    mseg = {f: dict(segs(text[f])) for f in files}
    log, errors, counts = [], [], {}
    for rule, ids, trig, pairs, expect in RULES:
        trig_re = re.compile(trig)
        done, found = 0, set()
        for f in files:
            for i, pidx in pseg[f]:
                if i not in ids:
                    continue
                found.add(i)
                midx = mseg[f].get(i)
                if midx is None or len(midx) != len(pidx):
                    errors.append(f"{rule[:3]}: {f} {i}: segment missing or not line-aligned")
                    continue
                for pk, mk in zip(pidx, midx):
                    np_ = len(trig_re.findall(pali[f][pk]))
                    if not np_:
                        continue
                    before, got = text[f][mk], 0
                    for old, new in pairs:
                        n = text[f][mk].count(old)
                        if n:
                            text[f][mk] = text[f][mk].replace(old, new)
                            got += n
                            log += [(f[:-3], i, str(mk + 1), old, new, rule)] * n
                    if got != np_:
                        errors.append(f"{rule[:3]}: {f[:-3]} {i} line {mk + 1}: {got} replacements, Pāli {np_}")
                    if marks(before) != marks(text[f][mk]):
                        errors.append(f"{rule[:3]}: {f[:-3]} {i} line {mk + 1}: «[ … – “ ”» counts changed")
                    done += got
        if found != set(ids):
            errors.append(f"{rule[:3]}: segments not found: {sorted(set(ids) - found)}")
        counts[rule] = done
        if done != expect:
            errors.append(f"{rule[:3]}: {done} replacements, expected {expect}")
    berr, info = book_checks(files, pali, text)
    errors += berr
    for rule, n in counts.items():
        print(f"{n:6d}  {rule[:110]}")
    for x in info:
        print(f"        check: {x}")
    if errors:
        print("\n".join(errors))
        print(f"{len(errors)} errors")
        sys.exit(1)
    for f in files:
        (OUT / f).write_text("\n".join(text[f]), encoding="utf-8")
    with open(LOG, "w", encoding="utf-8") as fh:
        fh.write("ch\tid\tline\told\tnew\trule\n")
        for row in log:
            fh.write("\t".join(row) + "\n")
    print(f"{len(RULES)} rules; {len(log)} replacements; {len({(r[0], r[2]) for r in log})} lines changed")


main()
