import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru")
import build_10_12_ru as X
G, T, F, S, B, Z = X.G, X.T, X.F, X.S, X.B, X.Z
print([k for k in G.BODY if k.startswith("Yaṃ cittaṃ")])
for k in G.BODY:
    if k.startswith("Yaṃ cittaṃ"): print(G.BODY[k])
print(F.TAIL_SENT.get("phasso hoti…pe… avikkhepo hoti."))
print(T.enum(["a","b","c"]))
print(repr(S.CHAPTER_CLOSING), S.TATTHA, S.VUCCATI)
print(X.TENA, "|", X.called("доброжелательностью"))
print(G.when("kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha"))
print(G.LOK_V_SUNNA)
print(G.LOK_K)
print(T.how_many_q("четырёх безмерных состояний"))
print(G.CETANA)
import inspect
print(inspect.getsource(S.attach_ids)[:600])
