"""pi-2 Burmese RAILS build: runs the zero-shot generators' own logic (pi-2-my/make_*.py + my2_formulas.py, read
only) with the rails layer (my_formulas_rails.py) and writes the chapters to the rails folder.

usage: python3 -I -X utf8 build_rails.py [--plain OUTDIR]
  * each generator runs in this process with a fresh my2_formulas module, as each zero-shot generator runs in its own
    process; my2_formulas.py and the generator are read as text, the layer's source patches are applied in memory
    (each patch must match exactly its stated number of times, else the run fails and nothing is kept), and the code
    is executed with OUT pointing at the rails folder (a source-level change of the OUT line, because make_ch17.py
    reads the other pi-2 chapters from OUT at import: its pi-2 sentence table is then the RAILS text) and the
    generators' «partial-» dump on a stop pointing at rails/scratch. The generators' term / notes writers are never
    called (my2-zeroshot-terms.md and notes-*.md are not touched).
  * order: as regen_zeroshot.sh, except that make_ch18 runs before make_ch17 (make_ch17 reads every other chapter
    from OUT, so the 18th chapter must already be there: the same fixed point as the zero-shot, from an empty folder).
  * --plain OUTDIR: no patches (reproduction test: OUTDIR must then equal the zero-shot byte for byte).
The zero-shot files, the generators and my2_formulas.py are only read.
"""
import pathlib
import sys
import types

HERE = pathlib.Path(__file__).resolve().parent          # pi-2-my/rails
GEN = HERE.parent                                       # pi-2-my
ROOT = HERE.parents[4]
RAILS_OUT = ROOT / "AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters"
ZS_LINE = 'OUT = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"'
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import my_formulas_rails as L  # noqa: E402


def _ch(ns, k):
    if ns[k] is False:
        raise PatchError(f"chapter writer {k} reported a stop")


# generator -> what its «__main__» block writes (the chapter writers only; never write_terms / write_notes)
RUNS = [
    ("make_sample", lambda ns: (ns["preamble"](), ns["chapter"]("1-khandhavibhango.md"))),
    ("make_ch2-4", lambda ns: (ns["install_rules"](), [ns["chapter"](n) or _stop(n) for n in ns["NAMES_OUT"]])),
    ("make_ch5-7-11", lambda ns: [ns["chapter"](n) or _stop(n) for n in ns["CHAPTERS"]]),
    ("make_ch6", lambda ns: ns["chapter"]()),
    ("make_ch12-14", lambda ns: (ns["rebuild_frames"](), [ns["chapter"](n) or _stop(n) for n in ns["NAMES_OUT"].values()])),
    ("make_ch15-16", lambda ns: [ns["chapter"](n) for n in ns["NAMES_OUT"]]),
    ("make_ch18", lambda ns: ns["main"]()),
    ("make_ch17", lambda ns: ns["main"]()),
]


class PatchError(Exception):
    pass


def _stop(name):
    raise PatchError(f"{name}: the generator stopped (a line no rule matches)")


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
    p = GEN / "my2_formulas.py"
    src = p.read_text(encoding="utf-8")
    log = []
    if not plain:
        src, log = patched(src, L.FORMULA_PATCHES, "my2_formulas.py")
    mod = types.ModuleType("my2_formulas")
    mod.__file__ = str(p)
    sys.modules["my2_formulas"] = mod
    exec(compile(src, str(p), "exec"), mod.__dict__)
    if not plain:
        L.after_import(mod)
    return mod, log


def run(out, plain=False):
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.md"):
        old.unlink()
    scratch = HERE / "scratch"
    log = []
    for name, main in RUNS:
        F, flog = fresh_formulas(plain)
        log += flog if name == RUNS[0][0] else []
        p = GEN / f"{name}.py"
        src = p.read_text(encoding="utf-8")
        if src.count(ZS_LINE) != 1:
            raise PatchError(f"{name}.py: OUT line not found once")
        src = src.replace(ZS_LINE, f"OUT = pathlib.Path({str(out)!r})")
        src = src.replace('HERE / "scratch"', f"pathlib.Path({str(scratch)!r})")
        if not plain:
            src, glog = patched(src, L.GEN_PATCHES.get(name, []), f"{name}.py")
            log += glog
        src = src.split('\nif __name__ == "__main__":\n')[0]
        ns = {"__name__": "rails_" + name.replace("-", "_"), "__file__": str(p)}
        try:
            exec(compile(src, str(p), "exec"), ns)
            main(ns)
        except SystemExit as e:
            raise PatchError(f"{name}: generator exit {e.code}")
        sys.modules.pop("my2_formulas", None)
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
            esc = lambda x: x.replace("\\", "\\\\").replace("\n", "\\n").replace("\t", "\\t")
            for w, c, o, n, r in log:
                f.write(f"{w}\t{c}\t{esc(o)}\t{esc(n)}\t{r}\n")
        print(f"layer: {len(log)} source patches")
