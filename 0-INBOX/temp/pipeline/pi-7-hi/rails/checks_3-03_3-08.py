"""Extra checks on the 3-03..3-08 outputs: double blanks, CR, Latin outside brackets, ':-', '…pe…', ASCII quotes."""
import collections
import pathlib
import re

OUT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters")
for f in ["3-03-asavagocchaka.md", "3-04-sannojanagocchaka.md", "3-05-ganthagocchaka.md",
          "3-06-oghayogagocchaka.md", "3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md"]:
    t = (OUT / f).read_text(encoding="utf-8")
    nob = re.sub(r"\[[^\]]*\]", "", t)
    nob = re.sub(r"\^[0-9A-Za-z-]+", "", nob)
    latin = collections.Counter(re.findall(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]{2,}", nob))
    print(f, "| double blank:", "\n\n\n" in t, "| CR:", "\r" in t, "| latin:", latin.most_common(8),
          "| ':-'", ":-" in t, "| pe:", "pe…" in t, "| ascii quote:", '"' in t, "| '??':", "??" in t,
          "| '  ':", "  " in t)
