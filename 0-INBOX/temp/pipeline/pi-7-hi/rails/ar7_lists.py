"""Pañhāvāra list phrases (crimes, upanissaya actions and objects, kamma nouns): Pāli phrase -> expected Hindi.
Prints, per phrase, the lines whose Pāli has the phrase but whose Hindi lacks the expected form (with a snippet).
usage: python -I -B -X utf8 ar7_lists.py [--bak] [-v]"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ar7_common as C

if "--bak" in sys.argv:
    C.CUR["hdir"] = C.BAK
T = [
    (r"pāṇaṃ hana(ti|nti)", r"जीव की हत्या कर"),
    (r"adinnaṃ ādiya(ti|nti)", r"बिना दिया हुआ ले"),
    (r"musā bhaṇa(ti|nti)", r"झूठ बोल"),
    (r"pisuṇaṃ bhaṇa", r"चुगली की बातें बोल"),
    (r"pharusaṃ bhaṇa", r"कठोर वचन बोल"),
    (r"samphaṃ palapa", r"व्यर्थ बकवास कर"),
    (r"sandhiṃ chinda", r"सेंध लगा"),
    (r"nillopaṃ hara", r"डाका डाल"),
    (r"ekāgārikaṃ kar", r"एक ही घर में डाका डाल"),
    (r"paripanthe tiṭṭh", r"राह में घात लगा"),
    (r"paradāraṃ gacch", r"पराई स्त्री के पास जा"),
    (r"gāmaghātaṃ kar", r"गाँव पर हमला कर"),
    (r"nigamaghātaṃ kar", r"कस्बे पर हमला कर"),
    (r"mātaraṃ jīvitā voropet", r"माता की जान ले"),
    (r"pitaraṃ jīvitā voropet", r"पिता की जान ले"),
    (r"arahantaṃ jīvitā voropet", r"अर्हत् की जान ले"),
    (r"lohitaṃ uppād", r"खून बहा"),
    (r"saṅghaṃ bhind", r"संघ में फूट डाल"),
    (r"mātughātikamm", r"माता की हत्या (का|के) कर्म"),
    (r"pitughātikamm", r"पिता की हत्या (का|के) कर्म"),
    (r"arahantaghātikamm", r"अर्हत् की हत्या (का|के) कर्म"),
    (r"ruhiruppādakamm", r"खून बहाने (का|के) कर्म"),
    (r"saṅghabhedakamm", r"संघ में फूट डालने (का|के) कर्म"),
    (r"dānaṃ de(ti|nti)", r"दान दे"),
    (r"sīlaṃ samādiya", r"सदाचार ग्रहण कर"),
    (r"uposathakammaṃ kar", r"उपवास-व्रत का पालन कर"),
    (r"jhānaṃ uppād", r"ध्यान उत्पन्न कर"),
    (r"vipassanaṃ uppād", r"अंतर्दृष्टि उत्पन्न कर"),
    (r"abhiññaṃ uppād", r"उच्च ज्ञान उत्पन्न कर"),
    (r"samāpattiṃ uppād", r"ध्यान-अवस्था उत्पन्न कर"),
    (r"mānaṃ jappe", r"अहंकार पाल"),
    (r"diṭṭhiṃ gaṇh", r"दृष्टि ग्रहण कर"),
    (r"attānaṃ ātāpe", r"स्वयं को तपा"),
    (r"paritāpe", r"कष्ट दे"),
    (r"pariyiṭṭhimūlakaṃ dukkhaṃ", r"खोज के कारण होने वाला दुःख"),
    (r"kāyikaṃ sukhaṃ upanissāya", r"शारीरिक सुख के प्रबल आश्रय से"),
    (r"kāyikaṃ dukkhaṃ upanissāya", r"शारीरिक दुःख के प्रबल आश्रय से"),
    (r"utuṃ upanissāya", r"तापमान के प्रबल आश्रय से"),
    (r"bhojanaṃ upanissāya", r"भोजन के प्रबल आश्रय से"),
    (r"senāsanaṃ upanissāya", r"निवास-स्थान के प्रबल आश्रय से"),
    (r"saddhaṃ upanissāya", r"श्रद्धा के प्रबल आश्रय से"),
    (r"sutaṃ upanissāya", r"सुने-सीखे ज्ञान के प्रबल आश्रय से"),
    (r"cāgaṃ upanissāya", r"त्याग के प्रबल आश्रय से"),
    (r"paññaṃ upanissāya", r"प्रज्ञा के प्रबल आश्रय से"),
    (r"rāgaṃ upanissāya", r"राग के प्रबल आश्रय से"),
    (r"paṭighātatthāya", r"प्रतिकार के लिए"),
    (r"pubbe suciṇṇāni", r"पहले भली-भाँति किए गए कार्य"),
    (r"(sakabhaṇḍe|parabhaṇḍe)", r"(अपनी|पराई) वस्तु के प्रति"),
    (r"pariggahe", r"परिग्रह|संपत्ति|अधिकार"),
    (r"atthappaṭisambhid|atthapaṭisambhid", r"अर्थ (का|के) विश्लेषणात्मक ज्ञान"),
    (r"dhammappaṭisambhid|dhammapaṭisambhid", r"परिघटनाओं (का|के) विश्लेषणात्मक ज्ञान"),
    (r"niruttippaṭisambhid|niruttipaṭisambhid", r"भाषा (का|के) विश्लेषणात्मक ज्ञान"),
    (r"paṭibhānappaṭisambhid|paṭibhānapaṭisambhid", r"सूझ-बूझ (का|के) विश्लेषणात्मक ज्ञान"),
    (r"ṭhānāṭhānakosall", r"स्थान और अस्थान"),
    (r"vaṇṇasampad", r"रंग-रूप की संपन्नता"),
]
for pr, hr in T:
    P, H = re.compile(pr), re.compile(hr)
    n = miss = 0
    ex = []
    for part in C.PARTS:
        for i, (p, h) in enumerate(C.pairs(part)):
            k = len(P.findall(p))
            if not k:
                continue
            n += 1
            if len(H.findall(h)) < k:
                miss += 1
                ex.append(f"{part[:4]}:{i+1}")
    print(f"[{n} lines, {miss} short] {pr} -> {hr}  {' '.join(ex[:12])}")
