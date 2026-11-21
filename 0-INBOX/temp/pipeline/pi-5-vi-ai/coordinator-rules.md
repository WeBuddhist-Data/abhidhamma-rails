# pi-5 Vietnamese zero-shot: coordinator rules (binding for every chapter agent, added 2026-11-21)

These extend vi-zeroshot-brief.md. Where they differ from an earlier finished chapter, the rule wins; the harmonise pass aligns the earlier chapter.

- "Āmantā?" (with a question mark) = «Đúng vậy?» as the sample (^5-95).
- punabbhava = «sự hiện hữu mới» (pi-2); upapatti / upapajjati = tái sinh.
- ruhiruppādaka = «kẻ làm chảy máu» (no «Như Lai»: not in the Pāli).
- One Pāli word that the argument turns on keeps one Vietnamese word throughout (do not split it by context, e.g. anāsava).
- Keep the Pāli's own punctuation: a "." stays a full stop even where a question is meant; report it. Missing commas may be rendered as meant.
- Add no word that is not in the Pāli and drop none that is (a repeated word such as a second dhammā stays).
- Never merge sentences: every Pāli sentence keeps its own Vietnamese sentence, even when the Pāli repeats itself.
- Vagga close: "Tassuddānaṃ –" = «Tóm tắt của chương này –» byte for byte; the closing vagga name line = the vagga heading wording from vi-zeroshot-terms.md with a full stop; each kathā name in its closing line and in the uddāna uses the same wording; a kathā name or term already used in an earlier chapter keeps that wording (read the finished chapters' notes).
- Fifty-groups (set in ch13): "Mahāpaṇṇāsako." = «Nhóm năm mươi lớn.»; "Tassāpi uddānaṃ –" = «Tóm tắt của nhóm năm mươi này nữa –»; "Dutiyo paṇṇāsako." = «Nhóm năm mươi thứ hai.» (same pattern).
- Cross-book terms keep the pi-1-4 wording exactly, e.g. gotrabhū = «người chuyển đổi dòng dõi» (pi-4). Where a pi-1/pi-2 fixed formula renders a word differently from the debate's word (e.g. kāyikaṃ dukkhaṃ), report it in your notes; do not decide it yourself.
- Where two finished chapters disagree, follow the pi-1-4 wording if there is one, otherwise the earlier chapter (the sample first), and list the clash in your notes.
- Vagga files 10-31: build_10_vi.py, build_11_vi.py and build_12_vi.py are the models.
- Write files with LF line endings: open(..., "w", encoding="utf-8", newline="\n").
- Grep only single named files, never a folder (not even the pi-5 output folder); use pi-5-vi-ai\find_pi1234_rails_vi.py for pi-1-4 lookups.
