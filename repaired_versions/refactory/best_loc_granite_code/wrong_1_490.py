def search(x, seq):
    l = len(seq)
    if l == 0:
        return 0
    for i in range(l):
        if x <= seq[i]:
            return i
    return l