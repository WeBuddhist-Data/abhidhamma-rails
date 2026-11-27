"""One-off: write gen_decisions_my.py for pi-6 from pi-5-my/senses/gen_decisions_my.py: its engine (functions) unchanged,
binding chain pi-5, pi-4, pi-3, pi-2, pi-1, Marathi pi-6 tags, and empty MANUAL / TAG_CHANGED / NEW_SENSE / LUMP_OK
tables (filled for pi-6 afterwards)."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE.parents[1] / 'pi-5-my/senses/gen_decisions_my.py').read_text(encoding='utf-8')
eng = src[src.index('\ndef parse_line'):]
eng = eng.replace('pi-5 sense decisions', 'pi-6 sense decisions')
eng = eng.replace("'# English tags: pi-4, then pi-3, then pi-2, then pi-1 Burmese senses (binding), else Marathi pi-5 senses '",
                  "'# English tags: pi-5, then pi-4, pi-3, pi-2, pi-1 Burmese senses (binding), else Marathi pi-6 senses '")
eng = eng.replace("'# values: pi-5 Burmese keyword map only.\\n'", "'# values: pi-6 Burmese keyword map only.\\n'")
eng = eng.replace('# pi-4 first where several list a value', '# pi-5 first where several list a value')
assert not [l for l in eng.split('\n') if 'pi-5' in l and 'pi-5 first' not in l and 'pi-5, then' not in l], [l for l in eng.split('\n') if 'pi-5' in l]
head = '''"""Write the Pāli→Burmese pi-6 decisions file for senses_my.py (brief: pi-6-my/burmese-senses-brief.md).
Adapted from pi-5-my/senses/gen_decisions_my.py (same engine and MANUAL / LUMP_OK / TAG_CHANGED / NEW_SENSE mechanism);
the binding chain is now pi-5, then pi-4, pi-3, pi-2, pi-1; the tags for headwords new in pi-6 come from the Marathi pi-6
senses (tags only).

usage: python -I -X utf8 gen_decisions_my.py <agg.tsv> <decisions.txt>

For every headword of agg.tsv that has Burmese values (NDE-only headwords are skipped):
  1. a hand decision in MANUAL below wins;
  2. otherwise the approved Burmese senses are BINDING, pi-5 first, then pi-4, pi-3, pi-2, pi-1 (each looked up exact,
     else the one case-insensitive match: the aggregation keeps the first spelling seen). The reference is the line of
     the first of pi-5 / pi-4 / pi-3 / pi-2 / pi-1 that has the headword. Every pi-6 value that the reference lists goes
     under the reference's sense with its English tag, in the reference's sense order (a sense with no pi-6 value is
     left out). A pi-6 value the reference does not list:
       - a later binding file lists it: that file's sense (tag) is added after the reference's, or the value joins the
         reference sense with the same tag (REVIEW);
       - otherwise, the reference has one sense: the value joins it (REVIEW unless the headword is in LUMP_OK);
       - otherwise (the reference has several senses): UNRESOLVED (write MANUAL);
  3. otherwise, if the Marathi pi-6 senses file gives the headword ONE English tag, the line is that tag + every
     attested Burmese value (one sense; several values -> REVIEW unless LUMP_OK);
  4. otherwise (several Marathi senses, or no Marathi line) the headword is UNRESOLVED: write MANUAL.
Only the ENGLISH tags are read from the Marathi file; its Marathi values are dropped on parsing and never written.
A MANUAL entry for a pi-5 / pi-4 / pi-3 / pi-2 / pi-1 headword must keep the binding split: every value the binding
senses list (pi-5's sense for it, else pi-4's, pi-3's, pi-2's, pi-1's) sits under a sense whose tag starts with that
binding tag (an appended «, …» is allowed) unless the headword is in TAG_CHANGED (logged reason); and a MANUAL sense
that holds only values the binding senses do not list, with a tag that starts with none of the binding tags, is a NEW
sense and the headword must be in NEW_SENSE (logged reason).
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
    ('p5', ROOT / 'AI_translation/burmese/pi-5-pali-word-burmese-senses-plain.md'),
    ('p4', ROOT / 'AI_translation/burmese/pi-4-pali-word-burmese-senses-plain.md'),
    ('p3', ROOT / 'AI_translation/burmese/pi-3-pali-word-burmese-senses-plain.md'),
    ('p2', ROOT / 'AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md'),
    ('p1', ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md'),
])
BOOK = {'p5': 'pi-5', 'p4': 'pi-4', 'p3': 'pi-3', 'p2': 'pi-2', 'p1': 'pi-1'}
MR_SENSES = ROOT / 'AI_translation/marathi/pi-6-pali-word-marathi-senses-plain.md'
VAL_RE = re.compile(r'^(.*)=(\\d+)\\[[^\\]]*\\]$')
NONLATIN = re.compile(r'[\\u0900-\\u097f\\u1000-\\u109f]')

# Hand decisions: headword -> [(English tag, [Burmese values])]. Values must be attested.
# Binding senses first (pi-5, else pi-4, pi-3, pi-2, pi-1 order and tag), then the senses new in pi-6.
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
# (variants or synonyms of one meaning, or the pi-6 text's own word for the binding meaning).
LUMP_OK = {
    # ---- sample ----
    # @@LUMP-SAMPLE
    # ---- full run: REVIEW headwords checked by hand ----
    # @@LUMP-FULL
}

'''
(HERE / 'gen_decisions_my.py').write_text(head + eng, encoding='utf-8')
print('ok')
