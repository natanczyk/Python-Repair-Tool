def search(x, seq):
    for i, value in enumerate(seq):
        if x <= value:
            return i
    return len(seq)