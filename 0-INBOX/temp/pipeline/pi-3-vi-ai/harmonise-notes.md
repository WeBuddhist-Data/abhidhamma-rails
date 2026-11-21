# pi-3 Vietnamese zero-shot: harmonise pass (2026-11-20), decisions and remaining divergences

Script: harmonise_vi.py (exact strings, one segment each, asserted counts; reads backup-pre-harmonise/, so rerunnable). Log: harmonise-log.tsv (24 lines). Divergence finder: find_divergences_vi.py (divergences-pre.md = before, divergences.md = after). Probes: probe_harm_vi.py, probe_pron_vi.py. The approved sample (preamble, 1-uddeso, 2-pathamanayo) is unchanged (byte-identical to the backup).

## Lines changed
ch4 5, ch5 1, ch6 1, ch8 1, ch9 4, ch10 5, ch13 2, ch14 1, ch15 4 (total 24). ch3, ch7, ch11, ch12: none.

## Decisions
- Bare abbreviated instrumental members (ch4 ^3-187, ch5 ^3-192, ch10 ^3-346): "Xehi…" = «đối với các X…» (every instrumental head gets «đối với», shared frame); "parāmāsehi dhammehi ye dhammā" = «đối với các hiện tượng là sự hiểu sai lệch, những hiện tượng nào» (ch6/11/12/13/15 form; ch4/ch10 lacked «đối với»). ch5 «là ô nhiễm… là xiềng xích…» → «đối với các ô nhiễm… đối với các xiềng xích…» (pi-1 «Bốn ô nhiễm», «Bốn sự bám víu»). This was the "Xehi dhammehi ye dhammā" point: in all full members the 13 chapters already agree («đối với các hiện tượng <pred>, những hiện tượng nào»).
- Verses: pada = «đề mục» (headings, terms file, ch5/7/11/12/13); a count without padā gets no «mục» (as written); antara without duka = «phần xen giữa» (ch7/9/11/15), with duka «bộ đôi xen giữa»; tato upari = «tiếp theo đó» (ch10; uddhaṃ ch5 «Tiếp theo»), upari (ch4) = «tiếp theo»; gocchaka = «nhóm» (already uniform); viññāṇadhātuyo = «yếu tố thức» (already uniform); navamassa padassa niddese = «trong phần giải thích đề mục thứ chín», saṅgahaṃ gatā = «đã được gộp vào» (ch13 wording for the identical ch10 = ch13 lines); jīvitaṃ = «sự sống» (pi-1 ^1-19, ch7/11); -ti dropped and every line capitalised (already uniform); no word moves to another verse line (ch4 atha now «tiếp đến» at the end of line 3; ch9/ch15 aparante back on line 3).
- As written: ch4 «ba sự thật cũng vậy» → «các sự thật cũng vậy»; ch13 «Bốn khối ngoài khối vật chất» → «Bốn khối vật chất»; ch6/ch14 itthipumaṃ jīvitaṃ «năng lực nữ tính, năng lực nam tính, năng lực sống» → «nữ tính, nam tính, sự sống».
- Pronoun after an association verb: follows the last chain member everywhere (probe_pron_vi.py: ch8 11/11, ch9 2/2, ch10 33/33, ch11 56/56, ch13 31/31, ch15 63/63 lines; the one probe miss, ch10 ^3-343, is the variant bracket after tehi dhammehi, correctly «chúng»). No change.
- «thì» before the predicate: one rule = the sample's B.THI principle (subject ending in the predicate's own verb). The shape (nominative subject whose last member carries «gắn liền với» + association predicate) occurs only in ch7 statements (8 lines), all with «thì»; no other chapter has it (other chapters' predicates follow «những hiện tượng đó»); questions keep the shared frame (^3-287). No change.
- na kehici … vippayuttā: «Không có khối nào, không có lĩnh vực nhận biết nào mà chúng/nó không gắn liền với, nhưng không gắn liền với N yếu tố» is already identical in ch7, ch8, ch11 (33 lines). Final «với» kept: it keeps the fixed term «không gắn liền với» and mirrors the sample's «mà chúng không được gộp vào»; a stranded «với» after «mà» is grammatical. No change.
- ^3-487 (ch15) «ye vippayuttā» without dhammā: «những gì» kept (as written; «những hiện tượng nào» would supply the missing dhammā).
- Kehici «một số hiện tượng trong», «Không có.», «Không gắn liền với bao nhiêu?», khandha-only answers: one form each already (divergences (a3)/(c)). No change.
- Variant brackets: labels already consistent (spelling-only = khác chính tả, other = dị bản; «na hetūhi sahetukehi» dị bản in ch6 and ch10; (bahūsu) = «(nhiều bản)»). No change.
- Dependent-origination links in the instrumental: the pi-2 string in “…” in all 8 chapters (avijjāpaccayā saṅkhārena / saṅkhārehi = “vô minh làm điều kiện cho các sự tạo tác”). No change.

## Remaining divergences (find_divergences_vi.py after the pass)
(a1) segments 0, (a2) lines 0, (a3) sentences 0, (a4) members 0. The finder lowercases a sentence-initial letter after an opening quote, so ch7 ^3-244 «“Cảm giác …”» (sentence start) vs ch2 «“cảm giác …”» is not counted.

## Builder constants that would need the same change (builders not rerun)
- build_4_vi.py: the bare-member strings of ^3-187 (BARE table, «các nút thắt» …) need «đối với» per member and before parāmāsehi dhammehi; VERSE lines 96-102.
- build_5_vi.py: the bare members of ^3-192 («là ô nhiễm…», comment line 73).
- build_10_vi.py: bare members of ^3-346 (line 104 table); VERSE line 215 and the other ^3-352 lines.
- build_13_vi.py: VERSE line 91 (tato upari) and «ngoài khối vật chất».
- build_8_vi.py: ANTARA (line 127) «bộ đôi xen giữa» → «phần xen giữa» for the verse.
- build_9_vi.py: MUC (line 84) and the VERSE (reused by build_15_vi.py).
- build_6_vi.py: VERSE line 1 (itthipumaṃ jīvitaṃ; reused by build_14_vi.py).

## For the user
- ch13 ^3-447 «Bốn khối vật chất» for "Rūpakkhandhā cattāro" is now literal; the agent's «Bốn khối ngoài khối vật chất» (rūpakkhandhā as ablative) was an interpretation.
- ch4 «các sự thật cũng vậy» (no «ba»); ch6/ch14 «nữ tính, nam tính, sự sống» (no «năng lực»).
- ^3-487 «những gì» (no dhammā in the Pāli).
- Verses now keep each Pāli word on its own line, so ch4 line 3 ends «tiếp đến;» (atha) and ch9/ch15 line 3 ends «trong phần xen giữa sau;» (aparante) with line 4 «Có mười bốn, …»; less smooth, but line-aligned.
