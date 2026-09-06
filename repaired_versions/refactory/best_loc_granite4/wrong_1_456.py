def search(x, seq):
    if not seq:
        return 0
    for i, val in enumerate(seq):
        if x <= val:
            return i
    return len(seq)