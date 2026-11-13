"""na-/no- items: for each Pāli negated item, count the Hindi forms found on the aligned lines."""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ar7_common as C

if "--bak" in sys.argv:
    C.CUR["hdir"] = C.BAK
T = [
    (r"\b[Nn]a ?pītisahagat", [r"उल्लास के साथ न होने वा", r"उल्लास के साथ होने वा\S+ न होने वा"]),
    (r"\b[Nn]a ?sukhasahagat", [r"सुख के साथ न होने वा", r"सुख के साथ होने वा\S+ न होने वा"]),
    (r"\b[Nn]a ?upekkhāsahagat", [r"समभाव के साथ न होने वा", r"समभाव के साथ होने वा\S+ न होने वा"]),
    (r"\b[Nn]a ?dassanena ?pahātabb(?!ahet)", [r"सत्य-दर्शन से न छोड़", r"सत्य-दर्शन से छोड़\S+ जाने वा\S+ न होने"]),
    (r"\b[Nn]a ?bhāvanāya ?pahātabb(?!ahet)", [r"मानसिक अभ्यास से न छोड़", r"मानसिक अभ्यास से छोड़\S+ जाने वा\S+ न होने"]),
    (r"\b[Nn]a ?dassanena ?pahātabbahetuk", [r"सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित", r"मूलों वा\S+ न होने"]),
    (r"\b[Nn]a ?kenaci ?viññeyy", [r"से न जानी जा सकने", r"जानी जा सकने वा\S+ न होने"]),
    (r"\b[Nn]ocittasahabh", [r"मन के साथ-साथ न होने", r"मन के साथ-साथ होने वा\S+ न होने"]),
    (r"\b[Nn]acittasahabh", [r"मन के साथ-साथ न होने", r"मन के साथ-साथ होने वा\S+ न होने"]),
    (r"\b[Nn]ocittānuparivatt", [r"मन का अनुसरण न करने", r"मन का अनुसरण करने वा\S+ न होने"]),
    (r"\b[Nn]acittānuparivatt", [r"मन का अनुसरण न करने", r"मन का अनुसरण करने वा\S+ न होने"]),
    (r"\b[Nn]oāsav[oaā]\b|\b[Nn]oāsavaṃ|\b[Nn]oāsavass", [r"मन के मैल रूपी न होने", r"मन का मैल न होने"]),
    (r"\b[Nn]aanuppann", [r"उत्पन्न न हु\S+ न होने", r"उत्पन्न हु\S+"]),
    (r"\b[Nn]aanāgat", [r"भविष्य की न होने", r"भविष्य क\S+ न होने"]),
]
for pr, hs in T:
    P = re.compile(pr)
    cnt = collections.Counter()
    files = collections.defaultdict(set)
    for part in C.PARTS:
        for p, h in C.pairs(part):
            if not P.search(p):
                continue
            cnt["_lines"] += 1
            for hr in hs:
                k = len(re.findall(hr, h))
                if k:
                    cnt[hr] += k
                    files[hr].add(part[:4])
    print(pr, dict(cnt), {k: " ".join(sorted(v)) for k, v in files.items()})
