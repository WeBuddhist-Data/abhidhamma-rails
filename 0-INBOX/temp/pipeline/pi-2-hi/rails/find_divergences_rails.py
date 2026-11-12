"""Cross-chapter alignment check for the pi-2 Hindi RAILS translation: identical Pāli, differing Hindi.

Reuses ../find_divergences_hi.py (scan_a, scan_items, report) with the Hindi folder pointed at the rails chapters
(normalisation: block ID and variant brackets stripped, spaces collapsed).
(a1) whole segments, (a2) whole lines, (a3) clauses, (a4) comma/dash items (cross-chapter only for a3/a4)
(b)  recurring formula phrases: candidate Hindi forms per chapter on lines whose aligned Pāli matches
(c)  "Pāli = Hindi" lines of rails/notes-*.md (and hi-rails-formulas.md): same Pāli, different Hindi

usage: python -I -X utf8 find_divergences_rails.py [out.md] [--bak]
       (default out: divergences.md next to this script; --bak scans backup-pre-align/)
"""
import collections, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import hz_common
import find_divergences_hi as F
from hz_common import PARTS, pairs, short

RAILS = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters"

PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), cands))


# Pañhāpucchaka frames
ph("siyā na vattabba (frame)", r"siyā na vattabb", "कभी ऐसा होता है कि", "कभी उसे नहीं कहा", "कभी उन्हें नहीं कहा",
   "कभी इसे नहीं कहा", "कभी इन्हें", "कभी उसे न ", "कभी उन्हें न ")
ph("na vattabbā – (dash frame)", r"(?<!siyā )na vattabb\w* –", "को नहीं कहा जा सकता –", "इन्हें नहीं कहा जा सकता –",
   "उन्हें नहीं कहा जा सकता –", "उसे नहीं कहा जा सकता –", "इसे नहीं कहा जा सकता –")
ph("na vattabbā (no dash frame)", r"(?<!siyā )na vattabb\w* (?!–)", "न ", "कहा जा सकता है, न", "नहीं कहा जा सकता")
ph("siyā X, siyā Y", r"\bsiyā\b", "होता है", "होते हैं", "होती है", "होती हैं", "कभी ")
ph("subject added (pañhā)", r"^(Siyā|Na |Sappaccayā|Appamāṇā|Kusalāyeva|Anārammaṇā|Sārammaṇā|Abyākatā|Kusalā)",
   "सभी तत्व", "पाँचों", "चारों", "पाँचों समूह", "इंद्रिय-क्षेत्र", "ये ", "वे ", "इन्हें")
# truths
ph("nirodhasacca", r"[Nn]irodhasacc", "दुःख के अंत का सत्य", "अंत का सत्य")
ph("samudayasacca", r"[Ss]amudayasacc", "दुःख की उत्पत्ति का सत्य", "उत्पत्ति का सत्य")
ph("maggasacca", r"[Mm]aggasacc", "मार्ग का सत्य")
ph("dukkhanirodhagāminī paṭipadā", r"[Nn]irodhagāmin", "ले जाने वाला प्रगति का ढंग", "ले जाने वाले प्रगति के ढंग",
   "ले जाने वाली प्रगति", "ले जाने वाला मार्ग", "प्रगति")
ph("paṭipadā (modes)", r"paṭipad", "दुःखद प्रगति", "सुखद प्रगति", "कठिन प्रगति", "आसान प्रगति", "प्रगति का ढंग", "प्रगति")
# definitions
ph("jāti string", r"jāti sañjāti okkanti", "गर्भ में उतरना", "प्रवेश")
ph("jarā string", r"jarā jīraṇatā khaṇḍiccaṃ", "दाँतों का टूटना", "बालों का पकना")
ph("maraṇa string", r"cuti cavanatā", "गुज़र जाना, गुज़र जाने की अवस्था", "च्युत")
ph("soka string", r"soko socanā", "शोकग्रस्त होना", "शोक से भरा होना")
ph("parideva string", r"ādevo paridevo", "रोने की अवस्था", "रोने से भरा होना")
ph("upāyāsa string", r"āyāso upāyāso", "हताश होने की अवस्था", "हताशा से भरा होना")
ph("byasana phrase", r"Ñātibyasanena", "पीड़ित, धन-संपत्ति", "पीड़ित, या धन-संपत्ति")
# efforts / development
ph("āsevati bhāveti bahulīkaroti", r"āsevati bhāveti bahulīkaroti",
   "निरंतर सेवन करता है, अभ्यास करता है, बार-बार करता है", "निरंतर सेवन करता है, उसका अभ्यास करता है, उसे बार-बार करता है")
ph("right-effort formula", r"anuppannānaṃ pāpakānaṃ", "उत्पन्न न हुई बुरी हानिकर", "उत्पन्न न हुई बुरी, हानिकर")
ph("upeto hoti string", r"upeto hoti", "सुसज्जित होता है, भली-भाँति", "सुसज्जित, भली-भाँति")
# veramaṇī
ph("veramaṇī", r"veramaṇ", "से दूर रहना", "से दूर रहने का", "से बचना", "से बचने का", "बचना", "दूर रहना")
ph("Dhammasaṅgaṇī reference", r"(?i)dhammasaṅgaṇ|dha\. ?sa\.", "परिघटनाओं की गणना", "धम्मसंगणी")
# headings
ph("mātikā heading", r"^#.*[Mm]ātikā", "वर्गीकरण की मूल सूची", "वर्गीकरणों की मूल सूची", "मूल सूची")
ph("niddesa heading", r"^#.*[Nn]iddeso", "की व्याख्या", "व्याख्या")
ph("Catukkaṃ / Pañcakaṃ (jhāna method)", r"^#*\s*(Catukkaṃ|Pañcakaṃ|Catukkanayo|Pañcakanayo)", "चार-चार की विधि",
   "पाँच-पाँच की विधि", "विधि")
ph("Tena vuccati", r"Tena vuccati|tena vuccati", "इसीलिए कहा जाता है", "इसीलिए “", "इसीलिए वह", "इसलिए")
ph("samannāgata", r"samannāgat", "युक्त", "घिरे", "घिरा")
ph("dukkhapaṭipadaṃ dandhābhiññaṃ", r"dukkhapaṭipadaṃ dandhābhiññaṃ", "दुःखद प्रगति और धीमे उच्च ज्ञान वाला")


def scan_b():
    out = ["## (b) recurring phrases: candidate Hindi forms per chapter", "",
           "Counts are occurrences of each candidate string on Hindi lines whose aligned Pāli matches; "
           "_lines = matching lines, _none = matching lines with no candidate (overlapping candidates counted separately).", ""]
    for name, rx, cands in PHRASES:
        out.append(f"### {name}  (`{rx.pattern}`)")
        for part in PARTS:
            c = collections.Counter()
            for p, h in pairs(part):
                if not rx.search(p):
                    continue
                c["_lines"] += 1
                hit = False
                for cand in cands:
                    k = h.count(cand)
                    if k:
                        c[cand] += k; hit = True
                if not hit:
                    c["_none"] += 1
            if c:
                items = ", ".join(f"{k}={v}" for k, v in c.items() if not k.startswith("_"))
                out.append(f"- {short(part)}: lines={c['_lines']} none={c['_none']} | {items}")
        out.append("")
    return out


def scan_notes():
    grp = collections.defaultdict(lambda: collections.defaultdict(list))
    files = sorted(glob.glob(os.path.join(HERE, "notes-*.md"))) + [os.path.join(HERE, "hi-rails-formulas.md")]
    for f in files:
        tag = os.path.basename(f)[:-3].replace("notes-", "")
        for ln in open(f, encoding="utf-8").read().splitlines():
            if " = " not in ln or ln.startswith("Format"):
                continue
            for c in re.split(r";\s+(?=[^=]*\s=\s)", ln.lstrip("- ")):
                if c.count(" = ") != 1:
                    continue
                pa, hi = c.split(" = ")
                hi = re.sub(r"\s*[\[(](pi-\d|new|same|sample|as |from |chapter|ch\d|the |not yet|pi-1|\w+\.py)[^\])]*[\])]\s*",
                            " ", hi).strip().strip(" .;")
                k = F.pkey(pa)
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
    hz_common.CUR["hdir"] = os.path.join(HERE, "backup-pre-align") if "--bak" in sys.argv else RAILS
    dest = args[0] if args else os.path.join(HERE, "divergences.md")
    seg, line, clause = F.scan_a()
    o1, n1 = F.report(seg, "(a1) whole segments: identical Pāli, differing Hindi")
    o2, n2 = F.report(line, "(a2) whole lines: identical Pāli, differing Hindi", minlen=12)
    o3, n3 = F.report(clause, "(a3) clauses (sentence parts of lines whose clause counts match), cross-chapter only",
                      minlen=12, cross_only=True)
    o4, n4 = F.report(F.scan_items(), "(a4) comma/dash items of lines whose item counts match (cross-chapter only)",
                      minlen=6, cross_only=True)
    oc, nc = scan_notes()
    ob = scan_b()
    head = ["# pi-2 Hindi rails: divergences (find_divergences_rails.py)", "",
            f"(a1) segment groups: {n1}; (a2) line groups: {n2}; (a3) clause groups: {n3}; (a4) item groups: {n4}; "
            f"(c) notes groups: {nc}", ""]
    open(dest, "w", encoding="utf-8", newline="\n").write("\n".join(head + o1 + o2 + o3 + o4 + oc + ob) + "\n")
    print("segments", n1, "lines", n2, "clauses", n3, "items", n4, "notes", nc, "->", dest)


if __name__ == "__main__":
    main()
