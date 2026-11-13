import re, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r4_struct_lib import *

L = r'(?<![a-zāīūṃṅñṭḍṇḷ])'
# (pali regex, hindi regex, name)
T = [
    (L + r'(?:\w*?)khandh', r'समूह', 'khandha'),
    (L + r'mahābhūt', r'महाभूत', 'mahabhuta'),
    (r'cittasamuṭṭhān', r'मन से उत्पन्न', 'cittasam'),
    (r'kaṭattā', r'किए गए कर्म से उत्पन्न', 'katatta'),
    (r'upādārūp', r'व्युत्पन्न', 'upada'),
    (r'paṭisandhi', r'पुनर्जन्म', 'patisandhi'),
    (L + r'(?:vatthu|vatthuṃ|vatthussa)(?![a-zāīūṃṅñṭḍṇḷ])', r'आधार', 'vatthu'),
    (r'āhārasamuṭṭhān', r'आहार से उत्पन्न', 'aharasam'),
    (r'utusamuṭṭhān', r'तापमान से उत्पन्न', 'utusam'),
    (r'asaññasatt', r'पहचान-रहित', 'asanna'),
    (L + r'bāhir', r'बाह्य', 'bahira'),
    (L + r'arūpe', r'अभौतिक लोक', 'arupe'),
    (L + r'ahetuk', r'मूल से रहित', 'ahetuka'),
    (r'cetan[āa]', r'इरादा|इरादे', 'cetana'),
    (r'kabaḷīkār', r'कौर-कौर', 'kabalikara'),
    (r'jīvitindriy', r'जीवन-क्षमता', 'jivita'),
    (L + r'rāg', r'राग', 'raga'),
    (r'vicikicch', r'संशय', 'vicikiccha'),
    (r'uddhacc', r'बेचैनी', 'uddhacca'),
    (r'domanass', r'उदासी', 'domanassa'),
    (L + r'moh', r'मोह', 'moha'),
    (r'nibbān', r'निर्वाण', 'nibbana'),
    (r'gotrabhu', r'गोत्र-परिवर्तन', 'gotrabhu'),
    (r'vodān', r'शुद्धि', 'vodana'),
    (r'āvajjan', r'मोड़ने', 'avajjana'),
    (r'cetopariy', r'दूसरों के मन को जानने', 'cetopariya'),
    (r'pubbenivās', r'पूर्व जन्मों', 'pubbenivasa'),
    (r'yathākammūpag', r'अपने कर्मों के अनुसार', 'yathakamma'),
    (r'anāgataṃsa', r'भविष्य को जानने', 'anagatamsa'),
    (r'iddhividh', r'अलौकिक शक्ति', 'iddhividha'),
    (r'(?:cakkhuviññāṇ|cakkhuviññāṇ)', r'आँख की चेतना', 'cakkhuvinnana'),
    (r'kāyaviññāṇ', r'शरीर की चेतना', 'kayavinnana'),
    (r'cakkhāyatan', r'आँख का इंद्रिय-क्षेत्र|आँख के इंद्रिय-क्षेत्र', 'cakkhayatana'),
    (r'kāyāyatan', r'शरीर का इंद्रिय-क्षेत्र|शरीर के इंद्रिय-क्षेत्र', 'kayayatana'),
    (r'rūpāyatan', r'दृश्य रूप का इंद्रिय-क्षेत्र|दृश्य रूप के इंद्रिय-क्षेत्र', 'rupayatana'),
    (r'phoṭṭhabbāyatan', r'स्पर्श का इंद्रिय-क्षेत्र|स्पर्श के इंद्रिय-क्षेत्र', 'photthabbayatana'),
    (r'saddhā|saddhaṃ|saddhāya', r'श्रद्धा', 'saddha'),
    (r'paññ[āa]', r'प्रज्ञा', 'panna'),
    (L + r'sīl', r'सदाचार', 'sila'),
    (L + r'dān', r'दान', 'dana'),
    (r'paccavekkh', r'पुनः विचार', 'paccavekkh'),
    (r'garuṃ katvā', r'महत्व देकर', 'garum'),
    (r'assād', r'रस ले', 'assada'),
    (r'abhinand', r'आनंद ले', 'abhinand'),
    (r'vipass', r'अंतर्दृष्टि से देख', 'vipass'),
    (r'phalasamāpatti', r'फल की ध्यान-अवस्था', 'phalasam'),
    (r'kusal', r'हितकर', 'kusala'),
    (r'akusal', r'हानिकर', 'akusala'),
    (r'abyākat', r'अनिर्धारित', 'abyakata'),
    (r'sampayuttak', r'जुड़े हुए', 'sampayuttaka'),
    (r'pacchājāt', r'पश्चात्-उत्पत्ति|बाद में उत्पन्न', 'pacchajata'),
    (r'purejātassa imassa kāyassa|purejātassa kāyassa', r'पहले उत्पन्न', 'purejatakaya'),
    (r'āpodhāt', r'जल तत्व', 'apodhatu'),
    (r'itthindriy', r'स्त्रीत्व', 'itthindriya'),
    (r'purisindriy', r'पुरुषत्व', 'purisindriya'),
    (r'(?<![a-z])nirodh', r'निरोध|समाप्ति', 'nirodha'),
    (r'(?<![a-zā])anantarūpanissay', r'निकटता रूपी प्रबल आश्रय', 'anantarupanissaya'),
    (r'ārammaṇūpanissay', r'विषय रूपी प्रबल आश्रय', 'arammanupanissaya'),
    (r'pakatūpanissay', r'स्वाभाविक प्रबल आश्रय', 'pakatupanissaya'),
    (r'ārammaṇādhipat', r'विषय रूपी प्रधानता', 'arammanadhipati'),
    (r'sahajātādhipat', r'सह-उत्पत्ति रूपी प्रधानता', 'sahajatadhipati'),
    (r'nānākkhaṇik', r'भिन्न क्षण', 'nanakkhanika'),
]
CT = [(re.compile(a, re.I), re.compile(b), n) for a, b, n in T]

def counts(s, latin):
    c = collections.Counter()
    for rp, rh, n in CT:
        c[n] = len((rp if latin else rh).findall(s))
    return c

if __name__ == '__main__':
    only = sys.argv[1] if len(sys.argv) > 1 else ''
    tot = 0
    agg = collections.Counter()
    for f in FILES:
        if only and not f.startswith(only):
            continue
        P = nonempty(load(os.path.join(PA, f)))
        H = nonempty(load(os.path.join(HI, f)))
        for n, ((_, p), (_, h)) in enumerate(zip(P, H), 1):
            if p.startswith('#'):
                continue
            a = counts(p, True); b = counts(h, False)
            diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
            if diff:
                tot += 1
                for k in diff: agg[k] += 1
                print(f[:4], n, ' '.join('%s:%d/%d' % (k, v[0], v[1]) for k, v in diff.items()))
    print('TOTAL', tot)
    print(agg.most_common())
