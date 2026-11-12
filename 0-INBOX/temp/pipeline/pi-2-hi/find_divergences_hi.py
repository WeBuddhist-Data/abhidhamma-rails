"""Find Hindi divergences for identical Pāli across the pi-2 Hindi zero-shot chapters.

(a) whole segments / whole lines / clauses / items: group by normalised Pāli (block ID and variant brackets
    stripped, spaces collapsed); list groups where the Hindi differs (cross-chapter groups only for (a3)/(a4)).
(b) recurring phrases: for each Pāli pattern in PHRASES, count per chapter which candidate Hindi forms occur on
    the aligned Hindi lines (and how many matching lines carry none of the candidates).
(c) notes files: "Pāli = Hindi" lines of notes-*.md grouped by the Pāli side; same Pāli, different Hindi.

usage: python -I -X utf8 find_divergences_hi.py [out.md] [--bak] [--no-b]
       (default out: divergences.md; --bak scans backup-pre-harmonise/, i.e. the state before the pass)
"""
import os, re, sys, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz_common import PARTS, HERE, pairs, segments, norm, short

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
                        clause[a][hnorm(b)].append(f"{short(part)}:{sid}")
    return seg, line, clause


SPLIT_ITEM_P = re.compile(r"(?<=[?.;:,])\s+|\s+[–—]\s+")
SPLIT_ITEM_H = re.compile(r"(?<=[?।;:,])\s+|\s+[–—]\s+")


def scan_items():
    """comma / dash items of lines whose item counts match"""
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
            fsets = [{l.split(':')[0] for l in locs} for locs in v.values()]
            if len(set().union(*fsets)) < 2:
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


ph("dukkhanirodhagāminī paṭipadā", r"[Nn]irodhagāmin", "ले जाने वाला मार्ग", "ले जाने वाले मार्ग", "ले जाने वाली प्रगति",
   "ले जाने वाली प्रतिपदा", "प्रगति", "मार्ग", "रास्त")
ph("upekkhā string", r"upekkhanā ajjhupekkhanā", "तटस्थ भाव से देखना, मन की तटस्थता", "उदासीन भाव से देखना, मन का संतुलन")
ph("akaniṭṭha", r"[Aa]kaniṭṭh", "सबसे ऊँचे अकनिष्ठ", "अकनिष्ठ")
ph("niddesa heading", r"^#.*[Nn]iddeso", "व्याख्या", "का विवरण", "विवरण")
ph("mātikā heading", r"^#.*[Mm]ātikā", "वर्गीकरण की मूल सूची", "वर्गीकरणों की मूल सूची", "प्रकारों की मूल सूची", "मूल सूची")
ph("Ekakaṃ…Dasakaṃ (closing/heading)", r"^#*\s*(Ekakaṃ|Dukaṃ|Tikaṃ|Catukkaṃ|Pañcakaṃ|Chakkaṃ|Sattakaṃ|Aṭṭhakaṃ|Navakaṃ|Dasakaṃ)\.?\s*\^",
   "के वर्गीकरण", "वर्गीकरण", "प्रकार", "की विधि")
ph("na vattabba frame", r"na vattabb", "को नहीं कहा जा सकता", "को कहा नहीं जा सकता", "नहीं कहना चाहिए", "न ", "कहा जा सकता है, न")
ph("kenaci viññeyyā", r"kenaci viññeyy", "किसी एक प्रकार की चेतना से जाने जा सकने वाले भी हैं", "जाने जा सकने वाली भी हैं",
   "जाने जा सकने वाले", "जाने जा सकने वाली", "जाने जा सकते")
ph("kati kusalā question", r"kati kusalā", "कितने हितकर हैं", "कितनी हितकर हैं", "कितने हितकर")
ph("siyā frame", r"\bsiyā\b", "कभी ", "होते हैं", "होती हैं", "होता है", "होती है")
ph("subject 'ye'/'sabhi' (pañhā)", r"^(Siyā|Na |Sappaccayā|Appamāṇā|Kusalā|Anārammaṇā|Sārammaṇā)", "ये ", "सभी क्षमताएँ", "वे ")
ph("byasana phrase", r"Ñātibyasanena", "संबंधियों की हानि से पीड़ित", "रिश्तेदारों की हानि से", "प्रभावित व्यक्ति")
ph("soko string", r"soko socanā", "शोक में डूबे रहना", "शोक से भरा होना")
ph("jāti string", r"jāti sañjāti okkanti", "प्रवेश", "गर्भ में उतरना")
ph("maraṇa string", r"cuti cavanatā", "च्युत होना", "गुज़र जाना")
ph("upāyāsa string", r"āyāso upāyāso", "परेशानी, निराशा", "हताशा, निराशा")
ph("sokaparideva compound", r"sokaparidevadukkhadomanassupāyās", "शोक, विलाप, दुःख, उदासी और निराशा")
ph("appiyehi sampayogo", r"appiyehi sampayogo", "अप्रिय से संयोग", "अप्रिय से मिलना", "अप्रियों से")
ph("piyehi vippayogo", r"piyehi vippayogo", "प्रिय से वियोग", "प्रिय से बिछड़ना", "प्रियों से")
ph("yampicchaṃ", r"[Yy]aṃ ?picchaṃ", "जो चाहता है, वह न मिलना", "जो चाहता है वह न मिलना", "न मिलना")
ph("satipaṭṭhāna", r"satipaṭṭhān", "सजगता के आधार", "सजगता का आधार", "सजगता की स्थापना")
ph("sammappadhāna", r"sammappadhān", "सही प्रयत्न", "सही प्रयास", "सही परिश्रम")
ph("iddhipāda", r"iddhipād", "सिद्धि के आधार", "सिद्धि का आधार")
ph("ātāpī", r"ātāpī", "उद्यमी", "तत्पर", "उत्साही")
ph("abhijjhādomanassa", r"abhijjhādomanass", "लालच और उदासी", "लोभ और उदासी")
ph("vineyya loke", r"vineyya loke", "लोक में", "संसार के प्रति", "संसार में")
ph("upeto hoti string", r"upeto hoti samupeto", "युक्त होता है, भली-भाँति युक्त", "सुसज्जित होता है", "से युक्त, भली-भाँति युक्त")
ph("iriyati string", r"[Ii]riyati vattati", "गतिशील रहता है", "चलता-फिरता है")
ph("Tena vuccati", r"Tena vuccati", "इसलिए", "इसीलिए")
ph("avasesā dhammā …sampayuttā", r"Avasesā dhammā", "शेष परिघटनाएँ", "बाकी परिघटनाएँ")
ph("seyyathidaṃ", r"seyyathidaṃ", "यानी", "जैसे", "अर्थात")
ph("musāvādā veramaṇī", r"[Mm]usāvādā veramaṇī", "झूठ बोलने से दूर रहना")
ph("pisuṇāya vācāya", r"pisuṇāya vācāya veramaṇī", "चुगली से दूर रहना", "चुगली करने से दूर रहना")
ph("pharusāya vācāya", r"pharusāya vācāya veramaṇī", "कठोर वाणी से दूर रहना", "कठोर वचन बोलने से दूर रहना")
ph("adinnādānā", r"adinnādānā veramaṇī", "न दी गई वस्तु लेने से", "जो न दिया गया हो, उसे लेने से", "बिना दी गई चीज़ लेने")
ph("kāmesumicchācārā", r"kāmesumicchācārā veramaṇī", "इंद्रिय-सुखों में दुराचार से", "काम-संबंधी ग़लत आचरण से")
ph("aṭṭhaṅgiko maggo", r"[Aa]ṭṭhaṅgiko maggo", "आठ अंगों वाला", "अष्टांगिक")
ph("metti string", r"metti mettāyanā", "मैत्री करना", "मैत्री रखना")
ph("pañcupādānakkhandhā", r"upādānakkhandh", "आसक्ति का विषय बनने वाले", "आसक्ति के विषय बनने वाले", "आसक्ति के पाँचों समूह",
   "आसक्ति के पाँच समूह")
ph("jarā string", r"jarā jīraṇatā", "बुढ़ापा, जीर्ण होना, दाँतों का टूटना")
ph("ājīva", r"ājīv", "आजीविका")
ph("sattanikāye", r"tamhi tamhi sattanikāye", "उस-उस प्राणी-वर्ग में", "उन-उन प्राणी-वर्गों में")
ph("ekakaṃ (in mātikā / niddesa)", r"^#.*Ekaka", "एकल वर्गीकरण", "एकल प्रकारों", "एकल प्रकार")
ph("kammapatha / X-ssa pahānaṃ", r"pahānaṃ", "छोड़ देना", "छोड़ना", "त्याग")
ph("nirodha (dukkhanirodha)", r"dukkhanirodh", "दुःख का अंत", "दुःख के अंत", "दुःख का निरोध", "निरोध")
ph("samudaya", r"dukkhasamuday", "दुःख की उत्पत्ति", "दुःख का उदय")
ph("bojjhaṅga name", r"sambojjhaṅg", "नामक जागृति का अंग", "जागृति के अंग", "जागृति का अंग")
ph("thinamiddha", r"[Tt]hinamiddh", "आलस्य और तंद्रा", "सुस्ती और तंद्रा")
ph("uddhaccakukkucca", r"[Uu]ddhaccakukkucc", "बेचैनी और पछतावा")
ph("kāmacchanda", r"[Kk]āmacchand", "इंद्रिय-सुखों की चाह", "कामना")
ph("vicikicchā", r"[Vv]icikicch", "संशय", "शंका", "संदेह")
ph("sakkāyadiṭṭhi", r"(?i)sakkāyadiṭṭh", "स्थायी आत्मा की ग़लत दृष्टि", "आत्मा की दृष्टि", "आत्म-दृष्टि")
ph("sīlabbataparāmāsa", r"(?i)sīlabbataparāmās", "सदाचार और व्रतों के बारे में ग़लत धारणा", "कर्मकांड")


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
    out = ["## (b) recurring phrases: candidate Hindi forms per chapter", "",
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
                hi = re.sub(r"\s*[\[(](pi-\d|new|same|sample|as |from |chapter|the |pi-1|\w+\.py)[^\])]*[\])]\s*", " ", hi).strip()
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
    import hz_common
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--bak" in sys.argv:
        hz_common.CUR["hdir"] = os.path.join(HERE, "backup-pre-harmonise")
    dest = args[0] if args else os.path.join(HERE, "divergences.md")
    seg, line, clause = scan_a()
    o1, n1 = report(seg, "(a1) whole segments: identical Pāli, differing Hindi")
    o2, n2 = report(line, "(a2) whole lines: identical Pāli, differing Hindi", minlen=12)
    o3, n3 = report(clause, "(a3) clauses (sentence parts of lines whose clause counts match), cross-chapter only",
                    minlen=12, cross_only=True)
    o4, n4 = report(scan_items(), "(a4) comma/dash items of lines whose item counts match (cross-chapter only)",
                    minlen=6, cross_only=True)
    oc, nc = scan_notes()
    ob = scan_b() if "--no-b" not in sys.argv else []
    head = ["# pi-2 Hindi zero-shot: divergences (find_divergences_hi.py)", "",
            f"(a1) segment groups: {n1}; (a2) line groups: {n2}; (a3) clause groups: {n3}; (a4) item groups: {n4}; "
            f"(c) notes groups: {nc}", ""]
    open(dest, "w", encoding="utf-8").write("\n".join(head + o1 + o2 + o3 + o4 + oc + ob) + "\n")
    print("segments", n1, "lines", n2, "clauses", n3, "items", n4, "notes", nc, "->", dest)


if __name__ == "__main__":
    main()
