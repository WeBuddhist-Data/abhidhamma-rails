"""pi-1 Burmese RAILS build: runs the zero-shot generators' own logic (pi-1-my/make_*.py + my_formulas.py, read
only) with the rails layer (my_formulas_rails.py) and writes the chapters to the rails folder.

usage: python3 -I -X utf8 build_rails.py [--plain OUTDIR]
  * each generator runs in this process with a fresh my_formulas module, as each zero-shot generator runs in its own
    process; my_formulas.py and the generator are read as text, the layer's source patches are applied in memory
    (each patch must match exactly its stated number of times, else the run fails and nothing is written), and the
    code is executed with OUT pointing at the rails folder. The generators' term / notes writers are never called.
  * --plain OUTDIR: no patches (reproduction test: OUTDIR must then equal the zero-shot byte for byte).
The zero-shot files, the generators and my_formulas.py are only read.
"""
import pathlib
import sys
import types

HERE = pathlib.Path(__file__).resolve().parent          # pi-1-my/rails
GEN = HERE.parent                                       # pi-1-my
ROOT = HERE.parents[4]
RAILS_OUT = ROOT / "AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters"
sys.path.insert(0, str(HERE))
import my_formulas_rails as L  # noqa: E402

# generator -> what its «__main__» block writes (the chapter writers only; never write_terms / write_notes)
RUNS = [
    ("make_sample", lambda ns: (ns["preamble"](), ns["chapter"]("1-matika.md"))),
    ("make_ch2-01", lambda ns: [ns["chapter"](n) for n in ns["NAMES_OUT"]]),
    ("make_ch2-02-03", lambda ns: (ns["extend"](), [ns["chapter"](ns["CHAPTERS"][c]) for c in ns["CHAPTERS"]])),
    ("make_ch2-04-05", lambda ns: [ns["chapter"](k) for k in ("2-04", "2-05")]),
    ("make_ch3", lambda ns: [ns["chapter"](ns["CHAPTERS"][a]) for a in ns["CHAPTERS"]]),
    ("make_ch4", lambda ns: (ns["build"](), [ns["chapter"](k) for k in ns["CHAPTERS"]])),
    ("make_ch5", lambda ns: ns["write_ch5"]()),
]


class PatchError(Exception):
    pass


def patched(src, patches, where):
    """Apply (old, new, count, reason) patches to a source text; each must occur exactly count times."""
    log = []
    for old, new, count, reason in patches:
        n = src.count(old)
        if n != count:
            raise PatchError(f"{where}: «{old[:70]}» occurs {n}×, expected {count} ({reason})")
        src = src.replace(old, new)
        log.append((where, count, old, new, reason))
    return src, log


def fresh_formulas(plain):
    p = GEN / "my_formulas.py"
    src = p.read_text(encoding="utf-8")
    log = []
    if not plain:
        src, log = patched(src, L.FORMULA_PATCHES, "my_formulas.py")
    mod = types.ModuleType("my_formulas")
    mod.__file__ = str(p)
    sys.modules["my_formulas"] = mod
    exec(compile(src, str(p), "exec"), mod.__dict__)
    if not plain:
        L.after_import(mod)
    return mod, log


def run(out, plain=False):
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.md"):
        old.unlink()
    log = []
    for name, main in RUNS:
        F, flog = fresh_formulas(plain)
        log += flog if name == RUNS[0][0] else []
        p = GEN / f"{name}.py"
        src = p.read_text(encoding="utf-8")
        if not plain:
            src, glog = patched(src, L.GEN_PATCHES.get(name, []), f"{name}.py")
            log += glog
        src = src.split('\nif __name__ == "__main__":')[0]
        if name == "make_ch5":   # its «__main__» block writes the chapter inline: the same two lines as a function
            src += ("\n\ndef write_ch5():\n"
                    "    txt = unicodedata.normalize('NFC', translate((PALI / NAME).read_text(encoding='utf-8-sig')))\n"
                    "    (OUT / NAME).write_text(txt, encoding='utf-8')\n"
                    "    print(f'wrote {NAME}: {sum(1 for l in txt.splitlines() if l)} lines')\n")
        ns = {"__name__": "rails_" + name.replace("-", "_"), "__file__": str(p)}
        exec(compile(src, str(p), "exec"), ns)
        ns["OUT"] = out
        main(ns)
        sys.modules.pop("my_formulas", None)
    return log


if __name__ == "__main__":
    if "--plain" in sys.argv:
        run(pathlib.Path(sys.argv[sys.argv.index("--plain") + 1]).resolve(), plain=True)
    else:
        try:
            log = run(RAILS_OUT)
        except PatchError as e:
            print("FAIL", e)
            sys.exit(1)
        with open(HERE / "layer-log.tsv", "w", encoding="utf-8") as f:
            f.write("file\tcount\told\tnew\treason\n")
            esc = lambda x: x.replace("\\", "\\\\").replace("\n", "\\n").replace("\t", "\\t")
            for w, c, o, n, r in log:
                f.write(f"{w}\t{c}\t{esc(o)}\t{esc(n)}\t{r}\n")
        print(f"layer: {len(log)} source patches")
