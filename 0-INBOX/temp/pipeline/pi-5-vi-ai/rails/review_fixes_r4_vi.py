# pi-5 Vietnamese rails: user-approved review fixes (findings-summary.md A / B, findings-r4.md), part r4 (ch16-22).
# Builds every chapter from its copy in backup-pre-review\ (made once, never overwritten), so it can be re-run.
# Each rule: (old, new, expected count, decision id, is_regex). Counts are asserted.
# Usage: python -I -X utf8 -B review_fixes_r4_vi.py [--dry]
import os, re, sys, shutil, unicodedata

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
CHDIR = ROOT + r"\AI_translation\vietnamese\pi-5-vietnamese-plain-rails_split_chapters"
RAILS = ROOT + r"\0-INBOX\temp\pipeline\pi-5-vi-ai\rails"
BACKUP = RAILS + r"\backup-pre-review"
LOG = RAILS + r"\review-fixes-log-r4.tsv"
DRY = "--dry" in sys.argv

S = False  # plain string
X = True   # regex

RULES = {
"16-atthamavaggo": [
    # B10 missing «?» (^5-504)
    ("Chẳng phải có nhóm a-tu-la sao, đúng vậy.", "Chẳng phải có nhóm a-tu-la sao? Đúng vậy.", 1, "B10", S),
    # B14 verse idiom tiṭṭhanti citrāni tatheva (^5-514)
    ("Những thứ muôn màu kéo dài cũng y như vậy trong thế gian;", "Những thứ muôn màu vẫn còn nguyên như thế trong thế gian;", 1, "B14", S),
    # minor: rūpānaṃ nissaraṇaṃ arūpaṃ, link to arūpesu (^5-526)
    ("lối thoát khỏi vật chất là phi vật chất", "lối thoát khỏi vật chất là cõi không hình sắc", 3, "minor", S),
    # minor + B3: MN 136 sañcetaniyaṃ kammaṃ katvā kāyena vācāya manasā …vedaniyaṃ (^5-539)
    (r"sau khi làm nghiệp có chủ ý, được cảm nhận là ([^,]+), bằng thân, bằng lời nói, bằng ý, người ấy",
     r"sau khi bằng thân, bằng lời nói, bằng ý tạo một nghiệp có chủ ý đưa đến cảm nhận \1, người ấy", 3, "minor+B3", X),
    # B3 kammaṃ karoti (^5-539, AN 6.63)
    ("làm nghiệp", "tạo nghiệp", 1, "B3", S),
    # B7 Handa hi answering «Do nghiệp nào …?» (^5-546)
    ("Do nghiệp nào làm nguyên nhân? Này, vì người ấy", "Do nghiệp nào làm nguyên nhân? Bởi vì người ấy", 1, "B7", S),
],
"17-navamavaggo": [
    # minor: vitakkavipphāro saddo in one form (^5-563, uddāna ^5-570)
    (r"thì sự lan tỏa của ((?:sự )?[^,;”?]+?) là âm thanh", r"thì có âm thanh lan tỏa của \1", 11, "minor", X),
    # minor: note kathā. 484 passitabbaṃ (^5-564)
    ("; Các vấn đề tranh luận 484, cần xem]", "; xem Các vấn đề tranh luận 484]", 1, "minor", S),
],
"18-dasamavaggo": [
    # minor: apubbaṃ acarimaṃ (^5-576, 580, 584)
    ("không sinh khởi không trước không sau", "không sinh khởi cùng một lúc, không trước không sau", 3, "minor", S),
    # minor: sataṃ dhammo asabbhi ārakā (^5-599, 603)
    ("bản chất của người hiền thiện ở xa kẻ không hiền thiện", "giáo pháp của người hiền thiện ở xa kẻ không hiền thiện", 2, "minor", S),
    # B16 uddāna: items contain commas, so semicolons between items (^5-604)
    ("Khi năm khối tìm cầu sự tái sinh chưa chấm dứt, năm khối mang tính chức năng sinh khởi, vật chất của người có được con đường là con đường, người có được năm loại thức có sự tu tập con đường, năm loại thức vừa là thiện vừa là bất thiện, năm loại thức có sự chú hướng, người có được con đường được trang bị hai giới hạnh, giới hạnh không phải là yếu tố đồng hành với tâm, giới hạnh không vận hành theo tâm, giới hạnh có nguyên nhân từ sự thọ trì tăng trưởng, sự biểu lộ là giới hạnh, sự không biểu lộ là sự phạm giới.",
     "Khi năm khối tìm cầu sự tái sinh chưa chấm dứt, năm khối mang tính chức năng sinh khởi; vật chất của người có được con đường là con đường; người có được năm loại thức có sự tu tập con đường; năm loại thức vừa là thiện vừa là bất thiện; năm loại thức có sự chú hướng; người có được con đường được trang bị hai giới hạnh; giới hạnh không phải là yếu tố đồng hành với tâm; giới hạnh không vận hành theo tâm; giới hạnh có nguyên nhân từ sự thọ trì tăng trưởng; sự biểu lộ là giới hạnh, sự không biểu lộ là sự phạm giới.",
     1, "B16", S),
],
"19-ekadasamavaggo": [
    # minor: note sakavādīpucchā viya dissati (^5-617)
    ("[thấy như là câu hỏi của người theo học thuyết của chúng ta]", "[có vẻ là câu hỏi của người theo học thuyết của chúng ta]", 1, "minor", S),
    # minor: the syllables (^5-620)
    ("Có phải hiểu biết “i” [khác chính tả (Syā., Pī.): īti] và “đam” và “đu” [khác chính tả (Syā., Pī.): dūti] và “kham” khởi lên không?",
     "Có phải hiểu biết về từng âm “i” [khác chính tả (Syā., Pī.): īti], “đam”, “đu” [khác chính tả (Syā., Pī.): dūti], “kham” khởi lên không?", 1, "minor", S),
    # A19 bare samāpanno, jhāna context (^5-626)
    ("là người đang nhập không?", "là người đang nhập thiền không?", 2, "A19", S),
],
"20-dvadasamavaggo": [
    # minor: brahmassaro (^5-637 segment)
    ("có giọng nói trong sạch", "có giọng nói như Phạm thiên", 1, "minor", S),
    # A2 assa (^5-650, 651)
    ("ngựa đực và ngựa cái", "ngựa và ngựa cái", 2, "A2", S),
    # B16 uddāna (^5-653): items contain commas, so semicolons between items
    ("Sự thu thúc là nghiệp, cũng vậy với sự không thu thúc, tất cả nghiệp đều có quả trổ, âm thanh là quả, sáu lĩnh vực nhận biết là quả, người tái sinh tối đa bảy lần được cố định vào trạng thái tái sinh tối đa bảy lần, người đi từ gia đình này sang gia đình khác được cố định vào trạng thái đi từ gia đình này sang gia đình khác, người có một hạt giống được cố định vào trạng thái có một hạt giống, người thành tựu về quan điểm có thể cố ý tước đoạt mạng sống của sinh vật, đối với người thành tựu về quan điểm, cõi xấu đã được dứt bỏ, cũng vậy với người ở lần hiện hữu thứ bảy.",
     "Sự thu thúc là nghiệp; cũng vậy với sự không thu thúc; tất cả nghiệp đều có quả trổ; âm thanh là quả; sáu lĩnh vực nhận biết là quả; người tái sinh tối đa bảy lần được cố định vào trạng thái tái sinh tối đa bảy lần; người đi từ gia đình này sang gia đình khác được cố định vào trạng thái đi từ gia đình này sang gia đình khác; người có một hạt giống được cố định vào trạng thái có một hạt giống; người thành tựu về quan điểm có thể cố ý tước đoạt mạng sống của sinh vật; đối với người thành tựu về quan điểm, cõi xấu đã được dứt bỏ; cũng vậy với người ở lần hiện hữu thứ bảy.",
     1, "B16", S),
],
"21-terasamavaggo": [
    # B14 kappaṭṭha / kappaṭṭhiya (heading, theses, verse ^5-657, close, uddāna ^5-685)
    ("tồn tại suốt một kiếp", "lưu lại suốt một kiếp", 31, "B14", S),
    # B3 kappaṭṭhiyaṃ kammaṃ karoti (^5-654)
    ("làm nghiệp", "tạo nghiệp", 1, "B3", S),
    # minor: tato vuṭṭhānaṃ (^5-659)
    ("tâm thiện của sự xuất khỏi từ đó", "tâm thiện để thoát ra khỏi tình trạng đó", 1, "minor", S),
    # A12 anantarāpayutta / payuttaṃ / payutto āsi (heading, ^5-660-662, uddāna ^5-685)
    ("tiến hành", "khởi xướng", 16, "A12", S),
    # minor: bhabbo … nābhisametuṃ (^5-664)
    ("Bồ-tát có khả năng không thấu hiểu", "Bồ-tát có thể không thấu hiểu", 1, "minor", S),
    # minor: nivuto nīvaraṇaṃ jahati (heading, ^5-665-667, uddāna)
    ("người bị ngăn che", "người bị các chướng ngại che lấp", 8, "minor", S),
    # minor: sammukhībhūto saṃyojanaṃ jahati (heading, ^5-668-670, uddāna)
    ("người đang hiện diện đối mặt", "người đang đối diện với các xiềng xích", 8, "minor", S),
    # minor: sataṃ dhammo asabbhi ārakā (^5-666, 669, 672)
    ("bản chất của người hiền thiện ở xa kẻ không hiền thiện", "giáo pháp của người hiền thiện ở xa kẻ không hiền thiện", 3, "minor", S),
    # A19 samāpanno assādeti (heading, ^5-671-673)
    ("người đang nhập thành tựu thiền", "người đang nhập thiền", 5, "A19", S),
    # B14 ajjhosāya tiṭṭhanti / tiṭṭhati (^5-674, 675)
    ("kéo dài sự bám chặt vào", "cứ bám chặt vào", 3, "B14", S),
    ("duy trì sự bám chặt vào nó", "cứ bám chặt vào nó", 1, "B14", S),
],
"22-cuddasamavaggo": [
    # minor: apubbaṃ acarimaṃ (^5-692 segment)
    ("Có phải không trước không sau, sáu lĩnh vực", "Có phải cùng một lúc, không trước không sau, sáu lĩnh vực", 1, "minor", S),
    # B3 kammaṃ karoti (^5-692)
    ("làm nghiệp", "tạo nghiệp", 3, "B3", S),
    # minor: stray opening quote before "Yañcassa (^5-692)
    ("tóc, lông và cả móng.\n“Và cái gì mà mẹ", "tóc, lông và cả móng.\nVà cái gì mà mẹ", 1, "minor", S),
    # B10 missing «?» (^5-693, ^5-704)
    ("sinh khởi nơi người mong cầu sao, đúng vậy.", "sinh khởi nơi người mong cầu sao? Đúng vậy.", 1, "B10", S),
    ("“nằm trong cõi không hình sắc” không, không nên nói như vậy…", "“nằm trong cõi không hình sắc” không? Không nên nói như vậy…", 1, "B10", S),
    # minor: micchādiṭṭhiparamāni vajjāni (^5-707)
    ("đã nói đến các lỗi có quan điểm sai lầm đứng đầu", "đã nói rằng trong các lỗi lầm, quan điểm sai lầm là nặng nhất", 2, "minor", S),
    # A13 apariyāpanna (heading, ^5-709, close, uddāna ^5-710)
    (r"điều không nằm trong(?! các cõi)", "điều không nằm trong các cõi tồn tại", 6, "A13", X),
],
}

FORBIDDEN_GROW = ["—", ":-", "….", ".…", "được được", "là là", "các các", "chánh niệm", "seed", "  "]


def seg_id_at(text, pos):
    m = re.compile(r"\^([0-9a-z-]+)[ \t]*(?:\n|$)").search(text, pos)
    return m.group(1) if m else "?"


def main():
    os.makedirs(BACKUP, exist_ok=True)
    log = []
    total = 0
    for ch, rules in RULES.items():
        src = CHDIR + "\\" + ch + ".md"
        bak = BACKUP + "\\" + ch + ".md"
        if not os.path.exists(bak):
            shutil.copyfile(src, bak)
        with open(bak, encoding="utf-8", newline="") as f:
            orig = f.read()
        assert "\r" not in orig
        text = orig
        for old, new, n, dec, isrx in rules:
            rx = re.compile(old if isrx else re.escape(old))
            hits = list(rx.finditer(text))
            if DRY:
                print("%s\t%s\t%d (expected %d)" % (ch, dec, len(hits), n))
            else:
                assert len(hits) == n, (ch, old, len(hits), n)
            for m in hits:
                rep = m.expand(new) if isrx else new
                log.append((ch + ".md", seg_id_at(text, m.end()), m.group(0).replace("\n", "\\n"), rep.replace("\n", "\\n"), dec))
            text = rx.sub(new if isrx else new.replace("\\", "\\\\"), text)
            total += len(hits)
        assert unicodedata.normalize("NFC", text) == text
        for s in FORBIDDEN_GROW:
            assert text.count(s) <= orig.count(s), (ch, s)
        # the replaced strings must be gone
        for old, new, n, dec, isrx in rules:
            if not isrx and old not in new:
                assert old not in text, (ch, old)
        if not DRY:
            with open(src, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
    if not DRY:
        with open(LOG, "w", encoding="utf-8", newline="\n") as f:
            f.write("file\tblock_id\told\tnew\tdecision\n")
            for row in log:
                f.write("\t".join(row) + "\n")
    print("replacements:", total)


main()
