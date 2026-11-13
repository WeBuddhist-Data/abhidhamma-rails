Set-Location D:\Work\OpenPecha\abhidhamma-rails
$P = 'AI_translation\pali\pi-6_split_chapters'
$H = 'AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters'
foreach ($i in 6..11) {
  $f = '7-{0:d2}-anusayayamaka.md' -f $i
  python -I 0-INBOX\temp\pipeline\check_chapter_ids.py $P $H $f
  python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py "$P\$f" "$H\$f"
  python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py "$P\$f" "$H\$f"
  python -I -X utf8 0-INBOX\temp\pipeline\pi-6-hi\lint_7b.py "$H\$f"
}
