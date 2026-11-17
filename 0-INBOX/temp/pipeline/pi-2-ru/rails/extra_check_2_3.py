"""Extra checks for the Russian rails chapters 2 and 3: «ли», Latin outside variant brackets, double blank lines,
CR, em dash, quote balance.
usage: python -I -X utf8 extra_check_2_3.py
"""
import pathlib
import re

OUT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-2-russian-plain-rails_split_chapters")
for name in ("2-ayatanavibhango.md", "3-dhatuvibhango.md"):
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
    print(name, "OK" if not probs else probs)
