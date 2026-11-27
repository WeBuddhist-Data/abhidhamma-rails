"""pi-7 rails fix round, helper (not part of the checks): PROPOSE case fixes for the clause units case_check.py flags
in a chapter folder (default: the pre-fix rails backup). Each proposal is one (rule, Pāli unit, old, new) row:
  K1  S0, single subject marked «ကို» before the recipients  -> «…သည်»
  K2  S0/D0, the subject written as the first recipient «Xအား(လည်းကောင်း)၊» -> «Xသည်» (a lone remaining
      recipient «…အားလည်းကောင်း» -> «…အား»)
  K3  S0, the subject joined to the recipients by «၊» (no marker)            -> «Xသည်»
  K4  S2, «၊» after the last co-subject «…လည်းကောင်း၊» before the recipients -> «…လည်းကောင်း»
Everything else is written by hand in apply_fixes.py. Output: case-proposals.tsv (reviewed by hand, then frozen into
case-fixes.tsv, which apply_fixes.py reads).
usage: case_propose.py [folder]"""
import collections
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import case_check as cc  # noqa: E402

FOLDER = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "review/fix-backup/rails-text"
# a «ကို» inside a noun phrase is followed by its verb / postposition
NP_KO_NEXT = ("ပိုင်းခြား", "အာရုံပြု", "အကြီးအမှူးပြု", "အမြစ်ပြု", "မှီ၍", "သိ", "ပြနိုင်", "အဖန်ဖန်", "မြင်",
              "သတ်", "လိုလား", "လိုချင်", "မသိ", "ယူ", "ဝိုင်း", "ဖျက်ဆီး", "ဖောက်ထွင်း", "လုယူ", "ပြော", "ထွက်စေ",
              "စွဲယူ", "ဖြစ်ပေါ်စေ", "ဆောက်တည်", "စောင့်ထိန်း", "ပြု", "ဖြစ်စေ", "အားကြီးစွာ", "ထိုးထွင်း", "သာယာ",
              "ပြန်လည်", "ဝင်စား", "ခံစား", "ပူပန်", "သင်းခွဲ", "ဖြိုခွဲ", "အရင်းခံ", "ခွဲခြား", "ချေဖျက်")


def first_dat(b, d_items):
    fd = list(cc.DAT.finditer(b))
    return fd[-min(len(fd), d_items)] if fd and d_items else None


def core_start(b, upto):
    vb = [m.end() for m in re.finditer(r"(?:ကြ၏|ကြသည်|သည်)၊ ", b[:upto])]
    s = max(vb) if vb else 0
    while s < len(b) and b[s] in " ၊":
        s += 1
    return s


def propose(code, u, b):
    subj, dat = cc.split_unit(u)
    d_items = sum(cc.count_items(s) for s in cc.segments(dat)) if dat else 0
    fd = first_dat(b, d_items)
    s_items = cc.count_items(cc.segments(subj)[-1], gen_list=False) if subj else 0
    if fd is None and code == "D1":
        s0 = core_start(b, len(b))
        core = b[s0:]
        lk = [m for m in re.finditer(r"(?<!အား)လည်းကောင်း(၊ )?", core)]
        if len(lk) == s_items + d_items:
            out, pos = [], 0
            for i, m in enumerate(lk):
                out.append(core[pos:m.start()])
                if i == s_items - 1:
                    out.append("လည်းကောင်း ")
                elif i >= s_items:
                    out.append("အားလည်းကောင်း" + (m.group(1) or ""))
                else:
                    out.append(m.group(0))
                pos = m.end()
            out.append(core[pos:])
            return "K5", core, "".join(out)
    if fd is None:
        return None
    s0 = core_start(b, fd.start())
    core = b[s0:]
    nb_all = len(cc.DAT.findall(core))
    s_items = cc.count_items(cc.segments(subj)[-1], gen_list=False) if subj else 0
    if code == "S2":
        sm = [m for m in cc.SUBJ_MARK2.finditer(b) if m.end() <= fd.start()]
        m = sm[-1]
        old = b[s0:fd.end()]
        new = b[s0:m.start()] + "လည်းကောင်း " + b[m.end():fd.end()].lstrip()
        return "K4", old, new
    if code == "D1":
        # K5: subjects and recipients all written «…လည်းကောင်း» (no «အား»): the recipients take «အား»
        lk = [m for m in re.finditer(r"(?<!အား)လည်းကောင်း(၊ )?", core)]
        if len(lk) == s_items + d_items and not cc.DAT.findall(core):
            out, pos = [], 0
            for i, m in enumerate(lk):
                out.append(core[pos:m.start()])
                if i == s_items - 1:
                    out.append("လည်းကောင်း ")
                elif i >= s_items:
                    out.append("အားလည်းကောင်း" + (m.group(1) or ""))
                else:
                    out.append(m.group(0))
                pos = m.end()
            out.append(core[pos:])
            return "K5", core, "".join(out)
        return None
    if code not in ("S0", "D0"):
        return None
    # K2: one more «အား» item than the Pāli recipients and the first of them is the subject
    if nb_all == d_items + 1 and s_items == 1:
        m = next(cc.DAT.finditer(core))
        mm = re.match(r"အား(?:လည်းကောင်း)?၊? ", core[m.start():])
        if mm:
            new_core = core[:m.start()] + "သည် " + core[m.start() + mm.end():]
            rest = new_core[m.start() + len("သည် "):]
            if d_items == 1:
                rest2 = re.sub(r"အားလည်းကောင်း(?=\s*$|\s+\S+$|\s+\S+ \S+$)", "အား", rest, count=1)
                if cc.DAT.findall(rest2) and rest2.count("အားလည်းကောင်း") == 0:
                    rest = rest2
            new_core = new_core[:m.start() + len("သည် ")] + rest
            return "K2", core, new_core
    # K1: «ကို» marking the subject
    pre = core[:fd.start() - s0]
    kos = [m for m in re.finditer(r"(?<!သည်)ကို ", pre)]
    kos = [m for m in kos if not pre[m.end():].startswith(NP_KO_NEXT)]
    if kos and s_items == 1:
        m = kos[-1]
        new = pre[:m.start()] + "သည် " + pre[m.end():]
        return "K1", core, new + core[len(pre):]
    # K3: joined by «၊»
    cm = [m for m in re.finditer(r"၊ ", pre)]
    if cm and s_items == 1:
        m = cm[0]
        new = pre[:m.start()] + "သည် " + pre[m.end():]
        return "K3", core, new + core[len(pre):]
    return None


def main():
    n, rows = cc.run(FOLDER)
    out, seen = [], collections.Counter()
    manual = []
    done_units = set()
    for ch, k, code, pu, bu in rows:
        if (ch, k, pu, bu) in done_units and code in ("D0", "S0"):
            continue
        # rows carry the unit text; recompute the unit words from the Pāli unit text
        u = pu.split()
        r = propose(code, u, bu)
        if r is None:
            manual.append((ch, k, code, pu, bu[-200:]))
            continue
        rule, old, new = r
        done_units.add((ch, k, pu, bu))
        key = (rule, pu, old, new)
        seen[key] += 1
    with open(HERE / "case-proposals.tsv", "w", encoding="utf-8") as fh:
        fh.write("rule\tn\tpali_unit\told\tnew\n")
        for (rule, pu, old, new), c in seen.items():
            fh.write(f"{rule}\t{c}\t{pu}\t{old}\t{new}\n")
    with open(HERE / "case-manual.tsv", "w", encoding="utf-8") as fh:
        for r in manual:
            fh.write("\t".join(map(str, r)) + "\n")
    print(f"{n} clauses, {len(rows)} flagged; {sum(seen.values())} proposed ({len(seen)} distinct); "
          f"{len(manual)} by hand")


main()
