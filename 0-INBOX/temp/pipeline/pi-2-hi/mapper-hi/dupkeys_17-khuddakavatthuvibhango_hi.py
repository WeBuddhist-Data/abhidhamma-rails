"""List keys of T assigned more than once with different values in map_17-khuddakavatthuvibhango_hi.py."""
import ast
import collections
import pathlib

src = (pathlib.Path(__file__).resolve().parent / "map_17-khuddakavatthuvibhango_hi.py").read_text(encoding="utf-8")
seen = collections.defaultdict(list)
for node in ast.walk(ast.parse(src)):
    if isinstance(node, ast.Call) and getattr(node.func, "attr", "") == "update" \
            and getattr(node.func.value, "id", "") == "T":
        d = node.args[0]
        for k, v in zip(d.keys, d.values):
            seen[ast.literal_eval(k)].append((node.lineno, ast.unparse(v)))
    if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Subscript) \
            and getattr(node.targets[0].value, "id", "") == "T":
        seen[ast.literal_eval(node.targets[0].slice)].append((node.lineno, ast.unparse(node.value)))
for k, vs in seen.items():
    if len(set(v for _, v in vs)) > 1:
        print(k, vs)
