import importlib.util, pathlib, sys
HERE = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails/0-INBOX/temp/pipeline/pi-7-my")
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("m5", HERE / "make_ch5-01-04.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for n in m.NAMES:
    m.translate(n)
out = []
out.append("## New strings (headings, names, note words, numbers)")
for k, v in m.NEW.items():
    out.append(f"- {k} = {v}")
out.append("\n## Notes composed by this group (Pāli as written = Burmese)")
for k, v in m.NOTE_MINE.items():
    out.append(f"- {k} = {v}")
out.append("\n## Paccanīya atoms «na-X» (the negation rule applied to the finished groups' X)")
for k, v in m.NEG_LOG.items():
    out.append(f"- {k}- = {v}")
out.append("\n## Term chains used (Pāli as written = Burmese of the one synthetic term)")
for my, k in m.KEYS.items():
    for p in sorted(m.KEY_PALI[k]):
        out.append(f"- {p} = {my}")
open(HERE / "chk-ch5-01-04/notes_tables.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len(m.NEW), len(m.NOTE_MINE), len(m.NEG_LOG), len(m.KEYS), sum(len(v) for v in m.KEY_PALI.values()))
print(sorted(set(m.SLIPS)))
