"""Mutation test for check_sample.py: each planted error must be caught (writes only into pi-7-my/chk-mut/).

usage: python3 -I -X utf8 chk_mutate.py
"""
import pathlib
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
TMP = HERE / "chk-mut"
MUT = [  # (file, old, new, what)
    ("1-02-vedanattika.md", "အမြစ်ဟူသော အကြောင်း၌ သုံးခု၊ အာရုံဟူသော", "အမြစ်ဟူသော အကြောင်း၌ နှစ်ခု၊ အာရုံဟူသော", "count"),
    ("1-02-vedanattika.md", "အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ဖြစ်ပေါ်သည်", "အမြစ်ဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်", "polarity"),
    ("1-02-vedanattika.md", "သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော သဘောတရားသည် နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော သဘောတရားအား",
     "နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော သဘောတရားသည် သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော သဘောတရားအား", "term order"),
    ("1-00-paccaya.md", "အာရုံဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်။ အသံ", "အကြီးအမှူးဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်။ အသံ",
     "condition"),
    ("1-02-vedanattika.md", "အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး နှစ်ပါး၊", "အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး သုံးပါး၊", "khandha count"),
    ("1-00-paccaya.md", "ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရားသည် အမြစ်", "ကုသိုလ် သဘောတရားသည် အမြစ်",
     "term"),
    ("1-02-vedanattika.md", "(10) ^7-3-63", "(11) ^7-3-63", "digits"),
]


def main():
    caught = 0
    for f, old, new, what in MUT:
        if TMP.exists():
            shutil.rmtree(TMP)
        TMP.mkdir()
        for n in ("1-00-paccaya.md", "1-02-vedanattika.md"):
            shutil.copy(OUT / n, TMP / n)
        t = (TMP / f).read_text(encoding="utf-8")
        if old not in t:
            print("mutation not applicable:", what)
            continue
        (TMP / f).write_text(t.replace(old, new, 1), encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE / "check_sample.py"), "--out", str(TMP)],
                           capture_output=True, text=True)
        last = r.stdout.strip().splitlines()[-1]
        ok = r.returncode != 0
        caught += ok
        print(f"{what:14} -> {'caught' if ok else 'MISSED'} ({last})")
    shutil.rmtree(TMP)
    print(f"{caught} / {len(MUT)} planted errors caught")
    sys.exit(0 if caught == len(MUT) else 1)


main()
