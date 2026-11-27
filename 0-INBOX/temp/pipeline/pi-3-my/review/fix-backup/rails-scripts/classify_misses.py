"""Classify every termbase-adherence miss of the pi-3 Burmese zero-shot: GENUINE / INFLECTION / ARTEFACT; and every
miss the rails introduce (a miss of the rails that the zero-shot did not have). Model: pi-2-my/rails/classify_misses.py.

usage: python3 -I -X utf8 classify_misses.py   (after build_rails.py + apply_termbase.py + the rails adherence run)
Inputs: rails/adherence-zeroshot.txt (fixed input), rails/adherence-rails.txt, rails/layer-log.tsv, rails/apply-log.tsv,
the zero-shot keyword map AI_translation/burmese/pi-3-keywords-by-reference-pali-burmese-plain.md (the zero-shot's own
form of each keyword in each segment) and termbase/decisions-A.tsv (the decided senses).
Writes rails/adherence-classified.tsv (id, keyword, termbase term, text form, class, reason, ch, src).
  * GENUINE row (zero-shot miss fixed in the rails): its keyword belongs to a family (FAM: keyword -> Lnn / Rnn) whose
    layer patch or residual rule was applied in this build (layer-log.tsv / apply-log.tsv); the zero-shot form (keyword
    map) occurs in the zero-shot segment; and the keyword passes in the rails segment (adherence_my.occurs).
  * INFLECTION / ARTEFACT row: its text-form regex must match the segment (zero-shot; rails for src=rails), the keyword
    map's zero-shot form for that keyword must be the same form (where given), and its Pāli check must match the
    segment's Pāli (a leading «!» means it must NOT match).
  * CONFLICT row (ARTEFACT, termbase conflict): an undecided entry that keeps the zero-shot form where the rails apply a
    decided entry of the same word; pi-3 has none (the six decisions agree with every other entry).
Any other row is UNVERIFIED and the run fails (exit 1).
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402

PALI = ROOT / "AI_translation/pali/pi-3_split_chapters"
ZS = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
RL = ROOT / "AI_translation/burmese/pi-3-burmese-plain-rails_split_chapters"
TB = ROOT / "AI_translation/burmese/pi-3-pali-burmese-termbase-plain.md"
KMAP = ROOT / "AI_translation/burmese/pi-3-keywords-by-reference-pali-burmese-plain.md"
DEC = HERE.parent / "termbase/decisions-A.tsv"
OUT = HERE / "adherence-classified.tsv"
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731

# --- GENUINE families: keyword -> layer patch (my_formulas_rails.py) / residual rule (apply_termbase.py).
# pi-3: none (no zero-shot miss is GENUINE; the layer and the rule list are empty).
FAM = {}

# --- INFLECTION / ARTEFACT families: (keyword regex, class, text-form regex, map form or None, reason, Pāli check)
OTHER = [
    (r"ādi", "INFLECTION", r"စသည့် ", "စသည်",
     "attributive «စသည့်» of the termbase «စသည်» before its noun: «Phassādisattakaṃ» = «တွေ့ထိမှု စသည့် ခုနစ်မျိုးတွဲ» "
     "(the heading «Khandhādi» = «အစုအဝေး စသည်» has the bare form; same word, my3_formulas HEAD)",
     r"ādisattakaṃ"),
    (r"uppannā|uppannehi", "ARTEFACT", r"မဖြစ်ပေါ်သေးသော", "ဖြစ်ပေါ်သော",
     "privative: the keyword is the fragment of Anuppannā / Anuppannehi «မဖြစ်ပေါ်သေးသော» (style rule: privative a- / "
     "an- = «မ» + verb; decision uppannā|0 / uppannehi|0: «ဖြစ်ပေါ်သော» is only the positive part of the fragment); no "
     "free Uppann- word in the segment",
     r"(?s)^(?!.*\b[Uu]ppann).*\b[Aa]nuppann"),
    (r"pariyāpannā|pariyāpannehi", "ARTEFACT", r"ဘဝဘုံတို့၌ အကျုံးမဝင်သော", "ဘဝဘုံတို့၌ အကျုံးဝင်သော",
     "privative: the keyword is the positive part of apariyāpannā / apariyāpannehi «ဘဝဘုံတို့၌ အကျုံးမဝင်သော» (style rule: "
     "privative a- = «မ» + verb, inside the termbase phrase); no free pariyāpann- word in the segment",
     r"(?s)^(?!.*\bpariyāpann).*\bapariyāpann"),
]
CONFLICT = []  # (keyword regex, decided headword|sense applied, what)


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


def pali_ok(check, text):
    if check is None:
        return True
    if check.startswith("!"):
        return re.search(check[1:], text) is None
    return re.search(check, text) is not None


def misses(path):
    out = []
    for l in open(path, encoding="utf-8"):
        f = N(l).rstrip("\n").strip().split("\t")
        if len(f) == 3 and f[0][:1].isdigit():
            out.append(tuple(f))
    return out


def applied_ids():
    ids = set()
    for name in ("layer-log.tsv", "apply-log.tsv"):
        for l in open(HERE / name, encoding="utf-8").read().splitlines()[1:]:
            ids.update(re.findall(r"\b([LR]\d\d?)\b", l.split("\t")[-1][:4]))
    return ids


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


def decided():
    d = {}
    for l in open(DEC, encoding="utf-8"):
        f = N(l).rstrip("\n").split("\t")
        if len(f) >= 2 and "|" in f[0] and not f[0].startswith("#"):
            d[f[0]] = f[1]
    return d


def main():
    tb = A.parse_termbase(TB)
    P, Z, R = segs(PALI), segs(ZS), segs(RL)
    done, KV, DECI = applied_ids(), kmap(), decided()
    zs = misses(HERE / "adherence-zeroshot.txt")
    rl = misses(HERE / "adherence-rails.txt")
    zkeys = {(i, k) for i, k, _ in zs}
    rkeys = {(i, k) for i, k, _ in rl}
    todo = [(r, "zeroshot") for r in zs] + [(r, "rails") for r in rl if (r[0], r[1]) not in zkeys]
    rows, counts, bad = [], {}, 0
    for (i, kw, term), src in todo:
        ch, zt = Z[i]
        rt, pt = R[i][1], P[i][1]
        left = (i, kw) in rkeys
        text = rt if left or src == "rails" else zt
        old = KV.get((i, kw), "")
        row = None
        if not left and src == "zeroshot":                      # fixed in the rails: must be a GENUINE family
            lid = FAM.get(kw)
            fixed = any(A.occurs(t, rt) for t in tb.get(kw.lower(), []))
            seen = bool(old) and (A.occurs(old, zt) or re.sub(r"(?:သည်|၏)$", "", old) in zt)
            if lid and lid in done and fixed and seen:
                row = (i, kw, term, old, "GENUINE", f"{lid}: zero-shot «{old}» → termbase «{term}»")
        if row is None and (left or src == "rails"):
            for rkw, cls, form, mform, reason, pcheck in OTHER:
                if re.fullmatch(rkw, kw):
                    fm = re.search(form, text)
                    if fm and (mform is None or old == mform) and pali_ok(pcheck, pt):
                        row = (i, kw, term, fm.group(0).strip(), cls, reason)
                        break
            if row is None:
                for rkw, dkey, what in CONFLICT:
                    dterm = DECI.get(dkey)
                    if re.fullmatch(rkw, kw) and dterm and A.occurs(dterm, rt) and \
                            re.search(rf"(?i){re.escape(kw.split()[-1])}", pt):
                        row = (i, kw, term, dterm, "ARTEFACT",
                               f"termbase conflict: the undecided entry «{term}» keeps the zero-shot form; the rails apply the "
                               f"decided {dkey} «{dterm}» ({what}); termbase doubt")
                        break
        if row is None:
            row = (i, kw, term, "", "UNVERIFIED", "no class")
        bad += row[4] == "UNVERIFIED"
        counts[row[4]] = counts.get(row[4], 0) + 1
        rows.append(row + (ch, src))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("id\tkeyword\ttermbase term\ttext form\tclass\treason\tch\tsrc\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    nz = sum(1 for r in rows if r[7] == "zeroshot")
    print(f"{nz} zero-shot misses + {len(rows) - nz} rails-introduced:",
          ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none")
    for r in rows:
        if r[4] == "UNVERIFIED":
            print("UNVERIFIED", r[0], r[1], r[7], "|", r[2])
    sys.exit(1 if bad else 0)


main()
