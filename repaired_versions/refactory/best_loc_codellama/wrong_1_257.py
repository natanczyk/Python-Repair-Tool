def search(x, seq):
    if not seq:
        return 0
    for i, v in enumerate(seq):
        if x <= v:
            return i
    return len(seq)