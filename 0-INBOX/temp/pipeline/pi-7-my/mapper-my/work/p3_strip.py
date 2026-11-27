"""phase 3 helper: remove from the group scripts the table entries the module (BOOK, the families) now holds.
usage: p3_strip.py FILE KEY [KEY …]   (single-line entries; a multi-line tuple entry with its continuation lines)"""
import sys, re, pathlib
f = pathlib.Path(sys.argv[1]); keys = set(sys.argv[2:])
L = f.read_text(encoding="utf-8").split("\n")
out, i, removed = [], 0, []
while i < len(L):
    l = L[i]
    ks = re.findall(r'^\s*"([^"]+)"\s*:|,\s*"([^"]+)"\s*:', l)
    ks = [a or b for a, b in ks]
    hit = [k for k in ks if k in keys]
    if hit and not l.lstrip().startswith("#"):
        if all(k in keys for k in ks):
            depth = l.split("#")[0].count("(") - l.split("#")[0].count(")")
            removed.append(l.strip()[:60]); i += 1
            while depth > 0 and i < len(L):
                depth += L[i].split("#")[0].count("(") - L[i].split("#")[0].count(")")
                removed.append("   +" + L[i].strip()[:60]); i += 1
            continue
        for k in hit:
            l2 = re.sub(r'"' + re.escape(k) + r'"\s*:\s*(?:"[^"]*"|\([^)]*\)|@?[A-Za-z_.]+)\s*,\s*', "", l)
            removed.append("part " + k); l = l2
    out.append(l); i += 1
f.write_text("\n".join(out), encoding="utf-8")
print(f.name, "removed", len(removed)); [print("   ", r) for r in removed]
