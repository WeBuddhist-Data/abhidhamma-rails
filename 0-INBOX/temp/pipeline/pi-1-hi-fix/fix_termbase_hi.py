"""Bring the Hindi pi-1 termbase in line with the fixed text (2026-11-27), and fix the termbase-only defects.

Runs on the backup copy (the termbase as it was) so it can be rerun. Each rule has an expected count.
Writes AI_translation/hindi/pi-1-pali-hindi-termbase-plain.md; the track copy is a plain copy of it.
usage: python3 -I fix_termbase_hi.py [--write]
"""
import sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import vinnana  # noqa: E402

REPO = HERE.parents[3]
SRC = HERE / "backup/pi-1-pali-hindi-termbase-plain.md"
OUT = REPO / "AI_translation/hindi/pi-1-pali-hindi-termbase-plain.md"
WRITE = "--write" in sys.argv

RULES = [  # (pattern, replacement, expected)
    ("परस्पर-आश्रित रूप से उत्पन्न", "कारणों पर आश्रित होकर उत्पन्न", 4),
    ("paṭiccasamuppanna: परस्पर-आश्रित}", "paṭiccasamuppanna: कारणों पर आश्रित}", 1),
    ("परस्पर-आश्रित उत्पत्ति", "कारणों पर आश्रित उत्पत्ति", 1),
    ("इच्छा-रहित", "आकांक्षा-रहित", 2),
    ("इच्छाओं का अभाव", "आकांक्षाओं का अभाव", 2),
    ("दुःखद प्रगति", "कष्टदायक प्रगति", 1),
    ("बुराई के प्रति निडरता", "बुराई से न डरने की वृत्ति", 8),
    ("amanussa: {non-human beings, spirits (compound member): अमानवीय प्राणी}",
     "amanussa: {non-human, in amanussasadda (compound member): मनुष्येतर}", 1),
    ("amanussasaddo: {the sound of non-human beings, spirit voices (nominative sg.): अमानवीय प्राणियों की ध्वनि}",
     "amanussasaddo: {non-human sound, every sound other than human speech (aṭṭhakathā) (nominative sg.): मनुष्येतर ध्वनि}", 1),
    ("upādiṇṇā: {acquired by kamma, produced by past action (nominative pl. participle): कर्म से उत्पन्न}",
     "upādiṇṇā: {acquired by kamma, produced by past action (nominative pl. participle): कर्म से उत्पन्न; taken up, grasped as one's own, kamma-born or not, in ^1-1050/1-1051 (aṭṭhakathā) (nominative pl. participle): ग्रहण की हुई}", 1),
    ("(neuter sg.): खारा}", "(neuter sg.): क्षारीय}", 1),
    ("{the existing body, the personality taken as a lasting self (compound member): स्थायी आत्मा}", "{the existing personality, the five groups regarded in terms of a self (compound member): पाँच समूह}", 1),
    ("{personality view, the wrong view of a lasting self (nominative sg.): स्थायी आत्मा की ग़लत दृष्टि}", "{personality view, regarding the five groups in terms of a self in four ways (nominative sg.): पाँच समूहों के संबंध में आत्मा की ग़लत दृष्टि}", 1),
    ("सदाचार और व्रतों के बारे में ग़लत धारणा", "नियमों और व्रतों को ही शुद्धि का मार्ग मानने की ग़लत धारणा", 8),
    ("सदाचार और व्रतों के प्रति आसक्ति", "नियमों और व्रतों के प्रति आसक्ति", 3),
    ("(compound member): सदाचार और व्रत}", "(compound member): नियम और व्रत}", 1),
    ("(nominative sg.): अशिक्षित}", "(nominative sg.): उपदेश से अनजान}", 1),
    ("compound final): मूर्छा}", "compound final): मदहोशी}", 1),
    ("आक्रोश", "रोष", 2),
    ("(neuter sg.): मान चुका होना}", "(neuter sg.): अपने को कुछ मान बैठना}", 1),
    ("(nominative sg.): मान लेना}", "(nominative sg.): अपने को कुछ मानना}", 1),
    ("(nominative sg.): निरंतर सेवन}", "(nominative sg.): निरंतर आचरण}", 1),
    ("मानसिक पक्ष", "अभौतिक पक्ष", 3),
    ("(adverb): कभी}", "(adverb): कुछ स्थितियों में}", 1),
    ("(compound member): न अ-पहचान}", "(compound member): न पहचान का अभाव}", 1),
    ("(compound member): अ-पहचान}", "(compound member): पहचान का अभाव}", 1),
    ("sīla: {virtue, moral conduct, precepts (compound member): सदाचार}",
     "sīla: {virtue, moral conduct, precepts (compound member): सदाचार; rules and observances, in sīlabbata and sīlena suddhi (compound member): नियम}", 1),
    ("dukkha: {pain, suffering, or painful (compound member, as in dukkhapaṭipadā and dukkhasahagata): दुःखद}",
     "dukkha: {pain, suffering, or painful (compound member, as in dukkhasahagata): दुःखद; painful, laborious, in dukkhapaṭipadā (compound member): कष्टदायक}", 1),
    ("pahātabbahetukā: {having roots that are to be abandoned (nominative pl.): छोड़े जाने वाले मूलों वाला}",
     "pahātabbahetukā: {having roots that are to be abandoned (nominative pl.): छोड़े जाने वाले मूलों वाला; having no root to be abandoned, in neva dassanena na bhāvanāya pahātabbahetukā (aṭṭhakathā ^1-528) (nominative pl.): छोड़े जाने वाले मूलों से भी रहित}", 1),
    ("upādiṇṇaṃ: {kamma-born, produced by past action (neuter sg. participle): कर्म से उत्पन्न}",
     "upādiṇṇaṃ: {kamma-born, produced by past action (neuter sg. participle): कर्म से उत्पन्न; taken up, grasped, kamma-born or not, in the element definitions ^1-967–970 (aṭṭhakathā) (neuter sg. participle): ग्रहण किया हुआ}", 1),
    ("external, belonging to others, in 'ajjhattaṃ vā bahiddhā vā' and the internal and external triad (adverb): दूसरों से संबंधित}",
     "external, belonging to others, in the internal and external triad (adverb): दूसरों से संबंधित; in 'ajjhattaṃ vā bahiddhā vā' of the four elements ^1-967–970 the sense is 'external' (aṭṭhakathā: bāhiraṃ), rendered बाहर}", 1),
    # termbase-only defects (the text was already right)
    ("(3rd sg. present): व्यर्थ और नहीं}", "(3rd sg. present): नहीं}", 1),
    ("indriyabaddharūpañca nibbānañca: {matter bound to the faculties, and Nibbāna (nominative sg.): इंद्रियों से बँधा भौतिक रूप और निर्वाण}",
     "indriyabaddharūpañca nibbānañca: {matter not bound to the faculties, and Nibbāna; the key is found inside anindriyabaddha- (nominative sg.): इंद्रियों से न बँधा भौतिक रूप और निर्वाण}", 1),
]


def main():
    t = SRC.read_text(encoding="utf-8")
    before = t.count("चेतना")
    t, log = vinnana.convert(t)
    assert "चेतन" not in t, "चेतन left in termbase"
    print(f"viññāṇa: {before} चेतना -> विज्ञान")
    bad = 0
    for pat, rep, exp in RULES:
        n = t.count(pat)
        t = t.replace(pat, rep)
        ok = n == exp
        bad += not ok
        print(f"{'OK' if ok else 'MISMATCH':8} {n}/{exp}  {pat[:60]}")
    import re
    SENSE = r"(?<![\u0900-\u0963\u0971-\u097F-])(आँख|कान|नाक|जीभ|शरीर|मन) (का|के) विज्ञान(?![\u0900-\u0963\u0971-\u097F])"
    t, n = re.subn(SENSE, lambda m: m.group(1) + (" से होने वाला विज्ञान" if m.group(2) == "का" else " से होने वाले विज्ञान"), t)
    ok = n == 30
    bad += not ok
    print(f"{'OK' if ok else 'MISMATCH':8} {n}/30  X का/के विज्ञान -> X से होने वाला/वाले विज्ञान")
    if bad:
        sys.exit("aborted: a count differs; nothing written")
    if WRITE:
        OUT.write_text(t, encoding="utf-8", newline="\n")
        print("written", OUT)


if __name__ == "__main__":
    main()
