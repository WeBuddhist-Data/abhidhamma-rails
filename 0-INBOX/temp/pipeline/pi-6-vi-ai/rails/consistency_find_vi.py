"""pi-6 Yamaka Vietnamese rails consistency scan (coordinator-delegated, 2026-11-22).

Adapted from the pi-5 rails finder (pi-5-vi-ai/rails/consistency_find_vi.py and the find_divergences_vi.py it runs;
pi-5 files untouched). Reads ONLY the 44 rails chapter files, the 44 Pāli chapter files, the pre-fix copies in
rails/consistency/ and (read-only, nothing written on import) the member tables of the family builders.

Levels (each: identical key, differing Vietnamese; keys normalised: block ID and variant brackets stripped, spaces
collapsed, no space before punctuation or «…», first letter lowercased, trailing punctuation stripped):
 (L) whole lines;  (S) sentences (Pāli and Vietnamese split on «. ? ;» + space, only where both give the same count);
 (M) masked sentences: member names (khandha, āyatana, dhātu, sacca, saṅkhāra, dhamma / kusala…, indriya, anusaya)
     masked on both sides (Vietnamese: only the names of the members present in that Pāli sentence), the verb lexemes
     uppajj- / nirujjh- / anuse- / pajah- / parijān- masked (tense and negation kept), labels kept;
 (H) answer heads: masked Pāli before the first «tesaṃ / tassa / tattha» + member (else before the first member),
     Vietnamese before the first «thì» (else before the first M);  (B) the answer bodies after those heads;
 (P) editorial notes in round brackets (Pāli "(…)" vs Vietnamese "(…)", same count);
 (C) headings (number prefix stripped) and closing sentences (…vāro. / …niṭṭhito. / …vāre anulomaṃ. …);
 (N) note phrases: an identical Pāli phrase inside the editorial notes (pucchā, anulomampi paccanīkampi,
     vibhajitabbaṃ, one-subject sadisaṃ vitthāretabbaṃ): which Vietnamese variant each note uses;
 (Q) per line: the number of «?» equal; every Pāli cut "…?" / "…pe…?" has a Vietnamese «… không?»;
 (V) a nested run with a second run-level «và» («… cõi X và cõi Y và <group>», «… tầng thiền thứ X và … và <group>»).
«?» is kept in the keys ("…pe…?" and "…pe…." are different Pāli).

usage: python -I -X utf8 -B consistency_find_vi.py        (writes rails/divergences-rails.md: before and after)
"""
import collections
import difflib
import importlib
import os
import re
import sys
import unicodedata

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-6_split_chapters")
VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters")
BAK = os.path.join(HERE, "consistency")
OUT = os.path.join(HERE, "divergences-rails.md")
if HERE not in sys.path:
    sys.path.insert(0, HERE)

PARTS = sorted((f[:-3] for f in os.listdir(VDIR) if f.endswith(".md")),
               key=lambda s: (0, 0, 0) if s == "preamble" else tuple(int(x) for x in re.findall(r"\d+", s)[:2]) + (1,))

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
BID = re.compile(r"\s*\^[\w-]+\s*$")
VAR = re.compile(r"\s*\[[^\]]*\]")


# ------------------------------------------------------------------ members (read-only imports of the builders)
def _members():
    B = importlib.import_module("build_rails_2-01_vi")
    out = {}
    for pref, mod, names in (("2", "2-01", ["KHANDHA"]), ("3", "3-01", ["AYATANA"]), ("4", "4", ["DHATU_M"]),
                             ("5", "5-01", ["SACCA_B", "SACCA_A"]), ("6", "6-01", ["SANKHARA"]),
                             ("9", "9-01", ["DHAMMA"]), ("10", "10-01", ["INDRIYA"])):
        m = importlib.import_module(f"build_rails_{mod}_vi")
        out[pref] = [getattr(m, n) for n in names]
        assert all(isinstance(x, B.Members) for x in out[pref])
    an = importlib.import_module("build_rails_7-01_vi").ANUSAYA
    return out, an


MEMBERS, ANUSAYA = _members()
AN_RE = re.compile(r"^(" + "|".join(sorted(list(ANUSAYA) + ["kāmārāg"], key=len, reverse=True)) + r")ānusay")
AN_VI = sorted(ANUSAYA.values(), key=len, reverse=True)
SUFFIX = ("ñceva", "ñca", "nti", "īti", "āti", "ūti", "ti")
PUNCT = "“”‘’\"'()[],.;:?!…"
VERB_P = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(n?)(uppajj|nirujjh|anuse|pajah|parijān)")
VERB_V = re.compile(r"(?<!\w)(sinh khởi|chấm dứt|nằm sẵn|dứt bỏ|hiểu biết trọn vẹn)(?!\w)")


def yam(part):
    m = re.match(r"(\d+)-", part)
    return m.group(1) if m else ""


def mask_pali(s, part):
    """members -> M(+suffix); returns masked text and the set of Vietnamese names to mask"""
    y = yam(part)
    vis = set()
    toks = s.split(" ")
    for i, tok in enumerate(toks):
        core = tok.strip(PUNCT)
        if not core:
            continue
        lead = tok[:tok.find(core)]
        trail = tok[tok.find(core) + len(core):]
        hit = None
        if y == "7":
            if AN_RE.match(core.lower()):
                hit = "M"
                vis.update(AN_VI)
        else:
            for M in MEMBERS.get(y, []):
                try:
                    k = M.key(core)
                except ValueError:
                    continue
                hit = "M"
                vis.update(M.vi[k])
                break
        if hit:
            suf = next((e for e in SUFFIX if core.lower().endswith(e)), "")
            toks[i] = lead + "M" + suf + trail
    out = " ".join(toks)
    out = VERB_P.sub(lambda m: m.group(1) + "V", out)
    return out, vis


def mask_vi(s, vis):
    for name in sorted(vis, key=len, reverse=True):
        s = re.sub(r"(?<!\w)" + re.escape(name) + r"(?!\w)", "M", s)
        s = re.sub(r"(?<!\w)" + re.escape(name[:1].upper() + name[1:]) + r"(?!\w)", "M", s)
    return VERB_V.sub("V", s)


# ------------------------------------------------------------------ reading
def lines(path):
    return [l for l in open(path, encoding="utf-8-sig").read().splitlines() if l.strip()]


def vpath(part, before):
    if before:
        b = os.path.join(BAK, part + ".pre-fix.md")
        if os.path.exists(b):
            return b
    return os.path.join(VDIR, part + ".md")


def pairs(part, before=False):
    p = lines(os.path.join(PDIR, part + ".md"))
    v = lines(vpath(part, before))
    assert len(p) == len(v), (part, len(p), len(v))
    out, buf = [], []
    for a, b in zip(p, v):
        buf.append((a, b))
        m = ID.search(a)
        if m:
            out.extend((m.group(1), x, y) for x, y in buf)
            buf = []
    out.extend(("?", x, y) for x, y in buf)
    return out


def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = BID.sub("", s)
    s = VAR.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([,.;:?!…])", r"\1", s)
    return s


def low1(s):
    m = re.match(r"[“‘\"(]*", s)
    i = m.end()
    return s[:i] + s[i:i + 1].lower() + s[i + 1:]


def key(s):
    """«?» is kept: a cut "…pe…?" and a cut "…pe…." are not the same Pāli (rule: «… không?» vs «…»)"""
    return low1(norm(s)).rstrip(".;:,! ")


HEADPFX = re.compile(r"^#+\s*(?:\([0-9]+\)\s*)?(?:[0-9]+(?:-[0-9]+)?\.\s*)?")
SPLIT = re.compile(r"(?<=[?.;])\s+")
SPLIT_V = re.compile(r"(?<=[?.;])\s+")
HEAD_P = re.compile(r"\s(?:tesaṃ tattha|tassa tattha|tāsaṃ tattha|tesaṃ|tassa|tāsaṃ|tattha|ettha)\s"
                    r"(?=M|na\s|ca\s|cittaṃ|kusalaṃ|akusalaṃ|abyākataṃ|…)")
FIRST_M = re.compile(r"\sM")
# a nested run with an inner list and a second run-level «và» (clash 1): «… cõi X và cõi Y và <group>»,
# «… tầng thiền thứ X và tầng thiền thứ Y và <group>»; the inner «và» of a ye-clause closed by its verb is not one
NESTED_VA = re.compile(r"(?:cõi|tầng thiền) [^,;.]*? và (?:cõi|tầng thiền) (?:(?!sẽ |đang |ngay )[^,;.])*? và "
                       r"(?:những người|chúng sinh|các bậc)")
CLOSE_P = re.compile(r"(?i)(vāro|vāre anulomaṃ|vāre paṭilomaṃ|niṭṭhito|niṭṭhitā|niṭṭhitaṃ|vāro\.)\.?$")
PAREN = re.compile(r"\([^()]*\)")


def short(p):
    m = re.match(r"(\d+(?:-\d+)?)", p)
    return m.group(1) if m else p[:3]


def collect(before=False):
    G = {k: collections.defaultdict(lambda: collections.defaultdict(list)) for k in "LSMHBPC"}
    cuts, vav = [], []
    for part in PARTS:
        for sid, p, v in pairs(part, before):
            loc = f"{short(part)}:{sid}"
            if p.startswith("#"):
                G["C"][key(HEADPFX.sub("", norm(p)))][key(HEADPFX.sub("", norm(v)))].append(loc)
                continue
            G["L"][key(p)][key(v)].append(loc)
            # (Q) line level: every Pāli «?» kept; a cut "…?" / "…pe…?" = «… không?»; a cut "…pe…." has no «?»
            np_, nv_ = norm(p), norm(v)
            if np_.count("?") != nv_.count("?"):
                cuts.append((loc, f"Pāli «?»={np_.count('?')}, Vietnamese «?»={nv_.count('?')}: " + np_[:90],
                             nv_[:110]))
            if len(re.findall(r"…(?:pe…)?\?", np_)) > len(re.findall(r"…\s*không\?|không\?…", nv_)):
                cuts.append((loc, "cut «…?» without «… không?»: " + np_[:90], nv_[:110]))
            for m in NESTED_VA.finditer(nv_):
                vav.append((loc, np_[:120], nv_[max(0, m.start() - 60):m.end() + 30]))
            cp = [c for c in SPLIT.split(np_) if c.strip()]
            cv = [c for c in SPLIT_V.split(nv_) if c.strip()]
            pp, pv = PAREN.findall(np_), PAREN.findall(nv_)
            if len(pp) == len(pv):
                for a, b in zip(pp, pv):
                    G["P"][a][b].append(loc)
            if len(cp) != len(cv):
                continue
            for a, b in zip(cp, cv):
                if len(cp) > 1:
                    G["S"][key(a)][key(b)].append(loc)
                ma, vis = mask_pali(a, part)
                mb = mask_vi(b, vis)
                G["M"][key(ma)][key(mb)].append(loc)
                if CLOSE_P.search(a.strip()) and len(a) < 80:
                    G["C"][key(a)][key(b)].append(loc)
                if a.startswith("("):
                    continue
                # (H) heads and (B) bodies: Pāli before «tesaṃ / tassa / tattha + member», else before the first
                # member (nominative / anusaya heads); Vietnamese before the first «thì», else before the first M
                # (masking is token for token and names hold no comma and no «thì», so the unmasked heads are
                # cut at the same token / comma: heads are compared unmasked, bodies masked)
                h = HEAD_P.search(" " + ma)
                if h and h.start() > 0:
                    mh, pb = (" " + ma)[:h.start()].strip(), (" " + ma)[h.start():].strip()
                    hv = re.split(r",? thì ", mb, maxsplit=1)
                    rv = re.split(r",? thì ", b, maxsplit=1)
                else:
                    f = FIRST_M.search(" " + ma)
                    if not f or f.start() == 0 or re.match(r"\((?:Ka|Kha|Ga|Gha)\)", ma):
                        continue
                    mh, pb = (" " + ma)[:f.start()].strip(), (" " + ma)[f.start():].strip()
                    hv = re.split(r", (?=M)", mb, maxsplit=1)
                    if len(hv) != 2 or "thì" in hv[0]:
                        continue
                    n = hv[0].count(", ") + 1
                    rv = [", ".join(b.split(", ")[:n]), ", ".join(b.split(", ")[n:])]
                ph = " ".join(a.split(" ")[:len(mh.split(" "))])
                if len(hv) == 2 and len(rv) == 2 and len(ph) > 3:
                    G["H"][ph][rv[0].strip()].append(loc)
                    G["B"][key(pb)][key(hv[1].strip())].append(loc)
    return G, cuts, vav


# (N) note phrases: identical Pāli phrases inside the editorial notes, which Vietnamese variant each line uses
NOTE_PHRASES = [
    ("… pucchā (questions about a time)", r"(?<!dhātu)pucchā",
     [("«các câu hỏi về …»", r"[Cc]ác câu hỏi về (?:hiện tại|quá khứ|tương lai)"),
      ("bare «câu hỏi về …»", r"(?<![Cc]ác )(?<!cặp )[Cc]âu hỏi về (?:hiện tại|quá khứ|tương lai)")]),
    ("anulomampi paccanīkampi", r"anulomampi paccanīkampi",
     [("«cả chiều thuận lẫn chiều nghịch»", r"cả chiều thuận lẫn chiều nghịch"),
      ("«theo chiều thuận và chiều nghịch»", r"chiều thuận và chiều nghịch")]),
    ("vibhajitabbaṃ / vibhajitabbā", r"vibhajitabb",
     [("«nên phân tích»", r"nên phân tích"), ("«nên được phân tích»", r"nên được phân tích")]),
    ("(Yassa yatthakampi / Yassayatthakampi) sadisaṃ vitthāretabbaṃ (one subject)",
     r"\((?:Yassa yatthakampi|Yassayatthakampi) sadisaṃ vitthāretabbaṃ",
     [("«giống như vậy»", r"chi tiết giống như vậy"), ("«giống nhau»", r"chi tiết giống nhau")]),
]


def scan_notes(before=False):
    out, n = [], 0
    for name, prx, cands in NOTE_PHRASES:
        found = collections.defaultdict(list)
        for part in PARTS:
            for sid, p, v in pairs(part, before):
                if re.search(prx, p) and "(" in p:
                    for lab, vrx in cands:
                        if re.search(vrx, v):
                            found[lab].append(f"{short(part)}:{sid}")
        if len(found) > 1:
            n += 1
        out.append(f"### {name}")
        out += [f"- {lab}: [{len(l)}] {', '.join(l)}" for lab, l in found.items()] + [""]
    return out, n


def diff(a, b):
    ta, tb = a.split(), b.split()
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    return "; ".join(f"«{' '.join(ta[i1:i2])}» → «{' '.join(tb[j1:j2])}»"
                     for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal")


TITLES = {"L": "(L) whole lines", "S": "(S) sentences", "M": "(M) masked sentences (members, verb lexemes)",
          "H": "(H) answer heads (before «thì», or before the first member)",
          "B": "(B) answer bodies (after the head, masked)", "P": "(P) notes in round brackets",
          "C": "(C) headings and closing sentences"}


def report(groups, title, minlen=0):
    out = [f"## {title}", ""]
    n = 0
    for k, v in sorted(groups.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        if len(k) < minlen or len(v) < 2:
            continue
        n += 1
        out.append(f"### {k[:400]}")
        ranked = sorted(v.items(), key=lambda kv: -len(kv[1]))
        top = ranked[0][0]
        for r, locs in ranked:
            files = sorted({l.split(':')[0] for l in locs}, key=lambda x: [int(y) for y in re.findall(r"\d+", x)] or [0])
            d = "" if r == top else f"  ⟨diff: {diff(top, r)[:600]}⟩"
            out.append(f"- [{len(locs)}] ch {','.join(files)} ({', '.join(locs[:5])}) :: {r[:500]}{d}")
        out.append("")
    out.insert(1, f"groups: {n}")
    return out, n


def counts(G, cuts, vav):
    c = {k: sum(1 for kk, v in G[k].items() if len(v) > 1 and len(kk) >= (4 if k in "PC" else 8)) for k in G}
    c["Q"] = len(cuts)
    c["V"] = len(vav)
    return c


def main():
    Gb, cb, vb = collect(before=True)
    G, cuts, vav = collect(before=False)
    nb, na = counts(Gb, cb, vb), counts(G, cuts, vav)
    _, nb["N"] = scan_notes(before=True)
    onotes, na["N"] = scan_notes()
    order = "LSMHBPCNQV"
    head = ["# pi-6 Vietnamese rails: consistency scan (consistency_find_vi.py)", "",
            "Before = the pre-fix copies in rails/consistency/ (where a chapter was changed), otherwise the chapter; "
            "after = the chapters now. Every group listed below is explained in consistency-notes.md.", "",
            "| level | before | after |", "|---|---|---|"]
    for k in order:
        head.append(f"| {k} | {nb[k]} | {na[k]} |")
    head.append("")
    body = []
    for k in "CHBPLSM":
        o, _ = report(G[k], TITLES[k], minlen=4 if k in "PC" else 8)
        body += o
    body += ["## (N) note phrases: identical Pāli phrase in the editorial notes, Vietnamese variants used", "",
             f"phrases with more than one variant: {na['N']}", ""] + onotes
    body += ["## (Q) questions and cut questions: «?» count per line; «…?» in the Pāli vs «… không?»", "",
             f"cases: {len(cuts)}", ""]
    body += [f"- {l}: PI {a} || VI {b}" for l, a, b in cuts] + [""]
    body += ["## (V) nested run with a second run-level «và» («… cõi X và cõi Y và <group>»)", "",
             f"cases: {len(vav)}", ""]
    body += [f"- {l}: PI {a} || VI {b}" for l, a, b in vav] + [""]
    open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(head + body) + "\n")
    print("before", nb)
    print("after ", na, "->", OUT)


if __name__ == "__main__":
    main()
