"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 11-dasamanayo (method 10: «Vippayuttena-
vippayuttapadaniddeso», dissociated from the dissociated).

usage: python -I -X utf8 map_11_vi.py                     (writes 11-dasamanayo.mapped.md and verifies it)
       python -I -X utf8 map_11_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_11_vi.py show lo hi          (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> segment rules below -> «X dhammehi» rule (as map_6_vi.py) ->
T11 (this script's table, on top of the finished tables T6 / T07 / T08 of map_6 / map_7 / map_8, read-only) ->
map_common_vi.value() (context3 -> KD -> alternatives / counts / «X saṅgahito» / «X dhammā» -> pi-2 -> pi-1 chain).
Conventions: pi-1 vi-map-conventions.md + notes, pi-2 vi-map-conventions-pi2.md + notes, vi-map-conventions-pi3.md,
finished chapters 3-8 (map_*_vi.py, notes-map-*.md).

Frame of this method (the double-relative frame of chapter 8, with vippayutta twice):
  «Rūpakkhandhena ye dhammā vippayuttā, tehi dhammehi ye dhammā vippayuttā, te dhammā katihi khandhehi … vippayuttā?
   Te dhammā catūhi khandhehi … vippayuttā; ekenāyatanena ekāya dhātuyā kehici vippayuttā.»
  «Đối với khối vật chất, những hiện tượng nào không gắn liền với nó, đối với những hiện tượng ấy, những hiện tượng
   nào không gắn liền với chúng, thì những hiện tượng đó không gắn liền với bao nhiêu khối, …? Những hiện tượng đó
   không gắn liền với bốn khối, …; không gắn liền với một số hiện tượng trong một lĩnh vực nhận biết, một yếu tố.»
"""
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi")
from map_common_vi import (GAP, NDE, build_part, lc, present, read_keywords, read_vietnamese, value,  # noqa: E402
                           verify)
import map_sample_vi as S  # noqa: E402
import map_6_vi as M6  # noqa: E402
import map_7_vi as M7  # noqa: E402
import map_8_vi as M8  # noqa: E402

PART = "11-dasamanayo"

_KGL = "không gắn liền"

T11 = {
    **M6.T6, **M7.T07, **M8.T08,
    # ---- heading «Phương pháp thứ mười», colophon «…, phần thứ mười»
    "dasama": "thứ mười", "dasamo": "thứ mười",
    # ---- the frame: «… những hiện tượng nào không gắn liền …» (artefact pairs; always « … », as ch8 dhammā vippayuttā)
    "dhammā vippayuttā": "hiện tượng" + GAP + _KGL,
    "dhammehi vippayuttā": "hiện tượng" + GAP + _KGL,
    "kehici": "một số hiện tượng",
    # ---- reference words «Đối với X» (X itself; «đối với» is the case frame)
    "rūpakkhandhena": "khối vật chất",
    "adhimokkhena": "sự quyết định",               # «Đối với sự quyết định» (pi-2 map adhimokkha = sự quyết định)
    "saṅkhārehi": "sự tạo tác",                    # avijjāpaccayā saṅkhārehi «vô minh làm điều kiện cho các sự tạo tác»
    "kusalehi": "thiện", "akusalehi": "bất thiện",
    "upādinnehi": "do nghiệp tạo ra",              # of Anupādinnehi «không do nghiệp tạo ra» (positive part)
    "uppannehi": "sinh khởi",                      # of Anuppannehi «chưa sinh khởi» (positive part, KD uppannā rule)
    "pītikehi": "có sự hân hoan",                  # Sappītikehi «có sự hân hoan» (pi-1 pītikā)
    "avitakkehi": "không có sự hướng tâm",         # Avitakkehi dhammehi «các hiện tượng không có sự hướng tâm» (own a-)
    "kilesa": "phiền não",
}

# per-segment choices (read from the segments)
OVERRIDES = {
    # Asaññābhavena «sự hiện hữu không có tri giác» / nevasaññānāsaññābhavena «… không phải có tri giác cũng không
    # phải không có tri giác»: saññā of the bhava list = có tri giác (as map_3 ^3-174, map_6 ^3-205 / ^3-206)
    "3-365": {"saññā": "có tri giác"},
    "3-366": {"saññā": "có tri giác"},
    # heading «Giải thích đề mục về điều không gắn liền dựa trên điều không gắn liền» (method noun, as map_8 ^3-8-1-0)
    "3-11-1-0": {"vippayutta": "điều không gắn liền"},
}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def _value(kw, kws, text):
    k = lc(kw)
    if k == "hetukehi":            # «có gốc rễ» / only maggahetukehi «lấy con đường làm gốc rễ» (pi-2 / context3 rule)
        return "có gốc rễ" if present("có gốc rễ", text) else "lấy" + GAP + "làm gốc rễ"
    if k not in T11 and k.endswith(" dhammehi"):    # «X dhammehi» = hiện tượng (là) X / hiện tượng … X (map_6_vi.py)
        xv = _value(kw.rsplit(" ", 1)[0], kws, text)
        for cand in (f"hiện tượng {xv}", f"hiện tượng là {xv}"):
            if present(cand, text):
                return cand
        return "hiện tượng" + GAP + xv
    return value(kw, kws, T11, text)


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


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        _patched(lambda: S.dump(PART, sys.argv[2:3] == ["miss"]))
    elif sys.argv[1:2] == ["show"]:
        _patched(lambda: S.show(PART, int(sys.argv[2]), int(sys.argv[3])))
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
