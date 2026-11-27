"""scratch: per chapter group, sentence units whose Pāli has no quote mark but whose Burmese has one."""
import sys, importlib.util, pathlib, collections
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
gen = sys.argv[1]
spec = importlib.util.spec_from_file_location(gen.replace("-", "_") + "_x", HERE / f"{gen}.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
F = sys.modules["my5_formulas"]
if hasattr(m, "install"): m.install()
QS = '"‘’“”'
hits = collections.Counter(); ex = {}
orig = F.line_my
def line_my(body):
    out = orig(body)
    return out
for name in m.NAMES_OUT:
    for ln, line in enumerate((m.PALI / name).read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip(): continue
        mm = F.ID_RE.search(line); body = (line[:mm.start()] if mm else line).strip()
        if F.HEAD_RE.fullmatch(body): continue
        clean = F.BR_RE.sub("", body); key = F.norm_pe(F.strip_q(clean))
        if key in F.LINES or key.rstrip(".") in F.COLO: continue
        if any(rx.fullmatch(key) for rx, fn in F.LINE_FRAMES): continue
        for a, b in F.split_sents(clean):
            u = clean[a:b].strip()
            if any(c in u for c in QS): continue
            try: my = F.unit_my(F.strip_q(u))
            except Exception: continue
            if any(c in my for c in "“”‘’"):
                hits[name] += 1; ex.setdefault(name, []).append(f"{ln}: {u[:120]} || {my[:160]}")
for k, v in hits.items():
    print(k, v); print("   " + "\n   ".join(ex[k][:4]))
