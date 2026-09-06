def search(x, seq):
    for i, b in enumerate(seq):
        if x <= b:
            return i
    return len(seq)