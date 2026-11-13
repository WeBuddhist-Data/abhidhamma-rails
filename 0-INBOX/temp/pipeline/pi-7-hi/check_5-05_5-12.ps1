$root = "D:\Work\OpenPecha\abhidhamma-rails"
Set-Location $root
$files = "5-05-paccaniya-dukatika.md","5-06-paccaniya-tikaduka.md","5-07-paccaniya-tikatika.md","5-08-paccaniya-dukaduka.md","5-09-anulomapaccaniya-tika.md","5-10-anulomapaccaniya-duka.md","5-11-anulomapaccaniya-dukatika.md","5-12-anulomapaccaniya-tikaduka.md"
foreach ($f in $files) {
  $p = "AI_translation\pali\pi-7_split_chapters\$f"
  $h = "AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters\$f"
  "=== $f"
  python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-7_split_chapters AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters $f
  python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py $p $h
  python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py $p $h
}
