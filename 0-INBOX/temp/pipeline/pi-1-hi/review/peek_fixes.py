"""Coordinator's read-only lookups for the review fixes."""
import collections, pathlib, re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi")
import hz_common as H
H.CUR["hdir"] = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters"


def clip(s, k, w=70):
    i = s.find(k)
    return s[max(0, i - w):i + len(k) + w]


def show(name, p_rx, h_key, maxn=6):
    rx = re.compile(p_rx)
    print("=====", name)
    forms, n = collections.Counter(), 0
    for part in H.PARTS:
        for p, h in H.pairs(part):
            if rx.search(p):
                n += 1
                if h_key:
                    for m in re.finditer(h_key, h):
                        forms[(part[:4], m.group(0))] += 1
    for (pt, f), c in sorted(forms.items(), key=lambda x: (-x[1], x[0])):
        print(f"  {c:4} {pt} {f}")
    print("  lines", n)


show("kasiṇa clause", r"kasiṇaṃ", r"[^,;।]{0,12}ध्यान-मंडल[^,;।]{0,30}")
show("Tasseva katattā", r"Tasseva|tasseva", r"कारण[,]? (जिस समय वह )?[^ ]+ [^ ]+")
show("jhāna object form", r"jhānaṃ upasampajja", r"(पहला|पहले|दूसरा|दूसरे|तीसरा|तीसरे|चौथा|चौथे|पाँचवाँ|पाँचवें) (ध्यान)( को)? प्राप्त")
show("paṭipadā link", r"[Pp]aṭipadaṃ", r"प्रगति[^।;]{0,40}उच्च ज्ञान[^ ,]* ?(वाला|वाली|वाले)?")
show("ārammaṇa link", r"parittaṃ parittārammaṇaṃ|parittaṃ appamāṇārammaṇaṃ|appamāṇaṃ parittārammaṇaṃ|appamāṇaṃ appamāṇārammaṇaṃ", r"(सीमित|अपरिमित)(,| और) (सीमित|अपरिमित) विषय[^ ,]* ?(वाला|वाली|वाले)?")
show("ṭhapetvā viññāṇa", r"ṭhapetvā viññāṇakkhandhaṃ", r"छोड़कर(,| और) चेतना के समूह")
show("sabbaso", r"sabbaso", r"[^,;।]{0,10}पूरी तरह[^,;।]{0,50}")
show("sahagata hoti", r"upekkhāsahagat|somanassasahagat", r"के साथ होने वाल[ाीे] (होता|होती|है)[^,;।]{0,6}")
show("somanassa-dhātu heading", r"manoviññāṇadhātu (somanassa|upekkhā)sahagat", r"(प्रसन्नता|समभाव) के साथ होने वाला मन की चेतना का तत्व")
show("mānasaṃ", r"mānasaṃ", r"मन, मानस, मानसिक क्रिया")
show("asārāgo", r"asārāgo", r"[^,]*राग का अभाव|प्रबल राग का अभाव")
show("sammappadhāna", r"sammappadhān", r"[^,;।]{0,16}सही [^ ,;।]+")
show("kāyena", r"kāyena paṭisaṃvedeti", r"(शरीर|काया) से सुख")
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi")
for b in (3, 4, 5):
    t = (ROOT / f"pi-{b}-hindi-plain.md").read_text(encoding="utf-8")
    print(b, {k: t.count(k) for k in ("शरीर से सुख", "काया से सुख", "मानसिक क्रिया", "सही प्रयत्न", "सही परिश्रम", "सही प्रयास", "प्रबल राग का अभाव")})
    tb = (ROOT / f"pi-{b}-pali-hindi-termbase-plain.md").read_text(encoding="utf-8")
    for l in tb.splitlines():
        if re.match(r"(kāyena|mānasaṃ|sammappadhānaṃ|sammappadhāna|sammappadhānā|asārāgo):", l):
            print("  ", l)
tb1 = (ROOT / "pi-1-pali-hindi-termbase-plain.md").read_text(encoding="utf-8")
for l in tb1.splitlines():
    if re.match(r"(kāyena|mānasaṃ|sammappadhānaṃ|asārāgo|sārāgo|asārajjanā|asārajjitattaṃ):", l):
        print(l)
