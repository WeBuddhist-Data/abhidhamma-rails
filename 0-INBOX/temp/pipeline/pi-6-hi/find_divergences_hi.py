"""Find Hindi divergences for identical Pāli across the pi-6 (Yamaka) Hindi zero-shot chapter files.

(a) whole segments / whole lines / clauses: group by normalised Pāli (block ID, variant brackets and
    (Ka)/(Kha)… labels stripped, spaces collapsed); list groups where the Hindi differs.
(b) recurring phrases: for each Pāli pattern in PHRASES, count per file which candidate Hindi forms occur on
    the aligned Hindi lines (and how many matching lines carry none of the candidates).
(c) notes files: "Pāli = Hindi" lines of notes-*.md grouped by the Pāli side; same Pāli, different Hindi.

usage: python -I -X utf8 find_divergences_hi.py [out.md] [--bak] [--no-b]
       (default out: divergences.md; --bak scans backup-pre-harmonise/, i.e. the state before the pass)
"""
import os, re, sys, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C
from hz6_common import PARTS, HERE, pairs, segments, norm, short

SPLIT_P = re.compile(r"(?<=[?.;:])\s+")
SPLIT_H = re.compile(r"(?<=[?।;:])\s+")


def hnorm(s):
    return norm(s).rstrip("।.?;: ")


def scan_a():
    seg = collections.defaultdict(lambda: collections.defaultdict(list))
    line = collections.defaultdict(lambda: collections.defaultdict(list))
    clause = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for sid, ps, hs in segments(part):
            kp = " / ".join(norm(x) for x in ps)
            kh = " / ".join(norm(x) for x in hs)
            seg[kp][kh].append(f"{short(part)}:{sid}")
            for p, h in zip(ps, hs):
                np_, nh = norm(p), norm(h)
                line[np_][nh].append(f"{short(part)}:{sid}")
                if p.startswith("#"):
                    continue
                cp = [c for c in SPLIT_P.split(np_) if c]
                ch = [c for c in SPLIT_H.split(nh) if c]
                if len(cp) == len(ch) and len(cp) > 1:
                    for a, b in zip(cp, ch):
                        clause[norm(a)][hnorm(b)].append(f"{short(part)}:{sid}")
    return seg, line, clause


def diff(a, b):
    import difflib
    ta, tb = a.split(), b.split()
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            out.append(f"«{' '.join(ta[i1:i2])}» → «{' '.join(tb[j1:j2])}»")
    return "; ".join(out)


def report(groups, title, minlen=0, cross_only=False, limit=None):
    out = [f"## {title}", ""]
    n = 0
    stats = collections.Counter()
    for k, v in sorted(groups.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        if len(v) < 2 or len(k) < minlen:
            continue
        keys = {hnorm(x) for x in v}
        if len(keys) < 2:
            continue
        fsets = [{l.split(':')[0] for l in locs} for locs in v.values()]
        if cross_only and len(set().union(*fsets)) < 2:
            continue
        n += 1
        if limit and n > limit:
            continue
        out.append(f"### {k[:300]}")
        ranked = sorted(v.items(), key=lambda kv: -len(kv[1]))
        top = ranked[0][0]
        for h, locs in ranked:
            files = sorted({l.split(':')[0] for l in locs})
            d = "" if h == top else f"  ⟨diff vs first: {diff(top, h)[:400]}⟩"
            out.append(f"- [{len(locs)}] {','.join(files)} ({', '.join(locs[:4])}) :: {h[:400]}{d}")
        out.append("")
    if limit and n > limit:
        out.append(f"(… {n - limit} more groups not listed)")
        out.append("")
    out.insert(1, f"groups with differing Hindi: {n}")
    return out, n


# (b) phrase table: pali regex -> candidate Hindi forms
PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), cands))


ph("sacakkhuka/acakkhuka …", r"\b(sa|a)(cakkhuk|sotak|ghānak|jivhak|kāyak|rūpak|cittak)",
   "आँख वाले", "आँख से रहित", "आँख-रहित", "आँख के साथ", "बिना आँख", "कान वाले", "कान से रहित", "कान-रहित", "कान के साथ",
   "बिना कान", "लेकिन", "पर बिना", "नाक वाले", "नाक से रहित", "नाक के साथ", "बिना नाक", "मन वाले", "मन से रहित",
   "मन के साथ", "बिना मन", "भौतिक रूप वाले", "भौतिक रूप से रहित", "भौतिक रूप के साथ", "बिना भौतिक रूप")
ph("dibbasotaṃ taṇhāsotaṃ", r"[Tt]aṇhāsot", "तृष्णा की धारा", "तृष्णा का प्रवाह", "(सोत)", "“कान”", "कान हैं", "कान है")
ph("catuvokāra pañcavokāra", r"[Cc]atuvokār\w* pañcavokār", "चार या पाँच समूहों वाले", "चार समूहों वाले और पाँच समूहों वाले",
   "चार समूहों वाले अस्तित्व या पाँच", "चार समूहों वाले अस्तित्व और पाँच")
ph("Natthi (short answer)", r"^Natthi\.", "ऐसा कोई नहीं है।", "ऐसा नहीं होता।", "नहीं है।")
ph("No (short answer)", r"^No\.", "नहीं।")
ph("Āmantā", r"^Āmantā", "हाँ।", "हाँ …।", "हाँ…।", "हाँ।…।")
ph("Uppajjati./Nuppajjati. short", r"^N?uppajj\w*\.\s*\^", "उत्पन्न")
ph("upapajjantānaṃ", r"upapajjantānaṃ", "जन्म लेने वालों में", "जन्म लेने वाले")
ph("cavantānaṃ", r"cavantānaṃ", "मरने वालों में", "से मरने वालों", "में मरने वालों")
ph("parinibbantānaṃ", r"parinibbantānaṃ", "पूर्ण निर्वाण पाने वालों में")
ph("pacchimabhavikānaṃ", r"[Pp]acchimabhavikānaṃ", "अंतिम जन्म वालों में", "अंतिम जन्म लेने वालों में", "अंतिम भव")
ph("Itaresaṃ", r"[Ii]tare(saṃ|sānaṃ)", "बाकी सबमें", "बाकी ", "शेष ")
ph("asaññasatta", r"[Aa]saññasatt", "पहचान-रहित प्राणियों", "पहचान-रहित")
ph("arūpa", r"\b[Aa]rūp(e|aṃ|ā|ānaṃ)\b", "अभौतिक लोक")
ph("apāya", r"[Aa]pāy|āpāyik", "दुर्गति")
ph("Suddhāvāsa", r"[Ss]uddhāvās", "शुद्ध निवास लोक", "शुद्धावास")
ph("pavatte", r"\bpavatte\b", "जीवन के दौरान", "प्रक्रिया में")
ph("nirodhasamāpannānaṃ", r"nirodhasamāpannānaṃ", "समाप्ति की ध्यान-अवस्था में लीन लोगों में")
ph("pañcavokāra", r"[Pp]añcavokār", "पाँच समूहों वाले अस्तित्व")
ph("catuvokāra", r"[Cc]atuvokār", "चार समूहों वाले अस्तित्व")
ph("ekavokāra", r"[Ee]kavokār", "एक समूह वाले अस्तित्व")
ph("kāmāvacara", r"[Kk]āmāvacar", "इंद्रिय-सुखों के लोक")
ph("rūpāvacara", r"[Rr]ūpāvacar", "सूक्ष्म भौतिक लोक")
ph("question yassa", r"^(\(\w+\) )?[Yy]assa (?!yattha)", "जिस व्यक्ति में", "जिसमें")
ph("question yattha", r"^(\(\w+\) )?[Yy]attha", "जिस स्थान पर", "जहाँ")
ph("question yassa yattha", r"[Yy]assa yattha", "जिस व्यक्ति में जिस स्थान पर")
ph("vā pana", r"vā pana", "(ख) और ", "और ")
ph("parijānāti question", r"parijān\w*ti\?", "पूरी तरह समझता", "पूरी तरह समझा", "पूरी तरह समझेगा")
ph("Pariññāvāro heading", r"^#.*Pariññāvār", "पूरी तरह समझने का खंड")
ph("Pavattivāro heading", r"^#.*Pavattivār", "प्रक्रिया का खंड")
ph("Uppādavāro", r"Uppādavār", "उत्पन्न होने का खंड")
ph("Paṇṇattivāro", r"Paṇṇattivār", "शब्दावली का खंड")
ph("Padasodhanavāro", r"Padasodhanavār", "शब्दों की जाँच का खंड")
ph("Padasodhanamūlacakka", r"Padasodhanamūlacakk", "शब्दों की जाँच पर आधारित चक्र का खंड")
ph("anulomaṃ heading", r"^#.*anulomaṃ", "सकारात्मक")
ph("paccanīkaṃ heading", r"^#.*paccanīk", "नकारात्मक")
ph("niṭṭhito/ā/aṃ", r"niṭṭhit", "पूरा हुआ", "पूरे हुए", "समाप्त")
ph("Cakkaṃ bandhitabbaṃ", r"[Cc]akkaṃ bandhitabb", "चक्र पूरा करना चाहिए", "चक्र को जोड़ लेना चाहिए")
ph("vitthāretabbaṃ", r"[Vv]itthāretabb", "विस्तार से कहना चाहिए", "विस्तार करना चाहिए", "विस्तार देना चाहिए")
ph("vibhajitabbaṃ", r"vibhajitabb", "विभाजन करना चाहिए", "विभाजित करना चाहिए", "बाँटकर बताने चाहिए")
ph("sadisaṃ", r"[Ss]adis", "एक जैसा", "समान", "पहले जैसा", "के समान")
ph("yassaka/yatthaka", r"yassak|yatthak", "व्यक्ति वाला", "स्थान वाला", "“जिस व्यक्ति में”", "“जिस स्थान पर”")
ph("natthi nānākaraṇaṃ", r"nānākaraṇ", "कोई अंतर नहीं है")
ph("Attharaso", r"Attharaso", "अर्थ का रस", "अर्थ का स्वाद")
ph("Dibbacakkhu", r"Dibbacakkhu", "दिव्य आँख और प्रज्ञा की आँख")
ph("Aggamaggasamaṅgī", r"Aggamaggasamaṅg", "सर्वोच्च मार्ग से युक्त")
ph("puthujjanā maggaṃ na", r"puthujjanā maggaṃ na", "साधारण व्यक्ति")
ph("dutiye citte vattamāne", r"dutiye\s+\w*\s*citte vattamāne", "के चलते समय")
ph("uppādakkhaṇe", r"uppādakkhaṇe", "उत्पन्न होने के क्षण में")
ph("bhaṅgakkhaṇe", r"bhaṅgakkhaṇe", "भंग होने के क्षण में")
ph("upapajjitvā parinibbāyissanti", r"upapajjitvā parinibbāyissanti", "जन्म लेकर पूर्ण निर्वाण पाएँगे")
ph("tesaṃ upapajjantānaṃ (after relative)", r"parinibbāyissanti tesaṃ (upapajjantānaṃ|cavantānaṃ)",
   "उनमें से जन्म लेने वालों में", "उनमें से मरने वालों में", "उन जन्म लेने वालों में", "उन मरने वालों में")
ph("na vattabbo", r"na vattabb|Na vattabb", "कहा जा सकता है")


def scan_b():
    tab = []
    for name, rx, cands in PHRASES:
        cnt = collections.defaultdict(collections.Counter)
        for part in PARTS:
            for p, h in pairs(part):
                if not rx.search(p):
                    continue
                cnt[part]["_lines"] += 1
                hit = False
                for c in cands:
                    k = h.count(c)
                    if k:
                        cnt[part][c] += k; hit = True
                if not hit:
                    cnt[part]["_none"] += 1
        tab.append((name, rx.pattern, cnt))
    out = ["## (b) recurring phrases: candidate Hindi forms per file", "",
           "Counts are occurrences of each candidate string on Hindi lines whose aligned Pāli matches; "
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


def pkey(s):
    s = s.strip().lstrip("#").strip()
    s = re.sub(r"\([^)]*\)", "", s)
    s = re.sub(r"[\"“”'.,:;?!–—]", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def scan_notes():
    """'Pāli = Hindi' pairs from notes-*.md, grouped by the Pāli side"""
    grp = collections.defaultdict(lambda: collections.defaultdict(list))
    for f in sorted(glob.glob(os.path.join(HERE, "notes-*.md"))):
        tag = os.path.basename(f)[6:-3]
        for ln in open(f, encoding="utf-8").read().splitlines():
            if " = " not in ln or ln.startswith("Format"):
                continue
            chunks = [c for c in re.split(r";\s+(?=[^=]*\s=\s)", ln.lstrip("- "))]
            for c in chunks:
                if c.count(" = ") != 1:
                    continue
                pa, hi = c.split(" = ")
                hi = re.sub(r"\s*[\[(](pi-\d|new|same|sample|as |from |chapter|the |terms|notes|\w+\.py)[^\])]*[\])]\s*", " ", hi).strip()
                hi = hi.strip(" .;")
                k = pkey(pa)
                if len(k) < 4:
                    continue
                grp[k][hi].append(tag)
    out = ["## (c) notes files: same Pāli, different Hindi", ""]
    n = 0
    for k, v in sorted(grp.items()):
        tags = {t for ts in v.values() for t in ts}
        if len(v) < 2 or len(tags) < 2:
            continue
        n += 1
        out.append(f"### {k}")
        for hi, ts in v.items():
            out.append(f"- {', '.join(sorted(set(ts)))} :: {hi[:300]}")
        out.append("")
    out.insert(1, f"groups: {n}")
    return out, n


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--bak" in sys.argv:
        C.CUR["hdir"] = C.BAK
    dest = args[0] if args else os.path.join(HERE, "divergences.md")
    seg, line, clause = scan_a()
    o1, n1 = report(seg, "(a1) whole segments: identical Pāli, differing Hindi", limit=400)
    o2, n2 = report(line, "(a2) whole lines: identical Pāli, differing Hindi", minlen=4)
    o3, n3 = report(clause, "(a3) clauses (sentence parts of lines whose clause counts match), cross-file only",
                    minlen=4, cross_only=True)
    import who_scan6, paren_scan6
    o4, n4 = who_scan6.scan()
    o4 = ["## (a4) being/place (WHO) phrases of the answers: same Pāli WHO, Hindi prefixes not compatible across files", "", "groups: %d" % n4, ""] + o4
    o5, n5 = paren_scan6.report(paren_scan6.scan())
    o5 = ["## (a5) parenthetical editorial notes: same Pāli, differing Hindi", "", "groups: %d" % n5, ""] + o5
    oc, nc = scan_notes()
    ob = scan_b() if "--no-b" not in sys.argv else []
    head = ["# pi-6 Hindi zero-shot (Yamaka): divergences (find_divergences_hi.py)", "",
            f"source: {'backup-pre-harmonise' if '--bak' in sys.argv else 'current output'}", "",
            f"(a1) segment groups: {n1}; (a2) line groups: {n2}; (a3) clause groups: {n3}; (a4) WHO groups: {n4}; (a5) note groups: {n5}; (c) notes groups: {nc}", ""]
    open(dest, "w", encoding="utf-8").write("\n".join(head + o2 + o3 + o1 + o4 + o5 + oc + ob) + "\n")
    print("segments", n1, "lines", n2, "clauses", n3, "who", n4, "paren", n5, "notes", nc, "->", dest)


if __name__ == "__main__":
    main()
