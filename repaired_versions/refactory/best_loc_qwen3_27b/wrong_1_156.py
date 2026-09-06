def search(x, seq):
    for a, b in enumerate(seq):
        if x <= b:
            return a
    return len(seq)