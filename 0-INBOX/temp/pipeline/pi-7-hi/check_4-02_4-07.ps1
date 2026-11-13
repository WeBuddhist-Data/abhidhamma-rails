Set-Location D:\Work\OpenPecha\abhidhamma-rails
$files = '4-02-dukatika-hetuduka.md','4-03-dukatika-sahetukaduka.md','4-04-dukatika-sappaccayaduka.md','4-05-dukatika-asavaduka.md','4-06-dukatika-sannojanaduka.md','4-07-dukatika-ganthaduka.md'
foreach ($f in $files) {
  $p = "AI_translation\pali\pi-7_split_chapters\$f"
  $h = "AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters\$f"
  python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-7_split_chapters AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters $f
  python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py $p $h
  python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py $p $h
}
python -I -B -X utf8 0-INBOX\temp\pipeline\pi-7-hi\latin_4-02_4-07.py
