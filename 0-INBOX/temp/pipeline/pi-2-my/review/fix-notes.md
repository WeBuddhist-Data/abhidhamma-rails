# pi-2 Burmese rails: bilingual-review fixes (2026-11-18, two rounds)

Brief: `review/fix-brief.md`; second round: the user's decisions on the three flagged points (coordinator message,
2026-11-18). Inputs: `report-A.md` (A1–A9), `report-B.md` (B1–B6). Built by `rails/regen_rails.sh`: rails layer
`rails/my_formulas_rails.py` (patches L69–L73; layer 156 → 164 source patches) and `rails/apply_fixes.py` (F1–F7,
explicit rules with segment IDs, Pāli triggers and expected counts; F7 a pattern function with its own checks; log
`rails/fixes-log.tsv`), run right after `apply_termbase.py`. Not touched by me: zero-shot chapters, generators,
my2_formulas.py, termbase, decisions-A.tsv, APPROVED.md, senses, keyword map, pi-1 (protected md5: 59 files unchanged;
termbase sha256 = the current lock 715bebdd…, set upstream). Pre-fix rails kept in `review/fix-backup/rails-before/`.

## Applied: 42 lines changed against the pre-fix rails (zero-shot → rails now 367 lines, was 329)

| ID | where | instances | lines per chapter |
|---|---|---|---|
| A1 | F1 (^2-188) | 1: the source quote slip rendered for its intended reading (as 1-khandha / 2-ayatana / 5-indriya); dashes 6 = Pāli 6, quotes balanced | 3-dhatu 1 (l.102) |
| A2 | L69 (my2_formulas r_item, in memory: the predicate «X rūpā.» = rūpino) | 3 (Dasāyatanā / Dasa dhātuyo / Sattindriyā rūpā.) = «… ရုပ် ဖြစ်သော သဘောတရားများ ဖြစ်ကြသည်»; script over every «X rūpā / rūpaṃ.» predicate: ch18 ^2-1043 (4) and ch1 already so | 2-ayatana 1, 3-dhatu 1, 5-indriya 1 |
| A3 ch6 | L70 (make_ch6 opening(), subject-first branch = exactly the compressed openings) | 10 lines: ^2-280, 284, 286, 294, 296, 297, 319, 331, 339, 346 («… နှင့်အတူ ဖြစ်၍ … နှင့် ယှဉ်တွဲလျက် / ကင်းကွာလျက် [တိုက်တွန်းမှုဖြင့်] …»; kiriyā neva kusalā … = pi-1's attributive «ပြုရုံမျှသာ ဖြစ်သော၊ … မဟုတ်သော» before the noun) | 6: 10 |
| A3 ch14/15 (round 2) | F7 (pattern function over the Burmese, 9 segment IDs, Pāli trigger) | 9 lines: ^2-704, 706, 709, 711, 712 (ch14), ^2-726, 731, 737, 745 (ch15): the same adverbial qualifier Burmese, subject first as ch6 (abstainer genitive «… ရှောင်ကြဉ်နေသူ၏» before the subject); checked: groups = Pāli «-sahagat-» count, «တိုက်တွန်းမှုဖြင့်» = «sasaṅkhārena» count, and ^2-712 / ^2-726 = ch6 ^2-339, ^2-737 = ch6 ^2-319 (identical Pāli openings, byte-identical Burmese openings) | 14: 5, 15: 4 |
| A4 | F2 (^2-223) | 2 sentences «…ဖြစ်ကြသည်၊ သို့သော် – “…”ဟု ခေါ်ဆို၍ မရ»; no other «၊ – “» in the book | 5-indriya 1 (l.51) |
| A5 | F3 (^2-184) | 1 «… ဖြစ်ပေါ်သည်၊ မနောကိုလည်းကောင်း»; no parallel needed it | 3-dhatu 1 (l.73) |
| A8 | L71 (make_ch2-4 SYN4, make_ch6 maraṇa-s) | 2 maccu «သေဆုံးခြင်း» (^2-193, ^2-236); «သေမင်း» left 0 | 4-sacca 1, 6: 1 |
| B1 (round 2) | F6 (^2-U30) | 1 «ဤလမ်းမှားကို မှီဝဲခြင်း၊ နီးကပ်စွာ မှီဝဲခြင်း၊ ကောင်းစွာ မှီဝဲခြင်း၊ ဆည်းကပ်ခြင်း၊ ကောင်းစွာ ဆည်းကပ်ခြင်း၊ ကိုးကွယ်ခြင်း၊ ကောင်းစွာ ကိုးကွယ်ခြင်း၊ ထိုလမ်းမှားဘက်သို့ ညွတ်ကိုင်းခြင်း ရှိသမျှ»; the 3 pāpamittatā definitions (persons) unchanged | 17: 1 (l.619) |
| B2 | L72 (make_ch17 item table) | 6 occurrences in 3 lines: siṅgaṃ «ဟန်လုပ်မှု» (mātikā item 35 ^2-832, heading ^2-17-2-10-0, ^2-852 ×3 incl. the closing quote), siṅgāratā «ဟန်လုပ်ခြင်း»; «ကြွားလုံး» left 0 | 17: 3 (l.5, 94, 96) |
| B3 | F4 (^2-724, ^2-796) | 2 «ဤသာသနာ၌ ရဟန်းသည်»; «ဤသာသနာတော်» left 0 | 15: 1, 16: 1 |
| B4 | L73 (make_ch12-14 list_my: sattesu joined with a space) | 8 (mettā / karuṇā / muditā / upekkhā ×2); the 2 ch3 lines already so | 13: 8 |
| B5 | F5 (^2-392) | 1 «…]၊ ပေါ်ထွက်စေ၏»; script over all 37 «word [variant] word» places: no other list item missing «၊» | 8: 1 (l.9) |
| B6 | reverted (round 2, user decision): L74 removed | ^2-1023 back to the pre-fix literal «ထိုညဖြင့် ည သုံးဆယ်သည် တစ်လ» (termbase rattiyo «ည», rattiyo māso «ည … တစ်လ»); ch18 = the pre-fix rails | 18: 0 |

Kept as decided: A6, A7 (source slips translated as written), A9 («ဆဋ္ဌမ အာရုံခံ နယ်ပယ်»). Nothing left unapplied.

## Classification / termbase-dependent inputs (only for the user-approved termbase changes)

- `rails/adherence-zeroshot.txt` re-run with each new termbase: 601 → 604 (round 1: maccu ×2, siṅgāratā) → 608 (round 2:
  Siṅgaṃ / siṅgaṃ at ^2-17-2-10-0, ^2-832, ^2-852 and taṃsampavaṅkatā at ^2-U30, the zero-shot's «ကြွားလုံး ထုတ်မှု» /
  «ထိုသူတို့ဘက်သို့ …»). sevanā / nisevanā keep a persons sense |0, so the zero-shot passes them.
- `classify_misses.py`: GENUINE families L71 maccu, L72 siṅgāratā / siṅgaṃ / Siṅgaṃ (decision Siṅgaṃ|0; the round-1
  «termbase conflict» row for Siṅgaṃ is removed), F6 taṃsampavaṅkatā; `applied_ids` also reads `fixes-log.tsv`.
  Explicit `ZS_FORM` table: the keyword map at ^2-U30 was revised after the review (mapper-my/map-harmonise-notes.md
  «Post-review revision») and now gives the rails form, so for sevanā / nisevanā / taṃsampavaṅkatā at ^2-U30 the
  GENUINE test takes the zero-shot's own (pre-revision) form from that table.
- `line_scan.py`: families L71 (req / forbid), L72 (req / forbid), F6 (req, the kummagga list).

## Checks (regen_rails.sh; second run byte-identical: 19 chapters + all rails/ tsv / txt outputs, 32 files)

protected md5 unchanged (59 files); termbase sha256 = recorded lock 715bebdddc3a…; plain build = zero-shot 19 / 19;
ids + text_pe + marks OK in all 19 files; typography OK; adherence: zero-shot 608 misses (input reproduced), rails 32431
checked, 178 misses = ARTEFACT 133 + INFLECTION 45 (all known rows), GENUINE fixed 479, GENUINE or unknown left 0;
align: 634 repeated Pāli sentences, 73 with differing Burmese = exactly the zero-shot's accepted set (71 topic noun,
2 kept), 0 new; hidden: 0 unmatched; pi-1 identity 321 / 321 (no pi-2 sentence equal to a pi-1 sentence changed);
line scan 0 lines left (zero-shot 326 flags); ALL CHECKS PASSED.

## Notes

1. **A3 and pi-1 at clause level.** pi-1 is unchanged. Its 2-02 (l.297), 2-04 (l.298) and 2-05 (l.206) openings keep the
   old attributive form, so the identical opening clauses of ch6 ^2-319 / ^2-346 / ^2-331 and ch15 ^2-737 / ^2-745 now
   differ from pi-1 inside the sentence (the sentences themselves are not in pi-1: identity 321 / 321).
2. **^2-709 / ^2-711** (ch14) carry the hīnaṃ … paṇītaṃ / adhipati tail of pi-1 2-02 (not in ch6): the adverbial
   qualifier run comes first, then «၊ [abstainer genitive] ယုတ်ညံ့သော… … မွန်မြတ်သော ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်စိတ်သည်
   ဖြစ်ပေါ်ပြီးသော», so those attributives stay directly before their noun; the misplaced «တိုက်တွန်းမှုဖြင့်» (after
   «ယုတ်ညံ့သော») is back after the last qualifier pair, as in the Pāli («… ñāṇavippayuttaṃ sasaṅkhārena hīnaṃ …»).
3. **B6** is the literal «ည» again, by the user's decision.
