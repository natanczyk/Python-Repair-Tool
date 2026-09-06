def search(x, seq):
    if not seq:
        return 0
    for i in seq:
        if x <= i:
            return seq.index(i)
    return len(seq)