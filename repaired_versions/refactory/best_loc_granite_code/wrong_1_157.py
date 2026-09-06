def search(x, seq):
    if not seq:
        return 0
    for a,b in enumerate(seq):
        if x <= b:
            return a
    return a + 1