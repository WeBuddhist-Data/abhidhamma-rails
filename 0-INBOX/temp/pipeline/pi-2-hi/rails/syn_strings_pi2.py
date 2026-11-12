"""Variants of the factor synonym strings across chapters (and pi-1 rails), Hindi from an anchor word to the next
« – » / «है» / «।».  usage: python -I -X utf8 syn_strings_pi2.py [--bak]"""
import collections, os, re, sys
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = ROOT + r"\AI_translation\pali\pi-2_split_chapters"
HDIR = ROOT + r"\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters"
if "--bak" in sys.argv:
    HDIR = ROOT + r"\0-INBOX\temp\pipeline\pi-2-hi\rails\backup-pre-align"
P1P = ROOT + r"\AI_translation\pali\pi-1_split_chapters"
P1H = ROOT + r"\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters"
SETS = [
    ("vīriya", r"vīriyārambho nikkamo", r"उत्साह जगाना, आगे बढ़ना[^–।]*"),
    ("sati", r"sati anussati paṭissati", r"सजगता, बार-बार स्मरण[^–।]*"),
    ("paññā", r"paññā pajānanā vicayo", r"प्रज्ञा, जानना[^–।]*"),
    ("samādhi", r"cittassa ṭhiti saṇṭhiti", r"मन की स्थिरता[^–।]*"),
    ("vitakka", r"takko vitakko saṅkappo appanā", r"सोचना, आरंभिक विचार[^–।]*"),
    ("pīti", r"pīti pāmojjaṃ", r"उल्लास, प्रमोद[^–।]*|उल्लास, आनंद[^–।]*"),
    ("passaddhi", r"passaddhi paṭippassaddhi", r"प्रशांति, पूरी प्रशांति[^–।]*"),
    ("upekkhā", r"upekkhā upekkhanā ajjhupekkhanā", r"समभाव, समभाव रखना[^–।]*"),
    ("chanda", r"chando chandikatā", r"चाह, चाहना[^–।]*"),
    ("saddhā", r"saddhā saddahanā okappanā", r"श्रद्धा, श्रद्धा रखना[^–।]*"),
    ("moha", r"aññāṇaṃ adassanaṃ", r"न जानना, न देखना[^–।]*"),
    ("lobha", r"rāgo sārāgo anunayo", r"राग, प्रबल राग[^–।]*"),
    ("dosa", r"āghāto paṭighāto", r"[^,।]{0,20}आघात[^–।]*"),
    ("diṭṭhi", r"diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ", r"दृष्टि, दृष्टियों में फँसना[^–।]*"),
    ("citta", r"cittaṃ mano mānasaṃ hadayaṃ", r"मन, मानस, मानसिक क्रिया[^–।]*"),
]


def lines(p):
    return [l for l in open(p, encoding="utf-8-sig").read().splitlines() if l.strip()]


def pairs(pd, hd):
    for f in sorted(os.listdir(pd)):
        if f.endswith(".md") and os.path.exists(os.path.join(hd, f)):
            yield f.split("-")[0] if pd == PDIR else "pi1:" + f[:4], lines(os.path.join(pd, f)), lines(os.path.join(hd, f))


for name, prx, hrx in SETS:
    cnt = collections.defaultdict(collections.Counter)
    for src in ((PDIR, HDIR), (P1P, P1H)):
        for tag, P, H in pairs(*src):
            for p, h in zip(P, H):
                if re.search(prx, p):
                    for m in re.finditer(hrx, h):
                        s = re.sub(r"\s*\[[^\]]*\]", "", m.group(0)).strip()
                        cnt[s][tag] += 1
    print(f"### {name}")
    for s, c in sorted(cnt.items(), key=lambda kv: -sum(kv[1].values())):
        print(f"  [{sum(c.values())}] {dict(c)} :: {s[:400]}")
