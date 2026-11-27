"""Classify every termbase-adherence miss of the pi-7 Burmese zero-shot (GENUINE / INFLECTION / ARTEFACT / CONTEXT) and
every miss the rails introduce. Model: pi-6-my/rails/classify_misses.py (read only, same logic); the Paṭṭhāna is extremely formulaic, so the rows are classified by rule (pattern + check), not
row by row.

usage: python3 -I -X utf8 classify_misses.py   (after build_rails.py + apply_termbase.py + the rails adherence run)
Inputs: rails/adherence-zeroshot.txt (fixed input), rails/adherence-rails.txt, rails/apply-log.tsv, the layer
(my_formulas_rails.py), the keyword map AI_translation/burmese/pi-7-keywords-by-reference-pali-burmese-plain.md.
Writes rails/adherence-classified.tsv (id, keyword, termbase term, text form, class, reason, ch, src).
  * GENUINE (a zero-shot miss the rails fix): the keyword passes in the rails segment, the rails segment differs from
    the zero-shot segment, and the change is attributed to a residual rule (apply-log.tsv, same id) or to a layer
    family whose reason names the keyword or the segment.
  * STALE (class ARTEFACT): a phrase entry of the termbase that copies the zero-shot wording of a member word which a
    locked decision changes: the phrase passes in the rails segment once the layer's / rules' own Burmese changes
    (old → new, the differing runs of each patch) are applied to the phrase term.
  * CONTEXT (a context sense): keyword, segment ids and rails text form (classify_rules.CONTEXT, empty for pi-7),
    only in the listed segments.
  * INFLECTION / ARTEFACT by rule (OTHER): keyword regex, a text-form regex that must match the segment (rails segment
    when the miss is left), the keyword map's form among the stated forms (where given), and a Pāli check.
Any other row is UNVERIFIED and the run fails (exit 1)."""
import difflib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402
import my_formulas_rails as L  # noqa: E402
from residual_rules import RULES  # noqa: E402
from classify_rules import OTHER, STALE_SUBS, STALE_NO, CONTEXT  # noqa: E402

PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
ZS = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
RL = ROOT / "AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters"
TB = ROOT / "AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md"
KMAP = ROOT / "AI_translation/burmese/pi-7-keywords-by-reference-pali-burmese-plain.md"
OUT = HERE / "adherence-classified.tsv"
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
MY = re.compile(r"[က-႟][က-႟ ]*[က-႟]")


def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for l in N(p.read_text(encoding="utf-8-sig")).splitlines():
            if not l.strip():
                continue
            buf.append(l)
            m = A.ID.search(l)
            if m:
                out[m.group(1)] = (p.name.split("-")[0].split(".")[0], " ".join(buf))
                buf = []
    return out


def misses(path):
    out = []
    for l in open(path, encoding="utf-8"):
        f = N(l).rstrip("\n").strip().split("\t")
        if len(f) == 3 and f[0][:1].isdigit():
            out.append(tuple(f))
    return out


def kmap():
    kv = {}
    for l in open(KMAP, encoding="utf-8"):
        m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
        if m:
            for x in m.group(2).split(", "):
                if "=" in x:
                    k, v = x.split("=", 1)
                    kv[(m.group(1), k)] = v
    return kv


def subs():
    """(old, new) Burmese runs of every layer patch and residual rule (the differing parts, Burmese only)."""
    pairs = set()
    items = [(o, n) for ps in L.PATCHES.values() for o, n, _, _ in ps] + [(r[3], r[4]) for r in RULES]
    for o, n in items:
        sm = difflib.SequenceMatcher(None, o, n, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                continue
            # widen to whole Burmese words around the change
            a0 = o.rfind(" ", 0, i1) + 1
            a1 = o.find(" ", i2) if o.find(" ", i2) >= 0 else len(o)
            b0 = n.rfind(" ", 0, j1) + 1
            b1 = n.find(" ", j2) if n.find(" ", j2) >= 0 else len(n)
            ow, nw = o[a0:a1].strip("\"'(){}၊။“”‘’,"), n[b0:b1].strip("\"'(){}၊။“”‘’,")
            if ow and MY.fullmatch(ow) and MY.fullmatch(nw or "က"):
                pairs.add((ow, nw))
        for ow, nw in zip(MY.findall(o), MY.findall(n)):
            if ow != nw:
                pairs.add((ow, nw))
    return sorted(pairs, key=lambda x: -len(x[0]))


END_OK = "(?=$| |…|၌|ကို|၏|သည်|သော|ခြင်း|မှု|အကြောင်း|ဖြင့်|နှင့်|တို့|၍|မှ|သို့)"


def WB(o):
    """«o» as whole Burmese words (start of the term or after a space; followed by the end, a space or a particle)."""
    start = "" if o.startswith(("ကို ", "၌ ", "သို့ ")) else r"(?:(?<=^)|(?<= ))"
    return re.compile(start + re.escape(o) + END_OK)


def pali_ok(check, text):
    if check is None:
        return True
    if check.startswith("!"):
        return re.search(check[1:], text) is None
    return re.search(check, text) is not None


def main():
    tb = A.parse_termbase(TB)
    P, Z, R = segs(PALI), segs(ZS), segs(RL)
    KV, SUBS = kmap(), sorted(set(subs()) | set(STALE_SUBS), key=lambda x: (-len(x[0]), x))
    applied = {}
    for l in open(HERE / "apply-log.tsv", encoding="utf-8").read().splitlines()[1:]:
        f = l.split("\t")
        applied.setdefault(f[1], set()).add(f[4].split(" ")[0])
    fam_reason = [(r.split(" ")[0], r) for ps in L.PATCHES.values() for _, _, _, r in ps]
    zs = misses(HERE / "adherence-zeroshot.txt")
    rl = misses(HERE / "adherence-rails.txt")
    zkeys = {(i, k) for i, k, _ in zs}
    rkeys = {(i, k) for i, k, _ in rl}
    todo = [(r, "zeroshot") for r in zs] + [(r, "rails") for r in rl if (r[0], r[1]) not in zkeys]
    rows, counts, bad = [], {}, []
    for (i, kw, term), src in todo:
        ch, zt = Z[i]
        rt, pt = R[i][1], P[i][1]
        left = (i, kw) in rkeys
        text = rt if left or src == "rails" else zt
        old = KV.get((i, kw), "")
        terms = tb.get(kw.lower(), [])
        row = None
        if not left and src == "zeroshot":                      # fixed in the rails
            fixed = any(A.occurs(t, rt) for t in terms)
            fam = sorted(applied.get(i, set()))
            if not fam:
                fam = sorted({f for f, r in fam_reason if kw.lower() in r.lower() or f"^{i}," in r + ","
                              or f"^{i} " in r or f"^{i})" in r})
            if not fam and rt != zt:
                fam = ["layer"]                                 # the segment was changed by the layer (no reason names it)
            if fixed and rt != zt and fam:
                row = (i, kw, term, old, "GENUINE", f"{'/'.join(fam[:3])}: zero-shot «{old}» → termbase «{term}»")
        if row is None and (left or src == "rails") and kw not in STALE_NO:
            for t in terms:                                     # a stale phrase entry
                app = [(o, n) for o, n in SUBS if WB(o).search(t) and n not in t]
                cands = [WB(o).sub(n, t) for o, n in app]
                cands += [WB(o2).sub(n2, WB(o).sub(n, t)) for k, (o, n) in enumerate(app) for o2, n2 in app[k + 1:]]
                t2 = next((c for c in cands if A.occurs(c, rt)), t)
                if t2 != t:
                    row = (i, kw, term, t2, "ARTEFACT", "STALE phrase entry: the term copies the zero-shot wording of "
                           "a member word that a locked decision changes (layer / rule); with that change applied the "
                           f"phrase reads «{t2}», which the rails segment has (termbase doubt: stale phrase entries)")
                    break
        if row is None and (left or src == "rails"):                 # CONTEXT senses, only in their segments
            for rkw, cids, form, reason in CONTEXT:
                fm = re.search(form, rt) if i in cids and re.fullmatch(rkw, kw) else None
                if fm:
                    row = (i, kw, term, fm.group(0).strip(), "CONTEXT", reason)
                    break
        if row is None:
            for rkw, cls, form, mforms, reason, pcheck in OTHER:
                if re.fullmatch(rkw, kw):
                    fm = re.search(form, text)
                    if fm and (mforms is None or old in mforms) and pali_ok(pcheck, pt):
                        note = "" if left or src == "rails" else (" [no longer a miss in the rails only because an "
                                                                   "unrelated change now puts the term in the segment]")
                        row = (i, kw, term, fm.group(0).strip(), cls, reason + note)
                        break
        if row is None:
            row = (i, kw, term, old, "UNVERIFIED", "no class")
            bad.append((i, kw, src, term, old))
        counts[row[4]] = counts.get(row[4], 0) + 1
        rows.append(row + (ch, src))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("id\tkeyword\ttermbase term\ttext form\tclass\treason\tch\tsrc\n")
        for r in rows:
            f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
    nz = sum(1 for r in rows if r[7] == "zeroshot")
    print(f"{nz} zero-shot misses + {len(rows) - nz} rails-introduced:",
          ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none")
    for i, kw, src, term, old in bad:
        print("UNVERIFIED", i, kw, src, "| TB", term[:60], "| map", old[:60])
    sys.exit(1 if bad else 0)


main()
