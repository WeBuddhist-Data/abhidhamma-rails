"""List keywords that contain an absolutive-looking Pāli word (-tvā/-tvāna/-ya/-cca/-bbha/-jja/-mma...) with their values."""
import re, pathlib, collections, sys
HERE = pathlib.Path(__file__).resolve().parent
ABS = re.compile(r"(tvā|tvāna|ṭhapetvā|paṭicca|ārabbha|upādāya|nissāya|upasampajja|abhibhuyya|samatikkamma|atikkamma|pahāya|vineyya|abhiññāya|ādāya|āgamma|sandhāya|paṭisaṅkhāya|pariññāya|nikkhamma|uddissa|vivicca)$")
res = collections.defaultdict(collections.Counter)
for f in sorted(HERE.glob("*.mapped.md")):
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if any(ABS.search(w) for w in k.split()):
                res[(k, v)][f.name[:4]] += 1
for (k, v), c in sorted(res.items()):
    print(f"{k}\t{v}\t{dict(c)}")
