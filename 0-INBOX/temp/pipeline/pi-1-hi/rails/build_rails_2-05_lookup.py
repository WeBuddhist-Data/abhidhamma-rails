"""Termbase lookup for chapter 2-05: print every entry whose key contains one of the stems."""
import pathlib

TB = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-pali-hindi-termbase-plain.md")
STEMS = """vitakkavicār vūpasam paṭhamaṃ dutiyaṃ tatiyaṃ pañcamaṃ paṭhamāya dutiyāya tatiyāya catutthāya suññat appaṇihit
animitt ākāsānañc ākāsa ānañc nevasaññ rūpasaññ paṭighasaññ nānattasaññ amanasikār sammappadhān iddhipād satipaṭṭhān
chandādhip vīriyādhip cittādhip vīmaṃsādhip anavases pathavīkasiṇ sukhavihār rūparāg arūparāg sasaṅkhār ahetuk sahetuk
nākusal neva tasseva aññātāv dhammavicayasamb maggapariy pariyāpann saṃbojjh sambojjh suddhik paṭipad mahānay vīsati nayā
kāyaviññāṇadhātu asātā dukkhā kāyikaṃ cetasik apacayagām vipāko vipākaṃ vipākassa kusalavipāk akusalavipāk
sahagataṃ dukkhasahagat vipassan abhiññ abhiñña bhāvitatt phassaṃ iddhi padhān niṭṭhit kaṇḍ pañcaviññāṇ
""".split()

entries = [l.rstrip("\n") for l in TB.read_text(encoding="utf-8").splitlines() if l.strip()]
seen = set()
for stem in STEMS:
    print(f"=== {stem}")
    for e in entries:
        key = e.split(":", 1)[0]
        if stem in key and e not in seen and len(key) <= 45:
            seen.add(e)
            print(e)
