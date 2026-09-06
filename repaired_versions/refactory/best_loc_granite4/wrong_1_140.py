def search(x, seq):
    for i, val in enumerate(seq):
        if val >= x:
            return i
    return len(seq)