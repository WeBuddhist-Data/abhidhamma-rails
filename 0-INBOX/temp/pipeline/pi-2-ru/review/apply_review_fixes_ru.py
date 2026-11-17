"""Apply the approved review fixes (findings-r1 … r6, user decision "Apply all", 2026-11-17) to the
pi-2 Russian plain rails chapter files.

usage: python -I -X utf8 apply_review_fixes_ru.py [<chapter dir>]
  default <chapter dir>: AI_translation/russian/pi-2-russian-plain-rails_split_chapters

Exact string replacements, each with its expected count per file (asserted). A rule whose old string is
no longer present and whose new string is present the expected number of times counts as already applied,
so a re-run is a no-op. Every changed line is logged to review/fixes-log.tsv
(file, line, finding, before, after). Guards: line count, block IDs and the number of "–" per line
must not change.

Rebuild order: build_rails_*_ru.py → refresh review/backup-pre-fixes from the builder output →
this script on the chapter dir (see review/builders-stale.md).
"""
import pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
RU = ROOT / "AI_translation/russian/pi-2-russian-plain-rails_split_chapters"
LOG = ROOT / "0-INBOX/temp/pipeline/pi-2-ru/review/fixes-log.tsv"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

CH15_NEW = ("Знание высказывания выражений, относящихся к явлениям, в том выражении, которым обозначаются "
            "эти явления, является аналитическим знанием выражений.")
CH15_OLD = ("выражением обозначаются эти явления, при этом знание высказывания выражений, относящихся к явлениям, "
            "является аналитическим знанием выражений.")

# (finding, file, old, new, expected count in that file)
RULES = [
    # r1
    ("r1 2-173 silā", "3-dhatuvibhango.md", "раковина, кристалл, коралл", "раковина, скала, коралл", 1),
    ("r1 2-174 siṅghāṇikā", "3-dhatuvibhango.md", "слюна, сопли, суставная", "слюна, носовая слизь, суставная", 1),
    ("r1 2-174 siṅghāṇikā", "7-satipatthanavibhango.md", "слюна, сопли, суставная", "слюна, носовая слизь, суставная", 3),
    ("r1 2-182 sabbepi", "3-dhatuvibhango.md", "Все благие явления тоже являются «элементом отречения».",
     "Все благие явления являются «элементом отречения».", 1),
    # r2 (book-wide)
    ("r2 ellipsis+stop", "1-khandhavibhango.md", "….", "…", 111),
    ("r2 ellipsis+stop", "2-ayatanavibhango.md", "….", "…", 1),
    ("r2 ellipsis+stop", "6-paticcasamuppadavibhango.md", "….", "…", 2),
    ("r2 ellipsis+stop", "10-bojjhangavibhango.md", "….", "…", 1),
    ("r2 ellipsis+stop", "12-jhanavibhango.md", "….", "…", 1),
    # r3
    ("r3 dhammacchando (user)", "8-sammappadhanavibhango.md", "благое стремление к Учению", "благое желание как явление", 4),
    ("r3 dhammacchando (user)", "9-iddhipadavibhango.md", "благое стремление к Учению", "благое желание как явление", 3),
    ("r3 2-510 space", "12-jhanavibhango.md", "подаянии;монах", "подаянии; монах", 1),
    ("r3 2-434 iddhi", "9-iddhipadavibhango.md", "То, что у этих явлений есть сверхспособность, успех",
     "То, что есть сверхспособность этих явлений, успех", 8),
    ("r3 2-516 sikkhā", "12-jhanavibhango.md",
     "обучение монахов для монахов, обучение монахинь для монахинь, обучение мирян для мирян и обучение мирянок для мирянок",
     "обучение для монахов, обучение для монахинь, обучение для мирян и обучение для мирянок", 1),
    # r4
    ("r4 2-725…745 nirutti", "15-patisambhidavibhango.md", "смысла, каким " + CH15_OLD, "смысла. " + CH15_NEW, 1),
    ("r4 2-725…745 nirutti", "15-patisambhidavibhango.md", "Каким " + CH15_OLD, CH15_NEW, 20),
    ("r4 brahmacakkaṃ (user)", "16-nanavibhango.md", "приводит в движение колесо Брахмы",
     "приводит в движение высшее колесо", 12),
    ("r4 2-750 hetu", "15-patisambhidavibhango.md", "являются корнями и имеют корни, корнями и связаны с корнями",
     "являются корнями и имеют корни, являются корнями и связаны с корнями", 1),
    ("r4 2-767 viññeyyā", "16-nanavibhango.md",
     "Всякая мудрость познаваема тем или иным видом сознания, не познаваема тем или иным видом сознания.",
     "Всякая мудрость познаваема тем или иным видом сознания и не познаваема тем или иным видом сознания.", 1),
    # r5
    ("r5 2-909 order", "17-khuddakavatthuvibhango.md", "жажда видимых форм, жажда звуков, жажда запахов",
     "жажда звуков, жажда видимых форм, жажда запахов", 1),
    ("r5 2-844 iriyāpatha", "17-khuddakavatthuvibhango.md", "из-за положения тела…", "из-за манеры держаться…", 1),
    ("r5 2-844 vaṇṇa", "17-khuddakavatthuvibhango.md", "из-за красоты…", "из-за внешности…", 1),
    ("r5 2-948 view", "17-khuddakavatthuvibhango.md",
     "», или же у него как истинное и достоверное возникает воззрение. Таковы шесть воззрений.",
     "», или же у него как истинное и достоверное возникает это воззрение. Таковы шесть воззрений.", 1),
    ("r5 2-958/959 spelling", "17-khuddakavatthuvibhango.md", "неповреждённа»", "неповреждена»", 13),
    ("r5 2-U10 idhekacco", "17-khuddakavatthuvibhango.md", "Здесь некий человек мучает существ",
     "Вот человек мучает существ", 1),
    ("r5 2-U10 idhekacco", "3-dhatuvibhango.md", "Здесь некий человек мучает существ",
     "Вот человек мучает существ", 1),
    ("r5 2-861 kuhanā", "17-khuddakavatthuvibhango.md",
     "или в манере держаться выставление [вариант написания (Ka.): āṭhapanā],",
     "или выставление напоказ манеры держаться [вариант написания (Ka.): āṭhapanā],", 1),
    ("r5 2-934 ariyā", "17-khuddakavatthuvibhango.md", "Что такое здесь благородные?", "Кто такие здесь благородные?", 1),
    ("r5 2-934 ariyā", "12-jhanavibhango.md", "что такое здесь благородные?", "кто такие здесь благородные?", 1),
    # r6
    ("r6 2-1023 ratti", "18-dhammahadayavibhango.md", "Тридцать таких ночей составляют месяц.",
     "Тридцать таких суток составляют месяц.", 6),
    ("r6 2-1029 line 1", "18-dhammahadayavibhango.md",
     "Вознесённые силой заслуг, ушедшие в удел мира чувственных желаний и мира форм,",
     "Вознесённые силой заслуг, они уходят в удел мира чувственных желаний и мира форм.", 1),
    ("r6 2-1029 line 2", "18-dhammahadayavibhango.md",
     "Достигшие даже вершины существования [вариант чтения (Syā.): bhavaggaṃ vāpi], вновь приходят",
     "Достигшие даже вершины существования [вариант чтения (Syā.): bhavaggaṃ vāpi] вновь приходят", 1),
]


def ids(lines):
    return [m.group(1) for m in (ID.search(l) for l in lines) if m]


def main():
    target = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else RU
    log, applied, skipped = [], 0, 0
    files = sorted({f for _, f, _, _, _ in RULES})
    for fname in files:
        p = target / fname
        text = p.read_text(encoding="utf-8")
        assert "\r" not in text, fname
        orig_lines = text.split("\n")
        for finding, f, old, new, exp in RULES:
            if f != fname:
                continue
            assert old not in new, (finding, "new contains old: not idempotent")
            n_old = text.count(old)
            if n_old == 0 and text.count(new) >= exp:
                skipped += 1
                continue
            assert n_old == exp, f"{fname} | {finding}: expected {exp}, found {n_old} of «{old}»"
            before = text.split("\n")
            text = text.replace(old, new)
            after = text.split("\n")
            assert len(before) == len(after), (fname, finding, "line count changed")
            for k, (a, b) in enumerate(zip(before, after), 1):
                if a != b:
                    log.append((fname, str(k), finding, a, b))
            applied += 1
        new_lines = text.split("\n")
        assert len(new_lines) == len(orig_lines), (fname, "line count changed")
        assert ids(new_lines) == ids(orig_lines), (fname, "block IDs changed")
        for k, (a, b) in enumerate(zip(orig_lines, new_lines), 1):
            assert a.count("–") == b.count("–"), (fname, k, "dash count changed")
            assert re.findall(r"\[[^\]]*\]", a) == re.findall(r"\[[^\]]*\]", b), (fname, k, "variant bracket changed")
        if text != "\n".join(orig_lines):
            p.write_text(text, encoding="utf-8", newline="\n")
    if log:
        with LOG.open("w", encoding="utf-8", newline="\n") as fh:
            fh.write("file\tline\tfinding\tbefore\tafter\n")
            for row in log:
                fh.write("\t".join(c.replace("\t", " ") for c in row) + "\n")
    print(f"rules applied: {applied}, already applied: {skipped}, changed line entries: {len(log)}"
          + (f" (log: {LOG})" if log else " (log untouched)"))


if __name__ == "__main__":
    main()
