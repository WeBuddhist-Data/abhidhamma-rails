def _notep_mine():
    cn, cd, N = F.cname, F.cond, F.N
    nine, two, three, four = CNT["nava"], CNT["dve"], CNT["tīṇi"], CNT["cattāri"]
    lok = F.cname("upanissaya") + "၌ " + B.LOKUTTARA + " " + NATTHI
    return {
        # kilesa dyads
        "(arūpe dosamūlakaṃ natthi)": f"({ARUPE} {DOSA}{F.MULAKA} {NATTHI})",
        "(evaṃ navapi pañhā kātabbā)": f"({EVAM_T} {PANHA} {nine}လုံးကို {KAT})",
        "(Evaṃ sabbe paccayā kātabbā.)": f"({EVAM_T} {F.PACCAYA} {SAB}ကို {KAT}{END})",
        "(Evaṃ itare dve gaṇanāpi sahajātavāropi kātabbo.)":
            f"({EVAM_T} {ITARE} {GANANA} {two}ကိုလည်း{C} {VARA('sahajāta')}ကိုလည်း {KAT}{END})",
        "(Ārammaṇapaccaye nokilesamūle pañca viññāṇā kātabbā.)":
            f"({cd('ārammaṇa', 'loc')} {NOKIL} {DHAMMA}{F.MULAKA}၌ {PANCAV}ကို {KAT}{END})",
        "(Cakkaṃ. Evaṃ nava pañhā kātabbā.)": f"({CAKKA}{END} {EVAM_T} {PANHA} {nine}ကို {KAT}{END})",
        "(evaṃ nahetupañhā cattāri kātabbā.)": f"({EVAM_T} {cd('hetu', 'n', True)}၏ {PANHA} {four}ကို {KAT}{END})",
        "(saṃkhittaṃ. Vitthāretabbaṃ.)": f"({SAMKH}{END} {VITTH}{END})",
        "(saṃkhittaṃ. Sahajātaṃ sahajātasadisaṃ, purejātaṃ purejātasadisaṃ.)":
            (f"({SAMKH}{END} {N['sahajāta']}သည် {N['sahajāta']}{SADISA}{C} {N['purejāta']}သည် "
             f"{N['purejāta']}{SADISA}{END})"),
        "(yathā lokiyadukaṃ, evaṃ ninnānākaraṇaṃ.)": f"({LOKIYA}{KAYYA} {EVAM} {NINNANAKARANA}{END})",
        "(Yathā lokiyadukaṃ, evaṃ ninnānākaraṇaṃ.)": f"({LOKIYA}{KAYYA} {EVAM} {NINNANAKARANA}{END})",
        "(Kilesasampayuttadukaṃ saṃkiliṭṭhadukasadisaṃ, ninnānākaraṇaṃ.)":
            f"({DN['Kilesasampayuttadukaṃ']}သည် {DN['Saṃkiliṭṭhadukaṃ']}{SADISA}{C} {NINNANAKARANA}{END})",
        "(Evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi "
        "kilesadukasadisā. Ninnānākaraṇaṃ. Āmasanaṃ nānaṃ.)":
            (f"({EVAM_T} {_pi(*ALL6)} {KILD}{SADISANI}{END} {NINNANAKARANA}{END} {AMASANA}သည် {K.NANAKARANA} "
             f"ဖြစ်သည်{END})"),
        "(evaṃ cattāri, kilesadukasadisaṃ.)": f"({EVAM_T} {four}{C} {KILD}{SADISA}{END})",
        "(itare dve kilesadukasadisā, ghaṭanārammaṇāpi kilesadukasadisā)":
            f"({ITARE} {two}သည် {KILD}{SADISANI}{C} {GHATANA} {N['ārammaṇa']}တို့သည်လည်း {KILD}{SADISANI})",
        "(Itare dvepi kilesadukasadisā. Ghaṭanādhipatipi.)":
            f"({ITARE} {two}လုံးလည်း {KILD}{SADISANI}{END} {GHATANA} {ADH}လည်း{END})",
        "(kilesadukasadisā)": f"({KILD}{SADISANI})",
        "(Itare dve anantarā kilesadukasadisā, ninnānākaraṇā. Ghaṭanānantarampi sabbe paccayā kilesadukasadisā, "
        "ninnānākaraṇā. Upanissaye lokuttaraṃ natthi, idaṃ dukaṃ kilesadukasadisaṃ, ninnānākaraṇaṃ.)":
            (f"({ITARE} {N['anantara']} {two}သည် {KILD}{SADISANI}{C} {NINNANAKARANA}{END} {GHATANA} "
             f"{N['anantara']}လည်း{C} {F.PACCAYA} {SAB}တို့သည် {KILD}{SADISANI}{C} {NINNANAKARANA}{END} {lok}{C} "
             f"ဤ {DUKA}သည် {KILD}{SADISA}{C} {NINNANAKARANA}{END})"),
        "(Evaṃ itare dve gaṇanāpi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi "
        "paṭiccavārasadisā.)":
            (f"({EVAM_T} {ITARE} {GANANA} {two}လည်း{C} {_pi(*ALL6[1:])} {PATICCA_V}{SADISANI}{END})"),
        "(Itarepi tīṇi kātabbā.)": f"({ITARE} {three}ကိုလည်း {KAT}{END})",
        "(Dve adhipati tīṇipi kātabbā, itare dvepi tīṇi kātabbā.)":
            f"({ADH} {two}၌ {three}လုံးကို {KAT}{C} {ITARE} {two}လုံး၌လည်း {three}ကို {KAT}{END})",
        "(navapi kātabbā, āvajjanāpi vuṭṭhānampi natthi)":
            f"({nine}လုံးကို {KAT}{C} {AVAJJ}လည်း{C} {VUTTH}လည်း {NATTHI})",
        "(purejātapaccayo pacchājātapaccayopi natthi)": f"({cn('purejāta')}{C} {cn('pacchājāta')}လည်း {NATTHI})",
        "(Navapi, tīṇiyeva padā kātabbā.)": f"({nine}လုံး{C} {PADA} {three}ကိုသာ {KAT}{END})",
        "(Kilesasaṃkiliṭṭhadukasadisaṃ ninnānākaraṇaṃ, sabbe vārā.)":
            f"({DN['Kilesasaṃkiliṭṭhadukaṃ']}{SADISA}{C} {NINNANAKARANA}{C} {VARAS} {SAB}{END})",
        # piṭṭhiduka: dassanena / bhāvanāya pahātabba (-hetuka)
        "(Itare dve gaṇanāpi sahajātavāropi kātabbo.)":
            f"({ITARE} {GANANA} {two}ကိုလည်း{C} {VARA('sahajāta')}ကိုလည်း {KAT}{END})",
        "(Itare dve gaṇanāpi nissayavāropi kātabbo.)":
            f"({ITARE} {GANANA} {two}ကိုလည်း{C} {VARA('nissaya')}ကိုလည်း {KAT}{END})",
        "(yathā dassanadukaṃ, evaṃ vitthāretabbaṃ, ninnānākaraṇaṃ)":
            f"({DASSD}{KAYYA} {EVAM} {VITTH}{C} {NINNANAKARANA})",
        "(Paccayavārapaccanīye nahetupaccaye uddhaccasahagate tīṇi, moho uddharitabbo. Sabbepi vārā "
        "dassanadukasadisā, uddhaccapaccanīyampi nānaṃ.)":
            (f"({VARA('paccaya')}၏ {ORD['paccanīyaṃ']}၌ {cd('hetu', 'loc', True)} {UDDH_SAH} {DHAMMA}၌ {three}{C} "
             f"{MOHA}ကို {UDDHAR}{END} {VARAS} {SAB}လည်း {DASSD}{SADISANI}{C} {F.LEX['uddhaccaṃ'][0]}၏ "
             f"{ORD['paccanīyaṃ']}လည်း {K.NANAKARANA} ဖြစ်သည်{END})"),
        "(dassanadukasadisā bhāvanā ninnānākaraṇā)": f"({DASSD}{SADISANI}{C} {BHAVANA}{C} {NINNANAKARANA})",
        "(Sabbapaccayā dassanadukasadisā, bhāvanā ninnānākaraṇā.)":
            f"({F.PACCAYA} {SAB}တို့သည် {DASSD}{SADISANI}{C} {BHAVANA}{C} {NINNANAKARANA}{END})",
        "(Paccanīyavibhaṅgo dassanadukasadiso vibhajitabbo. Evaṃ tīṇi gaṇanāpi gaṇetabbā.)":
            (f"({PACC_VIBH}ကို {DASSD}နှင့် တူအောင် {VIBHAJ}{END} {EVAM_T} {GANANA} {three}ကိုလည်း {GAN}{END})"),
        "(Avasesesu dvīsu anantarūpanissayo, pakatūpanissayo.)":
            f"({AVAS_O} {two}၌ {F.LEX['anantarūpanissayo'][0]}{C} {F.LEX['pakatūpanissayo'][0]}{END})",
        "(Saṃkhittaṃ. Vatthupurejātaṃ saṃkhittaṃ.)": f"({SAMKH}{END} {F.LEX['vatthupurejātaṃ'][0]} {SAMKH}{END})",
        "(Vatthupurejātaṃ saṃkhittaṃ.)": f"({F.LEX['vatthupurejātaṃ'][0]} {SAMKH}{END})",
        "(Evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi dassanena "
        "pahātabbahetukadukasadisā. Uddhaccasahagato moho vicikicchāsahagatamohaṭṭhāne ṭhapetabbo.)":
            (f"({EVAM_T} {_pi(*ALL6)} {DASSHD}{SADISANI}{END} {UDDH_SAH} {MOHA}ကို {VICI_SAH} {MOHA}၏ နေရာ၌ "
             f"{THAPET}{END})"),
        "(dassanena pahātabbahetukadukasadisā)": f"({DASSHD}{SADISANI})",
        "(ārabbha dassanena pahātabbahetukadukasadisā)": f"({ARABBHA} {DASSHD}{SADISANI})",
        "(ghaṭanārammaṇā tīṇipi kātabbā)": f"({GHATANA} {N['ārammaṇa']} {three}လုံးကို {KAT})",
        "(Anantarapaccaye nabhāvanāya pahātabbahetukakāraṇā vicikicchāsahagato moho na kātabbo, uddhaccasahagato "
        "moho kātabbo.)":
            (f"({cd('anantara', 'loc')} {NBH_HT} {DHAMMA} ဖြစ်သည့် အကြောင်းကြောင့် {VICI_SAH} {MOHA}ကို {NAKAT}{C} "
             f"{UDDH_SAH} {MOHA}ကို {KAT}{END})"),
        "(ghaṭanūpanissayāpi tīṇipi kātabbā)": f"({GHATANA} {N['upanissaya']}လည်း {three}လုံးကို {KAT})",
        "(nabhāvanāya pahātabbabhājanakāraṇe nānākkhaṇikā labbhati )":
            f"({NBH} {DHAMMA}ကို {BHAJANA} {NANAKK}ကို {LABHATI})",
        "(Saṃkhittaṃ. Yathā dassanena pahātabbahetukadukaṃ evaṃ bhāvanāya pahātabbahetukapaccayāpi paccanīyāpi "
        "vibhāgopi gaṇanāpi ninnānākaraṇā.)":
            (f"({SAMKH}{END} {DASSHD}{KAYYA} {EVAM} {BHH_T} {DHAMMA}၏ {F.PACCAYA}တို့လည်း{C} "
             f"{ORD['paccanīyaṃ']}တို့လည်း{C} {VIBHAGA}လည်း{C} {GANANA}တို့လည်း {NINNANAKARANA}{END})"),
        "(Parantena sakabhaṇḍachandarāgopi kātabbo.)": f"({PARANTENA} {SAKABH}ကိုလည်း {KAT}{END})",
        '(Parantena "sakabhaṇḍachandarāgo"ti kātabbaṃ.)': f"({PARANTENA} “{SAKABH}”ဟု {KAT}{END})",
        # savitakka / savicāra
        "(Savitakkamūlakā avasesā dve pañhā kātabbā, ahetukaṃ ninnānaṃ.)":
            f"({SAVIT} {DHAMMA}{F.MULAKA}၌ {AVAS_O} {PANHA} {two}ကို {KAT}{C} {AHET_S}{C} {NINNANA}{END})",
        '(Saṃkhittaṃ. Hetupaccayasadisaṃ. "Ahetuka"nti niyāmetabbaṃ.)':
            f"({SAMKH}{END} {cn('hetu')}{SADISA}{END} “{AHET_S}”ဟု {NIYAM}{END})",
        "(Avasesā dve pañhā hetupaccayasadisā ninnānā, ahetukanti niyāmetabbaṃ.)":
            f"({AVAS_O} {PANHA} {two}သည် {cn('hetu')}{SADISANI}{C} {NINNANA}{C} {AHET_S}ဟု {NIYAM}{END})",
        "(paṭisandhiyāpi dve)": f"({F.PATISANDHI}၌လည်း {two})",
        "(paṭisandhiyāpi pavattisadisāyeva)": f"({F.PATISANDHI}၌လည်း {PAVATTI}{SADISA}ပင်)",
        "(paṭisandhikkhaṇe dve kātabbā)": f"({PS_KHANA} {two}ကို {KAT})",
        "(tīṇi, paṭisandhiyāpi)": f"({three}{C} {F.PATISANDHI}၌လည်း)",
        '(Nava pañhā kātabbā. "Ahetukā"ti niyāmetabbā tīṇiyeva. Moho uddharitabbo, yathā paṭiccavāre '
        "hetupaccayasadisāyeva pañhā pañcaviññāṇā atirekā moho vitakkaṃ.)":
            (f"({PANHA} {nine}ကို {KAT}{END} “{AHET_P}”ဟု {three}ကိုသာ {NIYAM}{END} {MOHA}ကို {UDDHAR}{C} "
             f"{PATICCA_V}၌ {cn('hetu')}နှင့် တူသော {PANHA}များပင် ဖြစ်သကဲ့သို့ {PANCAV} {ATIREKA}{C} {MOHA}{C} "
             f"{VITAKKA}{END})"),
        "(Evaṃ cha pañhā kātabbā anulomasadisā, ahetukāti niyāmetabbā, tīṇiyeva, moho uddharitabbo.)":
            (f"({EVAM_T} {PANHA} {CNT['cha']}ကို {KAT}{C} {ORD['anulomaṃ']}နှင့် တူကြသည်{C} {AHET_P}ဟု {NIYAM}{C} "
             f"{three}သာ{C} {MOHA}ကို {UDDHAR}{END})"),
        "(heṭṭhā likhitaṃ lekhaṃ iminā kāraṇena daṭṭhabbaṃ)":
            f"({B.NEW['heṭṭhā']} {LIKHITA} {LEKHA}ကို {D.IMINA} {DATTH})",
        "(tīṇipi upanissayā sabbattha kātabbā)": f"({N['upanissaya']} {three}လုံးကို {K.SABBATTHA} {KAT})",
        "(dutiyavāre likhitapadā sabbe kātabbā)": f"(ဒုတိယ {VARAS}၌ {LIKHITA} {PADA} {SAB}ကို {KAT})",
        "(tīṇi, pacchājātā)": f"({three}{C} {N['pacchājāta']})",
        "(Evaṃ cattāri, sahajātāpi nānākkhaṇikāpi kātabbā.)":
            f"({EVAM_T} {four}{C} {SAH_KAMMA}ကိုလည်း{C} {NANAKK}ကိုလည်း {KAT}{END})",
        "(paṭisandhikkhaṇe sahajātāpi dvepi kātabbā)": f"({PS_KHANA} {N['sahajāta']} {two}လုံးကိုလည်း {KAT})",
        "(paṭisandhikkhaṇe, tīṇi)": f"({PS_KHANA}{C} {three})",
        "(anulomamātikā vitthāretabbā)": f"({ANUL_MATIKA}ကို {VITTH})",
        "(Yathā savitakkadukaṃ, evaṃ kātabbaṃ, ninnānākaraṇaṃ. Idha magge cattāri kātabbāni. Savicāraduke imaṃ "
        "nānākaraṇaṃ.)":
            (f"({SAVD}{KAYYA} {EVAM} {KAT}{C} {NINNANAKARANA}{END} {IHA} {cd('magga', 'loc')} {four}ကို {KAT}{END} "
             f"{SAVICD}၌ ဤသည် {K.NANAKARANA} ဖြစ်သည်{END})"),
        # sappītika / pīti / sukha / upekkhā
        "(Yathā savitakkadukaṃ sabbattha, evaṃ sappītikadukaṃ kātabbaṃ, sabbattha pavattipaṭisandhi navapi pañhā.)":
            (f"({SAVD}{KAYYA} {K.SABBATTHA}{C} {EVAM} {SAPD}ကို {KAT}{C} {K.SABBATTHA} {PAV_PS} {PANHA} "
             f"{nine}လုံး{END})"),
        "(yāva asaññasattāpi)": f"({YAVA_AS}လည်း)",
        "(Saṃkhittaṃ. Yathā savitakkaduke anulomapaccayavāraṃ, evaṃ pavattipaṭisandhi nava pañhā paripuṇṇā pīti "
        "ninnānākaraṇā.)":
            (f"({SAMKH}{END} {SAVD}၌ {ORD['anulomaṃ']}၏ {VARA('paccaya')}{KAYYA} {EVAM} {PAV_PS} {PANHA} {nine} "
             f"{PARIP}ကြသည်{C} {PITI}{C} {NINNANAKARANA}{END})"),
        "(Pavattipaṭisandhi kātabbā paṭiccavārasadisā, yāva asaññasattā.)":
            f"({PAV_PS} {KAT}{C} {PATICCA_V}{SADISANI}{C} {YAVA_AS}{END})",
        "(Anulomasadisā nava pañhā, pavattiyeva paṭisandhi natthi, ekoyeva moho.)":
            (f"({ORD['anulomaṃ']}နှင့် တူသော {PANHA} {nine}{C} {PAVATTI}သာ{C} {F.PATISANDHI} {NATTHI}{C} {MOHA} "
             f"တစ်ခုတည်း{END})"),
        "(dutiyavārasadisaṃ)": f"(ဒုတိယ {VARAS}{SADISA})",
        "(tīṇipi upanissayā)": f"({N['upanissaya']} {three}လုံး)",
        "(sahajātāpi nānākkhaṇikāpi kātabbā… dve nānākkhaṇikā)":
            f"({SAH_KAMMA}ကိုလည်း{C} {NANAKK}ကိုလည်း {KAT}{PE} {NANAKK} {two})",
        "(saṃkhittaṃ. Savitakkadukasadisaṃ kātabbaṃ.)": f"({SAMKH}{END} {SAVD}နှင့် တူအောင် {KAT}{END})",
        "(Paccanīyavibhaṅgagaṇanāpi savitakkadukasadisā. Yadipi na sameti imaṃ anulomaṃ paccavekkhitvā gaṇetabbaṃ, "
        "itare dve gaṇanā gaṇetabbā.)":
            (f"({PACC_VIBH}နှင့် {GANANA}တို့သည်လည်း {SAVD}{SADISANI}{END} {YADIPI} {SAMEN}သော်လည်း ဤ "
             f"{ORD['anulomaṃ']}ကို {PACCAVEKKH} {GAN}{C} {ITARE} {GANANA} {two}ကို {GAN}{END})"),
        "(evaṃ pītisahagatadukaṃ vitthāretabbaṃ, sappītikadukasadisaṃ ninnānākaraṇaṃ, āmasanaṃ ninnānaṃ.)":
            (f"({EVAM_T} {PITID}ကို {VITTH}{C} {SAPD}{SADISA}{C} {NINNANAKARANA}{C} {AMASANA}သည် {NINNANA}{END})"),
        "(Evaṃ sukhasahagatadukaṃ vitthāretabbaṃ, yathā sappītikadukassa anulomapaṭiccavāro.)":
            f"({EVAM_T} {SUKD}ကို {VITTH}{C} {SAPD}၏ {ORD['anulomaṃ']}၏ {PATICCA_V}{KAYYA}{END})",
        "(Yathā sappītike nahetupaccayasadisaṃ, ninnānaṃ sabbatthameva nava pañhā.)":
            (f"({SAPT} {DHAMMA}၌{KAYYA} {cd('hetu', 'n', True)}{SADISA}{C} {NINNANA}{C} {K.SABBATTHA}ပင် {PANHA} "
             f"{nine}{END})"),
        "(Evaṃ itare dve gaṇanāpi sahajātavāropi paṭiccavārasadisā. Paccayavāre pavattipi paṭisandhipi "
        "vitthāretabbā, yathā sappītikadukapaccayavārapaccanīyepi pavatte vatthu ca vitthāretabbaṃ, yathā "
        "sappītikaduke ekoyeva moho, evaṃ itare dve gaṇanāpi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi yathā "
        "sappītikadukaṃ, evaṃ kātabbaṃ.)":
            (f"({EVAM_T} {ITARE} {GANANA} {two}လည်း{C} {VARA('sahajāta')}လည်း {PATICCA_V}{SADISANI}{END} "
             f"{VARA('paccaya')}၌ {PAVATTI}ကိုလည်း{C} {F.PATISANDHI}ကိုလည်း {VITTH}{C} {SAPD}၏ {VARA('paccaya')}၏ "
             f"{ORD['paccanīyaṃ']}၌လည်း{KAYYA} {PAVATTE} {F.VATTHU}ကို{F.LAKAUNG} {VITTH}{C} {SAPD}၌ {MOHA} "
             f"တစ်ခုတည်း ဖြစ်သကဲ့သို့{C} {EVAM_T} {ITARE} {GANANA} {two}ကိုလည်း{C} "
             f"{_pi_obj('nissaya', 'saṃsaṭṭha', 'sampayutta')} {SAPD}{KAYYA} {EVAM} {KAT}{END})"),
        "(Ārammaṇepi adhipatiyāpi sappītikadukasadisā, sukhanti nānākaraṇaṃ.)":
            (f"({cd('ārammaṇa', 'loc')}လည်း{C} {cd('adhipati', 'loc')}လည်း {SAPD}{SADISANI}{C} {SUKHA}ဟူ၍ "
             f"{K.NANAKARANA} ဖြစ်သည်{END})"),
        "(Mūlaṃ. Tīṇipi sappītikadukasadisā.)": f"({MULA}{END} {three}လုံး {SAPD}{SADISANI}{END})",
        "(dutiyagamanasadisaṃ)": f"(ဒုတိယ {GAMANA}{SADISA})",
        "(Cha kammāni cattāri sahajātāpi nānākkhaṇikāpi kātabbā, dve nānākkhaṇikā.)":
            (f"({N['kamma']} {CNT['cha']}{C} {four}၌ {SAH_KAMMA}ကိုလည်း{C} {NANAKK}ကိုလည်း {KAT}{C} {two}သည် "
             f"{NANAKK}{END})"),
        "(Evaṃ paccanīyavibhaṅgopi gaṇanāpi sappītikadukasadisaṃ kātabbaṃ, yadipi vimati atthi anulomaṃ passitvā "
        "gaṇetabbaṃ.)":
            (f"({EVAM_T} {PACC_VIBH}ကိုလည်း{C} {GANANA}တို့ကိုလည်း {SAPD}နှင့် တူအောင် {KAT}{C} {YADIPI} {VIMATI} "
             f"ရှိသော်လည်း {ORD['anulomaṃ']}ကို {PASSITVA} {GAN}{END})"),
        "(Sappītikadukasadisaṃ, anulome navapi pañhā.)": f"({SAPD}{SADISA}{C} {ORDL['anulome']} {PANHA} {nine}လုံး{END})",
        '(yathā savitakkadukasadisaṃ paccayavāre nānākaraṇaṃ. "Upekkha"nti navapi pañhā kātabbā, '
        "paṭisandhipavattipi vatthupi.)":
            (f"({SAVD}နှင့် တူသည့်အတိုင်း {VARA('paccaya')}၌ {K.NANAKARANA}{END} “{UPEKKHA}”ဟု {PANHA} {nine}လုံးကို "
             f"{KAT}{C} {F.PATISANDHI}၌လည်း{C} {PAVATTE}လည်း{C} {F.VATTHU}လည်း{END})"),
        "(Evaṃ navapi pañhā pavattipaṭisandhiyo yathā savitakkadukassa evaṃ kātabbā. Tīṇiyeva moho, pavatte vatthupi "
        "kātabbā.)":
            (f"({EVAM_T} {PANHA} {nine}လုံးကို {PAV_PS} {SAVD}၌{KAYYA} {EVAM} {KAT}{END} {MOHA} {three}သာ{C} "
             f"{PAVATTE} {F.VATTHU}ကိုလည်း {KAT}{END})"),
        "(Yathā savitakkadukaṃ sampayuttavāro evaṃ kātabbo.)":
            f"({SAVD}၏ {VARA('sampayutta')}{KAYYA} {EVAM} {KAT}{END})",
        "(Evaṃ pañca pañhā yathā savitakkaduke evaṃ kātabbā.)":
            f"({EVAM_T} {PANHA} {CNT['pañca']}ကို {SAVD}၌{KAYYA} {EVAM} {KAT}{END})",
        "(Evaṃ cattāri pañhā yathā savitakkadukassa.)": f"({EVAM_T} {PANHA} {four}{C} {SAVD}၌{KAYYA}{END})",
        '(Yathā sappītikadukaṃ evaṃ ārammaṇampi adhipatipi vitthāretabbā, "upekkhā"ti nānaṃ.)':
            (f"({SAPD}{KAYYA} {EVAM} {N['ārammaṇa']}ကိုလည်း{C} {N['adhipati']}ကိုလည်း {VITTH}{C} “{UPEKKHA}”ဟူ၍ "
             f"{K.NANAKARANA} ဖြစ်သည်{END})"),
        "(tīṇi upanissayā dutiyagamanasadisā)": f"({N['upanissaya']} {three}သည် ဒုတိယ {GAMANA}{SADISANI})",
        "(sappītikadukasadisā)": f"({SAPD}{SADISANI})",
        "(Cattāri sahajātā nānākkhaṇikā kātabbā, dve nānākkhaṇikā ca.)":
            f"({four}၌ {SAH_KAMMA}{C} {NANAKK}ကို {KAT}{C} {two}၌ {NANAKK}ကိုလည်း{END})",
        "(Imāni paccayāni sappītikakaraṇena vibhajitabbāni.)":
            f"(ဤ {F.PACCAYA}တို့ကို {SAPT} {DHAMMA}၏ {KARANENA} {VIBHAJ}{END})",
        "(Evaṃ paccanīyavibhaṅgopi itare tīṇi gaṇanāpi sappītikadukasadisā kātabbā.)":
            (f"({EVAM_T} {PACC_VIBH}ကိုလည်း{C} {ITARE} {GANANA} {three}ကိုလည်း {SAPD}နှင့် တူအောင် {KAT}{END})"),
        # kāmāvacara … saraṇa
        "(itare dve pākatikā)": f"({ITARE} {two}သည် {PAKATIKA})",
        "(Avasesā tīṇi pākatikā. Saṃkhittaṃ.)": f"({AVAS_O} {three}သည် {PAKATIKA}{END} {SAMKH}{END})",
        "(Avasesā gaṇanāpi sahajātavāropi kātabbo.)":
            f"({AVAS_O} {GANANA}တို့ကိုလည်း{C} {VARA('sahajāta')}ကိုလည်း {KAT}{END})",
        "(paṭiccasadisā. Mūlaṃ kātabbaṃ.)": f"({PATICCA_V}{SADISANI}{END} {K.NOTE_FIXED['mūlaṃ kātabbaṃ']}{END})",
        '(suddhake arūpamissake ca "vipāka"nti niyāmetabbaṃ, rūpamissake natthi. Saṃkhittaṃ)':
            (f"({D.SUDDHAKE}{F.LAKAUNG}{C} {ARUPA_N}နှင့် {MISSAKE}{F.LAKAUNG} “{N['vipāka']}”ဟု {NIYAM}{C} "
             f"ရုပ်နှင့် {MISSAKE} {NATTHI}{END} {SAMKH})"),
        "(Nakāmāvacaraṃ paṭiccavārasadisaṃ ninnānaṃ, idha sabbe mahābhūtā kātabbā.)":
            (f"({NAKAMA} {DHAMMA}သည် {PATICCA_V}{SADISA}{C} {NINNANA}{C} {IHA} {MAHAB} {SAB}ကို {KAT}{END})"),
        "(yāva asaññasattā, itare pañcapi pañhā, anulomaṃ kātabbaṃ)":
            f"({YAVA_AS}{C} {ITARE} {PANHA} {CNT['pañca']}လုံး{C} {ORD['anulomaṃ']}ကို {KAT})",
        "(saṃkhittaṃ. Mūlaṃ. Itarepi pañhā kātabbā)": f"({SAMKH}{END} {MULA}{END} {ITARE} {PANHA}တို့ကိုလည်း {KAT})",
        "(yāva ajjhattikaṃ mahābhūtaṃ)": f"({AJJH} {MAHAB}အထိ)",
        '(suddhike arūpe ca missake ca "vipāka"nti niyāmetabbaṃ)':
            f"({SUDDHIKE} {ARUPE}{F.LAKAUNG}{C} {MISSAKE}{F.LAKAUNG} “{N['vipāka']}”ဟု {NIYAM})",
        "(anulomaṃ)": f"({ORD['anulomaṃ']})",
        "(paccanīyaṃ)": f"({ORD['paccanīyaṃ']})",
        "(Yathā cūḷantaraduke lokiyadukaṃ. Evaṃ imampi dukaṃ kātabbaṃ, ninnānākaraṇaṃ.)":
            f"({DK_LOK}{KAYYA}{END} {EVAM_T} ဤ {DUKA}ကိုလည်း {KAT}{C} {NINNANAKARANA}{END})",
        "(yāva asaññasattā kātabbā)": f"({YAVA_AS} {KAT})",
        "(arūpadukasadisā kātabbā)": f"({ARUPAD}နှင့် တူအောင် {KAT})",
        "(arūpadukasadisā kātabbā, āmasanā nānāpadāyeva)":
            f"({ARUPAD}နှင့် တူအောင် {KAT}{C} {AMASANA}တို့သည် {NANAPADA})",
        "(saṃkhittaṃ. Pañcapi pañhā kātabbā. Yathā niyyānikadukaṃ evaṃ paṭiccavāropi sahajātavāropi paccayavāropi "
        "nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi kātabbā, ninnānākaraṇaṃ āmasanaṃ nānaṃ)":
            (f"({SAMKH}{END} {PANHA} {CNT['pañca']}လုံးကို {KAT}{END} {NIYYD}{KAYYA} {EVAM} {_pi_obj(*ALL6)} {KAT}{C} "
             f"{NINNANAKARANA}{C} {AMASANA}သည် {K.NANAKARANA} ဖြစ်သည်)"),
        "(niyyānikadukasadisā ninnānākaraṇā)": f"({NIYYD}{SADISANI}{C} {NINNANAKARANA})",
        "(arūpadukasadisaṃ)": f"({ARUPAD}{SADISA})",
        "(arūpāvacaradukasadisaṃ)": f"({ARUD}{SADISA})",
        "(Yāva ajjhattikā mahābhūtā. Yathā cūḷantaraduke lokiyadukasadisaṃ ninnānākaraṇaṃ.)":
            f"({AJJH} {MAHAB}တို့အထိ{END} {DK_LOK}နှင့် တူသည့်အတိုင်း{C} {NINNANAKARANA}{END})",
        "(Pañca pañhā arūpāvacaradukasadisā, anulomapaṭiccasadisā.)":
            f"({PANHA} {CNT['pañca']}သည် {ARUD}{SADISANI}{C} {ORD['anulomaṃ']}၏ {PATICCA_V}{SADISANI}{END})",
        "(yathā arūpāvacaradukassa paccayavāropi evaṃ kātabbo)": f"({ARUD}၌{KAYYA} {VARA('paccaya')}ကိုလည်း {EVAM} {KAT})",
        "(Evaṃ itare dve gaṇanāpi nissayavāropi kātabbo, saṃsaṭṭhavārepi dve pañhā kātabbā sabbattha.)":
            (f"({EVAM_T} {ITARE} {GANANA} {two}ကိုလည်း{C} {VARA('nissaya')}ကိုလည်း {KAT}{C} "
             f"{VARA('saṃsaṭṭha')}၌လည်း {K.SABBATTHA} {PANHA} {two}ကို {KAT}{END})"),
        "(arūpadukasadisaṃ, cattāri)": f"({ARUPAD}{SADISA}{C} {four})",
        "(arūpadukasadisā)": f"({ARUPAD}{SADISANI})",
        "(anulomamātikā gahetabbā)": f"({ANUL_MATIKA}ကို {GAHET})",
    }
