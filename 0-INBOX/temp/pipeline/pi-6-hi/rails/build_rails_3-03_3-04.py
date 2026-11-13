"""pi-6 Āyatanayamaka 3-03 / 3-04 (Pāli -> Hindi plain, RAILS).

Imports build_rails_sample read-only for every shared string; adds the āyatana words, the sense-organ
modifiers (harmonise I1) and the few formulas of these two files (see notes-3-03-3-04.md).
usage: python -I -X utf8 build_rails_3-03_3-04.py [3-03|3-04 ...]
"""
import re
import sys
import pathlib

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

FILES = {"3-03": "3-03-ayatanayamaka.md", "3-04": "3-04-ayatanayamaka.md"}

# ---------------------------------------------------------------- terms (termbase)
AY = {  # stem -> Hindi (all masculine: इंद्रिय-क्षेत्र)
    "cakkhāyatana": "आँख का इंद्रिय-क्षेत्र",
    "sotāyatana": "कान का इंद्रिय-क्षेत्र",
    "ghānāyatana": "नाक का इंद्रिय-क्षेत्र",
    "rūpāyatana": "दृश्य रूप का इंद्रिय-क्षेत्र",
    "manāyatana": "मन का इंद्रिय-क्षेत्र",
    "dhammāyatana": "मन के विषयों का इंद्रिय-क्षेत्र",
}
G = "m"
AY_RE = "(" + "|".join(AY) + ")(?:ñca|ṃ)"

CYCLE = {  # closing labels of a cycle
    "(Cakkhāyatanamūlakaṃ)": "(आँख के इंद्रिय-क्षेत्र पर आधारित)",
    "(Ghānāyatanamūlakaṃ)": "(नाक के इंद्रिय-क्षेत्र पर आधारित)",
    "(Rūpāyatanamūlakaṃ)": "(दृश्य रूप के इंद्रिय-क्षेत्र पर आधारित)",
    "(Manāyatanamūlakaṃ)": "(मन के इंद्रिय-क्षेत्र पर आधारित)",
}

# sense-organ modifiers (harmonise I1: «X वाले / X से रहित», several joined « और », before the place)
MODS = {
    "sacakkhukānaṃ": "आँख वाले", "acakkhukānaṃ": "आँख से रहित",
    "sasotakānaṃ": "कान वाले", "asotakānaṃ": "कान से रहित",
    "saghānakānaṃ": "नाक वाले", "aghānakānaṃ": "नाक से रहित",       # not in the termbase: built like sacakkhuka
    "sarūpakānaṃ": "भौतिक रूप वाले", "arūpakānaṃ": "भौतिक रूप से रहित",  # sarūpaka not in the termbase
    "sacittakānaṃ": "मन वाले", "acittakānaṃ": "मन से रहित",
}
MOD_JOIN = " और "
PLACE_OR = " या "          # two places sharing one participle (like catuvokāraṃ pañcavokāraṃ, harmonise I3)
CATUPANCA_BEINGS = "चार या पाँच समूहों वाले अस्तित्व के प्राणियों में"   # catuvokārānaṃ pañcavokārānaṃ

EXTRA_CLOSINGS = {"Uppādavāro.": "उत्पन्न होने का खंड।"}

# notes and irregular lines (whole sentences)
FIXED_SENTENCES = {
    # 3-04 ^6-3-132
    "(Uppādavārepi nirodhavārepi uppādanirodhavārepi atītā pucchā anulomampi paccanīkampi "
    "[paccaniyampi (sī. syā. ka.)] sadisaṃ.)":
        "(उत्पन्न होने के खंड में भी, समाप्त होने के खंड में भी और उत्पन्न होने और समाप्त होने के खंड में भी "
        "अतीत के प्रश्न सकारात्मक भी और नकारात्मक भी [वर्तनी-भेद (Sī., Syā., Ka.): paccaniyampi] समान हैं।)",
    # 3-04 ^6-3-141
    "(Yathā uppādavāre yassa yatthake anāgatā pucchā vitthāritā, evaṃ nirodhepi vitthāretabbā).":
        "(जैसे उत्पन्न होने के खंड में व्यक्ति और स्थान वाले भाग में भविष्य के प्रश्नों का विस्तार किया गया है, "
        "वैसे ही समाप्त होने में भी उनका विस्तार करना चाहिए)।",
}
FIXED_LINES = {
    # 3-04 ^6-3-124
    "Yattha cakkhāyatanaṃ nirujjhati…pe… (uppādepi nirodhepi uppādanirodhepi yatthakaṃ sabbattha sadisaṃ).":
        "जिस स्थान पर आँख का इंद्रिय-क्षेत्र समाप्त होता है… (उत्पन्न होने में भी, समाप्त होने में भी और "
        "उत्पन्न होने और समाप्त होने में भी स्थान वाला भाग सब जगह समान है)।",
    # 3-04 ^6-3-125
    "Yassa yattha cakkhāyatanaṃ nirujjhati tassa tattha sotāyatanaṃ nirujjhatīti…pe… ghānāyatanaṃ… rūpāyatanaṃ… "
    "manāyatanaṃ… dhammāyatanaṃ nirujjhatīti? (Yassa yatthakampi sadisaṃ vitthāretabbaṃ).":
        "जिस व्यक्ति में जिस स्थान पर आँख का इंद्रिय-क्षेत्र समाप्त होता है, क्या उसमें वहाँ कान का इंद्रिय-क्षेत्र "
        "समाप्त होता है… नाक का इंद्रिय-क्षेत्र… दृश्य रूप का इंद्रिय-क्षेत्र… मन का इंद्रिय-क्षेत्र… मन के विषयों का "
        "इंद्रिय-क्षेत्र समाप्त होता है? (व्यक्ति और स्थान वाले भाग का भी इसी के समान विस्तार करना चाहिए)।",
    # 3-04 ^6-3-131
    "Yassa yattha cakkhāyatanaṃ na nirujjhati tassa tattha sotāyatanaṃ na nirujjhatī ti…pe… "
    "(yassa yatthakampi yassakasadisaṃ).":
        "जिस व्यक्ति में जिस स्थान पर आँख का इंद्रिय-क्षेत्र समाप्त नहीं होता, क्या उसमें वहाँ कान का इंद्रिय-क्षेत्र "
        "समाप्त नहीं होता…? (व्यक्ति और स्थान वाला भाग भी व्यक्ति वाले भाग के समान है)।",
}
# source slips (reported): stray "=93" in 3-03 line 333
# and in 3-04 ^6-3-148 a comma where a new sentence starts (", parinibbantānaṃ asaññasattānaṃ tesaṃ").
SLIP_REPLACE = [(" =93 ", " "),
                ("na nirujjhissati, parinibbantānaṃ asaññasattānaṃ tesaṃ",
                 "na nirujjhissati. Parinibbantānaṃ asaññasattānaṃ tesaṃ"),
                ("rūpāyatanaṃ …pe…", "rūpāyatanaṃ…pe…")]   # 3-04 ^6-3-151: stray space before …pe…


# ---------------------------------------------------------------- helpers
def verb_tok(tok):
    """'uppajjissatīti' / 'na nirujjhatīti' / 'uppajjati' -> Hindi (masculine)."""
    neg = tok.startswith("na ")
    w = tok[3:] if neg else tok
    w = S.strip_ti(w, S._VERB_TI)
    return S.verb_hi(("na " if neg else "") + w, G)


def is_verb(w):
    try:
        S.strip_ti(w, S._VERB_TI)
        return True
    except ValueError:
        return False


def render_chain(text):
    """Āyatana words, '…pe…'/'…' and verbs, in Pāli order -> Hindi."""
    toks = re.findall(r"…pe…|…|\s+|[^\s…]+", text)
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if t == "…pe…" or t == "…":
            out.append("…")
        elif t.isspace():
            out.append(" ")
        elif t == "na" and i + 2 < len(toks) and is_verb(toks[i + 2]):
            out.append(verb_tok("na " + toks[i + 2]))
            i += 2
        elif re.fullmatch(AY_RE, t):
            out.append(AY[re.fullmatch(AY_RE, t).group(1)])
        elif is_verb(t):
            out.append(verb_tok(t))
        else:
            raise ValueError(f"chain token {t!r} in {text!r}")
        i += 1
    return "".join(out)


RELS = [("yassa vā pana yattha", "tassa tattha"), ("yassa yattha", "tassa tattha"),
        ("yassa vā pana", "tassa"), ("yassa", "tassa")]


def question(s):
    lab = ""
    m = re.match(r"\((Ka|Kha)\) ", s)
    if m:
        lab = S.LABELS[f"({m.group(1)})"] + " "
        s = s[m.end():]
    if not re.match(r"[Yy]assa[ …]", s) or not s.endswith("?"):
        return None
    body = "y" + s[1:-1]
    for rel, cor in RELS:
        if body.startswith(rel + " ") or body.startswith(rel + "…"):
            rest = body[len(rel):]
            rel_hi, cor_hi = S.REL_FRAMES[(rel, cor)]
            if f" {cor} " in rest:
                p1, p2 = rest.split(f" {cor} ", 1)
                return f"{lab}{rel_hi} {render_chain(p1.strip())}, क्या {cor_hi} {render_chain(p2.strip())}?"
            return f"{lab}{rel_hi}{render_chain(rest)}?"
    return None


def place_str(places):
    keys = [k for k, _ in places]
    if keys == ["catuvokāra", "pañcavokāra"]:
        keys = ["catupañcavokāra"]
    if len(set(c for _, c in places)) > 1:
        raise ValueError(f"mixed cases {places}")
    return PLACE_OR.join(S.PLACE_NOUN[k] for k in keys), places[0][1]


def who(s):
    s = s[0].lower() + s[1:]
    if s == "itaresaṃ":
        return S.ITARESAM_ALONE
    ye_chunks = {}

    def _ye(mm):
        pl = [S.PLACE_FORMS[p] for p in mm.group(1).split()]
        txt = S.YE_PARINIBBAYISSANTI.format(place=place_str(pl)[0])
        if mm.group(2):
            txt += " से " + S.PARTICIPLES[mm.group(2)]
        tok = f"§{len(ye_chunks)}"
        ye_chunks[tok] = txt
        return tok
    s = re.sub(r"ye ca ((?:\S+ )+?)upapajjitvā parinibbāyissanti(?: tesaṃ (cavantānaṃ|upapajjantānaṃ))?", _ye, s)
    s = re.sub(r"(§\d+)(?= |$)", r"\1", s)
    toks = s.split()
    chunks, pre, mods, places, i = [], [], [], [], 0

    def flush(core):
        parts = pre + ([MOD_JOIN.join(mods)] if mods else []) + [core]
        chunks.append(" ".join(parts))
        pre.clear(); mods.clear(); places.clear()
    while i < len(toks):
        w = toks[i]
        if w in ye_chunks:
            assert not (pre or mods or places), s
            chunks.append(ye_chunks[w])
        elif w == "sabbesaṃ":
            pre.append(S.SABBESAM)
        elif w == "itaresaṃ":
            pre.append(S.ITARESAM)
        elif w in MODS:
            mods.append(MODS[w])
        elif w in S.PLACE_FORMS:
            places.append(S.PLACE_FORMS[w])
        elif w == "catuvokārānaṃ" and i + 1 < len(toks) and toks[i + 1] == "pañcavokārānaṃ":
            assert not (mods or places), s
            flush(CATUPANCA_BEINGS)
            i += 1
        elif w in S.BEINGS and not places and not mods:
            flush(S.BEINGS[w])
        elif w == "pacchimabhavikānaṃ" and not places:
            j, ahead = i + 1, []
            while j < len(toks) and toks[j] in S.PLACE_FORMS:
                ahead.append(S.PLACE_FORMS[toks[j]])
                j += 1
            if j < len(toks) and toks[j] == "upapajjantānaṃ":
                core = S.PACCHIMA_UPAPAJJ
                if ahead:
                    core = f"{place_str(ahead)[0]} में {core}"
                flush(core)
                i = j
            else:
                assert not ahead, s
                flush(S.PARTICIPLES[w])
        elif w in S.PARTICIPLES:
            if places:
                p, case = place_str(places)
                flush(f"{p} {S.CASE_POST[case]} {S.PARTICIPLES[w]}")
            else:
                flush(S.PARTICIPLES[w])
        else:
            raise ValueError(f"who: unknown token {w!r} in {s!r}")
        i += 1
    if pre or mods or places:
        raise ValueError(f"who: dangling tokens in {s!r}")
    if len(chunks) == 1:
        return chunks[0]
    return S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]


def ay(stem):
    return AY[stem]


def answer(s):
    m = re.fullmatch(rf"(.+?) (tesaṃ tattha|tesaṃ) {AY_RE} ((?:na )?\S+), no ca (?:tesaṃ tattha|tesaṃ) {AY_RE} "
                     rf"((?:na )?\S+)[.,]", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        frame = S.BUT_BEINGS_T if t == "tesaṃ tattha" else S.BUT_BEINGS
        return frame.format(who=who(wh), k1=ay(k1), v1=S.verb_hi(v1, G), k2=ay(k2),
                            v2=S.verb_hi(v2, G, flip=True))
    m = re.fullmatch(rf"(.+?) (tesaṃ tattha|tesaṃ) {AY_RE} ((?:na )?\S+?),? {AY_RE} ((?:na )?\S+)\.", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        frame = S.BOTH_BEINGS_T if t == "tesaṃ tattha" else S.BOTH_BEINGS
        return frame.format(who=who(wh), k1=ay(k1), v1=S.verb_hi(v1, G), k2=ay(k2), v2=S.verb_hi(v2, G))
    return None


def abbreviated_answer(s):
    """'Rūpāvacarānaṃ…pe… kāmāvacarānaṃ…pe….' and '… …pe… <full both-clause>.'"""
    if "…pe…" not in s or s.startswith(("Yattha", "Yassa", "(")):
        return None
    parts = s.split("…pe…")
    out = []
    for k, p in enumerate(parts):
        p = p.strip()
        if k == len(parts) - 1:
            if p == ".":
                out[-1] += "।"
                break
            out.append(answer(p))
            break
        out.append(who(p) + "…")
    return " ".join(out)


def abbreviated_place_q(s):
    m = re.fullmatch(rf"Yattha {AY_RE} ((?:na )?\S+)…pe…\.", s)
    if m:
        return f"जिस स्थान पर {ay(m.group(1))} {S.verb_hi(m.group(2), G)}…।"
    return None


def sentence(s):
    if s in FIXED_SENTENCES:
        return FIXED_SENTENCES[s]
    if s in EXTRA_CLOSINGS:
        return EXTRA_CLOSINGS[s]
    if s in CYCLE:
        return CYCLE[s]
    if s in S.CLOSINGS:
        return S.CLOSINGS[s]
    for fn in (abbreviated_place_q, question, abbreviated_answer, answer):
        r = fn(s)
        if r:
            return r
    r = S.short_answer(s, G)
    if r:
        return r
    raise ValueError(f"no formula: {s}")


def text_line(line):
    for a, b in SLIP_REPLACE:
        line = line.replace(a, b)
    if line in FIXED_LINES:
        return FIXED_LINES[line]
    return " ".join(sentence(x) for x in S._split_sentences(line))


def translate_line(line):
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    line = line.strip()
    if line.startswith("#"):
        hashes, text = line.split(" ", 1)
        return f"{hashes} {S.HEADINGS[text]}{bid}"
    return text_line(line) + bid


def translate_text(t):
    out, prev_blank = [], True
    for line in t.splitlines():
        if not line.strip():
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        out.append(translate_line(line))
        prev_blank = False
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def main():
    keys = sys.argv[1:] or list(FILES)
    for k in keys:
        f = FILES[k]
        src = (S.PALI_DIR / f).read_text(encoding="utf-8")
        (S.HI_DIR / f).write_text(translate_text(src), encoding="utf-8", newline="\n")
        print("built", f)


if __name__ == "__main__":
    main()
