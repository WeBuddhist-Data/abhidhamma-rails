import pathlib, re, sys
H = '''# consistency pass (harmonise-notes.md): forms changed on purpose against pi-1 / pi-2 / pi-3 (no longer reuse items)
HARMONISED = [(r"\\b[Tt]athāgat", F.TATHAGATA, "B4: tathāgata its own word (pi-2 «မြတ်စွာဘုရား» kept for bhagavā)")]
n_h = s_h = 0
for rx, my, why in HARMONISED:
    n_h += 1
    occ = [(p, m) for p, m in PI4 if re.search(rx, p)]
    miss = [p[:70] for p, m in occ if my not in m]
    if occ and not miss:
        s_h += 1
    else:
        bad.append(f"H «{rx}» / «{my}» ({why}): {len(occ)} lines, missing in {miss[:2]}")
print(f"H. harmonised forms (changed on purpose in the consistency pass): {s_h} / {n_h}")
'''
def patch(fn, removes, anchor):
    p = pathlib.Path(fn); s = p.read_text(encoding="utf-8")
    for a, b in removes:
        assert s.count(a) == 1, (fn, a); s = s.replace(a, b)
    i = s.index(anchor); s = s[:i] + H + s[i:]
    p.write_text(s, encoding="utf-8")
patch("check_ch3-4.py",
      [('    (r"\\bTathāgatappaveditā", "tathāgato", "မြတ်စွာဘုရား"), (r"\\btathāgatassa sāvakā", "tathāgato", "မြတ်စွာဘုရား"),\n', ''),
       ('"pubbakālaṃ kodho, aparakālaṃ upanāho.": "^4-66 joined with the next sentence (no full stop in the pi-4 Pāli)",',
        '"pubbakālaṃ kodho, aparakālaṃ upanāho.": "pi-4 Pāli without the comma (and ^4-66 without the full stop): «ဖြစ်၍» (harmonise A2)",'),
       ('\'"Mā maṃ jaññā"ti saṅkappeti\': "pi-4 spelling saṅkappati (same verb)",',
        '\'"Mā maṃ jaññā"ti saṅkappeti\': "pi-4 spelling saṅkappati (same verb); ^4-52 no comma after it: «ကြံစည်၍» (harmonise A2)",')],
      "tot_s, tot_n = s_c1 + s_c2 + s_c3, n_c1 + n_c2 + n_c3\n")
