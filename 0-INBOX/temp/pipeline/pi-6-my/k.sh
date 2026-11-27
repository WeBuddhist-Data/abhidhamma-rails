#!/bin/zsh
# scratch: k.sh REGEX [N] -> kwic6 with max N (default 3)
exec /opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8 "${0:A:h}/kwic6.py" "$1" --max "${2:-3}" "${@:3}"
