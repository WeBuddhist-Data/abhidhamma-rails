"""Count Hindi strings in my five files (strings listed in this script, edited as needed)."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[5]
D = ROOT / "AI_translation" / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters"
FILES = ["3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka", "3-05-ganthagocchaka",
         "3-06-oghayogagocchaka"]
S = ["जीव की हत्या", "जीवों की हत्या", "हत्या", "प्रधानता –", "निर्वाण", "आहार को", "भोजन को",
     "दूसरों के मन को जानने के ज्ञान से", "ग़लत दृष्टि से अलग और लोभ के साथ होने वाल", "लोभ के साथ होने वाल",
     "अभौतिक को", "दृष्टि के लिए", "बाहर आने", "बाहर आना"]
texts = {f: (D / f"{f}.md").read_text(encoding="utf-8") for f in FILES}
for s in S:
    print(s, {f[:4]: t.count(s) for f, t in texts.items() if t.count(s)})
