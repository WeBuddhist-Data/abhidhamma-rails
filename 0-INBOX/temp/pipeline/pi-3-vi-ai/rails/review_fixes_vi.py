# Review fixes for the pi-3 Vietnamese rails (Dhātukathā), user decisions 2026-11-20 ("Apply as recommended").
# Brief: 0-INBOX\temp\pipeline\pi-3-vi-ai\vi-review-fixes-brief.md; findings: pi-3-vi-ai\review\findings-r1..r3.md.
#
# Input is ALWAYS the pre-review backup (rails\backup-pre-review\, created from the chapter folder on the first run),
# so the script is re-runnable and every rule's occurrence count is asserted against the unfixed text.
# Output: the 16 chapter files in AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters\ and the log
# rails\review-fixes-log.tsv (file, block id, decision, old, new).
#
# Usage:  python -I -X utf8 review_fixes_vi.py            (apply)
#         python -I -X utf8 review_fixes_vi.py --dry-run  (asserts + summary, writes nothing but the backup)
#         python -I -X utf8 review_fixes_vi.py --probe count|show|showpi|pi|grep|builders PATTERN...  (read-only)
import sys, re, os, shutil, unicodedata
from collections import Counter, defaultdict

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
VI = os.path.join(ROOT, r"AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters")
PI = os.path.join(ROOT, r"AI_translation\pali\pi-3_split_chapters")
RAILS = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-3-vi-ai\rails")
BACKUP = os.path.join(RAILS, "backup-pre-review")
LOG = os.path.join(RAILS, "review-fixes-log.tsv")
CH = ["preamble", "1-uddeso", "2-pathamanayo", "3-dutiyanayo", "4-tatiyanayo", "5-catutthanayo",
      "6-pancamanayo", "7-chatthanayo", "8-sattamanayo", "9-atthamanayo", "10-navamanayo",
      "11-dasamanayo", "12-ekadasamanayo", "13-dvadasamanayo", "14-terasamanayo", "15-cuddasamanayo"]
BUILDERS = ["build_rails_sample_vi.py"] + ["build_rails_%d_vi.py" % n for n in range(3, 16)]

# ---------------------------------------------------------------------------------------------------------------
# Expected occurrence counts (asserted; measured on the pre-review text and checked against the Pāli)
# ---------------------------------------------------------------------------------------------------------------
EXP_D4 = {"2-pathamanayo": 8, "4-tatiyanayo": 5, "5-catutthanayo": 4, "6-pancamanayo": 8, "7-chatthanayo": 6,
          "8-sattamanayo": 3, "10-navamanayo": 6, "11-dasamanayo": 6, "12-ekadasamanayo": 4,
          "13-dvadasamanayo": 6, "14-terasamanayo": 1, "15-cuddasamanayo": 6}          # = Pāli main-text «Xpaccayā Y»: 63
EXP_D2 = {"3-dutiyanayo": 18, "4-tatiyanayo": 66, "5-catutthanayo": 52, "6-pancamanayo": 196,
          "8-sattamanayo": 22, "9-atthamanayo": 5, "10-navamanayo": 64, "11-dasamanayo": 134,
          "12-ekadasamanayo": 48, "13-dvadasamanayo": 67, "14-terasamanayo": 107, "15-cuddasamanayo": 182}
EXP_D2_BARE = {"4-tatiyanayo": 5, "5-catutthanayo": 8, "10-navamanayo": 5}               # ^3-187, ^3-192, ^3-346
EXP_D2_TEHI = {"6-pancamanayo": 33}                                                       # ch6 «tehi dhammehi ye dhammā…pe…»
EXP_D1 = {"3-dutiyanayo": 8}                                                              # ^3-171 .. ^3-178
EXP_D3 = {"7-chatthanayo": 13, "8-sattamanayo": 7, "11-dasamanayo": 13}
THI_BLOCKS = {"7-chatthanayo": ["3-264", "3-265", "3-279", "3-286", "3-292", "3-299", "3-301"]}
COMMA_BLOCKS = {"9-atthamanayo": ["3-317", "3-318"], "13-dvadasamanayo": ["3-417", "3-447"],
                "15-cuddasamanayo": ["3-456", "3-457", "3-518"]}

# Decision 4: dependent-origination link names (pi-2 «“A làm điều kiện cho B”») -> «B do A làm điều kiện»
LINKS = [("vô minh", "các sự tạo tác"), ("các sự tạo tác", "thức"), ("thức", "phần tinh thần và vật chất"),
         ("phần tinh thần và vật chất", "sáu lĩnh vực nhận biết"), ("sáu lĩnh vực nhận biết", "sự tiếp xúc"),
         ("sự tiếp xúc", "cảm giác"), ("cảm giác", "khao khát"), ("khao khát", "sự bám víu")]

# Decision 6 (verse lines, title quotes): (chapter, block, old, new, decision label)
EXACT = [
    ("2-pathamanayo", "3-112", "bộ đôi của Phân tích các hiện tượng]",
     "bộ đôi của “Phân tích các hiện tượng”]", "6"),
    ("6-pancamanayo", "3-227",
     "Điều không hòa lẫn với nó, điều do nó sinh ra, điều cùng tồn tại với nó, điều vận hành theo nó;",
     "Điều không hòa lẫn với tâm, điều do tâm sinh ra, điều cùng tồn tại với tâm, điều vận hành theo tâm;", "6"),
    ("6-pancamanayo", "3-227",
     "Điều thuộc phần bên ngoài, điều phái sinh, cả hai; phạm vi [dị bản (Syā.): dvevīsati] của phương pháp này đã được hiểu rõ.",
     "Điều thuộc phần bên ngoài, điều phái sinh, cả hai; đó là phạm vi [dị bản (Syā.): dvevīsati]; phương pháp này đã được hiểu rõ.", "6"),
    # ^3-455 line 3 has the same Pāli words as ^3-227 line 3 (rails rule: same verse words = same Vietnamese)
    ("14-terasamanayo", "3-455",
     "Điều không hòa lẫn với nó, điều do nó sinh ra, điều cùng tồn tại với nó, điều vận hành theo nó, điều thuộc phần bên ngoài, điều phái sinh;",
     "Điều không hòa lẫn với tâm, điều do tâm sinh ra, điều cùng tồn tại với tâm, điều vận hành theo tâm, điều thuộc phần bên ngoài, điều phái sinh;", "6 (ext. of ^3-227 l.3)"),
    ("14-terasamanayo", "3-455",
     "Cả hai; phạm vi của phương pháp này đã được hiểu rõ.",
     "Cả hai; đó là phạm vi; phương pháp này đã được hiểu rõ.", "6"),
    ("10-navamanayo", "3-352",
     "Những điều này đã được gộp vào trong phần giải thích đề mục thứ chín.",
     "Những đề mục này được tập hợp trong phần giải thích đề mục thứ chín.", "6"),
    ("13-dvadasamanayo", "3-447",
     "Những điều này đã được gộp vào trong phần giải thích đề mục thứ chín.",
     "Những đề mục này được tập hợp trong phần giải thích đề mục thứ chín.", "6"),
]

PH_N = re.compile(r"(?P<lead>[Nn]hững hiện tượng nào )cùng với (?P<x>[^…\n]+?)…")
PH_B = re.compile(r"(?:(?<=… )|(?<=\n)|^)(?P<lead>[Cc])ùng với (?P<x>[^…\n]+?)…")
FULL = re.compile(r"[Nn]hững hiện tượng nào (?P<pre>không được gộp vào cùng với |được gộp vào cùng với "
                  r"|không gắn liền với |gắn liền với )")
FIRST_MOD = re.compile(r"[Nn]hững hiện tượng nào (?:không )?được gộp vào cùng với [^…?]+? theo cách gộp vào khối")
SUFFIX_INCL = " theo cách gộp vào khối"
D1 = re.compile(r"(không được gộp vào cùng với (?:nó|chúng) theo cách gộp vào lĩnh vực nhận biết) và "
                r"(theo cách gộp vào yếu tố)")
D3 = re.compile(r"mà (nó|chúng|những hiện tượng ấy) không gắn liền với, nhưng không gắn liền với")
D3_POS = re.compile(r"mà (nó|chúng|những hiện tượng ấy) gắn liền với, nhưng gắn liền với")
THI = re.compile(r"(?<=[^\W\d_]) gắn liền với (?=(?:một|hai|ba|bốn|năm) )")
COMMA = re.compile(r"(?<=[^\W\d_]) thì những hiện tượng ấy")
DO = re.compile(r"“([^”]*?) làm điều kiện cho ([^”]*?)”")


def block_id(block):
    m = re.search(r"\^(\S+)\s*$", block)
    return m.group(1) if m else "?"


def cap(s):
    return s[0].upper() + s[1:]


def low(s):
    return s[0].lower() + s[1:]


class Fixer:
    def __init__(self):
        self.log = []
        self.counts = defaultdict(Counter)    # chapter -> Counter(rule)

    def rec(self, ch, bid, dec, old, new):
        self.log.append((ch + ".md", bid, dec, old, new))

    # ---- decision 4 -------------------------------------------------------------------------------------------
    def d4(self, ch, bid, b):
        def rep(m):
            a, c = m.group(1), m.group(2)
            upper = a[0].isupper()
            assert (low(a), c) in LINKS, (ch, bid, m.group(0))
            if upper:   # only sentence-initial
                st = m.start()
                assert st == 0 or b[st - 2:st] == ". " or b[st - 1] == "\n", (ch, bid, m.group(0))
            new = "%s do %s làm điều kiện" % (c, low(a))
            new = cap(new) if upper else new
            self.rec(ch, bid, "4", m.group(0), new)
            self.counts[ch]["D4"] += 1
            return new
        return DO.sub(rep, b)

    # ---- decision 2 -------------------------------------------------------------------------------------------
    def d2(self, ch, bid, b):
        ms = [("N", m) for m in PH_N.finditer(b)] + [("B", m) for m in PH_B.finditer(b)]
        ms.sort(key=lambda t: t[1].start())
        if not ms:
            return b
        runs, cur = [], [ms[0]]
        for t in ms[1:]:
            gap = b[cur[-1][1].end():t[1].start()]
            if gap.strip() == "":
                cur.append(t)
            else:
                runs.append(cur)
                cur = [t]
        runs.append(cur)
        reps = []
        for run in runs:
            pos = run[-1][1].end()
            while pos < len(b) and b[pos] in " \n":
                pos += 1
            fm = FULL.match(b, pos)
            tehi = False
            if fm:
                pre = fm.group("pre")
                if "gộp vào" in pre:
                    assert FIRST_MOD.match(b, pos), (ch, bid, b[pos:pos + 200])
            else:
                # ch6: «tehi dhammehi ye dhammā…pe…» second clause, predicate = the first clause's (same Pāli frame)
                assert len(run) == 1 and run[0][0] == "N" and run[0][1].group("x") == "các hiện tượng đó", (ch, bid)
                st = run[0][1].start()
                assert b[st - 2:st] == "; ", (ch, bid)
                prev = [m for m in FULL.finditer(b, 0, st)]
                assert prev, (ch, bid)
                pre = prev[-1].group("pre")
                assert pre == "không được gộp vào cùng với ", (ch, bid, pre)
                tehi = True
            suffix = SUFFIX_INCL if "gộp vào" in pre else ""
            for kind, m in run:
                x = m.group("x")
                assert "theo cách" not in x and "cùng với" not in x, (ch, bid, x)
                lead = m.group("lead")
                if kind == "N":
                    head = lead
                    self.counts[ch]["D2"] += 1
                    if tehi:
                        self.counts[ch]["D2_tehi"] += 1
                else:
                    head = "Những hiện tượng nào " if lead == "C" else ""
                    self.counts[ch]["D2"] += 1
                    self.counts[ch]["D2_bare"] += 1
                new = head + pre + x + suffix + "…"
                reps.append((m.start(), m.end(), new))
                self.rec(ch, bid, "2", m.group(0), new)
        out, last = [], 0
        for s, e, new in reps:
            out.append(b[last:s])
            out.append(new)
            last = e
        out.append(b[last:])
        return "".join(out)

    # ---- decisions 1, 3 ---------------------------------------------------------------------------------------
    def d1(self, ch, bid, b):
        def rep(m):
            new = m.group(1) + " hay " + m.group(2)
            self.rec(ch, bid, "1", m.group(0), new)
            self.counts[ch]["D1"] += 1
            return new
        return D1.sub(rep, b)

    def d3(self, ch, bid, b):
        def rep(m):
            p = m.group(1)
            new = "mà %s không gắn liền; nhưng %s không gắn liền với" % (p, p)
            self.rec(ch, bid, "3", m.group(0), new)
            self.counts[ch]["D3"] += 1
            return new

        def rep_pos(m):
            p = m.group(1)
            new = "mà %s gắn liền; nhưng %s gắn liền với" % (p, p)
            self.rec(ch, bid, "3", m.group(0), new)
            self.counts[ch]["D3"] += 1
            return new
        b = D3.sub(rep, b)
        return D3_POS.sub(rep_pos, b)

    # ---- decision 6 -------------------------------------------------------------------------------------------
    def d6(self, ch, bid, b):
        if bid in THI_BLOCKS.get(ch, []):
            m = THI.search(b)
            assert m and m.start() < b.index("."), (ch, bid)
            old = b[max(0, m.start() - 25):m.end()]
            b = b[:m.start()] + " thì gắn liền với " + b[m.end():]
            self.rec(ch, bid, "6 (thì)", old, old[:-len(" gắn liền với ")] + " thì gắn liền với ")
            self.counts[ch]["D6_thi"] += 1
        if bid in COMMA_BLOCKS.get(ch, []):
            ms = list(COMMA.finditer(b))
            assert len(ms) == 1, (ch, bid, len(ms))
            m = ms[0]
            old = b[max(0, m.start() - 20):m.end()]
            b = b[:m.start()] + ", thì những hiện tượng ấy" + b[m.end():]
            self.rec(ch, bid, "6 (comma)", old, old[:-len(" thì những hiện tượng ấy")] + ", thì những hiện tượng ấy")
            self.counts[ch]["D6_comma"] += 1
        for c, blk, old, new, dec in EXACT:
            if c == ch and blk == bid:
                assert b.count(old) == 1, (ch, bid, old)
                b = b.replace(old, new)
                self.rec(ch, bid, dec, old, new)
                self.counts[ch]["D6_exact"] += 1
        return b


def check_after(ch, text):
    bad = {
        "placeholder «nào cùng với»": r"[Nn]hững hiện tượng nào cùng với ",
        "bare «cùng với X…»": r"(?:(?<=… )|(?<=\n)|^)[Cc]ùng với [^…\n]+…",
        "quoted link «làm điều kiện cho»": r"làm điều kiện cho",
        "dangling «gắn liền với,»": r"gắn liền với,",
        "negated «và» pair": r"không được gộp vào cùng với (?:nó|chúng) theo cách gộp vào lĩnh vực nhận biết và",
        "«duy trì tâm gắn liền»": r"duy trì tâm gắn liền",
        "«X thì những hiện tượng ấy»": r"[^\W\d_] thì những hiện tượng ấy",
        "em dash": "—", "en dash": "–", ":-": r":-", "….": r"…\.", "được được": r"được được", "là là": r"\blà là\b",
        "chánh niệm": "chánh niệm", "seed": r"(?i)seed", "double space": "  ", "CR": "\r",
        "double blank line": "\n\n\n",
    }
    probs = []
    for k, p in bad.items():
        n = len(re.findall(p, text))
        if n:
            probs.append("%s: %s=%d" % (ch, k, n))
    if not unicodedata.is_normalized("NFC", text):
        probs.append("%s: not NFC" % ch)
    return probs


def main(dry):
    os.makedirs(BACKUP, exist_ok=True)
    for ch in CH:
        dst = os.path.join(BACKUP, ch + ".md")
        if not os.path.exists(dst):
            shutil.copyfile(os.path.join(VI, ch + ".md"), dst)
    fx = Fixer()
    results, lines_changed = {}, {}
    for ch in CH:
        src = open(os.path.join(BACKUP, ch + ".md"), encoding="utf-8", newline="").read()
        blocks = src.split("\n\n")
        out = []
        for b in blocks:
            bid = block_id(b)
            b2 = fx.d4(ch, bid, b)
            b2 = fx.d2(ch, bid, b2)
            b2 = fx.d1(ch, bid, b2)
            b2 = fx.d3(ch, bid, b2)
            b2 = fx.d6(ch, bid, b2)
            out.append(b2)
        new = "\n\n".join(out)
        ol, nl = src.split("\n"), new.split("\n")
        assert len(ol) == len(nl), ch
        assert re.findall(r"\^\S+", src) == re.findall(r"\^\S+", new), ch
        lines_changed[ch] = sum(1 for a, c in zip(ol, nl) if a != c)
        results[ch] = new
    # count assertions
    def chk(rule, exp):
        for ch in CH:
            got = fx.counts[ch][rule]
            assert got == exp.get(ch, 0), (rule, ch, got, exp.get(ch, 0))
    chk("D4", EXP_D4); chk("D2", EXP_D2); chk("D2_bare", EXP_D2_BARE); chk("D2_tehi", EXP_D2_TEHI)
    chk("D1", EXP_D1); chk("D3", EXP_D3)
    chk("D6_thi", {k: len(v) for k, v in THI_BLOCKS.items()})
    chk("D6_comma", {k: len(v) for k, v in COMMA_BLOCKS.items()})
    exact = Counter(c for c, *_ in EXACT)
    chk("D6_exact", exact)
    probs = []
    for ch in CH:
        probs += check_after(ch, results[ch])
    for p in probs:
        print("POST-CHECK:", p)
    assert not probs
    if not dry:
        for ch in CH:
            with open(os.path.join(VI, ch + ".md"), "w", encoding="utf-8", newline="") as f:
                f.write(results[ch])
        with open(LOG, "w", encoding="utf-8", newline="\n") as f:
            f.write("file\tblock\tdecision\told\tnew\n")
            for row in fx.log:
                f.write("\t".join(s.replace("\t", " ").replace("\n", " / ") for s in row) + "\n")
    rules = ["D1", "D2", "D2_bare", "D2_tehi", "D3", "D4", "D6_thi", "D6_comma", "D6_exact"]
    print("%-18s %6s " % ("chapter", "lines") + " ".join("%8s" % r for r in rules))
    tot = Counter()
    for ch in CH:
        print("%-18s %6d " % (ch, lines_changed[ch]) + " ".join("%8d" % fx.counts[ch][r] for r in rules))
        tot.update(fx.counts[ch])
        tot["lines"] += lines_changed[ch]
    print("%-18s %6d " % ("TOTAL", tot["lines"]) + " ".join("%8d" % tot[r] for r in rules))
    print("log rows:", len(fx.log), "(dry run, nothing written)" if dry else "-> " + LOG)


# ---------------------------------------------------------------------------------------------------------------
# read-only probe used while preparing the rules
# ---------------------------------------------------------------------------------------------------------------
def segs(path):
    txt = open(path, encoding="utf-8").read()
    out = []
    for block in txt.split("\n\n"):
        block = block.strip("\n")
        if block:
            out.append((block_id(block), block))
    return out


def probe(mode, pats):
    if mode == "builders":
        for b in BUILDERS:
            for i, line in enumerate(open(os.path.join(RAILS, b), encoding="utf-8"), 1):
                if all(re.search(p, line) for p in pats):
                    print("%s:%d: %s" % (b, i, line.rstrip()[:220]))
        return
    for ch in CH:
        vs = segs(os.path.join(VI, ch + ".md"))
        ps = dict(segs(os.path.join(PI, ch + ".md")))
        if mode == "count":
            txt = open(os.path.join(VI, ch + ".md"), encoding="utf-8").read()
            print(ch, [len(re.findall(p, txt)) for p in pats])
        elif mode in ("show", "showpi"):
            for bid, b in vs:
                if all(re.search(p, b) for p in pats):
                    print("=====", ch, bid)
                    if mode == "showpi":
                        print("PI:", ps.get(bid, ""))
                    print("VI:", b)
        elif mode == "grep":
            txt = open(os.path.join(VI if pats[1] == "vi" else PI, ch + ".md"), encoding="utf-8").read()
            for k, v in sorted(Counter(re.findall(pats[0], txt)).items()):
                print(ch, v, "|", k)
        elif mode == "pi":
            for bid, b in ps.items():
                if all(re.search(p, b) for p in pats):
                    print("=====", ch, bid)
                    print("PI:", b)
                    print("VI:", dict(vs).get(bid, ""))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--probe":
        probe(sys.argv[2], sys.argv[3:])
    else:
        main(dry="--dry-run" in sys.argv)
