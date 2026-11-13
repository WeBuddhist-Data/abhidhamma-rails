r"""Apply the accepted review fixes (findings-r1..r8.md, "APPLY") to the pi-6 Hindi rails.

usage: python -I -B -X utf8 apply_review_fixes_pi6.py [--dry] [--user]
Backs up each touched file once to backup-pre-fixes\, logs to fixes-log.tsv (file, line, fix id, old, new).
--user also applies the fixes the user decided (U1..U3), once they are set below.
"""
import pathlib, re, shutil, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
P = ROOT / "AI_translation/pali/pi-6_split_chapters"
H = ROOT / "AI_translation/hindi/pi-6-hindi-plain-rails_split_chapters"
D = pathlib.Path(__file__).parent
BAK = D / "backup-pre-fixes"
DRY = "--dry" in sys.argv
USER = "--user" in sys.argv

MOD = r"(?:आँख|कान|नाक|जीभ|शरीर|मन|भौतिक रूप|मूल|ज्ञान|स्त्रियों|पुरुषों) (?:वाले|से रहित|से अलग|से जुड़े|से भिन्न)"


def fix_line(fname, pali, hin):
    """Return [(fix_id, new_hindi)] applied in order."""
    out = []
    h = hin
    # r6: one mind dissociated from both
    if fname.startswith(("9-01", "9-02")):
        n = re.sub(r"(हितकर|हानिकर) से अलग और (हितकर|हानिकर) से अलग मन", r"\1 और \2 दोनों से अलग मन", h)
        if n != h: out.append("r6-both"); h = n
    # r4: plural Teva puggalā
    if fname.startswith(("7-03", "7-04")) and "Teva puggalā" in pali:
        if not re.search(r"[Ss]veva puggalo", pali):
            n = h.replace("वही व्यक्ति", "वे ही व्यक्ति")
        else:  # sentence-level
            ps = [s for s in re.split(r"(?<=[.?])\s+", pali) if s.strip()]
            hs = re.split(r"(?<=[।?])\s+", h)
            if len(ps) == len(hs):
                hs = [hh.replace("वही व्यक्ति", "वे ही व्यक्ति") if pp.lstrip().startswith("Teva puggalā") else hh
                      for pp, hh in zip(ps, hs)]
                n = " ".join(hs)
            else:
                n = h
                print("SENTENCE MISMATCH (Teva)", fname, pali[:60])
        if n != h: out.append("r4-teva"); h = n
    # r5: dangling marakar in "upapatti nāma natthi"
    if fname.startswith("7-11"):
        n = re.sub(r"से मरकर (?=[^।;]*? में जन्म नाम की कोई चीज़)", "से मरने वाले का ", h)
        if n != h: out.append("r5-marakar"); h = n
    # r3: 5-02 notes
    if fname.startswith("5-02"):
        n = h.replace("‘समाप्ति की ध्यान-अवस्था में लीन लोगों में’", "“समाप्ति की ध्यान-अवस्था में लीन लोगों में”")
        n = n.replace("व्यक्ति और स्थान वाला भाग भी समान है,", "व्यक्ति और स्थान वाला भाग भी समान हैं,")
        n = n.replace("[पाठभेद (Syā.): paccuppannenātītā]", "[वर्तनी-भेद (Syā.): paccuppannenātītā]")
        if n != h: out.append("r3-notes"); h = n
    # r7: drop «फिर» (no Pāli word) in the katici bhave chains
    if fname.startswith(("10-05", "10-06")):
        n = h.replace("बिताकर फिर ", "बिताकर ")
        if n != h: out.append("r7-phir"); h = n
    # r7: 10-02 modifier order follows the Pāli where the manner comes first
    if fname.startswith("10-02") and re.search(r"(Upekkhāya|Somanassena) \w+(kānaṃ|yuttānaṃ)", pali):
        ps = [s for s in re.split(r"(?<=[.?])\s+", pali) if s.strip()]
        hs = re.split(r"(?<=[।?])\s+", h)
        if len(ps) == len(hs):
            new = []
            for pp, hh in zip(ps, hs):
                if re.search(r"(Upekkhāya|Somanassena) \w+(kānaṃ|yuttānaṃ)", pp):
                    hh = re.sub(rf"({MOD}) और ((?:समभाव|प्रसन्नता) के साथ)", r"\2 और \1", hh)
                new.append(hh)
            n = " ".join(new)
        else:
            n = h
            print("SENTENCE MISMATCH (order)", fname, pali[:60])
        if n != h: out.append("r7-order"); h = n
    # r7: ellipsis spacing in short answers, book-wide
    n = h.replace("हाँ …", "हाँ…").replace("ऐसा कोई नहीं है …", "ऐसा कोई नहीं है…")
    if n != h: out.append("r7-ellipsis"); h = n
    # user decisions
    if USER:
        for fid, pref, pcond, old, new in USER_FIXES:
            if fname.startswith(pref) and pcond in pali and old in h:
                h2 = h.replace(old, new)
                if h2 != h: out.append(fid); h = h2
    return h, out


# (fix id, file prefix, Pāli line must contain, old, new): the user's answers of 2026-11-13
USER_FIXES = [
    # U1 emend the three source slips, with «[पाठ में: …]» as for pi-2 ^2-187
    ("U1-slip", "10-08", "no ca tesaṃ tattha somanassindriyaṃ na uppajjittha. Suddhāvāse parinibbantānaṃ asaññasattānaṃ arūpānaṃ tesaṃ tattha cakkhundriyañca na uppajjati sotindriyañca",
     "और कान की क्षमता भी उत्पन्न नहीं हुई थी।",
     "और प्रसन्नता की क्षमता [पाठ में: sotindriyañca] भी उत्पन्न नहीं हुई थी।"),
    ("U1-slip", "10-08", "asaññasattaṃ upapajjantānaṃ tesaṃ tattha somanassindriyaṃ na uppajjati, no ca tesaṃ tattha jīvitindriyaṃ na uppajjittha",
     "वहाँ प्रसन्नता की क्षमता उत्पन्न नहीं होती, पर उनमें वहाँ जीवन-क्षमता उत्पन्न हुई थी।",
     "वहाँ प्रसन्नता की क्षमता उत्पन्न नहीं हुई थी [पाठ में: na uppajjati], पर उनमें वहाँ जीवन-क्षमता उत्पन्न होती है [पाठ में: na uppajjittha]।"),
    ("U1-slip", "9-03", "paṭilabhissanti, asaññasattānaṃ tesaṃ tattha abyākatā dhammā nirujjhissanti, no ca tesaṃ tattha kusalā dhammā uppajjissanti. Itaresaṃ catuvokārānaṃ pañcavokārānaṃ tesaṃ tattha abyākatā ca dhammā nirujjhissanti akusalā",
     "पर उनमें वहाँ हितकर परिघटनाएँ उत्पन्न नहीं होंगी।",
     "पर उनमें वहाँ हानिकर [पाठ में: kusalā] परिघटनाएँ उत्पन्न नहीं होंगी।"),
    # U2 na uppannaṃ / na niruddhaṃ
    ("U2-uppanna", "8-", "", "उत्पन्न हो चुका नहीं है", "उत्पन्न नहीं हुआ है"),
    ("U2-uppanna", "8-", "", "समाप्त हो चुका नहीं है", "समाप्त नहीं हुआ है"),
    # U3 Pahīnavāra heading, oblique participle
    ("U3-pahina", "7-", "", "छोड़ा जा चुका होने", "छोड़े जा चुके होने"),
]


def lines_with_index(text):
    return [(i, l) for i, l in enumerate(text.split("\n")) if l.strip()]


log = []
for pf in sorted(P.glob("*.md")):
    hf = H / pf.name
    ptext = pf.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    htext = hf.read_text(encoding="utf-8")
    pl = [l for l in ptext.split("\n") if l.strip()]
    hraw = htext.split("\n")
    hidx = [i for i, l in enumerate(hraw) if l.strip()]
    assert len(pl) == len(hidx), pf.name
    changed = False
    for k, (pline, i) in enumerate(zip(pl, hidx)):
        new, ids = fix_line(pf.name, pline, hraw[i])
        if ids:
            log.append((pf.name, k + 1, "+".join(ids), hraw[i], new))
            hraw[i] = new
            changed = True
    if changed and not DRY:
        BAK.mkdir(exist_ok=True)
        if not (BAK / hf.name).exists():
            shutil.copy2(hf, BAK / hf.name)
        hf.write_text("\n".join(hraw), encoding="utf-8", newline="\n")

if not DRY:
    with open(D / "fixes-log.tsv", "a", encoding="utf-8", newline="\n") as f:
        for r in log:
            f.write("\t".join(map(str, r)) + "\n")
from collections import Counter
c = Counter()
for r in log:
    for x in r[2].split("+"):
        c[(r[0], x)] += 1
for (fn, x), n in sorted(c.items()):
    print(fn, x, n)
print("lines changed", len(log), "(dry)" if DRY else "")
