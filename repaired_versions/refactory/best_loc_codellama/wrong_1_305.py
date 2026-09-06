def search(x, seq):
    for i, v in enumerate(seq):
        if x <= v:
            return i
    return len(seq)