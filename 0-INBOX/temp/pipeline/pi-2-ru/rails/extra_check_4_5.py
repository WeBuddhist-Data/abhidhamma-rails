"""Extra checks for the Russian rails chapters 4 and 5: «ли», Latin outside variant brackets, double blank lines,
CR, em dash, quote balance, final punctuation.
usage: python -I -X utf8 extra_check_4_5.py
"""
import pathlib
import re

OUT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-2-russian-plain-rails_split_chapters")
for name in ("4-saccavibhango.md", "5-indriyavibhango.md"):
    raw = (OUT / name).read_bytes()
    t = raw.decode("utf-8")
    probs = []
    if b"\r" in raw:
        probs.append("CR")
    if "\n\n\n" in t:
        probs.append("double blank line")
    if "—" in t:
        probs.append("em dash")
    if ":-" in t:
        probs.append(":-")
    for i, ln in enumerate(t.splitlines(), 1):
        body = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln)
        if re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", body):
            probs.append(f"line {i}: «ли»")
        nob = re.sub(r"\[[^\]]*\]", "", body)
        lat = re.findall(r"[A-Za-zĀ-ž]+", nob)
        if lat:
            probs.append(f"line {i}: Latin {lat[:5]}")
        if body.count("«") != body.count("»"):
            probs.append(f"line {i}: «» unbalanced")
        if body.strip() and not body.startswith("#") and not body.rstrip().endswith((".", "?")):
            probs.append(f"line {i}: no final . or ?")
        if "  " in body or " ," in body or " ." in body:
            probs.append(f"line {i}: spacing")
    print(name, "OK" if not probs else probs)
