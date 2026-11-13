# Run the brief's checks on my files. usage: powershell -File checks_4-16_5-04.ps1
Set-Location D:\Work\OpenPecha\abhidhamma-rails
$files = "4-16-tikaduka-sappaccayaduka.md","4-17-tikaduka-asavaduka.md","4-18-tikaduka-sarammanaduka.md","4-19-tikaduka-kilesaduka.md","4-20-tikaduka-dassanenapahatabbaduka.md","4-21-tikaduka-sauttaraduka.md","5-01-anuloma-tikatika.md","5-02-anuloma-dukaduka.md","5-03-paccaniya-tika.md","5-04-paccaniya-duka.md"
$P = "AI_translation\pali\pi-7_split_chapters"
$H = "AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters"
foreach ($f in $files) {
    Write-Output "===== $f"
    python -I 0-INBOX\temp\pipeline\check_chapter_ids.py $P $H $f
    python -I -X utf8 0-INBOX\temp\pipeline\pi-1-en\dashcheck.py "$P\$f" "$H\$f"
    python -I -X utf8 0-INBOX\temp\pipeline\pi-1-hi\verify_hi.py "$P\$f" "$H\$f"
    $raw = [System.IO.File]::ReadAllText((Resolve-Path "$H\$f"))
    $cr = ($raw.ToCharArray() | Where-Object { $_ -eq "`r" }).Count
    $dbl = ([regex]::Matches($raw, "\n\s*\n\s*\n")).Count
    $noBr = [regex]::Replace($raw, "\[[^\]]*\]", "")
    $noBr = [regex]::Replace($noBr, "\^[0-9A-Za-z-]+", "")
    $lat = ([regex]::Matches($noBr, "[A-Za-zāīūṃṅñṭḍṇḷ]{2,}")).Count
    Write-Output "CR=$cr doubleBlank=$dbl latinWords=$lat"
}
