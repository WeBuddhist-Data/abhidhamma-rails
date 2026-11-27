"""phase 3: writes mapper-my/phase3-changes.tsv — every value that differs between work/phase2-mapped/ and the current
*.mapped.md (work/diff3.py) with its reason; exits with an error on any change without a reason.
usage: reasons.py   (reads work/d1.tsv = diff3.py output)"""
import sys, pathlib, collections
W = pathlib.Path(__file__).resolve().parent
D = W.parent
R = {}
def add(code, text, *kws):
    for k in kws:
        R[k] = (code, text)

add("M3", "mechanic 3: phrase_present() accepts the perfect predicate «Xပြီး ဖြစ်» for «Xပြီးသော» (as presence() does), so the "
    "text's «… Xကို …ပြီး ဖြစ်» is one phrase and is glued (rule 1: the inner particle stays) instead of « … »",
    "maggo bhāvito", "bojjhaṅgā bhāvitā", "dve phalāni paṭiladdhāni", "diṭṭhipariyuṭṭhānaṃ pahīnaṃ",
    "puggalassa diṭṭhipariyuṭṭhānaṃ pahīnaṃ", "anusayo pahīno")
add("M2", "mechanic 2: a verb is not glued to its neighbour through the text's verbal noun «…ခြင်း» (the adjacent phrase "
    "stands only as «…ခြင်း», another construction); the members are joined with « … » (rule 10)",
    "bhagavā voharati", "kusalaṃ paṭilabheyya", "niyāmaṃ okkameyya", "niyāmaṃ okkamati", "Akusalamūlaṃ paṭisandahati",
    "kusalamūlaṃ paṭisandahati", "saṅgho dakkhiṇaṃ visodheti", "saṅgho dakkhiṇaṃ paṭiggaṇhāti", "dānaṃ visujjhati",
    "dakkhiṇaṃ visodheti", "dakkhiṇaṃ paṭiggaṇhāti")
add("G2r-attr", "G2 made exact (phase 3): an attributive adjacency «…သော X» is the text's own construction and stays "
    "(the phase-2 reordering went through «ရုပ်» inside «ရုပ်မရှိသော» / a later clause)",
    "Kammūpacayo sahajāto", "rūpaṃ rūpāvacaraṃ", "rūpaṃ arūpāvacaraṃ")
add("G2r-clause", "G2 made exact (phase 3): the Pāli order stood only across a clause boundary («။ / … / –»); the text "
    "order of the one clause that has both members (Q3)", "saṅgho ujubhūto", "ariyo aṭṭhaṅgiko")
add("G5", "G5 book-wide: a duplicate member keeps both members (the composed value had dropped one)",
    "no paccuppannaṃ paccuppannaṃ", "Rūpena rūpaṃ")
add("OV", "module override moved (ch16-31 override 10, now @dhammo): the sutta's «sataṃ dhammo» «သူတော်ကောင်းတို့၏ "
    "တရား» = «တရား» (CTX, as ^5-599), not the pi-4 -dhammo compound value «သဘော ရှိသော»", "dhammo")
S1 = {
    "paṭilābhā": "S1 review: a noun «… ကို ရခြင်းကြောင့်» = «ရခြင်း» (stem value «ရသော»)",
    "upapattiyā": "S1 review: «cutiyā upapattiyā» = the noun «ပြန်လည် ဖြစ်ပေါ်ခြင်း» of the text (stem «…သော»)",
    "uppādā": "S1 review: saññuppādā «မှတ်သိမှု ဖြစ်ပေါ်ခြင်းကြောင့်» = the noun (stem «…သော»)",
    "passanto": "S1 review: present participle «…သော» (S5), text «မြင်နေစဉ်» (stem verb «မြင်သည်»)",
    "okkanta": "S1 review: the participle of okkantaniyāmo «…သက်ဆင်းပြီး၍» = «…သော» (rule 3; stem «သက်ဆင်းသည် / …ခြင်း»)",
    "carita": "S1 review: caritabrahmacariyo «… အကျင့်ကို ကျင့်ပြီးသူ» = «ကျင့်ပြီးသော» (rule 3; stem took cariya's «အကျင့်»)",
    "bodhiyā": "S1 review: «bodhiyā buddho» «ဗောဓိဖြင့် ဘုရား» = «ဗောဓိ» (stem took bodhisatta's «ဘုရားလောင်း»)",
    "bodhiyā buddho": "S1 review (follows bodhiyā): composed «ဗောဓိဖြင့် ဘုရား» as the text has it",
    "samāpajjeyya": "S1 review: a verb (rule 4) «ဝင်စားနေသည်» (stem «ဝင်စားနေသော»)",
    "pariyāye": "S1 review: cetopariyāye ñāṇaṃ «စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်»: the part pariyāya carries (ceto = စိတ်)",
    "uppajja": "S1 review: absolutive «ဖြစ်ပေါ်၍» (the text's form; stem verb «…သည်»)",
    "ṭhitā": "S1 review: «ṭhitāva sā dhātu» «တည်လျက်ပင်» = «တည်သော» (rule 3; stem took ṭhitatā «တည်ရှိခြင်း»)",
    "ṭhiti": "S1 review: viññāṇaṭṭhiti «သိစိတ် တည်ရာ» = «တည်ရာ» (as ch16-31 @thiti; stem «တည်သော»)",
    "sakavādi": "S1 review: the note «[မိမိဘက်၏ စကား …]» = «မိမိဘက်» (FRAME vādī; stem «မိမိ»)",
    "sahajātā": "S1 review: «cittena sahajātā» «စိတ်နှင့်အတူ ပေါ်ပေါက်သော» (as ch16-31; stem «အတူ»)",
    "vedaniyā": "S1 review: sukhavedaniya «သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော» (rule 3; stem noun «ခံစားမှု»)",
    "vedaniyaṃ": "S1 review: sukhavedaniya «သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော» (rule 3; stem noun «ခံစားမှု»)",
    "haraṇo": "S1 review: acoraharaṇo «ခိုးသူတို့ မယူဆောင်နိုင်သော» = the positive part «ယူဆောင်နိုင်သော» (rule 8; stem «ဆောင်သည်»)",
    "bhedako": "S1 review / scan: saṅghabhedako «သင်းခွဲသူ» (= ch16-31; stem «ခွဲသူ»)",
}
for k, t in S1.items():
    R[k] = ("S1", t)
SC = {
    "dhammapade": "scan: rule 1, the reference without its final «၌» («“ဓမ္မပဒ”», 2 of 4 already)",
    "methunaṃ dhammaṃ": "scan: «မေထုန် အကျင့်ကို မှီဝဲရာ» = «မေထုန် အကျင့်» (as ch30 / ch31; the composed «… သဘော» is not the phrase)",
    "buddha": "scan: buddhasāsane «ဘုရား», not bhagavā's «မြတ်စွာဘုရား»",
    "sacchikato": "scan: one sense per segment, the first («… မျက်မှောက်ပြုပြီး၍»), as the other uses of the keyword",
    "adhigato sacchikato": "scan: follows sacchikato (one sense per segment, the first)",
    "arahattappatto sacchikato": "scan: follows sacchikato (one sense per segment, the first)",
    "sotāpattiphalappatto sacchikato": "scan: follows sacchikato (one sense per segment, the first)",
    "sampajāno": "scan: rule 3 / Q8 adjective «…သော» (the book's value; the text «… ဆင်ခြင်သိမြင်ခြင်း ရှိသူ»)",
    "yoni": "scan: yoni «မွေးဖွားရာ အမျိုးအစား» (the list «bhavo … yoni»: «ဘဝ» is bhavo's word), now module STOCK",
    "atta": "scan: atta of attabhāva = «ကိုယ်» of «ကိုယ်ခန္ဓာ» (pi-2 decision 4, as ch16-31; module @atta)",
    "anāgatāya buddho": "scan: Q3 / G2, «အနာဂတ် ဗောဓိဖြင့် ဘုရား» (text and Pāli order)",
    "paccuppannāya buddho": "scan: Q3 / G2, «ပစ္စုပ္ပန် ဗောဓိဖြင့် ဘုရား» (text and Pāli order)",
    "anupalitto": "scan: S6, the privative keyword keeps the text's «မလိမ်းကျံ» (as ^5-803)",
    "pajahitvā": "scan: Q1, absolutive «X၍» against the text's «Xပြီး»", "visinitvā": "scan: Q1, absolutive «X၍» against the text's «Xပြီး»",
    "apacinitvā": "scan: Q1, absolutive «X၍» against the text's «Xပြီး»",
    "Abhabbo": "scan: the pi-1 … pi-4 value «မထိုက်တန်» (binding; as abhabbo ^5-317 …)",
    "sabbaññū": "scan: Q8 epithet «…သော» (as ^5-354, ^5-443)",
    "abbokiṇṇaṃ": "scan: rule 1, the value without the text's adverbial ending «…ဘဲ» (as ch12 «ကြားမလပ်»)",
}
for k, t in SC.items():
    R[k] = ("SC", t)
G2 = ("G2", "G2 approved book-wide (phase 3, now in the module): the Pāli order where the text has the members in that "
      "order inside one clause (was the Q3 text-order window, across a clause)")
KATHA = ("SC-katha", "scan A1: the kathā heading = the text's phrase «Xအကြောင်း ဆွေးနွေးချက်» (rule 1: the inner "
         "«အကြောင်း» stays; rule 10: « … » only for discontinuous parts), as ch16-31 (53 uses)")
rows, miss = [], []
cnt = collections.Counter()
for l in (W / "d1.tsv").read_text(encoding="utf-8").splitlines():
    ch, sid, k, old, new = l.split("\t")
    r = R.get(k)
    if r is None and k.lower().endswith("kathā") and new.endswith("အကြောင်း ဆွေးနွေးချက်"):
        r = KATHA
    if r is None and len(k.split()) == 2 and " … " in old and " … " in new \
            and sorted(old.split(" … ")) == sorted(new.split(" … ")):
        r = G2
    if r is None and len(k.split()) == 2 and " … " not in old and " … " in new \
            and old.replace(" ", "") == "".join(reversed(new.split(" … "))).replace(" ", ""):
        r = ("G2", G2[1] + "; a bare adjacency in the other order (no particle, no «၊» in the Pāli-order clause)")
    if r is None:
        miss.append(l); continue
    cnt[r[0]] += 1
    rows.append("\t".join([sid, k, old, new, f"{r[0]}: {r[1]}"]))
if miss:
    print("\n".join(miss)); sys.exit(f"{len(miss)} changes without a reason")
(D / "phase3-changes.tsv").write_text("segment\tkeyword\told\tnew\treason\n" + "\n".join(rows) + "\n", encoding="utf-8")
print("changes", len(rows), dict(cnt))
