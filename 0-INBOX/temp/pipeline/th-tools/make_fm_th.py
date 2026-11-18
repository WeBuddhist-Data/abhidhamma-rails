"""Write the frontmatter for a Thai Royal-edition book: one for the block-aligned file and one
for the raw (plain) copy.

Usage: make_fm_th.py <book> <thai_title> <pali_title> <vol_th_label> <pdf_name> <para_range> <out_aligned> <out_raw> [<raw_rel_path>]
"""
import sys

book, th_title, pi_title, vol_label, pdf, para_range, out_al, out_raw = sys.argv[1:9]
raw_rel = sys.argv[9] if len(sys.argv) > 9 and sys.argv[9] else f"0-INBOX/raw-data/th-{book}-thai_tipitaka-raw.md"
EXTRA = (sys.argv[10] + "; ") if len(sys.argv) > 10 and sys.argv[10] else ""

COMMON = f'''title: "{th_title}"
language: Thai
script: Thai
file_type: translation
lang_tag: th
pitaka: abhidhamma
root_text: 1-SOURCES/Text/pi-{book}.md
translator: "Royal edition (พระไตรปิฎกภาษาไทย ฉบับหลวง), Dept of Religious Affairs, {vol_label}"
translation_basis: "พระไตรปิฎก ฉบับ ๔๕ เล่ม, {vol_label}"
coverage: complete
'''
COPY = 'copyright: "Public domain in Thailand (government work, first published 1957; 50-year term)"\n'
SRC = (f'source_description: "archive.org item Tri4501, file \'{pdf}\' (Word export, June 2009); downloaded 2026-11-13. '
       'Text layer extracted with pypdf. [Ed: legacy Thai font glyphs (U+F700 to U+F71A) mapped back to Unicode; '
       'nikhahit + sara aa normalised to sara am; stray spaces before dependent vowels and marks removed; page headers removed; '
       + EXTRA.replace("{", "{{").replace("}", "}}") +
       '{tables}paragraph numbers {para_range}. Some stray spaces between Thai consonants may remain.]"\n')

aligned = ("---\n" + COMMON
           + 'alignment: "block-aligned to 1-SOURCES/Text/pi-' + book + '.md: each text block carries the root block ID and is preceded by a transclusion of the root block; root blocks rendered together are stacked (merge); headings carry the root heading ID with no transclusion; root headings with no heading in this translation are left out"\n'
           + "status: draft\n" + COPY
           + SRC.format(pdf=pdf, para_range=para_range,
                        tables=f"in two-column Pāli/Thai passages only the Thai column is kept (the Pāli is transcluded from the root; the raw copy {raw_rel} keeps both columns); Thai-only sub-headings kept as bold lines; ")
           + "verse_id_format: book-verse\n---\n")
raw = ("---\n" + COMMON
       + 'alignment: "none: plain markdown, no block IDs (raw copy; the block-aligned version is 1-SOURCES/Translations/Thai/th-' + book + '-thai_tipitaka.md)"\n'
       + "status: draft\n" + COPY
       + SRC.format(pdf=pdf, para_range=para_range, tables="two-column Pāli/Thai passages rendered as tables; ")
       + "---\n")
open(out_al, "w", encoding="utf-8", newline="\n").write(aligned)
open(out_raw, "w", encoding="utf-8", newline="\n").write(raw)
print("ok")
