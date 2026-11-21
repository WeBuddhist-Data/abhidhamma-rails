"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 9-atthamanayo (method 8: «Vippayuttena-
sampayuttapadaniddeso», association with what is dissociated).

usage: python -I -X utf8 map_9_vi.py                     (writes 9-atthamanayo.mapped.md and verifies it)
       python -I -X utf8 map_9_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_9_vi.py show lo hi          (segments lo..hi with every pair; writes nothing)

Importing this module writes nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T09 (this script's table) -> map_common_vi.value()
(context3 -> KD -> alternatives / counts / «X saṅgahito» / «X dhammā» -> pi-2 chain -> pi-1 chain).
Conventions: pi-1 vi-map-conventions.md + notes, pi-2 vi-map-conventions-pi2.md + notes, vi-map-conventions-pi3.md,
finished pi-3 chapters (map_3/4/5/7_vi.py and their notes; ch7 settled the association values).

The frame of this method:
  «Rūpakkhandhena ye dhammā vippayuttā, te dhammā katihi khandhehi katihāyatanehi katihi dhātūhi sampayuttāti? Natthi.»
  «Đối với khối vật chất, những hiện tượng nào không gắn liền với nó, thì những hiện tượng đó gắn liền với bao nhiêu
   khối, bao nhiêu lĩnh vực nhận biết, bao nhiêu yếu tố? Không có.»
  sampayuttā = gắn liền, vippayuttā = không gắn liền, Natthi = không có (map_7_vi.py); X-kkhandhena = khối X
  (map_4_vi.py; «đối với» is the case frame).
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-3-vi-ai\mapper-vi")
from map_common_vi import (GAP, NDE, build_part, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           present, read_keywords, read_pali, read_vietnamese, value, verify)

PART = "9-atthamanayo"

_GL, _KGL = "gắn liền", "không gắn liền"

T09 = {
    # ---- heading «Phương pháp thứ tám»; colophon «…, phần thứ tám»
    "aṭṭhama": "thứ tám", "aṭṭhamo": "thứ tám",
    # ---- heading / colophon «Giải thích đề mục về điều gắn liền dựa trên điều không gắn liền»: method nouns
    # (the text's «điều» kept, as asaṅgahita = điều không được gộp vào of map_3_vi.py / map_4_vi.py)
    "sampayutta": "điều " + _GL, "vippayutta": "điều " + _KGL,
    # ---- the association frame (predicates; map_7_vi.py)
    "sampayuttā": _GL, "vippayuttā": _KGL, "natthi": "không có",
    # ---- reference words «Đối với khối X» (X-kkhandhena = khối X, as map_4_vi.py)
    "rūpakkhandhena": "khối vật chất", "vedanākkhandhena": "khối cảm giác", "saññākkhandhena": "khối tri giác",
    "saṅkhārakkhandhena": "khối tạo tác", "viññāṇakkhandhena": "khối thức",
    "viññāṇa": "thức",
    # «đối với các hiện tượng có xung đột … không có xung đột» (araṇehi: the positive part, KD raṇā)
    "saraṇehi dhammehi": "hiện tượng có xung đột", "raṇehi": "xung đột",
    # ---- summary verse of ^3-318
    "jīvitaṃ": "sự sống",                    # «rồi sự sống» (map_7_vi.py)
    "mataṃ": "sự chết",                      # jātijarāmataṃ «sự sinh, sự lão hóa, sự chết»
    "labbhare": "tìm thấy",                  # na labbhare «thì không tìm thấy» («không» = na; ch7 labbhati «có»)
    "antare": "phần xen giữa",               # Paṭhamantare «trong phần xen giữa thứ nhất» (map_7_vi.py)
    "gocchake": "nhóm",                      # «mười trong các nhóm» («trong các» frame; map_5/7 gocchaka)
    "cuddasa": "mười bốn",
    "sattacattālīsa": "bốn mươi bảy",
    "sattacattālīsa dhammā": "bốn mươi bảy hiện tượng",   # «bốn mươi bảy hiện tượng này» (Vietnamese order)
    "samucchede": "sự phân tách",            # «Không tìm thấy trong sự phân tách» («trong» frame)
    "mogha": "rỗng", "pucchakena": "câu hỏi",   # moghapucchakena «do câu hỏi rỗng» («do» frame)
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
        return value(kw, kws, T09, vi.get(bid, ""))
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
