# pi-2 Burmese termbase: APPROVED and LOCKED

- Approved by the user on 2026-11-18 ("Approve and lock").
- File: `AI_translation/burmese/pi-2-pali-burmese-termbase-plain.md` (4956 headwords, 5064 senses; 191 decided, 85 aligned, 1 outside: kappasahassāni «ကမ္ဘာ ထောင်ပေါင်း»). Decisions: `decisions-A.tsv`, report: `termbase-decisions.md`.
- sha256 `45bf057a4596dcdd33257c52b93e29a302afc0892aabfc0f159c8a6a635ab15f`.
- Approved as built, incl. the 27 senses that depart from pi-1 (7 different meaning, 14 pi-1 term absent from the pi-2 text so the pi-2 form kept, 6 kept for context).
- pi-1's binding rules apply: proper names stay names; nāma-rūpa «စိတ်ပိုင်း / ရုပ်ပိုင်း»; bahiddhā «မိမိ၏ ပြင်ပ၌» (`pi-1-my/termbase/APPROVED.md`).
- Known doubt (not changed): samāpattiyā at ^2-511 takes pi-1's «ကျူးလွန်ခြင်း» (offence) where the context is good states; report in the rails step.
- Locked: the rails translation uses it as a fixed reference. Never edit the termbase file; a term that turns out wrong is reported to the user.

## Change approved by the user, 2026-11-18 (bilingual review A8 / B2)

- Approved by the user directly in the coordinating session ("Both (Recommended)").
- **A8** maccu = «သေဆုံးခြင်း» (plain death; not the personified «သေမင်း»), distinct from maraṇa «သေခြင်း» and kālakiriyā «ကွယ်လွန်ခြင်း».
- **B2** siṅgāratā = «ဟန်လုပ်ခြင်း» (affectation, putting on airs; not bragging «ကြွားလုံး ထုတ်»); siṅgaṃ «ဟန်လုပ်မှု» (see the next section: Siṅgaṃ has its own entry).
- Made only through `decisions-A.tsv` (section «Review fix A8 / B2, user-approved 2026-11-18», 2 entries) and `termbase_assemble.py 2 burmese my plain` (no errors; 191 multi, 87 aligned, 1 outside).
- Locked file now: sha256 `6ffa74840ba6c9e018ae4abe089aa6116d0148da7cee4a94c04436fe4d53e658` (before: `45bf057a4596dcdd33257c52b93e29a302afc0892aabfc0f159c8a6a635ab15f`). regen_rails.sh checks this hash.

## Change approved by the user, 2026-11-18 (bilingual review B1, B2 completion)

- Approved by the user in the coordinating session (B1: "Add 'path' senses"; B2: siṅgaṃ «ဟန်လုပ်မှု» with siṅgāratā).
- **B1** (^2-U30 kummaggasevanā): the object is the wrong path, not persons. New senses: sevanā|1 «မှီဝဲခြင်း» and nisevanā|1 «နီးကပ်စွာ မှီဝဲခြင်း» (persons keep sevanā|0 «ပေါင်းသင်းခြင်း», nisevanā|0 «နီးကပ်စွာ ပေါင်းသင်းခြင်း»); taṃsampavaṅkatā = «ထိုလမ်းမှားဘက်သို့ ညွတ်ကိုင်းခြင်း» (only at ^2-U30). Made upstream: keyword map ^2-U30 (assembled file and mapper-my/17-khuddakavatthuvibhango.mapped.md, 3 values), senses/agg-part1.tsv (3 lines), senses/decisions-part1.txt (3 lines), senses rebuilt (VERIFY OK, 5066 senses, first 82 = sample) and copied to AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md (VERIFY OK).
- **B2 completion**: Siṅgaṃ|0 «ဟန်လုပ်မှု» (it has its own entry).
- `termbase_assemble.py 2 burmese my plain`: no errors (5066 senses; 191 multi, 88 aligned, 1 outside).
- Locked file now: sha256 `715bebdddc3ae9a65a2032124ea52b6b7baa69c725a083883e863d7f688e8769` (before: `6ffa74840ba6c9e018ae4abe089aa6116d0148da7cee4a94c04436fe4d53e658`). regen_rails.sh checks this hash.
