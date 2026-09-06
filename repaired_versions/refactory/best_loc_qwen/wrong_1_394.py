def search(x, seq):
    n = len(seq)
    if n == 0:
        return 0
    for i in range(n):
        if x <= seq[i]:
            return i
    return n