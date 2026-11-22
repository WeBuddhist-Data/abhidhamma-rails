"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 6-02-sankharayamaka (Saṅkhārayamaka, second half: the rest of
the pavatti section (nirodhavāra, uppādanirodhavāra) and the pariññāvāra).

usage: python -I -X utf8 -B map_6-02_vi.py                     (writes 6-02-sankharayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_6-02_vi.py dump [miss]          (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_6-02_vi.py show lo hi [pi]      (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setters: map_6-01_vi (value601: the Saṅkhārayamaka members, breathing,
jhānas, citta kinds, moments, beings), map_2-01_vi (verb_value for every uppajjati / nirujjhati keyword), map_2-02_vi
(parinna_value for the pariññāvāra), map_8_vi (moments), map_sample_vi (FORMULAS / value6).
Resolution: OVERRIDES[bid][kw] -> value602(): T602 -> parinna_value -> map_6-01_vi.value601 (T601 -> 6-01 rules ->
2-01 frames -> value6).
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md, notes-map-2-01.md, notes-map-2-02.md, notes-map-8.md,
notes-map-6-01.md, notes-map-6-02.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import map_sample_vi as S  # noqa: E402,F401
from map_common_vi import (GAP, NDE, build_part, en, lc, present, read_keywords, read_pali,  # noqa: E402,F401
                           read_vietnamese, verify)

X = importlib.import_module("map_6-01_vi")        # frame-setter of the Saṅkhārayamaka
K = importlib.import_module("map_2-01_vi")        # verb_value
P = importlib.import_module("map_2-02_vi")        # parinna_value (pariññāvāra)

PART = "6-02-sankharayamaka"

# ---------------------------------------------------------------------------- headings and editorial lines
HEAD602 = {
    # ^6-6-29-1-0 «1-6. Mục về hiện tại và các mục khác» (= sample Hetuvārādi: inner «các» kept)
    "paccuppannavārādi": "mục về hiện tại và các mục khác",
    # the -pi / locative / instrumental forms of the vāra names (-pi no word; «trong», «giống như» frame; 3-04, 5-02)
    "uppādavārepi": "mục về sự sinh khởi",
    "uppādanirodhavārepi": "mục về sự sinh khởi và sự chấm dứt",
    # ^6-6-147 uppādavāranirodhavārepi «trong mục về sự sinh khởi và sự chấm dứt» (= uppādanirodhavāra)
    "uppādavāranirodhavārepi": "mục về sự sinh khởi và sự chấm dứt",
    "nirodhavārena": "mục về sự chấm dứt",           # ^6-6-158 «giống như mục về sự chấm dứt»
    # ^6-6-130 (itaresaṃ yatthakānaṃ sadisaṃ) «(giống như các phần về nơi chốn khác)»: leading «các» frame,
    # «khác» = itaresaṃ (no keyword here); 2-02 yatthakaṃ
    "yatthakānaṃ": "phần về nơi chốn",
    # ^6-6-159 (Yathā khandhayamake pariññāvāraṃ vibhattaṃ evaṃ saṅkhārayamakepi pariññāvāraṃ vibhajitabbaṃ.)
    # «(Như mục về sự hiểu biết trọn vẹn đã được phân tích trong phần các cặp câu hỏi về các khối, trong phần các
    # cặp câu hỏi về các tạo tác, …)»: the titles in running text lower case as written (8 TITLE_RUNNING, «Phần»
    # frame, -pi no word)
    "khandhayamake": "các cặp câu hỏi về các khối",
    "saṅkhārayamakepi": "các cặp câu hỏi về các tạo tác",
    "pariññāvāraṃ": "mục về sự hiểu biết trọn vẹn",
    # closer «Saṅkhārayamakaṃ niṭṭhitaṃ.» «Phần các cặp câu hỏi về các tạo tác đã hoàn tất.» (lower case as written,
    # as 8 cittayamakaṃ and the 2-02 Khandhayamakapāḷi closer; «Phần» frame)
    "saṅkhārayamakaṃ": "các cặp câu hỏi về các tạo tác",
}

T602 = {**HEAD602}


def moment602(kw, text):
    """A bare moment keyword (uppādakkhaṇe / bhaṅgakkhaṇe; the citta is a keyword of its own) = «khoảnh khắc sinh
    khởi» / «khoảnh khắc tan rã» (map_8_vi.moment_value; 5-02). None if not one."""
    if " " in kw:
        return None
    return X.C.moment_value(kw, text)


def value602(kw, kws, vi, pi, table=None):
    """T602 (+ your table) -> parinna_value -> the bare moments -> map_6-01_vi.value601."""
    k = lc(kw).lower()
    tab = {**T602, **(table or {})}
    if kw in tab:
        return tab[kw]
    if k in tab:
        return tab[k]
    v = P.parinna_value(kw, pi)
    if v is not None:
        return v
    v = moment602(kw, vi)
    if v is not None:
        return v
    return X.value601(kw, kws, vi, pi)


# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver_for(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value602(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(part=PART, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
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
                except KeyError:
                    v = "???"
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
