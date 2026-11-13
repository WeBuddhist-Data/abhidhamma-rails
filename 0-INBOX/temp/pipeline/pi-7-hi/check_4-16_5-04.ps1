$ErrorActionPreference = "Continue"
Set-Location D:\Work\OpenPecha\abhidhamma-rails
$files = '4-16-tikaduka-sappaccayaduka.md','4-17-tikaduka-asavaduka.md','4-18-tikaduka-sarammanaduka.md','4-19-tikaduka-kilesaduka.md','4-20-tikaduka-dassanenapahatabbaduka.md','4-21-tikaduka-sauttaraduka.md','5-01-anuloma-tikatika.md','5-02-anuloma-dukaduka.md','5-03-paccaniya-tika.md','5-04-paccaniya-duka.md'
foreach ($f in $files) {
    $p = "AI_translation\pali\pi-7_split_chapters\$f"
    $h = "AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters\$f"
    python -I 0-INBOX\temp\pipeline\check_chapter_ids.py AI_translation\pali\pi-7_split_chapters AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters $f
    python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py $p $h
    python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py $p $h
}
