"""Build the Pāli->Vietnamese keyword map for pi-5 (Kathāvatthu) chapter 7: 7-ekaccam-atthitikatha.

usage: python -I -X utf8 -B map_7_vi.py                  (writes 7-ekaccam-atthitikatha.mapped.md and verifies it)
       python -I -X utf8 -B map_7_vi.py show lo hi        (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> value5(kw, kws, T7, text) of map_sample_vi (T7 -> context5 ->
FORMULAS -> KV -> two-word composition -> the pi-4 chain).
Conventions: pi-1 … pi-4 vi-map-conventions*.md + notes-map-*.md, vi-map-conventions-pi5.md; new values in
notes-map-7.md.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai\mapper-vi")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import NDE, GAP, build_part, en_ru, lc, present, read_keywords, read_vietnamese, verify  # noqa
from map_sample_vi import FORMULAS, KV, context5, value5  # noqa: E402,F401

PART = "7-ekaccam-atthitikatha"

_CCM = "có quả chưa chín muồi"                    # avipakkavipākā
_DCM = "có quả đã chín muồi"                      # vipakkavipākā

T7 = {
    # ---- headings: Ekaccaṃ atthītikathā «Bàn về việc cho rằng một phần tồn tại», Atītādiekaccakathā «Bàn về một
    # phần của quá khứ và các mục khác», Anāgatādiekaccakathā «… của tương lai …»; closer «Phần bàn về … đã hoàn tất.»
    # (kathā = Bàn về, niṭṭhitā = đã hoàn tất: FORMULAS; atthi = tồn tại: context5)
    # ---- the time strings (pi-2 ^2-… words): «một phần đã chấm dứt, … đã mất đi, … đã biến mất, … đã biến mất hoàn
    # toàn»; «một phần đã sinh ra, … đã sinh thành, … đã phát sinh, … đã hiện ra»
    "niruddhaṃ": "đã chấm dứt", "vigataṃ": "đã mất đi", "atthaṅgataṃ": "đã biến mất",
    "abbhatthaṅgataṃ": "đã biến mất hoàn toàn",
    "jātaṃ": "đã sinh ra", "sañjātaṃ": "đã sinh thành", "nibbattaṃ": "đã phát sinh", "pātubhūtaṃ": "đã hiện ra",
    "ajātaṃ": "chưa sinh ra",                      # own a- keeps the negative (pi-2 «chưa …»)
    # ---- «Có phải quá khứ / tương lai tồn tại không?»
    "atītaṃ": "quá khứ", "anāgataṃ": "tương lai",
    "atītaṃ atthi": "quá khứ tồn tại", "anāgataṃ atthi": "tương lai tồn tại",
    "atītā dhammā": "hiện tượng thuộc quá khứ", "anāgatā dhammā": "hiện tượng thuộc tương lai",
    "paccuppannā dhammā": "hiện tượng thuộc hiện tại",
    # ---- «các hiện tượng thuộc quá khứ có quả chưa chín muồi / có quả đã chín muồi / không có quả trổ»
    "avipakkavipākā": _CCM, "vipakkavipākā": _DCM,
    "vipakka": "đã chín muồi",                     # member of (a)vipakkavipākā
    "vipaccissanti": "sẽ trổ quả",
    "ekadesaṃ": "một phần",                        # «một phần có quả đã chín muồi» (notes-map-3)
    # ---- «các hiện tượng thuộc tương lai sẽ sinh khởi / sẽ không sinh khởi»
    "uppādino": "sẽ sinh khởi",                    # pi-1 MATRIX
    # ---- «Có phải vì cho rằng … sẽ trổ quả, chúng tồn tại không?» (X-ti katvā)
    "katvā": "vì cho rằng",
    "nirujjhissanti": "sẽ chấm dứt",
}

OVERRIDES = {}

ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value5(kw, kws, T7, vi.get(bid, ""))
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
