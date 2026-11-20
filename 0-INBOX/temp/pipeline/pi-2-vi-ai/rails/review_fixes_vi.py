"""Review fixes (findings r1-r7, user decisions 2026-11-20) for the pi-2 Vietnamese plain RAILS translation.

Applies fixed old -> new rules to the 19 chapter files in
AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters/. A rule touches a Vietnamese line ONLY when the
aligned Pāli line (non-empty line i <-> non-empty line i, same file) matches the rule's Pāli pattern, and (if given)
only inside the listed segment IDs. Every rule carries the exact number of replacements it must make; the run aborts
when a count differs, so nothing is silently skipped or over-applied.
Kinds: plain string (default), regex (rx=True), whole-line (line_rule: the Vietnamese body of the line is replaced,
the block ID kept; used for the pi-1 verbatim copies, built from the pi-1 file at run time).
Per changed line the engine asserts: dash count, block IDs, heading level, variant brackets (unless the rule is
marked brackets=True), ellipsis count unchanged; no «—», «:-», doubled «là là».

Backup of the pre-fix files: backup-pre-review/ (made once, never overwritten). The script always reads from the
backup, so rerunning rebuilds the same output.
Log: review-fixes-log.tsv (rule, file, segment, line, old, new). Notes and builder constants: review-fixes-notes.md.
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
from review_fixes_lib import PDIR, VDIR, HERE, BAK, PARTS, P1_VDIR, P1_PARTS, ID, nonempty

R = []  # dicts: rid, pali, old, new, n, ids, parts, rx, line, brackets


def rule(rid, pali, old, new, n, ids=None, parts=None, rx=False, brackets=False):
    """old -> new on Vietnamese lines whose Pāli matches `pali` (and segment in `ids`, file prefix in `parts`);
    `n` = exact total number of replacements expected over all 19 files."""
    R.append(dict(rid=rid, pali=pali, old=old, new=new, n=n, ids=set(ids) if ids else None,
                  parts=parts, rx=rx, line=False, brackets=brackets))


def line_rule(rid, pali, new_body, must, n=1, ids=None):
    """replace the whole Vietnamese body (block ID kept) of lines whose Pāli matches; `must` = a substring the old
    line has to contain (sanity check)."""
    R.append(dict(rid=rid, pali=pali, old=must, new=new_body, n=n, ids=set(ids) if ids else None,
                  parts=None, rx=False, line=True, brackets=False))


def p1(block_id):
    """pi-1 Vietnamese body (block ID stripped) of the line that ends with ^block_id"""
    for part in P1_PARTS:
        for l in nonempty(os.path.join(P1_VDIR, part + ".md")):
            m = ID.search(l)
            if m and m.group(1) == block_id:
                return ID.sub("", l).rstrip()
    raise KeyError(block_id)


def must_replace(s, old, new):
    assert s.count(old) == 1, (old, s.count(old))
    return s.replace(old, new)


# Decision 1 (scope pattern, all chapters): a predicate without its own count that follows a sentence about a
# subset is restated with the whole set, always as «Cả <N> <X> đều …» (also before «đôi khi …»); after «Không nên
# nói» as «Về cả <N> <X> thì không nên nói …». Line counts unchanged; «;» before a restated clause becomes «.».
SET = {  # chapter number -> whole set
    "1": "Cả năm khối", "2": "Cả mười hai lĩnh vực", "3": "Cả mười tám yếu tố", "4": "Cả bốn sự thật",
    "5": "Cả hai mươi hai năng lực", "9": "Cả bốn nền tảng thần thông", "10": "Cả bảy chi phần giác ngộ",
    "11": "Cả tám chi phần của con đường", "12": "Cả bốn tầng thiền",
    "13": "Cả bốn trạng thái không thể đo lường", "15": "Cả bốn loại hiểu biết thông suốt",
}


def scope(sid, ch, old, new, n=1):
    """subjectless predicate after a subset -> whole set; «{S}» in new = SET[ch], «{s}» = the same, lower-case"""
    s = SET[ch]
    rule("D1-scope", r".", old, new.replace("{S}", s).replace("{s}", s[0].lower() + s[1:]), n, ids=[sid],
         parts=[ch])


# ============================================================ decision 1: scope pattern
# r1 ^2-152 / ^2-153 (aṭṭhakathā on ^2-150: no count = all five aggregates)
scope("2-152", "1", "”; đôi khi đã sinh khởi, đôi khi chưa sinh khởi",
      "”. {S} đều đôi khi đã sinh khởi, đôi khi chưa sinh khởi")
scope("2-152", "1", "”; đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân",
      "”. {S} đều đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân")
scope("2-153", "1", "Đều có điều kiện, đều do điều kiện tạo thành.",
      "{S} đều có điều kiện, đều do điều kiện tạo thành.")
scope("2-153", "1", "; chúng là những khối mà", ". {S} đều là những khối mà")
# r2 ^2-170 / 171 / 187 / 188 / 218 / 223 / 224 (aṭṭhakathā ^2-150, ^2-168)
scope("2-170", "2", "”; đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân",
      "”. {S} đều đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân")
scope("2-171", "2", "; chúng là những lĩnh vực mà", ". {S} đều là những lĩnh vực mà")
scope("2-187", "3", "”; đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân",
      "”. {S} đều đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân")
scope("2-188", "3", "; chúng là những yếu tố mà", ". {S} đều là những yếu tố mà")
scope("2-218", "4", "; chúng là những sự thật mà", ". {S} đều là những sự thật mà")
scope("2-223", "5", "đôi khi sẽ sinh khởi; đôi khi thuộc quá khứ", "đôi khi sẽ sinh khởi. {S} đều đôi khi thuộc quá khứ")
scope("2-223", "5", "”; đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân",
      "”. {S} đều đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân")
scope("2-224", "5", "; chúng là những năng lực mà", ". {S} đều là những năng lực mà")
scope("2-224", "5", "Đều có điều kiện. Đều do", "{S} đều có điều kiện. Đều do")
for x in ["xiềng xích.", "nút thắt.", "dòng lũ…", "sự hiểu sai lệch.", "sự bám víu.", "phiền não."]:
    scope("2-224", "5", "Đều không phải là " + x, "{S} đều không phải là " + x)
# ch9-ch13 question sections (r4 ^2-484, ^2-506, ^2-640, ^2-641, ^2-701, ^2-702 and the same pattern beside them)
scope("2-465", "9", "Đều có gốc rễ. Đều gắn liền với gốc rễ.", "{S} đều có gốc rễ. Đều gắn liền với gốc rễ.")
scope("2-465", "9", "”. Đều có điều kiện.", "”. {S} đều có điều kiện.")
scope("2-465", "9", "Đều không phải là phái sinh.", "{S} đều không phải là phái sinh.")
for sid, ch in [("2-484", "10"), ("2-506", "11")]:
    scope(sid, ch, "Đôi khi là quả của nghiệp, đôi khi có khả năng sinh ra quả.",
          "{S} đều đôi khi là quả của nghiệp, đôi khi có khả năng sinh ra quả.")
    scope(sid, ch, "Đều không cần dứt bỏ bằng sự thấy chân lý cũng", "{S} đều không cần dứt bỏ bằng sự thấy chân lý cũng")
scope("2-485", "10", "”. Đều có điều kiện.", "”. {S} đều có điều kiện.")
scope("2-485", "10", "Đều không thuộc cõi dục lạc.", "{S} đều không thuộc cõi dục lạc.")
scope("2-507", "11", "Đều có gốc rễ. Đều gắn liền với gốc rễ.", "{S} đều có gốc rễ. Đều gắn liền với gốc rễ.")
scope("2-507", "11", "Đều có điều kiện. Đều do", "{S} đều có điều kiện. Đều do")
scope("2-507", "11", "Đều không thuộc cõi dục lạc.", "{S} đều không thuộc cõi dục lạc.")
scope("2-640", "12", "Đôi khi là quả của nghiệp, đôi khi có khả năng sinh ra quả, đôi khi không phải",
      "{S} đều đôi khi là quả của nghiệp, đôi khi có khả năng sinh ra quả, đôi khi không phải")
scope("2-640", "12", "Đều không cần dứt bỏ bằng sự thấy chân lý cũng", "{S} đều không cần dứt bỏ bằng sự thấy chân lý cũng")
scope("2-640", "12", "Đôi khi trung bình, đôi khi ưu việt.", "{S} đều đôi khi trung bình, đôi khi ưu việt.")
scope("2-640", "12", "Đôi khi đã sinh khởi, đôi khi chưa sinh khởi", "{S} đều đôi khi đã sinh khởi, đôi khi chưa sinh khởi")
scope("2-640", "12", "Đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân",
      "{S} đều đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân")
scope("2-640", "12", "Đều không thấy được và không có tính va chạm.",
      "{S} đều không thấy được và không có tính va chạm.")
scope("2-641", "12", "có sự bình thản đi kèm; Đều không thuộc cõi dục lạc",
      "có sự bình thản đi kèm. {S} đều không thuộc cõi dục lạc")
scope("2-641", "12", "đôi khi không thuộc cõi không hình sắc; đôi khi nằm trong",
      "đôi khi không thuộc cõi không hình sắc. {S} đều đôi khi nằm trong")
scope("2-641", "12", "đôi khi không có điều gì cao hơn; Đều không có xung đột.",
      "đôi khi không có điều gì cao hơn. Đều không có xung đột.")
scope("2-701", "13", "Đôi khi là quả của nghiệp, đôi khi có khả năng sinh ra quả, đôi khi không phải",
      "{S} đều đôi khi là quả của nghiệp, đôi khi có khả năng sinh ra quả, đôi khi không phải")
scope("2-701", "13", "Đều không cần dứt bỏ bằng sự thấy chân lý cũng", "{S} đều không cần dứt bỏ bằng sự thấy chân lý cũng")
scope("2-702", "13", "thì không phải là gốc rễ, có gốc rễ, gắn liền với gốc rễ.",
      "thì không phải là gốc rễ. {S} đều có gốc rễ, đều gắn liền với gốc rễ.")
scope("2-702", "13", "Đều có điều kiện, do điều kiện tạo thành, không thấy được",
      "{S} đều có điều kiện, do điều kiện tạo thành, không thấy được")
scope("2-702", "13", "; đều không thuộc cõi dục lạc", ". {S} đều không thuộc cõi dục lạc")
# r5 A1 ch15 ^2-749 (lines 2, 6), ^2-750
scope("2-749", "15", "Đôi khi có sự hân hoan đi kèm, đôi khi có hạnh phúc đi kèm",
      "{S} đều đôi khi có sự hân hoan đi kèm, đôi khi có hạnh phúc đi kèm")
scope("2-749", "15", "Đôi khi thuộc quá khứ, đôi khi thuộc tương lai", "{S} đều đôi khi thuộc quá khứ, đôi khi thuộc tương lai")
scope("2-749", "15", "Đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân",
      "{S} đều đôi khi ở nơi bản thân, đôi khi ở bên ngoài bản thân")
scope("2-749", "15", "Đều không thấy được và không có tính va chạm.",
      "{S} đều không thấy được và không có tính va chạm.")
scope("2-750", "15", "; đều là những loại hiểu biết thông suốt mà", ". {S} đều là những loại hiểu biết thông suốt mà")
scope("2-750", "15", "Đều không gắn liền với ô nhiễm.", "{S} đều không gắn liền với ô nhiễm.")
scope("2-750", "15", "”. Không nên nói rằng “vừa là ô nhiễm vừa gắn liền",
      "”. Về {s} thì không nên nói rằng “vừa là ô nhiễm vừa gắn liền")
scope("2-750", "15", "Đều không phải là xiềng xích…", "{S} đều không phải là xiềng xích…")
scope("2-750", "15", "Đôi khi có sự hân hoan, đôi khi không có sự hân hoan.",
      "{S} đều đôi khi có sự hân hoan, đôi khi không có sự hân hoan.")
scope("2-750", "15", "Đều không thuộc cõi hình sắc.", "{S} đều không thuộc cõi hình sắc.")
scope("2-750", "15", "Đều không có xung đột.", "{S} đều không có xung đột.")
# r5 A2 ^2-749 lines 4-6: tisso = the three other than nirutti, dve = dhamma and paṭibhāna
rule("D1-con-lai", r".", "; ba loại hiểu biết thông suốt thì", "; ba loại hiểu biết thông suốt còn lại thì", 2,
     ids=["2-749"])
rule("D1-con-lai", r".", "; hai loại hiểu biết thông suốt thì", "; hai loại hiểu biết thông suốt còn lại thì", 2,
     ids=["2-749"])

# ============================================================ r1 (preamble, ch1)
# decision 11: asamāpannassa / samāpannassa (^2-11 … ^2-31): the object (the meditative attainment) named.
rule("r1-samapanna", r"[Aa]samāpannassa", "của người chưa chứng nhập", "của người không ở trong thành tựu thiền", 24,
     parts=["1"])
rule("r1-samapanna", r"[Aa]samāpannassa", "của người đã chứng nhập", "của người đang ở trong thành tựu thiền", 24,
     parts=["1"])

# ============================================================ r2 (ch2-ch5)
# ^2-176 aṭṭhakathā: uppalakavātā = winds that wrench the heart flesh; kāḷavātā = winds among black clouds
rule("r2-uppalakavata", r"uppalakavātā", "gió như kim châm", "gió như bứt tim", 1)
rule("r2-kalavata", r"kāḷavātā", "gió bão", "gió mây đen", 1)
# ^2-182 = pi-1 ^1-1287 (decision 8; r7 «bao gồm cả»): pi-1 wording, pi-2 variant bracket kept
rule("D8-kamadhatu", r"Heṭṭhato avīcinirayaṃ pariyantaṃ karitvā uparito paranimmitavasavattī deve anto karitvā",
     "Lấy địa ngục Vô Gián ở bên dưới làm giới hạn, tính cả chư thiên Tha Hóa Tự Tại ở bên trên vào bên trong, "
     "những gì ở trong khoảng giữa ấy, thuộc cõi này, nằm trong cõi này: các khối, yếu tố và lĩnh vực nhận biết, "
     "những gì thuộc vật chất [",
     "Lấy địa ngục Vô Gián ở bên dưới làm giới hạn, bao gồm cả chư thiên Tha Hóa Tự Tại ở bên trên, "
     "những điều trong khoảng giữa ấy thuộc cõi này, nằm trong cõi này: các khối, các yếu tố và các lĩnh vực nhận "
     "biết, tức vật chất [", 1)
# ^2-190 / ^2-199 appiyehi sampayogo (defined as saṅgati samāgamo …)
rule("r2-appiyehi", r"appiyehi sampayogo", "gắn bó với những gì mình không yêu quý",
     "gặp gỡ những gì mình không yêu quý", 3)
# ^2-193 / ^2-236 maccu maraṇaṃ is one item (decision 9; pi-1 has no maraṇa definition)
rule("D9-maccu-maranam", r"antaradhānaṃ maccu maraṇaṃ kālakiriyā", "sự tử vong, sự chết, sự qua đời",
     "sự tử vong, sự qua đời", 2)
# ^2-218 ajjhattaṃ / bāhiraṃ pair as in the rest of the line
rule("r2-ajjhattika", r"Tīṇi saccāni bāhirā\. Dukkhasaccaṃ siyā ajjhattaṃ, siyā bāh",
     "đôi khi ở nơi bản thân, đôi khi thuộc phần bên ngoài", "đôi khi thuộc phần bên trong, đôi khi thuộc phần bên ngoài",
     1, ids=["2-218"])
# ^2-223 one form with ^2-217 («nhưng không …»)
rule("r2-nhung-khong", r"siyā mahaggatārammaṇaṃ, na appamāṇārammaṇaṃ",
     "đôi khi có đối tượng rộng lớn, không có đối tượng không thể đo lường",
     "đôi khi có đối tượng rộng lớn nhưng không có đối tượng không thể đo lường", 1)

# ============================================================ r3 (ch6, ch7)
# samāgamo «sự hội tụ» (coming together); same word in ^2-199 / ^2-200 (decision 14)
rule("r3-samagamo", r"samāgamo hoti", "là sự gần gũi, là sự tụ hợp", "là sự hội tụ, là sự tụ hợp", 5)
rule("r3-samagamo", r"saṅgati samāgamo samodhānaṃ", "sự kết hợp, sự gần gũi, sự tụ hợp",
     "sự kết hợp, sự hội tụ, sự tụ hợp", 1)
rule("r3-samagamo", r"asaṅgati asamāgamo asamodhānaṃ", "sự không kết hợp, sự không gần gũi, sự không tụ hợp",
     "sự không kết hợp, sự không hội tụ, sự không tụ hợp", 1)
# decision 10: missing quotes after «đó được gọi là» (r3 list; the Pāli lacks them there)
for sid, txt, tail in [
        ("2-259", "sự tạo tác làm điều kiện cho thức có sự tạo tác làm nguyên nhân", "."),
        ("2-273", "sự tạo tác làm điều kiện cho thức", "."),
        ("2-279", "phần tinh thần", "."),
        ("2-281", "vô minh làm điều kiện cho sự tạo tác", "…"),
        ("2-283", "vô minh", "…"),
        ("2-327", "sự tạo tác", "."),
        ("2-354", "sự lão hóa", "."),
        ("2-368", "sự quán sát", "."),
        ("2-376", "sự thiết lập tỉnh thức", ".")]:
    rule("D10-quotes", r"vuccati [^\"]", f"– đó được gọi là {txt}{tail}", f"– đó được gọi là “{txt}”{tail}", 1,
         ids=[sid])

# ============================================================ r4 (ch8-ch13)
# ^2-640: the three jhānas with sukha include the two with pīti: no contrast «còn»
rule("r4-con", r".", "có sự hân hoan đi kèm; còn ba tầng thiền – ngoại trừ hạnh phúc",
     "có sự hân hoan đi kèm; ba tầng thiền – ngoại trừ hạnh phúc", 1, ids=["2-640"])
# ^2-701 MINOR: «đôi khi» ran on into the fixed predicates
rule("r4-701", r".", "cũng không dẫn đến sự giảm trừ, không thuộc về người còn đang tu học",
     "cũng không dẫn đến sự giảm trừ. Đều không thuộc về người còn đang tu học", 1, ids=["2-701"])
# ^2-645 … ^2-681 adhimuccitvā (aṭṭhakathā: adhikabhāvena muñcitvā … suppasāritaṃ suvitthataṃ)
rule("r4-adhimuccitva", r"pharitvā adhimuccitvā", "sau khi lan tỏa khắp, sau khi quyết định.",
     "sau khi lan tỏa khắp, sau khi trải rộng trọn vẹn.", 8)
# ^2-510 sekkho bhikkhu …
rule("r4-sekkho-bhikkhu", r"sekkho bhikkhu, asekkho bhikkhu, nevasekkhanāsekkho bhikkhu",
     "tỳ-khưu thuộc về người còn đang tu học, tỳ-khưu thuộc về người đã hoàn tất tu học, tỳ-khưu không thuộc về "
     "người còn đang tu học cũng không thuộc về người đã hoàn tất tu học",
     "tỳ-khưu còn đang tu học, tỳ-khưu đã hoàn tất tu học, tỳ-khưu không phải còn đang tu học cũng không phải đã "
     "hoàn tất tu học", 1)
# ^2-511 decision 7 (samāpattiyā = for obtaining, aṭṭhakathā paṭilābhatthāya)
rule("D7-samapattiya", r"kusalānaṃ dhammānaṃ samāpattiyā",
     "điều cao nhất, điều đứng đầu để các hiện tượng thiện xảy ra nơi mình.",
     "điều cao nhất, điều đứng đầu cho việc đạt được các hiện tượng thiện.", 1)
# ^2-537 mukhanimitte: the upper lip (aṭṭhakathā)
rule("r4-mukhanimitta", r"mukhanimitte", "nơi chóp mũi hoặc nơi vùng miệng", "nơi chóp mũi hoặc nơi môi trên", 1)
# ^2-508 appasaddaṃ … describes the lodging, not a tenth place
rule("r4-appasadda", r"palālapuñjaṃ appasaddaṃ", "đống rơm, nơi ít tiếng động,", "đống rơm; chỗ ở ấy ít tiếng động,",
     1)
# ^2-467 cittaṃ samādhiyati / samāhitaṃ cittaṃ (bojjhaṅga chain)
rule("r4-samadhiyati", r"cittaṃ samādhiyati – ayaṃ vuccati", "tâm được định tâm –", "tâm trở nên an định –", 1)
rule("r4-samadhiyati", r"So tathā samāhitaṃ cittaṃ sādhukaṃ ajjhupekkhitā", "nhìn tâm đã được định tâm như vậy",
     "nhìn tâm đã an định như vậy", 1)
# ^2-643 / 653 / 663 / 673 Kathañca: «Và» as ch8 / ch9 / ch12
rule("r4-kathanca", r"^Kathañca bhikkhu \w+sahagatena cetasā ekaṃ disaṃ",
     "Vị tỳ-khưu an trú sau khi lan tỏa khắp một phương", "Và vị tỳ-khưu an trú sau khi lan tỏa khắp một phương", 4)
# sabbena sabbaṃ sabbathā sabbaṃ: one wording (^2-648 … has both «sabbaṃ»)
rule("r4-sabbena-sabbam", r"sabbena sabbaṃ sabbathā sabbaṃ asesaṃ nissesaṃ samādāya",
     "một cách toàn bộ, về mọi mặt, không thiếu sót", "một cách toàn bộ, tất cả về mọi mặt, không thiếu sót", 1)
# ^2-619 saṅkhārāvasesasamāpatti
rule("r4-sankharavasesa", r"saṅkhārāvasesasamāpattiṃ", "tu tập thành tựu thiền còn sót lại các sự tạo tác",
     "tu tập thành tựu thiền trong đó các sự tạo tác chỉ còn sót lại", 1)

# decision 8: pi-1 drift. ^2-517 / ^2-518 / ^2-905 / ^2-U24 = pi-1 ^1-1352 … ^1-1355; pi-1 Vietnamese verbatim,
# keeping only the quote marks the pi-2 Pāli adds.
P1352 = must_replace(p1("1-1352"), "đó được gọi là sự không phòng hộ cửa các giác quan.",
                     "đó được gọi là “sự không phòng hộ cửa các giác quan”.")
P1353 = must_replace(p1("1-1353"), "đó được gọi là sự không biết tiết độ trong ăn uống.",
                     "đó được gọi là “sự không biết tiết độ trong ăn uống”.")
P1354 = must_replace(p1("1-1354"), "đó được gọi là sự phòng hộ cửa các giác quan.",
                     "đó được gọi là “sự phòng hộ cửa các giác quan”.")
# ^1-1355: the pi-2 Pāli quotes the whole reflection («neva davāya … phāsu vihāro cā"ti»), so the quote opens at
# «Không phải» and the pi-1 «, với ý nghĩ “Như vậy» (pi-1 quotes only the iti-clause) becomes «; như vậy».
P1355 = must_replace(must_replace(must_replace(p1("1-1355"), "đúng cách – không phải để vui đùa",
                                               "đúng cách – “Không phải để vui đùa"),
                                  ", với ý nghĩ “Như vậy, ta sẽ", "; như vậy, ta sẽ"),
                     "đó được gọi là sự biết tiết độ trong ăn uống.", "đó được gọi là “sự biết tiết độ trong ăn uống”.")
# ^2-U24 «Tattha katamo asaṃvaro?»: own question (as before), pi-1 body without the «Yā imesaṃ …» sentence
U24 = ("Ở đây, sự không thu thúc là gì? " + must_replace(P1352, "Ở đây, sự không phòng hộ cửa các giác quan là gì? ", "")
       .split(". Điều mà là sự không canh giữ")[0] + " – đó được gọi là “sự không thu thúc”.")
line_rule("D8-pi1-1352", r"^Tattha katamā indriyesu aguttadvāratā\?", P1352, "sự không phòng hộ cửa các giác quan",
          ids=["2-517"])
line_rule("D8-pi1-1352", r"^\(Ka\) tattha katamā indriyesu aguttadvāratā\?", "(a) " + P1352,
          "sự không phòng hộ cửa các giác quan", ids=["2-905"])
line_rule("D8-pi1-1352", r"^Tattha katamo asaṃvaro\? Idhekacco cakkhunā", U24, "sự không thu thúc", ids=["2-U24"])
line_rule("D8-pi1-1353", r"^Tattha katamā bhojane amattaññutā\?", P1353, "sự không biết tiết độ trong ăn uống",
          ids=["2-518"])
line_rule("D8-pi1-1353", r"^\(Kha\) tattha katamā bhojane amattaññutā\?", "(b) " + P1353,
          "sự không biết tiết độ trong ăn uống", ids=["2-905"])
line_rule("D8-pi1-1354", r"^Tattha katamā indriyesu guttadvāratā\?",
          P1354 + " Vị ấy có được, có được trọn vẹn… được trang bị sự phòng hộ cửa các giác quan này. Vì thế, điều "
                  "này được gọi là “phòng hộ cửa các giác quan”.", "Vị ấy có được, có được trọn vẹn…", ids=["2-517"])
line_rule("D8-pi1-1355", r"^Tattha katamā bhojane mattaññutā\?",
          P1355 + " Vị ấy có được… được trang bị sự biết tiết độ trong ăn uống này. Vì thế, điều này được gọi là "
                  "“biết tiết độ trong ăn uống”.", "Vị ấy có được… được trang bị sự biết tiết độ", ids=["2-518"])

# ============================================================ r5 (ch14-ch16)
# A17 surāmeraya: two kinds of liquor (also ch17 ^2-942)
rule("r5-surameraya", r"[Ss]urāmeraya", "rượu nấu rượu men", "rượu nấu, rượu men", 34)
# A11 dhammaniruttābhilāpe: the wording used to express the phenomena
rule("r5-abhilapa", r"dhammaniruttābhilāpe", "lời diễn tả cách diễn đạt các hiện tượng ở đó",
     "ngôn từ dùng để diễn đạt các hiện tượng ở đó", 29)
# A12 paññatti (aṭṭhakathā ^2-1496: naming)
rule("r5-pannatti", r"dhammānaṃ paññatti hoti", "khái niệm về những hiện tượng ấy", "sự gọi tên những hiện tượng ấy", 1)
rule("r5-pannatti", r"dhammānaṃ paññatti hoti", "Khái niệm về những hiện tượng ấy", "Sự gọi tên những hiện tượng ấy",
     20)
# decision 4: ñāṇavatthu = «loại hiểu biết» (aṭṭhakathā ^2-1511, ^2-1561 ñāṇagaṇanā)
rule("D4-nanavatthu", r"(?i)ñāṇavatth", "Như vậy là chỗ dựa của sự hiểu biết theo nhóm",
     "Như vậy là các loại hiểu biết theo nhóm", 19)
rule("D4-nanavatthu", r"(?i)ñāṇavatth", "Chỗ dựa của sự hiểu biết theo nhóm", "Các loại hiểu biết theo nhóm", 10)
rule("D4-nanavatthu", r"(?i)ñāṇavatth", "bảy mươi bảy chỗ dựa của sự hiểu biết", "bảy mươi bảy loại hiểu biết", 2)
rule("D4-nanavatthu", r"(?i)ñāṇavatth", "Bảy mươi bảy chỗ dựa của sự hiểu biết", "Bảy mươi bảy loại hiểu biết", 1)
# decision 4: dhamme ñāṇaṃ in the path-knowledge set = «sự hiểu biết về chân lý» (aṭṭhakathā ^2-1586)
rule("D4-dhamme-nanam", r"[Dd]hamme ñāṇaṃ|dhammena ñātena", "sự hiểu biết về Giáo Pháp", "sự hiểu biết về chân lý", 3)
rule("D4-dhamme-nanam", r"[Dd]hamme ñāṇaṃ", "Sự hiểu biết về Giáo Pháp", "Sự hiểu biết về chân lý", 1)
rule("D4-dhamme-nanam", r"dhammena ñātena", "Bằng Giáo Pháp này", "Bằng chân lý này", 1)
# decision 3: ^2-803 Dhammasamaṅgissa kept as written; the wrong «Giáo Pháp» goes
rule("D3-dhammasamangi", r"Dhammasamaṅgissa", "Sự hiểu biết của người có được Giáo Pháp",
     "Sự hiểu biết của người đang có các hiện tượng ấy", 1)
# A4 yāthāvakavatthuvibhāvanā (aṭṭhakathā ^2-1561: vatthu = the actual matter)
rule("r5-yathavaka", r"yāthāvakavatthu", "làm sáng tỏ chỗ dựa đúng như thật", "làm sáng tỏ sự việc đúng như thật", 2)
# A5 atthajāpikā / jāpitatthā (aṭṭhakathā ^2-1563: attha = result)
rule("r5-atthajapika", r"atthajāpik|jāpitatth", "tạo ra lợi ích", "tạo ra kết quả", 3)
rule("r5-atthajapika", r"atthajāpik|jāpitatth", "có lợi ích đã được tạo ra", "có kết quả đã được tạo ra", 2)
# A13 yogavihitesu (aṭṭhakathā ^2-1566: yogo = paññā)
rule("r5-yogavihita", r"yogavihit", "được tạo dựng bằng sự khéo léo", "được tạo dựng bằng trí tuệ", 6)
# A14 ^2-804 sasaṅkhāraniggayhavāritagato (aṭṭhakathā ^2-1599: effort)
rule("r5-sasankhara", r"na sasaṅkhāraniggayhavāritagato",
     "không phải đạt được nhờ sự kiềm chế và ngăn chặn có sự thúc đẩy",
     "không phải đạt được bằng cách gắng sức đè nén, ngăn chặn", 1)
# A15 ^2-805 sotadhātuvisuddhiyā ñāṇaṃ
rule("r5-sotadhatu", r"sotadhātuvisuddhiyā ñāṇaṃ", "sự hiểu biết về sự trong sạch của yếu tố tai",
     "sự hiểu biết của yếu tố tai đã được thanh lọc", 1)
# A9 ^2-809 upādāya (kept as written, «atthato» kept: decision 2)
rule("r5-upadaya", r"upādāya taṃ taṃ ṭhānaṃ", "thì tùy thuộc vào đó mà có điều có thể xảy ra tương ứng",
     "thì, xét theo đó, chính chúng là điều có thể xảy ra tương ứng", 1)
rule("r5-upadaya", r"upādāya taṃ taṃ ṭhānaṃ", "thì tùy thuộc vào đó mà có điều không thể xảy ra tương ứng",
     "thì, xét theo đó, chính chúng là điều không thể xảy ra tương ứng", 1)
# A10 sevanti bhajanti payirupāsanti (^2-813, ^2-818) and sevati bhajati payirupāsati (^2-514); none in pi-1
rule("r5-sevanti", r"payirupās", "gần gũi, lui tới, thường xuyên lui tới hầu cận", "gần gũi, kết giao, thân cận", 6)
rule("r5-sevanti", r"payirupās", "đã gần gũi, đã lui tới, đã thường xuyên lui tới hầu cận",
     "đã gần gũi, đã kết giao, đã thân cận", 4)
rule("r5-sevanti", r"payirupās", "sẽ gần gũi, sẽ lui tới, sẽ thường xuyên lui tới hầu cận",
     "sẽ gần gũi, sẽ kết giao, sẽ thân cận", 4)
# A19 ^2-828 comma
rule("r5-828", r"avitakkavicāramatto samādhi", "định tâm không có sự hướng tâm chỉ có sự duy trì tâm",
     "định tâm không có sự hướng tâm, chỉ có sự duy trì tâm", 1)
# A16 ^2-829 evaṃsukhadukkhappaṭisaṃvedī (feeling decision)
rule("r5-829", r"evaṃsukhadukkhappaṭisaṃvedī", "cảm nhận hạnh phúc và khổ đau như vậy",
     "cảm nhận dễ chịu và khó chịu như vậy", 2)
# decision 6: ^2-830 bhonto is nominative, agreeing with sattā
rule("D6-bhonto", r"ime vata bhonto sattā", "Quả thật, thưa các ngài, những chúng sinh này",
     "Quả thật, những chúng sinh đáng kính này", 1)
rule("D6-bhonto", r"Ime vā pana bhonto sattā", "Hoặc, thưa các ngài, những chúng sinh này",
     "Hoặc những chúng sinh đáng kính này", 1)

# ============================================================ r6 (ch17)
# decision 5: kamyatā = «sự mong muốn …», the negation on the act (wish for not-seeing)
rule("D5-kamyata", r"adassanakamyat", "ự không mong muốn thấy các bậc thánh", "ự mong muốn không thấy các bậc thánh", 4)
rule("D5-kamyata", r"adassanakamyatā adaṭṭhukamyatā",
     "sự không mong muốn thấy, sự không muốn nhìn, sự không mong muốn đến gần, sự không muốn cùng hội họp với",
     "sự mong muốn không thấy, sự mong muốn không nhìn, sự mong muốn không đến gần, sự mong muốn không hội họp với",
     1)
rule("D5-kamyata", r"asotukamyat", "ự không muốn nghe Giáo Pháp chân chính", "ự mong muốn không nghe Giáo Pháp chân chính",
     4)
rule("D5-kamyata", r"asotukamyatā asavanakamyatā",
     "sự không muốn nghe, sự không muốn lắng nghe, sự không muốn học hỏi, sự không muốn ghi nhớ",
     "sự mong muốn không nghe, sự mong muốn không lắng nghe, sự mong muốn không học hỏi, sự mong muốn không ghi nhớ",
     1)
rule("D5-catukamyata", r"anuppiyabhāṇitā cāṭukamyatā", "lời chiều lòng, lời nịnh bợ,",
     "lời chiều lòng, sự mong muốn nịnh bợ,", 1)
# ^2-844 bhogaṃ / vaṇṇaṃ as ^2-832 bhogamado / vaṇṇamado
rule("r6-bhoga-vanna", r"bhogaṃ paṭicca…pe… vaṇṇaṃ paṭicca", "dựa vào của cải… dựa vào sắc đẹp…",
     "dựa vào tài sản… dựa vào vẻ đẹp…", 1)
# ^2-854 the genitive (this body / outer requisites) governs all four nouns
rule("r6-cāpalya", r"imassa vā pūtikāyassa bāhirānaṃ vā parikkhārānaṃ maṇḍanā",
     "sự trang trí chỗ ở, sự trang trí, sự tô điểm, sự nâng niu, sự nâng niu quá mức thân hôi thối này hoặc các vật "
     "dụng bên ngoài, sự ham thích,",
     "sự trang trí chỗ ở; đối với thân hôi thối này hoặc các vật dụng bên ngoài thì có sự trang trí, sự tô điểm, sự "
     "nâng niu, sự nâng niu quá mức; sự ham thích,", 1)
# ^2-855 jeṭṭhe vā bhātari vā = the elder brother (one item)
rule("r6-jettha-bhatar", r"jeṭṭhe vā bhātari vā", "hoặc người lớn tuổi hơn, hoặc anh em,", "hoặc anh cả,", 1)
# ^2-904 appaṭisanthārako
rule("r6-patisanthara", r"appaṭisanthārako",
     "có người không niềm nở tiếp đón, với sự niềm nở tiếp đón bằng vật phẩm hoặc với sự niềm nở tiếp đón bằng Giáo Pháp",
     "có người không niềm nở tiếp đón bằng vật phẩm hoặc không niềm nở tiếp đón bằng Giáo Pháp", 1)
# ^2-U41 vipariyāsa: object and wrong notion first, then the three distortions
for i, (obj, notion) in enumerate([("vô thường", "thường còn"), ("khổ đau", "hạnh phúc"),
                                   ("không phải tự ngã", "tự ngã"), ("không đẹp", "đẹp")]):
    lead = "Sự" if i == 0 else "sự"
    rule("r6-vipariyasa", r"saññāvipariyāso cittavipariyāso diṭṭhivipariyāso",
         f"{lead} đảo ngược của tri giác, sự đảo ngược của tâm, sự đảo ngược của quan điểm rằng “{notion}” đối với "
         f"điều {obj}",
         f"{'Đối' if i == 0 else 'đối'} với điều {obj} mà cho là “{notion}”: sự đảo ngược của tri giác, sự đảo ngược "
         f"của tâm, sự đảo ngược của quan điểm", 1)
# ^2-939 itibhavābhavahetu (aṭṭhakathā: finer and finer requisites)
rule("r6-itibhavabhava", r"itibhavābhavahetu", "vì sự hiện hữu này hay sự hiện hữu khác mà",
     "vì những thứ tốt hơn rồi lại tốt hơn nữa mà", 1)
# ^2-947, ^2-U67, ^2-U68 gehasita at the end of the string (as ^2-U60)
for a, b in [("sự khoan khoái trong tâm, sự dễ chịu trong tâm", "khoan khoái và dễ chịu"),
             ("sự bứt rứt trong tâm, sự khó chịu trong tâm", "bứt rứt và khó chịu"),
             ("trạng thái trong tâm không khoan khoái cũng không bứt rứt", "không khó chịu cũng không dễ chịu")]:
    rule("r6-gehasita", r"gehasitaṃ cetasikaṃ",
         f"có {a} gắn với đời sống thế tục, cảm nhận {b} sinh từ sự tiếp xúc của tâm, cảm giác {b} sinh từ sự tiếp "
         f"xúc của tâm",
         f"có {a}, cảm nhận {b} sinh từ sự tiếp xúc của tâm, cảm giác {b} sinh từ sự tiếp xúc của tâm gắn với đời "
         f"sống thế tục", 2)
# ^2-949 bhavarāgānusayo as ^2-U69, ^2-U70, ^2-969, pi-1 ^1-1118
rule("r6-bhavaraga", r"bhavarāgānusay", "tham đắm sự hiện hữu", "tham đắm hiện hữu", 2)  # ^2-949 and ^2-816
# ^2-976 dangling «thuộc loại như vậy»
rule("r6-976", r"evarūpāni atītāni", "ba mươi sáu dòng khao khát thuộc quá khứ, thuộc loại như vậy,",
     "ba mươi sáu dòng khao khát như thế thuộc quá khứ,", 1)
# MINOR
rule("r6-papika", r"pāpikāya vā diṭṭhiyā", "quan điểm xấu xa", "quan điểm xấu ác", 1)
rule("r6-sampavanka", r" sampavaṅkatā – ayaṃ vuccati", "sự nghiêng về phía – đó", "sự nghiêng theo – đó", 1)
rule("r6-chambhitatta", r"bhayānakaṃ chambhitattaṃ", "trạng thái cứng đờ, sự dựng tóc gáy", "sự chết lặng, sự dựng tóc gáy",
     3)
# ^2-948 uppajjati: one form, the termbase «quan điểm … khởi lên» (the sixth occurrence followed «sinh khởi»)
rule("r6-948", r"saccato thetato diṭṭhi uppajjati", "hoặc quan điểm ấy sinh khởi nơi người ấy như là",
     "hoặc quan điểm ấy khởi lên nơi người ấy như là", 1)
rule("r6-953", r"gilānavuṭṭhito \(saddanībhi\)",
     "[khác chính tả (Saddanībhi): gilānavuṭṭhito; Tăng Chi Bộ Kinh 6.16, nên tham khảo chú giải phụ của đoạn này]",
     "[khác chính tả (Saddanībhi): gilānavuṭṭhito; nên xem chú giải phụ về kinh văn Tăng Chi Bộ Kinh 6.16]", 1,
     brackets=True)
rule("r6-apaham", r"apāhaṃ", "ước gì tôi cũng ", "ước gì tôi ", 42)
rule("r6-apaham", r"apāhaṃ", "Ước gì tôi cũng ", "Ước gì tôi ", 30)
rule("r6-U58", r"appiyo hoti amanāpo", "được nhiều người yêu quý, không đáng ưa thích,",
     "được nhiều người yêu quý, không được ưa thích,", 1)
rule("r6-U9", r"Sassatadiṭṭhi assādadiṭṭhi",
     "Quan điểm về sự trường tồn là quan điểm về sự thỏa thích, quan điểm về tự ngã là quan điểm xem có tự ngã, quan "
     "điểm về sự đoạn diệt là quan điểm sai lầm.",
     "Quan điểm về sự thỏa thích là quan điểm về sự trường tồn, quan điểm xem có tự ngã là quan điểm về tự ngã, quan "
     "điểm sai lầm là quan điểm về sự đoạn diệt.", 1)

# ============================================================ r7 (ch18)
rule("r7-1022", r"Vassasataṃ, appaṃ vā bhiyyo", "Một trăm năm, ít hơn hoặc nhiều hơn [",
     "Một trăm năm, hoặc nhiều hơn một chút [", 1)
rule("r7-1031", r".", "đôi khi không cần được tu tập, nhưng cần được tự mình chứng nghiệm.",
     "đôi khi không cần được tu tập, cần được tự mình chứng nghiệm.", 1, ids=["2-1031"])
rule("r7-1023", r"^Dvādasa koṭisataṃ tesaṃ", "Mười hai nghìn triệu của họ, cộng hai trăm tám mươi triệu;",
     "Tuổi thọ của họ là mười hai nghìn triệu, cộng hai trăm tám mươi triệu;", 1)
rule("r7-1023", r"^Paññāsa satasahassāni, vassaggena", "Cộng năm triệu, đã được công bố tính theo số năm.",
     "Cộng năm triệu năm, đã được công bố theo số năm.", 1)
rule("r7-heading", r"^#### Diṭṭhasutādidassanavāro", "những gì được thấy được nghe và", "những gì được thấy, được nghe và",
     1)
for q in ["có đầy đủ các lĩnh vực nhận biết", "mù bẩm sinh", "điếc bẩm sinh", "mù và điếc bẩm sinh"]:
    rule("r7-rebirth", r"tiracchānagatānaṃ,? nerayikānaṃ", f"hóa sinh, chúng sinh địa ngục, {q},",
         f"hóa sinh và chúng sinh địa ngục {'' if q.startswith('có') else 'bị '}{q},", 3)


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
    text = open(os.path.join(d, part + ".md"), "rb").read().decode("utf-8")
    assert "\r" not in text, part
    return text


def norm(s):
    s = re.sub(r"\s*\^[\w-]+\s*$", "", s)
    return re.sub(r"\s+", " ", s).strip()


def divergences(texts):
    """identical Pāli (block ID stripped) -> set of Vietnamese renderings; groups with >1 rendering"""
    grp, where = collections.defaultdict(set), collections.defaultdict(list)
    for part in PARTS:
        pl = nonempty(os.path.join(PDIR, part + ".md"))
        vl = [l for l in texts[part].lstrip("﻿").splitlines() if l.strip()]
        for k, (p, v) in enumerate(zip(pl, vl)):
            key = norm(p)
            if len(key) < 12:
                continue
            grp[key].add(norm(v))
            where[key].append(f"{part.split('-')[0]}:L{k + 1}")
    return {k: (v, where[k]) for k, v in grp.items() if len(v) > 1}


def apply(r, e):
    """-> (new line, number of replacements)"""
    if r["line"]:
        if r["old"] not in e:
            return e, 0
        m = re.search(r"\s\^[\w-]+\s*$", e)
        return r["new"] + (m.group(0) if m else ""), 1
    if r["rx"]:
        e2, n = re.subn(r["old"], r["new"], e)
        return e2, (n if e2 != e else 0)
    n = e.count(r["old"])
    return e.replace(r["old"], r["new"]), n


def main(dry=False):
    if ensure_backup():
        print("backup written:", BAK)
    for r in R:
        r["prx"] = re.compile(r["pali"])
    log, tot, files_of = [], collections.Counter(), collections.defaultdict(set)
    changed, residual = collections.Counter(), collections.Counter()
    before, after = {}, {}
    for part in PARTS:
        ch = part.split("-")[0]
        pl = nonempty(os.path.join(PDIR, part + ".md"))
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
            hits = []
            for ri, r in enumerate(R):
                if r["parts"] and ch not in r["parts"]:
                    continue
                if r["ids"] and sid_of.get(k) not in r["ids"]:
                    continue
                if not r["prx"].search(p):
                    continue
                e2, n = apply(r, e)
                if n:
                    hits.append(ri)
                    log.append((r["rid"], part, sid_of.get(k, "?"), k + 1, e, e2))
                    tot[ri] += n
                    files_of[ri].add(ch)
                    e = e2
            for ri, r in enumerate(R):  # residual: old wording still on a line in the rule's scope
                if r["line"] or (r["parts"] and ch not in r["parts"]) or (r["ids"] and sid_of.get(k) not in r["ids"]):
                    continue
                if r["prx"].search(p) and not r["rx"] and r["old"] in e and r["old"] not in r["new"]:
                    residual[ri] += e.count(r["old"])
            if e != e0:
                brackets_ok = any(R[ri]["brackets"] for ri in hits)
                assert dashes(e) == dashes(e0), (part, k + 1, "dash count changed", e)
                assert ID.findall(e) == ID.findall(e0), (part, k + 1, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k + 1, "heading")
                if not brackets_ok:
                    assert re.findall(r"\[[^\]]*\]", e) == re.findall(r"\[[^\]]*\]", e0), (part, k + 1, "brackets")
                assert e.count("…") == e0.count("…"), (part, k + 1, "ellipsis count", e)
                assert "—" not in e and ":-" not in e and "….” " not in e, (part, k + 1)
                assert not re.search(r"\blà là\b", e), (part, k + 1, "doubled là")
                assert e.strip(), (part, k + 1)
                el[li] = e
                changed[part] += 1
        out = "\n".join(el)
        assert out.count("\n") == text.count("\n"), part
        after[part] = out
    # every rule must make exactly the number of replacements it declares
    bad = [(ri, r) for ri, r in enumerate(R) if tot[ri] != r["n"]]
    print("replacements per rule (expected = actual; chapters):")
    for ri, r in enumerate(R):
        flag = "" if tot[ri] == r["n"] else f"   <-- EXPECTED {r['n']}"
        print(f"  {ri:3d} {r['rid']:22s} {tot[ri]:4d}  ch={','.join(sorted(files_of[ri], key=int))}"
              f"  residual={residual[ri]}{flag}  | {str(r['old'])[:60]}")
    if bad:
        sys.exit(f"ABORT: {len(bad)} rule(s) with an unexpected count; nothing written")
    assert not any(residual.values()), "residual old wording left in scope"
    if not dry:
        for part in PARTS:
            open(os.path.join(VDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(after[part])
        with open(os.path.join(HERE, "review-fixes-log.tsv"), "w", encoding="utf-8", newline="\n") as f:
            f.write("rule\tfile\tsegment\tline\told\tnew\n")
            for rid, part, sid, ln, old, new in log:
                f.write(f"{rid}\t{part}\t^{sid}\t{ln}\t{old}\t{new}\n")
    per_rid = collections.Counter()
    for ri, r in enumerate(R):
        per_rid[r["rid"]] += tot[ri]
    print("replacements per rule id:", dict(per_rid))
    print("lines changed per file:", {p.split("-")[0]: n for p, n in changed.items()}, "total",
          sum(changed.values()), "(dry run, nothing written)" if dry else "")
    db, da = divergences(before), divergences(after)
    new = {k: v for k, v in da.items() if k not in db}
    print(f"identical-Pāli groups with differing Vietnamese: before {len(db)}, after {len(da)}, new {len(new)}")
    for k, (vs, wh) in list(new.items())[:20]:
        print("  NEW DIVERGENCE:", wh[:6], "|", k[:120])
        for v in vs:
            print("     V:", v[:200])


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)

