def search(x, seq):
    n = len(seq)
    for i in range(n):
        if x <= seq[i]:
            return i
    return n