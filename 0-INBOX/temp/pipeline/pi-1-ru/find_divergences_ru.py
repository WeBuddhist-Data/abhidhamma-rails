"""Find Russian divergences for identical Pāli across the pi-1 Russian zero-shot parts.

(a) whole segments / whole lines / clauses / items: group by normalised Pāli (block ID and variant brackets
    stripped, spaces collapsed); list groups where the Russian differs.
(b) recurring phrases: for each Pāli pattern in PHRASES, count per part which candidate Russian forms occur on
    the aligned Russian lines (and how many matching lines carry none of the candidates).

usage: python -I -X utf8 find_divergences_ru.py [out.md] [--bak] [--no-b]
       (default out: divergences.md; --bak scans backup-pre-harmonise/, i.e. the state before the pass)
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ru_common
from ru_common import PARTS, HERE, pairs, segments, norm, short

SPLIT_P = re.compile(r"(?<=[?.;:])\s+")
SPLIT_R = re.compile(r"(?<=[?.;:])\s+")


def rnorm(s):
    return norm(s).rstrip(".?;: ")


def scan_a():
    seg = collections.defaultdict(lambda: collections.defaultdict(list))
    line = collections.defaultdict(lambda: collections.defaultdict(list))
    clause = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for sid, ps, rs in segments(part):
            kp = " / ".join(norm(x) for x in ps)
            kr = " / ".join(norm(x) for x in rs)
            seg[kp][kr].append(f"{short(part)}:{sid}")
            for p, r in zip(ps, rs):
                np_, nr = norm(p), norm(r)
                line[np_][nr].append(f"{short(part)}:{sid}")
                if p.startswith("#"):
                    continue
                cp = [c for c in SPLIT_P.split(np_) if c]
                cr = [c for c in SPLIT_R.split(nr) if c]
                if len(cp) == len(cr) and len(cp) > 1:
                    for a, b in zip(cp, cr):
                        clause[a][rnorm(b)].append(f"{short(part)}:{sid}")
    return seg, line, clause


SPLIT_ITEM_P = re.compile(r"(?<=[?.;:,])\s+|\s+[–—]\s+|…pe…\s*")
SPLIT_ITEM_R = re.compile(r"(?<=[?.;:,])\s+|\s+[–—]\s+|…\s*")


def scan_items():
    """comma / dash / ellipsis items of lines whose item counts match"""
    item = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for sid, ps, rs in segments(part):
            for p, r in zip(ps, rs):
                if p.startswith("#"):
                    continue
                cp = [c for c in SPLIT_ITEM_P.split(norm(p)) if c]
                cr = [c for c in SPLIT_ITEM_R.split(norm(r)) if c]
                if len(cp) == len(cr) and len(cp) > 1:
                    for a, b in zip(cp, cr):
                        item[a.rstrip(",.;:?")][rnorm(b).rstrip(",")].append(f"{short(part)}:{sid}")
    return item


P_STR = re.compile(r"\b(?:Yo|Yā|Yaṃ|yo|yā|yaṃ) (?:tasmiṃ samaye )?(?:evarūpo |evarūpā |evarūpaṃ )?(.+?)\s+[–—]\s")
R_STR = re.compile(r"(?:То, что|то, что) (?:[^–]*? )?(?:есть|является) (?:такое |такая |такой )?(.+?),?\s+[–—]\s")


def scan_words():
    """synonym strings: Pāli words (space-separated) vs Russian items (comma-separated) when the counts match"""
    word = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for sid, ps, rs in segments(part):
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
                            word[x.strip(",.;")][y].append(f"{short(part)}:{sid}")
    return word


def diff(a, b):
    import difflib
    ta, tb = a.split(), b.split()
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            out.append(f"«{' '.join(ta[i1:i2])}» → «{' '.join(tb[j1:j2])}»")
    return "; ".join(out)


def report(groups, title, minlen=0, cross_only=False):
    out = [f"## {title}", ""]
    n = 0
    for k, v in sorted(groups.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        if len(v) < 2 or len(k) < minlen:
            continue
        keys = {rnorm(x) for x in v}
        if len(keys) < 2:
            continue
        if cross_only:
            fsets = [{l.split(':')[0] for l in locs} for locs in v.values()]
            if len(set().union(*fsets)) < 2:
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


# (b) phrase table: pali regex -> candidate Russian forms
PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), cands))


ph("vivicceva kāmehi", r"vivicceva kāmehi", "полностью уединившись от чувственных удовольствий",
   "отстранившись от чувственных удовольствий", "от чувственных желаний")
ph("vivicca akusalehi dhammehi", r"vivicca akusalehi", "уединившись от неблагих явлений", "отстранившись от неблагих")
ph("savitakkaṃ savicāraṃ vivekajaṃ", r"savitakkaṃ savicāraṃ", "с направленной мыслью и удержанием мысли",
   "рождёнными уединением")
ph("vitakkavicārānaṃ vūpasamā", r"vitakkavicārānaṃ vūpasamā", "с затиханием направленной мысли и удержания мысли",
   "с успокоением направленной мысли")
ph("ajjhattaṃ sampasādanaṃ", r"ajjhattaṃ sampasādanaṃ", "с внутренней ясностью и единением ума")
ph("pītiyā ca virāgā", r"pītiyā ca virāgā", "с угасанием восторга")
ph("upekkhako ca viharati", r"upekkhako ca viharati", "пребывает невозмутимым", "осознанным и ясно понимающим")
ph("sukhassa ca pahānā", r"sukhassa ca pahānā", "с устранением приятного", "и с устранением приятного")
ph("upasampajja viharati", r"upasampajja viharati", "входит в", "и пребывает в нём", "достигает")
ph("bhāveti (subject)", r"bhāveti", "человек, развивая", "человек развивает", "развивают")
ph("paṭipadā", r"paṭipad", "с трудным способом практики", "с лёгким способом практики",
   "с болезненным способом практики", "с приятным способом практики")
ph("abhiññā", r"abhiññ", "медленным высшим знанием", "быстрым высшим знанием")
ph("adhipateyya", r"dhipateyy", "при преобладании желания", "при преобладании усердия", "при преобладании ума",
   "при преобладании пытливости", "при преобладании исследования")
ph("vīmaṃsā", r"vīmaṃs", "пытливост", "исследовани")
ph("kasiṇa", r"kasiṇ", "на всеохватном объекте", "всеохватн", "касин")
ph("āruppa / arūpāvacara", r"āruppa|arūpāvacar|arūpūpapatt", "к миру без форм", "в мире без форм", "без форм",
   "бесформ", "нематериальн")
ph("rūpāvacara", r"rūpāvacar|rūpūpapatt", "к миру форм", "в мире форм", "мир форм")
ph("kāmāvacara", r"kāmāvacar", "к миру чувственных желаний", "мир чувственных желаний", "чувственн")
ph("sasaṅkhāra", r"sasaṅkhār", "с побуждением", "побуждени")
ph("asaṅkhāra", r"asaṅkhār", "без побуждения")
ph("bhūmi", r"bhūmīsu|bhūmiy|bhūmik|bhūmak", "ступен", "мир", "уров", "сфер", "план")
ph("cittuppāda", r"cittuppād", "вид ума", "видов ума", "возникновение ума", "возникновения ума", "возникновени")
ph("counting line", r"Tasmiṃ kho pana samaye", "И в это время есть", "В это время есть", "И в это время")
ph("ṭhapetvā", r"ṭhapetvā", "кроме", "за исключением", "исключая")
ph("tadekaṭṭha", r"[Tt]adekaṭṭh", "пребывающ", "находящ", "в одном месте", "существующ", "одном и том же",
   "сопутствующ")
ph("kammassa katattā", r"kammassa katattā", "вследствие совершённого действия", "вследствие совершённых действий",
   "вследствие того, что было совершено", "совершено")
ph("sāta", r"\bsāt", "отрадн", "приятн")
ph("asāta", r"\basāt", "безотрадн", "неотрадн", "неприятн")
ph("viññatti", r"viññatt", "внешнее выражение", "внешнего выражения", "сообщени", "выражени")
ph("upacaya", r"upacay", "рост", "нарастани", "накоплени")
ph("santati", r"santati", "непрерывност", "поток", "продолжени")
ph("kakkhaḷa", r"kakkhaḷ", "твёрд", "грубост", "жёстк")
ph("diṭṭhigata", r"diṭṭhigat", "приверженност", "ложное воззрение", "ложного воззрения", "воззрени")
ph("micchādiṭṭhi", r"micchādiṭṭh", "ложное воззрение", "ложного воззрения", "неправильн")
ph("sakkāyadiṭṭhi", r"(?i)sakkāyadiṭṭh", "воззрение о личности", "воззрения о личности", "воззрение о существовании",
   "о постоянной личности", "личност")
ph("sīlabbataparāmāsa", r"(?i)sīlabbataparāmās", "искажение обрядов и обетов", "приверженность обрядам и обетам",
   "обряд", "нравственност", "добродетел")
ph("sīlabbatupādāna", r"(?i)sīlabbatupādān", "цепляние за обряды и обеты", "обряд", "нравственност")
ph("lobha", r"\b[Ll]obh", "жадност", "алчност")
ph("dosa", r"\b[Dd]os[oaā]", "злоб", "ненавист")
ph("moha", r"\b[Mm]oh[oaā]", "заблуждени", "омрачённост")
ph("diṭṭhi", r"[Dd]iṭṭhi", "воззрени")
ph("vicikicchā", r"[Vv]icikicch", "колебани", "сомнени")
ph("uddhacca", r"[Uu]ddhacc", "беспокойств", "возбуждени")
ph("thina", r"\b[Tt]hin", "вялост", "косност")
ph("middha", r"[Mm]iddh", "сонливост", "оцепенени")
ph("kukkucca", r"[Kk]ukkucc", "угрызени", "сожалени", "раскаяни")
ph("māna", r"\b[Mm]ān[oaā]\b|\bmānaṃ", "самомнени", "гордост", "высокомери")
ph("issā", r"\b[Ii]ssā", "завист", "ревност")
ph("macchariya", r"[Mm]acchari", "скупост", "жадност")
ph("āsava", r"[Aa]sav", "влечени")
ph("saṃyojana", r"[Ss]aṃyojan", "оков")
ph("gantha", r"[Gg]anth", "уз")
ph("ogha", r"\b[Oo]gh", "поток")
ph("yoga", r"\b[Yy]og[aāo]", "ярм")
ph("nīvaraṇa", r"[Nn]īvaraṇ", "помех")
ph("upādāna", r"[Uu]pādān", "цепляни")
ph("kilesa", r"[Kk]iles", "омрачени")
ph("parāmāsa", r"[Pp]arāmās|parāmaṭṭh", "искажени", "приверженност")
ph("sārāga", r"sārāg", "сильная страсть", "пристрасти", "страсть")
ph("bahūsu", r"bahūsu", "(во многих изданиях)", "во многих")
ph("patiṭṭhāho", r"patiṭṭhāh", "закреплени", "цепкост")
ph("sammappadhāna", r"sammappadhān", "правильное усилие", "правильного усилия")
ph("kabaḷīkāra", r"kabaḷīkār", "съедаемая пища", "съедаемой пищ", "пища")
ph("Tattha", r"\bTattha\b", "Среди них", "Здесь", "Из них", "Там")
ph("na vattabba", r"(?i)na vattabb", "нельзя сказать", "не следует говорить", "не следует называть")
ph("Teva / Tāneva frame", r"(Tāneva|Teyeva|Teva) ", "Те же самые", "Они же", "Те же")
ph("cittasamuṭṭhāna", r"cittasamuṭṭhān", "порождённ", "возникающ", "происходящ")
ph("upādārūpa", r"upādārūp|upādā rūp", "производн", "зависим")
ph("mahābhūta", r"mahābhūt", "великих элемент", "великие элемент", "первоэлемент")
ph("avasesa", r"[Aa]vases", "остальн", "оставш")


def scan_b():
    tab = []
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
        tab.append((name, rx.pattern, cnt))
    out = ["## (b) recurring phrases: candidate Russian forms per part", "",
           "Counts are occurrences of each candidate string on Russian lines whose aligned Pāli matches; "
           "_lines = matching lines, _none = matching lines with no candidate (overlapping candidates are counted separately).", ""]
    for name, pat, cnt in tab:
        out.append(f"### {name}  (`{pat}`)")
        for part in PARTS:
            if part in cnt:
                c = cnt[part]
                items = ", ".join(f"{k}={v}" for k, v in c.items() if not k.startswith("_"))
                out.append(f"- {short(part)}: lines={c['_lines']} none={c['_none']} | {items}")
        out.append("")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--bak" in sys.argv:  # scan the pre-pass files
        ru_common.CUR["rdir"] = ru_common.BAK
    dest = args[0] if args else os.path.join(HERE, "divergences.md")
    seg, line, clause = scan_a()
    o1, n1 = report(seg, "(a1) whole segments: identical Pāli, differing Russian")
    o2, n2 = report(line, "(a2) whole lines: identical Pāli, differing Russian", minlen=12)
    o3, n3 = report(clause, "(a3) clauses (sentence parts of lines whose clause counts match)", minlen=12)
    o4, n4 = report(scan_items(), "(a4) comma/dash/ellipsis items of lines whose item counts match (cross-part only)",
                    minlen=6, cross_only=True)
    o5, n5 = report(scan_words(), "(a5) words of synonym strings (Pāli word ↔ Russian comma item, cross-part only)",
                    minlen=3, cross_only=True)
    o4 += o5
    ob = scan_b() if "--no-b" not in sys.argv else []
    src = "backup-pre-harmonise (before the pass)" if "--bak" in sys.argv else "current outputs"
    head = ["# pi-1 Russian zero-shot: divergences (find_divergences_ru.py)", "", f"Scanned: {src}.", "",
            f"(a1) segment groups: {n1}; (a2) line groups: {n2}; (a3) clause groups: {n3}; (a4) item groups: {n4}; (a5) string-word groups: {n5}", ""]
    open(dest, "w", encoding="utf-8", newline="\n").write("\n".join(head + o1 + o2 + o3 + o4 + ob) + "\n")
    print("segments", n1, "lines", n2, "clauses", n3, "items", n4, "words", n5, "->", dest)


if __name__ == "__main__":
    main()
