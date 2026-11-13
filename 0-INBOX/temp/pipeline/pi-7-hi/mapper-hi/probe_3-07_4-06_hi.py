"""Helper for map_3-07_4-06_hi.py: test present(value, text) and print segments by id.
usage: python -I -B -X utf8 probe_3-07_4-06_hi.py present "<value>" "<text>"
       python -I -B -X utf8 probe_3-07_4-06_hi.py seg <file> <id> [<id> …]
"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import present, read_hindi, read_pali

if sys.argv[1] == "present":
    print(present(sys.argv[2], sys.argv[3]))
elif sys.argv[1] == "seg":
    hi, pa = read_hindi(sys.argv[2]), read_pali(sys.argv[2])
    for bid in sys.argv[3:]:
        print(bid, "PA:", pa.get(bid))
        print(bid, "HI:", hi.get(bid))
