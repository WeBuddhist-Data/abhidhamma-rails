import re, os, unicodedata
from collections import OrderedDict, defaultdict, Counter

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-6_split_chapters")
VDIR = os.path.join(ROOT, r"AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters")
FILES = ["10-%02d-indriyayamaka.md" % n for n in range(3, 14)]

IDRE = re.compile(r"\s*\^([0-9a-z-]+)\s*$")

def lines(path):
    with open(path, encoding="utf-8") as f:
        t = f.read()
    return [l for l in t.split("\n") if l.strip()]

def pairs(files=FILES):
    out = []
    for fn in files:
        P = lines(os.path.join(PDIR, fn)); V = lines(os.path.join(VDIR, fn))
        if len(P) != len(V):
            print("LINECOUNT", fn, len(P), len(V))
        cur = None
        # find segment ids: id at end of last line of a segment
        ids = [None] * len(P)
        nxt = None
        for i in range(len(P) - 1, -1, -1):
            m = IDRE.search(P[i])
            if m: nxt = m.group(1)
            ids[i] = nxt
        for i in range(min(len(P), len(V))):
            out.append((fn, i + 1, ids[i], P[i], V[i]))
    return out

# Pali indriya stems -> key
PSTEM = [
    ("anaññātaññassāmīt", "ANN"), ("aññātāv", "AV"), ("aññ", "AÑ"),
    ("cakkh", "cak"), ("sot", "sot"), ("ghān", "gha"), ("jivh", "jiv"), ("kāy", "kay"),
    ("itth", "itt"), ("puris", "pur"), ("jīvit", "jiv2"), ("somanass", "som"),
    ("domanass", "dom"), ("upekkh", "upe"), ("sukh", "suk"), ("dukkh", "duk"),
    ("saddh", "sad"), ("vīriy", "vir"), ("viriy", "vir"), ("sat", "sati"), ("samādh", "sam"),
    ("paññ", "pañ"), ("man", "man"),
]
VNAME = [
    ("năng lực của người đã hiểu biết trọn vẹn", "AV"),
    ("năng lực biết được điều chưa từng biết", "ANN"),
    ("năng lực hiểu biết trọn vẹn", "AÑ"),
    ("năng lực mắt", "cak"), ("năng lực tai", "sot"), ("năng lực mũi", "gha"),
    ("năng lực lưỡi", "jiv"), ("năng lực thân", "kay"), ("năng lực ý", "man"),
    ("năng lực nữ tính", "itt"), ("năng lực nam tính", "pur"), ("năng lực sống", "jiv2"),
    ("năng lực dễ chịu", "suk"), ("năng lực khó chịu", "duk"), ("năng lực niềm vui", "som"),
    ("năng lực nỗi buồn", "dom"), ("năng lực bình thản", "upe"), ("năng lực niềm tin", "sad"),
    ("năng lực tinh tấn", "vir"), ("năng lực tỉnh thức", "sati"), ("năng lực định tâm", "sam"),
    ("năng lực trí tuệ", "pañ"),
]
PIND = re.compile(r"\b(\w+?)(?:u?ndriy|indriy)(\w*)")
PADJ = re.compile(r"\b([SsAa]a?)(cakkhuk|sotak|ghānak)(\w+)")
VADJ = re.compile(r"(?<![\w])(mắt|tai|mũi)(?![\w])")
BMAP = {"cakkhuk": "cak", "sotak": "sot", "ghānak": "gha", "mắt": "cak", "tai": "sot", "mũi": "gha"}

def pstem(s):
    for pre, k in PSTEM:
        if s.startswith(pre) or s.lower().startswith(pre):
            return k
    return "?" + s

def norm_p(s):
    toks = []
    def ind(m):
        k = pstem(m.group(1)); toks.append(k)
        return "<I:%s>%s" % (k, m.group(2))
    s = PIND.sub(ind, s)
    def adj(m):
        pre = m.group(1)
        neg = pre.lower() == "a"
        k = BMAP[m.group(2)]; toks.append(k)
        return ("a" if neg else "sa") + "<B:%s>" % k + m.group(3)
    s = PADJ.sub(adj, s)
    return s, toks

def norm_v(s):
    for name, k in VNAME:
        s = s.replace(name, "<I:%s>" % k)
        s = s.replace(name[0].upper() + name[1:], "<I:%s>" % k)
    s = VADJ.sub(lambda m: "<B:%s>" % BMAP[m.group(1)], s)
    return s

TOK = re.compile(r"<([IB]):([^>]+)>")

def lettered(s, order):
    return TOK.sub(lambda m: "<%s%s>" % (m.group(1), order.get(m.group(2), "?" + m.group(2))), s)

def order_of(s):
    o = OrderedDict()
    for m in TOK.finditer(s):
        if m.group(2) not in o:
            o[m.group(2)] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[len(o)]
    return o

BR = re.compile(r"\[[^\]]*\]")
SPLIT = re.compile(r"(?<=[.?])\s+")

def sentences(s):
    s = IDRE.sub("", s)
    s = BR.sub("[VAR]", s)
    return [x for x in SPLIT.split(s.strip()) if x]
