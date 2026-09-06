def search(x, seq):
    if not seq:
        return 0
    for i, value in enumerate(seq):
        if x <= value:
            return i
    return len(seq)