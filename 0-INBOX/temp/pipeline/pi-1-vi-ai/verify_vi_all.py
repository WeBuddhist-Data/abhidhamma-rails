"""Checks for all 14 files of the Vietnamese pi-1 plain zero-shot after the harmonise pass.

usage: python -I -X utf8 verify_vi_all.py
- block IDs and per-segment line counts equal the Pāli part
- no BOM, no CR, no double blank lines, NFC, no em dash, no ":-", no «chánh niệm», no forbidden word
- per line: same number of "–" and "?" as the Pāli line; one "…" for every "…pe…"; same number of "[" brackets
- outside variant brackets: no Pāli letters (ā ī ū ṃ ṅ ñ ṭ ḍ ṇ ḷ) and no f / j / w / z (not in the Vietnamese alphabet)
- harmonise decisions: no «….» (four dots) and no «loại vật chất là» / «đây là loại vật chất» frame left
- protected text unchanged against backup-pre-harmonise/: preamble, 1-matika, the first 122 non-empty lines of 2-01
  (= ch2-01-sample.md line for line)
"""
import pathlib, re, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
VI = ROOT / "AI_translation" / "vietnamese" / "pi-1-vietnamese-plain-zeroshot_split_chapters"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
BAK = HERE / "backup-pre-harmonise"
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
FOREIGN = re.compile(r"[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶfjwzFJWZ]")


def segs(p):
    out, n = [], 0
    for l in p.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip():
            continue
        n += 1
        m = ID.search(l)
        if m:
            out.append((m.group(1), n))
            n = 0
    return out


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


bad = 0
for part in PARTS:
    name = part + ".md"
    f = VI / name
    raw = f.read_bytes()
    t = raw.decode("utf-8")
    errs = []
    if raw.startswith(b"\xef\xbb\xbf"):
        errs.append("BOM")
    if segs(PALI / name) != segs(f):
        errs.append("block IDs / segment line counts differ from the Pāli")
    if b"\r" in raw:
        errs.append("CR")
    if "\n\n\n" in t:
        errs.append("double blank line")
    if unicodedata.normalize("NFC", t) != t:
        errs.append("not NFC")
    if "—" in t or ":-" in t:
        errs.append("em dash or :-")
    if "chánh niệm" in t.lower():
        errs.append("chánh niệm")
    if "seed" in t.lower():
        errs.append("forbidden word")
    if "pe…" in t:
        errs.append("untranslated …pe…")
    if "…." in t:
        errs.append("four dots «….»")
    if "đây là loại vật chất" in t.lower():
        errs.append("old rūpa answer frame")
    info = t.count("loại vật chất là")  # 3-01 «Có loại vật chất là X» (Atthi rūpaṃ X): one «là», not the old frame
    for n, (p, line) in enumerate(zip(nonempty(PALI / name), nonempty(f)), 1):
        if p.count("–") != line.count("–") or p.count("—") != line.count("—") or p.count("?") != line.count("?"):
            errs.append(f"line {n}: dash/question-mark count differs")
        if p.count("…pe…") != line.count("…"):
            errs.append(f"line {n}: '…' count differs from '…pe…'")
        if p.count("[") != line.count("["):
            errs.append(f"line {n}: variant bracket count differs")
        if p.startswith("#") != line.startswith("#") or re.match(r"#*", p).group(0) != re.match(r"#*", line).group(0):
            errs.append(f"line {n}: heading level differs")
        if "loại vật chất là" in line and re.search(r"[Ii]daṃ taṃ rūpaṃ", p):
            errs.append(f"line {n}: old rūpa answer frame")
        body = ID.sub("", re.sub(r"\[[^\]]*\]", "", line))
        m = FOREIGN.search(body)
        if m:
            errs.append(f"line {n}: foreign letter {m.group(0)!r} in {body[max(0, m.start() - 30):m.start() + 30]!r}")
    # protected text
    if part in ("preamble", "1-matika"):
        if raw != (BAK / name).read_bytes():
            errs.append("protected file changed vs backup")
    if part.startswith("2-01"):
        if nonempty(f)[:122] != nonempty(BAK / name)[:122]:
            errs.append("first 122 non-empty lines changed vs backup")
        sample = (HERE / "ch2-01-sample.md").read_text(encoding="utf-8").splitlines()
        if t.splitlines()[:len(sample)] != sample:
            errs.append("ch2-01-sample.md no longer reproduced line for line")
    print(name, len(segs(f)), "segments", "OK" if not errs else errs[:5],
          f"(info: «loại vật chất là» x{info}, 3-01 'Atthi rūpaṃ X' lines)" if info else "")
    bad += bool(errs)
print("ALL OK" if not bad else f"{bad} problem(s)")
