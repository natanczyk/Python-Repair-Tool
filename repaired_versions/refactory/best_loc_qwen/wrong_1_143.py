def search(x, seq):
    n = []
    seq = list(seq)
    a = seq.copy()
    d = -1
    if not seq:
        return 0
    for i in a:
        if i < x:
            n.append(i)
            seq.remove(i)
        elif i == x:
            n.append(i)
            n.append(x)
            n.extend(seq)
            break
        else:
            n.append(x)
            n.extend(seq)
            break
    if x in n:
        return n.index(x)
    else:
        return len(n)