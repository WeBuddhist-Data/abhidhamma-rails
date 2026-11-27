# pi-6 phase 1: recurring frames check (the 200 most frequent keywords of the whole book)

Written by `frame_coverage.py` with the shared module `map6_rules.py` alone (no chapter table, no per-segment override): for every use of the keyword in the 44 `*.keywords.md`, the value the module gives in that segment and its presence in that segment's FINAL Burmese (the presence verifier of the module). «uses» = keyword uses; «values» = the values given (most frequent first, with uses); «presence» = uses whose value is in the segment's text; «source» = where the value came from (frame / stock = module tables, verb / participle / khandha / mula / place = the morphology R2-R5, base = R1, terms = my6-zeroshot-terms, pi-N = a pi-N value, compose, heading, stem).

**200 of 200 keywords reach 100% presence**; 19552 of 19552 uses present.

| # | keyword | uses | values (uses) | presence | source | chapters where it fails (why) |
|---|---|---|---|---|---|---|
| 1 | upapajjantānaṃ | 343 | ပြန်လည် ဖြစ်ပေါ်ဆဲသူ (314); ပြန်လည် ဖြစ်ပေါ်ဆဲ (29) | 343/343 (100%) | verb 343 | - |
| 2 | uppajjati | 290 | ဖြစ်ပေါ်သည် (290) | 290/290 (100%) | verb 290 | - |
| 3 | asaññasattānaṃ | 272 | အသညသတ် (272) | 272/272 (100%) | place 272 | - |
| 4 | uppajjissati | 264 | ဖြစ်ပေါ်လိမ့်မည် (249); ဖြစ်ပေါ်မည့် (15) | 264/264 (100%) | verb 264 | - |
| 5 | uppajjittha | 259 | ဖြစ်ပေါ်ခဲ့သည် (259) | 259/259 (100%) | verb 259 | - |
| 6 | manindriyaṃ | 244 | မနော၏ စွမ်းရည် (244) | 244/244 (100%) | pi-2 244 | - |
| 7 | paññindriyaṃ | 244 | ပညာ၏ စွမ်းရည် (244) | 244/244 (100%) | pi-2 244 | - |
| 8 | cavantānaṃ | 239 | စုတေဆဲသူ (239) | 239/239 (100%) | verb 239 | - |
| 9 | uppajjatīti | 236 | ဖြစ်ပေါ်သည် (236) | 236/236 (100%) | verb 236 | - |
| 10 | uppajjitthāti | 234 | ဖြစ်ပေါ်ခဲ့သည် (234) | 234/234 (100%) | verb 234 | - |
| 11 | nirujjhissati | 234 | ချုပ်ငြိမ်းလိမ့်မည် (234) | 234/234 (100%) | verb 234 | - |
| 12 | akusalā dhammā | 222 | အကုသိုလ် သဘောတရား (222) | 222/222 (100%) | stock 222 | - |
| 13 | uppajjissatīti | 218 | ဖြစ်ပေါ်လိမ့်မည် (218) | 218/218 (100%) | verb 218 | - |
| 14 | Itaresaṃ | 218 | အခြားသူ (216); အခြား (2) | 218/218 (100%) | stock 218 | - |
| 15 | saddhindriyaṃ | 216 | ယုံကြည်မှု၏ စွမ်းရည် (216) | 216/216 (100%) | pi-2 216 | - |
| 16 | nirujjhissatīti | 211 | ချုပ်ငြိမ်းလိမ့်မည် (211) | 211/211 (100%) | verb 211 | - |
| 17 | abyākatā dhammā | 202 | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား (202) | 202/202 (100%) | stock 202 | - |
| 18 | dhammāyatanaṃ | 200 | သဘောတရား အာရုံခံ နယ်ပယ် (200) | 200/200 (100%) | pi-2 200 | - |
| 19 | manāyatanaṃ | 200 | မနော အာရုံခံ နယ်ပယ် (200) | 200/200 (100%) | pi-2 200 | - |
| 20 | upekkhindriyaṃ | 189 | ဥပေက္ခာ၏ စွမ်းရည် (189) | 189/189 (100%) | pi-2 189 | - |
| 21 | nirujjhati | 188 | ချုပ်ငြိမ်းသည် (188) | 188/188 (100%) | verb 188 | - |
| 22 | manindriyañca | 184 | မနော၏ စွမ်းရည် (184) | 184/184 (100%) | base 184 | - |
| 23 | Natthi | 177 | မရှိသည် (177) | 177/177 (100%) | frame 177 | - |
| 24 | dhammāyatanañca | 174 | သဘောတရား အာရုံခံ နယ်ပယ် (174) | 174/174 (100%) | base 174 | - |
| 25 | arūpadhātuyā | 174 | ရုပ်မရှိသော ဘုံ (174) | 174/174 (100%) | place 174 | - |
| 26 | somanassindriyaṃ | 164 | ဝမ်းမြောက်မှု၏ စွမ်းရည် (164) | 164/164 (100%) | pi-2 164 | - |
| 27 | nirujjhittha | 161 | ချုပ်ငြိမ်းခဲ့သည် (161) | 161/161 (100%) | verb 161 | - |
| 28 | vedanākkhandho | 158 | ခံစားမှု အစုအဝေး (158) | 158/158 (100%) | khandha 158 | - |
| 29 | anantarā | 157 | ချက်ချင်း နောက် (157) | 157/157 (100%) | pi-5 157 | - |
| 30 | cittassa bhaṅgakkhaṇe | 156 | စိတ်၏ ပြိုပျက်ခြင်း ခဏ (156) | 156/156 (100%) | compose 156 | - |
| 31 | nirujjhitthāti | 153 | ချုပ်ငြိမ်းခဲ့သည် (153) | 153/153 (100%) | verb 153 | - |
| 32 | nirujjhatīti | 151 | ချုပ်ငြိမ်းသည် (151) | 151/151 (100%) | verb 151 | - |
| 33 | dvīsu vedanāsu | 151 | ခံစားမှု နှစ်ပါး (151) | 151/151 (100%) | compose 151 | - |
| 34 | rūpāyatanaṃ | 149 | အဆင်းအရောင် အာရုံခံ နယ်ပယ် (149) | 149/149 (100%) | pi-2 149 | - |
| 35 | upekkhindriyañca | 143 | ဥပေက္ခာ၏ စွမ်းရည် (143) | 143/143 (100%) | base 143 | - |
| 36 | jīvitindriyaṃ | 138 | အသက်၏ စွမ်းရည် (138) | 138/138 (100%) | pi-2 138 | - |
| 37 | indriyā | 138 | စွမ်းရည် (138) | 138/138 (100%) | pi-2 138 | - |
| 38 | kusalā dhammā | 136 | ကုသိုလ် သဘောတရား (136) | 136/136 (100%) | stock 136 | - |
| 39 | somanassindriyañca | 128 | ဝမ်းမြောက်မှု၏ စွမ်းရည် (128) | 128/128 (100%) | base 128 | - |
| 40 | abyākatā ca dhammā | 126 | ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား (126) | 126/126 (100%) | compose 126 | - |
| 41 | manāyatanañca | 125 | မနော အာရုံခံ နယ်ပယ် (125) | 125/125 (100%) | base 125 | - |
| 42 | rūpāyatanañca | 124 | အဆင်းအရောင် အာရုံခံ နယ်ပယ် (124) | 124/124 (100%) | base 124 | - |
| 43 | samudayasaccaṃ | 123 | ဖြစ်ပေါ်ခြင်း သစ္စာ (123) | 123/123 (100%) | family 123 | - |
| 44 | vacīsaṅkhāro | 123 | နှုတ်၏ ပြုပြင်ဖန်တီးမှု (123) | 123/123 (100%) | pi-5 123 | - |
| 45 | rūpakkhandho | 119 | ရုပ် အစုအဝေး (119) | 119/119 (100%) | khandha 119 | - |
| 46 | cittassa | 119 | စိတ် (119) | 119/119 (100%) | pi-2 119 | - |
| 47 | vicikicchānusayo | 119 | ယုံမှားမှု ကိန်းအောင်းခြင်း (119) | 119/119 (100%) | family 119 | - |
| 48 | purisindriyaṃ | 119 | ယောက်ျား၏ စွမ်းရည် (119) | 119/119 (100%) | pi-2 119 | - |
| 49 | nuppajjati | 117 | မဖြစ်ပေါ် (117) | 117/117 (100%) | verb 117 | - |
| 50 | rūpadhātuyā | 117 | သိမ်မွေ့သော ရုပ်ဘုံ (117) | 117/117 (100%) | place 117 | - |
| 51 | akusalā ca dhammā | 117 | အကုသိုလ် သဘောတရား (117) | 117/117 (100%) | compose 117 | - |
| 52 | puggalā | 115 | ပုဂ္ဂိုလ် (115) | 115/115 (100%) | stock 115 | - |
| 53 | cittaṃ | 115 | စိတ် (115) | 115/115 (100%) | pi-2 115 | - |
| 54 | bhavarāgānusayo | 115 | ဘဝရာဂ ကိန်းအောင်းခြင်း (115) | 115/115 (100%) | family 115 | - |
| 55 | cittasaṅkhāro | 114 | စိတ်၏ ပြုပြင်ဖန်တီးမှု (114) | 114/114 (100%) | pi-5 114 | - |
| 56 | avijjānusayo | 114 | အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း (114) | 114/114 (100%) | family 114 | - |
| 57 | jīvitindriyañca | 112 | အသက်၏ စွမ်းရည် (112) | 112/112 (100%) | base 112 | - |
| 58 | ṭhapetvā | 111 | ချန်ထား၍ (111) | 111/111 (100%) | stock 111 | - |
| 59 | ghānāyatanaṃ | 110 | နှာခေါင်း အာရုံခံ နယ်ပယ် (110) | 110/110 (100%) | pi-2 110 | - |
| 60 | diṭṭhānusayo | 110 | အယူ ကိန်းအောင်းခြင်း (110) | 110/110 (100%) | family 110 | - |
| 61 | avijjānusayaṃ | 108 | အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း (108) | 108/108 (100%) | family 108 | - |
| 62 | maggasaccaṃ | 107 | မဂ် သစ္စာ (107) | 107/107 (100%) | family 107 | - |
| 63 | cittassa uppādakkhaṇe | 107 | စိတ်၏ ဖြစ်ခြင်း ခဏ (107) | 107/107 (100%) | compose 107 | - |
| 64 | kāmadhātuyā | 106 | ကာမဘုံ (106) | 106/106 (100%) | place 106 | - |
| 65 | cakkhāyatanaṃ | 104 | မျက်စိ အာရုံခံ နယ်ပယ် (104) | 104/104 (100%) | pi-2 104 | - |
| 66 | anulomapuggalo | 102 | ပုဂ္ဂိုလ်အလိုက် အဟုတ်ပြ ပုံစံ (102) | 102/102 (100%) | terms 102 | - |
| 67 | dukkhasaccaṃ | 102 | ဒုက္ခ သစ္စာ (102) | 102/102 (100%) | family 102 | - |
| 68 | mānānusayo | 100 | မာန ကိန်းအောင်းခြင်း (100) | 100/100 (100%) | family 100 | - |
| 69 | kāyasaṅkhāro | 98 | ကိုယ် ပြုပြင်ဖန်တီးမှု (98) | 98/98 (100%) | pi-2 98 | - |
| 70 | cakkhundriyaṃ | 98 | မျက်စိ၏ စွမ်းရည် (98) | 98/98 (100%) | pi-2 98 | - |
| 71 | nuppajjatīti | 97 | မဖြစ်ပေါ် (97) | 97/97 (100%) | verb 97 | - |
| 72 | aññātāvindriyaṃ | 97 | အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည် (97) | 97/97 (100%) | pi-2 97 | - |
| 73 | maggasaccañca | 96 | မဂ် သစ္စာ (96) | 96/96 (100%) | family 96 | - |
| 74 | aggamaggaṃ paṭilabhissanti | 96 | အမြတ်ဆုံး မဂ်ကို ရရှိမည့် (96) | 96/96 (100%) | compose 96 | - |
| 75 | Kāmadhātuyā | 96 | ကာမဘုံ (96) | 96/96 (100%) | place 96 | - |
| 76 | bhavarāgānusayaṃ | 96 | ဘဝရာဂ ကိန်းအောင်းခြင်း (96) | 96/96 (100%) | family 96 | - |
| 77 | vicikicchānusayaṃ | 96 | ယုံမှားမှု ကိန်းအောင်းခြင်း (96) | 96/96 (100%) | family 96 | - |
| 78 | (no direct equivalent) | 94 | (no direct equivalent) (94) | 94/94 (100%) | frame 94 | - |
| 79 | samudayasaccañca | 94 | ဖြစ်ပေါ်ခြင်း သစ္စာ (94) | 94/94 (100%) | family 94 | - |
| 80 | itthindriyaṃ | 93 | မိန်းမ၏ စွမ်းရည် (93) | 93/93 (100%) | pi-2 93 | - |
| 81 | cakkhu | 90 | မျက်စိ (90) | 90/90 (100%) | pi-2 90 | - |
| 82 | purisindriyañca | 90 | ယောက်ျား၏ စွမ်းရည် (90) | 90/90 (100%) | base 90 | - |
| 83 | parinibbāyissanti | 89 | ပရိနိဗ္ဗာန် ပြုမည့် (89) | 89/89 (100%) | verb 89 | - |
| 84 | upapajjitvā | 89 | ပြန်လည် ဖြစ်ပေါ်၍ (89) | 89/89 (100%) | verb 89 | - |
| 85 | anulomaokāso | 88 | နေရာအလိုက် အဟုတ်ပြ ပုံစံ (88) | 88/88 (100%) | terms 88 | - |
| 86 | anulomapuggalokāsā | 88 | ပုဂ္ဂိုလ်နှင့် နေရာအလိုက် အဟုတ်ပြ ပုံစံ (88) | 88/88 (100%) | terms 88 | - |
| 87 | paṭighānusayo | 88 | မုန်းတီးမှု ကိန်းအောင်းခြင်း (88) | 88/88 (100%) | family 88 | - |
| 88 | nuppajjissati | 87 | မဖြစ်ပေါ်လိမ့်မည် (87) | 87/87 (100%) | verb 87 | - |
| 89 | Pacchimabhavikānaṃ | 87 | နောက်ဆုံး ဘဝ ရှိသူ (83); နောက်ဆုံး ဘဝ ရှိသော (4) | 87/87 (100%) | stock 87 | - |
| 90 | pavatte | 87 | ဘဝ တည်နေစဉ် (87) | 87/87 (100%) | stock 87 | - |
| 91 | ghānāyatanañca | 86 | နှာခေါင်း အာရုံခံ နယ်ပယ် (86) | 86/86 (100%) | base 86 | - |
| 92 | arahantānaṃ | 84 | ရဟန္တာ (84) | 84/84 (100%) | stock 84 | - |
| 93 | avasesā | 83 | ကြွင်းကျန်သော (83) | 83/83 (100%) | stock 83 | - |
| 94 | paccanīkapuggalo | 83 | ပုဂ္ဂိုလ်အလိုက် အငြင်းပြ ပုံစံ (83) | 83/83 (100%) | terms 83 | - |
| 95 | paccanīkapuggalokāsā | 83 | ပုဂ္ဂိုလ်နှင့် နေရာအလိုက် အငြင်းပြ ပုံစံ (83) | 83/83 (100%) | terms 83 | - |
| 96 | Pañcavokāre | 83 | အစုအဝေး ငါးပါး ရှိသော ဘဝ (83) | 83/83 (100%) | place 83 | - |
| 97 | parijānāti | 83 | ပိုင်းခြား သိသည် (83) | 83/83 (100%) | verb 83 | - |
| 98 | parijānātīti | 83 | ပိုင်းခြား သိသည် (83) | 83/83 (100%) | verb 83 | - |
| 99 | paccanīkaokāso | 82 | နေရာအလိုက် အငြင်းပြ ပုံစံ (82) | 82/82 (100%) | terms 82 | - |
| 100 | arūpānaṃ | 81 | ရုပ်မရှိသော ဘုံ၌ ရှိသူ (81) | 81/81 (100%) | place 81 | - |
| 101 | uppajjanti | 80 | ဖြစ်ပေါ်သည် (80) | 80/80 (100%) | verb 80 | - |
| 102 | dukkhāya vedanāya | 80 | နာကျင်သော ခံစားမှု (80) | 80/80 (100%) | pi-2 80 | - |
| 103 | mānānusayañca | 80 | မာန ကိန်းအောင်းခြင်း (80) | 80/80 (100%) | family 80 | - |
| 104 | vicikicchānusayañca | 80 | ယုံမှားမှု ကိန်းအောင်းခြင်း (80) | 80/80 (100%) | family 80 | - |
| 105 | nirodhasamāpannānaṃ | 79 | ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူ (79) | 79/79 (100%) | stock 79 | - |
| 106 | parinibbantānaṃ | 76 | ပရိနိဗ္ဗာန် ပြုဆဲသူ (76) | 76/76 (100%) | verb 76 | - |
| 107 | sotāyatanaṃ | 76 | နား အာရုံခံ နယ်ပယ် (76) | 76/76 (100%) | pi-2 76 | - |
| 108 | kāmarāgānusayo | 76 | ကာမရာဂ ကိန်းအောင်းခြင်း (76) | 76/76 (100%) | family 76 | - |
| 109 | arūpe | 75 | ရုပ်မရှိသော ဘုံ (75) | 75/75 (100%) | place 75 | - |
| 110 | arūpāvacarānaṃ | 75 | ရုပ်မရှိသော ဘုံ၌ ရှိသူ (71); ရုပ်မရှိသော ဘုံ၌ ရှိသော (4) | 75/75 (100%) | place 75 | - |
| 111 | nuppajjissatīti | 73 | မဖြစ်ပေါ်လိမ့်မည် (73) | 73/73 (100%) | verb 73 | - |
| 112 | Dukkhāya vedanāya | 73 | နာကျင်သော ခံစားမှု (73) | 73/73 (100%) | pi-2 73 | - |
| 113 | nuppajjittha | 72 | မဖြစ်ပေါ်ခဲ့ (72) | 72/72 (100%) | verb 72 | - |
| 114 | diṭṭhānusayaṃ | 72 | အယူ ကိန်းအောင်းခြင်း (72) | 72/72 (100%) | family 72 | - |
| 115 | paṭighānusayañca | 72 | မုန်းတီးမှု ကိန်းအောင်းခြင်း (72) | 72/72 (100%) | family 72 | - |
| 116 | Suddhāvāsānaṃ | 71 | သုဒ္ဓါဝါသ ဘုံ၌ ရှိသူ (71) | 71/71 (100%) | place 71 | - |
| 117 | Avasesā | 69 | ကြွင်းကျန်သော (69) | 69/69 (100%) | stock 69 | - |
| 118 | saññākkhandho | 69 | မှတ်သိမှု အစုအဝေး (69) | 69/69 (100%) | khandha 69 | - |
| 119 | puggalānaṃ | 69 | ပုဂ္ဂိုလ် (69) | 69/69 (100%) | stock 69 | - |
| 120 | cakkhundriyanti | 69 | မျက်စိ၏ စွမ်းရည် (69) | 69/69 (100%) | base 69 | - |
| 121 | aññātāvindriyanti | 69 | အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည် (69) | 69/69 (100%) | base 69 | - |
| 122 | upekkhāya | 69 | ဥပေက္ခာ (69) | 69/69 (100%) | stock 69 | - |
| 123 | Suddhāvāsaṃ | 68 | သုဒ္ဓါဝါသ ဘုံ (68) | 68/68 (100%) | place 68 | - |
| 124 | tīsu vedanāsu | 68 | ခံစားမှု သုံးပါး (68) | 68/68 (100%) | compose 68 | - |
| 125 | kāmarāgānusayañca | 68 | ကာမရာဂ ကိန်းအောင်းခြင်း (68) | 68/68 (100%) | family 68 | - |
| 126 | avijjānusayañca | 68 | အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း (68) | 68/68 (100%) | family 68 | - |
| 127 | ghānindriyaṃ | 68 | နှာခေါင်း၏ စွမ်းရည် (68) | 68/68 (100%) | pi-2 68 | - |
| 128 | puthujjanā | 67 | ပုထုဇဉ် (67) | 67/67 (100%) | stock 67 | - |
| 129 | kusalā ca dhammā | 66 | ကုသိုလ် သဘောတရား (66) | 66/66 (100%) | compose 66 | - |
| 130 | somanassena | 66 | ဝမ်းမြောက်မှု (66) | 66/66 (100%) | stock 66 | - |
| 131 | anulomaṃ | 65 | အဟုတ်ပြ ပုံစံ (65) | 65/65 (100%) | frame 65 | - |
| 132 | nuppajjitthāti | 65 | မဖြစ်ပေါ်ခဲ့ (65) | 65/65 (100%) | verb 65 | - |
| 133 | Aggamaggasamaṅgī | 63 | အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူ (63) | 63/63 (100%) | family 63 | - |
| 134 | vattamāne | 63 | ဖြစ်နေသော (63) | 63/63 (100%) | pi-5 63 | - |
| 135 | nirujjhissantīti | 62 | ချုပ်ငြိမ်းလိမ့်မည် (62) | 62/62 (100%) | verb 62 | - |
| 136 | cakkhundriyañca | 62 | မျက်စိ၏ စွမ်းရည် (62) | 62/62 (100%) | base 62 | - |
| 137 | paccanīkaṃ | 60 | အငြင်းပြ ပုံစံ (60) | 60/60 (100%) | frame 60 | - |
| 138 | vicikicchānusayena | 60 | ယုံမှားမှု ကိန်းအောင်းခြင်း (60) | 60/60 (100%) | family 60 | - |
| 139 | mānānusayaṃ | 60 | မာန ကိန်းအောင်းခြင်း (60) | 60/60 (100%) | family 60 | - |
| 140 | aññātāvindriyañca | 60 | အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည် (60) | 60/60 (100%) | base 60 | - |
| 141 | Rūpadhātuyā | 59 | သိမ်မွေ့သော ရုပ်ဘုံ (59) | 59/59 (100%) | place 59 | - |
| 142 | aññindriyaṃ | 59 | အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည် (59) | 59/59 (100%) | pi-2 59 | - |
| 143 | puggalo | 58 | ပုဂ္ဂိုလ် (58) | 58/58 (100%) | stock 58 | - |
| 144 | aññātāvī | 57 | အပြည့်အဝ သိမြင်ပြီးသူ (57) | 57/57 (100%) | pi-5 57 | - |
| 145 | bhavarāgānusayañca | 56 | ဘဝရာဂ ကိန်းအောင်းခြင်း (56) | 56/56 (100%) | family 56 | - |
| 146 | uppajjantīti | 56 | ဖြစ်ပေါ်သည် (56) | 56/56 (100%) | verb 56 | - |
| 147 | rūpaṃ | 55 | ရုပ် (49); အဆင်းအရောင် (6) | 55/55 (100%) | stock 55 | - |
| 148 | pañcavokārānaṃ | 55 | အစုအဝေး ငါးပါး ရှိသော ဘဝ၌ ရှိသော (43); အစုအဝေး ငါးပါး ရှိသော ဘဝ၌ ရှိသူ (12) | 55/55 (100%) | place 55 | - |
| 149 | cakkhāyatanañca | 55 | မျက်စိ အာရုံခံ နယ်ပယ် (55) | 55/55 (100%) | base 55 | - |
| 150 | bhavarāgānusayena | 55 | ဘဝရာဂ ကိန်းအောင်းခြင်း (55) | 55/55 (100%) | family 55 | - |
| 151 | ghānindriyañca | 55 | နှာခေါင်း၏ စွမ်းရည် (55) | 55/55 (100%) | base 55 | - |
| 152 | diṭṭhānusayena | 54 | အယူ ကိန်းအောင်းခြင်း (54) | 54/54 (100%) | family 54 | - |
| 153 | maggaṃ paṭilabhissanti | 53 | မဂ်ကို ရရှိမည့် (53) | 53/53 (100%) | compose 53 | - |
| 154 | Kāmāvacare | 53 | ကာမဘုံ (53) | 53/53 (100%) | place 53 | - |
| 155 | avijjānusayena | 53 | အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း (53) | 53/53 (100%) | family 53 | - |
| 156 | itthindriyañca | 53 | မိန်းမ၏ စွမ်းရည် (53) | 53/53 (100%) | base 53 | - |
| 157 | Asaññasatte | 52 | အသညသတ် ဘုံ (52) | 52/52 (100%) | place 52 | - |
| 158 | paṭighānusayaṃ | 52 | မုန်းတီးမှု ကိန်းအောင်းခြင်း (52) | 52/52 (100%) | family 52 | - |
| 159 | paññindriyañca | 52 | ပညာ၏ စွမ်းရည် (52) | 52/52 (100%) | base 52 | - |
| 160 | dukkhasaccañca | 51 | ဒုက္ခ သစ္စာ (51) | 51/51 (100%) | family 51 | - |
| 161 | Aggamaggasamaṅgīnaṃ | 51 | အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူ (51) | 51/51 (100%) | family 51 | - |
| 162 | Aggamaggassa | 51 | အမြတ်ဆုံး မဂ် (51) | 51/51 (100%) | stock 51 | - |
| 163 | Aṭṭhamako | 51 | အဋ္ဌမ (51) | 51/51 (100%) | stem 51 | - |
| 164 | pahīno | 51 | ပယ်ပြီးသော (51) | 51/51 (100%) | stock 51 | - |
| 165 | appahīno | 51 | မပယ်ရသေးသော (51) | 51/51 (100%) | stock 51 | - |
| 166 | nirujjhissanti | 51 | ချုပ်ငြိမ်းလိမ့်မည် (51) | 51/51 (100%) | verb 51 | - |
| 167 | indriyaṃ | 51 | စွမ်းရည် (51) | 51/51 (100%) | pi-2 51 | - |
| 168 | saddhindriyañca | 51 | ယုံကြည်မှု၏ စွမ်းရည် (51) | 51/51 (100%) | base 51 | - |
| 169 | arūpaṃ | 50 | ရုပ်မရှိသော ဘုံ (50) | 50/50 (100%) | place 50 | - |
| 170 | pañcavokāraṃ | 50 | အစုအဝေး ငါးပါး ရှိသော ဘဝ (50) | 50/50 (100%) | place 50 | - |
| 171 | rūpāvacarānaṃ | 50 | သိမ်မွေ့သော ရုပ်ဘုံ၌ ရှိသူ (30); သိမ်မွေ့သော ရုပ်ဘုံ … ရှိသူ (16); သိမ်မွေ့သော ရုပ်ဘုံ … ရှိသော (4) | 50/50 (100%) | place 50 | - |
| 172 | bhaṅgakkhaṇe | 49 | ပြိုပျက်ခြင်း ခဏ (49) | 49/49 (100%) | stock 49 | - |
| 173 | Anāgāmissa | 49 | အနာဂါမ် (49) | 49/49 (100%) | pi-5 49 | - |
| 174 | Asaññasattānaṃ | 48 | အသညသတ် (48) | 48/48 (100%) | place 48 | - |
| 175 | mānānusayena | 48 | မာန ကိန်းအောင်းခြင်း (48) | 48/48 (100%) | family 48 | - |
| 176 | sotindriyaṃ | 47 | နား၏ စွမ်းရည် (47) | 47/47 (100%) | pi-2 47 | - |
| 177 | pacchimabhavikānaṃ | 46 | နောက်ဆုံး ဘဝ ရှိသူ (46) | 46/46 (100%) | stock 46 | - |
| 178 | indriyanti | 46 | စွမ်းရည် (46) | 46/46 (100%) | base 46 | - |
| 179 | anaññātaññassāmītindriyaṃ | 45 | မသိရသေးသည်ကို သိရတော့မည်ဟူသော စွမ်းရည် (45) | 45/45 (100%) | pi-2 45 | - |
| 180 | sotāyatanañca | 44 | နား အာရုံခံ နယ်ပယ် (44) | 44/44 (100%) | base 44 | - |
| 181 | Rūpāvacarānaṃ | 44 | သိမ်မွေ့သော ရုပ်ဘုံ၌ ရှိသူ (38); သိမ်မွေ့သော ရုပ်ဘုံ … ရှိသူ (6) | 44/44 (100%) | place 44 | - |
| 182 | Pacchimacittasamaṅgīnaṃ | 44 | နောက်ဆုံး စိတ်နှင့် ပြည့်စုံသူ (44) | 44/44 (100%) | family 44 | - |
| 183 | uppajjissantīti | 44 | ဖြစ်ပေါ်လိမ့်မည် (44) | 44/44 (100%) | verb 44 | - |
| 184 | Puthujjanassa | 43 | ပုထုဇဉ် (43) | 43/43 (100%) | stock 43 | - |
| 185 | nirujjhanti | 43 | ချုပ်ငြိမ်းသည် (43) | 43/43 (100%) | verb 43 | - |
| 186 | arūpāvacare | 42 | ရုပ်မရှိသော ဘုံ (42) | 42/42 (100%) | place 42 | - |
| 187 | paṭighānusayena | 42 | မုန်းတီးမှု ကိန်းအောင်းခြင်း (42) | 42/42 (100%) | family 42 | - |
| 188 | Cakkhāyatanamūlakaṃ | 41 | မျက်စိ အာရုံခံ နယ်ပယ်ကို အခြေခံသော (41) | 41/41 (100%) | mulaka 41 | - |
| 189 | Cakkhundriyamūlakaṃ | 41 | မျက်စိ၏ စွမ်းရည်ကို အခြေခံသော (41) | 41/41 (100%) | mulaka 41 | - |
| 190 | uppajjissanti | 40 | ဖြစ်ပေါ်လိမ့်မည် (40) | 40/40 (100%) | verb 40 | - |
| 191 | nirujjhantīti | 40 | ချုပ်ငြိမ်းသည် (40) | 40/40 (100%) | verb 40 | - |
| 192 | aññindriyañca | 40 | အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည် (40) | 40/40 (100%) | base 40 | - |
| 193 | Parinibbantānaṃ | 39 | ပရိနိဗ္ဗာန် ပြုဆဲသူ (39) | 39/39 (100%) | verb 39 | - |
| 194 | Arahā | 39 | ရဟန္တာ (39) | 39/39 (100%) | stock 39 | - |
| 195 | kāyo | 39 | ကိုယ် (39) | 39/39 (100%) | pi-2 39 | - |
| 196 | sotaṃ | 39 | နား (39) | 39/39 (100%) | pi-2 39 | - |
| 197 | kāmāvacarānaṃ | 39 | ကာမဘုံ၌ ရှိသူ (30); ကာမဘုံ၌ ရှိသော (6); ကာမဘုံနှင့် ဆိုင်သော (2); ကာမဘုံ … ရှိသူ (1) | 39/39 (100%) | place 39 | - |
| 198 | pajahatīti | 39 | ပယ်သည် (39) | 39/39 (100%) | verb 39 | - |
| 199 | pajahati | 39 | ပယ်သည် (39) | 39/39 (100%) | verb 39 | - |
| 200 | nappajahatīti | 39 | မပယ် (39) | 39/39 (100%) | verb 39 | - |

## Notes for phase 2

**Module errors found by this check and fixed in `map6_rules.py`** (first run: 179 of 200 at 100%): the moment
phrases had no value (cittassa bhaṅgakkhaṇe / uppādakkhaṇe, bhaṅgakkhaṇe, pavatte: STOCK, harmonise B1 «… ခဏ»
without «၌», «ဘဝ တည်နေစဉ်»); counts + noun took a person classifier from elsewhere in the segment («နှစ်ယောက် …
ခံစားမှု»: compose now joins the noun with the adjacent count, «ခံစားမှု နှစ်ပါး»); the sacca names had no value or a
wrong stem value (maggasaccaṃ «မဂ်နှင့် ပြည့်စုံသော» from S1: family R8 «X သစ္စာ»); the -samaṅgī persons, the
anusaya names in the oblique cases, aggamagga, arahantānaṃ, puthujjanā, nirodhasamāpannānaṃ, pahīno / appahīno,
pacchimacitta (STOCK / R8); persons before a noun («နောက်ဆုံး ဘဝ ရှိသော ယောက်ျား», «အခြား ယောက်ျား»: tuples);
two planes sharing «၌ ရှိသူ» (R5 shared_being), «ကာမဘုံနှင့် ဆိုင်သော» (R5); the «(X-mūlakaṃ)» labels (R4 mulaka);
the contraction nānuseti (R2).

**Genuine context differences** (one keyword, two forms of the text; the module picks the segment's own form, no
action needed): upapajjantānaṃ «ပြန်လည် ဖြစ်ပေါ်ဆဲသူ» / «ပြန်လည် ဖြစ်ပေါ်ဆဲ» (before another person noun);
uppajjissati «ဖြစ်ပေါ်လိမ့်မည်» / «ဖြစ်ပေါ်မည့်» (relative clause «… ဖြစ်ပေါ်မည့်သူတို့», rule 3); Itaresaṃ «အခြားသူ» /
«အခြား»; Pacchimabhavikānaṃ, pañcavokārānaṃ, arūpāvacarānaṃ «…ရှိသူ» / «…ရှိသော» (before a noun); rūpāvacarānaṃ /
kāmāvacarānaṃ «P၌ ရှိသူ» / «P … ရှိသူ» / «Pနှင့် ဆိုင်သော»; rūpaṃ «ရုပ်» / «အဆင်းအရောင်» (rūpāyatana sense, f_rupam).

**Values from the stem fallback (S1)**: in the top 200 only Aṭṭhamako «အဋ္ဌမ» (51 uses; check the chapter's own word in
phase 2); in the whole book 624 uses of 88 keywords: review them in phase 2 (they are present but not checked by eye).

**Whole-book dry run** (all 27447 keyword uses of the 44 files, module only): 26302 present, 1145 uses (218
keywords) without a value, 0 with a value not in the text. The groups without a value, for the phase-2 chapter tables: sānusayo /
niranusayo (-ti, -ā) (ch. 7); sacakkhuka / acakkhuka / sasotaka / asotaka / sacittaka / arūpaka persons «မျက်စိ ရှိလျက် /
မရှိဘဲ …» (ch. 3, 4, 10; harmonise table: value «… ရှိသော / မရှိသော» by the ending rule); the X-sampayutta /
X-vippayutta + citta compounds «Xနှင့် ယှဉ်တွဲသော / ကင်းကွာသော စိတ်» and their moment phrases (ch. 5, 9, 10;
pi-1 rule 3 «…နှင့် ကင်းကွာသော»); avitakkaavicāra / savitakkasavicāra (ch. 6); Abhisametāvīnaṃ / Anabhisametāvīnaṃ
(ch. 5; harmonise A1 «ထင်ထင်ရှားရှား သိမြင်ပြီးသူ»); the cited forms Yassakampi / yassayatthakampi (ch. 3, 5, 6);
caññe (ch. 5), bhaṅgā (ch. 7), aññaṃ, anaññātaññassāmīti (ch. 10; harmonise A2), tesaṃyeva (ch. 6; harmonise B1
«ထိုသူတို့၏ပင်»), Atītānāgataṃ (ch. 8).

