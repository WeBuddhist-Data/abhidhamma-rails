"""build notes-ch5-13-20.md from notes_head.md, the generator's tables and the run logs (scratch helper)"""
import sys, pathlib, importlib.util, re, collections, glob
sys.dont_write_bytecode = True
CH = pathlib.Path(__file__).resolve().parent
HERE = CH.parent
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("m", HERE / "make_ch5-13-20.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
head = (CH / "notes_head.md").read_text(encoding="utf-8")
head = head[:head.index("## Recurring sentences")]
out = [head.rstrip() + "\n"]
out.append("\n## Recurring sentences built by this script (placeholders, as Q's bare counts)\n")
for k, v in M.SENT.items():
    out.append(f"- {k} = {v}{M.END}\n")
out.append("- Loose fragments (engine LEX): " + "; ".join(f"«{k}» = «{v}»" for k, v in M.LEX_X.items()) + "\n")
out.append("\n## Notes composed by this group (Pāli as written = Burmese)\n")
for k, v in M.MY_NOTES.items():
    out.append(f"- {k} = {v}\n")
new, chains, negs = collections.OrderedDict(), collections.OrderedDict(), collections.OrderedDict()
used_atoms = set()
for f in sorted(glob.glob(str(CH / "new-5-*.txt"))):
    for l in open(f, encoding="utf-8"):
        t, rest = l.rstrip("\n").split("\t", 1)
        if t in ("N", "Q"):
            k, v = rest.split(" = ", 1)
            new.setdefault(k, v)
        elif t == "T":
            pal, my = rest.rsplit(" = ", 1)
            chains.setdefault(my, set()).update(pal.split(" | "))
        elif t == "NEG":
            k, v = rest.split(" = ", 1)
            negs.setdefault(k, v)
out.append("\n## New strings (headings, part names, note words, numbers): Pāli = Burmese\n")
for k, v in new.items():
    out.append(f"- {k} = {v}\n")
# negated atoms that occur in these chapters
txt = "\n".join((M.PALI / n).read_text(encoding="utf-8-sig") for n in M.NAMES)
out.append("\n## Paccanīya atoms «na-X» used in these chapters (Q's rule on the finished groups' X)\n")
for k, v in negs.items():
    if re.search(r"(?<![\wāīūṃṅñṭḍṇḷ])[" + k[0].upper() + k[0] + "]" + re.escape(k[1:]), txt):
        out.append(f"- {k}- = {v}\n")
out.append("\n## Term chains used (Pāli as written, one or more per Burmese)\n")
for my, pals in chains.items():
    ps = sorted(pals)
    out.append(f"- {' | '.join(ps[:3])}{' …' if len(ps) > 3 else ''} = {my}\n")
chk = (CH / "checks.md").read_text(encoding="utf-8") if (CH / "checks.md").exists() else "\n## Checks\n(pending)\n"
out.append("\n" + chk.strip() + "\n")
(HERE / "notes-ch5-13-20.md").write_text("".join(out), encoding="utf-8")
print("notes written", sum(len(x) for x in out))
