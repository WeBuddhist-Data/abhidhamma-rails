"""Apply the user-approved review fixes (review-summary.md section A, user decisions of 2026-11-28 in
fix-brief.md) to the pi-6 Russian rails chapters.

Every rule is Pāli-anchored and counted per file. A rule is applied only when its count of old matches
(plus the matches already fixed) equals the expected count; a rule whose new text is already fully in place is
skipped, so the script is idempotent. Any count mismatch stops the run before anything is written.
Changed files are first copied to review\\backup-pre-fixes\\ (never overwritten once there); every change is
appended to review\\fixes-log.tsv (file, line, rule, old, new).

usage: python -I -X utf8 -B apply_review_fixes_ru.py [--dry] [--verbose]
       python -I -X utf8 -B apply_review_fixes_ru.py --report          (read-only scans of same-shape Pāli elsewhere)
       python -I -X utf8 -B apply_review_fixes_ru.py --show <regex> [--max N]   (inspection only)
"""
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / "AI_translation/pali/pi-6_split_chapters"
RDIR = ROOT / "AI_translation/russian/pi-6-russian-plain-rails_split_chapters"
HERE = ROOT / "0-INBOX/temp/pipeline/pi-6-ru/review"
BACKUP = HERE / "backup-pre-fixes"
LOG = HERE / "fixes-log.tsv"

# a sentence ends at «.» / «?» before a capital or «(»; sigla such as «(sī. syā.)» and «? …Pe…» do not split
SPLIT = re.compile(r"(?<=[.?])(\s+)(?=[A-ZĀĪŪṬḌṆÑṄА-ЯЁ(])")


def pairs(name):
    praw = (PDIR / name).read_text(encoding="utf-8").split("\n")
    rraw = (RDIR / name).read_text(encoding="utf-8").split("\n")
    pidx = [i for i, l in enumerate(praw) if l.strip()]
    ridx = [i for i, l in enumerate(rraw) if l.strip()]
    assert len(pidx) == len(ridx), name
    return praw, rraw, list(zip(pidx, ridx))


def sents(s):
    """[sentence, sep, sentence, …] so that ''.join() gives s back."""
    return SPLIT.split(s)


# ----------------------------------------------------------------------------------------------------------------
# Rules. Each: id, row, files {chapter stem prefix: expected count}, level 'line' | 'sent',
#   pali: regex the Pāli line / paired Pāli sentence must match,
#   old: regex on the Russian line / sentence, new: replacement (str or function of the match),
#   done: regex that matches the fixed text (for idempotency), check: optional f(pali, match) -> bool.
# ----------------------------------------------------------------------------------------------------------------
RULES = []


def rule(**kw):
    kw.setdefault("level", "line")
    kw.setdefault("check", None)
    RULES.append(kw)


# A1 ch. 8 past-time questions: the second half belongs to the question; every word kept.
A1_PI = re.compile(r"khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ, (na )?(nirujjhamānaṃ|uppajjamānaṃ) khaṇaṃ khaṇaṃ "
                   r"vītikkantaṃ atikkantakālaṃ (?:tassa taṃ|tassa|taṃ) citta(?:ṃ|nti)\?")


def a1_check(p, m):
    pm = A1_PI.search(p)
    neg_ok = bool(pm.group(1)) == m.group(1).startswith("не ")
    kind_ok = ("прекращения" in m.group(1)) == (pm.group(2) == "nirujjhamānaṃ")
    head = m.group(2)
    head_ok = {"у того тот ум": "tassa taṃ citta", "у того ум": "tassa citta", "тот ум": " taṃ citta"}[head] in p
    return neg_ok and kind_ok and head_ok


rule(id="A1", row="A1", files={"8-cittayamaka": 20}, pali=A1_PI.pattern,
     old=r", ((?:не )?миновал момент (?:возникновения|прекращения), этот момент, и время его (?:не )?прошло), "
         r"(у того тот ум|у того ум|тот ум) таков\?",
     new=r", \2 \1?",
     done=r", (?:у того тот ум|у того ум|тот ум) (?:не )?миновал момент (?:возникновения|прекращения), этот момент, "
          r"и время его (?:не )?прошло\?",
     check=a1_check)

# A2 ch. 8: the moment and the persons are separate cases.
rule(id="A2", row="A2", level="sent", files={"8-cittayamaka": 8},
     pali=r"^Cittassa (?:bhaṅga|uppāda)kkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ",
     old=r"^В момент (распада|возникновения) ума, у вошедших",
     new=r"В момент \1 ума, а также у вошедших",
     done=r"^В момент (?:распада|возникновения) ума, а также у вошедших",
     check=lambda p, m: (m.group(1) == "распада") == p.startswith("Cittassa bhaṅga"))

# A3 6-01 (and the same Pāli formulas in 6-02) editorial notes aligned with 5-01 / 5-02.
rule(id="A3a", row="A3", files={"6-01": 2, "6-02": 2}, pali=r"(?i)yassakampi yassayatthakampi sadisaṃ[.,)]",
     old=r"тоже такие же", new="тоже одинаковы", done=r"тоже одинаковы")
rule(id="A3b", row="A3", files={"6-01": 2, "6-02": 1}, pali=r"sadisaṃ vitthāretabb",
     old=r"следует развернуть так же", new="следует подробно изложить так же",
     done=r"следует подробно изложить так же")
rule(id="A3c", row="A3", files={"6-01": 1}, pali=r"nirodhasamāpannānanti na kātabbaṃ",
     old=r"использовать не следует", new="приводить не следует", done=r"приводить не следует")
rule(id="A3d", row="A3", files={"6-01": 1, "6-02": 1}, pali=r"natthi nānākaraṇaṃ",
     old=r"различий нет", new="различия нет", done=r"различия нет")


# A4 listed subjects take a plural verb (sentence-initial subject lists of the naming sections).
def plural_subject(new_subj):
    return lambda m: new_subj + m.group(1).replace("является", "являются")


for rid, pal, subj, new_subj, files in [
    ("A4a", r"^Dibbacakkhu paññācakkhu ", "Божественный глаз, глаз мудрости", "Божественный глаз и глаз мудрости",
     {"3-01": 4, "4-dhatu": 4, "10-01": 23}),
    ("A4b", r"^Dibbasotaṃ taṇhāsotaṃ ", "Божественное ухо, поток жажды", "Божественное ухо и поток жажды",
     {"3-01": 2, "4-dhatu": 2, "10-01": 4}),
    ("A4c", r"^Sīlagandho samādhigandho paññāgandho ", "Запах нравственности, запах сосредоточения, запах мудрости",
     "Запах нравственности, запах сосредоточения и запах мудрости", {"3-01": 2, "4-dhatu": 2}),
    ("A4d", r"^Attharaso dhammaraso vimuttiraso ", "Вкус смысла, вкус Учения, вкус освобождения",
     "Вкус смысла, вкус Учения и вкус освобождения", {"3-01": 2, "4-dhatu": 2}),
    ("A4e", r"^Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ dukkhañceva dukkhasaccañca", "Телесная боль, душевная боль",
     "Телесная боль, душевная боль", {"5-01": 1}),
]:
    rule(id=rid, row="A4", level="sent", files=files, pali=pal,
         old="^" + re.escape(subj) + r"( (?:не )?(?:и )?является .*)$", new=plural_subject(new_subj),
         done="^" + re.escape(new_subj) + r" (?:не )?(?:и )?являются ")

rule(id="A4f", row="A4", level="sent", files={"2-01": 6}, pali=r"^Piyarūpaṃ sātarūpaṃ ",
     old=r"^Привлекательная форма, отрадная форма ", new="Привлекательная, отрадная форма ",
     done=r"^Привлекательная, отрадная форма ")

# A5 «у них» where the Pāli has tesaṃ before the ca … ca pair after a moment / person phrase.
A5_PAIR = re.compile(r"(?P<pre>[^\s]+) (?P<pair>и (?:не )?(?:возник|прекра)[а-яё]*\b[^.?]*?, и (?:не )?(?:возник|прекра)[а-яё]*)")
A5_PI = re.compile(r"kkhaṇe\b.*\btesaṃ (?!tattha\b)(?:\S+ )?\S+?(?:ñca|ñceva| ca| ceva)\b")


def a5_find(r):
    """The first «и …, и …» verb pair after a moment phrase, not set off already (там / у них / у него) and not
    after a relative clause closed by a comma. Returns the insertion index or None."""
    for m in A5_PAIR.finditer(r):
        pre = m.group("pre")
        before = r[:m.start("pair")]
        if pre in ("там", "них", "него", "ней"):
            return None
        if not re.search(r"[Вв] момент|[Вв] течение жизни", before):
            continue
        if pre.endswith(","):
            # only the comma that closes a participle phrase «ума, (не) связанного с …,» (10-08 / 10-09 type)
            if not re.search(r"ума, (?:не )?связанного [^,]+, $", before):
                return None
        return m.start("pair")
    return None


A5_FILES = {"6-02": 7, "9-01": 3, "9-02": 9, "9-03": 3, "10-08": 9, "10-09": 16,
            # extension, user decision 2026-11-28 (second round): the same shape in the chapters left out first
            "5-01": 19, "5-02": 27, "5-03": 10, "10-02": 18, "10-10": 6, "6-01": 7}


def a5_apply(r, p):
    i = a5_find(r)
    if i is None or not A5_PI.search(p):
        return None
    return r[:i] + "у них " + r[i:]


A5_DONE = re.compile(r"(?:[Вв] момент|[Вв] течение жизни)[^.?]*? у них (?:и (?:не )?(?:возник|прекра)[а-яё]*\b[^.?]*?, и (?:не )?(?:возник|прекра))")

# A6 small wording.
rule(id="A6a", row="A6", files={"8-cittayamaka": 5}, pali=r"no ca", old=r"эти умы", new="они",
     done=r"(?:но|у него) они прекратятся")
rule(id="A6b", row="A6", files={"8-cittayamaka": 2}, pali=r"Suttantacittamissakaviseso",
     old=r"Особенность ума из наставлений в смешении", new="Особый случай: смешение с видами ума из наставлений",
     done=r"Особый случай: смешение с видами ума из наставлений")
rule(id="A6c", row="A6", files={"8-cittayamaka": 2}, pali=r"Abhidhammacittamissakaviseso",
     old=r"Особенность ума из Абхидхаммы в смешении", new="Особый случай: смешение с видами ума из Абхидхаммы",
     done=r"Особый случай: смешение с видами ума из Абхидхаммы")
rule(id="A6d", row="A6", files={"7-11": 4}, pali=r"kāmadhātuṃyeva upapajjati, satteva anusayā anusenti",
     old=r"(он перерождается только в мире чувственных желаний), (залегают именно семь)", new=r"\1, у него \2",
     done=r"он перерождается только в мире чувственных желаний, у него залегают именно семь")
rule(id="A6e", row="A6", files={"7-05": 1},
     pali=r"vicikicchānusayañca diṭṭhānusayañca pajahati kāmarāgānusayañca mānānusayañca tadekaṭṭhaṃ pajahati",
     old=r"там и устраняет (скрытые склонности к колебанию и к воззрениям), и устраняет (скрытые склонности к "
         r"чувственной страсти и к самомнению, пребывающие вместе с ними)",
     new=r"там устраняет \1, устраняет \2",
     done=r"в двух видах чувства там устраняет скрытые склонности к колебанию и к воззрениям, устраняет скрытые "
          r"склонности к чувственной страсти и к самомнению, пребывающие вместе с ними")
# «остальное X является X» where the Pāli has the noun (avaseso kāyo, avasesā upekkhā …): sentence level.
for rid, pal, noun_ru, files in [
    ("A6f", r"ṭhapetvā avaseso kāyo\b", "остальное тело", {"3-01": 1, "4-dhatu": 1, "10-01": 3}),
    ("A6g", r"ṭhapetvā avasesā upekkhā\b", "остальная невозмутимость", {"10-01": 3}),
]:
    rule(id=rid, row="A6", level="sent", files=files, pali=pal,
         old=r"^(Кроме [^,]+, )остальное является ", new=r"\1" + noun_ru + " является ",
         done=r"^Кроме [^,]+, " + noun_ru + " является ")
# User decision 2026-11-28 (second round): the extra A6h … A6m cases (dhammo, mano, samudayo / nirodho / maggo,
# saṅkhārā) were not approved. The rules are withdrawn; these revert rules restore the earlier Russian where a
# first run had applied them (on pristine text they find nothing to do and are skipped).
for rid, pal, noun_ru, files in [
    ("R-A6h", r"ṭhapetvā avaseso dhammo\b", "остальное явление", {"3-01": 3, "4-dhatu": 1}),
    ("R-A6i", r"ṭhapetvā avaseso mano\b", "остальной ум", {"4-dhatu": 1}),
    ("R-A6j", r"ṭhapetvā avaseso samudayo\b", "остальное возникновение", {"5-01": 2}),
    ("R-A6k", r"ṭhapetvā avaseso nirodho\b", "остальное прекращение", {"5-01": 2}),
    ("R-A6l", r"ṭhapetvā avaseso maggo\b", "остальной путь", {"5-01": 2}),
]:
    rule(id=rid, row="A6-revert", level="sent", files=files, pali=pal,
         old=r"^(Кроме [^,]+, )" + noun_ru + " является ", new=r"\1остальное является ",
         done=r"^Кроме [^,]+, остальное является ")
rule(id="R-A6m", row="A6-revert", level="sent", files={"2-01": 5}, pali=r"ṭhapetvā avasesā saṅkhārā\b",
     old=r"^(Кроме совокупности формирующих факторов, )остальные формирующие факторы являются ",
     new=r"\1остальные являются ",
     done=r"^Кроме совокупности формирующих факторов, остальные являются ")
rule(id="A6n", row="A6", files={"5-01": 2}, pali=r"Avasese catuvokāre pañcavokāre",
     old=r"В остальном существовании с четырьмя составляющими и с пятью составляющими",
     new="В остальном существовании с четырьмя составляющими и в существовании с пятью составляющими",
     done=r"В остальном существовании с четырьмя составляющими и в существовании с пятью составляющими")
rule(id="A6o", row="A6", files={"1-mulayamaka": 2}, pali=r"Hetuvārādi",
     old=r"Раздел о причинах и другие", new="Раздел о причинах и следующие разделы",
     done=r"Раздел о причинах и следующие разделы")
rule(id="A6p", row="A6", files={"1-mulayamaka": 8}, pali=r"\) Mūlakanayo",
     old=r"Метод основания на корне(?= \^)", new="Метод опоры на корень", done=r"Метод опоры на корень(?= \^)")
rule(id="A6q", row="A6", files={"1-mulayamaka": 8}, pali=r"\) Mūlamūlakanayo",
     old=r"Метод основания на корне корней", new="Метод опоры на корень корней",
     done=r"Метод опоры на корень корней")


# ----------------------------------------------------------------------------------------------------------------
def chapter_files():
    return sorted(p.name for p in PDIR.glob("*.md"))


def file_for(prefix):
    hits = [n for n in chapter_files() if n.startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]


def units(praw, rraw, pr, level):
    """Yield (ri, sentence index or None, pali text, russian text) for each line or aligned sentence."""
    for pi, ri in pr:
        if level == "line":
            yield ri, None, praw[pi], rraw[ri]
        else:
            ps, rs = sents(praw[pi]), sents(rraw[ri])
            if len(ps) != len(rs):
                yield ri, "UNALIGNED", praw[pi], rraw[ri]
                continue
            for k in range(0, len(rs), 2):
                yield ri, k, ps[k], rs[k]


def run_rule(rl, name, praw, rraw, pr, changes, errors, verbose):
    old, done, pal = re.compile(rl["old"]), re.compile(rl["done"]), re.compile(rl["pali"])
    exp = rl["files"][next(k for k in rl["files"] if name.startswith(k))]
    n_old = n_done = 0
    todo = []
    for ri, k, p, r in units(praw, rraw, pr, rl["level"]):
        if k == "UNALIGNED":
            if old.search(r) and pal.search(p):
                errors.append(f"{rl['id']} {name}:{ri + 1} sentence counts differ; matched only at line level")
            continue
        if not pal.search(p):
            continue
        ms = list(old.finditer(r))
        n_done += len(done.findall(r))
        for m in ms:
            if rl["check"] and not rl["check"](p, m):
                errors.append(f"{rl['id']} {name}:{ri + 1} Pāli check failed: {m.group(0)[:80]}")
        n_old += len(ms)
        if ms:
            todo.append((ri, k))
    if n_old == 0 and n_done == exp:
        return "skipped (already applied)"
    if n_old + n_done != exp:
        errors.append(f"{rl['id']} {name}: expected {exp}, found old {n_old} + done {n_done}")
        return "ERROR"
    for ri, k in todo:
        before = rraw[ri]
        if k is None:
            rraw[ri] = old.sub(rl["new"], before) if not callable(rl["new"]) else old.sub(rl["new"], before)
        else:
            rs = sents(before)
            rs[k] = old.sub(rl["new"], rs[k])
            rraw[ri] = "".join(rs)
        changes.append((name, ri + 1, rl["id"], before, rraw[ri]))
        if verbose:
            print(f"  {rl['id']} {name}:{ri + 1}")
    return f"applied {n_old}" + (f" (+{n_done} already)" if n_done else "")


def run_a5(name, praw, rraw, pr, changes, errors, verbose):
    exp = A5_FILES[next(k for k in A5_FILES if name.startswith(k))]
    n_new = n_done = 0
    todo = []
    for pi, ri in pr:
        ps, rs = sents(praw[pi]), sents(rraw[ri])
        if len(ps) != len(rs):
            if a5_find(rraw[ri]) is not None:
                errors.append(f"A5 {name}:{ri + 1} sentence counts differ")
            continue
        for k in range(0, len(rs), 2):
            if A5_PI.search(ps[k]) and A5_DONE.search(rs[k]):
                n_done += 1
                continue
            new = a5_apply(rs[k], ps[k])
            if new is not None:
                n_new += 1
                todo.append((ri, k, new))
    if n_new == 0 and n_done >= exp:
        return "skipped (already applied)"
    if n_new != exp:
        errors.append(f"A5 {name}: expected {exp}, found {n_new} (already {n_done})")
        return "ERROR"
    for ri, k, new in todo:
        before = rraw[ri]
        rs = sents(before)
        rs[k] = new
        rraw[ri] = "".join(rs)
        changes.append((name, ri + 1, "A5", before, rraw[ri]))
        if verbose:
            print(f"  A5 {name}:{ri + 1}\n    {new}")
    return f"applied {n_new}"


def main(dry, verbose):
    data, changes, errors, status = {}, [], [], []
    names = set()
    for rl in RULES:
        for pre in rl["files"]:
            names.add(file_for(pre))
    for pre in A5_FILES:
        names.add(file_for(pre))
    for name in sorted(names):
        data[name] = pairs(name)
    for rl in RULES:
        for pre in rl["files"]:
            name = file_for(pre)
            praw, rraw, pr = data[name]
            status.append((rl["id"], name, run_rule(rl, name, praw, rraw, pr, changes, errors, verbose)))
    for pre in A5_FILES:
        name = file_for(pre)
        praw, rraw, pr = data[name]
        status.append(("A5", name, run_a5(name, praw, rraw, pr, changes, errors, verbose)))
    for s in status:
        print(f"{s[0]:5} {s[1]:30} {s[2]}")
    if errors:
        print("ERRORS (nothing written):")
        for e in errors:
            print("  ", e)
        return 1
    # sanity: line counts and block ids unchanged
    for name in names:
        praw, rraw, pr = data[name]
        orig = (RDIR / name).read_text(encoding="utf-8").split("\n")
        assert len(orig) == len(rraw), name
        for a, b in zip(orig, rraw):
            ida, idb = re.findall(r"\^[0-9A-Za-z-]+\s*$", a), re.findall(r"\^[0-9A-Za-z-]+\s*$", b)
            assert ida == idb, (name, a[:60])
            assert bool(a.strip()) == bool(b.strip()), name
    changed = sorted({c[0] for c in changes})
    print(f"changes: {len(changes)} in {len(changed)} files")
    if dry or not changes:
        return 0
    BACKUP.mkdir(exist_ok=True)
    for name in changed:
        dst = BACKUP / name
        if not dst.exists():
            shutil.copyfile(RDIR / name, dst)
    for name in changed:
        with open(RDIR / name, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(data[name][1]))
    new_log = not LOG.exists()
    with open(LOG, "a", encoding="utf-8", newline="\n") as f:
        if new_log:
            f.write("file\tline\trule\told\tnew\n")
        for c in changes:
            f.write("\t".join(str(x).replace("\t", " ") for x in c) + "\n")
    print(f"written; backup in {BACKUP}; log {LOG}")
    return 0


def report():
    """Read-only: the same Pāli shapes outside the fixed chapters, left unchanged."""
    shapes = {
        "A2 moment directly followed by nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ (not ch. 8)":
            (re.compile(r"kkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ"), None, "8-"),
        "A3 vitthāretabbaṃ «следует развернуть» outside 6-0x":
            (re.compile(r"vitthāretabb"), re.compile(r"развернуть"), "6-"),
        "A5 tesaṃ pair after a moment phrase, other chapters":
            (A5_PI, "A5", tuple(A5_FILES)),
        "A6e parallel of ^6-7-162 (там и …, и …)":
            (re.compile(r"diṭṭhānusayañca (?:pajah|parijān)\S+ kāmarāgānusayañca mānānusayañca tadekaṭṭhaṃ"),
             re.compile(r"там и (?:устраняет|полностью понимает) скрытые склонности к колебанию и к воззрениям, и "), "7-05"),
    }
    for label, (pal, ru, skip) in shapes.items():
        tally = {}
        for name in chapter_files():
            if name.startswith(skip):
                continue
            praw, rraw, pr = pairs(name)
            for pi, ri in pr:
                if ru == "A5":
                    ps, rs = sents(praw[pi]), sents(rraw[ri])
                    if len(ps) != len(rs):
                        continue
                    n = sum(1 for k in range(0, len(rs), 2) if a5_apply(rs[k], ps[k]) is not None)
                else:
                    n = len(pal.findall(praw[pi])) if ru is None or ru.search(rraw[ri]) else 0
                    if ru is not None and not pal.search(praw[pi]):
                        n = 0
                if n:
                    tally.setdefault(name[:-3], []).append(f"{ri + 1}")
        print(label)
        for k, v in tally.items():
            print(f"   {k}: {len(v)} lines ({', '.join(v[:12])}{' …' if len(v) > 12 else ''})")


def show(pat, mx):
    rx = re.compile(pat)
    n = 0
    for name in chapter_files():
        praw, rraw, pr = pairs(name)
        for pi, ri in pr:
            if rx.search(rraw[ri]) or rx.search(praw[pi]):
                n += 1
                if n <= mx:
                    print(f"[{name[:-3]}:{ri + 1}]\n  PI: {praw[pi]}\n  RU: {rraw[ri]}")
    print("matches:", n)


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--typo" in a:  # checks on the changed files: «ли», Latin outside brackets, double blank lines, CR, em dash
        for name in sorted(p.name for p in BACKUP.glob("*.md")):
            raw = (RDIR / name).read_bytes().decode("utf-8")
            bad = []
            if "\r" in raw:
                bad.append("CR")
            if "\n\n\n" in raw:
                bad.append("double blank line")
            for i, ln in enumerate(raw.split("\n"), 1):
                if re.search(r"(?<![а-яё])ли(?![а-яё])", ln, re.I):
                    bad.append(f"{i}: «ли»")
                if "—" in ln:
                    bad.append(f"{i}: em dash")
                outside = re.sub(r"\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
                if re.search(r"[A-Za-zĀāĪīŪūṃṅñṭḍṇḷ]", outside):
                    bad.append(f"{i}: Latin outside brackets")
            print(f"{name:30} {'OK' if not bad else bad[:8]}")
    elif "--a5" in a:  # inspection: A5 candidates (pair after a moment phrase) in one chapter, with their status
        name = file_for(a[a.index("--a5") + 1])
        praw, rraw, pr = pairs(name)
        for pi, ri in pr:
            ps, rs = sents(praw[pi]), sents(rraw[ri])
            for k in range(0, len(rs), 2):
                m = A5_PAIR.search(rs[k])
                if m and re.search(r"[Вв] момент|[Вв] течение жизни", rs[k][:m.start("pair")]):
                    print(f"{ri + 1} aligned={len(ps) == len(rs)} pi={bool(A5_PI.search(ps[k] if len(ps) == len(rs) else praw[pi]))}"
                          f" find={a5_find(rs[k])} pre={m.group('pre')}")
    elif "--show" in a:
        show(a[a.index("--show") + 1], int(a[a.index("--max") + 1]) if "--max" in a else 30)
    elif "--report" in a:
        report()
    else:
        sys.exit(main("--dry" in a, "--verbose" in a))
