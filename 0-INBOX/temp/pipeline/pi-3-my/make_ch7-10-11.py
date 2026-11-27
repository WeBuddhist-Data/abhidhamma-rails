"""Burmese zero-shot of pi-3 (Dhātukathā, «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»): 7-chatthanayo, 10-navamanayo, 11-dasamanayo.

usage: python3 -I -X utf8 make_ch7-10-11.py [chapter ...] [--list]
Model: make_sample.py. Every line is generated from the Pāli by my3_formulas.translate_line(); the frames of the
sampayoga methods (sixth, ninth, tenth) are added IN MEMORY here (my3_formulas.py is never edited): a sentence rule
in F.EXTRA_RULES, new headings, verse lines (F.FIXED), sigla and variants. A sentence no frame matches raises
F.Miss and stops the chapter (nothing is guessed); the lines that passed go to scratch/partial-<chapter>.
--list prints every new string (for notes-ch7-10-11.md).
Writes only the three chapter files (and scratch/partial-* on a stop).
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my3_formulas as F  # noqa: E402

F.install()          # the book-wide values of the consistency pass (harmonise-notes.md)

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-3_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["7-chatthanayo.md", "10-navamanayo.md", "11-dasamanayo.md"]

C, END, PE, DHP, CL = F.C, F.END, F.PE, F.DHP, F.CL
NEW = []         # (Pāli, Burmese) of every new string, for the notes


def new(p, my):
    NEW.append((p, my))
    return my


# ===================================================================================== words of the sampayoga frames
V_MY = {"sampayutt": F.SAMPAYUTTA_V, "vippayutt": F.VIPPAYUTTA_V}       # ယှဉ်တွဲ / ကင်းကွာ (my3_formulas)
WITH = F.WITH                 # instrumental of association: «X နှင့် ယှဉ်တွဲ» (pi-1 SAMP «နှင့် ယှဉ်တွဲသော»)
WITH_PL = F.WITH_PL
assert F.P1.SAMP == f"{WITH} {F.SAMPAYUTTA_V}သော" and F.P1.VIPP == f"{WITH} {F.VIPPAYUTTA_V}သော"
SOME = new("kehici (after counts: 'with some of')", F.SOME + WITH)      # «… တို့၏ အချို့နှင့် ယှဉ်တွဲသည်»
SOME_PL = "တို့" + SOME
NATTHI = new("Natthi.", F.NATTHI + END)          # pi-1 ^1-1433 «… natthi.» = «… မရှိ။»
F.witness("1", "^1-1433", "natthi", "မရှိ")
Q1_MY = f"{F.KHANDHA} {F.KATI}{C} {F.AYATANA} {F.KATI}{C} {F.DHATU} {F.KATI}{WITH_PL}"
new(f"{F.Q1_P} sampayutto?", f"{Q1_MY} {F.SAMPAYUTTA_V}သနည်း{END}")
KATIHI_MY = f"{F.KATI}{WITH_PL}"                    # Katihi vippayutto? = «မည်မျှတို့နှင့် ကင်းကွာသနည်း။»
new("Katihi vippayutto?", f"{KATIHI_MY} {F.VIPPAYUTTA_V}သနည်း{END}")
REL = "သော"                    # ye dhammā V = «… V-သော သဘောတရားများ» (pi-1 ^1-1115; F.REL)
THOSE = F.TE                   # te dhammā = «ထိုသဘောတရားများသည်» (pi-1 ^1-1091 «teva te dhammā» )
TEHI = F.TEHI[:-len(WITH)]     # tehi dhammehi = «ထိုသဘောတရားတို့နှင့်» (pi-1 ^1-1115, identical Pāli)
assert F.REL == f"{REL} {DHP}"
F.witness("1", "^1-1115", "Tehi dhammehi ye dhammā sampayuttā", f"{TEHI}{WITH} {F.SAMPAYUTTA_V}{REL} {DHP}၊")
F.witness("1", "^1-1091", "te dhammā saṅkhatā", THOSE + F.SUBJ_MARK)
new("X-ena ye dhammā sampayuttā", f"X{WITH} {F.SAMPAYUTTA_V}{REL} {DHP} (pattern of pi-1 ^1-1115)")
new("te dhammā (subject)", THOSE + F.SUBJ_MARK + " (pi-1 ^1-1091)")
# TERM_ALIAS «na hetusahetukā» (pi-3 spelling, ch7 ^3-279) -> pi-1 «na hetū sahetukā»: my3_formulas.install()


def verb(stem, num, q=False):
    return V_MY[stem] + ("ကြ" if num == "pl" else "") + ("သနည်း" if q else "သည်")


new("sampayutto / sampayuttā (pl). (statement)", f"{verb('sampayutt', 'sg')} / {verb('sampayutt', 'pl')}")
new("vippayutto / vippayuttā (pl). (statement)", f"{verb('vippayutt', 'sg')} / {verb('vippayutt', 'pl')}")

# ===================================================================================== headings, sigla, variants
# Saccādi, the siglum «(bahūsu)» (= pi-1 / pi-2 «Bahūsu»), the variants of ^3-397 / ^3-343: my3_formulas.install()
new("Saccādi (heading)", F.HEAD["Saccādi"])
new("(bahūsu) (sigla: in many editions)", F.SIGLA["bahūsu"])

# ===================================================================================== the summary verses (whole lines)
# every summary verse of the book: my3_formulas.install() (consistency pass, B5), in F.FIXED / F.VERSES

# ===================================================================================== instrumental -> nominative
INSTR_SPECIAL = {"pañcahi indriyehi": "pañcindriyāni", "pañcahi balehi": "pañca balāni",
                 "sattahi bojjhaṅgehi": "satta bojjhaṅgā", "ariyena aṭṭhaṅgikena maggena": "ariyo aṭṭhaṅgiko maggo",
                 "upādādhammehi": "upādā dhammā"}


def _known(k):
    try:
        F.dhamma_subject(k) if k not in F.SUBJ else None
        return True
    except F.Miss:
        return False


def _adj(w):
    """One word of an instrumental plural «… dhammehi» phrase -> its nominative plural."""
    if w in ("hetūhi",):
        return "hetū"
    if w.endswith("bhūhi"):
        return w[:-len("bhūhi")] + "bhuno"
    if w.endswith("īhi"):
        return w[:-len("īhi")] + "ino"
    if w.endswith("ehi"):
        return w[:-len("ehi")] + "ā"
    return w


def instr_nom(x):
    """«Vedanākkhandhena» / «Kusalehi dhammehi» / «avijjāya» -> «vedanākkhandho» / «kusalā dhammā» / «avijjā»."""
    k = x[0].lower() + x[1:]
    if k in INSTR_SPECIAL:
        return INSTR_SPECIAL[k]
    ws = k.split()
    if ws[-1] == "dhammehi":
        return " ".join(_adj(w) for w in ws[:-1]) + " dhammā"
    if k.endswith("dhammadhammehi"):
        return k[:-len("ehi")] + "ā"
    last, head = ws[-1], ws[:-1]
    cands = []
    if last.endswith("dhātuyā"):
        cands = [last[:-len("yā")]]
    elif last.endswith("āya"):
        cands = [last[:-len("ya")]]
    elif last.endswith("ehi"):
        cands = [last[:-len("ehi")] + "ā"]
    elif last.endswith("ena"):
        cands = [last[:-len("ena")] + "o", last[:-len("ena")] + "aṃ"]
    hits = [" ".join(head + [c]) for c in cands if " ".join(head + [c]) in F.SUBJ]
    if len(hits) != 1:
        if ws[-1].endswith("ehi") and len(ws) == 1:          # bare «Saṃyojanehi» (no «dhammehi»): = «saṃyojanā dhammā»
            return _adj(ws[0]) + " dhammā"
        raise F.Miss(f"instrumental: {x} -> {hits or cands}")
    return hits[0]


def instr_my(x):
    """Instrumental item (with an optional variant bracket) -> Burmese name (from the FINAL subjects)."""
    q, br, pos = F.var_split(x)
    nom = instr_nom(q)
    if br:
        ws = nom.split()
        ws.insert(pos, br)
        nom = " ".join(ws)
    return F.subject_my(nom)[0]


# ===================================================================================== the sentence frames
VR = r"(?P<v>sampayutt|vippayutt)(?P<e>oti|anti|āti|āni|o|aṃ|ā)"
END_NORM = {"oti": "o", "anti": "aṃ", "āti": "ā"}
Q_FULL = re.compile(rf"(?P<pre>.*?) ?{F.Q1_P} {VR}\?")
Q_BARE = re.compile(rf"(?P<pre>.*?) ?{VR}\?")
KATIHI = re.compile(rf"Katihi {VR}\?")
REL_RE = re.compile(r"(?P<x>.+?) ye dhammā(?: (?P<v1>sampayuttā|vippayuttā), tehi dhammehi(?: (?P<var>\[[^\]]+\]))?"
                    r" ye dhammā (?P<v2>sampayuttā|vippayuttā)(?:, te dhammā (?P<rest>.+))?)?")
TE_RE = re.compile(r"[Tt]e dhammā (?P<rest>.+)")
CLAUSE_RE = re.compile(rf"(?P<pre>.*?) ?(?P<c>{F.COUNTS_RE.pattern})(?P<k> kehici)? {VR}", re.IGNORECASE)
SEP_RE = re.compile(r"\s*(…pe…|…Pe…|…|\.\.(?= ))\s*")
SLIP_SPLIT = {   # ^3-269: two subjects without «…» between them (source slip): as written, no «၊» added (A2)
    "Dassanena pahātabbā dhammā bhāvanāya pahātabbā dhammā": ["Dassanena pahātabbā dhammā",
                                                             "bhāvanāya pahātabbā dhammā"]}
CTX = {}


def num_of(e, state):
    e = END_NORM.get(e, e)
    if e in ("o", "aṃ"):
        return "sg"
    if e == "āni":
        return "pl"
    if state is None:
        raise F.Miss("number of «-ā» unknown")
    return "sg" if state == "fsg" else state


def counts_my(cs, stem, num, some):
    """Counts of one clause -> «A n-ပါး၊ B m-ပါးတို့နှင့် V-သည်»; zero runs «V-ရာ A၊ B မရှိ»; kehici «… တို့၏ အချို့နှင့်»."""
    runs = []
    for kind, n in cs:
        z = n == 0
        if runs and runs[-1][0] == z:
            runs[-1][1].append((kind, n))
        else:
            runs.append((z, [(kind, n)]))
    out = []
    for z, r in runs:
        if z:
            if some:
                raise F.Miss("kehici with a zero run")
            out.append(f"{V_MY[stem]}{F.WHERE} " + f"{C} ".join(F.KIND[k] for k, _ in r) + f" {F.ZERO_TAIL}")
        else:
            lst = f"{C} ".join(F.count_my(k, n) for k, n in r)
            one = len(r) == 1 and r[0][1] == 1
            post = (SOME if one else SOME_PL) if some else (WITH if one else WITH_PL)
            out.append(f"{lst}{post} {verb(stem, num)}")
    return f"{C} ".join(out)


def subj_pre(pre):
    """Subject text before a verb or counts -> «Sသည်» (or «ထိုသဘောတရားများသည်»); sets the number state."""
    pre = pre.strip()
    if not pre:
        return ""
    if pre.lower() == "te dhammā":
        CTX["num"] = "pl"
        return THOSE + F.SUBJ_MARK
    if pre in SLIP_SPLIT:
        parts = []
        for s in SLIP_SPLIT[pre]:
            my, n = F.subjects_my(s)
            CTX["num"] = n
            parts.append(my + F.SUBJ_MARK)
        return " ".join(parts)
    my, n = F.subjects_my(pre)
    CTX["num"] = n
    return my + F.SUBJ_MARK


def answer_my(s):
    """«[S] COUNTS [kehici] V; COUNTS kehici V.» -> Burmese (clauses joined by «၊», the last ending «။»)."""
    if not s.endswith("."):
        raise F.Miss("answer: " + s)
    clauses = s[:-1].split("; ")
    out = []
    for i, cl in enumerate(clauses):
        m = CLAUSE_RE.fullmatch(cl)
        if not m:
            raise F.Miss("clause: " + cl)
        lead = ""
        if m["pre"]:
            if i:
                raise F.Miss("subject in a later clause: " + cl)
            lead = subj_pre(m["pre"]) + " "
        n = num_of(m["e"], CTX.get("num"))
        out.append(lead + counts_my(F.counts_parse(m["c"].strip()), m["v"], n, bool(m["k"])))
    return f"{C} ".join(out) + END


def question_my(ch):
    m = Q_FULL.fullmatch(ch)
    if m:
        lead = subj_pre(m["pre"])
        n = num_of(m["e"], CTX.get("num"))
        return (lead + " " if lead else "") + f"{Q1_MY} {verb(m['v'], n, q=True)}{END}"
    m = Q_BARE.fullmatch(ch)
    if m:
        lead = subj_pre(m["pre"])
        n = num_of(m["e"], CTX.get("num"))
        return (lead + " " if lead else "") + f"{verb(m['v'], n, q=True)}{END}"
    return None


def rel_v(v):
    return V_MY[v[:-1]]


def chunk_my(ch, last):
    """One chunk of a sentence (between ellipses)."""
    m = REL_RE.fullmatch(ch)
    if m:
        if m["v1"]:
            out = f"{instr_my(m['x'])}{WITH} {rel_v(m['v1'])}{REL} {DHP}"
        else:                                                    # verb elided: «Xနှင့်…» (B3, F.chain_item_my)
            if not CTX.get("relv"):
                raise F.Miss("relative without verb: " + ch)
            out = F.chain_item_my(instr_my(m["x"]))
        if m["v2"]:
            var = (" " + F.var_my(m["var"])) if m["var"] else ""
            out += f"{C} {TEHI}{WITH}{var} {rel_v(m['v2'])}{REL} {DHP}"
        if m["rest"]:
            CTX["num"] = "pl"
            q = question_my(m["rest"])
            if q is None or not m["rest"].startswith("katihi"):
                raise F.Miss("relative question: " + ch)
            out += f"{C} {THOSE}{F.SUBJ_MARK} {q}"
        return out
    if CTX.get("relv") and re.fullmatch(r"\S+ehi", ch):            # bare «Saṃyojanehi…»
        return F.bare_item_my(instr_my(ch))                     # B7 (F.bare_item_my)
    m = TE_RE.fullmatch(ch)
    if m and m["rest"].endswith("."):
        return answer_my(ch)
    if ch.endswith("?"):
        q = question_my(ch)
        if q is None:
            raise F.Miss("question: " + ch)
        return q
    if ch.endswith("."):
        return answer_my(ch)
    if last:
        raise F.Miss("chunk: " + ch)
    return subj_pre(ch)                                          # a subject before «…»


def sentence(s):
    if s == "Natthi.":
        return NATTHI
    m = KATIHI.fullmatch(s)
    if m:
        return f"{KATIHI_MY} {verb(m['v'], num_of(m['e'], CTX.get('num')), q=True)}{END}"
    r = re.search(r"ye dhammā (sampayuttā|vippayuttā)", s)
    CTX["relv"] = r[1] if r else None
    parts = SEP_RE.split(s)
    chunks, seps = parts[0::2], parts[1::2]
    out = [chunk_my(ch, i == len(chunks) - 1) for i, ch in enumerate(chunks)]
    res = out[0]
    for sep, x in zip(seps, out[1:]):
        res += (".." if sep == ".." else PE) + " " + x
    return res


def _rule(m):
    return sentence(m.group(0))


F.EXTRA_RULES.append((re.compile(r"(?s).+"), _rule))
_orig_translate = F.translate_line


def translate_line(line, bid=None):
    CTX.clear()
    return _orig_translate(line, bid)


# ===================================================================================== driver (as make_sample.py)
def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def bids(lines):
    bid_of, cur = {}, []
    for i, line in enumerate(lines):
        if line.strip():
            cur.append(i)
            m = F.ID_RE.search(line)
            if m:
                for j in cur:
                    bid_of[j] = m.group(1)
                cur = []
    return bid_of


def render(name):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    bid_of = bids(lines)
    return "\n".join(translate_line(l, bid_of.get(i)) for i, l in enumerate(lines)).rstrip("\n") + "\n"


def chapter(name):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    bid_of = bids(lines)
    done = []
    for i, line in enumerate(lines):
        try:
            done.append(translate_line(line, bid_of.get(i)))
        except F.Miss as e:
            part = HERE / "scratch" / ("partial-" + name)
            part.parent.mkdir(exist_ok=True)
            part.write_text("\n".join(done) + "\n", encoding="utf-8")
            print(f"STOP {name} line {i + 1}: {e}\n  {line[:200]}\n  ({len(done)} lines kept in {part})")
            return False
    write(name, "\n".join(done).rstrip("\n") + "\n")
    return True


if __name__ == "__main__":
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES_OUT
    ok = True
    for n in names:
        ok = chapter(n) and ok
    if "--list" in sys.argv:
        for p, m in NEW:
            print(f"{p} = {m}")
    sys.exit(0 if ok else 1)
