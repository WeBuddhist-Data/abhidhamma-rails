"""Consistency (harmonise) pass for the pi-2 (Vibhaṅga) Russian plain zero-shot.

Applies fixed old -> new strings to the Russian chapter files. A rule touches a Russian line ONLY when the aligned
Pāli line (non-empty line i <-> non-empty line i) matches the rule's Pāli pattern, and only in the chapters listed
for it. Line counts, block IDs, heading levels, dashes and variant brackets are never touched (asserted per
changed line). Protected (user-approved, never changed): preamble and the first 77 non-empty lines of
1-khandhavibhango (= ch1-sample.md).
Backup of the pre-pass files: backup-pre-harmonise/ (made once, before the first run). The pass always reads from
the backup, so it is rerunnable: rerunning it rebuilds the same output. Log: harmonise-log.tsv
(rule, part, segment, line, old, new).

usage: python -I -X utf8 harmonise_ru.py [--dry]
"""
import os, re, sys, collections

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
RDIR = os.path.join(ROOT, r"AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-2-ru")
BAK = os.path.join(HERE, "backup-pre-harmonise")
PARTS = ["preamble", "1-khandhavibhango", "2-ayatanavibhango", "3-dhatuvibhango", "4-saccavibhango",
         "5-indriyavibhango", "6-paticcasamuppadavibhango", "7-satipatthanavibhango", "8-sammappadhanavibhango",
         "9-iddhipadavibhango", "10-bojjhangavibhango", "11-maggangavibhango", "12-jhanavibhango",
         "13-appamannavibhango", "14-sikkhapadavibhango", "15-patisambhidavibhango", "16-nanavibhango",
         "17-khuddakavatthuvibhango", "18-dhammahadayavibhango"]
PROTECTED_PARTS = {"preamble"}
PROTECTED_1 = 77  # first 77 non-empty lines of 1-khandhavibhango = approved sample
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

R = []  # (id, pali_regex, old, new, is_regex, chapter numbers or None)


def rule(rid, pali, old, new, rx=False, ch=None):
    R.append((rid, pali, old, new, rx, ch))


def chno(part):
    return part.split("-")[0]


# ---------------------------------------------------------------- 1. vīriyindriya string, ch5 ^2-220 (coordinator)
# The Pāli ends «… vīriyaṃ vīriyindriyaṃ vīriyabalaṃ – idaṃ vuccati», no sammāvāyāmo: drop the added item.
# (check_viriya_ru.py checks all 37 vīriya strings of the book against their own Pāli lines: this is the only one.)
rule("D1-viriya", r"vīriyindriyaṃ vīriyabalaṃ [–—] idaṃ vuccati",
     "способность усердия, сила усердия, правильное усилие, – это", "способность усердия, сила усердия, – это", ch=["5"])

# ---------------------------------------------------------------- 2. kāmesumicchācāra (ch4, 11, 17, pi-5 wording)
rule("D2-kamesu", r"kāmesumicchācār", "от неподобающего поведения в чувственных удовольствиях",
     "от неправильного поведения в чувственных удовольствиях", ch=["14"])

# ---------------------------------------------------------------- 3. Akaniṭṭha / formless-realm gods in ^2-1020
# (ch18 god list ^2-1021 … ^2-1028 = pi-5: «высочайшие боги», «боги, достигшие сферы …»)
rule("D3-gods", r"uparito akaniṭṭhe deve", "включить в эти пределы богов Аканиттха",
     "включить в эти пределы высочайших богов", ch=["18"])
rule("D3-gods", r"ākāsānañcāyatanūpage deve pariyantaṃ", "богов, рождённых в сфере бесконечного пространства",
     "богов, достигших сферы бесконечного пространства", ch=["18"])
rule("D3-gods", r"nevasaññānāsaññāyatanūpage deve anto", "богов, рождённых в сфере ни восприятия, ни невосприятия",
     "богов, достигших сферы ни восприятия, ни невосприятия", ch=["18"])

# ---------------------------------------------------------------- 4. sajjha / rajata (ch3 ^2-173)
# Vibhaṅga aṭṭhakathā on the outer earth element: «Sajjhūti rajataṃ» (sajjhu = silver, the metal) and
# «Rajatanti kahāpaṇo» (rajata in this list = coin). pi-1 has no such list (its jātarūparajata «золото и серебро»
# also stands in pi-2 ch2 ^2-162 and stays). sajjhaṃ keeps «серебро», rajataṃ becomes «монеты».
rule("D4-rajata", r"pavāḷaṃ rajataṃ jātarūpaṃ", "коралл, серебро, золото", "коралл, монеты, золото", ch=["3"])

# ---------------------------------------------------------------- 6. the one remaining «X, – это» after a plain noun
rule("D6-comma", r"Pathavīdhātu…pe… phoṭṭhabbadhātupesā [–—] ayaṃ vuccati",
     "… это элемент осязаемого, – это", "… это элемент осязаемого – это", ch=["3"])

# ---------------------------------------------------------------- 7. other divergences (pi-1 Russian wins)
# 7a ṭhapetvā = кроме (pi-1, pi-5 termbase; pi-2 ch6, 12, 17, 18)
rule("D7-thapetva", r"[Ṭṭ]hapetvā", "За исключением ", "Кроме ", ch=["16"])
rule("D7-thapetva", r"[Ṭṭ]hapetvā", "за исключением ", "кроме ", ch=["16"])

# 7b Dasa kilesavatthūni list: no «и» before the last item (pi-1 ^1-1218 …; pi-2 ch17 ^2-966)
rule("D7-kilesavatthu", r"Dasa kilesavatthūni [–—] lobho",
     "беспокойство, бессовестность и отсутствие страха перед дурным.",
     "беспокойство, бессовестность, отсутствие страха перед дурным.", ch=["16"])

# 7c ch16 niddesa headings and closings = pi-1 Rūpakaṇḍa (same structure: «Ekavidhena X … Evaṃ ekavidhena X» and
#    «Ekakaniddeso … Ekakaṃ.»): «Разъяснение классификации по одному» / «Классификация по одному.» (pi-1 ^1-2-3-1-0,
#    ^1-584 …). ch17 «Единицы. … Восьмёрки.» (groups of items in a list, like pi-1 4-01 «Тройки.») and the ch1 … ch15
#    question-section headings «Тройки» / «Пары» stay: same Pāli word, other referent (pi-1 makes the same split).
_N = [("Ekaka", "единиц", "Единицы", "по одному"), ("Duka", "пар", "Пары", "на два вида"),
      ("Tika", "троек", "Тройки", "на три вида"), ("Catukka", "четвёрок", "Четвёрки", "на четыре вида"),
      ("Pañcaka", "пятёрок", "Пятёрки", "на пять видов"), ("Chakka", "шестёрок", "Шестёрки", "на шесть видов"),
      ("Sattaka", "семёрок", "Семёрки", "на семь видов"), ("Aṭṭhaka", "восьмёрок", "Восьмёрки", "на восемь видов"),
      ("Navaka", "девяток", "Девятки", "на девять видов"), ("Dasaka", "десяток", "Десятки", "на десять видов")]
for pal, gen, nom, cls in _N:
    rule("D7-niddesa", rf"^##### {pal}niddeso\b", f"##### Объяснение {gen} ", f"##### Разъяснение классификации {cls} ",
         ch=["16"])
    rule("D7-niddesa", rf"^{pal}ṃ\.", rf"^{nom}\.", f"Классификация {cls}.", rx=True, ch=["16"])
# 7d niddesa = «разъяснение» (pi-1 ^1-2-3-1-0 …; pi-2 ch6, ch7, ch16): the ch17 group headings keep their counted nouns
rule("D7-niddesa", r"^#### \w+niddeso\b", "#### Объяснение ", "#### Разъяснение ", ch=["17"])


# ------------------------------------------------------------------------------------------------- engine
def dashes(t):
    return t.count("—") + t.count("–")


def main(dry=False):
    log = []
    tot = collections.Counter()
    changed = collections.Counter()
    hit = set()
    blocked = []
    comp = [(rid, re.compile(p), old, new, rx, ch) for rid, p, old, new, rx, ch in R]
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        text = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        assert "\r" not in text and not text.startswith("\ufeff"), part
        el = text.split("\n")
        idx = [i for i, l in enumerate(el) if l.strip()]
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        sid_of, cur = {}, []
        for k in range(len(idx)):
            cur.append(k)
            m = ID.search(pl[k])
            if m:
                for kk in cur:
                    sid_of[kk] = m.group(1)
                cur = []
        for k, li in enumerate(idx):
            p, e0 = pl[k], el[li]
            e = e0
            for ri, (rid, pr, old, new, rx, ch) in enumerate(comp):
                if ch and chno(part) not in ch:
                    continue
                if not pr.search(p):
                    continue
                if rx:
                    e2, n = re.subn(old, new, e)
                    if e2 == e:
                        n = 0
                else:
                    n = e.count(old)
                    e2 = e.replace(old, new)
                if n:
                    hit.add(ri)
                    if part in PROTECTED_PARTS or (part.startswith("1-") and k < PROTECTED_1):
                        blocked.append((rid, part, k + 1))
                        continue
                    log.append((rid, part, sid_of.get(k, "?"), k + 1, e, e2))
                    tot[(rid, part)] += n
                    e = e2
            if e != e0:
                assert dashes(e) == dashes(e0), (part, k, "dash count changed", e)
                assert ID.findall(e) == ID.findall(e0), (part, k, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k, "heading")
                assert re.findall(r"\[[^\]]*\]", e) == re.findall(r"\[[^\]]*\]", e0), (part, k, "brackets")
                assert "—" not in e and ":-" not in e, (part, k)
                el[li] = e
                changed[part] += 1
        if not dry:
            open(os.path.join(RDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write("\n".join(el))
    if not dry:
        with open(os.path.join(HERE, "harmonise-log.tsv"), "w", encoding="utf-8", newline="\n") as f:
            f.write("rule\tpart\tsegment\tline\told\tnew\n")
            for rid, part, sid, ln, old, new in log:
                f.write(f"{rid}\t{part}\t^{sid}\t{ln}\t{old}\t{new}\n")
    per = collections.defaultdict(dict)
    for (rid, part), n in tot.items():
        per[rid]["ch" + chno(part)] = n
    for rid in sorted(per):
        print(f"{rid:18s} " + ", ".join(f"{p}={n}" for p, n in sorted(per[rid].items())))
    print("lines changed per part:", dict(changed), "total", sum(changed.values()), "(dry run)" if dry else "")
    if blocked:
        print("BLOCKED (protected lines a rule would have changed):", blocked)
    for ri, r in enumerate(R):
        if ri not in hit:
            print("NO HIT:", r[0], "|", str(r[2])[:90])


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
