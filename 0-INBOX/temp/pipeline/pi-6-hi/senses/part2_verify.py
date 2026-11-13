"""part 2 helper: run senses_tool_pi6.verify with one parser change.

The tool's parse_out_line splits tag from values with rsplit(': ', 1), which breaks on heading values that keep
the Hindi colon (convention 8: «विपरीत: व्यक्ति», «नकारात्मक: स्थान»). Tags never contain ': ', so splitting at the
FIRST ': ' is exact. Everything else in verify is unchanged. The tool file itself is not modified.

python -I -X utf8 part2_verify.py <agg.tsv> <out.md>
"""
import importlib.util
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('senses_tool_pi6', os.path.join(HERE, 'senses_tool_pi6.py'))
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


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


tool.parse_out_line = parse_out_line
sys.exit(tool.verify(sys.argv[1], sys.argv[2]))
