"""phase 3 edit 2 of map5_rules.py: tuples in the tables, the Mapper with S1 / S3 / G1-G3 book-wide."""
import pathlib
p = pathlib.Path(__file__).resolve().parent.parent / "map5_rules.py"
s = p.read_text(encoding="utf-8")


def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:80])
    s = s.replace(old, new)


rep('''# ---- FUNCS-END
''', '''# ---- FUNCS-END


def alt_name(vals):
    """the FUNCS name of a tuple value («@alt:a|b|…»), registered on first use."""
    name = "alt:" + "|".join(vals)
    FUNCS.setdefault(name, alt(*vals))
    return "@" + name


for _tab in (FRAME, STOCK):          # the tuples of the module tables (phase 3) as «@alt:…» values
    for _k, _v in list(_tab.items()):
        if isinstance(_v, tuple):
            _tab[_k] = alt_name(_v)
''')

rep('''class Mapper:
    """chapter_tables: {ch: {kw: value}}; ctx: {sid: {kw: value}}; a value «@name» calls FUNCS[name] (or the
    mapper's own funcs). SRC[(sid, kw)] records where each value came from."""

    def __init__(self, chapter_tables=None, ctx=None, funcs=None, shared=None):
        self.tables = chapter_tables or {}
        self.ctx = ctx or {}
        self.funcs = dict(FUNCS)
        self.funcs.update(funcs or {})''', '''NEG_WORDS = ("na", "no")


def internal_neg(kw):
    """a multiword keyword with na / no after its first word («anāgāmī na parihāyati», «Na parihāyati anāgāmī» is
    initial and goes through compose)."""
    ws = [low(w) for w in kw.split()]
    return len(ws) > 1 and ws[0] not in NEG_WORDS + ("neva",) and any(w in NEG_WORDS for w in ws[1:])


def make_stem(tables):
    """S1 (phase 2 ch2-15, approved after the phase-3 review): the stem fallback over the pi-1 … pi-4 values and the
    given tables: a single keyword that nothing else maps takes the value of a keyword of the same stem (the longest
    common beginning, at least the keyword less four letters, length within five) that the segment's Burmese has as a
    phrase, most frequent first (a table value counts 50)."""
    pool = collections.defaultdict(collections.Counter)
    for t in PRIOR_ORDER:
        for k, c in prior()[t].items():
            pool[k].update(c)
    for tab in tables:
        for k, v in tab.items():
            for x in (v if isinstance(v, tuple) else (v,)):
                if not x.startswith("@") and x != NONE:
                    pool[low(k)][x] += 50
    keys = sorted(k for k in pool if " " not in k)

    def stem(kw, my):
        k = low(kw)
        for n in range(len(k), max(4, len(k) - 4) - 1, -1):
            pre = k[:n]
            c = collections.Counter()
            for kk in keys:
                if kk.startswith(pre) and abs(len(kk) - len(k)) <= 5:
                    c.update(pool[kk])
            for v, _ in c.most_common():
                if presence(v, my)[0] and phrase_ok(v, my):
                    return v
        return None
    stem.pool = pool
    return stem


class Mapper:
    """chapter_tables: {ch: {kw: value}}; ctx: {sid: {kw: value}}; a value «@name» calls FUNCS[name] (or the
    mapper's own funcs); a tuple value = alt(). stem: a make_stem() function (S1) for single keywords nothing else
    maps. SRC[(sid, kw)] records where each value came from.

    lookup(): CTX / table entry first; a negative inside a multiword keyword (S3 / G3) = negate(the rest); else the
    chain (_chain); a single keyword the chain cannot map = the stem fallback (S1); two members joined by compose =
    pali_order (G1 / G2)."""

    def __init__(self, chapter_tables=None, ctx=None, funcs=None, shared=None, stem=None):
        self.tables = {ch: {k: (alt_name(v) if isinstance(v, tuple) else v) for k, v in tab.items()}
                       for ch, tab in (chapter_tables or {}).items()}
        self.ctx = {sid: {k: (alt_name(v) if isinstance(v, tuple) else v) for k, v in tab.items()}
                    for sid, tab in (ctx or {}).items()}
        self.stem = stem
        self.funcs = dict(FUNCS)
        self.funcs.update(funcs or {})''')

rep('''    def lookup(self, ch, sid, kw, pali, my):
        v = table_get(self.ctx.get(sid, {}), kw)''', '''    def lookup(self, ch, sid, kw, pali, my):
        ws = kw.split()
        if internal_neg(kw) and table_get(self.ctx.get(sid, {}), kw) is None \\
                and table_get(self.tables.get(ch, {}), kw) is None:
            rest = " ".join(w for w in ws if low(w) not in NEG_WORDS)
            v = negate(self.lookup(ch, sid, rest, pali, my), my)
            self.SRC[(sid, kw)] = "neg"
            return v
        try:
            v = self._chain(ch, sid, kw, pali, my)
        except KeyError:
            if " " in kw or self.stem is None:
                raise
            v = self.stem(kw, my)
            if v is None:
                raise
            self.SRC[(sid, kw)] = "stem"
            return v
        if len(ws) == 2 and self.SRC.get((sid, kw)) == "compose" and v != NONE:
            v = self.pali_order(ch, sid, ws, v, pali, my)
        return v

    def pali_order(self, ch, sid, ws, v, pali, my):
        """two members joined by compose (phase 2 G1 / G2, book-wide): (G1) the «ပင်» of eva / va between them is not
        part of the keyword (as Q4: « … »); (G2) where the text has the members in the Pāli order too, that order (an
        adjacent pair in the other order with no particle between them may be a neighbouring phrase); an adjacency
        with a particle is the text's own construction and stays («ဆိုးသော လားရာကို ပယ်ပြီးသော»)."""
        try:
            x, y = (self._chain(ch, sid, w, pali, my) for w in ws)
        except KeyError:
            return v
        if NONE in (x, y) or is_verb(x) or is_verb(y) or x == y:
            return v
        for g in ("ပင် ", "သည်ပင် ", "၏ပင် ", "ကိုပင် "):
            if v in (x + g + y, y + g + x):
                v = (x + " … " + y) if v.startswith(x) else (y + " … " + x)
        g_rev = glue(y, x, my)
        glued = g_rev is not None and g_rev.strip() and v == y + g_rev + x
        if v.startswith(y) and v.endswith(x) and len(v) > len(y) + len(x) - 1 and not glued:
            px, py = occurrences(x, my), occurrences(y, my)
            if px and py and min(px) < max(py):
                g = glue(x, y, my)
                return x + (g.replace("\\0", "") if g is not None else " … ") + y
        return v

    def _chain(self, ch, sid, kw, pali, my):
        v = table_get(self.ctx.get(sid, {}), kw)''')
p.write_text(s, encoding="utf-8")
print("ok")
