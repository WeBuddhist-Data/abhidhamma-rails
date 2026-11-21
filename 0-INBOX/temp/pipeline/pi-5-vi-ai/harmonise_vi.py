"""Consistency (harmonise) pass for the pi-5 Vietnamese plain zero-shot (Kathāvatthu, 32 files, 1,400 segments).

Adapted from pi-4-vi-ai/harmonise_vi.py (pi-4 files untouched).
Exact old -> new string replacements, each scoped to one segment (chapter + block ID; "*" = every segment of the
file) and each with an asserted count of occurrences in that scope. Rules run in the order listed (a later rule sees
the text left by an earlier one). Line counts, block IDs, heading levels, dashes and ellipses are never touched
(asserted per changed line); variant brackets are asserted unchanged except by the bracket rules (HB*), which may
only change a label inside a bracket (bracket count and every Pāli word asserted equal).
The builders are NOT rerun (harmonise-notes.md lists the builder constants that would need the same change).
Protected (user-approved sample, not named by harmonise-brief.md for any change): preamble.md, 1-puggalakatha.md.
Backup of the pre-pass files: backup-pre-harmonise/ (made once by vi_common.ensure_backup, never overwritten).
The pass always reads from the backup, so it is idempotent: rerunning it rebuilds the same output.
Log: harmonise-log.tsv (rule, file, block id, line, old, new, reason). Decisions: harmonise-notes.md.

usage: python -I -X utf8 harmonise_vi.py [--dry]
       a rule with count -1 only reports what it finds (used while drafting; none is left in the final list)
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PDIR, VDIR, HERE, BAK, PARTS, PROTECTED_PARTS, ID

R = []  # (rid, part, sid, old, new, count, reason)
P = {p.split("-")[0]: p for p in PARTS if p[0].isdigit()}


def rule(rid, ch, sid, old, new, n, reason):
    part = P[str(ch)]
    assert old != new, (rid, old)
    R.append((rid, part, sid, old, new, n, reason))


# =============================================================== N1 as written (named points)
W = "as written (user rule; coordinator: never merge sentences / drop no word)"
rule("N1-sunetta", 4, "5-281",
     "Do không hiểu ra, không thấu triệt giới hạnh cao quý, định tâm cao quý, trí tuệ cao quý và sự giải thoát cao quý.",
     "Do không hiểu ra, không thấu triệt giới hạnh cao quý, định tâm cao quý, trí tuệ cao quý, do không hiểu ra, "
     "không thấu triệt sự giải thoát cao quý.", 1,
     W + ": the Pāli has ananubodhā appaṭivedhā twice (with sīlassa and with vimuttiyā); both restored, no «và» (no ca)")
rule("N1-punabbhava", 4, "5-281", "nay không còn sự tái sinh nữa", "nay không còn sự hiện hữu mới nữa", 1,
     "punabbhava = «sự hiện hữu mới» (pi-2; coordinator rule; ch12 natthi dāni punabbhavo)")
rule("N1-dhamma2", 7, "5-299",
     "Có phải các hiện tượng thuộc quá khứ một phần có quả đã chín muồi, một phần có quả chưa chín muồi, đã chấm dứt",
     "Có phải các hiện tượng thuộc quá khứ một phần có quả đã chín muồi, các hiện tượng một phần có quả chưa chín muồi, "
     "đã chấm dứt", 1, W + ": ekadesaṃ vipakkavipākā dhammā ekadesaṃ avipakkavipākā dhammā (dhammā twice)")
rule("N1-full-stop", 12, "5-405", "Ta sẽ tôn xưng ai?", "Ta sẽ tôn xưng ai.", 1,
     "coordinator: the Pāli's own «.» stays (kamuddiseyyaṃ.), the question word «ai» kept")
rule("N1-heading-stop", 27, "5-27-3-1-0", "(188) 3. Bàn", "(188) 3 Bàn", 1, W + ": the Pāli heading has «(188) 3» without a full stop")
rule("N1-ruhiruppada", 3, "5-269", "kẻ làm chảy máu Như Lai", "kẻ làm chảy máu", 2,
     "ruhiruppādaka = «kẻ làm chảy máu» (coordinator rule; ch10 / ch27 / ch28): «Như Lai» is not in the Pāli")
# added words: keep only where Vietnamese grammar needs them
WCH = ("«chúng» added (no te in the Pāli): dropped in the «vì cho rằng …» clause, which needs no subject (ch11 «vì cho "
       "rằng là …»); kept as the subject of the main clause, which Vietnamese needs")
rule("N1-chung", 7, "5-299", "vì cho rằng chúng sẽ trổ quả", "vì cho rằng sẽ trổ quả", 2, WCH)
rule("N1-chung", 7, "5-300", "vì cho rằng chúng sẽ sinh khởi", "vì cho rằng sẽ sinh khởi", 2, WCH)
rule("N1-chung", 15, "5-476", "vì cho rằng chúng cùng sinh", "vì cho rằng cùng sinh", 4, WCH)
WSE = "cakkavattisatta: «sẽ» is not in the Pāli and Vietnamese grammar does not need it (as bodhisatta «Bồ-tát»)"
rule("N1-se", 12, "*", "người sẽ làm vua chuyển luân", "người làm vua chuyển luân", 13, WSE)
rule("N1-se", 15, "*", "người sẽ làm vua chuyển luân", "người làm vua chuyển luân", 4, WSE)
rule("N1-bac", 13, "5-423", " là bậc vĩ đại”", " vĩ đại”", 4,
     "uḷāro (adjective predicate): «là bậc» not in the Pāli and not needed (Vietnamese adjective predicate)")

# =============================================================== N2 sample wins
rule("N2-amanta", 3, "5-270", "trong sạch không? Đúng vậy. Có phải người nào mang bình bát",
     "trong sạch không? Đúng vậy? Có phải người nào mang bình bát", 1,
     "Āmantā? = «Đúng vậy?» (sample ^5-95; coordinator rule)")
S_POS = ("có kết quả đáng mong muốn, có kết quả đáng yêu mến, có kết quả đáng ưa thích, có kết quả không pha tạp, "
         "đưa đến sự dễ chịu, có quả trổ dễ chịu")
S_NEG = ("có kết quả không đáng mong muốn, có kết quả không đáng yêu mến, có kết quả không đáng ưa thích, "
         "có kết quả pha tạp, đưa đến sự khó chịu, có quả trổ khó chịu")
O_POS = ("có quả đáng mong muốn, có quả đáng yêu thích, có quả vừa ý, có quả không pha tạp, đưa đến hạnh phúc, "
         "có kết quả hạnh phúc")
O_NEG = ("có quả không đáng mong muốn, có quả không đáng yêu thích, có quả không vừa ý, có quả bị pha tạp, "
         "đưa đến khổ đau, có kết quả khổ đau")
WS = "iṭṭhaphala … sukhudraya sukhavipāka (and the negatives) = the sample's forms (^5-98, ^5-99, ^5-101, ^5-102)"
rule("N2-phala", 10, "5-338", O_NEG, S_NEG, 2, WS)
rule("N2-phala", 10, "5-338", O_POS, S_POS, 4, WS)
rule("N2-phala", 15, "5-479", O_NEG, S_NEG, 1, WS)
rule("N2-phala", 15, "5-479", O_POS, S_POS, 4, WS)
rule("N2-phala", 15, "5-479", "sự bố thí có quả đáng mong muốn", "sự bố thí có kết quả đáng mong muốn", 2, WS)
rule("N2-phala", 15, "5-482", O_POS, S_POS, 3, WS)
rule("N2-phala", 15, "5-482", "sự bố thí có quả đáng mong muốn", "sự bố thí có kết quả đáng mong muốn", 2, WS)
rule("N2-phala", 15, "5-486", "có kết quả hạnh phúc", "có quả trổ dễ chịu", 4, WS + " (sukhavipāka)")
rule("N2-phala", 19, "5-624", "có kết quả khổ đau", "có quả trổ khó chịu", 1, WS + " (dukkhavipāka)")
WV = ("savipāka / avipāka = «có quả trổ» / «không có quả trổ» (sample savipāka «có quả trổ» ^5-98; ch18, ch22; "
      "the negative on the same word)")
rule("N2-vipaka", 15, "5-499", "có quả không?", "có quả trổ không?", 8, WV)
rule("N2-vipaka", 15, "5-500", "có quả, dẫn đến", "có quả trổ, dẫn đến", 8, WV)
rule("N2-vipaka", 20, "5-633", "có quả không?", "có quả trổ không?", 14, WV)
rule("N2-vipaka", 20, "5-634", "không có quả", "không có quả trổ", 8, WV)
rule("N2-vipaka", 20, "5-634", "đều có quả”", "đều có quả trổ”", 4, WV)
rule("N2-vipaka", 20, "5-635", "đều có quả", "đều có quả trổ", 2, WV)
rule("N2-vipaka", 20, "5-653", "tất cả nghiệp đều có quả,", "tất cả nghiệp đều có quả trổ,", 1, WV)
rule("N2-vipaka", 7, "5-299", "không có quả", "không có quả trổ", 5, WV)
WSD = "parakataṃ sukhadukkhaṃ = the sample's form (^5-173; ch25 ^5-801)"
rule("N2-sukhadukkha", 15, "5-488", "hạnh phúc và khổ đau do người khác làm,",
     "sự dễ chịu và sự khó chịu do người khác làm ra,", 1, WSD)
rule("N2-nanu", 25, "5-795",
     "Chẳng phải Đức Thế Tôn đã nói – “bữa ăn theo nhóm, bữa ăn thay thế, bữa ăn với thức ăn còn dư, bữa ăn với thức "
     "ăn không còn dư” sao?",
     "Chẳng phải Đức Thế Tôn đã nói thế này sao – “bữa ăn theo nhóm, bữa ăn thay thế, bữa ăn với thức ăn còn dư, bữa "
     "ăn với thức ăn không còn dư”?", 1,
     "Nanu vuttaṃ bhagavatā – = the sample's frame «Chẳng phải Đức Thế Tôn đã nói thế này sao –» (NANU_VUTTAM)")

# =============================================================== N3 pi-1-4 wins
WK = "kanta / manāpa = «đáng yêu mến» / «đáng ưa thích» (pi-2 iṭṭha kanta manāpa; sample kantaphala / manuññaphala)"
for ch in (10, 16):
    rule("N3-kanta", ch, "*", "đáng yêu thích", "đáng yêu mến", {10: 10, 16: 4}[ch], WK)
    rule("N3-kanta", ch, "*", "vừa ý", "đáng ưa thích", {10: 10, 16: 4}[ch], WK)
rule("N3-kanta", 15, "5-486", "đáng yêu thích", "đáng yêu mến", 4, WK)
rule("N3-kanta", 22, "5-708", "không đáng yêu thích", "không đáng yêu mến", 1, WK)
rule("N3-gotrabhu", 11, "*", "người chuyển dòng dõi", "người chuyển đổi dòng dõi", 2,
     "gotrabhū = «người chuyển đổi dòng dõi» (pi-4; coordinator rule; ch13)")
rule("N3-nekkhamma", 10, "5-338", "sự xuất ly", "sự từ bỏ", 1, "nekkhamma = «sự từ bỏ» (pi-2)")
WP = "patthanā / pattheti = «sự mong ước» / «mong ước» (pi-1 nikanti nikāmanā patthanā = … sự mong ước …; ch21, ch22)"
rule("N3-patthana", 15, "*", "ước nguyện", "mong ước", 7, WP)
rule("N3-patthana", 16, "*", "sự ước nguyện", "sự mong ước", 5, WP)
rule("N3-patthana", 17, "5-552", "sự mong muốn", "sự mong ước", 1, WP)
rule("N3-patthana", 18, "5-573", "sự ước nguyện", "sự mong ước", 1, WP)
rule("N3-patthana", 20, "5-636", "sự ước nguyện", "sự mong ước", 1, WP)
WA = "apubbaṃ acarimaṃ = «không trước không sau» (pi-2 ^2-764, ch18, ch22): «cùng một lúc» is not in the Pāli"
rule("N3-apubbam", 3, "5-273", ", cùng một lúc, không trước không sau,", ", không trước không sau,", 4, WA)
rule("N3-apubbam", 4, "5-280", "Có phải cùng một lúc, không trước không sau, tu tập", "Có phải không trước không sau, tu tập", 2, WA)
rule("N3-apubbam", 4, "5-280", "Có phải cùng một lúc, không trước không sau, tự mình chứng nghiệm",
     "Có phải không trước không sau, tự mình chứng nghiệm", 2, WA)
# sense verbs: «V O bằng X» (pi-2; ch10 ^5-338, ch18, ch20, ch26)
WSV = "cakkhunā rūpaṃ passati … = «thấy hình sắc bằng mắt …» (pi-2 word order; ch18, ch20, ch26)"
SENSE = [("mắt", "thấy hình sắc"), ("tai", "nghe âm thanh"), ("mũi", "ngửi mùi"), ("lưỡi", "nếm vị"),
         ("thân", "chạm vật xúc chạm"), ("ý", "nhận biết đối tượng của ý")]
CH5_N = {("mắt", "quá khứ"): 3, ("tai", "quá khứ"): 1, ("mũi", "quá khứ"): 1, ("lưỡi", "quá khứ"): 1, ("thân", "quá khứ"): 1,
         ("ý", "quá khứ"): 3, ("mắt", "tương lai"): 3, ("ý", "tương lai"): 3, ("mắt", "hiện tại"): 4, ("ý", "hiện tại"): 4}
for (o, t), n in CH5_N.items():
    v = dict(SENSE)[o]
    obj = v.split(" ", 1)
    rule("N3-sense", 5, "5-289", f"dùng {o} thuộc {t} mà {v} thuộc {t}", f"{v} thuộc {t} bằng {o} thuộc {t}", n, WSV)
for o, v in SENSE:
    rule("N3-sense", 10, "5-336", f"dùng {o} {v}", f"{v} bằng {o}", 2, WSV)
    rule("N3-sense", 12, "5-397", f"dùng {o} mà {v}", f"{v} bằng {o}", 2, WSV)
for o, v in SENSE:
    if o == "tai":
        continue
    vv = v.replace("đối tượng của ý", "đối tượng của ý ấy") if o == "ý" else v + " ấy"
    rule("N3-sense", 16, "*", f"dùng {o} ấy mà {vv}", f"{vv} bằng {o} ấy",
         {"mắt": 3, "mũi": 5, "lưỡi": 2, "thân": 4, "ý": 4}[o], WSV)
WPV = "paṭivijānāti = «nhận biết rõ» (pi-2 ^2 Ñāṇavibhaṅga; ch26)"
rule("N3-pativijanati", 10, "5-347", "nhận biết", "nhận biết rõ", 6, WPV)
rule("N3-pativijanati", 10, "5-352", "nhận biết", "nhận biết rõ", 4, WPV)
WM = "ariyo aṭṭhaṅgiko maggo = «con đường gồm tám chi phần cao quý» (pi-2 majority, 4 of 5)"
rule("N3-magga", 28, "5-874", "con đường cao quý gồm tám chi phần", "con đường gồm tám chi phần cao quý", 2, WM)
rule("N3-magga", 28, "5-875", "con đường cao quý gồm tám chi phần", "con đường gồm tám chi phần cao quý", 3, WM)
WPA = "pariyāpanna = «nằm trong» (pi-1 / pi-2 maggapariyāpanna «nằm trong con đường», dhammāyatanapariyāpanna; ch24, ch27)"
rule("N3-pariyapanna", 10, "5-334", "thuộc về con đường", "nằm trong con đường", 1, WPA)
rule("N3-pariyapanna", 15, "5-471", "thuộc về một số hiện tượng", "nằm trong một số hiện tượng", 2, WPA)
for sid in ("5-554", "5-555", "5-557"):
    rule("N3-pariyapanna", 17, sid, "thuộc về khối tạo tác", "nằm trong khối tạo tác", 6, WPA)
for sid in ("5-610", "5-612", "5-616"):
    rule("N3-pariyapanna", 19, sid, "thuộc về khối tạo tác", "nằm trong khối tạo tác", 6, WPA)
WDH = ("Pariyāpannakathā: saddadhātu … phoṭṭhabbadhātu = «yếu tố âm thanh … yếu tố vật xúc chạm» (pi-2 ^2-981; "
       "ch24 identical phrases), saddarāga … = «sự tham đắm âm thanh …» (ch24)")
for sid in ("5-703", "5-704"):
    for x in ("âm thanh", "mùi", "vị", "vật xúc chạm"):
        rule("N3-dhatu", 22, sid, f"sự tham đắm cõi {x}", f"sự tham đắm {x}", 2, WDH)
    for x in ("âm thanh", "vật xúc chạm"):
        rule("N3-dhatu", 22, sid, f"cõi {x}", f"yếu tố {x}", 4, WDH)
    rule("N3-pariyapanna", 22, sid, "thuộc về", "nằm trong", 10, WPA)
rule("N3-pariyapanna", 22, "5-705", "thuộc về", "nằm trong", 7, WPA)
rule("N3-pariyapanna", 22, "5-22-7-1-0", "Bàn về những gì thuộc về", "Bàn về những gì nằm trong", 1, WPA)

# =============================================================== N4 one word in one sense (coordinator rule)
rule("N4-anasava", 12, "5-392", "bậc A-la-hán không còn ô nhiễm", "bậc A-la-hán không phải là đối tượng của ô nhiễm", 2,
     "anāsava = «không phải là đối tượng của ô nhiễm» throughout the argument (coordinator: one word; pi-1)")
rule("N4-rupa", 26, "5-826", "nhận biết rõ hình sắc bằng vật chất", "nhận biết rõ vật chất bằng vật chất", 2,
     "identical Pāli Rūpena rūpaṃ paṭivijānātīti? = one form: rūpa «vật chất» (paṭivijānāti is not a seeing verb; "
     "the next question Rūpaṃ manoviññāṇaṃ already has «vật chất»)")

# =============================================================== N5 pick one (majority / earliest)
rule("N5-yoni", 11, "*", "cách thức sinh ra", "cách sinh", 17, "yoni = «cách sinh» (majority: ch14, ch16, 16 of 33; ch11 17)")
WVE = "sukhavedaniya … = «được cảm nhận là dễ chịu …» (ch15 earliest; ch20, ch24; 49 of 52)"
rule("N5-vedaniya", 16, "5-539", "đưa đến cảm giác không khó chịu cũng không dễ chịu", "được cảm nhận là không khó chịu cũng không dễ chịu", 1, WVE)
rule("N5-vedaniya", 16, "5-539", "đưa đến cảm giác dễ chịu", "được cảm nhận là dễ chịu", 1, WVE)
rule("N5-vedaniya", 16, "5-539", "đưa đến cảm giác khó chịu", "được cảm nhận là khó chịu", 1, WVE)
WVA = ("vipākābyākata = «không xác định về mặt đạo đức thuộc quả của nghiệp» (ch20 / ch30 majority, 10 of 13), "
       "kiriyābyākata «… mang tính chức năng» (pi-1); the identical list in ch19 / ch21 / ch22 one form")
rule("N5-vipakabyakata", 19, "5-605", "thuộc loại quả của nghiệp", "thuộc quả của nghiệp", 1, WVA)
rule("N5-vipakabyakata", 22, "5-706", "thuộc loại quả của nghiệp", "thuộc quả của nghiệp", 1, WVA)
rule("N5-vipakabyakata", 21, "5-676",
     "là quả của nghiệp không xác định về mặt đạo đức, điều không xác định về mặt đạo đức mang tính chức năng",
     "là cái không xác định về mặt đạo đức thuộc quả của nghiệp, cái không xác định về mặt đạo đức mang tính chức năng", 1, WVA)
WVT = "\"X\"ti vattabbo = «nên gọi là (“)X(”)» (sample; ch12, ch19, ch22); quotes only where the Pāli has them (unchanged)"
rule("N5-vattabbo", 10, "*", "nên được gọi là", "nên gọi là", 24, WVT)
rule("N5-vattabbo", 17, "*", "nên được gọi là", "nên gọi là", 4, WVT)
WDP = "dhammappaṭisaraṇo = «chỗ nương tựa của Giáo Pháp» (ch11 earliest, ch26); the identical maggakovido list = ch11"
rule("N5-patisarana", 13, "5-443", "nơi nương tựa của Giáo Pháp", "chỗ nương tựa của Giáo Pháp", 1, WDP)
rule("N5-patisarana", 13, "5-443",
     "người tuyên bố con đường chưa được tuyên bố, người biết con đường, người thông hiểu con đường, người tinh thông con đường",
     "người tuyên thuyết con đường chưa được tuyên thuyết, người biết con đường, người hiểu con đường, người thông thạo con đường",
     1, WDP)
WDD = "dadāti = «cho» (pi-4, ch15, ch25, ch28, ch30); dānaṃ dadāti = «thực hiện sự bố thí» (same chapters)"
rule("N5-dadati", 13, "5-432", "người đang dâng vật bố thí", "người đang thực hiện sự bố thí", 1, WDD)
rule("N5-dadati", 13, "5-432", "người đang dâng ", "người đang cho ", 4, WDD)
rule("N5-dadati", 13, "5-434", "người đang dâng ", "người đang cho ", 2, WDD)
rule("N5-dadati", 25, "5-798", "hãy dâng cho Tăng đoàn, khi bà đã dâng cho Tăng đoàn",
     "hãy cho Tăng đoàn, khi bà đã cho Tăng đoàn", 1, WDD + " (saṅghe dehi … dinne)")
rule("N5-buddha", 12, "5-403", "trở thành bậc giác ngộ", "trở thành Đức Phật", 2,
     "buddho by sense: the Bodhisatta becoming the Buddha = «Đức Phật»; (38) bodhiyā buddho keeps the generic «bậc giác ngộ»")
WSA = ("samādhi / vīriya as list members (saddhā… vīriyaṃ… sati… samādhi… paññā) = «sự định tâm» / «sự tinh tấn» "
       "(majority: ch15, ch17-19, ch23, ch24, ch27, ch29, ch31); a qualified samādhi keeps «định tâm» (pi-1 core term)")
for sid in ("5-527", "5-532"):
    rule("N5-samadhi", 16, sid, "niềm tin… tinh tấn… sự tỉnh thức… định tâm… trí tuệ",
         "niềm tin… sự tinh tấn… sự tỉnh thức… sự định tâm… trí tuệ", 2, WSA)
rule("N5-samadhi", 11, "5-371", "có định tâm", "có sự định tâm", 2, WSA)
rule("N5-samadhi", 11, "5-371", "và định tâm ấy", "và sự định tâm ấy", 1, WSA)
rule("HB-label", 17, "5-564", "[dị bản (Pī.): anāvaṭṭantassa; (Sī., Syā., Ka.): anāvajjantassa;",
     "[khác chính tả (Pī.): anāvaṭṭantassa; dị bản (Sī., Syā., Ka.): anāvajjantassa;", 1,
     "same kind of variant, same label: anāvaṭṭantassa = spelling (khác chính tả, ch15, ch22), anāvajjantassa = other word (dị bản)")
rule("HB-anenja", 27, "5-834", "Kinh Thích Hợp Với Sự Bất Động", "Kinh Thích Hợp Với Trạng Thái Bất Động", 1,
     "āneñja = «trạng thái bất động» (pi-2 āneñjābhisaṅkhāra; ch25, ch30); the āneñjappatta formula keeps pi-4 «đạt đến sự bất động»")
rule("N5-fifty", 28, "5-877", "đã ở lại", "đã sống", 1, "fifty-group uddāna aṭṭhāsi = ch26 thesis / uddāna «đã sống»")
rule("N5-anicca", 27, "5-832", "khối tạo tác vô thường", "khối tạo tác là vô thường", 2,
     "anicca … list as predicate: affirmative «X là vô thường, …» (sample ^5-95; ch25, ch31), negative «X không vô thường, …»")

# =============================================================== N6 other divergences found
rule("N6-ekadesa", 3, "5-274", "Có phải người ấy một phần", "Có phải một phần", 4,
     "«người ấy» not in the Pāli (coordinator: add no word); identical sentence ch11 ^5-366 «Có phải một phần …»")
for sid in ("5-275", "5-276", "5-277"):
    rule("N6-ekadesa", 3, sid, "Có phải người ấy một phần", "Có phải một phần", 4,
         "«người ấy» not in the Pāli (coordinator: add no word); identical sentence ch11 ^5-366 «Có phải một phần …»")
WT = "atīta / anāgata / paccuppanna as attribute = «thuộc quá khứ / thuộc tương lai / thuộc hiện tại» (pi-1, pi-2; ch5, ch19)"
for noun, t, n in (("vật chất", "quá khứ", 18), ("vật chất", "tương lai", 16), ("vật chất", "hiện tại", 20),
                   ("thức", "quá khứ", 16), ("thức", "tương lai", 16), ("thức", "hiện tại", 20),
                   ("cảm giác", "quá khứ", 1), ("tri giác", "quá khứ", 1), ("các tạo tác", "quá khứ", 1)):
    rule("N6-time", 6, "5-297", f"{noun} {t}", f"{noun} thuộc {t}", n, WT)
rule("N6-time", 6, "5-298", "lĩnh vực nhận biết quá khứ và tương lai", "lĩnh vực nhận biết thuộc quá khứ và tương lai", 4, WT)
rule("N6-sankhara", 6, "5-298", "bất cứ sự tạo tác nào", "bất cứ các tạo tác nào", 1,
     "identical sutta member ye keci saṅkhārā = ch5 ^5-296 (earliest; saṅkhārā «các tạo tác» as the sample)")
rule("N6-time", 21, "5-655", "kiếp quá khứ, có thể tồn tại suốt kiếp tương lai",
     "kiếp thuộc quá khứ, có thể tồn tại suốt kiếp thuộc tương lai", 1, WT)
rule("N6-time", 5, "5-296", "các vị Phật quá khứ", "các vị Phật thuộc quá khứ", 4, WT)
WFS = "coordinator: the Pāli's own «.» stays where a question is meant (paññāpeyyāti. / paññāpeyyā\"ti.); question word kept"
rule("N6-full-stop", 5, "5-296", "mô tả được không? Bạch Thế Tôn, có cái lưỡi", "mô tả được không. Bạch Thế Tôn, có cái lưỡi", 1, WFS)
rule("N6-full-stop", 5, "5-296", "mô tả được không?”", "mô tả được không”.", 1, WFS)
WES = ("samāpattesiya / upapattesiya = «tìm cầu …» (ch12, ch16, ch18, ch22: majority); the identical sentence in "
       "ch22 / ch24 one form, in the Pāli order (instrumentals before sahagato), which keeps the …pe… cuts in place")
rule("N6-esiya", 24, "*", "tìm kiếm", "tìm cầu", 41, WES)
E_OLD = ("đi kèm, cùng sinh, hòa lẫn, gắn liền, có cùng sự sinh khởi, có cùng sự chấm dứt, có cùng chỗ dựa, có cùng đối "
         "tượng với tâm tìm cầu sự thành tựu thiền, tâm tìm cầu sự tái sinh, tâm an trú trong hạnh phúc ngay trong đời này")
E_NEW = ("đi kèm với tâm tìm cầu sự thành tựu thiền, với tâm tìm cầu sự tái sinh, với tâm an trú trong hạnh phúc ngay "
         "trong đời này, cùng sinh, hòa lẫn, gắn liền, có cùng sự sinh khởi, có cùng sự chấm dứt, có cùng chỗ dựa, có "
         "cùng đối tượng")
rule("N6-esiya", 22, "5-703", "không " + E_OLD, "không " + E_NEW.replace(", với tâm", ", không với tâm"), 1, WES)
rule("N6-esiya", 22, "5-703", E_OLD, E_NEW, 1, WES)
rule("N6-esiya", 22, "5-704", E_OLD, E_NEW, 1, WES)
rule("N6-esiya", 22, "5-704", "không đi kèm… có cùng đối tượng với tâm tìm cầu sự thành tựu thiền sao?",
     "không đi kèm với tâm tìm cầu sự thành tựu thiền… có cùng đối tượng sao?", 1, WES)


# ------------------------------------------------------------------------------------------------- engine
def dashes(t):
    return t.count("—") + t.count("–")


LATIN = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+")


def bracket_pali(b):
    """the Pāli words inside a bracket: words with Pāli letters (diacritic-free Vietnamese ignored)"""
    return [w for w in LATIN.findall(b) if re.search(r"[āīūṃṅñṭḍṇḷ]", w)]


def main(dry=False):
    if vi_common.ensure_backup():
        print("backup written:", BAK)
    by_part = collections.defaultdict(list)
    for r in R:
        assert r[1] not in PROTECTED_PARTS, r
        by_part[r[1]].append(r)
    log, changed, hits, probes = [], collections.Counter(), collections.Counter(), []
    for part in PARTS:
        text = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        assert "\r" not in text and not text.startswith("﻿"), part
        if part not in by_part:
            if not dry:
                open(os.path.join(VDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(text)
            continue
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        el = text.split("\n")
        idx = [i for i, l in enumerate(el) if l.strip()]
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        sid_of, cur = {}, []
        for k in range(len(idx)):
            cur.append(k)
            m = ID.search(pl[k])
            if m:
                for kk in cur:
                    sid_of[kk] = m.group(1)
                cur = []
        orig = {k: el[idx[k]] for k in range(len(idx))}
        brule = collections.defaultdict(bool)
        for rid, _, sid, old, new, n, why in by_part[part]:
            ks = [k for k in range(len(idx)) if sid == "*" or sid_of.get(k) == sid]
            assert ks, (part, sid)
            got = sum(el[idx[k]].count(old) for k in ks)
            if n == -1:
                probes.append((rid, part, sid, got, old))
            elif dry and got != n:
                probes.append((rid, part, sid, f"MISMATCH expected {n} found {got}", old))
            else:
                assert got == n, (rid, part, sid, f"expected {n}, found {got}", old)
            for k in ks:
                e = el[idx[k]]
                if old in e:
                    log.append((rid, part, sid_of.get(k, "?"), k + 1, old, new, why))
                    el[idx[k]] = e.replace(old, new)
                    if rid.startswith("HB"):
                        brule[k] = True
            hits[rid] += got
        for k in range(len(idx)):
            e0, e = orig[k], el[idx[k]]
            if e != e0:
                assert dashes(e) == dashes(e0), (part, k, "dash count changed")
                assert ID.findall(e) == ID.findall(e0), (part, k, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k, "heading")
                b0, b1 = re.findall(r"\[[^\]]*\]", e0), re.findall(r"\[[^\]]*\]", e)
                if brule[k]:
                    assert len(b0) == len(b1), (part, k, "bracket count")
                    assert [bracket_pali(x) for x in b0] == [bracket_pali(x) for x in b1], (part, k, "bracket Pāli")
                else:
                    assert b0 == b1, (part, k, "brackets")
                assert e.count("…") == e0.count("…"), (part, k, "ellipsis")
                assert "—" not in e and ":-" not in e and "…." not in e, (part, k)
                assert "là là" not in e and "được được" not in e and "chánh niệm" not in e, (part, k)
                changed[part] += 1
        out = "\n".join(el)
        assert out.count("\n") == text.count("\n"), part
        if not dry:
            open(os.path.join(VDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(out)
    for p in probes:
        print("PROBE", p)
    if not dry:
        assert not probes, "count -1 rules left"
        with open(os.path.join(HERE, "harmonise-log.tsv"), "w", encoding="utf-8", newline="\n") as f:
            f.write("rule\tfile\tblock\tline\told\tnew\treason\n")
            for rid, part, sid, ln, old, new, why in log:
                f.write(f"{rid}\t{part}.md\t^{sid}\t{ln}\t{old}\t{new}\t{why}\n")
    for rid, n in sorted(hits.items()):
        print(f"{rid:18s} replacements={n}")
    print("lines changed per chapter:", {p.split('-')[0]: n for p, n in changed.items()},
          "total", sum(changed.values()), "log entries", len(log), "(dry run)" if dry else "")


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
