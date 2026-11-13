"""Find Hindi divergences for identical / recurring Pāli across the pi-7 (Paṭṭhāna) Hindi RAILS chapter files.

(a) whole lines: group by normalised Pāli (^id, {…} variants, count markers "(3)" stripped, spaces collapsed);
    list groups where the Hindi (normalised the same way, «[…]» brackets stripped) differs.
    Groups whose Pāli differs only inside {…} are marked (they are merged by the normalisation).
(n) editorial notes in round brackets: each Pāli «( … )» note (not a count marker) paired by position with the Hindi
    «( … )» of the aligned line (only when the counts agree); same Pāli note, different Hindi.
(b) recurring words and frames: for each Pāli pattern in PHRASES, per file, the count of each candidate Hindi
    form on the aligned Hindi lines (and how many matching lines carry none of the candidates).
(c) triad / dyad / cluster names in headings and closing lines: Pāli stem -> Hindi forms.
(d) every heading text: same Pāli heading, different Hindi.

usage: python -I -B -X utf8 find_divergences_rails.py [out.md] [--bak]
       (default out: divergences.md; --bak scans backup-pre-align/, i.e. the state before the pass)
"""
import os, re, sys, collections, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ar7_common as C
from ar7_common import PARTS, HERE, pairs, pnorm, hnorm, short

VARP = re.compile(r"\{[^}]*\}")


def hkey(s):
    return hnorm(s).rstrip("।.?;: ")


def scan_a():
    grp = collections.defaultdict(lambda: collections.defaultdict(list))
    raw = collections.defaultdict(set)
    for part in PARTS:
        for i, (p, h) in enumerate(pairs(part)):
            k = pnorm(p)
            if len(k) < 3:
                continue
            grp[k][hkey(h)].append(f"{short(part)}:{i + 1}")
            raw[k].add(VARP.sub("{}", re.sub(r"\s*\^[\w-]+\s*$", "", p)) if "{" in p else "")
    return grp, raw


def diff(a, b):
    ta, tb = a.split(), b.split()
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            out.append(f"«{' '.join(ta[i1:i2])}» → «{' '.join(tb[j1:j2])}»")
    return "; ".join(out)


def report_a(grp, raw):
    out, n = [], 0
    for k, v in sorted(grp.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        if len(v) < 2:
            continue
        n += 1
        brace = " ⟨Pāli differs only inside {…}⟩" if len(raw[k] - {""}) > 1 else ""
        out.append(f"### {k[:300]}{brace}")
        ranked = sorted(v.items(), key=lambda kv: -len(kv[1]))
        top = ranked[0][0]
        for h, locs in ranked:
            files = sorted({l.split(':')[0] for l in locs})
            d = "" if h == top else f"  ⟨diff vs first: {diff(top, h)[:400]}⟩"
            out.append(f"- [{len(locs)}] {','.join(files)} ({', '.join(locs[:4])}) :: {h[:400]}{d}")
        out.append("")
    return ["## (a) whole lines: identical Pāli, differing Hindi", "", f"groups: {n}", ""] + out, n


# ------------------------------------------------------------------ (n) bracketed editorial notes
PPAR = re.compile(r"\(([^()]*)\)")


def notes_of(s, pali):
    s = re.sub(r"\s*\^[\w-]+\s*$", "", s)
    s = VARP.sub("", s) if pali else re.sub(r"\[[^\]]*\]", "", s)
    out = []
    for m in PPAR.finditer(s):
        t = m.group(1).strip()
        if re.fullmatch(r"[\d.\s,=-]*", t) or re.fullmatch(r"[०-९\d.\s,=-]*", t):
            continue
        out.append(re.sub(r"\s+", " ", t))
    return out


def scan_n():
    g = collections.defaultdict(lambda: collections.defaultdict(list))
    mism = 0
    for part in PARTS:
        for i, (p, h) in enumerate(pairs(part)):
            pn, hn = notes_of(p, True), notes_of(h, False)
            if not pn:
                continue
            if len(pn) != len(hn):
                mism += 1
                continue
            for a, b in zip(pn, hn):
                g[a.rstrip(". ")][b.rstrip("।. ")].append(f"{short(part)}:{i + 1}")
    out, n = [], 0
    for k, v in sorted(g.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        if len(v) < 2:
            continue
        n += 1
        out.append(f"### ({k[:200]})")
        for h, locs in sorted(v.items(), key=lambda kv: -len(kv[1])):
            out.append(f"- [{len(locs)}] {' '.join(sorted({l.split(':')[0] for l in locs}))} ({locs[0]}) :: ({h[:300]})")
        out.append("")
    return ["## (n) editorial notes in round brackets: same Pāli note, differing Hindi", "",
            f"groups: {n} (lines with unequal bracket counts skipped: {mism})", ""] + out, n


# ------------------------------------------------------------------ (b) recurring words and frames
PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), [re.compile(c) for c in cands]))


ph("kātabba- (all forms)", r"kātabb", r"तैयार कर(?:ना|ने|नी) चाहिए", r"शामिल कर(?:ना|ने|नी) चाहिए",
   r"बना(?:ना|ने|नी) चाहिए", r"(?<!तैयार )(?<!शामिल )कर(?:ना|ने|नी) चाहिए", r"से शुरू करना चाहिए", r"बनाएँ")
ph("Mūlaṃ kātabbaṃ", r"[Mm]ūlaṃ kātabb", r"मूल वाक्य से शुरू करना चाहिए", r"मूल वाक्य बनाना चाहिए",
   r"मूल वाक्य करना चाहिए", r"मूल वाक्य तैयार करना चाहिए")
ph("Mūlaṃ pucchitabbaṃ", r"[Mm]ūlaṃ pucchitabb", r"मूल वाक्य से पूछना चाहिए", r"मूल वाक्य पूछना चाहिए")
ph("pucchitabba-", r"pucchitabb", r"पूछना चाहिए", r"पूछने चाहिए", r"प्रश्न करना चाहिए")
ph("(A/Savipākaṃ – n)", r"\([AaSs]a?vipākaṃ", r"कर्म-फल-कारण रहित", r"कर्म-फल-कारण के बिना", r"कर्म-फल-कारण सहित")
ph("gaṇetabbaṃ", r"gaṇet|gaṇat", r"इस तरह गिनना चाहिए", r"इसी तरह गिनना चाहिए", r"इस प्रकार गिनना चाहिए",
   r"वैसे ही गिनना चाहिए", r"गिनना चाहिए", r"गिनने चाहिए", r"गणना करनी चाहिए")
ph("gaṇitaṃ", r"[gn]aṇitaṃ", r"को .{0,200}? में भी गिना गया है", r"का .{0,200}?भी गिना गया है", r"गिना गया है",
   r"की गणना की गई है")
ph("sadisaṃ / sadisā / sadiso", r"sadis", r"के समान हैं", r"के समान है", r"के समान(?! है)", r"जैसा")
ph("paṭiccavārasadisaṃ (no verb)", r"paṭiccavārasadis(aṃ|ā)\.?\)?\s*$", r"के समान हैं", r"के समान है", r"के समान(?! है)")
ph("saṃkhittaṃ", r"[Ss]aṃkhitt|[Ss]aṅkhit", r"संक्षिप्त", r"संक्षेप")
ph("vitthāretabba-", r"vitthāret|vitthārat|vitthāreb", r"विस्तार करना चाहिए", r"विस्तार करने चाहिए",
   r"विस्तार से कहना")
ph("vitthāro", r"vitthāro", r"विस्तार से(?! क)", r"विस्तार(?! से| कर)")
ph("cakkaṃ", r"[Cc]akkaṃ", r"बारी-बारी से", r"चक्र")
ph("pañhā kātabbā", r"pañhā kātabb", r"प्रश्न करने चाहिए", r"प्रश्न तैयार करने चाहिए", r"प्रश्न बनाने चाहिए")
ph("pisuṇaṃ bhaṇati", r"pisuṇ", r"चुगली की बातें", r"चुगली की बात(?!ें)", r"चुगली करता")
ph("ekāgārikaṃ", r"ekāgārik", r"एक ही घर में डाका डालता", r"एक ही घर")
ph("lohitaṃ uppādeti", r"lohitaṃ uppād", r"खून बहाता", r"खून बहाने")
ph("sakapariggahe / parapariggahe", r"pariggah", r"अपने परिग्रह", r"पराए परिग्रह", r"अपनी संपत्ति", r"पराई संपत्ति",
   r"अपने अधिकार की चीज़", r"दूसरों के अधिकार की चीज़", r"परिग्रह")
ph("sakabhaṇḍe / parabhaṇḍe", r"bhaṇḍe", r"अपनी वस्तुओं", r"पराई वस्तुओं", r"अपनी वस्तु(?!ओं)", r"पराई वस्तु(?!ओं)",
   r"दूसरों की वस्तु")
ph("chandarāga", r"chandarāg", r"चाह-राग", r"चाह और राग", r"इच्छा-राग")
ph("dhamma(p)paṭisambhidā", r"dhamma(p)?paṭisambhid", r"परिघटनाओं का विश्लेषणात्मक ज्ञान",
   r"परिघटनाओं के विश्लेषणात्मक ज्ञान", r"शिक्षा का विश्लेषणात्मक ज्ञान", r"शिक्षा के विश्लेषणात्मक ज्ञान",
   r"धम्म")
ph("nirutti(p)paṭisambhidā", r"nirutti(p)?paṭisambhid", r"भाषा का विश्लेषणात्मक ज्ञान", r"भाषा के विश्लेषणात्मक ज्ञान",
   r"भाषा")
ph("attha(p)paṭisambhidā", r"attha(p)?paṭisambhid", r"अर्थ का विश्लेषणात्मक ज्ञान", r"अर्थ के विश्लेषणात्मक ज्ञान")
ph("paṭibhāna(p)paṭisambhidā", r"paṭibhāna(p)?paṭisambhid", r"सूझ-बूझ का विश्लेषणात्मक ज्ञान",
   r"सूझ-बूझ के विश्लेषणात्मक ज्ञान", r"प्रत्युत्पन्न")
ph("sukhindriya", r"sukhindriy", r"सुख की क्षमता", r"सुख-क्षमता", r"सुख रूपी क्षमता", r"शारीरिक सुख")
ph("dukkhindriya", r"dukkhindriy", r"दुःख की क्षमता", r"दुःख-क्षमता", r"दुःख रूपी क्षमता", r"शारीरिक दुःख")
ph("sahajātā (adjective before khandhā etc.)", r"sahajātā (ajjhattik|bāhir|khandh|kusal|akusal|abyākat)",
   r"साथ उत्पन्न", r"सह-उत्पन्न", r"सह-उत्पत्ति")
ph("anidassanasappaṭigha", r"anidassanasappaṭigh", r"दिखाई न देने वा(?:ला|ले|ली), पर टकराव",
   r"दिखाई न देने वा(?:ला|ले|ली) पर टकराव", r"दिखाई न देने वा(?:ला|ले|ली) और टकराव वा")
ph("avitakkavicāramatta", r"avitakkavicāramatt|avitakka vicāramatt",
   r"आरंभिक विचार से रहित, केवल सतत", r"आरंभिक विचार से रहित केवल सतत")
ph("adukkhamasukha", r"adukkhamasukh", r"न दुःखद, न सुखद", r"न दुःखद न सुखद")
ph("nevavipākanavipākadhamma", r"nevavipākanavipākadhamm", r"न कर्म-फल रूपी, न कर्म-फल", r"न कर्म-फल रूपी न कर्म-फल")
ph("anupādinnaanupādāniya", r"anupādinnaanupādāniy", r"न कर्म से उत्पन्न, न आसक्ति", r"न कर्म से उत्पन्न न आसक्ति")
ph("nevadassanena nabhāvanāya", r"nevadassanena ?nabhāvanāy", r"न सत्य-दर्शन से, न मानसिक", r"न सत्य-दर्शन से न मानसिक")
ph("nevasekkhanāsekkha", r"nevasekkhanāsekkh", r"न सीखने के चरण का, न", r"न सीखने के चरण का न", r"न सीखने के चरण की, न",
   r"न सीखने के चरण की न")
ph("nevācayagāmināpacayagāmi", r"nevācayagām|nevaācayagām", r"न संचय की ओर, न", r"न संचय की ओर न")
ph("asaṃkiliṭṭhasaṃkilesika", r"asaṃkiliṭṭhasaṃkilesik", r"क्लेशों से मलिन न होने वा(?:ला|ले|ली), पर",
   r"क्लेशों से मलिन न होने वा(?:ला|ले|ली) पर")
ph("double negation nana/nano", r"\b[Nn]ana|\b[Nn]ano", r"न होने वाली न होने वाली", r"न होने वाली \(न होने वाली\)",
   r"न होने वाली” न होने वाली", r"“")
ph("X ceva na/no ca Y", r"(ceva|ñceva) n[ao] ca", r", पर स्वयं", r"न होने वाली")
ph("X ceva nana/nano ca Y", r"(ceva|ñceva) nan[ao] ca", r", पर स्वयं .{0,80}?न होने वाली न होने वाली",
   r"भी और .{0,80}?न होने वाली न होने वाली भी")
ph("X ceva Y ca", r"(ceva|ñceva) (?!n[ao] ca)\w+ ca\b|ñceva \w+ñca", r"भी और .*? भी", r" भी")
ph("niṭṭhitaṃ / niṭṭhito (closing)", r"niṭṭhit", r"समाप्त", r"पूरा हुआ", r"“")
ph("ghaṭanā", r"ghaṭan", r"संयोजन", r"मेल")
ph("sabhāga", r"sabhāg", r"साथी कारण", r"सहभागी कारण")
ph("mūlake / mūle (series)", r"mūl(ak)?e\b", r"से शुरू होने वाली शृंखला", r"पद से शुरू", r"मूल वाक्य")
ph("gamana", r"gaman", r"प्रसंग", r"दौर", r"क्रम")
ph("ninnānākaraṇaṃ", r"ninnān", r"बिना किसी अंतर के", r"कोई अंतर नहीं", r"बिना अंतर के")
ph("āmasana", r"āmasan", r"उल्लेख", r"छूना", r"स्पर्श")
ph("iminā kāraṇena", r"iminā kāraṇena", r"इस तरीके से", r"इस कारण से", r"इस प्रकार")
ph("paripuṇṇaṃ", r"[Pp]aripuṇṇ", r"परिपूर्ण", r"पूर्ण")
ph("na labbhati / labbhanti", r"na labbh", r"लागू नहीं", r"नहीं मिलत", r"प्राप्त नहीं")
ph("sabbattha vitthāro", r"[Ss]abbattha vitthāro", r"हर जगह विस्तार से", r"हर जगह विस्तार(?! से)")
ph("Paccanīyuddhāro", r"Paccanīyuddhār", r"नकारात्मक क्रम के लिए [^\s।*]+(?: [^\s।*^]+)*")
ph("vippayuttakā (cetanā)", r"vippayuttakā", r"अलग इरादा", r"अलग हुआ इरादा", r"से अलग इरादा")
ph("Siyā question", r"^Siyā", r"\?")


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
                    ms = c.findall(h)
                    if ms:
                        hit = True
                        if name == "Paccanīyuddhāro":
                            for m in ms:
                                cnt[part][m] += 1
                        else:
                            cnt[part][c.pattern] += len(ms)
                if not hit:
                    cnt[part]["_none"] += 1
        tab.append((name, rx.pattern, cnt))
    out = ["## (b) recurring words and frames: candidate Hindi forms per file", "",
           "Counts are occurrences of each candidate (regex) on Hindi lines whose aligned Pāli matches; "
           "_lines = matching lines, _none = matching lines with none of the candidates.", ""]
    for name, pat, cnt in tab:
        out.append(f"### {name}  (`{pat}`)")
        tot = collections.Counter()
        for part in PARTS:
            if part in cnt:
                c = cnt[part]
                items = ", ".join(f"{k}={v}" for k, v in c.items() if not k.startswith("_"))
                out.append(f"- {short(part)}: lines={c['_lines']} none={c['_none']} | {items}")
                for k, v in c.items():
                    tot[k] += v
        out.append(f"- TOTAL: " + ", ".join(f"{k}={v}" for k, v in tot.most_common()))
        out.append("")
    return out


# ------------------------------------------------------------------ (c) names
PNUM = re.compile(r"^[\d\s\-–]+\.\s*")
END = re.compile(r"\s*(niṭṭhit(aṃ|o|ā)\.?)\s*$")
SPLIT = re.compile(r"(?:ajjhattikaduka|.+?(?:ttikadvaya|ttika|duka|gocchaka))")


def ppart(s):
    s = pnorm(s).lstrip("#").strip().strip("*").strip()
    s = PNUM.sub("", s)
    closing = bool(END.search(s))
    s = END.sub("", s).strip().rstrip(".")
    return s, closing


def split_p(s):
    if " " in s or "paṭṭhān" in s or re.search(r"ādi(?=duk|ttik|chag|gocch|pad)|ādi$|ādīni", s) \
            or not re.search(r"(ttik|duk|gocchak|dvay)(aṃ|a|āni)$", s):
        return None
    s = s.replace("-", "")
    s = s[0].lower() + s[1:]
    s = re.sub(r"(aṃ|āni)$", "a", s)
    s = re.sub(r"(duk|gocchak)āni", r"\1a", s)
    parts = SPLIT.findall(s)
    if "".join(parts) != s:
        return None
    return parts


def split_h(s):
    s = hnorm(s).lstrip("#").strip().strip("*").strip()
    s = PNUM.sub("", s)
    s = re.sub(r"\s*(समाप्त|पूरा हुआ|पूरे हुए)।?\s*$", "", s).strip().rstrip("।")
    return re.split(r"(?<=वर्गीकरण) और |(?<=वर्गीकरणों) और |(?<=वर्ग) और |(?<=वर्गों) और ", s)


def scan_c():
    inv = collections.defaultdict(lambda: collections.defaultdict(list))
    bad = []
    for part in PARTS:
        for i, (p, h) in enumerate(pairs(part)):
            ps, closing = ppart(p)
            if not (p.startswith("#") or closing):
                continue
            pp = split_p(ps)
            if not pp:
                continue
            hh = split_h(h)
            if len(pp) != len(hh):
                bad.append(f"{short(part)}:{i+1} {pp} | {hh}")
                continue
            for a, b in zip(pp, hh):
                inv[a][b].append(f"{short(part)}:{i+1}")
    out, n = [], 0
    for k in sorted(inv):
        v = inv[k]
        if len(v) > 1:
            n += 1
        out.append(f"### {k}" + ("" if len(v) > 1 else "  (one form)"))
        for h, locs in sorted(v.items(), key=lambda kv: -len(kv[1])):
            out.append(f"- [{len(locs)}] {h}   {' '.join(sorted({l.split(':')[0] for l in locs}))} ({locs[0]})")
        out.append("")
    out.append("### UNSPLIT (Pāli parts and Hindi parts differ in number)")
    out += [f"- {b}" for b in bad]
    out.append("")
    return ["## (c) triad / dyad / cluster names in headings and closing lines", "",
            f"stems with more than one form: {n}", ""] + out, n


def scan_d():
    g = collections.defaultdict(lambda: collections.defaultdict(list))
    for part in PARTS:
        for i, (p, h) in enumerate(pairs(part)):
            if not p.startswith("#"):
                continue
            kp = re.sub(r"^[\d\s\-–]+\.\s*", "", pnorm(p).lstrip("#").strip().strip("*").strip())
            kh = re.sub(r"^[\d\s\-–]+\.\s*", "", hnorm(h).lstrip("#").strip().strip("*").strip())
            g[kp][kh].append(f"{short(part)}:{i + 1}")
    out, n = [], 0
    for kp in sorted(g):
        v = g[kp]
        if len(v) < 2:
            continue
        n += 1
        out.append(f"### {kp}")
        for kh, locs in sorted(v.items(), key=lambda kv: -len(kv[1])):
            out.append(f"- [{len(locs)}] {' '.join(sorted({l.split(':')[0] for l in locs}))} ({locs[0]}) :: {kh}")
        out.append("")
    return ["## (d) headings (number prefix stripped): same Pāli, differing Hindi", "", f"groups: {n}", ""] + out, n


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--bak" in sys.argv:
        C.CUR["hdir"] = C.BAK
    dest = args[0] if args else os.path.join(HERE, "divergences.md")
    grp, raw = scan_a()
    oa, na = report_a(grp, raw)
    on, nn = scan_n()
    oc, nc = scan_c()
    od, nd = scan_d()
    ob = scan_b()
    head = ["# pi-7 Hindi RAILS (Paṭṭhāna): divergences (find_divergences_rails.py)", "",
            f"source: {'backup-pre-align' if '--bak' in sys.argv else 'current output'}", "",
            f"(a) identical-Pāli line groups with differing Hindi: {na}; (n) note groups: {nn}; "
            f"(c) names with >1 form: {nc}; (d) heading groups: {nd}", ""]
    open(dest, "w", encoding="utf-8").write("\n".join(head + ob + on + oc + od + oa) + "\n")
    print("a", na, "n", nn, "c", nc, "d", nd, "->", dest)


if __name__ == "__main__":
    main()
