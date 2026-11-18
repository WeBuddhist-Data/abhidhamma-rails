# Runs the verification set for the review fixes (pi-1 Vietnamese rails). Output: review_fixes_verify.log
$root = "D:\Work\OpenPecha\abhidhamma-rails"
Set-Location $root
$p = "AI_translation\pali\pi-1_split_chapters"
$v = "AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters"
$parts = @("preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
  "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
  "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam")
$pairs = @()
foreach ($c in $parts) {
  "== $c"
  python -I -X utf8 0-INBOX\temp\pipeline\check_chapter_ids.py $p $v "$c.md"
  python -I -X utf8 0-INBOX\temp\pipeline\dashcheck.py "$p\$c.md" "$v\$c.md"
  $pairs += "$p\$c.md"; $pairs += "$v\$c.md"
}
"== verify_rails_vi"
python -I -X utf8 0-INBOX\temp\pipeline\pi-1-vi-ai\verify_rails_vi.py @pairs
"== termbase adherence"
python -I -X utf8 0-INBOX\temp\pipeline\termbase_adherence_vi.py AI_translation\pali\pi-1-keywords-by-reference-pali-plain.md AI_translation\vietnamese\pi-1-pali-vietnamese-termbase-plain.md $v 0-INBOX\temp\pipeline\pi-1-vi-ai\rails\review_fixes_adherence_post.md
