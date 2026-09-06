def search(x, seq):
    n = len(seq)
    if n == 0:
        return 0
    for i in range(n):
        if x < seq[0]:
            return 0
        elif x <= seq[i] and x >= seq[i-1]:
            return i
        elif x > seq[n-1]:
            return n
    return -1