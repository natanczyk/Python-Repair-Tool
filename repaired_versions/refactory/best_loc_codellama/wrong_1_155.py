def search(x, seq):
    if not seq:
        return 0
    for i, b in enumerate(seq):
        if x <= b:
            return i
    return len(seq)