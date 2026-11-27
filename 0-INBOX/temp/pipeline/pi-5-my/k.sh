#!/bin/zsh
# scratch: k.sh REGEX [N] -> kwic5 with max N (default 2), Burmese cut
exec /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "${0:A:h}/kwic5.py" "$1" --max "${2:-2}"
