import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi")
import hz_common as H
H.CUR["hdir"] = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters"
def clip(s, k, w=60):
    i = s.find(k); return s[max(0, i - w):i + len(k) + w] if i >= 0 else "(none)"
for part in H.PARTS:
    for p, h in H.pairs(part):
        for rx, hk in ((r"padhān", "प्र"), (r"asārāgo", "राग का अभाव"), (r"kāyena paṭisaṃvedeti", "से सुख")):
            if re.search(rx, p):
                m = re.search(r"\S*" + rx + r"\S*", p)
                print(part[:4], rx, "|", m.group(0), "|", [clip(h, x.group(0), 30) for x in re.finditer(r"(सही )?(प्रयास|प्रयत्न)|राग का अभाव|(शरीर|काया) से सुख", h)][:3])
