# pi-5 Burmese termbase: APPROVED and LOCKED

- Approved and locked by the coordinator on 2026-11-22 under the user's standing go-ahead ("dont ask for my permission, continue now"; "continue now for pi all").
- File: `AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md` (5418 headwords, 5553 senses; 370 multi-candidate decided, 160 aligned, 14 outside). Decisions: `decisions-A.tsv` (built by `build.py` from raw-multi / raw-align / raw-family / raw-textinc), report: `termbase-decisions.md`, differences: `diff-categories.txt`.
- sha256 `6f2558f8460aa03fc03a458b36ce49d5fce7872d8c202febe03f030426e621de`.
- Approved as built by the termbase agent (1468 senses take a locked term: pi-4 560, pi-3 159, pi-2 675, pi-1 74; 237 differ, each explained in diff-categories.txt; family scan 446 -> 345, the rest grammar / sense differences; 26 §A text inconsistencies decided by a term, 10 left for the rails step), with the 12 outside terms approved (niruddhāya, upacchedo, niyāmaṃ okkamituṃ, visuddhiyā, saññāvedayitanirodhaṃ (+ samāpannassa), seṭṭho, ṭhitā, bhūtā «မူလဓာတ်», samannāhāro, saṃvattaniyaṃ kammaṃ, buddhā tiṭṭhanti).
- Key choices approved: kathā «ဆွေးနွေးချက်» (approved sample); eva «ပင်» (131 / 141 emphatic uses; the 10 restrictive uses may keep «သာ» in the rails as a context sense); buddha family «ဘုရားရှင်»; samāpatti «သမာပတ်», cessation «ချုပ်ငြိမ်းခြင်း သမာပတ်»; yoni «မွေးဖွားရာ အမျိုးအစား»; hitāya «အကျိုးစီးပွား» vs atthāya «အကျိုး»; dhammacakka «ဓမ္မစကြာ» (no locked term; pi-2's text word «တရားစက်» is not a termbase term); eka «တစ်».

## Coordinator changes before the lock (2026-11-22)
- paṭivedha / paṭivedho / paṭivedhā «ထိုးဖောက်၍ သိခြင်း», paṭivedhāya «ထိုးဖောက်၍ သိရန်», paṭividdha / paṭividdhaṃ «ထိုးဖောက်၍ သိပြီးသော», paṭivijjhanto «ထိုးဖောက်၍ သိလျက်», heading Paṭivedhānuyogo «ထိုးဖောက်၍ သိခြင်းကို စစ်ဆေးမေးမြန်းခြင်း»: the locked pi-4 paṭivedho / paṭivijjhati term; the built «ထိုးထွင်း သိမြင်ခြင်း» differed from vipassanā «ထိုးထွင်းသိမြင်ခြင်း» (locked pi-1 / pi-2 / pi-4) only by a space.
- abhisametuṃ «ထင်ထင်ရှားရှား သိမြင်ရန်»: the abhisamaya family (locked pi-4), not vipassanā's word.
- thero «မထေရ်»: the pi-5 text's word (32 of 33 uses) and natural standalone Burmese; pi-4 «ထေရ်» stays a substring.
- Backups of the agent's raw files: `raw-*.before-coordinator.tsv`.

## For the rails step
- Left for rails (§A, no term decides them): 1 uddāna / saṃkhitta, 7, 9, 10 negation spacing, 11 untranslated text at ^5-371, 21 vagga ordinals, 22 siglum, 27 asuci phrase, 29 jīvitā at ^5-857, 30 ^5-918 Mahāniyāmo split.
- Locked term kept although it fits some uses badly: ṭhiti in viññāṇaṭṭhiti, uppādeyya in methunaṃ uppādeyya, dānaṃ as the gift itself: render these by context and log them as context senses.
- Locked: the rails translation uses it as a fixed reference. Never edit the termbase file; a term that turns out wrong is reported.

## Change 2026-11-22 (rails-step proposals), decided by the coordinator under the user's standing go-ahead
- From `rails/termbase-proposals.tsv` (60): 56 stale phrase entries realigned to the locked word decisions (nirodhasamāpatti headings «ချုပ်ငြိမ်းခြင်း သမာပတ်», X-phalasamaṅgī «…ဖိုလ်နှင့် ပြည့်စုံသော», saṃvattaniko «ဖြစ်စေတတ်သော», sukhānuppadāna «ချမ်းသာကို ပေးခြင်း», Issariya headings «အစိုးရခြင်းဖြင့်…», rūpa / arūpa dhātu «…ဘုံ», paṭivijānanti «ခွဲခြား သိသည်», dadeyya «ပေးသည်» …) and voropetvā «ချ၍» (§A29 jīvitā voropetvā «အသက်မှ ချ၍»).
- Rejected: sattamabhavika / sattamabhavikassa «သတ္တမ ဘဝ…» (their own entry «ခုနစ်ကြိမ်မြောက် ဘဝ၌ ရှိသော» stays; the ordinal «သတ္တမ» is for headings only); sikkhāya «သိက္ခာ» (locked pi-2 / pi-1 «ကျင့်စဉ်», the same eight-doubts list as pi-2 Vibhaṅga).
- Added by the coordinator: the contrasted pair kept parallel: sabyābajjhaṃ «ညှဉ်းဆဲမှု ရှိသော» (was «ဆင်းရဲစေတတ်သော»), sabyābajjhaṃ abyābajjhaṃ «ညှဉ်းဆဲမှု ရှိသော … ညှဉ်းဆဲမှု ကင်းသော».
- Through raw-align.tsv + build.py + termbase_assemble.py 5 burmese my plain (aligned 218, outside 14, no errors). sha256 now `ee9018fbfe855b6e9595d95e26eab0176de35802502f73a1a6b16888328fba1f` (before `6f2558f8460aa03fc03a458b36ce49d5fce7872d8c202febe03f030426e621de`). Backups: `raw-*.before-rails-proposals.tsv`.

## Change 2026-11-22 (bilingual review A / B), decided by the coordinator under the user's standing go-ahead
- appiyaṃ «မခွဲခြား» (A2: appiyaṃ karitvā = without separating, in the identity formula; was «ဦးစားမပေး»).
- abhisambuddhāni «ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူခဲ့သော», Abhisambujjhitvā «ကိုယ်တိုင် အပြည့်အဝ သိမြင်၍», abhisambujjhati «ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသည်» (A5: the abhisambuddho family, not vipassanā's word).
- Bhaṭo «ကျွေးမွေးခဲ့သူ» (B2: AN 5.39, the one we supported; was «ဝေယျာဝစ္စ ပြုသူ»).
- voropeti «သတ်သည်», voropetvā «သတ်၍», mātaraṃ voropetvā «အမိကို အသက်မှ သတ်၍», Asañcicca voropetvā «မရည်ရွယ်ဘဲ … အသက်မှ သတ်၍» (B5: pi-2 active voropeyya «သတ်သည်»; reverses the rails-proposal «ချ…»; the passive jīvitā voropitā keeps «ချခံရသော»).
- ānantariko «ချက်ချင်း အကျိုးပေးသော ကံ ရှိသော», ānantariyassa «ချက်ချင်း အကျိုးပေးသော ကံကို ပြုသော», Dhammasaññī ānantariko «တရားဟု မှတ်သိသော … ချက်ချင်း အကျိုးပေးသော ကံ ရှိသော» (B6: pi-2 / pi-4 ānantarika family).
- samphaṃ «အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား» (B12: pi-1 … pi-4 samphappalāpa).
- Through the raw files + build.py + termbase_assemble.py 5 burmese my plain (aligned 226, outside 14, no errors). sha256 now `dbc048698d57557f5a6900a770d799f0deecdc6ec29cfe9ff1bb4d378d38e0d6` (before `ee9018fbfe855b6e9595d95e26eab0176de35802502f73a1a6b16888328fba1f`). Backups: `raw-*.before-review.tsv`.

## Change 2026-11-22 (review fix round 2), decided by the coordinator under the user's standing go-ahead
- From `rails/termbase-proposals-2.tsv`: the stale phrase entries after the review change: mātughātako / pitughātako / saṅghabhedako / ruhiruppādako ānantariko «… ချက်ချင်း အကျိုးပေးသော ကံ ရှိသော», Bhagavatā abhisambuddhāni «မြတ်စွာဘုရား … ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူခဲ့သော», Dukkhaṃ parinipphannaṃ «ဒုက္ခ … ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော»; natthika «ကံ၏ အကျိုး မရှိ» (A20).
- Not added as senses (the senses file stays as built): viloketi «ကြည့်ရှုသည်» (^5-401, sabbā ca disā viloketi), ādāna «ယူခြင်း» (adinnādāna ^5-546), añño «အခြား» (anañño ^5-89 / ^5-90). These are **context senses for the rails step**, like pi-4's phalaṃ note: the rails keep the review wording there and classify the rows as context senses.
- sha256 now `e45d99f4d08fed7d0343cbdf86c5d5d06d91db836b4b3af6b6b150b6adf6e5fa` (before `dbc048698d57557f5a6900a770d799f0deecdc6ec29cfe9ff1bb4d378d38e0d6`). Backups: `raw-*.before-review2.tsv`.
