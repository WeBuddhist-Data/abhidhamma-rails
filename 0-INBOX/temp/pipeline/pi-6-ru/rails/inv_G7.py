"""G7 inventory helper: distinct sentence templates in 7-01 … 7-11 (writes nothing; prints)."""
import pathlib, re, sys, collections

PALI = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters")
CH = [f"7-{i:02d}-anusayayamaka.md" for i in range(1, 12)]
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")
AN = re.compile(r"(kāmarāg|kāmārāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay(o|ena|aṃ|añca|ā)\b")
PERS = re.compile(r"\b(Anāgāmissa|Anāgāmī|Arahato|Arahā|Puthujjanassa|Puthujjano|Aṭṭhamakassa|Aṭṭhamako|"
                  r"Dvinnaṃ puggalānaṃ|Tiṇṇaṃ puggalānaṃ|Catunnaṃ puggalānaṃ|Pañcannaṃ puggalānaṃ|Dve puggalā|Tayo puggalā|Cattāro puggalā|Pañca puggalā|"
                  r"Tesaññeva puggalānaṃ|Tasseva puggalassa|Teva puggalā|Sveva puggalo)\b")
PLACE = re.compile(r"(Kāmadhātuyā|kāmadhātuyā) (dvīsu|tīsu) vedanāsu|(Dukkhāya|dukkhāya) vedanāya|(Rūpadhātuyā|rūpadhātuyā)|(Arūpadhātuyā|arūpadhātuyā)|(Apariyāpanne|apariyāpanne)|Sabbasakkāyapariyāpannesu dhammesu")


def norm(s):
    s = AN.sub(lambda m: "@" + m.group(2), s)
    s = PERS.sub("<P>", s)
    s = PLACE.sub("<L>", s)
    s = re.sub(r"(<L> )+<L>", "<LL>", s)
    s = re.sub(r"@(\w+)( ca)?(…pe…|\s)+(@\w+ ca ?)*", lambda m: m.group(0), s)
    s = re.sub(r"(@(\w+) ca ?)+(…pe… ?)?(@\w+ ca ?)*", lambda m: "{L" + m.group(2) + "} ", s)
    s = re.sub(r"(@(añca) \w+ ?)", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def sentences(line):
    return [x for x in re.split(r"(?<=[.?;])\s+(?=[A-ZĀĪŪṄÑṬḌṆa-zāīūṅñṭḍṇḷṃ(\"])", line) if x]


cnt = collections.Counter()
first = {}
for ch in CH:
    sid = None
    for ln in (PALI / ch).read_text(encoding="utf-8").splitlines():
        if not ln.strip():
            continue
        m = ID.search(ln)
        body = ID.sub("", ln).strip()
        if body.startswith("#"):
            k = "HEAD " + body
            cnt[k] += 1
            first.setdefault(k, ch)
            continue
        for s in sentences(body):
            k = norm(s)
            cnt[k] += 1
            first.setdefault(k, ch + " " + (m.group(1) if m else ""))
mode = sys.argv[1] if len(sys.argv) > 1 else "all"
for k, v in sorted(cnt.items(), key=lambda x: (first[x[0]], -x[1])):
    if mode == "all" or mode in k:
        print(f"{v:5d} {first[k][:9]} {k}")
print(len(cnt), "templates")
