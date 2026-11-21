"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 15-cuddasamanayo (method 14: «Vippayuttena-
saṅgahitāsaṅgahitapadaniddeso», inclusion and non-inclusion of what is dissociated; last chapter, book colophon).

usage: python -I -X utf8 map_15_vi.py                     (writes 15-cuddasamanayo.mapped.md and verifies it)
       python -I -X utf8 map_15_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_15_vi.py show lo hi          (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> segment rules below -> «X dhammehi» rule (as map_6 / map_11) ->
T15 (this script's table, on top of the finished tables of map_3 / map_6 / map_7 / map_8 / map_11 and the closing-verse
values of map_9, read-only) -> map_common_vi.value() (context3 -> KD -> alternatives / counts / «X saṅgahito» /
«X dhammā» -> pi-2 -> pi-1 chain).
Conventions: pi-1 vi-map-conventions.md + notes, pi-2 vi-map-conventions-pi2.md + notes, vi-map-conventions-pi3.md,
finished chapters 3-12 (map_*_vi.py, notes-map-*.md).

Frame of this method (the dissociation relative clause of chapters 9 / 11 + the inclusion answer of chapter 2):
  «Rūpakkhandhena ye dhammā vippayuttā, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā? Te dhammā
   catūhi khandhehi dvīhāyatanehi aṭṭhahi dhātūhi saṅgahitā. Katihi asaṅgahitā? Ekena khandhena dasahāyatanehi
   dasahi dhātūhi asaṅgahitā.»
  «Đối với khối vật chất, những hiện tượng nào không gắn liền với nó, thì những hiện tượng đó được gộp vào bao nhiêu
   khối, …? Những hiện tượng đó được gộp vào bốn khối, hai lĩnh vực nhận biết, tám yếu tố. Không được gộp vào bao
   nhiêu? Không được gộp vào một khối, mười lĩnh vực nhận biết, mười yếu tố.»
"""
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi")
from map_common_vi import (GAP, NDE, build_part, lc, present, read_keywords, read_vietnamese, value,  # noqa: E402
                           verify)
import map_sample_vi as S  # noqa: E402
import map_3_vi as M3  # noqa: E402
import map_9_vi as M9  # noqa: E402
import map_11_vi as M11  # noqa: E402

PART = "15-cuddasamanayo"

_KX = "không xác định về mặt đạo đức"

T15 = {
    **M3.T3,                                         # X-viññāṇadhātuyā = yếu tố thức qua X (notes-map-3)
    **M11.T11,                                      # T6 / T07 / T08 + the chapter-11 dissociation values
    **M9.T09,                                        # closing verse of ^3-318 (= the verse of ^3-518), values copied
    # ---- heading «Phương pháp thứ mười bốn»; colophon «…, phần thứ mười bốn»
    "cuddasama": "thứ mười bốn", "cuddasamo": "thứ mười bốn",
    # ---- heading / colophon compound «Giải thích đề mục về điều được gộp vào và điều không được gộp vào dựa trên điều
    # không gắn liền»: method nouns with the text's «điều» (as map_9 / map_11 vippayutta, map_3 / map_6 asaṅgahita)
    "vippayutta": "điều không gắn liền", "asaṅgahita": "điều không được gộp vào",
    # ---- the frame: dissociation predicate (map_9 / map_11) + inclusion answer (KD, sample chapter 2)
    "vippayuttā": "không gắn liền",
    "dhammehi vippayuttā": "hiện tượng" + GAP + "không gắn liền",   # artefact pair, always « … » (as map_11)
    # ---- headings «Các sự thật và các mục khác», «Nhóm bảy mục bắt đầu bằng sự tiếp xúc» (ādi: override)
    "sacca": "sự thật", "phassa": "sự tiếp xúc",
    # ---- reference words «Đối với X» (X itself; «đối với» is the case frame)
    "dukkhasaccena": "sự thật về khổ đau",
    "abyākatehi": _KX,                               # «các hiện tượng không xác định về mặt đạo đức»
    "parittehi": "hạn hẹp",                          # «các hiện tượng hạn hẹp» (pi-1 paritta)
    "majjhimehi": "trung bình",
    "uppādīhi": "sẽ sinh khởi",
    "lokiyehi": "thuộc thế gian",
    "sāsavehi": "đối tượng của ô nhiễm",             # Sāsavehi dhammehi «các hiện tượng là đối tượng của ô nhiễm»
    "asaṃkiliṭṭhehi": "không bị phiền não làm vẩn đục",   # own a- kept (KD asaṃkiliṭṭha)
    "sauttarehi": "còn có điều cao hơn",
    # ---- book colophon «Bộ “Thảo luận về các yếu tố” đã hoàn tất.» (Dhātukathāpakaraṇaṃ niṭṭhitaṃ)
    "niṭṭhitaṃ": "đã hoàn tất",
}

# per-segment choices (read from the segments)
OVERRIDES = {
    # «Nhóm bảy mục bắt đầu bằng sự tiếp xúc» (Phassādisattakaṃ): ādi = «bắt đầu bằng», not «các mục khác»
    "3-15-1-3-0": {"ādi": "bắt đầu bằng"},
    # saññābhavena «sự hiện hữu có tri giác» / asaññābhavena «… không có tri giác» / nevasaññānāsaññābhavena «… không
    # phải có tri giác cũng không phải không có tri giác»: saññā of the bhava list = có tri giác (as map_3 ^3-174,
    # map_6 ^3-205 / ^3-206, map_11 ^3-365 / ^3-366, sample ^3-67)
    "3-468": {"saññā": "có tri giác"},
    "3-470": {"saññā": "có tri giác"},
    "3-471": {"saññā": "có tri giác"},
}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def _value(kw, kws, text):
    k = lc(kw)
    if k == "hetukehi":            # «có gốc rễ» / only maggahetukehi «lấy con đường làm gốc rễ» (map_11 rule)
        return "có gốc rễ" if present("có gốc rễ", text) else "lấy" + GAP + "làm gốc rễ"
    if k == "uppannehi":           # Uppannehi «đã sinh khởi» / fragment of anuppannehi «chưa sinh khởi» (map_11)
        return "đã sinh khởi" if present("đã sinh khởi", text) else "sinh khởi"
    if k not in T15 and k.endswith(" dhammehi"):    # «X dhammehi» = hiện tượng (là) X / hiện tượng … X (map_6_vi.py)
        xv = _value(kw.rsplit(" ", 1)[0], kws, text)
        for cand in (f"hiện tượng {xv}", f"hiện tượng là {xv}"):
            if present(cand, text):
                return cand
        return "hiện tượng" + GAP + xv
    return value(kw, kws, T15, text)


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
