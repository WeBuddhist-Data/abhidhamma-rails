"""Per-line check of pi-2 Burmese chapter 17 (Khuddakavatthuvibhaṅgo) against its Pāli, plus the pi-1 reuse test.

usage: python3 -I -X utf8 check_ch17.py <pali_file> <burmese_file>
Adapted from check_sample.py (own tables, independent of make_ch17.py). For every non-empty line (same order):
  1. sentences  - Pāli sentence ends («.» «?» «!» outside variant brackets and labels) = Burmese «။»;
  2. negations  - Pāli negation morphemes (free na / no / neva / mā / natthi, the privative words of NEG_WORDS;
                  double forms = 2) against Burmese negation markers («မ» before a verb syllable, «အကုسိုလ်»);
  3. numbers    - Pāli number words (dve … dvāsaṭṭhi) against Burmese number words before «ပါး»;
  4. variants   - same count of «[»; the Roman text of every Pāli variant occurs in the Burmese line;
  5. typography - no «?», «।», «:-», no Latin letters outside brackets, Myanmar only, NFC.
Then the pi-1 REUSE TEST: every Pāli sentence of the file that also occurs in pi-1 (Pāli) must have exactly pi-1's
final Burmese sentence (rails text) in its line. Prints n / n.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
P1_PALI = ROOT / "AI_translation/pali/pi-1_split_chapters"
P1_MY = ROOT / "AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters"
ID = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
BR = re.compile(r"\[[^\]]*\]")
WB = r"(?<![A-Za-zāīūṃṅñṭḍṇḷ])"
WE = r"(?![A-Za-zāīūṃṅñṭḍṇḷ])"

# ------------------------------------------------------------------ negations (Pāli)
NEG2 = [r"neva\w*", r"adukkhamasukh\w*", r"nevasaññīnāsaññ\w*", r"nevasaññānāsaññ\w*", r"nevarūpīnārūp\w*",
        r"nevantavā"]          # double forms are counted by their parts below (neva + na/a-)
NEG_WORDS = (
    "na no mā natthi nāhosi nādhimuccati nālatthaṃ nāhaṃ nāsātaṃ nānantavā neso nevāhaṃ "
    "asakkaccakiriyatā asātaccakiriyatā anaṭṭhitakiriyatā anāsevanā abhāvanā abahulīkammaṃ anadhiṭṭhānaṃ ananuyogo "
    "amudutā asantuṭṭhassa assaddho asamāhito akhīṇāsavo anavaññāta\\w* anādariyaṃ anādariyatā anādaratā agāravatā "
    "appatissavatā appaṭissavatā anabhirati anabhiramaṇā aratitā arati akalyatā akammaññatā anuttānīkammaṃ "
    "anāvikammaṃ appaṭinissaggo anajjavo anajjavatā amaddavo amaddavatā akkhanti akkhamanatā anadhivāsanatā "
    "asoraccaṃ asākhalyaṃ asamādhisaṃvattanikā asaṇhavācatā asakhilavācatā appaṭisanthāro appaṭisandhāro "
    "appaṭisanthārako aguttadvāratā agutti agopanā anārakkho asaṃvaro asaṃvutaṃ amattaññutā appaṭisaṅkhā ayoniso "
    "asati assati ananussati appaṭissati asaraṇatā assaraṇatā adhāraṇatā asampajaññaṃ asampajaññatā aññāṇaṃ "
    "adassanaṃ anabhisamayo ananubodho asambodho appaṭivedho asaṃgāhanā apariyogāhanā asamapekkhanā "
    "apaccavekkhaṇā apaccakkhakammaṃ asampajaññaṃ avijjā avijjogho avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ "
    "avijjālaṅgī avijjāsavo avijjāsaṃyojanaṃ avijjāpariyuṭṭhānaṃ akusal\\w* ahirik\\w* anottapp\\w* appiyassa "
    "amanāpassa aṭṭhāne asassato anantavā anantavādiṭṭhi anariyavohārā adiṭṭhe assute amute aviññāte adiṭṭhavāditā "
    "assutavāditā amutavāditā aviññātavāditā alābhe ayase avītarāgo avigatacchando avigatapemo avigatapipāso "
    "avigatapariḷāho avigatataṇho assaddhiyaṃ assaddahanā anokappanā anabhippasādo avadaññutā anaddā anaddāyanā "
    "anaddāyitattaṃ asīlyaṃ acittīkāro adassanakamyatā adaṭṭhukamyatā asametukamyatā asamāgantukamyatā "
    "asotukamyatā asavanakamyatā anuggahetukamyatā adhāretukamyatā anicce anattani asubhe anāvaṭṭanā "
    "appatte akate anadhigate asacchikate anattamano anattamanatā agāravo appatisso appamāde amanāpo appiyo "
    "asaddhammā anottappī appattassa anadhigatassa asacchikatassa akammañño aciravuṭṭhito abyattassa appaccayañca "
    "anādiyitvā anāpannomhī assatiyāva asaññī asaññīvādā asaññivādā arūpī amanāpiyesu asātaṃ asātā "
    "avipariṇāmadhammo avipariṇāmadhammosmīti anattanā anattānaṃ asasmīti ahetu appaccayā asayaṅkāraṃ "
    "aparaṅkāraṃ anavakāriṃ amanasikārā ananto anantaṃ ākiñcaññāyatanūpago ākāsānañcāyatanūpago ākāsānañcāyatanaṃ "
    "viññāṇañcāyatanūpago viññāṇañcāyatanaṃ ākiñcaññāyatanaṃ nevasaññānāsaññāyatanūpago ahīnindriyo arūparāgo "
    "arūpataṇhā arūpadhātu\\w* adhammacariyā\\w* asantuṭṭhitā anupārambho anupārambhanā anupārambhitattaṃ "
    "adhammarāgo aniccā avūpasamo amara asabhāga dovacass assutavā adassāvī akovido avinīto").split()
NEG_WORDS += "anavaññatti agārav assaddh adinnādān".split()
NEG_WORDS = [w for w in NEG_WORDS if w not in ("anupārambho", "anupārambhanā", "anupārambhitattaṃ", "anāvaṭṭanā",
                                               "nāsātaṃ", "adukkhamasukh", "asasmīti",
                                               "nevasaññānāsaññāyatanūpago", "nānantavā")]
NEG_PI = [(re.compile(WB + "(?:" + "|".join((w.rstrip("ṃ") + r"\w*" if len(w) > 4 else w + WE) for w in sorted(dict.fromkeys(NEG_WORDS),
                                                                                       key=len, reverse=True)) + ")",
                      re.I), 1)]
NEG_PI += [(re.compile(WB + r"neva", re.I), 1), (re.compile(r"(?:nāsaññ|nārūp|nānant|nāsāt)"), 2),
           (re.compile(WB + r"adukkhamasukh", re.I), 2), (re.compile(r"(?<=dhātu)arūp"), 1)]
LETTER, CLOSE = "က-ဪ", "္်"
NEG_MY = [("ကာမ|မနော|မည်သည့်|မဆို(?!း)|သို့မဟုတ်|တမလွန်|မည်|(?<=္)မ", 0), ("အကုသိုလ်", 1),
          (r"မ(?=[" + LETTER + r"](?!့?[" + CLOSE + r"]))", 1)]
NEG_MY_RE = [(re.compile(p), w) for p, w in NEG_MY]
NOT_NEG = {"ākāsānañcāyatanūpago": 0}   # placeholder (kept for documentation)


def neg_pi(s):
    n = s.count('"Natthi dinnaṃ, natthi yiṭṭhaṃ…pe…')     # the elided last «natthi» carries «ye … pavedenti»
    s = BR.sub("", s).replace("…pe…", " ")
    for rx, w in NEG_PI:
        n += w * len(rx.findall(s))
    return n


def neg_my(s):
    s = BR.sub("", s)
    for rx, w in NEG_MY_RE:
        if w == 0:
            s = rx.sub(" ", s)
    return sum(w * len(rx.findall(s)) for rx, w in NEG_MY_RE if w)


# known differences (polarity carried by the Burmese wording, or a Pāli negation elided by «…pe…»): block id -> delta
NEG_OK = {}

# ------------------------------------------------------------------ numbers
NUM_PI = {"dve": "နှစ်", "tīṇi": "သုံး", "tayo": "သုံး", "tisso": "သုံး", "cattāro": "လေး", "cattāri": "လေး",
          "catasso": "လေး", "pañca": "ငါး", "cha": "ခြောက်", "satta": "ခုနစ်", "aṭṭha": "ရှစ်", "nava": "ကိုး",
          "dasa": "ဆယ်", "aṭṭhārasa": "ဆယ့်ရှစ်", "chattiṃsa": "သုံးဆယ့်ခြောက်", "dvāsaṭṭhi": "ခြောက်ဆယ့်နှစ်",
          "soḷasa": "ဆယ့်ခြောက်"}
NUM_PI.update({"pañcahi": "ငါး", "pañcasu": "ငါး", "channaṃ": "ခြောက်", "aṭṭhasu": "ရှစ်", "pañcorambhāgiyāni": "ငါး",
               "pañcuddhambhāgiyāni": "ငါး", "pañcindriyāni": "ငါး", "sattānusayā": "ခုနစ်", "aṭṭhaanariyavohārā": "ရှစ်", "aṭṭhaṅgiko": "ရှစ်", "cātumahābhūtiko": "လေး"})
NUM_RE = re.compile(WB + "(" + "|".join(sorted(NUM_PI, key=len, reverse=True)) + r")(?=[ .,?]|$)", re.I)


def nums_pi(s):
    s = BR.sub("", s)
    out = ["တစ်ရာ့ရှစ်"] * len(re.findall(r"aṭṭha ?taṇhāvicaritasataṃ", s))
    s = re.sub(r"aṭṭha ?taṇhāvicaritasataṃ", " ", s)
    out += ["ဆယ်"] * len(re.findall(WB + "dasavatthuk", s))
    return sorted(out + [NUM_PI[x[:1].lower() + x[1:]] for x in NUM_RE.findall(s)])


def nums_my(s):
    found = re.findall(r"(\S+)ပါး", BR.sub("", s))
    return sorted(x for x in found if x in NUM_PI.values() or x == "တစ်ရာ့ရှစ်")


# ------------------------------------------------------------------ sentences
def sent_pi(s):
    s = BR.sub("", s)
    s = re.sub(r"\((?:\d+\. )?[^()]*\)", "", s)
    return len(re.findall(r"[.?!](?=[\"”’]*(?:\s|$))", s))


def sent_my(s):
    return s.count("။")


# ------------------------------------------------------------------ pi-1 sentences
def psplit(l):
    l = ID.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]


def bsplit(l):
    return [s for s in re.split(r"(?<=။) ", ID.sub("", l)) if s]


S1 = {}
for p in sorted(P1_PALI.glob("*.md")):
    for a, b in zip(p.read_text(encoding="utf-8-sig").split("\n"), (P1_MY / p.name).read_text(encoding="utf-8").split("\n")):
        if a.startswith("#"):
            continue
        ps, bs = psplit(a), bsplit(b)
        if len(ps) == len(bs):
            for x, y in zip(ps, bs):
                S1.setdefault(x, y)


def main(pf, mf):
    A = [l for l in pathlib.Path(pf).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    B = [l for l in pathlib.Path(mf).read_text(encoding="utf-8").splitlines() if l.strip()]
    bad = []
    if len(A) != len(B):
        bad.append(f"line count {len(A)} / {len(B)}")
    reuse_n = reuse_ok = 0
    bid = ""
    for i, (a, b) in enumerate(zip(A, B), 1):
        m = ID.search(a)
        bid = m.group(1) if m else bid
        if a.startswith("#"):
            b = b.lstrip("#").lstrip()
        if unicodedata.normalize("NFC", b) != b:
            bad.append(f"{i}: not NFC")
        body = ID.sub("", b)
        if re.search(r"[?।]|:-", BR.sub("", body)):
            bad.append(f"{i}: forbidden mark")
        if re.search(r"[A-Za-z]", BR.sub("", body).replace("(?)", "")):
            bad.append(f"{i}: Latin outside brackets: {BR.sub('', body)[:60]}")
        if re.search(r"[^က-႟\s\[\]()0-9.,;:“”‘’…–\-+=A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ'\"^?/]", body):
            bad.append(f"{i}: unexpected character")
        if a.startswith("#"):
            continue
        if sent_pi(a) != sent_my(b):
            bad.append(f"{i} {bid}: sentences {sent_pi(a)} / {sent_my(b)}")
        dn = neg_pi(a) - neg_my(b)
        if dn != NEG_OK.get(bid, 0):
            bad.append(f"{i} {bid}: negations Pāli {neg_pi(a)} / Burmese {neg_my(b)}")
        if nums_pi(a) != nums_my(b):
            bad.append(f"{i} {bid}: numbers {nums_pi(a)} / {nums_my(b)}")
        if a.count("[") != b.count("["):
            bad.append(f"{i}: [ count")
        for v in re.findall(r"\[([^\]\(]+?) \(", a):
            for w in v.split(", "):
                if w.strip("( ") and w.strip("( ") not in b:
                    bad.append(f"{i}: variant text «{w}» missing")
        for s in psplit(a):
            k = s.replace("upādinn", "upādiṇṇ")
            k = k[:1].upper() + k[1:]
            if k in S1 and k[:1] == s[:1].upper():
                reuse_n += 1
                if S1[k] in b:
                    reuse_ok += 1
                else:
                    bad.append(f"{i}: pi-1 sentence not reused: {s[:60]}")
    for x in bad:
        print("MISMATCH", x)
    print(f"{pathlib.Path(mf).name}: {len(bad)} mismatches ({len(A)} lines)")
    print(f"pi-1 reuse: {reuse_ok} / {reuse_n} identical")
    return len(bad)


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1], sys.argv[2]) else 0)
