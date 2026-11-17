"""Find Russian divergences for identical Pāli across the pi-2 (Vibhaṅga) Russian zero-shot chapters,
and against the finished, reviewed Russian pi-1 (rails text).

(a) within pi-2: whole segments / whole lines / clauses / items / synonym-string words, grouped by normalised
    Pāli (block ID and variant brackets stripped, spaces collapsed, no space before punctuation);
    groups whose Russian differs are listed.
(b) pi-2 vs pi-1: the same units whose normalised Pāli also occurs in pi-1; listed where the Russian differs
    (pi-1 Russian wins).
(c) recurring terms and phrases: for each Pāli pattern in PHRASES, count per chapter which candidate Russian
    forms occur on the aligned Russian lines (and how many matching lines carry none of the candidates).

usage: python -I -X utf8 find_divergences_ru.py [out.md] [--bak] [--no-c]
       (default out: divergences.md; --bak scans backup-pre-harmonise/, i.e. the state before the pass)
"""
import os, re, sys, collections, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ru_common
from ru_common import PARTS, PARTS1, HERE, pairs, segments, segments1, norm, short

SPLIT = re.compile(r"(?<=[?.;:])\s+")
SPLIT_ITEM_P = re.compile(r"(?<=[?.;:,])\s+|\s+[–—]\s+|…pe…\s*")
SPLIT_ITEM_R = re.compile(r"(?<=[?.;:,])\s+|\s+[–—]\s+|…\s*")


def rnorm(s):
    return norm(s).rstrip(".?;: ")


def units(segs, tag):
    """yield (kind, pali_key, russian, loc) for segments, lines, clauses, items"""
    for sid, ps, rs in segs:
        loc = f"{tag}:{sid}"
        yield "seg", " / ".join(norm(x) for x in ps), " / ".join(norm(x) for x in rs), loc
        for p, r in zip(ps, rs):
            np_, nr = norm(p), norm(r)
            yield "line", np_, nr, loc
            if p.startswith("#"):
                continue
            cp = [c for c in SPLIT.split(np_) if c]
            cr = [c for c in SPLIT.split(nr) if c]
            if len(cp) == len(cr) and len(cp) > 1:
                for a, b in zip(cp, cr):
                    yield "clause", a, rnorm(b), loc
            ip = [c for c in SPLIT_ITEM_P.split(np_) if c]
            ir = [c for c in SPLIT_ITEM_R.split(nr) if c]
            if len(ip) == len(ir) and len(ip) > 1:
                for a, b in zip(ip, ir):
                    yield "item", a.rstrip(",.;:?"), rnorm(b).rstrip(","), loc


P_STR = re.compile(r"\b(?:Yo|Yā|Yaṃ|yo|yā|yaṃ) (?:tasmiṃ samaye )?(?:cetasiko |cittassa )?(.+?)\s+[–—]\s")
R_STR = re.compile(r"(?:То, что|то, что) (?:[^–]*? )?(?:есть|является) (?:такое |такая |такой )?(.+?),?\s+[–—]\s")


def words(segs, tag):
    for sid, ps, rs in segs:
        for p, r in zip(ps, rs):
            p, r = norm(p), norm(r)
            mp, mr = P_STR.findall(p), R_STR.findall(r)
            if len(mp) != len(mr):
                continue
            for a, b in zip(mp, mr):
                pw = [w for w in a.replace("…pe…", " ").split() if w]
                rw = [w.strip() for w in re.split(r",\s+|…\s*", b) if w.strip()]
                if len(pw) == len(rw) and len(pw) > 2:
                    for x, y in zip(pw, rw):
                        yield "word", x.strip(",.;"), y, f"{tag}:{sid}"


def diff(a, b):
    ta, tb = a.split(), b.split()
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            out.append(f"«{' '.join(ta[i1:i2])}» → «{' '.join(tb[j1:j2])}»")
    return "; ".join(out)


MINLEN = {"seg": 0, "line": 3, "clause": 12, "item": 6, "word": 3}
CROSS_ONLY = {"item", "word"}

# Groups left on purpose (identical Pāli key, Russian differs for a reason): listed, not counted.
_AGR = "agreement with subjects of different number / gender (the Pāli subject differs)"
_SPLIT_N = ("context split: ch16 classification of knowledge = pi-1 Rūpakaṇḍa «Классификация …»; ch17 groups of "
            "listed items «Единицы … Десятки» (as pi-1 4-01/5 «Тройки.»); ch12 the jhāna method «Четверичный / "
            "Пятеричный метод»")
EXPLAINED = {
    "Tattha katamaṃ saṅkhārapaccayā viññāṇaṃ?": "saṅkhāra plural in the Suttanta section (^2-227), singular in the "
                                                 "Abhidhamma section (notes-6: deliberate)",
    "Tattha katamaṃ dukkhaṃ?": "dukkha = «боль» where it is the bodily pain of the soka … upāyāsa list (^2-196, ^2-239; "
                               "notes-4-5: deliberate), «страдание» elsewhere",
    "siyā lokuttarā": _AGR, "kenaci na viññeyyā": _AGR, "atthi akusalaṃ": _AGR, "atthi abyākataṃ": _AGR,
    "siyā nevavipākanavipākadhammadhammā": _AGR, "siyā anāgatā": _AGR, "siyā paccuppannā": _AGR,
    "siyā bahiddhā": _AGR, "siyā ajjhattabahiddhā": _AGR,
    "jīvitindriyaṃ": "item-alignment artifact (ch1 ^2-33, approved sample: «… и та материальная форма» is the next "
                     "Pāli item's Russian)",
    "phoṭṭhabbāyatanaṃ": "item-alignment artifact (ch1 ^2-33, approved sample)",
    "ṭhiti": "string-word artifact: ṭhiti of the vīriya string «устойчивость» vs cittassa ṭhiti «устойчивость ума»",
    "Ekakaṃ.": _SPLIT_N, "Dukaṃ.": _SPLIT_N, "Tikaṃ.": _SPLIT_N, "Catukkaṃ.": _SPLIT_N, "Pañcakaṃ.": _SPLIT_N,
    "Chakkaṃ.": _SPLIT_N, "Sattakaṃ.": _SPLIT_N, "Aṭṭhakaṃ.": _SPLIT_N, "Navakaṃ.": _SPLIT_N, "Dasakaṃ.": _SPLIT_N,
    "##### Tikaṃ": "context split: question-section heading = the matrix triads «Тройки» (pi-1 4-01 «Тройки.»), "
                   "pi-1 Rūpakaṇḍa heading «Классификация на три вида» is the classification of matter",
    "##### Dukaṃ": "context split: question-section heading = the matrix dyads «Пары» (pi-1 «Матрица пар»), pi-1 "
                   "Rūpakaṇḍa heading «Классификация на два вида» is the classification of matter",
}
EXPL_SEEN = []


def collect2():
    g = {k: collections.defaultdict(lambda: collections.defaultdict(list)) for k in MINLEN}
    for part in PARTS:
        segs = segments(part)
        for kind, kp, kr, loc in list(units(segs, short(part))) + list(words(segs, short(part))):
            g[kind][kp][kr].append(loc)
    return g


def collect1():
    g = {k: collections.defaultdict(collections.Counter) for k in MINLEN}
    for part in PARTS1:
        segs = segments1(part)
        for kind, kp, kr, loc in list(units(segs, "pi1-" + part[:4])) + list(words(segs, "pi1")):
            g[kind][kp][kr] += 1
    return g


def report_a(groups, kind, title):
    out = [f"## {title}", ""]
    n = 0
    for k, v in sorted(groups.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        if len(v) < 2 or len(k) < MINLEN[kind]:
            continue
        if len({rnorm(x) for x in v}) < 2:
            continue
        if kind in CROSS_ONLY:
            fsets = [{l.split(':')[0] for l in locs} for locs in v.values()]
            if len(set().union(*fsets)) < 2:
                continue
        if k in EXPLAINED:
            EXPL_SEEN.append((title[:4], k, {r: locs[:3] for r, locs in v.items()}))
            continue
        n += 1
        out.append(f"### {k[:300]}")
        ranked = sorted(v.items(), key=lambda kv: -len(kv[1]))
        top = ranked[0][0]
        for r, locs in ranked:
            files = sorted({l.split(':')[0] for l in locs})
            d = "" if r == top else f"  ⟨diff vs first: {diff(top, r)[:400]}⟩"
            out.append(f"- [{len(locs)}] {','.join(files)} ({', '.join(locs[:4])}) :: {r[:400]}{d}")
        out.append("")
    out.insert(1, f"groups with differing Russian: {n}")
    return out, n


_P1LINES = []


def pi1_lines():
    if not _P1LINES:
        for part in PARTS1:
            for sid, ps, rs in segments1(part):
                _P1LINES.extend((norm(p), norm(r)) for p, r in zip(ps, rs))
    return _P1LINES


def report_b(g2, g1, kind, title):
    out = [f"## {title}", ""]
    n = 0
    for k, v in sorted(g2[kind].items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        if k not in g1[kind] or len(k) < max(MINLEN[kind], 3):
            continue
        r1 = g1[kind][k]
        r1n = {rnorm(x) for x in r1}
        bad = {r: locs for r, locs in v.items() if rnorm(r) not in r1n}
        if kind in ("item", "word"):  # item alignment can slip in pi-1: accept a form pi-1 has for the same Pāli
            bad = {r: locs for r, locs in bad.items()
                   if not any(k in pp and rnorm(r) in rr for pp, rr in pi1_lines())}
        if not bad:
            continue
        if k in EXPLAINED:
            EXPL_SEEN.append((title[:4], k, {r: locs[:3] for r, locs in bad.items()}))
            continue
        n += 1
        top = r1.most_common(1)[0][0]
        out.append(f"### {k[:300]}")
        for r, c in r1.most_common():
            out.append(f"- pi-1 [{c}] :: {r[:400]}")
        for r, locs in sorted(bad.items(), key=lambda kv: -len(kv[1])):
            out.append(f"- pi-2 [{len(locs)}] ({', '.join(locs[:5])}) :: {r[:400]}  ⟨vs pi-1: {diff(top, r)[:400]}⟩")
        out.append("")
    out.insert(1, f"groups where pi-2 differs from pi-1: {n}")
    return out, n


# ---------------------------------------------------------------- (c) recurring terms and phrases
PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), cands))


ph("kāmesumicchācāra", r"kāmesumicchācār", "неправильное поведение в чувственных удовольствиях",
   "неподобающее поведение", "неправильного поведения", "в чувственных")
ph("veramaṇī", r"veramaṇ", "воздержани", "уклонени")
ph("vīriyārambha string", r"vīriyārambho nikkamo", "сила усердия, правильное усилие", "сила усердия,", "правильное усилие")
ph("vīriyindriya / vīriyabala", r"vīriyindriyaṃ vīriyabalaṃ", "способность усердия, сила усердия")
ph("paññā string", r"paññā pajānanā", "мудрость, понимание", "понимание")
ph("sati string", r"sati anussati", "осознанность, припоминание", "памятовани")
ph("samādhi string", r"cittassa ṭhiti saṇṭhiti", "устойчивость ума", "стабильность ума", "пребывание ума")
ph("vivicceva kāmehi", r"vivicceva kāmehi", "полностью уединившись от чувственных удовольствий",
   "отстранившись от чувственных удовольствий")
ph("savitakkaṃ savicāraṃ", r"savitakkaṃ savicāraṃ", "с направленной мыслью и удержанием мысли")
ph("vitakkavicārānaṃ vūpasamā", r"vitakkavicārānaṃ vūpasamā", "с затиханием направленной мысли и удержания мысли",
   "с успокоением направленной мысли")
ph("ajjhattaṃ sampasādanaṃ", r"ajjhattaṃ sampasādanaṃ", "с ясностью внутри себя, с единением ума")
ph("pītiyā ca virāgā", r"pītiyā ca virāgā", "с угасанием восторга")
ph("upekkhako ca viharati", r"upekkhako ca viharati", "пребывает невозмутимым")
ph("sukhassa ca pahānā", r"sukhassa ca pahānā", "с устранением приятного", "с устранением счастья")
ph("upasampajja viharati", r"upasampajja viharati", "входит в", "и пребывает в нём", "достигает")
ph("lokuttara opening", r"lokuttaraṃ jhānaṃ bhāveti", "человек, развивая надмирское", "развивает надмирское")
ph("niyyānika apacayagāmi", r"niyyānikaṃ apacayagāmiṃ", "ведущее к освобождению и к убыванию", "ведущее к выходу")
ph("diṭṭhigatānaṃ pahānāya", r"diṭṭhigatānaṃ pahānāya", "для устранения воззрений", "для отказа от воззрений",
   "приверженност")
ph("paṭhamāya bhūmiyā pattiyā", r"paṭhamāya bhūmiyā pattiyā", "для достижения первой ступени", "первого уровня",
   "первой ступени")
ph("vuccati \"X\"", r"vuccati \"", "это называется «", "называется «")
ph("na vattabba", r"(?i)na vattabb", "нельзя определить", "нельзя сказать", "не следует говорить", "не следует")
ph("sajjha", r"sajjh", "серебро", "необработанное серебро", "чеканное серебро")
ph("rajata", r"rajat", "серебро", "монеты")
ph("dhamme ñāṇaṃ", r"dhamme ñāṇaṃ", "знание Учения", "знание явлений", "знание о явлениях")
ph("abhiññeyya", r"abhiññeyy", "следует постичь высшим знанием", "высшим знанием", "постичь")
ph("pariññeyya", r"pariññeyy", "следует полностью понять", "полностью понять", "следует понять")
ph("Akaniṭṭha", r"[Aa]kaniṭṭh", "высочайшие боги", "высочайших богов", "Аканиттха")
ph("ākāsānañcāyatanūpaga devā", r"ākāsānañcāyatan\w*(?:upag|ūpag)", "боги, достигшие сферы", "богов, рождённых в сфере",
   "рождённые в сфере", "достигших сферы")
ph("Brahmapārisajja", r"[Bb]rahmapārisajj", "боги свиты Брахмы", "свиты Брахмы")
ph("Cātumahārājika", r"[Cc]ātumahārājik", "боги Четырёх Великих Царей", "Четырёх Великих Царей", "четырёх великих царей")
ph("Tāvatiṃsa", r"[Tt]āvatiṃs", "боги Тридцати трёх", "Тридцати трёх", "тридцати трёх")
ph("Yāma", r"\b[Yy]āmā\b|\b[Yy]āmānaṃ", "боги Ямы", "Ямы", "яма")
ph("Tusita", r"[Tt]usit", "богов Тушиты", "Тушит")
ph("Nimmānarati", r"[Nn]immānarat", "радующ", "творени")
ph("Paranimmitavasavattī", r"[Pp]aranimmitavasavatt", "властвующ", "чужи")
ph("kāmāvacara", r"kāmāvacar", "к миру чувственных желаний", "мир чувственных желаний", "в мире чувственных желаний")
ph("rūpāvacara", r"\brūpāvacar", "к миру форм", "в мире форм", "мир форм")
ph("arūpāvacara", r"arūpāvacar", "к миру без форм", "в мире без форм", "мир без форм")
ph("kusalā dhammā (question section)", r"kusalā,? (?:siyā )?akusalā", "благ", "неблаг")
ph("Tīṇi / cattāri X (counted)", r"^(?:Tīṇi|Cattāri|Pañca|Cha|Satta|Aṭṭha|Nava|Dasa) \w+ni\b",
   "вида", "видов", "основ", "три", "четыре")
ph("ṭhapetvā", r"[Ṭṭ]hapetvā", "кроме", "за исключением")
ph("kammassa katattā", r"kammassa katattā", "вследствие совершённого и накопленного", "вследствие совершённых действий")
ph("sammappadhāna", r"sammappadhān", "правильное усилие", "правильных усили", "правильного усилия")
ph("saṅgati", r"saṅgati", "встреча", "сочетани")
ph("sīlabbataparāmāsa", r"(?i)sīlabbataparāmās", "искажение обрядов и обетов", "приверженность обрядам")
ph("sakkāyadiṭṭhi", r"(?i)sakkāyadiṭṭh", "воззрение о личности", "воззрения о личности", "личност")
ph("vicikicchā", r"[Vv]icikicch", "колебани", "сомнени")
ph("kukkucca", r"[Kk]ukkucc", "угрызени", "сожалени", "раскаяни")
ph("uddhacca", r"[Uu]ddhacc", "беспокойств", "возбуждени")
ph("thinamiddha", r"[Tt]hinamiddh", "вялость и сонливость", "вялости и сонливости", "вялост")
ph("ātāpī", r"ātāpī", "ревностный", "ревностен", "усердн")
ph("satipaṭṭhāna", r"satipaṭṭhān", "основ осознанности", "основа осознанности", "основы осознанности")
ph("iddhipāda", r"iddhipād", "основ сверхспособностей", "основа сверхспособностей", "основы сверхспособностей")
ph("bojjhaṅga", r"bojjhaṅg", "фактор пробуждения", "факторов пробуждения", "факторы пробуждения")
ph("upādānakkhandha", r"upādānakkhandh", "совокупност", "служащ")
ph("ariyasacca", r"ariyasacc", "благородн")
ph("dukkhanirodhagāminī paṭipadā", r"dukkhanirodhagāminī", "способ практики, ведущий к прекращению страдания",
   "практика, ведущая к прекращению страдания")
ph("kāmataṇhā", r"kāmataṇh", "чувственная жажда", "жажда чувственных удовольствий")
ph("brahmavihāra pervasion", r"ekaṃ disaṃ pharitvā", "пронизав", "наполнив")
ph("mettā", r"\b[Mm]ett", "доброжелательност", "дружелюби", "любящ")
ph("karuṇā", r"\b[Kk]aruṇ", "сострадани")
ph("muditā", r"\b[Mm]udit", "сорадовани", "радост")
ph("paṭisambhidā", r"paṭisambhid", "аналитическое знание", "аналитических знаний", "аналитического знания")
ph("Tathāgata", r"[Tt]athāgat", "Татхагат")
ph("anusaya", r"anusay", "скрыт", "склонност")
ph("pātimokkha", r"pātimokkh", "свод монашеских правил", "свода монашеских правил", "сводом монашеских правил")
ph("mada", r"\bmad[oaā]\b", "опьянени", "упоени")


def scan_c():
    out = ["## (c) recurring terms and phrases: candidate Russian forms per chapter", "",
           "Counts are occurrences of each candidate string on Russian lines whose aligned Pāli matches; "
           "_lines = matching lines, _none = matching lines with no candidate (overlapping candidates counted separately).", ""]
    for name, rx, cands in PHRASES:
        cnt = collections.defaultdict(collections.Counter)
        for part in PARTS:
            for p, r in pairs(part):
                if not rx.search(p):
                    continue
                cnt[part]["_lines"] += 1
                hit = False
                for c in cands:
                    k = r.count(c)
                    if k:
                        cnt[part][c] += k; hit = True
                if not hit:
                    cnt[part]["_none"] += 1
        out.append(f"### {name}  (`{rx.pattern}`)")
        for part in PARTS:
            if part in cnt:
                c = cnt[part]
                items = ", ".join(f"{k}={v}" for k, v in c.items() if not k.startswith("_"))
                out.append(f"- {short(part)}: lines={c['_lines']} none={c['_none']} | {items}")
        out.append("")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--bak" in sys.argv:
        ru_common.CUR["rdir"] = ru_common.BAK
    dest = args[0] if args else os.path.join(HERE, "divergences.md")
    g2 = collect2()
    g1 = collect1()
    body, counts = [], {}
    for kind, title in [("seg", "(a1) whole segments: identical Pāli, differing Russian"),
                        ("line", "(a2) whole lines"),
                        ("clause", "(a3) clauses (sentence parts of lines whose clause counts match)"),
                        ("item", "(a4) comma/dash/ellipsis items (cross-chapter only)"),
                        ("word", "(a5) words of synonym strings (cross-chapter only)")]:
        o, n = report_a(g2[kind], kind, title)
        body += o; counts["a-" + kind] = n
    for kind, title in [("seg", "(b1) whole segments identical to a pi-1 segment"),
                        ("line", "(b2) whole lines identical to a pi-1 line"),
                        ("clause", "(b3) clauses identical to a pi-1 clause"),
                        ("item", "(b4) items identical to a pi-1 item"),
                        ("word", "(b5) synonym-string words identical to pi-1's")]:
        o, n = report_b(g2, g1, kind, title)
        body += o; counts["b-" + kind] = n
    body += ["## Left on purpose (identical Pāli key, Russian differs for a stated reason; not counted above)", ""]
    for sec, k, forms in EXPL_SEEN:
        body.append(f"- {sec} «{k}»: {EXPLAINED[k]}")
        for r, locs in forms.items():
            body.append(f"    - {r[:160]} ({', '.join(locs)})")
    body.append("")
    counts["explained"] = len(EXPL_SEEN)
    oc = scan_c() if "--no-c" not in sys.argv else []
    src = "backup-pre-harmonise (before the pass)" if "--bak" in sys.argv else "current outputs"
    head = ["# pi-2 Russian zero-shot: divergences (find_divergences_ru.py)", "", f"Scanned: {src}.", "",
            "; ".join(f"{k}: {v}" for k, v in counts.items()), ""]
    open(dest, "w", encoding="utf-8", newline="\n").write("\n".join(head + body + oc) + "\n")
    print(counts, "->", dest)


if __name__ == "__main__":
    main()
