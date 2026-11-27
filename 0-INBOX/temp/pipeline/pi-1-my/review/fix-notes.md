# pi-1 Burmese rails: bilingual-review fixes (2026-11-17)

Brief: `review/fix-brief.md`. Inputs: `report-A.md` (A1–A5), `report-B.md` (B1–B11). Built by `rails/regen_rails.sh`:
rails layer `rails/my_formulas_rails.py` (new patches L28–L35, one source string = every copy) and the new
`rails/apply_fixes.py` (F1–F3, explicit rules with Pāli triggers and expected counts, log `rails/fixes-log.tsv`), run right
after `apply_termbase.py`. No zero-shot chapter, generator or my_formulas.py touched (protected md5 unchanged).

## Applied: 159 lines changed against the pre-fix rails (zero-shot → rails now 704 lines)

| ID | where | instances | lines per chapter |
|---|---|---|---|
| bahiddhā (B3, B5) | L28 (my_formulas TERMS: bahiddhā, ajjhattabahiddhā, bahiddhārammaṇā, ajjhattabahiddhārammaṇā) | 27 «သူတစ်ပါး၌» → «မိမိ၏ ပြင်ပ၌» (0 left) | 1-matika 4, 3-03 4, 4-01 4, 5 2 |
| A1 | L29 (TITLES Abyākatavipāko) | 1 | 2-04 1 |
| A2 | L29 (TITLES Akusalavipākaabyākataṃ) | 1 | 2-05 1 |
| A3 | L30 (TITLES Aṭṭhamahāvipākā) | 2 (heading + ^1-498) | 2-04 2 |
| A4 | L31 (TITLES Suddhikasuññataṃ, Chandādhipateyyasuddhikasuññatā) | 4 | 2-05 4 |
| A5 | L32 (my_formulas «cetasikaṃ neva sātaṃ nāsātaṃ») | 15 | 2-01 3, 2-04 12 |
| B1 | F2 (Pāli trigger: the lobha list) | 3 lists (6 items) | 4-01 2, 4-02 1 |
| B2 | F3 (^1-1387 only) | 1 | 5 1 |
| B4 | L33 (make_ch4 Dasa kilesavatthūni) | 1 (^1-1235; ^1-1565 already so) | 4-02 1 |
| B8 | F1 (Pāli trigger «X-bhūmiyaṃ kāmāvacare …», item count checked) | 21 segments, 49 plane items | 4-01 9, 4-02 12 |
| B9 | L34 (make_ch4 kusalābyākatā / kusalākusalābyākatā dhammā; make_ch5 ^1-1418) | 48 | 4-01 21, 4-02 26, 5 1 |
| B11 | L35 (make_ch3 rule: list follows directly; make_ch4 ^1-1201) | 48 | 3-02 5, 3-03 42, 4-02 1 |

Counts that differ from the brief, by the rule «all instances, identical Pāli = identical Burmese»:
- B8: 21, not 18. The three «Na X-bhūmiyaṃ kāmāvacare …» segments (^1-1282, ^1-1284, ^1-1286) have the same plane items
  and the same awkward locative; same pattern applied.
- B11: 48, not 36. The 12 «yaṃ vā panaññampi atthi rūpaṃ (na) kammassa katattā ākāsadhātu …» lines (3-03) are the same
  frame (list directly after «… အခြား ရုပ် ရှိသမျှ»). Not touched: the Pāli «…, rūpāyatanaṃ» (comma, 3-02 1×) and «… –»
  (^1-1535, chapter 5) cases, which keep «ရှိသမျှလည်း» as written.
- B9: the two «sabbeva kāmāvacarā kusalākusalābyākatā» lines (three items, no «နှင့်») are not this pattern; unchanged.

## Termbase change (user-approved, the only one)

`termbase/decisions-A.tsv`, new section «Review fix, user-approved 2026-11-17», 4 entries: bahiddhā|1 «မိမိ၏ ပြင်ပ၌»,
dhammā bahiddhā|0 / bahiddhā dhammā|0 «မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရား», Bahiddhā dhamme ārabbha|0
«မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရားတို့ကို အာရုံပြု၍». `termbase_assemble.py 1 burmese my plain`: no errors (67 decided,
30 aligned, 1 outside); diff = exactly those 4 lines. New sha256 `eafe0f8d0f22ece0dd5a4732782fac288959db69c01a3f3f21c325d6f30be51c`
(was `09668de0fa34…`), noted in `termbase/APPROVED.md`, recorded in regen_rails.sh (`TB_SHA`, checked) and in
`rails/protected-md5-before.txt`. The other senses stay («ပြင်ပ၌» 45× in the bases of mastery, «အပြင်ဘက်» for ito bahiddhā).
Classification updated only for this: `rails/adherence-zeroshot.txt` re-run with the new termbase (487 → 502 misses, the 15
new ones all bahiddhā keywords), one GENUINE family L28 in `classify_misses.py`, line-scan families L28 (req / forbid).

## Checks (regen_rails.sh, two runs, byte-identical chapters, logs and reports)

protected md5 unchanged (33 files); termbase hash = recorded lock; ids + text_pe + marks OK in all 14 chapters (chk-pe copies
removed); typography OK; adherence: zero-shot 502 misses (input reproduced), rails 100 misses = ARTEFACT 98 + INFLECTION 2,
GENUINE fixed 420, GENUINE or unknown left 0; align: 418 repeated Pāli sentences, 0 with differing Burmese; hidden: 0
unmatched; line scan 0 lines left; ALL CHECKS PASSED.

## Not applied: blocked by the locked termbase (need a user decision)

Each makes the rails miss a locked termbase term that the adherence check tests in that segment (B6 built and run: 6
UNKNOWN misses, run failed; B7 and B10 tested with adherence_my.occurs on the changed segment text: the keyword fails,
either stem for B7), and the brief allows no termbase or classification change except bahiddhā.

- **B6 cittahetuka** «စိတ်ကို အကြောင်းပြုသော»: termbase cittahetukaṃ = «စိတ်ကို အမြစ်ပြုသော» (checked at ^1-1201) and
  hetukaṃ = «အမြစ်» only (checked at ^1-666, 667, 769, 770, 1535). The hetū "causes" sense is a separate headword (hetū).
  To apply: decision cittahetukaṃ|0 «စိတ်ကို အကြောင်းပြုသော», plus an ARTEFACT row for hetukaṃ inside cittahetukaṃ
  (compound with its own entry, as dvedhāpatho); patches ready: my_formulas `CITTAHETUKA`, make_ch3 `CITTAHETU` (6 places).
- **B7 byāpatti / byāpajjanā / byāpajjitattaṃ**: the termbase itself fixes the two stems, byāpatti «ဖောက်ပြန်ခြင်း» and
  byāpajjanā «ညှဉ်းဆဲလိုခြင်း» (both checked at ^1-418, ^1-419; the same list is in 7 places: ^1-418, 419, 1066, 1120,
  1142, 1160, 1237). Option following the termbase's byāpatti: byāpajjanā|0 «ဖောက်ပြန်နေခြင်း», byāpajjitattaṃ
  «ဖောက်ပြန်ထားသော အဖြစ်» (cittassa byāpatti «စိတ်၏ ဖောက်ပြန်ခြင်း» then fits too).
- **B10 ucchedadiṭṭhi** (drop «သေပြီးနောက်»): termbase uccheda «သေပြီးနောက် ပြတ်စဲသွားသည်» and ucchedadiṭṭhi
  «အတ္တသည် သေပြီးနောက် ပြတ်စဲသွားသည်ဟူသော အယူ» (checked at ^1-1323, ^1-M2-112). To apply: decisions uccheda|0
  «ပြတ်စဲသွားသည်», ucchedadiṭṭhi|0 «အတ္တသည် ပြတ်စဲသွားသည်ဟူသော အယူ»; one patch (my_formulas «ucchedadiṭṭhi») changes all
  3 places, the Mātikā item ^1-M2-112 included (same Pāli).

## Note for the next termbase review

The adherence test is order-free, so A1–A3 and B9 pass, but these termbase entries still show the old wording or order:
Abyākatavipāko, vipākaabyākataṃ, mahāvipākā, Sāsavā kusalābyākatā dhammā, Sāsavā kusalākusalābyākatā dhammā,
akusalābyākatā. Aligning them would need user approval.

## B6 / B7 / B10 applied (2026-11-17, coordinating session, user-approved termbase change)
- Termbase: decisions-A.tsv section «Review fix B6/B7/B10, user-approved 2026-11-17» (cittahetukaṃ|0, byāpajjanā|0, uccheda|0, ucchedadiṭṭhi|0); termbase_assemble.py: no errors (67 decided, 34 aligned, 1 outside); sha256 3c8cc8d0654cfc94d1b337859305056d06c308b10693dd44f07e3beb821a9972 recorded in termbase/APPROVED.md, regen_rails.sh TB_SHA and protected-md5-before.txt.
- Rails layer (my_formulas_rails.py): L36 B6 CITTAHETUKA (my_formulas) + CITTAHETU (make_ch3) = «စိတ်ကို အကြောင်းပြုသော» → 6 places; L37 B7 byāpajjanā «ဖောက်ပြန်နေခြင်း», byāpajjitattaṃ «ဖောက်ပြန်ထားသော အဖြစ်» (make_ch2-04-05, make_ch4) → 7 copies of the dosa list; L38 B10 ucchedadiṭṭhi without «သေပြီးနောက်» → 3 places incl. the Mātikā ^1-M2-112.
- Classification: adherence-zeroshot.txt re-run against the new termbase (510 misses); GENUINE families L36–L38; ARTEFACT row for hetukaṃ inside cittahetukaṃ (own entry); line_scan families L36–L38.
- Checks (regen_rails.sh, run twice, byte-identical): structure OK ×14; adherence rails 105 misses = 103 ARTEFACT + 2 INFLECTION, GENUINE 0 (428 fixed); align 0 / hidden 0; line scan 0; zero-shot and generators unchanged (33 md5). Old forms left: 0; the 7 «မညှဉ်းဆဲလိုခြင်း» are abyāpāda (a different word).
