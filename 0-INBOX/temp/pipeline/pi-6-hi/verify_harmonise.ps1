# Run the three structural checks on every pi-6 Hindi file after the harmonise pass.
Set-Location D:\Work\OpenPecha\abhidhamma-rails
$P = "AI_translation\pali\pi-6_split_chapters"
$H = "AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters"
$bad = 0
foreach ($f in Get-ChildItem $H -Filter *.md) {
    $n = $f.Name
    $a = python -I 0-INBOX\temp\pipeline\check_chapter_ids.py $P $H $n | Out-String
    $b = python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py "$P\$n" "$H\$n" | Out-String
    $c = python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py "$P\$n" "$H\$n" | Out-String
    $line = "{0,-26} ids: {1} | verify: {2} | dash: {3}" -f $n, $a.Trim().Split("`n")[-1].Trim(), $b.Trim().Split("`n")[-1].Trim(), $c.Trim().Split("`n")[-1].Trim()
    $line
}
