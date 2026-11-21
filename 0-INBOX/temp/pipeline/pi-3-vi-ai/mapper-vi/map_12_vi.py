"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 12-ekadasamanayo (method 11:
«Saṅgahitenasampayuttavippayuttapadaniddeso», association / dissociation of what is included).

usage: python -I -X utf8 map_12_vi.py                    (writes 12-ekadasamanayo.mapped.md and verifies it)
       python -I -X utf8 map_12_vi.py dump [miss]        (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_12_vi.py show lo hi         (segments lo..hi with every pair; writes nothing)

Importing this module writes nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T12 (this script's table) -> map_common_vi.value()
(context3 -> KD -> alternatives / counts / «X saṅgahito» / «X dhammā» -> pi-2 chain -> pi-1 chain).
Conventions: pi-1 vi-map-conventions.md + notes, pi-2 vi-map-conventions-pi2.md + notes, vi-map-conventions-pi3.md,
finished pi-3 chapters (map_3 … map_9_vi.py and their notes: ch4 / ch5 the inclusion relative clauses and the
closing verse, ch7 the association values, ch8 / ch9 the method nouns of the heading compound).

The frame of this method:
  «Samudayasaccena ye dhammā … saṅgahitā …, te dhammā katihi khandhehi … sampayuttā? Te dhammā tīhi khandhehi …
   sampayuttā; ekena khandhena … kehici sampayuttā. Katihi vippayuttā? …»
  «Đối với sự thật về sự phát sinh, những hiện tượng nào … được gộp vào …, thì những hiện tượng đó gắn liền với
   bao nhiêu khối …? … gắn liền với một số hiện tượng trong một khối, … Không gắn liền với bao nhiêu? …»
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi")
from map_common_vi import (GAP, NDE, build_part, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           present, read_keywords, read_pali, read_vietnamese, value, verify)

PART = "12-ekadasamanayo"

_GL, _KGL = "gắn liền", "không gắn liền"

T12 = {
    # ---- heading «Phương pháp thứ mười một»; colophon «…, phần thứ mười một»
    "ekādasama": "thứ mười một", "ekādasamo": "thứ mười một",
    # ---- heading compound «Giải thích đề mục về điều gắn liền và điều không gắn liền dựa trên điều được gộp vào»:
    # method nouns with the text's «điều» (as map_8_vi.py / map_9_vi.py)
    "sampayutta": "điều " + _GL, "vippayutta": "điều " + _KGL,
    # ---- the association frame (predicates; map_7_vi.py)
    "sampayuttā": _GL, "vippayuttā": _KGL, "natthi": "không có",
    "kehici": "một số hiện tượng",     # «gắn liền với một số hiện tượng trong một khối, …» (map_7_vi.py)
    # ---- reference words «Đối với X, những hiện tượng nào …» = X itself (map_4_vi.py / map_5_vi.py)
    "saccena": "sự thật",                          # samudayasaccena «sự thật về sự phát sinh»
    "indriyena": "năng lực", "indriyehi": "năng lực",   # «năng lực nữ tính», «năm năng lực»
    "sampayuttehi": _GL,                           # hetu- / āsava- / kilesasampayuttehi «vừa gắn liền với …»
    "manasikārena": "sự chú tâm", "phassena": "sự tiếp xúc", "cetanāya": "chủ ý",
    "upādānena": "sự bám víu", "taṇhāya": "khao khát", "avijjāya": "vô minh",
    "saṅkhārehi": "sự tạo tác",                    # avijjāpaccayā saṅkhārehi «… làm điều kiện cho các sự tạo tác»
    "bhavena": "sự hiện hữu",                      # kammabhavena «sự hiện hữu dưới dạng nghiệp»
    "sokena": "sự sầu muộn", "paridevena": "sự than khóc", "upāyāsena": "sự tuyệt vọng",
    "dukkhena": "sự khó chịu", "domanassena": "nỗi buồn",   # soka list (map_4_vi.py / map_6_vi.py)
    "upaṭṭhānena": "sự thiết lập",                 # satipaṭṭhānena «sự thiết lập tỉnh thức»
    "padhānena": "nỗ lực",                         # sammappadhānena «nỗ lực đúng đắn»
    "appamaññāya": "trạng thái không thể đo lường",
    "balehi": "sức mạnh", "aṅgehi": "chi phần",    # bojjhaṅgehi «bảy chi phần giác ngộ»
    "ariyena": "cao quý", "aṭṭhaṅgikena": "gồm tám chi phần", "maggena": "con đường",
    # cluster plurals «các hiện tượng là X» = the MATRIX noun (map_5_vi.py; upādānehi map_4_vi.py)
    "hetūhi": "gốc rễ", "āsavehi": "ô nhiễm", "saṃyojanehi": "xiềng xích", "ganthehi": "nút thắt",
    "oghehi": "dòng lũ", "yogehi": "ách", "nīvaraṇehi": "chướng ngại", "parāmāsehi": "sự hiểu sai lệch",
    "upādānehi": "sự bám víu", "kilesehi": "phiền não",
    "saṃkilesikehi": "đối tượng của phiền não",    # «vừa là đối tượng của phiền não»
    "saṃkiliṭṭhehi": "bị phiền não làm vẩn đục",
    # ---- closing verse of ^3-416 (= ^3-192 of map_5_vi.py): «Hai sự thật, mười lăm năng lực, mười một đề mục về sự
    # sinh khởi tùy thuộc vào điều kiện; Tiếp theo lại có mười một, ở đây các đề mục thuộc các nhóm có ba mươi loại»
    "uddhaṃ": "tiếp theo", "gocchaka": "nhóm", "vidhā": "loại", "tiṃsa": "ba mươi", "pannarasa": "mười lăm",
}

# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value(kw, kws, T12, vi.get(bid, ""))
    return resolve


def dump(only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v == "???" or (v != NDE and not present(v, vi.get(bid, ""))):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        p1 = [x for x, _ in pi1_map_values(kw).most_common(2) if x != v]
        p2 = [x for x, _ in pi2_map_values(kw).most_common(2) if x != v]
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  pi1:{p1}" if p1 else "") + (f"  pi2:{p2}" if p2 else "")
              + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi):
    res = resolver()
    vi, pi = read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]\n-- PI {pi.get(bid, '')}\n-- VI {vi.get(bid, '')}")
            print("   " + " | ".join(f"{kw}={res(bid, kw, kws)}" for kw in kws))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]))
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
