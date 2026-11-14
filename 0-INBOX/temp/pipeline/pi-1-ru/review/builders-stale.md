# Rails builders made stale by apply_review_fixes_ru.py (2026-11-14)

The builders in `pi-1-ru\rails\` still produce the pre-review wording. After any rebuild, run in this order:

1. the builder(s)
2. `rails\fix_bare_comma_ru.py`
3. `review\apply_review_fixes_ru.py` (delete or refresh `review\backup-pre-fixes\` first: the script reads only from the backup, so a fresh backup of the rebuilt files is needed)

Note: `fix_bare_comma_ru.py` and `find_divergences_rails_ru.py` treat «это элемент осязаемого, – это» (^1-700, ^1-817, ^1-983, rule G3-comma-add) as a bare comma. Running `fix_bare_comma_ru.py` after this script removes those three commas again; the divergence check reports them as 3 bare lines (expected).

| rule (fixes-log.tsv) | builder constant(s) that would need the new wording |
|---|---|
| U1-saraga | `build_rails_sample_ru.py` `S_ALOBHA` (l. 586 f.: «отсутствие проявления / состояния страсти»); `build_rails_2-04_ru.py` `S_LOBHA` (l. 119: «проявление страсти, состояние страсти») |
| U2-asantutthita | `build_rails_sample_ru.py` dyad name `"1-M2-140"` (l. 428); ^1-1378 in `build_rails_4-02_4-03_ru.py` (l. 835) takes it via `kho('1-M2-140', 0)` |
| U3-bhanavara | `build_rails_sample_ru.py` `BHANAVARA_1` (l. 71); `build_rails_2-01_2-02_ru.py` `"Dutiyabhāṇavāro."` (l. 628); `build_rails_3-02_3-03_ru.py` `BHANA_8` (l. 608, `BHANA_1` follows `BHANAVARA_1`); `build_rails_4-01_ru.py` assert on `EXACT["Nikkhepakaṇḍe paṭhamabhāṇavāro."]` (l. 423, «Первый раздел …» → «Первая часть …»); `build_rails_4-02_4-03_ru.py` `once(…, "Первый", "Второй")` (l. 396) → `"Первая", "Вторая"` |
| U4-classification | `build_rails_3-01_ru.py` `NUM` table «по N» (l. 52 ff.), `CLASS_N`, `CLOSE_N` and the «Классификация материальной формы по N –» opener (l. 59–61): 2 … 11 → «на N вида / видов»; Ekakaṃ keeps «по одному» (`H_EKAKANIDDESO`, l. 65); `build_rails_3-02_3-03_ru.py` `H_DUKA_N`, `H_TIKA_N` (l. 603–604) and the 3-03 headings / closings built from `T.NUM` |
| U5-vibhatti | `build_rails_3-01_ru.py` `H_VIBHATTI` (l. 63; used for ^1-2-3-0 and, via `T.H_VIBHATTI`, ^1-984 in `build_rails_3-02_3-03_ru.py` l. 647) |
| U6-bhumi | `build_rails_5_ru.py` `K4`, `K3`, `V4`, `V3`, `KR3` (l. 117–122) and the literal strings in l. 572–588 («четырёх / трёх миров» → «уровней»); the note at l. 923. The ch2 heading `"#### Tebhūmakakusalaṃ"` (`build_rails_2-01_2-02_ru.py` l. 632) stays |
| G1-gatam | `build_rails_3-02_3-03_ru.py` the element definitions, l. 523–550 («, считающееся X» → «, то, что считается X») |
| G2-niyyanika | `build_rails_2-03_ru.py` `LOK_JH_R`, `LOK_CITTA_R` (l. 168–169; 2-05 imports them, `HIGHER_R` l. 151) |
| G3-comma-drop (2-01) | `build_rails_sample_ru.py` `body()` frame «{bod}, – это …» (l. 631) for the plain lists of ^1-66 … ^1-145; `build_rails_2-01_2-02_ru.py` «Name list, – это X» (l. 787 note and the matching frame) |
| G3-comma-drop (3-02/3-03) | `build_rails_3-02_3-03_ru.py` `ARE = ", – "` (l. 37) where the answer is a plain list, incl. «(Не) вследствие совершённых действий: X, Y» leads (l. 761) and lists with «…» |
| G3-comma-add | `build_rails_3-02_3-03_ru.py` ^1-700, ^1-817, ^1-983 («это элемент осязаемого, – это»); then skip them in `fix_bare_comma_ru.py` |
| G4-nivoznikla | `build_rails_3-02_3-03_ru.py` `OTHER` (l. 142) when followed by `KAMMA` / «не » + `KAMMA` («ни была» → «ни возникла»); the cittaja, vaṇṇanibhā and okāsa frames keep «ни была» |
| R1-163-ariya | `build_rails_2-01_2-02_ru.py` third-jhāna formula (l. 309) |
| R2-443-sukha | `build_rails_2-04_ru.py` `"sukhasahagataṃ": "сопровождаемое счастьем"` (l. 302) for kāyaviññāṇa ^1-443 → «сопровождаемое удовольствием» |
| R2-headings | `build_rails_2-04_ru.py` `"#### Dvādasa akusalāni"` (l. 391); `build_rails_2-05_ru.py` heading table l. 250–257 (Suddhikasuññataṃ, Suññatapaṭipadā, Suddhikaappaṇihitaṃ, Appaṇihitapaṭipadā, Chandādhipateyyasuddhikasuññatā, Akusalavipākaabyākataṃ), `KIR_ABY` (l. 247, used l. 261 and l. 293) |
| R4-1350-vaca | `build_rails_4-02_4-03_ru.py` l. 324 |
| R4-1344/1345-thana | `build_rails_4-02_4-03_ru.py` l. 305–307 |
| R4-1485-samyojana | `build_rails_5_ru.py` l. 678 (and the note l. 954) |
| R4-1042-ajata | `build_rails_4-01_ru.py` `NEG` (l. 535) |
