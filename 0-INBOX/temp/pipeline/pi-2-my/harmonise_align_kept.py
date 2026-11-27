"""Consistency pass: every repeated Pāli sentence that align_check_my.py still reports with differing Burmese must be a
genuine context difference (the Pāli context differs). Two kinds are accepted:
  * TOPIC: ch1 (the approved sample) «Atthi X, atthi Y …» lines of the abhidhamma part have no subject in the Pāli:
    the subject is the aggregate of the section (vedanā / saññā / saṅkhārā / viññāṇa), so the Burmese noun differs
    and nothing else does;
  * KEPT: the sentences listed below, each with its reason (harmonise-notes.md).
usage: python3 -I -X utf8 harmonise_align_kept.py [-v]   (exit 1 if an unexplained difference is left)"""
import difflib
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import harmonise_align_diff as A  # noqa: E402

TOPIC = {"ခံစားမှု", "မှတ်သိမှု", "ပြုပြင်ဖန်တီးမှု", "သိစိတ်"}
KEPT = {
    'Yaṃ kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā '
    'vedanā – idaṃ vuccati "dukkhaṃ".':
        "the quoted label names the word being defined: ch4 / ch6 define the dukkha of «soka-parideva-dukkha-"
        "domanass-upāyāsā» (pi-1 final «ကိုယ်ဆင်းရဲခြင်း»), ch12 the dukkha of the 4th-jhāna formula «dukkhassa ca "
        "pahānā» (pi-1 final «နာကျင်မှု»)",
    "Tattha katamaṃ saṅkhārapaccayā viññāṇaṃ?":
        "6:10 is the suttanta exposition («avijjāpaccayā saṅkhārā», plural; pi-1 final 4-03 «ပြုပြင်ဖန်တီးမှုများကြောင့်»), "
        "the others are the abhidhamma exposition («avijjāpaccayā saṅkhāro», singular)",
}


def words(a, b):
    a, b = a.split(" "), b.split(" ")
    return [(" ".join(a[i1:i2]), " ".join(b[j1:j2]))
            for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if op != "equal"]


def main(argv):
    bad = A.groups()
    topic = kept = 0
    left = []
    for s, v in bad.items():
        vs = list(v)
        diffs = [d for t in vs[1:] for d in words(vs[0], t)]
        if diffs and all(x in TOPIC and y in TOPIC for x, y in diffs):
            topic += 1
        elif s in KEPT:
            kept += 1
            if "-v" in argv:
                print(f"KEPT: {s[:90]} – {KEPT[s]}")
        else:
            left.append((s, v))
    print(f"align differences: {len(bad)} = topic noun (ch1, no subject in the Pāli): {topic}, kept (context): {kept}, "
          f"unexplained: {len(left)}")
    for s, v in left:
        print("  LEFT:", s[:120], dict((t[:80], l[:3]) for t, l in v.items()))
    return len(left)


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
