"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 6: 6-atitakkhandhadikatha.

usage: python -I -X utf8 -B map_6_vi.py                  (writes 6-atitakkhandhadikatha.mapped.md and verifies it)
       python -I -X utf8 -B map_6_vi.py show lo hi        (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> value5(kw, kws, T6, text) of map_sample_vi (T6 -> context5 ->
FORMULAS -> KV -> two-word composition -> the pi-4 chain).
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import NDE, GAP, build_part, en_ru, lc, present, read_keywords, read_vietnamese, verify  # noqa
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "6-atitakkhandhadikatha"

_LV = "lĩnh vực nhận biết"

T6 = {
    # ---- headings: Atītakkhandhādikathā «Bàn về các khối quá khứ và các mục khác» (closer «Phần bàn về … đã hoàn
    # tất.»), (Na)suttasādhanaṃ «(Không dựa trên) chứng cứ từ kinh»
    "atītakkhandha": "khối quá khứ",               # «các khối quá khứ» (frame «các» dropped)
    "sādhanaṃ": "chứng cứ",                        # notes-map-2 sādhana
    # ---- 5-297 «Có phải quá khứ là các khối không? … Có phải quá khứ tồn tại không? … là lĩnh vực nhận biết … là
    # yếu tố … là các khối, yếu tố, lĩnh vực nhận biết …»
    "āyatanaṃ": _LV,                               # the free-standing word (pi-1), not the member «lĩnh vực» (pi-2)
    "dhātu āyatanaṃ": "yếu tố " + _LV,             # «các khối, yếu tố, lĩnh vực nhận biết» (comma dropped, pi-1)
    # «quá khứ / tương lai / hiện tại» as the subject (inner «là các» kept, pi-1)
    "atītaṃ khandhā": "quá khứ là các khối", "anāgataṃ khandhā": "tương lai là các khối",
    "paccuppannaṃ khandhā": "hiện tại là các khối",
    "atītaṃ atthi": "quá khứ tồn tại", "anāgataṃ atthi": "tương lai tồn tại", "paccuppannaṃ atthi": "hiện tại tồn tại",
    "atītaṃ natthi": "quá khứ không tồn tại", "paccuppannaṃ natthi": "hiện tại không tồn tại",
    # «vật chất / thức thuộc quá khứ là khối …» (noun + attribute, pi-2; the subject before its predicate with the
    # inner «là» after the gap, as sample aññā vedanā «cảm giác … là khác»)
    "rūpaṃ khandho": "vật chất" + GAP + "là khối", "rūpaṃ khandhā": "vật chất" + GAP + "là các khối",
    "rūpaṃ āyatanaṃ": "vật chất" + GAP + "là " + _LV,
    "rūpaṃ atthi": "vật chất" + GAP + "tồn tại", "rūpaṃ natthi": "vật chất" + GAP + "không tồn tại",
    "viññāṇaṃ khandho": "thức" + GAP + "là khối", "viññāṇaṃ khandhā": "thức" + GAP + "là các khối",
    "viññāṇaṃ āyatanaṃ": "thức" + GAP + "là " + _LV,
    "viññāṇaṃ atthi": "thức" + GAP + "tồn tại", "viññāṇaṃ natthi": "thức" + GAP + "không tồn tại",
    "atītaṃ viññāṇaṃ khandhā": "thức thuộc quá khứ là các khối",
    "anāgataṃ viññāṇaṃ khandhā": "thức thuộc tương lai là các khối",
    "paccuppannaṃ viññāṇaṃ khandhā": "thức thuộc hiện tại là các khối",
    "atītaṃ viññāṇaṃ atthi": "thức thuộc quá khứ tồn tại", "anāgataṃ viññāṇaṃ atthi": "thức thuộc tương lai tồn tại",
    "paccuppannaṃ viññāṇaṃ atthi": "thức thuộc hiện tại tồn tại",
    # ---- 5-298 «các khối, yếu tố, lĩnh vực nhận biết thuộc quá khứ và tương lai, chúng không tồn tại» … «ba phạm
    # vi này của cách diễn đạt, phạm vi của tên gọi, khái niệm… bởi những người hiểu biết…» … «bất cứ vật chất nào,
    # dù thuộc quá khứ …, ở nơi bản thân hay ở bên ngoài bản thân, ở dạng thô hay ở dạng vi tế …»
    "atītānāgatā": "thuộc quá khứ và tương lai",
    "anāgatā": "thuộc" + GAP + "tương lai",        # member of atītānāgatā («thuộc» shared by the pair)
    "atītānāgatā khandhā": "khối" + GAP + "thuộc quá khứ và tương lai",
    "pathā": "phạm vi",                            # pi-1 MATRIX (niruttipathā …)
    "adhivacana": "tên gọi",                       # pi-1 adhivacanā
    "paññatti": "khái niệm",                       # the Suttanta 'concept' sense (pi-1 MATRIX), not pi-4 «định danh»
    "viññūhi": "người hiểu biết",                  # «bởi những người hiểu biết» («bởi», «những» = frame)
    "bahiddhā": "ở bên ngoài bản thân",            # pi-1 / pi-2 (sample «bên ngoài» where the text has only that)
}

OVERRIDES = {}

ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value5(kw, kws, T6, vi.get(bid, ""))
    return resolve


def show(lo, hi):
    res = resolver()
    vi = read_vietnamese(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            er = en_ru(bid)
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                e = er.get(kw, ["", ""])
                print(f"   {kw}={v}  [en:{e[0]} | ru:{e[1]}]{flag}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]))
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
