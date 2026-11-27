"""pi-6 Burmese RAILS build: runs the zero-shot generators' own logic (pi-6-my/make_*.py + my6_formulas.py, read
only) with the rails layer (my_formulas_rails.py) and writes the chapters to the rails folder. Model: the approved
pi-5 rails build (pi-5-my/rails/build_rails.py, read only), adapted to pi-6's import chain.

usage: python3 -I -X utf8 build_rails.py [--plain OUTDIR]
  * regen_zeroshot.sh runs each of the 9 generators in its own process. Here each runs in this process with FRESH
    modules: my6_formulas and make_ch7a are served by a meta-path finder (the generators' «import my6_formulas as F»
    and make_ch7b's «import make_ch7a as A» get a new, patched module per generator run), so a patch of
    my6_formulas / make_ch7a applies wherever that file runs or is imported, exactly as a change of the file on disk
    would, and the in-memory table extensions of one generator never leak into the next.
  * each source text is read, the layer's patches are applied in memory (each must match exactly its stated number
    of times, else the run fails and nothing is kept), the OUT line of each generator (make_ch7b uses A.OUT) is
    pointed at the output folder, and the generator's own «__main__» block runs with no arguments (its NAMES_OUT;
    a bad line stops it with sys.exit = a failed build). make_sample --terms is never run (my6-zeroshot-terms.md is
    not touched).
  * --plain OUTDIR: no patches (reproduction test: OUTDIR must then equal the zero-shot byte for byte).
The zero-shot files, the generators and my6_formulas.py are only read.
"""
import contextlib
import importlib.abc
import importlib.util
import io
import pathlib
import re
import sys
import types

HERE = pathlib.Path(__file__).resolve().parent          # pi-6-my/rails
GEN = HERE.parent                                       # pi-6-my
ROOT = HERE.parents[4]
RAILS_OUT = ROOT / "AI_translation/burmese/pi-6-burmese-plain-rails_split_chapters"
ZS_LINE = 'OUT = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"'
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import my_formulas_rails as L  # noqa: E402

RUNS = ["make_sample", "make_ch2-02-4-5", "make_ch3", "make_ch6-8", "make_ch7a", "make_ch7b", "make_ch9-10a",
        "make_ch10b", "make_ch10c"]
FILE_OF = {"my6_formulas": "my6_formulas", "make_ch7a": "make_ch7a"}
NO_OUT = {"my6_formulas", "make_ch7b"}                  # no OUT line of their own


class PatchError(Exception):
    pass


class Build:
    def __init__(self, out, plain):
        self.out, self.plain, self.log, self.seen = out, plain, [], set()

    def source(self, name):
        p = GEN / f"{name}.py"
        src = p.read_text(encoding="utf-8")
        if name not in NO_OUT:
            if src.count(ZS_LINE) != 1:
                raise PatchError(f"{name}.py: OUT line not found once")
            src = src.replace(ZS_LINE, f"OUT = pathlib.Path({str(self.out)!r})")
        elif "zeroshot_split_chapters" in src:
            raise PatchError(f"{name}.py: names the zero-shot folder (expected none)")
        if not self.plain:
            for old, new, count, reason in L.PATCHES.get(name, []):
                n = src.count(old)
                if n != count:
                    raise PatchError(f"{name}.py: «{old[:80]}» occurs {n}×, expected {count} ({reason[:60]})")
                src = src.replace(old, new)
                if (name, old) not in self.seen:      # log each patch once (a file is loaded once per generator run)
                    self.seen.add((name, old))
                    self.log.append((name, count, old, new, reason))
        return p, src

    def load(self, name, modname, module=None):
        p, src = self.source(name)
        mod = module if module is not None else types.ModuleType(modname)
        mod.__file__ = str(p)
        exec(compile(src, str(p), "exec"), mod.__dict__)
        return mod


class Finder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    """Serves my6_formulas / make_ch7a from the patched source (fresh per generator run)."""

    def __init__(self, build):
        self.build = build

    def find_spec(self, fullname, path=None, target=None):
        if fullname in FILE_OF:
            return importlib.util.spec_from_loader(fullname, self, origin=str(GEN / f"{FILE_OF[fullname]}.py"))
        return None

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        self.build.load(FILE_OF[module.__name__], module.__name__, module)


def run(out, plain=False):
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.md"):
        old.unlink()
    b = Build(out, plain)
    finder = Finder(b)
    sys.meta_path.insert(0, finder)
    argv = sys.argv
    try:
        for name in RUNS:
            for m in FILE_OF:
                sys.modules.pop(m, None)
            p, src = b.source(name)
            ns = {"__name__": "__main__", "__file__": str(p)}
            buf = io.StringIO()
            try:
                sys.argv = [str(p)]
                with contextlib.redirect_stdout(buf):
                    exec(compile(src, str(p), "exec"), ns)
            except SystemExit as e:
                if e.code not in (None, 0):
                    raise PatchError(f"{name}: generator exit {e.code}: {buf.getvalue()[-600:]}")
            except Exception as e:                       # noqa: BLE001  (a Miss at import, a table conflict …)
                raise PatchError(f"{name}: {type(e).__name__}: {e}\n{buf.getvalue()[-600:]}")
            bad = [l for l in buf.getvalue().splitlines() if re.search(r"MISS|Miss|CHECK|STOP|bad lines", l)]
            if bad:
                raise PatchError(f"{name}: {bad[0][:300]}")
    finally:
        sys.argv = argv
        sys.meta_path.remove(finder)
        for m in FILE_OF:
            sys.modules.pop(m, None)
    return b.log


if __name__ == "__main__":
    if "--plain" in sys.argv:
        try:
            run(pathlib.Path(sys.argv[sys.argv.index("--plain") + 1]).resolve(), plain=True)
        except PatchError as e:
            print("FAIL", e)
            sys.exit(1)
        print("plain build written")
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
                f.write(f"{w}.py\t{c}\t{esc(o)}\t{esc(n)}\t{r}\n")
        print(f"layer: {len(log)} source patches")
