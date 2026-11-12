"""Pañhāpucchaka (question-and-answer) units across chapters: subjectless Pāli predicate units and their Hindi.

A Pañhāpucchaka answer line is split into units (Pāli at . , ; ?  and …pe…; Hindi at । , ; ? and …, with the
Hindi-internal commas of single labels protected). Lines whose unit counts differ are skipped (counted).
Only subjectless Pāli units (starting with siyā / na / no / neva, or a single word) are grouped, keyed by
their exact Pāli text; the Hindi is normalised for agreement (वाला/वाले/वाली -> वाल◌ …) and a leading added
subject (ये / वे / सभी क्षमताएँ / पाँचों समूह) is split off.

usage: python -I -X utf8 hz_pp_units.py [--bak] [out.md]
"""
import sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz_common
from hz_common import PARTS, pairs, short, BID

SPLIT_P = re.compile(r"(?<=[.;,?])\s+|\s*…pe…\s*")
SPLIT_H = re.compile(r"(?<=[।;,?])\s+|\s*…\s*")
PROT = "⁣"  # invisible separator used to protect internal commas
SUBJ = re.compile(r"^(ये|वे|सभी क्षमताएँ|पाँचों समूह) ")

NORM = {}
for k, toks in {"वाल◌": "वाला वाले वाली", "होत◌": "होता होते होती होतीं", "ह◌": "है हैं", "जुड़◌": "जुड़ा जुड़े जुड़ी",
                "हु◌": "हुआ हुए हुई", "घुल◌-मिल◌": "घुला-मिला घुले-मिले घुली-मिली", "समा◌": "समाया समाए समाई",
                "छोड़◌": "छोड़ा छोड़े छोड़ी", "कितन◌": "कितने कितनी", "जान◌": "जाना जाने जानी"}.items():
    for t in toks.split():
        NORM[t] = k
GEN = {"का", "के", "की"}
F_T = {"वाली", "होती", "होतीं", "जुड़ी", "हुई", "घुली-मिली", "समाई", "छोड़ी", "कितनी", "जानी"}
PL_T = {"हैं", "होतीं", "होते", "वाले", "हुए", "समाए", "जुड़े", "घुले-मिले", "कितने", "छोड़े", "जाने"}


def pp_lines(part):
    on = False
    for p, h in pairs(part):
        if "kati kusalā" in p:
            on = True
            continue
        if not on or p.startswith("#"):
            continue
        yield p, h
        if "Pañhāpucchakaṃ" in p or "niṭṭhit" in p:
            on = False


def protect_h(h):
    h = h.replace("न दुःखद, न सुखद", "न दुःखद" + PROT + " न सुखद")
    h = re.sub(r", (केवल सतत विचार)", PROT + r" \1", h)
    h = re.sub(r", (पर स्वयं|पर क्लेशों|पर मूल|पर आसक्ति|पर )", PROT + r" \1", h)
    # ', न X' inside one label (neither … nor); not the 'न “…”' lists and not after 'कहा जा सकता है'
    h = re.sub(r"(?<!कहा जा सकता है), न (?!“)", PROT + " न ", h)
    return h


def units(p, h):
    p = BID.sub("", p).strip()
    h = protect_h(BID.sub("", h).strip())
    up = [u for u in SPLIT_P.split(p) if u.strip()]
    uh = [u for u in SPLIT_H.split(h) if u.strip()]
    return up, uh


def subjectless(u):
    w = u.strip(" .,;?").split()
    if not w:
        return False
    return w[0].lower() in {"siyā", "na", "no", "neva"} or len(w) == 1 or w[0][0].islower()


def toks_norm(text):
    t = text.split(" ")
    out = []
    for i, w in enumerate(t):
        nxt = t[i + 1] if i + 1 < len(t) else ""
        core = w.rstrip("”")
        tail = w[len(core):]
        if nxt.startswith("मूलों") or nxt == "मूल":  # agrees with मूलों, not with the subject
            out.append(w); continue
        if core in GEN and (nxt.startswith("होत") or nxt in {"है", "हैं", "नहीं"}):
            out.append("क◌" + tail); continue
        out.append(NORM.get(core, core) + tail)
    return " ".join(out)


def hnorm(u):
    u = u.replace(PROT, ",").strip(" ।;,?")
    m = SUBJ.match(u)
    subj = m.group(1) if m else ""
    if m:
        u = u[m.end():]
    return subj, toks_norm(u)


def sig(text):
    ts = {w.rstrip("”") for w in text.split(" ")}
    ws = text.split(" ")
    # ignore tokens agreeing with मूलों
    for i, w in enumerate(ws[:-1]):
        if ws[i + 1].startswith("मूलों"):
            ts.discard(w)
    f = bool(ts & F_T)
    pl = bool(ts & PL_T) or ("होती" in ts and "हैं" in ts)
    if f:
        pl = "हैं" in ts or "होतीं" in ts
    return ("f" if f else "m") + (".pl" if pl else ".sg")


INFL = {
    "वाल◌": {"m.sg": "वाला", "m.pl": "वाले", "f.sg": "वाली", "f.pl": "वाली"},
    "होत◌": {"m.sg": "होता", "m.pl": "होते", "f.sg": "होती", "f.pl": "होती"},
    "ह◌": {"m.sg": "है", "m.pl": "हैं", "f.sg": "है", "f.pl": "हैं"},
    "जुड़◌": {"m.sg": "जुड़ा", "m.pl": "जुड़े", "f.sg": "जुड़ी", "f.pl": "जुड़ी"},
    "हु◌": {"m.sg": "हुआ", "m.pl": "हुए", "f.sg": "हुई", "f.pl": "हुई"},
    "घुल◌-मिल◌": {"m.sg": "घुला-मिला", "m.pl": "घुले-मिले", "f.sg": "घुली-मिली", "f.pl": "घुली-मिली"},
    "समा◌": {"m.sg": "समाया", "m.pl": "समाए", "f.sg": "समाई", "f.pl": "समाई"},
    "छोड़◌": {"m.sg": "छोड़ा", "m.pl": "छोड़े", "f.sg": "छोड़ी", "f.pl": "छोड़ी"},
    "क◌": {"m.sg": "का", "m.pl": "के", "f.sg": "की", "f.pl": "की"},
    "कितन◌": {"m.sg": "कितने", "m.pl": "कितने", "f.sg": "कितनी", "f.pl": "कितनी"},
    "जान◌": {"m.sg": "जाना", "m.pl": "जाने", "f.sg": "जानी", "f.pl": "जानी"},
}


def inflect(norm, s):
    out = []
    ws = norm.split(" ")
    for i, w in enumerate(ws):
        core = w.rstrip("”")
        tail = w[len(core):]
        if core in INFL:
            v = INFL[core][s]
            if core == "होत◌" and s == "f.pl" and i > 0 and ws[i - 1] == "नहीं" and (i + 1 == len(ws) or ws[i + 1] not in {"ह◌"}):
                v = "होतीं"
            out.append(v + tail)
        else:
            out.append(w)
    return " ".join(out)


def collect():
    grp = collections.defaultdict(lambda: collections.defaultdict(list))  # pali -> hnorm -> [(part, subj, raw)]
    skipped = collections.Counter()
    for part in PARTS[1:]:
        for p, h in pp_lines(part):
            up, uh = units(p, h)
            if len(up) != len(uh):
                skipped[short(part)] += 1
                continue
            for a, b in zip(up, uh):
                if not subjectless(a):
                    continue
                key = a.strip(" .,;?")
                key = key[0].lower() + key[1:]
                subj, hn = hnorm(b)
                grp[key][hn].append((part, subj, b.replace(PROT, ",").strip(" ।;,?")))
    return grp, skipped


def main():
    if "--bak" in sys.argv:
        hz_common.CUR["hdir"] = os.path.join(hz_common.HERE, "backup-pre-harmonise")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dest = args[0] if args else os.path.join(hz_common.HERE, "pp-units.md")
    grp, skipped = collect()
    out = ["# Pañhāpucchaka subjectless units: normalised Hindi variants", "",
           f"lines skipped (unit counts differ): {dict(skipped)}", ""]
    subj = collections.defaultdict(collections.Counter)
    n = 0
    for k, v in sorted(grp.items(), key=lambda kv: -sum(len(x) for x in kv[1].values())):
        for hn, locs in v.items():
            for part, s, raw in locs:
                subj[short(part)][s or "-"] += 1
        if len(v) < 2:
            continue
        n += 1
        out.append(f"### {k}")
        for hn, locs in sorted(v.items(), key=lambda kv: -len({l[0] for l in kv[1]})):
            chs = sorted({short(l[0]) for l in locs}, key=lambda c: int(c[2:]))
            out.append(f"- [{len(chs)} ch] {','.join(chs)} :: {hn}")
        out.append("")
    out.insert(3, f"groups with variants: {n}")
    out.insert(4, "added subjects per chapter: " + "; ".join(f"{c} {dict(d)}" for c, d in subj.items()))
    open(dest, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("groups", n, "skipped", dict(skipped), "->", dest)


if __name__ == "__main__":
    main()
