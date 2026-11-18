"""Helper for chapter 4-01: print the earlier builders' strings this chapter reuses (writes nothing)."""
import importlib.util
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-vi-ai\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_vi as S  # noqa: E402

_spec = importlib.util.spec_from_file_location("build_rails_3_02_3_03_vi", HERE / "build_rails_3-02_3-03_vi.py")
Q = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(Q)
R = Q.R
E, D, T, B = R.E, R.D, R.T, R.B
print("KIRIYA_V:", E.KIRIYA_V)
print("U583:", R.U583_V)
print("VINN:", R.VINN)
print("qpred:", Q.qpred("anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ"))
print("SAB_DEF:", R.SAB_DEF)
print("DITTHI_V:", D.DITTHI_V)
for k in sys.argv[1:]:
    print(k, "=>", S.PREDS.get(k))
