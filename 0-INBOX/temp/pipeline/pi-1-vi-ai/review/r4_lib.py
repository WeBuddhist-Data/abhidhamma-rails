import re, os, unicodedata
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
PI = os.path.join(ROOT, r'AI_translation\pali\pi-1_split_chapters')
VI = os.path.join(ROOT, r'AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters')
RU = os.path.join(ROOT, r'AI_translation\russian\pi-1-russian-plain-rails_split_chapters')
TS = os.path.join(ROOT, r'1-SOURCES\Translations\Vietnamese\vi-1-tinh_su.md')
EN = os.path.join(ROOT, r'3-TRANSFORMATIONS\Translations\en-Contemporary-English-Abhidhamma\en-dhammasangani-ai.md')
FILES = ['4-01-nikkhepakandam.md', '4-02-nikkhepakandam.md', '4-03-nikkhepakandam.md', '5-atthakathakandam.md']
IDRE = re.compile(r'\s\^([0-9A-Za-z-]+)\s*$')


def segs(path):
    """Return ordered list of (id, [lines]) by blank-line separated segments."""
    txt = open(path, encoding='utf-8').read()
    out = []
    for block in re.split(r'\n\s*\n', txt):
        lines = [l for l in block.split('\n') if l.strip()]
        if not lines:
            continue
        m = IDRE.search(lines[-1])
        sid = m.group(1) if m else None
        out.append((sid, lines))
    return out


def seg_dict(path):
    return {sid: lines for sid, lines in segs(path) if sid}


_ts = None


def ts_dict():
    """Tịnh Sự: id -> text (in memory only)."""
    global _ts
    if _ts is not None:
        return _ts
    d = {}
    buf = []
    for line in open(TS, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('![[') or not line.strip():
            if line.startswith('![['):
                buf = []
            continue
        if re.fullmatch(r'\s*[\d\s.,\-–]+\.?\s*', line):
            continue
        buf.append(line.strip())
        m = IDRE.search(line)
        if m:
            d.setdefault(m.group(1), ' '.join(buf))
            buf = []
    _ts = d
    return d


def strip_id(s):
    return IDRE.sub('', s)
