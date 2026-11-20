# pi-2 Vietnamese keyword map, part 17-khuddakavatthuvibhango: new recurring decisions

Script: map_17_vi.py (T17 table, PRIO = same Pāli with the segment's own Vietnamese, context17() rules, OVERRIDES; reuses T16 / T1315 / T1012 / T79 / T45 and context() of map_16_vi.py). Base: pi-1 vi-map-conventions.md, vi-map-conventions-pi2.md, notes-map-2-3.md … notes-map-16.md; zero-shot notes-17.md. One "pāli = tiếng Việt (context)" per line. Helpers in the script: `show PART lo hi [all] [pali]`, `dump PART [miss|fallback]`.

## Headings and names
Khuddaka = nhỏ, vatthu = chủ đề («Phân tích các chủ đề nhỏ»); vatthu = chỗ dựa in kusītavatthu (^2-953)
mado = sự say sưa; X-mado = sự say sưa vì X; majjanā / majjitattaṃ = sự khởi say sưa / trạng thái khởi say sưa; Jātiṃ paṭicca = dựa vào xuất thân (^2-921 dựa vào sự sinh)
jāti / jātiṃ / jātiyā = xuất thân (mada, māna) / sự sinh (bhaya); the 27 mada grounds and the 12 māna grounds as notes-17.md (vaṇṇa = sắc đẹp / vẻ đẹp (vaṇṇapokkharatāya) / lời khen (macchariya); suta = sự học hỏi / đã nghe (anariyavohāra); bhoga = của cải / tài sản (byasana))
ādī / ādīni / ādi = những điều tương tự (X-ādī = X và những điều tương tự)
icchatā (member) = tham muốn (atricchatā, mahicchatā) / ước muốn (pāpicchatā); icchā = sự mong muốn / ước muốn (icchāpakata)
māno = sự kiêu mạn; where the segment has no «sự kiêu mạn»: sự ngạo mạn (atimāno heading) / sự tự ti (omāna string); ātimāno (of mānātimāno) = chồng chất; mānā = loại kiêu mạn, kiêu mạn after navavidhā («chín loại kiêu mạn»)
seyyo- / sadiso- / hīnohamasmī(ti) = Tôi hơn người / Tôi bằng người / Tôi kém người (quotes dropped); seyyassa / sadisassa / hīnassa = của người vốn hơn / bằng / kém người; sadiso / sadisaṃ = bằng, hīno = kém
ānudiṭṭhi = quan điểm về (pubbantā- / aparantānudiṭṭhi) / quan điểm xem (attānudiṭṭhi «quan điểm xem có tự ngã»)
vibhava = sự không hiện hữu (vibhavadiṭṭhi «quan điểm về sự không hiện hữu») / không còn hiện hữu (vibhavataṇhā); vibhavaṃ = sự không còn hiện hữu
pāpa = người xấu (pāpamittatā, pi-1); Māyā = sự xảo trá (ch17 list) / sự huyễn hoặc (lobha list, pi-1)
āyatanāni = lĩnh vực (titthāyatanāni «lĩnh vực của các học thuyết ngoại đạo»); uppādā = nguyên nhân khởi lên (taṇhuppādā); ānantarikāni = trổ quả ngay kiếp kế tiếp; vādā = học thuyết (nói in musāvādā); paṭighāto = sự va chạm (lokadhammesu) / sự phẫn uất (dosa string); purisa = con người
vicarita / vicaritāni = dòng (taṇhāvicarita = dòng khao khát); gatāni (dvāsaṭṭhi diṭṭhigatāni «sáu mươi hai quan điểm») = (no direct equivalent)
Dasavatthukā = có mười chủ đề, vatthukā = có … chủ đề; antaggāhikā = chấp giữ cực đoan

## Definitions
pamāda / kosajja body: vossaggo = sự buông lơi (not ch10 «sự buông xả»), cittassa vossaggo = sự buông lơi của tâm, ānuppadānaṃ = sự tiếp tục để mặc, vuttitā = sự hành xử, anaṭṭhita = có ngừng nghỉ
pi-1 fragment words that stand here as full items keep «sự»: jimhatā / vaṅkatā / kuṭilatā = sự quanh co / sự cong queo / sự vặn vẹo, kakkhaḷatā = sự thô cứng, pilāpanatā = sự hời hợt, sammusanatā = sự quên lãng; davāya / madāya / maṇḍanāya / vibhūsanāya / saṃvarāya = để vui đùa / để say sưa / để trang điểm / để làm đẹp / để thu thúc (pi-1)
sampaggāho = sự tự đề cao (māna string, pi-1); thambhanā / thambhitattaṃ = sự khởi cứng đầu / trạng thái khởi cứng đầu (thambha) / trạng thái cứng đờ (vicikicchā); unnāmo = sự vênh vang
Lābhasakkārasilokasannissitassa / -sannissito = người bám vào lợi lộc sự tôn vinh và tiếng tăm (comma dropped); sannissita = bám vào; pakata = chi phối
ṭhapanā / saṇṭhapanā = sự bày đặt / sự dàn dựng (kuhanā) / sự giữ lại / sự giữ chặt (upanāha); nimittaṃ / obhāso = sự ra dấu / sự gợi ý (nemittikatā); jappā = lời nói in sāmantajappā (sự thèm thuồng in the lobha list)
gehasito / gehasitā / gehasitāni / gehasitaṃ = gắn với đời sống thế tục; gehasitaṃ cetasikaṃ (asātaṃ / sātaṃ) = gắn với đời sống thế tục … trạng thái trong tâm / sự bứt rứt trong tâm / sự khoan khoái trong tâm
dhamma / dhammaṃ / dhammesu = đối tượng của ý where the segment is about the six objects (dhammataṇhā, manasā dhammaṃ viññāya, manāpiyesu dhammesu: rule + overrides ^2-905, 2-909, 2-947, 2-U24, 2-U60); Giáo Pháp in macchariya / paṭisanthāra / assaddhiya; hiện tượng elsewhere
Kāmadhātu = yếu tố dục lạc (^2-912) / cõi dục lạc (taṇhā); dhātu = yếu tố / cõi likewise
X-kammaṃ (kāya / vacī / mano) = nghiệp … bằng thân / lời nói / ý («nghiệp bất thiện bằng thân»); akusalaṃ kāyakammaṃ = nghiệp bất thiện bằng thân
sato = đang hiện hữu (sato sattassa); sati = khi có (tasmiṃ sati, ^2-974/976) / tỉnh thức (micchāsati); paṭilabhati = có được; bho = thưa ngài
hoti = còn tồn tại where «Như Lai (không) còn tồn tại» (^2-919, 2-972, 2-U34, as ch16 ^2-815); (no direct equivalent) in ^2-951 (copula)
vihiṃsā = sự hãm hại / hãm hại (yếu tố hãm hại); rāga / paṭigha / māna / vicikicchā / issā / parāmāsa as compound stems = tham đắm / ác cảm / kiêu mạn / hoài nghi / ganh tị / hiểu sai lệch (no «sự»)
sevanā / nisevanā / saṃsevanā = sự giao du … / sự đi theo … (kummaggasevanā); sampavaṅkatā = sự nghiêng theo (^2-901 slip, as written) / sự nghiêng về phía
saññīnāsaññī (fragment of nevasaññīnāsaññī) = có tri giác cũng không phải không có tri giác; nāsaññī = không phải không có tri giác
taṇhāvicarita (^2-973 … 976): asasmīti = Tôi thường còn, sātasmīti = Tôi đoạn diệt, aññathāsmīti = Tôi khác đi; (an)avakāriṃ = (không) tách riêng; khattiyo … manusso = người thuộc giai cấp quý tộc … con người; Parapuggalaṃ upanidhāya = người khác / so với
dukkhā (^2-943 kāmā … dukkhā) = khổ đau (override); doso (^2-957 purisadoso) = lỗi; doso (^2-925 «không có lỗi gì») = lỗi

## Source slips (as the Vietnamese says)
^2-901 sampavaṅkatā = sự nghiêng theo; ^2-904 kaṇḍakā = gai góc; ^2-933 bhavantattaṃ = trạng thái rối loạn (as meant, bhantattaṃ); ^2-948 nāhosi = không phải trước đây không có, bhavissati (na bhavissati) not a keyword there; ^2-957 codiyamāno = bị … buộc tội; ^2-U21 paṭisevanā = sự lui tới

## (no direct equivalent)
gatāni ^2-842, ^2-977 (diṭṭhigatāni = «quan điểm»); gata ^2-887 (diṭṭhigatapaṭisaṃyutto «liên quan đến các quan điểm»); hoti ^2-951

## Presence-check exceptions
None.

## Unclear
nijigīsanatā = sự … tìm kiếm (lābhena lābhaṃ nijigīsanatā «sự dùng lợi lộc để tìm kiếm lợi lộc»; the nominaliser sits at the head of the phrase)
gilāna / paccaya / bhesajja = chữa bệnh / vật dụng / thuốc men («thuốc men và vật dụng chữa bệnh»: the Vietnamese regroups the compound)
yogaṃ / āpajjati = dấn thân / dấn thân vào (^2-888 «tự mình dấn thân vào»: one Vietnamese verb phrase)
mahābhūtiko / bhūtiko = yếu tố cơ bản / yếu tố («gồm bốn yếu tố cơ bản»; cātu has no keyword)
gataṃ (diṭṭhigataṃ) = sự mắc kẹt trong
