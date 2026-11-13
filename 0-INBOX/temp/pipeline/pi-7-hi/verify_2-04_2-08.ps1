Set-Location D:\Work\OpenPecha\abhidhamma-rails
$files = '2-04-dassanenapahatabbahetukattika.md','2-05-acayagamittika.md','2-06-sekkhattika.md','2-07-parittattika.md','2-08-parittarammanattika.md'
foreach ($f in $files) {
  $p = "AI_translation\pali\pi-7_split_chapters\$f"
  $h = "AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters\$f"
  python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-7_split_chapters AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters $f
  python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py $p $h
  python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py $p $h
  $t = [IO.File]::ReadAllText((Resolve-Path $h))
  $dots = ([regex]::Matches($t, '[^\.\d]\.(\s|$)')).Count
  "extra: CR=$($t.Contains("`r")) dbl=$($t.Contains("`n`n`n")) latin-dots=$dots"
}
