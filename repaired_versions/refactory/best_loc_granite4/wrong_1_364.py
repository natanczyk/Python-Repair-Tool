def search(x, seq):
    if len(seq) == 0:
        return 0
    for i, val in enumerate(seq):
        if x <= val:
            return i
    return len(seq)