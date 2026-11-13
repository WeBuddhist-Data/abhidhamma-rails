r"""Make the pi-6 Hindi follow the Pāli as written (user decision 2026-11-13: no emendations unless the
source data is updated). Reverts every meaning-changing correction found by the agents and reviewers;
pure spelling slips (upapajj-/uppajj-, nirujjhattha, vadanā, ariyāpanne, bhavissanti for bhāvessanti …)
stay rendered as the word meant, and agreement slips stay grammatical Hindi.

usage: python -I -B -X utf8 revert_to_literal_pi6.py [--dry]
Backs up touched files once to backup-pre-literal\, appends to literal-log.tsv.
"""
import pathlib, shutil, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
P = ROOT / "AI_translation/pali/pi-6_split_chapters"
H = ROOT / "AI_translation/hindi/pi-6-hindi-plain-rails_split_chapters"
D = pathlib.Path(__file__).parent
BAK = D / "backup-pre-literal"
DRY = "--dry" in sys.argv

# (id, file, Pāli line must contain, old Hindi, new Hindi)
FIXES = [
    ("^6-6-121", "6-02-sankharayamaka.md",
     "Paṭhamajjhānaṃ samāpannānaṃ itaresaṃ kāmāvacarānaṃ tesaṃ tattha kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca nirujjhissati",
     "वहाँ शरीर की रचना भी समाप्त हुई थी और वाणी की रचना भी समाप्त होगी।",
     "वहाँ शरीर की रचना समाप्त नहीं हुई थी और वाणी की रचना समाप्त होगी।"),
    ("^6-6-132", "6-02-sankharayamaka.md",
     "(Ka) yassa kāyasaṅkhāro nuppajjati tassa cittasaṅkhāro nirujjhatīti?",
     "क्या उसमें मन की रचना समाप्त नहीं होती?",
     "क्या उसमें मन की रचना समाप्त होती है?"),
    ("^6-7-243", "7-07-anusayayamaka.md",
     "(Ka) yato paṭighānusayaṃ na parijānāti tato mānānusayaṃ parijānātīti?",
     "क्या वहाँ अहंकार की सुप्त प्रवृत्ति को पूरी तरह नहीं समझा जाता?",
     "क्या वहाँ अहंकार की सुप्त प्रवृत्ति को पूरी तरह समझा जाता है?"),
    ("^6-10-240", "10-05-indriyayamaka.md",
     "Yassa vā pana purisindriyaṃ uppajjittha tattha cakkhundriyaṃ uppajjitthāti?",
     "क्या उसमें आँख की क्षमता उत्पन्न हुई थी?",
     "क्या वहाँ आँख की क्षमता उत्पन्न हुई थी?"),
    ("^6-9-192", "9-03-dhammayamaka.md",
     "no ca tesaṃ tattha kusalā dhammā uppajjissanti. Itaresaṃ catuvokārānaṃ pañcavokārānaṃ tesaṃ tattha abyākatā ca dhammā nirujjhissanti akusalā",
     "पर उनमें वहाँ हानिकर [पाठ में: kusalā] परिघटनाएँ उत्पन्न नहीं होंगी।",
     "पर उनमें वहाँ हितकर परिघटनाएँ उत्पन्न नहीं होंगी।"),
    ("^6-10-357", "10-08-indriyayamaka.md",
     "cakkhundriyañca na uppajjati sotindriyañca na uppajjittha",
     "और प्रसन्नता की क्षमता [पाठ में: sotindriyañca] भी उत्पन्न नहीं हुई थी।",
     "और कान की क्षमता भी उत्पन्न नहीं हुई थी।"),
    ("^6-10-361", "10-08-indriyayamaka.md",
     "tesaṃ tattha somanassindriyaṃ na uppajjati, no ca tesaṃ tattha jīvitindriyaṃ na uppajjittha",
     "वहाँ प्रसन्नता की क्षमता उत्पन्न नहीं हुई थी [पाठ में: na uppajjati], पर उनमें वहाँ जीवन-क्षमता उत्पन्न होती है [पाठ में: na uppajjittha]।",
     "वहाँ प्रसन्नता की क्षमता उत्पन्न नहीं होती, पर उनमें वहाँ जीवन-क्षमता उत्पन्न हुई थी।"),
]

log, done = [], set()
for fname in sorted({f[1] for f in FIXES}):
    pl = [l for l in (P / fname).read_text(encoding="utf-8-sig").replace("\r\n", "\n").split("\n") if l.strip()]
    hf = H / fname
    raw = hf.read_text(encoding="utf-8").split("\n")
    idx = [i for i, l in enumerate(raw) if l.strip()]
    assert len(pl) == len(idx), fname
    for fid, f, cond, old, new in FIXES:
        if f != fname:
            continue
        hits = [k for k, p in enumerate(pl) if cond in p and old in raw[idx[k]]]
        for k in hits:
            i = idx[k]
            log.append((fid, fname, k + 1, raw[i], raw[i].replace(old, new)))
            raw[i] = raw[i].replace(old, new)
        if hits:
            done.add(fid)
        print(fid, fname, "lines", len(hits))
    if any(r[1] == fname for r in log) and not DRY:
        BAK.mkdir(exist_ok=True)
        if not (BAK / fname).exists():
            shutil.copy2(hf, BAK / fname)
        hf.write_text("\n".join(raw), encoding="utf-8", newline="\n")
missing = [f[0] for f in FIXES if f[0] not in done]
if missing:
    print("NOT FOUND:", missing)
if not DRY:
    with open(D / "literal-log.tsv", "a", encoding="utf-8", newline="\n") as fh:
        for r in log:
            fh.write("\t".join(map(str, r)) + "\n")
print("lines changed", len(log), "(dry)" if DRY else "")
