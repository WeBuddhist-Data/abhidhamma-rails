import re, os, sys
B = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
M = [
    ("cakkhāyatana", "сфера глаза"), ("sotāyatana", "сфера уха"), ("ghānāyatana", "сфера носа"),
    ("jivhāyatana", "сфера языка"), ("kāyāyatana", "сфера тела"), ("rūpāyatana", "сфера видимых форм"),
    ("saddāyatana", "сфера звуков"), ("gandhāyatana", "сфера запахов"), ("rasāyatana", "сфера вкусов"),
    ("phoṭṭhabbāyatana", "сфера осязаемого"), ("itthindriya", "способность женственности"),
    ("purisindriya", "способность мужественности"), ("jīvitindriya", "жизненная способность"),
    ("cakkhundriya", "способность глаза"), ("sotindriya", "способность уха"), ("ghānindriya", "способность носа"),
    ("jivhindriya", "способность языка"), ("kāyindriya", "способность тела"),
    ("kāyaviññatti", "телесное внешнее выражение"), ("vacīviññatti", "речевое внешнее выражение"),
    ("ākāsadhātu", "элемент пространства"), ("āpodhātu", "элемент воды"), ("pathavīdhātu", "элемент земли"),
    ("tejodhātu", "элемент огня"), ("vāyodhātu", "элемент ветра"),
    ("rūpassa lahutā", "лёгкость материальной формы"), ("rūpassa mudutā", "мягкость материальной формы"),
    ("rūpassa kammaññatā", "работоспособность материальной формы"), ("rūpassa upacayo", "рост материальной формы"),
    ("rūpassa santati", "непрерывность материальной формы"), ("rūpassa jaratā", "старение материальной формы"),
    ("rūpassa aniccatā", "непостоянство материальной формы"), ("kabaḷīkāro āhāro", "съедаемая пища"),
]
def seq(text, idx):
    hits = []
    for k, (p, r) in enumerate(M):
        pat = p if idx == 0 else r
        for m in re.finditer(re.escape(pat), text, flags=re.I):
            hits.append((m.start(), k))
    hits.sort()
    return [k for _, k in hits]
for ch in sys.argv[1:]:
    P = open(os.path.join(B, "pali", "pi-1_split_chapters", ch), encoding="utf-8").read().split("\n")
    R = open(os.path.join(B, "russian", "pi-1-russian-plain-rails_split_chapters", ch), encoding="utf-8").read().split("\n")
    n = 0
    for i, (p, r) in enumerate(zip(P, R)):
        if not p.startswith("Katamaṃ"):
            continue
        n += 1
        pa = p.split("?", 1)[1] if "?" in p else p
        pa = pa.split(" – idaṃ")[0]
        ra = r.split("?", 1)[1] if "?" in r else r
        ra = ra.split(" – это")[0]
        # cut long definitions (cakkhu etc.) irrelevant
        sp, sr = seq(pa, 0), seq(ra, 1)
        if sp != sr and not pa.strip().startswith("Y"):
            print(ch, i + 1, "P:", [M[k][0] for k in sp], "\n   R:", [M[k][0] for k in sr])
        # polarity counts
        for pp, rr in [("na kammassa", "не вследствие"), ("kammassa katattā", "вследствие совершённых"),
                       ("na cittajaṃ", "не рождённой умом"), ("cittajaṃ", "рождённой умом"),
                       ("…pe…", "…")]:
            cp = len(re.findall(re.escape(pp), pa, flags=re.I)); cr = len(re.findall(re.escape(rr), ra, flags=re.I))
            if cp != cr:
                print(ch, i + 1, "COUNT", pp, cp, rr, cr)
        # question polarity: count ' na ' / 'no ' / 'an' items in question vs 'не ' in question
        q_p = p.split("?")[0]; q_r = r.split("?")[0]
        neg_p = len(re.findall(r"\b(na|no)\b", q_p)) + len(re.findall(r"\b(anupādiṇṇ|anidassan|appaṭigh)", q_p))
        neg_r = len(re.findall(r"\bне\b|невидим", q_r, flags=re.I)) + len(re.findall(r"непроизводн", q_r, flags=re.I))
        if neg_p != neg_r:
            print(ch, i + 1, "QNEG", neg_p, neg_r, "|", q_p[-80:], "|", q_r[-120:])
        # answer tail polarity
        t_p = p.split(" – idaṃ taṃ rūpaṃ")[-1]; t_r = r.split(" – это")[-1]
        neg_p = len(re.findall(r"\b(na|no)\b", t_p)) + len(re.findall(r"\b(anupādiṇṇ|anidassan|appaṭigh)", t_p))
        neg_r = len(re.findall(r"\bне\b|невидим", t_r, flags=re.I)) + len(re.findall(r"непроизводн", t_r, flags=re.I))
        if neg_p != neg_r:
            print(ch, i + 1, "TNEG", neg_p, neg_r, "|", t_p[-80:], "|", t_r[-120:])
    print(ch, "checked", n)
