"""Move the pi-2 English working files onto the revised pi-2 root (new block IDs, no paragraph numbers).

usage: python -I -X utf8 reid_pi2_english.py [--write]
Old Pāli split: split-sync/backup-pre-sync/pi-2_split_chapters; new: AI_translation/pali/pi-2_split_chapters.
Non-empty lines align one to one (old Pāli = new Pāli = English). For each English line:
  - check its current ID equals the old Pāli line's ID (alignment check);
  - drop a leading "N. " when the old Pāli line starts with that same "N. ";
  - set the trailing ID to the new Pāli line's ID (add, replace, or remove);
  - blank lines follow the new Pāli split.
Files: the rails and zero-shot split folders, and the merged pi-2-english-plain.md (body aligned with the
whole old split in chapter order). Backup: split-sync/backup-pre-reid-en/. Nothing written unless every file passes.
"""
import pathlib, re, shutil, sys

B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
HERE = pathlib.Path(__file__).parent
OLD = HERE / "backup-pre-sync/pi-2_split_chapters"
NEW = B / "AI_translation/pali/pi-2_split_chapters"
EN = B / "AI_translation/english"
WRITE = "--write" in sys.argv
ID = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")
NUM = re.compile(r"^(\d+)\. ")


def rd(p):
    return p.read_text(encoding="utf-8").replace("\r\n", "\n")


def nonblank(t):
    return [l for l in t.split("\n") if l.strip()]


def blanks_after(t):
    """for each non-empty line: is it followed by a blank line before the next non-empty line?"""
    ls = t.rstrip("\n").split("\n")
    out, idx = [], [i for i, l in enumerate(ls) if l.strip()]
    for k, i in enumerate(idx):
        out.append(k + 1 < len(idx) and idx[k + 1] > i + 1)
    return out


def order(d):
    fs = [p for p in d.glob("*.md")]
    return sorted(fs, key=lambda p: -1 if p.stem == "preamble" else int(p.stem.split("-")[0]))


def segs(ls):
    out, buf = [], []
    for l in ls:
        buf.append(l)
        if ID.search(l):
            out.append(buf); buf = []
    if buf:
        out.append(buf)
    return out


def convert(en_lines, op, np, nb_new, label):
    """segment by segment (old IDs); line by line where the counts agree, else whole-segment fallback"""
    errs, stats = [], {"id_set": 0, "num_dropped": 0, "num_kept_missing": 0, "seg_fallback": 0}
    if len(op) != len(np):
        return None, [f"{label}: old/new Pāli line counts {len(op)} {len(np)}"], stats
    so, se = segs(op), segs(en_lines)
    if len(so) != len(se):
        return None, [f"{label}: segment counts old {len(so)} en {len(se)}"], stats
    text, k = "", 0
    for o_seg, e_seg in zip(so, se):
        n_seg, nb_seg = np[k:k + len(o_seg)], nb_new[k:k + len(o_seg)]
        k += len(o_seg)
        if len(o_seg) == len(e_seg):
            t, er = convert_lines(e_seg, o_seg, n_seg, nb_seg, label, stats)
        else:
            if any(ID.search(n) for n in n_seg[:-1]):
                errs.append(f"{label}: segment {o_seg[-1][-12:]} has {len(e_seg)} English lines for {len(o_seg)} Pāli lines and gains new IDs")
                continue
            stats["seg_fallback"] += 1
            # first/last lines carry the number and the ID; keep the English line breaks, no blank inside
            # a stand-in old/new Pāli per English line: number from the first Pāli line, ID from the last
            m = len(e_seg)
            o_std = [""] * m
            n_std = [""] * m
            o_std[-1], n_std[-1] = o_seg[-1], n_seg[-1]
            no = NUM.match(o_seg[0])
            if no:
                o_std[0] = no.group(0) + o_std[0]
            t, er = convert_lines(e_seg, o_std, n_std, [False] * m, label, stats)
            if nb_seg[-1]:
                t += "\n"
        errs += er
        text += t
    return text, errs, stats


def convert_lines(en_lines, op, np, nb_new, label, stats):
    errs, out = [], []
    for e, o, n in zip(en_lines, op, np):
        mo, me, mn = ID.search(o), ID.search(e), ID.search(n)
        if (mo and mo.group(1)) != (me and me.group(1)):
            errs.append(f"{label}: ID mismatch old {mo and mo.group(1)} en {me and me.group(1)}: {e[:60]}")
            continue
        body = e[:me.start()] if me else e.rstrip()
        no = NUM.match(o)
        if no and not NUM.match(n):
            if body.startswith(no.group(0)):
                body = body[len(no.group(0)):]
                stats["num_dropped"] += 1
            else:
                stats["num_kept_missing"] += 1
        new = body + (f" ^{mn.group(1)}" if mn else "")
        if (me and me.group(1)) != (mn and mn.group(1)):
            stats["id_set"] += 1
        out.append(new)
    text = ""
    for k, l in enumerate(out):
        text += l + "\n" + ("\n" if nb_new[k] else "")
    return text, errs


jobs, all_errs = [], []
old_files, new_files = order(OLD), order(NEW)
assert [p.name for p in old_files] == [p.name for p in new_files]
strip_prefix = lambda name: name if name == "preamble.md" else name.split("-", 1)[1]

for folder in ("pi-2-english-plain-rails_split_chapters", "pi-2-english-plain-zeroshot_split_chapters"):
    tot = {"id_set": 0, "num_dropped": 0, "num_kept_missing": 0}
    for po, pn in zip(old_files, new_files):
        pe = EN / folder / po.name
        if not pe.exists():
            pe = EN / folder / strip_prefix(po.name)
        if not pe.exists():
            all_errs.append(f"missing {pe}"); continue
        tn = rd(pn)
        text, errs, st = convert(nonblank(rd(pe)), nonblank(rd(po)), nonblank(tn), blanks_after(tn), f"{folder}/{pe.name}")
        all_errs += errs
        for k in tot: tot[k] += st[k]
        if text is not None and not errs:
            jobs.append((pe, text))
    print(folder, tot)

# merged file: frontmatter kept, body aligned with the whole split
pm = EN / "pi-2-english-plain.md"
tm = rd(pm)
m = re.match(r"(---\n.*?\n---\n)(.*)", tm, re.S)
fm, body = m.group(1), m.group(2)
op = [l for p in old_files for l in nonblank(rd(p))]
newt = "\n".join(rd(p).rstrip("\n") for p in new_files) + "\n"
np, nb = nonblank(newt), blanks_after(newt)
# chapter files are joined with a blank line between them in the merged file
text, errs, st = convert(nonblank(body), op, np, nb, "merged")
print("merged", st)
all_errs += errs
if text is not None and not errs:
    lead = "\n" if body.startswith("\n") else ""
    jobs.append((pm, fm + lead + text))

if all_errs:
    print("\n".join(all_errs[:30])); sys.exit(f"{len(all_errs)} problems, nothing written")
print("files ready:", len(jobs))
if WRITE:
    bak = HERE / "backup-pre-reid-en"
    for p, t in jobs:
        dst = bak / p.relative_to(EN)
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists():
            shutil.copy2(p, dst)
        p.write_text(t, encoding="utf-8", newline="\n")
    print("written; backup in", bak)
else:
    print("(dry run; add --write)")
