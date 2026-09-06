def search(x, seq):
    for i, v in enumerate(seq):
        if v >= x:
            return i
    return len(seq)