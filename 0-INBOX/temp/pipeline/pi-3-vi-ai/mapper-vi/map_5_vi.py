"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 5-catutthanayo.

usage: python -I -X utf8 map_5_vi.py                  (writes 5-catutthanayo.mapped.md and verifies it)
       python -I -X utf8 map_5_vi.py show lo hi       (segments lo..hi with every pair; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> T05 (this script's table) -> map_common_vi.value()
(context3 -> KD -> alternatives / counts / «X saṅgahito» / «X dhammā» -> pi-2 chain -> pi-1 chain).
Conventions: pi-1 vi-map-conventions.md + notes, pi-2 vi-map-conventions-pi2.md + notes, vi-map-conventions-pi3.md.
Importing this module writes nothing.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, build_part, read_keywords, read_pali, read_vietnamese,  # noqa: E402
                           value, verify)

PART = "5-catutthanayo"

# Instrumental reference words of the inclusion frame («Đối với X, những hiện tượng nào …»: X itself, «đối với» is
# the case frame) and the closing verse of ^3-192. Lower-case keys (lookup is case-insensitive on the first letter).
T05 = {
    # «tehi dhammehi ye dhammā khandhasaṅgahena …» «đối với những hiện tượng ấy, những hiện tượng nào … theo cách
    # gộp vào khối» (dhammehi = hiện tượng, as the pi-2 map; «ấy» = tehi, not in the keyword)
    "dhammehi khandhasaṅgahena": "hiện tượng" + GAP + "theo cách gộp vào khối",
    "saccena": "sự thật",                          # samudayasaccena «sự thật về sự phát sinh»
    "indriyena": "năng lực", "indriyehi": "năng lực",   # «năng lực nữ tính», «năm năng lực»
    "sampayuttehi": "gắn liền",                    # hetu- / kilesasampayuttehi «vừa gắn liền với …» («với» dropped)
    "manasikārena": "sự chú tâm", "phassena": "sự tiếp xúc", "cetanāya": "chủ ý",
    "upādānena": "sự bám víu", "taṇhāya": "khao khát", "avijjāya": "vô minh",
    "saṅkhārena": "sự tạo tác",                    # avijjāpaccayā saṅkhārena «vô minh làm điều kiện cho các sự tạo tác»
    "bhavena": "sự hiện hữu",                      # kammabhavena «sự hiện hữu dưới dạng nghiệp»
    "sokena": "sự sầu muộn", "paridevena": "sự than khóc", "upāyāsena": "sự tuyệt vọng",
    "upaṭṭhānena": "sự thiết lập",                 # satipaṭṭhānena «sự thiết lập tỉnh thức»
    "padhānena": "nỗ lực",                         # sammappadhānena «nỗ lực đúng đắn»
    "appamaññāya": "trạng thái không thể đo lường",
    "balehi": "sức mạnh", "aṅgehi": "chi phần",    # bojjhaṅgehi «bảy chi phần giác ngộ»
    "ariyena": "cao quý", "aṭṭhaṅgikena": "gồm tám chi phần", "maggena": "con đường",
    "hetūhi": "gốc rễ",                            # «các hiện tượng là gốc rễ»
    "āsavehi": "ô nhiễm", "saṃyojanehi": "xiềng xích", "ganthehi": "nút thắt", "oghehi": "dòng lũ",
    "yogehi": "ách", "nīvaraṇehi": "chướng ngại", "parāmāsehi": "sự hiểu sai lệch",
    "kilesehi": "phiền não", "saṃkilesikehi": "đối tượng của phiền não",   # «vừa là đối tượng của phiền não»
    "saṃkiliṭṭhehi": "bị phiền não làm vẩn đục",
    # closing verse «Hai sự thật, mười lăm năng lực, mười một đề mục về sự sinh khởi tùy thuộc vào điều kiện;
    # Tiếp theo lại có mười một, ở đây các đề mục thuộc các nhóm có ba mươi loại»
    "uddhaṃ": "tiếp theo",
    "gocchaka": "nhóm",                            # gocchakapadamettha «các đề mục thuộc các nhóm» («các» dropped)
    "vidhā": "loại",                               # tiṃsavidhā «có ba mươi loại» (not pi-2 «sự so sánh»)
    "tiṃsa": "ba mươi",
}

OVERRIDES = {}

ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value(kw, kws, T05, vi.get(bid, ""))
    return resolve


def show(lo, hi):
    res = resolver()
    vi, pi = read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                print(f"   {kw}={v}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]))
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
