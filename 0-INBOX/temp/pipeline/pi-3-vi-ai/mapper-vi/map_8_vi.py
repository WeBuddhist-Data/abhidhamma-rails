"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 8-sattamanayo (method 7).

usage: python -I -X utf8 map_8_vi.py                     (writes 8-sattamanayo.mapped.md and verifies it)
       python -I -X utf8 map_8_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_8_vi.py show lo hi          (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T08 (this script's table) -> map_common_vi.value()
(context3 -> KD -> alternatives / counts / «X saṅgahito» / «X dhammā» -> pi-2 chain -> pi-1 chain).
Reuses the tables of map_common_vi.py / map_sample_vi.py read-only.
Conventions: pi-1 vi-map-conventions.md + notes, pi-2 vi-map-conventions-pi2.md + notes, vi-map-conventions-pi3.md,
map_3_vi.py / map_4_vi.py / map_5_vi.py (finished chapters).
"""
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi")
from map_common_vi import (GAP, NDE, build_part, lc, read_keywords, read_vietnamese, value,  # noqa: E402
                           verify)
import map_sample_vi as S  # noqa: E402

PART = "8-sattamanayo"

# part table (method 7: «Đối với X, những hiện tượng nào gắn liền với nó, đối với những hiện tượng ấy, những hiện
# tượng nào không gắn liền với chúng, thì những hiện tượng đó không gắn liền với bao nhiêu khối …»).
# Reference words X-ena / X-āya / X-ehi = X itself («đối với» is the case frame), as map_3 / map_4 / map_5.
T08 = {
    # ---- the association frame (as map_7_vi.py): predicates, every gender / number; «với» dropped
    "sampayuttā": "gắn liền", "vippayuttā": "không gắn liền",
    "kehici": "một số hiện tượng",                 # «không gắn liền với một số hiện tượng trong một lĩnh vực …»
    # ---- heading «Phương pháp thứ bảy»; colophon «…, phần thứ bảy»
    "sattama": "thứ bảy", "sattamo": "thứ bảy",
    # ---- reference words «Đối với X, những hiện tượng nào gắn liền với nó …» (X itself)
    "vedanākkhandhena": "khối cảm giác", "saññākkhandhena": "khối tri giác",
    "saṅkhārakkhandhena": "khối tạo tác", "viññāṇakkhandhena": "khối thức",
    "manāyatanena": "lĩnh vực ý",
    "cakkhuviññāṇadhātuyā": "yếu tố thức qua mắt", "manodhātuyā": "yếu tố ý",
    "manoviññāṇadhātuyā": "yếu tố ý thức",
    "indriyena": "năng lực",                       # Manindriyena / Upekkhindriyena «năng lực ý / bình thản»
    "viññāṇena": "thức",                           # saṅkhārapaccayā viññāṇena «các sự tạo tác làm điều kiện cho thức»
    "phassena": "sự tiếp xúc", "vedanāya": "cảm giác", "saññāya": "tri giác", "cetanāya": "chủ ý",
    "cittena": "tâm", "manasikārena": "sự chú tâm",
    # «các hiện tượng có sự bình thản đi kèm» (pi-1 sahagataṃ = đi kèm; KD sahagatā dhammā)
    "sahagatehi": "đi kèm", "sahagatehi dhammehi": "hiện tượng có" + GAP + "đi kèm",
    # «các hiện tượng có sự hướng tâm và sự duy trì tâm» / «… có sự hướng tâm» / «… có sự duy trì tâm»
    "savitakka dhammehi": "hiện tượng có sự hướng tâm", "savitakkehi dhammehi": "hiện tượng có sự hướng tâm",
    "savicārehi dhammehi": "hiện tượng có sự duy trì tâm",
    "vitakkehi": "sự hướng tâm", "vicārehi": "sự duy trì tâm",
    # citta dyads (map_4_vi.py values): «các hiện tượng là tâm / là yếu tố đồng hành với tâm / hòa lẫn với tâm …»
    "cittehi": "tâm", "cetasikehi": "yếu tố đồng hành với tâm",
    "saṃsaṭṭhehi": "hòa lẫn", "saṃsaṭṭhehi dhammehi": "hiện tượng hòa lẫn",
    "samuṭṭhānehi": "do" + GAP + "sinh ra", "sahabhūhi": "cùng tồn tại", "anuparivattīhi": "vận hành theo",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi": "vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm",
    # ---- summary verse of ^3-316
    "indriyato": "năng lực",                       # dvepi ca indriyato «và hai nữa từ các năng lực» («từ các» frame)
    "tathariva": "cũng vậy",                       # phassapañcamā tathariva «… cũng vậy» (as map_4 tathā)
    "manasi": "sự chú tâm",                        # Adhimuccanā manasi «Sự khởi quyết định, sự chú tâm»
    "antarā": "phần xen giữa",                     # Sattantarā «Bảy trong phần xen giữa» (as map_7 antare)
    "manena": "ý", "yuttā": "kết hợp",             # dve ca manena yuttā «và hai kết hợp với ý»
    "vicāraṇā": "sự duy trì tâm",                  # Vitakkavicāraṇā «Sự hướng tâm, sự duy trì tâm»
}

# per-segment choices (read from the segments)
OVERRIDES = {
    # heading «Giải thích đề mục về điều không gắn liền dựa trên điều gắn liền»: method nouns (as map_3 / map_4
    # asaṅgahita = điều không được gộp vào)
    "3-8-1-0": {"sampayutta": "điều gắn liền", "vippayutta": "điều không gắn liền"},
}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value(kw, kws, T08, vi.get(bid, ""))
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
