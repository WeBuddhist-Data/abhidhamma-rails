"""Extract (Pāli, English) string pairs from every builder (dict literals and 2-tuples of strings) and list
Pāli keys with more than one English value across builders."""
import ast, glob, os, re, collections, sys
D = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-en"
FILES = sorted(glob.glob(os.path.join(D, "build_*.py")) + glob.glob(os.path.join(D, "const_*.py")))
PALI = re.compile(r"[āīūṃṅñṭḍṇḷ]")


def s(n):
    return n.value if isinstance(n, ast.Constant) and isinstance(n.value, str) else None


pairs = collections.defaultdict(lambda: collections.defaultdict(set))
for f in FILES:
    name = os.path.basename(f)
    try:
        tree = ast.parse(open(f, encoding="utf-8").read())
    except Exception as ex:
        print("parse fail", name, ex); continue
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                a, b = (s(k) if k else None), s(v)
                if a and b:
                    pairs[a.strip()][b.strip()].add(name)
        elif isinstance(node, ast.Tuple) and len(node.elts) == 2:
            a, b = s(node.elts[0]), s(node.elts[1])
            if a and b and PALI.search(a) and not PALI.search(b.replace("Nibbāna", "").replace("Māra", "").replace("Tathāgata", "").replace("Avīci", "").replace("Akaniṭṭha", "")):
                pairs[a.strip()][b.strip()].add(name)

out = []
for k in sorted(pairs, key=str.lower):
    v = pairs[k]
    if len(v) > 1:
        out.append(f"### {k}")
        for e, fs in v.items():
            out.append(f"   {sorted(x.replace('.py','') for x in fs)} :: {e}")
open(os.path.join(D, "hz_builders_out.txt"), "w", encoding="utf-8").write("\n".join(out))
print("keys", len(pairs), "multi", sum(1 for l in out if l.startswith("###")))
