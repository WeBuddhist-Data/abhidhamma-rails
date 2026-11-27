"""One-off: add the MR_ADJUST step to gen_decisions_my.py (pi-6)."""
import pathlib
p = pathlib.Path(__file__).resolve().parent / 'gen_decisions_my.py'
s = p.read_text(encoding='utf-8')
def rep(a, b):
    global s
    assert s.count(a) == 1, a
    s = s.replace(a, b)
rep("    stats['mr'] = 0\n", "    stats['mr'] = 0\n    stats['mr_adjusted'] = 0\n    adjusted = set()\n")
rep("""            if tags and len(tags) == 1:
                senses = [(tags[0], list(vals))]
                stats['mr'] += 1
""", """            if tags and len(tags) == 1:
                tag = tags[0]
                if hw in MR_ADJUST:
                    tag = MR_ADJUST[hw][0]
                    adjusted.add(hw)
                    stats['mr_adjusted'] += 1
                senses = [(tag, list(vals))]
                stats['mr'] += 1
""")
rep("""    unused = [h for h in list(MANUAL) + list(LUMP_OK) if h not in rows]
""", """    for h in MR_ADJUST:
        if h in rows and h not in adjusted:
            errs.append(f'{h}: MR_ADJUST entry for a headword that does not take a single Marathi tag')
        if not MR_ADJUST[h][1].strip():
            errs.append(f'{h}: MR_ADJUST entry without a reason')
    unused = [h for h in list(MANUAL) + list(LUMP_OK) + list(MR_ADJUST) if h not in rows]
""")
rep("""

def parse_line(line):""", """
# Headwords new in pi-6 (no binding line) whose single Marathi pi-6 tag does not describe the headword as the Burmese
# values show it: headword -> (adjusted English tag, reason). NEW in pi-6.
MR_ADJUST = {
    # @@ADJ
}


def parse_line(line):""")
p.write_text(s, encoding='utf-8')
print('ok')
