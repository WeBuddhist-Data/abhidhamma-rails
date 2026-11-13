Set-Location D:\Work\OpenPecha\abhidhamma-rails
$p = "AI_translation\pali\pi-6_split_chapters"
$h = "AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters"
foreach ($f in "1-mulayamaka.md", "2-01-khandhayamaka.md", "2-02-khandhayamaka.md", "4-dhatuyamaka.md") {
    "== $f"
    python -I 0-INBOX\temp\pipeline\check_chapter_ids.py $p $h $f
    python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py "$p\$f" "$h\$f"
    python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py "$p\$f" "$h\$f"
    python -I -X utf8 0-INBOX\temp\pipeline\pi-6-hi\latin_check_1-2-4.py "$h\$f"
}
