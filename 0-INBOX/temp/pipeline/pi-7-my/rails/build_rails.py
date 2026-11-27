"""pi-7 Burmese RAILS build: runs the 18 zero-shot generators' own logic (pi-7-my/make_*.py + my7_formulas.py, read
only) with the rails layer (my_formulas_rails.py) and writes the chapters to the rails folder. Model: the approved
pi-6 rails build (pi-6-my/rails/build_rails.py, read only), adapted to pi-7's import chain.

usage: python3 -I -X utf8 build_rails.py [--plain OUTDIR] [--jobs N]
  * Import chain (regen_zeroshot.sh header; harmonise-notes.md): make_sample <- my7_formulas; 1-01, 1-03-05 <- sample;
    2-01-02 <- 1-03-05; 2-03-06 <- 1-01 + 1-03-05; 2-07-11 <- 2-01-02; 2-12-17, 3-01-02 <- 2-03-06; 3-03-06,
    3-07-08-10 <- 3-01-02; 3-09 <- 3-03-06; 4-01 <- 3-07-08-10; 4-02-09 <- 2-07-11 + 2-12-17 + 3-03-06 + 3-07-08-10;
    4-10-14 <- 3-09 + 4-01 + 4-02-09; 4-15-21 <- 4-10-14; 5-01-04 <- 2-07-11 + 2-12-17 + 3-09 + 4-01;
    5-05-12, 5-13-20 <- 5-01-04. The shared modules my7_formulas / make_sample are imported by name (several
    generators pop them from sys.modules to get fresh copies); the generators load each other by FILE PATH
    (importlib.util.spec_from_file_location + exec_module).
  * Here every one of the 18 generators runs in its OWN process (as regen_zeroshot.sh runs them; the processes run
    side by side, --jobs, default 6). In each process: (a) a meta-path finder serves my7_formulas / make_sample, and
    (b) importlib.util.spec_from_file_location is wrapped so that a load of any pi-7-my/make_*.py by path gets a
    spec whose loader executes the PATCHED source. So a patch of my7_formulas or of an upstream generator applies
    wherever that file runs or is imported, at every depth of the chain, exactly as a change of the file on disk
    would, and every fresh copy a generator makes is patched too.
  * Each source text is read, its OUT line (if any) is pointed at the output folder, the layer's patches are applied
    (each must match exactly its stated number of times in that file's source, else the run fails and nothing is
    kept), and the generator's own «__main__» block runs with no arguments (its NAMES). A patch that no generator
    run ever applies also fails the build. make_sample --terms is never run (my7-zeroshot-terms.md is not touched).
  * The preamble is the fixed table of regen_zeroshot.sh (written there by the coordinator), copied here.
  * --plain OUTDIR: no patches (reproduction test: OUTDIR must then equal the zero-shot byte for byte).
The zero-shot files, the generators and my7_formulas.py are only read; nothing is written in pi-7-my/ outside rails/
(sys.dont_write_bytecode: no __pycache__).
"""
import concurrent.futures
import contextlib
import importlib.abc
import importlib.machinery
import importlib.util
import io
import json
import pathlib
import re
import subprocess
import sys
import time

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent          # pi-7-my/rails
GEN = HERE.parent                                       # pi-7-my
ROOT = HERE.parents[4]
RAILS_OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters"
ZS_LINE = 'OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"'
PY = "/opt/homebrew/Caskroom/miniconda/base/bin/python3"
RUNS = ["make_sample", "make_ch1-01", "make_ch1-03-05", "make_ch2-01-02", "make_ch2-03-06", "make_ch2-07-11",
        "make_ch2-12-17", "make_ch3-01-02", "make_ch3-03-06", "make_ch3-07-08-10", "make_ch3-09", "make_ch4-01",
        "make_ch4-02-09", "make_ch4-10-14", "make_ch4-15-21", "make_ch5-01-04", "make_ch5-05-12", "make_ch5-13-20"]
BY_NAME = {"my7_formulas", "make_sample"}               # imported by module name
NO_OUT = {"my7_formulas"}                               # no OUT line of its own
BAD = re.compile(r"MISS|Miss|STOP|unmatched|bad lines|Traceback")
PREAMBLE = [                                            # = regen_zeroshot.sh «== preamble» table (read only there)
    "ထိုမြတ်စွာဘုရား၊ ရဟန္တာ၊ အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်အား ရှိခိုးပါ၏ ^T-1",
    "",
    "# အဘိဓမ္မာပိဋကတွင် ^0",
    "",
    "## အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ ^7-0",
]


class PatchError(Exception):
    pass


# ===================================================================================== one generator (child process)
class Build:
    def __init__(self, out, plain, patches):
        self.out, self.plain, self.patches = out, plain, patches
        self.log = {}                                   # (file, old) -> [count, new, reason, loads]

    def source(self, stem):
        p = GEN / f"{stem}.py"
        src = p.read_text(encoding="utf-8")
        if stem not in NO_OUT:
            if src.count(ZS_LINE) != 1:
                raise PatchError(f"{stem}.py: OUT line not found once")
            src = src.replace(ZS_LINE, f"OUT = pathlib.Path({str(self.out)!r})")
        elif "zeroshot_split_chapters" in src:
            raise PatchError(f"{stem}.py: names the zero-shot folder (expected none)")
        if not self.plain:
            for old, new, count, reason in self.patches.get(stem, []):
                n = src.count(old)
                if n != count:
                    raise PatchError(f"{stem}.py: «{old[:90]}» occurs {n}×, expected {count} ({reason[:70]})")
                src = src.replace(old, new)
                e = self.log.setdefault(f"{stem}\x00{old}", [count, new, reason, 0])
                e[3] += 1
        return p, src


class Loader(importlib.abc.Loader):
    def __init__(self, build, stem):
        self.build, self.stem = build, stem

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        p, src = self.build.source(self.stem)
        module.__file__ = str(p)
        exec(compile(src, str(p), "exec"), module.__dict__)


class Finder(importlib.abc.MetaPathFinder):
    """Serves my7_formulas / make_sample (imported by name) from the patched source, fresh at every import."""

    def __init__(self, build):
        self.build = build

    def find_spec(self, fullname, path=None, target=None):
        if fullname in BY_NAME:
            spec = importlib.machinery.ModuleSpec(fullname, Loader(self.build, fullname),
                                                  origin=str(GEN / f"{fullname}.py"))
            spec.has_location = True
            return spec
        return None


def run_one(stem, out, plain, logpath):
    import my_formulas_rails as L                       # noqa: E402  (rails/ is on sys.path: the script's folder)
    b = Build(out, plain, L.PATCHES)
    orig = importlib.util.spec_from_file_location

    def sffl(name, location=None, *a, **k):              # a generator loading another generator by its path
        p = pathlib.Path(location).resolve() if location is not None else None
        if p is not None and p.parent == GEN and p.suffix == ".py" and (GEN / p.name).is_file():
            spec = importlib.machinery.ModuleSpec(name, Loader(b, p.stem), origin=str(p))
            spec.has_location = True
            return spec
        return orig(name, location, *a, **k)

    importlib.util.spec_from_file_location = sffl
    sys.meta_path.insert(0, Finder(b))
    for m in BY_NAME:
        sys.modules.pop(m, None)
    p, src = b.source(stem)
    ns = {"__name__": "__main__", "__file__": str(p)}
    buf = io.StringIO()
    err = None
    t0 = time.time()
    try:
        sys.argv = [str(p)]
        with contextlib.redirect_stdout(buf):
            exec(compile(src, str(p), "exec"), ns)
    except SystemExit as e:
        if e.code not in (None, 0):
            err = f"{stem}: generator exit {e.code}: {buf.getvalue()[-600:]}"
    except PatchError as e:
        err = f"{stem}: {e}"
    except Exception as e:                              # noqa: BLE001  (a Miss at import, a table conflict …)
        err = f"{stem}: {type(e).__name__}: {e}\n{buf.getvalue()[-600:]}"
    outtxt = buf.getvalue()
    if err is None:
        bad = [l for l in outtxt.splitlines() if BAD.search(l)]
        if bad:
            err = f"{stem}: {bad[0][:300]}"
    wrote = [l for l in outtxt.splitlines() if l.startswith("wrote ")]
    log = [[k.split("\x00", 1)[0], v[0], k.split("\x00", 1)[1], v[1], v[2], v[3]] for k, v in b.log.items()]
    pathlib.Path(logpath).write_text(json.dumps({"stem": stem, "err": err, "wrote": wrote, "log": log,
                                                 "secs": round(time.time() - t0)}, ensure_ascii=False),
                                     encoding="utf-8")
    return 0 if err is None else 1


# ===================================================================================== the parent
def run(out, plain=False, jobs=6):
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.md"):
        old.unlink()
    logs = HERE / "build-logs"
    logs.mkdir(exist_ok=True)
    for old in logs.glob("*.json"):
        old.unlink()
    (out / "preamble.md").write_text("\n".join(PREAMBLE) + "\n", encoding="utf-8")

    def child(stem):
        lp = logs / f"{stem}.json"
        r = subprocess.run([PY, "-I", "-X", "utf8", str(HERE / "build_rails.py"), "--one", stem, str(out),
                            "plain" if plain else "rails", str(lp)], capture_output=True, text=True)
        if not lp.is_file():
            return {"stem": stem, "err": f"{stem}: no log (exit {r.returncode}) {r.stderr[-800:]}", "wrote": [],
                    "log": [], "secs": 0}
        return json.loads(lp.read_text(encoding="utf-8"))

    order = sorted(RUNS, key=lambda s: -RUNS.index(s))  # the slow late generators first
    with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as ex:
        res = {r["stem"]: r for r in ex.map(child, order)}
    for old in logs.glob("*.json"):
        old.unlink()
    logs.rmdir()
    errs = [res[s]["err"] for s in RUNS if res[s]["err"]]
    if errs:
        raise PatchError("\n".join(errs))
    applied = {}
    for s in RUNS:
        for f, c, o, n, r, loads in res[s]["log"]:
            e = applied.setdefault((f, o), [f, c, o, n, r, 0, []])
            e[5] += loads
            e[6].append(s)
    if not plain:
        import my_formulas_rails as L                   # noqa: E402
        unused = [(f, o) for f, ps in L.PATCHES.items() for o, *_ in ps if (f, o) not in applied]
        if unused:
            raise PatchError("patches never applied: " + "; ".join(f"{f}: «{o[:70]}»" for f, o in unused))
    nfiles = sum(len(res[s]["wrote"]) for s in RUNS) + 1
    order_log = [applied[(f, o)] for f, ps in __import__("my_formulas_rails").PATCHES.items() for o, *_ in ps] \
        if not plain else []
    return nfiles, order_log, {s: res[s]["secs"] for s in RUNS}


if __name__ == "__main__":
    sys.path.insert(0, str(HERE))
    if "--one" in sys.argv:
        k = sys.argv.index("--one")
        stem, out, mode, lp = sys.argv[k + 1:k + 5]
        sys.exit(run_one(stem, pathlib.Path(out), mode == "plain", lp))
    jobs = int(sys.argv[sys.argv.index("--jobs") + 1]) if "--jobs" in sys.argv else 6
    plain = "--plain" in sys.argv
    out = pathlib.Path(sys.argv[sys.argv.index("--plain") + 1]).resolve() if plain else RAILS_OUT
    try:
        nfiles, log, secs = run(out, plain, jobs)
    except PatchError as e:
        print("FAIL", e)
        sys.exit(1)
    if plain:
        print(f"plain build written: {nfiles} files")
    else:
        with open(HERE / "layer-log.tsv", "w", encoding="utf-8") as f:
            f.write("file\tcount\tloads\told\tnew\treason\n")
            esc = lambda x: x.replace("\\", "\\\\").replace("\n", "\\n").replace("\t", "\\t")  # noqa: E731
            for w, c, o, n, r, loads, _ in log:
                f.write(f"{w}.py\t{c}\t{loads}\t{esc(o)}\t{esc(n)}\t{r}\n")
        print(f"layer: {len(log)} source patches; {nfiles} files")
