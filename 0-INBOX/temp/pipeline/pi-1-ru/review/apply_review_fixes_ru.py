"""Apply the user-approved review fixes (findings-r1 … r4 APPLY rows + user decisions of 2026-11-14) to the
pi-1 Russian plain RAILS translation (14 chapter files).

Each rule is a fixed old -> new string (a few regexes, rx=True) and touches a Russian line ONLY when
  - the aligned Pāli line (non-empty line i <-> non-empty line i) matches the rule's Pāli pattern (if given), and
  - the line belongs to one of the rule's segments (block IDs, if given), and to one of its parts (if given).
Line counts, block IDs, heading levels, variant brackets and dashes are never changed (asserted per changed line).

The 14 files are backed up once to backup-pre-fixes/ (only if that folder does not exist yet); every run reads
from the backup, so the script is rerunnable and idempotent. Log: fixes-log.tsv (file, line, rule, old, new).
Order after a rebuild of the rails builders: builders -> rails/fix_bare_comma_ru.py -> this script.

usage: python -I -X utf8 apply_review_fixes_ru.py [--dry]
"""
import collections, os, re, shutil, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
RDIR = os.path.join(ROOT, r"AI_translation\russian\pi-1-russian-plain-rails_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-1-ru\review")
BAK = os.path.join(HERE, "backup-pre-fixes")
LOG = os.path.join(HERE, "fixes-log.tsv")
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

R = []  # dict(rid, pali, old, new, rx, sids, parts)


def rule(rid, old, new, pali=None, rx=False, sids=None, parts=None, skip=None):
    """skip: a Russian-line regex; a line matching it is left alone by this rule."""
    R.append(dict(rid=rid, pali=re.compile(pali) if pali else None, old=re.compile(old) if rx else old, new=new,
                  rx=rx, sids=set(sids) if sids else None, parts=parts, skip=re.compile(skip) if skip else None))


# =================================================================== user decisions (2026-11-14), book-wide
# U1 sārāga family = «пристрастие» (rāga stays «страсть»)
rule("U1-saraga", "отсутствие проявления страсти", "отсутствие проявления пристрастия", pali=r"asārajjanā")
rule("U1-saraga", "отсутствие состояния страсти", "отсутствие состояния пристрастия", pali=r"asārajjitattaṃ")
rule("U1-saraga", "проявление страсти, состояние страсти", "проявление пристрастия, состояние пристрастия",
     pali=r"(?<!a)sārajjanā (?<!a)sārajjitattaṃ")

# U2 asantuṭṭhitā ca kusalesu dhammesu = «Ненасытность в благих явлениях»
rule("U2-asantutthita", "Отсутствие довольства благими явлениями", "Ненасытность в благих явлениях",
     pali=r"[Aa]santuṭṭhitā ca kusalesu dhammes")  # dhammesu / dhammesūti

# U3 bhāṇavāra = «часть для чтения вслух»
_ORDF = {"Первый": "Первая", "Второй": "Вторая", "Третий": "Третья", "Четвёртый": "Четвёртая", "Пятый": "Пятая",
         "Шестой": "Шестая", "Седьмой": "Седьмая", "Восьмой": "Восьмая"}
rule("U3-bhanavara", r"\b(" + "|".join(_ORDF) + r") раздел для чтения вслух",
     lambda m: _ORDF[m.group(1)] + " часть для чтения вслух", pali=r"bhāṇavār", rx=True)

# U4 matter-chapter classification by 2 … 11 = «на N вида / видов» (Ekakaṃ keeps «по одному»)
_NUM = {"два": "вида", "три": "вида", "четыре": "вида", "пять": "видов", "шесть": "видов", "семь": "видов",
        "восемь": "видов", "девять": "видов", "десять": "видов", "одиннадцать": "видов"}
rule("U4-classification", r"([Кк]лассификаци[яи](?: материальной формы)?) по (" + "|".join(_NUM) + r")(?![а-яё])",
     lambda m: f"{m.group(1)} на {m.group(2)} {_NUM[m.group(2)]}",
     pali=r"(?:v|bb)idhena rūpasaṅgaho|^(?:##### )?(?:Duk|Tik|Catukk|Pañcak|Chakk|Sattak|Aṭṭhak|Navak|Dasak|Ekādasak)"
          r"(?:aṃ|aniddeso)\b", rx=True, parts=["3-0"])

# U5 Rūpavibhatti = «Разбор материальной формы» (rūpasaṅgaha stays «классификация материальной формы»)
rule("U5-vibhatti", "Классификация материальной формы", "Разбор материальной формы", pali=r"^(?:#### )?Rūpavibhatti\b")

# U6 catūsu / tīsu bhūmīsu = «четырёх / трёх уровней» (the ch2 heading Tebhūmaka «… трёх миров» is not touched)
rule("U6-bhumi", r"(четырёх|трёх) миров\b", r"\1 уровней", pali=r"bhūmīsu", rx=True)

# =================================================================== book-wide consistency rules (with APPLY rows)
# G1 X-gataṃ after a noun = «то, что считается X» (r3 ^1-637 …)
rule("G1-gatam", r", считающееся ([а-яё]+)", r", то, что считается \1", pali=r"\w+gataṃ", rx=True, parts=["3-0"])

# G2 niyyānikaṃ apacayagāmiṃ = «ведущее к освобождению и к убыванию» (r2)
rule("G2-niyyanika", r"(ведущ[а-яё]+) к освобождению и \1 к убыванию", r"\1 к освобождению и к убыванию",
     pali=r"apacayagām", rx=True)

# G3 «X – это» without a comma after a plain noun phrase / list (r3 rows + the same lists in 2-01)
COMMA_DROP_R3 = ["1-658", "1-660", "1-662", "1-664", "1-668", "1-670", "1-746", "1-760", "1-763", "1-766", "1-772",
                 "1-775", "1-884", "1-885", "1-888", "1-889", "1-910", "1-912", "1-930", "1-932", "1-944", "1-951",
                 "1-954", "1-750", "1-945", "1-953", "1-956"]
COMMA_DROP_2_01 = ["1-66", "1-69", "1-119", "1-120", "1-122", "1-123", "1-124", "1-125", "1-126", "1-127", "1-128",
                   "1-129", "1-130", "1-131", "1-144", "1-145"]
rule("G3-comma-drop", ", – это", " – это", sids=COMMA_DROP_R3, parts=["3-0"])
# (the «какие бы другие … ни были в это время, – это» clause in the same segments keeps its comma)
rule("G3-comma-drop", ", – это", " – это", sids=COMMA_DROP_2_01, parts=["2-01"], skip=r"какие бы други")
# the «это X, …, это Y» chain keeps its comma: add it where it is missing (r3 ^1-700/817/983)
rule("G3-comma-add", "это элемент осязаемого – это", "это элемент осязаемого, – это", sids=["1-700", "1-817", "1-983"])

# G4 «какая бы другая материальная форма ни была (не) вследствие …» -> «… ни возникла (не) вследствие …» (r3)
rule("G4-nivoznikla", "ни была вследствие совершённых действий", "ни возникла вследствие совершённых действий",
     pali=r"kammassa katattā")
rule("G4-nivoznikla", "ни была не вследствие совершённых действий", "ни возникла не вследствие совершённых действий",
     pali=r"kammassa katattā")

# =================================================================== one-off APPLY rows
# r1 ^1-163 third-jhāna formula
rule("R1-163-ariya", "испытывает телом счастье, о котором благородные говорят – «",
     "испытывает телом счастье, так что благородные говорят о нём – «", pali=r"ariyā ācikkhanti")
# r2 ^1-443 bodily sukha
rule("R2-443-sukha", "осязательное сознание, сопровождаемое счастьем,", "осязательное сознание, сопровождаемое удовольствием,",
     pali=r"kāyaviññāṇaṃ uppannaṃ hoti sukhasahagataṃ", sids=["1-443"])
# r2 headings and closing lines (2-04, 2-05)
for _sids, _old, _new in [
    (["1-1-8-8-0", "1-537"], "Простое пустое с преобладанием желания", "Только пустое, с преобладанием желания"),
    (["1-1-8-2-0", "1-513"], "Простое пустое", "Только пустое"),
    (["1-1-8-4-0", "1-522"], "Простое свободное от устремлений", "Только свободное от устремлений"),
    (["1-1-8-3-0", "1-518"], "Пустое со способом практики", "Пустое в сочетании со способами практики"),
    (["1-1-8-5-0", "1-527"], "Свободное от устремлений со способом практики",
     "Свободное от устремлений в сочетании со способами практики"),
    (["1-1-6-0"], "Двенадцать неблагих видов ума", "Двенадцать видов неблагого ума"),
    (["1-1-9-0"], "Этически неопределённое, являющееся результатом неблагих действий",
     "Этически неопределённый результат неблагих действий"),
    (["1-1-10-0", "1-575"], "Этически неопределённое функциональное, не имеющее корней",
     "Этически неопределённый функциональный ум, не имеющий корней"),
    (["1-582"], "Этически неопределённое функциональное.", "Этически неопределённый функциональный ум."),
]:
    rule("R2-headings", _old, _new, sids=_sids, parts=["2-04", "2-05"])
# r4 ^1-1350, ^1-1344/1345, ^1-1485, ^1-1042/1045
rule("R4-1350-vaca", "говорит такой речью, которая", "произносит такую речь, которая", pali=r"tathārūpiṃ vācaṃ bhāsitā",
     sids=["1-1350"])
rule("R4-1344-thana", "то каждое такое является возможным", "то в каждом таком случае это возможное",
     pali=r"taṃ taṃ ṭhānanti", sids=["1-1344"])
rule("R4-1345-thana", "то каждое такое является невозможным", "то в каждом таком случае это невозможное",
     pali=r"taṃ taṃ aṭṭhānanti", sids=["1-1345"])
rule("R4-1485-samyojana", "двое или трое оков", "две или три оковы", pali=r"dve tīṇi saṃyojanāni", sids=["1-1485"])
rule("R4-1042-ajata",
     "не рождённые, не ставшие, не зародившиеся, не появившиеся, не появившиеся полностью, не проявившиеся, невозникшие, "
     "не возникшие полностью, не поднявшиеся, не поднявшиеся полностью",
     "нерождённые, неставшие, незародившиеся, непоявившиеся, не появившиеся полностью, непроявившиеся, невозникшие, "
     "не возникшие полностью, неподнявшиеся, не поднявшиеся полностью",
     pali=r"ajātā abhūtā asañjātā", sids=["1-1042", "1-1045"])


# ------------------------------------------------------------------------------------------------- engine
def dashes(t):
    return t.count("—") + t.count("–")


def backup():
    if os.path.isdir(BAK):
        missing = [p for p in PARTS if not os.path.exists(os.path.join(BAK, p + ".md"))]
        assert not missing, ("backup incomplete", missing)
        return False
    os.makedirs(BAK)
    for p in PARTS:
        shutil.copy2(os.path.join(RDIR, p + ".md"), os.path.join(BAK, p + ".md"))
    return True


def main(dry=False):
    made = backup()
    print("backup created:" if made else "backup exists, reading from:", BAK)
    log, tot, changed, hit = [], collections.Counter(), collections.Counter(), collections.Counter()
    bhumi_bad = []
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        text = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        assert "\r" not in text and not text.startswith("\ufeff"), part
        el = text.split("\n")
        idx = [i for i, l in enumerate(el) if l.strip()]
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        sid_of, cur = {}, []
        for k in range(len(pl)):
            cur.append(k)
            m = ID.search(pl[k])
            if m:
                for kk in cur:
                    sid_of[kk] = m.group(1)
                cur = []
        for k, li in enumerate(idx):
            p, e0 = pl[k], el[li]
            e = e0
            for ri, r in enumerate(R):
                if r["parts"] and not any(part.startswith(x) for x in r["parts"]):
                    continue
                if r["sids"] is not None and sid_of.get(k) not in r["sids"]:
                    continue
                if r["pali"] is not None and not r["pali"].search(p):
                    continue
                if r["skip"] is not None and r["skip"].search(e):
                    continue
                if r["rx"]:
                    e2, n = r["old"].subn(r["new"], e)
                else:
                    n = e.count(r["old"])
                    e2 = e.replace(r["old"], r["new"])
                if n and e2 != e:
                    hit[ri] += n
                    tot[r["rid"]] += n
                    log.append((part + ".md", li + 1, r["rid"], e, e2))
                    e = e2
            if "bhūmīsu" in p:
                np_ = len(re.findall(r"(?:[Cc]atūsu|[Tt]īsu) bhūmīsu", p))
                nr = len(re.findall(r"(?:четырёх|трёх) уровней", e))
                if np_ != nr:
                    bhumi_bad.append((part, sid_of.get(k), np_, nr))
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
        with open(LOG, "w", encoding="utf-8", newline="\n") as f:
            f.write("file\tline\trule\told\tnew\n")
            for fn, ln, rid, old, new in log:
                f.write(f"{fn}\t{ln}\t{rid}\t{old}\t{new}\n")
    for rid in sorted(tot):
        print(f"{rid:22s} {tot[rid]}")
    print("lines changed per part:", dict(changed), "total", sum(changed.values()))
    for ri, r in enumerate(R):
        if not hit[ri]:
            print("NO HIT:", r["rid"], "|", str(r["old"])[:90])
    if bhumi_bad:
        print("bhūmīsu count mismatch (pali, ru):", bhumi_bad)
    print("DRY RUN, nothing written" if dry else f"written; log: {LOG}")


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
