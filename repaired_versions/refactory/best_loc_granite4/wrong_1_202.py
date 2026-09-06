def search(x, seq):
    l = len(seq)
    if l == 0:
        return 0
    if x <= seq[0]:
        return 0
    for i in range(l - 1):
        if seq[i] <= x <= seq[i + 1]:
            return i + 1
    return l