"""pi-4 Burmese RAILS build: runs the zero-shot generators' own logic (pi-4-my/make_*.py + my4_formulas.py, read
only) with the rails layer (my_formulas_rails.py) and writes the chapters to the rails folder. Model: the approved
pi-3 / pi-2 rails builds (pi-3-my/rails/build_rails.py, pi-2-my/rails/build_rails.py, read only).

usage: python3 -I -X utf8 build_rails.py [--plain OUTDIR]
  * each generator runs in this process with a fresh my4_formulas module and (for make_ch3-4, make_ch5, make_ch6-11,
    which «import make_sample as M») a fresh make_sample module, exactly as each zero-shot generator runs in its own
    process (my4_formulas keeps module state: SENT, NAME, EXTRA_RULES, unit_my …, and make_sample installs its tables
    into it at import). my4_formulas.py, make_sample.py and the generator are read as text, the layer's source
    patches are applied in memory (each patch must match exactly its stated number of times, else the run fails and
    nothing is kept; the make_sample patches apply both where it runs and where it is imported), and the code is
    executed with OUT pointing at the rails folder (a source-level change of the OUT line) and the generators'
    «partial-» dump on a stop pointing at rails/scratch. Only the chapter writers are called: make_sample's
    terms_my4.write_terms() is never called (my4-zeroshot-terms.md is not touched).
  * order: as regen_zeroshot.sh (make_sample, make_ch3-4, make_ch5, make_ch6-11). No generator reads another
    chapter from OUT (my4_formulas reads only the Pāli and the FINAL pi-1 / pi-2 / pi-3 rails texts).
  * --plain OUTDIR: no patches (reproduction test: OUTDIR must then equal the zero-shot byte for byte).
The zero-shot files, the generators and my4_formulas.py are only read.
"""
import pathlib
import sys
import types

HERE = pathlib.Path(__file__).resolve().parent          # pi-4-my/rails
GEN = HERE.parent                                       # pi-4-my
ROOT = HERE.parents[4]
RAILS_OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters"
ZS_LINE = 'OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"'
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import my_formulas_rails as L  # noqa: E402


class PatchError(Exception):
    pass


def _chapters(ns):
    for n in ns["NAMES_OUT"]:
        if not ns["chapter"](n):
            raise PatchError(f"{n}: the generator stopped (a line no rule matches)")


def _ch5(ns):
    """make_ch5's «__main__»: generate(), the SENT5 coverage check, write NAME_OUT."""
    txt = ns["generate"]()
    if txt is None:
        raise PatchError("make_ch5: the generator stopped (a line no rule matches)")
    unused = set(ns["SENT5"]) - ns["USED"]
    if unused:
        raise PatchError(f"make_ch5: {len(unused)} SENT5 keys unused: {sorted(unused)[0][:80]}")
    (ns["OUT"] / ns["NAME_OUT"]).write_text(txt, encoding="utf-8")


# generator -> what its «__main__» block writes (the chapter writers only; never write_terms)
RUNS = [
    ("make_sample", _chapters),
    ("make_ch3-4", _chapters),
    ("make_ch5", _ch5),
    ("make_ch6-11", _chapters),
]


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
    p = GEN / "my4_formulas.py"
    src = p.read_text(encoding="utf-8")
    log = []
    if not plain:
        src, log = patched(src, L.FORMULA_PATCHES, "my4_formulas.py")
    mod = types.ModuleType("my4_formulas")
    mod.__file__ = str(p)
    sys.modules["my4_formulas"] = mod
    exec(compile(src, str(p), "exec"), mod.__dict__)
    if not plain and hasattr(L, "after_import"):
        L.after_import(mod)
    return mod, log


def gen_source(name, out, plain):
    p = GEN / f"{name}.py"
    src = p.read_text(encoding="utf-8")
    if src.count(ZS_LINE) != 1:
        raise PatchError(f"{name}.py: OUT line not found once")
    src = src.replace(ZS_LINE, f"OUT = pathlib.Path({str(out)!r})")
    src = src.replace('HERE / "scratch"', f"pathlib.Path({str(HERE / 'scratch')!r})")
    log = []
    if not plain:
        src, log = patched(src, L.GEN_PATCHES.get(name, []), f"{name}.py")
    parts = src.split('\nif __name__ == "__main__":\n')
    if len(parts) != 2:
        raise PatchError(f"{name}.py: main block not found once")
    return p, parts[0], log


def run(out, plain=False):
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.md"):
        old.unlink()
    log = []
    for name, main in RUNS:
        F, flog = fresh_formulas(plain)
        log += flog if name == RUNS[0][0] else []
        try:
            if name != "make_sample":       # «import make_sample as M»: a fresh, patched make_sample module
                p, src, _ = gen_source("make_sample", out, plain)
                mod = types.ModuleType("make_sample")
                mod.__file__ = str(p)
                sys.modules["make_sample"] = mod
                exec(compile(src, str(p), "exec"), mod.__dict__)
            p, src, glog = gen_source(name, out, plain)
            log += glog
            ns = {"__name__": "rails_" + name.replace("-", "_"), "__file__": str(p)}
            exec(compile(src, str(p), "exec"), ns)
            main(ns)
        except SystemExit as e:
            raise PatchError(f"{name}: generator exit {e.code}")
        except Exception as e:                       # noqa: BLE001  (a Miss at import, a table conflict …)
            raise PatchError(f"{name}: {type(e).__name__}: {e}")
        sys.modules.pop("my4_formulas", None)
        sys.modules.pop("make_sample", None)
    return log


if __name__ == "__main__":
    if "--plain" in sys.argv:
        try:
            run(pathlib.Path(sys.argv[sys.argv.index("--plain") + 1]).resolve(), plain=True)
        except PatchError as e:
            print("FAIL", e)
            sys.exit(1)
    else:
        try:
            log = run(RAILS_OUT)
        except PatchError as e:
            print("FAIL", e)
            sys.exit(1)
        with open(HERE / "layer-log.tsv", "w", encoding="utf-8") as f:
            f.write("file\tcount\told\tnew\treason\n")
            esc = lambda x: x.replace("\\", "\\\\").replace("\n", "\\n").replace("\t", "\\t")  # noqa: E731
            for w, c, o, n, r in log:
                f.write(f"{w}\t{c}\t{esc(o)}\t{esc(n)}\t{r}\n")
        print(f"layer: {len(log)} source patches")
