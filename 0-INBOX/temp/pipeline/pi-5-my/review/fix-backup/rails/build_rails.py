"""pi-5 Burmese RAILS build: runs the zero-shot generators' own logic (pi-5-my/make_*.py + my5_formulas.py, read
only) with the rails layer (my_formulas_rails.py) and writes the chapters to the rails folder. Model: the approved
pi-4 rails build (pi-4-my/rails/build_rails.py, read only), adapted to pi-5's import chain.

usage: python3 -I -X utf8 build_rails.py [--plain OUTDIR]
  * regen_zeroshot.sh runs each of the 8 generators in its own process. Here each runs in this process with FRESH
    modules: my5_formulas and make_sample are served by a meta-path finder (their «import my5_formulas as F» /
    «import make_sample as MS» get a new, patched module per generator run, created lazily, so make_ch2-5, which
    never imports make_sample, still does not), and the importlib blocks of make_ch11-12 … make_ch26-31
    («_spec = importlib.util.spec_from_file_location(…); P = module_from_spec(_spec); _spec.loader.exec_module(P)»)
    are replaced at source level by the same load of the patched file (make_ch6-10 inside make_ch11-12, make_ch11-12
    inside the later ones). So a patch of my5_formulas / make_sample / make_ch6-10 / make_ch11-12 applies wherever
    that file runs or is imported, exactly as a change of the file on disk would.
  * each source text is read, the layer's patches are applied in memory (each must match exactly its stated number
    of times, else the run fails and nothing is kept), the OUT line of make_sample / make_ch2-5 is pointed at the
    output folder (the later generators use MS.OUT), and the generator's own main() runs with no arguments (its
    NAMES_OUT; a MISS or CHECK stops it with exit 1 = a failed build). terms_my5.py is never run
    (my5-zeroshot-terms.md is not touched).
  * --plain OUTDIR: no patches (reproduction test: OUTDIR must then equal the zero-shot byte for byte).
The zero-shot files, the generators and my5_formulas.py are only read.
"""
import contextlib
import importlib.abc
import importlib.util
import io
import pathlib
import re
import sys
import types

HERE = pathlib.Path(__file__).resolve().parent          # pi-5-my/rails
GEN = HERE.parent                                       # pi-5-my
ROOT = HERE.parents[4]
RAILS_OUT = ROOT / "AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters"
ZS_LINE = 'OUT = ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"'
SPEC = re.compile(r'_spec = importlib\.util\.spec_from_file_location\("(\w+)", HERE / "([\w-]+)\.py"\)\n'
                  r'(\w+) = importlib\.util\.module_from_spec\(_spec\)\n_spec\.loader\.exec_module\(\3\)[^\n]*\n')
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import my_formulas_rails as L  # noqa: E402

RUNS = ["make_sample", "make_ch2-5", "make_ch6-10", "make_ch11-12", "make_ch13-16", "make_ch17-20", "make_ch21-25",
        "make_ch26-31"]
FILE_OF = {"my5_formulas": "my5_formulas", "make_sample": "make_sample"}


class PatchError(Exception):
    pass


class Build:
    def __init__(self, out, plain):
        self.out, self.plain, self.log, self.seen = out, plain, [], set()

    def source(self, name):
        p = GEN / f"{name}.py"
        src = p.read_text(encoding="utf-8")
        if name in ("make_sample", "make_ch2-5"):
            if src.count(ZS_LINE) != 1:
                raise PatchError(f"{name}.py: OUT line not found once")
            src = src.replace(ZS_LINE, f"OUT = pathlib.Path({str(self.out)!r})")
        elif "zeroshot_split_chapters" in src:
            raise PatchError(f"{name}.py: names the zero-shot folder (expected MS.OUT only)")
        if not self.plain:
            for old, new, count, reason in L.PATCHES.get(name, []):
                n = src.count(old)
                if n != count:
                    raise PatchError(f"{name}.py: «{old[:80]}» occurs {n}×, expected {count} ({reason[:60]})")
                src = src.replace(old, new)
                if (name, old) not in self.seen:      # log each patch once (a file is loaded once per generator run)
                    self.seen.add((name, old))
                    self.log.append((name, count, old, new, reason))
        src, k = SPEC.subn(lambda m: f'{m.group(3)} = __rails_load__("{m.group(2)}", "{m.group(1)}")\n', src)
        return p, src, k

    def load(self, name, modname, module=None):
        p, src, _ = self.source(name)
        mod = module if module is not None else types.ModuleType(modname)
        mod.__file__ = str(p)
        mod.__dict__["__rails_load__"] = self.load
        exec(compile(src, str(p), "exec"), mod.__dict__)
        return mod


class Finder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    """Serves my5_formulas / make_sample from the patched source (fresh per generator run)."""

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
            p, src, _ = b.source(name)
            ns = {"__name__": "rails_" + name.replace("-", "_"), "__file__": str(p), "__rails_load__": b.load}
            buf = io.StringIO()
            try:
                sys.argv = [str(p)]
                with contextlib.redirect_stdout(buf):
                    exec(compile(src, str(p), "exec"), ns)
                    ns["main"]()
            except SystemExit as e:
                raise PatchError(f"{name}: generator exit {e.code}: {buf.getvalue()[-600:]}")
            except Exception as e:                       # noqa: BLE001  (a Miss at import, a table conflict …)
                raise PatchError(f"{name}: {type(e).__name__}: {e}\n{buf.getvalue()[-600:]}")
            bad = [l for l in buf.getvalue().splitlines() if re.search(r"MISS|CHECK|STOP", l)]
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
