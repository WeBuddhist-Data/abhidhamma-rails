"""Russian plain zero-shot of pi-6 (Yamaka): chapter 3-04-ayatanayamaka.md (nirodhavāra).

Āyatana members, helpers and the driver come from build_3-01_ru / build_3-02_ru / build_3-03_ru (imported, never
edited); families A / B from build_2-01_ru / build_2-02_ru, the person / place shape from build_7-01_ru.
This module adds:
  - person units "sa-X-kānaṃ / a-X-kānaṃ [<plane>ā] cavantānaṃ" = «тех, кто умирает с X / без X [в …]»
    (3-01 descriptors + 2-01 "{P}ā cavantānaṃ"; patched into build_3-02_ru only inside ay4_units());
  - abbreviated beings answers "Rūpāvacarānaṃ…pe… kāmāvacarānaṃ…pe…." = «У существ мира форм… у существ …»;
  - the notes of the nirodhavāra (yatthaka / yassa-yatthaka / atītā pucchā / anāgatā pucchā).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_3-04_ru.py [--dry | --probe]
Import: importlib.import_module("build_3-04_ru")   (importing never writes any file)
"""
import contextlib
import importlib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

G = importlib.import_module("build_3-03_ru")    # ay3_units, abbr_line, AY3_CFG, tr_line
F = G.F                                         # build_3-02_ru: ay2_person_units, pe_question, AY2_CFG
A = G.A                                         # build_3-01_ru: members, AY_CFG
D = G.D                                         # build_2-01_ru: families A + B
C = G.C                                         # build_7-01_ru: person / place shape
E = G.E                                         # build_2-02_ru: PERSON_UNITS_2_02, pv_abbr
CHAPTER = "3-04-ayatanayamaka.md"
PREV_CHAPTERS = ["3-01-ayatanayamaka.md", "3-02-ayatanayamaka.md", "3-03-ayatanayamaka.md"]
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Family B: "sa-X-kānaṃ / a-X-kānaṃ [<plane>ā] cavantānaṃ"
# =============================================================================================
# 3-01: "sacakkhukānaṃ asotakānaṃ upapajjantānaṃ" = «тех, кто перерождается с глазом и без уха»; 2-01:
# "{P}ā cavantānaṃ" = «тех, кто умирает {in1}». So "sacakkhukānaṃ asotakānaṃ cavantānaṃ" = «тех, кто умирает с
# глазом и без уха»; "acakkhukānaṃ kāmāvacarā cavantānaṃ" = «тех, кто умирает без глаза в мире чувственных
# желаний» (descriptor, then the plane, as 3-02's REBORN_IN).
DYING = next(ru for rx, ru, _ in D.PERSON_UNITS if rx == r"{P}ā cavantānaṃ").replace("{in1}", "{desc}")
assert DYING == "тех, кто умирает {desc}", DYING
DYING_IN = DYING.replace("{desc}", "{desc} {in1}")
assert A.REBORN == "тех, кто перерождается {desc}" and F.REBORN_IN == A.REBORN + " {in1}"


def ay4_person_units(intro, planes=None, have=None):
    """build_3-02_ru.ay2_person_units with descriptors before "cavantānaṃ" / "<plane>ā cavantānaṃ" as well."""
    planes = A.AY_PLANES if planes is None else planes
    have = A.AY_HAVE if have is None else have
    toks = lower1(intro).split()
    pre = D._plane_re(planes)
    plane_acc = re.compile(pre + "aṃ")
    plane_abl = re.compile(pre + "ā")
    beings_rx = re.compile(pre + "ānaṃ")
    units, i = [], 0
    while i < len(toks):
        if toks[i:i + 2] == ["sabbesaṃ", "cavantānaṃ"]:                       # as 3-01
            units.append([A.ALL_DYING, True])
            i += 2
            continue
        j, descs = i, []
        while j < len(toks) and A.have_desc(toks[j], have):
            descs.append(A.have_desc(toks[j], have))
            j += 1
        if descs:
            desc = A.HAVE_JOIN.join(descs)
            nxt = toks[j + 1] if j + 1 < len(toks) else None
            cur = toks[j] if j < len(toks) else None
            if cur and plane_acc.fullmatch(cur) and nxt == "upapajjantānaṃ":              # as 3-02
                units.append([F.REBORN_IN.format(desc=desc, in1=planes[plane_acc.fullmatch(cur).group(1)]["in"]),
                              True])
                i = j + 2
            elif cur and plane_abl.fullmatch(cur) and nxt == "cavantānaṃ":                  # new
                units.append([DYING_IN.format(desc=desc, in1=planes[plane_abl.fullmatch(cur).group(1)]["in"]),
                              True])
                i = j + 2
            elif cur == "upapajjantānaṃ":                                                   # as 3-01
                units.append([A.REBORN.format(desc=desc), True])
                i = j + 1
            elif cur == "cavantānaṃ":                                                       # new
                units.append([DYING.format(desc=desc), True])
                i = j + 1
            else:
                raise ValueError(f"person intro not parsed: {intro!r}")
            continue
        beings = []
        while j < len(toks) and beings_rx.fullmatch(toks[j]):                  # as 3-01
            beings.append(planes[beings_rx.fullmatch(toks[j]).group(1)]["beings"])
            j += 1
        if beings:
            units.append([A.ru_and(beings), False])
            i = j
            continue
        rest = " ".join(toks[i:])                                               # 2-01 / 2-02 / 3-02 / 3-03 units
        for rx, ru, rel in F.UNITS:
            m = re.compile(rx.replace("{P}", pre)).match(rest)
            if m and (m.end() == len(rest) or rest[m.end()] == " "):
                g = [planes[x] for x in m.groups()] + [{"in": "", "beings": ""}] * 2
                units.append([ru.format(in1=g[0]["in"], in2=g[1]["in"], b1=g[0]["beings"], b2=g[1]["beings"]),
                              rel])
                i += len(rest[: m.end()].split())
                break
        else:
            raise ValueError(f"person intro not parsed at {toks[i]!r} in {intro!r}")
    out, k = [], 0                                                              # itaresaṃ: as 2-01
    while k < len(units):
        t, rel = units[k]
        if t == D.ITARESAM and k + 1 < len(units):
            nt, nrel = units[k + 1]
            t = D.ITARESAM + nt[3:] if nt.startswith("тех, кто") else f"{D.ITARESAM} {nt}"
            rel = nrel
            k += 1
        out.append([t, rel])
        k += 1
    return out


@contextlib.contextmanager
def ay4_units():
    """build_3-03_ru.ay3_units() with ay4_person_units in build_3-02_ru, for the block only."""
    old = F.ay2_person_units
    F.ay2_person_units = ay4_person_units
    try:
        with G.ay3_units():
            yield
    finally:
        F.ay2_person_units = old


# =============================================================================================
# Abbreviated beings answers: "Rūpāvacarānaṃ…pe… kāmāvacarānaṃ…pe…."
# =============================================================================================
# Each beings list stands for a whole answer sentence (3-01 person intro «У существ …»); the second and later
# lists are lower-case in the Pāli and stay so («… у существ …»). "…pe…." at the end = «…».
def beings_abbr(text, cfg):
    if "…pe… " not in text or "?" in text:
        return None
    body, end = (text[: -len("…pe….")], "…") if text.endswith("…pe….") else (text, "")
    parts = body.split("…pe… ")
    rx = re.compile(D._plane_re(cfg["planes"]) + "ānaṃ")
    out = []
    for n, p in enumerate(parts):
        toks = p.split()
        if all(rx.fullmatch(lower1(t)) for t in toks):
            ru = "у " + A.ru_and([cfg["planes"][rx.fullmatch(lower1(t)).group(1)]["beings"] for t in toks])
        elif n == len(parts) - 1 and not end and " tesaṃ " in p:
            ru = lower1(A.ay_answers(cap(p), cfg))
        else:
            return None
        out.append(ru)
    return cap("… ".join(out)) + end


# =============================================================================================
# Fixed lines (notes of the nirodhavāra), slips
# =============================================================================================
def _sec(key):
    """'Nirodhavāro' -> «в разделе о прекращении» (approved heading, prepositional case)."""
    h = B.SECTION_HEADINGS[key]
    assert h.startswith("Раздел "), h
    return "в разделе " + h[len("Раздел "):]


IN_UPPADA, IN_NIRODHA, IN_UPPADANIRODHA = _sec("Uppādavāro"), _sec("Nirodhavāro"), _sec("Uppādanirodhavāro")
assert IN_UPPADA == E.IN_UPPADAVARE
YASSAYATTHAKA = "раздел с «у кого где»"          # yassa yatthaka (A.YATTHAKA «раздел с «где»», A.YASSAKA)
ATITA_PUCCHA = "вопрос о прошлом"               # atītā pucchā (Atītavāro = Раздел о прошлом)
ANAGATA_PUCCHA = "вопрос о будущем"             # anāgatā pucchā (Anāgatavāro = Раздел о будущем)
VITTHARITA = "развёрнут"                         # vitthāritā; vitthāretabbā = C.VITTHARETABBAM «следует развернуть»
Q_PLACE_HEAD = C.Q_PLACE.split(",")[0]          # «Где {p1}»
_pv = A._pv


def _pq(body):
    return D.pv_question(lower1(body), A.AY_PV_SUBJ)[0]


# "(Uppādavārepi nirodhavārepi uppādanirodhavārepi atītā pucchā anulomampi paccanīkampi [paccaniyampi (sī. syā.
# ka.)] sadisaṃ.)"  anuloma / paccanīka = утвердительная / отрицательная форма (approved).
ATITA_NOTE = (f"({cap(IN_UPPADA)}, {IN_NIRODHA} и {IN_UPPADANIRODHA} {ATITA_PUCCHA} одинаков и в утвердительной, "
              f"и в отрицательной форме {D.variant_ru('paccaniyampi (sī. syā. ka.)', 'написания')}.)")
# "(Yathā uppādavāre yassa yatthake anāgatā pucchā vitthāritā, evaṃ nirodhepi vitthāretabbā)."
ANAGATA_NOTE_PALI = (" (Yathā uppādavāre yassa yatthake anāgatā pucchā vitthāritā, evaṃ nirodhepi "
                     "vitthāretabbā).")
ANAGATA_NOTE = (f" (Как {IN_UPPADA} {VITTHARITA} {ANAGATA_PUCCHA} в разделе с «у кого где», так же его "
                f"{C.VITTHARETABBAM} и {IN_NIRODHA}).")

AY4_FIXED = dict(G.AY3_FIXED)
AY4_FIXED.update({
    "Yattha cakkhāyatanaṃ nirujjhati…pe… (uppādepi nirodhepi uppādanirodhepi yatthakaṃ sabbattha sadisaṃ).":
        (f"{Q_PLACE_HEAD.format(p1=_pv('nirujjhati', 'cakkhu'))}… ({A.YATTHAKA} везде одинаков: {IN_UPPADA}, "
         f"{IN_NIRODHA}, {IN_UPPADANIRODHA})."),
    ("Yassa yattha cakkhāyatanaṃ nirujjhati tassa tattha sotāyatanaṃ nirujjhatīti…pe… ghānāyatanaṃ… rūpāyatanaṃ… "
     "manāyatanaṃ… dhammāyatanaṃ nirujjhatīti? (Yassa yatthakampi sadisaṃ vitthāretabbaṃ)."):
        (_pq("yassa yattha cakkhāyatanaṃ nirujjhati tassa tattha sotāyatanaṃ nirujjhatīti")[:-1] + "… "
         + "… ".join(A.AY_K[m]["nom"] for m in ("ghāna", "rūpa", "mana")) + "… " + _pv("nirujjhati", "dhamma")
         + f"? ({cap(YASSAYATTHAKA)} тоже {C.VITTHARETABBAM} одинаково)."),
    ("Yassa yattha cakkhāyatanaṃ na nirujjhati tassa tattha sotāyatanaṃ na nirujjhatīti…pe… "
     "(yassa yatthakampi yassakasadisaṃ)."):
        (_pq("yassa yattha cakkhāyatanaṃ na nirujjhati tassa tattha sotāyatanaṃ na nirujjhatīti")[:-1]
         + f"… ({YASSAYATTHAKA} тоже такой же, как {A.YASSAKA})."),
    ("Āmantā. (Uppādavārepi nirodhavārepi uppādanirodhavārepi atītā pucchā anulomampi paccanīkampi "
     "[paccaniyampi (sī. syā. ka.)] sadisaṃ.)"):
        B.AMANTA + " " + ATITA_NOTE,
})
assert C.VITTHARETABBAM == "следует развернуть" and A.YASSAKA == "раздел с «у кого»"

SLIPS = [   # (old, new, note): normalised for parsing; each must occur exactly once in the chapter
    ("sotāyatanaṃ na nirujjhatī ti…pe…", "sotāyatanaṃ na nirujjhatīti…pe…",
     "^6-3-131: 'nirujjhatī ti' written apart (= nirujjhatīti)"),
    ("rūpāyatanaṃ …pe… manāyatanaṃ", "rūpāyatanaṃ…pe… manāyatanaṃ",
     "^6-3-151: stray space before '…pe…' (spacing only)"),
    ("manāyatanaṃ na nirujjhissati, parinibbantānaṃ asaññasattānaṃ tesaṃ",
     "manāyatanaṃ na nirujjhissati. Parinibbantānaṃ asaññasattānaṃ tesaṃ",
     "^6-3-148: comma instead of the full stop between the two answer sentences (parallel lines have '.')"),
]


def preprocess(text):
    for old, new, note in SLIPS:
        if old in text:
            text = text.replace(old, new)
            SLIP_LOG.append(note)
    return text


AY4_CFG = dict(G.AY3_CFG)
AY4_CFG["fixed"] = AY4_FIXED


# =============================================================================================
# Driver
# =============================================================================================
def tr_line(text, cfg=None):
    cfg = AY4_CFG if cfg is None else cfg
    if not text.strip():
        return ""
    text = preprocess(text)
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    if text.startswith("#"):
        return G.tr_line(text, cfg)
    if text.endswith(ANAGATA_NOTE_PALI):
        return tr_line(text[: -len(ANAGATA_NOTE_PALI)], cfg) + ANAGATA_NOTE
    m = A.TAIL_RE.fullmatch(text)
    if m:
        return tr_line(m.group(1), cfg) + f" ({A.TAILS[m.group(2)]}){m.group(3)}"
    r = beings_abbr(text, cfg)
    if r is not None:
        return r
    return G.tr_line(text, cfg)


def translate_text(src, cfg=None):
    out = []
    with ay4_units():
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            out.append(tr_line(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("1", "в мире чувственных желаний"), ("1", "в мире форм"), ("1", "в мире без форм"),
    ("2", "умирают"), ("2", "перерождаются"), ("2", "достигают окончательного угасания"),
]


def check_previous_unchanged():
    """3-01, 3-02 and 3-03 must come out unchanged under the 3-04 person units."""
    pairs = []
    for name in PREV_CHAPTERS:
        src = (B.PALI_DIR / name).read_text(encoding="utf-8")
        on_disk = (B.OUT_DIR / name).read_text(encoding="utf-8")
        with ay4_units():
            if name.startswith("3-01"):
                again = A.translate_text(src, A.AY_CFG)
            elif name.startswith("3-02"):
                again = F.translate_text(src, F.AY2_CFG)
            else:
                again = G.translate_text(src, G.AY3_CFG)
        assert again == on_disk, f"{name} output would change with the 3-04 person units"
        pairs.append((src, on_disk))
    return pairs


def probe():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    bad = 0
    with ay4_units():
        for n, line in enumerate(src.split("\n"), 1):
            body, _ = B.ID_RE.match(line).groups()
            try:
                tr_line(body)
            except Exception as ex:  # noqa: BLE001
                bad += 1
                print(f"{n}: {type(ex).__name__}: {str(ex)[:300]}")
    print("failing lines:", bad)


def main():
    if "--probe" in sys.argv:
        probe()
        return
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(A.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    prev = check_previous_unchanged()
    for log in (SLIP_LOG, G.SLIP_LOG, F.SLIP_LOG, A.SLIP_LOG):
        log.clear()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for old, _, note in SLIPS:
        assert src.count(old) == 1, f"slip pattern must occur once: {note}"
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    pairs = [((B.PALI_DIR / n).read_text(encoding="utf-8"), (B.OUT_DIR / n).read_text(encoding="utf-8"))
             for n in B.SAMPLE_FILES + ["2-01-khandhayamaka.md", "2-02-khandhayamaka.md", "7-01-anusayayamaka.md"]]
    D.consistency(pairs + prev + [(src, ru)])
    if "--dry" in sys.argv:
        print(ru)
        return
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in dict.fromkeys(SLIP_LOG + G.SLIP_LOG + F.SLIP_LOG + A.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK (sample, 2-01, 2-02, 3-01 … 3-03, 7-01); "
          "3-01 … 3-03 unchanged")


if __name__ == "__main__":
    main()
