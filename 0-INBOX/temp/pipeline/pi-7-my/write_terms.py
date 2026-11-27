"""Write my7-zeroshot-terms.md from my7_formulas (and the sample's make_sample tables): «Pāli = Burmese».

Called by make_sample.py --terms. Every value is computed by the module's own functions, never retyped.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent


def write(F, S):
    L = ["# pi-7 Burmese zero-shot: formulas and key terms («Pāli = Burmese»)", "",
         "Written by `make_sample.py --terms` from `my7_formulas.py` (import the module; do not retype). "
         "«(pi-N ^id)» = the FINAL rails segment the value was read from and checked against at import (W()); "
         "NEW = proposed in this sample. Binding style: `0-INBOX/temp/pipeline/burmese-style.md`.", ""]

    def src(pali):
        w = F.WITNESS.get(pali)
        return f" (pi-{w[0]} {w[1]})" if w else " (NEW)"

    L += ["## 1. Book title and frame", "",
          f"- Paṭṭhānapāḷi (book title, Burmese only) = {F.TITLE} (NEW: \"how causes and results connect\")",
          f"- Namo tassa bhagavato arahato sammāsambuddhassa = {F.NAMO}{src('Namo tassa bhagavato arahato sammāsambuddhassa')}",
          f"- Abhidhammapiṭake = {F.ABHI}{src('Abhidhammapiṭake')}",
          f"- X niṭṭhitaṃ. = {F.finished('X')}{src('Khandhavibhaṅgo niṭṭhito')}",
          f"- …pe… / …Pe… = {F.PE}; «.» = «{F.END}»; «,» «;» = «{F.C}»; «–» kept only where the Pāli has it",
          f"- variants «{{reading (syā.)}}» = «{F.variant('reading (syā.)')}»; spelling only = "
          f"«{F.VAR_OPEN}{F.VAR_L} (Ka.): …{F.VAR_CLOSE}» (braces kept: see notes-sample.md)", ""]
    L += ["## 2. Headings and colophons", ""]
    for k, v in F.HEAD.items():
        L.append(f"- {k} = {v}")
    for k, v in F.TIKA_NAME.items():
        L.append(f"- {k} = {v}")
    for k, v in F.GROUP.items():
        L.append(f"- {k}(ṃ) (counting group) = {v}")
    L += [f"- X-padaṃ = «X {F.PADA}» -> Kusalābyākatapadaṃ = {F.heading('Kusalābyākatapadaṃ')}",
          f"- Xpaccayo (heading) = {F.heading('Hetupaccayo')}; Naxpaccayo = {F.heading('Nahetupaccayo')}",
          f"- Xpaccayādi = {F.heading('Ārammaṇapaccayādi')}; X-Ypaccayā = {F.heading('Napacchājāta-naāsevanapaccayā')}",
          f"- Xsabhāgaṃ = {F.heading('Hetusabhāgaṃ')}; Xādisabhāgaṃ = {F.heading('Sahajātādisabhāgaṃ')}",
          f"- Xmūlakaṃ = {F.heading('Hetumūlakaṃ')}; Xmūlakādi = {F.heading('Ārammaṇamūlakādi')}",
          f"- Xghaṭanā = {F.heading('Sahajātaghaṭanā')}; Xdukaṃ = {F.heading('Nahetudukaṃ')}; "
          f"Xādidukāni = {F.heading('Napacchājātādidukāni')}",
          f"- (saupanissayaṃ) = ({F.PAREN['saupanissayaṃ']}); (sakammaṃ) = ({F.PAREN['sakammaṃ']})"]
    for k, v in S.COLO.items():
        L.append(f"- {k} = {v}")
    L.append("")
    L += ["## 3. The 24 conditions in each case", "",
          "| Pāli | name (Xpaccayo) | Xpaccayā | naXpaccayā | counting Xe / Xyā | naXe | Xpaccayena paccayo |",
          "|---|---|---|---|---|---|---|"]
    for st in F.STEMS:
        L.append(f"| {st} | {F.cond(st, 'n')} | {F.cond(st, 'ab')} | {F.cond(st, 'ab', True)} | "
                 f"{F.cond(st, 'loc')} | {F.cond(st, 'loc', True)} | {F.iframe(st)} |")
    L += ["", f"- paccayo = {F.PACCAYA}{src('paccayo')}; «paccayena paccayo» = «… ဖြင့် {F.IS_COND}»; "
          f"«na Xpaccayena paccayo» = «{F.iframe('sahajāta', True)}»",
          f"- Xpaccayopi (vitthāretabbo) = {F.cond('ārammaṇa', 'pi')}; Xpaccayo (object) = {F.cond('hetu', 'obj')}",
          f"- ghaṭanā names (bare): " + "၊ ".join(F.cond(s, 'bare') for s in F.STEMS), ""]
    for k in ("hetu", "ārammaṇa", "adhipati", "anantara", "samanantara", "sahajāta", "āsevana", "āhāra", "indriya", "magga"):
        w = [x for x in F.WITNESS if x.lower().startswith(k) and "paccayena" in x.lower()]
        if w:
            b, bid, my = F.WITNESS[w[0]]
            L.append(f"- {w[0]} = {my} (pi-{b} {bid})")
    L.append("")
    L += ["## 4. Frames (by section, order and polarity)", "",
          "- paṭiccavāra: «X-aṃ dhammaṃ paṭicca Y-o dhammo uppajjati Zpaccayā» = «X သဘောတရားကို မှီ၍ Y သဘောတရားသည် "
          "Zဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်»; negative «naZpaccayā» = «… Zဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ဖြစ်ပေါ်သည်»",
          "- a chain «… uppajjati A… B… C – …» keeps one verb, after the last condition: «… A-ကြောင့်… B-ကြောင့်… "
          "C-ကြောင့် ဖြစ်ပေါ်သည် – …»",
          "- pucchāvāra: «Siyā X paṭicca Y uppajjeyya Zpaccayā» = «X ကို မှီ၍ Y သည် Z-ကြောင့် ဖြစ်ပေါ်နိုင်သလော»; "
          "plural uppajjeyyuṃ = «ဖြစ်ပေါ်နိုင်ကြသလော»",
          f"- the explanation «ekaṃ khandhaṃ paṭicca dve khandhā, dve khandhe paṭicca eko khandho» = "
          f"«အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး နှစ်ပါး၊ အစုအဝေး နှစ်ပါးကို မှီ၍ အစုအဝေး တစ်ပါး»",
          "- link words: " + "; ".join(f"{k} = «{v('X')}»" for k, v in F.LINK.items()),
          "- verbs: " + "; ".join(f"{k} = {v}" for k, v in F.VERB.items()),
          "- prefixes: " + "; ".join(f"{k} = {v}" for k, v in F.PREFIX.items()),
          "- pañhāvāra: «X-o dhammo Y-assa dhammassa Zpaccayena paccayo» = «X သဘောတရားသည် Y သဘောတရားအား "
          f"{F.iframe('hetu').replace('အမြစ်', 'Z')}» (pi-5 ^5-716: «ရှေးရှေး ကုသိုလ် သဘောတရားတို့သည် နောက်နောက် "
          "ကုသိုလ် သဘောတရားတို့အား ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းဖြင့် အကြောင်း …»)",
          f"- coordination «X Yñca» / «X ca Y ca» = «X{F.LAKAUNG}၊ Y{F.LAKAUNG}» (case marker inside); terms on one noun "
          "«kusalo ca abyākato ca dhammā» = «ကုသိုလ် သဘောတရားနှင့် … သဘောတရားတို့»",
          f"- aññamaññaṃ = {F.ANNAMANNAM}; kesañci (after a recipient) = «…{F.AMONG_SOME}»; kiñci kāle = {F.KINCI_KALE}; "
          f"-pi = «…{F.PI}»", ""]
    L += ["## 5. Counting frames", "",
          f"- «Hetuyā tīṇi» = «{F.count_my('hetu', False, 'tīṇi')}»; «Nahetuyā tīṇi» = «{F.count_my('hetu', True, 'tīṇi')}»",
          f"- «Hetupaccayā ārammaṇe tīṇi» = «{F.cond('hetu', 'ab')}{F.C} {F.count_my('ārammaṇa', False, 'tīṇi')}» "
          "(«၊» between the given conditions and the first count)",
          f"- ghaṭanā «Hetu-sahajāta-…nti tīṇi» = «{F.ghatana_list(['hetu', 'sahajāta'])}၌ {F.COUNT['tīṇi']}»; "
          f"with a following count «…nti naārammaṇe tīṇi» = «{F.ghatana_list(['hetu', 'sahajāta'])}နှင့် "
          f"{F.count_my('ārammaṇa', True, 'tīṇi')}»", ""]
    L += ["## 6. Doctrinal and other terms", ""]
    for k, (my, case, pl) in sorted(F.FIXED.items()):
        if k[:1].islower():
            L.append(f"- {k} = {my}{src(k)}")
    for k, v in sorted(F.QUAL.items()):
        L.append(f"- {k} = {v}{src(k)}")
    for k, (my, case, pl) in sorted(F.NOUN.items()):
        L.append(f"- {k} = {my}")
    L += ["", "### Phrase lexicon (LEX, kind in brackets)", ""]
    for k, (v, kind) in F.LEX.items():
        L.append(f"- {k} = {v.rstrip('+')} [{kind}]")
    L += ["", "### Notes (parenthetical remarks)", ""]
    for k, v in F.NOTES.items():
        L.append(f"- {k} = {v}")
    L += ["", "### This sample's phrases (make_sample.PH)", ""]
    for k, v in S.PH.items():
        L.append(f"- {k} = {v}")
    L += ["", "## 7. Number words", ""]
    for k, v in F.COUNT.items():
        L.append(f"- {k} (count) = {v}")
    for k, v in F.NP_NUM.items():
        L.append(f"- {k} (khandha / mahābhūta) = {F.PAA[v]}")
    L += ["", "## 8. Values reused from pi-1 … pi-6 (checked at import)", ""]
    for k, (b, bid, my) in F.WITNESS.items():
        L.append(f"- {k} = {my} (pi-{b} {bid})")
    (HERE / "my7-zeroshot-terms.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("wrote my7-zeroshot-terms.md:", len(L), "lines")
