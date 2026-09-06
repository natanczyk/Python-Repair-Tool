def search(x, seq):
    if not seq:
        return 0
    for i, item in enumerate(seq):
        if item == x:
            return i
        elif item > x:
            return i
    return len(seq)