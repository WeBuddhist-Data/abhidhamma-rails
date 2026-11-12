# -*- coding: utf-8 -*-
"""Shared helpers for the Hindi builders of pi-2 chapters 8 (Sammappadhāna) and 18 (Dhammahadaya).

Imports the approved sample builder (read-only) for headings, assemble() and the dash constant.
Agreement markers inside predicate strings (resolved by inf()):
  {a}    -> ा / े / ी      (जुड़ा, जुड़े, जुड़ी; वाला, वाले, वाली)
  {ua}   -> आ / ए / ई      (हुआ, हुए, हुई)
  {ya}   -> या / ए / ई     (समाया, समाए, समाई)
  {kiya} -> किया / किए / की
"""
import os, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi"
sys.path.insert(0, HERE)
import build_ch1_sample_hi as S  # noqa: E402  (read-only import; does not write anything)

DASH = S.DASH
PALI_DIR = S.PALI_DIR
HI_DIR = S.HI_DIR


def _form(g, n):
    return "msg" if (g == "m" and n == "sg") else ("mpl" if g == "m" else "f")


def inf(s, g, n):
    f = _form(g, n)
    rep = {
        "{a}": {"msg": "ा", "mpl": "े", "f": "ी"}[f],
        "{ua}": {"msg": "आ", "mpl": "ए", "f": "ई"}[f],
        "{ya}": {"msg": "या", "mpl": "ए", "f": "ई"}[f],
        "{kiya}": {"msg": "किया", "mpl": "किए", "f": "की"}[f],
    }
    for k, v in rep.items():
        s = s.replace(k, v)
    return s


def cop(n):
    return "हैं" if n == "pl" else "है"


def hota(g, n):
    """होता है / होते हैं / होती है / होती हैं"""
    f = _form(g, n)
    return {"msg": "होता है", "mpl": "होते हैं", "f": "होती हैं" if n == "pl" else "होती है"}[f]


def hota_neg(g, n):
    f = _form(g, n)
    return {"msg": "नहीं होता", "mpl": "नहीं होते", "f": "नहीं होतीं" if n == "pl" else "नहीं होती"}[f]


def pron(n):
    """object pronoun for 'na vattabbā' after the subject was named"""
    return "उन्हें" if n == "pl" else "उसे"


class Subj:
    def __init__(self, nom, g, n, obl=None):
        self.nom, self.g, self.n = nom, g, n
        self.obl = obl or nom  # form before «को»


def nv_tail(preds, g, n):
    """'na vattabbā P1-tipi, P2-tipi, P3-tipi' after «<X> को»: «न P1 कहा जा सकता है, न P2, न P3».
    A predicate that itself starts with «न » (न दुःखद, न सुखद …) follows the pi-1 ^1-1389 wording:
    «…, और <pron> P भी नहीं कहा जा सकता»."""
    ps = [inf(p, g, n) for p in preds]
    plain = [p for p in ps if not p.startswith("न ")]
    neg = [p for p in ps if p.startswith("न ")]
    out = "न " + plain[0] + " कहा जा सकता है"
    for p in plain[1:]:
        out += ", न " + p
    for p in neg:
        out += f", और {pron(n)} {p} भी नहीं कहा जा सकता"
    return out


def nv(subj, preds, siya=False):
    """subject-initial: «<X> को न …» ; siya=True after the subject was named: «कभी उसे/उन्हें न …»"""
    if siya:
        return f"कभी {pron(subj.n)} " + nv_tail(preds, subj.g, subj.n)
    return f"{subj.obl} को " + nv_tail(preds, subj.g, subj.n)


def parts(subj, items):
    """Build one predicate chain. items: list of (mode, value)
      ("is", [P, …])      -> «P1 और P2 है/हैं»
      ("not", [P, …])     -> single: «P नहीं है/हैं»; several: «न P1 है/हैं, न P2, न P3»
      ("siya", P)         -> «कभी P होता है»
      ("siyanot", [P, …]) -> single: «कभी P नहीं होता»; several: «कभी न P1, न P2, न P3 होता है»
      ("siyanotbut", (P, Q)) -> «कभी P नहीं, पर Q होता है»
      ("siyanv", [P, …])  -> «कभी उसे न P1 कहा जा सकता है, …»
    The phrases are joined with ", "; a "not" group right after an "is" group gets «पर»."""
    g, n = subj.g, subj.n
    out, prev = [], None
    for mode, val in items:
        if mode == "is":
            ps = [inf(p, g, n) for p in val]
            j = ps[0] if len(ps) == 1 else ", ".join(ps[:-1]) + " और " + ps[-1]
            out.append(j + " " + cop(n))
        elif mode == "not":
            ps = [inf(p, g, n) for p in val]
            if len(ps) == 1:
                ph = ps[0] + " नहीं " + cop(n)
            else:
                ph = "न " + ps[0] + " " + cop(n) + "".join(", न " + p for p in ps[1:])
            out.append(("पर " if prev == "is" else "") + ph)
        elif mode == "siya":
            out.append("कभी " + inf(val, g, n) + " " + hota(g, n))
        elif mode == "siyanot":
            ps = [inf(p, g, n) for p in val]
            if len(ps) == 1:
                out.append("कभी " + ps[0] + " " + hota_neg(g, n))
            else:
                out.append("कभी न " + ", न ".join(ps) + " " + hota(g, n))
        elif mode == "siyanotbut":
            p, q = (inf(x, g, n) for x in val)
            out.append(f"कभी {p} नहीं, पर {q} {hota(g, n)}")
        elif mode == "siyanv":
            out.append(nv(subj, val, siya=True))
        else:
            raise ValueError(mode)
        prev = mode
    return ", ".join(out)


def sent(subj, items, end="।"):
    """«<subject> <chain>।»"""
    return f"{subj.nom} {parts(subj, items)}{end}"


_PI1 = None


def _pi1_corpus():
    global _PI1
    if _PI1 is None:
        d = S.PI1_HI_DIR
        _PI1 = "\n".join(open(os.path.join(d, f), encoding="utf-8-sig").read()
                         for f in sorted(os.listdir(d)) if f.endswith(".md"))
    return _PI1


def pi1_line(bid, strip_brackets=True):
    """Hindi text of the pi-1 line that carries block ID ^<bid> (ID removed, variant brackets removed)."""
    import re
    for line in _pi1_corpus().splitlines():
        if line.rstrip().endswith("^" + bid):
            t = line.rstrip()[: -len("^" + bid)].rstrip()
            return re.sub(r"\s*\[[^\]]*\]", "", t) if strip_brackets else t
    raise KeyError(bid)


def check_pi1(strings):
    """Every reused pi-1 string must occur byte for byte in the pi-1 Hindi (variant brackets ignored)."""
    import re
    corpus = re.sub(r"\s*\[[^\]]*\]", "", _pi1_corpus())
    missing = [s for s in strings if s not in corpus]
    assert not missing, "not found in pi-1 Hindi: " + " | ".join(missing)


def write_chapter(fname, hindi_lines):
    pali = open(os.path.join(PALI_DIR, fname), encoding="utf-8-sig").read().splitlines()
    text = S.assemble(pali, hindi_lines)
    with open(os.path.join(HI_DIR, fname), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("written:", fname, "lines", sum(1 for l in text.splitlines() if l.strip()))
