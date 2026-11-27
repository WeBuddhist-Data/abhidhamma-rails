#!/bin/zsh
# work loop: build + rules + adherence diff against the zero-shot misses + align quick check
cd /Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails || exit 1
py() { /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "$@"; }
R=0-INBOX/temp/pipeline/pi-5-my/rails; T=AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters
S=AI_translation/pali/pi-5_split_chapters
py $R/build_rails.py || exit 1
py $R/apply_termbase.py || exit 1
py $R/adherence_my.py AI_translation/pali/pi-5-keywords-by-reference-pali-plain.md AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md $T $R/adherence-rails.txt
py $R/work/missdiff.py
py 0-INBOX/temp/pipeline/pi-1-my/align_check_my.py $S $T --all > $R/align-rails.txt; head -1 $R/align-rails.txt
py 0-INBOX/temp/pipeline/pi-1-my/align_hidden_my.py $S $T > $R/align-hidden-rails.txt; tail -1 $R/align-hidden-rails.txt
py $R/align_explained.py | head -5
py $R/pi1234_identity.py $T -q
