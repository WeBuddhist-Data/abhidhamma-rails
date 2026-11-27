"""pi-2 Burmese rails: the bilingual-review fixes that are single segments (review/report-A.md, review/report-B.md;
decisions in review/fix-brief.md, results and the items not applied in review/fix-notes.md).
The fixes that change a repeated formula or term are rails-layer patches (my_formulas_rails.py, L69 … L73).

usage: python3 -I -X utf8 apply_fixes.py
Run by regen_rails.sh right after apply_termbase.py (build_rails.py rewrites every chapter first, so a rebuild always
starts from the same input). Reads and rewrites AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters.

Every fix is an explicit rule, applied line by line (Pāli and Burmese lines are aligned inside each segment):
  - scope: a list of segment IDs;
  - trigger: a regex the aligned Pāli line must match, else the line is not touched;
  - change: exact Burmese old → new, or (old None) a pattern function (F7) that rebuilds the run and checks it;
  - expected replacement count over the whole book: the run fails (and writes nothing) if the count differs.
Every replacement is logged in rails/fixes-log.tsv (ch, id, line, old, new, rule); line = line number in the chapter file.
Deterministic: no randomness, files and rules in fixed order.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation/pali/pi-2_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters"
LOG = HERE / "fixes-log.tsv"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

_MY = "မှားယွင်းသော ယူဆမှု"
_B1_OLD = ("ဤလမ်းမှားကို ပေါင်းသင်းခြင်း၊ နီးကပ်စွာ ပေါင်းသင်းခြင်း၊ ကောင်းစွာ ပေါင်းသင်းခြင်း၊ ဆည်းကပ်ခြင်း၊ ကောင်းစွာ ဆည်းကပ်ခြင်း၊ "
           "ကိုးကွယ်ခြင်း၊ ကောင်းစွာ ကိုးကွယ်ခြင်း၊ ထိုသူတို့ဘက်သို့ ညွတ်ကိုင်းခြင်း ရှိသမျှ")
_B1_NEW = ("ဤလမ်းမှားကို မှီဝဲခြင်း၊ နီးကပ်စွာ မှီဝဲခြင်း၊ ကောင်းစွာ မှီဝဲခြင်း၊ ဆည်းကပ်ခြင်း၊ ကောင်းစွာ ဆည်းကပ်ခြင်း၊ "
           "ကိုးကွယ်ခြင်း၊ ကောင်းစွာ ကိုးကွယ်ခြင်း၊ ထိုလမ်းမှားဘက်သို့ ညွတ်ကိုင်းခြင်း ရှိသမျှ")
# ---------------------------------------------------------------- F7 (A3 extended, user decision 2026-11-18)
# The compressed citta openings of ch14 / ch15 (pi-1's verbatim attributive form «X နှင့်အတူ ဖြစ်သော၊ Y နှင့် ယှဉ်တွဲသော
# [တိုက်တွန်းမှုဖြင့်]… …») get the ch6 A3 Burmese (L70) for the same qualifier sequence: «X နှင့်အတူ ဖြစ်၍ Y နှင့်
# ယှဉ်တွဲလျက် / ကင်းကွာလျက် [တိုက်တွန်းမှုဖြင့်]», the subject first as ch6 («SUBJ သည် … [objects] ဖြစ်ပေါ်ပြီးသော»; the
# abstainer genitive «… ရှောင်ကြဉ်နေသူ၏» stays before the subject; kiriyā neva kusalā … before the noun as ch6 ^2-331).
# ^2-709 / ^2-711 (hīnaṃ … paṇītaṃ tail, pi-1 2-02 pattern, not in ch6): the adverbial qualifier run first, then
# «၊ GEN ယုတ်ညံ့သော… … မွန်မြတ်သော SUBJ သည်» (the hīna / adhipati attributives stay directly before their noun).
# Checked: groups = the Pāli «-sahagat-» count, «တိုက်တွန်းမှုဖြင့်» = the «sasaṅkhārena» count, and the result for the
# openings that are identical Pāli to ch6 (^2-712, ^2-726 = ^2-339; ^2-737 = ^2-319) is ch6's Burmese (main()).
_X = r"(?:ဝမ်းမြောက်မှု|ဥပေက္ခာ|စိတ်ဆင်းရဲမှု)နှင့်အတူ ဖြစ်သော"
_Y = r"(?:ဉာဏ်|အယူမှား|မုန်းတီးမှု|ယုံမှားမှု|ယောက်ယက်ခတ်မှု)နှင့် (?:ယှဉ်တွဲ|ကင်းကွာ)သော"
_G = rf"{_X}၊ {_Y}(?: တိုက်တွန်းမှုဖြင့်)?"
_QRUN = re.compile(rf"{_G}(?:… {_G})+")
_SUBJ = r"(?:ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်စိတ်|အကုသိုလ်စိတ်|မနော သိစိတ် ဓာတ်)"
_SAS = "တိုက်တွန်းမှုဖြင့်"
_KIR = "ပြုရုံမျှသာ ဖြစ်သော၊ ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်၊ ကံ၏ အကျိုးလည်း မဟုတ်သော"
F7_IDS = ["2-704", "2-706", "2-709", "2-711", "2-712", "2-726", "2-731", "2-737", "2-745"]
F7_SAME_AS_CH6 = {"2-712": "2-339", "2-726": "2-339", "2-737": "2-319"}


def _adv(run):
    out = []
    for g in run.split("… "):
        x, y = g.split("၊ ")
        x = x.removesuffix("ဖြစ်သော") + "ဖြစ်၍"
        sas = y.endswith(" " + _SAS)
        y = y.removesuffix(" " + _SAS)
        y = y[:-len("သော")] + "လျက်"
        out.append(f"{x} {y}" + (f" {_SAS}" if sas else ""))
    return "… ".join(out)


def f7(p, m):
    po = re.search(r"Yasmiṃ samaye (.*?)(?:, (?:tasmiṃ|yā tasmiṃ|yo tasmiṃ)|…pe… rūpāvacaraṃ jhānaṃ)", p).group(1)
    n_groups, n_sas = len(re.findall(r"sahagat(?:aṃ|ā) ", po)), po.count("sasaṅkhārena")
    q = _QRUN.search(m)
    if not q or len(_QRUN.findall(m)) != 1:
        raise ValueError("qualifier run not found once")
    start = m.rfind("။ ", 0, q.start()) + 2
    pre, run = m[start:q.start()], q.group(0)
    if run.count("… ") + 1 != n_groups:
        raise ValueError(f"groups {run.count('… ') + 1} != Pāli {n_groups}")
    rest = m[q.end():]
    r1 = re.match(rf" (?P<s>{_SUBJ})သည် (?P<a>{_SAS} )?ဖြစ်ပေါ်ပြီးသော", rest)
    r3 = re.match(rf"၊ ယုတ်ညံ့သော {_SAS}… (?P<t>.+? မွန်မြတ်သော) (?P<s>{_SUBJ})သည် ဖြစ်ပေါ်ပြီးသော", rest)
    sm = re.fullmatch(rf"(?P<h>.*?)(?P<s>{_SUBJ})သည် (?P<k>{_KIR}၊ )?", pre)
    if r1 and pre.endswith(("ဖြစ်စေ ", "၏ ")):                     # subject last (objects / abstainer before)
        a = _adv(run) + (f" {_SAS}" if r1["a"] else "")
        if pre.endswith("၏ "):
            new = f"{pre}{r1['s']}သည် {a} ဖြစ်ပေါ်ပြီးသော"
        else:
            new = f"{r1['s']}သည် {a} {pre}ဖြစ်ပေါ်ပြီးသော"
        old = m[start:q.end() + r1.end()]
    elif r3 and pre.endswith("၏ "):                                  # ^2-709 / ^2-711: hīna … paṇīta tail
        new = f"{_adv(run)} {_SAS}၊ {pre}ယုတ်ညံ့သော… {r3['t']} {r3['s']}သည် ဖြစ်ပေါ်ပြီးသော"
        old = m[start:q.end() + r3.end()]
    elif sm:                                                         # subject first already (^2-737, ^2-745)
        h = sm["h"] + (_KIR + " " if sm["k"] else "")
        new = f"{h}{sm['s']}သည် {_adv(run)}"
        old = m[start:q.end()]
    else:
        raise ValueError("opening shape not known")
    if new.count(_SAS) != n_sas:
        raise ValueError(f"«{_SAS}» {new.count(_SAS)} != sasaṅkhārena {n_sas}")
    return m[:start] + new + m[start + len(old):], [(old, new)]



# (rule, segment ids, Pāli trigger regex, old, new, expected)
RULES = [
    ("F1 A1 ^2-188 source quote slip «… parāmaṭṭhā cāti parāmaṭṭhā ceva no ca parāmāsā» rendered for its intended reading "
     "(as 1-khandha / 2-ayatana / 5-indriya: the first item denied, the second affirmed; one dash as the Pāli)",
     ["2-188"], r'Soḷasa dhātuyo na vattabbā – "parāmāsā ceva parāmaṭṭhā cāti parāmaṭṭhā ceva no ca parāmāsā"\.',
     f"ဓာတ် ဆယ့်ခြောက်ပါးသည် – “{_MY}လည်း ဖြစ်၊ {_MY}၏ အာရုံလည်း ဖြစ်နိုင်သော သဘောတရားများဟု {_MY}၏ အာရုံ "
     f"ဖြစ်နိုင်သော်လည်း {_MY} မဟုတ်သော သဘောတရားများ” ခေါ်ဆို၍ မရ။",
     f"ဓာတ် ဆယ့်ခြောက်ပါးသည် – “{_MY}လည်း ဖြစ်၊ {_MY}၏ အာရုံလည်း ဖြစ်နိုင်သော သဘောတရားများ”ဟု ခေါ်ဆို၍ မရ၊ {_MY}၏ အာရုံ "
     f"ဖြစ်နိုင်သော်လည်း {_MY} မဟုတ်သော သဘောတရားများ ဖြစ်ကြသည်။", 1),
    ("F2 A4 ^2-223 «siyā …, na vattabbā – ‘…’ti» = «…၊ သို့သော် – “…”ဟု ခေါ်ဆို၍ မရ» (as 2-ayatana, 4-sacca)",
     ["2-223"], r'siyā (?:uppādino|anuppannā), na vattabbā – "(?:anuppannā|uppādino)"ti',
     "ဖြစ်ကြသည်၊ – “", "ဖြစ်ကြသည်၊ သို့သော် – “", 2),
    ("F3 A5 ^2-184 «… tajjāmanoviññāṇadhātu manañca paṭicca …» = «… ဖြစ်ပေါ်သည်၊ မနောကိုလည်းကောင်း» (two clauses)",
     ["2-184"], r"tajjāmanoviññāṇadhātu manañca paṭicca dhamme ca",
     "ဓာတ် ဖြစ်ပေါ်သည် မနောကိုလည်းကောင်း၊", "ဓာတ် ဖြစ်ပေါ်သည်၊ မနောကိုလည်းကောင်း၊", 1),
    ("F4 B3 «Idha bhikkhu» = «ဤသာသနာ၌ ရဟန်းသည်» (as the 148 others)", ["2-724", "2-796"], r"\bIdha bhikkhu\b",
     "ဤသာသနာတော်၌ ရဟန်းသည်", "ဤသာသနာ၌ ရဟန်းသည်", 2),
    ("F5 B5 ^2-392 list «၊» after the variant bracket («samuṭṭhapeti [variant] nibbatteti»)", ["2-392"],
     r"samuṭṭhapeti \[uṭṭhāpeti samuṭṭhāpeti \(syā\.\) evamuparipi\] nibbatteti",
     "နောက်ပိုင်း၌လည်း ဤနည်းတူ] ပေါ်ထွက်စေ၏", "နောက်ပိုင်း၌လည်း ဤနည်းတူ]၊ ပေါ်ထွက်စေ၏", 1),
    ("F6 B1 ^2-U30 kummaggasevanā: the object is the wrong path, «မှီဝဲခြင်း» as the heading (path senses sevanā|1, nisevanā|1, taṃsampavaṅkatā, user-approved 2026-11-18)", ["2-U30"],
     r"Yā imassa kummaggassa sevanā nisevanā saṃsevanā bhajanā sambhajanā bhatti sambhatti taṃsampavaṅkatā",
     _B1_OLD, _B1_NEW, 1),
    ("F7 A3 (extended to ch14 / ch15, user decision 2026-11-18): compressed citta openings = the ch6 adverbial qualifiers",
     F7_IDS, r"sahagat(?:aṃ|ā) \w+(?:sampayutt|vippayutt)(?:aṃ|ā)(?: sasaṅkhārena)?…pe…", None, f7, 9),
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


def main():
    files = sorted(p.name for p in PALI.glob("*.md"))
    pali = {f: (PALI / f).read_text(encoding="utf-8").split("\n") for f in files}
    text = {f: (OUT / f).read_text(encoding="utf-8").split("\n") for f in files}
    pseg = {f: segs(pali[f]) for f in files}
    mseg = {f: dict(segs(text[f])) for f in files}
    log, errors, counts = [], [], {}
    for rule, ids, trig, old, new, expect in RULES:
        trig_re = re.compile(trig)
        done, found = 0, set()
        for f in files:
            for i, pidx in pseg[f]:
                if i not in ids:
                    continue
                found.add(i)
                midx = mseg[f].get(i)
                if midx is None or len(midx) != len(pidx):
                    errors.append(f"{rule}: {f} {i}: segment missing or not line-aligned")
                    continue
                for pk, mk in zip(pidx, midx):
                    if not trig_re.search(pali[f][pk]):
                        continue
                    if old is None:                       # pattern function: new(pali, burmese) -> (burmese, [(o, n)])
                        try:
                            text[f][mk], ch = new(pali[f][pk], text[f][mk])
                        except ValueError as e:
                            errors.append(f"{rule[:12]}: {f[:-3]} {i} line {mk + 1}: {e}")
                            continue
                        done += len(ch)
                        log += [(f[:-3], i, str(mk + 1), o, n_, rule) for o, n_ in ch]
                        continue
                    n = text[f][mk].count(old)
                    if n:
                        text[f][mk] = text[f][mk].replace(old, new)
                        done += n
                        log += [(f[:-3], i, str(mk + 1), old, new, rule)] * n
        if found != set(ids):
            errors.append(f"{rule}: segments not found: {sorted(set(ids) - found)}")
        counts[rule] = done
        if done != expect:
            errors.append(f"{rule}: {done} replacements, expected {expect}")
    for a, b in F7_SAME_AS_CH6.items():                     # F7: identical Pāli opening = ch6's Burmese
        o = {}
        for i in (a, b):
            f = next(f for f in files if i in mseg[f])
            line = text[f][mseg[f][i][-1]]
            o[i] = line[line.index("။ ") + 2:line.index("အချိန်၌")]
        if o[a] != o[b]:
            errors.append(f"F7: opening of ^{a} differs from ch6 ^{b}")
    for rule, n in counts.items():
        print(f"{n:6d}  {rule[:110]}")
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
