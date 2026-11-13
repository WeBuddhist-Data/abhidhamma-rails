# pi-7 Hindi zero-shot: parallel run (started 2026-11-13, after sample approval)

Sample agent (done): a86b6b892435311bd (preamble, 1-00-paccaya, sample s2-s4, build_sample_hi.py, hi-zeroshot-terms.md). User decisions: title «कारण-संबंध»; Siyā lines as questions.

agent id | files
---|---
a121dcd4724898162 | 1-01
a48f089dc8abe1dc2 | 1-02..1-05
ab9279be01251b39e | 2-01..2-03
ad7318f32f008300c | 2-04..2-08
ad56aa376bb124bda | 2-09..2-17
a0ae691366019e7bb | 3-01, 3-02, 3-10
a277e493a90c2ef20 | 3-03..3-08
a52cd7e86dadc8bba | 3-09
a747dbb8b4ded7097 | 4-01
ab56f3ab0cf15c432 | 4-02..4-07
aafbd9d2658714f39 | 4-08..4-15
a1a4d6bd99cd59870 | 4-16..4-21, 5-01..5-04
a7048e64d85dbf878 | 5-05..5-12
ae34cb1d25c654605 | 5-13..5-20

All 14 finished 2026-11-13 (paused twice by the user). My re-check: all 76 files OK (IDs, dashes, format; 38 verify flags, all {…} brackets or Siyā "?").
Harmonise agent: a8acb32d0d6998a8d (harmonise-brief.md). Done: 2331 lines in 71 files. Merged zero-shot: pi-7-hindi-plain-zeroshot.md (16,249 blocks).

## Keyword map (hi-mapper-brief.md); sample a9e76963a6c563b13 approved 2026-11-13
agent id | parts
---|---
a61fb53b0cab7ccad | 1-01, 1-02
a6cd446998ed4f6b7 | 1-03, 1-04, 1-05, 2-01
a93126fb62aef432d | 2-02..2-08
a39e033140c2b2e79 | 2-09..2-17 (not 2-13), 3-01
a0163fac8f5a4f1ef | 3-02..3-06
ab58d23565f009339 | 3-09
a78670019107cf78e | 3-07, 3-08, 3-10, 4-03..4-06
a56b7f137a9518cf1 | 4-01
a14156e98400822ba | 4-02, 4-08..4-14
ab98f202689a916c0 | 4-15..4-21, 5-01..5-04
a30fa53bffb4bbf1e | 5-05..5-20

All 11 done. Merged: AI_translation\hindi\pi-7-keywords-by-reference-pali-hindi-plain.md (15,312 lines, 179,791 pairs, 16 NDE; 131 keywords vary).

## Word senses (hi-senses-brief.md)
Input: senses_prepare_pi7.py 4 → 2,315 headwords (132 multi-value), agg-part1..4.tsv; agg-sample.tsv = first 90 of part1 + 30 more multi-value (35 multi).
Sample agent: a13875fbcf406a6b5 (approved 2026-11-13: 120 headwords, 142 senses)
Parts: a6518bfbb8d7a9e96 (1), a14a48edf02366189 (2), ada500474f3c4a155 (3), a5128c6705aa47967 (4). All verify OK.
Merged: AI_translation\hindi\pi-7-pali-word-hindi-senses-plain.md (2,315 headwords, 2,347 senses, 30 multi-sense, 113 multi-candidate; full verify OK).
Senses notes for the termbase: saṅkhāre merged (drift); suddhake «अकेला कारण / शुद्ध पद» merged; dyad/triad ordinals in tags from the standard matrix order (spot-checked 2nd-13th OK).

## Termbase (hi-termbase-brief.md; tb_tool_pi7.py)
Builder: ac8792048207ba22e. Approved 2026-11-13 (termbase\APPROVED.md; vipāka «कर्म-फल रूपी» everywhere).

## Rails translation (hi-rails-brief.md)
Sample agent: a2822a0d9e9846025 (preamble, 1-00-paccaya, 1-01 lines 1-190 and 1235-1262). Approved 2026-11-13.
Parallel (rails\agent-prompt.md):
agent id | files
---|---
a26d98b114ee76c5b | 1-01
a9e5028daab519832 | 1-02..1-05
a42a57ff0df99f7a3 | 2-01..2-03
a5f5bf7158ac6b64f | 2-04..2-08
a71f811afae9a0c88 | 2-09..2-17
a8ef63bbd3c56d5af | 3-01, 3-02, 3-10
afb27ca564630e5d9 | 3-03..3-08
aecfc44e7cba0d246 | 3-09
a7dd3c3acdf92d7df | 4-01
a13286ce25f77aea2 | 4-02..4-07
acfccea0320274a39 | 4-08..4-15
a96ef9fdfc8621a8b | 4-16..5-04
a84e9fcc96781e271 | 5-05..5-12
acd9b915659392591 | 5-13..5-20

All 14 finished 2026-11-13 (paused once). My re-check: 75 files OK; 38 expected verify flags; adherence 2440/179791 (1.4%), inflection.
Alignment agent: a18efc591dcc9bb7d (rails\align-brief.md). Done: 3,053 lines in 70 files.
User decision 2026-11-14: kātabba verb fits the object (rails\katabba_user_pi7.py; termbase reassembled).

## Review (review-brief.md; findings saved by me to review\findings-rN.md)
All 10 reviews in; findings-r1..r10.md with my decisions. User decisions 2026-11-14: U1 names «… वाली परिघटनाओं वाला» (Hetuduka «मूल रूपी परिघटनाओं वाला»); U2 vicikicchā/uddhacca «या» throughout incl. sample; U3 sahajāto «के साथ उत्पन्न होकर»; U4 inner negatives unchanged.
Fix agent: a14a44b6b640147d7 (review\fix-brief.md). After it: update termbase for U1 names (review\names-change.tsv) and U3.
r1 a6ad8ef45d0a4103e (preamble, 1-00, 1-01) | r2 a8c4a0d8736d9c305 (1-02..1-05) | r3 a88d4acf01bb4f57f (2-01..2-08) | r4 a130a7010f6c17e37 (2-09..2-17) | r5 a397409f6817e4901 (3-01, 3-02, 3-10) | r6 a8112e34d4eea4455 (3-03..3-08) | r7 a40dab29c989f3ff6 (3-09) | r8 a6a35b8e282f3fb95 (4-01) | r9 a47806457ee512e1c (4-02..4-15) | r10 a10b7a6288c7c7986 (4-16..5-20)
