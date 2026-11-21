"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 13-dvadasamanayo (method 12: inclusion and
non-inclusion by association, «Sampayuttenasaṅgahitāsaṅgahitapadaniddeso»).

usage: python -I -X utf8 map_13_vi.py                     (writes 13-dvadasamanayo.mapped.md and verifies it)
       python -I -X utf8 map_13_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_13_vi.py show lo hi          (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> «X dhammehi» rule (as map_6_vi.py / map_10_vi.py) -> T13 (this
script's table) -> map_common_vi.value() (context3 -> KD -> alternatives / counts / «X saṅgahito» / «X dhammā» ->
pi-2 chain -> pi-1 chain). Reuses the tables of map_common_vi.py / map_sample_vi.py read-only.
Conventions: pi-1 vi-map-conventions.md + notes, pi-2 vi-map-conventions-pi2.md + notes, vi-map-conventions-pi3.md,
finished chapters 3-10 (map_3 … map_10_vi.py and their notes); the reference words and the closing verse copy
map_10_vi.py (same Pāli, same harmonised Vietnamese); the inclusion answers copy the sample (2-pathamanayo).

The frame of this method:
  «X-ena ye dhammā sampayuttā, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi saṅgahitā? Te dhammā tīhi
   khandhehi … saṅgahitā. Katihi asaṅgahitā? Dvīhi khandhehi dasahāyatanehi dasahi dhātūhi asaṅgahitā.»
  «Đối với X, những hiện tượng nào gắn liền với nó, thì những hiện tượng đó được gộp vào bao nhiêu khối …? Những hiện
   tượng đó được gộp vào ba khối …. Không được gộp vào bao nhiêu? Không được gộp vào hai khối, mười lĩnh vực nhận
   biết, mười yếu tố.»
"""
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi")
from map_common_vi import (GAP, build_part, lc, present, read_vietnamese, value, verify)  # noqa: E402
import map_sample_vi as S  # noqa: E402

PART = "13-dvadasamanayo"

T13 = {
    # ---- predicates: sampayuttā = gắn liền (map_7 … map_10, «với» dropped); saṅgahitā / asaṅgahitā from KD
    "sampayuttā": "gắn liền",
    # ---- heading «Phương pháp thứ mười hai»; «Giải thích đề mục về điều được gộp vào và điều không được gộp vào
    # dựa trên điều gắn liền»; colophon «…, phần thứ mười hai»
    "dvādasama": "thứ mười hai", "dvādasamo": "thứ mười hai",
    "sampayutta": "điều gắn liền",                 # method noun of the heading compound (as map_8 / map_10)
    "asaṅgahita": "điều không được gộp vào",       # method noun of the heading compound (as map_3 / map_6)
    # ---- reference words «Đối với X» = X itself («đối với» is the case frame), as map_10_vi.py
    "vedanākkhandhena": "khối cảm giác", "saññākkhandhena": "khối tri giác",
    "saṅkhārakkhandhena": "khối tạo tác", "viññāṇakkhandhena": "khối thức",
    "manāyatanena": "lĩnh vực ý",
    "cakkhuviññāṇadhātuyā": "yếu tố thức qua mắt", "manodhātuyā": "yếu tố ý",
    "manoviññāṇadhātuyā": "yếu tố ý thức",
    "saccena": "sự thật",                          # samudaya- / maggasaccena «sự thật về sự phát sinh / con đường»
    "indriyena": "năng lực", "indriyehi": "năng lực",
    "avijjāya": "vô minh",
    "saṅkhārehi": "sự tạo tác",                    # avijjāpaccayā saṅkhārehi «vô minh làm điều kiện cho các sự tạo tác»
    "viññāṇena": "thức",                           # saṅkhārapaccayā viññāṇena «… làm điều kiện cho thức»
    "phassena": "sự tiếp xúc", "vedanāya": "cảm giác", "taṇhāya": "khao khát", "upādānena": "sự bám víu",
    "bhavena": "sự hiện hữu",                      # kammabhavena «sự hiện hữu dưới dạng nghiệp»
    "sokena": "sự sầu muộn", "dukkhena": "sự khó chịu", "domanassena": "nỗi buồn", "upāyāsena": "sự tuyệt vọng",
    "upaṭṭhānena": "sự thiết lập", "padhānena": "nỗ lực", "jhānena": "tầng thiền",
    "appamaññāya": "trạng thái không thể đo lường",
    "balehi": "sức mạnh", "aṅgehi": "chi phần", "ariyena": "cao quý", "aṭṭhaṅgikena": "gồm tám chi phần",
    "maggena": "con đường",
    "cetanāya": "chủ ý", "manasikārena": "sự chú tâm", "saññāya": "tri giác", "cittena": "tâm",
    # ---- triad / dyad references (bare X-ehi = the MATRIX / KD predicate, as map_6 / map_10)
    "sahagatehi": "đi kèm", "sahagatehi dhammehi": "hiện tượng có" + GAP + "đi kèm",   # KD sahagatā dhammā
    "vitakkehi": "sự hướng tâm", "vicārehi": "sự duy trì tâm",
    "pītikehi": "có sự hân hoan",                  # sappītikehi «có sự hân hoan» (pi-1 pītikā, map_7 / map_10)
    "savitakkehi": "có sự hướng tâm", "savicārehi": "có sự duy trì tâm",
    "sappītikehi dhammehi": "hiện tượng có sự hân hoan",
    "hetūhi": "gốc rễ", "hetukehi": "có gốc rễ", "sahetukehi": "có gốc rễ",
    "āsavehi": "ô nhiễm", "saṃyojanehi": "xiềng xích", "ganthehi": "nút thắt", "oghehi": "dòng lũ",
    "yogehi": "ách", "nīvaraṇehi": "chướng ngại", "parāmāsehi": "sự hiểu sai lệch",
    "parāmaṭṭhehi": "bị sự hiểu sai lệch nắm giữ",
    "cittehi": "tâm", "cetasikehi": "yếu tố đồng hành với tâm",
    "saṃsaṭṭhehi": "hòa lẫn", "saṃsaṭṭhehi dhammehi": "hiện tượng hòa lẫn",
    "samuṭṭhānehi": "do" + GAP + "sinh ra", "sahabhūhi": "cùng tồn tại", "anuparivattīhi": "vận hành theo",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi": "vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm",
    "upādānehi": "sự bám víu", "kilesehi": "phiền não", "saṃkilesikehi": "đối tượng của phiền não",
    "saṃkiliṭṭhehi": "bị phiền não làm vẩn đục",
    # ---- closing verse of ^3-447 = the verse of ^3-352 (map_10_vi.py, harmonised Vietnamese)
    "indriyā": "năng lực", "saccā": "sự thật", "upari": "tiếp theo", "gocchake": "nhóm",
    "tecattālīsaṃ": "bốn mươi ba", "antara": "xen giữa", "duke": "bộ đôi", "niddese": "phần giải thích",
    "saṅgahaṃ gatā": "đã được gộp vào", "navamassa": "thứ chín",
}

# per-segment choices (read from the segments)
# ^3-447 rūpa: the Pāli verse reads «Rūpakkhandhā cattāro» (ch10 ^3-352: «Arūpakkhandhā») and the Vietnamese has
# «Bốn khối vật chất», so context3 gives «vật chất» (no override; not map_10's «phi vật chất» of arūpa).
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def _value(kw, kws, text):
    """value() plus the «X dhammehi» rule of map_6_vi.py / map_10_vi.py: «hiện tượng X» / «hiện tượng là X» where the
    segment has it contiguous, else «hiện tượng … X»."""
    k = lc(kw)
    if k not in T13 and k.endswith(" dhammehi"):
        xv = _value(kw.rsplit(" ", 1)[0], kws, text)
        for cand in (f"hiện tượng {xv}", f"hiện tượng là {xv}"):
            if present(cand, text):
                return cand
        return "hiện tượng" + GAP + xv
    return value(kw, kws, T13, text)


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
