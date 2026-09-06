def search(x, seq):
    for i, y in enumerate(seq):
        if x <= y:
            return i
    return len(seq)