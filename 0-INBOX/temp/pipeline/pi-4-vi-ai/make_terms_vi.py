# -*- coding: utf-8 -*-
"""Writes vi-zeroshot-terms.md from the constants of build_sample_vi.py (so the list cannot drift from the builder).

usage: python -I -X utf8 make_terms_vi.py
"""
import pathlib
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-4-vi-ai")
sys.path.insert(0, str(HERE))
import build_sample_vi as S  # noqa: E402

P1, P2, P3, NEW = "pi-1", "pi-2", "pi-3", "new"
# source of each person name: exact phrase in the rails (pi-N), built from a pi-N noun (pi-N noun), or new
SRC = {
    "puthujjano": P1 + "/" + P2, "sekkho": P2, "asekkho": P2, "nevasekkhanāsekkho": "new (from pi-2 sekkha / asekkha)",
    "sammāsambuddho": P1, "arahā": P1, "sotāpanno": "pi-1 core", "sakadāgāmī": "new (pi-2 «trở lại một lần»)",
    "anāgāmī": "new (pi-2 «không trở lại»)", "ariyo": "pi-1 core (ariya person «bậc thánh»)",
    "anariyo": "new (pi-1 core «bậc thánh»)", "tevijjo": "new (pi-1 «ba loại hiểu biết chân thật»)",
    "chaḷabhiñño": "new (pi-2 «sáu loại hiểu biết trực tiếp»)",
    "sotāpattiphalasacchikiriyāya paṭipanno": "new (pi-2 «thành quả vào dòng», pi-1/2 «tự mình chứng nghiệm»)",
    "sakadāgāmiphalasacchikiriyāya paṭipanno": "new (pi-2 «thành quả trở lại một lần»)",
    "anāgāmiphalasacchikiriyāya paṭipanno": "new (pi-2 «thành quả không trở lại»)",
    "arahattaphalasacchikiriyāya paṭipanno": "new (pi-2 «thành quả A-la-hán»)",
    "asaṅkhāraparinibbāyī": "new (pi-1 «có sự thúc đẩy», pi-2 «nhập Niết-bàn trọn vẹn»)",
    "sasaṅkhāraparinibbāyī": "new (pi-1 «có sự thúc đẩy», pi-2 «nhập Niết-bàn trọn vẹn»)",
    "bhabbāgamano": "new (pi-2 bhabba «có khả năng»)", "abhabbāgamano": "new (pi-2 abhabba «không có khả năng»)",
    "niyato": "new (pi-1 niyata «cố định»)", "aniyato": "new (pi-1 niyata «cố định»)",
    "cetanābhabbo": "new (core cetanā «chủ ý»)",
    "kodhano": "pi-2 noun (kodha «sự giận dữ»)", "upanāhī": "pi-2 noun (upanāha «sự ôm hận»)",
    "makkhī": "pi-2 noun (makkha «sự gièm pha»)", "paḷāsī": "pi-2 noun (paḷāsa «sự ganh đua»)",
    "issukī": "pi-2 noun (issā «sự ganh tị»)", "maccharī": "pi-2 noun (macchariya «sự keo kiệt»)",
    "saṭho": "pi-2 noun (sāṭheyya «sự gian xảo»)", "māyāvī": "pi-2 noun (māyā «sự xảo trá»)",
    "ahiriko": P2, "anottappī": P2, "hirimā": "pi-1 noun (hirī «sự biết hổ thẹn»)",
    "ottappī": "pi-1 noun (ottappa «sự biết ghê sợ tội lỗi»)",
    "dubbaco": "pi-1 noun (dovacassatā «sự khó dạy bảo»)", "suvaco": "pi-1 noun (sovacassatā «sự dễ dạy bảo»)",
    "pāpamitto": "pi-1 noun (pāpamittatā)", "kalyāṇamitto": "pi-1 noun (kalyāṇamittatā)",
    "indriyesu aguttadvāro": "pi-1 noun (indriyesu aguttadvāratā)",
    "indriyesu guttadvāro": "pi-1 noun (indriyesu guttadvāratā)",
    "bhojane amattaññū": "pi-1 noun (bhojane amattaññutā)", "bhojane mattaññū": "pi-1 noun (bhojane mattaññutā)",
    "muṭṭhassati": P2, "upaṭṭhitassati": P2, "asampajāno": "pi-1 noun (asampajañña)",
    "sampajāno": "pi-1 noun (sampajañña)", "sīlavipanno": "pi-1 noun (sīlavipatti)",
    "diṭṭhivipanno": "pi-1 noun (diṭṭhivipatti)", "sīlasampanno": "pi-1 noun (sīlasampadā)",
    "diṭṭhisampanno": P2, "ajjhattasaṃyojano": "pi-2 noun (ajjhattasaṃyojana)",
    "bahiddhāsaṃyojano": "pi-2 noun (bahiddhāsaṃyojana)", "hīnādhimutto": "pi-2 («có chí hướng thấp kém»)",
    "paṇītādhimutto": "pi-2 («có chí hướng ưu việt»)", "akkodhano": "pi-2 noun", "anupanāhī": "pi-2 noun",
    "amakkhī": "pi-2 noun", "apaḷāsī": "pi-2 noun", "anissukī": "pi-2 noun", "amaccharī": "pi-2 noun",
    "asaṭho": "pi-2 noun", "amāyāvī": "pi-2 noun",
    "vijjūpamacitto": "pi-1 («giống như tia chớp»)", "vajirūpamacitto": "pi-1 («giống như kim cương»)",
    "asappuriso": "pi-1 («người chân chính»)", "sappuriso": P1,
    "suppameyyo": "new (pi-2 «không thể đo lường»)", "duppameyyo": "new", "appameyyo": "pi-2 («không thể đo lường»)",
    "appassuto sutena anupapanno": "new (pi-2 «ít học hỏi»)", "appassuto sutena upapanno": "new (pi-2 «ít học hỏi»)",
    "bahussuto sutena anupapanno": "new (pi-1 «học hỏi nhiều»)",
    "bahussuto sutena upapanno": "new (pi-1 «học hỏi nhiều»)",
    "sarāgo": "new (pi-1 nouns)", "sadoso": "new (pi-1 nouns)", "samoho": "new (pi-1 nouns)", "samāno": "new (pi-1 nouns)",
    "tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo": "new (pi-1 «bà-la-môn»)",
}


def src(p):
    return SRC.get(p, NEW)


def main():
    o = []
    a = o.append
    a("# pi-4 Vietnamese zero-shot: settled formulas and terms (sample: preamble, ch1 matrix, ch2 single persons)")
    a("")
    a("Format: Pāli = tiếng Việt | source. Sources: pi-1 / pi-2 / pi-3 = exact wording in that book's reviewed "
      "Vietnamese rails (asserted by build_sample_vi.py at build time); «pi-N noun» = person name formed from the "
      "approved pi-N abstract noun; new = settled in this sample. Chapter agents import "
      "build_sample_vi.py and use NAME[…], the frames and the headings VERBATIM. Names are lowercase constants; "
      "cap() only at the start of a list item or sentence.")
    a("")
    a("## Book frame")
    a(f"Namo tassa bhagavato arahato sammāsambuddhassa = {S.HOMAGE} | pi-1/pi-2/pi-3")
    a(f"Abhidhammapiṭake = {S.PITAKA} | pi-1/pi-2/pi-3")
    a(f"Puggalapaññattipāḷi (book title, proposed) = {S.BOOK_TITLE} | new")
    a(f"Book title, alternatives = {S.BOOK_TITLE_ALTERNATIVES[0]}; {S.BOOK_TITLE_ALTERNATIVES[1]} | new")
    a(f"paññatti (designation sense, whole book) = {S.PANNATTI} | new (pi-1 «khái niệm» = the 'concept' sense "
      "in Dhammasaṅgaṇī; pi-1 uses «sự định danh» for saṅkhā in the synonym string ^1-1313–1315)")
    a(f"Puggalapaññattimātikā niṭṭhitā. = {S.MATIKA_END} | new (pattern pi-1 «Bộ “…” đã hoàn tất.»)")
    a(f"Puggalapaññattipakaraṇaṃ niṭṭhitaṃ. (ch11) = {S.BOOK_END} | pi-1 pattern")
    a("")
    a("## Chapter and section headings (all chapters)")
    a(f"### Mātikā = ### {S.MATIKA} | pi-1")
    for n, p in zip(range(1, 11), ("Ekaka", "Duka", "Tika", "Catukka", "Pañcaka", "Chakka", "Sattaka", "Aṭṭhaka",
                                    "Navaka", "Dasaka")):
        a(f"#### {p}uddeso = #### {S.UDDESA_HEADING[n]} | new (pi-1/pi-3 Uddeso «Phần nêu đề mục»)")
    a(f"### Niddeso = ### {S.NIDDESO} | new")
    for n, p in zip(range(2, 12), ("Ekaka", "Duka", "Tika", "Catukka", "Pañcaka", "Chakka", "Sattaka", "Aṭṭhaka",
                                    "Navaka", "Dasaka")):
        a(f"#### {p}puggalapaññatti (ch{n}) = #### {S.CHAPTER_HEADING[n]} | new")
    for n, p in zip(range(1, 11), ("Ekakaṃ", "Dukaṃ", "Tikaṃ", "Catukkaṃ", "Pañcakaṃ", "Chakkaṃ", "Sattakaṃ",
                                    "Aṭṭhakaṃ", "Navakaṃ", "Dasakaṃ")):
        a(f"{p}. (matrix group closer) = {S.MATIKA_GROUP_CLOSER[n]} | pi-1")
    for n, p in zip(range(1, 11), ("Ekaka", "Duka", "Tika", "Catukka", "Pañcaka", "Chakka", "Sattaka", "Aṭṭhaka",
                                    "Navaka", "Dasaka")):
        a(f"{p}niddeso. (chapter closer) = {S.NIDDESA_CLOSER[n]} | pi-1/pi-2")
    a("")
    a("## Frames")
    a("Cha paññattiyo – khandhapaññatti … puggalapaññattīti. = Sáu sự định danh – sự định danh về các khối, … , "
      "sự định danh về các hạng người. | new")
    a(f"Kittāvatā X-ānaṃ X-paññatti? = {S.DESIGNATION_Q.format(x='{X}')} | new")
    a(f"Yāvatā N X – …; ettāvatā X-ānaṃ X-paññatti. = {S.DESIGNATION_A.format(x='{X}', n='{N X}', items='…')} | new")
    a(f"Dve / Tayo … Dasa puggalā – = {S.GROUP_OPENER[2]} / {S.GROUP_OPENER[3]} … {S.GROUP_OPENER[10]} | new")
    a(f"puggalā (counted as types) = {S.PUGGALA_TYPES}; puggala = {S.PUGGALA} | pi-1 core + new classifier")
    a("N X-ūpamā puggalā = N hạng người giống như X (TYPES_COUNT[n], e.g. «" + S.TYPES_COUNT[4]
      + " giống như mây mưa.») | new (pi-1 «giống như» for -ūpamā)")
    a("X ca, Y ca. (duka item) = X và Y. | new (pi-2 list style)")
    a(f"Katamo ca puggalo X? = {S.DEF_Q.format(name='X')} | new")
    a(f"Idhekacco (puggalo) = {S.IDHEKACCO} | pi-1")
    a(f"Atthekacco puggalo = {S.ATTHEKACCO} | pi-2 («có người hành thiền»)")
    a(f"– ayaṃ vuccati puggalo \"X\". = {S.DEF_CLOSE.format(name='X')} | new")
    a(f"Ayaṃ vuccati puggalo \"X\". (no dash) = {S.DEF_CLOSE_NODASH.format(name='X')} | new")
    a(f"– ime vuccanti puggalā \"X\". = {S.DEF_CLOSE_PL.format(name='những X')} | new")
    a(f"Tattha katamo / katamā / katamaṃ X? = {S.TATTHA_Q.format(x='X')} | pi-1/pi-2")
    a(f"– ayaṃ / idaṃ vuccati X. (noun, no quotes) = {S.THING_CLOSE.format(x='X')} | pi-1")
    a(f"samannāgato = {S.SAMANNAGATO} (bad states and āvaraṇa: «mang …», pi-2 ^2-826) | pi-2")
    a(f"Ṭhānaṃ kho panetaṃ vijjati, yaṃ = {S.THANA} | pi-2")
    a(f"Aṭṭhānametaṃ anavakāso yaṃ = {S.ATTHANA} | pi-2")
    a(f"aṭṭha vimokkhe kāyena phusitvā viharati = {S.VIMOKKHA} | new (pi-2 «tám sự giải thoát»)")
    a(f"paññāya cassa disvā (ekacce) āsavā parikkhīṇā honti = {S.PANNAYA_SOME} / {S.PANNAYA_ALL} | new")
    a(f"lābhī hoti rūpasahagatānaṃ vā arūpasahagatānaṃ vā samāpattīnaṃ = {S.SAMAPATTI_LABHI} | new (pi-2 «thành tựu thiền»)")
    a(f"(na) nikāmalābhī … samāpajjatipi vuṭṭhātipi = {S.NIKAMA_NEG} / {S.NIKAMA_POS} | new (pi-2 «chứng nhập / xuất khỏi»)")
    a(f"Sabbepi ariyapuggalā ariye vimokkhe X-ā. = {S.ARIYE_VIMOKKHE.format(pl='những X')} | new")
    a(f"\"idaṃ dukkha\"nti … yathābhūtaṃ pajānāti = {S.SACCA_PAJANATI} | pi-2 wording")
    a(f"Tathāgatappaveditā cassa dhammā paññāya vodiṭṭhā honti vocaritā = {S.TATHAGATA_DHAMMA} | new")
    a(f"pubbe ananussutesu dhammesu sāmaṃ saccāni (an)abhisambujjhati = {S.ANANUSSUTA} / {S.NA_ANANUSSUTA} | new")
    a(f"sabbaññutaṃ pāpuṇāti; balesu vasībhāvaṃ = {S.SABBANNUTA}; {S.VASIBHAVA} | new")
    a(f"tiṇṇaṃ saṃyojanānaṃ parikkhayā sotāpanno hoti avinipātadhammo niyato sambodhiparāyano = {S.SOTAPANNA_BASE} | new")
    a(f"pañcannaṃ orambhāgiyānaṃ saṃyojanānaṃ parikkhayā opapātiko hoti, tattha parinibbāyī anāvattidhammo tasmā lokā = "
      f"{S.ANAGAMI_BASE} | new (pi-2 «năm xiềng xích thuộc phần thấp», «nhập Niết-bàn trọn vẹn»)")
    a(f"ariyamaggaṃ sañjaneti upariṭṭhimānaṃ saṃyojanānaṃ pahānāya = {S.UPARITTHIMA} | new")
    a(f"X-phalasacchikiriyāya paṭipanno = {S.PATIPANNO_FOR.format(x='X')} | new (pi-2 phala names)")
    a(f"kāmarāgabyāpādānaṃ tanubhāvāya = {S.KAMARAGA_TANU} | pi-1")
    a(f"kāmarāgabyāpādānaṃ anavasesappahānāya = {S.KAMARAGA_PAHANA} | pi-1")
    a(f"rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya = {S.UDDHAM_PAHANA} | pi-1")
    a(f"kammāvaraṇena samannāgatā … duppaññā = {S.AVARANA_NEG} | pi-2 ^2-826 (+ eḷā «đần độn»)")
    a(f"na kammāvaraṇena … paññavanto = {S.AVARANA_POS} | pi-2 ^2-827 (+ aneḷā «không đần độn»)")
    a(f"(a)bhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ = {S.NIYAMA} / {S.NA_NIYAMA} | pi-2")
    a(f"tiṇṇo pāraṅgato thale tiṭṭhati (brāhmaṇo) = {S.TINNO} (bà-la-môn) | new")
    a(f"diṭṭheva dhamme = {S.DITTHEVA_DHAMME} | pi-2")
    a(f"dukkhassantaṃ karoti / dukkhassantakaro = đi đến tận cùng của khổ đau / {S.DUKKHASSANTAKARO} | new "
      "(kept apart from nirodha «sự chấm dứt»)")
    a("")
    a("## Person names by chapter (NAME[…] in build_sample_vi.py)")
    a("### Ekaka (matrix ^4-M-7, defined in ch2)")
    seen = set()
    for i, (p, v) in enumerate(S.EKAKA, 1):
        if p in seen:
            continue
        seen.add(p)
        a(f"{p} = {v} | {src(p)}")
    a(f"ch2 plurals: abhabbāgamanā = {S.PLURAL['abhabbāgamanā']}; bhabbāgamanā = {S.PLURAL['bhabbāgamanā']}; "
      f"sekkhā = {S.PLURAL['sekkhā']} | new")
    a(f"maggasamaṅgī = {S.MAGGASAMANGI}; phalasamaṅgī = {S.PHALASAMANGI} | pi-1 ^1-1373")
    a("")
    a("### Duka (matrix ^4-M-8, defined in ch3)")
    for it in S.DUKA:
        if isinstance(it, tuple):
            a(f"{it[0]} = {it[1]} | {src(it[0])}")
            a(f"{it[2]} = {it[3]} | {src(it[2])}")
        else:
            a(f"(sentence item) = {it} | new")
    a("")
    for title, d in (("Tika (matrix ^4-M-9, defined in ch4)", S.TIKA_NAMES),
                     ("Catukka (matrix ^4-M-10, defined in ch5)", S.CATUKKA_NAMES),
                     ("Pañcaka (matrix ^4-M-11, defined in ch6)", S.PANCAKA_NAMES)):
        a(f"### {title}")
        for p, v in d.items():
            a(f"{p} = {v} | {src(p)}")
        a("")
    a("### Similes (X-ūpamā puggalā = «N hạng người giống như X»)")
    for p, v in S.SIMILE.items():
        a(f"{p} = {v} | new")
    a("")
    a("### Sattaka (^4-M-13 (1), defined in ch8): " + "; ".join(S.SATTAKA_UDAKA) + " | new")
    a("Sattaka (2), Navaka: reuse the Ekaka names; Aṭṭhaka: «Bốn người có được con đường, bốn người có được "
      "thành quả.»; Dasaka: «Năm người đạt đến đích ngay ở đây, năm người đạt đến đích sau khi rời khỏi nơi đây.» | new")
    a("")
    a("## Terms")
    for line in (
        "dhamma = hiện tượng; the Teaching = Giáo Pháp (dhammānusārī, Tathāgatappaveditā dhammā) | pi-1 core",
        "pubbe ananussutesu dhammesu = trong những điều chưa từng được nghe trước đây | new",
        "khandha / āyatana / dhātu / sacca / indriya = khối / lĩnh vực nhận biết / yếu tố / sự thật / năng lực | pi-1 core",
        "the five / twelve / eighteen / four / twenty-two lists = pi-2 ^2-1 / pi-1 ^1-1342 / pi-2 ^2-183 / pi-2 ^2-982 / pi-2 ^2-221 | pi-1/pi-2",
        "puggala = người; ariyapuggala = bậc thánh; ariya (adj.) = cao quý | pi-1 core",
        "samāpatti = thành tựu thiền; samāpajjati / vuṭṭhāti = chứng nhập / xuất khỏi | pi-2",
        "vimokkha = sự giải thoát; cetovimutti = sự giải thoát của tâm; paññāvimutti = sự giải thoát nhờ trí tuệ | pi-2",
        "āsava = ô nhiễm; āsavā parikkhīṇā = các ô nhiễm được diệt tận; āsavānaṃ khaya = sự diệt tận các ô nhiễm | pi-1",
        "āsavapariyādāna / jīvitapariyādāna = sự kết thúc các ô nhiễm / sự kết thúc mạng sống | new",
        "saṃyojana = xiềng xích; orambhāgiya = thuộc phần thấp; upariṭṭhima = cao hơn | pi-1/pi-2 + new",
        "pahāna / pahīna = dứt bỏ / đã được dứt bỏ; anavasesa = không còn sót lại; aparisesa = không còn dư sót | pi-1 + new",
        "pamāda = sự buông thả; kuppati = bị lay chuyển; parihāyati = sa sút | pi-2 + new",
        "anusañceteti = luôn hướng chủ ý đến; anurakkhati = gìn giữ | new",
        "sekkha / asekkha = người còn đang tu học / người đã hoàn tất tu học | pi-2",
        "vijjā = hiểu biết chân thật; abhiññā = hiểu biết trực tiếp | pi-1/pi-2",
        "sacchikiriyā = sự tự mình chứng nghiệm; phala = thành quả; magga = con đường; ariyamagga = con đường cao quý | pi-1/pi-2",
        "paññindriya / saddhindriya adhimatta = năng lực trí tuệ / năng lực niềm tin vượt trội | pi-2 + new",
        "opapātika = hóa sinh; parinibbāyī = nhập Niết-bàn trọn vẹn; sasaṅkhāra / asaṅkhāra = có / không có sự thúc đẩy | pi-1/pi-2",
        "Avihā / Atappā / Sudassā / Sudassī / Akaniṭṭhā = cõi Vô Phiền / Vô Nhiệt / Thiện Hiện / Thiện Kiến / Sắc Cứu Cánh | new (established names, as pi-2 «Phạm Chúng»)",
        "cuta = chết (từ cõi …); āyuppamāṇa = tuổi thọ; deva / mānusa = chư thiên / loài người | pi-2",
        "kappa = kiếp; uḍḍayhati = bị thiêu hủy | pi-1 core + new",
        "sabbaññutā = sự toàn tri; bala = sức mạnh; vasībhāva = sự làm chủ; sāvakapāramī = sự toàn hảo của hàng đệ tử | pi-2 + new",
        "kāmarāga / byāpāda / rūparāga / arūparāga / māna / uddhacca / avijjā = sự tham đắm dục lạc / ác ý / sự tham đắm cõi hình sắc / … cõi không hình sắc / sự kiêu mạn / sự xao động / vô minh | pi-1",
        "pasāda = lòng tin trong sáng; paṭibhāna = tài ứng đáp; satthā = bậc đạo sư; samaṇa / brāhmaṇa = sa-môn / bà-la-môn | pi-1/pi-2",
        "uṭṭhāna = công sức (kept apart from vāyāma / padhāna «nỗ lực» and vīriya «tinh tấn»); puñña = phước | new / pi-2",
        "vippaṭisārī = ăn năn (kept apart from kukkucca «hối tiếc»); ārabhati = phạm lỗi | new",
        "samatha / vipassanā = sự tĩnh lặng / sự thấu suốt; adhipaññā = trí tuệ cao thượng | pi-1 + new",
        "sevitabbo bhajitabbo payirupāsitabbo = đáng gần gũi, đáng kết giao, đáng thân cận (pi-2 «gần gũi, kết giao, thân cận») | pi-2 + new",
        "a. ni. N.N (inside variant brackets) = Tăng Chi Bộ Kinh N.N | pi-2",
        "Kāsi = xứ Ca-thi | new",
    ):
        a(line)
    text = unicodedata.normalize("NFC", "\n".join(o) + "\n")
    (HERE / "vi-zeroshot-terms.md").write_bytes(text.encode("utf-8"))
    print("wrote", HERE / "vi-zeroshot-terms.md", len(o), "lines")


if __name__ == "__main__":
    main()
