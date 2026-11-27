#!/bin/zsh
# scratch: mutation test of check_sample.py (each mutation must be caught); restores the output file
D=/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters
H=${0:A:h}
PY=/opt/homebrew/Caskroom/miniconda/base/bin/python3
cp $D/2-01-khandhayamaka.md $H/khandha.bak
cp $D/1-mulayamaka.md $H/mula.bak
run() { $PY -I -X utf8 $H/../check_sample.py > $H/mut.out 2>&1; echo "$1: exit $? $(grep -oE "^   (A|B[0-9]|C[0-9])" $H/mut.out | sort -u | tr -d " " | tr "\n" " ")"; cp $H/khandha.bak $D/2-01-khandhayamaka.md; cp $H/mula.bak $D/1-mulayamaka.md; }
$PY -I -X utf8 -c "import pathlib,sys;p=pathlib.Path(sys.argv[1]);s=p.read_text();p.write_text(s.replace('ထိုသူတို့အား ခံစားမှု အစုအဝေး မဖြစ်ပေါ်။','ထိုသူတို့အား ခံစားမှု အစုအဝေး ဖြစ်ပေါ်။',1))" $D/2-01-khandhayamaka.md; run "dropped မ (polarity)"
$PY -I -X utf8 -c "import pathlib,sys;p=pathlib.Path(sys.argv[1]);s=p.read_text();p.write_text(s.replace('ဖြစ်ပေါ်ခဲ့သလော','ဖြစ်ပေါ်သလော',1))" $D/2-01-khandhayamaka.md; run "dropped ခဲ့ (tense)"
$PY -I -X utf8 -c "import pathlib,sys;p=pathlib.Path(sys.argv[1]);s=p.read_text();p.write_text(s.replace('သုံးပါးသာ','လေးပါးသာ',1))" $D/1-mulayamaka.md; run "three -> four"
$PY -I -X utf8 -c "import pathlib,sys;p=pathlib.Path(sys.argv[1]);s=p.read_text();p.write_text(s.replace('ဟုတ်ပါသည်။','ဟုတ်သည်။',1))" $D/2-01-khandhayamaka.md; run "changed Āmantā"
$PY -I -X utf8 -c "import pathlib,sys;p=pathlib.Path(sys.argv[1]);s=p.read_text();p.write_text(s.replace('ရုပ် အစုအဝေး','ရုပ်အစုအဝေး',1))" $D/2-01-khandhayamaka.md; run "changed khandha name"
rm -f $H/khandha.bak $H/mula.bak $H/mut.out
