import re, sys
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['1-02-vedanattika.md', '1-03-vipakattika.md', '1-04-upadinnattika.md', '1-05-sankilitthattika.md']
ID_RE = re.compile(r'\s\^([\w-]+)\s*$')

# (label, pali regex (lowercased text), hindi regex)
T = [
    ('paṭisandhi', r'paṭisandhik?k?h?aṇe|paṭisandhikhaṇe', r'पुनर्जन्म के क्षण'),
    ('cittasamuṭṭhāna', r'cittasamuṭṭhān', r'मन से उत्पन्न'),
    ('kaṭattā', r'kaṭattā', r'किए गए कर्म से उत्पन्न'),
    ('upādārūpa', r'upādārūp', r'व्युत्पन्न'),
    ('mahābhūta', r'mahābhūt', r'महाभूत'),
    ('vatthu', r'\bvatthu', r'आधार'),
    ('khandha', r'\bkhandh', r'समूह'),
    ('arūpe', r'\barūpe\b', r'अभौतिक'),
    ('asaññasatta', r'asaññasatt', r'पहचान-रहित'),
    ('bāhira', r'bāhir', r'बाह्य'),
    ('āhārasamuṭṭhāna', r'āhārasamuṭṭhān', r'आहार से उत्पन्न'),
    ('utu', r'\butu', r'तापमान'),
    ('cetanā', r'cetanā', r'इरादा|इरादे'),
    ('kabaḷīkāra', r'kabaḷīkār', r'कौर'),
    ('jīvitindriya', r'jīvitindriy', r'जीवन-क्षमता'),
    ('purimā', r'purimā', r'पहले-पहले'),
    ('pacchima', r'pacchimānaṃ', r'बाद-बाद'),
    ('anuloma(prose)', r'\banulomaṃ (?:gotrabhussa|vodānassa|phalassa|phalasamāpattiyā)', r'अनुरूपता'),
    ('gotrabhu', r'gotrabhu', r'गोत्र-परिवर्तन'),
    ('vodāna', r'vodān', r'शुद्धि'),
    ('nibbāna', r'nibbān', r'निर्वाण'),
    ('phala', r'\bphal', r'(?<!कर्म-)फल(?!-कारण)'),
    ('magga(prose)', r'\bmagg(?!apaccay)(?:o|aṃ|assa|ā)\b|maggaṅg', r'मार्ग(?!-कारण)'),
    ('cakkhu', r'\bcakkhu|\bcakkhā', r'आँख'),
    ('sota', r'\bsot[aā]|sotadhāt', r'कान'),
    ('ghāna', r'\bghān', r'(?<!ब)नाक'),
    ('jivhā', r'\bjivh', r'जीभ'),
    ('rūpe/rūpāyatana', r'\brūpe\b|rūpāyatan', r'दृश्य रूप'),
    ('sadda', r'\bsadd[ae]\b|\bsaddaṃ|saddāyatan', r'ध्वनि'),
    ('gandha', r'\bgandh', r'गंध'),
    ('rasa', r'\brase\b|rasāyatan', r'स्वाद'),
    ('phoṭṭhabba', r'phoṭṭhabb', r'स्पर्श'),
    ('rāga', r'\brāg', r'राग'),
    ('dosa', r'\bdos[oaā]', r'द्वेष'),
    ('moha', r'\bmoh', r'मोह'),
    ('diṭṭhi', r'diṭṭhi', r'(?<!अंतर्)दृष्टि'),
    ('vicikicchā', r'vicikicch', r'संशय'),
    ('uddhacca', r'uddhacc', r'बेचैनी'),
    ('domanassa', r'domanass', r'उदासी'),
    ('māna', r'\bmān[oaā]', r'अहंकार'),
    ('patthanā', r'patthan', r'कामना'),
    ('saddhā', r'\bsaddh', r'श्रद्धा'),
    ('sīla', r'\bsīl', r'सदाचार'),
    ('suta', r'\bsut[aā]', r'सुना-सीखा|सुने-सीखे'),
    ('cāga', r'\bcāg', r'त्याग'),
    ('paññā', r'\bpaññ', r'प्रज्ञा'),
    ('dāna', r'\bdān', r'दान'),
    ('uposatha', r'uposath', r'उपवास-व्रत'),
    ('vipassanā', r'vipassan[aā]ṃ', r'अंतर्दृष्टि उत्पन्न'),
    ('abhiññā', r'abhiññ', r'उच्च ज्ञान'),
    ('samāpatti', r'samāpatti|samāpajj', r'(?<!समाप्ति की )ध्यान-अवस्था'),
    ('sekkhā', r'sekkh', r'सीखने के चरण'),
    ('puthujjana', r'puthujjan', r'साधारण व्यक्ति'),
    ('ariyā', r'\bariy', r'आर्य'),
    ('arahā', r'\barah[aā]', r'अर्हत्'),
    ('garuṃ', r'\bgaruṃ', r'महत्व'),
    ('tadārammaṇatā', r'tadārammaṇ', r'उसी विषय को लेकर'),
    ('niruddhe', r'niruddhe', r'समाप्त होने पर'),
    ('dibba', r'\bdibb', r'दिव्य'),
    ('kiriya', r'kiriy', r'क्रिया'),
    ('bhavaṅga', r'bhavaṅg', r'जीवन-धारा'),
    ('āvajjanā', r'āvajjan', r'मोड़'),
    ('sahajāta(bare)', r'\bsahajāt(?:aṃ|ā|o)\b', r'सह-उत्पत्ति(?!-कारण| रूपी| का खंड)'),
    ('purejāta(bare)', r'\bpurejāt(?:aṃ|ā|o|assa)\b|vatthupurejāt|ārammaṇapurejāt', r'पूर्व-उत्पत्ति(?!-कारण)'),
    ('pacchājāta(bare)', r'\bpacchājāt(?:aṃ|ā|o)\b', r'पश्चात्-उत्पत्ति(?!-कारण)'),
    ('pakatūpanissaya', r'pakatū(?:pa)?nissay', r'स्वाभाविक प्रबल आश्रय'),
    ('ārammaṇūpanissaya', r'ārammaṇūpanissay', r'विषय रूपी प्रबल आश्रय'),
    ('anantarūpanissaya', r'anantarūpanissay', r'निकटता रूपी प्रबल आश्रय'),
    ('ārammaṇādhipati', r'ārammaṇādhipati', r'विषय रूपी प्रधानता'),
    ('sahajātādhipati', r'sahajātādhipati', r'सह-उत्पत्ति रूपी प्रधानता'),
    ('nānākkhaṇikā', r'nānāk?khaṇik', r'भिन्न'),
    ('kāyika', r'kāyik', r'शारीरिक'),
    ('bhojana', r'bhojan', r'भोजन'),
    ('senāsana', r'senāsan', r'निवास-स्थान'),
    ('ahetuka', r'ahetuk', r'मूल से रहित|मूल-रहित'),
    ('kusala(prose)', r'\bkusal(?!attik)', r'हितकर(?! वाल)'),
    ('akusala', r'akusal|kusalākusal', r'हानिकर'),
    ('kamma(prose)', r'\bkamma(?:ṃ|ssa)\b|kammavipāk|sakammaṃ', r'कर्म(?!-कारण|-फल| से उत्पन्न|ों)'),
    ('vipāka(prose,noun)', r'\bvipāko tadārammaṇ', r'कर्म-फल उसी'),
    ('jhāna(prose)', r'\bjhān(?:aṃ|ā|e|assa)\b(?! (?:ekaṃ|dve|tīṇi|cattāri|pañca|cha|satta|aṭṭha|nava|dasa))', r'ध्यान(?!-कारण|-अवस्था)'),
    ('indriya(prose)', r'\bindriy(?:aṃ|ā)\b|cakkhundriy|kāyindriy|jīvitindriy', r'क्षमता(?!-कारण)'),
    ('āhāra(prose)', r'\bāhār(?:o|aṃ|ā)\b|kabaḷīkār', r'आहार(?!-कारण| से उत्पन्न)'),
    ('viññāṇa', r'viññāṇ', r'चेतना'),
    ('vuṭṭhahitvā', r'vuṭṭhah|vuṭṭhān', r'उठकर|बाहर आ'),
    ('paccavekkhati', r'paccavekkh', r'पुनः विचार'),
    ('vipassati', r'vipass(?:ati|anti)|vippassanti', r'अंतर्दृष्टि से देख'),
    ('assādeti', r'assāde', r'रस लेत'),
    ('abhinandati', r'abhinand', r'आनंद लेत'),
    ('ārabbha', r'ārabbha', r'विषय बनाकर'),
    ('upanissāya', r'upanissāya', r'प्रबल आश्रय से'),
    ('jānāti', r'\bjān(?:āti|anti)\b', r'जानत'),
    ('passati', r'\bpass(?:ati|anti)\b', r'(?<!अंतर्दृष्टि से )देखत'),
    ('suṇāti', r'\bsuṇ(?:āti|anti)\b', r'सुनत'),
    ('aniccato', r'aniccato', r'अनित्य'),
    ('pahīne', r'pahīne', r'छोड़े'),
    ('vikkhambhite', r'vikkhambhite', r'दबाए'),
    ('samudāciṇṇe', r'samudāciṇṇe', r'बार-बार उठे'),
]
CT = [(lab, re.compile(p), re.compile(h)) for lab, p, h in T]

def main():
    filt = sys.argv[1:]
    for f in FILES:
        p = [l for l in open(ROOT + '\\pali\\pi-7_split_chapters\\' + f, encoding='utf8').read().split('\n') if l.strip()]
        h = [l for l in open(ROOT + '\\hindi\\pi-7-hindi-plain-rails_split_chapters\\' + f, encoding='utf8').read().split('\n') if l.strip()]
        for k, (ps, hs) in enumerate(zip(p, h), 1):
            if ps.startswith('#'):
                continue
            ps2 = re.sub(r'\{[^}]*\}', ' ', ps).lower()
            hs2 = re.sub(r'\[(पाठभेद|वर्तनी-भेद)[^\]]*\]', ' ', hs)
            diffs = []
            for lab, pr, hr in CT:
                if filt and lab not in filt:
                    continue
                a = len(pr.findall(ps2)); b = len(hr.findall(hs2))
                if a != b:
                    diffs.append('%s %d/%d' % (lab, a, b))
            if diffs:
                m = ID_RE.search(ps)
                print('%s L%d(%s): %s' % (f[:4], k, m.group(1) if m else '', '; '.join(diffs)))

main()
