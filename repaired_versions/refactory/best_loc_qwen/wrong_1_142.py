def search(x, seq):
    seq = list(seq)
    for i, val in enumerate(seq):
        if val >= x:
            return i
    return len(seq)