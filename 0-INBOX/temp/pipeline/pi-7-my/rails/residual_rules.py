"""pi-7 Burmese rails, residual rules (read by apply_termbase.py; model pi-6-my/rails/residual_rules.py, read only):
one rule per remaining single-segment difference, (rule id, Pāli keyword regex, segment ids, old, new, replacements
expected over all its ids, reason). Each Pāli text occurs once in the book (no repeated sentence is touched: the
repeated ones are changed in the layer, my_formulas_rails.py)."""

YATHA = ("§A4 «yathā [W] X-sadisaṃ» = «[W၌ / W၏] Xနှင့် တူသည့်အတိုင်း» (one shape book-wide, the majority 8 of 10: 3-01 ^7-24-…, "
         "3-09, 4-01 ×2, 4-06, 4-10 ×2, 4-13; the word X-sadisaṃ keeps its term «…နှင့် တူ…», yathā is «အတိုင်း»); the two "
         "«W(၌)ကဲ့သို့ … Xနှင့် တူသည်» lines take it")
RULES = [
    ("R01", r"Kusalattika-saññojanādidukāni", ["7-4-3-3-12-4-0"],
     "နှောင်ကြိုး နှစ်မျိုးတွဲ စသည်", "နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲများ", 1,
     "§A36 saññojanādidukāni = «နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲ(များ)» (termbase, decided; = 5-02 / 5-08 / 5-11 / 5-12 "
     "«Hetuduka-saññojanādidukāni» «… နှောင်ကြိုး စသည်တို့၏ နှစ်မျိုးတွဲများ»): the 4-17 heading «1-20-54. Kusalattika-"
     "saññojanādidukāni»"),
    ("R02", r"Yathā anulomaṃ sahajātasadisaṃ", ["7-4-32"],
     "အဟုတ်ပြ ပုံစံကဲ့သို့ အတူ ပေါ်ပေါက်ခြင်းနှင့် တူသည်။", "အဟုတ်ပြ ပုံစံ၏ အတူ ပေါ်ပေါက်ခြင်းနှင့် တူသည့်အတိုင်း။", 1,
     YATHA + " (accusative W as «Yathā cittasampayuttadukaṃ abyākatasadisaṃ» 4-10 «… နှစ်မျိုးတွဲ၏ …»)"),
    ("R03", r"Yathā sappītike nahetupaccayasadisaṃ", ["7-35-169"],
     "ပီတိ ရှိသော သဘောတရား၌ကဲ့သို့ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းနှင့် တူသည်၊",
     "ပီတိ ရှိသော သဘောတရား၌ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းနှင့် တူသည့်အတိုင်း၊", 1,
     YATHA + " (locative W as «Yathā cūḷantaraduke lokiyadukasadisaṃ» 4-01 / 4-06 «… အစုငယ်၌ …»)"),
]
