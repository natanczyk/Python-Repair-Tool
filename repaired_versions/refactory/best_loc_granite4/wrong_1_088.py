def search(x, seq):
    for i, value in enumerate(seq):
        if value >= x:
            return i
    return len(seq)