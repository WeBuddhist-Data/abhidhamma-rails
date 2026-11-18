# Notes for part 2-03 (Vietnamese plain zero-shot, Lokuttarakusalaṃ, ^1-1-5-0 … ^1-364): new recurring terms and formulas

Builder: build_2-03_vi.py (imports build_matika_vi, build_ch2_01_sample_vi and build_2-01_2-02_vi unchanged; adds entries to
the 2-01/2-02 tables in memory only, never overwriting one; all other lines go through the 2-01/2-02 line translator).
`python -I -X utf8 build_2-03_vi.py` checks the 32 headings against vi-zeroshot-terms.md and asserts that the 29 Pāli
lines that also occur in 2-01/2-02 get the published Vietnamese byte for byte. Checks: verify_vi_2-03.py. 96 segments.
Reusable pieces (import with importlib, the name has hyphens): NEW_NAMES, TOKENS, compose(), ABST(), G_ANANNATA, G_ANNA,
LEADS, STAGE, TWENTY_V, SUNNATA_Q, APPANIHITA_Q, translate_line().

## Headings and closing lines (headings verbatim from vi-zeroshot-terms.md)
Lokuttarakusalaṃ = Tâm thiện vượt thế gian
Suddhikapaṭipadā = Cách thực hành đơn thuần
Suññataṃ = Sự trống rỗng
Suññatamūlakapaṭipadā = Cách thực hành dựa trên sự trống rỗng
Appaṇihitaṃ = Sự không mong cầu
Appaṇihitamūlakapaṭipadā = Cách thực hành dựa trên sự không mong cầu
Vīsati mahānayā = Hai mươi phương pháp lớn
Adhipati = Yếu tố chủ đạo
Paṭhamo / Dutiyo / Tatiyo / Catuttho maggo. = Con đường thứ nhất. / Con đường thứ hai. / Con đường thứ ba. / Con đường thứ tư.
Lokuttaraṃ cittaṃ. = Tâm vượt thế gian.

## Names
anaññātaññassāmītindriyaṃ = năng lực biết được điều chưa từng biết
aññindriyaṃ = năng lực hiểu biết trọn vẹn
sammāvācā = lời nói đúng đắn
sammākammanto = hành động đúng đắn
sammāājīvo = sinh kế đúng đắn (ājīva = sinh kế; micchāājīva = sinh kế sai lầm)
navindriyāni = chín năng lực
aṭṭhaṅgiko maggo = con đường gồm tám chi phần

## String pieces (appended to the earlier strings with ", ")
maggaṅgaṃ maggapariyāpannaṃ = chi phần của con đường, thuộc về con đường
X-sambojjhaṅgo = chi phần giác ngộ là X (bojjhaṅga = chi phần giác ngộ): pīti = sự hân hoan, samādhi = định tâm, vīriya = sự tinh tấn, sati = sự tỉnh thức, dhammavicaya = sự tìm hiểu các hiện tượng, passaddhi = sự an tịnh
<obj> ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto = sự tránh xa <obj>, sự kiêng tránh, sự kiêng tránh hoàn toàn, sự kiềm chế, sự không làm, sự không thực hiện, sự không rơi vào lỗi vi phạm, sự không vượt quá giới hạn, sự phá bỏ cây cầu
catūhi vacīduccaritehi = bốn loại hành vi xấu bằng lời nói (duccarita = hành vi xấu)
tīhi kāyaduccaritehi = ba loại hành vi xấu bằng thân
micchāājīvā = sinh kế sai lầm
Yā tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya S – idaṃ tasmiṃ samaye X hoti. = Điều nhằm tự mình chứng nghiệm những hiện tượng ấy, vốn chưa được biết, chưa được thấy, chưa được đạt đến, chưa được nhận biết, chưa được tự mình chứng nghiệm, tức là S – đây là X vào lúc ấy.  (frame like jīvitindriya)
tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya = nhằm tự mình chứng nghiệm những hiện tượng ấy, vốn đã được biết, đã được thấy, đã được đạt đến, đã được nhận biết, đã được tự mình chứng nghiệm
sacchikiriyā = tự mình chứng nghiệm (sacchikata = được tự mình chứng nghiệm)

## Opening sentences
Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti = Vào lúc một người tu tập tầng thiền vượt thế gian
niyyānikaṃ apacayagāmiṃ = dẫn đến giải thoát và dẫn đến sự giảm trừ (matrix ^1-M2-97 (a), ^1-M1-10 (b))
diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā = nhằm dứt bỏ sự mắc kẹt trong các quan điểm, để đạt đến giai đoạn thứ nhất (diṭṭhigata = sự mắc kẹt trong các quan điểm; bhūmi = giai đoạn)
kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā = nhằm làm suy yếu sự tham đắm dục lạc và ác ý, để đạt đến giai đoạn thứ hai
kāmarāgabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā = nhằm dứt bỏ không còn sót lại sự tham đắm dục lạc và ác ý, để đạt đến giai đoạn thứ ba
rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā = nhằm dứt bỏ không còn sót lại sự tham đắm cõi hình sắc, sự tham đắm cõi không hình sắc, sự kiêu mạn, sự xao động và vô minh, để đạt đến giai đoạn thứ tư
rāga = sự tham đắm (kāmarāga = sự tham đắm dục lạc; kept apart from lobha = tham lam and sārāga = say đắm); byāpāda = ác ý; uddhacca = sự xao động; anavasesappahāna = dứt bỏ không còn sót lại; tanubhāva = làm suy yếu
suññataṃ (qualifying the absorption) = với tính chất trống rỗng
appaṇihitaṃ (qualifying the absorption) = với tính chất không mong cầu
lokuttaraṃ X bhāveti…pe… (the twenty methods) = tu tập X vượt thế gian… : maggaṃ = con đường, satipaṭṭhānaṃ = sự thiết lập tỉnh thức, sammappadhānaṃ = nỗ lực đúng đắn, iddhipādaṃ = nền tảng thần thông, indriyaṃ = năng lực, balaṃ = sức mạnh, bojjhaṅgaṃ = chi phần giác ngộ, saccaṃ = sự thật, samathaṃ = sự tĩnh lặng, dhammaṃ = hiện tượng, khandhaṃ = khối, āyatanaṃ = lĩnh vực nhận biết, dhātuṃ = yếu tố, āhāraṃ = dưỡng chất, phassaṃ = sự tiếp xúc, vedanaṃ = cảm giác, saññaṃ = tri giác, cetanaṃ = chủ ý, cittaṃ = tâm
(everything after the intro, …pe… forms, practice modes, dominant factors, Koṭṭhāsa summary, saṅkhārakkhandha list: the 2-01/2-02 formulas, unchanged)

## Choices to review
sammappadhāna = «nỗ lực đúng đắn» (padhāna = nỗ lực, binding); it coincides with sammāvāyāma = «nỗ lực đúng đắn». They never stand in one line here. To split them, change TWENTY_V[2].
iddhipāda = «nền tảng thần thông» (iddhi read as spiritual power, as the English «basis of spiritual power»).
setughāto = «sự phá bỏ cây cầu» (literal); velāanatikkamo = «sự không vượt quá giới hạn»; anajjhāpatti = «sự không rơi vào lỗi vi phạm» (āpatti = lỗi vi phạm, matrix ^1-M2-119).

## Source points translated as written
^1-364: «maggapariyāpannaṃ, idaṃ tasmiṃ samaye aññindriyaṃ hoti» has a comma where every other answer has « – »; the comma is kept (dash rule).
^1-314: the answer for amoho has no «amoho kusalamūlaṃ» (unlike ^1-34); nothing added.
^1-342, ^1-359: stray space before «…pe…» («vūpasamā …pe…», «paṭhamaṃ jhānaṃ …pe…»); spacing mirrored, as in 2-02.
^1-337, ^1-363: «kusalā…pe….» = «… đây là các hiện tượng thiện….» (as 2-02).
^1-342, 344, 349, 351, 356, 359: fivefold absorption sequence «dutiyaṃ… tatiyaṃ… catutthaṃ… paṭhamaṃ… pañcamaṃ» (the same order as the fivefold lines of 2-02); as written.
