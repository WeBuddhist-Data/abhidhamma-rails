"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 6-pancamanayo.

usage: python -I -X utf8 map_6_vi.py                     (writes 6-pancamanayo.mapped.md and verifies it)
       python -I -X utf8 map_6_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_6_vi.py show lo hi          (segments lo..hi with every pair; writes nothing)

Importing this module writes nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T6 (this script's table) -> map_common_vi.value()
(context3 -> KD -> alternatives / counts / «X saṅgahito» / «X dhammā» -> pi-2 chain -> pi-1 chain).
Conventions: pi-1 vi-map-conventions.md, pi-2 vi-map-conventions-pi2.md, pi-3 vi-map-conventions-pi3.md
(approved sample: map_sample_vi.py), finished chapter 5 (map_5_vi.py, notes-map-5.md).
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, NDE, build_part, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           present, read_keywords, read_pali, read_vietnamese, value, verify)

PART = "6-pancamanayo"

_DH = "theo cách gộp vào khối"

# part table (method 5: «Đối với X, những hiện tượng nào không được gộp vào theo cách gộp vào khối, …, đối với những
# hiện tượng ấy, những hiện tượng nào …, thì những hiện tượng đó không được gộp vào …»). Lower-case keys.
T6 = {
    # heading «Phương pháp thứ năm» / «Giải thích đề mục về điều không được gộp vào dựa trên điều không được gộp vào»
    "pañcama": "thứ năm",
    "asaṅgahita": "điều không được gộp vào",            # method noun (as map_3_vi.py)
    # artefact pairs «… ye dhammā khandhasaṅgahena»: the reference word … «theo cách gộp vào khối»
    "dhammehi khandhasaṅgahena": "hiện tượng" + GAP + _DH,    # as map_5_vi.py
    "indriyena khandhasaṅgahena": "năng lực" + GAP + _DH,     # manindriyena / jīvitindriyena / kāyindriyena …
    # Nāmarūpapaccayā saḷāyatanena «phần tinh thần và vật chất làm điều kiện cho sáu lĩnh vực nhận biết»
    "paccayā āyatanena": "làm điều kiện cho" + GAP + "lĩnh vực nhận biết",
    # the reference «Đối với X» (X-ena / X-āya / X-ehi = X itself; «đối với» is the case frame)
    "rūpakkhandhena": "khối vật chất", "vedanākkhandhena": "khối cảm giác", "saññākkhandhena": "khối tri giác",
    "saṅkhārakkhandhena": "khối tạo tác", "viññāṇakkhandhena": "khối thức",
    "cakkhāyatanena": "lĩnh vực mắt", "phoṭṭhabbāyatanena": "lĩnh vực vật xúc chạm", "manāyatanena": "lĩnh vực ý",
    "cakkhudhātuyā": "yếu tố mắt", "phoṭṭhabbadhātuyā": "yếu tố vật xúc chạm",
    "cakkhuviññāṇadhātuyā": "yếu tố thức qua mắt", "manodhātuyā": "yếu tố ý",
    "manoviññāṇadhātuyā": "yếu tố ý thức",
    "cakkhundriyena": "năng lực mắt", "indriyena": "năng lực", "indriyehi": "năng lực",
    "saccena": "sự thật",
    "avijjāya": "vô minh",
    "saṅkhārena": "sự tạo tác",                     # avijjāpaccayā saṅkhārena «vô minh làm điều kiện cho các sự tạo tác»
    "viññāṇena": "thức",                            # saṅkhārapaccayā viññāṇena «… làm điều kiện cho thức»
    "nāmarūpena": "phần tinh thần và vật chất",
    "phassena": "sự tiếp xúc", "taṇhāya": "khao khát", "upādānena": "sự bám víu",
    "bhavena": "sự hiện hữu",
    "jātiyā": "sự sinh", "jarāya": "sự lão hóa", "maraṇena": "sự chết",
    "paridevena": "sự than khóc", "sokena": "sự sầu muộn", "dukkhena": "sự khó chịu", "domanassena": "nỗi buồn",
    "upāyāsena": "sự tuyệt vọng",
    "upaṭṭhānena": "sự thiết lập", "padhānena": "nỗ lực", "jhānena": "tầng thiền",
    "appamaññāya": "trạng thái không thể đo lường",
    "balehi": "sức mạnh", "aṅgehi": "chi phần",
    "ariyena": "cao quý", "aṭṭhaṅgikena": "gồm tám chi phần", "maggena": "con đường",
    "manasikārena": "sự chú tâm", "cetanāya": "chủ ý",
    "cittena": "tâm",
    # triad / dyad references (X-ehi dhammehi «các hiện tượng X»; bare X-ehi = the MATRIX / KD predicate)
    "kusalehi": "thiện", "akusalehi": "bất thiện",
    "upādāniyehi": "đối tượng của sự bám víu",       # of anupādāniyehi «không phải là đối tượng của sự bám víu»
    "saṃkilesikehi": "đối tượng của phiền não",      # as map_5_vi.py
    "saṃkiliṭṭhehi": "bị phiền não làm vẩn đục",
    "sahagatehi": "đi kèm", "sahagatehi dhammehi": "hiện tượng có" + GAP + "đi kèm",   # KD sahagatā dhammā
    "pahātabbehi": "cần dứt bỏ", "bhāvanāya pahātabbehi": "cần dứt bỏ bằng sự tu tập",
    "hetukehi": "có gốc rễ", "sahetukehi": "có gốc rễ",
    "gāmīhi": "dẫn đến",
    "sekkhehi": "thuộc về người còn đang tu học", "asekkhehi": "thuộc về người đã hoàn tất tu học",
    "mahaggatehi": "rộng lớn", "appamāṇehi": "không thể đo lường",
    "ārammaṇehi": "có đối tượng",                    # parittārammaṇehi … / sārammaṇehi / of anārammaṇehi
    "hīnehi": "thấp kém", "paṇītehi": "ưu việt",
    "niyatehi": "cố định",
    "adhipatīhi": "lấy" + GAP + "làm yếu tố chủ đạo",   # maggādhipatīhi «lấy con đường làm yếu tố chủ đạo»
    "vicārehi": "sự duy trì tâm", "vitakkehi": "sự hướng tâm",
    "sampayuttehi": "gắn liền", "vippayuttehi": "không gắn liền",   # «với» dropped (map_5_vi.py)
    "hetūhi": "gốc rễ",
    "asaṅkhatehi": "không do điều kiện tạo thành",
    "sanidassanehi": "thấy được",
    "rūpīhi": "thuộc vật chất", "arūpīhi": "phi vật chất", "lokuttarehi": "vượt thế gian",
    "āsavehi": "ô nhiễm", "anāsavehi": "không phải là đối tượng của ô nhiễm",
    "saṃyojanehi": "xiềng xích", "ganthehi": "nút thắt", "oghehi": "dòng lũ", "yogehi": "ách",
    "nīvaraṇehi": "chướng ngại", "parāmāsehi": "sự hiểu sai lệch",
    "parāmaṭṭhehi": "bị sự hiểu sai lệch nắm giữ",   # also of aparāmaṭṭhehi «không bị …» (positive part)
    "cittehi": "tâm", "cetasikehi": "yếu tố đồng hành với tâm",
    "saṃsaṭṭhehi": "hòa lẫn", "samuṭṭhānehi": "do" + GAP + "sinh ra", "sahabhūhi": "cùng tồn tại",
    "anuparivattīhi": "vận hành theo", "cittānuparivattīhi": "vận hành theo tâm",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattīhi": "vừa hòa lẫn với tâm vừa do tâm sinh ra vừa vận hành theo tâm",
    "bāhirehi": "thuộc phần bên ngoài", "ajjhattikehi": "thuộc phần bên trong",
    "upādādhammehi": "hiện tượng phái sinh",         # as map_3_vi.py
    "upādānehi": "sự bám víu", "kilesehi": "phiền não",
    "kāmāvacarehi": "thuộc cõi dục lạc", "avacarehi": "thuộc cõi",   # of na kāmāvacarehi / rūpāvacarehi …
    "pariyāpannehi": "nằm trong các cõi tồn tại",    # of apariyāpannehi «không nằm trong các cõi tồn tại»
    "anuttarehi": "không có điều gì cao hơn",
    "raṇehi": "xung đột", "saraṇehi dhammehi": "hiện tượng có xung đột",
    "sappītikehi dhammehi": "hiện tượng có sự hân hoan",
    "savitakkehi": "có sự hướng tâm", "savicārehi": "có sự duy trì tâm",
    "niyyānikehi": "dẫn đến giải thoát", "visaṃsaṭṭhehi": "không hòa lẫn",
    # summary verse of ^3-227 («Vật chất, lĩnh vực đối tượng của ý, …; Hai loại hiện hữu, sự sinh, sự lão hóa, sự
    # chết, điều thuộc vật chất, …; Điều thuộc phần bên ngoài và điều phái sinh, hai điều; phạm vi … của phương pháp
    # này đã được hiểu rõ.»)
    "maccu": "sự chết", "pumaṃ": "nam tính", "jīvitaṃ": "sự sống",
    "ārammaṇaṃ": "có đối tượng",                     # of anārammaṇaṃ «điều không có đối tượng» (positive part)
    "bāhiraṃ": "điều thuộc phần bên ngoài",          # the text's «điều» kept (as map_3_vi.py Anidassanaṃ)
    "buddho": "đã được hiểu", "su": "rõ",           # subuddho «đã được hiểu rõ»
}

# per-segment choices
OVERRIDES = {
    # nevasaññānāsaññābhavena «sự hiện hữu không phải có tri giác cũng không phải không có tri giác» / asaññābhavena
    # «sự hiện hữu không có tri giác»: saññā of the bhava list = có tri giác (as map_3_vi.py ^3-174)
    "3-205": {"saññā": "có tri giác"},
    "3-206": {"saññā": "có tri giác"},
}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def _value(kw, kws, text):
    """value() plus the «X dhammehi» rule (as map_common_vi's «X dhammā»): «hiện tượng X» / «hiện tượng là X» where
    the segment has it contiguous, else «hiện tượng … X»."""
    k = lc(kw)
    if k not in T6 and k.endswith(" dhammehi"):
        xv = _value(kw.rsplit(" ", 1)[0], kws, text)
        for cand in (f"hiện tượng {xv}", f"hiện tượng là {xv}"):
            if present(cand, text):
                return cand
        return "hiện tượng" + GAP + xv
    return value(kw, kws, T6, text)


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return _value(kw, kws, vi.get(bid, ""))
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
