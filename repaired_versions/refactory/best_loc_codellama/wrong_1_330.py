def search(x, seq):
    for i, item in enumerate(seq):
        if x <= item:
            return i
    return len(seq)