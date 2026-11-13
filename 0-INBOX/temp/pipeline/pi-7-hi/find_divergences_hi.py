"""Find Hindi divergences for identical / recurring Pāli across the pi-7 (Paṭṭhāna) Hindi zero-shot chapter files.

(a) whole lines: group by normalised Pāli (^id, {…} variants, count markers "(3)" stripped, spaces collapsed);
    list groups where the Hindi (normalised the same way, «[…]» brackets stripped) differs.
    Groups whose Pāli differs only inside {…} are marked (they are merged by the normalisation).
(b) recurring words and frames: for each Pāli pattern in PHRASES, per file, the count of each candidate Hindi
    form on the aligned Hindi lines (and how many matching lines carry none of the candidates).
(c) triad / dyad / cluster names in headings and closing lines (hz7_names inventory): Pāli stem -> Hindi forms.
(d) every heading text: same Pāli heading, different Hindi.

usage: python -I -B -X utf8 find_divergences_hi.py [out.md] [--bak]
       (default out: divergences.md; --bak scans backup-pre-harmonise/, i.e. the state before the pass)
"""
import os, re, sys, collections, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz7_common as C
from hz7_common import PARTS, HERE, pairs, pnorm, hnorm, short

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


# ------------------------------------------------------------------ (b) recurring words and frames
PHRASES = []


def ph(name, pali, *cands):
    PHRASES.append((name, re.compile(pali), [re.compile(c) for c in cands]))


NAME_RX = r"[^\s,।()]+(?: [^\s,।()]+)*? वा(?:ला|ले) (?:तीन|दो) (?:का|के) वर्गीकरण"
ph("Paccanīyuddhāro", r"Paccanīyuddhār", r"नकारात्मक क्रम के लिए [^\s।*]+(?: [^\s।*^]+)*")
ph("niṭṭhitaṃ / niṭṭhito (closing)", r"niṭṭhit", r"समाप्त", r"पूरा हुआ", r"पूरे हुए", r"पूरी हुई", r"“")
ph("sahajātaṃ/-ā/-o (sub-kind label)", r"(^|[.–] )[Ss]ahajāt(aṃ|ā|o)\b(?!\s*(paccay|khandh|rūp|dhamm))",
   r"सह-उत्पत्ति रूपी", r"सह-उत्पत्ति(?! रूपी|-कारण| का खंड)")
ph("purejātaṃ (label)", r"(^|[.–,] )[Pp]urejātaṃ\b(?!\s*(paccay|khandh|rūp|dhamm))",
   r"पूर्व-उत्पत्ति रूपी", r"पूर्व-उत्पत्ति(?! रूपी|-कारण)", r"पहले उत्पन्न")
ph("pacchājātaṃ/-ā (label)", r"(^|[.–,] )[Pp]acchājāt(aṃ|ā|o)\s*[–,.]",
   r"पश्चात्-उत्पत्ति रूपी", r"पश्चात्-उत्पत्ति(?! रूपी|-कारण)", r"बाद में उत्पन्न")
ph("āhāraṃ / indriyaṃ (label)", r"(^|[.–,] )([Āā]hāraṃ|[Ii]ndriyaṃ)\s*[–,.]",
   r"आहार रूपी", r"क्षमता रूपी", r"आहार(?! रूपी|-कारण)", r"क्षमता(?! रूपी|-कारण)")
ph("nānākkhaṇikā", r"[Nn]ānākkhaṇik", r"भिन्न क्षण रूपी", r"भिन्न क्षणों वाला", r"भिन्न-क्षणिक", r"भिन्न क्षण(?! रूपी|ों)")
ph("ārammaṇādhipati", r"[Āā]rammaṇādhipati", r"विषय रूपी प्रधानता", r"विषय की प्रधानता")
ph("sahajātādhipati", r"[Ss]ahajātādhipati", r"सह-उत्पत्ति रूपी प्रधानता", r"सह-उत्पत्ति की प्रधानता")
ph("ārammaṇūpanissayo", r"[Āā]rammaṇūpanissay", r"विषय रूपी प्रबल आश्रय")
ph("anantarūpanissayo", r"[Aa]nantarūpanissay", r"निकटता रूपी प्रबल आश्रय")
ph("pakatūpanissayo", r"[Pp]akatūpanissay", r"स्वाभाविक प्रबल आश्रय")
ph("vatthupurejātaṃ / ārammaṇapurejātaṃ", r"(vatthu|ārammaṇa)purejāt", r"आधार रूपी पूर्व-उत्पत्ति", r"विषय रूपी पूर्व-उत्पत्ति")
ph("anulomaṃ (moment, before gotrabhu/vodāna)", r"[Aa]nuloma[ṃ]? (gotrabhu|vodān|phalasam)",
   r"अनुरूपता", r"अनुकूलता(?! का क्षण)", r"अनुकूलता का क्षण")
ph("gotrabhu", r"[Gg]otrabhu", r"गोत्र-परिवर्तन")
ph("vodāna", r"[Vv]odān", r"शुद्धि")
ph("bhavaṅga", r"[Bb]havaṅg", r"जीवन-धारा का मन", r"जीवन-धारा(?! का मन)", r"जीवन-प्रवाह")
ph("āvajjanā", r"[Āā]vajjan", r"मन को विषय की ओर मोड़ने की क्रिया", r"मन को विषय की ओर मोड़ना", r"मन को विषय की ओर मोड़ने")
ph("cuticitta", r"[Cc]uticitt", r"मृत्यु का मन", r"मृत्यु-क्षण का मन", r"मृत्यु के मन")
ph("upapatticitta", r"[Uu]papatticitt", r"जन्म का मन", r"जन्म के मन", r"जन्म-क्षण का मन", r"जन्म-क्षण के मन", r"उत्पत्ति का मन", r"उत्पत्ति के मन")
ph("paṭisandhi (word)", r"[Pp]aṭisandhi(?!kkhaṇ|khaṇ)", r"पुनर्जन्म")
ph("vuṭṭhāna", r"[Vv]uṭṭhān", r"बाहर आने वाला मन", r"बाहर आ", r"उत्थान")
ph("vuṭṭhahantassa (nirodhā)", r"vuṭṭhahantassa", r"से उठने वाले", r"से बाहर आने वाले", r"से बाहर आ रहे")
ph("parikamma", r"[Pp]arikamm", r"प्रारंभिक तैयारी", r"(?<!प्रारंभिक )तैयारी", r"प्रारंभिक अभ्यास")
ph("phalasamāpatti", r"[Pp]halasamāpatt", r"फल की ध्यान-अवस्था")
ph("pavatte / pavatti", r"\b[Pp]avatt(e|i)\b", r"जीवन के दौरान", r"जीवन का प्रवाह", r"जीवन-प्रक्रिया", r"जीवन-काल", r"जीवन-प्रवाह", r"प्रक्रिया")
ph("ghaṭanā", r"ghaṭan", r"संयोजन", r"मेल")
ph("sabhāga", r"sabhāg", r"साथी कारण", r"सहभागी कारण")
ph("mūla / mūlaka (series start, item-based)", r"mūl(a|ak)[ṃe]?\b(?!.*paccay)", r"शृंखला", r"आरंभ-बिंदु", r"आरंभिक पद", r"मूल वाक्य", r"मूल पद", r"से शुरू होने वाले")
ph("gamana", r"gaman", r"प्रसंग", r"दौर", r"क्रम")
ph("cakkaṃ", r"[Cc]akkaṃ", r"बारी-बारी से", r"चक्र")
ph("saṃkhittaṃ / saṅkhitaṃ", r"[Ss]aṃkhitt|[Ss]aṅkhit", r"संक्षिप्त", r"संक्षेप")
ph("vitthāretabbaṃ", r"vitthāret", r"विस्तार करना चाहिए", r"विस्तार करने चाहिए", r"विस्तार से कहना")
ph("vitthāro", r"vitthāro", r"विस्तार")
ph("sadisaṃ", r"sadis", r"के समान", r"जैसा", r"एक जैसे")
ph("kātabbaṃ / kātabbā", r"kātabb", r"तैयार करन", r"बनान", r"(?<![ा-ौ])करना चाहिए", r"करने चाहिए", r"लागू करन", r"शामिल करन")
ph("ninnānākaraṇaṃ", r"ninnān", r"बिना किसी अंतर के", r"कोई अंतर नहीं", r"बिना किसी भिन्नता के", r"बिना अंतर के")
ph("gaṇetabbaṃ", r"gaṇet", r"गिनना चाहिए", r"गणना")
ph("pañhā", r"pañhā\b", r"प्रश्न")
ph("na/nana double negation", r"\b[Nn]ana|\b[Nn]ano", r"न होने वाली” न होने वाली", r"न होने वाली न होने वाली", r"“")
ph("X ceva na/no ca Y", r"(ceva|ñceva) n[ao] ca", r", पर स्वयं", r"न होने वाली")
ph("X ceva Y ca", r"(ceva|ñceva) (?!n[ao] ca)\w+ ca\b|ñceva \w+ñca", r"भी और .*? भी", r" भी")
ph("{…} editorial query without siglum", r"\{[^}(]*\}", r"\[पाठभेद", r"\[(?!पाठभेद)")
ph("count line with quotes", r"(ghaṭan|-\w+nti\b|\w+-\w+-\w+nti)", r"“", r"”")
ph("tika / dyad names in Hindi lines", r"ttik|duk", NAME_RX)
ph("Siyā question", r"^Siyā", r"\?")
ph("niṭṭhito bhāgo", r"bhāgo niṭṭhito", r"भाग समाप्त", r"भाग पूरा")


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
                        if c.pattern == NAME_RX or name == "Paccanīyuddhāro":
                            for m in ms:
                                cnt[part][m if isinstance(m, str) else m[0]] += 1
                        else:
                            cnt[part][c.pattern] += len(ms)
                if not hit:
                    cnt[part]["_none"] += 1
        tab.append((name, rx.pattern, cnt))
    out = ["## (b) recurring words and frames: candidate Hindi forms per file", "",
           "Counts are occurrences of each candidate (regex) on Hindi lines whose aligned Pāli matches; "
           "_lines = matching lines, _none = matching lines with none of the candidates.", ""]
    for name, pat, cnt in tab:
        if name.startswith("tika / dyad names"):
            continue  # covered by (c)
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
    import hz7_names
    inv, _ = hz7_names.collect()
    oc, nc = ["## (c) triad / dyad / cluster names in headings and closing lines", ""], 0
    for k in sorted(inv):
        v = inv[k]
        if len(v) > 1:
            nc += 1
        oc.append(f"### {k}" + ("" if len(v) > 1 else "  (one form)"))
        for h, locs in sorted(v.items(), key=lambda kv: -len(kv[1])):
            oc.append(f"- [{len(locs)}] {h}   {' '.join(sorted({l.split(':')[0] for l in locs}))}")
        oc.append("")
    oc.insert(2, f"stems with more than one form: {nc}")
    od, nd = scan_d()
    ob = scan_b()
    head = ["# pi-7 Hindi zero-shot (Paṭṭhāna): divergences (find_divergences_hi.py)", "",
            f"source: {'backup-pre-harmonise' if '--bak' in sys.argv else 'current output'}", "",
            f"(a) identical-Pāli line groups with differing Hindi: {na}; (c) names with >1 form: {nc}; "
            f"(d) heading groups: {nd}", ""]
    open(dest, "w", encoding="utf-8").write("\n".join(head + oc + od + ob + oa) + "\n")
    print("a", na, "c", nc, "d", nd, "->", dest)


if __name__ == "__main__":
    main()
