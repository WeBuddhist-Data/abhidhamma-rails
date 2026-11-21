"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 4-tatiyanayo (method 3).

usage: python -I -X utf8 map_4_vi.py                     (writes 4-tatiyanayo.mapped.md and verifies it)
       python -I -X utf8 map_4_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_4_vi.py show lo hi          (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T04 (this script's table) -> map_common_vi.value()
(context3 -> KD -> pi-2 / pi-1 chain). Reuses the tables of map_common_vi.py / map_sample_vi.py read-only.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi")
from map_common_vi import (GAP, NDE, build_part, lc, read_keywords, read_vietnamese, value,  # noqa: E402
                           verify)
import map_sample_vi as S  # noqa: E402

PART = "4-tatiyanayo"

# part table (method 3: «Đối với X, những hiện tượng nào không được gộp vào theo cách gộp vào khối, được gộp vào
# theo cách gộp vào lĩnh vực nhận biết, được gộp vào theo cách gộp vào yếu tố … thì những hiện tượng đó …»).
# Reference words X-ena / X-āya / X-ehi = X itself («đối với» is the case frame), as map_3_vi.py / map_5_vi.py.
T04 = {
    # heading / colophon «Giải thích đề mục về điều được gộp vào dựa trên điều không được gộp vào» (method noun)
    "asaṅgahita": "điều không được gộp vào",
    # «được gộp vào theo cách gộp vào lĩnh vực nhận biết»: the Vietnamese puts the predicate first; copied as it
    # stands (contiguous), not in Pāli order (which would point at the next clause's «được gộp vào»)
    "āyatanasaṅgahena saṅgahitā": "được gộp vào theo cách gộp vào lĩnh vực nhận biết",
    # artefact pairs «… ye dhammā khandhasaṅgahena …» «…, những hiện tượng nào không được gộp vào theo cách gộp vào
    # khối» (as map_3_vi.py / map_5_vi.py)
    "dhammehi khandhasaṅgahena": "hiện tượng" + GAP + "theo cách gộp vào khối",
    "indriyena khandhasaṅgahena": "năng lực" + GAP + "theo cách gộp vào khối",
    "vedanākkhandhena": "khối cảm giác", "saññākkhandhena": "khối tri giác",
    "saṅkhārakkhandhena": "khối tạo tác",
    "saccena": "sự thật", "indriyena": "năng lực", "indriyehi": "năng lực",
    "sampayuttehi": "gắn liền",                    # hetu- / āsava- / citta- / kilesasampayuttehi «gắn liền với …»
    "upādānena": "sự bám víu", "phassena": "sự tiếp xúc", "taṇhāya": "khao khát", "avijjāya": "vô minh",
    "bhavena": "sự hiện hữu",                      # kammabhavena «sự hiện hữu dưới dạng nghiệp»
    "saṅkhārena": "sự tạo tác",                    # avijjāpaccayā saṅkhārena «… làm điều kiện cho các sự tạo tác»
    "vedanāya": "cảm giác", "saññāya": "tri giác", "cetanāya": "chủ ý", "manasikārena": "sự chú tâm",
    "jātiyā": "sự sinh", "jarāya": "sự lão hóa", "maraṇena": "sự chết", "jhānena": "tầng thiền",
    "sokena": "sự sầu muộn", "dukkhena": "sự khó chịu", "domanassena": "nỗi buồn", "upāyāsena": "sự tuyệt vọng",
    "upaṭṭhānena": "sự thiết lập", "padhānena": "nỗ lực", "appamaññāya": "trạng thái không thể đo lường",
    "balehi": "sức mạnh", "aṅgehi": "chi phần", "ariyena": "cao quý", "aṭṭhaṅgikena": "gồm tám chi phần",
    "maggena": "con đường",
    "hetūhi": "gốc rễ",                            # «các hiện tượng là gốc rễ»
    # «các hiện tượng không do điều kiện tạo thành» (adjective; the noun asaṅkhataṃ keeps «điều»)
    "asaṅkhatehi": "không do điều kiện tạo thành",
    "asaṅkhatehi dhammehi": "hiện tượng không do điều kiện tạo thành",
    # cluster plurals = the MATRIX noun
    "āsavehi": "ô nhiễm", "saṃyojanehi": "xiềng xích", "ganthehi": "nút thắt", "oghehi": "dòng lũ",
    "yogehi": "ách", "nīvaraṇehi": "chướng ngại", "parāmāsehi": "sự hiểu sai lệch",
    "parāmaṭṭhehi": "bị sự hiểu sai lệch nắm giữ",
    "upādānehi": "sự bám víu", "kilesehi": "phiền não", "saṃkilesikehi": "đối tượng của phiền não",
    "saṃkiliṭṭhehi": "bị phiền não làm vẩn đục",
    # citta dyads (pi-1 / sample values: «vừa hòa lẫn với tâm vừa do tâm sinh ra vừa …»)
    "cetasikehi": "yếu tố đồng hành với tâm",
    "saṃsaṭṭhehi": "hòa lẫn", "saṃsaṭṭhehi dhammehi": "hiện tượng hòa lẫn",
    "samuṭṭhānehi": "do" + GAP + "sinh ra",
    "sahabhūhi": "cùng tồn tại",
    "sahabhūmi": "cùng tồn tại",                   # Cittasahabhūmi (sic, for -sahabhūhi) «cùng tồn tại với tâm»
    "sahabhūmi dhammehi": "hiện tượng cùng tồn tại",
    "anuparivattīhi": "vận hành theo", "anuparivattīhi dhammehi": "hiện tượng vận hành theo",
    "cittānuparivattīhi": "vận hành theo tâm", "cittānuparivattīhi dhammehi": "hiện tượng vận hành theo tâm",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi": "vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm",
    # closing verse «Ba khối, các sự thật cũng vậy, và mười sáu năng lực; / Các đề mục trong chuỗi điều kiện, mười
    # bốn, tiếp theo có mười bốn. / Có tròn ba mươi đề mục, trong mười nhóm, tiếp đến; / Hai bộ đôi xen giữa nhỏ …,
    # tám thuộc phần xen giữa lớn.»
    "ākāre": "chuỗi",                              # paccayākāre «trong chuỗi điều kiện»
    "upari": "tiếp theo",                          # cuddasūpari «tiếp theo có mười bốn»
    "samatiṃsa": "tròn ba mươi",
    "gocchakesu": "nhóm",                          # «trong mười nhóm» (map_5 gocchaka = nhóm)
    "dasasu": "mười",
    "antara": "xen giữa",                          # cūḷantaradukā / mahantarā (pi-1 antara = xen giữa)
    "dukā": "bộ đôi",
}

OVERRIDES = {}

ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value(kw, kws, T04, vi.get(bid, ""))
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
