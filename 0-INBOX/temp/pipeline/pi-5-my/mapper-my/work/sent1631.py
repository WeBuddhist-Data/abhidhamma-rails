"""sentence split of a Pāli / Burmese segment (for the look helper)."""
import re
def pali_sents(t):
    t = re.sub(r"\s*\[[^\]]*\]", "", t)
    t = t.replace("…pe…", "…pe…\x00")
    parts = re.split(r"(?<=[?.!])\s+|\x00\s*", t)
    return [p.strip() for p in parts if p.strip() and p.strip() not in (".", "…")]
def my_sents(t):
    t = re.sub(r"\s*\[[^\]]*\]", "", t)
    parts = re.split(r"(?<=[။?])\s*|(?<=…)\s+", t)
    return [p.strip() for p in parts if p.strip() and p.strip() not in ("။", "…")]
import math
def align(a, b, r=None):
    """Gale-Church-like DP: -> list of (pāli idx list, burmese idx list)."""
    if not a or not b:
        return [(list(range(len(a))), list(range(len(b))))]
    la, lb = [len(x) for x in a], [len(x) for x in b]
    r = r or (sum(lb) / max(1, sum(la)))
    INF = float("inf")
    n, m = len(a), len(b)
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    beads = [(1, 1, 0), (1, 2, 1.5), (2, 1, 1.5), (1, 0, 4), (0, 1, 4), (2, 2, 2.5), (1, 3, 3), (3, 1, 3)]
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] == INF: continue
            for di, dj, pen in beads:
                ii, jj = i + di, j + dj
                if ii > n or jj > m: continue
                sa, sb = sum(la[i:ii]), sum(lb[j:jj])
                c = abs(math.log((sb + 8) / (r * sa + 8))) * 3 + pen
                if D[i][j] + c < D[ii][jj]:
                    D[ii][jj] = D[i][j] + c; B[ii][jj] = (i, j)
    out, i, j = [], n, m
    while (i, j) != (0, 0):
        pi_, pj = B[i][j]
        out.append((list(range(pi_, i)), list(range(pj, j))))
        i, j = pi_, pj
    return out[::-1]
