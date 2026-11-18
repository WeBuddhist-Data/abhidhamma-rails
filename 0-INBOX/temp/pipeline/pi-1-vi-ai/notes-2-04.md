# Notes for part 2-04 (Vietnamese plain zero-shot, twelve unwholesome minds and results of the wholesome, ^1-1-6-0 … ^1-504): new recurring terms and formulas

Builder: build_2-04_vi.py (imports build_matika_vi, build_ch2_01_sample_vi, build_2-01_2-02_vi and build_2-03_vi unchanged;
adds entries to their tables in memory only, never overwriting one). `python -I -X utf8 build_2-04_vi.py` checks the 41
headings against vi-zeroshot-terms.md, asserts that the 34 Pāli lines that also occur in 2-01/2-02/2-03 get the published
Vietnamese byte for byte, and re-renders 313 earlier lines to prove the added entries changed nothing. Checks:
verify_vi_2-04.py. 149 segments.
Reusable pieces (import with importlib): NEW_NAMES, NEW_COUNTED, NEW_STR, NEW_TOKENS, NEW_PH, TAJJA_OF(), RESULT_KAMA,
TASSEVA(), AKUSALA_V, ABYAKATA_V, ABY_ROOT, presub(), open_vi(), rest_vi(), sphere_vi(), translate_line().

## Headings and closing lines (headings verbatim from vi-zeroshot-terms.md)
Dvādasa akusalāni / Dvādasa akusalacittāni. = Mười hai loại tâm bất thiện / Mười hai loại tâm bất thiện.
Abyākatavipāko = Quả của nghiệp, không xác định về mặt đạo đức
Kusalavipākapañcaviññāṇāni / Kusalavipākāni pañcaviññāṇāni. = Năm loại thức là quả của nghiệp thiện (.)
Kusalavipākamanodhātu / Kusalavipākā manodhātu. = Yếu tố ý là quả của nghiệp thiện (.)
Kusalavipākamanoviññāṇadhātusomanassasahagatā / Kusalavipākā manoviññāṇadhātu somanassasahagatā. = Yếu tố ý thức là quả của nghiệp thiện, có niềm vui đi kèm (.)
Kusalavipākamanoviññāṇadhātuupekkhāsahagatā / Kusalavipākā upekkhāsahagatā manoviññāṇadhātu. = Yếu tố ý thức là quả của nghiệp thiện, có sự bình thản đi kèm (.)
Aṭṭhamahāvipākā (.) = Tám quả nghiệp lớn (.)
Rūpāvacaravipākā (.) / Arūpāvacaravipākā (.) = Các quả nghiệp thuộc cõi hình sắc (.) / Các quả nghiệp thuộc cõi không hình sắc (.)

## Frames
Katame dhammā akusalā? / abyākatā? = Những hiện tượng nào là bất thiện? / … là không xác định về mặt đạo đức? (M.QUESTION)
ime dhammā akusalā / abyākatā = đây là các hiện tượng bất thiện / … không xác định về mặt đạo đức (M.ANSWER_BARE)
Yasmiṃ samaye akusalaṃ cittaṃ uppannaṃ hoti X, tasmiṃ samaye … = Vào lúc tâm bất thiện sinh khởi, X, thì vào lúc ấy …
kāmāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti = (Vào lúc) thức qua mắt sinh khởi như là quả của nghiệp thiện thuộc cõi dục lạc đã được tạo và tích lũy
… vipākā manodhātu / manoviññāṇadhātu uppannā hoti = (Vào lúc) yếu tố ý / yếu tố ý thức sinh khởi như là quả của nghiệp thiện thuộc cõi dục lạc đã được tạo và tích lũy
ghāna- / jivhā- / kāyaviññāṇaṃ uppannaṃ hoti (after …pe…) = thức qua mũi / thức qua lưỡi / thức qua thân sinh khởi
Tasseva rūpāvacarassa / arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ X, tasmiṃ samaye … = Như là quả của chính nghiệp thiện thuộc cõi hình sắc / cõi không hình sắc ấy đã được tạo và tích lũy, khi một người X, thì vào lúc ấy …  (when X begins with «khi …»: «khi một người, khi đã …»)
(the wholesome sentence before «Tasseva» = B.kusala_vi, the 2-02 frame unchanged)
Yaṃ tasmiṃ samaye na hirīyati … / na ottappati … – … = Việc vào lúc ấy S – đây là X vào lúc ấy. (the sample's hirī frame)
alobho / adoso abyākatamūlaṃ = sự không tham lam / sự không sân hận, gốc rễ không xác định về mặt đạo đức
akusalamūlaṃ = gốc rễ bất thiện; abyākatamūlaṃ = gốc rễ không xác định về mặt đạo đức

## Opening qualifiers
somanassasahagata / domanassasahagata / upekkhāsahagata / sukhasahagata = có niềm vui / có nỗi buồn / có sự bình thản / có hạnh phúc đi kèm (triad 7 for the last two)
diṭṭhigatasampayuttaṃ / diṭṭhigatavippayuttaṃ = gắn liền / không gắn liền với sự mắc kẹt trong các quan điểm (diṭṭhigata as 2-03)
paṭighasampayuttaṃ = gắn liền với sự ác cảm  (paṭigha as aversion = sự ác cảm; paṭigha as sensory impact stays «sự va chạm», 2-02 / matrix)
vicikicchāsampayuttaṃ / uddhaccasampayuttaṃ = gắn liền với sự hoài nghi / gắn liền với sự xao động
rūpārammaṇaṃ / saddārammaṇaṃ / gandhārammaṇaṃ / rasārammaṇaṃ / phoṭṭhabbārammaṇaṃ (one object) = lấy hình sắc / âm thanh / mùi / vị / vật xúc chạm làm đối tượng
rūpārammaṇā vā…pe… phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha = lấy hình sắc… hoặc vật xúc chạm, hay bất cứ thứ gì làm đối tượng
rūpārammaṇaṃ vā…pe… yaṃ yaṃ vā panārabbha = lấy hình sắc… hay bất cứ thứ gì làm đối tượng
feminine forms (-sahagatā, ñāṇasampayuttā …, -ārammaṇā vā) = the same Vietnamese as the neuter ones

## Names
micchādiṭṭhi / micchāsaṅkappo / micchāvāyāmo / micchāsamādhi = quan điểm sai lầm / tư duy sai lầm / nỗ lực sai lầm / định tâm sai lầm (micchā = sai lầm, as micchatta, micchāsati)
ahirikabalaṃ / anottappabalaṃ = sức mạnh không biết hổ thẹn / sức mạnh không biết ghê sợ tội lỗi
ahirikaṃ / anottappaṃ = sự không biết hổ thẹn / sự không biết ghê sợ tội lỗi (matrix ^1-M2-115)
lobho / doso / moho = sự tham lam / sự sân hận / sự si mê
abhijjhā = sự thèm muốn; byāpādo = sự ác ý
vicikicchā = sự hoài nghi (kaṅkhā = sự nghi ngờ, kept apart); uddhaccaṃ = sự xao động
dukkhaṃ (factor) = sự đau khổ (sukhaṃ = hạnh phúc); domanassindriyaṃ = năng lực nỗi buồn; sukhindriyaṃ = năng lực dễ chịu (suggested for 2-05: dukkhindriyaṃ = năng lực khó chịu)
cakkhu- / sota- / ghāna- / jivhā- / kāyaviññāṇa = thức qua mắt / qua tai / qua mũi / qua lưỡi / qua thân
cakkhuviññāṇadhātu / kāyaviññāṇadhātu = yếu tố thức qua mắt / yếu tố thức qua thân; manodhātu = yếu tố ý
pañcindriyāni / cattāri indriyāni / tīṇindriyāni = năm / bốn / ba năng lực
tivaṅgiko / duvaṅgiko maggo = con đường gồm ba / hai chi phần
cattāri / tīṇi balāni = bốn / ba sức mạnh; eko hetu = một gốc rễ

## Strings
tajjācakkhuviññāṇadhātusamphassaja- / tajjākāyaviññāṇadhātusamphassaja- / tajjāmanodhātusamphassaja- = và sinh từ sự tiếp xúc của yếu tố thức qua mắt / yếu tố thức qua thân / yếu tố ý tương ứng (after «Điều có mặt vào lúc ấy»)
… viññāṇakkhandho tajjācakkhuviññāṇadhātu / tajjākāyaviññāṇadhātu / tajjāmanodhātu = …, khối thức, yếu tố thức qua mắt / thức qua thân / ý tương ứng
takko … cetaso abhiniropanā (+ micchāsaṅkappo) = the sample string without «, tư duy đúng đắn» (+ «, tư duy sai lầm»); likewise the samādhi string + «định tâm sai lầm», the vīriya string + «nỗ lực sai lầm»
cittassa ṭhiti (abbreviated string) = sự ổn định của tâm
cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā vedanā = sự bứt rứt trong tâm, sự khó chịu trong tâm, cảm nhận bứt rứt và khó chịu sinh từ sự tiếp xúc của tâm, cảm giác bứt rứt và khó chịu sinh từ sự tiếp xúc của tâm
kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā = sự khoan khoái nơi thân, sự dễ chịu nơi thân, cảm nhận khoan khoái và dễ chịu sinh từ sự tiếp xúc của thân, cảm giác khoan khoái và dễ chịu sinh từ sự tiếp xúc của thân
lobho lubbhanā lubbhitattaṃ sārāgo sārajjanā sārajjitattaṃ abhijjhā lobho akusalamūlaṃ = sự tham lam, sự khởi lòng tham, trạng thái khởi lòng tham, sự say đắm, sự bị cuốn hút, trạng thái bị cuốn hút, sự thèm muốn, sự tham lam, gốc rễ bất thiện
doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa = sự sân hận, sự khởi sân, trạng thái khởi sân, sự thù hằn, sự khởi thù hằn, trạng thái khởi thù hằn, sự chống đối, sự đối nghịch, sự hung dữ, sự thô lỗ, sự không hài lòng của tâm
aññāṇaṃ … moho akusalamūlaṃ = sự không biết, sự không thấy, sự không thấu hiểu, sự không hiểu ra, sự không tỉnh ngộ, sự không thấu triệt, sự không nắm bắt, sự không đi sâu, sự không xem xét, sự không xem xét lại, sự không tự mình thấy rõ, sự ngu muội, sự khờ dại, sự thiếu hiểu biết rõ ràng, sự si mê, sự mê muội, sự mê lầm, vô minh, dòng lũ vô minh, ách vô minh, khuynh hướng tiềm ẩn của vô minh, sự ám ảnh của vô minh, then cài của vô minh, sự si mê, gốc rễ bất thiện
diṭṭhi diṭṭhigataṃ … vipariyāsaggāho = quan điểm, sự mắc kẹt trong các quan điểm, rừng rậm quan điểm, hoang mạc quan điểm, sự quanh co của quan điểm, sự dao động của quan điểm, xiềng xích quan điểm, sự nắm giữ, sự bám chặt, sự cố chấp, sự hiểu sai lệch, con đường lệch lạc, lối đi sai lầm, sự sai lầm, nền tảng của các học thuyết ngoại đạo, sự nắm giữ điều đảo ngược
kaṅkhā kaṅkhāyanā … manovilekho = sự nghi ngờ, sự khởi nghi ngờ, trạng thái khởi nghi ngờ, sự phân vân, sự hoài nghi, sự lưỡng lự, sự đứng trước ngã ba đường, sự ngờ vực, sự không nắm giữ được điều chắc chắn, sự chần chừ, sự do dự, sự không đi sâu, trạng thái cứng đờ của tâm, sự giằng xé trong ý
cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa = sự xao động của tâm, sự không lắng xuống, sự tán loạn của tâm, trạng thái rối loạn của tâm
na hirīyati hiriyitabbena na hirīyati … = người ta không hổ thẹn với điều đáng hổ thẹn, không hổ thẹn khi để các hiện tượng xấu ác, bất thiện xảy ra nơi mình
na ottappati ottappitabbena na ottappati … = người ta không ghê sợ điều đáng ghê sợ, không ghê sợ khi để các hiện tượng xấu ác, bất thiện xảy ra nơi mình
single words: gāha = sự nắm giữ; abhinivesa = sự cố chấp; anusaya = khuynh hướng tiềm ẩn; pariyuṭṭhāna = sự ám ảnh; vikkhepa = sự tán loạn; avūpasama = sự không lắng xuống; apariyogāhanā = sự không đi sâu (in both the moha and the vicikicchā string)
Variants at ^1-381: patiṭṭhāho [dị bản (Sī., Syā.): paṭiggāho] (a different word); vipariyāsaggāho [khác chính tả (Ka.): vipariyesagāho]

## Choices to review
sukhindriyaṃ = «năng lực dễ chịu» (sukha as a feeling quality; the factor sukhaṃ stays «hạnh phúc» in ^1-443 ff., as identical Pāli).
dukkhaṃ (factor) = «sự đau khổ» (antonym of the factor «hạnh phúc»); the feeling string keeps «khó chịu».
cakkhuviññāṇa etc. = «thức qua mắt …» (plain; «nhãn thức» is specialist).
diṭṭhivisūkāyikaṃ / diṭṭhivipphanditaṃ = «sự quanh co của quan điểm» / «sự dao động của quan điểm»; titthāyatanaṃ = «nền tảng của các học thuyết ngoại đạo».

## Source points translated as written
^1-377: the answer ends with «hoti?» («… đây là năng lực định tâm vào lúc ấy?»), kept like ^1-33 / ^1-135.
^1-473: the question ends with «hoti.» instead of «hoti?»; the Vietnamese question ends with «.» («Vào lúc ấy, chủ ý là gì.»).
^1-381: «patiṭṭhāho [paṭiggāho (sī. syā.)]»: patiṭṭhāho may be a slip for paṭiggāho; rendered as written («sự bám chặt»), the bracket keeps paṭiggāho.
^1-429 («uddhaccaṃ hoti …pe… ye vā pana») and ^1-498 («avikkhepo hoti …pe… ime»): stray space before «…pe…»; spacing mirrored, as in 2-02 / 2-03.
^1-433: the feeling of eye-consciousness is defined with the mental string (cetasikaṃ … cetosamphassajaṃ …), while ^1-445 (body-consciousness) has the bodily string; kept as written.
^1-501 … ^1-504: the immaterial absorptions lack «upekkhāsahagataṃ» (unlike 2-02 ^1-265 ff.); nothing added.
^1-397, 400, 407, 410, 419, 425, 429, 441, 453, 467, 482, 496 and ^1-405 … 418, 423, 424, 428: «…pe….» = «….» (four dots), as 2-02 / 2-03.
