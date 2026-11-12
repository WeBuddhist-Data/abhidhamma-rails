"""Filter divergences.md groups: drop groups whose Hindi forms differ only by gender/number agreement.
usage: python -I -X utf8 div_filter_pi2.py [section-prefix, default (a]"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sec = sys.argv[1] if len(sys.argv) > 1 else "(a"
AGR = [(r"\b(होता|होते|होती|होतीं)\b", "होत_"), (r"\b(वाला|वाले|वाली)\b", "वाल_"), (r"\b(का|के|की)\b", "क_"),
       (r"\b(हुआ|हुए|हुई)\b", "हु_"), (r"(जुड़ा|जुड़े|जुड़ी)", "जुड़_"), (r"\b(कितने|कितनी)\b", "कितन_"),
       (r"\b(हैं|है)\b", "ह_"), (r"\b(जाने|जानी|जाना)\b", "जान_"), (r"(समाया|समाए|समाई)", "समा_"),
       (r"(घुला-मिला|घुले-मिले|घुली-मिली)", "घुल_"), (r"\b(उसे|उन्हें|इसे|इन्हें)\b", "PRON"), (r"\b(वह|वे|यह|ये)\b", "PR"),
       (r"(छोड़ा|छोड़े|छोड़ी)", "छोड़_"), (r"(चुका|चुके|चुकी)", "चुक_"), (r"(उठा|उठे|उठी)", "उठ_")]


def agr(s):
    for p, r in AGR:
        p = p.replace(r"\b(", r"(?<![^\s“])(").replace(r")\b", r")(?![^\s,।;”])")
        s = re.sub(p, r, s)
    return s


t = open(os.path.join(HERE, "divergences.md"), encoding="utf-8").read()
out, cur, forms, keep = [], None, [], 0
for block in re.split(r"\n(?=### )", t):
    if not block.startswith("### "):
        continue
    lines = block.split("\n")
    fs = [re.sub(r"\s*⟨diff vs first.*$", "", l.split(" :: ", 1)[1]) for l in lines[1:] if l.startswith("- [") and " :: " in l]
    if len({agr(f) for f in fs}) > 1:
        keep += 1
        print("\n".join(l[:400] for l in lines if l.strip()))
print("kept groups:", keep)
