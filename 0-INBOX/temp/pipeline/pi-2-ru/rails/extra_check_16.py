"""Extra checks for the Russian rails chapter 16: «ли», Latin outside variant brackets, double blank lines, CR, em
dash, «:-», quote balance, final punctuation (the matrix list lines (n) … end as the Pāli does), spacing, doubled words.
usage: python -I -X utf8 extra_check_16.py
"""
import pathlib
import re

OUT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-2-russian-plain-rails_split_chapters")
PALI = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-2_split_chapters")
name = "16-nanavibhango.md"
raw = (OUT / name).read_bytes()
t = raw.decode("utf-8")
p_lines = [ln for ln in (PALI / name).read_text(encoding="utf-8").splitlines() if ln.strip()]
r_lines = [ln for ln in t.splitlines() if ln.strip()]
assert len(p_lines) == len(r_lines)
probs = []
if b"\r" in raw:
    probs.append("CR")
if "\n\n\n" in t:
    probs.append("double blank line")
if "—" in t:
    probs.append("em dash")
if ":-" in t:
    probs.append(":-")
for i, (pl, ln) in enumerate(zip(p_lines, r_lines), 1):
    body = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln)
    pbody = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", pl)
    if re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", body):
        probs.append(f"line {i}: «ли»")
    nob = re.sub(r"\[[^\]]*\]", "", body)
    lat = re.findall(r"[A-Za-zĀ-ž]+", nob)
    if lat:
        probs.append(f"line {i}: Latin {lat[:5]}")
    if body.count("«") != body.count("»") and body.count("«") - body.count("»") != 1:
        probs.append(f"line {i}: «» unbalanced")
    p_end = pbody.rstrip()[-1:] if pbody.strip() else ""
    if body.strip() and not body.startswith("#"):
        if p_end in ".?" and not body.rstrip().endswith((".", "?", "]")):
            probs.append(f"line {i}: no final . or ?")
        if p_end not in ".?" and body.rstrip().endswith("."):
            probs.append(f"line {i}: final . where the Pāli has none")
    if "  " in body or " ," in body or " ." in body or ",," in body or ".." in body.replace("…", ""):
        probs.append(f"line {i}: spacing/punctuation")
    dw = re.search(r"\b(\w+) \1\b", body)
    if dw:
        probs.append(f"line {i}: doubled word {dw.group(0)}")
print(name, "OK" if not probs else probs)
