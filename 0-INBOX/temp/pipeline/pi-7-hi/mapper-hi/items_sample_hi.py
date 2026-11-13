"""Helper for the pi-7 sample: harvest the item wording of the Paṭicca frames.
For every sentence «X dhammaṃ paṭicca Y dhammo uppajjati …» whose X is one word (no ca / ñca), pair the
Pāli X (accusative stem) with the Hindi before «परिघटना पर निर्भर होकर». Prints Pāli | Hindi | count.
usage: python -I -B -X utf8 items_sample_hi.py <file-glob>
"""
import collections
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PI = ROOT / "AI_translation" / "pali" / "pi-7_split_chapters"
HI = ROOT / "AI_translation" / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters"


def segs(path):
    out = {}
    for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8")):
        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", block.strip())
        if m:
            out[m.group(1)] = block.strip()[: m.start()].strip()
    return out


def main():
    pairs = collections.Counter()
    for p in sorted(PI.glob(sys.argv[1] + ".md")):
        a, b = segs(p), segs(HI / p.name)
        for bid, t in a.items():
            if bid not in b:
                continue
            ps = re.findall(r"(?:^|[.–;] |\n)(?:Siyā )?([A-ZĀa-zāīūṃṇñṭḍḷṅ ]+?) dhammaṃ paṭicca ", t)
            hs = re.findall(r"(?:^|[।–;?] |\n)(?:क्या )?([^।–;?\n]+?) परिघटना पर निर्भर होकर", b[bid])
            for x, y in zip(ps, hs):
                if "ñca" in x or " ca " in x or len(x.split()) > 3:
                    continue
                pairs[(x.strip(), y.strip())] += 1
    for (x, y), c in sorted(pairs.items()):
        print(f"{c:5} {x} | {y}")


if __name__ == "__main__":
    main()
