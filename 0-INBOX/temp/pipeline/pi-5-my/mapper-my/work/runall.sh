#!/bin/zsh
# phase 3: run the three mapping scripts in order (from mapper-my); print only problems and the per-chapter lines
cd "$(dirname "$0")/.."
P=/opt/homebrew/Caskroom/miniconda/base/bin/python3
for s in map_ch1.py map_ch2-15.py map_ch16-31.py; do $P -I -X utf8 $s; done
