for k, v in X.NEW.items():
    print(f"- {k} = {v}")
print("--- notes (K.NOTE_FIXED additions)")
for k, v in X.NOTE_ADD.items():
    print(f"- ({k}) = ({v})")
print("--- NOTEP")
for k, v in X.NOTEP.items():
    print(f"- {k} = {v}")
print("--- headings")
for k, v in X.HL_ADD.items():
    print(f"- {k} = {v}")
print("--- SK/SKF")
for k, v in list(X.SK_ADD.items()) + list(X.SKF_ADD.items()):
    print(f"- {k} = {v}")
print("--- dyads")
for d, tab in X.DYADS.items():
    for k, v in tab.items():
        print(f"- {d}: {k} = {v}")
