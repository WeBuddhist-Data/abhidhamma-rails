"""Convert a Vietnamese Tịnh Sự Abhidhamma PDF (Word export) to plain markdown (no block IDs).

Usage: convert_vi.py <pdf> <out.md> <diagnostics.txt> [--keep-footnotes] [--start-page N]

Formatting only: title page, table of contents, running headers and page numbers are dropped;
wrapped lines are re-joined into paragraphs; headings are marked; bullet glyphs become list
items. Translator footnotes are dropped (user decision 2026-11-17: the Vietnamese is a
verification reference only), both the note text at the foot of the page and the marker digits
glued to the word they annotate; --keep-footnotes keeps them (for the raw copy).
"""
import re
import sys
import unicodedata

import pypdf

sys.stdout.reconfigure(encoding="utf-8")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
pdf_path, out_path, diag_path = args[:3]
KEEP_FN = "--keep-footnotes" in sys.argv
START = None
if "--start-page" in sys.argv:
    START = int(sys.argv[sys.argv.index("--start-page") + 1])
    args = [a for a in args if a != str(START)]
reader = pypdf.PdfReader(pdf_path)
pages = [(p.extract_text() or "") for p in reader.pages]
diag = {"pages": len(pages)}


def bump(key, n=1):
    diag[key] = diag.get(key, 0) + n


# ---------------------------------------------------------------- syllable repair
def base(ch):
    return unicodedata.normalize("NFD", ch)[0].lower()


VOWELS = set("aeiouy")


def vi_fix_syllables(s):
    """Re-join syllables split by the extractor ("x ứ" -> "xứ"): a vowel-less letter run of
    1-3 characters can never be a Vietnamese syllable on its own."""
    toks = s.split(" ")
    res, i = [], 0
    while i < len(toks):
        t = toks[i]
        if (i + 1 < len(toks) and 1 <= len(t) <= 3 and t.isalpha() and all(base(c) not in VOWELS for c in t)
                and toks[i + 1][:1].isalpha() and toks[i + 1][:1].islower() and base(toks[i + 1][0]) in VOWELS):
            res.append(t + toks[i + 1])
            bump("split_syllables_rejoined")
            i += 2
            continue
        res.append(t)
        i += 1
    return " ".join(res)


# ---------------------------------------------------------------- page cleaning
HEADER = re.compile(r"^\s*(\d+\s+)?(Việt [dD]ịch|Tạng Vô Tỷ Pháp|Tạng Diệu Pháp)|^\s*\d+\s*$")
MARKER = re.compile(r"(?<=[^\W\d_\s])(\d{1,2})(?=[\s,.;:!?)\]\"”']|$)")
fn_next = [1]  # number of the next translator footnote


def clean_page(text):
    ls = text.splitlines()
    while ls and not ls[0].strip():
        ls = ls[1:]
    # running header (and a page number on its own line) at the top
    while ls and HEADER.match(ls[0]):
        ls = ls[1:]
        bump("page_headers_removed")
    if KEEP_FN:
        return ls
    # footnotes: markers glued to a word in the body, notes "N text" at the foot of the page
    marks = set()
    for ln in ls:
        for m in MARKER.finditer(ln):
            marks.add(m.group(1))
    # footnotes are numbered in sequence through the book: the next number is a note too,
    # even when its marker is not glued to a word on this page
    marks.add(str(fn_next[0]))
    cut = None
    for k in range(len(ls) - 1, max(-1, len(ls) - 15), -1):
        m = re.match(r"^\s*(\d{1,2})\s+[^\W\d_]", ls[k])
        if m and m.group(1) in marks and (k == 0 or not ls[k - 1].strip() or k > len(ls) - 6):
            cut = k
    if cut is not None:
        nums = [int(x) for x in re.findall(r"(?:^|\s)(\d{1,2})\s+[^\W\d_]", " ".join(ls[cut:]))]
        fn_next[0] = max([fn_next[0] - 1] + [n for n in nums if n < fn_next[0] + 5]) + 1
        bump("footnote_lines_removed", len(ls) - cut)
        ls = ls[:cut]
    out = []
    for ln in ls:
        new, n = MARKER.subn("", ln)
        bump("footnote_markers_removed", n)
        out.append(new)
    return out


# ---------------------------------------------------------------- structure
VI_HEAD = [
    (re.compile(r"^Phần [A-Z]\.", re.I), 2),
    (re.compile(r"^[IVX]+\.\s"), 3),
    (re.compile(r"^\d+\.\d+\)\s"), 5),
    (re.compile(r"^\d+\)\s"), 4),
    (re.compile(r"^[a-zđ]\)\s"), 6),
]
NUM_LINE = re.compile(r"^\d{1,4}\.?$")  # the source occasionally drops the dot (e.g. "806")


def vi_heading_level(s):
    for rx, lvl in VI_HEAD:
        if rx.match(s):
            return lvl
    return None


def convert():
    start = START if START is not None else next(i for i, t in enumerate(pages) if "NAMO TASSA" in t.upper())
    diag["front_pages_skipped"] = start
    lines = []
    for text in pages[start:]:
        lines.extend(clean_page(text))
        lines.append("\x00PAGE")  # page boundary: never a paragraph break by itself

    out, para, pending_num = [], None, None

    def flush():
        nonlocal para
        if para is not None:
            out.append(para)
            para = None

    def nxt_meaningful(i):
        for j in range(i + 1, len(lines)):
            if lines[j] != "\x00PAGE" and lines[j].strip():
                return lines[j].strip()
        return ""

    for i, raw in enumerate(lines):
        if raw == "\x00PAGE":
            continue
        s = raw.strip()
        if not s:
            flush()
            continue
        bullet = 0xE000 <= ord(s[0]) <= 0xF8FF or (s[0] in "•▪●-–" and not re.fullmatch(r"[-~–]+", s))
        body = vi_fix_syllables(re.sub(r"\s+", " ", s[1:].strip() if bullet else s))
        if re.fullmatch(r"[-~]{2,}", s):
            flush()
            out.append(("hr",))
            continue
        if NUM_LINE.match(s):
            flush()
            pending_num = s
            continue
        if bullet:
            flush()
            if pending_num:
                out.append(("p", pending_num))
                pending_num = None
            para = ("li", body)
            bump("list_items")
            continue
        lvl = vi_heading_level(s)
        starts_block = para is None
        if lvl is None and starts_block and len(s) < 70 and not s.startswith("Dứt") and not re.search(r"[.?!:,;]$", s):
            n = nxt_meaningful(i)
            if NUM_LINE.match(n) or vi_heading_level(n):
                lvl = 4
        if lvl and starts_block and len(s) < 90 and pending_num is None:
            out.append(("h", lvl, body))
            bump("headings")
            continue
        if s.startswith("Dứt "):
            flush()
            out.append(("p", body))
            continue
        if para is None:
            text = f"{pending_num} {body}" if pending_num else body
            pending_num = None
            para = ("p", text)
        else:
            para = (para[0], para[1] + " " + body)
            bump("line_joins")
    flush()
    if pending_num:
        out.append(("p", pending_num))
    return out


def render(blocks):
    md = []
    for b in blocks:
        if b[0] == "h":
            md.append("#" * b[1] + " " + b[2])
        elif b[0] == "p":
            md.append(b[1])
        elif b[0] == "li":
            if md and md[-1].startswith("- "):
                md[-1] += "\n- " + b[1]
                continue
            md.append("- " + b[1])
        elif b[0] == "hr":
            md.append("---")
    return "\n\n".join(md) + "\n"


body = render(convert())
open(out_path, "w", encoding="utf-8", newline="\n").write(body)
diag["output_chars"] = len(body)
open(diag_path, "w", encoding="utf-8").write("".join(f"{k}: {v}\n" for k, v in diag.items()))
print(diag)
