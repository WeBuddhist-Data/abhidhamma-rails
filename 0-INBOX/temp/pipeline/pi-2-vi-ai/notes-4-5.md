# pi-2 Vietnamese zero-shot, chapters 4 (Saccavibhaṅga) and 5 (Indriyavibhaṅga): new terms and formulas

Builder: build_4-5_vi.py (imports build_ch1_sample_vi as S, build_1_vi as B, build_2-3_vi as T; T's item tables and Abhidhammabhājanīya frames are extended in memory only; pi-1 strings are copied from the pi-1 Vietnamese rails at build time and asserted; check_same_pali() asserts that the ch. 4/5 feeling and eye/body definitions have the same Pāli as ch. 3). Scratch lookup: probe_4-5_vi.py.
Format: Pāli = tiếng Việt, one per line. [pi-1] = verbatim from the pi-1 Vietnamese rails (block ID given); [ch1-3] = from the earlier builders; [new] = settled here.

## Truths
dukkha (suffering) = khổ đau [pi-1 APPROVED]; dukkha (bodily pain, ^2-196, in soka…upāyāsā) = sự khó chịu [pi-1 ^1-1343]
dukkhasamudaya = sự phát sinh của khổ đau [pi-1 ^1-1238]
dukkhanirodha = sự chấm dứt khổ đau [pi-1 ^1-1238]
dukkhanirodhagāminī paṭipadā = cách thực hành dẫn đến sự chấm dứt khổ đau [pi-1 ^1-1238]
ariyasacca = sự thật cao quý; dukkhaṃ ariyasaccaṃ = sự thật cao quý về khổ đau (… về sự phát sinh của khổ đau, … về sự chấm dứt khổ đau, … về cách thực hành dẫn đến sự chấm dứt khổ đau) [pi-1 core]
Cattāri ariyasaccāni – … = Bốn sự thật cao quý – …, … và … [new; «và» before the last, as ch. 2 numbered lists]
Cattāri saccāni – dukkhaṃ, dukkhasamudayo, dukkhanirodho, dukkhanirodhagāminī paṭipadā = Bốn sự thật – khổ đau, sự phát sinh của khổ đau, sự chấm dứt khổ đau và cách thực hành dẫn đến sự chấm dứt khổ đau [new]
##### Dukkhasaccaṃ / Samudayasaccaṃ / Nirodhasaccaṃ / Maggasaccaṃ = Sự thật về khổ đau / Sự thật về sự phát sinh / Sự thật về sự chấm dứt / Sự thật về con đường (as written, no «của khổ đau»; same strings as Pañhāpucchaka subjects) [new]
Dve saccā / Tīṇi saccāni = Hai sự thật / Ba sự thật [new]
Catunnaṃ ariyasaccānaṃ kati …? = Trong bốn sự thật cao quý, bao nhiêu sự thật thiện, …? [ch1-3 frame]

## Suttanta: suffering
Jātipi dukkhā, jarāpi dukkhā, maraṇampi dukkhaṃ = Sự sinh cũng là khổ đau, sự lão hóa cũng là khổ đau, sự chết cũng là khổ đau («cũng» only where the Pāli has pi) [new]
sokaparidevadukkhadomanassupāyāsā = sự sầu muộn, sự than khóc, sự khó chịu, nỗi buồn và sự tuyệt vọng [pi-1 ^1-1343]
appiyehi sampayogo dukkho = gặp gỡ những gì mình không yêu quý là khổ đau; as a name: khổ đau vì gặp gỡ những gì mình không yêu quý [new]
piyehi vippayogo dukkho = xa lìa những gì mình yêu quý là khổ đau; as a name: khổ đau vì xa lìa những gì mình yêu quý [new; piya «yêu quý» kept apart from kanta «yêu mến» and manāpa «ưa thích»]
yaṃ picchaṃ na labhati tampi dukkhaṃ = không đạt được điều mình mong cầu cũng là khổ đau (in the question and answer between “…”) [new]
saṃkhittena pañcupādānakkhandhā dukkhā = nói tóm lại, năm khối làm đối tượng cho sự bám víu là khổ đau [new]
rūpupādānakkhandho = khối vật chất làm đối tượng cho sự bám víu (likewise the other four) [new]
tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye = ở từng chúng sinh, trong từng loài chúng sinh [new; sample «từng chúng sinh»]
jāti sañjāti okkanti abhinibbatti khandhānaṃ pātubhāvo āyatanānaṃ paṭilābho = sự sinh, sự sinh ra, sự nhập thai, sự hình thành, sự xuất hiện của các khối, sự có được các lĩnh vực nhận biết [new; jāti pi-1]
jarā … indriyānaṃ paripāko = sự lão hóa, sự hao mòn, răng gãy rụng, tóc bạc, da nhăn nheo, sự suy giảm tuổi thọ, sự chín muồi của các năng lực [pi-1 ^1-643]
cuti cavanatā bhedo antaradhānaṃ maccu maraṇaṃ kālakiriyā khandhānaṃ bhedo kaḷevarassa nikkhepo jīvitindriyassupacchedo = sự lìa khỏi (từng loài chúng sinh), trạng thái lìa khỏi, sự tan rã, sự biến mất, sự tử vong, sự chết, sự qua đời, sự tan rã của các khối, sự bỏ lại thân xác, sự cắt đứt năng lực sống [new; bhedo, antaradhānaṃ pi-1 ^1-644]
byasana = tổn hại; Ñātibyasanena vā phuṭṭhassa … aññataraññatarena dukkhadhammena phuṭṭhassa = Ở người gặp phải tổn hại về người thân, hoặc gặp phải tổn hại về tài sản, hoặc gặp phải tổn hại do bệnh tật, hoặc gặp phải tổn hại về giới hạnh, hoặc gặp phải tổn hại về quan điểm, ở người vướng phải tổn hại này hay tổn hại khác, gặp phải điều khổ đau này hay điều khổ đau khác, có … [new]
soko socanā socitattaṃ antosoko antoparisoko cetaso parijjhāyanā domanassaṃ sokasallaṃ = sự sầu muộn, sự buồn rầu, trạng thái buồn rầu, nỗi sầu bên trong, nỗi sầu thấm sâu bên trong, sự héo hon của tâm, nỗi buồn, mũi tên sầu muộn [new]
ādevo paridevo ādevanā paridevanā ādevitattaṃ paridevitattaṃ vācā palāpo vippalāpo lālappo lālappanā lālappitattaṃ = sự kêu khóc, sự than khóc, hành động kêu khóc, hành động than khóc, trạng thái kêu khóc, trạng thái than khóc, lời nói, lời lảm nhảm, lời lảm nhảm không ngớt, sự rên rỉ, hành động rên rỉ, trạng thái rên rỉ [new]
āyāso upāyāso āyāsitattaṃ upāyāsitattaṃ = sự phiền muộn, sự tuyệt vọng, trạng thái phiền muộn, trạng thái tuyệt vọng [new; upāyāsa pi-1]
Yaṃ kāyikaṃ asātaṃ … = Điều mà là <ch. 3 dukkhadhātu body>; Yaṃ cetasikaṃ asātaṃ … = <ch. 3 domanassadhātu body> [ch1-3]
Idha yassa te honti aniṭṭhā akantā amanāpā rūpā … phoṭṭhabbā = Ở đời này, đối với người nào mà các hình sắc, âm thanh, mùi, vị, vật xúc chạm là không đáng mong muốn, không đáng yêu mến, không đáng ưa thích [sample words]
ye vā panassa te honti anatthakāmā ahitakāmā aphāsukakāmā ayogakkhemakāmā = hoặc có những người mong điều không lợi ích, mong điều không tốt lành, mong điều không thoải mái, mong điều không an ổn cho người ấy (positive: mong điều lợi ích, … an ổn) [new]
mātā vā pitā vā bhātā vā bhaginī vā mittā vā amaccā vā ñātī vā sālohitā vā = mẹ, hoặc cha, hoặc anh em trai, hoặc chị em gái, hoặc bạn bè, hoặc đồng sự, hoặc bà con, hoặc người ruột thịt (after ":") [new]
yā tehi saṅgati samāgamo samodhānaṃ missībhāvo = sự gặp gỡ, sự gần gũi, sự tụ hợp, sự hòa lẫn với chúng (a-: sự không gặp gỡ, …) [new]
X-dhammānaṃ sattānaṃ evaṃ icchā uppajjati – "aho vata, mayaṃ na X-dhammā assāma; na ca, vata, no X āgaccheyyā"ti! = Ở những chúng sinh có bản chất phải X, khởi lên mong muốn như vầy – “Ôi, ước gì chúng ta không có bản chất phải X; và ước gì X không đến với chúng ta”! [new]
jāti/jarā/byādhi/maraṇa-dhamma = có bản chất phải sinh / phải già / phải bệnh / phải chết; sokaparideva…dhamma = có bản chất phải chịu sự sầu muộn, … và sự tuyệt vọng [new]
Na kho panetaṃ icchāya pattabbaṃ. = Nhưng điều này không thể đạt được bằng sự mong muốn. [new]
Idampi "…". = Đây cũng là “…”. [new]
seyyathidaṃ – = cụ thể là – [ch1-3]

## Suttanta: craving
Yāyaṃ taṇhā ponobhavikā nandirāgasahagatā tatratatrābhinandinī = Đó là khao khát dẫn đến sự hiện hữu mới, có sự tham đắm vì thích thú đi kèm, tìm vui thích ở chỗ này chỗ kia [new; nandirāga pi-1 ^1-1065]
kāmataṇhā, bhavataṇhā, vibhavataṇhā = khao khát dục lạc, khao khát được hiện hữu, khao khát không còn hiện hữu [pi-1 ^1-1065]
X loke piyarūpaṃ sātarūpaṃ = X trong thế gian là điều đáng yêu, là điều khoan khoái [new; sāta pi-1 «khoan khoái»]
Kiñca loke piyarūpaṃ sātarūpaṃ? = Và điều gì trong thế gian là điều đáng yêu, là điều khoan khoái? [new]
Sā kho panesā taṇhā kattha uppajjamānā uppajjati, kattha nivisamānā nivisati? = Vậy khao khát này khi sinh khởi thì sinh khởi ở đâu, khi bám rễ thì bám rễ ở đâu? [new]
Yaṃ loke piyarūpaṃ sātarūpaṃ, etthesā taṇhā … = Điều gì trong thế gian là điều đáng yêu, là điều khoan khoái, thì ở đó, khao khát này … [new]
Etthesā taṇhā uppajjamānā uppajjati, ettha nivisamānā nivisati. = Ở đó, khao khát này khi sinh khởi thì sinh khởi, ở đó, khi bám rễ thì bám rễ. [new]
Etthesā taṇhā pahīyamānā pahīyati, ettha nirujjhamānā nirujjhati. = Ở đó, khao khát này khi được dứt bỏ thì được dứt bỏ, ở đó, khi chấm dứt thì chấm dứt. [new]
cakkhusamphasso = sự tiếp xúc của mắt (… của ý) [pi-1 words]
rūpasaññā = tri giác về hình sắc; rūpasañcetanā = sự cố ý về hình sắc; rūpataṇhā = khao khát hình sắc [pi-1]; rūpavitakko = sự hướng tâm đến hình sắc; rūpavicāro = sự duy trì tâm trên hình sắc (… đối tượng của ý) [new]
Yo tassāyeva taṇhāya asesavirāganirodho cāgo paṭinissaggo mutti anālayo = Đó là sự phai nhạt và chấm dứt không còn dư sót của chính khao khát ấy, sự xả bỏ, sự buông bỏ, sự giải thoát, sự không còn bám chấp [new; cāga «sự xả bỏ» kept apart from nekkhamma «sự từ bỏ»]

## Suttanta: path
Ayameva ariyo aṭṭhaṅgiko maggo = Đó chính là con đường cao quý gồm tám chi phần [pi-1 ^1-337 «con đường gồm tám chi phần»]
pañcaṅgiko maggo = con đường gồm năm chi phần [pi-1 ^1-89]
path-factor names = quan điểm / tư duy / lời nói / hành động / sinh kế / nỗ lực / tỉnh thức / định tâm đúng đắn [pi-1 ^1-297 … ^1-304]
Dukkhe ñāṇaṃ, … = Sự hiểu biết về khổ đau, sự hiểu biết về sự phát sinh của khổ đau, … [new; mirrors pi-1 ^1-1238 «sự không biết về …»]
Nekkhamma-/abyāpāda-/avihiṃsāsaṅkappo = Tư duy về sự từ bỏ / về sự không ác ý / về sự không hãm hại [new; ch. 3 words]
Musāvādā / pisuṇāya vācāya / pharusāya vācāya / samphappalāpā veramaṇī = Sự kiềm chế việc nói dối / việc nói lời chia rẽ / việc nói lời thô ác / việc nói lời phù phiếm [new; veramaṇī pi-1 «sự kiềm chế»]
Pāṇātipātā / adinnādānā / kāmesumicchācārā veramaṇī = Sự kiềm chế việc sát hại sinh mạng / việc lấy của không được cho / hành vi sai trái trong các dục lạc [new]
Idha ariyasāvako micchāājīvaṃ pahāya sammāājīvena jīvikaṃ kappeti = Ở đời này, vị đệ tử của bậc thánh, sau khi dứt bỏ sinh kế sai lầm, nuôi sống bản thân bằng sinh kế đúng đắn [new]
Idha bhikkhu anuppannānaṃ … padahati. (×4) = pi-1 ^1-1377 clauses, one sentence each; sentences 2–4 begin «Vị ấy …» [pi-1]
Idha bhikkhu kāye kāyānupassī viharati ātāpī sampajāno satimā, vineyya loke abhijjhādomanassaṃ = Ở đời này, vị tỳ-khưu, đối với thân, sống quán sát thân, nhiệt tâm, hiểu biết rõ ràng, có sự tỉnh thức, sau khi chế ngự sự thèm muốn và nỗi buồn đối với thế gian [new; abhijjhādomanassa pi-1 ^1-1352]
Vedanāsu…pe… citte…pe… dhammesu dhammānupassī = Đối với các cảm giác… đối với tâm… đối với các hiện tượng, vị ấy sống quán sát các hiện tượng [new; dhamma here = hiện tượng]
ātāpī = nhiệt tâm (kept apart from vīriya «tinh tấn») [new]
Sutta jhāna formula (Idha bhikkhu vivicceva kāmehi … catutthaṃ jhānaṃ upasampajja viharati) = pi-1 ^1-160 and the 2nd–4th rūpāvacara jhāna lines (2-02-cittuppadakandam lines 3, 6, 9) without «với đề mục bao trùm là đất»; «vị ấy» before the verb of the 2nd–4th jhāna [pi-1]

## Abhidhammabhājanīya (ch. 4)
Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti … dukkhapaṭipadaṃ dandhābhiññaṃ, tasmiṃ samaye = Ở đời này, vào lúc vị tỳ-khưu <pi-1 ^1-277 from «tu tập» to «chậm chạp,»> thì vào lúc ấy có … [pi-1]
aṭṭhaṅgiko maggo hoti – sammādiṭṭhi…pe… sammāsamādhi = con đường gồm tám chi phần – quan điểm đúng đắn… định tâm đúng đắn [pi-1 words]
phasso hoti…pe… avikkhepo hoti = sự tiếp xúc… có sự không tán loạn [pi-1 ^1-160]
Path-factor definitions = pi-1 ^1-297 … ^1-304 after «Điều mà là», «…pe…» cut at the same items [pi-1]
Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā. = Các hiện tượng còn lại gắn liền với cách thực hành dẫn đến sự chấm dứt khổ đau. [new]
avasesā kilesā = các phiền não còn lại; avasesā akusalā dhammā = các hiện tượng bất thiện còn lại [new]
tīṇi kusalamūlāni sāsavāni = ba gốc rễ thiện mà là đối tượng của ô nhiễm [new; «mà» marks the restrictive attribute; sāsava pi-1]
avasesā sāsavā kusalā dhammā = các hiện tượng thiện còn lại mà là đối tượng của ô nhiễm [new]
sāsavā kusalākusalānaṃ dhammānaṃ vipākā = các quả của các hiện tượng thiện và bất thiện mà là đối tượng của ô nhiễm [new; pi-1 ^1-583 words]
ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā, sabbañca rūpaṃ = những hiện tượng mang tính chức năng, không phải thiện, không phải bất thiện, cũng không phải quả của nghiệp; và toàn bộ vật chất [pi-1 ^1-583]
"X ca, Y ca, …" lists = «X, Y và Z»; with «; » and «; và» when an item has inner commas (pi-1 ^1-583) [new]
Taṇhāya (ca, …) pahānaṃ = Sự dứt bỏ khao khát (và …) [new]

## Faculties (ch. 5)
Bāvīsatindriyāni = Hai mươi hai năng lực; Bāvīsatīnaṃ indriyānaṃ kati …? = Trong hai mươi hai năng lực, bao nhiêu năng lực thiện, …? [new]
indriya names = năng lực mắt … năng lực của người đã hiểu biết trọn vẹn [pi-1]
rūpajīvitindriya / arūpajīvitindriya = năng lực sống thuộc vật chất / năng lực sống phi vật chất [new; pi-1 rūpino / arūpino]
Jīvitindriyaṃ duvidhena – atthi X, atthi Y = Phân loại năng lực sống theo nhóm hai – có loại là X, có loại là Y [new; ch. 1 frame]
manindriya classification = the ch. 2 manāyatana classification with «năng lực ý» (T's frames) [ch1-3]
Evaṃ dasavidhena manindriyaṃ…pe… evaṃ bahuvidhena manindriyaṃ. = Như vậy là phân loại năng lực ý theo nhóm mười… như vậy là phân loại năng lực ý theo nhiều nhóm. [ch1-3 words]
itthindriya / purisindriya / rūpajīvitindriya bodies = pi-1 ^1-714 / ^1-716 / ^1-718; arūpajīvitindriya = pi-1 ^1-19 (variant dropped) [pi-1]
saddhā / vīriya / sati / samādhi / paññā bodies = pi-1 ^1-12 … ^1-16 after «Điều mà là» (vīriya: pi-1 variants dropped, no «nỗ lực đúng đắn» as in the pi-2 Pāli) [pi-1]
thāmo ṭhiti (pi-2; pi-1 thāmo dhiti) = sức bền, sự ổn định [as written]
anaññātaññassāmītindriya / aññindriya bodies = pi-1 ^1-296 / 2-03-cittuppadakandam line 106, with «…» at the Pāli «…pe…» [pi-1]
Yā tesaṃ dhammānaṃ aññātāvīnaṃ diṭṭhānaṃ … = Điều mà, để tự mình chứng nghiệm những hiện tượng ấy vốn đã hiểu biết trọn vẹn, đã được thấy, … [new; aññindriya frame]
Subjects: Dvindriyā … Ekavīsatindriyā = Hai … Hai mươi mốt năng lực; Cha indriyā = Sáu năng lực [new]

## Pañhāpucchaka additions
Single named subjects (a truth, a faculty) take «thì» before the predicate (not before «là …»): «Sự thật về con đường thì thiện.», «Năng lực nỗi buồn thì bất thiện.», «Năng lực ý là tâm.»; numbered subjects as ch. 1–3 («thì» only before «không nên nói») [new]
Sentences without a subject (Sappaccayā. Saṅkhatā. Anidassanā. No āsavā. Sahetukā ceva na ca hetū.) = the predicate capitalised: «Có điều kiện. Do điều kiện tạo thành. Không thấy được. Không phải là ô nhiễm.» [ch1 LABELS «Có điều kiện, do điều kiện tạo thành.»]
na maggārammaṇaṃ = không lấy con đường làm đối tượng [new]
na maggārammaṇaṃ maggahetukaṃ = không lấy con đường làm đối tượng, lấy con đường làm gốc rễ [new; two predicates, a comma, as B piti_only]
maggārammaṇaṃ na maggahetukaṃ = lấy con đường làm đối tượng, không lấy con đường làm gốc rễ [new]
(siyā) mahaggatārammaṇaṃ na appamāṇārammaṇaṃ = có đối tượng rộng lớn, không có đối tượng không thể đo lường [new]
arūpāni (neuter pl.) = phi vật chất [B item]

## Variant brackets
[dukkhasamudayo (syā.)] / [dukkhanirodho (syā.)] = [khác chính tả (Syā.): dukkhasamudayo] / [… dukkhanirodho]
[lālapo lālapanā lālapitattaṃ (syā.)] = [khác chính tả (Syā.): lālapo lālapanā lālapitattaṃ]
[ponobbhavikā (syā. ka.)] = [khác chính tả (Syā., Ka.): ponobbhavikā]
[veramaṇi (ka.) evamuparipi] = [khác chính tả (Ka.): veramaṇi; cũng vậy ở các chỗ sau]
[viriyārambho (sī. syā.)] = [khác chính tả (Sī., Syā.): viriyārambho]; [viriyindriyaṃ (sī. syā.)] = [khác chính tả (Sī., Syā.): viriyindriyaṃ]

## Pāli slips (translated as written unless noted; all reported)
^2-206 "aṭṭhaṅgiko maggo hoti sammādiṭṭhi…pe…" (no dash; the repeats have one): a colon, no dash.
^2-207 "Ayaṃ vuccati – "dukkhanirodhagāminī paṭipadā"" (dash, the repeats have none): dash kept («Đó được gọi là – “…”»).
^2-207–212 "pattiyā, vivicceva" vs "pattiyā vivicceva": comma only, same Vietnamese.
^2-217 "siyā mahaggatārammaṇaṃ na appamāṇārammaṇaṃ" (no comma): rendered with a comma between the two predicates.
^2-218 "Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā." (full stop missing): two sentences.
^2-218 '…sampayuttañcā" tipi' ×2 (space); final "siyā araṇanti" (closing ti): punctuation only.
^2-218 "Dukkhasaccaṃ siyā ajjhattaṃ, siyā bāhiraṃ" (the ajjhattika/bāhira dyad; ajjhattaṃ perhaps for ajjhattikaṃ): as written, «đôi khi ở nơi bản thân, đôi khi thuộc phần bên ngoài».
^2-218 "Samudayasaccaṃ na vattabbaṃ – "parāmāso ceva parāmaṭṭhañcā"ti, parāmaṭṭhañceva no ca parāmāso." and the ch. 5 clusters "– "X"ti, Y." / "– "X"ti, "Y".": Y as an affirmative («mà …»), unquoted, as ch. 1–3.
^2-218 "Samudayasaccaṃ gantho ceva ganthasampayuttañca, siyā na vattabbaṃ …" / "Samudayasaccaṃ siyā upādānañceva upādānasampayuttañca, siyā na vattabbaṃ …": as written.
^2-220 answer "arūpajīvatindriyaṃ": spelling slip, rendered as meant («năng lực sống phi vật chất»).
^2-220 aññindriya answer "idaṃ vuccati aññindriyaṃ." without quotes: as written, unquoted.
^2-220 vīriyindriya "thāmo ṭhiti" (pi-1 "thāmo dhiti") and no "sammāvāyāmo": as written.
^2-223 "siyā parittārammaṇaṃ siyā mahaggatārammaṇaṃ" (comma missing); '"mahaggatārammaṇa"nti pi' (space): punctuation only.
^2-223 "…siyā ajjhattabahiddhārammaṇā, aṭṭhindriyā siyā …" (comma where a full stop is expected): kept, lowercase «tám năng lực».
^2-224 "Tīṇindriyā na vattabbā – "hetū ceva sahetukā cā"ti. Sahetukā ceva na ca hetū." (full stop where the clusters have a comma): two sentences, the second without a subject.
^2-224 '"gantho ceva ganthasampayutta"ñcāti' (quote closed too early): punctuation only.
^2-224 "Navindriyā na vattabbā – … siyā upādāniyā ceva no ca upādānā. Dasindriyā siyā upādāniyā ceva no ca upādānā, siyā na vattabbā …" (numbers look shifted against the parallel clusters): as written.
No doubled or missing negation found in chapters 4–5.
