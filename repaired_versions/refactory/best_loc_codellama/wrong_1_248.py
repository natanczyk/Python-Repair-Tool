def search(x, seq):
    if not seq:
        return 0
    for i, item in enumerate(seq):
        if x == item:
            return i
        elif x < item:
            return i
    return len(seq)