"""For a headword, list each id with the Pāli compounds containing a stem (regex) in that segment.
usage: ctx_my.py headword stem_regex"""
import sys, re, pathlib, subprocess
sys.argv = sys.argv
hw, stem = sys.argv[1], sys.argv[2]
here = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(here))
import importlib.util
spec = importlib.util.spec_from_file_location('seg', here / 'seg_my.py')
src = (here / 'seg_my.py').read_text(encoding='utf-8')
ns = {'__file__': str(here / 'seg_my.py')}
exec(src.split("args = sys.argv[1:]")[0], ns)
P = ns['P']
M = here.parents[4] / 'AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md'
for l in M.read_text(encoding='utf-8').splitlines():
    m = re.match(r'\[([^\]]+)\] (.*)', l)
    if not m: continue
    for p in m.group(2).split(', '):
        k, _, v = p.partition('=')
        if k == hw:
            words = sorted(set(w for w in re.findall(r"[\w’']+", P.get(m.group(1), '')) if re.search(stem, w, re.I)))
            print(m.group(1), v, words)
