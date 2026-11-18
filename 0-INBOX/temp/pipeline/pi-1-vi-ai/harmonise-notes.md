# pi-1 Vietnamese plain zero-shot: harmonise pass (harmonise-brief.md)

Scripts: vi_common.py (aligned lines, backup), find_divergences_vi.py, harmonise_vi.py, verify_vi_all.py, probe_harm_vi.py.
Backup of the pre-pass files: backup-pre-harmonise\ (written once). Log: harmonise-log.tsv (450 lines changed).
Divergence reports: divergences-pre.md (backup), divergences.md (after the pass).

## Divergence scan (before the pass)
(a1) segments 0, (a2) lines 0, (a5) synonym-string words 0: identical Pāli already had identical Vietnamese (each builder
imported the earlier ones). (a3) 4 clause groups and (a4) 16 item groups are split artefacts: the Pāli itself differs
(full vs «…pe…» lists, a stray space before «…pe…», «;» vs «, tức là» splitting), not divergences.
(b) every listed term is uniform across parts (jhāna formula, paṭipadā / abhiññā, adhipateyya, kasiṇa, formless spheres,
sasaṅkhāra, ṭhapetvā, tadekaṭṭhā, kammassa katattā, sāta / asāta, viññatti, upacaya, santati, diṭṭhigata, the defilement
strings and group names, patiṭṭhāho, bahūsu, sammappadhāna).

## Rules applied
D1-frame (3-02 = 149, 3-03 = 237): «– đây là loại vật chất <pred>.» -> «– vật chất này <pred>.»;
  «Đây là loại vật chất <pred>.» -> «Vật chất này <pred>.» (Pāli «idaṃ taṃ rūpaṃ»). The 3-01 predicates are unchanged.
D2-four-dots (2-01 = 8, 2-02 = 15, 2-03 = 2, 2-04 = 23, 2-05 = 14, 5 = 2; 64 in all): line-final «….» -> «…» where the
  Pāli has «…pe….». All 64 are at a line end; none is in the protected sample or the matrix.

## Decisions kept (no change)
3. «Tikaṃ.»: 3-01 «Phân loại theo nhóm ba.» closes the threefold classification of matter (heading ##### Tikaṃ inside
   Ekakaṃ … Ekādasakaṃ = «Phân loại theo nhóm một … mười một», same set in 3-03); 4-01 ^1-1058 and ch5 ^1-1440 «Các bộ
   ba.» close the summary of the 22 matrix triads («bộ ba» / «bộ đôi», as Cūḷantaradukaṃ «Các bộ đôi xen giữa nhỏ»).
   Different units: both kept. Dukaṃ / Ekakaṃ occur only in the 3-01 series.
4. bhūmi: «giai đoạn» (2-03 / 2-05 path stages), «cõi» (ch5 catūsu / tīsu bhūmīsu, heading «Tâm thiện thuộc ba cõi»),
   «Ở cấp độ có X» (4-01 ^1-988 … 1005, 4-02 ^1-1275 … 1286); ch5 has no X-bhūmiyaṃ line. Consistent.
5-7. sukhabhūmiyaṃ split, akakkhaḷatā / kakkhaḷa, sammappadhāna = sammāvāyāma: kept.
cittuppāda: «Phần về sự sinh khởi của tâm» (approved heading Cittuppādakaṇḍa) vs ch5 «loại tâm» (countable class,
   73 lines); different use, kept.
3-01 «Có loại vật chất là X» (Atthi rūpaṃ X, 29 lines): one «là», not the doubled frame; unchanged.

## Builder constants that would need the same change (do NOT rebuild: it would drop the pass)
- build_3-02_3-03_vi.py line 553 / 554: «Idaṃ taṃ rūpaṃ upādā. / no upādā.» = f"Đây là {KIND} …" -> f"Vật chất này …".
- build_3-02_3-03_vi.py line 617: f"đây là {KIND} {term(q2)}{end}" -> f"vật chất này {term(q2)}{end}".
- Four dots: the «…pe…» -> «…» conversions keep the Pāli's following «.»: build_2-01_2-02_vi.py (lines 190, 203, 216,
  457), build_2-03_vi.py 155, build_2-04_vi.py 331, build_2-05_vi.py 102, build_5_vi.py 625 / 626 (ELL + "."); a
  line-final «…pe….» would need «…» without the full stop.
- The byte-for-byte self-tests of the later builders (re-rendering earlier parts) would also need the new strings.
- The per-part checkers verify_vi_*.py do not encode the old frame or «….»; they pass unchanged.
