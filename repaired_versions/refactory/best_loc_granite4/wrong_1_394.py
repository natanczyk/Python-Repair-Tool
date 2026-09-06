def search(x, seq):
    seq = list(seq)  # Ensure seq is a list to handle tuples
    n = len(seq)
    if n == 0:
        return 0
    if x <= seq[0]:
        return 0
    for i in range(1, n):
        if x <= seq[i] and x > seq[i-1]:
            return i
    return n