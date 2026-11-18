"""Review fixes (findings r1-r4, triage 2026-11-18) for the pi-1 Vietnamese plain RAILS translation.

Applies fixed old -> new rules (a few regex rules, rx=True; a callable `new` is allowed for regex rules) to the 14
chapter files in AI_translation/vietnamese/pi-1-vietnamese-plain-rails_split_chapters/. A rule touches a Vietnamese
line ONLY when the aligned Pāli line (non-empty line i <-> non-empty line i, same file) matches the rule's Pāli
pattern; it applies in every chapter where that Pāli recurs. Line counts, block IDs, heading levels, dash counts,
variant brackets and ellipsis counts are asserted unchanged per changed line.

Backup of the pre-fix files: backup-pre-review/ (made once, never overwritten). The script always reads from the
backup, so rerunning rebuilds the same output.
Log: review-fixes-log.tsv (rule, file, segment, line, old, new).
After the pass: residual check per rule (old wording left on a line whose Pāli matches) and an identical-Pāli check
(groups of identical Pāli lines whose Vietnamese differs: before vs after).

usage: python -I -X utf8 review_fixes_vi.py [--dry]
"""
import collections
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_fixes_probe_lib import PDIR, VDIR, HERE, BAK, PARTS, ID

R = []  # (id, pali_regex, old, new, rx)


def rule(rid, pali, old, new, rx=False):
    R.append((rid, pali, old, new, rx))


# ============================================================ r1 (preamble, 1-matika, 2-01, 2-02)
# r1#1 negation scope: «không có gốc rễ cần dứt bỏ …» -> «không có gốc rễ nào cần dứt bỏ …» (matrix names and all
# reuses: ch3 rūpa lists, ch4 / ch5 question and answer frames, «đôi khi không có …»).
rule("r1#1-hetuka-scope", r"pahātabbahetuk", "không có gốc rễ cần dứt bỏ", "không có gốc rễ nào cần dứt bỏ")
rule("r1#1-hetuka-scope", r"neva dassanena na bhāvanāya pahātabbahetuk",
     "bằng sự thấy chân lý cũng không có gốc rễ nào", "bằng sự thấy chân lý, cũng không có gốc rễ nào")

# r1#2 / r4#4 yathādiṭṭhissa ca padhānaṃ (anurūpadiṭṭhi): one string book-wide.
rule("r1#2-yathaditthi", r"[Yy]athādiṭṭhissa", "của người làm theo quan điểm của mình",
     "của người có quan điểm tương xứng như thế")

# r1#3 third-jhāna formula: yaṃ refers to the jhāna, not to the bodily happiness. Dash kept in place.
rule("r1#3-ariya-acikkhanti", r"ariyā ācikkhanti", "điều mà các bậc thánh mô tả –",
     "là trạng thái mà nhờ đó các bậc thánh mô tả người ấy –")  # ācikkhanti keeps termbase «mô tả»

# r1#4 (ASK, approved) rūpañca «phần vật chất»: matrix pair ^1-M2-109 and its reuse ^1-1317.
rule("r1#4-rupanca-matrix", r"^\(Kha\) rūpañca\.", "(b) Vật chất.", "(b) Phần vật chất.")
rule("r1#4-rupanca-1317", r"^Tattha katamaṃ rūpaṃ\? Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ – "
     r"idaṃ vuccati rūpaṃ\.", "Ở đây, vật chất là gì?", "Ở đây, phần vật chất là gì?")
rule("r1#4-rupanca-1317", r"^Tattha katamaṃ rūpaṃ\? Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ – "
     r"idaṃ vuccati rūpaṃ\.", "– đó được gọi là vật chất.", "– đó được gọi là phần vật chất.")

# ============================================================ r2 (2-03, 2-04, 2-05)
# r2#1 heading ^1-1-7-0 (pattern of ^1-1-9-0).
rule("r2#1-heading", r"^#### Abyākatavipāko", "Quả của nghiệp không xác định về mặt đạo đức",
     "Loại không xác định về mặt đạo đức là quả của nghiệp")
# r2#2 ^1-565 line 2.
rule("r2#2-vipaka-abyakata", r"^Vipākā abyākatā\.", "Quả của nghiệp không xác định về mặt đạo đức.",
     "Các quả của nghiệp, thuộc loại không xác định về mặt đạo đức.")
# r2#3 Tasseva … katattā upacitattā / bhāvitattā vipākaṃ …: person as subject, result attached to the jhāna.
rule("r2#3-tasseva", r"[Tt]asseva \w+ kusalassa (kammassa|jhānassa) katattā",
     r"\. Là quả của chính (.+?) ấy đã được tạo và (tích lũy|tu tập), khi một người (.+?), thì vào lúc ấy",
     r". Còn khi một người \3, là quả của chính \1 ấy đã được tạo và \2, thì vào lúc ấy", rx=True)
# r2#4 ^1-555 aññātāvīnaṃ agrees with dhammānaṃ.
rule("r2#4-annatavinam", r"tesaṃ aññātāvīnaṃ dhammānaṃ",
     "Điều mà ở những hiện tượng ấy của người đã hiểu biết trọn vẹn là sự hiểu biết trọn vẹn,",
     "Điều mà ở những hiện tượng đã hiểu biết trọn vẹn ấy là sự hiểu biết trọn vẹn,")
# r2#5 (ASK, approved) asuropo «sự nói năng cộc cằn». anasuropo (^1-1348) keeps its own locked termbase term
# «sự không thô lỗ» (the user decision names asuropo only).
rule("r2#5-asuropo", r"(?<!an)asuropo", "sự thô lỗ", "sự nói năng cộc cằn")

# ============================================================ r3 (3-01, 3-02, 3-03)
# r3#1 ^1-584 uppannaṃ chahi viññāṇehi viññeyyaṃ is one property (as ^1-594).
rule("r3#1-uppannam-viññeyyam", r"uppannaṃ, chahi viññāṇehi viññeyyaṃ",
     "; đã sinh khởi; có thể được sáu loại thức nhận biết;",
     "; khi đã sinh khởi thì có thể được sáu loại thức nhận biết;")
# r3#2 ^1-590 eight-fold group: colon as in ^1-592.
rule("r3#2-atthaka", r"kāyaviññeyyaṃ rūpaṃ, atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ, manodhātuviññeyyaṃ",
     "vật chất mà thân có thể nhận biết, có loại khi tiếp xúc thì dễ chịu, có loại khi tiếp xúc thì khó chịu, "
     "vật chất mà yếu tố ý",
     "vật chất mà thân có thể nhận biết: có loại khi tiếp xúc thì dễ chịu, có loại khi tiếp xúc thì khó chịu; "
     "vật chất mà yếu tố ý")
# r3#3 drop «Điều mà là» in the chapter-3 definitions (16 lines).
for v_old, v_new in [("Điều mà là không gian, ", "Không gian, "), ("Điều mà là nước, ", "Nước, "),
                     ("Điều mà là lửa, ", "Lửa, "), ("Điều mà là gió, ", "Gió, "),
                     ("Điều mà là cái cứng, ", "Cái cứng, ")]:
    rule("r3#3-dieu-ma-la", r"(Yo|Yaṃ) (ākāso ākāsagataṃ|āpo āpogataṃ|tejo tejogataṃ|vāyo vāyogataṃ|kakkhaḷaṃ)",
         v_old, v_new)
rule("r3#3-dieu-ma-la", r"Yo āyatanānaṃ ācayo, so rūpassa upacayo",
     "Điều mà là sự tích lũy của các lĩnh vực nhận biết thì đó là sự tăng trưởng của vật chất",
     "Sự tích lũy của các lĩnh vực nhận biết, đó là sự tăng trưởng của vật chất")
rule("r3#3-dieu-ma-la", r"Yo rūpassa upacayo, sā rūpassa santati",
     "Điều mà là sự tăng trưởng của vật chất thì đó là sự liên tục của vật chất",
     "Sự tăng trưởng của vật chất, đó là sự liên tục của vật chất")
# r3#4 items first, cause after (no «sinh ra» added).
for items in ["lĩnh vực vật xúc chạm, yếu tố nước", "lĩnh vực hình sắc"]:
    rule("r3#4-kammassa-katatta", r"\? Kammassa katattā", f"? Do nghiệp đã được tạo: {items} –",
         f"? {items[0].upper() + items[1:]} do nghiệp đã được tạo –")
    rule("r3#4-kammassa-katatta", r"\? Na kammassa katattā", f"? Không do nghiệp đã được tạo: {items} –",
         f"? {items[0].upper() + items[1:]} không do nghiệp đã được tạo –")
# r3#5 ādāsamaṇḍalassa «mặt gương».
rule("r3#5-mat-guong", r"ādāsamaṇḍalassa", "vầng gương", "mặt gương")
# r3#6 (ASK, approved) vaṇṇanibhā «ánh màu».
rule("r3#6-vannanibha", r"vaṇṇanibhā", "màu sắc và dáng vẻ", "ánh màu")

# ============================================================ r4 (chapters 4 and 5)
# r4#1 the fourfold and fivefold schemes count the same jhānas: «hoặc», not «và».
rule("r4#1-naya-hoac", r"jjhān",
     r"theo phương pháp chia bốn và ((?:một|hai|ba|bốn|năm) tầng thiền theo phương pháp chia năm)",
     r"theo phương pháp chia bốn, hoặc \1", rx=True)
# r4#2 kenaci viññeyyā, kenaci na viññeyyā: matrix wording.
rule("r4#2-kenaci", r"Katame dhammā kenaci viññeyyā, kenaci na viññeyyā\?",
     "Những hiện tượng nào có thể được một loại thức nào đó nhận biết, không thể được một loại thức nào đó nhận biết?",
     "Những hiện tượng nào mà một loại thức nào đó có thể nhận biết, còn một loại thức nào đó không thể nhận biết?")
rule("r4#2-kenaci", r"Ime dhammā kenaci viññeyyā kenaci na viññeyyā",
     "Những hiện tượng này có thể được một loại thức nào đó nhận biết, không thể được một loại thức nào đó nhận biết.",
     "Những hiện tượng này là những hiện tượng mà một loại thức nào đó có thể nhận biết, còn một loại thức nào đó "
     "không thể nhận biết.")
rule("r4#2-kenaci", r"Sabbe .*dhammā kenaci viññeyyā, kenaci na viññeyyā",
     "đều có thể được một loại thức nào đó nhận biết, không thể được một loại thức nào đó nhận biết.",
     "đều là những hiện tượng mà một loại thức nào đó có thể nhận biết, còn một loại thức nào đó không thể nhận biết.")


# r4#3 ṭhapetvā X; taṃsampayutto: «chúng» -> the one excluded factor (plural exclusions keep «chúng»).
def _tam(m):
    x = m.group(1)
    if x.startswith("các "):
        return m.group(0)
    ref = "cảm giác ấy" if x.startswith("cảm giác") else x + " ấy"
    return f"ngoại trừ {x}{m.group(2)} {m.group(3)} gắn liền với {ref} –"


rule("r4#3-tam-sampayutto", r"ṭhapetvā[;,] taṃsampayutto",
     r"ngoại trừ ([^;,–]+?)([;,]) (khối [^;–]*?) gắn liền với chúng –", _tam, rx=True)

# r4#5 ^1-1051 ajjhattaṃ of the other beings.
rule("r4#5-parasatta", r"parasattānaṃ parapuggalānaṃ ajjhattaṃ", "ở nơi bản thân, riêng từng người",
     "ở nơi bản thân của họ, riêng từng người")
# r4#6 ^1-1350 recast with «một người» as subject.
rule("r4#6-sakhalya", r"tathārūpiṃ vācaṃ pahāya", "Từ bỏ lời nói thô cộc,", "Một người từ bỏ lời nói thô cộc,")
rule("r4#6-sakhalya", r"tathārūpiṃ vācaṃ pahāya", ", người ấy nói lời không có lỗi,", ", và nói lời không có lỗi,")
# r4#7 rūpāvacarā, arūpāvacarā (mahaggatā): «hoặc» as in ^1-1027.
rule("r4#7-mahaggata", r"Rūpāvacarā, arūpāvacarā, kusalābyākatā",
     "thuộc cõi hình sắc và thuộc cõi không hình sắc", "thuộc cõi hình sắc hoặc thuộc cõi không hình sắc")


# r4#8 «A, đối với B, vừa là N vừa V N» -> «A vừa là N vừa V B» (B is itself an N) or «… vừa V N là B».
def _doivoi(m):
    b, n, v = m.group(1), m.group(2), m.group(3)
    tail = b if n in b else f"{n} là {b}"
    return f" vừa là {n} vừa {v} {tail}"


rule("r4#8-doi-voi", r"ceva",
     r", đối với ([^,;?:–]+?), vừa là ([^;,–]+?) vừa (có|gắn liền với) \2(?=[;.]| –)", _doivoi, rx=True)
# r4#9 fragment «Ở nơi … cùng sinh khởi –»: give the clause a subject.
rule("r4#9-yattha", r"Yattha dve (tayo|tīṇi) \w+ ekato uppajjanti",
     r"Ở nơi hai hoặc ba (gốc rễ|ô nhiễm|xiềng xích|chướng ngại|phiền não) cùng sinh khởi –",
     r"Những \1 cùng sinh khởi theo nhóm hai hoặc ba –", rx=True)
rule("r4#9-yattha", r"Yattha diṭṭhi ca lobho ca ekato uppajjanti",
     "Ở nơi quan điểm và sự tham lam cùng sinh khởi –", "Quan điểm và sự tham lam khi cùng sinh khởi –")
# r4#10 (ASK, approved) cittahetukaṃ «có tâm làm nguyên nhân».
rule("r4#10-cittahetuka", r"cittahetuk", "có tâm làm gốc rễ", "có tâm làm nguyên nhân")


# ------------------------------------------------------------------------------------------------- engine
def dashes(t):
    return t.count("—") + t.count("–")


def ensure_backup():
    if os.path.isdir(BAK) and all(os.path.exists(os.path.join(BAK, p + ".md")) for p in PARTS):
        return False
    os.makedirs(BAK, exist_ok=True)
    for p in PARTS:
        dst = os.path.join(BAK, p + ".md")
        if not os.path.exists(dst):
            shutil.copyfile(os.path.join(VDIR, p + ".md"), dst)
    return True


def load(part, d):
    raw = open(os.path.join(d, part + ".md"), "rb").read()
    text = raw.decode("utf-8")
    assert "\r" not in text, part
    return text


def norm(s):
    s = re.sub(r"\s*\^[\w-]+\s*$", "", s)
    return re.sub(r"\s+", " ", s).strip()


def divergences(texts):
    """identical Pāli (block ID stripped) -> set of Vietnamese renderings; return groups with >1 rendering"""
    grp = collections.defaultdict(set)
    where = collections.defaultdict(list)
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        vl = [l for l in texts[part].lstrip("﻿").splitlines() if l.strip()]
        for k, (p, v) in enumerate(zip(pl, vl)):
            key = norm(p)
            if len(key) < 12:
                continue
            grp[key].add(norm(v))
            where[key].append(f"{part[:4]}:L{k + 1}")
    return {k: (v, where[k]) for k, v in grp.items() if len(v) > 1}


def main(dry=False):
    if ensure_backup():
        print("backup written:", BAK)
    comp = [(rid, re.compile(p), old, new, rx) for rid, p, old, new, rx in R]
    log, tot, changed, hit = [], collections.Counter(), collections.Counter(), set()
    files_of = collections.defaultdict(set)
    before, after = {}, {}
    residual = collections.Counter()
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        text = load(part, BAK)
        before[part] = text
        el = text.split("\n")
        idx = [i for i, l in enumerate(el) if l.strip()]
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        sid_of, cur = {}, []
        for k in range(len(pl)):
            cur.append(k)
            m = ID.search(pl[k])
            if m:
                for kk in cur:
                    sid_of[kk] = m.group(1)
                cur = []
        for k, li in enumerate(idx):
            p, e0 = pl[k], el[li]
            e = e0
            for ri, (rid, pr, old, new, rx) in enumerate(comp):
                if not pr.search(p):
                    continue
                if rx:
                    e2, n = re.subn(old, new, e)
                    if e2 == e:
                        n = 0
                else:
                    n = e.count(old)
                    e2 = e.replace(old, new)
                if n:
                    hit.add(ri)
                    log.append((rid, part, sid_of.get(k, "?"), k + 1, e, e2))
                    tot[rid] += n
                    files_of[rid].add(part)
                    e = e2
            for ri, (rid, pr, old, new, rx) in enumerate(comp):
                if pr.search(p):
                    if rx:
                        if callable(new):
                            left = [m for m in re.finditer(old, e) if new(m) != m.group(0)]
                            residual[rid] += len(left)
                        else:
                            residual[rid] += len(re.findall(old, e))
                    else:
                        residual[rid] += e.count(old)
            if e != e0:
                assert dashes(e) == dashes(e0), (part, k, "dash count changed", e)
                assert ID.findall(e) == ID.findall(e0), (part, k, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k, "heading")
                assert re.findall(r"\[[^\]]*\]", e) == re.findall(r"\[[^\]]*\]", e0), (part, k, "brackets")
                assert e.count("…") == e0.count("…"), (part, k, "ellipsis count")
                assert "—" not in e and ":-" not in e, (part, k)
                assert not re.search(r"\blà là\b", e), (part, k, "doubled là")
                assert e.strip(), (part, k)
                el[li] = e
                changed[part] += 1
        out = "\n".join(el)
        assert out.count("\n") == text.count("\n"), part
        after[part] = out
        if not dry:
            open(os.path.join(VDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(out)
    if not dry:
        with open(os.path.join(HERE, "review-fixes-log.tsv"), "w", encoding="utf-8", newline="\n") as f:
            f.write("rule\tfile\tsegment\tline\told\tnew\n")
            for rid, part, sid, ln, old, new in log:
                f.write(f"{rid}\t{part}\t^{sid}\t{ln}\t{old}\t{new}\n")
    print("replacements per rule (files):")
    for rid in dict.fromkeys(r[0] for r in R):
        print(f"  {rid:24s} {tot[rid]:4d}  lines={sum(1 for x in log if x[0] == rid):4d}  "
              f"files={','.join(sorted(p[:4] for p in files_of[rid]))}  residual={residual[rid]}")
    print("lines changed per file:", {p[:4]: n for p, n in changed.items()}, "total", sum(changed.values()),
          "(dry run)" if dry else "")
    for ri, r in enumerate(R):
        if ri not in hit:
            print("NO HIT:", r[0], "|", str(r[2])[:90])
    db, da = divergences(before), divergences(after)
    new = {k: v for k, v in da.items() if k not in db}
    print(f"identical-Pāli groups with differing Vietnamese: before {len(db)}, after {len(da)}, new {len(new)}")
    for k, (vs, wh) in list(new.items())[:20]:
        print("  NEW DIVERGENCE:", wh[:6], "|", k[:120])
        for v in vs:
            print("     V:", v[:160])


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
