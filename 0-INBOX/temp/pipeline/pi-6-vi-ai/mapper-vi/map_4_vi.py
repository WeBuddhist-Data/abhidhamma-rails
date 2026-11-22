"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 4-dhatuyamaka (the whole Dhātuyamaka: paṇṇattivāra, pavatti
present uppādavāra, pariññāvāra, closer).

usage: python -I -X utf8 -B map_4_vi.py                (writes 4-dhatuyamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_4_vi.py dump [miss]     (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_4_vi.py show lo hi [pi] (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setters: map_3-05_vi (value305 -> value304 -> value303 (Itaresaṃ +
plane-being rule) -> value302 (accusative / ablative planes, positional beings) -> map_3-01_vi (BARE, ATTR, SENSE,
PLANE_LOC, HEADS, value3) / map_2-01_vi.frames201 (verb_value for every uppajjati / nirujjhati keyword)),
map_2-02_vi.parinna_value (pariññāvāra), the yamaka titles in running text lower case as 6-02 / 9-03 / 8 map them.
The Āyatana members map to «lĩnh vực …»; the Dhātu members here to «yếu tố …» as the text has them (rūpadhātu = yếu tố
hình sắc: the eighteen elements, not the plane «cõi hình sắc» of rūpadhātuyā).
Resolver: OVERRIDES -> T4 (this chapter: members, bare viññāṇa words, headings) -> titles -> parinna_value ->
map_3-05_vi.value305.
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes, vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md,
notes-map-3-01.md … notes-map-3-06.md, notes-map-6-02.md, notes-map-9-03.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import map_sample_vi as S  # noqa: E402
from map_common_vi import (NDE, build_part, en, lc, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)

A35 = importlib.import_module("map_3-05_vi")
P = importlib.import_module("map_2-02_vi")        # parinna_value

PART = "4-dhatuyamaka"

# ---------------------------------------------------------------------------- the eighteen elements (^6-4-1)
# «Mười tám yếu tố – yếu tố mắt, …, yếu tố đối tượng của ý.» (pi-6 conventions: X-dhātu = yếu tố X, X-viññāṇadhātu =
# yếu tố thức qua X, manoviññāṇadhātu = yếu tố ý thức, dhammadhātu = yếu tố đối tượng của ý)
DHATU = {
    "cakkhu": "yếu tố mắt", "sota": "yếu tố tai", "ghāna": "yếu tố mũi", "jivhā": "yếu tố lưỡi",
    "kāya": "yếu tố thân", "rūpa": "yếu tố hình sắc", "sadda": "yếu tố âm thanh", "gandha": "yếu tố mùi",
    "rasa": "yếu tố vị", "phoṭṭhabba": "yếu tố vật xúc chạm",
    "cakkhuviññāṇa": "yếu tố thức qua mắt", "sotaviññāṇa": "yếu tố thức qua tai",
    "ghānaviññāṇa": "yếu tố thức qua mũi", "jivhāviññāṇa": "yếu tố thức qua lưỡi",
    "kāyaviññāṇa": "yếu tố thức qua thân",
    "mano": "yếu tố ý", "manoviññāṇa": "yếu tố ý thức", "dhamma": "yếu tố đối tượng của ý",
}
# every keyword form: bare, plural / question (-dhātū, -dhātūti), accusative -dhātuṃ, -ñca / -ñceva (no word of their
# own; «vừa … vừa», «và» are frame), -dhātuyo
_DHATU_SUF = ("dhātu", "dhātū", "dhātūti", "dhātuṃ", "dhātuñca", "dhātuñceva", "dhātuyo")

# dhātu itself («Các yếu tố có phải là mắt không?», «Mười tám yếu tố»): leading «Các» frame (as 3-01 āyatanā)
DHATU_BARE = {s: "yếu tố" for s in _DHATU_SUF}

# ---------------------------------------------------------------------------- the bare consciousness words
# «Thức qua mắt có phải là yếu tố thức qua mắt không?», «Ý thức có phải là yếu tố ý thức không?» (subject of the pair)
VINNANA = {
    "cakkhuviññāṇa": "thức qua mắt", "sotaviññāṇa": "thức qua tai", "ghānaviññāṇa": "thức qua mũi",
    "jivhāviññāṇa": "thức qua lưỡi", "kāyaviññāṇa": "thức qua thân", "manoviññāṇa": "ý thức",
}

# ---------------------------------------------------------------------------- headings, notes, closers
HEAD4 = {
    "suddhadhātuvāro": "mục về các yếu tố thuần túy",                       # = Suddhāyatanavāro (3-01)
    "suddhadhātumūlacakkavāro": "mục về vòng luân chuyển dựa trên các yếu tố thuần túy",
    # ^6-4-6 / ^6-4-15 «jivha ṭhapetvā» (short vowel, as written) «ngoại trừ lưỡi»
    "jivha": "lưỡi",
    # ^6-4-10 (Jivhāpi ghānadhātusadisā) «(Lưỡi cũng giống như yếu tố mũi)»; (Saddo ghānasadiso) «(Âm thanh giống như
    # mũi)»: -pi no word of its own («cũng» frame), -sadisa = «giống như» + the member (3-01 yassakasadisaṃ)
    "jivhāpi": "lưỡi",
    "ghānadhātusadisā": "giống như yếu tố mũi",
    "ghānasadiso": "giống như mũi",
}

T4 = {}
for _stem, _v in DHATU.items():
    for _suf in _DHATU_SUF:
        T4[_stem + _suf] = _v
T4.update(DHATU_BARE)
for _stem, _v in VINNANA.items():
    for _suf in ("ṃ", "nti", "ñca", "ñceva"):
        T4[_stem + _suf] = _v
T4.update(HEAD4)

# ---------------------------------------------------------------------------- the yamaka titles
# heading «### Các cặp câu hỏi về các yếu tố» keeps «Các» (map_sample_vi.FORMULAS); in running text and in the closer
# «Phần các cặp câu hỏi về các yếu tố đã hoàn tất.» lower case as written («Phần» frame; -pi, the locative «trong» and
# the genitive «của» no word of their own): = 6-02 khandhayamake / saṅkhārayamakepi, 9-03 / 3-06 closers, 8 TITLE_RUNNING
_TITLE = {
    "dhātuyamak": S.FORMULAS["dhātuyamakaṃ"],
    "āyatanayamak": S.FORMULAS["āyatanayamakaṃ"],
}
_TITLE_END = ("aṃ", "e", "assa", "ampi", "epi")


def title_value(kw, vi):
    k = lc(kw).lower()
    for st, v in _TITLE.items():
        if k.startswith(st) and k[len(st):] in _TITLE_END:
            if vi.lstrip().startswith("#"):
                return v
            return v[:1].lower() + v[1:]
    return None


# per-segment choices (read from the segments): none needed
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value4(kw, kws, vi, pi):
    for x in (kw, lc(kw), lc(kw).lower()):
        if x in T4:
            return T4[x]
    v = title_value(kw, vi)
    if v is not None:
        return v
    v = P.parinna_value(kw, pi)
    if v is not None:
        return v
    return A35.value305(kw, kws, vi, pi)


def resolver_for(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value4(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(part=PART, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError as e:
                v = f"KEYERROR {e}"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v != NDE and not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        e = en(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  en:{e}" if e else "") + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi, with_pali=False, part=PART):
    res = resolver_for(part)
    vi, pi = read_vietnamese(part), read_pali(part)
    for i, (bid, kws) in enumerate(read_keywords(part)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            if with_pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"-- VI {vi.get(bid, '')}")
            out = []
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError as e:
                    v = f"KEYERROR {e}"
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                out.append(f"{kw}={v}{flag}")
            print("   " + " | ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(PART, sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    else:
        build_part(PART, resolver_for(PART))
        verify(PART, ALLOWED)
