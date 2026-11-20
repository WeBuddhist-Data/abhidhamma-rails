# pi-2 Vietnamese zero-shot, chapters 7 (Satipaṭṭhāna), 8 (Sammappadhāna), 9 (Iddhipāda): new terms and formulas

Builder: build_7-9_vi.py (imports build_ch1_sample_vi as S, build_1_vi as B, build_2-3_vi as T, build_4-5_vi as F, build_6_vi as G; T's item tables extended in memory only; writes only the three ch. 7-9 files). pi-1 strings asserted at build time: ^1-1377 (four efforts), ^1-985 / ^1-986 (roots, defilements, aggregates, action), ^1-277 via ch4 (supramundane jhāna), ^1-505 via ch6 (Tasseva … suññataṃ), ^1-303 (sati with bojjhaṅga), ^1-269 (chanda / vīriya / citta / vīmaṃsā), ^1-1158 (hindrances), awakening-factor names. Clause-level parsers; unknown Pāli raises KeyError. Scratch lookup: probe_7-9_vi.py.
Format: Pāli = tiếng Việt, one per line. [pi-1] = pi-1 Vietnamese rails; [ch1-6] = earlier pi-2 builders; [new] = settled here.

## Reused
satipaṭṭhāna = sự thiết lập tỉnh thức; sammappadhāna = nỗ lực đúng đắn; iddhipāda = nền tảng thần thông [pi-1]
kāye kāyānupassī viharati = đối với thân, sống quán sát thân (vedanāsu … các cảm giác; citte … tâm; dhammesu … các hiện tượng) [ch4 MINDFUL]
ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ = nhiệt tâm, hiểu biết rõ ràng, có sự tỉnh thức, sau khi chế ngự sự thèm muốn và nỗi buồn đối với thế gian [ch4]
chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati = khởi lên ý muốn, nỗ lực, khởi động tinh tấn, nâng tâm lên, ra sức nỗ lực (+ the four purposes) [pi-1 ^1-1377]
Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti … dandhābhiññaṃ = Ở đời này, vào lúc vị tỳ-khưu tu tập tầng thiền vượt thế gian … chậm chạp, [pi-1 ^1-277 via ch4]
Tasseva lokuttarassa … suññataṃ = Còn khi một người … có tính chất trống rỗng, là quả của chính tầng thiền thiện vượt thế gian ấy đã được tạo và tu tập [pi-1 ^1-505, as ch6; «một người» kept: identical Pāli]
Tīṇi akusalamūlāni – lobho, doso, moho / tadekaṭṭhā ca kilesā / taṃsampayutto … / taṃsamuṭṭhānaṃ … = Ba gốc rễ bất thiện – sự tham lam, sự sân hận, sự si mê / và các phiền não cùng hiện diện với chúng / khối cảm giác, khối tri giác, khối tạo tác và khối thức gắn liền với chúng / nghiệp bằng thân, nghiệp bằng lời nói, nghiệp bằng ý do chúng sinh ra [pi-1 ^1-986, ^1-985]
pāpakā akusalā dhammā = các hiện tượng xấu ác bất thiện [pi-1]
sati / vīriya / samādhi / paññā bodies (plain and with …sambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ) = pi-1 ^1-13 … ^1-16, ^1-287 … ^1-303 via F [ch4-5]; vīriya full list in ^2-433 = F.VIRIYA + «, nỗ lực đúng đắn» (pi-2 has sammāvāyāmo here)
sati anussati sammāsati satisambojjhaṅgo … = sự tỉnh thức, sự nhớ lại, tỉnh thức đúng đắn, chi phần giác ngộ là sự tỉnh thức, chi phần của con đường, nằm trong con đường [pi-1 ^1-303 items]
Yo rāgo sārāgo…pe… cittassa sārāgo; Yaṃ cetasikaṃ asātaṃ …; Yaṃ cittaṃ mano mānasaṃ…pe… tajjāmanoviññāṇadhātu [ch6 strings]
kesā lomā … mutta = tóc, lông, … phân, mật, đờm, … nước tiểu [ch3 lists, asserted same Pāli]
kāmacchanda / byāpāda / thinamiddha / uddhaccakukkucca / vicikicchā = ý muốn dục lạc / ác ý / sự uể oải và đờ đẫn / sự xao động và hối tiếc / sự hoài nghi [pi-1 ^1-1158]
Xsambojjhaṅga = chi phần giác ngộ là sự tỉnh thức / sự tìm hiểu các hiện tượng / sự tinh tấn / sự hân hoan / sự an tịnh / định tâm / sự bình thản [pi-1; upekkhā one by pattern, pi-1 upekkhā «sự bình thản»]
chanda / vīriya / citta / vīmaṃsā = ý muốn / tinh tấn / tâm / sự thẩm xét [pi-1 ^1-269 «lấy … làm yếu tố chủ đạo»]; cittassekaggatā = sự nhất tâm; paggāho = sự dốc sức [pi-1]
vāyāmo / padhānaṃ = sự nỗ lực (both, pi-1 termbase); vīriyaṃ = sự tinh tấn [pi-1]
Tena vuccati "X"ti = Vì thế nên mới nói rằng “X” [ch6]; lemma Xti = “X”. [ch6]
Avasesā dhammā Xsampayuttā = Các hiện tượng còn lại gắn liền với X [ch4]

## Satipaṭṭhāna (ch. 7)
ajjhattaṃ / bahiddhā / ajjhattabahiddhā kāye kāyānupassī viharati = đối với thân ở nơi bản thân / ở bên ngoài bản thân / ở nơi bản thân và ở bên ngoài bản thân, sống quán sát thân [new; B items]
… dandhābhiññaṃ kāye kāyānupassī (Abhidhamma, no viharati) = …, đối với thân, quán sát thân, [new]
yā / yo / yaṃ tasmiṃ samaye X (after the jhāna frame) = thì điều mà vào lúc ấy là X [new; pi-1 «Điều mà vào lúc ấy là»]
Kathañca bhikkhu …? = Và vị tỳ-khưu … như thế nào? [new]
Kāyānupassanāniddeso / Vedanā- / Cittā- / Dhammā- = Giải thích sự quán sát thân / các cảm giác / tâm / các hiện tượng (also the closing lines) [new; ch6 «Giải thích …»]
anupassī / anupassanā = quán sát / sự quán sát; viharati = sống [new]
Iriyati vattati pāleti yapeti yāpeti carati viharati = Vị ấy vận động, tiến triển, gìn giữ, tiếp diễn, kéo dài, đi lại, sống [new; pi-1 ^1-19 words]
ātāpī / ātāpo = nhiệt tâm / sự nhiệt tâm [ch4 / new]; sampajāno / sampajaññaṃ = hiểu biết rõ ràng / sự hiểu biết rõ ràng [pi-1]; satimā = có sự tỉnh thức [ch4]
Imāya X-āya upeto hoti samupeto upāgato samupāgato upapanno sampanno samannāgato = Với X này, vị ấy là người có được, có được trọn vẹn, đã tiếp cận, đã tiếp cận trọn vẹn, đã đạt đến, đã thành tựu, được trang bị [new]; …upeto hoti…pe… samannāgato = … là người có được… được trang bị
uddhaṃ pādatalā adho kesamatthakā tacapariyantaṃ pūraṃ nānappakārassa asucino paccavekkhati = quán xét …, từ lòng bàn chân trở lên, từ đỉnh tóc trở xuống, được bao bọc bởi da, chứa đầy nhiều loại bất tịnh [new]
atthi imasmiṃ kāye / atthissa kāye = Trong thân này có / Trong thân của người ấy có [new]
So taṃ nimittaṃ āsevati bhāveti bahulīkaroti svāvatthitaṃ vavatthapeti = Vị ấy thực hành dấu hiệu ấy, tu tập, làm đi làm lại, xác định cho thật rõ ràng [new; pi-1 āsevanā bhāvanā bahulīkamma, nimitta]
… āsevitvā … vavatthapetvā X cittaṃ upasaṃharati = Sau khi thực hành dấu hiệu ấy, …, vị ấy đưa tâm đến X [new; «đưa tâm», not «hướng tâm» = vitakka]
Evaṃ bhikkhu … = Như vậy, vị tỳ-khưu, … [new]
pajānāti = hiểu rõ (rằng “…”) [new; pi-1 pajānanā «sự hiểu rõ»]
sukhaṃ vedanaṃ vedayamāno "… vedayāmī"ti = khi cảm nhận cảm giác dễ chịu, hiểu rõ rằng “Tôi đang cảm nhận cảm giác dễ chịu” [new]
… vedayamānaṃ "… vedayatī"ti = đối với người đang cảm nhận …, hiểu rõ rằng “Người ấy đang cảm nhận …” [new]
sukhaṃ vedanaṃ "sukhā vedanā"ti pajānāti = hiểu rõ cảm giác dễ chịu là “cảm giác dễ chịu” [new]
sāmisa / nirāmisa = có tính trần tục / không có tính trần tục [new]; vā = hoặc (on every item that has it)
sarāgaṃ vā cittaṃ "sarāgaṃ me citta"nti = hoặc đối với tâm có tham đắm, hiểu rõ rằng “Tâm tôi có tham đắm” (vāssa … "…massa citta": … của người ấy / “Tâm của người ấy …”; "…ṃ citta": hoặc hiểu rõ tâm … là “tâm …”) [new]
sarāga / vītarāga, sadosa / vītadosa, samoha / vītamoha = có tham đắm / đã lìa tham đắm, có sân hận / đã lìa sân hận, có si mê / đã lìa si mê [new]
saṃkhitta / vikkhitta = co rút / tán loạn; mahaggata / amahaggata = rộng lớn / không rộng lớn; sauttara / anuttara = còn có điều cao hơn / không có điều gì cao hơn; samāhita / asamāhita = được định tâm / không được định tâm; vimutta / avimutta = được giải thoát / không được giải thoát [new; pi-1 matrix words]
santaṃ vā ajjhattaṃ X "atthi me ajjhattaṃ X"ti pajānāti = hoặc khi ở nơi bản thân có X, hiểu rõ rằng “Ở nơi bản thân tôi có X” (asantaṃ: không có; vāssa: khi người ấy có X / “Người ấy có X”; both: khi có X / “Có X”) [new]
yathā ca anuppannassa X uppādo hoti tañca pajānāti = cũng hiểu rõ X chưa sinh khởi nảy sinh như thế nào [new]
yathā ca uppannassa X pahānaṃ hoti … = cũng hiểu rõ X đã sinh khởi được dứt bỏ như thế nào [new]
yathā ca pahīnassa X āyatiṃ anuppādo hoti … = cũng hiểu rõ X đã được dứt bỏ không nảy sinh trở lại trong tương lai như thế nào [new]
yathā ca uppannassa X bhāvanāya pāripūrī hoti … = cũng hiểu rõ X đã sinh khởi được tu tập đến chỗ hoàn thiện như thế nào [new]
loko = thế gian; abhijjhā = sự thèm muốn; domanassaṃ = nỗi buồn [ch4 / pi-1]
Sveva kāyo / Sāyeva vedanā / Taṃyeva cittaṃ / Teva dhammā loko = Chính thân ấy / Chính cảm giác ấy / Chính tâm ấy / Chính các hiện tượng ấy là thế gian [new]
Pañcapi upādānakkhandhā loko = Cả năm khối làm đối tượng cho sự bám víu cũng là thế gian [new; ch4 UPK]
Iti ayañca abhijjhā idañca domanassaṃ imamhi loke vinītā honti paṭivinītā santā samitā vūpasantā atthaṅgatā abbhatthaṅgatā appitā byappitā sositā visositā byantīkatā = Như vậy, sự thèm muốn này và nỗi buồn này đối với thế gian này đã được chế ngự, đã được chế ngự hoàn toàn, đã lắng yên, đã được làm lắng dịu, đã lắng dịu hoàn toàn, đã biến mất, đã biến mất hoàn toàn, đã đi đến kết thúc, đã đi đến kết thúc hoàn toàn, đã bị làm khô cạn, đã bị làm khô cạn hoàn toàn, đã bị làm cho tiêu tan [new; atthaṅgata pi-1 ^1-1044]
Catunnaṃ satipaṭṭhānānaṃ kati …? = Trong bốn sự thiết lập tỉnh thức, bao nhiêu sự thiết lập tỉnh thức thiện, …? [T.question_q]

## Sammappadhāna (ch. 8)
anuppannā / uppannā pāpakā akusalā dhammā = các hiện tượng xấu ác bất thiện chưa sinh khởi / đã sinh khởi; anuppannā / uppannā kusalā dhammā = các hiện tượng thiện chưa sinh khởi / đã sinh khởi [pi-1 ^1-1377 words]
Iti imesaṃ … padahati = Như vậy, vị ấy khởi lên ý muốn, …, ra sức nỗ lực để những hiện tượng … này … [new]
chandaṃ janeti / vāyamati / vīriyaṃ ārabhati / cittaṃ paggaṇhāti / padahati (lemmas) = khởi lên ý muốn / nỗ lực / khởi động tinh tấn / nâng tâm lên / ra sức nỗ lực [pi-1 ^1-1377]
Yo chando chandikatā kattukamyatā kusalo dhammacchando = Điều mà là ý muốn, sự khởi ý muốn, sự muốn hành động, ý muốn thiện đối với các hiện tượng [new]
Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti nibbatteti abhinibbatteti = Vị ấy khởi lên ý muốn này, làm sinh ra, làm trỗi dậy, làm trỗi dậy trọn vẹn, làm phát khởi, làm hình thành [new; ch6 nibbatti / abhinibbatti]
Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti = Vị ấy khởi động sự tinh tấn này, khởi động trọn vẹn, thực hành, tu tập, làm đi làm lại [new]
Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti = Vị ấy nâng tâm này lên, nâng lên trọn vẹn, nâng đỡ, nâng đỡ vững chắc [new]
Ṭhitiyāti = “Để được duy trì”; Yā ṭhiti so asammoso, … yā bhāvanā sā pāripūrī = Sự duy trì là sự không mai một, sự không mai một là sự tăng trưởng, sự tăng trưởng là sự lớn mạnh, sự lớn mạnh là sự tu tập, sự tu tập là sự hoàn thiện [new; pi-1 ^1-1377 words]
…, tasmiṃ samaye <effort> = …, thì vào lúc ấy vị ấy khởi lên ý muốn, … [new]

## Iddhipāda (ch. 9)
chandasamādhi / vīriya- / citta- / vīmaṃsāsamādhi = định tâm nhờ ý muốn / nhờ tinh tấn / nhờ tâm / nhờ sự thẩm xét [new]
padhānasaṅkhāro / padhānasaṅkhārā = sự tạo tác bằng nỗ lực / các sự tạo tác bằng nỗ lực [new; ch6 X-saṅkhāra «sự tạo tác bằng X»]
chandasamādhipadhānasaṅkhārasamannāgataṃ iddhipādaṃ bhāveti = tu tập nền tảng thần thông được trang bị định tâm nhờ ý muốn và sự tạo tác bằng nỗ lực [new]
chandiddhipādo / vīriyiddhipādo / cittiddhipādo / vīmaṃsiddhipādo = nền tảng thần thông bằng ý muốn / bằng tinh tấn / bằng tâm / bằng sự thẩm xét (also the ##### headings; «bằng» avoids a doubled «là» in the Pañhāpucchaka) [new]
Chandaṃ ce bhikkhu adhipatiṃ karitvā labhati samādhiṃ, labhati cittassekaggataṃ = Nếu vị tỳ-khưu, sau khi lấy ý muốn làm yếu tố chủ đạo, đạt được định tâm, đạt được sự nhất tâm [new; pi-1 words]
Iti ayañca chandasamādhi, ime ca padhānasaṅkhārā = Như vậy, đây là định tâm nhờ ý muốn, và đây là các sự tạo tác bằng nỗ lực [ch6 frame]
tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā Xotveva saṅkhyaṃ gacchati = khi gom tất cả lại làm một và thu tóm lại, thì được tính là “X” [sample KHANDHA_TOGETHER + new]
Iti iminā ca chandena, iminā ca samādhinā, iminā ca padhānasaṅkhārena upeto hoti … = Như vậy, với ý muốn này, với định tâm này và với sự tạo tác bằng nỗ lực này, vị ấy là người có được, … [new]
Iddhīti. Yā tesaṃ dhammānaṃ iddhi samiddhi ijjhanā samijjhanā lābho paṭilābho patti sampatti phusanā sacchikiriyā upasampadā. = “Thần thông”. Điều mà ở những hiện tượng ấy là thần thông, sự thịnh đạt, sự thành tựu, sự thành tựu trọn vẹn, sự đạt được, sự có được, sự đạt đến, sự đạt đến trọn vẹn, sự chạm, sự tự mình chứng nghiệm, sự chứng nhập. [new; ch4 paṭilābha, pi-1 phusanā]
Iddhipādoti. Tathābhūtassa X = “Nền tảng thần thông”. X của người đã trở nên như vậy. [new]
Te dhamme āsevati bhāveti bahulīkaroti = Vị ấy thực hành những hiện tượng ấy, tu tập, làm đi làm lại [new]

## Pañhāpucchaka additions
Kusalāyeva = Chỉ là thiện [new]
na maggādhipatino = không lấy con đường làm yếu tố chủ đạo [new]
(siyā) na vattabbā Xti(pi), Ytipi (no dash, no quotes in the Pāli) = (đôi khi) không nên nói rằng X, hay rằng Y (no dash, no quotes added; affirmative after it: «mà …») [new; B.NV without its dash]
Subjects (ch. 9): Vīmaṃsiddhipādo = Nền tảng thần thông bằng sự thẩm xét; cittiddhipādo = nền tảng thần thông bằng tâm (single subjects: «thì» before non-«là» predicates, F rule); Tayo iddhipādā = Ba nền tảng thần thông

## Variant brackets
ātāpo [katamaṃ ātāpaṃ (sabbattha)] = sự nhiệt tâm [dị bản (tất cả các ấn bản): katamaṃ ātāpaṃ]
nhāru [nahāru (sī.)], aṭṭhimiñjaṃ [aṭṭhimiñjā (sī.)] = ch3 strings
thinamiddhaṃ [thīnamiddhaṃ (sī. syā.)] = sự uể oải và đờ đẫn [khác chính tả (Sī., Syā.): thīnamiddhaṃ]
vīriyasambojjhaṅgaṃ [viriyasambojjhaṅgaṃ (sī. syā.)] = chi phần giác ngộ là sự tinh tấn [khác chính tả (Sī., Syā.): viriyasambojjhaṅgaṃ]
chandikatā [chandīkatā (syā.)] = sự khởi ý muốn [khác chính tả (Syā.): chandīkatā]
uṭṭhapeti samuṭṭhapeti [uṭṭhāpeti samuṭṭhāpeti (syā.) evamuparipi] = làm trỗi dậy, làm trỗi dậy trọn vẹn [khác chính tả (Syā.): uṭṭhāpeti samuṭṭhāpeti; cũng vậy ở các chỗ sau]
cittassekaggataṃ [cittassa ekaggataṃ (sī. syā.)] = sự nhất tâm [khác chính tả (Sī., Syā.): cittassa ekaggataṃ]
saṅkhyaṃ [saṅkhaṃ (sī.)] gacchati = thì được tính [khác chính tả (Sī.): saṅkhaṃ] là …

## Pāli slips (all reported)
Rendered as meant (spelling / punctuation only): ^2-388 "Siyā vipākā siyā vipākadhammadhammā" (comma); ^2-389 "sāsavācātipi", "āsavasampayuttācātipi" (spaces); ^2-364, ^2-367 (pītisambojjhaṅgaṃ …pe…), ^2-404, ^2-418, ^2-442, ^2-460 stray spaces before …pe…; ^2-432 "abhisaññahitvā" (later repeats abhisaññūhitvā); ^2-443 "viññāṇakhandho"; ^2-450 "Tathābhūtasa"; ^2-455 final full stop missing; ^2-459 "maggariyāpannaṃ"; "Araṇāti." (closing ti of the question list) = «Không có xung đột.»
As written: ^2-366 "Pañcapi upādānakkhandhā loko – tattha katamā abhijjhā?" (parallels: ". Ayaṃ vuccati "loko". Tattha …") = «… cũng là thế gian – ở đây, sự thèm muốn là gì?», dash kept; ^2-368 and ^2-376 answers unquoted; ^2-367 "tañca pajānāti, santaṃ vā ajjhattaṃ dhammavicaya…" (comma where the parallels have a full stop) = «; hoặc khi …»; ^2-389 "Āsavavippayuttā. Anāsavā." repeated; ^2-356 ajjhattabahiddhā quote "atthi imasmiṃ kāye" (as the ajjhatta one) = «Trong thân này có»; ^2-388 / ^2-389 / ^2-429 / ^2-464 "na vattabbā" clusters without dash or quotes = no dash, no quotes.
No doubled or missing negation found in chapters 7-9.
