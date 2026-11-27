# pi-1 Burmese termbase: APPROVED and LOCKED

- Approved by the user on 2026-11-17 ("Approve with rules").
- File: `AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md` (2485 headwords, 2520 senses; 67 decided, 26 aligned, 1 outside). Decisions: `decisions-A.tsv`, report: `termbase-decisions.md`.
- Approved with it, as changes to the earlier approved sample wording:
  - paṭicca = «အကြောင်းတို့ကို မှီ၍»; the Mātikā item paṭiccasamuppāda becomes «အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ».
  - Suññata = «ဆိတ်သုဉ်းခြင်း»; the heading Suññatavāro becomes «ဆိတ်သုဉ်းခြင်း ဖော်ပြချက်».
  - The outside term vibhava = «ဘဝ ပျောက်ကွယ်ခြင်း».
- Two binding rules for the rails translation:
  1. **Proper names stay names.** A termbase term for a compound member is never applied inside a proper name: Paranimmitavasavattī stays «ပရနိမ္မိတဝသဝတ္တီ» (para = «သူတစ်ပါး» only where para means "others"); the same for the other realm and deva names.
  2. **nāma-rūpa keeps the approved pair** «စိတ်ပိုင်း / ရုပ်ပိုင်း»: rūpa(ṃ) in nāmarūpa is «ရုပ်ပိုင်း», not the plain «ရုပ်».
- Locked: the rails translation uses it as a fixed reference. Never edit the termbase file; a term that turns out wrong is reported to the user.

## Change approved by the user, 2026-11-17 (bilingual review B3 / B5)

- **bahiddhā = «မိမိ၏ ပြင်ပ၌» (outside oneself)** for the "external, not one's own" sense, book-wide (Mātikā triad items bahiddhā dhammā «မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရား», ajjhattabahiddhā, bahiddhārammaṇā, ajjhattabahiddhārammaṇā; «ajjhattaṃ vā bahiddhā vā» incl. the four elements; ^1-1435). The other two senses stay: «ပြင်ပ၌» (bases of mastery), «အပြင်ဘက်» (ito bahiddhā).
- Made only through `decisions-A.tsv` (section «Review fix, user-approved 2026-11-17»: bahiddhā|1, dhammā bahiddhā|0, Bahiddhā dhamme ārabbha|0, bahiddhā dhammā|0, 4 entries) and `termbase_assemble.py 1 burmese my plain` (no errors; 67 decided, 30 aligned, 1 outside).
- Locked file now: sha256 `eafe0f8d0f22ece0dd5a4732782fac288959db69c01a3f3f21c325d6f30be51c` (before: `09668de0fa3475535293616d4c96bf0717a4638b0b69cafc11dd302e7c1bbb90`). The lock otherwise stands; regen_rails.sh checks this hash.

## Change approved by the user, 2026-11-17 (bilingual review B6 / B7 / B10)

- Approved by the user directly in the coordinating session ("Yes, do it here", after "Approve all three").
- **B6** cittahetukaṃ = «စိတ်ကို အကြောင်းပြုသော» (caused by mind; hetuka here is not the technical root).
- **B7** byāpajjanā = «ဖောက်ပြန်နေခြင်း», one stem with byāpatti «ဖောက်ပြန်ခြင်း» (byāpajjitattaṃ «ဖောက်ပြန်ထားသော အဖြစ်»).
- **B10** uccheda = «ပြတ်စဲသွားသည်», ucchedadiṭṭhi = «အတ္တသည် ပြတ်စဲသွားသည်ဟူသော အယူ» (no added «သေပြီးနောက်»).
- Made only through `decisions-A.tsv` (section «Review fix B6/B7/B10, user-approved 2026-11-17», 4 entries) and `termbase_assemble.py 1 burmese my plain` (no errors; 67 decided, 34 aligned, 1 outside).
- Locked file now: sha256 `3c8cc8d0654cfc94d1b337859305056d06c308b10693dd44f07e3beb821a9972` (before: `eafe0f8d0f22ece0dd5a4732782fac288959db69c01a3f3f21c325d6f30be51c`). regen_rails.sh checks this hash.
