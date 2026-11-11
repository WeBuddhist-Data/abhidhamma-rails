"""Find Hindi divergences for identical Pāli across the pi-1 Hindi zero-shot parts.

(a) whole segments / whole lines / clauses: group by normalised Pāli (block ID and variant brackets stripped,
    spaces collapsed); list groups where the Hindi differs.
(b) recurring phrases: for each Pāli pattern in PHRASES, count per part which candidate Hindi forms occur on
    the aligned Hindi lines (and how many matching lines carry none of the candidates).

usage: python -I -X utf8 find_divergences_hi.py [out.md] [--bak] [--no-b]
       (default out: divergences.md; --bak scans backup-pre-harmonise/, i.e. the state before the pass)
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz_common import PARTS, HERE, pairs, segments, norm

SPLIT_P = re.compile(r"(?<=[?.;:])\s+")
SPLIT_H = re.compile(r"(?<=[?।;:])\s+")


def short(part):
    return part[:4] if part[0].isdigit() and part[1] == "-" else part[:3]


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
                        clause[a][hnorm(b)].append(f"{short(part)}:{sid}")
    return seg, line, clause


SPLIT_ITEM_P = re.compile(r"(?<=[?.;:,])\s+|\s+[–—]\s+")
SPLIT_ITEM_H = re.compile(r"(?<=[?।;:,])\s+|\s+[–—]\s+")


def scan_items():
    """comma / dash items of lines (and clauses) whose item counts match"""
    item = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for sid, ps, hs in segments(part):
            for p, h in zip(ps, hs):
                if p.startswith("#"):
                    continue
                cp = [c for c in SPLIT_ITEM_P.split(norm(p)) if c]
                ch = [c for c in SPLIT_ITEM_H.split(norm(h)) if c]
                if len(cp) == len(ch) and len(cp) > 1:
                    for a, b in zip(cp, ch):
                        item[a.rstrip(",.;:?")][hnorm(b).rstrip(",")].append(f"{short(part)}:{sid}")
    return item


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
        keys = {hnorm(x) for x in v}
        if len(keys) < 2:
            continue
        if cross_only:
            # only groups where different parts disagree (not a within-part variation)
            fsets = [{l.split(':')[0] for l in locs} for locs in v.values()]
            allf = set().union(*fsets)
            if len(allf) < 2:
                continue
        n += 1
        out.append(f"### {k[:300]}")
        ranked = sorted(v.items(), key=lambda kv: -len(kv[1]))
        top = ranked[0][0]
        for h, locs in ranked:
            files = sorted({l.split(':')[0] for l in locs})
            d = "" if h == top else f"  ⟨diff vs first: {diff(top, h)[:400]}⟩"
            out.append(f"- [{len(locs)}] {','.join(files)} ({', '.join(locs[:4])}) :: {h[:400]}{d}")
        out.append("")
    out.insert(1, f"groups with differing Hindi: {n}")
    return out, n


# (b) phrase table: pali regex -> candidate Hindi forms
PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), cands))


ph("sammappadhāna", r"sammappadhān", "सही परिश्रम", "सही प्रयास", "सम्यक प्रयास", "प्रयत्न")
ph("sammāvāyāma", r"sammāvāyām", "सही प्रयास", "सही परिश्रम")
ph("parishram-any", r".", "परिश्रम")
ph("viññatti", r"viññatt", "प्रकट अभिव्यक्ति", "द्वारा अभिव्यक्ति", "संकेत", "सूचना")
ph("kāyaviññatti", r"kāyaviññatt", "शरीर द्वारा प्रकट अभिव्यक्ति", "शारीरिक संकेत", "शरीर द्वारा अभिव्यक्ति")
ph("vacīviññatti", r"vacīviññatt", "वाणी द्वारा प्रकट अभिव्यक्ति", "वाचिक संकेत", "वाणी द्वारा अभिव्यक्ति")
ph("abhiññā (paṭipadā)", r"abhiññ", "शीघ्र उच्च ज्ञान", "तीव्र उच्च ज्ञान", "धीमे उच्च ज्ञान", "धीमे", "शीघ्र", "तीव्र")
ph("paṭipadā", r"paṭipad", "दुःखद प्रगति", "सुखद प्रगति", "प्रगति")
ph("adhipati", r"adhipate", "प्रधान है", "की प्रधानता वाला", "प्रधानता", "प्रधान")
ph("bhūmi", r"bhūmīsu|bhūmiy|bhūmik", "स्तर", "लोक")
ph("bahūsu", r"bahūsu", "(कई संस्करणों में)", "(अनेक संस्करण)", "अनेक संस्करण", "कई संस्करण")
ph("sārāga", r"sārāg", "गहरा राग", "प्रबल राग", "राग")
ph("appamāṇa heading", r"Appamāṇāni", "अपरिमित रूपों पर विजय के आधार", "असीम भाव")
ph("tadekaṭṭha", r"[Tt]adekaṭṭh", "एक साथ रहने वाले", "एक साथ स्थित", "साथ रहते", "एक ही स्थान", "साथ")
ph("ṭhapetvā", r"ṭhapetvā", "को छोड़कर", "छोड़कर", "के अलावा", "सिवाय")
ph("avasesā", r"avases", "शेष", "बाकी", "बचे हुए")
ph("sīlabbataparāmāsa", r"(?i)sīlabbataparāmās", "सदाचार और व्रतों के बारे में ग़लत धारणा", "कर्मकांडों और व्रतों", "चिपकाव")
ph("sīlabbatupādāna", r"(?i)sīlabbatupādān", "सदाचार और व्रतों के प्रति आसक्ति", "कर्मकांडों और व्रतों")
ph("sīlena suddhi", r"sīlena suddhi", "सदाचार से शुद्धि", "कर्मकांड से शुद्धि")
ph("sakkāyadiṭṭhi", r"(?i)sakkāyadiṭṭh", "स्थायी आत्मा की ग़लत दृष्टि", "आत्मा की दृष्टि")
ph("kāmacchanda", r"(?i)kāmacchand", "इंद्रिय-सुखों की चाह", "कामना")
ph("diṭṭhāsava / -saṃyojana / -upādāna", r"(?i)diṭṭhāsav|diṭṭhisaṃyojan|diṭṭhupādān", "ग़लत दृष्टि का", "ग़लत दृष्टि की", "दृष्टि का मैल", "दृष्टि का बंधन", "दृष्टियों के प्रति")
ph("thina (as a defilement)", r"(?i)thinamiddh|thinaṃ", "आलस्य", "सुस्ती")
ph("kāmupādāna list", r"kāmupādān", "के प्रति आसक्ति", "की आसक्ति")
ph("paṭipadā (any)", r"paṭipadaṃ", "उच्च ज्ञान वाला", "उच्च ज्ञान के साथ", "तीव्र", "शीघ्र")
ph("dukkhanirodhagāminī paṭipadā", r"gāmin", "ले जाने वाले मार्ग", "ले जाने वाला मार्ग", "रास्त")
ph("satthari kaṅkhati", r"Satthari kaṅkhati", "के बारे में शंका करता है, संशय करता है", "शंका और संशय")
ph("kaṅkhā string", r"kaṅkhāyanā", "दुविधा, संशय, दुचित्तापन", "दोचित्तापन", "मति-भ्रम", "किसी एक बात को पक्का न पकड़ पाना")
ph("diṭṭhi string paṭiggāho/patiṭṭhāho", r"diṭṭhigataṃ diṭṭhigahanaṃ", "पकड़, कसकर पकड़ना", "अड़ जाना")
ph("rūpassa santati", r"rūpassa santati", "भौतिक रूप की धारा", "निरंतरता")
ph("rūpassa upacayo", r"rūpassa upacayo", "भौतिक रूप की वृद्धि", "भौतिक रूप का संचय")
ph("Tehi dhammehi frames", r"Tehi dhammehi ye dhammā", "उन परिघटनाओं से जो परिघटनाएँ", "उन परिघटनाओं के संबंध में जो परिघटनाएँ", "परिघटनाएँ: ", "परिघटनाओं में से")
ph("sphere list (plural)", r"kāmāvacarā, rūpāvacarā", "से संबंधित, ", "से संबंधित हों, ")
ph("vattabba frame", r"(?i)na vattabb", "को कहा नहीं जा सकता", "नहीं कहना चाहिए")
ph("Teva / Tāneva frame", r"(Tāneva|Teyeva|Teva) ", "वे ही ")
ph("upacaya", r"upacay", "वृद्धि", "संचय", "बढ़ना")
ph("santati", r"santati", "निरंतरता", "सिलसिला", "प्रवाह")
ph("āruppa", r"āruppa|arūpāvacar", "अभौतिक", "निराकार", "अरूप")
ph("sasaṅkhāra", r"sasaṅkhār", "प्रेरणा के साथ", "प्रेरणा सहित")
ph("asaṅkhāra", r"asaṅkhār", "बिना प्रेरणा", "प्रेरणा रहित", "प्रेरणा के बिना")
ph("lobha", r"\blobh", "लोभ", "लालच")
ph("dosa", r"\bdos", "द्वेष", "घृणा")
ph("moha", r"\bmoh", "मोह", "भ्रम")
ph("diṭṭhi", r"diṭṭhi", "मिथ्या दृष्टि", "दृष्टि", "धारणा", "मत")
ph("vicikicchā", r"vicikicch", "संशय", "शंका", "संदेह")
ph("uddhacca", r"uddhacc", "बेचैनी", "चंचलता")
ph("thina", r"\bthin", "सुस्ती", "जड़ता", "आलस्य")
ph("middha", r"middh", "तंद्रा", "उनींदापन", "निद्रालुता", "आलस")
ph("kukkucca", r"kukkucc", "पछतावा", "पश्चाताप")
ph("māna", r"\bmān[oaā]", "अहंकार", "घमंड", "मान")
ph("kāmarāga", r"kāmarāg", "इंद्रिय-सुख का राग", "काम-राग", "कामराग")
ph("issā", r"\bissā", "ईर्ष्या", "जलन")
ph("macchariya", r"macchari", "कंजूसी", "मात्सर्य")
ph("āsava", r"āsav", "मन के मैल", "आस्रव")
ph("saṃyojana", r"saṃyojan", "बंधन")
ph("nīvaraṇa", r"nīvaraṇ", "बाधा", "बाधाएँ", "आवरण", "रुकावट")
ph("upādāna", r"upādān", "आसक्ति", "पकड़", "उपादान")
ph("kilesa", r"kiles", "मन के क्लेश", "क्लेश")
ph("gantha", r"\bgantha|ganth", "गाँठ", "ग्रंथि", "बंधन")
ph("ogha", r"\bogh", "बाढ़", "प्रवाह")
ph("yoga", r"\byog", "जुआ", "योग", "बंधन")
ph("parāmāsa", r"parāmās", "गलत पकड़", "दुराग्रह", "पकड़")
ph("kāmāvacara", r"kāmāvacar", "इंद्रिय-सुख के लोक", "इंद्रिय-जगत", "कामलोक", "इंद्रिय-क्षेत्र")
ph("rūpāvacara", r"rūpāvacar", "सूक्ष्म-भौतिक", "रूप-लोक", "रूपलोक")
ph("lokuttara", r"lokuttar", "लोकोत्तर", "लोक से परे", "लोकातीत", "सांसारिक से परे")
ph("apariyāpanna", r"apariyāpann", "अस्तित्व के लोकों में शामिल न", "किसी लोक में शामिल न", "में शामिल नहीं")
ph("abyākata", r"abyākat", "नैतिक रूप से अनिर्धारित", "अनिर्धारित")
ph("vipāka", r"vipāk", "परिणाम", "विपाक", "फल")
ph("kiriya", r"kiriy", "क्रियात्मक", "केवल क्रिया", "क्रिया")
ph("hetu", r"hetu", "मूल", "हेतु", "कारण")
ph("kasiṇa", r"kasiṇ", "को आधार बनाकर", "कसिण", "ध्यान-आधार", "ध्यान के आधार")
ph("samatikkamā", r"samatikkam", "पार कर जाने से", "पार करके", "पार कर", "लांघ")
ph("asāta", r"\basāt", "असुहावना", "अप्रिय")
ph("sāta", r"\bsāt", "सुहावना", "प्रिय")
ph("kabaḷīkāra", r"kabaḷīkār", "ठोस भोजन", "कौर", "ग्रास")
ph("upādārūpa", r"upādā", "व्युत्पन्न", "निर्भर", "आश्रित")
ph("mahābhūta", r"mahābhūt", "महाभूत", "मूल तत्व", "चार महान तत्व", "महान तत्व")
ph("nirutti", r"nirutt", "अभिव्यक्ति", "भाषा", "शब्द")
ph("sallakkhaṇā", r"sallakkhaṇ", "पहचानना", "लक्षित", "भेद")
ph("sañjānanā", r"sañjānan", "पहचानना", "पहचान")
ph("pajānanā", r"\bpajānan", "भली-भाँति जानना", "जानना", "समझना")
ph("Tattha", r"\bTattha\b", "उनमें", "इनमें", "वहाँ", "इनमें से", "उनमें से")
ph("tasmiṃ samaye", r"tasmiṃ samaye", "उस समय")
ph("katame (question)", r"^Katame dhammā", "कौन-सी परिघटनाएँ", "कौन-सी हैं", "कौन सी")


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
    out = ["## (b) recurring phrases: candidate Hindi forms per part", "",
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


def main():
    import hz_common
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--bak" in sys.argv:  # scan the pre-pass files
        hz_common.CUR["hdir"] = os.path.join(HERE, "backup-pre-harmonise")
    dest = args[0] if args else os.path.join(HERE, "divergences.md")
    seg, line, clause = scan_a()
    o1, n1 = report(seg, "(a1) whole segments: identical Pāli, differing Hindi")
    o2, n2 = report(line, "(a2) whole lines: identical Pāli, differing Hindi", minlen=12)
    o3, n3 = report(clause, "(a3) clauses (sentence parts of lines whose clause counts match)", minlen=12)
    o4, n4 = report(scan_items(), "(a4) comma/dash items of lines whose item counts match (cross-part only)",
                    minlen=6, cross_only=True)
    ob = scan_b() if "--no-b" not in sys.argv else []
    head = ["# pi-1 Hindi zero-shot: divergences (find_divergences_hi.py)", "",
            f"(a1) segment groups: {n1}; (a2) line groups: {n2}; (a3) clause groups: {n3}; (a4) item groups: {n4}", ""]
    open(dest, "w", encoding="utf-8").write("\n".join(head + o1 + o2 + o3 + o4 + ob) + "\n")
    print("segments", n1, "lines", n2, "clauses", n3, "items", n4, "->", dest)


if __name__ == "__main__":
    main()
