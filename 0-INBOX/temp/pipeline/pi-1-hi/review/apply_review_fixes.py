"""Apply the mechanical findings of the independent review to the pi-1 Hindi rails chapters.

usage: python -I -X utf8 apply_review_fixes.py [--write]
Only wording alignment and punctuation; nothing here changes a term. Term questions are for the user.
Backup: backup-pre-review/ (only on --write, only if not already there). Log: review-fixes-log.tsv.
"""
import collections, pathlib, re, shutil, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi")
import hz_common as H

HDIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters")
HERE = pathlib.Path(__file__).parent
WRITE = "--write" in sys.argv
ORD = {"पहला": "पहले", "दूसरा": "दूसरे", "तीसरा": "तीसरे", "चौथा": "चौथे", "पाँचवाँ": "पाँचवें"}

# (name, file prefixes, Pāli-line regex or None, Hindi regex, replacement)
RULES = [
    ("A kasiṇa 2-04", ("2-04",), None, r"ध्यान-मंडल पर आधारित होता है", "ध्यान-मंडल वाला है"),
    ("A kasiṇa 2-05", ("2-05",), None,
     r"पृथ्वी के ध्यान-मंडल पर (पहला|पाँचवाँ) ध्यान प्राप्त करके उसमें रहता है,",
     lambda m: f"{ORD[m.group(1)]} ध्यान को प्राप्त करके उसमें रहता है, जो पृथ्वी के ध्यान-मंडल वाला है,"),
    ("A Tasseva 2-05", ("2-05",), r"[Tt]asseva", r"कारण, इंद्रिय-सुखों से", "कारण जिस समय वह इंद्रिय-सुखों से"),
    ("A jhāna object", ("2-03", "2-05"), r"jhānaṃ upasampajja", r"(पहला|दूसरा|तीसरा|चौथा|पाँचवाँ) ध्यान प्राप्त",
     lambda m: f"{ORD[m.group(1)]} ध्यान को प्राप्त"),
    ("A paṭipadā link", ("2-02",), None, r"प्रगति वाला(?:,| और) (धीमे|शीघ्र) उच्च ज्ञान", r"प्रगति और \1 उच्च ज्ञान"),
    ("A ārammaṇa link", ("2-02",), None, r"(सीमित|अपरिमित), (सीमित|अपरिमित) विषय वाला", r"\1 और \2 विषय वाला"),
    ("A ṭhapetvā और", ("2-04", "2-05"), r"ṭhapetvā viññāṇakkhandhaṃ", r"छोड़कर, चेतना के समूह", "छोड़कर और चेतना के समूह"),
    ("A sabbaso", ("2-04",), r"sabbaso",
     r"पूरी तरह (भौतिक रूप की पहचानों|अनंत आकाश के क्षेत्र|अनंत चेतना के क्षेत्र|कुछ भी न होने के क्षेत्र) को पार", r"\1 को पूरी तरह पार"),
    ("A sahagata hoti", ("2-04",), None, r"के साथ होने वाली होती है और", "के साथ होने वाली है और"),
    ("A sahagata hoti m", ("2-04",), None, r"के साथ होने वाला होता है और", "के साथ होने वाला है और"),
    ("A dhātu order", ("2-04", "2-05", "5-"), None, r"(प्रसन्नता|समभाव) के साथ होने वाला मन की चेतना का तत्व",
     r"मन की चेतना का \1 के साथ होने वाला तत्व"),
    ("B है before और", ("3-03",), None, r" है और (दिखाई|टकराव|स्थूल|सूक्ष्म|दूर|निकट)", r" और \1"),
    ("B Ekakaniddeso", ("3-01",), None, r"एकल वर्गीकरणों की व्याख्या", "एकल वर्गीकरण की व्याख्या"),
    ("C quotation", ("4-", "5-"), None,
     r"इस शिक्षा से बाहर के श्रमणों और ब्राह्मणों की “सदाचार से शुद्धि होती है, व्रत से शुद्धि होती है, सदाचार और व्रत से शुद्धि होती है”",
     "“इस शिक्षा से बाहर के श्रमणों और ब्राह्मणों की शुद्धि सदाचार से होती है, व्रत से होती है, सदाचार और व्रत से होती है”"),
]
# rules that apply to one segment only: id -> [(hindi regex, replacement, expected count)]
BY_ID = {
    "1-887": [(r"व्युत्पन्न और कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला", "व्युत्पन्न है और कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला", 2)],
    "1-1105": [(r"सारी ग़लत दृष्टि (?!भी)", "सारी ग़लत दृष्टि भी ", 1)],
    "1-1122": [(r"सारी ग़लत दृष्टि (?!भी)", "सारी ग़लत दृष्टि भी ", 1)],
    "1-1144": [(r"सारी ग़लत दृष्टि (?!भी)", "सारी ग़लत दृष्टि भी ", 1)],
    "1-1297": [(r"जो ग़लत दृष्टि निश्चित है वह, और", "जो ग़लत दृष्टि निश्चित फल वाली है, और", 1)],
    "1-1310": [(r"उजली परिघटनाएँ हैं\? सभी", "उजली परिघटनाएँ हैं। सभी", 1)],
    "1-1091": [(r"जो वे परिघटनाएँ", "जो परिघटनाएँ", 1), (r"वही वे निर्मित परिघटनाएँ", "वे ही निर्मित परिघटनाएँ", 1)],
    "1-1092": [(r"जो वह परिघटना", "जो परिघटना", 1), (r"वही वह अनिर्मित परिघटना", "वही अनिर्मित परिघटना", 1)],
    "1-1101": [(r"जो वे परिघटनाएँ", "जो परिघटनाएँ", None)],
}
for _sid in ("1-1106", "1-1128", "1-1168", "1-1181", "1-1240", "1-1241", "1-1369", "1-1371"):
    BY_ID[_sid] = [(r"[,।] इस प्रकार (का|की) जो", r"; इस प्रकार \1 जो", 1)]
# closing statements the Pāli wrongly ends with "?"
Q_SLIP = {"1-33", "1-377", "1-765", "1-773", "1-788"}
ROWS_922 = {"1-922", "1-923", "1-926", "1-927", "1-934", "1-935", "1-938", "1-939"}

log, changed, cnt, byid_seen = [], set(), collections.Counter(), collections.Counter()
new_text = {}
for part in H.PARTS:
    p = HDIR / f"{part}.md"
    raw = p.read_text(encoding="utf-8").split("\n")
    pali = H.lines(H.PDIR + "\\" + part + ".md") if False else H.lines(str(pathlib.Path(H.PDIR) / f"{part}.md"))
    idx = [i for i, l in enumerate(raw) if l.strip()]
    assert len(idx) == len(pali), part
    # the block ID stands on the segment's last line: give every line its segment's ID
    sids, cur = [None] * len(pali), None
    for n in range(len(pali) - 1, -1, -1):
        m = H.ID.search(pali[n])
        cur = m.group(1) if m else cur
        sids[n] = cur
    for n, i in enumerate(idx):
        l = raw[i]
        pl = pali[n]
        sid = sids[n]
        nl = l
        for name, pre, prx, hrx, rep in RULES:
            if not part.startswith(pre):
                continue
            if prx and not re.search(prx, pl):
                continue
            if name.startswith("B है") and sid not in ROWS_922:
                continue
            nl, k = re.subn(hrx, rep, nl)
            cnt[name] += k
        for hrx, rep, want in BY_ID.get(sid, []):
            nl, k = re.subn(hrx, rep, nl)
            cnt["C by id: " + str(sid)] += k
            byid_seen[(sid, hrx)] += k
        if sid in Q_SLIP:
            nl2 = re.sub(r"\? \^" + sid + r"$", "। ^" + sid, nl)
            if nl2 != nl:
                cnt["B/A final ? on statement"] += 1
            nl = nl2
        if nl != l:
            log.append((part, i + 1, l, nl))
            raw[i] = nl
            changed.add(p)
    if p in changed:
        new_text[p] = "\n".join(raw)

for k, v in cnt.items():
    print(f"{v:5}  {k}")
print("lines changed", len(log), "files", sorted(x.name[:4] for x in changed))
bad = [(sid, hrx, want, byid_seen[(sid, hrx)]) for sid, rs in BY_ID.items() for hrx, _, want in rs
       if want is not None and byid_seen[(sid, hrx)] != want]
if bad:
    sys.exit(f"segment rules with unexpected counts, nothing written: {bad}")
if WRITE:
    bak = HERE / "backup-pre-review"
    bak.mkdir(exist_ok=True)
    for p, t in new_text.items():
        if not (bak / p.name).exists():
            shutil.copy2(p, bak / p.name)
        p.write_text(t, encoding="utf-8", newline="\n")
    (HERE / "review-fixes-log.tsv").write_text("\n".join("\t".join(map(str, r)) for r in log) + "\n", encoding="utf-8", newline="\n")
    print("written")
else:
    print("(dry run; add --write)")
