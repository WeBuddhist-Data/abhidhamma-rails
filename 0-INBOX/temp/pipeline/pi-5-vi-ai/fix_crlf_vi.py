"""Restore LF line endings in the pi-5 Vietnamese working folders.

On 2026-11-21 at 09:02 a GitHub Desktop stash / pull rewrote untracked files
with CRLF (core.autocrlf=true). This only turns CRLF back into LF; no other byte changes.
Usage: python -I -X utf8 fix_crlf_vi.py <folder> [<folder> ...]
"""
import os
import sys

for folder in sys.argv[1:]:
    fixed = 0
    for root, _dirs, files in os.walk(folder):
        for name in files:
            if not name.endswith((".md", ".py", ".tsv", ".yaml", ".txt", ".json")):
                continue
            path = os.path.join(root, name)
            with open(path, "rb") as fh:
                data = fh.read()
            if b"\r\n" in data:
                with open(path, "wb") as fh:
                    fh.write(data.replace(b"\r\n", b"\n"))
                fixed += 1
    print(folder, "fixed", fixed)
