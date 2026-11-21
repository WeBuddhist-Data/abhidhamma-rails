"""pi-5 Vietnamese rails: user-approved review fixes (2026-11-22), part r5 (ch23-ch31).

Builds every chapter of the part from rails\\backup-pre-review\\<ch>.md (made once from the current file),
applies block-anchored exact replacements with asserted counts, writes the chapter (LF) and logs to
rails\\review-fixes-log-r5.tsv. Re-runnable.

usage: python -I -X utf8 -B review_fixes_r5_vi.py            (apply)
       python -I -X utf8 -B review_fixes_r5_vi.py scan <re> [vi|pi]
       python -I -X utf8 -B review_fixes_r5_vi.py seg <id,id> [vi|pi]
"""
import os
import re
import shutil
import sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
VI = os.path.join(ROOT, r"AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters")
PI = os.path.join(ROOT, r"AI_translation\pali\pi-5_split_chapters")
RAILS = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-5-vi-ai\rails")
BACKUP = os.path.join(RAILS, "backup-pre-review")
LOG = os.path.join(RAILS, "review-fixes-log-r5.tsv")
CHS = ["23-pannarasamavaggo.md", "24-solasamavaggo.md", "25-sattarasamavaggo.md",
       "26-attharasamavaggo.md", "27-ekunavisatimavaggo.md", "28-visatimavaggo.md",
       "29-ekavisatimavaggo.md", "30-bavisatimavaggo.md", "31-tevisatimavaggo.md"]

NOI = "Có phải không có bất cứ tính chất làm điều kiện thực hành nào không?"
NOI2 = "Có phải không tồn tại bất cứ tính chất làm điều kiện thực hành nào không?"
CON = "Vậy thì có tính chất làm điều kiện thực hành nào đó."
CON2 = "Vậy thì có tồn tại tính chất làm điều kiện thực hành nào đó."

# (chapter, block id, old, new, expected count, decision)
RULES = [
    # ---- ch23
    ("23", "5-738",
     "Có phải sự tích lũy nghiệp cùng sinh với nghiệp không, đúng vậy. Có phải sự tích lũy nghiệp cùng sinh với nghiệp thiện là thiện không, không nên nói như vậy…",
     "Có phải sự tích lũy nghiệp cùng sinh với nghiệp không? Đúng vậy. Có phải sự tích lũy nghiệp cùng sinh với nghiệp thiện là thiện không? Không nên nói như vậy…",
     1, "B10"),
    ("23", "5-742", "Có phải nghiệp là khác, sự tích lũy nghiệp là khác không, đúng vậy.",
     "Có phải nghiệp là khác, sự tích lũy nghiệp là khác không? Đúng vậy.", 1, "B10"),
    ("23", "5-742", "Phú-lâu-na", "Pun-na", 2, "A3"),
    ("23", "5-742",
     "Tính chất làm điều kiện được xác định riêng biệt, sự sinh khởi tùy thuộc vào điều kiện, thời gian, khoảnh khắc, chốc lát và thời khắc, bốn ô nhiễm không phải là đối tượng của ô nhiễm, sự lão hóa và sự chết của các hiện tượng vượt thế gian là vượt thế gian, thành tựu thiền chấm dứt tri giác và cảm giác là vượt thế gian, thành tựu thiền chấm dứt tri giác và cảm giác thuộc thế gian, người đang nhập sự chấm dứt tri giác và cảm giác có thể qua đời, chính con đường ấy hướng đến sự tái sinh vào cõi chúng sinh Vô Tưởng, nghiệp là khác, sự tích lũy nghiệp là khác.",
     "Tính chất làm điều kiện được xác định riêng biệt; sự sinh khởi tùy thuộc vào điều kiện; thời gian; khoảnh khắc, chốc lát và thời khắc; bốn ô nhiễm không phải là đối tượng của ô nhiễm; sự lão hóa và sự chết của các hiện tượng vượt thế gian là vượt thế gian; thành tựu thiền chấm dứt tri giác và cảm giác là vượt thế gian; thành tựu thiền chấm dứt tri giác và cảm giác thuộc thế gian; người đang nhập sự chấm dứt tri giác và cảm giác có thể qua đời; chính con đường ấy hướng đến sự tái sinh vào cõi chúng sinh Vô Tưởng; nghiệp là khác, sự tích lũy nghiệp là khác.",
     1, "B16"),
    # ---- ch24
    ("24", "5-770", "Chẳng phải do nghiệp thuộc cõi dục lạc đã được tạo, vật chất thuộc cõi dục lạc sao?",
     "Chẳng phải vật chất do nghiệp thuộc cõi dục lạc đã được tạo là thuộc cõi dục lạc sao?", 1, "minor"),
    ("24", "5-770",
     "Nếu do nghiệp thuộc cõi dục lạc đã được tạo, vật chất thuộc cõi dục lạc, thì này bạn, chắc chắn nên nói – “do nghiệp thuộc cõi hình sắc đã được tạo, vật chất thuộc cõi hình sắc, do nghiệp thuộc cõi không hình sắc đã được tạo, vật chất thuộc cõi không hình sắc”.",
     "Nếu vật chất do nghiệp thuộc cõi dục lạc đã được tạo là thuộc cõi dục lạc, thì này bạn, chắc chắn nên nói – “vật chất do nghiệp thuộc cõi hình sắc đã được tạo là thuộc cõi hình sắc, vật chất do nghiệp thuộc cõi không hình sắc đã được tạo là thuộc cõi không hình sắc”.",
     1, "minor"),
    # ---- ch25
    ("25", "5-777", "làm nghiệp", "tạo nghiệp", 8, "B3"),
    ("25", "5-787",
     "Chẳng phải cái gì vô thường thì cái ấy là khổ đau [Tương Ưng Bộ Kinh 3.15], Đức Thế Tôn đã nói – “điều không gắn kết",
     "Chẳng phải Đức Thế Tôn đã nói rằng cái gì vô thường thì cái ấy là khổ đau [Tương Ưng Bộ Kinh 3.15], và đã nói – “điều không gắn kết",
     1, "A6"),
    ("25", "5-787",
     "Nếu cái gì vô thường thì cái ấy là khổ đau [Tương Ưng Bộ Kinh 3.15], Đức Thế Tôn đã nói – điều không gắn kết",
     "Nếu Đức Thế Tôn đã nói rằng cái gì vô thường thì cái ấy là khổ đau [Tương Ưng Bộ Kinh 3.15], và đã nói – điều không gắn kết",
     1, "A6"),
    ("25", "5-798", "Sakka, vua của chư thiên", "Đế Thích, vua của chư thiên", 1, "B17"),
    ("25", "5-798", "Đang làm phước còn chấp trước,", "Làm phước dẫn đến tái sinh,", 2, "A5"),
    ("25", "5-798", "điều được bố thí ở đâu có quả lớn”.", "điều được bố thí ở đâu có quả lớn.", 1, "minor"),
    ("25", "5-798", "an định trong trí tuệ và giới hạnh.\nĐối với loài người",
     "an định trong trí tuệ và giới hạnh.\n“Đối với loài người", 1, "minor"),
    ("25", "5-801",
     "Bậc A-la-hán có sự tích lũy phước, bậc A-la-hán không có cái chết không đúng lúc, tất cả điều này đều do nghiệp, chỉ điều gắn kết với các năng lực mới là khổ đau, ngoại trừ con đường cao quý, các tạo tác còn lại là khổ đau, Tăng đoàn nhận phần cúng dường, Tăng đoàn làm thanh tịnh phần cúng dường, Tăng đoàn ăn, uống, nhai, nếm, điều được bố thí cho Tăng đoàn có quả lớn, có sự bố thí vì sự thanh tịnh",
     "Bậc A-la-hán có sự tích lũy phước; bậc A-la-hán không có cái chết không đúng lúc; tất cả điều này đều do nghiệp; chỉ điều gắn kết với các năng lực mới là khổ đau; ngoại trừ con đường cao quý, các tạo tác còn lại là khổ đau; Tăng đoàn nhận phần cúng dường; Tăng đoàn làm thanh tịnh phần cúng dường; Tăng đoàn ăn, uống, nhai, nếm; điều được bố thí cho Tăng đoàn có quả lớn; có sự bố thí vì sự thanh tịnh",
     1, "B16"),
    # ---- ch26
    ("26", "5-809", "cơm và cháo", "cơm và món đậu nấu", 2, "minor"),
    ("26", "5-820", "hai tầng thiền thuộc hiện tại", "hai tầng thiền đã sinh khởi", 2, "minor"),
    ("26", "5-820", "tầng thiền thứ hai thuộc hiện tại", "tầng thiền thứ hai đã sinh khởi", 2, "minor"),
    ("26", "5-823", "là người đang nhập không?", "là người đang nhập thiền không?", 1, "A19"),
    ("26", "5-823", "người đang nhập thành tựu thiền", "người đang nhập thiền", 5, "A19"),
    ("26", "5-824", "người đang nhập thành tựu thiền", "người đang nhập thiền", 2, "A19"),
    ("26", "5-825",
     "Có phải nếu Đức Thế Tôn đã nói rằng đối với tầng thiền thứ nhất, âm thanh là cái gai, thì người đang nhập thành tựu thiền nghe âm thanh không?",
     "Có phải vì Đức Thế Tôn đã nói rằng đối với tầng thiền thứ nhất, âm thanh là cái gai, nên người đang nhập thiền nghe âm thanh không?",
     2, "A19+minor"),
    ("26", "5-825", "là cái gai, người ấy có sự hướng tâm và sự duy trì tâm không?",
     "là cái gai, nên người ấy có sự hướng tâm và sự duy trì tâm không?", 1, "minor"),
    ("26", "5-825", "là cái gai, người ấy có tri giác và cảm giác không?",
     "là cái gai, nên người ấy có tri giác và cảm giác không?", 1, "minor"),
    ("26", "5-826",
     "Có phải chạm vào hình sắc bằng vật chất không? Đúng vậy. Có phải nhận biết rõ hình sắc bằng vật chất không? Không nên nói như vậy… có phải nhận biết rõ hình sắc bằng vật chất không?",
     "Có phải chạm vào vật chất bằng vật chất không? Đúng vậy. Có phải nhận biết rõ vật chất bằng vật chất không? Không nên nói như vậy… có phải nhận biết rõ vật chất bằng vật chất không?",
     1, "minor"),
    ("26", "5-826", "chạm vào vật xúc chạm bằng thân không? Đúng vậy. Có phải chạm vào hình sắc bằng vật chất không?",
     "chạm vào vật xúc chạm bằng thân không? Đúng vậy. Có phải chạm vào vật chất bằng vật chất không?", 1, "minor"),
    ("26", "5-827",
     "Đức Phật, Đức Thế Tôn đã sống trong thế giới loài người, Giáo Pháp đã được Đức Phật, Đức Thế Tôn thuyết giảng, Đức Phật, Đức Thế Tôn không có lòng trắc ẩn, phân và nước tiểu của Đức Phật, Đức Thế Tôn vượt trội hơn hẳn các loại hương thơm khác, tự mình chứng nghiệm bốn thành quả của đời sống sa-môn bằng một con đường cao quý, chuyển từ tầng thiền sang tầng thiền, tầng thiền trung gian tồn tại, người đang nhập thành tựu thiền nghe âm thanh, thấy hình sắc bằng mắt, chạm vào vật xúc chạm bằng thân.",
     "Đức Phật, Đức Thế Tôn đã sống trong thế giới loài người; Giáo Pháp đã được Đức Phật, Đức Thế Tôn thuyết giảng; Đức Phật, Đức Thế Tôn không có lòng trắc ẩn; phân và nước tiểu của Đức Phật, Đức Thế Tôn vượt trội hơn hẳn các loại hương thơm khác; tự mình chứng nghiệm bốn thành quả của đời sống sa-môn bằng một con đường cao quý; chuyển từ tầng thiền sang tầng thiền; tầng thiền trung gian tồn tại; người đang nhập thiền nghe âm thanh; thấy hình sắc bằng mắt, chạm vào vật xúc chạm bằng thân.",
     1, "A19+B16"),
    # ---- ch27
    ("27", "5-856",
     "Dứt bỏ các phiền não thuộc quá khứ, dứt bỏ các phiền não thuộc tương lai, dứt bỏ các phiền não thuộc hiện tại, sự trống rỗng nằm trong khối tạo tác, thành quả của đời sống sa-môn không do điều kiện tạo thành, sự đạt đến không do điều kiện tạo thành, tính đúng như thật của tất cả các hiện tượng không do điều kiện tạo thành, yếu tố Niết-bàn là thiện, người phàm phu có tính cố định hoàn toàn, năm năng lực thuộc thế gian không tồn tại.",
     "Dứt bỏ các phiền não thuộc quá khứ, dứt bỏ các phiền não thuộc tương lai, dứt bỏ các phiền não thuộc hiện tại; sự trống rỗng nằm trong khối tạo tác; thành quả của đời sống sa-môn không do điều kiện tạo thành; sự đạt đến không do điều kiện tạo thành; tính đúng như thật của tất cả các hiện tượng không do điều kiện tạo thành; yếu tố Niết-bàn là thiện; người phàm phu có tính cố định hoàn toàn; năm năng lực thuộc thế gian không tồn tại.",
     1, "B16"),
    # ---- ch28
    ("28", "5-861", "tồn tại suốt một kiếp", "lưu lại suốt một kiếp", 2, "B14"),
    ("28", "5-862", "tồn tại suốt một kiếp", "lưu lại suốt một kiếp", 1, "B14"),
    ("28", "5-868", "rồi đẽo bằng rìu…", "rồi đẽo bằng rìu lưỡi ngang…", 1, "minor"),
    ("28", "5-868", "rồi đẽo bằng búa [", "rồi đẽo bằng rìu [", 1, "minor"),
    ("28", "5-870", ", là xe cộ cõi trời được thắng một nghìn con", ", và cỗ xe cõi trời do một nghìn con kéo", 2, "A4"),
    ("28", "5-871", "người giữ ngựa đực", "người giữ ngựa", 1, "A2"),
    ("28", "5-877", "khổ đau ấy cần dứt bỏ’", "khổ đau ấy cần được dứt bỏ’", 1, "minor"),
    ("28", "5-877", "đã sống, với quá khứ, và kẻ giết mẹ.", "đã sống, các phiền não thuộc quá khứ, và kẻ giết mẹ.", 1, "minor"),
    ("28", "5-877",
     "kẻ chia rẽ Tăng đoàn là người tạo nghiệp có quả không gián đoạn, người phàm phu không có hiểu biết, trong các địa ngục không có những kẻ canh giữ địa ngục, giữa chư thiên có loài súc sinh, con đường gồm năm chi phần, hiểu biết có mười hai chủ đề là vượt thế gian.",
     "kẻ chia rẽ Tăng đoàn là người tạo nghiệp có quả không gián đoạn; người phàm phu không có hiểu biết; trong các địa ngục không có những kẻ canh giữ địa ngục; giữa chư thiên có loài súc sinh; con đường gồm năm chi phần; hiểu biết có mười hai chủ đề là vượt thế gian.",
     1, "B16"),
    # ---- ch30
    ("30", "5-892", "không còn phiền não", "không có phiền não", 2, "minor"),
    ("30", "5-894", "làm nghiệp", "tạo nghiệp", 8, "B3"),
    ("30", "5-903", NOI, NOI2, 2, "B9"),
    ("30", "5-903", CON, CON2, 2, "B9"),
    ("30", "5-904", NOI, NOI2, 2, "B9"),
    ("30", "5-904", CON, CON2, 2, "B9"),
    ("30", "5-905", NOI, NOI2, 2, "B9"),
    ("30", "5-905", CON, CON2, 2, "B9"),
    ("30", "5-907", "không có bất cứ tính chất làm điều kiện thực hành nào,",
     "không tồn tại bất cứ tính chất làm điều kiện thực hành nào,", 1, "B9"),
    # ---- ch31
    ("31", "5-917",
     "Chẳng phải cái gì vô thường thì cái ấy là khổ đau [Tương Ưng Bộ Kinh 3.15], Đức Thế Tôn đã nói – “vật chất",
     "Chẳng phải Đức Thế Tôn đã nói rằng cái gì vô thường thì cái ấy là khổ đau [Tương Ưng Bộ Kinh 3.15], và đã nói – “vật chất",
     1, "A6"),
    ("31", "5-917", "Nếu cái gì vô thường thì cái ấy là khổ đau, Đức Thế Tôn đã nói – “vật chất",
     "Nếu Đức Thế Tôn đã nói rằng cái gì vô thường thì cái ấy là khổ đau, và đã nói – “vật chất", 1, "A6"),
    ("31", "5-918", "Chẳng phải cái gì vô thường thì cái ấy là khổ đau, Đức Thế Tôn đã nói – “năng lực",
     "Chẳng phải Đức Thế Tôn đã nói rằng cái gì vô thường thì cái ấy là khổ đau, và đã nói – “năng lực", 1, "A6"),
    ("31", "5-918", "Nếu cái gì vô thường thì cái ấy là khổ đau, Đức Thế Tôn đã nói – “năng lực",
     "Nếu Đức Thế Tôn đã nói rằng cái gì vô thường thì cái ấy là khổ đau, và đã nói – “năng lực", 1, "A6"),
    ("31", "5-918",
     "Với cùng một ý định thì được phép hưởng thụ hành vi dâm dục, những chúng sinh không phải loài người, trong hình dạng của các bậc A-la-hán, hưởng thụ hành vi dâm dục, Bồ-tát, do việc làm theo ý muốn nhờ quyền uy, đi đến nơi đọa lạc, nhập vào bào thai, đã làm những việc khổ hạnh khó làm, đã làm khổ hạnh khác, đã tôn xưng một vị khác làm bậc đạo sư, có cái không phải là sự tham đắm nhưng tương tự sự tham đắm, có cái không phải là sự sân hận nhưng tương tự sự sân hận, có cái không phải là sự si mê nhưng tương tự sự si mê, có cái không phải là phiền não nhưng tương tự phiền não, vật chất không được hình thành trọn vẹn, năng lực",
     "Với cùng một ý định thì được phép hưởng thụ hành vi dâm dục; những chúng sinh không phải loài người, trong hình dạng của các bậc A-la-hán, hưởng thụ hành vi dâm dục; Bồ-tát, do việc làm theo ý muốn nhờ quyền uy, đi đến nơi đọa lạc; nhập vào bào thai; đã làm những việc khổ hạnh khó làm; đã làm khổ hạnh khác; đã tôn xưng một vị khác làm bậc đạo sư; có cái không phải là sự tham đắm nhưng tương tự sự tham đắm, có cái không phải là sự sân hận nhưng tương tự sự sân hận, có cái không phải là sự si mê nhưng tương tự sự si mê, có cái không phải là phiền não nhưng tương tự phiền não; vật chất không được hình thành trọn vẹn, năng lực",
     1, "B16"),
]

# strings that must have 0 hits in the part after the fixes
GONE = ["Phú-lâu-na", "ngựa đực", "làm nghiệp", "Sakka", "còn chấp trước", "người đang nhập thành tựu thiền",
        "người đang nhập không", "cơm và cháo", "tầng thiền thuộc hiện tại", "thứ hai thuộc hiện tại",
        "xe cộ cõi trời", "tồn tại suốt một kiếp",
        "đẽo bằng búa", "cần dứt bỏ", "với quá khứ", "không còn phiền não",
        "không có bất cứ tính chất làm điều kiện thực hành", "Vậy thì có tính chất làm điều kiện",
        "Chẳng phải cái gì vô thường", "Nếu cái gì vô thường", "không, đúng vậy", "không, không nên nói",
        "chạm vào hình sắc bằng vật chất"]
BAD = ["—", ":-", "….", "được được", "là là", "chánh niệm", "seed", "  ", "\r"]


def segs_of(txt):
    return txt.split("\n\n")


def bid(seg):
    m = re.search(r"\^([\d-]+)\s*$", seg)
    return m.group(1) if m else None


def apply():
    os.makedirs(BACKUP, exist_ok=True)
    log = ["file\tblock\told\tnew\tcount\tdecision"]
    report = []
    for ch in CHS:
        src = os.path.join(BACKUP, ch)
        if not os.path.exists(src):
            shutil.copyfile(os.path.join(VI, ch), src)
        txt = open(src, encoding="utf-8", newline="").read()
        segs = segs_of(txt)
        idx = {bid(s): i for i, s in enumerate(segs) if bid(s)}
        for (c, b, old, new, n, dec) in RULES:
            if c != ch[:2]:
                continue
            i = idx[b]
            k = segs[i].count(old)
            assert k == n, (ch, b, old[:60], k, n)
            segs[i] = segs[i].replace(old, new)
            log.append("\t".join([ch, "^" + b, old.replace("\n", "\\n"), new.replace("\n", "\\n"), str(n), dec]))
        out = "\n\n".join(segs)
        for g in GONE:
            assert g not in out, (ch, g)
        for g in BAD:
            assert g not in out, (ch, repr(g))
        with open(os.path.join(VI, ch), "w", encoding="utf-8", newline="\n") as f:
            f.write(out)
        a, bb = txt.split("\n"), out.split("\n")
        assert len(a) == len(bb), ch
        report.append((ch, sum(1 for x, y in zip(a, bb) if x != y)))
    with open(LOG, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(log) + "\n")
    for ch, n in report:
        print(ch, "lines changed:", n)
    dec = {}
    for (c, b, old, new, n, d) in RULES:
        dec[d] = dec.get(d, 0) + n
    print("replacements per decision:", dec)


def scan(pat, side="vi"):
    for ch in CHS:
        d = VI if side == "vi" else PI
        txt = open(os.path.join(d, ch), encoding="utf-8").read()
        for s in segs_of(txt):
            for ln in s.split("\n"):
                if re.search(pat, ln):
                    print("==", ch[:2], bid(s), "|", ln)


def seg(ids, side="pi"):
    want = set(ids.split(","))
    for ch in CHS:
        d = VI if side == "vi" else PI
        txt = open(os.path.join(d, ch), encoding="utf-8").read()
        for s in segs_of(txt):
            if bid(s) in want:
                print("==", ch[:2], bid(s))
                print(s)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "scan":
        scan(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "vi")
    elif len(sys.argv) > 1 and sys.argv[1] == "seg":
        seg(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "pi")
    else:
        apply()
