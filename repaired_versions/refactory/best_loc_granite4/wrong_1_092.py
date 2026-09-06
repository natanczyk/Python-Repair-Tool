def search(x, seq):
    if not seq:
        return 0
    for i, value in enumerate(seq):
        if value >= x:
            return i
    return len(seq)