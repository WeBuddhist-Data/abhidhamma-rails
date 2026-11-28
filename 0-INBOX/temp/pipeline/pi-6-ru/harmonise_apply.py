"""Harmonise pass for the pi-6 Russian zero-shot (coordinator, 2026-11-27). Applied to the chapter outputs AFTER
the chapter builders; re-run it whenever a builder is re-run. Idempotent: an edit whose new text is already in
place is skipped.

usage: python -I -X utf8 -B harmonise_apply.py [--dry]

Edits:
1. Punctuation repairs undone (user rule: a wrong mark stays as written):
   ^6-2-36 «?» back to «.»; ^6-5-130 «?» back to «.»; ^6-3-148 full stop back to the Pāli comma;
   ^6-2-151 stray comma restored.
2. atītā / anāgatā / paccuppannātītā / atītānāgatā pucchā = «вопросы о …» (plural) everywhere
   (5-02, 5-03, 6-01, 6-02 had it; 3-04 … 3-06 had the singular).
3. uppāde / nirodhe (in the editorial notes) = «в разделе о возникновении / прекращении», as 3-04, 3-05, 3-06
   (5-02 had «при возникновении / прекращении»).
4. ^6-10-385: plural verb with a singular subject rendered as meant («не возникнет»), as 10-13 does
   (^6-10-454, -459, -468); number agreement does not change the meaning.
5. "…" for "…pe…" after a word takes no space (pi-1 … pi-5 convention; 10-01, 10-02 and a few others had
   «Да …», «сфера носа …»). After «?» or «.» the space stays.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / "AI_translation/pali/pi-6_split_chapters"
RDIR = ROOT / "AI_translation/russian/pi-6-russian-plain-zeroshot_split_chapters"

# (file, Pāli line it must sit on or None, old, new, expected count of old in the file / on the line)
EDITS = [
    ("2-01-khandhayamaka.md", "(Ka) na saṅkhārā na saṅkhārakkhandhoti. Āmantā.",
     "формирующих факторов? Да.", "формирующих факторов. Да.", 1),
    ("5-02-saccayamaka.md",
     "(Kha) yassa vā pana yattha maggasaccaṃ nirujjhissati tassa tattha samudayasaccaṃ nirujjhitthāti.",
     "прекращалась истина о возникновении?", "прекращалась истина о возникновении.", 1),
    ("3-04-ayatanayamaka.md", None,
     "но у них там прекратится сфера ума. У тех, кто достигает окончательного угасания, и у существ без восприятия там не прекратится ни сфера носа, ни сфера ума.",
     "но у них там прекратится сфера ума, у тех, кто достигает окончательного угасания, и у существ без восприятия там не прекратится ни сфера носа, ни сфера ума.", 1),
    ("2-02-khandhayamaka.md", None,
     "там не прекращалась совокупность материальной формы и не прекратится совокупность чувств.",
     "там не прекращалась совокупность материальной формы, и не прекратится совокупность чувств.", 1),
    # 2. вопросы (plural)
    ("3-04-ayatanayamaka.md", None,
     "вопрос о прошлом одинаков и в утвердительной",
     "вопросы о прошлом одинаковы и в утвердительной", 1),
    ("3-04-ayatanayamaka.md", None,
     "развёрнут вопрос о будущем в разделе с «у кого где», так же его следует развернуть",
     "развёрнуты вопросы о будущем в разделе с «у кого где», так же их следует развернуть", 1),
    ("3-05-ayatanayamaka.md", None,
     "(Вопрос о прошлом в разделе о возникновении, в разделе о прекращении и в разделе о возникновении и прекращении одинаков и",
     "(Вопросы о прошлом в разделе о возникновении, в разделе о прекращении и в разделе о возникновении и прекращении одинаковы и", 1),
    ("3-06-ayatanayamaka.md", None,
     "разобран вопрос о настоящем и прошлом, так же и в разделе о возникновении и прекращении вопрос о настоящем и прошлом следует",
     "разобраны вопросы о настоящем и прошлом, так же и в разделе о возникновении и прекращении вопросы о настоящем и прошлом следует", 1),
    ("3-06-ayatanayamaka.md", None,
     "(Как в разделе о прекращении вопрос о прошлом и будущем [вариант чтения (Syā.): atītenānāgatā] разобран и",
     "(Как в разделе о прекращении вопросы о прошлом и будущем [вариант чтения (Syā.): atītenānāgatā] разобраны и", 1),
    ("3-06-ayatanayamaka.md", None,
     "следует разбирать вопрос о прошлом и будущем.)",
     "следует разбирать вопросы о прошлом и будущем.)", 1),
    # 3. в разделе о …
    ("5-02-saccayamaka.md", None,
     "(Раздел с «где» одинаков и при возникновении, и при прекращении, и при возникновении и прекращении, различия нет).",
     "(Раздел с «где» одинаков и в разделе о возникновении, и в разделе о прекращении, и в разделе о возникновении и прекращении, различия нет).", 1),
    ("5-02-saccayamaka.md", None,
     "так же следует разбирать и при прекращении, различия нет).",
     "так же следует разбирать и в разделе о прекращении, различия нет).", 1),
    # 4. number agreement as meant
    ("10-10-indriyayamaka.md", None,
     "не возникнут способность женственности, но у них возникает способность глаза.",
     "не возникнет способность женственности, но у них возникает способность глаза.", 1),
]

ELLIPSIS = re.compile(r"(?<=[0-9A-Za-zА-Яа-яЁё»)\]]) …")


def lines_nonempty_index(text):
    return [i for i, ln in enumerate(text.split("\n")) if ln.strip()]


def main():
    dry = "--dry" in sys.argv
    changed = {}
    for fname, pali, old, new, n in EDITS:
        rf = RDIR / fname
        text = changed.get(fname) or rf.read_text(encoding="utf-8")
        if pali is None:
            c = text.count(old)
            if c == 0 and new in text:
                print("already:", fname, new[:60]); continue
            assert c == n, (fname, old[:60], c)
            text = text.replace(old, new)
        else:
            praw = (PDIR / fname).read_text(encoding="utf-8").split("\n")
            rraw = text.split("\n")
            pidx, ridx = lines_nonempty_index("\n".join(praw)), lines_nonempty_index(text)
            assert len(pidx) == len(ridx), fname
            hits = [k for k, i in enumerate(pidx) if re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", praw[i]).strip() == pali]
            assert len(hits) == n, (fname, pali[:60], len(hits))
            for k in hits:
                ln = rraw[ridx[k]]
                if old not in ln and new in ln:
                    print("already:", fname, new[:60]); continue
                assert ln.count(old) == 1, (fname, ln[:80])
                rraw[ridx[k]] = ln.replace(old, new)
            text = "\n".join(rraw)
        changed[fname] = text
        print("edit:", fname, "|", new[:70])
    # 5. ellipsis spacing, every file
    total = 0
    for rf in sorted(RDIR.glob("*.md")):
        text = changed.get(rf.name) or rf.read_text(encoding="utf-8")
        text2, k = ELLIPSIS.subn("…", text)
        if k:
            total += k
            changed[rf.name] = text2
            print(f"ellipsis: {rf.name} {k}")
    print("ellipsis total:", total)
    if not dry:
        for fname, text in changed.items():
            (RDIR / fname).write_text(text, encoding="utf-8", newline="\n")
        print("written:", len(changed), "files")


if __name__ == "__main__":
    main()
