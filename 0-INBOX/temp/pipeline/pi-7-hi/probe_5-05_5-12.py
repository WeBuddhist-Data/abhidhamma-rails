import re, sys, pathlib, collections
P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
FILES = ["5-05-paccaniya-dukatika.md", "5-06-paccaniya-tikaduka.md", "5-07-paccaniya-tikatika.md",
         "5-08-paccaniya-dukaduka.md", "5-09-anulomapaccaniya-tika.md", "5-10-anulomapaccaniya-duka.md",
         "5-11-anulomapaccaniya-dukatika.md", "5-12-anulomapaccaniya-tikaduka.md"]
heads = collections.Counter(); parens = collections.Counter(); expl = collections.Counter()
words = collections.Counter(); braces = []
for f in FILES:
    for line in (P / f).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        body = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", line)
        if line.startswith("#"):
            heads[body] += 1
            continue
        for m in re.finditer(r"\([^()]*\)", body):
            parens[m.group(0)] += 1
        for m in re.finditer(r"\{[^}]*\}", body):
            braces.append((f, m.group(0)))
        for m in re.finditer(r" – (.*?)(?=(?:\. [A-Z(])|…pe… [a-z]+[ṃ]? [a-z]*dhamm|\.$|\. \(|$)", body):
            expl[m.group(1)] += 1
        for w in re.findall(r"[^\s.,;…()–?{}\[\]]+", body):
            words[w.lower()] += 1
out = []
out.append("=== HEADINGS")
out += [f"{c}\t{h}" for h, c in sorted(heads.items())]
out.append("=== PARENS")
out += [f"{c}\t{h}" for h, c in sorted(parens.items())]
out.append("=== BRACES")
out += [f"{a}\t{b}" for a, b in braces]
out.append("=== EXPL")
out += [f"{c}\t{h}" for h, c in sorted(expl.items())]
out.append("=== WORDS")
out += [f"{c}\t{h}" for h, c in sorted(words.items())]
pathlib.Path(sys.argv[1]).write_text("\n".join(out), encoding="utf-8")
