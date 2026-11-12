param([string]$rx, [int]$n = 2, [int]$clip = 700)
foreach ($b in 1, 3, 4, 5) {
  python -I -X utf8 D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\show_ch2_ch4_pi1.py $b $rx $n $clip
}
