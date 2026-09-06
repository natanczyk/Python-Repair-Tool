def search(x, seq):
    if not seq:
        return 0
    if x < 0:
        return 0
    for i, val in enumerate(seq):
        if val >= x:
            return i
    return len(seq)