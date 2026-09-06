def search(x, seq):
    n = len(seq)
    if n == 0 or x <= seq[0]:
        return 0
    for counter in range(n):
        if x > seq[counter]:
            continue
        else:
            return counter
    return n