"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 9: 9-hevatthikatha.

usage: python -I -X utf8 -B map_9_vi.py                  (writes 9-hevatthikatha.mapped.md and verifies it)
       python -I -X utf8 -B map_9_vi.py show lo hi        (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> value5(kw, kws, T9, text) of map_sample_vi (T9 -> context5 ->
FORMULAS -> KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md; new values in
notes-map-9.md.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import NDE, GAP, build_part, en_ru, lc, present, read_keywords, read_vietnamese, verify  # noqa
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "9-hevatthikatha"

T9 = {
    # ---- heading Hevatthikathā «Bàn về việc cho rằng có tồn tại theo cách này»; closer «Phần bàn về … đã hoàn tất.»
    # (kathā = Bàn về, niṭṭhitā = đã hoàn tất: FORMULAS; atthi = tồn tại: context5)
    # ---- «Có phải quá khứ / tương lai / hiện tại tồn tại không?» (as map_6_vi.py / map_7_vi.py)
    "atītaṃ atthi": "quá khứ tồn tại", "anāgataṃ atthi": "tương lai tồn tại", "paccuppannaṃ atthi": "hiện tại tồn tại",
    # «Có phải chính cái ấy tồn tại, chính cái ấy không tồn tại không?» (Sevatthi, seva natthīti?)
    "sevatthi": "chính cái ấy tồn tại",
    # ---- «Có phải ý nghĩa của sự tồn tại là ý nghĩa của sự không tồn tại, …, trạng thái tồn tại là trạng thái không
    # tồn tại, …, đó chính là cùng một thứ, cùng một nghĩa, như nhau, ngang nhau, cùng một loại không?»
    # (Atthaṭṭho natthaṭṭho … atthibhāvo natthibhāvo … esese ekaṭṭhe same samabhāge tajjāte)
    "aṭṭho": "ý nghĩa",                            # member of atthaṭṭho «ý nghĩa của sự tồn tại» (not the sample's
                                                   # saccikaṭṭho «thực tại»)
    "atthibhāvo": "trạng thái tồn tại",
    "samabhāge": "ngang nhau",                     # sample: sama (member) = ngang nhau, same = như nhau
    "tajjāte": "cùng một loại",                    # sample: jāte (member) = loại
    # ---- chapter verse «Tóm tắt của chương này – Sự được tìm thấy, sự suy thoái, đời sống tu hành trong sạch, từng
    # phần; Sự hiểu biết trọn vẹn, sự dứt bỏ sự tham đắm dục lạc, học thuyết cho rằng tất cả đều tồn tại, lĩnh vực
    # nhận biết; Quá khứ và tương lai được phân chia khéo léo […], tất cả các hiện tượng là sự thiết lập tỉnh thức.»
    "uddānaṃ": "Tóm tắt",                          # Tassuddānaṃ «Tóm tắt của chương này»
    "upalabbho": "Sự được tìm thấy",               # line-initial capital kept (sample peyyālā «Phần lặp lại»)
    "parihāni": "sự suy thoái",                    # notes-map-2
    "vāso": NDE,                                   # brahmacariyavāso «đời sống tu hành trong sạch» (notes-map-3)
    "odhiso": "từng phần",                         # notes-map-3
    "pariññā": "Sự hiểu biết trọn vẹn",
    "pahānaṃ": "sự dứt bỏ",                        # kāmarāgappahānaṃ «sự dứt bỏ sự tham đắm dục lạc»
    "vādo": "học thuyết",                          # sabbatthivādo «học thuyết cho rằng tất cả đều tồn tại»
    "āyatanaṃ": "lĩnh vực nhận biết",              # the free-standing word (notes-map-6)
    "atītānāgato": "Quá khứ và tương lai",         # Atītānāgato subhaṅgo «Quá khứ và tương lai được phân chia …»
}

OVERRIDES = {}

ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value5(kw, kws, T9, vi.get(bid, ""))
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
