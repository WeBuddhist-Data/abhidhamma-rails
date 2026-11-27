"""phase 3: phase3-changes.tsv = every value of the 75 *.mapped.md that differs from the phase-2 files
(work/phase2-mapped, md5 = work/before-phase3-files-md5.txt), with the stage that changed it and its reason
(model: pi-6-my/mapper-my/work/p3_changes.py)."""
import sys
import pathlib
import collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.dont_write_bytecode = True
import p3_stage as S

F1 = ("fix 1 (word boundaries): the old value stood in the segment only as the start of a longer word; the value is "
      "now the text's whole word")
REASON = {
    ("s1-bound", "paripanthe"): F1 + " («လမ်း» inside «လမ်းခရီး»: paripanthe «လမ်းခရီး၌ ဓားပြ တိုက်သည်»; U3 keeps a "
                                "pi value only where it stands as a phrase)",
    ("s1-bound", "cakkaṃ"): F1 + " («စက်» inside «စက်ဝိုင်း», the text's «(စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍ ပြုရမည်)»; the "
                            "coordinator's cakkaṃ example; module STOCK cakkaṃ «စက်ဝိုင်း»)",
    ("s1-bound", "sahajātaṃ"): F1 + " («အတူ ပေါ်ပေါက်ခြင်း» stood only inside the vāra name «…ခြင်းအလိုက်»; the "
                               "quoted «sahajātaṃ kāmupādāna»nti is the text's adjective «အတူ ပေါ်ပေါက်သော ကာမ စွဲလမ်းမှု»)",
    ("s1-bound", "paccaya"): "fix 1 follow-up (T4 / T5): «paccaya» as a part of the hyphen vāra name «Sahajāta-paccaya-"
                             "nissaya-saṃsaṭṭha-sampayuttavāro» is the vāra member «အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း» "
                             "(VARA, the text's heading); the old «အကြောင်း» was only the start of «အကြောင်းပြု၍»",
    ("s1-bound", "saṃsaṭṭha"): "fix 1 follow-up (T4 / T5): in the same hyphen vāra names saṃsaṭṭha is the vāra member "
                               "«ရောနှောခြင်း» (VARA), the text's word «ရောနှောခြင်းနှင့် ယှဉ်တွဲခြင်းအလိုက်», as "
                               "Sahajāta «အတူ ပေါ်ပေါက်ခြင်း» in the same heading (the old «ရောနှောသော» stood only by "
                               "the ending rule)",
    ("s2-gen", "pañcaviññāṇaṃ"): "fix 3 (generator reading) / fix 9: the module had read the concatenated generator "
                                 "string «'သိစိတ် ' + …» as the term «သိစိတ်»; pañcaviññāṇaṃ is the dictionary form "
                                 "«သိစိတ် ငါးပါး» (the text's phrase, pi-5 pañcaviññāṇā)",
    ("s2-gen", "tadārammaṇatā"): "fix 3: tadārammaṇatā is the text's phrase, one value per text form; the module's "
                                 "«စိတ်သည်» (the head noun of vipāko, read from «'စိတ်သည် ' + new(…)») goes; 2-05 "
                                 "^7-11-46 has the 1-01 form «… အာရုံပြုသည့် အနေဖြင့်» (rule 1: «ဖြင့်» goes)",
    ("s3-r1", "upādānañca"): "fix 5 (R1 order) with the gocchaka-item decision: Upādānañca takes its base form's value, "
                             "the bare item «စွဲလမ်းမှု» (T13's «N ဖြစ်သော» goes)",
    ("s6-item", "saññojano"): "coordinator, gocchaka dyad items (g3 G1 vs T13, g5 U-g5-1): the item term is the bare "
                              "noun «N» in every case (binding pi-1 Mātikā saṃyojanā «နှောင်ကြိုး», pi-1 rule 2); T13's "
                              "«N ဖြစ်သော» goes book-wide",
    ("s7-natthi", "natthi"): "coordinator, natthi: «မရှိ» where «မရှိသည်» stands only inside a longer term, otherwise "
                             "the module value (f_natthi, g4 G3 built in): the old «မရှိသည်» stood only by the ending "
                             "rule inside «မရှိခြင်းဟူသော အကြောင်း / ရုပ်မရှိသော / အမြစ် မရှိသော», so the note «(… "
                             "natthi)» «(… မရှိ)» is «မရှိ»; ^7-35-204 «… မရှိ။» is the module's «မရှိသည်» (the old «မရှိ» "
                             "came from g4's count test firing on 0 = 0)",
    ("s8-book", "uposathakammaṃ"): "coordinator, g2 decision: uposathakammaṃ = «ဥပုသ် စောင့်ထိန်းခြင်း» where the text "
                                   "has that noun (…pe… cuts the verb off); module STOCK tuple",
    ("s8-book", "nahetuṃ"): "g3 override Nahetuṃ, moved into the module (cond_cands): «Nahetuṃ (X) dhammaṃ» is the dyad "
                            "term «အမြစ် မဟုတ်သော» (T8), not the condition; the text has «အမြစ် မဟုတ်သော … သဘောတရား»",
    ("s8-book", "paripuṇṇaṃ"): "fix 9 (paripuṇṇo «ပြည့်စုံသော», one value per term): the bare stem «ပြည့်စုံ» is no "
                               "dictionary form; where the text has only the adverb «ပြည့်စုံစွာ» («(paripuṇṇaṃ nava)» "
                               "«(ပြည့်စုံစွာ ကိုးခု)») that is the value (g2 ^7-9-19 precedent)",
    ("s8-book", "naviññeyyaṃ"): "coordinator: naviññeyyo «မသိနိုင်သော», the text's own lexical negative (it stands in "
                                "the segment for «kenaci naviññeyyo»); the T8 «သိနိုင်သည် မဟုတ်သော» was the text of "
                                "«Nakenaci viññeyyaṃ», another phrase",
    ("s9-strip", "suciṇṇāni"): "one value per term / dictionary form (rule 3): the participle «ကောင်းစွာ ပြုခဲ့ဖူးသော» "
                               "(g2's value) against g1's nominal «… ပြုခဲ့ဖူးသည်»; the text's «… ပြုခဲ့ဖူးသည်တို့» by the "
                               "attributive ending rule",
    ("s9-strip", "paripuṇṇā"): "fix 9: paripuṇṇo «ပြည့်စုံသော» book-wide (g4 had the verb «ပြည့်စုံသည်»)",
    ("s10-head", "sappaccayasadisaṃ"): "coordinator, head noun «သဘောတရား» in -sadisa / -mūla notes: the gap is "
                                       "impossible where the next chunk would start with the particle «နှင့်», so the "
                                       "text's noun stays inside (logged exception)",
    ("s10-head", "upādinnamūlake"): "coordinator, head noun rule: the supplied «သဘောတရားကို» is left out with a « … » "
                                    "gap (the next chunk «အခြေခံခြင်း» starts with no particle)",
    ("s10-head", "pahātabbabhājanakāraṇe"): "coordinator, head noun rule (one rule everywhere): the supplied «သဘောတရားကို» "
                                            "joins the gap that already holds nabhāvanāya's negative",
    ("s11-scan", "sekkhāya"): "coordinator, g2 decision (sekkha as a qualifier «…၏»): «anulomaṃ sekkhāya "
                              "phalasamāpattiyā» «… ကျင့်ကြံဆဲသူ၏ ဖိုလ်သမာပတ်အား» (scan alignment, f_sekkha)",
    ("s11-scan", "vipākassa"): "scan alignment (one sense per segment, phase 1 §B): «kammaṃ vipākassa … paccayena "
                               "paccayo» is the noun «ကံ၏ အကျိုး» (the text's «… ကံသည် ကံ၏ အကျိုးအား»), as in 1-05, "
                               "3-02, 3-09 (f_vipakassa)",
    ("s11-scan", "suddhake"): "scan alignment (one value per term; coordinator principle: no translator's addition, "
                              "phase 1 A5): «ရိုးရိုး» as 4-01; the text's head noun «အပိုင်း» goes",
    ("s11-scan", "arūpāvacare"): "scan alignment (one value per term): «arūpāvacare khandhe» «ရုပ်မရှိသော ဘုံနှင့် "
                                 "ဆိုင်သော အစုအဝေး», the value of the other arūpāvacara- forms (the old «ရုပ်မရှိသော ဘုံ» "
                                 "was the plane, rule 11)",
}
for k in ("saññojanaṃ", "yogaṃ", "kilesañceva"):
    REASON[("s6-item", k)] = REASON[("s6-item", "saññojano")]
REASON[("s8-book", "naviññeyyo")] = REASON[("s8-book", "naviññeyyaṃ")]
REASON[("s10-head", "atītasadisaṃ")] = REASON[("s10-head", "sappaccayasadisaṃ")]
REASON[("s2-gen", "pañcaviññāṇaṃ")] = REASON[("s2-gen", "pañcaviññāṇaṃ")]


def low(w):
    return w[:1].lower() + w[1:]


order = (S.ST / "order.txt").read_text().split()
final = S.read(S.stage_dir(order[-1]))
base = S.read(S.stage_dir("phase2"))
who = {}
for a, b in zip(order, order[1:]):
    for sid, i, k, o, n in S.diff(S.read(S.stage_dir(a)), S.read(S.stage_dir(b))):
        who.setdefault((sid, i), []).append(b)
rows, missing = [], []
for sid, i, k, o, n in S.diff(base, final):
    st = who.get((sid, i), ["?"])
    r = "; ".join(f"[{x}] " + REASON.get((x, low(k)), "?") for x in dict.fromkeys(st))
    if "?" in r.split("] ")[-1][:1] or r.endswith("] ?") or "] ?;" in r:
        missing.append((sid, k, o, n, st))
    rows.append((sid, k, o, n, r))
out = pathlib.Path(__file__).resolve().parent.parent / "phase3-changes.tsv"
out.write_text("segment\tkeyword\told\tnew\treason\n" + "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
print("changes", len(rows), "unexplained", len(missing))
c = collections.Counter(r[4].split("] ")[0].strip("[") for r in rows)
print(dict(c))
for m in missing:
    print("  ?", m)
