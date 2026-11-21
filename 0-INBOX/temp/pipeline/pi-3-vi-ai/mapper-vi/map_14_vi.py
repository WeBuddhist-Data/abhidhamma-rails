"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 14-terasamanayo (method 13:
«Asaṅgahitenasampayuttavippayuttapadaniddeso», association / dissociation of what is not included).

usage: python -I -X utf8 map_14_vi.py                    (writes 14-terasamanayo.mapped.md and verifies it)
       python -I -X utf8 map_14_vi.py dump [miss]        (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_14_vi.py show lo hi         (segments lo..hi with every pair; writes nothing)
       python -I -X utf8 map_14_vi.py cross              (keywords whose value differs from a finished chapter's
                                                         mapped file 3 … 11; reads only; writes nothing)

Importing this module writes nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> «X dhammehi» rule (as map_6_vi.py / map_10_vi.py) -> T14
(this script's table, on top of map_6_vi.T6: chapter 6 has the same reference lists and the same closing verse)
-> map_common_vi.value() (context3 -> KD -> alternatives / counts / «X saṅgahito» / «X dhammā» -> pi-2 chain ->
pi-1 chain). Reuses map_common_vi.py / map_sample_vi.py / map_6_vi.py tables read-only.
Conventions: pi-1 vi-map-conventions.md + notes, pi-2 vi-map-conventions-pi2.md + notes, vi-map-conventions-pi3.md,
finished pi-3 chapters (ch3-6 the inclusion relative clauses, ch7 / ch10 the association answers, ch8 / ch9 the
method nouns of the heading compound, ch6 the closing verse).

The frame of this method:
  «Rūpakkhandhena ye dhammā khandhasaṅgahena asaṅgahitā …, te dhammā katihi khandhehi … sampayuttā? Te dhammā
   tīhi khandhehi sampayuttā; ekenāyatanena ekāya dhātuyā kehici sampayuttā. Katihi vippayuttā? …»
  «Đối với khối vật chất, những hiện tượng nào không được gộp vào theo cách gộp vào khối, …, thì những hiện tượng
   đó gắn liền với bao nhiêu khối …? … gắn liền với một số hiện tượng trong một lĩnh vực nhận biết, một yếu tố.
   Không gắn liền với bao nhiêu? …»
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi")
from map_common_vi import (GAP, NDE, build_part, lc, present, read_keywords, read_vietnamese,  # noqa: E402
                           value, verify)
import map_sample_vi as S  # noqa: E402
from map_6_vi import T6  # noqa: E402

PART = "14-terasamanayo"
HERE = pathlib.Path(__file__).resolve().parent

_GL, _KGL = "gắn liền", "không gắn liền"

T14 = {
    **T6,
    # ---- heading «Phương pháp thứ mười ba»; colophon «…, phần thứ mười ba»
    "terasama": "thứ mười ba", "terasamo": "thứ mười ba",
    # ---- heading compound «Giải thích đề mục về điều gắn liền và điều không gắn liền dựa trên điều không được
    # gộp vào»: method nouns with the text's «điều» (map_8_vi.py / map_9_vi.py / map_12_vi.py; asaṅgahita map_3)
    "sampayutta": "điều " + _GL, "vippayutta": "điều " + _KGL, "asaṅgahita": "điều không được gộp vào",
    # ---- the association frame (predicates, «với» dropped; map_7_vi.py / map_10_vi.py)
    "sampayuttā": _GL, "vippayuttā": _KGL, "natthi": "không có",
    "kehici": "một số hiện tượng",     # «gắn liền với một số hiện tượng trong một lĩnh vực nhận biết, một yếu tố»
    # ---- dyad references that lost a negative prefix (positive part; pi-1 MATRIX X-niyā = đối tượng của X)
    "saṃyojaniyehi": "đối tượng của xiềng xích", "ganthaniyehi": "đối tượng của nút thắt",
    "oghaniyehi": "đối tượng của dòng lũ", "yoganiyehi": "đối tượng của ách",
    "nīvaraṇiyehi": "đối tượng của chướng ngại",
    # keyword with its own a- keeps the negative (asaṃkiliṭṭhehi «không bị phiền não làm vẩn đục»; KD asaṃkiliṭṭha)
    "asaṃkiliṭṭhehi": "không bị phiền não làm vẩn đục",
    "asaṃyojaniyehi": "không phải là đối tượng của xiềng xích",   # asaṃyojaniyehi dhammehi «các hiện tượng không phải là …»
    "pītikehi": "có sự hân hoan",      # sappītikehi «có sự hân hoan» (map_10_vi.py / map_11)
}

# per-segment choices (read from the segments)
OVERRIDES = {
    # asaññābhavena «sự hiện hữu không có tri giác» / nevasaññānāsaññābhavena «… không phải có tri giác cũng không
    # phải không có tri giác»: saññā of the bhava list = có tri giác (as map_6_vi.py ^3-205 / ^3-206)
    "3-449": {"saññā": "có tri giác"},
    "3-450": {"saññā": "có tri giác"},
}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def _value(kw, kws, text):
    """value() plus the «X dhammehi» rule of map_6_vi.py: «hiện tượng X» / «hiện tượng là X» where the segment has it
    contiguous, else «hiện tượng … X»."""
    k = lc(kw)
    if k not in T14 and k.endswith(" dhammehi"):
        xv = _value(kw.rsplit(" ", 1)[0], kws, text)
        for cand in (f"hiện tượng {xv}", f"hiện tượng là {xv}"):
            if present(cand, text):
                return cand
        return "hiện tượng" + GAP + xv
    return value(kw, kws, T14, text)


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return _value(kw, kws, vi.get(bid, ""))
    return resolve


def _patched(fn):
    """Run a map_sample_vi helper (dump / show) with this part's resolver."""
    saved = S.resolver_for
    S.resolver_for = lambda part: resolver()
    try:
        fn()
    finally:
        S.resolver_for = saved


def cross():
    """Keywords of this chapter whose value differs from the values of the finished chapters 3 … 11 (read only)."""
    other = {}
    for n in range(3, 12):
        for f in HERE.glob(f"{n}-*.mapped.md"):
            for line in f.read_text(encoding="utf-8").splitlines():
                if "] " not in line:
                    continue
                for pair in line.split("] ", 1)[1].split(", "):
                    if "=" in pair:
                        k, v = pair.split("=", 1)
                        other.setdefault(k, Counter())[(v, n)] += 1
    res = resolver()
    seen = set()
    for bid, kws in read_keywords(PART):
        for kw in kws:
            v = res(bid, kw, kws)
            if (kw, v) in seen:
                continue
            seen.add((kw, v))
            vals = other.get(kw, Counter())
            diff = sorted({(x, n) for (x, n) in vals if x != v})
            if diff:
                print(f"[{bid}] {kw}={v}  other: {diff[:6]}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        _patched(lambda: S.dump(PART, sys.argv[2:3] == ["miss"]))
    elif sys.argv[1:2] == ["show"]:
        _patched(lambda: S.show(PART, int(sys.argv[2]), int(sys.argv[3])))
    elif sys.argv[1:2] == ["cross"]:
        cross()
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
