"""r2 review helper: line-aligned Pāli/Russian checks for 3-01..3-06 ayatanayamaka."""
import re, sys, os, collections

PD = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
RD = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-6-russian-plain-rails_split_chapters"
FILES = [f"3-0{i}-ayatanayamaka.md" for i in range(1, 7)]

def lines(path):
    raw = open(path, encoding="utf-8").read()
    return raw, [l for l in raw.split("\n") if l.strip()]

# (name, pali regex, russian regex)
PAIRS = [
    ("eye", r"cakkh[uū]?āyatan|cakkhāyatan", r"сфер\w*\s+глаза"),
    ("ear", r"sotāyatan|sotāyan", r"сфер\w*\s+уха"),
    ("nose", r"ghānāyatan", r"сфер\w*\s+носа"),
    ("tongue", r"jivhāyatan", r"сфер\w*\s+языка"),
    ("body", r"kāyāyatan", r"сфер\w*\s+тела"),
    ("vis", r"rūpāyatan", r"сфер\w*\s+видимых\s+форм"),
    ("sound", r"saddāyatan", r"сфер\w*\s+звуков"),
    ("smell", r"gandhāyatan", r"сфер\w*\s+запахов"),
    ("taste", r"rasāyatan", r"сфер\w*\s+вкусов"),
    ("touch", r"phoṭṭhabbāyatan", r"сфер\w*\s+осязаемого"),
    ("mind", r"manāyatan", r"сфер\w*\s+ума"),
    ("dham", r"dhammāyatan", r"сфер\w*\s+объектов\s+ума"),
    # tenses: uppajj
    # persons / planes
    ("upapajjantanam", r"upapajjantānaṃ", r"перерожда(ется|ются|ющихся)"),
    ("upapajjitva", r"upapajjitvā", r"переродившись"),
    ("cavanta", r"cavantānaṃ", r"умира(ет|ют|ющих)"),
    ("parinibbanta", r"parinibb[aā]ntānaṃ", r"достига(ет|ют) окончательного угасания"),
    ("parinibbayissanti", r"parinibbāyissanti", r"достигн(ет|ут) окончательного угасания"),
    ("pacchima", r"pacchimabhavik", r"последн(ей жизнью|ий раз)"),
    ("sabbesam", r"sabbesaṃ", r"\bвсех\b"),
    ("itaresam", r"itaresaṃ", r"\bостальных\b"),
    ("asanna", r"asaññasatt", r"без восприятия"),
    ("suddhavasa", r"suddhāvās", r"[Чч]истых обител"),
    ("pancavok", r"pañcavokār", r"пятью составляющими"),
    ("catuvok", r"catuvokār", r"четырьмя составляющими"),
    ("kamavacara", r"kāmāvacar", r"чувственных желаний"),
    ("rupavacara", r"(?<!a)rūpāvacar", r"мир\w*\s+форм\b"),
    ("arupa", r"arūpāvacar|arūpe\b|arūpānaṃ|arūpaṃ", r"без форм\b"),
    ("arahant", r"arah(ā|antañca)", r"архат"),
    ("aggamagga", r"aggamaggasamaṅgī", r"высшим путём"),
    ("puthujjana", r"puthujjanā", r"обычные люди"),
    ("sacakkhu", r"sacakkhuk", r"с глазом"),
    ("acakkhu", r"(?<!s)acakkhuk", r"без глаза"),
    ("sasota", r"sasotak", r"с ухом"),
    ("asota", r"(?<!s)asotak", r"без уха"),
    ("saghana", r"saghānak", r"с носом"),
    ("aghana", r"(?<!s)aghānak", r"без носа"),
    ("sarupa", r"sarūpak", r"с видимой формой"),
    ("arupak", r"(?<!s)arūpak", r"без видимой формы"),
    ("sacitta", r"sacittak", r"с умом"),
    ("acitta", r"(?<!s)acittak", r"без ума"),
    ("amanta", r"āmantā", r"\bДа\b"),
    ("natthi", r"[Nn]atthi", r"[Тт]акого нет|различия нет"),
    ("pe", r"pe…|…pe|…Pe", r"…"),
]

NEGP = re.compile(r"(?<![a-zāīūṃ])(na|no|nuppajj\w*|nāyatan\w*|neva|noti)(?![a-zāīūṃ])", re.I)
NEGR = re.compile(r"(?<![а-яё])(не|ни|нет)(?![а-яё])", re.I)

def labels(l, lang):
    if lang == "p":
        return re.findall(r"\((Ka|Kha|Ga|Gha|Ṅa|Ca)\)", l)
    return re.findall(r"\(([абвгде])\)", l)
LMAP = {"Ka": "а", "Kha": "б", "Ga": "в", "Gha": "г", "Ṅa": "д", "Ca": "е"}

def verbs_pali(l):
    """sequence of (verb, tense, neg) in order"""
    out = []
    toks = re.findall(r"[^\W\d_]+|[.,?]", l)
    last_neg = False
    for t in toks:
        tl = t.lower()
        if tl in ".,?":
            last_neg = False
            continue
        if tl in ("na", "no"):
            last_neg = not last_neg
            continue
        m = re.match(r"(n?)(uppajj|nirujjh|parijān)(ati|atī|anti|itth|iss|i)", tl)
        if m and not tl.startswith("upapajj"):
            v = {"uppajj": "U", "nirujjh": "N", "parijān": "P"}[m.group(2)]
            tn = m.group(3)
            tense = "pres" if tn.startswith("at") or tn == "anti" else ("past" if tn.startswith("itt") else "fut")
            neg = bool(m.group(1)) != last_neg
            out.append((v, tense, neg))
            last_neg = False
    return out

RV = [
    (r"возникает", "U", "pres"), (r"возникал[аои]?", "U", "past"), (r"возникнет", "U", "fut"),
    (r"прекращается", "N", "pres"), (r"прекращал(?:ась|ся|ось|ись)", "N", "past"), (r"прекратится", "N", "fut"),
    (r"понима(?:ет|ют)", "P", "pres"), (r"понял[иа]?", "P", "past"), (r"пойм(?:ёт|ут)", "P", "fut"),
]
RVRE = re.compile(r"(?<![а-яё])(не\s+)?(" + "|".join(p for p, _, _ in RV) + r")(?![а-яё])", re.I)

def verbs_rus(l):
    out = []
    ms = list(RVRE.finditer(l))
    for i, m in enumerate(ms):
        w = m.group(2).lower()
        for p, v, t in RV:
            if re.fullmatch(p, w):
                break
        neg = bool(m.group(1))
        n = 1
        if neg:
            end = ms[i + 1].start() if i + 1 < len(ms) else len(l)
            seg = l[m.end():end]
            seg = re.split(r"[.?]", seg)[0]
            k = len(re.findall(r"(?<![а-яё])ни(?![а-яё])", seg))
            if k >= 2:
                n = k
        # "и возникает X, и возникает Y" -> each separately (already)
        out.extend([(v, t, neg)] * n)
    return out

def member_seq(l, lang):
    pats = [(n, pp if lang == "p" else rp) for n, pp, rp in PAIRS[:12]]
    big = "|".join(f"(?P<{n}>{x})" for n, x in pats)
    return [m.lastgroup for m in re.finditer(big, l, re.I)]

def main():
    sel = sys.argv[1:] or FILES
    total_seg = 0
    for f in sel:
        praw, pl = lines(os.path.join(PD, f))
        rraw, rl = lines(os.path.join(RD, f))
        print(f"===== {f}: pali {len(pl)} lines, rus {len(rl)} lines")
        if "\n\n\n" in rraw:
            print("  DOUBLE BLANK LINE in Russian")
        if "\r" in rraw:
            print("  CR in Russian")
        ids_p = [re.findall(r"\^[\d-]+\s*$", l) for l in pl]
        total_seg += sum(1 for x in ids_p if x)
        for i, (p, r) in enumerate(zip(pl, rl)):
            idp = re.findall(r"\^[\d-]+", p)
            idr = re.findall(r"\^[\d-]+", r)
            tag = f"L{i+1}"
            probs = []
            if idp != idr:
                probs.append(f"ID {idp} vs {idr}")
            if p.count("–") + p.count("—") != r.count("–") + r.count("—"):
                probs.append("DASH")
            if re.search(r"(?<![а-яё])ли(?![а-яё])", r):
                probs.append("LI")
            lp = labels(p, "p"); lr = labels(r, "r")
            if [LMAP[x] for x in lp] != lr:
                probs.append(f"LABEL {lp} vs {lr}")
            if p.rstrip().endswith("?") != r.rstrip().endswith("?") and not idp:
                probs.append("ENDPUNCT")
            pe = re.sub(r"\s*\^[\d-]+\s*$", "", p).rstrip()[-1:]
            re_ = re.sub(r"\s*\^[\d-]+\s*$", "", r).rstrip()[-1:]
            if pe != re_ and not p.startswith("#") and not (pe=='.' and re_=='…'):
                probs.append(f"END '{pe}' vs '{re_}'")
            for name, pp, rp in PAIRS:
                cp = len(re.findall(pp, p, re.I)); cr = len(re.findall(rp, r, re.I))
                if name == "pe":
                    cp = len(re.findall(r"[Pp]e…", p)) + len(re.findall(r"…(?![Pp]e)", p.replace("…pe…", "#").replace("…Pe…", "#")))
                    cp = p.count("…pe…") + p.count("…Pe…") + len(re.findall(r"…", re.sub(r"…[Pp]e…", "", p)))
                    cr = r.count("…")
                if cp != cr:
                    probs.append(f"{name} {cp}/{cr}")
            vp = verbs_pali(p); vr = verbs_rus(r)
            if collections.Counter(vp) != collections.Counter(vr):
                probs.append(f"VERBS P{vp} R{vr}")
            elif vp != vr:
                probs.append(f"VERBORDER P{vp} R{vr}")
            mp = member_seq(p, "p"); mr = member_seq(r, "r")
            if collections.Counter(mp) == collections.Counter(mr) and mp != mr:
                probs.append(f"MEMBERORDER P{mp} R{mr}")
            # Latin outside brackets
            rr = re.sub(r"\[[^\]]*\]", "", r)
            rr = re.sub(r"\^[\d-]+", "", rr)
            lat = re.findall(r"[A-Za-zāīūṃñṭḍṅḷ]{2,}", rr)
            if lat:
                probs.append(f"LATIN {lat}")
            if probs:
                print(f"{tag} {'; '.join(probs)}")
                print("   P:", p[:300])
                print("   R:", r[:300])
    print("segments (block ids):", total_seg)

main()
