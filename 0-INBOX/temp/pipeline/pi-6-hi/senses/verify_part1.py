"""Run senses_tool_pi6.verify with one parser fix, without editing the shared tool.

The stock parser splits each sense at the LAST ': ' (rsplit), so a value that itself contains ': '
(the heading values «सकारात्मक: व्यक्ति», «नकारात्मक: स्थान» …, kept with their colon by convention §8)
is cut inside the value. Tags may not contain ': ' (tool docstring), so the first ': ' of a sense is
always the tag/value boundary; this wrapper splits there and otherwise runs the stock verify unchanged.

Usage: python -I -X utf8 verify_part1.py <agg.tsv> <out.md>
"""
import importlib.util
import os
import sys

sys.dont_write_bytecode = True
D = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('senses_tool_pi6', os.path.join(D, 'senses_tool_pi6.py'))
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)


def parse_out_line(line, allow_tag_only=False):
    i = line.find(': {')
    if i < 0 or not line.endswith('}'):
        raise ValueError(f'bad line: {line!r}')
    hw = line[:i]
    body = line[i + 3:-1]
    if allow_tag_only and ': ' not in body:
        return hw, [(body.strip(), None)]
    senses = []
    for s in body.split('; '):
        if ': ' not in s:
            raise ValueError(f'sense without "tag: value" in {hw!r}: {s!r}')
        tag, vals = s.split(': ', 1)
        senses.append((tag.strip(), [v.strip() for v in vals.split(' / ')]))
    return hw, senses


T.parse_out_line = parse_out_line

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(T.verify(sys.argv[1], sys.argv[2]))
