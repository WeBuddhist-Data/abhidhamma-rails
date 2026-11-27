#!/bin/zsh
# rebuild every chapter in dependency order (no checks); helper of the consistency pass. usage: zsh rebuild_only.sh [from-generator]
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
D=0-INBOX/temp/pipeline/pi-7-my
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
GENS=(make_sample make_ch1-01 make_ch1-03-05 make_ch2-01-02 make_ch2-03-06 make_ch2-07-11 make_ch2-12-17
      make_ch3-01-02 make_ch3-03-06 make_ch3-07-08-10 make_ch3-09 make_ch4-01 make_ch4-02-09 make_ch4-10-14
      make_ch4-15-21 make_ch5-01-04 make_ch5-05-12 make_ch5-13-20)
go=0; [[ -z "$1" ]] && go=1
for g in $GENS; do
  [[ "$g" == "$1" ]] && go=1
  [[ $go == 1 ]] || continue
  t0=$SECONDS
  out=$(py $D/$g.py 2>&1); rc=$?
  if [[ $rc != 0 ]] || print -r -- "$out" | grep -q "Miss\|STOP\|Traceback"; then
    echo "FAILED: $g"; print -r -- "$out" | tail -15
  else
    echo "  $g: $(print -r -- "$out" | grep -c '^wrote') files ($((SECONDS - t0)) s)"
  fi
done
py $D/harmonise_diff.py | cut -c1-3000
