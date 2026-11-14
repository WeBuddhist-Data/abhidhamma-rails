import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from r1_align import load, strip_id, PD, RD, FILES

# ordered token maps: (pali regex, russian regex)
SEQ = [
    (r"dukkhapaṭipadaṃ", r"с трудным способом"),
    (r"sukhapaṭipadaṃ", r"с лёгким способом"),
    (r"dandhābhiññaṃ", r"медленным высшим"),
    (r"khippābhiññaṃ", r"быстрым высшим"),
    (r"\bparittaṃ parittārammaṇaṃ", r"ограниченное и с ограниченным"),
    (r"\bparittaṃ appamāṇārammaṇaṃ", r"ограниченное и с безмерным"),
    (r"\bappamāṇaṃ parittārammaṇaṃ", r"безмерное и с ограниченным"),
    (r"\bappamāṇaṃ appamāṇārammaṇaṃ", r"безмерное и с безмерным"),
    (r"paṭhamaṃ jhānaṃ|paṭhamajjhānaṃ", r"первое медитативное"),
    (r"dutiyaṃ jhānaṃ|dutiyajjhānaṃ", r"второе медитативное"),
    (r"tatiyaṃ jhānaṃ|tatiyajjhānaṃ", r"третье медитативное"),
    (r"catutthaṃ jhānaṃ|catutthajjhānaṃ", r"четвёртое медитативное"),
    (r"pañcamaṃ jhānaṃ|pañcamajjhānaṃ", r"пятое медитативное"),
    (r"somanassasahagataṃ", r"сопровождаемый радостью"),
    (r"upekkhāsahagataṃ ñāṇ", r"сопровождаемый невозмутимостью"),
    (r"ñāṇasampayuttaṃ", r"(?<!не )связанный со знанием"),
    (r"ñāṇavippayuttaṃ", r"не связанный со знанием"),
    (r"sasaṅkhārena", r"с побуждением"),
    (r"\bhīnaṃ", r"низш"),
    (r"majjhimaṃ", r"средн"),
    (r"paṇītaṃ", r"высш(ий|ее)"),
    (r"chandādhipateyyaṃ", r"преобладанием желания"),
    (r"vīriyādhipateyyaṃ", r"преобладанием усердия"),
    (r"cittādhipateyyaṃ", r"преобладанием ума"),
    (r"vīmaṃsādhipateyyaṃ", r"преобладанием пытливости"),
    (r"pathavīkasiṇaṃ", r"объектом земли"),
    (r"(?<!a)kusal", r"(?<!не)благ"),
    (r"akusal", r"неблаг"),
    (r"abyākat", r"неопредел"),
]
NUM = [
    (r"\bcattāro khandhā", "четыре совокупности"), (r"dvāyatanāni", "две сферы"), (r"dve dhātuyo", "два элемента"),
    (r"tayo āhārā", "три вида питания"), (r"aṭṭhindriyāni", "восемь способностей"), (r"sattindriyāni", "семь способностей"),
    (r"pañcaṅgikaṃ jhānaṃ", "пятичастное медитативное"), (r"caturaṅgikaṃ jhānaṃ", "четырёхчастное медитативное"),
    (r"tivaṅgikaṃ jhānaṃ", "трёхчастное медитативное"), (r"duvaṅgikaṃ jhānaṃ", "двухчастное медитативное"),
    (r"pañcaṅgiko maggo", "пятичастный путь"), (r"caturaṅgiko maggo", "четырёхчастный путь"),
    (r"satta balāni", "семь сил"), (r"cha balāni", "шесть сил"), (r"tayo hetū", "три корня"), (r"dve hetū", "два корня"),
]


def seq(s, pats, idx):
    hits = []
    for i, pr in enumerate(pats):
        for m in re.finditer(pr[idx], s):
            hits.append((m.start(), i))
    hits.sort()
    return [h[1] for h in hits]


def main():
    for f in FILES:
        _, ps = load(os.path.join(PD, f))
        _, rs = load(os.path.join(RD, f))
        for (pid, pl, _), (rid, rl, _) in zip(ps, rs):
            for a, b in zip(pl, rl):
                a2 = re.sub(r"\[[^\]]*\]", "", strip_id(a))
                b2 = re.sub(r"\[[^\]]*\]", "", strip_id(b))
                if f.startswith("2-"):
                    sa = seq(a2, SEQ, 0)
                    sb = seq(b2, SEQ, 1)
                    # kusal pattern also matches akusal; normalise: drop 'kusal' hits where akusal
                    if sa != sb:
                        print("SEQ", f[:4], pid, [SEQ[i][0][:12] for i in sa], "||", [SEQ[i][1][:12] for i in sb])
                    na = seq(a2, NUM, 0)
                    nb = seq(b2, NUM, 1)
                    if na != nb:
                        print("NUM", f[:4], pid, na, nb)
                    ha = len(re.findall(r"\bhoti\b|\bhonti\b", a2.split(";")[0])) if "hoti," in a2 else None
                    if ha is not None:
                        hb = len(re.findall(r"(?<![А-Яа-яё])есть(?![А-Яа-яё])", b2.split(";")[0]))
                        if ha != hb:
                            print("HOTI", f[:4], pid, ha, hb)
                # list items for space-separated saṅkhārakkhandha lists
                m = re.match(r"(Katamo tasmiṃ samaye (eko )?saṅkhārakkhandho hoti\? )?Phasso (.*?)(;|\.|$)", a2)
                if m:
                    na = len(m.group(3).split()) + 1
                    rb = re.sub(r"^Что такое [^?]*\? ", "", b2)
                    mb = re.match(r"Контакт, (.*?)(;|\.|$)", rb)
                    if mb:
                        # count Pali items: words, but 'cittassekaggatā' is one token; Russian items by comma
                        nbb = len(mb.group(1).split(",")) + 1
                        if na != nbb:
                            print("SKLIST", f[:4], pid, na, nbb)
                    else:
                        print("SKLIST-nomatch", pid, rb[:60])


main()
