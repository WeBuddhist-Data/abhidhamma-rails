def items_of(pk):
    """split stemmed slot into items; 'X ^ Y &' (X ceva Y ca) stays inside one item"""
    items, cur = [], []
    pending = False
    for t in pk.split():
        if t == '^':
            pending = True
            cur.append('^')
        elif t == '&':
            if pending:
                cur.append('&')
                pending = False
            else:
                if cur:
                    items.append(' '.join(cur))
                cur = []
        elif t != 'dhamm':
            cur.append(t)
    if cur:
        items.append(' '.join(cur))
    return items
