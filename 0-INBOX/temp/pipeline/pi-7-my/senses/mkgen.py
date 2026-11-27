"""One-off: write gen_decisions_my.py for pi-7 from pi-6-my/senses/gen_decisions_my.py: its engine (functions, incl. the
MR_ADJUST step) unchanged, binding chain pi-6, pi-5, pi-4, pi-3, pi-2, pi-1, Marathi pi-7 tags, and empty MANUAL /
TAG_CHANGED / NEW_SENSE / LUMP_OK / MR_ADJUST tables (filled for pi-7 afterwards)."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE.parents[1] / 'pi-6-my/senses/gen_decisions_my.py').read_text(encoding='utf-8')
eng = src[src.index('\ndef parse_line'):]
def rep(a, b):
    global eng
    assert eng.count(a) == 1, a
    eng = eng.replace(a, b)
rep('pi-6 sense decisions', 'pi-7 sense decisions')
rep("'# English tags: pi-5, then pi-4, pi-3, pi-2, pi-1 Burmese senses (binding), else Marathi pi-6 senses '",
    "'# English tags: pi-6, then pi-5, pi-4, pi-3, pi-2, pi-1 Burmese senses (binding), else Marathi pi-7 senses '")
rep("'# values: pi-6 Burmese keyword map only.\\n'", "'# values: pi-7 Burmese keyword map only.\\n'")
rep('# pi-5 first where several list a value', '# pi-6 first where several list a value')
bad = [l for l in eng.split('\n') if ('pi-5' in l or 'pi-6' in l) and 'pi-6 first' not in l and 'pi-6, then' not in l]
assert not bad, bad
head = '''"""Write the Pāli→Burmese pi-7 decisions file for senses_my.py (brief: pi-7-my/burmese-senses-brief.md).
Adapted from pi-6-my/senses/gen_decisions_my.py (same engine and MANUAL / LUMP_OK / TAG_CHANGED / NEW_SENSE / MR_ADJUST
mechanism); the binding chain is now pi-6, then pi-5, pi-4, pi-3, pi-2, pi-1; the tags for headwords new in pi-7 come
from the Marathi pi-7 senses (tags only).

usage: python -I -X utf8 gen_decisions_my.py <agg.tsv> <decisions.txt>

For every headword of agg.tsv that has Burmese values (NDE-only headwords are skipped):
  1. a hand decision in MANUAL below wins;
  2. otherwise the approved Burmese senses are BINDING, pi-6 first, then pi-5, pi-4, pi-3, pi-2, pi-1 (each looked up
     exact, else the one case-insensitive match: the aggregation keeps the first spelling seen). The reference is the
     line of the first of pi-6 / pi-5 / pi-4 / pi-3 / pi-2 / pi-1 that has the headword. Every pi-7 value that the
     reference lists goes under the reference's sense with its English tag, in the reference's sense order (a sense
     with no pi-7 value is left out). A pi-7 value the reference does not list:
       - a later binding file lists it: that file's sense (tag) is added after the reference's, or the value joins the
         reference sense with the same tag (REVIEW);
       - otherwise, the reference has one sense: the value joins it (REVIEW unless the headword is in LUMP_OK);
       - otherwise (the reference has several senses): UNRESOLVED (write MANUAL);
  3. otherwise, if the Marathi pi-7 senses file gives the headword ONE English tag, the line is that tag + every
     attested Burmese value (one sense; several values -> REVIEW unless LUMP_OK); where that Marathi tag does not
     describe the headword the Burmese values show (e.g. the tag of a compound member, or a positive tag on a negated
     form), MR_ADJUST gives the adjusted English tag with its logged reason (only for such headwords);
  4. otherwise (several Marathi senses, or no Marathi line) the headword is UNRESOLVED: write MANUAL.
Only the ENGLISH tags are read from the Marathi file; its Marathi values are dropped on parsing and never written.
A MANUAL entry for a pi-6 / pi-5 / pi-4 / pi-3 / pi-2 / pi-1 headword must keep the binding split: every value the
binding senses list (pi-6's sense for it, else pi-5's, pi-4's, pi-3's, pi-2's, pi-1's) sits under a sense whose tag
starts with that binding tag (an appended «, …» is allowed) unless the headword is in TAG_CHANGED (logged reason); and a
MANUAL sense that holds only values the binding senses do not list, with a tag that starts with none of the binding
tags, is a NEW sense and the headword must be in NEW_SENSE (logged reason).
The script fails (exit 1) while anything is UNRESOLVED, a MANUAL value is not attested, a MANUAL entry omits an
attested value, a MANUAL entry breaks a binding sense, or a new sense is not logged in NEW_SENSE.
"""
import pathlib
import re
import sys
from collections import OrderedDict

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BIND_FILES = OrderedDict([
    ('p6', ROOT / 'AI_translation/burmese/pi-6-pali-word-burmese-senses-plain.md'),
    ('p5', ROOT / 'AI_translation/burmese/pi-5-pali-word-burmese-senses-plain.md'),
    ('p4', ROOT / 'AI_translation/burmese/pi-4-pali-word-burmese-senses-plain.md'),
    ('p3', ROOT / 'AI_translation/burmese/pi-3-pali-word-burmese-senses-plain.md'),
    ('p2', ROOT / 'AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md'),
    ('p1', ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md'),
])
BOOK = {'p6': 'pi-6', 'p5': 'pi-5', 'p4': 'pi-4', 'p3': 'pi-3', 'p2': 'pi-2', 'p1': 'pi-1'}
MR_SENSES = ROOT / 'AI_translation/marathi/pi-7-pali-word-marathi-senses-plain.md'
VAL_RE = re.compile(r'^(.*)=(\\d+)\\[[^\\]]*\\]$')
NONLATIN = re.compile(r'[\\u0900-\\u097f\\u1000-\\u109f]')

# Hand decisions: headword -> [(English tag, [Burmese values])]. Values must be attested.
# Binding senses first (pi-6, else pi-5, pi-4, pi-3, pi-2, pi-1 order and tag), then the senses new in pi-7.
MANUAL = OrderedDict([
    # ======== sample (agg-sample.tsv, the first 80 headwords) ========
    # @@MANUAL-SAMPLE
    # ======== full run (agg-part1.tsv) ========
    # @@MANUAL-FULL
])

# Binding headwords whose MANUAL entry deliberately departs from a binding tag (headword: reason).
TAG_CHANGED = {
    # @@TAGCH
}

# Binding headwords whose MANUAL entry adds a sense with values the binding senses do not list (headword: reason).
NEW_SENSE = {
    # ---- sample ----
    # @@NEW-SAMPLE
    # ---- full run ----
    # @@NEW-FULL
}

# Several Burmese values under one sense, or a value the binding sense does not list, checked by hand
# (variants or synonyms of one meaning, or the pi-7 text's own word for the binding meaning).
LUMP_OK = {
    # ---- sample ----
    # @@LUMP-SAMPLE
    # ---- full run: REVIEW headwords checked by hand ----
    # @@LUMP-FULL
}

# Headwords new in pi-7 (no binding line) whose single Marathi pi-7 tag does not describe the headword as the Burmese
# values show it: headword -> (adjusted English tag, reason).
MR_ADJUST = {
    # ---- sample ----
    # @@ADJ-SAMPLE
    # ---- full run ----
    # @@ADJ
}

'''
eng = eng[eng.index('\ndef parse_line'):]
(HERE / 'gen_decisions_my.py').write_text(head + eng, encoding='utf-8')
print('ok')
