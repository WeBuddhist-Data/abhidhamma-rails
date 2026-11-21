"""r3 review helper: compare (count, polarity) pairs per answer clause, Pāli vs Tịnh Sự, for ch 8-15.
Console only; writes nothing. Usage: python -I -X utf8 r3_ts_verbs.py
"""
import re
from pathlib import Path

ROOT = Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / r"AI_translation\pali\pi-3_split_chapters"
TS = ROOT / r"1-SOURCES\Translations\Vietnamese\vi-3-tinh_su.md"
CH = ["8-sattamanayo.md", "9-atthamanayo.md", "10-navamanayo.md", "11-dasamanayo.md",
      "12-ekadasamanayo.md", "13-dvadasamanayo.md", "14-terasamanayo.md", "15-cuddasamanayo.md"]
PN = {"ekena": 1, "ekāya": 1, "eken": 1, "dvīhi": 2, "dvīh": 2, "tīhi": 3, "catūhi": 4, "pañcahi": 5, "chahi": 6,
      "sattahi": 7, "aṭṭhahi": 8, "dasahi": 10, "dasah": 10, "ekādasahi": 11, "ekādasah": 11, "dvādasahi": 12,
      "dvādasah": 12, "terasahi": 13, "pannarasahi": 15, "soḷasahi": 16, "sattarasahi": 17, "aṭṭhārasahi": 18}
PNUM = re.compile(r"\b(ekena|ekāya|dvīhi|tīhi|catūhi|pañcahi|chahi|sattahi|aṭṭhahi|dasahi|ekādasahi|dvādasahi|terasahi|pannarasahi|soḷasahi|sattarasahi|aṭṭhārasahi) (khandhehi|khandhena|dhātūhi|dhātuyā)|\b(eken|dvīh|dasah|ekādasah|dvādasah)āyatane(?:na|hi)", re.I)
PVERB = re.compile(r"\b(asaṅgahitā|saṅgahitā|sampayuttā|vippayuttā)\b", re.I)
TNUM = re.compile(r"(\d+) ?(uẩn|u ẩn|xứ|giới)")
TVERB = re.compile(r"[Bb]ất yếu hiệp|[Yy]ếu hiệp|[Bb]ất tương ưng|[Tt]ương ưng")
VMAP = {"asaṅgahitā": "NG", "saṅgahitā": "G", "sampayuttā": "S", "vippayuttā": "V",
        "bất yếu hiệp": "NG", "yếu hiệp": "G", "bất tương ưng": "V", "tương ưng": "S"}
CAT = {"khandhehi": "K", "khandhena": "K", "dhātūhi": "D", "dhātuyā": "D", "uẩn": "K", "u ẩn": "K", "xứ": "A", "giới": "D"}


def p_pairs(s):
    out = []
    for cl in re.split(r"[;.?]", s):
        nums = []
        for m in PNUM.finditer(cl):
            if m.group(1): nums.append(f"{PN[m.group(1).lower()]}{CAT[m.group(2)]}")
            else: nums.append(f"{PN[m.group(3).lower()]}A")
        vs = PVERB.findall(cl)
        if nums:
            v = VMAP[vs[-1].lower()] if vs else "?"
            out += [(n, v) for n in nums]
    return out


def t_pairs(s):
    out = []
    for cl in re.split(r"[;.?!]", s):
        nums = [f"{m.group(1)}{CAT[m.group(2)]}" for m in TNUM.finditer(cl) if m.group(1) != "0"]
        vs = TVERB.findall(cl)
        if nums:
            v = VMAP[vs[-1].lower()] if vs else "?"
            out += [(n, v) for n in nums]
    return out


def main():
    txt = TS.read_text(encoding="utf-8")
    parts = re.split(r"!\[\[[^\]]*#\^(3-[0-9-]+)\]\]", txt)
    T = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
    for ch in CH:
        for b in re.split(r"\n\s*\n", (PDIR / ch).read_text(encoding="utf-8").strip()):
            m = re.search(r"\^(3-[0-9-]+)\s*$", b)
            if not m or b.startswith("#"):
                continue
            sid = m.group(1)
            first = b.split("\n")[0]
            # Pāli answer part only
            c = [x.start() for x in re.finditer(r"[Tt]e dhammā (?!katihi)|\bNatthi\b", first)]
            pa = p_pairs(first[min(c):]) if c else []
            ta = t_pairs(T.get(sid, ""))
            if [v for _, v in pa] != [v for _, v in ta]:
                print(sid, "\n   P ", pa, "\n   TS", ta)


if __name__ == "__main__":
    main()
