# -*- coding: utf-8 -*-
"""pi-5 (Kathāvatthu) Vietnamese zero-shot, chapter 7: 7-ekaccam-atthitikatha.md (Ekaccaṃ atthītikathā,
^5-7-0 … ^5-300).

Imports the approved sample builder (build_sample_vi, read-only) for every debate frame; the chapter's own
repeated phrases are fixed strings below, so every repeat is byte-identical. Every string claimed from the
pi-1..4 Vietnamese rails is asserted to occur there; the sample's per-line checks (IDs, dashes, quotes, NFC,
foreign letters) are run against the Pāli.

run:  python -I -X utf8 build_7_vi.py
"""
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-5-vi-ai")
import build_sample_vi as B  # noqa: E402

NAME = "7-ekaccam-atthitikatha.md"
Q, q, NANU, AM, cap = B.Q, B.q, B.NANU, B.AMANTA, B.cap
NH, NHP = B.NA_HEVAM, B.NA_HEVAM_PE
VAR = B.VAR

# ================================================================ terms (cross-book where marked)
ATITAM = "quá khứ"                          # atītaṃ (noun; terms-file heading «một phần của quá khứ»)
ANAGATAM = "tương lai"                      # anāgataṃ (noun; terms-file heading «một phần của tương lai»)
ATTHI = "tồn tại"                           # atthi (sample)
NATTHI = "không tồn tại"                    # natthi
EKACCAM = "một phần"                        # ekaccaṃ (neuter sg.; terms-file heading)
EKACCE = "một số"                           # ekacce (masc. pl., of dhammā)
E_AN = f"{EKACCAM} {ATTHI}, {EKACCAM} {NATTHI}"   # ekaccaṃ atthi, ekaccaṃ natthi
E_AN_PL = f"{EKACCE} {ATTHI}, {EKACCE} {NATTHI}"  # ekacce atthi, ekacce natthi
TE_A = f"chúng {ATTHI}"                     # te atthi
TE_N = f"chúng {NATTHI}"                    # te natthi

AT_DH = "các hiện tượng thuộc quá khứ"      # atītā dhammā (pi-1 matrix «Các hiện tượng thuộc quá khứ»)
AN_DH = "các hiện tượng thuộc tương lai"    # anāgatā dhammā (pi-1 matrix)
PA_DH = "các hiện tượng thuộc hiện tại"     # paccuppannā dhammā (pi-1 matrix)
AVP = "có quả chưa chín muồi"               # avipakkavipākā (pi-1 ^1-1043)
VP = "có quả đã chín muồi"                  # vipakkavipākā (new, mirrors pi-1)
AV = "không có quả"                         # avipākā (new; aṭṭhakathā: the indeterminate)
UPD = "sẽ sinh khởi"                        # uppādino (pi-1 matrix «Các hiện tượng sẽ sinh khởi»)
ANUPD = "sẽ không sinh khởi"                # anuppādino (new)
NIR = "đã chấm dứt"                         # niruddha (pi-1 ^1-1044)
AJATA = "chưa sinh ra"                      # ajāta (pi-1 ^1-1045)
VIPACC = "sẽ trổ quả"                       # vipaccissanti (vipaccati «trổ quả» pi-2)
UPPAJJ = "sẽ sinh khởi"                     # uppajjissanti (pi-1 ^1-1043 uppajjissati «sẽ sinh khởi»)
NIRUJJH = "sẽ chấm dứt"                     # nirujjhissanti (nirujjhati «chấm dứt» pi-2)
PACC = "thuộc hiện tại"                     # paccuppannā (predicate; pi-1 ^1-1046)

# atītaṃ: niruddhaṃ / vigataṃ / atthaṅgataṃ / abbhatthaṅgataṃ (pi-1 ^1-1044, pi-2 ^2 khandhavibhaṅga)
PAST_PAIRS = [("đã chấm dứt", "chưa chấm dứt"), ("đã mất đi", "chưa mất đi"),
              ("đã biến mất", "chưa biến mất"), ("đã biến mất hoàn toàn", "chưa biến mất hoàn toàn")]
# anāgataṃ: jātaṃ / sañjātaṃ / nibbattaṃ / pātubhūtaṃ (pi-2 ^2-3) and ajātaṃ … apātubhūtaṃ (pi-1 ^1-1045)
FUT_PAIRS = [("đã sinh ra", "chưa sinh ra"), ("đã sinh thành", "chưa sinh thành"),
             ("đã phát sinh", "chưa phát sinh"), ("đã hiện ra", "chưa hiện ra")]


def pairs(pp):
    """ekaccaṃ X, ekaccaṃ na X; … (four pairs, separated by «;» as the Pāli)"""
    return "; ".join(f"{EKACCAM} {a}, {EKACCAM} {b}" for a, b in pp)


def dh(base, quality, var=""):
    """atītā <quality> dhammā  ->  các hiện tượng thuộc quá khứ <quality>"""
    return f"{base} {quality}{var}"


def nir(np):
    """<…> dhammā niruddhā (attribute or predicate: one fixed form)"""
    return f"{np}, {NIR}"


def ajata(np):
    """<…> dhammā ajātā"""
    return f"{np}, {AJATA}"


def te(np, neg=False):
    """<…> dhammā – te atthi / te natthi"""
    return f"{np} – {TE_N if neg else TE_A}"


def katva(x, y, low=False):
    """Xti katvā Yti? (without «tena ca kāraṇena»; sample frame «vì cho rằng»)"""
    s = f"có phải vì cho rằng {x}, {y} không?"
    return s if low else cap(s)


def hanci_no(p, qq):
    """Hañci P, no ca vata re vattabbe – "Q"ti. (= build_3_vi.py nanca / build_2_vi.py hanci_no)"""
    return f"Nếu {p}, {B.NO_CA_VATA} “{qq}”."


A_AVP = dh(AT_DH, AVP)
A_VP = dh(AT_DH, VP)
A_AV = dh(AT_DH, AV)
F_UP = dh(AN_DH, UPD)
F_AN = dh(AN_DH, ANUPD)


def build():
    d = B.Doc()
    d.head(3, B.KATHA.format(x="việc cho rằng một phần tồn tại"), "5-7-0")     # Ekaccaṃ atthītikathā
    # ------------------------------------------------------------ Atītādiekaccakathā
    d.head(4, "Bàn về một phần của quá khứ và các mục khác", "5-7-1-0")
    T_A = f"{ATITAM} {E_AN}"                                                  # atītaṃ ekaccaṃ atthi, ekaccaṃ natthi
    d.seg("5-299",
          # 5
          f"{Q(f'{ATITAM} {ATTHI}')} {cap(E_AN)}. {Q(pairs(PAST_PAIRS))} {NHP}",
          # 6
          f"{Q(T_A)} {AM} {Q(f'{A_AVP}, {E_AN_PL}')} {NHP} {q(T_A)} {AM} "
          f"{Q(f'{A_VP}, {E_AN_PL}')} {NHP} {q(T_A)} {AM} {Q(f'{A_AV}, {E_AN_PL}')} {NHP}",
          # 7
          f"{Q(T_A)} {AM} Cái gì {ATTHI}, cái gì {NATTHI}? {cap(te(A_AVP))}; {te(A_VP, True)}. "
          f"{Q(te(A_AVP))} {AM} {Q(te(A_VP))} {NHP} {q(te(A_AVP))} {AM} "
          f"Có phải {te(A_AV)} [{VAR} (Ka.): atītā avipakkavipākā dhammā te natthīti] không? {NHP}",
          # 8
          f"{Q(te(A_VP, True))} {AM} {Q(te(A_AVP, True))} {NHP}",
          # 9
          f"{Q(te(dh(AT_DH, AV, f' [{VAR} (Syā.): vipakkavipākā; (Ka.): avipakkavipākā]'), True))} {AM} "
          f"{Q(te(dh(AT_DH, AVP, f' [{VAR} (Syā.): avipākā]'), True))} {NHP}",
          # 10
          f"{Q(te(A_AVP))} {AM} {NANU(nir(A_AVP))} {AM} "
          f"{hanci_no(nir(A_AVP), f'{A_AVP} – chúng [{VAR} (Syā., Ka.): dhammā niruddhā te] {ATTHI}')}",
          # 11
          f"{Q(te(nir(A_AVP)))} {AM} {Q(te(nir(A_VP)))} {NHP} {q(te(nir(A_AVP)))} {AM} "
          f"{Q(te(nir(dh(AT_DH, AV, f' [{VAR} (Sī., Ka.): avipakkavipākā]'))))} {NHP}",
          # 12
          f"{Q(te(nir(A_VP), True))} {AM} {Q(te(nir(A_AVP), True))} {NHP}",
          # 13
          f"{Q(te(nir(dh(AT_DH, AV, f' [{VAR} (Syā.): vipakkavipākā; (Ka.): avipakkavipākā]')), True))} {AM} "
          f"{Q(te(nir(dh(AT_DH, AVP, f' [{VAR} (Syā.): avipākā]')), True))} {NHP}",
          # 14
          f"{Q(te(nir(A_AVP)))} {AM} {Q(te(nir(A_VP), True))} {AM} "
          f"{Q(nir(f'{AT_DH} một phần {VP}, một phần {AVP}') + f' – chúng, {E_AN_PL}')} {NHP}",
          # 15
          f"{B.NA_VATTABBAM_Q(te(A_AVP))} {AM} {NANU(f'{A_AVP}, {VIPACC}')} {AM} "
          f"{B.hanci(f'{A_AVP}, {VIPACC}', te(A_AVP))}",
          # 16
          f"{katva(f'{A_AVP}, {VIPACC}', TE_A)} {AM} {katva(f'chúng {VIPACC}', f'chúng {PACC}')} {NHP} "
          f"{katva(f'chúng {VIPACC}', f'chúng {PACC}', low=True)} {AM} "
          f"{katva(f'{PA_DH} {NIRUJJH}', TE_N)} {NHP}")
    # ------------------------------------------------------------ Anāgatādiekaccakathā
    d.head(4, "Bàn về một phần của tương lai và các mục khác", "5-7-2-0")
    F_A = f"{ANAGATAM} {E_AN}"
    d.seg("5-300",
          # 20
          f"{Q(f'{ANAGATAM} {ATTHI}')} {cap(E_AN)}. {Q(pairs(FUT_PAIRS))} {NHP}",
          # 21
          f"{Q(F_A)} {AM} {Q(f'{F_UP}, {E_AN_PL}')} {NHP} {q(F_A)} {AM} {Q(f'{F_AN}, {E_AN_PL}')} {NHP}",
          # 22
          f"{Q(F_A)} {AM} Cái gì {ATTHI}, cái gì {NATTHI}? {cap(te(F_UP))}; {te(F_AN, True)}. "
          f"{Q(te(F_UP))} {AM} {Q(te(F_AN))} {NHP} {q(te(F_AN, True))} {AM} {Q(te(F_UP, True))} {NHP}",
          # 23
          f"{Q(te(F_UP))} {AM} {NANU(ajata(F_UP))} {AM} {hanci_no(ajata(F_UP), te(F_UP))}",
          # 24
          f"{Q(te(ajata(F_UP)))} {AM} {Q(te(ajata(F_AN)))} {NHP} {q(te(ajata(F_AN), True))} {AM} "
          f"{Q(te(ajata(F_UP), True))} {NHP}",
          # 25
          f"{B.NA_VATTABBAM_Q(te(F_UP))} {AM} {NANU(f'{F_UP}, {UPPAJJ}')} {AM} "
          f"{B.hanci(f'{F_UP}, {UPPAJJ}', te(F_UP))}",
          # 26
          f"{katva(f'{F_UP}, {UPPAJJ}', TE_A)} {AM} {katva(f'chúng {UPPAJJ}', f'chúng {PACC}')} {NHP} "
          f"{katva(f'chúng {UPPAJJ}', f'chúng {PACC}', low=True)} {AM} "
          f"{katva(f'{PA_DH} {NIRUJJH}', TE_N)} {NHP}",
          # 27
          B.KATHA_END.format(x="việc cho rằng một phần tồn tại"))
    return d.text()


# ================================================================ cross-book asserts (pi-1..4 rails)
CROSS = [
    ("Các hiện tượng thuộc quá khứ", 1), ("Các hiện tượng thuộc tương lai", 1), ("Các hiện tượng thuộc hiện tại", 1),
    ("có quả chưa chín muồi", 1), ("Các hiện tượng sẽ sinh khởi", 1), ("sẽ sinh khởi do nghiệp", 1),
    ("đã chấm dứt, đã mất đi, đã biến đổi, đã biến mất, đã biến mất hoàn toàn", 1),
    ("đã chấm dứt, đã mất đi, đã biến đổi, đã biến mất, đã biến mất hoàn toàn", 2),
    ("chưa sinh ra, chưa trở thành, chưa sinh thành, chưa phát sinh, chưa phát sinh rõ rệt, chưa hiện ra", 1),
    ("đã sinh ra, đã trở thành, đã sinh thành, đã phát sinh, đã phát sinh rõ rệt, đã hiện ra", 2),
    ("những hiện tượng này thuộc hiện tại", 1), ("mà trổ quả", 2), ("khi chấm dứt thì chấm dứt", 2),
    ("tồn tại", 1),
]


def check_cross():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(dd.glob("*.md")))
             for b, dd in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"ch7 cross-book asserts: {len(CROSS)} strings found in pi-1..4 rails")


def main():
    B.check_cross_book()
    check_cross()
    text = unicodedata.normalize("NFC", build())
    pali = (B.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs, repaired = B.check_lines(pali, text, NAME)
    for p in probs:
        print("PROBLEM", p)
    assert not probs, f"{len(probs)} line problems"
    assert "\r" not in text and "\n\n\n" not in text and "—" not in text
    with open(B.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {NAME}: {len([l for l in text.splitlines() if l.strip()])} lines; "
          f"odd closing order repaired: {len(repaired)}; line checks: OK")


if __name__ == "__main__":
    main()
