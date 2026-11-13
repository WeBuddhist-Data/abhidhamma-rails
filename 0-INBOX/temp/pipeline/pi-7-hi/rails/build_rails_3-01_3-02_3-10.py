"""pi-7 Paṭṭhāna, Hindi plain RAILS: builder for 3-01 (hetugocchaka), 3-02 (cūḷantaraduka), 3-10 (upādānagocchaka).

Uses the approved sample constants read-only (build_rails_sample as S). Lexicon and hand lines: lex_3-01_3-02_3-10.py.
run:  python -I -B -X utf8 build_rails_3-01_3-02_3-10.py [--report]
"""
import os, re, sys, importlib.util

RAILS = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails"
sys.path.insert(0, RAILS)
import build_rails_sample as S  # noqa: E402

_spec = importlib.util.spec_from_file_location("lex", os.path.join(RAILS, "lex_3-01_3-02_3-10.py"))
L = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L)

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI_DIR = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
OUT_DIR = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-hindi-plain-rails_split_chapters")
FILES = ["3-01-hetugocchaka.md", "3-02-culantaraduka.md", "3-10-upadanagocchaka.md"]

UNKNOWN = []          # (line, piece)
PO, PC = "\ue010", "\ue011"   # placeholder delimiters

# ------------------------------------------------------------------ helpers

def lower_initials(s):
    return S.lower_initials(s)


def join_and(hs):
    if len(hs) == 1:
        return hs[0]
    return ", ".join(hs[:-1]) + " और " + hs[-1]


def alt(d):
    return "|".join(re.escape(k) for k in sorted(d, key=len, reverse=True))


# ------------------------------------------------------------------ dyad items (frames)

ACC_ALT = alt(L.ACC_I)
NOM_ALT = alt(L.NOM_I)
DAT_ALT = alt(L.DAT_I)
PNOM_ALT = alt(L.PNOM_I)
FRAME_ALT = alt(L.FRAME)
COND_ALT = S.COND_ALT
CHAIN_SEP = r"(?:… |…pe… | …pe… | … | )"
CHAIN = rf"(?:{COND_ALT})(?:{CHAIN_SEP}(?:{COND_ALT}))*"

HEAD_RE = re.compile(rf"(?<![\w])({ACC_ALT}) dhammaṃ ({FRAME_ALT}) ({NOM_ALT}) (uppajjati|uppajjanti)(?: ({CHAIN}))?")
HEAD_TRUNC_RE = re.compile(rf"(?<![\w])({ACC_ALT}) dhammaṃ ({FRAME_ALT}) ({NOM_ALT})(?=…)")
PANHA_RE = re.compile(rf"(?<![\w])({PNOM_ALT}) ({DAT_ALT}) dhammassa(?: ({'|'.join(S.KEYS)})paccayena paccayo)?")
INS_RE = re.compile(rf"^(na )?({'|'.join(sorted(S.KEYS, key=len, reverse=True))})paccayena paccayo$")


def chain_hi(ch):
    return S.CH(ch)


def head_frame(m, st):
    acc, frame, nom, verb, ch = m.groups()
    nh, n = L.NOM_I[nom]
    st["frame"] = L.FRAME_ROOT[frame]
    out = f"{L.ACC_I[acc]} {L.FRAME[frame]} {nh}"
    if ch:
        out += f" {chain_hi(ch)}"
    return out + " " + S.ARISES[n]


def panha_head(m, st):
    pnom, dat, k = m.groups()
    h, g = L.PNOM_I[pnom]
    st["g"] = g
    out = f"{h}, {L.DAT_I[dat]}"
    if k:
        out += " " + S.INS(k, g)
    return out


# ------------------------------------------------------------------ noun-phrase lists (bodies)

UNIT_ALT_RE = None


def parse_units(words):
    """Greedy longest match of L.UNITS over a word list; 'ca' is skipped; L.MOD modifiers prefix the next unit.
    Returns (list of (hi, case, gn, has_ca), any_ca)."""
    out, i, any_ca, mods, coord = [], 0, False, [], False
    while i < len(words):
        if words[i] == "ca":
            if mods:
                coord = True
            else:
                any_ca = True
                if out:
                    out[-1] = out[-1][:3] + (True,)
            i += 1
            continue
        for n in range(min(8, len(words) - i), 0, -1):
            k = " ".join(words[i:i + n])
            if k in L.UNITS:
                h, case, gn = L.UNITS[k]
                ca = "ñca" in k or k.endswith(" ca") or " ca " in k
                any_ca = any_ca or ca
                if mods:
                    form = "f" if gn[0] == "f" else ("d" if case in ("N", "AN") and gn == "ms" else "o")
                    lead = [m for m in mods if "lead" in m]
                    adj = [m for m in mods if "lead" not in m]
                    hs = [m[form] if form in m else m["m" if form != "f" else "f"] for m in adj]
                    lh = " ".join(m["f" if form == "f" else "m"] for m in lead)
                    ah = (" और " if coord else ", ").join(hs)
                    h = " ".join(x for x in (lh, ah, h) if x)
                    mods, coord = [], False
                out.append((h, case, gn, ca))
                i += n
                break
            if (k in L.MOD or k in L.ADJF) and i + n < len(words):
                mods.append(dict(L.MOD[k], lead=1) if k in L.MOD else L.ADJF[k])
                if k.endswith("ñca"):
                    coord = True
                i += n
                break
        else:
            return None, any_ca
    if mods:
        return None, any_ca
    return out, any_ca


def np_hi(units, case):
    return join_and([u[0] for u in units])


def gn_of(units):
    if len(units) == 1:
        return units[0][2]
    return "mp" if any(u[2][0] == "m" for u in units) else "fp"


def dat_hi(units, any_ca):
    hs = [u[0] for u in units]
    if len(hs) == 2 and any_ca:
        return f"{hs[0]} के लिए और {hs[1]} के लिए"
    return join_and(hs) + " के लिए"


FRAME_POST = {"paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "nissāya": "के आश्रय से",
              "saṃsaṭṭha": "से घुल-मिलकर", "sampayutta": "से जुड़कर", "sahajāta": "के साथ जन्म लेकर"}
BODY_FRAME = {"paṭicca": "paṭicca", "paccayā": "paccayā", "nissāya": "nissāya", "saṃsaṭṭho": "saṃsaṭṭha",
              "saṃsaṭṭhā": "saṃsaṭṭha", "saṃsaṭṭhaṃ": "saṃsaṭṭha", "sampayutto": "sampayutta", "sampayuttā": "sampayutta",
              "sahajāto": "sahajāta", "sahajātā": "sahajāta"}
NUMVERB = {"ms": "उत्पन्न होता है", "fs": "उत्पन्न होती है", "mp": "उत्पन्न होते हैं", "fp": "उत्पन्न होती हैं"}


def clause(piece, st):
    core = piece.strip()
    if not core:
        return piece
    lead = piece[: len(piece) - len(piece.lstrip())]
    trail = piece[len(piece.rstrip()):]
    h = clause_core(core, st)
    if h is None:
        UNKNOWN.append((st["line"], core))
        h = "⟦" + core + "⟧"
    return lead + h + trail


def clause_core(core, st):
    if core in L.CLAUSE:
        return L.CLAUSE[core]
    if core in S.CLAUSE and core not in L.CLAUSE_SKIP_S:
        return S.CLAUSE[core]
    if core == ".":
        return "।"
    if core.endswith(".") and len(core) > 1:
        h = clause_core(core[:-1], st)
        return None if h is None else h + "।"
    if is_count(core):
        return count_hi(core)
    if re.fullmatch(CHAIN, core):
        return S.CH(core)
    m = INS_RE.match(core)
    if m:
        if st["g"] is None:
            return None
        return (S.NINS if m.group(1) else S.INS)(m.group(2), st["g"])
    words = core.split(" ")
    # optional prefix
    pre = ""
    for p in sorted(L.PREFIX, key=len, reverse=True):
        if core.startswith(p + " "):
            rest = core[len(p) + 1:]
            if rest in L.CLAUSE:
                return L.PREFIX[p] + " " + L.CLAUSE[rest]
            pre = L.PREFIX[p] + " "
            words = rest.split(" ")
            break
    m = re.fullmatch(r"(?:(ariyā) )?(?:(\S+) )?pahīne kilese( paccavekkhanti)?", " ".join(words))
    if m and (m.group(2) is None or m.group(2) in L.ADJF):
        return pre + ("आर्य " if m.group(1) else "") + (L.ADJF[m.group(2)]["o"] + " " if m.group(2) else "") + \
            "छोड़े जा चुके मन के क्लेशों पर" + (" पुनः विचार करते हैं" if m.group(3) else "")
    m = re.fullmatch(rf"({ACC_ALT}) dhammaṃ ({FRAME_ALT})", " ".join(words))
    if m:
        return pre + f"{L.ACC_I[m.group(1)]} {L.FRAME[m.group(2)]}"
    # X paṭicca / paccayā / nissāya / saṃsaṭṭhā … Y
    for i, w in enumerate(words):
        if w in BODY_FRAME and i > 0:
            a, _ = parse_units(words[:i])
            if a is None:
                return None
            fr = BODY_FRAME[w]
            st["frame"] = fr
            out = pre + np_hi(a, "A") + " " + FRAME_POST[fr]
            if i + 1 < len(words):
                b, _ = parse_units(words[i + 1:])
                if b is None:
                    return None
                out += " " + np_hi(b, "N")
            return out
    # X ārabbha / garuṃ katvā Y uppajjati/uppajjanti
    m = re.fullmatch(r"(.+?) (ārabbha|garuṃ katvā) (.+?)(?: (uppajjati|uppajjanti))?", " ".join(words))
    if m:
        a, _ = parse_units(m.group(1).split(" "))
        b, _ = parse_units(m.group(3).split(" "))
    if m and a is not None and b is not None:
        v = "विषय बनाकर" if m.group(2) == "ārabbha" else "महत्व देकर"
        oa = np_hi(a, "A")
        oa = "उसे" if oa == "उस" else oa + " को"
        return pre + f"{oa} {v} {np_hi(b, 'N')}" + (f" {NUMVERB[gn_of(b)]}" if m.group(4) else "")
    m = re.fullmatch(rf"({ACC_ALT}) dhammaṃ ({FRAME_ALT})", " ".join(words))
    if m:
        return pre + f"{L.ACC_I[m.group(1)]} {L.FRAME[m.group(2)]}"
    m = re.fullmatch(r"(.+?) (aniccato)", " ".join(words))
    if m:
        a, _ = parse_units(m.group(1).split(" "))
        if a is None:
            return None
        return pre + f"{np_hi(a, 'A')} को अनित्य"
    # [subject] OBJ [garuṃ katvā] assādeti abhinandati / paccavekkhati / paccavekkhanti
    if words[-1] == "assādeti":
        words = words + ["abhinandati§"]
    m = re.fullmatch(r"(?:(ariyā|sekkhā|arahā) )?(.+?)( garuṃ katvā)? (assādeti abhinandati§?|paccavekkhati|paccavekkhanti)", " ".join(words))
    if m:
        a, _ = parse_units(m.group(2).split(" "))
        if a is None:
            return None
        subj = {"ariyā": "आर्य ", "sekkhā": "सीखने के चरण वाले व्यक्ति ", "arahā": "अर्हत् ", None: ""}[m.group(1)]
        pl = len(a) > 1 or a[-1][2][1] == "p"
        o = np_hi(a, "A")
        if m.group(4) == "assādeti abhinandati§":
            if m.group(3):
                return pre + subj + f"{o} को महत्व देकर {'उनका' if pl else 'उसका'} रस लेता है"
            return pre + subj + f"{o} का रस लेता है"
        if m.group(4) == "assādeti abhinandati":
            if m.group(3):
                return pre + subj + f"{o} को महत्व देकर {'उनका' if pl else 'उसका'} रस लेता है, {'उनमें' if pl else 'उसमें'} आनंद लेता है"
            return pre + subj + f"{o} का रस लेता है, {'उनमें' if pl else 'उसमें'} आनंद लेता है"
        v = "पुनः विचार करता है" if m.group(4) == "paccavekkhati" else "पुनः विचार करते हैं"
        return pre + subj + (f"{o} को महत्व देकर {v}" if m.group(3) else f"{o} पर {v}")
    # OBJ upanissāya <act>
    m = re.fullmatch(r"(.+?) upanissāya (.+)", " ".join(words))
    if m:
        a, _ = parse_units(m.group(1).split(" "))
        act = L.CLAUSE.get(m.group(2))
        if a is None or act is None:
            return None
        return pre + f"{np_hi(a, 'A')} के प्रबल आश्रय से {act}"
    # SUBJ DAT [kiñci kāle] [na] Xpaccayena paccayo  (or SUBJ DAT alone)
    m = re.fullmatch(rf"(.+?)(?: (na))? ({'|'.join(sorted(S.KEYS, key=len, reverse=True))})paccayena paccayo", " ".join(words))
    body, ins = (" ".join(words), None)
    if m:
        body, ins = m.group(1), (m.group(2), m.group(3))
    units, any_ca = parse_units(body.split(" "))
    if units is None:
        return None
    subj = [u for u in units if u[1] in ("N", "AN")]
    dats = [u for u in units if u[1] == "D"]
    rest = [u for u in units if u[1] not in ("N", "AN", "D")]
    # order check: subjects first, then datives
    kinds = "".join("N" if u[1] in ("N", "AN") else "D" if u[1] == "D" else "X" for u in units)
    if rest or not re.fullmatch(r"N*D*", kinds):
        # an object list alone (elliptical, after …pe…)
        if all(u[1] in ("A", "N") for u in units) and ins is None and not dats:
            fr = st.get("frame")
            h = join_and([u[0] for u in units])
            if fr and (all(u[1] == "A" for u in units) or core in ("ekaṃ mahābhūtaṃ", "asaññasattānaṃ ekaṃ mahābhūtaṃ")):
                return pre + h + " " + FRAME_POST[fr]
            return pre + h
        return None
    out = []
    if subj:
        g = gn_of(subj)
        st["g"] = g
        sh = join_and([u[0] for u in subj])
        out.append(sh)
    if dats:
        dh = dat_hi(dats, any(u[3] for u in dats))
        if out and same_noun(out[-1], dh):
            out[-1] += ","
        out.append(dh)
    if ins:
        if st["g"] is None:
            return None
        out.append((S.NINS if ins[0] else S.INS)(ins[1], st["g"]))
    return pre + " ".join(out)


def has_ca_between(body, dats):
    # the Pāli dative list contains ca / ñca
    return bool(re.search(r"(ñca|\bca\b)", body.split(" ", 0)[0])) or ("ñca " in body or " ca " in body)


def stem1(w):
    return re.sub(r"(ों|ें|ाओं|ओं|े|ा|ी)$", "", w)


def same_noun(a, b):
    """comma after the subject where the same noun stands close on both sides (formulas §0, extended to the
    first three words of the dative: «लोभ का अभाव, द्वेष के अभाव …»)"""
    if a.endswith(","):
        return False
    wa = stem1(a.split(" ")[-1])
    return any(stem1(w) == wa for w in b.split(" ")[:3])


# ------------------------------------------------------------------ counts

COUNT_WORDS = set(S.P_ABL) | set(S.P_NABL) | set(S.P_LOC) | set(S.P_NLOC) | set(S.NUM) | set(L.NUM_EXTRA)


def is_count(text):
    toks = [t.strip() for t in re.split(rf"(…pe…|…|, |; | |\.|{PO}\d+{PC})", text)]
    toks = [t for t in toks if t and t not in ("…pe…", "…", ",", ";", ".") and not t.startswith(PO)]
    return bool(toks) and all(t in COUNT_WORDS for t in toks) and any(t in S.NUM or t in L.NUM_EXTRA for t in toks)


def count_hi(text):
    toks = [t for t in re.split(rf"(…pe…|…|, |; | |\.|{PO}\d+{PC})", text) if t]
    out = []
    for i, t in enumerate(toks):
        if t == " ":
            prev = toks[i - 1] if i else ""
            out.append(", " if prev in S.P_ABL or prev in S.P_NABL else " ")
        elif t == "…pe…":
            out.append("…")
        elif t == ".":
            out.append("।")
        elif t in ("…", ", ", "; ") or t.startswith(PO):
            out.append(t)
        else:
            for d in (S.P_ABL, S.P_NABL, S.P_LOC, S.P_NLOC, S.NUM, L.NUM_EXTRA):
                if t in d:
                    out.append(d[t])
                    break
            else:
                raise KeyError(t)
    return "".join(out)


# ------------------------------------------------------------------ line translator

def heading(line):
    m = re.fullmatch(r"(#+) (\*?)(.*?)(\*?)", line)
    hashes, st, body, en = m.groups()
    key = ("*" if st else "") + body
    if key in L.HEAD:
        h = L.HEAD[key]
    elif body in L.HEAD:
        h = L.HEAD[body]
    elif body in S.HEAD:
        h = S.HEAD[body]
    else:
        UNKNOWN.append((line, "HEADING " + body))
        h = "⟦" + body + "⟧"
    return f"{hashes} {st}{h}{en}"


def variants(line):
    inserts = []
    for v in re.findall(r"\{[^}]*\}", line):
        if v not in L.VARIANTS:
            UNKNOWN.append((line, "VARIANT " + v))
            continue
        kind, anchor = L.VARIANTS[v]
        line = line.replace(" " + v, "", 1) if (" " + v) in line else line.replace(v, "", 1)
        if kind.startswith("["):
            br = kind
        elif "(" in v:
            br = S.variant_hi(v, kind)
        else:
            br = f"[पाठभेद: {v[1:-1]}]"
        inserts.append((anchor, br))
    return line, inserts


def translate_line(line):
    if line.startswith("#"):
        return heading(line)
    if line in L.LINE:
        return L.LINE[line]
    line, inserts = variants(line)
    for a, b in L.SLIPS.items():
        line = line.replace(a, b)
    text = lower_initials(line)
    store = []
    st = {"g": LAST["g"], "frame": None, "line": line}
    try:
        return _translate(text, st, store, inserts, line)
    finally:
        LAST["g"] = st["g"]


LAST = {"g": None}


def _translate(text, st, store, inserts, line):

    def keep(h):
        store.append(h)
        return f"{PO}{len(store) - 1}{PC}"

    # notes
    def note(m):
        c = m.group(1)
        if c in L.NOTE:
            return keep("(" + L.NOTE[c] + ")")
        if c in S.NOTE:
            return keep("(" + S.NOTE[c] + ")")
        UNKNOWN.append((line, "NOTE " + c))
        return keep("(⟦" + c + "⟧)")
    text = re.sub(r"\(([^()]*[^\d().][^()]*)\)", note, text)
    # dative lists written with commas (knowledges, «gotrabhussa, vodānassa, …»): drop the commas
    text = re.sub(rf"(\w+(?:ssa|āya)), (?=(?:{L.DLIST_ALT})\b)", r"\1 ", text)
    # whole phrases
    for p in L.PHRASE_ORDER:
        if p in text:
            text = text.replace(p, keep(L.PHRASE[p]))
    # counts
    if is_count(text):
        return finish(count_hi(text), store, inserts)
    text = HEAD_RE.sub(lambda m: keep(head_frame(m, st)), text)
    text = HEAD_TRUNC_RE.sub(lambda m: keep(f"{L.ACC_I[m.group(1)]} {L.FRAME[m.group(2)]} {L.NOM_I[m.group(3)][0]}"), text)
    text = PANHA_RE.sub(lambda m: keep(panha_head(m, st)), text)
    out = []
    for tok in re.split(rf"( – |; |, |\. |…pe…|…|\.$|{PO}\d+{PC})", text):
        if tok in (" – ", "; ", ", ", "…"):
            out.append(tok)
        elif tok == ". ":
            out.append("। ")
        elif tok == ".":
            out.append("।")
        elif tok == "…pe…":
            out.append("…")
        elif tok.startswith(PO):
            out.append(tok)
        elif tok:
            for part in re.split(r"(\(\d+\))", tok):
                if not part.strip() or re.fullmatch(r"\(\d+\)", part):
                    out.append(part)
                else:
                    out.append(clause(part, st))
    return finish("".join(out), store, inserts)


def finish(s, store, inserts):
    for _ in range(3):
        s = re.sub(rf"{PO}(\d+){PC}", lambda m: store[int(m.group(1))], s)
    for anchor, br in inserts:
        if anchor and anchor in s:
            s = s.replace(anchor, anchor + " " + br, 1)
        else:
            s = s.rstrip("।") + " " + br + ("।" if s.endswith("।") else "")
    return s


ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")


def build_file(name):
    src = os.path.join(PALI_DIR, name)
    lines = open(src, encoding="utf-8").read().split("\n")
    out = []
    for ln in lines:
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        hi = translate_line(body)
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    with open(os.path.join(OUT_DIR, name), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or FILES
    for n in names:
        build_file(n)
    seen, cnt = {}, {}
    for line, piece in UNKNOWN:
        seen.setdefault(piece, line)
        cnt[piece] = cnt.get(piece, 0) + 1
    if "--report" in sys.argv:
        for piece in sorted(seen, key=lambda p: (not p.startswith("HEADING"), not p.startswith("VARIANT"), not p.startswith("NOTE"), -cnt[p], p)):
            print(f"{cnt[piece]}\t{piece}")
    if "--context" in sys.argv:
        for piece, line in seen.items():
            if not piece.startswith(("HEADING", "NOTE", "VARIANT")):
                print(f"{piece}\n    @ {line}")
    print(f"unknown pieces: {len(seen)}", file=sys.stderr)
