import sys, importlib.util, pathlib
sys.dont_write_bytecode = True
H = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(H))
spec = importlib.util.spec_from_file_location("mk", H / "make_ch3-07-08-10.py")
mk = importlib.util.module_from_spec(spec); spec.loader.exec_module(mk)
mk.K.CUR["fix"] = True
for n in mk.NAMES:
    mk.translate(n)
out = []
out.append("### Every new string of the generator (NEW: terms, names, notes, headings, lines)")
for k, v in mk.NEW.items():
    out.append(f"- {k} = {v}")
out.append("### Dyad terms (pi-1 final, read with W(); the both-members slot «A၊ B N»)")
for d, tab in mk.DYADS_ADD.items():
    for k, v in tab.items():
        out.append(f"- {d}: {k} = {v}")
out.append("### Names of single hindrances / clingings (W() unless marked NEW above)")
for k, v in mk.NAMED.items():
    out.append(f"- {k}aṃ = {v}")
out.append("### Readings for the parser (in memory)")
for r in sorted(mk.READ_LOG):
    out.append("- " + r)
out.append("### Slips logged by the engine")
for r in sorted(mk.F.SLIPS):
    out.append("- " + r)
out.append(f"### Units through the fallback engine: {sum(mk.M.VIA_G.values())}")
print("\n".join(out))
