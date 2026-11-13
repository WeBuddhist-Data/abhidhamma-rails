"""Termbase adherence on given Hindi files (the sample pairs live outside the output folder).
Runs the unchanged logic of 0-INBOX/temp/pipeline/hindi_termbase_adherence.py, with its directory glob
replaced by the file list.
usage: python -I -B -X utf8 adherence_sample.py <keywords.md> <termbase.md> <hindi files...>"""
import pathlib
import runpy
import sys

kw, tb, *files = sys.argv[1:]
paths = [pathlib.Path(f) for f in files]
_orig_glob = pathlib.Path.glob


def _glob(self, pattern):
    if str(self) == "__SAMPLE__":
        return iter(paths)
    return _orig_glob(self, pattern)


pathlib.Path.glob = _glob
sys.argv = ["hindi_termbase_adherence.py", kw, tb, "__SAMPLE__"]
runpy.run_path(str(pathlib.Path(__file__).resolve().parents[2] / "hindi_termbase_adherence.py"), run_name="__main__")
