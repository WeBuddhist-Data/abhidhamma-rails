"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 10-navamanayo (method 9: association by
association, «Sampayuttenasampayuttapadaniddeso»).

usage: python -I -X utf8 map_10_vi.py                     (writes 10-navamanayo.mapped.md and verifies it)
       python -I -X utf8 map_10_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_10_vi.py show lo hi          (segments lo..hi with every pair; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> «X dhammehi» rule (as map_6_vi.py) -> T10 (this script's table)
-> map_common_vi.value() (context3 -> KD -> alternatives / counts / «X saṅgahito» / «X dhammā» -> pi-2 chain ->
pi-1 chain). Reuses the tables of map_common_vi.py / map_sample_vi.py read-only.
Conventions: pi-1 vi-map-conventions.md + notes, pi-2 vi-map-conventions-pi2.md + notes, vi-map-conventions-pi3.md,
finished chapters 3-7 (map_3 … map_7_vi.py and their notes).

The frame of this method:
  «X-ena ye dhammā sampayuttā, tehi dhammehi ye dhammā sampayuttā, te dhammā katihi khandhehi … sampayuttā?
   Te dhammā tīhi khandhehi … sampayuttā; ekenāyatanena ekāya dhātuyā kehici sampayuttā.»
  «Đối với X, những hiện tượng nào gắn liền với nó, đối với những hiện tượng ấy, những hiện tượng nào gắn liền với
   chúng, thì những hiện tượng đó gắn liền với bao nhiêu khối …? … gắn liền với một số hiện tượng trong một lĩnh vực
   nhận biết, một yếu tố.»
"""
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi")
from map_common_vi import (GAP, NDE, build_part, lc, present, read_keywords, read_vietnamese,  # noqa: E402
                           value, verify)
import map_sample_vi as S  # noqa: E402

PART = "10-navamanayo"

T10 = {
    # ---- the association frame (as map_7_vi.py): predicate, «với» dropped; kehici = một số hiện tượng
    "sampayuttā": "gắn liền",
    "kehici": "một số hiện tượng",
    # ---- heading «Phương pháp thứ chín»; «Giải thích đề mục về điều gắn liền dựa trên điều gắn liền»
    "navama": "thứ chín", "navamassa": "thứ chín",
    "sampayutta": "điều gắn liền",                 # method noun of the heading compound (as map_8 / map_3 asaṅgahita)
    # ---- reference words «Đối với X» = X itself («đối với» is the case frame), as map_3 … map_8
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
    # ---- triad / dyad references (bare X-ehi = the MATRIX / KD predicate, as map_6_vi.py)
    "sahagatehi": "đi kèm", "sahagatehi dhammehi": "hiện tượng có" + GAP + "đi kèm",   # KD sahagatā dhammā
    "vitakkehi": "sự hướng tâm", "vicārehi": "sự duy trì tâm",
    "pītikehi": "có sự hân hoan",                  # sappītikehi «có sự hân hoan» (pi-1 pītikā, map_7)
    "savitakkehi": "có sự hướng tâm", "savicārehi": "có sự duy trì tâm",   # as map_6_vi.py
    "sappītikehi dhammehi": "hiện tượng có sự hân hoan",                  # as map_6_vi.py
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
    # ---- summary verse of ^3-352 («Bốn khối phi vật chất, và cả lĩnh vực ý; / Bảy yếu tố thức, hai sự thật, mười
    # bốn năng lực. / Trong phần điều kiện có mười hai đề mục, tiếp theo đó có mười sáu; / Trong các bộ ba có tám, và
    # trong các nhóm có cả bốn mươi ba. / Trong các bộ đôi xen giữa lớn có bảy, trong các bộ đôi cuối có sáu đề mục; /
    # Những đề mục này đã được gộp vào trong phần giải thích đề mục thứ chín.»)
    "indriyā": "năng lực",                         # cuddasindriyā (as map_3 Sattindriyā)
    "saccā": "sự thật",                            # dve saccā (as map_4 / map_5)
    "upari": "tiếp theo",                          # tato upari «tiếp theo đó» («đó» = tato; as map_4 cuddasūpari)
    "gocchake": "nhóm",                            # «trong các nhóm» («trong các» frame; as map_4 / map_5 / map_7)
    "tecattālīsaṃ": "bốn mươi ba",
    "antara": "xen giữa",                          # Mahantaraduke «bộ đôi xen giữa lớn» (as map_4 antara)
    "duke": "bộ đôi",                              # Mahantaraduke / piṭṭhi dukesu «bộ đôi … / bộ đôi cuối»
    "niddese": "phần giải thích",                  # locative «trong phần giải thích» («trong» frame; as map_7 antare)
    "saṅgahaṃ gatā": "đã được gộp vào",            # «đã được gộp vào» (Vietnamese as it stands)
}

# per-segment choices (read from the segments)
OVERRIDES = {
    # Arūpakkhandhā «Bốn khối phi vật chất»: arūpa = phi vật chất (pi-1 arūpino), not the bhava-list «không hình sắc»
    "3-352": {"arūpa": "phi vật chất"},
}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def _value(kw, kws, text):
    """value() plus the «X dhammehi» rule of map_6_vi.py: «hiện tượng X» / «hiện tượng là X» where the segment has it
    contiguous, else «hiện tượng … X»."""
    k = lc(kw)
    if k not in T10 and k.endswith(" dhammehi"):
        xv = _value(kw.rsplit(" ", 1)[0], kws, text)
        for cand in (f"hiện tượng {xv}", f"hiện tượng là {xv}"):
            if present(cand, text):
                return cand
        return "hiện tượng" + GAP + xv
    return value(kw, kws, T10, text)


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
