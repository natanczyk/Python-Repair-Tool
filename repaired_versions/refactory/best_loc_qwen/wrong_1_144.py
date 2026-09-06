def search(x, seq):
    seq = list(seq)
    if not seq:
        return 0
    a = seq.copy()
    n = []
    for i in a:
        if i < x:
            n.append(i)
        elif i == x:
            n.append(i)
            n.append(x)
            break
        else:
            n.append(x)
            break
    count = list(enumerate(n))
    for b in count:
        if b[1] == x:
            return b[0]
    return len(n)