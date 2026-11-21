"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 7-chatthanayo (method 6: association /
dissociation, «Sampayogavippayogapadaniddeso»).

usage: python -I -X utf8 map_7_vi.py                     (writes 7-chatthanayo.mapped.md and verifies it)
       python -I -X utf8 map_7_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_7_vi.py show lo hi          (segments lo..hi with every pair; writes nothing)

Importing this module writes nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T07 (this script's table) -> map_common_vi.value()
(context3 -> KD -> alternatives / counts / «X saṅgahito» / «X dhammā» -> pi-2 chain -> pi-1 chain).
Conventions: pi-1 vi-map-conventions.md + notes, pi-2 vi-map-conventions-pi2.md + notes, vi-map-conventions-pi3.md,
finished pi-3 chapters (map_3_vi.py, map_5_vi.py and their notes).

The association frame of this method (first sampayutta / vippayutta chapter):
  «X katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttoti? Natthi. Katihi vippayutto? Catūhi khandhehi …
   vippayutto; ekenāyatanena ekāya dhātuyā kehici vippayutto.»
  «X gắn liền với bao nhiêu khối, …? Không có. Không gắn liền với bao nhiêu? Không gắn liền với bốn khối, …;
   không gắn liền với một số hiện tượng trong một lĩnh vực nhận biết, một yếu tố.»
  sampayutto / -ā / -aṃ = gắn liền (predicate; the governing «với» dropped, as pi-2 sampayuttā and the sample);
  vippayutto / -ā / -aṃ = không gắn liền; Natthi = không có; kehici = một số hiện tượng (the KD proposal fits:
  «gắn liền với một số hiện tượng trong một lĩnh vực nhận biết»; «trong» is the case frame).
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, NDE, build_part, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           present, read_keywords, read_pali, read_vietnamese, value, verify)

PART = "7-chatthanayo"

_GL, _KGL = "gắn liền", "không gắn liền"

T07 = {
    # ---- the association frame (predicates, every gender / number)
    "sampayutto": _GL, "sampayuttā": _GL, "sampayuttaṃ": _GL,
    "vippayutto": _KGL, "vippayuttā": _KGL, "vippayuttaṃ": _KGL,
    "kehici": "một số hiện tượng",     # «gắn liền với một số hiện tượng trong một lĩnh vực nhận biết, một yếu tố»
    "natthi": "không có",               # «… gắn liền với bao nhiêu? Không có.»
    # ---- headings and colophon «Giải thích đề mục về sự gắn liền và sự không gắn liền, phần thứ sáu»
    "chaṭṭha": "thứ sáu", "chaṭṭho": "thứ sáu",
    "vippayoga": "sự không gắn liền",
    "sacca": "sự thật",                 # Saccādi «Các sự thật và các mục khác»
    # ---- summary verse of ^3-305
    "jīvitaṃ": "sự sống",               # dukkhasaccañca jīvitaṃ «… sự thật về khổ đau và sự sống»
    "bhavā": "sự hiện hữu",             # cattāro ca mahābhavā «cùng bốn sự hiện hữu lớn»
    "ekūnavīsati": "mười chín",         # tikesvekūnavīsati «trong các bộ ba có mười chín»
    "gocchakesu": "nhóm",               # «Trong các nhóm có năm mươi» (as map_5_vi.py gocchaka; «Trong», «các» frame)
    "paññāsa": "năm mươi",
    "antare": "phần xen giữa",          # cūḷantare / Mahantare «trong phần xen giữa nhỏ / lớn»
    "pannarasa": "mười lăm",
    "pare": "phần sau",                 # aṭṭhārasa tato pare «phần sau đó có mười tám» («đó» = tato)
    "tevīsa": "hai mươi ba",            # Tevīsa padasataṃ «Một trăm hai mươi ba đề mục»
    "sataṃ": "một trăm",
    "labbhati": "có",                   # sampayoge na labbhati «không có trong sự gắn liền» («không» = na)
}

# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value(kw, kws, T07, vi.get(bid, ""))
    return resolve


def dump(only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v == "???" or (v != NDE and not present(v, vi.get(bid, ""))):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        p1 = [x for x, _ in pi1_map_values(kw).most_common(2) if x != v]
        p2 = [x for x, _ in pi2_map_values(kw).most_common(2) if x != v]
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  pi1:{p1}" if p1 else "") + (f"  pi2:{p2}" if p2 else "")
              + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi):
    res = resolver()
    vi, pi = read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]\n-- PI {pi.get(bid, '')}\n-- VI {vi.get(bid, '')}")
            print("   " + " | ".join(f"{kw}={res(bid, kw, kws)}" for kw in kws))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]))
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
